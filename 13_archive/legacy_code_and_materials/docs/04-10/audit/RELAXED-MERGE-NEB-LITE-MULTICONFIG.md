# Relaxed Merge NEB-Lite Multi-Config Smoke

**Date:** 2026-04-10
**Session:** Cycle 39 — exp68 multi-config smoke comparison
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-NEB-LITE-HARDENING.md; experiments/exp68_relaxed_merge_neb.py

---

## 1. CURRENT GAP

Test whether NEB-lite consistently lowers direct relaxed interpolation across a small set of configurations without violating relaxed constraints.

---

## 2. Protocol

Common settings:

```text
lambda_rep = 1
n_images = 9
n_iter = 50
step = 0.001
spring = 0.05
n_restarts = 1
max_iter = 300
```

Configs:

```text
10x10:0.5
10x10:0.6
12x12:0.6
```

---

## 3. Results

| Config | Initial max_delta | Relaxed max_delta | Improvement | Max mass error | Max simplex violation | History monotone |
|---|---:|---:|---:|---:|---:|---|
| 10x10:0.5 | 4.893503 | 4.633269 | 0.260234 | 7.958e-13 | 0 | true |
| 10x10:0.6 | 8.652672 | 8.102978 | 0.549694 | 6.111e-13 | 0 | true |
| 12x12:0.6 | 11.784154 | 11.118872 | 0.665282 | 1.364e-12 | 0 | true |

---

## 4. Interpretation

NEB-lite consistently lowered the direct interpolation communication-height proxy in all three smoke configurations, with no observed mass/simplex constraint violations and monotone recorded max-energy history.

This strengthens the evidence that direct interpolation is not the right MEP estimator. It does **not** prove NEB-lite convergence or true communication height.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| direct interpolation locally optimal | falsified in all smoke configs |
| NEB-lite improves path proxy | supported numerically |
| constraint artifacts explain improvement | not supported by diagnostics |
| true MEP found | not proved |

---

## 6. Next Trigger

Proceed to convert exp68 into a reusable experiment with summary CSV across configs and seeds, or pause for commit/handoff if engineering cleanup is preferred.

First move if continuing theorem work:

> Add `--summary-csv` to exp68 or create `exp69_relaxed_merge_neb_sweep.py` to run config/seed sweeps and aggregate communication-height proxy statistics.
