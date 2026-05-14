> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 02_exploration.md — T-Temporal-Identity Cat B Tightening: Restatement, Multi-Approach, Primary Selection

**Session:** 2026-05-07 (Thu, W6 Day 5)
**Target (from `00_plan.md` Option A):** Tighten T-Temporal-Identity to a narrow Cat B theorem (parts a, b, d) — explicit assumption package A1–Ak, computable margin condition $\Delta_\mathrm{sep}$, canonical-ready statement. Part (c) (kernel independence) explicitly Cat C.
**This file covers:** §4.1 Restatement; §4.2 Multi-approach (≥3 mathematically independent paths); §4.3 Primary selection rationale.
**Depends on reading:** `canonical.md` §§3 (universe), §7.1 (persist_transport), §8.5 (E1–E4), §12 (multi-formation), §13 T-Persist-1(e), T-Persist-K-Sep; `theorem_status.md` OP-0011, OP-0012, T-Temporal-Identity Session V/X notes; `working/MF/temporal_identity_perscomp_transport.md` (full); `CODE/experiments/exp83_temporal_identity_transport.py` + results JSON.

---

## §1. Restatement

### §1.1 Working-file claim (paraphrased)

`working/MF/temporal_identity_perscomp_transport.md` §6.1 proposes T-Temporal-Identity in four parts. The narrowed Cat B target collapses the universal claim into:

> **Cat B target (working draft):** Let $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$ be soft cohesion fields on a finite graph. Let $\mathrm{PersComp}(u_t)$, $\mathrm{PersComp}(u_s)$ be their persistent-component sets (D-ST-3 thresholded super-level CC). Let $M_{t\to s}$ be an admissible transport plan (E1–E4, canonical §8.5). Define the normalized score matrix $\tilde{\mathbf{S}} \in \mathbb{R}^{K_t \times K_s}$ via §4 of the working file. Then:
> - **(a)** A relation $R_{t \to s} \subseteq \mathrm{PersComp}(u_t) \times \mathrm{PersComp}(u_s)$ exists, obtained by thresholding $\tilde{\mathbf{S}}$ with $\tau_\mathrm{id}, \tau_\mathrm{split}, \tau_\mathrm{merge}, \tau_\mathrm{birth}, \tau_\mathrm{death}$, classifying every component pair into one of five mutually-exclusive event types.
> - **(b)** Under stable-K ($K_t = K_s = K$), no birth/death, and an explicit margin condition $\Delta_\mathrm{sep} > 0$, $R_{t \to s}$ is a unique bijection given by the row-argmax permutation.
> - **(d)** When $K_t = K_s = 1$, $R_{t \to s}$ is non-empty $\iff$ `persist_transport`$(u_t, u_s, M_{t \to s}, \theta_\mathrm{core}) \geq \tau_\mathrm{id}$ (up to a fixed re-scaling).

### §1.2 What is question / data / success / failure?

**Question.** Can the working-file Cat B sketch (parts a, b, d) be tightened so that:
1. the assumption package (A1–Ak) is finite, explicit, and verifiable on any concrete instance;
2. the margin $\Delta_\mathrm{sep}$ has a *computable* lower bound expressed in terms of canonical-grade quantities (graph distances, fingerprint gap, $\beta/\alpha$, $\varepsilon_\mathrm{OT}$);
3. the proof chains to existing Cat A results (T-Persist-1(e), T-Persist-K-Sep restricted to its sep range $D_\mathrm{sep}\geq 3$, isoperimetric ordering, IFT, basin radius);
4. part (c) remains explicitly Cat C with a stated dependency on OP-0011 Step 2 (component-level confinement bound).

**Data.**
- canonical Cat A engine pieces: T-Persist-1(a)–(c)(e) Cat A; T-Persist-1(d) Cat C; T-Persist-K-Sep proved (regime-conditional Cat C, but its proved content suffices in the well-separated regime); two-tier transport concentration with 3-component fingerprint.
- E1–E4 admissibility (§8.5): sub-stochasticity, non-injectivity, core-inheritance solution-constraint, fingerprint-cost structural sensitivity.
- exp83 numerical anchor (Session X, 2026-05-06): 4/4 scenarios PASS; observed $\Delta_\mathrm{sep} \approx 0.726$ (Scenario A, 2 well-separated blobs) and $\approx 0.714$ (Scenario D, birth + continuation), with $\lambda_m = 1.0$, $\lambda_c = 0.005$, $\varepsilon_\mathrm{OT} = 1.0$, $\rho_\mathrm{pers} = 0.28$.
- working file §6.4 proof sketch (5 numbered steps).

**Success criterion.** A canonical-ready theorem statement consisting of:
- the assumption package (A1)–(A8);
- part (a) (existence, constructive, 0 blockers);
- part (b) (uniqueness under (A1)–(A8) including a margin condition $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^*$ where $\Delta_\mathrm{sep}^*$ is given by an explicit closed-form lower bound);
- part (d) (K=1 reduction to `persist_transport`);
- explicit Cat-B/C self-classification per part;
- explicit list of items NOT proved (Cat C riders kept open);
- promotion-pipeline criteria (what remains for canonical promotion in a future session).

**Failure modes.** The session fails to meet success if:
- the margin lower bound cannot be expressed without invoking T-Persist-1(d) Cat C (which would propagate Cat C up); or
- the bound is purely existential ("there exists a constant", with no formula); or
- silent reliance on OP-0011 Step 2 (component confinement) is required for part (b) — this would collapse (b) and (c) into a single Cat C claim.

### §1.3 Surfaced implicit assumptions

`00_plan.md` and the working file leave several assumptions implicit. We surface them now so that subsequent development can address each explicitly.

1. **Same vertex set across $t$ and $s$.** Working file uses $\mathcal{P}_t$, $\mathcal{P}_s$ (allowing different vertex sets), but the canonical transport kernel $M_{t\to s} : \mathcal{P}_t \times \mathcal{P}_s \to [0,1]$ is naturally defined on the product. For Cat B we restrict to $\mathcal{P}_t = \mathcal{P}_s =: \mathcal{P}$ (same finite graph at both times). Time-varying graph topology is deferred (out of scope; would require OP-0009 architecture maturation).
2. **Volume conservation across time.** $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$ with the *same* $M$. (E1 sub-stochasticity allows transported mass to drop below $M$, but both endpoints are in the same simplex by assumption.)
3. **PersComp definition.** D-ST-3 (canonical) requires threshold-stable connected components. exp83 uses a *proxy* via threshold + scipy CC; this proxy is NOT D-ST-3 but is monotone in $\rho_\mathrm{pers}$ and matches D-ST-3 on the well-separated regime. The Cat B statement uses D-ST-3; the numerical anchor uses the proxy. We will flag this gap in the non-overclaim register.
4. **Cost function.** Working file §4.1 uses $c(x,y) = \|\varphi(x) - \varphi(y)\|^2 + \sigma_\mathrm{sp}^{-2} \|x - y\|^2$. Canonical T-Persist-1(e) machinery uses essentially the same cost up to scaling. We commit to one explicit cost form and check that it satisfies the conditions of T-Persist-1(e) (TC1–TC3).
5. **Score normalization.** $\tilde S_{ij}^0 = S_{ij}^0 / \min(m_i^t, m_j^s)$ — the choice is implicit; alternatives (max, geometric mean, sum) lead to different margin formulas. We commit to $\min$.
6. **Component "pairing" in (b).** The working file says "$K_t = K_s$ + no birth/death + margin", but does not name the bijection $\pi$ that "should" hold. We make $\pi$ explicit as the row-argmax permutation and prove it agrees with the column-argmax permutation under (A8) (mutual-max consistency).
7. **Threshold parameters.** $\tau_\mathrm{id}$, etc., are calibration parameters of the *classifier*, not of the *theorem*: the theorem states "(b) $R_{t\to s}$ is a bijection" without depending on $\tau_\mathrm{id}$, provided $\Delta_\mathrm{sep} > 0$ (which already implies all diagonal entries are above any reasonable $\tau_\mathrm{id}$).

### §1.4 Cat B vs Cat C cleanly separated

The narrowed Cat B target is:
- (a) Existence — Cat B candidate (constructive; routine).
- (b) Uniqueness under (A1)–(A8) — Cat B target with explicit $\Delta_\mathrm{sep}^*$.
- (d) K=1 reduction — Cat B candidate (algebra).

Explicit Cat C riders (kept open):
- (c) Kernel independence — Cat C, blocked by OP-0011 Step 2 (component confinement bound on $|\gamma_M - \gamma_{M'}|$).
- (b') Stochastic / Langevin transport plan from Package II — Cat C, blocked by OP-0021 (T_* registration) + Package II (Eyring-Kramers).
- (b'') Multi-step composition $R_{t\to r} = R_{s\to r} \circ R_{t\to s}$ — Cat C overall; OP-0012-CC candidate is the Cat B target (separate session).
- $\sigma$-extension (full score $S_{ij}$) — Cat C, blocked by OP-0008 / T-σ-Inherit.

---

## §2. Multi-approach generation (≥3 mathematically independent paths)

We generate five candidate approaches. §2.6 audits independence.

### §2.1 Approach 1 — OT-concentration cascade (analytical, with Sinkhorn dual-potential refinement)

**Core idea.** Use T-Persist-1(e) two-tier concentration to bound:
- *diagonal* mass $\gamma(C_i^t, C_{\pi(i)}^s) \geq (1 - \eta_\mathrm{self}) \cdot \min(m_i^t, m_{\pi(i)}^s)$, and
- *off-diagonal* mass $\gamma(C_i^t, C_j^s) \leq \eta_\mathrm{cross}(\Delta_\varphi^2_\mathrm{inter}) \cdot \min(m_i^t, m_j^s)$ for $j \neq \pi(i)$.

**Coarse form** (union bound, T-Persist-1(e) line 1810 directly applied):
$$\eta_\mathrm{cross}^\mathrm{coarse} \leq n \cdot \exp\!\left(-\frac{\gamma_\mathrm{OT}\,\Delta_\varphi^2_\mathrm{inter} - \mathrm{diam}(\mathcal{P})^2/\sigma_\mathrm{sp}^2}{\varepsilon_\mathrm{OT}}\right).$$

**Sharp form** (Sinkhorn dual-potential Lipschitz argument, replaces union bound with a row-restricted analysis; see `03_development.md` §8 for full derivation):
$$\eta_\mathrm{cross}^\mathrm{sharp} \leq \exp\!\left(-\frac{\gamma_\mathrm{OT}\,\Delta_\varphi^2_\mathrm{inter} - L_g\,d_\mathrm{eff}}{\varepsilon_\mathrm{OT}}\right),$$
where $L_g \leq L_c$ is the dual-potential Lipschitz constant (Lemma 8.2; bounded by the cost Lipschitz constant via log-sum-exp inequality) and $d_\mathrm{eff}$ is the effective Sinkhorn-ball radius. The sharp form is tighter than coarse by a factor $n \exp(L_g d_\mathrm{eff} - \mathrm{diam}^2/\sigma_\mathrm{sp}^2)/\varepsilon_\mathrm{OT}$ — at default parameters ($n=225$): factor $\sim 6 \times 10^4$.

**Margin closed-form (sharp).**
$$\Delta_\mathrm{sep}^* \geq \lambda_m\big[\rho_\mathrm{deep}(1 - \eta_\mathrm{self}^{\,K}) - \eta_\mathrm{cross}^\mathrm{sharp}\big] - \lambda_c \cdot \bar c_\mathrm{intra}.$$

**Certified regime $\varepsilon_\mathrm{OT}^*$.**
- Coarse form: $\varepsilon_\mathrm{OT}^* \approx 0.05$ (default 15×15 grid).
- **Sharp form: $\varepsilon_\mathrm{OT}^* \approx 0.45$** (factor-9 improvement; brings exp83's $\varepsilon_\mathrm{OT}=1$ within factor 2.2 of certified threshold).

**Success form.** Closed-form $\Delta_\mathrm{sep}^*$ as a function of $(\lambda_m, \lambda_c, \beta/\alpha, \varepsilon_\mathrm{OT}, d_\mathrm{inter}^*, \Delta_\varphi^2_\mathrm{inter}, L_g, d_\mathrm{eff}, n)$. **Cat B sharp form** chains T-Persist-1(e) Cat A + Sinkhorn-Lipschitz Lemma 8.2 (Cat B; needs Bigot–Cazelles–Papadakis Lipschitz bound formalized for our cost class). **Cat A sharp form** = Cat B + S-B2 promotion of Lemma 8.2.

**Failure mode (sharp form).** Requires $\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} > L_g\,d_\mathrm{eff}$ — strictly weaker than coarse form's TC3. In strongly-overlapping or near-bifurcation regimes ($\mu \to 0$, hence $\Delta_\varphi^2_\mathrm{inter} \to 0$), the bound becomes vacuous. The sharp form preserves the failure-mode boundary location (failure still at strong-overlap / near-bifurcation) but with a ~9× larger certified regime above that boundary.

**Interaction with existing theory.** Hooks directly into T-Persist-1(e) Cat A + standard Sinkhorn theory (entropic-OT dual potentials). Reuses the canonical 3-component fingerprint. Compatible with T-Persist-K-Sep ($D_\mathrm{sep} \geq 3$). Does not invoke T-Persist-1(d) Cat C.

### §2.2 Approach 2 — Linear-programming / Hungarian assignment (algorithmic-dual)

**Core idea.** Recognize $\tilde{\mathbf{S}}$ as the cost (negated) matrix of a maximum-weight bipartite matching. By LP duality (König–Egerváry / Hungarian), the maximum-weight matching is unique iff the LP has a unique vertex solution, which holds iff no two distinct row-argmax permutations achieve the same sum. The margin condition $\Delta_\mathrm{sep} > 0$ implies row-wise unique argmax, and the bijection follows from a *row-by-row independence lemma*.

**Success form.** $\Delta_\mathrm{sep}$ characterized as the LP-dual gap. The bijection structure is a consequence of total unimodularity + uniqueness. Connection to $\sigma$-rich would extend via permutation invariance.

**Failure mode.** LP duality only gives the bijection, not a *quantitative* lower bound on $\Delta_\mathrm{sep}^*$ — the bound has to come from outside the LP. This approach yields the *structural* claim but not the canonical Cat B numerical anchor. **Failure occurs at the requirement to express $\Delta_\mathrm{sep}^*$ in canonical quantities.**

**Interaction with existing theory.** Adds a discrete-optimization layer not currently in canonical (no precedent for LP/Hungarian in canonical). May be a useful *internal* lemma but cannot be the primary path.

### §2.3 Approach 3 — Topological / persistent-homology stability (comparative)

**Core idea.** Treat $R_{t\to s}$ as the discrete analogue of the *bottleneck-stable* matching between persistence diagrams $\mathrm{Dgm}(u_t)$ and $\mathrm{Dgm}(u_s)$. Stability theorems (Cohen-Steiner–Edelsbrunner–Harer) give: bottleneck distance between diagrams is $\leq \|u_t - u_s\|_\infty$. Lift the bottleneck matching to a component-level bijection.

**Success form.** $\Delta_\mathrm{sep}^*$ would relate to the *gap between persistence pairs* in $\mathrm{Dgm}(u_t)$ — a topologically invariant quantity not depending on transport plan choice, automatically resolving part (c) (kernel independence) as a corollary of bottleneck stability.

**Failure mode.** (i) Bottleneck stability uses $L^\infty$ distance between fields, which is *not* the natural object in SCC (transport-based persist is the canonical metric). (ii) $\mathrm{Dgm}$ uses $H_0$ super-level filtration, which captures component birth/death but not *identity* across time. Identity tracking via persistence diagrams requires *vineyards* / *zigzag* persistence — these are non-canonical extensions. (iii) Provides no link to the SCC self-referential cost or fingerprint $\varphi$. **Failure: SCC primitive is $u_t$ via transport, not topological filtration.**

**Interaction with existing theory.** Currently no persistent-homology infrastructure in canonical. Would require introducing Dgm-based tracking — significant new commitment that contradicts CN8 (4 energy terms primitive) and CN10 (no reduction to external frameworks).

### §2.4 Approach 4 — Constructive counterexample + perturbation (constructive)

**Core idea.** Try to construct a counterexample: two admissible transport plans $M$, $M'$ giving distinct $R_{t\to s}$ relations under stable-K + (apparent) margin condition. Either succeed (refuting the working draft and forcing an additional assumption) or fail (then the failure mode reveals the critical hypothesis).

**Success form (negative).** A refuting example would force an additional assumption A_extra and refine the Cat B claim.

**Success form (positive).** Failure to refute, by repeated counterexample attempts, narrows the necessary condition and *empirically supports* the working draft.

**Failure mode (as a primary approach).** Counterexample search alone does not produce a *theorem*. It is an *audit* technique, not a development technique.

**Interaction with existing theory.** Useful as a sanity check on Approach 1's bound. Will be folded into §3 (Primary development) as Lemma-stage counterexample tests.

### §2.5 Approach 5 — Probabilistic / Markov-kernel formulation (axiomatic-reframe)

**Core idea.** Define $P(C_j^s \mid C_i^t) \propto \tilde S_{ij}^0 \cdot \mathbf{1}[\tilde S_{ij}^0 \geq \tau_\mathrm{id}]$ (working-file §7.2). Show that under stable-K + margin, $P$ is concentrated on a permutation matrix (so $R_{t\to s}$ is the deterministic limit). Then $R_{t\to r} = R_{s\to r} \circ R_{t\to s}$ becomes a Markov-chain composition (Chapman–Kolmogorov) — directly addressing OP-0012-CC.

**Success form.** Probabilistic Cat B for parts (a), (b), (d). OP-0012-CC becomes a corollary. Stochastic transport (Package II, OP-0021) plugs in naturally as noise on top of the deterministic permutation.

**Failure mode.** Requires interpreting $\tilde S_{ij}^0$ as a likelihood — but the score is a *signed* quantity, not a probability density. Normalizing it to a Markov kernel is ad hoc unless tied to a thermodynamic potential ($\propto e^{-S/T_*}$). Such tie introduces dependence on $T_*$ (OP-0021 OPEN). **Failure: smuggles in P-F-A1 / T_* dependence, breaking Cat B independence from OP-0021.**

**Interaction with existing theory.** Enabling for OP-0012-CC at Cat B level — but needs T_* canonicalized first. Defer to Session post-OP-0021.

### §2.6 Independence audit

We check pairwise that the five approaches are *mathematically independent* (different tools / different failure modes / different conditional success conditions).

| Pair | Same idea? | Same failure mode? | Same conditional? | Independent? |
|------|------------|--------------------|-------------------|--------------|
| 1 vs 2 | No (analytical OT vs LP duality) | No (TC3 violation vs LP-quantitative gap) | No (deep-core regime vs unique LP vertex) | **Independent** |
| 1 vs 3 | No (transport vs filtration) | No (fingerprint gap vs L∞ stability) | No (entropic OT vs PH bottleneck) | **Independent** |
| 1 vs 4 | No (analytic vs constructive) | No (TC3 vs successful counterexample) | N/A (different epistemic mode) | **Independent** in epistemic mode |
| 1 vs 5 | No (deterministic vs Markov) | No (TC3 vs T_* dependence) | No (β/α regime vs Gibbs-likelihood interpretation) | **Independent** |
| 2 vs 3 | No (LP vs PH) | No (LP gap vs L∞ stability) | No | **Independent** |
| 2 vs 5 | Both discrete optimization on $\tilde{\mathbf{S}}$ | Different (LP gap vs P-F dependence) | Different (LP vertex vs Boltzmann normalization) | **Independent (close but distinct)** |
| 3 vs 5 | Both lift the matrix to a higher-level object (PH / Markov) | No | No | **Independent** |

Conclusion: at minimum **three mutually independent approaches** (1, 2, 3) by all three independence criteria; with 4 and 5 as additional independent paths if epistemic-mode counterexample-style and probabilistic-axiomatic style are admitted. Quality bar of the prompt §5 met.

---

## §3. Primary selection rationale

### §3.1 Selected primary: Approach 1 (OT-concentration cascade)

**Rationale.**

1. **Hooks Cat A engine directly.** T-Persist-1(e) is canonical Cat A (after CV-1.1 strengthening). Approach 1's $\eta_\mathrm{cross}$ formula is *literally* the two-tier concentration applied component-by-component. Inheriting Cat A status of the upstream argument gives Cat B status to the downstream conclusion.
2. **Closed-form margin.** The bound on $\Delta_\mathrm{sep}^*$ is expressible in canonical-grade quantities — $\beta, \alpha, \varepsilon_\mathrm{OT}, d_\mathrm{inter}^*, \Delta_\varphi^2_\mathrm{inter}, \lambda_m, \lambda_c, n$ — none of which require new axiom commitments.
3. **Numerical anchor compatible.** exp83 Scenario A: $\Delta_\mathrm{sep} \approx 0.726$ at $\lambda_m=1, \lambda_c=0.005, \varepsilon_\mathrm{OT}=1, d_\mathrm{inter}^* \approx 8$ nodes. Approach 1 should predict $\Delta_\mathrm{sep}^* \in [0.5, 1)$ at these parameters — order of magnitude consistent.
4. **Avoids OP-0021 / OP-0011 dependencies.** Part (b) is established without the component confinement bound (OP-0011 Step 2) and without $T_*$ canonicalization (OP-0021). Part (c) is left as Cat C with explicit OP-0011 dependency, as the plan requires.
5. **Doesn't introduce new infrastructure.** No persistent-homology, no LP solvers, no Markov kernels. All structures already in `scc/transport.py`.

### §3.2 Why approaches 2, 3, 5 are not primary

- **Approach 2 (LP duality).** Cannot supply a *quantitative* lower bound on $\Delta_\mathrm{sep}^*$ — it gives uniqueness conditional on a nonzero gap, but the gap size itself comes from outside. Will be **internally absorbed** as Lemma in §4 of `03_development.md` (mutual-max ⇔ row-argmax bijection on finite matrices with strict gap).
- **Approach 3 (PH bottleneck).** Conflicts with CN10 (no reductive equivalence to external frameworks). Adds infrastructure (vineyards / zigzag) not currently canonical. Defer indefinitely.
- **Approach 5 (Markov / T_*).** Requires OP-0021 canonical $T_*$ to get Cat B; would otherwise smuggle in P-F-A1 dependency. Defer to post-Package-II session.

### §3.3 Use of approach 4 (counterexample audit)

Approach 4 is folded into the primary development as:
- (i) sanity-check counterexamples in §3.5 of `03_development.md` (does the proposed bound break under specific stress configurations);
- (ii) the explicit "no counterexample found in scope" entry in the non-overclaim register.

It is not the primary, but it *protects* the primary against silent over-reach.

### §3.4 Preserved alternatives for future sessions

If Approach 1 fails in development (e.g., the closed-form $\Delta_\mathrm{sep}^*$ requires invoking T-Persist-1(d) Cat C and propagates Cat C up):
- **Fallback to Approach 2** with $\Delta_\mathrm{sep}$ stated as an existential quantity (LP gap exists; no quantitative bound) — yields a *weaker* Cat B claim that holds whenever the LP is regular, but loses the numerical anchor compatibility.
- **Fallback to a Cat C statement** with kernel-dependent $\Delta_\mathrm{sep}$, deferring promotion.
- **Approach 5 as future Cat B / Cat A path** once OP-0021 closes.

These are recorded in §3 of `04_integration_and_new_open.md` for future activation.

---

## §4. Output of this file (handover to `03_development.md`)

`03_development.md` shall produce, in order:

1. Notation block (consistent with `working/MF/temporal_identity_perscomp_transport.md` §2 + canonical §3, §7.1, §8.5).
2. Assumption package (A1)–(A8), each verifiable on a finite graph instance.
3. Lemma 1 (Score matrix construction): well-defined finite-dimensional matrix; non-degenerate denominator under (A2)–(A3).
4. Lemma 2 (Diagonal lower bound): under (A4)–(A8) + T-Persist-1(e), $\gamma(C_i^t, C_{\pi(i)}^s) \geq (1 - \eta_\mathrm{self}) \min(m_i^t, m_{\pi(i)}^s)$.
5. Lemma 3 (Off-diagonal upper bound): under (A5), (A8) + T-Persist-1(e), $\gamma(C_i^t, C_j^s) \leq \eta_\mathrm{cross} \min(m_i^t, m_j^s)$ for $j \neq \pi(i)$.
6. Lemma 4 (Mutual-max ⇔ argmax bijection, finite-matrix algebra).
7. **Theorem T-Temporal-Identity Cat B** (parts a, b, d, narrowed scope) with explicit closed-form $\Delta_\mathrm{sep}^*$.
8. Counterexample audit (3 stress tests): Strong-overlap regime, near-bifurcation, kernel-perturbation.
9. K=1 reduction (part d).
10. Self-classification (per part: Cat A / Cat B / Cat B-conditional / Cat C) and explicit non-overclaim register.

`04_integration_and_new_open.md` shall produce: integration with canonical §13, OP impact (OP-0011/0012/0008), new open questions (≥3), prompt-improvement notes.

`99_summary.md` shall produce: 3–5 sentence session summary + tomorrow's seed.

---

*End of `02_exploration.md`.*
