# 05_nq244_launch_note.md — Theorem 4.6.1 Label Hygiene + NQ-244 Background Launch Spec

**Session:** 2026-05-01 (W5 Day 5)
**Block:** 4a (Operational Fixes, 16:00-17:00)
**Target (from plan.md):** Block 4 §16:00-16:30 — Theorem 4.6.1 / dynamic σ label hygiene cross-check (Critic C3 / MAJOR-4); Block 4 §16:30-17:00 — NQ-244 background launch metadata. **No interpretation of NQ-244 partial output.**
**This file covers:** Theorem 4.6.1 label hygiene verdict + NQ-244 launch readiness assessment + launch metadata template.
**Depends on reading:** `working/MF/sigma_multi_trajectory.md` (283 lines, Lemma 4.2(c) + Theorem 4.4(iii) status check), `working/MF/sigma_rich_phi_proof.md` (313 lines, post-EOD Φ_rich K-jump cross-check), `2026-04-30/05_critic_final_review.md` MAJOR-4 + Critic C3 recommendations, `2026-04-30/15_wave4_carry_forward.md` §2.3 (NQ-244 launch plan).

---

## §1. Theorem 4.6.1 / Lemma 4.2(c) Label Hygiene — Verdict: NO EDIT NEEDED

### §1.1 Critic C3 / MAJOR-4 recommendation summary

Per `05_critic_final_review.md` MAJOR-4 + Critic 7-agent verdict 2026-04-29:
> Lemma 4.2(c) σ^A K-jump non-determinism: "Cat B sketch" wording should be downgraded to "Cat C (conjectured)" because explicit two-trajectory counterexample construction (NQ-242c) is open; the assertion is not yet a sketched proof but a conjectured non-determinism statement.

This recommendation was applied to `working/MF/sigma_multi_trajectory.md` *during Wave 3*, prior to Day 5 entry.

### §1.2 Day 5 cross-check verdict

`working/MF/sigma_multi_trajectory.md` (283 lines, mtime Apr 30 11:15) current label state:

| Location | Current label | Day 5 verdict |
|---|---|---|
| §3.7 PH reformulation note (line 97) | "[Cohen-Steiner–Edelsbrunner–Harer 2007 / Carlsson–de Silva–Morozov 2009 standard PH fact]" | ✅ correctly cited as standard PH fact, not new SCC claim |
| §4.1 Lemma 4.1 (smooth-segment piecewise constancy) | "Cat B target in interior regime; OPEN in corner-saturated regime" (line 117-118) | ✅ correctly bracketed; (H4) corner-saturated exclusion explicit |
| **§4.2 Lemma 4.2 (c) σ^A inheritance non-determinism** | **"conjectured (Cat C) — explicit counterexample construction NQ-242c W6+. Status DOWNGRADE from earlier 'Cat B sketch' labeling"** (line 132-134) | ✅ **already applied per Critic C3**; explicit downgrade marker in place |
| §4.3 Proposition 4.3 (σ^D restriction at K-jump) | "Cat B sketch" (line 142) | ✅ defensible — proof sketch with explicit caveat about post-merger stabilizer; Critic did not request downgrade for this item |
| **§4.4 Theorem 4.4 (synthesis)** | **"(iii) σ^A inheritance non-determinism (conjectured Cat C)"** (line 151) | ✅ **already applied**; consistent with Lemma 4.2(c) |
| Status footer (line 282) | "Theorem 4.4 (σ_multi(t) trajectory) Cat B target in non-corner-saturated regime; Cat C in V5b-T-zero/V5b-F corner-saturated regime ... Lemma 4.2(c) σ^A K-jump non-determinism: Cat C (conjectured; downgraded from 'Cat B sketch' per `09_*` §2.3)" | ✅ comprehensive; explicit downgrade documented |

**Day 5 verdict**: ✅ **NO EDIT NEEDED**. Wave 3 already applied the Critic C3 / MAJOR-4 corrections. Day 5 cross-check confirms consistency between Lemma 4.2(c), Theorem 4.4(iii), and the file's status footer. Optional supplementary "small label-fix diff" item (per plan.md §4) is **not triggered**.

### §1.3 Cross-check with post-EOD `sigma_rich_phi_proof.md` (313 lines)

**Question (per `pre_brainstorm.md` §7)**: does the post-EOD Φ_rich K-jump inheritance argument retroactively try to upgrade Theorem 4.6.1's Cat C status?

**Answer**: Φ_rich is framed at the *σ_rich* augmentation layer (Path B for OP-0008), **not** the plain σ^A layer (Path A). σ_rich = (σ_A standard, centroids, orientations, Wigner-vN data) per `commitments_18_19_drafts.md` §2.1. Φ_rich Cat A target operates on σ_rich, deterministic by construction (σ_rich captures merger-geometry data $\mathcal{M}$ that plain σ^A lacks). Plain σ^A K-jump non-determinism (Lemma 4.2(c) Cat C) is **preserved** as the very motivation for σ_rich augmentation.

**Cross-check verdict**: σ_rich Path B does **not** retroactively upgrade Theorem 4.6.1 / Lemma 4.2(c). The two operate at different layers (plain vs rich). σ_rich is CV-1.7 parking lot per `04_cv16_packet_recalibration.md` §3; Theorem 4.6.1 plain-σ trajectory framework is CV-1.6 candidate (D-CV1.6-O6, READY-NEAR per `02_verification_audit.md` §3 + `04_*` §2.1). No conflict.

**Day 5 binding rule**: any future canonical text touching Lemma 4.2(c) or Theorem 4.4(iii) must continue to label these "Cat C (conjectured)" until NQ-242c explicit construction (W6 D6 input) closes. Φ_rich Cat A target on σ_rich ≠ plain σ^A Cat A target.

---

## §2. NQ-244 Background Launch Readiness Assessment

### §2.1 Target specification (per `15_wave4_carry_forward.md` §2.3 + Day 4 99_summary §8.1)

NQ-244 = 3D LSW dynamics on $T^3_{15}$ torus (3-dimensional, side length 15) with $K = 10$ formations.

**Purpose**: D-CV1.6-P3 — verify whether 3D LSW α-exponent matches 2D scaling. If 3D LSW α exponent measurement matches 2D, promote 3D extension to Cat B target at CV-1.6.

**Compute envelope**: ~12h overnight per `13_wave3_critical_findings.md` + `99_summary.md` Day 4 §8.1. Day 5 launch = ~15min setup; result analysis = Day 6+/W6 D4 (post `04_cv16_packet_recalibration.md` §2.2 P3 deferral rule).

### §2.2 Script existence audit at Day 5 entry

**Question**: Does a ready-to-run `nq244_3d_lsw_t3_15_k10.py` script exist?

**Audit result**: `ls CODE/scripts/` reveals **no `nq244*` script**. Closest existing infrastructure:
- `CODE/scripts/_v5_3D_torus.py` — 3D torus simulation template.
- `CODE/scripts/_f7_K10_LSW.py` — K=10 LSW simulation template (likely 2D).
- `CODE/scripts/_t1_higher_K_LSW.py`, `_t2_param_scan_LSW.py` — LSW parameter scans.
- `CODE/scripts/_q2_NQ220_LSW.py` — NQ-220 LSW reference implementation.

**Verdict**: NQ-244 launch script does **NOT** exist at Day 5 entry. Adaptation from `_v5_3D_torus.py` + `_f7_K10_LSW.py` templates is required (estimated 30-60 min script preparation, not 15 min).

### §2.3 Day 5 launch decision

**Day 5 binding rule** (per plan.md §5 explicit non-goal: "No NQ-244 result interpretation. Launch metadata only" + per Risk-3: "NQ-244 launch hijacks the session"):

- Lead does **NOT** create the NQ-244 script today (script creation = 30-60 min CODE work; not a Day 5 reconciliation deliverable).
- Lead **DOES** produce launch metadata template + script-adaptation pointer (this file §3 below).
- Actual launch is **deferred to operator** (user or downstream session) when the NQ-244 script is prepared.
- W6 D4 result analysis lane (per `04_cv16_packet_recalibration.md` §2.2 P3) accommodates this deferral cleanly: if launch happens W6 D1-D2 instead of Day 5 evening, overnight compute still completes by W6 D4.

This is consistent with plan.md Risk-3 mitigation. Day 5 reconciliation discipline > 1-day launch acceleration.

---

## §3. NQ-244 Launch Metadata Template (operator-ready spec)

### §3.1 Parameters

| Parameter | Value | Source |
|---|---|---|
| Graph | $T^3_{15}$ (3D torus, side 15, $n = 3375$ sites) | NQ-244 spec |
| K (formation count) | 10 | NQ-244 spec |
| Initial condition | Random K=10 Voronoi tessellation per LSW protocol | (template `_q2_NQ220_LSW.py`) |
| α (closure rate) | 1.0 | scc default |
| β (separation rate) | TBD per dynamic regime — start with $\beta = 4$ (default V5b-T) | (template) |
| Time horizon T | 200 (per Day 3 U2 long-time precedent in `_u2_long_time.py`) | adaptation |
| Snapshot frequency | every Δt = 2 (100 snapshots over T = 200) | NQ-242 PH alignment |
| Dimension | 3 | NQ-244 |
| Seed | 42 (reproducibility default) | scc default |

### §3.2 Launch command (template — NOT executed today)

```bash
# Adaptation required: combine _v5_3D_torus.py geometry + _f7_K10_LSW.py dynamics
cd CODE
python3 scripts/nq244_3d_lsw_t3_15_k10.py \
    --L 15 --dim 3 --K 10 \
    --beta 4.0 --alpha 1.0 \
    --T 200 --dt 0.01 \
    --snapshot_dt 2.0 \
    --seed 42 \
    --output results/nq244_3d_lsw_t3_15_k10.json \
    --log results/nq244_3d_lsw_t3_15_k10.log \
    > results/nq244_3d_lsw_t3_15_k10.stdout 2>&1 &
echo $! > results/nq244_3d_lsw_t3_15_k10.pid
```

Background launch (`&` + PID record) so the foreground session can close cleanly. Expected runtime: ~10-12 hours overnight.

### §3.3 Restart command (if interrupted)

```bash
cd CODE
python3 scripts/nq244_3d_lsw_t3_15_k10.py \
    --resume results/nq244_3d_lsw_t3_15_k10.checkpoint \
    [other params same] &
```

(Requires the script to support `--resume` checkpoint loading. Adaptation note: `_q2_NQ220_LSW.py` has checkpoint pattern that can be ported.)

### §3.4 Output file paths (expected)

| Path | Content |
|---|---|
| `CODE/scripts/results/nq244_3d_lsw_t3_15_k10.json` | Snapshot data: u(x,t) at 100 time points, K_act trajectory, energy trajectory |
| `CODE/scripts/results/nq244_3d_lsw_t3_15_k10.log` | Verbose execution log |
| `CODE/scripts/results/nq244_3d_lsw_t3_15_k10.stdout` | stdout (low-volume status) |
| `CODE/scripts/results/nq244_3d_lsw_t3_15_k10.pid` | Process ID for monitoring |
| `CODE/scripts/results/nq244_3d_lsw_t3_15_k10.checkpoint` | Checkpoint file for restart |

### §3.5 Day 5 binding non-action rule

The following are **forbidden today** (per plan.md §5 + Risk-3):
- Reading partial output if launch happens.
- Interpreting trajectory data (even cursory).
- Adjusting CV-1.6 P3 status based on partial NQ-244 evidence.
- Drafting CV-1.6 caveat text using NQ-244 partial data.

Result interpretation = **Day 6+ / W6 D4** (per `04_cv16_packet_recalibration.md` §2.2 P3 row + `07_w6_plan_preview.md` Block 6 §19:00-19:45 W6 D4 entry).

---

## §4. Block 4a Verdict Summary

### §4.1 Theorem 4.6.1 / Lemma 4.2(c) label hygiene

✅ **NO EDIT NEEDED**. Wave 3 corrections applied; Day 5 cross-check confirms. σ_rich Path B does not retroactively upgrade plain σ^A status. Optional supplementary label-fix diff is **not triggered** for Day 5.

### §4.2 NQ-244 background launch

🟡 **DEFERRED — launch metadata spec ready; script adaptation required**. NQ-244 launch script does not exist at Day 5 entry. Day 5 produces operator-ready launch command + parameter spec + output path template. Actual launch deferred to operator (Day 5 evening or W6 D1-D2). W6 D4 result analysis lane absorbs the deferral.

### §4.3 Block 4a outputs

This file (`05_nq244_launch_note.md`).

### §4.4 Transition to Block 4b

**Next**: Block 4b (16:30-17:30 in plan.md original; remapped to "after Block 4a" in actual Day 5 sequence) — active teammate decision + Wave 5 contingency review. Output: `06_active_teammate_and_wave5_decisions.md` (~100-150 lines).

---

**End of 05_nq244_launch_note.md.**
**Status:** Theorem 4.6.1 label hygiene = no edit needed (Wave 3 already applied); σ_rich Path B does not retroactively over-promote plain σ^A. NQ-244 launch script does not exist at Day 5 entry; launch metadata spec + adaptation pointer (`_v5_3D_torus.py` + `_f7_K10_LSW.py` templates) produced; actual launch deferred to operator with W6 D4 result analysis lane absorbing the deferral. No Day 5 NQ-244 interpretation per plan.md §5 + Risk-3.
