---
id: ROADMAP-0001
type: roadmap/master_map
status: accepted
last_updated: 2026-04-12
---

# Master Problem Map: SCC Theory Development Landscape

**Purpose:** Organize all research questions, claims, proofs, and problems into a unified hierarchical structure. Maps dependencies and shows how problems relate to proved results.

**Format:** Problems organized by category (foundational, extension, application) with cross-links to registries (D-xxxx, C-xxxx, P-xxxx, etc.).

---

## I. Foundational Layer (Primitives & Axioms)

### I.A Ontological Questions

**Q-0001:** What is the primitive entity in pre-objective formation?
- **Answer:** Soft cohesion field u_t : X_t → [0,1]
- **Concept:** D-0001 (Soft Cohesion Field)
- **Theorem:** T-1 (Existence of Minimizers)
- **Status:** Resolved ✅

**Q-0002:** Why start with fields rather than objects?
- **Answer:** Objects are emergent; not starting points
- **Foundational commitment** stated in ontology.md (Layer 0)
- **Status:** Philosophical commitment ✅

**Q-0003:** How do relational structures support cohesion?
- **Answer:** Via graph Laplacian and diffusion-like operator dynamics
- **Concept:** D-0002 (Relational Support Space), D-0006 (Resolvent)
- **Theorems:** T-11 (Γ-Convergence), QM-1:QM-4
- **Status:** Resolved ✅

---

### I.B Axiomatic Consistency

**Q-0010:** Are axioms A1–E mutually consistent?
- **Claim:** C-0020 (Axiom Consistency)
- **Proof:** P-0020 (line-by-line verification)
- **Validation:** exp25 (no contradictions observed)
- **Result:** T-20 ✅ Category A

**Q-0011:** Does closure operator have fixed points?
- **Claims:** 
  - C-0006a: Existence (T-6a)
  - C-0006b: Stability (T-6b)
  - C-0006c: Full stability analysis (T-6-Stability)
- **Proofs:** P-0006a, P-0006b, P-0006c
- **Validation:** exp5, exp6, exp7
- **Results:** T-6a, T-6b, T-6-Stability ✅ Category A

**Q-0012:** Is the resolvent axiomatically grounded?
- **Claim:** C-0101 (C-Axioms, C3'' Symmetrization)
- **Proof:** P-0101 (conjugation identity → Schur complement)
- **Validation:** exp30–exp32 (exact FD verification 1e-9)
- **Result:** Upgraded to Category A in v1.1 ✅

---

## II. Single-Formation Theory (K=1)

### II.A Existence & Stability

**Q-0020:** Do minimizers exist on the constraint manifold Σ_m?
- **Claim:** C-0001 (Existence of Minimizers)
- **Proof:** P-0001 (compactness + lower semicontinuity)
- **Result:** T-1 ✅ Category A

**Q-0021:** Are interior minimizers stable?
- **Claim:** C-0003 (Stability of Interior Minimizers)
- **Proof:** P-0003 (Hessian analysis)
- **Result:** T-3 ✅ Category A

**Q-0022:** What is the basin of attraction structure?
- **Claim:** C-0014 (Gradient Flow)
- **Proof:** P-0014 (convergence to minimizer)
- **Validation:** exp20–exp22
- **Result:** T-14 ✅ Category A

---

### II.B Phase Transitions & Bifurcation

**Q-0030:** Is there a phase transition in the energy landscape?
- **Claims:**
  - C-0008: Core Dominance (T-8-Core)
  - C-0009: Global Bifurcation (T-8-Full)
- **Proofs:** P-0008, P-0009
- **Critical parameter:** β_crit = 4λ₂/|W''(c)|
- **Validation:** exp10–exp13
- **Results:** T-8-Core, T-8-Full ✅ Category A

**Q-0031:** What are the conditions for phase transition?
- **Theorem:** β ∈ spinodal = ((3-√3)/6, (3+√3)/6)
- **Proof:** Perturbation analysis in T-8-Full proof
- **Assumption:** A-0020 (Spinodal Condition)
- **Status:** Resolved ✅

---

### II.C Diagnostic Predicates

**Q-0040:** Can we measure cohesion quality?
- **Answer:** Yes, via proto-cohesion diagnostic d = (Bind, Sep, Inside, Persist)
- **Concept:** D-0008 (Proto-Cohesion Diagnostic)
- **Theorems:** T-Bind-Proj (τ=1/2), Predicate-Energy Bridge
- **Status:** Resolved ✅

**Q-0041:** Is there an exact energy-diagnostic alignment?
- **Claim:** C-0300 (Predicate-Energy Bridge)
- **Proof:** P-0300 (variational characterization)
- **Validation:** exp30–exp32
- **Result:** Upgraded to Category A in v1.1 ✅

**Q-0042:** What is the binding capacity?
- **Theorem:** T-Bind-Proj (Category B, τ=1/2 only)
- **Generalization:** T-Bind-Full (Category C, general τ not resolved)
- **Open:** General τ dependence (OP-0010)

---

## III. Multi-Formation Theory (K ≥ 2)

### III.A K-Field Architecture (NEW in v1.1)

**Q-0050:** Can we formalize multi-formation dynamics?
- **Answer:** Yes, via K-field configuration {u¹_t, u²_t, ..., u^K_t}
- **Concept:** D-0014 (K-Field Configuration)
- **Constraint:** Simplex participation (Σ u^j_t = 1)
- **Status:** Formalized (but F-1/M-1 unresolved)

**Q-0051:** Do K formations have global stability?
- **Claims:**
  - C-0012: K=2 global minimum (conditional)
  - C-0015: Repulsion energy effects
- **Assumption:** K fixed externally (A-0012) ⚠️ **F-1 ISSUE**
- **Status:** Conditional on unresolved F-1

---

### III.B Critical Unresolved Problems (🔴 CRITICAL)

#### **F-1: K=2 Vacuity Problem** 🔴 CRITICAL

**Q-0100:** Why is K=2 globally stable if K=1 is energetically cheaper?

**Problem statement:**
- K=2 with m₁=m₂=M/2: E ≈ 4.66 (exp data)
- K=1 with m=M: E ≈ 2.25 (exp data)
- K=1 is **50% cheaper** than K=2
- Therefore: K=2 "global stability" requires **external** mass constraint

**Impact:**
- All K-field theorems (T-Persist-K-Sep, T-Persist-K-Unified) depend on fixed-K assumption
- Without fixed K, energy minimization always selects K=1
- No mechanism yet for how K is fixed in biological/cognitive systems

**Current status:** ❌ Unresolved  
**Related:** M-1 (root cause of this issue)  
**See:** assumption_registry.md (A-0012)  
**References:** exp62, exp63, THEORY_STATUS_2026-04-12.md

#### **M-1: K=1 Energetic Preference** 🔴 CRITICAL

**Q-0101:** Is K=1 always preferred in unconstrained energy minimization?

**Problem statement:**
- M₂ landscape: E(m₁, m₂) where m₁ + m₂ = M
- As m₂ → 0: E → E_K1(m=M) monotonically
- Therefore: K=1 limit is global minimum

**Impact:**
- This is the **root cause of F-1**
- Shows K>1 can never emerge from energy optimization alone
- Requires model selection mechanism (BIC, free energy, birth-death dynamics) to explain K>1

**Current status:** ❌ Unresolved  
**Related:** F-1 (consequence of this problem)  
**See:** assumption_registry.md (A-0013)  
**References:** THEORY_STATUS_2026-04-12.md, exp data

#### **MO-1: Morse Theory Failure** 🟠 HIGH

**Q-0102:** Is Morse theory applicable to K=2 constrained manifold?

**Problem statement:**
- Σ²_M = {(u¹, u²) : m_1=m_2=M/2} has corners (non-smooth)
- Smooth Morse theory requires manifold without boundary
- Therefore: Smooth Morse theory is **inapplicable**

**Impact:**
- Theorems relying on Morse theory (T-8-Core, T-14) may be invalid on M₂
- Full global analysis of K=2 landscape incomplete
- Needs stratified Morse theory (complex alternative)

**Current status:** ❌ Unresolved  
**Alternatives:** 
  - Accept current stable results (don't claim global optimality)
  - Adopt stratified Morse framework (significant work)  
**See:** assumption_registry.md (MO-1)  
**References:** THEORY_STATUS_2026-04-12.md

---

### III.C Temporal Persistence (Multi-Temporal)

**Q-0110:** How does cohesion persist across time?

**Approaches:**
1. **Transport-based:** M_{t→s} kernel (D-0007)
2. **Topological:** H₀ persistence (D-0011)
3. **Diagnostic:** Carry-forward measure (D-0012)

**Claims & Theorems:**
- C-0400–C-0404: Transport persistence (T-Persist-1(a–e))
- C-0500–C-0502: K-field persistence (T-Persist-K-Sep, Weak, Unified)

**Status:** Partially resolved (Categories A, B, C)
- ✅ T-Persist-1(b), T-Persist-1(e): Category A
- ⚠️ T-Persist-K-Unified: Category B (conditional)
- ❌ T-Persist-Full composition: Category C (very conditional)

---

## IV. Extension Research (04-10 onward)

### IV.A Branch Selection (R1)

**Q-0120:** Which branch does the system follow at bifurcation?

**Experiments:** exp66–exp73 (lambda_rep sweep, continuation, catalog)  
**New concepts:** Branch-conditioned vocabulary, overlap metrics  
**Status:** Active research; orthogonal to F-1/M-1/MO-1

**Note:** Branch selection doesn't resolve F-1/M-1; it's a *different* problem.

---

### IV.B Relaxed Merge Dynamics

**Q-0121:** How slowly do K=2 formations merge?

**Methods:**
- Barrier estimation (exp67–exp69: NEB-lite)
- Kramers rate theory (exp54–exp59)
- Core dissolution analysis

**Status:** Active research; conditional on resolving F-1

---

### IV.C Kinetic Multi-Formation Theory

**Q-0122:** Are K>1 formations kinetic or thermodynamic?

**Finding:** K>1 is **kinetic** (barrier-stabilized), not thermodynamic  
**Implication:** Resolves some paradox of F-1 (K>1 stable as metastable local minima, not global)  
**Status:** Under investigation (exp54–exp59)

---

## V. Validation & Implementation

### V.A Experimental Validation

**Q-0130:** Do theoretical predictions match empirical data?

**Validation suite:**
- exp1–exp35: Single-formation theory ✅
- exp40–exp50: Multi-formation basic ⚠️
- exp54–exp79: Branch selection & kinetic dynamics 🔄

**Status:** Single-formation well validated; K-field conditional on F-1/M-1

---

### V.B Software Implementation

**Q-0131:** Is theory implementable as executable code?

**Answer:** Yes
- scc/ package: 174 passing tests
- Core pipeline: field → operators → energy → optimizer → diagnostics
- All Category A theorems verified to FD 1e-9

**Status:** ✅ Complete

---

### V.C Publication & Communication

**Q-0140:** Can theory be clearly communicated in papers?

**Output:** 2 LaTeX papers (IEEEtran format)
- paper1_math.tex (11 pages): Mathematical formalism
- paper2_cogsci.tex (14 pages): Cognitive science interpretation

**Status:** Drafts complete; publication pending F-1/M-1 resolution

---

## VI. Meta-Problems (Research Governance)

### VI.A Specification Management

**Q-0150:** How do we manage spec versions and assumptions?

**Solution:** Research OS with immutable registries
- concept_registry.md (D-xxxx)
- symbol_registry.md (S-xxxx)
- assumption_registry.md (A-xxxx)
- theorem_registry.md (T-xxxx)

**Status:** ✅ Implemented (Phase 1)

---

### VI.B Problem Tracking

**Q-0151:** How do we prevent critical issues from being hidden?

**Solution:** Explicit documentation in release notes
- v1.2: F-1, M-1, MO-1 prominent
- Type A/B classification retracted
- All assumptions listed with scope

**Status:** ✅ Implemented (Phase 2)

---

## Problem Summary (Status Snapshot)

| Category | Count | Status | Notes |
|----------|-------|--------|-------|
| **Resolved ✅** | 25+ | Complete | Axioms, single-formation theory, diagnostics |
| **Active Research 🔄** | 10+ | Ongoing | Branch selection, kinetics, implementation |
| **Critical Unresolved 🔴** | 3 | BLOCKING | F-1, M-1, MO-1 (K-field foundation) |
| **High Open 🟠** | 5+ | Important | MO-1 variants, persistence composition |
| **Low Open 🟢** | 10+ | Specialty | Special cases, extensions |

---

## Hierarchical Dependency (Simplified)

```
Primitives (Q-0001:Q-0003)
    ↓
Axioms (Q-0010:Q-0012) ✅
    ↓
Single-Formation (Q-0020:Q-0042) ✅
    ├→ Existence, Stability, Dynamics
    ├→ Phase Transition
    └→ Diagnostics
    ↓
Multi-Formation K-Field (Q-0050:Q-0102)
    ├→ Architecture (Q-0050)
    ├→ Global Stability (Q-0051) ⚠️ Depends on F-1/M-1
    ├→ **CRITICAL PROBLEMS** (F-1, M-1, MO-1) 🔴
    └→ Persistence (Q-0110)
    ↓
Extensions (Q-0120:Q-0122)
    ├→ Branch Selection (orthogonal to F-1/M-1)
    ├→ Merge Dynamics (conditional on F-1/M-1)
    └→ Kinetic Theory (under investigation)
```

---

## Milestone Mapping

| Milestone | Status | Achieved | Blocked By |
|-----------|--------|----------|-----------|
| **M1: Foundations** | ✅ Complete | v1.0 | None |
| **M2: Formalism** | ✅ Complete | v1.1 (PLAN_0403) | None |
| **M3: Validation** | ⚠️ Partial | v1.2 single-formation ✅; K-field ⚠️ | F-1, M-1 |
| **M4: Publication** | 🔴 Blocked | Papers drafted | F-1/M-1 resolution needed |
| **M5: Application** | 🔴 Blocked | Code complete | Theory completion (F-1/M-1) |

---

## Navigation Guide

**For understanding what's been proved:**
- See: Canonical Spec v1.2, §13 (Proved Results Registry)
- Or: theorem_registry.md (00_meta/03_context_memory/)

**For critical open problems:**
- See: open_problems.md (same folder)
- Or: Canonical Spec v1.2, §14.1 (Critical Open Problems)

**For dependencies:**
- See: dependency_graph.md (next section)

**For research priorities:**
- See: milestones/ folder (M1–M5 status)

---

**Last updated:** 2026-04-12  
**Scope:** All research questions from Iterations 1–12 + 04-10/04-12 extensions  
**Total questions:** 50+ organized hierarchically  
**Critical blockers:** 3 (F-1, M-1, MO-1)

---

See also: **dependency_graph.md**, **open_problems.md**, **milestones/** (this folder)
