# Hybrid Retrieval Architecture

This document outlines the multi-strategy retrieval system for compliance mapping.

---

## Overview

```
                        ┌─────────────────────────────────┐
                        │   User: SEBI CSCRF Requirement  │
                        └───────────────┬─────────────────┘
                                        │
                        ┌───────────────▼─────────────────┐
                        │        Query Processor          │
                        │  - Parse requirement            │
                        │  - Extract key entities         │
                        │  - Generate query variants      │
                        └───────────────┬─────────────────┘
                                        │
          ┌─────────────────────────────┼─────────────────────────────┐
          │                             │                             │
          ▼                             ▼                             ▼
┌─────────────────┐         ┌─────────────────────┐         ┌─────────────────┐
│    BM25         │         │   Vector Search     │         │     HyDE        │
│  (Lexical)      │         │   (Semantic)        │         │  (Hypothetical) │
└────────┬────────┘         └──────────┬──────────┘         └────────┬────────┘
         │                             │                             │
         │                             │                             │
         └─────────────────────────────┼─────────────────────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │      Result Fusion          │
                        │  - Reciprocal Rank Fusion   │
                        │  - Score normalization      │
                        │  - Deduplication            │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │       GraphRAG Expansion    │
                        │  - Entity-based expansion   │
                        │  - Cross-policy traversal   │
                        │  - Relationship context     │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │         Reranker            │
                        │  - Cross-encoder scoring    │
                        │  - Relevance filtering      │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │    LLM Synthesis Layer      │
                        │  - Coverage assessment      │
                        │  - Gap analysis             │
                        │  - Explainable mapping      │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │          Output             │
                        │  - Mapped policy sections   │
                        │  - Coverage status          │
                        │  - Gaps & recommendations   │
                        └─────────────────────────────┘
```

---

## Component Details

### 1. BM25 (Lexical Search)

**Purpose:** Find exact keyword matches — critical for:
- Specific terms (CERT-IN, SEBI, 180 days)
- Control names (MFA, IDS, firewall)
- Regulatory references (ISO 27001:A.9.4)

**Implementation:**
```python
# Index: All policy sections as documents
# Fields: section_text, section_id, document_id, tags, likely_maps_to

from rank_bm25 import BM25Okapi

# Preprocessing
- Lowercase
- Remove stopwords (but keep domain stopwords like "shall", "must")
- Stem/lemmatize (optional - test impact)

# Query expansion
- Add synonyms from keyword expansion template
- Include entity variations (MFA → "multi-factor authentication")
```

**Strengths:**
- Fast
- No hallucination
- Good for exact compliance terms

**Weaknesses:**
- Misses semantic similarity
- Vocabulary mismatch between regulation and policy

---

### 2. Vector Search (Dense Retrieval)

**Purpose:** Find semantically similar content even with different wording.

**Embedding Models (Options):**
| Model | Dimensions | Strengths |
|-------|------------|-----------|
| `text-embedding-3-large` | 3072 | Best quality, OpenAI |
| `text-embedding-3-small` | 1536 | Cost-effective, OpenAI |
| `voyage-law-2` | 1024 | Optimized for legal/compliance |
| `BAAI/bge-large-en-v1.5` | 1024 | Open source, good quality |

**Chunking Strategy:**
```yaml
chunking:
  strategy: "semantic"  # Not fixed-size

  # Primary: Section-level chunks
  primary_unit: "section"  # Split on ## and ### headers

  # Include context
  include_parent_header: true
  include_document_metadata: true

  # Size limits
  max_tokens: 512
  overlap_tokens: 50  # For sections that exceed max
```

**Index Structure:**
```python
{
  "id": "CSP-6.3.2",
  "document_id": "CSP",
  "document_title": "Cyber Security Policy",
  "section_title": "Logical Access Security",
  "section_path": "6.0 > 6.3 > 6.3.2",  # Breadcrumb
  "content": "...",
  "embedding": [...],
  "metadata": {
    "compliance_relevance": "high",
    "likely_maps_to": ["MFA", "privileged access", ...],
    "entities": {
      "controls": ["MFA", "encryption"],
      "roles": ["CISO", "Information Security Team"]
    }
  }
}
```

**Vector DB Options:**
- Pinecone (managed, easy)
- Qdrant (open source, good filters)
- Weaviate (hybrid search built-in)
- ChromaDB (local development)

---

### 3. HyDE (Hypothetical Document Embedding)

**Purpose:** Bridge vocabulary gap between regulatory and policy language.

**Flow:**
```
1. Input: Regulatory requirement
2. Generate: Hypothetical policy section(s) using LLM
3. Embed: Hypothetical section(s)
4. Search: Find real sections similar to hypothetical
5. Return: Real sections (not hypothetical)
```

**When HyDE Helps Most:**
- Regulation uses "Market Infrastructure Institutions" → Policy uses "Choice Equity Broking"
- Regulation uses "shall ensure" → Policy uses "is mandatory"
- Regulation is abstract → Policy is procedural

**Configuration:**
```python
hyde_config = {
    "model": "gpt-4o-mini",  # Cost-effective for generation
    "num_hypothetical": 3,   # Generate multiple for diversity
    "temperature": 0.3,      # Consistent but some variation
    "use_multi_domain": True # Generate for different policy areas
}
```

**Caching Strategy:**
- Cache hypothetical docs by requirement hash
- Invalidate on prompt template changes
- Pre-generate for known CSCRF requirements

---

### 4. GraphRAG (Knowledge Graph Retrieval)

**Purpose:** Find related content through entity relationships, not just text similarity.

**Graph Schema:**
```
NODES:
├── Document (policy document)
├── Section (policy section)
├── Role (CISO, IT Team, etc.)
├── Control (MFA, Firewall, etc.)
├── Asset (servers, databases, etc.)
├── Process (incident management, etc.)
├── Regulation (ISO 27001, SEBI CSCRF, etc.)
└── Requirement (specific regulatory requirement)

EDGES:
├── Document -[HAS_SECTION]-> Section
├── Section -[REFERENCES]-> Section (cross-references)
├── Section -[MENTIONS]-> Role/Control/Asset/Process
├── Role -[RESPONSIBLE_FOR]-> Process/Control
├── Control -[PROTECTS]-> Asset
├── Regulation -[REQUIRES]-> Control
└── Requirement -[ADDRESSED_BY]-> Section
```

**Query Expansion via Graph:**
```cypher
// Given a requirement about "incident reporting to CERT-IN"
// Find all related sections through entity traversal

MATCH (req:Requirement {text: $requirement})
// Direct mentions
MATCH (s:Section)-[:MENTIONS]->(e:Entity)
WHERE e.name IN ['CERT-IN', 'incident reporting', 'incident management']

// Expand through relationships
MATCH (s)-[:MENTIONS]->(role:Role)-[:RESPONSIBLE_FOR]->(proc:Process)
WHERE proc.name CONTAINS 'incident'

// Get related sections from same process
MATCH (s2:Section)-[:MENTIONS]->(proc)
RETURN DISTINCT s, s2
```

**Graph-Enhanced Retrieval:**
```python
def graph_expand(initial_results, graph_client, max_hops=2):
    """Expand retrieval results using graph traversal"""

    expanded = set(initial_results)

    for section in initial_results:
        # Get entities mentioned in this section
        entities = graph_client.get_entities(section.id)

        # Find other sections mentioning same entities
        for entity in entities:
            related = graph_client.sections_mentioning(entity, max_hops)
            expanded.update(related)

        # Follow cross-references
        refs = graph_client.get_references(section.id)
        expanded.update(refs)

    return expanded
```

**Graph Database Options:**
- Neo4j (mature, Cypher query language)
- Amazon Neptune (managed)
- FalkorDB (Redis-based, fast)
- NetworkX (in-memory, for prototyping)

---

### 5. Result Fusion

**Reciprocal Rank Fusion (RRF):**
```python
def reciprocal_rank_fusion(result_lists, k=60):
    """
    Combine results from multiple retrievers.
    k=60 is standard, higher k reduces impact of rank differences.
    """
    fused_scores = defaultdict(float)

    for result_list in result_lists:
        for rank, doc in enumerate(result_list):
            fused_scores[doc.id] += 1 / (k + rank + 1)

    # Sort by fused score
    return sorted(fused_scores.items(), key=lambda x: -x[1])
```

**Weighted Fusion:**
```python
weights = {
    "bm25": 0.25,
    "vector": 0.35,
    "hyde": 0.25,
    "graph": 0.15
}

# Normalize scores to [0, 1] before weighting
final_score = sum(weights[source] * normalized_score[source] for source in sources)
```

---

### 6. Reranker

**Purpose:** Final relevance scoring using cross-encoder.

**Models:**
- `cross-encoder/ms-marco-MiniLM-L-12-v2` (fast)
- `BAAI/bge-reranker-large` (better quality)
- Cohere Rerank API (managed)

**Usage:**
```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('BAAI/bge-reranker-large')

# Score each candidate against the query
pairs = [(query, doc.content) for doc in candidates]
scores = reranker.predict(pairs)

# Filter by threshold and take top-k
threshold = 0.5
top_k = 10
final_results = [
    doc for doc, score in zip(candidates, scores)
    if score > threshold
][:top_k]
```

---

## Configuration Summary

```yaml
# config/retrieval.yaml

retrieval:
  # BM25 Settings
  bm25:
    enabled: true
    top_k: 20

  # Vector Search Settings
  vector:
    enabled: true
    model: "text-embedding-3-small"
    top_k: 20
    similarity_threshold: 0.7

  # HyDE Settings
  hyde:
    enabled: true
    model: "gpt-4o-mini"
    num_hypothetical: 3
    top_k: 20

  # GraphRAG Settings
  graph:
    enabled: true
    max_hops: 2
    max_expansion: 10

  # Fusion Settings
  fusion:
    method: "rrf"  # or "weighted"
    weights:
      bm25: 0.25
      vector: 0.35
      hyde: 0.25
      graph: 0.15

  # Reranker Settings
  reranker:
    enabled: true
    model: "BAAI/bge-reranker-large"
    threshold: 0.5
    top_k: 10
```

---

## Data Flow Example

**Input:** "REs shall report cyber incidents to CERT-In within 6 hours of detection"

**Step 1 - Query Processing:**
```json
{
  "original": "REs shall report cyber incidents to CERT-In within 6 hours of detection",
  "entities": ["CERT-In", "cyber incidents", "6 hours"],
  "intent": "incident_reporting_requirement"
}
```

**Step 2 - Parallel Retrieval:**
```
BM25 Results:
  1. CSP-6.5 (Detection and Response) - score: 18.4
  2. IMP-3.2 (Incident Reporting) - score: 15.2
  3. CSP-6.6 (Audits) - score: 8.1

Vector Results:
  1. IMP-3.2 (Incident Reporting) - score: 0.89
  2. CSP-6.5 (Detection and Response) - score: 0.85
  3. IMP-4.1 (Escalation Procedures) - score: 0.78

HyDE Results:
  1. IMP-3.2 (Incident Reporting) - score: 0.92
  2. IMP-3.3 (Regulatory Notification) - score: 0.88
  3. CSP-6.5 (Detection and Response) - score: 0.84

Graph Expansion:
  - IMP-3.2 mentions CERT-IN → expand to IMP-3.3, IMP-4.1
  - CSP-6.5 references IMP → include IMP-2.0
```

**Step 3 - Fusion (RRF):**
```
1. IMP-3.2 (Incident Reporting) - fused: 0.048
2. CSP-6.5 (Detection and Response) - fused: 0.045
3. IMP-3.3 (Regulatory Notification) - fused: 0.032
4. IMP-4.1 (Escalation Procedures) - fused: 0.028
```

**Step 4 - Reranking:**
```
1. IMP-3.2 - rerank: 0.94 ✓
2. IMP-3.3 - rerank: 0.91 ✓
3. CSP-6.5 - rerank: 0.82 ✓
4. IMP-4.1 - rerank: 0.45 ✗ (below threshold)
```

**Step 5 - LLM Synthesis:**
```json
{
  "coverage": "PARTIAL",
  "mapped_sections": [
    {
      "section_id": "IMP-3.2",
      "title": "Incident Reporting",
      "relevance": "Addresses incident reporting to regulators",
      "excerpt": "Cyber Incidents will be communicated to respective regulators as per regulatory requirements"
    },
    {
      "section_id": "IMP-3.3",
      "title": "Regulatory Notification",
      "relevance": "Specifies CERT-IN notification",
      "excerpt": "Incidents shall be reported to CERT-IN..."
    }
  ],
  "gaps": [
    {
      "aspect": "6-hour timeline",
      "issue": "Policy does not specify the 6-hour reporting window explicitly"
    }
  ],
  "recommendation": "Update IMP-3.2 to include explicit 6-hour timeline for CERT-IN reporting"
}
```

---

## Performance Targets

| Metric | Target |
|--------|--------|
| Query latency (p95) | < 3 seconds |
| Recall@10 | > 0.85 |
| Precision@5 | > 0.80 |
| Coverage accuracy | > 90% |

---

## Next Steps

1. [ ] Set up vector database (Qdrant recommended for hybrid)
2. [ ] Build BM25 index from converted policies
3. [ ] Implement HyDE generation pipeline
4. [ ] Build knowledge graph from extracted entities
5. [ ] Implement fusion and reranking
6. [ ] Build evaluation dataset from known CSCRF mappings
