---
type: working/proofs
task: P6 — OMS-1 ξ catalog T_* formal entry (Cat A axiomatic registration)
date: 2026-05-19
session: W8-Day2
author: D6 (Sonnet, executor)
input: E3_hmorse_stage0_oms.md §C + 03_T_star_fixed_point.md §5
canonical_version: CV-1.17 (read-only; amendments drafted only)
status: COMPLETE (draft amendments prepared; canonical edit 후속 결정 필요)
cat_verdict: Cat A axiomatic (ξ resident 정식 등록) — mathematical proof 아님
cot_enforced: yes
coc_enforced: yes
---

> [!nav] Linked: [[canonical|canonical.md (CV-1.17)]] · [[auxiliary_structures_master|AUX-1.5]] · [[03_T_star_fixed_point]] · [[E3_hmorse_stage0_oms]]

# P6 — OMS-1 ξ Catalog T_* Formal Entry (Cat A Axiomatic Registration)

**Mission**: OMS-1 의 $\Theta = (q, \lambda, \xi)$ framework 에서 $T_*$ 를 ξ resident 로
*정식 등록(formal entry)*. 03_T_star §5 Route C G1+G3 hybrid formalization 의
canonical promotion 준비 문서.

**Non-Overclaim 선언 (§7.2 에서 상세)**:

- 본 문서는 *axiomatic declaration* 이다. $T_*$ 의 *mathematical proof* 가 아니다.
- Brouwer existence (Cat A 후보, §2.3 L1-L3 sketch) 는 *검증 필요 미완성*.
- Uniqueness 는 OPEN (OP-T*-α).
- Route A/B 폐기는 *제안* — canonical OP-0021 본문 별도 amendment turn 필요.
- canonical 에 대한 *실제 편집 없음* — §3, §8 의 amendment 는 draft 형식만.

---

## §0 Pre-work Xref + Frontmatter

### §0.1 직접 입력 문서 확인

```
CoC anchor E3 §C: E3_hmorse_stage0_oms.md §C (§C.1-§C.4)
  → §C.1: 현재 ξ catalog 공백 상태 확인 (canonical.md L2416)
  → §C.2: ξ entry 6-field formal structure 제안
  → §C.3: T_* Route C + ξ resident coupling (B_{T_*}^{FP} ∩ B_ξ^{OMS-1})
  → §C.4: D6 권장 작업 순서 (amendment draft 4단계)

CoC anchor 03_T_star §5: 03_T_star_fixed_point.md §5
  → §5.1: Route C G1+G3 hybrid (T_* ∈ B_{FP} ∩ B_ξ + JND argmin)
  → §5.2: OP-0021 Route A/B 폐기 제안 (3-part silent OP resolution 회피)

CoC anchor canonical OMS-1: canonical.md L2416
  → Definition OMS-1: Θ = (q, λ, ξ); B_ξ "catch-all box" — 내용물 카탈로그 공백

CoC anchor AUX-1.5: auxiliary_structures_master.md
  → §4.7.1 (L471-488): ξ catalog seed (T_* 최상위 후보)
  → §4.6.1 (L371-378): Route A/B COB 위반 진단
  → §4.9.1 (L624-643): T_* fixed-point 순환 diagnosis + Route C 권장
```

### §0.2 기존 canonical 에서 T_* 위치 요약

- **canonical.md L2416**: OMS-1 Definition — $\xi \in B_\xi$ 선언, 내용물 미등록.
- **canonical.md L1670+**: T-PF-A1 family — $T_*$ 를 axiom parameter 로 처리
  (T-PF-A1-GI Cat A: Gibbs well-definedness; T-PF-A1-PE Cat A: Poincaré gap).
- **AUX-1.5 §4.7.1**: ξ catalog seed — $T_*$ 를 1번 항목으로 열거, canonical 미등록.
- **theorem_status.md**: OP-0021 (T_* registration) OPEN, Route C 권장 기록.

**CoT step**: canonical 에서 $T_*$ 는 axiomatic 어휘로만 존재하고, ξ resident 로서의
*정식 구조적 등록*이 부재함 → 본 P6 entry 가 그 *최초 formal form* 제공.

---

## §1 Statement (Cat A Axiomatic Registration Target)

### §1.1 OMS-1 $\Theta = (q, \lambda, \xi)$ Framework Recall

**Definition OMS-1 (canonical.md L2416, theorem-grade):**

$$\Theta = (q, \lambda, \xi) \;\in\; [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$$

- $q = \beta/\alpha$: spinodal ratio (명시 등록, T8 조건의 핵심 무차원수).
- $\lambda \in \Delta^3$: energy weights simplex $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}},
  \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$ (명시 등록).
- $\xi \in B_\xi$: 보조 박스 ("auxiliary box") — **내용물 카탈로그 현재 공백**.

Observer space $\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$
는 Tychonoff 에 의해 **compact** (canonical OMS-1, theorem-grade).

**CoT step**: $q$ 와 $\lambda$ 는 OMS-1 에서 *명시* 등록됨. $\xi$ 는 *컨테이너*만
선언되고 원소 목록이 비어있음. P6 의 과제는 이 컨테이너의 *첫 번째 공식 원소*($T_*$)
를 formal entry 형식으로 등록하는 것.

**CoC anchor**: canonical.md L2416 (Definition OMS-1 verbatim).

### §1.2 ξ Resident Category 의 Axiomatic 위상

OMS-1 framework 에서 $\xi$ 범주는 다음 위상을 갖는다:

1. **Observer-personal (P)**: 환경 통계나 $u_t$ 에서 수학적으로 결정되지 않는
   자유 매개변수.
2. **CN-COB 통과**: Closed Ontological Budget (AUX-1.5 §7) — 외생 통계 도입
   *없이* 관찰자-내부에서 정의 가능.
3. **축관적 자유 (G1)**: "정식 공리" 형태로 SCC 이론이 그 값을 *지정하지 않음*.
   관찰자의 선택 영역.
4. **비공허성 보장**: ξ category 가 공허한 선택을 *허용하지 않으려면*, 각 resident
   에 대해 valid range ($B_\xi$ 의 해당 성분) 가 비어있지 않아야 함.

$T_*$ 에 대해: Brouwer 1911 이 $B_{T_*}^{\mathrm{FP}} \neq \emptyset$ 를 보장
(03_T_star §2, Cat A 후보 sketch) — 관찰자의 선택이 *비공허*임을 수학적으로 뒷받침.

**CoT step**: ξ category 의 axiomatic 위상은 "수학적 결정 부재 + COB 통과 + 비공허
보장" 의 세 조건으로 특징지어짐. $T_*$ 가 세 조건을 모두 만족함 (§2 에서 상세).

**CoC anchor**: AUX-1.5 §7 (CN-COB); §4.7 (ξ catalog ); §4.9.1 (T_* P 분류).

### §1.3 T_* Entry Target Form

본 P6 가 목표하는 formal entry 의 형식:

$$\boxed{T_* \;\in\; \xi^{\mathrm{OMS-1}}, \qquad
T_* \;\in\; B_{T_*}^{\mathrm{FP}}(\Theta) \;\cap\; B_\xi^{\mathrm{OMS-1}}}$$

여기서:
- $\xi^{\mathrm{OMS-1}}$: OMS-1 ξ category (observer-personal resident 집합).
- $B_{T_*}^{\mathrm{FP}}(\Theta)$: fixed-point set $\{\,T \in [T_{\min}, T_{\max}] :
  \psi(T) = T\,\}$, $\Theta$ 의존 (Brouwer existence, §2).
- $B_\xi^{\mathrm{OMS-1}}$: ξ admissible range (관찰자 선택 가능 범위).

선택 criterion (Route C, G1+G3 hybrid):
$$T_* = \mathrm{argmin}_{T \in B_{T_*}^{\mathrm{FP}}(\Theta) \cap B_\xi^{\mathrm{OMS-1}}}
\rho_{\mathrm{JND}}(\Theta, T), \qquad
\rho_{\mathrm{JND}}(\Theta, T) := \frac{T}{\mathbb{E}_{\pi_T}[u]}$$

($\rho_{\mathrm{JND}}$: Weber-Fechner JND ratio, 03_T_star §5.1.)

**CoT step**: Entry target 은 T_* 의 *존재 보장* (Brouwer) + *observer-personal 위상*
(G1 축관적 자유) + *선택 ground* (G3 JND criterion) 의 삼중 구조. 이 삼중 구조가
§1.2 의 세 조건 (비공허/COB통과/자유) 과 일대일 대응.

### §1.4 Implication for OP-0021 (T_* Registration)

OP-0021 (theorem_status.md) 은 $T_*$ registration 을 OPEN 으로 등록하고
Route A (Mori-Zwanzig) + Route B (RG fixed point) 를 후보로 명시.

본 P6 entry 의 OP-0021 에 대한 함의:

- **Route C 채택 제안**: ξ resident formal entry 가 곧 *Route C (observer-personal)
  의 operational 형식*. Route C 채택 시 OP-0021 의 *scope 이 좁아짐* — "T_*
  mathematical derivation" → "ξ entry + Brouwer Cat A 승급 + uniqueness".
- **Route A/B 폐기 제안**: §5 에서 상세 분석. *OP 해결 아님* — OP-0021 은 여전히
  OPEN (scope 변경 + Route A/B 폐기 + Route C 채택이 남는 작업).
- **잔존 OPEN**: (a) Brouwer Cat A 승급 (L1 quantitative TV bound); (b) uniqueness
  (OP-T*-α); (c) canonical amendment 실행.

**CoT step**: OP-0021 에 대해 "해결" 이라고 주장하지 않음. Route C 채택 후에도
*mathematical substance* (Cat A proof + uniqueness) 는 여전히 미해결.

---

## §2 ξ Entry Formal Structure (6 Fields)

E3 §C.2 의 6-field formal structure 를 $T_*$ 에 적용.

### §2.1 Field 1 — Entry Name + Symbol

**이름**: $T_*$ (effective stochastic temperature, 유효 확률적 온도)

**기호**: $T_* \in \xi^{\mathrm{OMS-1}}$

**CoT step 1**: "Effective stochastic temperature" 라는 명칭이 canonical T-PF-A1
family (L1670+) 의 axiomatic 어휘와 일치. 새 어휘 도입 없음.

**CoT step 2**: $T_* \in \xi^{\mathrm{OMS-1}}$ 표기는 "OMS-1 의 ξ category 의 원소"
를 명시. AUX-1.5 §4.7.1 의 registry seed 표기 $T_*$ 와 일관.

**canonical 위치 (현재)**: canonical.md T-PF-A1 family (L1670+) — axiomatic
parameter 로 사용; OMS-1 $\xi$ 에 *미등록*.

**canonical 위치 (목표)**: Appendix OMS §A (L2416) amendment + §N 신설 entry.

**COB 상태**: COB 통과 (Route C: 관찰자-개인; 환경 외생 없음).

### §2.2 Field 2 — Position in SCC Pipeline

**1차 위치**: **Stage 5** (stochastic dynamics).

Stage 5 에서 $T_*$ 의 역할:
- **Gibbs measure**: $\pi_{T_*}(u) \propto \exp(-E(u)/T_*)$ — SCC field $u_t$ 의
  equilibrium 분포 parameter.
- **반사 Langevin SDE noise level**: $du = -\nabla E(u)\,dt + \sqrt{2T_*}\,dW_t +
  dL_t$ ($L_t$: 반사항, Lions-Sznitman 1984).
- **Poincaré gap**: $C_P \sim \exp(\mathrm{osc}(E)/T_*)$ — mixing time exponent.
- **Kramers exponent**: T-P-F-ε₀-K (Cat B) 의 escape rate.

**2차 위치**: **Stage 2** (energy) — $\pi_{T_*}$ 를 통해 에너지 함수 $E(u)$ 와 연결.

**CoT step**: Stage 5 가 $T_*$ 에 *직접 의존*하는 6개 이상의 canonical theorem 을
가짐 (T-PF-A1-GI, T-PF-A1-SDE, T-PF-A1-PE, T-K-Select-PF, T-K-Select-OBS,
T-P-F-ε₀-K). T_* 는 Stage 5 전체의 *공통 parameter* — pipeline 내 가장 광범위한
영향을 가진 ξ resident.

**CoC anchor**: canonical.md L1670+ (T-PF-A1-GI Cat A: Gibbs well-definedness),
L1703+ (T-PF-A1-PE Cat A: Poincaré gap), L1818+ (T-P-F-ε₀-K Cat B: Kramers).

**D5 와의 분리**: Stage 0 의 $T_{\mathrm{sensor}}$ (E3 §B, 6-부 composition)
와 $T_*$ (Stage 5) 는 *별개 개념*. $T_{\mathrm{sensor}}$ 는 raw → $u_t$ 변환의
sensor-level adaptation; $T_*$ 는 확률동역학의 noise level.
(SCC_unified_derivation_v0.1.md §2.5 CoT step 3 명시.)

단, **T-cond-7** (Stage 5, P-F-A1: T 연속) 이 $T_*$ well-posedness 의 *전제*:
D5 의 Stage 0 T 가 연속이어야 $\pi_{T_*}$ 가 well-defined (Lions-Sznitman) →
**D5 결과가 D6 의 전제 조건 중 하나** (E3 §D 교차참조).

### §2.3 Field 3 — Classification

**분류 코드**: P (관찰자-개인 stochastic resolution, ξ resident)

상세:

| 기준 | 분류 | 근거 |
|---|---|---|
| OMS-1 범주 | ξ resident | $B_\xi$ 내 observer-personal free parameter |
| COB 상태 | P (COB 통과) | 환경 통계 도입 없음, Route C |
| 수학적 결정 가능성 | P (axiomatically free) | G1: 이론이 값을 지정하지 않음 |
| 비공허 보장 | Cat A 후보 | Brouwer 1911 (§2 L1-L3 sketch) |
| 선택 criterion | G3 (JND) | Weber-Fechner $\rho_{\mathrm{JND}}$ minimizer |

**AUX-1.5 §4.9.1 최종 진단** (verbatim): "T_*는 *intrinsically* observer-side.
SDE의 noise level이 환경에서도, u에서도 유도되지 않는다. 관찰자가 어떤 *sampling
해상도*로 u를 관측하는가가 T_*. → P (observer-personal)가 자연."

**CoT step**: AUX-1.5 §4.6.1 (COB 위반 분석) + §4.9.1 (fixed-point diagnosis)
의 *registry-level* 결론 "P 분류 권장" 을 본 P6 가 *formal entry 형식으로 격상*.
Registry seed → formal entry 의 승급이지, 새로운 결론이 아님.

**CoC anchor**: AUX-1.5 §4.6.1 (Route A/B COB violation), §4.7.2 (Route C 권장),
§4.9.1 (T_* U → P 잠정 결론).

### §2.4 Field 4 — Range

**valid range (draft)**:

$$T_* \;\in\; B_{T_*}^{\mathrm{FP}}(\Theta) \;\cap\; B_\xi^{\mathrm{OMS-1}}$$

**$B_{T_*}^{\mathrm{FP}}(\Theta)$ (fixed-point set)**:

$$B_{T_*}^{\mathrm{FP}}(\Theta) := \{\,T \in [T_{\min}, T_{\max}] : \psi(T) = T\,\},
\qquad \psi(T) := \mathbb{E}_{\pi_T}\!\left[\,\lVert u - \mathbb{E}_{\pi_T}[u] \rVert^2\,\right]$$

- $T_{\min} := \min\{1, \inf\psi\}$, $T_{\max} := \max\{M_* + 1, \sup\psi\}$
  (03_T_star §1.2 B.2.2 선택).
- $M_* < \infty$: bounded polytope $\mathcal{F}_M(G)$ 위의 variance supremum.
- Brouwer 1911 → $B_{T_*}^{\mathrm{FP}} \neq \emptyset$ (Cat A 후보, 03_T_star §2).

**$B_\xi^{\mathrm{OMS-1}}$ (ξ admissible range)**:

- OMS-1 $B_\xi$ 의 $T_*$ 성분: observer 의 valid stochastic resolution range.
- *현재 canonical 에서 explicit 명시 부재* → **OP-OMS-1-ξ-2** (§9.2).
- 관찰자의 선택 영역: $B_{T_*}^{\mathrm{FP}}(\Theta)$ 내에서 JND criterion 기반 선택.

**CoT step 1**: $B_{T_*}^{\mathrm{FP}}$ 는 *수학적으로 결정 가능한* range
(Brouwer 에 의해 비공허). $B_\xi^{\mathrm{OMS-1}}$ 는 *관찰자 선택 영역*
(ξ category 에 의해 axiomatic 허용 범위).

**CoT step 2**: 교집합 $B_{T_*}^{\mathrm{FP}} \cap B_\xi^{\mathrm{OMS-1}}$ 가 비공허
→ Brouwer (존재) + OMS-1 framework consistency (허용) 의 결합.

**CoT step 3**: Multiplicity — multi-well $E$ (formation regime, T8 supercritical)
가 $|B_{T_*}^{\mathrm{FP}}| > 1$ 가능성. OP-T*-α (W9+) 에서 정량화.

**CoC anchor**: 03_T_star §1.2 (B.2.2: Brouwer existence), §1.3 (B.2.3: multiplicity
open), §5.1 (Route C formalization with intersection form).

### §2.5 Field 5 — OP Connections

| OP | 관계 | 현재 상태 | 본 P6 기여 |
|---|---|---|---|
| **OP-0021** | Primary — T_* registration | OPEN | Route C 채택 제안 draft; Route A/B 폐기 제안 (§5) |
| **OP-T*-FIXED-POINT** | 핵심 — Brouwer existence | 등록 권장 (AUX-1.5 §4.9.1) | 존재 Cat A 후보 경로 확인 (03_T_star §2 L1-L3) |
| **OP-T*-α** | 깊이 — multiplicity 정량화 | OPEN | 다중 fixed-point 가능성 명시 (§2.4 CoT 3) |
| **OP-OMS-1-ξ-1** | 확장 — 다른 ξ entries | 신규 (§9.1) | ξ catalog 시드 AUX-1.5 §4.7.1 forward hook |
| **OP-OMS-1-ξ-2** | 확장 — $B_\xi$ 명시 | 신규 (§9.2) | admissible range 미명시 확인 |
| **OP-OMS-1-ξ-3** | 확장 — cross-observer | 신규 (§9.3) | 관찰자 집단 변동성 |

**CoT step**: OP-T*-FIXED-POINT (존재), OP-T*-α (유일성), OP-0021 (등록) 는 계층 관계:
Brouwer 존재 → ξ 등록 → uniqueness. P6 는 중간 층 (ξ 등록) 을 진전.

### §2.6 Field 6 — Mathematical Role

$T_*$ 의 SCC 수학 구조 내 역할 (6개 canonical theorem 연결):

**역할 1 — Gibbs measure parameter** (T-PF-A1-GI, Cat A):
$$\pi_{T_*}(du) = Z(T_*)^{-1}\exp\!\bigl(-E(u)/T_*\bigr)\,d\sigma_M(u)$$
$\mathcal{F}_M(G)$ 위에서 well-defined. $T_* \to 0$: deterministic minimizer 집중.
$T_* \to \infty$: uniform distribution.

**역할 2 — Reflected Langevin SDE noise level** (T-PF-A1-SDE):
$$du_t = -\nabla E(u_t)\,dt + \sqrt{2T_*}\,dW_t + dL_t$$
$L_t$: 반사항 (Lions-Sznitman 1984, canonical Cat A). $T_*$ 가 클수록
탐색 광역성 증가.

**역할 3 — Variance map fixed-point** (P6 핵심 수학 기여):
$$\psi(T_*) = T_* \qquad \text{where} \quad \psi(T) = \mathbb{E}_{\pi_T}
\!\bigl[\,\lVert u - \mathbb{E}_{\pi_T}[u] \rVert^2\,\bigr]$$
자기-참조 순환의 해 — Brouwer 존재 보장, 유일성 미보장.

**역할 4 — Poincaré gap exponent** (T-PF-A1-PE, Cat A):
$$C_P \;\sim\; \frac{\pi^2}{n}\exp\!\Bigl(-\frac{\mathrm{osc}(E)}{T_*}\Bigr)$$
$T_*$ 가 작을수록 mixing time 지수적 증가 — formation metastability 정량화.

**역할 5 — Kramers escape rate** (T-P-F-ε₀-K, Cat B):
$T_*$ 와 saddle point 정보 결합 → escape rate. D4 (L-HMORSE-LOCAL Cat A 후보)
와 *병렬 해결 필요* (E3 §D "D4 Cat A + D6 ξ entry = Package II Cat B 의 두 기둥").

**역할 6 — Observer precision parameter** (Route C interpretation):
$\rho_{\mathrm{JND}} = T_*/\mathbb{E}_{\pi_{T_*}}[u]$ — 관찰자의 perceptual resolution.
Weber-Fechner JND (pre_brainstorm §5.4) 가 *selection criterion* 을 제공.

**CoT step**: 역할 1-5 는 *수학적* 역할 (canonical 기반). 역할 6 은 *해석적* 역할
(Route C 의 observer-personal framing). 수학적 역할은 Route A/B → Route C 전환
후에도 *변경되지 않음* (AUX-1.5 §4.7.2: "해석과 증명 책임만 변경 — Stage 5 전체의
*재해석*이지만 정리 카테고리 변경 없음").

**CoC anchor**: canonical T-PF-A1-GI (L1689), T-PF-A1-SDE (L1670+), T-PF-A1-PE
(L1703+), T-P-F-ε₀-K (L1818-1833), AUX-1.5 §4.7.2.

---

## §3 OMS-1 §A Amendment (Definition)

### §3.1 Current OMS-1 Definition (canonical §A, L2416)

**verbatim (canonical.md L2416)**:

> **Definition OMS-1 (Theorem-grade):** The SCC observer parameter vector is
> $\Theta = (q, \lambda, \xi)$ with $q = \beta/\alpha \in [q_{\min}, q_{\max}]$,
> $\lambda \in \Delta^3$ (energy weights, simplex), $\xi \in B_\xi$ (auxiliary box).
> The observer space $\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3
> \times B_\xi$ is **compact** (Tychonoff). The static face is
> $\Delta^2_{\mathrm{static}} = \{\lambda \in \Delta^3 : \lambda_{tr} = 0\}$.

**진단**: $\xi \in B_\xi$ 가 "auxiliary box" 로 선언되었지만 $B_\xi$ 의 원소 목록이
*공백*. E3 §C.1 + AUX-1.5 §4.7 진단과 동일.

### §3.2 Proposed Amendment (Draft — canonical edit 아님)

**Amendment target**: canonical.md L2416, Definition OMS-1 본문 끝에 추가.

**Draft amendment (verbatim)**:

> *[Amendment draft, P6, 2026-05-19]* The auxiliary box $B_\xi$ contains
> **observer-personal free parameters** under CN-COB (Closed Ontological Budget,
> AUX-1.5 §7). These parameters are axiomatically undetermined by the SCC theory
> and represent the observer's internal resolution choices. The ξ-catalog is
> maintained in **Appendix OMS §N** (below). First registered entry:
> **$T_*$ (effective stochastic temperature)** — see §N.1.

**Amendment 효과**:
- $B_\xi$ 의 *범주 선언* (axiomatically free, COB-passing) 추가.
- §N 으로의 forward hook 제공.
- 기존 compact/Tychonoff 내용 *변경 없음* (비침습적).

**CoT step**: Amendment 는 기존 내용을 *삭제하거나 수정하지 않고*, 빈 컨테이너에
*내용 설명과 전진 참조*를 추가함. 최소 canonical 변경 원칙.

### §3.3 Justification for §N 신설

E3 §C.4 권장 구조: "canonical.md Appendix OMS 의 §N 항목으로 ξ Catalog 삽입."

- §A–§M (Appendix OMS 기존 구조): OMS-2.0 Static/Temporal theorems.
- §N (신설 제안): "ξ Catalog — Observer-Personal Parameters"
  - §N.1: $T_*$ entry (본 P6 의 6-field form).
  - §N.2-§N.11: AUX-1.5 §4.7.1 시드 나머지 entries (stub 형식, forward hook).

---

## §4 Route C G1+G3 Hybrid Formalization (Canonical Entry)

03_T_star §5.1 의 Route C formalization 을 canonical promotion 형식으로 재정리.

### §4.1 G1 (Axiomatically Free P)

**G1 statement**:

$$T_* \;\in\; B_\xi^{\mathrm{OMS-1}} \qquad \text{(axiomatically free)}$$

$T_*$ 는 SCC 이론에 의해 *수학적으로 결정되지 않는다*.

**근거**:

- AUX-1.5 §4.6.1: Route A (Mori-Zwanzig) 와 Route B (RG fixed point) 가 모두
  COB 위반 → *어떤* external statistics 기반 derivation 도 SCC ontology 에서 적용
  불가.
- AUX-1.5 §4.9.1: "T_*는 *intrinsically* observer-side." — registry-level 결론.
- 03_T_star §1.4 (B.2.4): "SCC ontology under CN-COB excludes the environmental
  statistics needed for any *intrinsic* T_* definition."

**G1 의 의미**: G1 단독으로는 *너무 약함* — "어떤 T_* 도 허용" 이 되어 이론적
구속이 없음 (03_T_star §5.1 CoT step 1). G3 와의 결합이 필수.

**CoT step**: G1 는 $T_*$ 의 *부정 특성화* (환경 외생으로 결정될 수 없음) 를 제공.
$T_*$ 의 *긍정 특성화* (어디에 있어야 하는가) 는 G3 에서 제공.

### §4.2 G3 (Information-Theoretic Intersection)

**G3 statement**:

$$T_* \;\in\; B_{T_*}^{\mathrm{FP}}(\Theta), \qquad
B_{T_*}^{\mathrm{FP}}(\Theta) := \{\,T \in [T_{\min}, T_{\max}] : \psi(T) = T\,\}$$

$T_*$ 는 *self-consistency 조건* (variance map fixed-point) 을 만족해야 한다.

**self-consistency 해석**:
$T_*$ 가 Gibbs measure $\pi_{T_*}$ 를 결정 → $\pi_{T_*}$ 가 u 의 variance $\psi(T_*)$
를 결정 → 그 variance 가 다시 $T_*$ 와 일치해야 함. 이 순환이 observer 의 *내적
일관성* 조건 — 자신의 stochastic resolution 이 자신이 observe 하는 fluctuation 규모와
일치.

**G3 의 의미**: G3 만으로는 uniqueness 없음 (OP-T*-α — multi-well 시 다중 fixed-point).
그러나 *어디에서 선택해야 하는가*의 범위를 $B_{T_*}^{\mathrm{FP}}$ 로 제한.

**CoT step**: G3 의 self-consistency 조건은 *외부 환경 없이* 관찰자 내부에서 닫힌다
(Gibbs → variance → T_* → Gibbs). COB 통과. 단 fixed-point 개수 미결 → G1+G3
결합 후에도 uniqueness gap 은 남음.

**CoC anchor**: 03_T_star §1.2 (B.2.2 Brouwer, $B_{T_*}^{\mathrm{FP}}$ 정의),
§2 (L1-L3 sketch), §5.1 (G3 formalization).

### §4.3 Hybrid Form

$$\boxed{T_* = \mathrm{argmin}_{T \;\in\; B_{T_*}^{\mathrm{FP}}(\Theta) \cap
B_\xi^{\mathrm{OMS-1}}} \rho_{\mathrm{JND}}(\Theta, T)}$$

$$\rho_{\mathrm{JND}}(\Theta, T) = \frac{T}{\mathbb{E}_{\pi_T}[u]}
\qquad \text{(Weber-Fechner JND ratio)}$$

**해석**:
- 관찰자는 self-consistent fixed-point 의 집합 $B_{T_*}^{\mathrm{FP}}$ 에서,
  ξ admissible range $B_\xi^{\mathrm{OMS-1}}$ 와의 교집합 내에서,
  자신의 JND ratio 를 최소화하는 $T_*$ 를 선택한다.
- $\rho_{\mathrm{JND}} = T/\mathbb{E}[u]$ 는 noise-to-signal ratio 의 일종:
  작을수록 관찰자의 perceptual resolution 이 높음 (Weber-Fechner 해석).
- 따라서 argmin: 관찰자는 *가장 세밀한 resolution* 을 주는 fixed-point 선택.

**CoT step**: Hybrid form 이 G1+G3 를 모두 포함:
- G1: 선택 공간이 $B_\xi^{\mathrm{OMS-1}}$ (axiomatically free range).
- G3: 선택 공간을 $B_{T_*}^{\mathrm{FP}}$ 로 추가 제한 (self-consistency).
- 교집합 내 argmin: observer 의 *합리적 선택* ground (JND 최소화).

**CoC anchor**: 03_T_star §5.1 (hybrid formalization verbatim), pre_brainstorm §5.4
(Weber-Fechner JND).

### §4.4 Existence

두 계층의 existence 보장:

**계층 1 — Brouwer 존재** (03_T_star §2, Cat A 후보):
$$B_{T_*}^{\mathrm{FP}}(\Theta) \neq \emptyset$$
- L1 (Lemma): $T \mapsto \pi_T$ TV metric 연속 (canonical T-PF-A1-GI Cat A 기반).
- L2 (Lemma): $\psi(T)$ 연속 (L1 + bounded test function 적분 연속성).
- L3 (Lemma): Brouwer 1911 — 연속 자기 사상 $\psi : [T_{\min}, T_{\max}] \to
  [T_{\min}, T_{\max}]$ 는 고정점을 가짐.

**계층 2 — argmin 존재** (표준 분석):
- 전제: $B_{T_*}^{\mathrm{FP}} \neq \emptyset$ (계층 1) + $B_{T_*}^{\mathrm{FP}}$
  compact + $\rho_{\mathrm{JND}}$ 연속.
- $\rho_{\mathrm{JND}}(T) = T/\mathbb{E}_{\pi_T}[u]$ 는 $(0,\infty)$ 에서 연속
  (L1 + bounded functional 연속성).
- Extreme value theorem: compact 위의 연속 함수 → minimum attained.
- 따라서 $\mathrm{argmin}_{T \in B_{T_*}^{\mathrm{FP}} \cap B_\xi} \rho_{\mathrm{JND}}$
  존재.

**CoT step**: 계층 1 이 계층 2 의 전제. 계층 1 (Brouwer) 은 *sketch 단계*
(L1 quantitative TV bound 미완성). 계층 2 (argmin) 는 계층 1 을 *조건으로* 성립.
→ 전체 existence 는 **"계층 1 완성 시 Cat A"** 의 *조건부* 상태.

### §4.5 Uniqueness

**Uniqueness는 보장되지 않는다** (OPEN — OP-T*-α):

- **이유 1**: Brouwer 1911 은 *존재*만 보장. 유일성 보장은 Banach contraction
  theorem 요구 → $\psi$ 가 contraction 이어야 함.
- **이유 2**: Formation regime ($\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$) 의 multi-well
  에너지 $E$ → $\pi_T$ 의 다중 metastable basin → $\psi(T) = T$ 의 다중 해 가능.
- **이유 3**: 03_T_star §1.3 (B.2.3 verbatim): "Uniqueness is NOT guaranteed by
  Brouwer — Banach contraction principle would give uniqueness, but SCC E is *not*
  a contraction in T globally."

**Observer choice**: $|B_{T_*}^{\mathrm{FP}}| > 1$ 인 경우 관찰자는 *하나를 선택*
— JND argmin 이 선택 기준. Argmin 자체의 uniqueness 도 미보장 (다중 minimizer 가능)
— OP-T*-α 의 정량화 대상.

**canonical-observer 일관성**: 실험 (per-experiment) 마다 관찰자가 *하나의 $T_*$
를 고정* — 동일 실험 내 단일성은 *정의에 의해* (observer-fixed, per-experiment).

**CoT step**: Uniqueness 의 부재가 Route C 의 *결함*이 아니라 COB 의 *자연 귀결*:
외부 통계 없이 내부 self-consistency 만으로는 유일한 고정점을 기대할 수 없음.
다중 고정점은 *관찰자의 다중 해석 가능성* 으로 해석.

---

## §5 Route A (Mori-Zwanzig) / Route B (RG) Deprecation Proposal

### §5.1 Current OP-0021 Routes (Canonical)

canonical theorem_status.md 의 OP-0021 현재 상태:

```
OP-0021 (T_* registration):
  Status: OPEN
  Routes: A (Mori-Zwanzig) + B (RG fixed point) — 두 후보 명시
  Priority: HIGH (Stage 5 전체 의존)
```

AUX-1.5 §4.3 (canonical.md L287):
> "Mori-Zwanzig 또는 RG fixed-point route 후보."

### §5.2 COB Violation Analysis

**Route A — Mori-Zwanzig**:
- 접근: 환경 메모리 커널 $K(t-s)$ 에서 적분하여 effective T_* 유도.
- 기술: $K(t-s) = \langle F(0) F(t-s) \rangle_{\mathrm{env}}$ — 환경 fluctuation
  상관함수.
- COB 위반: *환경 Markov chain* 의 통계 ($\langle \cdot \rangle_{\mathrm{env}}$)
  가 외생 → CN-COB 위반.
- 외부 근거: Cugliandolo 2011 (J. Phys. A 44:483001) effective T review —
  *모든* Mori-Zwanzig 형 effective T 가 FDT + non-equilibrium environment 통계 의존.

**Route B — RG fixed point**:
- 접근: Renormalization group flow 의 fixed point 에서 universal effective T 유도.
- 기술: $\beta$-function $\beta(g) = 0$ → RG fixed point $g^*$ → $T_{\mathrm{eff}}$
  = $T$ at $g^*$.
- COB 위반: *보편 임계점* ($g^*$) 이 환경 물리적 universality class 에 의존 →
  외부 물리 외생 → CN-COB 위반.
- 외부 근거: Cugliandolo 2011 §6 (kinetic/granular effective T) 가 RG 접근의
  out-of-equilibrium generalization 으로 분류 — 환경 통계 불가피.

**Cugliandolo 2011 핵심 결론** (03_T_star §3.1 CoT step 1-2):
> *모든* effective T notion (FDT / kinetic / granular / active matter) 이 환경
> statistics 요구. SCC 의 CN-COB 하에서 직접 적용 불가.

**CoT step**: Route A/B 의 COB 위반은 *개별 수학 단계의 오류*가 아니라
*ontological 전제의 불일치*. 수학적으로는 정당한 접근이지만 SCC 의 폐쇄 존재론
(CN-COB) 과 *범주적으로 비호환*.

**CoC anchor**: AUX-1.5 §4.6.1 (verbatim: "Route A (Mori-Zwanzig): 환경 메모리
커널에서 유도 → 환경 외생. COB 위반. Route B (RG fixed point): 보편 임계점에서
유도 → 외부 물리 외생. COB 위반."); 03_T_star §3.1 CoT step 1-2.

### §5.3 Proposed Deprecation

**목표**: OP-0021 본문 amendment — Route A/B 를 DEPRECATED 로 표시.

**Draft OP-0021 amendment (verbatim, canonical edit 아님)**:

```
[Amendment proposal draft, P6, 2026-05-19]

OP-0021 (T_* registration) — Status: OPEN (scope revised)

Routes A (Mori-Zwanzig) and B (RG fixed point) are hereby marked:
  **DEPRECATED — COB-violating**

Rationale: Both routes require external environmental statistics for effective
T_* derivation (Cugliandolo 2011 J. Phys. A 44:483001 effective T review;
AUX-1.5 §4.6.1), violating CN-COB (AUX-1.5 §7). Route A requires environment
memory kernel statistics; Route B requires RG universality class (external physics).

Route C (observer-personal, ξ resident under OMS-1) is the unique COB-consistent
path. See P6_OMS-1_xi_Tstar_entry.md §4 for G1+G3 hybrid formalization.

OP-0021 remains OPEN with revised scope:
  1. Brouwer existence proof: Cat A 승급 (L1 quantitative TV bound — OP-T*-FIXED-POINT)
  2. ξ catalog entry: canonical OMS-1 §A amendment + Appendix OMS §N 신설
  3. Uniqueness quantification: OP-T*-α (W9+)
```

**Silent OP resolution 회피 (03_T_star §5.2 3-part 직접 인용)**:

(a) *본 접근이 OP-0021 의 어느 부분에 영향*:
"Route A/B 의 *COB 위반 측면* 의 *분석 정리* — 두 route 의 mathematical content
가 SCC ontology 와 incompatible 임을 명시."

(b) *여전히 open 의 부분 (verbatim)*:
"OP-0021 의 *T_* registration 본체* — Route C 채택 후에도 *canonical OMS-1 ξ
catalog 의 T_* entry 작성* + *Brouwer existence proof 의 Cat A 승급* 모두 OPEN.
*uniqueness* (OP-T*-α) 도 OPEN."

(c) *새 주장 (verbatim)*:
"Route C 채택 의 *추가 reason* (Brouwer existence + Weber-Fechner JND anchoring
+ OMS-1 ξ category 정합). Cat 잠정 C 후보 (검증 필요)."

**CoT step**: Deprecation 은 *수학 내용의 refutation* 이 아니라 *ontological
incompatibility 의 명시*. Route A/B 의 수학은 SCC 이론 *외부*에서 valid.

---

## §6 Counterexample Attempts (≥3)

### §6.1 Attempt 1: T_* 가 $\Theta$ 에서 유도 가능하다 (not free)

**주장**: $T_*$ 를 $\Theta = (q, \lambda, \xi)$ 의 *함수*로 결정할 수 있다 — 예:
$T_* = f(q, \lambda)$ 로 정의.

**실패 분석**:

- **단계 1**: 만약 $T_* = f(\Theta)$ 가 *수학적으로 결정*된다면, 그 결정 메커니즘이
  무엇인가?
- **단계 2**: 후보 (a) $T_* = $ variance$(u^*)$ — 자기 참조 순환 (AUX-1.5 §4.9.1
  진단: "순환. 일관된 fixed-point가 *원리적으로* 존재할 수 있지만 *유일성*은 보장
  안 됨").
- **단계 3**: 후보 (b) $T_* = 1/\lambda_{\min}(H_E)$ — *local* approximation 에
  불과, global SDE parameter 결정 불가 (AUX-1.5 §4.9.1 verbatim: "local quadratic
  approximation의 *local* scale을 정의할 뿐, *global* SDE 매개변수 T_*를 결정하지
  않음").
- **단계 4**: 모든 *external statistics* 기반 결정은 CN-COB 위반 (Route A/B
  분석, §5.2).

**결론**: $T_* = f(\Theta)$ 형태의 *수학적 결정* 은 (a) 순환이거나, (b) 국소 근사에
불과하거나, (c) COB 위반. 셋 다 *ξ resident P 분류*를 논박하지 못함.

### §6.2 Attempt 2: T_* 가 유일하다 (no multiplicity)

**주장**: $|B_{T_*}^{\mathrm{FP}}| = 1$ — fixed-point 유일, 관찰자 선택 불필요.

**실패 분석**:

- **단계 1**: 유일성은 Banach contraction 이 필요 — $|\psi'(T)| < 1$ globally.
- **단계 2**: Formation regime (T8 supercritical) 의 multi-well $E$ →
  $\pi_T$ 의 다중 metastable basin. $\psi(T) = \mathbb{E}_{\pi_T}[\mathrm{Var}]$
  가 각 basin 에서 다른 값 → multiple branches.
- **단계 3**: 03_T_star §1.3 (B.2.3) — 수치 evidence: "T-PF-A1-PE Cat A 의 $C_P
  \sim e^{\mathrm{osc}/T}$ exponential scaling 에서 *간접* confirmation — multi-well
  시 *spectral gap* 이 small (metastable basin separation) → multiple fixed-point
  candidates possible."
- **단계 4**: 반례 구성 (qualitative): 2-well potential 에서 $T$ 가 낮을 때 각
  well 이 독립적으로 variance-T consistency 를 가질 수 있음 → 최소 2개 fixed-point.

**결론**: Uniqueness 주장은 *미입증*. OP-T*-α 가 정량화 대상. Multiplicity 의
부재는 별도 증명 없이 주장 불가.

### §6.3 Attempt 3: T_* 에게 ξ Resident Framework 없이 별도 공리 부여

**주장**: $T_*$ 를 OMS-1 ξ framework 에 귀속시키지 말고, 독립적인 새 공리 (예:
"Axiom T-STOCH: $T_* \in [T_{\min}, T_{\max}]$") 로 선언.

**실패 분석**:

- **단계 1**: OMS-1 framework 는 *모든* observer-personal free parameter 를 $\xi$
  로 통일하는 것이 *목적* (canonical.md L2416 + AUX-1.5 §7.3: "OMS-1 컨테이너
  + ξ 카탈로그 + COB 원칙이 통일된 관찰자 모듈 *문서적* 등록").
- **단계 2**: 별도 공리 "Axiom T-STOCH" 를 추가하면:
  - (a) OMS-1 framework 의 *통일 목적* 을 위반 (분산 도입).
  - (b) $\xi$ 와 "Axiom T-STOCH" 의 *관계* 가 불명확 — 중복 또는 충돌 위험.
  - (c) CLAUDE.md 정책: "No per-item registry files" — 별도 공리는 동일 반패턴.
- **단계 3**: AUX-1.5 §8.5 carry-forward 결정 사항: "canonical OMS-1 B_ξ
  enumeration 수행" — ξ 내부 채움이 방향. 별도 공리는 역방향.
- **단계 4**: OMS-1 framework 가 T_* 를 수용하는 *정확한 형식* 이 ξ resident
  — 새 공리가 필요 없음 (framework 의 자연 후속).

**결론**: 별도 공리 추가는 OMS-1 통일 목적을 저해하고 중복을 생성. ξ resident
등록이 유일하게 일관된 경로.

---

## §7 Cat 자기 분류 + Honest Assessment

### §7.1 Cat A Axiomatic (ξ Resident Formal Entry)

본 P6 의 핵심 산출물의 분류:

| 항목 | Cat | 근거 |
|---|---|---|
| T_* ξ resident 선언 | **Cat A axiomatic** | OMS-1 framework 의 자연 후속; 별도 theorem 불필요 |
| Route C COB 통과 확인 | **Cat A axiomatic** | AUX-1.5 §4.9.1 prior + §5.2 systematic analysis |
| Route A/B 폐기 제안 | **제안 (미결)** | canonical OP-0021 amendment turn 별도 필요 |
| 6-field formal structure | **Cat A axiomatic** | E3 §C.2 형식 + canonical anchor 충족 |
| Brouwer existence (L1-L3) | **Cat A 후보** (잠정 Cat B) | sketch 단계; L1 quantitative TV bound 미완성 |
| Uniqueness | **OPEN** | OP-T*-α; Cat 분류 불가 |
| JND argmin selection | **Cat A axiomatic** | Weber-Fechner anchor + argmin existence (계층 2) |

### §7.2 Honest Assessment

**Cat A *axiomatic* ≠ Cat A *proved***

본 P6 의 Cat A 분류는 *axiomatic declaration* 의 성격:

1. **T_* mathematical determination 부재는 결함이 아님**: COB-respecting 이론에서
   observer-personal parameter 는 *정의상* mathematically undetermined. Cat A
   axiomatic 은 "이 미결정이 *설계에 의한 것임*을 공식 확인" 하는 act.

2. **수학적 내용의 한계 명시**:
   - Brouwer existence: sketch 수준 (L1 quantitative 미완성) → 실질적으로 **Cat B
     (conditional)** 상태.
   - Uniqueness: OPEN (OP-T*-α) — 수치 evidence 없음.
   - ξ admissible range $B_\xi^{\mathrm{OMS-1}}$: *explicit 미명시* (OP-OMS-1-ξ-2).

3. **"Cat A axiomatic" 의 정확한 의미**:
   - OMS-1 framework 가 $\xi \in B_\xi$ 를 *이미 axiom 등급*으로 선언 (canonical
     L2416 "Theorem-grade").
   - T_* 를 $\xi$ 에 추가하는 것은 *새 axiom 추가*가 아니라 *기존 axiom 의 내용
     명시* — 이것이 "framework 내의 채움" (E3 §C.4).
   - 따라서 **Cat A axiomatic = "OMS-1 framework 채움 act"** — 증명이 아닌 등록.

### §7.3 Cat A Entry Path

canonical 에서 T_* ξ entry 의 Cat A 등록 절차 (draft):

```
Step 1: canonical.md §A (OMS-1 Definition, L2416) amendment
  → $B_\xi$ 내용 선언 추가 + §N forward hook (§3.2 draft 사용)

Step 2: canonical.md Appendix OMS §N 신설
  → §N.1: T_* 6-field entry (본 P6 §2 사용)
  → §N.2+: 나머지 ξ candidates stub 형식

Step 3: theorem_status.md OP-0021 갱신
  → Route A/B DEPRECATED, Route C 채택, §N entry 완료 표시

Step 4: THEORY/CHANGELOG.md CV-1.X SEAL
  → CV-1.18 entry: "OMS-1 ξ catalog §N 신설 (T_* 정식 entry)"
```

### §7.4 Coupled Work

본 P6 와 *병렬 필요* 작업:

- **P2 결과 (OP-T*-α Cat B multiplicity)**: fixed-point 개수 정량화 → JND argmin
  uniqueness 에 영향.
- **P5 결과 (Stage 0 9-conditions)**: T-cond-7 (T 연속) 이 Langevin SDE
  well-posedness 의 전제 → T_* well-definedness 와 연결 (E3 §D 교차참조).
- **D4 결과 (L-HMORSE-LOCAL Cat A 후보)**: Kramers rate 에서 T_* 와 병렬 결합 →
  Package II Cat B 의 두 기둥 (E3 §D: "D4 Cat A + D6 ξ entry = Package II Cat B").

---

## §8 Integration with Canonical

### §8.1 OMS-1 §A Amendment Draft

**위치**: canonical.md L2416 (Definition OMS-1) 본문 끝.

**Draft (§3.2 verbatim 반복)**:

```
[Amendment to Definition OMS-1, draft 2026-05-19]
The auxiliary box B_ξ contains observer-personal free parameters under CN-COB
(AUX §7). These are axiomatically undetermined and represent observer's internal
resolution choices. The ξ-catalog is in Appendix OMS §N. First entry: T_* (§N.1).
```

**비침습 확인**: 기존 compact/Tychonoff/static face 내용 변경 없음. 추가만.

### §8.2 Appendix OMS §N Entry Draft

**위치**: canonical.md Appendix OMS 끝 (현재 §M 다음, L2663 이후).

**Draft §N header**:

```markdown
## Appendix OMS §N — ξ Catalog: Observer-Personal Parameters

Source: AUX-1.5 §4.7.1 (seed) → P6_OMS-1_xi_Tstar_entry.md (formal form).
Status: First entry T_* (§N.1) REGISTERED; remaining entries stub (§N.2–§N.11).

### §N.1 Entry: T_* (effective stochastic temperature)

| Field | Content |
|---|---|
| Symbol | $T_* \in \xi^{\mathrm{OMS-1}}$ |
| Name | Effective stochastic temperature |
| Pipeline position | Stage 5 (primary); Stage 2 via $\pi_{T_*}$ (secondary) |
| Classification | P (observer-personal); COB pass; ξ resident |
| Range | $B_{T_*}^{\mathrm{FP}}(\Theta) \cap B_\xi^{\mathrm{OMS-1}}$ |
| OP connections | OP-0021 (primary); OP-T*-FIXED-POINT (existence); OP-T*-α (multiplicity) |
| Math role | Gibbs $\pi_{T_*}$; Langevin noise; Poincaré gap; Kramers rate; variance fixed-point |
| Selection | $\mathrm{argmin}_{B_{T_*}^{\mathrm{FP}} \cap B_\xi} \rho_{\mathrm{JND}}$ (Weber-Fechner) |
| COB status | Pass (Route C; no environmental statistics) |
| Brouwer | $B_{T_*}^{\mathrm{FP}} \neq \emptyset$ (Cat A 후보 sketch, 03_T_star §2 L1-L3) |
| Uniqueness | OPEN (OP-T*-α, W9+) |

### §N.2–§N.11 Remaining ξ Entries (Stub)

Candidates from AUX-1.5 §4.7.1: ρ_pers, ε_kernel, ε_OT, θ_core, T_sensor,
d_σ, r, IC-protocol, ε (F-count threshold), η_cl. Formal entries pending.
```

**P5 연결**: §N.2 에 $T_{\mathrm{sensor}}$ stub 이 D5 의 Stage 0 9-conditions canonical
entry 와 *연결 예정* — D5 결과가 §N.2 를 채움.

### §8.3 OP-0021 본문 Amendment (Routes A/B Deprecation)

**위치**: theorem_status.md OP-0021 행.

**Draft 갱신**:

```
OP-0021 (T_* registration):
  Status: OPEN (scope revised 2026-05-19)
  Routes A (Mori-Zwanzig) + B (RG): DEPRECATED — COB-violating
  Route C (observer-personal ξ resident): ADOPTED (P6 §4 G1+G3 hybrid)
  Remaining:
    - Brouwer Cat A: L1 quantitative TV bound (OP-T*-FIXED-POINT)
    - ξ entry: canonical §A amendment + §N 신설 (ready for edit)
    - Uniqueness: OP-T*-α (W9+)
  Reference: P6_OMS-1_xi_Tstar_entry.md
```

### §8.4 theorem_status.md Update (OP-0021 Status)

위 §8.3 의 OP-0021 갱신이 theorem_status.md 의 대상. 추가 업데이트:

```
OP-T*-FIXED-POINT: 등록 권장 → OPEN 정식 등록
  Existence: Cat A 후보 (Brouwer sketch, 03_T_star §2)
  Reference: P6 §4.4 계층 1
  Required: L1 quantitative TV bound

OP-T*-α: 신규 등록
  Multiplicity quantification: |B_{T_*}^{FP}| as function of Θ
  Timeline: W9+
```

### §8.5 hypothesis_tree.md HT-3.8 → HT-3.9 (H-T* Row Update)

**HT 수정 범위**: hypothesis_tree.md 의 H-T* 관련 행.

**Draft 갱신**:

```
H-T* (stochastic temperature registration):
  이전 (HT-3.8): T_* axiomatic; Route C 권장 (AUX-1.5 §4.9.1)
  갱신 (HT-3.9 제안): T_* ξ resident formal entry (P6 §2); Route A/B DEPRECATED;
    Brouwer existence Cat A 후보; Uniqueness OPEN (OP-T*-α)
  의존성: OMS-1 Definition + AUX-1.5 §4.7.1 + 03_T_star §2
```

**수정 규칙 확인**: hypothesis_tree.md 의 수정 규칙 (HT 후미) 준수.
HT-3.9 는 HT-3.8 의 *revision* — 기존 H-T* 행 *대체* (추가 아님).

---

## §9 New Open Questions (≥3)

### §9.1 OP-OMS-1-ξ-1: ξ Catalog 의 Other Entries

**Statement**: AUX-1.5 §4.7.1 의 ξ catalog seed 에서 $T_*$ 외 10개 entries
($\rho_{\mathrm{pers}}, \varepsilon_{\mathrm{kernel}}, \varepsilon_{\mathrm{OT}},
\theta_{\mathrm{core}}, T_{\mathrm{sensor}}, d_\sigma, r, \mathrm{IC\text{-}protocol},
\varepsilon_{\mathrm{F\text{-}count}}, \eta_{\mathrm{cl}}$) 각각에 대해
*P6 와 동일한 6-field formal entry* 가 필요.

**선결 조건**:
- $T_{\mathrm{sensor}}$: D5 Stage 0 9-conditions canonical entry 완성 후 (P5 연결).
- $\rho_{\mathrm{pers}}, \theta_{\mathrm{core}}$: persistence/core threshold 의
  관찰자 의존성 formal analysis.
- $\varepsilon_{\mathrm{OT}}$: Sinkhorn regularization 과 transport topology 의
  관계 (OP-T*-β 의 전제일 수 있음).

**우선순위**: T_sensor (D5 결과 연동), ρ_pers (T-Temporal 의존), η_cl (closure
parameter, Stage 1 연결).

**CoT step**: 10개 entries 가 각자 독립적 formal analysis 를 요구. P6 가 *표준
형식* 을 제공했으므로 이후 entries 는 같은 6-field structure 적용.

### §9.2 OP-OMS-1-ξ-2: ξ Admissible Range $B_\xi^{\mathrm{OMS-1}}$ Explicit Specification

**Statement**: OMS-1 Definition 에서 $B_\xi$ 가 "auxiliary box" 로 선언되었지만
*구체적 structure* (product space? norm? topology?) 가 명시되지 않음.

**구체적 질문**:
- $B_\xi$ 의 product structure: $B_\xi = \prod_{j} B_{\xi_j}$ 인가?
  각 성분의 $B_{\xi_j}$ 는 어떤 형태인가 (interval, convex set, manifold)?
- $B_{T_*}^{\mathrm{OMS-1}}$ 성분의 상한/하한: $T_{\min}, T_{\max}$ 의 *explicit*
  $\Theta$-의존 형태?
- $B_\xi$ 의 topology: OMS-1 compact 주장이 $B_\xi$ 의 compact 를 요구 →
  각 $B_{\xi_j}$ 가 compact 이어야 함 (Tychonoff) → $T_* \in [T_{\min}, T_{\max}]$
  (bounded closed interval) 이면 충족.

**현재 상태**: $B_\xi$ 는 선언만 있고 structure 없음 (E3 §C.1: "catch-all box —
내용물 카탈로그가 비어있음").

**중요성**: compact observer space $\mathcal{M}_{\mathrm{obs}}$ 주장 (OMS-1 Definition)
이 $B_\xi$ compact 에 의존 → $B_\xi$ 의 explicit structure 가 *OMS-1 theorem-grade
선언의 완전성* 에 필요.

### §9.3 OP-OMS-1-ξ-3: Cross-Observer ξ Variability (Population Study)

**Statement**: 서로 다른 관찰자가 다른 ξ 값 (특히 다른 $T_*$) 을 선택할 때, SCC
이론이 예측하는 *관찰자 집단의 행동 분포* 는 무엇인가?

**구체적 질문**:
- 관찰자 집단 $\mathcal{O} = \{o_1, \ldots, o_N\}$ 가 각각 $T_*^{(i)} \in
  B_{T_*}^{\mathrm{FP}}$ 를 선택할 때, 집단 분포 $\mu(\mathcal{O})$ 의 특성?
- 서로 다른 $T_*$ 선택이 different *formation threshold* 를 낳는가?
  (→ 관찰자마다 다른 T8 임계점 지각)
- *Inter-observer consistency*: 두 관찰자가 같은 $u_t$ 를 보고 같은 formation
  을 report 하는 조건? (→ JND criterion 의 *social* 버전)

**SCC 이론적 중요성**: DECL-1.0 Q2 ("어떤 차이의 덩어리가 언제부터 하나의 객체가
되는가?") 의 *관찰자-의존 버전*. 서로 다른 $T_*$ 가 서로 다른 formation threshold
를 낳으면 → 객체성 자체가 관찰자-상대적 → SCC 의 *anti-realist ontological 함의*.

**선결 조건**: P6 ξ entry 완성 + OP-T*-α (multiplicity) 부분 해결.

---

## §10 Summary

### §10.1 P6 산출물 목록

| 번호 | 산출물 | 형식 | Cat |
|---|---|---|---|
| 1 | T_* 6-field formal entry (§2) | Draft canonical §N.1 | Cat A axiomatic |
| 2 | OMS-1 §A amendment (§3.2) | Draft canonical L2416 추가 | Cat A axiomatic |
| 3 | Appendix OMS §N draft (§8.2) | Draft canonical §N 전체 | Cat A axiomatic |
| 4 | Route C G1+G3 hybrid formal (§4) | Promotion-ready formalization | Cat A axiomatic |
| 5 | Route A/B deprecation proposal (§5) | OP-0021 amendment draft | 제안 (미결) |
| 6 | Counterexample attempts ×3 (§6) | Falsification record | — |
| 7 | Cat 자기 분류 + Honest assessment (§7) | Non-overclaim 명시 | — |
| 8 | New OP ×3 (§9) | Open question registration | OPEN |

### §10.2 Amendment Status

| 대상 | 내용 | 상태 |
|---|---|---|
| canonical.md L2416 | OMS-1 §A amendment (§3.2) | Draft ready |
| canonical.md Appendix OMS §N | ξ catalog §N 신설 (§8.2) | Draft ready |
| theorem_status.md OP-0021 | Route A/B DEPRECATED, Route C (§8.3) | Draft ready |
| theorem_status.md OP-T*-FIXED-POINT | 정식 등록 (§8.4) | Draft ready |
| theorem_status.md OP-T*-α | 신규 등록 (§8.4) | Draft ready |
| hypothesis_tree.md H-T* | HT-3.8 → HT-3.9 갱신 (§8.5) | Draft ready |
| THEORY/CHANGELOG.md | CV-1.18 entry | P6 완성 후 기록 |

**전체 canonical edit**: 결정권자의 별도 amendment turn 필요. 본 P6 는 *edit 준비
문서* — canonical 은 read-only (CLAUDE.md policy).

### §10.3 Cat Verdict

**P6 전체 Cat 판정: Cat A axiomatic (ξ resident 정식 등록)**

- *Cat A axiomatic 인 이유*: OMS-1 framework 채움 act. T_* 를 $B_\xi$ 의
  *첫 번째 formal entry* 로 등록하는 것은 OMS-1 Definition (theorem-grade) 의
  *자연 후속*.
- *Cat A proved 아닌 이유*: Mathematical determination 부재 by design (COB).
  Brouwer existence 는 sketch (잠정 Cat B). Uniqueness OPEN.
- *OP-0021 에 대한 함의*: Route C 채택 scope 내에서 *부분 진전* (ξ catalog entry
  ready) — OP-0021 전체 해결 아님.

---

*End of P6_OMS-1_xi_Tstar_entry.md.*
*Source: E3_hmorse_stage0_oms.md §C + 03_T_star_fixed_point.md §5.*
*작성: W8-Day2, 2026-05-19, D6 (Sonnet, executor).*
*다음 단계: 결정권자의 canonical amendment 실행 (§8.1-§8.5 draft 사용).*
