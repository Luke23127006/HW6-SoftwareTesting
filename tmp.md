# HUMAN GATE CI-FAIL-01

Status: WAITING_FOR_HUMAN

Reason for stopping: The temporary demonstration collection contains exactly one intentionally impossible assertion. Codex must not fabricate the commit, Actions run, screenshot, or observed one-failure result.

## Temporary change

- File: `postman/HW06.ci-demonstration.postman_collection.json`
- Test: `COUPON-AI-002 - 1: discount_amount equals 50000`
- Valid assertion: `pm.expect(body.discount_amount).to.eql(50000)`
- Temporary assertion: `pm.expect(body.discount_amount).to.eql(50001)`
- Authoritative full collection: unchanged

## Human task

1. Commit and push this one temporary assertion change.
2. Manually run `HW06 API Tests` with `suite = demo`.
3. Verify exactly one assertion fails for `COUPON-AI-002`.
4. Save a readable screenshot under `evidence/ci/`.
5. Fill the real evidence below and set `Decision: APPROVED`.

## Required evidence

- Temporary commit SHA: PENDING
- GitHub Actions run/job URL: PENDING
- Screenshot path: PENDING
- Result: PENDING
- Failed assertion count: PENDING

Decision: PENDING

Do not revert the assertion until Codex validates and archives the failure evidence. After validation, Codex will restore `50000` and prepare the revert step.
