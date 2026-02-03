```yaml
---
document_id: "HP"
title: "Hardening Policy"
filename: "Choice ISMS_Hardening Policy..pdf"
version: "2.3"
status: "approved"
created_date: "2016-10-17"
effective_date: "2025-01-08"
last_reviewed: "2024-03-31"
next_review: null

owner:
  name: "Abhishek Vinayak"
  role: "Policy Owner"

prepared_by:
  - name: "Ashutosh Bhardwaj"
    role: "Policy Preparer"

approved_by:
  - name: "Yogesh Jadhav"
    role: "Policy Approver"
    date: "2025-01-08"

classification: "Internal"
applies_to:
  - "employees"
  - "contractors"

regulatory_frameworks:
  - id: "ISO27001"
    name: "ISO 27001:2022"

references:
  - document_id: "ISMS"
    title: "Consolidated ISMS Policy"
    relationship: "related"

scope:
  description: "Guidance for establishing a secure configuration posture for various systems."
  inclusions:
    - "Fortinet Firewall"
    - "Switch"
    - "Windows Server"
    - "Ubuntu OS"
  exclusions:
    - "Non-specified systems"

entities:
  roles:
    - "Firewall Administrator"
    - "Network Administrator"
    - "Windows Server Administrator"
    - "Ubuntu System Administrator"
  controls:
    - "Firewall"
    - "Encryption"
    - "Two-factor Authentication"
  assets:
    - "FortiGate"
    - "Switch"
    - "Windows Server"
    - "Ubuntu Systems"
  processes:
    - "Compliance Checks"
    - "Logging and Monitoring"
    - "Backup and Recovery"
  external_parties:
    - "Fortinet"
    - "Microsoft"

tags:
  - "hardening"
  - "security"
  - "compliance"
---
# Hardening Policy
<!-- section_id: HP-0 -->

## Version Control
<!-- section_id: HP-0.1 -->

| Action      | Date       | Revision | Prepared / Amended By | Approved By   | Details                        |
|-------------|------------|----------|-----------------------|---------------|--------------------------------|
| Created On  | 2016-10-17 | 1.0      | Mahesh Tamhankar      | Amit Jaokar   | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2017-02-21 | 1.1      | Mahesh Tamhankar      | Amit Jaokar   | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2018-02-13 | 1.2      | Mahesh Tamhankar      | Amit Jaokar   | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2018-02-20 | 1.3      | Mahesh Tamhankar      | Utpal Parekh  | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2019-08-10 | 1.4      | Mahesh Tamhankar      | Yogesh Jadhav | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2020-01-11 | 1.4      | Mahesh Tamhankar      | Yogesh Jadhav | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2021-07-14 | 1.6      | Sunil Utekar          | Yogesh Jadhav | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2022-01-08 | 1.7      | Sunil Utekar          | Yogesh Jadhav | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2023-04-09 | 2.0      | Ashutosh Bhardwaj     | Yogesh Jadhav | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2024-01-31 | 2.1      | Anil Ashok & Associates | Ashutosh Bhardwaj | Inherited from Consolidated ISMS Policy |
| Reviewed On | 2024-03-31 | 2.2      | Abhishek Vinayak      | Ashutosh Bhardwaj | Added Latest Hardening controls |
| Approved On | 2025-01-08 | 2.3      | Abhishek Vinayak      | Yogesh Jadhav | Approval as per ISO requirement |

## Confidentiality Agreement
<!-- section_id: HP-1.0 -->

This document is classified as Choice Equity Broking Private Limited (referred to as CEBPL throughout the document) Internal. No part of it may be reproduced or disclosed without the prior consent of CEBPL, to include duplication and/or storage of documents to an alternate location. Disclosure of this document is solely for review and approval as is required for CEBPL to meet pertinent regulatory requirements and corporate policy compliance. No part of this document shall be taken to create or modify any contractually binding obligations upon CEBPL.

## Fortinet Firewall
<!-- section_id: HP-2.0 -->

### 1. Overview
<!-- section_id: HP-2.1 -->

This document provides prescriptive guidance for establishing a secure configuration posture for Fortinet Firewall OS v7.4.0 build2360.

### 2. Audience
<!-- section_id: HP-2.2 -->

This document is intended for the [[role:Firewall Administrator]] to implement secure solutions that incorporate Fortinet Firewall.

### 3. Scope
<!-- section_id: HP-2.3 -->

Revisions to this security baseline will be applicable to builds occurring after the revision date. No retroactive configurations are required as a result of revisions unless otherwise identified as necessary by [[process:Information Security Architecture]].

### 4. Fortinet Compliance Checks
<!-- section_id: HP-2.4 -->

#### 4.1 Install the FortiGate unit in a physically secure location
<!-- section_id: HP-2.4.1 -->

**[MANDATORY]** Install your FortiGate in a secure location, such as a locked room or one with restricted access. A restricted location prevents unauthorized users from getting physical access to the device.

#### 4.2 Register your product with Fortinet Support
<!-- section_id: HP-2.4.2 -->

**[MANDATORY]** Register your Fortinet product with Fortinet Support to receive customer services, such as firmware updates and customer support.

#### 4.3 Keep your FortiOS firmware up to date
<!-- section_id: HP-2.4.3 -->

**[MANDATORY]** Always keep FortiOS up to date. The most recent version is the most stable and has the most bugs fixed and vulnerabilities removed.

#### 4.4 Disable administrative access to the external (Internet-facing) interface
<!-- section_id: HP-2.4.4 -->

**[MANDATORY]** When possible, don’t allow administration access on the external (Internet-facing) interface unless required and approval is given.

#### 4.5 Allow only HTTPS access to the GUI and SSH access to the CLI
<!-- section_id: HP-2.4.5 -->

**[MANDATORY]** Use the following command to require TLS <LATEST_STABLE_TLS_VERSION> for HTTPS administrator access to the GUI.

#### 4.6 Re-direct HTTP GUI logins to HTTPS
<!-- section_id: HP-2.4.6 -->

**[MANDATORY]** Enable Redirect to HTTPS to ensure all attempted HTTP login connections are redirected to HTTPS.

#### 4.7 Change the HTTPS and SSH admin access ports to non-standard ports
<!-- section_id: HP-2.4.7 -->

**[MANDATORY]** Change the default port configurations for HTTPS and SSH administrative access for added security.

#### 4.8 Maintain short login timeouts
<!-- section_id: HP-2.4.8 -->

**[MANDATORY]** Set the idle timeout to a short time to avoid the possibility of an administrator walking away from their management computer and leaving it exposed to unauthorized personnel.

#### 4.9 Restrict logins from trusted hosts
<!-- section_id: HP-2.4.9 -->

**[MANDATORY]** Setting up trusted hosts for an administrator limits the addresses from where they can log into FortiOS.

#### 4.10 Set up two-factor authentication for administrators
<!-- section_id: HP-2.4.10 -->

**[MANDATORY]** FortiOS supports FortiToken and FortiToken Mobile 2-factor authentication.

#### 4.11 Create multiple administrator accounts
<!-- section_id: HP-2.4.11 -->

**[MANDATORY]** Create accounts for each person or each role that requires administrative access.

#### 4.12 Modify administrator account lockout duration and threshold values
<!-- section_id: HP-2.4.12 -->

**[MANDATORY]** Configure the lockout options to prevent unauthorized access attempts.

#### 4.13 Rename the admin administrator account
<!-- section_id: HP-2.4.13 -->

**[MANDATORY]** Improve security by renaming the admin account.

#### 4.14 Add administrator disclaimers
<!-- section_id: HP-2.4.14 -->

**[MANDATORY]** FortiOS can display a disclaimer before or after logging into the GUI or CLI.

#### 4.15 Turn on global strong encryption
<!-- section_id: HP-2.4.15 -->

**[MANDATORY]** Configure FortiOS to use only strong encryption and allow only strong ciphers.

#### 4.16 Disable static keys for TLS
<!-- section_id: HP-2.4.16 -->

**[MANDATORY]** Prevent all TLS sessions that are terminated by FortiGate from using static keys.

#### 4.17 Require larger values for Diffie-Hellman exchanges
<!-- section_id: HP-2.4.17 -->

**[MANDATORY]** Use larger Diffie-Hellman values for stronger encryption.

#### 4.18 Disable auto USB installation
<!-- section_id: HP-2.4.18 -->

**[MANDATORY]** Disable USB installation to prevent unauthorized configuration or firmware loading.

#### 4.19 Set system time by synchronizing with an NTP server
<!-- section_id: HP-2.4.19 -->

**[MANDATORY]** Use an NTP server to set system time for accurate auditing and consistency.

#### 4.20 Enable password policies
<!-- section_id: HP-2.4.20 -->

**[MANDATORY]** Create a password policy that all administrators must follow.

#### 4.21 Configure auditing and logging
<!-- section_id: HP-2.4.21 -->

**[MANDATORY]** Enable Event Logging for optimum security.

#### 4.22 Disable unused interfaces
<!-- section_id: HP-2.4.22 -->

**[MANDATORY]** Disable interfaces that are not in use to reduce the attack surface.

#### 4.23 Disable unused protocols on interfaces
<!-- section_id: HP-2.4.23 -->

**[MANDATORY]** Disable unused protocols that attackers may attempt to use to gather information.

## Switch
<!-- section_id: HP-3.0 -->

### 1. Overview
<!-- section_id: HP-3.1 -->

This document provides prescriptive guidance for establishing a secure configuration posture for Switch.

### 2. Audience
<!-- section_id: HP-3.2 -->

This document is intended for [[role:Network Administrator]] to implement secure solutions that incorporate on Switch.

### 3. Scope
<!-- section_id: HP-3.3 -->

Revisions to this security baseline will be applicable to builds occurring after the revision date. No retroactive configurations are required as a result of revisions unless otherwise identified as necessary by [[process:Information Security Architecture]].

### 4. Switch Compliance Checks
<!-- section_id: HP-3.4 -->

#### 4.1 Default passwords
<!-- section_id: HP-3.4.1 -->

**[MANDATORY]** Change the default passwords on the device, all of them, not just the one on the account being used.

#### 4.2 SNMP v3
<!-- section_id: HP-3.4.2 -->

**[RECOMMENDED]** If the device supports it, use SNMP v3, otherwise use a nice long community string.

#### 4.3 Logging and Monitoring
<!-- section_id: HP-3.4.3 -->

**[MANDATORY]** Use centralized logging of switch activities and regularly review logs to identify any anomalies.

#### 4.4 Management VLAN
<!-- section_id: HP-3.4.4 -->

**[MANDATORY]** Configure a management VLAN and use ACL to control access to this VLAN.

#### 4.5 Network Segmentation
<!-- section_id: HP-3.4.5 -->

**[MANDATORY]** Set up VLANs to segregate your network segments and use ACLs to control traffic flows between them.

#### 4.6 SSH /Telnet
<!-- section_id: HP-3.4.6 -->

**[MANDATORY]** Use SSH v2, disable telnet, and implement strong, unique passwords for administrative accounts.

#### 4.7 Web interface
<!-- section_id: HP-3.4.7 -->

**[MANDATORY]** If you need it, use SSL, otherwise disable the web interface.

#### 4.8 Update and Patch
<!-- section_id: HP-3.4.8 -->

**[MANDATORY]** Keep the switch firmware updated with the latest security patches and bug fixes.

#### 4.9 Disable Unused Services and Ports
<!-- section_id: HP-3.4.9 -->

**[MANDATORY]** Turn off unnecessary services and ports to reduce the attack surface.

#### 4.10 Physical Security
<!-- section_id: HP-3.4.10 -->

**[MANDATORY]** Secure the physical access to the switch to prevent unauthorized access or tampering.

#### 4.11 Backup Configuration
<!-- section_id: HP-3.4.11 -->

**[MANDATORY]** Regularly backup switch configurations to ensure quick recovery in case of configuration errors or security incidents.

## Windows Server
<!-- section_id: HP-4.0 -->

### 1. Overview
<!-- section_id: HP-4.1 -->

This document provides prescriptive guidance for establishing a secure configuration posture for Windows Server.

### 2. Audience
<!-- section_id: HP-4.2 -->

This document is intended for the [[role:Windows Server Administrator]] to implement secure solutions that incorporate Windows Server.

### 3. Scope
<!-- section_id: HP-4.3 -->

Revisions to this security baseline will be applicable to builds occurring after the revision date. No retroactive configurations are required as a result of revisions unless otherwise identified as necessary by [[process:Information Security Architecture]].

### 4. Hardening Windows Server
<!-- section_id: HP-4.4 -->

Hardening a Windows Server involves securing the system by implementing various measures to reduce its attack surface and enhance its resilience against potential threats. Here's a basic guideline for hardening steps:

1. **Installation and Configuration**:
   - Install the latest version of Windows Server from a trusted source.
   - During installation, configure roles and features only as necessary to minimize the attack surface.

2. **Applying Updates**:
   - Regularly update the server with the latest patches and security updates from Microsoft.
   - Enable automatic updates or establish a schedule for manual updates.

3. **User Accounts and Permissions**:
   - Implement the principle of least privilege. Assign users only the permissions they need to perform their tasks.
   - Disable or remove unnecessary default user accounts.
   - Change default passwords and ensure strong password policies are enforced.

4. **Firewall Configuration**:
   - Enable Windows Firewall and configure it to allow necessary traffic while blocking unnecessary ports and services.
   - Use Group Policy or Windows Defender Firewall with Advanced Security to create specific rules.

5. **Antivirus and Malware Protection**:
   - Install reputable antivirus software and keep it updated regularly.
   - Schedule regular scans and configure real-time protection.

6. **Remote Desktop Protocol (RDP) Security**:
   - Change the default RDP port from 3389 to a custom port to deter unauthorized access attempts.
   - Implement Network Level Authentication (NLA) for RDP sessions.

7. **Data Encryption**:
   - Use an encryption tool to encrypt sensitive data on the server’s drives.
   - Ensure that encryption keys are properly managed and stored securely.

8. **Auditing and Logging**:
   - Enable Windows auditing to track and log security events and system activities.
   - Configure log settings to store logs securely and regularly review them for suspicious activities.

9. **Server Roles and Features**:
   - Disable or remove unnecessary server roles and features.
   - Regularly review installed applications and services, removing or updating those not in use.

10. **Backup and Recovery**:
    - Set up regular backups of critical data and system configurations.
    - Test the backup and recovery process periodically to ensure its effectiveness.

11. **Physical Security and Access Control**:
    - Ensure physical access to the server is restricted and monitored.
    - Implement measures to protect against unauthorized access to server hardware.

12. **Monitoring and Incident Response**:
    - Deploy intrusion detection systems or monitoring tools to detect and respond to security incidents promptly.
    - Develop and regularly update an incident response plan.

## Ubuntu OS
<!-- section_id: HP-5.0 -->

### 1. Overview
<!-- section_id: HP-5.1 -->

This document provides prescriptive guidance for establishing a secure configuration posture for systems with Ubuntu OS.

### 2. Audience
<!-- section_id: HP-5.2 -->

This document is intended for the [[role:Ubuntu System Administrator]] to implement secure solutions that incorporate Ubuntu Systems.

### 3. Scope
<!-- section_id: HP-5.3 -->

Revisions to this security baseline will be applicable to builds occurring after the revision date. No retroactive configurations are required as a result of revisions unless otherwise identified as necessary by [[process:Information Security Architecture]].

### 4. Hardening Ubuntu Systems
<!-- section_id: HP-5.4 -->

Hardening a Ubuntu System involves securing the system by implementing various measures to reduce its attack surface and enhance its resilience against potential threats. Here's a basic guideline for hardening steps:

1. **Change time zone**
   - **Control Statement**: It's important to ensure that you select a valid timezone identifier.
   - **Risk/Impact**: Changing the time zone can affect the synchronization of time across various services and applications.

2. **Add below lines to ~/.bash_history**
   - **Control Statement**: The history size determines the number of commands that can be stored in the command history.
   - **Risk/Impact**: By carefully managing the history size, you can strike a balance between usability, security, and resource efficiency.

3. **Ensure that the sticky bit should be set on the below mentioned partitions.**
   - **Control Statement**: The sticky bit is typically used on directories to control file deletion within that directory.
   - **Risk/Impact**: It helps prevent accidental or unauthorized deletion of files within shared directories.

4. **Edit the /etc/fstab file and add nodev, noexec and nosuid to the fourth field (mounting options).**
   - **Control Statement**: This file is a critical system configuration file that contains information about filesystems and devices mounted during system boot.
   - **Risk/Impact**: Incorrect or improper modifications to this file can lead to system boot failures or cause file system errors.

5. **Check status for services:**
   - **Control Statement**: This will provide detailed information about the service, including its current status.
   - **Risk/Impact**: The risk and impact of checking the status of services in Ubuntu are generally low.

6. **Unconfined daemon**
   - **Control Statement**: A process running without any confinement or security restrictions imposed by a mandatory access control framework.
   - **Risk/Impact**: It's crucial to properly assess the risks associated with unconfined daemons and take appropriate measures to confine and secure them.

7. **Network Configuration and Firewalls**
   - **Control Statement**: It's important to follow best practices, such as configuring network interfaces correctly.
   - **Risk/Impact**: By addressing risks and implementing proper security measures, organizations can strengthen their network defenses.

8. **IPv6 Networking Protocols**
   - **Control Statement**: IPv6 is a networking protocol that supersedes IPv4.
   - **Risk/Impact**: It is recommended that systems not accept router advertisements as they could be tricked into routing traffic to compromised machines.

9. **Ensure mounting of FAT filesystems is disabled**
   - **Control Statement**: The FAT filesystem format is primarily used on older windows systems and portable USB drives.
   - **Risk/Impact**: Removing support for unneeded file system types reduces the local attack surface of the system.

10. **Logging and Auditing**
    - **Configure rsyslog**
    - **Control Statement**: The rsyslog software is recommended as a replacement for the default syslogd daemon.
    - **Risk/Impact**: The security enhancements of rsyslog justify installing and configuring the package.

11. **Configure System Accounting (Optional)**
    - **Control Statement**: System auditing, through auditd, allows system administrators to monitor their systems.
    - **Risk/Impact**: It is important that an appropriate size is determined for log files so that they do not impact the system.

12. **System Access, Authentication, and Authorization**
    - **Restrict access to Cron**
    - **Control Statement**: The anacron daemon is used on systems that are not up 24x7.
    - **Risk/Impact**: Cron jobs may include critical security or administrative functions that need to run on a regular basis.

13. **Configure SSH**
    - **Control Statement**: SSH is a secure, encrypted replacement for common login services.
    - **Risk/Impact**: It is strongly recommended that sites abandon older clear-text login protocols and use SSH.

14. **Configure PAM**
    - **Control Statement**: PAM (Pluggable Authentication Modules) is a service that implements modular authentication modules on UNIX systems.
    - **Risk/Impact**: The SHA-512 algorithm provides much stronger hashing than MD5.

15. **Restrict Access to the su Command**
    - **Control Statement**: The su command allows a user to run a command or shell as another user.
    - **Risk/Impact**: Restricting the use of su, and using sudo in its place, provides system administrators better control.

16. **User Accounts and Environment**
    - **Set Shadow Password Suite Parameters**
    - **Control Statement**: While a majority of the password control parameters have been moved to PAM, some parameters are still available through the shadow password suite.
    - **Risk/Impact**: This may lead to increased chances of brute force attacks.

17. **Disable System Accounts**
    - **Control Statement**: There are a number of accounts provided with the ubuntu that are used to manage applications.
    - **Risk/Impact**: It is important to make sure that accounts that are not being used by regular users are locked.

18. **Set Default Group for root Account**
    - **Control Statement**: The usermod command can be used to specify which group the root user belongs to.
    - **Risk/Impact**: Using GID 0 for the root account helps prevent root-owned files from accidentally becoming accessible to non-privileged users.

19. **Set Default umask for Users**
    - **Control Statement**: The default umask determines the permissions of files created by users.
    - **Risk/Impact**: Setting a very secure default value for umask ensures that users make a conscious choice about their file permissions.

20. **Lock Inactive User Accounts**
    - **Control Statement**: User accounts that have been inactive for over a given period of time can be automatically disabled.
    - **Risk/Impact**: Inactive accounts pose a threat to system security.

21. **Warning Banners**
    - **Set Warning Banner for Standard Login Services**
    - **Control Statement**: The contents of the /etc/issue file are displayed prior to the login prompt.
    - **Risk/Impact**: Warning messages inform users who are attempting to login to the system of their legal status.

22. **Remove OS Information from Login Warning Banners**
    - **Control Statement**: Unix-based systems have typically displayed information about the OS release and patch level.
    - **Risk/Impact**: Displaying OS and patch level information in login banners also has the side effect of providing detailed system information to attackers.

23. **System Maintenance**
    - **Control Statement**: Ensure proper system maintenance practices are followed to optimize system performance.
    - **Risk/Impact**: Proper planning, risk assessment, and adherence to best practices can help mitigate these risks.

24. **Review User and Group Settings**
    - **Control Statement**: This section provides guidance on securing aspects of the users and groups.
    - **Risk/Impact**: All accounts must have passwords or be locked to prevent the account from being used by an unauthorized user.

25. **Encryption**
    - **Restrict Cipher list**
    - **Control Statement**: Based on research conducted at various institutions, it was determined that the symmetric portion of the SSH Transport Protocol has security weaknesses.
    - **Risk/Impact**: Data will be communicated in plain text and unauthorized users may try to perform MitM attacks.

26. **Enable TLS 1.2 & Above protocol**
    - **Control Statement**: Strong protocol ensures the message communicated between client and server must be in an encrypted way.
    - **Risk/Impact**: Data will be communicated in plain text and unauthorized users may try to perform MitM attacks.

27. **Disable weak encryption protocol**
    - **Control Statement**: Strong protocol provides that the message communicated between client and server must be in an encrypted way.
    - **Risk/Impact**: Data will be communicated in plain text and unauthorized users may try to perform MitM attacks.

28. **Install RKhunter**
    - **Control Statement**: Rkhunter is a shell script which carries out various checks on the local system to try and detect known rootkits and malware.
    - **Risk/Impact**: Rootkit scanner is scanning tool to ensure you for about 99.9%* you're clean of nasty tools.

29. **Ensure ptrace_scope is restricted (Automated)**
    - **Control Statement**: The ptrace() system call provides a means by which one process may observe and control the execution of another process.
    - **Risk/Impact**: If one application is compromised, it would be possible for an attacker to attach to other running processes.

30. **Ensure core dumps are restricted (Automated)**
    - **Control Statement**: A core dump is the memory of an executable program.
    - **Risk/Impact**: Setting a hard limit on core dumps prevents users from overriding the soft variable.
```
