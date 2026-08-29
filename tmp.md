# HUMAN GATE B1 — Confirm SUT Bug Candidates

**Gate ID:** BUG-CANDIDATES-01  
**Status:** WAITING_FOR_HUMAN  
**Decision:** PENDING

## Reason for stopping

The first real Newman run produced eight requirement-backed `SUT_BUG_CANDIDATE` items. A failed test is not automatically a bug, and Codex cannot make the final defect decision for the student.

## Exact human task

Review `reports/failure-analysis.md` and decide `CONFIRM_BUG`, `REJECT_BUG`, or `NEEDS_RERUN` for each group:

| Group | Tests | Requirement | Decision |
| --- | --- | --- | --- |
| B1 — Incorrect percent calculation | COUPON-AI-001, COUPON-AI-017 | FR-09 percent formula | PENDING |
| B2 — Minimum equality rejected | COUPON-AI-007 | FR-09 C3 (`>=`) | PENDING |
| B3 — Apply Coupon ignores JWT | COUPON-AI-009, 010, 011 | FR-09 C4, SEC-02 | PENDING |
| B4 — Admin accepts missing required fields | ADMIN-COUPON-AI-008, 032 | FR-17 | PENDING |

The other 18 failures are classified `DATA_SETUP_FAILURE` and are not offered as bugs.

## Evidence to review

- `reports/newman/report.json`
- `reports/newman/report.html`
- `reports/results.json`
- `reports/failure-analysis.md`
- `docs/test-summary.md`

## Required human fields

- Decision for B1: PENDING
- Decision for B2: PENDING
- Decision for B3: PENDING
- Decision for B4: PENDING
- Human reasoning for each confirmed/rejected group: PENDING_HUMAN_ACTION
- Overall `Decision`: `APPROVED`, `MODIFIED`, or `REJECTED`

## Completion instructions

Update this file or reply with explicit decisions and reasoning for B1–B4, then ask Codex to continue. Confirmed groups may proceed to reproducible Markdown bug reports. Real GitHub Issue creation/URLs/screenshots will require a later human gate.
