# STATUS

## Project Overview
Agents & Skills Starter Kit — a library of 26 Claude Code agents and 47 skills for bootstrapping new projects.

## Current State
- All agents defined and consistent with CLAUDE.md listing
- Skill registry (v1.1.0) covers 15 categories + 5 universal skills
- Deprecated skills cleaned up (dask, geopandas, market-research-reports, theme-factory, web-artifacts-builder, document-skills/)
- Orphaned agent-memory directories removed (full-stack-dev, iot-embedded-engineer)
- Project templates defined for 8 common project types
- Validation script available at scripts/validate.sh
- Skill template documented at .claude/skills/SKILL-TEMPLATE.md
- Individual skills versioned (v1.0.0)

## Active Tasks
- None

## Key Decisions
- Universal skills (5) are always included for every agent
- cto-orchestrator + project-manager + docs-generator are always included for new projects
- Skills use semantic versioning in SKILL.md frontmatter
- Deprecated skills are deleted from disk, recorded only in SKILL-REGISTRY.md

## Blockers
- None
