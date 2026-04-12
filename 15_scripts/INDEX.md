---
title: Automation Scripts
type: index
last_updated: 2026-04-12
total_scripts: 4
---

# Automation Scripts — 15_scripts/

Helper scripts for Research OS maintenance: building dependency graphs, validating structure, finding unregistered items, and promoting results to canonical specifications.

## Purpose

Provide automated tools to:
1. **Validate** the Research OS structure (no orphaned files, consistent metadata)
2. **Build** dependency graphs (which theorems use which axioms)
3. **Find gaps** (questions without answers, unregistered symbols)
4. **Promote** experimental results into canonical specifications

## Script Inventory

### 1. build_dependency_graph.py

**Purpose:** Generate complete dependency graph: axioms → theorems → experiments

**Usage:**
```bash
cd /Perception_theory/15_scripts
python3 build_dependency_graph.py
```

**Output:** `02_roadmap/dependency_graph.md` (updated)

**What it does:**
- Reads all T-xxxx definitions from `01_canonical/`
- Extracts axiom dependencies (A-xxxx used in each proof)
- Extracts experiment links (which exp validates which theorem)
- Generates visualization of critical paths
- Identifies missing pieces (unproven theorems, unvalidated claims)

**Example output:**
```
T-0001: K=1 Uniqueness (Canonical Spec §3.1)
├── Depends on: A-0001, A-0005, A-0012
├── Proved by: P-0001 (Canonical Spec §13, proof outline)
├── Validated by: exp1, exp2, exp5
├── Supports: T-0003, T-0008 (used in their proofs)
└── Status: ✅ Category A (fully proved)

OP-0001: F-1 K=2 Vacuity
├── Unresolved in v1.2
├── Resolution attempt: Option C (kinetic theory)
├── Blocked by: T-Kinetic-1, T-Kinetic-2, T-Kinetic-3 (not yet proved)
├── Validation: exp81, exp82, exp84 (in progress)
└── Expected resolution: 2026-05-24
```

### 2. validate_headers.py

**Purpose:** Check Research OS structure for consistency

**Usage:**
```bash
python3 validate_headers.py --check all
python3 validate_headers.py --fix metadata  # Auto-fix timestamps
```

**What it validates:**
- All .md files have required frontmatter (id, type, date, status)
- All IDs are unique (no duplicate T-0001, Q-xxxx collisions)
- All cross-references point to existing files
- All date fields are valid YYYY-MM-DD
- All status fields use approved values (draft, active, complete, etc.)

**Output:** 
```
✅ Validation passed: 267 files checked
⚠️ Warnings: 3 files missing status
❌ Errors: 1 duplicate ID found (D-0045 appears twice)
```

### 3. find_unregistered_symbols.py

**Purpose:** Discover and register untracked concepts

**Usage:**
```bash
python3 find_unregistered_symbols.py --scan all
python3 find_unregistered_symbols.py --extract D-symbols
```

**What it does:**
- Scans all docs/ for mathematical notation (uses regex)
- Checks against 03_context_memory/symbol_registry.md
- Flags unmapped symbols (concepts without D-xxxx ID)
- Suggests registration
- Finds implicit assumptions (text patterns like "assume", "suppose", "we require")

**Output:**
```
Found 12 unregistered symbols:

1. "u_t" → D-0001 (registered: soft cohesion field)
2. "Σ_m" → D-0007 (registered: volume-constrained manifold)
3. "ρ_ij" → UNREGISTERED (appears in exp_barrier_measurement.py, line 45)
   Suggest registration as: D-NEW-001 (reaction coordinate density)

Found 8 implicit assumptions:

1. docs/iteration_06_*.md:12 — "assume finite support"
   Should be: Explicit assumption A-0XXX
2. exp81_barrier_measurement.py:67 — "we require smooth landscape"
   Should be: Listed in exp81 design assumptions
```

### 4. promote_to_canonical.py

**Purpose:** Elevate experimental results and proofs to canonical specifications

**Usage:**
```bash
python3 promote_to_canonical.py --promote result_R-0082
python3 promote_to_canonical.py --validate theorem_T-Kinetic-1
python3 promote_to_canonical.py --draft version_2.0
```

**What it does:**
- Takes a result file (R-xxxx) and prepares canonical version
- Formats with proper theorem statement + proof structure
- Checks dependencies (is the result really ready?)
- Generates diff showing what's new in Canonical Spec v2.1
- Prepares CHANGELOG entry

**Example workflow (promote exp82 to canonical):**

```bash
# 1. exp82 completed successfully
# 2. Critic reviewed (exp82 validates T-Kinetic-2)
# 3. Ready to promote

python3 promote_to_canonical.py --promote result_R-0082
# Output:
#   1. Creates 01_canonical/T-Kinetic-2_theorem_statement.md
#   2. Copies proof from 07_proofs/T-Kinetic-2/
#   3. Links to exp82 in results registry
#   4. Generates CHANGELOG entry:
#      "2026-05-03: T-Kinetic-2 proved via kinetic framework, exp82 validates"

python3 promote_to_canonical.py --validate theorem_T-Kinetic-2
# Output:
#   1. Checks: Is proof complete? Yes.
#   2. Checks: Are dependencies met? A-0024 formalized? Yes.
#   3. Checks: Is exp82 validated? Yes.
#   4. Status: ✅ Ready for publication in v2.0

python3 promote_to_canonical.py --draft version_2.0
# Output:
#   1. Creates draft canonical_version_2.0.md
#   2. Includes: A-0023/0024/0025, T-Kinetic-1/2/3
#   3. Compiles from current state of registries
#   4. Shows diff vs. v1.2: +3 axioms, +3 theorems, resolved F-1/M-1
```

---

## Running the Scripts

### Daily Use

```bash
# After each experimental session, validate structure
python3 validate_headers.py --check all

# Before promoting result to canonical
python3 promote_to_canonical.py --validate theorem_[id]
```

### Weekly Use

```bash
# Update dependency graph (Friday)
python3 build_dependency_graph.py

# Find any unregistered concepts
python3 find_unregistered_symbols.py --scan all
```

### At Release Points

```bash
# Prepare v2.0 for publication (2026-05-24)
python3 promote_to_canonical.py --draft version_2.0

# Validate all theorems are registered
python3 validate_headers.py --check theorems
```

---

## Implementation Status

- [ ] **build_dependency_graph.py** — Template ready, needs implementation
- [ ] **validate_headers.py** — Template ready, needs implementation
- [ ] **find_unregistered_symbols.py** — Template ready, needs implementation
- [ ] **promote_to_canonical.py** — Template ready, needs implementation

## Notes

These scripts are **helper tools**, not critical path blockers. They automate tedious validation and cross-reference work. Implementation can be phased:

1. **Phase 1:** Basic validation (check headers exist)
2. **Phase 2:** Dependency building (axiom→theorem links)
3. **Phase 3:** Symbol discovery (find unregistered concepts)
4. **Phase 4:** Promotion workflow (move results to canonical)

---

**Created:** 2026-04-12
**Scripts:** 4 (all templated)
**Status:** Ready for implementation as time permits
