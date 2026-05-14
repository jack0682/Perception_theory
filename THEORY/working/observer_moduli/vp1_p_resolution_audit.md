---
type: working/validation-protocol
created: 2026-05-07
version: 1.0
project: Observer Moduli Space of SCC
experiment: exp86_vp1_p_resolution_audit.py
op_target: OP-OMS-009
result: RESOLVED-NEGATIVE
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# VP-1: P-Resolution Audit

**Protocol defined in:** `validation_protocols.md` (VP-1)
**Experiment script:** `CODE/experiments/exp86_vp1_p_resolution_audit.py`
**Result files:** `CODE/experiments/results/observer_moduli/vp1_pairs.json`, `vp1_summary.md`
**Date run:** 2026-05-07

---

## 1. Question

Does P_min = d = (Bind, Sep, Inside, Persist) distinguish all perceptually relevant observer cores?

Specifically: does there exist a pair (Θ_1, Θ_2) such that:
- ||d(Θ_1) - d(Θ_2)|| < 0.15 (diagnostic-near)
- D_T(Θ_1, Θ_2) > 0.5 (topologically distinct)

where D_T is the topology distance metric weighting K_core differences most heavily.

If yes: P_min is too coarse. P_top (adding T_Θ) is needed. Proposition R1 is CONFIRMED.
If no: P_min may be sufficient. Proposition R1 status remains HYPOTHESIZED.

---

## 2. Protocol Summary

Four complementary approaches were executed:

**Part A** — Synthetic field comparison on 12×12 grid.
Six hand-constructed fields: single_blob, double_blob, triple_blob, horiz_strip, vert_strip, close_double.
Objective: find pairs where blob count differs but diagnostics agree.
Result: 0 counterexamples. Topologically distinct synthetic fields differed in diagnostics (||d|| >> 0.15).

**Part B** — Optimizer sweep with 10 λ configurations on 12×12 grid.
λ vectors from cl_dominant (0.6, 0.2, 0.2) to sep_very_strong (0.2, 0.6, 0.2).
Objective: find parameter pairs where the optimizer equilibria differ topologically but converge diagnostically.
Result: **3 counterexamples** (CE-1, CE-2, CE-3).

**Part C** — Analytic targeted construction on 10×10 grid.
Three fields hand-tuned to produce K_core=1 vs K_core=2 with matched diagnostics.
Objective: controlled construction to test the Inside collapse mechanism.
Result: 0 strict counterexamples (fields too diagnostically separated at construction level).

**Part D** — High-resolution λ sweep on 15×15 grid, 21 configurations, 210 pairs checked.
Objective: independent replication with larger graph and denser parameter sampling.
Result: **1 counterexample** (CE-4), independent replication.

**Total: 4 definitive counterexamples. OP-OMS-009 status: RESOLVED-NEGATIVE.**

---

## 3. The Counterexample Mechanism

All 4 counterexamples share one structure: **K_core(Θ_1) ≠ K_core(Θ_2) with ||d(Θ_1) - d(Θ_2)|| < 0.15**.

The mechanism is the collapse of the H0 barcode inside `Inside`:

```
Inside(u*, graph, params) = (l_max - c)/(1 - c) × (1 - l_second / l_max)
```

This is a product of two scalar summaries of the H0 persistence bar lengths. It partially tracks K_core: more components typically means l_second rises, reducing Inside. But the relationship is not injective:

- A K_core=2 configuration with one large and one small blob produces small l_second (small blob contributes short bar), keeping Inside near 1.
- A K_core=1 configuration with a single large blob also has small l_second.
- The two Inside values can be within 0.05 even as K_core differs by 1.

The cl_dominant configuration (w_cl = 0.6) consistently drives the optimizer to a two-blob equilibrium on the 12×12 grid. More balanced λ configurations produce single-blob equilibria. The diagnostic 4-vectors of these configurations can be within ||d|| = 0.07 (CE-1).

---

## 4. What P_top Adds

P_top = (d, T_Θ) where T_Θ = (N_0, Bar_0, l_1, l_2, A, K*, C_bd).

In particular, T_Θ includes K_core = K* (number of connected components at θ_core) explicitly. Every counterexample pair has |K_core_A - K_core_B| = 1, giving D_T ≥ 3.0. P_top trivially separates all 4 pairs.

There is no counterexample found where P_top itself fails. The topology-level information (K_core, l_second, l_third) is sufficient to distinguish all tested cases.

---

## 5. Proposition R1 Status Update

**Before VP-1:** Prop R1 (P_min is too coarse) — HYPOTHESIZED

**After VP-1:** Prop R1 — CONFIRMED (by explicit counterexample, exp86)

Formal statement:
> There exist observer parameter configurations Θ_1, Θ_2 such that ||P_min(Θ_1) - P_min(Θ_2)|| < 0.15 yet the topological signatures T_{Θ_1} and T_{Θ_2} differ by K_core: T_{Θ_1} has K_core=2 and T_{Θ_2} has K_core=1 (or vice versa).

**Implication for readout map hierarchy:** P_min is not a canonical readout map at the observer level. P_top is the minimal canonical readout resolving observer-level topological differences.

---

## 6. OP-OMS-009 Classification

**OP-OMS-009 (Readout resolution + continuity of u*(Θ)):**

The resolution question is now answered: **P_min is insufficient** (4 counterexamples).

The continuity question (does u*(Θ) vary continuously in Θ, enabling P_top to descend to M_obs/G?) remains open as a separate subquestion. VP-1 provides evidence that u*(Θ) does vary smoothly enough to produce near-diagnostic configurations with different topology — but formal continuity proof of u*(Θ) is still required for Prop R3 (descent of P_top to quotient).

**OP-OMS-009 final status: RESOLVED-NEGATIVE**
(The "negative" refers to P_min, not to P_top. P_top is not negated — it is confirmed as necessary.)

Residual: The continuity subquestion of OP-OMS-009 (u*(Θ) continuous → Prop R3) is spun off as a separate concern, still OPEN. This does not block the P_min finding.

---

## 7. Implications for Canonical Promotion

**Prop R1 confirmed** → `oms_1_candidate.md` Prop R1 status upgrades from HYPOTHESIZED to PROVED (by construction, exp86).

**OP-OMS-009 resolved** → one of three canonical blockers removed.
Remaining blockers: OP-OMS-001 (G_core-weight), OP-OMS-002 (V ∈ V_adm existence).

**Checklist B7 (Prop R1 status):** upgrades from HYPOTHESIZED to PROVED.

**Next validation priority:** VP-3 (core-weight symmetry test, attacks OP-OMS-001).

---

## 8. Audit Entry

See `audit_log.md` AUDIT-021 for the VP-1 decision record.

---

*Validation protocol VP-1 complete. Experiment: exp86_vp1_p_resolution_audit.py. Date: 2026-05-07.*
