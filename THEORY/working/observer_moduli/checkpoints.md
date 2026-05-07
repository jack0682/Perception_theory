---
type: working/checkpoints
created: 2026-05-07
project: Observer Moduli Space of SCC
---

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
- [x] Integration with SCC layers documented
- [x] Canonical promotion checklist written

**OMS-1.0-candidate overall: CANONICAL CANDIDATE (2 blockers remaining: OP-OMS-001, OP-OMS-002)**

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
