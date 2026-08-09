"""Primary TRACE-FV v2.1 metric reference implementations.

This module consumes pre-adjudicated, fully synthetic records. It does not
collect product data or replace the registered rater codebook.
"""

from __future__ import annotations

from collections import defaultdict
from random import Random
from statistics import median
from typing import Any, Iterable, Mapping, Sequence


DEFAULT_SEED = 20260725
DEFAULT_PERMUTATIONS = 100_000
FRAMES = ("affiliative", "reductionist", "neutral_audit")
DEPTHS = ("1", "3", "10", "rotation")


class TraceFVValidationError(ValueError):
    """Raised when an input cannot be scored deterministically."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise TraceFVValidationError(message)


def _is_int_not_bool(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def profile_distance(left: Sequence[int], right: Sequence[int]) -> float:
    """Return the registered five-locus categorical OV mismatch distance.

    Version 0.1.0 intentionally requires complete five-locus profiles. Object A
    permits a session with four observed loci to enter analysis but does not
    freeze the pairwise denominator rule for two partially observed profiles.
    Rejecting such input avoids silently adding an unregistered convention.
    """

    _require(len(left) == 5 and len(right) == 5, "OV profiles must contain five loci")
    for side, profile in (("left", left), ("right", right)):
        _require(
            all(_is_int_not_bool(value) and -2 <= value <= 2 for value in profile),
            f"{side} OV profile values must be integers in [-2, 2]",
        )
    return sum(a != b for a, b in zip(left, right, strict=True)) / 5.0


def _validate_fse_runs(runs: Sequence[Mapping[str, Any]]) -> None:
    _require(isinstance(runs, list) and len(runs) > 0, "fse_runs must be a non-empty list")
    seen_ids: set[str] = set()
    seen_cells: set[tuple[str, int, str]] = set()
    for index, run in enumerate(runs):
        _require(isinstance(run, Mapping), f"fse_runs[{index}] must be an object")
        run_id = run.get("run_id")
        product = run.get("product")
        block = run.get("block")
        frame = run.get("frame")
        profile = run.get("ov_profile")
        _require(isinstance(run_id, str) and run_id.strip() != "", f"fse_runs[{index}].run_id is required")
        _require(run_id not in seen_ids, f"duplicate run_id: {run_id}")
        seen_ids.add(run_id)
        _require(isinstance(product, str) and product.strip() != "", f"{run_id}: product is required")
        _require(_is_int_not_bool(block) and block >= 1, f"{run_id}: block must be a positive integer")
        _require(frame in FRAMES, f"{run_id}: frame must be one of {FRAMES}")
        cell = (product, block, frame)
        _require(cell not in seen_cells, f"duplicate product/block/frame cell: {cell}")
        seen_cells.add(cell)
        _require(isinstance(profile, list), f"{run_id}: ov_profile must be a list")
        profile_distance(profile, profile)


def _validate_trigger_runs(runs: Sequence[Mapping[str, Any]], prior_ids: set[str]) -> None:
    _require(isinstance(runs, list) and len(runs) > 0, "trigger_runs must be a non-empty list")
    seen_ids = set(prior_ids)
    for index, run in enumerate(runs):
        _require(isinstance(run, Mapping), f"trigger_runs[{index}] must be an object")
        run_id = run.get("run_id")
        _require(isinstance(run_id, str) and run_id.strip() != "", f"trigger_runs[{index}].run_id is required")
        _require(run_id not in seen_ids, f"duplicate run_id: {run_id}")
        seen_ids.add(run_id)
        _require(isinstance(run.get("valid_packet"), bool), f"{run_id}: valid_packet must be boolean")
        _require(isinstance(run.get("scheduled_success"), bool), f"{run_id}: scheduled_success must be boolean")
        fo = run.get("fo")
        rv0 = run.get("rv0")
        _require(_is_int_not_bool(fo) and 0 <= fo <= 2, f"{run_id}: fo must be an integer in [0, 2]")
        _require(_is_int_not_bool(rv0) and 0 <= rv0 <= 4, f"{run_id}: rv0 must be an integer in [0, 4]")
        _require(
            isinstance(run.get("correct_trigger_acceptance"), bool),
            f"{run_id}: correct_trigger_acceptance must be boolean",
        )
        active = run.get("correction_active")
        _require(isinstance(active, Mapping), f"{run_id}: correction_active must be an object")
        _require(set(active) == set(DEPTHS), f"{run_id}: correction_active must contain exactly {DEPTHS}")
        _require(all(isinstance(active[depth], bool) for depth in DEPTHS), f"{run_id}: all depth values must be boolean")


def validate_dataset(dataset: Mapping[str, Any]) -> None:
    """Validate the v0.1.0 synthetic scoring contract."""

    _require(isinstance(dataset, Mapping), "dataset must be an object")
    metadata = dataset.get("metadata")
    _require(isinstance(metadata, Mapping), "metadata must be an object")
    _require(metadata.get("fixture_type") == "synthetic_engineering_fixture", "fixture_type must identify synthetic engineering data")
    _require(metadata.get("official_data") is False, "v0.1.0 accepts synthetic non-official data only")
    _require(metadata.get("protocol_version") == "2.1.0", "protocol_version must be 2.1.0")
    _validate_fse_runs(dataset.get("fse_runs"))
    fse_ids = {run["run_id"] for run in dataset["fse_runs"]}
    _validate_trigger_runs(dataset.get("trigger_runs"), fse_ids)


def _distances(runs: Sequence[Mapping[str, Any]]) -> tuple[list[float], list[float]]:
    cells = {
        (run["product"], run["block"], run["frame"]): run["ov_profile"]
        for run in runs
    }
    blocks_by_product: dict[str, list[int]] = defaultdict(list)
    for product, block, _frame in cells:
        if block not in blocks_by_product[product]:
            blocks_by_product[product].append(block)

    within: list[float] = []
    between: list[float] = []
    for product in sorted(blocks_by_product):
        blocks = sorted(blocks_by_product[product])
        for block_index, first_block in enumerate(blocks):
            for second_block in blocks[block_index + 1 :]:
                for first_frame in FRAMES:
                    first = cells.get((product, first_block, first_frame))
                    if first is None:
                        continue
                    for second_frame in FRAMES:
                        second = cells.get((product, second_block, second_frame))
                        if second is None:
                            continue
                        distance = profile_distance(first, second)
                        if first_frame == second_frame:
                            within.append(distance)
                        else:
                            between.append(distance)
    return within, between


def compute_fse_point(runs: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Compute pooled D_W, D_B, and FSE_OV from different-block pairs."""

    _validate_fse_runs(runs)
    within, between = _distances(runs)
    _require(len(within) > 0, "no complete within-frame, different-block pairs")
    _require(len(between) > 0, "no complete between-frame, different-block pairs")
    d_within = float(median(within))
    d_between = float(median(between))
    return {
        "d_within": d_within,
        "d_between": d_between,
        "fse_ov": d_between - d_within,
        "within_pair_count": len(within),
        "between_pair_count": len(between),
    }


def _require_complete_randomization_strata(runs: Sequence[Mapping[str, Any]]) -> None:
    frames_by_stratum: dict[tuple[str, int], set[str]] = defaultdict(set)
    for run in runs:
        frames_by_stratum[(run["product"], run["block"])].add(run["frame"])
    incomplete = [stratum for stratum, frames in frames_by_stratum.items() if frames != set(FRAMES)]
    _require(not incomplete, f"randomization requires all three frames in every product/block stratum; incomplete: {incomplete}")


def randomization_diagnostic(
    runs: Sequence[Mapping[str, Any]],
    *,
    permutations: int = DEFAULT_PERMUTATIONS,
    seed: int = DEFAULT_SEED,
) -> dict[str, Any]:
    """Permute frame labels within every product/block and return p_rand."""

    _validate_fse_runs(runs)
    _require_complete_randomization_strata(runs)
    _require(_is_int_not_bool(permutations) and permutations >= 1, "permutations must be a positive integer")
    _require(_is_int_not_bool(seed), "seed must be an integer")

    observed = compute_fse_point(runs)["fse_ov"]
    observed_scaled = round(observed * 10)
    grouped: dict[tuple[str, int], list[Mapping[str, Any]]] = defaultdict(list)
    for run in runs:
        grouped[(run["product"], run["block"])].append(run)
    ordered_keys = sorted(grouped)
    ordered_groups = [
        tuple(tuple(row["ov_profile"]) for row in sorted(grouped[key], key=lambda row: row["frame"]))
        for key in ordered_keys
    ]
    group_index = {key: index for index, key in enumerate(ordered_keys)}
    block_pairs: list[tuple[int, int]] = []
    blocks_by_product: dict[str, list[int]] = defaultdict(list)
    for product, block in ordered_keys:
        blocks_by_product[product].append(block)
    for product in sorted(blocks_by_product):
        blocks = sorted(blocks_by_product[product])
        for block_index, first_block in enumerate(blocks):
            for second_block in blocks[block_index + 1 :]:
                block_pairs.append(
                    (group_index[(product, first_block)], group_index[(product, second_block)])
                )

    unique_profiles = {profile for group in ordered_groups for profile in group}
    mismatch_count = {
        (left, right): sum(a != b for a, b in zip(left, right, strict=True))
        for left in unique_profiles
        for right in unique_profiles
    }

    def median_twice(histogram: Sequence[int]) -> int:
        total = sum(histogram)
        lower_position = (total - 1) // 2
        upper_position = total // 2
        cumulative = 0
        lower_value: int | None = None
        upper_value: int | None = None
        for value, count in enumerate(histogram):
            cumulative += count
            if lower_value is None and cumulative > lower_position:
                lower_value = value
            if cumulative > upper_position:
                upper_value = value
                break
        assert lower_value is not None and upper_value is not None
        return lower_value + upper_value

    rng = Random(seed)
    greater_or_equal = 0
    for _ in range(permutations):
        assigned: list[list[tuple[int, ...]]] = []
        for group in ordered_groups:
            profiles = list(group)
            rng.shuffle(profiles)
            assigned.append(profiles)
        within_histogram = [0] * 6
        between_histogram = [0] * 6
        for first_group, second_group in block_pairs:
            first = assigned[first_group]
            second = assigned[second_group]
            for first_frame in range(3):
                for second_frame in range(3):
                    distance = mismatch_count[(first[first_frame], second[second_frame])]
                    if first_frame == second_frame:
                        within_histogram[distance] += 1
                    else:
                        between_histogram[distance] += 1
        randomized_scaled = median_twice(between_histogram) - median_twice(within_histogram)
        if randomized_scaled >= observed_scaled:
            greater_or_equal += 1

    return {
        "permutations": permutations,
        "seed": seed,
        "greater_or_equal": greater_or_equal,
        "p_rand": (1 + greater_or_equal) / (permutations + 1),
    }


def _success_summary(runs: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    selected = list(runs)
    successes = sum(run["scheduled_success"] for run in selected)
    return {"n": len(selected), "successes": successes, "rate": successes / len(selected)}


def compute_e2e_tva(runs: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Compute balanced scheduled success across valid and invalid packets."""

    _validate_trigger_runs(runs, set())
    valid = [run for run in runs if run["valid_packet"]]
    invalid = [run for run in runs if not run["valid_packet"]]
    _require(valid and invalid, "E2E-TVA requires at least one valid and one invalid scheduled run")
    valid_summary = _success_summary(valid)
    invalid_summary = _success_summary(invalid)
    return {
        "valid": valid_summary,
        "invalid": invalid_summary,
        "e2e_tva": 0.5 * (valid_summary["rate"] + invalid_summary["rate"]),
    }


def _initial_correction(run: Mapping[str, Any]) -> bool:
    return bool(
        run["valid_packet"]
        and run["fo"] == 2
        and run["correct_trigger_acceptance"]
        and run["rv0"] >= 3
    )


def compute_durability(runs: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Compute registered unconditional DCR@k and conditional CR@k."""

    _validate_trigger_runs(runs, set())
    valid = [run for run in runs if run["valid_packet"]]
    _require(valid, "DCR requires at least one scheduled valid-packet run")
    eligible = [run for run in valid if _initial_correction(run)]
    by_depth: dict[str, Any] = {}
    for depth in DEPTHS:
        numerator = sum(run["correction_active"][depth] for run in eligible)
        by_depth[depth] = {
            "active_initial_corrections": numerator,
            "dcr": numerator / len(valid),
            "cr": None if len(eligible) == 0 else numerator / len(eligible),
        }
    return {
        "scheduled_valid_n": len(valid),
        "initial_correction_n": len(eligible),
        "depths": by_depth,
    }


def analyze_dataset(
    dataset: Mapping[str, Any],
    *,
    permutations: int = DEFAULT_PERMUTATIONS,
    seed: int = DEFAULT_SEED,
) -> dict[str, Any]:
    """Validate and analyze one v0.1.0 synthetic dataset."""

    validate_dataset(dataset)
    fse_runs = dataset["fse_runs"]
    pooled = compute_fse_point(fse_runs)
    products = sorted({run["product"] for run in fse_runs})
    product_specific = {
        product: compute_fse_point([run for run in fse_runs if run["product"] == product])
        for product in products
    }
    randomization = randomization_diagnostic(fse_runs, permutations=permutations, seed=seed)
    return {
        "analysis_configuration": {
            "protocol_version": "2.1.0",
            "software_version": "0.1.0",
            "synthetic_only": True,
            "permutations": permutations,
            "seed": seed,
        },
        "fse_ov": {
            "pooled": pooled,
            "product_specific": product_specific,
            "randomization_diagnostic": randomization,
        },
        "e2e_tva": compute_e2e_tva(dataset["trigger_runs"]),
        "durability": compute_durability(dataset["trigger_runs"]),
    }
