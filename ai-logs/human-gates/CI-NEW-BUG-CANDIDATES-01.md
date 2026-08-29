# HUMAN GATE CI-NEW-BUG-CANDIDATES-01 — Completed

Status: COMPLETED

## Human decision

The student explicitly approved all 11 candidates as `CONFIRM_BUG` and subsequently approved the following shared reason after reviewing the AI recommendation:

> I confirm these as genuine SUT defects because the clean CI run reproducibly returned HTTP 200 and created coupons despite an expired administrator token or request values that violate explicit FR-17 required-field, enum, and numeric constraints. The failures show that the SUT does not enforce documented requirements; they are not caused by missing fixtures, polluted data, or incorrect test expectations.

## Confirmed test IDs

- `ADMIN-COUPON-AI-006`
- `ADMIN-COUPON-AI-013`, `ADMIN-COUPON-AI-014`, `ADMIN-COUPON-AI-015`
- `ADMIN-COUPON-AI-016`, `ADMIN-COUPON-AI-017`, `ADMIN-COUPON-AI-022`, `ADMIN-COUPON-AI-023`, `ADMIN-COUPON-AI-025`, `ADMIN-COUPON-AI-026`, `ADMIN-COUPON-AI-028`

## Resolution

The confirmed findings were grouped into an extension of BUG-004 and new BUG-005 through BUG-007 reports. No expected result or valid defect-detecting assertion was weakened.
