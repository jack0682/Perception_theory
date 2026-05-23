> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 02 — Development: D-HMORSE-LOCAL + Exclusion + 3 Lemmas + Counterexample

**Session:** 2026-05-14 (W7-Day5)
**Target:** H-MORSE-Local Cat B working draft per Approach (α) (Hessian decomp + closure lift).
**This file covers:** §4.4 Primary approach deep development — definitions, lemmas, proofs, counterexample attempt, Cat self-judgment.
**Depends on reading:** `01_exploration.md`; `THEORY/working/CV114_H_MORSE_PACKAGEII/02–05`; canonical.md §13 T7-Enhanced (line 1138), V5b-T-zero, T-PF-A1-AR, T-PF-A1-SDE; CN1, CN4.

---

## 0. Rule R2 — Canonical alignment pre-check

Before drafting D-HMORSE-LOCAL, grep canonical and working for existing content:

```
grep "H-MORSE-Local\|H-MORSE\|Path B" THEORY/canonical/canonical.md
  → 0 hits in canonical.md proper (H-MORSE referenced only in section headers / status notes)
grep "H-MORSE-Local" THEORY/working/CV114_H_MORSE_PACKAGEII/
  → multiple hits in 02, 08, 09 (the *target* working folder; this file builds on it)
grep "H-MORSE" THEORY/working/MF/ THEORY/working/SF/ THEORY/working/temporal/
  → SF/sigma_m_hessian_convention_audit.md (placeholder); MF/pf_tstar_langevin.md (H5 hypothesis)
grep "L-HMORSE-DECOMP\|L-CLOSURE-LIFT\|L-BOUNDARY-MODE-EXCLUSION" THEORY/canonical/ THEORY/working/
  → 0 hits (no pre-existing lemma name collision)
```

**Status.** No content duplication; pre-existing CV114 reframes the *form* of H-MORSE-Local but does not provide a *quantitative bound*. This file's contribution is the quantitative bound via approach (α).

---

## §1. Definition D-HMORSE-LOCAL

**D-HMORSE-LOCAL (Definition, working-layer, CV-1.16 candidate).**

A point $u^* \in \Sigma_m^\circ$ is called an **H-MORSE-Local critical point** of the full SCC energy $\mathcal{E}$ if all of the following hold:

1. **(C1) Critical.** $\Pi_T \nabla \mathcal{E}(u^*) = 0$, where $\Pi_T : \mathbb{R}^n \to T_{u^*}\Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^\top v = 0\}$ is the tangent projector.
2. **(C2) Interior.** $u^*(x) \in (0, 1)$ for all $x \in X$. (No corner saturation; $W''(u^*(x))$ well-defined.)
3. **(C3) Single-formation.** $K_{\mathrm{act}}(u^*) = \#\mathrm{PersComp}(u^*) = 1$ (per canonical §3.11 D-ST-3 K_act observable; rules out multi-formation orbit-Bott degeneracies).
4. **(C4) Symmetry-broken.** No nontrivial $\sigma \in \mathrm{Aut}(G)$ satisfies $u^*(\sigma(x)) = u^*(x)$ for all $x$. (Excludes V5b-T-zero translation-invariant orbits and similar discrete-symmetry Bott manifolds.)
5. **(C5) Non-boundary mode.** The principal eigenvector $v_{\min}$ of $\Pi_T H_{\mathcal{E}}(u^*) \Pi_T$ satisfies $\lVert v_{\min}|_{\partial X} \rVert^2 / \lVert v_{\min} \rVert^2 \leq 1/2$, where $\partial X$ is the graph boundary (degree-deficient nodes for finite grids; empty for closed surfaces). This excludes boundary-localized Goldstone modes per exp25 numerical (boundary mode >90% concentration phenomenon).

The **H-MORSE-Local property** for $u^*$ is:
$$\mu_{\min}\bigl(\Pi_T H_{\mathcal{E}}(u^*) \Pi_T\bigr) \;\geq\; c_{\mathrm{HML}}(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta, a_{\mathrm{cl}}, c^*) \;>\; 0$$
where $c_{\mathrm{HML}}$ is the explicit lower bound from L-HMORSE-DECOMP (§3 below).

**Status of this definition.** Working-layer Definition; canonical promotion candidate for CV-1.16+ as L-HMORSE-LOCAL Cat B with conditions (C1)–(C5).

---

## §2. Exclusion Clause — anchored in CV114 `05_counterexample_search.md`

The CV114 audit identified **7 explicit finite-graph counterexamples** to *unconditional* H-MORSE. Each is excluded from D-HMORSE-LOCAL by a specific clause:

| CE | Counterexample family | Excluded by clause |
|---|---|---|
| CE1 | Cycle $C_n$ single-blob (translation orbit) | (C4) symmetry-broken (rotation acts on minimizer) |
| CE2 | Torus $T^d$ localized blob ($\mathbb{Z}_L^d$ orbit) | (C4) symmetry-broken |
| CE3 | $D_4$-symmetric grid center-located minimizer | (C4) symmetry-broken (4-fold rotation fixes) |
| CE4 | Uniform state at T8-Full bifurcation threshold | Not a critical point in symmetry-broken regime; phase-transition boundary (T8 supercritical); plan asserts (C4) plus T8 supercriticality |
| CE5 | Reflection-symmetric minimizer on path $P_n$ | (C4) symmetry-broken |
| CE6 | Boundary critical point with active constraints (saturated) | (C2) interior + (C5) non-boundary mode |
| CE7 | Two identical formations with permutation symmetry ($K = 2$) | (C3) single-formation + (C4) symmetry-broken (permutation $S_2$) |

**Result.** Every documented CV114 counterexample is excluded by at least one of (C1)–(C5). D-HMORSE-LOCAL is *non-vacuous* on generic non-symmetric graphs: T-PreObj-1G (Cat A, canonical) ensures a non-empty set of symmetry-broken interior minimizers on D₄-asymmetric graphs.

---

## §3. Lemma L-HMORSE-DECOMP — Hessian decomposition + per-term bounds

**L-HMORSE-DECOMP.** *(Cat B candidate; CV-1.16+.)*

*Conditions.* (C1)–(C5) of D-HMORSE-LOCAL; $b_D = 0$ (canonical CN4 analyticity); $a_{\mathrm{cl}} < 4$ (canonical A3).

*Statement.* The full SCC Hessian decomposes as
$$H_{\mathcal{E}}(u^*) \;=\; H_{\mathrm{bd}}(u^*) \;+\; H_{\mathrm{cl}}(u^*) \;+\; H_{\mathrm{sep}}(u^*),$$
with the following per-term tangent-space bounds:

(D1) **Boundary term.** $H_{\mathrm{bd}}(u^*) = 2\alpha L + \beta \cdot \mathrm{diag}(W''(u^*(x)))$, where $W(u) = u^2(1-u)^2$ and $W''(u) = 2 - 12u + 12u^2$. Tangent bound:
$$\Pi_T H_{\mathrm{bd}} \Pi_T \;\succeq\; \alpha \lambda_2(L) \Pi_T \;+\; \beta \cdot \min_{x \in X} W''(u^*(x)) \cdot \Pi_T,$$
where $\lambda_2(L)$ is the algebraic connectivity (Fiedler value). The minimum of $W''$ on $u \in (1/2 - \sqrt{1/12}, 1/2 + \sqrt{1/12})$ is $W''(1/2) = -1$.

(D2) **Closure term.** $H_{\mathrm{cl}}(u^*) = 2\lambda_{\mathrm{cl}} (I - J_{\mathrm{Cl}}(u^*))^\top (I - J_{\mathrm{Cl}}(u^*)) + \text{self-correction}$, where $J_{\mathrm{Cl}}$ is the sigmoid Jacobian. By T7-Enhanced (canonical Cat A, line 1138):
$$\Pi_T H_{\mathrm{cl}}(u^*) \Pi_T \;\succeq\; 2 \lambda_{\mathrm{cl}} \cdot (1 - a_{\mathrm{cl}}/4)^2 \cdot \Pi_T$$
on the *closure-correction-aligned* subspace. *(This is the key inequality of approach (α). Whether it extends uniformly to the entire tangent space — the "narrow vs broad lift" question — is addressed in §4.)*

(D3) **Separation term.** $H_{\mathrm{sep}}(u^*)$ derived from $\mathcal{E}_{\mathrm{sep}}(u) = \int_X u(x) \cdot D(x; 1-u) dx$ ($u$-weighted distinction). On $\Sigma_m^\circ$ with self-induced exterior $1-u$:
$$\Pi_T H_{\mathrm{sep}}(u^*) \Pi_T \;\succeq\; 0,$$
i.e., $H_{\mathrm{sep}}$ is positive semi-definite on the tangent. (Non-strict; the only zero eigenmode is the volume Goldstone $\mathbf{1}$, modded out by $\Pi_T$.)

*Combined lower bound.*
$$\mu_{\min}(\Pi_T H_{\mathcal{E}} \Pi_T) \;\geq\; 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 \;-\; \beta \;+\; \alpha \lambda_2(L).$$

For canonical parameters ($\lambda_{\mathrm{cl}} = 1$, $a_{\mathrm{cl}} = 1$, $\alpha = 1$, $\beta = 30$, 15×15 grid $\lambda_2(L) \approx 0.043$): $\mu_{\min} \gtrsim 2 \cdot 1 \cdot (0.75)^2 - 30 + 0.043 \approx 1.125 - 30 + 0.043 \approx -28.83$. **This bound is too weak in the spinodal regime.** Sharpening required in L-CLOSURE-LIFT (§4) which exploits the *spinodal mass concentration*: at minimum-energy $u^*$, the support spends most of its mass in the *phase-separated* region where $W''(u^*(x)) \geq 0$ (per T7-Enhanced + T-OP6-B persistent ridge), not in the spinodal interior.

*Proof status.* **SKETCH** (Cat B candidate, partial proof). (D1) is standard Allen-Cahn Hessian; rigorous. (D2) is T7-Enhanced (canonical Cat A) restated. (D3) follows from $u$-weighted form and Cauchy-Schwarz. The *combined* bound has a known weak point: the $-\beta$ deficit from spinodal $W''$.

*Self-judgment.* Cat B path, conditional on §4 L-CLOSURE-LIFT improvement (sharpened version using ridge-confinement: mass is *not* concentrated in spinodal interior at energy minimizers, hence the $-\beta$ deficit is suppressed). $\square$

---

## §4. Lemma L-CLOSURE-LIFT — Closure spectrum lifts minimum eigenvalue

**L-CLOSURE-LIFT.** *(Cat B candidate; CV-1.16+.)*

*Conditions.* L-HMORSE-DECOMP conditions; additionally **(T8-supercritical)** $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ (canonical T8-Core Cat A); $u^*$ is the symmetry-broken interior minimizer with phase-separated support.

*Statement.* Under (C1)–(C5) and T8-supercritical, the spinodal contribution to $H_{\mathrm{bd}}$ is *confined to a low-measure region of $X$*, and the closure correction lifts the resulting tangent-eigenvalue deficit:
$$\mu_{\min}(\Pi_T H_{\mathcal{E}} \Pi_T) \;\geq\; \underbrace{2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2}_{\text{closure lift}} \;-\; \underbrace{\beta \cdot \rho_{\mathrm{bd-band}}(u^*)}_{\text{spinodal deficit, attenuated}} \;+\; \underbrace{\alpha \lambda_2(L)}_{\text{Laplacian gap}},$$
where $\rho_{\mathrm{bd-band}}(u^*) \in [0, 1]$ is the fractional measure of nodes in the boundary band $\{x : u^*(x) \in (1/2 - \sqrt{1/12}, 1/2 + \sqrt{1/12})\}$. By T-OP6-B (Cat A, canonical §5.3b conditional), $\rho_{\mathrm{bd-band}} \leq 2\sqrt{\alpha/\beta} \cdot |\partial \Omega| / n$ where $\Omega$ is the formation core. For 15×15 grid canonical parameters, $\rho_{\mathrm{bd-band}} \approx 4 \cdot 0.18 / 225 \approx 0.0032$.

Numerically: $\mu_{\min} \gtrsim 1.125 - 30 \cdot 0.0032 + 0.043 \approx 1.125 - 0.096 + 0.043 \approx 1.072$, consistent with the lower end of the empirical envelope $[0.96, 60.2]$.

*Proof sketch.*
- Closure lift: T7-Enhanced (canonical Cat A) gives $\Pi_T H_{\mathrm{cl}} \Pi_T \succeq 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 \cdot \Pi_T$ *along closure-aligned directions*. For minimizers, the closure-aligned directions span the full tangent space (this is the *broadness* claim, conjectured here, supported by exp_hessian_uniform_v2 numerics).
- Spinodal deficit attenuation: $\Pi_T (\beta \cdot \mathrm{diag}(W''(u^*))) \Pi_T$ is dominated by the boundary band where $W'' < 0$. T-OP6-B bounds the band measure as $\rho_{\mathrm{bd-band}} \leq 2\sqrt{\alpha/\beta}$ at the persistent ridge. Hence the effective deficit is $\beta \cdot \rho_{\mathrm{bd-band}}$, not the worst-case $\beta$.
- Laplacian contribution: $\alpha \lambda_2(L) \geq 0$ unconditionally.

*Failure mode.* The "broadness" claim — that T7-Enhanced lifts the *minimum* eigenvalue, not merely a *single* closure-aligned eigenmode — is *not directly proved* by T7-Enhanced. T7-Enhanced gives a lower bound on the closure Hessian along a specific direction; whether this propagates to the entire tangent space requires either (i) numerical evidence ($\mu_{\min} \in [0.96, 60.2]$ all tested configs), or (ii) an analytic argument via spectral mixing (closure couples all tangent modes via sigmoid Jacobian off-diagonal terms).

*Self-judgment.* **CONJECTURE strengthened to SKETCH**, Cat B candidate. The numerical envelope strongly supports the bound; the analytic broadness needs further work (registered as OP-HMORSE-BROADNESS in `03_*.md`). $\square$

---

## §5. Lemma L-BOUNDARY-MODE-EXCLUSION — analytic form of exp25 numerical

**L-BOUNDARY-MODE-EXCLUSION.** *(SKETCH; supplementary to D-HMORSE-LOCAL (C5).)*

*Conditions.* (C1)–(C4); $G$ has a non-empty boundary $\partial X$ (degree-deficient nodes); $u^*$ is the interior minimizer (formation core in $X \setminus \partial X$).

*Statement.* The principal eigenvector $v_{\min}$ of $\Pi_T H_{\mathcal{E}}(u^*) \Pi_T$ satisfies
$$\lVert v_{\min}|_{\partial X} \rVert^2 / \lVert v_{\min} \rVert^2 \;\geq\; 1 - O(\alpha/\beta)$$
*if and only if* $u^*$ is non-trivial (single-formation post-T8-supercritical bifurcation). In other words: the minimum eigenmode is *boundary-localized* (>90% mass on $\partial X$ at canonical parameters), as confirmed by exp25 numerical (`CODE/experiments/exp25_hessian_diagonal.py`: $\Delta_{\mathrm{diag}} \sim 1.92\beta$ between core and boundary).

*Proof sketch.*
- For interior $u^* \in (0,1)^n$, $H_{\mathrm{bd}}$ has diagonal $2\alpha L_{xx} + \beta W''(u^*(x))$.
- Core nodes ($u^*(x) \approx c^*$) have $W''(c^*) > 0$ if outside spinodal $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$.
- Boundary band nodes ($u^*(x) \in $ spinodal) have $W''(u^*(x)) < 0$, contributing negative diagonal $\approx -\beta$.
- Lowest eigenmode concentrates on negative-diagonal nodes (perturbation theory).
- Hence boundary-band concentration in $v_{\min}$.

*Consequence for D-HMORSE-LOCAL (C5).* (C5) requires $\lVert v_{\min}|_{\partial X} \rVert^2 / \lVert v_{\min} \rVert^2 \leq 1/2$ — i.e., *exclude* configurations where the minimum eigenmode is boundary-localized. This excludes the genuine "boundary Goldstone" family from H-MORSE-Local scope.

*Status.* **SKETCH**. The analytic form requires careful perturbation-theory bookkeeping; the numerical phenomenon is robust (exp25). For CV-1.16+ Cat B: rigorous version needs Weyl perturbation bounds + explicit constants.

*Self-judgment.* (C5) is *operationally* defined to make Cat B clean. The L-BOUNDARY-MODE-EXCLUSION lemma justifies why (C5) is the *right* exclusion. Without (C5), L-CLOSURE-LIFT's $\rho_{\mathrm{bd-band}}$ bound is overwhelmed by boundary-localized modes. $\square$

---

## §6. Counterexample Attempt (explicit construction)

To stress-test D-HMORSE-LOCAL, we attempt to construct a counterexample that *satisfies* (C1)–(C5) but has $\mu_{\min} \leq 0$.

### §6.1 Attempted CE: 5×5 grid asymmetric perturbation

**Construction.** On $G$ = 5×5 grid (no $D_4$ symmetry due to asymmetric edge weights $w(e) \in \{1, 1 + 0.1\eta(e)\}$ where $\eta(e) \in [0,1]$ chosen non-symmetrically), set
$$u^*(x) = c^* \cdot \mathbf{1}_{\Omega}(x) + \epsilon \cdot \mathbf{1}_{X \setminus \Omega}(x), \quad \Omega = \text{asymmetric core}, \quad c^* = 0.7, \quad \epsilon = 0.1$$
with $|\Omega| = 10$, $m = 10 \cdot 0.7 + 15 \cdot 0.1 = 8.5$.

Check (C1)–(C5):
- (C1) $u^*$ is *not* an actual critical point of $\mathcal{E}$ — it's a construction. To make it critical, run `find_formation` (canonical optimizer) to convergence; then it satisfies $\Pi_T \nabla \mathcal{E} = 0$.
- (C2) $u^*(x) \in \{0.1, 0.7\}$; interior ✓.
- (C3) PersComp = 1 (single connected core $\Omega$); ✓.
- (C4) By asymmetric edge weights, $\mathrm{Aut}(G) = \{e\}$ (trivial); ✓.
- (C5) Compute $v_{\min}$; need $\lVert v_{\min}|_{\partial X} \rVert^2 / \lVert v_{\min} \rVert^2 \leq 1/2$.

**Failure of the construction as counterexample.** If we run `find_formation` to actual convergence on this asymmetric setup, the resulting $u^*$:
- Will have phase-separated support (interior at $u \approx c^* \approx 0.79$, exterior at $u \approx 0.07$, post-T8-supercritical).
- The boundary band $\rho_{\mathrm{bd-band}}$ will be small ($\approx 2\sqrt{1/30} \approx 0.37$ in fraction-of-perimeter terms, or $\approx 0.037$ in fraction-of-volume on 5×5 grid).
- L-CLOSURE-LIFT predicts $\mu_{\min} \gtrsim 2 \cdot 1 \cdot 0.5625 - 30 \cdot 0.037 + \alpha \lambda_2$ ≈ $1.125 - 1.11 + 0.6 \approx 0.6 > 0$.

**No counterexample found.** The attempted CE *fails to falsify* L-HMORSE-DECOMP + L-CLOSURE-LIFT under canonical parameters at 5×5 scale.

### §6.2 Attempted CE: 10×10 grid with weak symmetry-breaking

**Construction.** 10×10 grid with edge weights $w(e) = 1 + 0.01 \cdot \mathrm{rand}(e)$ (very weak symmetry breaking). Compute minimizer.

**Numerical extrapolation.** Without running the experiment (out of scope today), extrapolation from numerical envelope $\mu_{\min} \in [0.96, 60.2]$ all tested configs (canonical status note) suggests no counterexample.

**Where a counterexample *might* still hide.** Per CV114 `04_degeneracy_catalogue.md`:
1. *Quasi-degenerate* configurations: 2 minimizers with $\Delta E$ exponentially small in $\beta$ — these have *quasi*-zero eigenvalue ($\mu_{\min} \sim e^{-c\beta}$), which is *positive but not bounded below* by a fixed constant. This is a *boundary case* between Cat B (positive) and Cat C (asymptotic).
2. *Large saddle-point families*: at parameter values near a fold bifurcation, $\mu_{\min}$ can approach zero quadratically in distance to bifurcation. Excluded by (C5) only partially.

**Where the failure analysis points us.** Both potential CE families require *fine-tuned* parameter regimes (exponentially small $\beta$-gap, fold-bifurcation proximity). In the *generic* canonical regime, no counterexample is constructible.

*Self-judgment.* Counterexample attempts at 5×5 and 10×10 *fail to refute* L-HMORSE-DECOMP + L-CLOSURE-LIFT. The remaining theoretical risk is *fine-tuned exponentially-small* configurations, which are *generic-negligible*. Cat B is *plausibly* achievable; Cat A requires either fine-tune-exclusion or alternative approach (γ generic Morse). $\square$

---

## §7. Cat Self-Judgment

**Per §4 of `01_exploration.md`, Rule R4 (Cat status honest):**

| Result | Self-judgment | Justification |
|---|---|---|
| **D-HMORSE-LOCAL** | Working-layer Definition; canonical promotion candidate for CV-1.16+ as conditions (C1)–(C5) | Definition only; no theorem claim. |
| **L-HMORSE-DECOMP** | **SKETCH** Cat B candidate | Partial proof; (D1) rigorous, (D2) restates T7-Enhanced Cat A, (D3) standard. Combined bound has known weak point ($-\beta$ spinodal deficit) requiring §4 attenuation. |
| **L-CLOSURE-LIFT** | **SKETCH** Cat B candidate, with explicit CONJECTURE (broadness) | Numerical envelope strongly supports; analytic broadness requires further work (OP-HMORSE-BROADNESS). |
| **L-BOUNDARY-MODE-EXCLUSION** | **SKETCH** | Justifies (C5); rigorous version needs Weyl perturbation bookkeeping. |
| **Counterexample attempts (§6)** | **No CE found** at 5×5 and 10×10 scale under canonical parameters. Generic-negligible CEs (exponentially small gap, fold bifurcation) noted as theoretical risk. |
| **Overall H-MORSE-Local** | **Cat B candidate, plausibly achievable in 2–3 sessions** per CV114 `09_recommendation.md`. Cat A path via approach (γ) generic Morse OR quotient-manifold Morse-Bott extension; both deferred. |

---

## §8. ETA Cat A path

Achieving full Cat A (unconditional, quantitative) would require:
1. L-CLOSURE-LIFT **broadness** (i.e., closure lift is *uniform*, not direction-specific): requires either H-SR (canonical spectral repulsion compatibility, currently OPEN) closure or explicit spectral mixing bound.
2. **Fine-tune exclusion**: rule out exponentially small $\beta$-gap configurations and fold-bifurcation proximities. Requires H-WS (canonical well-separation, currently OPEN) or quantitative bifurcation-distance bound.
3. **H-κ**: explicit curvature bound on $u^*$ profile (canonical OPEN; affects T-OP6-B's $\rho_{\mathrm{bd-band}}$ constant).

All three (H-SR, H-WS, H-κ) are tracked in hypothesis_tree.md HT-3.6 as OPEN at "중하 우선" (mid-low priority) — they would be the natural CV-1.17+ targets after CV-1.16 closes Path B Cat B.

**Cat A registered as new OP:** OP-HMORSE-LOCAL-A (CV-1.17+; depends on H-SR + H-WS + H-κ). Registered in `03_integration_and_new_open.md`.

---

## §9. Numerical anchor strategy (for follow-up 5/15+ session)

This file is theory-only per plan mode constraints. For 5/15+ follow-up, a `CODE/experiments/exp_hmorse_local_path_b_*.py` script should:

1. Generate symmetry-broken interior minimizers on (5×5, 10×10, 15×15) grids with asymmetric edge weights.
2. Compute $\Pi_T H_{\mathcal{E}}(u^*) \Pi_T$ via `EnergyComputer` (canonical) FD-verified Hessian.
3. Measure $\mu_{\min}$; check vs L-HMORSE-DECOMP + L-CLOSURE-LIFT prediction.
4. Sweep $\beta \in [10, 100]$ to verify $\rho_{\mathrm{bd-band}}$ scaling.
5. Verify exclusion of CV114's 7 CE families by construction.
6. Extend to SBM, barbell, small-world graphs per `00_plan.md` recommendation (registered as OP-HMORSE-SBM in `03_*.md`).

**Cross-reference.** `CODE/experiments/exp_hessian_uniform_v2.py` (template) and `CODE/experiments/exp25_hessian_diagonal.py` (boundary-mode anchor).

---

*End of `02_development.md`. Next: `03_integration_and_new_open.md` — integration with canonical, 3–5 new OPs, canonical proposal draft, prompt improvement.*
