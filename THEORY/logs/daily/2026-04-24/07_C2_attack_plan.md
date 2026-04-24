# 07_C2_attack_plan.md — Multi-Phase Strategy for C2 Cluster Conquest

**Session:** 2026-04-24 (evening, extension)
**Origin:** 사용자 요청 — C2 cluster (pre-objective mechanism) 의 완전 정복 목표.
**Goal:** Theorem 2 의 Cat C → Cat A 승급 + F-1 / M-1 / MO-1 의 정형적 status 결정 + NQ-132/133/134/135 의 closed-form 답 또는 numerical 확정.

---

## §1. C2 OP 의 정확한 진단

### 1.1 C2 cluster 멤버 (총 7)

| ID | Statement | Cat | 본 세션 후 status |
|---|---|---|---|
| F-1 | K=2 global stable 이려면 external per-formation mass constraint 필요. 자유 Σ_m 위에서는 K=1 always cheaper. | open conjecture | 본 세션 σ-(S1'-iv) 만 partial reframing |
| M-1 | E(m_1, m_2) monotone toward K=1 (isoperimetric). | open + new question | Theorem 2 가 F=1 saddle 임을 sketched |
| MO-1 | Σ²_M corner manifold, standard Morse 적용 불가. | open scope-clarified | σ scope 외 |
| NQ-132 | (C5) explicit threshold $\lambda_\text{cl}^\text{crit}(L, \beta, a_\text{cl}, c)$. | new, high difficulty | 본 phase 1 의 main theory target |
| NQ-133 | F=1 → F≥5 jump 의 spectral 설명. | new, medium | Phase 1 theory |
| NQ-134 | cl-only vs sep-only 의 disk destabilization 비교. | new, low-medium | Phase 2 light numerical |
| NQ-135 | Generalized $\mathcal{F} \leq F_*$ destabilization threshold. | new, high | Phase 1 theory + Phase 3 numerical |

### 1.2 핵심 통합 명제 (정복 후 도달 목표)

> **Pre-Objective Theorem (target Cat A statement, end of C2 attack):**
> Let $G = L \times L$ free-BC grid, $\mathcal{E}$ full SCC with $b_D = 0$, $c \in $ spinodal, $\beta > \beta_\text{crit}$. There exists an explicit threshold $\lambda_\text{cl}^\text{crit}(L, \beta, a_\text{cl}, c)$ and an explicit minimum-formation-count function $F_*(L, \beta, \lambda_\text{cl}, \lambda_\text{sep}, a_\text{cl}, c) \in \mathbb{Z}_{\geq 1}$ such that for $\lambda_\text{cl} > \lambda_\text{cl}^\text{crit}$, every Morse-0 local minimizer $u^*$ of $\mathcal{E}$ on $\Sigma_m$ satisfies $\mathcal{F}(u^*) \geq F_*$. In particular, single-disk minimizer (F=1) is destabilized into saddle.

이 통합 명제가 C2 의 모든 subitem 를 함의:
- F-1: 자유 Σ_m 에서 F≥F_* ⇒ K=2 가 K=1 의 partition 으로서 derivable, F-1 의 negative resolution.
- M-1: K=1 preference 가 $K_\text{step}$ layer 에서만 valid; $\mathcal{F}$ layer 에서는 K=F_*.
- MO-1: σ-framework 가 Σ_m 단일 manifold 위 작동, Σ²_M corner 회피.
- NQ-132: $\lambda_\text{cl}^\text{crit}$ 가 explicit.
- NQ-133: F_* = 5 (R23 empirical) 또는 F_*(L, β, c) closed form.
- NQ-134: $\lambda_\text{cl}^\text{crit}$ 와 $\lambda_\text{sep}^\text{crit}$ 가 분리 도출.
- NQ-135: F_* 함수 자체가 답.

---

## §2. Phase 분할 전략

### Phase 1 — Theory only (immediate, 본 세션 내 이행)

**작업 목록**:
- (1.1) **g_cl explicit at u*_disk** — Closure gradient 의 explicit form using Cor 2.2 ansatz.
- (1.2) **g_sep explicit at u*_disk** — Distinction gradient 의 explicit form.
- (1.3) **λ_cl^crit closed form (NQ-132)** — Step 5 of Theorem 2 의 cancellation 조건의 정량적 statement.
- (1.4) **Spectral gap argument for F_* (NQ-133, partial)** — Cor 2.2 + Prop 1.3a 결합으로 F=1 → F_* jump 의 spectrum-based 설명.
- (1.5) **F-1 / M-1 reformulation** — σ-framework 안에서의 statement 재기술. Negative resolution 또는 conditional 구조 정립.
- (1.6) **MO-1 sidestep clarification** — σ-framework 가 Σ_m 단일 manifold 위 작동함의 명시.

**산출**: `08_C2_phase1_theory.md` (예상 ~400 줄).

### Phase 2 — Light numerical (가능하면 본 세션 내, 사용 권한 의존)

**작업 목록**:
- (2.1) Phase 1 의 g_cl, g_sep 공식을 L=8 small grid 에서 verify (existing scc package 사용)
- (2.2) λ_cl^crit prediction 을 L=8, β=10 에서 numerical scan 으로 확인

**Approach**: scc package 의 `EnergyComputer`, `find_formation`, `GraphState` 사용. ~50줄 stand-alone script. Runtime <1분.

**산출**: `08a_C2_phase2_light_numerical.py` (script) + `09_C2_phase2_results.md` (결과).

### Phase 3 — Heavy numerical (USER RUNS)

**작업 목록**:
- (3.1) 32×32 scan: pure cl ($\lambda_\text{sep}=0$) 와 pure sep ($\lambda_\text{cl}=0$) 에서 minimum stable F 측정
- (3.2) F-distribution as $(\lambda_\text{cl}, \lambda_\text{sep})$ 변화 — full $(\lambda_\text{cl}, \lambda_\text{sep})$ phase diagram
- (3.3) Direct test of $\lambda_\text{cl}^\text{crit}$ prediction with multi-IC

**Estimated runtime**: 32×32 with ~50 IC × ~10 parameter pairs × 10 sec each ≈ 1.5 hours. **User runs**.

**Communication protocol**:
- 본 세션에서 script 작성 (`exp_C2_phase3_*.py`)
- 사용자에게 명령 제공
- 사용자 결과 (json) 반환 시 분석.

### Phase 4 — Integration

**작업 목록**:
- (4.1) Theorem 2 final statement 작성, Phase 1-3 결과 통합
- (4.2) F-1, M-1, MO-1 status 최종 update
- (4.3) `06_open_problems_digest.md` C2 cluster 갱신
- (4.4) 99_summary.md update

**산출**: `10_C2_final_integration.md` + 99 update.

### Phase 5 (optional, 시간 풍부 시) — Generalization

다른 graph (random, SBM) 에서의 Pre-Objective 일반화. NQ-150 (universality) 의 partial answer.

---

## §3. 실행 순서 + 병렬 처리

```
[t=0]    Plan 작성 (이 파일)                                   ← 완료
[t+5min] Phase 1 theory 시작 (08_*)                          ← 즉시 시작
[t+90min] Phase 1 완료
[t+95min] Phase 2 script + execute (light numerical)         ← 즉시 이행
[t+110min] Phase 2 결과 분석
[t+115min] Phase 3 script 작성 (heavy)
[t+125min] Phase 3 commands → user 에게 제공
[t+125min] User 실행 대기 중: Phase 4 partial integration 시작 (Phase 1-2 만으로 가능한 범위)
[t+...]   User 결과 도착 → Phase 4 완성
```

**Key principle**: User 실행 대기 중 idle 금지. Phase 4 partial 또는 Phase 5 sketch 진행.

---

## §4. 기대되는 실패 모드 + 대응

### 4.1 g_cl, g_sep 의 closed form 이 너무 복잡

**위험**: Cor 2.2 ansatz $u^*_\text{disk}(r) = \tfrac{1}{2}(1 - \tanh((r-r_0)/\xi_0))$ 위 closure operator $\text{Cl}$ 의 적용이 sigmoid 의 합성으로 closed form 미보유.

**대응**: leading-order asymptotic ($r \ll r_0$ interior, $r \gg r_0$ exterior, $r \approx r_0$ interface) 의 분리 + interface region 의 dominant contribution 만 유지.

### 4.2 λ_cl^crit 가 graph-dependent 으로 실패

**위험**: $\lambda_\text{cl}^\text{crit}$ 가 explicit closed form 으로 환원 안 되고 Laplacian eigenvalue 들의 함수로만 expressible.

**대응**: scaling form $\lambda_\text{cl}^\text{crit} \sim f(\beta, \alpha, a_\text{cl}, c) \cdot g(L, \lambda_2, \ldots)$ 으로 분리. $f$ 를 closed form, $g$ 를 graph-class-specific 으로.

### 4.3 F_* prediction 이 R23 의 5 와 불일치

**위험**: Spectral gap argument 가 F_* = 2 또는 F_* = 3 등 R23 와 다른 값 예측.

**대응**: Discrepancy 의 source 식별 — (a) Cor 2.2 ansatz 정확도, (b) cl/sep 의 nonlinearity 의 leading-order 누락, (c) finite L 효과. NQ 로 보존, Cat C 로 자기분류.

### 4.4 Phase 3 user execution 이 환경 issue 로 실패

**위험**: 사용자가 script 실행 시 dependency / GPU / memory issue.

**대응**: script 를 self-contained + verbose logging + intermediate save. 실패 시 작은 sub-problem 으로 fallback.

---

## §5. 성공 기준 (자가 평가)

- [ ] Phase 1 theory 의 (1.1)-(1.6) 6 작업 완료
- [ ] Phase 2 light numerical 의 (2.1)-(2.2) 2 작업 완료 또는 명시적 fallback
- [ ] Phase 3 script 작성 + user command 제공 완료
- [ ] Phase 4 partial integration 완료 (Phase 1-2 결과만으로)
- [ ] Theorem 2 의 새 statement 가 (a) explicit threshold, (b) F_* prediction, (c) Cat 분류 갱신 포함
- [ ] F-1, M-1, MO-1 의 새 statement 가 σ-framework 안에서 작성

**최소 acceptable**: Phase 1 + Phase 2 + Phase 3 script. Phase 4 final 은 user 결과 후.

---

## §6. Plan 종료 — 즉시 Phase 1 시작

다음 파일: `08_C2_phase1_theory.md`. Phase 1 의 6 작업.
