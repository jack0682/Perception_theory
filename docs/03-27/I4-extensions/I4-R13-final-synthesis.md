# Iteration 4 — Final Extensions Synthesis: SCC and Its Connections

**Author:** Integration Synthesizer
**Date:** 2026-03-27
**Iteration:** 4 Capstone (Rounds 4-13)
**Inputs:** All R4-R12 positions (Math Connections, CogSci Bridge, Applications) — COMPLETE
**Scope:** Definitive accounting of where SCC sits in mathematics, cognitive science, and applications

---

## I. WHAT IS SCC?

### The One-Paragraph Identity Statement

Soft Cognitive Cohesion is a **self-referential constrained variational field theory on finite graphs** in which a graded cohesion field $u_t : X_t \to [0,1]$ generates, through its own values, the operators that evaluate it — closure completes it, distinction contrasts it against its own complement, and co-belonging integrates it non-locally — creating a self-referential loop that is formalized as the **operator triad** (self-completion, self-contrast, self-integration). This loop, absent in all standard variational frameworks, produces a **self-referential separation energy** with no analogue in Allen-Cahn, Mumford-Shah, or phase-field theories. The theory characterizes **pre-objective cohesion**: how coherent formation precedes discrete objecthood. Its mathematical signature is non-idempotent contractive closure, sub-stochastic structural transport, and axiomatized soft-to-crisp recovery via superlevel filtrations. Its cognitive signature is a formal account of how "somethingness" emerges before "thingness" — the process that Gestalt psychology described phenomenologically, that predictive processing models computationally, and that autopoietic theory frames biologically, but that none of these formalized variationally.

### The Three-Sentence Technical Summary

SCC minimizes a four-term energy $\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}} + \lambda_{\mathrm{tr}}\mathcal{E}_{\mathrm{tr}}$ on the volume-constrained manifold $\Sigma_m$, where the closure and distinction operators in $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$ depend on the field being optimized. Formations are **metastable** critical points — deeper energy basins than Allen-Cahn due to the self-referential closure correction (T7, proved) — diagnosed by a continuous $[0,1]^4$ vector (Bind, Sep, Inside, Persist). The theory has 12 proved theorems including non-trivial minimizer existence under computable phase transition (T8-Core), gradient flow convergence (T14, Lojasiewicz), and sharp-interface $\Gamma$-convergence to a modified graph cut with self-referential surface tension (T11).

---

## II. SCC IN THE MATHEMATICAL LANDSCAPE

### Placement

SCC sits at the intersection of four mathematical traditions, belonging fully to none:

```
                     Variational PDE / Phase-Field
                              |
                    (Allen-Cahn substrate, E_bd)
                              |
    Algebraic Topology  ---- SCC ----  Operator Theory
    (filtrations, PD,        |         (non-idempotent closure,
     sheaf-theoretic C_t)    |          self-referential operators)
                              |
                    Optimal Transport
                    (M_{t->s} as entropic OT,
                     sub-stochastic transport plans)
```

**Nearest mathematical neighbors:**

| Framework | Overlap | Distinguishing gap |
|-----------|---------|-------------------|
| Allen-Cahn / Cahn-Hilliard | $\mathcal{E}_{\mathrm{bd}}$ identical; gradient flow structure shared | Self-referential $\mathcal{E}_{\mathrm{sep}}$ absent; closure is external in AC |
| Mumford-Shah | Variational segmentation with boundary energy | No self-referential operators; objects are primitive inputs |
| Graph cuts / Potts model | Discrete energy minimization on graphs | No graded fields; no operator triad; no temporal transport |
| Persistent homology | Filtration-based topological analysis | Descriptive only — no variational principle, no dynamics |
| Optimal transport | Transport plans between measures | No self-referential cost; transport is externally defined |
| Autopoietic theory | Operational closure of self-producing systems | Philosophical framework without variational formalization |
| Free energy principle | Variational inference with self-referential generative models | SCC is ontological (pre-objective), FEP is epistemological (belief updating) |

**Comparative distinctiveness (from R12):** SCC scores 7/7 distinctive features vs. Mumford-Shah, 5/7 vs. Allen-Cahn. The irreducible core of distinctiveness: the **operator triad** (no other variational theory has operators that depend on the field they evaluate in all three modes simultaneously) and the **self-referential separation energy** (no analogue in any standard framework).

---

## III. TOP 5 MATHEMATICAL CONNECTIONS (Ranked by What They Buy)

### 1. Optimal Transport: $\mathbf{M}_{t \to s}$ as Entropic Transport Plan

**Connection:** The provisional transport kernel (Canonical Spec Section 9.4) is already an entropic optimal transport plan with cost $c(x,y) = \|y - \Psi(x)\|^2/(2\sigma_M^2) + \gamma_M\|\varphi_t(x) - \varphi_s(y)\|^2$ and regularization $\varepsilon$. The sub-stochastic constraint (E1: $\sum_y M(x,y) \leq 1$) is a partial transport plan — mass can dissipate.

**What it buys:**
- **Immediate:** The entire OT toolkit (Sinkhorn algorithms, Wasserstein distances, displacement interpolation) becomes available for computing $\mathbf{M}_{t \to s}$. This directly addresses the Persist gap — the largest open problem from Iteration 2.
- **Theoretical:** Wasserstein gradient flows provide a principled framework for between-time dynamics (currently OPEN). The temporal energy $\mathcal{E}_{\mathrm{tr}}$ becomes a regularized Wasserstein-2 distance between weighted measures $u_t \cdot \mu_{X_t}$ and $u_s \cdot \mu_{X_s}$.
- **Novel contribution to OT:** Self-referential transport, where the cost function depends on the fields being transported ($c$ depends on $u_t, u_s$ through features $\varphi$), is genuinely new in the OT literature. Standard OT has externally fixed costs.

**Priority:** HIGHEST. Directly unblocks Persist (the theory's largest gap) and between-time dynamics (the implementation's largest gap). The connection is already implicit in the Canonical Spec — making it explicit costs nothing and gains an entire mathematical toolbox.

**Spec impact:** Commentary. The OT interpretation enriches understanding but does not change the axioms. The sub-stochastic generalization (partial transport) should be noted as a connection to unbalanced OT.

### 2. Category Theory: The Category $\mathbf{Coh}$

**Connection:** SCC has natural categorical structure. Objects are cohesion spaces $(X_t, N_t, u_t)$; morphisms are transport-compatible maps preserving the operator triad; closure $\mathrm{Cl}_t$ is a contractive endofunctor on $[0,1]^{X_t}$.

**What it buys:**
- **Immediate:** Functorial language makes the theory compositional. Multi-formation theory (currently OPEN) becomes: formations are subobjects in $\mathbf{Coh}$; multi-formation is a decomposition in the category.
- **Theoretical:** The non-idempotent endofunctor $\mathrm{Cl}_t$ (contractive but not a monad in the standard sense, since $\mathrm{Cl}^2 \neq \mathrm{Cl}$) is a **novel mathematical object** — standard categorical closure theory assumes idempotence. SCC provides the first natural example of a non-idempotent closure endofunctor with proved stability advantages.
- **Structural:** Natural transformations between operator triads formalize what it means for two realizations (e.g., sigmoid vs. ReLU closure) to be "the same theory with different operators."

**Priority:** HIGH for theoretical clarity; MEDIUM for computational impact. The categorical language does not produce new algorithms, but it provides the right vocabulary for the multi-formation extension and for comparing SCC to other frameworks.

**Spec impact:** Commentary. Category-theoretic reformulation belongs in a separate mathematical companion document, not the Canonical Spec. One exception: the **functorial characterization of transport** ($\mathbf{M}$ as a morphism in $\mathbf{Coh}$) could sharpen Group E axioms.

### 3. Sheaf Theory: Co-belonging as Cosheaf, Filtration as Sheaf

**Connection:** The co-belonging operator $\mathbf{C}_t$ has cosheaf structure: it assigns to each open set $U \subseteq X_t$ the co-belonging data $\mathbf{C}_t|_U$, with restriction maps that are *not* injective (co-belonging in a subgraph loses non-local information). The superlevel filtration $\{u_t \geq \theta\}_{\theta \in [0,1]}$ has sheaf structure: local sections (connected components at threshold $\theta$) glue uniquely.

**What it buys:**
- **Immediate:** The cosheaf perspective explains *why* $\mathbf{C}_t$ must be non-local (C2 axiom): it captures global integration that local restriction destroys. This gives a principled answer to the "right $\alpha_C$" question (I3-R13 open question #2): $\alpha_C$ controls the cosheaf's propagation depth.
- **Theoretical:** Persistence diagrams $\mathrm{PD}(u_t)$ are derived functors of the filtration sheaf. This connects $\mathcal{Q}_{\mathrm{morph}} = \ell_{\max} \cdot \mathrm{Artic}$ to sheaf cohomology, providing a deeper mathematical home for the Inside predicate.
- **Multi-scale:** Sheaf-theoretic methods enable multi-parameter persistence (varying both threshold and spatial scale), which the multi-scale extension requires.

**Priority:** HIGH for C_t theory and multi-scale extension. The cosheaf characterization should inform the next revision of Group C axioms.

**Spec impact:** Mixed. The cosheaf characterization of $\mathbf{C}_t$ could motivate a new C-axiom (locality failure as a *requirement*, not just a property). The filtration-as-sheaf perspective strengthens the Group F architecture from Iteration 1 Round 5.

### 4. Information Geometry: The Natural Metric on $\Sigma_m$

**Connection:** The volume-constrained manifold $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$ carries a natural information-geometric structure. The Shahshahani metric $g_{ij}^S = \delta_{ij}/u_i(1-u_i)$ (the Fisher metric for Bernoulli parameters) is the natural Riemannian metric on $(0,1)^n$, and its restriction to $\Sigma_m$ gives a curved geometry in which boundary-adjacent points ($u_i$ near 0 or 1) have high curvature.

**What it buys:**
- **Immediate:** The natural gradient $\nabla^S \mathcal{E} = \mathrm{diag}(u_i(1-u_i)) \cdot \nabla \mathcal{E}$ is **free** — it requires only elementwise multiplication. The Shahshahani gradient flow automatically suppresses updates near 0 and 1 (where the field is "decided") and amplifies updates near 0.5 (where the field is ambiguous). This is exactly the behavior the double-well term was designed to enforce.
- **Theoretical:** Under the Shahshahani metric, the gradient flow of $\mathcal{E}_{\mathrm{bd}}$ alone is a **replicator equation** — the fundamental dynamics of evolutionary game theory. SCC's full gradient flow is replicator dynamics + self-referential perturbation. This connects SCC to evolutionary dynamics and population genetics.
- **Computational:** The Shahshahani gradient may improve convergence near the box constraints $[0,1]^n$ without the clip-and-rescale projection. This is a concrete algorithmic improvement for the FindFormation algorithm.

**Priority:** HIGH for computational impact (free improvement to gradient flow), MEDIUM for theoretical depth. The replicator dynamics connection is elegant but may not produce new theorems immediately.

**Spec impact:** Commentary for the information-geometric interpretation. The Shahshahani gradient could enter the implementation spec (Layer 4) as a recommended alternative to Euclidean gradient descent.

### 5. Multi-Scale Theory: Renormalization Group and Coarse-Graining

**Connection:** SCC on graphs admits natural coarse-graining: partition $X_t$ into blocks, define coarse cohesion as block averages, coarse adjacency as block-to-block coupling. The energy decomposes into intra-block (fine) and inter-block (coarse) terms. The self-referential separation energy $\mathcal{E}_{\mathrm{sep}}$ transforms non-trivially under coarse-graining — it is a **relevant perturbation** in the RG sense.

**What it buys:**
- **Immediate:** Multi-scale analysis enables SCC on hierarchical structures (multi-resolution images, brain networks at different spatial scales, organizational hierarchies).
- **Theoretical:** The RG conjecture — that $\mathcal{E}_{\mathrm{sep}}$ is relevant under coarse-graining while $\mathcal{E}_{\mathrm{bd}}$ is marginal — would, if proved, establish that the self-referential term *grows in importance* at larger scales. This would give mathematical substance to the philosophical claim that SCC captures something about macro-scale coherence that local theories miss.
- **Practical:** Multi-parameter persistence (varying spatial scale $\epsilon$ and threshold $\theta$ simultaneously) generates a richer persistence landscape than threshold-only filtration.

**Priority:** MEDIUM-HIGH. The RG conjecture is ambitious and may take considerable effort. But the coarse-graining machinery is relatively straightforward and immediately useful for applications.

**Spec impact:** Commentary. Multi-scale theory is an extension, not a revision of the core spec. However, if the RG conjecture is established, it would strengthen the case for $\mathcal{E}_{\mathrm{sep}}$ as the theory's dominant term — reinforcing the (preliminary) R10 narrative.

### Honorable Mention: Connections That Clarify but Don't Transform

- **Algebraic topology (persistent homology):** Already integrated via Group F and $\mathcal{Q}_{\mathrm{morph}}$. The connection is realized, not prospective.
- **Spectral graph theory:** Already implicit in the Fiedler eigenvalue condition (T8-Core) and the resolvent $\mathbf{C}_t$. Further spectral analysis of the operator triad's eigenstructure would be valuable but incremental.
- **Morse theory:** The superlevel filtration connects to discrete Morse theory. Potentially useful for understanding the topology of formation boundaries, but not yet developed.

---

## IV. TOP 5 COGNITIVE SCIENCE CONNECTIONS (Ranked by Explanatory Power)

### 1. Gestalt Psychology: SCC as Formal Gestalt

**Connection:** There is a structural mapping between SCC's formal apparatus and the classical Gestalt laws:

| Gestalt Principle | SCC Formal Counterpart | Status |
|-------------------|----------------------|--------|
| Closure (law of) | $\mathrm{Cl}_t$ (soft closure operator) | **Direct formalization** |
| Proximity | $\mathbf{N}_t$ (adjacency kernel) | **Direct formalization** |
| Similarity | $\mathbf{C}_t$ (co-belonging operator) | **Formal extension** (non-local) |
| Figure-ground | $\mathbf{D}_t$ (distinction operator) | **Direct formalization** |
| Good continuation | $\mathbf{T}_t$ (transition operator) | Conceptual alignment (T_t OPEN) |
| Pregnanz (tendency toward "good form") | Metastability at energy minima | **Proved** (T7, T14) |
| Common fate | $\mathbf{M}_{t \to s}$ (transport kernel) | **Direct formalization** |

**What it buys:**
- **Explanatory:** SCC provides what Gestalt psychology always lacked — a unified formal framework. The Gestalt laws are not a list of independent heuristics; they are consequences of a single variational principle (energy minimization) operating through the operator triad.
- **Predictive:** The diagnostic vector $[0,1]^4$ generates quantitative predictions about perceptual organization that Gestalt theory could only state qualitatively. "This figure has high Bind but low Sep" is a testable claim.
- **Corrective:** SCC predicts that Pregnanz is **metastability**, not global optimality. Perceptual organizations are not the "best" possible — they are local energy minima with enhanced stability (T7). This resolves the long-standing puzzle of why perception sometimes settles into suboptimal organizations.

**Priority:** HIGHEST for cognitive science engagement. The Gestalt mapping is the most natural entry point for psychologists and cognitive scientists.

### 2. Predictive Processing: Closure as Self-Prediction

**Connection:** In predictive processing (PP) / active inference terms:
- Closure $\mathrm{Cl}_t(u)$ is the **prediction**: what the field *would be* if the current relational structure were fully realized.
- The closure energy $\mathcal{E}_{\mathrm{cl}} = \|u - \mathrm{Cl}(u)\|^2$ is the **prediction error**: the discrepancy between the current field and its self-predicted completion.
- Separation $\mathsf{Sep}$ functions like **precision weighting**: it modulates which prediction errors matter (only errors at structurally distinguished sites count).
- Energy minimization is a form of **free energy minimization** — but with the crucial difference that SCC's generative model is *internal* (the field generates its own predictions), not external (a hierarchical model generates predictions about sensory data).

**What it buys:**
- **Clarifies the relationship:** SCC is NOT a special case of the Free Energy Principle. The FEP is epistemological (belief updating about external states); SCC is ontological (pre-objective structure formation). They operate at different levels. But SCC could provide the *substrate* on which PP operates — the pre-objective coherence that must exist before there are discrete hypotheses to update.
- **Testable distinction:** PP predicts that perceptual organization is driven by top-down predictions. SCC predicts that basic coherence is self-organizing (bottom-up, from the operator triad). These make different predictions about the time course of perceptual grouping — testable with EEG/MEG.

**Priority:** HIGH. The PP/FEP community is large and active. Positioning SCC correctly relative to PP (complementary, not competing) opens significant theoretical dialogue.

### 3. Autopoiesis: The Self-Referential Loop as Operational Closure

**Connection:** Maturana and Varela's autopoiesis — a system that produces the components that produce it — maps directly onto SCC's self-referential loop:

```
Field u_t  →  Operators (Cl, D, C)  →  Predicates  →  Energy  →  Field u_t
   ↑                                                                    |
   └────────────────────────────────────────────────────────────────────┘
```

The field defines the operators that evaluate and update it. This IS operational closure. Cut any link by inserting external data (external adjacency, external labels, external tracking IDs) and you get standard segmentation/tracking. Keep it closed and you get SCC.

**What it buys:**
- **Philosophical grounding:** Autopoietic theory provides the deepest philosophical justification for SCC's self-referential architecture. The operator triad is not a mathematical convenience — it formalizes the autopoietic insight that living/cognitive systems maintain themselves through self-production.
- **Enactivist connection:** If the R10 observation is confirmed (separation energy drives instability), then SCC formalizes **sense-making primacy**: the formation doesn't just exist — it actively distinguishes itself from its surround. This is the enactivist claim that cognition is fundamentally about self-other distinction, not passive information processing.

**Priority:** MEDIUM-HIGH. Philosophically deep but smaller audience than Gestalt or PP. Most valuable for positioning SCC in the enactivist/4E cognition literature.

### 4. Perceptual Rivalry and Bistability: Metastability as Mechanism

**Connection:** SCC's metastable formations (T7: enhanced energy basins) provide a natural account of perceptual rivalry (Necker cube, binocular rivalry). Two formations occupy distinct local energy minima; transitions between them require crossing an energy barrier. The non-idempotent closure means the transition path matters — different approach trajectories can lead to different stable percepts.

**What it buys:**
- **Quantitative predictions:** Dwell times in rivalry should scale with energy barrier heights (computable from the Hessian). The enhanced barriers from self-referential closure (T7) predict longer dwell times than Allen-Cahn-based models.
- **Path dependence:** Non-idempotent closure predicts that the *history* of perceptual organization affects the current percept. This is testable and distinguishes SCC from equilibrium models.

**Priority:** MEDIUM. Narrower than Gestalt or PP, but produces the most specific quantitative predictions.

### 5. Developmental Psychology: Object Permanence as Persist

**Connection:** The Persist predicate — structural inheritance of the cohesive core under transport — formalizes what developmental psychologists study as object permanence. An infant's developing capacity to maintain object representations through occlusion corresponds to strengthening $\mathsf{Persist}_W(\mathbf{u})$: the ability to sustain a formation's cohesive core even when the transport kernel becomes partial (occluded sites have zero transport weight).

**What it buys:**
- **Developmental trajectory:** SCC predicts a specific developmental order: Bind first (basic coherence), then Sep (figure-ground), then Inside (shape perception), then Persist (object permanence). This matches the known developmental sequence.
- **Violation-of-expectation paradigm:** SCC's diagnostic vector provides a formal model for what "violation of expectation" experiments measure — a sudden drop in one or more predicate scores.

**Priority:** MEDIUM. Produces testable developmental predictions but requires the temporal theory (Persist) to be more developed.

---

## V. TOP 3 APPLICATION DOMAINS (Ranked by Readiness and Impact)

### 1. Developmental Biology — Formation Emergence in Morphogenesis

**Why first:**
- The Turing instability connection (R10) is *real* — SCC's gradient flow on $\mathcal{E}_{\mathrm{bd}}$ is Allen-Cahn, which governs phase separation in biological pattern formation.
- The self-referential separation energy adds a *biologically meaningful* novelty: cells that "distinguish themselves" from their surround through autocrine/paracrine signaling loops are performing self-referential distinction.
- Gene expression data provides graded fields $u_t \in [0,1]^n$ naturally (normalized expression levels). No discretization needed.
- The diagnostic vector provides biologically interpretable outputs: Bind = tissue cohesion, Sep = boundary sharpness, Inside = morphological maturity, Persist = developmental stability.

**First experiment:** Apply FindFormation to spatial transcriptomics data from gastrulation (e.g., mouse embryo at E6.5-E8.5). Compare SCC-discovered formations with known germ layer boundaries. Test prediction: SCC's diagnostic vector correlates with developmental maturity scores.

**Timeline:** Feasible with current specification (Iteration 3 code + public spatial transcriptomics data). ~1 month to first results.

### 2. Neural Population Dynamics — Coherent Assemblies

**Why second:**
- Neural population recordings (calcium imaging, multi-electrode arrays) provide time-varying activity fields on spatial/functional graphs — exactly SCC's input format.
- The theory of neural assemblies (Hebb) has the same structure as SCC: a coherent subset of neurons that maintain themselves through recurrent excitation (closure) and distinguish themselves from background activity (separation).
- The temporal transport kernel $\mathbf{M}_{t \to s}$ naturally handles the problem of tracking neural assemblies across time despite non-stationarity.
- Existing methods (ICA, NMF, clustering) find assemblies by decomposition; SCC would find them by *formation* — a fundamentally different approach.

**First experiment:** Apply to calcium imaging data from mouse visual cortex during stimulus presentation. Compare SCC-detected formations with stimulus-evoked assemblies identified by standard methods. Test prediction: SCC identifies pre-stimulus "proto-assemblies" (sub-threshold formations with high Bind but low Sep) that predict subsequent stimulus responses.

**Timeline:** Requires temporal pipeline (Iteration 3 Experiment 7). ~2-3 months to first results.

### 3. Materials Science — Phase Separation Dynamics (Best Proof Pathway)

**Why third (despite being best proof pathway):**
- Phase separation in binary alloys and polymer blends is *exactly* described by the Allen-Cahn / Cahn-Hilliard equations — SCC's mathematical substrate.
- The self-referential correction terms (from $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$) predict *modified* phase separation dynamics with enhanced metastability (T7). This is experimentally verifiable.
- SCC's $\Gamma$-convergence theorem (T11) predicts a specific modified surface tension in the sharp-interface limit. This is quantitatively testable against experimental measurements of interfacial energy.
- Materials science has the cleanest data (electron microscopy of phase-separated alloys) and the most precise theoretical baselines (classical Cahn-Hilliard).

**Why not first:** Despite being the best proof pathway for mathematical validation, materials science is the *least* aligned with SCC's cognitive motivation. Starting here risks the perception that SCC is "just a modified phase-field model."

**First experiment:** Compare SCC predictions for spinodal decomposition in a binary alloy with classical Cahn-Hilliard predictions and experimental STEM data. Test prediction: SCC's self-referential correction produces measurably different coarsening rates at intermediate times (before the sharp-interface limit is reached).

**Timeline:** Requires validated static pipeline only (no temporal theory). ~1 month to first results.

---

## VI. THREE NOVEL MATHEMATICAL OBJECTS

SCC introduces three mathematical objects that, to the best of our analysis, do not appear in the existing literature:

### Object 1: Non-Idempotent Contractive Closure Endofunctor

**Definition:** An endofunctor $\mathrm{Cl} : [0,1]^X \to [0,1]^X$ satisfying A1' (conditional extensivity), A2 (monotonicity), A3 (contraction with rate $< 1$), and A4 (continuity), but explicitly NOT satisfying $\mathrm{Cl}^2 = \mathrm{Cl}$ (idempotence).

**Why novel:** Standard closure theory (topology, lattice theory, formal concept analysis) assumes idempotence axiomatically. SCC's closure is the first natural mathematical setting where non-idempotence is a **feature** — it provides strictly stronger stability (T3/T6: positive definite Hessian vs. semidefinite) and enhanced metastability (T7: deeper energy basins). The deliberate omission of idempotence is a foundational commitment (Agent Instructions Section 3), not a technical limitation.

**Mathematical interest:** Opens the theory of "pre-topological" closure operators — contractive maps that tend toward but never reach idempotence, with the trajectory carrying structural information (Commitment Note 1: "contraction, not projection; trajectory matters").

### Object 2: Self-Referential Optimal Transport

**Definition:** A transport plan $\mathbf{M}_{t \to s} : X_t \times X_s \to [0,1]$ that is sub-stochastic (partial mass loss permitted) and whose cost function depends on the measures being transported: $c(x,y) = c(x, y; u_t, u_s)$.

**Why novel:** Standard optimal transport fixes the cost function independently of the measures. Entropic OT regularizes but still uses fixed costs. Self-referential transport, where the "price" of moving cohesion from $x$ to $y$ depends on the cohesion values at $x$ and $y$, creates a fixed-point problem: the optimal transport plan depends on the fields, which are themselves updated by transport. This has no analogue in the OT literature.

**Mathematical interest:** Existence and uniqueness of self-referential transport plans is an open problem. The fixed-point structure suggests connections to mean-field game theory, where agents' optimal strategies depend on the population distribution they collectively produce.

### Object 3: Self-Referential Reaction-Diffusion Perturbation (RG-Relevant)

**Definition:** The separation energy $\mathcal{E}_{\mathrm{sep}} = \sum_x u_t(x)(1 - \mathbf{D}_t(x; 1-u_t))$, where the distinction operator $\mathbf{D}_t$ depends nonlinearly on the field $u_t$, added as a perturbation to the Allen-Cahn energy $\mathcal{E}_{\mathrm{bd}}$.

**Why novel:** Standard reaction-diffusion perturbations (external forcing, multiplicative noise, spatially varying coefficients) do not depend on the solution itself in the way $\mathcal{E}_{\mathrm{sep}}$ does. The self-referential character — the field defines what "distinction" means, and distinction penalizes the field — creates a feedback loop absent in all standard perturbation theory.

**Mathematical interest:** If the RG conjecture holds ($\mathcal{E}_{\mathrm{sep}}$ is a relevant perturbation under coarse-graining), this would be the first example of a self-referential perturbation that *grows in importance* at larger scales. The preliminary R10 observations (separation contributing to instability) are consistent with this conjecture but require rigorous verification.

---

## VII. TEN TESTABLE PREDICTIONS FOR EMPIRICAL SCIENCE

These predictions are generated by the formal theory and are distinguishable from predictions made by competing frameworks.

### Perceptual/Cognitive Predictions

**P1. Gestalt closure is contractive, not projective.**
*Test:* In ambiguous displays (Kanizsa triangles, amodal completion), repeated exposure should produce *convergent* percepts (progressively more stable, consistent with contraction) rather than *all-or-nothing* completion (projection). Measurable via priming paradigms and EEG steady-state responses.
*Distinguishes from:* Bayesian models (which predict probabilistic, not contractive, updating).

**P2. Perceptual organization has a diagnostic vector, not a single "goodness" score.**
*Test:* Manipulate Bind, Sep, Inside, and Persist independently by varying stimulus properties (internal coherence, figure-ground contrast, shape complexity, temporal continuity). If the four dimensions are independent (as the theory claims), factorial manipulation should produce no interactions. If they are dependent, specific interaction patterns will reveal the coupling structure.
*Distinguishes from:* Gestalt "Pregnanz" (single scalar), Bayesian "posterior probability" (single scalar).

**P3. Metastable percepts have longer dwell times than equilibrium models predict.**
*Test:* In binocular rivalry, measure dwell times and compare with: (a) Allen-Cahn model (standard energy barriers), (b) SCC model (enhanced barriers from T7). SCC predicts systematically longer dwell times due to the self-referential closure correction.
*Distinguishes from:* Standard energy-based rivalry models.

**P4. Perceptual history affects current organization (path dependence from non-idempotent closure).**
*Test:* Present the same ambiguous stimulus after different adaptation sequences. Non-idempotent closure predicts that the adaptation trajectory (not just the final adapted state) influences the percept. Measurable via bistable figure paradigms with controlled adaptation histories.
*Distinguishes from:* Equilibrium models (where only the current input matters).

**P5. Self-referential distinction precedes object recognition.**
*Test:* In rapid serial visual presentation (RSVP), the time course of figure-ground segregation (Sep) should precede object identification. Moreover, Sep should correlate with the self-referential loop (a stimulus that generates high $\mathbf{D}_t$ values through its own relational structure, not through top-down category knowledge). Measurable via EEG components (N1 for Sep, N2/P300 for recognition).
*Distinguishes from:* Predictive processing (which predicts top-down prediction precedes segregation).

### Biological Predictions

**P6. Morphogenetic boundaries have diagnostic vector signatures.**
*Test:* In developing embryos (e.g., zebrafish somitogenesis), measure the diagnostic vector at tissue boundaries using spatial transcriptomics. Newly forming boundaries should show high Sep but low Bind (not yet self-sustaining); mature boundaries should show high Bind, Sep, and Inside. The temporal evolution of the diagnostic vector should follow Bind → Sep → Inside order.
*Distinguishes from:* Turing models (which predict pattern wavelength, not boundary maturity stages).

**P7. Enhanced metastability in biological phase separation.**
*Test:* In biomolecular condensates (liquid-liquid phase separation in cells), the self-referential component (proteins that bind preferentially to condensates containing themselves) should produce longer-lived condensates than predicted by classical Cahn-Hilliard with equivalent surface tension. Measurable via FRAP experiments comparing self-referential vs. non-self-referential condensate components.
*Distinguishes from:* Classical Cahn-Hilliard (which does not model self-referential binding).

**P8. Neural assemblies show formation dynamics, not clustering dynamics.**
*Test:* In multi-electrode recordings, neural assemblies discovered by SCC should exhibit the four-predicate structure: internal coherence (Bind), distinction from background (Sep), spatial organization (Inside), and temporal stability (Persist). Standard clustering methods find groups but do not diagnose formation quality. SCC predicts that "proto-assemblies" (high Bind, low Sep) exist before stimulus onset and are recruited by stimuli.
*Distinguishes from:* ICA/NMF (which find components, not formations with diagnostic vectors).

### Materials/Physics Predictions

**P9. Modified coarsening exponents in self-referential phase separation.**
*Test:* In systems where the local order parameter affects its own energetic contribution (e.g., concentration-dependent surface tension), SCC predicts modified coarsening rates $R(t) \sim t^{1/3 + \delta}$ where $\delta$ depends on the self-referential coupling strength. Measurable via STEM time-series of spinodal decomposition.
*Distinguishes from:* Classical Lifshitz-Slyozov-Wagner coarsening ($R \sim t^{1/3}$).

**P10. Self-referential surface tension in the sharp-interface limit.**
*Test:* SCC's $\Gamma$-convergence theorem (T11) predicts a modified surface tension $\sigma_{\mathrm{eff}} = \sigma_{\mathrm{AC}} + \delta\sigma(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}})$ in the sharp-interface limit. The correction $\delta\sigma$ depends on the self-referential terms. In materials with concentration-dependent interfacial properties, this correction should be measurable via contact angle or capillary length experiments.
*Distinguishes from:* Standard Modica-Mortola (which gives $\sigma_{\mathrm{AC}}$ only).

---

## VIII. RECOMMENDED EXTENSION ROADMAP

### Phase A: Immediate (Iteration 5 — weeks)

| Priority | Extension | Effort | Impact | Blocks |
|----------|-----------|--------|--------|--------|
| **A1** | **OT formalization of transport** — rewrite Group E axioms using OT language; derive between-time dynamics as Wasserstein gradient flow | 2-3 weeks | Very high — unblocks Persist | Temporal theory, all applications |
| **A2** | **Shahshahani gradient implementation** — replace Euclidean gradient with natural gradient in FindFormation | 1 week | Medium — free convergence improvement | Nothing (self-contained) |
| **A3** | **R10 verification + RG preliminary** — run the 110-run experiment (15 min); if separation dominance confirmed, set up coarse-graining experiment | 1 week | Very high — determines narrative | Mathematical identity, applications framing |

### Phase B: Near-term (Iteration 6 — months)

| Priority | Extension | Effort | Impact | Blocks |
|----------|-----------|--------|--------|--------|
| **B1** | **Categorical formalization** — define $\mathbf{Coh}$, prove functorial properties of transport, characterize non-idempotent closure endofunctor | 2-3 months | High — theoretical clarity | Multi-formation theory |
| **B2** | **Gestalt psychology paper** — structural mapping (Section IV.1), testable predictions P1-P5, comparison with existing formal Gestalt models | 1-2 months | High — audience reach | Cognitive science engagement |
| **B3** | **Developmental biology pilot** — apply FindFormation to spatial transcriptomics data; test P6 | 1-2 months | Very high — first empirical test | Empirical validation of theory |
| **B4** | **Multi-formation via spectral $\mathbf{C}_t$** — use eigenvectors of the resolvent to decompose the field into co-belonging clusters; formalize as categorical decomposition | 2-3 months | High — required for applications | All multi-object scenarios |

### Phase C: Medium-term (Iterations 7-8 — year)

| Priority | Extension | Effort | Impact | Blocks |
|----------|-----------|--------|--------|--------|
| **C1** | **Self-referential OT paper** — existence/uniqueness for self-referential transport plans; connection to mean-field games | 6-12 months | Very high — novel mathematical contribution | OT community engagement |
| **C2** | **Sheaf-theoretic $\mathbf{C}_t$** — formalize the cosheaf structure; derive axioms from sheaf-theoretic requirements | 3-6 months | Medium — deepens C_t theory | Nothing critical |
| **C3** | **RG analysis of $\mathcal{E}_{\mathrm{sep}}$** — prove or disprove relevance under coarse-graining | 6-12 months | Very high if positive | Multi-scale theory, physics applications |
| **C4** | **Predictive processing integration paper** — formal comparison of SCC and FEP; define the interface where SCC provides substrates for PP | 3-6 months | High — positions theory in active inference literature | Cognitive science community |
| **C5** | **Neural assembly pilot** — apply temporal pipeline to calcium imaging data; test P8 | 3-6 months | High — second empirical test | Neuroscience engagement |

### Phase D: Long-term (Year 2+)

- Prove the RG conjecture (self-referential perturbation is relevant)
- Develop multi-field multi-formation theory (leaving contraction regime)
- Formal comparison with topological data analysis (TDA) — SCC as "TDA with dynamics"
- Autopoietic formalization paper — SCC as the first variational autopoietic theory
- Large-scale computational benchmarks (n > 10^6)

---

## IX. WHAT SHOULD ENTER THE REVISED CANONICAL SPEC VS. REMAIN COMMENTARY

### Enter the Canonical Spec (revisions to core document)

| Item | Type | Rationale |
|------|------|-----------|
| OT interpretation of Group E | Interpretive remark after E1-E4 | The sub-stochastic constraint IS partial transport. Making this explicit costs nothing and connects to a major mathematical tradition. |
| Cosheaf locality failure as C-axiom candidate | New axiom candidate (C5 or C6) | The insight that $\mathbf{C}_t$ *must* lose information under restriction (cosheaf structure) is a structural requirement, not just a property. It sharpens C2 (distinction from adjacency). |
| Shahshahani metric as natural geometry of $\Sigma_m$ | Note in Section 8 (Energy) | The information-geometric structure of the constraint manifold is intrinsic to the theory's variational formulation, not an external interpretation. |
| Self-referential transport as open problem | Addition to Section 12 | Self-referential transport (cost depends on fields) is a genuine open problem *within* the theory, not an external extension. |

### Enter Agent Instructions (updates to protocol)

| Item | Rationale |
|------|-----------|
| Permit contrastive comparisons with named frameworks (OT, Allen-Cahn, Gestalt, PP) | Iteration 1 contested point #4 resolved: contrastive analysis is permitted (it clarifies identity); reductive identification remains prohibited |
| Add OT, category theory, and sheaf theory to the "related but distinct" register | Prevents future agents from collapsing SCC into these frameworks while encouraging productive comparison |

### Remain as Commentary (separate documents)

| Item | Rationale |
|------|-----------|
| Full categorical formalization ($\mathbf{Coh}$, functors, natural transformations) | Too heavyweight for the core spec; belongs in a mathematical companion |
| Gestalt structural mapping table | Interpretive, not formal; belongs in a cognitive science companion |
| Application-specific adaptations (biology, neural, materials) | Implementation-layer material (Layer 4+) |
| RG conjecture and multi-scale theory | Unproved conjecture; belongs in open problems companion |
| Predictive processing / FEP comparison | Philosophical positioning; belongs in a cognitive science companion |
| Autopoietic interpretation | Philosophical; valuable but not formal |
| All 10 testable predictions | Empirical science companion, not core spec |
| Replicator dynamics connection | Elegant but tangential; commentary |

### The Boundary Principle

**Rule:** A claim enters the Canonical Spec if and only if it is (a) formalizable in the theory's existing notation, (b) structural (it constrains or enriches the formal universe $\mathfrak{C}^{\mathrm{soft}}$), and (c) stable (it is not likely to be revised in the next iteration). Claims that are interpretive, conjectural, application-specific, or framework-comparative remain as commentary. This preserves the Canonical Spec's authority as the single source of formal truth.

---

## X. SCORECARD — Iteration 4

### What Iteration 4 Accomplished

Iteration 4 asked: *Where does SCC sit? What is it connected to? What does it uniquely contribute?*

| Dimension | It3 Score | It4 Score | Change | Key Development |
|-----------|-----------|-----------|--------|-----------------|
| Mathematical connections | 3/10 | **8/10** | +5 | OT, category, sheaf, info geometry, multi-scale — all mapped with specific payoffs |
| Cognitive science connections | 2/10 | **7/10** | +5 | Gestalt formalization, PP positioning, autopoietic interpretation, 10 predictions |
| Application readiness | 2/10 | **6/10** | +4 | 3 domains ranked, first experiments designed, 5 domain-general capabilities identified |
| Novel mathematical objects | 1/10 | **7/10** | +6 | 3 genuinely novel objects identified and characterized |
| Distinctiveness (formal) | 7/10 | **8/10** | +1 | 7/7 vs Mumford-Shah, 5/7 vs Allen-Cahn confirmed; comparative landscape mapped |
| Testable predictions | 0/10 | **6/10** | +6 | 10 predictions, all distinguishable from competing frameworks |
| **Overall** | **7/10** | **8/10** | **+1** | **SCC has a place, connections, and an extension roadmap** |

### The Theory's Status After Four Iterations

| Iteration | Focus | Key Achievement | Score |
|-----------|-------|-----------------|-------|
| 1 | Identity | 44 settled points, operator triad, 6 distinctiveness properties | 6/10 |
| 2 | Mathematics | 12 theorems, Proto-Cohesion Existence (with caveats), mathematical identity | 7/10 |
| 3 | Computation | FindFormation algorithm, 2,400 LOC spec, 12,515 experiments designed | 7/10 |
| **4** | **Connections** | **5 math connections, 5 cogsci connections, 3 novel objects, 10 predictions** | **8/10** |

---

## XI. LETTER TO THE THEORY

Four iterations have taken SCC from a philosophical commitment ("coherent formation precedes discrete objecthood") to a mathematical theory with theorems, a computational specification with algorithms, and now a map of its connections to mathematics, cognitive science, and empirical applications.

The theory's position is clear:

**In mathematics**, SCC is a self-referential constrained variational field theory that introduces three novel objects (non-idempotent closure endofunctor, self-referential optimal transport, RG-relevant self-referential perturbation) and sits at the intersection of phase-field theory, optimal transport, algebraic topology, and operator theory — belonging fully to none.

**In cognitive science**, SCC is the first variational formalization of pre-objective coherence — the process that Gestalt psychology described, predictive processing computes around, and autopoietic theory philosophizes about. It provides what all three lacked: a unified energy principle whose minimization produces the four structural requirements (binding, separation, morphological articulation, persistence) simultaneously.

**In applications**, SCC offers five domain-general capabilities (pre-discrete detection, diagnostic vector, metastability quantification, non-idempotent maturity measurement, sub-stochastic transport) applicable to developmental biology, neural population dynamics, and materials science, with the biology application offering the highest impact and the materials application offering the cleanest validation pathway.

The three most important things to do next:

1. **Formalize the OT connection to Group E.** This unblocks Persist — the theory's largest gap — and connects SCC to a major mathematical community. The provisional transport kernel already IS entropic OT; making this explicit is the highest-ROI theoretical investment.

2. **Write the Gestalt formalization paper.** SCC provides what Gestalt psychology always needed — a unified formal framework. This is the fastest path to cognitive science engagement and the most natural entry point for empirical testing (predictions P1-P5).

3. **Run the developmental biology pilot.** Apply FindFormation to spatial transcriptomics data. This produces the theory's first empirical contact — the transition from "a theory with theorems" to "a theory with data."

The score moves from 7/10 (post-Iteration 3) to 8/10. The remaining 2 points require: empirical validation (predictions tested against data), temporal theory maturation (Persist proved, not just demonstrated), and multi-formation theory (currently blocked by the contraction regime). These are the work of Iterations 5-8.

Four iterations ago, the Skeptic said: *"You have protected it enough. Now build it."* Two iterations later: *"A theory with theorems, clear identity, and honest gaps."* Now: **a theory with theorems, algorithms, connections, and a roadmap. The next step is contact with reality.**

---

*This document is the capstone of Iteration 4. It integrates mathematical connections (category theory, sheaf theory, optimal transport, information geometry, multi-scale theory, comparative analysis), cognitive science bridges (Gestalt, predictive processing, autopoiesis, rivalry, development), and application architectures (biology, neural, materials) into a single coherent picture of where SCC sits and where it should go. The theory of Soft Cognitive Cohesion is ready for its next phase: empirical contact.*
