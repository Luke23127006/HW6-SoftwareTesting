# Confirmed SUT Bugs

The student confirmed seven real defect groups across the local and CI Newman runs:

1. [BUG-001](../bugs/BUG-001.md) — incorrect percent coupon calculation.
2. [BUG-002](../bugs/BUG-002.md) — inclusive minimum threshold rejected.
3. [BUG-003](../bugs/BUG-003.md) — Apply Coupon ignores valid-JWT requirement.
4. [BUG-004](../bugs/BUG-004.md) — Admin coupon creation accepts missing required fields.
5. [BUG-005](../bugs/BUG-005.md) — Admin coupon creation accepts an expired administrator JWT.
6. [BUG-006](../bugs/BUG-006.md) — Admin coupon creation accepts null and invalid coupon types.
7. [BUG-007](../bugs/BUG-007.md) — Admin coupon creation accepts numeric values outside FR-17 constraints.

BUG-001 through BUG-007 have real GitHub Issues and screenshots. Issue #4 was updated with the additional missing-field test references from the CI run.
