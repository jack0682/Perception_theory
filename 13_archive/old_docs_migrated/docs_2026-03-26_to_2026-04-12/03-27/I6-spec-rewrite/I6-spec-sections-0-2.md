# Canonical Specification of Soft Cognitive Cohesion — v2.0

# Sections 0–2: Convention, Status, Foundation

**Author:** Spec Drafter | **Iteration:** 6, Round 1 | **Date:** 2026-03-27

---

## 0. Summation Convention

All double sums of the form $\sum_{x,y \in X_t}$ range over **ordered pairs**: when the kernel is symmetric ($\mathbf{N}_t(x,y) = \mathbf{N}_t(y,x)$), each undirected edge is counted twice. This convention is adopted because the Canonical Spec's energy terms are written with the bare double-index notation $\sum_{x,y}$, and fixing the convention to ordered pairs eliminates an ambiguity that propagates into every Hessian computation.

**Consequences.** The smoothness sub-term of the boundary energy (Section 8) evaluates to

$$
\alpha \sum_{x,y \in X_t} \mathbf{N}_t(x,y)\,(u_t(x) - u_t(y))^2 \;=\; 2\alpha\, v^T L\, v
$$

where $L$ is the combinatorial graph Laplacian and $v = u_t - c\mathbf{1}$ is the deviation from the uniform state at volume fraction $c$. The Hessian of this term with respect to $u$ is $4\alpha L$. The phase-transition theorem (T8-Core, Section 13) therefore gives the critical ratio

$$
\frac{\beta}{\alpha} > \frac{4\lambda_2}{\lvert W''(c)\rvert}
$$

where $\lambda_2$ is the Fiedler (smallest positive) eigenvalue of $L$ and $W(u) = u^2(1-u)^2$ is the double-well potential with $W''(c) = 12c^2 - 12c + 2$.

**Double-well gradient.** Because $W'(u) = 2u(1-u)(1-2u)$, the pointwise gradient of the double-well sub-term carries a factor of $2\beta$, not $\beta$. The full boundary-energy gradient on the constraint manifold is

$$
\nabla_{u}\,\mathcal{E}_{\mathrm{bd}} \;=\; 4\alpha\, L\, u \;+\; 2\beta\, u\,(1-u)\,(1-2u).
$$

This factor of $2$ is load-bearing: omitting it halves the double-well force and produces more diffuse formations than the theory intends.

**Unordered-pair notation.** Where sums over unordered pairs are intended, the notation $\sum_{\{x,y\} \subset X_t}$ is used explicitly, with the identity $\sum_{\{x,y\}} f(x,y) = \tfrac{1}{2}\sum_{x,y} f(x,y)$ for symmetric $f$.

---

## 1. Status Note

This document is the canonical human-readable formal specification of the theory of Soft Cognitive Cohesion, **version 2.0**. It supersedes the original Canonical Spec (v1.0, March 2026) and incorporates all mandatory revisions identified across five iterations of structured multi-agent development (Iterations 1–5, March 2026).

The document declares the primitive ontology, the formal universe, the axiomatic groups (A–E), the derived predicates, the minimal energy principle with its volume constraint, and the proved-results registry that jointly constitute the theory as it now stands. It separates stable theoretical commitments — principles that define the identity of the theory and are not subject to routine revision — from open design choices that remain underdetermined but constrained by those commitments. Provisional operator realizations are presented explicitly as currently favored candidates, not as permanently fixed definitions.

### 1.1. Principal Changes from v1.0

**Axiomatic revisions.**

- A1 (weak extensivity) is replaced by **A1' (conditional extensivity)**: the original A1 was proved incompatible with A3 for the sigmoid closure realization (satisfying A1 at $u = 0.9$ requires $a_{\mathrm{cl}} \geq 5.49$, contradicting the contraction bound $a_{\mathrm{cl}} < 4$). A1' resolves this by conditioning extensivity on commensurate neighborhood support, adding self-regulation as a structural feature.
- A3 (stabilization tendency) is **strengthened** to a Cauchy convergence condition with a proved contraction rate of $a_{\mathrm{cl}}/4$ for the sigmoid closure.
- C3 (reflexivity) is replaced by **C3'' (local monotonicity)**: self-co-belonging is monotone in cohesive participation, without committing to a specific functional form.
- **C4 (symmetry)** is added as an explicit axiom for co-belonging.
- **E3 (core inheritance)** is reclassified from operator axiom to **solution constraint**: it characterizes what good solutions achieve, not what the transport kernel must satisfy universally.
- The transition operator $\mathbf{T}_t$ is **removed from the formal universe** and demoted to a derived diagnostic. It had zero realizations, zero theorems, zero energy terms, and zero predicate roles across five iterations; its conceptual content is preserved by the gradient indicator $g_t$, the boundary band $\mathrm{Bd}_t$, and the morphological quality measure $\mathcal{Q}_{\mathrm{morph}}$.

**Structural additions.**

- The **volume constraint** $\sum_x u_t(x) = m$ is elevated to a structural axiom, with ontological justification as a finite cohesive budget (Section 8.0).
- The **morphological quality measure** receives a provisional definition: $\mathcal{Q}_{\mathrm{morph}} = \ell_{\max} \cdot \mathrm{Artic}$, based on the $H_0$ persistence diagram of the superlevel-set filtration (Section 7.1).
- The **co-belonging operator** receives a provisional resolvent realization $\mathbf{C}_t = (I - \alpha\, W_{\mathrm{sym}})^{-1}$, replacing the Cesàro form (which was proved to degenerate to the stationary distribution, destroying pairwise information).
- The **distinction parameter** $b_D$ is set to zero (or $\varepsilon$-smoothed) to ensure energy analyticity, as required by the gradient-flow convergence theorem (T14).
- The **summation convention** (ordered pairs) is declared explicitly (Section 0), resolving the ambiguity that produced the $2\lambda_2$ vs. $4\lambda_2$ discrepancy in T8-Core.

**Predicate and representation revisions.**

- The **separation predicate** $\mathsf{Sep}$ is revised to a $\mathbf{C}_t$-weighted form that is threshold-independent and naturally continuous (Section 7.1).
- The **binding predicate** $\mathsf{Bind}$ norm is specified as $\ell^2$ (the $\ell^\infty$ norm was proved unsuitable: boundary sites have inherent discrepancies up to $\sim 0.21$).
- **Proto-cohesion** is reformulated as a diagnostic vector $\mathbf{d} \in [0,1]^4$, replacing the Boolean conjunction. The graded vector is the primary representation; the Boolean form is a secondary projection obtained by thresholding each component.

**New sections.**

- **Section 0** (Summation Convention): resolves the ordered-pair convention and records the double-well gradient factor.
- **Section 13** (Proved Results Registry): 12 theorems from Iterations 1–2, with precise statements, proof methods, and caveats.
- **Section 14** (Commitment Notes): 13 consolidated meta-theoretical commitments governing interpretation and future development.

### 1.2. Mathematical Status

The theory has **12 proved theorems** (Section 13), including:

- **T8-Core** (non-trivial minimizer existence under computable phase transition),
- **T14** (gradient-flow convergence via Łojasiewicz inequality),
- **T3/T6-Stability** (non-idempotent closure gives strictly stronger stability than idempotent closure),
- **T7-Enhanced** (SCC formations have strictly deeper energy basins than Allen-Cahn formations),
- **T11** (Γ-convergence to a modified graph-cut functional in the sharp-interface limit).

The theory's **largest gap** is temporal: zero proved results for the persistence component of proto-cohesion, and dependence of the provisional transport kernel on external (non-self-referential) features. Multi-formation theory is architecturally blocked in the contraction regime ($a_{\mathrm{cl}} < 4$). These gaps are acknowledged, layer-classified (Section 12), and constitute the primary agenda for future development.

This specification is intended to serve as the authoritative reference for future formalization, implementation, and theoretical extension. It is written to be readable by mathematicians, theoretical cognitive scientists, and system designers alike.

---

## 2. Foundational Orientation

The theory of Soft Cognitive Cohesion does not begin from objects. It does not presuppose that the world is first given as a collection of discrete, bounded, individually identifiable things. It does not assume that perception starts with already-separated entities whose properties then need to be classified. Any framework that begins from such assumptions starts too late: it inherits the results of a prior process of individuation without accounting for how that individuation was achieved.

The foundational commitment of this theory is that **coherent formation precedes discrete objecthood**. What is first encountered — whether in sensory experience, in structured data, or in any relational medium — is not a set of labeled objects but a field of graded cohesion: regions of varying internal support, continuity, and mutual reinforcement, from which object-like stability may or may not eventually emerge.

### 2.1. Cohesion as Graded Field

Cohesion is given as a graded field, not as a binary partition. A soft cohesion field $u_t : X_t \to [0,1]$ assigns to each site in a relational support space a degree of participation in a cohesive formation. This degree is not a probability of class membership. It is an intensity of cohesive participation: how strongly a site is sustained by, and contributes to, the internal relational organization of a formation.

Objects, in this theory, are not primitives. They are later-read stabilized formations: cohesive fields that have achieved sufficient closure (self-support under relational completion), sufficient distinction (asymmetry with respect to their exterior), sufficient morphological articulation (a structured transition from core to boundary to exterior), and sufficient temporal persistence (structural inheritance of their cohesive organization across time). An object is not an input to the theory; it is, at most, a distinguished output — a formation that satisfies all four conditions of proto-cohesion robustly and stably. Proto-cohesion itself is assessed as a graded diagnostic vector $\mathbf{d} \in [0,1]^4$, not as a binary predicate: objecthood admits degrees, and the theory's formal apparatus is designed to represent those degrees without premature collapse.

### 2.2. Relational Priority

Relational structure is prior to discrete individuation. What makes a formation cohere is not an intrinsic property of isolated points but a pattern of local mutual support: sites that reinforce one another, that belong together not because of a shared label but because their relational configuration is self-sustaining. Internality, boundary, and persistence are consequences of this structured cohesion, not presupposed properties of pre-given objects.

### 2.3. The Relational Support Space

The relational support space $X_t$ is a domain of relational loci — the sites over which cohesion is defined — not a collection of pre-given objects. The individuation of sites in $X_t$ is a modeling decision at the implementation layer, not an ontological commitment of the theory. Sites are scaffolding; formations are architecture. The relevant contrast is between bare relational loci (which $X_t$ provides) and already-individuated objects (which the theory refuses to presuppose). Discreteness of substrate does not entail individuation of formations.

This distinction is essential because the theory claims to describe pre-objective cohesion — formation prior to objecthood. A natural objection is that defining a field over discrete sites already presupposes individuated entities. The response is that $X_t$ provides the *relational substrate* over which cohesion organizes itself, not the *objects* that the theory aims to explain. The discrete structure of $X_t$ no more commits the theory to pre-given objects than the discrete structure of a pixel grid commits image analysis to pre-given visual objects, or the atomic structure of a fluid commits hydrodynamics to pre-given fluid parcels. What is ontologically primitive is the cohesion field $u_t$ and its relational organization — the pattern of graded mutual support — not the identity of the sites over which it is defined. The theory's claim is that cohesive formation *over* $X_t$ precedes objecthood *within* $X_t$.

### 2.4. Finite Cohesive Capacity

The theory incorporates a structural commitment to **finite cohesive capacity**: any finite relational system can sustain only a bounded total amount of cohesion (formalized as the volume constraint $\sum_x u_t(x) = m$; see Section 8.0 for the full treatment). This is not a computational convenience but an ontological commitment. Formation is selection — the concentration of finite resources into structured regions. Universal cohesion ($u \equiv 1$ everywhere) is as featureless as universal non-cohesion ($u \equiv 0$): both lack the selective concentration that constitutes a formation. The cohesive budget $m$ is the finite resource that forces selectivity, and selectivity is the precondition for formation.

This commitment has a mathematical consequence: without the volume constraint, the trivial field $u \equiv 0$ is the global energy minimizer (all energy terms are nonnegative and vanish at zero). The volume constraint is therefore jointly motivated by ontological principle (finite capacity) and mathematical necessity (non-trivial minimizer existence).

### 2.5. Self-Referential Structure

A distinctive structural feature of the theory is that its operators are **self-referential in three categorically distinct modes**. The closure operator $\mathrm{Cl}_t$ completes the field using its own values (self-completion). The distinction operator $\mathbf{D}_t$ compares the field against its own complement $1 - u_t$ (self-contrast). The co-belonging operator $\mathbf{C}_t$ integrates the field's global structure through its own weighted adjacency (self-integration). This triple-mode operator triad — not self-referentiality per se, which is routine in nonlinear variational problems — is what gives the theory its mathematical identity. The definition graph is acyclic (operators are defined from the field); the computation graph is cyclic (the field is updated using the operators it defines). The distinction between these two senses of dependence is critical and is maintained throughout the specification (Commitment Note CN3, Section 14).

---

*[Sections 3–15 continue in subsequent drafts.]*
