---
id: CC-StableK-01
type: working/theory
status: open — CV-1.14 candidate working file
created: 2026-05-12
session: W7 carry-forward
scope: OP-0012-CC-StableK — 정의 패키지
source: temporal_identity_sharp_form_2026-05-07.md, S-B3_kernel_independence.md, canonical.md §§3,7,8.5
---

> [!nav] Linked: [[MOC_temporal_composition]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 01. 정의 패키지 — OP-0012-CC-StableK

모든 정의는 CV-1.13 canonical.md 및 temporal_identity_sharp_form_2026-05-07.md에서 복원함.
새로운 정의에는 [NEW] 표시.

---

## D-CC-1. 연성 응집 장 (Soft Cohesion Field)

시각 t에서의 연성 응집 장:

$$u_t \in \mathcal{F}_M(\mathcal{P}) = \{u \in [0,1]^n : \mu^\top u = M\}$$

- $\mathcal{P}$: 유한 연결 그래프 $G = (\mathcal{P}, E)$의 정점 집합 (크기 $n$)
- $M > 0$: 고정된 총 응집 질량 (cohesive mass)
- (A1): 모든 시점에서 동일한 그래프 사용 (time-varying topology는 NQ-T-Identity-3, OPEN)

## D-CC-2. 지속 성분 (Persistent Components)

D-ST-3 (canonical §3.11) 기준:

$$\mathrm{PersComp}(u_t) = \{C_1^t, \ldots, C_{K_t}^t\}$$

- 각 $C_i^t$: $\{x : u_t(x) \geq \rho_\mathrm{pers}\}$의 연결 성분 중 $\pm\tau$ 임계값 섭동에 대해 안정적인 것
- $K_t = K_\mathrm{act}(u_t) = |\mathrm{PersComp}(u_t)|$: 파생 관측량 (primitive 아님)
- $m_i^t = \sum_{x \in C_i^t} u_t(x)$: 성분 $i$의 응집 질량

**출처**: canonical §3.11 (D-ST-3), temporal_identity_sharp_form §2 (A3).

## D-CC-3. 성분 대응 점수 행렬 (Component Correspondence Score Matrix)

두 시각 $t$, $s$에서 성분 $C_i^t$와 $C_j^s$ 사이의 reduced score:

$$S_{ij}^0(t \to s) = \lambda_m\,\gamma(C_i^t, C_j^s) - \lambda_c \sum_{x \in C_i^t,\, y \in C_j^s} c(x,y)\,M_{t \to s}(x,y)$$

여기서:
- $\gamma(C_i^t, C_j^s) = \sum_{x \in C_i^t, y \in C_j^s} M_{t \to s}(x,y)$: 성분 간 수송 질량
- $c(x,y) = \|\varphi(x) - \varphi(y)\|^2 + \sigma_\mathrm{sp}^{-2}\|x - y\|^2$: fingerprint 기반 수송 비용
- $\varphi(x) = (u(x), \mathrm{Cl}(u)(x), D(x; 1-u))$: 응집 fingerprint
- $\lambda_m > 0$: 질량 수송 보상 가중치
- $\lambda_c > 0$: 비용 패널티 가중치

정규화 점수:
$$\tilde{S}_{ij}^0(t \to s) = \frac{S_{ij}^0(t \to s)}{\min(m_i^t, m_j^s)}$$

$K_t \times K_s$ 점수 행렬 $\tilde{\mathbf{S}}(t \to s) \in \mathbb{R}^{K_t \times K_s}$.

**출처**: temporal_identity_sharp_form §1, temporal_identity_perscomp_transport §4.

## D-CC-4. 시간적 대응 관계 (Temporal Identity Relation)

$$R_{t \to s} \subseteq \mathrm{PersComp}(u_t) \times \mathrm{PersComp}(u_s)$$

임계값 규칙:

$$(C_i^t, C_j^s) \in R_{t \to s} \iff \tilde{S}_{ij}^0(t \to s) \geq \tau_\mathrm{id}$$

동등하게: 상호 최대 점수(mutual max-score) 조건 + $\tau_\mathrm{id}$ 임계값.

**출처**: S-A3_EXISTENCE_AUDIT.md (Cat A, CV-1.13), canonical §13 T-Temporal-Identity.

## D-CC-5. Margin 조건

행(row) margin:
$$\Delta_\mathrm{sep}^\mathrm{row}(M) = \min_{i \in [K_t]} \left[\tilde{S}_{i,j^*(i)}^0 - \max_{j \neq j^*(i)} \tilde{S}_{ij}^0\right]$$

열(column) margin:
$$\Delta_\mathrm{sep}^\mathrm{col}(M) = \min_{j \in [K_s]} \left[\tilde{S}_{i^*(j),j}^0 - \max_{i \neq i^*(j)} \tilde{S}_{ij}^0\right]$$

전체 margin:
$$\Delta_\mathrm{sep}(M_{t \to s}) = \min\!\left(\Delta_\mathrm{sep}^\mathrm{row}(M_{t \to s}),\, \Delta_\mathrm{sep}^\mathrm{col}(M_{t \to s})\right) > 0$$

Margin 조건: $\Delta_\mathrm{sep}(M) > 0$이면 stable-K 하에서 $R_{t \to s}$는 유일한 bijection.

**출처**: temporal_identity_sharp_form §2 margin condition, S-B3 Lemma 11.

## D-CC-6. Stable-K 가정

**세 시점 stable-K** [D-CC-6]:

$$K_t = K_s = K_r = K, \quad \text{no birth/death/merge/split in } [t,s] \cup [s,r]$$

구체적으로:
- $\forall j$: $\sum_i \gamma(C_i^t, C_j^s) \geq \tau_\mathrm{birth} \cdot m_j^s$ (모든 $s$-성분이 $t$에서 기원)
- $\forall i$: $\sum_j \gamma(C_i^t, C_j^s) \geq \tau_\mathrm{death} \cdot m_i^t$ (모든 $t$-성분이 $s$에서 계승)
- $[s,r]$ 구간에도 동일 조건

**출처**: temporal_identity_perscomp_transport §5.2 (Case 1 condition), §6.1(b).

## D-CC-7. 합성 연산자

**관계 합성** (set-theoretic):

$$(R_{s \to r} \circ R_{t \to s})(C_i^t, C_k^r) = \exists\, j : (C_i^t, C_j^s) \in R_{t \to s} \wedge (C_j^s, C_k^r) \in R_{s \to r}$$

Stable-K 하에서 $R_{t \to s}$가 bijection $\pi_{ts}: [K] \to [K]$, $R_{s \to r}$가 bijection $\pi_{sr}: [K] \to [K]$이면:

$$R_{s \to r} \circ R_{t \to s} \leftrightarrow \pi_{sr} \circ \pi_{ts}: [K] \to [K]$$

## D-CC-8. 합성 오차 (Composition Error) [NEW]

**[D-CC-8]** 합성 오차 $\varepsilon_\mathrm{comp}$: 두 구간 OT 수송 계획의 정규화 불일치로 인해
직접 계산한 $M_{t \to r}$과 성분별 합성 $M_{t \to s} \otimes M_{s \to r}$이 차이나는 정도.

정규화 점수 기준 bound:

$$\varepsilon_\mathrm{comp} = \frac{2 M_\mathrm{tot} \cdot \varepsilon_\mathrm{OT,comp}}{\varepsilon_\mathrm{OT}^2 \cdot \min_i m_i}$$

여기서 $\varepsilon_\mathrm{OT,comp}$는 합성 후 정규화 항 불일치 크기 (Lemma CC-4에서 bound 유도 예정).

**현재 상태**: 추측 (conjectural). Lemma CC-4에서 명시적 bound 유도 필요. 현재 Cat C.

## D-CC-9. 합성 일관성 조건 (Consistency Condition CC) [NEW]

**[D-CC-9]** 두 구간 $[t,s]$와 $[s,r]$이 다음을 만족할 때 **compositionally consistent**:

**(CC-1)** Stable-K: $K_t = K_s = K_r = K$, 양 구간 no birth/death/merge/split  
**(CC-2)** Margin: $\Delta := \min(\Delta_\mathrm{sep}(M_{t \to s}), \Delta_\mathrm{sep}(M_{s \to r})) > 0$  
**(CC-3)** Basin containment: $u_s$가 동일 basin 내 ($K$-성분 분지 안)에 있음  
**(CC-4)** Error dominance: $\Delta > 2\varepsilon_\mathrm{comp}$

**출처**: temporal_identity_perscomp_transport §7.2 (Definition 7.1), temporal_identity_sharp_form §4 (Lemma 6 hypothesis).

## D-CC-10. 직접 대응과 합성 대응 비교 [NEW]

**직접 대응** $R_{t \to r}^\mathrm{direct}$:
- $M_{t \to r}$을 직접 Sinkhorn으로 계산 (세 번째 단계 없이 $t$에서 $r$로 직접)
- 유도 bijection: $\pi_{tr}^\mathrm{direct}: [K] \to [K]$

**합성 대응** $R_{t \to r}^\mathrm{comp}$:
- $R_{s \to r} \circ R_{t \to s}$로 계산
- 유도 bijection: $\pi_{sr} \circ \pi_{ts}: [K] \to [K]$

**목표**: CC 조건 하에서 $\pi_{tr}^\mathrm{direct} = \pi_{sr} \circ \pi_{ts}$.

---

## 파라미터 기본값 (exp83 기준, temporal_identity_sharp_form §5에서 복원)

| 파라미터 | 기본값 | 출처 |
|----------|--------|------|
| $\rho_\mathrm{pers}$ | 0.5 | D-ST-3 |
| $\tau_\mathrm{id}$ | 0.1 | §5.7 |
| $\varepsilon_\mathrm{OT}$ | 0.1 (sharp) / 1.0 (exp83) | (A7') |
| $\lambda_m$ | 1.0 | §4.1 |
| $\lambda_c$ | 0.005 | §4.1 |
| $\theta_\mathrm{core}$ | 0.8 | §2.3 |
| $\tau_\mathrm{birth/death}$ | 0.05 | §5.7 |
| $\varepsilon_\mathrm{OT}^*$ | ≈ 0.45 | (A7') |

---

*출처 확인*: 모든 정의는 읽은 파일에서 직접 복원. [NEW] 표시 항목은 OP-0012-CC-StableK 전용 신규 정의.
추측 항목 (D-CC-8의 ε_comp formula)은 명시적으로 표시함.
