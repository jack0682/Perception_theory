# Canonical Specification of Soft Cognitive Cohesion

---

## 1. Status Note

This document is the canonical human-readable formal specification of the current state of the theory of Soft Cognitive Cohesion. It declares the primitive ontology, the formal universe, the axiomatic groups, the derived predicates, and the minimal energy principle that jointly constitute the theory as it now stands.

The document separates stable theoretical commitments—those principles that define the identity of the theory and are not subject to routine revision—from open design choices that remain underdetermined but are constrained by the canonical commitments. Provisional concrete operator forms are presented explicitly as currently favored realizations, not as permanently fixed definitions.

This specification is intended to serve as the authoritative reference for future formalization, implementation, and theoretical extension. It is written to be readable by mathematicians, theoretical cognitive scientists, and system designers alike.

---

## 2. Foundational Orientation

The theory of Soft Cognitive Cohesion does not begin from objects. It does not presuppose that the world is first given as a collection of discrete, bounded, individually identifiable things. It does not assume that perception starts with already-separated entities whose properties then need to be classified. Any framework that begins from such assumptions starts too late: it inherits the results of a prior process of individuation without accounting for how that individuation was achieved.

The foundational commitment of this theory is that coherent formation precedes discrete objecthood. What is first encountered—whether in sensory experience, in structured data, or in any relational medium—is not a set of labeled objects but a field of graded cohesion: regions of varying internal support, continuity, and mutual reinforcement, from which object-like stability may or may not eventually emerge.

Cohesion is therefore given as a graded field, not as a binary partition. A soft cohesion field $u_t : X_t \to [0,1]$ assigns to each site in a relational support space a degree of participation in a cohesive formation. This degree is not a probability of class membership. It is an intensity of cohesive participation: how strongly a site is sustained by, and contributes to, the internal relational organization of a formation.

Objects, in this theory, are not primitives. They are later-read stabilized formations: cohesive fields that have achieved sufficient closure (self-support under relational completion), sufficient distinction (asymmetry with respect to their exterior), sufficient morphological articulation (a structured transition from core to boundary to exterior), and sufficient temporal persistence (structural inheritance of their cohesive organization across time). An object is not an input to the theory; it is, at most, a distinguished output—a formation that satisfies all the conditions of proto-cohesion robustly and stably.

Relational structure is prior to discrete individuation. What makes a formation cohere is not an intrinsic property of isolated points but a pattern of local mutual support: sites that reinforce one another, that belong together not because of a shared label but because their relational configuration is self-sustaining. Internality, boundary, and persistence are consequences of this structured cohesion, not presupposed properties of pre-given objects.

---

## 3. Formal Universe and Primitive Structure

The formal universe of the soft theory is a structured tuple

$$
\mathfrak{C}^{\mathrm{soft}} = \Big( T,\ \{X_t\}_{t \in T},\ \{u_t\}_{t \in T},\ \{\mathrm{Cl}_t\}_{t \in T},\ \{\mathbf{N}_t, \mathbf{C}_t, \mathbf{D}_t, \mathbf{T}_t\}_{t \in T},\ \{\mathbf{M}_{t \to s}\}_{t,s \in T} \Big)
$$

whose components are defined as follows.

### 3.1. Temporal Index Set

$T$ is a linearly ordered set of temporal indices. In the minimal case $T$ may be a finite discrete sequence $\{0, 1, 2, \ldots, n\}$; in the general case it may be any totally ordered set equipped with a notion of succession. The theory does not require continuous time, but it does require that temporal order be well-defined.

### 3.2. Sensory or Relational Support

For each $t \in T$, the set $X_t$ is the sensory or relational support at time $t$. It is the space of sites over which cohesion is defined. In a visual domain, $X_t$ might be a lattice of spatial positions; in a more abstract domain, it might be any finite or countable set of relational loci. The theory does not require that $X_t$ be Euclidean or even metric, though particular realizations may impose such structure.

The sets $X_t$ are allowed to vary with $t$. This generality is necessary because the relational support available to a cognitive or perceptual system may itself change over time.

### 3.3. Soft Cohesion Field

For each $t \in T$, the function

$$
u_t : X_t \to [0,1]
$$

is the soft cohesion field at time $t$. This is the primitive carrier of pre-objective cohesion. The value $u_t(x)$ represents the degree to which site $x$ participates in the cohesive formation at time $t$. A value near $1$ indicates full cohesive participation (deep interiority); a value near $0$ indicates effective exteriority; intermediate values indicate transitional or boundary participation.

The cohesion field $u_t$ is not a posterior probability, not a class membership score, and not a segmentation mask. It is the primary ontological entity of the theory: the graded field from which all further structure—closure, distinction, boundary, persistence—is derived.

### 3.4. Soft Closure Operator

For each $t \in T$, the operator

$$
\mathrm{Cl}_t : [0,1]^{X_t} \to [0,1]^{X_t}
$$

is the soft closure operator. It maps a cohesion field to its relationally completed form: the field that would result if every site's cohesion were updated to reflect the support it receives from its relational neighborhood. Closure is the mechanism by which cohesion becomes self-sustaining. Its formal properties are specified in Axiomatic Group A below.

### 3.5. Soft Adjacency

For each $t \in T$, the function

$$
\mathbf{N}_t : X_t \times X_t \to [0,\infty)
$$

is the soft adjacency kernel. It encodes the local relational support structure: $\mathbf{N}_t(x,y)$ measures the degree to which sites $x$ and $y$ are relationally proximate or locally coupled. Adjacency is the substrate from which closure, co-belonging, and boundary sensitivity are built.

### 3.6. Soft Co-belonging

For each $t \in T$, the function

$$
\mathbf{C}_t : X_t \times X_t \to [0,1]
$$

is the soft co-belonging operator. It measures the degree to which two sites participate in the same cohesive formation. Co-belonging is distinct from adjacency: two sites may be adjacent without co-belonging (if they lie on opposite sides of a cohesive boundary), and two sites may co-belong without being adjacent (if they are linked through a chain of mutually supporting intermediate sites). The precise functional form of $\mathbf{C}_t$ remains partially open; its conceptual role is fixed.

### 3.7. Soft Distinction

For each $t \in T$, the operator

$$
\mathbf{D}_t : X_t \times [0,1]^{X_t} \to [0,1]
$$

is the soft distinction operator. Given a site $x$ and a reference field (typically the complement $1 - u_t$, representing the exterior), $\mathbf{D}_t(x; 1-u_t)$ measures the degree to which site $x$ is asymmetrically positioned with respect to the exterior. Distinction is not mere local contrast; it is a structural asymmetry of the cohesive interior relative to the surrounding non-cohesive field as a whole.

### 3.8. Soft Transition Operator

For each $t \in T$, the operator

$$
\mathbf{T}_t : X_t \to [0,1]
$$

(or more generally a map that depends on the cohesion field and its local structure) is the soft transition operator. It characterizes the directional or structural nature of the transition across the boundary band. Where distinction measures the fact of asymmetry, transition characterizes the form of that asymmetry: whether the passage from interior to exterior is gradual or abrupt, isotropic or directional.

### 3.9. Temporal Transport Kernel

For each pair $t, s \in T$, the function

$$
\mathbf{M}_{t \to s} : X_t \times X_s \to [0,1]
$$

is the temporal transport or inheritance kernel. The value $\mathbf{M}_{t \to s}(x,y)$ represents the degree to which the cohesive role of site $x$ at time $t$ is inherited by site $y$ at time $s$. This kernel is the mechanism by which temporal identity is defined: the same formation through time is the formation whose cohesive core is structurally inherited under transport.

Temporal transport need not be one-to-one. It may be one-to-many (a cohesive region at time $t$ may distribute its inheritance across multiple sites at time $s$), many-to-one (multiple sites at time $t$ may converge onto a single inheritor), partial (some cohesive content may dissipate without successor), or probabilistic. What is required is that transport preserve the structural organization of cohesion, not that it preserve individual site identities.

---

## 4. Why the Soft Form Is Primary

It is essential to state explicitly, and with full theoretical force, that the soft system is not a relaxation, an approximation, or a computational convenience layered over a more fundamental crisp system. The soft system is the deeper and more original layer. The crisp system, if needed at all, is a derivative that may be recovered from the soft system by thresholding or collapse—but that recovery is a secondary operation, not a return to foundations.

The reasons for this primacy are structural, not merely pragmatic.

**Pre-objective cohesion is intrinsically graded.** Before a formation has stabilized into a recognizable object, its cohesion admits degrees. Some regions participate strongly in the formation; others participate weakly or ambiguously; still others lie on the boundary between belonging and not-belonging. A framework that begins from crisp sets $A_t \subseteq X_t$ cannot represent this graded pre-objective phase without immediately distorting it into a binary decision that has not yet been made.

**Inside and outside are not initially sharply separated.** The distinction between the interior of a formation and its exterior is, at the pre-objective stage, a matter of degree. There is typically a transition band—a region in which cohesion tapers from interior intensity to exterior quiescence. A crisp set has no such transition band; it has only membership and non-membership. The soft field $u_t$ naturally represents the full morphology of this transition.

**Closure is emergent rather than fully completed.** In the crisp case, closure is typically idempotent: applying the closure operator twice yields the same result as applying it once. But at the pre-objective level, closure is better understood as a stabilizing tendency rather than an already-completed operation. A cohesion field may be approximately self-supporting without being perfectly closed. The soft framework accommodates this by not imposing idempotence as a primitive axiom.

**External asymmetry is field-relative rather than pointwise.** Distinction—the structural asymmetry that separates a formation from its surround—is defined with respect to the exterior field as a whole, not as a pointwise property. In the soft system, this field-relative character is natural: $\mathbf{D}_t(x; 1-u_t)$ depends on the entire complementary field. In a crisp system, this dependence collapses to a much coarser boundary/non-boundary distinction that loses the graded structure of the asymmetry.

**The crisp system is recoverable but not foundational.** Given a soft cohesion field $u_t$, one may recover a crisp subset by thresholding: $A_t = \{x \in X_t \mid u_t(x) \geq \theta\}$ for a chosen threshold $\theta$. One may also recover crisp boundaries, crisp interiors, and crisp identity predicates. But these crisp entities are projections of the richer soft structure, not the other way around. The theory moves from soft to crisp, not from crisp to soft.

---

## 5. Derived Geometric and Morphological Notions

From the primitive cohesion field $u_t$ and the operators defined above, several derived notions of geometric and morphological significance can be constructed.

### 5.1. Core

The core of a cohesion field at time $t$ is the set of sites whose cohesive participation exceeds a high threshold:

$$
\mathrm{Core}_t(u_t) = \{x \in X_t \mid u_t(x) \geq \theta_{\mathrm{core}}\}
$$

where $\theta_{\mathrm{core}}$ is a parameter close to $1$. The core represents the deep interior of the formation: the sites that are most strongly and stably integrated into the cohesive organization. The core plays a distinguished role in temporal persistence, because it is the structural nucleus whose inheritance under transport defines the identity of the formation through time. A formation that loses its core has, in the relevant sense, ceased to persist.

### 5.2. Interior

The interior of a cohesion field is defined by a lower threshold:

$$
\mathrm{Int}_t(u_t) = \{x \in X_t \mid u_t(x) \geq \theta_{\mathrm{in}}\}
$$

where $\theta_{\mathrm{in}} < \theta_{\mathrm{core}}$. The interior includes the core together with the surrounding region of strong but not maximal cohesive participation. The interior is the region within which the formation's relational structure is substantially self-supporting.

### 5.3. Boundary Band

The boundary of a cohesion field is not a sharp line but a transition region—a band of sites where cohesion is intermediate between full interior participation and effective exteriority:

$$
\mathrm{Bd}_t(u_t) = \{x \in X_t \mid \theta_1 < u_t(x) < \theta_2\}
$$

where $\theta_1$ and $\theta_2$ are parameters chosen so that $0 < \theta_1 < \theta_2 < 1$. Within the boundary band, cohesion is neither fully established nor fully absent. This is the region of maximal structural transition—where the formation's internal relational support gives way to the exterior.

The boundary band may also be characterized in gradient terms. A local gradient indicator may be defined as

$$
g_t(x; u) = \sum_{y} \mathbf{N}_t(x,y)\, |u_t(x) - u_t(y)|
$$

which measures the rate of cohesion change at site $x$ relative to its relational neighborhood. Sites at which $g_t(x; u)$ is large are sites of rapid transition—boundary sites in the morphological sense.

The boundary band is not a codimension-one manifold in general. It is a volumetric region whose thickness and structure reflect the morphology of the formation. A formation with a thick boundary band transitions gradually from inside to outside; a formation with a thin boundary band has a more abrupt transition. Both are legitimate; the theory does not impose a preference.

### 5.4. Exterior

The exterior is defined by complementarity:

$$
\mathrm{Ext}_t(u_t) = \{x \in X_t \mid u_t(x) \leq \theta_{\mathrm{ext}}\}
$$

where $\theta_{\mathrm{ext}}$ is a threshold near $0$. The exterior is the domain against which the formation's distinction is measured.

---

## 6. Axiomatic Groups

The axioms of the theory are organized into five groups, corresponding to the five major structural concerns: closure, adjacency, co-belonging, distinction and transition, and temporal transport.

### Group A. Soft Closure

The soft closure operator $\mathrm{Cl}_t : [0,1]^{X_t} \to [0,1]^{X_t}$ is subject to the following axiomatic properties.

**A1. Weak Extensivity (Self-Support).** For all $u \in [0,1]^{X_t}$ and all $x \in X_t$,

$$
\mathrm{Cl}_t(u)(x) \geq u(x) \quad \text{whenever } u(x) > 0 \text{ and } u \text{ has local relational support at } x.
$$

This axiom states that closure does not diminish cohesion at sites that are already cohesive and locally supported. It is a self-support condition: cohesion that is relationally sustained tends to be maintained or strengthened under closure. The condition is weakened relative to classical extensivity ($\mathrm{Cl}(A) \supseteq A$) because sites that lack local support may legitimately lose cohesion under closure.

**A2. Monotonicity.** For all $u, v \in [0,1]^{X_t}$,

$$
u \leq v \implies \mathrm{Cl}_t(u) \leq \mathrm{Cl}_t(v)
$$

where the inequality is pointwise. If one field is everywhere at least as cohesive as another, its closure is also everywhere at least as cohesive. This ensures that the closure operator respects the ordering structure of cohesion fields.

**A3. Stabilization Tendency.** Iterated application of $\mathrm{Cl}_t$ tends toward a fixed point:

$$
\|\mathrm{Cl}_t^{(n+1)}(u) - \mathrm{Cl}_t^{(n)}(u)\| \to 0 \quad \text{as } n \to \infty
$$

for suitable norms. This axiom replaces the classical requirement of idempotence ($\mathrm{Cl}_t^2 = \mathrm{Cl}_t$) with a weaker convergence condition. The motivation is that pre-objective closure is not instantaneously complete; it is a stabilizing process that tends toward but does not necessarily achieve exact self-reproduction in a single step. Full idempotence may emerge as a consequence of stabilization in well-behaved cases, but it is not imposed as a primitive axiom.

**Interpretive Remark.** The deliberate omission of primitive idempotence is a signature commitment of the theory. Classical topological closure is idempotent by definition. But the present theory operates at a level prior to completed topological structure: at the level where closure is still a dynamic tendency, not yet an accomplished fact. Imposing idempotence at the primitive level would presuppose that the cohesive formation has already been fully completed, which would undermine the theory's foundational ambition to describe pre-objective emergence.

### Group B. Soft Adjacency

The soft adjacency kernel $\mathbf{N}_t : X_t \times X_t \to [0,\infty)$ is subject to the following properties.

**B1. Nonnegativity.** For all $x, y \in X_t$,

$$
\mathbf{N}_t(x,y) \geq 0.
$$

Adjacency is a nonnegative quantity representing relational proximity or coupling strength.

**B2. Symmetry.** In the minimal (undirected) case,

$$
\mathbf{N}_t(x,y) = \mathbf{N}_t(y,x).
$$

Symmetry may be relaxed in extensions that model directed relational structure, but the canonical theory adopts symmetry as the default.

**B3. Locality.** $\mathbf{N}_t(x,y)$ is negligible or zero for pairs $(x,y)$ that are not relationally proximate. Adjacency encodes local structure, not global equivalence. Two sites may both participate strongly in the same formation without being directly adjacent, if they are connected through intermediate sites.

**B4. Non-Transitivity.** Adjacency is not required to be transitive. The relation "$x$ is adjacent to $y$ and $y$ is adjacent to $z$" does not entail that $x$ is adjacent to $z$. This is essential: adjacency is a local relation, and global coherence (co-belonging) must be built from local adjacency, not assumed as a primitive property of adjacency itself.

**Interpretive Remark.** Adjacency provides the substrate over which closure, co-belonging, and boundary sensitivity are defined. It represents the minimal relational structure that the theory requires: a notion of which sites are locally coupled. All further structure is constructed from this local coupling in combination with the cohesion field.

### Group C. Soft Co-belonging

The soft co-belonging operator $\mathbf{C}_t : X_t \times X_t \to [0,1]$ measures the degree to which two sites participate in the same cohesive formation.

**C1. Dependence on Cohesion and Adjacency.** $\mathbf{C}_t(x,y)$ must depend on the cohesion field $u_t$ and on the adjacency structure $\mathbf{N}_t$. It is not a standalone relation but a derived or partially derived quantity that reflects the global pattern of cohesive organization.

**C2. Distinction from Adjacency.** Co-belonging is not reducible to adjacency. Two sites may be adjacent without co-belonging (they may lie on opposite sides of a boundary) and may co-belong without being adjacent (they may be connected through a chain of mutually supporting sites). Co-belonging captures the global structural fact of joint participation in a single cohesive formation.

**C3. Graded and Reflexive.** $\mathbf{C}_t(x,x) = u_t(x)$ (or a monotone function thereof): a site's co-belonging with itself is at least as strong as its cohesive participation. Co-belonging between distinct sites is graded and may take any value in $[0,1]$.

**Open Status.** The precise functional form of $\mathbf{C}_t$ is not yet canonically fixed. Its conceptual role—measuring joint participation in a single cohesive formation—is determined. Candidate realizations may involve diffusion-like propagation along the cohesion field, spectral methods on the adjacency graph weighted by cohesion, or other mechanisms that capture non-local structural integration. The canonical theory constrains but does not yet uniquely determine this operator.

### Group D. Distinction and Transition

#### D1. Soft Distinction

The soft distinction operator $\mathbf{D}_t(x; 1-u_t)$ measures the degree of structural asymmetry at site $x$ with respect to the exterior field $1 - u_t$.

**D-Ax1. Exterior Sensitivity.** $\mathbf{D}_t(x; 1-u_t)$ depends not only on the local value $u_t(x)$ but on the relational configuration of the exterior field in the neighborhood of $x$. Distinction is not a pointwise property of the cohesion field alone; it is a relational property that requires reference to the complementary (exterior) field.

**D-Ax2. Asymmetry.** Distinction is high when the relational support that site $x$ receives from the interior field $u_t$ substantially exceeds the support it receives from the exterior field $1 - u_t$. This asymmetry is the structural basis for individuation: a formation is distinguished from its surround precisely to the degree that its interior sites are asymmetrically supported relative to the exterior.

**D-Ax3. Boundary Sensitivity.** Distinction may incorporate sensitivity to the local gradient of cohesion. Sites in the transition band, where cohesion is changing rapidly, may exhibit enhanced or diminished distinction depending on the functional form. The canonical theory requires that distinction be structurally aware of the boundary morphology, not blind to it.

**Interpretive Remark.** Distinction is not merely "being different from one neighbor." It is a global structural property: the asymmetry of a site's relational environment with respect to the entire exterior domain. Without distinction, a cohesion field would be a diffuse intensity pattern with no principled inside/outside articulation. Distinction is what prevents the theory from collapsing into a featureless gradient.

#### D2. Soft Transition

The soft transition operator $\mathbf{T}_t$ characterizes the structural nature of the transition across the boundary band.

**T-Ax1. Boundary Localization.** $\mathbf{T}_t$ takes its significant values in or near the boundary band $\mathrm{Bd}_t(u_t)$. Away from the boundary—in the deep interior and the deep exterior—the transition operator should be negligible.

**T-Ax2. Directional or Structural Content.** $\mathbf{T}_t$ encodes not merely the fact that a transition exists but its character: the rate of change, the directional profile, the symmetry or asymmetry of the passage from inside to outside.

**Open Status.** The exact operator class for $\mathbf{T}_t$ remains an open design choice. Candidate formulations may involve gradient fields of $u_t$, curvature-like quantities derived from the boundary band, or directional derivatives with respect to the adjacency structure. The canonical theory fixes the conceptual role—characterizing boundary morphology—while leaving the precise realization underdetermined.

**Joint Role of Distinction and Transition.** Distinction and transition jointly prevent the theory from admitting degenerate solutions. Without distinction, a constant field $u_t \equiv c$ for $c \in (0,1)$ would trivially satisfy closure and adjacency conditions; distinction forces the field to exhibit structural contrast with its exterior. Without transition, a field could be distinguished but morphologically unstructured at its boundary; transition forces the boundary to have articulable form.

### Group E. Temporal Transport and Persistence

The temporal transport kernel $\mathbf{M}_{t \to s} : X_t \times X_s \to [0,1]$ is subject to the following axiomatic properties.

**E1. Soft Stochasticity.** For each $x \in X_t$,

$$
\sum_{y \in X_s} \mathbf{M}_{t \to s}(x,y) \leq 1.
$$

The inequality (rather than equality) permits partial dissipation: a site's cohesive content may be only partially inherited, with some fraction lost or unaccounted for. Strict equality would enforce perfect conservation of cohesive content, which is too strong for the general case.

**E2. Non-Injectivity.** $\mathbf{M}_{t \to s}$ need not be one-to-one. Multiple sites at time $t$ may transport to the same site at time $s$ (convergence), and a single site at time $t$ may transport to multiple sites at time $s$ (divergence). This generality is necessary because cohesive formations may merge, split, expand, or contract through time.

**E3. Core Inheritance.** The transport kernel must preferentially preserve the cohesive core. That is, for sites $x$ in $\mathrm{Core}_t(u_t)$, the inherited cohesion at the receiving sites should remain high:

$$
\sum_{y \in X_s} \mathbf{M}_{t \to s}(x,y)\, u_s(y) \geq \delta \quad \text{for some } \delta > 0
$$

whenever the formation persists from $t$ to $s$. This axiom ensures that temporal identity is not preserved merely by name or index but by the actual inheritance of structurally significant cohesion.

**E4. Structural Sensitivity.** $\mathbf{M}_{t \to s}(x,y)$ should depend on structural features of $x$ at time $t$ and $y$ at time $s$—not merely on spatial proximity. In particular, it should be sensitive to the representational or feature-level similarity between the two sites, so that transport respects the qualitative character of the cohesive formation, not just its spatial location.

**Interpretive Remark.** Temporal identity in this theory is not pointwise identity. It is not the assertion that "the same pixels" or "the same coordinates" are occupied at successive times. It is the assertion that the structurally significant core of a cohesive formation—the deep interior that defines the formation's relational organization—is inherited under transport. The same thing through time is the thing whose core persists through structural succession, even if its boundary shifts, its shape deforms, or its spatial locus migrates. This conception of identity is closer to the philosophical notion of genidentity than to the computational notion of a tracking ID.

---

## 7. Proto-Cohesion and Pre-Objective Cohesion

The central predicate of the theory is proto-cohesion: the condition under which a family of cohesion fields $\mathbf{u} = (u_t)_{t \in W}$ over a temporal window $W \subseteq T$ constitutes a genuine pre-objective cohesive formation.

### 7.1. Component Predicates

The proto-cohesion predicate is defined in terms of four component conditions, each of which corresponds to one of the core structural requirements of the theory.

**Binding.** The predicate $\mathsf{Bind}_t(u_t)$ asserts that the cohesion field at time $t$ is approximately self-supporting under closure:

$$
\mathsf{Bind}_t(u_t) \iff \|u_t - \mathrm{Cl}_t(u_t)\| \leq \varepsilon_{\mathrm{cl}}
$$

for a suitable norm and tolerance $\varepsilon_{\mathrm{cl}} > 0$. A field that satisfies binding coheres rather than scattering: its cohesive content is sustained by its own relational structure. A field that violates binding is dissipative—its cohesion would diminish under relational completion, indicating that it does not hold together as a genuine formation.

**Separation.** The predicate $\mathsf{Sep}_t(u_t)$ asserts that the cohesion field is structurally distinguished from its exterior:

$$
\mathsf{Sep}_t(u_t) \iff \frac{1}{|\mathrm{Int}_t|} \sum_{x \in \mathrm{Int}_t(u_t)} \mathbf{D}_t(x; 1-u_t) \geq \delta_{\mathrm{sep}}
$$

for a threshold $\delta_{\mathrm{sep}} > 0$. A field that satisfies separation is not merely a diffuse intensity pattern; it exhibits genuine asymmetry with respect to its exterior. The interior sites, on average, are structurally distinguishable from their non-cohesive surround.

**Inside-Structure.** The predicate $\mathsf{Inside}_t(u_t)$ asserts that the cohesion field possesses internal morphological articulation—a discernible core, a transition band, and a structured passage from inside to outside:

$$
\mathsf{Inside}_t(u_t) \iff \mathrm{Core}_t(u_t) \neq \emptyset \;\wedge\; \mathrm{Bd}_t(u_t) \neq \emptyset \;\wedge\; \mathcal{Q}_{\mathrm{morph}}(u_t) \geq \mu_{\mathrm{in}}
$$

where $\mathcal{Q}_{\mathrm{morph}}(u_t)$ is a morphological quality measure that captures the coherence of the core-boundary-exterior stratification. A field that satisfies inside-structure is not amorphously diffuse (core without boundary) nor artificially sharp (boundary without interior gradient); it has the layered morphology characteristic of a genuine cohesive formation.

**Persistence.** The predicate $\mathsf{Persist}_W(\mathbf{u})$ asserts that the cohesive organization is structurally inherited across time throughout the window $W$:

$$
\mathsf{Persist}_W(\mathbf{u}) \iff \forall\, t, s \in W \text{ with } t < s,\quad \sum_{x \in \mathrm{Core}_t} \sum_{y \in \mathrm{Core}_s} \mathbf{M}_{t \to s}(x,y)\, u_s(y) \geq \rho_{\mathrm{persist}}
$$

for a threshold $\rho_{\mathrm{persist}} > 0$. A family of fields that satisfies persistence maintains structural continuity of its cohesive core through time. The core at each time inherits substantial cohesive content from the core at earlier times under the transport kernel. This is the condition that underwrites temporal identity: the formation at time $s$ is the same formation as at time $t$ because the structurally significant part of the earlier formation has been inherited by the later one.

### 7.2. The Proto-Cohesion Predicate

The full proto-cohesion predicate for a temporal window $W$ is:

$$
\mathsf{ProtoCoh}^{\mathrm{soft}}_W(\mathbf{u}) \iff \Big( \forall\, t \in W,\ \mathsf{Bind}_t(u_t) \;\wedge\; \mathsf{Sep}_t(u_t) \;\wedge\; \mathsf{Inside}_t(u_t) \Big) \;\wedge\; \mathsf{Persist}_W(\mathbf{u}).
$$

A family of cohesion fields satisfies proto-cohesion if and only if, at every time in the window, the field is self-supporting (binding), structurally distinguished from its exterior (separation), and morphologically articulated (inside-structure), and furthermore the cohesive organization is inherited across time (persistence).

**Interpretive Remark.** Proto-cohesion is the central concept of the theory. It is the formal expression of what it means for something to "hold together as a coherent something" prior to discrete objecthood. A proto-cohesive formation is not yet an object in the traditional sense: it may have soft boundaries, graded interiority, and only approximate closure. But it is genuinely cohesive: it binds, it distinguishes itself, it has internal structure, and it persists. It is the pre-objective precursor of objecthood—the formation from which, under further stabilization and sharpening, a discrete object may eventually be read off.

---

## 8. Minimal Energy Principle

The theory admits a variational formulation in which cohesive formations are characterized as approximate minimizers of a canonical energy functional. The minimal energy principle provides a unified optimization target that encodes all four structural requirements—closure, separation, morphology, and transport—as energetic penalties.

The canonical energy over a temporal window $W$ is:

$$
\mathcal{E}(\mathbf{u}) = \lambda_{\mathrm{cl}}\, \mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\, \mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\, \mathcal{E}_{\mathrm{bd}} + \lambda_{\mathrm{tr}}\, \mathcal{E}_{\mathrm{tr}}
$$

where $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}} > 0$ are weighting coefficients that control the relative importance of each structural requirement. The four terms are defined as follows.

### 8.1. Closure Term

$$
\mathcal{E}_{\mathrm{cl}}(u_t) = \sum_{x \in X_t} \big( u_t(x) - \mathrm{Cl}_t(u_t)(x) \big)^2
$$

This term penalizes deviation of the cohesion field from its relationally completed form. Minimizing $\mathcal{E}_{\mathrm{cl}}$ drives the field toward self-support: a state in which the cohesion at every site is consistent with the relational support it receives from its neighborhood. A field that minimizes this term is approximately closed—it sustains itself under its own relational structure.

### 8.2. Separation Term

$$
\mathcal{E}_{\mathrm{sep}}(u_t) = \sum_{x \in X_t} u_t(x) \big( 1 - \mathbf{D}_t(x; 1-u_t) \big)
$$

This term penalizes cohesive sites that are not structurally distinguished from the exterior. Minimizing $\mathcal{E}_{\mathrm{sep}}$ drives the field toward a state in which every site that participates in the formation is asymmetrically positioned relative to the non-cohesive surround. A field that minimizes this term exhibits clear structural contrast between interior and exterior.

### 8.3. Boundary and Morphology Term

$$
\mathcal{E}_{\mathrm{bd}}(u_t) = \alpha \sum_{x,y \in X_t} \mathbf{N}_t(x,y) \big( u_t(x) - u_t(y) \big)^2 + \beta \sum_{x \in X_t} u_t(x)^2 \big( 1 - u_t(x) \big)^2
$$

where $\alpha, \beta > 0$ are morphological parameters.

The first sub-term is a smoothness penalty: it discourages arbitrary high-frequency oscillation in the cohesion field by penalizing large differences between adjacent sites. This ensures that the field has spatial coherence—that cohesive regions are connected and continuous rather than fragmented and noisy.

The second sub-term is a double-well penalty: it penalizes intermediate values of cohesion, favoring fields that are either close to $0$ (exterior) or close to $1$ (interior). This ensures that the field develops a structured morphology with discernible inside and outside regions rather than remaining at a featureless intermediate level.

Together, the two sub-terms drive the field toward a state with smooth, well-defined interior regions, coherent boundary bands, and clear exterior—the morphological signature of a genuine cohesive formation.

### 8.4. Transport Term

$$
\mathcal{E}_{\mathrm{tr}}(u_t, u_s) = \sum_{x \in X_t} \sum_{y \in X_s} \mathbf{M}_{t \to s}(x,y)\, \omega(u_t(x), u_s(y)) \big( u_s(y) - u_t(x) \big)^2
$$

where $\omega(a, b) : [0,1]^2 \to [0,\infty)$ is a weighting function that emphasizes inheritance at high-cohesion sites (for example, $\omega(a,b) = a \cdot b$ or $\omega(a,b) = \min(a,b)$). This term penalizes discontinuities in cohesive content under temporal transport. Minimizing $\mathcal{E}_{\mathrm{tr}}$ drives the field toward a state in which the structurally significant part of the formation is smoothly inherited from one time to the next.

### 8.5. Why Four Distinct Terms

The four energy terms correspond to four conceptually independent structural requirements:

- **Closure** ensures internal relational self-support.
- **Separation** ensures structural contrast with the exterior.
- **Boundary/morphology** ensures coherent spatial articulation.
- **Transport** ensures temporal inheritance of cohesive organization.

These requirements are logically independent: a field may be closed but undistinguished, distinguished but morphologically incoherent, morphologically coherent but temporally discontinuous, and so forth. Collapsing the four terms into fewer would obscure these independent requirements and reduce the theory's capacity to diagnose which structural condition a given formation fails to satisfy. The four-term structure must therefore be preserved in the canonical formulation.

---

## 9. Provisional Concrete Operator Forms

This section presents currently favored functional realizations of the canonical operators. These are adopted because they jointly support self-sustaining cohesion, exterior asymmetry, and non-deterministic structural inheritance in a computationally tractable manner. They are presented explicitly as provisional: they are the best current candidates, not permanently fixed definitions. Future work may refine, replace, or generalize these forms while remaining within the canonical framework.

### 9.1. Local Relation Kernel and Aggregation

The adjacency structure is instantiated through a local relation kernel $K_t : X_t \times X_t \to [0,\infty)$ satisfying

$$
K_t(x,y) \geq 0, \qquad K_t(x,y) = K_t(y,x).
$$

The associated aggregation operator is defined as

$$
(P_t f)(x) = \frac{\sum_{y} K_t(x,y)\, f(y)}{\sum_{y} K_t(x,y) + \varepsilon}
$$

where $\varepsilon > 0$ is a small stabilization constant that prevents division by zero at isolated sites. The operator $P_t$ computes a locally weighted average of any field $f$ with respect to the relational kernel $K_t$. It is the basic building block from which closure, distinction, and other operators are constructed.

### 9.2. Closure Candidate

The currently adopted closure operator is

$$
\mathrm{Cl}_t(u)(x) = \sigma\!\Big( a_{\mathrm{cl}} \big( (1 - \eta_{\mathrm{cl}})\, u(x) + \eta_{\mathrm{cl}}\, (P_t u)(x) - \tau_{\mathrm{cl}} \big) \Big)
$$

where:

- $\sigma$ is a sigmoid function (e.g., the logistic function $\sigma(z) = 1/(1 + e^{-z})$),
- $a_{\mathrm{cl}} > 0$ controls the steepness of the closure response,
- $\eta_{\mathrm{cl}} \in [0,1]$ controls the balance between self-retention and neighborhood aggregation,
- $\tau_{\mathrm{cl}}$ is a threshold that determines the level of combined support required for cohesion to be maintained.

This form blends a site's own cohesion with the aggregated cohesion of its neighbors, applies a threshold, and maps the result through a sigmoid to keep the output in $[0,1]$. The parameter $\eta_{\mathrm{cl}}$ controls how much closure depends on neighborhood support versus self-retention: at $\eta_{\mathrm{cl}} = 0$, closure reduces to a sigmoidal self-map; at $\eta_{\mathrm{cl}} = 1$, it reduces to pure neighborhood aggregation.

### 9.3. Distinction Candidate

The currently adopted distinction operator is

$$
\mathbf{D}_t(x; 1-u) = \sigma\!\Big( a_D \big( (P_t u)(x) - \lambda_D\, (P_t(1-u))(x) \big) + b_D\, g_t(x; u) - \tau_D \Big)
$$

where:

- $a_D > 0$ controls the sensitivity of the asymmetry comparison,
- $\lambda_D > 0$ scales the exterior aggregation relative to the interior aggregation,
- $b_D \geq 0$ controls the contribution of local gradient information,
- $\tau_D$ is a threshold,
- $g_t(x; u) = \sum_{y} K_t(x,y)\, |u(x) - u(y)|$ is the local gradient indicator.

This form computes distinction as the sigmoidal response to a comparison between interior support (how much cohesion is aggregated from the neighborhood) and exterior support (how much non-cohesion is aggregated from the neighborhood), optionally modulated by boundary sensitivity through the gradient term. A site has high distinction when its neighborhood is predominantly cohesive and the surrounding non-cohesive field is substantially weaker.

### 9.4. Transport Candidate

The currently adopted temporal transport kernel is

$$
\mathbf{M}_{t \to s}(x,y) = \frac{ \exp\!\Big( -\dfrac{\|y - \Psi_{t \to s}(x)\|^2}{2\sigma_M^2} - \gamma_M \|\varphi_t(x) - \varphi_s(y)\|^2 \Big) }{ \sum_{y'} \exp\!\Big( -\dfrac{\|y' - \Psi_{t \to s}(x)\|^2}{2\sigma_M^2} - \gamma_M \|\varphi_t(x) - \varphi_s(y')\|^2 \Big) + \varepsilon }
$$

where:

- $\Psi_{t \to s} : X_t \to X_s$ is a predicted spatial correspondence (e.g., from motion estimation or optical flow),
- $\sigma_M > 0$ controls the spatial tolerance of the transport,
- $\varphi_t(x)$ is a feature representation of site $x$ at time $t$ (capturing qualitative or structural characteristics),
- $\gamma_M > 0$ controls the importance of feature similarity relative to spatial proximity,
- $\varepsilon > 0$ prevents degenerate normalization.

This form defines transport as a soft assignment: each site $x$ at time $t$ distributes its inheritance across sites at time $s$ according to a combined measure of spatial proximity to the predicted correspondence and feature similarity. The softmax normalization ensures that the transport weights sum to at most $1$ (with the $\varepsilon$ term absorbing any residual), allowing partial dissipation.

The feature term $\gamma_M \|\varphi_t(x) - \varphi_s(y)\|^2$ is what makes transport structurally sensitive rather than merely spatial: it ensures that cohesive content is preferentially inherited by sites that not only occupy the right spatial location but also possess the right qualitative character.

---

## 10. Structural Interpretation

This section states, in disciplined theoretical prose, the core claims of the theory about the nature of cohesion, individuation, and persistence.

**Existence is not first given as objecthood.** The theory asserts that the most basic level of structured encounter—whether perceptual, cognitive, or computational—does not consist of already-individuated objects. What is first given is a field of graded relational intensity from which coherent formations may or may not emerge. Objects are late achievements, not starting points.

**Cohesion precedes object individuation.** Before a region of the world can be singled out as a distinct individual—before it can be named, classified, tracked, or reasoned about as a discrete entity—it must first hold together as a cohesive formation. This holding-together is the work of the cohesion field: the graded pattern of mutual relational support that makes a formation cohere rather than scatter. Individuation presupposes cohesion; it does not produce it.

**A genuine cohesive formation must exhibit internal support, exterior distinction, and temporal inheritance.** Mere intensity is not cohesion. A random pattern of high values in a field does not constitute a formation. A genuine formation is one that is self-supporting under its own relational structure (closure), structurally asymmetric with respect to its exterior (distinction), internally articulated with core, boundary, and exterior strata (morphology), and inherited through time as a structurally continuous organization (persistence). These four conditions jointly define the concept of proto-cohesion.

**The same thing through time is not a pointwise identical set of sites.** Temporal identity is not spatial identity. A formation that moves, deforms, partially dissolves, and reconstitutes itself may still be the same formation—provided that its structurally significant core is inherited under transport. What persists is not a rigid arrangement of points but a relational organization: the pattern of mutual support that defines the formation's cohesive character. This conception of identity is structural and dynamic, not extensional and static.

**The theory does not reduce to segmentation, clustering, or tracking.** Although the formal apparatus may superficially resemble techniques from image segmentation, graph clustering, or multi-object tracking, the theoretical intent is fundamentally different. Segmentation presupposes objects and seeks to delineate them; this theory seeks to explain how anything becomes delineable at all. Clustering groups pre-given data points; this theory asks how coherent groupings emerge from unstructured relational fields. Tracking follows identified objects through time; this theory asks what it means for something to be the same thing through time in the first place.

---

## 11. Fixed Commitments and Open Degrees of Freedom

### 11.1. Fixed Commitments

The following principles constitute the stable core of the theory and are not subject to routine revision:

1. **Primacy of soft cohesion fields.** The primitive ontological entity is the graded cohesion field $u_t : X_t \to [0,1]$, not a crisp subset, a class label, or an instance ID.

2. **Relational priority.** Relations are prior to objecthood. Cohesion, closure, distinction, and persistence are all defined in terms of relational structure, not as intrinsic properties of isolated entities.

3. **Non-primitive status of crisp objects.** Crisp objects may be recovered from the soft system by thresholding or stabilization, but they are derivative constructs, not foundational primitives.

4. **Non-primitive idempotence of closure.** The closure operator is subject to a stabilization tendency but is not required to be idempotent at the primitive level.

5. **Four-term minimal energy structure.** The canonical energy comprises four conceptually independent terms—closure, separation, boundary/morphology, and transport—which must remain distinct.

6. **Structural rather than pointwise persistence.** Temporal identity is defined as structural inheritance of the cohesive core under transport, not as pointwise identity of sites.

7. **Boundary as transition band.** Boundary is a graded transition region, not necessarily a sharp codimension-one frontier.

8. **Distinction as exterior asymmetry.** Distinction is a structural asymmetry with respect to the exterior field, not a local contrast measure.

### 11.2. Open Design Choices

The following aspects of the theory are constrained by the canonical commitments but not yet uniquely determined:

1. **Final functional form of $\mathbf{C}_t$.** The co-belonging operator has a fixed conceptual role but no single canonical realization.

2. **Exact operator class for $\mathbf{T}_t$.** The transition operator's structural role is fixed; its precise mathematical form is open.

3. **Closure regularity conditions.** The exact smoothness, continuity, or compactness conditions on $\mathrm{Cl}_t$ beyond the stated axioms remain to be specified.

4. **Threshold recovery rules.** The precise protocol by which crisp objects are extracted from soft cohesion fields (choice of thresholds, stability criteria, hysteresis rules) is not canonically fixed.

5. **Dynamic update laws.** The theory as stated is variational (characterizing formations as energy minimizers) rather than dynamical (specifying how fields evolve in time). The derivation of update laws—whether gradient descent, evolutionary optimization, or other mechanisms—is a future formalization layer.

6. **Variational versus evolutionary optimization strategies.** The canonical energy admits optimization by multiple strategies, including gradient-based variational methods and population-based evolutionary methods (such as xNES). The choice of optimization strategy is an implementation decision, not a theoretical commitment.

7. **Multi-formation interaction.** The canonical specification addresses a single cohesive formation. The interaction between multiple co-existing formations—competition, occlusion, merging, splitting—requires an extension of the theory that is not yet canonically specified.

The distinction between fixed and open is not the distinction between important and unimportant. The open choices are constrained and consequential; they are open because the theory has not yet accumulated sufficient evidence or argument to fix them uniquely.

---

## 12. Open Problems and Next Formalization Layers

The following problems remain unresolved and constitute the primary agenda for the next stages of theoretical development.

**Canonical form of co-belonging.** The operator $\mathbf{C}_t$ is conceptually essential—it captures the non-local structural fact of joint participation in a formation—but no single functional form has yet been demonstrated to be uniquely appropriate. Candidate approaches include diffusion kernels on the cohesion-weighted adjacency graph, spectral representations of the graph Laplacian weighted by $u_t$, and iterated aggregation operators. A canonical choice must be motivated by both theoretical considerations (compatibility with closure and distinction) and empirical performance.

**Canonical form of the transition operator.** The operator $\mathbf{T}_t$ requires a formal treatment that captures the directional and structural character of the boundary band. This may involve gradient fields, curvature estimates, or second-order neighborhood statistics. The canonical form must be compatible with the boundary morphology term in the energy and must provide information not already captured by the gradient indicator $g_t$.

**Derivation of dynamic update laws.** The current theory characterizes proto-cohesive formations as minimizers of the canonical energy but does not specify how cohesion fields evolve from arbitrary initial conditions toward such minimizers. A complete theory requires dynamical update laws—differential equations, discrete maps, or optimization algorithms—that govern the temporal evolution of $u_t$ within a single time step. These laws should ideally be derivable from the energy principle (e.g., as gradient flows) rather than imposed ad hoc.

**Crisp recovery.** The theory claims that crisp objecthood is derivable from the soft system, but it does not yet specify the precise recovery protocol. Questions include: What thresholding scheme is appropriate? Should thresholds be global or locally adaptive? Is hysteresis needed to prevent oscillation near threshold? Can the recovery protocol itself be derived from the energy principle rather than imposed externally?

**Existence and stability theorems.** It remains to be shown that the canonical energy admits minimizers under reasonable assumptions on the operators and the support spaces; that these minimizers satisfy the proto-cohesion predicate; and that they are stable under perturbation of the cohesion field, the relational kernel, or the transport structure. Such theorems would place the theory on rigorous mathematical foundations and clarify the conditions under which proto-cohesive formations are guaranteed to exist.

**Identifiability.** Given a family of cohesion fields that satisfies proto-cohesion, is the underlying formation uniquely determined (up to reparametrization), or can distinct formations yield the same observable cohesion pattern? This is a question about the information-theoretic sufficiency of the formal apparatus.

**Connection to optimization procedures.** The canonical energy is, in principle, amenable to optimization by gradient-based methods, evolutionary search (including xNES and related natural gradient strategies), or hybrid approaches. The formal connection between the canonical specification and specific optimization algorithms—convergence guarantees, parameter sensitivity, computational complexity—constitutes a separate layer of formalization that bridges the theory and its computational realization.

**Multi-formation theory.** The extension to multiple co-existing formations raises questions of competition (how formations divide the support space), interaction (how adjacent formations influence each other's boundaries and distinction), and multiplicity (how the number of formations is determined). These questions require a multi-field extension of the theory, possibly involving a family $(u_t^{(1)}, u_t^{(2)}, \ldots)$ of cohesion fields with coupling terms in the energy.

---

## 13. Closing Summary

This canonical specification establishes the formal structure of the theory of Soft Cognitive Cohesion in its current state. The theory is grounded in a single foundational commitment: that pre-objective cohesion, given as a graded relational field, is the proper starting point for any account of how coherent formations emerge, individuate, and persist. From this commitment, the theory develops a formal universe in which closure captures relational self-support, distinction captures exterior asymmetry, morphological structure captures the articulation of core, boundary, and exterior, and temporal transport captures the structural inheritance that constitutes persistence through time. The proto-cohesion predicate unifies these four requirements into a single formal condition on families of cohesion fields, and the minimal energy principle provides a variational characterization of formations that satisfy this condition. The theory now stands as a mathematically structured ontology of pre-objective cohesion in which relation, closure, distinction, morphology, and temporal inheritance jointly define the emergence of object-like persistence from a graded, relational, and fundamentally soft foundation.
