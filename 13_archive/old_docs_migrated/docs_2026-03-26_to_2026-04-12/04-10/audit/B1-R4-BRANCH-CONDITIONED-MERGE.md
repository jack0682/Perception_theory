# B1/R4 Branch-Conditioned F'' and Merge-Barrier Cleanup

**Date:** 2026-04-10
**Session:** Cycle 4 — branch-conditioned merge geometry cleanup
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/proof/OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md; docs/04-10/proof/POSITIVE-REPULSION-SELECTION.md; Canonical Spec v2.1.md §13 and §15

---

## 1. CURRENT GAP

**Canonical target:** B1 / R4 — barrier exponent and merge-barrier statements must be branch-conditioned.

**Current category:**

- B1 `gamma_eff ≈ 0.89`: Category B.
- R4 relaxed-manifold merge barrier: research extension / theorem-support blocker.

---

## 2. Exact Problem

Earlier work treated quantities such as

```text
F''(M/2), gamma_eff, merge barrier height
```

as if they were intrinsic scalars of `(grid_size, c_ref, beta, lambda_rep)`.

R1 showed this is unsafe. A K=2 configuration can lie on different local branches, and branch selection depends on repulsion, history, and tie-breakers.

The corrected problem is:

> Define `F''`, merge-barrier constants, and barrier exponents only after specifying a branch or a branch-selection rule.

---

## 3. Branch-Local Reduced Energy Theorem

Let `B` be a fixed smooth local K=2 branch parameterized by mass-transfer epsilon:

```text
z_B(epsilon) = (u_1^B(epsilon), u_2^B(epsilon))
```

with masses

```text
sum u_1^B(epsilon) = M/2 + epsilon,
sum u_2^B(epsilon) = M/2 - epsilon.
```

Assume the branch lies on a fixed active stratum and satisfies the nondegenerate KKT hypotheses from R1-P. Define

```text
F_B(epsilon) = E_2(z_B(epsilon)).
```

Then `F_B` is smooth/analytic locally and `F_B''(0)` is a well-defined **branch-local** curvature.

### Proof

This is an immediate application of the R1-P local branch-continuation theorem. The branch coordinates are analytic in epsilon on a fixed active stratum; the energy is analytic there; hence the composition `F_B(epsilon)` is analytic and has a well-defined second derivative.

**Status:** PROVED UNDER EXPLICIT BRANCH CONDITIONS.

---

## 4. Branch-Free F'' Is Not Well-Defined

If multiple local branches `B_i` exist, then the notation

```text
F''(M/2)
```

is ambiguous unless `F` is specified as one of:

1. a branch-local reduced energy `F_B`,
2. a global envelope `F_global(epsilon)=min_i F_{B_i}(epsilon)`,
3. an optimizer-selected trajectory-dependent curve,
4. a prescribed relaxed-manifold path energy.

These are different objects.

### Obstruction

- Branch-local curves can have different second derivatives at the same nominal mass.
- The global envelope can be non-smooth at energy crossings.
- Optimizer-selected curves can jump branches.
- Path energies depend on endpoint and path conventions.

Therefore a branch-free scalar `F''(M/2)` is a **false universalization**.

**Status:** DISPROVED in branch-free form.

---

## 5. Merge-Barrier Statement Cleanup

A merge barrier statement must specify all of the following:

| Required field | Reason |
|---|---|
| source branch | determines K=2 endpoint geometry |
| target manifold | constrained `Sigma^K_M` vs relaxed `Sigma_M^relax` differ |
| target endpoint | prior constrained merge endpoint was invalid |
| admissible path class | linear interpolation, geodesic, NEB, relaxed path give different barriers |
| branch-selection / tie-breaker rule | barrier constants depend on endpoint branch |
| asymptotic regime | finite-beta exponent fits are not constants |

Without these fields, “the merge barrier” is not a single mathematical object.

---

## 6. Corrected Theorem Form

The honest theorem schema is:

> For a specified K=2 branch `B`, specified relaxed or constrained target manifold `M_target`, and specified admissible path class `P(B,target)`, the branch-conditioned barrier is
>
> ```text
> Delta E_B = inf_{path in P(B,target)} max_t E(path(t)) - E(B).
> ```
>
> Any exponent or asymptotic constant attached to `Delta E_B` is branch/path/manifold conditioned. A scalar exponent such as `gamma_eff ≈ 0.89` is Category B unless its branch, path, and asymptotic regime are fixed and analytically derived.

---

## 7. Decision for B1

| Claim | Decision |
|---|---|
| positive barrier existence for a specified valid branch/path | may be theorem-level if path/endpoints valid |
| `gamma_eff ≈ 0.89` as universal exponent | reject; remains Category B empirical |
| branch-local `F_B''(0)` | proved well-defined under R1-P hypotheses |
| branch-free `F''(M/2)` | false universalization |
| merge barrier on original constrained `Sigma^K_M` to `(u_merged,0)` | invalid/retracted already |
| relaxed-manifold merge barrier | still open until endpoint/path class is specified |

---

## 8. Registry Delta

No Canonical Spec category changes.

B1 remains Category B, but its obstruction is now sharper:

> the fitted exponent is not merely empirical; it is branch/path/manifold conditioned.

R4 remains active as:

> define and analyze a valid relaxed-manifold, branch-conditioned merge barrier.

---

## 9. Next Trigger

Proceed to B3: branch-conditioned `d_min*` bounds.

First move:

> Rewrite `d_min*` as a branch- and tie-breaker-conditioned quantity. Determine which part is proved qualitatively (closure reduces critical distance) and which part is empirical (specific regression coefficients).
