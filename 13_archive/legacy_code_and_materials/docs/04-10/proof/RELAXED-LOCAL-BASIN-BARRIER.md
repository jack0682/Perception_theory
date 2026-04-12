# Relaxed Local Basin Barrier from Hessian Gap

**Date:** 2026-04-10
**Session:** Cycle 22 — relaxed local basin barrier theorem
**Category:** proof
**Status:** complete
**Depends on:** RELAXED-MERGE-BARRIER-LOWER-BOUND.md; docs/04-10/audit/R4-RELAXED-MERGE-MANIFOLD.md

---

## 1. CURRENT GAP

**Target:** conditional positive-barrier support theorem for R4.

The previous result showed that a universal positive relaxed merge barrier is false. A positive theorem requires the source branch `B` to be a strict local minimizer on the relaxed manifold `R_M^2`.

This document proves the local component:

> If `B` has a positive relaxed Hessian gap, then any path escaping a sufficiently small relaxed-neighborhood of `B` must cross a positive quadratic energy barrier.

---

## 2. Setup

Let `R_M^2` be the relaxed total-mass polytope. Let `B in R_M^2` be a KKT point lying on a fixed active stratum `S` of the polytope. Let `T_B S` denote the feasible tangent space of that stratum.

Assume:

1. `E_R` is `C^2` in a neighborhood of `B` within `S`.
2. `B` is a strict local minimizer on `S`.
3. The relaxed Hessian satisfies the gap condition

```text
v^T Hess_S(E_R)(B) v >= mu_R ||v||^2
```

for all `v in T_B S`, with `mu_R > 0`.

4. The Hessian is locally continuous, so for some radius `r0 > 0`,

```text
v^T Hess_S(E_R)(z) v >= (mu_R/2) ||v||^2
```

for all `z in S` with `||z-B|| <= r0`.

---

## 3. Theorem — Quadratic Local Basin Barrier

For any `0 < rho <= r0`, every continuous path

```text
gamma: [0,1] -> S
```

with

```text
gamma(0)=B,
||gamma(1)-B|| >= rho,
```

satisfies

```text
max_t E_R(gamma(t)) >= E_R(B) + (mu_R/4) rho^2.
```

Thus the local escape barrier from the radius-`rho` basin is at least `(mu_R/4) rho^2`.

---

## 4. Proof

By continuity of `gamma`, there exists `t_rho` such that

```text
||gamma(t_rho)-B|| = rho.
```

Let

```text
z = gamma(t_rho),
h = z - B.
```

Since `rho <= r0`, the segment `B + s h` for `s in [0,1]` remains inside the local neighborhood on the fixed stratum if the path class is restricted to that stratum or if `rho` is chosen inside one face chart.

Taylor's theorem with integral remainder gives

```text
E_R(B+h) - E_R(B)
  = dE_R(B)[h]
    + integral_0^1 (1-s) h^T Hess(E_R)(B+s h) h ds.
```

Because `B` is a KKT point and `h` is a feasible tangent displacement inside the stratum,

```text
dE_R(B)[h] = 0.
```

By the local Hessian lower bound,

```text
h^T Hess(E_R)(B+s h) h >= (mu_R/2) ||h||^2.
```

Therefore

```text
E_R(B+h)-E_R(B)
  >= integral_0^1 (1-s) (mu_R/2) ||h||^2 ds
  = (mu_R/4) ||h||^2
  = (mu_R/4) rho^2.
```

Since `z=gamma(t_rho)` lies on the path, the maximum energy along the path is at least this value. ∎

---

## 5. Boundary / Active-Set Caveat

`R_M^2` is a polytope with corners. If `B` lies on a boundary stratum, the theorem applies within a fixed active stratum or tangent cone chart. A path that changes active set must still cross the boundary of a sufficiently small stratified neighborhood; the same conclusion holds piecewise if the KKT second-order sufficient condition is uniform over the relevant tangent cones.

Therefore the cleanest theorem statement should say:

> positive local relaxed barrier holds under a stratified second-order sufficient condition on the relaxed feasible polytope.

---

## 6. Relation to Global Merge Barrier

This theorem proves only a **local escape barrier**. It does not prove that the entire path to `Embed(u_merged)` has a larger global minimax barrier. However, if the target lies outside the local radius `rho`, then any path from `B` to that target must first pay the local escape barrier.

Thus a global relaxed merge barrier lower bound can be decomposed as:

```text
DeltaE_relax >= local_escape_barrier
```

provided the source branch is a strict relaxed local minimizer and the target is outside the local basin radius.

---

## 7. Decision

| Claim | Outcome |
|---|---|
| local relaxed barrier from Hessian gap | PROVED under fixed-stratum / stratified SOSC hypotheses |
| global merge barrier lower bound | conditional on target outside basin and path class; still open globally |
| universal relaxed merge barrier | already rejected |

---

## 8. Next Trigger

Proceed to the global relaxed merge lower-bound problem:

> Determine whether every path from a strict relaxed local K=2 branch to the embedded K=1 target must leave the local basin. If yes, combine with this theorem for a positive lower bound; if no, identify endpoint choices where the target lies inside the same basin and the barrier is zero.
