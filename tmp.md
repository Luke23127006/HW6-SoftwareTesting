# HUMAN GATE CI-REVERT-01

Status: WAITING_FOR_HUMAN

Reason for stopping: Codex has restored the valid `COUPON-AI-002` expectation locally, but the assignment requires the temporary intentional failure to be reverted in real repository history. Codex must not fabricate the revert commit SHA.

## Human task

1. Review that `postman/HW06.ci-demonstration.postman_collection.json` again expects `discount_amount` equal to `50000` and contains no `50001` assertion.
2. Commit and push this restoration with a clear revert message.
3. Fill the real commit SHA below and set `Decision: APPROVED`.

## Required evidence

- Revert commit SHA: PENDING
- Restored assertion: `pm.expect(body.discount_amount).to.eql(50000)`
- Temporary value `50001` absent: APPROVED

Decision: PENDING

After filling the real revert SHA, ask Codex to continue.
