# Proof Attempts

**Date:** 2026-04-10
**Session:** Cycle 1 proof attempts for R1
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/CURRENT-TARGET.md; docs/04-10/audit/METHOD-LEDGER.md

---

## Theorem R1-P — Local Analytic Branch Continuation

### Statement

Fix a finite connected graph G, K=2, masses m1,m2 in the spinodal admissible range, and SCC parameters satisfying the analytic regime (`b_D=0`, `a_cl<4`, fixed finite `lambda_bar`). Consider the K-field energy restricted to a fixed active set of the box constraints and simplex-penalty regions. Suppose `(u1*,u2*)` is a strict local KKT minimizer and the bordered reduced Hessian on the active tangent space is invertible, equivalently positive definite on feasible first-order directions.

Then there exists a neighborhood U of the parameter point `(lambda_rep, m1, m2, beta, ...)` and a unique local branch `(u1(p),u2(p))` of KKT critical points continuing `(u1*,u2*)`. On any fixed active-set stratum this branch is analytic in p. Its branch-local quantities, including center of mass, separation, branch energy, and `F''(M/2)` along mass-transfer epsilon, are well-defined and analytic until one of the following event boundaries occurs:

1. reduced Hessian degeneracy,
2. active-set or simplex-penalty-region change,
3. energy crossing with another local branch under the selected branch rule,
4. boundary escape from the relevant feasible stratum.

### Proof Sketch

1. On a fixed active set, box constraints reduce to a linear subspace/face with volume constraints. The feasible tangent space is finite-dimensional.
2. With `b_D=0` and fixed active penalty region, all SCC energy terms used by `EnergyComputer` are analytic functions of the free coordinates. The penalty `(u1+u2-1)_+^2` is analytic on each region where the active violation set is fixed.
3. The KKT equations consist of the projected gradient equations plus volume constraints and active-boundary equations. These form a finite-dimensional analytic map `F(z,p)=0`, where z includes free field coordinates and Lagrange multipliers.
4. The derivative `D_z F` is the bordered reduced Hessian/KKT matrix. By the nondegeneracy hypothesis it is invertible.
5. The analytic implicit function theorem gives a unique analytic branch `z(p)` locally.
6. Branch observables such as center of mass, separation, energy, and mass-transfer curvature are analytic compositions along this branch.
7. The proof cannot cross event boundaries where the active set changes, the KKT matrix loses invertibility, or selection changes to a different branch.

### Outcome

**REFORMULATED AND PROVED UNDER EXPLICIT CONDITIONS.** This closes the local branch-continuation part R1-P. It does not close the quantitative branch-selection threshold R1-Q.

---

## Disproof of the Universal Scalar Branch Claim

### Claim rejected

“Type A/B is determined solely by `(grid_size, c_ref)` or by a single default scalar regime classification.”

### Reason

The latest exp65 probe shows the same `20x20_c0.6` configuration changes branch classification when `lambda_rep` changes:

| lambda_rep | observed classification |
|---:|---|
| 10 | Type A candidate |
| 1 | Type A candidate |
| 0 | Type B candidate |

Because branch type depends on at least `lambda_rep` and selection path, no theorem may state Type A/B as a function only of `(grid_size,c_ref)`.

### Outcome

**FALSE UNIVERSALIZATION OF A BRANCH-SPECIFIC FACT.** This does not prove the exact threshold, but it invalidates the overly strong formulation.

## R1 Support Lemma — Zero-Repulsion Branch Degeneracy

**Statement.** If `E_self` is graph-automorphism invariant and `(g u*, h u*)` is simplex-barrier feasible for automorphic copies of a single-formation minimizer `u*`, then at `lambda_rep=0` all such pairs have equal K=2 energy `2E_self(u*)`.

**Status.** PROVED as a support lemma in `docs/04-10/proof/ZERO-REPULSION-BRANCH-DEGENERACY.md`. This is a structural obstruction to unique zero-repulsion branch selection without tie-breaking/history data.

## R1 Support Lemma — Positive-Repulsion First-Order Selection

**Statement.** Among zero-repulsion candidate branches with equal self-energy and zero simplex-barrier cost, fixed-candidate energy ordering for `lambda_rep>0` is exactly overlap ordering. Along any smooth non-degenerate local branch, the envelope derivative satisfies `F'(lambda_rep)=<u_1,u_2>`.

**Status.** PROVED as a support lemma in `docs/04-10/proof/POSITIVE-REPULSION-SELECTION.md`. This explains why positive repulsion can immediately break zero-repulsion degeneracy.

**Remaining step.** Prove or conditionally state a graph-geometric lemma connecting overlap minimization to Type A/centered branch selection on square grids.

## R1-G — Overlap-to-Centeredness Counterexample

**Target tested.** Minimum-overlap feasible K=2 placements under positive repulsion imply Type A / centered placement.

**Status.** DISPROVED in universal form and REFORMULATED. See `docs/04-10/proof/OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md`.

**Reason.** On a square grid, opposite-corner and adjacent-corner pairs of small automorphic supports can both have zero overlap and equal self-energy, but different pair midpoints. Positive repulsion cannot distinguish them because the overlap term is zero for both.

**Corrected theorem shape.** Positive repulsion selects minimum-overlap branches. Centeredness requires a secondary tie-breaker such as maximum separation, boundary-distance preference, initialization rule, or higher-order finite-beta correction.
