# eta_seed vs eps_raw Further-Refinement Decision

**Date:** 2026-04-12
**Session:** Cycle 119 — choose the next positivity refinement route
**Category:** audit
**Status:** complete
**Depends on:** docs/04-12/proof/EPSRAW-POSITIVITY-ROLE-NOTE.md; docs/04-12/proof/ASEED-LOWER-BOUND-TEMPLATE.md; docs/04-12/proof/EPSRAW-STRUCTURAL-CONTROL-NOTE.md

---

## 1. Options

### Option A — strengthen `eta_seed`

Meaning:

> sharpen the positive seeded-access floor so that the positivity condition gains an explicitly robust positive side.

Pros:
- balances the current development, which has already invested heavily in the raw obstruction side;
- aligns naturally with the stable-entry interpretation and Exp80 evidence;
- helps turn `eta_seed > eps_raw` into a genuinely two-sided theorem-facing comparison rather than a mostly one-sided obstruction story.

Cons:
- seeded positivity is less directly quantified than raw exclusion at present;
- may require careful interpretation so it does not collapse into mere local-return language.

### Option B — sharpen `eps_raw` further

Meaning:

> continue refining the raw obstruction side before investing more in the seeded floor.

Pros:
- follows the sharpest existing empirical inequality prototype;
- may make the negative side even cleaner.

Cons:
- risks over-developing one side of the comparison while leaving the positive side too weak;
- the direct gap will remain visually unbalanced if `eta_seed` stays schematic for too long.

---

## 2. Decision

**Choose Option A first: strengthen `eta_seed`.**

Reason:

1. the raw ceiling has already been sharpened through branch-distance exclusion, symbolic local-chart obstruction, and sampled/checkpointed exclusion;
2. the next real bottleneck for a persuasive positivity story is now the positive side — showing that seeded access is not just nonzero but structurally robust;
3. this keeps the theorem lane balanced and makes the eventual comparison `eta_seed > eps_raw` read as a true asymmetry rather than only a raw failure statement.

---

## 3. Consequence

The next proof note should ask what the weakest useful structural support for `eta_seed` is, beyond the current placeholder reading.

A natural first move is to tie `eta_seed` to the stable-entry side already suggested by Exp80 and the strengthened event definition.

---

## 4. What Gets Deferred

Further sharpening of `eps_raw` is **deferred, not rejected**.
It can return later if the positive side proves harder to stabilize than expected.

---

## 5. Next Trigger

Write a compact proof note stating the weakest useful structural support for a positive seeded-access floor `eta_seed`.
