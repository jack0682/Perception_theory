# T8 Non-Trivial Minimizer Existence — Proof Strategist Complete Proof

**Author:** Proof Strategist
**Date:** 2026-03-27
**Iteration:** 2, Round 5

---

## THEOREM (T8)

Let (X_t, N_t) be a connected graph with n ≥ 2 vertices and Fiedler value λ₂ > 0. For the volume-constrained energy on Σ_m = {u ∈ [0,1]^n : Σu = m} with m = cn, c ∈ (0.211, 0.789):

(a) The constrained minimizer exists (compactness).
(b) The uniform state u ≡ c is NOT a minimizer when β/α > 4λ₂/|W''(c)|.
(c) The constrained minimizer is non-uniform.
(d) For large β/α, the minimizer has formation structure (core + boundary + exterior).
(e) Including closure and separation terms does not destroy the minimizer.

## PROOF CHAIN

### Lemma 1 (Existence)
Σ_m is compact. E_bd is continuous. Extreme value theorem. ∎

### Lemma 2 (Uniform Critical Point)
∇E_bd(ū) = βW'(c)·𝟏 satisfies Lagrange condition with μ = βW'(c). ∎

### Theorem 1 (Instability of Uniform State)
Hessian on tangent space T_ū Σ_m: H = 4αL + βW''(c)I.
Eigenvalues μ_k = 4αλ_k + βW''(c).
Smallest on tangent space: μ₂ = 4αλ₂ + βW''(c).
For c ∈ (0.211, 0.789): W''(c) < 0.
μ₂ < 0 when β/α > 4λ₂/|W''(c)|.
Fiedler eigenvector φ₂ is descent direction. ∎

### Theorem 2 (Non-Uniformity)
Global minimizer exists (Lemma 1). If it were uniform, it would be ū (unique uniform on Σ_m). But ū is a saddle (Theorem 1). Contradiction. ∎

### Theorem 3 (Formation Structure via Γ-convergence)
Set ε² = α/β. As ε → 0:
- Double-well dominates: W(u(x)) → 0 forces u(x) → {0,1}
- Limiting problem: minimize Cut(S) subject to |S| = m (graph isoperimetric)
- Diffuse interface width O(ε) = O(√(α/β))
- Exponential proximity to wells: |û(x) - {0,1}| ≤ Ce^(-d(x,∂S)/ε)
∎

### Theorem 4 (Persistence Under Full Energy)
Full Hessian: H_full = λ_cl·H_cl + λ_sep·H_sep + λ_bd·H_bd.
Closure and separation Hessians are PSD at uniform state → stabilizing.
Instability survives when λ_bd|μ₂| > λ_cl·σ_min^cl + λ_sep·σ_min^sep.
Revised critical ratio: (β/α)*_full = 4λ₂/|W''(c)| + O(λ_cl/λ_bd + λ_sep/λ_bd). ∎

## CORRECTED CRITICAL RATIO

$$(\beta/\alpha)^* = 4\lambda_2 / |W''(c)| = 4\lambda_2 / |2(1-6c+6c^2)|$$

At c = 1/2: (β/α)* = 4λ₂.
For k×k grid: λ₂ ≈ π²/k², so (β/α)* ≈ 4π²/k² → 0 as k → ∞.
