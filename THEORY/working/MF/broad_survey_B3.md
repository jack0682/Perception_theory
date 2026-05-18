> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[k_selection_b_kramers]] · [[n1_kramers_extension]]

# broad_survey_B3.md — OP-0005-DYN Kramers 3-Pillar Multi-Formation Lift Survey

**Type**: W8-Day1 Track B LIGHTER. *Survey + candidate identification only* — **no proof attempts**. W9+ staging input.
**Date**: 2026-05-18 (W8-Day1, Mon).
**Author**: Claude session, sole producer.
**Canonical refs**: `canonical.md §16 D-ST-4` (Kramers rate single-formation), `§13 T-K-Select-PF Cat B / T-K-Select-OBS Cat B` (equilibrium / observation K-selection), `theorem_status.md` OP-0005-DYN row.
**Working refs**: `k_selection_b_kramers.md` (Kramers single-formation working), `n1_kramers_extension.md` (multi-formation extension preliminary), `sigma_inherit_k_jump.md` (K-jump σ-inheritance).
**Pre-work xref check**: 20+ working file hit. 본 broad survey 의 *novel positioning* = *3-pillar* (nucleation / metastability / coarsening) 의 multi-formation *lift candidate* 의 *light* 매핑 — *증명 시도 0*.

---

## §1. Mission

> **OP-0005-DYN (Dynamical K-transition / Kramers rates) 의 W9+ staging — 3-pillar (nucleation, metastability, coarsening) 의 *multi-formation lift candidate* 식별. *증명 시도 부재*. *survey 만*.**

W8 strategic plan §11 W9+ Preview (모든 Path 공통):

> OP-0005-DYN Kramers rate full Cat A (Package II 의존)

본 file 이 그 *staging input*.

---

## §2. 현재 OP-0005-DYN 상태

`theorem_status.md`:

> **OP-0005-DYN** Dynamical K-transition / Kramers rates — **OPEN**. Package II (Eyring-Kramers, H5 + OP-0021). Not before W9+.

`k_selection_b_kramers.md §8.1-8.2`:
- Single-formation Kramers escape rate: Cat A established (classical formula + P-F-A1 Package I Cat A 입력).
- Multi-formation K-jump cascade: Cat B pending (§4.4 K-jump cascade 의 Markov chain approximation).

---

## §3. Pillar 1 — Nucleation

### §3.1 Single-formation 의 nucleation

Classical Kramers (1940): $\Gamma_{0 \to 1} \sim A \exp(-\Delta E_{0 \to 1} / T_*)$.

SCC single-formation: K=0 → K=1 의 *birth* event — F_M(P) 의 *uniform* state 에서 *first-formation* basin 으로의 escape.

`k_selection_b_kramers.md §4.1`: single-pair escape rate established (P-F-A1 Package I 의 T-PF-A1-PE spectral gap 활용).

### §3.2 Multi-formation lift candidate

K = K_0 → K_0 + 1 의 *new formation birth* 에서의 nucleation:
- *Heterogeneous nucleation*: 기존 $K_0$ formation 들의 spatial layout 이 *seed* 역할 — 새 formation 의 *embedding location* 의 *distributional* preference.
- *Concurrent nucleation*: 두 개 이상의 new formation 의 *동시 birth* (가능?). exp93 multi-step temporal Persist chaining 의 입력.

### §3.3 외부 reference

| Reference | 적용 |
|---|---|
| Langer, *Statistical theory of the decay of metastable states*, Ann. Phys. 41 (1967) | classical homogeneous nucleation barrier |
| Bovier-Manzo, *Metastability in Glauber dynamics in the low-temperature limit*, J. Stat. Phys. 107 (2002) | discrete-site nucleation barrier — SCC graph 형 적합 |
| Beltran-Landim, *Tunneling and metastability of continuous time Markov chains*, J. Stat. Phys. 140 (2010) | multi-basin metastability — multi-K lift 의 input |

### §3.4 Success / failure modes

- **Success**: K_0 → K_0 + 1 birth rate $\Gamma_{K_0 \to K_0 + 1} \sim A_\mathrm{nucl}(K_0) \exp(-\Delta E_\mathrm{nucl}(K_0) / T_*)$ 의 *closed form* + numerical anchor (Day 5 exp94 phase diagram 의 3-regime).
- **Failure**: $A_\mathrm{nucl}$ 가 *non-trivial* $K_0$-dependence — *N-body interaction* 의 effective form 미상; classical Langer formula 의 *direct lift* 불가.

---

## §4. Pillar 2 — Metastability

### §4.1 Single-formation 의 metastability

K-basin $\mathcal{B}_K(\mathcal{P})$ 의 *long-lived* nature (D-ST-3 canonical §16):
- *Equilibrium* K-selection: $p_K = Z_K / Z$ (T-K-Select-PF Cat B).
- *Kinetic* metastability: K-basin 내 dwell time $\tau_K \sim \exp(\Delta E / T_*)$.

### §4.2 Multi-formation lift candidate

Multi-K metastability:
- *Cascade structure*: K = K_max → K_max - 1 → ... → K^* 의 *sequential* metastable transitions. *exp_x1_v5_hysteresis* / *exp_x1_v7_predictions* 의 입력?
- *Cross-K interference*: 두 metastable K-basin 의 *interlocking* — non-trivial barrier landscape.
- *Beltran-Landim metastable hierarchy*: 가장 안정 K → 두번째 안정 K 의 *time-scale separation*.

### §4.3 외부 reference

| Reference | 적용 |
|---|---|
| Bovier-den Hollander, *Metastability: A Potential-Theoretic Approach* (2015) | book-length treatment of multi-basin metastability — SCC 의 multi-K 의 *시간 척도 분리* framework |
| Olivieri-Vares, *Large Deviations and Metastability* (2005) | Freidlin-Wentzell + 대조; SCC P-F-A1 Package II 의 zero-noise 의존성 |
| Schütte et al., *A Direct Approach to Conformational Dynamics Based on Hybrid Monte Carlo*, J. Comp. Phys. 151 (1999) | metastable conformation finding — SCC 의 K-basin 식별 algorithm 후보 |

### §4.4 Success / failure modes

- **Success**: Multi-K metastable hierarchy 의 *time-scale separation* (각 K 의 $\tau_K$) explicit form.
- **Failure**: K-basin 의 *fuzziness* — `subthreshold_demo_check` 의 sub-threshold regime 에서 K-tuple 자체가 *smooth* — metastable basin 정의 부재.

### §4.5 Zero-temperature flag (필수)

> **Metastability 의 thermodynamic 측면 (∃ Hessian 양정부호) 과 kinetic 측면 (∃ escape rate) 의 *분리* — prompt body §12 #4 carry-forward**. 본 broad survey 는 *kinetic metastability* (escape rate) 만 다룸; *thermodynamic local minimum* 의 *동의어* 로 사용 금지. 현 P-F-A1 Package I 만 Cat A; Package II 미수립 시 *완전한 metastability 주장 불가*.

---

## §5. Pillar 3 — Coarsening

### §5.1 Single-formation 에서의 부재

Single-formation 에는 *coarsening* 없음 (K=1 stable). Coarsening 은 *multi-formation phenomenon*.

### §5.2 Multi-formation lift candidate

Classical Allen-Cahn / Cahn-Hilliard coarsening:
- *LSW* (Lifshitz-Slyozov-Wagner) growth: $\langle r \rangle \sim t^{1/3}$ (Cahn-Hilliard) 또는 $t^{1/2}$ (Allen-Cahn).
- SCC multi-K 의 coarsening: K → K-1 cascades 의 *time-scaling*. `k_selection_b_kramers.md §7.4` 가 LSW-like coarsening 언급.

### §5.3 SCC distinctive feature

Allen-Cahn 의 coarsening 은 *length-scale 단일*; SCC 의 coarsening 은 *length + K + σ-tuple* 의 *3-D* coarsening. **prompt body §8 #4 (외부 reductive 환원 금지) 강제**:
- "SCC coarsening = Allen-Cahn coarsening" 형식의 환원 금지.
- 대조 (contrastive) 만 가능: "SCC coarsening 은 K-status 의 *discrete* jump 를 포함하므로 Allen-Cahn 의 *continuous* 와 다름".

### §5.4 외부 reference

| Reference | 적용 |
|---|---|
| Bray, *Theory of phase-ordering kinetics*, Adv. Phys. 51 (2002) | review of coarsening dynamics |
| Pego, *Front migration in the nonlinear Cahn-Hilliard equation*, Proc. Roy. Soc. A 422 (1989) | bubble growth → LSW |
| Lifshitz-Slyozov 1961, Wagner 1961 | classical LSW |

### §5.5 Success / failure modes

- **Success**: $K_\mathrm{act}(t)$ 의 *power-law decay* $K(t) \sim t^{-\alpha}$ 의 explicit exponent + dependence on cluster shape (σ-tuples).
- **Failure**: SCC coarsening 의 *discrete K-jump* 가 *Allen-Cahn LSW* 의 *continuous* coarsening 과 *호환 불가* — *separate framework* 필요.

---

## §6. 3-pillar 통합 의 *unlock chain*

| Pillar | OP-0005-DYN 의 partial closure 정도 |
|---|---|
| Pillar 1 Nucleation | K → K+1 escape rate Cat B (W9+) |
| Pillar 2 Metastability | K-basin time-scale separation Cat B (W10+) |
| Pillar 3 Coarsening | $K_\mathrm{act}(t)$ power-law Cat C (W11+) |

총 effort: **~5-8 sessions** (W9-W11). Pillar 1 가 가장 직접 (P-F-A1 Package I Cat A 가 입력).

---

## §7. 기존 working 과의 관계

본 broad_survey_B3 = `k_selection_b_kramers.md §4-7` + `n1_kramers_extension.md` 의 *multi-formation lift candidate* 식별 + 3-pillar 분류 + 외부 reference 매핑. *재정리 아님* — *W9+ staging 의 분류 입력*.

- **Silent resolution 회피**: OP-0005-DYN OPEN 유지. 3-pillar 모두 *Cat B/C target* 만; *해결 주장 부재*.

---

## §8. Hard constraint verification

- [x] canonical 직접 수정 0
- [x] silent OP resolution 0 — OP-0005-DYN OPEN 유지
- [x] Research OS 재도입 0
- [x] reductive 환원 0 — Allen-Cahn / Cahn-Hilliard / LSW 모두 *contrastive* tool (§5.3 명시)
- [x] primitive 전도 0
- [x] 4 에너지 항 병합 0
- [x] K 이중 취급 0 — K_act 정수 commit; coarsening 의 $K_\mathrm{act}(t)$ 도 *jump* 형
- [x] zero-temp metastability flag — §4.5 명시 (kinetic vs thermodynamic 분리 강조)
- [x] OMC 풀 오케스트레이션 0

---

## §9. Status

**Type**: working broad survey LIGHTER, P1 baseline.
**Effort to-date**: 1 session (본 W8 Day 1 Track B3).
**Next session**: W9+ `op0005_dyn_pillar1_nucleation.md` (Pillar 1 first attack), `op0005_dyn_pillar2_metastability.md` (W10+ Pillar 2), `op0005_dyn_pillar3_coarsening.md` (W11+ Pillar 3).
**Promotion path**: 각 pillar 의 Cat B 별도 등록 → Package II 완료 시 통합 Cat A (W12+?).

---

*broad_survey_B3.md 종료. OP-0005-DYN W9+ staging input — 3-pillar candidate identification 완료. canonical 0 edits. 증명 시도 0.*
