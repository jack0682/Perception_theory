# plan.md — 2026-05-05 (W6 Day 2, post-Day-1-overdelivery, slack-week mode)

**Title:** 2026-05-05 Research Plan — W6 Day 2 (closure-rigor + Decision Point 4 capture).
**Session type:** W6 Day 2 — *post-overdelivery slack day*. Day 1 (2026-05-04) substantively absorbed the originally-scheduled Days 1–6 of the redesigned 4-goal W6 plan (G1+G2+G3+G4 all closed) plus a post-EOD chat-session that closed NQ-G1-2 (P9-tight regime experiment) and applied 3 light cross-doc corrections. Day 2 has **no critical-path inheritance** from Day 1.
**W6 scope:** 2026-05-04 (Mon, Day 1) ~ 2026-05-10 (Sun, Day 7 W6 close).
**Session working directory:** `THEORY/logs/daily/2026-05-05/`.
**Weekly buffer target:** `THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md` (latest-first 05-05 entry append at end of day).
**Day 1 EOD references:**
- `THEORY/logs/daily/2026-05-04/99_summary.md` §7 (post-EOD wrap-up unified summary)
- `THEORY/logs/daily/2026-05-04/plan.md` §EOD COMPLETE MARKER (Day 1 final accounting)
- `THEORY/CHANGELOG.md` 14 addendums (1st G1 audit closure → 14th NQ-G1-2 fresh-full-run validation)
- `THEORY/logs/weekly/2026-05-W1/W6_strategic_plan.md` (G1 status FULLY CLOSED + status text revisions across §1–§7)
- `THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md` EOD UPDATE section (latest)
- `THEORY/logs/daily/2026-05-05/pre_brainstorm.md` (sibling file — read this first for conceptual frame).

**Active runtime:** no team dispatch Day 2 by default; this is audit-closure-rigor + decision-capture work, single-thread.
**User calibration:** Day 2 inherits no critical path. The pre_brainstorm.md §3 recommends primary shape (S1) closure-rigor day, with (S2) NQ-G3-1 cleanup as fill-in if (S1) finishes early.

---

## §1. Starting State (W6 Day 1 EOD baseline)

- **Canonical version current:** **CV-1.5.2 (2026-05-02) + W6 D1 EOD T-L1-M supervised addition (2026-05-04)**. Counts: **47A / 5B / 5C / 5R = 62 claims**, 75% fully proved. Synced across canonical.md / theorem_status.md / canonical/README.md / Perception_theory/CLAUDE.md / Perception/CLAUDE.md.
- **T-L1-M** is canonically registered as Cat A *conditional* under $(P0)$–$(P11) + \phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau) + \tau < \tau_*^{\mathrm{post-R2}}$ where $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$. Entry at `canonical.md` §13 line 1491. C-0722 row at `theorem_status.md` line 197.
- **W6 4-goal plan G1+G2+G3+G4: all CLOSED Day 1.** Schedule slack ~3 days relative to original.
- **CV-1.6 release feasibility**: upgraded from "deferred indefinitely" to **"W6 D7 EOD candidate"**. Decision Point 4 (W6 strategic plan §5) requires **explicit user decision** before Day 3+ scope is committed.
- **Tests**: 215 passed + 1 xfailed (unchanged W5 D7 EOD baseline). Smoke `DiagnosticVector(Bind=0.853, Sep=0.924, Inside=0.998, Persist=1.000)` verified post-EOD chat session.
- **No autonomous-session canonical edits since EOD**; all Day 1 EOD canonical promotions were sustained-supervised.
- **Open follow-ons (W7+, not blockers)**: NQ-G1-1-ext (ρ_bg vs ρ_res empirical), NQ-G1-2-ext (‖R_j‖_∞ post-flow direct measurement), NQ-G1-4 candidate (per-formation K_soft^{(j)} → `working/MF/ksoft_kact_bridge_per_formation.md`), NQ-G1-6 candidate (T-L1-M perturbation extension → `working/MF/ksoft_kact_bridge_perturbation.md`).
- **Only deferred-numerical NQ remaining**: NQ-G3-1 (439/1920 stability under ε perturbation; theoretical pre-analysis suggests piecewise-constant outcome per `op_resolution.md` §11.3).
- **3 user-decision items pending**: weekly_draft_storming.md disposition (default leave-as-is), CV-1.6 release scheduling (Decision Point 4), W7+ seed work prioritization.

---

## §2. Day 2 Goals (3 items, prioritised; total ~3-4h)

### G2.1 (P0, ~2-3h) — Closure-Rigor Audit (pre_brainstorm shape S1)

**Target.** Adversarial cold-read of the W6 D1 EOD canonical state. Find any drift that the 14 addendums + 13 modified files + 10 new artifacts may have introduced. Pattern: chain verification per Issue #1–#5 lessons (canonical sub-item tables + packet crosswalks are authoritative; working-file self-attribution can be aspirational).

**Specific checks:**

1. **T-L1-M canonical entry (canonical.md §13 line 1491)**: re-read with adversarial intent. Cross-check against:
   - `working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` (the working draft) — does the canonical entry's hypothesis statement match the working draft's Theorem L-M statement exactly?
   - `theorem_status.md` C-0722 row (line 197) — does the row's hypothesis package match the canonical entry?
   - τ_*^post-R2 definition: appears in canonical entry, theorem_status row, working draft, and `02_development.md` §3.4 (post-erratum). All four should agree on `min(2ρ_pert, ρ_bg, r_birth)`.

2. **§15 closing summary (canonical.md ~line 1700-1710)**: count update 46A→47A, 61→62 propagated. But also check:
   - `theorem_status.md` Proof Status Summary (line 645–704) "47" appears correctly in (a) Category A row count, (b) example row "etc." includes T-L1-M, (c) "Total canonical theorems: 57 = 47 Cat A" line.
   - `canonical/README.md` 47A/62 line consistent with both above.
   - Both `CLAUDE.md` (Perception/ + Perception_theory/) reference the count consistently.

3. **NQ-G1-2 EXECUTED status across 4 layers**:
   - CHANGELOG 13th + 14th addendums (post-processing + fresh-full-run)
   - `op_resolution.md` §10.6 + §10.7 + §13.1 row 11 + §0 row 11 + §13.4 item 4
   - W6 strategic plan G1 follow-on note (NQ-G1-2 EXECUTED)
   - 99_summary.md §7.2 + §7.3 + §7.5 inventory row
   All four should agree NQ-G1-2 = ✅ EXECUTED, with NQ-G1-2-ext registered W7+ (not blocker).

4. **Issue #5 RE-EXAMINATION (CHANGELOG 12th addendum) verdict re-check**: REJECT-RETIRE for OAT-5 (`cobelonging_vs_sigmaD.md`) and OAT-6 (`pre_objective_K_field_tension.md`). Cross-check: do the working-file headers reflect canonical-scheduled D-CV1.6-O4 + v2.0 §1 amendment correctly (per 12th addendum corrections)?

5. **Cross-doc consistency on §3.2 erratum + §3.4 cross-reference**:
   - `03_integration_and_new_open.md` §3.2 erratum block
   - `02_development.md` §3.4 cross-reference erratum
   - `op_resolution.md` §9.4–§9.10 self-correction chain
   - `op_resolution.md` §13.1 row 9 + §13.2 + §13.4 item 1 markers
   - `op_resolution.md` §13.6 erratum log
   All five should agree: ρ_bg vs ρ_res is configuration-dependent, NQ-G1-1-ext W7+, Cat A conditional unaffected.

**Output:** `01_closure_rigor_audit.md` documenting the audit pass with findings (if any). If no drift found: explicit "CLEAN" verdict per check. If drift found: erratum proposal text (NOT applied autonomously; user-supervised).

**Failure mode:** if any check fails, halt the audit and surface the drift. Do not silently continue.

**Success criterion:** all 5 checks return CLEAN, OR drift surfaced + erratum proposal drafted.

### G2.2 (P1, ~30 min) — Capture User Decision on Decision Point 4 (CV-1.6 release scheduling)

**Target.** Day 2 is when this decision should be captured (per pre_brainstorm.md §6 + W6 strategic plan §5 Decision Point 4 OPEN status). Without it, every Day 3+ priority decision drifts.

**Approach.** Surface the decision explicitly to the user with three options:

- **Option A**: push CV-1.6 release at Day 7 EOD with Stage 0 inventory as sufficient parking-lot resolution. Stage 1 per-file Cat-status header drafting becomes post-CV-1.6 / W7+ work.
- **Option B**: defer CV-1.6 release to W7 alongside Stage 1. W6 D7 produces weekly_summary.md + CV-1.6 release packet skeleton at `working/CV-1.6_release_packet_skeleton.md`. Release applied at W7 D-something.
- **Option C**: defer CV-1.6 release further (e.g., W8+). W6 D7 closes with weekly_summary.md only; CV-1.6 release packet not started this week.

**Recommended default (per pre_brainstorm.md §6):** Option B (defer to W7 alongside Stage 1). Rationale: avoids premature-release hazard H3; allows W6 D2-D7 slack to be either (S1) closure-rigor or (S2) NQ-G3-1 + Stage 1 prep without committing to release packet drafting yet.

**Output:** user response captured in `01_closure_rigor_audit.md` §0 or `02_decision_point_4_capture.md`. If Option B chosen, the weekly summary draft target for D7 is "weekly_summary + CV-1.6 release packet skeleton" (working only, not canonical).

**Failure mode:** if user defers the decision again, mark it explicitly as "deferred to Day 3" and capture it in tomorrow's plan.

**Success criterion:** user committed to A / B / C; Day 3-7 priority unblocked.

### G2.3 (P1, ~1-2h, fill-in if G2.1+G2.2 finish early) — NQ-G3-1 Cleanup (pre_brainstorm shape S2)

**Target.** Close the only remaining "📋 DEFERRED" row in `op_resolution.md` §13.1 (row 10: NQ-G3-1 ε stability of 439/1920 anchor). Per §11.3 theoretical pre-analysis, expected outcome is piecewise-constant: 22.9% for ε ∈ [0, 30), drops to 0 at ε = 30 (initial state has per-slot masses {30,30,30,0} so K_act jumps at ε = 30).

**Approach.** Two-phase pattern matching NQ-G1-2 (per pre_brainstorm.md §5 O3):
- Phase A (post-processing): re-classify existing baseline `l1i_constants_feasibility.json` under multiple ε values via `op_resolution_nq_g3_1_epsilon_stability.py` wrapper. Cheap (~seconds).
- Phase B (fresh-full-run validation): run `l1i_constants_feasibility.py --epsilon X --output ...` for at least 2 control ε values; verify post-processing predictions match.

Note: `--epsilon` may not be a current CLI arg of l1i_constants_feasibility.py. If not, the fresh-full-run phase requires a small script copy + patch (analogous to `l1i_constants_feasibility_p9_tight.py`). Estimated total ~1-2h.

**Output:** `op_resolution_nq_g3_1_epsilon_stability.py` (post-processing wrapper) + JSON output + (optional) script copy if fresh-full-run validation requires it. CHANGELOG entry: "W6 D2 NQ-G3-1 EXECUTED" — only deferred-numerical NQ from W6 D1 batch is now closed.

**Failure mode:** if theoretical prediction fails (i.e., the sweep is not piecewise-constant), surface the deviation as a new finding and re-classify NQ-G3-1 status.

**Success criterion:** NQ-G3-1 ✅ EXECUTED with prediction confirmed (or deviation documented). `op_resolution.md` §0 row 10 + §11.5/§11.6 + §13.1 row 10 + §13.4 item 4 all updated.

---

## §3. Day 2 Non-Goals (scope limit)

Things deliberately NOT attempted Day 2:

- **NQ-G1-1-ext / NQ-G1-2-ext / NQ-G1-4 candidate / NQ-G1-6 candidate.** All explicitly W7+ per W6 strategic plan §2 + W6 D1 EOD final inventory. Starting any of these today defeats the closure-week commitment (W6 strategic plan §7).
- **Stage 1 per-file Cat-status header drafting on 49 parking-lot files.** W7+ scope per W6 strategic plan §3 (was Day 6 task; deferred). Day 2 is not the right time even if (S2) NQ-G3-1 finishes early.
- **CV-1.6 release packet drafting.** Conditional on Decision Point 4 outcome (G2.2). If Option A chosen, packet drafting may slip to Day 3-7. If Option B/C, no Day 2 work.
- **Canonical edits.** Day 2 should NOT edit canonical/* unless G2.1 audit surfaces drift requiring an erratum (in which case the erratum is a *proposal* for user-supervised application, not autonomous edit).
- **`weekly_draft_storming.md` morning-entry deletion.** Default action is leave-as-is (historical record). Only delete if user explicitly requests.
- **OMC team dispatch / external agent runs.** Single-thread audit work; no parallel dispatch.

---

## §4. Carry-forward (from Day 1 EOD)

Three explicit carry-forward items per `99_summary.md` §7.8 and `plan.md` §EOD COMPLETE MARKER:

1. **`weekly_draft_storming.md` disposition** — already updated W6 D1 EOD chat session with EOD UPDATE section; default action is leave-as-is. (No Day 2 dependency.)
2. **CV-1.6 release scheduling (Decision Point 4)** — addressed by G2.2 above.
3. **W7+ seed work prioritization (4 follow-ons)** — no Day 2 dependency; W7+ activation question.

Plus the Day 2-7 candidate scope options from `99_summary.md` §7.7:

- (a) G4 Stage 1 per-file Cat-status header drafting on 49 files — W7+ deferred.
- (b) NQ-G3-1 ε-stability sweep — addressed by G2.3 above (P1 fill-in).
- (c) CV-1.6 release packet preparation — conditional on G2.2 Decision Point 4 outcome.
- (d) W7+ seed work — W7+ deferred.
- (e) Day 7 weekly_summary.md draft — Day 6-7 work, not Day 2.

---

## §5. Decision Points (Day 2)

These need explicit decisions during Day 2 morning, otherwise they become silent drift.

1. **G2.2 morning, ~30 min**: Decision Point 4 (CV-1.6 release scheduling — A/B/C). Affects Day 3-7 priority. **CRITICAL.**
2. **G2.1 conclusion, ~end of audit**: if drift surfaced, decide whether to apply erratum same-day (user-supervised) or defer to Day 3.
3. **G2.3 conditional on G2.1 + G2.2 finishing early**: pursue NQ-G3-1 today vs defer to Day 3 (only if user explicitly wants closure of all op_resolution.md deferred rows).

---

## §6. Risks (Day 2)

Per `pre_brainstorm.md` §6 hazard tree:

- **(H1) Confidence inflation.** Audit finds nothing; we conclude Day 1 was bulletproof. Mitigation: G2.1 explicitly looks for adversarial gaps, not just confirms claims. If audit returns CLEAN, that's a *finding*, not a default.
- **(H2) Scope creep into W7+.** Mitigation: §3 non-goals enumeration is binding. Day 2 ends without any W7+ candidate work started.
- **(H3) Premature CV-1.6 release.** Mitigation: G2.2 Decision Point 4 capture explicit; default recommendation is Option B (defer to W7 alongside Stage 1).
- **(H4) Hidden drift from 14 addendums + 13 modified files.** Mitigation: G2.1 5-check chain verification. If all 5 return CLEAN, hidden drift probability low. If any check fails, fail fast.
- **(H5) Pacing dissonance.** If Day 2 also closes "too fast", does that re-set baseline expectation? Mitigation: explicitly note in 99_summary.md §X whether Day 2 felt "right-sized" or "still over-delivered". This becomes data for future planning.

---

## §7. Hard-Constraint Sweep Target (Day 2)

The Day 2 session must produce these explicitly in the closing 99_summary.md or 01_closure_rigor_audit.md:

- [ ] Canonical 직접 수정 0 (autonomous-session). Erratum proposals only if drift surfaced.
- [ ] Working/ 직접 수정 0 (autonomous-session). Same.
- [ ] scc/ 0 edits. Tests still 215 passed + 1 xfailed.
- [ ] Silent OP resolution: 0.
- [ ] N-1 / CN5 / CN6 / CN7 / CN10 / CN15 / u_t primitive: all preserved.
- [ ] No Research OS resurrection.
- [ ] No OMC pool / external agent dispatch.
- [ ] No external framework reduction.
- [ ] No metastability claim w/o P-F flag.

Same template as W6 D1 EOD; the only relaxation possible is if user explicitly authorizes a same-day erratum application from G2.1 audit (in which case canonical/working write count is non-zero but documented).

---

## §8. Files Expected (Day 2)

`THEORY/logs/daily/2026-05-05/`:
- `plan.md` (this file)
- `pre_brainstorm.md` (sibling, conceptual frame)
- `01_closure_rigor_audit.md` (G2.1 audit output — REQUIRED)
- `02_decision_point_4_capture.md` (G2.2 user decision capture — REQUIRED if §0 of 01 doesn't capture it)
- `03_nq_g3_1_epsilon_stability.md` (G2.3 conditional fill-in)
- `99_summary.md` (Day 2 EOD summary — REQUIRED)

`CODE/scripts/` (conditional on G2.3):
- `op_resolution_nq_g3_1_epsilon_stability.py` (post-processing wrapper, NEW if G2.3 pursued)
- `l1i_constants_feasibility_epsilon_sweep.py` (script copy + patch if fresh-full-run requires CLI extension, NEW if G2.3 pursued)

`CODE/scripts/results/` (conditional on G2.3):
- `op_resolution_nq_g3_1_epsilon_stability.json` (post-processing output)
- `l1i_full_eps*.json` (1-2 fresh full run outputs for validation)

`THEORY/CHANGELOG.md`:
- W6 D2 closure-rigor audit entry (REQUIRED if G2.1 finds no drift; OR drift-erratum entry if drift found).
- W6 D2 Decision Point 4 capture entry (REQUIRED).
- W6 D2 NQ-G3-1 EXECUTED entry (conditional on G2.3).

`THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md`:
- 2026-05-05 entry append (latest-first above the 2026-05-04 entries) — REQUIRED at Day 2 EOD.

---

## §9. Success Criteria for Day 2

- **Bronze (minimum):** G2.1 audit completed (CLEAN or drift surfaced) + G2.2 Decision Point 4 captured. ~3h. Day 2 ends with the W6 status fully consolidated.
- **Silver (default target):** Bronze + G2.3 NQ-G3-1 EXECUTED. ~4-5h. Day 2 closes the last op_resolution.md deferred-numerical row.
- **Gold (stretch):** Silver + a CV-1.6 release packet skeleton drafted at `working/CV-1.6_release_packet_skeleton.md` (only if Option B chosen in G2.2). ~5-6h. Day 2 produces a forward-looking artifact.

**Anti-pattern (do not aim for):** "all of W7+ seed work started" — that breaks closure-week commitment.

---

## §10. Day 2 EOD Carry-Forward Target

Whatever Day 2 produces, the EOD summary should explicitly answer:

1. Did G2.1 audit find drift? If yes, what?
2. Did G2.2 Decision Point 4 get captured? Which option (A/B/C)?
3. Did G2.3 fill-in happen? If yes, what was the NQ-G3-1 verdict?
4. What's the Day 3 carry-forward? (Should be empty or near-empty if Bronze met.)
5. Any new open user-decision items?

---

**End of plan.md. Sibling file: `pre_brainstorm.md` for conceptual frame (read first).**
