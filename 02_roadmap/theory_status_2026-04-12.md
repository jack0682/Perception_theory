# Perception_theory 이론 상태 재정리 (2026-04-12)

**작성자:** Claude Code 감시  
**범위:** 04-07~04-12 전체 검토  
**대상:** Canonical Spec v2.1 + 04-03/04-06/04-07/04-10/04-11/04-12 작업  
**결론:** 이론이 **형식적 확장은 이루었으나 기초 문제는 미해결**

---

## 요약

### 현황

| 항목 | 상태 | 평가 |
|------|------|------|
| **PLAN_0403 완료** | ✅ 3개 증명 전부 작성됨 | Category A 3개 업그레이드 |
| **exp65 검증** | ❌ Type B 관찰 없음 | 04-07 "Type A vs B" 해석 기각 |
| **04-06 비판 처리** | ⚠️ 미해결 | F-1, M-1, MO-1 직면 회피 |
| **04-10~12 확장** | ✅ 광범위 | Branch selection, relaxed merge, Kramers (30+ 문서) |
| **Canonical Spec** | ⚠️ 암묵적 가정 | "고정 K/m" 제약 미명시 |

---

## I. 증명의 상태 재검증

### ✅ PLAN_0403 Tier 1 — 완전 실행

**1. C3'' 대칭화 gap 폐쇄**
```
파일: /docs/04-03/proof/C3-SYMMETRIZATION-COMPLETE.md
길이: 상세 증명 (수십 페이지)
방법: Conjugation identity → Schur complement → quadratic form
검증: FD 상대오차 < 1e-8
결과: C-Axioms Category C → A 업그레이드
```
**평가:** 엄밀하고 체계적. 논리 간극 없음.

**2. T-Persist-1(b) 무조건화**
```
파일: /docs/04-03/proof/T-PERSIST-1B-UNCONDITIONAL.md
길이: 상세 증명
방법: Sard + Kupka-Smale genericity
조건 제거: Generic transversality (GT), Non-degeneracy (NB) → residual set에서 자동
결과: Category B → A 업그레이드
```
**평가:** 개념적으로 타당. Genericity 논리 명확.

**3. Transport confinement tight bound**
```
파일: /docs/04-03/proof/TIGHT-CONFINEMENT-FINAL.md
길이: 상세 증명
개선: 33-116× overconservative → 2.4-3.5× (eps_OT=1.0)
방법: Formation-aware decomposition (core, boundary 분리)
결과: T-Persist-1(e) 무조건화 기여
```
**평가:** 실제 개선을 보여줌. 수치로 검증됨.

### 결론

**PLAN_0403은 약속대로 완료되었다.** Category A 3개 추가, 이론 완성도 88% → 91% (예상).

---

## II. exp65 Formation Tracking — 검증 실패

### 설계 의도

"Type A vs Type B" 분류 검증:
- **Type A:** centered, stable, no swaps
- **Type B:** off-center, swap-prone, valley-hopping

기준:
```
Type A: max_center_offset < 0.08, swaps = 0, max_rotation < 0.35
Type B: max_center_offset > 0.12 또는 swaps > 0 또는 max_rotation > 0.75
```

### 결과

```
exp65_formation_tracking.json 전체 config:

15×15, c=0.5:  Type A     (offset=0.038, swaps=0) ✓
15×15, c=0.6:  Mixed      (offset=0.081, swaps=0)
20×20, c=0.5:  Type A     (offset=0.014, swaps=0) ✓
20×20, c=0.6:  Type A     (offset=0.024, swaps=0) ✓

Type B 관찰: 0/4 configs
Mixed 경계: 1/4 configs
```

### 해석

**exp62 vs exp63 부호 차이는 "Type A vs B"이 아니다:**
- exp62: global mass-sweep optimization (모든 K=2 상태 탐색)
- exp63: local K=2 base point에서 perturbation (특정 minimizer)
- 이 둘은 완전히 다른 optimization problem

exp65가 대부분 Type A를 찾은 것은:
- 실제로 대부분의 config이 centered formations을 가짐
- 혹은 Type A/B 정의 자체가 "energy landscape에 없는 distinction"

### 결론

**04-07의 "Type A vs Type B" 해석은 exp65로 검증되지 않았다.** 모든 config이 Type A이거나 경계선.

---

## III. 04-06 CRITICAL 비판에 대한 응답 — 미해결

### F-1: "K=2 global stability는 정확하지만 vacuous"

**04-06 지적:**
```
K=2 (m1=30, m2=30):  E = 4.66
K=1 (m=60):          E = 2.25  ← K=2의 50% 저렴

고정 K 제약이 없으면 K=1로 merge.
따라서 K=2 "global stability"는 고정 K라는 scaffolding 위에서만 의미.
```

**04-07~12 응답:**
- ⚠️ **직접 응답 없음**
- 대신 F''(M/2) = "symmetric point의 curvature" 분석으로 topic shift
- 이는 "K=1과 K=2 사이 비교"가 아니라 "K=2 내부의 symmetric point vs asymmetric point"

**평가:** **비판이 정면으로 해결되지 않았다.**

### M-1: "K=1은 ALWAYS 에너지상 선호"

**04-06 지적:**
```
M₂ landscape: E(m1, m2) = E_self(u1*) + E_self(u2*) + E_rep
m2 → 0일 때 E → E_K1(m=M)  [단조 감소]
따라서 K=1 limit이 global minimum
```

**04-07~12 응답:**
- ⚠️ **언급 없음**
- "K=1 vs K=2 선택 문제"가 04-10 이후에도 다루어지지 않음
- 대신 "K=2 내부에서 branch selection" 문제로 축소

**평가:** **근본적 우월성 (K=1 < K=2)이 Spec에 반영되지 않았다.**

### MO-1: "M₂가 smooth manifold가 아니므로 smooth Morse theory 불가"

**04-06 지적:**
```
Σ²_M = Σ_m1 × Σ_m2는 manifold with corners
Smooth Morse theory 적용 불가 → stratified Morse theory 필요
```

**04-07~12 응답:**
- ⚠️ **언급 없음**
- 04-10 "relaxed merge" 분석에서 Morse-related 이론 계속 사용
- Stratified Morse theory로 전환하지 않음

**평가:** **기초적 수학 문제 (manifold with corners)가 미해결.**

---

## IV. 04-10부터의 주제 확장 분석

### 확장된 작업 (04-10~12)

**Branch Selection (R1):**
- exp66-73: lambda_rep sweep, branch continuation, branch catalog
- 20개+ audit & proof 문서
- "branch-conditioned vocabulary" 도입 (branch type A, B, γ_eff)

**Relaxed Merge:**
- "Zero-repulsion automorphism branch degeneracy"
- "Positive-repulsion overlap-selection"
- Core dissolution lower bounds
- 15개+ 문서

**Kramers Rate:**
- Communication-height large-deviation
- Fixed-stratum Eyring-Kramers
- 10개+ 문서

### 문제점

**1. 기초 가정과의 충돌**

F-1 비판: K=2가 K=1보다 비쌈 → K=2 선택이 에너지로 정당화되지 않음

하지만 04-10~12는:
- "K=2 내에서 어느 branch가 선택되는가?"
- "K=2가 주어졌을 때 merge가 얼마나 느린가?"

즉, **K=2의 정당성 없이 K=2 안의 문제를 풀고 있음.**

**2. Type A/B의 계속 사용**

exp65에서 Type B가 나타나지 않았는데도:
- 04-10 "branch-conditioned" 개념 계속 사용
- "branch type A" "branch type B"로 재명명
- 하지만 검증 근거가 exp65 실패

**3. 순환 논리 위험**

```
가정: K=2가 있다 (F-1이 정당화되지 않았는데도)
  ↓
Branch selection 분석 (30개+ 문서)
  ↓
결론: K=2 안의 branch가 선택됨
  ↓
그러나 근본 질문 회피: K=2가 왜 존재하는가?
```

---

## V. Canonical Spec v2.1의 명시적 문제점

### 문제 1: 암묵적 가정

**Spec이 명시하지 않은 것:**

```
"모든 K-field 정리는 다음을 가정:
 - 고정 K (per-formation mass m_j 고정)
 - 고정 m (total mass M 고정)
 - Σ²_M (또는 Σᴷ_M) 위에서만 정의됨"
```

**결과:**
- Category A 35개 중 몇 개가 K-field 관련?
- 이들이 "unconstrained energy minimization" 관점에서 의미 있는가?
- 아니면 "고정 K manifold 위에서만" 의미 있는가?

### 문제 2: F-1 비판의 미반영

**Spec에 추가되어야 할 사항:**

```
"IMPORTANT: K-field global stability (T-Persist-K-Sep 등)는
다음 조건 하에서만 성립:
 - Per-formation mass 제약이 EXTERNAL에서 imposed
 - 즉, K=2 manifold Σ²_M이 사전에 선택됨
 - 에너지 최소화만으로는 K 결정 불가
 - K=1이 일반적으로 K>1보다 저렴함 (F-1 확인)"
```

현재: **이 disclaimer 없음**

### 문제 3: Category 분류의 명확성

**예시:**

```
T-Persist-K-Sep (Category B)
Statement: "Well-separated regime에서 persistence 보증"

가정이 명시되어 있는가?
- "Well-separated"의 정의? (Λ_coupling 값?)
- "Generic parameters"?
- "Fixed K manifold 위에서"?
```

현재: **이런 qualifier들이 informal하거나 누락**

---

## VI. 최종 진단

### 강점

| 항목 | 설명 |
|------|------|
| **PLAN_0403 완료** | 3개 증명 엄밀함. C3'', Basin, Transport 실제로 업그레이드. |
| **광범위한 탐색** | 04-10~12 branch selection, relaxed merge, Kramers rate 상세 개발. |
| **수치 검증** | exp65, exp66-79 데이터 수집 및 분석 수행. |

### 약점

| 항목 | 설명 | 심각도 |
|------|------|--------|
| **F-1 미해결** | "K=2 vacuous" 비판 정면 회피 | 🔴 CRITICAL |
| **exp65 검증 실패** | Type B 없음. "Type A vs B" 해석 기각. | 🔴 CRITICAL |
| **기초 가정 암묵적** | "고정 K" 제약 Spec에 미명시. | 🟠 HIGH |
| **MO-1 미해결** | Morse theory vs manifold with corners | 🟠 HIGH |
| **주제 확장의 방향성 의문** | K=2 정당성 없이 K=2 내부 분석 | 🟠 HIGH |

### 평가

**형식적으로:** ✅ 이론이 진전했다. PLAN_0403 완료, 30개+ 새 문서, Category A 3개 추가.

**개념적으로:** ❌ 근본적 문제(F-1, exp65, 암묵적 가정)가 미해결. 대신 "K=2 내부"로 focus narrowing → main criticism을 회피하는 구조.

**결론:** 이론이 **형식적 확장은 이루었으나 기초 비판은 정면으로 다루지 않은 상태**. Canonical Spec v2.1은 재검토 필요.

---

## VII. 권고 작업

### A. 즉시 (우선순위 1)

1. **Canonical Spec v2.2 정정 작업**
   - 각 K-field 정리에 "고정 K 제약" 명시
   - F-1 비판 수용/반박 공식 성명
   - Morse theory MO-1 비판 처리 (포기 또는 stratified로 전환)

2. **exp65 결과 재해석**
   - Type A/B 분류 철회 또는 재정의
   - exp62/exp63 divergence의 **실제 원인** 파악 (manifold structure? optimizer path?)

### B. 중기 (우선순위 2)

3. **F-1 비판의 정면 대응**
   - "Model selection mechanism" (BIC, free energy, birth-death) 도입
   - K 결정 이론 개발
   - 현재 spec의 "K fixed" 제약을 명시적으로 수용

4. **Branch selection 작업의 위치 재정의**
   - "이것은 K=2 정당성을 보완하지 않는다" 명시
   - Orthogonal한 문제임을 명확히

### C. 장기 (우선순위 3)

5. **Morse theory 재구성**
   - Stratified Morse 도입 (MO-1 해결)
   - 또는 M₂ 분석 포기 및 다른 접근법 모색

---

## 참고: 메모리 업데이트

새 파일:
- `/Users/ojaehong/.claude/projects/-Users-ojaehong-Perception/memory/AUDIT_REPORT_2026-04-12.md`

갱신:
- `/Users/ojaehong/.claude/projects/-Users-ojaehong-Perception/memory/MEMORY.md` (F_Double_Prime_Divergence 표시 업데이트)

