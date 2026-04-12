# A_seed Lower-Bound Template

**Date:** 2026-04-12
**Session:** Cycle 114 — complementary lower-bound target for seeded accessibility
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/DIRECT-PROTOCOL-GAP-BOUND-TEMPLATE.md; docs/04-12/proof/STABLE-ENTRY-CRITERION.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Purpose

This note states the weakest useful theorem-facing lower-bound target on `A_seed`, as the natural complement to the raw upper-bound route.

---

## 2. Template

A safe current template is:

```text
A_seed(G, lambda; U_B) >= eta_seed(G, lambda; U_B),
```

where `eta_seed` is a positive regime-dependent quantity measuring how reliably the seeded protocol reaches or stably enters the target local neighborhood.

At this stage, `eta_seed` is not yet a proved analytic lower bound. It is the theorem-facing placeholder for the positive-access side.

---

## 3. Why This Complement Matters

The direct protocol-gap inequality ultimately needs both sides:
- raw accessibility small,
- seeded accessibility nontrivially positive.

Without the seeded lower-bound side, the direct gap remains only half-structured.

---

## 4. Relation to Evidence

### Exp80 anchor

Exp80 and dense Exp80 support the strongest current positive-side fact:
- once the target family is entered locally, return/capture is extremely reliable.

### Stable-entry connection

The event side has already been strengthened from first-hit to stable-entry.
So the seeded lower bound is most naturally read as:

```text
the seeded protocol has nontrivially positive probability of stable entry into U_B(lambda).
```

This is stronger than simply saying seeded trajectories “look better.”

---

## 5. Safe Current Reading

The strongest current theorem-support reading is:

> in the tested continuation-access regime, the seeded protocol should be thought of as having a positive lower accessibility floor to the target local neighborhood.

This is not yet a proof, but it is the right positive counterpart to the raw upper-bound route.

---

## 6. What Remains Open

- what structural quantity should control `eta_seed`;
- whether `eta_seed` should be read directly from stable-entry or via a capture-compatible local return quantity;
- how to combine `eta_seed` with `eps_raw` into a direct lower bound on `Delta_access`.

---

## 7. Next Trigger

The next step should compare the raw upper-bound and seeded lower-bound routes together and ask how they can be combined into a direct protocol-gap inequality.
