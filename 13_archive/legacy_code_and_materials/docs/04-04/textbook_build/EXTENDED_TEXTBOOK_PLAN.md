# Phase 15 확장 교재 계획 — 600쪽+ 대규모 교재 (Figure 통합)

**Date:** 2026-04-04 20:30 KST  
**Status:** 🟢 **확장 계획 수립 중**

---

## 📈 **확장 목표**

### 이전 계획 vs. 확장 계획

| 항목 | 이전 | 확장 | 증가 |
|------|------|------|------|
| **총 페이지** | 336pp | **600pp+** | +78% |
| **총 Figure** | 42개 | **80-100개** | +90-138% |
| **Part I** | 47pp | **80pp** | +33pp |
| **Part II** | 95pp | **160pp** | +65pp |
| **Part III** | 61pp | **100pp** | +39pp |
| **Part IV** | 84pp | **140pp** | +56pp |
| **부록 & 전문** | 49pp | **80pp** | +31pp |

**확장 방식:** 
- 더 상세한 설명 (줄글 비중 증가)
- 많은 예제 (1-2pp → 3-5pp)
- 풍부한 Figure (개념당 2-3개)
- 상세한 증명 (스케치 → 완전 증명)

---

## 🎨 **Figure 생성 계획 (80-100개 목표)**

### Figure 분류 및 수량

```
P1: 기초 개념 Figure (20-25개)
├─ 1.1 객체-중심 vs 응집도-중심 시각화 (3개)
├─ 1.2 Soft Cohesion Field 예제 (5개: 5×5, 10×10 격자)
├─ 1.3 Proto-cohesion 4요소 (각 2-3개 = 10개)
│  ├─ Bind: 예시 (3개)
│  ├─ Sep: 예시 (3개)
│  ├─ Inside: 예시 (3개)
│  └─ Persist: 예시 (3개)
├─ 1.4 역사 timeline (1개)
└─ 1.5 책 구조 다이어그램 (2개)

P2: 형식 이론 Figure (20-25개)
├─ Ch4: 공리 (4개)
│  ├─ A3 폐포 수렴 (animation series 3 frames)
│  ├─ 공리 의존성 DAG (1개)
│  └─ Sigmoid 함수와 변화 (2개)
├─ Ch5: 연산자 (5개)
│  ├─ 폐포 결과 시각화 (2개)
│  ├─ 구분 차이 시각화 (1개)
│  ├─ 리솔벤트 값 heatmap (1개)
│  └─ 응집도 지문 (1개)
├─ Ch6: 에너지 (6개)
│  ├─ 부피 제약 geometry (1개)
│  ├─ Double-well W(u) curve (1개)
│  ├─ 4개 에너지항 개별 (4개)
│  └─ 전체 에너지 landscape (cross-section, 2개)
├─ Ch7: 위상전이 (4개)
│  ├─ Bifurcation diagram (1개)
│  ├─ Fiedler 고유벡터 (2개: 그리드별)
│  └─ Spectral universality scatter (1개)
└─ Ch8: 수렴성 (2개)
   ├─ Gradient flow trajectory (1개)
   └─ Sharp-interface limit (1개)

P3: 실험 Figure (25-30개)
├─ Ch9: 다중형성 (8개)
│  ├─ K-field architecture schematic (1개)
│  ├─ Regime phase diagram (1개)
│  ├─ Barrier height scaling plot (1개)
│  ├─ Spectral bound comparison (1개)
│  ├─ d_min* with/without closure (2개)
│  └─ 다중형성 예제 시각화 (2개)
├─ Ch10: 시간수송 (6개)
│  ├─ Transport kernel visualization (1개)
│  ├─ Sinkhorn algorithm convergence (1개)
│  ├─ Core-to-core inheritance (1개)
│  ├─ Fingerprint components (1개)
│  ├─ Multi-formation temporal transport (2개)
│  └─ 시간 진화 sequence (5개)
├─ Ch11: 진단벡터 (4개)
│  ├─ 진단벡터 예제 (2개)
│  ├─ Q_morph persistence diagram (1개)
│  └─ 예측 검증 plots (5개)
├─ Ch13: 실험 결과 (10-15개)
│  ├─ Parameter sweep results (3개)
│  ├─ Phase transition curves (3개)
│  ├─ Allen-Cahn comparison (2개)
│  ├─ Transport verification (2개)
│  ├─ Multi-formation dynamics (2개)
│  ├─ Scaling analysis (2개)
│  └─ Prediction validation (3-5개)
└─ 소계: 25-30개

P4: 응용 Figure (15-20개)
├─ Ch14: 응용 사례 (12-15개)
│  ├─ Gestalt mapping diagram (1개)
│  ├─ Framework comparison table (1개)
│  ├─ 음성 신호 분할 예제 (2개: before/after)
│  ├─ 이미지 영역 분할 예제 (3개: original/field/result)
│  ├─ 뇌 영상 분석 예제 (3개: slices)
│  ├─ 신경망 통합 schematic (1개)
│  └─ 응용 도메인 개요 (2개)
├─ Ch15: 정리 레지스트리 (3개)
│  ├─ Theorem dependency DAG (1개)
│  ├─ Category 분포 파이차트 (1개)
│  └─ Critical path highlighting (1개)
└─ 소계: 15-20개

전문/부록 Figure (5-10개)
├─ Preface: 책 구조 다이어그램 (1개)
├─ Notation: 형식 우주 schematic (1개)
├─ Appendix A: Graph Laplacian visualization (2개)
├─ Appendix B: Parameter space (1개)
├─ Appendix C: Design decision tree (1개)
└─ Appendix D: Theorem DAG (1개)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
총 Figure: 80-100개
```

---

## 🛠️ **Figure 생성 자동화 계획**

### Figure 생성 도구 및 스크립트

**생성 스크립트 위치:** `/docs/04-04/textbook_build/figures/generate_*.py`

#### **P1: 기초 개념 Figure (Python + matplotlib)**

```python
# generate_foundations.py — 기초 개념 20-25개 figure

1. 객체 vs 응집도 시각화
   └─ 정사각형 격자, 좌우 비교 + 설명 텍스트

2. Soft field heatmap (5×5, 10×10, 20×20 격자)
   └─ colorbar, u_t 값 범위 [0,1]

3. Bind 예제 (3개)
   ├─ 높은 Bind 필드
   ├─ 낮은 Bind 필드
   └─ ℓ² 노름 계산 시각화

4. Sep 예제 (3개)
   ├─ u_t와 (1-u_t) 비교
   ├─ 가중 평균 계산
   └─ Sep 값 bar chart

5. Inside 예제 (3개)
   ├─ H0 filtration
   ├─ Q_morph 계산
   └─ Articulation measure

6. Persist 예제 (3개)
   ├─ t → t+1 필드 변화
   ├─ 겹침 영역 강조
   └─ 지속성 값 계산

[출력: 20-25개 PNG/PDF]
```

#### **P2: 형식 이론 Figure (matplotlib + TikZ)**

```python
# generate_formal_theory.py — 형식이론 20-25개 figure

1. 폐포 연산자 수렴 (3 frames)
   ├─ u_0 (초기)
   ├─ Cl(u_0) (1회)
   └─ Cl^k(u_0) (수렴)

2. Double-well W(u) curve
   └─ β·Σ u²(1-u)² 시각화

3. 4개 에너지항 (각 2-3pp 설명)
   ├─ E_cl 경계
   ├─ E_sep 분리
   ├─ E_bd 경계 + double-well
   └─ E_tr 수송

4. 에너지 landscape 3D/contour
   └─ u1 vs u2 vs E 값

5. 위상전이 bifurcation diagram
   └─ β/α vs formation amplitude

[출력: 20-25개 PNG/PDF]
```

#### **P3: 실험 Figure (실험 데이터 시각화)**

```python
# generate_experiments.py — 실험 25-30개 figure

1. Parameter sweep 결과
   ├─ λ-sweep curve
   ├─ Phase transition location
   └─ Hessian normalization

2. Phase transition verification
   ├─ 예측 vs 실험 β_c
   ├─ 하이스테리시스 없음 증명
   └─ Topological birth 시각화

3. Allen-Cahn 비교
   ├─ SCC vs Allen-Cahn 에너지 곡선
   ├─ Metastability 비교
   └─ 수렴 속도 비교

4. Transport & Persistence
   ├─ Transport 농축 plots
   ├─ Core-to-core 상속
   └─ 지속성 값 시계열

5. 다중형성 dynamics
   ├─ K=1 vs K=2 에너지
   ├─ Barrier height 스케일링
   └─ Merge dynamics trajectory

6. 대규모 격자 (50×50)
   ├─ Formation 예제
   ├─ Computational cost
   └─ Scaling law

[출력: 25-30개 PNG/PDF]
```

#### **P4: 응용 Figure (수동 + 합성)**

```python
# generate_applications.py — 응용 15-20개 figure

1. Gestalt mapping diagram (TikZ)
   └─ SCC ↔ Gestalt principles

2. Framework comparison (matplotlib table)
   └─ SCC vs IIT vs predictive processing

3. 음성 신호 분할
   ├─ 원본 신호 waveform
   ├─ SCC 형성 필드
   └─ 검출 경계

4. 이미지 분할
   ├─ 원본 이미지
   ├─ SCC 필드
   └─ 분할 결과

5. 뇌 영상 (synthetic data)
   ├─ 원본 MRI-like
   ├─ SCC 필드
   └─ 영역 검출

[출력: 15-20개 PNG/PDF]
```

---

## 📋 **Figure 통합 전략**

### 방법 1: LaTeX 자동 생성

```latex
% chapters/ch02_concepts.tex 예제

\section{Bind — Self-Support}

\subsection{정의}
Bind는...

\subsection{시각화}

\begin{figure}[h]
  \centering
  \begin{subfigure}{0.45\textwidth}
    \includegraphics{figures/bind_example_high.pdf}
    \caption{높은 응집도: Bind ≈ 0.85}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.45\textwidth}
    \includegraphics{figures/bind_example_low.pdf}
    \caption{낮은 응집도: Bind ≈ 0.40}
  \end{subfigure}
  \caption{Bind 진단 벡터 예제 (5×5 격자)}
\end{figure}

\subsection{수학적 정의}
$\text{Bind} = \frac{||u - \text{Cl}(u)||_2}{\sqrt{n \cdot m^2}}$
```

### 방법 2: 문서 대역폭 관리

| 요소 | 비중 | 쪽수 (600pp 기준) |
|------|------|-----------------|
| 줄글 | 50% | 300pp |
| Figure + Caption | 35% | 210pp |
| 공식 + 증명 | 10% | 60pp |
| 표 | 5% | 30pp |

**Figure 통합 밀도:**
- Part I: 80pp에 20-25개 figure → 평균 3-4pp/figure
- Part II: 160pp에 20-25개 figure → 평균 6-8pp/figure
- Part III: 100pp에 25-30개 figure → 평균 3-4pp/figure
- Part IV: 140pp에 15-20개 figure → 평균 7-9pp/figure

---

## 📅 **Figure 생성 일정**

### Phase 1: 초안 집필 병렬 (지금~2일)
- 6명 팀원이 **동시에** 메인 챕터 집필
- Figure 자리는 `\includegraphics{figures/figX_Y_Z.pdf}` placeholder 사용
- **아직 figure 생성하지 않음** (텍스트 먼저)

### Phase 2: Figure 생성 시작 (2-3일, 병렬 시작 가능)
- **초안 완성 후부터 병렬로 진행 가능**
- Python 스크립트 실행으로 자동 생성

**Figure 생성 팀:**
- 새 팀원 1-2명 추가 소환
  - **figure-generator:** Python + matplotlib 전문
  - **design-reviewer:** Figure 품질 검증

### Phase 3: Figure 최종화 (3-4일)
- LaTeX 컴파일과 동시 진행
- 누락된 figure 보충
- 크기/색상/해상도 조정

### Phase 4: 최종 PDF (4-5일)
- 모든 figure 포함
- 600pp+ 완전한 교재

---

## 🎯 **확장된 각 Part 계획**

### Part I: 기초 (80pp, 20-25 figures)

| Chapter | Pages | Figures | 특징 |
|---------|-------|---------|------|
| **Ch1: 동기** | 18 | 4 | 철학적 + 시각화 |
| **Ch2: Proto-cohesion** | 25 | 12 | 4요소 각각 3개씩 |
| **Ch3: 형식 우주** | 20 | 4 | 구조 다이어그램 |
| **Ch+: 추가 기초** | 17 | 3-5 | 깊이 추가 (선택) |

**확장 방향:**
- 각 요소(Bind/Sep/Inside/Persist) 더 많은 예제 (1→3개)
- Soft field visualization 다양한 크기 (5×5→20×20)
- 역사적 맥락 추가 (Gestalt, Allen-Cahn, 최적 수송)

---

### Part II: 형식 이론 (160pp, 20-25 figures)

| Chapter | Pages | Figures | 특징 |
|---------|-------|---------|------|
| **Ch4: 공리** | 28 | 4 | 각 그룹 visualization |
| **Ch5: 연산자** | 25 | 5 | Sigmoid, resolvent, OT |
| **Ch6: 에너지** | 35 | 6 | 4항 개별 + 합성 |
| **Ch7: 위상전이** | 30 | 4 | Bifurcation + spectral |
| **Ch8: 수렴** | 30 | 2-3 | Gradient flow + limit |

**확장 방향:**
- 각 공리에 motivation 설명 추가 (2-3pp)
- 에너지 landscape 3D + contour plots
- 위상전이의 기하학적 직관
- 완전한 증명 (스케치 → 상세)

---

### Part III: 다중형성 (100pp, 25-30 figures)

| Chapter | Pages | Figures | 특징 |
|---------|-------|---------|------|
| **Ch9: 다중형성** | 30 | 8 | K-field, regimes, barriers |
| **Ch10: 시간수송** | 35 | 6 | Transport kernel, fixed-point |
| **Ch11: 진단** | 35 | 10-12 | 예제 + 예측 검증 |

**확장 방향:**
- 2-3개 형성의 시간 진화 sequence (5 timeframes)
- Barrier height 실험적 검증 plots
- 각 진단 요소별 상세 예제

---

### Part IV: 구현/응용 (140pp, 15-20 figures)

| Chapter | Pages | Figures | 특징 |
|---------|-------|---------|------|
| **Ch12: 알고리즘** | 30 | 2 | Pipeline diagram + gradient verification |
| **Ch13: 실험** | 40 | 10-12 | 모든 exp 결과 plots |
| **Ch14: 응용** | 40 | 5 | Gestalt, frameworks, domains |
| **Ch15: 정리** | 30 | 1-2 | DAG + stats |

**확장 방향:**
- Ch13: 17개 실험 모두 결과 plots
- Ch14: 실제 응용 예제 (음성, 이미지, 뇌 영상)
- 신경망 통합 가능성 시각화

---

## 💾 **Figure 파일 관리**

### 디렉토리 구조

```
/docs/04-04/textbook_build/figures/
├─ P1_foundations/
│  ├─ bind_example_high.pdf
│  ├─ bind_example_low.pdf
│  ├─ sep_compare.pdf
│  ├─ inside_filtration.pdf
│  ├─ persist_evolution.pdf
│  └─ ... (20-25개)
├─ P2_formal/
│  ├─ closure_convergence_frame1.pdf
│  ├─ closure_convergence_frame2.pdf
│  ├─ doublewell_curve.pdf
│  ├─ energy_landscape_3d.pdf
│  └─ ... (20-25개)
├─ P3_experiments/
│  ├─ param_sweep_lambda.pdf
│  ├─ phase_transition_curve.pdf
│  ├─ allen_cahn_comparison.pdf
│  ├─ transport_verification.pdf
│  ├─ multiform_evolution_t0.pdf
│  ├─ multiform_evolution_t5.pdf
│  ├─ multiform_evolution_t10.pdf
│  └─ ... (25-30개)
└─ P4_applications/
   ├─ speech_signal_original.pdf
   ├─ speech_signal_scc.pdf
   ├─ image_segmentation_original.pdf
   ├─ image_segmentation_result.pdf
   └─ ... (15-20개)

생성 스크립트:
├─ generate_foundations.py (P1, 20-25개)
├─ generate_formal_theory.py (P2, 20-25개)
├─ generate_experiments.py (P3, 25-30개)
├─ generate_applications.py (P4, 15-20개)
└─ run_all_figures.py (마스터 스크립트)
```

---

## 👥 **확장 팀 구성**

### 기존 팀 (6명)
- template-expert: Part I + Appendices (67pp)
- architect: Ch3 (16pp)
- theory-writer: Part II (160pp → 더 상세)
- multi-writer: Part III (100pp → 더 상세)
- app-writer: Part IV (140pp → 더 상세)
- lead: 조율

### 추가 팀 (2명, Figure 전담)
- **figure-generator** (새 소환)
  - Python + matplotlib 자동화
  - 80-100개 figure 생성
  - 해상도, 색상, 스타일 통일
  
- **design-reviewer** (새 소환)
  - Figure 품질 검증
  - LaTeX 통합 검사
  - 레이아웃 최적화

---

## 📊 **확장 일정**

```
Phase 1: 초안 집필 (1-2일) [현재]
├─ 6명 병렬로 메인 챕터 작성
├─ Pages: 27 → ~300pp
└─ Figures: placeholder 사용

Phase 2: Figure 생성 시작 (2-3일)
├─ figure-generator + design-reviewer 소환
├─ Python 스크립트 병렬 실행
└─ 80-100개 figure 자동 생성

Phase 3: 검수 & 통합 (3-4일)
├─ Figure 품질 검증
├─ LaTeX 컴파일
└─ 레이아웃 최종화

Phase 4: 최종 완성 (4-5일)
└─ 600pp+ 완전한 교재 완성 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
총 예상: 5-6일 (이전 4-5일 → 약간 연장)
```

---

## 🎯 **최종 교재 목표**

### 페이지 분포 (600pp 기준)

```
Part I:   80pp (13%)  ← 기초 개념, 매우 많은 figure
Part II: 160pp (27%)  ← 형식이론, 상세 증명
Part III:100pp (17%)  ← 다중형성, 실험 검증
Part IV: 140pp (23%)  ← 구현/응용, 실제 예제
전문:     80pp (13%)  ← Preface, 부록, 색인, 참고문헌
──────────────────────
총:     600pp (100%)
```

### Figure 분포 (80-100개)

```
Part I:  20-25개 (25%)  ← 높은 figure 밀도 (3-4pp/fig)
Part II: 20-25개 (25%)  ← 중간 밀도 (6-8pp/fig)
Part III:25-30개 (30%)  ← 높은 밀도 (3-4pp/fig)
Part IV: 15-20개 (20%)  ← 중간 밀도 (7-9pp/fig)
전문:     3-5개  (~5%)
──────────────────────
총:     83-105개
```

### 콘텐츠 비중

```
줄글:        300pp (50%)  ← 설명형 텍스트
Figure:      210pp (35%)  ← 시각화 (caption 포함)
공식/증명:    60pp (10%)  ← 수학
표:           30pp  (5%)  ← 데이터
──────────────────────
총:          600pp (100%)
```

---

## ✨ **확장의 이점**

1. **이해도 향상** — 과도한 텍스트 대신 풍부한 시각화
2. **완전성** — 모든 개념에 구체적 예제 + figure
3. **접근성** — 배경이 다른 독자도 이해 가능
4. **참고 가치** — 상세한 부록과 색인
5. **출판 가능성** — 600pp는 학술 교재 표준 범위

---

## 📞 **다음 액션**

1. **초안 집필 계속** (현재 팀, 1-2일)
   - 모든 메인 챕터 완성

2. **Figure 생성 팀 소환** (새 팀원 2명)
   - figure-generator: Python script 작성
   - design-reviewer: Figure 품질 관리

3. **병렬 figure 생성** (2-3일)
   - 80-100개 자동 생성
   - LaTeX 통합

4. **최종 컴파일** (3-4일)
   - 600pp+ 완전한 교재

---

**Status:** 🟢 **확장 계획 수립 완료**

**새로운 목표:** **600쪽+ 시각화 풍부한 교재 (80-100개 figure)**

**추정 완성:** **5-6일** (원래 4-5일 + figure 생성 병렬화로 거의 같은 시간)
