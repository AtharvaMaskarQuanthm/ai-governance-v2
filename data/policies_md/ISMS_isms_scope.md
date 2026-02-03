```yaml
---
document_id: "ISMS"
title: "ISMS Scope"
filename: "ISMS SCOPE.pdf"
version: "1.1"
status: "approved"
created_date: "2024-11-11"
effective_date: null
last_reviewed: "2025-01-17"
next_review: null

owner:
  name: "Ajay Kejriwal"
  role: "CEO"

prepared_by:
  - name: "Abhishek Vinayak"
    role: "Associate Information Security"

approved_by:
  - name: "Ashutosh Bhardwaj"
    role: "CISO"
    date: "2025-01-17"
  - name: "Yogesh Jadhav"
    role: "CTO"
    date: "2025-01-08"
  - name: "Ajay Kejriwal"
    role: "CEO"
    date: "2025-01-09"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
  - id: "IT-Act-2008"
    name: "IT Act 2008"
  - id: "CERT-IN"
    name: "CERT-IN guidelines"
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"

references:
  - document_id: "SOA"
    title: "Statement of Applicability"
    relationship: "related"

scope:
  description: "Defines the detailed scope of the ISMS in CHOICE EQUITY BROKING PVT. LTD."
  inclusions:
    - "Front, middle, and back office operations for trading services"
  exclusions:
    - "Any Choice subsidiaries not captured as part of the scope document"
    - "Any other offices of choice not captured as part of the scope document"

entities:
  roles:
    - "CISO"
    - "CTO"
    - "CEO"
    - "Executive Management"
  controls:
    - "Physical Security"
    - "Network & Telephony Connections"
  assets:
    - "IT Infrastructure"
    - "Data Centers"
  processes:
    - "Internal Audit"
    - "Business Continuity"
  external_parties:
    - "SEBI"
    - "NSE"
    - "BSE"
    - "MCX"
    - "NCDEX"
    - "NSDL"
    - "CDSL"
    - "CERT-IN"

tags:
  - "ISMS"
  - "Scope"
  - "Information Security"
---
```

## ISMS Scope
<!-- section_id: ISMS-1 -->

### 1.0 Purpose
<!-- section_id: ISMS-1.0 -->

The ISMS Scope document defines the detailed scope of the ISMS in [[external:CHOICE EQUITY BROKING PVT. LTD.]], its users, locations, and any other exclusions to the ISMS application.

### 2.0 ISMS Scope
<!-- section_id: ISMS-2.0 -->

**Service Scope**

The ISMS of [[external:Choice Equity Broking Pvt. Ltd.]] covers front, middle, and back office operations for trading services supported by admin, HR, Legal & Compliance, IT services from:

- Choice Equity Broking Pvt Ltd, Head Office - 1st and 2nd Floor, Sunil Patodia Tower, JB Nagar, Andheri East - Mumbai
- Primary Data Center - NTT, DC 7, Lighthall 'E' Wing, Hiranandani Business Park, Hiranandani Lighthall, Saki Vihar Rd, Muranjan Wadi, Chandivali, Andheri East, Mumbai, Maharashtra 400072
- Disaster Recovery Data Center - SURVEY NO.115 SIFY INFINIT SPACES LIMITED NANAKRAMGUDA, FINANCIAL DISTRICT, HYDERABAD-500032

The in-scope controls along with justification for out-of-scope controls (if any) are articulated in [[doc:SOA]] attached herein.

### 3.0 Organization & Business Context
<!-- section_id: ISMS-3.0 -->

[[external:Choice Equity Broking Pvt. Ltd.]] provides online securities trading facility to its customers. It avails the following services provided by IT and security services vendors:

- Application support provided to clients and partners
- Underlying infrastructure to support the business including operating system, network, email & databases
- IT processes adopted & practiced to protect the information assets.

#### 3.1 Support Function & Its Dependencies
<!-- section_id: ISMS-3.1 -->

**Interfaces Dependencies**

- **External**
  - HR department manages the life cycle of employees and provides background verification services.
  - IT department depends on [[process:business continuity]] to provide a framework for IT service continuity strategy & planning.

- **Internal**
  - Facilities Management Services: FMG department provides physical security and manages PDC & DR environment controls for IT.
  - Service Providers: IT department depends on ISPs for network & telephony connections.
  - Contractors & Consultants: IT department depends on vendors for providing equipment & its maintenance & support including, Consulting, VAPT, Security Tools.
  - Government and Legal Bodies: Depends on the regulators for guidelines and frameworks for Equity broking Services.

### 3.2 Interested Parties
<!-- section_id: ISMS-3.2 -->

- **A. Government & Regulators-SEBI, NSE/BSE**

  [[external:CHOICE EQUITY BROKING PVT. LTD.]] needs to comply with [[regulatory_frameworks:IT-Act-2008]] and [[external:CERT-IN]] guidelines related to cyber security and privacy. It also needs to comply with various circulars issued by [[external:SEBI]], [[external:NSE]], [[external:BSE]], [[external:MCX]], [[external:NCDEX]], [[external:NSDL]], and [[external:CDSL]] related to cyber security and resilience.

- **B. Executive Management**

  Executive management at [[external:CHOICE EQUITY BROKING PVT. LTD.]] needs to protect information to mitigate the risk which may have financial, operational, reputational & compliance impact. The IT department needs to understand & manage information security requirements of management and board of directors by ensuring confidentiality, integrity & availability of information. It also needs to allocate budget, resources & time by assessing cost-benefit analysis.

- **C. Customers**

  [[external:CHOICE EQUITY BROKING PVT. LTD.]] handles personally identifiable as well as financial information of their customers. It is responsible for protecting this information. Customers need assurance that trade transactions are conducted in a safe and secure manner.

- **D. Vendors & Contractors**

  Vendors provide licensed software & various proprietary information. [[external:CHOICE EQUITY BROKING PVT. LTD.]] & vendors have signed a non-disclosure agreement on a reciprocal basis. Besides, certain vendors & contractors provide remote support for its IT infrastructure. It must be ensured that vendors & contractors abide by the confidentiality agreement of the IT department. Similarly, the IT department abides by non-disclosure, licensing agreement of software publishers & any other intellectual property rights.

#### 3.2.1 External and Internal Issues
<!-- section_id: ISMS-3.2.1 -->

**Internal Issues**

- IT hardware and software failures.
- Insider threats
- Business strategies
- Management directions

**External Issues**

- Cyber-attacks targeting at national level and financial sector including securities trading and operations.
- Data theft of personal identifiable and financial information of customers.
- Compliance with regulations and observations made if any.
- Natural Disasters, Environmental hazards and Climate changes

### 4.0 ISMS Exclusions
<!-- section_id: ISMS-4.0 -->

The following are excluded from the scope:

- Any Choice subsidiaries not captured as part of the scope document
- Any other offices of choice not captured as part of the scope document
```