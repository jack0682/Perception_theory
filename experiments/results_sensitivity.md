# Experiment 5: Parameter Sensitivity Analysis

**Date:** 2026-03-30
**Grid:** 15×15, n_restarts=2, max_iter=1000

## Result: ROBUST — 44/45 configurations have min_diag > 0.7

### Summary Table

| Parameter | Min | Max | Mean | All > 0.7? |
|-----------|-----|-----|------|-----------|
| a_cl [1.0, 3.9] | 0.704 | 0.889 | 0.811 | YES |
| eta_cl [0.1, 0.9] | 0.700 | 0.871 | 0.832 | borderline |
| tau_cl [0.3, 0.7] | 0.784 | 0.863 | 0.838 | YES |
| a_D [2.0, 12.0] | 0.812 | 0.867 | 0.853 | YES |
| w_cl [0.0, 5.0] | 0.743 | 0.868 | 0.840 | YES |
| w_sep [0.0, 5.0] | 0.721 | 0.869 | 0.838 | YES |
| w_bd [0.5, 10.0] | 0.858 | 0.867 | 0.863 | YES |
| beta_bd [5, 100] | 0.849 | 0.870 | 0.858 | YES |
| volume_fraction [0.25, 0.75] | 0.763 | 0.884 | 0.848 | YES |

### Key Findings

1. **Formation quality is ROBUST to parameter choice.** Across 45 configurations sweeping 9 parameters over wide ranges, only 1 configuration drops below 0.7 (eta_cl=0.1, min_diag=0.700).

2. **Most insensitive parameters:** w_bd and beta_bd — formation quality barely changes across 20× range. This confirms the double-well's robustness.

3. **Most sensitive parameters:** a_cl and eta_cl — these control closure operator behavior. Low a_cl (weak closure) degrades Bind. Extreme eta_cl (too much/too little neighbor influence) reduces Sep.

4. **Energy weights (w_cl, w_sep, w_bd):** All tolerate wide ranges. Even w_cl=0 or w_sep=0 gives min_diag > 0.7. Only extreme w_cl=5.0 degrades Sep (0.743).

5. **Volume fraction:** Robust across full spinodal range (0.25-0.75). Slightly weaker at 0.75 (Inside=0.763) — near spinodal boundary.

### Conclusion

**The theory is NOT hand-tuned.** Formation quality is structurally stable across wide parameter ranges. The only constraint that matters is the theoretical one: a_cl < 4 for contraction. Within the admissible parameter space, quality varies by ~15% but never collapses.

This addresses criticism W3: "researcher chooses a regime where structure appears" is refuted — structure appears across virtually the entire admissible parameter space.
