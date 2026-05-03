# THEORY/logs/ — Research Journal

The chronological record of the research process. Daily logs are the raw record; weekly and monthly tiers are retrospective synthesis. **Promotion to canonical does not pass through this directory** — it goes through `THEORY/working/` (the topic-organized middle layer in the 3-stage pipeline).

## Structure

```
logs/
+-- daily/     YYYY-MM-DD/       raw record (write freely; non-authoritative)
+-- weekly/    YYYY-MM-W<n>/     retrospective synthesis + strategic planning
+-- monthly/   YYYY-MM/          (optional) macro retrospective; not active in current cadence
```

## Pipeline position

The canonical promotion pipeline is **3-stage**:

```
logs/daily/YYYY-MM-DD/   --reorganize by topic-->   working/<topic>.md   --proof + review + tests + user merge-->   canonical/
```

Weekly and monthly tiers under `logs/` are **retrospective**, not staging. A weekly summary is a useful synthesis artifact for the human reader, but is not a required step before canonical promotion. The earlier 4-stage variant (which required `weekly_draft_storming.md` and `weekly_summary.md` as staging) was simplified during the 2026-05-04 audit pass to align with `CLAUDE.md`, `CONVENTIONS.md`, `working/README.md`, and `daily/MAIN_PROMPT.md`.

## daily/

Write daily as needed. Not mandatory every day, but every substantive session should leave a trace.

Standard daily-directory layout (per `MAIN_PROMPT.md`):

```
logs/daily/YYYY-MM-DD/
+-- pre_brainstorm.md             pre-session conceptual frame (loose)
+-- plan.md                       day's execution plan (concrete deliverables)
+-- 01_<topic>.md                 substantive work, topic-specific names
+-- 02_<topic>.md
+-- ...
+-- 99_summary.md                 end-of-day summary + tomorrow seed
```

For research-development sessions, the standard `01_/02_/03_/99_` quartet from `MAIN_PROMPT.md` (`01_exploration.md`, `02_development.md`, `03_integration_and_new_open.md`, `99_summary.md`) is acceptable. For canonical-release or other single-deliverable sessions, topic-specific names (e.g. `01_T_L1_F_canonical_promotion_closure.md`) are also acceptable.

## weekly/ (retrospective synthesis)

Folder naming: `YYYY-MM-W<n>/` (week numbered within the month, by start-date convention).

Typical weekly artifacts:
- `weekly_summary.md` — week-end synthesis: what was canonicalized, what was retracted, what remains open, what next week should focus on.
- `<weekN>_strategic_plan.md` — forward-looking plan for the upcoming week (when produced).

These weekly artifacts are **non-canonical**. They support the human reader and the next week's planner. Direct edits to `canonical/` from a weekly file are not allowed; edits go through `working/`.

## monthly/

Optional. Currently empty for 2026-04. If used, contains macro-view synthesis of the month's weekly summaries.

## Separation between record and theory

The job of files under `logs/` is to record the process, not to define the theory. The theory itself lives in `canonical/`; active development lives in `working/`. A daily log is the right place for "today I tried X and hit Y", but the canonical statement belongs in `canonical/` after promotion.

## Non-conventions (no Research OS)

- No 5-role daily format (lead/proof/critic/experiment/archivist).
- No prefix-style registry IDs (D-/S-/T-/A-/E-/Q-/C-/P-/X-).
- No frontmatter metadata is required.
- Maximum directory depth is 2 (`logs/daily/<YYYY-MM-DD>/`).

The Research OS scaffolding tried in 2026-04-12 collapsed by 04-16 and is archived in `_archive/research_os_2026-04-12/`. Do not re-introduce it.
