# Discussion Phase — Round 9: Existence, Stability, and What Can Be Proved

**Date:** 2026-03-27
**Phase:** Extended discussion — the theory meets mathematical reality

---

## Foundational Theorist — Round 9

### I. The Compactness Argument

For finite $X_t$ with $|X_t| = n$, the space $[0,1]^n$ is compact. Every continuous function on a compact set attains its minimum. So: if $\mathcal{E}_t$ is continuous, a minimizer exists.

**Proposed axiom A4 (Continuity).** $\mathrm{Cl}_t : [0,1]^{X_t} \to [0,1]^{X_t}$ is continuous with respect to $\ell^\infty$.

**Proposed axiom D-Ax4 (Continuity).** $\mathbf{D}_t(x; \cdot) : [0,1]^{X_t} \to [0,1]$ is continuous for each $x$.

**Theorem 1 (Existence of Static Minimizers).** *For finite $X_t$, if $\mathrm{Cl}_t$ satisfies A1-A4 and $\mathbf{D}_t$ satisfies D-Ax1-D-Ax4, the energy $\mathcal{E}_t$ attains its minimum on $[0,1]^{X_t}$.* Proof: continuous function on compact set. $\square$

### II. The Trivial Minimizer Problem

$u \equiv 0$ always has $\mathcal{E}_t(0) = 0$. Since $\mathcal{E}_t \geq 0$ everywhere, $u \equiv 0$ is a global minimizer. The theory's energy has a trivial ground state.

This is structurally correct: the theory permits "nothing coheres." The problem is guaranteeing *non-trivial* local minimizers.

For $u \equiv 1$: $\mathcal{E}_{\mathrm{cl}} \approx 0$, $\mathcal{E}_{\mathrm{bd}} = 0$, but $\mathcal{E}_{\mathrm{sep}}$ penalizes the saturated field for lacking distinction. The separation term is the only term preventing the degenerate $u \equiv 1$.

### III. Existence of Non-Trivial Local Minimizers

**Mountain pass strategy.** Consider a path $u_\lambda = \lambda \cdot \chi_S$ for connected subset $S \subset X_t$:
- Small $\lambda$: double-well penalizes intermediate values. Energy rises.
- Moderate $\lambda$ (near 1 on $S$, 0 off $S$): closure term small (self-supporting), distinction high, double-well small (near binary). Energy low.
- $\lambda = 1$ everywhere: distinction collapses. Energy rises.

The energy profile has a non-trivial minimum — a proto-cohesive formation.

**Theorem 2 (Non-Trivial Local Minimizers — Sketch).** Under conditions on adjacency structure and closure operator, for suitable parameters, $\mathcal{E}_t$ has a local minimizer $\hat{u} \neq 0, \hat{u} \neq \mathbf{1}$.

### IV. Stability Analysis

**At a closure fixed point $\hat{u}$ where $\mathrm{Cl}_t(\hat{u}) = \hat{u}$:**

$$\nabla^2 \mathcal{E}_{\mathrm{cl}}(\hat{u}) = 2(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}})$$

This is positive semidefinite (Gram matrix). If $\|J_{\mathrm{Cl}}\|_{\mathrm{op}} < 1$ (strict contraction), the Hessian is strictly positive definite on the complement of the fixed-point tangent space.

**Key insight:** Non-idempotent closure with $\|J_{\mathrm{Cl}}\| < 1$ gives *stronger* stability than idempotent closure (where eigenvalues of $J$ are in $\{0,1\}$ and the Hessian has zero eigenvalues in the range). This is a concrete, provable advantage of the non-idempotence commitment.

**Theorem 3 (Stability — Sketch).** *If $\hat{u}$ is a non-trivial closure fixed point with $\|J_{\mathrm{Cl}}(\hat{u})\|_{\mathrm{op}} < 1$ and lies in double-well basins, then for large enough $\lambda_{\mathrm{cl}}$ and $\beta$, $\hat{u}$ is a strict local minimizer.*

### V. The Persistence-Stability Bridge

**Conjecture.** Long-lived features in the persistence diagram of $\hat{u}$ correspond to energetically stable formation nuclei. The Cohen-Steiner-Edelsbrunner-Harer stability theorem provides topological stability; the Hessian analysis provides energetic stability. Features with high persistence are in deep double-well basins — the connection is: **stable formations produce clean persistence diagrams.**

### VI. The Inaugural Theorem

**Proto-Cohesion Existence Theorem (proposed).** Under mild conditions on adjacency and closure, there exist parameters such that $\mathcal{E}_t$ has a stable, non-trivial local minimizer satisfying $(\mathsf{Bind}, \mathsf{Sep}, \mathsf{Inside}) \in (1-\delta, 1]^3$.

### VII. Long-Term Goal: Turing Instability

The SCC gradient flow is a reaction-diffusion system. If the parameters enter a Turing-unstable regime, the homogeneous state $u \equiv c$ is unstable and spontaneously develops spatially structured formations. A theorem proving this would be the strongest vindication of the ontological commitment: **formations emerge spontaneously from unstructured fields.**

---

## Formal Systems Architect — Round 9

### 1. Theorem Registry at Layer 5.75

```
Layer Block 5.75: THEOREM REGISTRY
  - Derived consequences of Layers 1-5.5
  - Three categories: Axiomatic theorems, Realization-conditional, Conjectured
  - Each entry: claim, dependencies, status, proof strategy
```

### 2. Five-Category Classification

**(a) Trivially provable:** T1-T5 (monotonicity, sub-conservation, filtration nesting, reflexivity bounds).

**(b) Provable with regularity:** T6 (closure fixed points), T7 (energy minimizer existence), T8 (proto-cohesion non-vacuousness), T9 (PD stability import), T10 (multiple closure fixed points).

**(c) Requires C_t:** T11 (co-belonging ↔ basins), T12 (multi-formation decomposition), T13 (C_t-Sep strengthening).

**(d) Requires dynamics:** T14 (gradient flow → proto-cohesion), T15 (persistence under perturbation), T16 (convergence rate compatibility).

**(e) Genuinely open:** T17 (formal distinctiveness), T18 (identifiability), T19 (multi-formation coexistence), T20 (axiom consistency).

### 3. T20 — Axiom Consistency

**A1 may FAIL for sigmoid closure under some parameter regimes.** The sigmoid form gives $\mathrm{Cl}_t(u)(x) = \sigma(a_{\mathrm{cl}}((1-\eta)u(x) + \eta(P_t u)(x) - \tau_{\mathrm{cl}}))$. Weak extensivity ($\mathrm{Cl}_t(u)(x) \geq u(x)$) is NOT guaranteed for all parameters.

**T20 should produce a parameter admissibility registry:** for each realization, the parameter regimes satisfying all axioms.

### 4. Finite X_t as Canonical Target

The canonical spec targets finite $X_t$. All provisional realizations use discrete sums. On finite spaces, continuity is automatic for compositions of elementary operations. **Category (b) theorems upgrade to (a) on finite X_t.**

### 5. Load-Bearing Analysis

| Group | # Theorems | Most Critical |
|-------|-----------|---------------|
| A | 6 | T6 (fixed points) |
| B | 3 | T12 (decomposition) |
| C | 4 | T11 (co-belonging ↔ basins) |
| D | 3 | T17 (distinctiveness) |
| D' | **0** | — |
| E | 3 | T15 (persistence) |
| F | 4 | T9 (PD stability) |

**Group D' supports zero theorems.** Retained for conceptual completeness only.

### 6. Full Theorem Registry

Twenty theorems catalogued with dependencies, proof strategies, blocking relationships, and critical path. T20 → T6/T7 → T14 → T15/T16. T11 blocked on C_t, blocking T12 → T19.

---

## Critical Skeptic — Round 9

### 1. The Trivial Minimizer Problem Is Worse Than It Looks

$\mathcal{E}(0) \approx 0$ and $\mathcal{E}(\mathbf{1}) \approx 0$. Both trivial states are near-global minimizers. **Formations are NOT global energy minimizers.** They are local minimizers, saddle points, or metastable states.

The theory's real claim must be: formations are *constrained* minimizers. But the constraint is never stated. **Demand:** specify the admissibility constraint that excludes trivial minimizers.

### 2. Self-Referential Terms Break Standard Machinery

For finite $X_t$, existence is trivial by compactness. **The real question is non-trivial minimizer existence.**

The uniform field $u \equiv c = m/|X_t|$ is a serious competitor. Whether structured formations beat it depends on $\beta$: large $\beta$ (strong double-well) favors formation structure; small $\beta$ favors uniformity.

**There exists a critical $\beta^*$** below which minimizers are uniform and above which they have formation structure. This is the Allen-Cahn phase transition.

### 3. The Double-Well Irony

The double-well — the theory's main ontological embarrassment — is the term that **guarantees formation existence**. Without it ($\beta = 0$), the constrained minimizer is uniform. The double-well creates the energy barrier making non-trivial local minimizers possible.

### 4. Stability: The Nonlocal Hessian

The full Hessian $H = \lambda_{\mathrm{cl}} H_{\mathrm{cl}} + \lambda_{\mathrm{sep}} H_{\mathrm{sep}} + \lambda_{\mathrm{bd}} H_{\mathrm{bd}}$ is dense and nonlocal. $H_{\mathrm{bd}}$ (Allen-Cahn) is well-understood. $H_{\mathrm{cl}}$ is PSD at exact fixed points. $H_{\mathrm{sep}}$ has no known spectral structure.

### 5. Provability Horizon

**Green zone (now):** Basic existence, gradient flow existence, closure fixed points. Mathematically correct but theoretically uninteresting.

**Yellow zone (with effort):** Non-trivial minimizer existence, metastability, sharp-interface limit for E_bd. Genuine results requiring adaptation of known techniques. Each is a research paper.

**Red zone (blocked):** Anything involving C_t, T_t, Q_morph essentially. Proto-cohesion satisfiability, formal distinctiveness, multi-formation emergence.

**"The most theoretically interesting results are ALL in the red zone."**

### 6. Proof Roadmap

1. Non-trivial minimizer existence under volume constraint
2. Critical $\beta^*$ as function of $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}$
3. Minimizers satisfy Bind
4. Numerical Hessian analysis at computed minimizers
5. Develop C_t (unblocks red zone)

### 7. The Honest Assessment

The theory's deepest vulnerability: **the things it CAN prove are the least interesting, and the things that WOULD be interesting require operators it hasn't defined.** The proof program and the operator development program are coupled. Neither can succeed alone.

---

## Synthesis Moderator — Round 9

### 1. Four Provability Zones

- **Zone 1 (Now):** Energy minimizer existence (compactness), axiom consistency (T20), basic properties. Trivial but foundational.
- **Zone 2 (Moderate effort):** Gradient flow, sharp-interface for E_bd, stability of binary equilibria. Import from Allen-Cahn.
- **Zone 3 (Requires C_t):** Sep reformulation, Inside via persistence, full non-trivial minimizer existence.
- **Zone 4 (Open research):** Sharp-interface with corrections, Turing instability, multi-formation, formal distinctiveness.

### 2. T20 as Highest Priority

Axiom consistency must come first. The Architect's concern about A1 potentially failing for sigmoid closure is concrete and actionable. **T20 should produce a parameter admissibility registry.**

### 3. The Trivial Minimizer Resolution

Formations are metastable, not globally optimal. This is ontologically aligned: "something holding together" is an achievement against dissolution. The mountain pass argument provides the existence mechanism.

**The double-well irony:** ontological threat = existence guarantee. The energy barrier from the double-well enables the mountain pass. β governance must balance these competing roles.

### 4. Theorem Roadmap

**Tier 1 (Foundation):** T20 (axiom consistency), continuity axioms, existence by compactness.

**Tier 2 (Non-Trivial Existence):** Energy barrier analysis, mountain pass, Bind satisfaction, gradient flow.

**Tier 3 (Structural):** C_t convergence, reformulated Sep, Allen-Cahn import, Hessian analysis.

**Tier 4 (Deep):** Full ProtoCoh existence, sharp-interface limit, Turing instability, multi-formation.

### 5. Complete Settled/Contested/Deferred Tables

44 settled items across 9 rounds. 21 contested items. Comprehensive deferred research problems at foundational, bridging, extension, and theorem levels.

**Meta-observation:** Round 9 is the most technically grounded round. The path from foundational to spectacular runs through C_t formalization → Sep reformulation → full ProtoCoh existence → stability → sharp-interface limit. That path is now explicit. The discussion is ready for its final round.
