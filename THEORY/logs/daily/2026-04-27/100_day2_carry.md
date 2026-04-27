# 100_day2_carry.md — Day 2 (2026-04-28) Carry-Forward Notes

**Session:** 2026-04-27 (W5 Day 1 close, late-night carry-forward authoring)
**Purpose:** Concrete starter notes for Day 2 plan.md authoring — what's ready to execute, what's deferred to user decision, what's the most-pressing seed for the next session.
**Status:** Draft for user reference when writing `THEORY/logs/daily/2026-04-28/plan.md` Tuesday morning. Not a plan itself — plan authoring remains user's prerogative.

---

## §1. Day 1 Carry State (Honest Inventory)

### Completed
- G0 σ-framework supporting structures canonical merge (5 §13 entries, Round-1 + Round-2 corrected, all Cat A).
- G1 NQ-173 infrastructure (script + 5-branch verdict tree).
- G2 NQ-174 script + Day 2 morning checklist + PRE-RUN sanity-test.
- 15 NQ spawns registered (NQ-176..NQ-190).
- Canonical v1.5 release-ready; 2 Commitment-level changes deferred to user agenda.

### Awaiting user trigger (numerical)
- **NQ-173 V5b-F**: ~10-15 min runtime, fills Branch A/B/C/D/E verdict in `03_v5b_f_status_update.md` §7.
- **NQ-174 ζ_*(graph) precise**: ~27 min runtime, gives ζ_*(2D torus L=20) and ζ_*(1D cycle L=40) to 2-decimal precision.

### Awaiting user decision (Commitment-level canonical edits)
- **Commitment 14 (O5')** multi-irrep eigenspace convention.
- **Commitment 14 (O7)** tie-breaking convention by canonical irrep order (e.g., Mulliken $A_1, A_2, B_1, B_2, E$).

Proposed text in `92_critical_review_round2.md` §2 + §4. These touch §11.1 Fixed Commitments — non-trivial canonical changes. User can: (a) approve as-is; (b) propose modifications; (c) defer to W5 weekly close.

---

## §2. Day 2 Recommended Block Structure (Suggestion Only)

### Block 1 (09:00–10:00, AM): Numerical execution

**Parallel run** (separate terminals):

Terminal A — NQ-173 (~15 min):
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 scripts/nq173_v5b_f_partial_goldstone.py
```

Terminal B — NQ-174 (~27 min). Run PRE-RUN sanity test first (per `04_nq174_setup.md` §6):
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
# Sanity test (per 04_nq174_setup §6)
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
# Then full sweep:
python3 scripts/nq174_zeta_star_precise.py
```

**Expected**: NQ-173 done by 09:30, NQ-174 done by 09:45. JSON outputs at `CODE/scripts/results/nq173_v5b_f.json` and `nq174_zeta_star.json`.

### Block 2 (10:00–11:30, AM): Verdict filling

- **NQ-173**: apply `02_NQ173_v5b_f_results.md` §6 decision tree → identify Branch (A/B/C/D/E) → fill `03_v5b_f_status_update.md` §7 with verdict.
  - Most likely: **Branch B (H1+H2 mixed)** — ~70% a priori per pre_brainstorm §2.3.
  - On Branch B: V5b-F Cat C → Cat B target; canonical proposal "T-V5b-T entry + bulk-localized boundary-modification rider" (Day 2+ canonical-merge candidate).

- **NQ-174**: extract per-(ζ, seed) Goldstone overlaps from JSON; compute per-ζ mean → identify ζ_* (smallest ζ where mean > 0.9) per graph class.
  - Expected (a priori per W4-04-26 NQ-170c bracketing): ζ_*(2D torus L=20) ∈ (0.30, 0.40); ζ_*(1D cycle L=40) ∈ (0.05, 0.15).
  - On completion: T-V5b-T-(d) entry's bracket → 2-decimal precise value (canonical proposal).
  - Day 2 file: `01_NQ174_zeta_star_results.md` (~150-200 lines).

### Block 3 (13:00–17:00, PM): G3 multi-formation σ Phase 5 initiation

Per W5 strategic plan §6 Day 3 (advance to Day 2 PM if Block 1+2 completes ahead of schedule).

Key inputs from Day 1:
- σ supporting structures (Lemma 1/2/3 + Theorem 3/4) **canonical-grounded** — multi-formation σ can build on this base.
- V5b-F mechanism (NQ-173 verdict from Block 2): if Branch B, the **bulk-localization picture** gives an analytical tool for inter-formation gap analog (cross-cutting synergy noted in `03_v5b_f_status_update.md` §4 + `99_summary.md` §4).

Suggested approach: open `THEORY/working/MF/multi_formation_sigma.md` (currently empty — `THEORY/working/MF/` has only `from_single.md`). Initial scope:
- Phase 5 σ definition for K-formation field $\{u^{(j)}\}_{j=1}^K$ on $\Sigma^K_M$.
- MO-1 face decision (per W5 strategic plan §0.4 Decision 2): Option A (interior only, corner-avoiding) vs Option B (stratified Morse on $\Sigma^K_M$) vs Option C (soft-K detour on $\Sigma_m$).
- First numerical test on K=2 baseline.

Deliverable: `working/MF/multi_formation_sigma.md` skeleton (~200-300 lines) + `THEORY/logs/daily/2026-04-28/02_multi_formation_sigma_phase5.md`.

### Block 4 (17:00–19:00, evening): Commitment 14 user decision agenda

If Day 2 Blocks 1-3 successful, address the deferred Commitment-level changes:

- Review proposed (O5') and (O7) text in `92_critical_review_round2.md` §2 + §4.
- **User decision**: approve / modify / defer to W5 weekly close.
- If approved: edit canonical.md §11.1 Commitment 14 to add (O5') and (O7); add CHANGELOG addendum; update CV-1.5 release note in theorem_status.md.

### Block 5 (19:00–20:00, evening): Day 2 close

- `THEORY/logs/daily/2026-04-28/99_summary.md` (Day 2 reflection).
- weekly_draft 04-28 entry append.

---

## §3. Day 2 Failure Modes + Contingency

### F1: NQ-173 sanity-test fails (scc API mismatch)

**Trigger**: 09:00 sanity test errors (e.g., `find_formation()` doesn't accept `normalize=`, ParameterRegistry missing field).

**Action**: edit script kwargs to match actual scc API; retry. If structural mismatch: defer numerical, write Day 2 morning fix-script log instead.

### F2: NQ-173 numerical hang (>30 min)

**Trigger**: 09:30 still running.

**Action**: reduce to ζ=0.5 only (5 seeds), 5 minimizers. Day 3 carry ζ=0.7 + 1.0.

### F3: H1/H2/H3 inconclusive (Branch E)

**Trigger**: 11:00 analysis shows no dominant indicator.

**Action**: V5b-F Cat C unchanged; refined statement "mechanism mixed". W6+ NQ-173c (multi-pronged stronger discriminators).

### F4: G3 multi-formation σ scope explodes

**Trigger**: 14:00 PM Phase 5 initiation reveals scope >>> 4 hours.

**Action**: scope cut to "definition + MO-1 face decision only" (no numerical Day 2). Day 3+ continues.

### F5: Commitment 14 user decision pushes back

**Trigger**: 17:00 user wants more time to consider (O5')/(O7).

**Action**: defer to W5 weekly close; canonical v1.5 stays release-ready without these (current state).

---

## §4. Day 2 Most-Pressing Seed (Single Sentence)

> **NQ-173 + NQ-174 numerical AM verdicts → V5b-F Cat C→B Cat decision + ζ_* canonical proposal PM, then G3 multi-formation σ Phase 5 initiation with V5b-F bulk-localization as analytical tool.**

If only ONE thing happens Day 2: complete NQ-173 numerical + verdict (closes G1 P0 MUST started Day 1).

---

## §5. W5 Day 1 → Day 2 → Week Close Trajectory

Per W5 strategic plan §0.5 Success Ladder:

| Level | Conditions | Day 1 status | Day 2 progress contribution |
|-------|-----------|--------------|------------------------------|
| Minimal (~95%) | G0 + G1 (P0 only) | G0 ✅, G1 ⏳ | NQ-173 verdict closes G1 → **Minimal achieved Day 2 AM** |
| Standard (~70%) | + G2 + G3 substantive | G2 ⏳ | NQ-174 + G3 Phase 5 initiation → Standard ready Day 2 PM |
| Ambitious (~50%) | + G4-G6 ≥ 1 | not started | Day 5+ |
| Maximal (~30%) | + G7 + G8 | not started | Day 6+ |
| Stretch (~15%) | + v1.5 release + Paper 1 first draft | v1.5 release-ready | v1.5 weekly-close confirmation Day 7 |

Day 2 trajectory: **Standard ladder achievable by Day 2 EOD** if Blocks 1-3 complete.

---

## §6. Notes for Day 2 Pre-Brainstorm

Suggested topics for `THEORY/logs/daily/2026-04-28/pre_brainstorm.md` (user-authored Tuesday morning):

1. **Mental frame**: W5 Day 1 caught 14 corrections across 2 audit rounds. Day 2 should benefit from this momentum — apply both Round-1 (numerical sanity) and Round-2 (structural completeness) protocols proactively to G3 multi-formation σ work.

2. **G3 PM decision pre-think**: MO-1 face Options A/B/C — which fits the V5b-F mechanism transfer best? If V5b-F Branch B confirms bulk-localization, Option A (interior only) becomes more attractive (avoids stratified Morse on $\Sigma^K_M$ corners).

3. **Commitment 14 (O5')/(O7) personal lean**: review `92_critical_review_round2.md` §2 + §4 proposed text overnight; come to morning with provisional approve/modify/defer position.

4. **Day 1 momentum check**: did the 2-round audit feel useful? Or excessive overhead? Calibrate Day 2's audit rigor accordingly.

---

**End of 100_day2_carry.md.**
**For Day 2 plan.md author: this is reference material, not a plan. Use what's helpful, modify or discard rest.**
