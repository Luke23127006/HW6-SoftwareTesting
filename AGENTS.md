# HW06 Agent Rules

These rules apply to every AI interaction related to this repository.

## Sources of truth

Use these sources before making testing decisions:

1. `source/assignment.md`
2. `source/api_specification.md`
3. `source/system_requirements.md`

Do not silently replace missing source details with generic API-testing assumptions. Use `SPEC_UNDEFINED` or record an ambiguity when the supplied source does not define a value.

## Selected APIs

- Pool A / FR-02: `POST /api/login`
- Pool B / FR-09: `POST /api/apply-coupon`
- Pool C / FR-17: `POST /api/admin/coupons`

## Human-review boundary

AI may suggest `VALID`, `INVALID`, or `INCOMPLETE`, but it MUST NOT populate the final human verdict.

AI may propose additional tests, but a case becomes `source: HUMAN` only after explicit student acceptance and `human_confirmation: true`.

Never fabricate:

- Newman execution results
- screenshots
- GitHub Issue links or issue numbers
- GitHub Actions links
- commit hashes
- human-review decisions
- execution evidence
- the self-drawn AI test-generator diagram

## Mandatory AI Audit rule

After every HW06-related user prompt that produces analysis, code, test cases, documentation, or modifies an artifact:

1. Capture the exact user prompt.
2. Produce a concise factual summary of the AI response.
3. Record the AI tool/model when known.
4. Record local date and time.
5. Record created or modified artifacts.
6. Append a new entry to `docs/ai-audit.md` using the `audit-logger` workflow.
7. Never overwrite an earlier audit entry.
8. If a verbatim/full AI output is retained, store it under `ai-logs/` and reference it from the audit entry.

Do not log irrelevant chat that does not affect HW06 work.
