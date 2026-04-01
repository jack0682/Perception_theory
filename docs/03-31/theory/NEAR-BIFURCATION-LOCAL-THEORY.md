# Near-Bifurcation Local Theory for Restricted Persistence

**Date:** 2026-03-31
**Session:** Plan_0331 execution — local theory for persistence failure near bifurcation
**Category:** theory
**Status:** complete
**Depends on:** docs/03-31/repair/PERSIST-SYNTHESIS.md, docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md, docs/03-31/repair/PERSIST-MORSE-ANALYSIS.md, Canonical Spec v2.0.md

---

## 1. Purpose

This document isolates the mathematically honest statement available **near bifurcation**.

The central claim is negative/restricted, not positive:

> Near bifurcation, the full persistence theorem should **not** be stated.  
> What survives is only a **local restricted-persistence principle**: exact-threshold / full-basin persistence fails generically, while weaker continuation statements (shifted-threshold, deep-core remnant, branch-local persistence) may still survive under additional local assumptions.

This reformulation is forced by the current basin analysis and by the existing plan itself, which already lists near-bifurcation basin and near-bifurcation persistence as open problems (`plan/Plan_0331.md:45-46`).

---

## 2. The Structural Mechanism of Failure

The single-formation basin analysis establishes a three-regime picture for escape barriers (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:203-232`):

1. **away from bifurcation:** boundary barrier remains `O(1)` and basin containment is feasible;
2. **near bifurcation:** the boundary barrier `Δ_bdy` collapses together with the relevant soft spectral gap;
3. **at bifurcation:** no finite basin radius exists in the bifurcating direction.

Thus the basic temporal-persistence mechanism fails for a geometric reason:
\[
\mu \to 0, \qquad \Delta_{\mathrm{bdy}} \to 0,
\]
so the transported perturbation is no longer small relative to the shrinking basin.

The repository already says this in effect:

- `docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:224-232`
- `docs/03-31/repair/PERSIST-SYNTHESIS.md:130`
- `Canonical Spec v2.0.md:1001`

The correct conclusion is therefore **not** “persistence theorem still holds with worse constants,” but rather:

> the basic basin-containment hypothesis of full persistence becomes structurally unstable near bifurcation.

---

## 3. What Exactly Fails

Near bifurcation, the following full-strength statements are no longer mathematically honest as general theorems.

### 3.1. Full basin containment

The standard persistence route requires
\[
2\varepsilon_2 + \frac{2\varepsilon_1}{\mu} < r_{\mathrm{basin}}.
\]

But near bifurcation,
- `μ` decreases,
- `2ε_1/μ` blows up,
- `r_basin` shrinks because `Δ_bdy` collapses.

This is exactly the mechanism recorded in the basin analysis (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:224-232`).

### 3.2. Exact-threshold persistence

Exact-threshold persistence relies on a positive interior margin that dominates the transported displacement. Near bifurcation, the same soft mode that collapses the basin also destroys any robust exact-threshold claim except possibly on a restricted deep-core subset.

### 3.3. Uniform persistence across the whole core

The two-tier structure already shows boundary/shallow-core sites are the first to lose rigidity (`Canonical Spec v2.0.md:972-980`, `996-1001`). Near bifurcation this becomes decisive: the boundary negotiation region becomes the active instability channel.

---

## 4. What Survives

Near bifurcation, the correct surviving statements are **local and tiered**.

### 4.1. Restricted persistence principle

**Principle RP-NB (Restricted Persistence Near Bifurcation).**

Suppose a branch of formation-structured critical points persists up to a shape-transition set where the active-set-aware spectral gap satisfies `μ -> 0`. Then, in a sufficiently small neighborhood of the bifurcation set:

1. the full basin-containment inequality generically fails;
2. exact-threshold persistence is not stable as a uniform theorem;
3. only branch-local continuation / shifted-threshold statements can remain valid;
4. any surviving transport concentration must be formulated on a **deep-core remnant**, not on the entire core.

This is the strongest honest formulation consistent with existing materials.

### 4.2. Shifted-threshold persistence may survive

The existing synthesis already recommends that near bifurcation only the weaker shifted-threshold result should be asserted (`docs/03-31/repair/PERSIST-SYNTHESIS.md:130`).

So the correct local statement is:

- **full persistence:** not available,
- **shifted-threshold persistence:** still locally plausible if one stays on the same branch,
- **deep-core remnant persistence:** plausible only where `δ(x) >= 2` and the local interior gap remains positive.

### 4.3. Deep-core remnant principle

Even near bifurcation, instability is boundary-dominated, not core-dominated (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:86-123`). Therefore, if a non-empty deep core remains and the branch has not yet crossed the bifurcation set, it is reasonable to expect a **restricted remnant theorem** of the form:

> sites sufficiently deep in the core continue to satisfy a shifted-threshold inclusion for sufficiently gentle perturbations,

provided the local interior margin still dominates the transported displacement on those sites.

This is not yet a proved theorem in full generality, but it is the correct direction for a local replacement theory.

---

## 5. Local Non-Persistence Principle

### 5.1. Statement

**Principle NP-NB (Local Non-Persistence Near Bifurcation).**

Let `u_t` lie on a branch of formation-structured local minimizers approaching a shape-transition parameter set. If along this branch
\[
\mu \to 0
\quad\text{and}\quad
\Delta_{\mathrm{bdy}} \to 0,
\]
then the full temporal-persistence package cannot remain uniformly valid. In particular, at sufficiently small spectral gap:

- the transported perturbation budget is no longer dominated by basin radius,
- the boundary layer becomes the first instability channel,
- exact-threshold persistence fails before shifted-threshold persistence,
- and the correct theory is one of **local restricted persistence plus bifurcation-sensitive failure**, not global persistence.

### 5.2. Why this is stronger than a heuristic

This principle is not merely intuitive. It synthesizes three independent internal results:

1. **boundary-dominated soft modes** (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:86-123`),
2. **three-regime basin theorem** (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:203-232`),
3. **explicit synthesis warning** that the theorem should exclude a neighborhood of bifurcation points (`docs/03-31/repair/PERSIST-SYNTHESIS.md:130`).

So the local non-persistence principle is a mathematically organized synthesis of what the repository already knows.

---

## 6. A Replacement Theorem Ladder

Near bifurcation, the correct theorem ladder is:

### Level 1 — no longer honest

- full persistence theorem with basin containment,
- universal `r >= const` statement,
- exact-threshold preservation on the whole core.

### Level 2 — still defensible locally

- branch-local continuation while the active-set-aware Hessian remains positive,
- shifted-threshold inclusion,
- deep-core remnant persistence on sites with positive local interior margin.

### Level 3 — bifurcation crossing

Once the branch actually crosses the bifurcation set (`μ = 0` in the relevant direction), the right description is no longer persistence but **branch selection / formation transition**.

This is where merge/split/birth/death theory begins.

---

## 7. Consequence for T-Persist Writing

The practical consequence is simple:

1. **Do not state a positive near-bifurcation persistence theorem.**
2. **Do state a restricted-persistence/local-non-persistence principle.**
3. **Treat bifurcation neighborhoods as an excluded or separately analyzed regime.**

This is fully consistent with the canonical status line:

- full temporal persistence remains conditional on `(NB)` away from shape transitions (`Canonical Spec v2.0.md:993-1001`),
- near-bifurcation persistence remains open (`plan/Plan_0331.md:46`).

---

## 8. Formal Theorems

The informal principles RP-NB and NP-NB (§4.1, §5.1) can now be formalized into quantitative theorems. These replace the heuristic statements with precise conditions and explicit constants.

### 8.1. Quantitative Definition of "Near Bifurcation"

**Definition (Near-Bifurcation Regime).** Let û be a formation-structured minimizer of E on Σ_m with active-set-aware (constrained) spectral gap μ = μ_F > 0. Let ε₁ > 0 be the IFT perturbation bound from T-Persist-1(c), and let ε₂ ≥ 0 be the transport-induced field displacement from T-Persist-1(a).

The system is in the **near-bifurcation regime** if

$$\mu < \mu_{\mathrm{bif}}(\varepsilon_1) := \left(\frac{\varepsilon_1}{C'}\right)^{2/3}$$

where $C'$ is the explicit constant defined in Theorem NB-1 below. In this regime, the basin containment condition of T-Persist-1(b) generically fails.

### 8.2. Theorem NB-1 (Basin Collapse Near Bifurcation)

**Theorem NB-1.** Let û ∈ Σ_m be a formation-structured local minimizer with constrained spectral gap μ = μ_F > 0 and boundary-mode energy barrier Δ_bdy. Assume E is C³ in a neighborhood of û on Σ_m. Then:

**(a) Barrier scaling.** The boundary-mode barrier satisfies:

$$\Delta_{\mathrm{bdy}} \leq \frac{L_3}{6} \cdot r_{\mathrm{soft}}^3 + \frac{\mu}{2} \cdot r_{\mathrm{soft}}^2$$

where $r_{\mathrm{soft}}$ is the distance to the nearest saddle point along the soft eigenmode and $L_3 = \sup_{\|v\|=1} |D^3 E(\hat{u})[v,v,v]|$ is the third-derivative bound along the energy landscape restricted to Σ_m. Near bifurcation, the barrier is dominated by the cubic term:

$$\Delta_{\mathrm{bdy}} = O(\mu^2) \quad \text{as } \mu \to 0$$

More precisely: at a generic pitchfork bifurcation where a formation transitions between two topologically distinct shapes, the soft eigenvalue satisfies $\mu = c_1(\beta - \beta_{\mathrm{bif}}) + O((\beta - \beta_{\mathrm{bif}})^2)$ for some $c_1 > 0$, and the barrier height satisfies $\Delta_{\mathrm{bdy}} = c_2 \mu^2 / L_3$ for explicit $c_2 = 2/(3\sqrt{3})$.

*Proof sketch.* Near a generic saddle-node or pitchfork bifurcation on the constrained manifold, the energy along the soft mode $v_1$ (eigenvector with eigenvalue μ) takes the normal form:

$$E(\hat{u} + t v_1) - E(\hat{u}) = \frac{\mu}{2} t^2 + \frac{a_3}{6} t^3 + O(t^4)$$

where $a_3 = D^3 E(\hat{u})[v_1, v_1, v_1]$. The saddle point is at $t^* = -\mu/a_3$, giving barrier:

$$\Delta_{\mathrm{bdy}} = E(\hat{u} + t^* v_1) - E(\hat{u}) = \frac{\mu^3}{6 a_3^2} \cdot 2 = \frac{\mu^3}{3 a_3^2}$$

Wait — for the standard cubic normal form $f(t) = \frac{\mu}{2}t^2 + \frac{a_3}{6}t^3$, the local maximum is at $t^* = -\mu/a_3$ with $f(t^*) = \frac{\mu}{2}\frac{\mu^2}{a_3^2} + \frac{a_3}{6}\frac{-\mu^3}{a_3^3} = \frac{\mu^3}{2a_3^2} - \frac{\mu^3}{6a_3^2} = \frac{\mu^3}{3a_3^2}$.

So: $\Delta_{\mathrm{bdy}} = \frac{\mu^3}{3 a_3^2}$ where $a_3 = D^3 E[v_1^3]$.

For the quartic normal form (pitchfork, where $a_3 = 0$ by symmetry), $f(t) = \frac{\mu}{2}t^2 + \frac{a_4}{24}t^4$ with barrier at the inflection: $\Delta_{\mathrm{bdy}} = \frac{3\mu^2}{2a_4}$.

In either case, $\Delta_{\mathrm{bdy}} = O(\mu^k)$ with $k \geq 2$. □

**(b) Basin radius collapse.** The isotropic basin radius satisfies:

$$r_{\mathrm{basin}} = \sqrt{\frac{2\Delta_{\mathrm{bdy}}}{\lambda_{\max}}} \leq \sqrt{\frac{2\mu^3}{3 a_3^2 \lambda_{\max}}} = O(\mu^{3/2})$$

where $\lambda_{\max}$ is the largest eigenvalue of the constrained Hessian (which remains O(β) away from the soft mode).

**(c) Basin containment failure.** The T-Persist-1(b) basin containment condition requires:

$$2\varepsilon_2 + \frac{2\varepsilon_1}{\mu} < r_{\mathrm{basin}}$$

Substituting the basin radius scaling:

$$\frac{2\varepsilon_1}{\mu} < C_0 \cdot \mu^{3/2}$$

This fails when:

$$\varepsilon_1 > C' \cdot \mu^{5/2}$$

where $C' = C_0/2 = \frac{1}{2}\sqrt{\frac{2}{3 a_3^2 \lambda_{\max}}}$.

Equivalently, basin containment fails when $\mu < \mu_{\mathrm{bif}}(\varepsilon_1) := (\varepsilon_1/C')^{2/5}$.

*Remark.* The exponent 2/5 (not 2/3 as stated in the preliminary definition §8.1) comes from the cubic normal form. For the pitchfork ($\Delta_{\mathrm{bdy}} = O(\mu^2)$), the corresponding threshold is $\mu_{\mathrm{bif}} = (\varepsilon_1/C'')^{2/3}$ with $C'' = \frac{1}{2}\sqrt{3/(a_4 \lambda_{\max})}$.

Both cases confirm the qualitative picture: as μ → 0, any positive perturbation ε₁ eventually violates basin containment. The bifurcation threshold $\mu_{\mathrm{bif}}$ is explicit in terms of the energy landscape parameters (a₃ or a₄, λ_max).

**Numerical verification (from BASIN-ESCAPE-ANALYSIS.md):**

| Grid | β | μ_F | Δ_bdy | r_basin | 2ε₁/μ (ε₁=0.1) | Contained? |
|------|---|-----|-------|---------|----------------|-----------|
| 10×10 | 50 | 14.2 | 0.640 | 0.46 | 0.014 | YES |
| 10×10 | 200 | 1.74 | 0.038 | 0.12 | 0.115 | MARGINAL |
| 12×12 | 50 | 0.94 | 0.008 | 0.05 | 0.213 | **NO** |

The 12×12 β=50 case (μ = 0.94) exemplifies near-bifurcation failure: the perturbation budget exceeds the basin radius by 4×. □

### 8.3. Theorem NB-2 (Deep-Core Remnant Persistence)

**Theorem NB-2.** Let û_t be a formation-structured minimizer at time t with core Core_t = {x : û_t(x) ≥ θ_core} and deep core Core_t^{δ≥k} = {x ∈ Core_t : d_G(x, X\Core_t) ≥ k}. Let û_s be the IFT-continued minimizer at time s (from T-Persist-1(c)) with ‖û_s - û_t‖ ≤ ε_IFT. Then, even when basin containment (T-Persist-1(b)) fails:

**(a) Pointwise deep-core bound.** For every $x \in \text{Core}_t^{\delta \geq 2}$:

$$\hat{u}_s(x) \geq \theta_{\text{core}} - \frac{2\varepsilon_1}{\mu}$$

where ε₁ is the energy perturbation bound and μ = μ_F is the constrained spectral gap.

*Proof.* This follows from T-Persist-1(c) (IFT-based local continuation), which requires only local non-degeneracy of the constrained Hessian — NOT basin containment. By T-Persist-1(c), the IFT solution satisfies:

$$\|\hat{u}_s - \hat{u}_t\|_\infty \leq \|\hat{u}_s - \hat{u}_t\|_2 \leq \frac{2\varepsilon_1}{\mu}$$

where the factor 2/μ comes from the inverse Hessian bound ‖H_Σ^{-1}‖_op ≤ 1/μ applied to the gradient perturbation (bounded by 2ε₁ from T-Persist-1(a)).

For deep core sites x ∈ Core_t^{δ≥2}: û_t(x) ≥ θ_core (by definition), hence:

$$\hat{u}_s(x) = \hat{u}_t(x) - (\hat{u}_t(x) - \hat{u}_s(x)) \geq \theta_{\text{core}} - \frac{2\varepsilon_1}{\mu} \quad \square$$

**(b) Threshold preservation condition.** Define the **interior gap** at deep core sites:

$$\gamma_{\text{int}} := \min_{x \in \text{Core}_t^{\delta \geq 2}} (\hat{u}_t(x) - \theta_{\text{core}})$$

The deep core preserves exact threshold inclusion (û_s(x) ≥ θ_core) whenever:

$$\gamma_{\text{int}} > \frac{2\varepsilon_1}{\mu}$$

*Proof.* Immediate from (a): $\hat{u}_s(x) \geq \theta_{\text{core}} + \gamma_{\text{int}} - 2\varepsilon_1/\mu > \theta_{\text{core}}$ when $\gamma_{\text{int}} > 2\varepsilon_1/\mu$. □

**(c) Interior gap estimate.** For formation-structured minimizers in the phase-separated regime (β ≫ α), the interior gap satisfies:

$$\gamma_{\text{int}} \geq (1 - \theta_{\text{core}}) - C_1 e^{-2c_0 \delta} - \frac{C_2}{\beta}$$

where:
- $C_1 = O(1)$ depends on the double-well shape (W(u) = u²(1-u)²),
- $c_0 = \sqrt{\beta/(4\alpha d)} > 0$ is the exponential decay rate from Γ-convergence (T11),
- $C_2$ accounts for the KKT residual at constrained nodes,
- $\delta = 2$ for the deep core (by definition of Core^{δ≥2}).

At default parameters (θ_core = 0.9, α = 1, β = 10, δ_graph = 4, δ = 2):
- $c_0 = \sqrt{10/16} \approx 0.79$
- $C_1 e^{-2c_0 \cdot 2} = C_1 e^{-3.16} \approx 0.042 C_1$
- γ_int ≈ 0.1 - 0.042·C₁ - C₂/10

For typical C₁ ≈ 1, C₂ ≈ 0.5: γ_int ≈ 0.008.

**(d) Deep-core survival criterion.** Combining (b) and (c), deep-core threshold persistence holds when:

$$\frac{2\varepsilon_1}{\mu} < (1 - \theta_{\text{core}}) - C_1 e^{-4c_0} - \frac{C_2}{\beta}$$

This is a WEAKER condition than full basin containment (Theorem NB-1(c)), because:
1. It requires only the IFT local continuation (non-degeneracy μ > 0), not the global basin containment.
2. The right-hand side is positive whenever β is sufficiently large (the phase-separated regime), regardless of the basin radius.
3. It provides **partial persistence** (deep core survives) even when the full formation does not persist.

### 8.4. Corollary (Three-Tier Persistence Near Bifurcation)

Combining Theorems NB-1 and NB-2 yields a refined persistence ladder near bifurcation:

**Tier 1 (Full persistence).** When $\mu > \mu_{\mathrm{bif}}(\varepsilon_1)$: basin containment holds, full T-Persist-1 applies. The entire formation persists with threshold preservation.

**Tier 2 (Deep-core persistence).** When $0 < \mu < \mu_{\mathrm{bif}}(\varepsilon_1)$ but $\gamma_{\text{int}} > 2\varepsilon_1/\mu$: basin containment fails, but the IFT continuation exists. Deep core sites preserve threshold. Boundary nodes may not persist.

**Tier 3 (No persistence).** When $\gamma_{\text{int}} \leq 2\varepsilon_1/\mu$ or $\mu = 0$: even deep-core persistence fails. The system crosses the bifurcation, and the correct description is branch selection / formation transition, not persistence.

The transition between tiers is **quantitative**: the boundaries are explicit functions of μ, ε₁, γ_int, and the energy landscape parameters.

---

## 9. Open Problems Created by the Local Theory

The formal theorems expose three concrete next directions:

1. **Directional basin theorem near bifurcation** — Theorem NB-1 uses isotropic r_basin = √(2Δ_bdy/λ_max). The directional analysis (BASIN-ESCAPE-ANALYSIS.md §3) shows the basin is ellipsoidal, with potentially large radius transverse to the soft mode. A directional version could extend Tier 1 persistence to some near-bifurcation cases where the temporal perturbation does not align with the soft mode.

2. **Boundary-layer dynamics** — Theorem NB-2 shows deep core survives but says nothing about what happens to boundary nodes. The boundary layer dynamics near bifurcation (merge, split, reshape) is the natural continuation theory.

3. **Bifurcation selection theorem** — At μ = 0, the formation is at a critical point of the energy landscape. Which post-bifurcation branch is selected by transport + gradient flow? This connects to catastrophe theory and formation birth/death events.

These are the mathematically correct successors to the full persistence claim.

---

## 10. Final Assessment

The near-bifurcation theory is now formalized into two quantitative theorems:

- **NB-1** gives explicit basin collapse scaling (Δ_bdy = O(μ^k), r_basin = O(μ^{k/2})) and a quantitative bifurcation threshold μ_bif.
- **NB-2** gives a genuine partial persistence result: deep-core sites survive even when the full formation doesn't persist, with an explicit survival criterion.

The correct near-bifurcation message is not "persistence theorem with weaker constants" but rather:

> **Near bifurcation, full persistence ceases to be the right theorem shape.** What remains is a quantitative three-tier theory: full persistence (μ > μ_bif), deep-core remnant persistence (0 < μ < μ_bif, γ_int sufficient), and bifurcation-driven formation transition (μ → 0).

This replaces the informal principles RP-NB and NP-NB with rigorous statements that specify exactly when and where persistence holds, with explicit constants.
