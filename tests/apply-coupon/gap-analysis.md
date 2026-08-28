# Apply Coupon Post-Audit Gap Analysis

## Baseline

- Approved AI suite: 36 tests, all human-audited `VALID`
- Existing coverage: C1–C5, fixed/percent formulas, threshold boundaries, JWT failures, JWT/body identity mismatch characterization, usage boundaries, malformed values, SQL injection, response schema, rounding/expiration/usage ambiguities
- Boundary: candidates below are proposals only and are not human-authored until explicitly accepted or modified.

## Candidate gaps

### APPLY-CAND-01 — Usage limit is isolated per user

- Scenario: User A has exhausted a coupon's per-user allowance; user B has never used it and applies the same coupon.
- Target: FR-09-C5.
- Missing distinction: Existing tests vary one user's count but never prove another user's usage is independent.
- Proposed oracle: User A is rejected; authenticated user B remains eligible when B's own count is below maximum.
- Why missed: `STATE_COMPLEXITY` — the initial state model tracked one user/coupon pair.

### APPLY-CAND-02 — Concurrent final-allowance applications cannot both succeed

- Scenario: A user at `max_uses_per_user - 1` sends two synchronized application/usage flows for the same coupon.
- Target: FR-09-C5 and usage-state integrity.
- Missing distinction: Existing max−1/max cases are sequential.
- Proposed oracle: The usage count must not exceed the configured maximum; exact application/recording transaction semantics remain subject to `COUPON-AMB-10`.
- Why missed: `STATE_COMPLEXITY` — concurrency and split application/usage operations require a race-oriented model.

### APPLY-CAND-03 — Very large total does not overflow discount arithmetic

- Scenario: Apply a valid percent coupon to a very large finite numeric total within the JSON parser's range.
- Target: FR-09-R1 and FR-09-R3.
- Missing distinction: Existing formula tests use ordinary totals and do not exercise numeric overflow or precision loss.
- Proposed oracle: Returned numeric values follow the formulas without becoming non-finite; exact safe-integer limits are `SPEC_UNDEFINED`.
- Why missed: `API_CHARACTERISTIC` — JavaScript numeric precision is implementation-specific context beyond ordinary business boundaries.

### APPLY-CAND-04 — Fractional total preserves formula relationship

- Scenario: Apply a percentage coupon to a fractional monetary total such as `300000.55`.
- Target: FR-09-R1, FR-09-R3, and `COUPON-AMB-05`.
- Missing distinction: The AI rounding case creates a fractional discount from an integer total, but does not test a fractional input amount.
- Proposed oracle: Record rounding/precision behavior while asserting `final_amount = total_amount - discount_amount`; currency precision is `SPEC_UNDEFINED`.
- Why missed: `SPEC_AMBIGUITY` — monetary scale and accepted numeric precision are undocumented.

### APPLY-CAND-05 — JWT for deleted/deactivated user

- Scenario: Obtain a valid JWT, then delete or deactivate its subject before applying a coupon.
- Target: FR-09-C4 and SEC-02.
- Missing distinction: Missing/malformed/expired tokens are covered, but token cryptographic validity versus current subject validity is not.
- Proposed oracle: `SPEC_UNDEFINED`; record whether current user existence/status is revalidated and do not claim a defect without an authoritative rule.
- Why missed: `SECURITY_CONTEXT` — token lifecycle and account lifecycle were modeled independently.

### APPLY-CAND-06 — Duplicate `user_id` JSON keys cannot select another usage identity

- Scenario: Send a raw JSON body containing two `user_id` keys with different users and controlled usage counts.
- Target: FR-09-C5 and `COUPON-AMB-03`/`COUPON-AMB-04`.
- Missing distinction: Identity mismatch is covered with one body value, not parser ambiguity from duplicate identity keys.
- Proposed oracle: No usage-limit bypass; parser behavior is recorded as `SPEC_UNDEFINED`.
- Why missed: `SECURITY_CONTEXT` — duplicate-key parser differentials require raw-body adversarial testing.

### APPLY-CAND-07 — Coupon deactivation race during application

- Scenario: Deactivate a coupon concurrently with an application request that initially sees it as active.
- Target: FR-09-C1 and data lifecycle integrity.
- Missing distinction: Static active/inactive partitions exist, but not a state change during evaluation.
- Proposed oracle: Final outcome and transaction boundary are `SPEC_UNDEFINED`; capture whether an inactive coupon can be applied and document the race reproducibly.
- Why missed: `STATE_COMPLEXITY` — the initial suite assumed stable fixture state throughout one request.

## Human selection requirement

Decide `ACCEPT`, `MODIFY`, or `REJECT` for every candidate and accept or modify at least five. Only confirmed cases will be written with `source: HUMAN` and `human_confirmation: true`.
