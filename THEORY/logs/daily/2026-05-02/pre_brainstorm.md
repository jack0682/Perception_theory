# pre_brainstorm.md — 2026-05-02 W5 Day 6 (forward-leaning execution + W5 weekly close substance pre-think)

**Type:** Pre-session brainstorm. Sits next to `plan.md` as the looser mental frame for Day 6.
**Status:** Drafted 2026-05-01 EOD after Day 5 reconciliation close + 9-item retraction inventory + 1 substantive Cat A finding (R-1: $A_2/A_1 = 2/3$ exactly at every $L \geq 2$). Read this before plan.md execution Day 6 morning.
**Use:** Mental frame for the day. Not the execution contract; that is plan.md. This file captures *why* Day 6 should feel different from Day 5 and from Day 4.

---

## §0. Day 6 Feeling in One Sentence

Day 5 was cooling and measuring; Day 6 is **measured forward execution + W5 weekly close substance**. Day 7 is the close ceremony.

The trap to avoid: feeling that Day 5 was "just paperwork" and Day 6 should be "real work" (which would slide into Day 4-style burst). The opposite trap: feeling that Day 6 is "weekly_summary day" and reduce to clerical writing (Day 7-style premature finalization). Both extremes are wrong. Day 6 is *measured forward execution* — execute the *named* deferred items (3 verifiable artifacts), draft the W5 weekly close substance (1 long draft), and pre-condition W6 D1 dispatch (2 preliminary reports). Six artifacts in nine hours, none of them new theory branches.

---

## §1. What Day 5 Actually Achieved (handoff context)

The right way to think about Day 5 is **honest reorganization + 1 real Cat A finding**:

1. **9-item retraction inventory** (`2026-05-01/99_summary.md` §13): Day 4 burst contained 9 distinct items requiring correction or recalibration. Most are process-level; one (R-1) is arithmetic-level.

2. **R-1 substantive finding**: post-EOD `nq187b_L_extrapolation.md` §2.6 table claimed L-dependent values 0.80 / 0.762 / 0.703 / 0.668 / 0.659 → 2/3 asymptotic. Day 5 supplementary direct compute (`nq187b_a2_a1_extrapolation.py`, residual L² = 1.1×10⁻¹⁶) revealed: the closed-form is **identically 2/3 at every $L \geq 2$**. No finite-L correction. The post-EOD table is arithmetically wrong; correct $\sum_i \cos^4 = 3L/8$ exactly.

3. **R-2 priority elevation**: β-path conditional → unconditional W6 D1-D2 dispatch. R22's claim 4 vs structural 2/3 is now a *convention/derivation* question (β-path) — not a *finite-L correction* question (which doesn't exist).

4. **CV-1.7 parking lot vindication**: post-EOD un-audited cluster default = PARTIAL → CV-1.7 parking lot. R-1 finding *justifies* this discipline — the cluster contained a real arithmetic error caught only by Day 5 supplementary cross-check.

5. **W6 D1-D7 plan preview**: 5 specialist teammate roles parked (`gamma-path-prover` + `r22-audit-prover` [R-2 elevated unconditional] + `nq242-ph-engineer` + `oat5-c_t-prover` conditional + `cv16-finalizer`); 8 risks + 6 success criteria.

The carry-forward to Day 6: Day 5 named **what** to do. Day 6 must **do** it.

---

## §2. The Real Day 6 Question

Day 6 is **not**:

- "Can we add more theory like Day 4?"
- "Can we polish W5 weekly_summary like Day 7?"
- "Can we resolve T-σ-Theorem-4 today?"
- "Can we promote post-EOD cluster files now?"

Day 6 **is**:

> Can we execute the 5 named deferred items (errata application / NQ-244 launch / OAT-2 PH layer / OAT-3 Option 3 cleanup / W5 weekly_summary substantive draft) without sliding into either Day 4 burst or Day 7 finalization, AND can we pre-condition W6 D1 dispatch entry via β-path/γ-path preliminary reading?

That is the whole game.

If by Day 6 EOD all 5 items are done at *acceptable* quality (NQ-244 launched and not interpreted; weekly_summary 80-90% draft not 100% polish; OAT-2/3 extensions ~50/40 lines not 200), then Day 7 has clean handoff. If any single item balloons, the others slip.

---

## §3. NQ-244 Pre-Think — most schedule-impactful

NQ-244 is the **single most schedule-impactful Day 6 item**. If it doesn't launch Day 6, the W6 D4 result analysis lane slips by 1-2 days — which compresses the W6 D5-D7 packet finalize window.

### 3.1 Why launch matters more than perfection

The script will run for 10-12 hours overnight. Its design quality is *bounded* by the existing templates (`_v5_3D_torus.py` + `_f7_K10_LSW.py` + `_q2_NQ220_LSW.py`). It is **not** new theory; it is *combining existing infrastructure* for a 3D K=10 torus run.

Therefore Day 6 should *not* perfectionist-tune the script. The acceptable targets:
- Smoke test passes on $T^3_5$ K=2 T=10 (~30s runtime).
- Full launch starts; PID logged.
- Standard parameters (α=1.0, β=4.0, T=200, K=10, $T^3_{15}$).
- No partial output read.

If smoke test fails at 10:00 → fix in 15 min OR descope to script-prep-only and operator launch later. Do **not** fix into Block 2.

### 3.2 What NOT to do

- **Don't** add new dynamics features (e.g., adaptive timestep) — base templates suffice.
- **Don't** read partial output even out of curiosity ("just to see if it's running") — Day 6 anti-drift binding.
- **Don't** add interactive plotting — script-only, JSON output.
- **Don't** scale up to $T^3_{20}$ K=15 because "we have time" — spec is $T^3_{15}$ K=10 per `2026-05-01/05_*` §3.1.

### 3.3 If smoke fails

`5_*` §2.2 + Block 1 §10:00-10:15 cap is 15 min for smoke. If smoke fails:
- Inspect error in 5 min.
- If error is obvious (template mismatch, parameter error): fix in remaining 10 min.
- If error is non-obvious: descope. Document in Day 6 99_summary §3 + W6 D1 morning lead applies fix.

NQ-244 launch is a *recovery item* (W6 D4 schedule), not an *atomic Day 6 deliverable*. Slip is acceptable; over-engineering is not.

---

## §4. W5 weekly_summary Pre-Think — substance not polish

### 4.1 What weekly_summary is

W5 weekly_summary.md is the *internal* close of W5 — not paper, not canonical. It serves three audiences:
1. **Future-self**: Day 7 lead reads to finalize; W6 D1 lead reads to enter W6.
2. **User**: weekly-level trajectory tracking; ladder achievement record; retraction inventory.
3. **Cross-week archive**: W4 weekly_summary template was ~25 pages; W5 will be comparable.

Per W4 precedent: substantive narrative + cumulative tables + critical findings + OP advance + hard constraint compliance + W7 carry. Not a polished paper section.

### 4.2 What Day 6 produces vs Day 7 produces

**Day 6 (substantive draft, 80-90%)**:
- All 8 sections written through.
- All cumulative tables populated (counts may need Day 7 verification).
- All critical findings recorded.
- All retractions cross-referenced (per `2026-05-01/99_summary.md` §13).
- Sections marked `[Day 7 finalize: cross-reference verify]` where exact numbers need recheck.
- Sections marked `[Day 7 finalize: minor polish]` where prose is good-enough but not final.

**Day 7 (finalize, 10-20%)**:
- Cross-reference verification (every cited file exists; line counts current).
- Minor polish (sentence-level, not section-level).
- W6 carry forward addition (post-Day-6 EOD signals).
- Final sweep for retraction completeness.

### 4.3 What NOT to do Day 6

- **Don't** rewrite the W4 weekly_summary template in Day 6's voice. Read it once for structure; then proceed.
- **Don't** spend >30 min on any single section. 8 sections × 30 min = 4 hours. Tight but feasible.
- **Don't** add new analysis. weekly_summary consolidates; it does not synthesize-anew.
- **Don't** write Appendix D (cumulative reference corrections) from scratch — Day 4 99_summary §11.5 + Day 5 outputs already list the 8 corrections. Copy + verify.

### 4.4 What might surprise

The cumulative W5 picture may *feel* larger than expected. ~50+ working files + ~80+ daily logs across 7 days is a lot. The temptation will be to summarize everything; resist. weekly_summary cites *milestones*, not exhaustive inventory.

If Day 6 weekly_summary draft hits 1500 lines by 16:00, stop and consolidate; do not push to 2500 hoping for completeness. 1500-2000 is the target band.

---

## §5. OAT-2 / OAT-3 Integration Pre-Think — small but binding

These two are the *smallest substantive Day 6 items* (~50 / ~40 lines respectively). Their value is binding CV-1.6 D-CV1.6-O3 readiness ahead of W6 D6-D7 packet finalize.

### 5.1 OAT-2 F bridge PH layer (~50 lines)

**Substance**: F as derived diagnostic via $H_0$ Vietoris-Rips PH on super-level set. This is *not new theory* — it's the *Tool A3 4-tool mapping* per `mathematical_scaffolding_4tools.md` §4 applied to F.

**Cross-reference discipline**: cite `mathematical_scaffolding_4tools.md` §4 (existing canonical-track Commitment 17 candidate) + `sigma_multi_trajectory.md` §3.7 (PH reformulation precedent). Do NOT cite `sigma_rich_VR_phase1.md` (336 lines, post-EOD CV-1.7 parking lot) as canonical anchor.

**BC-1 generic-fail update preserved**: per Day 4 OAT-2 update, BC-1 conjecture (per-formation F ↔ aggregate F lobes bijection) **fails generic** in R23 overlapping regime. Day 6 PH layer addition does NOT change BC-1 status; it provides a *computational handle* on F that respects the R23 generic state caveat.

### 5.2 OAT-3 λ_rep Option 3 contrastive (~40 lines)

**Substance**: explicit CN5 amendment proposal text. λ_rep architectural-layer separate from CN5 single-formation 4-energy independence; bilinear $\langle u^j, u^k \rangle$ ≠ KKT Lagrange (Tool A4 partial fail honestly acknowledged); contrastive comparison to Allen-Cahn N-phase preserved (CN10 not reductive).

**Honest acknowledgment text** (key sentence): "SCC bilinear λ_rep is **not** identical to Allen-Cahn N-phase KKT Lagrange constraint multiplier. The structural correspondence is at the *level of constraint enforcement on simplex* (via different mechanisms); SCC's bilinear is a *4-energy-independent architectural-layer term*, not a Lagrange multiplier."

This is partial-fail-honest. Adding it to canonical (CV-1.6 D-CV1.6-O3) requires Tool A4 PARTIAL FAIL acknowledgment to be **unmoved** — that wording must survive into canonical text.

---

## §6. β-path / γ-path Preliminary Reading Pre-Think

### 6.1 β-path R22 reading — convention identification

`working/SF/symmetry_moduli.md` §3.3 is the source of R22's claim $A_2/A_1 = 4$. Day 6 reading goal is **identification** of which convention R22 uses — not full audit.

The 5 candidates per Day 5 R-1 finding:
- C1 naive integral (gives 2/3 — Cat A verified Day 5; **rejected** for R22).
- C2 normalized eigenmodes (same as C1; **rejected** for R22).
- C3 mass-conservation simplex projection.
- C4 W-potential expansion coefficients.
- C5 (NEW HYPOTHESIS): R22 derivation contains an actual error (4 has no valid convention origin).

Day 6 outputs `01_r22_convention_preliminary.md` (~80-120 lines) listing:
- (a) the actual R22 derivation as-is in §3.3 (transcribed).
- (b) which convention each step uses (if identifiable).
- (c) where the value 4 enters (which step).
- (d) candidate identification: C3 / C4 / C5 / inconclusive.

If C3 or C4: W6 D2 `r22-audit-prover` starts from identified convention; effort drops 1-2 weeks → 3-5 days.
If C5: T-σ-Theorem-4 (ii) statement requires *fundamental* revision and CV-1.6 caveat may need to escalate to Cat C downgrade.
If inconclusive: default first attempt convention C3 for `r22-audit-prover`.

### 6.2 γ-path literature scan — reference anchoring

Σ_m-Hessian convention (centered vs Lagrange) is a *standard mathematical convention question*. Day 6 reading goal is **named literature anchors** for `gamma-path-prover` W6 D1 morning input.

Targets:
- Modica-Mortola (1979, *Acta Metall*) Allen-Cahn / simplex projection.
- Garcke-Nestler-Stoth (1999, *SIAM J. Appl. Math.* 60(1)) multi-phase field model conventions.
- Boyd-Vandenberghe (2004) *Convex Optimization* Ch. 10.4 (simplex-tangent Hessian).
- García Trillos-Murray (2017, *J. Stat. Phys.* 167(3):934-958) regularized empirical risk minimization (per Day 4 8th citation correction).

The output `02_gamma_literature_scan.md` (~30-50 lines) lists 4-6 references with section/page anchors. Not a literature review — just *citable starting points*.

### 6.3 Why preliminary, not full

Both β and γ are W6 D1+ work. Day 6 preliminary reading just *reduces W6 entry cost*. If Day 6 turns into β/γ full audits, that's Day 7-style finalization slip OR Day 4-style scope expansion. Cap each at 60-90 min.

---

## §7. W5 Close Discipline — Day 6 vs Day 7 split

### 7.1 The split

W5 close is **two days**, not one:
- **Day 6 = substance** (weekly_summary substantive draft 80-90%; deferred items executed).
- **Day 7 = ceremony** (weekly_summary finalize; W6_strategic_plan.md authoring; CHANGELOG W5 close entry; final sweep).

Trying to do all of close on Day 6 is the bad failure mode. Trying to do *only* close on Day 6 (no execution) is the other bad failure mode.

### 7.2 Day 7 work cannot be moved to Day 6

- **W6_strategic_plan.md authoring (~400-600 lines)**: requires Day 6 outputs as input (NQ-244 partial state, OAT-2/3 extensions, β/γ preliminary reports). Cannot be authored Day 6.
- **CHANGELOG W5 close entry**: requires weekly_summary final form. Day 6 weekly_summary draft is not yet final.
- **Final retraction sweep**: requires Day 6 outputs as additional retraction sources (potential).

So Day 6 *cannot* steal Day 7 work even if tempted.

### 7.3 Day 6 work cannot be deferred to Day 7

- **NQ-244 launch**: must run overnight Day 6 → Day 7 morning. Day 7 morning launch loses 12 hours of compute.
- **Errata application**: blocks W6 D1 morning if not done; Day 7 application is fine but delays Day 7 finalization tasks.
- **OAT-2/3 extensions**: CV-1.6 D-CV1.6-O3 readiness; W6 D6-D7 packet finalize depends.
- **β/γ preliminary reading**: W6 D1-D2 dispatch entry conditioning; later means W6 D1 reads cold.

So Day 6 cannot defer to Day 7.

The split is binding. Don't cross it.

---

## §8. Day 6 Non-Goals Need to Be Emotionally Enforced

These are not only technical non-goals. They are anti-drift guards.

### 8.1 No paper mode

Even though weekly_summary has narrative prose, it is **internal close**. If Day 6 starts polishing sentences for paper-quality voice, scope slips. weekly_summary uses functional academic prose, not paper-quality prose.

### 8.2 No giant canonical merge

Day 6 canonical edit count = **0**. CV-1.6 release is W6 D7. W5 close is *internal*. CHANGELOG W5 close entry (Day 7) is metadata, not theorem promotion.

### 8.3 No "save the theorem in one day" impulse for T-σ-Theorem-4

γ + β audits are W6 D1+ work. Day 6 preliminary reading is *not* an audit. If Day 6 finds R22 derivation has an obvious error in §3.3, the right action is to *document the observation in `01_*`* and let `r22-audit-prover` confirm at W6 D2 — not to "fix" the theorem today.

### 8.4 No silent post-EOD cluster absorption

CV-1.7 parking lot binding. OAT-2 PH layer must not cite `sigma_rich_VR_phase1.md` as canonical anchor. β preliminary reading can use `nq187b_L_extrapolation.md` and `sigma_theorem4_canonical_revision.md` as *input* (post-EOD but `08_*` already extracted findings) but should not propagate cluster claims into weekly_summary as established theory.

### 8.5 No new Wave 5 dispatch

Day 5 `06_*` §4.5 binding. Defer to W6 D1.

### 8.6 No NQ-244 partial output read

W6 D4 only. Even if curiosity strong, do not read partial output.

### 8.7 No git commit

W5 close at Day 7 EOD. Day 4 last commit `50109a3 0430_done`. Day 6 changes accumulate without commit.

### 8.8 No new working file creation outside named outputs

Errata to `nq187b_L_extrapolation.md` is correction, not new creation. Extensions to `F_Kstep_K_triple.md` / `lambda_rep_ontology.md` are extensions, not new files. Preliminary reports go to `daily/2026-05-02/` (not `working/`). NEW files are `01_*`, `02_*`, `99_summary.md`, `nq244_3d_lsw_t3_15_k10.py`, `weekly_summary.md` — and that's the complete list.

---

## §9. Personal Calibration Note

Day 4 produced the psychological illusion of "almost there"; Day 5 corrected this with retraction inventory. Day 6 carries the calibration:

> "We are not almost done; we are executing the cleanly-bounded items that Day 5 catalogued. The W5 close is two days (Day 6 substance + Day 7 ceremony). W6 D1 is a fresh start with γ + β unconditional dispatches. CV-1.6 release is W6 D7. v2.0 is W11-W12. We are *on track*, not *near complete*."

Day 6 success looks like:
- 3 verifiable artifacts done (errata + NQ-244 + OAT-2 PH) at *acceptable* quality.
- 1 substantive draft (weekly_summary 80-90%).
- 2 preliminary reports (β R22 + γ literature) at *informative* quality.
- 1 EOD summary (Day 6 99_summary).
- 1 weekly storming append.

**8 outputs / 9-11 hours**. None of them are theorem-level new work. All of them are *measured forward execution*. That is the day.

---

## §10. User Directive Acknowledgment

User said (Day 5 close): "철회되는 사항들과 전체를 전부 정리해서 오늘 세션을 마무리하라 내일은 생산적인 계획이 필요함" + "정교하게 weekly에 맞게".

Translation into mental frame:
- **9-item retraction inventory** registered in Day 5 99_summary §13. Carry-forward to weekly_summary §8 (W5 retraction inventory cumulative).
- **"생산적인 계획"** = forward-leaning execution + W5 weekly close substance, NOT extension day. plan.md Block 1+2+4 = execution; Block 3 = weekly substance; Block 5 = close.
- **"정교하게 weekly에 맞게"** = Day 6 plan must respect W5 close discipline split (Day 6 substance + Day 7 ceremony). Both plan.md and pre_brainstorm.md are written at the level of detail of Day 5's plan.md (560 lines) + pre_brainstorm.md (368 lines).

The volume budget exists so that Day 6 can finish its execution lane today instead of pushing to Day 7. But "정교하게" gives quality, not license — reconciliation discipline carry is *still binding*.

---

## §11. Suggested Morning Reading Order

1. `THEORY/logs/daily/2026-05-01/99_summary.md` (Day 5 EOD; §13 retraction inventory; §14 Day 6 plan summary).
2. `THEORY/logs/daily/2026-05-01/09_day6_plan_seed.md` (this plan's seed; same blocks).
3. `THEORY/logs/daily/2026-05-01/08_alpha_path_direct_compute_finding.md` (R-1 finding + errata recommendation §5).
4. `THEORY/logs/daily/2026-05-02/plan.md` (this Day 6 execution contract).
5. `THEORY/logs/daily/2026-05-01/07_w6_plan_preview.md` (W6 D1-D7 skeleton; for Day 7 W6_strategic_plan.md authoring preview).
6. `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (template for Block 3).
7. `THEORY/logs/weekly/2026-04-W5/W5_strategic_plan.md` (W5 strategic plan; entry state for Block 3 §1).
8. `working/SF/nq187b_L_extrapolation.md` (errata target; full read 5 min).
9. `working/SF/symmetry_moduli.md` §3.3 (R22 source for β preliminary reading).
10. `working/MF/F_Kstep_K_triple.md` (OAT-2 extension target).
11. `working/MF/lambda_rep_ontology.md` (OAT-3 extension target).
12. `working/MF/mathematical_scaffolding_4tools.md` §4 + §6.3 (Tool A3 + Tool A4 partial fail; OAT-2/3 cross-reference).

---

## §12. Day 6 Closing Internal Sentence

> "Day 4 was forging; Day 5 was cooling and measuring; Day 6 is **measured forward execution + W5 close substance**; Day 7 is W5 close ceremony. W6 D1 starts from a known position with γ + β unconditional dispatches and CV-1.6 packet 5 + 5 + 3 + 17 classified honestly. We are not racing; we are *delivering on the schedule we already wrote*."

---

**End of pre_brainstorm.md (2026-05-02 W5 Day 6).**
**Day 6 mental frame:** keep the 5 named deferred items moving (errata + NQ-244 + OAT-2 + OAT-3 + weekly_summary draft), pre-condition W6 D1 dispatch via β/γ preliminary reading, do not slip into Day 4 burst or Day 7 finalization, respect W5 close two-day split. The Day 5 reconciliation discipline is *still binding* — what changed is the *posture* (cooling → measured execution), not the *constraints*.
