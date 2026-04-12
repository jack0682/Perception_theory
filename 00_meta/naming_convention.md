---
id: META-0003
type: meta/naming
status: accepted
last_updated: 2026-04-12
---

# Naming Conventions & ID Schema

## Directory Structure Rules

### Numeric Prefixes (Hierarchical Priority)

```
00_meta/           Constitutive rules, ontology, agent protocols
01_canonical/      Canonical specification versions & release notes
02_roadmap/        Master problem map, dependency graph, open problems
03_context_memory/ Registries (concept, symbol, theorem, assumption)
04_daily_log/      Research operations log (date-organized)
05_questions/      Q-xxxx problem definitions
06_claims/         C-xxxx assertions & conjectures
07_proofs/         P-xxxx proof attempts & verification
08_counterexamples/X-xxxx counterexamples & failure records
09_experiments/    E-xxxx computational & empirical validation
10_results/        R-xxxx result interpretation & analysis
11_papers/         Publication drafts, sections, figures
12_discussions/    DISC-xxxx conceptual debates & philosophy
13_archive/        Deprecated, migrated, or abandoned work
14_figures/        Diagrams, visual proofs, concept maps
15_scripts/        Automation tools for registry, validation, promotion
99_templates/      Document templates for each artifact type
```

**Principle:** Lower numbers = foundational, higher numbers = derivative.

---

## Document ID Schema

### Primary Categories

| Prefix | Type | Example | Location | Rationale |
|--------|------|---------|----------|-----------|
| **D-xxxx** | Concept/Definition | D-0001: Soft Cohesion Field | 03_context_memory/ | Primitive terms |
| **S-xxxx** | Symbol | S-0001: u_t | 03_context_memory/ | Notation (avoid collisions) |
| **Q-xxxx** | Question/Problem | Q-0001: K-field stability? | 05_questions/ | Research initiation |
| **C-xxxx** | Claim/Conjecture | C-0001: T1 existence | 06_claims/ | Formal assertions |
| **P-xxxx** | Proof | P-0001_main_theorem/ | 07_proofs/ | Verification attempts |
| **X-xxxx** | Counterexample | X-0001: K=1 cheaper | 08_counterexamples/ | Refutation data |
| **E-xxxx** | Experiment | E-0001: Lambda sweep | 09_experiments/ | Empirical tests |
| **R-xxxx** | Result | R-0001: Support for C-0001 | 10_results/ | Interpretation |
| **DISC-xxxx** | Discussion | DISC-0001: Boundary ontology | 12_discussions/ | Conceptual debate |
| **A-xxxx** | Assumption | A-0001: Fixed K | 03_context_memory/ | Context constraints |
| **OP-xxxx** | Open Problem | OP-0001: F-1 (K=2 vacuous) | 02_roadmap/ | Unresolved issues |
| **CV-x.y** | Canonical Version | CV-1.2 | 01_canonical/ | Formal spec snapshot |

### Meta Categories

| Prefix | Type | Example | Location |
|--------|------|---------|----------|
| **META-xxxx** | Meta-operational | META-0001: Project Manifest | 00_meta/ |
| **AG-xxxx** | Agent Protocol | AG-0001: Proof Agent | 00_meta/agent_protocols/ |

### ID Format Rules

1. **Numeric Padding:** Four digits, zero-padded
   - ✅ Correct: `Q-0001`, `D-0042`
   - ❌ Wrong: `Q-1`, `D-42`

2. **No Spaces in File Names:** Use hyphens only
   - ✅ Correct: `D-0001_soft_cohesion_field.md`
   - ❌ Wrong: `D-0001 soft cohesion field.md`

3. **Folder Names for Multi-File Artifacts:**
   - Proof: `07_proofs/P-0001_main_theorem/` (folder) containing:
     - `overview.md`
     - `proof_attempt_v1.md`
     - `proof_attempt_v2.md`
     - `lemma_candidates.md`
     - etc.
   - Experiment: `09_experiments/E-0001_lambda_sweep/` (folder) containing:
     - `spec.md`
     - `run_001/` (results)
     - `summary.md`

4. **Cross-References:** Always cite with full ID
   - ✅ Correct: `See C-0001 for the claim.` or `[C-0001](../06_claims/C-0001_...md)`
   - ❌ Wrong: `See the main theorem.`

---

## YAML Header Format (All Documents)

Every document must begin with a YAML frontmatter block:

```yaml
---
id: Q-0001              # Unique identifier
type: question          # question, claim, proof, experiment, result, discussion, etc.
status: active          # seed, draft, active, tentative, challenged, validated, accepted, deprecated, archived
created: 2026-04-12
last_updated: 2026-04-12
author: Claude Code
depends_on: [D-0001, A-0001]  # IDs of concepts/assumptions this depends on
referenced_by: [C-0001, P-0001]  # IDs that cite this document
tags: [k-field, stability, energy]
severity: CRITICAL     # For problems/open issues: CRITICAL, HIGH, MEDIUM, LOW
---
```

### Status Vocabulary

- **seed:** Rough idea, not yet formalized
- **draft:** First pass, incomplete or unvetted
- **active:** Currently under investigation/development
- **tentative:** Proposed, awaiting validation
- **challenged:** Critique received; integrity questioned
- **validated:** Experimental evidence supports this
- **accepted:** Canonical (or nearly so); production-ready
- **deprecated:** Superseded; kept for reference
- **archived:** Historical; no longer active research path

---

## Dependency Tracking

### depends_on (What this requires)

List IDs of documents that must exist for this one to be valid:

```yaml
depends_on: 
  - D-0001  # Soft Cohesion Field definition
  - A-0001  # Fixed K assumption
  - C-0001  # Main theorem claim
```

### referenced_by (What cites this)

Maintained by automation; shows which documents depend on this one:

```yaml
referenced_by:
  - C-0002  # Another claim using this
  - P-0003  # A proof building on this
```

### Conflict-related fields (For open problems)

```yaml
conflicts_with: [OP-0002]  # Other open problems that may be related
supersedes: [OP-0001]      # Older problem definitions this replaces
```

---

## File Naming Conventions

### Root Directory (.md files)

Root-level files are **transitional** during Phase 2. Final locations:

| Current | Final Location | New Name |
|---------|---|---|
| `CLAUDE.md` | `00_meta/CLAUDE.md` | (no change) |
| `CONVENTIONS.md` | `00_meta/CONVENTIONS.md` | (no change) |
| `Canonical Spec v2.1.md` | `01_canonical/canonical_version_1.2.md` | (rename + update) |
| `THEORY_STATUS_2026-04-12.md` | `02_roadmap/theory_status_2026-04-12.md` | (move) |
| `Agent Instructions.md` | `00_meta/agent_instructions.md` | (move, lowercase) |
| `AGENTS.md` | `00_meta/agents.md` | (move, lowercase) |
| `README.md` | `00_meta/README.md` | (move) |
| `CHANGELOG.md` | `00_meta/CHANGELOG.md` | (move) |
| `RESEARCH_OVERVIEW.md` | `02_roadmap/research_overview.md` | (move) |
| `EXP-VERIFICATION-RESULTS.md` | `10_results/verification_summary.md` | (move + rename) |

### Date-Based Files (docs/)

Old structure: `docs/2026-04-07/audit/SOME-LONG-FILE.md`  
New structure: `04_daily_log/2026-04-07.md` (single daily log with sections)

### Implementation Directories (No Changes)

- `scc/` — Keep as-is
- `tests/` — Keep as-is
- Keep their internal structure unchanged

---

## Capitalization Rules

- **Directory names:** lowercase with underscores
  - ✅ `00_meta`, `01_canonical`, `03_context_memory`
  - ❌ `00_Meta`, `01-Canonical`

- **File names in folders:** lowercase with underscores
  - ✅ `concept_registry.md`, `proof_attempt_v1.md`
  - ❌ `ConceptRegistry.md`, `ProofAttemptV1.md`

- **ID prefixes:** UPPERCASE
  - ✅ `D-0001`, `Q-0042`, `C-0001`
  - ❌ `d-0001`, `q-0042`

---

## Special Naming Cases

### Multiple Proof Attempts

```
P-0001_main_theorem/
├── proof_attempt_v1.md (first pass)
├── proof_attempt_v2.md (revised)
├── proof_attempt_v3.md (complete rewrite)
└── failure_analysis.md (why v1, v2 failed)
```

Internally reference as:
- `P-0001` (the proof folder)
- `P-0001_v1`, `P-0001_v2` (in metadata comments if needed)

### Experiment Runs

```
E-0001_lambda_sweep/
├── spec.md (experiment definition)
├── run_001/ (params: λ=0.1, grid=10x10)
│   ├── config.json
│   ├── results.json
│   └── analysis.md
├── run_002/ (params: λ=0.5, grid=10x10)
└── summary.md (aggregate analysis)
```

### Revisions to Canonical

When Canonical Spec changes:

```
01_canonical/
├── canonical_version_1.0.md (original)
├── canonical_version_1.1.md (03-04 update)
├── canonical_version_1.2.md (04-12 with explicit assumptions)
├── canonical_latest.md (symlink or pointer: "current is v1.2")
└── release_notes/
    ├── v1.0_release_note.md
    ├── v1.1_release_note.md
    └── v1.2_release_note.md
```

---

## Registry Consistency

All registries live in `03_context_memory/`:

1. **concept_registry.md** — D-xxxx definitions
2. **symbol_registry.md** — S-xxxx notation
3. **theorem_registry.md** — C-xxxx (claims) & P-xxxx (proofs)
4. **assumption_registry.md** — A-xxxx constraints
5. **glossary.md** — Plain-language definitions (links to registries)

**Rule:** Every ID used in documents must appear in exactly one registry.

---

## Automation & Validation

Scripts in `15_scripts/` enforce:

- `validate_headers.py` — Check all .md files have proper YAML frontmatter
- `build_dependency_graph.py` — Extract depends_on/referenced_by, generate mermaid DAG
- `find_unregistered_symbols.py` — Scan for IDs not in registries
- `promote_to_canonical.py` — Check promotion criteria before accepting claim

All scripts read YAML headers and registry files.

---

**Last updated:** 2026-04-12  
**Owner:** Research OS Architect  
**Next Review:** After Phase 2 completion
