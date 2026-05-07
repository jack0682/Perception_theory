---
id: HT-3.0
type: theory/hypothesis-tree
version: 3.0
created: 2026-05-07
last_updated: 2026-05-07
status: active
description: SCC 이론 가설 의존성 트리. HT-3.0: 블록을 수학적 주제에서 인식론적 질문 기준으로 재편. 에이전트 세션 최적화 구조 유지 (즉시 타겟 → 요약 → 상세).
---

# SCC Hypothesis Tree (HT-3.0)

---

## 세션 시작 / 즉시 타겟

**먼저 읽기:** `THEORY/canonical/DECLARATION.md` — 이론의 중심축 (2분 분량)

**지금 공략 가능 (Phase 1, unblocked):**

> **H-SINK** — Sinkhorn-Lipschitz (S-B2)
> Bigot-Cazelles-Papadakis 적용: SCC 비용 클래스에서 $L_g \leq L_c$ 증명
> 클로저 시: T-Temporal-Identity (a,b,d) Cat A → **CV-1.12 +3A**

*다른 가설에 의존하지 않음 — 다음 세션에서 바로 시작 가능*

---

## 가설 상태 요약

| ID | 가설 | 현재 상태 | 차단하는 정리 | 우선순위 | 페이즈 |
|----|------|----------|-------------|---------|-------|
| **H-SINK** | Sinkhorn-Lipschitz (S-B2) | OPEN | Q5 Cat A | 상 | **Phase 1** |
| **H-T*** | T_* 정규 등록 (OP-0021) | OPEN | Q3/Q4 수치화 | 최상 | Phase 2 |
| **H-MORSE** | Morse 안정성 | OPEN | Q3 Package II | 최상 | Phase 2 |
| **H-SR** | 스펙트럼 반발 호환성 | OPEN | Q2 무조건화 | 중 | Phase 2 |
| **H-WS** | Well-separation 도출 | OPEN | Q2 범위 확장 | 중 | Phase 2 |
| **H-σ4** | T-σ-Theorem-4 Cat A | PARTIALLY OPEN | Q1 σ-framework | 중 | Phase 2 |
| **H-P7** | Decay-to-cut (P7) | PARTIALLY STRUCTURED | Q2 조건 감소 | 중하 | Phase 3 |
| **H-κ** | 곡률 조건 도출 | OPEN | Q1 조건 감소 | 중하 | Phase 3 |
| **H-μ0** | μ₀ > 0 일반 증명 | OPEN | Q1 완전 무조건화 | 낮음 | Phase 3 |

---

## 대목표

> **어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?**
>
> $u_t : X_t \to [0,1]$ 만을 primitive로 하여, 감각장의 차이들이 에너지 최솟값으로 응집될 때 그 위상 구조가 객체성을 결정함을 수학적으로 정당화한다. 객체의 수, 경계, 동일성은 관측 조건의 함수다 — 절대량이 아니다.

**중심 정리 (T8 — 위상전이):**

$$\frac{\beta}{\alpha} > \frac{4\lambda_2}{|W''(c)|}$$

$\lambda_2$ = 그래프 해상도. 이 조건이 성립할 때 경계가 출현한다. 붕괴할 때 융합된다.

공리 층 (고정 — 수정 불가):
```
A1'(self-regulation)  A2(monotone)  A3(contraction, a_cl<4)  A4(continuity)
B1-B4 (adjacency: nonneg, sym, local, non-transitive)
E1-E4 (transport: sub-stoch, non-inj, core-inherit, fingerprint-cost)
```

---

## 크리티컬 패스

```
H-SINK [Phase 1] ──→ Q5 Cat A → CV-1.12
                          │
                          ▼
                      Q6 Cat B (σ-상속)

H-MORSE ──┐
           ├──→ Package II (Eyring-Kramers)
H-T*   ──┘         │
                    ▼
            Q4-DYN (K 동역학 완성) → 대목표 완성
```

세 경로 모두 독립 — 병렬 진행 시 상호 차단 없음.

---

## Q1 — 경계는 언제 출현하는가?

*인식론적 의미: 균일한 감각장에서 왜 경계가 생기는가? 해상도($\lambda_2$)가 낮으면 왜 두 사물이 하나로 보이는가?*

*Cat A 완성분: T1, T6b, T14, T8-Core, T8-Full, T-Persist-1(a,b,c,e), T-PreObj-1/1G, T-OP6-B, σ-framework (Lemma 1/2/3, Theorem 3). 열린 노드 3개.*
*참고: T-Persist-1(d) Interior Gap은 Cat C — β > 7α 필요조건 제거 불가, 구조적 한계.*

```
┌─────────────────────────────────────────┐
│ [H-μ0] μ₀ > 0 일반 그래프 증명          │  OPEN (낮은 우선순위 / Phase 3)
│  수치적으로 μ₀ ∈ [0.96, 60.2] 확인됨   │
│  일반 그래프 이론 증명 없음             │
│  닫히면: T8-Full 무조건 Cat A           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [H-κ] 곡률 조건 κ_max·ξ ≤ 0.1 도출    │  OPEN (중하 우선순위 / Phase 3)
│  에너지에서 도출 안 됨, 가정만 됨      │
│  닫히면: T-OP6-B 조건 하나 제거        │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [H-σ4] T-σ-Theorem-4 Cat A 증명        │  PARTIALLY OPEN (Phase 2)
│  A₂/A₁ = 4 유한격자 확인 (NQ-187)      │
│  세 경로 (α,β,γ) 중 하나 증명 필요     │
│  닫히면: T-σ-Theorem-4 Cat A 재승격    │
└─────────────────────────────────────────┘
```

---

## Q2 — 여럿이 공존할 수 있는가?

*인식론적 의미: 같은 감각장에서 여러 개의 독립된 덩어리가 동시에 성립할 수 있는가? 어떤 조건에서 두 덩어리가 분리된 채로 유지되는가?*

*Cat A 완성분: T-Persist-K-Sep/Weak (H-SR/H-WS 조건부), T-L1-F/T-L1-M (P0-P11 조건부). 열린 노드 3개.*

```
┌─────────────────────────────────────────┐
│ [H-SR] 스펙트럼 반발 호환성             │  OPEN (Phase 2)
│  min_k μ_k > (K-1)·λ_rep              │
│  접근: Weyl 부등식 → (β,α,D_sep,K)     │
│        에서 명시적 하한 도출            │
│  닫히면: T-Persist-K-Sep/Weak 무조건화 │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [H-WS] Well-separation 조건            │  OPEN (Phase 2)
│  D_sep ≥ d_min*(β, α, K)              │
│  접근: 에너지 장벽 분석 → d_min* 공식  │
│  닫히면: 분리 조건이 이론 내부화됨     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [H-P7] Decay-to-cut (L1-J P7)          │  PARTIALLY STRUCTURED (Phase 3)
│  Combes-Thomas/Agmon 분석              │
│  강한 정상상태 하에서 부분 도출 가능   │
│  닫히면: T-L1-F 조건 P7 제거          │
└─────────────────────────────────────────┘
```

---

## Q3 — 어떻게 변하는가?

*인식론적 의미: 응집된 덩어리는 시간이 지나면서 어떻게 요동치고 안정화되는가? 노이즈 속에서 왜 형태가 유지되는가?*

*Cat A 완성분: Package I 전체 (T-PF-A1-AR/SDE/GI/PE, T-P-F-ε0). T-PF-ε0-K Cat B.*

```
┌─────────────────────────────────────────────────┐
│ [H-MORSE] Morse 안정성                           │  MAJOR OPEN (Phase 2)
│  ∀ critical point u* of E on Σ_m,              │
│  Hessian H(u*)|_{T_{u*}Σ_m} has               │
│  μ_min > 0 (mod symmetry-zero eigenvalues)     │
│                                                 │
│  접근: T7-Enhanced 기반 + Allen-Cahn Morse 전이 │
│       수치: μ_min ∈ [0.96, 60.2] 전 config     │
│                                                 │
│  닫히면:                                        │
│  → T-PF-ε0-K Cat B → Cat A                    │
│  → Package II (Eyring-Kramers) 진입            │
│  → H-SR 보조 (임계점 구조 → μ_k 하한)         │
└─────────────────────────────────────────────────┘
```

*Package II (OPEN): H-MORSE + H-T* 전제. 목표: Eyring-Kramers Γ_K, K→K-1 barrier crossing.*

---

## Q4 — 몇으로 안정화되는가?

*인식론적 의미: 감각장이 안정화될 때, 왜 특정한 수의 덩어리로 수렴하는가? 해상도·에너지·온도가 K를 어떻게 결정하는가?*

*현재 상태: T-K-Select-PF Cat B, T-K-Select-OBS Cat B. DYN OPEN.*

```
┌─────────────────────────────────────────────────┐
│ [H-T*] T_* 정규 등록 (OP-0021)                  │  MAJOR OPEN (Phase 2)
│  π_{T_*} = Z^{-1} exp(-E/T_*) 가               │
│  SCC 동역학의 자연 불변측도                     │
│                                                 │
│  경로 A — Mori-Zwanzig (NOP-F, Lemma 20):      │
│   메모리 핵 감쇠율에서 유효 온도 추출          │
│   5개 gap 식별됨, 스케치 수준                  │
│                                                 │
│  경로 B — RG 고정점 (NOP-J, Lemma 24):         │
│   T_*^{Fisher} = T_*^{RG} 동치 스케치됨        │
│                                                 │
│  닫히면:                                        │
│  → T-K-Select-PF/OBS 수치 예측으로 전환        │
│  → Package II 진입 (H-MORSE 결합 시)           │
│  → D-ST-4 rate claims 완성                     │
└─────────────────────────────────────────────────┘
```

---

## Q5 — 시간이 지나도 같은 것인가?

*인식론적 의미: 덩어리는 움직이고 변형되는데, 어떤 수학적 기준으로 "같은 객체"라고 말할 수 있는가?*

*현재 상태: T-Temporal-Identity Cat B 전 파트 (a,b,c,d) — 2026-05-07 달성. Cat A OPEN.*

```
┌─────────────────────────────────────────────────┐
│ [H-SINK] Sinkhorn-Lipschitz (S-B2, Lemma 8.2)   │  OPEN — Phase 1 타겟
│  ∀ cost c ∈ SCC-cost-class, ∀ ε_OT > 0:       │
│  L_g(ε_OT) ≤ L_c (Bigot-Cazelles-Papadakis)   │
│                                                 │
│  대안 경로: H-SPEC → ARCHIVED (scaling error)   │
│                                                 │
│  닫히면:                                        │
│  → T-Temporal-Identity (a,b,d) Cat A           │
│  → CV-1.12 승격 (+3A, 57 Cat A)                │
└─────────────────────────────────────────────────┘
```

*파트 (c) kernel independence: 추가로 S-B3 (iso-ratio 의존성 제거) 필요.*
*OP-0011: PARTIALLY RESOLVED (Lemma 10, 2026-05-07).*

---

## Q6 — 분열·합병 후에도 이어지는가?

*인식론적 의미: 두 덩어리가 하나로 합쳐지거나 하나가 둘로 나뉠 때, 그 형태적 서명(σ)은 어떻게 이어지는가?*

*전제: T-Temporal-Identity Cat B ✓ (2026-05-07 충족).*

```
OP-0008 하위문제:
  CONT  (연속 K):      PARTIALLY STRUCTURED
  MERGE (K-jump 합병): Cat B 부분 ✓ / σ_standard Cat C (Wigner-projection W9+ 필요)
  SPLIT (K-jump 분열): STRUCTURED
  DIST  (교란 안정성): CLOSED Cat B ✓ (Lemma 16, 2026-05-07)

T-σ-Inherit (Cat B target): CONT/MERGE/SPLIT 해결 시 진입
```

---

## 연구 페이즈

### Phase 1 — 단기 (~5세션, 즉시 공략 가능)

| 타겟 | 경로 | 결과 |
|---|---|---|
| **H-SINK** | Bigot-Cazelles-Papadakis → SCC 비용 클래스 $L_g \leq L_c$ | Q5 Cat A → CV-1.12 |

### Phase 2 — 중기 (병렬 공략)

| 타겟 | 답하는 질문 | 열리는 것 |
|---|---|---|
| **H-MORSE** | Q3 | Package II 진입, T-PF-ε0-K Cat A |
| **H-T*** | Q4 | K-Select 수치화, Package II |
| **H-SR + H-WS** | Q2 | T-Persist-K 무조건화 |
| **H-σ4** | Q1 | T-σ-Theorem-4 Cat A |

*H-MORSE + H-T* 동시 클로저 시: Package II → Q4-DYN*

### Phase 3 — 장기 (잔여 무조건화)

| 타겟 | 답하는 질문 | 열리는 것 |
|---|---|---|
| **H-P7** | Q2 | T-L1-F 조건 감소 |
| **H-κ** | Q1 | T-OP6-B 조건 제거 |
| **H-μ0** | Q1 | T8-Full 무조건화 |

---

## 수정 규칙 (Modification Protocol)

### 버전 체계

```
HT-x.y
  x: 구조 변경 (섹션 순서, 블록 추가/삭제, 의존성 방향, 대목표 변경) — 사용자 결정 필요
  y: 노드 변경 (가설 추가/클로저/상태 갱신)                           — 세션 중 자유롭게
```

현재: **HT-3.0**

### 조작 유형

**HT-ADD** (y+1): 새 H-노드 추가. 추가 시 "이 가설이 Q1-Q6 중 어느 질문에 답하는가?" 명시 필수.

**HT-CLOSE** (y+1): 가설 클로저. 절차: 박스에 `✓ CLOSED (날짜, 방법)` → 요약 테이블 갱신 → CHANGELOG.md 기록. working 파일 증명 없이 선언 불가.

**HT-PROMOTE** (y+1 선택): 상태 갱신 (OPEN → PARTIALLY STRUCTURED → PARTIALLY RESOLVED).

**HT-RESTRUCTURE** (x+1, y=0): Q 번호 변경, 질문 재정의, 블록 분할/통합, 대목표 변경. 사용자 결정 필요.

**HT-SYNC**: canonical.md/theorem_status.md 변경 후 확인. DECLARATION.md 내용과 일치하는지도 검토.

### 불변 규칙

1. 대목표 진술 ("어떤 차이의 덩어리가 언제부터...") — 사용자 결정 없이 수정 불가
2. 모든 H-노드는 Q1-Q6 중 하나에 귀속되어야 한다 — 귀속 불가 시 DECLARATION.md와의 정합성 재검토
3. 가설 클로저는 working 파일 증명 없이 선언 불가
4. 의존성 화살표는 단방향 — 순환 의존 금지

---

## 보류/철회 경로 (Archived Paths)

### H-SPEC — Spectral-gap bypass (NQ-6)  [ARCHIVED 2026-05-07]

**목표:** H-SINK 우회 → Q5 Cat A
**진술:** $\eta_{\text{cross}} \leq \exp(-\mu_{\text{joint}} \cdot d^2 / \varepsilon_{\text{OT}})$
**시도:** Lemma 13 — scaling 오류 발견 후 철회
**재시도 가능성:** ~50%
**재활성화 조건:** scaling correction 확인 + H-SINK 대비 명확한 경로 확보 시

---

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| HT-1.0 | 2026-05-07 | 초기 등록. 6개 BLOCK (수학적 주제), 10개 가설 노드. |
| HT-1.1 | 2026-05-07 | GAP-0/1/2 → H-μ0/H-κ/H-σ4; H-SPEC Archived; Phase 1/2/3 추가. |
| HT-2.0 | 2026-05-07 | 에이전트 읽기 최적화 리스트럭처: 즉시 타겟 → 요약 → 상세 순서. |
| HT-3.0 | 2026-05-07 | 블록을 수학적 주제(BLOCK-I~VI)에서 인식론적 질문(Q1~Q6)으로 재편. 대목표를 "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"로 재정의. T8 중심 정리 명시. DECLARATION.md 참조 추가. 모든 H-노드에 Q 귀속 표시. |
