---
name: human-gate-manager
description: >
  Manage explicit human-in-the-loop checkpoints for HW06.
  Use this skill whenever work requires student approval, student-authored
  decisions, real screenshots, real URLs, manual actions, or other evidence
  that the agent must not fabricate.
---

# Human Gate Manager

## Purpose

Provide one consistent protocol for pausing automated HW06 work
when student participation is required.

The agent performs all automatable work first, prepares the material
for review, writes a single actionable `tmp.md`, then stops.

The agent must never impersonate the student.

## Trigger Conditions

Use this skill whenever any task requires:

- final human audit verdict;
- confirmation of a human-added test;
- student-specific data that must not be invented;
- manual screenshot capture;
- real GitHub Actions evidence;
- real GitHub Issue creation;
- confirmation that a candidate is a genuine bug;
- a student-created diagram;
- final manual submission review;
- any other artifact explicitly prohibited from AI generation.

Do not create a gate for normal AI work that can safely be automated.

## Human Gate Protocol

### Step 1 — Finish automatable preparation

Before creating a gate:

1. complete all safe automated work;
2. generate review artifacts;
3. validate them where possible;
4. identify the exact human decision/action required.

Do not ask the human to perform work the agent can perform itself.

### Step 2 — Write `tmp.md`

Create or replace the repository-root file:

`tmp.md`

It must contain:

- Gate ID
- status
- reason for stopping
- exact human task
- files to review
- evidence required
- fields the student must fill
- completion instructions

Set:

`Status: WAITING_FOR_HUMAN`

and:

`Decision: PENDING`

### Step 3 — Stop

After writing `tmp.md`:

STOP execution.

Do not:

- mark the TODO gate complete;
- mark the workflow state complete;
- fabricate approval;
- fabricate evidence;
- continue to dependent phases.

Tell the student only that human action is required in `tmp.md`.

### Step 4 — Resume

When the student asks to continue:

1. read `tmp.md`;
2. verify `Decision`;
3. verify all requested files/evidence exist;
4. inspect supplied human values;
5. reject incomplete gates instead of guessing.

Accepted decisions:

- APPROVED
- REJECTED
- MODIFIED

If still PENDING, stop again.

### Step 5 — Apply human decision

For APPROVED or MODIFIED:

- apply only the confirmed human decisions;
- update the relevant artifact;
- run validators;
- update `state/hw06-state.yaml`;
- update the corresponding item in `todo.md`;
- append the interaction to `docs/ai-audit.md`.

Never rewrite a human decision as if it originated from AI.

### Step 6 — Archive

Archive the completed gate under:

`ai-logs/human-gates/<GATE-ID>.md`

Preserve:

- original request;
- human decision;
- supplied evidence references;
- notes;
- resolution.

Then reset:

`tmp.md`

to:

`No pending human action.`

## Evidence Rules

The following must be real and must never be synthesized:

- screenshots;
- Newman execution output;
- actual HTTP responses;
- X-Student-Id evidence;
- GitHub Actions URLs;
- Git commit SHAs;
- GitHub Issue numbers and URLs;
- student audit verdicts;
- student ownership of human-added tests;
- self-drawn diagram.

If missing, use:

`PENDING_HUMAN_ACTION`

## Human Review Rules

AI may provide recommendations such as:

`ai_review.suggested_verdict`

but it may not populate:

`human_review.verdict`

unless the human explicitly supplied that decision.

For human-added tests, the agent may suggest gaps or ideas,
but may only mark:

`source: HUMAN`
`human_confirmation: true`

after explicit student acceptance or modification.

## Gate ID Convention

Use stable IDs such as:

- LOGIN-AUDIT-01
- LOGIN-EXTEND-01
- APPLY-COUPON-AUDIT-01
- ADMIN-COUPON-AUDIT-01
- NEWMAN-EVIDENCE-01
- BUG-001-CONFIRM
- CI-PASS-01
- CI-FAIL-01
- GENERATOR-DIAGRAM-01
- FINAL-REVIEW-01

## Principle

Automate preparation.

Require humans only for genuine human judgment or real-world evidence.

Never use a human gate as an excuse to delegate routine agent work
back to the student.