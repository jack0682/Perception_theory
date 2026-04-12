# B4 Beyond-Weyl Quantification Audit

**Date:** 2026-04-10
**Session:** Cycle 6 — Beyond-Weyl 33x quantification audit
**Category:** audit
**Status:** complete
**Depends on:** docs/04-02/proof/BEYOND-WEYL-SPECTRAL.md; Canonical Spec v2.1.md §13; docs/04-06/HONEST-RECOUNT.md

---

## 1. CURRENT GAP

**Canonical item:** B4 — Beyond-Weyl 33x quantification.

**Current category:** Category B.

The bundled claim has two different parts:

1. a structured perturbation formula / theorem schema;
2. a numerical improvement factor, “33x”.

These must not be assigned the same proof status.

---

## 2. Split Claim

| Component | Statement | Status |
|---|---|---|
| Structured perturbation form | Joint gap loss depends on overlap of soft modes with coupling/overlap region, not merely full-space Weyl norm | PROVED UNDER GAP/LOCALIZATION CONDITIONS |
| Improvement factor | well-separated 12x12 case gives `1 / omega_soft ≈ 33` | NUMERICAL / CONFIG-SPECIFIC |
| Universal “33x wider window” | same factor applies generally | FALSE UNIVERSALIZATION |

---

## 3. Correct Quantity

The real improvement factor is not the number `33`. It is

```text
I(B, geometry) = 1 / omega_soft(B, geometry)
```

where

```text
omega_soft = max_{j != k} || P_{O_jk} psi_k^soft ||^2.
```

Thus the structured bound should be written as an interval or function:

```text
mu_joint >= min_k mu_k
            - (K-1) lambda_rep omega_soft
            - higher_order(lambda_rep^2 / spectral_gap_2)
```

under a gap condition separating the soft mode from the next Hessian mode.

---

## 4. What Is Mathematically Solid

| Piece | Reason |
|---|---|
| Weyl bound | standard operator norm perturbation |
| branch-local Hessian setup | finite-dimensional symmetric Hessian on tangent space |
| Davis-Kahan / perturbative eigenvector control | standard if second eigen-gap condition holds |
| dependence on `omega_soft` | valid as first-order / controlled perturbative correction |
| BMD localization input | already treated as proved in project registry |

The theorem-level object is therefore:

> A structured, soft-mode-overlap-dependent perturbation bound under explicit spectral-gap and localization hypotheses.

---

## 5. What Remains Empirical

| Piece | Why empirical |
|---|---|
| `omega_soft ≈ 0.03` | measured / validated on limited grid and branch geometries |
| `33x` | reciprocal of the measured `0.03`; not a universal constant |
| extended coexistence window by exactly `33/(K-1)` | depends on graph, branch, overlap geometry, and soft-mode localization |

---

## 6. Corrected Theorem Schema

The honest theorem is:

> For a specified K-formation branch `B`, overlap geometry `O_jk`, soft Hessian modes `psi_k^soft`, and second-gap condition `lambda_rep << mu_2 - mu_1`, the joint Hessian gap admits a structured perturbation lower bound with loss proportional to `omega_soft(B,O)`. The coexistence-window improvement is `1/omega_soft(B,O)`, not a universal constant.

---

## 7. Decision for B4

| Claim | Decision |
|---|---|
| structured spectral perturbation formula | keep as theorem-level under explicit conditions |
| “33x” exact improvement | Category B empirical/config-specific |
| universal `33x` claim | reject |
| replacement | report `1/omega_soft` interval/function by branch/geometry |

---

## 8. Registry Delta

No Canonical Spec category change.

B4 remains Category B only because Canonical Spec bundles the theorem and the 33x quantification. If split later:

- structured bound could be registered as proved under conditions;
- numerical improvement factor remains empirical.

---

## 9. Next Trigger

Proceed to B2 — general-graph birth supercriticality beyond D4/simple eigenspaces.

First move:

> Identify whether the missing step is truly supercriticality on arbitrary degenerate eigenspaces, and determine whether a generic transversality theorem or a counterexample is more honest than a universal proof.
