# T20 Axiom Consistency — Proof Strategist Full Analysis

**Author:** Proof Strategist
**Date:** 2026-03-27
**Iteration:** 2 (Deep Mathematical Development), Round 4

---

## Complete Parameter Admissibility Registry

### Group A: Sigmoid Closure

**A2 (Monotonicity): PROVED unconditionally.**
If u ≤ v pointwise, then P_t u ≤ P_t v (positive linear operator), so blend_u ≤ blend_v, so σ(a·(blend_u - τ)) ≤ σ(a·(blend_v - τ)). ∎

**A3 (Contraction): PROVED for a_cl < 4.**
Lipschitz constant L = a_cl/4 via chain rule: σ' ≤ 1/4, blend is affine in u with coefficient ≤ 1. Contraction rate geometric: ‖Cl^(n)(u) - u*‖ ≤ (a/4)^n · ‖Cl(u) - u‖. ∎

**A1 (Weak Extensivity): STRUCTURALLY IMPOSSIBLE for full range.**
At u(x) near 1, need σ(a·(z-τ)) ≥ u(x) → a → ∞. But a < 4 for A3.

**A1-Revised proposed:** Cl_t(u)(x) ≥ u(x) whenever u(x) ≤ c* where c* is the unique fixed point of c ↦ σ(a(c-τ)). For τ=0.3, a=3: c* ≈ 0.63.

**A4 (Continuity): TRIVIALLY SATISFIED** on finite X_t.

### THE A1-A3 INCOMPATIBILITY THEOREM

For the logistic sigmoid closure, A1 (full extensivity for all u(x) ∈ (0,1)) and A3 (strict contraction with a < 4) are logically incompatible. No parameter choice satisfies both. The resolution requires A1-Revised.

### Group D: Distinction Candidate

- D-Ax1 (Exterior Sensitivity): PROVED unconditionally
- D-Ax2 (Asymmetry): PROVED when λ_D ≥ 1, a_D > 0
- D-Ax3 (Boundary Sensitivity): PROVED when b_D > 0
- D-Ax4 (Continuity): TRIVIALLY SATISFIED

### Group E: Transport Candidate

- E1 (Sub-stochasticity): PROVED unconditionally (strict when ε > 0)
- E2 (Non-injectivity): PROVED (inherent in softmax)
- E3 (Core Inheritance): CONDITIONAL on correspondence quality
- E4 (Structural Sensitivity): PROVED when γ_M > 0

### Group C: Diffusion Co-belonging

- C1 (Dependence): PROVED by construction
- C2 (≠ Adjacency): PROVED via disconnected-region argument
- C3 (Monotone Reflexivity): PROVED for no-self-loop graphs (derivative explicitly ≥ 0)
- C4 (Convergence): PROVED for finite X_t (Cesàro average of finite Markov chain)

### Admissible Parameter Set

P_admissible = {a_cl ∈ (0,4), τ_cl ∈ (0, 1/2], η ∈ (0,1), ε > 0, a_D > 0, λ_D ≥ 1, b_D > 0, γ_M > 0, σ_M > 0}

with A1 replaced by A1-Revised.
