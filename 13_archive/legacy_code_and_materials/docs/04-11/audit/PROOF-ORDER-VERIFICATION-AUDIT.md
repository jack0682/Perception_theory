# Proof-Order Verification Audit

**Date:** 2026-04-11
**Session:** Cycle 89+ — proof-feasible ordering and fresh evidence audit
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/LATEST-GAP-TABLE.md; docs/04-10/audit/THEOREM-STATUS-REGISTRY.md; docs/04-11/theory/BASIN-ACCESS-CONJECTURE-SUPPORT-LADDER.md; experiments/results/exp79_continuation_access_20x20_0.6_l05.json; experiments/results/exp80_local_basin_proxy_20x20_0.6_l05_dense.json; experiments/results/exp81_active_set_transition_proxy_20x20_0.6_l05.json; experiments/results/exp82_access_path_trajectory_20x20_0.6_l05.json

---

## 1. Verification Rule

Claims should be checked in the following order:

1. **Already-proved support lemmas / theorem-status registry facts**
2. **Conditional theorems whose hypotheses are explicit and non-removable**
3. **Numerically supported propositions with cross-config evidence**
4. **Open theorem targets that still lack search-neutral structure**

This ordering minimizes theorem inflation and keeps protocol dependence explicit.

---

## 2. Proof-Feasible Order

### Tier A — Safest to treat as proved now

- theorem-count/status facts in `THEOREM-STATUS-REGISTRY.md`
- R1-P local branch continuation on fixed active strata / KKT nondegeneracy
- zero-repulsion degeneracy support lemma
- positive-repulsion ordering inside a fixed candidate set / smooth nondegenerate branch family
- local/conditional relaxed-manifold support lemmas already marked proved in the registry

### Tier B — Proved only under explicit regime hypotheses

- C1–C5 persistence claims
- relaxed local escape / path-conditioned barrier statements
- branch-conditioned communication-height / Kramers schema notes

These should remain condition-tagged rather than upgraded.

### Tier C — Strong numerical support, not theorem status

- search-protocol dependence support proposition
- continuation-access support proposition
- basin-access geometry statement / conjecture ladder
- raw-access failure + local-basin robustness + early-corridor divergence evidence chain

### Tier D — Still open / not theorem-ready

- search-neutral selected-branch theorem
- protocol-invariant branch threshold scalar
- search-neutral basin-access theorem (ladder rung 4)
- branch-free merge-barrier theorem on the relaxed manifold
- general-graph birth supercriticality outside the currently handled cases

---

## 3. Fresh Quantitative Verification

### Exp79 — continuation access

Fresh JSON re-check:

- `20x20:0.6`, `lambda=0.5`
  - threshold `<= 4.0`: `0 / 16`
  - threshold `<= 5.0`: `7 / 16`
  - best raw branch: Type A candidate, energy `26.222776`
  - continued branch: Type B candidate, energy `17.930247`
- `15x15:0.6`, `lambda=0.5`
  - threshold `<= 4.0`: `1 / 16`
  - best raw branch: Type A candidate, energy `13.217750`
  - continued branch: Type B candidate, energy `13.186253`

Interpretation: strict family thresholds still show raw access failure.

### Exp80 — local basin proxy

Fresh JSON aggregation:

- base grid: sigma `0.01, 0.02, 0.05, 0.10` all `8 / 8`
- dense grid: sigma `0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20` all `12 / 12`

Interpretation: once entered, the tested Type B family is locally robust over the tested perturbation range.

### Exp81 — active-set transition proxy

Fresh JSON re-check:

- raw transition count: `30`
- seeded transition count: `12`
- raw final type: Type A candidate
- seeded final type: Type B candidate

Interpretation: raw and seeded runs traverse substantially different coarse path geometries.

### Exp82 — access-path trajectory

Fresh JSON re-check:

- earliest divergence iteration: `1`
- raw iter 1 `(E, R) = (91.490273, 29.103149)`
- seed iter 1 `(E, R) = (17.902276, 0.044707)`

Interpretation: the gap opens immediately; this is an entry/corridor problem, not a late-stage refinement issue.

---

## 4. Current Honest Reading

The strongest currently defensible theorem-adjacent story is:

```text
raw access is weak,
entered-basin local robustness is strong,
and raw/seeded trajectories diverge from the first logged step.
```

Therefore the leading interpretation remains:

```text
entry problem >> local stability problem.
```

---

## 5. Next Proof Lane

The next theorem-oriented move should not be another branch-free scalar claim.

Instead, priority should be:

1. keep branch-selection language protocol-tagged;
2. decide whether to strengthen ladder rung 3 with one broader support extension;
3. or outline explicit hypotheses for a search-neutral rung-4 basin-access theorem.

At current evidence quality, rung 4 still needs an explicit hypothesis outline before any theorem upgrade is honest.
