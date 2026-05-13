---
id: ACT-09
type: working/theory
status: open — promotion 전 최종 감사
created: 2026-05-12
session: W7 carry-forward
scope: 내부 일관성 감사, canonical 충돌 확인, promotion readiness 판정
---

# 09. 최종 감사 (Pre-Promotion Audit) — CV-1.15

---

## §1. 감사 방법

CV115_ACTION_TEMPORAL_COST/ 9개 파일 전체 독해 + canonical.md 크로스체크.
확인 항목: (A) φ fingerprint 충돌, (B) K symbol 충돌, (C) Sinkhorn OPEN 유지, (D) 프레이밍 ("대체" vs "refinement"), (E) 수학 오류.

---

## §2. 확인 결과 (사실)

### A. Fingerprint φ 정의 — canonical 충돌 없음 ✓

CV-1.15 정의 (02 파일):

$$\varphi_i(x) = (u_i(x),\; \mathrm{Cl}_i(u_i)(x),\; D_i(x;\,1-u_i)) \in \mathbb{R}^3$$

canonical §8.5 확인 (canonical.md line 634, 982):

> "3-component cohesion fingerprint φ(x) = (u(x), Cl(u)(x), D(x;1−u)) — the resolvent diagonal C(x,x) was demoted from the canonical fingerprint (contributes <0.4%)"

**결론**: CV-1.15 fingerprint 정의가 canonical §8.5와 일치. 4성분 버전 (resolvent diagonal 포함)을 optional로 언급하고 3성분을 기본으로 쓴 것도 canonical 방침과 동일. ✓

---

### B. K Symbol 충돌 — 주의 필요 ⚠️

**문제**: canonical.md 전반에서 $K$ = 형성(formation) 수 (예: $K=2$).
CV-1.15에서 $K_{i\to k}$ = raw Gibbs kernel (행렬).

**충돌 범위**:
- 04_softmin_gibbs_semigroup.md: "$K_{i\to k}$는 raw Gibbs kernel" 반복 사용
- canonical.md: "K transport plans $\mathbf{M}^k_{t\to s}$, one per formation" (line 981) — 여기서 $k$는 formation 인덱스

**완화 조건**: CV-1.15 문서 내에서는 $K$가 항상 Gibbs kernel context에서만 사용됨. $K$ = formation 수 notation은 $K=1$, $K=2$ 등 scalar 맥락에서만 나타남. 행렬 vs scalar이므로 문맥상 구분 가능.

**권고**: canonical promotion 시 Gibbs kernel에 다른 기호 사용. 후보: $\mathbf{G}_{i\to k}$ 또는 $\mathcal{K}_{i\to k}$ 또는 $\mathbf{K}_{i\to k}$ (볼드체). 07_promotion_draft.md에서 사전 주석 삽입 필요.

**판정**: ⚠️ minor fix 필요 (promotion 시 기호 명확화)

---

### C. Sinkhorn OPEN 유지 확인 ✓

모든 파일에서 Sinkhorn-scaled plan semigroup을 "OPEN (proved failure)" 또는 "일반적으로 성립 안 함"으로 일관되게 표기.

| 파일 | Sinkhorn 판정 표현 |
|---|---|
| 00_goal.md | "Sinkhorn-scaled plan semigroup: scaling vector 호환성 보장 없음; generically fails" |
| 05_relation_to_sinkhorn.md | "T-SINKHORN-PLAN-SEMIGROUP-FAILS-GENERICALLY: OPEN (proved failure)" |
| 07_promotion_draft.md | "Warning T-SINKHORN-PLAN-SEMIGROUP-FAILS-GENERICALLY: OPEN — proved failure" |
| 08_gap_audit.md | "OPEN (proved failure)" |

**결론**: 일관됨. OP-0012-SINK OPEN 유지 명시 완전. ✓

---

### D. "대체" vs "composition-compatible refinement" 프레이밍 ⚠️

**발견**: 00_goal.md line 17에서 "cost 구조를 endpoint similarity에서 action-based path inheritance로 **전환**한다"는 표현이 있음. "전환"은 "대체(replacement)"로 읽힐 수 있음.

**사실 확인**: action cost는 **기존 SCC temporal cost의 "refinement"**이어야 한다. 기존 endpoint/Sinkhorn cost를 완전히 대체하는 것이 아니라, composition-compatible 버전을 추가/정제하는 것.

**구체적 의존 관계**:
- T-Temporal-Identity (canonical §8.5, Cat A, CV-1.13)는 score matrix $S^0_{ij}$에 의존하며 action cost와 직접 연결되지 않음.
- CV-1.15 action cost는 **별도의 temporal cost 레이어**로 정의된다. 기존 temporal identity proof를 invalidate하지 않는다.

**권고**: 00_goal.md §핵심목적에 다음 문장 추가:
> "이것은 기존 endpoint/fingerprint similarity cost의 대체가 아니라, temporal composition analysis를 위한 composition-compatible refinement이다."

01_endpoint_failure.md도 동일 주의: L-ENDPOINT-NONSEMI는 "endpoint cost의 temporal composition incompatibility"를 보일 뿐, 기존 T-Temporal-Identity를 부정하지 않는다.

**판정**: ⚠️ minor fix 필요 (framing 명확화)

---

### E. 수학 오류 검토

#### E.1 T-ACT-DP 증명 (03 파일)

양방향 부등식 구조:
- ($\geq$): 임의 경로 P → $\mathcal{A}_{i:k}(P) \geq \mathrm{BV}$ → infimum 취함. ✓
- ($\leq$): argmin $y^*$ + 최적 경로 이어붙임 → $\mathcal{A}_{i:k}(P^*) = \mathrm{BV}$ → $c \leq \mathrm{BV}$. ✓

**미세 사항**: ($\geq$) 방향에서 $\inf_P \mathcal{A}_{i:k}(P) \geq \mathrm{BV}$를 도출할 때, 유한 site set이면 inf = min이므로 OK. 문서에서 "$c_{i\to k}^{\mathrm{act}}(x,z) = \inf_P \mathcal{A}_{i:k}(P)$"로 표기했는데 유한 site에서 min = inf이므로 수학적으로 무결. ✓

#### E.2 T-ACT-GIBBS 증명 (04 파일)

경로 집합의 disjoint union 분해 + action additivity + exp 인수분해. ✓

**미세 사항**: $K_{i\to k}(x,z) > 0$ 보장. $a_\ell(x,y) \geq 0$ (L-FINGERPRINT-ACTION-ADMISSIBLE) + 유한 경로 수 → $K_{i\to k}(x,z) \geq \exp(-M/\varepsilon) > 0$ (단 $M = \max \mathcal{A}$). $-\varepsilon\log$ 적용 가능. ✓

#### E.3 L-SOFTMIN-HARDMIN-BOUND (04 파일)

표준 log-sum-exp 부등식. 양방향 bound 도출 정확. Tightness 설명 정확. ✓

#### E.4 T-SINKHORN-PLAN-SEMIGROUP-FAILS (05 파일)

$M_1 M_2 = \mathrm{diag}(a_1) K_{ts} \mathrm{diag}(b_1 \odot a_2) K_{sr} \mathrm{diag}(b_2)$의 전개.

**미세 사항**: 등호 조건 "$\mathrm{diag}(b_1 \odot a_2) = c\cdot I$"는 충분 조건이지, **필요충분 조건이 아닐 수 있다**. 왜냐하면 $K_{ts}$가 특수한 구조를 가지면 $b_1 \odot a_2 \neq c\cdot\mathbf{1}$이어도 등호가 성립할 수 있다.

더 정확한 표현: "$b_1 \odot a_2 \neq c\cdot\mathbf{1}$이면 일반 $K$에 대해 등호 불성립"이다. 반례는 일반 위치에서의 $K$에 대해 구성되었으므로 "generically fails" 결론은 유효. ✓

**권고**: 05 파일 §2에서 "등호 조건" 표현을 "충분 조건" 또는 "일반 $K$에 대한 조건"으로 정확화 가능. 단, 결론 ("generically fails") 자체는 유효하므로 필수 수정 아님.

---

## §3. 내부 일관성 확인

| 항목 | 파일 간 일관성 | 비고 |
|---|---|---|
| φ fingerprint 3성분 | ✓ (02, 07 파일 동일) | canonical 동일 |
| T-ACT-GIBBS의 K = raw Gibbs kernel | ✓ (모든 파일) | canonical K=formation 수와 symbol 충돌 주의 |
| Sinkhorn OPEN | ✓ (00, 05, 07, 08 파일) | 일관됨 |
| δ_eff=0 조건부 표현 | ✓ (03, 08 파일: "action direct cost 정의 하에서만") | non-overclaim 유지 |
| Cat A/B/OPEN 판정 | ✓ (07, 08 파일 동일 표) | 일관됨 |
| OP-0012-SINK OPEN 유지 | ✓ (05, 07, 08 파일) | 일관됨 |

---

## §4. 승격 가능 항목 (Cat A 후보)

모두 수학적으로 완결된 증명 보유:

| ID | 핵심 | 조건 | 파일 |
|---|---|---|---|
| L-ENDPOINT-NONSEMI | endpoint² 합성 불가 반례 | $\mathbb{R}^1$, 임의 $x\neq z$ | 01 |
| L-ACTION-NORMALIZATION | 등속 경로 time-normalized cost additive | 등속 경로만 | 01 |
| L-FINGERPRINT-ACTION-ADMISSIBLE | $a_i\geq0$ + additivity | 구조적 확인 | 02 |
| **T-ACT-DP** | Bellman: $c^{\mathrm{act}}=\min_y[\ldots]$ | 유한 site, additive action | 03 |
| L-ACTION-DELTA-EFF-ZERO | $\delta_\mathrm{eff}=0$ | action direct cost 정의 하에서만 | 03 |
| **T-ACT-GIBBS** | $K_{i\to k}=K_{i\to j}K_{j\to k}$ | 유한 site, $\varepsilon>0$, additive | 04 |
| L-SOFTMIN-HARDMIN-BOUND | $|\mathrm{smin}_\varepsilon-\min|\leq\varepsilon\log N$ | 표준 | 04 |
| L-SOFT-ACTION-DELTA-EFF-ZERO | $\delta^\varepsilon_\mathrm{eff}=0$ | T-ACT-GIBBS 귀결 | 04 |

## §5. Cat B 조건부 항목

| ID | 핵심 조건 | 비고 |
|---|---|---|
| T-ACT-KERNEL-COMP→REL | (GK) + (stable-K) + (margin) | canonical §8.5 정의 변경 필요 |
| P-SINKHORN-STABILITY-CONDITIONAL | H-SINK + MARGIN + SMALL-SINK-GAP | H-SINK 별도 미증명 |

## §6. OPEN 항목

| ID | 이유 |
|---|---|
| T-SINKHORN-PLAN-SEMIGROUP-FAILS | proved failure (generically false); OP-0012-SINK 유지 |
| OP-0012-SINK | Sinkhorn scaling gap bound 없음 |
| action kernel canonical 채택 여부 | CV-1.16 이후 결정 |
| fingerprint 3 vs 4성분 | 별도 실험 필요 |
| continuous-time limit | Γ-수렴 미분석 |

---

## §7. Canonical 삽입 시 주의 문장

### 7.1 K symbol 충돌 방지

> **(주의)** 이 섹션에서 $\mathbf{K}_{i\to k}$ (볼드체)는 Gibbs 전이 kernel을 뜻하며, 기존 canonical 표기의 $K$ (이탤릭, formation 수)와 구별한다.

canonical §13 삽입 시 반드시 이 주석을 서두에 포함할 것.

### 7.2 "refinement" 표현

> **(비고)** CV-1.15의 action cost는 기존 temporal identity cost (T-Temporal-Identity, §8.5)의 **대체가 아니라 composition-compatible refinement**이다. T-Temporal-Identity 증명은 score matrix $S^0_{ij}$ 기반이며 CV-1.15와 독립적으로 유효하다.

### 7.3 δ_eff=0 scope 제한

> L-ACTION-DELTA-EFF-ZERO는 $c^\mathrm{act}$를 direct cost로 **재정의**했을 때만 성립한다. 기존 endpoint cost, fingerprint similarity cost, Sinkhorn plan에는 적용되지 않는다.

---

## §8. theorem_status.md 업데이트 초안

`theorem_status.md` Cat A 섹션 끝 (현재 59A 이후) 삽입용:

```
### CV-1.15 Action-Based Temporal Succession Package (2026-05-12)

| 행 | ID | 내용 | 판정 |
|---|---|---|---|
| (new) | L-ENDPOINT-NONSEMI | endpoint² cost는 composition-incompatible (반례: x=0,z=2 ∈ ℝ) | Cat A |
| (new) | L-ACTION-NORMALIZATION | time-normalized cost는 등속 경로에서 additive (선형 보간 대수 증명) | Cat A |
| (new) | L-FINGERPRINT-ACTION-ADMISSIBLE | SCC fingerprint action a_i≥0 + additive; T-ACT-DP/GIBBS 전제 충족 | Cat A |
| (new) | T-ACT-DP | hard-min action cost Bellman DP: c^act_{i→k}=min_y[c^act_{i→j}+c^act_{j→k}] | Cat A |
| (new) | L-ACTION-DELTA-EFF-ZERO | δ_eff=0 under action direct cost definition (T-ACT-DP 귀결) | Cat A |
| (new) | T-ACT-GIBBS | Gibbs kernel semigroup: K_{i→k}=K_{i→j}K_{j→k} (Chapman-Kolmogorov) | Cat A |
| (new) | L-SOFTMIN-HARDMIN-BOUND | smin_ε 오차: min−ε log N ≤ smin_ε ≤ min | Cat A |
| (new) | L-SOFT-ACTION-DELTA-EFF-ZERO | soft-min δ_eff^ε=0 (T-ACT-GIBBS 직접 귀결) | Cat A |
| (new) | P-ACTION-PATH-INHERITANCE | action cost = path inheritance 해석 (definition justification) | Interpretation |
| (new) | T-ACT-KERNEL-COMP→REL | Gibbs kernel + Lemma 6 → relation composition (GK+stable-K+margin 조건부) | Cat B |
| (new) | T-SINKHORN-PLAN-SEMIGROUP-FAILS | Sinkhorn plan semigroup generically fails (b₁⊙a₂≠c·I 반례) | OPEN (proved failure) |
| (new) | P-SINKHORN-STABILITY-CONDITIONAL | H-SINK+MARGIN+SMALL-SINK-GAP 조건부 relation 보존 | Cat B |

OP-0012-SINK 업데이트:
  이전: "δ_eff bound 없음"
  CV-1.15 이후: δ_eff blocker는 action cost 재정의 시 0 (Cat A). 남은 blocker: Sinkhorn scaling gap.
  상태: OPEN 유지. 필요: L-δ_eff-SINK + L-Eff-Sinkhorn.
```

---

## §9. hypothesis_tree.md 업데이트 초안

기존 H-COMP 가지에 CV-1.15 추가:

```
H-COMP (OP-0012 계열):

├── H-COMP-KERNEL (CV-1.14, Cat B — 완결)
│   └── R[M∘M] = R[M]∘R[M] (stable-K + margin)

├── H-COMP-ACTION  [NEW, CV-1.15]
│   ├── L-ENDPOINT-NONSEMI: endpoint² 합성 불가 (Cat A)
│   ├── T-ACT-DP: hard-min Bellman DP (Cat A)
│   ├── T-ACT-GIBBS: Gibbs kernel semigroup K_{i→k}=K_{i→j}K_{j→k} (Cat A)
│   └── T-ACT-KERNEL-COMP→REL: (GK)+(stable-K)+(margin) → R 합성 (Cat B)
│       → action kernel level: cost/Gibbs level 닫힘; canonical M 재정의 필요

└── H-COMP-SINK (OP-0012-SINK — OPEN)
    ├── T-SINKHORN-PLAN-SEMIGROUP-FAILS: b₁⊙a₂≠c·I generically (proved failure)
    ├── CV-1.15 기여: cost-level δ_eff blocker 해소 (action cost 재정의 시)
    └── 잔여: Sinkhorn scaling gap bound → L-δ_eff-SINK + L-Eff-Sinkhorn 필요
```

---

## §10. CV-1.15 Promotion Readiness 판정

### 판정: **READY AFTER MINOR FIXES**

**필수 수정 (minor, 증명 변경 없음)**:

1. **K symbol 명확화**: canonical 삽입 시 Gibbs kernel을 $\mathbf{K}_{i\to k}$ (볼드) 또는 $\mathcal{K}_{i\to k}$로 변경하여 formation 수 $K$와 구별. 또는 서두에 주석 명시.

2. **"전환" → "refinement" 프레이밍**: 00_goal.md + canonical 삽입 블록에서 action cost가 기존 temporal cost의 "대체"가 아니라 "composition-compatible refinement"임을 명시.

**선택적 수정**:

3. **T-SINKHORN-PLAN-SEMIGROUP-FAILS §2 등호 조건 정확화**: 현재 표현 "$b_1\odot a_2 = c\cdot I$가 충분 조건"을 "$K$의 일반 위치에서 반례 구성"으로 정확화. 결론은 동일하므로 필수 아님.

4. **exp89 구현 완료**: 이론 검증용. promotion 조건은 아니지만 병행 권장.

**왜 READY가 아닌가**: K symbol 충돌이 canonical.md에 삽입될 경우 독자 혼란을 유발할 수 있음 (formation K vs Gibbs kernel K). 이 충돌은 1문장 주석으로 해결 가능하므로 "READY AFTER MINOR FIXES".

**왜 NOT READY가 아닌가**: Cat A 8건 모두 수학적으로 완결된 증명 보유. Sinkhorn OPEN 명시 완전. canonical 오염 없음.

---

*작성: 2026-05-12. 감사 기준: φ fingerprint 충돌, K symbol 충돌, Sinkhorn OPEN, framing, 수학 오류.*

---

## §11. exp89 수치 검증 결과 반영 (2026-05-13 추가)

### exp89 실행 결과 (experiments/results/exp89_results.json)

| Case | 항목 | 결과 | 기대 | 판정 |
|---|---|---|---|---|
| A (1D analytic) | endpoint_residual | 2.0 | 2.0 | PASS |
| A (1D analytic) | time_normalized_residual | 0.0 | 0.0 | PASS |
| B (2D K=1, n=10) | endpoint_residual | 80.0 | > 0 | PASS |
| B (2D K=1, n=10) | action_residual_2hop | 0.0 | ≈ 0 | PASS |
| B (2D K=1, n=10) | action_dp_3hop_residual | 0.0 | ≈ 0 | PASS |
| B (2D K=1, n=10) | soft_residual (ε=0.01) | 2.84e-14 | ≈ 0 | PASS |
| B (2D K=1, n=10) | sinkhorn_residual (ε=0.01) | 0.0287 | > 0 | PASS |
| C (2D K=2, n=10) | action_residual_2hop | 0.0 | ≈ 0 | PASS |
| C (2D K=2, n=10) | soft_residual (ε=0.01) | 2.84e-14 | ≈ 0 | PASS |
| C (2D K=2, n=10) | sinkhorn_residual (ε=0.01) | 0.0173 | > 0 | PASS |

**해석**: exp89 numerically confirms the hierarchy: endpoint residual nonzero, action/Gibbs residual zero up to numerical tolerance (~2.84e-14 ≈ machine ε), Sinkhorn-scaled plan residual nonzero.

**주의**: exp89는 수학적 proof가 아닌 numerical validation / sanity check이다. Cat A 판정의 근거는 01–04 파일의 수학 증명이다. exp89는 이론과의 정합성을 수치로 확인한다.

---

### §11.1 업데이트된 Promotion Readiness 판정

이전 판정 (§10): **READY AFTER MINOR FIXES** — K symbol 명확화 + "refinement" 프레이밍 수정 필요.

exp89 완료 후 업데이트: **READY FOR USER APPROVAL**

이유:
- P1: Cat A lemma 8건 증명 완료 ✓
- P2: Sinkhorn plan semigroup OPEN 명시 완전 ✓
- P3: 반례 존재 (L-ENDPOINT-NONSEMI, 1D analytic) ✓
- P4: exp89 구현 및 3-case 검증 완료 (endpoint/action/soft/Sinkhorn 모두 기대 방향 확인) ✓
- P5: canonical.md 직접 수정 없음 ✓
- P6: 절대금지 항목 비위반 확인 ✓
- **P7: 사용자 승인 대기**

minor fixes (K symbol → 10_patch_plan.md §1 주석 블록으로 처리; "refinement" 프레이밍 → 10_patch_plan.md §1 비고 블록으로 처리)는 canonical 삽입 시 draft block에 이미 포함됨.

적용 순서 (승인 후): CHANGELOG → theorem_status → hypothesis_tree → canonical.

*업데이트: 2026-05-13. exp89_results.json 기준.*

---

## §12. 2026-05-13 audit pass — amendments applied (R-C + S-i)

This section records the second-pass audit performed 2026-05-13 (after exp89 PASS), which expanded the "READY AFTER MINOR FIXES" judgment of §10 with additional findings and applied them as amendments.

### §12.1 Findings applied to 10_patch_plan.md (via 04_proposed_amendments.md)

| Finding (label from 2026-05-13 audit) | Severity | Action applied |
|---|---|---|
| §2 CV-1.14 dependency | MEDIUM | **R-C** chosen: CV-1.15 §13.Y background + T-ACT-KERNEL-COMP→REL annotation rewritten to cite CV-1.14 T-CC-StableK-Kernel as *working candidate*, not canonical. T-ACT-KERNEL-COMP→REL Cat B status preserved with explicit "conditional on CV-1.14 promotion" annotation. |
| §3 style mismatch | LOW | **S-i** chosen: single §13.Y block split into per-category inserts (Cat A insert + Cat B insert + §12 OPEN insert + Interpretation insert). |
| 1.2a "fingerprint similarity cost" undefined | LOW | Parenthetical added inside L-ACTION-DELTA-EFF-ZERO 주의-line: "(the standard SCC self-referential cost $c[u_t, u_s]$ used in single-formation transport, canonical §8.5; cf. T-Temporal-Identity score matrix derivation)" |
| 1.2b "temporal identity cost" semantic slip | LOW | §13.Y refinement-framing note rephrased to reference "T-Temporal-Identity (§13 Cat A; based on score matrix $S^0_{ij}$ derived from $c[u_t, u_s]$ of §8.5)" instead of "T-Temporal-Identity (§8.5)". |
| 1.3b $\varepsilon$ vs $\varepsilon_{\mathrm{OT}}$ collision | MEDIUM | (기호 주의 — 2) note added to canonical insert header explicitly distinguishing the two parameters. |
| 1.4a L-FINGERPRINT-ACTION-ADMISSIBLE under-stated conditions | LOW | Explicit condition list added: "$\varphi_i$ Lipschitz, $\Delta t_i > 0$, $d_i \geq 0$, $a_i$ per D-LOCAL-ACTION". |
| 1.4b L-SOFTMIN-HARDMIN-BOUND under-stated conditions | LOW | Explicit condition list added: "$a \in \mathbb{R}^N$, $N$ finite, $\varepsilon > 0$". |
| 1.5 §8.5 cross-reference target | LOW | Header note updated to "(§13 Cat A; $S^0_{ij}$ from §8.5)" — see 1.2b. |
| 1.7 exp89 missing from CHANGELOG file list | LOW | CHANGELOG draft §"Files updated" includes exp89 file paths. |
| §2.4 Cat B header staleness (pre-existing) | LOW (hygiene) | Cat B header amended to record T-Temporal-Identity's CV-1.13 promotion to Cat A. |
| 1.3a $a_\ell$ vs $a$ (Sinkhorn row scaling) | LOW | **DEFERRED.** Purely internal stylistic; revisit if T-SINKHORN-PLAN-SEMIGROUP-FAILS body becomes a canonical Cat B + theorem (currently OPEN in §12 Warning subsection). |
| 1.3c $c$ has six superscripts | LOW | **ACCEPTED.** All six superscripts are defined inline in the Cat A insert; no rename. |

### §12.2 Updated readiness judgment

- §10 (2026-05-12): READY AFTER MINOR FIXES (K symbol clarity + refinement framing).
- §11 (2026-05-13 morning, post exp89 PASS): READY FOR USER APPROVAL.
- **§12 (2026-05-13 audit pass): READY FOR USER APPROVAL + AMENDMENTS APPLIED.**

All Cat A 8-entry proofs unchanged. All claim counts unchanged (+8A +2B → 67A/16B/5C/5R = 93 claims, Interpretation row excluded). Symbol clarity, refinement framing, scope restrictions, condition explicitness all updated.

The amendments source is `THEORY/logs/daily/2026-05-13/04_proposed_amendments.md` §A–§E. The user has authorized full apply 2026-05-13 ("go without question"); the canonical / theorem_status / hypothesis_tree / CHANGELOG / 10_patch_plan apply is being executed in the same session per §F apply-order.

*Updated: 2026-05-13. Audit reference: `THEORY/logs/daily/2026-05-13/02_development.md + 04_proposed_amendments.md`. P7 granted 2026-05-13 in-session.*
