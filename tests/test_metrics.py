from __future__ import annotations

import copy
import json
import tempfile
import unittest
from collections import defaultdict
from pathlib import Path
from random import Random

from trace_fv.cli import reproduce
from trace_fv.metrics import (
    DEPTHS,
    TraceFVValidationError,
    compute_durability,
    compute_e2e_tva,
    compute_fse_point,
    profile_distance,
    randomization_diagnostic,
    validate_dataset,
)


ROOT = Path(__file__).resolve().parents[1]


def make_fse_rows(profile_for) -> list[dict]:
    rows = []
    for block in range(1, 6):
        for frame in ("affiliative", "reductionist", "neutral_audit"):
            rows.append(
                {
                    "run_id": f"R-{block}-{frame}",
                    "product": "synthetic-product",
                    "block": block,
                    "frame": frame,
                    "ov_profile": profile_for(block, frame),
                }
            )
    return rows


class TestFSE(unittest.TestCase):
    def test_profile_distance_is_categorical(self) -> None:
        self.assertEqual(profile_distance([0, 0, 0, 0, 0], [0, 1, 0, -1, 0]), 0.4)

    def test_all_profiles_equal(self) -> None:
        rows = make_fse_rows(lambda _block, _frame: [0, 0, 0, 0, 0])
        point = compute_fse_point(rows)
        diagnostic = randomization_diagnostic(rows, permutations=59, seed=20260725)
        self.assertEqual(point["fse_ov"], 0.0)
        self.assertEqual(diagnostic["p_rand"], 1.0)

    def test_frame_constant_profiles_are_positive(self) -> None:
        profiles = {
            "affiliative": [2, 2, 2, 2, 2],
            "reductionist": [-2, -2, -2, -2, -2],
            "neutral_audit": [0, 0, 0, 0, 0],
        }
        rows = make_fse_rows(lambda _block, frame: profiles[frame])
        self.assertGreater(compute_fse_point(rows)["fse_ov"], 0.0)

    def test_block_constant_profiles_have_no_frame_excess(self) -> None:
        rows = make_fse_rows(lambda block, _frame: [block - 3] * 5)
        self.assertEqual(compute_fse_point(rows)["fse_ov"], 0.0)

    def test_global_label_swap_is_invariant(self) -> None:
        rows = make_fse_rows(
            lambda block, frame: {
                "affiliative": [2, 2, block % 2, 2, 1],
                "reductionist": [-2, -2, -(block % 2), -2, -1],
                "neutral_audit": [0, 0, 0, 0, 0],
            }[frame]
        )
        swapped = copy.deepcopy(rows)
        mapping = {
            "affiliative": "reductionist",
            "reductionist": "neutral_audit",
            "neutral_audit": "affiliative",
        }
        for row in swapped:
            row["frame"] = mapping[row["frame"]]
        self.assertEqual(compute_fse_point(rows), compute_fse_point(swapped))

    def test_optimized_randomization_matches_slow_reference(self) -> None:
        profiles = {
            "affiliative": [2, 2, 2, 2, 2],
            "reductionist": [-2, -2, -2, -2, -2],
            "neutral_audit": [0, 0, 0, 0, 0],
        }
        rows = make_fse_rows(lambda _block, frame: profiles[frame])
        permutations = 37
        seed = 314159
        observed = compute_fse_point(rows)["fse_ov"]
        grouped = defaultdict(list)
        for row in rows:
            grouped[(row["product"], row["block"])].append(row)
        ordered_groups = [sorted(grouped[key], key=lambda row: row["frame"]) for key in sorted(grouped)]
        rng = Random(seed)
        greater_or_equal = 0
        for _ in range(permutations):
            permuted = []
            for group in ordered_groups:
                shuffled_profiles = [row["ov_profile"] for row in group]
                rng.shuffle(shuffled_profiles)
                for row, profile in zip(group, shuffled_profiles, strict=True):
                    new_row = dict(row)
                    new_row["ov_profile"] = profile
                    permuted.append(new_row)
            if compute_fse_point(permuted)["fse_ov"] >= observed:
                greater_or_equal += 1
        optimized = randomization_diagnostic(rows, permutations=permutations, seed=seed)
        self.assertEqual(optimized["greater_or_equal"], greater_or_equal)
        self.assertEqual(optimized["p_rand"], (1 + greater_or_equal) / (permutations + 1))

    def test_one_missing_session_is_deterministic(self) -> None:
        rows = make_fse_rows(
            lambda _block, frame: {
                "affiliative": [2, 2, 2, 2, 2],
                "reductionist": [-2, -2, -2, -2, -2],
                "neutral_audit": [0, 0, 0, 0, 0],
            }[frame]
        )
        rows = [row for row in rows if row["run_id"] != "R-3-neutral_audit"]
        first = compute_fse_point(rows)
        second = compute_fse_point(list(reversed(rows)))
        self.assertEqual(first, second)
        self.assertGreater(first["within_pair_count"], 0)

    def test_duplicate_run_id_is_hard_failure(self) -> None:
        rows = make_fse_rows(lambda _block, _frame: [0, 0, 0, 0, 0])
        rows[1]["run_id"] = rows[0]["run_id"]
        with self.assertRaisesRegex(TraceFVValidationError, "duplicate run_id"):
            compute_fse_point(rows)

    def test_partial_profile_fails_closed(self) -> None:
        with self.assertRaisesRegex(TraceFVValidationError, "five loci"):
            profile_distance([0, 0, 0, 0], [0, 0, 0, 0, 0])


class TestTriggerMetrics(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dataset = json.loads((ROOT / "synthetic_data/worked_example.json").read_text(encoding="utf-8"))

    def test_worked_e2e_tva(self) -> None:
        result = compute_e2e_tva(self.dataset["trigger_runs"])
        self.assertEqual(result["valid"], {"n": 4, "successes": 2, "rate": 0.5})
        self.assertEqual(result["invalid"], {"n": 4, "successes": 3, "rate": 0.75})
        self.assertEqual(result["e2e_tva"], 0.625)

    def test_worked_durability(self) -> None:
        result = compute_durability(self.dataset["trigger_runs"])
        self.assertEqual(result["scheduled_valid_n"], 4)
        self.assertEqual(result["initial_correction_n"], 2)
        self.assertEqual(result["depths"]["1"]["dcr"], 0.5)
        self.assertEqual(result["depths"]["3"]["cr"], 1.0)
        self.assertEqual(result["depths"]["10"]["dcr"], 0.25)
        self.assertEqual(result["depths"]["rotation"]["cr"], 0.5)

    def test_zero_conditional_denominator_is_not_estimable(self) -> None:
        runs = copy.deepcopy(self.dataset["trigger_runs"])
        for run in runs:
            if run["valid_packet"]:
                run["fo"] = 0
        result = compute_durability(runs)
        for depth in DEPTHS:
            self.assertIsNone(result["depths"][depth]["cr"])
            self.assertEqual(result["depths"][depth]["dcr"], 0.0)

    def test_dataset_ids_are_globally_unique(self) -> None:
        dataset = copy.deepcopy(self.dataset)
        dataset["trigger_runs"][0]["run_id"] = dataset["fse_runs"][0]["run_id"]
        with self.assertRaisesRegex(TraceFVValidationError, "duplicate run_id"):
            validate_dataset(dataset)


class TestCommandLinePath(unittest.TestCase):
    def test_reproduce_writes_valid_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "metrics.json"
            result = reproduce(
                ROOT / "synthetic_data/worked_example.json",
                output_path=output,
                permutations=19,
                seed=20260725,
            )
            parsed = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(parsed, result)
            self.assertFalse(parsed["source"]["official_data"])


if __name__ == "__main__":
    unittest.main()
