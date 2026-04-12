# R1-Q Status Note — Protocol-Tagged

**Date:** 2026-04-11
**Session:** Cycle 68 — compact protocol-tagged R1-Q status note
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/audit/R1-Q-PROTOCOL-TAGGED-REFORMULATION.md; docs/04-10/audit/THEOREM-STATUS-REGISTRY.md; docs/04-10/audit/GAP-REGISTRY.md

---

## 1. Canonical Name

**R1-Q:** protocol-dependent K=2 branch-selection threshold / selected-branch inference gap.

---

## 2. What Is Proved / Supported / Open

### A. Proved under explicit conditions

- **R1-P local branch continuation:** local analytic continuation of nondegenerate KKT branches on fixed active strata.
- **zero-repulsion degeneracy support lemma:** equal-self-energy automorphic copies can remain degenerate at `lambda_rep=0`.
- **positive-repulsion overlap-selection support lemma:** within a fixed candidate set or smooth nondegenerate branch family, positive repulsion orders branches by the overlap term.

### B. Numerically supported

- seeded branch families can persist to positive `lambda_rep` and, in the hardest tested sentinel, up to `lambda_rep=1.0`;
- raw multistart search, seeded continuation, and injected-seed upgraded optimization can yield different selected branches;
- in multiple sentinels (`10x10:0.6`, `15x15:0.6`, `20x20:0.6`), upgraded search finds lower-energy Type B branches than raw catalog search.

### C. Structurally open

- a search-neutral selected-branch theorem;
- a protocol-invariant branch-threshold scalar;
- analytic control of the gap between `Sel_raw` and `Sel_upgrade`.

---

## 3. Required Vocabulary

For any future R1-Q statement, use:

- `Disc_S(G,p)` = branch set discovered by protocol `S`
- `Sel_S(G,p)` = lowest-energy branch inside `Disc_S(G,p)`
- `Pers_seed(G,p)` = seeded/warm continuation branch from a named family

Without these tags, “selected branch” is currently ambiguous and unsafe.

---

## 4. Current Honest Reading of R1-Q

R1-Q is **not** presently a single theorem gap about one scalar threshold. It is a three-part status object:

1. **persistence question** — does a branch family survive under continuation?
2. **protocol-dependent selection question** — which branch is selected under a named search protocol?
3. **search reliability gap** — how different can selected branches be across protocols?

The active obstruction is now primarily (3).

---

## 5. Guardrail

Until protocol dependence is neutralized or bounded:

> never infer a canonical selected branch from raw multistart search alone.

---

## 6. Decision Label

**R1-Q = OPEN-CONDITIONAL**

More specifically:

- **branch-family persistence threshold** — partially supported numerically,
- **protocol-dependent selected-branch threshold** — numerically unstable across search rules,
- **search-neutral selected-branch threshold** — open.

---

## 7. Next Trigger

Either:

1. push the protocol-tagged status into a more formal theorem-support proposition, or
2. seek analytic mechanisms that could explain why raw multistart search systematically misses lower-energy Type B branches.
