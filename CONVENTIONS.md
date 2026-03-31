# CONVENTIONS.md — File & Log Management Rules

**Every new Claude session MUST read this file before creating, modifying, or logging any file.**

---

## 1. Directory Structure

```
/home/jack/ex/
  CLAUDE.md              # Claude Code instructions (read-only unless updating)
  CONVENTIONS.md         # THIS FILE — file management rules
  Agent Instructions.md  # Binding protocol (read-only)
  Canonical Spec v2.0.md # Authoritative spec
  CHANGELOG.md           # Session-level change log (append-only)

  scc/                   # Python package — code only
  tests/                 # Test files only
  experiments/           # Experiment scripts only
  papers/                # LaTeX drafts and figures only
  paper_template/        # Template files (read-only)

  docs/                  # Research record — organized by date
    00-overview.md       # Master index (update when adding new iteration)
    YYYY-MM-DD/          # Date folder (e.g., 03-31/)
      INDEX.md           # Date-level index (required)
      <category>/        # Category subfolder
        <files>.md       # Actual documents
```

## 2. File Creation Rules

### 2.1 Research Documents (docs/)

**Always** place in `docs/YYYY-MM-DD/<category>/`.

| Category | When to use | Example filenames |
|----------|------------|-------------------|
| `proof/` | New theorem proofs, proof attempts | `CORE-DEPTH-PROOF.md`, `T-PERSIST-K-SEP.md` |
| `audit/` | Reviews, verification, gap analysis | `A7-transport-audit.md`, `RE-AUDIT-6.md` |
| `repair/` | Bug fixes, gap closures, corrections | `GAP-CLOSURES-4.md`, `BASIN-REPAIR.md` |
| `theory/` | New theoretical development, design decisions | `MULTI-TEMPORAL-THEORY.md`, `BIRTH-DEATH.md` |
| `experiment/` | Experiment analysis reports | `EXP16-ANALYSIS.md` |
| `synthesis/` | Session summaries, iteration capstones | `I14-SYNTHESIS.md` |
| `generalization/` | Extensions beyond core theory | `CONTINUUM.md`, `STOCHASTIC.md` |

**Procedure:**
1. Check if today's date folder exists: `docs/YYYY-MM-DD/`. Create if not.
2. Check if the category subfolder exists. Create if not.
3. Create the file with a header (see §4).
4. Update `docs/YYYY-MM-DD/INDEX.md` — add one row to the relevant table.
5. If starting a new iteration (I13, I14, ...), also update `docs/00-overview.md`.

### 2.2 Code Files (scc/, tests/, experiments/)

- **scc/**: Only create new modules if the theory pipeline genuinely needs it. Prefer extending existing modules.
- **tests/**: Mirror `scc/` structure. One test file per module (`test_<module>.py`).
- **experiments/**: Name as `exp<N>_<short_name>.py`. Increment N from the highest existing experiment number.
- **papers/**: Only modify existing `.tex` files unless creating a new paper.

### 2.3 Files That Must NOT Be Created

- No README.md (CLAUDE.md serves this role)
- No duplicate specs (Canonical Spec v2.0.md is authoritative)
- No scratch/temp files in the repo root
- No `.py` files outside `scc/`, `tests/`, `experiments/`, `papers/`

## 3. File Modification Rules

### 3.1 Canonical Spec v2.0.md

- **Only modify** when a theorem status changes (proved/retracted), an erratum is needed, or a new theorem is added.
- **Always** add an erratum note inline: `*(Erratum YYYY-MM-DD: <what changed and why>)*`
- **Never** silently change a proof status. The change must be logged in CHANGELOG.md.

### 3.2 Code (scc/)

- Run `python3 -m pytest tests/ -v` after any code change.
- Record the test count in CHANGELOG.md if it changes (e.g., "174 → 180 tests").
- If a function signature changes, grep for all callers and update them.

### 3.3 Papers (papers/)

- Only update when theory/code changes necessitate it.
- Note which section was modified in CHANGELOG.md.

## 4. Document Header Format

Every `.md` file in `docs/` must start with:

```markdown
# <Title>

**Date:** YYYY-MM-DD
**Session:** <brief session description, e.g., "Multi-formation gap closure">
**Category:** proof | audit | repair | theory | experiment | synthesis | generalization
**Status:** active | complete | superseded
**Depends on:** <list of prerequisite documents or theorems, if any>

---

<content>
```

## 5. CHANGELOG.md — Session Log

Every session that modifies files must append to `CHANGELOG.md`. Format:

```markdown
## YYYY-MM-DD — <Session Title>

### Summary
<1-3 sentences: what was accomplished>

### Files Created
- `path/to/file.md` — <one-line description>

### Files Modified
- `path/to/file.md` — <what changed>

### Theorem Status Changes
- <theorem name>: <old status> → <new status> (reason)

### Test Count
<N> tests passing (previously <M>)

### Open Items Carried Forward
- <anything unfinished that the next session should know>
```

## 6. Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Research doc | `UPPER-KEBAB-CASE.md` | `CORE-DEPTH-PROOF.md` |
| Iteration doc | `I<N>-<topic>.md` | `I14-SYNTHESIS.md` |
| Audit doc | `A<N>-<topic>.md` | `A7-transport-audit.md` |
| Repair doc | `R<N>-<topic>.md` or `GAP-CLOSURES-<N>.md` | `R7-basin-repair.md` |
| Experiment | `exp<N>_<snake_case>.py` | `exp16_birth_death.py` |
| Test file | `test_<module>.py` | `test_transport.py` |
| Date folder | `MM-DD` (within same year) | `04-01/` |
| Category folder | `lowercase/` | `proof/`, `audit/` |

## 7. Session Start Checklist

When starting a new session, Claude must:

1. **Read** `CONVENTIONS.md` (this file)
2. **Read** `CHANGELOG.md` (last entry) to understand where the previous session left off
3. **Check** `docs/00-overview.md` header for current project state
4. **Verify** test count: `python3 -m pytest tests/ --co -q 2>/dev/null | tail -1`
5. If continuing interrupted work, check `CHANGELOG.md` "Open Items Carried Forward"

## 8. When Multiple Agents Work in Parallel

- Each agent team writes to its own output file(s) in the correct `docs/YYYY-MM-DD/<category>/` path.
- The orchestrating session is responsible for updating `INDEX.md` and `CHANGELOG.md` after all agents complete.
- Agent output files should include the agent/team name in the header.

## 9. Superseding and Archiving

- When a document is superseded, add `**Status:** superseded by <new-file-path>` to its header. Do NOT delete it.
- When a theorem is retracted, keep the original proof doc but mark status as `retracted` with reason.
