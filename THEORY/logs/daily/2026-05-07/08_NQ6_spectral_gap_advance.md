> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 08_NQ6_spectral_gap_advance.md — NQ-T-Identity-6 Advancement (Spectral-Gap Cat A Path)

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended evening session
**Closure target:** NQ-T-Identity-6 — formalize Proposition 12.1 (`03_development.md` §12) into a development sketch suitable for transition to working/MF/. Full Cat A closure deferred to a future session; today's goal is *substantive advancement*.
**Depends on:** `02_exploration.md` Approach 6; `03_development.md` §12; canonical T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified; standard Allen-Cahn / gradient-flow / linearized-transport theory.

---

## §1. Objective

NQ-T-Identity-6 sketches a Cat A promotion path for T-Temporal-Identity that bypasses Sinkhorn dual-potential machinery (currently the S-B2 Cat A bottleneck) and instead uses the joint formation Hessian spectral gap $\mu_\mathrm{joint}$ from T-Persist-K-Sep / T-Persist-K-Unified.

If formalized: collapses Cat A timeline from ~6 sessions (post-NQ-5/OP-0011 closures) to ~3 sessions, since (i) S-B2 (Lemma 8.2 Cat A) becomes unnecessary; (ii) S-B3 / OP-0011 Step 2 becomes unnecessary (kernel uniqueness from Hessian uniqueness); (iii) dependency chain to T-Persist-K-Sep is purely canonical.

---

## §2. The transport-Hessian functional

### §2.1 Setup

Let $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$ with $\mathrm{PersComp}(u_t) = \{C_1^t, \ldots, C_K^t\}$, $\mathrm{PersComp}(u_s) = \{C_1^s, \ldots, C_K^s\}$ (stable-K). Let $\mathcal{M} = \{M : \mathcal{P} \times \mathcal{P} \to \mathbb{R}_{\geq 0}\}$ be the transport plan space.

Define the **transport-energy functional** with self-referential cost:
$$\mathcal{T}_{\varepsilon_\mathrm{OT}}(M; u_t, u_s) \;=\; \sum_{x,y} c[u_t](x,y)\,M(x,y) \;+\; \varepsilon_\mathrm{OT}\,H(M),$$
where $H(M) = \sum_{x,y} M(x,y)\log M(x,y) - M(x,y)$ is the entropy and the cost is self-referential:
$$c[u_t](x,y) = \lVert \varphi(u_t)(x) - \varphi(u_t)(y) \rVert^2 + \sigma_\mathrm{sp}^{-2}d_G(x,y)^2.$$

The Sinkhorn optimum $M^*$ satisfies the marginal constraints:
$$\sum_y M^*(x,y) \leq u_t(x),\quad \sum_x M^*(x,y) \leq u_s(y),$$
with at least one equality holding by complementary slackness (E1 sub-stochastic, E2 non-injective).

### §2.2 Connection to joint formation Hessian

The joint formation manifold is $\mathcal{F}_M^K \subset \prod_{k=1}^K \mathcal{F}_{m_k}(\mathcal{P})$ (canonical §12). The joint formation Hessian $H_\mathrm{joint}$ at the K-formation $(\hat u^1_t, \ldots, \hat u^K_t)$ has spectral gap $\mu_\mathrm{joint} \geq \min_k \mu_k - (K-1)\lambda_\mathrm{rep}$ (Weyl, canonical §12 line 1016).

**Heuristic:** A perturbation that maps $\mathrm{Core}(C_i^t)$ to $\mathrm{Core}(C_j^s)$ with $j \neq \pi(i)$ (off-diagonal transport) corresponds to a *joint-Hessian eigendirection* — specifically, a "swap" mode between formations $i$ and $j$. Such modes have eigenvalue $\geq \mu_\mathrm{joint}$ since they take the configuration *away* from the formation manifold.

### §2.3 Goal: bound $\eta_\mathrm{cross}$ in terms of $\mu_\mathrm{joint}$

We want a result of the form:
$$\eta_\mathrm{cross}^\mathrm{spec} \;\leq\; \exp\!\Big(-\frac{\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2}{\varepsilon_\mathrm{OT}}\Big),$$
where $d_\mathrm{inter}^* = $ minimum inter-component core distance.

The exponent has the right form: large $\mu_\mathrm{joint}$ (strong joint stability) ⇒ small $\eta_\mathrm{cross}$ (small off-diagonal transport).

---

## §3. Lemma 13 — Linearized transport-Hessian connection (sketched)

**Lemma 13 (sketch, Cat C target Cat A).** *Under (A1)–(A6) + T-Persist-K-Sep hypotheses (H1-K), (WS), (SR), (NB-K), the entropic-OT optimum $M^*$ satisfies:*

*Off-diagonal mass concentration*
$$\gamma_{M^*}(C_i^t, C_j^s) \leq \exp\!\Big(-\frac{\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2}{\varepsilon_\mathrm{OT}}\Big) \cdot \min(m_i^t, m_j^s),\quad \forall j \neq \pi(i).$$

*Equivalently, $\eta_\mathrm{cross}^\mathrm{spec}$ has the spectral form.*

### §3.1 Proof sketch (NOT fully formalized)

1. **Step 1 — Linearize the transport-energy functional around the formation.** At the entropic-OT optimum $M^*$, the second variation $\delta^2 \mathcal{T}_{\varepsilon_\mathrm{OT}}$ controls perturbation costs. For a perturbation $\delta M$ that conserves marginals:
$$\delta^2 \mathcal{T}_{\varepsilon_\mathrm{OT}} = \varepsilon_\mathrm{OT}\,\sum_{x,y}\frac{\delta M(x,y)^2}{M^*(x,y)}.$$
This is positive but the *effective* curvature for a *swap-mode* perturbation depends on how the perturbation projects onto formation Hessian eigendirections.

2. **Step 2 — Project onto formation Hessian.** A swap-mode $\delta M_{ij}$ that transports mass from $\mathrm{Core}(C_i^t)$ to $\mathrm{Core}(C_j^s)$ (instead of $\mathrm{Core}(C_{\pi(i)}^s)$) induces a corresponding *field perturbation* $\delta u^{j} = (\delta M_{ij})^\top \mathbf{1}$ on the time-$s$ field. This $\delta u^j$ deforms the K-formation by adding mass to $C_j^s$ from the wrong source.

The energy cost of this field perturbation is bounded below by joint Hessian + spatial transport:
$$\Delta E_\mathrm{form} \geq \frac{1}{2}\mu_\mathrm{joint}\,\lVert \delta u^j \rVert^2 + \tfrac{1}{2}\sigma_\mathrm{sp}^{-2}(d_\mathrm{inter}^*)^2\,\lVert \delta M_{ij} \rVert^2.$$
The first term: formation Hessian on $\delta u$. The second: spatial transport cost over distance $d_\mathrm{inter}^*$.

3. **Step 3 — Boltzmann concentration.** The entropic-OT optimum is a Boltzmann distribution over plans:
$$M^*(\delta M) \propto \exp(-\Delta E[\delta M]/\varepsilon_\mathrm{OT}).$$
Therefore the probability of a swap-mode perturbation of magnitude $\lVert \delta M_{ij} \rVert$ is bounded by:
$$\Pr[\lVert \delta M_{ij} \rVert > t] \leq \exp(-(\mu_\mathrm{joint} t^2 + \sigma_\mathrm{sp}^{-2}(d_\mathrm{inter}^*)^2 t^2)/(2\varepsilon_\mathrm{OT})).$$

4. **Step 4 — Mass interpretation.** Off-diagonal mass $\gamma(C_i^t, C_j^s) = \int t \cdot \Pr[\lVert \delta M_{ij} \rVert = t] dt$. By Gaussian-tail integration:
$$\gamma(C_i^t, C_j^s) \leq \min(m_i^t, m_j^s) \cdot \exp(-(\mu_\mathrm{joint} + \sigma_\mathrm{sp}^{-2}(d_\mathrm{inter}^*)^2)\,(d_\mathrm{inter}^*)^2 / (2\varepsilon_\mathrm{OT})).$$

The spatial term is $\geq 0$ and small for moderate $d_\mathrm{inter}^*$ (at $\sigma_\mathrm{sp}^2 = \mathrm{diam}^2/2 \approx 392$ and $d_\mathrm{inter}^* = 5$: $\sigma_\mathrm{sp}^{-2}(d_\mathrm{inter}^*)^2 = 25/392 \approx 0.064$, much smaller than $\mu_\mathrm{joint}$ at default).

Dropping the small spatial term and taking the exponent:
$$\gamma(C_i^t, C_j^s) \leq \min(m_i^t, m_j^s) \cdot \exp(-\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2 / (2\varepsilon_\mathrm{OT})).$$

This is the sketched bound.

### §3.2 Critical gaps in the proof sketch

1. **Step 1 second-variation formula.** The formula $\delta^2 \mathcal{T} = \varepsilon_\mathrm{OT}\sum (\delta M)^2/M^*$ is correct for entropy-only; the cost term contributes $\sum c \cdot \delta^2 M$ which vanishes for marginal-conserving perturbations only if $c$ is linear in $M$ (which it is). So this formula is correct.

2. **Step 2 projection.** This is the *crucial* and least rigorous step. Need to show that swap-mode plan perturbations actually *do* induce field perturbations that engage the joint formation Hessian. The connection requires:
   - $\delta M$ parametrized by both source ($\delta u^t$) and target ($\delta u^s$) field perturbations.
   - These field perturbations live in the joint-formation tangent space.
   - The joint Hessian acts on $(\delta u^t, \delta u^s) \in T \mathcal{F}^K_M \times T \mathcal{F}^K_M$.

   A clean formulation: $\Delta E_\mathrm{form}[\delta u^s | \delta M_{ij}, u_t] \geq \mu_\mathrm{joint} \cdot \lVert \delta u^s_{(j)} \rVert^2$ — energy increment for the $j$-th formation slot deformation. Need to formalize.

3. **Step 3 Boltzmann factor.** The entropic-OT plan is a *constrained* Boltzmann distribution (marginal constraints), not a free one. The naive Boltzmann argument needs adjustment for the marginal constraints — typically a saddle-point / Legendre-transform argument.

4. **Step 4 integration.** Gaussian-tail integration is standard; the constant in front depends on the variance of the Boltzmann distribution.

### §3.3 Aggregate status of Lemma 13

**Status:** Cat C (sketched, proof not closed). To upgrade to Cat A:
- Formalize Step 2 (joint-Hessian projection).
- Formalize Step 3 (constrained Boltzmann argument).
- Verify constants in Step 4.

**Estimated difficulty:** 1–2 sessions of dedicated formalization. Mid-high.

---

## §4. Quantitative comparison: spectral form vs sharp form

At default parameters (15×15 grid, $\beta = 20\alpha$, $\alpha = 1.0$, $K = 2$):

| Bound form | Exponent | $\varepsilon_\mathrm{OT}^*$ | Source |
|------------|----------|------------------------------|--------|
| Coarse (T-Persist-1(e) literal) | $\Delta_\varphi^2_\mathrm{inter} - \mathrm{diam}^2/\sigma_\mathrm{sp}^2 - \varepsilon_\mathrm{OT}\log n$ | ≈ 0.05 | `03_development.md` §3.3 |
| Sharp (Sinkhorn-Lipschitz) | $\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff}$ | ≈ 0.45 | `03_development.md` §8 |
| Variance | $\Delta_\varphi^2_\mathrm{inter} - \sqrt{V_g \varepsilon_\mathrm{OT} \mathrm{diam}}$ | ≈ 0.39 | `07_close_NQ4_robust.md` |
| **Spectral (NQ-6 sketched)** | $\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2 / 2$ | ≈ ? | this file §3 |

For default: $\mu_\mathrm{joint} \approx 70$ (canonical T-Persist-1(e) line 1816 measured), $d_\mathrm{inter}^* = 5$ (well-separated): exponent $\approx 70 \cdot 25 / 2 = 875$. **No** $\varepsilon_\mathrm{OT}^*$ ceiling — bound active for *any* $\varepsilon_\mathrm{OT}$ provided $\mu_\mathrm{joint} > 0$ and the linearization is valid.

**Implication if Lemma 13 is closed:** the spectral form has *no $\varepsilon_\mathrm{OT}$ ceiling* in the well-separated regime — the certified regime extends to *all $\varepsilon_\mathrm{OT}$*. This subsumes NQ-T-Identity-4b.

This is the *transformative* potential of NQ-T-Identity-6.

---

## §5. Cat A path collapse if Lemma 13 closes

### §5.1 Bypassed sub-steps

If Lemma 13 is fully proved (Cat A):
- **S-B2** (Sinkhorn-Lipschitz Lemma 8.2 Cat A) — bypassed; spectral form does not need it.
- **S-B3** (OP-0011 Step 2) — partially bypassed; under linearized-transport-Hessian analysis, kernel uniqueness follows from Hessian uniqueness (which is canonical Cat A under WS+SR).
- **S-B4** (NQ-5 full) — already closed today (Lemma 8); no change.
- **NQ-T-Identity-4b** — bypassed; no $\varepsilon_\mathrm{OT}^*$ ceiling.

### §5.2 New Cat A timeline (if Lemma 13 closes)

- Part (a) Cat A: 2 sessions (S-A1, S-A2 unchanged).
- Part (b) Cat A: 2 sessions (S-B1 iso-ratio + Lemma 13 formalization).
- Part (c) Cat A: 0 sessions (immediate corollary of Lemma 13 + canonical Hessian uniqueness).
- Part (d) Cat A: 1 session (S-D1 + S-D2 unchanged).

**Total Cat A:** ~5 sessions (down from 6, post-NQ-5/OP-0011-Step-2 closures).

The dominant remaining bottleneck is Lemma 13 itself (1–2 sessions).

### §5.3 Risk assessment

Lemma 13 has 4 critical gaps (§3.2). Each is non-trivial:
- Step 1: routine (already closed, just formula verification).
- Step 2: hardest (requires fresh joint-Hessian-vs-transport-perturbation theorem).
- Step 3: standard but requires care with marginal constraints.
- Step 4: routine.

**Estimated probability of full closure in 2 sessions:** ~50–60%. Higher reward, higher risk than NQ-5 / OP-0011 Step 2 closures (which were lower-risk in the standard sense).

---

## §6. Closure status

### §6.1 NQ-T-Identity-6 status: **PARTIALLY ADVANCED**

Today's advancement:
- Proposition 12.1 (`03_development.md` §12) extended into Lemma 13 with explicit 4-step proof outline.
- Critical gaps identified explicitly (§3.2).
- Quantitative comparison vs sharp/variance forms (§4) — spectral form, if closed, **has no $\varepsilon_\mathrm{OT}^*$ ceiling**.
- Cat A timeline collapse mapped (§5.2): from 6 → ~5 sessions if Lemma 13 closes.

### §6.2 Genuinely open

- Lemma 13 full proof closure (§3.2 critical gaps).
- Validation: numerical anchor showing that the spectral bound holds at large $\varepsilon_\mathrm{OT}$ (recommended: exp variant at $\varepsilon_\mathrm{OT} \in \{1, 2, 5\}$, comparing measured $\eta_\mathrm{cross}$ vs $\exp(-\mu_\mathrm{joint}(d_\mathrm{inter}^*)^2/(2\varepsilon_\mathrm{OT}))$).

### §6.3 NQ priority re-ranking after today's closures

| Rank | NQ | Status | Reason |
|------|----|----|---|
| ~~1~~ | NQ-T-Identity-5 | **CLOSED** today | Lemma 8 |
| ~~2~~ | NQ-T-Identity-1 | **CLOSED** today | Lemma 10 + Route B |
| **1** | **NQ-T-Identity-6** | PARTIALLY ADVANCED | High-reward Cat A timeline collapse; ~50% closure probability in 2 sessions |
| ~~3~~ | NQ-T-Identity-4 | **PARTIALLY CLOSED** | 4a closed, 4b open low-priority |
| 2 | NQ-T-Identity-2 (iso-ratio) | OPEN | Required for S-B1 |
| 3 | NQ-T-Identity-3 (time-varying topology) | OPEN | W9+ priority |

After today's session: tomorrow's seed is **NQ-T-Identity-6** (continue closure) or T-σ-Inherit Cat B Review (Option B, applied with refined Theorem T-Temporal-Identity).

---

## §7. Cross-references for `04_integration_and_new_open.md`

When refreshing integration/new-open file:

1. NQ-T-Identity-6 **PARTIALLY ADVANCED**.
2. Lemma 13 (sketched, Cat C target Cat A) registered.
3. Cat A timeline collapse if Lemma 13 closes: 6 → 5 sessions.
4. Spectral form would have *no $\varepsilon_\mathrm{OT}^*$ ceiling*, subsuming NQ-T-Identity-4b.
5. Tomorrow's seed re-ranked: NQ-T-Identity-6 (high-reward) or T-σ-Inherit (lower-risk).

---

*End of `08_NQ6_spectral_gap_advance.md`.*
