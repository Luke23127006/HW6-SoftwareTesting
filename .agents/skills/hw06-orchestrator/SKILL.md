---
name: hw06-orchestrator
description: Coordinate the HW06 API-testing workflow, enforce prerequisites, and update workflow state without doing specialist testing work itself.
---

# HW06 Orchestrator

## Purpose

Coordinate the complete HW06 workflow for the three selected APIs:

- Pool A / FR-02 — `POST /api/login`
- Pool B / FR-09 — `POST /api/apply-coupon`
- Pool C / FR-17 — `POST /api/admin/coupons`

This skill tracks progress, checks prerequisites, routes work to the correct specialist skill, and updates `state/hw06-state.yaml`.

It must not directly replace specialist skills.

## Inputs

- `config/hw06.yaml`
- `state/hw06-state.yaml`
- artifacts already present under:
  - `tests/`
  - `postman/`
  - `reports/`
  - `docs/`
  - `bugs/`

## Outputs

- updated `state/hw06-state.yaml`
- next-step recommendation
- routed invocation of the correct specialist skill

## Per-API Workflow

For each API, use this order:

1. `api-spec-analyzer`
2. `api-test-generator`
3. `test-case-auditor`
4. `test-case-extender`
5. `postman-test-builder`
6. real execution with Postman/Newman
7. `test-result-analyzer`
8. `bug-report-writer` if a failure is confirmed as a real bug

## Global Workflow

After the three APIs are processed:

1. `cicd-helper`
2. `report-writer`
3. `ai-critique-writer`
4. `submission-validator`

## State Rules

Allowed statuses:

- `pending`
- `in_progress`
- `done`
- `blocked`

Do not mark a step `done` only because an AI artifact exists. Confirm the required evidence exists.

## Human-Only Gates

Never set `human_audit: done` unless:

- every AI-generated test has a final human verdict;
- each verdict is one of:
  - `VALID`
  - `INVALID`
  - `INCOMPLETE`
- each verdict contains human reasoning;
- every INVALID/INCOMPLETE case contains a correction.

Never increment `human_added_count` unless the test:

```yaml
source: HUMAN
human_confirmation: true
```

Never mark:

- execution
- GitHub Issue evidence
- CI/CD evidence
- screenshots
- self-drawn diagram

as complete based on generated text alone.

## Next-Step Logic

Choose the first prerequisite-safe incomplete step.

Example:

```text
spec_analysis == pending
→ api-spec-analyzer

spec_analysis == done
AND ai_generation == pending
→ api-test-generator

ai_generation == done
AND human_audit == pending
→ test-case-auditor
```

If a prerequisite is missing, mark the dependent step `blocked` and explain exactly what artifact is missing.


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

## Human-in-the-Loop Protocol

Whenever the current TODO task reaches a `HUMAN GATE`,
delegate gate handling to `human-gate-manager`.

The orchestrator must:

1. finish all automatable work before the gate;
2. invoke the human gate protocol;
3. create `tmp.md`;
4. stop immediately;
5. wait for explicit human completion;
6. on resume, validate the human response and evidence;
7. update artifacts;
8. update `todo.md`;
9. update `state/hw06-state.yaml`;
10. append AI audit;
11. archive the completed gate;
12. continue with the next TODO item.

Never bypass a HUMAN GATE because sufficient information appears
inferable from existing artifacts.