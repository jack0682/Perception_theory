# Relaxed Merge Core-Preserving Path Class

**Date:** 2026-04-10
**Session:** Cycle 27 — restricted core-preserving merge paths
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/RELAXED-MERGE-SUBLEVEL-SEPARATION.md; docs/04-10/proof/RELAXED-MERGE-MEP-AFTER-ESCAPE.md

---

## 1. CURRENT GAP

The unrestricted relaxed path class permits diffuse shortcut routes. We test whether a restricted path class can support a meaningful post-escape morphology lower bound.

Candidate class:

```text
P_core-preserving
```

paths where both formations retain a core above threshold until an explicitly declared transfer event.

---

## 2. Definition of P_core-preserving

A relaxed path

```text
gamma(t)=(u1(t),u2(t)) in R_M^2
```

belongs to `P_core-preserving(theta, m_core, t_transfer)` if for all `t < t_transfer`:

1. each component has a nonempty core,

```text
Core_k(t) = { x : u_k(t,x) >= theta }
```

2. each core has mass or cardinality at least `m_core`,
3. the two cores remain distinguishable, for example

```text
Core_1(t) ∩ Core_2(t) = empty
```

or overlap bounded by a specified tolerance,
4. mass transfer that eliminates `Core_2` is allowed only at `t_transfer`.

---

## 3. Lower-Bound Mechanism Inside This Class

Within this restricted class, a merge path must eventually destroy the second core or force core-core interaction. Therefore at least one of the following events occurs:

| Event | Cost mechanism |
|---|---|
| core dissolution | double-well / morphology cost to move core mass away from near-1 state |
| core overlap | repulsion / simplex / spinodal mixing cost |
| boundary expansion | increased interface / Laplacian boundary cost |
| discrete transfer event | non-continuous in branch identity; must be modeled as jump, not continuous MEP |

Thus a lower-bound theorem may be possible, but it is a theorem about this restricted path class, not the unrestricted relaxed MEP.

---

## 4. Artificiality Audit

`P_core-preserving` excludes the dissolve-spread-transfer-reconcentrate shortcut by definition. That makes it useful for studying **identity-preserving merge attempts**, but artificial for unrestricted physical coarsening.

Interpretation:

| Use | Verdict |
|---|---|
| proving a barrier for paths that preserve two identities until transfer | meaningful |
| estimating unrestricted MEP | too restrictive |
| modeling stochastic coarsening after identity dissolves | insufficient |
| formalizing “merge while both formations remain formations” | appropriate |

---

## 5. Conditional Theorem Schema

A valid theorem should say:

> In `P_core-preserving`, any continuous path from a two-core K=2 branch to a one-core K=1 endpoint must cross a morphology bottleneck where either the second core dissolves, the cores overlap, or interface length increases. If each event has a quantified lower bound `eta_event`, then the post-escape barrier is at least `min eta_event`.

This theorem is not yet proved because event-specific lower bounds must be derived.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| `P_core-preserving` definable | yes |
| lower-bound theorem in this class | plausible conditional theorem |
| relevance to unrestricted MEP | limited / artificial |
| use for identity-preserving merge | meaningful |
| use for stochastic coarsening | incomplete |

---

## 7. Next Trigger

Proceed to event-specific lower bounds for `P_core-preserving`.

First move:

> Derive a core-dissolution lower bound: how much boundary/double-well energy must be paid to reduce a core of mass at least `m_core` below threshold `theta` while staying continuous?
