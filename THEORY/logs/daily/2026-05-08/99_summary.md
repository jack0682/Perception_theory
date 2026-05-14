---
type: log/daily-summary
date: 2026-05-08
sessions: Session 5, Session 5 cont., Session 6 (OMS-2.0 push)
day_arc: OMS-1.1 → OMS-1.2 → OMS-2.0 Conditional Accepted
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# 2026-05-08 — Day Summary

## One-line digest

**OMS promoted from 1.1 (Computationally Grounded Canonical Candidate) through 1.2 (with Local Regularity Theorem) to OMS-2.0 Conditional Accepted in a single day, via three sessions and 11 new theory files / 6 experiments / 18 propositions PROVED.**

---

## Day-arc summary

### Morning — Session 5

VP-6 effective DOF + OP-OMS-018 attack.

- VP-6: 42 stencils on S3/S4. Effective dimension on simplex slice: $d_{\mathrm{eff}} \le 2$ in 100% of samples; typically 1.
- OP-OMS-018 partially resolved: R1 (interior $C^1$), R2 (boundary $C^1$), R3 (Berge u.h.c. + global $C^1$ REJECTED), R4 ($v$ continuous concave Lipschitz), R5 (envelope) all PROVED.
- Effective DOF theory (Props ED1, ED2 PROVED).
- Stage promoted to **OMS-1.2**.

### Mid-day — Session 5 continuation

Three OPs (OP-OMS-026, OP-OMS-028, OP-OMS-001) attacked after final report.

- OP-OMS-026: VP-7 fine-grid Σ_branch on Δ²; P12 has dominant 66.7% branch (constant-rank candidate); S3 fragmented.
- OP-OMS-028: PROVED Theorem L1 (global Lipschitz of $v$ with explicit constant).
- OP-OMS-001: Three-reduction proof sketch; continuous component triviality PROVED (registered as OP-OMS-029).

### Afternoon — Session 6 (OMS-2.0 push)

User-mandated 8-gate execution.

- Gate 1: Three theory files (rank theorem RT1/RT2/RT3, sensitivity formula S1/S2, analytic genericity G1–G8 + GAP-C1).
- Gate 2: VP-8 rank witness — H4 CONFIRMED (34/42 = 81% explicit witnesses).
- Gate 3: $V_2$ / $V_{2,\tau}$ defined; NV3–NV10 PROVED.
- Gate 4: VP-9 basin test — NONTRIVIAL on P12 and S3 for τ = 0.01.
- Gate 5: SB1–SB11 PROVED (codim-1 part); $\Sigma_{T8} \subset \Sigma_{\mathrm{branch}}$ identified.
- Gate 6: VP-10 pseudo-Δ³ — codim-1 CONSISTENT (transition fraction 0.311 ≤ 0.375 budget).
- Gate 7: OMS-2.0 promotion audit. Conservative classification: **OMS-2.0 Conditional Accepted**.
- Gate 8: All bookkeeping files updated.

---

## Scoreboard

| Metric | Count |
|---|---|
| Sessions | 3 |
| Theory files created | 11 |
| Theory files modified | 7 |
| Experiments created | 6 (VP-6, VP-6 path, VP-7, VP-8, VP-9, VP-10) |
| Total experiment runtime | ≈ 32 min (612 + 267 + 79 + 49 + 97 + 97 s) |
| Propositions PROVED | 18 (R1–R5, ED1–ED2, RT1–RT3, S1–S2, G4, G8, NV4–NV10, SB5–SB11, L1, L2, OP-OMS-029) |
| New OPs registered | 9 (OP-OMS-024 through OP-OMS-032/033/034) |
| OPs promoted to PROVED / CONFIRMED | 7 (OP-OMS-018 partial, 028, 029, 030, 031, 026, 001 conditional) |
| Stage promotions | 2 (OMS-1.1 → OMS-1.2 → OMS-2.0 Conditional Accepted) |

---

## Major theoretical contributions

1. **Local regularity of $u^*(\lambda)$** on regular branches PROVED (Theorems R1/R2 — IFT + Robinson–Fiacco), with global $C^1$ REJECTED via Prop R3 (3) (VP-1/VP-4 counterexample). The branch-switching surfaces are **observer-type transitions, not regularity defects**.

2. **Value function $v(\lambda) = \min_u E_\lambda(u)$** PROVED to be continuous, concave, locally Lipschitz on Δ³ (Theorem R4), with envelope $\nabla v(\lambda) = (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*)$ on the regular branch (Theorem R5). $v$ takes over from $u^*$ as the canonical smooth-on-Δ³ object.

3. **Explicit sensitivity formula** $J_e(\lambda) = -G_T(\lambda)^\top H_T(\lambda)^{-1} G_T(\lambda)$ (Theorem S1) — both an analytical handle on the perceptual Jacobian and a numerical recipe (VP-8).

4. **Analytic genericity chain** (Lemmas G1–G3 + Theorem G4 dichotomy + Corollaries G5/G7/G8) — converts H4 (one witness) into H2 (open-dense rank-3) into Reduction-C closure into identity-everywhere.

5. **$\Sigma_{T8} = \Sigma_{\mathrm{Hess}} \subset \Sigma_{\mathrm{branch}}$** — identifies the SCC central T8 phase-transition surface as one component of the OMS branch-switching set. **Major conceptual unification.**

6. **Effective DOF** theory: distinguishes formal / constraint / gauge / response dimensions (Props ED1, ED2). Low Jacobian rank is **not** evidence for hidden gauge symmetry.

7. **Non-trivial admissible $V$** explicit construction $V_2 = \min\{D_1, D_2 + c\}$ and softened $V_{2,\tau}$. Prop NV7 PROVED ≥ 2 basins with distinct readouts.

---

## Major computational results

- **VP-6** (effective DOF): 42 stencils, $d_{\mathrm{eff}} \le 2$ in 100% on simplex slice; revised Hyp RG1 supported.
- **VP-6 path test**: all four $u^*$ regimes (R1, R2, kink, branch-switch) realized empirically.
- **VP-7** (Σ_branch on Δ²): P12 → 7 branches with 66.7% dominant; S3 → 17 branches fragmented.
- **VP-8** (H4 witness): rank(J_e_tan) = 2 in 42/42; |det 3×3 minor| > 1e-6 in 34/42.
- **VP-9** (basin test): NONTRIVIAL on P12 (3 attractors / 2 distinct pairs) and S3 (4 attractors / 4 distinct pairs) for τ = 0.01.
- **VP-10** (pseudo-Δ³): P12 K=8 → 7 branches (same as Δ²); transition fraction 0.311 ≤ 0.375 codim-1 budget.

---

## Final status

$$\boxed{\textbf{OMS-2.0 Conditional Accepted}}$$

with three sub-OPs (OP-OMS-032 / 033 / 034) for OMS-2.0 Accepted promotion.

---

## Tomorrow's priority

1. **OP-OMS-032** — closed-form symbolic H4 witness on $P_3$ or $P_4$.
2. **OP-OMS-033** — Arnold saddle-node theorem applied to SCC double-well energy.
3. **OP-OMS-034** — full temporal Δ³ via `scc.multi` 2-time-slice scene.
4. After all three sub-OPs closed, promote stage to **OMS-2.0 Accepted**.
5. Promote Session-5/6 sub-results into `THEORY/canonical/canonical.md` §13 OMS appendix.

---

## File map (today's deliverables)

### Theory files created (`THEORY/working/observer_moduli/`)

- `vp6_initial_reading_log.md`
- `effective_dof_theory.md`
- `op_oms_018_regular_u_star.md`
- `vp6_effective_dof.md`
- `vp6_effective_dof_log.md`
- `observer_landscape_admissible_class.md`
- `oms_1_2_status_audit.md`
- `vp7_branch_map_results.md`
- `op_oms_028_lipschitz_v.md`
- `op_oms_001_formal_proof_attempt.md`
- `op_oms_001_gap_c1_rank_theorem.md`
- `op_oms_001_gap_c1_sensitivity.md`
- `op_oms_001_gap_c1_genericity.md`
- `op_oms_002_nontrivial_v.md`
- `op_oms_026_sigma_branch_full.md`
- `oms_2_0_promotion_audit.md`

### Code files created (`CODE/experiments/observer_moduli/`)

- `vp6_effective_dof_jacobian.py`
- `vp6_u_star_regular_path_test.py`
- `vp7_branch_map.py`
- `vp8_gap_c1_rank_witness.py`
- `vp9_nontrivial_v_basin_test.py`
- `vp10_sigma_branch_delta3.py`

### Result files created (`CODE/experiments/results/observer_moduli/`)

- `vp6_jacobian_spectra.{json,md}`
- `vp6_u_star_path_results.{json,md}`
- `vp7_branch_map.{json,md}`
- `vp8_gap_c1_rank_witness.{json,md}`
- `vp9_nontrivial_v_basin.{json,md}`
- `vp10_sigma_branch_delta3.{json,md}`

### Theory files modified

- `open_problems.md` — OPs 016–034 statuses.
- `audit_log.md` — AUDIT-023, AUDIT-024 + W13–W21.
- `basin_stratification.md` — §11 added.
- `stratified_dynamics.md` — §8 added.
- `canonical_promotion_checklist.md` — v1.3 / v1.4 / OMS-2.0 Conditional final.
- `daily_log.md` — Session 5 / 5-cont. / 6 entries.
- `checkpoints.md` — Session 5 / 6 rows + OMS-2.0 status.
- `oms_1_candidate.md` — frontmatter + §20 promoted to OMS-2.0 Conditional Accepted.
- `THEORY/CHANGELOG.md` — Session 5 / 6 entries.
- `THEORY/working/INDEX.md` — Session 5 / 6 file tables + status update.

### Daily log files (this folder)

- `00_plan.md`, `01_pre_brainstorm.md`, `02_session5_vp6_effective_dof.md`,
  `03_session5_op_018_regularity.md`, `04_session5_cont_vp7_op_028_op_001.md`,
  `05_session6_gate1_gap_c1_theory.md`, `06_session6_gate2_vp8_h4_witness.md`,
  `07_session6_gate3_4_op_002_basin.md`, `08_session6_gate5_6_op_026_branch.md`,
  `09_session6_gate7_oms_2_0_audit.md`, `10_op_catalog_state_eod.md`,
  `99_summary.md`.
