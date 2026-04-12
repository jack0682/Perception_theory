# Q2 vs Q4 Lane Decision

**Date:** 2026-04-12
**Session:** Cycle 95 — choose the first quantitative blocker in the fixed-protocol theorem lane
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/FIXED-PROTOCOL-BASIN-ACCESS-THEOREM-CANDIDATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md

---

## 1. Options

### Option A — Q2 raw-entry upper bound

Goal:

> derive or propose a theorem-usable upper bound for how often `S_raw` enters the target neighborhood `U_B(lambda)`.

Pros:
- directly attacks the hardest remaining accessibility ingredient;
- turns Exp79-style rarity into a theorem-shaped object;
- would later help both fixed-protocol and search-neutral lanes.

Cons:
- analytically difficult;
- still needs a credible entry surrogate quantity;
- may stall if no usable bound candidate is found quickly.

### Option B — Q4 protocol-comparison gap

Goal:

> first formalize the gap between `S_raw` and `S_seed`/`S_up` as a protocol-comparison object.

Pros:
- more directly aligned with existing evidence;
- easier to phrase using already established protocol-tagged vocabulary;
- can produce a theorem-support statement before a full raw-entry bound exists.

Cons:
- depends on Q2/Q3-style quantities indirectly;
- comparison is still not a complete accessibility theorem by itself.

---

## 2. Decision

**Choose Option B first: Q4 protocol-comparison gap.**

Reason:

1. the current evidence is strongest at the level of protocol contrast, not at the level of a standalone raw-entry bound;
2. a protocol-comparison object can be stated immediately using `Sel_raw`, `Sel_upgrade`, `Pers_seed`, and the neighborhood language from the fixed-protocol candidate;
3. once Q4 is formalized, it becomes clearer what kind of Q2 surrogate would actually be useful.

---

## 3. Consequence

The next artifact should define a compact comparison statement of the form:

```text
under a fixed protocol pair (S_raw, S_seed),
the accessibility gap to U_B(lambda) is strictly ordered,
and this ordering coexists with strong local return once U_B(lambda) is reached.
```

This is not yet a theorem, but it is the sharpest next proof-facing object.

---

## 4. What Gets Deferred

Q2 is **deferred, not rejected**.

It should return once the protocol-comparison object has been stated cleanly enough to indicate which raw-entry quantity would actually matter:
- direct entry probability,
- coarse-region crossing probability,
- or another surrogate.

---

## 5. Next Trigger

Write a protocol-comparison note that introduces the fixed-protocol gap quantity explicitly and states the strongest current theorem-support claim that can be made about it.
