```yaml
---
document_id: "IRM"
title: "IS Risk Management Methodology"
filename: "Choice_IS_Risk_Management_Procedure.pdf"
version: "1.1"
status: "approved"
created_date: "2024-08-24"
effective_date: "2024-09-01"
last_reviewed: "2025-01-28"
next_review: null

owner:
  name: "Ashutosh Bhardawaj"
  role: "CISO"

prepared_by:
  - name: "Shripad Mayekar"
    role: "GRC Consultant"

approved_by:
  - name: "Ashutosh Bhardawaj"
    role: "CISO"
    date: "2025-02-20"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"
  - id: "SEBI"
    name: "SEBI Act"

references:
  - document_id: "RMT"
    title: "Risk Management Template"
    relationship: "related"

scope:
  description: "Defines the methodology for identification, classification, treatment, and monitoring of information security risks."
  inclusions:
    - "Information assets"
    - "Information processing facilities"
  exclusions:
    - "Non-information security risks"

entities:
  roles:
    - "CISO"
    - "Information Security Manager"
  controls:
    - "Audit reports"
    - "Checklists"
  assets:
    - "Information systems"
    - "Trading platforms"
  processes:
    - "Risk Assessment"
    - "Risk Treatment"
  external_parties:
    - "Government"
    - "Industry"

tags:
  - "risk management"
  - "information security"
  - "ISO27001"
---
## 1. Introduction
<!-- section_id: IRM-1.0 -->

- It is essential for every organization to have a clearly defined, comprehensive, and repeatable risk management program. This document defines the methodology for identification, classification, treatment, and monitoring of information security risks at [[external:Choice]].
- This risk management methodology **[RECOMMENDED]** should be adopted and implemented while assessing, treating, and managing risks associated with the [[asset:information assets]] and [[asset:information processing facilities]] of [[external:Choice]].
- This methodology sets out a pro-active, semi-quantitative approach for systematically addressing the existing risks throughout the lifecycle of information and information processing facilities of [[external:Choice]].

## 2. Risk Management Methodology
<!-- section_id: IRM-2.0 -->

Risk Management methodology is a continual process that involves the following key steps:

1. Communication and consultation
2. Establishing the context
3. Risk Assessment
   - Risk Identification
   - Risk Analysis
   - Risk Evaluation
4. Risk Treatment
5. Risk Monitoring and review

This methodology **[MANDATORY]** should be followed to ensure that the [[external:Choice]] approach to risk management is both comprehensive and consistent. All steps of this methodology should be formally conducted across the entire organization on an annual basis or when significant changes are proposed or occur. Further, risk management would not solely be an annual process and should be performed at all times and in relation to all activities affecting information security. Therefore, everyone shall have a responsibility to continually apply this methodology when making business decisions and when conducting day-to-day management.

Based on the below risk matrix, risk would be assessed and treated:

| TYPE OF RISK   | RANGE OF RISK VALUES | ACCEPTABLE RISK VALUE |
|----------------|-----------------------|-----------------------|
| Residual Risk  | High (H)              | Low (L)               |
| Inherent Risk  | Medium (M)            |                       |
|                | Low (L)               |                       |

## 2.1 Communication and consultation
<!-- section_id: IRM-2.1 -->

[[external:Choice]] should communicate and consult with the internal and external stakeholders throughout the risk management lifecycle to ensure that the organization has a comprehensive picture of the existing risks and mitigation steps.

External communication and consultation is targeted at communicating the following with external stakeholders (including [[external:Government]] and [[external:Industry]]):

1. The organization’s risk management approach;
2. The effectiveness of risk management approach; and
3. Requesting feedback where appropriate.

Internal communication and consultation is aimed at communicating the following with internal stakeholders:

1. The risk management process;
2. Seeking feedback in relation to the process; and
3. Key risks and their responsibilities relating to management of the process.

## 2.2 Risk Criteria/Triggers
<!-- section_id: IRM-2.2 -->

Risk assessments will be initiated whenever specific criteria or triggers occur that indicate a potential threat to the organization’s operations, assets, or compliance obligations.

- **Changes in Business Strategy or Objectives**: Any significant changes to the organization’s strategic direction, new business initiatives, mergers, acquisitions, or expansion into new markets.
- **Organizational Change (Leadership or Structural)**: Change in key leadership (e.g., CEO, CFO, CIO), significant structural reorganizations, or departmental shifts.
- **Introduction of New Technology or Systems**: The organization is introducing new technologies (e.g., software, hardware, cloud services) or systems (e.g., new trading platforms, ERP systems, or customer relationship management systems).
- **Regulatory or Legal Changes**: New or updated laws, regulations, or compliance standards (e.g., IT Act, [[external:SEBI]] Act, financial regulations, cybersecurity frameworks).
- **Audit Findings or Internal Controls Weaknesses**: Identified major weaknesses, deficiencies, or major non-compliance issues during internal audits, external audits, or self-assessments.

## 2.3 Risk Assessment
<!-- section_id: IRM-2.3 -->

Risk assessment is a careful examination of risks, its cause, probability of risk occurrence, and impact which may affect, cause loss or damage to information and information systems managed by [[external:Choice]]. Risk Assessment shall be performed in accordance with the defined Scope in ISMS.

Risk assessment involves:

1. Risk Identification
2. Risk Analysis
3. Risk Evaluation

### 2.3.1 Risk Identification
<!-- section_id: IRM-2.3.1 -->

Risk identification is a key step in the risk assessment process to ensure a complete list of risks is identified.

1. [[external:Choice]] should identify risk sources, areas of impact, causes, and possible consequences to form a comprehensive list of risks based on events that might create, enhance, prevent, degrade, accelerate, or delay the achievement of an organization's objectives. Comprehensive identification of risks is critical because risks that are not identified at this stage would not be included in further analysis. Risks can be identified using various tools and techniques including, but not limited to the following:
   - Audit reports
   - Checklists
   - Strategic and business plans
   - Structured interviews
   - Surveys and questionnaires
   - Self-observations and experiences
   - Project plans
   - Architectures

2. Risk identification step should capture the following:

| Risk Identification |                            |                                                  |                                       |                       |                         |                                                    |                                     |                                                    |
|---------------------|----------------------------|--------------------------------------------------|---------------------------------------|-----------------------|-------------------------|----------------------------------------------------|-------------------------------------|----------------------------------------------------|
| SR No               | Risk                       | Cause                                            | Risk Context                          | Location              | Department              | Asset                                              | Risk Category                      | Risk Owner                                         |
| #No                 | Enter the Identified Risk  | Describe the potential causes of event occurring | Identify the type of the Risk Context | Name of the Location  | Name of the Department  | Identify the Assets relevant to the risk identified | Identify the relevant risk category | [[external:CHOICE INDUSTRIES LTD]] (Risk Owner for each identified risk) |

- Enter the identified risk – Document the risks after considering the external and internal factors along with the help of various tools and techniques;
- Identification of potential causes – Determine the causes that could lead to risks.
- Identification of risk content – Internal / External factor;
- Affected locations – e.g., Choice Head Office, Hyderabad, etc.
- Affected assets – Affected assets should be categorized as Physical / Software / Information / Document / Service / People;
- Categorizing the risk – Risk should be categorized based on their nature: Business Continuity / Infrastructure Assets & Systems / Environmental / Financial / Reputation / Operational / Compliance
- Owner of the risk – Based on the locations and responsibilities, risk owner(s)

### 2.3.2 Risk Analysis
<!-- section_id: IRM-2.3.2 -->

Risk analysis involves identifying and assessing the effectiveness of the existing controls (automatic/manual) to manage the risk, by either reducing the consequence or likelihood of the risk.

Risk analysis step should capture the following details:

| Risk Analysis                      |                    |            |       |
|------------------------------------|--------------------|------------|-------|
| Existing Control / Current Measure | Control Assessment | Likelihood | Impact|

- List of existing controls: The existing controls should be captured against all in-scope business processes that are currently being protected against the identified risks.
- Effectiveness of the existing control: On application of existing controls, the effectiveness of the existing controls should be evaluated based on its performance – Effective / Adequate / Marginal / Deficient. Existing controls can be evaluated through several different processes including:
  - Control self-assessment;
  - Internal Audit reviewing the effectiveness of controls; and
  - External Audit reviewing the effectiveness of controls.

- The definition for the effectiveness value is as follows:

| Control Assessment                                 |                                                    |                                                    |                                                    |
|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| Any action or activity that the firm has in place  |                                                    |                                                    |                                                    |
| RATING                                             | Design                                             | Performance                                        | Description                                        |
| Effective                                          | Designed to reduce risk entirely                   | Control is always applied as intended              | The design and the performance of the controls are considered sufficient |
| Adequate                                           | Designed to reduce most aspects of risk            | Control is generally operational but on occasions  | Minor weaknesses exist in the design or in the performance of the control |
| Marginal                                           | Designed to reduce some area of risk               | Control is sometimes applied correctly             | Deficiencies exist in risk mitigation / controls   |
| Deficient                                          | Very limited or badly designed, even where used co | Control is not applied or applied incorrectly      | Limited controls and/or management activities are in place, high level of risk remains. |

- Likelihood of the risk: Based on the existing control, assess the probability of risk event occurring as Frequent / Possible / Rare. The definition of the likelihood ratings is as follows:

| Likelihood                         |                                       |
|------------------------------------|---------------------------------------|
| The probability of risk occurring: |                                       |
| RATING                             | POTENTIAL FOR RISK TO OCCUR           |
| Frequent                           | Likely to occur several times a year  |
| Possible                           | Possibly occurs once a year or 2 years|
| Rare                               | Possibly occurs once 5- 10 years      |

- Impact of the risk: Impact of the risk should be based on the effectiveness of the existing controls for the identified risks. The impact should be captured as major / moderate / Incidental. The definition of the impact ratings is as follows:

| Impact level | Confidentiality                                    | Integrity                                          | Availability                                      |
|--------------|----------------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| Major        | Unauthorized access to highly sensitive data such  | Major discrepancies in financial transactions, tra | Full system downtime affecting trading platforms, |
| Moderate     | Sensitive data exposed. Breach results in medium t | Inaccurate or altered data in customer accounts or | Partial downtime or degraded performance of tradin|
| Incidental   | Access to non-sensitive data leading to reputation | Minor discrepancies in customer accounts or trade  | Partial downtime or degraded performance affecting |

### 2.3.3 Risk Evaluation
<!-- section_id: IRM-2.3.3 -->

Risk evaluation step should evaluate the risk with existing controls and method to treat the same. Risk evaluation step should capture the following:

| Risk Evaluation                        |                     |                                             |
|----------------------------------------|---------------------|---------------------------------------------|
| Inherent Risk                          |                     | Risk Treatment Option                       |
| Inherent risk post prevention controls | Inherent Risk Level | Describe the treatment to be applied to risk|

- Inherent risk post prevention controls: Based on evaluation of the existing controls, likelihood, and risk impact ratings, the inherent risks that exist even after the application of the current controls have to be documented.
- Inherent Risk Level: The value of inherent risk is automatically calculated based on the likelihood and impact ratings.

Risk Level (potential / residual) = Likelihood * Consequence

Below table depicts the Risk Level based on likelihood and consequence of the risk:

| Level of Risk                                      |                               |      |
|----------------------------------------------------|-------------------------------|------|
| The ranking assigned after considering the likelih |                               |      |
| Risk Level                                         | Activity                      | Range|
| High                                               | Needs Action                  | 7-9  |
| Medium                                             | Needs Attention / Improvement | 4-6  |
| Low                                                | Monitoring Needed - Annually  | 1-3  |

## 2.4 Risk Treatment
<!-- section_id: IRM-2.4 -->

Risk treatment is the process to make decisions on risks which can be reduced, accepted, avoided, and transferred. The risk treatment plan should be implemented, in order to achieve the identified control objectives. Risk treatment phase should capture the following details:

| Risk Treatment/ Action Plan |                     |                                 |
|-----------------------------|---------------------|---------------------------------|
| Risk Treatment Action/Plan  | ISO 27001 Reference | Timelines                       |
| Steps to treat the risk     |                     | Specify the period of resolution|

- Steps to treat the risk: Based on the risk treatment option selected during the risk evaluation stage, the risk with the risk value as high and medium shall be addressed with appropriate risk treatment measures. For the risks having lower risk values, minimum safeguards should be put in place for ensuring security of the information.
- ISO 27001:2022 Reference: The risk treatment controls shall be mapped to the ISO 27001:2022 standard controls.
- Specify the timeliness: The period required for resolving and mitigating the risks should be specified.

## 2.5 Risk Monitoring and Review
<!-- section_id: IRM-2.5 -->

The risk value remaining after treatment (residual risk), should be accepted based on the risk acceptance criteria. Risk monitoring and review should capture the following details:

| Residual Risk | Residual Risk Likelihood | Residual Risk Impact | Residual Risk Level | Risk Acceptance | Plan/Justification for Residual Risk | Risk Treatment Status | Remarks |
|---------------|---------------------------|----------------------|---------------------|-----------------|--------------------------------------|-----------------------|---------|
| Residual Risk | Assess the probability of risk event occurring | Assess the plausible impact of risk event occurring | Residual Risk Level | Risk Acceptance Criteria | Plan/Justification for Residual Risk | Risk Treatment Status | Describe the Remarks if any e.g.; acceptance criteria |

- Residual Risk: Document the risks that exist even after the controls are taken into account and implemented effectively.
- Likelihood of residual risk: Determine the likelihood of the residual risk based on the residual risk as follows: Frequent / Possible / Rare. The definition of the likelihood ratings is as follows:

| Likelihood                         |                                       |
|------------------------------------|---------------------------------------|
| The probability of risk occurring: |                                       |
| RATING                             | POTENTIAL FOR RISK TO OCCUR           |
| Frequent                           | Likely to occur several times a year  |
| Possible                           | Possibly occurs once a year or 2 years|
| Rare                               | Possibly occurs once 5- 10 years      |

- Impact of residual risk: Determine the impact of the residual risk irrespective of the controls implemented as follows: Major / Moderate / Incidental. The definition of the impact ratings is as follows:

| Consequences                                       |                                                    |
|----------------------------------------------------|----------------------------------------------------|
| The potential outcome of a risk event that affects |                                                    |
| RATING                                             | POTENTIAL FOR RISK TO OCCUR                        |
| Major                                              | The loss of confidentiality, integrity, or availab |
| Moderate                                           | The loss of confidentiality, integrity, or availab |
| Incidental                                         | Little/negligible impact on operations, assets or  |

- Residual Risk: The value of residual risk is automatically calculated based on the likelihood and impact ratings.

Risk Level (residual) = Likelihood * Consequence

Below table depicts the Risk Level based on likelihood and consequence of the risk:

| Level of Risk                                      |                               |      |
|----------------------------------------------------|-------------------------------|------|
| The ranking assigned after considering the likelih |                               |      |
| Risk Level                                         | Activity                      | Range|
| High                                               | Needs Action                  | 7-9  |
| Medium                                             | Needs Attention / Improvement | 4-6  |
| Low                                                | Monitoring Needed – Annually  | 1-3  |

- Risk Acceptance Criteria: The various reasons for accepting risk as defined as below:

| Reason                | Details                                            |
|-----------------------|----------------------------------------------------|
| Budgetary / Financial | There will be financial constraints binding on the |
| Environmental         | Environmental factors, such as space availability, |
| Technological         | Some measures are technically not feasible, e.g. i |
| Cultural              | Sociological constraints on the implementation of  |
| Time                  | Not all safeguards can be implemented immediately. |

- Plan or justification of residual risk: The plan to resolve and reduce the residual risk effects should be documented.
- Risk treatment Status for residual risks: Based on the plan for managing the residual risks, the following could be the status for the treatment plan:
  1. Ongoing: Select if the treatment is a continuous activity
  2. Planned: Select if the treatment is planned and yet to be implemented.
  3. Implemented: Select if the treatment plan has been implemented and executed.
- Remarks (If any): Deviation to the process or risk acceptance criteria should be documented.

## 3. Maintenance of Risk Management Methodology
<!-- section_id: IRM-3.0 -->

In view of the constant change of operating environment in terms of people, process, and technology, management should ensure risk monitoring and compliance regime on an on-going basis to ascertain the performance and effectiveness of the risk management process. Further, improvements should be documented and implemented, as dictated by regular review of the ISMS and events that impact the risk management to ensure that the risk management methodology does not become obsolete.

[[external:Choice]] should conduct at least an annual review of risk management methodology, the risks identified, their assessment, and treatment plans. [[role:CISO]] is responsible for the overall review and update of risk management methodology and risk assessment and treatment sheet. Individual owners are responsible to review and update the related risks and their treatment plans. The reviews should include adequacy and effectiveness with regard to any identified significant changes in [[external:Choice]], changes in technology, changes in business objectives and processes, changes in identified threats, and changes in legal and regulatory environment. Further, reviews should be performed whenever there is an incident.

## 4. References
<!-- section_id: IRM-4.0 -->

1. [[doc:Risk Management Template]]
```
