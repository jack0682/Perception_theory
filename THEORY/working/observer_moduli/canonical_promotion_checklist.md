---
type: working/checklist
created: 2026-05-07
stage: OMS-1.0
project: Observer Moduli Space of SCC
---

# Canonical Promotion Checklist — OMS

Use this checklist to determine when OMS is ready for promotion from `THEORY/working/observer_moduli/` to `THEORY/canonical/canonical.md`.

Each item is marked: **[✓] COMPLETE** | **[~] PARTIAL** | **[✗] INCOMPLETE** | **[!] BLOCKER**

---

## Criterion A: Definitions Complete

| # | Item | File | Status |
|---|---|---|---|
| A1 | $\Theta = (q, \lambda, \xi)$ fully defined with domains | definitions.md DEF-2 | **[✓]** |
| A2 | $\mathcal{M}_{\mathrm{obs}} = [q_{\min},q_{\max}] \times \Delta^3 \times B_\xi$ | definitions.md DEF-4 | **[✓]** |
| A3 | $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$ defined (criticality hypothesis) | definitions.md DEF-5 | **[✓]** |
| A4 | Readout map $P = P_{\mathrm{top}}$ with three levels | readout_map_audit.md DEF-R1,R2 | **[✓]** |
| A5 | Gauge group $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{task}$ | definitions.md DEF-8 | **[✓]** |
| A6 | Moduli space $\mathfrak{M} = \mathcal{M}_{\mathrm{obs}} / G$ | oms_1_candidate.md DEF-7 | **[✓]** |
| A7 | Stabilizer subgroup $G_\Theta$ | definitions.md DEF-9 | **[✓]** |
| A8 | Fundamental domain for finite $G$ | definitions.md DEF-12 | **[✓]** |
| A9 | Admissible observer landscape class $\mathcal{V}_{\mathrm{adm}}$ | observer_landscape_candidates.md | **[✓]** |
| A10 | Basin stratification and perceptual type | basin_stratification.md DEF-11 | **[✓]** |
| A11 | Topological signature $T_\Theta$ | readout_map_audit.md DEF-R2 | **[✓]** |
| A12 | Relevant/irrelevant directions, $d_{\mathrm{eff}}$ | rg_relevance_flow.md RG3–RG5 | **[✓]** |
| A13 | Boundary strata $\partial_I \Delta^3$ | stratified_dynamics.md SD1 | **[✓]** |
| A14 | Latent generator framework | latent_symmetry.md LS1–LS3 | **[✓]** |
| A15 | Unique canonical $V \in \mathcal{V}_{\mathrm{adm}}$ | — | **[!] BLOCKER (OP-OMS-002)** |

**Criterion A summary:** 14/15 complete. Blocked on A15 (explicit canonical $V$).

---

## Criterion B: Proofs Complete

| # | Item | File | Status |
|---|---|---|---|
| B1 | $\mathcal{M}_{\mathrm{obs}}$ compact (Tychonoff) | observer_moduli_space.md Prop 1 | **[✓]** |
| B2 | $\mathfrak{M}$ compact | Prop 3 | **[✓]** |
| B3 | $\mathfrak{M}$ Hausdorff | Prop 4 | **[✓]** |
| B4 | $\mathfrak{M}$ connected | Prop 6 | **[✓]** |
| B5 | Finite gauge preserves dimension | Prop 5 | **[✓]** |
| B6 | $\mathfrak{M}$ is orbifold | Prop 7 | **[✓]** |
| B7 | $P_{\mathrm{top}}$ descent to quotient | readout_map_audit.md Prop R3 | **[~] PARTIAL** (conditional on $u^*$ continuity) |
| B8 | $P_{\min}$ too coarse (Prop R1) | readout_map_audit.md, vp1_counterexamples.md | **[✓] PROVED** (VP-1, exp86, 4 CEs, 2026-05-07) |
| B9 | K=1 minimal model $\cong \Delta^3$ | toy_models.md Props A1–A6 | **[✓]** |
| B10 | K=2 symmetric product + diagonal singularity | toy_models.md Props B1–B3 | **[✓]** |
| B11 | Multiple basins on connected space (Prop BS1) | basin_stratification.md | **[✓]** |
| B12 | Boundary faces as absorbing walls (Prop SD1) | stratified_dynamics.md | **[✓]** |
| B13 | $S_4$ weight permutation rejected (CW1) | core_weight_symmetry.md | **[✓]** |
| B14 | U(1) on $(\alpha,\beta)$ rejected | audit_log.md AUDIT-001 | **[✓]** |
| B15 | No vertex-preserving cont. symmetry (LS1) | latent_symmetry.md | **[✓]** |
| B16 | Transport invariance (static scenes, CW2) | core_weight_symmetry.md | **[✓] conditional** |
| B17 | Continuity of $u^*(\Theta)$ | — | **[~] OPEN** (OP-OMS-009 residual — resolution sub-question closed, continuity still unproved) |
| B18 | Existence of $V \in \mathcal{V}_{\mathrm{adm}}$ | — | **[!] BLOCKER (OP-OMS-002)** |
| B19 | RG relevance: $d_{\mathrm{eff}}$ computation | rg_relevance_flow.md | **[~] HYPOTHESIZED** (VP-6 needed) |

**Criterion B summary:** 14/19 fully proved; 2 partial/hypothesized; 1 blocker; 1 conditional. (B8 promoted to proved by VP-1.)

---

## Criterion C: Audits Complete

| # | Item | File | Status |
|---|---|---|---|
| C1 | No U(1) gauge overclaim | audit_log.md AUDIT-001 | **[✓]** |
| C2 | No finite-gauge dimension overclaim | audit_log.md AUDIT-002 | **[✓]** |
| C3 | $G_{\mathrm{core\text{-}weight}} = \{e\}$ labeled as default | audit_log.md AUDIT-003 | **[✓]** |
| C4 | Criticality hypothesis labeled as assumption | audit_log.md AUDIT-004 | **[✓]** |
| C5 | $\mathrm{Aut}_{task}$ task-anchored (not full $\mathrm{Aut}(X_t)$) | audit_log.md AUDIT-005 | **[✓]** |
| C6 | $S_4$ weight symmetry rejection documented | core_weight_symmetry.md CW1 | **[✓]** |
| C7 | No species-typical overclaim from orbifold singularities | oms_1_candidate.md §19 | **[✓]** |
| C8 | Diagnostic-only core overclaim warned | readout_map_audit.md Warning R1 | **[✓]** |
| C9 | No canonical $V$ overclaim | observer_landscape_candidates.md | **[✓]** |
| C10 | RG labeled as program not theorem | rg_relevance_flow.md Warning RG1 | **[✓]** |
| C11 | Connected $\mathfrak{M}$ ≠ single perceptual type | oms_1_candidate.md §19 | **[✓]** |
| C12 | Latent symmetry labeled as Gen extension | latent_symmetry.md | **[✓]** |
| C13 | Basin count labeled as $V$-dependent | oms_1_candidate.md §19 | **[✓]** |
| C14 | Boundary face degeneracy labeled as open | stratified_dynamics.md | **[✓]** |
| C15 | $b_D = 0$ fixed (not observer) | audit_log.md AUDIT-009 | **[✓]** |
| C16 | $m$ scene-determined (not observer) | audit_log.md AUDIT-010 | **[✓]** |
| C17 | Effective DOF estimate labeled as hypothesis | rg_relevance_flow.md Warning RG3 | **[✓]** |

**Criterion C summary:** 17/17 complete. All audit warnings documented.

---

## Criterion D: Open Problems Classified

| # | ID | Title | Classification | Promotion blocker? |
|---|---|---|---|---|
| D1 | OP-OMS-001 | Core-weight gauge group | OPEN (constrained) | **YES** |
| D2 | OP-OMS-002 | Admissible $V$ existence | OPEN | **YES** |
| D3 | OP-OMS-003 | Connectedness | **RESOLVED** (Prop 6) | No |
| D4 | OP-OMS-004 | Contractibility of $\mathrm{Sym}^K(\Delta^3)$ | OPEN | No |
| D5 | OP-OMS-005 | Effective DOF / continuous gauge | OPEN | No |
| D6 | OP-OMS-006 | Topology for non-trivial $\mathrm{Aut}_{task}$ | OPEN | No |
| D7 | OP-OMS-007 | Observer dynamics (Level-3) | DEFERRED | No |
| D8 | OP-OMS-008 | Relation to RelationWorld | OPEN | No |
| D9 | OP-OMS-009 | Readout resolution + continuity | **RESOLVED-NEGATIVE** (VP-1, 2026-05-07) | REMOVED |
| D10 | OP-OMS-010 | $V$ regularity | OPEN | No (subsumed by D2) |
| D11 | OP-OMS-011 | Basin stability | OPEN | No |
| D12 | OP-OMS-012 | Boundary face interpretation | OPEN | No |
| D13 | OP-OMS-013 | Stratified flow at corners | OPEN | No |
| D14 | OP-OMS-014 | Empirical identifiability | OPEN | No |
| D15 | OP-OMS-015 | OMS ↔ perceptual styles | OPEN | No |
| D16 | OP-OMS-016 | Computational $d_{\mathrm{eff}}$ | COMPUTATIONALLY TESTABLE | No |

**Criterion D summary:** 16/16 classified. 2 canonical blockers (OP-OMS-001, OP-OMS-002). 2 resolved (OP-OMS-003, OP-OMS-009).

---

## Criterion E: Integration Complete

| # | Item | Status |
|---|---|---|
| E1 | `THEORY/working/INDEX.md` updated with observer_moduli/ | **[✓]** (Session 1) |
| E2 | `THEORY/CHANGELOG.md` updated with Session 1 entry | **[✓]** (Session 1) |
| E3 | Cross-links to SCC static theory | **[✓]** (integration_with_scc.md) |
| E4 | Cross-links to multi-formation theory | **[✓]** (integration_with_scc.md §3.2) |
| E5 | Cross-links to temporal identity theory | **[✓]** (integration_with_scc.md §3.1) |
| E6 | Layer map in integration document | **[✓]** (integration_with_scc.md §2) |
| E7 | INDEX.md updated with Session 2 new files | **[✗]** (pending Task 27) |
| E8 | CHANGELOG.md updated with Session 2 entry | **[✗]** (pending Task 27) |
| E9 | OMS promotion criteria listed in canonical.md | **[✗]** (deferred — OMS not yet canonical) |

**Criterion E summary:** 6/9 complete. Tasks 27 will complete E7–E8. E9 deferred until OMS is canonical-accepted.

---

## Validation Protocols Status

| Protocol | Purpose | Status |
|---|---|---|
| VP-1: P-resolution audit | Confirm Prop R1 | **COMPLETE** (exp86, 2026-05-07; 4 CEs; RESOLVED-NEGATIVE) |
| VP-2: Basin discovery | Demonstrate multi-basin $V_D^0$ | **NOT YET RUN** |
| VP-3: Core-weight symmetry | Test closure-separation swap | **NOT YET RUN** |
| VP-4: Boundary face ablation | Validate face interpretations | **NOT YET RUN** |
| VP-5: Latent symmetry (toy) | Verify dimension formula | **NOT YET RUN** |
| VP-6: RG Jacobian singular spectrum | Estimate $d_{\mathrm{eff}}$ | **NOT YET RUN** |

All protocols defined in `validation_protocols.md`. Recommended execution order: VP-1 → VP-3 → VP-4 → VP-2 → VP-6 → VP-5.

---

## Promotion Pathway

### Path to CANONICAL ACCEPTED

1. **Immediate (computational):**
   - ~~Run VP-1 → Confirm Prop R1 → Resolve OP-OMS-009 partially.~~ **DONE** (exp86, 2026-05-07; RESOLVED-NEGATIVE)
   - Run VP-3 → Test $g_1 \notin G_{\mathrm{cw}}$ → Constrain OP-OMS-001 further. **NEXT PRIORITY**
   - Run VP-2 → Demonstrate multi-basin $V_D^0$ → Resolve OP-OMS-002 partially.

2. **Near-term (theoretical):**
   - Prove or cite regularity of $u^*(\Theta)$ (SCC optimizer output) → Resolve continuity part of OP-OMS-009.
   - Show $V_D^0 \in \mathcal{V}_{\mathrm{adm}}$ (verify V1–V5 for this specific $V$) → Partially resolve OP-OMS-002.

3. **Medium-term:**
   - Either prove $G_{\mathrm{core\text{-}weight}} = \{e\}$ or find a non-trivial element → Resolve OP-OMS-001.
   - Define a canonical $V$ satisfying all criteria V1–V5 with proof → Resolve OP-OMS-002.

4. **Promotion trigger:**
   - All three blockers resolved → Status upgrades from CANONICAL CANDIDATE to CANONICAL ACCEPTED.
   - Add OMS §14 to canonical.md. Log in CHANGELOG.md. Update INDEX.md.

---

## Final Classification

$$\boxed{\textbf{OMS-1.0-candidate: CANONICAL CANDIDATE — Blocked by OP-OMS-001, OP-OMS-002}}$$

*(OP-OMS-009 blocker REMOVED 2026-05-07, VP-1.)*

**The following sub-results are canonical-ready and may be promoted independently:**
- Compactness, Hausdorff, connectedness, orbifold structure (Props 1–7).
- Toy models A and B (Props A1–A6, B1–B3).
- Basin multiplicity on connected space (Prop BS1).
- Boundary face absorbing-wall result (Prop SD1).
- Gauge rejection results (CW1, LS1, AUDIT-001).
- $P_{\min}$ coarseness result (Prop R1, PROVED by VP-1).
- Mandatory audit warnings C1–C17.

**The following require resolution of blockers before promotion:**
- Basin stratification as core OMS claim (pending OP-OMS-002).
- Full gauge group $G_{\mathrm{SCC}}^{(0)}$ with $G_{\mathrm{core\text{-}weight}}$ determined (pending OP-OMS-001).

---

*Checklist version 1.1, 2026-05-07. Updated after VP-1 resolution of OP-OMS-009.*
