# What to look for

## Chapter 1

**Policy Statements**:
Policy Statement
  - Should be clear and unambiguous
  Exception
    - Provides specific guidance about the procedure or process that must be followed in order to deviate from the policy.
    - may include an escalation contact in the event the person who is dealing with the situation needs to know whom to contact next.
  Overview
  Accountability
    - Should address who is responsible for ensuring that the policy is enforced
    - Usually expressed as a position, not the actual name of an individual
    - provides additional information to the reader about who to contact if a problem is discovered.
**Standards**
  Scope and Purpose
    - Should explain or describe.
  Roles and Responsibilities
    - outline and highlight roles and responsibilities.
    - who implements, monitors, and maintains the standard

**Policies**
  Mandatory Vacations
    - requires employees to take time away from work to refresh, and it is primarily used in jobs related to the financial sector.
    - gives company a chance to make sure that others can fill in any gaps in skills and it satisfies the need to have replication or duplication at all levels.
    - provides an opportunity to discover fraud
  Job rotation
    - defines intervals at which employees must rotate through positions.
    - similar to mandatory vacations, helps ensure the company does not become dependent on one person.
    - provides opportunity to see what the previous person did and potentially uncover fraud
  Separation of Duties
    - designed to reduce the risk of fraud and to prevent other losses in the organization.
    - require more than one person to accomplish key processes
    - To embezzle funds successfully, an individual would need to recruit others to commit an act of collusion, an agreement between two or more parties established for the purpose of committing deception or fraud.
  Clean Desk
    - what do you think genius.
  Background Check
  Acceptable Use
    - Describe how the employees in an organization can use company systems and resources, both software and hardware.
    - outline consequences for misuse
  Least Privilege
  Physical Access Control

**Management types**
  Audit Management
  Incident Management
  Change Management

**Acronyms**
  SLA
    - Service level Agreement
    MTBF
      - Mean Time Between Failures: measure of the anticipated incidence of failure for a system or component
    MTTF
      - Mean Time to Failure: average time to failure for a nonrepairable system.
    MTTR
      - Mean Time to Restore: The measurement of how long it takes to repair a system or component once a failure occurs.
    RTO
      - Recovery Time Objective: the maximum amount of time that a process or service is allowed to be down and the consequences still be considered acceptable
    RPO
      - Recovery Point Objective: similar to RTO, but defines the point at which the system needs to be restored
  **Privacy:**
    PIA
      - Privacy IMpact Assessment: associated with Business Impact Analysis (BIA) and it identifies the adverse impacts that can be associated with the destruction, corruption, or loss of accountability for data.
    PTA
      - Privacy Threshold Analysis
    DHS
      - Department of Homeland security: uses PIA to identify and mitigate privacy risks by telling the public wat PII it collects, why it is collected, and how it is used, accessed, shared, safeguarded, and stored.
    PII
      - Personally Identifiable Information
  DLP
    - Data Loss Prevention: systems that monitor contents of other systems, in order to make sure that the key content is not deleted or removed.
  RAC
  BIA
    - Business Impact Analysis: process of evaluating all the critical systems (important to core business functions) in an organization to define impact and recovery plans.
    - only focuses on the impact loss would have on the organization
    - Goals:
      - The true impact and damage that an outage can cause will be visible.
      - Understanding the true loss potential may help you in your fight for a budget.
      - Most important, perhaps, the process will document which business processes are being used, the impact they have on the organization, and how to restore them quickly.
  BPA
    - Business Partner Agreements: An agreement between partners in a business that outlines their responsibilities, obligations, and sharing of profits and losses
  MOA/MOU
    - Memorandum of agreement/Memorandum of Understanding:
    - Most commonly known as MOU rather than MOA
    - This is a document between two or more parties defining their respective responsibilities in accomplishing a particular goal or mission, such as securing a system.  
  ISA
    - Interconnection Security Agreement: Specifies the technical and security requirements of interconnection.
  SLE
  ARO
  ALE
  AV
  RAID 0
    - Disk striping, uses multiple drives and maps them together as a single phsyical drive.
    - Good Performance, bad for fault tolerance.
  RAID 1
    - Disk Mirroring
    - provides 100 percent redundancy because everything is stored on two disks. if a disk fails another operates. the failed disk can be replaced and the RAID 1 can be regereated.
  RAID 3
    - Disk striping with a parity disk
    - Implements fault tolerance, Ensures that the data can be recovered in the event of a failure.
    - stripes in conjuction with a separate disk that stores parity information - the value based ont he value of the data stored in each disk location.
    - Each set of servers comes with a corresponding disk for parity.
  RAID 5
    - Disk Striping with parity
    - Most common form of RAID today
    - each individual disk per server has its own parity disk
## Chapter 2

  Hotfix
  Service pack
  Overhaul
  Security update

  DMZ
    - DeMilitarized Zone
    - A network segment between two firewals.
    -  meant to set public facing servers, the exterior firewall of the DMZ is more permissive than the interior, making the D<Z somewhat less secure.
  ISMS
    - Information Security Management System
    - Applies a wide raneg of systems used for infosec
  SPI
    - Stateful packet inspection
    - firwall that examines each packet and also remembers the recent previous packets.

  Air-Gap
  VLAN
  Control Diversity
    - do not address any particular security concern with a single control or single vendor.
  Vendor Diversity
    - maintaining a diverse set of vendors.

  **Industry-Standard Frameworks and Architectures**
    ISO Standards
    - International Organization for Standardization
    - de facto source for international standards.
    - ISO Standards:
      - ISO/IEC 27001:2013
        - Information Technology Security Techniques -- InfoSec Management systems requirements
      - ISO 27017: guidance for cloud security.
      - ISO 27002: recommends best practices for initiating, implementing, and maintaining ISMS
    NIST Standards
      - National Institute of Standards and Technology
      - source for many standards int he United States.
      - NIST Publication:
        - 800-12: provides a broad overview of computer security.
          - Primarily deals with areas of security controls.
          - Written for federal agencies.
          - Introduction to Computer Security.
          - Emphasizes the need to address computer security throughout the system development life cycle.
        - 800-14: describes common security principles that should be addressed within security policies.
          - Describe 8 principals and 14 practices that can be used to develop proper security policies.
          - large portion dedicated to auditing user activity.
        - 800-53: organizes security measures into families of controls, such as risk, assessment, access control, incident response, and others.
          - Also defines three levels of minimum security controls.
        - 800-82 revision 2: Guide to Industrial Control System (ICS) Security.
          - includes SCADA (Supervisor Control and Data Acquisition) and PLCs (Primary Logic Controllers)
          - examines the threats to these systems in detail
  **Firwalls**
    SDN
      - Software-Defined Networking
      - Entire network is virtualized.
      - allows relatively easy segmentation of the network.
    Proxy Firewalls
      - intermediary between the network and any other network.
      - used to process data from an outside network; the proxy firewall examines the data and makes rule-based decisions.  
    SPI
      - Stateful Packet inspection Firewall
      - entire conversation between between client and server is examined.
      - remembers what the recent previous packets from the same client contained
  **Hardware Firmware**
  SDN
    - Software-Defined Network
    - all of the network including security is virtualized.
  SED
    - Self Encrypting Drive
  FDE
    - Full disk encryption
  MEK
    - Media Encryption Key
  KEK
    - Key encryption key
  TPM
    - Trusted Platorm Modules
  HSM
    - Hardware security Modules
  RoT
    - Root of trust
    - each layer starting with BIOS/UEFI is validated upon startup.

## Chapter 3
  **Infrastructure**
  ACL
    - Access Control List: table or data file that specifies whether a user or group has access to a specific resource on a computer or network.
  AP
    - Access Point
  AD-IDS:
    - Anomaly Detection IDS:
    - looks for deviations from a pattern of normal network traffic.
  AH
    - Authentication Header
  clustering:
    - Balancing loads and providing fault tolerance.
  DLP:
    - Data Loss Prevention
    - any systems that identify, monitor, and protect data to prevent it from unauth use.
  ESP
    - Encapsulating Security Protocol
    - an IPSec header used to provide a mix of security services in IPv4 and IPv6.
    - encapsulation: enclosing data into a packet.
  HIDS:
    - Host-based IDS
    - run as a service or a background process.
    - examines the machine logs, system events, and application interactions; it normally doesn't monitor incoming network traffic to the host.
  HSM
    - Hardware Security Model:
    - software or appliance stand-alone used to enhance security
  NAC:
    - Network access control
    - The set of standards defined by the network for clients attempting to access it.
  NIPS
    - Network Intrusion Prevention System
  NIDS
    - Network IDS
    - sometimes placed infront of the firewall.
  bridge
    - used to divide large networks into smaller sections by sitting between two physical network segments and managing the flow of data between the two.
    -
 **Firewalls**
  URL Filters
    - blocking websites based solely on URL.
  Stateless
    - makes decisions based on the data that comes in.
  UTM
    - Unified threat Management
    - provides:
      - URL Filtering
      - Content inspection
      - Malware Inspection
  Content inspection
    - looks through data that is coming in.
  Malware Inspection
    - tool that identifies malware before it accesses a system.
  Full Tunnel
    - all requests are routed and encrypted through the VPN
  Split Tunnel
    - only some (usually all incoming requests) are routed and encrypted over the VPN
  **Intrusion Detection Systems**
  Computer or server after the firewall designed to monitor traffic for potential criminal activity.
    Activity
      - element of a data source that is of interest to the oerator.
    Administrator
      - person responsible fro setting the security policy for an organization and responsible for making decisions about the deployment and configuration of the IDS.
    Alert
      - message fromt he analyzer indicating that an event of interest has occurred
    Analyzer
      - component or process that analyzes the data collected by the sensor.
    Data Source
      - raw informatino that the IDS or IPS uses to detect suspicious activity.
    Event
      - Occurrence or continuous occurrence in a data source that indicates that a suspicious activity has occured.
    Manager
      - component or process the operator uses to manage the IDS or IPS
    notification
      - the IDS/IPS manager makes the operator aware of an alert.
    Operator
      - the person primarily responsible for the IDS/IPS, generally the administrator.
    Sensor:
      - the IDS component that collects data from the data source and passes it to the analyzer for analysis.
    Behavior-Based Detection
      - looks for variations in behavior such as unusually high traffic, policy violations, and so on.
    Signature-Based Detection
      - MD-IDS (Misuse Detection IDS)
      - primarily focused on evaluating attacks based on signatures and audit trails.
    Anomaly Detection
      - AD system looks for anomalies.
      - checks for operations that go outside the normal, meaning a baseline is required for this to be effective.
    heuristic
      - uses algorithms to analyze traffic passing through the network.
      - there should be a baseline of activity which provides a  stable, long-term perspective on network activity.
## Chapter 4
  Vocab
    CHAP
      - Challenge Handshake Authentication Protocol
      - Periodically re-authenticates.
    CER
       - Crossover Error Rate
       - The point at which the FRR and FAR are equal.
       - sometimes called the Equal Error Rate ERR
    DEP
      - Data Execution prevention
      - Any technique that prevents a program from running without the users approval.
    DLP
      - Data Loss Prevention
      - Software or techniques designed to detect attempts to exfiltrate data
    FAR
      - False acceptance rate
      - The rate at which a biometric solution allows individuals it shoudl have rejected
    FRR
      - False Rejection Rate
      - The rate at which a biometric solution rejects individuals it should have allowed.
    Federation
      - A collection of computer networks that agree on standards of operation.
    OAUTH
      - Open Authorization Standard. Common method for authorizing websites or applications.
  **Network Tools**
    tcpdump
      - common packet sniffer for Linux.
    Wireshark
      - network packet sniffer
      - often use to view network logs
    SolarWinds
      - Network scanner
      - shows the network topology in the scan.
    LanHelper
      - Cheap network mapper and scanner
      - Options
        - Scan Lan
        - Scan IP
        - Scan Workgroups
    Aircrack
      - Scanner and password cracker for free.
    pwdump
      - password cracker
    Ophcrack
      - Widely popular password cracking tool.
    Nessus
      - vulnerability scanner.
    MBSA
      - Microsoft Baseline Security Analyzer.
    OWASP Zap
      - Publish top vulnerabilities.
      - Zap is a free tool used to scan website vulnerabilities.
  **Authentication**
    LDAP
      - Lightweight Directory Access Protocol
    Kerberos
      - authentication protocol
      - uses Key distribution center (KDC)
      - hands out tickets
    RADIUS
      - Remote Authentication Dial-In User Service
      - Allows authentication
      - IEtF standard implementd by major operating system manufacturers
      - allows authentication of remote and other network connections.
    TACACS, TACACS+, XTACACS
      - Terminal Access Controller Access Control System, Extended TACACS (XTACACAS)
      - client-server-oriented environment.
      - works like RADIUS
    OATH
      - Open Standard for Authorization,
      - used for websites
    SAML
      - Security Assertion Markup Language
      - uses tags that define security authorization.
      - Shibboleth is a single-sign-on system used widely ont he internet written in SAML
  **Identity and Access Control**
    MAC
      - Mandatory Access Control
      - inflexible method for how information is permitted.
      - all access is predefined.
      - Admin must make changes that need to be made.
      - all relationships must be planned first in order to work effectively.
      - often used in classified use cases.
    DAC
      - flexible access regarding how information is accessed.
      - allows users to sahre information dynamically with others.
      - increases the risk of unauthorized disclosure of information.
      - Example, the Owner, Group, other, permission groups in linux for read, write, execute.
    RoBAC
      - Role-based Access Control
      - Models approach the problem of access control based on estblished roles in an organization.
      - each employee has one or more roles that allow access to specific information.
      - think group-based control or group-based permissions.
    RuBAC
      - Rule-Based Access Control
      - Uses settings preconfigured security policies to make all decisions.
        - Deny all but those who specifically appear in a list (allow list or whitelist)
        - deny only those who specifically appear in the list (a true deny list or blacklist)
      - easiest setup is with access control lists (ACL)
    ABAC
      - Attribute-based access control
      - looks at subjects that are attempting to access a given object but considers all the various attributes associated with the subject and object in making the accses control decision.
        - where *subject* is an active entity, generally an individual, process or device.
        - where *object* is some resource that the subject is attempting access
        - where *attributes* are characteristics that define specific aspects of teh subject, object, environment conditions, and/or requested actions that re predefined and preassigned by an authority.
    Token

## Chapter 5

  Vocab
    RFID
      - Radio Frequency Identification
      - Technology that incorporates the use of electromagnetic coupling in the radio frequency of the spectrum to identify items uniquely.
    NFC
      - Near Field Communication
      - Enables communication between devices when they're touched together.
        - 1.6 inches
    WPS
      - Wi-Fi Protected Setup
      - An authentication process that requires the user to do something in order to complete the enrollment process.
    WEP
      - Wired Equivalent Privacy
      - A security protocol for 802.11b (wireless) networks that attempts to establish the same security for them as would be present in a wired network.
    IV attack
      - Initialization Vector attack
      - possible due to weaknesses in WEP
      - 24-bit
      - when attackers crack the WEP secret key
    TKIP
      - Temporal Key Integrity Protocol
      - Placed a 128-bit wrapper aroundt he WEP encryption with a key that is based on things such as the MAC address of the destiniation device and the serial number of the packet.
      - backward compatible replacement to WEP
      - TKIP is broken
    Disassociation
      - Also called Deauthentication
      - forces user to disconnect from AP
## Chapter 6
  Vocab
    Cloud access Security Broker
      - On-premise or cloud-based security policy (CASB)
    Cloud Bursting
      - Moving the execution of an application to the cloud on an as-needed basis
      - usually associated with the QoS protocol (Quality of Service)
    Private Cloud
      - Provisioned for the exclusive use by a single organization comprising multiple consumers. It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.
      - Data does not need to be put on the internet.
    Public Cloud
      - Provisioned for open use by the general public. It may be owned, managed, or operated by a business, academic, or government organization, or some combination of them. It exists on the premises of the cloud provider.
    Community Cloud
      - Provisioned for exclusive use by a specific community of consumers from organizations that ahve shared concerns. It may be owned, managed, or operated by one or more of the organizations in the community, a third party, or some conbination of them, and it may exist on or off premises.
    Hybrid Cloud
      - combination of any other type of cloud, generally public and private.
    PaaS
      - Platform as a Service model, the consumer has the ability to create applications and host them
      - The consumer can "deploy" but do not "manage or control" any of the underlying cloud infrastructure
      - they can have "control over the deployed application"
    SaaS
      - Software as a Service model, the consumer has the ability to use applications provided by the cloud provider over the internet.
      - The consumer can "use" the providers application and they do not "manage or control" any of the unerlying cloud infrastructure.
    IaaS
      - Infrastructure as a Service IaaS model, the consumer can "provision" and is able to "deploy an run", but they still do not "manage or control" the underlying infrastructure.
      - The user can be responsible for some aspects of the infrasture but does not manage or control it all.
      -
    VM Sprawl
      - Growth that occurs one a large number of virtual machines and requries resources -- usually administration related -- to keep up with
    VM escape
      - The act of breaking out of one virtual machine into one or more others on the same physical host.
    VDI/VDE
      - Virtual Desktop environment/Infrastructure
        - Environment: Stores everything related to the user remotely and client software locally simulates the user's desktop environment and capabilities while running them on the host.
    Multitenancy
      - The ways cloud computing is able to obtain cost efficiencies is by putting data from various clients on the same machines.

## Chapter 7

### Vocab
  APT
    - Advanced Persistent Threats
    - Any sophisticated series of related attacks taking place over an extended period of time.
  Agile Development
    - A method of software development meant to be rapid.
  database Normalization
    - The process of removing duplication in a relational database.
  fuzzing
    - A method of testing that intentionally enters invalid input to see if the application can handle it.
  IaC
    - Infrastructure as Code
    - The process of managing and provisioning computer data centers through machine-readable definition files.
  IoT
    - Internet of Things
  OWASP
    - Open Web Application Security Project
    - An online community that develops free articles, documentation, tools, and more on web application security.
### Types of testing

**Unit Testing**
  Test a unit whenever it is completed, this can be a a module, programming class, or complete application. testing can be dynamic, static, or both.

**Integration Testing**
  If two or more units are connected in some manner this is functionality needs to be tested. usually dynamically tested.
**User Acceptance Testing**
  referred to as beta testing. test of  if users have the system that meets their needs while not exceeding their needs.
**Regression Testing**
  test changes and all systems affected by the change.

### Patch Management

**Hotfix**
  Immediate and urgent patch. not optional and automatically updated
**Patch**
  Provides additional functionality, non-urgent fix. Sometimes optional.
**Service Pack**
  Cumulative assortment of the hotfixes and patches to date. requires heavy testing to ensure no problems arise during update.

### Database security

Three models of augmented security for databases.
**One-Tie Model**
  single-tier environment. The database and the application exist on a single system.
**Two-Tier Model**
  client workstation or system runs an application that communicates with the database that is running on a different server.
**Three-Tier Model**
  middle-tier server, isolates end user from database. client server connects to middle tier server, which evaluates the requests and sends them to the database for processing. all data must flow through the middle-tier.
## Chapter 8

### Vocab

Asymmetric Cipher
Challenge Handshake Authentication Protocol (CHAP)
Collision
Cryptographic Hash
PRNG - Pseudo-Random Number Generator
Rainbow Table
Salt
Symmetric Cipher
X.509
