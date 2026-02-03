#!/usr/bin/env python3
"""
Build search indexes for policy documents.

Creates:
- BM25 index (lexical search)
- ChromaDB vector store (semantic search)
- Knowledge graph (GraphRAG)

Usage:
    python run_indexing.py              # Build all indexes
    python run_indexing.py --test       # Test search after building
    python run_indexing.py --no-graph   # Skip graph building
    python run_indexing.py --no-vector  # Skip vector embeddings
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Load environment variables
load_dotenv()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Build search indexes for policies")
    parser.add_argument("--test", action="store_true", help="Test search after building")
    parser.add_argument("--no-graph", action="store_true", help="Skip building knowledge graph")
    parser.add_argument("--no-vector", action="store_true", help="Skip building vector embeddings")
    parser.add_argument("--model", default="text-embedding-3-small",
                        help="Embedding model (default: text-embedding-3-small)")

    args = parser.parse_args()

    # Check for API key (needed for embeddings)
    if not args.no_vector and not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY not set")
        print("\nSet it with: export OPENAI_API_KEY=sk-your-key")
        print("Or create a .env file with: OPENAI_API_KEY=sk-your-key")
        print("\nOr use --no-vector to skip embedding generation")
        sys.exit(1)

    project_root = Path(__file__).parent
    markdown_dir = project_root / "data" / "policies_md"
    index_dir = project_root / "data" / "indexes"

    # Check if markdown files exist
    md_files = list(markdown_dir.glob("*.md"))
    if not md_files:
        print(f"[ERROR] No markdown files found in {markdown_dir}")
        print("Run `python run_conversion.py` first to convert PDFs")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files")
    print(f"Building indexes in {index_dir}")
    print()

    # Import here to avoid ChromaDB/rank_bm25 conflict at module level
    from indexing.markdown_parser import parse_all_markdown_files
    from indexing.index_builder import BM25Index, VectorStore, create_chunks_from_documents

    print("=" * 60)
    print("PARSING DOCUMENTS")
    print("=" * 60)
    docs = parse_all_markdown_files(markdown_dir)
    print(f"\nParsed {len(docs)} documents")

    print("\n" + "=" * 60)
    print("CREATING CHUNKS")
    print("=" * 60)
    chunks = create_chunks_from_documents(docs)
    print(f"Created {len(chunks)} chunks")

    # Build BM25 index
    print("\n" + "=" * 60)
    print("BUILDING BM25 INDEX")
    print("=" * 60)
    bm25_index = BM25Index()
    bm25_index.build(chunks)
    bm25_index.save(index_dir / "bm25_index.pkl")
    print("[OK] BM25 index saved")

    # Build ChromaDB vector store
    vector_store = None
    if not args.no_vector:
        print("\n" + "=" * 60)
        print("BUILDING CHROMADB VECTOR STORE")
        print("=" * 60)
        print("This may take a few minutes...")

        vector_store = VectorStore(index_dir / "chromadb")
        vector_store.initialize()
        vector_store.build(chunks, embedding_model=args.model)
        print(f"[OK] ChromaDB vector store saved ({vector_store.collection.count()} entries)")

    # Build knowledge graph for GraphRAG
    if not args.no_graph:
        print("\n" + "=" * 60)
        print("BUILDING KNOWLEDGE GRAPH (GraphRAG)")
        print("=" * 60)

        from indexing.graph_builder import build_knowledge_graph
        builder = build_knowledge_graph(markdown_dir, index_dir)

        stats = builder.get_stats()
        print(f"\nGraph Statistics:")
        print(f"   Nodes: {stats.total_nodes}")
        print(f"   Edges: {stats.total_edges}")
        print(f"\n   Node types:")
        for node_type, count in sorted(stats.nodes_by_type.items()):
            print(f"     {node_type}: {count}")

        print("\n[OK] Knowledge graph saved")

    print("\n" + "=" * 60)
    print("INDEXING COMPLETE!")
    print("=" * 60)

    # Test search if requested
    if args.test:
        print("\n" + "=" * 60)
        print("TESTING SEARCH")
        print("=" * 60)

        test_query = "multi-factor authentication for privileged access"
        print(f"\nTest query: '{test_query}'\n")

        # BM25 results
        print("--- BM25 Results ---")
        bm25_results = bm25_index.search(test_query, top_k=3)
        for chunk, score in bm25_results:
            print(f"  [{chunk.section_id}] {chunk.section_title}")
            print(f"    Score: {score:.2f}")
            print()

        # Vector results
        if vector_store:
            print("--- Vector Search Results ---")
            vector_results = vector_store.search(test_query, top_k=3)
            for result in vector_results:
                print(f"  [{result['metadata']['section_id']}] {result['metadata']['section_title']}")
                print(f"    Similarity: {result['similarity']:.3f}")
                print()


if __name__ == "__main__":
    main()
