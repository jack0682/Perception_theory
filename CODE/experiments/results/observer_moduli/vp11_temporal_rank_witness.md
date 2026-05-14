> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# VP-11 Phase 1 — Temporal Rank Witness Summary

**Date:** 2026-05-08  
**Experiment:** vp11_temporal_delta3.py (Phase 1)  
**Attack:** OP-OMS-034 — temporal rank witness (Wit-T)  
**Scene:** 6×6 grid, M_G Gaussian σ=1.5, u_1_fixed blob at (4, 4)  

## Method

Centered FD Jacobian of e_temp(λ) ∈ R^4 along Δ³ tangent basis v1=(1,-1,0,0)/√2, v2=(1,1,-2,0)/√6, v3=(1,1,1,-3)/√12. J_e_tan ∈ R^{4×3}. Pass criterion: rank 3 at ≥1 sample with λ_tr-nontrivial response.

## Headline numbers

- Total samples: 14
- **Full-rank witnesses (rank ≥ 3, abs σ ≥ 1e-3):** **14**
- Full-rank witnesses (rank ≥ 3, abs σ ≥ 1e-2): 10
- λ_tr-nontrivial witnesses: 14
- **(Wit-T) supported:** **True**

## Per-sample table

| label | branch | σ_1 | σ_2 | σ_3 | rank(abs 1e-3) | E_tr response | λ_tr nontrivial |
|---|---|---|---|---|---|---|---|
| barycenter | (6, 11) | 2.818e+00 | 8.335e-02 | 1.073e-02 | 3 | 6.744e-02 | YES |
| cl_dominant | (4, 9) | 6.747e+00 | 7.764e-01 | 7.615e-02 | 3 | -7.966e-02 | YES |
| sep_dominant | (7, 11) | 1.672e+02 | 1.456e+01 | 3.589e-02 | 3 | 1.525e+02 | YES |
| bd_dominant | (5, 11) | 1.847e+00 | 3.622e-02 | 3.556e-03 | 3 | 2.039e-02 | YES |
| tr_dominant | (8, 9) | 6.835e+00 | 1.081e+00 | 9.830e-03 | 3 | 1.587e-01 | YES |
| random_1 | (6, 11) | 3.049e+00 | 1.036e-01 | 2.418e-02 | 3 | 8.372e-02 | YES |
| random_2 | (6, 11) | 5.518e+00 | 2.429e-01 | 4.919e-02 | 3 | 1.411e-01 | YES |
| random_3 | (4, 9) | 5.303e+00 | 1.832e-01 | 1.714e-02 | 3 | -3.099e-02 | YES |
| random_4 | (6, 11) | 4.787e+00 | 4.701e-01 | 9.291e-02 | 3 | 1.483e-01 | YES |
| random_5 | (6, 11) | 1.978e+00 | 3.019e-02 | 7.710e-03 | 3 | 2.820e-02 | YES |
| random_6 | (6, 9) | 8.394e+00 | 7.736e-01 | 3.134e-02 | 3 | 7.289e-03 | YES |
| random_7 | (6, 11) | 3.028e+00 | 1.017e-01 | 1.900e-02 | 3 | 8.501e-02 | YES |
| random_8 | (6, 11) | 2.274e+00 | 4.182e-02 | 1.062e-02 | 3 | 4.858e-02 | YES |
| random_9 | (6, 11) | 2.086e+00 | 7.482e-02 | 7.757e-03 | 3 | 5.675e-02 | YES |

## Verdict

**(Wit-T) COMPUTATIONALLY CONFIRMED.** Temporal energy decomposition has full simplex-tangent rank 3 at ≥1 regular interior witness with non-trivial λ_tr response. Theorem T6 (rank-3 ⇒ rigidity) closure is rigorous on the static-temporal regular branch.