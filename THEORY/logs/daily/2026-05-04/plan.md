# plan.md — 2026-05-04 (W6 Day 1, Triple Parallel Thread Launch)

**Title:** 2026-05-04 Research Plan — W6 Day 1 Triple Parallel Thread Launch (G1 + G2 + G3 + G7).
**Session type:** W6 Day 1 — *AGGRESSIVE marathon launch* (mirrors W5 Day 1 G0 σ-merge + G1/G2 setup pattern). Triple-thread parallel start per W6 strategic plan §0.4 Decision 1 Option α.
**W6 scope:** 2026-05-04 (Mon, Day 1) ~ 2026-05-10 (Sun, Day 7 W6 close).
**Session working directory:** `THEORY/logs/daily/2026-05-04/`.
**Weekly buffer target:** `THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md` (latest-first 05-04 entry append; create if missing).
**W5 Day 7 EOD references:** `THEORY/logs/daily/2026-05-03/02_development.md` (L1-M working draft, audit input); `THEORY/logs/daily/2026-05-03/03_integration_and_new_open.md` §4 (NQ-L1M-1..8); `THEORY/logs/weekly/2026-04-W5/weekly_summary.md` §7 (W6 carry-forward).
**Active runtime:** triple-thread parallel — 2 external-audit teammate dispatches (G1, G3) + 1 single-target completion (G2) + 1 PARTIAL→READY integration (G7) + 1 background numerical launch (NQ-187b).
**User calibration:** W6 strategic plan §0.4 Decision 1 Option α (parallel) recommended; Day 3 EOD critical decision artifact (G1 verdict + G3 시나리오) 사용자 검토 필수.

---

## §1. Starting State

### §1.1 W5 close inventory (2026-05-03 EOD)

- **Canonical version current:** **CV-1.5.2** (2026-05-02). T-L1-F (Hard-Bar / Active-Count Bridge under L1-J Regime) Cat A conditional canonical-merged.
- **Counts:** 46A / 5B / 5C / 5R / 61 claims / 75% proved.
- **Tests:** 196/196 passing.
- **L1-M working draft (Day 7):** in `THEORY/logs/daily/2026-05-03/02_development.md` (~542 lines). Status: Cat-B sketched; CV-1.6 promotion target via L1-M-AUDIT.
- **3 bookkeeping refinements flagged in `02_development.md` §5.7**: R-1 (bottleneck-stability factor-2 sharpness in §5.4), R-2 (Type-B bound LG-7 reuse explicit reproof in §5.5), R-3 (terminal-death convention Type-N consistency in §5.4).

### §1.2 W6 carry-forward (P0 from W5 weekly_summary §7.1)

- **G1 L1-M-AUDIT** (~2-3 days, Day 1-3): external audit + repair cycle on L1-M working draft.
- **G2 NQ-L1M-2 CSEH 2007 factor-2 sharpness** (~1 day, Day 1 single target): Cat A absolute target.
- **G3 γ-path Σ_m-Hessian convention audit** (~3-5 days, Day 1-3): T-σ-Theorem-4 Cat B → Cat A re-promotion attempt.

W5 P1:
- **G7 OAT-2/3 short integration** (~1-2 days, Day 1-2): F bridge + λ_rep PARTIAL → READY upgrade.

### §1.3 Open Problems unchanged (W6 D1 entry)

- OP-0005 (K-Selection): 🟠 HIGH; working-level partial only.
- OP-0008 (σ^A K-jump non-determinism): 🟠 HIGH; W7+ Path B σ_rich entry.
- OP-0009 (Multi-Formation Ontological Foundations 7-sub-items): 🟠 HIGH; 1/7 RESOLVED + 6/7 PARTIALLY.
- OP-0003 (MO-1) re-activation rider: not triggered (W6 multi-formation Morse work 없음).
- OP-0001 (F-1) / OP-0002 (M-1): RESOLVED / LAYER-CLARIFIED at W4; unchanged.

---

## §2. Main Objective

**Day 1 Goal**: Launch **triple parallel thread** (G1 + G3 + G7) + **complete G2 single target** + **launch NQ-187b background numerical**.

**End-of-Day target**:
- G2: ✅ COMPLETE (CSEH factor sharpness analysis Cat A absolute, Day 1 single target).
- G1: ✅ DISPATCHED (audit input package prepared + teammate `l1m-audit-prover` launched fire-and-forget; verdict expected Day 2-3).
- G3: ✅ DISPATCHED (audit input package prepared + teammate `gamma-path-prover` launched fire-and-forget; verdict expected Day 2-3).
- G7: ⏳ PARTIAL (OAT-2 PH layer scope drafted; complete Day 2).
- NQ-187b: ✅ BACKGROUND LAUNCHED (script `nq187b_a2_a1_extrapolation.py` running; ~10-30 hours estimated).

**Day 1 success criterion**: 4 substantive thread starts + 1 complete + 1 background launch = **5 distinct deliverables** before EOD.

---

## §3. Key Inputs

### §3.1 G1 L1-M-AUDIT input package

- `THEORY/logs/daily/2026-05-03/02_development.md` (~542 lines) — substantive content (Definition L-M-D1 Φ_res, Lemma L-M-1 envelope-pure, Lemma L-M-2 edge-band emptiness sketched, Theorem L-M, 3 per-family corollaries, 4 counterexample attempts).
- `THEORY/logs/daily/2026-05-03/01_exploration.md` (~290 lines) — approach rationale (A1 primary + A4 enhancement; A2/A3 preserved; A5/A6/A7 excluded with rationale).
- `THEORY/logs/daily/2026-05-03/03_integration_and_new_open.md` (~310 lines) — integration with canonical + OP non-impact audit + 8 new NQs.
- `THEORY/canonical/canonical.md` §13 T-L1-F entry (line 1462) — anchor.
- `THEORY/working/MF/ksoft_kact_bridge_lemma.md` (WQ-2 bridge lemma, predecessor).
- `THEORY/working/MF/wq_lat1b_phi_envelope_refinement_results.md` (empirical anchor for envelope sub-classes).
- `THEORY/working/MF/ksoft_kact_bridge_proof_status.md` (C-09/C-10/C-11 lemma candidate framework).

### §3.2 G2 NQ-L1M-2 CSEH factor sharpness inputs

- CSEH 2007: Cohen-Steiner, Edelsbrunner, Harer, *Stability of persistence diagrams*, Theorem 4.2 (already cited in `working/E/soft_K_definition.md` §2.1).
- L-M-2 §5.4 statement: $|\ell_i - \ell_i^{(u^{(j)})}| \le 2 \cdot \rho_{\mathrm{pert}}/2 = \rho_{\mathrm{pert}}$.
- T-L1-F P0 (terminal-death $H_0$ superlevel persistence convention) — for Type-D (dominant) bars.
- Type-D (terminal survivors) vs Type-N (non-dominant, possibly finite-death) vs Type-B (background) classification from `02_development.md` §5.2.

### §3.3 G3 γ-path audit input package

- `THEORY/logs/daily/2026-04-30/13_wave3_critical_findings.md` §1.4 — NQ-187 RED finding original.
- `THEORY/logs/daily/2026-05-01/03_t_sigma_theorem4_reconciliation.md` — γ/β/α 3-path framework.
- `THEORY/working/SF/symmetry_moduli.md` §3.3 — R22 cubic coefficient analysis (Cat A reference).
- `THEORY/canonical/canonical.md` §13 T-σ-Theorem-4 entry — current Cat B retroactive status.
- W4 04-22 SF Round 4 documents (`logs/daily/2026-04-22/04..07_deepening_round*.md`) — original $A_2/A_1 \in \{2, 4\}$ claim source.
- `THEORY/logs/daily/2026-04-30/nq187b_L_extrapolation.md` (post-EOD, 422 lines) — finite-L extrapolation.

### §3.4 G7 OAT-2/3 inputs

- OAT-2: `THEORY/working/MF/F_Kstep_K_triple.md` (359 lines, OP-0009-F).
- OAT-3: `THEORY/working/MF/lambda_rep_ontology.md` (242 lines, OP-0009-λ).

### §3.5 NQ-187b numerical script inputs

- W5 Day 5 §3 prep: `CODE/scripts/nq187b_a2_a1_extrapolation.py` (NEW W6 D1 to be written).
- L1-I FEASIBLE_WITH_BUDGET configurations from `working/MF/kbar_kact_bridge_L1I_constants_feasibility.md`.
- $D_4$ free-BC L sweep target: L ∈ {20, 24, 28, 32, 36, 40} (vs W5 Day 4-5 only L≤16).

---

## §4. Work Packages (5 Blocks)

### Block 1 — pre-brainstorm + plan finalize (09:00-11:00)

- **Output 1**: `pre_brainstorm.md` (Day 1) — looser conceptual frame:
  - G1 audit input package gathering 검토 (which files are load-bearing for L-M-2 verification).
  - G3 γ-path approach review (3 conventions: centered Hessian / Lagrange-projected / reduced on Σ_m).
  - G7 OAT-2/3 PH layer scope (50 lines target; what specific PH layer additions).
  - G2 NQ-L1M-2 mathematical depth preview (factor-2 → factor-1 sharpening under terminal-death).
- **Output 2**: this `plan.md` (Day 1) — Block 2-5 schedule.

**Estimated time**: ~2 hours.

### Block 2 — G2 NQ-L1M-2 single-target completion (11:00-13:00)

**Mathematical depth**:
- CSEH 2007 Theorem 4.2: $W_\infty(\mathrm{Dgm}(f), \mathrm{Dgm}(g)) \le \|f - g\|_\infty$.
- Standard analysis: bar $[d_i, b_i]$ → $[d_i', b_i']$ under perturbation $\delta = W_\infty$. $|b_i - b_i'| \le \delta$ + $|d_i - d_i'| \le \delta$ → $|\ell_i - \ell_i'| \le 2\delta$.
- **Sharpening under terminal-death convention** (T-L1-F P0): $d_i = d_i' = 0$ for terminal-death survivors → $|d_i - d_i'| = 0$ → $|\ell_i - \ell_i'| = |b_i - b_i'| \le \delta$. **Factor-2 → factor-1**.

**Per-bar-type analysis**:
- **Type-D (dominant terminal survivors)**: factor-1 (sharpening applicable).
- **Type-N (non-dominant)**: depends on whether bar is terminal (survivor) or finite-death (merged). per-bar 분석 필요.
- **Type-B (background)**: typically terminal under T-L1-F P0; factor-1 likely.

**Output**: `THEORY/working/MF/cseh_factor_sharpness_analysis.md` (~150-250 lines).
- §1: Statement (revised factor for each bar type).
- §2: CSEH 2007 + terminal-death derivation.
- §3: Per-bar-type analysis + table.
- §4: Implication for L-M-2 §5.4 — new $\tau_*$ expression $\tau_* = \min(5\rho_{\mathrm{pert}}/2, \rho_{\mathrm{res}}, r_{\mathrm{birth}})$ (vs original $\min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}})$ — **25% expansion**).
- §5: Implication for L-M Theorem — new sub-class bounds (sharpened by factor 2).
- §6: Cat classification: **Cat A absolute** (CSEH 2007 + terminal-death convention 직접 분석).

**Estimated time**: ~2 hours.

### Block 3 — G1 L1-M-AUDIT dispatch (Thread 1) (14:00-17:00)

**Step 1 (14:00-15:30)**: L1-M audit input package 준비
- Bundle 7 input files (§3.1).
- Audit prompt 작성 (per W6 strategic plan §4.1.3 audit dispatch protocol):
  - "Audit L-M working draft (Day 7 02_development.md) for Cat A conditional promotion under (P0)–(P11) + Φ_res + τ < τ_*. 3 bookkeeping refinements (R-1 bottleneck-stability factor / R-2 LG-7 reuse / R-3 terminal-death Type-N consistency) flagged in §5.7. Verdict: PASS / REPAIR-NEEDED / FAIL. Per-refinement verdict + new findings."

**Step 2 (15:30-17:00)**: Teammate dispatch
- **Teammate**: `l1m-audit-prover` (general-purpose subagent, audit prompt with structural completeness focus).
- **Mode**: fire-and-forget background dispatch.
- **Expected verdict timing**: Day 2 morning ~ Day 3 morning.
- **Output 1 (Day 1 EOD)**: `THEORY/logs/daily/2026-05-04/01_l1m_audit_dispatch.md` (~100-150 lines) — dispatch record + audit prompt + input package list + expected output schema.

**Estimated time**: ~3 hours.

### Block 4 — G3 γ-path dispatch (Thread 2) + NQ-187b numerical launch (17:00-20:00)

**Step 1 (17:00-18:00)**: γ-path audit input package 준비
- Bundle 6 input files (§3.3).
- Audit prompt:
  - "Audit T-σ-Theorem-4 Cat B retroactive status (CV-1.5.1 Day 4) for Cat A re-promotion attempt. 3-way A_2/A_1 discrepancy (2/3 vs 4 vs 8) cleanly bounded into γ/β/α paths. **γ-path scope: Σ_m-Hessian convention audit** — centered (H_c = ∇²E - μI), Lagrange-projected (H_L = P^⊥ ∇²E P^⊥), reduced on Σ_m (H_r). Specify which convention A_2/A_1 ratio belongs to + verdict on 3 conventions reconciliation."
- **Verdict scenarios** (per W6 strategic plan §4.3.4):
  - 시나리오 A: $A_2/A_1$ resolves to single value → T-σ-Theorem-4 Cat A re-promotion candidate.
  - 시나리오 B: γ verdict inconclusive → β-path R22 audit conditional dispatch (W6 D4-W7 spillover).
  - 시나리오 C: deeper structural error → T-σ-Theorem-4 retract or major restatement (paradigm-shift candidate).

**Step 2 (18:00-19:00)**: Teammate dispatch
- **Teammate**: `gamma-path-prover` (general-purpose subagent, audit + structural analysis prompt).
- **Mode**: fire-and-forget background dispatch.
- **Expected verdict timing**: Day 2 morning ~ Day 3 EOD.
- **Output 2 (Day 1 EOD)**: `THEORY/logs/daily/2026-05-04/02_gamma_path_dispatch.md` (~100-150 lines) — dispatch record + audit prompt + input package list + 3-scenario decision tree.

**Step 3 (19:00-20:00)**: NQ-187b numerical script + background launch
- **Script**: `CODE/scripts/nq187b_a2_a1_extrapolation.py` (NEW W6 D1).
  - Setup: $D_4$ free-BC, c=0.5, β=30, $A_2/A_1$ measurement at L ∈ {20, 24, 28, 32, 36, 40}.
  - 5 seeds per L → 30 minimizers total.
  - Output: $A_2/A_1(L)$ table + linear/inverse-L extrapolation to continuum L → ∞.
  - Estimated runtime: ~10-30 hours (size depends on convergence iters).
- **Background launch**: `nohup python3 scripts/nq187b_a2_a1_extrapolation.py > nq187b.log 2>&1 &`.
- **Output 3 (Day 1 EOD)**: `THEORY/logs/daily/2026-05-04/03_nq187b_numerical_launch.md` (~80-120 lines) — script doc + launch record + expected output schema.

**Estimated time**: ~3 hours.

### Block 5 — G7 OAT-2/3 partial start + Day 1 99_summary (20:00-21:00)

**Step 1 (20:00-20:30)**: G7 OAT-2 PH layer scope
- `THEORY/working/MF/F_Kstep_K_triple.md` (359 lines, OP-0009-F)에 PH layer 추가 *scope* 작성 (실제 추가는 Day 2):
  - Current 4-quantity bridge: $\mathcal F$ / $K_{\mathrm{step}}$ / $K_{\mathrm{act}}$ / $K_{\mathrm{field}}$.
  - PH layer 추가: $K_{\mathrm{bar}}^{\ell_{\min}}(U)$ + L-M $K_{\mathrm{soft}}^\phi(U)$ → **6-quantity bridge**.
  - Section 추가 위치: §4 또는 §5 (existing 4-quantity 다음).
  - 예상 ~50 lines.
- **Output 4 (Day 1 EOD)**: `THEORY/logs/daily/2026-05-04/04_oat2_ph_layer_scope.md` (~50-100 lines) — Day 2 morning 작업 prep.

**Step 2 (20:30-21:00)**: Day 1 99_summary
- Block 1-5 산출 정리.
- Day 2 priority adjustment.
- Hard constraint verification.
- weekly_draft_storming.md 04-W5 → 05-W1 transition 처리 (Day 1 entry append).
- **Output 5 (Day 1 EOD)**: `THEORY/logs/daily/2026-05-04/99_summary.md`.

**Estimated time**: ~1 hour.

---

## §5. Success Criteria

Day 1 is successful if:

1. **G2 ✅ COMPLETE**: `cseh_factor_sharpness_analysis.md` produced; new $\tau_*$ expression derived; Cat A absolute classification.
2. **G1 ✅ DISPATCHED**: `l1m-audit-prover` teammate launched fire-and-forget; dispatch record file produced.
3. **G3 ✅ DISPATCHED**: `gamma-path-prover` teammate launched fire-and-forget; dispatch record file produced.
4. **G7 ⏳ PARTIAL**: OAT-2 PH layer scope drafted; Day 2 complete path 명료.
5. **NQ-187b ✅ BACKGROUND LAUNCHED**: script `nq187b_a2_a1_extrapolation.py` running; launch record produced.
6. **5 distinct daily files produced** + Day 1 99_summary.
7. **No canonical edits applied** (per W6 plan §13.4 hard constraint; G4 release Day 7).
8. **No silent OP resolution** (per W6 plan §13.4 hard constraint).
9. **Tests still 196/196 passing** (no scc/ edits expected).

---

## §6. Risk Register

- **Risk D1-1 — Background teammate dispatch overhead**: G1 + G3 audit dispatch가 Day 1 evening에 launch되어 verdict는 Day 2-3 도착. Day 1 EOD에 verdict 미도착이 정상. **Mitigation**: 두 dispatch 모두 fire-and-forget; Day 1 99_summary는 dispatch record만 기록.
- **Risk D1-2 — NQ-187b script 작성 시 scc/ 의존성 break**: $D_4$ free-BC L=20-40 sweep에 새로운 graph constructor 또는 minimizer init mode 필요 가능. **Mitigation**: 기존 `scc/graph.py` GraphState constructors 사용; 새 mode 필요 시 별도 standalone helper에 격리 (scc/ unmodified).
- **Risk D1-3 — G2 mathematical depth가 expected보다 깊음**: CSEH factor sharpness가 Type-N bars의 mixed terminal/finite-death case에서 생각보다 복잡 → Block 2 ~2시간 over. **Mitigation**: Block 2를 Day 1 morning Block 1과 swap 가능 (Block 2가 Day 1 single most important). Block 5를 Day 2 morning으로 이동.
- **Risk D1-4 — Pre-brainstorm corrections이 G1/G3/G7 input package 수정 강제**: 평소 wording-level corrections (W5 Day 1 패턴)이 substantive package change 강제 가능. **Mitigation**: pre-brainstorm을 Block 1에서 마무리; Block 3-4 dispatch는 corrections 적용 후.
- **Risk D1-5 — Triple-thread coordination이 single-session에서 무리**: G1 + G3 + G7 + G2 4-thread를 single 세션에 처리 시 cognitive load. **Mitigation**: G2 single-target은 ~2시간 budget; G1 + G3 dispatch는 input package + prompt 작성으로 한정 (verdict 처리는 Day 2-3); G7은 partial scope only.

---

## §7. Expected Output Files

**Daily files (5 + 99 = 6)**:

- `THEORY/logs/daily/2026-05-04/pre_brainstorm.md` — Day 1 looser conceptual frame.
- `THEORY/logs/daily/2026-05-04/plan.md` — this file.
- `THEORY/logs/daily/2026-05-04/01_l1m_audit_dispatch.md` — G1 dispatch record (~100-150 lines).
- `THEORY/logs/daily/2026-05-04/02_gamma_path_dispatch.md` — G3 dispatch record (~100-150 lines).
- `THEORY/logs/daily/2026-05-04/03_nq187b_numerical_launch.md` — NQ-187b script doc + launch record (~80-120 lines).
- `THEORY/logs/daily/2026-05-04/04_oat2_ph_layer_scope.md` — G7 Day 2 morning prep (~50-100 lines).
- `THEORY/logs/daily/2026-05-04/99_summary.md` — Day 1 EOD reflection.

**Working files (1 new)**:

- `THEORY/working/MF/cseh_factor_sharpness_analysis.md` — G2 deliverable (~150-250 lines).

**CODE files (1 new)**:

- `CODE/scripts/nq187b_a2_a1_extrapolation.py` — NQ-187b numerical script (~200-350 lines).

**Background processes (1 launched)**:

- `nq187b.log` — NQ-187b background run output (~10-30 hours expected).

**Weekly file (1 modified)**:

- `THEORY/logs/weekly/2026-05-W1/weekly_draft_storming.md` — Day 1 entry append (create file if missing).

**Total Day 1 output**: 6 daily files + 1 working file + 1 CODE script + 1 background process + 1 weekly entry = **9 distinct artifacts** (excluding the background log file which builds passively).

---

## §8. End-of-Day Target for 2026-05-04

By the end of 2026-05-04, the goal is to have **W6 triple parallel thread launched + G2 single target complete**. The state at EOD should:

- Confirm G2 NQ-L1M-2 Cat A absolute (CSEH factor sharpness) → L-M-2 §5.4의 새 $\tau_*$ expression이 W6 G1 audit input에 반영 가능.
- Confirm G1 + G3 audit dispatches launched fire-and-forget; Day 2-3 verdict 처리 path 명료.
- Confirm G7 OAT-2 PH layer scope drafted; Day 2 morning 작업 entry 가능.
- Confirm NQ-187b background numerical launched; Day 5 EOD analysis 가능 (or earlier if convergence faster than expected).
- Confirm 196/196 tests passing (no scc/ edits).
- Confirm canonical 직접 수정 0; silent OP resolution 0; CN10/CN6/CN15 violation 0.

Day 1 의 substantive Day 1 contribution은 **G2 single target complete (CSEH factor sharpness Cat A)** + **3 background threads launched (G1, G3, NQ-187b)**. Day 2-3 는 verdict aggregation + G7 complete. Day 4-5 는 G6 + G8. Day 6-7 는 G4 release + G5 dispatch.

---

**Source files for Day 1:**

- W5 close: `THEORY/logs/weekly/2026-04-W5/weekly_summary.md`
- W6 strategic plan: `THEORY/logs/weekly/2026-05-W1/W6_strategic_plan.md` (especially §6.1 Day 1 Block 1-5)
- L1-M working draft: `THEORY/logs/daily/2026-05-03/02_development.md`
- L1-M exploration: `THEORY/logs/daily/2026-05-03/01_exploration.md`
- L1-M integration: `THEORY/logs/daily/2026-05-03/03_integration_and_new_open.md`
- T-L1-F canonical: `THEORY/canonical/canonical.md` §13 (line 1462)
- T-σ-Theorem-4 canonical: `THEORY/canonical/canonical.md` §13 + `theorem_status.md` CV-1.5.1 entry
- γ/β/α framework: `THEORY/logs/daily/2026-05-01/03_t_sigma_theorem4_reconciliation.md`
- NQ-187 RED finding: `THEORY/logs/daily/2026-04-30/13_wave3_critical_findings.md` §1.4
- OAT-2 source: `THEORY/working/MF/F_Kstep_K_triple.md`
- OAT-3 source: `THEORY/working/MF/lambda_rep_ontology.md`
- CSEH 2007 reference: `THEORY/working/E/soft_K_definition.md` §2.1
