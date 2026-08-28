---
name: test-case-extender
description: Identify coverage gaps after human audit and help the student add at least five explicitly human-confirmed tests per API, including why the AI missed them.
---

# Test Case Extender

## Purpose

Fulfill the HW06 requirement to add at least five student-owned test cases that the initial AI generation missed.

This skill finds gaps and proposes candidates. It must not falsely relabel AI-generated content as human-authored.

## Inputs

```text
tests/<api>/api-context.yaml
tests/<api>/generated-tests.yaml
tests/<api>/audit.yaml
tests/<api>/coverage.json
```

## Outputs

```text
tests/<api>/gap-analysis.md
tests/<api>/human-tests.yaml
tests/<api>/final-tests.yaml
```

## Workflow

### 1. Recalculate Meaningful Coverage

Consider the human audit:

- INVALID AI cases do not count as final coverage unless corrected.
- INCOMPLETE cases count only after correction.

### 2. Find Gaps

Prioritize:

- security
- authorization
- state behavior
- cross-field interactions
- data lifecycle
- specification ambiguity
- negative business rules

### 3. Propose Candidate Cases

For each candidate explain:

- what is missing
- which requirement it targets
- why existing AI cases do not already cover it
- why AI likely missed it

### 4. Human Decision

The student must explicitly:

- accept;
- modify and accept;
- reject.

### 5. Persist Accepted Cases

Only accepted cases may be written with:

```yaml
source: HUMAN
human_confirmation: true
```

## Why AI Missed Categories

Use one:

- `PROMPT_GAP`
- `MODEL_LIMITATION`
- `API_CHARACTERISTIC`
- `CROSS_FIELD_INTERACTION`
- `STATE_COMPLEXITY`
- `SECURITY_CONTEXT`
- `SPEC_AMBIGUITY`

Example:

```yaml
why_ai_missed:
  category: CROSS_FIELD_INTERACTION
  explanation: >
    The initial generation considered JWT authentication and body user_id
    independently and did not test whether the authenticated identity must
    match the supplied user_id.
```

## Minimum Requirement

Per API:

```text
>= 5 confirmed HUMAN tests
```

## Final Suite

`final-tests.yaml` should contain:

- corrected accepted AI-generated cases
- confirmed human-added cases

Do not include rejected AI cases.

## Validation

```bash
python .agents/skills/test-case-extender/scripts/validate_extensions.py   tests/<api>/human-tests.yaml
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

