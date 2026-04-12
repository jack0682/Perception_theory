# R4 Relaxed-Manifold Merge Barrier Definition

**Date:** 2026-04-10
**Session:** Cycle 17 — relaxed-manifold merge barrier setup
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/R3-KINETIC-DYNAMICS-STATE.md; docs/04-10/audit/B1-R4-BRANCH-CONDITIONED-MERGE.md

---

## 1. CURRENT GAP

**Canonical item:** R4 — relaxed-manifold merge barrier.

**Current category:** research blocker.

The old constrained-manifold merge endpoint `(u_merged,0)` was invalid on fixed per-formation mass constraints. Therefore a valid merge barrier requires a relaxed state space.

---

## 2. Valid Relaxed State Space

For K=2 total mass `M`, define a relaxed two-field manifold:

```text
R_M^2 = { (u1,u2): 0 <= u_k <= 1,  sum_x (u1+u2)=M,  u1+u2 <= 1 }
```

This relaxes per-formation masses while retaining total mass and simplex occupancy.

The K=1 state embeds as

```text
Embed(u) = (u, 0)
```

or any label permutation `(0,u)`.

Now `(u_merged,0)` is a valid endpoint if `sum u_merged = M`.

---

## 3. Branch-Conditioned Source

The source must be a selected K=2 branch state

```text
B = (u1_B, u2_B) in R_M^2
```

with metadata:

- branch id / selection rule,
- masses `(m1,m2)`,
- overlap/separation geometry,
- Hessian gaps,
- tie-breaker convention.

Without this, the barrier is not a scalar.

---

## 4. Admissible Path Class

A relaxed merge path is a continuous path

```text
gamma: [0,1] -> R_M^2
```

such that

```text
gamma(0)=B,
gamma(1)=Embed(u_merged).
```

Path classes must be specified. Examples:

| Path class | Meaning |
|---|---|
| linear relaxed interpolation | simple upper-bound path |
| projected gradient/NEB path | numerical minimum-energy path candidate |
| geodesic in total-field variable | path constrained by total field geometry |
| mass-transfer path | transfers mass from u2 to u1 before shape relaxation |

---

## 5. Barrier Functional

For a specified branch `B`, target `u_merged`, and path class `P`, define

```text
DeltaE_relax(B,u_merged,P)
  = inf_{gamma in P} [ max_t E_R(gamma(t)) - E_R(B) ].
```

Here `E_R` is the relaxed K-field energy with total mass constraint and without fixed per-formation masses.

---

## 6. What Is Now Fixed

| Prior issue | Resolution |
|---|---|
| invalid endpoint on `Sigma_M^K` | use relaxed total-mass manifold `R_M^2` |
| branch-free source | require selected branch `B` |
| path ambiguity | include path class `P` in barrier definition |
| scalar exponent ambiguity | exponent becomes branch/path/manifold conditioned |

---

## 7. Remaining Open Work

This document defines the object. It does not prove a positive lower bound or compute a minimum-energy path.

Next proof work must attack:

1. existence of minimax path in `R_M^2`,
2. lower bound from boundary/morphology energy along any merge path,
3. comparison of linear path vs NEB path,
4. Kramers-rate interpretation under a specified noise model.

---

## 8. Gap Campaign Status

At this point, every formal Category B/C item and every listed research blocker from `LATEST-GAP-TABLE.md` has a current 04-10 audit/proof artifact. None required an unsafe Canonical Spec category upgrade.

---

## 9. Next Trigger

Start a new pass over the registry deltas and prepare a consolidated theorem-status synchronization proposal.

First move:

> Create `docs/04-10/audit/CAMPAIGN-SYNTHESIS.md` summarizing all closed/reformulated/open-exhausted outcomes and listing exact future Canonical Spec edits to consider, without applying them yet.
