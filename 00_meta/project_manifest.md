---
id: META-0001
type: meta/manifest
status: accepted
last_updated: 2026-04-12
---

# Project Manifest: Soft Cognitive Cohesion (SCC)

## Mission

Develop a rigorous mathematical theory of how coherent formations emerge *prior to discrete objecthood*—before the world is parsed into separately-identified things. The primitive entity is a soft cohesion field `u_t : X_t → [0,1]` over a relational support space.

## Philosophical Foundation

The theory rejects several common framings:
- **NOT** fuzzy segmentation (objects exist with fuzzy boundaries)
- **NOT** clustering (pre-assigned point clouds)
- **NOT** tracking (object IDs persist mysteriously)
- **Instead:** Formations emerge dynamically from relational structure and variational principles

The soft field `u_t` is ontologically primitive. Crisp objects (if they appear) are derivative.

## Current Status (2026-04-12)

### Proven Results
- **Category A:** 35 fully proved theorems
  - T1 (existence), T6a/T6b (closure fixed points), T-A2 (monotonicity), T8 (phase transition)
  - T20 (axiom consistency), T14 (gradient flow), T3/T6 (stability), T7 (metastability)
  - T11 (Γ-convergence), C-Axioms (4), QM1–4, Predicate-Energy Bridge
  - Deep Core Dominance 2b, plus auxiliary results
- **Category B:** 4 theorems with conditions
  - T-Bind-Proj/Full (proved for τ=1/2)
  - T-Persist-K-Sep (well-separated regime)
- **Category C:** 5 conditional theorems
  - T-Persist-1(b,d,e), T-Persist-Full, T-Persist-K-Weak
- **Retracted:** 2 results (K-Saddle Conjecture, r̄₀ general τ)

### Critical Open Problems (04-12 Audit)

| ID | Problem | Status | Impact |
|-----|---------|--------|--------|
| **F-1** | K=2 global stability is "vacuous" (K=1 always 50% cheaper energetically) | ⚠️ UNRESOLVED | **CRITICAL** |
| **M-1** | K=1 is ALWAYS preferred in M₂ energy landscape | ⚠️ UNRESOLVED | **CRITICAL** |
| **MO-1** | M₂ is manifold with corners → smooth Morse theory fails | ⚠️ UNRESOLVED | **CRITICAL** |
| **exp65-fail** | Type A/B classification doesn't empirically validate (Type B never observed) | ✅ DOCUMENTED | High |
| **spec-implicit** | Canonical Spec assumes "fixed K, fixed m" without stating it | ⚠️ NEEDS CLARIFICATION | High |

### 04-12 Decisions

1. **Honest audit conducted** — THEORY_STATUS_2026-04-12.md documents F-1/M-1/MO-1 as unresolved
2. **Research OS structure adopted** — Moving to state-machine-based knowledge organization
3. **Canonical Spec v1.2 proposed** — Will include explicit assumption documentation
4. **04-10 branch selection work** — Orthogonal to F-1/M-1/MO-1; can continue independently

## Core Concepts (Ontology)

See `ontology.md` for detailed definitions. Summary:

| Concept | Definition | Status |
|---------|-----------|--------|
| **Cohesion Field** | u_t : X_t → [0,1], primitive entity | Accepted |
| **Closure Operator** | Cl_t, axiom A3, stabilization tendency | Accepted |
| **Distinction Operator** | D_t, axiom D, boundary definition | Accepted |
| **Resolvent** | C_t, self-interaction measure | Accepted |
| **Transport** | M_{t→s}, temporal persistence kernel | Accepted |
| **Boundary** | New concept being developed (D-0004) | Tentative |

## Implementation Status

- **scc/ package:** 174 passing tests, full core pipeline
- **tests/:** Comprehensive unit test suite
- **experiments/:** 75+ experiments (exp1–exp79) with results
- **papers/:** 2 LaTeX drafts (IEEEtran format, 11+14 pages)
- **docs/:** 148+ development documents (04-03~04-12, organized by date)

## Authoritative Documents

1. **Canonical Spec v1.2** (01_canonical/) — Current formal specification
2. **Agent Instructions.md** — Binding operational protocol
3. **CONVENTIONS.md** — Naming, directory structure, logging
4. **ontology.md** (this folder) — Conceptual primitives

## Next Immediate Actions (Priority 1)

### For Theory Foundation
1. Decide on response to F-1 (K=2 vacuous):
   - Option A: Honest restatement ("K=2 requires external mass constraint")
   - Option B: Status quo (acknowledge but continue)
   - Option C: Fundamental reconstruction (introduce model selection mechanism)

2. Clarify Canonical Spec v1.2:
   - Explicit "fixed K, fixed m" assumption statements
   - Classification of which theorems require these constraints
   - F-1/M-1/MO-1 explicit disclaimer

3. Re-examine exp62/exp63 divergence:
   - Original hypothesis (Type A vs Type B) invalidated by exp65
   - Determine actual cause (manifold structure? optimizer path bias?)

### For Research OS Implementation
1. Complete Phase 1 (00_meta, 03_context_memory) ✓ (in progress)
2. Complete Phase 2 (01_canonical reorganization)
3. Establish registry infrastructure (concept, symbol, theorem, assumption)
4. Create daily_log system for operations tracking

## Team Roles (as of 2026-04-12)

- **Lead:** Orchestration, spec decisions, canonical promotions
- **Proof Agent:** Formal verification, theorem formalization
- **Critic Agent:** Audit, counterexample search, vulnerability analysis
- **Experiment Agent:** Design, execution, result analysis, validation
- **Archivist:** Documentation organization, registry maintenance, state tracking

## Development Timeline

| Iteration | Dates | Focus | Theorems | Score |
|-----------|-------|-------|----------|-------|
| I1 | 03-26 | Brainstorming | 0 | 6/10 |
| I2 | 03-27 | Deep math | 12 | 7/10 |
| I3 | 03-30 | Implementation | — | 7/10 |
| I4 | 03-31 | Extensions | 10 predictions | 7/10 |
| I5–I6 | 04-01~04-03 | Vulnerability audit → Spec v2.0 | 27 | 7.5/10 |
| I7–I8 | 04-04~04-06 | Temporal theory → scc/ package | 174 tests | 8.5/10 |
| I9 | 04-07 | Multi-formation architecture | K-field | 9/10 |
| I10 | 04-10 | Publication drafts | 2 papers | 9/10 |
| I11 | 04-11 | Transport implementation | T-Persist verified | 8.5/10 |
| I12 | 04-12 | **Audit → Research OS** | — | — |

## References

- **THEORY_STATUS_2026-04-12.md** — Comprehensive audit of theory foundation
- **AUDIT_REPORT_2026-04-12.md** (in memory/) — Detailed findings
- **Canonical Spec v1.2** (01_canonical/) — Current specification with assumptions explicit

---

**Last updated:** 2026-04-12 by Claude Code  
**Next review:** After F-1/M-1/MO-1 decisions made
