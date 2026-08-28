---
name: test-case-auditor
description: Prepare and validate the mandatory human audit of every AI-generated test while keeping AI suggestions separate from the student's final verdict.
---

# Test Case Auditor

## Purpose

Support the mandatory review of every AI-generated test case.

AI may suggest whether a case appears VALID, INVALID, or INCOMPLETE, but the final decision belongs to the student.

## Inputs

```text
tests/<api>/generated-tests.yaml
tests/<api>/api-context.yaml
```

## Outputs

```text
tests/<api>/audit.yaml
tests/<api>/audit.md
tests/<api>/corrected-ai-tests.yaml
```

## Allowed Verdicts

- `VALID`
- `INVALID`
- `INCOMPLETE`

## Mandatory Separation

Each audit record must distinguish:

```yaml
ai_review:
  suggested_verdict:
  reasoning:

human_review:
  verdict:
  reasoning:
```

AI MUST NOT fill:

```yaml
human_review.verdict
human_review.reasoning
```

unless the student explicitly supplies the decision.

## Review Criteria

Review every AI-generated test for:

### Contract Accuracy

- correct method
- correct path
- correct fields
- source-supported expectations

### Technique Accuracy

Check whether the claimed technique actually matches the test.

### Duplicate Value

Reject or merge tests that are semantically duplicate without meaningful distinction.

### Preconditions

Check whether setup requirements are realistic.

### Expected Result

Check whether the result is defined by source material.

If not:

- mark incomplete if the test otherwise makes sense;
- preserve ambiguity;
- do not invent expected behavior.

### Security Traceability

Make sure security tests point to relevant SEC requirements or a clearly justified security risk.

### State Feasibility

Check whether the test can actually place the SUT in the required state.

### Cleanup

Confirm mutation tests do not unnecessarily pollute following tests.

## INVALID Cases

When the human verdict is `INVALID`, record exactly why.

Examples:

- endpoint does not exist
- expected behavior contradicts specification
- duplicate scenario
- impossible state
- irrelevant security rule

## INCOMPLETE Cases

Record missing information.

Examples:

- missing precondition
- undocumented expected status
- missing assertion
- missing setup/cleanup
- missing cross-user setup for IDOR

## Corrections

For every `INVALID` or `INCOMPLETE` case:

```yaml
correction:
  required: true
  description: ...
```

Preserve the original test for audit history.

## Prepare Audit Scaffold

```bash
python .agents/skills/test-case-auditor/scripts/prepare_audit.py   tests/<api>/generated-tests.yaml   tests/<api>/audit.yaml
```

## Validate Human Review

After the student completes all verdicts:

```bash
python .agents/skills/test-case-auditor/scripts/validate_human_audit.py   tests/<api>/audit.yaml
```

Do not continue to final test assembly until this passes.


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

