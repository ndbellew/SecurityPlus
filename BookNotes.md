# Notes.md
# Nathan Bellew

# Chapter 1

## Security+ Terms

  - **Acceptable use policy/rules**
    - of behavior Agreed-uponprinciples set forth by a company to govern how the employees ofthat company may use resources such as computers and Internetaccess.
  - **annual loss expectancy (ALE)**
    -  A calculation used to identifyrisks and calculate the expected loss each year.
  - **annualized rate of occurrence (ARO)**
    -  A calculation of howoften a threat will occur. For example, a threat that occurs onceevery five years has an annualized rate of occurrence of 1/5, or 0.2.
  - **asset value (AV)**
    -  The assessed value of an item (server, property,and so on) associated with cash flow.
  - **business impact analysis (BIA)**
    -  A study of the possible impactif a disruption to a business’s vital resources were to occur.
  - **business partners agreement (BPA)** An agreement betweenpartners in a business that outlines their responsibilities,obligations, and sharing of profits and losses.
  - **exposure factor (EF)**
    -  The potential percentage of loss to anasset if a threat is realized.
  - **interconnection security agreement (ISA)**
    -  As defined byNIST (in Publication 800-47), it is “an agreement establishedbetween the organizations that own and operate connected ITsystems to document the technical requirements of theinterconnection. The ISA also supports a Memorandum ofUnderstanding or Agreement (MOU/A) between theorganizations.”
  - **maximum tolerable downtime (MTD)** The maximum period of time that a business process can be down before the survival ofthe organization is at risk.
  - **mean time between failures (MTBF)** The measurement of theanticipated lifetime of a system or component.
  - **mean time to failure (MTTF)** The measurement of the averageof how long it takes a system or component to fail.
  - **mean time to restore (MTTR)** The measurement of how long ittakes to repair a system or component once a failure occurs.
  - **memorandum of understanding (MOU)/memorandum ofagreement (MOA)**
    -  Most commonly known as an MOU ratherthan MOA, this is a document between two or more partiesdefining their respective responsibilities in accomplishing aparticular goal or mission, such as securing a system.
  - **recovery point objective (RPO)**
    - The point last known gooddata prior to an outage that is used to recover systems.
  - **recovery time objective (RTO)**
    - The maximum amount of timethat a process or service is allowed to be down and theconsequences still to be considered acceptable.
  - **Redundant Array of Independent Disks (RAID)**
    -  A configuration of multiple hard disks used to provide fault toleranceshould a disk fail. Different levels of RAID exist.
  - **risk**
    -  The probability that a particular threat will occur, eitheraccidentally or intentionally, leaving a system vulnerable and theimpact of this occurring.
  - **risk acceptance**
    - A strategy of dealing with risk in which it is decided the best approach is simply to accept the consequencesshould the threat happen.
  - **risk analysis**
    - An evaluation of each risk that can be identified.Each risk should be outlined, described, and evaluated on thelikelihood of it occurring.
  - **risk assessment**
    - An evaluation of the possibility of a threat or vulnerability existing. An assessment must be performed before any other actions—such as how much to spend on security in termsof dollars and manpower—can be decided.
  - **risk avoidance**
    -  A strategy of dealing with risk in which it isdecided that the best approach is to avoid the risk.
  - **risk calculation**
    - The process of calculating the risks that exist interms of costs, number, frequency, and so forth.
  - **risk deterrence**
    - A strategy of dealing with risk in which it isdecided that the best approach is to discourage potential attackers from engaging in the behavior that leads to the risk.
  - **risk mitigation**
    -  A strategy of dealing with risk in which it isdecided that the best approach is to lessen the risk.
  - **risk transference**
    -  A strategy of dealing with risk in which it isdecided that the best approach is to offload some of the riskthrough insurance, third-party contracts, and/or shared responsibility.
  - **service-level agreement (SLA)**
    - An agreement that specifiesperformance requirements for a vendor. This agreement may usemean time before failure (MTBF) and mean time to repair (MTTR)as performance measures in the SLA.
  - **single loss expectancy (SLE)**
    -  The cost of a single loss when itoccurs. This loss can be a critical failure, or it can be the result ofan attack.
  - **single point of failure (SPOF)**
    -  A single weakness that iscapable of bringing an entire system downvulnerability A flaw or weakness in some part of a system’ssecurity procedures, design, implementation, or internal controlsthat could expose it to danger (accidental or intentional) and resultin a violation of the security policy.
  - **Vulnerability**
    - A flaw or weakness in some part of a system's security procedures, design, implementation, or internal controls that could expose it to danger (accidental or intentional) and result in a violation of a security policy.

### Threat Assessment
  - Important to identify threats, three types of threats:
    - **Environmental**
      - Bad weather like hurricanes, or just some simple flooding like heavy rain.
    - **Manmade**
      - A threat that could appear to be environmental but actually manmade, such as fire alarm going off without a fire present.
    - **Internal vs. External**
      - threat made by someone who is within the company or an outside threat.
  - Risk Register - scatterplot of possible problem areas.
### Risk Assessment
  - Also known as risk calculation
  - Deals with the threats, vulnerabilities, and impacts of a loss of information-processing capabilities or a loss of information itself.
  - Conventional threats and risks are often too limited when considering risk assessment.
  - Chief components of risk assessment:
    - **Risks to Which the Organization Is Exposed**
      - Develop scenarios that can help you evaluate how to deal with these types of risks if they occur.
      - Create a plan to deal with risks that could happen to an OS, server, or application in certain environments
    - **Risks that Need Addressing**
      - Provides reality check on which risks are real and which are unlikely.
      -
    - **Coordination with BIA**
      - Business Impact Analysis
#### Computing Risk Assessment
  - ensure prioritization.
  - Not everything should be weighed evenly, because some events have a greater likelihood of happening.
#### Risk Calculations
  - SLE x ARO = ALE
  - Calculate ALE to ensure the cost of a fix is within company standards.
  - Key to any risk assessment is identifying assets and threats.
#### Quantitative vs. Qualitative Risk Assessment
  - Quantitative: Cost-based and objective
    - does the damage effect productivity
  - Qualitative: opinion-based and subjective
    - does the damage affect company politics.
  - SLE, ARO, and ALE are apart of Quantitative
#### Risk Measurements
  - Service Level Agreement (SLA)
  - Key terms:
    - likelihood
    - Threat Vectors
    - Mean Time Betwen Failures
    - Mean time to Failure
    - Mean Time to Restore
    - Recovery Time Objective
    - Recovery Point Objective
