# Exp81 Active-Set Transition Proxy on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 75 — raw vs seeded trajectory-region comparison
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md; experiments/exp81_active_set_transition_proxy.py

---

## 1. Goal

Probe whether raw and seeded trajectories differ not only in final branch family, but also in how often they change coarse active-set / simplex-penalty / support-region signatures during optimization.

---

## 2. Proxy Definition

At logged iterations, record coarse state variables:

- simplex violation count and mass,
- near-zero / near-one counts,
- tau=0.1 support counts and component counts.

Count a transition whenever this coarse region signature changes between logged checkpoints.

---

## 3. Result

For `20x20:0.6` at `lambda=0.5`:

- raw trajectory transition count: `30`
- raw final branch type: `Type A candidate`
- seeded trajectory transition count: `12`
- seeded final branch type: `Type B candidate`

---

## 4. Interpretation

The raw trajectory experiences many more coarse region transitions than the seeded one.

Current reading:

1. the seeded run stays on a more coherent access path into the Type B valley;
2. the raw run wanders across more region changes before settling into a different final family;
3. this is consistent with the active-set trapping / access-path picture, even though it is still only a proxy diagnostic.

So Exp81 does not yet prove active-set trapping, but it strengthens the idea that **path geometry differs substantially** between raw and seeded access.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| raw vs seeded runs follow similarly stable coarse region paths | rejected in this proxy |
| active-set / penalty-region diagnostics are worth continuing | supported |
| next bridge should compare transition structure more systematically | yes |

---

## 6. Next Trigger

Decide whether to formalize an active-set trapping conjecture register, or to go back and build a cleaner basin-volume proxy now that both access-path and local-basin evidence exist.
