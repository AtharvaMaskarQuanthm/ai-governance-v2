---
# ============================================================
# EXAMPLE: Converted Policy Document
# This shows what a properly extracted policy should look like
# ============================================================

# === DOCUMENT IDENTIFICATION ===
document_id: "CSP"
title: "Cyber Security Policy"
filename: "Choice-ISMS-CyberSecurity Policy.pdf"

# === VERSION CONTROL ===
version: "2.3"
status: "approved"
created_date: "2016-10-17"
effective_date: "2025-01-08"
last_reviewed: "2025-04-07"
next_review: "2026-04-07"

# === OWNERSHIP ===
owner:
  name: "Ashutosh Bhardwaj"
  role: "CISO"
  email: null

prepared_by:
  - name: "Abhishek Vinayak"
    role: "Associate, Information Security"

approved_by:
  - name: "Shripad Mayekar"
    role: "Manager, Information Security"
    date: "2025-04-07"
  - name: "Ashutosh Bhardwaj"
    role: "CISO"
    date: "2025-04-07"

# === CLASSIFICATION ===
classification: "Internal"
applies_to:
  - "employees"
  - "contractors"
  - "vendors"
  - "third-party staff"

# === REGULATORY & FRAMEWORK ALIGNMENT ===
regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
    clauses: []
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"
    reference: "SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113"
  - id: "NCIIPC"
    name: "NCIIPC Guidelines"
    reference: null

# === INTERNAL REFERENCES ===
references:
  - document_id: "ISP"
    title: "Information Security Policy"
    relationship: "parent"
  - document_id: "IMP"
    title: "Incident Management Policy"
    relationship: "related"
  - document_id: "LAC"
    title: "Logical Access Control Policy"
    relationship: "related"
  - document_id: "ICP"
    title: "Information Classification Policy"
    relationship: "related"
  - document_id: "CCP"
    title: "Cryptography Control Policy"
    relationship: "related"

# === DOCUMENT SCOPE ===
scope:
  description: "Defines cyber security controls, operations, and governance for protecting critical cyber assets"
  inclusions:
    - "All IT infrastructure"
    - "All business applications"
    - "Network security"
    - "Endpoint security"
    - "Vendor management"
  exclusions: []

# === EXTRACTED ENTITIES ===
entities:
  roles:
    - "CISO"
    - "Information Security Team"
    - "IT Department"
    - "Technology Committee"
    - "Information Security Steering Committee"
    - "Asset Owners"
    - "Business Function Heads"
  controls:
    - "Multi-factor Authentication"
    - "Intrusion Detection System"
    - "Intrusion Prevention System"
    - "Firewall"
    - "Next-Gen Firewall"
    - "Encryption"
    - "Network Access Control"
    - "WPA-2"
    - "Endpoint Protection"
    - "SIEM"
    - "Privileged Access Management"
    - "Content Filtering"
    - "Proxy"
  assets:
    - "Critical Cyber Assets"
    - "Network Devices"
    - "Servers"
    - "Databases"
    - "Workstations"
    - "Laptops"
    - "Mobile Devices"
    - "Information Assets"
  processes:
    - "Incident Management"
    - "Vulnerability Assessment"
    - "Penetration Testing"
    - "Access Review"
    - "Risk Assessment"
    - "Patch Management"
    - "Change Management"
    - "Configuration Management"
    - "Social Engineering Testing"
    - "Security Awareness Training"
  external_parties:
    - "CERT-IN"
    - "SEBI"
    - "NSE"
    - "BSE"
    - "NCIIPC"
    - "NTRO"

# === TAGS ===
tags:
  - "cyber security"
  - "access control"
  - "incident response"
  - "vulnerability management"
  - "network security"
  - "security operations"
  - "VAPT"
  - "SOC"
  - "governance"
---

# Cyber Security Policy

## 1.0 Background
<!-- section_id: CSP-1.0 -->
<!-- compliance_relevance: low -->

In light of the growing cyber security threats, [[role:Choice Equity Broking Pvt. Ltd.]] has outlined the policy to protect its information, infrastructure and people resources from the risks of cyber-attacks and breaches.

A cyber-attack is an intentional exploitation of [[asset:critical cyber assets]] (people, systems, networks, processes and services) using threat agents such as exploits, denial of service, backdoors and social engineering, indirectly or directly with the intent to adversely affect or compromise the confidentiality, integrity or availability of such assets.

**Examples of cyber-attacks include:**

- Network intrusions involving sniffing, spoofing, session hijacking, man-in-the-middle attacks, foot-printing, password hacking and denial of service
- Systemic compromise using malware such as viruses, trojans, worms, advanced persistent threats to obtain unauthorized access to assets
- Application security breaches involving SQL injections, privilege escalation and gaining illegitimate access to sensitive data
- Social engineering techniques involving elicitation of people assets using telephonic, electronic (email, SMS and chat messengers) or physical communication
- Unauthorized access to sensitive data

---

## 2.0 Cyber Security Program
<!-- section_id: CSP-2.0 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["cyber security framework", "security program", "governance"] -->

The Cyber Security program shall operate in a continuously improving environment with the following stages:

| # | Stage | Description |
|---|-------|-------------|
| 1 | **Governance** | Establishing governance structures, policies, and procedures for cybersecurity. Defining roles, enforcing compliance and conducting cybersecurity audits and board reviews. |
| 2 | **Identify** | Identification of critical assets and management of cyber security risks |
| 3 | **Protect** | Continually safeguarding identified assets by deploying controls such as security architecture mechanisms, event correlation systems, [[control:intrusion prevention and detection systems]], and enforcement of secure configurations |
| 4 | **Detect** | Detecting incidents related to attacks or anomalies through continuous monitoring of critical infrastructure |
| 5 | **Respond** | Take steps to assess the incident impact and take appropriate response measures including escalation to relevant authorities |
| 6 | **Recover** | Recover from incident adequately following the organization's incident management, business continuity and disaster recovery policies |
| 7 | **Evolve** | Continuously assessing controls through security testing, ensuring ongoing compliance, and implementing improvements based on incident learnings |

---

## 3.0 Governance
<!-- section_id: CSP-3.0 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["security governance", "CISO responsibilities", "security committee"] -->

- **[MANDATORY]** The ownership and responsibility for the maintenance of the Cyber Security Policy and the Cyber Security program lies with the [[role:Chief Information Security Officer (CISO)]].

- **[MANDATORY]** The responsibility for cyber security operations across the organization rests with the [[role:Information Security Team]].

- **[MANDATORY]** A [[role:Technology Committee]] has been appointed for contribution and guidance regarding this policy.

> [!CROSS-REF]
> Refer to Annexure A for details on Cyber Security Committee composition.

- **[MANDATORY]** An [[role:Information Security Steering Committee (ISSC)]] shall be formulated comprising of key technology and business stakeholders, to review the implementation of Cyber Security Policy on an annual basis.

- **[MANDATORY]** Choice Equity Broking Pvt. Ltd. shall set up partnership and/or membership with [[external:CERT-IN]] (Computer Emergency Response Team - India).

---

## 4.0 Policy Review and Approval
<!-- section_id: CSP-4.0 -->
<!-- compliance_relevance: medium -->
<!-- likely_maps_to: ["policy review", "document control", "approval process"] -->

- **[MANDATORY]** This policy document shall be reviewed at least annually, or in the event of any significant change(s) in the existing cyber security environment.

- **[MANDATORY]** The [[role:CISO]] will be responsible to approve changes to the Cyber Security policy document.

- **[MANDATORY]** The Cyber Security policy shall be shared with [[role:ISSC]] for review and approval.

---

## 5.0 Policy Exceptions
<!-- section_id: CSP-5.0 -->
<!-- compliance_relevance: medium -->
<!-- likely_maps_to: ["exception handling", "risk acceptance", "deviation management"] -->

- **[MANDATORY]** All exceptions or deviations from the policies outlined in the Cyber Security Policy document are mandated to be formally approved by the [[role:CISO]].

- **[MANDATORY]** Approval for such exceptions will be provided only after an appropriate assessment of the risks arising out of providing the exception.

- **[MANDATORY]** Exceptions will be granted for a maximum of **one calendar year** from the date of approval.

- **[MANDATORY]** Business must formally accept/reject risks identified as part of [[role:Information Security Team]] assessment.

---

## 6.0 Cyber Security Operations
<!-- section_id: CSP-6.0 -->
<!-- compliance_relevance: high -->

### 6.1 Critical Cyber Asset Identification
<!-- section_id: CSP-6.1 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["asset identification", "asset classification", "asset register", "critical assets"] -->

- **[MANDATORY]** Respective teams shall identify and categorize [[asset:critical information assets]], system, service, software, application and people assets in the Information Asset Register.

- **[MANDATORY]** Assets should be identified & classified on the basis of the organization's risk assessment methodology.

- The [[role:Information Security Team]] shall provide guidance and support as required.

---

### 6.2 Cyber Risk Identification and Assessment
<!-- section_id: CSP-6.2 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["risk assessment", "threat identification", "vulnerability assessment", "risk management"] -->

- **[MANDATORY]** [[role:Information Security Team]] shall identify cyber security risks, i.e., threats to and vulnerabilities in its [[asset:critical cyber assets]] and business environment.

- **[MANDATORY]** The Information Security Team must assess the likelihood and impact of such threats on various business processes.

- **[MANDATORY]** Information Security Team shall maintain a library of controls that can be implemented to mitigate or transfer specific cyber security risks.

**Special attention shall be given to potential reputation risks such as:**

- Leakage of company information to the public domain
- Inappropriate actions by disgruntled employees on the public domain
- Misrepresentation of Choice Equity Broking Pvt. Ltd. identity

---

### 6.3 Security Controls Management and Monitoring
<!-- section_id: CSP-6.3 -->
<!-- compliance_relevance: high -->

#### Physical Access Security
<!-- section_id: CSP-6.3.1 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["physical access", "data center security", "facility security", "physical controls"] -->

- **[MANDATORY]** Physical access to [[asset:critical cyber assets]] must be limited only to duly authorized end-users, especially for third-party vendor and service-provider personnel.

- **[MANDATORY]** Adequate monitoring controls shall be implemented to ensure protection of critical cyber assets from natural and manmade disasters.

- **[MANDATORY]** Access shall be granted based on **need to know** and **least privilege** basis.

- **[MANDATORY]** Employees must immediately report lost or stolen devices to the local IT teams.

---

#### Logical Access Security
<!-- section_id: CSP-6.3.2 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["logical access", "authentication", "password policy", "access control", "privileged access", "MFA"] -->

- **[MANDATORY]** Electronic access to cyber assets should be limited to end-users using valid approved requests.

- **[MANDATORY]** Access-levels granted to end-users (employees, vendor & customers) should be commensurate with the respective users' business roles and should be granted strictly on a **'need-to-use'** and **'least-privilege'** principle.

- **[MANDATORY]** Administrative access on systems viz [[asset:desktops]], [[asset:laptops]], [[asset:servers]] and software shall be controlled and monitored.

- **[MANDATORY]** Access (authentication and sign-out) and activity logs should be stored for audit and review purposes for **180 days at minimum**, and should be archived at an offsite location.

- **[MANDATORY]** [[role:Information Security Team]] shall perform annual review on password parameters for all types of accounts in accordance with the [[doc:Logical Access Control Policy]].

- **[MANDATORY]** Passwords shall not be stored in plaintext form; they shall be stored only using strong hashing/encryption algorithms.

- **[MANDATORY]** Information Security Team shall monitor [[control:privileged access management]] roles on all cyber assets and enforce implementation of additional controls including:
  - Restricting number of privileged accounts
  - Periodic and independent review of sample privileged account activity
  - Restricting remote access to approved privileged accounts
  - Denying access to update/delete activity logs for privileged accounts
  - Monitoring access deprovisioning process for privileged accounts

---

#### Internet Usage
<!-- section_id: CSP-6.3.3 -->
<!-- compliance_relevance: medium -->
<!-- likely_maps_to: ["internet usage", "web filtering", "acceptable use", "social media"] -->

- **[MANDATORY]** Guidelines for acceptable use of internet services shall be enforced across the network, spanning all office locations including branches.

- **[MANDATORY]** Employees shall have clear knowledge of what types of websites are deemed unacceptable.

- **[MANDATORY]** Defined rules on [[control:Proxies/Content filtering]] solutions should be monitored by the [[role:Information Security Team]].

- **[MANDATORY]** Guidelines for employees' acceptable behavior on social networking forums shall be enforced.

---

#### Network and Host Security
<!-- section_id: CSP-6.3.4 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["network security", "firewall", "IDS", "IPS", "endpoint protection", "wireless security"] -->

- **[MANDATORY]** Configuration of all [[asset:network devices]], appliances & critical infrastructure components shall be reviewed on an annual basis at minimum.

- **[MANDATORY]** [[role:Information Security Team]] shall monitor compliance of critical infrastructure components against defined baseline standards.

- **[MANDATORY]** Adequate controls shall be implemented including:
  - [[control:Next-gen firewalls]]
  - [[control:Network Access Control]]
  - [[control:WPA-2 encryption]] for wireless networks
  - [[control:Intrusion Prevention and Detection systems]]

---

### 6.4 Cyber Security Metrics and Measurement
<!-- section_id: CSP-6.4 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["security metrics", "KPI", "monitoring", "measurement"] -->

- **[MANDATORY]** [[role:Information Security Team]] shall monitor various people, process and technology controls across the environment.

- **[MANDATORY]** Activity logs for critical application, system and network device assets should be aggregated and correlated to generate alerts and actionable event information.

- **[MANDATORY]** Capacity utilization of critical system and network assets should be monitored by respective asset owners.

---

### 6.5 Detection and Response
<!-- section_id: CSP-6.5 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["SOC", "incident detection", "incident response", "SIEM", "security monitoring"] -->

- **[MANDATORY]** [[control:Security Operations Center]] shall be established to enable log aggregation and correlation for providing analysis and overarching situational awareness of cyber threats.

- **[MANDATORY]** Security Incident Management Portal must be in place for all employees/outsourced staff to log information security incidents.

- **[MANDATORY]** Once detected and preliminary checks are performed, the [[role:Information Security Team]] should be notified immediately.

- **[MANDATORY]** Response plans should aim at timely restoration of systems affected by incidents, in line with defined RTOs and RPOs.

- **[MANDATORY]** Cyber Incidents will be communicated to respective regulators ([[external:SEBI]], [[external:CERT-IN]]) as per regulatory requirements.

> [!CROSS-REF]
> For detailed procedures, refer to [[doc:Incident Management Policy]].

---

### 6.6 Audits
<!-- section_id: CSP-6.6 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["VAPT", "vulnerability assessment", "penetration testing", "security audit", "audit frequency"] -->

- **[MANDATORY]** [[role:Information Security Team]] shall ensure Cyber Security & VAPT Audits to confirm the cyber security controls and test their effectiveness as per regulatory guidelines.

**Audit Matrix:**

| Asset Type | Audit Type | Frequency |
|------------|------------|-----------|
| Web Applications | Internal VAPT | After every major release |
| Web Applications | External CERT-IN Empanelled VAPT | Bi-annually |
| Mobile Applications | Internal VAPT | After every major release |
| Mobile Applications | External CERT-IN Empanelled VAPT | Bi-annually |
| Firewalls | Internal VAPT | Quarterly (Rule Reviews) |
| Firewalls | External CERT-IN Empanelled VAPT | Bi-annually |
| Infrastructure (Servers) | External CERT-IN Empanelled VAPT | Bi-annually |
| API Security | Internal VAPT | After every major release |
| API Security | External CERT-IN Empanelled VAPT | Bi-annually |

---

### 6.7 Cyber Security Drills
<!-- section_id: CSP-6.7 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["security drills", "tabletop exercises", "incident simulation", "readiness testing"] -->

- **[MANDATORY]** The [[role:Information Security Team]] shall conduct periodic drills or exercises to test the readiness of the people, process and technology aspects to detect, respond and recover from cyber attacks.

- The scope and frequency of such drills shall be determined based on the scale of operations, threat landscape, and resource availability.

---

### 6.8 Awareness and Training
<!-- section_id: CSP-6.8 -->
<!-- compliance_relevance: high -->
<!-- likely_maps_to: ["security awareness", "training", "employee training", "phishing awareness"] -->

- **[MANDATORY]** Periodic training and initiatives shall be undertaken for augmenting awareness among employees, third-party staff and vendors about:
  - The organization's Cyber Security policies
  - Peoples' obligations towards the Cyber Security program
  - Appropriate use of [[asset:Critical Cyber Assets]]
  - Physical and logical controls
  - Guidelines for identification of Cyber Security incidents

- **[MANDATORY]** The Cyber Security policy should be included as part of the employment agreement.

- **[MANDATORY]** Specific awareness mailers should be sent periodically to all employees regarding Cyber Security basics.

- **[MANDATORY]** Periodic mailers to customers shall be communicated by business management to create awareness regarding cyber security risks, reporting of phishing mails & social engineering attacks.

---

## 7.0 Continual Improvement
<!-- section_id: CSP-7.0 -->
<!-- compliance_relevance: medium -->
<!-- likely_maps_to: ["continuous improvement", "security program review", "lessons learned"] -->

- **[MANDATORY]** [[role:Information Security Team]] shall periodically monitor the technological environment by evaluating Cyber Security metrics covering:
  - Incident Management
  - Vulnerability Management
  - Patch Management
  - Configuration Management
  - Change Management
  - Application Security
  - Identity & Access Management

- **[MANDATORY]** The performance results shall be reported annually to the [[role:CISO]] and Senior Management.

- **[MANDATORY]** Lessons learnt from Cyber Security incidents shall be documented and inputs should be fed into response plans.

---

## 8.0 Reference Documents
<!-- section_id: CSP-8.0 -->

- [[framework:ISO 27001:2022]]
- [[framework:SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113]]

---

## 9.0 Glossary
<!-- section_id: CSP-9.0 -->

**Cyberspace**
: The interdependent global network of information technology infrastructure that comprises of the Internet, telecommunications networks, computer systems, tools, end-users and other entities.

**Cyber Security**
: The capability and processes where information technology and communication systems, and the information contained therein are protected against damage, compromise, unauthorized use or modification, or exploitation in cyberspace.

**Cyber Security Event**
: An event or an anomaly detected by a security device, service, application, process or human on a technology infrastructure environment.

**Cyber Security Incident**
: Any malicious act or suspicious event that compromises or attempted to compromise the electronic, physical and logical security of a critical cyber asset or the operation of service(s) involving critical cyber assets.

**Cyber Security Breach**
: A Cyber Security Incident that has successfully accomplished its malicious task of exploiting technology and/or communication systems, by overcoming or bypassing the deployed Cyber Security controls in the environment.

---

## Annexure A: Cyber Security Committee
<!-- section_id: CSP-ANNEX-A -->

### Composition

| Sr. No | Name | Designation | Committee Role |
|--------|------|-------------|----------------|
| 1 | Mr. Ashutosh Bhardwaj | Group CISO | Chairperson |
| 2 | Mr. Ankit Jain | Senior Vice President | Member |
| 3 | Mr. Sunil Utekar | Head - IT Operations | Member |
| 4 | Mr. Shailendra Chaudhari | Security Analyst | Member |

### Quorum

The quorum for a meeting of the Cyber Security Committee shall be either **two members** or **one third of the members** of the committee, whichever is higher, including at least one member of the Board in attendance.

### Meeting Frequency

- **[MANDATORY]** The Committee shall meet at least **twice in a year** with a gap of not more than **180 days** between any two consecutive meetings.
