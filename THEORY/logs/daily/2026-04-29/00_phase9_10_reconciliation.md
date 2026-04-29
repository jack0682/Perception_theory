# 00_phase9_10_reconciliation.md — Phase 9-10 REVISION ↔ Proposal Text Reconciliation

**Session:** 2026-04-29 (W5 Day 3, Block 0.5)
**Target (from plan.md §3 Block 0.5):** Verify each D-1..D-6 proposal text reflects **FINAL Phase 10 state**, not earlier-cycle drafts.
**This file covers:** §1 method, §2 per-item verdict (D-1..D-6), §3 D-6 SPLIT recommendation (D-6a vs D-6b), §4 actionability summary.
**Depends on reading:** `2026-04-28/01_NQ173_v5b_f_verdict.md` §3.4, `02_NQ174_zeta_star_results.md` §6, `03_canonical_proposal_v5b_t_update.md` §§2-5, `20_canonical_proposals_F10_F11.md` Part 1+2, `34_Phase10_findings.md` §3 (V3 Hessian σ_multi^A(t)), `33_Phase9_findings_integration.md` (U4 simplified σ trajectory).

---

## §1. Method

For each user-decision item, ask three questions:

(Q1) **Source phase**: in which Phase was the proposal text drafted?
(Q2) **Subsequent cycles**: did Phase ≥ Q-source produce findings that *modify*, *extend*, or *invalidate* the proposal's substantive claim?
(Q3) **Final-state delta**: if (Q2) yes, the proposal text either (a) needs revision before canonical apply, or (b) needs SPLIT into static-stable (apply) + dynamic-new (defer).

A reconciliation that returns "no Phase ≥ source change" = proposal reflects FINAL; ready for Block 1 user review without textual update.

---

## §2. Per-Item Reconciliation

### D-1: Commitment 14 (O5') multi-irrep eigenspace convention

- (Q1) Source: Day 1 W5 Round-2 review (`2026-04-27/92_critical_review_round2.md` §4.3); Phase 1+2 review confirmed Phase 4 §5.4-5.5.
- (Q2) Phase 5-10 cycles: σ_multi^A two-layer (Phase 2-4), T-σ-Multi-1 dynamic vs static (Phase 5+6), LSW recovery (Phase 7), CH correspondence (Phase 8-9), 3D structural verification (Phase 10). **None of these touch single-formation σ-tuple ordering convention.**
- (Q3) **No Phase ≥ 5 change. FINAL.**

**Proposal text** (`03_canonical_proposal_v5b_t_update.md` §5.2): reflects FINAL. Ready for Block 1 review unchanged.

### D-2: Commitment 14 (O7) tie-breaking via Mulliken character order

- (Q1) Source: same as D-1 (Day 1 Round-2 review).
- (Q2) Subsequent cycles: same null result as D-1 — no Phase ≥ 5 result modifies the σ-tuple ordering convention for single-formation graphs.
- (Q3) **No Phase ≥ 5 change. FINAL.**

**Proposal text** (`03_canonical_proposal_v5b_t_update.md` §5.3): reflects FINAL. Ready for Block 1 review unchanged.

### D-3: V5b-F mechanism rider in T-V5b-T

- (Q1) Source: Phase 2 α (NQ-173 monkey-patch run); written up in `01_NQ173_v5b_f_verdict.md` §3.4 + `03_canonical_proposal_v5b_t_update.md` §2.2.
- (Q2) Subsequent cycles touching V5b-F:
  - Phase 3: `11_PN_unification.md` §4 unified PN-barrier formula — *augments* the V5b-F mechanism (provides Cat A path NQ-198), but does **not change the static mechanism description**.
  - Phase 4 F8 (NQ-198 path): no progress; still Cat B target.
  - Phase 5-7 dynamic-stability findings (Q1 volume-projected, R1.2 box-clipping): pertain to **K-field LSW dynamics**, not single-formation V5b-F static Hessian structure.
  - Phase 8-10 LSW α / hybrid γ / 3D: orthogonal to V5b-F.
- (Q3) **Static V5b-F mechanism FINAL** (Phase 2 derivation stable). Phase 6 box-clipping finding **does not affect this static claim** — it concerns whether the **multi-formation Goldstone instability manifests dynamically** under volume + simplex + box constraints.

**Optional refinement** (not blocking): could add an inline static-vs-dynamic remark in the V5b-F entry: *"[The single-formation Hessian mechanism (a)+(b)+(c) is a static spectral statement; whether the corresponding dynamic instability manifests under gradient flow with [0,1] box constraint is a separate question, see §13 T-σ-Multi-1 / Phase 6 R1.2 dynamic stability finding.]"* Adds 2-3 lines. Decision left to user.

**Proposal text** (`01_*` §3.4 + `03_*` §2.2): reflects FINAL substantive content. Optional 2-3 line dynamic-vs-static remark **available** but not required.

### D-4: ζ_*(graph, c) precise + c-dependence

- (Q1) Source: Phase 2 α (NQ-174 monkey-patch run); written up in `02_NQ174_zeta_star_results.md` §6 + `03_canonical_proposal_v5b_t_update.md` §3.2.
- (Q2) Subsequent cycles touching ζ_*:
  - Phase 4 F5 grid: parameter sweep at L ∈ {16, 20, 24}, c ∈ {0.10, 0.15} — confirms ζ_*(2D torus L=20, c=0.10) ≈ 0.40, no new dimensional generalization.
  - Phase 5-10 K-field architecture work: orthogonal to single-formation ζ_*.
  - Phase 9 U1 (K → ∞ shared pool): provides α plateau data; does not refine ζ_*.
- (Q3) **No Phase ≥ 4 change to ζ_* statement. FINAL.**

**Proposal text** (`03_canonical_proposal_v5b_t_update.md` §3.2): reflects FINAL. Ready for Block 1 review unchanged.

### D-5: V5b-T' new canonical entry

- (Q1) Source: Phase 3 E5 + E10 (`11_PN_unification.md` §3.1, `16_K2_baseline_and_zeta45_results.md` §2.5 R3a/R3b transition).
- (Q2) Subsequent cycles touching V5b-T':
  - Phase 4 F5 grid: c-eff(L) → 1 in continuum limit. Refines V5b-T' "PN-barrier-lifted Goldstone" claim with finite-L correction. Already incorporated into `20_*` Part 1 §1.2 statement.
  - Phase 5-10 dynamic-stability + K-field architecture work: orthogonal to V5b-T' static structural claim.
- (Q3) **Static V5b-T' structural claim FINAL.** Phase 3 mechanism + Phase 4 c_eff(L) numerical anchor stable.

**Proposal text** (`20_canonical_proposals_F10_F11.md` Part 1, lines 18-52): reflects FINAL. Ready for Block 1 review unchanged.

### D-6 (composite): Commitment 14-Multi extension

This is the **only proposal where Phase 9-10 substantively expands beyond the Phase 4 source**. SPLIT REQUIRED.

#### D-6a — STATIC σ_multi^A + σ_multi^D (Phase 4 baseline)

- (Q1) Source: Phase 4 F11 (`20_canonical_proposals_F10_F11.md` Part 2).
- (Q2) Substantive content of `20_*` Part 2 §2.2:
  - σ_multi^A = (F_total; {σ_j}; {σ_jk}) — static spectroscopic tuple.
  - σ_multi^D = orbit-type conjugacy class of joint stabilizer.
  - Reduction K=1 → single-formation Commitment 14.
  - Goldstone-pair instability formula μ_antisym ≈ μ_Gold − c_eff(L) · λ_rep with c_eff → 1 continuum.
- (Q3) Phase 5-10 changes:
  - Phase 5 P1.1: static instability ≠ dynamic instability — does **not affect static σ_multi structure**, only the dynamic interpretation. Could be added as 2-line clarifying note.
  - Phase 6-7 dynamic stability + LSW recovery: orthogonal to static σ_multi.
  - Phase 8-10 hybrid γ + CH: orthogonal to static σ_multi.

**STATIC framework FINAL.** Optional 2-line note "*static σ_multi structure ≠ dynamic instability under volume+simplex+box constraints, see Phase 6 R1.2*" can be appended.

**Proposal text** (`20_*` Part 2, lines 75-103): reflects FINAL for static layer. Ready for Block 1 review with optional 2-line remark.

#### D-6b — DYNAMIC σ_multi^A(t) trajectory (Phase 9-10 NEW)

This is **NEW substantive content** absent from `20_*` Part 2:

- Phase 8 T4 (`30_*`): proposes σ_multi^A(t) time-varying as **continuous interpolation between K-jump events**.
- Phase 9 U4 (`33_Phase9_findings_integration.md`): **simplified σ trajectory implemented numerically**. K-jumps detected (~6 events over t=200). Smooth-segment + jump structure confirmed.
- Phase 10 V3 (`34_Phase10_findings.md` §3): **Hessian-based σ_multi^A(t) at 10 snapshots**. K=8, n=400. Computational scaling: ~2s per Hessian sample. Results show lowest eigvals ≈ 0 (volume tangent) + 2.1-3.1 (bulk modes at ≈ 2β); **no exponentially-suppressed Goldstone observed** — consistent with corner-saturated regime per V5b-T'.
- Phase 10 V4: K-jump statistics Δt ∝ t^1.315.

These add **a dynamic time-trajectory layer** to σ_multi^A. The Phase 4 `20_*` Part 2 proposal text **does not contain** the dynamic layer. If user wishes D-6b in CV-1.5.1, the proposal text must be **augmented** with:

1. Definition of σ_multi^A(t) as time-evolving spectral tuple along K-field gradient flow trajectory.
2. K-jump event characterization (smooth-segment + jump structure).
3. Numerical anchor: V3 Hessian-based trajectory (K=8 T²_20) + V4 K-jump statistics.
4. Cat status: **Cat B sketch only** — full Hessian σ-tuple time series with rigorous K-jump theory remains unproved.

**Recommendation (per plan.md §3 Block 0.5)**: **DEFER D-6b to W6+**. Rationale:
- Phase 10 V3 used **simplified σ-tuple** (lowest 4 eigvals), not full Hessian σ-tuple per Commitment 14.
- K-jump theory at canonical level requires resolving "what σ-tuple does the K-1 formation inherit from the merged pair?" — not addressed.
- Full Hessian σ-tuple time-series analysis with rigorous derivation is still NQ-242 (carry to W6+).
- Cat B sketch is below the typical canonical Cat-A/Cat-B-target threshold for new Commitment-level extensions.

**If user disagrees with this recommendation** and wants D-6b in CV-1.5.1: ~20-30 lines additional text needed, drafting effort ~30 min within Block 1 budget.

---

## §3. D-6 SPLIT Recommendation Summary

| Sub-item | Phase source | Phase 9-10 changes | Recommendation |
|---|---|---|---|
| **D-6a** STATIC σ_multi^A + σ_multi^D | Phase 4 F11 | None (orthogonal) | **APPROVE** — proposal text FINAL |
| **D-6b** DYNAMIC σ_multi^A(t) trajectory | Phase 8 T4 + Phase 9 U4 + Phase 10 V3+V4 | NEW substantive layer | **DEFER to W6+** — needs full Hessian σ-tuple time series + K-jump theory rigorous |

This SPLIT is reflected in plan.md §3 Block 1 D-6a / D-6b distinction.

---

## §4. Actionability Summary (Block 1 input)

| Item | Status | Phase ≥ source change? | Action before Block 1 user review |
|---|---|---|---|
| D-1 Commitment 14 (O5') | FINAL | No | None — present as-is |
| D-2 Commitment 14 (O7) | FINAL | No | None — present as-is |
| D-3 V5b-F mechanism rider | FINAL (substantive) | No (static unchanged) | Optional 2-3 line static-vs-dynamic remark available; user decides |
| D-4 ζ_*(graph, c) | FINAL | No | None — present as-is |
| D-5 V5b-T' canonical entry | FINAL | No | None — present as-is |
| D-6a Commitment 14-Multi static | FINAL | No (Phase 5-10 orthogonal) | Optional 2-line static-vs-dynamic note available |
| D-6b Commitment 14-Multi dynamic | NEEDS UPDATE | YES — Phase 9-10 NEW layer | RECOMMEND DEFER; if user wants approve, need ~20-30 lines extra drafting |

**Block 1 user-decision queue is therefore READY** with the SPLIT presented. Default option matrix (per pre_brainstorm `2026-04-29` §2):
- **Recommended**: D-1, D-2, D-3, D-4, D-5, D-6a (defer D-6b) — ~250-310 canonical lines.
- **Conservative**: D-1, D-2, D-3, D-4 (defer D-5, D-6a, D-6b) — ~80-100 lines.
- **All-7**: D-1..D-6b — ~300-380 lines (requires D-6b text drafting).
- **Defer all**: 0 lines.

---

## §5. Hard Constraint Verification

- [x] canonical 직접 수정 0 — this file is reconciliation analysis only.
- [x] Silent resolution 0 — D-6b explicitly flagged as needing additional drafting if approved; not silently included.
- [x] No primitive override, no 4-term merging, no closure idempotence, no K dual-treatment.
- [x] No metastability without P-F flag — V3 trajectory analysis cited only spectrally, not thermodynamically.
- [x] No reductive equation — D-6b LSW connection cited as **correspondence**, not reduction (per CN10).

---

**End of 00_phase9_10_reconciliation.md.**
**Verdict: D-1..D-5 + D-6a proposal texts are FINAL (Phase ≥ source orthogonal or stable). D-6b is NEW Phase 9-10 layer — RECOMMEND DEFER to W6+.**
**Block 1 user-decision queue ready with 7-item SPLIT presentation.**
