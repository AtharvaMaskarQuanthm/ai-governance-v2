Compliance processes in most organizations are highly manual and inefficient. Regulatory requirements are typically maintained in spreadsheets where auditors manually map individual compliance guidelines to internal policy documents. These spreadsheets are then shared with the CISO or compliance leadership, who often respond by attaching or linking large policy PDFs without clearly demonstrating how specific regulatory requirements are addressed.

This workflow leads to several issues:

- Lack of traceability between regulatory guidelines and internal controls

- High dependence on manual interpretation and judgment

- Poor explainability during audits

- Significant time and effort spent reviewing large policy documents

- Increased risk of missed or weakly mapped compliance requirements

To address this, the goal is to build an agentic, hybrid retrieval-augmented generation (RAG) system that takes a regulatory guideline (for example, from SEBI’s CSCRF framework) as input and automatically identifies the most relevant sections from an organization’s internal policy documents stored as PDFs.

The system should leverage multiple retrieval strategies—including lexical search (BM25), dense vector search, HyDE-based query expansion, and graph-based retrieval—to ensure high recall and precision. It must provide explainable mappings between regulatory requirements and internal policies, clearly indicating why a particular policy section is relevant and where gaps may exist.
