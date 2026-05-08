# VP-6 Path Test — u*(λ) Regularity Summary

**Date:** 2026-05-08  
**Experiment:** vp6_u_star_regular_path_test.py  
**Paths:** 5 line segments × 2 scenes × 11 samples each  
**Elapsed:** 266.9s

## Per-scene path verdicts

### S3_grid6x6

| path | verdict | branch_jumps | AS_changes | max ||Δu||_∞ | max ||Δu||_2 |
|---|---|---|---|---|---|
| cl_axis | branch-switch detected | 5 | 4 | 0.852 | 3.226 |
| sep_axis | branch-switch detected | 5 | 7 | 1.000 | 4.367 |
| bd_axis | active-set change (R2 boundary) | 0 | 4 | 0.012 | 0.035 |
| CE1_pair | branch-switch detected | 2 | 1 | 0.951 | 4.077 |
| random | branch-switch detected | 6 | 5 | 1.000 | 4.267 |

### S4_two_cliques

| path | verdict | branch_jumps | AS_changes | max ||Δu||_∞ | max ||Δu||_2 |
|---|---|---|---|---|---|
| cl_axis | branch-switch detected | 1 | 1 | 0.602 | 1.897 |
| sep_axis | field jump (possible kink) | 0 | 0 | 0.602 | 1.897 |
| bd_axis | smooth branch (R1) | 0 | 0 | 0.000 | 0.000 |
| CE1_pair | field jump (possible kink) | 0 | 0 | 0.602 | 1.897 |
| random | active-set change (R2 boundary) | 0 | 1 | 0.031 | 0.096 |

## Interpretation

Following `op_oms_018_regular_u_star.md`:

- 'smooth branch (R1)' = no branch jump, no active-set change, no field jump → consistent with Theorem R1 (interior IFT branch).
- 'active-set change (R2 boundary)' = #{u_i ~= 0} or #{u_i ~= 1} changes along the path, but no branch jump → consistent with Theorem R2 piecewise C^1 across an active-set boundary.
- 'field jump (possible kink)' = ||Δu||_∞ > 0.3 between adjacent samples without a branch-id flip → suggestive of a non-smooth kink within a single branch.
- 'branch-switch detected' = K_core or n_high jumps → R3 (3) obstruction; the u*-correspondence is multi-valued at some λ_c on this path. Locates Σ_branch (OP-OMS-026).

## OP-OMS-018 status update

Combine path-test results with the proofs in `op_oms_018_regular_u_star.md`:

- Theorem R1 / R2 are PROVED (theory).
- Path test demonstrates which paths in Δ³ realize each regime computationally, distinguishing R1, R2, kink, and branch-switch.
- Branch switches in the path test = empirical realization of Σ_branch (OP-OMS-026).
