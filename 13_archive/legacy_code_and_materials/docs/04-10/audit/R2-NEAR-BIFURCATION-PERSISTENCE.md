# R2 Near-Bifurcation Persistence Problem Statement

**Date:** 2026-04-10
**Session:** Cycle 13 — near-bifurcation persistence setup
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/C1-TPERSIST-EXACT-THRESHOLD.md; docs/04-10/audit/C2-TPERSIST-FULL-COMPOSITION.md; docs/03-31/theory/NEAR-BIFURCATION-LOCAL-THEORY.md

---

## 1. CURRENT GAP

**Canonical item:** R2 — near-bifurcation persistence (`mu -> 0`).

**Current category:** research blocker.

---

## 2. What Fails as mu -> 0

The standard perturbation displacement estimate has the form

```text
||u_s - u_t|| <= C epsilon / mu.
```

As the constrained Hessian gap `mu -> 0`, this bound diverges. Therefore no uniform full-persistence theorem can hold across bifurcation without additional structure.

Exact-threshold preservation fails first, because it requires

```text
C epsilon / mu < interior_gap.
```

For fixed epsilon, this inequality eventually fails as `mu -> 0`.

---

## 3. What Can Survive

| Persistence form | Near-bifurcation status |
|---|---|
| branch-local IFT away from `mu=0` | valid for each `mu>0`, with shrinking radius |
| shifted-threshold persistence | survives in shrinking window |
| deep-core remnant | survives if interior gap dominates displacement on deep core |
| all-core exact-threshold persistence | not uniform; generally fails |
| branch selection through crossing | open center-manifold problem |

---

## 4. Shrinking-Window Theorem Schema

A valid theorem should have the form:

> Let `mu` be the smallest constrained Hessian eigenvalue along a formation branch approaching a bifurcation. If the transition size satisfies `epsilon = o(mu * gamma_int(mu))`, then deep-core exact-threshold persistence survives. If only `epsilon = O(mu)`, shifted-threshold persistence survives with margin loss. No fixed epsilon window persists uniformly as `mu -> 0`.

---

## 5. Center-Manifold Attack Plan

To close R2, reduce the dynamics near the critical branch to a soft-mode coordinate `a`:

```text
E(a,lambda) = E0 + 1/2 mu(lambda) a^2 + c3 a^3 + c4 a^4 + higher order.
```

Required tasks:

1. identify the critical eigenmode and active stratum;
2. derive normal form coefficients `c3,c4`;
3. classify branch selection across `mu=0`;
4. compute basin shrinkage rate;
5. translate basin shrinkage into persistence margin conditions.

---

## 6. Obstruction Notes

Uniform persistence across `mu=0` is structurally impossible without restricting perturbation size, because arbitrarily small energy curvature allows finite displacement along the soft mode.

Thus R2 should not target “remove near-bifurcation condition.” It should target:

- exact shrinking-window exponents,
- branch-selection normal form,
- remnant persistence classification.

---

## 7. Next Trigger

Continue R2 with a method ledger and normal-form derivation attempt.

First concrete subtarget:

> Derive a one-dimensional normal-form persistence bound: if `E(a)=1/2 mu a^2 + 1/4 c4 a^4` with `c4>0`, determine basin radius and displacement scaling as `mu -> 0`.
