---
id: META-0101
type: registry/concepts
status: accepted
last_updated: 2026-04-12
---

# Concept Registry (D-xxxx)

**Purpose:** Immutable record of all conceptual primitives and derived concepts in SCC theory. Every concept used in claims, proofs, or discussions must be registered here.

**Format:** Each row is a registered concept with its definition, status, and usage.

---

## Registry Table

| ID | Name | Definition | Type | Status | First Used | Used In | Notes |
|----|------|-----------|------|--------|-----------|---------|-------|
| **D-0001** | Soft Cohesion Field | u_t : X_t → [0,1]; primitive function mapping relational space to cohesion strength | Primitive | accepted | 03-26 | C-0001, P-0001, all others | Ontological primitive; never invert |
| **D-0002** | Relational Support Space | X_t = (V_t, E_t); graph structure at time t (vertices, edges) | Primitive | accepted | 03-26 | C-0001, D-0001 | Fixed per-formation; no dynamic topology |
| **D-0003** | Energy Functional | E(u_t) = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd + λ_tr E_tr | Primitive | accepted | 03-27 | C-0001, P-0001 | Four independent terms |
| **D-0004** | Closure Operator | Cl_t : [0,1]^n → [0,1]^n; axiom A3' (conditional extensivity) | Axiomatic | accepted | 03-27 | C-0002, P-0002 | Stabilization tendency, not idempotent |
| **D-0005** | Distinction Operator | D_t : [0,1]^n → [0,1]; boundary contrast on (1 - u_t) | Axiomatic | accepted | 03-27 | C-0003, E-0010 | Constraint: b_D = 0 for analyticity |
| **D-0006** | Resolvent (Co-belonging) | C_t = L^{-1}[u_t]; global integration measure | Derived | accepted | 03-30 | C-0004, P-0004 | Demoted from formal universe in v2.0 |
| **D-0007** | Transport Kernel | M_{t→s} : [0,1]^n_s × [0,1]^n_t → [0,1]; temporal correspondence via OT | Axiomatic | tentative | 04-01 | C-0005, E-0015:E-0020 | Form provisional; under investigation |
| **D-0008** | Proto-Cohesion Diagnostic | d = (Bind, Sep, Inside, Persist) ∈ [0,1]^4 | Derived | accepted | 04-01 | E-0001:E-0079, C-0010 | Operational measurement of formations |
| **D-0009** | Bind (Cohesion Strength) | ℓ²(u_t) / √n; concentration measure | Derived | accepted | 04-01 | E-0005, C-0010 | How concentrated is u_t? |
| **D-0010** | Sep (Separation Distance) | u-weighted average distance between K formations | Derived | accepted | 04-01 | E-0015:E-0020, C-0007 | Multi-field spacing metric |
| **D-0011** | Inside (Topological Persistence) | H₀ persistence Q_morph; core topological stability | Derived | accepted | 04-01 | E-0025, C-0011 | How persistent is core? |
| **D-0012** | Persist (Transport Fidelity) | Transport-based carry-forward measure; M_{t→s} application | Derived | tentative | 04-06 | E-0030:E-0035, C-0009 | Form under investigation; core-overlap proxy working |
| **D-0013** | Boundary (Graded) | Region where D_t(u_t) > threshold; sharp transition region | Derived | tentative | 04-10 | C-0008, E-0040 | D-0004 in development; not yet crisp definition |
| **D-0014** | K-Field Configuration | {u¹_t, u²_t, ..., u^K_t}; K independent fields, simplex constraint | Extension | accepted | 04-07 | C-0012:C-0020, P-0015 | Multi-formation coupling |
| **D-0015** | Per-Formation Mass | m_j = ∫ u^j_t dx; "volume" of formation j | Derived | accepted | 04-07 | C-0012, A-0005 | Usually externally imposed; problematic in F-1 |
| **D-0016** | Global Minimum (Fixed K) | u* = argmin_{u : Σ u_j=1} E; optimization solution | Derived | tentative | 04-07 | C-0012, X-0001 | Only valid if K fixed externally; F-1 critical issue |
| **D-0017** | Repulsion Energy | E_rep = λ_rep × [inter-formation penalty]; K-field separation | Derived | accepted | 04-10 | E-0066:E-0079, C-0015 | Branch selection related; R1 experiments |
| **D-0018** | Formation Fingerprint | Cohesion signature for transport matching (curve in (Bind, Sep, Persist)) | Derived | tentative | 04-11 | E-0030, P-0016 | Used in M_{t→s} transport kernel definition |
| **D-0019** | Category A (Unconditional) | Theorem proved without special assumptions beyond SCC axioms | Meta | accepted | 04-01 | promotion_rules.md | Fully accepted; canonical ready |
| **D-0020** | Category B (Conditional) | Theorem proved under stated conditions (e.g., "generic parameters") | Meta | accepted | 04-01 | promotion_rules.md | Conditional; needs disclaimer |
| **D-0021** | Category C (Very Conditional) | Theorem proved only under restrictive regime (e.g., "well-separated K-field") | Meta | accepted | 04-01 | promotion_rules.md | Very restrictive; specialty result |
| **D-0022** | Crisp Object | (Rejected) "Thing" with sharp boundary; derivative, not primitive in SCC | Anti-concept | deprecated | 03-26 | ontology.md | **NOT USED**: objects are emergent |
| **D-0023** | Object ID / Tracking | (Rejected) Persistent label for individuals; not defined in SCC | Anti-concept | deprecated | 03-26 | ontology.md | **NOT USED**: no tracking in field theory |
| **D-0024** | Fuzzy Set | (Rejected) "Degree to which x belongs to object"; wrong ontology for SCC | Anti-concept | deprecated | 03-26 | ontology.md | **NOT USED**: u_t is not membership function |
| **D-0025** | Clustering | (Rejected) Pre-assigned point cloud with inference; not SCC model | Anti-concept | deprecated | 03-26 | ontology.md | **NOT USED**: no point sets in SCC |

---

## Pending Concepts (Under Development)

| ID | Name | Definition | Type | Status | Blocker | Notes |
|----|------|-----------|------|--------|---------|-------|
| **D-0026** | Boundary (Crisp) | UNDER DEVELOPMENT | Derived | seed | MO-1 | Stratified Morse theory required? |
| **D-0027** | Object Emergence | How u_t → crisp objects (if at all) | Meta | seed | OP-0001 | Requires F-1 resolution |
| **D-0028** | Dynamic Topology | Evolution of X_t itself (change in connectivity) | Extension | seed | R3 | Not in current theory scope |
| **D-0029** | Multi-scale Cohesion | Hierarchy of fields at different scales | Extension | seed | R2 | Future work (roadmap item) |

---

## Concept Groups (Hierarchical)

### Layer 0: Primitives (Foundational)
- D-0001: Soft Cohesion Field
- D-0002: Relational Support Space
- D-0003: Energy Functional

### Layer 1: Axiomatic Operators
- D-0004: Closure Operator (axiom A3')
- D-0005: Distinction Operator (axiom D)
- D-0006: Resolvent (derived from axioms)
- D-0007: Transport Kernel (axiom E)

### Layer 2: Diagnostics (Measurements)
- D-0008: Proto-Cohesion Diagnostic Vector
- D-0009: Bind
- D-0010: Sep
- D-0011: Inside
- D-0012: Persist
- D-0013: Boundary

### Layer 3: K-Field Extensions
- D-0014: K-Field Configuration
- D-0015: Per-Formation Mass
- D-0016: Global Minimum (Fixed K)
- D-0017: Repulsion Energy
- D-0018: Formation Fingerprint

### Meta-Concepts
- D-0019: Category A
- D-0020: Category B
- D-0021: Category C

### Rejected/Anti-Concepts
- D-0022: Crisp Object (rejected)
- D-0023: Object ID (rejected)
- D-0024: Fuzzy Set (rejected)
- D-0025: Clustering (rejected)

---

## Registration Rules

1. **Every new concept gets next available ID** (D-0001, D-0002, etc.)
2. **Once registered, ID never reused** (even if concept deprecated)
3. **Status changes tracked** (in YAML header, not by moving rows)
4. **Cross-references maintained** (Used In column auto-generated by build_dependency_graph.py)

---

## Maintenance

- **Updated by:** Archivist Agent + Lead
- **Review:** Every concept added must be approved by Critic Agent
- **Validation:** find_unregistered_symbols.py checks for violations

---

**Last updated:** 2026-04-12  
**Rows:** 29 concepts (19 active, 5 pending, 5 rejected)  
**See also:** symbol_registry.md (S-xxxx), theorem_registry.md (C-xxxx, P-xxxx), assumption_registry.md (A-xxxx)
