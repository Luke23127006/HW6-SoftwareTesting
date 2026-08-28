# AI-Driven API Test Generator — Pseudocode

> The architecture diagram must be designed and drawn by the student. This file only defines the generator algorithm.

```text
INPUT:
    api_specification
    system_requirements
    selected_api

context = analyze_spec(
    api_specification,
    system_requirements,
    selected_api
)

validate_context(context)

tests = []

tests += generate_happy_path_tests(context)
tests += generate_equivalence_partition_tests(context)
tests += generate_boundary_value_tests(context)
tests += generate_authentication_authorization_tests(context)
tests += generate_security_tests(context)
tests += generate_state_transition_tests(context)
tests += generate_schema_validation_tests(context)
tests += generate_cross_field_interaction_tests(context)

tests = remove_exact_duplicates(tests)
tests = remove_semantic_duplicates(tests)

coverage = analyze_coverage(tests, context)

WHILE meaningful_gap_exists(coverage):
    gap = select_highest_priority_gap(coverage)
    additional_tests = generate_tests_for_gap(gap, context)
    tests += additional_tests
    tests = remove_exact_duplicates(tests)
    tests = remove_semantic_duplicates(tests)
    coverage = analyze_coverage(tests, context)
END WHILE

IF count(tests) < minimum_required_test_count:
    identify_uncovered_meaningful_partitions(context, tests)
    generate_additional_non_duplicate_tests()
END IF

validate_each_test_against_test_case_schema(tests)
validate_traceability(tests, context)

OUTPUT:
    generated_tests
    coverage_report
```
