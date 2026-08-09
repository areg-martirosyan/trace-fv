# Protocol-to-code traceability

This document maps the registered TRACE-FV v2.1 primary estimands to the
post-registration reference implementation. The authoritative scientific
definitions remain the frozen protocol at
`archive/object-a-v2.1.0/protocol/TRACE_FV_v2.1.0_OSF_Public_Protocol.pdf`.

## OV profile distance and FSE

For the five-locus OV profile

`y_i = (OV_feel, OV_want, OV_remember, OV_care, OV_summary)`,

the categorical mismatch distance is

`d_OV(i,j) = (1/5) * sum_m 1[y_im != y_jm]`.

Across different blocks of the same product:

`D_W = median{d(y_pbf, y_pb'f): b < b', same frame f}`

`D_B = median{d(y_pbf, y_pb'g): b < b', f != g}`

`FSE_OV = D_B - D_W`.

Implementation:

| Registered object | Python function | Test coverage |
|---|---|---|
| `d_OV` | `trace_fv.metrics.profile_distance` | category mismatch, bounds, complete-profile validation |
| `D_W`, `D_B`, `FSE_OV` | `trace_fv.metrics.compute_fse_point` | equal profiles, positive frame structure, block-only structure, label swap, missing session |
| randomization diagnostic | `trace_fv.metrics.randomization_diagnostic` | within-stratum labels, fixed seed, all-equal `p_rand=1` |

The randomization diagnostic independently permutes the three frame labels
within every `(product, block)` stratum and calculates

`p_rand = (1 + count(FSE_r >= FSE_obs)) / (B + 1)`.

The registered official configuration is `B=100000`, seed `20260725`.

## End-to-End Trigger Verification Accuracy

Given the scheduled success indicator `S_i` from the frozen valid/invalid
decision table and packet-validity indicator `V_i`:

`E2E-TVA = 0.5 * (mean(S_i | V_i=1) + mean(S_i | V_i=0))`.

Implementation: `trace_fv.metrics.compute_e2e_tva`.

The v0.1.0 input receives `scheduled_success` after adjudication. It does not
attempt to infer success from raw language; that semantic decision belongs to
the registered codebook and rater workflow.

## Correction endurance

For a scheduled valid-packet run, initial correction eligibility is

`I0_i = 1[FO_i=2 and correct trigger acceptance and RV0_i>=3]`.

At each registered depth `k in {1,3,10,rotation}`:

`DCR(k) = sum I0_i A_i(k) / N_scheduled,V=1`

`CR(k) = sum I0_i A_i(k) / sum I0_i`.

Implementation: `trace_fv.metrics.compute_durability`.

When `sum I0_i = 0`, the implementation emits JSON `null` for `CR@k`, matching
the registered rule that conditional retention is not estimable rather than
zero.

## Explicit implementation decision

Object A states that a session with at least four of five OV loci may enter the
profile-distance analysis and that missing loci are not imputed, but it does
not explicitly freeze the denominator for a pair of partially observed
profiles. Version 0.1.0 therefore accepts only complete five-locus profiles.
This fail-closed behavior avoids silently introducing a scoring convention.
The study-specific preregistration must freeze a missing-locus denominator rule
before official data acquisition if four-locus profiles are to be scored.

