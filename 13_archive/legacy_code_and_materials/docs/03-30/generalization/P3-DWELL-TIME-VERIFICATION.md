# P3 Verification: Enhanced Dwell Times — SCC vs Allen-Cahn

**Date:** 2026-03-30

## RESULT: SCC formations survive noise 1.5x more often than Allen-Cahn

### Langevin Escape Experiment

Setup: 8×8 grid, β=5 (weak formation), T=2.0 (high noise), 30 trials each.
Escape criterion: Bind drops below 0.75.
Observation window: 30 seconds (30,000 steps × dt=0.001).

| Metric | AC-only | Full SCC |
|--------|---------|----------|
| Survived (30s) | 16/30 (53%) | **24/30 (80%)** |
| Escaped | 14/30 (47%) | 6/30 (20%) |
| Mean escape time (escaped) | 16.87s | 15.88s |

### Temperature Sweep (mean Bind under noise)

| T | AC Bind | SCC Bind | Δ |
|---|---------|----------|---|
| 0.05 | 0.861 | 0.876 | +0.015 |
| 0.10 | 0.831 | 0.860 | +0.029 |
| 0.20 | 0.819 | 0.840 | +0.021 |
| 0.50 | 0.816 | 0.827 | +0.011 |
| 1.00 | 0.814 | 0.820 | +0.006 |

SCC maintains higher Bind at ALL temperatures.

### Interpretation

The self-referential closure term E_cl = ||Cl(u)-u||² acts as a restoring force: when noise perturbs u away from self-support, the closure gradient pulls it back. Allen-Cahn has no such mechanism — its restoring force comes only from the double-well potential, which is purely local (site-by-site) rather than relational (neighborhood-dependent).

This is the first computational validation of P3: SCC formations exhibit enhanced metastability under stochastic perturbation, as predicted by T4 (Hessian curvature enhancement).

### Statistical Significance

Survival: 24/30 vs 16/30. Fisher exact test: p = 0.037 (one-tailed). Significant at α=0.05.
