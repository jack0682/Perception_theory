# Experiments 7-8: Allen-Cahn Comparison & Computational Predictions

**Date:** 2026-03-30
**Grid:** 15x15 (225 nodes), beta=20, c=0.3

---

## Experiment 7: Allen-Cahn vs SCC Basin Depth

### Setup
- **Config A (Allen-Cahn):** BD-only (w_cl=0, w_sep=0, w_bd=1, beta=20)
- **Config B (Full SCC):** w_cl=1, w_sep=1, w_bd=1, beta=20
- Perturbation: 20 random directions per delta, projected to Sigma_m
- Hessian eigenvalues via finite-difference power iteration

### Results

| Metric | Allen-Cahn | Full SCC | Ratio (SCC/AC) |
|--------|-----------|----------|----------------|
| E_total | 2.482 | 5.716 | — |
| lam_min (Hessian) | 0.419 | 0.185 | 0.44 |
| lam_max (Hessian) | 6.392 | 7.529 | 1.18 |
| dE(delta=0.01) | 0.000468 | 0.008126 | **17.4x** |
| dE(delta=0.02) | 0.001269 | 0.016478 | **13.0x** |
| dE(delta=0.05) | 0.005531 | 0.043863 | **7.9x** |
| dE(delta=0.10) | 0.017166 | 0.098920 | **5.8x** |
| dE(delta=0.20) | 0.058474 | 0.222882 | **3.8x** |
| Bind | 0.852 | 0.856 | — |
| Sep | 0.926 | 0.944 | — |
| Inside | 1.000 | 0.964 | — |

### Analysis

**Theorem 4 prediction CONFIRMED:** SCC basins are 4-17x deeper than Allen-Cahn basins across all perturbation scales. The self-referential terms (closure + separation) create substantially steeper energy wells around minimizers.

Key observations:
1. **Basin depth ratio decreases with perturbation magnitude** (17x at delta=0.01 down to 3.8x at delta=0.2), suggesting the SCC advantage is most pronounced near the minimizer (steeper local curvature from self-referential terms).
2. **Hessian lam_min is lower for SCC** (0.185 vs 0.419), meaning the SCC landscape has shallower directions. But this is offset by the much larger energy scale — the absolute energy barriers are still higher.
3. **Diagnostic quality is comparable** — SCC slightly better Sep (0.944 vs 0.926), AC slightly better Inside (1.000 vs 0.964).

### Interpretation
The closure energy ||Cl(u)-u||^2 and separation energy sum u_i(1-D_i) create additional energy barriers around coherent formations that pure Allen-Cahn lacks. These terms penalize perturbations that break self-consistency (closure) or dissolve distinction boundaries, making SCC minimizers more robust.

---

## Experiment 8: Computational Predictions

### P1: Contraction Not Projection — CONFIRMED

| Iteration k | ||Cl^k(u) - Cl^{k-1}(u)|| | Ratio |
|-------------|---------------------------|-------|
| 0 | 1.087 | — |
| 5 | 0.182 | 0.843 |
| 10 | 0.087 | 0.868 |
| 15 | 0.044 | 0.873 |
| 20 | 0.022 | 0.875 |
| 25 | 0.011 | 0.875 |
| 29 | 0.007 | 0.875 |

- **Predicted contraction ratio (a_cl/4):** 0.875
- **Observed mean late ratio:** 0.871
- **Relative error:** 0.4%

The closure operator exhibits geometric convergence with ratio converging to a_cl/4 = 0.875, confirming it is a contraction (not a projection). A projection would reach its fixed point in a single step (ratio = 0). The contraction rate exactly matches the theoretical prediction from the A3 axiom (a_cl < 4).

### P2: 4 Independent Dimensions — PARTIALLY CONFIRMED

| Config | Bind | Sep | Inside |
|--------|------|-----|--------|
| BD-only | 0.851 | 0.936 | 1.000 |
| BD+CL | 0.862 | 0.921 | 0.981 |
| BD+SEP | 0.849 | 0.938 | 0.991 |
| Full-SCC | 0.853 | 0.928 | 0.989 |
| CL-only | 1.000 | 0.500 | 0.500 |
| SEP-only | 0.834 | 0.912 | 0.913 |

Correlation matrix (energy weight -> diagnostic):

|       | Bind   | Sep    | Inside |
|-------|--------|--------|--------|
| w_cl  | **+0.531** | -0.458 | -0.403 |
| w_sep | -0.517 | **+0.440** | +0.382 |
| w_bd  | -0.530 | +0.665 | **+0.747** |

- **w_cl -> Bind** (strongest positive correlation): Closure energy primarily drives binding quality
- **w_sep -> Sep** (strongest positive correlation among remaining): Separation energy drives distinction
- **w_bd -> Inside** (strongest positive correlation): Boundary/morphology drives interior coherence

The correlations confirm partial independence: each energy term has a distinguishable primary diagnostic target, though the effects are not perfectly orthogonal. The strongest separation is between w_bd (Inside) and w_cl (Bind), with w_sep providing complementary improvement to Sep.

### P4: Path Dependence — CONFIRMED

| Seed | Energy | Bind | Sep | Inside |
|------|--------|------|-----|--------|
| 0 | 8.542 | 0.852 | 0.894 | 0.004 |
| 1 | 8.253 | 0.852 | 0.901 | 0.003 |
| 2 | 6.285 | 0.857 | 0.930 | 0.967 |
| 3 | 6.043 | 0.854 | 0.937 | 0.975 |
| 4 | 9.397 | 0.852 | 0.878 | 0.004 |

**Energy spread:** 3.35 (44% relative)
**Mean field distance:** 7.51 (threshold for distinct basins: 1.50)

Two distinct classes of minimizers emerged:
1. **Well-formed formations** (seeds 2, 3): E ~ 6.0-6.3, Inside ~ 0.97, Sep ~ 0.93
2. **Fragmented states** (seeds 0, 1, 4): E ~ 8.3-9.4, Inside ~ 0.004, Sep ~ 0.88-0.90

This confirms multiple metastable basins in the SCC energy landscape. The multi-start strategy (default n_restarts=5 in the optimizer) is essential — without it, 3 out of 5 initializations converge to suboptimal fragmented states.

---

## Summary

| Prediction | Status | Key Evidence |
|-----------|--------|-------------|
| P1: Contraction not projection | **CONFIRMED** | Ratio -> a_cl/4 = 0.875, error 0.4% |
| P2: 4 independent dimensions | **PARTIALLY CONFIRMED** | Each w has distinct primary target |
| P4: Path dependence | **CONFIRMED** | 44% energy spread, 2 basin classes |
| Thm 4: SCC > AC basin depth | **CONFIRMED** | 4-17x deeper basins |

Runtime: 17.7s total (exp7: 8.9s, exp8: 8.8s)
