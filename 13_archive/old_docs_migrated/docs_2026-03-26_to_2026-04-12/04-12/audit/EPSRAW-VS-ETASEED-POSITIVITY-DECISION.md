# eps_raw vs eta_seed Positivity Decision

**Date:** 2026-04-12
**Session:** Cycle 116 — choose the first positivity route for the direct protocol-gap lower bound
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/DELTA-ACCESS-COMBINATION-PATTERN.md; docs/04-12/proof/ARAW-UPPER-BOUND-TEMPLATE.md; docs/04-12/proof/ASEED-LOWER-BOUND-TEMPLATE.md

---

## 1. Options

### Option A — shrink `eps_raw` first

Meaning:

> focus first on making the raw-access ceiling as small as possible.

Pros:
- follows the sharpest existing evidence from Exp79;
- attacks the obstruction side directly;
- may be easier to formalize in theorem-facing language because the raw failure is already stark.

Cons:
- positivity would still remain incomplete without a decent seeded floor;
- can over-focus on absence rather than comparative advantage.

### Option B — strengthen `eta_seed` first

Meaning:

> focus first on making the seeded-access floor robustly positive.

Pros:
- aligns with the positive local-basin interpretation;
- fits the stable-entry strengthening already made on the event side.

Cons:
- seeded positivity can still look weaker if the raw ceiling is not simultaneously sharp;
- current strongest evidence still feels cleaner on the raw-failure side than on a quantified seeded floor.

---

## 2. Decision

**Choose Option A first: shrink `eps_raw` first.**

Reason:

1. Exp79 gives the single cleanest theorem-facing inequality prototype in the whole continuation-access line: strict raw access is zero or near-zero under strict thresholds;
2. a stronger raw obstruction immediately improves the direct gap lower bound by subtraction;
3. the seeded floor can remain as a positive complement, but the current bottleneck is that the obstruction side is easier to formalize than the positive side.

---

## 3. Consequence

The next refinement should deepen the raw obstruction side rather than the seeded floor side.

Concretely, the theorem lane should ask what is the **weakest useful structural control** making `eps_raw` small.

---

## 4. What Gets Deferred

Strengthening `eta_seed` is **deferred, not rejected**.
It remains the next natural complement after the raw ceiling has been sharpened enough.

---

## 5. Next Trigger

Write a compact proof note asking what the weakest useful structural control on `eps_raw` should be.
