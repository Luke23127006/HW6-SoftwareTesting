# HUMAN GATE CI-DEMO-STRATEGY-01 — Completed

Status: COMPLETED

## Human decision

Decision: APPROVED

The student explicitly approved the complete transparent demonstration method with: “continue, I approved all”.

## Approved safeguards

- Preserve the authoritative 133-request collection and all confirmed defect assertions.
- Use a separately named smoke-subset collection only for CI mechanism demonstration.
- Label its PASS as a demonstration-subset PASS, not a full-suite PASS.
- Create exactly one intentional assertion failure only after a real subset PASS exists, then revert it.

## Resolution

Codex created the separate demonstration collection and added an explicit manual `full`/`demo` workflow selection. Normal push and pull-request runs continue to use the authoritative full suite.
