---
name: submission-validator
description: Perform the final deterministic HW06 readiness check across required documents, test counts, human audit, execution evidence, CI/CD evidence, and generator artifacts.
---

# Submission Validator

## Purpose

Prevent submission with missing mandatory deliverables.

This skill runs near the end of the assignment.

## Inputs

The entire repository.

Machine-readable requirements are stored in:

```text
.agents/skills/submission-validator/references/requirements.yaml
```

## Output

```text
reports/submission-validation.txt
```

and a concise console readiness report.

## Required API Checks

For each selected API verify:

### AI Generation

```text
>= 35 AI-generated tests
```

### Human Audit

Every AI-generated case has:

- human verdict
- human reasoning
- correction where needed

### Human Extension

```text
>= 5 confirmed human tests
```

### Execution

Real execution evidence exists.

## Required Documents

Check for required artifacts such as:

- main report Markdown
- main report PDF
- AI Audit Markdown
- AI Audit PDF
- AI Critique
- CI/CD report
- Postman collection
- Newman HTML report
- test summary
- Excel test cases
- git log
- README
- generator pseudocode
- self-drawn diagram
- bug reports when bugs exist

## CI/CD Checks

Require evidence for:

- all-pass run
- deliberately failing run

Do not consider placeholder text such as:

```text
PENDING_HUMAN_ACTION
```

to be real evidence.

## Content Validation

Do more than file existence checks.

Examples:

- count YAML tests
- count confirmed human tests
- detect missing human verdicts
- detect empty files
- detect missing PDF artifacts
- detect missing self-drawn diagram

## Status

Possible overall outcomes:

```text
READY
NOT READY
```

## Example

```text
HW06 Submission Validation

Pool A
✓ 38 AI tests
✓ human audit complete
✓ 5 human tests

Pool C
✗ only 34 AI tests

Documents
✗ ai-audit.pdf missing

CI/CD
✗ FAIL-run screenshot missing

Status: NOT READY
```

## Run

```bash
python .agents/skills/submission-validator/scripts/validate_submission.py
```

Do not weaken requirements simply to produce READY.


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

