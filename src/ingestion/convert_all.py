"""
Batch PDF to Markdown Conversion

Converts all policy PDFs in the data/policies directory to structured markdown.
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Optional

from openai import OpenAI

from .pdf_extractor import extract_all_pdfs, ExtractedDocument
from .pdf_to_markdown import convert_to_markdown, save_markdown


def get_project_root() -> Path:
    """Get the project root directory."""
    current = Path(__file__).resolve()
    # Navigate up from src/ingestion/convert_all.py
    return current.parent.parent.parent


def convert_all_policies(
    input_dir: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    model: str = "gpt-4o",
    skip_existing: bool = True,
    dry_run: bool = False
) -> dict:
    """
    Convert all PDF policies to structured markdown.

    Args:
        input_dir: Directory containing PDFs (default: data/policies)
        output_dir: Directory for markdown output (default: data/policies_md)
        model: OpenAI model to use
        skip_existing: Skip files that already have a markdown version
        dry_run: If True, only show what would be done

    Returns:
        Summary dict with results
    """
    project_root = get_project_root()

    if input_dir is None:
        input_dir = project_root / "data" / "policies"
    if output_dir is None:
        output_dir = project_root / "data" / "policies_md"

    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key and not dry_run:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)

    # Initialize client
    client = OpenAI(api_key=api_key) if not dry_run else None

    # Get all PDFs
    pdf_files = sorted(input_dir.glob("*.pdf"))
    print(f"\nFound {len(pdf_files)} PDF files in {input_dir}")
    print("=" * 60)

    # Track results
    results = {
        "total": len(pdf_files),
        "converted": [],
        "skipped": [],
        "failed": [],
        "start_time": datetime.now().isoformat(),
        "model": model
    }

    # Check existing markdown files
    existing_md = {f.stem.lower(): f for f in output_dir.glob("*.md")}

    for i, pdf_path in enumerate(pdf_files, 1):
        pdf_name = pdf_path.stem
        print(f"\n[{i}/{len(pdf_files)}] {pdf_path.name}")

        # Check if already converted
        if skip_existing:
            # Check if any markdown file references this PDF
            should_skip = False
            for md_file in output_dir.glob("*.md"):
                content_preview = md_file.read_text(encoding="utf-8")[:500]
                if pdf_path.name in content_preview:
                    should_skip = True
                    print(f"  ⏭ Skipping (already exists: {md_file.name})")
                    results["skipped"].append({
                        "pdf": pdf_path.name,
                        "existing_md": md_file.name
                    })
                    break

            if should_skip:
                continue

        if dry_run:
            print(f"  📝 Would convert to markdown")
            results["converted"].append({
                "pdf": pdf_path.name,
                "status": "dry_run"
            })
            continue

        try:
            # Extract PDF
            print(f"  📄 Extracting text...")
            from .pdf_extractor import extract_pdf
            document = extract_pdf(pdf_path)
            print(f"     {document.total_pages} pages extracted")

            # Convert to markdown
            print(f"  🤖 Converting with {model}...")
            start_time = time.time()
            markdown = convert_to_markdown(document, client, model)
            elapsed = time.time() - start_time
            print(f"     Conversion took {elapsed:.1f}s")

            # Save markdown
            output_path = save_markdown(markdown, output_dir)
            print(f"  ✅ Saved: {output_path.name}")

            results["converted"].append({
                "pdf": pdf_path.name,
                "markdown": output_path.name,
                "pages": document.total_pages,
                "time_seconds": round(elapsed, 1)
            })

            # Rate limiting - be nice to the API
            if i < len(pdf_files):
                time.sleep(1)

        except Exception as e:
            print(f"  ❌ Error: {e}")
            results["failed"].append({
                "pdf": pdf_path.name,
                "error": str(e)
            })

    # Summary
    results["end_time"] = datetime.now().isoformat()
    print("\n" + "=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)
    print(f"Total PDFs:     {results['total']}")
    print(f"Converted:      {len(results['converted'])}")
    print(f"Skipped:        {len(results['skipped'])}")
    print(f"Failed:         {len(results['failed'])}")

    if results["failed"]:
        print("\nFailed files:")
        for f in results["failed"]:
            print(f"  - {f['pdf']}: {f['error']}")

    # Save results log
    log_path = output_dir / "conversion_log.json"
    with open(log_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nLog saved to: {log_path}")

    return results


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert all policy PDFs to structured markdown"
    )
    parser.add_argument(
        "--input-dir", "-i",
        type=Path,
        help="Input directory containing PDFs"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        help="Output directory for markdown files"
    )
    parser.add_argument(
        "--model", "-m",
        default="gpt-4o",
        help="OpenAI model to use (default: gpt-4o)"
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="Re-convert files that already exist"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without converting"
    )

    args = parser.parse_args()

    convert_all_policies(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        model=args.model,
        skip_existing=not args.no_skip,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
