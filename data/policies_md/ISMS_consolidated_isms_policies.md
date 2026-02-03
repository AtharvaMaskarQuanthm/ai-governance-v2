```yaml
---
document_id: "ISMS"
title: "Consolidated ISMS Policies"
filename: "Choice_ISMS_Consolidated_Policies.pdf"
version: "2.4"
status: "approved"
created_date: "2016-10-17"
effective_date: "2025-02-20"
last_reviewed: "2025-02-20"
next_review: null

owner:
  name: "Ashutosh Bhardwaj"
  role: "CISO"

prepared_by:
  - name: "Mahesh Tamhankar"
    role: "Role Title Unknown"

approved_by:
  - name: "Yogesh Jadhav"
    role: "CTO"
    date: "2025-01-08"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"
  - "consultants"
  - "temporary staff"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"

references:
  - document_id: "XXX"
    title: "Non-Employee Access Standards"
    relationship: "related"

scope:
  description: "The document outlines the ISMS policies for Choice Equity Broking Pvt. Ltd."
  inclusions:
    - "All employees and temporary staff"
  exclusions:
    - "None specified"

entities:
  roles:
    - "CISO"
    - "CTO"
    - "ISMS Manager"
    - "Internal Auditor"
    - "Department Head"
    - "Authorized User"
  controls:
    - "Firewall"
    - "Proxy Server"
    - "PAM Tool"
    - "Multi-Factor Authentication"
  assets:
    - "Servers"
    - "Databases"
    - "Laptops"
    - "Desktops"
  processes:
    - "Incident Management"
    - "Access Review"
    - "Backup and Restoration"
  external_parties:
    - "SEBI"

tags:
  - "information security"
  - "access control"
  - "internet usage"
  - "data backup"
---
```

```markdown
## INFORMATION SECURITY ROLES AND RESPONSIBILITIES
<!-- section_id: ISMS-1.0 -->

### 1.0 Scope
<!-- section_id: ISMS-1.1 -->
The target audience of this document is all the employees of Choice Equity Broking Pvt. Ltd. and all the temporaries (vendors and users of Choice Equity Broking Pvt. Ltd.’s information assets, other than direct employees). The scope of this document is to make the target audience aware of their Information security roles and responsibilities.

### 2.0 Roles and Responsibilities
<!-- section_id: ISMS-1.2 -->
Information Security Management System Steering Committee

The Information Security Management System Steering Committee is responsible for the establishment, implementation, operation, monitoring, review, maintenance and improvement of Information Security Management System (ISMS) at Choice Equity Broking Pvt. Ltd. The responsibilities of the Information Security Management System Steering Committee include:

- Ensuring that Information security objectives and plans are established for ISMS.
- Communicating to the organization the importance of meeting information security objectives and conforming to the information security policy, its responsibilities under the organization’s regulations and the need for continual improvement.
- Providing sufficient resources to develop, implement, operate and maintain the ISMS.
- Identifying the acceptable levels of risk for the Information Assets.
- Periodically reviewing the status of Choice Equity Broking Pvt. Ltd. Information Security Management System.
- Reviewing and monitoring remedial work related to Information security incidents.
- Approving new or modified information security policies and procedures.
- Approving major initiatives in enhancing Information security.
- Ensuring that an internal audit is carried out Annually or as and when required for client’s requirements, and a third-party audit is carried out annually.
- Providing competent training and, if necessary, employing competent personnel to satisfy the security requirements of Choice Equity Broking Pvt. Ltd..
- If needed, reporting the security posture of Choice Equity Broking Pvt. Ltd.to the Management board and investors once in a year.
- The Information security Committee will compromise senior management C-Suite/SVP/director of different departments.

The Information Security Management System Steering Committee has to meet annually once to discuss and review the security program. This meeting shall be chaired by the Information Security Management System Steering Committee Chairman.

**Authority**: The Steering Committee holds the authority to set strategic direction, approve policies, and oversee the implementation and effectiveness of the ISMS.

### 2.1 Responsibilities of Departments
<!-- section_id: ISMS-1.3 -->

#### Director / Vice President
The Director’s / Vice President’s responsibilities, with respect to ISMS, are as follows:

- Ensure that appropriate levels of security are applied to all information assets (whether retained in-house or under the control of contractors) and Oversee, define, plan, budget, and implement the information security program.
- Ensure that Choice Equity Broking Pvt. Ltd.has established ISMS program
- Allocate sufficient resources necessary for the protection of Choice Equity Broking Pvt. Ltd.’s information assets
- Hold Choice Equity Broking Pvt. Ltd.’s managers accountable for the security of the information assets under their control
- Ensure that staff, facilities, and IT processing assets with appropriate national security clearances are available in the Office of Choice Equity Broking Pvt. Ltd.

**Authority**: Senior leadership is authorized for providing necessary resources, and fostering a culture of security across their respective departments.

#### Chief Information Security Office (CISO)
The CISO responsibilities, with respect to ISMS, are as follows:

- Ensure that all information assets owned or operated by or for Choice Equity Broking Pvt. Ltd.’s are accredited and that all information assets are assigned to an information system
- Ensure that Choice Equity Broking Pvt. Ltd. has established ISMS program & Coordinate implementation of the information security program.
- Approve and issue information security program policy, procedures, and guidance.
- Ensure that information assets are developed and operated in full compliance with Department and Choice Equity Broking Pvt. Ltd.’s policies, as well as ISO 27001’s information security- related directives.
- Ensure that positions with significant information security responsibilities are held by staff with sufficient training and education qualifications as well as by staff who have had appropriate background checks.

**Authority**: The CISO is authorized for the development, implementation, and management of the ISMS and has the authority to approve ISMS policies.

#### ISMS Manager (Information Security Manager)
The ISMS Manager will perform the following:

- Coordinate implementation of the IT security program
- Develop IT security program policy, procedures, standards, and guidance consistent with Departmental and ISO 27001’s requirements
- Assist with the development of IT system specific policy, procedures, and safeguards
- Implement and manage an IT security awareness and training program
- Assist with the planning and budgeting of IT security functions for Choice Equity Broking Pvt. Ltd..
- Establish and maintain an IT security certification and accreditation program. This includes ensuring that all assets have completed and maintained security plans, risk assessments, contingency plans, and security self-assessments
- Ensure that an objective, independent review and approval process exists for both security plans and procurement requests to validate the adequacy of proposed security safeguards;
- Communicate security requirements to Choice Equity Broking Pvt. Ltd.’s management and staff and serve as a resource on effective IT security practices
- Create and maintain an incident response capability

**Authority**: The ISMS Manager is authorized to enforce security policies, conduct risk assessments, propose and request resources including budget, tools, and personnel, to support ISMS-related activities, to initiate and enforce mandatory security awareness and training programs for employees.

#### Internal Auditor’s
- Provide an internal audit function capable of evaluating information security controls.
- Engage an outside consultant or auditors to perform the internal audit function.
- Or use a combination of both methods to ensure that the institution has received adequate information security audit coverage.
- Provide information, analyses, and counsel to assist in effectively and efficiently handling the ISMS project.
- Examines, evaluates and report on the adequacy and reliability of existing internal controls.
- Recommends, as necessary, actions to improve automated and manual systems of processing revenues and expenses, financial reporting, compliance with laws, regulations and internally developed policies and procedures and the safeguarding of assets.

**Authority**: Internal Auditors have the authority to assess and evaluate the effectiveness of the ISMS, identify weakness and areas for improvement in the management system.

#### Department Head’s Representatives/Working group (ISMS - SPOC)
Department representatives are directly responsible for the security of the assets under their purview. Department representatives have the following responsibilities:

- Ensure that appropriate levels of security are applied to all the assets and that sufficient resources are planned and assigned to maintain the required level of security;
- Ensure all assets are developed and operated in full compliance with Department and policies (e.g., annual user training requirements) as well as ISO 27001’s information security-related directives and mandates;
- Account for IT security in capital investment plans which must include all information security resources (e.g., labour, hardware, software, maintenance) for procurement, maintenance, and replacement of all assets;
- Ensure that department positions with significant security responsibilities are held by staff with sufficient training and education qualifications as well as by staff who have had appropriate background checks;
- Assign ownership of information security resources such that all department resources are assigned to a particular system and such that all assets have a designated system owner;
- Perform business assets access rights review of the team members

**Authority**: Department representatives have the authority to enforce departmental adherence to security policies, represent their department or team in all ISMS-related matters, communication between the ISMS Manager and their department, request necessary resources, participate in internal audits, assessments, and compliance checks.

#### Authorized User’s (Employee’s)
The success of IT security programs ultimately depends on the commitment of each user. Users are to:

- Operate IT assets in a secure and responsible manner
- Know and abide by all applicable policies and procedures. This includes reading and understanding system-specific rules of behaviour regarding inappropriate use or abuse of the company’s resources
- Participate in security awareness and training activities
- Know which assets or parts of assets for which they are directly responsible (e.g., printer, desktop, specific support service, etc.)
- Know the sensitivity of the data they handle and take appropriate measures to protect it as per the Information Labelling & Handling policy.
- Report incidents to the IT Team using the method devised.
- Follow acceptable usage policy.

**Authority**: Employees are authorized to access and use information and systems only as permitted by their role, to report security incidents, vulnerabilities, or potential threats to the appropriate teams without fear of retaliation.

## 1. LOGICAL ACCESS CONTROL POLICY
<!-- section_id: ISMS-2.0 -->

### 1.1. Purpose
<!-- section_id: ISMS-2.1 -->
Access to business information and data shall be controlled in order to restrict access to authorized users only. Logical access to information systems shall be controlled. Access control standards shall be clearly defined and implemented. These security measures are the minimum controls required to mitigate threats to information and information systems including unauthorized access, disclosure, duplication, modification, appropriation, destruction, loss, misuse, and denial of use.

### 1.2. Scope
<!-- section_id: ISMS-2.2 -->
This policy applies to all employees, contractors, consultants, and temporary staff etc. who have access to Choice Equity Broking Pvt. Ltd. (Choice) resources. These standards apply to all computer and data communication systems used by and/or administered by Choice Equity Broking Pvt. Ltd. (Choice). Similarly, these standards apply to all platforms (operating systems), all computer devices and all application systems (whether developed in-house or purchased from third parties, Internet Service Providers, or service bureaus).

### 1.3. Responsibility
<!-- section_id: ISMS-2.3 -->
The Head - Technology is responsible for the development, maintenance, implementation, operation and escalation of enforcement of this policy.

### 1.4. Policy
<!-- section_id: ISMS-2.4 -->

#### 1.4.1. Managing User Access
<!-- section_id: ISMS-2.4.1 -->

##### 1.4.1.1. User Access to Information, Data and Application
- Choice Equity Broking Pvt. Ltd. (Choice) users shall be granted access to information, data and applications strictly on a "need to know" basis.
- Any change in access privileges shall be carried out only after approved by appropriate personnel, by using a formal documented process.
- Segregation of duties shall exist between information access requestors, information access approvers and those implementing access changes. Each of these roles is limited to a pre-defined group and only those specifically given the responsibility shall be allowed to either request or approve access.
- All access changes shall be carried by the respective operations team specifically authorized to carry out such changes. Examples of access changes include: creation of new employee accounts, transfers, terminations, file folder permissions, etc.
- User access rights to applications and data shall be assigned based on the user role and permissions approved by the respective application administration team.
- Privilege escalation for any application and data shall be granted only by the application administrator (IT / Technical Team), on receipt of a documented approval from the LOB Head/ RA/ authorized approver of the person requesting access. All access requests shall include the purpose for request of access.
- In case the authentication and authorization for an application not being authenticated by the centralized active directory, then a separate application administrator shall manage the user management, password management, and privilege management for the application. The application owners shall be responsible for defining and maintaining access control lists for applications and data. They shall ensure that the level of access granted is appropriate to the business requirements.
- If for any reason, a user’s access rights need to be modified or revoked, the LOB Head shall send the request for the same in writing to the respective application’s owner / Operations team. The team shall then accordingly modify/revoke the access rights.
- HR shall promptly report all changes (i.e. LOB transfers, termination, job duty changes) in end-user duties or employment status to application operations team and also to the Technology team handling the user IDs of the affected persons. Respective Operations Team and / or Technology team shall then accordingly modify/revoke the access rights.
- Users shall be required to re-authenticate themselves after a specific period of inactivity. All systems wherever possible shall use inactivity timeout for sensitive applications.
- All users shall be granted “read” access to all information classified as “public”. Other rights to such information shall be strictly reserved with the owner of such information.
- Non-employee Internal System IDs – In addition to meeting the above requirements for internal system access, non-employees have additional constraints that must be adhered to by the non- employee. The leader responsible for the non-employee is accountable for all actions taken by the non-employee. All non-employee systems access should be limited to information necessary for specific business purposes and should be in accordance with the requirements set forth in the Non- Employee Access Standards and the contract governing the work.
- All Choice Equity Broking Pvt. Ltd. (Choice) information systems privileges shall be disabled within 24 hours of receipt of the termination request, unless otherwise it is stated to disable the access on the last day of the employment or any specific day of employment.

**Access Logs**
- Access logs for critical assets/ infrastructure shall be monitored and reviewed on near real time basis. In case of security breaches, Incident shall be reported to the Chief Information Security Officer (CISO) as well.

**Managing User IDs**
- User Ids shall follow a standard naming convention for all computer systems to facilitate user identification. Naming conventions shall cover all end users, contractors, consultants and vendors. Generic IDs shall not be used.
- Access to information services shall be controlled by using unique user Ids, wherever possible, which shall enable:
  - individual accountability
  - permit centralized identification of users
  - aids in timely control of potential threats
- The application / system administrators are responsible for identifying inactive accounts and disabling them. If a user account has been inactive for more than 30 days, the application / system administrator shall disable the account after confirmation from the respective LOB Heads. The application / system administrator shall reactivate the account only after receiving a written request from the user and approval regarding the same from his LOB Head.
- "Guest" accounts and other default accounts shall be disabled on all servers.

Each user is personally responsible for the usage of his or her user ID and password.

**Password Management**
User authentication refers to the methods by which a user proves his or her identity. All users must be positively identified prior to using any computer or communication system resources. Traditional user authentication consists of a user ID/password.

The authentication process verifies the identity of a user attempting to access a system. The process uses one or more of three tests to determine if the user is the authorized user. Passwords are confidential information and are the most commonly used security tool in company systems. Each user is responsible for maintaining and protecting the passwords, PINs, and tokens used for system access. As they become available, enhanced authentication methods may be used.

A good password is the best defense against inadvertent or malicious damage to computer programs and company data. If passwords can be easily guessed or viewed, or if there are not sufficient integrity controls, a perpetrator can break into company systems and gain access to the business data. If a legitimate user ID/password is used to gain access, the breach can go undetected long enough for the perpetrator to do damage.

Organization would promote strong password controls and ensure the controls are updated from time to time as per security recommendations.

- An initial password shall be provided to the users in a secure manner during the user creation process and the system shall be configured to force the users to change the initial password immediately after the first logon.
- Passwords shall be conveyed to users in a secure manner. Passwords shall never be disclosed through third parties or through unprotected (clear text) electronic mails.
- Password constraints and account policy shall be enforced for all user and administrative accounts on operating systems, applications, databases and all other information protected by passwords controls. The controls enforced shall be:
  - Passwords shall be at least eight characters in length
  - Password shall be a mix of alphabets, numerals and special characters
  - Password shall not be a part or same as username or user Ids
  - New password shall not be same as of the previous 4 passwords (Password history)
  - Passwords shall not be transmitted over the network without encryption
- Minimum password age shall be 3 days. In Active Directory, at user level, password expiry shall be set to ‘Never Expiry’. Additionally, multi-factor authentication shall be enabled on available accounts. Non-AD integrated application specific password shall continue to have expiry period of 60 days.
- Users shall not choose passwords, which can be easily guessed such as the user’s name, car registration number, telephone number, birth date etc.
- Account shall be locked out after 3 consecutive failed access attempts. For unlocking the user account, user may choose the self-service option or contact Service Desk. Positive user identification is mandatory before any account is unlocked by Technology or by an automated system.
- In case the user has forgotten the password, the user needs to reset the password
- Password shall be changed immediately if a user suspects that the password is leaked or compromised.
- All vendor-supplied default passwords (or other alternative access mechanisms) shall be changed before any computer or communications system is used for any Choice Equity Broking Pvt. Ltd. (Choice) business activity beyond initial evaluation in a test environment. These standards apply to passwords associated with end-user user IDs, as well as passwords associated with systems administrator and other privileged user IDs.
- Locked account shall be automatically unlocked by the system after 30 minutes.
- Users shall not share their password with anyone, including their reporting supervisors or colleagues.
- Passwords should not be written down or left in a place where unauthorized persons might discover them.
- Passwords shall not be stored unencrypted format in system resources.
- Appropriate procedures shall be put in place for storing and management of administrative passwords for critical information systems.
- Due to system limitations or business necessity if any of the password or logical access control policy cannot be followed, associated risk should be brought the attention of the management, and exception shall be documented. Compensating controls shall be put in place to mitigate the associated risk.

**Ensuring Logical Security on Laptops and Desktops**
Securing Information on Laptops and Desktops

- The folders or disk drives in individual desktops or laptops shall not be shared unless appropriate access controls have been enabled on the folder or the disk drive. Sharing of any information classified as ‘confidential’ is not permitted unless authorized by concerned authority.
- Prior LOB Head approval shall be required to use any removable devices like floppy drives, CD Writer etc.

**Controlling Privileged User IDs**
Use of privileged user IDs

- User ids with high-level access privileges (administrators) shall only be used in the event of emergency.
- System Administrator shall logon using their normal user Id when performing regular work duties rather than logging in as the administrator. Use of Administrator profile shall be limited to administrative activities only.
- User id’s with privilege access shall be managed with PAM tool.
- All emergency actions, which bypass normal access control procedures, shall be logged and reported for immediate review by delegated authority.

**Use of Generic IDs**
- Local logon rights should be disabled for generic system ID’s
- Generic ID’s should not have system or security administration authority
- All interactive login methods (FTP, telnet, rexec, SSH, etc.) should be disabled for such user ID’s by either:
  - Denying access to the user rights: 'Access this computer from network' and 'Logon through Terminal Services' OR
  - Another method that disables interactive login methods for the given service or protocol
- If the password for such user ID is hardcoded in a file, the same needs to be encrypted and should not be in clear text.
- Id owner details should be established so ownership is documented for accountability

**Use of Privileged utility programs**
Sensitive system utilities are the utilities which give unrestricted access to the critical system resources. The sensitive system utilities include but not limited to Format, User addition / deletion / update, Change in Network Settings.

**Restricting Use of System Utilities**
- Access to system utilities shall be restricted to authorized personnel in accordance with their business functions and needs.
- All unnecessary sensitive utilities shall be removed / disabled from the system.
- The use of all system utilities shall be logged and regularly reviewed by the Technology team.
- It shall be ensured that normal users do not have access rights to use utilities. Any backend update to the data using SQL / similar utilities shall be done only after approval of credential request over email.
- System utilities shall be separated from application software.

### 1.5.0 Extended Authentication
<!-- section_id: ISMS-2.5 -->
When using an offsite remote/external connection to company systems or networks, there are different user authentication requirements based on the role used and the information desired.

A User ID and password is required when employees are accessing information about themselves in their role as a customer, providing access to information such as insurance mutual funds, demat account, etc. In order to access employee human resources application such as online pay stub, leaves, performance etc, a second User ID and password will be required.

### 1.6.0 Session Management and Data Movement
<!-- section_id: ISMS-2.6 -->
Session security controls are a combination controls used to limit access appropriately. Such controls may include:

- Individual user - Identification, Authentication
- Logical grouping - Authorization by membership in a group
- Perimeter - Managing user and system traffic between the public and the company’s restricted internal use network.

### 1.7.0 Unauthorized Access
<!-- section_id: ISMS-2.7 -->
- Accessing Information Systems - Users using corporate computer systems shall access or attempt to access only those information systems and networks for which they have been granted access to perform their job functions.
- Damaging Information Systems - Users using Choice Equity Broking Pvt. Ltd. (Choice) computer networks shall not engage in activities that damage, disrupt or interfere with the operations of multi-user information systems to which they are connected.
- Circumventing Access Control Mechanisms - Programmers and other users must refrain from installing trap doors that circumvent the authorized access control mechanisms found in operating systems and/or access control packages. Shortcuts bypassing systems security measures, as well as pranks and practical jokes involving the compromise of systems security measures are prohibited.
- Customer Requests to Compromise Security Mechanisms - Requests to compromise Choice Equity Broking Pvt. Ltd. (Choice) security mechanisms must NOT be satisfied unless (a) the Chief Operating Officer provides written approval in advance, or (b) Choice Equity Broking Pvt. Ltd. (Choice) is compelled to comply by law, or (c) is ordered in writing to do so by its General Counsel and CEO.
- Social Engineering - A social engineer is an unauthorized person who impersonates an authorized user. The social engineer will use personal charm, manipulation or inside knowledge to persuade the authorized person that he or she is legitimate. The social engineer asks an authorized company user to do something that should not be done for an unauthorized person. Employees must not give company confidential, restricted internal use, or non-restricted internal use data or access information to unidentified persons. Any actual or suspected Social Engineering attempt must be reported to Technology Team.
- Compromising Security Measures - Incidents involving system cracking (hacking), password cracking (guessing), file decryption, software copying, or similar unauthorized attempts to compromise security measures may be unlawful and will be considered serious violations of this policy.
```

```markdown
## 4.0 Mobile Device Policy
<!-- section_id: CSP-4.0 -->

### 1.0 Purpose
<!-- section_id: CSP-4.1 -->

Choice Equity Broking Pvt. Ltd. (Choice) and its subsidiaries, associates, and entities (collectively referred to as ‘Choice’). The policy aims at providing guidelines to authorized users on usage of Choice supported Mobile devices for permitted corporate services.

### 2.0 Scope
<!-- section_id: CSP-4.2 -->

This policy applies to users authorized to use corporate or personally owned (BYOD) mobile devices. Mobile devices currently scoped as part of this policy are limited to the following:

- Apple iOS 11.0 and later
- Apple iPad OS 13.0 and later
- Mac OS X 10.14 and later
- Android 5.0 and later (including Samsung KNOX Standard 2.4 and higher)

Corporate mobility services provisioned under corporate mobile devices policy are:

- Email services
- Outlook Contacts
- Outlook Calendar
- Business Applications
- Corporate Collaboration Tools

> **Note**: Above services shall only be provisioned via [[control:MDM]] (Mobile Device Management)/ [[control:MAM]] (Mobile Application Management). MDM/ MAM is security software that helps administer mobile device and protects corporate services/data published over mobile device with below controls:

- Protection against Jailbroken/Rooted device – MDM/ MAM detect and restrict installation of corporate application on rooted or jailbroken devices.
- Protection against unauthorized access - In case where a user does not implement screen lock, MDM/ MAM can use a policy in order to prevent data theft or unauthorized application usage.
- The corporate data is not accessible outside the MDM/ MAM container. It protects the data stored in the devices by access control policies.
- Current/Updated app on all endpoints – Reduces pain of IT & user on installing updated app. Ensure all the endpoints with current/updated app.
- Data wipe – For resigned/unwanted employees or stolen devices.

### 3.0 Policy for Corporate Devices
<!-- section_id: CSP-4.3 -->

#### 3.1 Eligibility
<!-- section_id: CSP-4.3.1 -->

- For existing employees, user will be required to raise a Logit ticket for corporate mobile device.
- For new joiners, corporate mobile device may be allocated based on Logit raised by HR.

#### 3.2 Device Provisioning
<!-- section_id: CSP-4.3.2 -->

- Users seeking corporate mobility service can avail the services on their personal device with appropriate versions of mobile device (as defined in scope – 2.0).
- The user’s device should meet the pre-requisites and should not be rooted or jailbroken.
- A user can only have one device configured under this policy.

#### 3.3 Device Configuring
<!-- section_id: CSP-4.3.3 -->

- **Corporate Devices**
  - [[role:Technology Mobility team]] shall be responsible for configuring of corporate devices to eligible users.
  - Procurement/ Purchase/ [[role:Asset team]] hands over the corporate device to Technology Mobility team.
  - Technology Mobility team configures the device as per corporate policy and hands over the device to user.

- **Personal Devices**
  - Users are required to download the company portal application and register the device.
  - Users are expected to complete the configuration process by following on-screen instructions.
  - User shall backup the data prior configuration. Technology Mobility team will not be responsible for any data loss that happens during the configuration of corporate mobile services.

#### 3.4 Pre-requisites
<!-- section_id: CSP-4.3.4 -->

- For personal device, please refer Section 2.0.
- Data services must be available on the device to allow Technology Mobility team to provision the corporate services.

#### 3.5 Responsibilities
<!-- section_id: CSP-4.3.5 -->

- Technology Mobility team shall be responsible for providing support for authorized corporate service devices only.
- Technology Mobility team shall not be responsible for the accessories, service fees or charges incurred due to personal use of company-provided equipment or services, and any other related billing costs.
- User shall be responsible and accountable for storing any personal or company’s sensitive, proprietary or confidential information on the device under this policy.
- User shall be responsible for physical safeguarding of the mobile device.

#### 3.6 Appropriate usage policy for corporate service device
<!-- section_id: CSP-4.3.6 -->

- The user shall not use this mobile device for business activities that mandate certain safeguard/protocol to be followed in accordance with prevailing laws including but not limited to, call recording, logging, monitoring etc.
- User shall refrain from malicious downloads and storage on this device.
- Users shall not install any unauthorized software (i.e hacking, cracking etc.) on the devices under this policy.
- Users shall not leave the devices unattended anytime.
- Users shall not share the device passwords with anyone.
- When travelling devices would be kept within close view and shall not be left unattended at any point in time to avoid theft.
- In the event, if the device (company provided or personal) is lost or stolen, users are required to report the incident to Technology Mobility team immediately. These actions shall ensure that appropriate steps are taken to remotely wipe information residing on the device.
- The user shall not be allowed to create backup of the data on an unauthorized device.
- In case of violation, corporate services will be discontinued by the Technology Mobility team without any prior notice to the user.

#### 3.7 Support Service Levels
<!-- section_id: CSP-4.3.7 -->

- For corporate service mobile devices, Technology Mobility team would be responsible for supporting corporate applications/services only.

#### 3.8 Exit User
<!-- section_id: CSP-4.3.8 -->

- In cases where the user exits through the resignation or termination process, Technology Mobility team would remotely remove/wipe the MDM container. This activity would not impact the user’s personal data stored anywhere outside the MDM container.
- For all the Apple devices, it is mandatory for the users to support the Technology Mobility team to delete their Apple ID/Profile so that the devices can be used / accessible by the Technology Mobility team.

#### 3.9 Violation
<!-- section_id: CSP-4.3.9 -->

- Any Violation of the policy, or any of its tenets, could result in disciplinary action which may even lead to and include termination of employment and civil and/or criminal prosecution under local, state and federal laws.

### 4.0 Exceptions
<!-- section_id: CSP-4.4 -->

- Exceptions shall not be universal but shall be agreed on a case-by-case basis, upon official request made by the information owner. These may arise, for example, because of local circumstances, conditions or legal reason existing at any point of time.
- All exceptions during implementation shall be submitted by the concerned person responsible for implementation. These shall be submitted through the Exception Form and sign-off on the same shall be maintained as per the below grid.

## 5.0 Remote Access Policy
<!-- section_id: CSP-5.0 -->

### 1. Purpose
<!-- section_id: CSP-5.1 -->

The purpose of this policy is to define rules and requirements for connecting to Choice Equity Broking Pvt. Ltd.'s network from any host. These rules and requirements are designed to minimize the potential exposure to Choice Equity Broking Pvt. Ltd. from damages which may result from unauthorized use of Choice Equity Broking Pvt. Ltd. resources. Damages include the loss of sensitive or company confidential data, intellectual property, damage to public image, damage to critical Choice Equity Broking Pvt. Ltd. internal systems, and fines or other financial liabilities incurred as a result of those losses.

### 2. Scope
<!-- section_id: CSP-5.2 -->

This policy applies to all Choice Equity Broking Pvt. Ltd. employees, contractors, vendors and agents with a Choice Equity Broking Pvt. Ltd.-owned or personally-owned computer or workstation used to connect to the Choice Equity Broking Pvt. Ltd. network. This policy applies to remote access connections used to do work on behalf of Choice Equity Broking Pvt. Ltd., including reading or sending email and viewing intranet web resources. This policy covers any and all technical implementations of remote access used to connect to Choice Equity Broking Pvt. Ltd. networks.

### 3. Policy
<!-- section_id: CSP-5.3 -->

It is the responsibility of Choice Equity Broking Pvt. Ltd. employees, contractors, vendors and agents with remote access privileges to Choice Equity Broking Pvt. Ltd.'s corporate network to ensure that their remote access connection is given the same consideration as the user's on-site connection to Choice Equity Broking Pvt. Ltd..

General access to the Internet for recreational use through the Choice Equity Broking Pvt. Ltd. network is strictly limited to Choice Equity Broking Pvt. Ltd. employees, contractors, vendors and agents (hereafter referred to as “Authorized Users”). When accessing the Choice Equity Broking Pvt. Ltd. network from a personal computer, Authorized Users are responsible for preventing access to any Choice Equity Broking Pvt. Ltd. computer resources or data by non-Authorized Users. Performance of illegal activities through the Choice Equity Broking Pvt. Ltd. network by any user (Authorized or otherwise) is prohibited. The Authorized User bears responsibility for and consequences of misuse of the Authorized User’s access.

> [!CROSS-REF]
> Refer to [[doc:acceptable-use-policy]] for further information and definitions.

Authorized Users will not use Choice Equity Broking Pvt. Ltd. networks to access the Internet for outside business interests.

### 4. Requirements
<!-- section_id: CSP-5.4 -->

#### 4.1 Secure remote access must be strictly controlled with encryption (i.e., Virtual Private Networks (VPNs)) and strong pass-phrases.
<!-- section_id: CSP-5.4.1 -->

#### 4.2 Authorized Users shall protect their login and password, even from family members.
<!-- section_id: CSP-5.4.2 -->

#### 4.3 While using a Choice Equity Broking Pvt. Ltd.-owned computer to remotely connect to Choice Equity Broking Pvt. Ltd.'s corporate network, Authorized Users shall ensure the remote host is not connected to any other network at the same time, with the exception of personal networks that are under their complete control or under the complete control of an Authorized User or Third Party.
<!-- section_id: CSP-5.4.3 -->

#### 4.1.1 Use of external resources to conduct Choice Equity Broking Pvt. Ltd. business must be approved in advance by InfoSec and the appropriate business unit manager.
<!-- section_id: CSP-5.4.1.1 -->

#### 4.1.2 All hosts that are connected to Choice Equity Broking Pvt. Ltd. internal networks via remote access technologies must use the most up-to-date anti-virus software, this includes personal computers. Third party connections must comply with requirements as stated in the Third Party Agreement.
<!-- section_id: CSP-5.4.1.2 -->

#### 4.1.3 Personal equipment used to connect to Choice Equity Broking Pvt. Ltd.'s networks must meet the requirements of Choice Equity Broking Pvt. Ltd.-owned equipment for remote access as stated in the Hardware and Software Configuration Standards for Remote Access to Choice Equity Broking Pvt. Ltd. Networks.
<!-- section_id: CSP-5.4.1.3 -->

### 5. Policy Compliance
<!-- section_id: CSP-5.5 -->

#### 5.1 Compliance Measurement
<!-- section_id: CSP-5.5.1 -->

The Infosec team will verify compliance to this policy through various methods, including but not limited to, business tool reports, internal and external audits, and feedback to the policy owner.

#### 5.2 Exceptions
<!-- section_id: CSP-5.5.2 -->

Any exception to the policy must be approved by the Infosec team in advance.

#### 5.3 Non-Compliance
<!-- section_id: CSP-5.5.3 -->

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## 6.0 Bring Your Own Device (BYOD) Policy
<!-- section_id: CSP-6.0 -->

### 1. Background
<!-- section_id: CSP-6.1 -->

Choice Equity Broking Pvt. Ltd. and its subsidiaries, associates, and entities (collectively referred to as ‘Choice’). This Bring Your Own Device Policy (‘the Policy’) is applicable to all individuals (hereinafter referred to as Choice Users) of Choice and its subsidiaries and associate entities in India and overseas (collectively referred to as Choice, at all levels and grades, whether regular, fixed term or temporary, without exception.

Choice grants the Choice Users the privilege of using their Personal Electronic Devices (‘PEDs’) for work-related purposes, for their convenience. Choice reserves the right to revoke this privilege if Choice users do not abide by the procedures outlined in this policy. Choice users must agree to the terms and conditions set forth in this policy in order to be able to connect their PEDs to the Choice network.

This Policy is intended to protect the security and integrity of Choice data and technology infrastructure.

### 2. Scope
<!-- section_id: CSP-6.2 -->

This Policy includes within its scope the following PEDs:

- Personal laptop/desktop to connect office desktop via Arcon
- Personal laptop/desktop to connect Azure Virtual desktop
- Personal laptop/desktop for accessing O365 and internal applications using Windows 10

> **Note**: Above list is indicative and may be limited based on compatibility of technology.

### 3. Policy
<!-- section_id: CSP-6.3 -->

#### 3.1 Authorisation
<!-- section_id: CSP-6.3.1 -->

Choice Users need to seek the consent from LOB Head to use their PED for work purposes. For new joinees, HR Relationship Manager shall take the required approval from LOB Head.

#### 3.2 Acceptable Use
<!-- section_id: CSP-6.3.2 -->

- Acceptable business use is defined as activities that directly or indirectly support the business of Choice.
- Acceptable personal use on Choice time is defined as reasonable and limited personal communication or recreation, such as reading or game playing.
- While at work, Choice Users are expected to exercise the same discretion in using their PEDs as is expected for the use of company devices. Choice policies pertaining to anti-harassment, anti-discrimination, anti-retaliation, protection of trade secrets, protection of confidential information and ethics apply to the use of PEDs for work-related activities.
- PEDs with valid license operating system should only be used for BYOD.
- PEDs should not be used at any time to:
  - Store or transmit illicit materials
  - Store or transmit proprietary information belonging to another company
  - Harass others
  - Engage in outside business activities
- Users may use their mobile PEDs to access the Choice-owned resources such as email, calendars, contacts, documents, etc.

#### 3.3 IT Support
<!-- section_id: CSP-6.3.3 -->

- For personal owned laptop/desktop connectivity issues, operating system or hardware-related issues, Choice User should contact their own vendor for resolution.
- Functionality issue of O365 and Choice’ internal applications will be supported by Choice.
- For issues with Choice’ remote owned laptop/desktop or virtual machines, Choice User should contact Choice for technology support.

#### 3.4 Security
<!-- section_id: CSP-6.3.4 -->

- In order to prevent unauthorized access, PEDs shall be password protected using the features of the PED and a strong password.
- [[control:MFA]] shall be enabled.
- On PEDs, Windows 10 operating system should be installed.
- Choice Users access to Choice’ data shall be limited, based on user profiles defined by IT and automatically enforced.

#### 3.5 Lost, stolen, hacked or damaged equipment
<!-- section_id: CSP-6.3.5 -->

- Choice Users are expected to protect PEDs used for work-related purposes from loss, damage or theft.
- Choice will not be responsible for loss or damage of personal applications or data resulting from the loss of PED’s. Choice Users must immediately notify management in the event their PED is lost, stolen or damaged.
- In case of loss IT will wipe off the data remotely.
- Choice Users may receive disciplinary action up to and including termination of employment for data leakage that is caused willfully.

> **Termination of employment**: Upon resignation or termination of employment, or at any time on request, the Choice User may be asked to produce the PED for inspection. All Choice data on PEDs will be removed by IT upon termination of employment.

#### 3.6 Privacy/ Monitoring
<!-- section_id: CSP-6.3.6 -->

- No staff using the PED should expect any privacy requirements except that which is governed by law.
- Choice has the right, at any time, to monitor and preserve any communication that uses the Choice’ network in any way, including data, voice mail, telephone logs, Internet use and network traffic, to determine proper use.
- Choice reserves the right to review or retain personal and Choice-related data on PEDs or to share the data with government agencies or third parties during an investigation or litigation. Choice may review the activity and analyse usage patterns and may choose to publicise this data to ensure that Choice’ resources in these areas are being used in accordance with this Policy. Furthermore, no staff may knowingly disable any network software or system identified as a monitoring tool.

- Choice reserves the right to disconnect any of the PEDs or disable any of the services without notification to the Choice User/s.

### 4. Review of Policy
<!-- section_id: CSP-6.4 -->

This Policy shall be reviewed at least once in a year or earlier as may be required.

### 5. Exception
<!-- section_id: CSP-6.5 -->

Any deviation to this Policy should be properly documented and COO approval is needed on the same. Deviation will be there for a specific period of time.

## 7.0 Physical and Environmental Security Policy
<!-- section_id: CSP-7.0 -->

### 1. Purpose
<!-- section_id: CSP-7.1 -->

Physical and environmental security policy addresses measures for securing information processing facilities and information assets from unauthorized access, damage or interference or any natural calamities.

### 2. Scope
<!-- section_id: CSP-7.2 -->

This policy and any other associated guidelines apply to the employees of Choice Equity Broking Pvt. Ltd. (Choice) and any person having access to physical assets of Choice Equity Broking Pvt. Ltd. (Choice). This could include contractors, consultants, third-party associates and any temporary employees and covers physical access to computing facilities, hardware, corporate data, application and systems software. These facilities include server rooms / data centers, network control centers and other related areas. Physical access scope is under Admin department and rest is with IT.

### 3. Policy
<!-- section_id: CSP-7.3 -->

#### 3.1 Physical Security
<!-- section_id: CSP-7.3.1 -->

##### 3.1.1 Physical Entry Controls by Admin
<!-- section_id: CSP-7.3.1.1 -->

- Choice Equity Broking Pvt. Ltd. (Choice) shall have a well-defined and secure perimeter.
- All doors shall be locked, when unattended or beyond working hours.
- Security guards shall be placed at minimum, at entry points of the premises at all times.
- The date and time of entry and departure of visitors shall be recorded, and all visitors shall be supervised unless their access has been previously approved; they shall only be granted access for specific, authorized purposes. The identity of visitors shall be authenticated by appropriate means; Directories and internal books or layout plans identifying locations of organizational information processing facilities shall not be readily available or accessible to the public.
- A physical log book or electronic audit trail of all access shall be securely maintained and shall be reviewed as per the need.
- All employees, contractors and external parties shall be required to wear some form of visible identification and shall immediately notify security personnel if they encounter unescorted visitors and anyone not wearing visible identification.
- External party support service personnel shall be granted restricted access to secure areas or confidential information processing facilities only when required; this access shall be authorized and monitored.
- Access rights to secure areas shall be annually / Admin/ Admin reviewed and updated, and revoked when necessary.

##### 3.1.2 Protocol during Pandemic
<!-- section_id: CSP-7.3.1.2 -->

Office entry control & checks will be amended in line with Govt./equivalent authority’s guidelines.

##### 3.1.3 Physical Entry Controls
<!-- section_id: CSP-7.3.1.3 -->

Technology Team shall ensure access to areas where confidential information is processed or stored (e.g. Data Centers) shall be restricted to authorized individuals only by implementing appropriate access controls.

##### 3.1.4 Security of Office and Facilities
<!-- section_id: CSP-7.3.1.4 -->

- **Admin shall ensure:**
  - Facilities to be set up to prevent confidential information or activities from being visible and audible from the outside-area.
  - The place where information-processing equipment is located shall be secured from theft, physical intrusion and environmental hazards.
  - Incoming and outgoing mail (sealed documents/parcels) must be protected from unauthorized use during and outside normal working hours.
  - A gate pass shall be issued for outgoing material. Security Personnel at the entry gate shall not allow any material outside without appropriate gate pass.

- **Technology Team shall ensure:**
  - Support functions and equipment’s e.g. photocopiers, shall be sited appropriately within the secure area to restrict access, which could compromise information. Any equipment shall be taken outside only after an approval from the reporting authority of the asset owner and the Administration department. A written approval shall be obtained for the same and shall be produced to the security personnel on demand.

##### 3.1.5 Security of Office and Facilities
<!-- section_id: CSP-7.3.1.5 -->

- **IT shall ensure:**
  - Printer memory shall be cleared immediately after printing any documents classified as ‘Confidential’.
  - Details of movement of hardware equipment between offices shall be recorded to facilitate easy tracking of inventory and identification of hardware for disposal / buy back or write off.

##### 3.1.6 Securing Access to Secure Areas (Server Rooms, Data Center)
<!-- section_id: CSP-7.3.1.6 -->

- **Technology Team shall ensure:**
  - All critical servers and communications equipment shall be located in secure locked rooms (referred as secure areas) to prevent tampering and unauthorized usage.
  - Additional controls (like access cards shall be in place to secure critical or sensitive information. Access to secure areas shall be strictly controlled e.g. access to server rooms shall be controlled and restricted to authorize personnel like server and database administrators who need to perform their duties.
  - Signs indicating "Authorized Personnel Only" or a similar message shall be prominently posted at all entrances of secure areas.
  - Knowledge or access to the “secure areas” [example: server room, UPS room, trading room etc.] shall be given to employees or third parties on a “need-to-know” basis.
  - Secure areas shall not be visible or identifiable from the outside; i.e. there shall not be any directional signs providing access to such rooms.
  - Secure areas shall be equipped with CCTV systems. The tapes shall be retained for a period of one month.
  - Emergency lighting shall be installed in the server rooms and other such sensitive areas for use during power outages.
  - Visitors and suppliers shall be allowed entry to secure areas with visitor pass for authorized and specific purposes only. Visitors or third parties shall not be permitted unsupervised access to secure areas.
  - A separate register shall be maintained at the entry gate of the secure areas for recording the entry of the people (Employee, vendor, contractors etc.) who do not have regular access to the secure areas. Any such entry to the secure areas shall only be provided after making an appropriate entry in the register.
  - Unsupervised working in secure areas shall be avoided both for safety reasons and to prevent opportunities for malicious activities;
  - Vacant secure areas shall be physically locked and periodically reviewed;

##### 3.1.7 Deliver and loading areas
<!-- section_id: CSP-7.3.1.7 -->

Access points such as delivery and loading areas and other points where unauthorized persons could enter the premises shall be controlled and, if possible, isolated from information processing facilities to avoid unauthorized access. The following guidelines shall be considered:

- Access to a delivery and loading area from outside of the building shall be restricted to identified and authorized personnel;
- The delivery and loading area shall be designed so that supplies can be loaded and unloaded without delivery personnel gaining access to other parts of the building;
- Incoming material shall be inspected and examined for explosives, chemicals or other hazardous materials, before it is moved from a delivery and loading area;
- Incoming material shall be registered in accordance with asset management procedures on entry to the site;
- Incoming and outgoing shipments shall be physically segregated, where possible;
- Security to inform the requesting dept. of incoming material which should be inspected by representative of requesting dept. for any evidence of tampering enroute.

##### 3.1.8 Securing access to the Trading & Dealing rooms
<!-- section_id: CSP-7.3.1.8 -->

- **Admin shall ensure:**
  - Access to trading and dealing rooms shall be strictly controlled. E.g. access to trading room shall be controlled and restricted to authorize personnel like Choice Equity Broking Pvt. Ltd. (Choice) traders who need to perform their duties.
  - Signs indicating "Authorized Personnel Only" or a similar message shall be prominently posted at all entrances of trading and dealing rooms with the help of Admin.
  - Knowledge or access of the trading / dealing rooms shall be given to employees or third party on a “need-to-know” basis.

- **Technology Team shall ensure:**
  - Mobile phone usage shall be prohibited inside the trading and dealing rooms. Secure Storage space for mobile phones shall be provided where traders and dealers shall deposit their mobile phone before entering the trading / dealing areas.

##### 3.1.9 Securing the Premises from Visitors and Suppliers
<!-- section_id: CSP-7.3.1.9 -->

- Employees shall wear the Photo ID badge provided by Choice Equity Broking Pvt. Ltd. (Choice) during their stay on Choice Equity Broking Pvt. Ltd. (Choice) premises.
- Employees not carrying the Photo ID badges shall not be allowed inside the premise without getting a temporary access card issued to himself / herself. The access card shall be issued after verifying the employee. When the card is issued, an auto-generated email alert shall be sent to the employee’s reporting authority. When exiting the premise for the day, the employee shall return the card to the Security Guard in charge, failing to which an auto-generated email alert shall be sent to the employee and escalation to the reporting authority the subsequent day onwards till the card is returned.
- Visitors shall be advised to provide the following details so that the relevant details can be captured for records:
  - Visitor name
  - Company
  - Date
  - Time in
  - Contact details
  - Purpose of visit
  - Whom to meet (Person to be met)
- A visitor badge shall be allotted to every visitor, except VVIP/VIP visitors, eg. Visitors/guests of Manco.
- Employees shall not be authorized to take any visitor near areas demarked as sensitive within the premise. Visitor’s entry shall be restricted to the meeting / discussion rooms only.
- Choice Equity Broking Pvt. Ltd. (Choice) personnel may seek information by questioning all unescorted visitors.

##### 3.1.10 Securing Information Storage Media
<!-- section_id: CSP-7.3.1.10 -->

- **Technology Team shall ensure:**
  - All information storage media (e.g. hard disks, floppy disks, pen drives, magnetic tapes and CD-ROMs) containing sensitive or confidential data shall be physically secured, when not in use.
  - Information storage media shall not be taken outside the computer room or storage area, unless specifically authorized.
  - Physical access to magnetic tape, disk and documentation libraries shall be restricted to authorized personnel only.
  - Back-up media shall be stored in fire resistant safes or cabinets.
  - Employees are not permitted to bring any personal information storage media like cartridge tapes, DAT drives, CDs, pen drives, or floppy drives unless specifically approved by LOB Head.
  - Visitors and third parties shall not be allowed to connect external storage devices to Choice Equity Broking Pvt. Ltd. (Choice) Network, unless authorized by Choice Equity Broking Pvt. Ltd. (Choice) officials.
  - Media containing sensitive corporate information shall be monitored with audit trails.

##### 3.1.11 Securing Offsite Facilities [Disaster Recovery Site]
<!-- section_id: CSP-7.3.1.11 -->

- **Technology Team shall ensure:**
  - Fall back equipment and back-up media shall be stored at a safe distance (at an offsite location) to avoid damage from disaster at the main site.
  - The physical and environmental safeguards available at the off-site location shall provide the same level of security, at a minimum, as at the primary site.

##### 3.1.12 Security Inspections
<!-- section_id: CSP-7.3.1.12 -->

- **Admin shall:**
  - Perform random physical security inspections shall be done at all sites and locations.
  - The results of all inspections shall be documented & appropriate action shall be taken.

#### 3.2 Environmental Security
<!-- section_id: CSP-7.3.2 -->

##### 3.2.1 Ensuring Suitable Environmental Conditions in Data Centre
<!-- section_id: CSP-7.3.2.1 -->

- **Technology Team shall ensure:**
  - Temperature and humidity levels shall be monitored and maintained, especially in Server/UPS Room.
  - Smoking shall be strictly prohibited inside the office area.
  - Eating and drinking inside server and UPS rooms shall be strictly prohibited.

##### 3.2.2 Securing Premises from Fire
<!-- section_id: CSP-7.3.2.2 -->

- **Admin shall ensure:**
  - All computer systems shall be housed in an environment equipped with fire extinguishers.
  - The fire extinguishers shall be placed at all strategic and prominent locations within Choice Equity Broking Pvt. Ltd. (Choice) office so that they are easily accessible in all areas.
  - Smoke detectors shall be located within the office premises including Server Room.
  - Fire safety equipment shall be checked regularly in accordance with manufacturer's instructions. A maintenance sheet/note shall be attached with the equipment.
  - All fire exits shall be marked clearly and shall be easily accessible from work sections.
  - Hazardous and combustible materials shall be stored at a safe distance from the server rooms and other computer rooms. Computer supplies such as stationery shall not be stored in server rooms.
  - Fire and emergency instructions (via building escape plan) shall be displayed at prominent locations.
  - Functioning and operations of the fire safety devices/equipments installed by Choice Equity Broking Pvt. Ltd. (Choice) shall be explained to the security guards periodically during internal training programs. Some of the Choice Equity Broking Pvt. Ltd. (Choice) employees shall also be made part of such internal training programs.
  - Evacuation drills shall be conducted annually to ensure the effectiveness of the training and instructions to be followed in case of emergency.

##### 3.2.3 Securing Premises from Floods and Water Damage
<!-- section_id: CSP-7.3.2.3 -->

- **Technology Team shall ensure:**
  - Computer and communication rooms shall not be located in areas like basements which are susceptible to water seepage and flooding.
  - Computer and communication rooms shall be located on raised or elevated floors.

- **Admin shall ensure:**
  - Adequate drainage provision shall be provided to prevent water damage or flooding.
  - Water sprinklers shall not be installed in server rooms/storage rooms etc.
  - Electrical equipment, damaged due to water, shall be checked and dried before being returned to service.

##### 3.2.4 Power Supplies
<!-- section_id: CSP-7.3.2.4 -->

###### 3.2.4.1 Power Supply Controls
<!-- section_id: CSP-7.3.2.4.1 -->

- **Technology Team shall ensure:**
  - Uninterrupted Power Supply (UPS) shall be installed to ensure continuous running of all critical computing and supporting equipment at all locations. UPS shall have the capability to continue the power supply to allow for an orderly shutdown of the system.
  - UPS equipment shall be maintained in accordance with the manufacturer’s recommendations to ensure that it is in working condition.
  - Backup generators may be installed for continuous running of information processing systems in case of prolonged power failures. The generator shall be maintained as per the manufacturer’s instructions and shall be checked regularly for sufficient fuel supply.
  - All buildings shall have proper earthing to prevent electric surges.
  - Voltage regulators shall be installed, wherever necessary, to guard against fluctuations in power. Circuit breakers of appropriate capacity shall be installed to protect the hardware against power fluctuations or short circuits.
  - Lightning protection filters shall be installed for the buildings.

###### 3.2.4.2 Power off Switches
<!-- section_id: CSP-7.3.2.4.2 -->

- **Admin shall ensure:**
  - Emergency power off switches shall be installed at strategic locations in order to facilitate rapid power-off in case of an emergency such as a fire.
  - The power-off switches shall be clearly labeled, easily accessible but shielded to prevent accidental activation.

##### 3.2.5 Cabling Security
<!-- section_id: CSP-7.3.2.5 -->

- **Technology Team shall ensure:**
  - Power and telecommunication cables that connect various information processing facilities are exposed to many environmental hazards like sand storms, floods, fire, lightning, cutting due to careless digging or damage by rats and rodents. Cables carrying data or supporting information services shall be protected from interception or damage to reduce the risk of power or communication failure.

##### 3.3 Cabling Standards
<!-- section_id: CSP-7.3.3 -->

- **Technology shall ensure:**
  - Power and telecommunication lines used for information processing facilities shall be laid underground, where possible, or subject to adequate alternative protection.
  - Network cabling shall be protected from unauthorized interception or damage due to environmental hazards e.g. by using conduit or by avoiding routes through public areas.
  - Power cables shall be separated from communication cables to prevent interference.
  - For sensitive or critical systems further controls to consider include:
    - Use of electromagnetic shielding to protect the cables.
    - Controlled access to patch panels and cable rooms.

##### 3.4 Clear Desk Policy and Clear screen policy
<!-- section_id: CSP-7.3.4 -->

- **Technology Team shall ensure** a clear desk policy for papers and removable storage media and a clear screen policy for information processing facilities shall be adopted. The clear desk and clear screen policy shall take into account the information classifications (Ref: Information classification). The following guidelines shall be considered:
  - Sensitive or critical business information, e.g. on paper or on electronic storage media, shall be locked away (ideally in a safe or cabinet or other forms of security furniture) when not required, especially when the office is vacated.
  - Computers and Terminals shall be left logged off or protected with a screen and keyboard locking mechanism controlled by a password, token or similar user authentication mechanism when unattended and shall be protected by key locks, passwords or other controls when not in use.
  - Unauthorized use of photocopiers and other reproduction technology (e.g. scanners, digital cameras) shall be prevented.
  - Sensitive (Confidential/Internal) information and storage media shall be locked (in a fire resistant safe or cabinet), when not required.

##### 3.5 Equipment Security
<!-- section_id: CSP-7.3.5 -->

###### 3.5.1 Equipment sitting and protection
<!-- section_id: CSP-7.3.5.1 -->

Equipment shall be sited and protected to reduce the risks from environmental threats and hazards, and opportunities for unauthorized access. The following guidelines shall be considered to protect equipment:

- **Admin shall ensure:**
  - Storage facilities shall be secured to avoid unauthorized access.
  - Environmental conditions, such as temperature and humidity, shall be monitored for conditions which could adversely affect the operation of information processing facilities.
  - Lightning protection shall be applied to all buildings and lightning protection filters shall be fitted to all incoming power and communications lines.

- **Technology Team shall ensure:**
  - Equipment shall be sited to minimize unnecessary access into work areas.
  - Items requiring special protection shall be safeguarded to reduce the general level of protection required.
  - Information processing facilities handling sensitive data shall be positioned carefully to reduce the risk of information being viewed by unauthorized persons during their use.
  - Equipment processing confidential information shall be protected to minimize the risk of information leakage due to electromagnetic emanation.
  - Guidelines for eating, drinking and smoking in proximity to information processing facilities shall be established.

###### 3.5.2 Supporting utilities
<!-- section_id: CSP-7.3.5.2 -->

Equipment shall be protected from power failures and other disruptions caused by failures in supporting utilities. Supporting utilities (e.g. Fax, telecommunications, water supply, sewage, ventilation and air conditioning) shall:

- Conform to equipment manufacturer’s specifications and local legal requirements.
- Be appraised regularly for their capacity to meet business growth and interactions with other supporting utilities.
- Be inspected and tested regularly to ensure their proper functioning.
- If necessary, be alarmed to detect malfunctions.
- If necessary, have multiple feeds with diverse physical routing.

- **Admin shall ensure:**
  - Emergency lighting and communications shall be provided. Emergency switches and valves to cut off power, water, or other utilities shall be located near emergency exits or equipment rooms.

###### 3.5.3 Physical Security of Laptops and Desktops
<!-- section_id: CSP-7.3.5.3 -->

- **Technology Team shall ensure:**
  - A complete and up-to-date inventory of all laptops/desktops issued by the organization shall be prepared and kept updated at all times with the TSG. Each laptop/desktops shall be marked with the asset code for easy identification.
  - Laptops / Workstations shall be traceable to individual users.
  - Laptops and desktops shall be physically secured at all times to prevent unauthorized access or theft. Each individual shall be accountable for the physical security of his / her laptop / workstation / handheld devices.
  - All Employees to whom laptops / handheld devices are issued are responsible for the security of the data contained within the laptops / handheld devices.

###### 3.5.4 Equipment Maintenance
<!-- section_id: CSP-7.3.5.4 -->

- **Technology Team shall ensure:**
  - All equipment shall be maintained to ensure its continued availability and integrity in accordance with manufacturer's specifications.
  - Only authorized maintenance personnel shall be allowed to service or perform repairs on equipment. A log shall be maintained of all repairs or service work.
  - Records shall be kept of all suspected or actual faults, and of all preventive and corrective maintenance.
  - If equipment needs to be sent offsite for repairs, the confidentiality and integrity of the information, stored in the equipment, shall be ensured. The entire data available on the equipment shall be backed up on a backup device and securely wiped from the equipment.
  - All maintenance requirements imposed by insurance policies shall be complied with.
  - Before putting equipment back into operation after its maintenance, it shall be inspected to ensure that the equipment has not been tampered with and does not malfunction.

###### 3.5.5 Removal of assets
<!-- section_id: CSP-7.3.5.5 -->

- **Technology Team shall ensure:**
  - Equipment, information or software shall not be taken off-site without prior authorization. The following guidelines shall be considered:
  - Employees and suppliers who have authority to permit off-site removal of assets shall be identified.
  - Time limits for asset removal shall be set and returns verified for compliance.
  - Where necessary and appropriate, assets shall be recorded as being removed off-site and recorded when returned.
  - The identity, role and affiliation of anyone who handles or uses assets shall be documented and this documentation returned with the equipment, information or software.

###### 3.5.6 Security of Equipment off Premises
<!-- section_id: CSP-7.3.5.6 -->

- **Technology Team shall ensure:**
  - Security be applied to off-site assets taking into account the different risks of working outside the Choice Equity Broking Pvt. Ltd. (Choice)’s premises.
  - Equipment and media taken off premises shall not be left unattended in public places.
  - Controls for off-premises locations, such as home-working, teleworking and temporary sites shall be determined by a risk assessment and suitable controls applied as appropriate, e.g. lockable filing cabinets, clear desk policy, access controls for computers and secure communication with the office.
  - When off-premises equipment is transferred among different individuals or external parties, a log shall be maintained that defines the chain of custody for the equipment including at least names and organizations of those who are responsible for the equipment.
  - Risks, e.g. of damage, theft or eavesdropping, may vary considerably between locations and shall be taken into account in determining the most appropriate controls.
  - Any equipment can be taken outside office premises only after written permission from the LOB Head.
  - Any equipment or media taken outside the organization’s premises shall be controlled, secured, protected and insured.
  - Employees or contractors shall not remove any Choice Equity Broking Pvt. Ltd. (Choice) property off premises, without prior authorization.
  - A returnable / non-returnable gate pass shall accompany all property movement outside Choice Equity Broking Pvt. Ltd. (Choice).

###### 3.5.7 Secure disposal or re-use of equipment
<!-- section_id: CSP-7.3.5.7 -->

- **Technology Team shall ensure:**
  - All items of equipment containing storage media shall be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.
  - Equipment shall be verified to ensure whether or not storage media is contained prior to disposal or re-use.
  - Storage media containing confidential or copyrighted information shall be physically destroyed or the information shall be destroyed, deleted or overwritten using techniques to make the original information non-retrievable rather than using the standard delete or format function.

###### 3.5.8 Unattended user equipment
<!-- section_id: CSP-7.3.5.8 -->

- **Technology Team shall ensure:**
  - Users shall ensure that unattended equipment has appropriate protection. All users shall be made aware of the security requirements and procedures for protecting unattended equipment, as well as their responsibilities for implementing such protection. Users shall be advised to:
  - Terminate active sessions when finished, unless they can be secured by an appropriate locking mechanism, e.g. a password protected screen saver.
  - Log-off from applications or network services when no longer needed.
  - Secure computers or mobile devices from unauthorized use by a key lock or an equivalent control, e.g. password access, when not in use.

## Annexure/Supporting (Applicable During Pandemic)
<!-- section_id: CSP-Annexure -->

Office entry is restricted to users – All employees have to submit their health declaration in the prescribed format provided by the Organisation (Currently it is on PowerApps and also in an excel for those who cannot access PowerApps), wherein they must confirm they are without any ailments comorbidities such as common illnesses/diseases, which can be linked to upper-respiratory system, eg. diabetes, blood pressure or any of the family member having these or any of these illness/diseases or has a child less than 2 years of age. The address also needs to be validated of the user coming from Containment / Non-Containment zone as defined by Government of Maharashtra.

- Upon receipt of confirmation from the Incident Room to employee, Security, Facilities Team of respective office, clearing the entry protocol, the employee or visitor is allowed to enter in the premise to operate from office.
- Every employee is expected to follow the protocol of wearing a mask, wash hands frequently/sanitize hands, maintain social distance, so as to keep themselves and others safe whilst in the premise.
```


```markdown
## 8.0 Patch Management Policy
<!-- section_id: CSP-8.0 -->

### 1.0 Purpose
<!-- section_id: CSP-8.1 -->

To ensure that the patches are rolled out on the network in a controlled and secure manner.

### 2.0 Scope
<!-- section_id: CSP-8.2 -->

All operating systems, applications, servers, desktops, and network equipment identified in the [[asset:Asset Register]].

### 3.0 Responsibility
<!-- section_id: CSP-8.3 -->

The Head – Technology for execution of this policy. The [[role:Information Security team]] for auditing the policy.

### 4.0 Policy
<!-- section_id: CSP-8.4 -->

The minimum baseline security standards **[MANDATORY]** shall be reviewed from the point of view of various technical vulnerabilities and vendor’s recommendations for additional security patches and updated at least once a year or on a need basis.

#### 4.1 Guidelines for Implementation
<!-- section_id: CSP-8.4.1 -->

- [[role:ISG]] shall document the baseline configuration of all IT assets identified in the [[asset:asset inventory]]. The baseline is the minimum patch level required on the network. The baseline shall be based on industry best practices and fine-tuned to Choice Equity Broking Pvt. Ltd. (Choice) landscape.
- The baseline configuration **[MANDATORY]** shall be reviewed at least once a year.
- Once a baseline has been established, the [[role:Technology team]] shall conduct a patch analysis. The analysis shall involve determining:
  - If all machines on the network meet the minimum baseline established.
  - All available patches for the network.
  - Whether the patches are installed or missing on all machines.
- Vulnerability assessment on the network **[MANDATORY]** shall also be carried out at least once a year. The Technology team shall analyze the severity of vulnerabilities found and prioritize and schedule the patch rollouts required on the basis of the severity found.
- The regular updates received directly from the supplier shall also be maintained centrally and updated.
- Every patch to be deployed **[MANDATORY]** shall be tested before being rolled out onto the production environment on a need basis. The Technology team shall maintain a test plan with acceptance criteria and also develop a rollback strategy for the same. For applications, the rollback strategy will be provided by the internal/external vendor.
- Once successfully tested, the patch shall be deployed in the production environment during the maintenance window period. The Technology team shall also ensure that the rollback plan is in place.
- Once the patch has been deployed, the team shall verify and confirm the successful application of the patch by logging on to the system.

## 9.0 Information Classification Policy
<!-- section_id: CSP-9.0 -->

### 1.0 Purpose
<!-- section_id: CSP-9.1 -->

To ensure that the integrity and confidentiality of information is maintained, an information classification scheme has been designed for Choice Equity Broking Pvt. Ltd. (Choice). The level of security to be afforded to the information/data of Choice Equity Broking Pvt. Ltd. (Choice) is directly dependent on the classification of the information. All employees are expected to familiarize themselves with this information classification scheme, to consistently use it in their business activities.

### 2.0 Scope
<!-- section_id: CSP-9.2 -->

This information classification scheme is applicable to all information including intellectual property (IP), whether stored or transmitted, which is in the possession or under the control of Choice Equity Broking Pvt. Ltd. (Choice). For example, confidential information entrusted to Choice Equity Broking Pvt. Ltd. (Choice) by its customers, suppliers, business partners, and others shall be protected with this information classification scheme. Similarly, the employees, contractors, and service providers of Choice Equity Broking Pvt. Ltd. (Choice) are expected to protect third-party information with the same care that they protect information belonging to Choice Equity Broking Pvt. Ltd. (Choice).

### 3.0 Policy
<!-- section_id: CSP-9.3 -->

#### 3.1 Information
<!-- section_id: CSP-9.3.1 -->

Information is an asset which, like other business assets, has value to the organization and consequently, needs to be protected. Information can be of any form as mentioned below:
- Printed or written on paper
- Stored electronically
- Transmitted by emails or any other electronic means
- Shown on corporate videos
- Spoken in conversation

#### 3.2 Personal Information
<!-- section_id: CSP-9.3.2 -->

- Personally Identifiable Information (PII) is data that can be traced back to an individual and that, if disclosed, could result in harm to that person. Such information includes biometric data, medical information, personally identifiable financial information (PIFI), and unique identifiers such as passport or Social Security numbers.
- Information containing PII data **[MANDATORY]** shall be considered as confidential information and shall be protected using minimum baseline controls mentioned in the Information Classification Policy.
- Personal information received/stored/sent by employees without any business reason will not be treated as confidential information. Safeguarding personal information stored on corporate systems shall be the user's responsibility. Any such personal information stored on corporate infrastructure shall be accessed by Choice Equity Broking Pvt. Ltd. (Choice) only post management approval. For example, employees share personal data with HR to complete the HR formalities and forget to delete these records like PAN card, Salary slip from the corporate systems. Choice Equity Broking Pvt. Ltd. (Choice) shall not be liable to safeguard this data.

#### 3.3 Business Information
<!-- section_id: CSP-9.3.3 -->

Sensitive business information includes anything that poses a risk to the company if discovered by a competitor or the general public. Such information includes trade secrets, acquisition plans, financial data, and supplier and customer information, among other possibilities.
- Information pertaining to business is further classified to restrict the use or access to the information based on its level of sensitivity (for example, confidential, internal, and public). Information is generally classified to protect such information from unauthorized use.
- Any information classified as confidential and internal **[MANDATORY]** shall be protected with minimum baseline controls as mentioned in the Information Classification Policy. Access/sharing of such information shall not be conducted without any business reason and appropriate approval. Information classified as public will have no control and restriction on disclosure and storage.

#### 3.4 Intellectual Property (IP)
<!-- section_id: CSP-9.3.4 -->

Choice Equity Broking Pvt. Ltd. (Choice) Intellectual Property includes anything that poses a risk to the organization if discovered by a competitor or the general public. Such information includes trade secrets, algorithmic trading source codes/products, acquisition plans, financial data, and supplier and customer information, among other possibilities. Such IP may be created by Choice Equity Broking Pvt. Ltd. (Choice) employees or contractors or consultants.
- To protect intellectual property, maintain appropriate asset registers giving details of asset ownership and controls implemented for each asset. Ownership of each Intellectual property needs to be assigned and reviewed on a quarterly basis.
- A detailed authority matrix needs to be developed by respective Business Heads to grant appropriate access to Business-specific IP. The respective Business Head is the overall owner for all the IPs developed and managed by the business unit. Different controls need to be implemented to protect the IP.
- Intellectual Property needs to be classified as “Confidential” by default.

#### 3.5 Classification Responsibilities
<!-- section_id: CSP-9.3.5 -->

The respective Information owners/business owners are responsible for the execution of the policy on Information Classification. Unclassified information shall always be deemed as sensitive information.

#### 3.6 Need to Know
<!-- section_id: CSP-9.3.6 -->

One of the fundamental principles of information security is "need to know." This principle holds that information shall be disclosed only to those people who have a legitimate business need for the information. The following information classification scheme has been designed for Choice Equity Broking Pvt. Ltd. (Choice) to support the need-to-know principle so that information will be protected from unauthorized disclosure, use, modification, and deletion.

#### 3.7 Inventory of Assets
<!-- section_id: CSP-9.3.7 -->

The information of Choice Equity Broking Pvt. Ltd. (Choice) shall be consistently protected throughout its life cycle, from its origination to its destruction. Information shall be protected in a manner commensurate with its sensitivity; no matter where it resides, what form it takes, what technology is used to handle it, and what purpose it serves. Although this Information Classification scheme provides overall guidance to achieve consistent information protection, employees of Choice Equity Broking Pvt. Ltd. (Choice) need to apply and extend these concepts to fit the needs of day-to-day operations.
- Assets associated with information and information processing facilities shall be identified and an inventory of these assets shall be drawn up and maintained.
- The lifecycle of information shall include creation, processing, storage, transmission, deletion, and destruction. Documentation shall be maintained in dedicated or existing inventories as appropriate.
- The asset inventory shall be accurate, up to date, and consistent and aligned with other inventories.

#### 3.7.1 Information Asset Owner
<!-- section_id: CSP-9.3.7.1 -->

The information asset owner is the individual who oversees the implementation and is responsible for the availability of the information. The information asset owner is responsible for defining the access matrix for policy implementation. Information Owner shall coordinate with the information asset custodian to ensure the access privileges as defined on a “need to know” basis is implemented.
- Any individual creating any official document related to the company, he/she becomes an information owner for those set of documents created by him. There shall be an information owner for every information asset. The information owners shall be responsible for assigning/maintaining appropriate information classifications for the critical information under their custody as defined below.
  - Ensure that assets are inventoried.
  - All files/emails created by individuals shall be owned and classified by them.
  - The information classification process shall be completed for existing critical information and shall be undertaken for any new avenues that can create new forms/instances of the information like new software applications.
  - The same information stored in several media formats (either hard copy or electronic) shall have the same level of classification.
  - Define and periodically review access restrictions and classifications to important assets, considering applicable access control policies.
  - Ensure proper handling when the asset is deleted or destroyed.

#### 3.7.2 Acceptable Use of Information Assets
<!-- section_id: CSP-9.3.7.2 -->

- The Choice Equity Broking Pvt. Ltd. (Choice) information assets shall be used only for business purposes.
- The responsibility of ensuring the security of the asset shall lie with the asset owner (information owner).
- However, the user shall exercise Due Diligence and Due Care towards the information asset assigned to him.
- Any misuse, abuse of Information asset shall be considered as a policy violation.
- Information assets shall not be shared with unauthorized individuals.
- Users must not engage in activities that could compromise the security of information or assets, such as unauthorized access, sharing, copying, or downloading data, or using personal devices without security controls.
- Employees, contractors, and third parties must ensure that confidential information is protected and not disclosed to unauthorized individuals or external parties.
- Only licensed, authorized, and secure software is permitted for use on organizational systems. Unauthorized software, including pirated or unapproved applications, is prohibited.
- Minimal or no personal use of organizational information and assets is permitted. Any personal use must not interfere with work responsibilities or compromise security.
- The organization reserves the right to monitor the use of information and assets to ensure compliance with security policies, detect suspicious activities, and maintain an audit trail for accountability.
- Violation of acceptable usage policies will result in disciplinary action, which may include termination of employment, legal action, and reimbursement for damages if any.

#### 3.7.3 Return of Assets
<!-- section_id: CSP-9.3.7.3 -->

- All employees and external party users shall return all the Choice Equity Broking Pvt. Ltd. (Choice) assets in their possession upon termination of their employment, contract, or agreement.
- The termination process shall be formalized to include the return of all previously issued physical and electronic assets owned by or entrusted to the Choice Equity Broking Pvt. Ltd. (Choice).
- In cases where an employee or external party user purchases the Choice Equity Broking Pvt. Ltd. (Choice)’s equipment or uses their own personal equipment, procedures shall be followed to ensure that all relevant information is transferred to the organization and securely erased from the equipment.
- In cases where an employee or external party user has knowledge that is important to ongoing operations, that information shall be documented and transferred to the Choice Equity Broking Pvt. Ltd. (Choice).
- During the notice period of termination, the Choice Equity Broking Pvt. Ltd. (Choice) shall control unauthorized copying of relevant information (e.g., intellectual property) by terminated employees and contractors.

#### 3.8 Information Classification Matrix
<!-- section_id: CSP-9.3.8 -->

Information owners of Choice Equity Broking Pvt. Ltd. (Choice) shall use the following matrix to classify information assets in a manner that balances the risk of compromise with the needs of normal business operations.

| Classification Level | Definition | Examples |
|----------------------|------------|----------|
| Confidential (Level III) | This classification applies to the most sensitive business information, which is intended strictly for use within Choice Equity Broking Pvt. Ltd. (Choice). Its unauthorized disclosure could seriously and adversely impact Choice Equity Broking Pvt. Ltd. (Choice), its stockholders, its business partners, and/or its customers leading to legal and financial repercussions and adverse public opinion. Information that some people would consider to be private is included in this classification. | Investment plans, trading positions, trading strategies (long/short), Algorithm Trading (source codes/developed products), merger and acquisition plans, customer information, information security data, Strategy Documents. Employee performance evaluations, internal audit reports, short-term marketing plans, analysis of competitive products/services and intellectual capital of Choice Equity Broking Pvt. Ltd. (Choice) which comprises the collective experience, knowledge, skill, and information of Choice Equity Broking Pvt. Ltd. (Choice) and its people. Sensitive personal information and information that can come under data protection act/legislation. |
| Internal (Level II) | This classification applies to all other information, which does not clearly fit into any of the other two classifications. While its unauthorized disclosure is against policy, it is not expected to seriously or adversely impact Choice Equity Broking Pvt. Ltd. (Choice), its employees, its stockholders, its business partners, and/or its customers. | Choice Equity Broking Pvt. Ltd. (Choice) internal telephone directory, training materials, and policy documents. |
| Public (Level I) | This classification applies to information, which has been explicitly approved by Choice Equity Broking Pvt. Ltd. (Choice) management for release to the public. By definition, there is no such thing as unauthorized disclosure of this information and it may be freely disseminated without potential harm. | Published research reports, Published annual/quarterly reports, Web site content, Service brochures, advertisements, job opening announcements, and press releases. |

#### 3.8.1 Cumulative Classification
<!-- section_id: CSP-9.3.8.1 -->

The information classification levels represent cumulative information sensitivity. As the levels of sensitivity increase, the access and modification controls become more rigorous and comprehensive. For example, confidential information is a restricted subset of internal information and requires additional security controls.

#### 3.8.2 Minimum Baseline Security Control Matrix
<!-- section_id: CSP-9.3.8.2 -->

The requirements in the following table outline the minimum baseline security control (MBSC) mechanisms that shall be used for each information classification.

| Security Objective | Public | Internal | Confidential |
|--------------------|--------|----------|--------------|
| Identification and Authentication | None | User IDs and Passwords | User IDs and Passwords, Strong Authentication (2 Factor) |
| Authorization and Access Control | Access Control for Modification | Authorization for granting access by LOB Head, access control as per functions, or directory level access control | Access control |
| Confidentiality | None | Encryption over public communications facilities (Internet, dial-up) | Encrypted communications and encrypted files on storage media |
| Integrity | Access/change control | Minimal audit trail (e.g., document history), data integrity checks | Detailed audit trail (e.g., system-level file history), “maker-checker”, Field-level change history |
| Non-repudiation | Access/change control | Minimal audit trail (e.g., document history) | Detailed audit trail (e.g., system-level file history, Field-level change history, digital signatures) |
| Auditing | Modification, events | User activities, access denials | All events |
| Availability | Virus scanning, backup/restore | Virus scanning, backup/restore | Virus scanning, strong change control over system configuration, backup/restore |

#### 3.8.3 Consistent Classification Labeling
<!-- section_id: CSP-9.3.8.3 -->

All confidential information in physical format shall be labeled accordingly, from the time it is created until the time it is destroyed or re-labeled. Such markings shall appear on all manifestations of the information (hard copies, floppy disks, CD-ROMs, etc.).

#### 3.8.4 Handling of Assets
<!-- section_id: CSP-9.3.8.4 -->

The handling of sensitive material shall be guided by:
- Access restrictions supporting the protection requirements for each level of classification.
- Storage of IT assets in accordance with manufacturers’ specifications.
- Labeling material to reflect its sensitivity and security classification.
- Minimizing distribution of sensitive material.
- Recording authorized recipients, marking information with the recipient’s identity, confirming receipt of transmitted data, and periodically reviewing records of authorized recipients.
- Checking completeness of sensitive material (e.g., by ensuring all information is Input/processed and there is proper accounting for all computer media).
- Sensitive documents and data storage media shall be stored in physically secure locations (e.g., locked, fireproof cabinets, etc.).

## 10.0 Capacity Planning Policy
<!-- section_id: CSP-10.0 -->

### 1. Managing Capacity for Information Processing Facilities
<!-- section_id: CSP-10.1 -->

- Capacity planning process ensures that adequate capacity is available and that best and optimal use is made of it to meet performance needs. Capacity planning process shall cover all critical IT resources including the following:
  - Server resources
  - Network resources
  - Application software
  - Critical PCs/Laptops
- Capacity of information processing facilities shall be monitored continuously, and the data gathered shall be used for projecting future capacity requirements and identifying potential bottlenecks.
- Items to monitor, include but are not limited to the following:
  - Processors
  - Primary memory (RAM)
  - Secondary memory (Hard disk)
  - Backup media
  - Printers and other output devices
  - Communication systems
```


```markdown
## 15.0 Cloud Computing Policy
<!-- section_id: CSP-15.0 -->

### 1. Introduction
<!-- section_id: CSP-15.1 -->

The purpose of this document is to set out the organization’s policy in the area of cloud computing. Choice Equity Broking Pvt. Ltd. makes extensive use of [[control:cloud computing]] services in the delivery of its core business systems. The nature of these services is such that data is stored outside of the Choice Equity Broking Pvt. Ltd. internal network and is subject to access and management by a third party. Furthermore, many cloud services are offered on a multi-tenanted basis in which the infrastructure is shared across multiple customers of the [[external:CSP]], making effective and secure segregation a key requirement.

It is therefore essential that rules are established for the selection and management of cloud computing services so that data is appropriately protected according to its business value and classification.

Cloud computing is generally accepted to consist of the following types of services:

- **Software-as-a-Service (SaaS)**: The provision of a hosted application for use as part of a business process. Hosting usually includes all supporting components for the application such as hardware, operating software, databases, etc.
- **Platform-as-a-Service (PaaS)**: Hardware and supporting software such as operating system, database, development platform, web server, etc. are provided but no business applications.
- **Infrastructure-as-a-Service (IaaS)**: Only physical or virtual hardware components are provided.

This policy applies to the use of all types of cloud computing services and is particularly relevant where personal data is stored.

### 2. Policy
<!-- section_id: CSP-15.2 -->

It is Choice Equity Broking Pvt. Ltd.'s policy in the area of cloud computing that:

- Data belonging to Choice Equity Broking Pvt. Ltd. will only be stored within cloud services with the prior permission of the Choice Equity Broking Pvt. Ltd., Directors.
- Appropriate risk assessment must be carried out regarding proposed or continued use of cloud services, including a full understanding of the information security controls implemented by the [[external:CSP]].
- Due diligence must be conducted prior to sign-up to a cloud service provider to ensure that appropriate controls will be in place to protect data. Preference will be given to suppliers who are certified to the [[regulatory:ISO27001]] international standard and who comply with the principles of the [[regulatory:ISO27017]] and [[regulatory:ISO27018]] codes of practice for cloud services.
- Service level agreements and contracts with cloud service providers must be reviewed, understood, and accepted before sign-up to the service.
- Contracts involving personal data must be checked to ensure that they comply with applicable data protection legislation. If not, a separate data processing agreement may be required.
- Roles and responsibilities for activities such as backups, patching, log management, malware protection, and [[process:incident management]] must be agreed and documented prior to the commencement of the cloud service.
- Procedures must be established to ensure that activities that are irreversible in the cloud environment (e.g., deletion of virtual [[asset:servers]], terminating a cloud service, or restoration from backups) are subject to appropriate controls to avoid error. Supervision by a second, suitably qualified person must be a stated part of such procedures.
- The location of the data stored with the [[external:CSP]] must be understood and the applicable legal basis established, such as the country whose law applies to the contract.
- Where available, [[control:MFA]] must be used to access all cloud services.
- Sufficient audit logging must be available to allow Choice Equity Broking Pvt. Ltd. to understand the ways in which its data is being accessed and to identify whether any unauthorized access has occurred.
- Confidential data stored in cloud services must be encrypted at rest and in transit using acceptable technologies and techniques. Where possible, encryption keys will be held by Choice Equity Broking Pvt. Ltd. rather than the supplier.
- Choice Equity Broking Pvt. Ltd. policies for the creation and management of user accounts will apply to cloud services.
- Backups must be taken of all data stored in the cloud. This may be performed either directly by Choice Equity Broking Pvt. Ltd. or under contract by the cloud service provider.
- All Choice Equity Broking Pvt. Ltd. data must be removed from cloud services in the event of a contract coming to an end for whatever reason. Data must not be stored in the cloud for longer than is necessary to deliver business processes.

## 16.0 Data Disposal and Retention Policy
<!-- section_id: CSP-16.0 -->

### 1. Scope
<!-- section_id: CSP-16.1 -->

The aim of the Data Disposal and Retention Policy is to set out practices to be followed for ensuring the information that is supposed to be disposed of is not stolen or misused and maintained securely. This is applicable to all the [[applies_to:employees]] of Choice Equity Broking Pvt. Ltd. who have access to data.

### 2. Purpose
<!-- section_id: CSP-16.2 -->

The purpose of the policy is to ensure that data is handled in a manner that the confidentiality, integrity, and availability of the data are not compromised. It also ensures that data is adequately protected and maintained and to ensure that data that is no longer needed or has no value is destroyed at the appropriate time.

### 3. Procedure
<!-- section_id: CSP-16.3 -->

**Data**
: Information created, received, and maintained as evidence and information by any individual in the organization, in pursuance of legal/statutory/contractual obligations or in the transaction of business.

#### 3.1 Data Maintenance
<!-- section_id: CSP-16.3.1 -->

- Data shall be maintained for the client audits as a part of compliance requirement and deemed necessary by virtue of a legal or a statutory requirement.
- Data shall be maintained in a protective environment, safeguarding them against deterioration, damage by environmental or deliberate threats.
- Electronic storage media shall be ensured for the ability to read data throughout the retention period and safeguarded against loss of readability due to technology change.
- Choice Equity Broking Pvt. Ltd. shall establish and maintain procedures for identifying, maintaining, retaining, and disposal of data.
- Data should be kept securely and made available to authorized persons when required.

#### 3.2 Data Retention Period
<!-- section_id: CSP-16.3.2 -->

- For customer-specific application data, the retention period will be defined in the Choice Equity Broking Pvt. Ltd. applications and share drives as a part of client SLA.
- For Choice Equity Broking Pvt. Ltd. owned data, the length of the retention period is based on the likelihood that the evidence will be needed at some point in the future.
- Evidences and Audit Reports that will serve no further purpose (as determined by the length of their retention period) will be destroyed. As in documents, records which are in soft copy format, shall be reviewed and deleted post authorization.

#### 3.3 Data Disposal
<!-- section_id: CSP-16.3.3 -->

- Choice Equity Broking Pvt. Ltd. shall identify data to be disposed.
- Data shall be disposed in a protective environment and under the supervision of authorized person with prior approvals.

##### 3.3.1 Paper Records
<!-- section_id: CSP-16.3.3.1 -->

- Paper records to be disposed of are to be segregated from the paper documents that are going to be used.
- Employees of Choice Equity Broking Pvt. Ltd. must make sure that they don’t dispose of documents that are required.
- Wherever required, shredder or pulping method is to be used to shred/pulp the unwanted paper documents.

##### 3.3.2 Equipment
<!-- section_id: CSP-16.3.3.2 -->

- [[role:IT Department]] must ensure equipment productivity after its depreciation period. If the equipment is not functioning to meet the business requirements of Choice Equity Broking Pvt. Ltd., then the IT team of Choice Equity Broking Pvt. Ltd. can take a call to scrap/donate/sell the equipment.
- The equipment’s memory elements have to be damaged beyond repair and other parts can be disposed of by destroying them or sending them for recycling.
- In case of donating/selling the equipment, it has to be ensured that the memory elements of the equipment are formatted thoroughly and tested to see if data can still be retrieved.
- If it is possible to retrieve data, the equipment’s memory elements should be removed, and the rest of the equipment can be donated.

## 17.0 Malware Protection Policy
<!-- section_id: CSP-17.0 -->

### 1. Scope
<!-- section_id: CSP-17.1 -->

This policy applies to Choice Equity Broking Pvt. Ltd.’s information processing and communication facilities. It includes all [[applies_to:employees]] of Choice Equity Broking Pvt. Ltd. and third-party users who in any form use IT infrastructure of Choice Equity Broking Pvt. Ltd.

### 2. Purpose
<!-- section_id: CSP-17.2 -->

The purpose of this policy is to provide the directions for enforcement of procedural and prevention of Virus Attacks related security controls in the day-to-day working across software platforms of Choice Equity Broking Pvt. Ltd.

- The purpose of the anti-virus policy is divided into the following ways:
  - To prevent unexpected and unauthorized access attempted on Choice Equity Broking Pvt. Ltd. IT infrastructure which are external threats.
  - To ensure customers’ and organization’s information assets like data, computer application systems, and IT equipment are adequately and consistently protected from unauthorized use or access, data damage, inappropriate data alteration, or data loss. The level of protection should be commensurate to the level of information services required by the company to conduct its business.
  - To strive for minimum downtime thus make information and information systems available to authorized users as per the business needs to promote Choice Equity Broking Pvt. Ltd.’s IT Security mission.
  - To meet all audit requirements pertaining to information collection, storage, processing, transmittal, and disclosure that are applicable to the company.
  - To create within the company a level of awareness on information security as part of the day-to-day operations of the company and to ensure that all employees understand their responsibilities for maintaining information security.
  - To establish detailed information security processes based on this policy and ensure compliance against such processes.

### 3. Policy Statement
<!-- section_id: CSP-17.3 -->

This policy states security awareness, prevention, and detection controls should be utilized to protect information systems and services against malicious software.

### 4. Procedure
<!-- section_id: CSP-17.4 -->

#### General Clauses
<!-- section_id: CSP-17.4.1 -->

- All Choice Equity Broking Pvt. Ltd. Laptops and Desktops must have Choice Equity Broking Pvt. Ltd.'s standard, supported anti-virus software installed and scheduled to run at regular intervals.
- Choice Equity Broking Pvt. Ltd.’s in-house Antivirus server is in sync with the global server that allows automatic update of file at Choice Equity Broking Pvt. Ltd. end.
- Virus-infected computers must be removed from the network until they are verified as virus-free.
- Any activity with the intention to create and/or distribute malicious programs into Choice Equity Broking Pvt. Ltd.'s networks (e.g., viruses, worms, Trojan horses, e-mail bombs, etc.) is prohibited.

#### Antivirus Management (Users)
<!-- section_id: CSP-17.4.2 -->

- Choice Equity Broking Pvt. Ltd.’s systems must have Antivirus software installed and enabled at all times.
- The systems facing internet should have antivirus software installed. Automatic updates are to be scheduled to ensure maximum protection against malicious software.
- Scanning the physical storage media and external storage devices should be done automatically or are to be scheduled such that Choice Equity Broking Pvt. Ltd. business or user’s performance is not affected.
- Reports should be generated and reviewed periodically to ensure correct working of the antivirus software and analyze Choice Equity Broking Pvt. Ltd.’s security posture against various malware threats.

#### Control against Malicious Software
<!-- section_id: CSP-17.4.3 -->

Unless proper control precautions are taken, information systems are vulnerable to the introduction of malicious software such as computer viruses, network worms, Trojan horses, logic bombs, and spyware/adware code. Protection from malicious software shall be based on awareness, and system access controls, such as the following:

- All antivirus software on servers, desktops, and laptops should be configured to protect the system on a real-time basis (Each file accessed should be first scanned by antivirus software). Users should not be allowed to change these settings.
- Users should be made aware through mail about the new virus outbreaks and necessary precautions to be taken.
- Users should be made aware of the precautions to take and to operate antivirus software.
```
