# Iteration 3 R5 — Algorithm Designer: C_t Resolvent Efficient Computation

**Author:** Algorithm Designer
**Date:** 2026-03-27
**Iteration:** 3 (Implementation), Round 5

---

## THE PROBLEM

Resolvent C_t = (I - α_C W_sym)^{-1} is O(n³) naively. Changes every gradient step. Bottleneck.

## KEY FINDING: Neumann-Expressiveness Tension

- Cheap Neumann (K≤10) requires α_C·ρ < 0.5 → short-range co-belonging
- Expressive resolvent needs α_C·ρ close to 1 → long-range but expensive
- This is a FUNDAMENTAL trade-off, not a tuning issue

## RECOMMENDED STRATEGY (Tiered)

| n | α_C·ρ | Method | Cost |
|---|-------|--------|------|
| < 500 | Any | Dense inverse | O(n³) |
| 500-10K | Any | Sparse Cholesky | O(n^{3/2}) |
| 10K-100K | < 0.5 | Neumann K=10 | O(100|E|) |
| 10K-100K | > 0.5 | Hutchinson+CG m=30 | O(90|E|) |
| > 100K | Any | Hutchinson+CG m=30 | O(90|E|) |

## SEP GRADIENT: The Hard Part

∂Sep/∂u through C_t requires off-diagonal elements.
- **Approach A (frozen C_t):** Treat C_t as constant during gradient. Simple, O(|E|).
- **Approach C (adjoint):** One extra linear solve. Theoretically exact. Complex.
- **Recommend:** Start with A, upgrade to C if convergence issues.

## NEUMANN ACCURACY TABLE (α_C = 0.1, ρ = 4, α_C·ρ = 0.4)

| K | Error bound |
|---|-------------|
| 5 | 0.007 |
| 10 | 7×10⁻⁵ |

## LAZY CACHING

Recompute C_t only when ‖u^k - u^{k_last}‖₂ > ε_C. Expected 5-10× speedup.

## IMPLEMENTATION

Python class ResolventCt with backends: dense, cholesky, neumann, hutchinson. Auto-select based on n. Diagonal caching with staleness check.
