# d_min Derivation: Gap Analysis and Cat A Viability

**Date:** 2026-04-08
**Role:** Mathematical critic
**Source:** DMIN-FORMULA.md (792 lines), HONEST-RECOUNT.md #38
**Verdict:** Cat A upgrade is possible for a **qualitative bound**, not for the quantitative formula.

---

## 1. Tail Superposition Linearity

**Problem.** The formula assumes $u_{\mathrm{mid}} \approx u_{\mathrm{tail}_1} + u_{\mathrm{tail}_2}$ (Step 2, line 204). This uses linearity of the screened Poisson equation, which only holds when $u \ll 1$ (so $W'(u) \approx 2u$). The actual double-well has $W'(u) = 2u(1-u)(1-2u)$, giving cubic corrections:

$$W'(u) = 2u - 6u^2 + 4u^3$$

The superposition error is $O(u^2)$ where $u$ is the individual tail value. At the midpoint where merge is triggered, $u_{\mathrm{mid}} \approx u_{\mathrm{sp}} \approx 0.211$, so each tail contributes $\sim 0.1$. The nonlinear correction at $u = 0.1$ is $6u^2 = 0.06$, which is 60% of $2u = 0.2$. This is not a small correction.

**Severity:** Moderate. The superposition is qualitatively correct (two tails add up to raise the midpoint field) but quantitatively off by a factor that grows as the tails approach spinodal values. The direction of the error: nonlinearity makes the effective superposition *sub-additive* (W' grows slower than linearly), so $u_{\mathrm{mid}} < u_{\mathrm{tail}_1} + u_{\mathrm{tail}_2}$. This means the formula **underestimates** $d_{\min}^*$ — formations are actually more stable than predicted.

**Fix:** For a bound (not exact formula), this is actually favorable. Superposition gives an *upper bound* on $u_{\mathrm{mid}}$ and hence a *lower bound* on $d_{\min}^*$. A rigorous statement: $d_{\min}^* \geq (2/c_0)\ln(2A/u_{\mathrm{sp}})$ using the worst-case linear superposition. For a tighter bound, one could use the exact sub-additive correction via comparison principle arguments.

---

## 2. The Tail Amplitude A = 1/2

**Problem.** The document uses $A \leq 1$ with $A \approx 0.5$-$1.0$ (line 84, 206), calibrated by matching to the interface profile. The tanh profile $u(r) = \frac{1}{2}(1 - \tanh((r-R)/(2\varepsilon)))$ gives $u(R) = 1/2$ by symmetry. But the actual formation on a discrete grid deviates because:

(a) **Discrete lattice:** On $\mathbb{Z}^2$, the radial profile is not a smooth tanh. At small $R$ (formations spanning 3-5 nodes), the discrete step effects are $O(1/R)$, which is 20-33%.

(b) **Volume constraint:** The Lagrange multiplier $\nu$ shifts the effective potential asymmetrically. The minimizer of $\mathcal{E}_{\mathrm{bd}} + \nu \sum u_i$ on $\Sigma_m$ does not have the same profile as the unconstrained Allen-Cahn kink.

(c) **SCC core saturation:** The closure energy drives $u_{\mathrm{core}} \to 1$ (Lemma 10.2), which steepens the interface and changes $A$. The SCC profile is *not* a tanh — it's closer to a step function smeared by $\varepsilon_{\mathrm{int}}^{\mathrm{SCC}} < \varepsilon_{\mathrm{int}}^{\mathrm{AC}}$.

**Severity:** Moderate for the formula, minor for a bound. The value of $A$ shifts $d_{\min}^*$ additively by $(2/c_0)\ln(A_{\mathrm{true}}/A_{\mathrm{assumed}})$. If $A_{\mathrm{true}} = 0.7$ vs $A_{\mathrm{assumed}} = 0.5$, the shift is $\sim (2/2.83)\ln(1.4) \approx 0.24$ lattice units — significant at the scale of $d_{\min}^* \approx 3$-$7$.

**Fix:** For a bound, one can use $A \leq 1$ (worst case), which gives $d_{\min}^* \geq (2/c_0)\ln(2/u_{\mathrm{sp}})$. This is loose but rigorous. For a tighter bound, derive $A$ from the discrete Euler-Lagrange equation at the outermost interface node.

---

## 3. The $\beta_{\mathrm{eff}}$ Formula and the 100x Discrepancy

**Problem.** The document's §4-5 uses $\beta_{\mathrm{eff}} = \beta + 2\lambda_{\mathrm{cl}}(1 - j_{\mathrm{bdy}})^2$ from the T7-Enhanced single-site Gram boost. This predicts 0.3% d_min reduction (§5.4, line 414) while experiments show 30-45%. The document identifies this as a 100x error and resolves it via the "three-mechanism" analysis (§10).

**The resolution is physically correct but mathematically incomplete.** Here is why:

(a) The single-site analysis is not wrong — it correctly computes the Hessian boost at *one exterior site*. The error is in treating the merge instability as a single-site phenomenon. Merge is a *collective* mode involving $O(\ell_{\mathrm{eff}} \cdot L^{d-1})$ interface sites.

(b) The $\beta_{\mathrm{eff}}$ formula in §10.8 (line 747) uses the *same* single-site boost to define the SCC interface width $\varepsilon_{\mathrm{int}}^{\mathrm{SCC}} = \sqrt{2\alpha/\beta_{\mathrm{eff}}}$. But the interface width is determined by the *boundary-site* Jacobian $j_{\mathrm{bdy}}$ (where $u \sim 0.5$), not the exterior-site $j_0$ (where $u \sim 0$). At $u = 0.5$: $j_{\mathrm{bdy}} \approx a_{\mathrm{cl}}/8 = 0.375$, giving $(1 - j_{\mathrm{bdy}})^2 \approx 0.39$, so $\beta_{\mathrm{eff}} \approx 30 + 2 \times 0.39 = 30.78$. This is only a 2.6% increase over $\beta$, nowhere near enough to explain the observed effect.

(c) **The real mechanism (core saturation + mass redistribution) is proved qualitatively but not quantitatively.** The mass redistribution theorem (§10.3) proves $\bar{u}_{\mathrm{ext}}^{\mathrm{SCC}} < \bar{u}_{\mathrm{ext}}^{\mathrm{AC}}$ but the *amount* of reduction depends on the numerical profile.

**Severity:** Critical for the quantitative formula, non-issue for the qualitative bound. The 100x discrepancy reveals that the perturbative approach (linearized Hessian at a single site) misses the dominant physics. The §10 resolution correctly identifies core saturation as the dominant mechanism, but the final formula still uses $\beta_{\mathrm{eff}}$ to compute the SCC interface width — which only partially captures the effect.

**Fix:** The qualitative claim $d_{\min}^{\mathrm{SCC}} < d_{\min}^{\mathrm{AC}}$ (§10.6, line 716) is legitimately Cat A — it follows from the rigorous chain: T7-Enhanced (Hessian boost) + Theorem 10.3 (mass redistribution) + volume constraint. The quantitative formula cannot be Cat A without deriving $\bar{u}_{\mathrm{ext}}$ analytically with controlled error.

---

## 4. The $\bar{u}_{\mathrm{ext}}$ Formula (§10.8)

**Problem.** The formula $\bar{u}_{\mathrm{ext}} = 2c\varepsilon_{\mathrm{int}} / (R(1-c))$ uses volume balance (rigorous) but the tanh profile (approximate). The verification table (lines 769-773) shows:

| Grid | AC formula/actual | SCC formula/actual |
|------|-------------------|-------------------|
| 10x10 | 0.62x (underestimate) | 2.1x (overestimate) |
| 15x15 | 0.48x | 1.9x |
| 20x20 | 0.37x | 2.6x |

The errors are 2-3x and **diverge with grid size** for AC (0.62x → 0.37x). This is not a fixable discretization artifact — it's a structural problem with the continuum tanh approximation on finite discrete grids. Specifically:

(a) The tanh profile underestimates tail mass on a lattice because the discrete Laplacian has faster effective decay than the continuum one at short distances.

(b) The circular approximation $R = \sqrt{cn^2/\pi}$ assumes a round formation; on $\mathbb{Z}^2$, small formations are diamond-shaped (taxi-cab ball), changing the perimeter-to-area ratio.

(c) The SCC overestimate comes from $\beta_{\mathrm{eff}}$ being too conservative (see §3 above).

**Severity:** Critical for Cat A quantitative formula. The 2-3x error in $\bar{u}_{\mathrm{ext}}$ translates to an $O(1)$ error in $d_{\min}^*$ through the logarithm: $\Delta d_{\min} = (2/c_0)\ln(\text{error factor})$. For a 3x error: $(2/2.83)\ln(3) \approx 0.78$ lattice units — this is 15-25% of the typical $d_{\min}^* \sim 3$-$7$.

**Fix:** For a bound, one needs a *one-sided* estimate: either a rigorous upper bound on $\bar{u}_{\mathrm{ext}}^{\mathrm{AC}}$ or a rigorous lower bound on $\bar{u}_{\mathrm{ext}}^{\mathrm{SCC}}$. The volume balance argument gives $\bar{u}_{\mathrm{ext}} \leq c(1 - \alpha_{\mathrm{core}})/(1-c)$, and the core mass fraction $\alpha_{\mathrm{core}}$ can be bounded rigorously via the Euler-Lagrange equation. This is viable but requires careful discrete analysis.

---

## 5. Can d_min Be Cat A as a Bound?

**Yes, with significant caveats.** Here is the viable path:

### What can be proved (Cat A):

**Theorem (d_min bound).** For K formations on $\mathbb{Z}^2$ with the SCC energy, if the inter-formation distance satisfies:

$$d_{\min} \geq \frac{2}{c_0}\ln\left(\frac{2}{u_{\mathrm{sp}} - \bar{u}_{\mathrm{ext}}^{\mathrm{ub}}}\right)$$

where $\bar{u}_{\mathrm{ext}}^{\mathrm{ub}}$ is a rigorous upper bound on the exterior field level, then the K-formation configuration is a local minimum.

**Proof structure:**
1. Screened Poisson tail decay — **rigorous** (standard, line 562).
2. Linear superposition gives *upper bound* on midpoint field — **rigorous** (nonlinearity is sub-additive, see §1).
3. $u_{\mathrm{mid}} < u_{\mathrm{sp}} - \bar{u}_{\mathrm{ext}} \Rightarrow$ Hessian positive at midpoint — **rigorous** (direct computation).
4. Midpoint positivity + formation interior positivity (T7-Enhanced) $\Rightarrow$ full Hessian PD — **this is the gap**.

Gap (4) is the hard part: showing that the merge mode's instability is *entirely* determined by the midpoint Hessian sign. The document implicitly assumes this (single-site analysis), but the merge mode couples multiple sites. A rigorous version needs: either (a) a Perron-Frobenius argument showing the midpoint is the weakest link, or (b) a Gershgorin-type bound showing that the off-diagonal Hessian coupling cannot overwhelm the diagonal positivity.

Option (b) is feasible: the off-diagonal Hessian elements decay exponentially with distance (because the energy is local + exponentially decaying tails), so the Gershgorin radius at the midpoint is $O(\exp(-c_0))$, which is small compared to the diagonal element for $c_0 > 1$.

### What cannot be proved (Cat A):

- The specific coefficients 4.8, 0.31, 0.018 in the regression formula — these are pure curve-fits.
- The exact magnitude of the SCC reduction (30-45%) — this depends on $\bar{u}_{\mathrm{ext}}$ which requires numerical profile information.
- The $\bar{u}_{\mathrm{ext}}$ formula at better than 2-3x accuracy — the continuum-to-discrete gap is structural.

### Bottom line for Cat A upgrade:

The viable Cat A theorem is: **"For $d_{\min} \geq f(\beta, \alpha, a_{\mathrm{cl}})$ (explicit, conservative), K formations are metastable."** This is a *sufficient condition*, not a tight formula. The function $f$ will overestimate $d_{\min}^*$ by a factor of 2-3x because of the conservative bounds, but it would be fully rigorous.

---

## 6. The Regression Formula $4.8 + 0.31\sqrt{\beta/\alpha} - 0.018\beta/\alpha$

### Physical mechanism of each term:

**Constant 4.8:** This is the minimum lattice distance for two formations to have non-overlapping cores at *any* parameter values. On $\mathbb{Z}^2$, a single formation occupies a connected component of $\sim 4$-$9$ sites (radius $\sim 1$-$2$); two non-overlapping formations need $d \geq 2R + 1 \approx 3$-$5$. The value 4.8 is essentially this geometric floor. It could in principle be derived from the isoperimetric properties of the grid, but it depends on the volume fraction $c$ which is treated as fixed in the regression.

**$0.31\sqrt{\beta/\alpha}$:** This captures the interface-width contribution. The Allen-Cahn interface width is $\varepsilon = \sqrt{2\alpha/\beta}$, so $\sqrt{\beta/\alpha} \propto 1/\varepsilon$. As the interface sharpens ($\beta/\alpha$ grows), tails decay faster, so formations can be closer — but the $d_{\min}$ still grows because the *formation radius* also grows (sharper phase separation means more of the field is near 0 or 1, creating a larger "hard core"). The $\sqrt{\cdot}$ scaling comes from the competition between $c_0 \sim \sqrt{\beta/\alpha}$ (tail decay) and $R \sim (\beta/\alpha)^0$ (formation size is set by volume constraint, not sharpness).

**$-0.018\beta/\alpha$:** This is a second-order correction from the spinodal threshold shift. As $\beta/\alpha$ increases, $u_{\mathrm{crit}} \to u_{\mathrm{sp}}$ (the Laplacian correction becomes negligible), reducing the spinodal margin. The linear term in $\beta/\alpha$ arises from expanding $c_0 \sim \sqrt{\beta/\alpha}$ in the logarithmic formula at large $\beta/\alpha$.

### Can any coefficient be derived?

**4.8:** Partially. A geometric lower bound $d_{\min}^* \geq 2\lceil\sqrt{cn^2/\pi}\rceil + 1$ from formation non-overlap is derivable, but depends on $n$ and $c$, not just $\beta/\alpha$. The regression formula absorbs this dependence into the constant for the specific experimental grid sizes.

**0.31 and 0.018:** Not from current analysis. These encode the tail-decay/spinodal interplay at specific $(c, n, \lambda_{\mathrm{cl}})$ values. The analytical formula $(2/c_0)\ln(2A/\Delta_{\mathrm{sp}})$ gives the right functional form ($\sim 1/c_0 \sim 1/\sqrt{\beta/\alpha}$ for the dominant term), but the coefficients require knowing $A$ and $\Delta_{\mathrm{sp}}$ to the precision the regression achieves.

**Severity:** Critical for claiming these as "derived." They are curve-fits, period. The R² = 0.987 is good for engineering but irrelevant for mathematical proof.

---

## Summary Table

| Issue | Severity | Cat A viable? | What would fix it |
|-------|----------|---------------|-------------------|
| Tail superposition nonlinearity | Moderate | Yes (as upper bound) | Comparison principle argument |
| Tail amplitude A undetermined | Moderate | Yes (use A ≤ 1) | Conservative bound |
| β_eff 100x discrepancy | Critical (formula) | N/A for formula | §10 resolution is qualitative |
| ū_ext 2-3x error | Critical (formula) | Fixable for bound | One-sided discrete estimate |
| Midpoint → full Hessian gap | Critical (bound) | Fixable | Gershgorin + exponential decay |
| Regression coefficients | Critical | No | Cannot be derived |

## Recommendation

**Do not attempt Cat A for the quantitative formula.** The regression $4.8 + 0.31\sqrt{\beta/\alpha} - 0.018\beta/\alpha$ is empirical and should remain Cat B.

**Do attempt Cat A for a qualitative bound theorem** of the form:

> If $d_{\min} \geq C/c_0$ for an explicit constant $C$ depending on $(c, \lambda_{\mathrm{cl}}, a_{\mathrm{cl}})$, then K formations are metastable.

This requires closing one gap: the midpoint-to-full-Hessian step (Gershgorin argument). The remaining pieces (tail decay, superposition bound, core saturation, mass redistribution) are already proved or provable.

The qualitative ordering $d_{\min}^{\mathrm{SCC}} < d_{\min}^{\mathrm{AC}}$ is already **Cat A** per §10.6 — this should be stated as the headline result, with the quantitative formula as a Cat B supplement.
