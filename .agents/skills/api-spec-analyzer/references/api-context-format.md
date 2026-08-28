# API Context Format

`api-context.yaml` is the normalized source of truth passed from `api-spec-analyzer`
to later HW06 skills.

## Required top-level fields

```yaml
api:
request:
responses:
business_rules:
states:
security_requirements:
dependencies:
ambiguities:
```

Optional:

```yaml
security_observations:
```

## Rules

- Record only information supported by:
  - `requirements/req_en.md`
  - `requirements/req_vi.md`
  - `eshop-sut/api_specification.md`
  - `eshop-sut/README.md`
- Use `SPEC_UNDEFINED` when an exact value is not defined.
- Do not infer conventional HTTP status codes.
- Keep requirement references traceable.
