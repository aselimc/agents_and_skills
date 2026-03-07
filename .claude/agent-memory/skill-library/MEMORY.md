# Skill Library Agent Memory

## Registry Location
- **Skill Registry**: `.claude/skills/SKILL-REGISTRY.md` (v1.0.0, created 2026-03-08)

## Key Decisions (v1.0.0)

### Audit Results
- 9 skills deprecated/removed: geopandas, market-research-reports, theme-factory, web-artifacts-builder, dask, and 4 document-skills/* duplicates
- 14 existing skills retained: read-arxiv-paper, read-software-docs, pytorch-lightning, transformers, scikit-learn, matplotlib, citation-management, webapp-testing, docx, pdf, pptx, xlsx, proposal-writer, proposal-reviewer
- 31 new skills codified across 13 domain categories

### Registry Structure
- 5 universal skills (all agents): git-workflow, code-quality-standards, structured-logging, read-software-docs, config-management
- 40 domain skills across: ML/DL Core (5), CV (4), NLP (4), Robotics (4), RL (3), Inference/Edge (3), Full Stack (4), DevOps/MLOps (4), Security (3), QA (3), Scientific Computing (3), Simulation (2), Research/Docs (5)

### Most-Reused Skills
- experiment-tracking: 6 agents
- read-arxiv-paper: 6 agents
- pytorch-training-pipeline: 5 agents
- test-pyramid: 4 agents
- ci-cd-pipeline: 4 agents

### Duplicate Resolution
- document-skills/docx,pdf,pptx,xlsx -> consolidated to top-level versions
- dask -> replaced by high-performance-computing skill (broader scope)

### Org Context
- User: CS master's, expertise in SSL, 2D/3D perception, JEPAs, world models
- Project focus: DL/CV/Robotics research + full-stack dev + academic research + tech entrepreneurship
- 24 agents in org (see SKILL-REGISTRY.md coverage matrix)
