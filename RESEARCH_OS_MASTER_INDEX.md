---
id: RESEARCH-OS-INDEX
type: meta/master_index
status: active
created: 2026-04-12
last_updated: 2026-04-12
---

# Research OS: Master Index

**Purpose:** Central navigation hub for the entire Research OS refactoring (Phases 1–5)

**Date:** 2026-04-12  
**Status:** ✅ All Phases 1–5 Complete  
**Next:** Phase 4/5 operational execution (2026-04-13+)

---

## Quick Navigation

### By Role
- **Lead:** Start at 00_meta/agent_protocols/agent_system.md → milestones/ (current status)
- **Proof:** Start at 03_context_memory/theorem_registry.md → 02_roadmap/open_problems.md
- **Critic:** Start at 00_meta/ (assumptions) → 03_context_memory/assumption_registry.md
- **Experiment:** Start at 02_roadmap/open_problems.md → experiments/ (data)
- **Archivist:** Start at 13_archive/README.md → archival_policy.md

### By Question
- **"What's the theory status?"** → 01_canonical/canonical_latest.md
- **"What's broken?"** → 02_roadmap/open_problems.md (OP-0001, OP-0002, OP-0003)
- **"What's the roadmap?"** → 02_roadmap/master_problem_map.md
- **"Where are assumptions?"** → 03_context_memory/assumption_registry.md
- **"How do I log my work?"** → 02_roadmap/04_daily_log/operational_logging_guide.md
- **"Where's the archive?"** → 13_archive/README.md

---

## Hierarchical Structure: 6 Layers

```
Layer 0: Project Root
├── RESEARCH_OS_MASTER_INDEX.md (this file)
├── CLAUDE.md (project instructions)
└── CONVENTIONS.md (naming, style conventions)

Layer 1: Constitutional Foundation (00_meta/)
├── project_manifest.md (project overview, mission, critical problems)
├── ontology.md (4-layer conceptual hierarchy)
├── naming_convention.md (ID schema: D-xxxx, S-xxxx, T-xxxx, A-xxxx, etc.)
├── status_codes.md (document lifecycle: seed → draft → active ⇄ tentative → ...)
├── promotion_rules.md (how to upgrade claims to canonical theorems)
├── CLAUDE.md (copied from root, project guidelines)
├── CONVENTIONS.md (copied from root, naming conventions)
└── agent_protocols/
    ├── agent_system.md (5 roles: Lead, Proof, Critic, Experiment, Archivist)
    └── [decision protocols, escalation paths]

Layer 1b: Immutable Registries (03_context_memory/)
├── concept_registry.md (D-0001 through D-0025; 29 concepts registered)
├── symbol_registry.md (S-0001 through S-0046; 46 symbols)
├── theorem_registry.md (C-xxxx claims, P-xxxx proofs, T-xxxx theorems; 39 total)
├── assumption_registry.md (A-0001 through A-0035; 35 assumptions, F-1/M-1/MO-1 explicit)
├── glossary.md (plain-English definitions)
└── notation_decisions.md (rationale for all symbol choices)

Layer 2: Canonical Specifications (01_canonical/)
├── canonical_latest.md (pointer to current version)
├── canonical_version_1.0.md (baseline, 2026-04-01, 12 theorems)
├── canonical_version_1.1.md (PLAN_0403, 2026-04-03, 15 theorems)
├── canonical_version_1.2.md (audit-driven, 2026-04-12, 39 theorems with caveats)
├── release_notes/
│   ├── v1.0_release_note.md
│   ├── v1.1_release_note.md
│   └── v1.2_release_note.md
└── [future: canonical_version_2.0.md if Option B/C chosen]

Layer 3: Master Problem Map (02_roadmap/)
├── master_problem_map.md (50+ research questions organized hierarchically)
├── dependency_graph.md (Mermaid DAG, critical blocking chains, 3 options A/B/C)
├── open_problems.md (OP-0001 through OP-0022; 15+ problems by severity)
├── PHASE_4_COMPLETION_SUMMARY.md (Phase 4 overview)
├── PHASE_5_COMPLETION_SUMMARY.md (Phase 5 overview)
├── milestones/
│   ├── M1_foundations.md (✅ completed 2026-04-01)
│   ├── M2_formalism.md (✅ completed 2026-04-03)
│   ├── M3_validation.md (✅ completed 2026-04-12, decision pending)
│   └── M4_publication.md (⏳ awaiting direction, 3 options)
└── 04_daily_log/
    ├── README.md (Phase 4 overview)
    ├── operational_logging_guide.md (detailed protocols, 5 agent roles)
    ├── daily_log_index.md (master index, blocker registry)
    ├── PHASE_4_SETUP_2026-04-12.md (setup & next steps)
    └── [2026-04-13+]: YYYY-MM-DD/ (daily session directories)

Layer 5: Archival & Migration (13_archive/)
├── README.md (archive overview, structure, timeline)
├── archival_policy.md (retention rules, 3-month timeline, purge policy)
├── archive_index.md (master pointer registry)
├── archive_index_docs.md (documentation index)
├── archive_index_logs.md (daily logs index)
├── old_docs_migrated/
│   └── docs_2026-03-26_to_2026-04-12/ [ready 2026-04-13]
├── old_logs_quarterly/
│   └── daily_logs_2026-Q2/ [ready 2026-07-13]
├── deprecated_versions/
│   ├── canonical_version_0.9.md
│   └── deprecated_theorems.md (Type A/B classification)
├── experiments_archive/
│   └── [ready 2026-10-12]
└── reference_pdfs/
    └── [ready post-M4 publication]

Layer 4: Experiments & Results (future reorganization)
├── 09_experiments/ [TO CREATE]
│   ├── README.md
│   ├── experiments_index.md (by exp_ID, category, theorem)
│   └── [experiments data organized by category]
└── 10_results/ [TO CREATE]
    ├── README.md
    ├── results_index.md (by date, category, relevance)
    └── [results organized by category]
```

---

## Complete File Inventory: 36+ Files Created

### Layer 1: Constitutional (00_meta/)
1. project_manifest.md
2. ontology.md
3. naming_convention.md
4. status_codes.md
5. promotion_rules.md
6. CLAUDE.md
7. CONVENTIONS.md
8. agent_protocols/agent_system.md

### Layer 1b: Registries (03_context_memory/)
9. concept_registry.md
10. symbol_registry.md
11. theorem_registry.md
12. assumption_registry.md
13. glossary.md
14. notation_decisions.md

### Layer 2: Canonical Specs (01_canonical/)
15. canonical_latest.md
16. canonical_version_1.0.md
17. canonical_version_1.1.md
18. canonical_version_1.2.md
19. release_notes/v1.0_release_note.md
20. release_notes/v1.1_release_note.md
21. release_notes/v1.2_release_note.md

### Layer 3: Roadmap (02_roadmap/)
22. master_problem_map.md
23. dependency_graph.md
24. open_problems.md
25. PHASE_4_COMPLETION_SUMMARY.md
26. PHASE_5_COMPLETION_SUMMARY.md
27. milestones/M1_foundations.md
28. milestones/M2_formalism.md
29. milestones/M3_validation.md
30. milestones/M4_publication.md
31. 04_daily_log/README.md
32. 04_daily_log/operational_logging_guide.md
33. 04_daily_log/daily_log_index.md
34. 04_daily_log/PHASE_4_SETUP_2026-04-12.md

### Layer 5: Archive (13_archive/)
35. README.md
36. archival_policy.md
37. archive_index.md
38. archive_index_docs.md
39. archive_index_logs.md

---

## Registered Knowledge Items: 169+

| Category | Count | Location |
|----------|-------|----------|
| **Concepts (D-xxxx)** | 29 | concept_registry.md |
| **Symbols (S-xxxx)** | 46 | symbol_registry.md |
| **Theorems (T-xxxx)** | 39 | theorem_registry.md |
| **Assumptions (A-xxxx)** | 35 | assumption_registry.md |
| **Open Problems (OP-xxxx)** | 15+ | open_problems.md |
| **Research Questions (Q-xxxx)** | 50+ | master_problem_map.md |
| **Total** | **169+** | All registries |

---

## Critical Decision Point: F-1/M-1/MO-1 Resolution

**Current Status:** Awaiting user input (decision needed by 2026-04-13)

**Three options fully documented:**

### Option A: Publish v1.2 as Conditional Theory
- **Timeline:** M4 now (~4 weeks to publication)
- **What:** Release v1.2 as-is, with explicit caveats on K-field theory
- **Details:** See milestones/M4_publication.md (Option A section)

### Option B: Develop K-Selection Mechanism ⭐ RECOMMENDED
- **Timeline:** 4–6 weeks theory development → v2.0 → M4 (6–8 weeks total)
- **What:** Introduce BIC/free energy criterion for K selection; prove K emerges naturally
- **Details:** See milestones/M4_publication.md (Option B section)

### Option C: Reformulate as Kinetic Theory
- **Timeline:** 4–6 weeks reformulation → v2.0 → M4 (6–8 weeks total)
- **What:** Shift from thermodynamic to kinetic framework; K>1 as metastable local minima
- **Details:** See milestones/M4_publication.md (Option C section)

**Decision Location:** milestones/M3_validation.md (lines 138–194)  
**Implementation Plans:** milestones/M4_publication.md (all 3 options detailed)

---

## Immediate Execution Timeline

### 2026-04-13 (Phase 4 & 5 Start)

**Phase 4: Operational Logging Begins**
- Create 04_daily_log/2026-04-13/ directory
- All roles (Lead, Proof, Critic, Experiment, Archivist) begin session_log_[ROLE].md logging
- Daily consolidation: decisions_YYYY-MM-DD.md, blockers_YYYY-MM-DD.md
- Archivist updates registries from daily findings

**Phase 5: Archival Execution Begins**
- Migrate Q1 docs (2026-03-26 to 2026-04-12) → 13_archive/old_docs_migrated/
- Create migration_index_2026-04-12.md with full inventory
- Update archive_index.md with migration summary

### Ongoing (Phases 4 & 5 Parallel)

**Daily:** Operational logging in 04_daily_log/YYYY-MM-DD/  
**Weekly:** Consolidation report (weekly_summary_report_[WW].md)  
**Quarterly:** Archival batch move (Q-end + 90 days buffer)

### Post-Decision (Dependent on Option A/B/C)

**Option A:** Proceed to M4 (publication), ~4 weeks  
**Option B/C:** Execute theory development (~4–6 weeks), then M4 (~4 weeks), total ~8 weeks

---

## How to Use This Index

### For Session Start (All Roles)

1. **Open this file** (RESEARCH_OS_MASTER_INDEX.md)
2. **Find your role** in "By Role" section
3. **Check current status** (milestones/M3_validation.md or current M?.md)
4. **Review blockers** (02_roadmap/open_problems.md, severity 🔴)
5. **Begin daily log** (04_daily_log/YYYY-MM-DD/session_log_[ROLE].md)

### For Theory Questions

1. **"What's the current spec?"** → 01_canonical/canonical_latest.md
2. **"What theorems exist?"** → 03_context_memory/theorem_registry.md
3. **"What's proven vs conditional?"** → 03_context_memory/theorem_registry.md (Category column)
4. **"What's the critical path?"** → 02_roadmap/dependency_graph.md (critical blocking chains)

### For Problem Hunting

1. **"What's unresolved?"** → 02_roadmap/open_problems.md (sort by severity)
2. **"What blocks publication?"** → open_problems.md (OP-0001, OP-0002, OP-0003 are CRITICAL)
3. **"What's high-priority research?"** → open_problems.md (🟠 HIGH section)
4. **"Where do I start?"** → master_problem_map.md (question hierarchy)

### For Archival Questions

1. **"What's archived?"** → 13_archive/archive_index.md
2. **"How do I retrieve something?"** → 13_archive/archive_index.md (retrieval examples)
3. **"What's the retention policy?"** → 13_archive/archival_policy.md

---

## Key Statistics

| Metric | Value |
|--------|-------|
| Total Files Created | 36+ |
| Registered Knowledge Items | 169+ |
| Constitutional Files (00_meta/) | 8 |
| Registry Files (03_context_memory/) | 6 |
| Canonical Versions | 3 (v1.0, v1.1, v1.2) |
| Theorems Registered | 39 (35 A, 4 B, 5 C, 2 retracted) |
| Concepts Registered | 29 (25 active, 4 pending) |
| Symbols Registered | 46 |
| Assumptions Registered | 35 |
| Open Problems Registered | 15+ |
| Research Questions Mapped | 50+ |
| Critical Blockers | 3 (F-1, M-1, MO-1) |
| Milestones Completed | 3 (M1, M2, M3) |
| Milestones Pending | 1 (M4, awaiting direction) |

---

## Constitution Summary

**Mission:** Transform scattered documentation into hierarchical, immutable, transparent Research OS

**Achieved:**
- ✅ Hidden assumptions now explicit (F-1, M-1, MO-1 documented with severity)
- ✅ Problem landscape mapped (50+ questions, 15+ open problems, critical path clear)
- ✅ Dependencies traceable (theorem → proof → axiom; critical blocking chains visible)
- ✅ Theory status honest (v1.2 acknowledges limitations and conditionality)
- ✅ Operational framework ready (5 agent roles, daily/weekly/monthly procedures)
- ✅ Archival strategy in place (3-month retention, quarterly consolidation, no data loss)

---

## Next Phase: Confirmation & Execution

**Before 2026-04-13:**
- User reviews M3_validation.md (decision context)
- User chooses Option A, B, or C
- User confirms direction

**On 2026-04-13:**
- Phase 4 operational logging begins
- Phase 5 archival execution begins
- Daily/weekly/quarterly cycles start

**Expected Outcome:**
- ✅ Theory remains transparent and honest
- ✅ Knowledge is protected (immutable registries, archival)
- ✅ Research can proceed confidently (clear roadmap, explicit problems)
- ✅ Future sessions benefit (documented assumptions, decision history)

---

## See Also

- **Project charter:** 00_meta/project_manifest.md
- **Decision context:** 02_roadmap/milestones/M3_validation.md
- **Implementation plans:** 02_roadmap/milestones/M4_publication.md
- **Current theory status:** 01_canonical/canonical_latest.md
- **All problems:** 02_roadmap/open_problems.md
- **All registries:** 03_context_memory/[all files]
- **Operational procedures:** 02_roadmap/04_daily_log/operational_logging_guide.md
- **Archival procedures:** 13_archive/archival_policy.md

---

**Last updated:** 2026-04-12  
**Status:** ✅ All layers complete, ready for Phase 4/5 execution  
**Maintained by:** Lead role (Phase 4+)
