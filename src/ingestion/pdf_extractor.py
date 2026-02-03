"""
PDF Text Extraction Module

Extracts text and tables from policy PDF documents using pdfplumber.
Preserves structure as much as possible for downstream LLM processing.
"""

import pdfplumber
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ExtractedPage:
    """Represents extracted content from a single PDF page."""
    page_number: int
    text: str
    tables: list[list[list[str]]] = field(default_factory=list)


@dataclass
class ExtractedDocument:
    """Represents extracted content from an entire PDF document."""
    filename: str
    filepath: Path
    pages: list[ExtractedPage]
    total_pages: int
    metadata: dict = field(default_factory=dict)

    def get_full_text(self, include_page_markers: bool = True) -> str:
        """Get all text concatenated, optionally with page markers."""
        parts = []
        for page in self.pages:
            if include_page_markers:
                parts.append(f"\n--- Page {page.page_number} ---\n")
            parts.append(page.text)

            # Add tables as formatted text
            for table_idx, table in enumerate(page.tables):
                parts.append(f"\n[Table {table_idx + 1}]\n")
                parts.append(format_table_as_text(table))

        return "\n".join(parts)

    def get_text_chunks(self, max_chars: int = 15000) -> list[str]:
        """
        Split document into chunks for LLM processing.
        Tries to split on page boundaries.
        """
        chunks = []
        current_chunk = []
        current_size = 0

        for page in self.pages:
            page_text = f"\n--- Page {page.page_number} ---\n{page.text}"

            # Add tables
            for table_idx, table in enumerate(page.tables):
                page_text += f"\n[Table {table_idx + 1}]\n"
                page_text += format_table_as_text(table)

            page_size = len(page_text)

            if current_size + page_size > max_chars and current_chunk:
                # Save current chunk and start new one
                chunks.append("\n".join(current_chunk))
                current_chunk = [page_text]
                current_size = page_size
            else:
                current_chunk.append(page_text)
                current_size += page_size

        # Don't forget the last chunk
        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks


def format_table_as_text(table: list[list[str]]) -> str:
    """Convert a table (list of rows) to formatted text."""
    if not table:
        return ""

    # Clean up None values
    cleaned = []
    for row in table:
        cleaned_row = [str(cell) if cell is not None else "" for cell in row]
        cleaned.append(cleaned_row)

    # Calculate column widths
    col_widths = []
    for col_idx in range(len(cleaned[0])):
        max_width = 0
        for row in cleaned:
            if col_idx < len(row):
                max_width = max(max_width, len(row[col_idx]))
        col_widths.append(min(max_width, 50))  # Cap at 50 chars

    # Format rows
    lines = []
    for row_idx, row in enumerate(cleaned):
        cells = []
        for col_idx, cell in enumerate(row):
            width = col_widths[col_idx] if col_idx < len(col_widths) else 20
            cells.append(cell[:width].ljust(width))
        lines.append(" | ".join(cells))

        # Add separator after header
        if row_idx == 0:
            separators = ["-" * w for w in col_widths]
            lines.append("-|-".join(separators))

    return "\n".join(lines)


def extract_pdf(filepath: str | Path) -> ExtractedDocument:
    """
    Extract text and tables from a PDF file.

    Args:
        filepath: Path to the PDF file

    Returns:
        ExtractedDocument containing all extracted content
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"PDF not found: {filepath}")

    if not filepath.suffix.lower() == ".pdf":
        raise ValueError(f"Not a PDF file: {filepath}")

    pages = []

    with pdfplumber.open(filepath) as pdf:
        metadata = pdf.metadata or {}
        total_pages = len(pdf.pages)

        for page_num, page in enumerate(pdf.pages, start=1):
            # Extract text
            text = page.extract_text() or ""

            # Extract tables
            tables = []
            extracted_tables = page.extract_tables()
            if extracted_tables:
                tables = extracted_tables

            pages.append(ExtractedPage(
                page_number=page_num,
                text=text,
                tables=tables
            ))

    return ExtractedDocument(
        filename=filepath.name,
        filepath=filepath,
        pages=pages,
        total_pages=total_pages,
        metadata=metadata
    )


def extract_all_pdfs(directory: str | Path) -> list[ExtractedDocument]:
    """
    Extract all PDFs from a directory.

    Args:
        directory: Path to directory containing PDFs

    Returns:
        List of ExtractedDocument objects
    """
    directory = Path(directory)

    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    documents = []
    pdf_files = sorted(directory.glob("*.pdf"))

    for pdf_path in pdf_files:
        print(f"Extracting: {pdf_path.name}")
        try:
            doc = extract_pdf(pdf_path)
            documents.append(doc)
            print(f"  ✓ {doc.total_pages} pages extracted")
        except Exception as e:
            print(f"  ✗ Error: {e}")

    return documents


# CLI for testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python pdf_extractor.py <pdf_path_or_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_file():
        doc = extract_pdf(path)
        print(f"\nExtracted {doc.total_pages} pages from {doc.filename}")
        print("\n" + "="*50)
        print(doc.get_full_text()[:2000])
        print("...")
    elif path.is_dir():
        docs = extract_all_pdfs(path)
        print(f"\nExtracted {len(docs)} documents")
    else:
        print(f"Path not found: {path}")
