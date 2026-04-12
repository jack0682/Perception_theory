# Exp82 Access-Path Trajectory Comparison on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 85 — raw vs seeded trajectory profiles
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/audit/ACCESS-PATH-DIAGNOSTIC-DESIGN.md; experiments/exp82_access_path_trajectory.py

---

## 1. Goal

Compare raw and seeded trajectories before basin entry using the most interpretable observables:

- `E_total(tau)`
- overlap `R(tau)`

---

## 2. Main Result

For `20x20:0.6`, `lambda=0.5`:

- earliest clear divergence iteration: `1`

First logged checkpoints:

### Raw trajectory
- iter 1: energy = 91.490273, overlap = 29.103149
- iter 5: energy = 88.874945, overlap = 28.469858
- iter 10: energy = 86.030259, overlap = 27.764231

### Seeded trajectory
- iter 1: energy = 17.902276, overlap = 0.044707
- iter 5: energy = 17.896069, overlap = 0.044185
- iter 10: energy = 17.888260, overlap = 0.043526

---

## 3. Interpretation

The two trajectories are not merely diverging late near convergence. They are already in radically different corridors at the first logged iteration:

- raw start begins in a very high-energy, high-overlap regime;
- seeded start begins immediately in a low-energy, low-overlap regime close to the target Type B basin.

So the access asymmetry appears **very early**, well before any subtle late-stage branch choice.

This strongly reinforces the continuation-access explanation:

> the key difference is not how the optimizer behaves near the end, but whether it enters the right corridor at all.

---

## 4. Decision

| Claim | Outcome |
|---|---|
| raw and seeded runs diverge only late in optimization | rejected |
| corridor access differs from the very start | strongly supported |
| continuation-access hypothesis | strengthened again |

---

## 5. Next Trigger

The next sensible move is no longer another small diagnostic; it is to summarize the analytic evidence chain for continuation access in one compact note.
