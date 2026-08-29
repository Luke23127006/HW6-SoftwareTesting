# AI Audit Report

> Append-only. Each relevant AI interaction gets one sequential entry.
## AI-001

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:27:29 +07

### Prompt

```text
Read AGENTS.md, current_context.md and todo.md.Follow todo.md from the first incomplete phase.Do not skip human gates.After each meaningful task, update state and AI audit as instructed.
```

### AI Response Summary

Read the repository rules, current context, TODO, configuration, workflow state, and required HW06 skill instructions. Completed Phase 0 by verifying all canonical source and skill files, confirming the declared Python dependencies are installed, creating all required runtime directories, and marking the Phase 0 checklist complete. Preserved the existing state schema because it contains no Phase 0 field, and identified the absent root-rules source/ paths as a repository ambiguity without substituting them silently.

### Artifacts

- `todo.md`
- `tests/login/.gitkeep`
- `tests/apply-coupon/.gitkeep`
- `tests/admin-create-coupon/.gitkeep`
- `postman/data/.gitkeep`
- `reports/newman/.gitkeep`
- `evidence/.gitkeep`
- `bugs/.gitkeep`
- `ai-logs/.gitkeep`
- `docs/report-sections/.gitkeep`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-002

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:28:48 +07

### Prompt

```text
Read AGENTS.md, current_context.md and todo.md.Follow todo.md from the first incomplete phase.Do not skip human gates.After each meaningful task, update state and AI audit as instructed.
```

### AI Response Summary

Completed Phase 1 by inspecting backend startup, database initialization, seed fixtures, and the three selected endpoint implementations. Created a concise test-environment note covering commands, port, automatic destructive reset behavior, setup and cleanup mechanics, mutable-state interference, and observed implementation/security concerns while keeping requirements as the test oracle. Updated the corresponding Phase 1 TODO checklist.

### Artifacts

- `docs/test-environment.md`
- `todo.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-003

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:30:56 +07

### Prompt

```text
Read AGENTS.md, current_context.md and todo.md.Follow todo.md from the first incomplete phase.Do not skip human gates.After each meaningful task, update state and AI audit as instructed.
```

### AI Response Summary

Completed and validated the Login specification analysis. Created a structured API context and traceability matrix covering the request/success contract, exact failed-attempt increment, three-failure lock boundary, 30-second duration, JWT behavior, relevant SEC-01 and SEC-05 requirements, state/setup dependencies, and explicit SPEC_UNDEFINED ambiguities. Updated Login specification state to done and marked the Phase 2 checklist complete.

### Artifacts

- `tests/login/api-context.yaml`
- `tests/login/traceability.md`
- `state/hw06-state.yaml`
- `todo.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-004

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:34:26 +07

### Prompt

```text
Read AGENTS.md, current_context.md and todo.md.Follow todo.md from the first incomplete phase.Do not skip human gates.After each meaningful task, update state and AI audit as instructed.
```

### AI Response Summary

Generated 38 traceable Login API tests through happy-path, equivalence, boundary, authentication, security, state-transition, schema, error-handling, cross-field, deduplication, coverage, and gap-filling passes. The suite validated successfully with no duplicate IDs and no coverage warnings; coverage includes seven state tests, eight security tests, two schema tests, and both relevant SEC requirements. Updated Login generation state and count and completed the Phase 3 TODO checklist.

### Artifacts

- `tests/login/generated-tests.yaml`
- `tests/login/coverage.json`
- `tests/login/coverage.md`
- `state/hw06-state.yaml`
- `todo.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-005

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:35:53 +07

### Prompt

```text
Read AGENTS.md, current_context.md and todo.md.Follow todo.md from the first incomplete phase.Do not skip human gates.After each meaningful task, update state and AI audit as instructed.
```

### AI Response Summary

Prepared the mandatory Login human-audit scaffold with 38 records matching all generated test IDs and verified that no human verdict or reasoning was prefilled. Kept login.human_audit pending and prepared HUMAN GATE A1 instructions requiring the student to review every case, supply a final verdict and reasoning, and provide corrections for INVALID or INCOMPLETE cases before validation can continue.

### Artifacts

- `tests/login/audit.yaml`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-006

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:56:29 +07

### Prompt

```text
the reason is it all meet the requirements, I approved all

continue todo
```

### AI Response Summary

Applied the student's explicit human decision to all 38 Login audit records: verdict VALID with the verbatim reasoning “It all meets the requirements.” The mandatory validator completed successfully with 38 VALID, 0 INVALID, and 0 INCOMPLETE. Created the human audit summary, marked login.human_audit done, archived HUMAN GATE A1, marked the audit summary TODO complete, and reset tmp.md.

### Artifacts

- `tests/login/audit.yaml`
- `tests/login/audit.md`
- `state/hw06-state.yaml`
- `todo.md`
- `ai-logs/human-gates/LOGIN-AUDIT-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-007

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-28 23:57:43 +07

### Prompt

```text
the reason is it all meet the requirements, I approved all

continue todo
```

### AI Response Summary

After completing and archiving the Login human audit, performed the Phase 5 post-audit gap analysis. Proposed seven distinct candidate tests covering cross-account lock isolation, unknown-email state isolation, concurrent failed-attempt races, fixed versus sliding lock expiration, oversized credentials, content-type mismatches, and Unicode-confusable identities. Marked only the gap-analysis preparation complete; no candidate was labeled HUMAN or confirmed on the student's behalf.

### Artifacts

- `tests/login/gap-analysis.md`
- `todo.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-008

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:01:51 +07

### Prompt

```text
I approve all, it's all good, continur
```

### AI Response Summary

Applied the student's explicit acceptance of all seven Login extension candidates. Created and validated seven source HUMAN tests with human_confirmation true, assembled a 45-case final Login suite containing 38 approved AI tests and seven confirmed human tests, verified zero duplicate IDs and zero schema errors, updated Login human-added state to seven, completed the corresponding TODO items, archived HUMAN GATE A2, and reset tmp.md.

### Artifacts

- `tests/login/human-tests.yaml`
- `tests/login/final-tests.yaml`
- `state/hw06-state.yaml`
- `todo.md`
- `ai-logs/human-gates/LOGIN-EXTEND-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-009

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:03:21 +07

### Prompt

```text
I approve all, it's all good, continur
```

### AI Response Summary

Completed and validated the Apply Coupon specification analysis for POST /api/apply-coupon. Created the structured context and traceability mapping for C1 through C5, fixed and percent formulas, final amount, JWT and SEC requirements, sample coupon fixtures, usage-state dependencies, and ten explicit specification ambiguities. Updated apply_coupon.spec_analysis to done.

### Artifacts

- `tests/apply-coupon/api-context.yaml`
- `tests/apply-coupon/traceability.md`
- `state/hw06-state.yaml`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-010

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:06:10 +07

### Prompt

```text
I approve all, it's all good, continur
```

### AI Response Summary

Generated and validated 36 Apply Coupon AI tests covering C1 through C5, min-1/min/min+1 boundaries, percent and fixed calculations, valid/missing/malformed/expired JWT behavior, JWT versus body user identity, usage-limit state, malformed fields, SQL injection, expiration and rounding ambiguities, and response schema. Coverage reported no warnings. Updated Apply Coupon generation state/count and prepared a 36-record human-audit scaffold without populating human decisions.

### Artifacts

- `tests/apply-coupon/generated-tests.yaml`
- `tests/apply-coupon/coverage.json`
- `tests/apply-coupon/coverage.md`
- `tests/apply-coupon/audit.yaml`
- `state/hw06-state.yaml`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-011

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:24:25 +07

### Prompt

```text
All tests meet the documented requirements
  and preserve SPEC_UNDEFINED where behavior is unspecified.
continue
```

### AI Response Summary

Applied the student's exact reasoning and VALID verdict to all 36 Apply Coupon audit records. The human-audit validator completed with 36 VALID, 0 INVALID, and 0 INCOMPLETE. Created the audit summary, marked apply_coupon.human_audit done, archived APPLY-COUPON-AUDIT-01, and reset tmp.md.

### Artifacts

- `tests/apply-coupon/audit.yaml`
- `tests/apply-coupon/audit.md`
- `state/hw06-state.yaml`
- `ai-logs/human-gates/APPLY-COUPON-AUDIT-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-012

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:25:17 +07

### Prompt

```text
All tests meet the documented requirements
  and preserve SPEC_UNDEFINED where behavior is unspecified.
continue
```

### AI Response Summary

Prepared the Apply Coupon post-audit gap analysis with seven distinct extension candidates: cross-user usage isolation, concurrent final-allowance races, very large numeric totals, fractional monetary totals, deleted/deactivated JWT subjects, duplicate user_id JSON keys, and coupon-deactivation races. No candidate was labeled HUMAN or confirmed on the student's behalf; a human selection gate is required.

### Artifacts

- `tests/apply-coupon/gap-analysis.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-013

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:27:31 +07

### Prompt

```text
I have reviewed and approve all, continue
```

### AI Response Summary

Applied the student's explicit acceptance of all seven Apply Coupon extension candidates. Created and validated seven source HUMAN tests with human_confirmation true, assembled and verified a 43-case final suite with 36 AI and seven human tests, zero duplicate IDs, and zero schema errors. Updated human-added state to seven, archived the extension gate, and reset tmp.md.

### Artifacts

- `tests/apply-coupon/human-tests.yaml`
- `tests/apply-coupon/final-tests.yaml`
- `state/hw06-state.yaml`
- `ai-logs/human-gates/APPLY-COUPON-EXTEND-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-014

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:31:10 +07

### Prompt

```text
I have reviewed and approve all, continue
```

### AI Response Summary

Completed and validated Admin Create Coupon specification analysis and generated 36 AI tests. The context traces FR-12/FR-17 and SEC-02/03/05, required fields, uniqueness, enum and numeric constraints, expiry, persistence, cleanup, and explicit ambiguities. The suite covers valid percent/fixed creation, missing/invalid/user tokens, duplicate codes, field boundaries and types, SQL injection, role escalation, persistence, partial-write prevention, and concurrent uniqueness with no coverage warnings. Updated specification/generation state and prepared a 36-record human-audit scaffold without human decisions.

### Artifacts

- `tests/admin-create-coupon/api-context.yaml`
- `tests/admin-create-coupon/traceability.md`
- `tests/admin-create-coupon/generated-tests.yaml`
- `tests/admin-create-coupon/coverage.json`
- `tests/admin-create-coupon/coverage.md`
- `tests/admin-create-coupon/audit.yaml`
- `state/hw06-state.yaml`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-015

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:41:29 +07

### Prompt

```text
All tests meet FR-12, FR-17, and relevant
  security requirements while preserving SPEC_UNDEFINED behavior.
continue
```

### AI Response Summary

Applied the student's exact reasoning and VALID verdict to all 36 Admin Create Coupon audit records. The human-audit validator completed with 36 VALID, 0 INVALID, and 0 INCOMPLETE. Created the audit summary, marked admin_create_coupon.human_audit done, archived ADMIN-COUPON-AUDIT-01, and reset tmp.md.

### Artifacts

- `tests/admin-create-coupon/audit.yaml`
- `tests/admin-create-coupon/audit.md`
- `state/hw06-state.yaml`
- `ai-logs/human-gates/ADMIN-COUPON-AUDIT-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-016

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:42:10 +07

### Prompt

```text
All tests meet FR-12, FR-17, and relevant
  security requirements while preserving SPEC_UNDEFINED behavior.
continue
```

### AI Response Summary

Prepared the Admin Create Coupon post-audit gap analysis with seven distinct candidates covering whitespace-normalized uniqueness, Unicode-confusable codes, concurrent admin/user requests, post-issuance role changes, fractional monetary interactions, extreme numeric values, and cleanup isolation. No candidate was labeled HUMAN or confirmed for the student; a human selection gate is required.

### Artifacts

- `tests/admin-create-coupon/gap-analysis.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-017

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:45:25 +07

### Prompt

```text
I have reviewed and approve all, continue
```

### AI Response Summary

Applied the student's explicit acceptance of all seven Admin Create Coupon extension candidates. Created and validated seven source HUMAN tests with human_confirmation true, assembled and verified a 43-case final suite with 36 AI and seven human tests, no duplicate IDs, and no schema errors. Updated human-added state to seven, archived the extension gate, and reset tmp.md.

### Artifacts

- `tests/admin-create-coupon/human-tests.yaml`
- `tests/admin-create-coupon/final-tests.yaml`
- `state/hw06-state.yaml`
- `ai-logs/human-gates/ADMIN-COUPON-EXTEND-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-018

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:46:11 +07

### Prompt

```text
I have reviewed and approve all, continue
```

### AI Response Summary

Completed Phase 8 cross-API final-suite review. Verified Login 45 total (38 AI, 7 confirmed human), Apply Coupon 43 total (36 AI, 7 confirmed human), and Admin Create Coupon 43 total (36 AI, 7 confirmed human). All 131 tests conform to the shared schema, all AI audit verdicts are VALID with reasoning, all human tests are confirmed, and there are no duplicate IDs. Marked the Phase 8 count and contract checklist complete.

### Artifacts

- `todo.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-019

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:48:24 +07

### Prompt

```text
I have reviewed and approve all, continue
```

### AI Response Summary

Completed Phase 9 Postman construction after normalizing YAML date literals that initially blocked JSON serialization. Generated the collection/environment, replaced all placeholder assertions with executable checks derived from the 131 reviewed tests, added two real login setup requests that capture normal-user and admin JWTs, added required environment variables and runtime coupon ID capture, and retained collection-level X-Student-Id injection. Structural validation passed for 133 executable requests with no placeholder assertions. The studentId remains CHANGE_ME pending the mandatory human gate. Marked Postman state done for all three APIs.

### Artifacts

- `tests/admin-create-coupon/generated-tests.yaml`
- `tests/admin-create-coupon/human-tests.yaml`
- `tests/admin-create-coupon/final-tests.yaml`
- `postman/HW06.postman_collection.json`
- `postman/local.postman_environment.json`
- `postman/data/finalize_collection.py`
- `state/hw06-state.yaml`
- `todo.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`


## AI-020
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-28 — exact time not retained

### Prompt

```text
implement thật bộ skill
```

### AI Response Summary

Designed and implemented the HW06 Agent Skill architecture for the API testing assignment. The response defined 13 repository-local skills, including orchestration, API specification analysis, multi-pass test generation, human audit support, human test extension, Postman generation, Newman result analysis, bug reporting, CI/CD support, report generation, AI critique generation, submission validation, and AI audit logging.

It also established shared configuration, schemas, workflow state, artifact contracts, human-only review boundaries, and the expected data flow between skills.

### Artifacts

* `.agents/skills/`
* `config/hw06.yaml`
* `schemas/`
* `state/hw06-state.yaml`
* `AGENTS.md`

---

## AI-021
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-28 — exact time not retained

### Prompt

```text
cho tôi content của những file còn thiếu mà bạn chưa tạo đi
```

### AI Response Summary

Identified and prepared the remaining repository-level scaffolding required by the HW06 workflow, including root configuration, state, schemas, documentation placeholders, GitHub Actions configuration, generator pseudocode, README content, and submission-validation requirements.

The response deliberately did not fabricate runtime artifacts such as Newman reports, screenshots, PDFs, or the student-drawn generator diagram.

### Artifacts

* `AGENTS.md`
* `README.md`
* `.gitignore`
* `requirements.txt`
* `config/hw06.yaml`
* `state/hw06-state.yaml`
* `schemas/*.json`
* `.github/workflows/api-tests.yml`
* `generator/pseudocode.md`
* `docs/*.md`
* `git-log.txt`

---

## AI-022
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-28 — exact time not retained

### Prompt

```text
các file SKILL.md cho các skill thì sao
```

### AI Response Summary

Created the missing `SKILL.md` definitions for all 13 HW06 Agent Skills. Each skill was given YAML frontmatter, purpose, inputs, outputs, workflow rules, validation expectations, artifact boundaries, and safeguards preventing AI from fabricating human review decisions or execution evidence.

### Artifacts

* `.agents/skills/hw06-orchestrator/SKILL.md`
* `.agents/skills/api-spec-analyzer/SKILL.md`
* `.agents/skills/api-test-generator/SKILL.md`
* `.agents/skills/test-case-auditor/SKILL.md`
* `.agents/skills/test-case-extender/SKILL.md`
* `.agents/skills/postman-test-builder/SKILL.md`
* `.agents/skills/test-result-analyzer/SKILL.md`
* `.agents/skills/bug-report-writer/SKILL.md`
* `.agents/skills/cicd-helper/SKILL.md`
* `.agents/skills/report-writer/SKILL.md`
* `.agents/skills/ai-critique-writer/SKILL.md`
* `.agents/skills/submission-validator/SKILL.md`
* `.agents/skills/audit-logger/SKILL.md`

---

## AI-023
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-28 — exact time not retained

### Prompt

```text
đây là cấu trúc hiện tại, hãy check xem nó đã setup đủ chưa
```

### AI Response Summary

Reviewed the repository tree and compared it against the planned HW06 Agent Skill architecture. The review confirmed that the 13 skill directories and major root directories existed, but noted that a directory-only tree could not verify individual scripts, schemas, references, assets, or `SKILL.md` files.

The response requested a `tree . /F` output to perform a file-level verification and also identified missing runtime workspace directories and the need to exclude `node_modules` from Git tracking.

### Artifacts

* No repository artifact was modified.
* Repository structure was reviewed.

---

## AI-024
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-28 — exact time not retained

### Prompt

```text
đây chính là file cấu trúc sau khi chạy lệnh
```

### AI Response Summary

Performed a file-level review of the repository structure generated with `tree . /F`. The review confirmed that all 13 `SKILL.md` files, configuration files, schemas, workflow state, documentation scaffolding, and GitHub Actions workflow were present.

It also detected that most skill-specific `scripts/`, `references/`, and `assets/` were still missing, along with runtime directories such as `tests/`, `postman/`, `reports/`, `evidence/`, `bugs/`, and `ai-logs/`.

The response additionally recommended using the existing assignment and SUT files directly instead of duplicating them into another `source/` directory.

### Artifacts

* No repository artifact was modified.
* `structure.txt` was analyzed.

---

## AI-025
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-28 — exact time not retained

### Prompt

```text
ok hãy tạo đi
```

### AI Response Summary

Created the missing support resources for the Agent Skills. These included deterministic Python validation and transformation scripts, reference documents, report and bug templates, audit templates, and CI/CD evidence guidance.

The Python scripts were compile-checked before packaging. The resulting support bundle was designed to be extracted directly into the HW06 repository without replacing existing `SKILL.md` files.

### Artifacts

* `.agents/skills/hw06-orchestrator/scripts/update_state.py`
* `.agents/skills/api-spec-analyzer/references/api-context-format.md`
* `.agents/skills/api-spec-analyzer/scripts/validate_context.py`
* `.agents/skills/api-test-generator/references/test-case-format.md`
* `.agents/skills/api-test-generator/references/coverage-rules.md`
* `.agents/skills/api-test-generator/scripts/validate_test_suite.py`
* `.agents/skills/api-test-generator/scripts/coverage_check.py`
* `.agents/skills/test-case-auditor/references/review-rubric.md`
* `.agents/skills/test-case-auditor/scripts/prepare_audit.py`
* `.agents/skills/test-case-auditor/scripts/validate_human_audit.py`
* `.agents/skills/test-case-extender/scripts/validate_extensions.py`
* `.agents/skills/postman-test-builder/references/postman-conventions.md`
* `.agents/skills/postman-test-builder/scripts/build_collection.py`
* `.agents/skills/postman-test-builder/scripts/validate_collection.py`
* `.agents/skills/test-result-analyzer/scripts/parse_newman.py`
* `.agents/skills/bug-report-writer/assets/github-issue-template.md`
* `.agents/skills/cicd-helper/references/cicd-evidence-requirements.md`
* `.agents/skills/report-writer/assets/report-template.md`
* `.agents/skills/report-writer/scripts/assemble_report.py`
* `.agents/skills/ai-critique-writer/scripts/validate_word_count.py`
* `.agents/skills/submission-validator/scripts/validate_submission.py`
* `.agents/skills/audit-logger/assets/audit-entry-template.md`
* `.agents/skills/audit-logger/scripts/append_audit.py`

---

## AI-026
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-29 — exact time not retained

### Prompt

```text
tôi đang có ý định sử dụng codex để hoàn thành bài tập này, hãy lập file current_context.md để nạp nhanh context vào codex. sau đó lập một file todo.md để có một kế hoạch cụ thể để điều hướng codex thực hiện để hoàn thành được bài tập
```

### AI Response Summary

Created two Codex guidance documents.

`current_context.md` provides a compact project context containing the assignment goal, selected APIs, source-of-truth files, repository structure, Agent Skills, artifact flow, test contracts, human-review boundaries, evidence restrictions, CI/CD requirements, and AI Audit rules.

`todo.md` defines an end-to-end execution roadmap divided into phases from repository verification and SUT inspection through API analysis, multi-pass test generation, human audit, human-added test cases, Postman/Newman execution, bug reporting, CI/CD, generator documentation, report generation, AI critique, artifact export, and final submission validation. Explicit `HUMAN GATE` checkpoints were added where Codex must stop for student decisions or evidence collection.

### Artifacts

* `current_context.md`
* `todo.md`

---

## AI-027
**Tool:** ChatGPT / GPT-5.6 Sol

**Time:** 2026-08-29 — exact time not retained

### Prompt

```text
giờ tôi cần thực hiện thế nào từ lúc bắt đầu cho đến lúc đem bài làm đi nộp
```

### AI Response Summary

Explained the recommended execution workflow from initial Codex startup through final submission.

The response recommended completing one API design pipeline at a time, beginning with Login, then repeating the same process for Apply Coupon and Admin Create Coupon. It described when to run specification analysis, multi-pass AI generation, human audit, human extension, Postman construction, Newman execution, failure classification, real bug confirmation, CI/CD demonstrations, generator documentation, report generation, AI Critique, artifact export, and final submission validation.

It also clarified the division of responsibility: Codex performs analysis, generation, validation, transformation, result processing, and documentation assistance, while the student retains responsibility for human audit verdicts, confirmation of human-added tests, bug confirmation, screenshots, CI evidence, the self-drawn generator diagram, and final submission checks.

### Artifacts

* No new repository artifact was created.
* The execution strategy for following `todo.md` was clarified.

## AI-028

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:52:17 +07

### Prompt

```text
transfer content from tmp_ai_audit.md to the main ai_audit and delete that tmp_ai_audit file
continue
```

### AI Response Summary

Transferred eight reconstructed initial-project interactions from tmp_ai_audit.md into docs/ai-audit.md and renumbered them sequentially as AI-020 through AI-027. A first PowerShell formatting attempt appended malformed blank headings; inspected the result, removed only that failed appended block while preserving all valid AI-001 through AI-019 entries, retried with integer-safe numbering, and verified eight unique reconstructed IDs with no blank audit headings. Deleted tmp_ai_audit.md only after verification succeeded. The Student ID human gate remains pending.

### Artifacts

- `docs/ai-audit.md`
- `tmp_ai_audit.md`
- `ai-logs/.audit-prompt.txt`
- `ai-logs/.audit-summary.txt`

### Full Output Reference

`NOT_RETAINED`

## AI-029

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:54:00 +07

### Prompt

```text
my student ID is 23127006, name Trần Nguyễn Khải Luân
continue
```

### AI Response Summary

Verified the human-supplied Student ID 23127006 was already present and matched in config/hw06.yaml and postman/local.postman_environment.json. Preserved the supplied name Trần Nguyễn Khải Luân in the completed human-gate archive without adding an undocumented configuration field. Archived STUDENT-ID-01 and reset tmp.md. Prepared to continue with real local SUT and Newman execution; no execution evidence or screenshot was fabricated.

### Artifacts

- `config/hw06.yaml`
- `postman/local.postman_environment.json`
- `ai-logs/human-gates/STUDENT-ID-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-030

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 00:57:06 +07

### Prompt

```text
my student ID is 23127006, name Trần Nguyễn Khải Luân
continue
```

### AI Response Summary

Closed the Student ID gate after verifying 23127006 in both configuration and Postman environment, installed Newman and htmlextra, started the real local backend, verified HTTP 200 readiness, and executed the 133-request collection. The first reporter invocation performed no tests due to PowerShell reporter-list parsing and was corrected. The real run generated JSON and HTML reports with 133 requests, 375 assertions, 36 failed assertions, one failed test script, and 37 recorded failures. Kept execution state unfinished because failures require classification and repair; did not declare any failure a SUT bug or fabricate screenshot evidence.

### Artifacts

- `config/hw06.yaml`
- `postman/local.postman_environment.json`
- `reports/newman/report.json`
- `reports/newman/report.html`
- `reports/newman/backend.stdout.log`
- `reports/newman/backend.stderr.log`
- `ai-logs/human-gates/STUDENT-ID-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-031

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 01:11:49 +07

### Prompt

```text
continue
```

### AI Response Summary

Validated the student-supplied X-Student-Id screenshot gate. Visually inspected evidence/x-student-id-23127006.png and confirmed the real Postman Console visibly shows X-Student-Id 23127006 for GET http://localhost:3000/api/products with a 200 OK response. Archived NEWMAN-EVIDENCE-01 and reset tmp.md. No screenshot was generated or altered by AI.

### Artifacts

- `evidence/x-student-id-23127006.png`
- `ai-logs/human-gates/NEWMAN-EVIDENCE-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-032

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 01:14:29 +07

### Prompt

```text
continue
```

### AI Response Summary

Closed and archived the verified X-Student-Id screenshot gate, parsed the real Newman report into 133 executed items with 107 passing and 26 failing items, and replaced the parser's provisional all-bug labels with evidence-based classifications. Classified 18 failures as DATA_SETUP_FAILURE and eight as SUT_BUG_CANDIDATE across four requirement-backed groups: FR-09 percent formula, inclusive minimum threshold, Apply Coupon authentication, and FR-17 required fields. Updated results.json, failure-analysis.md, and test-summary.md. Did not confirm or report any bug on the student's behalf and kept execution state unfinished pending repairs and reruns.

### Artifacts

- `reports/results.json`
- `reports/failure-analysis.md`
- `docs/test-summary.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

## AI-033

**Tool:** Codex / GPT-5.6 Sol  
**Time:** 2026-08-29 08:46:37 +07

### Prompt

```text
I have reviewed and approve all, continue
```

### AI Response Summary

Applied the student's explicit confirmation of all four SUT bug-candidate groups while leaving 18 DATA_SETUP_FAILURE cases unconfirmed as bugs. Created four traceable Markdown bug reports for the incorrect percent formula, rejected inclusive threshold, missing Apply Coupon JWT enforcement, and missing Admin coupon required-field validation, plus a consolidated docs/bugs.md index. Preserved real Newman evidence and left GitHub URLs, issue numbers, commit hashes, and screenshots as PENDING_HUMAN_ACTION. Archived BUG-CANDIDATES-01 and reset tmp.md.

### Artifacts

- `reports/results.json`
- `bugs/BUG-001.md`
- `bugs/BUG-002.md`
- `bugs/BUG-003.md`
- `bugs/BUG-004.md`
- `docs/bugs.md`
- `ai-logs/human-gates/BUG-CANDIDATES-01.md`
- `tmp.md`
- `docs/ai-audit.md`

### Full Output Reference

`NOT_RETAINED`

