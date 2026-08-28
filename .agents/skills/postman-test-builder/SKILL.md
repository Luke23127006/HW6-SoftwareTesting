---
name: postman-test-builder
description: Convert reviewed final API test cases into a traceable Postman collection and environment with X-Student-Id injection, setup, assertions, and cleanup structure.
---

# Postman Test Builder

## Purpose

Translate reviewed test cases into executable Postman artifacts.

This skill must only use final reviewed tests.

## Inputs

```text
tests/login/final-tests.yaml
tests/apply-coupon/final-tests.yaml
tests/admin-create-coupon/final-tests.yaml
config/hw06.yaml
```

API contexts may also be read for setup/dependency information.

## Outputs

```text
postman/HW06.postman_collection.json
postman/local.postman_environment.json
postman/data/*
```

## Collection Structure

Use:

```text
HW06 API Testing
├── Setup
├── Pool A - Login
├── Pool B - Apply Coupon
├── Pool C - Admin Create Coupon
└── Cleanup
```

Subfolders may be created by:

- Functional
- Domain
- Boundary
- State
- Authentication
- Authorization
- Security
- Schema

when useful.

## Traceability

Every executable Postman item should include the original test ID.

Example:

```text
LOGIN-AI-001 | Login with valid credentials
```

## Environment Variables

At minimum support:

```text
baseUrl
studentId

userEmail
userPassword
userToken

adminEmail
adminPassword
adminToken
```

Add runtime IDs only when tests require them.

## Mandatory X-Student-Id

At collection level use a pre-request script:

```javascript
pm.request.headers.upsert({
  key: "X-Student-Id",
  value: pm.environment.get("studentId")
});
```

Do not hardcode the real student ID inside test definitions if it can be stored in environment configuration.

## Authentication Setup

Use real login requests to capture tokens.

Example:

```javascript
const body = pm.response.json();
pm.environment.set("userToken", body.token);
```

Do the same for `adminToken`.

Do not fabricate tokens.

## Assertions

Translate reviewed expected results into Postman assertions.

Avoid placeholder assertions such as:

```javascript
pm.expect(true).to.eql(true);
```

in the final collection.

Every final test should contain meaningful executable assertions.

## Schema Validation

Where applicable, validate:

- required fields
- field types
- absence of sensitive fields

## Data-Driven Tests

Use Collection Runner/Newman data files when it meaningfully reduces repeated cases.

Do not force data-driven testing where state/setup requirements differ too much.

## Cleanup

For mutation tests:

- remove created coupons where possible;
- restore reusable state;
- isolate generated identifiers.

## Student Evidence Boundary

AI may generate the pre-request script.

The student must personally run the collection and capture real evidence that `X-Student-Id` is present.

## Build

```bash
python .agents/skills/postman-test-builder/scripts/build_collection.py
```

## Validate

```bash
python .agents/skills/postman-test-builder/scripts/validate_collection.py   postman/HW06.postman_collection.json
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

