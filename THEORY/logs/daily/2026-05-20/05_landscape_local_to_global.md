---
type: log/daily/refined-exposition
date: 2026-05-20
day_of_week: Wed
session_label: W8-Day3 POST-99 evening — Local-to-Global Energy Landscape Exposition (refined per 7 user corrections)
canonical_version: CV-1.19 (sealed 2026-05-20 evening, untouched throughout)
mode_label: working-layer exposition refinement (NOT verification, NOT SEAL-prep)
status: working-layer draft, 7 corrections applied, NOT canonical-ready (Cat C exposition with Cat A/B anchors)
purpose: |
  국소(local) → 상태공간(state space) → 균일해 불안정성(uniform instability) 3단 노출의
  epistemically calibrated 버전. conversational draft 의 직관은 유지, 강한 수학적 주장은
  7개 user-specified 수정사항으로 약화. canonical 진입 전 정밀화 단계의 first instance.
preceded_by:
  - W8-Day3 99_summary.md §POST-99 EXTENSION (CV-1.19 SEAL completion)
  - working/foundation/manifold_topology_attempt_v1.md (S1/S2/S3 anchors)
  - working/field_equation_framework/06_surface_tension_rescaling_cat_a.md (L-SURFACE-TENSION-RESCALE Cat A direct)
  - conversational draft (this session, §1-§3 unified)
canonical_anchors:
  - canonical.md §13 Theorem 4 (L1466) — μ_k formula + spinodal discussion (Cat A)
  - canonical.md §13 T-σ-Lemma-1 (L1386) — Hessian commutes with G_u-action (Cat A)
  - canonical.md §13 V5b-T-zero (L1328) — orbit-tangent zero on corner-saturated configurations (Cat A def)
  - canonical.md §13 L-HMORSE-LOCAL (L1953-1990) — (C1)-(C5) post-formation stability (Cat B, CV-1.16)
  - canonical.md §13 L-S3-KERNEL-MULT (L1798) — kernel-multiplicity identity (Cat A, CV-1.19)
  - canonical.md §13 L-LOJASIEWICZ-CG (L2066) — c_G explicit bound (Cat B, CV-1.19)
  - canonical.md §13 SB7 (L2540) — Σ_T8 = Σ_Hess codim-1 algebraic (Cat A)
  - CV-1.19_SEAL.md (193L, new) — 100 claims baseline + non-overclaim explicit
constraint_compliance:
  canonical_edits: 0
  DECLARATION_edits: 0
  theorem_status_edits: 0
  hypothesis_tree_edits: 0
  scc_edits: 0
  new_framework_letters: 0
  silent_OP_resolution: 0
  retraction_retry: 0
  pytest_status: 225 passed + 1 xfailed (inherited, scc/ 0 edits)
cot_enforced: yes
coc_enforced: yes
seven_corrections_applied:
  - "#1 λ-index unification (1-index, μ_k for k=2..n on 1⊥)"
  - "#2 Soften unique critical point claim (fully symmetric distinguished state)"
  - "#3 Soften global skeleton claim (primary bifurcation skeleton only)"
  - "#4 Goldstone three-type reclassification (Type A/B/C; uniform has A/B only)"
  - "#5 Pitchfork vs transcritical caution (c ≠ 1/2 needs case-by-case normal form)"
  - "#6 c = m/n explicit (uniform value not independent)"
  - "#7 Branch → vertex is tendency, not theorem (finite-β catalog of branch fates)"
---

> [!nav] Linked: [[00_plan|W8-Day3 plan]] · [[99_summary|99 summary + POST-99 EXTENSION]] · [[../../canonical/canonical|CV-1.19 canonical]] (§13 Theorem 4 L1466, T-σ-Lemma-1 L1386, V5b-T-zero L1328, L-HMORSE-LOCAL L1953-1990, L-S3-KERNEL-MULT L1798, L-LOJASIEWICZ-CG L2066, SB7 L2540) · [[../../canonical/DECLARATION|DECL-1.0]] · [[../../canonical/CV-1.19_SEAL|CV-1.19 SEAL]] · [[../../working/foundation/manifold_topology_attempt_v1|v1 master synthesis (S1-S5)]] · [[../../working/field_equation_framework/06_surface_tension_rescaling_cat_a|06 L-SURFACE-TENSION-RESCALE]]

# 05 — Local-to-Global Energy Landscape Exposition (Refined)

**Mode**: working-layer exposition refinement. NOT verification (어제 02), NOT SEAL-prep (오후 CV-1.19), NOT canonical edit. *Conversational draft 의 7 user corrections 적용 정밀화*.

---

## §0 — Pre-flight: xref check + §8a P1-P6 audit + 7 corrections checklist

### §0.1 Pre-work xref check

본 문서가 *기존 canonical / working 의 중복* 인지 확인:

| 잠재 중복 source | grep 결과 | 판정 |
|---|---|---|
| `canonical.md` "local to global" / "uniform instability" / "primary bifurcation" | 부재 (Theorem 4 + SB7 자체는 *수학적 statement*; 본 exposition 은 *narrative integration*) | 신규 contribution |
| `working/foundation/manifold_topology_attempt_v1.md` §1 (S1-S5 catalog) | S-claims 의 *summary list*; 본 exposition 의 §1-§3 narrative 와 *상보적* | 신규 contribution |
| `working/field_equation_framework/01_ns_inspired_synthesis.md` §3-§4 (SCC field structure + NS mapping) | NS contrastive analysis; 본 exposition 의 §2.4 (Π ↔ NS pressure) 와 *cross-reference only* | 신규 contribution |
| `THEORY/working/INDEX.md` foundation/ section | conversational draft 의 *축약본* 없음 | 신규 contribution |

**판정**: 본 exposition = *기존 산발 산출물의 narrative integration + 7 corrections 적용*. 중복 없음, contribution 정합.

### §0.2 §8a archive pattern P1-P6 audit

본 작업이 archive (`_archive/research_os_2026-04-12/`) 의 *재도입 위험* 인지:

| Pattern | 검사 | 결과 |
|---|---|---|
| P1 — 근본 질문 우회 | DECL-1.0 Q1 (T8) 의 *직접 narrative integration* (§3 전체) — 우회 아님 | ✓ |
| P2 — Vocabulary refactoring | $u_t$ primitive 변경 0, 새 alphabet 0 (Goldstone Type A/B/C 는 *재분류 만*, 새 letter 아님) | ✓ |
| P3 — Canonical content 중복 | Theorem 4 / SB7 / V5b-T-zero / L-S3-KERNEL-MULT / L-LOJASIEWICZ-CG 모두 *anchor only*, 재증명 0 | ✓ |
| P4 — 외부 도구 도입 | NS contrastive reference 만, 새 theory 도입 0 | ✓ |
| P5 — Self-audit 부재 | 본 §0 + §4 + §6 의 triple audit | ✓ |
| P6 — 언어-수학 분리 | 각 절마다 *수식 박스 + 산문 설명* 분리 | ✓ |

**0/6 부합 → 진행 합법**.

### §0.3 7 Corrections checklist (사용자 feedback 정확 매핑)

| # | Correction | 적용 위치 | Status |
|---|---|---|---|
| 1 | λ-index unification (1-index, k=2..n on 1⊥) | §1.4, §3.2, §3.5 | inline 적용 |
| 2 | "유일한 critical point" 약화 → "fully symmetric distinguished state" | §3.1 | inline 적용 |
| 3 | "전역 골격" → "primary bifurcation skeleton" | §3.9, §3.10 | inline 적용 |
| 4 | Goldstone 3-type 재분류 (Type A/B/C) | §3.7 (대규모 rewrite) | inline 적용 |
| 5 | Pitchfork vs transcritical 약화 (c ≠ 1/2 case-by-case) | §3.4 | inline 적용 |
| 6 | $c = m/n$ 명시 (균일해 value 비독립) | §3.1 첫 박스 | inline 적용 |
| 7 | Branch → vertex 는 tendency, theorem 아님 | §3.3, §3.6 finite-β catalog | inline 적용 |

각 correction 의 적용은 해당 절에서 *명시적으로 marked* (예: "**Correction #N 적용**").

---

# 제1부 — 국소적 형태 (Local Form)

## §1.1 한 점에서 — Single-site double-well

가장 작은 단위는 단 하나의 노드 $i$에서의 $u_i \in [0,1]$. 이 점이 느끼는 단일-site 에너지 (canonical §3.5; CLAUDE.md I6 correction):

$$W(u_i) = u_i^2(1-u_i)^2$$

이중우물 (double-well). 두 안정점 $u = 0$ (참여 없음) 과 $u = 1$ (완전 참여), 한 불안정점 $u = 1/2$ (능선).

### §1.1.1 도함수 catalog

- $W'(u) = 2u(1-u)(1-2u)$ (factor 2; CLAUDE.md "Critical Implementation Details" I6 correction)
- $W''(u) = 2(1 - 6u + 6u^2)$
- $W'''(u) = 12(2u - 1)$

**핵심 값**:
- $W''(0) = W''(1) = 2$ (안정점에서 양)
- $W''(1/2) = -1$ (불안정점에서 음)
- $W'''(1/2) = 0$ (대칭 중심)

### §1.1.2 Spinodal 구간

$W''(u) < 0 \iff u \in (s_-, s_+)$ where:
$$s_\pm = \frac{3 \mp \sqrt{3}}{6} \approx 0.211 \text{ 또는 } 0.789$$

**spinodal 내부에서만 비균일 분기 가능** (canonical Theorem 4 hypothesis discussion, L1466).

### §1.1.3 국소 해석

> 한 노드는 본질적으로 "0이거나 1이거나" 선택하고 싶어합니다. 중간값은 불안정한 능선 위에 있을 뿐. 그러나 *어떤 중간값에서 능선이 가장 가파른가* (= $\lvert W''(c) \rvert$ 최대) 는 $c = 1/2$.

---

## §1.2 두 점 사이 — Pairwise smoothness coupling

이제 두 노드 $i, j$가 간선 $(i,j) \in E$ 로 연결되어 있다고 하자. 둘 사이의 **smoothness 비용** (canonical §3.5):

$$E_{bd}^{\text{pair}}(u_i, u_j) = \alpha \cdot w_{ij}(u_i - u_j)^2$$

여기서 $w_{ij} > 0$ 은 간선 가중치.

### §1.2.1 전체 그래프 합산

모든 간선에 대해 합하면:
$$\alpha \cdot u^T L_G u = \alpha \sum_{(i,j) \in E} w_{ij}(u_i - u_j)^2$$

여기서 $L_G = D_G - A_G$ 는 graph Laplacian ($D_G$ degree diagonal, $A_G$ adjacency matrix). $L_G$ 는 symmetric positive semi-definite (PSD).

### §1.2.2 두 욕구의 갈등 — 이론의 핵심

> **한 노드의 욕구**: $W(u_i)$ → "0 또는 1로 가자"
> **이웃 사이의 욕구**: $w_{ij}(u_i - u_j)^2$ → "같은 값을 갖자"
>
> 이 둘은 일반적으로 *양립 불가능*. 만약 이웃 노드 일부가 0, 일부가 1을 원한다면, 어딘가에서 *transition* 이 일어나야 한다. 이 transition 이 *boundary*.

---

## §1.3 Allen-Cahn balance — 국소 boundary 구조

§1.1 + §1.2 를 결합한 boundary energy (canonical §3.5):

$$\boxed{\mathcal{E}_{bd}(u) = \alpha\, u^T L_G u + \beta \sum_{i=1}^n W(u_i)}$$

이것이 그래프 위 **Allen-Cahn** 형식. 두 욕구의 균형으로 다음이 결정됩니다.

### §1.3.1 Boundary 폭 (interface width)

$$\ell_{bd} \sim \sqrt{\alpha/\beta}$$

- $\alpha$ 크면 → smoothness 강 → boundary *퍼짐* (흐릿한 경계)
- $\beta$ 크면 → double-well 강 → boundary *얇아짐* (선명한 경계)

### §1.3.2 Surface tension — Wave 2 critic √2 fix 반영

Modica-Mortola 표준 공식 (canonical §5.3 / `working/field_equation_framework/12_wave1_critical_fixes_consolidated.md` §2 Wave 2 critic Fix #1):

$$\boxed{\sigma = \frac{\sqrt{2}}{6}\sqrt{\alpha\beta} \approx 0.2357\sqrt{\alpha\beta}}$$

도출:
$$\sigma = \sqrt{\alpha\beta} \int_0^1 \sqrt{2W(s)}\,ds = \sqrt{\alpha\beta} \cdot \sqrt{2}\int_0^1 s(1-s)\,ds = \sqrt{\alpha\beta} \cdot \frac{\sqrt{2}}{6}$$

**역사적 주의** (Wave 2 critic): files 05/06 의 *initial* $\sigma = \sqrt{\alpha\beta}/3$ 표기는 *factor $\sqrt{2}$ 오차*. 본 문서는 Wave 2 corrected form $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta}$ 사용.

### §1.3.3 핵심 항등식 — Parameter rescaling

$(\alpha, \beta) \to (s\alpha, s\beta)$ 하에서 (L-SURFACE-TENSION-RESCALE, Cat A direct, `working/field_equation_framework/06`):

- $\beta/\alpha$ 보존 → T8 조건 그대로
- $\sqrt{\alpha/\beta}$ 보존 → boundary 폭 그대로
- $\sqrt{\alpha\beta} \to s\sqrt{\alpha\beta}$ → **surface tension만 linear scaling**

> $\ell_{bd}$ 와 $\sigma$ 는 $(\alpha, \beta)$ 의 *서로 다른 조합*. 따라서 *형상은 그대로 두고 강도만 키울 수 있다*. 이것이 어제 CSSL critic 에서 살아남은 유일한 idea.

---

## §1.4 국소 Hessian spectrum (Correction #1 적용)

균일해 $u^* = c\mathbf{1}$ 근방에서의 Hessian. **여기서부터 1-index convention 통일**.

### §1.4.1 λ-index convention (Correction #1)

Graph Laplacian $L_G$ 의 eigenvalues 를 *1-index* 로 통일:

$$\boxed{0 = \lambda_1(L_G) < \lambda_2(L_G) \leq \lambda_3(L_G) \leq \cdots \leq \lambda_n(L_G)}$$

- $\lambda_1 = 0$ 는 *constant mode* (eigenvector $\mathbf{1}/\sqrt{n}$); 그래프가 연결되어 있으면 중복도 1
- $\lambda_2$ = **Fiedler eigenvalue** (algebraic connectivity); 실질적 *첫* 비자명 mode
- 모드들은 mass-conservation 제약 ($\Sigma_m$ 의 접공간 $\mathbf{1}^\perp$) 에서 의미를 가짐

**중요**: mass constraint 에 의해 constant mode 가 *사영자 $\Pi$ 에 의해 제거* 됨 (§2.4). 따라서 *유효 spectrum* 은 $k = 2, \ldots, n$.

### §1.4.2 Hessian eigenvalues on $T_u\Sigma_m = \mathbf{1}^\perp$

Canonical Theorem 4 (canonical.md L1466, Cat A) — Correction #1 적용 표현:

$$\boxed{\mu_k = 4\alpha\,\lambda_k(L_G) + \beta\,W''(c), \qquad k = 2, \ldots, n}$$

여기서 $k = 1$ (constant mode) 은 $\Pi$ 에 의해 제거 — 본 spectrum 에 포함되지 않음.

**의미**:
- $\mu_k > 0$: mode $k$ 방향으로 perturbation 시 에너지 *증가* → 안정
- $\mu_k < 0$: 같은 방향으로 *감소* → 불안정
- $\mu_k = 0$: 평평 — 임계 또는 zero mode

### §1.4.3 T8 critical condition (Correction #1 적용)

가장 약한 mode 는 $\mu_2$ (Fiedler):
$$\mu_2 = 4\alpha\,\lambda_2(L_G) + \beta\,W''(c)$$

Spinodal 내부 ($W''(c) < 0$) 에서 처음 0 이 되는 조건:
$$\boxed{\mu_2 = 0 \iff \frac{\beta}{\alpha} = \frac{4\lambda_2(L_G)}{\lvert W''(c) \rvert}}$$

이것이 canonical T8 — DECLARATION-1.0 의 중심 정리. canonical SB7 (L2540, Cat A) 는 *$\Sigma_{T8} = \Sigma_{\mathrm{Hess}}$ codim-1 algebraic hypersurface*.

---

## §1.5 국소 사진 정리

```
한 노드 i:        W(u_i) 이중우물 — 0 또는 1 선호
                 │
                 │   spinodal interior: s_- < c < s_+
                 ↓
이웃과의 쌍:     α w_{ij}(u_i - u_j)² — 같아지기 비용
                 │
                 ↓
국소 balance:    α (smoothness) vs β (double-well)
                 │
                 ↓
나타나는 것:     ℓ_bd ~ √(α/β),  σ = (√2/6)·√(αβ)
                 │
                 ↓
Hessian on 1⊥:   μ_k = 4αλ_k + βW''(c),  k = 2,...,n  ← Correction #1
                 │
                 ↓
임계:           Fiedler mode μ_2 = 0  ⟺  β/α = 4λ_2/|W''(c)|
```

### §1.5.1 국소 시각의 한계 — 전역으로 가야 하는 이유

> 위 모든 양은 *한 점 근방의 곡률* 만 말합니다. 두 unstable point 사이를 *어떻게 가는가*, *얼마나 멀리 있는가*, *몇 개의 객체가 가능한가* 는 보이지 않습니다. 또한 *어디서 boundary 가 형성되는가* (그래프의 어느 부분에서 분할이 일어나는가) 도 국소 곡률만으로는 답할 수 없습니다.

이것이 *상태 공간 자체의 형태* (§2) 와 *균일해의 불안정성 분기 구조* (§3) 로 가야 하는 이유입니다.

---

# 제2부 — 상태 공간의 형태 (State Space Geometry)

먼저 $u_t$가 *어디에 살고 있는가* 를 정확히 잡습니다. 에너지 분석은 그 다음이고, 동역학은 그보다 더 뒤입니다. 무대를 모르면 연극을 못 봅니다.

## §2.1 세 겹의 제약 — 무대의 건축

상태 공간은 **세 단계 제약의 교집합** 입니다 (canonical §3.1 + T-PF-A1-AR).

### §2.1.1 1단계 — 주변 공간 (Ambient)

가장 큰 공간은 단순한 유클리드:
$$u \in \mathbb{R}^n, \quad n = \lvert V \rvert$$

### §2.1.2 2단계 — 박스 제약 (Box)

각 노드가 $[0,1]$ 안에:
$$u \in [0,1]^n = \{u \in \mathbb{R}^n : 0 \leq u_i \leq 1 \text{ for all } i\}$$

**$n$차원 하이퍼큐브** (hypercube):
- $2^n$ 개의 꼭짓점 (각 좌표가 0 또는 1)
- 각 꼭짓점 = "**완전히 결정된 이진 상태**" — 어느 노드는 in (1), 어느 노드는 out (0)
- $n \cdot 2^{n-1}$ 개의 모서리
- $2n$ 개의 codim-1 면 (각 $u_i = 0$ 또는 $u_i = 1$)

### §2.1.3 3단계 — 질량 제약 (Mass)

총합 고정 (canonical §3.1):
$$\sum_{i=1}^n u_i = m, \quad m \in [0, n]$$

이것은 affine **하이퍼평면** (codim-1):
$$H_m = \{u \in \mathbb{R}^n : \mathbf{1}^T u = m\}$$

법선벡터 $\mathbf{1} = (1, \ldots, 1)$.

### §2.1.4 세 제약의 교집합 — 상태 공간

$$\boxed{\Sigma_m = [0,1]^n \cap H_m = \{u \in [0,1]^n : \sum_i u_i = m\}}$$

이것이 SCC 의 진짜 무대 (canonical T-PF-A1-AR, L1953 anchor; W6 D4 Sessions M–N CV-1.8 Cat A).

---

## §2.2 $\Sigma_m$의 정체 — Hypersimplex $\Delta(n, m)$

$\Sigma_m$ 은 조합기하학적으로 잘 알려진 객체.

### §2.2.1 차원
$$\dim \Sigma_m = n - 1$$
($n$차원 큐브를 codim-1 평면으로 자르므로.)

### §2.2.2 $m$ 값별 형태

| $m$ 값 | $\Sigma_m$ 모양 | 비고 |
|---|---|---|
| $m = 0$ | 단일점 $\{0\}$ | 모두 0 |
| $m \in (0, 1)$ | 원점에서 잘린 작은 simplex | $n$개 꼭짓점 |
| $m = 1$ | **표준 simplex** $\Delta^{n-1}$ | $n$개 꼭짓점 |
| $m \in (1, n-1)$ | **진정한 hypersimplex** $\Delta(n, m)$ | $\binom{n}{\lceil m \rceil}$ 또는 $\binom{n}{\lfloor m \rfloor}$ 꼭짓점 (정수 $m$ 이면 정확) |
| $m = n/2$ | **중앙 slice** (최대 부피) | $\binom{n}{n/2}$ 꼭짓점 (최대) |
| $m = n$ | 단일점 $\{\mathbf{1}\}$ | 모두 1 |

### §2.2.3 꼭짓점의 의미 — Discrete formations

$m$ 정수 → $\Sigma_m$ 의 꼭짓점:
$$V(\Sigma_m) = \{u \in \{0,1\}^n : \sum u_i = m\}$$

**$n$ 노드 중 정확히 $m$ 개를 골라 1로 만든 모든 방법** — $\binom{n}{m}$ 가지. 각 꼭짓점 = *한 가지 완전 crisp formation*.

> **핵심 통찰**: $\Sigma_m$ 의 꼭짓점들은 *미리 정해진 객체의 카탈로그*. SCC 동역학은 이 꼭짓점들 사이를 *내부 부피를 통해* 움직임. 어느 꼭짓점에 안착할지가 "어떤 객체가 출현하는가". 단, **꼭짓점 도달은 $\beta \to \infty$ 극한 tendency** 이지 *모든 finite-β trajectory 가 꼭짓점에 도달함* 을 의미하지 않음 (Correction #7; §3.6 참조).

---

## §2.3 경계 격자 — 차원 stratification

$\Sigma_m$ 은 *닫힌 볼록 다면체*. 그 경계는 차원별 stratification:

```
차원         경계 객체              의미
n-1   ←  interior              모든 노드 0 < u_i < 1
n-2   ←  facet (한 노드 saturated)  한 노드가 in 또는 out
n-3   ←  ridge (두 노드 saturated)  두 노드 결정
 ⋮         ⋮
 0    ←  vertex (m개 노드 1)       완전 crisp formation
```

### §2.3.1 Saturation 의 의미

노드 $i$ 가 *saturated* ($u_i = 0$ 또는 $u_i = 1$) → "이 노드는 *결정되었다*".

> **객체화 = 차원 압축**: 시작은 interior 의 모호한 상태. 점점 더 많은 노드가 0/1 로 포화 → *더 낮은 차원의 면* 으로 빠져나옴. 꼭짓점에 도달하면 *완전한 객체*. 단, finite-β 에서는 partial saturation (facet/ridge 내부) 에 머무를 수 있음 (Correction #7).

---

## §2.4 접공간과 사영자 — Π 의 결정성

### §2.4.1 접공간

내부 $u \in \mathrm{int}(\Sigma_m)$ 에서, 어느 방향으로 움직여도 $\Sigma_m$ 안에 머무를 수 있는가?

$\sum u_i = m$ 보존하려면 $\sum v_i = 0$, 즉 $v \perp \mathbf{1}$. 따라서:

$$\boxed{T_u\Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^T v = 0\} = \mathbf{1}^\perp}$$

- 차원 $n - 1$
- 모든 내부점에서 같음 (parallel transport trivial)

### §2.4.2 사영자 Π — SCC 동역학의 핵심

$\mathbb{R}^n$ 에서 $T_u\Sigma_m$ 으로의 정직교 사영 (canonical T-PF-A1-AR, Cat A, CV-1.8):

$$\boxed{\Pi = I - \frac{1}{n}\mathbf{1}\mathbf{1}^T}$$

성질:
- $\Pi^2 = \Pi$ (사영자)
- $\Pi^T = \Pi$ (대칭)
- $\Pi\mathbf{1} = 0$ (constant mode 죽임)
- rank $= n - 1$
- 스펙트럼: $\{0 \text{ (중복도 1)}, 1 \text{ (중복도 } n-1)\}$ — **L-PROJ-1** (`working/field_equation_framework/04` §3.2, working Cat A)

### §2.4.3 사용처

모든 SCC 동역학에서 등장 (canonical T-PF-A1-SDE, Cat A, CV-1.8):
- Reflected Langevin: $dU = -\Pi\nabla E\,dt + \sqrt{2T_*}\,\Pi\,dB + dK$
- Gradient flow: $\nabla E$ 대신 *제약된* $\Pi\nabla E$
- Hessian: $T_u\Sigma_m$ 으로 제약된 $\Pi^T H \Pi$ 의 spectrum 만 의미

### §2.4.4 NS pressure 와의 deep match (cross-reference)

`working/field_equation_framework/01_ns_inspired_synthesis.md` §4.3:

| Navier-Stokes | SCC |
|---|---|
| $-\nabla p / \rho$ (압력항) | $\Pi$ (mass 사영자) |
| $\nabla \cdot u = 0$ (incompressibility, *local*) | $\mathbf{1}^T u = m$ (mass conservation, *global*) |
| $p$ = Lagrange multiplier | $\Pi$ = constraint enforcer |

**두 operator가 정확히 같은 mathematical role**. 차이는: NS는 *local* 제약, SCC는 *global* 제약. 이 local vs global 차이가 dynamic class 를 결정 (`working/field_equation_framework/01` §4.3 + §6.3 spectrum proof: SCC ≠ Cahn-Hilliard).

---

## §2.5 Skorokhod reflection — 경계 처리

내부에서는 매끄럽지만, 경계 $u_i = 0$ 또는 $u_i = 1$ 에 닿으면? 동역학이 박스를 *떠나려고* 하면 **Skorokhod 국소시간** $K_t$ 가 그것을 막음 (canonical T-PF-A1-AR, Cat A, CV-1.8, Lions-Sznitman 1984 convex case):

$$dU_t = -\Pi\nabla E(U_t)\,dt + \sqrt{2T_*}\,\Pi\,dB_t + dK_t$$

$K_t$ 의 역할:
- 내부에서는 0
- $u_i = 0$ 도달 시 안쪽으로 *infinitesimal* 밀어냄
- $u_i = 1$ 에서도 마찬가지
- 질량 보존 유지하면서 박스 안에 머물게 함

### §2.5.1 Saturation 의 동적 의미

$u_i$ 가 0 이나 1 에 도달했다는 것은:
- "이 노드는 결정되었다"
- 더 이상 $u_i$ 방향으로의 *부드러운 변화* 없음
- 그러나 *다른 노드들의 변화로 인해* 다시 $u_i$ 가 깨어날 수는 있음 (mass conservation 의 *글로벌* 보상)

> **SCC 동역학 = 내부의 부드러운 유체 + 경계의 충격적 반사**. 객체 형성 과정 = 점점 더 많은 노드가 saturated → 차원이 점점 낮아지는 면으로 압축.

---

## §2.6 위상 구조

| 성질 | 값 |
|---|---|
| 연결성 | 연결 (convex polytope) |
| 콤팩트성 | 콤팩트 (closed bounded) |
| 볼록성 | 볼록 (Box ∩ hyperplane) |
| 단순연결성 | 단순연결 ($D^{n-1}$ 위상동형) |
| Euler 표수 | 1 (디스크) |
| 호몰로지 | trivial (자명) |

**즉 위상적으로는 그냥 디스크**. 모든 흥미로움은 위상이 아니라 *기하* 와 *그 위에 얹힌 에너지 함수* 에서 옵니다.

---

## §2.7 작은 예시 — $n = 3, m = 1$

$$\Sigma_1 = \{u \in [0,1]^3 : u_1 + u_2 + u_3 = 1\} = \Delta^2$$

표준 2-simplex (정삼각형):

```
              (0,0,1)
                 ●
                / \
               /   \
              /  ●  \   ← 균일해 u* = (1/3, 1/3, 1/3)
             /       \
            /         \
           ●───────────●
        (1,0,0)     (0,1,0)
```

- 3개 꼭짓점: $(1,0,0), (0,1,0), (0,0,1)$ — 각각 *어느 노드 하나만 in* 인 객체
- 3개 모서리: 두 노드 사이 transition
- 1개 내부: 모든 노드 부분 참여
- 중심점 $(1/3, 1/3, 1/3) = c\mathbf{1}$ with $c = 1/3 = m/n$ (**Correction #6 의 작동 예시**)

---

## §2.8 일반 hypersimplex 의 풍부함

$n = 4, m = 2$: $\Sigma_2 = \Delta(4, 2) =$ **정팔면체** (octahedron):
- $\binom{4}{2} = 6$ 꼭짓점: $(1,1,0,0), (1,0,1,0), (1,0,0,1), (0,1,1,0), (0,1,0,1), (0,0,1,1)$
- 중심점 $u^* = (1/2, 1/2, 1/2, 1/2)$ = 균일해 with $c = 2/4 = 1/2 = m/n$

더 큰 $n$ 에서는 매우 풍부한 조합 구조 (permutohedron family 의 친척).

---

## §2.9 무대의 본질 — 한 줄 요약

```
주변 공간 ℝⁿ
   │
   ↓ box constraint
[0,1]ⁿ — n차원 하이퍼큐브, 2ⁿ 꼭짓점
   │
   ↓ mass constraint  Σu_i = m
Σ_m — (n-1)차원 hypersimplex Δ(n, m)
   │
   ├─ interior (매끈 manifold, dim n-1)
   ├─ facets (codim 1, 한 노드 saturated)
   ├─ ⋮
   └─ vertices (꼭짓점, 완전 crisp, C(n,m) 개)

접공간 어디서나:  T_uΣ_m = 1⊥ = mean-zero subspace
사영자:           Π = I − (1/n)11ᵀ
경계 처리:         Skorokhod K_t (Lions-Sznitman)
대칭:             Aut(G) 작용 (꼭짓점 permutation)
```

### §2.9.1 세 가지 핵심 결론

1. **꼭짓점 = 객체 카탈로그**: $\binom{n}{m}$ 개의 가능한 완전 crisp formations 가 미리 *기하학적으로* 존재. 동역학은 어디에 안착할지 선택 (단, finite-β 에서는 partial saturation 도 가능, §3.6 + Correction #7).

2. **차원 압축이 곧 객체화**: interior (모호) → facets → ⋯ → vertices (완전 결정).

3. **사영자 Π 가 SCC 의 진짜 골격**: 모든 동역학·노이즈·gradient 가 Π 통과. NS pressure 와 동일 mathematical role.

---

# 제3부 — 균일해의 불안정성 (Uniform Solution Instability)

지금까지의 Hessian 분석은 *한 점 근방의 곡률* 만 말합니다. 전역으로 가려면 **균일해 $u^* = c\mathbf{1}$ 의 불안정성 구조** 가 모든 것의 골격 (단 **primary bifurcation skeleton** 의 의미에서, Correction #3) 이 됩니다.

## §3.1 균일해 도입 — Correction #2 + #6 적용

### §3.1.1 균일해의 정의 — Correction #6 (c = m/n 명시)

**중요 (Correction #6)**: $u^* = c\mathbf{1} \in \Sigma_m$ 이려면 $\sum_i u_i^* = nc = m$, 즉:

$$\boxed{c = \frac{m}{n}}$$

따라서 균일해의 $c$ 값은 *비독립*. $c$ 를 바꾼다는 것은 *mass slice $\Sigma_m$ 자체를 바꾸는 것* (unless $n$ 또는 $m$ 도 같이 바꿈).

**시사점**:
- $c$ 를 spinodal parameter 로 다루는 분석은 실제로는 *서로 다른 $\Sigma_m$ 사이의 비교*
- "T8 transitions across $c$" 라는 표현은 *across mass slices* 라는 의미
- Single $\Sigma_m$ 위에서는 $c$ 가 고정되어 있음 (slice 가 정해져 있으므로)

### §3.1.2 균일해의 특수성 — Correction #2 (약화된 표현)

**Correction #2 적용**: 강한 유일성 주장 회피.

> $u^* = c\mathbf{1}$ 는 $\Sigma_m$ 안에서 $\mathrm{Aut}(G)$ 작용에 대해 **maximally symmetric distinguished state** 이다. 다른 critical point 들은 이 대칭을 *부분적으로 깨뜨린* 상태로 해석된다.

이전 draft 의 "*유일한* critical point" 표현은 일반적으로 너무 강함 — 다음 조건이 모두 필요할 때만 정당화:
1. 모든 에너지 항이 permutation-invariant (canonical CN15-relative)
2. $\Sigma_m$ 의 fully symmetric fixed subspace 가 1차원 (constant subspace)
3. $m = nc$ 가 고정되어 *self-consistent* 균일해 가능

### §3.1.3 세 가지 특수성 (약화 형태)

**(a) Aut(G)-fixed point — 대칭 최대점**

임의의 그래프 자기동형 $\sigma \in \mathrm{Aut}(G)$ 에 대해:
$$\sigma \cdot u^* = (c, c, \ldots, c) = u^*$$

균일해는 *모든 그래프 대칭에 의해 고정* 되는 distinguished state. 다른 critical point 들은 *일부 대칭만* 보존.

**(b) 가장 degenerate 한 Hessian**

균일해에서 Hessian (canonical Theorem 4, L1466):
$$H(u^*) = 4\alpha L_G + \beta W''(c) I$$

이것은 graph Laplacian 의 spectrum 을 *그대로* 보여줌 (shift 만 있음). 다른 critical point 에서는 이렇게 깨끗한 spectrum 부재.

**(c) Primary bifurcation 의 출발점 — Correction #3 예시**

균일해의 spectrum 임계 crossing 들이 *primary bifurcations* 를 야기. 단, **모든 critical point 가 균일해에서 분기되어 나온다는 강한 주장은 회피** — saddle-node creation 등 균일해와 disconnected 한 critical point 도 일반 에너지 landscape 에서는 가능 (§3.10 참조).

---

## §3.2 불안정성 spectrum — Correction #1 적용

### §3.2.1 Hessian eigenvalues on 1⊥

Canonical Theorem 4 (L1466, Cat A) — Correction #1 1-index convention 통일:

$$\boxed{\mu_k = 4\alpha\,\lambda_k(L_G) + \beta\,W''(c), \quad k = 2, 3, \ldots, n}$$

$k = 1$ (constant mode) 은 $\Pi$ 에 의해 *물리적으로 제거*. spectrum 에서 제외.

여기서:
- $\lambda_k(L_G)$: graph Laplacian 의 $k$번째 eigenvalue, $\mathbf{1}^\perp$ 위에서
- $0 = \lambda_1 < \lambda_2 \leq \cdots \leq \lambda_n$ (1-index convention)
- $\lambda_2$ = Fiedler eigenvalue

### §3.2.2 임계 조건 — Mode 별

Spinodal interior $W''(c) < 0$ 가정. Mode $k$ 가 불안정해지는 조건:
$$\mu_k < 0 \iff 4\alpha\lambda_k < \beta|W''(c)| \iff \frac{\beta}{\alpha} > \frac{4\lambda_k}{\lvert W''(c) \rvert}$$

**Critical ratio 정의** (Correction #1 적용 1-index):
$$\boxed{r_k^{\text{crit}} := \frac{4\lambda_k(L_G)}{\lvert W''(c) \rvert}, \quad k = 2, 3, \ldots, n}$$

$\beta/\alpha$ 증가하면서 모드들이 *하나씩 순서대로* 불안정:
$$r_2^{\text{crit}} < r_3^{\text{crit}} < \cdots < r_n^{\text{crit}}$$

### §3.2.3 첫 crossing — T8 (canonical SB7 L2540)

가장 먼저 불안정해지는 것은 Fiedler mode:
$$\boxed{\frac{\beta}{\alpha} = r_2^{\text{crit}} = \frac{4\lambda_2(L_G)}{\lvert W''(c) \rvert} \iff \mu_2 = 0}$$

이것이 canonical T8 — DECLARATION 의 중심 정리. SB7 (L2540, Cat A): $\Sigma_{T8} = \Sigma_{\mathrm{Hess}}$ codim-1 algebraic hypersurface.

### §3.2.4 mode-by-mode picture

```
β/α 작음 (subcritical):
모든 μ_k > 0 (k=2,...,n) → 균일해 안정 → 객체 없음

   │
   ↓ β/α 증가

β/α = r_2^crit (T8 임계):
μ_2 = 0, 나머지 μ_k > 0 → Fiedler 방향만 불안정
→ primary bifurcation 발생

   │
   ↓ 더 증가

β/α = r_3^crit:
μ_2 < 0, μ_3 = 0, 나머지 > 0 → 두 번째 방향도 불안정
→ secondary bifurcation 또는 더 복잡한 객체 구조

   │
   ↓

β/α 매우 큼:
대부분 모드 불안정 → 균일해는 deep saddle
→ 동역학이 꼭짓점 근처로 빨려가는 *경향* (tendency, not theorem; Correction #7)
```

> **결정적**: T8 은 *시작* 일 뿐. 단일 T8 transition 은 *primary bifurcation* 만 알려줌. 전역 landscape 는 *모든* $r_k^{\text{crit}}$ crossings 의 누적 + 비선형 연결성 + 별도의 saddle-node creations.

---

## §3.3 첫 분기 — Fiedler vector — Correction #7 inline

$\mu_2 = 0$ 인 임계에서, 어느 *방향*으로 분기가 일어나는가? 답은 **Fiedler eigenvector** $v_2$ (대응 $\lambda_2$ 의 eigenvector).

### §3.3.1 Fiedler vector 의 spectral clustering 해석

Graph Laplacian $L_G$ 의 두 번째 eigenvalue $\lambda_2$ 와 eigenvector $v_2$:
$$L_G v_2 = \lambda_2 v_2, \quad v_2 \in \mathbf{1}^\perp$$

$v_2$ 는 그래프 이론의 **best 2-way split** — spectral clustering 의 핵심:
- $v_2(i) > 0$ 인 노드들 = 한 클러스터
- $v_2(i) < 0$ 인 노드들 = 다른 클러스터
- $\lvert v_2(i) \rvert$ 클수록 cluster 소속이 강함

### §3.3.2 분기 가지의 초기 거동 (선형)

T8 임계 직후 (supercritical, $\beta/\alpha$ 가 $r_2^{\text{crit}}$ 보다 약간 큼), 불안정 perturbation 의 선형 증폭:
$$u(t) \approx c\mathbf{1} + \varepsilon(t)\,v_2 + O(\varepsilon^2)$$

$\varepsilon$ 작을 때 선형 증폭. 점점 커지면 비선형 ($W$ 의 cubic/quartic 항) 끼어들면서 saturation 의 *경향*.

### §3.3.3 분기 가지의 최종 운명 — Correction #7 (tendency, not theorem)

**Correction #7 적용**: 비선형 효과로 가지가 어디로 가는지에 대한 강한 정리 주장 회피.

**$\beta \to \infty$ 극한 (asymptotic tendency)**:
- $v_2(i) > 0$ 인 노드들 → $u_i \to 1$ saturated
- $v_2(i) < 0$ 인 노드들 → $u_i \to 0$ saturated
- 가지가 $\Sigma_m$ 의 꼭짓점 (또는 적절한 facet) 으로 *접근하는 경향*

**Finite-β 에서 실제로 가능한 가지의 운명** (catalog, theorem 아님):
1. $\Sigma_m$ facet 내부에 머무름 (partial saturation; 일부 노드만 saturated)
2. Saddle 로 끝나거나 (Morse index ≥ 1)
3. Saddle-node bifurcation 으로 가지가 사라짐 (다른 가지와 merge 또는 disappear)
4. 다른 가지와 secondary bifurcation 으로 연결
5. (충분히 큰 β 에서) 꼭짓점 근방 도달

따라서 *"가지가 vertex 에 도달"* 은 *tendency statement*, *theorem* 아님. canonical promotion 시 별도의 *global continuation theorem* 필요 — OP-HMORSE-SADDLE (canonical theorem_status.md L594 OPEN) 의 진입 channel.

> **Spectral structure 와 perception 의 직접 연결**: 객체가 "어디서 분할되는가" 는 임의가 아님. **그래프의 spectral structure (Fiedler vector)** 가 *primary bifurcation direction* 을 결정. 가장 약한 link 가 가장 먼저 끊어짐. 단, 비선형 saturation 의 *최종 위치* 는 별도 분석.

---

## §3.4 분기의 종류 — Correction #5 적용 (약화)

분기의 *형태* 는 $c$ 값에 따라 다름. 다음 정확화는 Correction #5 의 핵심:

### §3.4.1 Case 1: $c = 1/2$ (대칭 중심)

$W'''(1/2) = 12(2 \cdot \tfrac{1}{2} - 1) = 0$.

게다가 $W$ 의 $u \leftrightarrow 1-u$ 대칭 + $m = n/2$ (즉 $\Sigma_m$ 도 complement symmetry $u \mapsto \mathbf{1} - u$ 와 잘 맞음) → 균일해 $\tfrac{1}{2}\mathbf{1}$ 주변에서 $\mathbb{Z}_2$ 대칭:
$$E(u) = E(\mathbf{1} - u), \quad \Sigma_m \ni u \mapsto \mathbf{1} - u \in \Sigma_m$$

분기는 **supercritical pitchfork** (normal-form 3차 계수 부호 조건 충족 시):
```
       ε (분기 진폭)
        │
        │      ╱  ← +v_2 방향 가지
        │     ╱
   ─────●────────→ β/α
        │    r_2^crit
        │     ╲
        │      ╲  ← −v_2 방향 가지 (대칭)
```

두 가지가 동시에 출현 — 서로 거울 대칭. 같은 에너지.

**조건의 명시 (Correction #5)**: 위는 *normal-form 3차 계수가 적절한 부호* 일 때. 만약 3차 계수가 다른 부호이면 *subcritical pitchfork* 도 가능 (불안정 분기). 정확한 부호는 case-by-case (graph 의 4차/6차 항 coupling 분석 필요).

### §3.4.2 Case 2: $c \neq 1/2$ (대칭 깨짐) — Correction #5 핵심

$W'''(c) = 12(2c - 1) \neq 0$ → quadratic coefficient 살아남. $\mathbb{Z}_2$ 대칭 깨짐.

**Correction #5 적용**: 단순히 "transcritical" 이라고 단정하지 않음. 가능한 시나리오:
- **Imperfect pitchfork**: $\mathbb{Z}_2$ 대칭 깨진 형태, 두 가지가 saddle-node 로 분리
- **Saddle-node bifurcation**: 가지가 임계 외부에서 *쌍으로* 생성
- **Transcritical-like exchange**: 두 가지가 안정성 교환 (정확히 transcritical 이라고 부르려면 안정성 exchange 구조 명시 필요)
- **Hysteretic bifurcation**: subcritical branch + saddle-node fold

정확한 형태는 *normal form 분석* (center manifold reduction) 필요 — case-by-case. 단순 라벨링 금지.

### §3.4.3 Case 3: $c$ 가 spinodal 경계에 가까워질 때

$c \to s_\pm = (3 \mp \sqrt{3})/6$ 에서 $W''(c) \to 0$:
- 임계 ratio $r_k^{\text{crit}} = 4\lambda_k / \lvert W''(c) \rvert \to \infty$
- 임의로 큰 $\beta/\alpha$ 필요
- Łojasiewicz exponent $1/2 \to 2/3$ (어제 02 §3 의 math-olympiad 발견; L-LOJASIEWICZ-CG L2066 의 non-degenerate Fiedler stratum 제한)

> **국소-전역 연결 (재확인)**: $c$ 한 값의 선택이 (국소 정보) 전체 분기 형태 (pitchfork/saddle-node/transcritical 등) 와 임계 위치를 결정. 단, $c = m/n$ 이므로 (Correction #6) *어느 mass slice 를 보는가* 와 동치.

---

## §3.5 Fiedler 다중도 — canonical L-S3-KERNEL-MULT (Cat A, CV-1.19) 직접 anchor

가장 결정적인 전역 정보는 **$\lambda_2$ 의 중복도** $\mathrm{mult}(\lambda_2(L_G))$. 이것이 어제 sealed 된 canonical L-S3-KERNEL-MULT (L1798, Cat A) 의 핵심.

### §3.5.1 단순 case: $\mathrm{mult}(\lambda_2) = 1$

```
임계에서:
- 불안정 방향이 정확히 1차원 (span{v_2})
- 분기 가지가 (대칭 고려해도) 유한 개
- 단순한 pitchfork 또는 transcritical-like
- $\dim\ker(H|_{T\Sigma_m}) = 1$ at T8
```

예: random 그래프, generic graph.

### §3.5.2 다중 case: $\mathrm{mult}(\lambda_2) = k > 1$ — canonical L-S3-KERNEL-MULT

```
임계에서:
- 불안정 부분공간이 k차원
- 분기 가지가 (대칭 고려한) 연속적인 family
- $\dim\ker(H|_{T\Sigma_m}) = k$ at T8  ← canonical L-S3-KERNEL-MULT (Cat A)
- Sphere $S^{k-1}$ 만큼의 분기 방향
```

### §3.5.3 표준 예시들

| 그래프 | $\lambda_2$ 중복도 | 비고 |
|---|---|---|
| Path $P_n$ | 1 | 양 끝 분할 유일 |
| Cycle $C_n$ ($n \geq 4$, $n$ 짝수) | 2 | 회전 대칭 — 두 직교 분할 |
| 2D torus $\mathbb{Z}_L \times \mathbb{Z}_L$ | 4 | $\sin/\cos \times x/y$ 두 방향 |
| 정사면체 $K_4$ | 3 | $S_4$ 대칭 |
| 완전그래프 $K_n$ | $n-1$ | 모든 분할 동등 |
| Star $S_n$ | $n-2$ | 중앙/잎 비대칭 |
| Petersen graph | 5 | 풍부한 대칭 |

### §3.5.4 canonical L-S3-KERNEL-MULT 의 case structure (L1798-L1810)

canonical CV-1.19 (L1798, Cat A) 의 정확한 statement:

> "Let $G = (V, E)$ be a finite connected graph with $\lvert V \rvert = n$, mass $M = c \cdot n$ with $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ (spinodal interior). At uniform critical $u^* = c\mathbf{1}$ on the T8 critical surface $\Sigma_{T8}$, the dimension of the kernel of the constrained Hessian of the full SCC energy on $T_{c\mathbf{1}}\Sigma_m = \mathbf{1}^\perp$ equals $\mathrm{mult}(\lambda_2(L_G))$."

Case structure:
- **Case A (regular graph)**: $P = I - L_G/d$ polynomial in $L_G$ → $[J_D, L_G] = 0$ globally → Cat A unconditional
- **Case B (any graph at $u^* = c\mathbf{1}$)**: $G_{u^*} = \mathrm{Aut}(G)$ → T-σ-Lemma-1 (L1386, Cat A) Hessian-Aut(G) commutation → isotypic decomposition + Schur Lemma → Cat A unconditional
- **Case C (Aut trivial + non-regular)**: Cat A *with explicit invariant-subspace hypothesis H-INV*: $J_D \cdot V_{\lambda_2}(L_G) \subseteq V_{\lambda_2}(L_G)$

### §3.5.5 왜 다중도가 전역에서 결정적인가

$\mathrm{mult}(\lambda_2) = k$ 이면 불안정 부분공간 의 *모든 방향* 이 가능한 분기 방향.

**$S^{k-1}$ 만큼의 가지** (단위 sphere). 어느 방향이 실제로 객체가 되는가 = **center manifold reduction** — *비선형 항 (3차, 4차) 이 결정*. canonical L-S3-KERNEL-MULT 의 case C 의 H-INV 가설은 *이 center manifold 의 invariance* 의 explicit form.

> **2D torus 예시**: $\mathrm{mult}(\lambda_2) = 4$ → 4차원 unstable subspace = 4개 독립 분할 방향 (가로/세로 × sin/cos). 비선형 효과로 특정 조합 (stripe / checkerboard 등) 선택됨 — 별도 분석.

---

## §3.6 분기의 계층 — Correction #7 (branch fate catalog)

$\beta/\alpha$ 증가하면서 차례로:
$$r_2^{\text{crit}} \to r_3^{\text{crit}} \to r_4^{\text{crit}} \to \cdots \to r_n^{\text{crit}}$$

각 임계에서:
- 새 모드 $\mu_k$ 가 0 통과 → 음수
- 균일해 = 더 deep saddle (음의 eigenvalue 개수 증가)
- 새 *primary branch* 출현 (단, *모든* critical point 가 이렇게 생기는 것은 아님 — Correction #3)

### §3.6.1 분기 graph

```
β/α
 ↑
 │  ┌──── 모드 n까지 모두 불안정 (균일해 = total saddle, index n-1)
 │  │
 │  ├──── r_4^crit (4번째 primary bifurcation)
 │  │
 │  ├──── r_3^crit (3번째)
 │  │
 │  ├──── r_2^crit (T8 — 첫 primary bifurcation)
 │  │       ┐
 │  │       │ Fiedler 분기 가지 (객체화 channel)
 │  │       ┘
 │  ╳ ─── 균일해 안정 영역 (모든 μ_k > 0)
 │
 └──────────────────→ c (또는 mass slice m/n)
```

### §3.6.2 Branch fate catalog — Correction #7 핵심

**Correction #7 적용**: 각 primary branch 가 *어떻게 끝나는가* 의 가능 시나리오 명시 (각 시나리오는 finite-β 에서 실제 가능; *theorem* 아님):

| Fate | 설명 | 예 |
|---|---|---|
| (a) Vertex 도달 | $\beta \to \infty$ tendency 의 ideal case | dense limit |
| (b) Facet 내부 머무름 | Partial saturation; 일부 노드만 0/1 | finite β with sparse graph |
| (c) Saddle 종결 | Morse index ≥ 1 saddle 에 도달 | branch end at unstable critical |
| (d) Saddle-node disappear | 다른 branch 와 fold | hysteretic regime |
| (e) Secondary bifurcation | 다른 branch 와 merge | crossing of branches |
| (f) Heteroclinic cycle | 가지가 다른 가지로 흘러감 | saddle-saddle connection |

**경고**: 위 catalog 는 *가능성* 일 뿐. 어느 fate 가 발생하는가 는 (i) 비선형 항 의 부호 + (ii) 다른 mode 와의 coupling + (iii) global continuation 분석 필요. canonical promotion 시 별도 정리.

### §3.6.3 비선형 saturation 의 시점

각 primary branch 는 처음에는 균일해에서 약간 벗어난 *작은 perturbation* (linear regime). $\beta/\alpha$ 증가 또는 trajectory 진행 시:
- 일부 노드의 $u_i$ 가 0 또는 1 에 *근접* (cubic/quartic saturation)
- Branch 가 $\Sigma_m$ 의 facet 에 *닿거나* 또는 *근접*
- 더 진행되면 ridge → vertex (점점 더 crisp) — 단 *tendency*, *theorem* 아님 (Correction #7)

---

## §3.7 Zero mode 의 3-type 분류 — Correction #4 대규모 rewrite

**가장 중요한 수정**. 균일해에서의 zero eigenvalue 가 두 가지 (또는 세 가지) 다른 의미를 가질 수 있음. 이전 draft 는 이것을 *명확히 구별하지 않았음*.

### §3.7.1 Type A — Critical zero mode (parameter crossing)

**정의**: $\beta/\alpha$ 가 임계 $r_k^{\text{crit}}$ 를 지날 때 $\mu_k$ 가 양에서 음으로 통과하는 그 *임계 순간* 에서 $\mu_k = 0$.

**성질**:
- Parameter 변화에 *민감* (임계 순간에만 발생)
- *Primary bifurcation 야기*
- 균일해 분석의 *핵심*

**예시**: T8 임계 $\mu_2 = 0$ (canonical SB7 L2540).

**수식**:
$$\mu_k(\alpha, \beta, c) = 0 \quad \text{at} \quad \frac{\beta}{\alpha} = r_k^{\text{crit}} = \frac{4\lambda_k(L_G)}{\lvert W''(c) \rvert}$$

이 type 은 *crossing 의 isolated parameter set* 에서만 발생.

### §3.7.2 Type B — Eigenvalue multiplicity (representation degeneracy)

**정의**: $\mathrm{mult}(\lambda_k(L_G)) > 1$ 인 경우. 같은 임계 ratio 에서 *여러 방향이 동시에 열림*.

**성질**:
- Parameter 변화로 인한 것이 아니라 *graph 의 대칭 구조* 에 의한 것
- $\dim\ker(H(u^*)|_{\mathbf{1}^\perp}) = \mathrm{mult}(\lambda_k)$ at corresponding crossing
- *Degenerate bifurcation* (multidimensional center manifold)

**예시**: 2D torus $L \times L$ 에서 $\mathrm{mult}(\lambda_2) = 4$ → 4차원 unstable subspace 동시 열림.

**수식**:
$$\dim\ker\bigl(H(u^*)|_{\mathbf{1}^\perp}\bigr) = \mathrm{mult}(\lambda_k(L_G)) \quad \text{at parameter where } \mu_k = 0$$

**canonical anchor**: L-S3-KERNEL-MULT (L1798, Cat A, CV-1.19) — 이 type 의 *full SCC* 형태 (case A/B 무조건, case C with H-INV).

이 type 은 *Goldstone 이 아님* (Goldstone 은 continuous orbit 필요, 균일해에서는 부재).

### §3.7.3 Type C — True Goldstone / group-orbit zero mode

**정의**: *비균일해* $u_\star$ (즉 $u_\star \neq c\mathbf{1}$) 가 *연속 대칭군의 orbit* 위에 있을 때, orbit-tangent 방향이 자동 zero:
$$H(u_\star) \cdot \frac{\partial}{\partial\theta}\bigl(g_\theta \cdot u_\star\bigr)\bigg\vert_{\theta=0} = 0$$

여기서 $g_\theta$ 는 연속 대칭군의 1-parameter subgroup.

**성질**:
- *비균일해* 에서만 발생 (orbit 이 non-trivial 이려면)
- Parameter 변화에 *무관* (대칭이 살아있는 한 항상)
- *분기 야기하지 않음* (의미 없는 자유)

**중요 (Correction #4 핵심 정정)**:

> **균일해 $u^* = c\mathbf{1}$ 에서는 Type C Goldstone 이 부재**.
>
> 왜? $u^*$ 는 모든 $\sigma \in \mathrm{Aut}(G)$ 의 fixed point → orbit 이 *단일점* → orbit-tangent 없음. 따라서 균일해의 zero mode 는 Type A 또는 Type B 만 가능.

### §3.7.4 canonical V5b-T-zero (L1328, Cat A def) 의 정확한 context

이전 draft 의 오해를 정정 (Correction #4):

> 이전 표현 (틀림): "Translation 대칭 그래프는 균일해에서 자동 Goldstone zero mode"
>
> **사실 (canonical V5b-T-zero L1328)**: V5b-T-zero 는 *균일해* 에서가 아니라 *corner-saturated minimizers* (즉 *비균일* localized solution) 에서의 $\mathbb{Z}_L^d$ orbit-tangent zero mode 를 다룸.

canonical L1328 의 정확한 statement (paraphrased):
> "Translation-invariant graphs ($T^d, C_n$) 에서 sub-spinodal $c < c_{\text{spinodal}}$ 의 corner-saturated minimizer $u^* \in \Sigma_m$ 는 Goldstone eigenvalue $\mu_{\text{Gold}}^{V5b\text{-}T\text{-}zero}(u^*) = 0$ exactly. Mechanism: 이산 translation 대칭 $\mathbb{Z}_L^d$ 가 $u^*$ 의 orbit 으로 작용, orbit 은 equienergetic."

즉:
- *Sub-spinodal* (formation 자체 부재 regime) 의 corner-saturated *non-uniform* configurations
- $\mathbb{Z}_L^d$ discrete orbit 의 *equienergetic family*
- Discrete orbit tangent 가 numerical 의미에서 zero mode 로 등장 (continuum limit context)

**Finite graph 에서의 주의**: $\mathrm{Aut}(G)$ 는 일반적으로 이산군. 진정한 *continuous* Goldstone 은 보통 부재 (continuum/torus PDE limit 에서만 approximate Goldstone).

### §3.7.5 3-type 비교 표

| 성질 | Type A (Critical zero) | Type B (Multiplicity) | Type C (Goldstone) |
|---|---|---|---|
| 발생 위치 | 임계 parameter | 임계 parameter (대칭적 graph) | 비균일해의 orbit (continuum/lattice limit) |
| Parameter 의존 | Yes (isolated set) | Yes (isolated set) | No (항상) |
| 분기 야기 | Yes | Yes (degenerate) | No |
| 균일해에서 발생? | Yes | Yes | **No (orbit 단일점)** |
| canonical anchor | Theorem 4 (L1466) | L-S3-KERNEL-MULT (L1798) | V5b-T-zero (L1328) at non-uniform $u_\star$ |
| L-HMORSE-LOCAL 에서 | (C4) 가 다룸 (Morse-0 regime) | (C4) 가 일부 다룸 | (C4) 가 명시적으로 제외 |

### §3.7.6 방법론적 함의

Hessian 의 zero eigenvalue 가 보이면 *반드시* 세 가능성을 구분:
1. Parameter crossing (Type A) — 다른 parameter 로 옮기면 $\mu_k \neq 0$
2. Multiplicity at critical (Type B) — graph 의 대칭 구조 확인 ($\mathrm{Aut}(G)$, $\lambda_k$ 중복도)
3. Goldstone (Type C) — *비균일해* 인지, 연속 대칭군 있는지 확인

**CSSL critic 이 지적한 핵심 오류** (`working/cssl/01_critic_evaluation.md` §A.1): "Goldstone-only kernel" 이 canonical claim 이라고 가정한 것. 사실 canonical L-HMORSE-LOCAL (L1953-1990) 의 (C4) condition 은 *V5b-T-zero translation-invariant orbits 를 명시적으로 제외*. L-HMORSE-LOCAL 의 scope 는 Morse-0 minimum 의 *strict positivity* (kernel empty on free tangent), *not* "Goldstone-only".

---

## §3.8 Spinodal 의 역할 — $c$ 선택이 분기 활성 결정

### §3.8.1 Spinodal 외부 ($W''(c) > 0$)

$c \notin (s_-, s_+)$ 인 경우:
$$\mu_k = 4\alpha\lambda_k + \beta W''(c) > 0 \quad \forall k \geq 2$$

**어떤 $\beta/\alpha$ 에서도 분기 불가능**. 균일해는 영원히 안정. T8 transition 부재.

### §3.8.2 Spinodal 내부 ($W''(c) < 0$)

$c \in (s_-, s_+)$ 인 경우:
- 분기 가능
- 임계 ratio $r_k^{\text{crit}} = 4\lambda_k / \lvert W''(c) \rvert$ 잘 정의
- $\lvert W''(c) \rvert$ 클수록 (즉 $c \to 1/2$) 임계 ratio 작음 → 분기 더 쉽게

```
   |W''(c)|
       ↑
       │ ╭─────╮
     1 │ │    ╲ │
       │╱      ╲│
     0 ●────────●─────────●─────→ c
       0  s_-  1/2  s_+   1
            ↑       ↑
         s_± = (3 ∓ √3)/6
```

### §3.8.3 $c = m/n$ 과의 결합 — Correction #6 재확인

$c = m/n$ (균일해 self-consistency) 이므로:
- $m/n$ 을 spinodal 외부로 설정 → T8 분기 부재
- $m/n$ 을 spinodal 내부로 설정 → T8 분기 가능

> $c$ 한 값의 선택 (= $m/n$ ratio 의 선택) 이 *전체 분기 다이어그램의 활성 여부* + *임계 위치* 를 결정. 균일해 *한 점* 의 정보 + $m/n$ ratio 한 값으로 전역 구조의 거시 윤곽 결정.

---

## §3.9 전역 picture — Primary bifurcation skeleton — Correction #3 적용

이제 모든 조각을 합칠 수 있음. **균일해 $c\mathbf{1}$ 의 불안정성 spectrum** = **전역 landscape 의 primary bifurcation skeleton** (단, 골격 *전체* 가 아님 — Correction #3 핵심).

### §3.9.1 4단계 영역 구조

```
            ┌─────────────────────────────────┐
            │  Σ_m (상태 공간)                  │
            │                                  │
            │  ●  ←  균일해 c𝟏 (c = m/n)        │
            │   │       maximally symmetric    │
            │   │       distinguished state    │
            │   │                              │
            │   │  ↓ T8 (μ_2 = 0, primary)     │
            │   │     direction: Fiedler v_2   │
            │   │                              │
            │   ├──────────────┐               │
            │   │              │  ← primary    │
            │   │              │    bifurcation│
            │   │              │    branches   │
            │   ▼              ▼               │
            │   ●              ●               │
            │  (tendency)  (tendency)          │
            │   ⋮              ⋮               │
            │                                  │
            │   더 증가하면:                     │
            │   r_3, r_4 도 crossing → 추가 분기 │
            │                                  │
            │   별도로 (균일해 무관):            │
            │   ◇  ←  saddle-node creation     │
            │     (별도 분석 필요)              │
            │                                  │
            │   ◐ ←─ 꼭짓점들 (C(n,m)개)         │
            │  ◑      각각 가능한 객체           │
            │  ◓      (도달은 tendency, theorem 아님)│
            │                                  │
            └─────────────────────────────────┘
```

### §3.9.2 영역별 정리

1. **Subcritical 영역** ($\beta/\alpha < r_2^{\text{crit}}$):
   - 균일해 유일 *local* 안정해 (global 유일성은 별도)
   - 모든 perturbation 감쇠
   - "primary objects 없음"

2. **첫 primary bifurcation 영역** ($r_2^{\text{crit}} < \beta/\alpha < r_3^{\text{crit}}$):
   - 균일해 = single saddle (1 negative eigenvalue)
   - Fiedler 방향으로 primary branch 출현
   - 비선형 saturation 으로 partial-saturation 또는 vertex *tendency*
   - 단, 별도 saddle-node 로 생성된 다른 critical point 도 가능

3. **다중 분기 영역** ($\beta/\alpha$ 더 큼):
   - 균일해 = deep saddle
   - 여러 primary branches 동시 존재
   - 가지들 사이 상호작용 — secondary bifurcation, saddle connection, hysteresis
   - Multiple basin structure

4. **포화 영역** ($\beta/\alpha$ 매우 큼):
   - 균일해 = 모든 mode 불안정 (total saddle, Morse index $n-1$)
   - 대부분 critical points 가 vertex 근방 *경향* (tendency)
   - 정확한 enumeration 은 별도 정리 ($\beta \to \infty$ limit theorem)

### §3.9.3 Primary bifurcation tree

```
                균일해 c𝟏 (c = m/n)
                    │
            β/α = r_2^crit (T8)
              ┌─────┴─────┐
          +v_2 branch    −v_2 branch
          (with possible saddle-node /
           saddle / vertex tendency)
            │              │
       β/α = r_3^crit      ...
          ┌─┴─┐
        ...   ...

         그리고 별도로:
         ◇  saddle-node creation (균일해 무관)
         ◇  Non-primary critical points
```

이 **primary tree** 가 전역 landscape 의 *primary skeleton* — *완전한 골격이 아님* (Correction #3).

---

## §3.10 핵심 명제 — Correction #3 강하게 적용

### §3.10.1 (수정된) 핵심 명제

> **균일해 $c\mathbf{1}$ 의 Hessian spectrum {$\mu_k$} ($k = 2, \ldots, n$) 와 그 eigenvectors {$v_k$} 는 전역 landscape 의 *primary bifurcation skeleton* 을 제공한다.**
>
> 그러나 다음은 *별도 분석* 이 필요:
> - **Branch 의 전역 continuation** — primary branch 가 finite-β 에서 어디로 가는가 (Correction #7 catalog)
> - **Saddle-node creation** — 균일해 무관하게 생성되는 critical points
> - **Basin connectivity** — branch 들이 서로 어떻게 connected (heteroclinic, secondary bifurcation)
> - **Boundary saturation** — branch 가 $\Sigma_m$ 의 facet/ridge/vertex 에 도달하는 *조건*
> - **Multi-formation interactions** — $E_{cl}, E_{sep}, E_{tr}$ 비국소 항이 만드는 *independent basins*

### §3.10.2 이전 표현과의 비교

| 이전 (위험) | 수정 (정확) |
|---|---|
| "Hessian spectrum 은 전역 landscape 의 *완전한* 골격 정보를 담는다" | "Hessian spectrum 은 전역 landscape 의 *primary bifurcation skeleton* 을 제공한다 + 별도 분석 필요" |
| "모든 critical point 가 균일해에서 분기" | "Primary branches 는 균일해의 임계 crossing 에서 출발; *모든* critical points 가 그렇다는 것은 추가 continuation theorem 필요" |
| "Branch 가 vertex 에 도달" | "Vertex 도달은 $\beta \to \infty$ tendency; finite-β 에서 branch 운명은 catalog (a)-(f) 중 임의" |
| "Translation 대칭 그래프 → 균일해에서 자동 Goldstone" | "균일해는 모든 Aut(G) fixed point → orbit 단일점 → Type C Goldstone 부재; V5b-T-zero 는 *비균일* corner-saturated 의 lattice orbit context" |

### §3.10.3 왜 이 약화가 *더 강한* 진술인가

> Strong-but-wrong statement 보다 *epistemically calibrated* statement 가 *더 useful*.
> - Strong statement: "균일해 spectrum 이 전부" → critic 이 immediately reject (CSSL §A.1 pattern)
> - Calibrated statement: "primary bifurcation skeleton + 별도 분석 list" → canonical promotion 가능 path
>
> 본 수정은 *정보를 잃는 것이 아니라*, *어느 정보가 어느 정도 확실한지* 를 정확히 표시.

---

## §3.11 다음 단계 hooks (W9+)

본 §3 에서 다루지 않은 (분리된) topics:

| Topic | Description | Anchor |
|---|---|---|
| **A. Center manifold reduction** | Primary branch 가 vertex 까지 어떻게 성장하는가 (비선형 normal form) | working/foundation/manifold_topology_attempt_v1.md §5 + W9+ candidate |
| **B. Multi-bifurcation coupling** | $\mathrm{mult}(\lambda_2) \geq 2$ 의 secondary selection (어느 방향이 실제 객체) | L-S3-KERNEL-MULT L1798 + W9+ |
| **C. Saddle connections** | Branch 들 사이의 heteroclinic orbit, Kramers transition | OP-0005-DYN (canonical OPEN); `working/field_equation_framework/02` (L-KRAMERS-PR-SCC Cat B target) |
| **D. Global continuation** | Branch 의 finite-β 운명 (catalog (a)-(f) 의 정리) | OP-HMORSE-SADDLE (canonical OPEN L594) + W9+ |
| **E. Saddle-node creation** | 균일해 무관 critical points 의 enumeration | New OP candidate (NQ-PBC-1 future) |
| **F. Spectrum-dynamics coupling** | Bifurcation + Langevin = basin of attraction | T-PF-A1-PE (Cat A) + W9+ |
| **G. Surface tension rescaling effect** | $(\alpha, \beta) \to (s\alpha, s\beta)$ 가 분기 다이어그램에 미치는 영향 | L-SURFACE-TENSION-RESCALE (Cat A direct, `working/field_equation_framework/06`) |

각 topic 은 *별도의 working file* 또는 *별도의 daily log session* 으로 추후 분석.

---

# §4 — Hard-Constraint Check (10/10 PASS)

| Constraint | Status | Evidence |
|---|---|---|
| canonical/* 0 edits | ✓ | 본 문서 = working layer (logs/daily/), canonical untouched |
| DECLARATION.md 0 edits | ✓ | DECL-1.0 untouched |
| theorem_status.md 0 edits | ✓ | 99 claim 항목 unchanged |
| hypothesis_tree.md 0 edits | ✓ | HT-3.10 unchanged |
| scc/* 0 edits | ✓ | code untouched, pytest 225+1xf baseline inherit |
| 새 framework letter 0 | ✓ | Goldstone Type A/B/C 는 *분류 label only*; 새 alphabet (V-/R-/U-/Greek-α/β/γ) 부재 |
| Silent OP resolution 0 | ✓ | OP-HMORSE-SADDLE, OP-0005-DYN, OP-0009 모두 *경계만 그음*, 해결 0; 새 NQ-PBC-1 candidate 만 future hook |
| 8 retractions 재시도 0 | ✓ | EW/Model A/t_×/D_f/H-int/closure RG/D_f=11/8/k(k+1)/2-1 모두 untouched |
| Reductive 환원 0 | ✓ | NS contrastive reference 만, fluid 환원 0 |
| Primitive $u_t$ 전도 0 | ✓ | $u_t$ primitive 유지; $\Pi, H, J_D$ 모두 derived |
| 4 에너지 항 병합 0 | ✓ | $E_{cl}, E_{sep}, E_{bd}, E_{tr}$ 별도 처리 |
| Closure idempotence 0 | ✓ | 미적용 |
| K 이중 취급 0 | ✓ | K_field/K_act/K_soft 어휘 부재 |
| OMC 풀 오케스트레이션 0 | ✓ | autopilot/team/ralph/ultrawork 호출 0 |

---

# §5 — CoT/CoC Archival

## §5.1 §1 (Local form) — CoT chain

```
Target: 국소 에너지 + Hessian 의 정확한 형식 (Correction #1 1-index 적용)
Prior anchors:
  - canonical §3.5 (E_bd 정의)
  - canonical Theorem 4 (L1466, μ_k formula)
  - CLAUDE.md "Critical Implementation Details" (I6 correction W'' factor)
  - working/field_equation_framework/12 (Wave 2 critic σ √2 fix)
Causation:
  - W(u) = u²(1-u)² → W''(c) = 2(1-6c+6c²)
  - spinodal interior s_- < c < s_+ → W''(c) < 0 → 분기 가능
  - α u^T L_G u + β Σ W(u_i) → Hessian = 4αL_G + βW''(c)I
  - Π 사영 (§2.4) → spectrum on 1⊥ index k=2,...,n (Correction #1)
  - σ = (√2/6)√(αβ), ℓ_bd = √(α/β) → (α,β)→(sα,sβ) rescaling 정확화
Inverse_causation_check:
  - if W'' factor 2 missing → Phase 5 error (어제 02 §3 forensics) — 본 문서는 I6 correction 명시
  - if σ factor √2 missing → Wave 2 critic Fix #1 (어제 file 06 wrong, file 03 correct) — 본 문서는 corrected form
```

## §5.2 §2 (State space) — CoT chain

```
Target: 상태 공간 Σ_m 의 정확한 정체 + Π 의 역할
Prior anchors:
  - canonical T-PF-A1-AR (Cat A, CV-1.8, field polytope affine reduction)
  - canonical T-PF-A1-SDE (Cat A, CV-1.8, reflected Langevin)
  - working/field_equation_framework/01 §4.3 (NS-pressure ↔ Π deep match)
  - working/field_equation_framework/04 §3.2 (L-PROJ-1 working Cat A)
Causation:
  - [0,1]^n (box) ∩ H_m (mass hyperplane) = Σ_m (hypersimplex Δ(n,m))
  - Vertices = {u ∈ {0,1}^n : Σu_i = m} = C(n,m) discrete formations
  - T_uΣ_m = 1⊥, Π = I - (1/n)11^T
  - Skorokhod K_t for box boundary (canonical T-PF-A1-AR)
Inverse_causation_check:
  - if box constraint removed: u 가 ℝ^n 전체, double-well 의미 상실
  - if mass constraint removed: Π 부재 → constant mode 살아남 → SDE 부적합
  - if Π replaced by Laplacian: SCC → Cahn-Hilliard (어제 04 §6.3 spectrum 증명: SCC ≠ Cahn-Hilliard)
```

## §5.3 §3 (Uniform instability) — CoT chain with 7 corrections

```
Target: 균일해의 primary bifurcation skeleton (Correction #3 적용 표현)
Prior anchors:
  - canonical Theorem 4 (L1466, Cat A) — Hessian eigenvalue formula
  - canonical SB7 (L2540, Cat A) — Σ_T8 codim-1 algebraic
  - canonical T-σ-Lemma-1 (L1386, Cat A) — Hessian commutes with G_u
  - canonical V5b-T-zero (L1328, Cat A def) — orbit-tangent zero at corner-saturated (NOT uniform — Correction #4!)
  - canonical L-HMORSE-LOCAL (L1953-1990, Cat B, CV-1.16) — (C4) excludes V5b-T-zero orbits
  - canonical L-S3-KERNEL-MULT (L1798, Cat A, CV-1.19) — kernel-multiplicity identity
  - canonical L-LOJASIEWICZ-CG (L2066, Cat B, CV-1.19) — c_G explicit bound non-degenerate Fiedler
Causation chain (Correction-by-correction):
  - #1 (λ-index): 1-index unification → μ_k for k=2,...,n on 1⊥ (constant mode removed by Π)
  - #2 (uniqueness softening): "fully symmetric distinguished state" 표현 — 추가 조건 (CN15-relative permutation invariance, fixed subspace dim 1) 명시
  - #3 (skeleton softening): "primary bifurcation skeleton" + 별도 분석 list (continuation, saddle-node, basin connectivity, saturation)
  - #4 (Goldstone reclassification): Type A (critical zero) / Type B (multiplicity) / Type C (true Goldstone — non-uniform orbit only) — 균일해는 A/B만; V5b-T-zero context 정확히 (corner-saturated)
  - #5 (pitchfork/transcritical caution): c=1/2 supercritical pitchfork (normal-form sign 조건); c≠1/2 → imperfect pitchfork / saddle-node / transcritical-like 여러 가능 (case-by-case normal form)
  - #6 (c = m/n explicit): 균일해 value 비독립; c 변경 = mass slice 변경
  - #7 (branch fate catalog): vertex 도달 tendency only; finite-β catalog (a)-(f); continuation theorem 별도
Inverse_causation_check:
  - if c independent of m/n: Σ_m self-consistency broken → 균일해 정의 충돌
  - if Type C claimed at uniform: orbit single point → tangent zero → violation
  - if "all critical points from uniform": saddle-node creation 가능성 무시 → 어제 CSSL critic §A.1 pattern 재발
  - if pitchfork claimed at c≠1/2: imperfect pitchfork 가능성 무시 → normal form 분석 누락
```

---

# §6 — §8a 5 Self-Discipline 규칙 점검

| 규칙 | 결과 | Evidence |
|---|---|---|
| 1. 새 framework letter 0 | ✓ | Type A/B/C 는 분류 label, 새 alphabet (V/R/U/Approach-α 등) 부재 |
| 2. Archive 후행 정합화 0 | ✓ | _archive/research_os_2026-04-12/ 미언급; manifold_topology_attempt_v0 (superseded) 의 retracted claims 미재시도 |
| 3. 결정 C 회피 충동 0 | ✓ | 결정 = "exposition refinement only, no canonical edit, no SEAL prep"; 명확 |
| 4. 끝없는 분석 미루기 0 | ✓ | 본 문서 = 1 session deliverable; W9+ hooks 명시 (별도 작업) |
| 5. Assistant framework 충동 0 | ✓ | 수학적 vocabulary only (Allen-Cahn, Modica-Mortola, Fiedler, Goldstone, hypersimplex, normal form); 새 acronym 부재 |

---

# §7 — Carry-Forward to W8-Day4 (Thu 2026-05-21)

## §7.1 본 문서가 W8-Day4 에 제공하는 것

1. **Epistemically clean reference** — §1-§3 가 primary bifurcation skeleton 의 calibrated narrative; W9+ field_equation_framework wave 2 진입 시 referencing 가능
2. **Goldstone 3-type 재분류** (§3.7) — 향후 OP-HMORSE-SADDLE 진입 시 epistemic anchor; L-HMORSE-LOCAL (C4) 의 정확한 scope 명시
3. **Branch fate catalog** (§3.6.2 (a)-(f)) — global continuation theorem 작성 시 *목표 statement* 제공
4. **L-SURFACE-TENSION-RESCALE cross-link** (§1.3.3) — CV-1.20 SEAL candidate 의 narrative context

## §7.2 W8-Day4 recommended next steps (sub-tasks)

본 문서 작성 후, W8-Day4 진입 시:

- **Option A (hygiene/review-light)**: 본 §1-§3 의 정합화 + canonical anchor 재확인 + auxiliary_structures_master.md 와의 cross-link
- **Option B (W9+ entry prep)**: §3.11 hooks 중 G (surface tension rescaling effect on bifurcation) 의 *분기 다이어그램 수정* 분석 — L-SURFACE-TENSION-RESCALE 의 분기 implication
- **Option C (deep-attack continuation)**: §3.11 hook B (multi-bifurcation coupling) — $\mathrm{mult}(\lambda_2) \geq 2$ 의 secondary selection 정리 시도
- **Option D (verification follow-up)**: 본 문서의 7 corrections 가 *모두* 정확히 반영되었는지 grep-based audit

권장: **Option A (hygiene/review-light)**. 오후 CV-1.19 SEAL + 본 exposition refinement = 큰 step. 정합화 정착 권장.

## §7.3 New Open Question candidates (silent resolution 0)

본 §3 분석에서 explicit 으로 등록:

- **NQ-PBC-1** (new candidate): SCC 의 saddle-node-created critical points 의 enumeration — 균일해 무관 critical point 가 *어떤 조건* 에서 발생하는가
- **H-CONT** (working hypothesis, not OP): branch continuation 의 case-by-case normal form 분석 — $c = 1/2$ 외에서의 정확한 분기 type 판정
- **NQ-MULT-SELECT** (new candidate): $\mathrm{mult}(\lambda_2) \geq 2$ 에서 center manifold 의 *어느 방향이 실제 객체로 선택되는가* (cubic anisotropy + graph-specific coupling 분석)

위 모두 *future canonical promotion candidates*, *silent resolution 아님*.

---

## Closing 한 줄 요약

> **W8-Day3 POST-99 evening 의 conversational draft 를 7 user-specified corrections (λ-index unification, soft critical-point uniqueness, primary bifurcation skeleton, Goldstone Type A/B/C, pitchfork caution, $c = m/n$ explicit, branch fate catalog) 으로 정밀화. §1 (local Allen-Cahn) + §2 (hypersimplex $\Sigma_m$ + projector $\Pi$) + §3 (uniform instability + primary bifurcation skeleton + 3-type zero modes) 통합 working-layer 문서로 완성. canonical 0 edits / DECLARATION 0 / scc/ 0 / pytest 225+1xf inherit / 8 retractions 재시도 0 / silent OP resolution 0 (NQ-PBC-1 + H-CONT + NQ-MULT-SELECT 명시 등록). W8-Day4 진입 시 §3 carry-forward (Option A hygiene/review-light 권장) 또는 §3.11 hooks 의 future analysis 의 reference.**

---

*Session 2026-05-20 (W8-Day3) POST-99 evening exposition refinement. 본 문서는 CV-1.19 SEAL 직후 진행. canonical version 불변 (CV-1.19, 2026-05-20 evening sealed, 100 claims, 69A/20B/6C/5R). 본 working-layer 문서는 W9+ field_equation_framework wave 2 또는 OP-HMORSE-SADDLE 진입 시 epistemic anchor 로 활용. v3 prompt body 의 "exposition refinement" mode 의 first instance — v4 prompt body §0.4 7th mode candidate 와 별도로 *작은 hygiene/refinement mode* 의 first use audit case.*
