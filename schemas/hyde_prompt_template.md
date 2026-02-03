# HyDE Prompt Templates

This document defines prompt templates for Hypothetical Document Embedding (HyDE) in the compliance mapping system.

---

## Overview

HyDE bridges the vocabulary gap between:
- **Regulatory language** (formal, prescriptive, uses terms like "shall", "MIs", "REs")
- **Policy language** (internal, procedural, uses org-specific terminology)

By generating a hypothetical policy section that *would* address the regulation, we can find semantically similar real sections.

---

## Template 1: Regulation → Hypothetical Policy Section

**Use case:** User pastes a SEBI CSCRF requirement, generate a hypothetical internal policy section.

```
SYSTEM:
You are an expert compliance officer at a financial services organization (stock broker) in India.
You write internal security policies that address regulatory requirements from SEBI, ISO 27001, and CERT-IN.

Your organization uses this terminology:
- "CISO" or "Chief Information Security Officer" for security leadership
- "Information Security Team" for the security operations group
- "Critical Cyber Assets" for high-value systems
- Controls are annotated as [[control:Control Name]]
- Roles are annotated as [[role:Role Name]]
- Assets are annotated as [[asset:Asset Name]]

USER:
Given the following regulatory requirement, write a hypothetical internal policy section that would fully address this requirement.

**Regulatory Requirement:**
{requirement_text}

**Instructions:**
1. Write 1-2 paragraphs that would appear in an internal policy document
2. Use section heading format: ### Section Title
3. Prefix mandatory items with **[MANDATORY]**
4. Include specific controls, frequencies, and responsible roles
5. Use [[control:...]], [[role:...]], [[asset:...]] annotations
6. Be specific - mention concrete measures, not vague statements
7. Match the tone of an ISO 27001-aligned ISMS policy

**Output format:**
### [Appropriate Section Title]
<!-- likely_maps_to: [relevant keywords] -->

[Policy content addressing the requirement]
```

---

## Template 2: Regulation → Multiple Hypothetical Sections

**Use case:** A regulation might be addressed across multiple policy sections. Generate several hypothetical sections.

```
SYSTEM:
You are an expert compliance officer mapping regulatory requirements to internal policies.

USER:
The following regulatory requirement may be addressed across multiple internal policy sections (e.g., Access Control Policy, Incident Management Policy, Network Security Policy).

**Regulatory Requirement:**
{requirement_text}

Generate 2-3 SHORT hypothetical policy excerpts from DIFFERENT policy domains that would collectively address this requirement.

**Output format:**
---
**Domain: [Policy Domain, e.g., "Access Control"]**
### [Section Title]
[1-2 sentences of policy content]
---
**Domain: [Another Policy Domain]**
### [Section Title]
[1-2 sentences of policy content]
---
```

---

## Template 3: Keyword Expansion for BM25

**Use case:** Generate keyword variations to improve BM25 recall.

```
SYSTEM:
You are a compliance terminology expert.

USER:
Given this regulatory requirement, list all synonyms, related terms, and keyword variations that might appear in internal policy documents addressing this requirement.

**Regulatory Requirement:**
{requirement_text}

**Output format (JSON):**
{
  "primary_keywords": ["exact terms from the requirement"],
  "synonyms": ["alternative terms with same meaning"],
  "related_controls": ["specific security controls that address this"],
  "related_processes": ["business/IT processes involved"],
  "regulatory_references": ["standards/frameworks this relates to"]
}
```

---

## Template 4: Gap Analysis Prompt

**Use case:** After retrieval, analyze whether the retrieved sections fully address the requirement.

```
SYSTEM:
You are a compliance auditor analyzing whether internal policies adequately address regulatory requirements.

USER:
**Regulatory Requirement:**
{requirement_text}

**Retrieved Policy Sections:**
{retrieved_sections}

**Instructions:**
Analyze the coverage and provide:

1. **Coverage Assessment:** FULL | PARTIAL | NOT_COVERED

2. **Mapping Details:** For each aspect of the requirement, identify which policy section addresses it.

3. **Gaps Identified:** What aspects of the requirement are NOT addressed by the retrieved sections?

4. **Recommendations:** What additional policy content would be needed to achieve full compliance?

**Output format:**
```json
{
  "coverage": "PARTIAL",
  "mappings": [
    {
      "requirement_aspect": "MFA for privileged access",
      "covered_by": "CSP-6.3.2",
      "excerpt": "relevant quote from policy",
      "coverage_strength": "STRONG"
    }
  ],
  "gaps": [
    {
      "requirement_aspect": "MFA for remote access",
      "gap_description": "Policy mentions MFA for privileged accounts but not specifically for remote access scenarios"
    }
  ],
  "recommendations": [
    "Add explicit requirement for MFA on all remote access connections"
  ]
}
```

---

## Template 5: Entity Extraction for GraphRAG

**Use case:** Extract entities and relationships from policy sections for knowledge graph construction.

```
SYSTEM:
You are an NLP system extracting entities and relationships from security policy documents.

USER:
Extract all entities and their relationships from this policy section:

**Policy Section:**
{section_text}

**Entity Types:**
- ROLE: Organizational roles (CISO, IT Team, etc.)
- CONTROL: Security controls (MFA, Firewall, Encryption, etc.)
- ASSET: Information assets (servers, databases, etc.)
- PROCESS: Business/IT processes (incident management, access review, etc.)
- REGULATION: Regulatory frameworks (ISO 27001, SEBI CSCRF, etc.)
- EXTERNAL: External parties (CERT-IN, vendors, etc.)
- FREQUENCY: Time-based requirements (annually, 180 days, etc.)

**Relationship Types:**
- RESPONSIBLE_FOR: Role → Process/Control
- IMPLEMENTS: Process → Control
- PROTECTS: Control → Asset
- REQUIRES: Regulation → Control
- REPORTS_TO: Role → Role
- FREQUENCY_OF: Frequency → Process

**Output format (JSON):**
{
  "entities": [
    {"text": "CISO", "type": "ROLE", "normalized": "Chief Information Security Officer"}
  ],
  "relationships": [
    {"source": "CISO", "target": "access review", "type": "RESPONSIBLE_FOR"}
  ]
}
```

---

## Configuration Parameters

```yaml
hyde:
  model: "gpt-4o"  # or claude-3-sonnet for cost efficiency
  temperature: 0.3  # Low temp for consistency
  max_tokens: 500   # Keep hypothetical docs focused

  # Number of hypothetical docs to generate per query
  num_hypothetical_docs: 3

  # Whether to use multi-domain generation
  multi_domain: true

  # Domains to consider for multi-domain generation
  domains:
    - "Access Control"
    - "Network Security"
    - "Incident Management"
    - "Data Protection"
    - "Business Continuity"
    - "Vendor Management"
    - "Security Operations"
```

---

## Example: End-to-End HyDE Flow

**Input Regulation:**
> "Market Infrastructure Institutions shall ensure that multi-factor authentication is implemented for all users accessing critical systems, with mandatory enforcement for privileged accounts."

**Generated Hypothetical Section:**
```markdown
### Multi-Factor Authentication Requirements
<!-- likely_maps_to: ["MFA", "privileged access", "critical systems", "authentication"] -->

- **[MANDATORY]** All users accessing [[asset:critical cyber assets]] shall authenticate using [[control:Multi-factor Authentication]].

- **[MANDATORY]** [[role:Information Security Team]] shall enforce MFA for all [[asset:privileged accounts]] with no exceptions unless formally approved by [[role:CISO]].

- **[MANDATORY]** MFA shall be implemented using approved methods including hardware tokens, authenticator apps, or biometric verification. SMS-based OTP is not permitted for privileged access.
```

**Retrieved Real Sections:**
1. `CSP-6.3.2` (Logical Access Security) - Similarity: 0.91
2. `LAC-4.1` (Authentication Controls) - Similarity: 0.87
3. `ISP-5.2` (Access Management) - Similarity: 0.82

---

## Notes for Implementation

1. **Embedding Model:** Use the same embedding model for hypothetical and real documents
2. **Chunking Alignment:** Hypothetical docs should be similar length to real chunks
3. **Batch Processing:** For bulk regulation mapping, batch HyDE generation for efficiency
4. **Caching:** Cache hypothetical docs for repeated queries
5. **Fallback:** If HyDE retrieval confidence is low, fall back to direct embedding + BM25
