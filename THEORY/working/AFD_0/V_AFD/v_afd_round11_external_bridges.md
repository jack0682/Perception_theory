---
type: working/afd/v_afd
status: V-AFD Round 11 External Bridges (2026-05-12)
parent: v_afd_round10_master_v2.md
session_origin: logs/daily/2026-05-12/40_v_afd_session.md → Round 11 continuation
mandate: user "좀더 깊이 keep going"
canonical_compatibility: CV-1.13 read-only
non_goals:
  - reductive claim that SCC = any external framework (CN10)
  - silently identify Bind/Sep/Inside with ML loss functions
  - claim V-AFD resolves consciousness / hard problem
---

# V-AFD Round 11 — External-Framework Bridges

Round 11 opens four **comparative bridges** between V-AFD and external frameworks. The bridges are **contrastive**, not reductive (per CN10 of canonical SCC: comparison allowed, reduction forbidden). Each bridge identifies *structural analogies* and *differences*, never claiming "V-AFD = X".

- (Part A) **V-AFD ↔ Representation Learning / ML.** Z(u) as a learnable embedding; Pareto preorder as multi-objective optimization. **V-AFD-T41**.
- (Part B) **V-AFD ↔ Bayesian Formation Inference.** $\nu_{T_*}$ as posterior on V_Z; $E$ as negative log-likelihood. **V-AFD-T42**.
- (Part C) **V-AFD ↔ Free Energy Principle (Friston-style).** V-AFD vector as variational state; $C_V$ as path free energy. **V-AFD-T43**.
- (Part D) **V-AFD ↔ Neuroscience Perception Theory.** Formation as a perceptual object hypothesis; transitions as perceptual reorganization. **V-AFD-T44 (discussion)**.
- (Part E) Round 11 audit + Round 12 priorities.

**Compatibility statement.** Adds V-AFD-T41..T44 as **comparative theorems / discussions**, *not* reductive identifications. Aligns with canonical CN10 and CLAUDE.md non-reductive policy. No canonical edit.

---

## Part A — V-AFD ↔ Representation Learning (V-AFD-T41)

### A.1 Setup

Representation learning (Bengio 2013; Bengio-Courville-Vincent 2014): given high-dim inputs $u$, learn a low-dim embedding $\phi(u) \in \mathbb{R}^d$ that *preserves* task-relevant information and *discards* task-irrelevant variance.

V-AFD's $\pi_Z : \Sigma_m \to \mathcal{Z}$ is a *low-dim projection* (effective dim ~K_field per V-AFD-T24) from the field state space Σ_m (dim $n = |V|$). **Structural analogy** with representation learning.

### A.2 The analogy

| Representation Learning | V-AFD analog | Comment |
|---|---|---|
| Input space $\mathbb{R}^n$ | $\Sigma_m \subset \mathbb{R}^n$ | V-AFD constrained to volume simplex |
| Embedding $\phi(u) \in \mathbb{R}^d$ | $Z(u) = \pi_Z(u) \in \mathcal{Z}$ | Both are dim-reducing maps |
| Task-relevant features | Bind, Sep, Inside, Persist + K, E, τ | V-AFD pre-specifies the "task-relevant" features |
| Information loss | V-AFD-T9 | V-AFD makes loss explicit |
| Symmetry invariance | Group-equivariant networks | V-AFD-T14(a) Aut(G)-equivariance |
| Multi-task / multi-objective | Pareto loss | V-AFD-D8 Pareto preorder |
| Latent space structure | $\mathcal{Z}$ = product space | V-AFD has explicit factor structure |
| Distance in latent space | Product metric $d_\mathcal{Z}$ | V-AFD definite metric (with K-jump indicator) |
| Stability of representation | V-AFD-T26 robustness | Under parameter perturbation |

### A.3 V-AFD-T41 — Structural Analogy Theorem

**Theorem V-AFD-T41 (V-AFD as Pre-specified Representation Learning).** Under canonical V-AFD axioms:

(R-1) The V-AFD projection $\pi_Z$ is a **hand-designed (non-learned) feature extractor** producing a low-dim, interpretable, task-relevant embedding.

(R-2) The V-AFD-T24 effective dim ~K_field (compression ratio ~$n/K_{\mathrm{field}}$ for canonical SCC) matches typical ML representation-learning compression ratios.

(R-3) V-AFD-T14(a) Aut(G)-equivariance is the **canonical SCC analog** of equivariant deep networks (Cohen-Welling 2016).

(R-4) V-AFD-D8 Pareto preorder is the **multi-objective optimization analog** for SCC: instead of summing diagnostic components into a scalar loss, V-AFD explicitly preserves componentwise comparison.

(R-5) V-AFD-T9 information loss is **principled**: V-AFD explicitly tracks what is lost (basin labels, intra-basin geometry, sorted-bar reordering), unlike black-box ML embeddings.

(R-6) V-AFD is **not** a learned representation — it is the canonical SCC-derived diagnostic. The analogy is **structural**, not reductive.

**Status.** **Theorem Cat A descriptive** (analogy mapping; no SCC operator changes).

**Cat self-rating.** A descriptive.

### A.4 What V-AFD shares with ML

- **Compression:** both V-AFD and ML embed high-dim inputs into lower-dim representation.
- **Symmetry handling:** Aut(G)-equivariance (V-AFD-T14a) ↔ group-equivariant networks.
- **Multi-objective:** Pareto preorder ↔ multi-task learning.
- **Information loss tracking:** V-AFD explicit (T9, T14) ↔ ML rate-distortion theory implicit.

### A.5 What V-AFD does NOT share with ML

(NO-1) **No learning.** V-AFD's $\pi_Z$ is determined by canonical SCC operators (A3 closure, Pred-E Bridge, QM3, CSEH). No training.

(NO-2) **No optimization on the embedding.** The map $\pi_Z$ is given; the structure ON $\mathcal{Z}$ (Pareto preorder, vector cost, Lyapunov sheaf) is derived from canonical SCC.

(NO-3) **No "task" in the supervised sense.** Formation extraction is not a labeled-data problem.

(NO-4) **No universality claim.** V-AFD does not claim to be optimal among all possible projections of Σ_m; it is **the canonical SCC vector representation**, specified by ontological choice.

### A.6 OP-VAFD-021 (new R11)

**OP-VAFD-021.** Investigate whether *learned* refinements of $\pi_Z$ (e.g. fine-tuning weights $w$ in $Q_w$ or augmenting Z with learned features) improve V-AFD's discriminative power for specific tasks. **Severity L** (engineering direction; canonical V-AFD is fixed). Register for future ML-side study.

---

## Part B — V-AFD ↔ Bayesian Formation Inference (V-AFD-T42)

### B.1 Setup

Bayesian inference: given observations, compute posterior $p(\text{state} \mid \text{obs}) \propto p(\text{obs} \mid \text{state}) \cdot p(\text{state})$.

In V-AFD setting: "state" = formation F ∈ V_form; "obs" = the field configuration $u$; "posterior" = probability that u is in each basin.

### B.2 The mapping

Reflected gradient Langevin SDE at T_* > 0 has Gibbs invariant measure $\mu_{T_*}(du) = e^{-E(u)/T_*}/Z_{T_*}$. Reading $E$ as **negative log-likelihood**:

$$-\log p(u \mid \Theta) \;\propto\; E(u; \Theta) / T_*,$$

with $\Theta$ = parameters (canonical OMS), $T_*$ = inverse-temperature.

Posterior on V_form (basin label) given an observed field state $u_{\mathrm{obs}}$:

$$p(F \mid u_{\mathrm{obs}}) \;=\; \mathbf{1}[u_{\mathrm{obs}} \in B_F].$$

(In the deterministic case; trivial since basins partition.) Posterior at noise $T_*$ on an observed window $\{u_t\}$ trajectory:

$$p(F \mid \{u_t\}) \;\propto\; \int_{B_F} p(\{u_t\} \mid u_0) \cdot p(u_0) \, du_0,$$

with $p(\{u_t\} \mid u_0)$ the SDE path density (Onsager-Machlup, Layer-3 conditional).

### B.3 V-AFD-T42 — Bayesian Bridge

**Theorem V-AFD-T42 (V-AFD as Bayesian Formation Inference, conditional).** Under canonical Pkg I Cat A + Layer-3 EK hypotheses:

(B-1) **V-AFD invariant measure $\nu_{T_*}$ = marginal posterior on V_Z** via the projection: $\nu_{T_*}(A) = \mu_{T_*}(\pi_Z^{-1}(A))$ for measurable $A \subset V_Z$.

(B-2) **V-AFD K-selection (V-AFD-T20-general) = MAP estimation in $\nu_{T_*}$:** $K^* = \arg\max_K \nu_{T_*}(S_K^Z)$ and $F^* = \arg\max_F \nu_{T_*}(\{Z_F\})$ (with appropriate mod-Aut(G) tie-breaking).

(B-3) **V-AFD-T17-sharper(a)-quantitative ↔ Bayesian regime where the posterior is sharply concentrated on F^*** = K=1 global min at β > 5β_crit, T_* → 0.

(B-4) **V-AFD-T9 information loss = marginalization bias:** projecting out intra-basin coordinates loses Bayes information, just as marginalizing a posterior loses dimension-specific information.

(B-5) **V-AFD-T35 quasipotential ↔ Bayesian "negative-log-likelihood ratio":** $V^{\mathrm{V}}(Z_i, Z_j) / T_* = -\log [p(Z_j | u_{\mathrm{obs}} \in B_{F_i}) / p(Z_i | u_{\mathrm{obs}} \in B_{F_i})]$ in the small-T_* limit (FW asymptotic).

(B-6) **V-AFD-T34-Layer-2 strong connectivity ↔ Bayesian completeness:** every formation state reachable from every other implies the chain explores the full posterior support.

**Status.** **Theorem Cat A (B-1, B-2, B-4, B-6)**; **L3 conditional (B-3, B-5)**.

**Cat self-rating.** Mostly A; L3 cond for FW-related parts.

### B.4 What this says

V-AFD is **compatible with Bayesian formation inference**: the canonical Gibbs measure projects to V-AFD vector image, V-AFD K-selection becomes posterior MAP, V-AFD-T9 information loss becomes marginalization.

This is **not** a reduction: V-AFD's Pareto preorder, multi-criteria cost, K-jump structure, Conley extension, etc., are **not** captured by Bayesian posterior alone. The Bayesian bridge is a *projection* of V-AFD onto a subset of its structure.

### B.5 OP-VAFD-022

**OP-VAFD-022.** Explicit calculation of marginal posterior $\nu_{T_*}$ on canonical 15×15 V_Z; compare V-AFD MAP with V-AFD-T17-sharper(a) singleton. Severity M.

---

## Part C — V-AFD ↔ Free Energy Principle (V-AFD-T43)

### C.1 Setup

Free Energy Principle (Friston 2009, 2010): biological systems minimize **variational free energy**

$$F[q] \;=\; \mathbb{E}_q[\log q - \log p],$$

where $q$ is a *variational* (approximate posterior) distribution and $p$ is the true generative model.

Active inference: agents act to minimize *expected* free energy:

$$\mathbb{E}[F] \;=\; \text{epistemic value} + \text{pragmatic value}.$$

### C.2 V-AFD ↔ FEP analogy

In V-AFD:
- Variational distribution $q$ = a distribution on Σ_m or V_Z representing the "agent's belief" about the formation state.
- Generative model $p$ = canonical Gibbs $\mu_{T_*}$ at fixed parameters.

For $q = \nu_{T_*}$ exactly: $F[\nu_{T_*}] = 0$ (variational distribution matches truth; KL = 0).

For $q \neq \nu_{T_*}$: $F[q] = \mathrm{KL}(q \| \nu_{T_*}) \geq 0$.

### C.3 V-AFD-T43 — FEP Bridge (Discussion-level)

**Theorem V-AFD-T43 (V-AFD ↔ FEP, discussion-level).** Under canonical Pkg I + V-AFD-T33:

(FEP-1) The V-AFD invariant measure $\nu_{T_*}$ on V_Z is the *unique minimizer of variational free energy* among all probability measures on V_Z, given fixed Gibbs prior $\mu_{T_*}$ on Σ_m.

(FEP-2) **Gradient flow as free-energy descent:** the SCC gradient flow $\dot u = -P_T \nabla E$ at T_* = 0 is the deterministic limit of the SDE that *minimizes a path-integral free energy* (Onsager-Machlup; Layer 3).

(FEP-3) **Active inference analog:** an agent observing partial information (e.g. one component of $D(u)$) could compute the variational free energy of competing formation-states and select the F minimizing it. **This is the Bayesian MAP (V-AFD-T42 B-2) reformulated in FEP language.**

(FEP-4) **V-AFD Pareto preorder ↔ FEP multi-objective free energy:** when "free energy" is vector-valued (one component per task / criterion), Pareto-incomparable agents are FEP-compatible without scalar reduction.

(FEP-5) **V-AFD vector cost $C_V$ ↔ FEP expected free energy on trajectories:** the cost C_V along a path is the (Layer-2 deterministic) analog of expected free energy in active inference, generalized to multi-criteria.

**Status.** **Discussion-level (not a math theorem)** — V-AFD-T43 is a *framework-comparison* statement.

**Cat self-rating.** Discussion / structural analogy.

### C.4 What V-AFD does NOT claim about FEP

(C-N1) V-AFD does **not** claim to *be* the Free Energy Principle. CN10: contrastive, not reductive.

(C-N2) V-AFD's deterministic Layer-2 dynamics is **not** active inference: active inference includes action selection by an agent; V-AFD's gradient flow is autonomous (no agent).

(C-N3) FEP's *generative model* hypothesis is not V-AFD's *canonical Gibbs* — they may overlap but are not identified.

(C-N4) V-AFD does not claim biological substrate (per CLAUDE.md: SCC is a mathematical theory of perception, not biology).

### C.5 OP-VAFD-023

**OP-VAFD-023.** Formalize V-AFD ↔ FEP at the level of an active-inference variant of V-AFD (V-AFD + action selection) and check whether canonical SCC dynamics emerges as a limit of FEP optimization. Severity L (speculative / external).

---

## Part D — V-AFD ↔ Neuroscience Perception Theory (V-AFD-T44, Discussion)

### D.1 Context

SCC's stated agenda (canonical DECLARATION.md, CLAUDE.md): "before objects, there are cohesive formations." The theory has **explicit non-reductive intent toward neuroscience perception** (DECL-1.0, CN10).

V-AFD's vector state $Z(u)$ is naturally interpretable as a **neural representation of the formation**:
- Bind ↔ "coherence" of a percept.
- Sep ↔ "figure-ground separation."
- Inside ↔ "object-like solidness."
- Persist ↔ "temporal binding / object continuity."

This is **not a claim** of biological reduction; it is a **discussion-level mapping** of SCC's diagnostic vector to perception-research vocabulary.

### D.2 V-AFD-T44 — Perception Bridge Discussion

**Discussion V-AFD-T44 (V-AFD ↔ Neuroscience Perception, framework-comparison only).**

(P-1) **Bind ↔ binding problem.** In neuroscience, the *binding problem* (Treisman 1996) asks: how do separate features get unified into a single percept? Bind in V-AFD-D1 quantifies *intra-formation coherence* — a structural analog.

(P-2) **Sep ↔ figure-ground / Gestalt separation.** Wertheimer / Koffka Gestalt principles emphasize separation of figure from ground. Sep in V-AFD-D1 quantifies separation-from-background.

(P-3) **Inside ↔ object solidness / figural goodness.** Gestalt's "good figure" + amodal completion suggest perceptual systems detect *interior coherence* — V-AFD's Inside diagnostic captures this via H_0 persistence + mass concentration.

(P-4) **Persist ↔ object continuity / temporal binding.** Spelke (1990) object permanence + Treisman temporal binding. V-AFD-D1 pairwise Persist (T28 Cat A) is the SCC analog.

(P-5) **K_act ↔ subitizing count.** Trick-Pylyshyn (1994) subitizing: humans rapidly count up to ~4 objects. K_act in V-AFD is an analog of this discrete count.

(P-6) **Vector dynamics ↔ perceptual reorganization.** Bistable percepts (Necker cube, Rubin face-vase) involve discrete switches between two formations. V-AFD vector transitions $Z_i \Rightarrow Z_j$ are the structural analog of such switches.

(P-7) **Pareto preorder ↔ multi-criteria perception.** Different perceptual qualities (binding, separation, solidness, continuity) are not collapsed to a single scalar — V-AFD's Pareto preorder reflects this.

(P-8) **V-AFD-T17-sharper(a) singleton at high β ↔ "clean" perceptual decision.** At high β (high contrast / strong cohesion), the K=1 Pareto frontier is singleton — corresponds to *unambiguous* perception. Lower β allows Pareto-incomparable formations → ambiguous perception (cf. Necker cube).

### D.3 What V-AFD-T44 is and is not

**It is:** a structural-analogy mapping between V-AFD diagnostic vectors and classical perception-research vocabulary.

**It is not:**
- A biological-mechanism claim.
- A reduction of perception to V-AFD (CN10).
- A claim that SCC describes any specific neural circuit.
- An identification of K_act with subitizing capacity (analogy, not equation).
- A resolution of the binding problem (which is open).

**Status.** **Discussion-level framework comparison**. Not a math theorem.

**Cat self-rating.** Discussion only.

### D.4 OP-VAFD-024

**OP-VAFD-024.** Develop V-AFD-T44 from discussion-level to mathematical-structural-comparison level: formalize the analogy mappings and explicitly state which V-AFD claims have neuroscientific testable predictions (vs which are purely mathematical). Severity L (cross-disciplinary).

---

## Part E — Round 11 Self-Audit + Round 12 Priorities

### E.1 Round 11 Self-audit (per CN10)

The audit for Round 11 has an additional focus: **non-reductive policy** (CN10 of canonical SCC).

1. ✓ Projection not replacement: T41 explicitly states V-AFD is not learned (NO-1); T42 marginal posterior projection only; T43 framework comparison; T44 discussion.
2. ✓ Persist forms: unchanged.
3. ✓ Continuity explicit: unchanged.
4. ✓ K_act discontinuity: unchanged.
5. ✓ τ stability: unchanged.
6. ✓ Injectivity loss: T42 (B-4) marginalization bias = V-AFD-T9 information loss restatement.
7. ✓ Nonnegativity: unchanged.
8. ✓ Not a metric: unchanged.
9. ✓ H-MORSE free: all R11 bridges Layer-2 base; FEP / Bayesian L3 conditional parts explicitly marked.
10. ✓ EK Layer-3 only: T42 (B-3), (B-5) L3 cond explicit.
11. ✓ Scalarization optional: T41 (R-4) explicit Pareto over scalar.
12. ✓ Pareto incomparability: T41 (R-4) + T43 (FEP-4) preserves.
13. ✓ Markovianity open: unchanged.
14. ✓ Examples concrete: T44 mentions Necker cube etc.
15. ✓ Honest statuses: T41 Cat A descriptive; T42 mixed (A core, L3 conditional); T43 discussion; T44 discussion.

**CN10 audit:**
- ✓ T41 explicitly disclaims "V-AFD is not a learned representation" (NO-1).
- ✓ T42 distinguishes Bayesian *bridge* from Bayesian *identification* (B-1 is a projection statement, not equivalence).
- ✓ T43 explicit (C-N1)–(C-N4) "V-AFD does NOT claim to be FEP."
- ✓ T44 explicit "structural analogy, not biological reduction" (D.3).

**No reductive claim in Round 11.** Audit PASS on all 15 + CN10.

### E.2 Round 11 deltas

| ID | Statement | Status | Cat |
|---|---|---|---|
| **V-AFD-T41** | V-AFD ↔ ML structural analogy | Theorem (descriptive) | A descriptive |
| **V-AFD-T42** | V-AFD ↔ Bayesian formation inference | Theorem | A (B-1, B-2, B-4, B-6); L3 cond (B-3, B-5) |
| **V-AFD-T43** | V-AFD ↔ FEP discussion | Discussion | — |
| **V-AFD-T44** | V-AFD ↔ neuroscience perception discussion | Discussion | — |

### E.3 OP deltas

| ID | Severity | Status |
|---|---|---|
| **OP-VAFD-021** (new) | L | ML-side fine-tuning of $\pi_Z$ |
| **OP-VAFD-022** (new) | M | Marginal posterior explicit calculation |
| **OP-VAFD-023** (new) | L | FEP active-inference V-AFD variant |
| **OP-VAFD-024** (new) | L | Neuroscience formal comparison |

### E.4 Round 12 priorities

Given v2.0 master is consolidated (R10) and external bridges established (R11), Round 12 can focus on:

(P-A) **Execute V-AFD-T40 numerical baseline** — definitive test of V-AFD-T14(c)-conj, T17-sharper(a)-q, T15, T29. **CODE-side**, 2–3 sessions.

(P-B) **OP-VAFD-016a Cat A** — non-convex Cheeger constant. 1 session.

(P-C) **V-AFD-T35 explicit quasipotential calculation** for canonical 15×15 transitions. 1–2 sessions.

(P-D) **V-AFD ↔ ∞-categorical extension** — derived V-AFD or higher functoriality. 1–2 sessions.

(P-E) **V-AFD ↔ category theory of perception** — Yoneda-style embedding of V_form into a category of "test perception probes." 2 sessions.

(P-F) **V-AFD paper draft** — manuscript-quality outline based on v2.0 + external bridges. 1–2 sessions.

(P-G) **V-AFD ↔ thermodynamic geometry** — Ruppeiner / Weinhold metric on $\mathcal{Z}$ inducing curvature analysis. 1 session.

### E.5 Reflections on V-AFD's growing scope

After 11 rounds, V-AFD has bridges to:

- **Static + Temporal + Conley** modalities (V-AFD internal).
- **OMS-2.0** observer-moduli framework (canonical Appendix).
- **Classical metastability theory** (Bovier-Den Hollander).
- **Representation learning / ML**.
- **Bayesian inference**.
- **Free Energy Principle**.
- **Neuroscience perception**.
- **Category theory** (functorial structure).
- **Ergodic theory** (invariant measure).
- **Large-deviation theory** (LDP rate function).

V-AFD is becoming a **generalist Layer-2 framework**, bridging SCC core to multiple external mathematical / scientific frameworks while preserving CN10 (contrastive, not reductive).

This is in line with the original AFD-T9 commitment: V-AFD provides **transition order**, EK provides **transition rate**, and the broader frameworks (ML, Bayesian, FEP, neuroscience) provide **interpretation contexts** — all on top of the canonical V-AFD architecture.

---

## Closing slogans Round 11

> **V-AFD-T41:** V-AFD is a *pre-specified* representation: hand-designed interpretable embedding, multi-objective by Pareto preorder. Structurally analogous to ML but **not learned**.
>
> **V-AFD-T42:** V-AFD invariant measure is the marginal posterior on V_Z; V-AFD K-selection is Bayesian MAP. Cat A core + L3 conditional refinements.
>
> **V-AFD-T43:** V-AFD is FEP-compatible (variational free energy minimized at $\nu_{T_*}$); but V-AFD is **not** identified with FEP — CN10 preserved.
>
> **V-AFD-T44:** V-AFD's diagnostic vector has structural analogies to neuroscience perception vocabulary (binding, figure-ground, subitizing); discussion-level, not biological-reduction.

V-AFD Round 11 establishes 4 external-framework bridges. All preserved as **contrastive comparisons** per CN10. V-AFD is now a multi-bridge Layer-2 framework with explicit non-reductive policy.

---

*End of `v_afd_round11_external_bridges.md`. V-AFD Round 11 closed.*
