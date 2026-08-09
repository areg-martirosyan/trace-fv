# Reproducibility note

The v0.1.0 reference path has no runtime dependencies beyond Python 3.11+.

## Deterministic controls

- input is UTF-8 JSON with a published JSON Schema;
- run identifiers and `(product, block, frame)` cells must be unique;
- profiles must contain exactly five integer OV scores in `[-2,2]`;
- medians use the Python standard-library definition;
- Monte Carlo permutations use `random.Random` with an explicit integer seed;
- output JSON has stable key ordering and no generated timestamp;
- the input SHA-256 is embedded in the output;
- the archived OSF package is checked against its frozen checksum manifest.

## Reproduce the committed example

```bash
python -m pip install -e .
python scripts/verify_release.py
```

The committed example uses 999 permutations for rapid engineering verification.
Official analysis under Object A requires 100,000 permutations with seed
20260725 and a separately frozen study-specific implementation.

## Platform note

The fixed-seed permutation sequence is defined by Python's `random.Random` in
this software version. Exact output reproduction therefore includes the
software release and supported Python environment, not only the numeric seed.

