# HUMAN GATE — Select Apply Coupon Human Tests

**Gate ID:** APPLY-COUPON-EXTEND-01  
**Status:** WAITING_FOR_HUMAN  
**Decision:** ACCEPT

## Reason for stopping

At least five student-owned Apply Coupon tests are required. Codex proposed seven gaps but cannot claim student authorship or set `human_confirmation: true` without explicit selection.

## Exact human task

Review `tests/apply-coupon/gap-analysis.md`. Mark every candidate `ACCEPT`, `MODIFY`, or `REJECT`; accept or modify at least five. Describe exact changes for every `MODIFY`.

| Candidate | Decision |
| --- | --- |
| APPLY-CAND-01 — Usage limit isolated per user | ACCEPT |
| APPLY-CAND-02 — Concurrent final-allowance applications | ACCEPT |
| APPLY-CAND-03 — Very large total arithmetic | ACCEPT |
| APPLY-CAND-04 — Fractional monetary total | ACCEPT |
| APPLY-CAND-05 — JWT subject deleted/deactivated | ACCEPT |
| APPLY-CAND-06 — Duplicate `user_id` JSON keys | ACCEPT |
| APPLY-CAND-07 — Coupon deactivation race | ACCEPT |

## Files to review

- `tests/apply-coupon/gap-analysis.md`
- `tests/apply-coupon/generated-tests.yaml`
- `tests/apply-coupon/api-context.yaml`

## Evidence required

- Explicit decision for all seven candidates.
- At least five accepted or modified cases.
- Exact instructions for modifications.
- Overall `Decision` set to `APPROVED`, `MODIFIED`, or `REJECTED`.

**Human notes:**

APPROVED

## Completion instructions

Save this file and ask Codex to continue. Codex will persist only accepted/modified cases, validate them, assemble the final Apply Coupon suite, update state/TODO/audit, archive this gate, and continue.
