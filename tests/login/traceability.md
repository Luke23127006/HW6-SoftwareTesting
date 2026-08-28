# Login API Traceability

## Contract mapping

| Context item | Source | Traceable requirement |
| --- | --- | --- |
| `POST /api/login` | `eshop-sut/api_specification.md`, §1.2 | Login method and path |
| JSON `email`, `password` | `eshop-sut/api_specification.md`, §1.2; `eshop-sut/README.md`, FR-02 | Request example and user inputs |
| HTTP 200 with JWT `token` and `user` | `eshop-sut/api_specification.md`, §1.2 | Defined success response |
| Counter increases exactly one per failure | `eshop-sut/README.md`, FR-02 | FR-02-R1 |
| Lock at three or more consecutive failures | `eshop-sut/README.md`, FR-02 | FR-02-R2 |
| Lock duration 30 seconds | `eshop-sut/README.md`, FR-02 | FR-02-R3 |
| Appropriate, non-disclosing failure | `eshop-sut/README.md`, FR-02 | FR-02-R4 |
| Successful login returns JWT | `eshop-sut/README.md`, FR-02 | FR-02-R5 |
| Later authenticated calls use Bearer JWT | `eshop-sut/README.md`, FR-02 | FR-02-R6 |
| Password not stored plaintext | `eshop-sut/README.md`, SEC-01 | Security storage check relevant to authentication |
| Parameterized database queries | `eshop-sut/README.md`, SEC-05 | SQL-injection resistance |

## State coverage targets

| Transition | Rule |
| --- | --- |
| Eligible, 0 failures → eligible, 1 failure | FR-02-R1 |
| Eligible, 1 failure → eligible, 2 failures | FR-02-R1 |
| Eligible, 2 failures → locked on third failure | FR-02-R1, FR-02-R2 |
| Locked → eligible after 30 seconds | FR-02-R3 |
| Eligible with prior failures → successful login | Outcome is `SPEC_UNDEFINED`; preserve as an ambiguity test |

## Specification boundaries

The sources define the successful HTTP status but not failure statuses, exact error schemas/messages, `user` schema, JWT claims/lifetime, malformed-input behavior, or precise timer tolerance. Tests for those areas must label their expected values `SPEC_UNDEFINED` unless later human review resolves them from an authoritative source. Implementation observations in `docs/test-environment.md` are for execution setup and defect discovery, not replacements for these expected results.

The paths expected by the analyzer skill and root rules under `source/` are absent. This analysis therefore uses the source files explicitly identified by `current_context.md` and Phase 0 of `todo.md`: `requirements/req_en.md`, `requirements/req_vi.md`, `eshop-sut/api_specification.md`, and `eshop-sut/README.md`.
