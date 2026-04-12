# Zero-Repulsion Relaxed Merge: Zero-Barrier Conditions

**Date:** 2026-04-10
**Session:** Cycle 44 — zero-repulsion relaxed merge zero-proxy theorem
**Category:** proof
**Status:** complete
**Depends on:** docs/04-10/audit/RELAXED-MERGE-NEB-LITE-LREP-GRID.md; docs/04-10/proof/RELAXED-MERGE-BARRIER-LOWER-BOUND.md

---

## 1. CURRENT GAP

The exp69 lambda/grid sweep repeatedly observed:

```text
lambda_rep = 0  => relaxed merge proxy = 0
lambda_rep > 0  => relaxed merge proxy > 0
```

We test whether the zero-repulsion proxy is a theorem under the exp67/exp69 endpoint and path conventions.

---

## 2. Energy at Zero Repulsion

At `lambda_rep=0`, the relaxed K=2 energy is

```text
E_R(u1,u2) = E_self(u1) + E_self(u2) + lambda_bar ||(u1+u2-1)_+||^2.
```

If the path stays in the simplex-feasible region `u1+u2<=1`, this reduces to

```text
E_R(u1,u2) = E_self(u1) + E_self(u2).
```

There is no coupling term selecting or penalizing interaction between the two fields.

---

## 3. Sufficient Zero-Barrier Condition

Let `B=(u1,u2)` be the source and `T=(u_merge,0)` the target. For a path class `P`, if there exists a path `gamma in P(B,T)` satisfying

```text
E_R(gamma(t)) <= E_R(B)     for all t,
```

then

```text
DeltaE_R(B,T,P) <= 0.
```

With the convention that barriers are clipped at zero,

```text
DeltaE_R^+ = max(0, DeltaE_R) = 0.
```

**Proof.** Direct from the definition of communication height. ∎

---

## 4. Is the Condition Automatic at lambda_rep=0?

No.

Zero repulsion removes the interaction term, but `E_self(u1)+E_self(u2)` may still have nonconvex barriers along a chosen path. A zero barrier requires a non-increasing or non-overshooting path from the selected K=2 branch to the embedded K=1 target.

Thus the theorem is conditional:

```text
lambda_rep=0 alone does not prove zero barrier.
```

---

## 5. Why exp67/exp69 See Zero

In the smoke runs, the selected endpoint/path convention apparently satisfies the sufficient condition: along the sampled direct/relaxed path, the maximum energy never exceeds the source energy. This is consistent with the fact that the K=1 total-mass formation often has lower self-energy than two independent half-mass formations, and there is no repulsion penalty at `lambda_rep=0`.

But this remains a sampled numerical fact for those branches and paths.

---

## 6. Counterexample Possibility

A zero-repulsion path can still have positive barrier if:

1. the target `u_merge` is separated by a self-energy barrier from `u1`,
2. the path class is restricted to direct interpolation through high double-well states,
3. `E_self(u2)` must dissolve through a high-energy uniform/spinodal state,
4. the selected K=2 source is itself a strict relaxed local minimizer at `lambda_rep=0`.

Therefore no universal theorem says all zero-repulsion relaxed merges have zero barrier.

---

## 7. Corrected Theorem

**Theorem (Zero-Repulsion Zero-Barrier Criterion).**
At `lambda_rep=0`, the relaxed merge barrier is zero for a specified source, target, and path class if and only if the source and target lie in the same connected component of the sublevel set

```text
{ z in R_M^2 : E_R(z) <= E_R(B) }.
```

**Proof.** If they lie in the same connected component, there is a continuous path from `B` to `T` inside the sublevel set, so the communication height is at most `E_R(B)`, giving zero clipped barrier. Conversely, if the clipped barrier is zero, for every `eta>0` there are paths with maximum energy at most `E_R(B)+eta`; exact same-component membership at level `E_R(B)` additionally requires compactness/closed-sublevel limiting or an actually attained path. Thus the precise biconditional is exact for an attained path and approximate in the usual communication-height infimum sense. ∎

---

## 8. Decision

| Claim | Outcome |
|---|---|
| `lambda_rep=0` removes interaction barrier | proved |
| zero clipped barrier if source/target connected below source energy | proved |
| lambda_rep=0 alone implies zero barrier | false / too strong |
| exp69 zero proxy | numerical evidence that sufficient condition holds in tested branch/path convention |

---

## 9. Next Trigger

Proceed to sublevel connectivity diagnostics:

> For exp69 zero-repulsion cases, verify whether sampled direct path energies are all below source energy and record this as evidence for same-sublevel connectivity under the sampled path.
