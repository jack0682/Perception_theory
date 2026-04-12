# Next Proof Lane Decision

**Date:** 2026-04-10
**Session:** Cycle 30 — proof-lane selection after relaxed merge/no-peeling analysis
**Category:** audit
**Status:** complete
**Depends on:** CORE-DISSOLUTION-NO-PEELING.md; CAMPAIGN-SYNTHESIS.md; R3-KRAMERS-RATE-FORMULATION.md

---

## 1. Candidate Lanes

| Lane | Theorem value | Risk | Verdict |
|---|---|---|---|
| A. Collective/no-peeling morphology barrier | Could produce mass-scaled event barrier | High artificiality; path class may be modeling artifact | Defer until physical path rule justified |
| B. Constrained Langevin/Kramers theorem | Turns branch barriers into kinetic rates; central for R3 | Requires stochastic model choices; can be cleanly axiomatized | **Select next** |
| C. Relaxed merge MEP numerical design | Useful evidence for path geometry | Numerical support only, not theorem closure | Defer as support after theorem model fixed |

---

## 2. Decision

Select **Lane B: constrained Langevin/Kramers theorem assumptions**.

Reason:

1. R3 kinetic dynamics cannot become theorem-level without a stochastic process definition.
2. Relaxed barrier artifacts already identify candidate `DeltaE_branch`; rate claims now need model assumptions.
3. Collective/no-peeling morphology barriers are too path-class-specific and risk becoming artificial before the physical stochastic model is specified.
4. Numerical MEP design should follow, not precede, a clear stochastic/path model.

---

## 3. Next Theorem Target

Define a constrained finite-dimensional overdamped Langevin model on a fixed active stratum and state a theorem-schema for Kramers exit asymptotics.

The immediate objective is not to prove a new Kramers theorem from scratch, but to specify exactly what SCC must assume/cite before claiming rates.

---

## 4. Required Output

Create:

```text
docs/04-10/audit/CONSTRAINED-LANGEVIN-KRAMERS-SCHEMA.md
```

It must include:

1. state space / active stratum,
2. SDE or projected/reflected dynamics,
3. noise normalization,
4. source minimum and saddle hypotheses,
5. rate formula status,
6. what remains open.
