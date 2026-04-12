# B2 General-Graph Birth Supercriticality Audit

**Date:** 2026-04-10
**Session:** Cycle 7 — general-graph birth supercriticality audit
**Category:** audit
**Status:** complete
**Depends on:** docs/04-02/proof/FORMATION-BIRTH-THEOREM.md; docs/04-04/FORMATION-BIRTH-GENERAL.md; Canonical Spec v2.1.md §13

---

## 1. CURRENT GAP

**Canonical item:** B2 — T-Birth-Parametric, general non-D4 graph supercriticality.

**Current category:** Category B.

The gap is not uniform formation existence. The gap is the local **supercriticality direction** of the bifurcating branch in general graphs, especially narrow-gap / non-D4 degenerate cases.

---

## 2. Split Claim

| Component | Status | Reason |
|---|---|---|
| instability threshold `beta_crit = 4 alpha lambda_2 / |W''(c)|` | PROVED | Hessian eigenvalue crossing / T8-Core |
| non-uniform minimizer exists for `beta > beta_crit` | PROVED | compactness + T8-Core |
| local branch exists when `lambda_2` simple | PROVED | Crandall-Rabinowitz |
| supercriticality on D4 / equivariant cases | PROVED | equivariant branching normal form with positive cubic coefficients |
| supercriticality on simple eigenvalue with sufficient spectral gap | PROVED UNDER EXPLICIT GAP CONDITION | Lyapunov-Schmidt cubic coefficient dominated by `W''''=24` under gap bound |
| narrow-gap non-D4 simple case | Category B / OPEN-CONDITIONAL | Lyapunov-Schmidt correction may dominate; sign not proved |
| arbitrary degenerate non-D4 eigenspace | Category B / structurally conditional | requires finite-dimensional normal-form coefficient analysis for the eigenspace representation |

---

## 3. Why the Universal Claim Is Too Strong

For a simple eigenvalue, the Lyapunov-Schmidt cubic coefficient has the form:

```text
g_sss = positive W'''' term - negative correction involving
        sum_k ( <v_2^2, v_k>^2 / (lambda_k - lambda_2) ).
```

When `lambda_3 - lambda_2` is small, the correction can be large. Existing proofs give positivity only under a spectral-gap condition. Without that condition, the sign is not controlled by current arguments.

For degenerate eigenspaces without a symmetry group such as D4, the reduced bifurcation equation is a finite-dimensional normal form. Its branch directions and stability depend on tensors of eigenvector products, not only on `lambda_2`.

Therefore a universal “all general graphs are locally supercritical by the same argument” is not justified.

---

## 4. Corrected Theorem Schema

The honest theorem is:

> Formation birth instability and non-uniform minimizer existence are universal above `beta_crit`. Local supercriticality is proved for D4/equivariant cases and for simple-eigenvalue graphs satisfying an explicit spectral-gap domination condition. In narrow-gap or non-D4 degenerate eigenspaces, local supercriticality is a finite-dimensional normal-form question and remains Category B unless its cubic/quartic coefficients are checked.

---

## 5. Decision for B2

| Claim | Decision |
|---|---|
| universal instability/existence | keep proved |
| D4 supercriticality | keep proved |
| generic simple-eigenvalue spectral-gap case | proved under explicit spectral gap |
| narrow-gap simple case | remains Category B |
| arbitrary non-D4 degenerate eigenspace | remains Category B / structurally normal-form dependent |
| empirical validation on diverse graphs | support only, not proof |

---

## 6. Registry Delta

No Canonical Spec category change.

B2 remains Category B because the official entry bundles all general graphs. If split later:

- existence/instability could be Category A;
- D4 and sufficient-gap supercriticality could be Category A/conditional-A;
- narrow-gap and arbitrary non-D4 degenerate cases remain Category B.

---

## 7. Next Trigger

Proceed to C1 — T-Persist-1(d), exact threshold preservation.

First move:

> Split exact threshold preservation from shifted-threshold preservation and decide whether `beta > 7 alpha` is a non-removable structural regime condition or merely an artifact of current proof constants.
