#!/usr/bin/env python3
"""
Compliance Query Interface

Paste a SEBI CSCRF requirement and find where it's covered in your policies.

Usage:
    python run_query.py                     # Interactive mode
    python run_query.py "requirement text"  # Single query
    python run_query.py --file reqs.txt     # Process file of requirements
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Load environment variables
load_dotenv()


def check_setup():
    """Check that everything is set up correctly."""
    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY not set")
        print("Set it with: export OPENAI_API_KEY=sk-your-key")
        sys.exit(1)

    index_dir = Path(__file__).parent / "data" / "indexes"
    if not (index_dir / "bm25_index.pkl").exists():
        print("[ERROR] Indexes not found")
        print("Run `python run_indexing.py` first")
        sys.exit(1)


def load_mapper(use_expand: bool = True):
    """Load the compliance mapper."""
    from retrieval.hybrid_retriever import load_retriever
    from retrieval.compliance_mapper import ComplianceMapper
    from retrieval.requirement_expander import RequirementExpander

    index_dir = Path(__file__).parent / "data" / "indexes"

    print("Loading indexes...")
    retriever = load_retriever(index_dir)

    expander = None
    if use_expand:
        expander = RequirementExpander()
        print("Requirement expansion enabled.")

    mapper = ComplianceMapper(retriever, expander=expander)
    print("[OK] Ready!\n")

    return mapper


def interactive_mode(mapper, use_hyde: bool = True, use_expand: bool = True):
    """Interactive query mode."""
    from retrieval.compliance_mapper import format_compliance_result

    print("="*70)
    print("COMPLIANCE MAPPING INTERFACE")
    print("="*70)
    print("Paste a regulatory requirement and press Enter twice to search.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        print("-"*70)
        print("Enter requirement (or 'quit'):")

        # Collect multi-line input
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break

            if line.lower() in ['quit', 'exit']:
                print("\nGoodbye!")
                return

            if line == "" and lines:
                break
            lines.append(line)

        requirement = "\n".join(lines).strip()

        if not requirement:
            continue

        if requirement.lower() in ['quit', 'exit']:
            print("\nGoodbye!")
            return

        print("\n[SEARCHING...]\n")

        try:
            result = mapper.map_requirement(
                requirement, top_k=10, use_hyde=use_hyde, use_expand=use_expand
            )
            print(format_compliance_result(result, verbose=True))
        except Exception as e:
            print(f"[ERROR] {e}")


def single_query(mapper, requirement: str, use_hyde: bool = True, use_expand: bool = True):
    """Process a single query."""
    from retrieval.compliance_mapper import format_compliance_result

    print(f"[SEARCHING] {requirement[:100]}...")
    result = mapper.map_requirement(
        requirement, top_k=10, use_hyde=use_hyde, use_expand=use_expand
    )
    print(format_compliance_result(result, verbose=True))


def process_file(mapper, filepath: str, use_hyde: bool = True, use_expand: bool = True):
    """Process requirements from a file (one per line or separated by blank lines)."""
    from retrieval.compliance_mapper import format_compliance_result

    path = Path(filepath)
    if not path.exists():
        print(f"[ERROR] File not found: {filepath}")
        sys.exit(1)

    content = path.read_text(encoding="utf-8")

    # Split by double newlines or treat each line as a requirement
    if "\n\n" in content:
        requirements = [r.strip() for r in content.split("\n\n") if r.strip()]
    else:
        requirements = [r.strip() for r in content.split("\n") if r.strip()]

    print(f"Processing {len(requirements)} requirements...\n")

    for i, req in enumerate(requirements, 1):
        print(f"\n[{i}/{len(requirements)}]")
        result = mapper.map_requirement(
            req, top_k=10, use_hyde=use_hyde, use_expand=use_expand
        )
        print(format_compliance_result(result))


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Map regulatory requirements to internal policies"
    )
    parser.add_argument(
        "requirement",
        nargs="?",
        help="Regulatory requirement text (optional, starts interactive mode if not provided)"
    )
    parser.add_argument(
        "--file", "-f",
        help="File containing requirements (one per line or separated by blank lines)"
    )
    parser.add_argument(
        "--no-hyde",
        action="store_true",
        help="Disable HyDE (faster but less accurate)"
    )
    parser.add_argument(
        "--no-expand",
        action="store_true",
        help="Disable requirement expansion (faster, single-pass retrieval)"
    )

    args = parser.parse_args()

    use_hyde = not args.no_hyde
    use_expand = not args.no_expand

    check_setup()
    mapper = load_mapper(use_expand=use_expand)

    if args.file:
        process_file(mapper, args.file, use_hyde=use_hyde, use_expand=use_expand)
    elif args.requirement:
        single_query(mapper, args.requirement, use_hyde=use_hyde, use_expand=use_expand)
    else:
        interactive_mode(mapper, use_hyde=use_hyde, use_expand=use_expand)


if __name__ == "__main__":
    main()
