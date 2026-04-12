---
id: META-0002
type: meta/ontology
status: accepted
last_updated: 2026-04-12
---

# Ontology: Core Concepts of Soft Cognitive Cohesion

## Primitive vs. Derived

This ontology follows a strict hierarchy:

### Layer 0: Primitives (Foundational)

**These are NOT derived from anything else; they define the universe of SCC.**

1. **Soft Cohesion Field** `u_t : X_t → [0,1]`
   - Definition: A real-valued function mapping relational support space X_t into the unit interval
   - Role: The primitive entity; everything else is understood in terms of u_t
   - Axioms: A1 (non-negativity), A2 (boundedness), A3 (closure tendency)
   - Why primitive: There is no "prior" discrete object; formations emerge from u_t dynamics
   - Danger: Never invert this. Objects are not primitive; they are derivative phenomena

2. **Relational Support Space** `X_t`
   - Definition: Graph or contact structure at time t; vertices and edges
   - Role: Domain on which u_t is defined
   - Constraint: Fixed per-formation (no dynamic topology change in single-field model)

3. **Energy Functional** `E(u_t)`
   - Definition: Variational principle; sum of four independent terms
   - Components: E_cl (closure), E_sep (separation), E_bd (boundary), E_tr (transport)
   - Role: Determines u_t dynamics; u* = argmin E on constraint surface
   - Why separate: Each term corresponds to distinct physical/conceptual principle

### Layer 1: Axiomatic Operators (From Primitives)

**These are defined via axioms that constrain interaction with the primitive field.**

4. **Closure Operator** `Cl_t : [0,1]^n → [0,1]^n`
   - Axiom: A3' (conditional extensivity)
   - Behavior: u_t → Cl_t(u_t) = u_t + [stabilization correction]
   - Fixed Point: Cl_t(u*) = u*, so u* is "closed"
   - Danger: Do NOT assume idempotence (Cl ∘ Cl ≠ Cl in general)
   - Status: Axiomatically defined; implementation is provisional

5. **Distinction Operator** `D_t : [0,1]^n → [0,1]^n`
   - Axiom: D (contrast on 1 - u_t)
   - Behavior: Quantifies "boundary richness" at each position
   - Constraint: b_D = 0 (required for energy analyticity)
   - Status: Axiomatically defined; exact form provisional

6. **Resolvent (Co-belonging)** `C_t : [0,1]^n → [0,1]`
   - Definition: L^{-1}[u_t] where L is the graph Laplacian
   - Role: Measures global integration of u_t across X_t
   - Status: Derived from graph structure + u_t (demoted from formal universe in v2.0)
   - Danger: Never treat C_t as primitive; it is conditional on X_t

7. **Transport Kernel** `M_{t→s} : [0,1]^n_s × [0,1]^n_t → [0,1]`
   - Definition: Temporal correspondence; "how does u_t inherit from u_s?"
   - Implementation: Cohesion fingerprint → entropy-regularized OT → fixed-point
   - Status: Provisionally defined; exact form an open problem
   - Danger: Transport is NOT "tracking" (no object IDs)

### Layer 2: Diagnostic Concepts (Derived from Primitives + Operators)

**These are measurements that probe the state of u_t.**

8. **Proto-Cohesion Diagnostic Vector** `d = (Bind, Sep, Inside, Persist) ∈ [0,1]^4`
   - **Bind (ℓ²/√n):** "How concentrated is u_t?" (cohesion strength)
   - **Sep (u-weighted distance):** "How separated are multiple fields?" (K-field spacing)
   - **Inside (H₀ persistence Q_morph):** "How persistent is core across time?" (topological stability)
   - **Persist:** "How much of u_t carries forward temporally?" (transport fidelity)
   - Role: Operationalization of "does this look like a coherent formation?"
   - Status: Empirically validated; theoretically grounded in topology + transport

9. **Boundary** `B_t`
   - Definition: (UNDER DEVELOPMENT) Region where u_t transitions sharply; measured via D_t
   - Current proxy: Locations where D_t(u_t) > threshold
   - Danger: This is NOT a crisp set; it is a graded concept
   - Status: Tentative; D-0004 in registries

### Layer 3: Multi-Field Extensions (K-field Architecture)

**These apply when modeling K independent fields with inter-formation coupling.**

10. **K-Field Configuration** `{u¹_t, u²_t, ..., u^K_t}`
    - Definition: K soft fields over a *shared* relational space
    - Constraint: Simplex participation: Σ_j u^j_t(x) = 1 for all x
    - Repulsion: E_rep = λ_rep × [inter-formation repulsion energy]
    - Status: Axiomatically grounded; implementation via multi.py
    - Danger: **Fixed K assumption** — the "fixed m" constraint is often implicit

11. **Per-Formation Mass** `m_j = ∫ u^j_t dx`
    - Definition: "Volume" or "size" of formation j
    - Constraint: Usually externally imposed (m_j = m₀ for all j, or Σ m_j = M)
    - Problem: F-1 criticism — if m_j is allowed to vanish, K decreases, violating "fixed K"
    - Status: Accepted mathematically; philosophically problematic

12. **Global Minimum / Stability (Fixed K)**  
    - Definition: u* = argmin_{u : Σ u_j(x)=1} E
    - Condition: ONLY meaningful if K is externally fixed
    - Danger: If K is allowed to vary, then K=1 (all mass in one field) always wins (M-1)
    - Status: **Requires explicit disclaimer in Canonical Spec v1.2**

### Layer 4: Not (Yet) Primitives — Rejected Framings

**These are NOT primitive in SCC and must never be reintroduced.**

- **Crisp Objects:** "Things" with sharp boundaries. Derivative, not primitive.
- **Object IDs / Tracking:** Persistent labels. Not defined in SCC; emergence is post-hoc.
- **Fuzzy Set Membership:** u_t is not "degree to which x belongs to object O"; O doesn't exist primitively.
- **Clustering:** Pre-assigned point cloud with membership inference. Not our model.
- **Gestalt Rules:** Fixed perceptual principles (closure, continuity, etc.). Too rigid; SCC is variational.

## Conceptual Dependencies

```
Layer 0 (Primitives)
├── u_t : X_t → [0,1]
├── X_t (relational support)
└── E(u_t) (energy functional)
    │
Layer 1 (Axiomatic Operators)
├── Cl_t (axiom A3')
├── D_t (axiom D)
├── C_t (resolvent)
└── M_{t→s} (transport)
    │
Layer 2 (Diagnostics)
├── d = (Bind, Sep, Inside, Persist)
└── B_t (boundary)
    │
Layer 3 (Multi-Field)
├── {u^j_t} (K-field)
├── m_j (per-formation mass)
└── Global stability (fixed K)
```

## Critical Assumptions (Implicit in Current Spec)

These must be stated explicitly in Canonical Spec v1.2:

1. **Fixed Relational Structure:** X_t is given (no dynamic topology)
2. **Fixed K (Number of Formations):** K is imposed externally, not derived from energy minimization
3. **Fixed Per-Formation Mass:** m_j is held constant (or Σ m_j = M constant)
4. **Volume Constraint:** ∫ u^j_t dx = m_j exactly
5. **No Discrete Objects Initially:** We start with u_t, not with labeled point sets

## Known Vulnerabilities

| Concept | Vulnerability | Severity | Status |
|---------|---|---|---|
| K-Field Global Stability | F-1: Vacuous without external m constraint | CRITICAL | Unresolved |
| Energy Minimization | M-1: K=1 always preferred in unconstrained landscape | CRITICAL | Unresolved |
| Morse Theory | MO-1: M₂ is manifold with corners; smooth theory invalid | CRITICAL | Unresolved |
| Boundary Definition | B_t via D_t is provisional; exact form uncertain | HIGH | Tentative (D-0004) |
| Transport Kernel | M_{t→s} form may not capture all temporal persistence modes | MEDIUM | Under investigation |

## Philosophical Position

### What SCC IS

- A **variational theory** of pre-objective formation
- A **field-based** model (not particle-based)
- An **axiomatically grounded** framework (not ad-hoc rules)
- **Ontologically committed** to soft cohesion as primitive

### What SCC IS NOT

- A **fuzzy logic** system
- An **object-tracking** algorithm
- A **clustering** framework
- A **gestalt psychology** formalization

### Core Commitment

> The soft cohesion field u_t is the primitive entity. All structure (boundaries, multiple formations, temporal persistence) emerges from variational dynamics on u_t, not from discrete objects.

---

**Last updated:** 2026-04-12  
**See also:** concept_registry.md, symbol_registry.md (in 03_context_memory)
