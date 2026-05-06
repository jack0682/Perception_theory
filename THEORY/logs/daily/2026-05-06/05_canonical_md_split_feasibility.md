# 05_canonical_md_split_feasibility.md — canonical.md Split Feasibility

**Session:** 2026-05-06 (W6 Day 3 G3.5, P1).
**Debt addressed:** W4 documentation — canonical.md has grown to ~1,700 lines; navigability degraded.
**Question:** Is splitting into Part I / Part II / Part III / Part IV feasible? When?
**Recommendation:** W10 D6 (not earlier). Rationale below.

---

## §1. Current State

| Metric | Value |
|---|---|
| canonical.md size | ~1,700 lines (CV-1.5.2) |
| Sections | §1 Universe / §2-§6 Axioms / §7-§12 Core theory / §13 Theorems / §14 Commitments / §15 Summary |
| Cross-references | ~40+ inter-section references (§13 theorems reference §6 axioms, §14 commitments reference §13 theorems, etc.) |
| Theorem count | 62 claims (47A / 5B / 5C / 5R) — all in §13 |
| Active edit frequency | ~3-4 edits/week (W5-W6 rate) |

---

## §2. Proposed Split Structure

**Part I — Foundations** (§1-§6): Universe, primitive, closure, energy, axioms. ~300 lines.
**Part II — Core Theory** (§7-§12): Phase transitions, formations, σ-framework, multi-formation. ~500 lines.
**Part III — Theorem Catalog** (§13): All 62 claims with proof sketches. ~600 lines.
**Part IV — Commitments + Conventions** (§14-§15): CN1-CN17, Commitment 1-16, summary. ~300 lines.

---

## §3. Feasibility Analysis

### 3.1 What Works

- Logical structure is already Part-shaped: Foundations → Core → Theorems → Commitments.
- Part III (Theorem Catalog) is already the largest and most independently navigable unit.
- `theorem_status.md` already serves as the Part III index — split would just formalize this.

### 3.2 What Doesn't Work (Yet)

**Cross-reference density:** §13 theorems reference §6 axioms (A1-A6), §7 phase transition conditions, §9 σ-framework definitions. A split creates cross-file links. In Markdown, these require either:
  - Absolute paths (brittle — path-dependent).
  - Relative paths (manageable, but must be maintained on every reorganization).
  - A single table-of-contents file pointing to all parts.

**Active edit frequency:** canonical.md is edited 3-4 times/week. During high-frequency editing, maintaining consistency across 4 files is harder than editing 1 file. The split adds overhead proportional to edit rate.

**Promotion pipeline dependency:** The promotion pipeline (`daily → working → canonical`) currently has a single canonical target. A split requires specifying *which* Part a promoted item goes to — adds a routing decision to every promotion.

**Retraction markers:** Retracted theorems (5R) have inline markers. In a split, a retraction in Part III must remain consistent with the theorem_status.md index. Currently these are in one file — split increases consistency maintenance.

### 3.3 Cost-Benefit by Timeline

| Timeline | Cost | Benefit | Net |
|---|---|---|---|
| W7 (now) | Very high (disrupts active editing; cross-refs not yet stable) | Low (file is navigable now via §N headers) | **NO** |
| W8-W9 | High (P-F framework additions still active) | Medium | **NO** |
| W10 D6 | Low (post-CV-1.7 freeze; editing rate drops) | Medium (navigability at ~2,000 lines) | **YES** |
| v2.0 prep | Natural (v2.0 introduces new §§ → split for new structure) | High (v2.0 reader-facing) | **YES** |

---

## §4. Recommendation

**Recommend: Split at W10 D6 (post-CV-1.7 freeze), as a CV-1.7 → v2.0 structural preparation.**

**Conditions for proceeding:**
1. CV-1.7 promotion complete and frozen (no active theorem additions for ≥ 1 week).
2. Cross-reference audit complete (identify all §N→§M links; convert to explicit `[§N](partX.md#anchor)` format).
3. `theorem_status.md` index verified as complete (all 62+ claims indexed; can serve as standalone Part III table of contents).
4. Promotion pipeline routing decision documented (which Part receives new promoted items).

**Do not split before CV-1.7.** The W6-W9 period has active OP resolution (OP-0005, OP-0008, OP-0009, OP-P-F) feeding new theorem statements into §13. Splitting now creates a moving-target problem.

---

## §5. Interim Navigability Improvements (W7)

Instead of splitting, apply these cheap improvements at W7 D1:
- Add a **§0 Table of Contents** to canonical.md (6-line quick-nav for §1-§15).
- Add **anchor tags** at each §N header for direct linking from theorem_status.md.
- Add a **"Latest changes" box** at §0 (last 3 entries from CHANGELOG.md, updated on each CV release).

These cost ~15 min and recover most navigability value without split risk.

---

**End of `05_canonical_md_split_feasibility.md`. Recommendation: no split before W10 D6. Interim improvements at W7 D1 (§0 ToC + anchors). G3.5 complete.**
