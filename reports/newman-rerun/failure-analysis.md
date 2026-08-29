# Clean Fixture Rerun — Failure Analysis

- Requests: 133
- Assertions: 375
- Failed assertions: 22
- Failed request items: 19
- Failed test scripts: 0
- Setup/data failures: 0
- Incorrect tests identified: 0

All 12 setup/data failures passed after a fresh SUT restart and `postman/data/prepare_fixtures.js`. The remaining 19 failed items map only to student-confirmed BUG-001 through BUG-007. No valid assertion was weakened, skipped, removed, or changed to match buggy behavior.
