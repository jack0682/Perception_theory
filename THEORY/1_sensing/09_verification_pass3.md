---
type: working/sensing_pipeline/verification
version: v0
date: 2026-05-25
status: COMPLETED (single-pass adversarial verification ledger)
purpose: |
  Math-olympiad style adversarial verification of all 20 TC-SP candidates
  using 4 attack patterns (#4 RH-specialization, #18 tautology, #40 too-clean
  general lemma, #5 hypothesis recheck). Each pattern applied by a fresh-context
  Opus critic agent reading all 8 deepened docs. Asymmetric vote: 4 HOLDS = CONFIRMED,
  2+ HOLE FOUND = REFUTED, otherwise UNCLEAR.
register: VERIFICATION-LEDGER (descriptive; no theorem promotion, no canonical changes)
parent: 01_framework_master
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  new_TC_codes: 0
  new_OP_codes: 0 (none registered in this pass — see §6)
  inline_doc_edits_to_02_07: 0 (status NOT marked in stage docs; this ledger is the only place)
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[08_open_problems_sp]] · Source verifiers: 4 fresh-context Opus critics (math-olympiad #4 + #18 + #40 + #5 patterns)

# Pass 3 — Adversarial Verification Ledger

## 0. 본 문서의 위치

본 문서는 Pass 2 deepening 후의 20 TC-SP-N.M candidates 에 *math-olympiad style adversarial verification* 을 적용한 결과의 통합 ledger 다. 4개 *fresh-context Opus critic agent* 가 각각 하나의 attack pattern 을 specialized 적용:

- **Pattern #4** (RH-style specialization): 일반화 시 famous open problem 을 푸는가?
- **Pattern #18** (tautological extraction): proof 가 conclusion 의 재진술인가?
- **Pattern #40** (too-clean general lemma): general form 에 simple counterexample 존재? retinal specifics 가 articulated 되었나?
- **Pattern #5** (hypothesis recheck): 인용 정리 / 가정의 *exact hypothesis* 가 retinal context 에서 만족되는가?

각 verifier 는:
- **무도구, 무계산, 무웹** (math-olympiad 규칙)
- **Fresh context** — 다른 verifier 의 verdict 미인지
- 20 TC 전체에 본인 pattern 적용
- HOLDS / HOLE FOUND / UNCLEAR 표 반환

**Asymmetric vote 임계** (math-olympiad 표준):
- **4 HOLDS → CONFIRMED** (이 corpus 에서 모든 pattern 통과)
- **2+ HOLE FOUND → REFUTED** (두 독립 pattern 이 gap 발견)
- 그 외 → **UNCLEAR** (추가 검증 필요)

본 ledger 는 *descriptive*: stage 문서 02-07 의 본문 *수정하지 않음*. TC-SP-N.M 라벨 어디서도 *RESOLVED*, *REVISED*, *RETRACTED* 등 의 status 마킹 안 함. 본 ledger 가 단일 권위.

---

## 1. 개별 TC-SP verdict matrix + Pass 3 disposition (집행 완료 2026-05-25)

**Pass 3 cleanup 집행됨**: REFUTED 9개 중 5개 DELETE, 4개 WEAKEN, 1개 SPLIT (TC-SP-0.1 → 0.1a 유지 + 0.1b 삭제).

| TC-SP | #4 RH | #18 Taut | #40 TooClean | #5 Hyp | HOLDS | HOLE | UNCLEAR | **Pass 3 Verdict** | **Disposition (Phase 2 집행)** |
|-------|-------|----------|--------------|--------|-------|------|---------|---------------------|------------------------------------|
| **0.1a** Stats determined by Λ | HOLDS | (split) | HOLDS | HOLDS | 3+ | 0 | 0 | (post-split) CONFIRMED | **RETAINED** (split out clean part) |
| **0.1b** Factorization formula | HOLDS | HOLE | HOLDS | HOLE | 2 | 2 | 0 | REFUTED | **DELETED** ([[02_stage0_photon_point_process#TC-SP-0.1b]]) |
| **0.2** Photon limit | HOLDS | HOLDS | HOLDS | HOLDS | 4 | 0 | 0 | CONFIRMED | **RETAINED** |
| **1.1** Kernel composition | HOLDS | HOLDS | HOLDS | HOLE | 3 | 1 | 0 | UNCLEAR | **RETAINED** (UNCLEAR, Pass 4 target) |
| **1.2** DPI chain | HOLDS | HOLDS | HOLDS | HOLDS | 4 | 0 | 0 | CONFIRMED | **RETAINED** |
| **1.3** Causal pipeline | HOLDS | HOLE | HOLDS | HOLE | 2 | 2 | 0 | REFUTED | **WEAKENED** (qualifiers (Q1)(Q2) added; [[01_framework_master#TC-SP-1.3]]) |
| **1.4** Logarithmic compression | HOLDS | HOLDS | HOLE | HOLE | 2 | 2 | 0 | REFUTED | **WEAKENED** (qualifiers (Q1)(Q2)(Q3); [[03_stage1_photoreceptor_sde#TC-SP-1.4]]) |
| **1.5** Single-photon detectability | HOLDS | HOLE | HOLDS | HOLE | 2 | 2 | 0 | REFUTED | **DELETED** ([[03_stage1_photoreceptor_sde#TC-SP-1.5]]) |
| **2.1** Riesz uniqueness | HOLDS | HOLDS | HOLDS | HOLDS | 4 | 0 | 0 | CONFIRMED | **RETAINED** |
| **2.2** DoG edge selectivity | HOLDS | HOLDS | HOLE | HOLDS | 3 | 1 | 0 | UNCLEAR | **RETAINED** (UNCLEAR, Pass 4 target) |
| **2.3** DoG Bayesian MAP | HOLDS | HOLDS | HOLE | HOLE | 2 | 2 | 0 | REFUTED | **WEAKENED** (qualifiers (Q1)(Q2)(Q3); [[04_stage2_inner_retinal_algebra#TC-SP-2.3]]) |
| **2.4** Adelson-Bergen velocity slab | HOLDS | HOLDS | HOLDS | HOLDS | 4 | 0 | 0 | CONFIRMED | **RETAINED** |
| **2.5** Reichardt ≡ energy | HOLDS | HOLDS | HOLDS | HOLDS* | 4 | 0 | 0 | CONFIRMED | **RETAINED** |
| **2.6** Color PCA | (silent) | (silent) | (silent) | HOLDS-candidate | partial | 0 | 0 | PARTIAL | **RETAINED** (Pass 4 will fully verify) |
| **3.1** Rate sufficiency | HOLDS | HOLDS | HOLDS-conditional | HOLE | 3 | 1 | 0 | UNCLEAR | **RETAINED** (UNCLEAR, Pass 4 target) |
| **3.2** Latency asymmetry | HOLDS | HOLE | HOLDS | HOLE-minor | 2 | 2 | 0 | REFUTED | **DELETED** ([[05_stage3_ganglion_spike_encoding#TC-SP-3.2]]) |
| **3.3** Compression bound | HOLDS | HOLE | HOLE | HOLDS-upper | 2 | 2 | 0 | REFUTED | **WEAKENED** (qualifiers (Q1)(Q2)(Q3) + 126:1 anatomical fact 분리; [[05_stage3_ganglion_spike_encoding#TC-SP-3.3]]) |
| **4.1** End-to-end bound | HOLDS | HOLDS | HOLDS | HOLDS | 4 | 0 | 0 | CONFIRMED | **RETAINED** |
| **4.2** Lossy-stage ranking | UNCLEAR | UNCLEAR | HOLDS-conditional | HOLE | 1 | 1 | 2 | UNCLEAR | **RETAINED** (UNCLEAR, Pass 4 target; depends on TC-SP-3.1) |
| **4.3** Naka-Rushton optimality | HOLDS | HOLDS | HOLDS | HOLE | 3 | 1 | 0 | UNCLEAR | **RETAINED** (UNCLEAR, Pass 4 target) |
| **5.1** σ propagation functorial | HOLDS | HOLE | HOLE | HOLE | 1 | 3 | 0 | REFUTED (strong) | **DELETED** (case analysis 본문 유지, TC 자격 박탈; [[07_omega_sigma_lift#TC-SP-5.1]]) |
| **5.2** Tier 2 closure | HOLDS | HOLE | HOLE | HOLE | 1 | 3 | 0 | REFUTED (strong) | **DELETED** (Definition 4.1/4.2 본문 유지, TC 자격 박탈; [[07_omega_sigma_lift#TC-SP-5.2]]) |

---

## 2. 통계 요약

- **CONFIRMED**: 6 (TC-SP-0.2, 1.2, 2.1, 2.4, 2.5, 4.1)
- **REFUTED**: 9 (TC-SP-0.1, 1.3, 1.4, 1.5, 2.3, 3.2, 3.3, 5.1, 5.2)
- **UNCLEAR**: 5 (TC-SP-1.1, 2.2, 3.1, 4.2, 4.3)
- **PARTIAL**: 1 (TC-SP-2.6 — silent in 3 of 4 verifiers; non-zero candidate)

총 21 = 6 + 9 + 5 + 1.

CONFIRMED 비율: **28.6%** (6 / 21)
REFUTED 비율: **42.9%** (9 / 21)
미확정 (UNCLEAR + PARTIAL): **28.6%** (6 / 21)

---

## 3. CONFIRMED — 6 TC-SP 의 강한 candidates

**전체 4개 pattern 모두 HOLDS**. 본 directory 의 *대표 정리 후보* 들. 후속 plan 에서 *full proof* 작업의 자연 target:

| TC-SP | 명제 | 위치 | 강도 분석 |
|-------|------|------|-----------|
| **0.2** | Photon limit (단광자 검출 = 1차 사건) | [[02_stage0_photon_point_process#TC-SP-0.2]] | Poisson Taylor 전개; Baylor 1979 empirical confirmation; CLE 가 violated 되어도 *single-event regime* 은 영향 없음 |
| **1.2** | DPI chain (mutual info 단조 감소) | [[01_framework_master#TC-SP-1.2]] | Cover-Thomas Thm 2.8.1 의 직접 적용; SSKP construction 이 Markov 보장; verifier #5 가 invocation 의 hypothesis 깨끗 확인 |
| **2.1** | Riesz uniqueness ($V = V_+ - V_-$) | [[04_stage2_inner_retinal_algebra#TC-SP-2.1]] | Aliprantis-Burkinshaw Thm 1.5 의 직접 적용; "best-justified TC-SP in directory" (verifier #5); 모든 pattern HOLDS |
| **2.4** | Adelson-Bergen velocity slab | [[04_stage2_inner_retinal_algebra#TC-SP-2.4]] | Spacetime Fourier + Gabor 의 direct 결과; Parseval hypothesis 깨끗; mathematical content (slab thickness) 진짜 |
| **2.5** | Reichardt ≡ motion energy | [[04_stage2_inner_retinal_algebra#TC-SP-2.5]] | Adelson-Bergen 1985 §4 의 알려진 동치; Wiener-Khinchin 의 진짜 적용; *load-bearing qualifier ("under normalization") 가 statement 안에 명시됨* |
| **4.1** | End-to-end capacity ≤ min stage capacity | [[06_endtoend_information_bound#TC-SP-4.1]] | DPI 의 직접 corollary; Shannon classical; capacity 정의로부터 자명 |

이 6개는 *다음 단계 작업의 안전한 출발점*: full proof attempt, canonical-track promotion, 또는 SCC 의 substrate-canonical 과의 연결.

---

## 4. REFUTED — 9 TC-SP 의 약점 분석

**2개 이상의 pattern 이 독립적으로 HOLE 발견**. 본 directory 의 *수정 또는 약화 필요* 후보. **본 ledger 는 수정하지 않음** — 단지 식별만.

### 4.1 TC-SP-0.1 — Stage 0 statistics factorization

- **#18 hole**: $\Lambda = L \cdot T \cdot \eta \cdot (h\nu)^{-1}$ 가 §2.5 의 *정의*; 정리가 정의 재진술
- **#5 hole**: Stiles-Crawford 효과 + intraocular scatter 가 "marginalize-direction" 가정을 위반; aging lens 의 scatter 무시

**Convergence**: 두 패턴이 *다른 측면* 에서 hole 발견 — definitional engineering + physical hypothesis violation. 강한 refute signal.

**Fix path**: 첫 절 (Poisson 통계 = $\Lambda$ 가 결정) 와 둘째 절 (factorization formula) 분리. 첫 절은 genuine; 둘째 절은 *definition* 으로 격하.

### 4.2 TC-SP-1.3 — Causal pipeline

- **#18 hole**: 각 $K_i$ 가 *by construction* causal (Stage 4 = latency shift; SDE = forward integration); 정리 = 정의 집계
- **#5 hole**: Adelson-Bergen Gabor 가 canonical Fourier-tuning derivation 에서 *non-causal* (centered Gaussians); 저자 "causal version 채택" 명시하나 §5.3 의 velocity-slab proof 는 symmetric Gabor 사용; 또한 cortico-fugal feedback (OP-SP-010) 가 *empirical real* 이나 TC 는 무조건 causality 주장

**Convergence**: 둘 다 본질적. Strong refute.

**Fix path**: 정리를 *conditional* 로 재진술: "feedback 무시 가정 하 + causal-Gabor 채택 시 pipeline causal." 또는 *axiom* 으로 격하 ("우리는 causal pipeline 을 가정한다").

### 4.3 TC-SP-1.4 — Logarithmic compression

- **#40 hole**: $n \to \infty$ Hill = step function → $\Delta R/\Delta I \neq 1/\bar{I}$; *fixed* $I_{50}$ Hill 은 *narrow regime* 에서만 Weber; statement 가 adaptive-sliding qualifier 와 log-normal prior qualifier 를 strip
- **#5 hole**: Pavliotis-Stuart §16 averaging 의 가정 (fast SDE 의 uniform ergodicity under fixed slow parameter) 가 jump-diffusion + Poisson input 에 대해 verify 안 됨

**Convergence**: 둘 다 *generality* / *invocation hypothesis* 의 미articulated 가정 — qualifier stripping.

**Fix path**: INDEX one-liner 을 "Naka-Rushton 응답 후 *with adaptive $I_{50} = \kappa \bar{I}$ AND log-normal natural light* 의 dynamic range ∝ log(input)" 로 명시. Ergodicity 는 OP 로 등록 (이미 OP-SP-002 와 연관).

### 4.4 TC-SP-1.5 — Single-photon detectability

- **#18 hole**: "Detectable" 가 SNR ≥ 1 로 operationally 정의됨; 정리가 SNR ≥ 1 → detectable 주장 — *pure self-reference*; 저자 "SNR 정의로부터 자명" admit
- **#5 hole**: CLE 의 copy number ≳ 20-100 가정이 R* (rate-limiting species; copy number = 1) 에 대해 *명시적으로* 위반; 광수용기 noise 는 discrete bumps 로 *non-Gaussian* 이나 정리는 Gaussian SNR 가정

**Convergence**: Tautology + hypothesis violation. Strong refute.

**Fix path**: Empirical 사실 (Baylor 1979 의 단광자 detection) 을 *empirical observation* 으로 명시; *theorem* 으로 다루지 않음. Or: SNR 의 *operational* 정의를 *empirical detection task* 의 정확한 기준 (예: Hecht-Shlaer-Pirenne 의 5-7 photon threshold) 으로 elaborate.

### 4.5 TC-SP-2.3 — DoG Bayesian MAP edge

- **#40 hole**: General Gaussian prior 는 DoG 를 주지 않음; specifically $P_V(\xi) = A/|\xi|^2$ (Brownian) 가 *load-bearing*; white prior → identity inverse; $1/|\xi|^4$ → bi-Laplacian; INDEX "Brownian prior" 가 smuggled 단어
- **#5 hole**: 자연 이미지는 *empirically non-Gaussian* (heavy-tailed wavelet coefficients — Ruderman 1994, Simoncelli 1999, Olshausen-Field 1996 sparse coding); $1/|\xi|^2$ 는 mean 에서만 성립; Gaussian noise 가정도 low-light 에서 위반 (Poisson-dominated)

**Convergence**: 일반화 실패 + empirical prior 위반.

**Fix path**: Statement 약화: "*Gaussian prior + $1/|\xi|^2$ spectrum* 가정 하" 를 명시; *natural images are not Gaussian* 을 ackonwledge; sparse coding 과의 연결을 후속 작업으로.

### 4.6 TC-SP-3.2 — M/P latency asymmetry → two time axes

- **#18 hole**: "Two time axes" = "two distinct constant latencies" 의 *rename* — 정의 재진술; 7-bit alignment cost 는 heuristic (σ_Δτ ≈ 1 ms stipulation), formally derived 아님
- **#5 hole (minor)**: 시간적 $1/\omega^2$ spectrum 이 Field 1987 의 *spatial* 결과로부터 extrapolated 되었으나 *separate empirical assertion* (Dong-Atick 1995 가 시간 통계는 다르다고 보임)

**Convergence**: Tautology + empirical extrapolation 미검증. Refute.

**Fix path**: "Two distinct time axes require alignment" 를 *명백한 정의적 사실* 로 인정하고 정리 자격 박탈. Alignment bit cost (7 bits) 는 *별도 estimate* 로 분리, Cramér-Rao 의 hypothesis 와 함께 명시.

### 4.7 TC-SP-3.3 — Peripheral compression bound

- **#18 hole**: 126:1 figure 는 *anatomical* (photoreceptor:ganglion ratio); rate-distortion calculation 은 $\int |\xi|^{-2} 2\pi f \, df$ 가 *발산* (저자 admit); $\alpha > 2$ 로 hand-wave 보정; *anatomical* 와 *information-theoretic* 사이의 연결이 juxtaposed, not derived
- **#40 hole**: 자연 이미지 1/f² spectrum 의 *infinite integral correlation length* (general form fails); edges (discontinuities) 는 pooling 으로 destroyed regardless of $L_{\text{corr}}$; non-Gaussian/non-stationary fields

**Convergence**: 핵심 산식 발산 + general form 실패.

**Fix path**: 126:1 을 *anatomical fact* 로 명시 (정리 아님); compression bound 의 정량 statement 는 *windowed* 또는 *bandlimited natural image patch* 로 약화; full rate-distortion 은 OP-SP-005 (sheaf) 와 합쳐서 후속.

### 4.8 TC-SP-5.1 — σ propagation functorial

- **#18 hole**: $\sigma_i$ 가 pushed σ 를 흡수하도록 *post-hoc 정의* — 1→2 transition 에서 σ_2^natural 이 DoG output structure 까지 포함하도록 *expanded*; "non-trivial functoriality" 라는 label 이 *engineering* 의 wrapper
- **#40 hole**: General form 의 obvious counterexamples — *constant map* 은 모든 σ-pair 를 diagonal 로 push (pushed σ trivial); *broadly-mixing kernel* 은 pushed σ 가 empty 또는 universal; σ-confluence 는 kernel 과 target tolerance 의 *specific compatibility* 요구 — generic 아님
- **#5 hole**: 5-stage retinal instance 의 verification 이 *case-by-case* + *regularity 가 required 만 stated, not verified* (DoG 는 non-compact support, but compact-support 가정됨)

**Convergence**: *Strong* refute. 3개 pattern 이 동의.

**Fix path**: Functoriality 주장 *완전 약화*: "5-stage retinal SSKP 에 대해, *상호 regularity 조건* 만족 시 σ propagation 이 잘 정의됨." 그 조건들을 *axiom 으로* 등록하고 검증은 별도. General functoriality 는 *false-as-stated* 로 명시.

### 4.9 TC-SP-5.2 — Tier 2 closure

- **#18 hole**: σ_i 가 *Tier 4 norm 으로 계산되지만 binary threshold 후 Tier 2 label* — *definitional fiat*; 저자 §4 명시적 admit "증명 어려움. '본질적으로 요구하지 않는다' 의 완전 형식화" — meta-OP 임을 본인이 인정
- **#40 hole**: Stage 1 의 SDE drift $-\tau^{-1}(V - V_{\text{rest}}) dt + \sigma dW$ 가 본질적으로 Tier 4 vector structure 요구; "implementation tool vs. axiom-level data" 의 distinction 이 형식화 안 됨
- **#5 hole**: Tier 2 closure 가 category-theoretic forgetful functor 의 *not-yet-constructed* 형식에 의존; threshold parameter 자체가 Tier 3 datum

**Convergence**: *Strongest* refute — 저자 본인이 formalization gap 명시 admit.

**Fix path**: 정리 자격 *명확히 박탈*. "Tier 2 closure 는 *conjecture-with-evidence* 이며 formalization 은 OP." Stage 별로 *어떤 implementation tool* 이 Tier 4 인지, *output binarization* 이 어떻게 Tier 2 로 falling back 하는지 명시.

---

## 5. UNCLEAR — 5 TC-SP 의 추가 검증 필요

3/4 HOLDS or split — math-olympiad 규칙으로는 *추가 verifier* 추천. 본 pass 에서는 미실시. 다음 plan 에서 추가 패턴 (#5 의 더 specific instance 또는 새 패턴) 으로 attack 권장.

| TC-SP | Single dissent | 분석 |
|-------|----------------|------|
| **1.1** Kernel composition | #5 (Polish on which topology? Stage 1 function space) | Topology 의 ambiguity (uniform vs uniform-on-compacts) 명확화로 해결 가능 |
| **2.2** DoG edge selectivity | #40 (Marr-Hildreth counterexamples: curved, T-junctions, parallel edges) | Refined statement 의 (A1)(A2)(A3) 가정과 ε bound 가 honest — counterexamples 는 *acknowledged failure modes*; UNCLEAR 보다 *CONFIRMED-with-bound* 평가 가능 |
| **3.1** Rate sufficiency | #5 (Cox biologically violated — Berry-Meister 1998, Pillow 2008) | *Cox approximation regime* 으로 statement conditional 화 필요; high-firing-rate parvocellular 에선 OK; magnocellular bursting 에선 fail |
| **4.2** Lossy-stage ranking | #5 (Cox 위반 → ranking inherit), #4 + #18 UNCLEAR | TC-SP-3.1 의 fix 에 *전부 의존*; 일종의 derived TC, 부모 fix 후 재평가 |
| **4.3** Naka-Rushton optimality | #5 (Markov adaptation 위반 by OP-SP-009 multi-timescale; bounded-range hypothesis added beyond Laughlin 1981) | Laughlin 의 *명확한* hypothesis 와 본 statement 의 *enriched* hypothesis 의 차이 명시; OP-SP-009 advancement 가 필요 |

---

## 6. New OP-SP candidates from REFUTED TC-SPs (등록 *안 함*)

본 ledger 는 새 OP-SP-N 코드를 *registering 하지 않음* — [[00_INDEX#0. 본 working subdirectory 의 위치|00 §0]] 의 discipline. 단, 후속 plan 에서 등록할 *candidate gaps* 를 *식별만*:

| Refuted TC-SP | Identified gap (후속 plan 의 OP candidate) |
|---------------|-----------------------------------------------|
| 0.1 | OP-SP-(future): Stiles-Crawford 효과의 marginalization 정당화 |
| 1.3 | OP-SP-(future): Adelson-Bergen Gabor 의 causal version 의 velocity-tuning 정확성 |
| 1.4 | OP-SP-(future): Pavliotis-Stuart averaging hypothesis 의 jump-diffusion 검증 (OP-SP-002 의 sharpening) |
| 1.5 | OP-SP-(future): Single-photon detection 의 *non-Gaussian* (discrete-bump) decision theory |
| 2.3 | OP-SP-(future): Sparse-coding prior 하의 DoG-like Bayesian estimator |
| 3.2 | OP-SP-(future): Temporal spectrum extrapolation 의 empirical justification (Dong-Atick 1995 와 정합) |
| 3.3 | OP-SP-(future): Bandlimited natural image patch 위의 rate-distortion bound (anatomy-information 연결) |
| 5.1 | OP-SP-(future): σ-propagation 의 *regularity condition* 의 형식화 (kernel support vs target tolerance compatibility) |
| 5.2 | OP-SP-(future): Tier 2 closure 의 forgetful-functor 형식 — Markov category → Tier2 category |

이들 9개 후보 OP 가 등록된다면 14 + 9 = 23 OP-SP. 본 작업에서는 *등록 deferred*.

---

## 7. Methodology — 본 ledger 의 방법론적 한계

### 7.1 Single-pass (no follow-up extension)

Math-olympiad 표준은 *up to 5 verifiers per TC + asymmetric vote with pigeonhole exit*. 본 pass 는 *exactly 4 verifiers* (one per pattern) — extension 없이. UNCLEAR 의 5개는 *strict* 한 평가가 아니라 *pending*.

### 7.2 Pattern selection

사용자 선택은 #4 + #18 + #40 + #5. 본 corpus 에 *not applied*:
- #6 (divergent regularization): TC-SP-3.3 의 divergent integral 사례에 직접 적용 가능했음 — fix 시도가 hand-wave 임을 가시화
- #46 (boundary condition): Stage 0 의 wavelength domain Λ 의 endpoint 처리에 적용 가능
- #51 (independence assumption): Cox process 의 conditional independence assumption (TC-SP-3.1, 4.2) 의 보조 attack

추가 attack pattern 은 *Pass 4* 의 candidate.

### 7.3 Pattern specialist vs per-TC verifier

본 pass 의 architecture: 4 *pattern specialist* (각 specialist 가 20 TC 전체 보다). Math-olympiad 의 *fresh-context 원칙* 의 cross-pattern 보존되나 *cross-TC* 는 약화 (한 specialist 가 본인의 이전 TC 분석에 노출). 더 강한 isolation: *80 separate agents* (each: one TC × one pattern). Pass 4 candidate.

### 7.4 Verifier-of-verifier 미실시

Math-olympiad 의 *rebuttal round* (두 leading hypothesis 가 충돌 시 third verifier 의 *judging*) 본 pass 에서 미실시. UNCLEAR 의 5개에 적용 시 추가 collapse 가능.

### 7.5 Conditional pattern 의 *strictness*

Verifier 들이 "HOLDS with reservations" 또는 "HOLDS conditional" 등의 *intermediate* verdict 를 사용. 본 ledger 는 보수적으로 HOLDS 로 처리. *Strict* mode (모든 conditional 을 HOLE 으로 변환) 시 CONFIRMED 가 6 → ~3 로 감소.

---

## 8. 후속 작업 권고

### 우선순위 1 (REFUTED 9개에 대한 fix)

- TC-SP-5.1, 5.2 (양쪽 strong refute): *명확한 자격 박탈* + conjecture-with-evidence 로 재진술
- TC-SP-0.1, 1.4: *qualifier articulation* (statement 에 hypothesis 명시)
- TC-SP-1.3, 1.5: *operational definition* 의 self-reference 인정 + axiom 으로 격하
- TC-SP-2.3, 3.3: empirical hypothesis (Gaussian prior, finite correlation length) 의 명시
- TC-SP-3.2: 정리 자격 박탈 + bit cost estimate 분리

### 우선순위 2 (UNCLEAR 5개)

- Pass 4: 추가 pattern (#6, #46, #51) 적용
- 또는 per-TC × per-pattern 80 agent extension (full math-olympiad 표준)
- TC-SP-3.1, 4.2 가 paired — Cox approximation 의 regime conditioning 필요

### 우선순위 3 (CONFIRMED 6개)

- Full proof attempt — *next plan*
- SCC substrate-canonical 과의 연결 (OP-SP-006 의 *evidence* 역할)
- 별도 plan 에서 canonical-track promotion 후보

### 우선순위 4 (PARTIAL TC-SP-2.6)

- 다음 pass 에서 4 verifier 모두에게 *explicit instruction* 으로 포함

---

## 9. Constraint Compliance

| 항목 | 상태 |
|------|------|
| `canonical/` 수정 | **0 lines** ✓ |
| `CODE/scc/` 수정 | **0 lines** ✓ |
| PAI canonical 수정 | **0 lines** ✓ |
| `working/INDEX.md` 수정 | **0** (이 ledger 의 추가 entry 는 별도 결정) |
| `CHANGELOG.md` 수정 | **0** (이 ledger 의 entry 는 별도 결정) |
| Stage docs (02-07) 인라인 status 마킹 | **0** (사용자 commit: "09 ledger only, no inline updates") |
| 새 TC-SP 코드 | **0** |
| 새 OP-SP 코드 | **0** (후보 9개 식별만; 등록 deferred) |
| 8 retractions 부활 | **0** ✓ |
| RESOLVED / REVISED / RETRACTED 마킹 | **0** ✓ |

---

## 10. 한 줄 요약

> 4 pattern × 20 TC-SP adversarial verification: **6 CONFIRMED, 9 REFUTED, 5 UNCLEAR, 1 PARTIAL**. Refute 율 ~43% — DEFINITION-DRAFT register 의 expected attrition. Strong refute (3+ patterns) on **TC-SP-5.1, 5.2** (저자 본인 admit meta-OP). Strongest CONFIRMED (4/4 patterns) on **TC-SP-0.2, 1.2, 2.1, 2.4, 2.5, 4.1**. 본 ledger 가 단일 권위; stage docs 02-07 본문 unmodified.

---

*Pass 3 v0. 단일 pass. 후속 권고: Pass 4 (UNCLEAR 추가 검증) + REFUTED 9개 의 fix plan. PAI bridge 작업은 OP-SP-006 advancement 후 — 본 ledger 는 그 작업의 *empirical input* 으로 활용.*

---

## 11. Cleanup Execution Log (Pass 3 → Phase 2 집행 2026-05-25)

사용자 directive: *"모순은 가차없이 박탈 삭제하고 계속 찾아라"*. Plan: [[../../../../.omc/plans/sensing-pipeline-full-verify-cleanup|sensing-pipeline-full-verify-cleanup]].

### 11.1 집행된 disposition

| TC | Action | Where | Note |
|----|--------|-------|------|
| **5.1** σ functoriality | DELETE | 07 §3.3 end | 3-pattern HOLE; case analysis 본문 유지 |
| **5.2** Tier 2 closure | DELETE | 07 §4 | 3-pattern HOLE; 저자 본인 meta-OP admit; Def 4.1/4.2 본문 유지 |
| **1.5** Single-photon detectability | DELETE | 03 §9 | Tautological; Baylor empirical fact 으로 격하 |
| **3.2** Latency → two time axes | DELETE | 05 §5.2 | Pure rename of latency difference; bit cost estimate 분리 |
| **0.1b** Factorization formula | DELETE | 02 §8 | Definition restatement; §2.5 본문 유지 |
| **1.3** Causal pipeline | WEAKEN | 01 §5 | Qualifiers (Q1) no-feedback + (Q2) causal-Gabor 명시 |
| **1.4** Log compression | WEAKEN | 03 §9 | Qualifiers (Q1) adaptive sliding + (Q2) log-normal natural light + (Q3) Pavliotis-Stuart ergodicity |
| **2.3** DoG Bayesian MAP | WEAKEN | 04 §4.7 end | Qualifiers (Q1) Gaussian field + (Q2) 1/f² + (Q3) Gaussian noise; sparse coding 한계 명시 |
| **3.3** Compression bound | WEAKEN | 05 §7.3 | Qualifiers (Q1) bandlimited patch + (Q2) finite L_corr^eff + (Q3) sparse edges; 126:1 anatomical fact 분리 |
| **0.1a** Stats determined by Λ | SPLIT-RETAIN | 02 §8 | TC-SP-0.1 의 첫 절 보존 (HOLDS); 둘째 절 (factorization) 만 DELETE |

### 11.2 Post-cleanup TC-SP 통계

| Status | Count | Codes |
|--------|-------|-------|
| **CONFIRMED** (RETAINED, 4/4 HOLDS in Pass 3) | 6 | 0.2, 1.2, 2.1, 2.4, 2.5, 4.1 |
| **WEAKENED** (RETAINED with qualifiers) | 4 | 1.3, 1.4, 2.3, 3.3 |
| **SPLIT** (retained partial) | 1 | 0.1a |
| **UNCLEAR** (Pass 4 target) | 5 | 1.1, 2.2, 3.1, 4.2, 4.3 |
| **PARTIAL** (Pass 4 will fully verify) | 1 | 2.6 |
| **DELETED** | 5 | 0.1b, 1.5, 3.2, 5.1, 5.2 |

Active TC-SP after Pass 3 집행: **17** (= CONFIRMED 6 + WEAKENED 4 + SPLIT 1 + UNCLEAR 5 + PARTIAL 1). Down from 21.

### 11.3 Pass 4 진행 중

Pattern #6 (divergent regularization), #46 (boundary condition), #51 (independence assumption) 3개 specialist Opus critic 병렬 실행 중. 17 active TC 에 대한 추가 verdicts 대기. 새 HOLE 2+ pattern 발견 시 동일 cleanup 정책 적용 (DELETE/WEAKEN).

### 11.4 Constraint 재확인 (집행 후)

| 항목 | 상태 |
|------|------|
| `canonical/` 수정 | **0 lines** ✓ |
| `CODE/scc/` 수정 | **0 lines** ✓ |
| PAI canonical 수정 | **0 lines** ✓ |
| Stage docs 02-07 의 *retraction notice* 추가 (audit trail) | **9 sections** (5 DELETE + 4 WEAKEN; line counts: 02 expands by ~25, 03 ~30, 04 ~25, 05 ~40, 07 ~50) |
| 새 TC-SP 코드 | **+1** (0.1a — split, not new candidate; same content as 0.1's first clause) |
| 새 OP-SP 코드 | **0** (9개 후보 식별만, 등록 deferred) |
| 8 retractions 부활 | **0** ✓ |

---

*Pass 3 v1 (집행 ledger 업데이트). Pass 4 진행 중 — 완료 시 v2 로 추가 갱신.*

---

## 12. Pass 4 Results (2026-05-25, 3 추가 attack patterns)

### 12.1 Pass 4 verdict matrix (17 active TCs × 3 patterns)

| TC-SP | Status pre-P4 | #6 Divergent | #46 Boundary | #51 Independence | Cumulative HOLE (P3+P4) | **Pass 4 Decision** |
|-------|---------------|--------------|--------------|------------------|------------------------|---------------------|
| 0.1a | CONFIRMED (post-split) | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| 0.2 | CONFIRMED | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| 1.1 | UNCLEAR | HOLDS | HOLDS | HOLE | 1+1 = **2** | **DELETED** |
| 1.2 | CONFIRMED | HOLDS | UNCLEAR | HOLDS | 0 | **RETAINED** |
| 1.3 | WEAKENED | HOLDS | HOLE | HOLE | 2+2 = **4** | **DELETED** (escalated) |
| 1.4 | WEAKENED | HOLDS | HOLE | HOLE | 2+2 = **4** | **DELETED** (escalated) |
| 2.1 | CONFIRMED | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| 2.2 | UNCLEAR | HOLDS | HOLE | HOLE | 1+2 = **3** | **DELETED** |
| 2.3 | WEAKENED | HOLDS | HOLE | HOLE | 2+2 = **4** | **DELETED** (escalated) |
| 2.4 | CONFIRMED | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| 2.5 | CONFIRMED | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| 2.6 | PARTIAL | HOLDS | HOLDS | HOLDS-caveat | 0 | **RETAINED** (now fully verified) |
| 3.1 | UNCLEAR | HOLDS | HOLDS | HOLE | 1+1 = **2** | **DELETED** |
| 3.3 | WEAKENED | HOLDS-cond | HOLE | HOLE | 2+2 = **4** | **DELETED** (escalated) |
| 4.1 | CONFIRMED | HOLDS | HOLDS | HOLDS | 0 | **RETAINED** |
| 4.2 | UNCLEAR | HOLDS | UNCLEAR | HOLE | 1+1 = **2** | **DELETED** |
| 4.3 | UNCLEAR | HOLDS | HOLE | HOLE | 1+2 = **3** | **DELETED** |

### 12.2 Pass 4 통계

- **RETAINED**: **8** (0.1a, 0.2, 1.2, 2.1, 2.4, 2.5, 2.6, 4.1) — 7 attack patterns 통과 (Pass 3 의 #4 #18 #40 #5 + Pass 4 의 #6 #46 #51)
- **DELETED (Pass 4)**: 9 (1.1, 1.3, 1.4, 2.2, 2.3, 3.1, 3.3, 4.2, 4.3)

### 12.3 Pass 4 attack-pattern 기여도

| Pattern | HOLE 발견 수 | 가장 강한 hit |
|---------|--------------|---------------|
| #6 Divergent regularization | 0 (모두 HOLDS, 일부 conditional) | (없음 — TC-SP-3.3 weakened form 의 conditional HOLDS 가 가장 fragile) |
| #46 Boundary condition | 6 | TC-SP-4.3 (additive Gaussian on bounded range) |
| #51 Independence assumption | 9 | TC-SP-3.1 (Cox conditional-independence 위반, double confirmation) |

**Key 발견**: 
- **Pattern #6 (divergent regularization)**: Pass 3 cleanup 이 발산 관련 hole 을 *모두 흡수* 함 — Pass 4 에서 0 HOLE. 가장 fragile 한 TC-SP-3.3 도 weakening 의 (Q2) finite L_corr 가 boundary 안전화.
- **Pattern #51 (independence)**: 가장 *yield 높은* attack — 9 hits. Cox process / Markov / pixel-independence 가정이 망막 회로의 *공통 약점*. 본 corpus 의 *structurally 가장 약한 dimension*.

### 12.4 Total 누적 cleanup (Pass 3 + Pass 4)

| 총합 | 카운트 |
|------|--------|
| Original TC-SP-N.M | 21 (including 2.6) |
| Pass 3 DELETED | 5 (0.1b, 1.5, 3.2, 5.1, 5.2) |
| Pass 3 WEAKENED → Pass 4 DELETED (escalated) | 4 (1.3, 1.4, 2.3, 3.3) |
| Pass 4 DELETED (newly REFUTED) | 5 (1.1, 2.2, 3.1, 4.2, 4.3) |
| **Total DELETED** | **14** |
| **RETAINED (활성)** | **8** |
| **Retraction 율** | **66.7%** |

### 12.5 8 surviving TCs (7-pattern verified)

| TC-SP | 명제 | 위치 | Strength |
|-------|------|------|----------|
| **0.1a** Stats determined by Λ | Poisson finite-dim stats = Λ 의 함수 | 02 §8 | Janossy product form |
| **0.2** Photon limit | $\Lambda \to 0$ → 1차 사건 dominate | 02 §8 | Poisson Taylor expansion |
| **1.2** DPI chain | Markov chain → MI 단조 감소 | 01 §5 | Cover-Thomas Thm 2.8.1 |
| **2.1** Riesz uniqueness | $V = V_+ - V_-$ unique decomp | 04 §3 | Aliprantis-Burkinshaw Thm 1.5 |
| **2.4** Adelson-Bergen slab | Gabor energy = velocity slab in Fourier | 04 §5 | Parseval + Fourier shift |
| **2.5** Reichardt ≡ motion energy | Quadratic equivalence (qualifier explicit) | 04 §5 | Adelson-Bergen 1985 §4 |
| **2.6** Color PCA | L-M, S-(L+M), Lum ≈ PCA principal axes | 04 §6 | Ruderman-Cronin-Chiao 1998 |
| **4.1** End-to-end bound | $C(\Phi) \leq \min_i C(\mathcal{K}_i)$ | 06 §2 | DPI corollary |

### 12.6 Pass 5 (진행 중)

사용자 directive "계속 찾아라" — Pass 5 추가 attack patterns (e.g., #11 model misspecification, #29 continuity at limits) 발사 예정. 8 surviving TCs 에 적용. 새 HOLE 발견 시 동일 cleanup 정책.

---

*Pass 3 v2 (Pass 4 결과 통합). 활성 TC = 8. Pass 5 발사 대기.*

---

## 13. Pass 5 Results (2026-05-25, 2 추가 attack patterns: #11, #29)

### 13.1 Pass 5 verdict matrix (8 surviving TCs)

| TC-SP | Status pre-P5 | #11 Model misspec | #29 Continuity limits | Cumulative HOLE (P3+P4+P5) | **Pass 5 Decision** |
|-------|---------------|-------------------|-----------------------|---------------------------|---------------------|
| 0.1a | RETAINED | HOLDS | HOLDS | 0 | **RETAINED (sole survivor)** |
| 0.2 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** (user ruthless directive) |
| 1.2 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** |
| 2.1 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** |
| 2.4 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** |
| 2.5 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** |
| 2.6 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** |
| 4.1 | RETAINED | HOLE | HOLDS | 1 (#11) | **DELETED** |

### 13.2 Pass 5 통계

- **#11 (Model misspecification)**: 1 HOLDS / 7 HOLE FOUND — *devastating*. Verifier 결론: "Mathematical proofs handle different objects than biological claims."
- **#29 (Continuity at limits)**: 8 HOLDS / 0 HOLE FOUND. Verifier confirms: "Pass 4 cohort 가 limit-interchange attack 에 *genuinely robust*."

### 13.3 Pass 5 deletion 근거 (ruthless directive)

Math-olympiad standard 2+ HOLE rule 아닌, 사용자 directive *"가차없이 박탈"* 적용:
- Pattern #11 의 HOLE 들이 *systematic* (8 중 7) 이고 *factually grounded* (예: DSGC mechanism, Shannon capacity premise 등 *empirically false* claims)
- 단일 pattern 이나 *substantive*; verifier 본인이 "ruthless directive 하 단지 0.1a 만 survives" 명시 권고

7 TCs DELETED with detailed retraction notices:
- TC-SP-0.2 (02): photon arrival ≠ rod detection 의 *동일 conflation* (TC-SP-1.5 와 같은 issue)
- TC-SP-1.2 (01): generic Cover-Thomas DPI 는 정리, *retinal Markov 적용* 은 false
- TC-SP-2.1 (04): Riesz lattice generic 정리, *retinal ON/OFF* 가 overlapping + tonic + parallel cascades — pointwise 분해 아님
- TC-SP-2.4 (04): Adelson-Bergen 은 cortical V1 모델, *retinal DSGC* 는 starburst amacrine asymmetric inhibition
- TC-SP-2.5 (04): Reichardt 는 insect lobula 모델 — *two non-applicable models* 의 equivalence 증명
- TC-SP-2.6 (04): PCA alignment ≠ causal optimization (phylogenetic accident alternative)
- TC-SP-4.1 (06): Shannon capacity ≠ retinal task-relevant Fisher information

### 13.4 최종 누적 cleanup (Pass 3 + 4 + 5)

| 단계 | DELETED | Cumulative DELETED | RETAINED |
|------|---------|---------------------|----------|
| Pass 3 (Phase 2) | 5 (0.1b, 1.5, 3.2, 5.1, 5.2) | 5 | 16 |
| Pass 3 (Phase 2 WEAKEN) | (4 — 1.3, 1.4, 2.3, 3.3 — *later escalated*) | 5 | 16 (12 strict + 4 weakened) |
| Pass 4 (escalation of weakened) | +4 (1.3, 1.4, 2.3, 3.3) | 9 | 12 |
| Pass 4 (newly REFUTED) | +5 (1.1, 2.2, 3.1, 4.2, 4.3) | 14 | 8 (Pass 4 final) |
| Pass 5 (model misspec) | +7 (0.2, 1.2, 2.1, 2.4, 2.5, 2.6, 4.1) | **21 deleted out of 22; 1 SPLIT-retained (0.1a)** | **1** (TC-SP-0.1a) |

### 13.5 Final surviving TC

**TC-SP-0.1a (Statistics determined by Λ)** — sole survivor of 9 attack patterns (P3 4 + P4 3 + P5 2).

- Statement: Stage 0 의 Poisson 점과정의 모든 finite-dimensional 통계는 강도 측도 Λ 만으로 결정됨.
- Proof basis: Janossy product density `j_n^W = e^{-Λ(W)} ∏λ(x_i)` (Last-Penrose §6); Tonelli on compact windows.
- Why survives: *Mathematical fact* 만 주장 (Λ 결정성), *biological applicability* claim 없음. Coherence concerns 는 OP-SP-001 로 isolated (Mandel-Wolf M~10¹¹ modes argument 가 detection regime 에서 valid).

### 13.6 Honest assessment — 본 corpus 의 진단

전체 21 TC 중 1 survival rate **4.8%**. 이 *attrition* 의 의미:

1. **Mathematical content 자체는 대부분 sound** — Pass 4 #6 (divergent) + Pass 5 #29 (continuity) 모두 거의 HOLDS. 수학적 derivation 은 잘 됨.

2. **Biological applicability 가 systematic 약점** — Pass 5 #11 (model misspecification) 이 8 중 7 hits. 본 corpus 의 TC 들이 *abstract math + retinal motivation* 의 hybrid 인데, *biological claim* 의 verification 이 부재.

3. **Cox process / Markov / iid 가정의 systematic 위반** — Pass 4 #51 가 17 중 9 hits. 망막의 *correlation, feedback, adaptation* 이 standard probability theory 의 standard assumption 들을 위반.

4. **본 corpus 가 *biological theorems* 가 아닌 *mathematical observations with retinal motivation*** — 이 distinction 이 본 directory 의 register 가 *DEFINITION-DRAFT + THEOREM-CANDIDATE* 인 이유 (실제 정리 promotion 시도 안 함).

### 13.7 Constraint 재확인 (Pass 5 cleanup 후)

| 항목 | 상태 |
|------|------|
| `canonical/` 수정 | **0 lines** ✓ |
| `CODE/scc/` 수정 | **0 lines** ✓ |
| PAI canonical 수정 | **0 lines** ✓ |
| Stage docs 02-07 의 *retraction notice* (audit trail) | **21 sections** (모든 retracted TC 가 historical record 로 보존) |
| 새 TC-SP 코드 | **+1** (0.1a — split, not new candidate) |
| 새 OP-SP 코드 | **0** |
| 8 SCC retractions 부활 | **0** ✓ |

---

## 14. Pipeline Stable State 선언

3-pass adversarial verification + ruthless cleanup 완료. **Stable state 도달** — 추가 verification pass 의 marginal value 가 매우 낮음 (1 TC 만 남아 있고, 그 TC 가 9 patterns 통과; 추가 attack 으로도 fall 가능성 매우 낮음).

**Final corpus**:
- 1 active TC-SP (0.1a)
- 9 attack patterns 통과
- 21 deletions with full retraction notices (audit trail preserved)
- canonical / SCC / PAI 무수정 유지

다음 단계 권고 (사용자 직접 결정):
1. Corpus 자체의 *registerc 격하* — DEFINITION-DRAFT 가 아닌 *retinal lecture notes with mathematical references* 로 framing 변경
2. Task-relevant Fisher information (Geisler 2008) framework 채택 — Shannon capacity 의 대안
3. OP-SP-006 (SCC $u_t$ ↔ stage) 의 advancement — *어차피* SCC 와의 다리가 본 corpus 의 *유일한 unique 가치* (생존 0.1a 만으로는 부족)
4. 전체 sensing_pipeline 디렉토리의 *archival* — *learning artifact* 로 보존, 새 framework 로 fresh start

---

*Pass 3 v3 (Pass 5 결과 통합 + 최종 stable state 선언). Survivor: 1 TC. 21 deletions. Audit trail 완전 보존. Constraint 100% 준수.*
