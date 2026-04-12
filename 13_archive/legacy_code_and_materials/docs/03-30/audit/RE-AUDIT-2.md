# RE-AUDIT-2: Adversarial Numerical & Mathematical Verification

**Date:** 2026-03-30
**Scope:** Energy gradients, optimizer convergence, volume projection, Fiedler computation, resolvent stability, silent numerical failures
**Auditor stance:** Maximally adversarial — hand-derive every formula, run every computation, trust nothing

---

## VERIFIED CORRECT

### V1. Energy gradients match finite differences to machine precision

All three energy gradients were verified against centered FD (h=1e-7) on a 4x4 grid with random field:

| Term | Max FD error | Verdict |
|------|-------------|---------|
| ∇E_cl | 2.48e-10 | ✓ Correct |
| ∇E_sep | 3.78e-09 | ✓ Correct |
| ∇E_bd | 1.30e-08 | ✓ Correct |

**Hand derivation of ∇E_cl:**
- E_cl = ||Cl(u) - u||² = Σ(Cl_i(u) - u_i)²
- ∂E_cl/∂u_j = 2Σ(Cl_i - u_i)(∂Cl_i/∂u_j - δ_ij) = 2(J_Cl - I)^T(Cl(u) - u)
- Code (energy.py:84-87): `2.0 * (JtR - residual)` where JtR = J_Cl^T @ (Cl(u) - u). **Matches.**

**Hand derivation of ∇E_sep:**
- E_sep = Σ u_i(1 - D_i(u))
- ∂E_sep/∂u_j = (1 - D_j) - Σ u_i(∂D_i/∂u_j) = (1 - D_j) - (J_D^T u)_j
- Code (energy.py:106-108): `frozen_part - jac_part` = (1-D) - J_D^T u. **Matches.**

**Hand derivation of ∇E_bd:**
- E_bd = 2α u^T L u + β Σ W(u_i)
- ∇E_bd = 4αLu + βW'(u) where W'(u) = 2u(1-u)(1-2u)
- Code (energy.py:63-64): `4.0 * alpha_bd * Lu + beta_bd * double_well_deriv(u)`. **Matches.**

### V2. Jacobian formulas are correct

**Closure Jacobian:**
- Cl(u)(x) = σ(a_cl((1-η)u(x) + ηP_t(u)(x) - τ))
- J_Cl = diag(σ' · a_cl) · ((1-η)I + ηP)
- J_Cl^T · v = ((1-η)I + ηP^T)(σ' · a_cl · v)
- Code (operators.py:86-102) matches exactly. ✓

**Distinction Jacobian:**
- D(u)(x) = σ(a_D((1+λ_D)P_t(u)(x) - λ_D P_1(x)) - τ_D)
- J_D = diag(σ'_D · a_D · (1+λ_D)) · P
- Code (operators.py:143-156) matches exactly. ✓

### V3. Closure contraction bound is correct

The proof (paper1, Theorem 1) claims ||Cl(u) - Cl(v)||_∞ ≤ (a_cl/4)||u - v||_∞. Verification:
- max σ'(z) = 1/4 (attained at z=0). ✓
- P is sub-stochastic (rows sum to deg/(deg + ε) < 1), hence non-expansive in ∞-norm. ✓
- (1-η)I + ηP is a convex combination of I and P, hence non-expansive. ✓
- Lipschitz constant = (1/4) · a_cl. For a_cl < 4, this is < 1. ✓

The actual contraction rate is slightly better than a_cl/4 due to ε in the denominator of P, but the stated bound is valid.

### V4. Phase transition formula is correct

Paper1 Theorem 3: β/α > 4λ₂/|W''(c)| ensures non-uniform minimizer.
- Hessian of smoothness on T(Σ_m): 4αL (ordered-pair convention). ✓
- W''(c) = 2(1 - 6c + 6c²) = 12c² - 12c + 2. ✓
- At c ∈ spinodal, W''(c) < 0. Fiedler direction gives v₂^T H v₂ = 4αλ₂ + βW''(c) < 0. ✓

### V5. Łojasiewicz convergence argument is structurally sound

Paper1 Theorem 5 invokes Łojasiewicz-Simon for real-analytic functions on compact domains. The energy is real-analytic when b_D = 0 (sigmoid, polynomial, rational operations compose analytically; Σ_m ∩ [0,1]^n is compact semialgebraic). The argument is standard. ✓

---

## NEW ISSUES FOUND

### **BUG-1 (CRITICAL): Hessian normalization has spurious factor of 2**

**Location:** energy.py:190-191

```python
sigma_bd = abs(4.0 * self.params.alpha_bd * lam_max_L
               + 2.0 * self.params.beta_bd * W_pp)
```

The `2.0` multiplying `beta_bd * W_pp` is **wrong**. The E_bd Hessian at u = c·1 is:

    ∇²E_bd = 4α L + β W''(c) I

The spectral norm (largest absolute eigenvalue restricted to T(Σ_m)) is:

    max_{k≥2} |4α λ_k + β W''(c)|

The code computes |4α λ_max + **2**β W''(c)|, introducing a factor of 2 on the double-well curvature that has no mathematical justification.

**Empirical confirmation (6x6 grid, default params):**

| Method | σ_bd |
|--------|------|
| FD power iteration (ground truth) | 24.6564 |
| Correct formula: \|4αλ_max + βW''(c)\| | 24.6564 |
| Code formula: \|4αλ_max + 2βW''(c)\| | 19.4564 |

The code **underestimates** σ_bd by ~21%. Since λ_bd = w_bd / σ_bd, this **overweights** E_bd by ~24% (1.24x on 15x15 grid). All experimental results in both papers were computed with this bug, meaning the reported energy weight ratios and formation diagnostics are systematically biased toward the boundary energy.

**Impact on reported results:**
- The "sweet spot" at λ_sep/λ_bd ≈ 1 (paper1 line 768) was found with buggy normalization. The true sweet spot is at a different ratio.
- The Hessian normalization suggestion "λ_sep/λ_bd ~ 10^{-5}" (paper1 line 854) is computed with the wrong formula.

**Fix:** Change `2.0 * self.params.beta_bd * W_pp` to `self.params.beta_bd * W_pp` on line 191.

### **BUG-2 (CRITICAL): Optimizer NEVER converges on standard test cases**

Tested find_formation on 10×10 and 15×15 grids with default parameters (max_iter=10000, n_restarts=5):

| Grid | Best seed | converged | Iterations | Final ‖∇E‖ | Threshold |
|------|-----------|-----------|------------|-------------|-----------|
| 10×10 | 0 | **False** | 1628 | 9.29e-02 | 1e-06 |
| 10×10 | 1 | **False** | 467 | 6.80e-02 | 1e-06 |
| 10×10 | 2 | **False** | 173 | 7.60e-02 | 1e-06 |
| 10×10 | 3 | **False** | 1658 | 9.29e-02 | 1e-06 |
| 10×10 | 4 | **False** | 464 | 7.57e-02 | 1e-06 |
| 15×15 | best | **False** | 356 | 8.54e-02 | 1e-06 |

**Zero out of ten runs converge.** The gradient norm stagnates at ~0.07-0.09, four orders of magnitude above the convergence threshold of 1e-6. The optimizer exits via the stagnation check (lines 159-161) or max_iter, not via convergence.

This means:
1. **All experimental results in both papers use non-converged fields.** The `converged` flag is False for every reported result.
2. The `find_formation` API silently returns non-converged results without warning.
3. The gradient norm at termination (~0.09) means the field is not at a critical point — it's an approximate minimizer at best.

**Possible causes:**
- The convergence threshold eps_grad = 1e-6 is unrealistically tight for this problem
- The BB step size oscillates without damping
- The non-smooth projection disrupts gradient-based convergence
- The stagnation exit (50-iteration window) triggers before true convergence

**Mitigation:** Either (a) relax convergence thresholds to realistic values (eps_grad ~ 1e-2 would match actual termination behavior), or (b) add convergence warnings to find_formation, or (c) investigate why the gradient plateaus.

### **BUG-3 (MODERATE): Hessian normalization ignores negative eigenvalue at λ₂**

**Location:** energy.py:184-191

The code only checks the eigenvalue at λ_max(L). But the spectral norm on T(Σ_m) is max(|eigenvalue at λ_max|, |eigenvalue at λ_2|). When W''(c) < 0 (formation regime), the eigenvalue at λ₂ is more negative. If β|W''(c)| > 4αλ_max (strong double-well), ALL eigenvalues are negative, and the one at λ₂ has the largest absolute value — the code misses this.

For default parameters this doesn't bite (the positive eigenvalue at λ_max dominates), but for β > 4αλ_max/|W''(c)| ≈ 61 (6×6 grid), the code would silently underestimate the spectral norm.

### **ISSUE-4 (MODERATE): project_volume is biased — not the Euclidean nearest-point projection**

The code (optimizer.py:39-55) uses iterative clip-and-**multiply** (u *= m/s). The true projection onto {v ∈ [0,1]^n : Σv = m} is clip-and-**shift** (v = clip(u - λ, 0, 1), solve for λ).

**Empirical comparison:**

| Method | Projected u | Distance from original |
|--------|-------------|----------------------|
| Code (clip-rescale) | [0.633, 0.633, 0.633, 0.033, 0.033, 0.033, 0.333, 0.333, 0.333] | 0.620 |
| True (clip-shift) | [0.725, 0.725, 0.725, 0.000, 0.000, 0.000, 0.275, 0.275, 0.275] | 0.558 |

The code gives a point 11% farther from the original than the true projection. The multiplicative scaling uniformly shrinks all components, while the true projection clips small components to 0 and preserves large components — qualitatively different behavior.

**Impact:** The optimizer takes projection steps that are not the nearest feasible point, introducing systematic drift. This may contribute to the convergence failure (BUG-2) since the projected gradient is not the true Riemannian gradient on Σ_m.

**Fix:** Replace clip-rescale with the standard KKT-based projection:
```python
def project_volume(u, m):
    from scipy.optimize import brentq
    def vol(lam): return np.sum(np.clip(u - lam, 0, 1)) - m
    lam = brentq(vol, u.min() - 1, u.max() + 1)
    return np.clip(u - lam, 0, 1)
```

### **ISSUE-5 (MODERATE): Gradient computed twice per accepted step**

In optimizer.py, the gradient is computed at line 101 (`g = ec.gradient(u)`) and again at line 133 (`g_new = ec.gradient(u_new)`) after step acceptance. On the next iteration, `u = u_new` and the gradient is recomputed at line 101. The `g_new` computation at line 133 (used only for BB) is discarded.

This doubles the gradient evaluation cost per accepted step. The fix: cache g_new and reuse it as g on the next iteration.

### **ISSUE-6 (MODERATE): Paper1 Figure 2 caption contradicts Theorem 4 disclaimer**

Paper1 Figure 2 caption (line 440):
> "SCC basin with depth Δ E_SCC > Δ E_AC"

But the theorem's own disclaimer (line 411-413):
> "the relationship between Hessian eigenvalue and actual barrier height ... requires additional Morse-theoretic analysis not pursued here"

The figure caption directly claims deeper basins (Δ E), which is exactly what the remark disclaims. The caption should say "greater local curvature" not "greater depth."

### **ISSUE-7 (LOW): W_sym can have negative eigenvalues — resolvent convergence check is misleading**

The cohesion-weighted symmetric matrix W_sym = 0.5(D^{-1}W_weighted + W_weighted^T D^{-1}) is NOT positive semidefinite. Empirical test on 5×5 grid: eigsh returns negative eigenvalue for W_sym (spectral radius computation gave -0.1013 via alpha_C * eigenvalue).

The Neumann series (I - αW_sym)^{-1} = Σ (αW_sym)^k converges iff the spectral radius ρ(αW_sym) = max|eigenvalue| < 1. The validation (params.py:107-108) checks α_C * spectral_radius_W_sym >= 1, but:
1. spectral_radius_W_sym is almost never provided (not computed by default)
2. If it were computed, it should be `abs(eigenvalue)`, not the raw signed eigenvalue

For default α_C = 0.1 and typical W_sym spectral radii ~1.0, the product α*ρ ≈ 0.1, so the series converges well. But there is no runtime guard. With α_C = 2.0 (tested), the series diverges silently and the resolvent diagonal returns values of 137-260 (should be near 1).

### **ISSUE-8 (LOW): Paper1 Open Problem 5 mis-attributes the Sep-energy bridge**

Paper1 line 845-846:
> "The exact bridge Sep_old = 1 - E_sep/m holds for the unweighted separation predicate"

This is backwards. The bridge Sep = 1 - E_sep/m holds for the **current u-weighted** formulation:
- E_sep = Σ u(1-D), Sep = Σ uD / Σ u
- E_sep = Σu - ΣuD = m - m·Sep, so Sep = 1 - E_sep/m. ✓

The "unweighted" (simple average of D over all nodes) does NOT satisfy this bridge. The naming "Sep_old" is also confusing — the u-weighted Sep is the newest version, not the oldest.

---

## NUMERICAL CONCERNS

### N1. Eigsh reliability for small Fiedler eigenvalues

graph.py:97-105 uses `eigsh(L, k=3, which="SM")` for the Fiedler eigenvalue. The `which="SM"` mode finds eigenvalues of smallest magnitude. For graph Laplacians with a known zero eigenvalue:

- **Works well** on connected graphs where λ₂ is well-separated from 0
- **Can fail** on nearly-disconnected graphs where λ₂ ≈ 0 (ARPACK struggles to distinguish near-zero eigenvalues)
- **Shift-invert** (`sigma=0, which="LM"`) would be more robust but requires handling the singular Laplacian

For the current experiments (regular grids), this is fine. For general graphs, it could silently return wrong Fiedler eigenvalues.

### N2. Semi-implicit scheme has no formal convergence guarantee

The operator-splitting scheme (explicit for reaction, implicit for diffusion + BB step size + Armijo backtracking) provides:
- Unconditional stability for the diffusion part ✓
- Adaptive step size via BB ✓
- Energy monotonicity (via rejection) approximately ✓ (only after iteration 5, line 125)

But:
- No convergence rate is proved or estimated
- The BB step can oscillate without damping
- The first 5 iterations always accept (even if energy increases), which can push the field far from the initial condition
- The stagnation exit (50-iteration energy window) can trigger before convergence

This is consistent with the observed non-convergence (BUG-2).

### N3. Energy evaluated at non-converged points affects all reported diagnostics

Since the optimizer never converges (BUG-2), all diagnostic scores in the papers are computed at non-critical points. The gradient norm at termination (~0.09) implies the field could potentially move to a significantly different (lower-energy) configuration. The reported diagnostics (Bind ≈ 0.87, Sep ≈ 0.89, Inside ≈ 0.90) may not reflect the actual energy minimizer's properties.

---

## REMAINING GAPS (from RE-AUDIT-1, still unaddressed)

1. **C_t orphaned (N1+D2):** C_t enters no predicate, no energy term. Three spec passages falsely claim it enters Sep.
2. **Q_morph formula inconsistency (S2+D1):** Normalized vs unnormalized across spec, papers, code.
3. **T7-Enhanced overstatement in spec (S1):** "Energy barriers" should be "Hessian eigenvalues."
4. **A1' theta_support undefined (S3):** No value specified anywhere.
5. **C3'' symmetrization gap (S4):** Documented but unresolved.
6. **beta_crit → 0 at scale (S5):** Phase transition trivially satisfied on large graphs.
7. **Paper2 Persist formula differs from spec/paper1 (S6):** Crisp vs soft formulas.
8. **Predicate-energy bridge one-directional (S7):** Low energy ⟹ high predicates, not converse.
9. **D5 Hessian ratio discrepancy:** λ_sep/λ_bd theoretical ~10^{-5} vs empirical ~1. Now we know the theoretical estimate is computed with BUG-1, so the 10^{-5} number is wrong.

---

## PRIORITY RANKING (All Issues)

1. **BUG-1: Hessian normalization factor-of-2 error** — Affects all experimental results. One-line fix.
2. **BUG-2: Optimizer never converges** — Every reported result is from a non-converged run. Needs investigation (convergence thresholds? projection bias? BB oscillation?).
3. **ISSUE-4: project_volume bias** — May contribute to BUG-2. Clean fix available.
4. **C_t orphaned (RE-AUDIT-1 N1+D2)** — Theoretical architecture claim is false.
5. **Q_morph inconsistency (RE-AUDIT-1 S2+D1)** — All files must agree.
6. **ISSUE-6: Figure caption contradicts theorem disclaimer** — Paper1 internal inconsistency.
7. **BUG-3: Hessian norm ignores λ₂ eigenvalue** — Edge case but mathematically wrong.
8. **ISSUE-5: Double gradient computation** — Performance (2x cost), not correctness.
9. **ISSUE-7: Resolvent divergence unguarded** — Only affects diagnostic computation.
10. **ISSUE-8: Open Problem 5 mis-attribution** — Terminology fix.
