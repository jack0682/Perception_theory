---
type: MOC
cluster: experiments-validation
id: MOC_experiments_validation
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: Experiments × Theory Mapping

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]]
> Authority: `CODE/experiments/` + `CODE/tests/`
> Status: 215 passed, 1 xfailed (CV-1.16 baseline)

## Purpose

`CODE/experiments/exp<N>_*.py`, OMS VP-1..VP-11, WQ Layer/Reservoir 실험, 그리고 H-MORSE broadness 실험이 어떤 정리·가설을 검증하는지의 역참조 인덱스. 이 MOC 는 *링크 노드* 만 제공하며, 실험 파일 자체는 `CODE/` 에 있다.

## 1. WQ Experiments (K-selection / L1-J 영역)

검증 대상: [[MOC_Q4_K_selection]] 의 T-L1-F, L1-J upgrade attempt.

- `wq1c_layerI_h0_bardeath_protocol.py / .results` ↔ [[wq1c_layerI_h0_bardeath_protocol]] · [[wq1c_layerI_h0_bardeath_results]]
- `wq1c_r2_projected_layerII_aggregate_sigma.py` ↔ [[wq1c_r2_projected_layerII_aggregate_sigma_results]]
- `wq_lat1_reservoir_resolution_sweep.py` ↔ [[wq_lat1_reservoir_resolution_sweep_protocol]] · [[wq_lat1_reservoir_resolution_sweep_results]]
- `wq_lat1b_phi_envelope_refinement.py` ↔ [[wq_lat1b_phi_envelope_refinement_results]]

## 2. OMS Validation Protocols (VP-1 ~ VP-11)

검증 대상: [[MOC_observer_moduli_OMS]] OMS-2.0 Accepted — Full.

- VP-1 (exp86) — OP-OMS-009 R1 PROVED. ↔ [[vp1_p_resolution_audit]], [[vp1_counterexamples]], [[vp1_results]]
- VP-3 (exp87) — G_cw = {e} COMP. SUPPORTED. ↔ [[vp3_core_weight_symmetry_results]]
- VP-4 (exp88) — Prop BS1 CONFIRMED. ↔ [[vp4_basin_stratification_results]]
- VP-6 — d_eff ≤ 2 in 42/42. ↔ [[vp6_effective_dof]], [[vp6_effective_dof_log]]
- VP-7 — Σ_branch fine-grid. ↔ [[vp7_branch_map_results]]
- VP-8/9/10 — OMS-2.0 Gates 1–8 ↔ [[op_oms_001_gap_c1_rank_theorem]], [[op_oms_002_nontrivial_v]], [[op_oms_026_sigma_branch_full]]
- VP-11 (vp11_temporal_delta3) — Phase 1+2; OP-OMS-034 Case A verdict. ↔ [[op_oms_034_temporal_delta3_resolution]]

## 3. H-MORSE Broadness 실험

검증 대상: [[MOC_H_MORSE_packageII]] / OP-HMORSE-BROADNESS Approach (c).

- `exp_hmorse_broadness_full_spectrum.py` → 15/15 PASS (broadness + lift). ↔ [[CV-1.16_SEAL]] Certification Record

## 4. Code Modules ↔ MOC

| Module | MOC |
| --- | --- |
| `scc/graph.py`, `params.py`, `operators.py`, `energy.py`, `optimizer.py`, `diagnostics.py` | [[MOC_canonical_authority]] (pipeline core) |
| `scc/multi.py`, `transport.py`, `k_soft.py` | [[MOC_Q2_multi_formation]], [[MOC_Q4_K_selection]] |
| `scc/langevin.py` | [[MOC_Q3_stochastic_dynamics]] |
| `scc/sigma_rich.py` | [[MOC_sigma_rich_framework]], [[MOC_Q6_sigma_inherit]] |
| `scc/persistence.py`, `resolvent.py`, `predicates.py` | [[MOC_Q1_boundary_T8]], [[MOC_Q4_K_selection]] |

## 5. Test Suite Baseline

```
cd CODE && python3 -m pytest tests/ -v
# 215 passed, 1 xfailed (CV-1.16 sealed baseline)
```

## Dependencies

- All canonical Cat A promotions must pass tests baseline (215 + 1 xfailed) per [[README|canonical/README.md]] promotion criteria.
- Experiments are *provenance only* — re-derivation from experimental results into canonical not permitted unless paired with proof.

## Related Clusters

- 모든 Q-MOC
- [[MOC_observer_moduli_OMS]]
- [[MOC_H_MORSE_packageII]]
- [[MOC_canonical_authority]]

---

*MOC_experiments_validation, 2026-05-14.*
