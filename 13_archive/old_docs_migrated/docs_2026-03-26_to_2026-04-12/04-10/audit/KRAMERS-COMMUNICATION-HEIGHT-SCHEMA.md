# Kramers / Large-Deviation Communication-Height Schema

**Date:** 2026-04-10
**Session:** Cycle 35 — fixed-stratum large-deviation schema
**Category:** audit
**Status:** complete
**Depends on:** RELAXED-MERGE-SADDLE-VS-COMMUNICATION-HEIGHT.md; KRAMERS-FIXED-STRATUM-THEOREM.md

---

## 1. CURRENT GAP

We need a rate statement that does **not** assume an index-1 saddle exists. The safe object is the communication height

```text
H(A,Basin';P)=inf_gamma max_t E_R(gamma(t)).
```

---

## 2. Fixed-Stratum Large-Deviation Model

On a smooth active stratum `S`, consider

```text
dZ_t = - grad_S E_R(Z_t) dt + sqrt(2 epsilon) dW_t^S.
```

Let `A` be the source basin around a local minimum `a`, and let `B` be a target/event basin. Define

```text
H(A,B) = inf_{gamma: A -> B} max_t E_R(gamma(t)),
DeltaE_comm = H(A,B) - E_R(a).
```

---

## 3. Large-Deviation Theorem Schema

Under standard Freidlin-Wentzell assumptions for finite-dimensional gradient diffusions on a smooth manifold / active stratum, the exponential scale of the mean transition time satisfies

```text
lim_{epsilon -> 0} epsilon log E_a[tau_B] = DeltaE_comm.
```

Equivalently, the transition rate has exponential scale

```text
rate(A -> B) ~ exp(-DeltaE_comm / epsilon)
```

at logarithmic accuracy.

---

## 4. Difference from Eyring-Kramers

| Level | Requires saddle? | Gives |
|---|---|---|
| Freidlin-Wentzell communication height | No explicit saddle required | exponential scale only |
| Eyring-Kramers prefactor | Yes, nondegenerate index-1 saddle | prefactor + exponential |

Thus SCC can safely use communication height for **log-scale kinetic predictions** before proving saddle existence.

---

## 5. SCC Assumptions Needed

| ID | Assumption |
|---|---|
| LD1 | fixed smooth active stratum or no boundary hit before transition |
| LD2 | finite-dimensional gradient diffusion with noise `sqrt(2 epsilon)` |
| LD3 | compact relevant sublevel sets or confinement |
| LD4 | source basin and target basin are open sets in the stratum |
| LD5 | communication height finite and positive |
| LD6 | branch/path class defining admissible transitions is fixed |

---

## 6. What Is Now Theorem-Level

The theorem-level statement is conditional:

> If SCC branch dynamics is modeled as a finite-dimensional fixed-stratum overdamped Langevin gradient diffusion satisfying LD1-LD6, then the transition-time exponential scale is controlled by the branch-conditioned communication height.

This is a classical large-deviation theorem schema, not a newly proved SCC-specific stochastic theorem.

---

## 7. What Remains Open

| Open item | Reason |
|---|---|
| reflected-polytope large deviations | boundary/corner reflection not specified |
| prefactor | requires saddle and Hessian determinant |
| actual communication height for relaxed merge | requires MEP/sublevel analysis |
| stochastic model validation | modeling / implementation question |

---

## 8. Decision

| Claim | Outcome |
|---|---|
| communication height controls log-scale rate | accepted under fixed-stratum Freidlin-Wentzell assumptions |
| saddle-free prefactor | not available |
| SCC stochastic rate without LD assumptions | invalid |
| next deterministic need | compute/bound `DeltaE_comm` for selected branch/path class |

---

## 9. Next Trigger

Return to deterministic communication-height computation for relaxed merge.

First move:

> Build a finite-dimensional discretized MEP experiment or proof scaffold that estimates `H(A,B)` for the selected branch/path class, explicitly comparing direct interpolation and diffuse shortcut paths.
