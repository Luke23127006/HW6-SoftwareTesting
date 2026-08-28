# Test Case Format

Every test case uses the shared schema in `schemas/test-case.schema.json`.

Example:

```yaml
- id: LOGIN-AI-001
  source: AI
  title: Login with valid credentials
  requirements: [FR-02]
  techniques: [equivalence_partitioning]
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
      - response contains user
      - response does not expose password
  cleanup: []
  rationale: Valid equivalence partition for both login parameters.
```

If the source does not define an exact expected value, use `SPEC_UNDEFINED`.
