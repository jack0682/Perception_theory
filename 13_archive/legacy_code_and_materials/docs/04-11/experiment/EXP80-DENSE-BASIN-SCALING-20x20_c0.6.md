# Exp80 Dense Basin-Size Scaling on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 83 — dense perturbation ladder for local basin size
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md; experiments/results/exp80_local_basin_proxy_20x20_0.6_l05_dense.json

---

## 1. Goal

Replace the coarse four-point Exp80 proxy with a denser perturbation-radius ladder, to see whether the local-basin return curve starts decaying within the tested range.

---

## 2. Results

| Sigma | Hits | Rate |
|---:|---:|---:|
| 0.005 | 12 / 12 | 1.0000 |
| 0.010 | 12 / 12 | 1.0000 |
| 0.020 | 12 / 12 | 1.0000 |
| 0.030 | 12 / 12 | 1.0000 |
| 0.050 | 12 / 12 | 1.0000 |
| 0.080 | 12 / 12 | 1.0000 |
| 0.100 | 12 / 12 | 1.0000 |
| 0.150 | 12 / 12 | 1.0000 |
| 0.200 | 12 / 12 | 1.0000 |

---

## 3. Main Finding

The return profile is flat at 100% across the entire tested ladder:

```text
sigma = 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20
```

So within the tested range, the local Type B basin is not merely present — it is **very robust**.

---

## 4. Interpretation

This makes the current asymmetry even sharper:

- raw starts at the same lambda almost never enter the family at strict thresholds (Exp79),
- but once the family is entered, even fairly large perturbations still flow back to it (Exp80 dense ladder).

Therefore the next bottleneck is no longer local basin sizing inside this tested range. The more informative next step is to understand the **access path** into that basin.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| local basin return starts decaying in the tested sigma range | not observed |
| basin-size scaling within the tested range adds more than access-path work right now | no |
| next quantitative step should move to access-path diagnostics | yes |

---

## 6. Next Trigger

Design an access-path diagnostic that compares how raw and seeded trajectories approach the target basin, rather than only measuring whether they return once already inside it.
