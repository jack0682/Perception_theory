---
type: MOC
cluster: Q4-K-selection
id: MOC_Q4_K_selection
parent: [[THEORY_INDEX]]
question: Q4. 몇으로 안정화되는가?
last_updated: 2026-05-14
---

# MOC: Q4 — 몇으로 안정화되는가? (K-Selection)

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]] · [[INDEX|working/INDEX.md]]
> Authority: [[canonical]] T-K-Select-PF, T-L1-F, T-L1-M; [[theorem_status]]
> Status: Cat B (T-K-Select-PF); K-act/K-bar/K-soft 사다리 Cat A 조건부

## Purpose

K_field (모델 슬롯) / K_act (활성) / K_bar (위상 컴포넌트) / K_soft (persistence 가중) 의 4가지 count 가 어떤 조건에서 일치·분기하는지 다룬다. 핵심: 세 가지 selection 메커니즘 (EQ free energy, OBS posterior, DYN Kramers) 의 호환성.

## Core Files (Active)

- [[k_selection_mechanism]] ★ — Core K-selection 메커니즘
- [[k_select_pf_equilibrium]] — T-K-Select-PF Cat B working
- [[k_select_obs_posterior]] — T-K-Select-OBS Cat B working
- [[k_selection_a_free_energy]] — EQ branch (OP-0005-EQ)
- [[k_selection_b_kramers]] — DYN branch (Kramers rate)
- [[k_selection_c_numerical_anchor]] — Numerical anchors
- [[k_selection_compatibility_proof]] — EQ/OBS/DYN compatibility
- [[commitment_19_k_selection_axiom_packet]] — Axiom packet
- [[reservoir_reinterpretation_of_K]] — Reservoir reinterpretation
- [[pre_objective_K_field_tension]] — Pre-objective K-field tension
- [[F_Kstep_K_triple]] — F, K-step, K-triple structure
- [[K_status_commitment]] — Status commitment
- [[shared_pool_canonical_proposal]] — Shared pool proposal
- [[op_0009_pre_a_kfield_chart_validity]] — OP-0009 pre-A K-field chart
- [[soft_K_definition]] — Soft-K definition

## T-L1-F Provenance Series → [[MOC_Q2_multi_formation]]

T-L1-F (K-act → K-bar bridge) 의 16-file provenance 는 Q2 MOC 에 정리. 여기서는 결과만 사용.

## WQ Experiment Results

- [[wq1c_layerI_h0_bardeath_protocol]] · [[wq1c_layerI_h0_bardeath_results]]
- [[wq1c_r2_projected_layerII_aggregate_sigma_results]]
- [[wq_lat1_reservoir_resolution_sweep_protocol]] · [[wq_lat1_reservoir_resolution_sweep_results]]
- [[wq_lat1b_phi_envelope_refinement_results]]

## Code / Theory Modules

- `CODE/scc/multi.py` — K-field, transport_k_formations
- `CODE/scc/k_soft.py` — k_soft(u), φ_sat / φ_lin, Lipschitz-certified

## Reading Order

1. [[canonical]] §T-K-Select-PF, §T-L1-F
2. [[k_selection_mechanism]]
3. [[k_select_pf_equilibrium]]
4. [[k_selection_a_free_energy]], [[k_selection_b_kramers]], [[k_selection_c_numerical_anchor]]
5. [[k_selection_compatibility_proof]]
6. [[commitment_19_k_selection_axiom_packet]]

## Dependencies

- Requires: [[MOC_Q2_multi_formation]] (T-L1-F Cat A), [[MOC_Q3_stochastic_dynamics]] (Kramers rate for DYN branch).
- Feeds into: [[MOC_Q5_temporal_identity]] (stable-K kernel), [[MOC_Q6_sigma_inherit]].
- Blocked by: H-T* (DYN branch), H-MORSE (Kramers prefactor), OP-0005 (EQ K-selection 완성).

## Current Status (CV-1.16)

- **Canonical:** T-L1-F (Cat A), T-L1-M (Cat A), T-K-Select-PF (Cat B).
- **Working:** EQ/OBS/DYN compatibility proof, k_soft Lipschitz bridge.
- **Open:** OP-0005 (K-selection EQ 완전), OP-0009 (multi-formation 무조건화).

## Related Clusters

- [[MOC_Q2_multi_formation]] (T-L1-F provenance 의 본거지)
- [[MOC_Q3_stochastic_dynamics]] (DYN branch)
- [[MOC_temporal_composition]] (CV-1.14 T-CC-StableK; K-stability across time)
- [[MOC_H_MORSE_packageII]]
- [[MOC_hypothesis_tree]]

---

*MOC_Q4_K_selection, 2026-05-14.*
