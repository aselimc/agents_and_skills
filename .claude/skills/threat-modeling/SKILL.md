---
name: threat-modeling
version: 1.0.0
description: STRIDE threat modeling. Attack surfaces, trust boundaries, severity ratings, ML-specific threats.
---

# Threat Modeling

## STRIDE Methodology
| Threat | Description | Mitigation |
|--------|------------|------------|
| **S**poofing | Pretending to be another user/service | AuthN, certificates |
| **T**ampering | Modifying data in transit/at rest | Integrity checks, signing |
| **R**epudiation | Denying actions | Audit logs |
| **I**nformation Disclosure | Unauthorized data access | Encryption, access control |
| **D**enial of Service | Making service unavailable | Rate limiting, scaling |
| **E**levation of Privilege | Gaining unauthorized access | Least privilege, RBAC |

## Process
1. Identify attack surfaces and trust boundaries
2. Map data flows between components
3. Apply STRIDE to each data flow
4. Rate severity: likelihood x impact (Critical/High/Medium/Low)
5. Prioritize mitigations by severity

## ML-Specific Threats
- **Model extraction**: API queries to reconstruct model
- **Adversarial inputs**: crafted inputs to fool model
- **Data poisoning**: corrupted training data
- **Prompt injection**: malicious input to LLMs

## Tools
OWASP Threat Dragon, Microsoft Threat Modeling Tool
