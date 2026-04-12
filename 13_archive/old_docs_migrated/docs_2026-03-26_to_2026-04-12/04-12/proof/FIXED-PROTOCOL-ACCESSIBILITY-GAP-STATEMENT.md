# Fixed-Protocol Accessibility-Gap Statement

**Date:** 2026-04-12
**Session:** Cycle 96 — protocol-gap quantity and theorem-support statement
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/Q2-VS-Q4-LANE-DECISION.md; docs/04-12/proof/FIXED-PROTOCOL-BASIN-ACCESS-THEOREM-CANDIDATE.md; docs/04-11/proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md

---

## 1. Purpose

This note introduces the fixed-protocol accessibility-gap object for the pair `(S_raw, S_seed)` and states the strongest current support claim that can be made without overstating theorem status.

---

## 2. Gap Quantity

Let `U_B(lambda)` denote a neighborhood capturing the target branch family `B(lambda)`.

Define the protocol-gap quantity

```text
Gap_{raw,seed}(G, lambda; U_B)
  := A_seed(G, lambda; U_B) - A_raw(G, lambda; U_B),
```

where:

- `A_raw(G, lambda; U_B)` is the accessibility quantity for the raw-search rule `S_raw`,
- `A_seed(G, lambda; U_B)` is the accessibility quantity for the seeded rule `S_seed`.

At the most abstract level, `A_*` may mean:
- entry probability into `U_B(lambda)`,
- return probability to `B(lambda)` after controlled perturbation,
- or another theorem-usable surrogate tied to basin capture.

---

## 3. Strongest Current Support Claim

The strongest currently honest statement is:

```text
For tested SCC K=2 sentinel configurations,
there exist protocol-tagged accessibility surrogates for which
Gap_{raw,seed}(G, lambda; U_B) > 0,
while local persistence inside U_B(lambda) remains strong.
```

This is still a **numerically supported statement**, not a theorem.

---

## 4. Evidence Mapping

### E1 — Raw accessibility is weak

Exp79 supports that raw access to the continued Type B neighborhood is rare on tested sentinels.

Interpretation:
- pushes `A_raw` downward.

### E2 — Local return is strong once near the target family

Exp80 / dense Exp80 support near-perfect return across the tested sigma ladder.

Interpretation:
- supplies a strong lower-bound surrogate for persistence inside `U_B(lambda)`.

### E3 — Seeded trajectories immediately occupy the right corridor

Exp82 shows seeded and raw trajectories diverge at the first logged iteration.

Interpretation:
- supports that `A_seed` is not merely slightly larger than `A_raw`, but belongs to a qualitatively different access regime.

### E4 — Protocol-selected outcomes differ across configs

The search-protocol dependence support proposition shows that protocol choice changes discovered/selected branch families across multiple sentinels.

Interpretation:
- justifies treating `Gap_{raw,seed}` as a meaningful protocol object rather than a one-off artifact.

---

## 5. What Is Already Strong vs Still Missing

### Strong now

- protocol-tagged language for comparing raw and seeded rules;
- numerical evidence that `A_seed` dominates `A_raw` in the tested continuation-access line;
- strong persistence evidence once entry occurs.

### Missing now

- a canonical definition of `A_raw` and `A_seed` suitable for theorem use;
- a proved inequality for `Gap_{raw,seed}`;
- a sharp neighborhood definition `U_B(lambda)` that is analytically portable;
- a theorem-level bridge from trajectory evidence to quantified accessibility comparison.

---

## 6. Safe Theorem-Support Reading

At present, the accessibility-gap line supports the following safe methodological conclusion:

> protocol choice changes accessibility to the target branch family in a way that is already numerically large enough to matter before local persistence even becomes the main issue.

This is stronger than a vague “optimization is sensitive” claim, but still below theorem level.

---

## 7. Next Trigger

The next artifact should choose which theorem-facing refinement is more feasible:

1. define a canonical theorem-usable surrogate for `A_raw`/`A_seed`, or
2. define the neighborhood `U_B(lambda)` more sharply so that the gap quantity becomes less ambiguous.
