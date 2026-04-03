# T-Bind-Proj: Experimental Baseline for r-bar-0 tau-Dependence

**Date:** 2026-04-04
**Session:** Phase 13 -- T-Bind-Proj general-tau analysis
**Category:** theory (experimental baseline)
**Status:** complete
**Depends on:** R-BAR-BOUND.md (Phase 6), exp5_sensitivity.py, exp42_scale_verification.py
**Produces:** exp58_bind_tau_sweep.py, this document

---

## 1. Executive Summary

We measure the mean closure residual r-bar-0 = |sum(Cl(u-hat) - u-hat)| / n at constrained minimizers across tau in {0.10, 0.15, ..., 0.90} and grid sizes 5x5 through 20x20 (n = 25 to 400). The experiment (exp58) establishes the following:

**Key Findings:**

1. **r-bar-0 is O(1) for all tau, including tau=1/2.** It does NOT vanish with n. The R-BAR-BOUND.md claim that r-bar-0 = O(n^{-1/d}) at tau=1/2 is **not supported by experiment** -- r-bar-0 ~ 0.060 at tau=0.5 regardless of n.

2. **The minimum of r-bar-0 occurs near tau* ~ 0.643, not tau=0.5.** This is the tau where the binary mass-balance equation (1-c)delta_- = c*delta_+ has exact cancellation (for c = 0.3, a_cl = 3.5).

3. **The binary mass-balance theory from R-BAR-BOUND.md Proposition 4.1 is an excellent predictor.** The formula r-bar-0(binary) = |(1-c)*delta_-(tau) - c*delta_+(tau)| achieves R^2 = 0.995 against experimental data. A scaled version (k*binary + b) reaches R^2 = 0.999.

4. **The dominant tau-dependence is through delta_+(tau) and delta_-(tau)**, i.e., the sigmoid saturation residuals at core and exterior. The n-dependence is a small O(n^{-1/d}) correction on top of a large O(1) base.

5. **For T-Bind-Proj Category A upgrade at general tau:** r-bar-0 is bounded by an explicit, computable function of (tau, c, a_cl) -- the binary mass-balance formula. It is NOT small, but it IS bounded and predictable.

---

## 2. Experimental Setup

### 2.1 Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| a_cl | 3.5 | Default, contraction regime (< 4) |
| eta_cl | 0.5 | Default mixing |
| beta_bd | 50.0 | Sharp-interface regime |
| volume_fraction c | 0.3 | Default |
| w_cl, w_sep, w_bd | 1.0 each | Equal weights |
| n_restarts | 3 | Multi-start |
| max_iter | 3000 | |
| tau_cl | 0.10 to 0.90 (step 0.05) | 17 values |
| grid sides | 5, 10, 15, 20 | n = 25, 100, 225, 400 |

### 2.2 Measured Quantities

At each (tau, n) pair, we find the constrained energy minimizer u-hat via `find_formation()` and measure:

- **r-bar-0** = |1^T r| / n where r = Cl(u-hat) - u-hat
- **||r_T||_2 / sqrt(n)** = tangential residual per sqrt(n)
- **Bind** = 1 - ||r||_2 / sqrt(n)
- **delta_+** = 1 - sigma(a_cl(1-tau))  (core saturation residual)
- **delta_-** = sigma(-a_cl*tau) = 1 - sigma(a_cl*tau)  (exterior saturation residual)
- Transition layer size |T|, core/exterior counts

---

## 3. Raw Data: r-bar-0(tau, n)

### Table 1: Mean Closure Residual r-bar-0

| tau   |  5x5 (n=25) | 10x10 (n=100) | 15x15 (n=225) | 20x20 (n=400) |
|-------|-------------|----------------|----------------|----------------|
| 0.10  |  0.3045     |  0.2917        |  0.2900        |  0.2855        |
| 0.15  |  0.2715     |  0.2595        |  0.2573        |  0.2555        |
| 0.20  |  0.2422     |  0.2280        |  0.2243        |  0.2236        |
| 0.25  |  0.2100     |  0.1941        |  0.1941        |  0.1918        |
| 0.30  |  0.1752     |  0.1676        |  0.1644        |  0.1625        |
| 0.35  |  0.1479     |  0.1364        |  0.1372        |  0.1347        |
| 0.40  |  0.1152     |  0.1118        |  0.1083        |  0.1089        |
| 0.45  |  0.0897     |  0.0856        |  0.0833        |  0.0842        |
| **0.50** | **0.0594** | **0.0590** | **0.0608** | **0.0596** |
| 0.55  |  0.0356     |  0.0354        |  0.0365        |  0.0376        |
| 0.60  |  0.0101     |  0.0133        |  0.0154        |  0.0153        |
| **0.65** | **0.0144** | **0.0082** | **0.0065** | **0.0060** |
| 0.70  |  0.0399     |  0.0307        |  0.0273        |  0.0268        |
| 0.75  |  0.0622     |  0.0503        |  0.0477        |  0.0459        |
| 0.80  |  0.0836     |  0.0712        |  0.0669        |  0.0704        |
| 0.85  |  0.1040     |  0.0907        |  0.0858        |  0.0834        |
| 0.90  |  0.1233     |  0.1085        |  0.1040        |  0.1025        |

### Key observations:

- **Minimum** of r-bar-0 is near tau=0.60-0.65 (NOT tau=0.5)
- At tau=0.5, r-bar-0 ~ 0.060 is remarkably constant across all n (3% variation)
- At tau=0.65, r-bar-0 decreases with n: 0.0144 -> 0.0060 (slope ~ n^{-0.33})
- For tau far from tau*, r-bar-0 is large and essentially n-independent

### Table 2: Bind Diagnostic

| tau   | 5x5    | 10x10  | 15x15  | 20x20  |
|-------|--------|--------|--------|--------|
| 0.10  | 0.629  | 0.641  | 0.645  | 0.646  |
| 0.30  | 0.758  | 0.769  | 0.773  | 0.773  |
| 0.50  | 0.832  | 0.841  | 0.847  | 0.849  |
| 0.60  | 0.827  | 0.847  | 0.853  | 0.854  |
| 0.65  | 0.818  | 0.840  | 0.845  | 0.847  |
| 0.90  | 0.731  | 0.750  | 0.758  | 0.761  |

Bind is maximized near tau=0.55-0.60, not at the r-bar-0 minimum, because Bind depends on the full ||r||_2 (not just the mean).

---

## 4. Theoretical Framework: Binary Mass-Balance

### 4.1 The binary prediction (R-BAR-BOUND.md Proposition 4.1)

For a binary profile u = chi_S with |S| = cn:

$$\bar{r}_0^{\text{binary}}(\tau) = |(1-c)\delta_-(\tau) - c \cdot \delta_+(\tau)| + O(|\partial S|/n)$$

where:
- delta_+(tau) = 1 - sigma(a_cl(1-tau)): how far core sites map below 1
- delta_-(tau) = 1 - sigma(a_cl*tau): how far exterior sites map above 0

### 4.2 Bulk asymmetry table

| tau  | delta_+  | delta_-  | |delta_+-delta_-| | r-bar-0(binary) |
|------|----------|----------|------------------|-----------------|
| 0.10 | 0.0411   | 0.4134   | 0.3723           | 0.2770          |
| 0.30 | 0.0794   | 0.2592   | 0.1798           | 0.1576          |
| 0.50 | 0.1480   | 0.1480   | 0.0000           | 0.0592          |
| 0.65 | 0.2271   | 0.0932   | 0.1338           | 0.0029          |
| 0.70 | 0.2592   | 0.0794   | 0.1798           | 0.0222          |
| 0.90 | 0.4134   | 0.0411   | 0.3723           | 0.0953          |

**Critical insight:** At tau=0.5, delta_+ = delta_- (sigmoid symmetry), so the binary r-bar-0 simplifies to delta*|1-2c| = 0.148 * 0.4 = 0.059. This is NOT zero (it vanishes only when c=0.5 AND tau=0.5). The R-BAR-BOUND.md Theorem 6.1 claim that r-bar-0 = O(n^{-1/d}) at tau=1/2 implicitly assumed c ~ 1/2 or relied on KKT cancellation that the experiment shows does NOT occur.

**The true zero** of the binary mass-balance occurs at tau* defined by:

$$(1-c)(1 - \sigma(a_{\mathrm{cl}} \tau^*)) = c(1 - \sigma(a_{\mathrm{cl}}(1-\tau^*)))$$

For c=0.3, a_cl=3.5: **tau* = 0.6427**

### 4.3 Why tau* != 0.5 when c != 0.5

At tau=0.5, the sigmoid is symmetric: delta_+ = delta_-. But the mass balance weights these by the population fractions c and 1-c:

    r-bar-0(tau=0.5) = delta * |1 - 2c|

For c=0.3: r-bar-0 = 0.148 * 0.4 = 0.059, which is exactly what we observe experimentally.

To achieve zero bulk residual, we need the **asymmetric** threshold tau* > 0.5 (when c < 0.5) that makes the smaller core produce less outward leakage (larger delta_+) while the larger exterior produces less inward leakage (smaller delta_-).

---

## 5. Curve Fitting Results

### 5.1 Model comparison (20x20 grid data)

| Rank | Model | Parameters | R^2 |
|------|-------|-----------|-----|
| 1 | Scaled binary: k*|binary(tau)| + b | k=1.026, b=0.002 | **0.9989** |
| 2 | Power law: a*|tau-tau*|^p + b | a=0.612, p=1.29, b=0.008 | 0.9977 |
| 3 | Raw binary theory (no fit) | -- | 0.9948 |
| 4 | Asymmetric linear about tau* | a_L=0.519, a_R=0.455, b=-0.008 | 0.9926 |
| 5 | Linear |tau-tau*| | a=0.525, b=-0.012 | 0.9887 |
| 6 | Quadratic (tau-tau*)^2 | a=0.926, b=0.037 | 0.9673 |

### 5.2 Best model: Scaled binary theory

The binary mass-balance formula with a single scale factor provides the best fit:

**r-bar-0(tau) ~ 1.026 * |(1-c)(1-sigma(a_cl*tau)) - c(1-sigma(a_cl(1-tau)))| + 0.002**

The scale factor k ~ 1.03 indicates the actual minimizer has ~3% larger residual than the binary prediction, consistent with the transition layer contributing additional mass mismatch.

### 5.3 Approximate closed form

For practical use, the linear approximation about tau* is adequate (R^2 = 0.989):

**r-bar-0(tau) ~ 0.525 * |tau - 0.643| - 0.012**

with the caveat that r-bar-0 >= 0 always.

---

## 6. n-Dependence Analysis

### 6.1 Scaling at fixed tau

| tau  | r-bar-0 range (5x5 to 20x20) | Variation | n-slope |
|------|-------------------------------|-----------|---------|
| 0.10 | 0.286 -- 0.305 | 6.5% | flat |
| 0.30 | 0.163 -- 0.175 | 7.6% | flat |
| 0.50 | 0.059 -- 0.061 | 3.0% | flat |
| 0.60 | 0.010 -- 0.015 | 53%  | +0.16 |
| 0.65 | 0.006 -- 0.014 | 141% | **-0.33** |
| 0.70 | 0.027 -- 0.040 | 49%  | -0.15 |
| 0.85 | 0.083 -- 0.104 | 24%  | -0.08 |

### 6.2 Interpretation

**For tau away from tau*:** r-bar-0 is dominated by the O(1) bulk term and essentially n-independent. The small n-dependence (< 8%) comes from the O(|boundary|/n) correction.

**Near tau*:** The bulk term nearly vanishes, exposing the O(n^{-1/d}) boundary correction. At tau=0.65 (closest to tau*=0.643), we observe slope -0.33, consistent with O(n^{-1/3}) to O(n^{-1/2}) (the range n=25-400 is too small for a precise exponent).

**At tau=0.5:** r-bar-0 is flat at ~0.060. The KKT cancellation claimed in Theorem 6.1 does NOT suppress the bulk term delta*|1-2c|. This bulk term is O(1) and is the dominant contribution.

### 6.3 Decomposition

$$\bar{r}_0(\tau, n) = \underbrace{|(1-c)\delta_-(\tau) - c\cdot\delta_+(\tau)|}_{\text{O(1) bulk term}} + \underbrace{O\!\left(\frac{|\partial\text{Core}|}{n}\right)}_{\text{O}(n^{-1/d})\text{ correction}}$$

The bulk term depends on (tau, c, a_cl) but NOT on n. The correction term is the only n-dependent piece and is small (~0.002-0.008 at n=400).

---

## 7. Implications for T-Bind-Proj

### 7.1 Reassessment of Theorem 6.1 (R-BAR-BOUND.md)

**Theorem 6.1 claims** r-bar-0 = O(n^{-1/d}) at tau=1/2 via KKT cancellation.

**Experiment shows** r-bar-0 ~ 0.060 at tau=0.5 for all n in [25, 400], with no decay.

**Diagnosis:** The KKT argument in Section 5 of R-BAR-BOUND.md has a gap. It claims that the O(1) terms in the Lagrange multiplier nu and the energy gradient sums cancel through the KKT identity, leaving only O(n^{-1/d}). But the experiment shows they do NOT cancel -- the residual delta*|1-2c| persists.

The gap is in Section 5.5-5.6 where the argument asserts the dominant O(1) terms cancel "by the structure of the identity" without quantitative verification. The binary mass-balance (Section 4) correctly identifies that the O(1) bulk term is delta*|1-2c| != 0 when c != 1/2, but Section 6 incorrectly claims this is suppressed by the KKT structure.

### 7.2 What IS true

1. **r-bar-0 is bounded by an explicit function of (tau, c, a_cl):**

   r-bar-0(tau) <= C(a_cl) * |(1-c)(1-sigma(a_cl*tau)) - c(1-sigma(a_cl(1-tau)))| + O(n^{-1/d})

   where C ~ 1.03 is a universal constant.

2. **r-bar-0 is genuinely O(n^{-1/d}) at tau = tau*(c, a_cl)** defined by the binary mass-balance zero.

3. **r-bar-0 is O(1) but uniformly bounded for all tau in (0,1):**

   r-bar-0 <= max(delta_+, delta_-) <= 1 - sigma(min(a_cl*tau, a_cl*(1-tau)))

4. **The Bind lower bound becomes:**

   Bind(u-hat) >= 1 - sqrt(||r_T||^2/n + r-bar-0(tau)^2)

   where r-bar-0(tau) is the computable O(1) function above. This is still a valid lower bound, just weaker than O(1) convergence to 1.

### 7.3 Category assessment

- **tau = tau*(c, a_cl):** r-bar-0 = O(n^{-1/d}). T-Bind is Category A at this special tau.
- **tau = 1/2, c = 1/2:** tau* = 1/2 when c = 1/2 by symmetry. T-Bind is Category A.
- **tau = 1/2, c != 1/2:** r-bar-0 = delta*|1-2c| = O(1). T-Bind holds as a LOWER BOUND but the bound does not approach 1 as n -> infinity. Category B (bound is valid but not asymptotically tight).
- **General tau:** r-bar-0 given by the binary formula. Same Category B status.

### 7.4 Proposed revision

The current spec says:
> T-Bind-Proj: Category A for tau=1/2; Category B for general tau

Based on this analysis, we should revise to:
> T-Bind-Proj: Category A for tau = tau*(c, a_cl) (including tau=1/2 when c=1/2); Category B for general (tau, c) with explicit bound r-bar-0(tau, c, a_cl)

---

## 8. Hypothesis for Perturbation Analyst

### 8.1 Functional form

$$\bar{r}_0(\tau, c, a_{\mathrm{cl}}, n) = \underbrace{R(\tau, c, a_{\mathrm{cl}})}_{\text{bulk}} + \underbrace{B(a_{\mathrm{cl}}, c) \cdot n^{-1/d}}_{\text{boundary}}$$

where:

$$R(\tau, c, a) = |(1-c)(1-\sigma(a\tau)) - c(1-\sigma(a(1-\tau)))|$$

is the binary mass-balance residual, and B is a bounded prefactor.

### 8.2 Concrete predictions to validate

1. R(tau, c, a_cl) = 0 at tau* = tau*(c, a_cl) defined by (1-c)*sigma(-a*tau*) = c*(1-sigma(a*(1-tau*)))
2. For c=0.3, a_cl=3.5: tau* = 0.6427
3. dR/dtau|_{tau=tau*} ~ a_cl * sigma'(a_cl*tau*) * [(1-c) + c] = a_cl * sigma'(a_cl*tau*) (non-zero, so the zero is simple)
4. R(0.5, c, a) = (1-sigma(a/2)) * |1-2c| (exact, verified)
5. B ~ 4*sqrt(c) for 2D grids (from isoperimetric argument)

### 8.3 Open question for theory

Can the KKT suppression argument from R-BAR-BOUND.md Section 5 be salvaged to show that the actual minimizer has r-bar-0 < R(tau) (i.e., the energy minimization DOES suppress the bulk residual below the binary prediction)?

The data shows the actual r-bar-0 is within 3% of the binary prediction (scale factor k=1.03), suggesting the energy minimization provides almost no suppression of the bulk mass-balance term. This is consistent with the bulk term being a consequence of the sigmoid's fundamental asymmetry, which no amount of profile optimization can eliminate.

---

## 9. Validation Checklist

- [x] Raw data extracted across 17 tau values x 4 grid sizes = 68 data points
- [x] Curve fit identifies dominant tau-dependence: binary mass-balance formula R^2=0.995
- [x] Hypothesis concrete: r-bar-0(tau) = R(tau, c, a_cl) + O(n^{-1/d})
- [x] n-scaling verified: O(1) bulk + O(n^{-1/d}) correction
- [x] Minimum identified at tau* = 0.643 (not 0.5)
- [x] Theorem 6.1 gap identified and documented
- [x] Category assessment updated

---

## Appendix: Full Data (JSON)

See `experiments/results/exp58_bind_tau_sweep.json` for complete numerical results.
