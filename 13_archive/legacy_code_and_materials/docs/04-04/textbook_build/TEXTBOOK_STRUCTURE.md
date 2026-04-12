# Textbook Structure: Soft Cognitive Cohesion — A Mathematical Theory of Pre-Objective Formation

**Date:** 2026-04-04 (Updated: 600pp expansion)
**Session:** Textbook architecture design — expanded edition
**Category:** synthesis
**Status:** active
**Depends on:** Canonical Spec v2.1, all 12 iterations (I1-I12), 48 Category A theorems

---

## Expansion Summary (336pp → 600pp+)

| Metric | Previous | Expanded | Change |
|--------|----------|----------|--------|
| **Total pages** | 336 | **616** | +83% |
| **Total figures** | 42 | **90** | +114% |
| **Total tables** | 18 | **28** | +56% |
| **Content ratio** | 60/25/15 | **50/10/35/5** | More visual |

**Content ratio (600pp basis):**
- Prose: 50% (~308pp) — explanatory text, motivation, examples
- Figures + captions: 35% (~216pp) — rich visualization throughout
- Equations + proofs: 10% (~62pp) — complete proofs where appropriate
- Tables: 5% (~30pp) — data, registries, comparisons

---

## Front Matter

### Foreword (3 pages)
- **By:** A recognized figure in mathematical physics or theoretical cognitive science
- Candidates: someone working at the intersection of variational methods and perception theory
- Frame: why a graded, pre-objective account of formation matters for both mathematics and cognition
- **NEW:** Brief historical perspective on the gap between continuum models and discrete individuation

### Preface (6 pages)
- **Motivation:** The gap between continuous perception and discrete objecthood — no existing framework addresses the *emergence* of coherence prior to individuation
- **Audience:** Three tracks
  - *Mathematicians:* variational methods on graphs, phase-field theory, optimal transport — new self-referential structures
  - *Cognitive scientists:* formal account of Gestalt-like phenomena, testable predictions, relationship to predictive processing/IIT/active inference
  - *ML/AI researchers:* non-standard soft segmentation, self-referential energy minimization, graph neural architecture insights
- **Prerequisites:** Linear algebra, basic real analysis, familiarity with optimization. Graph theory and PDE background helpful but not required (self-contained appendices provided)
- **How to read this book:**
  - Sequential path (Parts I-IV): full understanding
  - Math-first path: Chapters 1, 4-9, Appendix A
  - Cognitive science path: Chapters 1-3, 7, 10-12
  - Implementation path: Chapters 1, 4-5, 8-9, 13-14
- **NEW:** Guided exercises note — each chapter ends with discussion questions and computational exercises
- **NEW:** Companion code note — all experiments reproducible via `scc/` package

### Notation and Conventions (5 pages)
- Symbol table (u_t, Cl_t, D_t, N_t, M_{t→s}, etc.)
- Summation convention (ordered pairs vs. unordered; Section 0 of spec)
- Norm conventions (l^2 default, l^inf where noted)
- Indexing: t temporal, x spatial, k formation index
- **NEW:** Visual notation guide with annotated equation examples (2 figures)
- **NEW:** Quick-reference fold-out table

### List of Theorems (3 pages)
### List of Figures (3 pages)
### List of Algorithms (1 page)

**Front matter total: ~21 pages, 2 figures**

---

## Part I: Foundations — Why Soft Cognitive Cohesion? (Chapters 1-3, ~80pp)

### Chapter 1: The Problem of Pre-Objective Formation
**Learning objectives:** Understand why existing frameworks start "too late"; articulate the gap between perception and discrete objecthood; appreciate why a graded field is more primitive than a crisp set.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 1.1 | Objects Are Not Given | 4 | The philosophical problem: perception does not begin with separated, labeled things. Everyday examples (fog, crowd, dawn, watercolor edges). Extended discussion with visual examples. |
| 1.2 | Where Existing Theories Start Too Late | 5 | Segmentation assumes boundaries; tracking assumes identity; clustering assumes distance. Each presupposes what needs explaining. **NEW:** Detailed comparison table of 5 frameworks and their implicit assumptions. |
| 1.3 | What Would a Pre-Objective Theory Look Like? | 4 | Five desiderata: graded fields, self-referential structure, emergence of inside/outside, temporal inheritance without tracking IDs, energy-based characterization. **NEW:** Each desideratum with a concrete visual example. |
| 1.4 | The Central Metaphor: Cohesion as a Field | 4 | The soft cohesion field u_t : X_t → [0,1]. Not probability, not membership — intensity of cohesive participation. **NEW:** Three different field examples on 10×10 grid with heatmap visualizations. |
| 1.5 | Overview of the Theory | 4 | Roadmap: formal universe, five axiomatic groups, four-term energy, diagnostic vector, temporal transport. **NEW:** Full-page pipeline diagram with annotations. |
| 1.6 | Historical Context and Intellectual Debts | 4 | Gestalt psychology, topological perception, Merleau-Ponty's figure/ground, Allen-Cahn/phase-field, optimal transport. **NEW:** Expanded treatment with illustrated timeline. |
| 1.7 | Discussion Questions and Exercises | 2 | **NEW:** 5-7 conceptual questions + 2-3 computational exercises (plot a field, compare frameworks). |

**Pages: ~27. Figures: 8** (1.1: graded field vs. crisp set; 1.2: five framework comparison; 1.3: five desiderata illustrated; 1.4: three field examples on 10×10 grid; 1.5: theory pipeline (full page); 1.6: historical timeline; 1.7-1.8: additional field visualization examples).
**Spec connection:** §2 Foundational Orientation, §4 Why the Soft Form Is Primary.

---

### Chapter 2: The Ontology of Softness
**Learning objectives:** Internalize why the soft system is primary (not an approximation); understand the role of X_t as substrate vs. emergent structure; grasp the four structural requirements through rich examples.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 2.1 | Soft Primacy: Not a Relaxation | 4 | Five structural arguments for soft primacy (graded cohesion, blurred inside/outside, emergent closure, field-relative distinction, crisp recoverability). Each argument with a figure. |
| 2.2 | The Relational Support Space X_t | 3 | X_t as domain of relational loci, not pre-given objects. The pixel-grid analogy. Varying X_t through time. **NEW:** Three examples of X_t (grid, social network, abstract graph). |
| 2.3 | Four Structural Requirements — Binding | 4 | **NEW (expanded from 2.3):** Dedicated treatment of Binding/self-support. Intuitive examples. What binding looks like on 5×5, 10×10 grids. Three visualization examples. |
| 2.4 | Four Structural Requirements — Separation | 4 | **NEW:** Dedicated treatment of Separation/distinction. Interior vs. exterior asymmetry. Three visualization examples showing high/medium/low Sep. |
| 2.5 | Four Structural Requirements — Articulation | 4 | **NEW:** Dedicated treatment of Inside/morphological quality. Core-boundary-exterior stratification. Persistence diagrams explained visually. |
| 2.6 | Four Structural Requirements — Persistence | 4 | **NEW:** Dedicated treatment of temporal persistence. Two-frame examples. Core inheritance visualized. Genidentity concept introduced. |
| 2.7 | From Formation to Object | 3 | Objects as distinguished outputs: formations where all four requirements are robustly satisfied. Thresholding as secondary projection. **NEW:** The diagnostic vector as a "quality space" with 3D projection figure. |
| 2.8 | What the Theory Does Not Claim | 2 | Honest scope limitations: not a theory of consciousness, not a neural model, not a replacement for all segmentation. The discrete substrate caveat. |
| 2.9 | Discussion Questions and Exercises | 2 | **NEW:** 5-7 questions + 2-3 exercises (compute Bind for a given field, sketch boundary bands). |

**Pages: ~30. Figures: 14** (2.1-2.2: soft primacy arguments; 2.3: X_t examples (3 types); 2.4-2.6: Bind examples (high/medium/low); 2.7-2.9: Sep examples; 2.10-2.12: Inside/Q_morph examples with persistence diagram; 2.13: Persist two-frame example; 2.14: diagnostic vector 3D projection).
**Spec connection:** §2, §4, §5 Derived Geometric Notions, §7.1 Component Predicates.

---

### Chapter 3: The Formal Universe
**Learning objectives:** Know every component of C^soft; distinguish primitives from derived notions; understand the operator catalogue and its rationale.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 3.1 | Design Principles for the Formal Universe | 2 | Minimal primitivity, functional justification, layer separation. Why these three principles matter. |
| 3.2 | The Formal Universe Tuple | 5 | C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, D_t}, {M_{t→s}}). Each component with intuition + formal definition. Component summary table. **NEW:** Extended 5×5 grid worked example showing all components computed. |
| 3.3 | Primitives vs. Derived Notions | 3 | Clear registry: what is primitive (u_t, Cl_t, N_t, D_t, M_{t→s}) vs. derived (Core_t, Bd_t, C_t, g_t, Q_morph). Full registry table. Why this distinction matters (ontological, economic, traceable). |
| 3.4 | The Operator Triad | 4 | Self-completion (Cl_t), Self-contrast (D_t vs. 1-u), Self-integration (C_t as diagnostic). Why three, not two or four. Variational vs. diagnostic distinction. **NEW:** Worked computation showing all three operators on a bump field. |
| 3.5 | Temporal Transport: Identity Without Tracking | 4 | M_{t→s} as structural inheritance kernel. Sub-stochastic, non-injective, core-preserving. Genidentity vs. tracking IDs. **NEW:** Extended three-frame temporal example showing formation migration. |
| 3.6 | Derived Geometric Notions | 3 | Core, Interior, Boundary Band, Exterior. Threshold-based definitions. The gradient indicator g_t. Boundary as transition region, not codimension-one surface. Q_morph definition. |
| 3.7 | What Was Removed and Why | 3 | T_t demotion (v2.0): zero realizations, zero theorems. C_t demotion to diagnostic (v2.1): Sep correction removed its only predicate role. **NEW:** Detailed functional-role table for each removed operator. Lessons for theory design. |
| 3.8 | Discussion Questions and Exercises | 2 | **NEW:** 5-7 questions + 2-3 exercises (construct formal universe for a given graph, compute derived notions). |

**Pages: ~26. Figures: 6** (3.1: formal universe diagram (full page); 3.2: operator triad relationships; 3.3: temporal transport 3-frame schematic; 3.4: 5×5 grid worked example — all components; 3.5: derived geometric notions on a formation; 3.6: removed operators timeline).
**Spec connection:** §3 (all subsections), §5.
**NOTE:** ch03_formal_universe.tex (565 lines) already written — expand by ~6pp with additional examples and exercises.

---

**Part I total: ~83 pages, 30 figures**

---

## Part II: The Formal Theory (Chapters 4-8, ~160pp)

### Chapter 4: Axiomatic Groups
**Learning objectives:** State and interpret all axioms (Groups A-E); understand the design choices (non-idempotent closure, conditional extensivity, sub-stochastic transport); distinguish axioms from realizations.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 4.1 | Design Philosophy: Axioms vs. Realizations | 3 | The layer separation principle. Axioms constrain; realizations instantiate. Multiple realizations may satisfy the same axioms. **NEW:** Analogy with group axioms and concrete groups. |
| 4.2 | Group A: Soft Closure | 8 | A1' (conditional extensivity + proof for sigmoid), A2 (monotonicity), A3 (stabilization/contraction, a_cl < 4 sharp bound), A4 (continuity). The non-idempotence commitment and its mathematical payoff. Two-landscape structure. **NEW:** 3-frame closure convergence visualization. Detailed proof of A1' compatibility. Numerical demonstration of contraction rate. |
| 4.3 | Group B: Soft Adjacency | 3 | B1-B4 (nonnegativity, symmetry, locality, non-transitivity). Why non-transitivity is essential. **NEW:** Counter-example showing failure of transitivity in co-belonging. |
| 4.4 | Group C: Soft Co-Belonging | 4 | C1-C4 (dependence, distinction from adjacency, local monotonicity C3'', symmetry). Current diagnostic status. Resolvent realization. **NEW:** C3'' proof via Schur complement with worked example. |
| 4.5 | Group D: Distinction | 4 | D-Ax1 (exterior sensitivity), D-Ax2 (asymmetry), D-Ax3 (boundary sensitivity, b_D = 0). Why analyticity forces b_D = 0. **NEW:** Comparison of b_D = 0 vs. b_D > 0 on formation quality. |
| 4.6 | Group E: Temporal Transport | 4 | E1 (sub-stochasticity), E2 (non-injectivity), E3 (core inheritance as solution constraint), E4 (structural sensitivity). The self-referential transport problem. **NEW:** Visual comparison of stochastic vs. sub-stochastic transport. |
| 4.7 | Axiom Consistency (T20) | 3 | Parameter admissibility: existence of parameter regimes satisfying all axioms simultaneously. **NEW:** Full proof with parameter space visualization. |
| 4.8 | Axiom Interaction and Independence | 3 | **NEW:** How axioms interact. Which axioms constrain which operators. Independence analysis. Axiom dependency DAG. |
| 4.9 | Discussion Questions and Exercises | 2 | **NEW:** Verify axioms for alternative operators. Design a toy closure satisfying A1'-A4. |

**Pages: ~34. Figures: 7** (4.1: closure iteration convergence (3 frames); 4.2: sigmoid function and fixed points; 4.3: non-transitivity example; 4.4: b_D comparison; 4.5: stochastic vs. sub-stochastic transport; 4.6: axiom dependency graph (full page); 4.7: parameter admissibility region).
**Spec connection:** §6 (all groups), §13 T20.
**Key theorems: T20 (Axiom Consistency), A2 (Monotonicity), A3 (Contraction).**

---

### Chapter 5: Provisional Operator Realizations
**Learning objectives:** Understand the concrete mathematical forms of each operator; verify that realizations satisfy their axioms; compute operators on small examples.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 5.1 | Closure: The Sigmoid Form | 6 | Cl(u)(x) = σ(a_cl · (P_t u(x) - τ_cl)). Row-normalized aggregation P_t. Contraction rate a_cl/4. Fixed-point computation. **NEW:** Extended worked example on 5×5 and 10×10 grids. Comparison of a_cl values. Visualization of Cl(u) for different a_cl. |
| 5.2 | Distinction: Aggregated Exterior Asymmetry | 4 | D(x; 1-u) = \|P(u)(x) - P(1-u)(x)\|. The b_D = 0 choice. Self-referential structure. **NEW:** Side-by-side visualization of u, 1-u, P(u), P(1-u), and D. |
| 5.3 | Co-Belonging: The Resolvent | 5 | C_t = (I - αW_sym)^{-1}. Neumann series convergence. Spectral radius condition. 3+ orders of magnitude discrimination. Why Cesaro averaging fails. **NEW:** Heatmap comparison of resolvent vs. Cesaro. Discrimination factor visualization. |
| 5.4 | Transport: Cohesion Fingerprint and Self-Referential OT | 6 | 3-component fingerprint φ(x) = (u, Cl(u), D(x;1-u)). Squared-distance cost. Entropy-regularized partial OT (Sinkhorn). Fixed-point iteration for self-referential cost. **NEW:** Fingerprint component visualization. Sinkhorn convergence plot. Transport plan heatmap. |
| 5.5 | Jacobians and Differentiability | 4 | Exact Jacobian-transpose-vector products for each operator. Chain rule through sigmoid. Why analyticity matters for convergence theory. **NEW:** Finite difference verification plot. Jacobian sparsity pattern visualization. |
| 5.6 | Alternative Realizations and Robustness | 3 | **NEW:** What happens with different sigmoid steepness? ReLU-based closure? How robust are the results? Sensitivity analysis. |
| 5.7 | Discussion Questions and Exercises | 2 | **NEW:** Implement operators from scratch. Verify axiom satisfaction numerically. |

**Pages: ~30. Figures: 8** (5.1: sigmoid closure for different a_cl; 5.2: 10×10 worked example (u, Cl(u), D); 5.3: resolvent vs. Cesaro heatmaps; 5.4: fingerprint components visualization; 5.5: Sinkhorn convergence; 5.6: transport plan heatmap; 5.7: FD gradient verification; 5.8: Jacobian sparsity pattern).
**Spec connection:** §9 Provisional Realizations, §10 Transport.

---

### Chapter 6: The Energy Functional
**Learning objectives:** Derive each energy term from structural requirements; compute gradients; understand the volume constraint; prove existence of minimizers.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 6.1 | The Volume Constraint | 4 | Σ_m = {u ∈ [0,1]^n : Σu = m}. Ontological justification: finite cohesive capacity forces selectivity. Admissible range for c. **NEW:** Geometric visualization of Σ_m as simplex cross-section. What happens without the constraint. |
| 6.2 | Closure Energy E_cl | 5 | \|\|u - Cl(u)\|\|^2. Penalizes deviation from self-support. Gradient: 2(I - J_Cl)^T(u - Cl(u)). Hessian positive-definiteness from non-idempotence. **NEW:** E_cl landscape on 2D projection. Gradient field visualization. |
| 6.3 | Separation Energy E_sep | 5 | Σ u(x)(1 - D(x;1-u)). Self-referential penalty. The exact identity Sep = 1 - E_sep/m (complete proof). Gradient derivation. **NEW:** E_sep as function of formation quality. Self-referential loop visualization. |
| 6.4 | Boundary/Morphology Energy E_bd | 6 | Smoothness: 2α u^T L u (ordered pairs → factor 4 gradient). Double-well: β Σ u^2(1-u)^2. W'(u) = 2u(1-u)(1-2u). Allen-Cahn connection. Hessian: 4αL + βW''(u). **NEW:** Double-well curve. Smoothness vs. double-well balance visualization. Effect of α/β ratio. |
| 6.5 | Transport Energy E_tr | 3 | Wasserstein-based temporal cost. Coupling to within-time energy. **NEW:** Transport cost matrix visualization. |
| 6.6 | The Full Energy and Its Landscape | 5 | E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd + λ_tr E_tr. Four-term independence principle. Parameter sensitivity. **NEW:** Full energy landscape cross-sections for different λ ratios. 3D energy surface. Side-by-side: each term's contribution at a formation. |
| 6.7 | Existence of Minimizers (T1) | 4 | Compactness of Σ_m. Continuity of E. Weierstrass extreme value theorem. **NEW:** Complete proof with all details. |
| 6.8 | The Predicate-Energy Bridge | 4 | **NEW (promoted from Ch.8):** Sep = 1 - E_sep/m (exact). Bind ≥ 1 - √(E_cl/n) (Cauchy-Schwarz). Reverse bounds at minimizers. Full proofs. Visual demonstration. |
| 6.9 | Discussion Questions and Exercises | 2 | **NEW:** Compute energy for given fields. Verify gradient formulas. Plot energy landscapes. |

**Pages: ~38. Figures: 10** (6.1: volume constraint geometry (Σ_m); 6.2: E_cl landscape; 6.3: E_sep self-referential loop; 6.4: double-well W(u); 6.5: smoothness vs. double-well balance; 6.6: transport cost matrix; 6.7: full energy landscape (3D); 6.8: four terms side-by-side at formation; 6.9: predicate-energy correspondence; 6.10: λ-ratio sensitivity).
**Spec connection:** §8 (all subsections).
**Key theorems: T1 (Existence), Predicate-Energy Bridge.**

---

### Chapter 7: Phase Transition and Formation Birth
**Learning objectives:** Derive the critical parameter β_crit; prove formation birth via bifurcation; understand spectral universality; connect to Allen-Cahn theory.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 7.1 | The Uniform State and Its Stability | 4 | u ≡ c as trivial minimizer. Hessian at uniform state. Linear stability analysis. **NEW:** Eigenvalue spectrum visualization. Instability onset animation (3 frames). |
| 7.2 | Phase Transition (T8-Core) | 6 | Critical ratio β/α > 4λ₂/\|W''(c)\|. Spinodal range. Fiedler eigenvalue. Mountain pass existence of non-trivial minimizer. **NEW:** Complete proof. Phase diagram in (α, β) space. |
| 7.3 | Supercritical Pitchfork Bifurcation (T-Birth-Parametric) | 6 | Crandall-Rabinowitz theorem. Cubic coefficient A > 0. Square-root scaling of amplitude. D₄ symmetry on square grids. **NEW:** Bifurcation diagram with numerical data overlay. Amplitude scaling verification. |
| 7.4 | Spectral Universality (FORMATION-BIRTH General) | 5 | Courant-Rayleigh variational principle. λ₂ as sole topological factor. 32-graph empirical validation (R² = 0.9924). **NEW:** Full proof via Courant-Rayleigh. Gallery of diverse graphs with their Fiedler eigenvectors and formation shapes. |
| 7.5 | The Full Energy Perturbation (T8-Full) | 4 | IFT on bordered KKT. Smooth family of perturbed minimizers. Non-degeneracy at E_bd minimizer. **NEW:** Perturbation path visualization. |
| 7.6 | Stability and Metastability (T7-Enhanced) | 4 | Closure-enhanced Hessian eigenvalues. Deeper attraction basins. Comparison with pure Allen-Cahn. **NEW:** Side-by-side SCC vs. Allen-Cahn basin visualization. |
| 7.7 | Geometric Intuition for Phase Transitions | 3 | **NEW:** Why phase transitions happen — geometric and physical intuition. The "competition" between smoothness and phase separation. Analogy with soap films. |
| 7.8 | Discussion Questions and Exercises | 2 | **NEW:** Compute β_crit for different graphs. Verify spectral universality numerically. |

**Pages: ~34. Figures: 8** (7.1: eigenvalue spectrum at uniform state; 7.2: phase diagram in (α,β) space; 7.3: bifurcation diagram with data; 7.4: spectral universality scatter (32 graphs); 7.5: Fiedler eigenvector gallery (6 diverse graphs); 7.6: SCC vs. Allen-Cahn basin comparison; 7.7: perturbation path; 7.8: geometric intuition for phase separation).
**Spec connection:** §8.6, §13 (T8-Core, T8-Full, T-Birth-Parametric, T7-Enhanced, FORMATION-BIRTH).
**Key theorems: T8-Core, T8-Full, T-Birth-Parametric, FORMATION-BIRTH, T7-Enhanced.**

---

### Chapter 8: Convergence, Stability, and Limits
**Learning objectives:** Prove gradient flow convergence; understand the Łojasiewicz framework; derive the sharp-interface Γ-convergence limit; quantify the non-idempotence stability advantage.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 8.1 | Gradient Flow on Σ_m | 4 | Projected gradient descent. Semi-implicit scheme. Projection onto tangent space and box constraints. **NEW:** Gradient flow trajectory visualization on energy landscape. |
| 8.2 | Łojasiewicz Convergence (T14) | 5 | Analytic energy on compact domain. Łojasiewicz-Simon inequality. Exponential convergence rate. Why b_D = 0 is required. **NEW:** Complete proof. Convergence rate comparison plot. |
| 8.3 | The Non-Idempotence Advantage (T3/T6-Stability) | 4 | Gram matrix analysis. n/n positive eigenvalues (contraction) vs. ≤(n-k)/n (idempotent). Quantified stability gap. **NEW:** Eigenvalue spectrum comparison figure. |
| 8.4 | Sharp-Interface Γ-Convergence (T11) | 5 | α/β → 0 limit. Modica-Mortola on graphs. Convergence to perimeter functional. Modified surface tension from self-referential terms. **NEW:** Sequence of formations as α/β → 0. Comparison with classical Modica-Mortola. |
| 8.5 | Deep Core Dominance | 3 | **NEW (promoted from brief mention):** Deep Core Dominance 2b. Isoperimetric inequality on Z^d. Core structure guarantees. |
| 8.6 | Discussion Questions and Exercises | 2 | **NEW:** Implement gradient flow. Verify convergence rate. Plot Γ-convergence sequence. |

**Pages: ~23. Figures: 5** (8.1: gradient flow on energy landscape; 8.2: convergence rate comparison; 8.3: eigenvalue spectrum (idempotent vs. non-idempotent); 8.4: sharp-interface limit sequence (4 panels); 8.5: deep core dominance visualization).
**Spec connection:** §8, §13 (T14, T3/T6-Stability, T11, Deep Core Dominance 2b).
**Key theorems: T14, T3/T6-Stability, T11, Deep Core Dominance 2b.**

---

**Part II total: ~159 pages, 38 figures**

---

## Part III: Multi-Formation and Temporal Theory (Chapters 9-11, ~100pp)

### Chapter 9: Multi-Formation Theory
**Learning objectives:** Understand the K-field architecture; derive inter-formation coupling; classify regimes by Λ_coupling; prove multi-formation metastability.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 9.1 | Why Multi-Formation Is Hard | 4 | Single-field contraction → unique fixed point. The need for K coupled fields. Four architecture options (Peeling, K-Field, Spectral C_t, Localization) and why K-Field was selected. **NEW:** Visual comparison of all four architectures. |
| 9.2 | K-Field Architecture | 5 | Product manifold Σ^K_M. Simplex participation constraint. Inter-field repulsion. Per-formation operators. **NEW:** K=2 worked example with full computation. |
| 9.3 | The Coupling Bound Lemma | 5 | Joint Hessian structure. Weyl bound. Spectral-repulsion compatibility (SR). Exponential gradient decay at core sites. Cross-term vanishing. **NEW:** Full proof with all six parts. |
| 9.4 | Regime Classification via Λ_coupling | 4 | Λ = λ_rep · ω_jk / min(μ_j, μ_k). Well-separated (Λ < 0.01), weakly-interacting (0.01 < Λ < 1/(K-1)), strongly-interacting (Λ > 1/(K-1)). **NEW:** Phase diagram with experimental overlay. |
| 9.5 | Multi-Formation Is Kinetic, Not Thermodynamic | 5 | K*=1 universally on connected graphs. K>1 as metastable local minima. Three kinetic pillars: nucleation, metastability, coarsening. Barrier height ∝ β^{0.89}. **NEW:** Energy barrier visualization. Merge dynamics sequence (5 frames). |
| 9.6 | The T-Beyond-Weyl Spectral Bound | 4 | Soft-mode localization. Boundary-Mode Dominance. 33× improvement over Weyl. Extended coexistence window. **NEW:** Spectral bound comparison with numerical validation. |
| 9.7 | Critical Inter-Formation Distance (T-d_min-Formula) | 3 | Empirical formula. Closure reduces d_min* by ~30%. CN14: closure expands multi-formation stability. **NEW:** d_min* curve with/without closure. |
| 9.8 | Discussion Questions and Exercises | 2 | **NEW:** Compute K-field energy. Classify regimes for given configurations. |

**Pages: ~32. Figures: 10** (9.1: four architecture comparison; 9.2: K-field schematic (full page); 9.3: K=2 worked example; 9.4: regime phase diagram with data; 9.5: energy barrier visualization; 9.6: merge dynamics sequence (5 frames); 9.7: barrier height scaling plot; 9.8: spectral bound comparison; 9.9: d_min* with/without closure; 9.10: multi-formation gallery on diverse graphs).
**Spec connection:** §12, §13 (T-Merge, T-Beyond-Weyl, T-d_min-Formula, T-Persist-K-Unified).
**Key theorems: Coupling Bound Lemma, T-Merge, T-Beyond-Weyl, T-d_min-Formula, T-Persist-K-Unified.**

---

### Chapter 10: Temporal Transport and Persistence
**Learning objectives:** Construct the self-referential transport kernel; prove fixed-point existence; derive T-Persist-1; understand the core-overlap and transport-based persistence implementations.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 10.1 | The Problem of Temporal Identity | 4 | Identity without tracking IDs. Genidentity. Why spatial proximity is insufficient. The structural inheritance requirement. **NEW:** Three scenarios where tracking fails but SCC succeeds (split, merge, deform). |
| 10.2 | Cohesion Fingerprint and Self-Referential Cost | 4 | 3-component fingerprint φ = (u, Cl(u), D(x;1-u)). Why resolvent C(x,x) was demoted (<0.4% contribution, Jacobian norm ~9300). Squared-distance cost construction. **NEW:** Fingerprint component visualization. Cost matrix heatmap. |
| 10.3 | Entropy-Regularized Partial Optimal Transport | 5 | Log-domain Sinkhorn algorithm. Sub-stochastic coupling. Partial mass transport. Convergence guarantees. **NEW:** Step-by-step Sinkhorn iteration visualization. Algorithm pseudocode. |
| 10.4 | Self-Referential Fixed Point | 4 | Schauder fixed-point existence. Transport confinement bound. Uniqueness via contraction. Banach iteration in practice. **NEW:** Fixed-point iteration convergence plot. |
| 10.5 | T-Persist-1: Single-Formation Persistence | 5 | Five conditions (a-e). Core inheritance under gentle transport. Two-tier concentration (deep core >99.99%, shallow >99.3%). **NEW:** Complete proof of conditions (a) and (c). Transport plan at formation. |
| 10.6 | Multi-Formation Persistence | 4 | T-Persist-K-Sep (well-separated), T-Persist-K-Weak (weakly-interacting). T-Persist-K-Unified (parametric). Per-formation transport plans. Simplex constraint in temporal domain. **NEW:** K=2 temporal transport visualization. |
| 10.7 | Temporal Evolution Sequences | 4 | **NEW:** Extended examples showing formation evolution over 5-10 time steps. Migration, deformation, persistence maintenance. Full temporal sequence visualization. |
| 10.8 | Discussion Questions and Exercises | 2 | **NEW:** Implement Sinkhorn. Compute transport plans. Verify persistence conditions. |

**Pages: ~32. Figures: 8** (10.1: three failure scenarios for tracking; 10.2: fingerprint components; 10.3: Sinkhorn iteration visualization; 10.4: transport plan heatmap; 10.5: fixed-point convergence; 10.6: core-to-core inheritance; 10.7: K=2 temporal transport; 10.8: temporal evolution sequence (5 frames)).
**Spec connection:** §3.8, §6 Group E, §7.1 Persist, §10, §12.
**Key theorems: T-Persist-1, T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified.**

---

### Chapter 11: Proto-Cohesion and the Diagnostic Vector
**Learning objectives:** Compute all four diagnostic components; interpret the diagnostic vector geometrically; understand the proto-cohesion existence theorem; evaluate predictions P1-P5.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 11.1 | The Diagnostic Vector d ∈ [0,1]^4 | 4 | (Bind, Sep, Inside, Persist). Graded assessment vs. Boolean conjunction. Why four dimensions, not three or five. **NEW:** Diagnostic vector "radar chart" for different field types. |
| 11.2 | Bind: Self-Support Under Closure | 4 | l^2 norm, not l^inf. Why boundary sites prevent l^inf from working. T-Bind-Proj and T-Bind-Full. General τ via binary mass-balance formula. **NEW:** Bind as function of a_cl and τ. Complete proof of T-Bind-Proj. |
| 11.3 | Sep: Distinction from Exterior | 4 | u-weighted average. The exact identity Sep = 1 - E_sep/m. Why C_t-weighting gives ~0.5 always. **NEW:** Sep comparison (u-weighted vs. C_t-weighted) with visualization. |
| 11.4 | Inside: Morphological Quality | 5 | Q_morph = (l_max - c)/(1-c) · Artic. H0 persistence. Superlevel-set filtration. QM1-QM4 axiom satisfaction. **NEW:** Step-by-step persistence diagram construction. QM axiom verification on examples. |
| 11.5 | Persist: Temporal Inheritance | 3 | Two implementations: core-overlap approximation vs. transport-based. When to use which. **NEW:** Side-by-side comparison on same formation. |
| 11.6 | The Proto-Cohesion Existence Theorem | 4 | Non-trivial minimizer satisfies proto-cohesion. Assembly from T1 + T8-Core + predicate bounds. **NEW:** Complete proof assembly with all intermediate steps. |
| 11.7 | Five Verified Predictions | 5 | P1 (contraction), P2 (independence), P3 (enhanced dwell, p=0.037), P4 (path dependence), P5 (Sep-before-Inside ordering). **NEW:** Each prediction with figure showing experimental verification. |
| 11.8 | Discussion Questions and Exercises | 2 | **NEW:** Compute diagnostic vector for given fields. Verify predictions numerically. |

**Pages: ~31. Figures: 10** (11.1: diagnostic vector radar charts (3 types); 11.2: Bind as function of parameters; 11.3: Sep comparison (u-weighted vs. C_t-weighted); 11.4: persistence diagram construction (step-by-step); 11.5: QM axiom verification; 11.6: core-overlap vs. transport-based Persist; 11.7-11.11: five prediction verification plots (one per prediction)).
**Spec connection:** §7 (all), §13 predictions.
**Key theorems: T-Bind-Proj/Full, QM1-4, Proto-Cohesion Existence.**

---

**Part III total: ~95 pages, 28 figures**

---

## Part IV: Implementation and Applications (Chapters 12-15, ~140pp)

### Chapter 12: Algorithms and the Python Implementation
**Learning objectives:** Implement the full SCC pipeline from scratch; understand projected gradient descent on Σ_m; verify gradients numerically; run the optimizer.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 12.1 | The Pipeline: Graph → Operators → Energy → Optimizer | 4 | Architecture overview. Module responsibilities. Data flow diagram. **NEW:** Full-page module dependency diagram with code sizes. |
| 12.2 | Graph Representation and Laplacian | 4 | Sparse adjacency. Graph Laplacian. Fiedler eigenvalue computation. Row-normalized P. Cohesion-weighted W_sym. Code: `graph.py`. **NEW:** Code walkthrough with annotated snippets. |
| 12.3 | Operator Implementation | 5 | Closure (sigmoid + aggregation), Distinction (aggregated exterior), Resolvent (Neumann series). Exact JVPs for gradient computation. Code: `operators.py`. **NEW:** Annotated code for each operator. |
| 12.4 | Energy Computation and Exact Gradients | 5 | E_cl, E_sep, E_bd with analytic gradients. FD verification to 1e-9. Critical details: ordered-pair factor 4, double-well factor 2. Code: `energy.py`. **NEW:** Gradient verification methodology explained. |
| 12.5 | Optimization on Σ_m | 5 | Semi-implicit projected gradient descent. BB step size. Simplex projection. Multi-start strategy. Convergence criteria. Code: `optimizer.py`. **NEW:** Optimization trajectory visualization. |
| 12.6 | Diagnostics and Persistence | 4 | DiagnosticVector computation. Core-overlap Persist. Transport-based Persist. Code: `diagnostics.py`, `transport.py`. |
| 12.7 | Multi-Formation Pipeline | 4 | K-field optimization. Inter-formation repulsion. Regime classification. Transport for K formations. Code: `multi.py`. |
| 12.8 | Running Your First Formation | 3 | **NEW:** Complete tutorial: from `pip install` to formation visualization. Smoke test. Interpreting output. |
| 12.9 | Discussion Questions and Exercises | 2 | **NEW:** Implement a minimal SCC from scratch. Add a new energy term. |

**Pages: ~36. Figures: 4** (12.1: module dependency graph (full page); 12.2: gradient verification plot; 12.3: optimization trajectory; 12.4: first formation tutorial output).
**Spec connection:** Implementation of all spec sections. Code: `scc/` package.

---

### Chapter 13: Experiments and Numerical Verification
**Learning objectives:** Reproduce key theoretical predictions computationally; interpret experimental results; understand parameter sensitivity and scaling behavior.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 13.1 | Experiment Design Philosophy | 3 | Theory-first experiments. Each experiment tests a specific theorem or prediction. **NEW:** Experiment-theorem mapping table. |
| 13.2 | Parameter Sweeps (exp1, exp5) | 5 | λ-ratio sensitivity. Phase transition location. Hessian normalization. **NEW:** Multiple sweep plots. Sensitivity analysis. |
| 13.3 | Phase Transition Verification (exp2, exp37, exp39) | 6 | β_crit prediction. Bifurcation crossing (zero hysteresis). Topological birth. **NEW:** Three experiments each with detailed figure. Hysteresis test. |
| 13.4 | Allen-Cahn Comparison (exp7) | 4 | SCC vs. pure Allen-Cahn: metastability enhancement, convergence speed, formation quality. **NEW:** Side-by-side comparison figures. Energy curve overlay. |
| 13.5 | Transport and Persistence (exp9-11, exp26-28) | 6 | Transport concentration. Chain verification. Stress tests. **NEW:** Concentration plots. Chain success rate. Failure mode analysis. |
| 13.6 | Multi-Formation Experiments (exp6, exp30, exp38, exp55) | 6 | Merge flow. Barrier height. Stochastic coarsening. Regime classification. **NEW:** Merge dynamics sequence. Barrier scaling. Coarsening time series. |
| 13.7 | Scaling and Large Grids (exp42-43) | 4 | 50×50 scale verification. Computational cost analysis. **NEW:** Large-grid formation gallery. Scaling law plots. |
| 13.8 | Prediction Verification (exp15, exp58) | 5 | The five predictions. Bind-τ sweep. General-τ mass-balance validation. **NEW:** Each prediction with dedicated figure. R² validation. |
| 13.9 | Advanced Experiments (exp46-57) | 5 | **NEW:** Regime sweep, unified predictions, K-selection, closure threshold, nucleation. Summary of all 58 experiments. |
| 13.10 | Discussion Questions and Exercises | 2 | **NEW:** Design your own experiment. Reproduce a specific result. |

**Pages: ~46. Figures: 18** (13.1-13.3: parameter sweep results; 13.4-13.6: phase transition (3 experiments); 13.7-13.8: Allen-Cahn comparison; 13.9-13.11: transport & persistence; 13.12-13.14: multi-formation dynamics; 13.15-13.16: scaling and large grids; 13.17-13.18: prediction verification).
**Spec connection:** §13 proved results, predictions P1-P5. Code: `experiments/`.

---

### Chapter 14: Connections and Applications
**Learning objectives:** Map SCC to Gestalt principles; compare with predictive processing, IIT, and active inference; identify testable empirical predictions; understand application domains.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 14.1 | SCC and Gestalt Psychology | 6 | Proximity → adjacency, Similarity → cohesion-weighted transport, Closure → Cl_t, Good continuation → boundary smoothness, Common fate → temporal transport. Formal Gestalt mapping table. **NEW:** Extended mapping with 5+ Gestalt principles. Visual demonstration of each correspondence. |
| 14.2 | Comparison with Predictive Processing | 4 | Both emphasize top-down influence. SCC's self-referential energy vs. prediction error. Convergences and divergences. **NEW:** Detailed side-by-side analysis. |
| 14.3 | Comparison with IIT, Bayesian Brain, Active Inference | 5 | Φ vs. diagnostic vector. Prior/posterior vs. energy minimum. Free energy vs. SCC energy. **NEW:** Comprehensive framework comparison matrix (table + figure). |
| 14.4 | Ten Empirical Predictions | 6 | Testable predictions for psychophysics, neuroimaging, and development. Testability ratings. **NEW:** Each prediction with proposed experimental protocol. |
| 14.5 | Applications: Computer Vision | 4 | Soft segmentation. Self-referential graph neural networks. Beyond standard GNN message passing. **NEW:** Worked example with synthetic image. |
| 14.6 | Applications: Cognitive Modeling | 4 | Object permanence. Figure-ground segregation. Attentional grouping. **NEW:** SCC model of visual search. |
| 14.7 | Applications: Signal Processing and Neuroscience | 4 | **NEW:** Speech segmentation. EEG/fMRI coherence. Neural population analysis. |
| 14.8 | Open Problems and Future Directions | 4 | Continuum limit. Stochastic extensions. Learning parameters from data. Neural implementation. **NEW:** Research roadmap with prioritized problems. |
| 14.9 | Discussion Questions and Exercises | 2 | **NEW:** Design an application. Map a new cognitive phenomenon to SCC. |

**Pages: ~39. Figures: 8** (14.1: Gestalt mapping diagram (full page); 14.2: framework comparison matrix; 14.3: SCC vs. PP vs. IIT schematic; 14.4: prediction experimental protocols; 14.5: synthetic image segmentation example; 14.6: visual search model; 14.7: speech segmentation example; 14.8: research roadmap).
**Spec connection:** §11 Commitment Notes, §12 Open Problems, I4/I10 extensions.

---

### Chapter 15: The Complete Theorem Registry
**Learning objectives:** Reference all 48 Category A theorems; understand interdependencies; appreciate the completeness of the theory.

| Section | Title | Pages | Content |
|---------|-------|-------|---------|
| 15.1 | Theorem Dependency Graph | 3 | Visual map of which theorems depend on which. **NEW:** Full-page DAG with color-coded categories. |
| 15.2 | Single-Formation Theorems (24) | 5 | Complete statements and proof sketches for T1, T8-Core, T8-Full, T14, T3/T6-Stability, T7-Enhanced, T11, T20, A2, A3, C-Axioms, QM1-4, etc. |
| 15.3 | Predicate and Bridge Theorems (8) | 4 | Predicate-Energy Bridge, T-Bind-Proj/Full, Deep Core Dominance 2b, Sep identity, Bind bound. |
| 15.4 | Multi-Formation Theorems (8) | 4 | T-Merge, T-Birth-Parametric, FORMATION-BIRTH, T-Beyond-Weyl, T-d_min-Formula, T-Persist-K-Unified. |
| 15.5 | Persistence Theorems (8) | 4 | T-Persist-1, T-Persist-K-Sep, T-Persist-K-Weak, transport fixed-point, confinement. |
| 15.6 | Theory Completeness: From 0 to 48 | 3 | **NEW:** The journey from 0 theorems (I1) to 48 Cat A (Phase 14). Score trajectory. What "100% complete" means and doesn't mean. |

**Pages: ~23. Figures: 2** (15.1: theorem dependency DAG (full page, color-coded); 15.2: completeness trajectory chart).
**Spec connection:** §13 (complete registry).

---

**Part IV total: ~144 pages, 32 figures**

---

## Back Matter

### Appendix A: Mathematical Background (20 pages)
- A.1: Graph Theory (Laplacian, Fiedler eigenvalue, spectral gap) — 5pp, 2 figures
- A.2: Variational Methods (Euler-Lagrange, constrained optimization, KKT conditions) — 4pp
- A.3: Optimal Transport (Kantorovich duality, Sinkhorn algorithm, partial OT) — 4pp, 1 figure
- A.4: Bifurcation Theory (Crandall-Rabinowitz, pitchfork, Lyapunov-Schmidt) — 4pp
- A.5: Γ-Convergence (definition, compactness, equi-coercivity) — 3pp
- **NEW:** Each section with worked examples and key intuitions

### Appendix B: Parameter Registry (6 pages)
- Complete parameter table with constraints, default values, and sensitivity notes
- Parameter admissibility regions — 1 figure
- Recommended settings for different graph scales
- **NEW:** Parameter tuning guide for practitioners

### Appendix C: Commitment Notes and Design Decisions (8 pages)
- All 14+ Commitment Notes from the spec, with expanded commentary
- Why each major design choice was made (non-idempotence, b_D=0, u-weighted Sep, etc.)
- **NEW:** Decision tree figure for key design choices

### Appendix D: Development History (6 pages)
- Summary of the 12-iteration development process
- Key discoveries and corrections at each stage
- The vulnerability audit and its resolution
- **NEW:** Iteration score trajectory figure

### Glossary (4 pages)
- **NEW:** Complete glossary of technical terms (Korean + English)

### Bibliography (8 pages)
- ~120-150 references across mathematics, cognitive science, ML, philosophy
- **NEW:** Annotated bibliography for key references

### Index (6 pages)
- **NEW:** Expanded dual-language index (Korean + English terms)

**Back matter total: ~58 pages, 5 figures**

---

## Page Budget Summary (600pp Edition)

| Part | Chapters | Pages | Figures | Tables |
|------|----------|-------|---------|--------|
| Front Matter | — | 21 | 2 | 1 |
| **Part I: Foundations** | 1-3 | 83 | 30 | 3 |
| **Part II: Formal Theory** | 4-8 | 159 | 38 | 6 |
| **Part III: Multi-Formation & Temporal** | 9-11 | 95 | 28 | 4 |
| **Part IV: Implementation & Applications** | 12-15 | 144 | 32 | 8 |
| Back Matter | App. A-D, Glossary, Bib, Index | 58 | 5 | 6 |
| **TOTAL** | **15 chapters + 4 appendices** | **~616 pages** | **~90 figures** | **~28 tables** |

### Comparison with Previous Edition

| Part | Previous | Expanded | Increase |
|------|----------|----------|----------|
| Front Matter | 13pp | 21pp | +62% |
| Part I | 47pp | 83pp | +77% |
| Part II | 95pp | 159pp | +67% |
| Part III | 61pp | 95pp | +56% |
| Part IV | 84pp | 144pp | +71% |
| Back Matter | 36pp | 58pp | +61% |
| **TOTAL** | **336pp** | **616pp** | **+83%** |

### Content Ratio (600pp Basis)

| Content Type | Percentage | Pages | Description |
|-------------|-----------|-------|-------------|
| Prose | 50% | ~308pp | Explanatory text, motivation, examples |
| Figures + captions | 35% | ~216pp | Rich visualization throughout |
| Equations + proofs | 10% | ~62pp | Complete proofs where appropriate |
| Tables | 5% | ~30pp | Data, registries, comparisons |

---

## Chapter Interdependency Graph

```
Ch.1 (Problem) ──→ Ch.2 (Ontology) ──→ Ch.3 (Formal Universe)
                                              │
                                              ▼
Ch.4 (Axioms) ◄────────────────────── Ch.3
    │
    ├──→ Ch.5 (Realizations) ──→ Ch.12 (Implementation)
    │         │
    ▼         ▼
Ch.6 (Energy) ──→ Ch.7 (Phase Transition)
    │                    │
    ▼                    ▼
Ch.8 (Convergence) ──→ Ch.9 (Multi-Formation)
    │                         │
    ▼                         ▼
Ch.10 (Transport) ──→ Ch.11 (Diagnostic Vector)
                              │
                              ├──→ Ch.13 (Experiments)
                              ├──→ Ch.14 (Applications)
                              └──→ Ch.15 (Registry)
```

**Critical path:** 1 → 2 → 3 → 4 → 6 → 7 → 8 (core mathematical development)

**Independent branches after Ch.8:**
- Ch.9-10 (multi-formation + temporal) can be read somewhat independently
- Ch.12-13 (implementation) requires Ch.5-6 but not Ch.7-8 for basic pipeline
- Ch.14 (applications) requires Ch.1-3 + Ch.11 for cognitive science track

---

## Key Figures Summary (Total: ~90 figures)

| Chapter | Count | Key Figures |
|---------|-------|-------------|
| Front | 2 | Notation guide, book structure |
| 1 | 8 | Graded field, framework comparison, desiderata, field examples, pipeline, timeline |
| 2 | 14 | Soft primacy, X_t types, Bind examples (3), Sep examples (3), Inside examples (3), Persist example, diagnostic 3D |
| 3 | 6 | Formal universe, operator triad, transport, worked example, derived notions, removal timeline |
| 4 | 7 | Closure convergence, sigmoid, non-transitivity, b_D comparison, transport types, axiom DAG, parameter region |
| 5 | 8 | Sigmoid a_cl, worked example, resolvent vs. Cesaro, fingerprint, Sinkhorn, transport plan, FD verification, Jacobian |
| 6 | 10 | Volume constraint, E_cl landscape, E_sep loop, double-well, balance, transport cost, 3D energy, four terms, predicate-energy, λ-sensitivity |
| 7 | 8 | Eigenvalue spectrum, phase diagram, bifurcation, spectral universality, Fiedler gallery, SCC vs. AC, perturbation, geometric intuition |
| 8 | 5 | Gradient flow, convergence rate, eigenvalue comparison, sharp-interface, deep core |
| 9 | 10 | Architecture comparison, K-field, K=2 example, regime diagram, barriers, merge sequence, barrier scaling, spectral bound, d_min*, graph gallery |
| 10 | 8 | Tracking failures, fingerprint, Sinkhorn iteration, transport plan, fixed-point, core inheritance, K=2 transport, temporal sequence |
| 11 | 10 | Radar charts, Bind(params), Sep comparison, persistence construction, QM verification, Persist comparison, P1-P5 verification (5) |
| 12 | 4 | Module graph, gradient verification, optimization trajectory, tutorial output |
| 13 | 18 | Parameter sweeps (3), phase transition (3), Allen-Cahn (2), transport (3), multi-formation (3), scaling (2), predictions (2) |
| 14 | 8 | Gestalt mapping, framework matrix, SCC vs PP vs IIT, predictions, CV example, visual search, speech, roadmap |
| 15 | 2 | Theorem DAG, completeness trajectory |
| Back | 5 | Graph Laplacian (2), OT, parameter space, decision tree |

---

## Key Tables Summary (Total: ~28 tables)

| # | Table | Chapter |
|---|-------|---------|
| 1 | Notation and symbol reference | Front |
| 2 | Five framework implicit assumptions | Ch.1 |
| 3 | X_t types comparison | Ch.2 |
| 4 | Formal universe components | Ch.3 |
| 5 | Primitive/derived registry | Ch.3 |
| 6 | Operator removed: functional roles | Ch.3 |
| 7 | Axiom summary (all groups) | Ch.4 |
| 8 | Parameter admissibility | Ch.4 |
| 9 | Operator realization summary | Ch.5 |
| 10 | Energy term comparison | Ch.6 |
| 11 | Gradient formula reference | Ch.6 |
| 12 | Phase transition parameters | Ch.7 |
| 13 | Theorem dependency matrix | Ch.8 |
| 14 | Regime classification | Ch.9 |
| 15 | T-Persist conditions | Ch.10 |
| 16 | Diagnostic vector examples | Ch.11 |
| 17 | Prediction verification results | Ch.11 |
| 18 | Module API reference | Ch.12 |
| 19 | Experiment-theorem mapping | Ch.13 |
| 20 | Experiment summary (all 58) | Ch.13 |
| 21 | Gestalt mapping | Ch.14 |
| 22 | Framework comparison matrix | Ch.14 |
| 23 | Empirical prediction protocols | Ch.14 |
| 24 | Complete parameter registry | App.B |
| 25 | Parameter tuning guide | App.B |
| 26 | Commitment Notes index | App.C |
| 27 | Development timeline | App.D |
| 28 | Complete theorem registry | Ch.15 |

---

## Expansion Details: What's New in Each Chapter

### Key Additions Across All Chapters

1. **Discussion Questions and Exercises** (2pp per chapter, 15 chapters = 30pp total)
   - Conceptual discussion questions (5-7 per chapter)
   - Computational exercises (2-3 per chapter)
   - Reference to companion code where applicable

2. **Rich Visualization** (figures increased from 42 → 90)
   - Each concept gets 2-3 figures (previously 1)
   - Step-by-step construction visualizations
   - Side-by-side comparisons (before/after, with/without)
   - Gallery-style figures for diverse examples

3. **Extended Examples** (examples expanded from 1-2pp → 3-5pp)
   - Worked computations on 5×5 and 10×10 grids
   - Multiple parameter settings shown
   - Failure cases alongside success cases

4. **Complete Proofs** (where previously only sketched)
   - T-Bind-Proj: full proof with all intermediate steps
   - Coupling Bound Lemma: all six parts
   - Proto-Cohesion Existence: complete assembly
   - T14 Łojasiewicz convergence: full details

---

## Audience Reading Paths (Updated for 600pp)

### For Mathematicians (~200pp core + appendix)
Chapters 1, 3, 4-8, 15, Appendix A
- Focus: axioms, proofs, convergence, phase transitions
- All 48 theorems with proof sketches or full proofs

### For Cognitive Scientists (~170pp)
Chapters 1-3, 7, 10-11, 14
- Focus: motivation, Gestalt connections, predictions, applications
- Minimal mathematical prerequisites

### For ML/AI Researchers (~160pp)
Chapters 1, 4-5, 6, 12-13
- Focus: energy formulation, algorithms, implementation, experiments
- Hands-on with `scc/` package

---

## Design Rationale (Updated)

### Why 600pp?

1. **Academic textbook standard:** 500-700pp is typical for graduate-level monographs (Springer, Cambridge)
2. **Visual richness:** 90 figures (35% of content) makes the theory accessible to diverse audiences
3. **Complete proofs:** The expanded edition includes full proofs where the 336pp version had only sketches
4. **Self-containedness:** Expanded appendices (20pp math background) remove the need for external references
5. **Exercise integration:** 30pp of exercises make the book suitable for course adoption

### What This Is NOT

- Not a theorem listing — substantial prose explains *why* each structural choice matters
- Not a paper compilation — the material is reorganized pedagogically, not chronologically
- Not implementation documentation — code serves the theory, not vice versa
- Not padded — every added page serves a specific pedagogical purpose (example, visualization, proof detail, or exercise)
