# Zero-Repulsion Branch Degeneracy Lemma

**Date:** 2026-04-10
**Session:** R1 branch-selection proof cycle
**Category:** proof
**Status:** active
**Depends on:** docs/04-10/audit/theorem-closing/SWEEP-ANALYSIS-R1.md; scc/multi.py K-field energy

---

## 1. Lemma Statement

Let `G=(V,E)` be a finite graph and let `E_self` be invariant under a graph automorphism group `Aut(G)`. Suppose `u* in Sigma_m` is a local minimizer of `E_self`, and suppose there exist automorphisms `g,h in Aut(G)` such that the pair `(g u*, h u*)` has zero simplex-barrier violation:

```text
((g u*) + (h u*) - 1)_+ = 0.
```

For the K=2 energy

```text
E_2(u_1,u_2; lambda_rep=0, lambda_bar)
  = E_self(u_1)+E_self(u_2)+lambda_bar ||(u_1+u_2-1)_+||_2^2,
```

every such pair `(g u*, h u*)` has the same K=2 energy `2 E_self(u*)`.

Consequently, at zero repulsion there is no unique branch selector among these automorphism-related, barrier-feasible branches unless additional tie-breaking, initialization, or history data is supplied.

## 2. Proof

Because `E_self` is invariant under graph automorphisms,

```text
E_self(g u*) = E_self(u*)
E_self(h u*) = E_self(u*).
```

Because the pair is simplex-barrier feasible,

```text
lambda_bar ||(g u* + h u* - 1)_+||_2^2 = 0.
```

Substituting into `E_2` at `lambda_rep=0` gives

```text
E_2(g u*, h u*; 0, lambda_bar) = 2 E_self(u*).
```

Thus all such feasible automorphism pairs are energy-degenerate. If two such pairs have different branch descriptors, for example different pair midpoint or orientation, then branch selection cannot be a function of the energy alone at `lambda_rep=0`. It must depend on tie-breaking, initialization, perturbation, or an added branch descriptor.

## 3. Scope

This proves a structural obstruction, not a complete classifier.

It applies when:

- graph automorphisms preserve `E_self`,
- multiple automorphic copies of a single-formation minimizer exist,
- at least two feasible K=2 placements avoid simplex-barrier violation,
- branch descriptors differ among those placements.

It does not prove that the optimizer will find all such branches.

## 4. Relation to exp65

The `20x20_c0.6` sweep shows Type B at `lambda_rep=0` and Type A for all positive tested `lambda_rep >= 0.05`. The lemma explains why zero repulsion is structurally special: the K-field energy loses a selection term and can admit degenerate branch placements.

## 5. Next Lemma Needed

A positive-repulsion perturbation lemma:

> Among a zero-repulsion degenerate family with equal self-energy and zero simplex-barrier violation, the first-order energy correction for small `lambda_rep>0` is `<u_1,u_2>`. Hence positive repulsion selects minimizers of overlap within that family. To convert this into centeredness, one must add graph-symmetry/geometric assumptions connecting overlap minimization to centered/well-separated placement.
