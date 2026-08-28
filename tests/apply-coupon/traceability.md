# Apply Coupon Traceability

| Context item | Source |
| --- | --- |
| `POST /api/apply-coupon`, JSON fields `code`, `total_amount`, `user_id`, response fields | `eshop-sut/api_specification.md`, §5.1 |
| C1 existing and active | `eshop-sut/README.md`, FR-09 C1 |
| C2 current date before expiration | `eshop-sut/README.md`, FR-09 C2 |
| C3 total at least minimum | `eshop-sut/README.md`, FR-09 C3 |
| C4 valid JWT | `eshop-sut/README.md`, FR-09 C4; SEC-02 |
| C5 usage below per-user maximum | `eshop-sut/README.md`, FR-09 C5 |
| Percent/fixed/final formulas | `eshop-sut/README.md`, FR-09 formulas |
| SQL query safety | `eshop-sut/README.md`, SEC-05 |

The source defines all five eligibility conditions and formulas but not HTTP statuses, failure schemas, rounding, identity mismatch handling, malformed-value behavior, or expiration equality/timezone semantics. Those expectations remain `SPEC_UNDEFINED`.
