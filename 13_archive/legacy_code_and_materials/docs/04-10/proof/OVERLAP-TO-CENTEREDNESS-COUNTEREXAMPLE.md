# Overlap-Minimization Does Not Imply Centeredness

**Date:** 2026-04-10
**Session:** R1-G graph-geometric overlap-to-centeredness cycle
**Category:** proof
**Status:** complete
**Depends on:** POSITIVE-REPULSION-SELECTION.md; ZERO-REPULSION-BRANCH-DEGENERACY.md; docs/04-10/audit/NEXT-TRIGGER.md

---

## 1. Target Claim Tested

The next-trigger candidate was:

> On a square grid with equal masses and automorphic copies of a compact single-formation support, minimum-overlap feasible K=2 placements under positive repulsion are maximally separated. Determine whether “maximally separated” implies Type A/centered under the exp65 branch descriptor.

The intended use was to connect the positive-repulsion first-order selection lemma

```text
positive lambda_rep selects minimum <u_1,u_2>
```

to Type A / centered branch selection.

---

## 2. Counterexample Statement

Let `G` be an `L x L` square grid with `L` large enough to contain at least two disjoint automorphic copies of a compact support `S`. Let `u*` be a sharp or soft formation supported inside a small corner block `S` with values in `[0,1]` and mass `m`.

Assume `E_self` is invariant under the square-grid automorphism group `D4` and that all chosen copies avoid simplex-barrier violation.

Choose two K=2 placements:

1. **Opposite-corner pair:** `S_NW` and `S_SE`.
2. **Adjacent-corner pair:** `S_NW` and `S_NE`.

For sufficiently small supports, both pairs are disjoint:

```text
<u_NW, u_SE> = 0,
<u_NW, u_NE> = 0.
```

By automorphism invariance,

```text
E_self(u_NW)=E_self(u_NE)=E_self(u_SE)=E_self(u*).
```

Both pairs therefore have identical K=2 energy for every `lambda_rep >= 0`:

```text
E_2(u_NW,u_SE) = 2E_self(u*)
E_2(u_NW,u_NE) = 2E_self(u*)
```

because the repulsion term is zero for both and the simplex-barrier term is zero for both.

However, their branch descriptors differ:

- the opposite-corner pair has pair midpoint at the grid center;
- the adjacent-corner pair has pair midpoint on the top edge midpoint, hence off-center.

Thus overlap minimization does **not** imply centeredness.

---

## 3. Proof

All self-energy terms are equal by graph automorphism invariance. Both pairs have zero simplex-barrier violation by construction and zero overlap because the supports are disjoint. Hence all terms in `E_2` agree for the two placements.

The pair midpoint is geometric. Opposite corners average to the grid center. Adjacent top corners average to the top-edge midpoint. These midpoints are distinct. Therefore the two equal-energy, minimum-overlap placements have different centeredness labels.

This is a direct counterexample to any theorem of the form:

```text
minimum overlap => centered Type A
```

without extra tie-breaking assumptions.

---

## 4. Consequence

Positive repulsion alone selects **minimum overlap**, not centeredness. If multiple placements already have zero overlap, the first-order repulsion term is exhausted and cannot choose between them.

Centeredness can only be recovered by adding additional selection data, for example:

1. maximum graph distance / separation as a secondary tie-breaker;
2. boundary-distance or confinement penalty;
3. initialization / optimizer basin rule;
4. higher-order finite-beta deformation terms;
5. a canonical branch rule such as “choose minimum overlap, then maximum separation, then symmetry-balanced pair midpoint.”

---

## 5. Reformulated Honest Theorem

The valid theorem is:

> Positive repulsion selects minimum-overlap branches to first order. If the minimum-overlap set contains multiple geometrically distinct placements, centeredness is not determined by repulsion alone. A Type A/centered branch theorem requires an explicit secondary tie-breaker or graph-geometric selection rule.

This closes R1-G as **DISPROVED in universal centeredness form** and **REFORMULATED** as a minimum-overlap-plus-tie-breaker problem.

---

## 6. Downstream Impact

- `Lambda_coupling` and overlap alone cannot classify Type A vs Type B.
- `d_min*` formulas must include a separation or tie-breaker convention.
- merge-barrier / `F''` statements must specify the selected branch and tie-breaking rule.
- multi-formation persistence can use overlap for spectral coupling, but not for centered branch identity.
