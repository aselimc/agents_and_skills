#!/usr/bin/env bash
# Validates consistency between agents, skills, registry, and CLAUDE.md
# Usage: bash scripts/validate.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AGENTS_DIR="$REPO_ROOT/.claude/agents"
SKILLS_DIR="$REPO_ROOT/.claude/skills"
MEMORY_DIR="$REPO_ROOT/.claude/agent-memory"
REGISTRY="$SKILLS_DIR/SKILL-REGISTRY.md"
CLAUDE_MD="$REPO_ROOT/CLAUDE.md"

errors=0
warnings=0

echo "=== Agents & Skills Validation ==="
echo ""

# 1. Check all agents listed in CLAUDE.md exist on disk
echo "--- Checking agents listed in CLAUDE.md ---"
agents_in_claude=$(grep -A3 "^All agent definitions" "$CLAUDE_MD" | grep -v "^All agent" | grep -v "^$" | head -1 | tr ',' '\n' | sed 's/^ *//;s/ *$//')
for agent in $agents_in_claude; do
    if [[ ! -f "$AGENTS_DIR/$agent.md" ]]; then
        echo "  ERROR: Agent '$agent' listed in CLAUDE.md but not found in $AGENTS_DIR/"
        ((errors++))
    fi
done

# 2. Check all agent .md files on disk are listed in CLAUDE.md
echo "--- Checking agents on disk are in CLAUDE.md ---"
for agent_file in "$AGENTS_DIR"/*.md; do
    agent_name=$(basename "$agent_file" .md)
    if ! echo "$agents_in_claude" | grep -qw "$agent_name"; then
        echo "  ERROR: Agent '$agent_name' exists on disk but not listed in CLAUDE.md"
        ((errors++))
    fi
done

# 3. Check agent-memory directories have matching agents
echo "--- Checking agent-memory directories ---"
for mem_dir in "$MEMORY_DIR"/*/; do
    mem_name=$(basename "$mem_dir")
    if [[ ! -f "$AGENTS_DIR/$mem_name.md" ]]; then
        echo "  WARNING: agent-memory/$mem_name/ has no matching agent definition"
        ((warnings++))
    fi
done

# 4. Check all agents have memory directories
echo "--- Checking agents have memory directories ---"
for agent_file in "$AGENTS_DIR"/*.md; do
    agent_name=$(basename "$agent_file" .md)
    if [[ ! -d "$MEMORY_DIR/$agent_name" ]]; then
        echo "  WARNING: Agent '$agent_name' has no memory directory"
        ((warnings++))
    fi
done

# 5. Check all active skill directories have SKILL.md
echo "--- Checking skill directories have SKILL.md ---"
for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    if [[ ! -f "$skill_dir/SKILL.md" ]]; then
        echo "  ERROR: Skill directory '$skill_name/' missing SKILL.md"
        ((errors++))
    fi
done

# 6. Check skill SKILL.md files have version field
echo "--- Checking skills have version in frontmatter ---"
for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"
    if [[ -f "$skill_file" ]]; then
        if ! grep -q "^version:" "$skill_file"; then
            echo "  WARNING: Skill '$skill_name' SKILL.md missing version field"
            ((warnings++))
        fi
    fi
done

# 7. Check no deprecated skill directories remain
echo "--- Checking for deprecated skill directories ---"
deprecated_skills=("dask" "geopandas" "market-research-reports" "theme-factory" "web-artifacts-builder" "document-skills")
for dep in "${deprecated_skills[@]}"; do
    if [[ -d "$SKILLS_DIR/$dep" ]]; then
        echo "  ERROR: Deprecated skill '$dep' directory still exists"
        ((errors++))
    fi
done

# 8. Check skills referenced in registry exist on disk
echo "--- Checking registry skills exist on disk ---"
registry_skills=$(grep '### `' "$REGISTRY" | sed 's/.*### `//;s/`.*//' | grep -v '(existing)')
for skill in $registry_skills; do
    # Skip if in deprecated section (check by looking at context)
    if grep -A2 "### \`$skill\`" "$REGISTRY" | grep -q 'deprecated\|Deprecated'; then
        continue
    fi
    if [[ ! -d "$SKILLS_DIR/$skill" ]]; then
        echo "  WARNING: Skill '$skill' in registry but no directory on disk"
        ((warnings++))
    fi
done

echo ""
echo "=== Results ==="
echo "  Errors:   $errors"
echo "  Warnings: $warnings"

if [[ $errors -gt 0 ]]; then
    echo "  FAILED - fix errors above"
    exit 1
else
    echo "  PASSED"
    exit 0
fi
