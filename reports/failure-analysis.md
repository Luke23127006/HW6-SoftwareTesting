# Failure Analysis

> Based on the real Newman report. SUT bug candidates require explicit student confirmation before bug reporting.

## Run summary

- Executed items: **133**
- Passed items: **107**
- Failed items: **26**
- Failed assertions: **36**
- Failed test scripts: **1**

## DATA_SETUP_FAILURE — 18 items

### Shared Login state / missing users

- `LOGIN-AI-001`, `002`, `020`, `027`, `028`, `033`, `034`, `035`, `036`: the shared seeded user was already locked; expected success preconditions were not restored.
- `LOGIN-HUMAN-001`, `002`: required secondary/existing users and state sequences were not created.

### Coupon usage fixtures

- `COUPON-AI-015`, `016`: max/max+ usage rows were not established before execution.

### Admin unique-code fixtures

- `ADMIN-COUPON-AI-001`, `002`, `018`, `021`, `024`: actual response was `500 SQLITE_CONSTRAINT UNIQUE`; the supposedly unique codes already existed, so the valid-create precondition was false.

These failures must be repaired and rerun; they are not bug evidence.

## SUT_BUG_CANDIDATE — 8 items

### FR-09 percent formula

- `COUPON-AI-001`: total 500000 with SAVE10 returned `discount_amount = -4500000` and `final_amount = 5000000`, contradicting `discount = total × value / 100`.
- `COUPON-AI-017`: total 1000000 with SAVE10 returned `discount_amount = -9000000` and `final_amount = 10000000`.

### FR-09 inclusive threshold

- `COUPON-AI-007`: total exactly 300000 for SAVE10 was rejected with HTTP 400, contradicting C3 `total_amount >= min_order_amount`.

### FR-09 authentication

- `COUPON-AI-009`: missing Authorization returned HTTP 200 and applied the coupon.
- `COUPON-AI-010`: malformed JWT returned HTTP 200 and applied the coupon.
- `COUPON-AI-011`: expired JWT returned HTTP 200 and applied the coupon.
- These contradict C4 and SEC-02, subject to human confirmation.

### FR-17 required fields

- `ADMIN-COUPON-AI-008`: missing required `code` returned HTTP 200 and created coupon id 43.
- `ADMIN-COUPON-AI-032`: empty body returned HTTP 200 and created coupon id 45.
- These contradict FR-17 required-field rules, subject to human confirmation.

## Next action

1. Student confirms or rejects each bug-candidate group.
2. Repair isolated setup/state generation for the 18 setup failures.
3. Rerun affected tests and preserve new real evidence.
4. Create bug reports only for human-confirmed, reproducible SUT defects.
