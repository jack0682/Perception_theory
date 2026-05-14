---
id: ACT-07
type: working/theory
status: open — CV-1.15 promotion draft
created: 2026-05-12
scope: canonical theorem block 초안, theorem_status.md 업데이트 초안,
       hypothesis_tree.md OP-0012-SINK 업데이트 초안
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 07. Promotion Draft — CV-1.15

---

## §1. Canonical Theorem Block 초안

canonical.md §13 (Theorem Catalog) 삽입용.

---

### §13.X Action-Based Temporal Succession Package (CV-1.15)

**배경**: CV-1.14에서 T-CC-StableK-Kernel (Cat B)은 M이 합성 구조를 가지면 relation도 합성됨을 보였다. CV-1.15는 action principle이 자연스럽게 합성 구조를 갖는 kernel을 산출함을 보인다.

---

**Lemma L-ENDPOINT-NONSEMI** *(Cat A)*

Squared endpoint cost $c^\mathrm{end}(x,z)=\|z-x\|^2$는 일반적으로 temporal composition과 호환되지 않는다:

$$c^\mathrm{end}_{t\to r}(x,z) \neq \min_y\!\bigl[c^\mathrm{end}_{t\to s}(x,y)+c^\mathrm{end}_{s\to r}(y,z)\bigr]$$

*반례*: $x=0,\,z=2 \in \mathbb{R}$ — 좌변 $4$, 우변 $\leq 2$. *(Proof: 01_endpoint_failure.md §L-ENDPOINT-NONSEMI)*

---

**Lemma L-ACTION-NORMALIZATION** *(Cat A)*

$t<s<r$. 선형 보간 중간점 $y^*=\frac{r-s}{r-t}x+\frac{s-t}{r-t}z$에서:

$$\frac{\|z-x\|^2}{r-t}=\frac{\|y^*-x\|^2}{s-t}+\frac{\|z-y^*\|^2}{r-s}$$

*(Proof: 01_endpoint_failure.md §L-ACTION-NORMALIZATION)*

---

**Definition D-LOCAL-ACTION** *(Definition)*

SCC local action:

$$a_i(x,y)=\frac{d_i(x,y)^2}{\Delta t_i}+\gamma\frac{\|\varphi_{i+1}(y)-\varphi_i(x)\|^2}{\Delta t_i}$$

$\varphi_i(x)=(u_i(x),\,\mathrm{Cl}_i(u_i)(x),\,D_i(x;\,1-u_i))$: SCC fingerprint ($\gamma\geq0$, $\Delta t_i>0$).

Path action: $\mathcal{A}_{i:k}(P)=\sum_{\ell=i}^{k-1}a_\ell(x_\ell,x_{\ell+1})$.

Hard-min cost: $c_{i\to k}^{\mathrm{act}}(x,z)=\min_{\mathrm{paths}\,x\to z}\mathcal{A}_{i:k}$.

---

**Lemma L-FINGERPRINT-ACTION-ADMISSIBLE** *(Cat A)*

SCC fingerprint action은 (1) $a_i\geq0$ (nonnegativity), (2) $\mathcal{A}_{i:k}=\sum_\ell a_\ell$ (additivity)를 만족하며 T-ACT-DP, T-ACT-GIBBS의 전제를 충족한다. *(Proof: 02_action_cost_definition.md §L-FINGERPRINT-ACTION-ADMISSIBLE)*

---

**Theorem T-ACT-DP** *(Cat A)*

*가정*: $X_i$ 유한 ($|X_i|<\infty$), $\mathcal{A}_{i:k}$ additive, $i<j<k$.

*결론*:

$$\boxed{c_{i\to k}^{\mathrm{act}}(x,z)=\min_{y\in X_j}\!\bigl[c_{i\to j}^{\mathrm{act}}(x,y)+c_{j\to k}^{\mathrm{act}}(y,z)\bigr]}$$

*(Proof: 03_dynamic_programming_theorem.md — 양방향 부등식)*

---

**Definition D-GIBBS-KERNEL** *(Definition)*

Local Gibbs kernel: $K_{\ell,\ell+1}(x,y)=\exp(-a_\ell(x,y)/\varepsilon)$, $\varepsilon>0$.

Long-horizon: $K_{i\to k}(x,z)=\sum_{\mathrm{paths}\,x\to z}\exp(-\mathcal{A}_{i:k}/\varepsilon)$.

Soft-min cost: $c_{i\to k}^{\varepsilon}(x,z)=-\varepsilon\log K_{i\to k}(x,z)$.

---

**Theorem T-ACT-GIBBS** *(Cat A)*

*가정*: $X_j$ 유한, $\mathcal{A}_{i:k}$ additive, $\varepsilon>0$, $i<j<k$.

*결론* (행렬 등식):

$$\boxed{K_{i\to k}=K_{i\to j}\,K_{j\to k}}$$

Soft-min recursion:

$$c_{i\to k}^{\varepsilon}(x,z)=-\varepsilon\log\!\sum_{y\in X_j}\exp\!\left(-\frac{c_{i\to j}^{\varepsilon}(x,y)+c_{j\to k}^{\varepsilon}(y,z)}{\varepsilon}\right)$$

*(Proof: 04_softmin_gibbs_semigroup.md — Chapman-Kolmogorov path-integral 분해)*

---

**Lemma L-SOFTMIN-HARDMIN-BOUND** *(Cat A)*

실수열 $a_1,\ldots,a_N$에 대해 $\operatorname{smin}_\varepsilon(a)=-\varepsilon\log\sum_i e^{-a_i/\varepsilon}$:

$$\min_i a_i-\varepsilon\log N\;\leq\;\operatorname{smin}_\varepsilon(a)\;\leq\;\min_i a_i$$

*(Proof: 04_softmin_gibbs_semigroup.md §L-SOFTMIN-HARDMIN-BOUND)*

---

**Lemma L-ACTION-DELTA-EFF-ZERO** *(Cat A, action direct cost 정의 하에서)*

Direct cost를 $c_{i\to k}^{\mathrm{act}}$로 정의하면 effective cost와 정확히 같다:

$$\delta_\mathrm{eff}=\left\|c_{i\to k}^{\mathrm{act}}-c_{i\to k}^{\mathrm{eff}}\right\|_\infty=0$$

*주의*: endpoint/fingerprint similarity direct cost에는 적용 불가. Sinkhorn plan과 무관. *(Proof: 03_dynamic_programming_theorem.md §L-ACTION-DELTA-EFF-ZERO)*

---

**Lemma L-SOFT-ACTION-DELTA-EFF-ZERO** *(Cat A)*

Soft-min 경우:

$$c_{i\to k}^{\varepsilon}=c_{i\to k}^{\mathrm{eff},\varepsilon}, \quad \delta_\mathrm{eff}^{\varepsilon}=0$$

T-ACT-GIBBS의 직접 귀결. *(Proof: 04_softmin_gibbs_semigroup.md §L-SOFT-ACTION-DELTA-EFF-ZERO)*

---

**Proposition P-ACTION-PATH-INHERITANCE** *(Definition Justification)*

SCC temporal identity는 endpoint similarity보다 low-action path inheritance에 더 잘 부합한다. SCC axiom A3 (stabilization tendency)는 경로상 작은 action을 함의하며, hard-min action cost는 이를 t→r 간 최소 action 역사 경로를 찾는 방식으로 포착한다.

---

**Theorem T-ACT-KERNEL-COMP→REL** *(Cat B 조건부)*

가정: (GK) $M_{t\to s}:=K_{t\to s}$ (Gibbs kernel로 재정의), (stable-K) $K_t=K_s=K_r=K$, (margin) $\Delta_\mathrm{sep}^{ts}>0$, $\Delta_\mathrm{sep}^{sr}>0$.

결론: $R[K_{t\to r}]=R[K_{t\to s}]\circ R[K_{s\to r}]$, 즉 $\pi_{tr}^\mathrm{comp}=\pi_{sr}\circ\pi_{ts}$.

*조건 의존성*: (GK)는 canonical §8.5의 $M_{t\to s}$ 정의 변경을 요구. → CV-1.16 이후. *(05_relation_to_sinkhorn.md §5)*

---

**Warning T-SINKHORN-PLAN-SEMIGROUP-FAILS-GENERICALLY** *(OPEN — proved failure)*

Sinkhorn-scaled plan $M^{\mathrm{sink}}(K)=\mathrm{diag}(a)K\mathrm{diag}(b)$는 일반적으로:

$$M^{\mathrm{sink}}(K_{t\to s})\cdot M^{\mathrm{sink}}(K_{s\to r})\neq M^{\mathrm{sink}}(K_{t\to r})$$

이유: $b_1\odot a_2 \neq c\cdot\mathbf{1}$ (서로 다른 transport 문제에서 결정된 scaling vector). *(05_relation_to_sinkhorn.md §2)*

---

**Proposition P-SINKHORN-STABILITY-CONDITIONAL** *(Cat B 조건부)*

H-SINK + MARGIN + SMALL-SINK-GAP 조건 하에서 induced relation이 approximate하게 보존됨. 상세 조건: 05_relation_to_sinkhorn.md §3.

---

## §2. theorem_status.md 업데이트 초안

다음을 `theorem_status.md`의 Cat A 섹션에 추가 (CV-1.15 승격 시):

```markdown
### CV-1.15 Action-Based Temporal Succession Package

| ID | 내용 | 판정 |
|----|------|------|
| L-ENDPOINT-NONSEMI | Endpoint²는 composition-incompatible | Cat A |
| L-ACTION-NORMALIZATION | Time-normalized cost는 등속 경로에서 additive | Cat A |
| L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action은 DP/Gibbs 전제 충족 | Cat A |
| T-ACT-DP | Hard-min Bellman: c^act = min_y[...] | Cat A |
| T-ACT-GIBBS | Gibbs kernel semigroup: K_{i→k}=K_{i→j}K_{j→k} | Cat A |
| L-SOFTMIN-HARDMIN-BOUND | smin_ε 오차 ≤ ε log N | Cat A |
| L-ACTION-DELTA-EFF-ZERO | δ_eff=0 under action direct cost definition | Cat A |
| L-SOFT-ACTION-DELTA-EFF-ZERO | soft δ_eff^ε=0 (T-ACT-GIBBS 귀결) | Cat A |
| P-ACTION-PATH-INHERITANCE | Action = path inheritance 해석 명제 | Interpretation |
| T-ACT-KERNEL-COMP→REL | Gibbs kernel + Lemma 6 → relation composition | Cat B |
| T-SINKHORN-PLAN-SEMIGROUP-FAILS | Sinkhorn plan semigroup generically fails | OPEN (proved failure) |
| P-SINKHORN-STABILITY-CONDITIONAL | H-SINK 조건부 relation 보존 | Cat B |
```

**OP-0012 업데이트**:

```markdown
OP-0012-SINK (Sinkhorn plan composition):
  - Blocker δ_eff: CV-1.15에서 action cost level로 재정의 시 δ_eff=0 (Cat A).
  - 남은 blocker: Sinkhorn scaling gap (b₁⊙a₂ ≠ c·I generically).
  - 상태: OPEN. 필요 lemma: L-δ_eff-SINK (cost→plan gap bound), L-Eff-Sinkhorn.
```

---

## §3. hypothesis_tree.md OP-0012-SINK 업데이트 초안

```markdown
H-COMP (OP-0012 관련 가지):

├── H-COMP-KERNEL (T-CC-StableK-Kernel, Cat B)
│   └── "kernel composition → relation composition"
│       → CV-1.14 완결

├── H-COMP-ACTION-LEVEL (CV-1.15 새 가지)
│   ├── T-ACT-DP (Cat A): action cost level Bellman DP
│   ├── T-ACT-GIBBS (Cat A): raw Gibbs kernel semigroup
│   └── T-ACT-KERNEL-COMP-REL (Cat B): Gibbs kernel + Lemma 6 조건부
│       → action kernel level partially resolved

└── H-COMP-SINK (OP-0012-SINK)
    ├── T-SINKHORN-PLAN-SEMIGROUP-FAILS (proved failure)
    │   → generically false; scaling gap b₁⊙a₂ ≠ c·I
    └── OPEN: L-δ_eff-SINK + L-Eff-Sinkhorn 필요
        → Sinkhorn-scaled plan composition remains OPEN
```

---

## §4. CV-1.15 Promotion Checklist

| 조건 | 상태 |
|---|---|
| P1: Cat A lemma 8건 증명 완료 | ✓ (01–04 파일) |
| P2: Sinkhorn plan semigroup OPEN 명시 | ✓ (05 파일) |
| P3: 반례 존재 (L-ENDPOINT-NONSEMI) | ✓ |
| P4: 실험 계획 작성 (exp89) | ✓ (06 파일) |
| P5: canonical.md 직접 수정 없음 | ✓ (이 파일은 draft만) |
| P6: 절대금지 항목 비위반 확인 | ✓ |
| P7: 사용자 승인 | **대기** |

---

*작성: 2026-05-12.*
