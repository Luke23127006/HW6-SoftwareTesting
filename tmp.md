# HUMAN GATE B2 — Create Real GitHub Issues

**Gate ID:** GITHUB-BUG-ISSUES-01  
**Status:** WAITING_FOR_HUMAN  
**Decision:** PENDING

## Reason for stopping

Four defects were confirmed and documented locally. HW06 requires real GitHub Issues with screenshots. Codex must not invent issue URLs, numbers, or screenshots.

## Exact human task

Create one real GitHub Issue for each report, copying its reproducible content:

- `bugs/BUG-001.md` — incorrect percent calculation
- `bugs/BUG-002.md` — equality at minimum rejected
- `bugs/BUG-003.md` — Apply Coupon accepts invalid/missing JWT
- `bugs/BUG-004.md` — Admin accepts missing required coupon fields

Attach readable real evidence to each issue. Then save screenshots under `evidence/` and fill:

| Bug     | Issue number | Real GitHub URL      | Screenshot path      |
| ------- | ------------ | -------------------- | -------------------- |
| BUG-001 | PENDING      | PENDING_HUMAN_ACTION | PENDING_HUMAN_ACTION |
| BUG-002 | PENDING      | PENDING_HUMAN_ACTION | PENDING_HUMAN_ACTION |
| BUG-003 | PENDING      | PENDING_HUMAN_ACTION | PENDING_HUMAN_ACTION |
| BUG-004 | PENDING      | PENDING_HUMAN_ACTION | PENDING_HUMAN_ACTION |

## Evidence required

- Four real issue numbers and direct URLs.
- Four readable screenshots showing the created issues/evidence.
- URLs are accessible in the intended public repository.
- Set overall `Decision` to `APPROVED`.

**Human notes:** PENDING_HUMAN_ACTION

## Completion instructions

Update this file and ask Codex to continue. Codex will verify the supplied files/URLs syntactically, update each local bug report, archive this gate, and continue. It will not fabricate or silently replace missing evidence.
