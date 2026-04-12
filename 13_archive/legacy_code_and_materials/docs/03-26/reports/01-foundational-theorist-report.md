# Foundational Theorist Report: Analysis of Soft Cognitive Cohesion Specification

**Role:** Foundational Theorist (Teammate 1)
**Task:** Analyze modules for theoretical fidelity
**Date:** 2026-03-26

---

## A. FOUNDATIONAL ASSUMPTIONS AND RISKS MEMO

### Module 1: Formal Universe & Primitives (Section 3)

**What it secretly assumes:**

1. **Container-space realism.** The formal universe posits $X_t$ as a pre-given "sensory or relational support" space over which the cohesion field is defined. But this quietly assumes that the domain of individuation is itself already individuated — the *sites* are discrete, enumerable, pre-given loci. The theory claims relational priority over objecthood, yet the relational field $u_t$ is defined *over* a space of already-distinguished points. This is the theory's deepest hidden assumption: **the substrate is crisp even though the field is soft.** Sites $x \in X_t$ are atoms; they have identity conditions (they can be arguments to functions, elements of sums). The theory's own ontological starting point — "existence is not first given as objecthood" — is violated at the level of the support space.

    *Counter-hypothesis:* One might argue this is a necessary formal concession — you must write functions *on* something. But the theory should explicitly acknowledge this as a foundational limitation, not leave it implicit. A truly radical version would define cohesion over a pre-topological relational structure where sites themselves have graded identity.

2. **Temporal ordering is externally imposed.** $T$ is a linearly ordered set given from outside the theory. Time is not emergent from cohesion dynamics; it is a container parameter. This is a significant metaphysical commitment that the theory does not flag. If coherent formation precedes objecthood, does temporal succession also precede objecthood, or is it co-emergent? The theory silently assumes the former.

3. **The [0,1] codomain is a hidden commitment.** Mapping to the unit interval imposes a total ordering on degrees of cohesion. This assumes cohesion is *scalar* — a single graded intensity. But the theory's own language sometimes suggests cohesion is multi-dimensional (a site might participate strongly in closure but weakly in distinction). The scalar codomain forecloses vector-valued or lattice-valued cohesion fields, which might be more faithful to the theory's relational spirit.

4. **The tuple structure presupposes modular decomposition.** Listing the formal universe as a structured tuple $\mathfrak{C}^{\mathrm{soft}} = (T, \{X_t\}, \{u_t\}, \{\mathrm{Cl}_t\}, \ldots)$ presupposes that these components are separable. But if relational priority is genuine, perhaps the closure operator and the cohesion field are not independently specifiable — perhaps they co-constitute. The tuple format imports a set-theoretic modularity that may not be faithful to the theory's holistic commitments.

**Ontological drift risk: MODERATE-HIGH.** The support space $X_t$ is doing quiet object-theoretic work. Sites function as proto-objects.

---

### Module 2: Derived Geometric/Morphological Notions (Section 5)

**What it secretly assumes:**

1. **Threshold-dependent definitions are crypto-crisp.** Core, Interior, Boundary Band, and Exterior are all defined via threshold inequalities: $\{x \mid u_t(x) \geq \theta\}$. These are crisp sets derived from the soft field. The theory explicitly endorses this derivation direction (soft -> crisp), but the *immediate* introduction of threshold-based crisp sets in Section 5 — before the axiomatics are even stated — creates a structural temptation. Subsequent formal apparatus (proto-cohesion predicates, energy terms) heavily depends on these crisp derived sets. The risk: **the theory's working vocabulary becomes quietly crisp even though its ontology is nominally soft.**

2. **The gradient indicator $g_t(x;u)$ smuggles in a metric-like assumption.** The formula $g_t(x;u) = \sum_y \mathbf{N}_t(x,y)|u_t(x) - u_t(y)|$ assumes that the absolute difference $|u_t(x) - u_t(y)|$ is meaningful. This presupposes that the codomain $[0,1]$ has a natural metric structure, and that "rate of cohesion change" is well-defined. For a theory that claims not to require metric structure on $X_t$, this is a quiet importation of metric assumptions on the *value* space.

3. **Morphological vocabulary borrows from spatial geometry.** Terms like "core," "interior," "boundary band," "exterior" carry strong geometric connotations. The theory warns against reducing to segmentation, but the derived notions *are* segmentation vocabulary. The risk is not that they exist (they must, for downstream use) but that they are introduced without sufficient warning that they are convenient projections, not ontological categories.

**Ontological drift risk: MODERATE.** The threshold-based definitions are necessary but dangerously convenient. They should be more clearly quarantined as derived projections.

---

### Module 3: Axiomatic Group A — Closure

**What it secretly assumes:**

1. **A1's conditioning on "local relational support" is underspecified.** The axiom states $\mathrm{Cl}_t(u)(x) \geq u(x)$ "whenever $u(x) > 0$ and $u$ has local relational support at $x$." But "local relational support" is not formally defined. This is the axiom most vulnerable to silent resolution — any implementation will need to define this phrase, and different definitions will yield different theories. The axiom is conceptually rich but formally incomplete.

2. **A2 (Monotonicity) assumes pointwise ordering is the right ordering.** The pointwise partial order on $[0,1]^{X_t}$ is natural but not inevitable. If cohesion is genuinely relational, one could imagine orderings that respect structural features (e.g., a field with lower maximum but better-connected support might be "more cohesive" in a structural sense). Monotonicity with respect to pointwise ordering is a commitment to *intensive* rather than *structural* comparison.

3. **A3 (Stabilization Tendency) assumes convergence in norm.** The formulation $\|\mathrm{Cl}_t^{(n+1)}(u) - \mathrm{Cl}_t^{(n)}(u)\| \to 0$ assumes a norm topology on the field space. Which norm? This is left open but consequential. Convergence in $L^\infty$ is very different from convergence in $L^1$. The choice of norm encodes a decision about what kind of deviation counts as significant.

**Faithfulness assessment:** This module is *largely faithful* to the theory's commitments. The deliberate omission of idempotence is the theory's signature move, and it is well-executed. The main risk is the underspecification of A1, which creates a gap that implementations will fill silently.

---

### Module 4: Axiomatic Group B — Adjacency

**What it secretly assumes:**

1. **Symmetry (B2) is adopted as default but may betray relational asymmetry.** Many relational structures are inherently directional (e.g., one site may support another without reciprocation). The theory acknowledges this with "may be relaxed" but adopts symmetry as canonical. This is a non-trivial commitment that favors spatial/geometric intuitions over more general relational ones.

2. **B3 (Locality) and B4 (Non-Transitivity) are conceptually excellent but in tension.** If adjacency is strictly local and non-transitive, then *all* global structure must be built from local adjacency via closure and co-belonging. This is conceptually right but places enormous structural weight on the closure and co-belonging operators.

3. **The codomain $[0, \infty)$ is unbounded.** Unlike cohesion (bounded in $[0,1]$), adjacency values are unbounded above. This creates a normalization issue: how do adjacency magnitudes interact with cohesion values?

**Faithfulness assessment:** HIGH. This is one of the most theoretically faithful modules. The non-transitivity axiom (B4) is particularly important and well-motivated.

---

### Module 5: Axiomatic Group C — Co-belonging

**What it secretly assumes:**

1. **C3 (Reflexivity condition $\mathbf{C}_t(x,x) = u_t(x)$) ties co-belonging to self-cohesion.** This is elegant but assumes that self-co-belonging is identical to cohesive participation. A boundary site torn between formations might have high cohesion but low self-co-belonging.

2. **The "Open Status" is the theory's most honest moment — but also its greatest vulnerability.** Co-belonging must do the work of converting local adjacency into global structural integration. Without a canonical form, the theory cannot make specific predictions about what counts as "the same formation."

    *Hypothesis:* The difficulty in canonicalizing $\mathbf{C}_t$ may indicate that co-belonging is not a binary operator between pairs of sites but a *higher-order* structural property — something closer to a simplicial complex or a sheaf-theoretic notion of local-to-global consistency.

3. **C1's dependence requirement is stated but not axiomatized.** Saying $\mathbf{C}_t$ "must depend on" $u_t$ and $\mathbf{N}_t$ is a meta-constraint, not a formal axiom.

**Faithfulness assessment:** MODERATE. Conceptually faithful but formally thin.

---

### Module 6: Axiomatic Group D — Distinction & Transition

**What it secretly assumes:**

1. **Distinction's dependence on $1 - u_t$ as "the exterior" presupposes a single-formation context.** If multiple formations coexist, the exterior of formation A is not simply $1 - u_t^A$. The axiom's structure *commits* to single-formation distinction in a way that may be difficult to generalize.

2. **D-Ax2 (Asymmetry) uses interior/exterior support comparison — but "support" is undefined at this level.** This conflates the axiomatic level with the realization level.

3. **The Transition Operator ($\mathbf{T}_t$) has inconsistent type signatures.** In Section 3.8, it is typed as $\mathbf{T}_t : X_t \to [0,1]$, but the parenthetical suggests the actual type is more complex. This ambiguity conceals a conceptual uncertainty about what transition *is*.

**Faithfulness assessment:** MODERATE-HIGH. Distinction is well-motivated. Transition is underdeveloped — it reads more like a placeholder than a worked-out concept.

---

### Module 7: Axiomatic Group E — Transport & Persistence

**What it secretly assumes:**

1. **E1 (Soft Stochasticity) imposes a conservation-like constraint.** Requiring $\sum_y \mathbf{M}_{t \to s}(x,y) \leq 1$ imports probabilistic/measure-theoretic machinery. The theory claims persistence is structural inheritance, not probabilistic transition, yet the axiom is essentially a probability axiom.

    *Counter-hypothesis:* The sub-stochastic constraint is necessary to prevent transport from "creating" cohesion ex nihilo. This is defensible as an energy-conservation principle, not a probabilistic one.

2. **E3 (Core Inheritance) depends on the threshold-derived crisp set $\mathrm{Core}_t$.** This is the most significant crypto-crisp intrusion in the axiomatics. A foundational axiom that defines temporal identity depends on a threshold-derived set.

    *Hypothesis for resolution:* Reformulate E3 in purely soft terms — e.g., as a weighted integral condition: $\sum_{x,y} \mathbf{M}_{t \to s}(x,y) \cdot \phi(u_t(x)) \cdot \phi(u_s(y)) \geq \rho$.

3. **E4 (Structural Sensitivity) is an axiom that resists axiomatization.** The reference to $\varphi_t(x)$ (feature representations) introduces an entirely new primitive that is nowhere declared in the formal universe.

**Faithfulness assessment:** MODERATE. Conceptually strong, but E3's dependence on crisp cores and E4's informal character weaken the formal integrity.

---

### Module 8: Proto-Cohesion Predicate (Section 7)

**What it secretly assumes:**

1. **Conjunction is the right logical connective.** The proto-cohesion predicate is Bind AND Sep AND Inside AND Persist. This prohibits trade-offs between structural conditions. **The crisp conjunction is ironic: the theory of soft cohesion uses a hard logical gate as its central predicate.**

    *Hypothesis:* A softer proto-cohesion predicate — perhaps $\mathrm{ProtoCoh} = f(\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist})$ for some monotone aggregation function $f$ — would be more consistent with the theory's own commitment to graded structure.

2. **The Separation predicate averages distinction over the interior.** Averaging is insensitive to spatial distribution: a formation could satisfy Sep by having half its interior maximally distinguished and half completely undistinguished.

3. **Inside-Structure introduces an unspecified morphological quality measure $\mathcal{Q}_{\mathrm{morph}}$.** This is a free parameter masquerading as a predicate component.

4. **Persistence is assessed over all pairs $(t,s)$ with $t < s$.** This demands *transitive* temporal inheritance, which may be too strong.

**Faithfulness assessment:** MIXED. **The conjunctive, threshold-laden form of the central predicate is the theory's most significant internal inconsistency.**

---

### Module 9: Energy Principle (Section 8)

**What it secretly assumes:**

1. **Linearity of energy combination.** The weighting coefficients $\lambda$ encode precisely the kind of inter-term dependency that the theory claims to avoid. "Independence" in the theory means *conceptual* independence, not *variational* independence. This distinction should be made explicit.

2. **The double-well penalty actively pushes toward {0,1} values.** It is a crispness-promoting term embedded in the energy of a theory that claims soft primacy. This is a significant tension.

3. **The separation energy creates a nonlinear coupling between $u_t$ and $\mathbf{D}_t$.** Since $\mathbf{D}_t$ itself depends on $u_t$, the energy landscape is highly non-convex, and the existence of minimizers is far from guaranteed.

**Faithfulness assessment:** MODERATE. The four-term structure is well-motivated, but the linear combination and the double-well potential introduce tensions with the theory's stated commitments.

---

### Module 10: Provisional Operator Forms (Section 9)

**What it secretly assumes:**

1. **The sigmoid function imports a specific nonlinear regime.** Both closure and distinction candidates use sigmoid activation — soft thresholding that encodes a specific transition shape.

2. **The transport candidate introduces feature representations $\varphi_t(x)$ as a new primitive.** These are not part of the formal universe declared in Section 3. This is the most significant layer violation in the document.

3. **The transport candidate uses predicted spatial correspondence $\Psi_{t \to s}$.** This imports optical flow / motion estimation from external computation. The transport operator, as provisionally realized, is not self-contained within the theory.

4. **The aggregation operator $P_t$ normalizes by total kernel weight.** This makes $P_t$ a weighted average, which is insensitive to the total amount of support.

**Faithfulness assessment:** MODERATE. Reasonable engineering candidates, but they introduce hidden primitives and make specific functional choices not forced by the axioms.

---

## B. PROPOSED CONCEPTUAL CORRECTIONS

### Correction 1: Acknowledge the crisp substrate problem

The theory should explicitly state that the discreteness of $X_t$ is a foundational concession, not a commitment. A future version might define cohesion over a pre-topological structure where sites themselves have graded identity.

### Correction 2: Reformulate E3 (Core Inheritance) without threshold-derived crisp sets

Replace:
$$\sum_{x \in \mathrm{Core}_t} \sum_{y \in \mathrm{Core}_s} \mathbf{M}_{t \to s}(x,y) u_s(y) \geq \rho$$

With a purely soft formulation:
$$\sum_{x \in X_t} \sum_{y \in X_s} \mathbf{M}_{t \to s}(x,y) \cdot \phi(u_t(x)) \cdot \phi(u_s(y)) \geq \rho$$

where $\phi: [0,1] \to [0,1]$ is a monotone function that emphasizes high-cohesion sites (e.g., $\phi(v) = v^p$ for $p > 1$).

### Correction 3: Soften the proto-cohesion predicate

Replace the conjunction with a graded proto-cohesion *score*: $\mathrm{ProtoCoh}(\mathbf{u}) = \min(\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist})$ where each component is a continuous $[0,1]$-valued measure.

### Correction 4: Flag the double-well potential as a crispness-promoting mechanism

The double-well term should carry an interpretive remark acknowledging the tension with soft primacy, similar to the idempotence remark.

### Correction 5: Explicitly declare the status of feature representations $\varphi_t(x)$

Either add $\{\varphi_t\}$ to the formal universe as a primitive, or explicitly state that $\varphi_t$ is an implementation-level construct.

### Correction 6: Soften the Persistence predicate's all-pairs requirement

Replace all-pairs condition with successive-pairs, or adopt a graded persistence measure that naturally decays with temporal distance.

### Correction 7: Formalize "local relational support" in A1

Give "has local relational support at $x$" a formal definition, e.g., $\sum_y \mathbf{N}_t(x,y) u(y) > 0$.

---

## C. NON-NEGOTIABLE THEORETICAL COMMITMENTS

1. **Ontological direction: soft -> crisp, never crisp -> soft.**
2. **Non-primitive idempotence.** Closure has stabilization tendency, not idempotence.
3. **Four-term energy independence.** The four terms must remain formally separable.
4. **Persistence as structural inheritance, not identity tracking.**
5. **Boundary as graded transition band.**
6. **Distinction as field-relative exterior asymmetry.**
7. **Relational priority.** No formal construct definable from $u_t(x)$ alone.
8. **The theory is not segmentation, clustering, or tracking.**
9. **Open problems must stay open.**
10. **Layer separation.** Ontology, axiomatics, provisional realizations, and implementation must remain distinct.

---

## APPENDIX: Summary of Key Tensions

| Tension | Location | Severity |
|---------|----------|----------|
| Crisp substrate ($X_t$ sites) under soft field | Module 1 | High — foundational |
| Threshold-derived crisp sets in axioms (E3, Proto-Cohesion) | Modules 7, 8 | High — self-contradictory |
| Boolean proto-cohesion predicate in a graded theory | Module 8 | High — ironic |
| Double-well potential promotes crispness | Module 9 | Moderate — tension with soft primacy |
| Feature representations $\varphi_t$ as undeclared primitive | Module 10 | Moderate — layer violation |
| "Local relational support" undefined in A1 | Module 3 | Moderate — formal incompleteness |
| Linear energy combination vs. term independence | Module 9 | Low-Moderate — conceptual confusion |
| Symmetric adjacency as default | Module 4 | Low — defensible but restrictive |
| All-pairs persistence condition | Module 8 | Low-Moderate — possibly too strong |
