"""
Index Builder for Policy Documents

Creates:
1. BM25 index for lexical/keyword search
2. ChromaDB vector store for semantic search
"""

import os
import json
import pickle
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional

from rank_bm25 import BM25Okapi
import chromadb
from chromadb.config import Settings

from .markdown_parser import ParsedDocument, Section, parse_all_markdown_files


@dataclass
class IndexedChunk:
    """Represents a chunk ready for indexing."""
    chunk_id: str
    document_id: str
    document_title: str
    section_id: str
    section_title: str
    section_path: str
    content: str
    content_for_embedding: str
    level: int
    compliance_relevance: Optional[str]
    likely_maps_to: list[str]
    entities: dict

    def to_metadata(self) -> dict:
        """Convert to metadata dict for ChromaDB."""
        return {
            "document_id": self.document_id,
            "document_title": self.document_title,
            "section_id": self.section_id,
            "section_title": self.section_title,
            "section_path": self.section_path,
            "level": self.level,
            "compliance_relevance": self.compliance_relevance or "",
            "likely_maps_to": json.dumps(self.likely_maps_to),
            "entities": json.dumps(self.entities)
        }


def create_chunks_from_documents(documents: list[ParsedDocument]) -> list[IndexedChunk]:
    """
    Create indexable chunks from parsed documents.

    Each section becomes a chunk. Very short sections are skipped.
    """
    chunks = []
    min_content_length = 50  # Skip very short sections
    seen_ids = set()  # Track IDs to ensure uniqueness

    for doc in documents:
        section_counter = 0
        for section in doc.sections:
            content = section.get_full_text()

            # Skip very short or empty sections
            if len(content.strip()) < min_content_length:
                continue

            section_counter += 1

            # Generate unique chunk_id
            base_chunk_id = f"{doc.document_id}_{section.section_id}"

            # Ensure uniqueness by adding counter if needed
            chunk_id = base_chunk_id
            counter = 1
            while chunk_id in seen_ids:
                chunk_id = f"{base_chunk_id}_{counter}"
                counter += 1
            seen_ids.add(chunk_id)

            chunk = IndexedChunk(
                chunk_id=chunk_id,
                document_id=doc.document_id,
                document_title=doc.title,
                section_id=section.section_id,
                section_title=section.title,
                section_path=section.section_path,
                content=content,
                content_for_embedding=section.get_text_for_embedding(),
                level=section.level,
                compliance_relevance=section.compliance_relevance,
                likely_maps_to=section.likely_maps_to,
                entities=section.entities
            )
            chunks.append(chunk)

    return chunks


class BM25Index:
    """BM25 index for lexical search."""

    def __init__(self):
        self.bm25: Optional[BM25Okapi] = None
        self.chunks: list[IndexedChunk] = []
        self.tokenized_corpus: list[list[str]] = []

    def build(self, chunks: list[IndexedChunk]):
        """Build BM25 index from chunks."""
        self.chunks = chunks

        # Tokenize corpus
        self.tokenized_corpus = [
            self._tokenize(chunk.content)
            for chunk in chunks
        ]

        # Build BM25 index
        self.bm25 = BM25Okapi(self.tokenized_corpus)

        print(f"BM25 index built with {len(chunks)} chunks")

    def _tokenize(self, text: str) -> list[str]:
        """Simple tokenization - lowercase and split."""
        # Lowercase
        text = text.lower()
        # Remove special chars but keep alphanumeric and spaces
        text = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text)
        # Split and filter empty
        tokens = [t for t in text.split() if len(t) > 1]
        return tokens

    def search(self, query: str, top_k: int = 10) -> list[tuple[IndexedChunk, float]]:
        """
        Search the BM25 index.

        Returns:
            List of (chunk, score) tuples sorted by relevance
        """
        if self.bm25 is None:
            raise ValueError("Index not built. Call build() first.")

        tokenized_query = self._tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)

        # Get top-k results
        scored_chunks = list(zip(self.chunks, scores))
        scored_chunks.sort(key=lambda x: x[1], reverse=True)

        return scored_chunks[:top_k]

    def save(self, filepath: str | Path):
        """Save index to disk."""
        filepath = Path(filepath)
        data = {
            "chunks": [asdict(c) for c in self.chunks],
            "tokenized_corpus": self.tokenized_corpus
        }
        with open(filepath, "wb") as f:
            pickle.dump(data, f)
        print(f"BM25 index saved to {filepath}")

    def load(self, filepath: str | Path):
        """Load index from disk."""
        filepath = Path(filepath)
        with open(filepath, "rb") as f:
            data = pickle.load(f)

        self.chunks = [IndexedChunk(**c) for c in data["chunks"]]
        self.tokenized_corpus = data["tokenized_corpus"]
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        print(f"BM25 index loaded: {len(self.chunks)} chunks")


class VectorStore:
    """ChromaDB vector store for semantic search."""

    def __init__(self, persist_directory: str | Path, collection_name: str = "policies"):
        self.persist_directory = Path(persist_directory)
        self.collection_name = collection_name
        self.client: Optional[chromadb.Client] = None
        self.collection = None

    def initialize(self):
        """Initialize ChromaDB client and collection."""
        self.persist_directory.mkdir(parents=True, exist_ok=True)

        self.client = chromadb.PersistentClient(
            path=str(self.persist_directory),
            settings=Settings(anonymized_telemetry=False)
        )

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}  # Use cosine similarity
        )

        print(f"ChromaDB initialized at {self.persist_directory}")

    def build(self, chunks: list[IndexedChunk], embedding_model: str = "text-embedding-3-small"):
        """
        Build vector store from chunks.

        Uses OpenAI embeddings by default.
        """
        if self.collection is None:
            self.initialize()

        # Clear existing data
        existing = self.collection.count()
        if existing > 0:
            print(f"Clearing {existing} existing items...")
            # Get all IDs and delete
            all_ids = self.collection.get()["ids"]
            if all_ids:
                self.collection.delete(ids=all_ids)

        print(f"Building vector store with {len(chunks)} chunks...")

        # Prepare data for ChromaDB
        ids = [chunk.chunk_id for chunk in chunks]
        documents = [chunk.content_for_embedding for chunk in chunks]
        metadatas = [chunk.to_metadata() for chunk in chunks]

        # Add in batches (ChromaDB handles embedding internally if configured,
        # but we'll use OpenAI embeddings explicitly for better control)
        batch_size = 100

        # Get embeddings from OpenAI
        from openai import OpenAI
        client = OpenAI()

        all_embeddings = []
        for i in range(0, len(documents), batch_size):
            batch_docs = documents[i:i + batch_size]
            print(f"  Embedding batch {i // batch_size + 1}/{(len(documents) - 1) // batch_size + 1}...")

            response = client.embeddings.create(
                model=embedding_model,
                input=batch_docs
            )

            batch_embeddings = [e.embedding for e in response.data]
            all_embeddings.extend(batch_embeddings)

        # Add to collection
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=all_embeddings,
            metadatas=metadatas
        )

        print(f"Vector store built with {len(chunks)} chunks")

    def search(
        self,
        query: str,
        top_k: int = 10,
        embedding_model: str = "text-embedding-3-small",
        where: Optional[dict] = None
    ) -> list[dict]:
        """
        Search the vector store.

        Args:
            query: Search query
            top_k: Number of results
            embedding_model: Model for query embedding
            where: Optional filter conditions

        Returns:
            List of results with metadata and distances
        """
        if self.collection is None:
            self.initialize()

        # Get query embedding
        from openai import OpenAI
        client = OpenAI()

        response = client.embeddings.create(
            model=embedding_model,
            input=[query]
        )
        query_embedding = response.data[0].embedding

        # Search
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where,
            include=["documents", "metadatas", "distances"]
        )

        # Format results
        formatted = []
        for i in range(len(results["ids"][0])):
            formatted.append({
                "chunk_id": results["ids"][0][i],
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
                "similarity": 1 - results["distances"][0][i]  # Convert distance to similarity
            })

        return formatted

    def search_with_embedding(
        self,
        embedding: list[float],
        top_k: int = 10,
        where: Optional[dict] = None
    ) -> list[dict]:
        """Search with a pre-computed embedding (for HyDE)."""
        if self.collection is None:
            self.initialize()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            where=where,
            include=["documents", "metadatas", "distances"]
        )

        formatted = []
        for i in range(len(results["ids"][0])):
            formatted.append({
                "chunk_id": results["ids"][0][i],
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
                "similarity": 1 - results["distances"][0][i]
            })

        return formatted


def build_all_indexes(
    markdown_dir: str | Path,
    index_dir: str | Path,
    embedding_model: str = "text-embedding-3-small"
) -> tuple[BM25Index, VectorStore, list[IndexedChunk]]:
    """
    Build all indexes from markdown files.

    Args:
        markdown_dir: Directory containing markdown policy files
        index_dir: Directory to save indexes
        embedding_model: OpenAI embedding model to use

    Returns:
        Tuple of (bm25_index, vector_store, chunks)
    """
    markdown_dir = Path(markdown_dir)
    index_dir = Path(index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)

    # Parse all documents
    print("\n=== Parsing Markdown Files ===")
    documents = parse_all_markdown_files(markdown_dir)
    print(f"Parsed {len(documents)} documents")

    # Create chunks
    print("\n=== Creating Chunks ===")
    chunks = create_chunks_from_documents(documents)
    print(f"Created {len(chunks)} chunks")

    # Save chunks metadata
    chunks_meta_path = index_dir / "chunks_metadata.json"
    chunks_data = [asdict(c) for c in chunks]
    with open(chunks_meta_path, "w", encoding="utf-8") as f:
        json.dump(chunks_data, f, indent=2, ensure_ascii=False)
    print(f"Chunks metadata saved to {chunks_meta_path}")

    # Build BM25 index
    print("\n=== Building BM25 Index ===")
    bm25_index = BM25Index()
    bm25_index.build(chunks)
    bm25_index.save(index_dir / "bm25_index.pkl")

    # Build vector store
    print("\n=== Building Vector Store ===")
    vector_store = VectorStore(index_dir / "chromadb")
    vector_store.initialize()
    vector_store.build(chunks, embedding_model)

    print("\n=== Indexing Complete ===")
    print(f"Total documents: {len(documents)}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Index directory: {index_dir}")

    return bm25_index, vector_store, chunks


# CLI
if __name__ == "__main__":
    import sys

    # Default paths
    project_root = Path(__file__).parent.parent.parent
    markdown_dir = project_root / "data" / "policies_md"
    index_dir = project_root / "data" / "indexes"

    if len(sys.argv) > 1:
        markdown_dir = Path(sys.argv[1])
    if len(sys.argv) > 2:
        index_dir = Path(sys.argv[2])

    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set")
        sys.exit(1)

    build_all_indexes(markdown_dir, index_dir)
