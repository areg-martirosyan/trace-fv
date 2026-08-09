# TRACE-FV

[![CI](https://github.com/areg-martirosyan/trace-fv/actions/workflows/ci.yml/badge.svg)](https://github.com/areg-martirosyan/trace-fv/actions/workflows/ci.yml)

**Reference implementation and reproducibility assets for TRACE-FV v2.1**

TRACE-FV is a black-box evaluation protocol for observable conversational-AI
product behavior under frame variance, verified correction triggers, and
correction endurance. This repository implements a small, fully synthetic
vertical slice of the registered measurement pipeline.

- **Registered protocol (Object A):** [10.17605/OSF.IO/6U3QX](https://doi.org/10.17605/OSF.IO/6U3QX)
- **Protocol version:** 2.1.0
- **Reference software version:** 0.1.0
- **Principal investigator and maintainer:** Areg Martirosyan, Independent Researcher
- **ORCID:** [0009-0008-4208-750X](https://orcid.org/0009-0008-4208-750X)
- **Status:** preregistered protocol plus post-registration synthetic reference implementation; no official pilot results

## What this release demonstrates

The repository provides executable reference implementations of:

1. categorical OV profile distance and Frame Sensitivity Excess (`FSE_OV`);
2. the registered within-`(product, block)` frame-label randomization diagnostic;
3. End-to-End Trigger Verification Accuracy (`E2E-TVA`);
4. unconditional Durable Correction Rate (`DCR@k`) and conditional retention (`CR@k`);
5. deterministic input validation, including duplicate-run hard failure;
6. a synthetic input fixture, expected output, unit tests, and continuous integration.

The synthetic fixture contains no product output, no participant data, no
held-out material, and no official pilot datum. It is an engineering test of
the scoring path, not evidence about any AI system.

## Quick start

Python 3.11 or later is required.

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python -m trace_fv reproduce \
  synthetic_data/worked_example.json \
  --permutations 999 \
  --seed 20260725 \
  --output build/worked_example_metrics.json
python scripts/verify_release.py
```

The final command verifies the byte-identical Object A archive, reruns the
synthetic analysis, and compares it with the committed expected output.

For a protocol-conforming official randomization diagnostic, use exactly
`100000` Monte Carlo permutations and seed `20260725`. The smaller value in the
worked example keeps continuous integration fast and is explicitly an
engineering test configuration.

## Repository map

| Path | Purpose |
|---|---|
| `src/trace_fv/` | Dependency-free Python reference implementation and CLI |
| `tests/` | Registered synthetic checks and trigger-metric tests |
| `synthetic_data/` | Fully synthetic, pre-adjudicated worked input |
| `expected_outputs/` | Deterministic output for the worked input |
| `schemas/` | Machine-readable v0.1.0 input contract |
| `docs/PROTOCOL_TO_CODE.md` | Formula-to-function traceability |
| `docs/IMPLEMENTATION_STATUS.md` | Implemented scope, limitations, and non-claims |
| `docs/STUDY_SPECIFIC_GATE.md` | Materials that must be frozen before official data acquisition |
| `archive/object-a-v2.1.0/` | Byte-identical public OSF Object A package |
| `.zenodo.json` | Zenodo deposition metadata for the software release |
| `CITATION.cff` | GitHub citation metadata for the software release |

## Registration and implementation boundary

Object A is the parent protocol registration. The files in
`archive/object-a-v2.1.0/` are preserved byte-for-byte, including their original
pre-registration status wording. That wording is historical metadata, not the
current status: OSF displays the registration date as 3 August 2026 at 1:24 AM,
and the DOI is shown above.

The code, schema, tests, and synthetic fixture in the repository root are a
post-registration reference implementation. They were not part of Object A and
must not be represented as preregistered. Before any official pilot datum is
generated, a separate study-specific preregistration must freeze the exact
products, settings, prompts, claim targets, evidence-acquisition procedures,
allocation schedule, rater materials, and analysis implementation.

## Deliberate exclusions

This public repository does not contain provider credentials, private case
records, proprietary architectures, schedule secrets, hidden allocation keys,
held-out plaintext, product-specific pilot prompts, or official product data.
It makes no claim of empirical validation, external replication, peer review,
industry prevalence, model consciousness, hidden-state access, deception, or
regulatory compliance.

## Citation

Please cite both the registered protocol and the software release:

Martirosyan, A. (2026). TRACE-FV v2.1: Trigger-Verified Retraction and Correction Endurance under Frame Variance — Black-Box Evaluation Protocol. OSF. https://doi.org/10.17605/OSF.IO/6U3QX
Martirosyan, A. (2026). TRACE-FV: Reference Implementation and Reproducibility Assets (Version 0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21863770
For the latest archived software version, use the concept DOI: https://doi.org/10.5281/zenodo.21863769.

## License

Source code is licensed under Apache-2.0. Documentation, synthetic fixtures,
expected outputs, and the frozen Object A materials are licensed under
CC-BY-4.0 unless a file states otherwise. See `LICENSES.md`.

