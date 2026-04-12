# R3 Branch-Aware Kinetic Dynamics State

**Date:** 2026-04-10
**Session:** Cycle 16 — multi-formation kinetic dynamics state setup
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/proof/NEARBIF-CUBIC-NORMAL-FORM.md; docs/04-10/audit/B1-R4-BRANCH-CONDITIONED-MERGE.md; docs/04-10/proof/OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md

---

## 1. CURRENT GAP

**Canonical item:** R3 — multi-formation kinetic dynamics.

**Current category:** research blocker.

The theory has moved from thermodynamic K-selection to kinetic branch/barrier dynamics. A minimal state description is needed before rigorous coarsening or stochastic birth/death rates can be stated.

---

## 2. Minimal Kinetic State Variables

A branch-aware kinetic state should include:

| Variable | Meaning |
|---|---|
| `K` | number of active formations |
| `branch_id` | selected local branch / tie-breaker class |
| `u^1,...,u^K` | current soft fields or reduced branch coordinates |
| `m_k` | per-formation masses |
| `d_jk` | pairwise graph/support distances |
| `omega_jk` | soft overlap / coupling weights |
| `barrier_{event}` | branch-conditioned barrier to merge/split/birth/death |
| `mu_k`, `mu_joint` | local Hessian gaps |
| `noise_scale` | stochastic forcing amplitude |
| `event_type` | merge, split, birth, death, branch switch |
| `path_class` | admissible transition path class |

---

## 3. Markov Skeleton

A minimal coarse kinetic model is a continuous-time jump process over branch states:

```text
state S = (K, branch_id, geometry, masses, barriers, gaps)
```

with transition rates of Kramers type:

```text
rate(S -> S') ~ A(S,S') exp(-DeltaE_branch(S,S') / noise_scale^2)
```

where `DeltaE_branch` is branch/path conditioned, not universal.

---

## 4. What Is Proved vs Open

| Claim | Status |
|---|---|
| K>1 states are kinetic/metastable, not global thermodynamic minima | established by prior audits |
| branch-conditioned barriers are required | established by R1/B1/R4 |
| Kramers-form transition rates | plausible but unproved for SCC finite-dimensional gradient dynamics with constraints |
| event graph over branch states | open construction |
| stochastic birth/death rates | open |

---

## 5. Corrected Research Target

R3 should not attempt a single deterministic K evolution law. The honest target is:

> Construct a branch-state transition graph and assign rigorously defined branch-conditioned barriers. Only after barriers and noise model are specified can stochastic coarsening rates be derived.

---

## 6. Next Trigger

Proceed to R4 — relaxed-manifold merge barrier, now as the first concrete kinetic barrier needed by R3.

First move:

> Define a valid relaxed manifold and endpoint convention for K=2 -> K=1 merge, avoiding the retracted constrained-manifold endpoint error.
