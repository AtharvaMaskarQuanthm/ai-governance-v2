#!/usr/bin/env python3
"""
Quick runner script for PDF to Markdown conversion.

Usage:
    python run_conversion.py                    # Convert all policies
    python run_conversion.py --dry-run          # Preview what would be done
    python run_conversion.py --single <pdf>     # Convert a single PDF
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Load environment variables from .env file
load_dotenv()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert policy PDFs to markdown")
    parser.add_argument("--dry-run", action="store_true", help="Preview without converting")
    parser.add_argument("--single", type=str, help="Convert a single PDF file")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model (default: gpt-4o)")
    parser.add_argument("--no-skip", action="store_true", help="Re-convert existing files")

    args = parser.parse_args()

    # Check for API key
    if not os.getenv("OPENAI_API_KEY") and not args.dry_run:
        print("❌ Error: OPENAI_API_KEY not set")
        print("\nOptions:")
        print("  1. Create a .env file with: OPENAI_API_KEY=sk-your-key")
        print("  2. Or set environment variable: export OPENAI_API_KEY=sk-your-key")
        print("  3. Or run with --dry-run to preview")
        sys.exit(1)

    if args.single:
        # Convert single file
        from openai import OpenAI
        from ingestion.pdf_to_markdown import convert_pdf_to_markdown

        pdf_path = Path(args.single)
        if not pdf_path.exists():
            print(f"❌ File not found: {pdf_path}")
            sys.exit(1)

        output_dir = Path(__file__).parent / "data" / "policies_md"
        client = OpenAI()

        print(f"Converting: {pdf_path.name}")
        output_path = convert_pdf_to_markdown(pdf_path, output_dir, client, args.model)
        print(f"\n✅ Done! Output: {output_path}")

    else:
        # Convert all
        from ingestion.convert_all import convert_all_policies

        results = convert_all_policies(
            model=args.model,
            skip_existing=not args.no_skip,
            dry_run=args.dry_run
        )

        if not args.dry_run:
            print(f"\n✅ Conversion complete!")
            print(f"   Markdown files saved to: data/policies_md/")


if __name__ == "__main__":
    main()
