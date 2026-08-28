---
name: report-writer
description: Incrementally assemble the HW06 main Markdown report from existing testing artifacts and real evidence without inventing missing results.
---

# Report Writer

## Purpose

Maintain the main report throughout the assignment instead of generating it from scratch at the end.

## Inputs

Use only project artifacts that already exist.

Relevant sources include:

```text
source/*
tests/*/api-context.yaml
tests/*/coverage.*
tests/*/audit.*
tests/*/human-tests.yaml
reports/results.json
reports/failure-analysis.md
bugs/*
docs/cicd-report.md
generator/pseudocode.md
docs/ai-critique.md
docs/ai-audit.md
```

## Outputs

```text
docs/report-sections/*.md
docs/report.md
```

The PDF is generated later from the final Markdown.

## Report Structure

Follow:

```text
.agents/skills/report-writer/assets/report-template.md
```

Core sections:

1. Introduction
2. SUT and Testing Environment
3. Selected APIs
4. Testing Approach
5. Pool A — Login
6. Pool B — Apply Coupon
7. Pool C — Admin Create Coupon
8. Postman Features Used
9. CI/CD Integration
10. AI-Driven API Test Generator
11. Overall Test Summary
12. AI Critique
13. AI Audit Appendix

## API Sections

For each API include:

### API Analysis

Summarize:

- endpoint
- requirements
- important constraints
- security/state context

### AI Test Generation

Include:

- number generated
- techniques used
- generation process

### Coverage

Use actual coverage artifacts.

### Human Audit

Include:

- VALID count
- INVALID count
- INCOMPLETE count
- important corrections

### Human-Added Tests

Include:

- at least five tests
- why AI missed them

### Execution

Use real Newman results.

### Bugs

Only include confirmed bugs.

## Evidence-First Rule

If a required value does not exist yet, write an explicit TODO.

Example:

```markdown
> TODO: Add real GitHub Actions FAIL-run screenshot.
```

Never fill missing evidence with plausible values.

## Postman Features

Only list features actually used.

Examples may include:

- collections
- environments
- variables
- pre-request scripts
- test scripts
- data files
- Collection Runner
- mock server
- monitor

Do not claim features just because the assignment mentions them.

## Generator Section

The test-generator architecture diagram must be student-drawn.

The report may reference the student's file.

Do not generate a fake diagram artifact.

## Assembly

```bash
python .agents/skills/report-writer/scripts/assemble_report.py
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

