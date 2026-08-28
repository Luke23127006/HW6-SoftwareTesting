# HUMAN GATE — Select Admin Create Coupon Human Tests

**Gate ID:** ADMIN-COUPON-EXTEND-01  
**Status:** WAITING_FOR_HUMAN  
**Decision:** PENDING

## Reason for stopping

At least five student-owned Admin Create Coupon tests are required. Codex proposed seven gaps but cannot claim student authorship without explicit selection.

## Exact human task

Review `tests/admin-create-coupon/gap-analysis.md`. Mark every candidate `ACCEPT`, `MODIFY`, or `REJECT`; accept or modify at least five and describe exact changes for every modification.

| Candidate | Decision |
| --- | --- |
| ADMIN-CAND-01 — Whitespace-normalized uniqueness | PENDING |
| ADMIN-CAND-02 — Unicode-confusable code uniqueness | PENDING |
| ADMIN-CAND-03 — Concurrent admin/user requests | PENDING |
| ADMIN-CAND-04 — Role changes after token issuance | PENDING |
| ADMIN-CAND-05 — Fractional monetary fields | PENDING |
| ADMIN-CAND-06 — Extreme numeric values | PENDING |
| ADMIN-CAND-07 — Cleanup isolation | PENDING |

## Evidence required

- Decision for all seven candidates.
- At least five accepted/modified cases.
- Exact instructions for modifications.
- Overall `Decision` set to `APPROVED`, `MODIFIED`, or `REJECTED`.

**Human notes:**

PENDING_HUMAN_ACTION

## Completion instructions

Save this file and ask Codex to continue. Codex will persist only accepted/modified tests, validate and assemble the final suite, update state/TODO/audit, archive the gate, and continue.
