# Continuation-Access Follow-up Decision

**Date:** 2026-04-11
**Session:** Cycle 78 — choose the strongest next continuation-access follow-up
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/audit/CONTINUATION-ACCESS-CONJECTURE-REGISTER.md

---

## 1. Candidate Follow-ups

### Option A — Basin-Size Proxy Scaling

Goal:

> map return probability versus perturbation size more finely around the continued branch.

Benefit:
- sharpens the local geometry of the basin already identified in Exp80.

Limitation:
- still stays on one configuration unless replicated later.

### Option B — Cross-Config Continuation-Access Replication

Goal:

> repeat the Exp79/Exp80 access-vs-local-basin pattern on another sentinel, such as `15x15:0.6`.

Benefit:
- directly tests whether the continuation-access conjecture generalizes beyond the current hardest sentinel.

Limitation:
- gives slightly less detailed local geometry on the original config.

---

## 2. Decision

**Choose Option B first: cross-config continuation-access replication.**

### Reason

1. the campaign already has one strong sentinel-level demonstration on `20x20:0.6`;
2. what matters most now is whether the conjecture generalizes at all;
3. if the same pattern appears on `15x15:0.6`, the conjecture becomes substantially stronger than a one-config phenomenon.

So the immediate next experiment should be:

> run Exp79-style continuation-access diagnostics on `15x15:0.6`, then decide whether Exp80-style local-basin proxy is also needed there.

---

## 3. Deferred Option

Basin-size proxy scaling remains valuable, but it should be the **second** continuation-access follow-up after cross-config replication.

---

## 4. Next Trigger

Run the continuation-access diagnostic on `15x15:0.6` at a representative lambda and compare the raw hit rate against the `20x20:0.6` baseline.
