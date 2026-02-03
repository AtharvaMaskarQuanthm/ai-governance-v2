```yaml
---
document_id: "BCP"
title: "Business Continuity Policy"
filename: "Choice-ISMS-Business Continuity Policy.pdf"
version: "2.3"
status: "approved"
created_date: "2016-10-17"
effective_date: "2025-04-07"
last_reviewed: "2025-04-07"
next_review: null

owner:
  name: "CTO"
  role: "Chief Technology Officer"

prepared_by:
  - name: "Abhishek Vinayak"
    role: "Associate"

approved_by:
  - name: "Ashutosh Bhardwaj"
    role: "CISO"
    date: "2025-04-07"

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
  - document_id: "IMP"
    title: "Incident Management Policy"
    relationship: "related"

scope:
  description: "Applies to critical business processes and IT infrastructure"
  inclusions:
    - "Trading & Risk Management Operations"
  exclusions:
    - "Special situations like simultaneous breakdown of all vital services citywide"

entities:
  roles:
    - "CISO"
    - "CTO"
    - "Business Continuity Manager"
    - "Emergency Response Team Head"
  controls:
    - "2 factor authentication"
    - "VPN"
  assets:
    - "Servers"
    - "Databases"
    - "NTT Mumbai"
    - "SIFY Hyderabad"
  processes:
    - "Incident Management"
    - "Disaster Recovery"
    - "Business Continuity Management"
  external_parties:
    - "Media"
    - "Government Agencies"

tags:
  - "business continuity"
  - "disaster recovery"
  - "information security"
---
## 1. Policy
<!-- section_id: BCP-1.0 -->

Choice Equity Broking Pvt. Ltd’s management is committed to deliver continual service to its clients and adherence to stakeholders expectations including regulatory and legal requirements. Towards this, Choice Equity Broking Pvt. Ltd (CHOICE) **[MANDATORY]** shall implement business continuity capabilities and test them periodically. This will be monitored to ensure compliance with relevant regulatory and legal mandates.

Choice Equity Broking Pvt. Ltd (CHOICE) **[MANDATORY]** shall take all reasonable steps to ensure that in the event of a service interruption or a disaster – (1) employees and other concerned personnel are safe, (2) reputation, regulatory, financial and operational impact is minimized. In any eventuality, it is CHOICE policy to have in place robust Business Continuity Capability that is regularly updated to match business requirements.

To help operations management in the creation of adequate business continuity and service recovery plans, CHOICE’s management **[MANDATORY]** shall approve allocation of resources (including manpower), budget and external expertise (if required) to support and achieve business continuity objectives.

In order to ensure that Business Continuity Plan (Business Continuity Plan) remains effective and usable at all times, CHOICE’s Management **[MANDATORY]** shall constitute an effective business continuity plan, comprising a team of executives, processes and monitoring measures. This plan will ensure that business continuity requirements are fulfilled in all existing businesses and new programs. The team of executives drawn from business and technology teams across all of CHOICE’s Line of Businesses (Business Function) will be jointly responsible for implementation and maintenance of business continuity requirements.

As a general guide, Business Continuity Plan measures **[RECOMMENDED]** shall aim to minimize the effects of a number of potentially disruptive events, including but not restricted to:
- Natural Disasters such as Tsunami or Earthquakes Pandemic
- Socio-political events such as terrorist attacks, riots or strikes
- Local disasters such as fires, flooding, explosions or water leakages
- Loss of support utilities such as telecommunications breakdowns or power failures
- Information technology related outages such as Server, Application or Network failures
- Cyber Security incidents such ransomware attacks, malware attacks, website defacement

This document sets out the general principles and processes for the creation and revision of the business continuity plan for CHOICE. This policy and all its related documentation **[MANDATORY]** shall be reviewed at least on half yearly basis, after the occurrence of any disaster or whenever there is a significant change to CHOICE’s business or technology environment that may warrant a corresponding change to the Business Continuity Plan of the organization.

The objective is to enable CHOICE to ensure that the acceptable levels of service to its business units are maintained, regardless of impact to the infrastructure and information processing facilities.

The [[role:CTO]] is the designated owner of the Business Continuity Plan and shall be assisted in its maintenance by the Business Continuity Management Team.

## 2. Scope
<!-- section_id: BCP-2.0 -->

This policy applies to critical business processes and IT infrastructure and ICT devices for the following lines of businesses of CHOICE:
- Trading & Risk Management Operations

The following supporting functions will also be taken into account with respect to their interactions with the lines of businesses listed above:
- Information Technology (IT)

### 2.1 Assumptions
<!-- section_id: BCP-2.1 -->

The key assumptions, which have been considered while preparing this business continuity plan, are:
- Overall losses, in many cases may be far greater in the event of actual disaster. It should be noted that due to the inherent limitations of a risk assessment exercise, it is never possible to quantify the full impact of such a scenario. Therefore, intangible losses shall be considered while assessing the impact. However, the intangible impacts shall not be a part of the financial impact calculations.
- Third party services used by the organization shall be available for assistance during recovery operations as governed by their respective SLA with CHOICE.
- There are innumerable disaster scenarios that CHOICE could be confronted with. After careful analysis, CHOICE Management has decided to formulate its Business Continuity Plan to counter various disaster categories rather than each individual disaster scenario in order to provide breadth to the Business Continuity Plan service offerings.
- However, Business Continuity Plan shall not provide for special situations that may occur, such as, simultaneous breakdown of all vital services citywide including telecom/power/utilities infrastructure, flooding, fires, war, earthquake impacting both sites (Primary and DR site) at the same time etc. Any decisions for situations not covered in this plan will be made by the senior management as part of [[process:incident management]].

Specifically, the Business Continuity Plan assumes:
- Key personnel and/or their designated substitutes identified in the plan will be available in the event of a disaster.
- Support staff with skills will be available for recovery. Without relevant people, functional recovery is not possible.
- IT, Logistical and Infrastructure facilities will be available, which can facilitate specific recovery activities.
- During a disaster, the company may operate in two shifts (including Sundays) at the recovery location.
- Risk assessment will be a continual exercise to identify and manage disruption risks proactively.
- The recovery teams are aware of their roles and responsibilities in executing the plan.

### 2.2 Approach
<!-- section_id: BCP-2.2 -->

CHOICE has adopted the following phased approach to Business Continuity Management plan:

### 2.3 Terminology
<!-- section_id: BCP-2.3 -->

The following terminology has been used in this document to reference key Business Continuity Plan elements:
- **Interested Parties**: All people and entities who are from and are involved in the normal commercial operations of CHOICE, including customers, employees, contractors, service providers, and liability managers such as insurance companies.
- **Primary Data Center**: The current location of the IT systems required to carry out the Critical Business Processes (CBP).
- **Disaster**: Disaster is an event that drastically reduces the ability to provide critical data processing services.
- **Disaster Recovery Center**: The location where the required IT Systems have been replicated.
- **Primary Site**: The current site where CBP are being carried out.
- **Recovery Site**: A location far from the primary site where personnel may be relocated to carry out CBP.
- **IT Recovery Team**: IT Operations Team at all locations.
- **Administrative Recovery Team**: Administrative Operations Team at all locations.
- **Central Business Continuity Plan Coordinators**: A small set of people who have complete understanding of Business Continuity Plan for Choice Equity Broking Pvt. Ltd (CHOICE) and have been involved in implementation and maintenance of Business Continuity Plan at Choice Equity Broking Pvt. Ltd (CHOICE) level.

> [!CROSS-REF]
> Please refer to Annexure 9.1 for the list of business processes and their primary, recovery sites and disaster recovery locations.

## 3. Choice Equity Broking Pvt. Ltd (CHOICE) Business Continuity Management Strategy
<!-- section_id: BCP-3.0 -->

### 3.1 Business Continuity Strategy
<!-- section_id: BCP-3.1 -->

After careful evaluation of risk assessment and impact analysis of various scenarios to CHOICE Critical Business Process (CBP), the management has decided to employ the following strategies to recover its CBP to meet their individual Recovery Time Objective (RTO) and Recovery Point Objective (RPO) criteria. The RTO and RPO has been defined for incidents as per [[doc:incident-management-policy]]. Business Continuity Plan strategies shall differ based on the actual timing of the disaster – based on whether the disaster occurs during critical or non-critical times.

1. If the incident is not resolved within 30 minutes, the incident will be declared as a disaster and Business Continuity Plan will be invoked to restore business operations from the DR Site.

2. Switching Telecom and Data Network Links to the Disaster Recovery Location in those events when the servers and computing equipment in the Main Data Center or availability zone are unavailable for normal operations, due to a failure or outage. However, if the Primary Site and its network connectivity are available Business Operations teams shall continue to work from their regular office facilities.

3. Relocating the Functional Teams to a business continuity center in the event of the Primary office being unavailable for operations. The Supporting Business Function Coordinators shall ensure that the business teams are able to connect to the Main Data Center servers/ Disaster Recovery Location servers and resume normal job functions.

### 3.2 Disaster Categories
<!-- section_id: BCP-3.2 -->

CHOICE has defined the following disaster categories based on the extent of impact on operations.

| Category                                           | Description                                        |
|---------------------------------------------------|---------------------------------------------------|
| Disaster Category I (DC I CT) during Critical Times | An event which affects the Main Data Center, however, does not affect the Primary Site during Critical Times |
| Disaster Category II during Non Critical Times (DC I NCT) | An event which affects the Main Data Center, however, does not affect the Primary Site during Non-Critical Times |
| Disaster Category II during Critical Times (DC II CT) | An event which affects the Main Data Center and the Primary Site during Critical Times |
| Disaster Category III during Non Critical Times (DC II NCT) | An event which affects the Main Data Center, Primary Site and the during Non-Critical Times |
| Disaster Category III during Critical Times (DC III CT) | An event which affects the Main Data Center, Primary Site and the Recovery Site during Critical Times |
| Disaster Category III during Non Critical Times (DC III NCT) | An event which affects the Main Data Center, Primary Site and the Recovery Site during Non-Critical Times |
| Disaster Category IV (DC IV) | City Level Disaster |

### 3.3 Continuation of Information Security requirement in case of disaster scenarios
<!-- section_id: BCP-3.3 -->

- In case of “Work from Home”, management **[MANDATORY]** should agree to the work from home option and usages of CHOICE remote network access controls ([[control:2 factor authentication]], secured communication channel using [[control:VPN]]) shall be mandatory to ensure adherence to Information Security Controls.

## 4. Choice Equity Broking Pvt. Ltd (CHOICE) Business Continuity Management Organization Structure
<!-- section_id: BCP-4.0 -->

The organizational backbone of business continuity planning at CHOICE is the Business Continuity Management Team. In the event of a disaster affecting CHOICE or its resources, the Business Continuity Management Team will respond in accordance with this framework and will initiate specific actions for recovery. The Business Continuity Management Team is called into action under the authority of the designated Senior management who has the responsibility for approving actions regarding Business Continuity Planning at CHOICE. The organizational structure of the Business Continuity Management Team is depicted below:

ERT : Emergency Response Team SRT : Salvage and Response Team IRT/CMT : Incident Response Team/ Crisis Management Team

The formulation of Business Continuity Management Teams needs to be built with following considerations:
- Skills / Knowledge possessed by the Team Members
- Training on Contingency Plan purpose
- Training on various procedures for executing the recovery plan. There shall be at least two people identified for each role required, so as to take care of the unavailability of a critical person.

### 4.1 Roles and Responsibilities
<!-- section_id: BCP-4.1 -->

#### Business Continuity Management Head (Business Continuity Manager)
<!-- section_id: BCP-4.1.1 -->

Business Continuity Management head will have the overall responsibility for implementing the Business Continuity Framework by performing the following activities:
- Spearheading Business Continuity Management Team, strategizing, reviewing and implementing Business Continuity Plan Framework and Business Continuity Plan requirements along with Business Continuity Management Core Team
- Responsible for overall health check of the Business Continuity Management plan implementation and upkeep, along with the Business Continuity Management Team (includes planning, documentation, awareness, maintenance, tests, etc.)
- Providing budgetary approval for Business Continuity Plan implementation as well as approving expenses incurred during and after a disaster
- Declaration of the disaster and disaster category (with inputs from the Business Continuity Management Core Team and Business Continuity Management Coordinators)
- The declaration of disaster will be reported in the preliminary report submitted to the Exchange, as specified in [[process:incident management]] procedure
- Chairing calls with Business heads during emergencies to understand business criticality and planning for business continuity during Business Continuity Plan scenarios
- Emergency Response Coordination including overseeing communication management to all stakeholders
- Providing decision making support to Business Continuity Management Coordinator
- Monitoring the recovery process
- Providing sign-off post event, that recovery procedures were followed and RPO, RTO was achieved

#### Business Continuity Management Team
<!-- section_id: BCP-4.1.2 -->

Business Continuity Management Team is responsible for implementation of the Business Continuity Plan by performing the following activities:
- Strategy, Administration, Maintenance and Testing of Business Continuity Plan
- Central Point of Contact for all Business Continuity Plan needs
- Responsible for coordination with all Business Continuity Plan Teams
- Ensuring that the recovery site profiles (that include facilities, resources and equipment to be used during a disaster) are up-to-date through periodic audits of infrastructure
- Ensure DR drills conducted on a periodic basis not exceeding half yearly basis. Also, Fire drills are conducted at the primary site at the defined intervals
- Declaration of the disaster in absence of, or on behalf of, the Business Continuity Management Head
- Communication and updating the on-ground situation to the Business Continuity Management Head on a regular basis and have all alternate means of communication including channel for communication for communicating with the clients in case of any disruption. All such communication shall be completed within 30 minutes from the time of disruption
- Recovery Teams Coordination
- Confirmation of completion of Business Continuity Plan activities
- Monitoring the recovery process and communicating the same to Business Continuity Management Head
- Documenting the learning from crisis incidents

#### Crisis Management Team / Incident Response Team
<!-- section_id: BCP-4.1.3 -->

Crisis Management Team is responsible for coordinating with the Emergency Response Team (ERT) for exit, Admin for logistics & accommodation, IT for Business Continuity Plan site readiness, HR for counseling, Salvage and Recovery team for primary site readiness. CMT Team is also responsible for assisting the Business Continuity Management Head during the Disaster by performing the following activities:
- Coordinate with Emergency Response Team Head to ensure effective response to emergency situations
- Coordinate with Business Continuity Management Coordinators and Business Continuity Management Team to arrange for logistics to travel to the Business Continuity Plan site and, food & accommodation at the Business Continuity Plan site
- Ensure all IT infrastructure requirements are provisioned at the Business Continuity Plan site
- Effectively managing Public relations and Media Communication to relevant Marketing and Communication personnel and Business Continuity Management Head without making any comments
- Activating the management succession plans if necessary after due consultation with the Human Resources Department and the Senior Management
- Coordinate with the Salvage & Recovery Team to ensure seamless resumption of business delivery from the primary site once the primary site is fully operational
- Update the Business Continuity Management Team with the status on Business Continuity Plan situation
- Cater to all requirements during Business Continuity Mode of Operations
- Ensuring critical applications required by Salvage & Recovery Team are made available
- Obtaining the Damage Assessment report from the Business Continuity Management head in case of a disaster
- Obtaining and Reviewing incident reports to analyze the impact of such incidents and review the adequacy of the existing Business Continuity Plan framework to meet RTO and RPO

#### Emergency Response Team
<!-- section_id: BCP-4.1.4 -->

Emergency Response Team is responsible for coordinating safe exit of employees at the affected site, managing casualties and other emergencies along with assisting the Business Continuity Management Head during the Disaster by performing the following activities:
- Execution of emergency response
- Facilitating speedy evacuation of affected personnel
- Ensuring the Safety and Security of personnel
- Organization of Medical Assistance if required
- Liaising with Senior Personnel of Public Authorities and Agencies to ensure rapid relief operations
- Coordination with CMT
- Reporting completion of Emergency Response Activities to the Emergency Response Team Head

#### Emergency Response Team Head
<!-- section_id: BCP-4.1.5 -->

Emergency Response Team Head is responsible for assisting the Business Continuity Management Team during the Disaster by performing the following activities:
- Ensuring the Safety and Security of personnel
- Ensuring adequate guidance is provided to the ERT members for safe evacuation
- Ensuring usage of PA system for communication during emergencies
- Ensuring no panic situation is created during evacuation
- Timely coordination with External Emergency Response service for assistance, where needed
- Liaising with Senior Personnel of Public Authorities and Agencies to ensure rapid relief operations
- Coordination and status update to CMT
- Ensuring personnel roll call at the assembly point
- Reporting completion of Emergency Response Activities to CMT / Business Continuity Management Team

#### Salvage & Recovery Team
<!-- section_id: BCP-4.1.6 -->

Salvage & Recovery Team is responsible for salvage and assessment of the damage, and recovery of the primary site along with assisting the Business Continuity Management Head during the Disaster by performing the following activities:
- Visiting the affected facility prior to the arrival of media, public services, or authorized visitors
- Damage Assessment on the ground and submission of the Damage Assessment Report to the Business Continuity Management Team / Crisis Management Team
- Ensuring all Public relations and Media Communication to relevant Marketing and Communication and Business Continuity Management Head without making any comments
- Activating the management succession plans if necessary after due consultation with the Human Resources Department and the Senior Management
- Notifying the governing regulatory bodies about the nature and gravity of the disaster
- Notifying the internal and external stakeholders about the nature and gravity of the disaster salvage
- Instructing the Administration team to notify the external agencies such as nearest post office / courier companies for delivering and collection of mail at recovery site in the event of relocation due to disaster
- As a post Business Continuity Plan activity, once the site is restored, before BAU is achieved ensure testing of connectivity, restoration of backup, testing critical applications
- Maintaining adequate level of IT infrastructure as per the resource requirements at Recovery Site/DR Site
- Restoring network to normalcy at all locations
- Restoration of the required critical applications and infrastructure at the primary site
- Allowing network users access to networked services at all locations
- Connecting network to other external systems
- Obtaining necessary office supplies and workspace
- Obtaining and installing necessary hardware components
- Obtaining and loading backup media
- Obtaining Backup media to be obtained for applications from the Data Control Team
- Restoring critical operating system and application software
- Restoring system data
- Assessing the required OS recovery measures
- Execution of the steps based on the installation checklist
- Restoring Telecommunication facilities to normal working conditions
- Coordination with vendor for restoration of telecom links
- Providing necessary hardware/software support during the telecom restoration process
- Restoring Databases and applications based on available databases
- Maintaining documentation of the databases and their connectivity to other applications/databases
- Maintaining documentation of the applications connecting to the databases
- Restoration based on the installation checklists
- Troubleshooting and providing hardware/system level support for the database restoration process
- Obtaining authorization to access damaged facilities
- Restoring utilities back to normal operating conditions
- Maintaining proper documentation of the available infrastructure
- Vendor coordination (applicable for Admin, IT)
- Testing of fire equipment on periodic basis

## 5. Communication flow during a Crisis & Disaster
<!-- section_id: BCP-5.0 -->

Once Business Continuity Plan is invoked, the Incident communication protocol is considered to be automatically invoked. Please refer below table for communication plan.

| From                                               | To                                                 | Content                                            | Mode                                               |
|---------------------------------------------------|----------------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| Media / SOC / Customer Complaints / Govt. Alerts   | Crisis Management Team / Incident Response Team (CTO) | Initial incident alert or notification             | Monitoring tools, Email, Call, Escalation triggers |
| Communication to Crisis Management Team(CMT / IRT) | Business Continuity Management Head                | Incident summary, impact, BCP invoked, actions initiated | Email, Phone, SMS, Collaboration Tools             |
| Business Continuity Management Head                | Business Continuity Management Team                | Situation update, safety instructions, alternate work arrangements | Email, SMS, WhatsApp, Collaboration Tools          |
| Location Administration team / Business Continuity Management Team | Employee                                        | Service impact (if any), continuity measures, helpline/support contact | Email, Phone, SMS, WhatsApp, Website banner/notice |
| Business Continuity Management Team                | Stakeholders                                    | High-level business impact summary, action plan    | Email, SMS, WhatsApp                               |
| Business Function Manager / Business Managers      | All customers / front offices within 30 minutes | Official, verified statements; impact details; compliance references | Phone, Email (only if needed)                      |
| Marketing Head under guidance of Business Continuity Management Head | Media /Government Agencies                      | Official, verified statements; impact details; compliance references | Phone, Email (only if needed)                      |

## 6. Administration and Maintenance of the Business Continuity Plan
<!-- section_id: BCP-6.0 -->

Administration of the plan is the responsibility of the Business Continuity Management Coordinator, who will ensure that corporate standards and procedures are adhered to during the administration of plan.

As custodian and administrator of the Business Continuity plan, the Business Continuity Manager is required to have a thorough knowledge of the plan. As a further safeguard, the Alternative Recovery Coordinator will also be a participant in all recovery plan maintenance and testing activities.

Responsibility for maintaining the Business Continuity plan, which includes incorporating the changes and issuing the updates, rests with the Business Continuity Management Coordinator who will ensure compliance with the documented procedures for recovery plan administration.

### 6.1 Key Business Continuity Plan Maintenance Activities
<!-- section_id: BCP-6.1 -->

The objective of developing procedures for administration of the Business Continuity plan is to keep the plan updated by promptly processing the changes necessary for maintaining a workable Business Continuity plan.

Specific plan administration activities ensure that the plan is updated and include:
- Updating of the Business Continuity plan by the Business Continuity Manager
- Developing administrative procedures to control changes to the Business Continuity plan
- Providing the necessary standards and procedures, which ensure compliance with plan requirements
- Developing a training program to include all executive management, recovery teams, vendors, emergency services personnel and the end user community
- Instituting procedures for planning, developing, scheduling, and executing tests of the Business Continuity Plan including the evaluation of test results
- Assisting internal audit in the performance evaluation process, to ensure overall compliance with recovery plan
- Maintaining the Business Continuity Plan in electronic format for ease of maintenance

### 6.2 Business Continuity Plan Documentation Management
<!-- section_id: BCP-6.2 -->

#### 6.2.1 Document Classification
<!-- section_id: BCP-6.2.1 -->

The CHOICE Business Continuity Framework (business continuity plan) is an internal document as it contains proprietary and sensitive company information. For the purpose of having this framework, internal information is defined as the information that could have a significant adverse impact on CHOICE or its interested parties, if it’s available to unauthorized parties, such as malicious elements or competitors.

This document has been classified as internal and is for restricted distribution only, as it contains CHOICE strategy for recovery of critical business processes / IT systems in the event of a disaster, and names, addresses and telephone numbers of the key recovery team members. Therefore, the framework should be distributed on a need-to-know basis within the organization only.

Each party possessing a copy of the business continuity plan is responsible for security and control of the document in accordance with the policies for the protection of proprietary information.

The business continuity plan documentation shall be available for “Read-Only” access in an access-controlled environment.

#### 6.2.2 Change Management
<!-- section_id: BCP-6.2.2 -->

Following events may necessitate an evaluation of, and a possible change to, the business continuity plan documentation:
- An operational change within an existing business process which could impact the Recovery Time Objective and the Recovery Point Objective for that particular process
- Launch of a new service line or discontinuation of an existing service offering
- Introduction of a new application to the technology landscape of Choice
- A new office facility or relocation of an existing office location to a different site
- A change in the existing organization structure
- A change in technological infrastructure and resource requirements that affects critical business processes
- A change in the regulatory environment
- Change in the contact details of employees, vendors, emergency service providers
- A change to the Business Continuity strategy or recovery procedures as an outcome of Business Continuity Plan and DR test results
- Learning from the incident/ disaster or results of Business Continuity Plan tests

Heads of the business units as well as IT department heads are responsible for informing the Business Continuity Manager about a change in their respective operational processes. This is to ensure that the business continuity plan documentation remains current and is updated as and when there is a significant change to the operating environment of CHOICE.

Based on the respective change request inputs obtained from the business, the Business Continuity Manager shall ensure:
- Update the list of critical business processes, impact analysis sheets
- Ensure recovery location(s) are available and details are updated
- Review and update contact lists (employees, vendors, emergency service) and phone numbers
- Review and update Resource requirements after discussion with process owners
- Review recovery options and update as necessary after discussion and inputs from the process owners

#### 6.2.3 Review, Updating and Release
<!-- section_id: BCP-6.2.3 -->

The Business Continuity Management coordinators should proactively liaise with the Business units of CHOICE and identify and analyze whether any change has occurred to the operating environment of the respective business units and the impact of such changes to the business continuity plan. Based on analysis and discussion with business process owners, the Business Continuity Management coordinator should initiate change management procedures to update the relevant business continuity plan documentation such as impact analysis, resource requirements, and recovery procedures after consultation with respective process owners.

The Business Continuity Manager shall provide Management Information System (MIS) reports concerning status of Business Continuity Management (progress on IT Disaster Recovery implementation and testing, awareness training programs conducted, KPIs etc) within the organization.

CHOICE Management shall review, approve and release the updated version of the business continuity plan documentation to the concerned stakeholders after completion of required changes.

#### 6.2.4 Distribution
<!-- section_id: BCP-6.2.4 -->

The Business Continuity Manager is responsible for the authorized distribution of the business continuity plan. This is accomplished by developing a master distribution list on a need-to-know basis.

Copies of the plan and updates shall be provided to:
- The Business Continuity Manager
- Business Continuity Management Team
- Incident Management Team
- Emergency Response Team Head
- Emergency Response Team
- Salvage & Recovery Team

## 7. DR Drill
<!-- section_id: BCP-7.0 -->

Periodic review and updating of the business continuity plan will ensure that the information contained within the framework is current. The testing of the framework will determine:
- The state of readiness of the business to respond to and cope with a disaster involving the IT systems as well as facilities and services
- Whether all the services for Line of Business are adequate to support recovery
- Whether backup of data and documentation stored at offsite are adequate to support the recovery of IT systems
- Whether the defined tasks and procedures are adequate to support the recovery of business processes / IT systems within the given time frame
- Whether the business continuity plan has been properly maintained and updated to reflect the current status. The following tests should be carried out:
  - Remote testing
  - Full interruption test

### 7.1 Remote Testing
<!-- section_id: BCP-7.1 -->

Remote tests are exercises designed to assess the readiness and effectiveness of Business Continuity Plan setup at the recovery/ Business Continuity Plan site. Teams can login remotely to the Business Continuity Plan machines and perform the testing.

### 7.2 Full Interruption Test
<!-- section_id: BCP-7.2 -->

The full interruption test requires extensive planning and preparation and should not be performed until most, if not all, of the framework components have been tested. This test requires the simulated recovery of critical business application systems and communication components. It is the closest exercise to an actual disaster scenario. Although a full interruption test requires weeks of planning and considerable coordination of personnel and resources, the exercise provides the highest level of confidence about the ability to recover in an actual event.

### 7.3 Administration of Business Continuity Plan Testing
<!-- section_id: BCP-7.3 -->

Test schedule
The following table provides frequency for carrying out various types of tests in order to keep the Business Continuity plan current and maintain the efficiency of the recovery teams. The table below indicates the ideal frequency of testing the business continuity plan, however, based on the availability of business users to participate in the test, the Business Continuity Management coordinator shall amend the test timings after due consultation with the Business process owners.

| Type of tests          | Frequency of the test |            
|-----------------------|-----------------------|------------
|                       | Monthly               | Six monthly
| Full Interruption Test | NA                    | □          

Review of test results
The team will document test results as-soon-as possible, and share results with stakeholders. Observations encountered during the testing would be documented and followed up for closure.

## 8. Awareness, Education and Training
<!-- section_id: BCP-8.0 -->

Awareness of the need for maintaining a viable recovery capability is essential. This awareness will be achieved through formal education and training sessions that will be conducted on a regular basis.

The objective of the training is to:
- Ensure that all the personnel who are responsible for maintaining and executing the plan have necessary awareness and understanding of the Business Continuity procedures.
- Increase Business Continuity awareness for those personnel who are not directly involved in maintenance and/or execution.

Awareness workshops addressing the plan shall be scheduled on a regular basis. These workshops will include overview of the following:
- Recovery strategy, roles and responsibilities
- Recovery priorities and time-frames
- Business Continuity structure and contents
- Recovery plan administration, maintenance and testing

## 9. Annexure
<!-- section_id: BCP-9.0 -->

### 9.1 Business Processes with Primary, Business Continuity Plan & DR Site
<!-- section_id: BCP-9.1 -->

| S.No. | Business Function        | Primary Site | DR Site       |
|-------|--------------------------|--------------|---------------|
| 1     | Trading Services         | NTT Mumbai   | SIFY Hyderabad|
| 2     | Risk Management Services | NTT Mumbai   | SIFY Hyderabad|

Data center locations:

| Data Center 1 | Data center 2 |
|---------------|---------------|
| NTT Mumbai    | SIFY Hyderabad|

If the application is hosted on cloud, then the DR should be hosted on a different availability zone.

| Primary Data Center | Disaster Recovery Site |
|---------------------|------------------------|
| If AWS AZ 1         | AWS AZ 2               |
| Mumbai Region       | Hyderabad Region       |
```