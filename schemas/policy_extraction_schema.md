# Policy Extraction Schema

This schema defines the structured markdown format for converting internal policy PDFs into a format optimized for:
1. **Hybrid RAG retrieval** (semantic search + keyword matching)
2. **GraphRAG** (entity/relationship extraction)
3. **Compliance mapping** (tracing regulatory requirements to policy sections)

---

## 1. Document Structure Overview

```
┌─────────────────────────────────────────────────────────┐
│  YAML Frontmatter (metadata)                            │
├─────────────────────────────────────────────────────────┤
│  # Document Title                                       │
│                                                         │
│  ## 1.0 Section                                         │
│  <!-- section_id: POL-SEC-1.0 -->                       │
│                                                         │
│  ### 1.1 Subsection                                     │
│  <!-- section_id: POL-SEC-1.1 -->                       │
│                                                         │
│  Content with [[entity:ROLE:CISO]] annotations          │
│                                                         │
│  > [!CROSS-REF]                                         │
│  > References: [[doc:incident-management-policy]]       │
└─────────────────────────────────────────────────────────┘
```

---

## 2. YAML Frontmatter Schema

Every converted policy document MUST have this frontmatter:

```yaml
---
# === DOCUMENT IDENTIFICATION ===
document_id: "CSP"                          # Unique short identifier
title: "Cyber Security Policy"              # Full title
filename: "Choice-ISMS-CyberSecurity Policy.pdf"  # Original PDF filename

# === VERSION CONTROL ===
version: "2.3"
status: "approved"                          # draft | review | approved | superseded
created_date: "2016-10-17"
effective_date: "2025-01-08"
last_reviewed: "2025-04-07"
next_review: "2026-04-07"                   # If specified in document

# === OWNERSHIP ===
owner:
  name: "Ashutosh Bhardwaj"
  role: "CISO"
  email: null                               # If available

prepared_by:
  - name: "Abhishek Vinayak"
    role: "Associate, Information Security"

approved_by:
  - name: "Yogesh Jadhav"
    role: "CTO"
    date: "2025-01-08"

# === CLASSIFICATION ===
classification: "Internal"                  # Public | Internal | Confidential | Restricted
applies_to:
  - "employees"
  - "contractors"
  - "vendors"
  - "third-party staff"

# === REGULATORY & FRAMEWORK ALIGNMENT ===
regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
    clauses: ["5.1", "6.1", "7.5"]          # Specific clauses addressed
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"
    reference: "SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113"
  - id: "CERT-IN"
    name: "CERT-IN Guidelines"

# === INTERNAL REFERENCES ===
references:
  - document_id: "ISP"
    title: "Information Security Policy"
    relationship: "parent"                  # parent | child | related | supersedes
  - document_id: "IMP"
    title: "Incident Management Policy"
    relationship: "related"

# === DOCUMENT SCOPE ===
scope:
  description: "Defines cyber security controls and operations"
  inclusions:
    - "All IT infrastructure"
    - "All business applications"
    - "Network security"
  exclusions:
    - "Physical security (covered in separate policy)"

# === EXTRACTED ENTITIES (for GraphRAG) ===
entities:
  roles:
    - "CISO"
    - "Information Security Team"
    - "IT Department"
    - "Technology Committee"
  controls:
    - "Multi-factor Authentication"
    - "Intrusion Detection System"
    - "Firewall"
    - "Encryption"
  assets:
    - "Critical Cyber Assets"
    - "Network Devices"
    - "Servers"
    - "Databases"
  processes:
    - "Incident Management"
    - "Vulnerability Assessment"
    - "Penetration Testing"
    - "Access Review"
  external_parties:
    - "CERT-IN"
    - "SEBI"
    - "NSE"
    - "BSE"

# === TAGS (for search enhancement) ===
tags:
  - "cyber security"
  - "access control"
  - "incident response"
  - "vulnerability management"
  - "network security"
---
```

---

## 3. Section Structure

### 3.1 Section IDs

Every section MUST have a unique, hierarchical ID embedded as an HTML comment:

```markdown
## 6.0 Cyber Security Operations
<!-- section_id: CSP-6.0 -->

### 6.1 Critical Cyber Asset Identification
<!-- section_id: CSP-6.1 -->

#### Physical Access Security
<!-- section_id: CSP-6.3.1 -->
```

**ID Format:** `{DOCUMENT_ID}-{SECTION_NUMBER}`

This enables precise citations like: *"Covered in CSP-6.3.1 (Physical Access Security)"*

### 3.2 Section Metadata Block (Optional)

For sections with specific compliance relevance:

```markdown
### 6.3 Security Controls Management and Monitoring
<!-- section_id: CSP-6.3 -->
<!-- controls: ["access control", "monitoring", "logging"] -->
<!-- frameworks: ["ISO27001:A.9", "SEBI-CSCRF:4.2"] -->
```

---

## 4. Content Formatting

### 4.1 Requirements and Controls

Use structured lists with clear imperative language:

```markdown
- **[MANDATORY]** Physical access to critical cyber assets must be limited to authorized personnel only.
- **[MANDATORY]** Access logs shall be retained for minimum 180 days.
- **[RECOMMENDED]** Implement biometric authentication for data center access.
```

### 4.2 Entity Annotations (for GraphRAG)

Annotate key entities inline for relationship extraction:

```markdown
The [[role:CISO]] shall approve all exceptions to this policy.

All [[asset:critical cyber assets]] must be protected using [[control:encryption]].

Incidents shall be reported to [[external:CERT-IN]] within 6 hours.
```

**Entity Types:**
- `[[role:...]]` — Organizational roles
- `[[control:...]]` — Security controls
- `[[asset:...]]` — Information assets
- `[[process:...]]` — Business/IT processes
- `[[external:...]]` — External parties/regulators
- `[[doc:...]]` — Internal document references
- `[[framework:...]]` — Regulatory framework references

### 4.3 Cross-References

Use callout blocks for cross-references:

```markdown
> [!CROSS-REF]
> For detailed incident handling procedures, refer to [[doc:incident-management-policy]].
```

### 4.4 Tables

Preserve tables in markdown format with clear headers:

```markdown
| Asset Type | Audit Type | Frequency |
|------------|------------|-----------|
| Web Applications | Internal VAPT | After every major release |
| Web Applications | External CERT-IN VAPT | Bi-annually |
| Firewalls | Internal VAPT | Quarterly (Rule Reviews) |
```

### 4.5 Definitions

Use definition list format:

```markdown
**Cyber Security Event**
: An event or anomaly detected by a security device, service, application, process or human on a technology infrastructure environment.

**Cyber Security Incident**
: Any malicious act or suspicious event that compromises or attempts to compromise the electronic, physical and logical security of a critical cyber asset.
```

---

## 5. Compliance Mapping Hints

To optimize for regulatory mapping, sections should include hints where obvious:

```markdown
### 6.5 Detection and Response
<!-- section_id: CSP-6.5 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["incident detection", "SOC operations", "SIEM", "log monitoring"] -->

- Security Operations Center shall be established to enable log aggregation...
```

The `likely_maps_to` field contains keywords that help match against regulatory requirements.

---

## 6. File Naming Convention

```
{document_id}_{snake_case_title}.md

Examples:
- CSP_cyber_security_policy.md
- ISP_information_security_policy.md
- IMP_incident_management_policy.md
- DCP_data_classification_policy.md
```

---

## 7. Directory Structure

```
data/
├── policies/                    # Original PDFs (source of truth)
│   └── *.pdf
├── policies_md/                 # Converted structured markdown
│   ├── CSP_cyber_security_policy.md
│   ├── ISP_information_security_policy.md
│   └── ...
└── policies_extracted/          # JSON exports for graph ingestion
    ├── entities.json            # All extracted entities
    ├── relationships.json       # Entity relationships
    └── sections.json            # Section metadata for indexing
```

---

## 8. Validation Checklist

Before considering a policy conversion complete:

- [ ] Frontmatter includes all required fields
- [ ] Every section has a unique `section_id`
- [ ] Version matches the source PDF
- [ ] All tables are properly formatted
- [ ] Cross-references use `[[doc:...]]` syntax
- [ ] Key entities are annotated (at least roles and controls)
- [ ] No content is lost from original PDF
- [ ] Regulatory frameworks are accurately listed
