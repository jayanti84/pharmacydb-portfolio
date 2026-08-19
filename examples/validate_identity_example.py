"""Sanitized portfolio example for deterministic package-identity validation.

This is illustrative portfolio code, not production PharmacyDB code.
It uses no private data, credentials, endpoints, or cloud configuration.
"""

from collections import Counter


def validate_ndc11(values: list[str]) -> list[str]:
    """Return validation errors for a bounded list of NDC11 strings."""
    errors: list[str] = []
    normalized = [value.strip() for value in values]

    for index, value in enumerate(normalized, start=1):
        if len(value) != 11 or not value.isdigit():
            errors.append(f"row {index}: invalid NDC11 format")

    duplicates = [value for value, count in Counter(normalized).items() if count > 1]
    for value in sorted(duplicates):
        errors.append(f"duplicate NDC11: {value}")

    return errors


if __name__ == "__main__":
    # Synthetic test values only; these are not production PharmacyDB records.
    sample_values = [
        "00000000001",
        "00000000002",
        "00000000003",
    ]

    validation_errors = validate_ndc11(sample_values)

    if validation_errors:
        raise SystemExit("VALIDATION_FAILED: " + "; ".join(validation_errors))

    print("VALIDATION_PASS")
