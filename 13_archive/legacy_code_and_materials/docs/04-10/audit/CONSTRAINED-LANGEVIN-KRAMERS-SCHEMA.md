# Constrained Langevin / Kramers Schema for SCC Branch Dynamics

**Date:** 2026-04-10
**Session:** Cycle 31 — constrained stochastic dynamics schema
**Category:** audit
**Status:** complete
**Depends on:** NEXT-PROOF-LANE-DECISION.md; R3-KRAMERS-RATE-FORMULATION.md; RELAXED-LOCAL-BASIN-BARRIER.md

---

## 1. CURRENT TARGET

Turn branch-conditioned deterministic barriers into legitimate stochastic transition-rate claims.

---

## 2. Fixed-Stratum Langevin Model

On a fixed active stratum `S` of the relaxed feasible polytope, with tangent projection `Pi_T`, the clean model is

```text
dZ_t = - Pi_T grad E_R(Z_t) dt + sqrt(2 epsilon) Pi_T dW_t.
```

This model is theorem-friendly only while the process remains inside the stratum. Boundary interaction must be handled separately.

---

## 3. Reflected Polytope Model

On the full polytope `R_M^K`, a more faithful model is a reflected diffusion:

```text
dZ_t = - Proj_T grad E_R(Z_t) dt + sqrt(2 epsilon) Proj_T dW_t + dL_t,
```

where `dL_t` is a reflection/local-time term enforcing box and simplex constraints.

This requires specifying:

- reflection directions at each active face,
- compatibility at corners,
- invariant measure,
- whether projection or reflection is intended.

---

## 4. Kramers Hypotheses Needed

For a transition from branch state `A` to event basin `Basin'`, SCC must assume/prove:

| Hypothesis | Meaning |
|---|---|
| H1 | source branch is a nondegenerate local minimum on the constrained stratum |
| H2 | exit saddle / minimax point exists and is nondegenerate index-1 |
| H3 | barrier height `DeltaE = E(saddle)-E(source) > 0` |
| H4 | no lower boundary/corner escape route bypasses the saddle |
| H5 | noise model and temperature normalization fixed |
| H6 | prefactor Hessian determinants are computed on tangent spaces |

---

## 5. Rate Formula Status

Under classical finite-dimensional overdamped Langevin assumptions on a smooth manifold without boundary, one expects

```text
rate(A -> B) ~ C_A exp(-DeltaE / epsilon).
```

For SCC constrained polytopes, this is **not yet a proved SCC theorem**. It is a theorem schema requiring either:

1. restriction to an interior/fixed active stratum with no boundary hits before transition, or
2. a cited reflected-diffusion Kramers theorem on domains with corners.

---

## 6. Decision

| Claim | Status |
|---|---|
| deterministic branch-conditioned barrier prerequisite | established |
| smooth fixed-stratum Langevin schema | defined |
| full reflected-polytope Langevin schema | defined but technically open |
| Kramers exponential rate in SCC | theorem-schema only, not proved |
| rate claims without noise model | invalid |

---

## 7. Next Trigger

Proceed to choose whether to:

1. restrict SCC stochastic rates to fixed active strata, or
2. develop/cite reflected-diffusion Kramers theory for polytopes.

First move:

> Create `docs/04-10/audit/KRAMERS-ACTIVE-STRATUM-VS-REFLECTED.md` comparing these two routes and selecting the safer theorem path.
