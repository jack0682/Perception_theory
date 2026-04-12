# Relaxed Merge Global Path Condition

**Date:** 2026-04-10
**Session:** Cycle 23 — global relaxed merge path condition
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/proof/RELAXED-LOCAL-BASIN-BARRIER.md; docs/04-10/proof/RELAXED-MERGE-BARRIER-LOWER-BOUND.md

---

## 1. CURRENT GAP

**Target:** determine whether the embedded K=1 endpoint necessarily lies outside the local relaxed basin of a strict K=2 source branch.

The local theorem already proves:

```text
path leaves radius rho around B
=> max E_R >= E_R(B) + (mu_R/4) rho^2.
```

The remaining issue is whether every merge path from `B` to `T=Embed(u_merged)` must leave such a radius.

---

## 2. Basic Distance Bound

Let

```text
B = (u1_B, u2_B),
T = (u_merged, 0)
```

in the relaxed manifold `R_M^2`, with total mass `M` and second-formation mass

```text
m2 = sum_x u2_B(x).
```

Then for any choice of `u_merged`,

```text
||B - T||_2^2
  = ||u1_B - u_merged||_2^2 + ||u2_B||_2^2
  >= ||u2_B||_2^2.
```

Since `0 <= u2_B <= 1` and `sum_x u2_B = m2`, Cauchy-Schwarz gives

```text
||u2_B||_2 >= m2 / sqrt(n).
```

Therefore

```text
||B - T||_2 >= m2 / sqrt(n).
```

---

## 3. Sufficient Global-Path Condition

Let `rho_B` be any radius for which the local relaxed basin barrier theorem applies around `B`.

If

```text
rho_B < m2 / sqrt(n),
```

then the embedded K=1 target `T` is outside the radius-`rho_B` local neighborhood of `B`, regardless of the chosen `u_merged`.

Hence every continuous path from `B` to `T` must leave that neighborhood and must cross the local barrier:

```text
DeltaE_relax(B,T,P) >= (mu_R/4) rho_B^2
```

for any path class `P` that is continuous in the relaxed Euclidean topology and stays within the fixed-stratum/stratified-SOSC regime until radius `rho_B` is crossed.

---

## 4. Is Target-Outside-Basin a Theorem or Assumption?

It is **not automatic** from K=2 branch identity alone.

It becomes a theorem only after supplying:

1. a positive second-formation mass lower bound `m2 >= m_min > 0`,
2. a certified local basin radius `rho_B`,
3. the inequality `rho_B < m_min / sqrt(n)`,
4. relaxed local stability / stratified SOSC at `B`.

Without these, target-outside-local-basin is a **branch/path condition**, not a universal theorem.

---

## 5. Degenerate Failure Case

If `m2 -> 0`, then

```text
||B - T||_2 >= m2/sqrt(n) -> 0.
```

The embedded K=1 endpoint can approach the source arbitrarily closely. Thus no uniform target-outside-basin statement can hold across all relaxed K=2 branches.

This matches the no-universal-lower-bound degeneration already proved in `RELAXED-MERGE-BARRIER-LOWER-BOUND.md`.

---

## 6. Corrected Conditional Theorem

**Theorem (Conditional Global Relaxed Local-Barrier Lower Bound).**
Let `B=(u1_B,u2_B)` be a strict relaxed local minimizer of `E_R` on `R_M^2`, satisfying the stratified Hessian gap condition with `mu_R>0` on radius `rho_B`. Suppose the second formation mass satisfies

```text
m2 >= m_min > sqrt(n) rho_B.
```

Then every continuous relaxed merge path from `B` to an embedded K=1 target `(u_merged,0)` exits the local basin and satisfies

```text
max_t E_R(gamma(t)) >= E_R(B) + (mu_R/4) rho_B^2.
```

**Status:** PROVED UNDER EXPLICIT CONDITIONS.

---

## 7. Remaining Global Barrier Gap

The theorem gives a **local contribution** to the relaxed merge barrier. It does not prove that the global minimax barrier is larger than the local escape barrier, nor does it quantify what happens after the path exits the local basin.

The full global R4 problem remains:

- compute or bound the minimum-energy path after local escape;
- rule out low-energy dissolve/spread/reconcentrate routes or include them in the path class;
- connect the barrier to stochastic Kramers rates.

---

## 8. Next Trigger

Proceed to Kramers/noise-rate formulation for branch-state dynamics.

First move:

> Given a branch-conditioned barrier `DeltaE_branch`, specify the finite-dimensional overdamped Langevin model and state the Kramers-rate theorem assumptions needed before rates can be claimed.
