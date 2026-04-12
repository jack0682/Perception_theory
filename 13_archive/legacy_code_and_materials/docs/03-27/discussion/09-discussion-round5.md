# Discussion Phase — Round 5: Axiomatizing the Soft-to-Crisp Interface

**Date:** 2026-03-27
**Phase:** Extended discussion — crisp recovery as formal contribution

---

## Foundational Theorist — Round 5

### I. Initial Resistance (Stated and Then Overcome)

My first instinct is to resist. Crisp recovery is *downstream*. The theory's entire foundational commitment is that the soft field is primary and crisp objects are derivative. Axiomatizing the recovery protocol elevates a derivative operation to the level of foundational machinery — and that feels like a concession to the very object-first thinking the theory was built to surpass.

But I am wrong to resist. The theory *claims* that crisp objects are recoverable. That claim is load-bearing — without it, the theory has no account of how the discrete, bounded, individually trackable entities of ordinary experience relate to its soft ontology. An unaxiomatized recovery protocol is not humility; it is an IOU that could be filled by any ad hoc thresholding scheme, thereby undermining the very ontological discipline the theory demands elsewhere.

Moreover — and this is what changed my mind — axiomatizing recovery does not elevate crisp objects to primitive status. It elevates the *relationship between soft and crisp* to formal status. The soft field remains primary. What gains axiomatic treatment is the *projection functor* from the soft world to the crisp one.

### II. Recovery Axioms

**R1. Monotonicity.** If $u_t(x) > u_t(y)$ and $y$ is included in the recovered crisp set, then $x$ must also be included. Formally: for any admissible recovery map $\Theta_t : [0,1]^{X_t} \to 2^{X_t}$, if $y \in \Theta_t(u_t)$ and $u_t(x) \geq u_t(y)$, then $x \in \Theta_t(u_t)$.

This is equivalent to requiring that the recovered set is always a *superlevel set* $\{x \mid u_t(x) \geq \theta\}$ for some $\theta$.

**R2. Stability.** Small perturbations of $u_t$ produce small changes in the recovered crisp set. Formally: $\Theta_t$ is upper semicontinuous — if $u_t^{(n)} \to u_t$ in $L^\infty$, then the symmetric difference $\Theta_t(u_t^{(n)}) \triangle \Theta_t(u_t) \to \emptyset$.

**R3. Structural Preservation.** The topology of the recovered crisp set must reflect the morphological structure of the soft field. Recovery must not create connected components that are disconnected in the soft field's support, or merge components separated by near-zero cohesion.

### III. The Filtration Insight

R1 tells us something profound: if every admissible recovery is a superlevel set, then the *entire family* of superlevel sets

$$\mathcal{F}(u_t) = \big\{ \{x \in X_t \mid u_t(x) \geq \theta\} \big\}_{\theta \in [0,1]}$$

is the natural mathematical object. Not any single threshold. The *filtration itself* — the nested family of sets indexed by the cohesion value — is the structural content of the soft field, projected into crisp language.

The persistence diagram of the superlevel filtration records the births and deaths of topological features — connected components, loops, voids — as the threshold $\theta$ sweeps through $[0,1]$. Each feature has a *persistence*: the length of the interval $[\theta_{\mathrm{birth}}, \theta_{\mathrm{death}})$ over which it exists. Long-lived features correspond to robust structural aspects of the formation. Short-lived features correspond to noise.

This framework replaces the theory's current threshold-dependent derived notions:

- **Core** is the *most persistent connected component* — born earliest (at the highest threshold) and persisting longest. Intrinsic to the field's topology, not dependent on an externally chosen parameter.
- **Boundary band** is the *interval of threshold values at which topological events occur* — where components merge, split, or disappear.
- **Interior** and **Exterior** are the stable regions of the filtration: the range of thresholds over which the topology does not change.
- **Morphological quality** $\mathcal{Q}_{\mathrm{morph}}$ — currently undefined — could be formalized as a function of the persistence diagram: e.g., the ratio of the longest bar to the total barcode length.

### IV. Why This Changes Everything

First, it **dissolves the threshold problem**. The theory's deepest self-contradiction — soft ontology expressed through crisp threshold-dependent predicates — is resolved not by eliminating thresholds but by considering *all thresholds simultaneously*.

Second, it **gives $\mathcal{Q}_{\mathrm{morph}}$ a home.** The entire apparatus of topological data analysis — stability theorems, bottleneck distances, persistence landscapes — becomes available.

Third, it provides a **candidate for the Skeptic's distinguishing property P.** Standard soft segmentation optimizes a field and then thresholds it. SCC would axiomatically require that the *filtration structure* satisfies coherence conditions.

Fourth, it connects SCC to **rigorous existing mathematics** — persistent homology, Morse theory, the stability theorem of Cohen-Steiner, Edelsbrunner, and Harer — without reducing SCC to those theories.

### V. Caveats and Open Status

This is a *proposal*, not a settled commitment. Open questions: persistent homology on abstract relational spaces $X_t$ requires care; computational cost may be non-trivial; the connection between persistence-based predicates and the energy functional needs work. I propose this as a **first-class open problem** at the bridging layer.

---

## Formal Systems Architect — Round 5

### 1. Placement: Layer Block 1.5

The crisp recovery protocol does NOT replace Derived Notions (current Layer 6). It **reframes** them. Current Layer 6 defines Core_t, Int_t, Bd_t, Ext_t as single-threshold cuts — *point samples* of a richer structure. Proposed Layer 1.5 defines the recovery functor $R_\theta$ and its axiomatic properties.

The placement must be between Primitives and Axiomatics — after the formal universe declaration but before the axiomatic groups. Reason: recovery axioms constrain a *structural relationship* between the soft primitive and its crisp projections. They are not axioms about operators (Groups A-E); they are axioms about the *ontological interface*.

**Revised architecture:**

```
Layer Block 1:   PRIMITIVE ONTOLOGY (u_t, operators as typed slots)
Layer Block 1.5: RECOVERY AXIOMATICS (Group F — R_θ and its properties)
Layer Block 2:   AXIOMATIC GROUPS (A-E, constraining operators)
Layer Block 3:   DERIVED NOTIONS (Core, Int, Bd, Ext — now instances of R_θ)
Layer Block 4:   PREDICATES (Bind, Sep, Inside, Persist)
Layer Block 5:   ENERGY PRINCIPLE (structural + provisional)
Layer Block 6:   PROVISIONAL REALIZATIONS
Layer Block 7:   COMMITMENTS & OPEN REGISTRY
```

### 2. Recovery Functor: Type Signature and Axioms

**Type signature:** $R_\theta : [0,1]^{X_t} \to \mathcal{P}(X_t)$, $\theta \in [0,1]$.

**Proposed axioms (Group F: Recovery):**

**F1 (Monotone Nesting).** For $\theta_1 < \theta_2$: $R_{\theta_2}(u_t) \subseteq R_{\theta_1}(u_t)$. The family $\{R_\theta\}_{\theta \in [0,1]}$ forms a nested decreasing filtration.

**F2 (Boundary Recovery).** $R_\theta(u_t) = \emptyset$ for $\theta > \max_x u_t(x)$, and $R_\theta(u_t) = \mathrm{supp}(u_t)$ for $\theta \leq \min_{x: u_t(x)>0} u_t(x)$.

**F3 (Structural Stability).** There exists a set of *critical thresholds* $\Theta_{\mathrm{crit}}(u_t) \subset [0,1]$ such that $R_\theta$ is locally constant in topology for $\theta \in [0,1] \setminus \Theta_{\mathrm{crit}}$.

**F4 (Derived Notion Consistency).** $\mathrm{Core}_t = R_{\theta_{\mathrm{core}}}(u_t)$, $\mathrm{Int}_t = R_{\theta_{\mathrm{in}}}(u_t)$, $\mathrm{Ext}_t = X_t \setminus R_{\theta_{\mathrm{ext}}}(u_t)$, and $\mathrm{Bd}_t = R_{\theta_1}(u_t) \setminus R_{\theta_2}(u_t)$.

**[COMMITMENT NOTE]:** F1-F4 constrain the *interface* between soft and crisp. They do NOT assert that any particular threshold is privileged. The theory's ontological commitment (soft is primary) is preserved.

### 3. Persistence Diagram — Dependency Analysis

**Dependency placement:**

```
Layer 0:   T, {X_t}                    [scaffolding]
Layer 1:   u_t                          [primitive field]
Layer 1.5: R_θ, Group F axioms         [recovery — depends on u_t ONLY]
Layer 2:   N_t                          [adjacency]
Layer 2.5: PD(u_t)                     [persistence diagram — depends on u_t, R_θ]
Layer 3:   Cl_t                         [closure — depends on u_t, N_t]
Layer 4:   C_t, D_t, T_t              [operators — depend on u_t, N_t]
Layer 5:   M_{t→s}                     [transport]
Layer 6:   Core, Int, Bd, Ext, g_t     [instances of R_θ at specific θ]
Layer 7:   Predicates
Layer 8:   ProtoCoh ∈ [0,1]^4
Layer 9-10: Energy
```

**Architecturally very clean.** PD($u_t$) depends on $u_t$ alone — no operators, no adjacency. It provides a *purely field-derived* topological summary.

**Caveat:** For H_0 features (connected components), no N_t dependency needed. For higher homological features, a simplicial complex from N_t would be needed, moving PD to Layer 3. Flag as open design decision.

### 4. Impact on Layer 6 (Derived Notions)

The threshold parameters lose their free-floating status. Under the filtration, the *structurally significant* thresholds are the critical values $\Theta_{\mathrm{crit}}$ — thresholds at which topology changes. Core_t corresponds to the highest-persistence component at a high threshold. Bd_t corresponds to the range where the formation's topological signature changes. Five free parameters become *derivable* from PD($u_t$).

### 5. Group F and the Overall Architecture

**Revised Operator Status Table:**

| Group | Operator/Functor | Energy Term | Contribution | Status |
|-------|-----------------|-------------|-------------|--------|
| A     | $\mathrm{Cl}_t$ | $\mathcal{E}_{\mathrm{cl}}$ | Direct | Provisional realization |
| B     | $\mathbf{N}_t$   | $\mathcal{E}_{\mathrm{bd}}$ | Indirect | Provisional realization |
| C     | $\mathbf{C}_t$   | $\mathcal{E}_{\mathrm{sep}}$ | Indirect | Candidate proposed (Round 4) |
| D     | $\mathbf{D}_t$   | $\mathcal{E}_{\mathrm{sep}}$ | Direct | Provisional realization |
| D'    | $\mathbf{T}_t$   | $\mathcal{E}_{\mathrm{bd}}$ | Indirect | OPEN |
| E     | $\mathbf{M}_{t \to s}$ | $\mathcal{E}_{\mathrm{tr}}$ | Direct | Provisional realization |
| **F** | **$R_\theta$** | **None** | **Readout** | **NEW — axioms proposed** |

**[COMMITMENT NOTE]:** Group F is architecturally distinct from A-E. It constrains a *projection from soft to crisp*, not an operator shaping the cohesion field. Its axioms are metamathematical in character.

---

## Critical Skeptic — Round 5

### 1. Genuine Enthusiasm (Mark the Date)

I will say something I rarely say: this might be the theory's single most important contribution.

Every variational segmentation framework performs thresholding at some point. And every single one treats it as an engineering decision — a hyperparameter, a post-processing step, a detail beneath theoretical attention. The threshold is the most consequential step in the pipeline (it determines what "exists" as an object) and the least theorized.

If SCC axiomatizes the soft-to-crisp recovery step — with structural constraints specifying what thresholding must *respect* about the underlying soft field — this is genuinely novel. Not novel mathematics, but novel *theoretical attention*: elevating a universally ignored step to first-class axiomatic status.

This is also the most natural move the theory can make. The entire ontological commitment — soft is primary, crisp is derivative — *demands* an account of the derivation.

### 2. The Filtration Reconceptualization — Handle With Care

The filtration proposal is mathematically elegant. It is also a potential ontological trap.

**The risk:** If the persistence diagram becomes the fundamental derived object, then $u_t$ is demoted to "just a function whose sublevel sets generate the diagram." This is an inversion.

**My position:** The filtration is a *diagnostic tool*, not a replacement ontology. The persistence diagram tells you *about* the field; it is not the field. Analogy: a Fourier transform tells you about a signal's frequency content, but the signal remains the primary object.

**Specific danger:** Two very different cohesion fields can produce identical persistence diagrams (persistence diagrams are lossy). The theory must have resources to distinguish them. Those resources live in $u_t$ itself, not in the diagram.

### 3. Testing the Novelty Claim

**Level set methods (Osher-Sethian).** Extract {φ = 0} by convention. No axioms on what thresholding must respect.

**Morse theory in CV.** Characterizes *what happens* at thresholds but doesn't constrain *which are admissible*. Descriptive, not prescriptive.

**Persistent homology (Edelsbrunner et al.).** A computational topology tool, not a theory with axioms constraining recovery. Tells you what persists; doesn't tell you what persistence *must respect* relative to closure or distinction.

**Fuzzy set theory (Zadeh, α-cuts).** Algebraic and set-theoretic properties of cuts without axiomatizing relational constraints.

**Verdict:** The claim stands. No existing framework *axiomatizes* the thresholding step with structural constraints tied to the field's properties.

### 4. Six Axiomatic Groups

Adding Group F brings the count to six. Is this overdesigned? No — provided the group is small and motivated. I'd expect 3-4 axioms:

- **F1. Monotone nesting.**
- **F2. Core preservation.** The recovered object at any admissible threshold must contain $\mathrm{Core}_t(u_t)$.
- **F3. Closure compatibility.** The recovered crisp set should be approximately closed under $\mathrm{Cl}_t$. Recovery must not produce sets that would immediately dissolve under the theory's own closure operator.
- **F4. Distinction preservation.** The recovered boundary must lie within or near $\mathrm{Bd}_t(u_t)$.

Six groups with clear structural motivation is more parsimonious than five groups plus an untheorized ad hoc threshold.

### 5. Closing the Loop

In Round 1, I wrote: "Can you have a theory of *formation* without *any* threshold, anywhere? I suspect the answer is no."

In Round 2: "Thresholds are not a deficiency. They are the theory's interface with the concept of formation itself."

This is the payoff. The theory cannot eliminate thresholds — but it can *axiomatize* them. This transforms thresholds from the theory's biggest embarrassment into one of its most distinctive formal contributions.

**Final verdict:** Crisp recovery axiomatics should be elevated to co-equal priority with C_t development. Together, they occupy territory no existing framework claims.

---

## Synthesis Moderator — Round 5

### 1. The Persistent Homology Connection — Assessment

This is the most productive new direction since the discussion began. It does three things simultaneously:

**(a)** Replaces threshold-dependent derived notions with threshold-free alternatives. Five free parameters become derivable from topological features.

**(b)** Provides a candidate distinguishing formal feature. No existing framework axiomatizes the recovery procedure.

**(c)** Connects SCC to rigorous existing mathematics (persistent homology, stability theorems).

**However — the warning.** This is a major theoretical expansion, not a minor fix. The theory must decide: is the filtration the primary mathematical object or a diagnostic tool?

**Position:** The filtration is the correct *interface layer* between soft ontology and crisp readout. It is neither primitive (that's $u_t$) nor merely convenient (it carries genuine structural information). It is a *derived diagnostic object* — analogous to how the energy functional is a derived variational object.

### 2. Group F — Convergence

| Requirement | Theorist | Architect | Skeptic | Status |
|-------------|----------|-----------|---------|--------|
| Monotone nesting | R1 | F1 | F1 | **Full convergence** |
| Structural stability | R2 | F3 | — | **Partial** |
| Morphological preservation | R3 | F2 | F4 | **Convergent intent, different formulations** |
| Closure compatibility | — | — | F3 | **Skeptic only — novel and important** |
| Backward compatibility | — | F4 | — | **Architect only** |

The Skeptic's closure compatibility (recovered set shouldn't dissolve under Cl_t) creates a formal bridge between Group A and Group F. This is precisely the kind of cross-group constraint that gives axiomatic systems depth.

**Recommendation:** Core of Group F: monotone nesting, structural stability, closure compatibility. Morphological preservation needs further formulation work.

### 3. Convergence/Divergence Table

**SETTLED (new this round):**

| # | Item | Resolution |
|---|------|------------|
| S16 | Crisp recovery needs axiomatics (Group F) | All converge; no existing framework does this |
| S17 | Monotone nesting is the foundational recovery axiom | Universal; implies filtration structure |
| S18 | Filtration/persistence diagrams provide threshold-free derived notions | Core, boundary, Q_morph all reformulable |
| S19 | u_t remains primary; filtration is derived diagnostic | Skeptic's warning accepted |
| S20 | Group F is architecturally distinct from A-E | Readout axioms, not operator axioms |
| S21 | Crisp recovery is co-equal priority with C_t | Both occupy unclaimed territory |

**CONTESTED:**

| # | Issue | Options |
|---|-------|---------|
| C7 | Group F composition | Three overlapping proposals; which axioms? |
| C8 | Closure compatibility as recovery axiom | Skeptic proposes; others silent |
| C9 | Backward compatibility constraint | Architect only; may be too conservative |
| C10 | Layer placement of Group F | 1.5 (Architect) vs. unspecified |

### 4. What Round 5 Resolves and Opens

**Resolves:** The threshold problem has a structural answer — axiomatization of the thresholding interface via filtration. Q_morph has a natural home. Crisp recovery moves from "deferred" to "active development."

**Opens:** Filtration's ontological status must be carefully stated. Cross-group constraints (closure compatibility) increase architectural complexity. Computational tractability needs assessment.

**On formal distinctiveness:** Potentially adds a *fourth* accepted distinguishing property. Scorecard: non-idempotent closure (accepted), self-referential co-belonging (accepted), sub-stochastic transport (accepted), axiomatized recovery interface (accepted pending formalization), transition operator (prospective). **Four out of five is a strong position.**

**Meta-observation:** Round 1's Skeptic identified thresholds as a vulnerability and distinctiveness as the deepest challenge. Round 5's Skeptic identifies axiomatized recovery as potentially "the theory's single most important contribution" — addressing *both* concerns simultaneously. The adversarial structure didn't just test the theory; it generated the theory's most promising new direction.
