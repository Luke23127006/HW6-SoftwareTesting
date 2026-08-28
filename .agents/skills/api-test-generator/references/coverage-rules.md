# Coverage Rules

A suite is not complete merely because it contains 35 cases.

Check meaningful coverage across:

- every documented parameter
- equivalence partitions
- boundary values
- authentication
- authorization
- relevant SEC requirements
- state transitions where applicable
- response schema
- cross-field interactions
- negative/error behavior

Use:

- `PASS`
- `PARTIAL`
- `MISSING`
- `INDIRECT`

Use `INDIRECT` when black-box API testing cannot prove an implementation property directly.
