# HW06 – API Testing

## Student Information

- Student ID: `CHANGE_ME`
- Assignment: `HW06-AI`
- SUT: EShop
- Base URL: `http://localhost:3000`

## Selected APIs

| Pool | Feature | API |
|---|---|---|
| A | FR-02 Login | `POST /api/login` |
| B | FR-09 Apply Coupon | `POST /api/apply-coupon` |
| C | FR-17 Admin Create Coupon | `POST /api/admin/coupons` |

## Test Summary

| Metric | Pool A | Pool B | Pool C | Total |
|---|---:|---:|---:|---:|
| AI-generated test cases | 0 | 0 | 0 | 0 |
| Human-added test cases | 0 | 0 | 0 | 0 |
| Executed | 0 | 0 | 0 | 0 |
| Passed | 0 | 0 | 0 | 0 |
| Failed | 0 | 0 | 0 | 0 |
| Confirmed bugs | 0 | 0 | 0 | 0 |

## Postman Features Used

- Collection: one collection organized into Setup, Login, Apply Coupon, Admin Create Coupon, and Cleanup folders; 133 executable requests.
- Environment variables: `baseUrl`, `studentId`, user/admin credentials and tokens, and `lastCreatedCouponId` are defined in `postman/local.postman_environment.json`.
- Pre-request scripts: a collection-level script injects `X-Student-Id: {{studentId}}` into every request.
- Test scripts/assertions: all 133 requests have executable Postman test scripts; the 131 reviewed test cases contain concrete status, response, security, and state assertions.
- Runtime variable capture: Setup requests save normal-user and administrator JWTs, and applicable requests save the last created coupon ID.
- Collection Runner/Newman: the collection was executed locally with Newman using CLI, JSON, and HTML Extra reporters.
- Not used: data-driven runner input, mock servers, and monitors.

## CI/CD Evidence

- Passing run: `PENDING_HUMAN_ACTION`
- Intentionally failing run: `PENDING_HUMAN_ACTION`

## AI Test Generator

- Pseudocode: `generator/pseudocode.md`
- Self-drawn diagram: `PENDING_HUMAN_ACTION`

## Public Repository

`PENDING_HUMAN_ACTION`

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---:|---|---:|---:|
| 1 | API 1 — full pipeline | 30 | 0 |
| 2 | API 2 — full pipeline | 30 | 0 |
| 3 | API 3 — full pipeline | 30 | 0 |
| 4 | Agent Skills / AI-driven test generator | 10 | 0 |
|  | **Total** | **100** | **0** |

## Submission Notes

Before submission, run the `submission-validator` skill and replace every `TODO`, `CHANGE_ME`, and `PENDING_HUMAN_ACTION` with real data/evidence where applicable.
