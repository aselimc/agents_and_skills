---
name: code-quality-standards
version: 1.0.0
description: Org-wide code quality standards for linting, formatting, type safety, and error handling.
---

# Code Quality Standards

## Python
- **Type hints** on all public functions
- **Linting**: `ruff check .` (replaces flake8+isort+pyupgrade)
- **Formatting**: `ruff format .`
- **Type checking**: `mypy` or `pyright` in strict mode
- **No bare `except`** - always catch specific exceptions
- **No magic numbers** - use named constants or config

## JavaScript/TypeScript
- **TypeScript strict mode** (`"strict": true`)
- **Linting**: `eslint`
- **Formatting**: `prettier`

## Rust
- **Linting**: `clippy`
- **Formatting**: `rustfmt`

## Universal Rules
- Meaningful variable names (no single-letter except loop indices/lambdas)
- Config-driven design: dataclasses/hydra (Python), typed schemas (TS)
- Module-boundary functions/classes must have docstrings/JSDoc
- Internal helpers need not be documented
- Structured error handling with context messages
