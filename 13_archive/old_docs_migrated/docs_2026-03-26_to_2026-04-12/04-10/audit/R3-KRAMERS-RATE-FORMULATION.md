# R3 Kramers-Rate Formulation for Branch-State Dynamics

**Date:** 2026-04-10
**Session:** Cycle 24 — Kramers/noise-rate formulation
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/RELAXED-MERGE-GLOBAL-PATH-CONDITION.md; docs/04-10/audit/R3-KINETIC-DYNAMICS-STATE.md

---

## 1. CURRENT GAP

**Target:** specify the stochastic model and assumptions required before Kramers-type branch transition rates can be claimed.

---

## 2. Required Stochastic Model

A theorem-level Kramers statement requires an explicit finite-dimensional constrained overdamped Langevin model, for example on a fixed active stratum `S`:

```text
dZ_t = - Proj_T grad E_R(Z_t) dt + sqrt(2 tau) Proj_T dW_t + reflection / projection terms at boundary.
```

where:

| Symbol | Meaning |
|---|---|
| `Z_t` | relaxed branch-state coordinate in `R_M^K` or a stratum chart |
| `E_R` | branch/path-conditioned relaxed energy |
| `tau` | noise temperature / variance scale |
| `Proj_T` | tangent projection enforcing mass/simplex constraints |
| boundary rule | reflection, projection, or absorbing transition convention |

Without specifying the boundary stochastic calculus, Kramers rates are physics analogies, not theorems.

---

## 3. Required Barrier Data

For a transition `S -> S'`, define:

```text
DeltaE(S,S') = E_R(z_saddle) - E_R(S)
```

where `z_saddle` is the relevant index-1 transition state or minimax saddle in the chosen path class.

Needed assumptions:

1. source branch is a strict local minimizer;
2. target/event basin is specified;
3. saddle exists and is nondegenerate in the stratum;
4. barrier is positive;
5. Hessian determinants / prefactors are finite after constraint projection;
6. boundary/corner effects are controlled.

---

## 4. Kramers Rate Schema

Under the assumptions above, the expected transition rate has the formal shape

```text
rate(S -> S') ≈ A(S,S') exp(-DeltaE(S,S') / tau)
```

or, depending on noise convention,

```text
rate(S -> S') ≈ A(S,S') exp(-DeltaE(S,S') / tau^2).
```

The project must fix the noise normalization before using either exponent.

---

## 5. What Is Theorem vs Analogy

| Claim | Status |
|---|---|
| branch-conditioned barrier must be specified before rates | theorem-level requirement |
| local basin barrier gives lower contribution to `DeltaE` | proved under SOSC conditions |
| Kramers exponential form | plausible / standard, but not yet proved for SCC constraints |
| prefactor formula | open |
| boundary-reflected constrained Langevin theory | open |
| stochastic birth/death event graph | open |

---

## 6. Corrected Research Target

R3 should state:

> Given a finite-dimensional constrained Langevin model on a specified branch-state manifold and nondegenerate transition states, Kramers theory predicts branch transition rates controlled by branch-conditioned barriers. SCC has not yet proved the full stochastic rate theorem; current deterministic work supplies candidate barriers and state variables.

---

## 7. Next Trigger

Proceed to final verification and campaign handoff refresh.

First move:

> Update `CAMPAIGN-SYNTHESIS.md`, `THEOREM-STATUS-REGISTRY.md`, and `NEXT-TRIGGER.md` to include the relaxed barrier and Kramers-rate additions, then run fresh verification.
