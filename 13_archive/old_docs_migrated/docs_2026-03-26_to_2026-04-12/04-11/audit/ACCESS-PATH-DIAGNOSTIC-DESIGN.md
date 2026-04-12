# Access-Path Diagnostic Design

**Date:** 2026-04-11
**Session:** Cycle 84 — design for the next continuation-access diagnostic
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP80-DENSE-BASIN-SCALING-20x20_c0.6.md; docs/04-11/experiment/EXP81-ACTIVE-SET-TRANSITION-PROXY-20x20_c0.6.md

---

## 1. Goal

Now that local basin robustness is strongly established, the next useful question is not whether the basin exists, but **how trajectories approach or fail to approach it**.

So the next diagnostic should compare raw and seeded runs *before* they are near the final basin.

---

## 2. Candidate Observables

### A. Energy descent profile

Track total energy versus iteration and compare:

- early descent speed,
- plateau timing,
- whether seeded runs enter a low-energy corridor earlier.

### B. Overlap decay profile

Track the inter-field overlap along the trajectory.

Reason:
- the target Type B branch is low-overlap at the tested positive lambdas;
- overlap decay may reveal whether seeded runs enter the right corridor earlier than raw runs.

### C. Coarse-region transition chronology

Refine the existing Exp81 idea by not only counting transitions, but timestamping when major region changes occur.

Reason:
- if raw trajectories make large early region jumps before seeded runs do, that could identify the point of divergence.

---

## 3. Recommended Diagnostic

**Start with A + B together.**

Reason:

1. energy and overlap are already central observables in the branch-selection story;
2. they are easier to interpret than a purely combinatorial transition trace;
3. they may show the basin-entry point more directly.

So the next experiment should log, for raw vs seeded runs on the same config/lambda:

- `E_total(tau)`
- `overlap(tau)`
- optionally a coarse region signature as supporting context.

---

## 4. Next Trigger

Implement a trajectory-comparison experiment that logs energy and overlap profiles for one raw run and one seeded run on `20x20:0.6`, `lambda=0.5`, then identify the earliest iteration at which the two paths clearly diverge.
