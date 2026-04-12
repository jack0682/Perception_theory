# Fixed-Stratum Kramers Theorem Schema for SCC

**Date:** 2026-04-10
**Session:** Cycle 33 — fixed-stratum Kramers theorem schema
**Category:** audit
**Status:** complete
**Depends on:** KRAMERS-ACTIVE-STRATUM-VS-REFLECTED.md; CONSTRAINED-LANGEVIN-KRAMERS-SCHEMA.md; RELAXED-LOCAL-BASIN-BARRIER.md

---

## 1. CURRENT GAP

We need a theorem-safe way to turn a branch-conditioned deterministic barrier into a stochastic transition-rate statement.

The selected route is the **fixed active stratum** route.

---

## 2. State Space

Let `S` be a smooth active stratum of the relaxed SCC feasible polytope. Let `dim S = d`, and let `z in S` denote local coordinates for a selected branch-state chart.

Assume `E_R:S -> R` is smooth on `S`.

---

## 3. Dynamics

Use overdamped Langevin dynamics on the stratum:

```text
dZ_t = - grad_S E_R(Z_t) dt + sqrt(2 epsilon) dW_t^S.
```

Here:

- `grad_S` is the Riemannian / Euclidean stratum gradient;
- `W_t^S` is Brownian motion in the tangent coordinates of `S`;
- `epsilon` is the noise temperature.

This excludes boundary/corner interactions before the transition.

---

## 4. Kramers Assumptions

For a transition from source branch `A` to target basin `Basin'`, assume:

| ID | Assumption |
|---|---|
| K1 | `a` is a nondegenerate local minimum of `E_R` on `S` |
| K2 | `s` is the unique relevant index-1 saddle separating `a` from `Basin'` |
| K3 | `DeltaE = E_R(s)-E_R(a) > 0` |
| K4 | all lower-energy boundary/corner escape routes are excluded by the fixed-stratum assumption |
| K5 | Hessian at `a` is positive definite on `T_a S` |
| K6 | Hessian at `s` has exactly one negative eigenvalue on `T_s S` |
| K7 | no competing saddle with equal or lower communication height is omitted |

---

## 5. Classical Rate Formula

Under the classical Eyring-Kramers theorem for finite-dimensional overdamped Langevin dynamics on a smooth domain/manifold, the transition rate has exponential scale

```text
rate(a -> Basin') = prefactor * exp(-DeltaE / epsilon) * (1 + o(1))
```

as `epsilon -> 0`.

For Euclidean tangent coordinates, the formal prefactor has the usual Hessian-ratio shape:

```text
prefactor = |lambda_-(s)| / (2 pi)
            * sqrt( det Hess E_R(a) / |det' Hess E_R(s)| )
```

where `lambda_-(s)` is the unique negative Hessian eigenvalue at the saddle and `det'` omits/sign-corrects the unstable direction.

---

## 6. SCC Interpretation

In SCC notation:

```text
DeltaE_branch = E_R(s_branch) - E_R(B_branch)
```

is branch/path/stratum conditioned. Therefore the rate is also branch/path/stratum conditioned.

The only theorem-level SCC statement is:

> If the SCC branch dynamics is modeled by fixed-stratum overdamped Langevin dynamics and the classical Eyring-Kramers assumptions K1-K7 hold, then the branch transition rate has exponential scale `exp(-DeltaE_branch/epsilon)`.

---

## 7. What This Does Not Prove

| Missing item | Status |
|---|---|
| reflected-polytope Kramers law | not proved |
| boundary/corner saddle contribution | excluded |
| existence of the relevant saddle | separate deterministic variational problem |
| correctness of stochastic model for implementation | modeling assumption |
| prefactor for SCC with active constraints | classical formula after coordinate choice, not computed |

---

## 8. Decision

| Claim | Outcome |
|---|---|
| fixed-stratum Kramers schema | accepted as classical theorem under assumptions |
| SCC rate without specifying stratum/noise/saddle | invalid |
| reflected-polytope Kramers rate | deferred |
| branch-conditioned exponential scale | theorem-schema under K1-K7 |

---

## 9. Next Trigger

Proceed to deterministic saddle existence / communication-height identification for a specified branch transition.

First move:

> For a selected relaxed merge branch and path class, identify whether an index-1 saddle exists after local basin escape, or whether only a minimax communication height can be defined.
