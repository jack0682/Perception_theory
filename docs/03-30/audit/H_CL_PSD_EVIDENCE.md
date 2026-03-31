# H_cl PSD at Energy Minimizers — Computational Evidence

**Date:** 2026-03-30

## Result: H_cl is PSD at ALL 24 tested minimizers

| Grid | β | c | min_eig(H_cl) |
|------|---|---|--------------|
| 5×5 | 10,20,50 | 0.3,0.5 | 2.00-2.01 |
| 7×7 | 10,20,50 | 0.3,0.5 | 1.93-1.96 |
| 10×10 | 10,20,50 | 0.3,0.5 | 1.98-1.98 |
| 15×15 | 10,20,50 | 0.3,0.5 | 1.98-1.99 |

**Zero violations across 24 configurations.**

## Interpretation

The minimum eigenvalue of H_cl at energy minimizers is consistently ~2.0 = 2·(1-0)² = γ_GN.

This means the residual correction R_cl has near-zero contribution to the spectral norm in practice. The rank-1 terms 2·r_i·σ''(z_i)·w_i·w_i^T nearly cancel each other due to:
1. Mixed signs in r_i (some sites have Cl(u) > u, others Cl(u) < u)
2. Mixed signs in σ''(z_i) (positive for z < 0, negative for z > 0)
3. The w_i vectors point in different directions

## Implication for T4

The current T4 statement is conditional on γ_GN - δ_res > (λ_sep/λ_cl)·δ_sep.

The computational evidence strongly suggests that this condition is ALWAYS satisfied in practice because:
1. H_cl is PSD (δ_res < γ_GN effectively, even though the BOUND δ_res >> γ_GN)
2. H_sep is PSD at tested minimizers (δ_sep = 0)

A stronger T4 could be stated: "H_cl is PSD at energy minimizers (computationally verified across 24 configurations). Conjecture: H_cl ≥ 2(1-a_cl/4)²I at all minimizers of the SCC energy."

## Open Problem

Prove analytically that R_cl has small spectral norm at energy minimizers. The worst-case bound (sum of rank-1 norms) is extremely loose (factor ~78x). A tighter bound exploiting sign cancellation would close T4 unconditionally.
