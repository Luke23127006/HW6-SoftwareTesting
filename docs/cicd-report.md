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

The workflow configuration is complete. Real PASS and intentional-FAIL run evidence remains subject to the human gates below. The existing local Newman result is not presented as a passing CI baseline because it contains confirmed SUT defects and data-setup failures.

## Passing Run

- Commit SHA: `PENDING_HUMAN_ACTION`
- GitHub Actions URL: `PENDING_HUMAN_ACTION`
- Screenshot: `PENDING_HUMAN_ACTION`
- Result: `PENDING_HUMAN_ACTION`

## Intentionally Failing Run

- Commit SHA: `PENDING_HUMAN_ACTION`
- GitHub Actions URL: `PENDING_HUMAN_ACTION`
- Screenshot: `PENDING_HUMAN_ACTION`
- Intentionally changed assertion: `PENDING_HUMAN_ACTION`
- Result: `PENDING_HUMAN_ACTION`

## Revert Confirmation

`PENDING_HUMAN_ACTION`
