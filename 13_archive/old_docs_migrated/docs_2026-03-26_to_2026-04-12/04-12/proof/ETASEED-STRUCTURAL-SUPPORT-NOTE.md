# eta_seed Structural Support Note

**Date:** 2026-04-12
**Session:** Cycle 119 — weakest useful structural support for the seeded-access floor
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ETASEED-VS-EPSRAW-REFINEMENT-DECISION.md; docs/04-12/proof/ASEED-LOWER-BOUND-TEMPLATE.md; docs/04-12/proof/STABLE-ENTRY-CRITERION.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Purpose

This note asks what the weakest useful structural support for a positive seeded-access floor `eta_seed` should be.

---

## 2. Candidate Support Shape

The most natural current structural support is:

```text
stable-entry-compatible seeded access to the target local neighborhood
=> eta_seed should be nontrivially positive.
```

This is the seeded-side analogue of the raw obstruction principle.

---

## 3. Why This Is the Right Starting Form

The seeded side is currently strongest where the theory already has positive local evidence:
- once the target family is approached correctly,
- return/capture is highly reliable,
- and the stable-entry event has already been defined as the theorem-facing version of meaningful access.

So `eta_seed` should first be tied to **stable-entry support**, not to a more ambitious global success claim.

---

## 4. Relation to Evidence

### Exp80 anchor

Exp80 and dense Exp80 provide the clearest positive-side prototype:
- perturbations around the target branch return with extremely high reliability.

### Stable-entry connection

Because the event side has already been strengthened, the seeded lower-bound route can now be read as:

```text
the seeded protocol has a nontrivially positive stable-entry floor
into U_B(lambda).
```

This is more informative than simply saying seeded access exists.

---

## 5. Safe Current Reading

The strongest current theorem-support reading is:

> seeded accessibility should be supported first by the structural fact that, once the seeded protocol reaches the local target neighborhood, stable-entry/capture is robust enough to justify a positive accessibility floor.

This is still not a theorem, but it is the right structural support principle for `eta_seed`.

---

## 6. What Remains Open

- how to quantify “nontrivially positive” in theorem-facing form;
- whether `eta_seed` should be tied directly to stable-entry probability or to a slightly weaker capture-compatible event;
- how to compare the size of `eta_seed` with the currently obstruction-controlled `eps_raw`.

---

## 7. Next Trigger

The next step should return to the direct gap and ask how the strengthened seeded floor and structured raw ceiling should be compared most cleanly.
