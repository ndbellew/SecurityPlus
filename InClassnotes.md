# Security+
# Nathan Bellew

## Big Stack

## Chapter 1
,,,

*Hierarchy of Standard Documents*

  Two types of Documents:
    *Strategic
      Policy and Guidlines
    *Tactical
      Procedures, Processes, Tasks.
*Developing Policies, Standards, and Guidelines
  Implementing Policy
    Policy can be legal status, work status, or team status.

*Key Areas of Good Policy*
  __Scope Statement__
    The statement describing who this is for and to what extent.
  __Policy Overview Statement__
    Goal of the policy, why it's imporant and how to comply
  __Policy Statement__
    Needs to be clear and unambiguous
  __Accountability Statements__
    Who holds accountability in regards to the policy, Who to contact if a problem is discovered.
  __Exception Statement__
    Guidance if procedure or process deviates from policy.
REVIEW: 5 points of the Policy
  1. Scope and Purpose
  2. Roles and Responsibilities
  3. Reference
  4. Performance Criteria
  5. **Maintenance** and Administrative Requirements
*Following Guidelines*
  Help an organization implement or maintain standards by providing information on how to accomplish policiers and maintain standards.
  Four Minimum Contents of Good Guidelines
    1. Scope and Purpose
    2. Roles and Responsibilities
    3. Guideline Statements
    4. Operational Considerations
*Business Policies* Primary Areas of Concern
  - Mandatory Vacations: Protects from Theft and allows people the review to ensure the employee isn't performing illegal tasks.
  - Job Rotation: Helps with employee threats
  - Seperation of duties: same as above.
  - Clean Desk: protects vital information from prying eyes of other employees.
  - Background Checks
  - Nondisclosure
    - Ensure you don't do anything on a computer that is owned or used by the company, also ensure that you attempt not to access data from an insecure computer.
    -
  - Onboarding
  - Continuing education
  - Exit interviews
  - Role-based awareness
  NOTE: Do not delete accounts instead disable them in order to maintain their history.
*Business Policies Primary Areas of Concern Continued*
  - Acceptable Use Policies (AUP)
  - Adverse Actions
  - General Security Policies
  - Network/Application Policies
*Measuring and Weighing Risk
  False Positive:
    event that shows as incident but isnt.
    Overtuned
  False Negative:
    Should be an event that slips through.
    Often referred to as Zero-Day hacks.
  Risk Management Best Practices:
    Business Impact Analysis (BIA)
## Chapter 2
  ,,
*Framework*
    Abstraction - Large Collection
      - Software that provides generic functionality
      - That is selectively changed by additional user-written code
      - Thus providing application-specific software that can have its "Behavoir" altered.
        - By the presence of some additional text
          - inject text as config data or source code in order to communicate with the framework.
          -
    - Add some metadata to config file.
    - Loose coupling is Good
    - Simply inject some Metadata (attribute class) and signal item from that Framework to some config items.
*Frameworks, best practices and Config Guidse*
  - ISO standards
  - North American Electric Reliability Corporation (NERC)
  - National institute of Standards and Technology (NIST)
  - ISA/IEC-62443
    - Series of STandards, Technical Reports and Related information that define procedures for IACS.
  - Payment Card Industry Data Security Standard (PCI-DSS)
      - This is primarily handled by Machine Learning via variaties of statistics.
    - Build maintain a Secure network.
    - Protect cardholder data.
    - Maintain a vulnerability management program.
    - Reguralrly monitor and test networks.
    - Maintain a vulnerability managment program.
      - Occurs twice, this is called a feedback adjustmant loop.
  - OWASP (Open-Web-App. Security Project)
  - SEI (sei.cmu.edu)
*Open WebApplication Security Project* OWASP
  - Verify for Security Early and Often
  - Parameterize Queries
    - refers to database query, protecting against SQL injection or NoSQL injection.
    - Sending a SQL Text Command to retrieve data - Use Framework objects to build the binary (optimized) into the code at build time.
  - Encode data
  - Validate All Inputs
    - Knowing what to do with Out of Band Data
  - Implement Identity and Authentication Controls
  - Implement Appropiate Access Controls
  - Protect Data
  - Implement Logging and Intrusion Detection
  - Leverage Security Frameworks and Libraries
  - Error and Exception Handling
11 Biggest Threats to Online Security
  1. Malware
  2. Phishing
  3. Pharming
## Chapter 3

## Chapter 4
  Login = Identification + Authentication + Authorization (bare minimum in order left to right)
  Special Protocols have evolved over the years.
    All SW evolves/changes over time.
    They started out - simple and easy.
      Never needeed anything complex.
    The original Handshake was simplistic
      Password and the handshake was in total clear text - most early prototypes were origin implemented as text.
        Point to Point WAN network prototype called PPP
      The password was not encyrpted for a long time.
  Hash is a cryptographic prototype but it is not an encryption.
    Great uniqueness to the hash number.
    Managing the assocation of the hash
    PAP - Password Authentication Protocol. - using PPP to validate users.
    SPAP - Secured PAP for MS email clients, microsoft specific.
    CHAP - start of the 3-way handshake. Challenge Authentication Protocol
      - using the limited information they would build a formula from encrypted data, if it works then the handshake was completed.
  Encryption to make it provatge (Confidentiality) - but you also hash to gaurentee no error in transmission.
  Hashes
    NTLM:
      V1. MD4 using DES - The weakest thing you could use.
      V2. Uses HMAC (Hashed Message Authentication Code) and MD5 which was stronger (relies on more than just Challenge and Password by adding "BLOB")
        - now uses SHA-256
        - This was the addition of the digital signature
          - Unique ID is involved - providing the Unique ID along with all the authentication
      Layer 2 = 802.1X-EAP prototype Suite.
        - VPNS are secure because this level of hashing occurs at L2 instead of L4
  B2B - Business 2 Business the new Extranet which is generally on a VPN.
  Security on the network is a minimum 2-fold
    a. AUTH privacy and strength
      - Be able to strongly identify the user and integrity of connection
    b Payload privacy and strength
      - may not be needed so long as authentication is successful.
  **EAP** Network Authentication very important.

  Overexposing the most critical control server - LMI access Control
    i neeeeeeeed a different server to handle remote logins on the DMZ that can check (one the remote login server feels safe - secy POLOCIU) => it can check with the internal reources of the LMI that want to access (LDAP/KER = ADDS)
  DMZ in networks.
     1. Bastion
       - Maintains control, veiwing all data, blocking most data into the DMZ, usually a VPN is what gains entrance.
     2. Different Servers used here
       1. **RADIUS** (Remote Authentication Dia in User Access)
          - works as a AAA server (Authentication, Authorization, and Accounting)
          - Remote access coming into the Danger Zone
          - Generally does only the first two A's, The accounting is a standardized reporting activity, meaning it does maintain an event log, a very crude log, for reports but does not stop the DMZ access process.
            - ML/AI to do reports from the event logs
            - LManually  / Daily review those logs, Analyze and build reports.
        2. TACACS/TACACS+/XTACACS
          - CISCO Server built into GW
          - Maintains AAA
          - Everyone in your team that is necessary can have remote access to the LMI
        3. Diamater
          - The other option to server
     3. (Possible) OAUTH
        - Open Authentication Architecture && an Implementation
        - HTTP Based (L7)
          - 2 common carrier prototype on modern networks
            - Bottom half carrier = IP
            - Top half comm - http/s
          - Grants internet users access to websites or applications
            - Without givient them the passwords

  One-Time Passwords (OTP)
    - Many current 2FA authentication Apps generate these.
    - Helps enable Entropy (randomness)
    - Additional Number gen to be used only once with login - additional Authentication
      - Data Value = Have
  SAML(Security Assessment Markup Language)
    - Like all Markup Languages, its based on XML with language specific Tags and attributes.

## Chapter 5 Wireless Vulnerabilities
  Replay attack
    - Sniff and retransmit, leading to a delay in the data transmission.
    - Attacker tries to fool around with the Target gaining access.
    - Attempts to fool target into sharing encryption key
  Rogue Access Points <- Instance
    - Any wireless access point added to your network that has not been authorized.
  Evil Twin Attack <- Act
    - Rogue Access Point that poses as a legitimate wireless server provider.

  Jamming - DOS
    Not a full DOS but a way to stop communication
  WPS
    - Network Security Standard to Create a Secure Wireless home network
    - shortcut:
      - Router has 8digit pin for router.
      - WPS only checks 4/8 on inital connection checks
        - only 11k possible choices.
  BlueTooth: short range high quality data,
    Bluejacking: Sending unsolicited messages over bluetooth connection.
    Bluesnarfing: gaining unauthorized access through a bluetooth connection.

## Chapter 6

  VDI/VDE (Virtual Desktop Interface/Virtual Desktop Environment)
    - desktop virtualization tools
    -
    Helpful Web References:
      - ThreatCrowd
      - OpenPhish
      - OSINT Framework
      - Shodan
        - Service Banners

Password Security:
  What to avoid:
    1. TLA
      - Tech Acronyms in them
