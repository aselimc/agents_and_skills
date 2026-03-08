---
name: prompt-engineering
version: 1.0.0
description: Systematic prompt design. Structured output, few-shot, chain-of-thought, and anti-patterns.
---

# Prompt Engineering

## Structured Output
```python
import instructor
client = instructor.from_anthropic(anthropic.Anthropic())
result = client.messages.create(
    model="claude-sonnet-4-6",
    response_model=MyPydanticModel,
    messages=[{"role": "user", "content": prompt}],
)
```

## Patterns
- **Few-shot**: 3-5 examples covering edge cases
- **Chain-of-thought**: "Think step by step" or explicit reasoning structure
- **System prompt**: role + constraints + output format
- **XML tags**: use `<context>`, `<instructions>`, `<examples>` for structure

## Anti-Patterns
- Prompt injection: validate/sanitize user input before embedding in prompts
- Output validation: parse and validate LLM output, retry on failure
- Don't rely on "don't" instructions - tell the model what TO do

## Rules
- Template with Jinja2 or f-strings, never string concatenation with user input
- Version control prompts alongside code
- Evaluate: consistency (same input -> same output), accuracy, latency

## Key Libraries
anthropic SDK, openai SDK, instructor, outlines, guidance
