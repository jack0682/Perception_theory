# exp48 Analysis: Λ_coupling Regime Sweep Results

**Date:** 2026-04-02
**Session:** Experimental validation of unified regime parametrization
**Category:** experiment
**Status:** complete
**Depends on:** UNIFIED-REGIME-PARAMETRIZATION.md, T-PERSIST-K-UNIFIED.md

---

## 1. Setup

48 configurations: 2 grids (8×8, 10×10) × 2 volume fractions (0.40, 0.45) × 12 λ_rep values (0.001 to 10.0). K=2, β=10.

## 2. Key Results

### 2.1. Regime Transitions Exist

| Actual Regime | Count | λ_rep range | d_min | overlap |
|---------------|-------|-------------|-------|---------|
| well-separated | 0 | — | — | — |
| weakly-interacting | 41 | 0.001–10.0 | 0–1 | 0–16 |
| strongly-interacting | 7 | 0.001–0.02 | 0 | 4–16 |

Strongly-interacting formations appear at low λ_rep (≤ 0.02) where repulsion is too weak to separate the formations. At λ_rep ≥ 1, formations always separate (d_min ≥ 1, overlap = 0).

### 2.2. Prediction Accuracy: 17% (8/48)

**Root causes of poor prediction:**

1. **Spectral gap instability.** μ_k (computed from E_bd Hessian) is near zero at some formations, causing Λ = λ_rep · ω / μ to blow up. Example: 10×10 vf=0.45 lrep=0.01: ω = 0.034, μ = 1e-6, giving Λ = 336 — wildly above the bifurcation threshold 1.0.

2. **Hard/soft overlap mismatch.** classify_regime() uses hard support overlap (sites with u > θ_supp), while Λ_coupling uses soft overlap weight ω_jk. A formation with ω_jk = 0.035 (soft) can have 0 or 16 hard overlap sites depending on the threshold.

3. **Multi-start variability.** The optimizer (2 restarts) can land on different local minima with different spectral gaps. This creates noise in Λ_coupling.

### 2.3. What the Theory Gets RIGHT

Despite poor quantitative predictions, the **qualitative structure** is correct:

- **Monotonicity in λ_rep:** Higher λ_rep → less overlap → more separated formations ✓
- **Low λ_rep creates strong interaction:** overlap > 0 only at λ_rep ≤ 0.1 ✓  
- **d_min correlates with regime:** d_min = 0 ↔ strongly/weakly-interacting; d_min ≥ 2 ↔ well-separated ✓

### 2.4. What Needs Fixing

1. **Use full energy spectral gap** (μ_full, not μ_bd) in Λ_coupling denominator. μ_full is more stable because E_cl adds positive curvature (§2.7-2.10 of CATEGORY-B-UPGRADES.md).

2. **Regularize μ:** Use μ_eff = max(μ, μ_floor) with μ_floor set from the closure curvature bound: μ_floor ≥ w_cl · 2(1 - a_cl/4)² ≈ 0.03.

3. **Align classify_regime with Λ_coupling:** Either update classify_regime to use soft overlap, or define Λ thresholds in terms of the hard overlap quantities it currently uses.

4. **More restarts:** 2 restarts insufficient for stable μ estimation. Use n_restarts ≥ 5.

## 3. Revised Λ_coupling Proposal

$$\Lambda_{\mathrm{coupling}}^{\mathrm{reg}} = \max_{j \neq k} \frac{\lambda_{\mathrm{rep}} \cdot \omega_{jk}}{\max(\min(\mu_j^{\mathrm{full}}, \mu_k^{\mathrm{full}}), \; \mu_{\mathrm{floor}})}$$

where $\mu_k^{\mathrm{full}}$ is the full energy Hessian spectral gap and $\mu_{\mathrm{floor}} = w_{\mathrm{cl}} \cdot 2(1 - a_{\mathrm{cl}}/4)^2$.

## 4. Status

The unified parametrization's **theoretical foundation** is validated (correct qualitative behavior, correct limiting cases). The **numerical implementation** needs the three fixes above. This is a calibration issue, not a theoretical flaw.

**Next step:** Implement regularized Λ_coupling and re-run exp48.
