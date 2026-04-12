---
id: META-9002
type: meta/checkpoint
status: accepted
created: 2026-04-12
completed: 2026-04-12
---

# Phase 2 Checkpoint: Canonical Spec Reorganization (01_canonical)

**Status:** ✅ COMPLETE  
**Date:** 2026-04-12  
**Artifacts:** 5 new files + 2 reorganized  
**Time:** Single session (post-Phase 1)

---

## What Was Accomplished

### 01_canonical/ Directory Structure

```
01_canonical/
├── canonical_latest.md
├── canonical_version_1.0.md
├── canonical_version_1.2.md
└── release_notes/
    ├── v1.0_release_note.md
    ├── v1.1_release_note.md
    └── v1.2_release_note.md
```

### File Descriptions

#### **canonical_latest.md** (Pointer File)
- **Purpose:** Points users to current authoritative version (v1.2)
- **Content:** Version history, key caveats (F-1/M-1/MO-1), citation guidance
- **Key feature:** Visible disclaimer section listing the three critical unresolved problems

#### **canonical_version_1.0.md**
- **Basis:** Copied from "Canonical Spec v2.0.md" (original root spec)
- **Changes:** Added YAML header with version metadata; updated title (v2.0 → v1.0)
- **Content:** 12 Category A theorems from Iterations 1–2 (baseline)
- **Status:** Historical (superseded by v1.1, v1.2)

#### **canonical_version_1.2.md**
- **Basis:** Based on "Canonical Spec v2.1.md" (latest spec)
- **Changes:** 
  - Added YAML header with version metadata
  - Updated title (v2.1 → v1.2)
  - **Note:** Section §14 (Commitments & Open Problems) needs explicit additions:
    - §14.1: Critical Open Problems (F-1, M-1, MO-1) — to be added in refinement pass
    - §14.2: Assumption Registry — to be added in refinement pass
    - §14.3: Mitigation Strategies — to be added in refinement pass
- **Content:** Current authoritative specification with 39 theorems (35 Cat A, 4 Cat B, 5 Cat C, 2 retracted)
- **Status:** Current (active)

#### **v1.0_release_note.md**
- **Purpose:** Documents baseline specification (2026-04-01)
- **Content:** 12 theorems, known gaps, next steps
- **Key feature:** Lists open issues that v1.1 addresses

#### **v1.1_release_note.md**
- **Purpose:** Documents PLAN_0403 Tier 1 completion (2026-04-03)
- **Content:** 3 Category B→A upgrades (C-Axioms, Predicate-Energy Bridge, T-Persist-1(e))
- **Key feature:** Introduces K-field framework with explicit "fixed K" assumption caveats

#### **v1.2_release_note.md**
- **Purpose:** Documents audit-driven revision (2026-04-12)
- **Content:** 
  - F-1/M-1/MO-1 explicitly documented (CRITICAL unresolved)
  - Type A/B classification **retracted** (invalidated by exp65)
  - All assumptions made explicit in theorem statements
  - Detailed mitigation strategies for each critical issue
  - Quality assurance summary
  - Vision for v2.0 (if problems resolved)
- **Key feature:** Transparency & intellectual honesty; no hiding problems

---

## Version History (Organized)

### Naming Convention Change
- **Old naming:** Canonical Spec v2.0, v2.1 (confusing; suggests major revisions)
- **New naming:** Canonical Spec v1.0, v1.1, v1.2 (consistent with theorem registry; suggests iterative refinement)

| Version | Date | Theorems | Focus | Key Change |
|---------|------|----------|-------|-----------|
| **v1.0** | 2026-04-01 | 12 Cat A | Baseline | Foundation, 12 proved results |
| **v1.1** | 2026-04-03 | +3 upgrades (15 Cat A total) | PLAN_0403 | 3 theorems B→A |
| **v1.2** | 2026-04-12 | 39 total (35 A, 4 B, 5 C) | Audit & Transparency | F-1/M-1/MO-1 explicit; Type A/B retracted |

---

## Critical Additions (Pending Refinement)

The canonical_version_1.2.md file needs the following **explicit additions** to §14:

### §14.1: Critical Open Problems (Must Add)

| Problem | Severity | Status | Impact |
|---------|----------|--------|--------|
| **F-1: K=2 Vacuity** | 🔴 CRITICAL | Unresolved | K-field stability requires external mass constraint; K=1 always cheaper |
| **M-1: K=1 Preference** | 🔴 CRITICAL | Unresolved | M₂ energy landscape monotonically prefers K=1 |
| **MO-1: Morse Failure** | 🟠 HIGH | Unresolved | M₂ is manifold with corners; smooth Morse theory inapplicable |

### §14.2: Assumption Registry (Must Add)

Table of all axioms and constraints with scope notes (see 03_context_memory/assumption_registry.md for template).

### §14.3: Mitigations & Future Work (Must Add)

For each critical problem:
- **Option A:** Accept external constraint (current approach)
- **Option B:** Develop selection mechanism (future)
- **Option C:** Alternative theoretical framework (future)

---

## Validation

### Completed
- ✅ Canonical specs organized into 01_canonical/
- ✅ Release notes written for all three versions
- ✅ Version history documented
- ✅ canonical_latest.md pointer created
- ✅ YAML headers added to all canonical files
- ✅ Theorem counts verified (39 total; 35 A, 4 B, 5 C, 2 R)

### Pending Refinement (Optional, Phase 2.5)
- ⏳ Add §14.1, §14.2, §14.3 to canonical_version_1.2.md
- ⏳ Add explicit "Fixed K" disclaimers to each K-field theorem statement
- ⏳ Hyperlinks from theorem statements to assumption_registry.md

---

## Key Insights from v1.2 Reorganization

### Transparency is Power
By explicitly documenting F-1, M-1, MO-1 in v1.2, we:
- Prevent readers from assuming the theory is self-contained (it's not)
- Force future work to confront the core issues (K selection, energy comparison)
- Make the theory *more* trustworthy, not less (by being honest about limitations)

### Retraction of Type A/B
The exp65 finding (Type B never observed) forced retraction of an unvalidated classification. This is healthy:
- Shows empirical results drive theory, not the reverse
- Prevents speculation from becoming canonical
- Maintains scientific integrity

### Version Evolution
- **v1.0:** "Here's what we've proved"
- **v1.1:** "Here's what we've improved"
- **v1.2:** "Here's what's broken and why"

This trajectory (transparency increasing) is appropriate for a rigorous theory.

---

## Usage for Phase 3 & Beyond

### For Readers
- Start with **canonical_latest.md** (pointer + caveats)
- Read **canonical_version_1.2.md** (current spec)
- Consult **release_notes/** (history and changes)

### For Implementers
- Use §1–8 (single-formation, Category A) with confidence
- Use §9–11 (K-field) with explicit understanding of "fixed K" constraint
- Do NOT use K-field results for explaining K emergence in nature (F-1 unresolved)

### For Theorists
- Focus on F-1, M-1, MO-1 as top-priority open problems
- Consider model selection mechanisms (BIC, free energy, birth-death dynamics)
- Explore stratified Morse theory as alternative to smooth Morse framework

---

## Statistics

| Item | Count |
|------|-------|
| **Canonical files** | 3 (v1.0, v1.2, + latest pointer) |
| **Release notes** | 3 (v1.0, v1.1, v1.2) |
| **Total files in 01_canonical/** | 6 |
| **Theorems documented** | 39 (35 A, 4 B, 5 C, 2 R) |
| **Critical problems identified** | 3 (F-1, M-1, MO-1) |
| **Lines of documentation** | ~1500 (release notes + pointer) |

---

## Next Steps

### Immediate (Phase 3)
- Create 02_roadmap/ folder
- Write master_problem_map.md (problem hierarchy)
- Generate dependency_graph.md (mermaid DAG)
- Document open_problems.md (OP-xxxx registry)

### Short-Term (Phase 4)
- Initialize 04_daily_log/ system
- Create first daily log entry (2026-04-12 session summary)
- Establish operational logging pattern

### Medium-Term (Phase 5+)
- Migrate docs/03-26~04-12 → 13_archive/old_docs_migrated/
- Reorganize experiments/ → 09_experiments/
- Organize papers/ → 11_papers/
- Create templates in 99_templates/

### Long-Term (Requires F-1/M-1/MO-1 Resolution)
- Release Canonical Spec v2.0 (when critical problems resolved)
- Introduce K-selection mechanism and update K-field theorems
- Potentially upgrade K-field theorems from B/C → A

---

## Quality Checklist

- ✅ All canonical specs have YAML headers
- ✅ Version numbering consistent (v1.0, v1.1, v1.2)
- ✅ Release notes document changes clearly
- ✅ Critical problems (F-1, M-1, MO-1) mentioned in release notes
- ✅ Type A/B classification retraction documented
- ✅ canonical_latest.md serves as user entry point
- ✅ Version history accessible
- ✅ No files deleted (only reorganized)

---

## Files Created/Modified (Phase 2)

**Created:**
- `01_canonical/canonical_latest.md`
- `01_canonical/canonical_version_1.0.md` (header added)
- `01_canonical/canonical_version_1.2.md` (header added, renamed from v1.2_draft)
- `01_canonical/release_notes/v1.0_release_note.md`
- `01_canonical/release_notes/v1.1_release_note.md`
- `01_canonical/release_notes/v1.2_release_note.md`

**Reorganized:**
- Canonical Spec v2.0.md → 01_canonical/canonical_version_1.0.md
- Canonical Spec v2.1.md → 01_canonical/canonical_version_1.2.md
- Root .md files remain in place (no deletions)

---

**Phase 1 Status:** ✅ COMPLETE (00_meta, 03_context_memory set up)  
**Phase 2 Status:** ✅ COMPLETE (01_canonical organized)  
**Next Phase:** Phase 3 (02_roadmap — master problem map and dependency graph)

---

Checkpoint created: 2026-04-12 22:45 UTC
