# dist_family vs Energy/Capture Decision

**Date:** 2026-04-12
**Session:** Cycle 99 — choose the first internal formalization step inside `U_B(lambda)`
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/UB-NEIGHBORHOOD-DEFINITION.md; docs/04-12/proof/FIXED-PROTOCOL-ACCESSIBILITY-GAP-STATEMENT.md

---

## 1. Options

### Option A — formalize `dist_family`

Meaning:

> try to turn the current family-distance convention into a theorem-facing branch-family metric first.

Pros:
- attacks the most obviously noncanonical ingredient directly;
- would sharpen branch identity language at the deepest level;
- could later stabilize neighborhood definitions across configs.

Cons:
- currently the most analytically underdeveloped part of `U_B(lambda)`;
- risks stalling on metric design before the theorem lane gets a usable capture statement;
- existing experiments support it numerically but not structurally.

### Option B — formalize the energy/capture criterion

Meaning:

> first isolate the theorem-facing role of energy tolerance and return/capture behavior inside the proposed neighborhood.

Pros:
- closer to canonical quantities already present in the energy framework;
- aligns directly with Exp80 return-to-family evidence;
- can sharpen the theorem lane without immediately solving the hardest branch-metric problem.

Cons:
- leaves `dist_family` provisional for longer;
- does not fully remove ambiguity about branch identity.

---

## 2. Decision

**Choose Option B first: formalize the energy/capture criterion.**

Reason:

1. the energy functional and return-to-family behavior are already native objects of the theory, while `dist_family` is still mainly a numerical convention;
2. a capture criterion can be made theorem-facing sooner by building on local persistence evidence;
3. once the capture side is stabilized, the remaining role of `dist_family` becomes narrower and easier to isolate.

---

## 3. Consequence

The next proof artifact should explain:

```text
what it means for a state to count as energetically admissible and capture-compatible
with the target branch family once it is near the neighborhood U_B(lambda).
```

This yields a cleaner theorem-facing local-basin statement even before the full branch-family metric is canonical.

---

## 4. What Gets Deferred

`dist_family` is **deferred, not abandoned**.

It should return once the energy/capture side is explicit enough to show exactly what geometric metric remains necessary.

---

## 5. Next Trigger

Write a short proof note formalizing the energy tolerance and capture criterion inside `U_B(lambda)` and explaining how Exp80 supports it numerically.
