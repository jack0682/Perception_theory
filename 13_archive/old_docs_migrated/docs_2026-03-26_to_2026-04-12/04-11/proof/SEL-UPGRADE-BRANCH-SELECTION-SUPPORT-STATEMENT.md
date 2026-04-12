# Sel_upgrade Branch-Selection Support Statement

**Date:** 2026-04-11
**Session:** Cycle 71 — protocol-fixed support statement under Sel_upgrade
**Category:** proof
**Status:** complete
**Depends on:** docs/04-11/audit/R1-Q-LANE-DECISION.md; docs/04-11/proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md; docs/04-11/theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md

---

## 1. Statement Type

This is a **protocol-fixed numerical-support statement**, not a search-neutral SCC theorem.

The protocol is:

- recover a branch family by seeded continuation,
- inject that branch as an initializer into direct optimization,
- define selection by the resulting upgraded optimization rule `Sel_upgrade`.

---

## 2. Support Statement

Under the explicit search rule `Sel_upgrade`, current SCC K=2 experiments support the following claim:

> In the tested sentinel configurations, `Sel_upgrade` consistently returns Type B branches with strictly lower energy than the branches selected by raw multistart search `Sel_raw` at representative positive repulsion values.

In symbols, for the tested `(G, lambda)` pairs,

```text
E(Sel_upgrade(G, lambda)) < E(Sel_raw(G, lambda)).
```

Moreover, in the tested cases the selected upgraded branch remains in the Type B family.

---

## 3. Evidence Scope

Supported sentinel set:

- `10x10:0.6` at `lambda = 0.1, 0.5, 1.0`
- `15x15:0.6` at `lambda = 0.1, 0.5, 1.0`
- `20x20:0.6` at `lambda = 0.1, 0.5, 1.0`

So this is a multi-config, multi-lambda support statement, but still a finite tested regime.

---

## 4. What Is Honestly Claimed

### Claimed

- `Sel_upgrade` is a materially different selection rule from `Sel_raw` in current evidence;
- under `Sel_upgrade`, Type B selection is numerically supported on the tested sentinel set;
- raw-search-selected branch type is not stable under search-rule improvement.

### Not claimed

- that `Sel_upgrade` is globally optimal in the true nonconvex SCC landscape;
- that all SCC configurations prefer Type B under positive repulsion;
- that the same conclusion holds outside the tested sentinel set.

---

## 5. Consequence for R1-Q

This gives the strongest current protocol-fixed support form of R1-Q:

- **protocol-fixed selected-branch statement under `Sel_upgrade`** — numerically supported;
- **search-neutral selected-branch theorem** — open;
- **raw-search-selected branch statement** — method dependent and not canonical.

So if a branch-selection result must be stated today, the honest version is:

> under the explicitly defined `Sel_upgrade` search rule, the tested sentinel configurations select Type B branches at the sampled positive repulsion values.

---

## 6. Next Trigger

Now that the protocol-fixed support lane is stabilized, the next deeper lane is analytic:

> investigate why `Sel_raw` misses the lower-energy Type B branches found by `Sel_upgrade`.
