# VP-4 Basin Stratification Summary

**Date:** 2026-05-08  
**Experiment:** exp88_vp4_basin_stratification.py (direct evaluation)  
**Strategy:** 6 strategic λ-points, d-clustering (d_tol=0.15)  
**Attacks:** OP-OMS-002, OP-OMS-010  
**Elapsed:** 31.1s  

## Basin/Observer-Type Discovery Results

| Scene | N_types | Prop_BS1 | min_Δd | max_Δd |
|---|---|---|---|---|
| S3_grid6x6 | 2 | YES | 0.4012 | 0.4012 |
| S4_two_cliques | 2 | YES | 0.5206 | 0.5206 |

## Strategic Starting Points

| Label | λ_cl | λ_sep | λ_bd | λ_tr |
|---|---|---|---|---|
| P1_cl_dominant | 0.70 | 0.10 | 0.10 | 0.10 |
| P2_sep_dominant | 0.10 | 0.70 | 0.10 | 0.10 |
| P3_balanced | 0.25 | 0.25 | 0.25 | 0.25 |
| P4_cl_sep | 0.40 | 0.40 | 0.10 | 0.10 |
| P5_bd_dominant | 0.10 | 0.10 | 0.70 | 0.10 |
| P6_tr_dominant | 0.10 | 0.10 | 0.10 | 0.70 |

## VP-1 Constructive Evidence (anchor)

Prop BS1 is already PROVED constructively by VP-1 (exp86, 2026-05-07):
- λ_A = (0.60, 0.20, 0.20, 0.00) → K_core = 2 (cl-dominant: two-blob perceptual type)
- λ_B = (0.50, 0.30, 0.20, 0.00) → K_core = 1 (balanced: single-formation perceptual type)
- ||d_A - d_B|| = 0.071, D_T > 0.5 → distinct topological readouts on connected M_obs

VP-4 direct evaluation extends this by testing 6 λ-configurations on S3 and S4.

## OP-OMS-010(c) Classification

**Status:** COMPUTATIONALLY_SUPPORTED
**Prop BS1 (all scenes):** YES
**Max observer types found:** 2

## Interpretation

Multiple distinct observer perceptual types (d-vector clusters) are found across
strategic λ configurations on the tested scenes. This extends the constructive VP-1
proof with broader sampling of the observer parameter space.

The diversity of d-vectors across λ-orientations confirms that V_D^0 induces
a non-trivial stratification of M_obs into distinct observer types.

**Prop BS1 is COMPUTATIONALLY SUPPORTED (direct evaluation + VP-1 construction).**

Note: V_D^0 with d* = (1,1,1,0) may not be the optimal landscape choice — gradient
descent on V_D^0 converges slowly on S3 (36 nodes), suggesting a flat landscape.
The d-cluster diversity (not gradient convergence) is the primary BS1 evidence.