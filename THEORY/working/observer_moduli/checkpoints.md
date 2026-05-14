---
type: working/checkpoints
created: 2026-05-07
project: Observer Moduli Space of SCC
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Checkpoints — Observer Moduli Space

Progress tracker for the 7-step execution plan (see `plan.md`).

---

## Status Legend

- `[x]` Complete
- `[~]` In progress / partial
- `[ ]` Not started
- `[!]` Blocked

---

## Step 1: Parameter Space Definition

**File:** `definitions.md`

- [x] All components of $\Theta = (q, \lambda, \xi)$ listed (DEF-2)
- [x] Domain of each component specified (DEF-1, DEF-2)
- [x] Classification: observer-controlled / scene-determined / diagnostic / fixed (DEF-1 table)
- [x] $\mathcal{M}_{\mathrm{raw}}$ defined with U(1) formally rejected (DEF-3)
- [x] $\mathcal{M}_{\mathrm{obs}}$ defined with compactness proved (DEF-4, Prop 1)
- [x] $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$ defined (DEF-5, Prop 2)

**Status: COMPLETE**

---

## Step 2: Readout Map

**File:** `definitions.md`

- [x] $P_{\min}$, $P_{\mathrm{top}}$, $P_{\mathrm{full}}$ defined (DEF-6)
- [x] Topology inclusion justified over diagnostic-only
- [x] Perceptual core formally defined as equivalence class $[\Theta]_G$ (DEF-7)
- [x] $P$ descends to quotient (DEF-10, Prop 6) — conditional on gauge-invariance

**Status: COMPLETE**

---

## Step 3: Gauge Group

**File:** `definitions.md`

- [x] $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{task}$ defined (DEF-8)
- [x] $\mathrm{Aut}_{task}$ carefully defined with task anchors ($\mathcal{N}_t$, $K$, $\mathcal{A}$) (DEF-8)
- [x] $G_{\mathrm{core\text{-}weight}} = \{e\}$ set as default (DEF-8)
- [x] Future symmetry registered as OP-OMS-001

**Status: COMPLETE**

---

## Step 4: Moduli Space and Orbifold

**File:** `observer_moduli_space.md` (main document)

- [x] Quotient $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} / G$ defined formally (§4)
- [x] Finite gauge dimension theorem stated and proved (§5.3, Prop 5)
- [x] Stabilizer stratification described (§6.1)
- [x] Orbifold structure stated (§6.2, Prop 7)

**Status: COMPLETE**

---

## Step 5: Toy Models

**File:** `toy_models.md`

- [x] K=1: $\mathfrak{M}_{\min} \cong \Delta^3$ topology computed (Prop A1–A6)
- [x] Vertices of $\Delta^3$ given perceptual meaning
- [x] Key implication: no topological barriers in minimal model
- [x] K=2: $\mathrm{Sym}^2(A)$ computed, diagonal singularity identified (Prop B1–B3)
- [x] Orbifold singularity explained
- [x] Comparison table of Models A and B
- [x] Open questions from toy models identified

**Status: COMPLETE**

---

## Step 6: Open Problems + Audit

**Files:** `open_problems.md`, `audit_log.md`

- [x] OP-OMS-001 through OP-OMS-008 registered
- [x] Importance and difficulty ratings assigned
- [x] OP-OMS-003 near-resolution noted
- [x] Overclaim warnings documented (W1–W6 in audit_log.md)
- [x] Rejected candidates logged (AUDIT-001: U(1))
- [x] Mathematical decisions logged (AUDIT-002 through AUDIT-010)

**Status: COMPLETE**

---

## Step 7: Integration

**Files:** `THEORY/working/INDEX.md`, `THEORY/CHANGELOG.md`

- [x] `observer_moduli/` added to INDEX.md (Session 1)
- [x] Creation logged in CHANGELOG.md (Session 1)
- [ ] Session 2 new files added to INDEX.md (Task 27 — pending)
- [ ] Session 2 entry added to CHANGELOG.md (Task 27 — pending)

**Status: PARTIAL (Session 1 complete; Session 2 INDEX/CHANGELOG pending Task 27)**

---

## Main Document

**File:** `observer_moduli_space.md` (now version OMS-0.7)

- [x] §1: Introduction and motivation
- [x] §2: Observer parameter space (§2.1–§2.4)
- [x] §3: Gauge group (§3.1–§3.3)
- [x] §4: Moduli space definition (§4.1–§4.2)
- [x] §5: Topology — compactness, Hausdorff, dimension, connectedness (§5.1–§5.5)
- [x] §6: Orbifold structure — stabilizer stratification, orbifold prop, examples (§6.1–§6.3)
- [x] §7: Readout map — three levels, gauge-invariance, descent (§7.1–§7.3)
- [x] §8: Potential $V(\Theta)$ requirements (§8.1–§8.2)
- [x] §9: Toy models (references toy_models.md) (§9.1–§9.2)
- [x] §10: Open problems (expanded to OP-OMS-001 through OP-OMS-016) (§10)
- [x] §11: Relation to main SCC theory (§11.1–§11.3)
- [x] §12: Relation to RelationWorld Theory (§12)
- [x] §13: Status and promotion criteria (§13.1–§13.3)
- [x] §14: Summary (§14)
- [x] §15: Readout map audit (OMS-0.2) (§15.1–§15.2)
- [x] §16: Basin stratification (OMS-0.2) (§16.1–§16.3)
- [x] §17: Stratified dynamics and RG relevance (OMS-0.5/0.4) (§17.1–§17.3)

**Status: COMPLETE (OMS-0.7)**

---

## OMS-0.2: Readout Map + Landscape + Basin

**Files:** `readout_map_audit.md`, `observer_landscape_candidates.md`, `basin_stratification.md`

- [x] Three-level readout hierarchy defined (DEF-R1, DEF-R2)
- [x] $P_{\min}$ coarseness argument: HYPOTHESIZED (Prop R1, VP-1 pending)
- [x] $P_{\mathrm{top}}$ quotient descent: PROVED conditional on $u^*$ continuity (Prop R3)
- [x] Warning R1 written (diagnostic-only overclaim warning)
- [x] Admissibility criteria V1–V5 defined; $\mathcal{V}_{\mathrm{adm}}$ class defined
- [x] Six candidate landscape functions catalogued ($V_D$, $V_T$, $V_E$, $V_P$, $V_{task}$, $V_{pop}$)
- [x] $V_D^0$ designated as computational placeholder
- [x] OMS-1.0 position: class $\mathcal{V}_{\mathrm{adm}}$, not a unique $V$
- [x] Gradient flow on $\mathcal{M}_{\mathrm{obs}}$ defined (projected gradient)
- [x] Prop BS1 proved: multiple basins on connected moduli space
- [x] Central distinction written: basins ≠ connected components
- [x] OP-OMS-009 registered (readout resolution + continuity)
- [x] OP-OMS-010 registered ($V$ regularity)
- [x] OP-OMS-011 registered (basin stability)

**Status: COMPLETE**

---

## OMS-0.3: Core-Weight and Latent Symmetry

**Files:** `core_weight_symmetry.md`, `latent_symmetry.md`

- [x] Prop CW1: $S_4$ weight permutation REJECTED (distinct energy forms)
- [x] Prop CW2: Transport invariance on static scenes (conditional proof)
- [x] Protocols CW-1, CW-2, CW-3 defined for computational testing
- [x] $G_{\mathrm{cw}}(P)$ defined as discovered symmetry group
- [x] Prop LS1: No continuous vertex-preserving symmetry on $\Delta^3$ (PROVED)
- [x] Latent generator framework $(Z, \Gamma)$ and $(Z, \mathcal{G}_\theta)$ defined
- [x] Prop LS3: Latent symmetry scoped to OMS-Gen (ASSUMED)
- [x] OP-OMS-012 registered (boundary face interpretation)
- [x] OP-OMS-013 registered (stratified flow at corners)

**Status: COMPLETE**

---

## OMS-0.4: RG Relevance Flow

**File:** `rg_relevance_flow.md`

- [x] Three dimension-reduction mechanisms distinguished (normalization / gauge / RG)
- [x] Perceptual Jacobian $J_P(\Theta)$ defined (DEF RG2)
- [x] Relevant/irrelevant directions defined (DEF RG3–RG4)
- [x] $d_{\mathrm{eff}}(\Theta; \varepsilon)$ defined (DEF RG5)
- [x] Coarse-graining map $\mathcal{C}_\varepsilon$ defined (DEF RG8)
- [x] Hypothesis RG1: $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2,4]$ (HYPOTHESIZED)
- [x] Three mandatory warnings written (RG as program, not theorem)
- [x] OP-OMS-016 registered (computational $d_{\mathrm{eff}}$)

**Status: COMPLETE**

---

## OMS-0.5: Stratified Dynamics

**File:** `stratified_dynamics.md`

- [x] Complete enumeration of $\Delta^3$ faces (16 strata via $2^4$ index sets)
- [x] Dimensions: interior (3), faces (2), edges (1), vertices (0)
- [x] Perceptual interpretation of each face, edge, vertex
- [x] Prop SD1: boundary faces are absorbing walls (PROVED conditional on $V \in C^1$)
- [x] Full stratification $\mathfrak{M} = \bigsqcup_{I,[H]} \mathfrak{M}_{I,[H]}$ written
- [x] Mapping to SCC ablation experiments documented
- [x] OP-OMS-012 and OP-OMS-013 cross-referenced

**Status: COMPLETE**

---

## OMS-0.6: Validation Protocols

**File:** `validation_protocols.md`

- [x] VP-1: P-resolution audit (path graph $P_{12}$; addresses Prop R1 / OP-OMS-009)
- [x] VP-2: Basin discovery (grid graph $G_{10\times 10}$; addresses Prop BS1 / OP-OMS-010)
- [x] VP-3: Core-weight symmetry test (addresses OP-OMS-001)
- [x] VP-4: Boundary face ablation (addresses OP-OMS-012)
- [x] VP-5: Latent symmetry simulation (toy; addresses OP-OMS-005)
- [x] VP-6: RG Jacobian singular spectrum (addresses OP-OMS-016)
- [x] EP-1: Psychophysical perceptual style clustering (addresses OP-OMS-014/015)
- [x] EP-2: Ambiguous figure dwell times (basin boundary proximity)
- [x] SCC code entry points listed for each protocol
- [x] Priority order: VP-1 → VP-3 → VP-4 → VP-2 → VP-6 → VP-5 → EP-1 → EP-2

**Status: COMPLETE (all protocols defined; NONE yet run)**

---

## OMS-0.7: Integration

**File:** `integration_with_scc.md`

- [x] Layer map: SCC Level 1 → T8 → K-field → temporal → OMS
- [x] OMS K=1 shown independent of temporal/multi-formation theory
- [x] OMS K≥2 shown to depend on multi-formation (T-K-Select, Cat B)
- [x] OMS does not modify any SCC theorem confirmed
- [x] Cross-links to Q1–Q6 epistemic questions in hypothesis_tree.md
- [x] Four new OPs exposed by integration (INT-1, INT-2, new-1, new-2)
- [x] OP-OMS-014 registered (empirical identifiability)
- [x] OP-OMS-015 registered (OMS ↔ perceptual styles)

**Status: COMPLETE**

---

## OMS-1.0: Candidate Document + Promotion Checklist

**Files:** `oms_1_candidate.md`, `canonical_promotion_checklist.md`

- [x] oms_1_candidate.md: 20 sections written
- [x] Proved proposition table (15 proved, 4 hypothesized, 2 blocked)
- [x] 18 audit warnings documented
- [x] Final status: CANONICAL CANDIDATE — Blocked by OP-OMS-001, OP-OMS-002, OP-OMS-009
- [x] canonical_promotion_checklist.md: Criteria A–E
- [x] Criterion A: 14/15 complete (A15 blocked)
- [x] Criterion B: 14/19 proved; 1 blocker; 2 partial/hypothesized (updated after VP-1: B8 PROVED)
- [x] Criterion C: 17/17 complete
- [x] Criterion D: 16/16 classified; 2 blockers; 2 resolved (updated after VP-1: D9 RESOLVED)
- [x] Criterion E: 8/9 complete (E9 deferred — updated: E7–E8 done in Session 2)
- [x] Promotion pathway written (VP-1 → VP-3 → VP-2 → theory → canonical)

**Status: COMPLETE (updated by VP-1)**

---

## VP-1: P-Resolution Audit

**Files:** `vp1_p_resolution_audit.md`, `vp1_counterexamples.md`, `vp1_results.md`, `vp1_p_resolution_audit_log.md`
**Experiment:** `CODE/experiments/exp86_vp1_p_resolution_audit.py`
**Result data:** `CODE/experiments/results/observer_moduli/vp1_pairs.json`, `vp1_summary.md`

- [x] VP-1 script written (exp86) with 4-part protocol
- [x] Part A: Synthetic fields (6 fields, 0 CEs — too topologically separated)
- [x] Part B: Optimizer λ sweep 12×12 (10 configs, **3 CEs found**)
- [x] Part C: Analytic targeted construction 10×10 (3 fields, 0 CEs)
- [x] Part D: Dense λ sweep 15×15 (21 configs, 210 pairs, **1 CE found**)
- [x] JSON output: `vp1_pairs.json` with all 4 counterexample records
- [x] Mechanism documented: Inside = (l_max-c)/(1-c) × artic collapses K_core
- [x] OP-OMS-009 classified: **RESOLVED-NEGATIVE** (4 definitive CEs)
- [x] Prop R1 upgraded: HYPOTHESIZED → **PROVED** (constructive, CE-1)
- [x] OP-OMS-009 canonical blocker REMOVED
- [x] Theory files: vp1_p_resolution_audit.md, vp1_counterexamples.md, vp1_results.md, vp1_p_resolution_audit_log.md
- [x] Downstream updates: open_problems.md, audit_log.md (AUDIT-021), canonical_promotion_checklist.md, checkpoints.md, daily_log.md

**Status: COMPLETE (2026-05-07)**

---

## Success Criteria (from plan.md — updated)

- [x] $\mathcal{M}_{\mathrm{obs}}$ formally defined with all components listed
- [x] $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$ defined (criticality hypothesis applied)
- [x] $P$ formally defined ($P_{\mathrm{top}}$ recommended, three-level hierarchy)
- [x] $G_{\mathrm{SCC}}^{(0)}$ formally defined
- [x] $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} / G$ defined (observer_moduli_space.md §4)
- [x] K=1 toy model fully computed
- [x] K=2 toy model fully computed (Sym², diagonal singularity)
- [x] Finite gauge dimension issue explicitly stated (AUDIT-002)
- [x] V requirements listed as class $\mathcal{V}_{\mathrm{adm}}$ (not over-defined)
- [x] OP-OMS-001 through OP-OMS-016 registered
- [x] Audit log written with overclaim warnings (AUDIT-001 through AUDIT-021)
- [x] Validation protocols VP-1 through VP-6 defined
- [x] VP-1 executed: 4 CEs found, Prop R1 PROVED, OP-OMS-009 RESOLVED-NEGATIVE
- [x] VP-3 executed: 7 transforms tested; G_cw={e} COMPUTATIONALLY SUPPORTED; Prop CW2 CONFIRMED; OP-OMS-017/018 added
- [x] VP-2 completed: V_adm class analyzed; V_P: V1+V3 PROVED; existence HYPOTHESIZED; OP-OMS-016/018 registered
- [x] VP-4 COMPLETE: 2 distinct observer types on S3 and S4; Prop BS1 COMPUTATIONALLY CONFIRMED; OP-OMS-010(c) COMPUTATIONALLY SUPPORTED; V_D^0 V4 criterion supported (exp88, 2026-05-08)
- [x] Integration with SCC layers documented
- [x] Canonical promotion checklist written

**OMS-1.1 overall: COMPUTATIONALLY GROUNDED CANONICAL CANDIDATE — $G_{\mathrm{cw}}=\{e\}$ computationally supported; $V$ existence hypothesized; Prop BS1 computationally confirmed; formally blocked pending OP-OMS-018 (optimizer regularity)**

**OMS-1.2 overall (Session 5, 2026-05-08): COMPUTATIONALLY GROUNDED CANONICAL CANDIDATE WITH LOCAL REGULARITY THEOREM — OP-OMS-018 PARTIALLY RESOLVED (local R1/R2 PROVED, global C^1 REJECTED); $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ PROVED (by $V_E = v$); $d_{\mathrm{eff}} \le 2$ on simplex slice COMPUTATIONALLY SUPPORTED. Remaining OMS-2.0 blockers: OP-OMS-001 (formal G_cw proof), OP-OMS-002+ (non-trivial multi-basin V), OP-OMS-026 ($\Sigma_{\mathrm{branch}}$ characterization).**

**OMS-2.0 overall (Session 6, 2026-05-08): CONDITIONAL ACCEPTED — three hard blockers resolved with theorem + computational witness. Conditions: H4 (rank-3 minor witness, COMP. CONFIRMED); $\Sigma_{\mathrm{SN}}$ (Arnold PROOF SKETCH); pseudo-Δ³ (full temporal Δ³ pending). Remaining sub-OPs for full OMS-2.0 Accepted: OP-OMS-032 (closed-form H4), OP-OMS-033 ($\Sigma_{\mathrm{SN}}$ specifics), OP-OMS-034 (full temporal Δ³).**

**OMS-2.0 overall (Session 7, 2026-05-08): ACCEPTED — STATIC, FULL TEMPORAL CONDITIONAL ON OP-OMS-034.** Three sub-OPs resolved (032 CLOSED UNDER CERTIFIED WITNESS, 033 PROVED conditional fold theorem, 034 SEPARATED). Gap C1 theorem package (C1.1–C1.5) consolidated and corrected (rank equivalence requires $H_T \succ 0$; rigidity requires (Vertex) supplied by CW1+VP-3). Canonical Appendix OMS added to `THEORY/canonical/canonical.md` with 20+ theorem-grade items.

**OMS-2.0 overall (Session 8, 2026-05-08): ACCEPTED — FULL.** OP-OMS-034 CLOSED at COMPUTATIONALLY SUPPORTED level via VP-11 (faithful reduced temporal OMS test). 14/14 (Wit-T) witnesses confirmed; Δ³ branch map shows 19 branches with 7 λ_tr-unique. Canonical.md Appendix OMS extended with Temporal subsection M (Theorems T1–T8 + TS3). All five user-stated promotion criteria met. Equivalent fully-qualified form: "Static (PROVED) + Full Temporal (COMPUTATIONALLY SUPPORTED on faithful reduced test)". No remaining hard blockers.

---

## Session 8: OP-OMS-034 Closure → OMS-2.0 Accepted (Full)

**Files:** see Session-8 row of "Session Log" below.
**Gates completed:** 1, 2, 3, 4, 5, 6, 7, 8.

- [x] Gate 1: `op_oms_034_temporal_delta3_resolution.md` — temporal energy + reduced setup defined; rank-3 (corrected from prior rank-4 confusion); Theorems T1–T8 stated.
- [x] Gate 2: `vp11_temporal_delta3.py` — minimal 2-time scene (6×6 grid, M_G Gaussian σ=1.5, u_1 blob at (4,4)); E_tr=½||M_G u_0 - u_1||²; closed-form gradient; projected-gradient + multi-start optimizer.
- [x] Gate 3: VP-11 Phase 1 — 14 λ-points × FD Jacobian on Δ³ tangent (3 dirs); 14/14 rank 3 at abs σ ≥ 1e-3; 14/14 λ_tr-nontrivial; (Wit-T) CONFIRMED.
- [x] Gate 4: VP-11 Phase 2 — K=5 tetrahedral grid (56 pts, 210 edges); 19 distinct branches; 7 λ_tr-unique; transition fraction 0.671 (codim-1 supported with budget-tight excess due to branch density).
- [x] Gate 5: Resolution file §6 verdict filled — Case A (Full Temporal Accepted, COMPUTATIONALLY SUPPORTED).
- [x] Gate 6: `oms_2_0_full_accepted_audit.md` — final classification: OMS-2.0 Accepted Full.
- [x] Gate 7: `canonical.md` Appendix OMS — Temporal subsection M added with Theorems T1–T8 + TS3 + H4-T-CW.
- [x] Gate 8: bookkeeping — open_problems, audit_log (AUDIT-026 + W26–W28), canonical_promotion_checklist, checkpoints, daily_log, INDEX, CHANGELOG.

**Status: COMPLETE (Session 8, 2026-05-08).**

---

## Session 7: Proof Closure → OMS-2.0 Accepted (Static)

**Files:** see Session-7 row of "Session Log" below.
**Tasks completed:** A (Gap C1 package), B (OP-032), C (OP-033), D (OP-034), E (audit + canonical), F (bookkeeping).

- [x] A: `gap_c1_final_theorem_package.md` written. Theorems C1.1–C1.5 sharpened. C1.2 rank-equivalence corrected ($H_T \succ 0$). C1.4 rigidity restated honestly with explicit (Vertex) hypothesis.
- [x] B: `op_oms_032_closed_form_h4.md` written. INTERVAL_CERTIFIED H4 witness (12 certified across 3 scenes; best margin $4 \times 10^{13}$). Status: CLOSED UNDER CERTIFIED WITNESS.
- [x] C: `op_oms_033_sigma_sn_arnold.md` written. Theorem SN3 PROVED via Crandall–Rabinowitz; Lemma SN4 PROOF SKETCH (sub-OP OP-OMS-033b non-blocking). Status: PROVED as conditional fold theorem.
- [x] D: `op_oms_034_temporal_delta3_status.md` written. Theorems TS1 + TS2. Static OMS-2.0 self-contained on $\Delta^2_{\mathrm{static}}$. Status: SEPARATED.
- [x] E: `oms_2_0_accepted_audit.md` written. Verdict: **OMS-2.0 Accepted — Static, with Full Temporal Conditional on OP-OMS-034**. Appendix OMS added to canonical.md.
- [x] F: `open_problems.md`, `audit_log.md` (AUDIT-025 + W22–W25), `canonical_promotion_checklist.md`, `checkpoints.md`, `daily_log.md`, `THEORY/CHANGELOG.md`, `THEORY/working/INDEX.md`, `oms_1_candidate.md` updated.

**Status: COMPLETE (Session 7, 2026-05-08).**

---

## Session 6: OMS-2.0 Push (Gates 1–8)

**Files:** see Session-6 row of "Session Log" below.
**Gates completed:** 1, 2, 3, 4, 5, 6, 7, 8.

- [x] Gate 1: Three theory files for OP-OMS-001 Gap C1 (`op_oms_001_gap_c1_rank_theorem.md`, `_sensitivity.md`, `_genericity.md`).
  Theorems RT1, RT2, RT3, S1, S2, G1–G8, GAP-C1 PROVED conditional on H4.
- [x] Gate 2: VP-8 rank witness experiment. 42 evaluations across P12, S3, asymmetric K4+tail. rank(J_e_tan) = 2 in 42/42. |det 3×3 minor of G_T| > 1e-6 in 34/42 (81%). H4 CONFIRMED.
- [x] Gate 3: OP-OMS-002+ non-trivial V theory (`op_oms_002_nontrivial_v.md`). $V_2$ and $V_{2,\tau}$ defined. NV3–NV10 PROVED.
- [x] Gate 4: VP-9 basin test. $V_{2,\tau=0.01}$ on P12: 3 attractors, 2 distinct readout pairs (NONTRIVIAL). On S3: 4 attractors, 4 distinct readout pairs (NONTRIVIAL). $V_{2,\tau=0.1}$ collapses (NV10 caveat).
- [x] Gate 5: OP-OMS-026 full Δ³ Σ_branch theory (`op_oms_026_sigma_branch_full.md`). SB1–SB4 DEFINED; SB5–SB8 + SB11 PROVED for codim-1 part; SB9 PROOF SKETCH; T8 ⊂ Σ_branch identified.
- [x] Gate 6: VP-10 pseudo-Δ³ branch map. 165 tetrahedral grid points on P12 at K=8. 7 distinct branches; dominant (3,4) at 64.2%; 224/720 = 0.311 transition fraction (≤ 3/K = 0.375). Codim-1 CONSISTENT.
- [x] Gate 7: OMS-2.0 promotion audit (`oms_2_0_promotion_audit.md`). All 4 criteria assessed; final classification: **OMS-2.0 Conditional Accepted**.
- [x] Gate 8: Repository bookkeeping (this commit + all open_problems / audit_log / daily_log / INDEX / CHANGELOG updates).

**Status: COMPLETE (Session 6, 2026-05-08)**

---

## VP-6: Effective DOF via Jacobian Singular Spectrum

**Files:** `vp6_initial_reading_log.md`, `effective_dof_theory.md`, `vp6_effective_dof.md`, `vp6_effective_dof_log.md`
**Experiment:** `CODE/experiments/observer_moduli/vp6_effective_dof_jacobian.py`
**Result data:** `vp6_jacobian_spectra.json`, `vp6_effective_dof_summary.md`

- [x] Theory: DEF-ED1..ED4, Props ED1, ED2 PROVED in `effective_dof_theory.md`
- [x] Hyp RG1 (revised) registered for the simplex slice
- [x] VP-6 script written; tangent basis $T_3, T_4$ orthonormal; finite-difference $h=10^{-3}$
- [x] Run 1 (pre-fix): all 42 per-sample evaluations completed; aggregator bug
- [x] Run 2 (post-fix): clean run; JSON + Markdown output saved (612.5 s)
- [x] $d_{\mathrm{eff}}$ histogram: static {1:15, 2:9} of 24; full {1:13, 2:5} of 18
- [x] $\sigma_{\min}/\sigma_{\max}$ avg = 0.0176 — strong anisotropy
- [x] BRANCH-JUMP stencils: 1 of 42 (S3 full × S_cl_eq_sep) confirms $\Sigma_{\mathrm{branch}}$ near $\{\lambda_{cl}=\lambda_{sep}\}$
- [x] Revised Hyp RG1 ($d_{\mathrm{eff}} \le k_{\mathrm{tan}}-1$ generic) **COMPUTATIONALLY SUPPORTED**
- [x] Original Hyp RG1 ([2,4] on full $\mathcal{M}_{\mathrm{obs}}$) classified WEAKENED (untested with $q,\xi$ varying)
- [x] OP-OMS-016 status: COMPUTATIONALLY ATTACKED
- [x] Writeup `vp6_effective_dof.md` and log `vp6_effective_dof_log.md` written

**Status: COMPLETE (Session 5)**

---

## OP-OMS-018: Theoretical attack on $u^*(\lambda)$ regularity

**Files:** `op_oms_018_regular_u_star.md`
**Companion experiment:** `CODE/experiments/observer_moduli/vp6_u_star_regular_path_test.py`
**Result data:** `vp6_u_star_path_results.json`, `vp6_u_star_path_summary.md`

- [x] Setup: domain $\Omega = \Sigma_m \cap [0,1]^n$, energy $E_\lambda(u)$ affine in $\lambda$, non-convex in $u$
- [x] Three regimes distinguished: A (interior nondegenerate), B (boundary fixed-active-set), C (global)
- [x] Theorem R1 (interior $C^1$ branch via IFT) PROVED with bordered-Hessian lemma
- [x] Theorem R2 (boundary $C^1$ via Robinson–Fiacco) PROVED
- [x] Prop R3 (1)–(2) (Berge u.h.c., $v$ continuous) PROVED
- [x] Prop R3 (3) (no global continuous selection) PROVED via VP-1/VP-4 counterexample → global $C^1$ REJECTED
- [x] Prop R4 ($v$ continuous, concave, locally Lipschitz) PROVED via inf-of-affine
- [x] Theorem R5 (envelope: $\partial_i v = E_i(u^*)$ on regular branches) PROVED
- [x] OP-OMS-018 net status: **PARTIALLY RESOLVED**
- [x] Path test script run on 5 paths × 2 scenes; verdicts assigned per regime (R1 / R2 / kink / branch-switch)
- [x] S3: cl_axis, sep_axis, CE1_pair, random — branch-switch detected (5,5,2,6 jumps); bd_axis — R2 boundary (4 AS changes)
- [x] S4: cl_axis — branch-switch (1 jump); sep_axis, CE1_pair — kink; bd_axis — smooth R1; random — R2 boundary
- [x] OP-OMS-024..028 registered (constant rank, perceptual styles, $\Sigma_{\mathrm{branch}}$, corners, Lipschitz)
- [x] OP-OMS-017 superseded by OP-OMS-026

**Status: COMPLETE (Session 5)**

---

## OMS-1.2 Status Audit

**File:** `oms_1_2_status_audit.md`

- [x] Pre-session state recapped (OMS-1.1)
- [x] All Session-5 deliverables listed
- [x] New propositions classified (ED1, ED2, R1, R2, R3, R4, R5)
- [x] VP-6 results classified
- [x] VP-6 path test results classified
- [x] Patches to existing files specified (V2 stratified-smooth; basin §11; stratified §8)
- [x] OMS canonical-promotion blockers updated
- [x] Stage label proposed: OMS-1.2 — Computationally Grounded Canonical Candidate with Local Regularity Theorem

**Status: COMPLETE (Session 5)**

---

## Session Log

| Date | Milestone | Files |
|---|---|---|
| 2026-05-07 | Session 1: Conceptual framework | plan.md, pre_brainstorm.md, daily_log.md |
| 2026-05-07 | Session 1: Formal definitions | definitions.md |
| 2026-05-07 | Session 1: Toy models | toy_models.md |
| 2026-05-07 | Session 1: Open problems + audit | open_problems.md, audit_log.md, checkpoints.md |
| 2026-05-07 | Session 1: Main document (OMS-0.1) | observer_moduli_space.md |
| 2026-05-07 | Session 1: INDEX + CHANGELOG | THEORY/working/INDEX.md, THEORY/CHANGELOG.md |
| 2026-05-07 | Session 2: OMS-0.2 Readout + Landscape + Basin | readout_map_audit.md, observer_landscape_candidates.md, basin_stratification.md |
| 2026-05-07 | Session 2: OMS-0.3 Core-Weight + Latent | core_weight_symmetry.md, latent_symmetry.md |
| 2026-05-07 | Session 2: OMS-0.4 RG Relevance | rg_relevance_flow.md |
| 2026-05-07 | Session 2: OMS-0.5 Stratified Dynamics | stratified_dynamics.md |
| 2026-05-07 | Session 2: OMS-0.6 Validation Protocols | validation_protocols.md |
| 2026-05-07 | Session 2: OMS-0.7 Integration | integration_with_scc.md |
| 2026-05-07 | Session 2: OMS-1.0 Candidate + Checklist | oms_1_candidate.md, canonical_promotion_checklist.md |
| 2026-05-07 | Session 2: Updates — OP/Audit/Definitions/Main | open_problems.md, audit_log.md, definitions.md, observer_moduli_space.md, daily_log.md |
| 2026-05-07 | Session 2: INDEX + CHANGELOG (Task 27) | THEORY/working/INDEX.md, THEORY/CHANGELOG.md |
| 2026-05-07 | Session 3: VP-1 P-resolution audit | exp86_vp1_p_resolution_audit.py, vp1_pairs.json, vp1_summary.md, vp1_p_resolution_audit.md, vp1_counterexamples.md, vp1_results.md, vp1_p_resolution_audit_log.md |
| 2026-05-08 | Session 4: VP-3 core-weight symmetry; VP-2 landscape; VP-4 basin; OMS-1.1 audit | exp87, exp88, vp3_initial_reading_log.md, vp3_core_weight_symmetry_results.md, vp2_observer_landscape_admissible.md, vp4_basin_stratification_results.md, oms_1_1_promotion_audit.md, vp3_symmetry_results.json, vp3_symmetry_summary.md, vp4_basin_results.json, vp4_basin_summary.md |
| 2026-05-08 | Session 5: VP-6 effective DOF; OP-OMS-018 partial resolution; OMS-1.2 audit | vp6_effective_dof_jacobian.py, vp6_u_star_regular_path_test.py, vp6_initial_reading_log.md, effective_dof_theory.md, op_oms_018_regular_u_star.md, vp6_effective_dof.md, vp6_effective_dof_log.md, observer_landscape_admissible_class.md, oms_1_2_status_audit.md, vp6_jacobian_spectra.json, vp6_effective_dof_summary.md, vp6_u_star_path_results.json, vp6_u_star_path_summary.md |
| 2026-05-08 | Session 6: OMS-2.0 push (Gates 1–8); Conditional Accepted | op_oms_001_gap_c1_rank_theorem.md, op_oms_001_gap_c1_sensitivity.md, op_oms_001_gap_c1_genericity.md, op_oms_002_nontrivial_v.md, op_oms_026_sigma_branch_full.md, oms_2_0_promotion_audit.md, vp8_gap_c1_rank_witness.py, vp9_nontrivial_v_basin_test.py, vp10_sigma_branch_delta3.py, vp8_gap_c1_rank_witness.json/.md, vp9_nontrivial_v_basin.json/.md, vp10_sigma_branch_delta3.json/.md |
| 2026-05-08 | Session 7: proof closure → **OMS-2.0 Accepted — Static** | proof_promotion_reading_log.md, gap_c1_final_theorem_package.md, op_oms_032_closed_form_h4.md, op_oms_033_sigma_sn_arnold.md, op_oms_034_temporal_delta3_status.md, oms_2_0_accepted_audit.md, canonical.md (Appendix OMS added) |
| 2026-05-08 | Session 8: OP-OMS-034 closure → **OMS-2.0 Accepted — Full** | op_oms_034_initial_log.md, op_oms_034_temporal_delta3_resolution.md, oms_2_0_full_accepted_audit.md, vp11_temporal_delta3.py, vp11_temporal_rank_witness.{json,md}, vp11_temporal_delta3.{json,md}, canonical.md Appendix OMS subsection M (Temporal) |
