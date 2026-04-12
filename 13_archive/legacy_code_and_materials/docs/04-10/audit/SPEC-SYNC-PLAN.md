# Canonical Spec Sync Plan — 04-10 Gap Campaign

**Date:** 2026-04-10
**Session:** Cycle 19 — non-editing spec synchronization plan
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/CAMPAIGN-SYNTHESIS.md; Canonical Spec v2.1.md

---

## 1. Rule

This is a plan only. Do not edit `Canonical Spec v2.1.md` until a dedicated spec-sync pass is approved/executed.

No theorem category count changes are proposed.

Current counts remain:

```text
35 Category A / 4 Category B / 5 Category C / 5 Retracted
```

---

## 2. Proposed Spec Locations

| Spec location | Current issue | Proposed sync |
|---|---|---|
| §12 / multi-formation architecture | branch selection not explicit enough | add note that branch identity is external data: selected local branch, tie-breaker, initialization/history |
| §12 / merge dynamics | old merge language can sound branch-free | define relaxed merge manifold `R_M^2` before any future relaxed merge theorem |
| §13 / B1 gamma_eff | exponent appears as scalar fit | state branch/path/manifold conditioning explicitly |
| §13 / B3 d_min formula | branch-free `d_min*` notation | replace with `d_min*(B, rule, params, graph)` in explanatory text |
| §13 / B4 Beyond-Weyl | theorem and 33x factor bundled | split structured bound from empirical `33x` factor in prose |
| §13 / C1/C2 persistence | exact threshold can sound all-core | distinguish shifted threshold, deep-core exact, all-core exact invalidity |
| §13 / C3-C5 K-persistence | Category C may read as proof weakness | label WS/WI/SR/PS/ND/etc. as regime/branch hypotheses |
| §15 closing summary | research extensions now sharper | mention branch-conditioned relaxed merge barrier and near-bif normal forms |

---

## 3. Specific Patch Sketches

### 3.1 Branch-selection note

Add near multi-formation regime discussion:

> K-formation statements are branch-conditioned. A branch is a selected local K-field minimizer together with its selection rule or history. Scalar quantities such as `F''(M/2)`, `d_min*`, and merge barriers are not branch-free invariants.

### 3.2 B1 wording

Replace scalar wording:

> `gamma_eff ≈ 0.89` is an empirical exponent.

with:

> `gamma_eff ≈ 0.89` is an empirical exponent for a specified branch/path/manifold protocol. The branch-local barrier may be defined only after source branch, target manifold, endpoint, and path class are fixed.

### 3.3 B3 wording

Replace:

```text
d_min*
```

with:

```text
d_min*(B, rule, params, graph)
```

where text permits, and clarify that coefficients remain empirical.

### 3.4 B4 wording

Add:

> The improvement factor is `1/omega_soft(B,O)`. The value `33x` is one measured configuration, not a universal constant.

### 3.5 Persistence wording

Add tiered statement:

> Shifted-threshold persistence is robust. Exact-threshold persistence is a deep-core theorem requiring positive interior gap. Boundary core sites and near-bifurcation regimes retain only shifted/remnant persistence.

### 3.6 Relaxed merge object

Add definition:

```text
R_M^2 = { (u1,u2): 0 <= u_k <= 1, sum_x(u1+u2)=M, u1+u2 <= 1 }.
```

and state that merge-barrier claims must use this or another explicitly valid relaxed manifold.

---

## 4. Files to Consult During Actual Patch

- `docs/04-10/audit/CAMPAIGN-SYNTHESIS.md`
- `docs/04-10/audit/B1-R4-BRANCH-CONDITIONED-MERGE.md`
- `docs/04-10/audit/B3-DMIN-BRANCH-CONDITIONED.md`
- `docs/04-10/audit/B4-BEYOND-WEYL-QUANTIFICATION.md`
- `docs/04-10/audit/C1-TPERSIST-EXACT-THRESHOLD.md`
- `docs/04-10/audit/C2-TPERSIST-FULL-COMPOSITION.md`
- `docs/04-10/proof/OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md`
- `docs/04-10/audit/R4-RELAXED-MERGE-MANIFOLD.md`

---

## 5. Next Trigger

If the next session is a spec-sync session:

1. edit `Canonical Spec v2.1.md` only in the locations above;
2. do not alter theorem counts;
3. add inline errata dated 2026-04-10;
4. update `CHANGELOG.md`;
5. run text consistency grep for `gamma_eff`, `d_min*`, `33x`, `F''`, `exact threshold`, and `merge barrier`.
