# CI/CD Evidence Requirements

Document:

- workflow trigger
- runtime setup
- SUT installation/startup
- readiness check
- Newman installation
- Newman command
- JSON/HTML reports
- artifact upload

## Passing Run

Record real commit SHA, run URL, screenshot, and result.

## Failing Run

Record real commit SHA, run URL, screenshot, intentionally modified assertion,
and confirmation that the deliberate failure was reverted.

Never fabricate CI evidence.
