```yaml
---
document_id: "ACP"
title: "Asset Classification Policy"
filename: "Choice-ISMS-Asset Classification Policy.pdf"
version: "2.3"
status: "approved"
created_date: "2016-10-17"
effective_date: "2016-10-17"
last_reviewed: "2025-04-07"
next_review: null

owner:
  name: "Yogesh Jadhav"
  role: "Approver"

prepared_by:
  - name: "Abhishek Vinayak"
    role: "Associate Information Security"

approved_by:
  - name: "Ashutosh Bhardwaj"
    role: "CISO"
    date: "2025-04-07"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"
  - "third-party service providers"

regulatory_frameworks:
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"

references:
  - document_id: "XXX"
    title: "Incident Management Policy"
    relationship: "related"

scope:
  description: "Defines asset criticality and data sensitivity levels and establishes appropriate security controls and procedures."
  inclusions:
    - "All assets across physical & digital domains"
  exclusions:
    - "None specified"

entities:
  roles:
    - "CISO"
    - "Operations & IT Teams"
    - "Data Owners"
  controls:
    - "Firewall"
    - "Encryption"
    - "Access Control"
    - "Backup & Disaster Recovery"
    - "Monitoring & Logging"
  assets:
    - "Servers"
    - "Databases"
    - "Laptops"
    - "Desktops"
    - "Mobile Devices"
    - "Firewalls"
    - "Routers"
    - "Switches"
    - "CCTV Systems"
    - "UPS"
    - "Access Control Mechanisms"
  processes:
    - "Incident Management"
    - "Access Review"
    - "Data Collection and Storage"
    - "Data Sharing & Transfer"
    - "Data Retention & Deletion"
    - "Asset Onboarding"
    - "Asset Decommissioning"
  external_parties:
    - "SEBI"

tags:
  - "asset classification"
  - "data sensitivity"
  - "security controls"
  - "compliance"
---
# Asset Classification Policy

## 1. Objective
<!-- section_id: ACP-1.0 -->
The primary objective of this policy is to establish a structured framework for classifying IT assets, in accordance with their criticality and sensitivity. This will ensure appropriate protection measures are in place, facilitate regulatory compliance with regulatory guidelines, and safeguard the confidentiality, integrity, and availability of Choice Equity Broking Pvt. Ltd. 's (CEBPL) data and systems.

## 2. Scope
<!-- section_id: ACP-2.0 -->
This policy defines asset criticality and data sensitivity levels and establishes appropriate security controls and procedures. This policy applies to all CEBPL employees, contractors, and third-party service providers who handle or manage organizational assets. It covers all assets across physical & digital domains, including:

- **Data Assets**: Customer databases, KYC documents, trade transactions, financial records, internal communications (email, messaging)
- **End-User Devices**: Laptops, desktops, and mobile devices used by staff and dealers
- **Compute Infrastructure**: On-premise servers (e.g., MSSQL, MySQL, Redis, Elastic), virtual machines, cloud compute (e.g., AWS EC2)
- **Network Infrastructure**: Firewalls, routers, switches
- **Software Assets**: Core business and trading systems (RMS, OMS, back office), SaaS tools (Zoho Analytics, JIRA, Freshdesk, Slack), monitoring platforms (Grafana, Zabbix)
- **Physical Infrastructure**: CCTV systems, UPS, access control mechanisms

This policy defines the classification levels and protection controls applicable to each asset type. A detailed and up-to-date inventory, including asset criticality and sensitivity labels, to be maintained in the internal Critical Asset Register.

## 3. Key Definitions
<!-- section_id: ACP-3.0 -->
**Asset**
: Any system, software, hardware, or data that holds value to the organization or is required to perform business operations.

**Data Classification**
: The process of categorizing data based on its level of sensitivity, regulatory requirements, and impact on business if exposed or compromised.

**Critical Asset**
: Any asset whose unavailability, compromise, or unauthorized access would directly impact the continuity, integrity, or security of CEBPL’s trading operations, client obligations, or regulatory compliance.

## 4. Asset and Data Classification Framework
<!-- section_id: ACP-4.0 -->
The framework classifies all assets at CEBPL along two independent types of classification levels:

- **Asset Criticality Level** - Based on impact to trading, operations, or compliance if the asset is unavailable or compromised.
- **Data Sensitivity Level** - Based on risk from unauthorized access, disclosure, or misuse of the data content.

### 4.1 Asset Criticality Levels
<!-- section_id: ACP-4.1 -->
Assets are classified into two levels based on their impact on CEBPL's trading operations, regulatory obligations, and business continuity: Critical and Non-Critical.

#### 4.1.1 Critical Assets
<!-- section_id: ACP-4.1.1 -->
Assets essential for maintaining trading operations, regulatory obligations, and core business continuity. Disruption or compromise of these assets can lead to significant financial, operational, or reputational damage.

| Asset Type             | Asset Name / Examples                              | Scope & Usage                                      |
|------------------------|----------------------------------------------------|---------------------------------------------------|
| Compute Infrastructure | AWS EC2, On-prem SQL, MySQL, Redis, Elastic        | Servers hosting trading related web servers, application servers, databases and storage / file servers |
| Network Infrastructure | Firewalls & Network Equipments such as switches at Head Office, Primary Data Center & Disaster Recovery Site | Maintains secure communication with exchanges and trading systems |
| Trading Applications   | RMS, OMS                                           | Core applications for real-time order routing and execution |

#### 4.1.2 Non-Critical Assets
<!-- section_id: ACP-4.1.2 -->
Assets that support internal operations, reporting, or analysis. Their unavailability has limited or no immediate impact on critical business functions.

| Asset Type              | Asset Name / Examples                 | Scope & Usage                                      |
|-------------------------|---------------------------------------|---------------------------------------------------|
| Business Support Apps   | Zoho Analytics, Freshdesk             | BI, analytics, and customer service - supports decision making |
| Monitoring Tools        | Grafana, Zabbix, Superset             | Used for monitoring system performance and visualizations |
| General IT Devices      | Laptops, Desktops, Printers           | Used for documentation, internal communication    |
| Physical Infrastructure | CCTV, Biometric & Door Access Systems | Shadow IT used for physical surveillance and attendance tracking |

### 4.2 Data Sensitivity Levels
<!-- section_id: ACP-4.2 -->
Data is classified based on the potential impact of unauthorized access, disclosure, or misuse. Classification helps determine the appropriate level of protection and controls required.

#### 4.2.1 Confidential
<!-- section_id: ACP-4.2.1 -->
Highly sensitive information that, if compromised, could result in significant legal, regulatory, financial, or reputational damage.

| Data Type                                | Examples                                           | Scope & Usage                                      |
|------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| Personally Identifiable Information (PII) | KYC documents, PAN, Aadhaar, customer account data | Used for login, onboarding, trading session, regulatory compliance, and client servicing |
| Financial & Transactional Data           | Customer trades, ledgers, margin statements        | Used in trading, reporting, and compliance submissions |

#### 4.2.2 Internal
<!-- section_id: ACP-4.2.2 -->
Data intended for internal use only, where unauthorized access could result in internal disruptions but no regulatory impact.

| Data Type   | Examples                                          | Scope & Usage                  |
|-------------|---------------------------------------------------|--------------------------------|
| System Logs | Non-sensitive operational logs                    | Used for operational management |
| MIS         | Non-sensitive, internal only business MIS Reports | Used for business reporting    |

#### 4.2.3 Public
<!-- section_id: ACP-4.2.3 -->
Data that can be freely shared without significant risk to the organization or clients.

| Data Type      | Examples                                           | Scope & Usage                              |
|----------------|----------------------------------------------------|-------------------------------------------|
| Public Notices | Ads, Circulars                                     | Used for marketing campaigns.             |
| Market data    | Stock price historical data, Stock price live data | Used for providing information to clients. |

## 5. Protection Mechanisms
<!-- section_id: ACP-5.0 -->
Each asset and data classification level requires specific security controls and procedures to ensure its protection.

### 5.1 Critical Assets
<!-- section_id: ACP-5.1 -->
Protection Mechanisms:

- **Physical Security**: Restricted access to physical infrastructure (e.g., servers, data centers) using biometric or keycard systems.
- **Network Security**: Implement [[control:firewalls]] at both primary and DR sites to block unauthorized network access.
- **Encryption**: Use [[control:encryption]] at rest and in transit for all critical databases (SQL, MySQL, Redis, Elastic), ensuring that sensitive data is encrypted with organization-managed keys.
- **Backup & Disaster Recovery**:
  - Daily encrypted backups of critical data (KYC, PII) to AWS S3 with a minimum retention period of 10 years.
  - Test DR plans annually, ensuring business continuity from the DR site.
- **Access Control**:
  - Active Directory with Role-Based Access Control (RBAC) to enforce least privilege.
  - **[MANDATORY]** Multi-Factor Authentication (MFA) for all critical systems, including AWS access, GitLab, and customer databases.
- **Monitoring & Logging**:
  - Continuous monitoring of servers using Grafana and Zabbix for real-time alerts on anomalies.
  - Retain logs for firewalls, databases, and applications for a minimum of 6 months in active mode and 2 years in archival as per [[external:SEBI]] guidelines.

### 5.2 Non-Critical Assets
<!-- section_id: ACP-5.2 -->
Protection Mechanisms:

- **Basic Security Controls**: Access control using Active Directory, regular software updates.
- **Regular Backups**: Weekly backups of non-critical data to AWS S3.
- **Basic Monitoring**: Systems monitored for operational efficiency without extensive security controls.

## 6. Data Handling Procedures
<!-- section_id: ACP-6.0 -->

### 6.1 Data Collection and Storage
<!-- section_id: ACP-6.1 -->
- **Confidential Data**: PII and trade secrets should only be collected where necessary and stored in encrypted databases. Access to this data must be logged and monitored continuously.
- **Anonymization & Masking**: For non-production environments, any use of sensitive data must be anonymized or masked to prevent unauthorized access to real customer information.

### 6.2 Data Sharing & Transfer
<!-- section_id: ACP-6.2 -->
- **Internal Sharing**: Sensitive data should only be shared internally on a need-to-know basis, utilizing secure channels such as encrypted email.
- **External Sharing**: When sharing with third parties (e.g., auditors), ensure that data is transferred securely using encryption mechanisms.

### 6.3 Data Retention & Deletion
<!-- section_id: ACP-6.3 -->
- **Data Retention**: Critical customer data must be retained for 10 years to comply with [[external:SEBI]] requirements.
- **Data Deletion**: Once the retention period is complete, data must be irreversibly deleted or destroyed following secure data wiping practices.

## 7. Asset Lifecycle Management
<!-- section_id: ACP-7.0 -->

### 7.1 Asset Onboarding
<!-- section_id: ACP-7.1 -->
- **Risk Assessment**: Prior to deployment, every new asset must undergo a comprehensive risk assessment to determine its criticality and required protection measures.

### 7.2 Asset Decommissioning
<!-- section_id: ACP-7.2 -->
- **Secure Deletion**: Before decommissioning any hardware or cloud instances, ensure that all sensitive data is securely wiped and cannot be recovered.
- **Compliance Verification**: Conduct an audit to confirm that no critical data remains on decommissioned systems.

## 8. Compliance with Regulations
<!-- section_id: ACP-8.0 -->
- **Periodic Reports**: The [[role:CISO]] must submit detailed reports to the cyber security committee covering:
  - Compliance with cybersecurity frameworks.
  - Incident reports related to critical data breaches or compromises.
  - Updates on audits and assessments of critical and sensitive assets.
- **Regulatory Audits**: Regular audits must be conducted internally and by third-party auditors to ensure ongoing compliance with [[external:SEBI]]’s data security requirements.

## 9. Roles & Responsibilities
<!-- section_id: ACP-9.0 -->

### 9.1 Chief Information Security Officer (CISO)
<!-- section_id: ACP-9.1 -->
- Ensure regular reviews of asset criticality and data sensitivity levels.
- Coordinate regulatory reporting and compliance efforts.

### 9.2 Operations & IT Teams
<!-- section_id: ACP-9.2 -->
- Implement technical controls for asset protection, such as [[control:firewalls]], [[control:encryption]], and backups.
- Conduct periodic reviews of access control mechanisms and backup processes.

### 9.3 Data Owners
<!-- section_id: ACP-9.3 -->
- Ensure accurate classification of data based on data classification.
- Manage access rights to ensure the principle of least privilege.

## 10. Review and Maintenance
<!-- section_id: ACP-10.0 -->
This policy must be reviewed and updated annually or upon significant changes to regulatory requirements, business operations, or the IT environment.

## Annexure
<!-- section_id: ACP-Annexure -->
A. Classification Matrix
Link: Annexure-Asset Classification Matrix
```