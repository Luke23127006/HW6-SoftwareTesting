# HUMAN GATE — Review Apply Coupon Tests

**Gate ID:** APPLY-COUPON-AUDIT-01  
**Status:** WAITING_FOR_HUMAN  
**Decision:** PENDING

## Reason for stopping

All 36 AI-generated Apply Coupon tests require a final student-authored audit. Codex cannot supply or infer the final human verdicts, reasoning, or corrections.

## Exact human task

Review every record in `tests/apply-coupon/audit.yaml` against the original test and authoritative context. For each record fill:

```yaml
human_review:
  verdict: VALID | INVALID | INCOMPLETE
  reasoning: <your concrete human reasoning>
```

For every `INVALID` or `INCOMPLETE` verdict also set `correction.required: true` and provide `correction.description`. For `VALID`, leave correction unnecessary.

## Files to review

- `tests/apply-coupon/generated-tests.yaml`
- `tests/apply-coupon/api-context.yaml`
- `tests/apply-coupon/traceability.md`
- `tests/apply-coupon/audit.yaml`

Pay special attention to `SPEC_UNDEFINED` statuses, JWT/body `user_id` mismatch, rounding, expiration equality, usage mutation timing, and whether each precondition is executable.

## Evidence required

- All 36 final verdicts are `VALID`, `INVALID`, or `INCOMPLETE`.
- All 36 records contain substantive student reasoning.
- Every invalid/incomplete case contains a correction description.
- `tests/apply-coupon/audit.yaml` is saved.

## Completion fields

Set the overall `Decision` above to `APPROVED`, `MODIFIED`, or `REJECTED` and add notes:

**Human notes:**

PENDING_HUMAN_ACTION

## Completion instructions

Save the files and ask Codex to continue. Codex will validate the audit, apply only your confirmed decisions, update state/TODO/audit, archive this gate, and proceed to the next prerequisite-safe task.
