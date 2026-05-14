---
type: working/reading-log
created: 2026-05-08
session: Session 7 (proof closure + canonical promotion)
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Proof-Promotion Reading Log

State at session start: **OMS-2.0 Conditional Accepted** with three sub-OPs.

## Documents reviewed (in mandated order)

1. `oms_2_0_promotion_audit.md` — Gate 7 of Session 6. Conservative classification verdict: Conditional Accepted because (i) H4 lacks closed-form, (ii) Σ_SN is PROOF SKETCH, (iii) pseudo-Δ³ ≠ full temporal.
2. `op_oms_001_gap_c1_rank_theorem.md` — RT1/RT2/RT3 PROVED conditional on H1, H2, H3. Reduction-C closure of $G_{\mathrm{cw}}$.
3. `op_oms_001_gap_c1_sensitivity.md` — Theorem S1: $J_e = -G_T^\top H_T^{-1} G_T$. **Subtle point:** rank equality $\mathrm{rank}\,J_e = \mathrm{rank}\,G_T$ used $H_T \succ 0$. If $H_T$ is only invertible (not PD), equality may fail — must restate.
4. `op_oms_001_gap_c1_genericity.md` — G1–G8 + GAP-C1, conditional on H4.
5. `op_oms_002_nontrivial_v.md` — $V_2$, $V_{2,\tau}$ admissible + nontrivial under H5.
6. `op_oms_026_sigma_branch_full.md` — SB5 codim-1 of $\Sigma_{ab}$ PROVED; SB7/SB8 codim-1 algebraic; SB9 PROOF SKETCH.
7. `op_oms_018_regular_u_star.md` — R1–R5 PROVED.
8. `op_oms_028_lipschitz_v.md` — L1 PROVED with explicit Lipschitz constant.
9. `open_problems.md` — current OP-OMS-001..034 statuses.
10. `audit_log.md` — AUDIT-024 super-entry; W18–W21 active.
11. `canonical_promotion_checklist.md` — v1.4 + OMS-2.0 Conditional final classification.
12. `canonical.md` — CV-1.11 with §13 Category A/B/C registry. No OMS appendix yet — will be inserted as Appendix OMS at file end.
13. VP-8 / VP-9 / VP-10 result MDs — only for **certification**, no exploration.

## Items I will sharpen (no broadening)

- **Theorem C1.2 fix:** restate rank equivalence with the correct hypothesis on $H_T$ (positive-definiteness, not just invertibility — needed because $-G_T^\top H_T^{-1} G_T$ being positive-semidefinite only follows when $H_T \succ 0$, which is exactly what gives second-order sufficiency for a strict local minimum).
- **Theorem C1.4 honest statement:** local rigidity, not unconditional global identity. Need extra structural assumption (vertex-fixing or face-preservation, both already provable from VP-3 / Prop CW1) to bridge from local to global.
- **Witness classification (OP-OMS-032):** use IEEE-double error bound × condition-number to argue **INTERVAL_CERTIFIED** for the low-cond witnesses. Magnitude > 0.05 with cond(H_T) < 100 ⇒ relative error ≤ 100 × eps ≈ 10^{-13} ≪ witness magnitude.
- **OP-OMS-033 fold theorem:** finite-dim fold (Crandall–Rabinowitz / Golubitsky–Schaeffer) directly applies; codim-1 conditional on quadratic nondegeneracy (which is generic).
- **OP-OMS-034:** explicitly separate static face from temporal Δ³; static does **not** require temporal.

## Target outcome

**OMS-2.0 Accepted — Static + Conditional Temporal**, with:
- All Gap C1 theorems cleanly stated and proved (with corrected hypotheses).
- H4 status: CLOSED UNDER CERTIFIED WITNESS (interval-certified via condition-number argument).
- Σ_SN: PROVED as conditional fold theorem.
- Temporal Δ³: separated; conditional on OP-OMS-034.
- Canonical.md gets Appendix OMS with precise labels.

If H4 closure cannot be argued rigorously, fall back to **OMS-2.0 Conditional Accepted — Static**.
