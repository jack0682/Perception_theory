# Kramers Route Decision: Fixed Active Stratum vs Reflected Polytope

**Date:** 2026-04-10
**Session:** Cycle 32 — Kramers route decision
**Category:** audit
**Status:** complete
**Depends on:** CONSTRAINED-LANGEVIN-KRAMERS-SCHEMA.md

---

## 1. CURRENT GAP

We need a theorem-safe route for stochastic transition rates in SCC branch dynamics.

Two possible routes:

1. fixed active stratum / smooth manifold route;
2. reflected diffusion on the full polytope with corners.

---

## 2. Comparison

| Route | Pros | Cons | Theorem risk |
|---|---|---|---|
| Fixed active stratum | smooth finite-dimensional manifold; classical Eyring-Kramers tools apply; tangent Hessians clear | ignores boundary hits; only valid if transition tube stays in stratum | low/moderate |
| Reflected polytope | faithful to box/simplex constraints | reflection at corners, local time, invariant measure, saddle on boundary all nontrivial | high |

---

## 3. Decision

Select **fixed active stratum** as the next theorem path.

Reason:

- It is the only route where a clean theorem schema can be stated immediately.
- It matches the project’s branch-conditioned philosophy: branch = selected local minimizer on a specified active stratum.
- Boundary/corner dynamics can be added later as a separate extension.
- Reflected-polytope Kramers theory is important but would require importing substantial stochastic-analysis machinery before any SCC-specific progress.

---

## 4. Fixed-Stratum Scope

The theorem should explicitly assume:

1. source branch and saddle lie in the same smooth active stratum or in a controlled smooth transition chart;
2. the dominant transition path does not hit polytope boundary/corners before reaching the saddle;
3. Hessian at source is positive definite on tangent space;
4. Hessian at saddle has exactly one negative tangent eigenvalue;
5. noise is tangent-projected with normalization `sqrt(2 epsilon)`.

---

## 5. Reflected-Polytope Status

Reflected-polytope rates are deferred as an advanced extension. Any future claim must specify:

- reflection cone,
- invariant measure,
- boundary saddle theory,
- corner compatibility,
- whether projection dynamics approximate reflection.

Until then, reflected-boundary Kramers statements are **not SCC theorems**.

---

## 6. Next Theorem Target

Create a fixed-stratum Eyring-Kramers schema theorem:

> On a finite-dimensional smooth active stratum, for overdamped Langevin dynamics with source local minimum and index-1 saddle, the branch transition rate has exponential scale `exp(-DeltaE/epsilon)`; prefactor is classical and can be cited rather than rederived.

This is a theorem-schema/citation target, not an original proof of Eyring-Kramers.

---

## 7. Next Trigger

Proceed to fixed-stratum Kramers theorem schema.

First move:

> Create `docs/04-10/audit/KRAMERS-FIXED-STRATUM-THEOREM.md` stating exact assumptions and rate formula, with status “theorem by classical citation under assumptions,” not newly proved SCC result.
