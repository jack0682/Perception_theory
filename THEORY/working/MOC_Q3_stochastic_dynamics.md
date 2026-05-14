---
type: MOC
cluster: Q3-stochastic-dynamics
id: MOC_Q3_stochastic_dynamics
parent: [[THEORY_INDEX]]
question: Q3. 어떻게 변하는가?
last_updated: 2026-05-14
---

# MOC: Q3 — 어떻게 변하는가? (Stochastic Dynamics / Gibbs)

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]] · [[INDEX|working/INDEX.md]]
> Authority: [[canonical]] T-PF-A1-SDE, P-F-A1 Package I; [[theorem_status]]
> Status: Package I Cat A (CV-1.9); Package II 진입 타겟 (CV-1.17)

## Purpose

Σ_m 위의 projected Langevin SDE 와 Lions-Sznitman 반사 동력학을 통해 SCC 응집장의 시간 변화를 모형화한다. Package I (존재·유일·non-explosion) 는 Cat A 완료. 다음 표적은 Package II (Eyring-Kramers prefactor) — [[MOC_H_MORSE_packageII]] 와 연동.

## Core Files (Active)

- [[pf_tstar_langevin]] ★ — P-F-A1 stochastic foundation (T_* axiom + Package I/II)
- [[pf_a1_lions_sznitman_freidlin_route]] — Lions-Sznitman / Freidlin-Wentzell route
- [[n1_kramers_extension]] — N1 Kramers rate extension
- [[bernshtein_conservation]] — Bernstein conservation law
- [[self_ref_fp_stability]] — Self-referential fixed-point stability
- [[mathematical_scaffolding_4tools]] — 4-tool mathematical scaffolding
- [[scc_mass_gap_connection]] — SCC / mass gap connection
- [[foundational_bridges_2026]] — Foundational bridges

## Code Module

- `CODE/scc/langevin.py` — Projected Euler-Maruyama SDE sampler on Σ_m (F3 axiom Cat A via Lions-Sznitman).

## Reading Order

1. [[canonical]] §P-F (Package I, T-PF-A1-SDE Cat A)
2. [[pf_tstar_langevin]]
3. [[pf_a1_lions_sznitman_freidlin_route]]
4. [[n1_kramers_extension]] (Kramers 진입)
5. [[bernshtein_conservation]]
6. [[scc_mass_gap_connection]] (Q3 ↔ 외부 물리 연결)

## Dependencies

- Requires: A3 ($a_{cl} < 4$), $b_D = 0$, [[02_axioms_and_primitives]] F1-F3 axioms.
- Feeds into: [[MOC_Q4_K_selection]] (DYN branch), [[MOC_H_MORSE_packageII]] (Eyring-Kramers prefactor).
- Blocked by: **H-T*** (T_* registration; OP-0021) + **H-MORSE** (Local Cat B 가짐, Global Cat A path = OP-HMORSE-LOCAL-A).

## Current Status (CV-1.16)

- **Canonical:** T-PF-A1-SDE (Cat A); P-F-A1 Package I full (CV-1.9).
- **Working:** Package II 진입 준비 — L-HMORSE-LOCAL (Cat B, CV-1.16) 가 H5 partial replacement 제공.
- **Open:** H-T* (OP-0021), Package II prefactor.

## Next Target (CV-1.17)

> Package II Eyring-Kramers prefactor Cat B — L-HMORSE-LOCAL + OP-0021 ($T_*$) 결합.

## Related Clusters

- [[MOC_H_MORSE_packageII]]
- [[MOC_Q4_K_selection]]
- [[MOC_Q5_temporal_identity]]
- [[MOC_action_temporal_cost]] (CV-1.15 action 기반 시간 비용)
- [[MOC_hypothesis_tree]]

---

*MOC_Q3_stochastic_dynamics, 2026-05-14.*
