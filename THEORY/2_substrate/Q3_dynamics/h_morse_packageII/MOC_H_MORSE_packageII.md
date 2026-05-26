---
type: MOC
cluster: H-MORSE-PackageII
id: MOC_H_MORSE_packageII
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: H-MORSE Closure Package (CV114) → Package II Eyring-Kramers

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]] · [[MOC_Q3_stochastic_dynamics]]
> Authority: [[canonical]] L-CLOSURE-LIFT (Cat A), L-HMORSE-LOCAL (Cat B), L-HMORSE-DECOMP (Cat B); [[CV-1.16_SEAL]]
> Status: PARTIALLY CLOSED — Local Cat B 달성 (CV-1.16). Global Cat A path = OP-HMORSE-LOCAL-A.

## Purpose

H-MORSE 가설 (E 의 Morse 안정성) 은 Package II Eyring-Kramers prefactor 의 핵심 차단 가설이었다. CV-1.16 봉인 시 H-MORSE-Local Closure Package 가 promote 되어 Local 형태가 Cat B 무조건적으로 닫혔으며, OP-HMORSE-BROADNESS 는 3-approach (Perron-Frobenius, operator-norm, 15/15 numerical PASS) 로 Cat A 닫힘.

## Core Files

- [[00_index]] — CV114 H-MORSE Package II index
- [[01_canonical_audit]] — Canonical audit
- [[02_H_MORSE_statement_reconstruction]] — Statement reconstruction
- [[03_energy_landscape_and_hessian]] — Energy landscape + Hessian
- [[04_degeneracy_catalogue]] — Degeneracy catalogue
- [[05_counterexample_search]] — Counterexample search (V5b-T-zero 등 7 families)
- [[06_packageII_dependency_map]] — Package II dependency map
- [[07_Eyring_Kramers_requirements]] — Eyring-Kramers prerequisites
- [[08_candidate_lemma_chain]] — Candidate lemma chain
- [[09_CV114_recommendation]] — Recommendation
- [[10_agent_handoff_prompt]] — Handoff prompt
- [[11_broadness_attack]] — Broadness attack (OP-HMORSE-BROADNESS path)

## Promoted Results (CV-1.16)

- **L-CLOSURE-LIFT Cat A** — operator-norm broadness 의 closure-correction Hessian.
- **L-HMORSE-LOCAL Cat B** — projected Hessian lower bound on free tangent subspace; D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) active-set form.
- **L-HMORSE-DECOMP Cat B** — Hessian 분해 $H_\mathcal{E} = H_{bd} + H_{cl} + H_{sep}$.
- **L-BOUNDARY-MODE-EXCLUSION Cat C** — SKETCH-level Weyl perturbation.
- **OP-HMORSE-BROADNESS CLOSED Cat A** — Approach (b) Theorem B2 primary + (a) Perron-Frobenius supplementary + (c) 15/15 numerical PASS.

## Reading Order

1. [[CV-1.16_SEAL]] — H-MORSE Local Closure Package 요약
2. [[00_index]]
3. [[02_H_MORSE_statement_reconstruction]] (D-HMORSE-LOCAL (C1)-(C5))
4. [[03_energy_landscape_and_hessian]]
5. [[08_candidate_lemma_chain]] (L-CLOSURE-LIFT 경로)
6. [[11_broadness_attack]] (3-approach 수렴)
7. [[07_Eyring_Kramers_requirements]] (Package II 진입 요건)

## Dependencies

- Requires: [[MOC_Q3_stochastic_dynamics]] (Langevin foundation), [[sct_axioms_and_primitives]] (A3, $b_D = 0$).
- Feeds into: Package II Eyring-Kramers prefactor (CV-1.17 타겟 Cat B).
- Pairs with: OP-HMORSE-LOCAL-A (Cat A path, ~2 sessions), OP-HMORSE-SBM (numerical robustness 확장).

## Current Status (CV-1.16)

- **Canonical:** L-CLOSURE-LIFT (Cat A); L-HMORSE-LOCAL, L-HMORSE-DECOMP (Cat B); L-BOUNDARY-MODE-EXCLUSION (Cat C); OP-HMORSE-BROADNESS CLOSED.
- **Working:** Package II prefactor 진입 준비.
- **Open:** OP-HMORSE-LOCAL-A (Cat A path), OP-HMORSE-SBM (robustness), OP-0021 (T_* 정규 등록 — H-T*).

## Code / Experiment

- `CODE/experiments/exp_hmorse_broadness_full_spectrum.py` — 15/15 numerical PASS.

## Related Clusters

- [[MOC_Q3_stochastic_dynamics]]
- [[MOC_canonical_authority]]
- [[MOC_hypothesis_tree]]
- [[MOC_experiments_validation]]

---

*MOC_H_MORSE_packageII, 2026-05-14.*
