# Postman Conventions

## Environment variables

- `baseUrl`
- `studentId`
- `userEmail`
- `userPassword`
- `userToken`
- `adminEmail`
- `adminPassword`
- `adminToken`

## Required header

Every request must receive:

```text
X-Student-Id: {{studentId}}
```

Preferred collection-level pre-request script:

```javascript
pm.request.headers.upsert({
  key: "X-Student-Id",
  value: pm.environment.get("studentId")
});
```

## Traceability

Postman item names should begin with the test ID.

## Execution reporters

Prefer JSON + HTML Newman reports.
