# Branch Reselection Threshold Estimate

**Date:** 2026-04-10
**Session:** Cycle 50 — empirical branch-reselection threshold estimate
**Category:** audit
**Status:** complete
**Depends on:** POSITIVE-REPULSION-BRANCH-RESELECTION.md; experiments/results/exp69_branch_reselection_threshold_10x10_c06.csv

---

## 1. CURRENT GAP

The finite-candidate theorem gives a threshold

```text
lambda > DeltaE_0 / DeltaR
```

when comparing two identified branches with known zero-repulsion self-energy difference `DeltaE_0` and overlap difference `DeltaR`.

We tested whether available exp69 optimized branches allow such a threshold estimate.

---

## 2. Diagnostic Run

Command:

```bash
python3 experiments/exp69_relaxed_merge_neb_sweep.py \
  --configs 10x10:0.6 \
  --lambda-reps 0 0.05 0.1 0.5 1 \
  --n-images 7 \
  --n-iter 10 \
  --step 0.001 \
  --spring 0.05 \
  --n-restarts 1 \
  --max-iter 250 \
  --output-json experiments/results/exp69_branch_reselection_threshold_10x10_c06.json \
  --output-csv experiments/results/exp69_branch_reselection_threshold_10x10_c06.csv
```

---

## 3. Source Branch Summary

Inferred zero-repulsion self-energy is computed as

```text
E0_inferred = E_lambda_source - lambda * source_overlap.
```

| lambda | E_lambda_source | source_overlap | E0_inferred | dE0 vs lambda=0 | dR vs lambda=0 | threshold estimate |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 14.597629 | 8.315565 | 14.597629 | 0 | 0 | — |
| 0.05 | 15.590423 | 8.835832 | 15.148632 | +0.551003 | -0.520268 | invalid |
| 0.1 | 15.937716 | 9.139201 | 15.023796 | +0.426167 | -0.823636 | invalid |
| 0.5 | 18.569444 | 8.090028 | 14.524430 | -0.073199 | +0.225537 | -0.3246 |
| 1.0 | 6.113963 | 0.006896 | 6.107067 | -8.490562 | +8.308668 | -1.0219 |

---

## 4. Interpretation

The available optimized branches do **not** yield a clean threshold estimate:

1. At `lambda=0.05` and `0.1`, the optimizer found branches with **higher** overlap than the zero-repulsion branch, so they are not lower-overlap competitors.
2. At `lambda=0.5` and `1.0`, the inferred `E0` is lower than the zero-repulsion branch, so the positive-lambda winner is not merely paying self-energy cost for lower overlap; it appears to be a different lower-self-energy basin/branch.
3. The threshold formula `DeltaE_0/DeltaR` is meaningful only when two candidate branches are matched across lambda and compared as fixed candidates. Current multi-start optimized outputs do not provide branch identity matching.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| threshold can be estimated from current optimized exp69 rows | rejected |
| branch identity matching is required | yes |
| positive repulsion selects lower-overlap branch | theorem remains true for fixed candidate set |
| current data shows optimizer branch reselection | yes, but not enough for threshold formula |

---

## 6. Next Trigger

To estimate thresholds honestly, implement branch continuation rather than independent reoptimization:

> Warm-start a branch from `lambda=0` upward and another from `lambda=1` downward, preserving branch identity, then compare their fixed-candidate energies and overlaps.
