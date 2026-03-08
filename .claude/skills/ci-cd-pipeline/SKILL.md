---
name: ci-cd-pipeline
version: 1.0.0
description: CI/CD pipeline design. Lint, test, build, scan, deploy with environment promotion and rollbacks.
---

# CI/CD Pipeline

## Standard Stages
```
lint -> test -> build -> security-scan -> deploy-staging -> approve -> deploy-prod
```

## GitHub Actions Example
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: pytest --cov=src --cov-report=xml
  build:
    needs: test
    steps:
      - run: docker build -t app:${{ github.sha }} .
      - run: docker push app:${{ github.sha }}
```

## Container Image Tagging
- `app:v1.2.3` (semver release)
- `app:<git-sha>` (every build)
- `app:latest` (staging only, never production)

## ML-Specific Additions
- Model validation gate: accuracy threshold before registry promotion
- Data validation: schema checks on training data
- GPU test runner for model inference tests

## Rules
- Manual approval gate for production deploys
- Rollback mechanism: keep N-1 version ready
- Never skip security scanning

## Key Libraries
GitHub Actions, GitLab CI, Docker, Kubernetes
