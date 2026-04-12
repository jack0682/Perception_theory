# Formal Systems Architecture Report: Soft Cognitive Cohesion

**Role:** Formal Systems Architect (Teammate 2)
**Task:** Structural diagnosis and refactoring hypotheses
**Date:** 2026-03-26

---

## A. Structural Diagnosis

### A.1. What Is Well-Separated

**Primitives are clearly declared (Section 3).** The formal universe tuple `C^soft` is stated upfront with explicit type signatures for every component. The nine subsections (3.1-3.9) each introduce one primitive with its domain, codomain, and conceptual role. This is architecturally clean — it reads like a proper signature declaration.

**Axiomatic Groups (Section 6) are internally well-organized.** Groups A-E each address a single operator family. Axioms are numbered, named, and followed by interpretive remarks that are clearly marked as such.

**Fixed vs. Open (Section 11) is explicitly partitioned.** The 8 fixed commitments and 7 open design choices are clearly enumerated. This is one of the strongest architectural features.

**Provisional operator forms (Section 9) are clearly labeled as provisional.** The section's preamble explicitly states these are "currently favored realizations, not permanently fixed definitions."

**Open Problems (Section 12) are catalogued.** Eight distinct open problems are listed with enough context to understand their scope and constraints.

---

### A.2. Where Layer Boundaries Are Violated or Blurred

**VIOLATION 1: Derived notions (Section 5) sit between primitives (Section 3) and axioms (Section 6).**

Core, Interior, Boundary Band, and Exterior are derived by thresholding $u_t$. They introduce threshold parameters ($\theta_{\mathrm{core}}$, $\theta_{\mathrm{in}}$, $\theta_1$, $\theta_2$, $\theta_{\mathrm{ext}}$) whose status is ambiguous. Worse, the derived notions are *used* inside the axioms (E3 references Core_t) and the proto-cohesion predicate (Section 7 references Int_t, Core_t, Bd_t). This creates a circular dependency problem. The boundary band section also introduces the gradient indicator $g_t(x; u)$ which is essentially an operator candidate form embedded in a "derived notions" section — a layer confusion.

**VIOLATION 2: Philosophical argumentation is interleaved with formal specification.**

Sections 2 (Foundational Orientation), 4 (Why the Soft Form Is Primary), and 10 (Structural Interpretation) are Layer 1 motivational material living inside the Layer 2 Canonical Spec. This means the Canonical Spec does double duty as both motivational document and formal specification, violating the Agent Instructions' own prescribed layering.

**VIOLATION 3: The proto-cohesion predicate (Section 7) mixes axiomatic and derived layers.**

The four component predicates (Bind, Sep, Inside, Persist) are defined using specific functional forms — norms, averages over sets, summations. These are not abstract axioms; they are concrete mathematical expressions that commit to particular measurement strategies. They have the character of provisional operator forms dressed as axioms.

**VIOLATION 4: Group D conflates two conceptually distinct operators.**

Distinction ($D_t$) and Transition ($T_t$) are bundled into a single axiomatic group. They have different type signatures, different conceptual roles, and different open/fixed statuses. The justification ("jointly prevent degenerate solutions") is a *functional* argument about energy minimization, not a *structural* argument about operator classification.

**VIOLATION 5: Energy principle (Section 8) has ambiguous layer membership.**

Is the energy functional an axiom, a derived consequence, or a provisional realization? The four-term *structure* is a fixed commitment (per Section 11), but the specific *forms* of each term seem provisional. This distinction is not made within Section 8 itself.

**VIOLATION 6: The gradient indicator $g_t$ appears in three different contexts.**

Introduced in Section 5.3 (derived notions), reappears in Section 9.3 (provisional distinction operator), and is implicitly present in the boundary energy term (Section 8.3). Its formal status is never clarified.

**VIOLATION 7: Naming inconsistency between energy terms and axiomatic groups.**

The mapping between axiom groups and energy terms is not one-to-one. Group C (co-belonging) has *no corresponding energy term*. Group B (adjacency) has no direct energy term — it appears implicitly through the smoothness penalty in $\mathcal{E}_{\mathrm{bd}}$.

---

### A.3. Dependency Problems

1. **Circular reference**: Axiom E3 references Core_t, a derived notion defined by thresholding with parameter $\theta_{\mathrm{core}}$.
2. **Proto-cohesion predicates depend on derived notions**: Sep_t uses Int_t, Inside_t uses Core_t and Bd_t, Persist uses Core_t.
3. **Energy terms depend on provisional operators**: $\mathcal{E}_{\mathrm{sep}}$ uses $D_t$, $\mathcal{E}_{\mathrm{cl}}$ uses $\mathrm{Cl}_t$, $\mathcal{E}_{\mathrm{tr}}$ uses $M_{t \to s}$.
4. **No explicit dependency on co-belonging**: $C_t$ is declared primitive but appears in *zero* axioms that bind it, *zero* energy terms, and *zero* proto-cohesion predicates. It is a declared primitive with no downstream consumers.

---

## B. Three Competing Refactoring Architectures

### Hypothesis 1: "Strict Stratification" — Layer-Pure Document Decomposition

**Principle**: Each document corresponds to exactly one abstraction layer.

**Proposed structure**:

```
Module 1: ONTOLOGY (Primitives Only)
  - T, {X_t}, u_t, six operator *slots* with type signatures only
  - NO threshold parameters, NO derived notions, NO functional forms

Module 2: AXIOMATICS (Abstract Properties Only)
  - Groups A-E, stated purely in terms of Module 1 primitives
  - All axioms rewritten to avoid reference to derived notions

Module 3: DERIVED NOTIONS (Defined from Modules 1+2)
  - Core, Interior, Boundary Band, Exterior
  - Gradient indicator g_t
  - Explicit threshold parameter registry

Module 4: PREDICATES (Defined from Modules 1-3)
  - Proto-cohesion predicate and its four components

Module 5: ENERGY PRINCIPLE (Structural commitment + provisional forms)
  - Four-term structure declared as fixed
  - Specific functional forms marked as provisional

Module 6: PROVISIONAL REALIZATIONS (All candidate forms)

Module 7: COMMITMENTS & OPEN PROBLEMS (Registry)
```

**Pros**: Maximum layer purity, single responsibility per module, clear dependency chain, makes co-belonging gap visible.

**Cons**: Splits Canonical Spec into 7+ modules, may destroy narrative coherence, some axioms become awkward without derived notions, over-engineering for ~600 lines.

---

### Hypothesis 2: "Annotated Monolith" — Single Document with Explicit Layer Tags

**Principle**: Keep the Canonical Spec as one document but annotate every element with its formal layer membership.

**Tags**: [PRIMITIVE], [AXIOM], [DERIVED], [PREDICATE], [ENERGY-FIXED], [ENERGY-PROVISIONAL], [REALIZATION], [PARAMETER], [OPEN], [MOTIVATION]

**Pros**: Preserves narrative unity, tags make cross-layer references visible, lower refactoring cost, compatible with future machine-readable extraction.

**Cons**: Annotations add visual noise, doesn't enforce separation (only reveals violations), still a monolith.

---

### Hypothesis 3: "Operator-Centric Modular Architecture" — Organize by Operator

**Principle**: Instead of organizing by abstraction layer, organize by *operator family*. Each operator gets a complete vertical slice.

**Proposed structure**:

```
Preamble: Formal Universe
Module Cl: CLOSURE (primitive + axioms + derived + energy + predicate + realization + open)
Module N: ADJACENCY (...)
Module C: CO-BELONGING (...)
Module D: DISTINCTION (...)
Module T_op: TRANSITION (...)
Module M: TEMPORAL TRANSPORT (...)
Cross-Cutting: Derived notions, Proto-Cohesion, Energy Principle, Registry
```

**Pros**: Makes co-belonging gap structurally visible, each operator's full "stack" is co-located, supports independent development.

**Cons**: Breaks narrative flow, cross-cutting concerns don't fit neatly, energy principle's structural independence harder to state, risk of duplicating shared infrastructure.

---

## C. Recommended Layered Architecture

**Recommendation: Hybrid of Hypothesis 1 and 2 — "Layered Spec with Operator Cross-Reference"**

Preserves the Canonical Spec as a **single primary document** reorganized into **clearly demarcated layer blocks** with an accompanying **operator cross-reference table**.

### Recommended Structure

```
CANONICAL SPECIFICATION (single document, reorganized)

LAYER BLOCK 0: STATUS & READING GUIDE
LAYER BLOCK 1: PRIMITIVE ONTOLOGY
  - Formal universe tuple, type signatures only

LAYER BLOCK 2: AXIOMATIC GROUPS
  - Group A: Closure (A1-A3)
  - Group B: Adjacency (B1-B4)
  - Group C: Co-belonging (C1-C3) [OPEN marker]
  - Group D: Distinction (D-Ax1-3) [SEPARATED from Transition]
  - Group D': Transition (T-Ax1-2) [OWN GROUP, OPEN marker]
  - Group E: Transport (E1-E4)
  - KEY CHANGE: E3 restated with inline threshold, not Core_t

LAYER BLOCK 3: DERIVED NOTIONS
  - Core_t, Int_t, Bd_t, Ext_t, g_t
  - Threshold parameter table

LAYER BLOCK 4: PROTO-COHESION PREDICATE
  - Bind, Sep, Inside, Persist -> ProtoCoh
  - Open question: are predicate forms axiomatic or provisional?

LAYER BLOCK 5: ENERGY PRINCIPLE
  5a. STRUCTURAL COMMITMENT (fixed): four-term architecture
  5b. PROVISIONAL ENERGY FORMS (replaceable): specific functionals

LAYER BLOCK 6: PROVISIONAL OPERATOR REALIZATIONS

LAYER BLOCK 7: FIXED COMMITMENTS & OPEN REGISTRY
  Including OPERATOR STATUS TABLE:
  | Operator | Type Sig | Axioms | Energy Term | Predicate Role | Realization | Status |

SEPARATE DOCUMENTS:
  - "Foundational Orientation" (current Sections 2, 4, 10) -> Layer 1
  - Agent Instructions -> Layer 3 (already separate)
```

### Key Architectural Decisions

1. **Separate Distinction from Transition into Groups D and D'.** Different type signatures, different open/fixed statuses, different conceptual roles.

2. **Split energy principle into structural commitment (5a) and provisional forms (5b).** The four-term architecture is fixed; specific forms are not.

3. **Extract philosophical sections to a separate document.** Sections 2, 4, and 10 are Layer 1 material. This is the single highest-impact change.

4. **Rewrite Axiom E3 to eliminate dependence on derived notions.** Use inline threshold instead of Core_t reference.

5. **Add the Operator Status Table (Block 7d).** Makes co-belonging gap, transition gap, and asymmetric development immediately legible.

6. **Flag the co-belonging orphan.** C_t participates in no energy term and no proto-cohesion predicate component.

7. **Flag the ambiguous status of proto-cohesion predicate forms.** Are they definitions or provisional realizations?

---

### Summary of Findings

| Issue | Severity | Fix |
|-------|----------|-----|
| Philosophical content inside formal spec | High | Extract to Layer 1 document |
| Derived notions referenced by axioms (circular) | High | Inline thresholds in axioms |
| D and T_t bundled in one group | Medium | Separate into Groups D and D' |
| Energy forms presented as if axiomatic | High | Split energy into structure vs. forms |
| Co-belonging has no energy term or predicate role | High (gap) | Flag in open problems + operator table |
| g_t appears in 3 contexts without clear status | Medium | Assign to Derived Notions |
| Proto-cohesion predicate forms: axiom or realization? | Medium | Flag explicitly in Block 4 |
| Axiom groups don't map 1-to-1 to energy terms | Low | Document mapping in operator table |
