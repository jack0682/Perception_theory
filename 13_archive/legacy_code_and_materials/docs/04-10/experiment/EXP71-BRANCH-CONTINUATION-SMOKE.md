# Exp71 Branch-Continuation Threshold Smoke

**Date:** 2026-04-10
**Session:** Cycle 51 — branch continuation smoke result
**Category:** experiment
**Status:** complete
**Depends on:** EXP71-BRANCH-CONTINUATION-DESIGN.md; experiments/exp71_branch_continuation_threshold.py

---

## 1. CURRENT GAP

Independent optimized rows do not preserve branch identity, so `DeltaE0/DeltaR` threshold estimates were invalid. Exp71 warm-starts branches upward/downward in `lambda_rep` to preserve branch identity.

---

## 2. Smoke Protocol

```bash
python3 experiments/exp71_branch_continuation_threshold.py \
  --config 10x10:0.6 \
  --lambdas 0 0.1 0.5 1.0 \
  --n-restarts 1 \
  --max-iter 300 \
  --output-json experiments/results/exp71_branch_continuation_threshold_smoke.json \
  --output-csv experiments/results/exp71_branch_continuation_threshold_smoke.csv
```

---

## 3. Branch Rows

| Direction | lambda | E_lambda | E0 | overlap | center offset | type |
|---|---:|---:|---:|---:|---:|---|
| up | 0.0 | 12.405917 | 12.405917 | 8.794843 | 0.109224 | Mixed |
| up | 0.1 | 4.616632 | 4.579487 | 0.371451 | 0.184650 | Type B |
| up | 0.5 | 4.624506 | 4.618951 | 0.011111 | 0.179426 | Type B |
| up | 1.0 | 4.613215 | 4.609878 | 0.003337 | 0.177023 | Type B |
| down | 0.0 | 4.682851 | 4.682851 | 0.000000 | 0.077138 | Type A |
| down | 0.1 | 4.715393 | 4.715393 | 0.000000 | 0.070345 | Type A |
| down | 0.5 | 4.769359 | 4.769359 | 0.000000 | 0.061541 | Type A |
| down | 1.0 | 5.515394 | 5.514040 | 0.001354 | 0.042070 | Type A |

---

## 4. Threshold Estimate Rows

| lambda | lower-overlap branch | higher-overlap branch | delta_E0 | delta_R | lambda_star | branch types |
|---:|---|---|---:|---:|---:|---|
| 0.0 | down | up | -7.723066 | 8.794843 | -0.878136 | up Mixed / down Type A |
| 0.1 | down | up | 0.135907 | 0.371451 | 0.365880 | up Type B / down Type A |
| 0.5 | down | up | 0.150408 | 0.011111 | 13.537208 | up Type B / down Type A |
| 1.0 | down | up | 0.904162 | 0.001983 | 456.001862 | up Type B / down Type A |

---

## 5. Interpretation

Warm-start continuation preserves two distinct branches:

- **Up branch:** starts high-overlap / mixed at `lambda=0`, then jumps or relaxes into Type B with small but nonzero overlap.
- **Down branch:** remains Type A and nearly zero-overlap across the sweep.

The threshold estimate is meaningful only where branch identities are stable and `delta_R` is not tiny. The `lambda=0.1` estimate (`lambda_star≈0.366`) is the only plausible finite threshold row in this smoke run. At larger lambda, `delta_R` is too small and threshold estimates explode.

The `lambda=0` row shows the down branch already has much lower `E0`, so the up branch is not the zero-repulsion ground branch. This confirms that source branch selection is history/basin dependent.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| branch continuation is necessary | confirmed |
| up/down branches remain distinct | confirmed in smoke |
| threshold can be estimated from continuation | partially, but unstable and branch-dependent |
| independent optimized rows are enough | rejected |
| robust threshold theorem | not yet; needs better branch identity controls and more lambdas |

---

## 7. Next Trigger

Refine Exp71:

> Add branch-distance metrics between successive warm-start fields and detect jumps, so threshold estimates are only reported on continuous branch segments.
