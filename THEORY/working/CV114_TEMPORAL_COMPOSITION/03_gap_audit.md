---
id: CC-StableK-03
type: working/theory
status: open — gap 분석 v2 (2026-05-12, §10 정밀 독해 반영)
created: 2026-05-12
updated: 2026-05-12 (§10 독해 + canonical §8.5 확인 후 전면 업데이트)
session: W7 carry-forward
scope: OP-0012-CC-StableK — 이미 증명된 것 / Cat B 가능 / 새로 필요한 것 분류
---

> [!nav] Linked: [[MOC_temporal_composition]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 03. Gap Audit v2 — OP-0012-CC-StableK

---

## §A. 2026-05-12 정밀 독해 결과 (v2 업데이트 근거)

### A.1 `03_development.md` §10 (Lemma 6) 정밀 독해

**읽은 파일**: `THEORY/logs/daily/2026-05-07/03_development.md`, lines 506–544.

#### 핵심 발견: Lemma 6의 M_{t→r} 정의 방식

§10.2 증명에서:
> "the *direct* relation computed via the **composed transport plan**
> $M_{t \to r}^\mathrm{direct} := M_{s\to r} \circ M_{t \to s}$
> (matrix product / measure pushforward)"

**결론**: Lemma 6은 $M_{t\to r}$을 **행렬 합성으로 정의**한다.  
독립적으로 Sinkhorn$(u_t, u_r, c_{t\to r})$을 계산한 것이 아님.

#### Lemma 6의 주장 유형 분류

| 주장 유형 | 포함 여부 | 설명 |
|-----------|-----------|------|
| Kernel-level composition | **YES** | $M_{t\to r} := M_{s\to r} \circ M_{t\to s}$ 정의로 사용 |
| Relation-level composition | **YES** | $R[M_{s\to r} \circ M_{t\to s}] = R[M_{s\to r}] \circ R[M_{t\to s}]$ |
| Score-level composition (Sinkhorn vs composed) | **NO** | 스코어 비교 없음 |
| Explicit error term ε_comp | **NO** | 오차 항 없음 (정의로 합성하므로 ε_comp = 0 자동) |
| Comparison with independent Sinkhorn(u_t, u_r) | **NO** | 이것이 OP-0012-CC-StableK의 실제 gap |

#### Lemma 6 가정과 OP-0012-CC-StableK 호환성

| 가정 | Lemma 6 | OP-0012-CC-StableK | 호환? |
|------|---------|-------------------|-------|
| Stable-K (K_t=K_s=K_r=K) | (I_{ts}) + (I_{sr}) | (A4) 세 시점 | 호환 |
| No birth/death | 함의됨 (stable-K) | 명시 | 호환 |
| Margin ≥ Δ_sep* | (I_{ts}), (I_{sr}) | Δ > 0 | 호환 |
| M_{t→r} 계산 방법 | **M_{s→r} ∘ M_{t→s} (정의)** | **Sinkhorn(u_t, u_r) (독립 계산)** | **불호환** |

**핵심 불호환**: Lemma 6은 $M_{t\to r} := M_{s\to r} \circ M_{t\to s}$를 **정의로** 사용하지만,
OP-0012-CC-StableK는 실무에서 $M_{t\to r}$을 $u_t$, $u_r$에 대한 독립적 Sinkhorn으로 계산함.
이 둘이 같다는 보장이 없음 — 이것이 실제 gap.

#### Lemma 6 상태 재분류

- **Cat B (완전 증명)** — 하지만 좁은 범위
- 주장: "$M_{s\to r} \circ M_{t\to s}$를 사용하면 R 합성이 성립"
- 실무 relevant 주장 (독립 Sinkhorn)에는 직접 적용 불가

### A.2 `canonical.md §8.5` E3 refined / self-referential transport 확인

**읽은 내용**: canonical §8.5 (lines 720–730), §12 open problems (lines 934, 1069).

#### Route B "ε_comp = 0" 판정: **폐기**

canonical.md §8.5 명시적 발언:
> "A fully self-referential transport realization — where cost depends only on $u_t$, $u_s$,
> and $\mathbf{N}$ — is an open problem for strong-regime analysis (Section 12)."

canonical §12 open problems:
> "Self-referential optimal transport existence. Existence and uniqueness of OT plans with
> self-referential cost... (Existence proved via Schauder; uniqueness proved via transport
> confinement; **semigroup/composition property NOT listed as proved**.)"

**결론**: self-referential cost 하에서도 $M_\mathrm{Sinkhorn}(u_t, u_r) \neq M_{s\to r} \circ M_{t\to s}$.
양쪽의 cost function이 다르기 때문:
- $M_{t\to s}$: cost $c(x,y; u_t, u_s)$
- $M_{s\to r}$: cost $c(y,z; u_s, u_r)$
- $M_\mathrm{Sinkhorn}(u_t, u_r)$: cost $c(x,z; u_t, u_r)$

세 cost가 동일한 self-referential 구조를 가지더라도 $c(x,z; u_t, u_r) \neq c(x,y; u_t,u_s) + c(y,z; u_s,u_r)$.
Semigroup 성질 (composition = direct) is an open problem, NOT proved.

**Route B "ε_comp = 0" 주장 폐기**. Route A (perturbative)가 유일한 경로.

---

## §B. 읽은 파일 목록 (v2 기준)

- `03_development.md §10` (Lemma 6 완전 증명, 2026-05-12 독해)
- `temporal_identity_sharp_form_2026-05-07.md` (Lemma 6 참조, (A1)-(A9) 패키지)
- `S-B3_kernel_independence.md` (Lemma 9/10/11 Cat A/B)
- `partial_ot_stability.md` (Theorem Partial-H-SINK Cat A)
- `S-A3_EXISTENCE_AUDIT.md` (R_{t→s} 존재성 Cat A)
- `temporal_identity_perscomp_transport.md` (정의 출처)
- `canonical.md §8.5, §12` (self-referential transport, open problems)

---

## §C. Lemma별 Gap 감사 (v2)

### Lemma CC-1: Stable-K Bijection 존재 및 유일

**필요한 것**: (I_{ts}) 하에서 $R_{t\to s}$가 유일한 bijection $\pi_{ts}$를 정의함.

**[PROVED — Cat A]**

근거:
- T-Temporal-Identity (b) Cat A (CV-1.13, canonical §13)
- Lemmas 4+5+8 (sharp form §3): margin → bijection
- 동일 결론이 (I_{sr})에도 성립

**결론**: CC-1 새 증명 불필요. 완전 증명됨.

---

### Lemma CC-2: Kernel-Composition vs Sinkhorn 비교 [v2 재명명]

**v2 재정의**: CC-2는 이제 두 수송 계획의 TV distance를 묻는 문제:

$$\lVert M_{t\to r}^\mathrm{Sinkhorn} - M_{t\to r}^\mathrm{kernel-comp} \rVert_\mathrm{TV} \leq \varepsilon_\mathrm{comp}$$

여기서:
- $M_{t\to r}^\mathrm{Sinkhorn} = \mathrm{Sinkhorn}(u_t, u_r, c[u_t,u_r], \varepsilon_\mathrm{OT})$ (독립 계산)
- $M_{t\to r}^\mathrm{kernel-comp} = M_{s\to r} \circ M_{t\to s}$ (행렬 합성)

**기존 도구**:

### [PROVED — Cat A] Theorem Partial-H-SINK

```
‖M*(c) - M*(c')‖_TV ≤ 2m_t · δ/ε_OT  (linear regime)
```

cost perturbation δ에 대한 TV bound. CC-2의 기초 도구.

**적용 가능성 분석**:  
Partial-H-SINK는 "같은 Sinkhorn objective를 다른 cost로 푼" 두 계획의 차이를 bound함.
CC-2에서 $M^\mathrm{kernel-comp}$는 Sinkhorn objective를 풀지 않으므로 **직접 적용 불가**.
중간 단계 필요: kernel-comp가 어떤 effective cost로 계산한 Sinkhorn에 가까운가?

### [CAT B AVAILABLE] Lemma 3-sharp (off-diagonal mass)

```
γ_{M_{t→s}}(C_i^t, C_j^s) ≤ e^{-(γΔ²-L_g d_eff)/ε_OT} · min(m^t, m^s)
```

비대각 mass가 지수적으로 작음. CC-2에서 간접 사용 가능:
kernel-comp의 비대각 성분 bound → Sinkhorn의 비대각 성분 bound와 비교.

### [CAT B, 이미 증명] Lemma 6 (kernel-composition = relation-composition)

Lemma 6은 다음을 Cat B로 증명함:
```
R[M_{s→r} ∘ M_{t→s}] = R[M_{s→r}] ∘ R[M_{t→s}]
```
이것이 **T-CC-StableK-Kernel** (좁은 버전). CC-2는 이보다 강한 것을 요구함.

### [NEW NEEDED] Core gap: effective cost of kernel-composition

$M^\mathrm{kernel-comp}(x,z) = \sum_y M_{t\to s}(x,y) M_{s\to r}(y,z)$의  
effective Sinkhorn cost는?

$$c^\mathrm{eff}(x,z) = -\varepsilon_\mathrm{OT} \log \sum_y \frac{M_{t\to s}(x,y) M_{s\to r}(y,z)}{u_t(x)}$$

이것과 $c(x,z; u_t, u_r)$ (직접 fingerprint cost)의 차이 $\delta_\mathrm{eff}$를 bound하면  
Partial-H-SINK로 TV bound를 얻을 수 있음.

**현재 상태**: **Cat C** — $\delta_\mathrm{eff}$ bound 없음.

---

### Lemma CC-3: Argmax Stability

**[CAT B, CC-2 조건부]** — v2에서 변화 없음.

CC-2가 $\varepsilon_\mathrm{comp}$를 주면 CC-3의 대수 논증은 자명:
- $\Delta > 2\varepsilon_\mathrm{comp}$ → argmax gap > 0 → bijection 일치

CC-3 자체의 새 증명 불필요. CC-2에 완전 종속.

---

### Lemma CC-4: Composition Error Explicit Bound [v2: Route B 폐기]

**[CAT C] — Route A만 유효, Route B 폐기**

#### Route B 폐기 근거 (2026-05-12 확인)

canonical.md §8.5:
> self-referential OT의 semigroup property (composition = direct) is NOT proved.
> It is listed as an open problem.

따라서:
- $c(x,z; u_t, u_r) \neq c(x,y; u_t, u_s) + c(y,z; u_s, u_r)$ 일반적
- Self-referential cost 하에서도 $\varepsilon_\mathrm{comp} \neq 0$
- "ε_comp = 0" 주장 완전 폐기

#### Route A (유일한 경로, Cat C → B 목표)

**단계 1**: $\delta_\mathrm{eff}$ 계산 — kernel-comp의 effective cost와 직접 cost의 차이:
$$\delta_\mathrm{eff} = \lVert c_\mathrm{direct}(x,z; u_t,u_r) - c^\mathrm{eff}(x,z; M_{t\to s}, M_{s\to r}) \rVert_\infty$$

**단계 2**: Partial-H-SINK (Cat A) 적용:
$$\lVert M^\mathrm{Sinkhorn} - M^\mathrm{eff-Sinkhorn} \rVert_\mathrm{TV} \leq 2m_t \cdot \delta_\mathrm{eff}/\varepsilon_\mathrm{OT}$$

여기서 $M^\mathrm{eff-Sinkhorn} = \mathrm{Sinkhorn}(u_t, u_r, c^\mathrm{eff}, \varepsilon_\mathrm{OT})$.

**단계 3**: $M^\mathrm{eff-Sinkhorn} \approx M^\mathrm{kernel-comp}$ 확인 (별도 lemma 필요).

**단계 4**: Lemma 10 (Cat B): TV → 성분 질량 차이:
$$|\gamma_{M^\mathrm{Sinkhorn}} - \gamma_{M^\mathrm{kernel-comp}}| \leq 2M_\mathrm{tot} \cdot \delta_\mathrm{eff}/\varepsilon_\mathrm{OT}$$

**단계 5**: 성분 질량 차이 → 정규화 점수 오차 $\varepsilon_\mathrm{comp}$:
$$\varepsilon_\mathrm{comp} \leq \frac{2M_\mathrm{tot} \cdot \delta_\mathrm{eff}}{\varepsilon_\mathrm{OT} \cdot \min_i m_i}$$

**핵심 블로커**: 단계 1 ($\delta_\mathrm{eff}$ 계산), 단계 3 (eff-Sinkhorn ≈ kernel-comp).

**현재 상태**: **Cat C** — Route A의 단계 1, 3 미완성.

---

## §D. 전체 Gap 요약 테이블 (v2)

| 항목 | 상태 | 출처 파일 | 범위 | 필요 신규 작업 |
|------|------|-----------|------|---------------|
| T-Temporal-Identity (a,b,c,d) | **Cat A** | canonical §13 | 단일 구간 | 없음 |
| Lemma 9 (Partial-H-SINK) | **Cat A** | partial_ot_stability.md | cost perturbation TV bound | 없음 |
| Lemma 10 (Component confinement) | **Cat B** | S-B3 §2.3 | TV→성분 질량 | 없음 |
| Lemma 3-sharp (off-diag mass) | **Cat B** | sharp form §3 | 비대각 지수 bound | 없음 |
| **Lemma 6** (kernel-comp = relation-comp) | **Cat B (완전 증명)** | `03_development.md §10` | M_{t→r}:=M_{s→r}∘M_{t→s} 기준 | **없음** |
| **T-CC-StableK-Kernel** | **Cat B** | Lemma 6 직접 귀결 | Kernel-comp 전제 | **없음** |
| **CC-1** (bijection 존재) | **Cat A** | T-Temporal-Identity (b) | 없음 | |
| **CC-2** (Sinkhorn vs kernel-comp TV) | **Cat C** | 없음 | δ_eff bound 필요 | Route A 단계 1, 3 |
| **CC-3** (argmax stability) | **Cat B** (CC-2 조건부) | margin algebra | CC-2 완전화 후 자동 | |
| **CC-4** (ε_comp Route A) | **Cat C** | 없음 | Route B 폐기 | Route A 단계 1, 3 |
| **T-CC-StableK-Sinkhorn** | **Cat C** | — | 독립 Sinkhorn 기준 | CC-2 + CC-4 |

---

## §E. 정정된 문제 구조

OP-0012-CC-StableK는 **두 수준**으로 분리됨:

```
수준 1: T-CC-StableK-Kernel (Cat B, 완전 증명됨)
  - M_{t→r} := M_{s→r} ∘ M_{t→s} (정의)
  - 결론: R[M_{s→r}∘M_{t→s}] = R[M_{s→r}] ∘ R[M_{t→s}]
  - 출처: Lemma 6 (03_development.md §10)
  - 추가 작업: 없음

수준 2: T-CC-StableK-Sinkhorn (Cat C, 미해결)
  - M_{t→r} = Sinkhorn(u_t, u_r) (독립 계산)
  - 결론: R[Sinkhorn(u_t,u_r)] = R[M_{s→r}] ∘ R[M_{t→s}]
  - 조건: Δ > 2ε_comp (ε_comp = Sinkhorn vs kernel-comp 차이)
  - 블로커: δ_eff = ‖c_direct - c_eff‖ bound 미완성
```

**CV-1.14 승격 전략 수정**:
- 수준 1 (T-CC-StableK-Kernel)은 이미 Cat B → **CV-1.14 최소 정리로 사용 가능**
- 수준 2는 추가 작업 필요; Cat B 달성 시점 불확실

---

## §F. 우선순위 작업 순서 (v2)

**1순위 (즉시 가능)**: T-CC-StableK-Kernel Cat B promotion 검토  
- Lemma 6이 Cat B (완전 증명)이므로 이미 canonical promotion 대상
- canonical.md §13에 "T-CC-StableK-Kernel (Cat B)" 항목 추가 가능
- theorem_status.md OP-0012 상태 "PARTIALLY RESOLVED via Lemma 6" 업데이트 가능

**2순위**: δ_eff 계산 시도  
- kernel-comp의 effective cost $c^\mathrm{eff}(x,z)$ 명시적 계산
- Stable-K + well-separated 하에서 $\delta_\mathrm{eff}$ bound 유도 시도
- 성공 시 CC-2, CC-4, T-CC-StableK-Sinkhorn이 Cat B로 상승

**3순위**: 실험 (04_experiment_plan.md)  
- T-CC-StableK-Kernel은 이미 이론적으로 Cat B이므로 실험은 수준 2 검증 목적
- ε_comp를 직접 측정하여 δ_eff 추정 데이터 수집

---

*작성: 2026-05-12 v1 → v2. 03_development.md §10 정밀 독해 + canonical §8.5 확인 반영.*  
*변경 요약: (1) Lemma 6 범위 재분류, (2) Route B 폐기, (3) 문제 수준 1/2 분리, (4) T-CC-StableK-Kernel Cat B 확인.*
