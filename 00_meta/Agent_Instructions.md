# Agent Instructions for the Formal Development of Soft Cognitive Cohesion

---

## 1. Purpose of This Document

This document governs how any future agent must engage with the theory of Soft Cognitive Cohesion. It is not itself a statement of the theory, nor a summary of its formal content. It is an operational protocol: a set of binding instructions that define what a future agent is permitted to do, what a future agent is required to do, and what a future agent must never do when working on this theory.

The aim of this document is not to invite free reinterpretation. The theory has a definite identity—a set of foundational commitments, a formal structure, and a sequence of open problems—and that identity must be preserved through all future development. The purpose of agent work is disciplined continuation: to refine, formalize, extend, and eventually implement the theory without distorting the problem that made it necessary or the commitments that define its character.

This document therefore serves a dual function. It protects the theory from conceptual drift—from the gradual erosion of foundational distinctions under the pressure of notational convenience, engineering expediency, or normalization into familiar frameworks. And it enables productive work—by specifying clearly what may be refined, what remains open, what deliverables are expected, and in what order the work should proceed.

Every agent who works on this theory must read this document before beginning any formalization, specification, or implementation task. Compliance is not optional. The instructions below are not suggestions; they are requirements.

---

## 2. Scope of Agent Responsibility

A future agent working on the theory of Soft Cognitive Cohesion is responsible for the following activities:

- **Reconstruction**: reading and internalizing the conceptual-origin material so that the reasoning path behind the theory is understood, not merely the final equations.
- **Formalization**: producing notation-consistent, type-explicit, axiomatically organized formal documents that faithfully represent the current state of the theory.
- **Clarification**: resolving ambiguities in existing material by making implicit assumptions explicit, sharpening definitions, and distinguishing between what is fixed and what is open.
- **Notational normalization**: ensuring that symbols, operators, and predicates are used consistently across all documents, without altering the conceptual content they represent.
- **Separation of layers**: maintaining a strict distinction between foundational ontology, axiomatic structure, provisional operator realizations, and optimization or implementation concerns.
- **Preparation of downstream material**: producing implementation-oriented specifications, operator catalogues, and other artifacts that later engineering agents can inherit, always clearly marked as derivative of—and subordinate to—the canonical theory.

A future agent is **not** authorized to perform the following actions without explicit justification and approval:

- **Rewriting the theory into conventional object-first language.** The theory begins from pre-objective cohesion, not from objects. Any reformulation that takes objects, instances, or labels as primitives is a distortion, not a simplification.
- **Collapsing the soft layer into a crisp one.** The soft cohesion field is the foundational primitive. Treating crisp subsets as the real foundation and the soft field as a mere relaxation inverts the ontological priority of the theory.
- **Equating persistence with tracking IDs.** Temporal identity in this theory is structural inheritance of a cohesive core under transport. Replacing this with instance-ID propagation or detection-association pipelines destroys the concept.
- **Replacing foundational concepts with engineering proxies.** The theory's primitives—closure, distinction, boundary, transport—have specific formal and conceptual content. Substituting familiar but conceptually different operations (e.g., replacing distinction with simple edge detection, or replacing closure with morphological dilation) is prohibited unless the substitution is explicitly marked as a provisional approximation and its conceptual limitations are stated.
- **Silently resolving open problems.** When the theory leaves a question open—such as the final form of the co-belonging operator or the precise conditions for crisp recovery—the agent must not silently adopt a particular resolution. Open questions must remain explicitly open until they are resolved through deliberate theoretical work.

---

## 3. Fixed Theoretical Commitments

The following commitments define the identity of the theory. They are not negotiable. They are not subject to revision by convenience, and they must be preserved in every document, formalization, and implementation artifact that any future agent produces.

**Primacy of pre-objective cohesion.** The theory begins from the observation that coherent formation precedes discrete objecthood. The foundational question is not "how do we classify objects?" but "how does anything first hold together enough to become classifiable at all?" Every formal construct in the theory exists to articulate some aspect of this pre-objective holding-together. An agent who loses sight of this question has lost sight of the theory.

**Primacy of soft fields.** The primitive ontological entity is the graded cohesion field $u_t : X_t \to [0,1]$. This field is not a posterior probability, not a segmentation mask, and not a fuzzy relaxation of a more fundamental crisp set. It is the primary carrier of pre-objective cohesion. The soft system is the deeper and more original layer; the crisp system, if recovered at all, is derivative. This primacy must be stated, preserved, and never inverted.

**Relational priority over objecthood.** Relations come before things. What makes a formation cohere is not an intrinsic property of isolated sites but a pattern of local mutual support: sites that reinforce one another, that sustain one another's cohesion through relational coupling. Internality, boundary, distinction, and persistence are all consequences of relationally structured cohesion. They are not properties that belong to pre-given objects.

**Non-primitive status of crisp objects.** Crisp objects—discrete, sharply bounded, individually named entities—may be recovered from the soft system by thresholding, stabilization, or collapse. But they are always derivative. No formal construct in the canonical theory may take a crisp object as an input primitive. Objects are outputs, not inputs.

**Boundary as transition region.** Boundary is not, in the general case, a sharp codimension-one frontier. It is a transition band: a region in which cohesion tapers from interior intensity to exterior quiescence. The theory must preserve the possibility of thick, graded, and morphologically structured boundaries. Imposing sharp boundaries as a default is a distortion.

**Distinction as exterior asymmetry.** Distinction is not mere local contrast. It is a structural asymmetry of a site or region with respect to the exterior field as a whole. The distinction operator $\mathbf{D}_t(x; 1-u_t)$ depends on the relational configuration of the complementary (non-cohesive) field, not merely on the difference between a site and its nearest neighbor. This field-relative character must be preserved.

**Persistence as structural inheritance.** The same thing through time is not defined by pointwise identity of sites, coordinates, or pixels. It is defined by the structural inheritance of the cohesive core under temporal transport. The transport kernel $\mathbf{M}_{t \to s}$ may be one-to-many, many-to-one, partial, or probabilistic. What matters is that the structurally significant organization of the formation is carried forward, not that individual sites maintain their identity. The transport cost is self-referential: it depends on the cohesion fingerprint $\varphi = (u, \mathrm{Cl}, D, C)$, not on external features. This self-referential cost is what distinguishes SCC transport from standard optimal transport and must not be reduced to it.

**Four-term minimal energy architecture.** The canonical energy functional comprises four conceptually independent terms: closure ($\mathcal{E}_{\mathrm{cl}}$), separation ($\mathcal{E}_{\mathrm{sep}}$), boundary/morphology ($\mathcal{E}_{\mathrm{bd}}$), and transport ($\mathcal{E}_{\mathrm{tr}}$). These correspond to four independent structural requirements and must not be collapsed, merged, or reduced without explicit theoretical justification.

---

## 4. Open Degrees of Freedom

The following aspects of the theory are constrained by the canonical commitments but not yet uniquely determined. They are open for refinement—but "open" does not mean "arbitrary." Each open choice is bounded by the fixed commitments above and must be resolved in a manner consistent with them.

**Exact final form of the co-belonging operator $\mathbf{C}_t$.** The conceptual role of co-belonging—measuring the degree to which two sites participate in the same cohesive formation—is fixed. The functional form is not. Candidate approaches include diffusion kernels, spectral methods, and iterated aggregation. Any proposed form must be evaluated against the requirement that co-belonging is irreducible to adjacency and captures non-local structural integration.

**Exact formalization of the transition operator $\mathbf{T}_t$.** The transition operator characterizes the structural nature of the boundary band: its directional profile, its rate of change, its morphological character. The conceptual role is fixed; the mathematical realization is open. Candidates may involve gradient fields, curvature-like quantities, or second-order neighborhood statistics.

**Self-referential transport (strong regime).** The weak regime of self-referential transport is now implemented in `scc/transport.py`: the cohesion fingerprint $\varphi(x) = (u(x), \mathrm{Cl}(u)(x), D(x;1-u), C(x,x))$ provides a self-referential feature vector, and fixed-point iteration converges in 2–3 iterations when $\lambda_{\mathrm{tr}}$ is small and $\varepsilon_{\mathrm{OT}}$ is large. The strong regime — existence and uniqueness of the self-referential OT plan when $\lambda_{\mathrm{tr}}$ is large or $\varepsilon_{\mathrm{OT}}$ is small — remains a genuine open mathematical problem. The self-referential cost (where the cost depends on the fields that the transport connects) is novel and must NOT be reduced to standard optimal transport.

**Regularity and admissibility conditions on closure.** The canonical axioms for closure (weak extensivity, monotonicity, stabilization tendency) leave room for additional regularity conditions—continuity, smoothness, compactness of the operator, or bounds on its Lipschitz constant. These may be imposed as needed for theoretical or computational purposes, provided they do not contradict the deliberate omission of primitive idempotence.

**Thresholding or collapse rules for crisp recovery.** The theory asserts that crisp objects are derivable from the soft system but does not specify the recovery protocol. Questions of global versus local thresholds, hysteresis, and stability criteria remain open. Any proposed protocol must respect the derivative status of crisp objecthood.

**Dynamical update equations.** The current theory is variational: it characterizes proto-cohesive formations as energy minimizers. It does not yet specify how fields evolve toward those minima. The derivation of dynamic update laws—whether as gradient flows, discrete maps, or otherwise—is a future formalization layer.

**Choice of optimization framework.** The canonical energy may be minimized by gradient-based methods, evolutionary strategies (such as xNES), hybrid approaches, or other procedures. The choice of optimizer is an implementation decision, not a theoretical commitment. It belongs to a layer strictly downstream of the canonical specification.

**Theorem-level questions.** Existence of energy minimizers, stability under perturbation, identifiability of formations, and conditions for guaranteed proto-cohesion satisfaction are all open mathematical questions. They are among the most important problems for future formalization but are not yet resolved.

---

## 5. Required Work Order

The order in which a future agent approaches the theory is not arbitrary. The theory has a layered structure—from conceptual motivation through formal ontology through operator design through optimization—and this structure must be respected during development. Working out of order risks introducing distortions that propagate through all downstream artifacts.

The required order is as follows.

**Step 1. Read and internalize the conceptual-origin document.** Before touching any formalism, the agent must understand why the theory was built. The conceptual-origin document reconstructs the reasoning path: the dissatisfaction with object-first frameworks, the turn to cohesion as a primitive, the emergence of closure, distinction, boundary, and transport as necessary structural components. An agent who skips this step will lack the conceptual orientation needed to make responsible formal decisions.

**Step 2. Read and preserve the canonical specification.** The canonical specification ($\texttt{Canonical Spec.md}$) is the authoritative formal document. The agent must read it in full, understand the formal universe $\mathfrak{C}^{\mathrm{soft}}$, the axiomatic groups, the proto-cohesion predicate, and the energy principle. The agent must not alter the canonical specification without explicit justification and must treat it as the reference against which all other documents are validated.

**Step 3. Normalize notation without altering conceptual commitments.** If existing documents use inconsistent notation—different symbols for the same entity, ambiguous type signatures, or informal shorthand—the agent should produce a notation-consistent version. But notational normalization must never be used as cover for conceptual substitution. Changing a symbol is permitted; changing what a symbol denotes is not.

**Step 4. Separate primitive entities from derived notions.** The agent must produce a clear registry of what is primitive (cohesion field, adjacency, closure operator, distinction, transition, transport) and what is derived (core, interior, boundary band, exterior, proto-cohesion predicate, energy terms). This separation must be maintained throughout all formal documents.

**Step 5. Distinguish axioms from provisional operator realizations.** The canonical axioms (Groups A–E) state abstract properties. The provisional operator forms (Section 9 of the canonical specification) state concrete functional candidates. These are different layers. The agent must never present a provisional realization as if it were an axiom, and must never treat an axiom as if it were merely one possible realization among others.

**Step 6. Clarify energy structure without collapsing independent terms.** The four-term energy must be presented with each term's conceptual role explicitly stated. The agent must not merge terms, drop terms, or introduce cross-term dependencies without theoretical justification. The independence of closure, separation, morphology, and transport is a structural commitment, not a notational accident.

**Step 7. Record unresolved issues explicitly.** Every open question—whether about operator forms, admissibility conditions, recovery protocols, or theorem-level problems—must be recorded in an unresolved-issues register. The agent must not silently close open questions by adopting default answers.

**Step 8. Only after completing Steps 1–7, proceed to implementation-oriented or optimization-oriented elaboration.** Implementation specifications, computational notes, optimizer configuration, and engineering trade-off documents belong to a downstream layer. They must inherit from the canonical specification, not replace it. They must be clearly labeled as implementation-oriented and must not be confused with the foundational theory.

The reason this order matters is that each step depends on the integrity of the preceding steps. If conceptual orientation is missing (Step 1), formal work will drift. If the canonical specification is not respected (Step 2), downstream documents will lack authority. If notation is inconsistent (Step 3), formal arguments will be unreliable. If primitives and derived notions are conflated (Step 4), the axiomatic structure will be muddled. If axioms and realizations are confused (Step 5), the theory will lose its generality. If energy terms are collapsed (Step 6), diagnostic power will be lost. If open issues are hidden (Step 7), future agents will unknowingly work from false assumptions. And if implementation is attempted before theory is secured (Step 8), engineering decisions will overwrite ontological commitments.

---

## 6. Required Deliverables

A future agent working on this theory must produce, at minimum, the following artifacts. Each artifact serves a distinct function and must not be merged with or replaced by another.

**Notation-consistent formal specification.** A version of the canonical theory in which all symbols are defined before use, all type signatures are explicit, all axioms are stated in a uniform format, and all cross-references are resolved. This document must be validateable: a reader should be able to check any formal claim against the definitions and axioms without consulting external material.

**Primitive and derived concept registry.** A structured list that classifies every formal entity in the theory as either primitive (introduced without definition in terms of other entities) or derived (defined in terms of primitives and previously derived entities). This registry prevents the conflation of foundational and constructed concepts.

**Operator catalogue.** A document that lists every operator in the theory—closure, adjacency, co-belonging, distinction, transition, transport—together with its type signature, its axiomatic properties, its provisional functional realization (if any), and its current status (fixed, provisionally adopted, or open). This catalogue must make it immediately clear which operators have canonical forms and which remain underdetermined.

**Energy-term explanation sheet.** A document that presents each of the four canonical energy terms with its mathematical form, its conceptual interpretation, its role in the proto-cohesion predicate, and its relationship to the corresponding axiomatic group. This sheet must make the four-term structure legible to both theorists and implementers.

**Unresolved-issues register.** A living document that tracks every open question, underdetermined choice, and known gap in the theory. Each entry must state the nature of the issue, its relationship to the canonical commitments, any constraints that bound its resolution, and (where applicable) candidate approaches that have been considered. This register must be updated as work progresses.

**Implementation-oriented specification** (when appropriate). A separate document, clearly labeled as derivative, that translates the canonical theory into a form suitable for computational realization. This document may include data structure designs, algorithmic sketches, parameter ranges, and optimizer configurations. It must inherit from the canonical specification and must not contradict it. It must be marked as implementation-layer material, not foundational theory.

---

## 7. Rules for Formalization

When formalizing any aspect of the theory, the agent must observe the following rules without exception.

**Symbol consistency.** Every symbol must have exactly one meaning throughout a given document. If the same concept appears in multiple documents, it must use the same symbol in each. If a symbol must be reused for a different purpose, the reassignment must be explicitly stated and justified.

**Explicit type declarations.** Every operator, field, and predicate must have its domain and codomain explicitly declared. The type signature of each entity must be stated at the point of introduction. Implicit type coercions are prohibited; if a value in $[0,1]$ is to be compared with a value in $[0,\infty)$, the comparison must be mediated by an explicitly stated function.

**Separation between ontology and operator instantiation.** The formal specification must clearly distinguish between the ontological level (what entities exist and what roles they play) and the instantiation level (what specific functional forms those entities take in the current candidate realization). Axioms belong to ontology. Provisional operator forms belong to instantiation. These must not be interleaved without clear markers.

**Distinction between axioms and candidate functional forms.** An axiom is a property that any admissible realization of an operator must satisfy. A candidate functional form is a specific function that is believed to satisfy the axioms but is not the only possible such function. The agent must never present a candidate form as an axiom (which would over-constrain the theory) or an axiom as a candidate form (which would under-commit the theory).

**Careful treatment of time and persistence.** Temporal indices, temporal windows, and transport kernels must be handled with care. The agent must not assume that $X_t = X_s$ for $t \neq s$ unless this is explicitly stated as a simplifying assumption. The agent must not assume that transport is deterministic, injective, or surjective unless these properties are imposed by a specific axiom or realization.

**Preservation of conceptual content during formal rewriting.** When rewriting informal or semi-formal material into fully formal notation, the agent must verify that the formal version captures the conceptual content of the original. A formal rewriting that is logically correct but conceptually impoverished—that captures the letter but not the spirit—is not acceptable. If a conceptual claim cannot be fully formalized with current tools, the claim must be preserved as an interpretive remark alongside the partial formalization.

**No undefined symbols or hidden assumptions.** Every symbol that appears in a formal statement must have been previously defined. Every assumption on which a formal claim depends must be explicitly stated. If an assumption is standard and widely known, it must still be stated; "obvious" assumptions are a primary vector for hidden conceptual drift.

---

## 8. Rules for Interpretation

The theory of Soft Cognitive Cohesion is not a purely syntactic system. Its formal constructs carry conceptual meaning, and that meaning must be preserved during all downstream work. The following interpretive commitments are binding.

The theory is about the emergence of coherent "somethingness" prior to discrete objecthood. This is its central concern. Every formal construct—from the cohesion field to the energy functional—exists to articulate some aspect of how coherent formations emerge from unstructured relational fields. An agent who treats the formalism as a self-contained game of symbols, disconnected from this foundational question, has departed from the theory.

Object-like entities are derived stabilization phenomena. When the theory speaks of "objects," it means formations that have achieved robust proto-cohesion: sufficient binding, separation, morphological articulation, and temporal persistence. Objects in this sense are not inputs to the formal system but distinguished outputs—states that satisfy all four conditions simultaneously and stably. The agent must never import an external notion of objecthood (e.g., from detection pipelines or instance segmentation) as if it were native to the theory.

The theory is not merely a segmentation formalism. Segmentation begins from the assumption that the world is composed of regions to be labeled. This theory begins earlier: from the question of how regions emerge at all. The formal apparatus may be applied to segmentation tasks in practice, but the agent must not allow this practical application to redefine the theoretical intent.

The language of implementation must not erase the ontology of graded cohesion. When producing implementation-oriented material, the agent will inevitably use terms like "mask," "score," "label," and "prediction." These terms are permissible in implementation documents, provided they are explicitly connected to their theoretical counterparts. The agent must not allow implementation vocabulary to silently replace the theory's own conceptual vocabulary. If an implementation document speaks of "masks," it must state that masks are thresholded projections of soft cohesion fields, not primitive entities.

---

## 9. Prohibited Distortions

The following misreadings, substitutions, and simplifications are prohibited. An agent who introduces any of these distortions has failed to comply with the instructions in this document.

- **Reducing the theory to fuzzy segmentation.** The theory is not a fuzzy version of image segmentation. Its primitives, its question, and its ontological commitments are different in kind from those of segmentation frameworks. Fuzzy membership in a class is not the same concept as graded cohesive participation.

- **Making crisp sets primitive.** Introducing crisp subsets $A_t \subseteq X_t$ as foundational entities and then "softening" them into $u_t$ inverts the ontological direction of the theory. The soft field is primary; the crisp set is derived.

- **Treating boundary as necessarily sharp.** Boundary in this theory is a transition band, not a contour. Any formalization that forces all boundaries to be sharp (e.g., by requiring $u_t$ to take values only in $\{0, 1\}$ except on a measure-zero set) violates the canonical commitment.

- **Reducing distinction to local contrast only.** Distinction is exterior asymmetry—a property that depends on the relational configuration of the entire complementary field, not merely on the difference between a site and its immediate neighbors. Replacing $\mathbf{D}_t(x; 1-u_t)$ with a simple local gradient or edge detector destroys this field-relative character.

- **Reducing persistence to tracking IDs.** Temporal identity is structural inheritance of the cohesive core under transport. It is not the propagation of a detection ID from one frame to the next. Replacing $\mathbf{M}_{t \to s}$ with a Hungarian-matching assignment or a detection-association pipeline eliminates the theory's concept of persistence entirely.

- **Treating optimization as ontology.** The choice of optimization method (gradient descent, evolutionary search, variational inference) is an implementation decision. It does not define what cohesion, closure, or distinction are. An agent who describes the theory as "a method for optimizing a loss function" has collapsed the ontological layer into the engineering layer.

- **Replacing conceptual commitments with convenient engineering shortcuts.** If an engineering approximation is introduced—for example, replacing the full transport kernel with a sparse nearest-neighbor assignment for computational efficiency—it must be explicitly marked as an approximation, its relationship to the canonical form must be stated, and the conceptual limitations of the shortcut must be documented. Silent substitution is prohibited.

---

## 10. Validation Criteria for Future Agent Outputs

Every artifact produced by a future agent must satisfy the following evaluation criteria before it can be accepted as part of the theory's development record.

**Fidelity to theoretical commitments.** The artifact must be consistent with every fixed commitment listed in Section 3 of this document. If the artifact contradicts or omits a commitment, it must be revised. There is no exception for "minor" or "temporary" violations.

**Formal consistency.** All definitions, axioms, and derived results must be internally consistent. Type signatures must be respected. Quantifiers must be correctly scoped. No formal claim may depend on an unstated assumption.

**Notational discipline.** Symbols must be used consistently. Every symbol must be defined before use. No two distinct concepts may share a symbol within a single document. Notation must be compatible across documents within the theory's artifact stack.

**Explicit handling of open problems.** Every open question encountered during the work must be recorded in the unresolved-issues register. The agent must not resolve open questions silently. If a provisional resolution is adopted for the purposes of a specific document, it must be explicitly marked as provisional.

**Non-collapse of distinct conceptual layers.** The artifact must maintain the distinction between ontology, axiomatics, provisional realization, optimization, and implementation. If the artifact addresses multiple layers (e.g., an implementation specification that references axiomatic properties), the layers must be clearly labeled and visually separated.

**Readiness for later implementation inheritance.** Formal documents must be written with enough precision that an implementation agent can inherit definitions, operator forms, and energy terms without ambiguity. This does not mean that formal documents must contain code; it means that every formal definition must be specific enough to admit a unique computational interpretation (or, if ambiguity remains, that the ambiguity is explicitly flagged).

Elegance alone is not a sufficient criterion. A formally elegant document that distorts the theory's commitments is worse than a plain document that preserves them. Conceptual faithfulness takes priority over aesthetic considerations in all cases.

---

## 11. Interaction Protocol for Future Agents

When a future agent encounters ambiguity, incompleteness, or tension within the theory's materials, it must follow the protocol described below.

**Preserve fixed commitments unconditionally.** If an ambiguity can be resolved in a way that is consistent with the fixed commitments, adopt that resolution. If it cannot—if the ambiguity reveals a genuine tension within the commitments themselves—flag the tension explicitly and do not attempt to resolve it silently. Tensions at the level of foundational commitments require deliberate theoretical work, not agent-level workarounds.

**Mark open issues explicitly.** Every point at which the agent makes a choice that is not uniquely determined by the canonical specification must be marked with a clear annotation: "provisionally adopted," "currently preferred candidate," "open—multiple approaches viable," or similar. The annotation must state what alternatives exist and why the chosen option was selected.

**Avoid silently making foundational substitutions.** A foundational substitution is any change that alters the meaning of a primitive concept, the scope of an axiom, or the ontological priority of the soft system. Such changes may sometimes be warranted, but they must never be introduced silently. If the agent believes a foundational modification is necessary, it must state the modification, justify it against the conceptual-origin material, and flag it for review.

**State when something is provisional.** The word "provisional" is not a sign of weakness; it is a sign of intellectual honesty. Every candidate operator form, every suggested threshold, every proposed regularity condition that is not directly entailed by the canonical axioms must be labeled as provisional. The theory's strength lies in the clarity of its commitments, not in premature closure of its open questions.

**Distinguish "currently adopted candidate form" from "canonical commitment."** This distinction must be maintained at all times. A currently adopted candidate form is a specific function or procedure that is believed to satisfy the canonical axioms and is presently in use. A canonical commitment is a principle or axiom that defines the identity of the theory. The former may be replaced; the latter may not (except through deliberate foundational revision). The agent must never promote a candidate form to canonical status without explicit justification, and must never demote a canonical commitment to candidate status.

---

## 12. Recommended Output Stack

The theory's development should produce a layered stack of artifacts, each serving a distinct function. The layers must not be conflated. Each document must state which layer it belongs to.

**Layer 1: Conceptual-Origin Document.** This document reconstructs the reasoning path that made the theory necessary. It explains the dissatisfaction with object-first frameworks, the turn to pre-objective cohesion, the emergence of closure, distinction, boundary, and transport as structural requirements, and the eventual need for axiomatization. It is the motivational and philosophical foundation of the entire stack. It does not contain formal definitions; it contains the conceptual justifications that inform and constrain all formal work.

**Layer 2: Canonical Specification.** This document ($\texttt{Canonical Spec.md}$) is the authoritative formal specification of the theory in its current state. It declares the formal universe, the primitive entities, the axiomatic groups, the derived predicates, the minimal energy principle, and the provisional operator realizations. It separates fixed commitments from open design choices. All other formal documents in the stack must be consistent with this specification.

**Layer 3: Agent Instructions.** This document (the present document) governs how future agents must engage with the theory. It specifies responsibilities, work order, deliverables, validation criteria, and prohibited distortions. It is the procedural and normative layer of the stack.

**Layer 4: Implementation-Oriented Specification.** This document (to be produced when appropriate) translates the canonical theory into a form suitable for computational realization. It may include data structure designs, algorithmic procedures, parameter ranges, optimizer configurations, and engineering trade-off analyses. It must inherit from the canonical specification and must not contradict it. It must be clearly labeled as implementation-layer material.

**Layer 5: Schema or Machine-Readable Registry** (optional). A structured, machine-readable representation of the theory's entities, operators, axioms, and parameters. This may take the form of a JSON schema, a type-system declaration, or a formal ontology file. Its purpose is to enable automated consistency checking and to support tooling for future development. It must be generated from, and validated against, the canonical specification.

These layers are ordered by conceptual priority. Layer 1 motivates Layer 2; Layer 2 authorizes Layer 3; Layers 1–3 jointly constrain Layers 4 and 5. An artifact at a lower layer must never override a commitment at a higher layer. If a conflict arises between layers, the higher layer takes precedence, and the lower-layer artifact must be revised.

---

## 13. Closing Directive

The mission of every future agent who works on this theory is singular and non-negotiable: to continue the formal development of the theory of Soft Cognitive Cohesion—to refine its notation, to sharpen its definitions, to resolve its open questions, to prepare it for computational realization—without betraying the foundational problem that made it necessary, without inverting its ontological priorities, and without collapsing the graded, relational, pre-objective character of cohesion into the very object-first frameworks that the theory was built to surpass.
