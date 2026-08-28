---
name: bug-report-writer
description: Draft a reproducible, traceable GitHub-style bug report only after the student confirms that a real failed test represents a genuine SUT defect.
---

# Bug Report Writer

## Purpose

Create report-ready bug documentation from confirmed real defects.

## Preconditions

Do not use this skill merely because Newman reports a failure.

The student must first confirm the failure is a genuine SUT bug.

## Inputs

For each confirmed bug:

- related test ID
- FR/SEC requirement
- environment
- preconditions
- exact reproduction steps
- expected result
- actual result
- relevant real response/evidence
- screenshot path if already captured

## Outputs

```text
bugs/BUG-XXX.md
docs/bugs.md
```

The content can then be copied into a GitHub Issue by the student.

## Required Sections

Use:

```text
Title
Requirement
Environment
Preconditions
Steps to Reproduce
Expected Result
Actual Result
Evidence
Related Test
GitHub Issue
```

## Title

Keep it specific.

Good:

```text
[BUG-001] Apply Coupon accepts user_id that does not match JWT identity
```

Bad:

```text
Coupon bug
```

## Traceability

Always reference:

- test ID
- FR requirement
- relevant SEC requirement when applicable

## Evidence Rules

Never invent:

- screenshot
- issue number
- GitHub URL
- request/response
- commit hash

If a human action is still required:

```text
PENDING_HUMAN_ACTION
```

## GitHub Issue

After the student creates the issue, the report may be updated with the real URL and issue number.

## Template

Use:

```text
.agents/skills/bug-report-writer/assets/github-issue-template.md
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

