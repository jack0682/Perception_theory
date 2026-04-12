# SCC Theory Structure Analysis for Textbook Scope

**Date:** 2026-04-03
**Session:** SCC Textbook — Spec Analysis & Scope Determination
**Category:** analysis
**Status:** complete
**Depends on:** Canonical Spec v2.1.md, Agent Instructions.md, CONVENTIONS.md, CHANGELOG.md

---

## 1. Executive Summary

This document analyzes the complete structure of Soft Cognitive Cohesion (SCC) theory as formalized in **Canonical Spec v2.1** (1122 lines, 15 sections) to determine the scope, depth, and content ordering for a graduate-level textbook. The theory has matured through 12 structured iterations, yielding **27 Category A theorems**, **3 Category B**, **6 Category C**, **2 retracted claims**, a working Python implementation (174 tests), and two paper drafts.

---

## 2. Canonical Spec v2.1 — Section-by-Section Summary

| Section | Title | Content | Textbook Relevance |
|---------|-------|---------|-------------------|
| §0 | Summation Convention | Ordered-pair convention (load-bearing for T8-Core) | Notation chapter |
| §1 | Status Note | Version history, key changes from v2.0 | Preface material |
| §2 | Foundational Orientation | Pre-objective cohesion philosophy; soft > crisp | Ch1: Motivation |
| §3 | Formal Universe | $\mathfrak{C}^{\mathrm{soft}}$ tuple; 6 primitives (T, X_t, u_t, Cl_t, N_t/D_t, M_{t→s}) | Ch2: Formal Framework |
| §4 | Why Soft Is Primary | 5 structural arguments for soft primacy | Ch1: Motivation |
| §5 | Derived Notions | Core, Interior, Boundary Band, Exterior, Transition Diagnostics | Ch3: Morphology |
| §6 | Axiomatic Groups A–E | 5 groups, ~15 axioms total | Ch4-Ch5: Axioms |
| §7 | Proto-Cohesion | 4 predicates (Bind, Sep, Inside, Persist) + diagnostic vector $\mathbf{d} \in [0,1]^4$ | Ch6: Predicates |
| §8 | Minimal Energy Principle | Volume constraint $\Sigma_m$; 4-term energy $\mathcal{E} = \lambda_{cl}\mathcal{E}_{cl} + \lambda_{sep}\mathcal{E}_{sep} + \lambda_{bd}\mathcal{E}_{bd} + \lambda_{tr}\mathcal{E}_{tr}$ | Ch7: Energy |
| §9 | Provisional Operator Forms | Sigmoid closure, distinction, resolvent co-belonging, transport kernel | Ch8: Realizations |
| §10 | Structural Interpretation | Philosophical claims; dual-mode self-referentiality | Ch1/Ch9 |
| §11 | Fixed Commitments & Open Choices | 13 fixed commitments, 9 open design choices | Ch9: Open Problems |
| §12 | Open Problems | Multi-formation kinetic paradigm; 3 pillars; K-field architecture | Ch12-Ch14 |
| §13 | Proved Results Registry | 27 Cat A + 3 Cat B + 6 Cat C + 2 retracted = 36 total | Ch10-Ch11: Theorems |
| §14 | Commitment Notes | CN1–CN14: meta-theoretical constraints | Throughout |
| §15 | Closing Summary | Status summary; 75% fully proved | Epilogue |

---

## 3. Axiomatic Groups — Organization

### Group A: Soft Closure (4 axioms)
- **A1'** Conditional Extensivity — $\mathrm{Cl}(u)(x) \geq u(x)$ when $u(x) \leq c^*$ and $(Pu)(x) \geq u(x)$
- **A2** Monotonicity — $u \leq v \Rightarrow \mathrm{Cl}(u) \leq \mathrm{Cl}(v)$
- **A3** Stabilization Tendency — Contraction with rate $a_{cl}/4 < 1$ (Banach)
- **A4** Continuity

Key: Non-idempotent closure is a *signature commitment* (CN1). Strictly positive-definite Hessian (T3/T6-Stability).

### Group B: Soft Adjacency (4 axioms)
- **B1** Nonnegativity
- **B2** Symmetry
- **B3** Locality
- **B4** Non-Transitivity

### Group C: Soft Co-belonging (4 axioms, DIAGNOSTIC ONLY)
- **C1** Dependence on u and N
- **C2** Distinction from Adjacency
- **C3''** Local Monotonicity (revised from C3)
- **C4** Symmetry (new in v2.0)

Key: $\mathbf{C}_t$ demoted from formal universe — does not enter predicates or energy.

### Group D: Distinction (3 axioms)
- **D-Ax1** Exterior Sensitivity
- **D-Ax2** Asymmetry
- **D-Ax3** Boundary Sensitivity ($b_D = 0$ for analyticity, CN13)

### Group E: Temporal Transport (4 axioms)
- **E1** Sub-Stochasticity
- **E2** Non-Injectivity
- **E3** Core Inheritance (reclassified: solution constraint, not operator axiom)
- **E4** Structural Sensitivity

---

## 4. Energy Functional — Key Formulas

### Volume Constraint
$$\Sigma_m = \{u \in [0,1]^n : \sum_x u(x) = m\}$$

Admissible range: $c = m/n \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6) \approx (0.211, 0.789)$

### Four Energy Terms

| Term | Formula | Role | Gradient |
|------|---------|------|----------|
| $\mathcal{E}_{cl}$ | $\sum_x (u(x) - \mathrm{Cl}(u)(x))^2$ | Self-support | $\nabla = 2(I - J_{Cl})^T(u - Cl(u))$ |
| $\mathcal{E}_{sep}$ | $\sum_x u(x)(1 - D(x; 1-u))$ | Exterior distinction | Self-referential |
| $\mathcal{E}_{bd}$ | $\alpha \sum_{x,y} N(x,y)(u(x)-u(y))^2 + \beta \sum_x u(x)^2(1-u(x))^2$ | Morphology | $4\alpha Lu + \beta W'(u)$ |
| $\mathcal{E}_{tr}$ | $\sum_{x,y} M(x,y)\omega(u_t(x),u_s(y))(u_s(y)-u_t(x))^2$ | Temporal inheritance | Transport-dependent |

Critical implementation details:
- Ordered-pair: $E_{bd}$ smoothness = $2\alpha u^T L u$, gradient = $4\alpha Lu$ (factor 4, not 2)
- Double-well: $W'(u) = 2u(1-u)(1-2u)$ (factor 2 correction from I6)
- Sep uses u-weighted average (not C_t-weighted)

---

## 5. Proved Results Registry — Complete Classification

### Category A: 27 Fully Proved

| # | Theorem | Statement (compressed) |
|---|---------|----------------------|
| 1 | **T1** Existence | Energy minimizer exists on $\Sigma_m$ (compactness) |
| 2 | **T6a** Closure FP Existence | Sigmoid closure has fixed point |
| 3 | **T6b** Closure FP Uniqueness | Unique when $a_{cl} < 4$ (Banach contraction) |
| 4 | **T-A2** Monotonicity | Unconditional for sigmoid |
| 5 | **T8-Core** Phase Transition | Non-trivial minimizer exists when $\beta/\alpha > 4\lambda_2/|W''(c)|$ |
| 6 | **T8-Full** Full Energy Minimizer | $\mu_0(H_{bd})$ at minimizer > 0 (upgraded from Cat B) |
| 7 | **T20** Axiom Consistency | Parameter admissibility registry |
| 8 | **T14** Gradient Flow | Convergence via Łojasiewicz inequality (analytic energy) |
| 9 | **T3/T6-Stability** | Non-idempotent closure → strictly positive-definite Hessian |
| 10 | **T7-Enhanced** Metastability | SCC Hessian eigenvalue > Allen-Cahn eigenvalue |
| 11 | **T11** Γ-Convergence | Sharp-interface limit → modified graph cut |
| 12 | **C-Axioms** | Resolvent satisfies C1–C4 |
| 13 | **QM1–4** | $\mathcal{Q}_{morph}$ axiom satisfaction |
| 14 | **Predicate-Energy Bridge** | Sep = 1 − E_sep/m (exact); Bind reverse at minimizers (upgraded) |
| 15 | **Deep Core Dom. 2b** | Isoperimetric inequality on $\mathbb{Z}^d$ (upgraded) |
| 16-27 | Auxiliary results | Sep identity, Bind bound, T-Persist-1(a), T-Persist-1(c), etc. |

### Category B: 3 Proved with Structural Parameter

| # | Theorem | Condition |
|---|---------|-----------|
| 1 | **T-Bind-Proj** | Proved for $\tau = 1/2$; general $\tau$ regime-specific |
| 2 | **T-Bind-Full** | Same condition |
| 3 | **T-Persist-K-Sep** | Conditional on per-formation H1–H4, WS, SR |

### Category C: 6 Conditional

| # | Theorem | Key Condition |
|---|---------|--------------|
| 1 | **T-Persist-1(b)** | Basin containment (BC' proved, tightened to Cat B effective) |
| 2 | **T-Persist-1(d)** | Interior gap (H2'+H3) |
| 3 | **T-Persist-1(e)** | Transport concentration (TC' proved, effective Cat B) |
| 4 | **T-Persist-Full** | Unified under (WR', PS, ND, NB, H2', H3, GT) |
| 5 | **T-Persist-K-Weak** | Weakly-interacting regime under (SR), (WI) |
| 6 | **T-Persist-K-Unified** | Parametric: $\Lambda_{coupling}$ bridges Sep/Weak/Strong |

### Retracted: 2

| # | Claim | Reason |
|---|-------|--------|
| 1 | **Theorem 3.3** ($\bar{r}_0 = O(n^{-1/d})$ general $\tau$) | Experimentally falsified |
| 2 | **K-Saddle Conjecture** | K=2 is always local minimum, never saddle (exp30) |

---

## 6. Phase Transition Theory

The central existence result is **T8-Core**:

**Condition:** $\beta/\alpha > 4\lambda_2 / |W''(c)|$

where:
- $\beta$: double-well strength
- $\alpha$: smoothness penalty
- $\lambda_2$: Fiedler eigenvalue (algebraic connectivity)
- $W''(c) = 2(1-6c+6c^2)$, negative in spinodal $(0.211, 0.789)$

**Mechanism:** At the critical ratio, the uniform state $u \equiv c$ on $\Sigma_m$ becomes unstable (negative Hessian eigenvalue in Fiedler direction). Non-trivial phase-separated minimizer bifurcates supercritically.

**Enhanced metastability (T7):** SCC energy has strictly larger minimum Hessian eigenvalue than Allen-Cahn alone, due to the positive-definite closure energy Hessian contribution.

---

## 7. Multi-Formation & Temporal Results

### Paradigm Shift (2026-04-02)
- **K*=1 universally** on connected graphs — single formation is always global minimum
- Multi-formation = **metastable local minima** (kinetic, not thermodynamic)
- Barrier height $\propto \beta^{0.89}$ (exp38, exp55)

### Three Kinetic Pillars
1. **Nucleation**: Spectral eigenvectors seed initial separation
2. **Metastability**: Inter-formation barriers prevent merging ($d > d^*_{min}$)
3. **Coarsening**: Noise-driven merge dynamics toward K=1

### Temporal Persistence Hierarchy
- **T-Persist-1**: Single-formation core inheritance (5 parts: a-e)
- **T-Persist-K-Sep**: Well-separated (proved)
- **T-Persist-K-Weak**: Weakly-interacting (conditional)
- **T-Persist-K-Unified**: Parametric via $\Lambda_{coupling}$

### K-Field Architecture (I9 Decision)
- $K$ coupled fields $u^1, \ldots, u^K$ on product manifold
- Inter-field repulsion $\lambda_{rep}\langle u^j, u^k \rangle$
- Simplex constraint $\sum_k u^k(x) \leq 1$
- Guarantees K>1 by construction

### Closure's Multi-Formation Role (CN14)
- Reduces $d^*_{min}$ by ~30% (from 7 → 5 nodes at $\beta=30$)
- Barrier height increases ($\beta^{0.89}$ vs $\beta^{0.85}$ for Allen-Cahn)

---

## 8. Implementation Status

### Python Package (`scc/`)
- 7 core modules: graph, params, operators, energy, optimizer, diagnostics, multi
- 2 extension modules: transport, persistence/predicates/resolvent (thin wrappers)
- **174 passing tests** (gradient FD verified to $10^{-9}$)
- Pipeline: `GraphState → ParameterRegistry → find_formation() → FormationResult`

### Experiments (17+ total)
- exp1–exp4: λ sweep, phase transition, ablation, grid scaling
- exp9–exp11: Transport demos, fingerprint gap, concentration
- exp14: Multi-formation persistence
- exp37–exp57: Kinetic multi-formation (nucleation, barriers, coarsening, closure threshold)

### Papers
1. **Paper 1** ("Self-Referential Phase Fields on Graphs") — Math paper targeting J. Math. Phys.
2. **Paper 2** ("Before Objects: Pre-Objective Perceptual Cohesion") — CogSci paper targeting Cognitive Science

---

## 9. Unresolved Issues (from Spec §11–§12)

### Foundational Open Problems
1. **Strong self-referential transport** — tight confinement constants (25–100× conservative)
2. **Discrete substrate defense** — philosophical justification for $X_t$ individuation
3. **Strongly-interacting merge** — Kramers rates, barrier-crossing timescales
4. **Formation birth/death** — quantitative scaling laws
5. **Coarsening cascade** — full thermal noise dynamics

### Open Design Choices
1. Final form of $\mathbf{C}_t$ (resolvent is provisional)
2. Closure regularity conditions beyond A1'–A4
3. Threshold recovery rules (crisp from soft)
4. Dynamic update laws (gradient flow, evolutionary)
5. Parameter regime theory ($\lambda$ ratios)
6. Multi-formation interaction specifics
7. Self-referential transport (strong regime)

### Extension Problems
1. Renormalization group analysis
2. Sharp-interface dynamics → modified mean curvature flow
3. Crisp recovery protocol
4. Identifiability of formations

---

## 10. Commitment Notes Summary (CN1–CN14)

| CN | Title | Key Rule |
|----|-------|----------|
| CN1 | Contraction, Not Projection | Closure: unique FP, path-dependence at energy level only |
| CN2 | τ Not Primitive | Within-time evolution is implementation detail |
| CN3 | Definition Acyclic, Computation Cyclic | Must not conflate |
| CN4 | Group F Distinct | Crisp recovery ≠ soft axioms |
| CN5 | Four-Term Independence Is Conceptual | Terms interact mathematically |
| CN6 | K Is Kinetic | Multi-formation from dynamics, not energy minimum |
| CN7 | Operator Pair, Not Generic Self-Ref | Dual mode: self-completion + self-contrast |
| CN8 | Formations Metastable | Local minima, not global optimum |
| CN9 | Two-Landscape Structure | Closure landscape ≠ energy landscape |
| CN10 | Contrastive, Not Reductive | Compare to Allen-Cahn etc., but never reduce |
| CN11 | Resolvent, Not Cesàro | Co-belonging form |
| CN12 | Q_morph Persistence-Based | Filtration commitment |
| CN13 | Sep Contributes to Instability | Qualitative confirmed; quantitative TBD |
| CN14 | Closure Expands Multi-Formation | d_min* reduced ~30% by closure |

---

## 11. Textbook Scope Determination

### Recommended Scope: Full Theory + Implementation

The textbook should cover the **complete SCC theory** as of Canonical Spec v2.1, organized into 5 parts:

**Part I: Foundations (Ch1–Ch5)**
- Motivation & philosophical orientation (§2, §4, §10)
- Formal universe & primitives (§3)
- Derived morphological notions (§5)
- Axiomatic Groups A–E (§6)
- Proto-cohesion diagnostic vector (§7)

**Part II: Energy & Optimization (Ch6–Ch8)**
- Minimal energy principle & volume constraint (§8)
- Provisional operator realizations (§9)
- Gradient computation & optimization (from scc/ package)

**Part III: Main Theorems (Ch9–Ch11)**
- Existence & phase transition (T1, T8-Core, T8-Full)
- Closure contraction & stability (T6a/b, T3/T6, T7-Enhanced)
- Convergence & Γ-limit (T14, T11)
- Predicate-energy bridge

**Part IV: Temporal & Multi-Formation (Ch12–Ch14)**
- Transport theory (E1–E4, self-referential cost)
- Persistence theorems (T-Persist hierarchy)
- Multi-formation kinetic paradigm (3 pillars, K-field, Λ_coupling)

**Part V: Computation & Applications (Ch15–Ch16)**
- Implementation guide (scc/ package architecture)
- Experiments & numerical verification
- Connections to Gestalt, cognitive science, phase-field theory

### Content Ordering Principles
1. Follow the theory's own layered structure (§2 → §3 → ... → §12)
2. Proofs presented immediately after the relevant definitions
3. Computational verification alongside theoretical results
4. Open problems clearly marked per chapter
5. Each chapter opens with conceptual motivation before formalism

### Estimated Depth
- ~16 chapters, ~400–500 pages
- Graduate-level mathematics (functional analysis, graph theory, variational methods, optimal transport)
- Self-contained: all prerequisites in appendices

---

## 12. Key Mathematical Prerequisites (for Appendices)

1. **Graph theory**: Laplacian, Fiedler eigenvalue, spectral gap
2. **Functional analysis**: Banach contraction, Schauder fixed point
3. **Variational calculus**: Constrained minimization on manifolds, Łojasiewicz inequality
4. **Optimal transport**: Entropy-regularized OT, Sinkhorn algorithm
5. **Topological data analysis**: Persistent homology, superlevel-set filtration
6. **Phase-field theory**: Allen-Cahn / Ginzburg-Landau, Γ-convergence

---

## 13. Verified Predictions

### Single-Formation (5/5 verified)
- **P1** Contraction: closure iterates converge geometrically
- **P2** Independence: 4 energy terms contribute independently to diagnostics
- **P3** Enhanced dwell: metastable formations have longer lifetime (p=0.037)
- **P4** Path dependence: different initial conditions → different metastable states
- **P5** Sep-before-Inside: separation predicate satisfied before morphological articulation

### Multi-Formation Kinetic Predictions (MK-1 through MK-4)
- **MK-1** Nucleation via spectral modes (exp51)
- **MK-2** Coarsening exponent $\alpha < 1/2$ (exp57)
- **MK-3** Barrier scaling $\propto \beta^{0.89}$ (exp38)
- **MK-4** Enhanced metastability from closure (exp57 corrected)

### Falsified
- **P-Unified-1**: Persist degradation NOT monotone in $\Lambda_{coupling}$ (exp49-50)
- **Theorem 3.3**: $\bar{r}_0$ is O(1) for $\tau \neq 1/2$, not $O(n^{-1/d})$
