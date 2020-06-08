# SEcurity Plus
## Section 3.6

### Code Quality and Testing
  - Code Analysis
    - Static Code Anaylsis: doesnt need to be ran.
    - Dynamic Code Analysis: has series of tests to ensure its made correctly.
      - often Fuzzing is used.
  - Stress Testing: check for bottle necks or performance issues.
    - Test to see the worst case workload for the system on any given day.
    -  Model Verification: ensuring the code performs correctly. Ensure teh app meets the needs of the customer correctly.
## Section 3.6 Cloud and Virtualization

### Virtualization Concepts
  - Used to enable a computer to use multipe operating systems on the a single operating system.
  - Hypervisor: allow a computer OS to be seperated from the hardware and the applications from the underlying Physical Hardware.
    - TypeI: Hypervisers run directly on the hardware: Offers more speed and efficiency
    - TypeII: Run on top of the host operating system, these were more popular in the early days of virtualization.
  - Application cells/Containers:
    - run portions of an Operating System seperated from the kernel
    - Allows us to allocate resources to different containers.
    - Share Operating System without needing to share resources with other applications.
  - VM Sprawl: that occurs when a number of virtual machines reaches a point were we can no longer administrator them.
    - Happen because we do not have appropiate policies in place.
    - VMs become stored files that are easier to lose track of.
    - need to keep track of them.
  - VM Escape Protection: When an attack can hit a VM and access the underlying Operating System:
    - Since VMs share memory it can happen.
    - Happens Quickly due to the housing of too many VMs
    - we should treat VMs Like any other computer systems, with the same intrusion detection and protection systems.

### Cloud Concepts
  - Cloud Storage: service model where data is stored on a remote server.
    - data is maintained, managed and operated by a cloud service provider.
    - built using virtualization
    - must ensure that data is always available and secured..
  - Types of Cloud Deployment Models:
    - **Software as a Service (SaaS**): offering of software to end users from with the cloud rather than being installed on client machines.
    - **Platform as a Service**: multiple sets of software working together to provide a service. Provider offers an entire app stack on their own infrastructure.
    - **Infrastructure as a service (IaaS)**: cloud-based system where the provider offers minimum installations. customer is responsible for installing all apps on their cloud.
  - Cloud Systems:
    - Private Cloud: enables organization to better define security processessing and handling of data.
    - Public CLoud: refers to an environment where public users have access to the cloud. your information is still housed in a segregated section of the cloud and shoudl be secure.
    - community cloud: several organizations with common interest share an anvironment.
    - Hybrid Cloud: combines elements from each of the environments.
  - Security as a Service: outsourcing of security functions to a vendor that can offer advantages in scale, costs, and speed.
    - normally called Managed Security Service Provider (MSSP)
    - Hire security professionals that are experts in the realm, MSSPs can perform any functions.
  - Cloud Access Security Broker (CASB): provide policy enforcement between the cloud service providers and customers to ensure that enterprise security polices are maintained across the cloud based resources.
### Resiliency and Automation
  - Automation:
    - Automated Courses of action: saves time performing activities
  - Elasticity: the ability of a system to dynamically increase or decreas on demand hardware resource to scale out.
### Redundancy and High Availability:
  - Redundant security is good.
  - if operations fail, others can pick up immediately in a redundant system.
  - Keeping spare parts around is good.
  - Distributive Allocation:
      - utilize information by storing and managing it across multiple locations.
  - RAID (Redundant Array of Independent Disks): Takes data that normally stored on a single disk and spreads it out amongst several disks.
    - Striping: spreading and storing the data across multiple disks.
    - Mirroring: copying data from one disk to another.
  - RAID 0
    - Striped Disks
  - RAID 1
    - Mirrored Disks
  - RAID 2
    - Bit-level error-correcting code
      - Stripes data at the bit level. rarely used.
  - RAID 3
    - Byte-striped with error check
      - spreads data at the byte level across multiple disks, rarely used.
  - RAID 4
    - Dedicated parity drive
      - Stripes data across several disks, and uses a single drive for parity-based error checking Good for redundancy.
  - RAID 5
    - Block stripped with error check
      - Most commonly used. Stripes data and parity checks across multiple drives; increased reliability and speed.
  - RAID 10
    - Stripe of Mirrors
      - Combines striping and mirroring
## Section 3.9
### Physical Controls
  - Lighting: enables people to observe activities and conditions that are incorrect.
  - Signs: tell people where they are permitted
  - Alarms: alert us when somethign is going wrong.
  - Barricades: prevent access from unautherized parties.
  - Fencing: physical barrier.
  - Cage: Fencing inside.
  - Gate: access to caged or fenced area.
  - Bollard: those polls that stop cars.
  - Security Guard: man who does the secure
  - mantraps: area where you have to authenticate one time to enter mantrap, and authenticate again to get out of mantrap.
  - Tokens or Cards: built into badges to be tied to automatically checking and logging
  - Air Gap: system that is physically and logically separated.
  - Faraday cages: prevent EMI. encrlosures of grounded conductive material usually room size, to block emissions.
  - TEMPEST: DOD program desinged to keep emissions inside the facility and to prevent eavesdropping of sensitive informatin.
  - Camera systems: need to be secured themselves because anything can be attacked.
  - Motion Detectors: used in areas with little or no traffic to alert security personnel of unauthrozed activity.
  - Logs: should always be kept:
  - Safes: allow us to store items.
  - bump key: cut with all the notches as maximum depth, the key is inserted inot a lock and then struck, bouncing the lock pin which can openthe locks.
  - HVAC (Heating ventilating and air contidioning)
  - Hot and cold aisles: maintain temperature in server area, place servers in specific areas where temperature is easier to keep constant.

## Section 4.1 Identity and Access management Concepts
### Identification, authentication, Authorization, and Accounting (IAAA)
 - Identification: Assigning a user or system a unique name.
 - Authentication: Verifying the identity
 - Authorization: process of permitting or denying access to a resource based on identity.
 - Accountability: maintaining logs to keep track of people accessing data they are allowed to and policies being followed.
 - Multifactor Authentication (MFA): using multiple forms of authentication.
    - Biometrics
    - Tokens (badges)
    - Passwords:
    - location
    - Physical Activity that you perform that only you would know.
  - Single-Sign-On(SSO): authenticae credentials between systems. Signing in only signs in to a single system and not all at once.
  - federation: linking a user's identity across multiple distinct systems across different enterprises.
  - Transitive Trust: Trust that follows transitive property, If A Trusts B and B Trusts C then A must Trust C.
## Section 4.2 Installtion and Cofniguration of Identity and Access Services
### Define Different identity and access service types

### Identity and access services part 2

## Section 4.3 Identity and Access Management Controls:

### Identity and Access MAnagment Controls

## Section 4.4 Common Account MAnagment PRactices

### Account Management
  - Process of ensureing users have the privileges needed to perform their base job functions.
    - Least Privileges: bare minimum permissions needed.
    - Onboarding and Offboarding: processes in place to add and remove personnel from an organization team.
      - Onboard people to give permissions if more are needed.
      - Offboard if they move and dont need any of the older permissiosn.
    - Time of DAy restrictions: Time Synchronization with account permissions.
  - Tombstones: deleted account after firing even though logs of user still exist.
### Account Policy Enforcement
  - Not much beyond common sense or logical thinking

## Section 5.1 Organizational Security Policies, Plans and policies

### Personnel Management
  - Background Investigations: check background for any unideal employees who have a lower chance of a leak. Credit reports and law enforcement inquiries.
  - Onboarding needs to happen as soon as new hires are introduced with training.
  - Role-Based Security Awareness Training: each person has their own responsibility.
    - Data Owner: Ultimately responsible for the security of the Data
    - System Administrator: Enables the use of the system, through some administrative configurations.
    - System Owner: oversees the configuration settings of the system to ensure that they comply with the data owner's requirement.
    - Users: regular users with minimum acccess.
    - Privileged Users: have a a little more access.
    - Executive users: High level users, CEOs, managers, etc.
    - Acceptable Use Policy: aka Rules of Behavior. Outlines what the corporate network and systems should be used. Part of it should be general security policies such as prohibiting the use of social media or persnal email.
    - Continuaing Education: Regular training to maintain secure work area, especially for new patches and updates.
  - Adverse Actions: In some cases, Admin actions must be taken against an employee. it is imperative to maintain the documentation for such users.
  - Many Personel Management policies should be in place:
    - Clean Desk
    - Mandatory Vacation and Job Rotations: help prevent malicious activies like fraud. Help identify weaknesses and ineffiencies in processess as they allow other employees to undertake work previously performed by a single employee.
    - Separation of Duties: Another method used to prevent fraud. Multiple people needed for a secure job.
    - Exit Interview
  -

### Agreement Types
  - Standard Operating Procedures: ensure day-to-day functions
    - can be used as evidence by auditors that a company is meeting requirements.
  -  Agreements: connectivity to some third-party
    - Business PArtner Agreement (BPA): partners or organizations who have vested interest in the success of the other. in a addition to the nature of the business the BPA should also outline the roles and responsibilities in the partnership.
    - Service Level Agreement (SLA): breaks down minimum terms of a service.
    - Interconnection Security Agreement (ISA): employed by the US federal Government when systems controlled by separate entities interconnect. outlines security controls that affect each of the connections between those systems
    - Memorandums of Understanding (MOU) Memorandums of Agreement (MOA)
    - MOU: describes broad concepts of understandings, goals, and plans, shared by the organizations involved, **not a legal document**.
    - MOA: Outlines responsibilities of each organization, legally binding contract, must be signed, less formal than a full contract but still binds the company.

## SEction 5.2 Concepts from a Business Impact Analysis

### Business Impact Analysis
  - BIA is a process that determines and evaluates the impacts to operations that could arise due to the results of a disaster, accident, or emergency.
    - comprisd of several roles and fucnctions with the organization.
    - Elemnts of BIA:
      - Identifying mission essential functionalitie:
        - Do we know what services our customer expects to be available always?
        - Do we know what services our employees need available at all times?
        - Indentify the critical systems
      - Determine Impacts: of mission essential functionalities.
        - Life (dont cause death due to loss of functionality, ie hospital care.)
        - Property
        - Safety
        - Financial
        - Reputation
      - Privacy Threshold Assessment (PTA): process conducted to determine what levels of information a system is collecting to determine inf a PIA is required.
      - Privacy Impact Assessment(PIA): impact assessment where processes of a system are audited to determine if there are failures in these processess that might cmopromise a PII(Personally identifiable information)
        - designed to evaluate the protections of a system to ensure privacy risks are propler mitigated.
      - Recovery Point Objective (RPO)
        - maximum amount of time a company can assume that a backup is still considered good
      - Recovery Time Objective (RTO)
        - Duration of time in which a service must be restored after a disaster.
      - Mean Time Between Failures (MTBF)
        - measurement of time between the time a device was repaired and the time it next fails
      - Mean Time to Repair (MTTR)
        - measuring the average time to repair a failed component or device.

## Section 5.3 Risk Management and Processes and Concepts

### Risk Management
  - Threat Assessment: identify potential threats and assign probabilities
  - Environmental Threats: identify Environmental threats to determine the likely ones based on their geography
  - man-made threats: includes cyber-crime, as well as accidents.
  - Quantifying Risks:
    - Single Loss Expectancy: How much we except each individual event to cost our organization.
    - Annual Rate of Occurance (ARO): how often this even is likely to happen.
    - Annual Loss Expectancy:
      - ARO x SLE = ALE
      - excepted cost to our organization due to these events eacy year.
  - Risk Response Techniques:
    - Always consider which to employ based on investment.
    - Accepting a Risk: acknowledge risk exists but potential loss is not great enough to warrent spending money to avoid it.
    - Transferring a risk: transfer risk from one org to another such as insurance.
    - Risk avoidance: eliminating elements that expose our org to risks.
    - Risk Mitigation: taking steps to reduce the adverse effects of a particular risk.

## Section 5.4 Incident Response

### Incident Response Concepts
  - Incedent Response (IR): approach to addressing and managing the aftermath of a security breach or cyber attack.
    - handle the situation in a method which limits damage and recovery time and cost.
    - there will be incidents
  - Incident Response Planning: must categorize risk. NIST has a set of categories for risks.
      1. External Removable Media
      2. Attrition
      3. Web
      4. Email
      5. Improper Usage
      6. Loss or Theft of Equipment
      7. Other
    - Roles and Responsibilities:
      - Incident Response Team: trained and tested for Incidence response.
      - Security Management: help lead response team during planning and carryin gout IR procedures.
      - Compliance Officers: Having detailed knowledge of compliance rules and procedures,
      - Technical Staff: Determine the details of the cyber incidents.
      - Cyber Incident Response Team (CIRT): predefined experts that an org can reach out to during incident handling
    - Exercises:
      - Tabletop exercise: discuss what steps to take during a given scenario.
    - Process:
      - Preparation -> Identification -> Containment -> Eradication -> Recovery -> Lessons Learned -> Preparation
## Section 5.5 Digital Forensics

### Digital Forensics
  - Branch of forensic sciences encompassing the recovery and investigation of material found in digital devices.
  - Volitality: memory not being permanent, a specific order is made so you dont lose any data.
    - Data stored in the CPU cache and data stored in RAM (volatile) should be first
    - archived and backed up data should be collected last.
    - Data volatile to least:
      1. CPU cache and registers
      2. Remaining data stored in RAM, system stats, ARP cache, etc.
      3. Temporary file systems.
      4. Files written to a disk.
      5. Remote monitoring data from that system.
      6. Archived data.
  - Collecting Evidence:
    - Capture system images.
    - network traffic and logs
    - Capture video
    - Screenshots
    - witness interviews
    - capture any hashes of the systems so that we know it remains unaltered during investigation.
  - Chain of custody: document everyone who comes in contact with evidence or information.
  - Preservation: ensure we preserve all data we collect, never remove anything.
  - Legal Hold: courts rule evidence inadmissable if there is a lack of documentation demonstrating adequate control.
    - Legal hold - documentable process in place for an ongoing preservation.
  - Recovery:
    - Strategic Intelligence: did we discover soemthing that shows we need to update policies?
    - Counterintelligence Gathering: What did we learna bout the attacker.
    - Active Logging: capture everything.

## Section 5.6 Disaster Recovery and Continueity of Operations

### Disaster recovery and Continuity of Operations.
  - Disaster Recovery: setting policies and procudures in place to recover vital systems after a disaster.
  - Continuity of operations: ensure operations through unanticipated events, such as disasters.
  - Recovery Sites:
    - hot site: separate facility with all of the necessary equipment for operations to continue. Site mirrors production environment with recovery site.
    - Warm site: similar to hot site, need data to be restored before operations can resume. does not mirror the production.
    - Cold sites: Secondary sites, nothing is installed, configured, or established, take a lot of effort to get operations online. very cheap to use but could take days to get things back up after a disaster.
  - Backup Types:
    - Full backup: makes an archived copy of every file selected for backup.
    - Differential backup: make copies of files that have cahgned since last full backup.
    - Incremental backup: copy files that have changed since last backup, whether it was full or incremental.
    - snapshots: backups of vms.
  - Continuity of Operations Planning: During Planning is when we identify and communicate our alternate processing sites and business practices.
    - folow practices similar to IR.
    - always learn from action reprots.
  - Geographic Considerations
    - Off-site Storage
    - Distance
    - Location Selection
    - Legal Implications
    - Data Sovereignty

## Section 5.7 Control Types

### Differentiating Between Control Types
  - Security Controls: countermeasures and safeguards put in place to avoid or minimize loss due to security risks.
  - Control Families:
    - Technical Controls: Technical safegaurds put in place to minimize loss or system downtime due to threats acting on their mathcing vulnerability.
    - Administrative Controls: management usually put in place. Risk assessments, acceptable use policies, and planning are all examples of administrative controls.
    - Physical Controls: are those put in place to deter, detect, and respond to physical threats.
  - Control Objectives:
    - Deterrent
    - Preventive
    - Detective
    - Corrective

## Section 5.8 Data Security and Privacy Policies

### Data Security and Privacy Practices
  - Data Sensitivity: Different Data Types:
    - Public: Data that anyone can view. Does not require security safegaurds.
    - Proprietary Information: the property of the organization. Like trade secrets, and information unique and important to the company.
    - Confidential: requires restrictive access, sharing information requires a Non-Disclosure Agreement (NDA).
    - Private: Personal information that we should protect extensively there are two types:
      - **Personal Identifiable Information(PII):** data that could potentially identify a specific individual, like SSN or Drivers license.
      - **Personal Health Information(PHI):** Any data about health status, provision of health care, or payment for health care that can be linked to a specific individual.
  - Data Roles:
    - Data Owner: senior management that owns all the data in storage, but dont carry out the protection of the data.
    - Data Stewards or Custodians: are responsible for the accuracy, privacy, and security of the data. this individual is responsible for ensuring compliance with any laws or standards as it pertains to that data as well as managing access and implementing security.
    - Privacy Officer: Responsible for the organization's data privacy. Implement policies and procedures to carry out the privacy controls.
  - Data Retention: keep certain data for specified amount of time. because:
    - Version Control: many times when we need to recover a previous configuration after changes are made. Maintaining previous file versions allows us to do so.
    - Recover from Cyber Attacks: Recover to a time before attack in order to prepare for attacks.
    - Legal/Regulatory compliance: there can be industries that legally must maintain records of events.
  - Data Destruction and Media Sanitization Techniques
    - Burning
    - Shredding
    - Pulping
    - Pulverizing
    - Degaussing
    - Purging
    - Wiping
## Section 6.1 Basic Concepts of Cryptography
### Basic Concepts of Cryptography P1
  - Cryptography - Kryptos: secret Graphein: Writings
  - Objectives of Cryptography: PAIN
    - Privacy: ensure those things that should stay confidential, remain private.
    - Authentication: help us prove individuals are who they say they are. without showing everyone the steps or answers taken.
    - Integrity: can assure that data is accurate and complete and no unauthorized individuals have altered teh data.
    - Nonrepudiation: In transactional exchanges cryptography provides both the sender and receiver assurance of the other's status in the transaction.
  - How does Cryptography Work
    - Data in Transite: Data being passed between multiple entities.
      - How is the data being sent
    - Data in Rest: Inactive data that is stored in any form.
      - How is data displayed when its not in transit?
      - How accessible is it?
    - Data in Use: assure that our data remains private and maintains its integrity.
  -  History of Cryptography:
    - Steganography: hiding a message in a message
    - Obfuscation: hide something by making it harder to read while still being able to get the original message.
      - Caesar's Cipher

### Basic Concepts of Cryptography P2
  - Ciphers: keys used to encrypt or decrypt data, two types of ciphers:
    - Block: encrypt and decrypt whole chunks or blocks of data.
      -
    - stream: ciphers are used to break the data into bits and encrypt each bit.
    ||Stream|Block|
    |Advantages| Speed Low Error Propagation||High Diffusion and Immune to insertion
    |Disadvantages|Low diffusions and susceptible to insertions| slow to encrypt and error propagation|
  - Hashes: encrypts data but is not meant to be encrypted. but the way it is encrypted is always the same.
    - Hashes are commonly hashed in a specific size, MD5-128bits where SHA-256 is 256bits
  - Encryption Algorithms:
    - Symmetric: Uses same key to encrypt and decrypt
      - DES, AES, 3DES
    -Asymmetric: uses 2 keys, public and private, to encrypt one and decrypt on the otherside.
      - RSA, DSA, Eliptical curve
  - Confusiong: Making a relationship between encrypted data and the cipher as complex as possible.
  - Diffusion: process of shifting bits of data throughout the encryption process. as bits of the plaintext shift, then ehalf of the bits of ciphertext should change. So if there is no correct key there cannot be any reverse engineering.
  - Substituion: replacement of certain bits of the Data following a set of rules.
  - Permutation: manipulation of the order of the bits according to the rules.
  - Obfuscation: making something obscure, unclear, or unintelligible.
    - Ciphers are Obfuscation

## Section 6.2 Basic Characteristics of Cryptographic Algorithms
### Symmetric Algorithms
  - use the same key for encryption and decryption
  - DES(Data Encryption Standard): first commonly used symmetric algrothm, uses 64 bit key, but 8 bits are used for parity, so the key is 56 bits.
  - 3DES (Triple DES):
    - Encrypts with 112 or 168 (DES only uses 56 bits) bits, depending on the number of keys used:
      - DES EEE2: uses 2 keys, encryption process happens three times, alternating keys.
      - DES EDE2: uses 2 keys, first is used twice, encrypt-decrypt-encrypt
      - DES EEE3 uses 3 keys, encryption happens 3 times, each time with a different key.
      - DES EDE3: uses 3 Keys, operates by Encrypting, Decryption, Encrypt
  - AES (Advanced Encryption Standard):
    - Replaced DES in 2002 via NIST,
    - Rijndael was chosen as replacement, which became AES.
    - can be deployed with key sizes of 128, 192, or 256 bits.
  - RC4 (Rivest Cipher):
    - Family of ciphers developed by Ron Rivest. One of the founders of RSA.
    - Fast stream cipher, suited for Wi-Fi Equivalent Protection (WEP).
    - 40-bit in length but is paired with a 24-bit IV to create a 64-bit WEP.
  - Cipher Modes:
    - Counter Mode (CTR)
      - Encryption mode carried out by turning a block cipher into a stream cipher and then adding a counter to the process.
      - The counter is a function which produces a sequence that will not repeat for a long time.
      - Combined wiht an IV to produce input into a symmetric key block cipher.
      - Data is then encrypted with Symmetric block cipher.
    - Electronic Codebook(ECB)
      - Native encryption mode of DES.
      - if last block is not full, padding is added to make the clear text a full block.
      - Produces highest throughput but is easiest form to break.
    - Galois/Counter Mode (GCM):
      - authentication mode, using Galois Multiplication.
      - combines counter mode, with Galois Authentication.
      - Used specifically for 128 block encryption.
    - Cipher Block Chaining (CBC)
      - Widely used and very similary to ECB
      - Processes 64-bit blocks of data but inserts some of the ciphertext created in each block into the next block. This is called chaining.
      - comes with slightly higher error rate, as any error in transmissions causes the block to be impossible to decrypt upon receipt.

### Asymmetric Algorithms
  - Diffie Hellman:
    - First public key algorithm.
    - Allows 2 users to exchange secret key over an insecure medium without any prior secrets.
    - Susceptible to MiTM
  - RSA
    - made by Ron Rivest, Adi Shamir, and Len Adelman.
    - supports key up to 2048 bits.
  - Digital Signature Algorithm(DSA):
    - provides digital signatures.
    - Great for determining the integrity of data, bad with confidentiality.
    - adopted by NIST as their Digital Signature Standard (DSS) as FIPS 186
  - Elliptical Curve Cryptosystem
    - ECC is considered more secure as it is harder to crack based on the discret log problems it employs.
    - Usually defined over finite resources, using only real and rational numbers.
    - fast.
    - requires smaller key to provide equivalent security.
### Hashing Algorithms
  - Operates by taking data an compressing it into a fixed length value referred to as a hash value.
    - Provides a message digest of the data that allows us to verify that the information has remained unchanged.
  - Message Digest: Most common form of hashing. This is the MD series such as MD4.
    - Ron Rivest Developed the entire MD series
  - MD5: most commonly used hashing algorithm today.
    - Processes a variable-size input and produces a 128-bit output.
  - Secure Hasing Algorithm (SHA): very similary to MD5.
    - SHA-0 and -1 have been deprecated and are no longer recommended.
    - SHA-2 is a family of functions and is a safe replacement.
      - Made up of:
        - SHA-224
        - SHA-256
        - SHA-386
        - SHA-512
  - HMAC (Hashed Message Authentication Code): designed to avoid collision attacks that other hashing algorithms are susceptible to.
    - Uses Shared secret key.
    - uses MD or SHA and then password-protecting it.
    - If attacker gets it they will need to crack both password and algorithm.
    - Requires sender and recipient to share the key through some out-of-band channel.

## Section 6.3 Wireless Cryptography
### Wireless Cryptography.
  - Wep uses RC4 cipher, for authentication and encryption. this is shared with every device on a wireless netowrk. The key is only 40 bits to 104 bit. for about 64 or 128 total bits after initilization.
    - Its so small that its eas yto crack and major companies were hacked because of this. So WPA replaced WEP.
  - WPA (Wi-Fi Protected Access): based on RC4, introduced several enhancements over its predecessor. It uses Temporal Key Integrity Protocol (TKIP) which has:
    - Use of 256-bit keys.
    - Per-packet key mixing.
    - Automatic broadcast of updated keys.
    - Message integrity checker.
    - A larger IV size (48-bits as apposed to the WEP 24-bits.)
  - WPA was designed to be backward compatible with WEP. which helped encourage a quick and seamless adoption. Unfortunately WPA had bad security so now the WPA2 is in charge!
  - WPA2: replaces RC4 cipher and TKIP with 2 stronger encryption and authentication mechanisms.
    - AES and Counter Mode with Cipher Block Chaining Message Authentication Code Protocol.
    - Supports TKIP as a fallback if a device cannot support CCMP.
    - protects data confidentiality by allowing only authorized network users to recieve data. and uses CCMP to ensure message integrity.
    - easier roaming. allowing clients to move from one access point to another on the same network without reauthentication aka preauthentication.
  - Extensible Authentication Protocol (EAP): framework that is sued to create different types of authentication.
    - EAP-FAST(Flexible Authentication via Secure Tunneling): widely deployed EAP method was LEAP(lightweight EAP). LEAP contained some serious security vulnerabilities. so to address these cisco developed EAP-FAST .
      - Addresses these vulnerabilities by performing this Authentication over a TLS tunnel.
    - EAP-TLS: EAP over a TLS connection.
    - PEAP (Protected EAP): sending EAP within an encrypted and authenticated TLS tunnel. Developed by CISCO, Microsoft, and RSA security.
  - IEEE 802.1X: port based network access control:
    - You cannot have access to network resources until you have completed Authentication process.
    - 3 devices involved in authenticaion.
      1. Device Requesting access (workshop)L this is the supplicant.
      2. Switch (Wireless AP) which is the authenticator.
      3. Authentication Server (RADIUS, TACACS, etc.) The authenticator pushes authentication requests to this erver to verify the requestor.

## Section 6.4 Public Key Infrastructure (PKI)
### PKI overview
  - PKI: framework
    - Uses any asymmetric algorithms for communications.
    - Certificates are issued by a trusted Certificate Authority (CA)
    - PKI provides confidentiality, Authentication, Nonrepudiation
      - Authentication is provided via the digital signature of the sender, which is required to send messages.
      - confidentiality is provided through data being encrypted before being transmitted.
      - Nonrepudiation is provided through an assurance that both the sender sent the message and the reciever did in fact, receive the message.
### Types of Certificates
  - Root Certificate: Most important certificate in a PKI enironment. this is the one that identifies the Root CA (Everything in the environment starts with this certificate.)
    - issues other certificates.
  - User Certificates: used to associate a User with a certificate.
    - Acts as a type of digital ID for that User.
    - Can be used as an additional Authentication factor (Something you have)
  - Email Certificates:
  - Web Server SSL Certificates
    - Domain Validation(DV): Certificate, when using, the CA verifies that the applicant has been validated by proving some control over the DNS domain associated with it.
    - Extended Validation Certificate: CA provides additional Verification of the requestors identity to verify that they are the the legal entity controlling the website.
    - Subject Alternate Name (SAN) Certificate: allows you to put a subject alternate name extension, where you can list all of the domain names that would be associated with the certificate.
    - Wildcard Certificates: allow us to break down domains into multiple server names that change parts of the URL using the \*.
  - Internal Certificates:
    - Self-signed Certificates: Access our web server via some external entities, we therefore must pay some third-party CA that is also trusted by those entities. if it was all internal we would not need a third-party to come in.
      - from this we can surmise that because we trust our own internal network we can establish certificates that we sign ourselves.
      - you can do this by adding the certificates on all of the company machines, using it this way means that if someone is connecting from in or outside of the network, we can validate because our certificates are on our machines.
  - Certificate File Types:
    - DER(Distinguished Encoding Rule) common format especially for Java.
    - PEM (Privacy-Enhanced MAil); most common format; ASCII files, easy to read as a human?
    - PFX: Binary format for storing a server certificate. Any intermediate certificates and a private key in one encrypt-able file.
      - PFX is the Windows version of PKCS#12 aka P12
    - CER: in Windows. Contains only the public Key, if you needed to transfer the private key, you would use PFX.
    - P7B: contain only certificates and chain certificates, not the private key.
### Concepts
  - PKI Components:
    - Digital Certificates: link entity with public key. Verify the identity of the linked entity. contains info about the issuer of cert so that the cert itself can be validated.
    - Certificate Signing Request(CSR): first step to obtain an SSL Cert for a web server.
      - when we generate keys on our own server to include CSR, these include info about the org and the server that the CA will then use to generate the SSL cert.
    - Certificate Authority (CA): He who issues digital certificates. Certs issued by the CA are generally trusted by any entity that has an established trust relationship with that CA.
    - Certificate Revocation List(CRL) certs that are actively rejected  by CA.
    - Online Certificate Status Protocol (OCSP): check the status of certs. OSCP traffic is sent via HTTP, servers verify the status of requested cert. allows systems to verify that cert have not been added to the CRL.
  - PKI Concepts
    - Stapling: process of appending a time-stamp response signed by the CA, so that clients dont need to contact teh OCSP during every TLS handshake.
    - Pinning: tells web client to associate a specific public key with a certain web server to decrease the risk of man-in-the-middle attack with forged certs
    - Key Escrow: arrangement where keys needed to decrypt encrypted data are held in escrow, so that under certain circumstances, an authorized party may gain access to those keys.
    - Certificate Chain: ordered list of certs that contain an SSL cert and CA that enable the reciever to verify that the sender and all CA's are trustworthy.
