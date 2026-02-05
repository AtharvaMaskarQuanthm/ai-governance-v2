"""
Hybrid Retriever for Compliance Mapping

Combines:
1. BM25 (lexical search) - for exact keyword matches
2. Vector search (semantic) - for meaning-based similarity
3. HyDE (Hypothetical Document Embedding) - bridges regulation ↔ policy language
4. GraphRAG (knowledge graph) - entity-based expansion

Uses Reciprocal Rank Fusion (RRF) to combine results.
"""

import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from openai import OpenAI

# Add parent to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from indexing.index_builder import BM25Index, VectorStore
from indexing.graph_builder import KnowledgeGraphBuilder


@dataclass
class RetrievalResult:
    """A single retrieval result."""
    chunk_id: str
    document_id: str
    document_title: str
    section_id: str
    section_title: str
    section_path: str
    content: str
    score: float
    sources: list[str]  # Which retrievers found this: ["bm25", "vector", "hyde", "graph"]
    # Metadata preserved from IndexedChunk
    entities: dict = None                          # from IndexedChunk.entities
    compliance_relevance: Optional[str] = None     # HIGH/MEDIUM/LOW
    likely_maps_to: list[str] = None               # regulatory frameworks
    level: int = 0                                 # heading level 1-6
    retriever_scores: dict = None                  # {"bm25": 0.8, "vector": 0.6, ...}

    def __post_init__(self):
        if self.entities is None:
            self.entities = {}
        if self.likely_maps_to is None:
            self.likely_maps_to = []
        if self.retriever_scores is None:
            self.retriever_scores = {}


HYDE_SYSTEM_PROMPT = """You are an expert compliance officer at a financial services organization in India.
You write internal security policies that address regulatory requirements from SEBI, ISO 27001, and CERT-IN.

Given a regulatory requirement, write a SHORT hypothetical internal policy section (2-3 sentences) that would address this requirement.

Use this style:
- Start with "The organization shall..." or "[[role:Information Security Team]] shall..."
- Be specific about controls and responsibilities
- Use formal policy language

Output ONLY the hypothetical policy text, nothing else."""


class HybridRetriever:
    """
    Hybrid retriever combining BM25, Vector, HyDE, and GraphRAG search.
    """

    def __init__(
        self,
        bm25_index: BM25Index,
        vector_store: Optional[VectorStore] = None,
        graph_builder: Optional[KnowledgeGraphBuilder] = None,
        openai_client: Optional[OpenAI] = None,
        embedding_model: str = "text-embedding-3-small",
        hyde_model: str = "gpt-4o-mini"
    ):
        self.bm25_index = bm25_index
        self.vector_store = vector_store
        self.graph_builder = graph_builder
        self.graph_retriever = None
        self.client = openai_client or OpenAI()
        self.embedding_model = embedding_model
        self.hyde_model = hyde_model

        # Initialize graph retriever if graph builder provided
        if graph_builder:
            from .graph_retriever import GraphRetriever
            self.graph_retriever = GraphRetriever(graph_builder)

    def _generate_hypothetical_document(self, query: str) -> str:
        """Generate a hypothetical policy section using HyDE."""
        response = self.client.chat.completions.create(
            model=self.hyde_model,
            messages=[
                {"role": "system", "content": HYDE_SYSTEM_PROMPT},
                {"role": "user", "content": f"Regulatory requirement:\n{query}"}
            ],
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content

    def _get_embedding(self, text: str) -> list[float]:
        """Get embedding for text."""
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=[text]
        )
        return response.data[0].embedding

    def _reciprocal_rank_fusion(
        self,
        result_lists: list[list[tuple[str, float, str]]],
        k: int = 60
    ) -> list[tuple[str, float, list[str], dict]]:
        """
        Combine results using Reciprocal Rank Fusion.

        Args:
            result_lists: List of [(chunk_id, score, source), ...] for each retriever
            k: RRF parameter (higher = less impact from rank differences)

        Returns:
            List of (chunk_id, fused_score, sources, retriever_scores) sorted by score
        """
        fused_scores = {}
        chunk_sources = {}
        chunk_retriever_scores = {}

        for result_list in result_lists:
            for rank, (chunk_id, score, source) in enumerate(result_list):
                if chunk_id not in fused_scores:
                    fused_scores[chunk_id] = 0
                    chunk_sources[chunk_id] = []
                    chunk_retriever_scores[chunk_id] = {}

                fused_scores[chunk_id] += 1 / (k + rank + 1)
                if source not in chunk_sources[chunk_id]:
                    chunk_sources[chunk_id].append(source)
                chunk_retriever_scores[chunk_id][source] = round(score, 4)

        # Sort by fused score
        results = [
            (chunk_id, score, chunk_sources[chunk_id], chunk_retriever_scores[chunk_id])
            for chunk_id, score in fused_scores.items()
        ]
        results.sort(key=lambda x: x[1], reverse=True)

        return results

    def search(
        self,
        query: str,
        top_k: int = 10,
        use_bm25: bool = True,
        use_vector: bool = True,
        use_hyde: bool = True,
        use_graph: bool = True,
        per_retriever_k: int = 20,
        graph_max_hops: int = 2
    ) -> list[RetrievalResult]:
        """
        Perform hybrid search.

        Args:
            query: The regulatory requirement or search query
            top_k: Number of final results to return
            use_bm25: Whether to use BM25 search
            use_vector: Whether to use direct vector search
            use_hyde: Whether to use HyDE
            use_graph: Whether to use GraphRAG expansion
            per_retriever_k: Results to fetch from each retriever before fusion
            graph_max_hops: Maximum hops for graph traversal

        Returns:
            List of RetrievalResult objects
        """
        result_lists = []

        # 1. BM25 Search
        if use_bm25:
            bm25_results = self.bm25_index.search(query, top_k=per_retriever_k)
            bm25_list = [
                (chunk.chunk_id, score, "bm25")
                for chunk, score in bm25_results
            ]
            result_lists.append(bm25_list)

        # 2. Direct Vector Search (requires vector_store)
        if use_vector and self.vector_store:
            vector_results = self.vector_store.search(query, top_k=per_retriever_k)
            vector_list = [
                (r["chunk_id"], r["similarity"], "vector")
                for r in vector_results
            ]
            result_lists.append(vector_list)

        # 3. HyDE Search (requires vector_store)
        if use_hyde and self.vector_store:
            # Generate hypothetical document
            hyde_doc = self._generate_hypothetical_document(query)

            # Embed the hypothetical document
            hyde_embedding = self._get_embedding(hyde_doc)

            # Search with hypothetical embedding
            hyde_results = self.vector_store.search_with_embedding(
                hyde_embedding, top_k=per_retriever_k
            )
            hyde_list = [
                (r["chunk_id"], r["similarity"], "hyde")
                for r in hyde_results
            ]
            result_lists.append(hyde_list)

        # First fusion pass (before graph expansion)
        fused = self._reciprocal_rank_fusion(result_lists)

        # 4. GraphRAG Expansion
        if use_graph and self.graph_retriever:
            # Get initial section IDs from top results
            initial_section_ids = [
                self._chunk_id_to_section_id(chunk_id)
                for chunk_id, _, _, _ in fused[:per_retriever_k]
            ]

            # Expand via graph
            expanded = self.graph_retriever.expand_results(
                initial_section_ids,
                query=query,
                max_hops=graph_max_hops,
                max_expansion=per_retriever_k
            )

            # Convert graph results to the same format
            # Section ID → chunk ID lookup
            section_to_chunk = {}
            for chunk in self.bm25_index.chunks:
                if chunk.section_id not in section_to_chunk:
                    section_to_chunk[chunk.section_id] = chunk.chunk_id

            graph_list = []
            for exp in expanded:
                chunk_id = section_to_chunk.get(exp.section_id)
                if chunk_id:
                    # Score based on relevance (normalize to 0-1 range)
                    score = min(exp.relevance_score / 3.0, 1.0)
                    graph_list.append((chunk_id, score, "graph"))

            if graph_list:
                result_lists.append(graph_list)

                # Re-fuse with graph results
                fused = self._reciprocal_rank_fusion(result_lists)

        # Build chunk lookup from BM25 index (has full chunk data)
        chunk_lookup = {chunk.chunk_id: chunk for chunk in self.bm25_index.chunks}

        # Build final results
        results = []
        for chunk_id, score, sources, ret_scores in fused[:top_k]:
            chunk = chunk_lookup.get(chunk_id)
            if chunk:
                results.append(RetrievalResult(
                    chunk_id=chunk_id,
                    document_id=chunk.document_id,
                    document_title=chunk.document_title,
                    section_id=chunk.section_id,
                    section_title=chunk.section_title,
                    section_path=chunk.section_path,
                    content=chunk.content,
                    score=score,
                    sources=sources,
                    entities=chunk.entities if chunk.entities else {},
                    compliance_relevance=chunk.compliance_relevance,
                    likely_maps_to=chunk.likely_maps_to if chunk.likely_maps_to else [],
                    level=chunk.level,
                    retriever_scores=ret_scores,
                ))

        return results

    def _chunk_id_to_section_id(self, chunk_id: str) -> str:
        """Extract section ID from chunk ID."""
        for chunk in self.bm25_index.chunks:
            if chunk.chunk_id == chunk_id:
                return chunk.section_id
        return chunk_id


def load_retriever(index_dir: str | Path, load_graph: bool = True) -> HybridRetriever:
    """
    Load a HybridRetriever from saved indexes.

    Args:
        index_dir: Directory containing bm25_index.pkl, chromadb/, and knowledge_graph.pkl
        load_graph: Whether to load the knowledge graph for GraphRAG

    Returns:
        Initialized HybridRetriever
    """
    index_dir = Path(index_dir)

    # Load BM25 index
    bm25_index = BM25Index()
    bm25_index.load(index_dir / "bm25_index.pkl")

    # Load vector store (ChromaDB)
    vector_store = None
    chromadb_path = index_dir / "chromadb"
    if chromadb_path.exists():
        try:
            print("Loading ChromaDB vector store...")
            vector_store = VectorStore(chromadb_path)
            vector_store.initialize()
            if vector_store.collection.count() == 0:
                print("[WARNING] ChromaDB collection is empty. Vector search disabled.")
                vector_store = None
        except Exception as e:
            print(f"[WARNING] ChromaDB failed to load: {e}")
            print("         Vector search and HyDE disabled.")
            vector_store = None
    else:
        print("[WARNING] ChromaDB not found. Vector search and HyDE disabled.")
        print("         Run `python run_indexing.py` to build it.")

    # Optionally load knowledge graph
    graph_builder = None
    if load_graph and (index_dir / "knowledge_graph.pkl").exists():
        print("Loading knowledge graph for GraphRAG...")
        graph_builder = KnowledgeGraphBuilder.load(index_dir)

    return HybridRetriever(bm25_index, vector_store, graph_builder=graph_builder)


# CLI for testing
if __name__ == "__main__":
    import sys

    project_root = Path(__file__).parent.parent.parent
    index_dir = project_root / "data" / "indexes"

    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set")
        sys.exit(1)

    print("Loading retriever (with all 4 methods)...")
    retriever = load_retriever(index_dir, load_graph=True)

    print(f"\nComponents loaded:")
    print(f"  - BM25: {len(retriever.bm25_index.chunks)} chunks")
    print(f"  - Vector: {'YES' if retriever.vector_store else 'NO'}")
    print(f"  - HyDE: {'YES' if retriever.vector_store else 'NO'}")
    print(f"  - GraphRAG: {'YES' if retriever.graph_retriever else 'NO'}")

    # Test query
    query = "Organizations shall implement multi-factor authentication for privileged access"

    print(f"\nQuery: {query}\n")
    print("Searching with BM25 + Vector + HyDE + GraphRAG...")

    results = retriever.search(query, top_k=5, use_graph=True)

    print(f"\nTop {len(results)} results:\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. [{r.section_id}] {r.section_title}")
        print(f"   Document: {r.document_title}")
        print(f"   Score: {r.score:.4f} (sources: {', '.join(r.sources)})")
        print(f"   Preview: {r.content[:150]}...")
        print()
