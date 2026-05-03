# CONVENTIONS.md — Repository & Theory Discipline

Read at session start with `THEORY/canonical/canonical.md`, `THEORY/canonical/open_problems.md`, and the last entry of `THEORY/CHANGELOG.md`.

---

## 1. Top-Level Split: CODE / THEORY

Two physically separated trees:

| Tree | Contains | Imported / Executed? |
|------|----------|----------------------|
| `CODE/` | `scc/`, `tests/`, `experiments/`, `scripts/`, `papers/` | Yes — run everything from `cd CODE` |
| `THEORY/` | `canonical/`, `working/`, `logs/`, `CHANGELOG.md` | No — read-only narrative |

**Do not put executable code under `THEORY/`.**
**Do not put theory narrative under `CODE/`** (except LaTeX sources, which are theory output but require Python to generate figures — these live in `CODE/papers/`).

---

## 2. THEORY/ Internal Structure

```
THEORY/
├── CHANGELOG.md           state changes to canonical (status changes, errata, retractions)
├── canonical/             authoritative specification — no contamination allowed
├── working/               active theory development (topic-based, free-form)
└── logs/                  chronological journal (daily / weekly / monthly)
```

### Promotion Pipeline (Contamination Barrier)

```
logs/daily/YYYY-MM-DD.md   ──── reorganize by topic ──→   working/<topic>.md
                                                                │
                                                                │ proof + review + tests
                                                                ↓
                                                     canonical/canonical.md
                                                    (one-way — no return path)
```

- `canonical/` accepts **promoted content only**. No direct editing from raw ideas.
- Retractions from `canonical/` are **explicit** — `*(Retracted YYYY-MM-DD: reason)*` inline, logged in `THEORY/CHANGELOG.md`. Retracted content stays visible (crossed-out, not removed).
- **No reverse flow.** A canonical theorem under re-examination does not move back to `working/`. It stays in canonical/ with a visible erratum/retraction marker.

### canonical/ rules

Edit only to:
1. Add a newly promoted theorem (`canonical.md` body + row in `theorem_status.md`)
2. Insert inline erratum: `*(Erratum YYYY-MM-DD: what and why)*`
3. Mark explicit retraction: `*(Retracted YYYY-MM-DD: reason)*`

All three require a `THEORY/CHANGELOG.md` entry.

### working/ rules

- One file per topic. Filename: descriptive, snake or kebab case (`F-1_kinetic.md`, `multi-formation.md`).
- Header optional; minimum recommended:
  ```markdown
  # <topic>
  **Status:** exploring | developing | near-promotion
  **Last touched:** YYYY-MM-DD
  **Canonical refs:** canonical.md §X.Y
  ```
- Free-form body.
- Once fully promoted, either delete working file (its content is now in canonical.md) or move to `_archive/working_promoted/YYYY-MM-DD_<topic>.md`.

### logs/ rules

- **daily/YYYY-MM-DD.md** — only when meaningful work happens that day. No daily obligation.
- **weekly/YYYY-Www.md** — optional week summary.
- **monthly/YYYY-MM.md** — optional month summary.
- Free-form. No metadata frontmatter required.

---

## 3. CODE/ Discipline

### Running things

**Everything is run from `CODE/` as cwd.** `tests/conftest.py` has a 3-line sys.path bridge that resolves `scc` relative to `CODE/`.

```bash
cd CODE && python3 -m pytest tests/ -v
```

### Tests

- Run `cd CODE && python3 -m pytest tests/` after any code change. 175 must pass.
- Test count delta → append entry to `THEORY/CHANGELOG.md`.
- Signature change → grep callers and update.
- Extend existing modules before adding new `scc/*.py`.

### Experiments

- Name: `experiments/exp<N>_<snake_case>.py`. N increments from highest existing.
- Results: `experiments/results/` — one `.json` per run (+ optional `.csv`).
- **Do not rename existing exp<N>.** Numbering is stable history.

### Papers

- `papers/` — IEEEtran.cls + figures/ + generate_figures.py (the `paper1_math.tex` / `paper2_cogsci.tex` drafts were deleted on 2026-05-04 per user decision to rewrite from scratch later; see `THEORY/CHANGELOG.md` 2026-05-04 entry).
- `papers/generate_figures.py` for figures.

---

## 4. CHANGELOG Format

Append to `THEORY/CHANGELOG.md` after any session that modifies canonical, working, or code:

```markdown
## YYYY-MM-DD — <title>

### Summary
<1–3 sentences>

### Files Created / Modified
- `<path>` — <short>

### Theorem Status Changes
- <theorem>: <old> → <new> (reason)

### Test Count
<N> passing (previously <M>)

### Carry-Forward
- <unfinished items>
```

---

## 5. Naming

| Type | Pattern | Example |
|------|---------|---------|
| Experiment | `CODE/experiments/exp<N>_<snake>.py` | `exp14_multi_persist.py` |
| Test | `CODE/tests/test_<module>.py` | `test_transport.py` |
| Canonical spec | `THEORY/canonical/canonical.md` (single file) | — |
| Working topic | `THEORY/working/<topic>.md` | `F-1_kinetic.md` |
| Daily log | `THEORY/logs/daily/YYYY-MM-DD.md` | `2026-04-20.md` |
| Weekly log | `THEORY/logs/weekly/YYYY-Www.md` | `2026-W17.md` |
| Monthly log | `THEORY/logs/monthly/YYYY-MM.md` | `2026-04.md` |

**No prefix registries** (D-/S-/T-/A-/E-/Q-/C-/P-/X-) and **no numbered top-level directories** (00_meta, 01_canonical, ...). The Research OS that used these patterns is archived at `_archive/research_os_2026-04-12/` and must not be re-introduced.

---

## 6. Forbidden

- Numbered top-level dirs (00_meta, 01_canonical, ..., 99_templates)
- Per-item registry files (standalone Q-xxxx, P-xxxx, X-xxxx, etc.)
- 5-role daily logs (lead/proof/critic/experiment/archivist format)
- Editing `canonical/` directly from raw ideas — must pass through `working/` with review
- Editing inside `_archive/` — if something there is still alive, pull a copy out explicitly and log why
- Silently resolving an open problem — F-1 / M-1 / MO-1 stay open until explicit promotion

---

## 7. When Something is Superseded

1. Mark intent in `THEORY/CHANGELOG.md`.
2. Move the file to `_archive/<topic>_YYYY-MM-DD/` (preserve with date stamp).
3. Do not delete — preserve the record.
