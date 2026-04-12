# Iteration 10 — Publication-Ready Paper Outlines

**Date:** 2026-03-27

---

# PAPER 1: Mathematics Paper

## Target Venue

**Journal of Mathematical Physics** or **Annales de l'Institut Henri Poincaré (C) — Analyse Non Linéaire**

---

## Title

**Self-Referential Phase Fields on Graphs: A Variational Theory of Pre-Objective Cohesion**

---

## Draft Abstract

We introduce a variational framework for cohesive formation on finite weighted graphs in which the energy functional is self-referential: the operators defining the energy depend on the field being minimized. The theory extends the Allen–Cahn / Ginzburg–Landau model with two structurally novel terms — a closure energy measuring deviation from a non-idempotent contractive completion operator, and a separation energy measuring self-referential distinction of the field from its own complement. We prove: (i) existence of non-trivial volume-constrained minimizers via a computable phase transition criterion involving the graph's Fiedler eigenvalue (Theorem 1); (ii) uniqueness of the contractive closure fixed point with geometric convergence rate, yielding a strictly positive-definite Hessian contribution absent in idempotent closure (Theorem 2); (iii) enhanced metastability — self-referential energy basins are provably deeper than their Allen–Cahn counterparts (Theorem 3); (iv) gradient flow convergence via the Łojasiewicz inequality for the analytic energy (Theorem 4); (v) Γ-convergence to a perimeter functional with modified surface tension in the sharp-interface limit (Theorem 5). We construct a resolvent co-belonging operator on cohesion-weighted graphs that achieves three orders of magnitude discrimination between within-formation and cross-boundary site pairs, and propose a self-referential optimal transport formulation where the transport cost depends on the fields being transported — a fixed-point problem in transport-plan space whose existence we establish via Brouwer's theorem. Computational experiments on grid graphs confirm formation existence, verify gradient accuracy to $10^{-9}$, and validate the diagnostic vector framework. We identify eight open problems, including self-referential transport uniqueness, renormalization group relevance of the separation term, and multi-formation architecture.

**(248 words)**

---

## Section Structure

### 1. Introduction (3–4 pages)

**Content:**
- Motivation: phase-field models on graphs lack self-referential operator structure. Standard Allen–Cahn treats the double-well and Laplacian as fixed; here, two of four energy terms involve operators that depend on the field being optimized.
- The triple-mode self-referential structure: self-completion (closure), self-contrast (distinction), self-integration (co-belonging). Emphasize this is *not* generic nonlinearity — it is three structurally distinct modes of self-dependence entering through independent channels.
- Informal statement of main results (phase transition, enhanced metastability, Γ-convergence, gradient flow convergence, self-referential transport existence).
- Positioning statement: the framework sits at the intersection of phase-field theory, spectral graph theory, optimal transport, and persistent homology, but reduces to none of these. CN10 applies: contrastive comparison, not reductive identification.

**Key references to position against:**
- Allen–Cahn / Cahn–Hilliard on graphs (van Gennip & Bertozzi, 2012)
- Mumford–Shah on graphs (spectral approaches)
- Graph cuts and spectral clustering (Shi & Malik, 2000)
- Phase-field models with non-standard potentials
- Optimal transport on discrete spaces (Peyré & Cuturi, 2019)

**What is genuinely new (honest assessment):**
1. The closure energy $\mathcal{E}_{\rm cl} = \|u - {\rm Cl}(u)\|^2$ where Cl is a non-idempotent contraction — no analogue in phase-field literature.
2. The separation energy $\mathcal{E}_{\rm sep} = \sum u_i(1 - D_i(1-u))$ where D depends on the field's own complement — no analogue in *any* existing variational framework.
3. The proved stability advantage of non-idempotent closure (positive-definite vs. semidefinite Hessian).
4. Self-referential optimal transport where cost depends on transported quantity.
5. Resolvent co-belonging on cohesion-weighted graphs as a structural integration operator distinct from spectral clustering.

**What is incremental:**
- The Allen–Cahn component ($\mathcal{E}_{\rm bd}$) is standard.
- Volume-constrained minimization on graphs is well-studied.
- Γ-convergence for the leading term is Modica–Mortola; the self-referential corrections are perturbative.

### 2. Formal Framework (5–6 pages)

**2.1. Setup and Notation**
- Finite weighted graph $(X, N)$, cohesion field $u: X \to [0,1]$, volume constraint $\Sigma_m$.
- Ordered-pair summation convention (load-bearing for T8-Core; state explicitly).

**2.2. The Operator Triad**
- *Closure operator* ${\rm Cl}_t$: sigmoid form, axioms A1'–A4. State parameter constraint $a_{\rm cl} < 4$.
- *Distinction operator* $D_t(x; 1-u)$: sigmoid comparison of aggregated interior vs. exterior. State $b_D = 0$ for analyticity.
- *Co-belonging operator* $C_t = (I - \alpha W_{\rm sym})^{-1}$: resolvent on cohesion-weighted adjacency. State convergence condition $\alpha \rho(W_{\rm sym}) < 1$.
- Emphasize: definition graph is acyclic (field → operators → energy); computation graph is cyclic (energy → gradient → field update). This is CN3.

**2.3. Energy Functional**
- Four terms: $\mathcal{E} = \lambda_{\rm cl}\mathcal{E}_{\rm cl} + \lambda_{\rm sep}\mathcal{E}_{\rm sep} + \lambda_{\rm bd}\mathcal{E}_{\rm bd} + \lambda_{\rm tr}\mathcal{E}_{\rm tr}$.
- For the static theory (this paper's primary focus): $\lambda_{\rm tr} = 0$.
- State each term with full definitions. Emphasize: $\mathcal{E}_{\rm cl}$ and $\mathcal{E}_{\rm sep}$ are the novel contributions; $\mathcal{E}_{\rm bd}$ is the Allen–Cahn substrate.

**2.4. Derived Diagnostics**
- Proto-cohesion diagnostic vector $\mathbf{d} \in [0,1]^4$: Bind, Sep, Inside (via $\mathcal{Q}_{\rm morph}$), Persist.
- Morphological quality $\mathcal{Q}_{\rm morph} = \ell_{\max} \cdot {\rm Artic}$ from $H_0$ persistence diagrams.
- Co-belonging enters predicates (Sep) but *not* the energy. State this as an architectural decision, not an oversight.

**Figure 1:** Schematic of the self-referential energy architecture. Show: field $u$ feeds into Cl, D, C; these produce $\mathcal{E}_{\rm cl}$, $\mathcal{E}_{\rm sep}$ (D enters energy; C enters only diagnostics); $\mathcal{E}_{\rm bd}$ is field-only; gradient flows back to update $u$.

### 3. Main Results: Static Theory (6–8 pages)

**SELECT THESE 8 THEOREMS (strongest, cleanest):**

**Theorem 1 (Closure Fixed Point and Contraction).** *[T6a + T6b]* The sigmoid closure on $[0,1]^n$ has at least one fixed point (Brouwer). For $a_{\rm cl} < 4$, the fixed point is unique and iterates converge geometrically at rate $a_{\rm cl}/4$ (Banach contraction).

*Proof sketch:* Brouwer for existence; Lipschitz bound $\max \sigma' \cdot a_{\rm cl}/4 < 1$ for contraction.

**Theorem 2 (Non-Idempotent Stability Advantage).** *[T3/T6]* At a non-idempotent closure fixed point with $\|J_{\rm Cl}\|_{\rm op} < 1$, the closure Hessian $2(I - J_{\rm Cl})^T(I - J_{\rm Cl})$ is strictly positive definite ($n/n$ positive eigenvalues). For idempotent closure, $\leq (n-k)/n$ positive eigenvalues.

*Proof:* Gram matrix analysis. This is the paper's most conceptually distinctive result — it gives a *mathematical reason* to prefer non-idempotent closure beyond philosophical commitment.

**Theorem 3 (Phase Transition — Non-Trivial Minimizer Existence).** *[T8-Core]* On a connected graph with Fiedler eigenvalue $\lambda_2 > 0$, volume fraction $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$, and $\beta/\alpha > 4\lambda_2/|W''(c)|$: the global minimizer of $\mathcal{E}_{\rm bd}|_{\Sigma_m}$ is non-uniform.

*Proof:* Second variation at uniform state; ordered-pair convention gives Hessian $4\alpha L + \beta W''(c)I$ on $\Sigma_m$; negative eigenvalue implies saddle point; compactness gives non-uniform global minimizer.

**Theorem 4 (Enhanced Metastability).** *[T7-Enhanced]* Non-trivial minimizers of the full SCC energy have strictly larger energy barriers than corresponding Allen–Cahn minimizers with the same $\mathcal{E}_{\rm bd}$.

*Proof:* The closure term adds $\lambda_{\rm cl} \cdot 2(I - J_{\rm Cl})^T(I - J_{\rm Cl})$ to the Hessian — positive definite by Theorem 2 — deepening every energy basin.

**Theorem 5 (Gradient Flow Convergence).** *[T14]* The projected gradient flow on $\Sigma_m$ converges to a critical point. For analytic energy (with $b_D = 0$), convergence is exponential via Łojasiewicz inequality.

*Proof sketch:* Compact domain, monotone energy decrease, Łojasiewicz–Simon for analytic functions on compact semi-algebraic sets.

**Theorem 6 (Axiom Consistency).** *[T20]* The sigmoid closure satisfies A1' (conditional extensivity), A2 (monotonicity), A3 (contraction for $a_{\rm cl} < 4$), A4 (continuity). A1 (unconditional extensivity) and A3 are jointly unsatisfiable.

*Proof:* Direct computation; the incompatibility follows from $\sigma^{-1}(0.9)/z > 4$.

**Theorem 7 (Sharp-Interface Γ-Convergence).** *[T11]* As $\varepsilon = \alpha/\beta \to 0$, $\mathcal{E}_{\rm bd}$ Γ-converges to a perimeter functional with self-referential surface tension correction.

*Proof sketch:* Leading term is standard Modica–Mortola; correction terms from $\mathcal{E}_{\rm cl}$ and $\mathcal{E}_{\rm sep}$ are lower-order perturbations with explicit surface tension modification $\sigma_{\rm eff} = \sigma_{\rm AC} + \delta\sigma(\lambda_{\rm cl}, \lambda_{\rm sep})$.

**Theorem 8 (Resolvent Co-Belonging).** *[C-Axioms + discrimination]* The resolvent $C_t = (I - \alpha W_{\rm sym})^{-1}$ satisfies axioms C1–C4 and achieves $3+$ orders of magnitude discrimination between within-formation and cross-boundary site pairs.

*Proof:* Neumann series monotonicity for C3''; explicit numerical witnesses for discrimination. *(Note the C3'' gap — state it honestly as a remark.)*

**Figure 2:** Phase transition diagram: $\beta/\alpha$ vs. $\lambda_2$ showing the transition boundary $\beta/\alpha = 4\lambda_2/|W''(c)|$ for several values of $c$.

**Figure 3:** Energy landscape schematic showing Allen–Cahn basin vs. SCC basin (deeper due to closure term).

### 4. Novel Mathematical Objects (3–4 pages)

**4.1. The Self-Referential Operator Triad**
- Cl, D, C form a self-consistent system: each depends on the field $u$, and the energy constructed from them determines $u$ at equilibrium.
- Unlike generic nonlinear PDEs where the solution appears in the equation, here *three independent modes* of self-dependence operate simultaneously through structurally distinct channels.
- The definition/computation graph distinction (CN3) is essential: no circular definition, only circular computation.

**4.2. Self-Referential Optimal Transport**
- Cost $c(x,y) = d_{\rm graph}(x,y)^2/2\sigma^2 + \gamma\|\phi_t(x) - \phi_s(y)\|^2$ where the fingerprint $\phi(x) = (u(x), {\rm Cl}(u)(x), D(x;1-u), C(x,x))$ depends on the field being transported.
- This creates a fixed-point equation in transport-plan space: the optimal plan depends on the fields, which are updated using the plan.
- **Existence:** Proved via Brouwer (continuous self-map on compact convex set $\Sigma_m \times \Sigma_m$). Continuity from: fingerprint continuous in $u$; entropic OT unique and $C^\infty$ in cost; energy minimizer continuous in $M$ at non-degenerate points.
- **Uniqueness:** Not in general. Multiple fixed points correspond to different identity assignments — a feature, not a bug. Local uniqueness condition: $\lambda_{\rm tr} \cdot \gamma \cdot \|\partial\phi/\partial u\| / (\varepsilon \cdot \lambda_{\min}(H_{\rm static})) < 1$.
- **Three regimes:** Weak transport (unique, safe), moderate (multiple fixed points), strong (may diverge — excluded by parameter constraint).
- *No precedent in OT literature.* The closest relative is mean-field game theory (where the cost depends on the distribution of agents), but even there the cost does not depend on the *specific values* being transported.

**4.3. Resolvent Co-Belonging on Cohesion-Weighted Graphs**
- $C_t = (I - \alpha W_{\rm sym})^{-1}$ where the weight matrix itself depends on the cohesion field through $\sqrt{u(x)} N(x,y) \sqrt{u(y)}$.
- The Neumann series $\sum \alpha^k W_{\rm sym}^k$ captures contributions from paths of all lengths, weighted by the cohesion field along the path.
- Distinct from spectral clustering: (a) weights are field-dependent, creating a self-referential graph; (b) the resolvent preserves the full path structure, not just the top eigenvectors; (c) enters the theory diagnostically, not variationally.
- The Cesàro alternative (random walk averaging) was proved to degenerate to the stationary distribution, destroying structural information. This negative result is itself of interest for graph-based learning.

**4.4. Volume-Constrained Ginzburg–Landau with Self-Referential Corrections**
- The energy on $\Sigma_m$ is a perturbation of the classical volume-constrained Ginzburg–Landau by two self-referential terms.
- The perturbation is structurally non-trivial: the closure term adds a positive-definite Hessian contribution (Theorem 2), the separation term has a self-referential Hessian (field appears in the operator being differentiated).
- This is *not* a simple nonlinear potential replacement — the operators have independent parameters and enter through structurally distinct channels.

**Figure 4:** Resolvent discrimination: heatmap of $C_t(x,y)$ for a formation-structured field, showing high within-formation and low cross-boundary values.

**Figure 5:** Self-referential transport schematic: the fingerprint loop $u \to \phi \to c \to M^* \to u'$.

### 5. Computational Validation (2–3 pages)

**5.1. Implementation**
- Semi-implicit projected gradient descent with Barzilai-Borwein step sizes and multi-start initialization.
- Gradient implementation verified against finite differences to tolerance $10^{-9}$.
- 89 tests covering axiom satisfaction, energy decomposition, gradient accuracy, and diagnostic properties.

**5.2. Experimental Results**
- **Formation existence:** 100% success rate across grid sizes 5×5 to 20×20 with multi-start optimization.
- **Energy ablation:** $\mathcal{E}_{\rm bd}$ is the primary formation driver; $\mathcal{E}_{\rm cl}$ and $\mathcal{E}_{\rm sep}$ are refinements that sharpen formation quality. BD-only already produces excellent formations; SEP-only can form but is weaker.
- **Diagnostic vector:** Formations achieve Bind $\approx 0.85$, Sep (u-weighted) $\approx 0.90$, Inside $\approx 1.0$.
- **Phase transition:** No sharp transition under full SCC energy (T8-Core covers $\mathcal{E}_{\rm bd}$ only); gradual crossover observed. This is an honest limitation.

**5.3. Issues Found (Honesty)**
- Sep_new (C_t-weighted) is broken as a global diagnostic ($\approx 0.5$ regardless); must restrict to formation support.
- Bind caps at $\sim 0.85$ due to inherent boundary closure residual.
- Separation energy is marginal — refines but does not substantially improve beyond Allen–Cahn in current experiments.

**Figure 6:** Example formations on 10×10 and 20×20 grids showing cohesion field, diagnostic vector components, and energy decomposition.

**Figure 7:** Energy ablation: formation quality metrics under BD-only, CL+BD, SEP+BD, and full energy.

### 6. Open Problems (2 pages)

**Presented in order of mathematical importance:**

1. **Self-referential OT existence and uniqueness.** The Brouwer argument gives existence of a fixed point in transport-plan space; uniqueness and convergence of the alternating minimization are open beyond the weak-transport regime.

2. **Renormalization group relevance of $\mathcal{E}_{\rm sep}$.** Does the separation energy remain relevant under spatial coarse-graining? If it has a nontrivial RG fixed point, separation is a "relevant" perturbation of Allen–Cahn — significant for scale behavior.

3. **Multi-formation theory.** The contraction regime ($a_{\rm cl} < 4$) limits to single formations. Extending to $K$ coupled fields, leaving the contraction regime, or spectral $C_t$ decomposition are all open.

4. **Sharp-interface dynamics.** The Γ-convergence (Theorem 7) characterizes the limit functional; the dynamics of the sharp-interface limit (modified mean curvature flow with self-referential surface tension) are unproved.

5. **Temporal persistence theorems.** Proving that gentle transport preserves formation structure (core inheritance, diagnostic vector stability) at the level of full rigor. The proof strategy via quantitative IFT exists but has three critical gaps.

6. **T8-Full gap.** Extending the phase transition from $\mathcal{E}_{\rm bd}$ to the full energy $\mathcal{E}$ via implicit function theorem.

7. **Sep_new/energy relationship.** The exact bridge ${\rm Sep}_{\rm old} = 1 - \mathcal{E}_{\rm sep}/m$ does not extend to the C_t-weighted form.

8. **Parameter regime theory.** Principled method for setting $\lambda$ ratios; Hessian normalization suggests $\lambda_{\rm sep}/\lambda_{\rm bd} \sim 10^{-5}$.

### 7. Discussion (1–2 pages)

- The framework's mathematical identity: a self-referential extension of volume-constrained Ginzburg–Landau on graphs, with three novel structural features (operator triad, self-referential transport, resolvent co-belonging).
- Relationship to existing frameworks (contrastive, not reductive): closest to Allen–Cahn (shares $\mathcal{E}_{\rm bd}$), but the self-referential terms have no analogue; resolvent co-belonging is related to but distinct from spectral clustering; self-referential OT is novel.
- The non-idempotent closure result (Theorem 2) is perhaps the most surprising: there is a *mathematical advantage* to not imposing idempotence, beyond philosophical preference.
- Honest limitations: the separation energy is experimentally marginal; the temporal theory has critical gaps; multi-formation theory is blocked.

### Appendices

- **A.** Full proofs of Theorems 1–8.
- **B.** Computational details: optimizer, parameter validation, gradient derivations.
- **C.** Proof of Sep_new covariance identity.

---

## Estimated Length: 28–35 pages

---
---

# PAPER 2: Cognitive Science Paper

## Target Venue

**Cognitive Science** or **Psychological Review**

---

## Title

**Before Objects: A Formal Theory of Pre-Objective Perceptual Cohesion**

---

## Draft Abstract

How does perception arrive at discrete objects? Standard accounts begin from objects and ask how they are recognized, tracked, or categorized. We propose that a prior question must be answered first: how does anything become a coherent *something* — a formation that holds together, distinguishes itself from its surround, and persists through time — before it is identified as any particular thing? We present Soft Cognitive Cohesion (SCC), a formal mathematical theory in which the primitive entity is a graded cohesion field, not a set of discrete objects. SCC formalizes four structural requirements for pre-objective formation: binding (self-support under relational closure), separation (structural distinction from exterior), morphological articulation (core-boundary-exterior stratification), and temporal persistence (structural inheritance under transport). These four requirements define a diagnostic vector $\mathbf{d} \in [0,1]^4$ that provides a continuous, multi-dimensional measure of formation quality — replacing the single scalar of Gestalt Prägnanz with a decomposed assessment. We show that SCC provides the first variational foundation for the Gestalt laws: closure corresponds to Prägnanz, distinction to figure-ground segregation, co-belonging to common fate, and temporal transport to perceptual identity. Crucially, the theory's operators are self-referential: the field defines what counts as "closure," "distinction," and "belonging," and is then evaluated against its own definitions — formalizing the autopoietic insight that cognitive systems maintain themselves through self-production. We derive 10 empirical predictions that distinguish SCC from Predictive Processing, Global Workspace Theory, Integrated Information Theory, and Bayesian accounts, several of which are testable with current psychophysical and neuroimaging methods. Computational experiments demonstrate formation existence and validate the diagnostic framework on graph-based domains.

**(256 words)**

---

## Section Structure

### 1. Introduction: The Problem of Pre-Objective Cohesion (3–4 pages)

**1.1. What Comes Before Objects?**
- Standard cognitive science begins from objects: recognition, categorization, tracking, binding. But this starting point presupposes that the perceptual field has already been parsed into discrete entities.
- The problem SCC addresses: how does a region of the perceptual field come to hold together as a *coherent something* — before it is identified as any particular thing?
- Historical precedents: Gestalt psychology (Wertheimer, Köhler, Koffka) described this pre-objective organization phenomenologically but never formalized it mathematically. Merleau-Ponty's "pre-objective field" captures the philosophical insight. Husserl's passive synthesis names the process.

**1.2. Why Current Theories Start Too Late**
- Predictive Processing assumes discrete hypotheses being tested against sensory data — but hypotheses about *what*? Objects are already presupposed.
- Global Workspace Theory assumes discrete contents competing for access — but how do contents become discrete in the first place?
- IIT assumes a system decomposed into elements — but decomposition presupposes individuation.
- Bayesian brain assumes a generative model over an external world parsed into variables — but parsing is the question.

**1.3. The Proposal**
- SCC posits a graded cohesion field $u: X \to [0,1]$ as the primitive entity. Objects are late achievements — formations that have achieved sufficient binding, separation, articulation, and persistence.
- Preview the four-component diagnostic vector.
- Preview the self-referential operator triad as the core formal novelty.

### 2. The Formal Framework (Accessible Presentation) (5–6 pages)

**2.1. The Cohesion Field**
- Present $u_t(x) \in [0,1]$ as intensity of cohesive participation — not probability, not membership score.
- Analogy: the field is like the pre-attentive "togetherness" that allows you to see a face in a crowd before you identify whose face it is.

**2.2. The Four Structural Requirements**

**Binding (Closure):**
- A formation must be self-supporting: the relational structure at each site must be consistent with the cohesion at that site.
- Formalization: ${\rm Cl}_t(u) \approx u$ — the field is approximately a fixed point of its own relational completion.
- Gestalt connection: this is the formal analogue of the law of closure — incomplete figures are completed by the perceptual system. SCC says: completion is contractive (converges gradually), not projective (all-or-nothing).

**Separation (Distinction):**
- A formation must distinguish itself from its surround.
- Formalization: $D_t(x; 1-u)$ measures the asymmetry of relational support from interior vs. exterior.
- Gestalt connection: figure-ground segregation. But SCC's distinction is *self-referential*: the field defines what counts as "interior" and "exterior," then measures its own distinction against that definition.

**Morphological Articulation (Inside-Structure):**
- A formation must have internal structure: core, boundary, exterior strata.
- Formalization: $\mathcal{Q}_{\rm morph} = \ell_{\max} \cdot {\rm Artic}$ from persistence diagrams (topological data analysis applied to the superlevel-set filtration).
- Gestalt connection: the law of good form — formations have a structured morphology, not a featureless blob.

**Temporal Persistence:**
- A formation must be the same formation through time: its structurally significant core must be inherited under transport.
- Formalization: $M_{t \to s}$ maps cohesive roles from time $t$ to time $s$; the core is preserved.
- Gestalt connection: common fate — elements that move together belong together. SCC formalizes "moving together" as structural inheritance of the cohesive core.

**2.3. The Diagnostic Vector**
- $\mathbf{d} = ({\rm Bind}, {\rm Sep}, {\rm Inside}, {\rm Persist}) \in [0,1]^4$.
- Replaces the single scalar of Gestalt Prägnanz with a decomposed, continuous measure.
- A formation with $\mathbf{d} = (0.95, 0.3, 0.8, 0.7)$: well-bound but poorly separated — diagnostic information lost in a single score.

**2.4. Self-Referential Structure**
- The operator triad: self-completion (Cl), self-contrast (D), self-integration (C).
- The field defines the operators → the operators define the energy → the energy determines the field.
- This formalizes autopoiesis: the system maintains itself through its own self-evaluation.
- Accessible analogy: a social group that defines its own membership criteria, evaluates itself against those criteria, and adjusts — the criteria and the group co-evolve.

**Figure 1:** The four structural requirements illustrated with visual examples (Kanizsa triangle for closure, figure-ground vase for distinction, concentric shapes for morphology, apparent motion for persistence).

**Figure 2:** The diagnostic vector as a radar/spider plot for different visual stimuli, showing how different formations satisfy different requirements to different degrees.

### 3. The Gestalt Connection (3–4 pages)

**3.1. Mapping Gestalt Laws to SCC Operators**

| Gestalt Principle | SCC Counterpart | Status |
|---|---|---|
| Closure | ${\rm Cl}_t$ (closure operator) | Direct formalization |
| Proximity | $N_t$ (adjacency kernel) | Direct formalization |
| Similarity / Common fate | $C_t$ (co-belonging) | Formal extension (non-local) |
| Figure-ground | $D_t$ (distinction operator) | Direct formalization |
| Prägnanz (good form) | Metastable energy minima | Proved (Theorems 3, 4) |

**3.2. Three Gestalt Puzzles SCC Resolves**

**(a) Why is Prägnanz metastable, not optimal?**
Perception sometimes settles into suboptimal organizations (the Necker cube has two stable percepts, neither globally optimal). SCC explains: formations are metastable local minima of the energy with enhanced stability barriers (T7). Prägnanz is *local* goodness, not *global* optimality. This is a theorem, not an assumption.

**(b) Why does perceptual history matter?**
Adaptation and priming affect perceptual organization — the same stimulus is organized differently depending on what preceded it. SCC explains: non-idempotent closure means the stabilization trajectory carries information. Different starting points (different adaptation histories) converge to different metastable formations in the energy landscape.

**(c) Why is figure-ground segregation asymmetric?**
The figure "owns" its boundary in a way the ground does not (Rubin, 1921). SCC explains: the distinction operator $D_t(x; 1-u)$ is structurally asymmetric — it measures interior support relative to exterior, creating an inherent inside/outside asymmetry. The formation's boundary belongs to the formation, not to the surround.

**3.3. What SCC Adds Beyond Gestalt Description**
- Gestalt laws are qualitative; SCC provides quantitative, continuous measures.
- Gestalt laws are independent heuristics; SCC unifies them as consequences of a single variational principle.
- Gestalt has no formal account of temporal persistence; SCC's transport kernel formalizes common fate and perceptual identity.

### 4. Distinguishing SCC from Contemporary Theories (4–5 pages)

**4.1. SCC vs. Predictive Processing (PP)**

| Dimension | SCC | PP |
|---|---|---|
| Ontological level | Pre-objective (before objects) | Post-objective (updating beliefs about objects) |
| Generative model | Internal (field predicts itself) | External (model predicts sensory data) |
| Self-reference | Structural (operator triad) | Absent at basic level |
| Direction | Bottom-up self-organization | Top-down prediction + bottom-up error |
| Core mechanism | Energy minimization on cohesion field | Free energy minimization on beliefs |

**Key distinction:** SCC is *ontological* (what structures exist before objects), PP is *epistemological* (how beliefs about objects are updated). They are complementary, not competing: SCC provides the substrate on which PP operates. The pre-objective formations that SCC describes are the raw material that PP then interprets.

**Testable difference:** PP predicts that top-down predictions drive perceptual organization; SCC predicts that basic coherence is bottom-up self-organizing from the operator triad. Measurable via EEG time-course: if SCC is correct, figure-ground segregation (Sep) should precede top-down categorical effects (P5).

**4.2. SCC vs. Global Workspace Theory (GWT)**

| Dimension | SCC | GWT |
|---|---|---|
| Starting point | Graded cohesion field | Discrete contents in specialized modules |
| Competition | Energy landscape (metastable basins) | Contents compete for workspace access |
| Consciousness | Not addressed (pre-objective level) | Workspace access = consciousness |
| Scope | Formation emergence | Information broadcasting |

**Key distinction:** GWT assumes contents are already discrete — they compete for global broadcasting. SCC asks: how do contents become discrete in the first place? SCC operates at a level prior to GWT's starting point.

**Testable difference:** GWT predicts all-or-nothing access (contents are either in the workspace or not); SCC predicts graded formation quality (the diagnostic vector) with continuous transitions. Non-conscious stimuli should still have measurable diagnostic vector components (partial binding, partial separation) — they are formations that haven't fully stabilized, not absent representations.

**4.3. SCC vs. Integrated Information Theory (IIT)**

| Dimension | SCC | IIT |
|---|---|---|
| Primitive | Cohesion field (continuous) | Causal relations among discrete elements |
| Integration | Co-belonging $C_t$ (field-dependent) | $\Phi$ (over system partition) |
| Level | Pre-objective | System-level |
| Claims about consciousness | None | $\Phi > 0$ = consciousness |

**Key distinction:** IIT assumes a system decomposed into elements and asks how much their interactions exceed the sum of parts. SCC asks how elements come to cohere into a system in the first place. IIT's $\Phi$ presupposes individuation; SCC's diagnostic vector describes individuation in progress.

**Testable difference:** IIT predicts $\Phi$ as a single integration measure; SCC predicts four independent dimensions. Formations can be highly integrated ($C_t$ values high) but poorly distinguished (low Sep) — a state IIT cannot represent with a single scalar.

**4.4. SCC vs. Bayesian Brain**

| Dimension | SCC | Bayesian |
|---|---|---|
| Prediction error | Self-referential ($u$ vs. ${\rm Cl}(u)$) | External (prediction vs. sensation) |
| Priors | Emergent from energy landscape | Explicit in generative model |
| Formation | Energy minimization discovers structure | Inference assumes structure |

**Key distinction:** Bayesian approaches presuppose a generative model with variables corresponding to objects or features. SCC asks how the perceptual system arrives at the variables in the first place. SCC is *pre-Bayesian*: it operates at the level where the categories for Bayesian inference are being formed.

**Testable difference:** The Bayesian brain predicts contractive updating toward a single posterior (given fixed priors); SCC predicts multiple metastable formations with path-dependent selection (P3, P4). For ambiguous stimuli, Bayesian models predict probability distributions over interpretations; SCC predicts discrete metastable states with enhanced dwell times.

### 5. Empirical Predictions (3–4 pages)

**5.1. Cognitive/Perceptual Predictions (Testable Now)**

**P1. Gestalt closure is contractive, not projective.**
- *Protocol:* Ambiguous displays (Kanizsa triangles, amodal completion); repeated brief exposure.
- *SCC predicts:* Progressive convergence of percepts (contractive stabilization).
- *Competing prediction:* Bayesian models predict probabilistic updating; equilibrium models predict all-or-nothing completion.
- *Method:* Priming paradigms + EEG steady-state responses.
- *Testability:* **HIGH** — standard psychophysics + EEG.

**P2. Perceptual organization has four independent dimensions.**
- *Protocol:* Factorial manipulation of stimulus properties: internal coherence (Bind), figure-ground contrast (Sep), shape complexity (Inside), temporal continuity (Persist).
- *SCC predicts:* Four factors are independently manipulable with no interactions (or specific, predictable interactions).
- *Competing prediction:* Single-scalar models (Prägnanz, posterior probability) predict all dimensions are correlated.
- *Method:* Psychophysical thresholds + factor analysis.
- *Testability:* **HIGH** — standard psychophysics.

**P3. Metastable percepts have longer dwell times than equilibrium models predict.**
- *Protocol:* Binocular rivalry; measure dwell times.
- *SCC predicts:* Systematically longer dwell times than Allen–Cahn (standard energy barrier model) due to self-referential closure enhancement (T7).
- *Method:* Binocular rivalry + computational model comparison.
- *Testability:* **MEDIUM** — requires quantitative model fitting.

**P4. Perceptual history affects current organization (path dependence).**
- *Protocol:* Same ambiguous stimulus after different adaptation sequences.
- *SCC predicts:* Adaptation trajectory (not just final adapted state) influences percept.
- *Competing prediction:* Equilibrium models predict only current input matters.
- *Method:* Bistable figure paradigms with controlled adaptation histories.
- *Testability:* **HIGH** — standard psychophysics; some existing data supports this.

**P5. Self-referential distinction precedes object recognition.**
- *Protocol:* RSVP; measure time-course of figure-ground segregation vs. object identification.
- *SCC predicts:* Sep (measured via N1 EEG component) precedes recognition (N2/P300).
- *Competing prediction:* PP predicts top-down prediction precedes segregation.
- *Method:* EEG/MEG with time-course analysis.
- *Testability:* **HIGH** — standard ERP paradigm.

**5.2. Biological/Neuroscience Predictions**

**P6. Morphogenetic boundaries follow Bind → Sep → Inside developmental order.**
- *Domain:* Developmental biology (e.g., zebrafish somitogenesis).
- *Method:* Spatial transcriptomics at tissue boundaries across developmental stages.
- *Testability:* **MEDIUM** — requires spatial transcriptomics + SCC model fitting.

**P7. Self-referential binding prolongs biomolecular condensate lifetimes.**
- *Domain:* Cellular biology (liquid-liquid phase separation).
- *Method:* FRAP experiments comparing self-referential vs. non-self-referential condensate components.
- *Testability:* **MEDIUM** — requires specific experimental design.

**P8. Neural assemblies show formation dynamics (Bind, Sep, Inside, Persist), not just clustering.**
- *Domain:* Systems neuroscience.
- *SCC predicts:* "Proto-assemblies" (high Bind, low Sep) exist before stimulus onset and are recruited by stimuli.
- *Method:* Multi-electrode recordings + SCC diagnostic analysis.
- *Testability:* **MEDIUM-HIGH** — re-analysis of existing datasets possible.

**5.3. Materials/Physics Predictions (Long-Term)**

**P9. Modified coarsening exponents in self-referential phase separation.**
- $R(t) \sim t^{1/3 + \delta}$ where $\delta$ depends on self-referential coupling strength.
- *Testability:* **LOW** — requires STEM time-series of specialized materials.

**P10. Self-referential surface tension in sharp-interface limit.**
- $\sigma_{\rm eff} = \sigma_{\rm AC} + \delta\sigma(\lambda_{\rm cl}, \lambda_{\rm sep})$.
- *Testability:* **LOW** — requires precise surface tension measurement in self-referential systems.

**Table 1:** Summary of all 10 predictions with testability rating, required methods, and which theories each distinguishes from.

### 6. Computational Proof-of-Concept (2–3 pages)

**6.1. What the Experiments Show**
- Formations emerge reliably from energy minimization on graph-based domains (100% success rate).
- The diagnostic vector provides meaningful, differentiated assessment: Bind $\approx 0.85$, Sep $\approx 0.90$, Inside $\approx 1.0$.
- Different energy components contribute differently to formation quality, confirming the four-term independence claim.

**6.2. What the Experiments Don't Show**
- These are graph-based simulations, not perceptual experiments. They demonstrate mathematical consistency, not psychological validity.
- The temporal component (Persist) is not yet computationally validated.
- The parameter regime is hand-tuned, not derived from perceptual data.

**Figure 3:** Example formations with diagnostic vector components, shown as heat maps on a grid graph with radar-plot diagnostic summaries.

**Figure 4:** Energy ablation results showing independent contributions of each energy term.

### 7. Philosophical Implications (2–3 pages)

**7.1. Pre-Objective Perception**
- SCC formalizes what phenomenologists have long described: a level of perceptual organization that is prior to object identification.
- Merleau-Ponty's "pre-objective field" = the cohesion field $u_t$.
- Husserl's passive synthesis = the axiomatic groups (association = adjacency + co-belonging; contrast = distinction; temporal = transport).
- The theory gives mathematical substance to "somethingness before thingness."

**7.2. Autopoiesis Formalized**
- The self-referential operator triad formalizes Maturana & Varela's autopoiesis: the system maintains itself through self-production.
- The field defines the operators → the operators evaluate the field → the evaluation determines the field. This is operational closure.
- SCC positions this not as metaphor but as mathematical structure with proved properties.

**7.3. Soft Ontology**
- SCC proposes a "soft ontology" in which existence is graded, not binary.
- A formation exists *to a degree*: the diagnostic vector quantifies how strongly each structural requirement is satisfied.
- Objects are not discovered in a pre-given world; they are *achieved* by cohesive formations that stabilize sufficiently.

**7.4. Honest Philosophical Limitations**
- **The discrete substrate problem:** SCC presupposes individuated sites $X_t$ while claiming relational priority. The theory begins with discrete points but philosophically claims that objects are derivative. This tension is acknowledged but unresolved.
- **Volume constraint as smuggled objecthood:** The fixed cohesive budget $m$ presupposes knowledge of "how much formation" to expect — arguably smuggling object-level information into the pre-objective level.
- **No consciousness claims:** SCC describes pre-objective structure formation, not consciousness. It is a necessary substrate theory, not a sufficient theory of experience.

### 8. Limitations and Open Problems (1–2 pages)

**What is proved:**
- Formation existence (mathematical theorem on graphs).
- Enhanced metastability (mathematical theorem).
- Gradient flow convergence (mathematical theorem).
- Axiom consistency for all operators.
- Computational demonstration of formation emergence.

**What is conjectured but unproved:**
- Temporal persistence theorems (proof strategy with gaps).
- Self-referential transport existence (Brouwer sketch only).
- Multi-formation theory (architecturally blocked).
- Sep_new / energy relationship.

**What is speculative:**
- All 10 empirical predictions (derived from the theory but not yet tested).
- The phenomenological interpretations (Gestalt mapping, autopoiesis, pre-objective field).
- The claim that SCC captures something psychologically real, not just mathematically elegant.

**What is honestly weak:**
- Separation energy is experimentally marginal in current simulations.
- The temporal theory has zero fully proved results.
- The parameter regime is not derived from data.
- The theory is limited to single formations in the contraction regime.

### 9. Conclusion (1 page)

- SCC proposes that perception begins not with objects but with graded cohesive formations characterized by a four-dimensional diagnostic vector.
- The theory provides the first variational foundation for Gestalt laws and generates testable predictions distinguishing it from PP, GWT, IIT, and Bayesian accounts.
- The most immediately testable predictions (P1, P2, P4, P5) require only standard psychophysics and EEG.
- The theory's philosophical contribution — formalizing pre-objective perception — is independent of whether every mathematical detail survives empirical testing.

---

## Cross-References Between Papers

| Paper 1 (Math) | Paper 2 (CogSci) |
|---|---|
| Theorem 1 (Closure contraction) | §3.2a (Prägnanz as metastability; closure is contractive not projective) |
| Theorem 2 (Non-idempotent advantage) | §3.2b (Why perceptual history matters) |
| Theorem 3 (Phase transition) | §6.1 (Formation existence proof-of-concept) |
| Theorem 4 (Enhanced metastability) | §4.1, P3 (Longer dwell times than equilibrium models) |
| Theorem 5 (Gradient flow convergence) | §6.1 (Mathematical consistency) |
| Theorem 7 (Γ-convergence) | P10 (Modified surface tension — long-term prediction) |
| §4.2 (Self-referential OT) | §2.2 Temporal Persistence, P8 (Neural assemblies) |
| §4.3 (Resolvent co-belonging) | §2.2 Separation, §3.1 (Common fate formalization) |
| §5.3 (Experimental issues) | §8 (Honest limitations) |
| §6 (Open problems) | §8 (What is conjectured vs. proved) |

---

## Figure Summary

### Paper 1 (Mathematics)
1. Self-referential energy architecture schematic
2. Phase transition diagram ($\beta/\alpha$ vs. $\lambda_2$)
3. Energy landscape: Allen–Cahn vs. SCC basin depth
4. Resolvent co-belonging heatmap
5. Self-referential transport fingerprint loop
6. Example formations on grid graphs with diagnostic vectors
7. Energy ablation results

### Paper 2 (Cognitive Science)
1. Four structural requirements with visual examples (Kanizsa, vase, etc.)
2. Diagnostic vector as radar plot for different stimuli
3. Computational formations with diagnostic summaries
4. Energy ablation showing independent term contributions
5. (Optional) Timeline: figure-ground segregation preceding object recognition (schematic for P5)
6. (Optional) Gestalt law → SCC operator mapping diagram

---

## Honest Overall Assessment

### What These Papers Can Legitimately Claim

**Paper 1:**
- A mathematically well-defined variational framework with genuine theorems (12+ rigorously proved).
- Three novel mathematical objects with no direct precedent.
- A computational implementation that validates the framework.

**Paper 2:**
- A formal theory that provides the first variational foundation for Gestalt organizing principles.
- 10 empirical predictions, at least 4 of which are testable with current methods.
- A clear positioning relative to PP, GWT, IIT, and Bayesian brain.

### What These Papers Cannot Legitimately Claim

- That the theory has been empirically validated (it has not — only computationally demonstrated).
- That the temporal theory is complete (the persistence component has zero fully proved results).
- That multi-formation perception is addressed (it is architecturally blocked).
- That the separation energy is empirically important (it is experimentally marginal so far).
- That the phenomenological interpretations are more than suggestive analogies.

### Risk Assessment

**Paper 1 risk:** Reviewers may see the Allen–Cahn substrate and dismiss the self-referential extensions as minor. The defense: Theorem 2 (non-idempotent advantage) and the self-referential OT are genuinely without precedent.

**Paper 2 risk:** Reviewers may demand empirical data. The defense: the paper presents a theoretical framework with testable predictions, not an empirical study. Comparable papers (IIT's original formulation, FEP's initial presentation) were published on theoretical grounds.

**Shared risk:** The separation energy's experimental marginality weakens the claim that all four terms are necessary. The defense: conceptual independence is the claim, not equal quantitative importance.
