# B3 Branch-Conditioned d_min* Audit

**Date:** 2026-04-10
**Session:** Cycle 5 — B3 branch-conditioned critical-distance audit
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/B1-R4-BRANCH-CONDITIONED-MERGE.md; Canonical Spec v2.1.md §13; docs/04-06/HONEST-RECOUNT.md

---

## 1. CURRENT GAP

**Canonical item:** B3 — quantitative `d_min*` formula.

**Current category:** Category B.

Current formula in Canonical Spec v2.1:

```text
d_min* = 4.8 + 0.31 sqrt(beta/alpha) - 0.018 beta/alpha
```

with regression fit `R^2 = 0.987`.

---

## 2. Precise Meaning of d_min*

A branch-safe definition must specify:

```text
d_min*(B, rule, params, graph)
```

where:

| Argument | Meaning |
|---|---|
| `B` | selected K-formation branch / branch family |
| `rule` | tie-breaker or optimizer-selection convention |
| `params` | SCC parameters including closure, beta, alpha, lambda_rep, volume |
| `graph` | geometry and boundary conditions |

Without these, `d_min*` conflates different branch geometries.

---

## 3. What Remains Proved / Supported / Open

| Claim | Status | Reason |
|---|---|---|
| There is a qualitative critical-separation concept for K-formation metastability | PROVED UNDER REGIME DEFINITIONS | T-Persist-K-Sep/Weak use explicit separation/overlap hypotheses; local persistence requires support separation or bounded coupling. |
| Closure can reduce the effective separation needed for observed multi-formation persistence | NUMERICAL SUPPORT + PLAUSIBLE MECHANISM | exp57 SCC 10x10 vs AC 15x15 supports ~30%; mechanism via closure self-reinforcement and basin strengthening is plausible. |
| The specific regression formula with coefficients `4.8, 0.31, -0.018` | Category B / NUMERICAL SUPPORT ONLY | Least-squares fit; no coefficient-level derivation. |
| A universal branch-free `d_min*` scalar | FALSE UNIVERSALIZATION | R1 shows branch/tie-breaker geometry changes separation; overlap alone does not determine centered branch. |
| Branch-conditioned bounds of the form `d_min*(B,rule) in [lower, upper]` | OPEN | Requires branch descriptor and tie-breaker convention. |

---

## 4. Failure Mode of the Old Formula

The old formula treated `d_min*` as if it were determined only by parameters such as `beta/alpha`.

R1/B1 show that this is incomplete:

- branch source matters;
- tie-breaker matters;
- overlap minimization may leave multiple zero-overlap placements;
- centeredness and separation are not equivalent;
- merge/barrier endpoints depend on branch geometry.

Therefore the formula can remain useful only as an empirical fit for the tested branch-selection protocol.

---

## 5. Corrected Theorem Schema

The honest theorem form is:

> For a specified graph class, SCC parameter regime, K-formation branch family `B`, and branch-selection rule `rule`, there exists a branch-conditioned critical separation `d_min*(B,rule)` such that K-formation local persistence/metastability holds for separations above this threshold under the relevant Hessian/basin hypotheses.

A coefficient-level formula for `d_min*(B,rule)` is not proved unless derived from a branch-specific geometric/asymptotic model.

---

## 6. Decision for B3

| Component | Decision |
|---|---|
| qualitative separation threshold | keep as regime-level theorem/support concept |
| closure lowers observed threshold | keep as experimentally supported and mechanistically plausible |
| exact regression formula | remains Category B |
| universal branch-free scalar | reject |
| next proof target | branch-conditioned bounds after branch rule is fixed |

---

## 7. Registry Delta

No Canonical Spec category change.

B3 remains Category B with sharper wording:

> `d_min*` is branch-, rule-, graph-, and parameter-conditioned. Current coefficients are empirical and cannot be used as universal theorem constants.

---

## 8. Next Trigger

Proceed to B4 — Beyond-Weyl 33x quantification.

First move:

> Separate the rigorous structured spectral perturbation inequality from the empirical/grid-specific “33x” improvement factor. Determine whether the factor can be replaced with a branch/overlap-dependent interval.
