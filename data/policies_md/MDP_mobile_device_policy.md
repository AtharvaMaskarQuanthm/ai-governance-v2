```yaml
---
document_id: "MDP"
title: "Mobile Device Policy"
filename: "Choice-ISMS-mobiledevice-POLICY.pdf"
version: "2.1"
status: "approved"
created_date: "2016-10-17"
effective_date: null
last_reviewed: "2024-01-31"
next_review: null

owner:
  name: "Ashutosh Bhardwaj"
  role: "Reviewer"

prepared_by:
  - name: "Mahesh Tamhankar"
    role: "Preparer"

approved_by:
  - name: "Ashutosh Bhardwaj"
    role: "Approver"
    date: "2024-01-31"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
  - id: "SEBI-CSCRF"
    name: "SEBI CSCRF"

references:
  - document_id: "BYOD"
    title: "Bring Your Own Device Policy"
    relationship: "related"

scope:
  description: "Guidelines for usage of Choice supported mobile devices for corporate services"
  inclusions:
    - "Corporate or personally owned (BYOD) mobile devices"
  exclusions:
    - "Devices not listed in the scope"

entities:
  roles:
    - "Technology Mobility team"
    - "HR"
    - "BU CTO"
    - "BU Compliance Team"
    - "BU COO"
  controls:
    - "MDM"
    - "MAM"
  assets:
    - "Mobile devices"
    - "Apple devices"
  processes:
    - "Device provisioning"
    - "Device configuring"
    - "Incident reporting"
  external_parties:
    - "Apple"
    - "Samsung"

tags:
  - "mobile"
  - "device management"
  - "security"
---
# Mobile Device Policy

## 1.0 Purpose
<!-- section_id: MDP-1.0 -->
Choice Equity Securities Pvt. Ltd. and its subsidiaries, associates, and entities in India and overseas (collectively referred to as ‘Choice’). The policy aims at providing guidelines to authorized users on usage of Choice supported Mobile devices for permitted corporate services.

## 2.0 Scope
<!-- section_id: MDP-2.0 -->
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

**[MANDATORY]** Above services shall only be provisioned via [[control:MDM]] (Mobile Device Management)/ [[control:MAM]] (Mobile Application Management). MDM/ MAM is security software that helps administer mobile device and protects corporate services/data published over mobile device with below controls:
- Protection against Jailbroken/Rooted device – MDM/ MAM detect and restrict installation of corporate application on rooted or jailbroken devices.
- Protection against unauthorized access - In case where a user does not implement screen lock, MDM/ MAM can use a policy in order to prevent data theft or unauthorized application usage.
- The corporate data is not accessible outside the MDM/ MAM container. It protects the data stored in the devices by access control policies
- Current/Updated app on all endpoints – Reduces pain of IT & user on installing updated app. Ensure all the endpoints with current/updated app.
- Data wipe – For resigned/unwanted employees or stolen devices.

## 3.0 Definitions
<!-- section_id: MDP-3.0 -->

**Personal Device**
: Device purchased and owned by an employee which can be used to deploy corporate mobile services.

**Corporate service device**
: A mobile device on which the corporate services are deployed.

**MDM**
: Mobile Device Management

**MAM**
: Mobile Application Management

**Authorized software**
: Software required for basic functioning of the device

**Unauthorized software**
: Software not required for basic functioning of the device.

## 4.0 Policy for Corporate Devices
<!-- section_id: MDP-4.0 -->

### 4.1 Eligibility
<!-- section_id: MDP-4.1 -->
- **[MANDATORY]** For existing employees, user will be required to raise a Logit ticket for corporate mobile device
- **[RECOMMENDED]** For new joiners, corporate mobile device may be allocated based on Logit raised by [[role:HR]]

### 4.2 Device Provisioning
<!-- section_id: MDP-4.2 -->
- Users seeking corporate mobility service can avail the services on their personal device with appropriate versions of mobile device (as defined in scope – 2.0).
- **[MANDATORY]** The user’s device should meet the pre-requisites and should not be rooted or jailbroken.
- **[MANDATORY]** A user can only have one device configured under this policy.

### 4.3 Device Configuring
<!-- section_id: MDP-4.3 -->
- **Corporate Devices**
  - [[role:Technology Mobility team]] shall be responsible for configuring of corporate devices to eligible users.
  - Procurement/ Purchase/ Asset team hands over the corporate device to [[role:Technology Mobility team]]
  - [[role:Technology Mobility team]] configures the device as per corporate policy and hands over the device to user.
- **Personal Devices**
  - Users are required to download the company portal application and register the device with O365
  - Users are expected to complete the configuration process by following on-screen instructions
  - **[MANDATORY]** User shall backup the data prior configuration. [[role:Technology Mobility team]] will not be responsible for any data loss that happens during the configuration of corporate mobile services.

### 4.4 Pre-requisites
<!-- section_id: MDP-4.4 -->
- For personal device, please refer Section 2.0.
- **[MANDATORY]** Data services must be available on the device to allow [[role:Technology Mobility team]] to provision the corporate services.

### 4.5 Responsibilities
<!-- section_id: MDP-4.5 -->
- [[role:Technology Mobility team]] shall be responsible for providing support for authorized corporate service devices only
- [[role:Technology Mobility team]] shall not be responsible for the accessories, service fees or charges incurred due to personal use of company-provided equipment or services, and any other related billing costs
- **[MANDATORY]** User shall be responsible and accountable for storing any personal or company’s sensitive, proprietary or confidential information on the device under this policy.
- **[MANDATORY]** User shall be responsible for physical safeguarding of the mobile device.

### 4.6 Appropriate usage policy for corporate service device
<!-- section_id: MDP-4.6 -->
- **[MANDATORY]** The user shall not use this mobile device for business activities that mandate certain safeguard/protocol to be followed in accordance with prevailing laws including but not limited to, call recording, logging, monitoring etc.
- **[MANDATORY]** User shall refrain from malicious downloads and storage on this device
- **[MANDATORY]** Users shall not install any unauthorized software (i.e hacking, cracking etc.) on the devices under this policy
- **[MANDATORY]** Users shall not leave the devices unattended anytime
- **[MANDATORY]** Users shall not share the device passwords with anyone
- **[MANDATORY]** When travelling devices would be kept within close view and shall not be left unattended at any point in time to avoid theft.
- **[MANDATORY]** In the event, if the device (company provided or personal) is lost or stolen, users are required to report the incident to [[role:Technology Mobility team]] immediately. These actions shall ensure that appropriate steps are taken to remotely wipe information residing on the device.
- **[MANDATORY]** The user shall not be allowed to create backup of the data on an unauthorized device.
- **[MANDATORY]** In case of violation, corporate services will be discontinued by the [[role:Technology Mobility team]] without any prior notice to the user.

### 4.7 Support Service Levels
<!-- section_id: MDP-4.7 -->
- For corporate service mobile devices, [[role:Technology Mobility team]] would be responsible for supporting corporate applications/services only.

### 4.8 Exit User
<!-- section_id: MDP-4.8 -->
- In cases where the user exits through the resignation or termination process, [[role:Technology Mobility team]] would remotely remove/wipe the [[control:MDM]] container. This activity would not impact the user’s personal data stored anywhere outside the [[control:MDM]] container.
- For all the Apple devices, it is mandatory for the users to support the [[role:Technology Mobility team]] to delete their Apple ID/Profile so that the devices can be used / accessible by the [[role:Technology Mobility team]].

### 4.9 Violation
<!-- section_id: MDP-4.9 -->
- **[MANDATORY]** Any Violation of the policy, or any of its tenets, could result in disciplinary action which may even lead to and include termination of employment and civil and/or criminal prosecution under local, state and federal laws.

## 5.0 Exceptions
<!-- section_id: MDP-5.0 -->
- **[RECOMMENDED]** Exceptions shall not be universal but shall be agreed on a case-by-case basis, upon official request made by the information owner. These may arise, for example, because of local circumstances, conditions or legal reason existing at any point of time.
- All exceptions during implementation shall be submitted by the concerned person responsible for implementation. These shall be submitted through the Exception Form and sign-off on the same shall be maintained as per the below grid.

| Action   | High/Medium                                   | Low   |
|----------|-----------------------------------------------|-------|
| Reviewer | Level 1 - [[role:BU CTO]]<br>Level 2 - [[role:BU Compliance Team]] | [[role:BU CTO]] |
| Approver | [[role:BU COO]]                               |       |
```