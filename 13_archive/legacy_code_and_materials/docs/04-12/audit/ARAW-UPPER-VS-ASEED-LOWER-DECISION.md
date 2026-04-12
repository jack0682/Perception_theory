# A_raw Upper vs A_seed Lower Decision

**Date:** 2026-04-12
**Session:** Cycle 112 — choose the first supporting route toward the direct protocol-gap bound
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/DIRECT-PROTOCOL-GAP-BOUND-TEMPLATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Options

### Option A — upper bound on `A_raw`

Meaning:

> first try to formalize that raw accessibility is small.

Pros:
- directly matches the strongest current raw-search evidence from Exp79;
- gives a clean obstruction statement on the difficult side of the gap;
- likely easier to state in theorem-facing form than a positive seeded lower bound.

Cons:
- only treats one side of the comparison;
- leaves the seeded advantage implicit.

### Option B — lower bound on `A_seed`

Meaning:

> first try to formalize that seeded accessibility is large.

Pros:
- aligns with the persistence/capture interpretation;
- pairs naturally with Exp80-style local success.

Cons:
- more exposed to the fact that seeded success is mediated by the already chosen target family;
- does not on its own explain why raw access is poor.

---

## 2. Decision

**Choose Option A first: upper bound on `A_raw`.**

Reason:

1. the direct gap is currently bottlenecked most clearly by the raw-access failure side;
2. Exp79 already gives the cleanest concrete evidence in the entire lane — raw entry is rare under strict neighborhood thresholds;
3. once a theorem-facing raw upper bound is articulated, the gap object has a firmer negative side and the seeded side can be added later as the positive complement.

---

## 3. Consequence

The next proof note should ask for the weakest useful upper-bound form on `A_raw`, not yet a final proof, but a theorem-facing inequality target of the form:

```text
A_raw(G, lambda; U_B) <= eps_raw(G, lambda; U_B)
```

where `eps_raw` is small in the regime of interest.

---

## 4. What Gets Deferred

The `A_seed` lower-bound route is **deferred, not rejected**.
It remains the natural next complement once the raw upper-bound side is more explicit.

---

## 5. Next Trigger

Write a compact proof note stating the weakest useful upper-bound template on `A_raw` for the fixed-protocol theorem lane.
