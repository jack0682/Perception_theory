# Search-Protocol Dependence Support Proposition

**Date:** 2026-04-11
**Session:** Cycle 69 — compact support proposition for R1-Q3
**Category:** proof
**Status:** complete
**Depends on:** docs/04-11/audit/R1-Q-STATUS-NOTE-PROTOCOL-TAGGED.md; docs/04-11/theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md; docs/04-11/experiment/EXP78-SEARCH-PROTOCOL-UPGRADE-20x20_c0.6.md; docs/04-11/experiment/EXP78-CROSS-CONFIG-15x15_c0.6.md; docs/04-11/experiment/EXP78-CROSS-CONFIG-10x10_c0.6.md

---

## 1. Proposition (Numerical Support Only)

Let `S_raw` denote the raw multistart catalog-search protocol and `S_up` denote the upgraded direct-optimization protocol that injects a recovered continuation branch as an initializer.

Then, in the tested SCC K=2 branch-selection experiments, there exist configurations `G` and repulsion parameters `lambda` such that:

```text
Sel_{S_raw}(G, lambda) != Sel_{S_up}(G, lambda)
```

at the level of branch family / geometric type, and moreover

```text
E(Sel_{S_up}(G, lambda)) < E(Sel_{S_raw}(G, lambda)).
```

This statement is not a theorem of SCC. It is a **numerically supported proposition** extracted from the current audited experiments.

---

## 2. Evidence Instances

### Instance A — 20x20:0.6

At `lambda = 0.1, 0.5, 1.0`, the upgraded protocol returns lower-energy Type B branches than the raw-catalog winner.

### Instance B — 15x15:0.6

At `lambda = 0.1, 0.5, 1.0`, the upgraded protocol again returns lower-energy Type B branches than the raw-catalog Type A winner.

### Instance C — 10x10:0.6

At `lambda = 0.1, 0.5, 1.0`, the upgraded protocol again returns lower-energy Type B branches than the raw-catalog Type A winner.

So the proposition is supported on at least three nontrivial sentinel configurations.

---

## 3. What This Proposition Does and Does Not Say

### It does say

- selected-branch claims are protocol dependent in current evidence;
- raw multistart search is not a search-neutral oracle for branch selection;
- branch-threshold wording must carry an explicit protocol tag.

### It does not say

- that `S_up` is globally optimal;
- that the true SCC selected branch is always Type B;
- that a search-neutral branch-selection theorem is impossible.

---

## 4. Consequence for R1-Q

R1-Q must remain **OPEN-CONDITIONAL**.

The strongest honest upgrade from the current cycle is not a theorem closure, but the following methodological rule:

> Any selected-branch threshold statement in SCC must specify the search protocol used to define selection.

---

## 5. Next Trigger

Either seek analytic control on why `S_raw` misses lower-energy Type B branches, or formalize a protocol-dependent branch-selection theorem under a fixed search rule.
