---
name: api-test-generator
description: Generate at least 35 traceable AI API test cases per selected API using disciplined multi-pass test design and explicit coverage validation.
---

# API Test Generator

## Purpose

Generate the AI-created test suite required by HW06.

The generator must not use one generic prompt to create all tests at once. It must design tests in multiple passes and evaluate coverage before stopping.

## Inputs

- `tests/<api>/api-context.yaml`
- `config/hw06.yaml`

## Outputs

```text
tests/<api>/generated-tests.yaml
tests/<api>/coverage.json
tests/<api>/coverage.md
```

## Minimum Requirement

Generate:

```text
>= 35 AI-generated tests per API
```

The count alone is not sufficient. Cases must be meaningful and cover the documented techniques.

## Mandatory Generation Passes

Run the following passes in order.

### Pass 1 — Happy Path

Generate valid normal scenarios.

### Pass 2 — Equivalence Partitioning

Partition every documented parameter into meaningful valid/invalid classes.

### Pass 3 — Boundary Value Analysis

Cover boundaries for:

- numeric constraints
- string length constraints
- counters
- dates
- thresholds
- usage limits

### Pass 4 — Authentication / Authorization

Cover where applicable:

- valid token
- missing token
- malformed token
- wrong role
- identity mismatch

### Pass 5 — Security

Generate tests for relevant SEC rules and realistic API attack vectors.

Examples:

- SQL injection probes
- IDOR
- privilege escalation
- sensitive data leakage
- role manipulation

Do not claim a black-box API test proves an implementation property such as "uses parameterized queries". Mark such coverage as indirect where appropriate.

### Pass 6 — State Transition

Generate tests for documented state transitions.

### Pass 7 — Schema Validation

Check response:

- shape
- required fields
- field types
- absence of sensitive fields

### Pass 8 — Cross-Field / Business Interactions

Test combinations of fields or rules that are valid independently but dangerous together.

### Pass 9 — Deduplication

Remove duplicate or semantically equivalent tests unless the distinction is meaningful.

### Pass 10 — Coverage Analysis

Produce `coverage.json` and `coverage.md`.

### Pass 11 — Gap Filling

Only add more tests for real uncovered areas.

Do not add low-value cases simply to increase count.

## Test Case Contract

Every generated test must satisfy `schemas/test-case.schema.json`.

Required structure:

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
    - response contains user
    - response does not expose password

cleanup: []

rationale: Valid partition for both credential fields.
```

## Allowed Categories

- `functional`
- `domain`
- `boundary`
- `state`
- `authentication`
- `authorization`
- `security`
- `schema`
- `error-handling`

## Undefined Expectations

If the source does not define an exact status code:

```yaml
status: SPEC_UNDEFINED
```

Do not invent one.

## API-Specific Coverage

### Login

Include coverage for:

- valid credentials
- invalid email partitions
- missing/null/empty email
- incorrect password
- malformed request body
- failed attempt #1
- failed attempt #2
- failed attempt #3
- account locked
- behavior after lock timeout
- JWT presence
- information disclosure
- SQL injection probes
- response schema

### Apply Coupon

Cover all:

- C1 coupon exists/active
- C2 expiration
- C3 minimum amount
- C4 authentication
- C5 usage limit
- threshold `min - 1`
- threshold `min`
- threshold `min + 1`
- fixed calculation
- percent calculation
- malformed `total_amount`
- JWT/body `user_id` mismatch
- response schema

### Admin Create Coupon

Cover:

- valid admin request
- no token
- invalid token
- normal user token
- duplicate code
- invalid type
- missing fields
- `discount_value` boundary
- `min_order_amount` boundary
- `max_uses_per_user` boundary
- invalid date values
- wrong data types
- schema
- persistence behavior where testable

## Validation

Run:

```bash
python .agents/skills/api-test-generator/scripts/validate_test_suite.py tests/<api>/generated-tests.yaml
python .agents/skills/api-test-generator/scripts/coverage_check.py tests/<api>/generated-tests.yaml tests/<api>/api-context.yaml
```

Do not proceed to human audit until validation succeeds.


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

