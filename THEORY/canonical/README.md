> [!nav] Linked: [[MOC_canonical_authority]] · [[THEORY_INDEX]]

# THEORY/canonical/ — Authoritative Specification

**Promoted content only.** Work-in-progress, unverified hypotheses, and exploratory framings live elsewhere (`THEORY/working/` for active development, `THEORY/logs/daily/` for the chronological journal). Anything in this folder must have been promoted through the pipeline below.

## Contents

- **`DECLARATION.md`** — **(DECL-1.0, 2026-05-07) 먼저 읽기.** 이론 중심축 선언문. "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?" 중심 정리 T8, 6개 인식론적 질문(Q1~Q6), 이론의 범위와 비-주장 명시. 모든 수학 이전에 읽어야 할 2분 분량 문서.
- **`canonical.md`** — Authoritative specification. Current release is **CV-1.11 (2026-05-07)**. Counts: **54 Cat A / 14 Cat B / 5 Cat C / 5 Retracted** (**78 claims**, ~69% fully proved). Includes stereo extension (CV-1.6), P-F foundation (CV-1.7), P-F-A1 Package I fully Cat A (CV-1.9), K-selection equilibrium Cat B (CV-1.10), T-Temporal-Identity all-Cat-B + NQ closures (CV-1.11). Updated per merge, not on a fixed cadence.
- **`theorem_status.md`** — Theorem index (proved / conditional / open / retracted) + Open Problems Catalog (OP-0001..OP-0022). Active high-priority OPs: OP-0005, OP-0008, OP-0009; OP-0006 RESOLVED; OP-0011 PARTIALLY RESOLVED (Lemma 10); OP-0008-DIST CLOSED Cat B (Lemma 16).
- **`hypothesis_tree.md`** — Hypothesis dependency tree (HT-3.0, 2026-05-07). 블록이 수학적 주제 → 인식론적 질문(Q1~Q6)으로 재편. Phase 1 타겟: H-SINK. Authoritative source for hypothesis dependency structure and modification governance.
- **`figures/`** — Figure source scripts (Python). Rendered PNG/SVG live in the blog repo.

## Pipeline (Promotion Barrier)

The project uses a **3-stage promotion pipeline**:

```
THEORY/logs/daily/YYYY-MM-DD/    raw chronological record (write freely; not authoritative)
         |
         |  reorganize by topic + audit
         v
THEORY/working/<topic>.md         active theory development (one file per topic)
         |
         |  proof + review + tests + user merge decision
         v
THEORY/canonical/canonical.md     authoritative — one-way only
THEORY/canonical/theorem_status.md  index updated in same merge
THEORY/CHANGELOG.md               session log entry recorded
```

**This 3-stage flow is the single canonical pipeline** used by `CLAUDE.md`, `CONVENTIONS.md`, `working/README.md`, and `THEORY/logs/daily/MAIN_PROMPT.md`. The earlier 4-stage variant (with `weekly/weekly_draft_storming.md` and `weekly/weekly_summary.md` as required staging files) was simplified during the 2026-05-04 audit pass; weekly summaries are still produced for retrospective synthesis but are not a required staging step before canonical merge.

### Promotion criteria (from working to canonical)

A `working/<topic>.md` entry may be promoted only when all of the following hold:

1. The result is proved (Cat A) or has explicit conditional structure (Cat B/C, with conditions stated).
2. Implementation tests pass (where applicable; current baseline is 215 + 1 xfailed).
3. No contradiction with existing canonical content.
4. The working file references its provenance (daily logs, scripts, experiments).
5. User has reviewed and approved the merge.

### Editing rules for canonical files

- New theorem: insert a row in `theorem_status.md` and the corresponding section in `canonical.md`. Append a `THEORY/CHANGELOG.md` entry with date, version increment, and rationale.
- Inline correction: use `*(Erratum YYYY-MM-DD: what and why)*` markers in place. Do not rewrite history; preserve the original text and annotate.
- Retraction: mark with `*(Retracted YYYY-MM-DD: reason)*` inline; the original statement remains visible. Update `theorem_status.md` row and append a CHANGELOG entry.

### No reverse flow

A canonical theorem under re-examination does not move back to `working/`. It stays in `canonical/` with a visible erratum or retraction marker. The barrier is intentionally one-way.

## Why this discipline matters

The canonical layer protects the theory from contamination by ideas that have not been audited. The discipline only works if the barrier is respected in both directions: only promoted content enters, and edits to canonical content are done by erratum / retraction markers rather than by silent rewriting. When the barrier breaks (e.g. when working-state forecasts leak into `theorem_status.md`), the canonical layer loses authority. The 2026-05-04 audit pass corrected one such leak (forward-looking "W6+ pending" content was moved to CHANGELOG and `THEORY/logs/weekly/2026-05-W1/` strategic plan).
