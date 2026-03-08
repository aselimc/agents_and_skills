---
name: git-workflow
version: 1.0.0
description: Standard git workflow conventions for branching, commits, and PRs. Apply to all code changes.
---

# Git Workflow

## Branch Naming
- `feat/<description>` - New features
- `fix/<description>` - Bug fixes
- `refactor/<description>` - Code refactoring
- `docs/<description>` - Documentation changes
- `test/<description>` - Test additions/fixes

## Commit Messages (Conventional Commits)
```
<type>: <short description>

[optional body]
```
Types: `feat`, `fix`, `chore`, `docs`, `test`, `refactor`, `perf`, `ci`

## PR Conventions
- Descriptive title under 72 chars
- Link related issues
- Include summary of changes and test evidence
- Squash-merge to main

## Rules
- Branch from `main`
- Never force-push shared branches
- Tag releases with semver (vMAJOR.MINOR.PATCH)
- Keep commits atomic (one logical change per commit)
