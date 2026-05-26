---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

> [!nav] Linked: [[MOC_AFD_0_foundation]] · [[THEORY_INDEX]]


# AFD-0 Work Log

Chronological work log for the AFD-0 development session.

---

## 2026-05-12 — AFD-0 initiated

### Repository reading (Layer-1 grounding)

Files read or grepped:

- `THEORY/2_substrate/canonical/canonical.md` (CV-1.13, 2377 lines; checked §3, §7, §8, §11, §13, §16 (D-ST-3, D-ST-4), Appendix OMS).
- `THEORY/2_substrate/canonical/theorem_status.md` (968 lines; checked Cat A/B/C/R counts, Open Problems Catalog, OP-0005 / OP-0008 / OP-0009 / OP-0021 statuses).
- `THEORY/2_substrate/canonical/hypothesis_tree.md` (HT-3.5, 355 lines; checked Q1–Q6 dependency block structure).
- `THEORY/2_substrate/Q3_dynamics/h_morse_packageII/06_packageII_dependency_map.md` (Package II requirements; H-MORSE-Local + H-MORSE-Saddle + EK prefactor formula confirmed).
- `THEORY/2_substrate/Q3_dynamics/h_morse_packageII/07_Eyring_Kramers_requirements.md` (EK form for SCC documented).
- `THEORY/2_substrate/foundations/dissolutions/soft_K_definition.md` (G1 K_soft definition; vineyard set V codim-1 confirmed; QM3 Lipschitz Cor 2.2 cited).
- `CODE/scc/diagnostics.py` (DiagnosticVector + Bind/Sep/Inside/Persist predicates; Sep = u-weighted distinction confirmed).
- `CODE/scc/multi.py` (K-field architecture; V1–V4 validity conditions; K_act = #PersComp post-hoc).
- `CODE/scc/k_soft.py` (K_soft = Σ φ(ℓ_i) implementation; phi_sat / phi_lin).
- `THEORY/2_substrate/INDEX.md` (working file navigation, Q1–Q6 organization).

Grepped for:

- "K_act" — confirmed Commitment 16 two-tier decomposition (K_field / K_act); D-ST-3 D-ST-4 stereo extension; T-K-Select-PF (Cat B) and T-K-Select-OBS (Cat B).
- "vineyard" — confirmed codim-1 semi-algebraic set V in `working/E/soft_K_definition.md` §2.3.
- "K-jump" — confirmed OP-0008 σ^A K-jump non-determinism (HIGH); referenced in CN6, OP-0009-K, sigma_multi_trajectory.md.

### Layer-1 Cat A facts identified for AFD-0 use

(All confirmed as Cat A in `theorem_status.md`.)

- T8-Core: non-trivial minimizer exists when β/α > 4 λ_2 / |W''(c)|.
- T14: Łojasiewicz gradient-flow convergence.
- T-Merge(b): K = 1 is global energy minimum.
- T-Persist-1(b): basin radius r_basin = sqrt(2 Δ_min / λ_max).
- T7-Enhanced: enhanced metastability Hessian gap.
- P-F-A1 Package I (T-PF-A1-AR/SDE/GI/PE, all Cat A as of CV-1.9).
- QM3 (K_soft Lipschitz on Σ_m).
- Commitment 16 (K_field / K_act two-tier).
- T-Temporal-Identity (CV-1.13, all 4 parts Cat A).
- Predicate-Energy Bridge (Sep = 1 − E_sep/m).
- CSEH 2007 bottleneck stability (external).

### Layer-3 facts identified (NOT used by AFD-0)

- H-MORSE-Local: Cat B target (CV-1.14, in progress).
- H-MORSE-Saddle: not yet registered.
- EK prefactor formula (Bovier-Eckhoff-Gayrard): literature-available, reflected-Langevin adaptation OPEN.

### Key decisions

1. **Layer architecture commitment.** AFD-0 = Layer 2, sitting between SCC Core (Layer 1) and Exact EK (Layer 3). The slogan "AFD separates transition order from transition rate; EK refines AFD" was adopted as the central canonical statement.

2. **Deterministic basin as default.** AFD-D2 = `B_det` (gradient-flow basin via T14). Stochastic variant AFD-D2' = `B_stoch` is offered but not default.

3. **Raw representatives, not equivalence classes.** AFD-D4 (equivalence class) is reserved for an optional refinement; AFD-0 uses raw representatives to avoid commitments about Goldstone families and Aut(G)-orbit identification.

4. **Set-theoretic K-strata only.** AFD-D12 explicitly warns that S_K is *not* claimed to be a smooth or Whitney stratum. Upgrade to genuine stratification is OP-AFD-002.

5. **ExitCost-based preorder, not pairwise C_AFD.** AFD-D14 / AFD-T6 use the scalar ExitCost to give a total preorder. The pairwise comparison C_AFD(F_i, F_j) ⋚ C_AFD(F_j, F_i) is explicitly *not* used as a preorder (no transitivity in general).

6. **C_AFD is a cost, not a metric.** Symmetry fails; triangle inequality fails. Stated explicitly in AFD-T5 properties + AFD-audit Q11.

7. **AFD-T8 is a Lemma Candidate (Conditional, Layer 3).** Not promoted to Theorem. Full proof routed through OP-AFD-005.

8. **AFD-T9 is the central architectural theorem.** Proved by inspection of definitions. This is the formal statement of "H-MORSE ∉ Layer 2."

### Unresolved gaps (carried to OP-AFD-001..010)

- (OP-AFD-001) Topology-signature continuity at vineyard set (needed for sharper AFD-T2).
- (OP-AFD-002) K_act stratification regularity (needed to upgrade AFD-D12 / AFD-T3 to genuine stratification).
- (OP-AFD-003) Existence of minimizing transition paths (attainment of inf in AFD-D7).
- (OP-AFD-004) Positive merge barrier analytic lower bound (replaces numerical exp38/exp60).
- (OP-AFD-005) FW-to-SCC refinement theorem (full proof of AFD-T8).
- (OP-AFD-006) Diagnostic coarse-graining and Markov / lumpability.
- (OP-AFD-007) Multi-formation K-field state graph extension.
- (OP-AFD-008) Topology-aware K-jump cost refinement.
- (OP-AFD-009) Connection to Conley index (AFD-1).
- (OP-AFD-010) Finiteness of V_form for generic parameters.

### Files written today

- `README.md` — overview and reading order.
- `abstract_formation_dynamics.md` — main document with 18 sections, AFD-D1..D15, AFD-T1..T10.
- `afd_theorem_registry.md` — tabular index of theorems with status and dependencies.
- `afd_open_problems.md` — OP-AFD-001..010.
- `afd_audit.md` — 20-question honesty audit + overclaim corrections.
- `afd_hmorse_reclassification.md` — formal H-MORSE reclassification document.
- `afd_examples.md` — 7 worked examples on small grids.
- `afd_framework_comparison.md` — 15-framework comparison table.
- `afd_log.md` (this file) — chronological work log.
- `afd_summary_for_next_agent.md` — compact handoff.
- `afd_layer_diagram.md` — ASCII three-layer diagram.

### Internal audit (post-write)

Reviewed `abstract_formation_dynamics.md` + `afd_audit.md`. Verified:

- No definition or theorem hidden-depends on H-MORSE (AFD-T9 by-inspection proof rechecked).
- All theorem labels correct (1 Theorem AFD-T2, 1 Theorem AFD-T5, 1 Theorem AFD-T9, 6 Propositions, 1 Lemma Candidate, 1 Design Principle).
- C_AFD is *never* called a metric. Warnings present in AFD-T5 and AFD-audit Q11.
- K-strata are *never* called smooth strata. Warnings present in AFD-D12, AFD-T3, AFD-audit Q6.
- H-MORSE reclassification (Layer 3, not Layer 2) is stated in §13 slogan 2 + `afd_hmorse_reclassification.md` formal claim + AFD-T9 corollary.

No revisions needed.

### Update to working index

`THEORY/2_substrate/INDEX.md` updated with AFD_0 entry (see `INDEX.md` patch).

---

## Carry-forward to next session

See `afd_summary_for_next_agent.md` for the compact handoff.

Top three suggested next actions:

1. **Prove OP-AFD-004 (positive merge barrier).** Use T7-Enhanced + T-Persist-1(b) to give an analytic lower bound c(β, n, G) > 0 for `C_K(K, K−1)`.
2. **Resolve OP-AFD-003 (infimum attainment).** Arzelà-Ascoli on rectifiable curves of bounded length in Σ_m compact; verify lower semicontinuity of Bar along the admissible class.
3. **External audit of AFD-0.** One round of independent review before any canonical promotion.

In parallel:

4. Pursue CV-1.14 (H-MORSE-Local Cat B) in `CV114_H_MORSE_PACKAGEII/`. This is *Layer 3* and unblocks AFD-T8.

---

## Session 2 — 2026-05-12 (W7 Day 2)

### Work done

1. **OP-AFD-004 Cat B resolved.** `op_afd_004_proof.md` written.
   - Strategy A (qualitative): basin-exit argument from T8-Core + T14 + T-Merge(b) Cat A. No H-MORSE.
   - Strategy B (quantitative): c_low = 0.0221β from T-Persist-1(b) Δ_core ≥ 0.0441β. Conditional on H1-H4+WS+SR.
   - exp38 re-run: barrier at β=50 is 23.5 (refined) / 37.2 (NEB). c_low = 1.1 — conservative factor ~21.

2. **AFD-T7 registry upgraded:** Lemma Candidate → Cat B Proposition (C_K(K,K-1) ≥ 0.0221β, conditional).

3. **OP-AFD-004 in afd_open_problems.md:** Marked "PARTIALLY RESOLVED (Cat B)". Sub-problems OP-AFD-004a/b/c registered.

### Files changed

- `op_afd_004_proof.md` — new (proof file, ~300 lines)
- `afd_theorem_registry.md` — AFD-T7 row + promotion section updated
- `afd_open_problems.md` — OP-AFD-004 section + cross-ref table updated
- `afd_log.md` — this entry

### Carry-forward

Next priority (W7 Day 3):
1. **M-A2 numeric verification** (Track A, CV-1.14 blocker): Stab_{Aut(G)}(u*) check on canonical 15×15 minimizer.
2. **AFD-0 external audit** (TeamCreate, 3 agents): definition / proof / overclaim reviewers.
3. **OP-AFD-003** (infimum attainment): Arzelà-Ascoli argument on rectifiable curves in Σ_m.
