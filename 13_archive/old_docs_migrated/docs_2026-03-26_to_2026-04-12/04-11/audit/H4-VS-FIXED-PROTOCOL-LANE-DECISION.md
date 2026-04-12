# H4 vs Fixed-Protocol Lane Decision

**Date:** 2026-04-11
**Session:** Cycle 93 — choose the next theorem blocker lane
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/proof/RUNG-4-BASIN-ACCESS-THEOREM-CANDIDATE.md; docs/04-11/theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md; docs/04-11/proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md

---

## 1. Options

### Option A — H4 analytic-access lane

Meaning:

> seek an access-volume / entry-probability bound that would support a genuinely search-neutral basin-access theorem.

Pros:
- attacks the deepest open blocker directly;
- would be the cleanest route toward the original rung-4 target;
- could convert empirical rarity into a quantitative theorem ingredient.

Cons:
- currently has the weakest analytic foothold;
- needs a new access quantity, not just refinement of existing evidence;
- risks a long stall before producing any theorem-shaped artifact.

### Option B — fixed-protocol theorem lane

Meaning:

> weaken the goal from search-neutrality to a theorem candidate under one explicit raw-search rule or one explicit protocol pair.

Pros:
- is closer to the already established protocol-tagged vocabulary;
- uses existing evidence more directly;
- can produce a theorem-shaped statement sooner by sidestepping full H6 neutrality.

Cons:
- does not solve the full search-neutral rung-4 problem;
- produces a narrower theorem target;
- still leaves H4-style accessibility control for the future if stronger claims are desired.

---

## 2. Decision

**Choose Option B first: the fixed-protocol theorem lane.**

Reason:

1. the current evidence base is already organized around explicit protocol tags (`Sel_raw`, `Sel_upgrade`, `Pers_seed`);
2. H4 currently lacks a candidate analytic quantity, so pushing it immediately is likely to stall;
3. a fixed-protocol theorem candidate can turn existing protocol-dependence evidence into a sharper proof target without pretending that search-neutrality is already within reach.

---

## 3. Consequence

The next proof target should no longer aim first at:

```text
search-neutral basin-access separation.
```

Instead it should aim first at something narrower, such as:

```text
under a fixed raw-search rule S_raw and a fixed seeded protocol S_seed,
local persistence and protocol-level accessibility can be quantitatively contrasted
for a named branch family.
```

This is weaker than the rung-4 dream theorem, but much closer to the present evidence.

---

## 4. What Gets Deferred

The full H4 lane is **not rejected**.

It is deferred until one of the following appears:
- a credible access-volume quantity,
- a finite-step entry probability model,
- or a region-partition theorem strong enough to bound entry rarity.

Until then, H4 remains the long-range theorem blocker rather than the immediate next lane.

---

## 5. Guardrail

Choosing the fixed-protocol lane does **not** upgrade any result to theorem status today.
It only changes the next proof target to a more reachable one.

---

## 6. Next Trigger

Write a compact fixed-protocol theorem-candidate note using the current protocol-tagged vocabulary and specify exactly which quantities would need to be bounded under `S_raw` and `S_seed`.
