# Skill Template

Use this template when creating a new skill. Copy this structure into a new folder under `.claude/skills/<skill-name>/SKILL.md`.

## Required SKILL.md Format

```markdown
---
name: <skill-id>
version: 1.0.0
description: <One-line description. This appears in the skill registry and Claude Code's skill list.>
---

# <Skill Title>

## <Section 1: Core Pattern or Convention>
- Bullet points or code blocks showing the primary pattern

## <Section 2: Code Example> (if applicable)
```<language>
# Minimal working example demonstrating the skill
```

## <Section 3: Checklist or Rules>
1. Rule/step 1
2. Rule/step 2
3. Rule/step 3

## Key Libraries
<comma-separated list of relevant tools/libraries>
```

## Guidelines

- **Keep it concise**: Target 25-50 lines. Skills are reference cards, not tutorials.
- **Lead with code**: If the skill involves code patterns, show the canonical example first.
- **Use checklists**: Enumerate steps or rules as numbered lists for easy scanning.
- **YAML frontmatter is required**: `name`, `version`, and `description` fields.
- **Version with semver**: Start at `1.0.0`. Bump minor for additions, major for breaking changes.
- **One skill, one concern**: Don't combine unrelated topics. Create separate skills instead.

## Optional Subdirectories

| Directory | Purpose | Example |
|-----------|---------|---------|
| `references/` | Reference docs, papers, or specs | API specs, protocol docs |
| `scripts/` | Helper scripts used by the skill | Linters, generators |
| `assets/` | Static files (templates, configs) | Config templates, schema files |

## After Creating a Skill

1. Add an entry to `SKILL-REGISTRY.md` in the appropriate category section
2. Update the Skill Coverage Matrix with which agents should use this skill
3. Update the Statistics section at the bottom of the registry
4. Run `bash scripts/validate.sh` to verify consistency
