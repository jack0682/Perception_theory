---
id: CV-latest
type: canonical/pointer
status: accepted
created: 2026-04-12
current_version: 1.2
---

# Canonical Specification — Current Version Pointer

**This file directs readers to the authoritative current specification.**

---

## Current Canonical Version

**Version:** 1.2  
**File:** `canonical_version_1.2.md`  
**Release Date:** 2026-04-12  
**Status:** Active, authoritative  

---

## What to Read

### For Quick Overview
1. Start with **canonical_version_1.2.md** — Main formal specification
2. Read **release_notes/v1.2_release_note.md** — What changed, what's new
3. Check **§14.1** (v1.2 spec) — Critical open problems (F-1, M-1, MO-1)

### For Implementation
- Sections §1–8 (Single-Formation Theory): Solid, Category A results
- Sections §9–11 (K-Field): Use with explicit understanding of fixed-K assumption
- Section §12 (Transport & Persistence): Provisional forms; confinement bounds verified

### For Theory Development
- Section §14 (Commitments & Open Problems)
- release_notes/v1.2_release_note.md (mitigations and future directions)
- Registries in 00_meta/03_context_memory/ (assumptions, concepts, theorems)

---

## Version History

| Version | Date | Status | Focus | Key Change |
|---------|------|--------|-------|-----------|
| **v1.0** | 2026-04-01 | Historical | Baseline | 12 Category A theorems |
| **v1.1** | 2026-04-03 | Historical | PLAN_0403 | 3 Category B→A upgrades |
| **v1.2** | 2026-04-12 | **Current** | Audit & Transparency | Explicit assumptions, F-1/M-1/MO-1 documented |

---

## Key Differences: v1.1 → v1.2

### Added
- Explicit "Fixed K" and "Fixed m_j" assumptions in every K-field theorem
- §14.1: Critical Open Problems (F-1, M-1, MO-1) with severity ratings
- Type A/B classification framework **retracted** (invalidated by exp65)
- Detailed assumption registry (§14.2)
- Mitigation strategies for unresolved issues (§14.3)

### Clarified
- Which theorems are self-contained (single-formation, Category A)
- Which theorems depend on external scaffolding (K-field, Category B/C)
- What empirical validation exists for each result
- What experiments are still needed to resolve open problems

### Retracted
- Type A/B classification (no Type B observed; unvalidated hypothesis)

---

## Critical Caveats (Must Read)

### F-1: "K=2 Vacuity Problem" 🔴 CRITICAL
- **Statement:** K=2 global stability requires per-formation mass held fixed *externally*
- **Issue:** If masses allowed to vary, energy always prefers K=1 (50% cheaper)
- **Impact:** All K-field theorems (T-Persist-K-Sep, etc.) depend on fixed-K assumption
- **Status:** Unresolved; no mechanism yet for why K would be fixed in nature
- **Mitigation:** Accept as external constraint OR develop K-selection theory (future work)

### M-1: "K=1 Energetic Preference" 🔴 CRITICAL
- **Statement:** The K=2 energy landscape (E as function of m_1) is monotonic decreasing toward K=1
- **Issue:** This is the root cause of F-1
- **Impact:** K>1 can never emerge naturally from energy minimization alone
- **Status:** Unresolved; requires model selection mechanism (BIC? free energy?)
- **Mitigation:** Acknowledge K>1 as metastable (kinetic barriers) OR introduce selection criterion

### MO-1: "Morse Theory Failure" 🟠 HIGH
- **Statement:** The K=2 constrained manifold Σ²_M has corners (non-smooth)
- **Issue:** Smooth Morse theory inapplicable; theorems relying on it may be invalid
- **Impact:** Full global analysis of K=2 energy landscape incomplete
- **Status:** Unresolved; potential fix is stratified Morse theory (complex)
- **Mitigation:** Use existing stable results; avoid claiming global optimality without proof

---

## Validation Status

### Category A Results (Single-Formation)
- ✅ T-1 to T-14: Fully proved, verified experimentally
- ✅ QM-1 to QM-4: Quantum analogy, empirically sound
- ✅ C-Axioms, Predicate-Energy Bridge, Deep Core Dominance 2b: Upgraded to A in v1.1
- **Confidence:** High; use in applications with confidence

### Category B Results (K-Field, Conditional)
- ✅ T-Persist-K-Unified: Parametric theorem, 100% validation (exp46–exp47)
- ⚠️ T-Persist-K-Sep: Conditional on well-separation (not always satisfied)
- ⚠️ T-Bind-Proj: Proved only for τ=1/2 (general τ is Category C)
- **Confidence:** Medium; use with explicit understanding of conditions

### Category C Results (Very Conditional)
- ⚠️ T-Persist-K-Weak: Only in weakly-interacting regime (narrow parameter range)
- ⚠️ T-Bind-Full: General τ dependence incomplete
- **Confidence:** Low; specialty results only

---

## For Citation

**Recommended citation:**
```
Soft Cognitive Cohesion Canonical Specification, Version 1.2.
Released 2026-04-12.
Available at: Perception/Perception_theory/01_canonical/canonical_version_1.2.md
```

**For specific theorem:**
```
Theorem T-Persist-K-Unified (Category B, conditional).
See: Canonical Spec v1.2, §12, T-Persist-K-Unified.
Proof: 07_proofs/P-0502_...
Validation: E-0046, E-0047 (100% geometric-Lambda agreement, 69 configs).
Assumptions: Fixed K, fixed per-formation mass, well-separated or weakly-interacting regime.
```

---

## Next Steps

### Immediate (Phase 2 Complete)
- ✅ Canonical Spec v1.2 released with explicit assumptions
- ✅ Release notes for v1.0, v1.1, v1.2 written
- ✅ F-1, M-1, MO-1 documented with mitigation strategies

### Near-Term (Phase 3–4)
- [ ] Create 02_roadmap/ with dependency graph and open problems (Phase 3)
- [ ] Initialize 04_daily_log/ for operational tracking (Phase 4)
- [ ] Create 05_questions/, 06_claims/, 07_proofs/ folders with ID mapping (Phase 6)

### Future (Requires F-1/M-1/MO-1 Resolution)
- [ ] Resolve F-1: K-selection mechanism or accept external constraint
- [ ] Resolve M-1: Energy comparison theory or free energy framework
- [ ] Resolve MO-1: Stratified Morse theory or alternative analysis
- [ ] Release Canonical Spec v2.0 (if all three resolved)

---

## Contact & Questions

For questions about:
- **Specification details:** See canonical_version_1.2.md and cited sections
- **Version history:** See release_notes/ folder
- **Open problems:** See §14 (v1.2 spec) or assumption_registry.md
- **Implementation:** See scc/ package (Python) with 174 passing tests

---

**Last updated:** 2026-04-12  
**Maintained by:** Theory Lead  
**Authority:** Official specification for all SCC-related work
