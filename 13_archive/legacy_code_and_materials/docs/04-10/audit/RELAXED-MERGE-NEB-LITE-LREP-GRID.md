# Relaxed Merge NEB-Lite Lambda/Grid Sweep

**Date:** 2026-04-10
**Session:** Cycle 43 — targeted exp69 lambda/grid sweep
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-NEB-LITE-LREP-SWEEP.md; experiments/exp69_relaxed_merge_neb_sweep.py

---

## 1. CURRENT GAP

Test whether the lambda-rep dependence seen in one config repeats across multiple small grid/volume configurations.

---

## 2. Protocol

Configs:

```text
10x10:0.5
10x10:0.6
12x12:0.6
```

Lambda sweep:

```text
lambda_rep = 0, 1, 5
```

Common settings:

```text
n_images = 7
n_iter = 25
step = 0.001
spring = 0.05
n_restarts = 1
max_iter = 250
```

Outputs:

```text
experiments/results/exp69_relaxed_merge_neb_sweep_lrep_config_grid.json
experiments/results/exp69_relaxed_merge_neb_sweep_lrep_config_grid.csv
```

---

## 3. Results

| Config | lambda_rep | Initial | Relaxed | Improvement | Improvement frac | Simplex violation | Monotone |
|---|---:|---:|---:|---:|---:|---:|---|
| 10x10:0.5 | 0 | 0.000000 | 0.000000 | 0.000000 | 0.0000 | 0 | true |
| 10x10:0.5 | 1 | 4.917542 | 4.700906 | 0.216636 | 0.0441 | 0 | true |
| 10x10:0.5 | 5 | 9.115947 | 8.209190 | 0.906757 | 0.0995 | 0 | true |
| 10x10:0.6 | 0 | 0.000000 | 0.000000 | 0.000000 | 0.0000 | 0 | true |
| 10x10:0.6 | 1 | 9.549813 | 9.208117 | 0.341696 | 0.0358 | 0 | true |
| 10x10:0.6 | 5 | 31.083158 | 27.256190 | 3.826969 | 0.1231 | 0 | true |
| 12x12:0.6 | 0 | 0.000000 | 0.000000 | 0.000000 | 0.0000 | 0 | true |
| 12x12:0.6 | 1 | 11.987056 | 11.620566 | 0.366489 | 0.0306 | 0 | true |
| 12x12:0.6 | 5 | 36.401644 | 31.372025 | 5.029619 | 0.1382 | 0 | true |

---

## 4. Interpretation

The pattern is now repeated across all three tested configs:

1. `lambda_rep=0` gives zero relaxed merge communication proxy.
2. positive `lambda_rep` gives nonzero proxy.
3. increasing `lambda_rep` increases the proxy.
4. NEB-lite relaxation lowers the direct proxy in all positive-repulsion cases.
5. diagnostics show no mass/simplex violations.

This supports the branch-conditioned theorem architecture:

```text
relaxed merge communication height depends strongly on repulsion and path class.
```

---

## 5. Status

| Claim | Status |
|---|---|
| zero-repulsion relaxed communication proxy can collapse | repeated numerical support |
| positive repulsion creates barrier proxy | repeated numerical support |
| NEB-lite lowers direct path | repeated numerical support |
| exact communication height / MEP | not proved |
| theorem category change | none |

---

## 6. Next Trigger

Given repeated smoke evidence, stop broad numerical exploration and return to theorem work or delivery.

Recommended next theorem target:

> Prove or disprove whether `lambda_rep=0` relaxed merge proxy is exactly zero under the exp67/exp69 endpoint convention, and characterize when the source and target lie in the same connected component of a zero-excess sublevel set.
