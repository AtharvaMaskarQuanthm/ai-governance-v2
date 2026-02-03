"""
PDF to Structured Markdown Conversion

Uses OpenAI GPT-4o to convert extracted PDF text into structured markdown
following the policy extraction schema.
"""

import json
import re
from pathlib import Path
from typing import Optional
from openai import OpenAI

from .pdf_extractor import ExtractedDocument, extract_pdf


# System prompt for the conversion
SYSTEM_PROMPT = """You are an expert document converter specializing in information security policies.

Your task is to convert raw PDF text into structured markdown following a specific schema.

## Output Format

The output MUST have two parts:
1. YAML frontmatter (between --- markers)
2. Markdown content with section IDs and entity annotations

## Frontmatter Schema

```yaml
---
document_id: "XXX"           # 2-5 letter unique ID (e.g., CSP, ISP, IMP)
title: "Full Policy Title"
filename: "original.pdf"
version: "X.X"
status: "approved"           # draft | review | approved | superseded
created_date: "YYYY-MM-DD"   # Or null if unknown
effective_date: "YYYY-MM-DD"
last_reviewed: "YYYY-MM-DD"
next_review: "YYYY-MM-DD"    # Or null if not specified

owner:
  name: "Person Name"
  role: "Role Title"

prepared_by:
  - name: "Person Name"
    role: "Role Title"

approved_by:
  - name: "Person Name"
    role: "Role Title"
    date: "YYYY-MM-DD"

classification: "Internal"    # Public | Internal | Confidential | Restricted
applies_to:
  - "employees"
  - "contractors"
  # etc.

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"
  # Include all mentioned frameworks

references:                   # Other internal policies referenced
  - document_id: "XXX"
    title: "Policy Name"
    relationship: "related"   # parent | child | related

scope:
  description: "Brief scope description"
  inclusions:
    - "What's covered"
  exclusions:
    - "What's not covered"

entities:
  roles:
    - "CISO"
    - "IT Department"
    # All roles mentioned
  controls:
    - "Firewall"
    - "Encryption"
    # All security controls mentioned
  assets:
    - "Servers"
    - "Databases"
    # All assets mentioned
  processes:
    - "Incident Management"
    - "Access Review"
    # All processes mentioned
  external_parties:
    - "CERT-IN"
    - "SEBI"
    # External entities mentioned

tags:
  - "relevant"
  - "keywords"
---
```

## Content Formatting Rules

1. **Section Headers**: Use proper markdown hierarchy (##, ###, ####)

2. **Section IDs**: Add HTML comment after EVERY section header:
   ```markdown
   ## 6.0 Cyber Security Operations
   <!-- section_id: CSP-6.0 -->
   ```

3. **Mandatory vs Recommended**: Prefix requirements with:
   - `**[MANDATORY]**` for "shall", "must", "is required"
   - `**[RECOMMENDED]**` for "should", "may consider"

4. **Entity Annotations**: Annotate key entities inline:
   - `[[role:CISO]]` for roles
   - `[[control:MFA]]` for security controls
   - `[[asset:servers]]` for assets
   - `[[process:incident management]]` for processes
   - `[[external:CERT-IN]]` for external parties
   - `[[doc:policy-name]]` for internal document references

5. **Tables**: Preserve tables in markdown format with proper headers

6. **Cross-References**: Use callout blocks:
   ```markdown
   > [!CROSS-REF]
   > Refer to [[doc:incident-management-policy]] for details.
   ```

7. **Definitions**: Use definition list format:
   ```markdown
   **Term**
   : Definition text here
   ```

8. **Compliance Hints**: For sections highly relevant to compliance, add:
   ```markdown
   <!-- compliance_relevance: high -->
   <!-- likely_maps_to: ["keyword1", "keyword2"] -->
   ```

## Important Guidelines

- Preserve ALL content from the original - do not summarize or omit
- Fix obvious OCR/extraction errors
- Normalize inconsistent formatting
- Extract the document_id from the title (e.g., "Cyber Security Policy" → "CSP")
- If dates are in formats like "17-Oct-16", convert to "2016-10-17"
- If information is not available, use null (not "N/A" or "Unknown")
- Include ALL sections, including appendices and annexures
"""


USER_PROMPT_TEMPLATE = """Convert the following extracted PDF content into structured markdown.

**Original Filename:** {filename}

**Extracted Content:**
{content}

---

Please output the complete structured markdown with YAML frontmatter.
Remember to:
1. Include ALL content - do not summarize
2. Add section_id comments to EVERY section
3. Annotate entities with [[type:entity]] syntax
4. Mark requirements as [MANDATORY] or [RECOMMENDED]
5. Extract all metadata for the frontmatter"""


def convert_to_markdown(
    document: ExtractedDocument,
    client: OpenAI,
    model: str = "gpt-4o",
    max_tokens: int = 16000
) -> str:
    """
    Convert an extracted PDF document to structured markdown using OpenAI.

    Args:
        document: ExtractedDocument from pdf_extractor
        client: OpenAI client instance
        model: Model to use for conversion
        max_tokens: Max tokens for response

    Returns:
        Structured markdown string
    """
    # Get full text content
    content = document.get_full_text(include_page_markers=True)

    # Check if content is too large - if so, process in chunks
    if len(content) > 100000:  # Roughly 25k tokens
        return convert_large_document(document, client, model, max_tokens)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        filename=document.filename,
        content=content
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.1  # Low temperature for consistency
    )

    return response.choices[0].message.content


def convert_large_document(
    document: ExtractedDocument,
    client: OpenAI,
    model: str = "gpt-4o",
    max_tokens: int = 16000
) -> str:
    """
    Convert a large document by processing in chunks and combining.
    First pass extracts frontmatter, subsequent passes convert content.
    """
    chunks = document.get_text_chunks(max_chars=50000)

    # First chunk: Extract frontmatter + convert content
    first_chunk_prompt = f"""Convert this PDF content to structured markdown.
This is PART 1 of {len(chunks)} parts. Extract the YAML frontmatter from the document metadata visible here.

**Filename:** {document.filename}

**Content:**
{chunks[0]}

Output the frontmatter AND the converted content for this section."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": first_chunk_prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.1
    )

    result_parts = [response.choices[0].message.content]

    # Subsequent chunks: Just convert content
    for i, chunk in enumerate(chunks[1:], start=2):
        chunk_prompt = f"""Continue converting this PDF content to structured markdown.
This is PART {i} of {len(chunks)}. Do NOT include frontmatter - just continue the content.

**Content:**
{chunk}

Continue the markdown content, maintaining section IDs and entity annotations."""

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": chunk_prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.1
        )

        result_parts.append(response.choices[0].message.content)

    # Combine parts (remove any duplicate frontmatter from later parts)
    combined = result_parts[0]
    for part in result_parts[1:]:
        # Remove any accidental frontmatter
        if part.startswith("---"):
            # Find the end of frontmatter and take content after
            end_match = re.search(r'\n---\n', part[3:])
            if end_match:
                part = part[end_match.end() + 3:]
        combined += "\n\n" + part

    return combined


def generate_document_id(title: str) -> str:
    """Generate a document ID from the title."""
    # Common mappings
    mappings = {
        "cyber security": "CSP",
        "cybersecurity": "CSP",
        "information security": "ISP",
        "incident": "IMP",
        "access control": "ACP",
        "network security": "NSP",
        "data classification": "DCP",
        "asset classification": "ACP",
        "business continuity": "BCP",
        "disaster recovery": "DRP",
        "sdlc": "SDLC",
        "supplier": "SPP",
        "vendor": "VMP",
        "mobile device": "MDP",
        "hardening": "HSP",
        "crisis": "CMP",
        "risk management": "RMP",
        "data disposal": "DDP",
        "retention": "DRP",
    }

    title_lower = title.lower()
    for key, doc_id in mappings.items():
        if key in title_lower:
            return doc_id

    # Fallback: Use first letters of significant words
    words = re.findall(r'[A-Z][a-z]+|[A-Z]+', title)
    if words:
        return "".join(w[0] for w in words[:4]).upper()

    return "DOC"


def save_markdown(content: str, output_path: Path, document_id: str = None) -> Path:
    """
    Save markdown content to file with proper naming.

    Args:
        content: Markdown content
        output_path: Output directory or file path
        document_id: Optional document ID for filename

    Returns:
        Path to saved file
    """
    output_path = Path(output_path)

    if output_path.is_dir():
        # Generate filename from document_id or extract from content
        if not document_id:
            # Try to extract from frontmatter
            match = re.search(r'document_id:\s*["\']?(\w+)["\']?', content)
            if match:
                document_id = match.group(1)
            else:
                document_id = "DOC"

        # Extract title for filename
        title_match = re.search(r'title:\s*["\']?([^"\'\n]+)["\']?', content)
        if title_match:
            title_slug = re.sub(r'[^\w\s]', '', title_match.group(1))
            title_slug = re.sub(r'\s+', '_', title_slug.strip().lower())
        else:
            title_slug = "policy"

        filename = f"{document_id}_{title_slug}.md"
        output_path = output_path / filename

    # Write content
    output_path.write_text(content, encoding="utf-8")
    return output_path


def convert_pdf_to_markdown(
    pdf_path: str | Path,
    output_dir: str | Path,
    client: OpenAI,
    model: str = "gpt-4o"
) -> Path:
    """
    Full pipeline: Extract PDF and convert to structured markdown.

    Args:
        pdf_path: Path to PDF file
        output_dir: Directory to save markdown output
        client: OpenAI client
        model: Model to use

    Returns:
        Path to saved markdown file
    """
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Extracting: {pdf_path.name}")
    document = extract_pdf(pdf_path)
    print(f"  → {document.total_pages} pages extracted")

    print(f"Converting with {model}...")
    markdown = convert_to_markdown(document, client, model)
    print(f"  → Conversion complete")

    output_path = save_markdown(markdown, output_dir)
    print(f"  → Saved to: {output_path.name}")

    return output_path


# CLI for testing
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown.py <pdf_path> [output_dir]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output"

    # Initialize OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    output_path = convert_pdf_to_markdown(pdf_path, output_dir, client)
    print(f"\nDone! Output saved to: {output_path}")
