# HW06 Current Context

## Project

Course assignment: **HW06-AI — API Testing**

Repository root:

```text
D:\Software Engineer\Sofware Testing\HW6
```

The project uses Codex with repository-local Agent Skills under:

```text
.agents/skills/
```

Root-level AI rules are in:

```text
AGENTS.md
```

Before doing HW06 work, read `AGENTS.md`.

---

## Assignment Goal

Test 3 APIs from the EShop SUT.

Required pipeline for each API:

```text
spec analysis
→ AI test generation
→ human audit
→ human-added tests
→ Postman implementation
→ Newman execution
→ failure analysis
→ bug reporting if confirmed
```

Global requirements also include:

```text
Postman features
CI/CD integration
AI-driven API test generator
AI Critique
AI Audit Report
final report
submission validation
```

---

## Selected APIs

These APIs are final and should not be changed unless explicitly requested by the student.

### Pool A — FR-02 Login

```http
POST /api/login
```

Main focus:

- email/password partitions
- successful JWT response
- failed-login counter
- account lock after 3 consecutive failures
- 30-second lock duration
- information disclosure
- SQL injection probes
- response schema

---

### Pool B — FR-09 Apply Coupon

```http
POST /api/apply-coupon
```

Main focus:

- C1: coupon exists and active
- C2: coupon not expired
- C3: total >= minimum order amount
- C4: valid authentication
- C5: user usage count below maximum
- fixed discount
- percent discount
- threshold boundaries
- JWT identity vs body `user_id`
- response schema

Known example coupons from requirements:

```text
SAVE10
BIGBUY
VIP100
EXPIRED
```

---

### Pool C — FR-17 Admin Create Coupon

```http
POST /api/admin/coupons
```

Main focus:

- valid JWT
- admin role
- unique `code`
- `type` is `percent` or `fixed`
- `discount_value > 0`
- `min_order_amount >= 0`
- `max_uses_per_user >= 1`
- `expired_at`
- malformed types
- authorization
- response/persistence behavior

---

## Minimum Test Requirements

Per API:

```text
>= 35 AI-generated test cases
>= 5 human-added test cases
```

Overall minimum target:

```text
>= 105 AI-generated tests
>= 15 human-added tests
>= 120 total tests
```

Quality and coverage matter more than inflating test count.

---

## Source of Truth

Do not guess requirements.

Read these files:

```text
requirements/req_en.md
requirements/req_vi.md

eshop-sut/api_specification.md
eshop-sut/README.md
```

The SUT source is available under:

```text
eshop-sut/
```

Important backend files include:

```text
eshop-sut/backend/server.js
eshop-sut/backend/database.js
eshop-sut/backend/database.sqlite
eshop-sut/backend/package.json
```

Source code may be inspected to understand implementation or test setup, but expected behavior must remain traceable to the supplied requirements/specification.

If the expected behavior is not defined by the source documents, use:

```text
SPEC_UNDEFINED
```

Do not silently assume conventional HTTP status codes.

---

## Repository Structure

Important project areas:

```text
.agents/skills/
.github/workflows/
config/
docs/
eshop-sut/
generator/
requirements/
schemas/
state/
tests/
postman/
reports/
evidence/
bugs/
ai-logs/
```

Selected API workspaces:

```text
tests/login/
tests/apply-coupon/
tests/admin-create-coupon/
```

---

## Agent Skills

Available skills:

```text
hw06-orchestrator
api-spec-analyzer
api-test-generator
test-case-auditor
test-case-extender
postman-test-builder
test-result-analyzer
bug-report-writer
cicd-helper
report-writer
ai-critique-writer
submission-validator
audit-logger
```

Use specialist skills instead of implementing the entire workflow inside one prompt.

---

## Canonical Artifact Flow

For each API:

```text
api-context.yaml
        ↓
generated-tests.yaml
        ↓
coverage.json / coverage.md
        ↓
audit.yaml
        ↓
human-tests.yaml
        ↓
final-tests.yaml
        ↓
Postman collection
        ↓
Newman execution
        ↓
results.json
        ↓
failure-analysis.md
```

Expected files per API:

```text
tests/<api>/
├── api-context.yaml
├── traceability.md
├── generated-tests.yaml
├── coverage.json
├── coverage.md
├── audit.yaml
├── audit.md
├── gap-analysis.md
├── human-tests.yaml
└── final-tests.yaml
```

---

## Test Case Contract

Use the shared schema:

```text
schemas/test-case.schema.json
```

Typical test:

```yaml
id: LOGIN-AI-001
source: AI
title: Login with valid credentials

requirements:
  - FR-02

techniques:
  - equivalence_partitioning

category: functional
priority: high

preconditions:
  - Test user exists.
  - Account is not locked.

request:
  method: POST
  path: /api/login
  headers: {}
  body:
    email: test@eshop.com
    password: Test1234!

expected:
  status: 200
  assertions:
    - response contains token
    - response does not expose password

cleanup: []

rationale: Valid equivalence partition.
```

---

## AI Test Generation Rule

Do not generate all test cases in one generic pass.

Use multiple passes:

```text
1. happy path
2. equivalence partitioning
3. boundary values
4. authentication / authorization
5. security
6. state transitions
7. schema validation
8. cross-field interactions
9. deduplication
10. coverage analysis
11. fill meaningful gaps
```

---

## Human Audit Boundary

Every AI-generated test must be reviewed by the student.

Allowed final verdicts:

```text
VALID
INVALID
INCOMPLETE
```

AI may provide:

```yaml
ai_review:
  suggested_verdict:
  reasoning:
```

AI MUST NOT invent:

```yaml
human_review:
  verdict:
  reasoning:
```

The student must make the final decision.

For INVALID or INCOMPLETE cases, preserve the original AI test and record the correction.

---

## Human-Added Test Boundary

AI may identify coverage gaps and propose candidate ideas.

A test can only be stored as:

```yaml
source: HUMAN
human_confirmation: true
```

after explicit student acceptance or modification.

Do not relabel AI-written tests as human-written just to satisfy the count.

Each human-added test should explain why the AI missed it.

---

## Execution Requirements

Default toolchain:

```text
Postman
Newman
```

Every request must include:

```http
X-Student-Id: {{studentId}}
```

The student ID comes from:

```text
config/hw06.yaml
```

Do not hardcode or invent it.

Real execution should produce:

```text
reports/newman/report.json
reports/newman/report.html
```

JSON is for machine analysis.
HTML is submission evidence.

---

## Failure Classification

A failed test is not automatically a bug.

Classify failures as:

```text
SUT_BUG_CANDIDATE
TEST_DEFECT
ENVIRONMENT_FAILURE
SPECIFICATION_GAP
DATA_SETUP_FAILURE
```

A bug report may only be created after human confirmation.

---

## Evidence That Must Be Real

Never fabricate:

```text
Newman output
screenshots
X-Student-Id evidence
GitHub Actions links
GitHub Actions screenshots
commit hashes
GitHub Issue numbers
GitHub Issue URLs
actual HTTP responses
human audit decisions
human-added ownership
self-drawn generator diagram
```

Use `PENDING_HUMAN_ACTION` or a TODO when real evidence is not yet available.

---

## CI/CD Requirement

Integrate Newman into the repository pipeline.

Need two real runs:

```text
1. all tests passing
2. one intentionally failing test
```

For the failing demonstration, prefer changing one test assertion temporarily rather than breaking the SUT.

Capture:

```text
commit SHA
Actions run URL
screenshot
result
```

Then revert the deliberate failure.

---

## AI-Driven Test Generator

The main assignment-facing generator is conceptually:

```text
API Specification
        ↓
Spec Analyzer
        ↓
Structured API Context
        ↓
AI Test Generator
        ↓
Multi-pass Test Design
        ↓
Coverage Validator
        ↓
Generated Test Suite
```

Pseudocode:

```text
generator/pseudocode.md
```

The final architecture diagram must be drawn by the student.
AI must not generate the final diagram artifact.

---

## AI Audit

Every relevant Codex interaction must be appended to:

```text
docs/ai-audit.md
```

Use:

```text
audit-logger
```

Audit entry should contain:

```text
interaction ID
tool/model
timestamp
exact user prompt
concise AI response summary
artifact paths
optional raw output reference
```

Never overwrite earlier entries.

---

## Main Documentation

Important final documents:

```text
docs/report.md
docs/report.pdf

docs/ai-audit.md
docs/ai-audit.pdf

docs/ai-critique.md
docs/cicd-report.md
docs/test-summary.md
docs/bugs.md
```

The AI Critique must be based on actual audit/execution evidence and should be 200–300 words.

---

## Current Working Principle

Do the assignment incrementally.

Do not jump directly to Postman implementation or final reporting.

For one API, complete:

```text
analysis
→ generation
→ human audit
→ human extension
```

before treating its test design as final.

Use `state/hw06-state.yaml` to track progress.

At the end of every meaningful step:

```text
1. validate artifact
2. update workflow state
3. append AI Audit entry
4. commit the workflow step
```

Use small Git commits because the assignment expects workflow history.
