---
id: CC-StableK-05
type: working/promotion-draft
status: DRAFT — canonical 수정 전 검토용 초안 (not yet promoted)
created: 2026-05-12
session: W7 carry-forward
scope: T-CC-StableK-Kernel Cat B → canonical promotion draft
source: 03_gap_audit.md v2 + 03_development.md §10 (Lemma 6 Cat B 완전 증명 확인)
non-overclaim: |
  이 파일의 모든 theorem block / status update는 제안(proposal) 수준임.
  실제 canonical 수정은 별도 promotion session + user authorization 필요.
  canonical.md / theorem_status.md / hypothesis_tree.md 직접 수정 금지.
---

# 05. Promotion Draft — T-CC-StableK-Kernel (CV-1.14 후보)

---

## §1. 근거 요약

### 확인된 사실 (2026-05-12, 03_development.md §10 정밀 독해)

**[CONFIRMED]** Lemma 6 (`THEORY/logs/daily/2026-05-07/03_development.md §10`):

> *Let $u_t, u_s, u_r \in \mathcal{F}_M(\mathcal{P})$. Let $M_{t\to s}, M_{s\to r}$ be
> E1–E4-admissible transport plans. Under (I_{ts}) + (I_{sr}) — stable-K + margin on
> both intervals — define $M_{t\to r}^\mathrm{comp} := M_{s\to r} \circ M_{t\to s}$
> (matrix product). Then:*
> $$R_{t \to r}\!\left[M_{t\to r}^\mathrm{comp}\right] \;=\; R_{s\to r}\!\left[M_{s\to r}\right] \;\circ\; R_{t\to s}\!\left[M_{t\to s}\right].$$

- 증명 유형: Lemma 2 (diagonal mass lower bound) + Lemma 3-sharp (off-diagonal) + Theorem 4.2(b) (bijection from margin)
- 오차 항: 없음 ($M_{t\to r}$이 합성으로 정의되므로 ε_comp = 0)
- **현재 status**: Cat B (완전 증명, 2026-05-07 W6 D5)

---

## §2. Canonical Theorem Block (proposed, not yet inserted)

> **이 블록은 canonical.md §13 "Category B Theorems" 항목에 추가할 제안 문안이다.**
> **실제 삽입은 별도 promotion session에서 수행한다.**

---

**T-CC-StableK-Kernel (Compositional Consistency, Kernel-Composed Case). Cat B.**

*(New, CV-1.14 candidate. Source: `THEORY/logs/daily/2026-05-07/03_development.md §10`,
Lemma 6. Working file: `THEORY/working/CV114_TEMPORAL_COMPOSITION/`)*

*Let $u_t, u_s, u_r \in \mathcal{F}_M(\mathcal{P})$ be soft cohesion fields at successive
times $t < s < r$. Let $M_{t\to s}$, $M_{s\to r}$ be E1–E4-admissible transport plans.
Assume:*

- *(I_{ts}) Stable-K on $[t,s]$: $K_t = K_s = K$, well-separated regime
  ($d_\mathrm{inter}^* \geq d_\mathrm{min}^* \geq 3$), sharp-OT regime
  ($\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^*$), margin
  $\Delta_\mathrm{sep}(M_{t\to s}) \geq \Delta_\mathrm{sep}^*$.*
- *(I_{sr}) Same conditions on $[s,r]$: $K_s = K_r = K$, with $M_{s\to r}$.*

*Define the kernel-composed transport plan:*
$$M_{t\to r}^\mathrm{comp} \;:=\; M_{s\to r} \circ M_{t\to s}$$
*(matrix product / measure pushforward: $M_{t\to r}^\mathrm{comp}(x,z) = \sum_y M_{t\to s}(x,y)\,M_{s\to r}(y,z)$).*

*Then:*
$$\boxed{R_{t\to r}\!\left[M_{t\to r}^\mathrm{comp}\right] \;=\; R_{s\to r}\!\left[M_{s\to r}\right] \;\circ\; R_{t\to s}\!\left[M_{t\to s}\right]}$$

*In the stable-K bijective case, writing $\pi_{ts}$, $\pi_{sr}$, $\pi_{tr}^\mathrm{comp}$ for
the induced bijections on $[K]$:*
$$\pi_{tr}^\mathrm{comp} \;=\; \pi_{sr} \;\circ\; \pi_{ts} : [K] \to [K].$$

*Proof sketch: (1) By (I_{ts}) + Lemma 2: $\gamma_{M_{t\to s}}(C_i^t, C_{\pi_{ts}(i)}^s) \geq
(1-\eta_\mathrm{self}^K)m_i^{t,\mathrm{deep}}$ (diagonal mass lower bound). (2) By (I_{sr})
+ Lemma 2: same on $[s,r]$. (3) Composition:
$\gamma_{M_{t\to r}^\mathrm{comp}}(C_i^t, C_{(\pi_{sr}\circ\pi_{ts})(i)}^r) \geq
(1-\eta_\mathrm{self}^K)^2 \min_j m_j^{s,\mathrm{deep}}$. (4) Lemma 3-sharp on composed plan:
off-diagonal $\gamma \leq 2\eta_\mathrm{cross}^\mathrm{sharp}\min(m^t,m^r)$ (factor 2 from
leakage at either intermediate step; absorbed by per-interval margin). (5) Apply Theorem
T-Temporal-Identity (b) to $M_{t\to r}^\mathrm{comp}$: composed plan satisfies E1–E4; margin
condition at the composed level holds; bijection $\pi_{tr}^\mathrm{comp} = \pi_{sr}\circ\pi_{ts}$
is induced. $\square$*

### 한계 (Limitation) — 반드시 포함

> **이 정리는 $M_{t\to r} = M_{s\to r} \circ M_{t\to s}$로 정의된 kernel-composed 수송
> 계획에 한정된다. 독립적으로 계산된 Sinkhorn 계획
> $M_{t\to r}^\mathrm{Sink} = \mathrm{Sinkhorn}(u_t, u_r,\, c[u_t,u_r],\, \varepsilon_\mathrm{OT})$
> 에 대해서는 어떠한 것도 주장하지 않는다.**
>
> 특히:
> - $M_{t\to r}^\mathrm{comp} \neq M_{t\to r}^\mathrm{Sink}$ 일반적 (semigroup property는
>   canonical §12에서 open problem으로 명시됨)
> - $R_{t\to r}[M_{t\to r}^\mathrm{Sink}] = R_{s\to r}\circ R_{t\to s}$ 여부는 미해결
>   (→ OP-0012-SINK, §5 참조)

---

## §3. theorem_status.md 업데이트 초안 (proposed)

> **이 섹션은 theorem_status.md OP-0012 항목에 적용할 업데이트 문안이다.**
> **실제 파일 수정은 별도 session에서 수행한다.**

### 현재 OP-0012 상태 (theorem_status.md 기준, CV-1.13)

```
OP-0012 (Persistence Composition): PARTIALLY STRUCTURED
  - OP-0012-CC: stable-K 조건부 합성 일관성 — Cat B path 정의됨
  - K-jump 일반 경우: Cat C
```

### 제안 업데이트 (CV-1.14 반영)

```
OP-0012 (Persistence Composition): PARTIALLY RESOLVED

  Sub-case A — Kernel-composed plan:
    STATUS: Cat B (Lemma 6, 03_development.md §10, 2026-05-07)
    STATEMENT: Under (I_{ts})+(I_{sr}), with M_{t→r}:=M_{s→r}∘M_{t→s}:
      R[M_{t→r}^comp] = R[M_{s→r}] ∘ R[M_{t→s}]
    See: T-CC-StableK-Kernel (CV-1.14, canonical §13)

  Sub-case B — Independent Sinkhorn plan:
    STATUS: OPEN (OP-0012-SINK, new)
    BLOCKER: δ_eff lemma (c_direct vs c_eff bound) + Eff-Sinkhorn lemma
    See: THEORY/working/CV114_TEMPORAL_COMPOSITION/03_gap_audit.md §C

  Sub-case C — K-jump general:
    STATUS: OPEN, Cat C
    DEPENDENCY: OP-0008 (σ-inherit), Package II
    Unchanged from CV-1.13.

  Sub-case D — Markov-kernel with T_*:
    STATUS: OPEN, deferred post OP-0021
    Unchanged from CV-1.13.
```

---

## §4. hypothesis_tree.md 업데이트 초안 (proposed)

> **이 섹션은 hypothesis_tree.md OP-0012 관련 노드에 적용할 업데이트 문안이다.**

### 기존 hypothesis_tree OP-0012 노드 (HT-3.0/HT-3.5 기준 추정)

```
H-COMP: Can temporal correspondence compose? [OPEN, OP-0012]
  → depends on: T-Temporal-Identity Cat A [✓ CV-1.13]
```

### 제안 업데이트

```
H-COMP (OP-0012): Temporal correspondence composition
  ├── H-COMP-KERNEL: Kernel-composed plan → [CAT B, CV-1.14]
  │     T-CC-StableK-Kernel: R[M_comp] = R[M_{s→r}]∘R[M_{t→s}]
  │     Depends on: T-Temporal-Identity Cat A [✓], Lemma 6 [✓]
  │
  ├── H-COMP-SINK: Independent Sinkhorn → [OPEN, OP-0012-SINK]
  │     Blocked by: δ_eff lemma, Eff-Sinkhorn lemma
  │     Working file: CV114_TEMPORAL_COMPOSITION/03_gap_audit.md
  │
  ├── H-COMP-KJUMP: K-jump general case → [OPEN, Cat C]
  │     Blocked by: OP-0008, Package II
  │
  └── H-COMP-MARKOV: Markov-kernel formulation → [OPEN, post-OP-0021]
```

---

## §5. 새 Open Subproblem 제안: OP-0012-SINK

> **이 섹션은 theorem_status.md Open Problems Catalog에 추가할 신규 항목이다.**

---

**OP-0012-SINK** (새 subproblem, CV-1.14 제안)

**상태**: OPEN

**문제**:
Independent Sinkhorn 계획 $M_{t\to r}^\mathrm{Sink} = \mathrm{Sinkhorn}(u_t, u_r, c[u_t,u_r])$에 대해,
$\Delta > 2\varepsilon_\mathrm{comp}$ 조건 하에서 $R_{t\to r}[M^\mathrm{Sink}] = R_{s\to r}\circ R_{t\to s}$가 성립하는가?

**배경**:
T-CC-StableK-Kernel (Cat B)은 $M_{t\to r} := M_{s\to r}\circ M_{t\to s}$로 정의할 때만
성립. 실무에서는 $u_t$와 $u_r$ 사이의 OT를 직접 계산하는 경우가 표준이므로,
이 질문이 응용 측면에서 핵심.

**필요한 새 lemma**:

**Lemma δ_eff (NEW, Cat C)**:
$$\delta_\mathrm{eff} := \left\|c_\mathrm{direct}(x,z;\,u_t,u_r) - c^\mathrm{eff}(x,z;\,M_{t\to s},M_{s\to r})\right\|_\infty$$
여기서 $c^\mathrm{eff}(x,z) = -\varepsilon_\mathrm{OT}\log\!\sum_y M_{t\to s}(x,y)M_{s\to r}(y,z)/u_t(x)$.

stable-K + well-separated 하에서 $\delta_\mathrm{eff}$의 명시적 bound 유도가 핵심.

**Lemma Eff-Sinkhorn (NEW, Cat C)**:
$$\left\|M^\mathrm{Sinkhorn}(c^\mathrm{eff}) - M_{s\to r}\circ M_{t\to s}\right\|_\mathrm{TV} \leq \zeta_\mathrm{marg}$$
entropic regularization과 marginal constraint 불일치로 인한 $\zeta_\mathrm{marg}$ bound.

**ε_comp formula (proposed)**:
Lemma δ_eff와 Lemma Eff-Sinkhorn이 완성되면:
$$\varepsilon_\mathrm{comp} = \frac{2M_\mathrm{tot}\cdot\delta_\mathrm{eff}}{\varepsilon_\mathrm{OT}\cdot\min_i m_i} + \frac{\zeta_\mathrm{marg}}{\min_i m_i}$$

**T-CC-StableK-Sinkhorn 정리 (proposed, Cat C 목표)**:
Under (I_{ts}) + (I_{sr}) + $\Delta > 2\varepsilon_\mathrm{comp}$:
$$R_{t\to r}[M_{t\to r}^\mathrm{Sink}] \;=\; R_{s\to r}[M_{s\to r}] \;\circ\; R_{t\to s}[M_{t\to s}]$$

**Cat B 달성 조건**: Lemma δ_eff + Lemma Eff-Sinkhorn 모두 Cat B 이상.

**의존**: T-CC-StableK-Kernel Cat B [✓], Lemma 9 (Partial-H-SINK, Cat A) [✓], Lemma 10 (Cat B) [✓]

---

## §6. Cat 판정표 (최종)

| 정리 / 문제 | 판정 | 근거 | 제한 |
|---|---|---|---|
| **T-CC-StableK-Kernel** | **Cat B** | Lemma 6 (03_development.md §10, 완전 증명) | $M_{t\to r} := M_{s\to r}\circ M_{t\to s}$ 기준만 |
| **T-CC-StableK-Sinkhorn** | **Cat C / OPEN** | OP-0012-SINK, δ_eff 미결 | 독립 Sinkhorn 재계산 경우 |
| **K-jump composition** | **OPEN** | Cat C, OP-0008/Package II 의존 | MERGE/SPLIT 이벤트 포함 |
| Lemma δ_eff | Cat C | 신규, 미착수 | |
| Lemma Eff-Sinkhorn | Cat C | 신규, 미착수 | |

---

## §7. Promotion Pipeline 체크리스트 (T-CC-StableK-Kernel)

canonical 삽입 전 완료 조건:

- [ ] **P1** Promotion session user authorization
- [ ] **P2** canonical.md §13 Category B 항목 삽입 (§2 블록 사용)
- [ ] **P3** theorem_status.md OP-0012 항목 업데이트 (§3 문안 사용)
- [ ] **P4** hypothesis_tree.md H-COMP 노드 업데이트 (§4 문안 사용)
- [ ] **P5** 신규 OP-0012-SINK 항목 추가 (§5 문안 사용)
- [ ] **P6** CHANGELOG.md 항목 추가 (CV-1.14 세션 진입 기록)
- [ ] **P7** 실험 검증 (04_experiment_plan.md 구현 + PASS)

P7은 Cat B에 필수적이지 않으나 강력 권장 (canonical §13 표준).

---

## §8. 비과대 주장 등록

1. **T-CC-StableK-Kernel Cat B**: 커널 합성 정의 기준만. 독립 Sinkhorn에는 적용 불가. canonical 파일 아직 수정 안 됨.
2. **T-CC-StableK-Sinkhorn**: 증명되지 않음. Cat C 수준. ε_comp=0 Route B 폐기됨.
3. **OP-0012-SINK**: 신규 문제 제안. 미착수. 어떤 것도 claimed하지 않음.
4. **이 파일 전체**: 검토용 초안. user authorization 없이 canonical 반영 금지.

---

*작성: 2026-05-12 (W7 carry-forward). CV-1.14 promotion draft, 미승인 상태.*

---

## §9. CV-1.15와의 연결 (2026-05-13 추가)

> "CV-1.15 action/Gibbs kernel semigroup provides a principled source of composition-compatible raw kernels, while independent Sinkhorn recomputation remains open."

**연결 구조 요약**:

| 정리 | 출처 | 내용 | 연결 |
|---|---|---|---|
| T-CC-StableK-Kernel | CV-1.14, Cat B | M이 합성 구조 → R도 합성됨 | CV-1.15의 전제 조건 상위 정리 |
| T-ACT-GIBBS | CV-1.15, Cat A | raw Gibbs kernel K_{i→k}=K_{i→j}K_{j→k} 정확히 성립 | composition-compatible kernel 원천 제공 |
| T-ACT-KERNEL-COMP→REL | CV-1.15, Cat B | (GK)+(stable-K)+(margin) → R[K_{t→r}]=R[K_{t→s}]∘R[K_{s→r}] | T-ACT-GIBBS + T-CC-StableK-Kernel 연결 |

**T-CC-StableK-Kernel / T-CC-StableK-Sinkhorn 구분 유지**:
- T-CC-StableK-Kernel (Cat B): kernel-composed case — CV-1.14에서 완결.
- T-CC-StableK-Sinkhorn: independent Sinkhorn recomputation — CV-1.15 포함 미해결, OPEN 유지.
- T-ACT-KERNEL-COMP→REL (CV-1.15, Cat B): Gibbs kernel을 M으로 채택할 경우 T-CC-StableK-Kernel이 적용됨. canonical §8.5 M_{t→s} 정의 변경 필요 (CV-1.16 이후 결정).

*추가: 2026-05-13.*
