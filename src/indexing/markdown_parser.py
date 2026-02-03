"""
Markdown Parser for Policy Documents

Parses structured markdown files and extracts:
- YAML frontmatter (metadata)
- Sections with IDs
- Entity annotations
- Cross-references
"""

import re
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Section:
    """Represents a section from a policy document."""
    section_id: str
    title: str
    level: int  # 1 = #, 2 = ##, 3 = ###, etc.
    content: str

    # Metadata from HTML comments
    compliance_relevance: Optional[str] = None
    likely_maps_to: list[str] = field(default_factory=list)

    # Extracted entities
    entities: dict = field(default_factory=dict)

    # Parent document info
    document_id: str = ""
    document_title: str = ""

    # Position in document
    section_path: str = ""  # e.g., "6.0 > 6.3 > 6.3.1"

    def get_full_text(self) -> str:
        """Get section content with title for indexing."""
        return f"{self.title}\n\n{self.content}"

    def get_text_for_embedding(self) -> str:
        """Get clean text for embedding (no annotations)."""
        text = self.get_full_text()
        # Remove entity annotations but keep the entity text
        text = re.sub(r'\[\[(?:role|control|asset|process|external|doc|framework):([^\]]+)\]\]', r'\1', text)
        # Remove HTML comments
        text = re.sub(r'<!--[^>]*-->', '', text)
        # Remove markdown formatting
        text = re.sub(r'\*\*\[(?:MANDATORY|RECOMMENDED)\]\*\*\s*', '', text)
        return text.strip()


@dataclass
class ParsedDocument:
    """Represents a fully parsed policy document."""
    filepath: Path
    filename: str
    document_id: str
    title: str
    frontmatter: dict
    sections: list[Section]
    raw_content: str

    def get_all_entities(self) -> dict:
        """Get all entities from frontmatter."""
        return self.frontmatter.get("entities", {})

    def get_section_by_id(self, section_id: str) -> Optional[Section]:
        """Find a section by its ID."""
        for section in self.sections:
            if section.section_id == section_id:
                return section
        return None


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """
    Extract YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter_dict, remaining_content)
    """
    if not content.startswith("---"):
        return {}, content

    # Find the closing ---
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content

    yaml_content = match.group(1)
    remaining = match.group(2)

    try:
        frontmatter = yaml.safe_load(yaml_content) or {}
    except yaml.YAMLError as e:
        print(f"Warning: Failed to parse YAML frontmatter: {e}")
        frontmatter = {}

    return frontmatter, remaining


def extract_section_metadata(content: str) -> dict:
    """Extract metadata from HTML comments in section content."""
    metadata = {}

    # Extract section_id
    section_id_match = re.search(r'<!--\s*section_id:\s*([^\s>]+)\s*-->', content)
    if section_id_match:
        metadata["section_id"] = section_id_match.group(1)

    # Extract compliance_relevance
    relevance_match = re.search(r'<!--\s*compliance_relevance:\s*(\w+)\s*-->', content)
    if relevance_match:
        metadata["compliance_relevance"] = relevance_match.group(1)

    # Extract likely_maps_to
    maps_match = re.search(r'<!--\s*likely_maps_to:\s*\[([^\]]+)\]\s*-->', content)
    if maps_match:
        items = maps_match.group(1)
        metadata["likely_maps_to"] = [
            item.strip().strip('"\'')
            for item in items.split(",")
        ]

    return metadata


def extract_entities_from_content(content: str) -> dict:
    """Extract entity annotations from content."""
    entities = {
        "roles": [],
        "controls": [],
        "assets": [],
        "processes": [],
        "external": [],
        "documents": [],
        "frameworks": []
    }

    # Pattern: [[type:entity]]
    pattern = r'\[\[(role|control|asset|process|external|doc|framework):([^\]]+)\]\]'

    for match in re.finditer(pattern, content):
        entity_type = match.group(1)
        entity_value = match.group(2).strip()

        type_mapping = {
            "role": "roles",
            "control": "controls",
            "asset": "assets",
            "process": "processes",
            "external": "external",
            "doc": "documents",
            "framework": "frameworks"
        }

        key = type_mapping.get(entity_type, entity_type)
        if entity_value not in entities[key]:
            entities[key].append(entity_value)

    return entities


def parse_sections(content: str, document_id: str, document_title: str) -> list[Section]:
    """
    Parse markdown content into sections.

    Uses heading hierarchy to create sections.
    """
    sections = []

    # Split by headers (##, ###, ####, etc.)
    # Keep the header with the content
    header_pattern = r'^(#{1,6})\s+(.+?)$'

    lines = content.split('\n')
    current_section = None
    current_content = []
    section_stack = []  # Track hierarchy for section_path

    for line in lines:
        header_match = re.match(header_pattern, line)

        if header_match:
            # Save previous section if exists
            if current_section is not None:
                current_section.content = '\n'.join(current_content).strip()
                if current_section.content or current_section.title:  # Only add non-empty
                    sections.append(current_section)

            # Parse new header
            level = len(header_match.group(1))
            title = header_match.group(2).strip()

            # Update section stack for path
            while section_stack and section_stack[-1][0] >= level:
                section_stack.pop()
            section_stack.append((level, title))

            # Build section path
            section_path = " > ".join(t for _, t in section_stack)

            # Create new section
            current_section = Section(
                section_id="",  # Will be filled from content
                title=title,
                level=level,
                content="",
                document_id=document_id,
                document_title=document_title,
                section_path=section_path
            )
            current_content = []

        else:
            current_content.append(line)

    # Don't forget the last section
    if current_section is not None:
        current_section.content = '\n'.join(current_content).strip()
        if current_section.content or current_section.title:
            sections.append(current_section)

    # Post-process sections: extract metadata and entities
    for section in sections:
        # Extract metadata from HTML comments
        metadata = extract_section_metadata(section.content)

        if "section_id" in metadata:
            section.section_id = metadata["section_id"]
        else:
            # Generate section_id from document_id and title
            title_slug = re.sub(r'[^\w\s]', '', section.title)
            title_slug = re.sub(r'\s+', '-', title_slug.strip().lower())[:20]
            section.section_id = f"{document_id}-{title_slug}"

        section.compliance_relevance = metadata.get("compliance_relevance")
        section.likely_maps_to = metadata.get("likely_maps_to", [])

        # Extract entities
        section.entities = extract_entities_from_content(section.content)

    return sections


def parse_markdown_file(filepath: str | Path) -> ParsedDocument:
    """
    Parse a structured markdown policy document.

    Args:
        filepath: Path to the markdown file

    Returns:
        ParsedDocument with all extracted information
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    content = filepath.read_text(encoding="utf-8")

    # Extract frontmatter
    frontmatter, body = parse_frontmatter(content)

    # Get document identifiers
    document_id = frontmatter.get("document_id", filepath.stem[:3].upper())
    title = frontmatter.get("title", filepath.stem)

    # Parse sections
    sections = parse_sections(body, document_id, title)

    return ParsedDocument(
        filepath=filepath,
        filename=filepath.name,
        document_id=document_id,
        title=title,
        frontmatter=frontmatter,
        sections=sections,
        raw_content=content
    )


def parse_all_markdown_files(directory: str | Path) -> list[ParsedDocument]:
    """
    Parse all markdown files in a directory.

    Args:
        directory: Path to directory containing markdown files

    Returns:
        List of ParsedDocument objects
    """
    directory = Path(directory)

    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    documents = []
    md_files = sorted(directory.glob("*.md"))

    # Skip conversion log
    md_files = [f for f in md_files if f.name != "conversion_log.json"]

    for md_path in md_files:
        print(f"Parsing: {md_path.name}")
        try:
            doc = parse_markdown_file(md_path)
            documents.append(doc)
            print(f"  [OK] {len(doc.sections)} sections extracted")
        except Exception as e:
            print(f"  [ERROR] {e}")

    return documents


# CLI for testing
if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) < 2:
        print("Usage: python markdown_parser.py <markdown_file_or_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_file():
        doc = parse_markdown_file(path)
        print(f"\nParsed: {doc.title}")
        print(f"Document ID: {doc.document_id}")
        print(f"Sections: {len(doc.sections)}")
        print("\nSections:")
        for s in doc.sections[:10]:
            print(f"  [{s.section_id}] {s.title}")
    elif path.is_dir():
        docs = parse_all_markdown_files(path)
        print(f"\nParsed {len(docs)} documents")
        total_sections = sum(len(d.sections) for d in docs)
        print(f"Total sections: {total_sections}")
