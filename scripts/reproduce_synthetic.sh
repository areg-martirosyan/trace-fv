#!/usr/bin/env sh
set -eu

python -m trace_fv reproduce \
  synthetic_data/worked_example.json \
  --permutations 999 \
  --seed 20260725 \
  --output build/worked_example_metrics.json

