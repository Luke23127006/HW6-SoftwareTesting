# HUMAN GATE CI-FAIL-01 — Completed

Status: COMPLETED

## Evidence

- Decision: APPROVED
- Temporary commit: `168347660b306c43efa2bb55e69e403016724331`
- Run: https://github.com/Luke23127006/HW6-SoftwareTesting/actions/runs/33260060548
- Job: https://github.com/Luke23127006/HW6-SoftwareTesting/actions/runs/33260060548/job/99120346545
- Screenshot: `evidence/ci/ci-fail-demo.png`
- Result: FAIL
- Student-confirmed failed assertion count: 1

## Intentional change

Only the separate demonstration collection changed: `COUPON-AI-002` expected `discount_amount` was temporarily changed from `50000` to `50001`. The authoritative collection was not modified.

## Validation

The screenshot and public Actions API verify a manually triggered failed job at the exact temporary commit. Before the run, deterministic inspection verified exactly one `to.eql(50001)` temporary assertion in the five-request collection. GitHub's unauthenticated job-log endpoint returned 403, so the exact count is retained as the student's explicit evidence statement rather than inferred from inaccessible logs.
