---
name: api-spec-analyzer
description: Convert the supplied API specification and system requirements into a structured, traceable API testing context without inventing undefined behavior.
---

# API Spec Analyzer

## Purpose

Create the structured testing context used by all later skills.

The analyzer converts source documentation into a normalized `api-context.yaml`.

## Supported APIs

- `login`
- `apply_coupon`
- `admin_create_coupon`

## Inputs

- `source/api_specification.md`
- `source/system_requirements.md`
- `config/hw06.yaml`
- one selected API key

## Outputs

For the selected API:

```text
tests/<api>/api-context.yaml
tests/<api>/traceability.md
```

## Required Extraction

Extract all source-supported information for:

### API Contract

- feature ID
- method
- path
- authentication requirement
- authorization requirement
- headers
- path parameters
- query parameters
- request body fields
- response information

### Domain Constraints

Capture:

- required vs optional
- type
- allowed enum values
- numeric bounds
- format rules
- uniqueness rules
- cross-field rules

### Business Rules

Capture relevant FR rules as individually traceable rules.

Example:

```yaml
business_rules:
  - id: FR-02-R1
    description: Failed login increments the failure counter by exactly one.
```

### State Behavior

Capture explicit states and transitions.

### Security

Map relevant:

- SEC-01
- SEC-02
- SEC-03
- SEC-04
- SEC-05
- SEC-06
- SEC-07

Do not force irrelevant SEC requirements onto an API.

### Dependencies

Identify fixtures or setup data required before execution.

### Ambiguities

If the supplied documentation does not define something, record it.

Example:

```yaml
ambiguities:
  - Login failure HTTP status is not explicitly defined.
```

Never silently assume `401`, `400`, or another conventional status.

## API-Specific Focus

### Login

Capture:

- `POST /api/login`
- email/password body
- successful JWT response
- failed-attempt counter
- 3 consecutive failures
- 30-second lock
- appropriate non-disclosing error behavior
- relevant SQL injection/security implications

### Apply Coupon

Capture:

- `POST /api/apply-coupon`
- `code`
- `total_amount`
- `user_id`
- five coupon conditions C1–C5
- percent/fixed formulas
- coupon fixtures such as `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`
- JWT requirement from system requirements
- potential JWT identity vs request `user_id` mismatch risk

### Admin Create Coupon

Capture:

- `POST /api/admin/coupons`
- JWT requirement
- `role = admin`
- unique `code`
- `type ∈ {percent, fixed}`
- `discount_value > 0`
- `min_order_amount >= 0`
- `max_uses_per_user >= 1`
- `expired_at`
- persistence expectations only where source-supported

## Output Contract

Use the schema in:

```text
schemas/api-context.schema.json
```

Recommended top-level fields:

```yaml
api:
request:
responses:
business_rules:
states:
security_requirements:
dependencies:
ambiguities:
security_observations:
```

## Validation

After writing the context:

```bash
python .agents/skills/api-spec-analyzer/scripts/validate_context.py tests/<api>/api-context.yaml
```

Fix validation errors before continuing.


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

