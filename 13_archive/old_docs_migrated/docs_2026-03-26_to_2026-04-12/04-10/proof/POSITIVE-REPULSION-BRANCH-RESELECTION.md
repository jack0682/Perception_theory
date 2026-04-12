# Positive-Repulsion Branch Reselection Theorem

**Date:** 2026-04-10
**Session:** Cycle 49 — source branch reselection under positive repulsion
**Category:** proof
**Status:** complete
**Depends on:** docs/04-10/audit/FIXED-BRANCH-REPULSION-PERTURBATION.md; POSITIVE-REPULSION-SELECTION.md

---

## 1. CURRENT GAP

Positive-lambda exp69 barriers appear mainly because the optimized source branch changes. We prove the finite-candidate branch-ordering mechanism.

---

## 2. Setup

Let `B_i=(u1_i,u2_i)` be a finite family of candidate K=2 branches in the relaxed or fixed K-field state space. Write the energy as

```text
E_lambda(B_i) = E_0(B_i) + lambda R(B_i),
R(B_i)=<u1_i,u2_i>.
```

---

## 3. Equal Self-Energy Ordering Theorem

Suppose two branches `B_a`, `B_b` satisfy

```text
E_0(B_a)=E_0(B_b),
R(B_a) < R(B_b).
```

Then for every `lambda>0`,

```text
E_lambda(B_a) < E_lambda(B_b).
```

**Proof.** Subtract:

```text
E_lambda(B_b)-E_lambda(B_a)
  = [E_0(B_b)-E_0(B_a)] + lambda [R(B_b)-R(B_a)]
  = lambda [R(B_b)-R(B_a)] > 0.
```

Thus the lower-overlap branch is selected among equal-self-energy candidates. ∎

---

## 4. Unequal Self-Energy Threshold

If

```text
DeltaE_0 = E_0(B_a)-E_0(B_b),
DeltaR = R(B_b)-R(B_a) > 0,
```

then `B_a` beats `B_b` when

```text
E_lambda(B_a) < E_lambda(B_b)
```

which is equivalent to

```text
DeltaE_0 < lambda DeltaR.
```

If `DeltaE_0>0`, the lower-overlap branch `B_a` becomes preferred only above the threshold

```text
lambda > DeltaE_0 / DeltaR.
```

---

## 5. Consequence for exp69 / exp70

- exp70 fixed-branch evaluation showed that adding repulsion to the same zero-repulsion branch/path did not create overlap-excess barrier.
- exp69 positive-lambda optimization selected different low-overlap branches, from which merge paths created overlap-excess.

The theorem above explains this: positive `lambda_rep` reorders candidate source branches by overlap, with a threshold determined by self-energy gap divided by overlap gap.

---

## 6. Corrected Branch-Conditioned Picture

Positive repulsion influences relaxed merge barriers through two distinct channels:

1. **source branch reselection:** lower-overlap branches become energetically preferred;
2. **path communication excess:** once a low-overlap source is selected, paths to K=1 may create overlap excess and therefore positive repulsion cost.

These must not be conflated.

---

## 7. Decision

| Claim | Outcome |
|---|---|
| equal-self-energy lower-overlap branch wins for any positive lambda | PROVED |
| unequal self-energy selection threshold | PROVED: `lambda > DeltaE_0/DeltaR` |
| exp69 positive-lambda barrier via branch reselection | theoretically explained |
| universal branch selection without candidate set | not proved |

---

## 8. Next Trigger

Estimate branch-reselection thresholds empirically:

> Use exp65/exp66 branch data to compare source self-energy and overlap for zero-vs-positive-lambda branches, estimating `DeltaE_0/DeltaR` where possible.
