---
name: test-result-analyzer
description: Analyze real Newman execution output, summarize results, and classify failures without automatically declaring them to be SUT bugs.
---

# Test Result Analyzer

## Purpose

Convert actual Newman output into structured test results and failure analysis.

## Inputs

Required:

```text
reports/newman/report.json
```

Also use:

```text
tests/*/final-tests.yaml
tests/*/api-context.yaml
```

when interpreting failures.

## Outputs

```text
reports/results.json
reports/failure-analysis.md
docs/test-summary.md
```

## Preconditions

The input Newman report must come from a real run.

Do not create synthetic execution evidence.

## Initial Parsing

For every executed Postman item capture:

- test ID
- pass/fail
- response status
- failed assertion(s)
- available Newman error details

## Failure Classification

Every failure must eventually be classified as one of:

- `SUT_BUG_CANDIDATE`
- `TEST_DEFECT`
- `ENVIRONMENT_FAILURE`
- `SPECIFICATION_GAP`
- `DATA_SETUP_FAILURE`

Passing tests use:

- `NONE`

## Classification Guidance

### SUT_BUG_CANDIDATE

Use when:

- the test is valid;
- the expected result is explicitly supported;
- setup is correct;
- actual behavior contradicts the requirement.

Still require human confirmation.

### TEST_DEFECT

Use when:

- assertion is wrong;
- test expectation is unsupported;
- request payload does not match intended test.

### ENVIRONMENT_FAILURE

Examples:

- SUT not running
- connection refused
- database unavailable
- malformed environment configuration

### SPECIFICATION_GAP

Use when the test exposes ambiguity and no authoritative expectation exists.

### DATA_SETUP_FAILURE

Use when the intended precondition was not actually created.

## Bug Boundary

Never automatically convert:

```text
FAIL → BUG
```

Use:

```text
FAIL
→ classify
→ inspect evidence
→ human confirmation
→ bug-report-writer
```

## Test Summary

Update `docs/test-summary.md` with:

- executed
- passed
- failed

Do not count tests that did not actually execute as passed.

## Command

```bash
python .agents/skills/test-result-analyzer/scripts/parse_newman.py   reports/newman/report.json
```

After parsing, AI may assist with classification using source requirements.


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

