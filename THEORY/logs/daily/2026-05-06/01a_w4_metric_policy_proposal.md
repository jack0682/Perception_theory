> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 01a_w4_metric_policy_proposal.md — W4 Metric: Substance:Administrative Ratio

**Session:** 2026-05-06 (W6 Day 3 G3.11).
**Parent:** `01_strategic_recalibration_core.md` §4.
**W4 Debt:** Recent 2 weeks ~15h administrative, 0 new substantive theorems (T-L1-M was W5 D7 working draft). Ratio ~1:15 (alarm).

---

## §1. Metric Definition

**`substance_count` (S)** — per week:
- Each new theorem promoted Cat A/B/C in canonical.md: +1 each
- Each working draft *substantively expanded* (≥1 KB new mathematical content, not status updates or cross-references): +1 each
- Each substantive OP sub-item resolution (PARTIALLY → RESOLVED with explicit witness): +1 each

**`administrative_count` (A)** — per week:
- Each CHANGELOG entry ≥500B without a corresponding S increment: +1
- Each audit pass entry (closure-rigor audit, chain-verification, Issue series): +1 per session
- Each parking-lot inventory update (Stage 0/1/2 status rows, file header edits only): +1 per batch
- Each NQ status row update without new mathematical result: +0.5 per batch
- Each `99_summary.md` / `weekly_summary.md` / `plan.md` written: +0.5 each (documentation of work, not work itself)

**Ratio = S : A** (displayed as fraction, e.g., 2:7 = 0.29).

---

## §2. Measurement Protocol

**When:** Every week at EOD (weekly_summary.md or weekly_draft_storming.md latest entry).

**Format — `[W-metric]` section in weekly document:**

```markdown
### [W-metric] W6 Substance:Administrative Ratio

| Category | Count | Items |
|---|---|---|
| Substance (S) | X | e.g., T-L1-M promotion, NQ-G3-1 EXECUTED |
| Administrative (A) | Y | e.g., 14 addendums, Issue #1-#5 series, … |
| Ratio S:A | X:Y (= X/Y) | |
| Alarm? | yes/no | alarm if A ≥ 2 × S |
```

**Alarm rule:** `A ≥ 2 × S` → alarm **yes** → next week plan must include R1-style redirection (at least 40% of budget on substantive debt, not administrative work).

**Not counted:** reading passes, context loading, planning (these are overhead, not output).

---

## §3. W6 Retrospective Measurement

| Category | Count | Items |
|---|---|---|
| Substance (S) | ~2 | T-L1-M canonical promotion (+1); NQ-G3-1 EXECUTED (empirical anchor, +1) |
| Administrative (A) | ~30 | 14 CHANGELOG addendums (W6 D1), 12 NQ resolution entries, Issue #1-#5 series (5 audit sessions), Stage 0 inventory, 3 W6 D2 CHANGELOG entries, W6 D2 99_summary, plan files |
| Ratio S:A | 2:30 = 0.07 | |
| Alarm? | **YES** (very strong administrative dominance) | A ≈ 15× S |

**W6 alarm analysis:** The 14-addendum day (W6 D1) was justified as closure of W4-W5 accumulated work. But the ratio makes explicit that *the week produced ~15h of packaging for ~1h of new mathematical content*. This is the O5' self-proliferation pattern: administrative documentation generates more administrative documentation (audit → CHANGELOG → 99_summary → weekly_summary).

---

## §4. W7-W10 Targets

| Week | Substance target | Administrative cap | Target ratio | Alarm threshold |
|---|---|---|---|---|
| **W7** (debt-paydown) | S ≥ 3 (NQ-G1-2-ext result + OP-0009-Pre Phase 1 working draft + Stage 1 Cat-status headers on ≥10 files) | A ≤ 6 | 3:6 = 0.5 | alarm if A ≥ 6 |
| **W8** (substantive theorem) | S ≥ 6 (OP-0009-Pre Phase 2 + OP-0005 Layers A+C + OP-0009-A/F) | A ≤ 4 | 6:4 = 1.5 | alarm if A ≥ 12 |
| **W9** (P-F + OP-0008) | S ≥ 5 (P-F axiom v1 + OP-0005 Layer B + OP-0008 Path B) | A ≤ 4 | 5:4 = 1.25 | alarm if A ≥ 10 |
| **W10** (closure + CV-1.7) | S ≥ 4 (CV-1.7 promoted entries, OP resolutions) | A ≤ 5 (release activities) | 4:5 = 0.8 | alarm if A ≥ 8 |

W8 = target 2:1 substantive dominance (the benchmark for a "real theorem week").

---

## §5. Failure Mode and Mitigation

**Failure mode:** The metric measurement itself is an administrative item (A + 0.5 per measurement, per §1). If metric leads to more meta-documentation about the metric, the recursion is self-defeating.

**Mitigation:**
- Measurement capped at ~5-10 min per week (table fill-in only; no analysis required unless alarm fires).
- Alarm-triggered analysis capped at ~15-30 min (identify which items drove alarm + next-week correction).
- The metric is a *monitoring tool*, not a deliverable. It does not appear in CHANGELOG unless alarm fires and triggers a redirection day.

**Anti-pattern:** If alarm fires 2 consecutive weeks and redirection is declared but no actual S items produced, the third week should *not* produce another redirection calendar — it should produce actual mathematical work (even if incomplete).

---

**End of `01a_w4_metric_policy_proposal.md`. W4 metric defined. W6 retrospective: 2:30 = alarm YES. W7-W10 targets: S:A ≥ 1:1 minimum, W8 target 2:1.**
