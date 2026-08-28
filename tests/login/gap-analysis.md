# Login Post-Audit Gap Analysis

## Baseline

- AI suite: 38 tests
- Human audit: 38 `VALID`, 0 `INVALID`, 0 `INCOMPLETE`
- Existing strengths: credential partitions, missing/null/type errors, third-failure boundary, lock timeout, SQL injection, non-disclosure, JWT shape, and response schema
- Constraint: items below are AI-proposed candidates only. None is a `source: HUMAN` test until the student explicitly accepts or modifies it.

## Meaningful remaining gaps

### LOGIN-CAND-01 — Lockout is isolated per account

- Missing scenario: Lock user A through three consecutive failures, then log in successfully as distinct user B during A's lock interval.
- Target: FR-02 account lock semantics and cross-account state isolation.
- Why existing cases do not cover it: Existing state tests use one account and never prove that one user's lock state cannot deny another user.
- Why AI initially missed it: `STATE_COMPLEXITY` — the first pass modeled the counter as a single-account state machine.
- Proposed oracle: User A remains locked; user B succeeds with HTTP 200 and receives a JWT.
- Setup/cleanup: Create two isolated users; restore user A's lock state.

### LOGIN-CAND-02 — Unknown-email failures do not mutate a real account

- Missing scenario: Submit three failures for an unregistered email, then immediately log in with correct credentials for an existing user.
- Target: FR-02 counter ownership and non-disclosure.
- Why existing cases do not cover it: Unknown-email and counter tests exist independently, but no test connects the two state domains.
- Why AI initially missed it: `CROSS_FIELD_INTERACTION` — the suite did not combine identity resolution with counter persistence.
- Proposed oracle: Existing user's correct login succeeds with HTTP 200 and JWT; its lock state is unaffected.
- Setup/cleanup: Existing user starts unlocked; use a unique nonexistent email.

### LOGIN-CAND-03 — Parallel failures cannot lose or multiply increments

- Missing scenario: Send concurrent incorrect-password requests for one unlocked account and inspect the resulting counter/lock transition.
- Target: FR-02 exact +1 increment and third-failure lock boundary.
- Why existing cases do not cover it: Existing counter cases are sequential only.
- Why AI initially missed it: `STATE_COMPLEXITY` — concurrency introduces races outside a simple sequential transition model.
- Proposed oracle: Each completed failed login contributes exactly one increment; reaching three consecutive failures locks the account for 30 seconds.
- Setup/cleanup: Dedicated user, synchronized requests, authoritative state inspection, then state restoration.

### LOGIN-CAND-04 — Lock expiration remains scoped to the original lock timestamp

- Missing scenario: Attempt login multiple times during a lock, then retry just after 30 seconds measured from the original lock activation.
- Target: FR-02-R3 and `LOGIN-AMB-08`.
- Why existing cases do not cover it: LOGIN-AI-029 records one during-lock attempt but does not distinguish a fixed lock window from a sliding/extended window.
- Why AI initially missed it: `SPEC_AMBIGUITY` — the source defines duration but not whether attempts extend it.
- Proposed oracle: `SPEC_UNDEFINED`; record whether the implementation uses fixed or sliding expiration without declaring a defect until the ambiguity is resolved.
- Setup/cleanup: Controllable timing and dedicated account.

### LOGIN-CAND-05 — Oversized credential input fails safely

- Missing scenario: Submit very large email and password strings within the HTTP client's supported request size.
- Target: Login robustness, FR-02 non-disclosure, and security resilience.
- Why existing cases do not cover it: Empty and wrong-type boundaries are covered, but no upper-size stress partition exists because no maximum length is specified.
- Why AI initially missed it: `SPEC_AMBIGUITY` — absent maximum lengths made ordinary boundary-value generation stop at the empty boundary.
- Proposed oracle: Status is `SPEC_UNDEFINED`; response must be controlled, must not expose internals, and must not issue a token.
- Setup/cleanup: Isolated account state; record payload sizes used.

### LOGIN-CAND-06 — Content-Type mismatch does not authenticate accidentally

- Missing scenario: Send valid-looking credentials as `text/plain` and as form data rather than documented JSON.
- Target: Documented JSON request contract and safe error handling.
- Why existing cases do not cover it: Malformed JSON is tested only under `application/json`; transport representation is not varied.
- Why AI initially missed it: `API_CHARACTERISTIC` — the original partitions focused on body fields after JSON parsing.
- Proposed oracle: Exact status is `SPEC_UNDEFINED`; requests must not authenticate accidentally or expose internal errors.
- Setup/cleanup: None beyond an unlocked test account.

### LOGIN-CAND-07 — Unicode-confusable email identity is characterized

- Missing scenario: Replace an ASCII character in a registered email with a visually similar Unicode code point while using the correct password.
- Target: Identity matching, non-disclosure, and `LOGIN-AMB-04` normalization behavior.
- Why existing cases do not cover it: Case and surrounding whitespace are covered, but Unicode normalization/confusables are not.
- Why AI initially missed it: `SECURITY_CONTEXT` — visually confusable identifiers require an adversarial internationalization perspective.
- Proposed oracle: `SPEC_UNDEFINED`; record normalization behavior, do not issue a token for a different stored identity, and do not disclose account existence.
- Setup/cleanup: Use a controlled registered ASCII email and record exact code points.

## Human selection requirement

Select, modify, or reject each candidate. At least five accepted cases are required. Only explicitly accepted cases will be converted to `tests/login/human-tests.yaml` with `source: HUMAN` and `human_confirmation: true`.
