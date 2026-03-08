---
name: dependency-security
description: Dependency auditing. CVE scanning, SBOM, lock files, container image scanning.
---

# Dependency Security

## Automated Scanning (CI)
```yaml
# Python
- run: pip-audit --requirement requirements.txt
# Node
- run: npm audit --audit-level=high
# Container
- run: trivy image myapp:latest --severity HIGH,CRITICAL
```

## Best Practices
- Pin exact versions in lock files (requirements.txt, package-lock.json)
- Enable Dependabot/Renovate for automated PRs
- Generate SBOM for compliance (cyclonedx-bom, syft)
- Review transitive dependencies, not just direct

## Severity Response
| Severity | Action | Timeline |
|----------|--------|----------|
| Critical | Patch immediately, deploy hotfix | <24 hours |
| High | Patch in next sprint | <1 week |
| Medium | Schedule update | <1 month |
| Low | Track, update when convenient | Next release |

## Key Libraries
pip-audit, npm audit, Trivy, Snyk, Dependabot
