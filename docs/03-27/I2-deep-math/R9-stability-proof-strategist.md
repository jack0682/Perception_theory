# Gradient Flow and Stability — Proof Strategist Complete Proofs

**Author:** Proof Strategist
**Date:** 2026-03-27
**Iteration:** 2, Round 9

---

## THEOREMS PROVED

| # | Result | Status | Method |
|---|--------|--------|--------|
| T14a | Projected gradient flow well-posedness | **PROVED** | Picard-Lindelöf + viability |
| T14b | Energy descent along flow | **PROVED** | Moreau projection |
| T14c | Convergence to single critical point | **PROVED** | Łojasiewicz gradient inequality |
| T14d | Convergence rate (exponential for non-degenerate) | **PROVED** | Łojasiewicz exponent θ=1/2 |
| T6 | Stability of formation minimizers | **PROVED** | Hessian positive definite on T_Σ |
| T7 | Enhanced metastability vs Allen-Cahn | **PROVED** (qualitative) | Energy barrier comparison |
| T8 | Formation lifetime bound | **SKETCH** | Kramers' formula |

## KEY RESULTS

### Łojasiewicz Convergence
Real-analytic energy on compact convex Ω_m. Trajectory has finite arc length. Converges to single critical point. Rate: exponential (θ=1/2) at non-degenerate critical points.

### Stability Theorem (Theorem 6)
At formation minimizer û that is a closure fixed point with ‖J_Cl‖ < 1:
- H_bd: positive definite from Laplacian + double-well (interior/exterior sites)
- H_cl: positive definite from contraction (2(1-‖J‖)² > 0)
- H_sep: bounded, dominated by other terms for large β
- Combined: H_Σ positive definite when β > λ_sep·C_sep / (2λ_bd(1-n_b/n))

### Non-Idempotence Stability Payoff (QUANTIFIED)
λ_min(H_cl^non-idem) = 2(1-‖J_Cl‖)² > 0
λ_min(H_cl^idem) = 0 (zero eigenvalues in range of J_Cl)

Non-idempotent closure contributes curvature 2λ_cl(1-‖J‖)² that idempotent closure CANNOT.

### Enhanced Metastability (Theorem 7)
ΔE_SCC = ΔE_AC + λ_cl·ΔE_cl + λ_sep·ΔE_sep > ΔE_AC
Formations more metastable under SCC than pure Allen-Cahn.

### Blocker
Theorem 6 assumes û is a closure fixed point. Not automatically guaranteed — needs perturbation argument showing minimizers are approximate fixed points.
