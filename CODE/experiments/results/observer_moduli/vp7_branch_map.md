> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# VP-7 Σ_branch Mapping Summary

**Date:** 2026-05-08  
**Experiment:** vp7_branch_map.py  
**Attack:** OP-OMS-026 (Σ_branch characterization), OP-OMS-024 (constant-rank regions)  
**Elapsed:** 79.1s

## Method

Triangular grid on the static face Δ² ⊂ Δ³ (λ_cl, λ_sep, λ_bd, λ_tr=0).
Per-point optimization with `find_formation` (n_restarts=2).
Branch identifier = (n_core, n_high). Edges connect adjacent grid points; Σ_branch is approximated by edges whose endpoints have different branch IDs.

## Per-scene results

### P12_path

- K = 10 → 66 grid points
- distinct branches: 7
- transition edges (Σ_branch crossings): 44

| branch (n_core, n_high) | count | fraction |
|---|---|---|
| (3, 4) | 44 | 66.67% |
| (2, 4) | 8 | 12.12% |
| (2, 3) | 4 | 6.06% |
| (0, 4) | 3 | 4.55% |
| (0, 3) | 3 | 4.55% |
| (1, 3) | 2 | 3.03% |
| (0, 0) | 2 | 3.03% |

### S3_grid6x6

- K = 8 → 45 grid points
- distinct branches: 17
- transition edges (Σ_branch crossings): 74

| branch (n_core, n_high) | count | fraction |
|---|---|---|
| (6, 11) | 9 | 20.00% |
| (7, 11) | 7 | 15.56% |
| (7, 12) | 6 | 13.33% |
| (8, 12) | 4 | 8.89% |
| (0, 0) | 3 | 6.67% |
| (4, 9) | 2 | 4.44% |
| (4, 8) | 2 | 4.44% |
| (5, 11) | 2 | 4.44% |
| (0, 8) | 2 | 4.44% |
| (5, 10) | 1 | 2.22% |
| (9, 12) | 1 | 2.22% |
| (8, 11) | 1 | 2.22% |
| (1, 8) | 1 | 2.22% |
| (3, 9) | 1 | 2.22% |
| (4, 11) | 1 | 2.22% |
| (0, 9) | 1 | 2.22% |
| (0, 12) | 1 | 2.22% |

## Interpretation

**Multiple branches** = multiple perceptual observer types coexist on the static face. Each branch corresponds to a distinct (n_core, n_high) signature of u*(λ).

**Transition edges** = approximate location of the codim-1 branch-switching surface Σ_branch.

**Constant-rank region candidates (OP-OMS-024):** Open subsets of the simplex on which all interior grid points share the same branch identifier. The largest such subset per scene is a candidate for a constant-rank region of J_R.
