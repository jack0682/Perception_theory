# Iteration 3 R4 — Systems Engineer: Software Architecture

**Author:** Systems Engineer
**Date:** 2026-03-27
**Iteration:** 3 (Implementation), Round 4

---

## THREE-LAYER ARCHITECTURE

**Layer 1: Static Evaluation Engine** — pure function: field → operators → predicates → energy
**Layer 2: Within-Time Optimizer** — projected gradient flow on Ω_m (τ-dynamics)
**Layer 3: Between-Time Evolution** — transport + re-optimization (t-dynamics, PARTIALLY BLOCKED)

## SIX MODULES

1. **Graph Infrastructure**: sparse adjacency, Fiedler eigenvalue caching
2. **Operator Suite**: Cl_t (sigmoid), N_t (kernel), C_t (resolvent), D_t (sigmoid), T_t (STUB), M_{t→s} (softmax), R_θ (superlevel)
3. **Predicate Engine**: Bind(ℓ²), Sep(C_t-weighted), Inside(Q_morph), Persist(stub)
4. **Energy Engine**: 4-term with per-term gradients, Hessians, eigenvalue decomposition
5. **Constrained Optimizer**: projected GD on Σ_m, adaptive step, Łojasiewicz monitoring
6. **Analysis & Diagnostics**: Hessian eigendecomposition, phase diagrams, R10 verification

## PARAMETER MANAGEMENT

~25 parameters in 3 tiers:
- Tier 1: Theoretically constrained (a_cl < 4, β/α > threshold, etc.)
- Tier 2: Theoretically motivated defaults
- Tier 3: Empirically determined

Configuration object with validation, derived quantities, serialization.

## TESTING STRATEGY

- Property-based tests from ALL axioms (A1'-A4, B1-B4, C1-C5, D-Ax1-4, E1-E4, F1-F4)
- Regression against Iteration 2 results
- Finite-difference gradient verification (NON-NEGOTIABLE)
- Numerical stability at edge cases

## TECHNOLOGY

Python + NumPy/SciPy + giotto-tda + pytest. No frameworks. Mathematical transparency paramount.

## PRIORITIES

1. R10 verification infrastructure (URGENT)
2. Static evaluation + optimization pipeline
3. Phase diagram reproduction
4. Predicate-energy bridge data

## KEY RISKS

1. Parameter sensitivity (25+ params) → theoretical constraints reduce dimensionality
2. Self-referential gradient correctness → finite-difference checking
3. C_t resolvent cost → sparse iterative solvers
4. False confidence from computation → tag proof status
