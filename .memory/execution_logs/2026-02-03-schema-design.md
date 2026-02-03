# Execution Log: Policy Extraction Schema Design

**Date:** 2026-02-03
**Task:** Design structured markdown schema for policy document conversion
**Status:** Completed

---

## Context

Building an agentic compliance mapping system that needs to:
1. Take SEBI CSCRF regulatory guidelines as input
2. Find where they're covered in internal policy documents
3. Provide explainable mappings with gap analysis

## Decision: Convert PDFs to Structured Markdown

**Why not keep PDFs?**
- Poor chunking (arbitrary character splits)
- No semantic structure preservation
- Hard to build knowledge graphs
- Entity extraction is noisy

**Why structured markdown?**
- Preserves document hierarchy (sections → subsections)
- Enables precise citations (e.g., "CSP-6.3.1")
- Entity annotations enable GraphRAG
- Version controllable and diffable
- Clean input for both BM25 and dense retrieval

## Schema Design Decisions

### 1. Section IDs for Precise Citation
Every section gets a unique ID: `{DOC_ID}-{SECTION_NUMBER}`
Example: `CSP-6.3.2` = Cyber Security Policy, Section 6.3.2 (Logical Access Security)

**Rationale:** When the system says "this requirement is covered", we need to point to the exact location, not just "somewhere in the Cyber Security Policy".

### 2. YAML Frontmatter for Metadata
Rich metadata including:
- Version control info
- Ownership chain
- Regulatory framework alignment
- Cross-references to other policies
- Extracted entities (roles, controls, assets)

**Rationale:**
- Enables filtering ("show me only policies that reference SEBI CSCRF")
- Supports GraphRAG node creation
- Provides context for LLM synthesis

### 3. Entity Annotations Inline
Using `[[type:entity]]` syntax:
- `[[role:CISO]]`
- `[[control:MFA]]`
- `[[asset:servers]]`
- `[[doc:incident-management-policy]]`

**Rationale:** Enables relationship extraction for knowledge graphs without separate NER pass.

### 4. Compliance Hints
Added `<!-- likely_maps_to: [...] -->` comments to sections.

**Rationale:** Helps with HyDE (Hypothetical Document Embedding) by giving the LLM hints about what regulatory topics this section likely addresses. When generating a hypothetical document for a query like "multi-factor authentication requirements", the system knows CSP-6.3.2 is relevant.

### 5. Mandatory/Recommended Markers
Using `**[MANDATORY]**` and `**[RECOMMENDED]**` prefixes.

**Rationale:** Distinguishes between hard requirements and best practices. Important for compliance mapping — "MUST implement MFA" vs "SHOULD consider MFA".

## Files Created

1. `schemas/policy_extraction_schema.md` — Human-readable schema documentation
2. `schemas/policy_frontmatter.schema.json` — JSON Schema for validation
3. `schemas/example_policy.md` — Full example of converted Cyber Security Policy

## HyDE Considerations

The schema supports HyDE retrieval through:
1. **`likely_maps_to` hints** — Keywords that help generate hypothetical documents
2. **Consistent section structure** — HyDE-generated docs will match real structure
3. **Standardized terminology** — Entity annotations normalize language

For HyDE to work optimally, the conversion prompt should:
- Use consistent terminology across all policies
- Include the `likely_maps_to` hints based on section content
- Normalize control names (e.g., always "Multi-factor Authentication" not "MFA" or "2FA")

## Next Steps

1. Build PDF → Markdown conversion pipeline using OpenAI API
2. Convert all 19 policy documents
3. Build hybrid retrieval (BM25 + dense + HyDE + GraphRAG)
4. Create query interface for SEBI CSCRF mapping

---

## Additional Documents Created

### HyDE Prompt Templates (`schemas/hyde_prompt_template.md`)
- Template 1: Regulation → Hypothetical Policy Section
- Template 2: Multi-domain hypothetical generation
- Template 3: Keyword expansion for BM25
- Template 4: Gap analysis prompt
- Template 5: Entity extraction for GraphRAG

**Key Decision:** HyDE generates **policy-style** hypothetical documents (not regulation-style) because we're searching a policy corpus. The hypothetical doc should match the style/structure of what we're searching.

### Retrieval Architecture (`schemas/retrieval_architecture.md`)
Documented the full hybrid retrieval pipeline:

```
Query → [BM25 | Vector | HyDE | GraphRAG] → Fusion (RRF) → Reranker → LLM Synthesis
```

**Key Decisions:**
1. **Fusion Method:** Reciprocal Rank Fusion (RRF) - robust, no tuning needed
2. **Graph Expansion:** Max 2 hops to avoid noise
3. **Reranker:** Cross-encoder with 0.5 threshold for final filtering
4. **Chunking:** Section-level (not fixed-size) for semantic coherence

---

## Open Questions

- Should we extract tables into separate structured JSON for better retrieval?
- Which vector DB? Leaning toward Qdrant for built-in hybrid support
- Evaluation dataset needed - manually map some CSCRF requirements first?

---

## PDF to Markdown Pipeline (Added)

Built the conversion pipeline:

### Files Created
- `src/ingestion/pdf_extractor.py` - pdfplumber-based extraction
- `src/ingestion/pdf_to_markdown.py` - OpenAI GPT-4o conversion
- `src/ingestion/convert_all.py` - Batch processing with logging
- `run_conversion.py` - Quick runner script
- `requirements.txt` - Python dependencies

### Design Decisions

1. **pdfplumber over PyMuPDF**: Better table extraction, which is critical for ISMS policy docs with audit matrices, version control tables, etc.

2. **Chunked processing for large docs**: Documents > 100K chars are split into chunks and processed sequentially to stay within context limits.

3. **Single model call per document**: Rather than extract-then-annotate, we do it in one pass. LLM handles structure detection, entity annotation, and formatting together.

4. **Skip existing**: By default, won't re-convert files that already have markdown versions. Use `--no-skip` to force reconversion.

5. **Temperature 0.1**: Low temperature for consistent, reproducible conversions.

### Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export OPENAI_API_KEY=sk-your-key
# Or create .env file

# Preview what would be converted
python run_conversion.py --dry-run

# Convert all policies
python run_conversion.py

# Convert single file
python run_conversion.py --single "data/policies/some-policy.pdf"
```

---

## Hybrid Retrieval Pipeline (Added)

### Files Created
- `src/retrieval/hybrid_retriever.py` - BM25 + Vector + HyDE fusion
- `src/retrieval/compliance_mapper.py` - Coverage analysis with LLM
- `run_query.py` - Interactive query interface

### Architecture
```
Query (SEBI CSCRF requirement)
        │
        ├──→ BM25 (keyword matching)
        ├──→ Vector Search (semantic similarity)
        └──→ HyDE (hypothetical doc → embedding → search)
                │
                ▼
        Reciprocal Rank Fusion
                │
                ▼
        Top-K Policy Sections
                │
                ▼
        LLM Analysis (GPT-4o)
                │
                ▼
        ComplianceResult
        ├── coverage: FULL/PARTIAL/NOT_COVERED
        ├── mappings: [section → relevance]
        ├── gaps: [what's missing]
        └── recommendations: [actions needed]
```

### Usage
```bash
# Interactive mode
python run_query.py

# Single query
python run_query.py "MIs shall implement MFA for privileged access"

# Process file of requirements
python run_query.py --file requirements.txt
```
