# A_raw Upper-Bound Template

**Date:** 2026-04-12
**Session:** Cycle 112 — weakest useful upper-bound target for raw accessibility
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ARAW-UPPER-VS-ASEED-LOWER-DECISION.md; docs/04-12/proof/DIRECT-PROTOCOL-GAP-BOUND-TEMPLATE.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md

---

## 1. Purpose

This note states the weakest useful theorem-facing upper-bound target on `A_raw`.

---

## 2. Template

A safe current template is:

```text
A_raw(G, lambda; U_B) <= eps_raw(G, lambda; U_B),
```

where `eps_raw` is a small regime-dependent quantity measuring how rarely raw search reaches the target local neighborhood.

At this stage, `eps_raw` is not yet a proved analytic formula. It is the theorem-facing placeholder for the raw-access obstruction side.

---

## 3. Why This Is the Right First Supporting Route

The direct protocol gap needs at least one asymmetry component that is already close to explicit.
The raw side is the cleanest candidate because current evidence already says:

```text
strict-neighborhood raw access is very small.
```

This is exactly the kind of statement an upper bound is meant to encode.

---

## 4. Relation to Evidence

### Exp79 anchor

Exp79 is the main motivating example:
- under strict thresholds, raw hits are zero or near-zero in tested cases,
- even when looser thresholds give superficial near-misses.

So the theorem lane already has a concrete empirical prototype for a small `eps_raw`.

### Interpretive role

This upper bound formalizes the obstruction side of continuation-access:
- raw search does not reliably enter the target neighborhood.

---

## 5. Safe Current Reading

The strongest current theorem-support reading is:

> in the tested branch-selection regime, the raw protocol should be thought of as having a small accessibility upper bound to the target branch-family neighborhood.

This is not yet a proof, but it is a clean theorem-facing target.

---

## 6. What Remains Open

- what structural quantity should control `eps_raw`;
- whether `eps_raw` should depend on branch-distance threshold, energy tolerance, or both;
- how to combine the eventual raw upper bound with a complementary seeded lower bound to obtain the direct gap.

---

## 7. Next Trigger

The next refinement should decide whether `eps_raw` should first be tied to:

1. the branch-distance side of `U_B(lambda)`, or
2. the energy/capture side of `U_B(lambda)`.
