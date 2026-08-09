"""Command-line entry point for the TRACE-FV synthetic reference pipeline."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Sequence

from .metrics import DEFAULT_PERMUTATIONS, DEFAULT_SEED, TraceFVValidationError, analyze_dataset


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="trace-fv", description="TRACE-FV v2.1 synthetic scoring reference")
    subparsers = parser.add_subparsers(dest="command", required=True)
    reproduce = subparsers.add_parser("reproduce", help="score a synthetic v0.1.0 input file")
    reproduce.add_argument("input", type=Path, help="path to a JSON input fixture")
    reproduce.add_argument("--output", type=Path, help="write JSON output to this path; stdout if omitted")
    reproduce.add_argument("--permutations", type=int, default=DEFAULT_PERMUTATIONS)
    reproduce.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser


def reproduce(input_path: Path, *, output_path: Path | None, permutations: int, seed: int) -> dict:
    raw = input_path.read_bytes()
    dataset = json.loads(raw.decode("utf-8"))
    result = analyze_dataset(dataset, permutations=permutations, seed=seed)
    result["source"] = {
        "fixture_name": dataset["metadata"]["fixture_name"],
        "sha256": hashlib.sha256(raw).hexdigest(),
        "official_data": False,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if output_path is None:
        print(rendered, end="")
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    return result


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "reproduce":
            reproduce(
                args.input,
                output_path=args.output,
                permutations=args.permutations,
                seed=args.seed,
            )
            return 0
    except (OSError, json.JSONDecodeError, TraceFVValidationError) as exc:
        raise SystemExit(f"trace-fv: {exc}") from exc
    raise AssertionError("unreachable")

