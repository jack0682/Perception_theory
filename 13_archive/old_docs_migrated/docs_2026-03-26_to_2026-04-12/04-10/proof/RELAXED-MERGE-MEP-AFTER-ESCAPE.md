# Relaxed Merge MEP After Local Basin Escape

**Date:** 2026-04-10
**Session:** Cycle 25 — global relaxed merge MEP after local escape
**Category:** proof
**Status:** complete
**Depends on:** RELAXED-LOCAL-BASIN-BARRIER.md; docs/04-10/audit/RELAXED-MERGE-GLOBAL-PATH-CONDITION.md; docs/04-10/audit/R3-KRAMERS-RATE-FORMULATION.md

---

## 1. CURRENT GAP

After proving a local relaxed basin barrier, the remaining question is:

> Once a path exits the local basin of a strict K=2 branch `B`, must it pay an additional boundary/morphology energy cost before reaching the embedded K=1 target `T=(u_merged,0)`?

This document decides what can and cannot be proved without stronger path restrictions.

---

## 2. Definitions

Let `E_R` be the relaxed energy on `R_M^2`. Let `B` be a strict relaxed local minimizer with local basin radius `rho_B`, and define the local sphere

```text
S_B(rho_B) = { z in R_M^2 : ||z-B|| = rho_B }.
```

Let `T = Embed(u_merged)` be the K=1 target.

Define the post-escape communication height:

```text
H_post(B,T;rho_B,P)
  = inf_{z in S_B(rho_B)} inf_{eta in P(z,T)} max_s E_R(eta(s)).
```

Then the global relaxed merge barrier decomposes as

```text
DeltaE_relax(B,T,P)
  >= max( local_escape_height,
          H_post(B,T;rho_B,P) - E_R(B) )
```

where

```text
local_escape_height >= (mu_R/4) rho_B^2.
```

---

## 3. Tautological but Useful Theorem

**Theorem (Post-Escape Separation Criterion).**
If every path from the local sphere `S_B(rho_B)` to the target `T` in path class `P` crosses energy level at least

```text
E_R(B) + (mu_R/4) rho_B^2 + eta
```

for some `eta > 0`, then

```text
DeltaE_relax(B,T,P) >= (mu_R/4) rho_B^2 + eta.
```

**Proof.** Any path from `B` to `T` first exits the local ball, paying the local basin barrier. After first exit, by the hypothesis on post-escape paths, it must cross the higher level. Taking the infimum over paths preserves the lower bound. ∎

**Status:** PROVED, but the substantive burden is the post-escape separation hypothesis.

---

## 4. No Automatic Additional Barrier

There is no theorem-level reason, from current SCC assumptions alone, that `eta > 0` must hold.

If there exists a path from some exit point `z in S_B(rho_B)` to `T` satisfying

```text
E_R(eta(s)) <= E_R(B) + (mu_R/4) rho_B^2 + o(1),
```

then the global barrier equals the local escape barrier up to `o(1)`.

Thus additional global barrier is a **sublevel-set connectivity question**:

```text
Are S_B(rho_B) and T disconnected inside the sublevel set
{ E_R <= E_R(B) + local_escape_height + eta } ?
```

Without proving this disconnection, one cannot claim an additional boundary/morphology barrier.

---

## 5. Dissolve-Spread-Transfer-Reconcentrate Route

The main obstruction is an admissible route of the form:

1. leave the local K=2 basin by softening or spreading one formation;
2. transfer mass through low-overlap diffuse states;
3. concentrate the total field into the K=1 target.

This route may avoid direct core-core overlap and may avoid the high linear-interpolation barrier. Whether it pays a boundary/morphology cost larger than the local escape height depends on the chosen path class and energy normalization.

Therefore:

- direct interpolation barriers are upper bounds for direct path classes only;
- NEB/string methods approximate a path-class-dependent MEP;
- no branch-independent lower bound follows from current theory.

---

## 6. Corrected Global Barrier Statement

A rigorous global relaxed merge lower bound must be stated as:

> Under relaxed local stability at `B`, target-outside-local-basin, and a post-escape sublevel separation condition between the local exit sphere and `T`, the relaxed merge barrier is at least the local escape height plus the post-escape separation margin.

Equivalently:

```text
DeltaE_relax >= local_escape_height + eta
```

only if `eta` is proved by sublevel-set separation or path-class restrictions.

---

## 7. Decision

| Claim | Outcome |
|---|---|
| local escape contribution | proved under relaxed Hessian gap |
| additional post-escape boundary/morphology barrier | not automatic |
| global barrier > local barrier | conditional on sublevel-set separation |
| dissolve-spread-transfer shortcut | obstruction requiring analysis or path restriction |
| direct interpolation barrier | path-specific upper bound, not MEP lower bound |

---

## 8. Registry Delta

R4 remains **OPEN-CONDITIONAL**:

- object defined;
- local barrier proved;
- target-outside-local-basin condition proved under mass/radius assumptions;
- global post-escape barrier requires a new sublevel-set separation theorem or explicit path restrictions.

---

## 9. Next Trigger

Proceed to sublevel-set separation / shortcut analysis.

First move:

> Decide whether SCC energy sublevel sets below the direct-interpolation barrier connect the local exit sphere to the K=1 target through diffuse states. If yes, direct barrier overestimates the MEP; if no, prove a morphology lower bound.
