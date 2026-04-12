# Iteration 3 R7 — Algorithm Designer: D_t and Sep Computation

**Author:** Algorithm Designer | **Iteration:** 3, Round 7

## D_t Algorithm
σ(a_D · ((1+λ_D)·P_u − λ_D·P_1) − τ_D). One sparse mat-vec. O(|E|).

## D_t Jacobian
J_D = diag(σ'·a_D·(1+λ_D)) @ P. Sparse, same nnz as W. O(|E|) to construct.

## E_sep Gradient (THE CRITICAL FORMULA)
∇E_sep = (1-D) − J_Dᵀ·u
**Does NOT involve C_t.** O(|E|). One sparse transpose mat-vec.

## Sep_old = 1 − E_sep/m (EXACT EQUALITY)
Monitoring Sep is FREE — just read the energy term. Sep_new adds C_t info but costs extra.

## POSITION
- First implementation: monitor Sep_old (free) + periodic Sep_new (every 50-100 steps)
- b_D = 0 strongly recommended (analyticity + simpler Jacobian)
- C_t enters diagnostics only, NOT gradient flow
