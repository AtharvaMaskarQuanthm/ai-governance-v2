```yaml
---
document_id: "DCP"
title: "Data Classification Policy"
filename: "Data Classification Policy.pdf"
version: "2.1"
status: "approved"
created_date: "2016-10-17"
effective_date: null
last_reviewed: "2024-01-31"
next_review: null

owner:
  name: "Ashutosh Bhardwaj"
  role: "Policy Owner"

prepared_by:
  - name: "Mahesh Tamhankar"
    role: "Policy Preparer"
  - name: "Sunil Utekar"
    role: "Policy Preparer"
  - name: "Ashutosh Bhardwaj"
    role: "Policy Preparer"

approved_by:
  - name: "Yogesh Jadhav"
    role: "Policy Approver"
    date: "2024-01-31"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"

regulatory_frameworks:
  - id: "SEBI-CSCRF"
    name: "SEBI CyberSecurity Framework"

references:
  - document_id: "IMP"
    title: "Incident Management Policy"
    relationship: "related"

scope:
  description: "Policy for classifying data based on sensitivity to prevent data leakage and ensure compliance."
  inclusions:
    - "Data classification"
    - "Data protection"
  exclusions:
    - "Non-sensitive data not related to PII"

entities:
  roles:
    - "Developer"
    - "DevOps"
  controls:
    - "DLP Software"
    - "Encryption"
  assets:
    - "Servers"
    - "Databases"
    - "API Endpoints"
    - "File Storage"
    - "Media Storage"
    - "Redis / Elastic"
    - "S3"
    - "Network Access"
    - "Data Center Hardware"
    - "Trading System"
    - "LMS Software"
    - "KYC Software"
    - "Back Office Software"
    - "RMS"
    - "MF Back Office Software"
    - "Partner System"
    - "Insurance Back Office System"
    - "Physical Documents"
  processes:
    - "Data Classification"
    - "Data Leakage Protection"
    - "Risk Assessment"
    - "Security Audits"
  external_parties:
    - "SEBI"

tags:
  - "data classification"
  - "PII"
  - "data protection"
  - "compliance"
---
# Data Classification Policy
<!-- section_id: DCP-1.0 -->

## Overview
<!-- section_id: DCP-1.1 -->
To implement the security policy and prevent [[PII]] data leakage. It also improves compliance and helps organizations adhere to data protection regulations. Data classification is important because it allows organizations to understand the types of information they are processing and storing. The knowledge gained through data classification allows a company to take the necessary measures to protect the data based on its importance or sensitivity.

## What is Personally Identifiable Information (PII)?
<!-- section_id: DCP-1.2 -->
**Personally Identifiable Information (PII)**
: Includes any information that can be used to distinguish or trace an individual’s identity, such as name, social security number, date and place of birth, mother’s maiden name, or biometric records. It also includes any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information.

Examples of PII include, but are not limited to:
- Name: full name, father’s name, mother’s name, nominee name.
- Date of birth.
- Personal identification numbers: passport number, driver’s license number, PAN number, Bank account number, or credit card number.
- Personal address information: street address, or email address.
- Personal Mobile numbers.
- Personal characteristics: photographic images (particularly of face or other identifying characteristics), fingerprints, or handwriting.

## Data Types
<!-- section_id: DCP-1.3 -->
**Highly Sensitive Data**
: A data point which represents or can be used to identify a unique customer/entity in the system and associated permanently with the customer/entity. Example: PII Data.

**Medium Sensitive Data**
: A data point assigned to customer/entity to be used by internal team members to address customer/entity. Example: Client Id or a unique customer identifier.

**Non-sensitive Data**
: A data point which is system generated and does not hold any significant value individually. Example: System generated dates (createdOn, modifiedOn), System Generated Flags.

## Data Leakage Protection
<!-- section_id: DCP-1.4 -->
**Data Classification**
: Implement a data classification scheme to categorize data based on sensitivity (e.g., public, internal, confidential). Ensure that employees understand which types of data are considered sensitive and require extra protection.

**Data Loss Prevention Software**
: Implement [[control:DLP Software]] to monitor and block unauthorized data transfers (e.g., to USB devices, cloud storage, or external email). Configure the DLP system to detect attempts to send, print, or copy sensitive information outside the organization.

## Goals
<!-- section_id: DCP-1.5 -->
1. **[MANDATORY]** To protect all types of data that are associated with the organization and can potentially expose the customer/entity.
2. **[MANDATORY]** To protect user and organization data from unauthorized access.
3. **[MANDATORY]** To follow the compliance rules and regulations.
4. **[MANDATORY]** Proper Authentication/Authorization to access data on [[asset:servers]] and [[asset:databases]].

## Classification Levels
<!-- section_id: DCP-1.6 -->
### Developer
<!-- section_id: DCP-1.6.1 -->
1. **[MANDATORY]** While logging data avoid logging PII data (PAN, Mobile, email, etc.) in log files.
2. **[MANDATORY]** While logging PII data is unavoidable then keep it masked.
3. **[MANDATORY]** PII files should be privately accessible (PAN, AADHAR, SELFIE).
4. **[MANDATORY]** Do not use PII data as file name use.
5. **[MANDATORY]** While storing data use [[control:encryption]] mechanisms to store PII data in [[asset:databases]], elastic, redis, etc.
6. **[MANDATORY]** Follow relevant compliance rules and regulations like [[external:SEBI]] CyberSecurity Framework.

### DevOps
<!-- section_id: DCP-1.6.2 -->
1. **[MANDATORY]** At the time of server to server communication, use a private network for data transferring.
2. **[MANDATORY]** Authorize/Authenticate users properly.
3. **[MANDATORY]** While logging data, avoid logging PII data in log files.
4. **[MANDATORY]** Limit database and server and maintain proper user permission.
5. **[MANDATORY]** Conduct security audits on a regular basis.

### Organization
<!-- section_id: DCP-1.6.3 -->
1. **[MANDATORY]** Conduct regular risk assessments to identify potential security vulnerabilities and prioritize actions to mitigate risks.
2. **[MANDATORY]** Limit access to sensitive data to only those who need it.
3. **[MANDATORY]** Educate employees on data security best practices and provide regular training on how to identify and respond to security incidents.
4. **[MANDATORY]** Use internal tools for data analytics and visualization.

## Business Entity Assets / Software Under Protection
<!-- section_id: DCP-1.7 -->
| Business Entity  | Assets / Software Under Protection | Sensitivity Level |
|------------------|------------------------------------|-------------------|
| CEBPL            | Data Center Hardware               | HIGH              |
| CEBPL            | Trading System                     | HIGH              |
| CEBPL            | LMS Software                       | HIGH              |
| CEBPL            | KYC Software                       | HIGH              |
| CEBPL            | Back Office Software               | HIGH              |
| CEBPL            | RMS                                | HIGH              |
| CWMPL            | MF BACK OFFICE SOFTWARE            | HIGH              |
| CHOICE CONNECT   | Partner System                     | HIGH              |
| CHOICE INSURANCE | Insurance Back Office System       | HIGH              |
| CEBPL            | KYC Department - Physical Documents| HIGH              |

## Authority / Regularity
<!-- section_id: DCP-1.8 -->
1. **[MANDATORY]** We can educate employees on data security best practices and provide regular training on how to identify and respond to security incidents.
2. **[MANDATORY]** Can implement access controls, as they are critical for ensuring that only authorized users have access to the organization's data assets. Access controls can include user authentication, role-based access controls, and data encryption.
3. **[MANDATORY]** Can conduct security audits on a regular basis.
4. **[MANDATORY]** The authority can check whether the system complies with relevant regulations, standards, and guidelines.
```
