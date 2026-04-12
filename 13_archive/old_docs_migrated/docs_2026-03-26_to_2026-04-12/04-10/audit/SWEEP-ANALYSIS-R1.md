# SWEEP-ANALYSIS-R1

**Date:** 2026-04-10
**Session:** R1 lambda-rep sweep analysis
**Category:** audit
**Status:** complete
**Depends on:** EXPERIMENT-THEORY-BRIDGE.md; experiments/results/exp65_sweep_20x20_c06_lrep_0.json

---

## Sweep Protocol

Config: `20x20_c0.6`.

Fixed protocol:

- `exp65_formation_tracking.py`
- `n_restarts=4`
- `max_iter=1500`
- epsilons `[-3,-2,-1,-0.5,0,0.5,1,2,3]`

Varied only `lambda_rep` over:

```text
0, 0.05, 0.1, 0.2, 0.5, 1.0
```

## Result Table

| `lambda_rep` | Type label | Mean center offset | Max center offset | Mean separation | Swaps | E(+)-E(-) | `Lambda_coupling` |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0.00 | Type B candidate | 0.1877 | 0.1884 | 10.62 | 0 | -0.0238 | 0 |
| 0.05 | Type A candidate | 0.0164 | 0.0195 | 12.50 | 0 | +0.0601 | 0 |
| 0.10 | Type A candidate | 0.0195 | 0.0210 | 12.54 | 0 | +0.0516 | 0 |
| 0.20 | Type A candidate | 0.0280 | 0.0313 | 12.42 | 0 | +0.0682 | 0 |
| 0.50 | Type A candidate | 0.0397 | 0.0440 | 12.30 | 0 | +0.0945 | 0 |
| 1.00 | Type A candidate | 0.0459 | 0.0465 | 12.16 | 0 | +0.0571 | 0 |

## Interpretation

The branch switch is not resolved as a smooth threshold in `[0,1]`; the observed transition occurs between `lambda_rep=0` and the first positive tested value `0.05`.

This suggests a **singular zero-repulsion degeneracy** rather than a generic finite-positive bifurcation. In words:

- At `lambda_rep=0`, branch selection is dominated by decoupled formation placement, simplex penalty, and optimizer history.
- For any tested positive `lambda_rep`, even very small repulsion selects a centered/well-separated branch under this protocol.
- `Lambda_coupling` remains zero throughout because supports are disjoint; therefore it cannot distinguish zero-repulsion off-center disjoint branches from positive-repulsion centered disjoint branches.

## Theorem Direction Created by Sweep

The next theorem target is no longer “find threshold near `lambda_rep≈0.5`.” The target is:

> Prove a zero-repulsion degeneracy / positive-repulsion selection theorem: when `lambda_rep=0`, automorphism-related and history-selected disjoint local branches can coexist; when `lambda_rep>0`, the first-order perturbation among degenerate disjoint candidate pairs selects branches minimizing overlap and/or maximizing separation, but centeredness still requires graph symmetry assumptions.

## Registry Consequence

No theorem category changes. R1 remains active, but its obstruction is sharper: **zero-repulsion degeneracy + missing branch/history state**.
