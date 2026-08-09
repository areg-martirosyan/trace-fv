"""TRACE-FV v2.1 synthetic reference implementation."""

from .metrics import (
    DEFAULT_PERMUTATIONS,
    DEFAULT_SEED,
    DEPTHS,
    TraceFVValidationError,
    analyze_dataset,
    compute_durability,
    compute_e2e_tva,
    compute_fse_point,
    profile_distance,
    randomization_diagnostic,
    validate_dataset,
)

__all__ = [
    "DEFAULT_PERMUTATIONS",
    "DEFAULT_SEED",
    "DEPTHS",
    "TraceFVValidationError",
    "analyze_dataset",
    "compute_durability",
    "compute_e2e_tva",
    "compute_fse_point",
    "profile_distance",
    "randomization_diagnostic",
    "validate_dataset",
]

__version__ = "0.1.0"

