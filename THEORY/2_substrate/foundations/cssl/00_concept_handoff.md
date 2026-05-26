---
type: working/cssl/concept-handoff
date: 2026-05-20
session_origin: W8-Day3 evening (post-EOD, user-initiated new direction)
canonical_version: CV-1.18 (SEALED untouched)
status: concept-handoff (user-prepared full document); awaiting critic agent evaluation + Cat assignment
authors: user (Jaehong Oh)
preceded_by:
  - W8-Day3 02_cg_numerical_verification.md (S1 Cat B verified)
  - W8-Day3 03_D_L_commutation.md (S3 Cat A on standard regimes + Case C §6 NEW L-INV-1/L-INV-2/L-INV-3)
  - W8-Day3 99_summary.md (Decision A: CV-1.19 SEAL-prep candidate for S1 + S3)
  - W7-Day5 CV-1.16 SEAL (L-HMORSE-LOCAL Cat B, D-HMORSE-LOCAL active-set form)
context_in_canonical:
  - canonical §13 L-HMORSE-LOCAL (Cat B, CV-1.16) — active-set form (C1)(C2′)(C3)(C4)(C5)
  - canonical §13 L-HMORSE-DECOMP (Cat B conditional, CV-1.16) — Schur complement decomposition
  - canonical §13 L-BOUNDARY-MODE-EXCLUSION (Cat C, CV-1.16) — boundary modes
  - canonical §13 T-σ-Lemma-1 (Cat A) — Hessian commutes with G_u action
  - canonical §3.7 §9.3 — Distinction operator + candidate
  - canonical §13 T-V5b-T-zero (Cat A) — Goldstone exact zero on translation-invariant graphs
problem_statement: |
  Existing H-Morse analysis at non-uniform critical points decomposes Hessian into bulk (B) / active (A) / exterior (E) blocks and seeks Goldstone-only nondegeneracy on the effective active-set Hessian H_eff^{AA}. The user's new proposal: instead of requiring ker H_eff^{AA} = Goldstone subspace, allow ker H_eff^{AA} = Goldstone ⊕ E_surg at isolated topology-changing moments (split/merge/birth/death), with E_surg = finite-dimensional surgery event subspace. Wild degeneracy (non-Goldstone, non-surgery) must still be excluded.
proposal_name: Critical Skeleton Surgery Layer (CSSL)
key_themes:
  - shape regularity ≠ spectral non-degeneracy
  - damping/viscosity addresses dynamics, not Hessian curvature
  - surface tension scaling (α, β) → (sα, sβ) preserves T8 + boundary width, increases σ
  - no external "operation mode" — singular skeleton must arise intrinsically from energy landscape
  - tame vs wild singularity distinction
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§3.7, §9.3, §13 L-HMORSE-LOCAL/DECOMP/BOUNDARY-MODE-EXCLUSION, T-σ-Lemma-1, T-V5b-T-zero) · [[../foundation/manifold_topology_attempt_v1|v1 master synthesis]] · [[../../logs/daily/2026-05-20/03_D_L_commutation|W8-Day3 03 [D, L_G] Case C derivation]] · [[../../logs/daily/2026-05-20/99_summary|W8-Day3 99 summary §"Carry-Forward"]]

# Critical Skeleton Surgery Layer (CSSL) — Concept Handoff Document

**Origin**: 2026-05-20 W8-Day3 evening, user-prepared full conceptual proposal (post W8-Day3 EOD). Goal: organize narrative of *where the idea started, what intuition drove it, and how the existing H-Morse problem is being reconstructed at a different layer*, in a form ready for agent-handoff.

---

## 비-uniform critical의 H-Morse 문제에서 Critical Skeleton Surgery Layer로 가는 아이디어

### 0. 배경: 현재 문제의 출발점

현재 SCC/formation 이론에서 비-uniform critical point $u^*$ 는 formation regime에서 나타나는 공간적으로 비균질한 critical point이다. 이는 $u_i^* \neq c$인 site들이 생기며, 하나의 응집된 formation이 bulk, boundary, exterior의 구조를 갖는 상태다. 기존 정리에 따르면 이 구조는 대략 다음과 같다.

```
[exterior, u≈0] [active boundary band, 0<u<1] [bulk, u≈1] [active boundary band] [exterior, u≈0]
```

즉 형상은 발산하거나 spike처럼 튀는 것이 아니라, Allen-Cahn / Modica-Mortola류의 phase-field처럼 **부드러운 diffuse interface**를 가진다. boundary 폭은 대략

$$\ell_{\mathrm{bd}} \sim \sqrt{\alpha/\beta}$$

로 이해된다.

기존 H-Morse 분석의 핵심은 전체 Hessian을 직접 보지 않고, saturated 영역인 bulk/exterior를 제거한 뒤 active boundary band 위의 Schur complement를 보는 것이다. 메모에서도 Hessian은 bulk (B), active (A), exterior (E)로 block decomposition되고, 실제 Morse 분석 대상은 effective active-set Hessian

$$H_{\mathrm{eff}}^{AA}$$

라고 정리되어 있다.

기존 목표는 다음과 같다.

$$\ker H_{\mathrm{eff}}^{AA} = \text{Goldstone subspace only}$$

즉 translation, rotation, mass conservation, formation permutation 같은 정당한 zero mode 외에는 추가 퇴화가 없어야 한다.

---

## 1. 처음 떠오른 직관: "형상이 부드러운데 왜 문제가 되는가?"

처음 의문은 이것이었다.

> 비-uniform critical의 boundary가 부드러운 diffuse interface라면, 대체 무엇이 문제인가?

여기서 중요한 구분이 생겼다.

$$\text{shape regularity} \neq \text{spectral non-degeneracy}$$

즉 boundary가 매끈하다는 것과 Hessian이 Morse-nondegenerate하다는 것은 다른 문제다.

부드러운 boundary는 오히려 여러 작은 변형 모드를 갖는다.

예를 들어:

```
1. formation 전체가 조금 이동하는 mode
2. boundary가 살짝 출렁이는 wobble mode
3. neck이 열리거나 닫히는 mode
4. 두 formation이 merge/split되는 mode
5. mass constraint에 의해 전체 높이가 조정되는 mode
```

이 중 translation 같은 것은 정당한 Goldstone mode다. 하지만 Goldstone도 아니고 위상 사건도 아닌데 Hessian eigenvalue가 0 또는 near-zero라면, formation identity가 불안정해진다.

따라서 기존 H-Morse 문제는 다음과 같이 이해된다.

> 경계가 예쁘게 생겼는지가 문제가 아니라, 그 경계가 흔들릴 때 에너지가 확실히 증가하는지가 문제다.

즉 문제는 geometry의 매끄러움이 아니라 spectral degeneracy다.

---

## 2. 첫 번째 해결 직관: "점도나 damping을 높이면 되는가?"

다음으로 떠오른 직관은:

> 동점성/점도를 높이면 boundary wobble이 줄지 않을까?

하지만 여기서도 구분이 필요하다.

동역학적 점도 또는 damping을 높이는 것은 gradient flow의 시간 응답을 느리게 만든다.

예를 들어 $\eta \dot u = -\nabla E(u)$ 에서 $\eta$를 키우면 변화 속도는 느려진다. 또는 $\partial_t u = -\nabla E(u) + \nu \Delta u$ 처럼 동점성적 smoothing을 넣으면 wobble이 시간적으로 안정된다.

하지만 이것은 critical point의 Hessian 자체를 바꾸지 않는다.

$$H(u^*)=\nabla^2 E(u^*)$$

따라서 extra degeneracy가 존재한다면 damping은 그것을 제거하지 못한다. 단지 "평평한 지형 위에서 천천히 미끄러지게" 만들 뿐이다.

결론:

> 동점성 증가는 수치 안정화에는 유용하지만, H-Morse non-degeneracy의 본질적 해결은 아니다.

필요한 것은 dynamics의 damping이 아니라 **energy landscape의 curvature를 바꾸는 것**이다.

---

## 3. 두 번째 해결 직관: "에너지 지형의 곡률을 바꾸면 되는가?"

다음으로 나온 생각은:

> 그렇다면 $H_{\mathrm{eff}}^{AA}$의 Goldstone-orthogonal spectral gap을 직접 키우면 되는가?

즉 목표는 다음이다.

$$\lambda_{\min}^{\perp}\left(H_{\mathrm{eff}}^{AA}\right) \ge c_{\mathrm{gap}}>0$$

여기서 $\perp$는 Goldstone mode를 제외한 방향이다.

### 3.1 Smoothness 계수 $\alpha$ 증가

기본 smoothness 항이 $E_{\mathrm{smooth}} = \alpha \sum_{(i,j)}(u_i-u_j)^2$ 라면 $\alpha$를 키우면 boundary wobble이 줄어들 수 있다. 하지만 formation 발생 조건이 대략 $\beta/\alpha > 4\lambda_2(L_G)/\lvert W''(c) \rvert$ 형태라서 $\alpha$만 키우면 $\beta/\alpha$가 줄어들어 T8 formation emergence 자체가 약해질 수 있다. 즉 $\alpha$ 증가는 boundary를 안정화하지만, 동시에 formation의 자연 발생을 죽일 수 있다.

### 3.2 계면장력 surface tension 증가

> 작동 모드를 따로 만들지 말고, 자연스럽게 뭉치는 구조는 유지하되 계면장력만 늘릴 수 없을까?

Allen-Cahn류 scaling에서 boundary 폭은 $\ell_{\mathrm{bd}}\sim \sqrt{\alpha/\beta}$이고, 계면장력은 대략 $\sigma \sim \sqrt{\alpha\beta}$로 이해할 수 있다. 그러면 $\alpha$와 $\beta$를 동시에 같은 비율로 키우는 방법이 있다.

$$(\alpha,\beta) \mapsto (s\alpha,s\beta)$$

이 경우 $\beta/\alpha$는 유지, $\sqrt{\alpha/\beta}$도 유지, 하지만 $\sqrt{\alpha\beta} \mapsto s\sqrt{\alpha\beta}$이므로 계면장력은 증가한다.

> T8 발생 조건과 boundary 폭은 보존하면서, 형성된 경계의 surface tension만 키울 수 있다.

즉 객체는 여전히 자연스럽게 뭉치지만, 경계는 더 단단해진다.

---

## 4. 세 번째 직관: "작동 모드는 따로 있으면 안 된다"

여기서 중요한 철학적 조건이 확인되었다.

> formation을 위해 별도의 작동 모드나 switch가 있으면 안 된다.

왜냐하면 SCC의 핵심은 객체가 외부 명령으로 label되는 것이 아니라, soft cohesion field의 자기조직화로 자연 발생한다는 데 있기 때문이다.

나쁜 방식: "if boundary mode then turn on sharpening"
좋은 방식: $E(u)$ 자체의 물성으로부터 boundary sharpening/surface tension이 자연 발생

즉 boundary 안정화는 외부 controller가 아니라, 에너지 함수 내부의 intrinsic material property여야 한다.

---

## 5. 네 번째 직관: "임계항으로 boundary를 더 뾰족하게 만들 수 있는가?"

그다음 나온 아이디어는:

> local boundary에서 일부러 critical wall을 만들어, diffuse boundary를 더 날카롭게 만들 수 있지 않을까?

이것은 단순 계면장력 증가와 다르다. 수학적으로는 $\ell_{\mathrm{bd}} \sim \sqrt{\alpha/\beta}$이므로 $\beta/\alpha$를 키우면 boundary가 얇아진다. 하지만 너무 날카롭게 만들면 위험하다.

```
너무 넓은 boundary:        너무 얇은 boundary:
- 객체 경계가 흐림         - binary segmentation으로 퇴화
- wobble mode가 많음       - lattice pinning
                           - singular perturbation
                           - soft cohesion 철학 훼손
```

따라서 목표는 "그냥 뾰족하게"가 아니라 **controlled sharp-interface regime** 이어야 한다.

---

## 6. 핵심 전환: "특이점/특이선을 일부러 만들고 위상 수술을 하면 어떨까?"

최종적으로 나온 가장 중요한 직관은 이것이다.

> boundary를 무조건 매끄럽게 안정화하는 대신, 일부러 제어된 특이점/특이선을 만들고, 그 특이 구조를 대상으로 위상적 surgery를 수행하면 어떨까?

이것은 이전 아이디어들과 질적으로 다르다.

기존 H-Morse 접근은 모든 non-Goldstone degeneracy를 제거하려고 했다.

$$\ker H_{\mathrm{eff}}^{AA} = \mathcal{G}$$

하지만 새로운 아이디어는 일부 degeneracy를 제거 대상이 아니라 **위상 사건의 문법**으로 본다.

$$\ker H_{\mathrm{eff}}^{AA} = \mathcal{G} \oplus \mathcal{E}_{\mathrm{surg}}$$

여기서 $\mathcal{G}$ = Goldstone subspace, $\mathcal{E}_{\mathrm{surg}}$ = split/merge/birth/death 같은 topology-changing event subspace.

> 모든 extra degeneracy가 나쁜 것이 아니다. 어떤 degeneracy는 객체가 자기 위상을 바꾸는 순간이다.

---

## 7. 왜 특이점이 필요한가?

객체의 위상 변화는 매끈한 안정 상태만으로 설명하기 어렵다.

```
merge event:
before:    ○     ○
neck:      ○──●──○         (● = neck saddle = index-1 critical point)
after:     ███████

split event:
before:    ███████
neck:      ○──●──○
after:     ○     ○
```

birth/death/split/merge 같은 사건에는 어떤 형태의 critical event가 필요하다. 따라서:

> 평상시에는 H-Morse stable phase를 유지하고, 위상 변화 순간에는 controlled singular skeleton을 통해 surgery를 수행한다.

---

## 8. 제안하는 새 층위: Critical Skeleton Surgery Layer (CSSL)

$$\boxed{\text{Critical Skeleton Surgery Layer, CSSL}}$$

이 층위의 역할:

```
soft cohesion field → formation → active boundary → critical skeleton → topological surgery → identity transition
```

즉 기존 SCC가 formation의 자연 발생을 설명했다면, CSSL은 formation의 **위상 변화와 identity transition**을 설명한다.

---

## 9. Critical Skeleton 정의의 방향

기본 field는 여전히 $u:X\to[0,1]$이다. 중요한 점은 $u$ 자체를 wild하게 singular하게 만들지 않는 것이다. 대신 $u$에서 파생된 ridge/skeleton 구조를 읽는다.

### 9.1 Active boundary band

$$A(u) = \{i\in V:\delta<u_i<1-\delta\}$$

### 9.2 Boundary ridge density

$$r_i(u) = \sum_{j\sim i} w_{ij}(u_i-u_j)^2$$

이 값은 $u$가 급격히 변하는 곳에서 커진다.

### 9.3 Ridge set

$$\mathcal{R}(u) = \{i\in A(u): r_i(u)\ge r_j(u)\text{ for nearby }j\}$$

### 9.4 Critical skeleton

$$\mathcal{S}(u) = \{i\in\mathcal{R}(u): i\text{ is a ridge-critical point and induces local topology change}\}$$

가능한 skeleton type:
1. index-0 nucleation point: birth
2. index-1 neck saddle: split/merge
3. ridge junction: multiple formation interaction
4. cusp/pinch point: boundary surgery
5. loop saddle: hole birth/death

---

## 10. Tame singularity vs wild singularity

> 특이점은 허용하되, 모든 특이점을 허용하면 안 된다.

**허용** (tame): finite-index Morse saddle, neck point, controlled cusp, ridge junction, persistent topology event, split/merge에 대응하는 critical point

**금지** (wild): random spike, lattice-scale checkerboard, fractal boundary, non-persistent topological noise, unbounded curvature blow-up, numerical artifact

### Definition: Tame Singularity

점 $i\in\mathcal{S}(u)$가 tame singularity라는 것은 다음을 만족한다.
1. local critical index가 유한하다.
2. local topology change가 persistent homology 변화와 대응한다.
3. curvature concentration이 bounded다.
4. lattice-scale oscillation이 아니다.
5. 사건 이후 formation이 다시 H-Morse stable phase로 돌아간다.
6. 해당 singularity는 finite-dimensional surgery event subspace를 만든다.

---

## 11. Surgery-admissible critical point

기존 stable phase: $\ker H_{\mathrm{eff}}^{AA} = \mathcal{G}$

surgery event phase: $\ker H_{\mathrm{eff}}^{AA} = \mathcal{G} \oplus \mathcal{E}_{\mathrm{surg}}$

여기서 $\mathcal{E}_{\mathrm{surg}}$는 finite-dimensional surgery event subspace다.

| Event | Surgery mode |
|---|---|
| birth | nucleation mode |
| death | collapse mode |
| merge | neck-closing mode |
| split | neck-opening mode |
| hole birth | loop-opening mode |
| hole death | loop-closing mode |

금지: $\ker H_{\mathrm{eff}}^{AA} \supsetneq \mathcal{G} \oplus \mathcal{E}_{\mathrm{surg}}$ (Goldstone도 아니고 surgery event도 아닌 추가 degeneracy).

---

## 12. 에너지 설계 방향

$$E_{\mathrm{CSSL}}(u) = E_{\mathrm{SCC}}(u) + \kappa E_{\mathrm{ridge}}(u) + \eta E_{\mathrm{wild}}(u) + \zeta E_{\mathrm{pers}}(u)$$

### 12.1 Ridge concentration term

$$E_{\mathrm{ridge}}(u) = -\sum_i \phi(r_i(u))$$

$\phi$는 bounded saturating function (예: $\phi(r)=r/(1+r)$ 또는 $\phi(r)=1-e^{-r/\tau}$). 역할: boundary ridge를 어느 정도 명확하게 만든다. 하지만 무한 spike로 발산하지 않게 한다.

### 12.2 Wild singularity penalty

$$E_{\mathrm{wild}}(u) = \sum_i(\Delta_G u_i)^2$$

또는 더 강하게 $\sum_i\vert \Delta_G^2 u_i\vert ^2$. 역할: checkerboard instability, lattice spike, fractal boundary를 억제한다.

### 12.3 Persistence filter

$$E_{\mathrm{pers}}(u) = \text{penalty for low-persistence topological noise}$$

역할: 짧게 생겼다 사라지는 의미 없는 topology noise를 제거한다. persistent한 skeleton event만 남긴다.

---

## 13. 사건 판정 알고리즘

### Step 1. Field evolution
$$u_{t+1} = u_t - \eta_t\nabla E_{\mathrm{CSSL}}(u_t)$$

### Step 2. Active boundary 추출
$$A_t=\{i:\delta<u_i(t)<1-\delta\}$$

### Step 3. Ridge density 계산
$$r_i(t)=\sum_{j\sim i}w_{ij}(u_i(t)-u_j(t))^2$$

### Step 4. Critical skeleton 후보 추출
$$\mathcal{S}_t = \text{local ridge-critical points inside }A_t$$

### Step 5. Persistent homology 계산
threshold filtration $X_\theta(t) = \{i:u_i(t)\ge\theta\}$에 대해 $H_0, H_1$ barcode를 추적한다.

### Step 6. Surgery event 판정
- $H_0$ component count increases: birth or split
- $H_0$ component count decreases: merge or death
- $H_1$ appears: hole birth
- $H_1$ disappears: hole death

### Step 7. Hessian eigenmode alignment 확인
event 근처에서 near-zero eigenvector $v_{\mathrm{nz}}$를 구하고, skeleton event direction $v_{\mathrm{surg}}$와 비교한다. $\langle v_{\mathrm{nz}}, v_{\mathrm{surg}}\rangle \approx 1$이면 tame surgery event. 그렇지 않으면 wild degeneracy.

---

## 14. 주요 정리 후보

### Theorem 1. Morse–Surgery Dichotomy (T-MORSE-SURGERY-DICHOTOMY)

**Statement.** Tame skeleton regularization을 갖는 SCC trajectory에서, 거의 모든 시간의 formation boundary는 H-Morse stable하다.

$$\ker H_{\mathrm{eff}}^{AA}(u_t)=\mathcal{G}(u_t)$$

위상 변화가 일어나는 고립된 시간 $t_k$에서만

$$\ker H_{\mathrm{eff}}^{AA}(u_{t_k}) = \mathcal{G}(u_{t_k}) \oplus \mathcal{E}_{\mathrm{surg}}(u_{t_k})$$

가 된다.

> 객체는 대부분의 시간 동안 안정적이고, split/merge/birth/death는 고립된 surgery event로만 일어난다.

### Theorem 2. Skeleton–Persistence Correspondence (T-SKELETON-PERSISTENCE-CORRESPONDENCE)

**Statement.** Tame singular boundary 조건 아래에서 critical skeleton event는 persistent homology barcode의 birth/death/merge/split event와 대응한다.

$$s\in\mathcal{S}(u) \quad\longleftrightarrow\quad \Delta H_k(u)$$

| Skeleton event | PH event |
|---|---|
| index-0 nucleation | $H_0$ birth |
| index-1 neck saddle | $H_0$ merge/split |
| loop saddle | $H_1$ birth |
| cap collapse | $H_1$ death |

### Theorem 3. Wild Degeneracy Exclusion (T-WILD-DEGENERACY-EXCLUSION)

**Statement.** $E_{\mathrm{wild}}$가 충분히 강하고 $E_{\mathrm{ridge}}$가 bounded saturating 형태이면, lattice-scale spike, checkerboard singularity, non-persistent topological artifact는 bounded-energy critical point로 남을 수 없다.

> 제어된 특이성만 살아남고, 의미 없는 특이점은 제거된다.

### Theorem 4. Surgery-Admissible H-Morse Extension (T-SURGERY-ADMISSIBLE-HMORSE)

**Statement.** 비-uniform critical $u^*$가 surgery-admissible하면, active-set Hessian의 kernel은 Goldstone subspace와 finite-dimensional surgery event subspace로 정확히 분해된다.

$$\ker H_{\mathrm{eff}}^{AA} = \mathcal{G} \oplus \mathcal{E}_{\mathrm{surg}}$$

그리고 Goldstone 및 surgery direction을 제외한 보공간에서는 spectral gap이 존재한다.

$$\lambda_{\min}^{\perp(\mathcal{G}\oplus\mathcal{E}_{\mathrm{surg}})}\left(H_{\mathrm{eff}}^{AA}\right) > 0$$

---

## 15. 철학적 의미

기존 H-Morse 관점에서는 formation이 안정적으로 존재하려면 모든 non-Goldstone degeneracy가 제거되어야 했다.

하지만 객체가 진짜로 생성되고, 합쳐지고, 갈라지고, 사라지는 존재라면, 어떤 순간에는 반드시 위상 변화가 필요하다. 그리고 위상 변화는 보통 critical event를 요구한다.

> 특이점은 객체가 자기 경계를 다시 쓰는 순간이다.

기존 구조:
$$\text{soft cohesion} \rightarrow \text{formation} \rightarrow \text{boundary}$$

새 구조:
$$\text{soft cohesion} \rightarrow \text{formation} \rightarrow \text{boundary} \rightarrow \text{critical skeleton} \rightarrow \text{surgery} \rightarrow \text{identity transition}$$

즉 객체는 단순히 경계를 가진 덩어리가 아니다. 객체는 자신의 경계 안에 스스로를 나누거나, 붙이거나, 소멸시키는 **위상적 절개선**을 잠재적으로 품고 있다.

---

## 16. 에이전트 검토 방향

### A. 기존 H-Morse framework와의 충돌
1. 기존 L-HMORSE-LOCAL 조건을 어떻게 수정해야 하는가?
2. Goldstone-only kernel 조건을 Goldstone ⊕ Surgery kernel 조건으로 확장할 수 있는가?
3. surgery event가 없는 구간에서는 기존 H-Morse 조건을 그대로 회복할 수 있는가?

### B. Critical skeleton 정의의 수학적 안정성
1. $r_i(u)=\sum_j w_{ij}(u_i-u_j)^2$ 기반 ridge density가 충분한가?
2. graph Morse index를 어떻게 정의할 것인가?
3. ridge-critical point와 PH barcode event의 대응이 성립하는가?
4. discrete graph에서 saddle/neck을 안정적으로 판정할 수 있는가?

### C. Tame vs wild singularity 구분
1. bounded curvature concentration 조건을 어떻게 쓸 것인가?
2. lattice-scale spike를 배제하는 충분조건은 무엇인가?
3. low-persistence topology noise를 어떻게 제거할 것인가?
4. tame singularity의 finite-index 조건은 discrete setting에서 어떻게 표현되는가?

### D. Energy design의 well-posed성
1. $E_{\mathrm{ridge}} = -\sum \phi(r_i)$가 ill-posed하지 않은가?
2. $\phi$가 bounded saturating이면 ridge concentration과 coercivity를 동시에 만족하는가?
3. $E_{\mathrm{wild}} = \sum(\Delta_G u_i)^2$가 ridge 자체까지 과도하게 죽이지 않는가?
4. $E_{\mathrm{pers}}$ 같은 PH 기반 항을 에너지에 직접 넣는 것이 가능한가, 아니면 diagnostic으로만 써야 하는가?

### E. Surgery event subspace 정의
1. neck-closing/opening mode를 eigenvector로 정의할 수 있는가?
2. near-zero Hessian eigenvector와 PH event direction의 alignment를 어떻게 측정할 것인가?
3. $E_{\mathrm{surg}}$가 finite-dimensional임을 보일 수 있는가?
4. event 이후 H-Morse stable phase로 복귀하는 조건은 무엇인가?

---

## 17. 가장 중요한 요약

이 아이디어는 단순히 boundary를 더 뾰족하게 만들자는 것이 아니다.

> 비-uniform critical의 active boundary band에서 발생하는 non-Goldstone degeneracy를 전부 제거하지 말고, 그중 일부를 split/merge/birth/death에 대응하는 controlled singular skeleton event로 분류하자. 평상시에는 H-Morse stable phase를 유지하고, 위상 변화 순간에는 finite-index tame singularity를 통해 topological surgery를 수행하게 하자.

수식적으로:

$$\ker H_{\mathrm{eff}}^{AA} = \mathcal{G} \quad \text{(stable phase)}$$

$$\ker H_{\mathrm{eff}}^{AA} = \mathcal{G} \oplus \mathcal{E}_{\mathrm{surg}} \quad \text{(surgery phase)}$$

금지: $\ker H_{\mathrm{eff}}^{AA} \supsetneq \mathcal{G} \oplus \mathcal{E}_{\mathrm{surg}}$ (Goldstone도 아니고 surgery event도 아닌 wild degeneracy).

---

## 18. Agent prompt (handoff target)

For the critic / general-purpose agent. Self-contained prompt:

```text
You are auditing and extending a theoretical framework called SCC (Soft Cognitive Cohesion), where objects emerge as non-uniform critical points of a soft cohesion field u: X -> [0,1]. The current H-Morse analysis decomposes a non-uniform critical point u* into bulk B, active boundary band A, and exterior E. Bulk/exterior are saturated and strictly positive in the Hessian, so the real Morse problem is reduced via Schur complement to the effective active-set Hessian H_eff^{AA}. The existing goal is Goldstone-only nondegeneracy:

    ker H_eff^{AA} = Goldstone subspace.

However, I want you to rethink this. My intuition is that not every non-Goldstone degeneracy should be treated as bad. Some degeneracies may be the actual grammar of object topology change: birth, death, split, merge, hole creation, and hole destruction. Instead of only increasing surface tension or sharpening the boundary, consider a new layer:

    Critical Skeleton Surgery Layer (CSSL)

The idea is to allow controlled singular points/lines inside the active boundary band, not as random noise, but as finite-index tame singularities that correspond to topological surgery events. In stable phases, the old H-Morse condition should hold:

    ker H_eff^{AA} = G

where G is the Goldstone subspace. But at surgery events, we allow

    ker H_eff^{AA} = G ⊕ E_surg

where E_surg is a finite-dimensional surgery event subspace corresponding to a critical skeleton event such as neck-opening, neck-closing, nucleation, collapse, loop opening, or loop closing. What must still be excluded is wild degeneracy:

    ker H_eff^{AA} strictly larger than G ⊕ E_surg.

Please deeply analyze this proposal.

Tasks:
1. Formalize the conceptual transition: Goldstone-only H-Morse nondegeneracy → surgery-admissible H-Morse nondegeneracy.
2. Define a possible critical skeleton S(u) inside the active boundary band A(u). Suggested ingredients: A(u)={i:δ<u_i<1-δ}, r_i(u)=Σ_{j~i}w_ij(u_i-u_j)^2, ridge set R(u)=local maxima of r_i inside A(u), critical skeleton S(u)=ridge-critical points that induce local topology change.
3. Distinguish tame singularities from wild singularities.
4. Propose an energy design: E_CSSL(u) = E_SCC(u) + κ·E_ridge(u) + η·E_wild(u) + ζ·E_pers(u). Check well-posedness and preservation of natural formation emergence.
5. Propose theorem candidates: T-MORSE-SURGERY-DICHOTOMY, T-SKELETON-PERSISTENCE-CORRESPONDENCE, T-WILD-DEGENERACY-EXCLUSION, T-SURGERY-ADMISSIBLE-HMORSE.
6. Identify the main mathematical risks: ridge concentration → spike formation? PH events differentiable? graph Morse index robustness? neck saddle vs numerical artifact? contradicts soft-cohesion ontology? becomes segmentation/free-boundary theory?
7. Give a recommended canonical version: which parts are Cat A candidates / Cat B conditional / Cat C numerical / open problems?

Key constraint: Objects should still emerge naturally from the cohesion field. There must be no external "operation mode." The singular skeleton must arise intrinsically from the energy landscape and should serve as the grammar of object identity transition, not as a manually triggered procedure.
```
