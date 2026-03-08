---
name: secrets-management
version: 1.0.0
description: Secrets handling. Never hardcode. Vault, env vars, rotation, leak detection.
---

# Secrets Management

## Rules
1. **Never** hardcode secrets in source code
2. **Never** commit `.env` files (add to `.gitignore`)
3. **Never** log secrets or include in error messages

## Local Development
```bash
# .env (in .gitignore)
DATABASE_URL=postgresql://user:pass@localhost:5432/db
API_KEY=sk-...
```
Load with `dotenv` (Python) or `dotenv` (Node).

## Production
- HashiCorp Vault, AWS Secrets Manager, or GCP Secret Manager
- Inject as environment variables at runtime
- Rotate credentials on schedule (90 days max)

## Leak Detection (CI)
```yaml
- name: Scan for secrets
  run: gitleaks detect --source . --verbose
```

## Key Libraries
vault, gitleaks, trufflehog, dotenv
