# HUMAN GATE A1 — Review Login Tests

**Gate ID:** LOGIN-AUDIT-01  
**Status:** WAITING_FOR_HUMAN  
**Decision:** PENDING

## Reason for stopping

All 38 AI-generated Login tests require a final student-authored audit. Codex cannot supply or infer the final human verdicts, reasoning, or corrections.

## Exact human task

Review every record in `tests/login/audit.yaml` against the original test and authoritative context. For each of the 38 records, fill:

```yaml
human_review:
  verdict: VALID | INVALID | INCOMPLETE
  reasoning: <your concrete human reasoning>
```

For every `INVALID` or `INCOMPLETE` verdict, also fill:

```yaml
correction:
  required: true
  description: <the correction you approve>
```

For a `VALID` verdict, leave `correction.required: false`; no correction description is required.

Do not alter `test_id` values and do not present AI suggestions as your human reasoning.

## Files to review

- `tests/login/generated-tests.yaml` — the 38 original AI tests
- `tests/login/api-context.yaml` — normalized source-backed oracle and ambiguities
- `tests/login/traceability.md` — requirement mapping
- `tests/login/audit.yaml` — file you must complete

Pay special attention to tests whose expected status is `SPEC_UNDEFINED`, implementation-inspection test `LOGIN-AI-036`, timing feasibility, setup/cleanup feasibility, and whether each claimed technique matches the case.

## Evidence required

- All 38 `human_review.verdict` fields contain exactly `VALID`, `INVALID`, or `INCOMPLETE`.
- All 38 `human_review.reasoning` fields contain substantive student reasoning.
- Every `INVALID`/`INCOMPLETE` record contains a correction description.
- The completed `tests/login/audit.yaml` is saved in the repository.

## Completion fields

After completing the audit, edit the top of this file:

```text
Decision: APPROVED
```

Use `MODIFIED` if you changed the proposed review material while completing it, or `REJECTED` if the audit scaffold should not proceed. Add any notes below.

**Human notes:**

PENDING_HUMAN_ACTION

## Completion instructions

Save both files, then ask Codex to continue. Codex will validate the audit, reject incomplete entries rather than guessing, apply only your confirmed decisions, update state/TODO/audit, archive this gate, and continue to the next prerequisite-safe phase.
