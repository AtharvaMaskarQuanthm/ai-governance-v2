```yaml
---
document_id: "ISMS"
title: "Choice Equity Broking Pvt Ltd Consolidated Procedures"
filename: "Choice_ISMS_Consolidated_PROCEDURES.pdf"
version: "2.2"
status: "approved"
created_date: "2016-10-17"
effective_date: "2016-10-17"
last_reviewed: "2023-04-09"
next_review: "2024-01-31"

owner:
  name: "Abhishek Vinayak"
  role: "Approver"

prepared_by:
  - name: "Mahesh Tamhankar"
    role: "Preparer"

approved_by:
  - name: "Yogesh Jadhav"
    role: "Approver"
    date: "2025-01-08"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"
  - "third-party personnel"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"

references:
  - document_id: "ISMS_LAP"
    title: "ISMS Logical Access Policy"
    relationship: "related"
  - document_id: "ISMS_RWP"
    title: "ISMS Remote Working Policy"
    relationship: "related"
  - document_id: "ISMS_SMP"
    title: "ISMS Supplier Management Policy"
    relationship: "related"

scope:
  description: "Procedures for managing information security within Choice Equity Broking Pvt Ltd."
  inclusions:
    - "Access control"
    - "Antivirus management"
    - "Asset management"
    - "Internal audit"
    - "Corrective actions"
    - "Human resources security"
    - "Patch management"
    - "Document control"
    - "Backup and restoration"
    - "Communication"
    - "Performance monitoring"
    - "Skill development"
  exclusions:
    - "Non-ISMS related procedures"

entities:
  roles:
    - "CISO"
    - "IT Department"
    - "HR"
    - "Legal and Compliance Officer"
    - "Employees"
    - "Third-Party Vendors"
  controls:
    - "Antivirus"
    - "Firewall"
    - "Encryption"
    - "MFA"
  assets:
    - "Servers"
    - "Databases"
    - "Laptops"
    - "Desktops"
  processes:
    - "Access Management"
    - "Incident Management"
    - "Patch Management"
    - "Audit"
  external_parties:
    - "SEBI"
    - "CERT-IN"

tags:
  - "information security"
  - "compliance"
  - "risk management"
---
# Choice Equity Broking Pvt Ltd Consolidated Procedures

## I. Access Control Procedure
<!-- section_id: ISMS-I -->

### Purpose
The Access Control Procedure details the guidelines to be followed for the granting, modifying, reconciling, and revoking physical and logical access to the information, information processing facilities, and premises of [[external:CHOICE EQUITY BROKING PVT. LTD]].

### Scope
Access control procedure covers all aspects of the following:
- User Registration and Deregistration
- Review of User access rights
- Password Controls

### Business Requirement for Access Control
**[MANDATORY]** Access shall be provided to information and various information processing facilities for the employees of [[external:CHOICE EQUITY BROKING PVT. LTD]] and third-party personnel only on a need-to-know basis and upon completion of the access formalities.

### Access Management for Employees
#### Access Granting Procedures
| Sr. No. | Activities | Mandatory (Y/N) | Responsibility |
|---------|------------|-----------------|----------------|
| 1 | HR team on-boards the new joiners on the first day | Y | [[role:HR]] |
| 2 | During the on-boarding process, the new joiners are requested to fill the new joiner form | Y | [[role:HR]] and New Joiner |
| 3 | New joiner form is to be approved by the appropriate authority | Y | [[role:HR]] |
| 4 | The new joiner form is dispatched to the IT Team for the creation of physical access rights | Y | [[role:HR]] |
| 5 | The new joiner form is dispatched to the IT Team for the creation of domain ID and email ID | Y | [[role:HR]] |
| 6 | The IT Team also assigns a desktop or a laptop to the new joiner as indicated in the form | N | [[role:IT Staff Member]] |
| 7 | Access to applications/projects shall be provided to the new joiner based on approval of the respective access request mails by reporting manager | N | [[role:IT Staff Member]] |

### Access Modification
**[MANDATORY]** Access Modification request to be made for an employee and appropriate approvals should be taken.

### Revocation of Access Rights
#### Resigned/Terminated/Retired and Transferred Employees
| Sr. No. | Activities | Mandatory (Y/N) | Responsibility |
|---------|------------|-----------------|----------------|
| 1 | The last working day of the employee is communicated to the employee, and the reporting manager of the employee | Y | [[role:HR]] |
| 2 | The IT Team is informed regarding the last working day of the employee at least one day in advance | Y | [[role:HR]] |
| 3 | Employee fills the termination checklist and that the termination checklist is signed off by the relevant personnel before the employee leaves the premises of [[external:CHOICE EQUITY BROKING PVT. LTD]] | Y | [[role:HR]] and employee |
| 4 | Physical and logical access rights of the employee are revoked within one business working day from the last working day of the employee | Y | [[role:IT]] |
| 5 | In case the email ID of the employee is to be kept active for business reasons, the password of the email ID is changed with immediate effect | N | [[role:IT Staff Member]] |

#### Absconding Employees
| Sr. No. | Activities | Mandatory (Y/N) | Responsibility |
|---------|------------|-----------------|----------------|
| 1 | The reporting manager informs the HR team regarding the uninformed absence of any employee for more than 5 business days | Y | Line Manager |

## II. Antivirus Management
<!-- section_id: ISMS-II -->

### Purpose
The objective of this antivirus procedure is to provide a secure computing environment where the entire business data is processed.

### Scope
The procedure is applicable to all employees of [[external:CHOICE EQUITY BROKING PVT. LTD]] and all third-party personnel posted within the premises.

### Antivirus Procedure
**[MANDATORY]** Installation for all Antivirus servers shall be done in the following manner:
- Groups should be created separately for desktops, laptops, and servers.
- Should create separate policies for each group.
- Should create separate client packages for each group with specified policies.
- Should be up-to-date with all product updates and virus definitions.
- Live update to be configured to fetch updates from the internet every hour.
- All the clients connected to the management console should be monitored on a regular basis.

### Firewall Policy
**[MANDATORY]** Firewall policy should be enabled for all machines.

## III. Asset Management
<!-- section_id: ISMS-III -->

### Purpose
The Asset Management Procedure contains the procedures for the identification, inventory, inventory verification, maintenance, and acceptable use of the information assets of [[external:CHOICE EQUITY BROKING PVT. LTD]].

### Scope
This procedure will apply to all [[external:CHOICE EQUITY BROKING PVT. LTD]] Information assets and to all personnel responsible for these assets.

### Asset Management Procedure
#### Asset Categories
The assets of [[external:CHOICE EQUITY BROKING PVT. LTD]] have been categorized into the following asset categories:
- Physical Assets / IT Infrastructure
- Information – Softcopy
- Information - Hardcopy
- Software
- Services
- Personnel

#### Key Activities
| Sr. No. | Activities | Mandatory (Y/N) | Responsibility |
|---------|------------|-----------------|----------------|
| 8 | Inventory of Assets: The owner of the Physical / IT Infrastructure assets is the IT Team along with the facilities team | Y | Asset Owners |
| 9 | The asset inventory will be updated by an identified IT team member whenever a new asset is procured by [[external:CHOICE EQUITY BROKING PVT. LTD]], or an existing asset is decommissioned or disposed | Y | IT Staff Member; IT Manager |
| 10 | A physical verification of the asset inventory shall be conducted on an annual basis by the IT team to ensure accuracy of the asset inventory | Y | IT Staff Member; IT Manager |

## IV. ISMS Internal Audit Procedure
<!-- section_id: ISMS-IV -->

### Scope of the Audit
All Data Center processes across all the locations within the scope of the ISMS must be audited periodically to ensure compliance with the Information Security policies, controls, and procedures defined and implemented.

### Audit Methodology
**[MANDATORY]** The auditors shall have a thorough understanding of the ISO/IEC 27001:2022 standards and its requirements before the audit.

### Audit Schedule
**[MANDATORY]** This must be at minimum once a year for effectively identifying and resolving the non-conformities and areas for improvement.

## V. Corrective Actions Procedure
<!-- section_id: ISMS-V -->

### Purpose
The process of reacting to an existing non-conformity, fixing it, and ensuring it does not reoccur is called corrective action.

### Procedure
Adequate mechanisms to investigate reported non-conformities and arrive at corrective actions to prevent occurrence/recurrence shall be implemented to ensure continued improvement of the ISMS.

## VI. Human Resources Security Procedure
<!-- section_id: ISMS-VI -->

### Introduction
The objective of this procedure is to ensure that [[external:CHOICE EQUITY BROKING PVT. LTD]] employees, contractors, and external party users understand their responsibilities, and are suitable for the roles they are considered for, and to reduce the risks of human error, theft, fraud, or misuse of facilities.

### Scope
This policy applies to all [[external:CHOICE EQUITY BROKING PVT. LTD]] employees and third-party personnel providing various services.

## VII. Patch Management Procedure
<!-- section_id: ISMS-VII -->

### Purpose
The purpose of this procedure is to ensure that software patches are applied on the information systems in accordance with the approved business and technical requirements.

### Patch Management
**[MANDATORY]** The security and the server team need to identify the new patches to be released under their respective domain.

## VIII. Procedure for Control of ISMS Documents and Records
<!-- section_id: ISMS-VIII -->

### Purpose
The purpose of this procedure is to establish effective control over the preparation, authorization, issue, distribution, maintenance, integrity, and subsequent change (if any) of documents required by the ISMS, in all process areas.

### Control of Documents
All new issues of ISMS documents as well as revised versions owing to changing practices are initiated, reviewed, approved, and issued through the following method.

## IX. Communication Procedure
<!-- section_id: ISMS-IX -->

### Purpose
The purpose of this document is to define the communication procedure for ensuring the security of information related to the Equity Broking business in compliance with the regulatory requirements and the requirements of the Information Security Management System (ISMS) framework.

### Communication Channels
**[MANDATORY]** All sensitive communications must be encrypted and password-protected if necessary.

## X. Performance Monitoring Procedure
<!-- section_id: ISMS-X -->

### Purpose
The purpose of this document is to define the performance monitoring procedure for ensuring the effectiveness of the Information Security Management System (ISMS).

### Performance Monitoring Framework
**[MANDATORY]** To effectively measure the performance of ISMS, the company will monitor the following key KPIs.

## XI. Skill Development Procedure
<!-- section_id: ISMS-XI -->

### Purpose
To establish a procedure for skill development related to the Information Security Management System (ISMS), ensuring employees have the necessary skills to safeguard sensitive data and comply with regulatory requirements.

### Training Programs
**[MANDATORY]** Information security awareness training (data protection, phishing, incident reporting) to be conducted annually.
```
