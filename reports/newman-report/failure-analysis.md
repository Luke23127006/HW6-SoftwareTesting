# CI Run 33228816770 — Failure Analysis

## Evidence

- Commit: `34ea594f39061e6eed9c8be9a702141f20109b96`
- Actions job: `https://github.com/Luke23127006/HW6-SoftwareTesting/actions/runs/33228816770/job/99037708089`
- Source JSON: `reports/newman-report/report.json`
- Source HTML: `reports/newman-report/report.html`
- Screenshot: `evidence/ci/ci-fail.png`

The JSON is authoritative for machine counts: 133 requests, 375 assertions, 39 failed assertions, no failed test scripts, and 31 request items with at least one failed assertion. The previously supplied value of 37 failed tests is preserved as a student-reported/display value, but it does not match the downloaded JSON or the screenshot log numbering, which reaches failure 39.

## A — Confirmed Genuine SUT Defects (8 items)

- `COUPON-AI-001`, `COUPON-AI-017`: confirmed BUG-001, incorrect percent calculation.
- `COUPON-AI-007`: confirmed BUG-002, equality at the minimum rejected.
- `COUPON-AI-009`, `COUPON-AI-010`, `COUPON-AI-011`: confirmed BUG-003, missing/malformed/expired JWT accepted.
- `ADMIN-COUPON-AI-008`, `ADMIN-COUPON-AI-032`: confirmed BUG-004, missing required fields accepted.

These assertions remain unchanged in the authoritative suite.

## B — Test Data / Setup Failures (12 items)

### Shared login state or absent fixtures (9)

- `LOGIN-AI-020`, `LOGIN-AI-027`, `LOGIN-AI-028`, `LOGIN-AI-033`, `LOGIN-AI-034`, `LOGIN-AI-035`, `LOGIN-AI-036`: the shared user was locked by earlier tests and the required state was not restored.
- `LOGIN-HUMAN-001`, `LOGIN-HUMAN-002`: the required secondary/existing-user fixtures were not created.

### Coupon usage fixtures (2)

- `COUPON-AI-015`, `COUPON-AI-016`: the maximum and above-maximum usage rows were not established before execution.

### Duplicate coupon fixture (1)

- `ADMIN-COUPON-AI-007`: the request expected duplicate-code rejection, but its required existing duplicate was not established; the clean CI database therefore accepted the first creation.

These setup defects may be corrected without changing the documented expected results.

## C — Genuinely Incorrect Test Cases

No incorrect expected result has been identified from this CI artifact. This count is **0** unless later evidence establishes a test defect.

## Unconfirmed SUT Bug Candidates (11 items)

These failures are not setup failures merely because the SUT returned HTTP 200. Their requests exercised documented authentication, required-field, enum, and numeric constraints, but human confirmation is required before they become confirmed bugs:

- `ADMIN-COUPON-AI-006`: expired administrator JWT accepted.
- `ADMIN-COUPON-AI-013`: missing required `type` accepted.
- `ADMIN-COUPON-AI-014`: invalid `type` enum accepted.
- `ADMIN-COUPON-AI-015`: null `type` accepted.
- `ADMIN-COUPON-AI-016`: zero `discount_value` accepted.
- `ADMIN-COUPON-AI-017`: negative `discount_value` accepted.
- `ADMIN-COUPON-AI-022`: negative `min_order_amount` accepted.
- `ADMIN-COUPON-AI-023`: missing required `min_order_amount` accepted.
- `ADMIN-COUPON-AI-025`: zero `max_uses_per_user` accepted.
- `ADMIN-COUPON-AI-026`: negative `max_uses_per_user` accepted.
- `ADMIN-COUPON-AI-028`: missing required `expired_at` accepted.

## Infrastructure Next Step

After the human confirmation gate, repair only the 12 setup/data cases, rerun the full suite, and preserve all confirmed or still-valid defect-detecting assertions. CI PASS planning remains separate and must not represent the full suite as passing while genuine defects remain observable.
