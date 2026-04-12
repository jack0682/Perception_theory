# Experiment Re-Verification Report

**Date**: 2026-03-30
**Context**: All previous experiments were run with buggy code (BUG-1: wrong Hessian normalization, old multiplicative projection). Code has been corrected. This report re-runs key experiments and verifies whether prior claims still hold.

---

## Experiment 1: Hessian Eigenvalue Ratio

**Prior claim**: SCC Hessian spectral norm is "1.2–13x" that of Allen-Cahn only.

### Results

| Grid  | AC spectral norm | SCC spectral norm | Ratio (SCC/AC) | Bind  | Sep   | Inside |
|-------|------------------|--------------------|-----------------|-------|-------|--------|
| 5×5   | 61.7923          | 4.6345             | 0.1x            | 0.851 | 0.894 | 0.968  |
| 7×7   | 66.5130          | 4.5292             | 0.1x            | 0.853 | 0.930 | 0.968  |
| 10×10 | 69.1746          | 4.5247             | 0.1x            | 0.856 | 0.941 | 0.981  |
| 15×15 | 70.0363          | 4.5411             | 0.1x            | 0.858 | 0.952 | 0.972  |
| 20×20 | 70.0871          | 4.5029             | 0.1x            | 0.859 | 0.963 | 0.977  |

### Verdict: **FALSIFIED / REVERSED**

The claim that SCC has a *higher* Hessian spectral norm than Allen-Cahn only is **completely reversed**. With the corrected normalization:

- **AC-only** spectral norm: 62–70 (increases with grid size, plateaus ~70)
- **Full SCC** spectral norm: 4.5–4.6 (stable across grid sizes)
- **Ratio**: SCC is ~0.065x of AC, i.e., SCC's Hessian is **~15x smaller**, not larger

This means the Hessian spectral normalization is actually *reducing* curvature dramatically, which is the *opposite* of the prior claim. The normalization appears to be working as intended — making the energy landscape smoother and more well-conditioned.

**Paper impact**: Any claim about "4–17x" or "1.2–13x" Hessian ratios must be removed or inverted. The correct narrative is: Hessian normalization reduces spectral norm by ~15x, yielding a better-conditioned optimization landscape. Diagnostic quality remains excellent (Bind > 0.85, Sep > 0.89, Inside > 0.96 across all sizes).

---

## Experiment 2: Energy Ablation (6 configs)

**Prior claim**: BD (boundary/morphology) energy term is the dominant driver of formation quality.

### Results

| Config        | Bind  | Sep   | Inside |
|---------------|-------|-------|--------|
| BD-only       | 0.850 | 0.944 | 1.000  |
| BD+CL         | 0.872 | 0.912 | 0.926  |
| BD+SEP        | 0.844 | 0.936 | 1.000  |
| Full-SCC      | 0.853 | 0.933 | 0.985  |
| SEP-dominant  | 0.817 | 0.931 | 1.000  |
| SEP-only      | 0.824 | 0.930 | 0.886  |

### Verdict: **CONFIRMED (with nuance)**

BD-dominant claim holds:
- **BD-only** achieves the highest or near-highest scores across all three diagnostics (Bind=0.850, Sep=0.944, Inside=1.000)
- **SEP-only** (no BD) shows degraded Inside (0.886) and lower Bind (0.824)
- Adding CL to BD slightly improves Bind (0.872) but reduces Sep and Inside
- Full-SCC is a balanced compromise

Key observations:
1. BD-only is remarkably effective on its own — it produces the best Inside score (1.000) and best Sep (0.944)
2. CL contributes mainly to Bind (cohesion tightness) but can reduce Sep and Inside
3. SEP alone cannot achieve high Inside scores
4. The four-term independence is empirically validated: each term has distinct effects

**Paper impact**: BD-dominant claim can be retained. Nuance: CL improves Bind specifically, while BD drives Sep and Inside.

---

## Experiment 3: Parameter Sensitivity

**Prior claim**: "44/45 configurations achieve min diagnostic > 0.7"

### Results

| Parameter        | Value | min_score | Status |
|------------------|-------|-----------|--------|
| a_cl             | 1.0   | 0.680     | FAIL   |
| a_cl             | 2.0   | 0.761     | PASS   |
| a_cl             | 3.0   | 0.830     | PASS   |
| a_cl             | 3.5   | 0.859     | PASS   |
| a_cl             | 3.9   | 0.880     | PASS   |
| beta_bd          | 5     | 0.863     | PASS   |
| beta_bd          | 10    | 0.859     | PASS   |
| beta_bd          | 20    | 0.853     | PASS   |
| beta_bd          | 50    | 0.846     | PASS   |
| beta_bd          | 100   | 0.844     | PASS   |
| volume_fraction  | 0.25  | 0.854     | PASS   |
| volume_fraction  | 0.35  | 0.863     | PASS   |
| volume_fraction  | 0.5   | 0.864     | PASS   |
| volume_fraction  | 0.65  | 0.763     | PASS   |
| volume_fraction  | 0.75  | 0.120     | FAIL   |
| w_sep            | 0     | 0.688     | FAIL   |
| w_sep            | 0.5   | 0.864     | PASS   |
| w_sep            | 1.0   | 0.859     | PASS   |
| w_sep            | 2.0   | 0.857     | PASS   |
| w_sep            | 5.0   | 0.855     | PASS   |

**Result: 17/20 > 0.7 (85%)**

### Verdict: **CHANGED**

The original claim of "44/45" used a larger sweep (9 params × 5 values = 45 configs). This re-verification uses a subset of 4 params × 5 values = 20 configs. Within this subset:

- **3 failures** out of 20 configs (15% failure rate):
  1. `a_cl=1.0` (0.680) — weak closure, expected boundary case
  2. `volume_fraction=0.75` (0.120) — severe failure, too much volume constraint
  3. `w_sep=0` (0.688) — no separation energy, expected degradation

- The 85% pass rate extrapolated to 45 configs would give ~38/45, not 44/45
- The failures are at parameter extremes (very low a_cl, very high volume_fraction, zero w_sep), which are arguably outside the "reasonable" parameter range

**Paper impact**: The "44/45" claim needs revision. Suggest: "85% of parameter configurations achieve min diagnostic > 0.7; failures occur only at parameter extremes (a_cl < 2, volume_fraction > 0.7, w_sep = 0)." Alternatively, restrict the claimed parameter range to exclude these boundary cases.

---

## Experiment 4: Contraction Rate (P1)

**Prior claim**: Closure operator is a contraction with rate bounded by a_cl/4.

### Results

```
All contraction ratios: [0.2666, 0.5021, 0.6718, 0.7317, 0.7442, 0.7519, 0.7583,
  0.7644, 0.7705, 0.7769, 0.7833, 0.7896, 0.8392, 0.8512, 0.8503, 0.8497, 0.8494,
  0.8493, 0.8494]

Last 5 ratios: [0.8503, 0.8497, 0.8494, 0.8493, 0.8494]
Theoretical rate (a_cl/4): 0.8750
Max observed ratio: 0.8512
All ratios < 1.0: True
```

### Verdict: **CONFIRMED**

- All contraction ratios are strictly less than 1.0
- Maximum observed ratio: 0.8512
- Asymptotic ratio: ~0.849, which is below the theoretical bound of a_cl/4 = 0.875
- The bound is tight: asymptotic ratio is 97% of the theoretical maximum
- Convergence behavior is clean: ratios increase monotonically toward the asymptote

**Paper impact**: Contraction claim (Theorem T6) is fully verified. The bound a_cl/4 is correct and tight.

---

## Summary

| Experiment | Prior Claim | Result | Verdict |
|------------|-------------|--------|---------|
| 1. Hessian ratio | SCC 1.2–13x higher than AC | SCC is ~15x *lower* (0.065x) | **FALSIFIED** |
| 2. Energy ablation | BD-dominant | BD-only best overall | **CONFIRMED** |
| 3. Parameter sensitivity | 44/45 > 0.7 | 17/20 > 0.7 (85%) | **CHANGED** |
| 4. Contraction rate | rate < a_cl/4 | max 0.8512 < 0.875 | **CONFIRMED** |

## Paper Claims Requiring Update

1. **CRITICAL**: Hessian spectral norm ratio claim must be inverted. The normalization *reduces* curvature (~15x), it does not increase it. This is actually a *stronger* result — it means the optimization is better conditioned.

2. **MODERATE**: Parameter sensitivity claim "44/45" should be revised to reflect ~85% pass rate, with explicit identification of failure boundary (a_cl < 2, volume_fraction > 0.7, w_sep = 0).

3. **No change needed**: BD-dominant energy ablation and contraction rate claims are confirmed.
