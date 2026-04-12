# Core Dissolution: No-Peeling / Simultaneous-Core-Loss Condition

**Date:** 2026-04-10
**Session:** Cycle 29 — no-peeling condition audit
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/proof/CORE-DISSOLUTION-LOWER-BOUND.md

---

## 1. CURRENT GAP

The prior theorem proved only a single-site crossing lower bound:

```text
beta W(theta)
```

for core dissolution. This cycle asks whether a stronger mass-scaled lower bound

```text
q beta W(theta)
```

or

```text
m_core beta W(theta)
```

can be obtained by adding a no-peeling / simultaneous-core-loss condition.

---

## 2. Natural vs Artificial Conditions

### Artificial strong condition

A condition like

```text
at least m_core sites cross theta at exactly the same time
```

is mathematically sufficient but dynamically artificial. Generic continuous paths will cross thresholds at distinct times after arbitrarily small perturbation of the path. Exact simultaneity is codimension-high and not stable.

### More natural condition

A more stable version is an interval / density condition:

```text
At some time t, at least q sites lie in [theta-delta, theta+delta].
```

This is robust under perturbation and expresses macroscopic dissolution rather than exact simultaneity.

---

## 3. Robust Band-Crossing Bound

Let

```text
A_q(t) = { x : u(t,x) in [theta-delta, theta+delta] }.
```

If for some `t*`,

```text
|A_q(t*)| >= q,
```

then the double-well contribution at that time is bounded below by

```text
beta q min_{s in [theta-delta, theta+delta]} W(s).
```

provided the interval lies inside `(0,1)`.

**Proof.** At time `t*`, each of the `q` sites contributes at least the minimum of `W` over the band. Summing gives the bound. ∎

---

## 4. Can q=m_core Be Forced Naturally?

Not generally.

A path can peel boundary/core sites sequentially so that only `O(|boundary|)` or even one site lies in the threshold band at a given time. To force `q` proportional to `m_core`, one needs an additional collective-motion condition, such as:

1. spatially coherent core dissolution,
2. bounded rate of interface motion plus bounded total event time,
3. no sequential peeling,
4. symmetry-constrained path,
5. path parameterization tied to a collective amplitude coordinate.

These are modeling restrictions, not consequences of relaxed continuity alone.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| exact simultaneous crossing of all core sites | artificial / nongeneric |
| band-crossing lower bound for `q` sites | PROVED |
| `q=m_core` forced by continuity | false |
| `q=O(|boundary|)` or `q=1` without stronger conditions | plausible minimal generic behavior |
| mass-scaled core-dissolution barrier | conditional on collective/no-peeling path restriction |

---

## 6. Corrected Theorem Schema

A meaningful theorem is:

> If a core-dissolution path has a macroscopic threshold-band occupancy `q` at some time, then the double-well energy cost is at least `beta q min_{band} W`. In unrestricted relaxed paths, `q` is not forced to scale with core mass; mass-scaled barriers require a collective-dissolution path class.

---

## 7. Implication for Merge Barrier

The strongest natural unrestricted lower bound remains local-basin escape plus single/band crossing. Strong macroscopic barriers require specifying a physical path mechanism that forces collective core dissolution.

---

## 8. Next Trigger

Proceed to campaign state checkpoint and decide whether to continue into a new proof target or prepare a commit/PR handoff.

First move:

> Refresh `CAMPAIGN-SYNTHESIS.md`, `HANDOFF.md`, and verification evidence with the no-peeling result.
