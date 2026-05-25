---
type: working/sensing_pipeline/index
version: v0
date: 2026-05-25
status: Active — DEFINITION-DRAFT + THEOREM-CANDIDATE
purpose: |
  Sensing pipeline working subdirectory navigation hub.
  9-document mathematical-physics formalization of the
  Raw sensing → perceptual field transformation,
  positioned as a PARALLEL substrate layer to PAI (not under PAI).
parent_substrate: CV-1.20 (SCC) — unchanged, 102 claims preserved
parallel_layer: PAI-PIVOT-2026-05-21 — no bridge attempted in this layer
constraint_compliance:
  canonical_theorem_changes: 0
  claim_count: 102 (unchanged)
  CV_version: CV-1.20 (unchanged)
  scc_edits: 0
  pai_canonical_edits: 0
  retractions_revived: 0
  register: DEFINITION-DRAFT (objects) + THEOREM-CANDIDATE (propositions, no proofs)
---

> [!nav] Parent: [[../INDEX|working/INDEX.md]] · Parallel: [[../../canonical/perception_action_interpretation_pivot_2026_05_21|PAI Pivot]] · Substrate: [[../../canonical/canonical|canonical.md (CV-1.20)]] · Plan: `/Users/ojaehong/.claude/plans/gleaming-juggling-crab.md`

# Sensing Pipeline — Mathematical-Physics Bootstrap

## 0. 본 working subdirectory 의 위치

본 디렉토리는 **PAI 의 입력측 substrate** 를 *수리물리학적으로* 형식화한다. 다루는 단계:

```
[광자]──Stage 0──[광수용기]──Stage 1──[내부 망막]──Stage 2──[신경절세포]──Stage 3──[시신경]
```

대화 컨텍스트 (요약): 사용자는 (1) SCC 가 *substrate* 로 격하된 이후의 새 axis 를 탐색 중이며, (2) Raw → 인식의 장 변환을 (Ω, σ) Tier 2 수준에서 commit 하고, (3) 그 변환의 물리적 기질을 광센서 / 망막으로 잡았다. 본 디렉토리는 이 변환의 *수학적 어휘*를 구축한다.

**중요**: 본 디렉토리는 PAI 의 *interpretation invariance* 질문에 답하지 않는다. PAI Phase 1 ($\Delta_{\text{interp}}$ 정의) 가 가정하는 "perceptual individuation" 자체를 *생산하는 메커니즘*을 다룬다. 따라서 PAI 와 **병렬** 이며, 본 layer 가 자기-안정된 이후에만 PAI 와의 다리를 별도 plan 에서 시도한다.

---

## 1. 문서 목록 (9개)

| # | 파일 | 역할 | 상태 |
|---|------|------|------|
| 00 | [[00_INDEX]] | 본 파일 — 네비게이션, 색인 | Active |
| 01 | [[01_framework_master]] | 마스터 아키텍처 + 수학 도구 포괄 survey | Draft pending |
| 02 | [[02_stage0_photon_point_process]] | Stage 0 — 광자 도래 점과정 | Draft pending |
| 03 | [[03_stage1_photoreceptor_sde]] | Stage 1 — 광수용기 SDE | Draft pending |
| 04 | [[04_stage2_inner_retinal_algebra]] | Stage 2 — 내부 망막 대수 (ON/OFF + DoG + 운동) | Draft pending |
| 05 | [[05_stage3_ganglion_spike_encoding]] | Stage 3 — 신경절세포 스파이크 부호화 | Draft pending |
| 06 | [[06_endtoend_information_bound]] | Cross-cutting — 정보론적 회계 | Draft pending |
| 07 | [[07_omega_sigma_lift]] | (Ω, σ) Tier 2 프레임워크로의 lift | Draft pending |
| 08 | [[08_open_problems_sp]] | OP-SP 통합 등록부 | Draft pending |

---

## 2. Theorem-Candidate 통합 색인 (TC-SP)

본 디렉토리에서 등록되는 모든 명제는 **THEOREM-CANDIDATE** 등록. 본 디렉토리 어느 문서도 증명을 시도하지 않는다. 증명은 별도 후속 plan.

| 코드 | 명제 | 등록 위치 |
|------|------|----------|
| TC-SP-1.1 | Composition: $\mathcal{K}_4 \circ \cdots \circ \mathcal{K}_1$ well-defined as stochastic kernel | 01 |
| TC-SP-1.2 | Data processing inequality: $I(\mathcal{S}_0; \mathcal{S}_i) \geq I(\mathcal{S}_0; \mathcal{S}_{i+1})$ | 01, 06 |
| TC-SP-1.3 | No retro-information: pipeline causal (time non-reversal) | 01 |
| TC-SP-0.1 | Stage 0 통계 = scene radiance × optics × QE 곱 | 02 |
| TC-SP-0.2 | Photon limit: 단광자 검출 = 1차 사건 (Baylor 1979 의 수학적 한계) | 02 |
| TC-SP-1.4 | Compression: Naka-Rushton 후 dynamic range ∝ log(input) | 03 |
| TC-SP-1.5 | Single-photon detectability under SNR conditions | 03 |
| TC-SP-2.1 | Riesz 분해: $V = V_{\text{ON}} - V_{\text{OFF}}$ uniqueness | 04 |
| TC-SP-2.2 | DoG zero-crossing = edge (Marr-Hildreth) | 04 |
| TC-SP-2.3 | DoG ≈ Bayesian MAP edge estimator under Brownian prior | 04 |
| TC-SP-2.4 | Adelson-Bergen energy = velocity-tuned slab in spacetime Fourier | 04 |
| TC-SP-2.5 | Reichardt ≡ motion energy under normalization | 04 |
| TC-SP-3.1 | Rate sufficiency under specified priors | 05 |
| TC-SP-3.2 | M/P latency asymmetry ↔ two distinct time axes (info-theoretic) | 05 |
| TC-SP-3.3 | 126:1 compression bound from peripheral spatial correlation | 05 |
| TC-SP-4.1 | End-to-end bound: $I(\text{scene}; \text{spikes}) \leq \min_i C_i$ | 06 |
| TC-SP-4.2 | Lossy-stage ranking (which stage loses most information) | 06 |
| TC-SP-4.3 | Naka-Rushton adaptation maximizes mutual information (Laughlin 1981) | 06 |
| TC-SP-5.1 | σ propagation: $\sigma_i \to \sigma_{i+1}$ functorial under $\mathcal{K}_i$ | 07 |
| TC-SP-5.2 | Tier 2 closure: 어떤 stage 도 Tier 4 metric/vector 본질적 요구 없음 | 07 |

목표 상한 ~20 — 본 등록부는 정확히 20개. 추가 시 TaskList 에 반영.

---

### 2.1 [2026-05-25 UPDATE] Post-Pass-3+4+5 Adversarial Verification

3-pass adversarial verification (9 attack patterns) + ruthless cleanup 후 활성 TC-SP 카운트:

**Active TC-SP**: **1** (down from 21)

| 코드 | 명제 | 상태 |
|------|------|------|
| **TC-SP-0.1a** | Stage 0 Poisson 통계 = Λ 의 함수 | **CONFIRMED** (9 patterns 통과) |

**Retracted TC-SP**: **21** (5 P3 + 4 P3-weakened-then-P4-deleted + 5 P4 + 7 P5)

| 코드 | Pass | 사유 |
|------|------|------|
| TC-SP-0.1b | P3 | Definition restatement (#18 tautology); Stiles-Crawford violation (#5) |
| TC-SP-1.1 | P4 | Markov hypothesis violated by retinal adaptation (#51) |
| TC-SP-1.2 | P5 | Shannon DPI vs retinal feedback/coupling (#11 model misspec) |
| TC-SP-1.3 | P4 (escalated) | Causality def + Adelson-Bergen non-causal Gabor + channel coupling |
| TC-SP-1.4 | P4 (escalated) | Adaptation hypothesis insufficient; Pavliotis-Stuart ergodicity unverified |
| TC-SP-1.5 | P3 | Tautological SNR definition + CLE copy number violation |
| TC-SP-0.2 | P5 | Photon arrival math ≠ rod detection biology |
| TC-SP-2.1 | P5 | Riesz generic ≠ retinal ON/OFF (overlap + tonic + parallel cascades) |
| TC-SP-2.2 | P4 | Sensor edge + pixel noise correlation (#46 + #51) |
| TC-SP-2.3 | P4 (escalated) | DC pole + sparse coding + non-iid pixels |
| TC-SP-2.4 | P5 | Adelson-Bergen cortical model ≠ retinal DSGC (starburst amacrine) |
| TC-SP-2.5 | P5 | Reichardt insect/Adelson-Bergen cortical — neither retinal |
| TC-SP-2.6 | P5 | PCA alignment ≠ causal optimization (phylogenetic accident) |
| TC-SP-3.1 | P4 | Cox conditional-independence violation (double confirmed #5 + #51) |
| TC-SP-3.2 | P3 | Pure rename of latency difference (#18) |
| TC-SP-3.3 | P4 (escalated) | W_max boundary inherits divergence; overlapping RF correlation |
| TC-SP-4.1 | P5 | Shannon capacity ≠ retinal task-relevant Fisher information |
| TC-SP-4.2 | P4 | Inherits TC-SP-3.1; ranking ties; population correlations |
| TC-SP-4.3 | P4 | Additive Gaussian on bounded range + iid violation |
| TC-SP-5.1 | P3 | σ functoriality false (constant maps, broadly-mixing) |
| TC-SP-5.2 | P3 | Tier 2 closure definitional fiat (저자 본인 admit) |

**Survival rate**: 1 / 22 = **4.5%**.

자세한 ledger: [[09_verification_pass3|09_verification_pass3.md]] §11–14.

**Stable state 선언**: 추가 attack 의 marginal value 매우 낮음 — 본 corpus 의 *register 자체* 가 *biological theorem candidates* 가 아니라 *mathematical observations with retinal motivation* 으로 재해석 필요.

---

## 3. Open Problems (OP-SP) 통합 등록부

본 디렉토리에서 등록되는 모든 open problems. 어느 것도 RESOLVED 로 이동시키지 않음 (본 디렉토리 내에서는).

| 코드 | 문제 | 등록 위치 | 심각도 |
|------|------|----------|-------|
| OP-SP-001 | 양자 결맞음(coherence) 무시의 정당화 | 02 | Low |
| OP-SP-002 | Naka-Rushton $I_{50}$ 적응 동역학의 형식화 | 03 | Medium |
| OP-SP-003 | 다채널 분기 = fiber bundle section? | 04 | Medium |
| OP-SP-004 | 색 대립축 (L-M, S-(L+M)) 의 군론적 정당화 | 04 | High |
| OP-SP-005 | 비균질 표본화 (fovea vs periphery) 의 sheaf 처리 | 05 | Medium |
| OP-SP-006 | SCC 의 $u_t$ ↔ 어느 stage 출력? | 07 | High |
| OP-SP-007 | Stage 4 cut location (LGN? V1 input?) | 08 | Medium |
| OP-SP-008 | 색 대립의 군론적 정당화 (재진술 / OP-SP-004 와 중복 검토) | 08 | (merged) |
| OP-SP-009 | 적응 시상수 hierarchy (msec ~ hour scales) | 08 | Medium |
| OP-SP-010 | Top-down feedback (V1→LGN→retina) 무시 정당화 | 08 | Low |

---

## 4. 정합성 ledger (constraint compliance)

본 디렉토리 작업 전후로 반드시 0 유지:

- [ ] `canonical/canonical.md` 수정 라인 수
- [ ] `canonical/theorem_status.md` 수정 라인 수
- [ ] `canonical/perception_action_interpretation_pivot_2026_05_21.md` 수정 라인 수
- [ ] `canonical/PAI_ROADMAP.md` 수정 라인 수
- [ ] 8 retraction 부활 시도 수 (EW universality / Model A / $t_\times$ / $D_f$ / H-int / closure RG / $D_f=11/8$ / $k(k+1)/2-1$)
- [ ] macro_audit §9 hard-stop 위반 수

`THEORY/working/INDEX.md` 와 `THEORY/CHANGELOG.md` 에는 *각 1줄* 진입 허용 (등록 목적).

---

## 5. Master Framework 한 줄 요약

본 디렉토리의 마스터 객체:

$$
\boxed{\;\mathcal{S}_0 \xrightarrow{\;\mathcal{K}_1\;} \mathcal{S}_1 \xrightarrow{\;\mathcal{K}_2\;} \mathcal{S}_2 \xrightarrow{\;\mathcal{K}_3\;} \mathcal{S}_3 \xrightarrow{\;\mathcal{K}_4\;} \mathcal{S}_4\;}
$$

- $\mathcal{S}_i$ = stage $i$ 의 상태공간 (measurable / function / measure space)
- $\mathcal{K}_i$ = stage $i-1 \to i$ 의 stochastic Markov kernel
- 전체 = stratified stochastic kernel pipeline (Bayesian network with deterministic temporal order)

각 단계의 구체 정의는 02~05 에서. 추상 골격은 01 에서. Cross-cutting 은 06~07 에서.

---

## 6. 읽기 순서

**처음 진입**: 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08

**Stage 별 deep dive**: 01 ($\mathcal{K}_i$ 추상 형식 이해) → 해당 stage 문서

**(Ω, σ) Tier 2 연결만 보고 싶다면**: 07 → 01 → 본 INDEX §5

**Open problems 만**: 08

---

## 7. 본 디렉토리가 *시도하지 않는 것* (non-goals)

1. **증명** — 모든 TC-SP-N.M 은 진술만; 증명은 별도 후속 plan
2. **PAI 와의 다리** — $\Delta_{\text{interp}}$, $\mathcal{A}(u)$, IPF 와의 연결은 미시도
3. **SCC canonical 수정** — 102 claims 보존
4. **CV 승격** — 본 디렉토리 전체가 `working/` 내부 (DEFINITION-DRAFT)
5. **biological completeness** — LGN feedback, top-down attention, melanopsin 등은 OP 로 둠
6. **코드 / 시뮬레이션 / 실험** — 수학적 정식화 only

---

*INDEX v0 — 작성된 문서 수 0/8. Plan 시퀀스대로 01 부터 채워나감. 각 문서 안정화 후 본 INDEX 의 상태 컬럼과 TC/OP 색인 갱신.*
