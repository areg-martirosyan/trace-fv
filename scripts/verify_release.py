#!/usr/bin/env python3
"""Verify the frozen archive and deterministic synthetic release output."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from trace_fv.cli import reproduce  # noqa: E402


def verify_object_a() -> int:
    archive = ROOT / "archive/object-a-v2.1.0"
    manifest = archive / "SHA256SUMS.txt"
    checked = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split(maxsplit=1)
        target = archive / relative.strip()
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(f"checksum mismatch: {target.relative_to(ROOT)}")
        checked += 1
    return checked


def verify_metadata() -> None:
    zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schemas/scored_dataset.schema.json").read_text(encoding="utf-8"))
    with (ROOT / "pyproject.toml").open("rb") as stream:
        project = tomllib.load(stream)
    if zenodo["version"] != "0.1.0" or project["project"]["version"] != "0.1.0":
        raise SystemExit("software version mismatch")
    if zenodo["related_identifiers"][0]["identifier"] != "https://doi.org/10.17605/OSF.IO/6U3QX":
        raise SystemExit("OSF related identifier mismatch")
    if schema["properties"]["metadata"]["properties"]["official_data"]["const"] is not False:
        raise SystemExit("synthetic-only schema guard is missing")


def verify_expected_output() -> None:
    with tempfile.TemporaryDirectory() as directory:
        generated = Path(directory) / "worked_example_metrics.json"
        reproduce(
            ROOT / "synthetic_data/worked_example.json",
            output_path=generated,
            permutations=999,
            seed=20260725,
        )
        expected = json.loads((ROOT / "expected_outputs/worked_example_metrics.json").read_text(encoding="utf-8"))
        actual = json.loads(generated.read_text(encoding="utf-8"))
        if actual != expected:
            raise SystemExit("synthetic output differs from expected_outputs/worked_example_metrics.json")


def main() -> int:
    checked = verify_object_a()
    verify_metadata()
    verify_expected_output()
    print(f"release verification passed: {checked} frozen files, metadata, and synthetic output")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
