# Core-Dissolution Lower Bound

**Date:** 2026-04-10
**Session:** Cycle 28 — event-specific lower bound for core-preserving relaxed merge paths
**Category:** proof
**Status:** complete
**Depends on:** docs/04-10/audit/RELAXED-MERGE-CORE-PRESERVING-PATHS.md

---

## 1. CURRENT GAP

For the restricted path class `P_core-preserving`, a merge path must eventually eliminate one formation core. We need a lower bound for the event:

```text
Core(t) = {x : u(t,x) >= theta}
```

loses core membership under a continuous path.

---

## 2. Minimal Crossing Lemma

Let `u(t,x)` be continuous in `t` for each site `x`. Suppose for some site `x0`,

```text
u(t0,x0) > theta,
u(t1,x0) < theta.
```

Then there exists `t* in (t0,t1)` such that

```text
u(t*,x0) = theta.
```

For the double-well term

```text
W(u)=u^2(1-u)^2,
```

the boundary/morphology energy at that instant contains at least

```text
beta W(theta)
```

from that site, before adding any graph-smoothness/interface contribution.

**Proof.** Intermediate value theorem gives `u(t*,x0)=theta`. At that time the double-well contribution of site `x0` is exactly `beta W(theta)`. Other energy terms are nonnegative in the standard SCC boundary/morphology energy. ∎

---

## 3. What This Does and Does Not Give

The lemma gives a **single-site crossing lower bound**:

```text
DeltaE_cross >= beta W(theta)
```

relative to a zero double-well reference at `u=0` or `u=1`.

For `theta=0.9`,

```text
W(0.9)=0.9^2 * 0.1^2 = 0.0081,
```

so the single-site double-well cost is

```text
0.0081 beta.
```

This is positive but small.

---

## 4. Why a Mass-Scaled Bound Does Not Follow Automatically

One might hope for

```text
m_core * beta W(theta)
```

but this is not automatic. A core can dissolve one site at a time. At each crossing time, only one site need be exactly at threshold, while the rest may remain near `0` or `1`.

Thus a mass-scaled lower bound requires an additional synchronization or density condition, such as:

1. at least `q` core sites cross threshold simultaneously;
2. a macroscopic fraction of core mass must pass through the spinodal interval at the same time;
3. interface length or core cardinality is constrained so one-by-one evaporation is impossible;
4. the path class forbids sequential peeling.

Without such conditions, the universal lower bound is only single-crossing scale.

---

## 5. Core-Cardinality Drop Bound

Let `N_core(t)=|{x:u(t,x)>=theta}|`. If `N_core` changes from at least `m_core` to less than `m_core` along a continuous path, then at the first time this happens at least one site is at threshold. Therefore the same lower bound applies:

```text
max_t E_bd(u(t)) >= beta W(theta)
```

above the ideal well contribution for at least one crossing site.

This does **not** scale with `m_core` unless multiple threshold crossings are forced to coincide.

---

## 6. Interface / Smoothness Add-On

If the crossing site has neighbors remaining near the core value `1` while it is at `theta`, the Laplacian part contributes an additional amount of order

```text
alpha * (# core-neighbors) * (1-theta)^2.
```

However this is geometry-dependent and can be reduced if the path peels boundary sites first or spreads the transition over a diffuse layer. Therefore the only branch-free contribution is the double-well crossing term.

---

## 7. Decision

| Claim | Outcome |
|---|---|
| at least one threshold crossing cost | PROVED: `beta W(theta)` |
| mass-scaled `m_core beta W(theta)` bound | FALSE without synchronization / no-peeling assumptions |
| geometry-enhanced smoothness bound | conditional on neighbor/core geometry |
| unrestricted core-dissolution barrier | small; may be much lower than direct interpolation barrier |

---

## 8. Implication for `P_core-preserving`

The core-preserving path class yields a positive event lower bound, but the universally provable bound is only single-site scale unless the path class is strengthened. This makes `P_core-preserving` useful for identity-event bookkeeping, but insufficient for strong macroscopic barrier estimates.

---

## 9. Next Trigger

Proceed to strengthen or reject mass-scaled core dissolution:

> Decide whether adding a no-peeling / simultaneous-core-loss condition is mathematically natural. If natural, prove a mass-scaled bound; if artificial, record that core-dissolution lower bounds are only single-site without further constraints.
