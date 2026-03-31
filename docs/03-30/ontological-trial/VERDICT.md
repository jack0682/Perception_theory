# VERDICT: The Ontological Trial of Soft Cognitive Cohesion

**Judge's Ruling**
**Case:** *The Formalism v. The Philosophy*
**Date:** 2026-03-30

---

## 1. Summary of Prosecution's Strongest Points

The prosecution built a formidable case on four pillars:

**P1. "Graded does not equal pre-objective" (Count 4).** This is the prosecution's tightest logical argument. The observation that posterior probabilities, neural activations, fuzzy membership functions, and cohesion fields are all $[0,1]$-valued --- and that only the last claims to be "pre-objective" --- demands an answer. If gradedness alone is not sufficient for pre-objectivity, what is? The prosecution correctly identifies that the theory has not given a satisfying formal criterion for what makes $u_t$ pre-objective rather than merely continuous.

**P2. The double-well potential drives toward binary states (Count 5).** The term $\beta \sum_x u(x)^2(1-u(x))^2$ explicitly penalizes intermediate values and drives the field toward $\{0,1\}$. This is, as the prosecution says, "explicitly anti-gradedness." The formalism's own energy functional works against the philosophy's core claim. The formations that `find_formation` actually produces have values clustered near 0 and 1 with a narrow transition band --- they look like objects with boundaries.

**P3. The volume constraint is pre-specification of formation scale (Count 2).** Without $\sum u(x) = m$, the theory produces only $u \equiv 0$. The theory cannot generate formations from its own dynamics; it must be told that formations of a particular total mass exist. This is a serious wound to the "how anything becomes a coherent something" narrative.

**P4. The theory's own auditors found overclaiming (Count 8).** The philosophy audit's findings --- "OVERSTATED BUT SALVAGEABLE" for pre-objective priority, "FUNDAMENTALLY UNSUPPORTED" for autopoiesis --- are prosecution evidence from the theory's own house. This is not external skepticism; it is internal quality control.

## 2. Summary of Defense's Strongest Points

The defense mounted three genuinely powerful arguments:

**D1. Intensity field $\neq$ probability field (Defense 1).** This is mathematically precise and irrefutable. A cohesion field $u_t \in [0,1]^{X_t}$ with self-referential evaluation is a formally different mathematical object from a posterior $P(z = k \mid x)$ over latent discrete variables. There is no likelihood function, no prior, no latent variable being estimated. The prosecution's attempt to equate $u_t$ with a fuzzy membership function or a posterior probability ignores genuine structural differences in the mathematical machinery. A formation with $\mathbf{d} = (0.7, 0.5, 0.6, 0.4)$ is a legitimate final state of the theory, not an incomplete inference that should converge to a crisp answer.

**D2. The $[0,1]^4$ intermediate zone has genuine representational novelty (Defense 5).** Object-based theories partition the diagnostic space into "object present" and "no object." SCC populates the entire cube with structurally meaningful states. The defense's perceptual examples --- peripheral vision, scene gist, visual crowding --- are compelling illustrations of phenomena that resist object-level description but admit natural formation-level description. "Moderately bound but poorly separated" is a meaningful structural state that object theories cannot express.

**D3. Asymmetric failure modes (Defense 4).** SCC correctly produces no formation on complete graphs (Sep $\approx$ 0.12, Inside $= 0.00$), because complete graphs lack the relational structure needed for cohesive differentiation. A template-matching object detector could still produce proposals on a complete graph. This asymmetry is genuine evidence that SCC is sensitive to different structural features than object detectors.

## 3. Where Prosecution Wins

### 3.1. The Double-Well Objection Is Devastating

The prosecution wins decisively on the double-well point. The energy term $\beta \sum_x W(u_i)$ with $W(u) = u^2(1-u)^2$ is a binary attractor. It pushes $u$ toward $\{0,1\}$. The formations that the optimizer actually produces (I have read `optimizer.py` and `energy.py`) exhibit near-binary profiles: values close to 1 in the interior, values close to 0 in the exterior, and a narrow transition band. The code confirms this: the convergence criteria (`eps_energy`, `eps_grad`, `eps_field`) are designed to find well-separated energy minima, not to stabilize in genuinely intermediate states.

The defense cannot escape this. The double-well potential is not an incidental feature --- it is load-bearing. Without it, the phase transition theorem (T8-Core) fails, because $W''(c) < 0$ in the spinodal region is what makes the homogeneous state unstable. The binary attractor is the engine of formation. The philosophy says "gradedness is primitive"; the mathematics says "gradedness is penalized."

**Ruling: Prosecution wins.** The formalism's energy landscape actively works against genuinely intermediate states. The formations it produces are near-binary. The "graded field" is a transient computational state, not the theory's equilibrium ontology.

### 3.2. The Volume Constraint Is Smuggling

The prosecution wins on the volume constraint. The defense's analogy to mass conservation in physics is instructive but ultimately fails, for a reason the defense does not address: mass conservation in physics is a dynamical law discovered about existing matter. The volume constraint $\sum u(x) = m$ is a parameter set before optimization begins. It tells the theory how much formation to find. This is closer to saying "find me an object of size 25" than to saying "discover what emerges."

The defense correctly notes that the volume constraint does not specify *where* or *what shape* the formation takes. This is true and important. But the prosecution's deeper point stands: a theory that claims to explain how "anything becomes a coherent something" should not require being told how much something to expect.

**Ruling: Prosecution wins,** with a caveat. The volume constraint undermines the *generative* claim ("how formations emerge") but does not undermine the *structural* claim ("what formation-level organization looks like"). The theory can honestly claim to characterize formation structure even if it cannot claim to explain formation genesis from nothing.

### 3.3. The Gestalt Mapping Is Self-Defeating

The prosecution's Count 6 is correct: Gestalt psychology *is* about object perception. The laws of grouping describe how the perceptual field is organized into objects. If SCC formalizes Gestalt, it formalizes object perception. The theory cannot simultaneously claim to be "before objects" and to formalize laws that describe how objects emerge.

The defense does not adequately address this. The correct resolution is not that SCC formalizes Gestalt, but that SCC provides a *substrate* from which Gestalt-like organization can be read off --- a distinction the papers should make more carefully.

**Ruling: Prosecution wins** on the Gestalt overclaim. SCC does not formalize Gestalt psychology. It provides a variational framework whose equilibria exhibit structural properties analogous to Gestalt organizational principles.

## 4. Where Defense Wins

### 4.1. Intensity $\neq$ Probability Is Real and Important

The defense wins on the foundational mathematical point. The prosecution's Count 4 (the table comparing $u_t$ to posteriors, activations, and fuzzy memberships) is rhetorically effective but mathematically imprecise. A Bayesian posterior $P(z=k \mid x)$ presupposes a discrete latent variable $z$. A fuzzy membership function $\mu_A(x)$ presupposes a fuzzy set $A$. The cohesion field $u_t$ presupposes neither. It is a primitive entity in its own right, evaluated by self-referential operators, not by comparison to a hidden ground truth.

The prosecution asks: "What is $u_t$ then, if not a membership function?" The answer is in the mathematics: $u_t$ is a field whose value at each site measures the intensity of cohesive participation, where "cohesive participation" is defined self-referentially by the field's own closure and distinction operators. This circularity is the point, and it is formally distinct from anything in the Bayesian or fuzzy-set frameworks.

**Ruling: Defense wins.** The mathematical distinction between self-referential intensity fields and posterior probabilities over discrete latent variables is genuine, precise, and consequential. The prosecution's claim that $u_t$ "is" a membership function is a category error.

### 4.2. The Intermediate Zone Is Genuinely Novel

The defense wins on the representational point. The diagnostic vector $\mathbf{d} \in [0,1]^4$ with four independently varying components provides a richer description of structural states than any object-based framework can express. The state "moderately bound, poorly separated, well-articulated, barely persistent" is meaningful, structural, and not representable in object theories (which can only say "object at confidence $p$").

The prosecution could respond that a Bayesian model with rich enough latent structure could also represent such states. This is true in principle, but misses the point: in the Bayesian model, these states are intermediate inferential states converging toward a discrete answer. In SCC, they are legitimate final states that the diagnostic vector evaluates on their own terms.

**Ruling: Defense wins.** The four-dimensional diagnostic space is a genuine theoretical contribution with no equivalent in object-based frameworks.

### 4.3. The Failure Mode Asymmetry Is Evidence

The defense wins on failure modes. SCC's inability to form coherent structures on complete graphs, and its ability to produce diagnostically meaningful partial formations, are structural properties that distinguish it from object detectors. These are not mere implementation details --- they follow from the mathematical structure (the Fiedler eigenvalue $\lambda_2 = 0$ on disconnected graphs, $\lambda_2 = n$ on complete graphs changes the energy landscape qualitatively).

**Ruling: Defense wins.** The asymmetric failure modes are genuine evidence that SCC is sensitive to relational structure in ways that object detectors are not.

### 4.4. Self-Referential Dual-Mode Structure Is Distinctive

The defense wins a partial victory on self-referentiality. The prosecution is right that self-referentiality per se is generic (Count 7). But the defense correctly identifies that SCC's specific architecture --- self-completion through closure and self-contrast through distinction, entering through independent energy channels with distinct Hessian contributions --- is more specific than "any nonlinear PDE." The positive-definite Gram matrix $(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}})$ from the closure term is a structural feature not present in Allen-Cahn, and the enhanced metastability theorem (T7) is a formal consequence of this architecture.

**Ruling: Defense wins on architectural novelty.** The dual-mode self-referential structure is genuinely distinctive within the phase-field literature. But this is *mathematical* novelty, not necessarily *ontological* novelty. Having a more interesting energy functional does not automatically establish a new ontological layer.

---

## 5. VERDICT on Each Question

### Question 1: Is "pre-objective cohesion" an independent ontological layer?

**VERDICT: PARTIALLY.**

The theory identifies something real: a level of structural description --- the graded, self-referentially evaluated cohesion field with four-dimensional diagnostics --- that is formally distinct from object-level description and captures structural states that object theories cannot represent.

But the theory *overstates* the independence of this layer. The double-well potential drives formations toward near-binary states. The volume constraint pre-specifies formation scale. The optimizer finds well-defined, bounded, morphologically structured configurations that satisfy classical object criteria. The equilibrium formations are objects by any reasonable empirical test.

What is genuinely "pre-objective" is not the equilibrium formations but the *space of all formation states* --- the entire $[0,1]^4$ diagnostic cube, including the intermediate zone where formations are partially bound, poorly separated, or weakly articulated. The theory provides a language for describing structural states that exist before full objecthood is achieved. But the formalism's own energy landscape treats these intermediate states as transients on the way to well-formed (object-like) equilibria, not as stable ontological entities in their own right.

**The layer is not independent. It is the approach ramp to objecthood, described with more structural precision than object theories provide.**

### Question 2: Does the mathematics support the philosophy?

**VERDICT: The mathematics supports a WEAKER version of the philosophy.**

The philosophy claims: "Coherent formation precedes discrete objecthood. The soft field is ontologically prior."

The mathematics shows: "Given a graph with relational structure and a volume budget, energy minimization with self-referential operators produces spatially coherent formations whose quality can be assessed along four independent graded dimensions."

The gap:

1. **"Precedes" is not formalized.** The theory provides no formal notion of temporal or ontological priority. It provides a variational characterization of formation structure, not a dynamical account of how formations emerge from nothing. The phase transition theorem (T8-Core) comes closest --- it shows when homogeneous states become unstable --- but this is a property of the energy landscape, not a temporal process.

2. **The formalism's equilibria are object-like.** Whatever the field looks like during gradient descent, the final output of `find_formation` is a well-defined, bounded, near-binary configuration. The code returns a `FormationResult` with diagnostic scores typically above 0.8. These are objects.

3. **The self-referential structure is real but does not establish priority.** The closure and distinction operators genuinely depend on $u$ in ways that external classifiers do not. But self-referential evaluation is a *property* of the formalism, not evidence that the formalism operates at a *prior* level. A self-referential object detector is still an object detector.

**What the mathematics genuinely supports:** The formation-level description (graded, decomposed, self-referentially evaluated) is formally richer than and not reducible to object-level description (binary, holistic, externally classified). The two descriptions are structurally different mathematical frameworks. Whether the former is ontologically "prior to" the latter is a philosophical claim the mathematics constrains but does not settle.

### Question 3: What is the strongest honest version of the claim?

> **Soft Cognitive Cohesion provides a variational framework in which the structural properties of coherent formations --- binding, separation, morphological articulation, and persistence --- are decomposed into four independently graded dimensions and evaluated through self-referential operators that depend on the field they assess. This framework is formally distinct from object-based representations: it operates on continuous intensity fields (not discrete labels or probability distributions over them), evaluates formation quality through self-referential criteria (not external classifiers), and represents a continuous space of structural states including intermediate zones (partial binding, weak separation, incomplete articulation) that have no equivalent in object-level description. The formalism does not presuppose that the world is pre-parsed into objects, though its computational implementation does presuppose a discrete substrate and a formation-scale parameter. Whether this framework describes a level of perceptual or cognitive organization that is genuinely prior to object individuation is an empirical question that the theory's predictions can address but its mathematics alone cannot answer.**

This version:
- Preserves the core contribution (four-dimensional graded diagnostics, self-referential operators)
- Preserves the formal novelty (irreducibility to object-level description)
- Drops the metaphysical priority claim ("precedes," "prior to," "before objects")
- Replaces it with a structural distinctness claim ("formally distinct from," "not reducible to")
- Honestly flags the substrate and volume-constraint assumptions
- Defers the priority question to empirical testing, where it belongs

### Question 4: The User's Three Problems

**Problem 1: Minimum difference between object and pre-objective cohesion.**

The minimum formal difference is this: an object is a binary-valued, externally classified, countable, categorizable entity. A cohesive formation is a continuous-valued, self-referentially evaluated, non-countable (in the single-field theory), non-categorizable structural state. These differ in:

| Property | Object | Formation |
|----------|--------|-----------|
| Existence type | Binary (present/absent) | Graded ($\mathbf{d} \in [0,1]^4$) |
| Evaluation | External criteria | Self-referential operators |
| Countability | Countable | Not countable (single-field) |
| Categorization | Category-bearing | Category-free |
| Boundary | Crisp (codimension-1) | Graded (transition band) |
| Identity | Extensional (same sites/features) | Structural (core inheritance) |

The minimum *necessary* difference is evaluation type: self-referential vs. external. This is the irreducible core. Everything else follows from it or can be recovered by thresholding.

However, I note: this difference is real but does not automatically entail ontological priority. A self-referentially evaluated object is still an object. The difference establishes *structural distinctness*, not *ontological precedence*.

**Problem 2: Can the theory be stated without object language?**

**Mostly yes, with one critical exception.**

The three spatial predicates (Bind, Sep, Inside) can be stated entirely in terms of fields, operators, and topological constructions:

- Bind: $\ell^2$ distance between a field and its closure-operator image
- Sep: field-weighted mean of sigmoid-processed asymmetry between field-weighted and complement-weighted neighborhood averages
- Inside: persistence diagram statistics of the superlevel-set filtration

No objects, no boundaries, no "insides" or "outsides." These are operations on continuous fields with continuous outputs.

**The critical exception is Persist.** The spec's persistence formula uses $\mathrm{Core}_t = \{x : u_t(x) \geq \theta_{\mathrm{core}}\}$ --- a crisp threshold-derived set. This reintroduces object language at the temporal level. The code's placeholder (`persist_predicate` in `diagnostics.py`) avoids this by using raw $\ell^2$ field similarity, but this is acknowledged as a placeholder that does not implement the spec.

A fully object-free persistence predicate is possible in principle (e.g., using optimal transport between fields, or soft core-weighting without crisp thresholds), but does not yet exist in the theory. This is the theory's most honest gap.

**Problem 3: Three cases where the distinction matters empirically.**

The defense's three cases (Kanizsa, binocular rivalry, change blindness) are well-chosen. I assess them:

**Case 1: Kanizsa triangle.** This is the strongest case. The illusory triangle has cohesive properties (binding, separation, articulation) without being an object in any material sense. An object theory must explain it as a recognized pattern; SCC explains it as a self-sustaining cohesive field. **The distinction matters here: SCC predicts that the "triangle" will exhibit specific diagnostic profiles (high Bind from relational support of inducers, high Sep from contrast with surround), while object theories can only say "triangle detected." The profiles are more informative and more testable.**

**Case 2: Visual crowding.** This is the most empirically accessible case. SCC predicts that crowding selectively destroys Sep (separation) while preserving Bind (binding) --- the formation holds together but loses its distinctness from flankers. This is a decomposed prediction: object theories predict only "recognition fails." **The distinction matters here because SCC makes a more specific prediction (Sep drops, Bind persists) that is testable with existing psychophysical methods.**

**Case 3: Pre-attentive texture segmentation.** I substitute this for the defense's change blindness case, which is less directly tied to the formation/object distinction. In pre-attentive texture segmentation, the visual system rapidly segments textures before object recognition occurs. SCC predicts that this segmentation corresponds to formation-level organization (high Bind from texture coherence, moderate Sep from texture boundaries) without requiring object identification. **The distinction matters here because SCC provides a formal framework for describing the structural organization that exists before object recognition, and predicts specific diagnostic profiles for pre-attentive segmentation that differ from post-attentive object identification.**

### Question 5: What should the papers say?

**Canonical Spec Section 2 should be revised as follows:**

Remove or weaken:
- "The theory of Soft Cognitive Cohesion does not begin from objects" --- replace with: "The theory of Soft Cognitive Cohesion does not require objects as primitive inputs."
- "Coherent formation precedes discrete objecthood" --- replace with: "Coherent formation can be characterized independently of discrete objecthood."
- "Any framework that begins from such assumptions starts too late" --- remove. This is a philosophical claim the mathematics does not support.

Preserve and strengthen:
- The description of the cohesion field as a graded intensity, not a probability
- The distinction between self-referential evaluation and external classification
- The four-dimensional diagnostic vector as a richer description than binary object presence
- The claim that objects are a special case (fully bound, fully separated, fully articulated, fully persistent) of a more general space of formation states

**Paper2's introduction should be revised as follows:**

The opening vignette (the "coherent something" in a crowded room) is good and should be kept. But the framing should shift from:

> "This pre-objective cohesion --- the emergence of 'somethingness' before 'thingness' --- is the phenomenon this paper addresses."

To something like:

> "This structural cohesion --- the organization of a region into a bound, distinguished, articulated formation that may or may not stabilize into a recognized object --- is the phenomenon this paper addresses. We provide a mathematical framework in which the properties typically attributed to objects are decomposed, graded, and independently assessed, revealing a continuous space of formation states that is richer than the binary object/non-object distinction."

This preserves the empirical motivation while replacing the ontological priority claim with a structural distinctness claim that the mathematics actually supports.

---

## 6. Recommended Revision to the Foundational Claim

**Current claim (Canonical Spec Section 2):**
> "The foundational commitment of this theory is that coherent formation precedes discrete objecthood."

**Recommended revision:**
> "The foundational commitment of this theory is that coherent formation can be characterized as a graded, self-referentially evaluated structural state that is formally richer than and not reducible to discrete objecthood. Objects, in this framework, are a distinguished region of the formation space --- the region where all four structural requirements (binding, separation, articulation, persistence) are maximally satisfied --- not the starting point of the analysis."

This revision:
- Drops the temporal/ontological "precedes" that the mathematics does not formalize
- Preserves the core insight that formation-level description is richer than object-level description
- Preserves the claim that objects are derivative (a special case of formation states)
- Is fully supported by the existing theorems and implementation
- Remains interesting and publishable

---

## 7. What the Theory ACTUALLY Achieves (Not What It Claims)

### What is genuinely achieved:

1. **A variational framework for soft formation detection on graphs** with a mathematically novel self-referential operator pair (closure and distinction) that enters the energy through independent channels and produces enhanced metastability relative to standard Allen-Cahn. This is a real contribution to applied mathematics and variational methods.

2. **A four-dimensional diagnostic decomposition** (Bind, Sep, Inside, Persist) that provides a more informative assessment of formation quality than any single scalar or binary predicate. This decomposition is useful regardless of one's philosophical position on pre-objectivity.

3. **A formal framework that unifies several structural properties** (self-support, figure-ground asymmetry, morphological stratification, temporal continuity) under a single energy principle, with proved theorems about formation existence, closure contraction, gradient flow convergence, and enhanced metastability.

4. **Twelve rigorously proved theorems** establishing the mathematical foundations of the framework, including the phase transition theorem, the closure contraction theorem, the Lojasiewicz convergence result, and the Sep covariance identity.

5. **A structural connection** (not a formalization) to Gestalt organizational principles, phenomenological accounts of pre-objective experience, and the concept of operational closure --- which can motivate further empirical investigation.

### What is NOT achieved:

1. **A demonstration that pre-objective cohesion is ontologically prior to objecthood.** The mathematics shows structural distinctness, not ontological priority. The "precedes" claim is a philosophical interpretation that the formalism is consistent with but does not compel.

2. **A dynamical account of formation emergence.** The theory is variational (characterizing equilibria), not dynamical (describing how fields evolve from homogeneous to structured states in real time). The gradient flow in `optimizer.py` is a computational method, not a model of temporal formation dynamics.

3. **A complete temporal theory.** Persistence has zero proved results. The transport kernel is unimplemented. The crisp-core formula reintroduces object language. This is the theory's largest gap and its most honest admission.

4. **A formalization of Gestalt psychology.** The structural analogies are suggestive but loose. The word "closure" in SCC and in Gestalt psychology mean different things. The mapping is interpretive, not formal.

5. **A theory of consciousness or subjective experience.** The theory correctly disclaims this, but the phenomenological framing (Merleau-Ponty, Husserl) may lead readers to expect more than is delivered.

---

## Final Judgment

The theory of Soft Cognitive Cohesion is a genuine mathematical contribution with a real intellectual core. Its self-referential operator pair, four-term energy decomposition, and four-dimensional diagnostic vector constitute a novel and potentially valuable framework for characterizing coherent formations on relational structures.

The philosophical claim that this framework describes a level of reality "prior to" objecthood is not supported by the formalism. What the formalism supports is a *structurally richer* description of formation states that *includes* object-like states as a special case. This is interesting, publishable, and potentially important --- but it is a claim about the *expressiveness of a mathematical framework*, not about the *ontological priority of a layer of reality*.

The theory should be presented as what it is: a variational framework for characterizing graded coherent formations through self-referential operators and decomposed diagnostics. This is more than standard phase-field theory (the self-referential structure is genuine). It is less than a new ontology (the equilibria are objects). The honest middle ground --- structural distinctness without ontological priority --- is both defensible and, I believe, more compelling than the current overclaim.

The prosecution is right that the emperor's clothes are overstated. The defense is right that the emperor is wearing *something* --- something mathematically novel and potentially important. The verdict is that the theory should describe what it is wearing accurately, rather than claiming it constitutes an entirely new category of garment.

---

*The court is adjourned.*
