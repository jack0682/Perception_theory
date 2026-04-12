# Direct Protocol-Gap Bound Template

**Date:** 2026-04-12
**Session:** Cycle 111 — weakest useful direct-gap inequality for the accessibility surrogate
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/ARAW-VS-ASEED-VS-GAP-DECISION.md; docs/04-12/proof/FINALIZED-FIXED-PROTOCOL-ASTAR-STATEMENT.md

---

## 1. Purpose

This note states the weakest useful theorem-facing inequality template for the fixed-protocol accessibility surrogate.

---

## 2. Gap Template

A safe current template is:

```text
A_seed(G, lambda; U_B) - A_raw(G, lambda; U_B) >= Delta_access(G, lambda; U_B),
```

where `Delta_access` is a positive comparison quantity capturing the protocol advantage.

At this stage, `Delta_access` is not yet a proved analytic lower bound. It is a theorem-facing placeholder that names the comparison the theory now wants to explain.

---

## 3. Why Direct Gap Is the Right Object

The current evidence supports an asymmetric picture:
- raw access is rare,
- seeded/localized access is much stronger,
- and the contrast matters more than either side alone.

So the direct gap is the smallest inequality form that preserves the actual meaning of the current continuation-access results.

---

## 4. Relation to Evidence

### Exp79 contribution

Exp79 pushes the raw side downward:

```text
A_raw is small on tested sentinels.
```

### Exp80 contribution

Exp80 supports the local success side underlying seeded access and post-entry stability.

### Combined reading

Together they motivate a positive gap:

```text
A_seed - A_raw > 0.
```

The theorem lane now asks how to make that positive gap structurally explicit.

---

## 5. Safe Current Reading

The strongest current theorem-support reading is:

> the fixed-protocol accessibility theory should aim to prove not just that raw access can be small or seeded access can be large, but that their difference is positively ordered in a structurally meaningful way.

This is still not a theorem, but it is the right next inequality target.

---

## 6. What Remains Open

- whether `Delta_access` should later be derived from one-sided bounds or introduced directly;
- how large a gap needs to be to count as theorem-useful;
- which structural assumptions should control the size of `Delta_access`.

---

## 7. Next Trigger

The next refinement should decide whether to derive `Delta_access` from:

1. an upper bound on `A_raw`, or
2. a lower bound on `A_seed`.
