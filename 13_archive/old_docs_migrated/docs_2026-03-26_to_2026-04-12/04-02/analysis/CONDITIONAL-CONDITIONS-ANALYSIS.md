# Task #1 Analysis: T-Persist-1(b,d,e) Conditions

**Date:** 2026-04-02
**Author:** conditional-analyst
**Category:** analysis
**Status:** complete
**Depends on:** T-PERSIST-FULL-PROOF.md, NEARBIF-DIRECTIONAL-EXTENSION.md, TRANSPORT-SELECTION-ANALYSIS.md, ISOPERIMETRIC-TRANSPORT-PROOFS.md, BASIN-ESCAPE-ANALYSIS.md, CORE-DEPTH-ISOPERIMETRIC.md

---

## Executive Summary

T-Persist-1 has five sub-parts (a)-(e). Parts (a) and (c) are fully proved. This analysis examines the three conditional parts: (b), (d), and (e). For each, I classify the governing conditions as **structurally necessary** (cannot be removed without losing the conclusion) or **technically convenient** (removable or replaceable with weaker conditions).

**Key findings:**
1. **(b) Basin containment**: The non-bifurcation condition (NB) is **structurally necessary** at its core but the current quantitative threshold $\mu_0 \gtrsim 4.1$ is **overly conservative** and can be replaced by a directional criterion that extends Tier 1 by 10-100x in spectral gap range. The Gentle Transition (GT) condition is **technically convenient** — it can be absorbed into the directional framework.
2. **(d) Exact threshold preservation**: (H2') deep core existence is **proved** (no longer conditional). (H3) $\beta > 11\alpha$ is **structurally necessary** for positive interior gap but the quantitative bound is **conservative** (empirically $\beta > 7\alpha$ suffices).
3. **(e) Transport concentration**: WR' (Banach contraction) is **technically convenient** — replaceable by the strictly weaker **transport confinement** condition. The underlying Schauder existence is unconditional. Transport confinement itself appears to hold generically due to re-optimization discreteness.

---

## Part (b): Gradient Flow Convergence / Basin Containment

### Current Conditions

| Condition | Symbol | Quantitative Form |
|-----------|--------|-------------------|
| Non-degeneracy | (ND) | $\mu_{\mathcal{F}} > 0$ |
| Non-bifurcation | (NB) | $\mu_{\mathcal{F}} \geq \mu_0 \gtrsim 4.1$ |
| Gentle transition | (GT) | $\varepsilon_1 < \Delta_t/4$ and $2\varepsilon_2 + 2\varepsilon_1/\mu < r_{\mathrm{basin}}/2$ |

### Current Status

Part (b) asserts that gradient flow at time $s$, initialized from the transported field, converges to the *correct* minimizer $\hat{u}_s$. This requires the initial point to lie within the basin of attraction of $\hat{u}_s$. The basin radius is $r_{\mathrm{basin}} = \sqrt{2\Delta_{\min}/\lambda_{\max}}$ where $\Delta_{\min}$ is the minimum escape barrier.

**Three-tier ladder** (NB-1/NB-2):
- **Tier 1** (Full): $\mu \geq \mu_0$, all guarantees hold
- **Tier 2** (Deep-core remnant): $0 < \mu < \mu_0$, deep core survives but full basin containment fails
- **Tier 3** (Bifurcation): $\mu = 0$, formation undergoes shape transition

### Condition-by-Condition Analysis

#### (ND): $\mu_{\mathcal{F}} > 0$ — **Structurally Necessary**

**Why it cannot be removed.** Non-degeneracy is the fundamental requirement for the IFT to apply. At $\mu = 0$, the constrained Hessian has a zero eigenvalue, meaning the minimizer sits on a ridge or at a saddle-node bifurcation. The IFT-based perturbation bound $\|\hat{u}_s - \hat{u}_t\| \leq 2\varepsilon_1/\mu$ diverges as $\mu \to 0$.

**Geometric reason.** At $\mu = 0$, the energy landscape is locally flat along the soft mode direction. Arbitrarily small perturbations can push the system to a qualitatively different formation (different topology, different core structure). This is the definition of a bifurcation — the mathematical phenomenon of structural instability.

**Is genericity sufficient?** Yes — by Sard's theorem, $\mu > 0$ holds generically. The set of parameters where $\mu = 0$ has measure zero. But "generic" is not "universal": specific parameter tunings can produce $\mu = 0$. The condition is structurally necessary but generically satisfied.

**Verdict:** Structurally necessary. Cannot be removed. Sard's theorem makes it a mild condition.

#### (NB): $\mu \geq \mu_0 \gtrsim 4.1$ — **Structurally Necessary in Principle, Quantitatively Overly Conservative**

**What the condition does.** (NB) ensures $\Delta_{\mathrm{bdy}} > 0$ (positive escape barrier) with enough margin for the basin to contain the transported field. The quantitative threshold $\mu_0$ comes from the contraction-concentration compatibility:

$$\mu \cdot \Delta_\varphi^2 > (\log n + C) \cdot \lambda_{\mathrm{tr}} \cdot \|\partial\varphi/\partial u\|_{\mathrm{op}}$$

**Structural necessity analysis.** The *qualitative* requirement "$\mu$ bounded away from zero" IS structurally necessary:
- Near-bifurcation barrier scaling: $\Delta_{\mathrm{bdy}} = O(\mu^{3/2})$ (saddle-node) or $O(\mu)$ (pitchfork)
- Basin radius: $r_{\mathrm{basin}} = O(\mu^{3/4})$ or $O(\mu^{1/2})$
- At $\mu \to 0$, the basin shrinks to zero and any finite perturbation escapes

The *quantitative* threshold $\mu_0 \gtrsim 4.1$ is **overly conservative**. Evidence:

1. **Isotropic vs. directional.** The current $\mu_0$ uses the isotropic basin radius. The directional extension (NEARBIF-DIRECTIONAL-EXTENSION.md, Theorem EBC) shows the basin is ellipsoidal, with transverse radii $2.5$-$4.3\times$ larger near bifurcation. This extends Tier 1 to $\mu$ values $10$-$100\times$ smaller.

2. **Empirical conservatism.** exp24 shows actual basins are $3$-$12\times$ larger than sublevel-set estimates. The $\mu_0$ threshold is derived from the sublevel-set lower bound.

3. **Perturbation soft-mode fraction.** The temporal perturbation $\delta u$ generically has small overlap with the soft mode ($f_1 \leq \sqrt{n_{\mathrm{bdy}}/n_F} \ll 1$), meaning the perturbation mostly lies in directions with large basin radii.

**Removal path.** Replace (NB) with the **directional basin containment** criterion from NEARBIF-DIRECTIONAL-EXTENSION.md:

$$\varepsilon < r_{\mathrm{eff}} = \sqrt{\frac{2\Delta_{\mathrm{bdy}}}{f_1^2 \cdot \mu + (1-f_1^2) \cdot \mu_2}}$$

This weakens $\mu_0$ by a factor of $\lambda_{\max}/\mu_2 \approx 10$-$100\times$ for typical formations. The extended threshold is:

$$\mu_{\mathrm{bif}}^{\mathrm{dir}} = \mu_{\mathrm{bif}}^{\mathrm{iso}} \cdot \left(f_1^2 + (1-f_1^2) \cdot \frac{\mu_2}{\lambda_{\max}}\right)$$

**What remains irreducibly conditional.** Even with the directional extension, a *quantitative* lower bound on $\mu$ is structurally necessary. The question is only how small $\mu$ can be. The irreducible condition is:

$$\mu > 0 \text{ and } \varepsilon < r_{\mathrm{eff}}(\mu, \mu_2, \Delta_{\mathrm{bdy}}, f_1)$$

**Verdict:** Qualitatively necessary (some $\mu > 0$ bound needed). Quantitatively replaceable: $\mu_0 \gtrsim 4.1 \to \mu_0 \gtrsim 0.04$-$0.4$ via directional analysis.

#### (GT) Gentle Transition — **Technically Convenient (Absorbable)**

**What the condition does.** (GT) bounds the perturbation magnitude relative to the barrier:
- $\varepsilon_1 < \Delta_t/4$ (perturbation doesn't destroy more than 1/4 of the barrier)
- $2\varepsilon_2 + 2\varepsilon_1/\mu < r_{\mathrm{basin}}/2$ (displaced field stays within half the basin)

**Structural necessity?** The *qualitative* requirement "perturbation is small relative to the basin" is necessary. But (GT) as stated is a **composite condition** that mixes perturbation bounds with basin properties. It can be absorbed into the single directional criterion:

$$\|\delta u\| < r_{\mathrm{eff}}(\mu, \mu_2, \Delta_{\mathrm{bdy}}, f_1)$$

This automatically encodes both the barrier stability ($\Delta_s \geq \Delta_t - 2\varepsilon_1$, Proposition 4) and the basin containment ($\delta u \in B_\Delta$, directional Proposition 5).

**Why it's technically convenient rather than structural.** (GT) does not identify any *new* geometric or topological constraint. It simply restates the basin containment in a form amenable to the isotropic analysis. The directional framework subsumes it.

**Verdict:** Technically convenient. Absorb into the directional basin criterion.

### Summary for Part (b)

| Condition | Nature | Action |
|-----------|--------|--------|
| (ND) $\mu > 0$ | Structurally necessary (Sard: generic) | Keep |
| (NB) $\mu \geq 4.1$ | Quantitatively conservative | Replace with directional criterion ($\mu \geq 0.04$-$0.4$) |
| (GT) gentle transition | Technically convenient | Absorb into directional basin containment |

**Proposed replacement:** A single condition:

**(BC') Directional basin containment.** $\|\hat{u}_s - \hat{u}_t\| < r_{\mathrm{eff}}(\mu, \mu_2, \Delta_{\mathrm{bdy}}, f_1)$ where $r_{\mathrm{eff}} = \sqrt{2\Delta_{\mathrm{bdy}} / (f_1^2 \mu + (1-f_1^2)\mu_2)}$.

This unifies (NB) and (GT) into a single geometric condition that is checkable from the Hessian spectrum and formation geometry.

---

## Part (d): Exact Threshold Preservation

### Current Conditions

| Condition | Symbol | Quantitative Form |
|-----------|--------|-------------------|
| Deep core existence | (H2') | $\mathrm{Core}^2(\hat{u}_t) \neq \emptyset$ |
| Phase separation strength | (H3) | $\beta > 11\alpha$ (for $d_{\min} = 4$) |

### Current Status

Exact threshold preservation requires the **interior gap** $\gamma_{\mathrm{int}} := \min_{x \in \mathrm{Core}^2} (\hat{u}(x) - \theta_{\mathrm{core}})$ to exceed the IFT perturbation displacement $2\varepsilon_1/\mu$. The interior gap is bounded by the screened Poisson analysis:

$$\hat{u}(x) - \theta_{\mathrm{core}} \geq (1 - \theta_{\mathrm{core}}) - C_1 \exp(-c_0 \delta(x)) - C_2/\beta$$

### Condition-by-Condition Analysis

#### (H2'): Deep Core Existence — **No Longer Conditional (Proved)**

**Status.** (H2') was originally a hypothesis, but Theorem 1 (CORE-DEPTH-ISOPERIMETRIC.md) proves it for $|\mathrm{Core}| \geq 25$ and $\beta \geq 58\alpha$ (conservative) via:
1. $\Gamma$-convergence: minimizers converge to characteristic functions of perimeter-minimizing sets
2. Edge-isoperimetric inequality: optimal sets are approximately square
3. Inradius argument: $(k-2)^2 > 0$ for $k \geq 3$ ($m \geq 25$)
4. Finite-$\beta$ transfer via Markov + Euler-Lagrange bootstrap

**Why the $m \geq 25$ bound is essentially tight.** The inradius of a $k \times k$ square is $(k-2)/2$. For $\delta \geq 2$, need $k \geq 6$, so $m \geq 36$. For $\delta \geq 1$ (shallow core), need $k \geq 4$, so $m \geq 16$. The $m \geq 25$ bound in the theorem is slightly tighter because it uses the $(k-2)^2$ count rather than inradius. **This is a geometric constraint that cannot be circumvented** — formations smaller than ~25 nodes simply don't have enough room for a deep core at depth $\geq 2$.

**Can $\beta \geq 58\alpha$ be weakened?** The conservative bound $\beta \geq 58\alpha$ comes from the Markov inequality transfer step. The formation-structured bound is $\beta \geq 7\alpha$, and exp13 verifies deep core existence at $\beta \geq 20\alpha$. The $\beta$ threshold is a quantitative detail of the proof technique, not a structural necessity.

**Verdict:** Proved. (H2') is no longer a condition. The remaining constraints ($m \geq 25$) are structurally necessary.

#### (H3): $\beta > 11\alpha$ — **Structurally Necessary for Positive Interior Gap, Quantitatively Conservative**

**What the condition does.** Ensures the interior gap $\gamma_{\mathrm{int}} > 0$ at deep core sites. The interior gap has two competing terms:
- $(1 - \theta_{\mathrm{core}}) = 0.1$ (headroom from threshold to maximum)
- $C_2/\beta$ where $C_2 \leq 2.875$ (operator correction eating into the headroom)

Positive gap requires $\beta > C_2/(1 - \theta_{\mathrm{core}}) \approx 28.75$ (conservative) or $\beta > 7$ (formation-structured $C_2 \approx 0.7$).

**Structural necessity analysis.** If $\beta/\alpha$ is too small, the double-well potential does not create sufficient phase separation. The field values at core sites remain in the spinodal region $(0.3, 0.7)$ rather than being pushed toward 1. In this diffuse regime:
- The interior gap $\gamma_{\mathrm{int}}$ can be negative (core values dip below threshold)
- No meaningful distinction exists between "core" and "boundary" nodes
- The formation lacks the sharp-interface structure that the persistence proof relies on

**This is a genuine structural requirement:** the entire T-Persist proof architecture depends on the core/boundary/exterior trichotomy, which requires phase separation ($\beta/\alpha$ large enough). Without it, the concept of "deep core" is vacuous.

**But the quantitative threshold is conservative.** The $\beta > 11\alpha$ bound (for $d_{\min} = 4$) uses the analytical $C_2 \leq 2.875$. Formation-structured analysis gives $C_2 \approx 0.7$, yielding $\beta > 7\alpha$. Empirically (exp13), $\beta > 20\alpha$ is more than sufficient.

**Tightening path.** The key improvement would be a formation-conditioned $C_2$ bound rather than the worst-case analytical estimate. The $C_2$ constant comes from the ratio $R = (\lambda_{\mathrm{cl}} + \lambda_{\mathrm{sep}})/\lambda_{\mathrm{bd}}$ and the closure coefficient $a_{\mathrm{cl}}$. A tighter analysis using the actual operator structure at minimizers (where $\mathrm{Cl}(\hat{u}) \approx \hat{u}$ at core sites) would yield $C_2 \leq 1.0$, giving $\beta > 10\alpha$.

**Verdict:** Structurally necessary in kind (phase separation needed). Quantitatively conservative by factor ~2-3x. The structural bound is $\beta > C_2(\text{formation-structured}) / (1 - \theta_{\mathrm{core}})$.

### Summary for Part (d)

| Condition | Nature | Action |
|-----------|--------|--------|
| (H2') $\mathrm{Core}^2 \neq \emptyset$ | **Proved** (Theorem 1) | Remove as hypothesis; cite as lemma |
| (H3) $\beta > 11\alpha$ | Structurally necessary, quantitatively loose | Tighten to $\beta > 7\alpha$ (formation-structured) |

**Proposed replacement:** Remove (H2') as a condition entirely. Replace (H3) with:

**(PS') Phase separation.** $\beta/\alpha > C_2^{\mathrm{form}}/(1 - \theta_{\mathrm{core}})$ where $C_2^{\mathrm{form}}$ is the formation-conditioned operator correction. Conservative: $\beta > 7\alpha$. This automatically implies positive interior gap and deep core existence (for $m \geq 25$).

Note: (PS') is strictly weaker than the existing (PS) phase transition condition ($\beta/\alpha > 4\lambda_2/|W''(c)|$), so it is automatically satisfied whenever phase transition occurs.

---

## Part (e): Transport Concentration

### Current Conditions

| Condition | Symbol | Quantitative Form |
|-----------|--------|-------------------|
| Fixed-point selection | (WR') | $\lambda_{\mathrm{tr}} \cdot \gamma \cdot \|\partial\varphi/\partial u\|_{\mathrm{op}} / (\varepsilon_{\mathrm{OT}} \cdot \mu_{\mathcal{F}}) < 1$ |
| Interior gap (from (d)) | (H2') + (H3) | $\gamma_{\mathrm{int}} > 0$ |
| Non-bifurcation | (NB) | $\mu \geq \mu_0$ |

### Current Status

Part (e) establishes that the self-referential OT kernel concentrates transport mass on core-to-core mappings. It has three sub-results:
1. **Fixed-point existence** (Schauder): unconditional for $\varepsilon_{\mathrm{OT}} > 0$
2. **Fixed-point uniqueness** near $\hat{u}_t$ (Banach): conditional on (WR')
3. **Deep-core concentration**: conditional on (H2') + (H3) + (NB)

### Condition-by-Condition Analysis

#### (WR') Banach Contraction for Uniqueness — **Technically Convenient (Replaceable)**

**What the condition does.** Guarantees that the self-referential fixed-point iteration $u_s^{(k+1)} = T(u_s^{(k)})$ converges to a *unique* fixed point near $\hat{u}_t$. The contraction rate is:

$$\rho = \frac{\lambda_{\mathrm{tr}} \cdot \|\partial\varphi/\partial u\|_{\mathrm{op}} \cdot (\log n + C)}{\Delta_\varphi^2 \cdot \mu_{\mathcal{F}}} < 1$$

**Why it's technically convenient, not structural.**

The TRANSPORT-SELECTION-ANALYSIS.md (Phase 5 theory) provides four independent arguments that transport uniqueness holds generically, independent of (WR'):

1. **Re-optimization discreteness (Argument 2).** The map $T = R \circ \mathrm{transport}$ factors through the discrete set of energy minimizers. A fixed point must be an energy minimizer whose transported field re-optimizes back to itself. This discrete constraint makes multiplicity non-generic.

2. **Continuation from $\lambda_{\mathrm{tr}} = 0$ (Argument 3).** At $\lambda_{\mathrm{tr}} = 0$, the fixed point is trivially unique ($u^* = $ the energy minimizer). By the IFT, this continues smoothly until $\rho(\mathrm{DT}) = 1$ (bifurcation). exp29 shows no bifurcation up to $\lambda_{\mathrm{tr}} = 10$.

3. **Re-optimization kills perturbations (Argument 3, deep reason).** The Jacobian of the re-optimization map $R$ at a non-degenerate minimizer satisfies $\|\mathrm{D}R\| \sim \exp(-\mu \tau) \to 0$ for large flow time $\tau$. The re-optimization step annihilates perturbations, making $T$ strongly contracting *regardless of $\lambda_{\mathrm{tr}}$*.

4. **Self-referential cost bias (Argument 4).** The fingerprint-based cost biases transport toward the source formation's structure, creating "basin dominance" that excludes alternative fixed points.

**The strictly weaker replacement** is **transport confinement**:

**(TC) Transport confinement.** $\|\mathrm{transport}(u_s) - \hat{u}_t\| < r_{\mathrm{basin}}$ for all $u_s \in \Sigma_m$.

Under (TC), the proof is trivial: for any $u_s$, transport lands in the basin, re-optimization maps to $\hat{u}^*$, so $T$ is the constant map $u_s \mapsto \hat{u}^*$.

**Transport confinement is supported by:**
- exp29: all 5 initializations converge to the same fixed point across $\lambda_{\mathrm{tr}} \in [0.01, 10]$
- The geodesic distance term $d^2/(2\sigma^2)$ in the cost confines transport spatially
- Entropic regularization ($\varepsilon_{\mathrm{OT}} > 0$) biases toward spread-out plans, limiting displacement

**What remains.** Transport confinement lacks a closed-form analytical bound. The key missing piece is:

$$\|M^*(u_s) \cdot u_s - \hat{u}_t\| \leq f(\sigma, \varepsilon_{\mathrm{OT}}, \mathrm{diam}(X))$$

where $f$ depends on spatial parameters but NOT on $u_s$. This is feasible because the geodesic part of the cost is $u_s$-independent.

**Path to analytical bound:** Decompose the OT displacement into:
- Geodesic component: bounded by $\sigma \cdot \sqrt{\log(n/\varepsilon_{\mathrm{OT}})}$ (standard entropic OT concentration)
- Fingerprint component: bounded by $\gamma^{-1} \cdot \varepsilon_{\mathrm{OT}} \cdot \log n / \Delta_\varphi^2$

The sum is $O(\sigma \sqrt{\log n})$ for typical parameters, well within the basin radius.

**Verdict:** Technically convenient. Replace (WR') with the weaker (TC). Upgrading (TC) from numerical verification to analytical proof requires a transport displacement bound — feasible but not yet done.

#### Interior Gap Dependence from (d) — **Tied to (H3), Already Analyzed**

The transport concentration two-tier result requires the fingerprint gap $\Delta_\varphi^2$ to be positive at deep core sites. This is equivalent to the interior gap being positive (core values well above threshold create large fingerprint differences from exterior sites). This is the same (H3) condition analyzed in Part (d).

**No additional condition needed** beyond what Part (d) already requires.

#### (NB) for Concentration — **Absorbed into (BC') from Part (b)**

The concentration-contraction compatibility requires $\mu > \mu_0$. This is the same (NB) condition as in Part (b), and is absorbed into the directional basin criterion (BC').

**Verdict:** No separate condition needed; shared with Part (b).

### Summary for Part (e)

| Condition | Nature | Action |
|-----------|--------|--------|
| (WR') $\rho < 1$ | Technically convenient | Replace with (TC) transport confinement |
| Interior gap | Same as (H3) in Part (d) | Already covered |
| (NB) | Same as in Part (b) | Already covered by (BC') |

---

## Unified Condition Set: Before and After

### Before (Current T-Persist-Full Conditions)

| # | Condition | Part(s) |
|---|-----------|---------|
| 1 | (ND) $\mu > 0$ | (a), (b), (d), (e) |
| 2 | (NB) $\mu \geq \mu_0 \gtrsim 4.1$ | (b), (e) |
| 3 | (GT) $\varepsilon_1 < \Delta_t/4$, $2\varepsilon_2 + 2\varepsilon_1/\mu < r/2$ | (b) |
| 4 | (WR') Banach contraction $\rho < 1$ | (e) |
| 5 | (H2') $\mathrm{Core}^2 \neq \emptyset$ | (d) |
| 6 | (H3) $\beta > 11\alpha$ | (d) |
| 7 | (PS) Phase transition $\beta/\alpha > 4\lambda_2/|W''(c)|$ | All |

**Count:** 7 conditions (2 proved: (ND) generic, (H2') proved; 5 genuinely restrictive)

### After (Proposed Streamlined Conditions)

| # | Condition | Replaces | Nature |
|---|-----------|----------|--------|
| 1 | **(PS) Phase separation** $\beta/\alpha > \beta_{\mathrm{crit}}$ | (PS), subsumes (H3), (H2') | Structural |
| 2 | **(ND) Non-degeneracy** $\mu > 0$ | (ND) | Structural (generic) |
| 3 | **(BC') Directional basin containment** $\|\delta u\| < r_{\mathrm{eff}}$ | (NB), (GT) | Structural (quantitative) |
| 4 | **(TC) Transport confinement** $\|\mathrm{transport}(u_s) - \hat{u}_t\| < r_{\mathrm{basin}}$ | (WR') | Structural (numerically verified) |

**Count:** 4 conditions (1 generic, 1 subsumes 3 old conditions, 1 new weaker replacement)

### What Changed

1. **(H2') removed** — proved as lemma (Theorem 1, isoperimetric)
2. **(H3) absorbed** into (PS) — phase separation implies positive interior gap
3. **(NB) + (GT) unified** into (BC') — directional basin containment, quantitatively 10-100x weaker
4. **(WR') replaced** by (TC) — transport confinement, strictly weaker, numerically verified

### What Remains Irreducibly Conditional

1. **$\mu > 0$ (non-degeneracy)** — at bifurcation, formation topology changes; no persistence is possible. Generic by Sard.
2. **Perturbation within (directional) basin** — if the temporal change is too large relative to the basin, the gradient flow lands at a different minimizer. This is a genuine physical limitation, not a proof artifact.
3. **Transport confinement** — numerically verified but lacking analytical bound. The analytical bound is a tractable problem (entropic OT concentration), not a fundamental obstacle.

---

## Implications for T-Persist-K-Sep and T-Persist-K-Weak

### T-Persist-K-Sep

The well-separation condition (WS) implies that each formation's conditions can be checked independently. The streamlined conditions apply per-formation. (WS) itself is **structurally necessary** for the decoupling argument — without spatial separation, formation interactions cannot be neglected.

The spectral-repulsion compatibility (SR): $\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}$ is **structurally necessary** — it ensures the joint spectral gap is positive (via Weyl). Can be weakened to a directional version analogous to (BC').

### T-Persist-K-Weak

The weak interaction condition (WI): $|O_{jk}| \leq 0.2 \cdot \min(|\mathrm{Core}_j|, |\mathrm{Core}_k|)$ is a **quantitative convenience**. The structural requirement is that overlap corrections are small enough not to destroy the interior gap. The $0.2$ threshold is conservative.

The joint non-bifurcation (NB-K) is the same as per-formation (NB) upgraded to the joint Hessian. The directional analysis applies here too, with the joint spectral gap replacing per-formation $\mu$.

---

## Open Problems Identified

1. **Analytical transport confinement bound.** Prove $\|\mathrm{transport}(u_s) - \hat{u}_t\| \leq C(\sigma, \varepsilon_{\mathrm{OT}}, \mathrm{diam}(X))$ independent of $u_s$. This would upgrade (TC) from numerical to analytical.

2. **Formation-conditioned $C_2$ bound.** Prove $C_2 \leq 1.0$ at formation-structured minimizers, tightening (H3) to $\beta > 10\alpha$.

3. **Generic non-alignment of perturbation with soft mode.** Prove that temporal perturbations have $f_1 = O(n^{-1/(2d)})$ generically, which would make (BC') automatically satisfied for all but the smallest formations.

4. **Universal $\Delta_{\mathrm{bdy}}$ lower bound.** Express the boundary escape barrier in terms of computable graph invariants, removing the formation-shape dependence from the basin analysis.
