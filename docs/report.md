# HW06 – API Testing Report

## Postman Features Used

The implementation uses one Postman collection organized into Setup, Login, Apply Coupon, Admin Create Coupon, and Cleanup folders. It contains 133 executable requests: 131 reviewed test cases plus two authentication setup requests. All requests have executable test scripts, and the reviewed cases use concrete status, response-body, security, and state assertions.

The local environment defines `baseUrl`, `studentId`, normal-user and administrator credentials and tokens, and `lastCreatedCouponId`. A collection-level pre-request script injects `X-Student-Id: {{studentId}}` into every request. Setup requests capture the normal-user and administrator JWTs for later authenticated requests, while applicable requests capture the most recently created coupon ID.

The collection was executed locally through Newman with CLI, JSON, and HTML Extra reporters. The implementation does not use data-driven runner input, a Postman mock server, or a monitor. A Postman workspace is therefore not claimed as an implemented testing feature based solely on its appearance in execution evidence.

> This report is assembled incrementally. Missing real evidence must remain marked as TODO rather than being invented.
