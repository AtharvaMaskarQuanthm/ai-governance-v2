```yaml
---
document_id: "DDR"
title: "Data Disposal and Retention Policy"
filename: "Choice-ISMS-Data disposal & retention POLICY.pdf"
version: "2.1"
status: "approved"
created_date: "2016-10-17"
effective_date: null
last_reviewed: "2024-01-31"
next_review: null

owner:
  name: "Ashutosh Bhardwaj"
  role: "Role Title"

prepared_by:
  - name: "Anil Ashok & Associates"
    role: "Role Title"

approved_by:
  - name: "Ashutosh Bhardwaj"
    role: "Role Title"
    date: "2024-01-31"

classification: "Internal"
applies_to:
  - "employees"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2013"

references: []

scope:
  description: "Practices for secure data disposal and retention"
  inclusions:
    - "All employees with data access"
  exclusions:
    - "Non-employees"

entities:
  roles:
    - "IT Manager"
    - "CTO"
  controls:
    - "Shredder"
    - "Pulping"
  assets:
    - "Paper Records"
    - "Equipment"
  processes:
    - "Data Maintenance"
    - "Data Retention"
    - "Data Disposal"
  external_parties: []

tags:
  - "data retention"
  - "data disposal"
  - "compliance"
---
```

```markdown
## 1. Scope
<!-- section_id: DDR-1.0 -->
The aim of [[doc:Data Disposal and Retention Policy]] is to set out practices to be followed for ensuring the information that is supposed to be disposed is not stolen or misused and maintained securely. This is applicable to all the [[role:employees]] of Choice Equity Broking Pvt. Ltd. who have access to data.

## 2. Purpose
<!-- section_id: DDR-2.0 -->
The purpose of the policy is to ensure that data is handled in a manner that the confidentiality, integrity, and availability of the data are not compromised. It also ensures that data is adequately protected and maintained and to ensure that data is no longer needed or have no value are destroyed at the appropriate time.

## 3. Procedure Section and Clauses
<!-- section_id: DDR-3.0 -->
Data is “information created, received, and maintained as evidence and information by any individual in the organization, in pursuance of legal/statutory/contractual obligations or in the transaction of business.

### 3.1 Data Maintenance
<!-- section_id: DDR-3.1 -->
- **[MANDATORY]** Data shall be maintained for the client audits as a part of compliance requirement and deemed necessary by virtue of a legal or a statutory requirement.
- **[MANDATORY]** Data shall be maintained in a protective environment, safeguarding them against deterioration, damage by environmental or deliberate threats.
- **[MANDATORY]** Electronic storage media shall be ensured for the ability to read data throughout the retention period and safeguarded against loss of readability due to technology change.
- **[MANDATORY]** Choice Equity Broking Pvt. Ltd. shall establish and maintain procedures for identifying, maintaining, retaining, and disposal of data.
- **[MANDATORY]** Data should be kept securely and made available to authorized persons when required.

### 3.2 Data Retention Period
<!-- section_id: DDR-3.2 -->
- **[MANDATORY]** For customer-specific application data, the retention period will be defined in the Choice Equity Broking Pvt. Ltd. systems as a part of internal retention periods.
- **[MANDATORY]** For Choice Equity Broking Pvt. Ltd. owned data, the length of the retention period is based on the likelihood that the evidence will be needed at some point in the future.
- **[MANDATORY]** Evidences and Audit Reports that will serve no further purpose (as determined by the length of their retention period) will be destroyed. As in documents, records which are in soft copy format, shall be reviewed and deleted post authorization.
- **[MANDATORY]** Client Records and KYC: Maintain Know Your Customer (KYC) documents, client identification records, and account opening forms for a minimum of 8 years from the date of the last transaction with the client.
- **[MANDATORY]** Books of Accounts and Financial Records: Maintain books of accounts, ledgers, balance sheets, and profit & loss accounts for 5 years.
- **[MANDATORY]** Transaction Records: Maintain records of client transactions, including order logs, trade logs, and contract notes, for 5 years or until the case is settled, in case of disputes or complaints.

### 3.3 Data Disposal
<!-- section_id: DDR-3.3 -->
- **[MANDATORY]** Choice Equity Broking Pvt. Ltd. shall identify data to be disposed.
- **[MANDATORY]** Data shall be disposed in a protective environment and under the supervision of [[role:IT Manager]] with prior approvals from [[role:CTO]].

#### 3.3.1 Paper Records
<!-- section_id: DDR-3.3.1 -->
- **[MANDATORY]** Paper record to be disposed of are to be segregated from the paper documents that are going to be used.
- **[MANDATORY]** Employees of Choice Equity Broking Pvt. Ltd. must make sure that they don’t dispose documents that are required.
- **[MANDATORY]** Wherever required, [[control:shredder]] OR [[control:pulping]] method is to be used to shred/pulp the unwanted paper documents.

#### 3.3.2 Equipment
<!-- section_id: DDR-3.3.2 -->
- **[MANDATORY]** [[role:IT team]] must ensure equipment productivity after its depreciation period. If the equipment is not functioning to meet the business requirements of Choice Equity Broking Pvt. Ltd., then [[role:IT team]] of Choice Equity Broking Pvt. Ltd. can take a call to scrap/donate/sell the equipment.
- **[MANDATORY]** The equipment’s memory elements have to be damaged beyond repair and other parts can be disposed-off by destroying them or sending them for recycling.
- **[MANDATORY]** In case of donating/selling the equipment, it has to be ensured that the memory elements of the equipment are formatted thoroughly and tested to see if data can be still retrieved.
- **[MANDATORY]** If it is possible to retrieve data, the equipment’s memory elements should be removed, and the rest of the equipment can be donated.

## 4. Enforcement
<!-- section_id: DDR-4.0 -->
Necessary disciplinary action will be taken against any employee not following the policies and procedures laid down by Choice Equity Broking Pvt. Ltd.’s code of conduct. Similarly, action will be taken against those employees encouraging/observing such an activity and not reporting the same to the concerned authority. Any employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment as per Choice Equity Broking Pvt. Ltd. code of conduct.

## 5. ISMS Control Reference
<!-- section_id: DDR-5.0 -->
This policy is guided by the following clauses in the International security standard [[doc:ISO 27001:2013]]:
- A.11.2.7 Secure disposal or re-use of equipment
- A.8.3.2 Disposal of media
- A.16.1.7 Collection of Evidence
```