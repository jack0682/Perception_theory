# plan.md — 2026-04-28 (W5 Day 2, MODERATE: Verdict Closure + G3 Opening + Commitment 14 Decision)

**Session type:** W5 Day 2 — *verdict closure + transition day*. G1 (NQ-173 V5b-F numerical 완수 + verdict) + G2 (NQ-174 ζ_*(graph) precise + canonical proposal) + G3 (multi-formation σ Phase 5 *initiation*) + Commitment 14 (O5')/(O7) user decision.
**W5 scope:** 2026-04-27 (Mon, Day 1 G0 done) ~ 2026-05-03 (Sun). 8 goals per `W5_strategic_plan.md`.
**Prerequisite:** W5 Day 1 close 2026-04-27 — canonical v1.5 release-ready post-Round-1 + Round-2 corrections; G1 + G2 scripts ready; 2 Commitment-level changes deferred to user agenda.
**Session working directory:** `THEORY/logs/daily/2026-04-28/`.
**Weekly buffer target:** `logs/weekly/2026-04-W5/weekly_draft_storming.md` (04-28 entry append, latest-first).
**Strategic plan:** `logs/weekly/2026-04-W5/W5_strategic_plan.md` (8-goal blueprint).
**Day 1 reference:** `THEORY/logs/daily/2026-04-27/100_day2_carry.md` (carry-forward starter).

---

## §1. Day 2 Mission Statement

**"Day 1 G0 완수 (canonical v1.5 release-ready) 이후 G1 + G2 verdict를 *AM에 마감*하고 G3 multi-formation σ Phase 5를 *PM에 substantively 시작*. Commitment 14 (O5')/(O7) user decision agenda 처리."**

Day 1이 *AGGRESSIVE marathon launch* (G0 + G1 + G2 setup, ~12-14h)였다면, Day 2는 *MODERATE verdict-and-opening day* (~9h). 이것은 W4 → W5 transition의 자연스런 패턴: 선포 → 검증 → 확장.

---

## §2. Day 2 Targets vs Day 1 (Calibration)

| 항목 | Day 1 (AGGRESSIVE) | **Day 2 (MODERATE)** |
|------|-------------------|---------------------|
| Total time | 12-14h | **8-10h** |
| canonical edits | 5 §13 entries + 4 counts (~150 lines) | 1-2 entries (V5b-F update) + Commitment 14 (O5'/O7) if approved (~100-150 lines) |
| Numerical runs | 0 (scripts only) | **2 sweeps** (NQ-173 ~15min + NQ-174 ~27min) |
| Verdict deliverables | 0 | **2** (V5b-F Branch + ζ_* values) |
| New theory files | 6 daily + 2 audit (8 G0) | **4-5 daily** (NQ-173 verdict + NQ-174 results + G3 Phase 5 + 99_summary) |
| User decisions | Option α (G0 entries) | **Commitment 14 (O5')/(O7)** |
| New Cat A | 5 (σ supporting) | 0 confirmed (V5b-F Cat C → B target if Branch B; canonical proposal only) |
| Files outputs | 14 (12 daily + 2 audits) | **6-8** (4-5 daily + canonical edits + weekly_draft) |

---

## §3. 30-Minute Granular Schedule

### Block 1 — Morning Numerical (09:00-11:00, 2h) — G1 + G2 sweeps + initial inspection

#### 09:00-09:15 (15min): PRE-RUN sanity test (Round-1 §6.G follow-through)

**Action**: per `100_day2_carry.md` §2 Block 1, run scc API sanity test:

```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 -c "
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
import scipy.sparse as sp
import numpy as np
n = 16
rows = list(range(n-1)) + list(range(1, n))
cols = list(range(1, n)) + list(range(n-1))
g = GraphState(sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n)))
p = ParameterRegistry(alpha_bd=1.0, beta_bd=4.0, volume_fraction=0.1, a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0, w_cl=0.0, w_sep=0.0, w_bd=1.0, n_restarts=1, max_iter=100)
res = find_formation(g, p, normalize=False, verbose=False, u_init=np.full(n, 0.1))
print('OK', res.converged, res.energy)
"
```

**Success metric**: prints `OK True <number>`.

**Failure mode F1**: API mismatch (e.g., `find_formation()` doesn't accept `normalize=`). Action: edit script kwargs (15-30min); resume Block 1 at 09:30-09:45.

#### 09:15-09:45 (30min): NQ-173 + NQ-174 parallel launch

**Action**: open two terminals.

Terminal A (NQ-173, ~15min):
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 scripts/nq173_v5b_f_partial_goldstone.py
```

Terminal B (NQ-174, ~27min):
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 scripts/nq174_zeta_star_precise.py
```

**While waiting (30min)**: open `02_NQ173_v5b_f_results.md` §5 (results template) + `04_nq174_setup.md` §6 (Day 2 checklist) for refresher.

**Success metric**: NQ-173 done by 09:30, JSON output at `CODE/scripts/results/nq173_v5b_f.json`.

#### 09:45-10:30 (45min): NQ-173 verdict via decision tree

**Action**:
1. Open `nq173_v5b_f.json`. Parse 15 minimizer attempts.
2. Compute per-(ζ, seed) measurements: max_overlap_full, max_overlap_bulk, bulk_mass_fraction, α/β/γ mode decomposition.
3. Apply `02_NQ173_v5b_f_results.md` §6 decision tree.
4. Identify Branch (A/B/C/D/E).

**Output skeleton** (Day 2 file): `01_NQ173_v5b_f_verdict.md` (~150-200 lines).
- §1 results table (15 rows filled).
- §2 per-ζ aggregates.
- §3 verdict identification (Branch X).
- §4 implications for V5b-F status (Cat C → ?, refined statement).
- §5 canonical proposal (T-V5b-T entry update text, drafted).

**Success metric**: V5b-F Branch identified; Cat C → Cat B target decision recorded.

**Failure mode F3**: H1/H2/H3 inconclusive (Branch E). Action: V5b-F Cat C unchanged + refined statement; W6+ NQ-173c (multi-pronged discriminators).

#### 10:30-11:00 (30min): NQ-174 verdict + ζ_* canonical proposal draft

**Action**:
1. Open `nq174_zeta_star.json`. Parse 40 minimizer attempts (25 torus + 15 cycle).
2. Per-ζ mean overlap → identify ζ_* (smallest ζ where mean > 0.9) per graph class.
3. Compare to W4-04-26 NQ-170c brackets:
   - ζ_*(2D torus L=20): expected ∈ [0.30, 0.40]
   - ζ_*(1D cycle L=40): expected ∈ [0.05, 0.15]
4. Draft canonical proposal: T-V5b-T-(d) entry's bracket → 2-decimal precise value.

**Output**: `02_NQ174_zeta_star_results.md` (~150 lines). §1 sweep results, §2 ζ_* extraction, §3 canonical proposal text (for user-decision later in Day).

**Success metric**: ζ_*(2D torus L=20), ζ_*(1D cycle L=40) extracted; canonical proposal drafted.

---

### Block 2 — Late Morning Verdict + Canonical Proposal (11:00-12:30, 1.5h)

#### 11:00-11:45 (45min): V5b-F status update finalization

**Action**: complete `THEORY/logs/daily/2026-04-27/03_v5b_f_status_update.md` §7 verdict (deferred from Day 1):
- Apply NQ-173 Branch verdict (from Block 1).
- Update §2 to "**Verdict: Branch X**" header.
- Cat C → ? decision finalized.

**Output**: `03_v5b_f_status_update.md` updated (Day 2 modification — explicitly noted with `*Verdict 2026-04-28:*` marker).

**Success metric**: V5b-F status post-NQ-173 documented; future canonical-merge candidate prepared.

#### 11:45-12:30 (45min): Canonical proposal review + user decision input

**Action**: prepare canonical proposal package for user decision:
- T-V5b-T entry refinement (V5b-F mechanism reference + ζ_* precise values).
- Both go into a single canonical edit batch (Day 2 PM Block 4 or Day 3 morning).

**Output**: `03_canonical_proposal_v5b_t_update.md` (~100 lines). Contains:
- Proposed T-V5b-T-(d) line replacement (precise ζ_* values).
- Proposed V5b-F mechanism rider (per Branch X verdict).
- Estimated canonical line count delta (~20-30 lines).

**Success metric**: User can review proposal package and approve/modify in Block 4.

---

### Block 3 — Lunch + G3 Multi-Formation σ Phase 5 Initiation (13:30-16:00, 2.5h)

#### 13:30-14:30 (60min): G3 — multi-formation σ definition draft

**Action**: open `THEORY/working/MF/multi_formation_sigma.md` (currently doesn't exist; create).

**Initial scope**:
- Phase 5 σ definition for K-formation field $\{u^{(j)}\}_{j=1}^K$ on $\Sigma^K_M = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$.
- Per-formation σ_j (single-formation σ-tuple per formation).
- Inter-formation σ_jk (cross-formation Hessian terms).
- Combined σ_multi := (σ_1, ..., σ_K, {σ_jk}_{j<k}).

**Cross-cutting input** (from Day 1 V5b-F + G3 synergy noted in `99_summary.md` §4):
- If V5b-F Branch B verdict supports bulk-localization → inter-formation gap analog uses similar mechanism.
- If V5b-F Branch C/D (other branches) → mechanism transfer less direct.

**Output**: `working/MF/multi_formation_sigma.md` (~250-300 lines). Definition + first observations + open questions.

**Success metric**: σ_multi definition committed at working level; Phase 5 work officially initiated.

#### 14:30-15:30 (60min): MO-1 face decision (W5 strategic plan §0.4 Decision 2)

**Action**: choose among Options A/B/C for handling MO-1 (Morse theory inapplicability on $\Sigma^K_M$ corners):
- **Option A (interior 한정)**: σ_multi defined only on $\Sigma^K_M$ interior, corners excluded. Pragmatic; doesn't engage MO-1 directly.
- **Option B (stratified Morse on $\Sigma^K_M$)**: directly attack MO-1; theoretically rigorous, time-heavy (multi-week).
- **Option C (soft-K detour)**: use W4-04-21 K_soft on $\Sigma_m$ (single-formation manifold), avoiding $\Sigma^K_M$ corners. Conservative but may not fully achieve multi-formation σ.

**Decision criteria**:
- If V5b-F Branch B verdict supports bulk-localization → **Option A pragmatic** is more attractive (interior only, leveraging single-formation σ + boundary correction).
- If V5b-F other branch → consider Option C as backup.

**Output**: `04_G3_phase5_MO1_decision.md` (~100-150 lines). Decision recorded with rationale + W5+ implications.

**Success metric**: MO-1 face strategy chosen; W6+ trajectory clarified.

#### 15:30-16:00 (30min): G3 first numerical test prep

**Action**: prepare K=2 baseline numerical script (DEFER actual run to Day 3 morning — Day 2 scope ends with script draft).

**Output**: `CODE/scripts/g3_baseline_k2_sigma.py` (~150 lines, skeleton).

**Success metric**: K=2 sigma_multi baseline script written; Day 3 09:00 run target.

---

### Block 4 — Late Afternoon Commitment 14 User Decision (16:00-17:30, 1.5h)

#### 16:00-16:30 (30min): Review Commitment 14 (O5')/(O7) proposed text

**Action**: open `92_critical_review_round2.md` §2 (O7 tie-breaking) + §4 (O5' multi-irrep). Review proposed canonical text for:
- Consistency with existing Commitment 14 (O1-O5).
- Compatibility with T-σ-Theorem-3 (vi) irrep table format.
- Compatibility with T-σ-Theorem-4 (v) σ-tuple ordering.

**Discussion topics** for user:
- O5' multi-irrep representation: multi-set vs separate entries — which is more useful for paper §4 σ-framework section?
- O7 tie-breaking: Mulliken convention ($A_1, A_2, B_1, B_2, E$) vs character-evaluation order — which is more standard in computational literature?
- Should both go into canonical v1.5 (today's edit) or separate v1.6 release?

**Success metric**: User approve/modify/defer position recorded.

#### 16:30-17:30 (60min): Commitment 14 canonical edit (if approved)

**Action** (if approved): edit `canonical.md` §11.1 Commitment 14 to add (O5') and (O7).

**Specific edits**:
1. canonical.md line ~768 (Commitment 14 main body): append (O5') and (O7) sub-clauses.
2. theorem_status.md CV-1.5 entry: append "Commitment 14 update" note.
3. CHANGELOG.md: append "Addendum 3 (Day 2)" with Commitment 14 update.
4. T-σ-Theorem-4 entry: remove "deferred to user decision" markers; replace with direct reference to Commitment 14 (O7).

**Output**: canonical.md +~30 lines; theorem_status.md +~10 lines; CHANGELOG +~50 lines.

**Success metric**: Commitment 14 (O5')/(O7) canonically promoted; v1.5 canonical fully self-consistent.

**Failure mode F5**: User defers decision (wants more time). Action: skip Block 4 edits; record deferral in Day 2 summary.

---

### Block 5 — Day 2 Close (17:30-18:30, 1h)

#### 17:30-18:00 (30min): Day 2 summary

**Action**: write `99_summary.md` Day 2 reflection (~200-250 lines).

**Sections**:
- §1 What got done (Block-by-Block).
- §2 What did not (deferred/failed).
- §3 Quantitative outcomes vs targets.
- §4 What went well / surprised / blocked.
- §5 Day 3 priority adjustment.
- §6 NQ spawns from Day 2.

**Success metric**: Day 2 status documented.

#### 18:00-18:30 (30min): Weekly_draft 04-28 entry

**Action**: append 04-28 entry to `THEORY/logs/weekly/2026-04-W5/weekly_draft_storming.md` (latest-first).

**Sections** (per W5 weekly_draft format):
- ### Added (Day 2 verdicts: V5b-F Branch X, ζ_* values, G3 σ_multi definition initiated).
- ### Modified (V5b-F status canonical proposal, MO-1 face decision, possibly Commitment 14 (O5')/(O7) if approved).
- ### Pending (G3 Phase 5 K=2 baseline numerical Day 3, V5b-F canonical edit Day 3, etc.).

**Success metric**: Weekly_draft up-to-date.

---

## §4. Day 2 Output Inventory (총 6-8 files)

### canonical/ updates

| 파일 | 변경 (conditional on user decision) | 분량 |
|------|-----------------------------------|------|
| `canonical.md` | T-V5b-T entry update (V5b-F + ζ_*) + possible Commitment 14 (O5')/(O7) | +50-80 lines |
| `theorem_status.md` | possible Commitment 14 update | +10-30 lines |
| `CHANGELOG.md` | Day 2 entry + possible Addendum 3 | +200-300 lines |

### daily/ outputs

| 파일 | 분량 |
|------|------|
| `01_NQ173_v5b_f_verdict.md` | ~200 lines |
| `02_NQ174_zeta_star_results.md` | ~150 lines |
| `03_canonical_proposal_v5b_t_update.md` | ~100 lines |
| `04_G3_phase5_MO1_decision.md` | ~150 lines |
| `99_summary.md` | ~200-250 lines |

### CODE/scripts/ outputs

| 파일 | 분량 |
|------|------|
| `g3_baseline_k2_sigma.py` | ~150 lines (skeleton) |

### CODE/scripts/results/ outputs

| 파일 |
|------|
| `nq173_v5b_f.json` (15 minimizers data) |
| `nq174_zeta_star.json` (40 minimizers data) |

### working/ outputs

| 파일 | 분량 |
|------|------|
| `working/MF/multi_formation_sigma.md` | ~250-300 lines (NEW) |

### W5 weekly buffer

| 파일 | 변경 |
|------|------|
| `weekly_draft_storming.md` | 04-28 entry append (~150-200 lines) |

**Total Day 2 line count added**: ~1500-2000 lines across all files (vs Day 1's ~3500 — moderate scope).

---

## §5. Specific Success Metrics (Day 2 EOD)

### Quantitative

- [ ] NQ-173 numerical run successful → 15 minimizers analyzed → Branch verdict identified.
- [ ] NQ-174 numerical run successful → ζ_*(2D torus L=20), ζ_*(1D cycle L=40) extracted to 2-decimal precision.
- [ ] G3 multi-formation σ definition committed at working level (`working/MF/multi_formation_sigma.md`).
- [ ] MO-1 face decision (Option A/B/C) recorded.
- [ ] G3 K=2 baseline script drafted.
- [ ] Daily files: 5+ new files in `daily/2026-04-28/`.
- [ ] V5b-F Cat C → Cat B target decision (if Branch A or B verdict).
- [ ] Commitment 14 (O5')/(O7) user decision recorded (approve/modify/defer).

### Qualitative

- [ ] **G1 P0 closed** (V5b-F characterization Day 2 verdict).
- [ ] **G2 P1 substantive** (ζ_* canonical proposal ready).
- [ ] **G3 P1 opened** (multi-formation σ Phase 5 initiated).
- [ ] **canonical v1.5 self-consistent** (with or without Commitment 14 update — both states are coherent).
- [ ] T1 = 8 → 9 if V5b-F Cat B promoted (Day 3+ canonical merge); otherwise T1 = 8 unchanged.
- [ ] W5 Standard ladder achieved (per W5_strategic_plan.md §0.5).

---

## §6. Hard Constraints (Day 2)

- [ ] Pre-Run sanity test before NQ-173/174 sweeps (Round-1 §6.G follow-through).
- [ ] Mode-agnostic detection enforced in numerical analysis (no `mode_overlaps[1]` hardcode).
- [ ] V5b-F canonical edit only after NQ-173 verdict + user approval (per Day 1 plan §6 hard constraint extended).
- [ ] Commitment 14 (O5')/(O7) user decision required before canonical edit.
- [ ] Silent resolution 0 (V5b-F Branch X verdict explicitly recorded).
- [ ] 175 tests passing 유지 (no `scc/` changes expected; G3 baseline script in `scripts/`).
- [ ] **Round-1 + Round-2 audit protocols proactively applied to G3 work** (numerical sanity + structural completeness check before G3 Phase 5 commit).

---

## §7. Failure Modes + Contingency

### F1: NQ-173 sanity test fails (scc API mismatch)

**Trigger**: 09:00-09:15 sanity test errors.
**Action**: edit script kwargs (15-30min); resume at 09:30-09:45. If structural mismatch (e.g., missing scc module), defer numerical to Day 3; Day 2 focuses on G3 + Commitment 14.

### F2: NQ-173 numerical hang (>30 min)

**Trigger**: 10:00 NQ-173 still running.
**Action**: cut to ζ=0.5 only (5 seeds). Day 3 carry ζ=0.7, 1.0.

### F3: Branch verdict Branch E (inconclusive)

**Trigger**: 10:30 H1/H2/H3 mixed signals, no dominant.
**Action**: V5b-F Cat C unchanged with refined "mechanism-mixed" statement; W6+ NQ-173c.

### F4: NQ-174 hang (>40 min for 40 minimizers)

**Trigger**: 10:30 NQ-174 still running.
**Action**: ζ_*(2D torus) prioritized; cut 1D cycle to ζ ∈ {0.05, 0.15} only.

### F5: G3 Phase 5 scope explodes (>2.5h budget)

**Trigger**: 15:30 still on definition without MO-1 decision.
**Action**: scope cut — definition only Day 2; MO-1 decision Day 3.

### F6: Commitment 14 user defers

**Trigger**: 16:30 user wants more time.
**Action**: skip Block 4 edits; record deferral; canonical v1.5 stays current state. Day 3+ revisit.

### F7: Time pressure (>10h cumulative)

**Trigger**: 18:30 Day 2 close time + Block 5 incomplete.
**Action**: cut Block 5 to weekly_draft only (defer 99_summary to Day 3 morning).

---

## §8. Decision Tree (Day 2 specific)

```
09:30 — NQ-173 numerical run complete?
  ├ Yes → 09:45 verdict via decision tree (Block 1 continues)
  ├ Hung → cut to ζ=0.5 only (F2)
  └ Crashed → debug + Day 3 carry

10:30 — Verdict identified (A/B/C/D/E)?
  ├ Branch B (most likely, ~70%) → V5b-F Cat C → Cat B target; canonical proposal Day 2 PM (Block 2)
  ├ Branch A → similar to B but stronger; same canonical proposal
  ├ Branch C/D → V5b-F Cat C refined; canonical proposal weaker
  └ Branch E → V5b-F Cat C unchanged + W6+ NQ-173c

12:30 — Canonical proposals (V5b-F + ζ_*) drafted?
  ├ Yes → Block 3 G3 begins 13:30
  └ No → cut Block 3 G3 to definition only

15:30 — G3 MO-1 face decision made?
  ├ Yes → Block 4 Commitment 14 begins 16:00
  ├ Pending → defer MO-1 to Day 3; Block 4 starts 16:00 with V5b-F canonical update
  └ Scope explosion → defer entire G3 to Day 3

16:30 — Commitment 14 user decision?
  ├ Approve → 16:30-17:30 canonical edit + theorem_status + CHANGELOG
  ├ Modify → 16:30-17:30 user revision; edit Day 3
  └ Defer → skip Block 4 edits; current state stays

18:00 — Day 2 close ready?
  ├ All success metrics met → write 99_summary + weekly_draft
  └ Partial → honest 99_summary; Day 3 plan adjusted
```

---

## §9. Day 2 Moderate vs Day 1 Aggressive (Calibration)

### Day 1 (AGGRESSIVE, ~12-14h, 3500 lines)
- G0 fully merged + Round-1 + Round-2 corrections
- G1 + G2 scripts ready
- 14 artifact files
- 2 commitment-level changes deferred

### Day 2 (MODERATE, ~9h, 1500-2000 lines)
- G1 verdict + G2 numerical + G3 opening
- 6-8 artifact files
- Commitment 14 user decision processed

### Why moderate?
- Day 1 marathon was *infrastructure-heavy* (canonical merge + 2 scripts).
- Day 2 is *substantive* (verdicts + opening) but requires user trigger for numerical (~45min) — less Claude-side text generation, more User+Claude collaborative analysis.
- Day 1 Round-1 + Round-2 audit fatigue suggests calibrating Day 2 to leave audit budget for G3 (which will need its own Round-1/2 audit when committed).

---

## §10. Pre-Built Templates (Block 2 morning shortcut)

### V5b-F status update template (for `01_NQ173_v5b_f_verdict.md`)

```markdown
## §1. Numerical Results

| ζ | seed | F1? | mode_idx | λ | max_ov_full | max_ov_bulk | bmf | α²+β² |
|---|------|----|---------|---|-------------|-------------|-----|-------|
| 0.5 | 0 | Y | ? | ? | ? | ? | ? | ? |
... (15 rows total)

## §2. Per-ζ Aggregates

| ζ | mean max_ov_full | mean max_ov_bulk | mean bmf | mean α²+β² |
|---|------------------|------------------|----------|-----------|
| 0.5 | ? | ? | ? | ? |
| 0.7 | ? | ? | ? | ? |
| 1.0 | ? | ? | ? | ? |

## §3. Verdict: Branch X

[Apply 02_NQ173_v5b_f_results.md §6 decision tree.]

[If Branch B (most likely):]
**Branch B verdict — H1+H2 mixed.** Bulk-only overlap > 0.85 (H1 partial); α²+β² < 0.95 with γ ≈ <value> (H2 partial). V5b-F mechanism = bulk-localized translation Goldstone with boundary mode hybridization.

[Etc. for other branches.]

## §4. V5b-F Status Update

- Pre-Day-2: Cat C (qualitative observation, NQ-173 quantification carry).
- Post-Day-2: **Cat B target** (if Branch A or B) / Cat C refined (otherwise).

## §5. Canonical Proposal

[T-V5b-T entry refinement text.]
```

### ζ_* template (for `02_NQ174_zeta_star_results.md`)

```markdown
## §1. Sweep Results

[Per (graph_class, ζ, seed) overlap table.]

## §2. ζ_* Extraction

| Graph class | L | ζ_* (estimated) | mean overlap at ζ_* |
|-------------|---|-----------------|---------------------|
| 2D torus | 20 | <value> | <value> |
| 1D cycle | 40 | <value> | <value> |

## §3. Canonical Proposal

T-V5b-T-(d) line replacement (line 1129 in canonical.md):
- Old: $\zeta_*(2D \text{ torus}) \in [0.2, 0.5]$ + $\zeta_*(1D \text{ cycle}) < 0.2$
- New: $\zeta_*(2D \text{ torus L=20}) \approx <value>$ + $\zeta_*(1D \text{ cycle L=40}) \approx <value>$

[Estimated canonical line delta: ~5-10 lines.]
```

---

## §11. Reference: W5 Strategic Plan Goal Cross-Reference

- **G0** ✅ COMPLETE (Day 1 + Round 1+2).
- **G1 (P0 MUST, Day 1-2 → finishes Day 2 AM)**: NQ-173 V5b-F partial Goldstone — Day 2 Block 1+2.
- **G2 (P1, Day 2-3 → finishes Day 2 if smooth)**: NQ-174 ζ_*(graph) precise — Day 2 Block 1+2.
- **G3 (P1, Day 3-4 → INITIATES Day 2 PM)**: Multi-formation σ Phase 5 — Day 2 Block 3.
- **G4 (P2, Day 5)**: NQ-175 V5b 3D extension — Day 5+.
- **G5 (P2, Day 5)**: SF Round 1-5 Cat A merge — Day 5+.
- **G6, G7, G8 (P3, Day 6-7)**: Day 6+.

Day 2 advances W5 to **Standard ladder** (P0+P1) per `W5_strategic_plan.md` §0.5 (~70% a priori probability).

---

## §12. End-of-Day Reflections (template)

18:00-18:30 자가 reflection (in `99_summary.md`):

1. **What went well**: ?
2. **What surprised**: ? (e.g., V5b-F branch unexpected? G3 MO-1 decision easier than feared?)
3. **What blocked**: ? (e.g., scc API mismatch? G3 scope explosion?)
4. **Day 3 priority adjustment**: ?
5. **W5 strategic plan revision needed?**: ?
6. **Round-1/2 audit budget check**: did Day 2 leave time for G3 audit when Day 3+ commits to canonical?

---

**End of plan.md for 2026-04-28 (W5 Day 2 MODERATE).**
**Mission: G1 verdict + G2 ζ_* + G3 Phase 5 initiation + Commitment 14 user decision.**
**Time budget: 8-10 hours. Output: 6-8 files, ~1500-2000 lines text.**
**Hard target: V5b-F Branch verdict closed + ζ_* values + G3 σ_multi definition.**
**Stretch (only if all blocks ahead of schedule)**: G3 K=2 baseline numerical Day 2 evening (move from Day 3).
