# CI/CD Report

## Pipeline Configuration

The GitHub Actions workflow is defined in `.github/workflows/api-tests.yml` and runs on pushes and pull requests using Ubuntu and Node.js 22. It performs the following verified steps:

1. checks out the repository;
2. installs Newman and `newman-reporter-htmlextra`;
3. installs the backend dependencies from `eshop-sut/backend/package-lock.json` with `npm ci`;
4. starts the actual SUT command, `node server.js`, from `eshop-sut/backend`;
5. polls `http://localhost:3000/api/products` until the SUT is ready, or fails after 30 attempts and prints the SUT log;
6. executes `postman/HW06.postman_collection.json` with `postman/local.postman_environment.json`;
7. exports CLI, JSON, and HTML Extra results to `reports/newman/`; and
8. uploads the Newman report directory with `actions/upload-artifact@v4`, including when the Newman step fails.

The workflow configuration is complete. A real CI execution has now verified that the pipeline reaches and executes Newman and uploads its report. Real PASS and intentional single-FAIL demonstrations remain subject to separate human gates.

## Operational Full-Suite Run (Not the Intentional Single-Failure Sample)

- Commit SHA: `34ea594f39061e6eed9c8be9a702141f20109b96`
- GitHub Actions job: https://github.com/Luke23127006/HW6-SoftwareTesting/actions/runs/33228816770/job/99037708089
- Screenshot: `evidence/ci/ci-fail.png`
- Result: **FAIL** — Newman exited with code 1 after executing the real collection.
- Student-reported/display totals: 133 requests, 375 assertions, 37 failed tests, and 0 skipped tests.
- Downloaded JSON totals: 133 requests, 375 assertions, **39 failed assertions**, no failed test scripts, and 31 request items containing failures. The difference from the reported value 37 is retained as an evidence discrepancy rather than silently normalized.
- Interpretation: CI pipeline execution and Newman execution in CI are verified. This run is not PASS evidence and is not the assignment's intentional one-failure demonstration because it contains 37 failures, including valid tests that expose confirmed SUT defects.

The screenshot visibly identifies assertion failures including `ADMIN-COUPON-AI-025`, `ADMIN-COUPON-AI-026`, `ADMIN-COUPON-AI-028`, and `ADMIN-COUPON-AI-032`, and shows that the report-upload step succeeded after Newman exited with code 1.

## Failure Triage Plan

The downloaded CI run classifies its 31 failed request items as follows:

- confirmed genuine SUT defects: 19 items;
- test-data/setup failures: 12 items;
- incorrect test cases: 0 identified.

Only setup/environment failures and genuinely incorrect tests may be corrected as testing-infrastructure work. Confirmed defect-detecting tests and their expected results remain unchanged in the final suite and bug reports. The detailed classification is recorded in `reports/newman-report/failure-analysis.md`.

## PASS Demonstration Planning

GitHub's public Actions history was inspected on 2026-08-29. It contains four `HW06 API Tests` runs, all with conclusion `failure`. Only commits `a674794fee845ee6566c9119cc9b08a4bd55ec66` and `34ea594f39061e6eed9c8be9a702141f20109b96` contained the final Postman collection; neither produced a passing run. Therefore, no existing real PASS sample can currently be reused.

The smallest honest fallback, subject to student approval after CI failure triage, is an explicitly labeled, separate CI demonstration collection containing a stable requirement-valid smoke subset. It would not replace or modify the complete 131-test collection. The complete suite would remain the authoritative defect-detection artifact and continue to report known SUT failures. The demonstration collection would be used only to prove the CI pass/fail mechanism: first unchanged for a genuine PASS, then in a separate temporary commit with exactly one intentionally impossible assertion for the required single-FAIL run, followed by a revert. The report must disclose the subset scope and must not describe it as a full-suite pass.

The student approved this strategy. The manual `workflow_dispatch` input now offers `full` and `demo`. Push and pull-request events still execute the authoritative full collection. The `demo` option explicitly executes `postman/HW06.ci-demonstration.postman_collection.json`, containing authentication setup plus one stable requirement-valid case from Login, Apply Coupon, and Admin Create Coupon. Any green demonstration run will be labeled as a subset PASS, never a full-suite PASS.

## Passing Run

- Commit SHA: `5308109afb952ef31371e7e59fe66af2d15036e1`
- GitHub Actions URL: https://github.com/Luke23127006/HW6-SoftwareTesting/actions/runs/33259457076
- Job URL: https://github.com/Luke23127006/HW6-SoftwareTesting/actions/runs/33259457076/job/99118782545
- Screenshot: `evidence/ci/ci-pass-demo.png`
- Result: **PASS**
- Scope: transparent five-request CI demonstration subset; this is not a full-suite PASS.

The public Actions API and screenshot verify a manual `workflow_dispatch` success at the recorded commit. The authoritative full suite continues to preserve and expose the confirmed SUT defects.

## Intentionally Failing Run

- Commit SHA: `PENDING_HUMAN_ACTION`
- GitHub Actions URL: `PENDING_HUMAN_ACTION`
- Screenshot: `PENDING_HUMAN_ACTION`
- Intentionally changed assertion: `PENDING_HUMAN_ACTION`
- Result: `PENDING_HUMAN_ACTION`

## Revert Confirmation

`PENDING_HUMAN_ACTION`
