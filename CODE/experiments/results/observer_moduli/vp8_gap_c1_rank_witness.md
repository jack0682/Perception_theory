# VP-8 — Gap C1 Rank Witness Summary

**Date:** 2026-05-08  
**Experiment:** vp8_gap_c1_rank_witness.py  
**Attacks:** OP-OMS-001 Gap C1 (H4 witness), OP-OMS-024  
**Elapsed:** 48.8s  

## Method

Compute J_e = -G_T^T H_T^{-1} G_T at each λ, where:
- G ∈ R^{n×3} is the matrix of energy gradients `[grad_cl | grad_sep | grad_bd]` at u*(λ).
- P_T ∈ R^{n × (n-1)} is an orthonormal Householder basis of ker(1^T).
- G_T = P_T^T G (projects each gradient onto T).
- H_T = P_T^T H P_T where H is the FD Hessian of E_λ at u*(λ).
- J_e ∈ R^{3×3} is the energy-decomposition Jacobian (Theorem S1).
- J_e_tan = V J_e V^T ∈ R^{2×2} is the simplex-tangent Jacobian.

**H4 witness criterion:** rank(J_e_tan) = 2 AND |det of top 3×3 minor of G_T| > 1e-6.

## H4 witness statistics

- **Total evaluations:** 42
- **Full-rank witnesses:** 34/42 (81.0%)
- **H4 supported (≥1 witness):** YES

## Per-scene results

### P12_path

| label | branch | rank(G_T) | rank(J_e_tan) | σ_max | σ_min | cond(H_T) | |det 3×3 minor| | H_T PD |
|---|---|---|---|---|---|---|---|---|
| barycenter | (3, 4) | 3 | 2 | 3.3326e+01 | 1.3268e-01 | 1.15e+16 | 2.4350e-02 | NO |
| cl_dominant | (1, 4) | 3 | 2 | 4.1805e+00 | 3.0456e+00 | 4.25e+01 | 2.7983e-06 | YES |
| sep_dominant | (3, 4) | 3 | 2 | 1.5878e+00 | 4.3382e-01 | 5.03e+15 | 1.5038e-01 | NO |
| bd_dominant | (3, 4) | 3 | 2 | 9.6432e+01 | 2.6466e-02 | 3.55e+03 | 1.5899e-04 | YES |
| random_1 | (2, 4) | 3 | 2 | 2.6136e+00 | 1.2488e+00 | 3.50e+01 | 3.2320e-05 | YES |
| random_2 | (3, 4) | 3 | 2 | 5.1494e+02 | 6.4723e-02 | 1.50e+16 | 1.7666e-02 | NO |
| random_3 | (2, 4) | 3 | 2 | 2.3922e+00 | 1.1308e+00 | 3.18e+01 | 4.3186e-05 | YES |
| random_4 | (3, 4) | 3 | 2 | 4.9428e+00 | 3.8151e-01 | 5.45e+01 | 3.2483e-02 | YES |
| random_5 | (3, 4) | 3 | 2 | 3.0870e+00 | 2.1603e-01 | 9.35e+15 | 2.4171e-02 | NO |
| random_6 | (3, 4) | 3 | 2 | 2.9603e+00 | 2.5925e-01 | 9.39e+15 | 5.9731e-03 | NO |
| random_7 | (2, 4) | 3 | 2 | 1.9910e+00 | 4.6784e-01 | 3.00e+01 | 2.6314e-03 | YES |
| random_8 | (3, 4) | 3 | 2 | 2.3760e+00 | 1.6672e-01 | 1.03e+16 | 3.2091e-03 | NO |
| random_9 | (3, 4) | 3 | 2 | 1.0046e+00 | 9.0314e-01 | 7.01e+15 | 1.5797e-01 | NO |
| random_10 | (3, 4) | 3 | 2 | 1.4428e+00 | 1.4042e+00 | 4.07e+15 | 7.7693e-02 | NO |

### S3_grid6x6

| label | branch | rank(G_T) | rank(J_e_tan) | σ_max | σ_min | cond(H_T) | |det 3×3 minor| | H_T PD |
|---|---|---|---|---|---|---|---|---|
| barycenter | (6, 12) | 3 | 2 | 4.9852e+00 | 1.2719e+00 | 7.83e+00 | 8.4727e-07 | YES |
| cl_dominant | (0, 12) | 3 | 2 | 9.6208e+00 | 2.4595e+00 | 8.03e+15 | 1.5046e-05 | NO |
| sep_dominant | (7, 12) | 3 | 2 | 5.1402e+01 | 4.2052e+00 | 1.25e+01 | 1.1540e-02 | YES |
| bd_dominant | (6, 12) | 3 | 2 | 2.3207e+00 | 1.5086e-01 | 9.22e+00 | 2.8736e-05 | YES |
| random_1 | (0, 12) | 3 | 2 | 5.1982e+00 | 1.6069e+00 | 5.03e+01 | 8.5056e-08 | YES |
| random_2 | (6, 12) | 3 | 2 | 3.2510e+00 | 4.2733e-01 | 8.77e+00 | 1.9892e-05 | YES |
| random_3 | (0, 12) | 3 | 2 | 5.0458e+00 | 1.5513e+00 | 3.12e+01 | 6.7366e-06 | YES |
| random_4 | (4, 12) | 3 | 2 | 5.1530e+00 | 6.3211e-01 | 1.10e+01 | 1.4981e-04 | YES |
| random_5 | (7, 11) | 3 | 2 | 1.0690e+01 | 9.9832e-01 | 1.15e+01 | 5.2561e-02 | YES |
| random_6 | (7, 11) | 3 | 2 | 1.2586e+01 | 1.2787e+00 | 1.31e+01 | 1.1613e-01 | YES |
| random_7 | (2, 12) | 3 | 2 | 4.7789e+00 | 7.1117e-01 | 1.69e+01 | 7.8448e-05 | YES |
| random_8 | (7, 11) | 3 | 2 | 8.2458e+00 | 6.5944e-01 | 9.46e+00 | 8.4500e-02 | YES |
| random_9 | (7, 11) | 3 | 2 | 2.7893e+01 | 2.4124e+00 | 1.25e+01 | 1.0124e-01 | YES |
| random_10 | (7, 12) | 3 | 2 | 5.7357e+01 | 4.8279e+00 | 1.61e+01 | 1.6920e-03 | YES |

### asym_K4+tail

| label | branch | rank(G_T) | rank(J_e_tan) | σ_max | σ_min | cond(H_T) | |det 3×3 minor| | H_T PD |
|---|---|---|---|---|---|---|---|---|
| barycenter | (2, 2) | 3 | 2 | 1.5515e+00 | 1.5067e-02 | 1.58e+01 | 5.4428e-19 | YES |
| cl_dominant | (0, 2) | 3 | 2 | 2.7879e+00 | 1.3296e+00 | 1.24e+01 | 2.8582e-05 | YES |
| sep_dominant | (2, 2) | 3 | 2 | 5.1728e+00 | 4.9976e-01 | 1.66e+01 | 6.5799e-02 | YES |
| bd_dominant | (0, 3) | 3 | 2 | 2.3069e+00 | 3.6395e-02 | 1.02e+01 | 1.5627e-09 | YES |
| random_1 | (0, 3) | 3 | 2 | 8.0274e+00 | 6.8813e-02 | 1.08e+01 | 1.2341e-16 | YES |
| random_2 | (2, 2) | 3 | 2 | 1.3955e+00 | 1.8604e-02 | 2.01e+01 | 5.5279e-18 | YES |
| random_3 | (0, 3) | 3 | 2 | 7.7587e+00 | 6.1508e-02 | 1.07e+01 | 1.0439e-15 | YES |
| random_4 | (1, 2) | 3 | 2 | 2.3714e+00 | 3.0081e-01 | 1.72e+01 | 7.4706e-18 | YES |
| random_5 | (2, 2) | 3 | 2 | 1.5511e+00 | 5.5138e-02 | 1.56e+01 | 2.9174e-02 | YES |
| random_6 | (2, 2) | 3 | 2 | 1.6112e+00 | 9.1440e-02 | 1.57e+01 | 3.6843e-02 | YES |
| random_7 | (1, 2) | 3 | 2 | 2.5308e+00 | 4.2751e-01 | 1.74e+01 | 2.0306e-03 | YES |
| random_8 | (2, 2) | 3 | 2 | 1.4008e+00 | 3.2213e-02 | 1.64e+01 | 4.5254e-02 | YES |
| random_9 | (2, 2) | 3 | 2 | 3.1205e+00 | 3.2193e-01 | 1.08e+01 | 6.5799e-02 | YES |
| random_10 | (2, 2) | 3 | 2 | 4.0112e+00 | 6.4330e-01 | 2.19e+01 | 7.1749e-02 | YES |

## H4 explicit witnesses

Each witness below is a (scene, λ, |det 3×3 minor|) triple establishing H4 of `op_oms_001_gap_c1_genericity.md`:

- **P12_path** at `barycenter`, λ = [0.333, 0.333, 0.333], |det 3×3 minor of G_T| = 2.4350e-02.
- **P12_path** at `cl_dominant`, λ = [0.7, 0.15, 0.15], |det 3×3 minor of G_T| = 2.7983e-06.
- **P12_path** at `sep_dominant`, λ = [0.15, 0.7, 0.15], |det 3×3 minor of G_T| = 1.5038e-01.
- **P12_path** at `bd_dominant`, λ = [0.15, 0.15, 0.7], |det 3×3 minor of G_T| = 1.5899e-04.
- **P12_path** at `random_1`, λ = [0.631, 0.164, 0.205], |det 3×3 minor of G_T| = 3.2320e-05.

These witnesses establish H4. By Theorem G7 of `op_oms_001_gap_c1_genericity.md`, hypothesis H2 of the Rank Obstruction Theorem (RT1) holds on an open dense subset of (λ, X_t). Combined with RT3 + Corollary G8, OP-OMS-001 is closed conditional on H4 — and H4 is now confirmed.
