# Relaxed Merge: Saddle vs Communication Height

**Date:** 2026-04-10
**Session:** Cycle 34 — deterministic transition object for relaxed merge
**Category:** audit
**Status:** complete
**Depends on:** KRAMERS-FIXED-STRATUM-THEOREM.md; RELAXED-MERGE-MEP-AFTER-ESCAPE.md; RELAXED-MERGE-SUBLEVEL-SEPARATION.md

---

## 1. CURRENT GAP

Kramers-rate claims require a barrier `DeltaE` and usually an index-1 saddle. For relaxed merge, it is not yet clear whether such a saddle exists, because the relaxed feasible space has boundary/corners and the path class may admit diffuse shortcuts.

---

## 2. Communication Height Is Always Definable

For source branch `A`, target basin `Basin'`, and path class `P`, define the communication height:

```text
H(A,Basin';P) = inf_{gamma in P(A,Basin')} max_t E_R(gamma(t)).
```

Then the barrier height is

```text
DeltaE_comm = H(A,Basin';P) - E_R(A).
```

This object is well-defined whenever the path class is nonempty and the minimax infimum is finite.

---

## 3. Saddle Existence Is Stronger

An index-1 saddle representation requires additional hypotheses:

1. smooth active stratum or smooth manifold;
2. compactness / Palais-Smale-type condition for the path class;
3. communication height is attained;
4. minimax critical point is interior to the stratum, not on boundary/corner;
5. Hessian at critical point has exactly one negative direction;
6. no competing lower boundary escape.

Without these, `H` exists as a minimax value but may not be represented by a classical saddle.

---

## 4. Decision for Relaxed Merge

For current SCC relaxed merge theory:

| Object | Status |
|---|---|
| communication height | safe primary object |
| index-1 saddle | conditional / unproved |
| Kramers prefactor | unavailable until saddle exists |
| exponential scale via communication height | plausible large-deviation object, but needs stochastic theorem |

Thus the next deterministic object should be `DeltaE_comm`, not automatically `E(saddle)-E(source)`.

---

## 5. Corrected Kramers Input

For Kramers-style rates, use two tiers:

### Tier 1 — large-deviation scale

```text
rate exponential scale controlled by DeltaE_comm
```

if a Freidlin-Wentzell / large-deviation theorem is established for the chosen stochastic process.

### Tier 2 — Eyring-Kramers prefactor

```text
prefactor formula using Hessian determinant
```

only if `DeltaE_comm` is attained at a nondegenerate index-1 saddle in the fixed active stratum.

---

## 6. Registry Delta

Relaxed merge should use:

```text
communication height first,
saddle second if proved.
```

This avoids smuggling in saddle assumptions not yet established.

---

## 7. Next Trigger

Proceed to large-deviation communication-height schema.

First move:

> State a Freidlin-Wentzell-style theorem schema for fixed-stratum Langevin dynamics using communication height, without requiring a nondegenerate saddle/prefactor.
