# Phase 15 교재 개발 — 최종 팀 구성 및 배치

**Date:** 2026-04-04 (19:00 KST)  
**Status:** 🟢 **모든 팀원 활성화 — 병렬 집필 전개**

---

## 👥 팀 구성 (6명)

| 역할 | 팀원 | 배정 Task | 담당 | 분량 | 예상 시간 |
|------|------|---------|------|------|---------|
| **Lead** | team-lead | #1-#5 조율 | 전체 조율, 최종 통합 | - | 지속 |
| **Template/Ch1-2** | template-expert | #3 | Part I: Ch1-2 (동기, 개념) | 35-45pp | 1-2일 |
| **Formal Theory** | theory-writer | #4 | Part II: Ch4-8 (공리, 에너지, 증명) | 95pp | 1-2일 |
| **Formal Universe** | architect | #3b | Part I: Ch3 (형식 우주) | 16pp | 1일 |
| **Multi-Temporal** | multi-writer | #4b | Part III: Ch9-11 (K-필드, 시간) | 61pp | 1-2일 |
| **Impl/Apps** | app-writer | #5b | Part IV: Ch12-15 (알고리즘, 응용) | 84pp | 1-2일 |

**총 집필 분량:** 336쪽 (병렬 분담)

---

## 📋 Task 배치도

### Part I: 기초 개념 (47pp 총)

| Task | Chapter | 담당 | 분량 | 내용 |
|------|---------|------|------|------|
| #3 | Ch1-2 | template-expert | 35-45pp | 동기 + Proto-cohesion 개념 |
| #3b | Ch3 | architect | 16pp | 형식 우주 |

**의존성:** None (병렬 진행 가능)  
**완료 예상:** 1-2일

---

### Part II: 형식 이론 (95pp 총)

| Task | Chapters | 담당 | 분량 | 내용 |
|------|----------|------|------|------|
| #4 | Ch4-8 | theory-writer | 95pp | 공리 5그룹 → 에너지 → 위상전이 → 수렴 |

**섹션:**
- Ch4: 공리 (20pp)
- Ch5: 연산자 (17pp)
- Ch6: 에너지 (21pp)
- Ch7: 위상전이 (20pp)
- Ch8: 수렴성 (17pp)

**의존성:** Part I 완료 후 (권장, 하지만 독립적 집필 가능)  
**완료 예상:** 1-2일

---

### Part III: 다중형성 & 시간 이론 (61pp 총)

| Task | Chapters | 담당 | 분량 | 내용 |
|------|----------|------|------|------|
| #4b | Ch9-11 | multi-writer | 61pp | K-필드 → 시간수송 → 진단벡터 |

**섹션:**
- Ch9: 다중형성 (23pp)
- Ch10: 시간수송 (20pp)
- Ch11: 진단벡터 (18pp)

**의존성:** Part II 기초 개념 필요 (하지만 병렬 가능)  
**완료 예상:** 1-2일

---

### Part IV: 구현 & 응용 (84pp 총)

| Task | Chapters | 담당 | 분량 | 내용 |
|------|----------|------|------|------|
| #5b | Ch12-15 | app-writer | 84pp | 알고리즘 → 실험 → 응용 → 정리레지스트리 |

**섹션:**
- Ch12: 알고리즘 (24pp)
- Ch13: 실험 (24pp)
- Ch14: 연결 & 응용 (21pp)
- Ch15: 정리 레지스트리 (15pp)

**의존성:** Part I-III 참고 (하지만 독립적으로 작성 가능)  
**완료 예상:** 1-2일

---

### 전문 & 후문 (49pp 총)

| 항목 | 담당 | 분량 | 내용 |
|------|------|------|------|
| **Foreword** | TBD | 2pp | 외부 인물의 추천사 |
| **Preface** | template-expert (또는 lead) | 4pp | 동기, 청중, 독서방법 |
| **Notation** | architect | 3pp | 기호 표 |
| **Appendices A-D** | TBD | 40pp | 수학 배경, 파라미터, 설계결정, 약어 |
| **Index** | lead | - | 자동 생성 |

**예상:** 마지막 단계 (모든 Chapter 완료 후)

---

## 🚀 **병렬 실행 시간표**

```
Timeline (일 기준):

Day 1-2: 모든 Task 병렬 진행
  ├─ template-expert: Ch1-2 집필 (1-2일)
  ├─ architect: Ch3 집필 (1일, Part I 병렬)
  ├─ theory-writer: Ch4-8 집필 (1-2일)
  ├─ multi-writer: Ch9-11 집필 (1-2일)
  └─ app-writer: Ch12-15 집필 (1-2일)

Day 3: 병렬 작업 검수 시작
  ├─ 각 Chapter 일관성 검증
  ├─ 참고문헌 교정
  └─ 그림 생성 계획 검토

Day 4-5: 그림/표 생성 (P1-P4)
  ├─ P1 (기초): matplotlib 스크립트
  ├─ P2 (형식): TikZ 다이어그램
  ├─ P3 (실험): 데이터 시각화
  └─ P4 (응용): 응용 다이어그램

Day 6: 전체 통합
  ├─ LaTeX 마스터 파일 구성
  ├─ 모든 Chapter 컴파일
  └─ 레이아웃 검증

Day 7: 최종 완성
  ├─ 색인 생성
  ├─ 참고문헌 정렬
  └─ PDF 배포
```

---

## 📊 **병렬성 분석**

### 독립적 경로 (병렬 가능)

**Path A (Part I 기초):**
- template-expert: Ch1-2
- architect: Ch3 (동시 진행)
- 의존성: None → **완전 병렬**

**Path B (Part II 형식):**
- theory-writer: Ch4-8
- 의존성: Part I 개념 활용하지만, 자체 설명 포함 → **준독립**

**Path C (Part III 시간):**
- multi-writer: Ch9-11
- 의존성: Part II 에너지 이해 필요하지만, 자체적 설명 → **준독립**

**Path D (Part IV 구현):**
- app-writer: Ch12-15
- 의존성: Part I-III 참고, 하지만 구현은 독립적 → **준독립**

### 종속성 최소화

모든 집필자가 **자체 완전 설명을 포함**하도록 지시됨:
- Ch4-8에서 Part I 개념 복습
- Ch9-11에서 Part II 에너지 복습
- Ch12-15에서 필요 시 정의 포함

**결과:** 병렬 집필 가능 (1-2일 내 모든 초안 완성 가능)

---

## ✅ 각 팀원 배정 상태

### ✅ template-expert (Task #3 ACTIVE)
- **상태:** Ch1-2 집필 진행 중
- **마감:** 1-2일
- **산출물:** ch01_motivation.tex, ch02_concepts.tex

### ✅ architect (Task #3b 배정됨)
- **상태:** Ch3 집필 시작
- **마감:** 1일
- **산출물:** ch03_formal_universe.tex

### ✅ theory-writer (Task #4 ACTIVE)
- **상태:** Ch4-8 집필 진행 중
- **마감:** 1-2일
- **산출물:** ch04_*.tex, ch05_*.tex, ..., ch08_*.tex

### ✅ multi-writer (Task #4b 배정됨)
- **상태:** Ch9-11 집필 시작
- **마감:** 1-2일
- **산출물:** ch09_*.tex, ch10_*.tex, ch11_*.tex

### ✅ app-writer (Task #5b 배정됨)
- **상태:** Ch12-15 집필 시작
- **마감:** 1-2일
- **산출물:** ch12_*.tex, ch13_*.tex, ch14_*.tex, ch15_*.tex

### 🟡 team-lead (Task #1-5 조율)
- **상태:** 팀 조율, 진행상황 모니터링
- **마감:** 지속
- **산출물:** 마스터 파일, 최종 PDF

---

## 📈 **진행 메트릭 (목표)**

| 메트릭 | 목표 | 현황 | ETA |
|--------|------|------|-----|
| **Part I 완성** | 51pp | 0-10% | 2일 |
| **Part II 완성** | 95pp | 0% | 2일 |
| **Part III 완성** | 61pp | 0% | 2일 |
| **Part IV 완성** | 84pp | 0% | 2일 |
| **전문/후문** | 49pp | 20% (계획) | 3일 |
| **그림/표 생성** | 60개 | 100% (계획) | 3-4일 |
| **최종 PDF** | 336pp | 0% | 4-5일 |

---

## 🎯 **검수 체크리스트**

### Phase 1: 초안 완성 (1-2일)
- [ ] Part I 완성 (template-expert, architect)
- [ ] Part II 완성 (theory-writer)
- [ ] Part III 완성 (multi-writer)
- [ ] Part IV 완성 (app-writer)

### Phase 2: 일관성 검증 (2-3일)
- [ ] 각 Chapter 내부 일관성
- [ ] Chapter 간 참고문헌 교정
- [ ] 수식 정확성 검증
- [ ] Canonical Spec v2.1과 대조

### Phase 3: 그림 생성 (2-3일)
- [ ] P1 (기초 개념) 8개 그림
- [ ] P2 (형식 이론) 5개 그림
- [ ] P3 (실험) 4개 그림
- [ ] P4 (응용) 3개 그림

### Phase 4: 통합 (1일)
- [ ] LaTeX 마스터 파일 구성
- [ ] 전체 컴파일 및 오류 검사
- [ ] 레이아웃 최종 검증

### Phase 5: 최종 완성 (1일)
- [ ] 색인 생성
- [ ] 참고문헌 정렬
- [ ] PDF 배포

---

## 🔗 **참고 자료**

모든 팀원에게 제공:
- ✅ `TEXTBOOK_STRUCTURE.md` — 각 Chapter 상세 요구사항
- ✅ `FIGURE_PLAN.md` — 그림 생성 계획
- ✅ `SNmono_optimized.cls` — LaTeX 템플릿
- ✅ `Canonical Spec v2.1.md` — 형식 정의 & 정리
- ✅ `/scc/` — Python 구현 (Ch12-15 참고)
- ✅ `/experiments/` — 실험 데이터 (Ch13 참고)

---

## 💡 **핵심 원칙 (모든 팀원)**

1. **이론 나열 금지:** 각 개념 후 1-2쪽 직관 설명 필수
2. **줄글 비중:** 60% 이상 (증명 25%, 그림 15%)
3. **예제 구체성:** 5×5 격자 또는 1D 예제 항상 포함
4. **Canonical Spec 준수:** 정의와 정리는 v2.1과 정확히 일치
5. **자체 완전성:** 다른 Part 읽지 않고도 이해 가능하도록 설명 포함

---

## 🚀 **현 상황 요약**

✅ **준비 완료:**
- 코드 검증 (175/175 테스트)
- 템플릿 최적화 (여백 조정)
- 구조 설계 (336쪽, 15장)
- 팀 구성 (5명 활성화)

🟡 **진행 중:**
- 5명의 팀원이 **동시에 5개 Task 진행 중**
- Part I-IV 전체 병렬 집필

⏳ **다음:**
- 1-2일 내 모든 초안 완성
- 2-3일 검수 및 그림 생성
- 4-5일 최종 통합

---

**Status:** 🟢 **최적 병렬성 확보 — 모든 팀원 활성화**

**ETA 완성:** 4-5일 (가속 가능)

**Next Check-in:** 24시간 또는 초안 완성 시점
