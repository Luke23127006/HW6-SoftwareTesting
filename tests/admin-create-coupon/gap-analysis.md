# Admin Create Coupon Post-Audit Gap Analysis

## Baseline

The 36 approved AI cases cover authentication, admin role, uniqueness, required fields, enum/type errors, numeric/date boundaries, SQL injection, persistence, and concurrent duplicate creation. The following are distinct candidate extensions only; none is `source: HUMAN` until explicitly accepted.

### ADMIN-CAND-01 — Uniqueness after whitespace normalization

- Create `"SPACE"`, then attempt `" SPACE "`.
- Target: FR-17 unique `code`; normalization is `ADMIN-AMB-05`.
- Gap: Case variants are covered, whitespace-collision behavior is not.
- Oracle: `SPEC_UNDEFINED`; record whether codes are normalized while ensuring uniqueness is internally consistent.
- Why missed: `SPEC_AMBIGUITY`.

### ADMIN-CAND-02 — Unicode-confusable coupon-code uniqueness

- Create an ASCII code, then a visually confusable Unicode variant.
- Target: FR-17 unique `code` and security-relevant identifier handling.
- Gap: ASCII case and SQL probes do not cover Unicode normalization/confusables.
- Oracle: `SPEC_UNDEFINED`; record exact code points and whether identities remain distinct.
- Why missed: `SECURITY_CONTEXT`.

### ADMIN-CAND-03 — Concurrent admin and normal-user creation attempts

- Synchronize identical-code requests from an admin token and normal-user token.
- Target: FR-12 role enforcement, SEC-03, FR-17 uniqueness.
- Gap: Role rejection and uniqueness races are tested independently.
- Oracle: Only the authorized admin request may create; at most one row exists.
- Why missed: `CROSS_FIELD_INTERACTION`.

### ADMIN-CAND-04 — Admin token subject loses role after token issuance

- Issue an admin JWT, then demote/delete the subject before coupon creation.
- Target: FR-12/SEC-03 token-role lifecycle.
- Gap: Static admin/user/expired tokens are covered, not post-issuance role changes.
- Oracle: `SPEC_UNDEFINED`; record whether current role is revalidated without inventing a requirement.
- Why missed: `SECURITY_CONTEXT`.

### ADMIN-CAND-05 — Fractional min order and discount together

- Create a coupon with fractional positive `discount_value` and fractional nonnegative `min_order_amount`.
- Target: FR-17 positivity/nonnegativity plus `ADMIN-AMB-04`.
- Gap: Fractional max uses is covered, but monetary fields' fractional interaction is not.
- Oracle: Acceptance and persisted precision are `SPEC_UNDEFINED`.
- Why missed: `CROSS_FIELD_INTERACTION`.

### ADMIN-CAND-06 — Extremely large numeric fields

- Use large finite values near the runtime's safe-integer boundary for discount, minimum, and maximum uses.
- Target: FR-17 numeric constraints and persistence integrity.
- Gap: Lower boundaries are comprehensive; upper numeric robustness is absent because maxima are unspecified.
- Oracle: `SPEC_UNDEFINED`; no non-finite/corrupted persisted values or internal-error disclosure.
- Why missed: `API_CHARACTERISTIC`.

### ADMIN-CAND-07 — Cleanup deletes only the created coupon

- Create two coupons, delete one by its captured ID, and verify the other remains unchanged.
- Target: FR-17 CRUD data isolation and executable suite cleanup.
- Gap: Each case names cleanup, but no test verifies cleanup isolation.
- Oracle: Deleted coupon is absent; untouched coupon remains with original values.
- Why missed: `STATE_COMPLEXITY`.

## Human selection requirement

Decide `ACCEPT`, `MODIFY`, or `REJECT` for all seven and accept or modify at least five. Only confirmed cases will be persisted as human-authored tests.
