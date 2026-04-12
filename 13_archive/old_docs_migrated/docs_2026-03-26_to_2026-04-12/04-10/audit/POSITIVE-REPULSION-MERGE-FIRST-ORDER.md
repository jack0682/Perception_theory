# Positive-Repulsion Relaxed Merge First-Order Analysis

**Date:** 2026-04-10
**Session:** Cycle 46 — positive-repulsion relaxed merge first-order bound
**Category:** audit
**Status:** complete
**Depends on:** ZERO-REPULSION-SUBLEVEL-DIAGNOSTICS.md; ZERO-REPULSION-RELAXED-MERGE-ZERO-BARRIER.md; POSITIVE-REPULSION-SELECTION.md

---

## 1. CURRENT GAP

The zero-repulsion sampled relaxed merge barrier collapses to zero. For `lambda_rep > 0`, exp69 shows a positive communication-height proxy. We need to determine whether this admits a theorem-level first-order lower bound of the form

```text
DeltaE(lambda_rep) >= lambda_rep * unavoidable_overlap + higher-order terms.
```

---

## 2. Energy Decomposition

Write the relaxed energy as

```text
E_lambda(z) = E_0(z) + lambda R(z),
```

where

```text
R(u1,u2) = <u1,u2>
```

is the repulsion/overlap functional.

For a fixed path `gamma`,

```text
max_t E_lambda(gamma(t))
  = max_t [E_0(gamma(t)) + lambda R(gamma(t))].
```

If `gamma` lies in the zero-repulsion source sublevel set `E_0 <= E_0(B)`, then the only positive excess at small lambda comes from overlap along the path.

---

## 3. Path-Class First-Order Quantity

Define the unavoidable overlap height inside the zero-repulsion sublevel path class:

```text
Omega_0(B,T;P)
  = inf_{gamma in P_0(B,T)} max_t R(gamma(t)),
```

where

```text
P_0(B,T) = { gamma in P(B,T) : max_t E_0(gamma(t)) <= E_0(B) }.
```

If `P_0` is nonempty, then for paths restricted to this zero-excess class,

```text
DeltaE_lambda(B,T;P_0) >= lambda * Omega_0(B,T;P).
```

This is immediate because `E_0` contributes no positive excess and `R >= 0`.

---

## 4. Obstruction to a Universal Positive Coefficient

The first-order coefficient can be zero.

If there exists a zero-excess path with

```text
max_t <u1(t),u2(t)> = 0,
```

then

```text
Omega_0 = 0.
```

This is possible when mass can be transferred through states with disjoint supports or by first moving one component to zero before overlap occurs. Therefore positive repulsion alone does not guarantee a positive first-order lower bound unless the path class forces overlap or simultaneous occupancy.

---

## 5. Corrected Theorem Schema

**Theorem (Path-Class First-Order Repulsion Bound).**
For a specified branch, target, and path class `P`, suppose the zero-repulsion source-sublevel path class `P_0(B,T)` is nonempty and has unavoidable overlap height

```text
Omega_0(B,T;P) > 0.
```

Then for small positive `lambda_rep`, any path in `P_0` has communication excess at least

```text
lambda_rep * Omega_0(B,T;P).
```

If `Omega_0=0`, no positive first-order lower bound follows from repulsion.

---

## 6. Relation to exp69

exp69 shows positive barrier proxies for `lambda_rep=1,5`, but this does not by itself prove `Omega_0>0`; the observed proxy may depend on the sampled path class, source branch, endpoint convention, and nonzero-lambda deformation of the source.

The zero-lambda sampled paths have zero excess. To extract a first-order theorem, future experiments should measure overlap maxima along zero-excess paths and estimate whether `Omega_0` is positive under the chosen path restrictions.

---

## 7. Decision

| Claim | Outcome |
|---|---|
| first-order repulsion term is overlap | proved / by decomposition |
| positive first-order lower bound | conditional on unavoidable overlap `Omega_0>0` |
| universal positive coefficient | false; can be zero if overlap-avoiding paths exist |
| exp69 positive-lambda proxy | numerical support, not proof of `Omega_0>0` |

---

## 8. Next Trigger

Measure/estimate `Omega_0` for sampled path classes:

> Add overlap maxima diagnostics to exp67/exp68/exp69 path summaries, especially for `lambda_rep=0`, to distinguish zero-excess paths with zero overlap from zero-excess paths that would acquire first-order repulsion cost.

---

## Cycle 47b correction — use overlap excess

Follow-up diagnostics showed that raw max overlap is insufficient. The first-order communication excess relative to the source branch depends on overlap excess:

```text
max_t <u1(t),u2(t)> - <u1(0),u2(0)>
```

The sampled zero-repulsion path has nonzero source overlap but zero overlap excess. Therefore a positive first-order lower bound requires unavoidable overlap excess, not merely nonzero overlap. Positive-lambda exp69 barriers also reflect branch re-selection under repulsion.
