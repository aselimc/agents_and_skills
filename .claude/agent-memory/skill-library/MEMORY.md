# Skill Library Agent Memory

## Registry Location
- **Skill Registry**: `.claude/skills/SKILL-REGISTRY.md` (v1.1.0, updated 2026-03-08)

## Key Decisions

### v1.0.0 (2026-03-08) - Initial Audit
- 9 skills deprecated/removed: geopandas, market-research-reports, theme-factory, web-artifacts-builder, dask, and 4 document-skills/* duplicates
- 14 existing skills retained
- 31 new skills codified across 13 domain categories
- 5 universal skills: git-workflow, code-quality-standards, structured-logging, read-software-docs, config-management

### v1.1.0 (2026-03-08) - Gap Analysis + New Agents
- Gap analysis identified 9 capability gaps
- 2 new agents created: world-model-researcher, research-paper-writer
- 2 new skills added: world-model-implementation, paper-writing
- Remaining 7 gaps addressed as: skills (4), prompt improvements (2), skill extensions (1)

### New Agent Design Rationale
- **world-model-researcher**: Passed all 5 criteria of agent-architect framework. User's core research area (SSL, JEPAs, world models). Unique persona crossing RL + CV + robotics dynamics. No existing agent covers >30%. Model: opus.
- **research-paper-writer**: Passed all 5 criteria. Fundamentally different persona from docs-generator (scientific writing vs code docs). Research org needs dedicated paper writing. Model: opus.
- 7 gaps did NOT warrant new agents: data annotation, LLM eval, video understanding, synthetic data, embedded patterns, GPU cost, API client gen.

### Org Stats
- 26 agents, 47 active skills, 9 deprecated
- User: CS master's, SSL / 2D-3D perception / JEPAs / world models
- Most-reused skills: read-arxiv-paper (8), experiment-tracking (7), pytorch-training-pipeline (6)

### Pending Skills (identified but not yet codified)
- data-annotation-pipeline (MEDIUM-HIGH priority)
- llm-evaluation (MEDIUM-HIGH)
- video-understanding (MEDIUM)
- synthetic-data-generation (MEDIUM)
- embedded-firmware-patterns (MEDIUM-LOW)
