# Search-Aware Branch-Selection Statement

**Date:** 2026-04-11
**Session:** Cycle 66 — search-aware branch-selection reformulation
**Category:** theory
**Status:** active
**Depends on:** docs/04-11/experiment/EXP78-SEARCH-PROTOCOL-UPGRADE-20x20_c0.6.md; docs/04-11/experiment/EXP78-CROSS-CONFIG-15x15_c0.6.md; docs/04-11/experiment/EXP78-CROSS-CONFIG-10x10_c0.6.md

---

## 1. Problem

The phrase “selected branch” is currently too ambiguous. In the recent R1-Q experiments, at least three distinct objects have diverged:

1. **discovered branch set** from a raw multistart protocol,
2. **persistent branch** obtained by seeded/warm continuation,
3. **search-upgraded selected branch** obtained when the persistent branch is injected back into direct optimization.

A theorem or audit statement that uses “the selected branch” without naming which of these it means is therefore unsafe.

---

## 2. Proposed Vocabulary

For a fixed configuration `G`, repulsion parameter `lambda`, and search protocol `S`, define:

- `Disc_S(G, lambda)` = set of branches discovered by protocol `S`
- `Sel_S(G, lambda)` = lowest-energy branch inside `Disc_S(G, lambda)`
- `Pers_{seed}(G, lambda)` = branch obtained by seeded/warm continuation from a specified seed family

Then the experimental evidence now supports the following **search-aware support statement**:

> There exist configurations `G` and lambdas `lambda` such that `Sel_{raw}(G, lambda)` and `Sel_{upgrade}(G, lambda)` belong to different branch families, and `Sel_{upgrade}(G, lambda)` can have strictly lower energy than both `Sel_{raw}(G, lambda)` and `Pers_{seed}(G, lambda)`.

This is not yet a theorem of SCC; it is a numerical support statement and a wording constraint.

---

## 3. Consequence for R1-Q

R1-Q should no longer be framed as a single branch-threshold number unless the branch-selection rule is fixed.

The honest form is closer to:

- branch continuation / persistence question,
- branch selection under an explicit search protocol,
- and optimizer-reliability gap between protocols.

So future branch-threshold statements should be labeled one of:

- **branch-family persistence threshold**,
- **protocol-dependent selected-branch threshold**,
- **search-upgraded selected-branch threshold**.

---

## 4. Immediate Guardrail

Until search-protocol dependence is neutralized or formally bounded:

> never infer a canonical selected branch from raw multistart search alone.

That is now an explicit methodological guardrail, not just a cautionary aside.

---

## 5. Next Trigger

Use this vocabulary in the next R1-Q audit cycle and test whether the same protocol gap appears on one more nontrivial config or can be bounded analytically.
