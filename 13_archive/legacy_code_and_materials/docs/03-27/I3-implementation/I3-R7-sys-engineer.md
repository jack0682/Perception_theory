# Iteration 3 R7 — Systems Engineer: Distinction and Sep Modules

**Author:** Systems Engineer | **Iteration:** 3, Round 7

## DistinctionOperator — Key Optimization
P_t(1-u) = P_1 - P_t(u). P_1 precomputed once. D_t requires only ONE sparse mat-vec.
With b_D=0: D_t(x) = σ(a_D·((1+λ_D)·P_u(x) - λ_D·P_1(x)) - τ_D). Cost: O(nnz) or O(n) if P_u shared.

Jacobian: J_D = diag(σ'·a_D·(1+λ_D)) @ A where A = normalized adjacency. Same sparsity as W.

## SepModule — Dual Variant
Sep_old: threshold-dependent, discontinuous. Sep_new: C_t-weighted, continuous. Both computed for A/B testing.

CRITICAL: E_sep ≠ Sep. E_sep = Σu(1-D) is the ENERGY (optimized). Sep_new = ΣC·D/ΣC is the PREDICATE (diagnostic). **C_t enters predicates but NOT energy gradient.**

## Complete code provided with:
- DistinctionOperator with intermediates + Jacobian
- SepModule (old + new)
- SepComparator for A/B testing
- Full axiom and continuity tests
