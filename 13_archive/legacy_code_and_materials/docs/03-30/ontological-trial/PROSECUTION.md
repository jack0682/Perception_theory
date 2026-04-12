# PROSECUTION BRIEF: "Pre-Objective Cohesion" Is Not an Independent Ontological Layer

**Case:** *The Formalism v. The Philosophy*
**Charge:** That the theory of Soft Cognitive Cohesion claims to describe a level of reality *prior to* objecthood, when in fact its mathematical apparatus describes, detects, optimizes, and measures objects under a different name.

**Filed:** 2026-03-30

---

## Opening Statement

The theory of Soft Cognitive Cohesion makes an extraordinary philosophical claim: that it operates at a level of description *before* objects exist. It asserts that the cohesion field $u_t$ is "not a posterior probability, not a class membership score, and not a segmentation mask" (Canonical Spec v2.0, Section 3.3). It declares that "objects are late achievements, not starting points" (paper2_cogsci.tex, Section I-C).

The prosecution will demonstrate that this claim is hollow. At every level --- substrate, operators, energy, optimization, diagnostics, and interpretation --- the formalism presupposes, constructs, measures, and optimizes *objects*. The word "pre-objective" is philosophical window-dressing on a phase-field object detector. The emperor has no clothes; he merely insists that his clothes precede clothing.

---

## COUNT 1: "Pre-Objective" Is Just "Uncertain Object"

### The Claim

> "The cohesion field is not a posterior probability, not a class membership score, and not a segmentation mask." (Canonical Spec v2.0, Section 3.3)

> "What is first encountered [...] is not a set of labeled objects but a field of graded cohesion: regions of varying internal support, continuity, and mutual reinforcement." (Canonical Spec v2.0, Section 2)

### The Evidence

The diagnostic vector $\mathbf{d} = (\text{Bind}, \text{Sep}, \text{Inside}, \text{Persist}) \in [0,1]^4$ is presented as measuring "proto-cohesion" --- something supposedly prior to objecthood. But examine what each component actually measures:

| Diagnostic | What the Theory Calls It | What It Actually Is |
|-----------|--------------------------|---------------------|
| **Bind** = $1 - \|u - \text{Cl}(u)\|_2 / \sqrt{n}$ | "Self-support under closure" | Internal coherence of a bounded region --- an **object property** |
| **Sep** = $\sum u(x) D(x; 1-u) / \sum u(x)$ | "Structural distinction from exterior" | Figure-ground segregation --- **the defining property of an object** in vision science |
| **Inside** = $\mathcal{Q}_{\text{morph}}$ | "Morphological articulation" | Core-boundary-exterior stratification --- **object morphology** |
| **Persist** = core inheritance under $M_{t \to s}$ | "Temporal inheritance" | Object tracking / identity persistence --- **object identity through time** |

Consider a formation with $\mathbf{d} = (0.86, 0.93, 0.98, 1.0)$, which the implementation demonstrably produces on modest grids. This formation:
- Is 86% self-supporting (internally coherent)
- Is 93% distinguished from its surround (has clear boundaries)
- Has 98% morphological articulation (has a core, a boundary band, and an exterior)
- Is 100% temporally persistent (maintains identity through time)

**This is an object.** It has internal coherence, boundaries, morphology, and identity. Calling it "pre-objective" is like calling a duck "pre-avian" because you measured its feathers with a continuous instrument rather than counting them discretely.

The theory's own "Boolean recovery" (Spec Section 7.2) makes this explicit:

> $\mathsf{ProtoCoh}^{\text{soft}}_W(\mathbf{u}) \iff \mathsf{Bind}_t \geq \varepsilon_{\text{cl}} \wedge \mathsf{Sep}_t \geq \delta_{\text{sep}} \wedge \mathsf{Inside}_t \geq \mu_{\text{in}} \wedge \mathsf{Persist}_W \geq \rho_{\text{persist}}$

A formation that passes all four thresholds *is* an object by any reasonable standard. The diagnostic vector does not measure "pre-objective cohesion." It measures *how object-like something is*. This is object detection with a continuous confidence score, not a new ontological layer.

### Why the Defense Fails

The defense will argue that the *gradedness* is the point --- that formations can be partially cohesive, weakly separated, poorly articulated. But gradedness is not pre-objectivity. A probability distribution over object hypotheses is also graded. A neural network's activation map is also continuous. A fuzzy membership function is also $[0,1]$-valued. None of these claim to describe something "before objects." They describe *uncertain*, *partial*, or *graded* representations of objects. SCC does the same thing and calls it philosophy.

---

## COUNT 2: The Formalism Smuggles In Objecthood

### The Substrate: Pre-Individuated Sites

The theory begins from a finite set $X_t$ of individually indexed sites with a given adjacency kernel $N_t(x,y)$. The spec acknowledges this tension:

> "The discrete structure of $X_t$ no more commits the theory to pre-given objects than the discrete structure of a pixel grid commits image analysis to pre-given visual objects." (Canonical Spec v2.0, Section 2)

But this analogy defeats itself. Pixels *are* pre-given discrete entities. Image analysis *does* presuppose their individuation. The fact that interesting visual objects emerge as patterns over pixels does not mean that pixel-level individuation is ontologically innocent --- it means that *some* level of discrete individuation has already occurred before the "pre-objective" process begins. The theory's own philosophy audit concurs:

> "The theory begins with discrete points yet claims that discreteness is emergent." (paper2_cogsci.tex, Section VII-D)

### The Volume Constraint: Knowing How Much Object to Expect

The constraint $\sum_x u(x) = m$ is devastating to the "pre-objective" claim. The theory must be told *in advance* how much formation to expect. As the philosophy audit notes:

> "A formation of volume $m = 25$ in a $10 \times 10$ grid has been told, in advance, roughly how large it should be." (paper2_cogsci.tex, Section VII-D)

The spec's defense --- that this is "analogous to mass conservation in physics" (Spec Section 8.0) --- is question-begging. Mass conservation presupposes that mass already exists and has a quantity. If cohesion is truly "pre-objective," where does the budget $m$ come from? Who decides that there is $m = 25$ units worth of formation to find? This is an external specification of expected object size, smuggled in as a constraint.

Without the volume constraint, the theory admits only the trivial solution $u \equiv 0$. The spec acknowledges this:

> "Without the volume constraint, the trivial field $u \equiv 0$ is the global energy minimizer." (Canonical Spec v2.0, Section 8.0)

In other words: the theory cannot generate formations from its own dynamics. It must be externally told that formations exist and how large they are. This is not a theory of how "anything becomes a coherent something." It is a theory of how a something of pre-specified size arranges itself spatially.

### The Thresholds: Crisp Object Boundaries by Another Name

The recovery protocol (Spec Sections 5.1--5.4) defines:

- $\text{Core}_t(u_t) = \{x \in X_t \mid u_t(x) \geq \theta_{\text{core}}\}$
- $\text{Int}_t(u_t) = \{x \in X_t \mid u_t(x) \geq \theta_{\text{in}}\}$
- $\text{Bd}_t(u_t) = \{x \in X_t \mid \theta_1 \leq u_t(x) \leq \theta_2\}$
- $\text{Ext}_t(u_t) = \{x \in X_t \mid u_t(x) \leq \theta_{\text{ext}}\}$

These are crisp sets derived by thresholding. They define an object with a core, an interior, a boundary, and an exterior. The theory claims these are "derived" and not "primitive" --- but they are the only geometric concepts the theory actually uses to talk about formations. The persistence predicate uses $\text{Core}_t$ explicitly (Spec Section 7.1). The morphological quality measure uses the superlevel-set filtration, which is a family of thresholded sets. Every concrete claim the theory makes about formation structure passes through these crisp constructions.

The "primitive" graded field $u_t$ is the representation. The thresholded crisp sets are where the work gets done. This is exactly the architecture of any probabilistic object detector: compute a continuous score, threshold to get object boundaries.

---

## COUNT 3: Existing Theories Already Handle This --- Without Inventing a New Ontology

### Bayesian Segmentation

Bayesian approaches to perceptual grouping (Feldman & Singh 2001, Froyen et al. 2015) handle uncertain, graded representations of boundaries and regions. They compute posterior distributions over segmentation hypotheses, producing continuous-valued maps of boundary probability and region membership. They do this without claiming to operate at a "pre-objective" level. They simply say: "we have uncertain beliefs about object boundaries." The result is a graded, continuous representation of potential objects --- exactly what SCC produces.

### The Free Energy Principle

The spec and papers systematically mischaracterize Predictive Processing by equating it with its most rigid Bayesian formulation:

> "PP assumes a hierarchical generative model in which discrete hypotheses are tested against sensory data." (paper2_cogsci.tex, Section I-B)

But the Free Energy Principle (Friston 2010) explicitly addresses self-organization on continuous state spaces. It handles structure formation without presupposing objects. Friston's work on morphogenesis describes how structured states emerge from homogeneous conditions through free energy minimization --- *the same type of question SCC claims PP cannot address.* The philosophy audit confirms:

> "The characterization of PP as requiring 'discrete hypotheses' about 'objects, features, categories' is a selective reading of the PP literature." (A5-philosophy-audit.md, Section 4)

### IIT 4.0

Integrated Information Theory 4.0 addresses intrinsic causal structure before decomposition into objects. It asks how a system's causal architecture specifies its own structure --- a self-referential question structurally similar to SCC's.

### The Prosecution's Point

The "pre-objective" level that SCC claims to have discovered is already occupied. Other theories handle graded, uncertain, continuous representations of perceptual structure without inventing a new ontological layer. They call these representations what they are: uncertain beliefs about structure, graded activation patterns, continuous fields. SCC does the same thing but dresses it in phenomenological language.

---

## COUNT 4: "Graded" Does Not Equal "Pre-Objective"

This is the prosecution's central logical argument.

The theory's philosophical claim rests on a conflation: because the cohesion field is continuous ($u \in [0,1]$) rather than binary ($u \in \{0, 1\}$), it is supposedly "pre-objective" rather than "objective." But this conflation is a non sequitur.

Consider the following continuous-valued representations:

| Representation | Domain | Values | "Pre-Objective"? |
|---------------|--------|--------|-------------------|
| Posterior probability $P(\text{object} \mid \text{data})$ | Bayesian segmentation | $[0,1]$ | No --- uncertain object |
| Activation map $a(x)$ | Neural network | $[0,\infty)$ | No --- neural response |
| Membership function $\mu_A(x)$ | Fuzzy set theory | $[0,1]$ | No --- graded membership |
| Cohesion field $u_t(x)$ | SCC | $[0,1]$ | **Claimed** --- but why? |

What distinguishes $u_t(x)$ from a fuzzy membership function? The spec anticipates this and insists:

> "The cohesion field $u_t$ is not a posterior probability, not a class membership score, and not a segmentation mask." (Canonical Spec v2.0, Section 3.3)

But *what is it then?* It is defined as "the degree to which site $x$ participates in the cohesive formation." This *is* a membership score. The formation is the set; the cohesion value is the degree of membership. Renaming "membership" as "participation" and "set" as "formation" does not create a new ontological level.

The theory's prohibition against interpreting $u_t$ as any of these familiar constructs (Spec Section 10, CLAUDE.md constraint 4) is revealing. If the distinction were mathematically substantive, the theory wouldn't need to *prohibit* the interpretation --- the mathematics would make it impossible. The fact that a prohibition is needed suggests that the mathematics doesn't enforce the distinction. The distinction is rhetorical, not formal.

---

## COUNT 5: The Mathematical Structure IS Object-Like

### Energy Minimization Finds Objects

The energy functional $\mathcal{E} = \lambda_{\text{cl}} \mathcal{E}_{\text{cl}} + \lambda_{\text{sep}} \mathcal{E}_{\text{sep}} + \lambda_{\text{bd}} \mathcal{E}_{\text{bd}} + \lambda_{\text{tr}} \mathcal{E}_{\text{tr}}$ on the constrained manifold $\Sigma_m$ is a standard phase-field energy with two novel self-referential terms. Its minimizers are spatially localized, bounded, morphologically structured configurations.

The boundary/morphology energy $\mathcal{E}_{\text{bd}}$ contains:

- A **smoothness penalty** $\alpha \sum_{x,y} N_t(x,y)(u(x) - u(y))^2$ --- penalizes non-smooth boundaries, just like in image segmentation.
- A **double-well potential** $\beta \sum_x u(x)^2(1-u(x))^2$ --- drives values toward 0 or 1, creating *binary* inside/outside regions.

The double-well potential is *explicitly anti-gradedness*. It penalizes the very intermediate values that the theory claims are its ontological innovation. It drives the field toward a binary partition --- exactly the object/non-object distinction the theory claims to precede. The formation that emerges from energy minimization has values near 1 inside, values near 0 outside, and a narrow transition band. This is an object with a boundary.

### The Optimizer Is an Object Finder

The primary API is `find_formation(GraphState, ParameterRegistry) -> FormationResult`. This function:

1. Takes a graph (the world)
2. Takes parameters (including volume budget $m$)
3. Runs semi-implicit projected gradient descent with multi-start
4. Returns a `FormationResult` containing the optimized field, diagnostics, and energy

This is an object finder. Its name says so. Its function says so. Its output --- a localized, bounded, morphologically structured configuration with a diagnostic vector measuring its object-quality --- says so.

### The Phase Transition Creates Objects

The phase transition theorem (T8-Core) states that when $\beta/\alpha > 4\lambda_2/|W''(c)|$, the homogeneous state $u \equiv c$ becomes a saddle point and non-trivial minimizers emerge. This is the *creation of objects from nothing*. Before the transition: uniform field, no structure, no formation. After the transition: localized, bounded formations --- objects.

The spec calls this "formation existence." Call it what it is: object genesis. The phase transition is the moment when the featureless field crystallizes into discrete things. This is not "pre-objective" --- it is the very birth of objecthood, described in the language of phase-field mathematics.

---

## COUNT 6: The Gestalt Mapping Proves the Point

### SCC Claims to Formalize Gestalt

> "SCC provides [a variational] framework [with] structural correspondences with the classical Gestalt laws of perceptual organization." (paper2_cogsci.tex, Abstract)

The Gestalt Table (paper2_cogsci.tex, Table I) maps:

| Gestalt Principle | SCC Counterpart |
|-------------------|-----------------|
| Closure | $\text{Cl}_t$ (closure operator) |
| Figure-Ground | $D_t$ (distinction operator) |
| Pregnanz | Metastable energy minima |
| Common Fate | $C_t$ / $M_{t \to s}$ |

### But Gestalt Psychology IS About Objects

The Gestalt laws describe **how objects are perceived**:

- **Closure**: incomplete figures are perceived as *complete objects*
- **Figure-Ground**: the visual field is parsed into *objects* (figures) and *background* (ground)
- **Pregnanz**: perception tends toward *the best possible object organization*
- **Common Fate**: elements that move together are perceived as *a single object*

Every Gestalt law is a law about object perception. The Gestalt psychologists were not describing something "before" objects --- they were describing the *process by which objects emerge in perception*. Wertheimer's grouping principles answer the question: "how do we see things as things?"

If SCC formalizes Gestalt, then SCC formalizes object perception. Not pre-objective cohesion. Object perception. The theory cannot simultaneously claim to be "before objects" and to formalize the laws of object perception.

### The Theory's Own Honesty Undermines It

The paper acknowledges that its Gestalt mappings are "structural analogies --- not direct formalizations of the specific perceptual phenomena" (paper2_cogsci.tex, Section III). The philosophy audit goes further:

> "Loose analogy, not direct formalization. The word 'closure' is doing heavy lifting." (A5-philosophy-audit.md, Section 3)

> "Trivially true but not distinctive. Every spatial model 'formalizes' proximity in this sense." (A5-philosophy-audit.md, Section 3)

> "Reinterpretation, not formalization. The paper redefines Pregnanz to match what the math delivers." (A5-philosophy-audit.md, Section 3)

If the Gestalt mapping is merely analogical, then SCC doesn't formalize Gestalt, and the Gestalt connection provides no support for the "pre-objective" claim. If the mapping is substantive, then SCC formalizes object perception, and the "pre-objective" claim is contradicted. Either way, the prosecution wins.

---

## COUNT 7: The Self-Referentiality Argument Is Overstated

### The Claim

> "The theory's self-referentiality is dual-mode, not generic." (Canonical Spec v2.0, Section 10)

The theory claims that its distinctive feature is the "triple-mode self-referential structure" --- closure, distinction, and co-belonging all depend on the field they evaluate.

### The Prosecution's Response

The spec itself concedes the weakness of this claim:

> "Self-referentiality per se [...] is routine in nonlinear variational problems (the Euler-Lagrange equation for any nonlinear functional has the solution appearing in the equation). What is distinctive is the specific structure: two independent modes of self-dependence operating simultaneously." (Canonical Spec v2.0, Section 10)

This admission is devastating. The theory acknowledges that self-referentiality is "routine" and retreats to claiming that *two* modes of self-dependence are distinctive. But having two nonlinear terms in an energy functional is also routine. The Allen-Cahn equation has self-referential gradient energy and self-referential double-well potential --- two modes. The Ginzburg-Landau functional has self-referential kinetic energy and self-referential potential energy --- two modes. The Cahn-Hilliard equation has the same structure. None of these claim to operate at a "pre-objective" ontological level.

The philosophy audit's conclusion on the autopoiesis/self-referentiality claim is unambiguous:

> "The mathematics does not formalize autopoiesis in any non-trivial sense. It formalizes self-consistent nonlinear field equilibria --- a well-understood mathematical structure that is not specific to autopoietic systems." (A5-philosophy-audit.md, Section 2)

---

## COUNT 8: The Theory's Own Auditors Agree with the Prosecution

The most damning evidence comes from the theory's own vulnerability audit (I5) and philosophy audit (A5). The I5 ontological audit identified the central tension with precision:

> **Mathematics:** "Given a discrete domain, pre-specified volume, and 15 parameters, phase-separation produces diagnostic formations."
>
> **Philosophy:** "Coherent formation precedes discrete objecthood."
>
> **The gap between these is the central vulnerability.** (A5-philosophy-audit.md, Section 8)

The philosophy audit's overall assessment:

| Claim | Verdict |
|-------|---------|
| Pre-objective priority | OVERSTATED BUT SALVAGEABLE |
| Autopoiesis formalization | FUNDAMENTALLY UNSUPPORTED |
| Variational Gestalt foundation | OVERSTATED BUT SALVAGEABLE |
| PP supersession | OVERSTATED BUT SALVAGEABLE |
| Soft ontology | Acceptable interpretation |

Two of six philosophical claims are "OVERSTATED," one is "FUNDAMENTALLY UNSUPPORTED," and the comparison tables "systematically characterize competing theories at their weakest/most rigid formulations while presenting SCC at its most flexible" (A5, Section 7). The theory's own auditors have found it guilty of overclaiming.

---

## SUMMATION: What the Mathematics Actually Shows

Strip away the phenomenological language. Strip away the prohibitions against interpreting $u_t$ as a membership function. Strip away the insistence that this is not segmentation. What remains?

**The mathematics shows:** Given a finite weighted graph and a pre-specified volume budget, energy minimization with a phase-field energy (Allen-Cahn smoothness + double-well) augmented by two self-referential terms (closure consistency and distinction from complement) produces spatially localized, bounded, morphologically structured configurations with measurable internal coherence, figure-ground contrast, core-boundary-exterior stratification, and temporal continuity.

**What this is:** A phase-field model for detecting spatially coherent formations on graphs. It is more interesting than standard Allen-Cahn because of the self-referential closure and distinction terms, which genuinely enrich the energy landscape. It is a legitimate contribution to variational methods on graphs.

**What this is not:** An ontological layer prior to objecthood. The formalism presupposes individuation (discrete sites), presupposes formation scale (volume constraint), drives toward binary inside/outside partition (double-well potential), defines crisp geometric notions (Core, Interior, Boundary, Exterior), measures object properties (coherence, boundaries, morphology, identity), and calls its optimizer `find_formation`. Every mathematical operation in the theory either presupposes objects or produces them. The "pre-objective" claim lives in the prose, not in the equations.

---

## VERDICT

**"Pre-objective cohesion" is not a genuine independent ontological layer.** It is a marketing term for what is, mathematically, a self-referential phase-field model that detects and characterizes objects on graphs. The mathematical contribution --- the closure/distinction operator pair, the four-term energy decomposition, the diagnostic vector --- is real and potentially valuable. But the philosophical claim that this describes something *before* objects is unsupported by the formalism and contradicted by its structure.

The theory should be presented for what it is: a variational framework for soft object detection with a novel self-referential architecture, producing continuous-valued object quality assessments. This is honest, interesting, and publishable. The "pre-objective" claim is not dishonest --- the authors clearly believe it --- but it is a philosophical interpretation that the mathematics does not compel and, on close examination, actively undermines.

The prosecution rests.
