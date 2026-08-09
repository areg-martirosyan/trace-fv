# Implementation status and non-claims

## Implemented in v0.1.0

- complete five-locus categorical OV profile distance;
- pooled and product-specific `D_W`, `D_B`, and `FSE_OV`;
- within-`(product, block)` Monte Carlo frame-label randomization;
- balanced `E2E-TVA` from frozen scheduled-success adjudications;
- `DCR@k` and `CR@k` at depths 1, 3, 10, and rotation;
- deterministic validation of run identifiers, design cells, score ranges, and
  trigger fields;
- synthetic fixture, expected output, tests, and CI;
- byte-integrity check of the archived Object A package.

## Not implemented in this release

This release does not collect live product sessions, generate evidence
packets, adjudicate free text, implement rater assignment, compute inter-rater
reliability, estimate Wilson or posterior intervals, produce retention curves,
or implement exploratory FAI, LAD, FTI, CFRG, or SIED analyses.

These exclusions are a versioned scope boundary, not a claim that the omitted
work is unnecessary. They keep v0.1.0 small enough to audit while completing
one real scoring path end to end.

## Evidence status

The repository demonstrates that selected registered estimands are computable
from a declared input contract. It does not show that TRACE-FV has been
validated, replicated, peer reviewed, or run against a product. It does not
establish industry prevalence, provider-wide behavior, private subjective
state, hidden mechanisms, consciousness, deception, or regulatory compliance.

## Version boundary

- Protocol: `2.1.0`, registered Object A.
- Software: `0.1.0`, post-registration reference implementation.

The two versions identify different objects and must not be collapsed into one
DOI or one release claim.

