# Agents & Skills Starter Kit

A library of reusable [Claude Code](https://docs.anthropic.com/en/docs/claude-code) agents and skills for bootstrapping new projects.

## What Is This?

This repo contains **26 specialist agents** and **47 skills** organized by domain. When you start a new project, Claude Code uses this library to select the right agents and skills, copies them into your project, and generates a tailored `CLAUDE.md` and `STATUS.md`.

## Quick Start

1. Open Claude Code in this directory
2. Tell Claude what project you want to build:
   ```
   "I want to start a new robotics project at ~/projects/my-robot"
   ```
3. Claude will:
   - Select relevant agents and skills for your domain
   - Present the selection for your approval
   - Create the project folder with `.claude/agents/` and `.claude/skills/`
   - Write a project-specific `CLAUDE.md` and `STATUS.md`

## Repository Structure

```
agents_and_skills/
├── CLAUDE.md                          # Claude Code instructions for this repo
├── README.md                          # This file
├── STATUS.md                          # Current project state
├── .gitignore
├── scripts/
│   └── validate.sh                    # Validates repo consistency
├── .claude/
│   ├── agents/                        # 26 agent definitions (.md files)
│   ├── skills/
│   │   ├── SKILL-REGISTRY.md          # Central catalog of all skills
│   │   ├── SKILL-TEMPLATE.md          # Template for creating new skills
│   │   └── <skill-name>/SKILL.md      # Individual skill definitions
│   └── agent-memory/                  # Persistent memory per agent
```

## Available Agents

| Category | Agents |
|----------|--------|
| **Orchestration** | cto-orchestrator, project-manager, agent-architect, agent-evaluator, skill-library |
| **ML / Research** | computer-vision-engineer, nlp-llm-specialist, rl-engineer, world-model-researcher, scientific-computing, research-paper-writer |
| **Robotics** | robotics-engineer, embedded-firmware-engineer, edge-computing-architect |
| **Infrastructure** | backend-architect, frontend-builder, mobile-app-builder, system-architect, devops-infra-engineer, data-engineer |
| **Quality / Security** | qa-test-engineer, security-guardian, docs-generator, mlops-pipeline, inference-engineer, realtime-sim-engine |

## Available Skills (47 active)

Skills are grouped into 15 categories. See [SKILL-REGISTRY.md](.claude/skills/SKILL-REGISTRY.md) for the full catalog with agent mappings.

**Universal** (applied to all agents): git-workflow, code-quality-standards, structured-logging, read-software-docs, config-management

**Domain skills** span: ML/DL Core, Computer Vision, NLP/LLM, Robotics, Reinforcement Learning, Inference & Edge, Full Stack, DevOps & MLOps, Security, QA & Testing, Scientific Computing, Simulation, Research & Documentation, Document Generation.

## Project Templates

See [project-templates.md](project-templates.md) for pre-built agent+skill bundles for common project types (robotics, web app, ML research, etc.).

## Creating New Skills

Use `.claude/skills/SKILL-TEMPLATE.md` as the starting point. Each skill needs:
- A folder under `.claude/skills/<skill-name>/`
- A `SKILL.md` with YAML frontmatter (name, version, description)
- An entry in `SKILL-REGISTRY.md`

## Validation

Run the consistency checker to ensure agents, skills, and registry are in sync:

```bash
bash scripts/validate.sh
```

## License

Internal use. Adapt as needed for your organization.
