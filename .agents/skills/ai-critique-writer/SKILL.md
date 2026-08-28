---
name: ai-critique-writer
description: Draft the mandatory 200–300 word AI critique using concrete evidence from the actual HW06 generation, audit, extension, and execution process.
---

# AI Critique Writer

## Purpose

Produce the required evidence-based critique of AI collaboration.

Do not write a generic essay about AI.

## Inputs

Use real evidence:

```text
tests/*/audit.yaml
tests/*/gap-analysis.md
tests/*/human-tests.yaml
reports/failure-analysis.md
bugs/*
docs/ai-audit.md
```

## Output

```text
docs/ai-critique.md
```

## Required Length

```text
200–300 words
```

## Required Questions

Address:

1. Where was AI wrong, biased, or incomplete?
2. Why did AI fail to catch the issue?
3. What principle did the student learn about collaborating with AI?

## Evidence Extraction

Before drafting, derive facts such as:

- number of INVALID AI cases
- number of INCOMPLETE cases
- repeated assumption patterns
- human-added gaps
- bugs missed by initial AI generation
- incorrect assumptions about undocumented status codes
- missed cross-field security risks
- state setup limitations

Only include counts if they are supported by project artifacts.

## Recommended Structure

### Part 1 — Concrete AI Weakness

Describe one or two real examples.

### Part 2 — Cause

Explain whether the cause was:

- prompt scope
- model assumption
- missing context
- cross-field complexity
- state complexity
- security reasoning limitation

### Part 3 — Collaboration Lesson

State what workflow change improved reliability.

For example:

- separating spec analysis from generation
- explicitly validating coverage
- requiring human verdicts
- using real execution evidence

## Style

Keep it concrete.

Avoid empty phrases such as:

```text
AI is a powerful tool but has limitations.
```

unless followed immediately by assignment-specific evidence.

## Validation

```bash
python .agents/skills/ai-critique-writer/scripts/validate_word_count.py   docs/ai-critique.md
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

