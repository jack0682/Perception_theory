---
id: ACT-10
type: working/theory
status: open — promotion patch 계획 (draft block 형태)
created: 2026-05-12
scope: canonical.md, theorem_status.md, hypothesis_tree.md, CHANGELOG.md 업데이트 draft
non-overclaim: 실제 파일 수정 없음. 이 파일은 draft block만 포함.
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 10. Patch Plan — CV-1.15 Promotion

---

## 주의사항

이 파일은 **draft block 형태**만 포함한다. 실제 파일 수정은 사용자 승인 후 진행.
canonical.md / theorem_status.md / hypothesis_tree.md 직접 수정 금지 (이 session에서는 적용 안 함).

---

## §1. canonical.md 업데이트 draft

### 삽입 위치

`§13. Theorem Catalog` 섹션의 끝부분 (현재 T-Temporal-Identity 이후; CV-1.14 T-CC-StableK-Kernel 이후).

### §13.Y K symbol 주석 (첫 줄에 삽입)

```markdown
> **(기호 주의)** 이 §13.Y 섹션에서 $\mathbf{K}_{i\to k}$ (볼드체)는 Gibbs 전이 kernel (raw, 비정규화 행렬)을 뜻한다.
> 기존 canonical 표기 $K$ (이탤릭, formation 수)와 다른 기호이다.
```

### §13.Y Action-Based Temporal Succession Package (CV-1.15, 2026-05-12)

```markdown
#### §13.Y Action-Based Temporal Succession Package (CV-1.15)

**배경**: CV-1.14 T-CC-StableK-Kernel (Cat B)은 M이 합성 구조를 가지면 relation도 합성됨을 보였다.
CV-1.15는 action principle이 자연스럽게 합성 구조를 갖는 kernel을 산출함을 보인다.
이것은 기존 temporal identity cost의 **대체가 아니라 composition-compatible refinement**이다.
T-Temporal-Identity (§8.5)는 독립적으로 유효하다.

---

**Lemma L-ENDPOINT-NONSEMI** *(Cat A)*

Squared endpoint cost $c^\mathrm{end}(x,z)=\|z-x\|^2$는 일반적으로 temporal composition과 호환되지 않는다:

$$c^\mathrm{end}_{t\to r}(x,z) \neq \min_y\bigl[c^\mathrm{end}_{t\to s}(x,y)+c^\mathrm{end}_{s\to r}(y,z)\bigr]$$

*반례*: $x=0,\,z=2 \in \mathbb{R}$ — 좌변 $4$, 우변 $\leq 2$.

---

**Lemma L-ACTION-NORMALIZATION** *(Cat A)*

$t<s<r$. 선형 보간 중간점 $y^*=\frac{r-s}{r-t}x+\frac{s-t}{r-t}z$에서:

$$\frac{\|z-x\|^2}{r-t}=\frac{\|y^*-x\|^2}{s-t}+\frac{\|z-y^*\|^2}{r-s}$$

단, 등속 경로에서만 성립.

---

**Definition D-LOCAL-ACTION** *(Definition)*

SCC local action ($\gamma\geq0$, $\Delta t_i>0$, $\varphi_i(x)=(u_i(x),\mathrm{Cl}_i(u_i)(x),D_i(x;1-u_i))$):

$$a_i(x,y)=\frac{d_i(x,y)^2}{\Delta t_i}+\gamma\frac{\|\varphi_{i+1}(y)-\varphi_i(x)\|^2}{\Delta t_i}$$

Path action: $\mathcal{A}_{i:k}(P)=\sum_{\ell=i}^{k-1}a_\ell(x_\ell,x_{\ell+1})$.
Hard-min cost: $c_{i\to k}^{\mathrm{act}}(x,z)=\min_{\mathrm{paths}}\mathcal{A}_{i:k}$.

---

**Lemma L-FINGERPRINT-ACTION-ADMISSIBLE** *(Cat A)*

SCC fingerprint action은 $a_i\geq0$ (nonnegativity), $\mathcal{A}_{i:k}=\sum a_\ell$ (additivity)를 만족하며
T-ACT-DP, T-ACT-GIBBS의 모든 전제를 충족한다.

---

**Theorem T-ACT-DP** *(Cat A)*

*가정*: $X_i$ 유한, $\mathcal{A}_{i:k}$ additive, $i<j<k$.

$$\boxed{c_{i\to k}^{\mathrm{act}}(x,z)=\min_{y\in X_j}\bigl[c_{i\to j}^{\mathrm{act}}(x,y)+c_{j\to k}^{\mathrm{act}}(y,z)\bigr]}$$

*증명*: 경로를 $t_j$에서 절단 (≥방향) + 최적 경로 이어붙임 (≤방향). 양방향 부등식 완결.

---

**Lemma L-ACTION-DELTA-EFF-ZERO** *(Cat A; action direct cost 정의 하에서만)*

$c_{i\to k}^{\mathrm{direct}} := c_{i\to k}^{\mathrm{act}}$로 재정의하면:

$$\delta_\mathrm{eff} = \|c_{i\to k}^{\mathrm{act}} - c_{i\to k}^{\mathrm{eff}}\|_\infty = 0$$

*주의*: endpoint cost, fingerprint similarity cost, Sinkhorn plan에는 적용 불가.

---

**Definition D-GIBBS-KERNEL** *(Definition)*

Local: $\mathbf{K}_{\ell,\ell+1}(x,y)=\exp(-a_\ell(x,y)/\varepsilon)$, $\varepsilon>0$.
Long-horizon: $\mathbf{K}_{i\to k}(x,z)=\sum_{\mathrm{paths}}\exp(-\mathcal{A}_{i:k}/\varepsilon)$.
Soft-min cost: $c_{i\to k}^{\varepsilon}=-\varepsilon\log\mathbf{K}_{i\to k}$.

---

**Theorem T-ACT-GIBBS** *(Cat A)*

*가정*: $X_j$ 유한, $\mathcal{A}_{i:k}$ additive, $\varepsilon>0$, $i<j<k$.

$$\boxed{\mathbf{K}_{i\to k}=\mathbf{K}_{i\to j}\,\mathbf{K}_{j\to k}}$$

Soft-min recursion:

$$c_{i\to k}^{\varepsilon}(x,z)=-\varepsilon\log\!\sum_{y\in X_j}\exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y)+c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

*증명*: Chapman-Kolmogorov path-integral 분해; action additivity + exp 인수분해.

---

**Lemma L-SOFTMIN-HARDMIN-BOUND** *(Cat A)*

$$\min_i a_i - \varepsilon\log N \leq \operatorname{smin}_\varepsilon(a) \leq \min_i a_i$$

---

**Lemma L-SOFT-ACTION-DELTA-EFF-ZERO** *(Cat A)*

$c_{i\to k}^{\varepsilon} = c_{i\to k}^{\mathrm{eff},\varepsilon}$; $\delta_\mathrm{eff}^{\varepsilon}=0$. (T-ACT-GIBBS 직접 귀결)

---

**Proposition P-ACTION-PATH-INHERITANCE** *(Definition Justification)*

SCC temporal identity는 endpoint similarity보다 low-action path inheritance에 더 잘 부합한다.
SCC axiom A3 (stabilization tendency)는 경로상 작은 action을 함의한다.

---

**Theorem T-ACT-KERNEL-COMP→REL** *(Cat B 조건부)*

가정: (GK) $M_{t\to s}:=\mathbf{K}_{t\to s}$로 재정의, (stable-K) $K_t=K_s=K_r$, (margin) $\Delta_\mathrm{sep}>0$.

결론: $R[\mathbf{K}_{t\to r}]=R[\mathbf{K}_{t\to s}]\circ R[\mathbf{K}_{s\to r}]$.

*조건 의존성*: (GK) 조건은 canonical §8.5의 $M_{t\to s}$ 정의 변경을 요구. → CV-1.16 이후.

---

**Warning T-SINKHORN-PLAN-SEMIGROUP-FAILS** *(OPEN — proved failure)*

Sinkhorn-scaled plan $M^\mathrm{sink}(K)=\mathrm{diag}(a)K\mathrm{diag}(b)$는 일반적으로:

$$M^\mathrm{sink}(\mathbf{K}_{ts})\cdot M^\mathrm{sink}(\mathbf{K}_{sr})\neq M^\mathrm{sink}(\mathbf{K}_{tr})$$

이유: 중간 scaling $b_1\odot a_2$는 서로 다른 transport 문제에서 독립 결정되며 $c\cdot\mathbf{1}$이 되지 않는다.
OP-0012-SINK는 OPEN 유지.
```

---

## §2. theorem_status.md 업데이트 draft

### 삽입 위치

현재 `## Cat A Results` 섹션의 마지막 행 이후 (CV-1.13 이후 항목들 뒤).

### 카운트 업데이트

현재: `59A / 14B / 5C / 5R = 83 claims` (CV-1.13 기준)

CV-1.15 후: `+8 Cat A, +2 Cat B = 67A / 16B / 5C / 5R = 93 claims`

(단, P-ACTION-PATH-INHERITANCE는 Interpretation이므로 claim 카운트 포함 여부 결정 필요.
포함 시 +1 → 94 claims. 보수적으로 배제하면 93 claims.)

```markdown
### CV-1.15: Action-Based Temporal Succession Package (2026-05-12)

| C-행 | ID | 내용 | 판정 | 조건 |
|---|---|---|---|---|
| C-new-01 | L-ENDPOINT-NONSEMI | endpoint² cost는 composition-incompatible | Cat A | 반례 (x=0,z=2) |
| C-new-02 | L-ACTION-NORMALIZATION | time-normalized cost 등속 경로에서 additive | Cat A | 등속 경로 |
| C-new-03 | L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action DP/Gibbs 전제 충족 | Cat A | 구조적 확인 |
| C-new-04 | T-ACT-DP | hard-min Bellman DP: c^act=min_y[...] | Cat A | 유한 site, additive |
| C-new-05 | L-ACTION-DELTA-EFF-ZERO | δ_eff=0 (action direct cost 정의 하에서만) | Cat A | action 재정의 전제 |
| C-new-06 | T-ACT-GIBBS | Gibbs kernel semigroup K_{i→k}=K_{i→j}K_{j→k} | Cat A | 유한 site, ε>0 |
| C-new-07 | L-SOFTMIN-HARDMIN-BOUND | smin_ε ∈ [min−ε log N, min] | Cat A | 표준 |
| C-new-08 | L-SOFT-ACTION-DELTA-EFF-ZERO | soft δ_eff^ε=0 (T-ACT-GIBBS 귀결) | Cat A | ε>0 |
| C-new-09 | T-ACT-KERNEL-COMP→REL | (GK)+(stable-K)+(margin) → R 합성 | Cat B | M 재정의 필요 |
| C-new-10 | P-SINKHORN-STABILITY-CONDITIONAL | H-SINK+MARGIN+GAP → relation 보존 | Cat B | H-SINK 미증명 |

OP-0012-SINK 상태 업데이트:
  CV-1.15 기여: cost-level δ_eff blocker = action cost 재정의 시 0 (Cat A).
  잔여 blocker: Sinkhorn scaling gap (b₁⊙a₂≠c·I generically; T-SINKHORN-PLAN-SEMIGROUP-FAILS).
  상태: OPEN 유지. 다음 필요 lemma: L-δ_eff-SINK, L-Eff-Sinkhorn.
```

---

## §3. hypothesis_tree.md 업데이트 draft

### 삽입 위치

기존 `H-COMP` 가지 (OP-0012 계열) 아래.

```markdown
## H-COMP (OP-0012: temporal composition)

### H-COMP-KERNEL (CV-1.14, Cat B)
- **T-CC-StableK-Kernel**: M_{t→r}=M_{s→r}∘M_{t→s} → R[M_{t→r}]=R[M_{s→r}]∘R[M_{t→s}]
- 조건: stable-K + margin
- 상태: Cat B (완결; canonical 삽입 대기)

### H-COMP-ACTION (CV-1.15, 2026-05-12)  [NEW]
- **L-ENDPOINT-NONSEMI** (Cat A): endpoint² 합성 불가
- **T-ACT-DP** (Cat A): hard-min action cost Bellman DP
- **T-ACT-GIBBS** (Cat A): raw Gibbs kernel semigroup K_{i→k}=K_{i→j}K_{j→k}
- **T-ACT-KERNEL-COMP→REL** (Cat B): (GK)+(stable-K)+(margin) → R 합성
  - 주: (GK) 조건이 canonical §8.5 M_{t→s} 재정의 요구; CV-1.16 이후
- 상태: action/Gibbs cost level 완결 (Cat A); canonical M 재정의 조건부 (Cat B)

### H-COMP-SINK (OP-0012-SINK, OPEN)
- **T-SINKHORN-PLAN-SEMIGROUP-FAILS** (proved failure): b₁⊙a₂≠c·I generically
- CV-1.15 기여: cost-level δ_eff blocker 해소 (action cost 재정의 시)
- 잔여: Sinkhorn scaling gap → L-δ_eff-SINK + L-Eff-Sinkhorn 필요
- 상태: OPEN
```

---

## §4. CHANGELOG.md 업데이트 draft

### 삽입 위치

CHANGELOG.md 최상단 (newest-on-top 규칙).

```markdown
## [CV-1.15] 2026-05-12 — Action-Based Temporal Succession Package

### 추가 (Cat A)
- L-ENDPOINT-NONSEMI: endpoint² cost는 temporal composition과 호환 안 됨 (반례: 1D)
- L-ACTION-NORMALIZATION: time-normalized cost는 등속 경로에서 additive
- L-FINGERPRINT-ACTION-ADMISSIBLE: SCC fingerprint action이 DP/Gibbs 전제 충족
- T-ACT-DP: hard-min action cost Bellman DP 정확 성립 (양방향 부등식)
- L-ACTION-DELTA-EFF-ZERO: action cost 재정의 시 δ_eff=0 (T-ACT-DP 귀결)
- T-ACT-GIBBS: Gibbs kernel semigroup K_{i→k}=K_{i→j}K_{j→k} (Chapman-Kolmogorov)
- L-SOFTMIN-HARDMIN-BOUND: soft-min / hard-min 오차 ≤ ε log N
- L-SOFT-ACTION-DELTA-EFF-ZERO: soft-min δ_eff^ε=0 (T-ACT-GIBBS 귀결)

### 추가 (Cat B 조건부)
- T-ACT-KERNEL-COMP→REL: (GK)+(stable-K)+(margin) → R[K_{t→r}]=R[K_{t→s}]∘R[K_{s→r}]
- P-SINKHORN-STABILITY-CONDITIONAL: H-SINK+MARGIN+GAP 조건부 relation 보존

### 추가 (Interpretation)
- P-ACTION-PATH-INHERITANCE: action cost = path inheritance 해석 명제 (수학 정리 아님)

### OPEN 유지
- T-SINKHORN-PLAN-SEMIGROUP-FAILS: Sinkhorn plan semigroup generically fails (proved failure)
- OP-0012-SINK: Sinkhorn scaling gap (b₁⊙a₂≠c·I) — L-δ_eff-SINK + L-Eff-Sinkhorn 필요

### Claim count
- 이전 (CV-1.13): 59A / 14B / 5C / 5R = 83 claims
- 추가: +8 Cat A, +2 Cat B
- 이후 (CV-1.15): 67A / 16B / 5C / 5R = 93 claims

### 파일
- THEORY/working/CV115_ACTION_TEMPORAL_COST/ (00–10 파일)
- CODE/experiments/exp89_endpoint_vs_action_temporal_cost.py (scaffold)
```

---

## §5. 파일별 실제 수정 순서 (사용자 승인 후)

| 순서 | 파일 | 작업 | 비고 |
|---|---|---|---|
| 1 | THEORY/CHANGELOG.md | §4 draft 최상단 삽입 | 가장 먼저 |
| 2 | THEORY/canonical/theorem_status.md | §2 draft 삽입 + 카운트 업데이트 | CV-1.15 섹션 추가 |
| 3 | THEORY/canonical/hypothesis_tree.md | §3 draft 삽입 | H-COMP 업데이트 |
| 4 | THEORY/canonical/canonical.md | §1 draft 삽입 (§13 끝부분) | K symbol 주석 포함 |
| 5 (완료) | CODE/experiments/exp89_endpoint_vs_action_temporal_cost.py | 3-case 검증 완료 (PASS) | exp89_results.json 저장됨; numerical validation only, not proof |

---

*작성: 2026-05-12. 실제 파일 수정 없음 — draft block만.*
