---
name: cicd-helper
description: Integrate the reviewed Newman API suite into GitHub Actions and document one real passing run and one intentionally failing run.
---

# CI/CD Helper

## Purpose

Implement the HW06 CI/CD requirement for automatic API-test execution.

## Inputs

- Postman collection
- environment strategy
- SUT repository/startup commands
- Newman command
- repository structure

## Outputs

```text
.github/workflows/api-tests.yml
docs/cicd-report.md
```

## Pipeline

A typical pipeline should:

1. checkout source
2. setup Node
3. install SUT dependencies
4. initialize required data/environment
5. start the SUT
6. wait until the API is available
7. install Newman
8. run the collection
9. save JSON/HTML reports
10. upload reports as artifacts

## Do Not Guess SUT Commands

If the real repository uses a different startup process, inspect the repository before writing CI commands.

Do not assume:

```text
npm start
```

unless source files support it.

## Newman

Prefer:

```bash
newman run postman/HW06.postman_collection.json   -e postman/local.postman_environment.json   -r cli,json,htmlextra   --reporter-json-export reports/newman/report.json   --reporter-htmlextra-export reports/newman/report.html
```

## Required PASS Run

The student must produce a real commit where all intended API tests pass.

Record:

- real commit SHA
- real GitHub Actions URL
- real screenshot
- outcome

## Required FAIL Run

Create one deliberate test failure.

Preferred approach:

Temporarily change one reviewed Postman assertion to an intentionally impossible expected value.

Example concept:

```javascript
pm.expect(pm.response.code).to.eql(999);
```

Do not break SUT production logic solely to create the demonstration.

Commit the deliberate failure, run CI, capture evidence, then revert it.

## Report

`docs/cicd-report.md` should contain:

### Pipeline Configuration

- trigger
- runtime
- SUT startup
- Newman execution
- report upload

### Passing Run

- commit
- URL
- screenshot
- result

### Failing Run

- commit
- URL
- screenshot
- intentionally modified assertion
- confirmation that it was reverted

## Evidence Boundary

Never invent CI evidence.

If not yet available:

```text
PENDING_HUMAN_ACTION
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

