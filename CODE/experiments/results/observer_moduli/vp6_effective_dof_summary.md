# VP-6 Effective DOF Summary

**Date:** 2026-05-08  
**Experiment:** vp6_effective_dof_jacobian.py  
**Attacks:** OP-OMS-016 (computational d_eff), OP-OMS-005 (effective DOF), Hypothesis RG1 (d_eff^typical(0.05) ∈ [2,4])  
**Elapsed:** 612.5s

## Method

Centered finite-difference Jacobian of the smooth components of P_top, sampled along the orthonormal tangent basis of the simplex.

Static face: 7-dim readout × 2-dim tangent → J ∈ R^{7×2}.
Full simplex: 8-dim readout × 3-dim tangent → J ∈ R^{8×3}.

## Per-scene singular spectra

### Scene: S3_grid6x6

**Variant:** `static`  (k_tangent=2)

| label | branch | σ values | d_eff(rel,5e-2) | branch_clean |
|---|---|---|---|---|
| P1_cl_dominant | (0, 12) | [2.2596, 0.1255] | 2 | YES |
| P2_sep_dominant | (10, 12) | [0.4658, 0.0081] | 1 | YES |
| P3_balanced | (6, 12) | [0.6112, 0.0581] | 2 | YES |
| P4_cl_sep | (6, 12) | [42.9820, 0.3226] | 1 | YES |
| P5_bd_dominant | (6, 12) | [0.4442, 0.0260] | 2 | YES |
| CE1_lambda_A | (2, 12) | [1.2611, 0.0907] | 2 | YES |
| CE1_lambda_B | (6, 12) | [0.7378, 0.0781] | 2 | YES |
| R1_random | (6, 12) | [0.7315, 0.0766] | 2 | YES |
| R2_random | (6, 12) | [0.1057, 0.0082] | 2 | YES |
| R3_random | (6, 12) | [0.5293, 0.0381] | 2 | YES |
| S_cl_eq_sep | (7, 11) | [0.2538, 0.0048] | 1 | YES |
| S_bd_face_near | (6, 12) | [0.4178, 0.0214] | 2 | YES |

**Variant:** `full`  (k_tangent=3)

| label | branch | σ values | d_eff(rel,5e-2) | branch_clean |
|---|---|---|---|---|
| P1_cl_dominant | (0, 8) | [3.6827, 0.0265, 0.0000] | 1 | YES |
| P2_sep_dominant | (10, 12) | [1.0677, 0.0106, 0.0000] | 1 | YES |
| P3_balanced | (6, 12) | [0.8146, 0.0773, 0.0000] | 2 | YES |
| P4_cl_sep | (6, 12) | [42.3320, 0.2087, 0.0000] | 1 | YES |
| P5_bd_dominant | (6, 12) | [0.4717, 0.0273, 0.0000] | 2 | YES |
| P6_tr_dominant | (6, 12) | [2.0363, 0.1928, 0.0003] | 2 | YES |
| CE1_lambda_A | (0, 12) | [2.2249, 0.1479, 0.0000] | 2 | YES |
| CE1_lambda_B | (6, 12) | [0.8952, 0.0973, 0.0000] | 2 | YES |
| S_cl_eq_sep | (7, 11) | [57.2733, 0.1282, 0.0121] | 1 | NO |

### Scene: S4_two_cliques

**Variant:** `static`  (k_tangent=2)

| label | branch | σ values | d_eff(rel,5e-2) | branch_clean |
|---|---|---|---|---|
| P1_cl_dominant | (0, 5) | [3.2410, 0.0009] | 1 | YES |
| P2_sep_dominant | (0, 5) | [0.0050, 0.0000] | 1 | YES |
| P3_balanced | (0, 5) | [0.0029, 0.0000] | 1 | YES |
| P4_cl_sep | (0, 5) | [0.0029, 0.0000] | 1 | YES |
| P5_bd_dominant | (0, 5) | [0.0029, 0.0000] | 1 | YES |
| CE1_lambda_A | (0, 5) | [2.1257, 0.0010] | 1 | YES |
| CE1_lambda_B | (0, 5) | [0.0024, 0.0000] | 1 | YES |
| R1_random | (0, 5) | [0.0024, 0.0000] | 1 | YES |
| R2_random | (0, 5) | [0.0040, 0.0000] | 1 | YES |
| R3_random | (0, 5) | [0.0026, 0.0000] | 1 | YES |
| S_cl_eq_sep | (0, 5) | [0.0027, 0.0000] | 1 | YES |
| S_bd_face_near | (0, 5) | [0.0029, 0.0000] | 1 | YES |

**Variant:** `full`  (k_tangent=3)

| label | branch | σ values | d_eff(rel,5e-2) | branch_clean |
|---|---|---|---|---|
| P1_cl_dominant | (0, 0) | [7.2031, 0.0007, 0.0000] | 1 | YES |
| P2_sep_dominant | (0, 5) | [0.0066, 0.0000, 0.0000] | 1 | YES |
| P3_balanced | (0, 5) | [0.0038, 0.0000, 0.0000] | 1 | YES |
| P4_cl_sep | (0, 5) | [0.0029, 0.0000, 0.0000] | 1 | YES |
| P5_bd_dominant | (0, 5) | [0.0033, 0.0000, 0.0000] | 1 | YES |
| P6_tr_dominant | (0, 5) | [0.0092, 0.0000, 0.0000] | 1 | YES |
| CE1_lambda_A | (0, 5) | [3.0742, 0.0012, 0.0000] | 1 | YES |
| CE1_lambda_B | (0, 5) | [0.0031, 0.0000, 0.0000] | 1 | YES |
| S_cl_eq_sep | (0, 5) | [0.0033, 0.0000, 0.0000] | 1 | YES |

## Aggregate d_eff(rel, 5e-2) histograms

- **static**: {1: 15, 2: 9}
- **full**: {1: 13, 2: 5}

## Sigma statistics

- σ_max average: 4.2215
- σ_max range: [0.0024, 57.2733]
- σ_min/σ_max average ratio: 0.0176

## Branch-cleanness

- Samples without branch jumps in any FD pair: 41 / 42

Branch-jumping samples cross a u*(λ) regularity boundary within the FD stencil. Their Jacobian is contaminated by a discrete component switch and over-states σ on the affected tangent direction. They corroborate OP-OMS-018 — global C^1 regularity of u*(λ) fails on these stencils.