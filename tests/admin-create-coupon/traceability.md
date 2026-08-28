# Admin Create Coupon Traceability

| Rule | Source |
| --- | --- |
| POST path and six body fields | `eshop-sut/api_specification.md`, §6.4 |
| Valid JWT and admin role | `eshop-sut/api_specification.md`, §6; FR-12; SEC-02/SEC-03 |
| Unique code; percent/fixed; positive discount; required expiry; minimum >=0; maximum uses >=1 | `eshop-sut/README.md`, FR-17 |
| Query safety | SEC-05 |

Undefined statuses, response schemas, expiry format/future constraint, numeric integrality, maximum lengths, percent upper bound, normalization, and atomicity remain `SPEC_UNDEFINED`.
