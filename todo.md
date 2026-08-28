# HW06 TODO — Codex Execution Plan

## How to Use This File

This file is the operational roadmap for Codex.

Rules:

1. Work from top to bottom unless a task explicitly says it can run in parallel.
2. Do not mark human-only gates complete.
3. After every meaningful Codex interaction:
   - update relevant artifact;
   - validate it;
   - update `state/hw06-state.yaml`;
   - append `docs/ai-audit.md`;
   - suggest a Git commit.
4. Before starting a phase, read the referenced skill's `SKILL.md`.
5. Stop and ask the student only at explicit `HUMAN GATE` steps.
6. Never fabricate execution or evidence.

---

# Phase 0 — Verify Repository Setup

## 0.1 Read Context

- [ ] Read `AGENTS.md`
- [ ] Read `current_context.md`
- [ ] Read `config/hw06.yaml`
- [ ] Read `state/hw06-state.yaml`

## 0.2 Check Sources

Confirm these files exist:

- [ ] `requirements/req_en.md`
- [ ] `requirements/req_vi.md`
- [ ] `eshop-sut/api_specification.md`
- [ ] `eshop-sut/README.md`

## 0.3 Check Agent Skills

Confirm all exist:

- [ ] `.agents/skills/hw06-orchestrator/SKILL.md`
- [ ] `.agents/skills/api-spec-analyzer/SKILL.md`
- [ ] `.agents/skills/api-test-generator/SKILL.md`
- [ ] `.agents/skills/test-case-auditor/SKILL.md`
- [ ] `.agents/skills/test-case-extender/SKILL.md`
- [ ] `.agents/skills/postman-test-builder/SKILL.md`
- [ ] `.agents/skills/test-result-analyzer/SKILL.md`
- [ ] `.agents/skills/bug-report-writer/SKILL.md`
- [ ] `.agents/skills/cicd-helper/SKILL.md`
- [ ] `.agents/skills/report-writer/SKILL.md`
- [ ] `.agents/skills/ai-critique-writer/SKILL.md`
- [ ] `.agents/skills/submission-validator/SKILL.md`
- [ ] `.agents/skills/audit-logger/SKILL.md`

## 0.4 Check Python Support

Run:

```powershell
python -m pip install -r requirements.txt
```

Then compile/check support scripts if useful.

## 0.5 Check Runtime Folders

Ensure:

```text
tests/login/
tests/apply-coupon/
tests/admin-create-coupon/
postman/data/
reports/newman/
evidence/
bugs/
ai-logs/
docs/report-sections/
```

exist.

## Exit Criteria

- [ ] Sources found
- [ ] Skills found
- [ ] Python dependencies installed
- [ ] Runtime folders ready

Suggested commit:

```text
chore: finalize HW06 agent workflow setup
```

---

# Phase 1 — Inspect the SUT Before Test Design

Purpose: understand how to run the backend and identify useful setup/cleanup endpoints.

Do not use source code to redefine expected behavior.

## 1.1 Backend Startup

Inspect:

```text
eshop-sut/backend/package.json
eshop-sut/backend/server.js
eshop-sut/setup_guide.md
eshop-sut/run_servers.bat
```

Determine:

- [ ] backend install command
- [ ] backend start command
- [ ] expected port
- [ ] database initialization behavior
- [ ] whether database state resets automatically

## 1.2 Selected Endpoints

Locate implementation for:

```text
POST /api/login
POST /api/apply-coupon
POST /api/admin/coupons
```

Identify only practical test concerns:

- [ ] required setup data
- [ ] authentication flow
- [ ] response shape
- [ ] cleanup endpoints
- [ ] mutable database state
- [ ] whether tests can interfere with one another

## 1.3 Fixtures

Determine IDs/fixtures needed for execution.

Do not hardcode unstable IDs when runtime creation is possible.

## Exit Criteria

Create/update a concise execution note if necessary:

```text
docs/test-environment.md
```

Suggested commit:

```text
docs: document SUT API test environment
```

---

# Phase 2 — API A: Login Specification Analysis

Skill:

```text
api-spec-analyzer
```

Input API:

```text
login
```

## 2.1 Analyze

Create:

- [ ] `tests/login/api-context.yaml`
- [ ] `tests/login/traceability.md`

Must capture:

- [ ] request contract
- [ ] success response
- [ ] failed-login counter
- [ ] 3-failure lock boundary
- [ ] 30-second lock
- [ ] relevant SEC requirements
- [ ] setup dependencies
- [ ] ambiguities

## 2.2 Validate

Run:

```powershell
python .agents/skills/api-spec-analyzer/scripts/validate_context.py tests/login/api-context.yaml
```

## 2.3 Update State

Set:

```text
login.spec_analysis = done
```

## Exit Criteria

- [ ] context validates
- [ ] no unsupported assumptions
- [ ] traceability exists

Suggested commit:

```text
test(login): analyze API specification
```

---

# Phase 3 — API A: Login AI Test Generation

Skill:

```text
api-test-generator
```

## 3.1 Generate in Multiple Passes

Generate sequentially:

- [ ] happy path
- [ ] equivalence partitions
- [ ] boundaries
- [ ] authentication/security
- [ ] state transitions
- [ ] schema tests
- [ ] error handling
- [ ] cross-field cases
- [ ] deduplicate

Target:

```text
>= 35 tests
```

Output:

- [ ] `tests/login/generated-tests.yaml`

## 3.2 Coverage

Run:

```powershell
python .agents/skills/api-test-generator/scripts/validate_test_suite.py tests/login/generated-tests.yaml
python .agents/skills/api-test-generator/scripts/coverage_check.py tests/login/generated-tests.yaml tests/login/api-context.yaml
```

Create:

- [ ] `tests/login/coverage.json`
- [ ] `tests/login/coverage.md`

## 3.3 Update State

Set:

```text
login.ai_generation = done
login.generated_count = actual count
```

## Exit Criteria

- [ ] >=35 meaningful tests
- [ ] no duplicate IDs
- [ ] meaningful state/security/schema coverage
- [ ] coverage warnings reviewed

Suggested commit:

```text
test(login): generate AI API test suite
```

---

# Phase 4 — API A: Human Audit

Skill:

```text
test-case-auditor
```

## 4.1 Prepare Audit

Run:

```powershell
python .agents/skills/test-case-auditor/scripts/prepare_audit.py tests/login/generated-tests.yaml tests/login/audit.yaml
```

Codex may fill only:

```text
ai_review.suggested_verdict
ai_review.reasoning
```

Codex must NOT fill final human verdicts.

---

## HUMAN GATE A1 — Review Login Tests

Student reviews every test and fills:

```text
human_review.verdict
human_review.reasoning
```

Allowed verdicts:

```text
VALID
INVALID
INCOMPLETE
```

For INVALID/INCOMPLETE cases, student confirms correction.

Codex may help explain suspicious cases but must not impersonate the human reviewer.

---

## 4.2 Validate Audit

After student review:

```powershell
python .agents/skills/test-case-auditor/scripts/validate_human_audit.py tests/login/audit.yaml
```

Create:

- [ ] `tests/login/audit.md`
- [ ] corrected AI tests if required

## 4.3 Update State

Only after validator succeeds:

```text
login.human_audit = done
```

Suggested commit:

```text
test(login): complete human audit
```

---

# Phase 5 — API A: Human Extension

Skill:

```text
test-case-extender
```

## 5.1 Gap Analysis

Create:

- [ ] `tests/login/gap-analysis.md`

Codex identifies candidate gaps, especially:

- [ ] security
- [ ] state interactions
- [ ] assumptions AI made incorrectly
- [ ] hard-to-model setup

---

## HUMAN GATE A2 — Select Human Tests

Codex proposes candidate ideas.

Student must accept/modify at least 5.

Only then persist:

```yaml
source: HUMAN
human_confirmation: true
```

---

## 5.2 Validate

Create:

- [ ] `tests/login/human-tests.yaml`
- [ ] `tests/login/final-tests.yaml`

Run:

```powershell
python .agents/skills/test-case-extender/scripts/validate_extensions.py tests/login/human-tests.yaml
```

## 5.3 Update State

Set:

```text
login.human_added_count = actual count
```

Suggested commit:

```text
test(login): add human-designed test cases
```

---

# Phase 6 — Repeat Design Pipeline for API B: Apply Coupon

Repeat Phases 2–5 using:

```text
tests/apply-coupon/
```

Focus on:

- [ ] C1 coupon exists/active
- [ ] C2 expiration
- [ ] C3 minimum threshold
- [ ] C4 authentication
- [ ] C5 usage count
- [ ] threshold min-1/min/min+1
- [ ] percent calculation
- [ ] fixed calculation
- [ ] JWT identity vs body `user_id`
- [ ] malformed values
- [ ] schema

Expected artifacts:

```text
tests/apply-coupon/api-context.yaml
tests/apply-coupon/traceability.md
tests/apply-coupon/generated-tests.yaml
tests/apply-coupon/coverage.json
tests/apply-coupon/coverage.md
tests/apply-coupon/audit.yaml
tests/apply-coupon/audit.md
tests/apply-coupon/gap-analysis.md
tests/apply-coupon/human-tests.yaml
tests/apply-coupon/final-tests.yaml
```

Use explicit human gates for:

- [ ] audit
- [ ] human-added tests

Suggested commits:

```text
test(coupon): analyze API specification
test(coupon): generate AI API test suite
test(coupon): complete human audit
test(coupon): add human-designed test cases
```

---

# Phase 7 — Repeat Design Pipeline for API C: Admin Create Coupon

Repeat Phases 2–5 using:

```text
tests/admin-create-coupon/
```

Focus on:

- [ ] no token
- [ ] invalid token
- [ ] normal user token
- [ ] admin token
- [ ] duplicate code
- [ ] type enum
- [ ] discount_value > 0
- [ ] min_order_amount >= 0
- [ ] max_uses_per_user >= 1
- [ ] expired_at
- [ ] wrong types
- [ ] schema
- [ ] persistence
- [ ] cleanup

Use explicit human gates for:

- [ ] audit
- [ ] human-added tests

Suggested commits:

```text
test(admin-coupon): analyze API specification
test(admin-coupon): generate AI API test suite
test(admin-coupon): complete human audit
test(admin-coupon): add human-designed test cases
```

---

# Phase 8 — Cross-API Final Test Review

Before Postman generation, verify:

## 8.1 Counts

- [ ] Login AI >= 35
- [ ] Login Human >= 5
- [ ] Apply Coupon AI >= 35
- [ ] Apply Coupon Human >= 5
- [ ] Admin Coupon AI >= 35
- [ ] Admin Coupon Human >= 5

## 8.2 Contracts

- [ ] all final tests conform to `schemas/test-case.schema.json`
- [ ] no rejected AI cases in final suites
- [ ] all human tests have confirmation
- [ ] no duplicated test IDs
- [ ] setup/cleanup is executable

## Exit Criteria

Three stable files:

```text
tests/login/final-tests.yaml
tests/apply-coupon/final-tests.yaml
tests/admin-create-coupon/final-tests.yaml
```

---

# Phase 9 — Build Postman Collection

Skill:

```text
postman-test-builder
```

## 9.1 Build

Run:

```powershell
python .agents/skills/postman-test-builder/scripts/build_collection.py
```

Expected:

```text
postman/HW06.postman_collection.json
postman/local.postman_environment.json
```

## 9.2 Replace Placeholder Assertions

IMPORTANT:

The initial builder may leave placeholder assertion blocks.

Codex must convert every reviewed natural-language expected assertion into a real Postman assertion.

No final test may retain:

```javascript
pm.expect(true).to.eql(true);
```

## 9.3 Add Setup

Implement as needed:

- [ ] normal user login/token capture
- [ ] admin login/token capture
- [ ] dynamic created coupon IDs
- [ ] setup state
- [ ] cleanup state

## 9.4 X-Student-Id

Ensure collection-level script injects:

```http
X-Student-Id: {{studentId}}
```

Set real Student ID only in the environment/config.

## 9.5 Validate

Run:

```powershell
python .agents/skills/postman-test-builder/scripts/validate_collection.py postman/HW06.postman_collection.json
```

Resolve all errors and placeholder warnings.

Suggested commit:

```text
test(postman): implement reviewed API test collection
```

---

# Phase 10 — Local Postman/Newman Execution

## HUMAN GATE E1 — Student ID

Student provides/sets the actual Student ID in:

```text
config/hw06.yaml
postman/local.postman_environment.json
```

Codex must not invent it.

## 10.1 Start SUT

Use the actual backend startup command identified in Phase 1.

Verify:

```text
http://localhost:3000
```

or the actual configured backend URL.

## 10.2 Newman

Run:

```powershell
newman run postman/HW06.postman_collection.json `
  -e postman/local.postman_environment.json `
  -r cli,json,htmlextra `
  --reporter-json-export reports/newman/report.json `
  --reporter-htmlextra-export reports/newman/report.html
```

If `htmlextra` is missing:

```powershell
npm install -g newman newman-reporter-htmlextra
```

## HUMAN GATE E2 — X-Student-Id Evidence

Student opens Postman console / execution evidence and captures the required real screenshot proving the header is sent.

Save under:

```text
evidence/
```

Codex must not generate this screenshot.

Suggested commit:

```text
test: execute API suite with Newman
```

---

# Phase 11 — Analyze Execution Results

Skill:

```text
test-result-analyzer
```

## 11.1 Parse

Run:

```powershell
python .agents/skills/test-result-analyzer/scripts/parse_newman.py reports/newman/report.json
```

Expected:

```text
reports/results.json
reports/failure-analysis.md
docs/test-summary.md
```

## 11.2 Classify Every Failure

Review each failure and classify:

```text
SUT_BUG_CANDIDATE
TEST_DEFECT
ENVIRONMENT_FAILURE
SPECIFICATION_GAP
DATA_SETUP_FAILURE
```

Fix test defects/setup problems before declaring a SUT bug.

Re-run tests when necessary.

---

# Phase 12 — Confirm and Report Real Bugs

Skill:

```text
bug-report-writer
```

For every SUT bug candidate:

## HUMAN GATE B1 — Bug Confirmation

Student confirms whether it is a genuine bug.

If confirmed:

- [ ] create `bugs/BUG-XXX.md`
- [ ] include requirement
- [ ] include related test ID
- [ ] include steps
- [ ] include expected
- [ ] include actual
- [ ] include real evidence

## HUMAN GATE B2 — GitHub Issue

Student creates the real GitHub Issue and attaches screenshot.

Then update:

```text
GitHub Issue URL
issue number
screenshot reference
```

Do not create fake URLs.

Suggested commit:

```text
docs: add confirmed API bug reports
```

---

# Phase 13 — Postman Feature Inventory

Review the final collection and list only features actually used.

Potential features:

```text
workspace
collection
variables
environment
pre-request scripts
test scripts
data-driven Collection Runner
mock server
monitor
```

Do not claim unused features.

Update relevant report section.

---

# Phase 14 — CI/CD Integration

Skill:

```text
cicd-helper
```

## 14.1 Fix Workflow

Inspect current:

```text
.github/workflows/api-tests.yml
```

Replace placeholders with actual SUT commands.

Pipeline should:

- [ ] checkout
- [ ] setup Node
- [ ] install backend dependencies
- [ ] start backend
- [ ] wait until backend ready
- [ ] install Newman
- [ ] execute tests
- [ ] create JSON/HTML reports
- [ ] upload reports

## 14.2 Passing Run

Push commit with valid tests.

---

## HUMAN GATE CI1 — Capture PASS Evidence

Record:

```text
commit SHA
GitHub Actions URL
screenshot
```

---

## 14.3 Intentional Failure

Change exactly one test assertion temporarily.

Commit and push.

---

## HUMAN GATE CI2 — Capture FAIL Evidence

Record:

```text
commit SHA
GitHub Actions URL
screenshot
changed assertion
```

Then revert the deliberate failure.

## 14.4 CI/CD Report

Update:

```text
docs/cicd-report.md
```

Suggested commits:

```text
ci: run Newman API tests in GitHub Actions
test: demonstrate failing API assertion in CI
revert: restore valid API assertion
```

---

# Phase 15 — AI-Driven Test Generator Documentation

The actual Agent Skill is primarily:

```text
api-spec-analyzer
api-test-generator
```

with deterministic validators.

## 15.1 Pseudocode

Review/update:

```text
generator/pseudocode.md
```

Make sure it matches the implemented workflow.

## HUMAN GATE G1 — Self-Drawn Diagram

Student draws the final generator diagram manually.

Suggested conceptual flow:

```text
API Specification
→ Spec Analyzer
→ Structured API Context
→ Multi-Pass Generator
→ Deduplication
→ Coverage Validator
→ Test Suite
```

Save the student's diagram under:

```text
generator/
```

Codex must not generate the final diagram artifact.

Suggested commit:

```text
docs: document AI-driven API test generator
```

---

# Phase 16 — Write Main Report Incrementally

Skill:

```text
report-writer
```

Use actual artifacts only.

Populate:

- [ ] Introduction
- [ ] SUT/environment
- [ ] API selection
- [ ] methodology
- [ ] Login section
- [ ] Apply Coupon section
- [ ] Admin Coupon section
- [ ] Postman features
- [ ] CI/CD
- [ ] AI generator
- [ ] test summary
- [ ] bugs
- [ ] AI Audit appendix/reference

Do not fill missing evidence with invented values.

If evidence is missing:

```text
TODO
```

Assemble:

```powershell
python .agents/skills/report-writer/scripts/assemble_report.py
```

Suggested commit:

```text
docs: assemble HW06 API testing report
```

---

# Phase 17 — AI Critique

Skill:

```text
ai-critique-writer
```

Read actual:

```text
tests/*/audit.yaml
tests/*/human-tests.yaml
tests/*/gap-analysis.md
reports/failure-analysis.md
bugs/
docs/ai-audit.md
```

Draft:

```text
docs/ai-critique.md
```

Must cover:

- [ ] where AI was wrong/incomplete
- [ ] why AI missed it
- [ ] what was learned from collaborating with AI

Validate:

```powershell
python .agents/skills/ai-critique-writer/scripts/validate_word_count.py docs/ai-critique.md
```

Requirement:

```text
200–300 words
```

Suggested commit:

```text
docs: add AI collaboration critique
```

---

# Phase 18 — Export Required Submission Artifacts

Generate real final files:

- [ ] `docs/report.pdf`
- [ ] `docs/ai-audit.pdf`
- [ ] test cases Excel file
- [ ] Newman HTML report
- [ ] Postman collection JSON
- [ ] CI/CD report
- [ ] bug report
- [ ] screenshots
- [ ] GitHub links
- [ ] git log

Generate real git log:

```powershell
git log --oneline --decorate > git-log.txt
```

Do not leave placeholder text.

---

# Phase 19 — README Finalization

Update root:

```text
README.md
```

Include final:

- [ ] self-assessment table
- [ ] selected APIs
- [ ] AI-generated test count
- [ ] human-added test count
- [ ] executed count
- [ ] pass/fail count
- [ ] bug count
- [ ] public GitHub repository link
- [ ] main execution instructions

---

# Phase 20 — Final Submission Validation

Skill:

```text
submission-validator
```

Run:

```powershell
python .agents/skills/submission-validator/scripts/validate_submission.py
```

Resolve every blocker.

Do not weaken validator requirements just to obtain READY.

Expected final result:

```text
Status: READY
```

---

# Phase 21 — Final Manual Submission Check

## HUMAN GATE FINAL

Student manually verifies:

- [ ] public GitHub repo accessible
- [ ] all screenshots readable
- [ ] GitHub Issue links work
- [ ] GitHub Actions links work
- [ ] PDFs open correctly
- [ ] Excel opens correctly
- [ ] Newman HTML opens correctly
- [ ] self-drawn diagram included
- [ ] AI Audit complete
- [ ] final ZIP naming correct

Final ZIP naming format:

```text
<StudentID>_HW06_AI_API_<SelfAssessedGrade>.zip
```

Only after this manual check is the assignment ready to submit.

---

# Codex Default Next Action

If no phase has started yet:

```text
Start with Phase 0.
Verify setup.
Then inspect the backend execution environment.
Then run api-spec-analyzer for Login.
Do not generate Login tests until api-context.yaml validates.
```
