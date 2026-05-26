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

## 1. 문서 목록 (22개)

| # | 파일 | 역할 | 상태 |
|---|------|------|------|
| 00 | [[00_INDEX]] | 본 파일 — 네비게이션, 색인 | Active |
| 01 | [[01_framework_master]] | 마스터 아키텍처 + 수학 도구 포괄 survey | Active (Pass 3-9 cuts logged) |
| 02 | [[02_stage0_photon_point_process]] | Stage 0 — 광자 도래 점과정 | Active (Pass 3, 5, 8 cuts logged) |
| 03 | [[03_stage1_photoreceptor_sde]] | Stage 1 — 광수용기 SDE | Active (Pass 3, 7 cuts logged) |
| 04 | [[04_stage2_inner_retinal_algebra]] | Stage 2 — 내부 망막 대수 | Active (Pass 3-9 cuts logged) |
| 05 | [[05_stage3_ganglion_spike_encoding]] | Stage 3 — 신경절세포 스파이크 부호화 | Active (Pass 3-9 cuts logged) |
| 06 | [[06_endtoend_information_bound]] | Cross-cutting — 정보론적 회계 | Active (Pass 3-9 cuts logged) |
| 07 | [[07_omega_sigma_lift]] | (Ω, σ) Tier 2 프레임워크로의 lift | Active (Pass 3 cuts logged) |
| 08 | [[08_open_problems_sp]] | OP-SP 통합 등록부 | Active |
| 09 | [[09_verification_pass3]] | Pass 3+4+5 verification ledger | Final |
| 10 | [[10_reconstruction_pass6]] | Pass 6 reconstruction (R-1..R-10) | Final (all R-* cut in Pass 7-9 except R-5 UNCLEAR) |
| 11 | [[11_minimal_core]] | Pass 10 minimal core (5+5+5) | Final |
| 12 | [[12_perception_cone_field_equation]] | Pass 11 perception cone + Einstein-form field equation | Final (20 iter) |
| 13 | [[13_p1_p2_verification]] | Pass 12 Phase A — Postulate verification (Tasks 1-5) | Final |
| 14 | [[14_field_equation_verification]] | Pass 12 Phase B — Field equation verification (Tasks 6-10) | Final |
| 15 | [[15_operational_test_protocols]] | Pass 12 Phase C — Operational test protocols (Tasks 11-15) | Final |
| 16 | [[16_op_pfe_advancement]] | Pass 12 Phase D — OP-PFE advancement (Tasks 16-20) | Final |
| 17 | [[17_pass12_adversarial_extensions]] | Pass 12 Phase E — Extended adversarial gauntlet (Tasks 21-23) | Final |
| 18 | [[18_stress_energy_alternatives]] | Pass 12 Phase F-1 — Stress-energy alternatives (Task 24) | Final |
| 19 | [[19_delta_interp_synthesis]] | Pass 12 Phase F-2 — Δ_interp synthesis (Task 25) | Final |
| 20 | [[20_three_framework_synthesis]] | Pass 12 Phase F-3 — Three-framework synthesis (Task 26) | Final |
| 21 | [[21_pass12_final_report]] | Pass 12 Phase G — Final report (Task 27) | Final |

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

### 2.2 [2026-05-25 EVENING] Pass 6 Reconstruction — 10 New TC-SP-R Candidates

Pass 3-5 collapse 이후 *pattern-aware design* 으로 reconstruction: **10 new TC-SP-R-N candidates** (5 MATH-FACT + 5 CONDITIONAL-OBSERVATION). Each TC addresses ≥3 of 9 known attack patterns explicitly in its design.

**MATH-FACT TCs** (5 — pure math, retinal motivation only):

| 코드 | 명제 | Predicted survival |
|------|------|----|
| **TC-SP-R-1** | Janossy product density (Poisson factorization) | HIGH |
| **TC-SP-R-2** | Riesz lattice disjoint decomposition (Aliprantis-Burkinshaw) | HIGH |
| **TC-SP-R-3** | Spacetime Fourier velocity-slab identity (Adelson-Bergen V1, NOT retinal DSGC) | HIGH |
| **TC-SP-R-4** | DPI for Markov kernel cascades (Cover-Thomas) | HIGH |
| **TC-SP-R-5** | Composition of stochastic kernels (Kallenberg) | HIGH |

**CONDITIONAL-OBSERVATION TCs** (5 — biological claim with explicit Q-conditions):

| 코드 | 명제 (조건부) | Predicted survival |
|------|--------------|----|
| **TC-SP-R-6** | Naka-Rushton Weber-Fechner within bounded operating range (Q1-Q5) | MOD-HIGH |
| **TC-SP-R-7** | DoG ≈ Laplacian on C² interior with margin (Q1-Q3) | MOD-HIGH |
| **TC-SP-R-8** | Cox process rate sufficiency in high-rate bandlimited Q5-conditioned regime | MODERATE |
| **TC-SP-R-9** | Shannon min-capacity bound (math-only; biological non-applicability explicit via Geisler 2008) | HIGH |
| **TC-SP-R-10** | Sparse coding L1-regularized MAP for V1 simple cells (Olshausen-Field 1996; NOT retinal bipolar) | MODERATE |

**Aggregate**: HIGH 6, MOD-HIGH 2, MODERATE 2. Estimated Pass 7 survival ≥70% (vs Pass 5 post-attack rate 4.5%).

자세한 내용: [[10_reconstruction_pass6|10_reconstruction_pass6.md]].

**Active TC count update**: 1 (TC-SP-0.1a survivor) + 10 (TC-SP-R-N reconstruction) = **11 active candidates** (post-Pass-6).

Pass 7 verification (별도 plan) 미실시 — predicted survival 만 등록.

---

### 2.3 [2026-05-25 LATE EVENING] Pass 7 Verification — 3 new attack patterns on 10 NTCs

User directive: "더 깎아보자 정밀하게". 3 추가 attack patterns 적용:

- **#22 Q-condition compounding** (conjunction empty support in real data)
- **#3 Assumption-by-citation** (rhetorical authority vs verified hypothesis)  
- **#50 Typicality vs guarantee** (approximate ≠ uniform bound)

**Pass 7 결과**:
- **RETAINED (0 HOLE)**: 5 (R-1, R-2, R-4, R-5, R-9 — 모두 MATH-FACT)
- **DELETED (≥2 HOLE)**: 2 (R-7 with 3 patterns, R-8 with 2 patterns)
- **UNCLEAR (1 HOLE)**: 3 (R-3, R-6, R-10 — pending Pass 8)

**최종 active TC count after Pass 7**: **9** = TC-SP-0.1a + 5 RETAINED + 3 UNCLEAR

**핵심 발견**: COND-OBS TCs 가 *systematically vulnerable* — Q-condition multiplicative compounding (#22) 이 가장 lethal. R-7 의 3-pattern failure 가 *mathematical citation 자체* 의 hypothesis-check 필요성 드러냄. Pass 6 self-prediction 7/10 correct (3 over-optimistic).

자세한 내용: [[10_reconstruction_pass6|10_reconstruction_pass6.md]] §11.

---

### 2.4 [2026-05-25 DEEPEST CUT] Pass 8 Verification — 3 meta-mathematical patterns

User directive: "더 깎아보자 정밀하게". 3 추가 attack patterns:
- **#7 implicit regularity smuggle** (silent smoothness/integrability assumptions)
- **#37 pointwise vs uniform conflation** (sup-interchange-without-uniform-convergence)
- **#28 subset support** (actual proof scope < stated)

**Pass 8 결과**:
- **RETAINED (truly ironclad — 0 HOLE across 6 P7+P8 patterns)**: **2** (R-4 DPI, R-5 Composition)
- **UNCLEAR (1 minor HOLE; fixable)**: 2 (R-1 Janossy, R-2 Riesz)
- **DELETED (Pass 8)**: 5 (TC-SP-0.1a, R-3, R-6, R-9, R-10)

**중대 발견**:
- **TC-SP-0.1a (original 9-pattern survivor) falls** — Radon-Nikodym a.c. + simple-process 가정이 *명사구 안에 hidden*; statement 외 hypothesis
- **R-3, R-9 두 MATH-FACT failure** — *signal-model regularity* (R-3 PSD existence) + *sup-interchange compatibility* (R-9) 가 silent
- **R-3, R-10 4-pattern strongest refute**
- **Cumulative DELETED: 28 of 32 ever-created TCs (87.5% attrition)**

**최종 active TC count after Pass 8**: **4** (R-4 DPI, R-5 Composition — RETAINED; R-1 Janossy, R-2 Riesz — UNCLEAR-minor).

**Meta-lesson**: 본 corpus 의 *truly-ironclad core* 는 *signal-class hypothesis 0* 의 *generic existence/closure on Polish-Borel* claims (R-4, R-5). 본 corpus 의 *진정한 value* 는 TCs 가 아니라 *11,000+ 라인의 mathematical exploration record* 그 자체.

자세한 내용: [[10_reconstruction_pass6|10_reconstruction_pass6.md]] §12.

**Stable state 선언**: 추가 attack 의 marginal value 극히 낮음 — R-4/R-5 는 textbook generic results; UNCLEAR R-1/R-2 는 fix 가능. PAI bridge pivot 권고.

---

### 2.5 [2026-05-25 ABSOLUTE FINAL] Pass 9 — Corpus Collapse

사용자 directive (third "더 깎아보자 정밀하게"): 3 추가 patterns 적용:
- **#41 non-constructive set-theoretic dependency**
- **#15 vacuity at biological boundary**
- **#52 information-theoretic vs operational mismatch**

**Pass 9 결과**:
- **RETAINED**: **0** ⚠️ — R-4 (last MATH-FACT ironclad) falls
- **UNCLEAR**: **1** (R-5 sub-probability vs probability)
- **DELETED (Pass 9)**: 3 (R-1, R-2, R-4)

**Pattern #15 hits ALL 4 active TCs**: corpus 의 *every TC's universal hypothesis class is empty in actual retina* (Poisson 가정 vs super-Poisson 자연 광; Banach lattice 가정 vs bounded cone 현실; Markov 가정 vs feedback+adaptation 현실; probability kernel 가정 vs sub-probability+intensity 현실).

**최종 active TC count after Pass 9**: **1** (R-5 UNCLEAR).

**Cumulative DELETED: 31 of 32 TCs (96.9% attrition)**.

**Meta-meta-lesson**: 본 corpus 의 *진정한 contribution* 은 *negative result* — textbook mathematical structures 의 retinal applicability 가 systematically vacuous. 다음 framework 의 출발점: super-Poisson + bounded cone + non-Markov + sub-probability/intensity 가 *실제 retinal 구조*.

자세한 내용: [[10_reconstruction_pass6|10_reconstruction_pass6.md]] §13.

**Absolute stable state 도달** — 추가 verification 의 marginal value 0. PAI bridge pivot 또는 framework 전면 reformulation 권고.

---

### 2.6 [2026-05-25 PASS 10 MINIMAL CORE] Reclassification to Exploration Record + Minimal Core

User directive: "10번의 iteration 으로 minimal-structure adversarial refinement". Executed in main context (ralph-loop slash-command 이 shell parsing limitation 으로 실패).

**산출**: [[11_minimal_core|11_minimal_core.md]] (~700 LOC) — single authoritative document containing:
- **5 Primitives** (P1-P5, operationally defined): photon arrival event, bounded intensity response, forward-only kernel transformation, tolerance σ, channel index
- **5 Negative Constraints** (C1-C5): NOT Poisson, NOT Markov, NOT probability-kernel, NOT unbounded, NOT biological-theorem
- **5 Open Problems** (OP-MIN-1..5): operational perceptual field, super-Poisson Mandel Q measurement, sub-probability kernel composition, non-Markov DPI, SCC u_t mapping
- 11 prior docs (00-10) reclassified as **EXPLORATION RECORD** (research process documentation)

**Reclassification verdict**:
- ~11,000 LOC = EXPLORATION-RECORD (mathematical derivations + audit trail + verification methodology)
- 1 active CONDITIONAL-OBS (TC-SP-R-5 with OP-MIN-3 salvage)
- 5 OPERATIONAL-HYPOTHESES / OPEN-PROBLEMS (OP-MIN-1..5)
- 0 BIOLOGICAL-CLAIM (per constraint C5)

**No-expansion compliance**: NO new framework name; NO new TC; ONLY compression + reclassification; canonical/SCC/PAI/8-retractions untouched.

**Final standard met**: smaller (32→6 active claims), sharper (operational definitions), more falsifiable (each OP-MIN has explicit failure mode).

자세한 내용 + 5 Next Cut Recommendations: [[11_minimal_core|11_minimal_core.md]].

**MINIMAL ADVERSARIAL REFINEMENT COMPLETE**.

---

### 2.7 [2026-05-26 PASS 11 PERCEPTION CONE + FIELD EQUATION] 20-iteration framework construction

User directive (third major strategic turn today): "Minkowski lightcone 도출처럼 인식 관계를 찾아보자" + "Einstein 장방정식 형식으로" + "20번 iteration 으로 derive + verify".

**산출**: [[12_perception_cone_field_equation|12_perception_cone_field_equation.md]] (~700 LOC) — single document with 20 iterations visible, each: derive + adversarial check + state-after.

**Core construction**:
- **2 postulates**: P1 perceptual relativity (within observer class) + P2 limiting rate $c_p^{(s)}$ per stage
- **σ relation 이 derived** (Tier 2 primitive 가 아닌 P1+P2 의 결과)
- **Per-stage perception cone** $\mathcal{C}^{(s)}$ — operationally measurable $c_p^{(s)} = \ell_s / \tau_s$
- **Local Lorentz metric** $g_{\mu\nu}^{(s)} = \text{diag}(-c_p^{(s)2}, 1, 1)$
- **Einstein-style field equation**: $R_{\mu\nu}^{(s)} - \frac{1}{2} g_{\mu\nu}^{(s)} R^{(s)} = \kappa^{(s)} T_{\mu\nu}^{\text{perception}}[u, g^{(s)}]$
- **Stress-energy from SCC E[u]** (variational derivative; SCC canonical 무수정)
- **6 approximation regimes** (Newtonian / vacuum / linearized / cosmological / Schwarzschild-like / geodesic)
- **4 operational tests** (falsifiable): $c_p$ stability, cone ↔ binding, curvature ↔ binding variation, multi-stage intersection ↔ unification
- **5 open problems** (OP-PFE-1..5): multi-metric coupling, $\kappa$ determination, vacuum existence/uniqueness, alternative $\Delta_{\text{interp}}$ candidates, cortical cone

**Adversarial gauntlet results** (6 patterns applied within iterations 11-15):
- #11 misspec: pass *as conditional observation*
- #15 vacuity: pass via *operational framing of deviations*
- #51 independence: partial pass (OP-PFE-1 needed for multi-stage)
- #28 subset: pass with *narrow effective domain* (smooth + short window + intermediate stages)
- #7+#37+#50: conditional pass on *smooth regime*
- #18 tautology: pass (σ now *derived*, not asserted)

**Constraint compliance**:
- SCC canonical (CV-1.20): **0 edits**
- PAI canonical: **0 edits**
- 8 SCC retractions: **0 revivals**
- Prior 31 deletions: preserved as audit trail
- No new framework name registered as canonical (PFE is descriptive label)
- **All SCC + PAI substrates preserved + naturally used as components**

**Connections** (자연 합성):
- SCC's $E[u]$ → stress-energy $T_{\mu\nu}^{\text{perception}}$
- PAI's $\Delta_{\text{interp}}$ → candidate operational form via geodesic distance
- 31 prior deletions → reframed as *non-cone-respecting attempts*

**Load-bearing open question**: SCC E[u] 가 정말 correct stress-energy source 인지 *empirical 검증* 필요. 대안 (Friston F, Fisher info, sparse coding loss) 모두 *다른 PFE* 가능.

**Honest meta-assessment**: framework 가 *structurally well-defined* + *operationally testable* + *constraint-compliant* 이나 *truth* 는 4 tests 의 empirical validation 에 의존 (아직 미시행). *Measurement scaffold* register — *theorem* 아님.

자세한 내용: [[12_perception_cone_field_equation|12_perception_cone_field_equation.md]] §1–§20 + meta-reflection §21.

---

### 2.8 [2026-05-26 PASS 12 CONTINUOUS VERIFICATION PROGRAM] 27-task adversarial audit of Pass 11 framework

User directive: "태스크를 20개 이상으로 나눠서 자세하게 만들어줘서 계속 검증해줘". Pass 12 = 27 verification tasks across 7 phases (A: postulates, B: field equation, C: protocols, D: OP advancement, E: extended adversarial gauntlet, F: synthesis, G: consolidation).

**산출**: 9 docs ([[13_p1_p2_verification|13_]] through [[21_pass12_final_report|21_]]) — each phase = single doc; each task = section. ~6,000 LOC total.

**Per-task verdict count**:
- PASS: 18 / 27 (67%)
- WEAKEN: 8 / 27 (30%)
- FAIL: 1 / 27 (3.7%, Task 3 σ-derivation rigor)
- OPEN: 0
- Framework-collapse threshold (>50% FAIL): **NOT triggered**

**Pass 11 framework state — substantive weakening but SURVIVES**:
- Postulate count: not 2, actually 1 commitment + 4 implicit hypotheses (Task 4) → 6 commitments
- σ derivation: not derived, *constructed* under P1+P2+I1-I4 (Task 3 FAIL)
- σ at threshold: not binary, *probabilistic* with fuzzy edge ~15-25% (Task 1)
- Stage table: 3/6 PASS, 2/6 FAIL (>2× error), 1/6 AMBIGUOUS (Task 2)
- Vacuum: locally flat + conical defects only — Schwarzschild-like claim *wrong* in 1+2D (Task 8)
- Linear regime: matches DoG conditionally, fails motion-energy without multi-stage (Task 9)
- Geodesics: motion ✓, apparent ✓, pursuit ✓, attentional capture ✓ (novel), saccades ✗ (Task 10)
- Symmetry: Newton-Cartan-like (NOT Lorentz-invariant, NOT time-reparametrization-invariant) (Task 21)
- Cauchy problem: well-posed only in quasi-static equilibrium (PFE-SCC dynamical coupling inconsistent) (Task 22)
- Conservation: spatial momentum-like ✓, energy ✗ (dissipative SCC) (Task 23)
- Stress-energy: SCC E[u] is 1 of 4 plausible candidates; noise-scaling experiment discriminates (Task 24)

**OP catalog growth**: 5 original (OP-PFE-1..5) + 14 added (OP-PFE-6..19) = **19 OPs**. Closure paths identified per OP. 0 OPs closed in Pass 12.

**Tier 1 Pass 13 priorities** (zero new-experiment cost):
- OP-PFE-11: Execute Test 1 on Chichilnisky CRCNS data (validates/refutes core P2 claim)
- OP-PFE-6: Re-extract stage table under consistent convention ($\tau$ = STA peak-to-zero, $\ell$ = STA Gaussian 1σ)
- OP-PFE-7: Reformulate P1 via reachability R to remove Task 3 circularity

**Three-framework synthesis (Task 26)**:
- SCC is fully upstream (provides u, E, transport.py infrastructure)
- PAI is intermediate (provides observer-class taxonomy; needs substrate decision for $\Delta_{\text{interp}}$ commitment)
- PFE is downstream coupling layer (applies SCC via stress-energy; operationalizes PAI via Wasserstein)
- 4 natural integration points; 5 unresolved gaps; 3 discipline-violation risks flagged

**$\Delta_{\text{interp}}$ recommendation (Task 25)**: Wasserstein $W_2$ uniquely best against 3 criteria (PAI consistency + operational + PFE-geometric); SCC `transport.py` provides computation. PAI substrate commitment is upstream gating dependency.

**Constraint compliance** (100% maintained):
- SCC canonical (CV-1.13): **0 edits**
- PAI canonical: **0 edits**
- 8 SCC retractions: **0 revivals**
- sensing_pipeline/01-12 body content: **0 edits** (all verification outputs in 13-21)
- CODE/scc/: **0 edits**

**Framework register update**: from Pass 11's "structurally well-defined + operationally testable + constraint-compliant measurement scaffold" to Pass 12's "**...in the quasi-static equilibrium regime, with Newton-Cartan-like (not fully relativistic) symmetry, with empirically uncalibrated coupling, awaiting Test 1 execution as Tier-1 priority**".

자세한 내용: [[21_pass12_final_report|21_pass12_final_report.md]] (executive summary + complete task catalog + 19 OPs + Tier 1-5 prioritization).

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
