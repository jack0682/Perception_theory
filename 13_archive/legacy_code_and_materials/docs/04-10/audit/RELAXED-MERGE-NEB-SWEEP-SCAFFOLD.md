# Relaxed Merge NEB-Lite Sweep Aggregator

**Date:** 2026-04-10
**Session:** Cycle 40 — exp69 NEB-lite sweep aggregator
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-NEB-LITE-MULTICONFIG.md; experiments/exp69_relaxed_merge_neb_sweep.py

---

## 1. CURRENT GAP

Convert exp68 from one-off smoke runs into a reusable sweep aggregator that emits summary CSV/JSON for communication-height proxy statistics.

---

## 2. Implementation

Created:

```text
experiments/exp69_relaxed_merge_neb_sweep.py
```

It runs exp68 over multiple configs and lambda values, recording:

- initial max_delta,
- relaxed max_delta,
- improvement and improvement fraction,
- constraint diagnostics,
- history monotonicity.

---

## 3. Smoke Run

Command:

```bash
python3 experiments/exp69_relaxed_merge_neb_sweep.py \
  --configs 10x10:0.5 10x10:0.6 \
  --lambda-reps 1.0 \
  --n-images 7 \
  --n-iter 25 \
  --step 0.001 \
  --spring 0.05 \
  --n-restarts 1 \
  --max-iter 250 \
  --output-json experiments/results/exp69_relaxed_merge_neb_sweep_smoke.json \
  --output-csv experiments/results/exp69_relaxed_merge_neb_sweep_smoke.csv
```

Observed:

| Config | Initial | Relaxed | Improvement | Improvement frac | Mass error | Simplex violation | Monotone |
|---|---:|---:|---:|---:|---:|---:|---|
| 10x10:0.5 | 14.175321 | 13.879431 | 0.295890 | 0.0209 | 1.009e-12 | 0 | true |
| 10x10:0.6 | 7.817848 | 7.457876 | 0.359972 | 0.0460 | 1.620e-12 | 0 | true |

---

## 4. Interpretation

The aggregator works and preserves constraints in the smoke run. NEB-lite again lowers the direct path proxy in both configs.

This is now a reusable numerical scaffold for communication-height exploration, but still not theorem evidence.

---

## 5. Next Trigger

Use exp69 for a broader grid/lambda sweep only after choosing which theorem question it supports. The current best theorem target remains deterministic: sublevel-set/path-class conditions for relaxed merge.

First move:

> Decide whether to pause for commit/handoff or run a targeted exp69 sweep for the most relevant branch/path question.
