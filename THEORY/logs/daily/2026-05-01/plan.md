# plan.md — 2026-05-01 (W5 Day 5, RECONCILIATION-FIRST: T-σ-Theorem-4 Audit + CV-1.6 Packet Integration)

**Session type:** W5 Day 5 — *reconciliation and integration day* after W5 Day 4's theory-deepening burst. Day 4 produced a large volume of working artifacts, several CV-1.6 candidate bridges, and one genuinely red critical result around `T-σ-Theorem-4`. Day 5 should integrate the green outputs, isolate the red outputs, and convert ambiguity into a bounded audit path.
**W5 scope:** 2026-04-27 (Mon, Day 1 G0) ~ 2026-05-03 (Sun). 8 goals per `W5_strategic_plan.md`.
**Prerequisite:** Day 4 close 2026-04-30 — `99_summary.md`, `12_wave3_eod_status.md`, `13_wave3_critical_findings.md`, `15_wave4_carry_forward.md`, `TASK_LEDGER.md`, OAT batch logs, and persisted Wave 3 working files.
**Session working directory:** `THEORY/logs/daily/2026-05-01/`.
**Weekly buffer target:** `THEORY/logs/weekly/2026-04-W5/weekly_draft_storming.md` (05-01 entry append, latest-first).
**Strategic plan:** `THEORY/logs/weekly/2026-04-W5/W5_strategic_plan.md`.
**Day 4 references:** `THEORY/logs/daily/2026-04-30/99_summary.md`, `12_wave3_eod_status.md`, `13_wave3_critical_findings.md`, `15_wave4_carry_forward.md`.
**User calibration:** "Paper 만드는 단계는 아직 이르다" — Day 5 remains theory-first; no paper drafting blocks.

---

## §1. Day 5 Mission Statement

> **"Day 4의 대량 산출물을 Day 5에서 정리한다: persisted artifacts를 검증하고, `T-σ-Theorem-4`의 붉은 경고를 별도의 audit lane으로 격리하며, CV-1.6 packet에서 실제로 READY인 것과 PARTIAL인 것을 다시 구분한다. Operationally는 Theorem 4.6.1 label correction과 NQ-244 background launch까지 마감한다."**

Day 4 was an **expansion + deepening day**. Day 5 should be a **reconciliation day**. The biggest risk is to treat all Day 4 output as equally mature. It is not. Some results are ready for packet integration; others are evidence of unresolved fracture. Day 5 succeeds if that distinction becomes cleaner.

---

## §2. Day 5 Targets vs Day 4 (Calibration)

| 항목 | Day 4 (theory-deepening burst) | **Day 5 (reconciliation-first)** |
|------|-------------------------------|----------------------------------|
| Main mode | expansion + parallel research lanes | **verification + audit + integration** |
| New working files | 20+ substantive files | **3-5 focused files** |
| Canonical pressure | CV-1.5.1 promotion + CV-1.6 candidate inflation | **CV-1.6 status recalibration** |
| Highest-risk item | implicit ontological overclaim | **T-σ-Theorem-4 discrepancy reconciliation** |
| Numerical emphasis | broad batch + teammate runs | **1 background launch (NQ-244) + optional small checks** |
| Deliverable style | many parallel outputs | **few, explicit decision documents** |
| Non-goal risk | paper drift / over-promotion | **must be explicitly blocked** |

---

## §3. 30-Minute Granular Schedule

### Block 0 — Morning State Reload (09:00-09:30, 30min)

#### 09:00-09:15: Read Day 4 close as a single state packet

**Action**:
- Read `99_summary.md` §7-§8 + §13-§15.
- Read `12_wave3_eod_status.md`.
- Read `13_wave3_critical_findings.md`.
- Read `15_wave4_carry_forward.md`.

**Goal**: form one coherent Day 5 picture before touching any new lane.

**Success metric**: one-sentence summary of Day 4 state produced in Day 5 notes:
- green: what is usable now
- yellow: what is only partially usable
- red: what must be audited before promotion

#### 09:15-09:30: Sync active ledger + file expectations

**Action**:
- Compare `TASK_LEDGER.md` active items with actual persisted files.
- Prepare a Day 5 checklist of:
  - teammate files to verify
  - tests to rerun
  - working files requiring critic re-read

**Output**: `01_morning_state_reload.md` (~80-120 lines).

---

### Block 1 — Verification + Persistence Audit (09:30-10:30, 1h)

#### 09:30-10:00: File persistence audit

**Action**:
- `ls` + `wc -l` on key Wave 3/Day 4 outputs.
- Confirm presence of:
  - `working/SF/sigma_theorem4_higher_order.md`
  - `working/SF/sigma_theorem4_canonical_revision.md`
  - `working/SF/theorem_2g_schramm_restatement.md`
  - `working/MF/k_selection_mechanism.md`
  - `working/MF/shared_pool_canonical_proposal.md`
  - `working/MF/lambda_rep_ontology.md`
  - `CODE/scc/sigma_rich.py`
  - `CODE/scripts/results/sigma_theorem4_scaling.json`

**Success metric**: no phantom deliverables; missing file list empty.

#### 10:00-10:30: Test refresh

**Action**:
- Rerun the Wave 3 code anchors first:
  - `CODE/tests/test_sigma_rich.py`
  - `CODE/tests/test_sigma_rich_integration.py`
  - `CODE/tests/test_aut_g_stabilizer.py`
- If budget permits and nothing strange appears, optional full `pytest` run later in Block 5.

**Output**: `02_verification_audit.md` (~80-120 lines).

**Success metric**: code anchor tests green; recorded baseline for Day 5.

---

### Block 2 — T-σ-Theorem-4 Red Lane (10:30-12:30, 2h)

#### 10:30-11:15: Read the two red-source packets carefully

**Action**:
- Read `working/SF/sigma_theorem4_higher_order.md` revised form.
- Read `working/SF/sigma_theorem4_canonical_revision.md`.
- Re-read `13_wave3_critical_findings.md` §1 + §10.

**Question**:
What exactly is broken:
1. the finite-L numerical claim,
2. the cubic-equivariant ratio derivation,
3. the Σ_m-Hessian convention map,
or some mixture?

#### 11:15-12:00: Separate the three audit paths cleanly

Use the Day 4 naming:
- **γ path**: Σ_m-Hessian convention audit
- **β path**: R22 `symmetry_moduli.md` cubic-equivariant derivation audit
- **α path**: finite-L / continuum extrapolation audit

**Required output**:
- which path is the true Day 5 priority
- which path can be deferred to W6
- which path is merely confirmatory rather than causal

#### 12:00-12:30: Produce reconciliation note

**Output**: `03_t_sigma_theorem4_reconciliation.md` (~180-250 lines).

**This file must contain**:
1. precise statement of the discrepancy (`2/3` vs `4` vs implied `8`)
2. which theorem text remains safe today
3. what exact caveat CV-1.6 should carry
4. whether Day 5 can promote anything here at all (default expectation: no)

**Success metric**: `T-σ-Theorem-4` is no longer "confusing"; it is "clearly unresolved in a specific way."

---

### Block 3 — CV-1.6 Packet Recalibration (13:30-15:30, 2h)

#### 13:30-14:15: Collect OAT / Wave 3 packet pieces

**Action**:
- Read:
  - `working/CV-1.6_packet_crosswalk.md`
  - `working/MF/shared_pool_canonical_proposal.md`
  - `working/MF/F_Kstep_K_triple.md`
  - `working/MF/lambda_rep_ontology.md`
  - `working/MF/cobelonging_vs_sigmaD.md`
  - `working/MF/pre_objective_K_field_tension.md`
- Compare against `open_problems.md` OP-0009 sub-item table.

#### 14:15-15:00: Reclassify READY / PARTIAL / DEFER

**Key rule**:
Do not inherit Day 4 optimism automatically.

Minimum categories:
- **READY for CV-1.6 packet inclusion**
- **PARTIAL but includable as bounded caveated item**
- **DEFER to v2.0 / W6+**

Expected conservative baseline:
- O5 Commitment 17 scaffolding: READY
- Schramm restatement / CN15 / N-1 Kramers: READY or near-ready
- OP-0009 full resolution: NOT READY
- `T-σ-Theorem-4` re-promotion: NOT READY

#### 15:00-15:30: Produce packet note

**Output**: `04_cv16_packet_recalibration.md` (~180-240 lines).

**Success metric**: CV-1.6 packet shape is smaller but cleaner than Day 4's inflated picture.

---

### Block 4 — Focused Operational Fixes (15:30-17:00, 1.5h)

#### 15:30-16:00: Theorem 4.6.1 / dynamic σ label hygiene

**Action**:
- Inspect `working/MF/sigma_multi_trajectory.md`.
- Apply the promised label correction for Theorem 4.6.1 / Lemma 4.2(c)-adjacent language:
  - do not leave "Cat B sketch" wording where the actual status is "conjectured / Cat C"
  - ensure dynamic σ inheritance non-determinism is not oversold

**Success metric**: Day 4's own self-critique is reflected in file labels.

#### 16:00-16:30: NQ-244 background launch

**Action**:
- Launch 3D LSW background run if the environment is ready.
- Keep this as a background numerical seed, not the main Day 5 lane.

**Output**: `05_nq244_launch_note.md` (~60-100 lines), even if only launch metadata + parameters + expected runtime.

#### 16:30-17:00: Optional micro-dispatch or queue cleanup

Only if Blocks 1-4 close on time:
- dispatch `oat5-c_t-prover`, or
- prep a Day 6 note for `NQ-187b` / `symmetry_moduli` deeper audit,
- but do **not** open a new major branch.

---

### Block 5 — Day 5 Close (17:00-18:00, 1h)

#### 17:00-17:30: Day 5 summary

**Action**: write `99_summary.md`.

Required sections:
- what was verified
- what was downgraded or caveated
- what remains red
- what is genuinely ready for CV-1.6

#### 17:30-18:00: Weekly draft append

Append 05-01 entry to `weekly_draft_storming.md` with explicit emphasis:
- Day 5 was not a growth day
- it was a calibration / reconciliation day
- this was necessary after Day 4 burst

**Success metric**: Day 6 starts from a cleaned state, not a swollen state.

---

## §4. Day 5 Output Inventory (target 5-6 files)

| 파일 | 목적 | 예상 분량 |
|------|------|-----------|
| `01_morning_state_reload.md` | Day 4 close → Day 5 state packet | 80-120 lines |
| `02_verification_audit.md` | persistence + tests | 80-120 lines |
| `03_t_sigma_theorem4_reconciliation.md` | red-lane audit note | 180-250 lines |
| `04_cv16_packet_recalibration.md` | packet READY/PARTIAL/DEFER map | 180-240 lines |
| `05_nq244_launch_note.md` | background numerical launch note | 60-100 lines |
| `99_summary.md` | Day 5 close | 150-220 lines |

Optional:
- `weekly_draft_storming.md` 05-01 entry append
- one small label-fix diff in `working/MF/sigma_multi_trajectory.md`

---

## §5. Explicit Non-Goals

- **No paper drafting or paper §4 polishing.**
- No broad canonical merge of Day 4 outputs as a single batch.
- No attempt to "save" `T-σ-Theorem-4` in one rushed Day 5 pass.
- No new giant theory branch unless a red-lane reconciliation file explicitly justifies it.
- No git commit unless the user explicitly asks.

---

## §6. Risks and Mitigations

### Risk-1: Day 4 optimism contaminates Day 5 classification

**Likelihood:** High.  
**Mitigation:** force READY / PARTIAL / DEFER triage in Block 3.

### Risk-2: `T-σ-Theorem-4` audit expands into full week-long work

**Likelihood:** High.  
**Mitigation:** Day 5 output is a reconciliation note, not a full repair.

### Risk-3: NQ-244 launch hijacks the session

**Likelihood:** Medium.  
**Mitigation:** background only; no Day 5 interpretation beyond launch metadata.

### Risk-4: OP-0009 is accidentally over-claimed

**Likelihood:** High.  
**Mitigation:** use the exact Day 4 critic-calibrated wording: `1/7 resolved + 6/7 partially addressed`.

---

## §7. Suggested Reading Order at Session Start

1. `THEORY/logs/daily/2026-04-30/15_wave4_carry_forward.md`
2. `THEORY/logs/daily/2026-04-30/13_wave3_critical_findings.md`
3. `TASK_LEDGER.md`
4. `THEORY/working/CV-1.6_packet_crosswalk.md`
5. `THEORY/working/MF/sigma_multi_trajectory.md`
6. `THEORY/canonical/open_problems.md` (OP-0008, OP-0009)

---

**End of plan.md.**
**Day 5 posture:** integrate the stable, isolate the unstable, do not confuse output volume with theorem maturity.
