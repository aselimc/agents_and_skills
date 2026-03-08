# Agents & Skills Starter Kit

This project is a library of reusable Claude Code agents and skills. Its purpose is to bootstrap new projects by selecting and copying the right agents and skills into them.

## What This Project Does

When the user describes a new project idea, you must:

1. **Create the project folder** at the path the user specifies (or ask if not provided)
2. **Select relevant agents and skills** based on the project's domain and requirements
3. **Copy them** into the new project's `.claude/agents/` and `.claude/skills/` directories
4. **Write a CLAUDE.md** tailored to the new project (not a copy of this file)
5. **Write a STATUS.md** in the new project root

## How to Select Agents and Skills

- Ask the user what the project is about if unclear
- Match agents and skills to the project domain (e.g., a robotics project gets `robotics-engineer`, `ros2-development`, `sensor-fusion-pipeline`, etc.)
- Always include foundational skills: `git-workflow`, `test-pyramid`, `code-quality-standards`
- Always include the `cto-orchestrator` and `project-manager` agents
- Include `docs-generator` agent for any non-trivial project
- Present the selected list to the user for approval before copying

## Available Agents

All agent definitions live in `.claude/agents/` in this repo:

agent-architect, agent-evaluator, backend-architect, computer-vision-engineer, cto-orchestrator, data-engineer, devops-infra-engineer, docs-generator, edge-computing-architect, embedded-firmware-engineer, frontend-builder, inference-engineer, mlops-pipeline, mobile-app-builder, nlp-llm-specialist, project-manager, qa-test-engineer, realtime-sim-engine, research-paper-writer, rl-engineer, robotics-engineer, scientific-computing, security-guardian, skill-library, system-architect, world-model-researcher

## Available Skills

All skill definitions live in `.claude/skills/` in this repo. See `SKILL-REGISTRY.md` for the full catalog.

## STATUS.md Convention

Every new project gets a `STATUS.md` in its root. Rules:
- Maximum 100 lines
- NOT a changelog — it reflects **current state only**
- Sections: Project Overview, Current State, Active Tasks, Key Decisions, Blockers
- Update it as work progresses; remove completed items, don't accumulate history
- Keep it concise — one line per item where possible

## CLAUDE.md Convention for New Projects

The generated CLAUDE.md for each new project should include:
- Project name and one-line description
- Tech stack and key dependencies
- Project structure overview
- Build/run/test commands
- Conventions specific to the project
- Reference to STATUS.md for current state

## Project Templates

See `project-templates.md` for pre-built agent+skill bundles for common project types (robotics, web app, ML research, etc.). Use these as starting points when bootstrapping.

## Directory Structure

```
agents_and_skills/
├── CLAUDE.md                          # This file
├── README.md                          # Human-facing documentation
├── STATUS.md                          # Current project state
├── project-templates.md               # Pre-built bundles for common project types
├── .gitignore
├── scripts/
│   └── validate.sh                    # Consistency checker
├── .claude/
│   ├── agents/                        # Agent definitions (.md files)
│   ├── skills/
│   │   ├── SKILL-REGISTRY.md          # Central skill catalog
│   │   ├── SKILL-TEMPLATE.md          # Template for new skills
│   │   └── <skill-name>/SKILL.md      # Individual skill definitions
│   └── agent-memory/                  # Persistent memory per agent
```

## Workflow

1. User says: "I want to start a new project about X"
2. You ask clarifying questions if needed (path, tech stack, scope)
3. You select appropriate agents and skills
4. You present the selection for approval
5. You create the project folder structure
6. You copy agents and skills
7. You write the project's CLAUDE.md and STATUS.md
8. You confirm completion and summarize what was set up
