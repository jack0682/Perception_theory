---
type: develop/phase2
task: D5 (P5 — Stage 0 sensor T 9-조건 canonical entry path)
date: 2026-05-19
session: W8-Day2
target_canonical_version: CV-1.18 (prep)
target_consumers: V1 (Phase 3 verification), V2 (Phase 3 canonical xref), Phase 4 _SUMMARY_v0.2.md
direct_input: /tmp/scc_proofs_v02/E3_hmorse_stage0_oms.md §B
auxiliary_input:
  - THEORY/2_substrate/canonical/auxiliary_structures_master.md §4.5 (L303-365), §4.9.9 (L748-764)
  - THEORY/2_substrate/foundations/manifold/SCC_unified_derivation_v0.1.md §2 (L214-510)
  - THEORY/2_substrate/canonical/canonical.md Appendix OMS §A-§M (L2404-2663)
self_cat: A axiomatic (T axiom package, A on P)
canonical_edits: 0 (draft only)
status: COMPLETE
---

# P5 — Stage 0 Sensor $T$ : 9-Conditions Canonical Entry Path

**목적**: Stage 0 sensor transformation $T : \mathcal{I} \to \tilde{\mathcal{I}}$ 의 9 downstream 조건 (T-cond-1 ~ T-cond-9) 을 *수학적 formal form* 으로 정밀화하고, canonical Appendix OMS §N 신설을 위한 *entry draft* 를 작성한다. *Cat A axiomatic* (9×A: T 위에 부과되는 axiom — A on P).

**Phase 1 직접 입력**: `/tmp/scc_proofs_v02/E3_hmorse_stage0_oms.md §B` (P5 D5 Opus 입력). 본 § 는 §B 의 9-조건 enumeration + 6-부 composition + canonical entry path 권고를 *수학적 formal form 으로 격상*하여 canonical 등록 가능 수준의 draft 로 만든다.

---

## §0 Pre-work xref + frontmatter

### §0.1 직접 입력 — E3 §B 요약

**E3 §B.1 (9-조건 enumeration)**: AUX-1.5 §4.5 (L339-351) 의 표를 그대로 T-cond-1 ~ T-cond-9 로 라벨링. *Cat 분류*: 9×A — 각 조건은 T (관찰자-개인 P) 위에 부과되는 axiom (A on P) — `auxiliary_structures_master.md §4.9.9` L748-764 확인.

**E3 §B.2 (6-부 Composition)**: SCC_unified_derivation_v0.1 §2.1 (L228-249) 의 $T = T_{\mathrm{temp}} \circ T_{\mathrm{CSF}} \circ T_{\mathrm{gain}} \circ T_{\mathrm{LMS}} \circ T_{\mathrm{sample}} \circ T_{\mathrm{PSF}}$ 가 *operational starting point*. 현재 Cat C SKETCH.

**E3 §B.5 (Canonical entry path)**: 두 경로 중 **경로 α (OMS-Appendix §N 추가)** 권장 — canonical 최소 변경. §N heading: "Stage 0 $T$ Axiomatic Package (AUX-1.5 §4.5 canonical promotion)".

### §0.2 CoC anchors (Chain of Citations)

| Anchor | Path | 사용 위치 |
|---|---|---|
| AUX-1.5 §4.5 | `auxiliary_structures_master.md` L303-365 | 9-조건 seed table |
| AUX-1.5 §4.9.9 | `auxiliary_structures_master.md` L748-764 | Cat 분류 (9×A) |
| SCC unified §2.1 | `SCC_unified_derivation_v0.1.md` L228-249 | 6-부 composition |
| SCC unified §2.2-§2.7 | L253-468 | 각 sub-$T$ 의 explicit form |
| E3 §B | `/tmp/scc_proofs_v02/E3_hmorse_stage0_oms.md` L176-298 | D5 input (본 § 의 직접 출발) |
| canonical Appendix OMS §A | `canonical.md` L2404-2420 | 삽입 위치 reference |
| Weber-Fechner | Weber 1834, Fechner 1860 | T-cond-2, T-cond-5 anchor |
| DKL (1984) | Derrington-Krauskopf-Lennie 1984 | T-cond-4 group structure |
| Pelli-Robson CSF | Pelli-Robson 1988 | T-cond-3, T-cond-5 |
| Watson (1986) | Temporal CSF | T-cond-6 |
| Lions-Sznitman 1984 | reflected SDE well-posedness | T-cond-1 continuity → Stage 5 |
| LeCun et al. 1989 | "Efficient BackProp" | (보조) saturation analytics |

### §0.3 Non-modification commit

본 D5 출력은 **canonical 0 edits**. canonical.md / theorem_status.md / CHANGELOG.md *수정하지 않는다*. Canonical entry 는 §4 의 *draft* 형식으로만 제공; 실제 등록은 Phase 4 의 별도 commit turn 에서 사용자 승인 후.

---

## §1 Statement — Cat A Axiomatic Entry Target

### §1.1 Stage 0 sensor $T$ 의 SCC 파이프라인 내 위치

`canonical.md §3` 는 primitive $u_t : X_t \to [0,1]$ 를 *선언*하지만 그 *origin* 은 미정의. `AUX-1.5 §4.5` 가 이 누락을 진단하고 "Stage 0" 으로 등록을 권고. SCC 파이프라인은 다음과 같이 7-단계로 흐른다:

$$\underbrace{I_t \in \mathcal{I}}_{\text{Stage 0 입력 (외부, COB 비대상)}} \;\xrightarrow{T}\; \underbrace{\tilde{I}_t : V_{\mathrm{ret}} \times [0, T_{\mathrm{end}}] \to \mathbb{R}_{\geq 0}^3}_{\text{Stage 0 출력}} \;\xrightarrow{\pi_G}\; \underbrace{\text{Stage 1: 그래프 } G + u_t \text{ projection}}_{\text{T8, spinodal, } \Sigma_m}$$

그 다음 Stage 2 (에너지 최소화, $u_t$ 생성), Stage 3 (PersComp), Stage 4 ($\sigma_{\mathrm{standard}}$), Stage 5 (P-F-A1 reflected SDE, $T_*$), Stage 6 (T-Temporal-Identity, partial OT), Stage 7 (K-jump, $\sigma$-inheritance) 로 연결.

**핵심 관측**: $u_t$ 는 Stage 2 의 *output* (에너지 최소화 결과) 이고, Stage 0 의 $T$ 는 $u_t$ 의 *조상 신호* $\tilde{I}_t$ 를 생성. 즉 $T$ 는 *primitive 의 origin 으로의 역행 추적*. AUX-1.5 §4.5 표현:

> "$T$는 본질적으로 *관찰자가 raw에 가하는 변환*. ... §3 (primitive 선언) 과 OMS-2.0 Appendix (observer moduli) 가 만나는 *바닥*이 $T$."

### §1.2 9-조건 enumeration overview

각 downstream stage 가 *역방향으로 $T$ 에 부과하는* 조건이 9 개. AUX-1.5 §4.5 (L339-351) 표 :

| # | T-cond-X | 부과 Stage | 조건 (자연어) | 형식 카테고리 |
|---:|---|---|---|---|
| 1 | T-cond-1 | Stage 1 (T8 mass) | $T(I) \in \Sigma_m$ — simplex 보존 | A on P |
| 2 | T-cond-2 | Stage 1 (spinodal) | 적당한 매끄러움 (formation 가능성) | A on P |
| 3 | T-cond-3 | Stage 1 (homog. 존재) | $\{I : T(I) \equiv c\mathbf{1}\} \neq \emptyset$ | A on P |
| 4 | T-cond-4 | Stage 2 (T-PreObj-1G) | graph-class independence | A on P |
| 5 | T-cond-5 | Stage 3 (D-ST-3) | 위상 정보 보존 (persistence-respecting) | A on P |
| 6 | T-cond-6 | Stage 4 ($\sigma$) | $\mathrm{Aut}(G)$ 호환 | A on P |
| 7 | T-cond-7 | Stage 5 (P-F-A1) | 시간 연속 → 반사 SDE well-posed | A on P |
| 8 | T-cond-8 | Stage 5 (T-K-Select-OBS) | LM1-LM3 likelihood 호환 | A on P |
| 9 | T-cond-9 | Stage 6 (T-Temporal-Identity) | 시간 연속 + Stage 1 coupling | A on P |

**총계**: 9 axioms on $T$. 단, Cat 분류는 *T 자체* (관찰자-개인 P) 위의 axiom 임 (AUX §4.9.9 진단: 9×A = A on P).

**추가 후보**: T-cond-10 (HWF-1 isoperimetric regularity, AUX §4.9.6) + T-cond-11 (Stage 7 K-jump 연속, MOC_Q6_sigma_inherit) 는 본 D5 scope 외 — §9 (open questions) 에서 forward hook 만 둠.

### §1.3 Canonical entry form (Appendix OMS §N 신설 권장)

E3 §B.5 의 경로 α 채택: canonical.md Appendix OMS 의 §N 항목으로 신설. 권장 §N heading:

> **§N. Stage 0 $T$ Axiomatic Package (9-Conditions, AUX-1.5 §4.5 promotion)**

내부 구조 4-부:
- §N.1 Definition (Stage 0 sensor $T$ + 입력/출력 공간)
- §N.2 9-Conditions (T-cond-1 ~ T-cond-9) 의 *formal mathematical form*
- §N.3 6-Part Composition (operational instance, Cat C SKETCH 명시)
- §N.4 Anatomical + Neural parameter dependence (R-an, R-nn roots)
- §N.5 Cat A axiomatic registration + Non-Overclaim

**Cat 분류 (canonical entry 자기 분류)**: **9×A (axiomatic on P)** — T 는 관찰자-개인 P, 9 conditions 는 T 위의 axiomatic 제약. 본 entry 는 *axiomatic declaration*; mathematical proof 아님.

---

## §2 9-Conditions Explicit List (T-cond-1 ~ T-cond-9)

각 조건의 *수학적 formal form*. AUX §4.5 의 자연어 표현을 *registry-grade formal* 로 격상.

### §2.1 T-cond-1: Mass-preservation (Simplex 보존)

**Statement (formal)**: 모든 $I \in \mathcal{I}$ 에 대해, Stage 0 출력 $\tilde{I} = T(I)$ 가 Stage 1 의 그래프 투영 $\pi_G$ 를 거쳐 생성되는 초기조건 $u_t^{(0)} := \pi_G(\tilde{I})$ 가 simplex $\Sigma_m$ 에 속한다:

$$\pi_G(T(I)) \in \Sigma_m \;:=\; \Bigl\{u \in [0,1]^n : \sum_{v \in V_{\mathrm{ret}}} u(v) = m \Bigr\}$$

**Mathematical form**: $T(I)$ 의 적분 normalization 이 보장되어야 함. 6-부 composition 에서 $T_{\mathrm{LMS}}$ + $T_{\mathrm{gain}}$ 이 핵심 — log-luminance 압축 후 그래프 투영 단계에서 mass $m$ 으로 rescaling.

**Composition-level instance**:

$$\bigl\lVert T(I)\bigr \rVert_{L^1(V_{\mathrm{ret}})} \;=\; m \cdot c_{\mathrm{norm}}(I, T)$$

여기서 $c_{\mathrm{norm}}$ 은 $T_{\mathrm{gain}}$ 의 log-baseline $L_0$ + $T_{\mathrm{LMS}}$ 의 cone-ratio normalization 조합으로 결정 (SCC unified §2.5 L380, $L_0 = \pi (d_{\mathrm{pup}}^0/2)^2 L_{\mathrm{ambient}}$).

**COB rationale**: Stage 1 의 *질량 보존* (canonical T8, `canonical.md §13`) 이 $\Sigma_m$ 위에서의 에너지 최소화를 요구. $T$ 의 출력이 $\Sigma_m$ 호환 형태로 변환 가능해야 그래프 투영 후 Stage 1 진입 가능.

**Validation requirement**: 6-부 composition 에서 mass-normalization step 의 명시. SCC unified §2.5 L376-380 의 $L_0$ baseline 정의가 partial instance — Cat A 격상 시 *모든* $I \in \mathcal{I}$ 에 대한 simplex 도달성 증명 필요.

---

### §2.2 T-cond-2: Spinodal-Compatible Smoothness (적당한 매끄러움)

**Statement (formal)**: $T(I)$ 의 *spectral content* 가 Stage 1 의 spinodal regime ($q = \beta/\alpha > q_{\mathrm{crit}} := 4\lambda_2 / \lvert W''(c) \rvert$) 와 호환되는 매끄러움 등급에 속한다. 구체적으로:

$$\exists \, s \in (0, 1) : \quad T(I) \in H^s(V_{\mathrm{ret}}) \quad \text{(fractional Sobolev)}, \quad s \neq 0, \; s \neq \infty$$

즉 $T(I)$ 가:
- 너무 매끄러움 ($s \to \infty$, e.g., $C^\infty$ 균질) → 모든 모드가 균질 → formation 불발;
- 너무 거침 ($s \to 0$, e.g., white noise) → 구조가 *입력에 이미 꽂혀있음* → formation 이 trivial;
- *중간 매끄러움* ($s \in (0, 1)$) → spinodal 임계 통과 후 자발적 formation 가능.

**Mathematical form (instance)**: SCC unified §2.6 의 $T_{\mathrm{CSF}}$ 가 핵심:

$$\hat{K}_{\mathrm{CSF}}(\nu) \;=\; A_{\mathrm{CSF}} \nu^a e^{-b\nu}, \quad \text{peak} \in [3, 6]\,\mathrm{cpd}, \quad \text{cutoff} \in [30, 60]\,\mathrm{cpd}$$

이 bandpass 가 $T(I)$ 를 *spinodal-compatible Sobolev class* 로 강제. Pelli-Robson CSF (1988) anchor.

**Weber-Fechner 정밀화**: SCC unified §2.5 의 $T_{\mathrm{gain}}$ 이 log-compression $\log(\tilde{I}^{\mathrm{LMS}}/L_0)$ 을 적용. Weber-Fechner 법칙 (JND $\propto$ stimulus magnitude) 이 매끄러움 등급을 *생리적으로* 결정 — T-cond-2 의 자연어 "적당한 매끄러움"의 *정량 anchor*.

**COB rationale**: spinodal 임계 통과 가능성 = Stage 1 에서 *자발적 phase separation* 발현의 필요조건. *환경 통계* (자연영상 1/f spectrum) 가 아니라 *관찰자의 sensor smoothness* (R-nn-5 $\sigma_{\mathrm{pool}}^{V1}$) 가 spinodal 호환성을 결정.

**Validation requirement**: 6-부 composition 의 출력에 대한 Sobolev norm 측정. Cat A 격상 시 spinodal-regime 진입 확률 (R-an, R-nn root 분포 하에서) 의 정량적 lower bound.

---

### §2.3 T-cond-3: Homogeneous Input Existence

**Statement (formal)**: $T$ 의 image 가 균질 fiber 를 *포함*한다:

$$\bigl\{I \in \mathcal{I} : T(I) \equiv c \cdot \mathbf{1}, \; c \in (0, 1)\bigr\} \;\neq\; \emptyset$$

**Mathematical form**: 적당한 균질 입력 $I^{\mathrm{hom}} \in \mathcal{I}$ (예: spatially uniform field) 가 존재하여 $T(I^{\mathrm{hom}}) = c^{\mathrm{hom}} \cdot \mathbf{1}$. 이 균질 fiber 가 Stage 1 의 *unstable homogeneous starting point* 역할.

**Composition-level instance**: $I^{\mathrm{hom}}(x) \equiv I_0$ (spatially uniform). 6-부 composition 적용:
1. $T_{\mathrm{PSF}}(I^{\mathrm{hom}}) = I_0$ (convolution with normalized $K_{\mathrm{PSF}}$ 은 균질 신호 보존)
2. $T_{\mathrm{sample}}$: Poisson sampling 의 mean-field 한계에서 $\eta(v) I_0$
3. $T_{\mathrm{LMS}}$: $\mathbf{M}_{\mathrm{LMS}} \cdot (I_0, I_0, I_0)^\top$
4. $T_{\mathrm{gain}}$: $\log(I_0/L_0) \cdot G(t; \tau_{\mathrm{adapt}})$
5. $T_{\mathrm{CSF}}$: DC component 가 통과 ($K_{\mathrm{CSF}}(0) = A_{\mathrm{CSF}} \cdot 0$ 인데 한계 처리 필요)
6. $T_{\mathrm{temp}}$: bandpass 의 DC 거동

**Open issue**: CSF 의 *bandpass* 특성으로 인해 DC 가 *완전* 통과되지 않음 (peak ≈ 3-6 cpd). 따라서 *strict* 균질 fiber 는 통과되기 어렵고, *near-homogeneous* fiber 가 실질적 instance. T-cond-3 의 정확한 statement 는:

$$\bigl\lVert \,T(I^{\mathrm{hom}}) - c^{\mathrm{hom}} \mathbf{1}\,\bigr \rVert_{L^2(V_{\mathrm{ret}})} \;\leq\; \epsilon_{\mathrm{hom}}, \quad \epsilon_{\mathrm{hom}} \to 0 \text{ as bandpass } \to \text{DC-passing}$$

(weak form). Cat A 격상 시 strict vs weak form 의 명시.

**COB rationale**: Stage 1 의 *출발점* (homogeneous initial condition) 이 존재해야 spinodal-driven formation 의 *자연 발현* 가능. 만약 $T$ 가 균질 fiber 를 *전혀* 통과시키지 않으면 Stage 1 의 unstable homogeneous fixed point 가 vacuous.

**Validation requirement**: Empirical — $I^{\mathrm{hom}} =$ uniform gray field 에 대해 $T(I^{\mathrm{hom}})$ 의 spatial variance 측정.

---

### §2.4 T-cond-4: Graph-Class Independence

**Statement (formal)**: $T$ 의 output 이 Stage 2 의 *T-PreObj-1G* (canonical, `canonical.md §6`) 의 graph-class universality 와 호환된다. 구체적으로:

$$\forall \, G \in \mathcal{G}_{\mathrm{admissible}} : \quad T(I) \big\vert_{V_G} \in \mathcal{D}_G^{\mathrm{admissible}}$$

여기서 $\mathcal{G}_{\mathrm{admissible}}$ 는 SCC 의 admissible graph class (grid, hexagonal, irregular mesh, $\mathrm{Cay}(\Gamma)$ 등), $\mathcal{D}_G^{\mathrm{admissible}}$ 는 $G$ 위에서의 admissible signal class.

**Mathematical form**: $T$ 가 *graph-specific 구조에 hard-coded 되어 있지 않다*. 즉 $T$ 의 구성에서 specific graph $G_0$ 의 spectral basis 가 사용되지 않음. 6-부 composition 의 *각 sub-T* 가 graph-independent:
- $T_{\mathrm{PSF}}$ : continuous spatial convolution (graph 무관)
- $T_{\mathrm{sample}}$ : retinal mesh $V_{\mathrm{ret}}$ 결정 — 단, $V_{\mathrm{ret}}$ 의 *생성 규칙* 이 R-an roots (cone density) 에 의해 admissible class 내에 항상 위치
- $T_{\mathrm{LMS}}, T_{\mathrm{gain}}, T_{\mathrm{CSF}}, T_{\mathrm{temp}}$ : pointwise / convolutional — graph spectral basis 비의존

**COB rationale**: T-PreObj-1G (Stage 2) 는 *그래프-보편 정리* — graph-class 무관하게 Stage 2 에너지 최소화가 작동. 만약 $T$ 가 특정 $G_0$ 에 의존한다면 Stage 2 universality 위반.

**Validation requirement**: 다양한 admissible graph $G$ 에 대해 $T(I)\vert _{V_G}$ 의 일관성 (Stage 2 수렴 거동의 graph 무관성).

---

### §2.5 T-cond-5: Topology Preservation (위상 정보 보존)

**Statement (formal)**: $T$ 가 입력 $I$ 의 *위상 구조* (topology) 를 출력 $T(I)$ 에서 보존한다. 즉 PersComp (persistence complex, Stage 3 D-ST-3) 카운트가 $T$ 작용 전후로 의미를 가진다:

$$\dim H_k\bigl(\mathrm{PersComp}(I; \tau)\bigr) \;=\; \dim H_k\bigl(\mathrm{PersComp}(T(I); \tau')\bigr) \quad \forall \, k \in \{0, 1, \ldots, d\}$$

(homotopy-respecting up to a *scale renormalization* $\tau \mapsto \tau'$).

**Mathematical form**: $T$ 가 *위상 동형* (homeomorphism) 또는 *위상 동치 보존* (homotopy equivalence) 의 약한 형태를 만족. 엄밀한 형식:

$$T_*: H_k(\mathcal{I}) \to H_k(\tilde{\mathcal{I}}) \quad \text{is well-defined and rank-preserving}$$

**Composition-level analysis**:
- $T_{\mathrm{PSF}}$: blurring 이 *충분히 smooth* 하면 위상 보존 (small-scale features 만 smoothing); $\vert \sigma_{\mathrm{PSF}}\vert < $ 위상 특성 scale 일 때 성립.
- $T_{\mathrm{sample}}$: Poisson sampling 이 *충분히 dense* 하면 위상 보존; Nyquist-type 조건.
- $T_{\mathrm{LMS}}$: pointwise affine — 위상 보존 (선형, full-rank $\mathbf{M}_{\mathrm{LMS}}$).
- $T_{\mathrm{gain}}$: pointwise monotonic ($\log$) — 위상 보존.
- $T_{\mathrm{CSF}}$: bandpass — *고주파 위상 소실 가능* (cutoff 이상의 fine topology). 이 step 이 T-cond-5 의 *주 위협*.
- $T_{\mathrm{temp}}$: temporal smoothing — 시간 위상 보존 (causal Gamma kernel).

**Open issue**: $T_{\mathrm{CSF}}$ 의 cutoff 이상 위상 정보는 *원리상 소실*. T-cond-5 의 정확한 statement 는 *cutoff-restricted* form:

$$T_*: H_k(\mathcal{I}_{\nu \leq \nu_{\mathrm{cutoff}}}) \to H_k(\tilde{\mathcal{I}})$$

(spatial frequency-bandlimited submanifold 위에서만 rank-preserving).

**COB rationale**: Stage 3 의 PersComp 가 의미 있으려면 $T$ 가 위상을 *완전히 파괴*하지 않아야 함. Atick-Redlich (1992) 의 efficient coding 이 *information-theoretic* anchor — redundancy reduction 후에도 위상 정보가 보존됨.

**Validation requirement**: 위상-controlled 입력 (disk, annulus, figure-eight) 에 대한 $T(I)$ 의 PersComp Betti numbers 비교.

---

### §2.6 T-cond-6: $\mathrm{Aut}(G)$ Compatibility (Group Equivariance)

**Statement (formal)**: $T$ 가 그래프 자기동형군 $\mathrm{Aut}(G)$ 와 호환된다 — Stage 4 의 $\sigma_{\mathrm{standard}}$ 변환 불변성을 가능하게 함:

$$\forall \, g \in \mathrm{Aut}(G), \; \forall \, I \in \mathcal{I} : \quad T(g \cdot I) \;=\; g \cdot T(I)$$

(equivariance / intertwining property).

**Mathematical form**: $T$ 가 *group homomorphism* 의 의미에서 $\mathrm{Aut}(G)$-equivariant. 6-부 composition 에서:
- $T_{\mathrm{PSF}}$: rotation-invariant if $K_{\mathrm{PSF}}$ is rotationally symmetric (Zernike radial component); aberration 항이 *broken symmetry* 일 가능성 — astigmatism $Z_2^{\pm 2}$ 가 $\mathrm{SO}(2)$ 깸. T-cond-6 의 *주 위협*.
- $T_{\mathrm{sample}}$: hexagonal grid 의 경우 $D_6$ (dihedral) 대칭; rectangular 의 경우 $D_4$.
- $T_{\mathrm{LMS}}$: cone-ratio 가 vertex-별 다르면 group symmetry 깸.
- $T_{\mathrm{gain}}, T_{\mathrm{CSF}}, T_{\mathrm{temp}}$: pointwise / convolutional — group homomorphism 호환.

**DKL 색공간 연결**: Derrington-Krauskopf-Lennie (1984) 의 LMS → opponent (Luminance / RG / BY) 변환이 *group-theoretic 구조*: $\mathbf{M}_{\mathrm{opp}} \in \mathrm{GL}(3, \mathbb{R})$ 의 specific factorization. T-cond-6 가 color channel 의 group symmetry 와 연결 — E3 §B.3 anchor.

**Composition-level instance**:

$$\bigl[\, T_{\mathrm{LMS}}, g_G \,\bigr] \;=\; 0 \quad \forall \, g_G \in \mathrm{Aut}(G) \;\text{(commutator vanishing)}$$

여기서 $g_G$ 의 색 채널 작용은 *trivial* (cone-ratio 가 $g_G$-불변).

**COB rationale**: $\sigma_{\mathrm{standard}}$ (Stage 4) 의 변환 불변성이 ortho-stabilization 의 핵심. 만약 $T$ 가 $\mathrm{Aut}(G)$-깨짐 ($T \circ g \neq g \circ T$) 이면 $\sigma_{\mathrm{standard}}$ 가 well-defined 아님.

**Open issue**: Astigmatism (R-an-3, R-an-4 의 cylindrical aberration) 이 PSF 의 회전대칭 깸. 이는 *관찰자-specific* (각 사람의 astigmatism 축) — Cat A 격상 시 $\mathrm{Aut}(G)$ 의 *제한된 부분군* 만 commuting 의 형식이 됨.

**Validation requirement**: Stage 4 의 $\sigma_{\mathrm{standard}}$ 가 well-defined 함을 numerical 로 확인 (e.g., 대칭 입력의 일관된 $\sigma$ 출력).

---

### §2.7 T-cond-7: Temporal Continuity (반사 SDE Well-posedness)

**Statement (formal)**: 시간 매개 $t \mapsto T(I_t)$ 가 적절한 위상 의미에서 *연속*. 구체적으로 Stage 5 의 P-F-A1 (reflected SDE on $\Sigma_m$, Lions-Sznitman 1984) 의 입력으로서의 well-posedness 를 위해:

$$t \mapsto T(I_t) \;:\; [0, T_{\mathrm{end}}] \to C^0(V_{\mathrm{ret}}; \mathbb{R}_{\geq 0}^3) \quad \text{is continuous}$$

이때 driver process $b(t) := \pi_G(T(I_t))$ 가 $\Sigma_m$ 의 boundary 와의 *reflection* 을 well-define 하게 만듦.

**Mathematical form**: Stage 5 의 reflected SDE:

$$du_t \;=\; -\nabla_{\Sigma_m} E(u_t) \, dt \;+\; \sqrt{2 T_*} \, dW_t \;+\; d\Lambda_t \quad \text{(Lions-Sznitman reflection)}$$

여기서 $T_* > 0$ 는 stochastic temperature (Q6/OP-0021 의 ξ resident), $\Lambda_t$ 는 boundary local time. $T(I_t)$ 의 *입력 driver* 가 연속이어야 SDE solution 의 strong existence + pathwise uniqueness (Lions-Sznitman 1984 Thm 2.1).

**Composition-level analysis**: 6-부 composition 에서 *시간 의존성* 은 $T_{\mathrm{gain}}$ ($G(t; \tau_{\mathrm{adapt}})$ 시간 적응) 과 $T_{\mathrm{temp}}$ ($K_{\mathrm{temp}}$ 시간 합성곱) 에 집중. $T_{\mathrm{PSF}}, T_{\mathrm{sample}}, T_{\mathrm{LMS}}, T_{\mathrm{CSF}}$ 는 *순간적* (instantaneous).

- $T_{\mathrm{gain}}$ 시간 연속: $G(t; \tau_{\mathrm{adapt}}) = G_\infty + (G_0 - G_\infty) e^{-t/\tau_{\mathrm{adapt}}}$ — $C^\infty$ in $t$ ✓
- $T_{\mathrm{temp}}$ 시간 연속: causal Gamma kernel + half-wave rectification. Rectification $u \mapsto \max(u, 0)$ 가 *Lipschitz* (continuous 보존, $C^0$) — but not $C^1$. 따라서 T-cond-7 은 *$C^0$ 수준* 만 보장.

**COB rationale**: $T_*$ (Stage 5 stochastic temperature, OP-0021) 의 자체 fixed-point 가 reflected SDE 의 *invariant measure* $\pi_{T_*}$ 에 의존. 만약 driver 가 불연속이면 invariant measure 의 well-definedness 가 깨짐. Lions-Sznitman 정리의 *입력 조건* 충족이 T-cond-7 의 정확한 의미.

**Validation requirement**: $T(I_t)$ 의 시간 modulus of continuity 측정. Cat A 격상 시 *strong continuity* (e.g., $C^\alpha$ for some $\alpha > 0$) 의 boundary 결정.

---

### §2.8 T-cond-8: Observation Model Compatibility (LM1-LM3 Likelihood)

**Statement (formal)**: $T$ 의 output 이 Stage 5 의 T-K-Select-OBS (canonical) 의 likelihood 모델 LM1-LM3 와 호환:

$$\mathcal{L}_{\mathrm{LM}k}\bigl(T(I) \mid u_t, \Theta_{\mathrm{obs}}\bigr) \;>\; 0 \quad \forall \, k \in \{1, 2, 3\}, \; \forall \, (u_t, \Theta_{\mathrm{obs}}) \text{ in admissible domain}$$

(positivity of likelihood across LM1-LM3 family).

**Mathematical form**: LM1 (Gaussian), LM2 (Poisson), LM3 (heavy-tail) — `canonical.md §13` T-K-Select-OBS family. 각 LM 의 $T(I)$ likelihood 가 *non-degenerate*:
- LM1: $T(I) \vert u_t \sim \mathcal{N}(\mu_{\mathrm{LM1}}(u_t), \Sigma_{\mathrm{LM1}})$ — $T(I) \in \mathbb{R}_{\geq 0}^3$ 호환 (positivity 후 truncation 처리).
- LM2: $T(I) \vert u_t \sim \mathrm{Poisson}(\lambda_{\mathrm{LM2}}(u_t))$ — SCC unified §2.3 의 $T_{\mathrm{sample}}$ Poisson 통계와 *직접 매칭*.
- LM3: $T(I) \vert u_t \sim \mathrm{StudentT}_\nu(\mu_{\mathrm{LM3}}(u_t), \Sigma_{\mathrm{LM3}})$ — heavy-tail noise 모델, $T(I)$ 의 outlier 처리.

**Composition-level instance**: $T_{\mathrm{sample}}$ 의 Poisson 통계 (SCC unified §2.3 L312-314):

$$I_t^{\mathrm{samp}}(v) \sim \mathrm{Poisson}\!\left(\eta(v) \int_{A(v)} I_t^{\mathrm{PSF}}(x)\,dx\right)$$

가 LM2 와 native 호환. LM1 (Gaussian) 은 large-count Poisson limit 에서, LM3 는 saccade/blink 등 outlier event 처리에서.

**COB rationale**: T-K-Select-OBS (Stage 5) 의 *observation likelihood* 가 *관찰자-내부 inference* 에서만 작동 (CN-COB: 외부 ground-truth 없음). $T(I)$ 가 LM family 의 *어떤 instance* 와도 호환되어야 inference 작동.

**Validation requirement**: LM1-LM3 별로 $T(I)$ 의 likelihood 평가 가능성 확인 (likelihood ratio test 의 well-definedness).

---

### §2.9 T-cond-9: Stage 1 Coupling (Output Format)

**Statement (formal)**: $T$ 의 output $\tilde{I}_t$ 가 Stage 1 의 그래프 투영 $\pi_G$ 입력 형식과 *정확히* 호환:

$$T(I) = \tilde{I}_t \;:\; V_{\mathrm{ret}} \times [0, T_{\mathrm{end}}] \;\to\; \mathbb{R}_{\geq 0}^3$$

with:
- $V_{\mathrm{ret}}$: Stage 1 그래프 $G$ 의 vertex set (Stage 0 $T_{\mathrm{sample}}$ 에서 결정)
- 3 channels: LMS (Stage 0 $T_{\mathrm{LMS}}$ 에서 결정)
- $\mathbb{R}_{\geq 0}$: non-negativity (Stage 0 $T_{\mathrm{temp}}$ half-wave rectification 후 보장)
- 시간 의존: continuous (T-cond-7) + Stage 6 partial OT 호환 (T-cond-9 자체)

**Mathematical form**: pipeline interface specification. $\pi_G$ 의 시그니처:

$$\pi_G: \bigl\{\tilde{I}_t : V_{\mathrm{ret}} \to \mathbb{R}_{\geq 0}^3\bigr\} \;\to\; \{u^{(0)} \in \Sigma_m\}$$

가 well-defined 하려면 $\tilde{I}_t$ 의 format 이 위 사양 *정확히 일치*.

**Stage 6 partial OT 연결**: T-Temporal-Identity (canonical §13, CV-1.13 SEAL Cat A) 의 partial optimal transport 가 시간 연속 $t \mapsto u_t$ 에서 작동. $T(I_t)$ 의 시간 연속성이 *전제* (T-cond-7 의 강화) + Stage 1 input format 의 *시간 sequence* 형식.

**Composition-level instance**: SCC unified §2.9 (output specification) L492-510 의 explicit form:

$$\tilde{I}_t = T_{\mathrm{temp}} \circ T_{\mathrm{CSF}} \circ T_{\mathrm{gain}} \circ T_{\mathrm{LMS}} \circ T_{\mathrm{sample}} \circ T_{\mathrm{PSF}}(I_t) \;\in\; \mathbb{R}_{\geq 0}^{\vert V_{\mathrm{ret}}\vert \times 3}$$

format match check:
- vertex: ✓ ($V_{\mathrm{ret}}$ from $T_{\mathrm{sample}}$)
- channels: ✓ (3, from $T_{\mathrm{LMS}}$)
- positivity: ✓ (from $T_{\mathrm{temp}}$ half-wave rectification)
- time: ✓ (continuous, from T-cond-7)

**COB rationale**: pipeline interface 일치 = SCC 전체 파이프라인이 *함수 합성* 으로 well-defined. T-cond-9 위반 시 Stage 1 진입 자체가 type-error.

**Validation requirement**: Stage 1 $\pi_G$ 의 입력 format 사양과 Stage 0 $T$ 의 output format 의 *literal* 일치 (channel 수, vertex domain, codomain $\mathbb{R}_{\geq 0}$, 시간축).

---

## §3 6-Part Composition (Canonical-style)

SCC_unified_derivation_v0.1 §2.1 (L228-249) 의 *operational instance*. 각 sub-$T$ 의 *현재 Cat C SKETCH 상태* 와 9-conditions 와의 *대응 관계*.

$$\boxed{\;T_{\mathrm{sensor}} \;=\; T_{\mathrm{temp}} \circ T_{\mathrm{CSF}} \circ T_{\mathrm{gain}} \circ T_{\mathrm{LMS}} \circ T_{\mathrm{sample}} \circ T_{\mathrm{PSF}}\;}$$

### §3.1 $T_{\mathrm{PSF}}$ — Zernike Convolution

**SCC unified §2.2 (L253-285)**.

**Form**:

$$I_t^{\mathrm{PSF}}(x, y) \;=\; (K_{\mathrm{PSF}} * I_t^{\mathrm{pre}})(x, y), \quad K_{\mathrm{PSF}} = \vert \mathcal{F}[P]\vert ^2, \quad P(x,y) = \mathbf{1}_{\lvert (x,y) \rvert \leq r_{\mathrm{pup}}} \cdot e^{i \frac{2\pi}{\lambda} W(x,y)}$$

with $W(x, y) = \sum_{n,m} Z_n^m \mathcal{Z}_n^m(x/r_{\mathrm{pup}}, y/r_{\mathrm{pup}})$ (OSA/ANSI Zernike).

**Roots**: R-an-3 ($R_{\mathrm{cor}}$, 각막 곡률), R-an-4 ($A_{\mathrm{acc}}$, 조절), R-an-5 ($\{Z_n^m\}$, HOA).

**9-conditions 대응**:
- T-cond-3 (homog. existence): convolution 이 균질 신호 보존 (normalized $K_{\mathrm{PSF}}$, $\int K = 1$) ✓
- T-cond-4 (graph independence): continuous-domain convolution, graph 무관 ✓
- T-cond-5 (위상 보존): blurring 이 smooth + sub-scale features 만 smoothing — *위상 보존 부분 검증 필요*
- T-cond-6 ($\mathrm{Aut}(G)$): radial Zernike 항만 rotational symmetric, astigmatism 항 ($Z_2^{\pm 2}$) 깸 — *부분 위반*
- T-cond-7 (time continuity): instantaneous (시간 의존 없음) ✓

**Open issue (SCC unified §2.2 L284)**: Chromatic aberration (파장별 PSF 차이) — Cat A 격상 시 채널별 $K_{\mathrm{PSF}}^{(c)}$ 필요.

---

### §3.2 $T_{\mathrm{sample}}$ — Poisson Sampling on Retinal Mesh

**SCC unified §2.3 (L288-329)**.

**Form**:

$$I_t^{\mathrm{samp}}(v) \sim \mathrm{Poisson}\!\left(\eta(v) \int_{A(v)} I_t^{\mathrm{PSF}}(x)\,dx\right), \quad v \in V_{\mathrm{ret}} = V_{\mathrm{fov}} \cup V_{\mathrm{per}}$$

with vertex density $\rho_{\mathrm{cone}}^{\mathrm{fov}}, \rho_{\mathrm{rod}}(\theta)$; macular pigment $\eta(v)^{(S)} = \eta_0^{(S)} \cdot 10^{-\mathrm{OD}_{\mathrm{mac}}(v)}$.

**Roots**: R-an-6 (foveal cone density), R-an-7 (rod density profile), R-an-8 (macular pigment OD), R-an-11 (FOV).

**9-conditions 대응**:
- T-cond-1 (mass): integration $\int_{A(v)} I_t^{\mathrm{PSF}}$ 이 mass 정의 가능 ✓
- T-cond-4 (graph indep.): $V_{\mathrm{ret}}$ generation rule 이 admissible graph class 내 ✓
- T-cond-5 (위상 보존): Poisson sampling 의 Nyquist condition — *bandwidth-dependent*
- T-cond-8 (LM2): Poisson 통계 = LM2 직접 매칭 ✓

**Open issue**: Stochastic vs mean-field 처리 — SCC unified §2.3 L329 에서 Cat A 격상 시 명확화 필요.

---

### §3.3 $T_{\mathrm{LMS}}$ — Spectral Projection (LMS)

**SCC unified §2.4 (L333-364)**.

**Form**:

$$\tilde{I}_t^{\mathrm{LMS}}(v) \;=\; \mathbf{M}_{\mathrm{LMS}}(v) \cdot I_t^{\mathrm{samp}}(v), \quad \mathbf{M}_{\mathrm{LMS}}(v) \in \mathbb{R}^{3 \times 3}$$

with cone-ratio $(r_L, r_M, r_S) \in \Delta^2$ (R-an-9), color phenotype 보정 (R-an-10), color constancy gain $\mathbf{G}_{\mathrm{const}}(c_{\mathrm{const}}, \bar{I}^{\mathrm{LMS}})$.

**Roots**: R-an-9 (cone ratio), R-an-10 (color phenotype), $c_{\mathrm{const}}$ (seed decode).

**9-conditions 대응**:
- T-cond-1 (mass): linear, normalization 가능 ✓
- T-cond-4 (graph indep.): pointwise ✓
- T-cond-5 (위상 보존): linear full-rank → 위상 보존 ✓ (full-rank assumption needed)
- T-cond-6 (Aut group): cone-ratio vertex-별 다른 경우 깸 — *부분 위반*

**DKL connection**: LMS → opponent (L+M / L-M / S-(L+M)) 변환의 group-theoretic 구조 (Derrington-Krauskopf-Lennie 1984). T-cond-6 의 색-채널 부분.

---

### §3.4 $T_{\mathrm{gain}}$ — Adaptive Log-Luminance

**SCC unified §2.5 (L368-398)**.

**Form**:

$$\tilde{I}^{c,\mathrm{gain}}(v, t) \;=\; \log\!\left(\frac{\tilde{I}^{c,\mathrm{LMS}}(v, t)}{L_0} + \epsilon\right) \cdot G(t; \tau_{\mathrm{adapt}})$$

with $L_0 = \pi (d_{\mathrm{pup}}^0/2)^2 L_{\mathrm{ambient}}$, $G(t; \tau_{\mathrm{adapt}}) = G_\infty + (G_0 - G_\infty) e^{-t/\tau_{\mathrm{adapt}}}$.

**Roots**: R-nn-1 ($\tau_{\mathrm{adapt}}$), R-nn-2 ($d_{\mathrm{pup}}^0$).

**9-conditions 대응**:
- T-cond-2 (smoothness): log-compression = Weber-Fechner anchor → spinodal-compatible 매끄러움 ✓
- T-cond-7 (time continuity): $G(t)$ 가 $C^\infty$ in $t$ ✓

**Note**: $L_{\mathrm{ambient}}$ 는 $I_t$ *자체*의 평균 — *외부* calibration 통계 아님 (CN-COB 준수). SCC unified §2.5 L380 명시.

**Weber-Fechner 정밀화**: T-cond-2 의 "적당한 매끄러움"의 *생리적 instance* — JND $\propto$ stimulus magnitude (Weber 1834). T-cond-2 의 Sobolev class 매개변수 $s$ 가 $\tau_{\mathrm{adapt}}$ 와 *역방향 dependency* (빠른 적응 → fine-grained smoothness).

---

### §3.5 $T_{\mathrm{CSF}}$ — Spatial CSF Filter

**SCC unified §2.6 (L402-429)**.

**Form**:

$$\tilde{I}_t^{\mathrm{CSF}}(v) \;=\; (\hat{K}_{\mathrm{CSF}} * \tilde{I}_t^{\mathrm{gain}})(v), \quad K_{\mathrm{CSF}}(\nu) = A_{\mathrm{CSF}} \nu^a e^{-b\nu}$$

with peak $\approx 3{-}6$ cpd, cutoff $\approx 30{-}60$ cpd. Roots: R-nn-5 ($\sigma_{\mathrm{pool}}^{V1}$) → cutoff inverse. Pelli-Robson (1988) anchor.

**9-conditions 대응**:
- T-cond-2 (smoothness): bandpass → spinodal-compatible Sobolev class 결정 ✓ (*핵심 instance*)
- T-cond-5 (위상 보존): cutoff 이상 *고주파 위상* 소실 — *부분 위반* (cutoff-restricted)
- T-cond-3 (homog. existence): bandpass 가 DC 차단 → *strict* homog. fiber 통과 못함; weak form $\epsilon_{\mathrm{hom}}$-near homog. 만 ✓

**Stage 0/1 경계 open issue**: SCC unified §2.6 L428 — CSF 가 Stage 0 의 *마지막* 인지 Stage 1 의 *시작* 인지 commit 필요. 본 §3.5 에서는 *Stage 0 마지막 공간 처리* 로 commit.

---

### §3.6 $T_{\mathrm{temp}}$ — Temporal Kernel

**SCC unified §2.7 (L432-468)**.

**Form**:

$$\tilde{I}_t(v) \;=\; \int_0^t K_{\mathrm{temp}}(t - t'; \tau_{\mathrm{int}}, f_{\mathrm{temp}}) \cdot \tilde{I}_{t'}^{\mathrm{CSF}}(v)\,dt' \;\to\; \max(\cdot, 0)$$

with $K_{\mathrm{temp}}(\tau) = \frac{1}{\Gamma(k) \theta^k} \tau^{k-1} e^{-\tau/\theta} \cos(2\pi f_{\mathrm{temp}} \tau)$, $k \in \{3, 4\}$, $\tau_{\mathrm{int}} = k\theta$.

**Roots**: R-nn-3 ($\tau_{\mathrm{int}}$), R-nn-4 ($f_{\mathrm{temp}}$). Watson (1986) anchor.

**9-conditions 대응**:
- T-cond-7 (time continuity): causal convolution + half-wave rectification = $C^0$ in $t$ ✓ (not $C^1$)
- T-cond-9 (Stage 6 coupling): time-series output ready for partial OT ✓
- T-cond-1 (positivity): half-wave rectification $\max(\cdot, 0)$ 가 $\mathbb{R}_{\geq 0}^3$ 보존 ✓

**Open issue**: $k = 3$ vs $k = 4$ canonical convention 미정 (SCC unified §2.7 L447).

---

### §3.7 6-Part vs 9-Conditions Mapping Summary

| Sub-$T$ | T-cond-1 | T-cond-2 | T-cond-3 | T-cond-4 | T-cond-5 | T-cond-6 | T-cond-7 | T-cond-8 | T-cond-9 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $T_{\mathrm{PSF}}$ | – | – | ✓ | ✓ | △ | △ | – | – | – |
| $T_{\mathrm{sample}}$ | ✓ | – | – | ✓ | △ | △ | – | ✓ | – |
| $T_{\mathrm{LMS}}$ | ✓ | – | – | ✓ | ✓ | △ | – | – | – |
| $T_{\mathrm{gain}}$ | – | ✓ | – | ✓ | ✓ | ✓ | ✓ | – | – |
| $T_{\mathrm{CSF}}$ | – | ✓★ | △ | – | △ | ✓ | – | – | – |
| $T_{\mathrm{temp}}$ | ✓ | – | – | – | – | – | ✓★ | – | ✓★ |

(✓ = 만족, △ = 부분 만족 / restricted, – = 해당 없음, ★ = 주된 책임 sub-$T$)

**관측**: 9-condition 별로 *주된 책임* sub-$T$ 가 존재; △ (부분 만족) cells 가 *Open issues catalog* 의 source.

---

## §4 Canonical Entry Draft — Appendix OMS §N

E3 §B.5 의 경로 α 채택. 다음은 *draft* — canonical edit 아님; Phase 4 의 별도 commit turn 에서 사용자 승인 후 등록.

### §4.1 Proposed canonical §N structure

```
canonical.md Appendix OMS §N — Stage 0 T Axiomatic Package (AUX-1.5 §4.5 promotion)

§N.1 Definition (Stage 0 sensor T : I → tilde{I})
  - 입력 공간 I (CN-COB-respecting raw input, COB 비대상 — AUX §4.9.8)
  - 출력 공간: V_ret × [0, T_end] → R_{≥0}^3
  - Cat 분류: P (관찰자-개인, ξ resident with §N below 의 9 axioms)

§N.2 9-Conditions (T-cond-1 ~ T-cond-9)
  - 각 조건의 formal statement (본 D5 §2 참조)
  - Cat 분류: 9×A (axiom on P) — AUX §4.9.9

§N.3 6-Part Composition (operational instance)
  - T = T_temp ∘ T_CSF ∘ T_gain ∘ T_LMS ∘ T_sample ∘ T_PSF
  - 현재 Cat C SKETCH (SCC_unified_derivation_v0.1 §2)
  - 6-부 ↔ 9-cond mapping (본 D5 §3.7)

§N.4 Anatomical + Neural Parameter Dependence
  - R-an-3 ~ R-an-11 (anatomical roots, 8 항목)
  - R-nn-1 ~ R-nn-5 (neural roots, 5 항목)
  - Seed-decoded idio: c_const

§N.5 Cat A Axiomatic Registration + Non-Overclaim
  - 본 §N entry 는 axiomatic declaration (T 위에 9 axioms 부과)
  - mathematical proof of existence (T satisfying all 9) is OPEN — OP-AUX-T-FIXED-POINT (별도)
  - 6-부 composition 의 Cat A 격상은 OPEN — Cat C SKETCH 수준 유지
```

### §4.2 SEAL-style Draft Entry (CV-1.18 prep)

```
═══════════════════════════════════════════════════════════════
canonical.md §13.5 (또는 Appendix OMS §N) — DRAFT for CV-1.18 SEAL
═══════════════════════════════════════════════════════════════

DEFINITION — Stage 0 Sensor Transformation T

Stage 0 의 sensor transformation T : I → tilde{I} 는 다음 9 axioms 를 만족하는
관찰자-개인 변환 (P) 으로 정의된다. 구체적 instance 는 6-부 composition
(T = T_temp ∘ T_CSF ∘ T_gain ∘ T_LMS ∘ T_sample ∘ T_PSF, Cat C SKETCH) 에 의해
제공된다.

AXIOM PACKAGE — T-cond-1 ~ T-cond-9 (각각 Cat A on P)

[T-cond-1] (Mass-preservation) ∀ I ∈ I, π_G(T(I)) ∈ Σ_m.
[T-cond-2] (Spinodal-compatible smoothness) ∃ s ∈ (0,1) : T(I) ∈ H^s(V_ret).
[T-cond-3] (Homog. fiber existence) {I : T(I) ≡ c·1} ≠ ∅ (weak form, ε_hom-near).
[T-cond-4] (Graph-class independence) ∀ G ∈ G_admissible : T(I)|_{V_G} ∈ D_G^admissible.
[T-cond-5] (Topology preservation, cutoff-restricted)
            T_* : H_k(I_{ν ≤ ν_cutoff}) → H_k(tilde{I}) rank-preserving.
[T-cond-6] (Aut(G) compatibility, partial)
            ∀ g ∈ Aut(G)|_{compat} : T(g·I) = g·T(I).
[T-cond-7] (Temporal continuity) t ↦ T(I_t) : [0, T_end] → C^0(V_ret) continuous.
[T-cond-8] (LM1-LM3 observation likelihood) L_{LMk}(T(I) | u_t, Θ_obs) > 0.
[T-cond-9] (Stage 1 coupling) T(I) ∈ R_{≥0}^{|V_ret| × 3}, Stage 6 partial OT 호환.

CAT CLASSIFICATION

 - T 자체: Cat P (관찰자-개인 변환, ξ resident)
 - T-cond-1 ~ T-cond-9: 9 × Cat A (axiom on P)
 - 6-부 composition (T_temp ∘ ... ∘ T_PSF): Cat C SKETCH
   (canonical 등록 X; SCC_unified_derivation_v0.1 §2 에 위치)

ROOT DEPENDENCIES

 - Anatomical: R-an-3 (R_cor), R-an-4 (A_acc), R-an-5 ({Z_n^m}),
               R-an-6 (ρ_cone^fov), R-an-7 (ρ_rod(θ)), R-an-8 (OD_mac),
               R-an-9 ((r_L, r_M, r_S)), R-an-10 (color phenotype),
               R-an-11 ((ω_h, ω_v, θ_fov))
 - Neural: R-nn-1 (τ_adapt), R-nn-2 (d_pup^0), R-nn-3 (τ_int),
           R-nn-4 (f_temp), R-nn-5 (σ_pool^V1)
 - Seed: c_const (color constancy strength, idio entry)

NON-OVERCLAIM

 - 본 §N entry 는 axiomatic declaration — 9 axioms 의 simultaneous
   satisfiability 의 mathematical proof 아님 (OP-AUX-T-FIXED-POINT, OPEN).
 - 6-부 composition 은 Cat C SKETCH — Cat A 격상은 (a) chromatic aberration
   처리, (b) Poisson stochastic vs mean-field 명확화, (c) CSF Stage 0/1
   경계 commit, (d) Gamma kernel k=3 vs k=4 canonical convention 결정
   등의 separate session 필요.
 - T-cond-3 (homog. fiber): bandpass CSF 로 인해 *strict* form 은 falsifiable,
   *weak form* (ε_hom-near homog.) 으로만 성립.
 - T-cond-5 (위상 보존): *cutoff-restricted* — 고주파 위상 소실은 framework
   의 acceptable loss.
 - T-cond-6 (Aut(G)): astigmatism (R-an-5) 으로 인해 *부분* commutator
   vanishing 만 성립.

═══════════════════════════════════════════════════════════════
END DRAFT
═══════════════════════════════════════════════════════════════
```

### §4.3 OP-AUX-T-FIXED-POINT 의 Forward Hook

§N.5 Non-Overclaim 의 (proof of existence OPEN) 항목이 새 OP 후보:

```
OP-AUX-T-FIXED-POINT (proposed)

Statement: 9 axioms T-cond-1 ~ T-cond-9 를 *동시에* 만족하는 T : I → tilde{I}
           가 존재하는가? 만약 존재한다면 modular space (T 의 자유도) 의 
           dimension 은? 6-부 composition 이 이 fixed-point 의 한 instance 인가?

Status: OPEN
Required for: Cat C SKETCH (6-부 composition) → Cat A 격상 path
Dependencies: 9-axioms simultaneous compatibility + 6-부 composition Cat A 격상
Phase: W10+ (멀티-세션, 각 sub-T 의 Cat A 격상 후 동시 적합성 분석)
```

이 OP 는 theorem_status.md 에 등록 권고 (Phase 4 의 commit turn).

---

## §5 Empirical Validation Requirements (Cat A axiomatic + Validation Path)

각 condition 의 *empirical anchor* 와 *validation experiment* 명시. 핵심 원칙: COB-respecting — 외부 환경 통계가 아니라 *관찰자 자체의 측정 가능 속성*.

### §5.1 T-cond-1 (Mass-preservation): 광도 측정 + Σ_m 매핑

**Validation experiment**:
1. Standardized 입력 (e.g., 균질 회색 화면, calibrated luminance)
2. $T(I)$ output 의 $L^1$-norm 측정 ($\sum_v \tilde{I}_t(v)$)
3. Mass-normalization step ($\pi_G$) 후 $\Sigma_m$ membership 확인

**Anchor**: photometric saturation curve (Weber 1834 + modern psychophysics, e.g., adaptation TVI curves)

**Cat A path**: ⭕ 측정 가능, ✗ 외부 통계 미사용 ✓

---

### §5.2 T-cond-2 (Smoothness): Photometric TVI Curve

**Validation experiment**: Threshold-vs-Intensity (TVI) curve 측정
- 다양한 background luminance $L_b$ 에서 just-noticeable difference $\Delta L$ 측정
- Weber-Fechner: $\Delta L / L_b \approx $ const → log-compression confirm
- $\tau_{\mathrm{adapt}}$ (R-nn-1) 추정

**Anchor**: Weber 1834, Fechner 1860 (psychophysical law); Crawford (1947) dark adaptation curves

**Cat A path**: TVI curve 의 Sobolev exponent $s$ 추정 가능. R-nn-1 분포 하에서 $s \in (0, 1)$ 범위 확률 정량화 (W10+).

---

### §5.3 T-cond-3 (Homog. fiber): Uniform Field Spatial Variance

**Validation experiment**: 균질 입력 (uniform gray field) 의 perceived spatial variance 측정
- Output $T(I^{\mathrm{hom}})$ 의 $\mathrm{Var}_v[\tilde{I}_t(v)]$ 측정
- weak form $\epsilon_{\mathrm{hom}}$ 정량화

**Anchor**: Ganzfeld stimulus 실험 (Metzger 1930) — 균질 시야의 *perceptual fading*

**Cat A path**: $\epsilon_{\mathrm{hom}}$ 의 R-an-5 (HOA) + R-nn-5 (CSF cutoff) 의존성 정량화.

---

### §5.4 T-cond-4 (Graph independence): Multi-Mesh Consistency

**Validation experiment**: 동일 $I$ 입력에 대해 다양한 admissible graph $G$ (square grid, hex, Voronoi mesh) 에 투영한 후 Stage 2 수렴 거동 비교
- $T(I)\vert _{V_G}$ 의 graph-별 distribution 비교
- Stage 2 ($u_t$) 의 graph-invariance 확인

**Anchor**: theoretical only — 6-부 composition 의 graph-free property (continuous PSF, pointwise LMS/gain, vertex-rule sampling)

**Cat A path**: 본 condition 은 *구성적* 으로 만족 (sub-T 별 graph-free); empirical 은 *Stage 2 결과의 graph 무관성* 으로 indirect.

---

### §5.5 T-cond-5 (Topology preservation): Persistence Stability

**Validation experiment**: Topology-controlled 입력 (disk, annulus, figure-8) 의 $T(I)$ PersComp Betti numbers 측정
- $H_0$ (connected components), $H_1$ (1-cycles) 카운트 안정성
- Cutoff $\nu_{\mathrm{cutoff}}$ 이하에서 stable 확인

**Anchor**: Atick-Redlich (1992) "What does the retina know about natural scenes?" — efficient coding hypothesis. 단 본 framework 에서는 *환경 통계 비사용* — 위상 보존은 $T$ 의 *내재 속성* 으로 해석.

**Cat A path**: $\nu_{\mathrm{cutoff}}$ 의 R-nn-5 의존성 + topology preservation rank 정량화.

---

### §5.6 T-cond-6 (Aut(G) compat.): Symmetric Pattern Equivariance

**Validation experiment**: 대칭 입력 (e.g., grating, checkerboard) 에 대해 $T(g \cdot I)$ 와 $g \cdot T(I)$ 의 비교
- Commutator $[T, g]$ 의 magnitude 측정
- Astigmatism (R-an-5 의 $Z_2^{\pm 2}$) 에 따른 broken symmetry 정량화

**Anchor**: Derrington-Krauskopf-Lennie (1984) DKL color space — LMS group structure

**Cat A path**: ⭕ Commuting subgroup $\mathrm{Aut}(G)\vert _{\mathrm{compat}}$ 의 정량적 특성화.

---

### §5.7 T-cond-7 (Temporal continuity): CFF + Motion-Detection

**Validation experiment**:
1. Critical Flicker Fusion (CFF) frequency 측정 → $T_{\mathrm{temp}}$ 의 시간 해상도
2. Smooth pursuit eye movement 의 perceived smoothness — $C^0$ continuity check
3. Motion-induced phase lag 측정 → $\tau_{\mathrm{int}}$ (R-nn-3) 추정

**Anchor**: Watson (1986) temporal CSF; Lions-Sznitman 1984 (reflected SDE well-posedness, *upstream theory*)

**Cat A path**: $C^0$ continuity 의 modulus 추정; $C^\alpha$ for $\alpha > 0$ 의 boundary 결정.

---

### §5.8 T-cond-8 (Observation likelihood): LM1-LM3 Inference Fit

**Validation experiment**: $T(I)$ 의 *internal* observation 노이즈 분포 추정
- Poisson statistics (LM2) 의 직접 측정 ($T_{\mathrm{sample}}$ 의 광자 잡음)
- Gaussian limit (LM1) 의 high-illumination regime confirm
- Heavy-tail (LM3) 의 saccade/blink artifact 분포

**Anchor**: theoretical only — Stage 5 T-K-Select-OBS family 의 *내부* observation model. 외부 ground-truth 없음 (CN-COB).

**Cat A path**: LM family 적합성의 *self-consistency* check (관찰자 내부 inference 결과의 consistency).

---

### §5.9 T-cond-9 (Stage 1 coupling): Pipeline Integration Test

**Validation experiment**: Stage 0 output 을 Stage 1 $\pi_G$ 에 *직접* 입력 → type-check
- Output format ($\vert V_{\mathrm{ret}}\vert \times 3$, $\mathbb{R}_{\geq 0}$) literal match
- Stage 1 진입 후 spinodal regime 통과 확률 측정

**Anchor**: theoretical only — pipeline interface

**Cat A path**: Constructive (sub-T 별 output 사양으로 인해 자동 만족).

### §5.10 Validation Summary Table

| Cond | Type | Anchor | Cat A Path 가능성 |
|---|---|---|---|
| T-cond-1 | Photometric | Weber 1834, TVI curves | ✓ short-term |
| T-cond-2 | Psychophysical | Weber-Fechner, Crawford 1947 | ✓ short-term |
| T-cond-3 | Psychophysical | Ganzfeld (Metzger 1930) | ⚠ weak form only |
| T-cond-4 | Theoretical | constructive | ✓ structural |
| T-cond-5 | Persistence | Atick-Redlich 1992 (re-interpret) | ⚠ cutoff-restricted |
| T-cond-6 | Symmetric | DKL 1984 | ⚠ partial (astigmatism) |
| T-cond-7 | Temporal | Watson 1986, Lions-Sznitman | ✓ short-term |
| T-cond-8 | Theoretical | LM1-LM3 internal | ✓ structural |
| T-cond-9 | Theoretical | Pipeline interface | ✓ constructive |

**핵심 관측**: 4 conditions (T-cond-1, T-cond-2, T-cond-7) 는 *short-term* (~1 session) Cat A path 가능; 3 conditions (T-cond-3, T-cond-5, T-cond-6) 는 *restricted form* 만 Cat A; 4 conditions (T-cond-4, T-cond-8, T-cond-9) 는 *constructive* (자동 만족).

---

## §6 Counterexample Attempts (≥3 explicit)

본 9-condition framework 의 *boundary* 를 명시하기 위해, 9-cond 중 하나를 위반하는 hypothetical $T$ 의 예시 + failure mode.

### §6.1 Attempt 1: Stage 0 $T$ 가 환경 통계 의존 (T-cond-7 COB-혼동 시험)

**Setup**: 가정 $T$ 가 *natural image priors* $p_{\mathrm{env}}(I)$ 를 통해 sharpening:

$$T_{\mathrm{env}}(I) := T_{\mathrm{base}}(I) + \alpha \cdot \nabla_I \log p_{\mathrm{env}}(I)$$

여기서 $p_{\mathrm{env}}$ 는 *외부* 자연 이미지 데이터셋 (e.g., ImageNet, McGill) 으로 fit.

**Failure mode**: **CN-COB 위반** — $T_{\mathrm{env}}$ 가 외부 환경 통계 $p_{\mathrm{env}}$ 를 도입. SCC 의 closed ontological budget (관찰자-개인 P + 자체 axioms A + u-derived D) 의 *경계 밖*.

**Diagnosis**: 본 framework 의 Stage 0 $T$ axioms 는 *CN-COB 통과* 가 *전제* — Atick-Redlich 의 자연영상 통계 활용은 외부 reference 로만 (validation anchor); $T$ 자체의 *구성* 에는 사용 불가.

**참고**: AUX-1.5 §7 (COB 원칙) + §4.5 의 "T는 관찰자-개인 (P)" 명시.

---

### §6.2 Attempt 2: Non-linear PSF (T-cond-3 위반 시험)

**Setup**: 가정 $T$ 가 *energy-dependent PSF*:

$$K_{\mathrm{PSF}}^{\mathrm{nonlin}}(x; I_{\mathrm{intensity}}) \;=\; K_{\mathrm{PSF}}^0(x) \cdot \bigl(1 + \beta \cdot I_{\mathrm{intensity}}\bigr)$$

intensity-dependent blurring (높은 강도에서 더 큰 PSF, 예: glare 효과).

**Failure mode**: **T-cond-3 (homog. existence) 약화** + **T-cond-2 (smoothness regime) 변형**. 균질 입력 $I^{\mathrm{hom}}$ 의 경우 nonlinear PSF 가 균질 출력 유지하지만, near-homog. 의 *변동* 이 intensity-dependent — Stage 1 의 unstable homogeneous fixed point 가 *왜곡* 됨.

**Diagnosis**: 본 framework 의 $T_{\mathrm{PSF}}$ 는 *linear convolution* (SCC unified §2.2). Nonlinear PSF 는 framework 의 *linear approximation 외부* — 별도 OP (e.g., OP-Stage-0-3, §9 참조).

**참고**: SCC unified §2.2 L271-275 (linear convolution 명시).

---

### §6.3 Attempt 3: Inversion-violating Gain (T-cond-5 위상 보존 위반)

**Setup**: 가정 $T_{\mathrm{gain}}$ 이 *quadratic compression* (vs log):

$$T_{\mathrm{gain}}^{\mathrm{quad}}(L) \;=\; L^2 / L_0$$

(Weber-Fechner *위반* — quadratic 은 high-luminance 에서 *expanding*, not compressing).

**Failure mode**: **T-cond-5 (위상 보존) 위반** — quadratic 압축이 *non-monotonic* 인 경우 (e.g., $T_{\mathrm{gain}}^{\mathrm{quad}}(L) - T_{\mathrm{gain}}^{\mathrm{quad}}(L')$ 의 부호가 $L, L'$ 분포에 따라 결정) 위상 정보의 *fold* 발생 — disk → folded structure.

**Diagnosis**: $T_{\mathrm{gain}}$ 의 *monotonicity* 가 T-cond-5 의 핵심. Weber-Fechner log-compression 은 strictly monotonic → 위상 보존. Quadratic 은 non-injective (e.g., $L = \pm a$ 매핑 동일) → information creation/loss → reversibility 위반.

**Diagnosis (additional)**: 본 framework 의 $T_{\mathrm{gain}}$ 은 *strictly monotonic log* — pointwise injection. Quadratic compression 은 framework 의 *injectivity assumption 외부*.

**참고**: SCC unified §2.5 L382-384 (log-compression 명시).

---

### §6.4 Attempt 4 (bonus): Time-Reversed $T_{\mathrm{temp}}$ (T-cond-7 위반)

**Setup**: 가정 $T_{\mathrm{temp}}$ 의 kernel 이 *non-causal* (예: $K_{\mathrm{temp}}(\tau)$ for $\tau < 0$):

$$\tilde{I}_t(v) \;=\; \int_{-T_{\mathrm{end}}}^{T_{\mathrm{end}}} K_{\mathrm{temp}}^{\mathrm{ncc}}(t - t') \cdot \tilde{I}_{t'}(v)\,dt' \quad (\text{non-causal})$$

**Failure mode**: **CN-COB 시간 방향 위반** + **T-cond-7 변형**. Non-causal kernel 이 미래 정보 $\tilde{I}_{t'}$ ($t' > t$) 를 사용 → 관찰자의 *시간적 인과성* 위반.

**Diagnosis**: SCC unified §2.7 L456 명시 — "causal ($t' \leq t$ 만 사용) 임에 주목 — 미래 정보 사용 금지 (CN-COB 의 시간 방향 적용)". Non-causal $T_{\mathrm{temp}}$ 는 framework 의 *causality assumption 외부*.

**참고**: Stage 5 reflected SDE 의 *time-adapted filtration* 도 causal — 일관성.

---

### §6.5 Counterexample Summary

| Attempt | Violated condition | Type | Framework status |
|---|---|---|---|
| 1: 환경 통계 | T-cond-7 COB (간접) | CN-COB 위반 | *Outside framework* |
| 2: Non-linear PSF | T-cond-3 + T-cond-2 | Linear approx. 외부 | Extension (Op-Stage-0-3) |
| 3: Quadratic gain | T-cond-5 + 단사성 | Monotonicity 외부 | *Outside framework* |
| 4: Non-causal temporal | T-cond-7 + causality | Time-causal 외부 | *Outside framework* |

**핵심 메시지**: 9-condition framework 는 *non-vacuous* — 위반 시 명확한 failure mode 가 존재. 본 framework 의 boundary 가 명시적.

---

## §7 Cat 자기 분류 + Honest Assessment

### §7.1 Cat A axiomatic (Stage 0 axiom package)

**자기 분류**: **9×A (axiom on P)**

- $T$ 자체: Cat P (관찰자-개인 변환, ξ resident)
- T-cond-1 ~ T-cond-9: 9 axioms on $T$ (A on P, AUX §4.9.9 결정)
- 6-부 composition (operational instance): Cat C SKETCH

**Cat A entry path**:
1. canonical.md Appendix OMS §N 신설 (본 §4 의 draft 사용)
2. theorem_status.md 등록: "Stage 0 $T$ axiom package — 9 × Cat A on P; 6-part composition Cat C SKETCH; OP-AUX-T-FIXED-POINT (proposed) OPEN"
3. THEORY/CHANGELOG.md 갱신: CV-1.18 entry "Stage 0 §N 신설 + 9-axioms; OP-AUX-T-FIXED-POINT 등록"

**근거**:
- AUX-1.5 §4.5: T 자체가 *관찰자-개인* (P, ξ resident); 9-조건은 *T 위 axioms* (A on P)
- AUX-1.5 §4.9.9: "9 × Cat A (T axiom, A on P)" 진단 명시
- E3 §B.5: 경로 α (Appendix OMS §N) 권고 — canonical 최소 변경

### §7.2 Honest assessment

**무엇이 달성되었나**:
- 9-조건의 *수학적 formal form* — 자연어 → registry-grade formal 격상.
- 6-부 composition 의 *각 sub-$T$* 와 9-조건의 *대응 관계* (본 §3.7 table).
- canonical entry draft (본 §4.2 SEAL-style) — 즉시 사용 가능.
- 4 counterexample attempts — framework boundary 명시.

**무엇이 미해결인가**:
- **9-조건 동시 satisfiability**: 9 axioms 가 동시에 만족 가능한 $T$ 의 존재 증명 = *OP-AUX-T-FIXED-POINT* (OPEN, W10+).
- **각 sub-T 의 Cat A 격상**: $T_{\mathrm{PSF}}$ (chromatic aberration), $T_{\mathrm{sample}}$ (stochastic Poisson 처리), $T_{\mathrm{LMS}}$ (color phenotype 일반화), $T_{\mathrm{CSF}}$ (Stage 0/1 경계), $T_{\mathrm{temp}}$ (k=3 vs 4 convention) — 5 sub-T 각각 별도 session.
- **Empirical validation**: 9 conditions 각각의 psychophysical anchor 측정 (본 §5 table) — long-term (W10+ multi-session).
- **T-cond-3 strict vs weak form**: bandpass CSF 로 인한 *DC 차단* 문제 — Cat A 격상 시 strict form (정확한 균질 fiber) 가능성 분석 필요.
- **T-cond-5 cutoff 처리**: 고주파 위상 *unavoidable loss* — framework 의 *acceptable loss* boundary 결정.
- **T-cond-6 astigmatism**: R-an-5 의 cylindrical aberration 으로 인한 *부분* commutator vanishing — *quantitative* 처리 (어느 $g \in \mathrm{Aut}(G)$ 가 commutes 하는가) 별도 session.

### §7.3 Cat A entry path — 즉시 가능

**즉시 (본 D5 출력 → Phase 4 commit turn)**:
- canonical.md Appendix OMS §N 신설 (본 §4.1 structure + §4.2 SEAL draft)
- theorem_status.md 등록 (9 × Cat A on P + 1 OP)
- CHANGELOG.md CV-1.18 entry

**W10+ (별도 session)**:
- 6-부 composition Cat C SKETCH → Cat A 격상 (5 sub-T 각각)
- OP-AUX-T-FIXED-POINT 의 simultaneous satisfiability 증명 시도
- Psychophysical validation experiments (9 conditions 각각)

### §7.4 본 D5 output 의 *self-imposed limit*

본 D5 출력 (P5 D5 Opus) 의 *scope* 명시:
- ✓ 9-조건의 수학적 formal form
- ✓ 6-부 composition 과 9-조건의 매핑
- ✓ canonical entry draft (§N)
- ✓ Empirical validation requirements (anchor + experiment)
- ✓ ≥3 counterexample attempts
- ✓ Cat 자기 분류 + Honest assessment
- ✗ 실제 canonical edit (Phase 4 commit turn 의 책임)
- ✗ Sub-T Cat A 격상 시도 (별도 session)
- ✗ Empirical validation 실행 (psychophysics experiment 별도)
- ✗ OP-AUX-T-FIXED-POINT 의 실제 증명 시도 (W10+)

---

## §8 Integration with Canonical

### §8.1 Appendix OMS §N draft (CV-1.18 SEAL prep)

본 §4.2 의 SEAL-style draft 가 CV-1.18 SEAL turn 의 입력. 권장 commit sequence:

```
CV-1.18 SEAL turn:
  1. canonical.md L2663 (Appendix OMS §M 끝) 다음에 §N 삽입
       — 본 §4.1 + §4.2 SEAL-style draft 사용
  2. canonical.md §A (Definition OMS-1, L2416) 의 ξ ∈ B_ξ 라인에 
     "(ξ-catalog: see §C below + §N for T)" 주석 추가
       — D6 의 ξ catalog amendment 와 결합
  3. theorem_status.md 의 Cat A 카탈로그에 9 axioms (T-cond-1 ~ T-cond-9)
     등록 — "9 × Cat A on P (AUX §4.9.9 promotion)"
  4. theorem_status.md Open Problems 에 OP-AUX-T-FIXED-POINT 등록 —
     "T 가 9 axioms 동시 만족? Modular space dimension?"
  5. THEORY/CHANGELOG.md CV-1.18 entry: 
     "Stage 0 §N 신설 (9 × Cat A on P); 6-부 composition 명시 (Cat C SKETCH);
      OP-AUX-T-FIXED-POINT 등록"
```

### §8.2 OMS-1 ξ catalog T_* entry (D6 P6) 와의 coupling

E3 §D 의 cross-reference:

- **D5 (Stage 0 $T$, 본 P5)** ↔ **D6 (OMS-1 ξ catalog T_*, P6)**:
  - $T_*$ 는 Stage 5 의 stochastic temperature (관찰자-개인 ξ entry); $T$ 는 Stage 0 의 sensor transformation (관찰자-개인 P 자체)
  - 두 entry 는 *분리* (SCC unified §2.5 L392 명시: "T_* 는 Stage 5 ... *별개 개념*")
  - 단, T-cond-7 (시간 연속) 이 T_* well-posedness (Lions-Sznitman) 의 *입력 전제*
  - D6 의 ξ catalog §C entry 는 본 §N entry 와 *병행* — canonical.md §A 의 ξ ∈ B_ξ 가 두 entry 모두 가리킴

**Coordinated canonical structure** (CV-1.18 후):
```
canonical.md §A: ξ ∈ B_ξ (ξ-catalog: §C [D6 의 T_*], §N [본 D5 의 Stage 0 T])
canonical.md §C: T_* ξ-entry (D6 결과)
canonical.md §N: Stage 0 T axiomatic package (본 D5 결과)
```

### §8.3 SCC_unified_derivation_v0.1 §2 의 canonical 확인

본 D5 output 후 SCC_unified_derivation_v0.1 §2 의 Cat 분류:
- 현재: Cat C SKETCH (6-부 composition)
- D5 후: Cat C SKETCH 유지 — 단 "9 × Cat A axioms (canonical §N) 의 *constructive instance*" 명시

즉, 6-부 composition 은 *Cat C* 이지만 9 axioms 는 *Cat A* — 후자는 *axiomatic declaration*, 전자는 *constructive proposal*. 두 Cat 의 *별개* 상태 유지.

---

## §9 New Open Questions (≥3)

### §9.1 OP-Stage-0-1: Psychophysical Validation per Condition

**Statement**: T-cond-1 ~ T-cond-9 각각의 *empirical validation* 실험 설계 + 실행. 본 §5 의 validation table 의 *concrete instance*.

**Required for**: 9-조건 framework 의 *empirical grounding*. Cat A axiomatic declaration 의 *validation* 보강.

**Phase**: W10+ multi-session. 9 conditions × ~1 session/cond = ~10 sessions.

**Dependencies**:
- T-cond-2: Weber-Fechner JND apparatus
- T-cond-5: persistence stability with topology-controlled stimuli
- T-cond-6: symmetric pattern equivariance test
- T-cond-7: CFF + smooth pursuit
- (나머지) constructive 또는 theoretical-only

**Priority**: 중-고 (framework grounding).

---

### §9.2 OP-Stage-0-2: Non-linear PSF Extension (T-cond-3 generalization)

**Statement**: $T_{\mathrm{PSF}}$ 가 *non-linear* (e.g., intensity-dependent kernel, glare 효과) 인 경우의 9-condition framework 확장. 본 §6.2 의 counterexample 의 *방향 전환* — failure mode 인지 framework 확장 가능성인지.

**Required for**: 실제 인간 시각의 *non-linear optical effects* (glare, saccade-induced motion blur) 를 framework 내로 포섭.

**Phase**: W12+ (multi-session, sub-T Cat A 격상과 결합).

**Dependencies**:
- $T_{\mathrm{PSF}}$ 의 linear → non-linear 확장
- T-cond-3 (homog. fiber) 의 nonlinear 형태 재정의

**Priority**: 중 (extension, not necessity).

---

### §9.3 OP-Stage-0-3: Bayesian Observer / FEP Integration

**Statement**: 9-condition framework 와 Free Energy Principle (FEP, Friston 2010) 의 *active inference* observer 사이의 관계. 특히 T-cond-8 (LM1-LM3 observation likelihood) 가 FEP 의 *generative model* 과 어떻게 mapping 되는가.

**Required for**: SCC 의 Stage 5 inference (T-K-Select-OBS) 와 FEP active inference 의 *연결고리* — 더 넓은 perception 이론과의 통합.

**Phase**: W14+ (long-term, theoretical integration).

**Dependencies**:
- Stage 5 T-K-Select-OBS 의 Bayesian 해석
- FEP 의 generative model 의 SCC-compatible formulation

**Priority**: 저-중 (long-term integration).

---

### §9.4 OP-Stage-0-4 (bonus): Multi-modal Extension

**Statement**: Stage 0 framework 가 vision-only — *audio*, *somatosensory*, *multimodal* 입력에 대한 일반화. 각 modality 의 sub-$T$ composition 의 다른 부분 ($T_{\mathrm{cochlear}}, T_{\mathrm{tactile}}, \ldots$).

**Required for**: SCC 의 cross-modal perception 이론 확장.

**Phase**: W16+ (long-term).

**Dependencies**:
- modality-specific sub-T 들의 catalog
- 9-condition framework 의 modality-independent formulation

**Priority**: 저 (long-term extension).

---

## §10 Summary

### §10.1 본 D5 의 *결과물*

1. **9-조건 formal mathematical statements** (T-cond-1 ~ T-cond-9, 본 §2)
2. **6-부 composition 의 9-cond mapping** (본 §3.7 table)
3. **Canonical entry draft (§N for CV-1.18 SEAL)** (본 §4.2)
4. **Empirical validation requirements per condition** (본 §5 table)
5. **4 counterexample attempts** (본 §6, framework boundary 명시)
6. **Cat 자기 분류 + Honest assessment** (본 §7)
7. **4 new open questions** (본 §9, W10+ forward hooks)

### §10.2 Cat verdict

**자기 분류**: **9 × Cat A axiomatic on P** (T 는 관찰자-개인 P; 9 conditions 는 T 위 axioms)

**6-부 composition**: Cat C SKETCH (유지) — operational instance only.

**Canonical entry status**: **DRAFT ready** — Phase 4 commit turn 에서 사용자 승인 후 등록.

### §10.3 Phase 4 Hand-off Items

다음은 본 D5 output 이 Phase 4 _SUMMARY_v0.2.md consolidation 으로 전달되는 항목:

| 항목 | 위치 | 출력 type |
|---|---|---|
| 9-axioms formal statements | 본 §2 + §4.2 SEAL draft | canonical §N draft |
| 6-part composition table | 본 §3.7 | canonical §N.3 |
| Validation requirements | 본 §5 table | canonical §N.5 Non-Overclaim |
| Counterexamples | 본 §6.5 summary | canonical §N.5 Non-Overclaim |
| OP-AUX-T-FIXED-POINT | 본 §4.3 + §9.1 | theorem_status.md Open Problems |
| OP-Stage-0-2, -3, -4 | 본 §9.2-§9.4 | theorem_status.md Open Problems (low-priority) |
| CHANGELOG.md CV-1.18 entry | 본 §8.1 step 5 | CHANGELOG.md |

### §10.4 Canonical edits made by this document

**ZERO** (read-only).

본 D5 출력은 canonical.md / theorem_status.md / CHANGELOG.md 를 *수정하지 않는다*. 모든 entry 는 *draft* 형식. Phase 4 commit turn 에서 사용자 명시 승인 후 등록.

---

## §11 Cross-Reference Index

### §11.1 Internal (본 D5 문서 내부)

| 본 § | Topic | Forward / Backward link |
|---|---|---|
| §0 | Pre-work + frontmatter | → §1 |
| §1 | Statement (Cat A axiomatic entry target) | ← §0; → §2, §4 |
| §2 | 9-conditions explicit list | ← §1; → §3 |
| §3 | 6-part composition | ← §2; → §4 |
| §4 | Canonical entry draft (§N) | ← §3; → §8 |
| §5 | Empirical validation requirements | ← §4; → §9 |
| §6 | Counterexample attempts | ← §5; → §7 |
| §7 | Cat 자기 분류 + honest assessment | ← §6; → §8 |
| §8 | Integration with canonical | ← §7; → §10 |
| §9 | New open questions | ← §8; → §10 |
| §10 | Summary + hand-off | ← §9 |
| §11 | Cross-reference index | (this) |

### §11.2 External (canonical / AUX / SCC unified)

| Anchor | Path | 위치 in 본 D5 |
|---|---|---|
| AUX-1.5 §4.5 | `auxiliary_structures_master.md` L303-365 | §0.2, §1, §2 |
| AUX-1.5 §4.9.9 | `auxiliary_structures_master.md` L748-764 | §1, §7 |
| SCC unified §2.1 | `SCC_unified_derivation_v0.1.md` L228-249 | §3 (전체) |
| SCC unified §2.2 ($T_{\mathrm{PSF}}$) | L253-285 | §3.1, §6.2 |
| SCC unified §2.3 ($T_{\mathrm{sample}}$) | L288-329 | §3.2, §5.8 |
| SCC unified §2.4 ($T_{\mathrm{LMS}}$) | L333-364 | §3.3 |
| SCC unified §2.5 ($T_{\mathrm{gain}}$) | L368-398 | §3.4, §6.3 |
| SCC unified §2.6 ($T_{\mathrm{CSF}}$) | L402-429 | §3.5, §2.5 |
| SCC unified §2.7 ($T_{\mathrm{temp}}$) | L432-468 | §3.6, §6.4 |
| canonical Appendix OMS §A | `canonical.md` L2404-2420 | §4, §8 |
| E3 §B | `/tmp/scc_proofs_v02/E3_hmorse_stage0_oms.md` L176-298 | §0, §1, §10 |
| Weber-Fechner (1834, 1860) | external | §2.2, §3.4, §5.2 |
| Pelli-Robson (1988) | external | §2.2, §3.5 |
| Watson (1986) | external | §3.6, §5.7 |
| Atick-Redlich (1992) | external | §2.5, §5.5 |
| Derrington-Krauskopf-Lennie (1984) | external | §2.6, §3.3, §5.6 |
| Lions-Sznitman (1984) | external | §2.7, §5.7 |

---

## §12 Closing Note

본 D5 output (P5 — Stage 0 sensor T 9-conditions canonical entry path) 은 **Cat A axiomatic 등록 가능 수준의 draft**. 9-조건의 수학적 formal form + 6-부 composition 의 매핑 + canonical entry draft (§N) + empirical validation requirements + 4 counterexample attempts + honest assessment 를 포함.

**핵심 메시지**:
- T 는 관찰자-개인 P (ξ resident); 9 conditions 는 T 위 axioms (A on P) — 9 × Cat A
- 6-부 composition (Cat C SKETCH) 은 9-axioms 의 *constructive instance* — *별개 Cat*
- Canonical entry §N 은 *axiomatic declaration*, mathematical proof 아님
- OP-AUX-T-FIXED-POINT (9-axioms simultaneous satisfiability) 는 OPEN — W10+

**Phase 4 commit turn 의 책임**:
- canonical.md Appendix OMS §N 신설
- theorem_status.md Cat A 카탈로그 + Open Problems 등록
- THEORY/CHANGELOG.md CV-1.18 entry

본 D5 자체는 **canonical 0 edits** — Phase 4 hand-off 만.

---

*End of P5_Stage0_sensor_T_9conditions.md. D5 Opus, 2026-05-19 W8-Day2. Cat verdict: 9 × Cat A on P + 6-part Cat C SKETCH. Entry status: DRAFT ready for CV-1.18 SEAL turn. Canonical edits: 0.*
