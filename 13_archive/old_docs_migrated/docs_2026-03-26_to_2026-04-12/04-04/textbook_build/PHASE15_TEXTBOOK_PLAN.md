# Phase 15: SCC 교재 개발 계획

**Date:** 2026-04-04  
**Team:** scc-textbook (template-expert, architect, writers, auditor)  
**Status:** 🚀 **시작 단계**

---

## 📋 현황

### 이론 완성도
- ✅ **48/48 이론 정리됨 (Category A)**
- ✅ **Canonical Spec v2.1 확정**
- ✅ **Python 구현 174 tests passing**
- ✅ **실험 검증 완료 (exp1-exp57)**

### 다음 단계: 교재 개발
**목표:** 수학자, 이론 인지과학자, ML 연구자를 위한 **체계적이고 설명이 잘 된** 교재

---

## 📐 기술 사양

### 형식
- **템플릿:** Springer Nature SNmono.cls
- **용지:** A4 (210×297mm)
- **여백 조정:**
  - 좌우: 2.0 cm (기본 2.5cm에서 축소)
  - 상하: 2.0-2.3 cm
  - **목표:** 텍스트 폭 확대, 표와 그림이 깔끔하게 배치

### 콘텐츠 스타일
- **이론 나열 금지** — 각 개념마다 "왜?"와 "어떻게?"를 설명
- **줄글 비중:** 60% 이상
- **증명과 정리:** 25%
- **예제/그림/표:** 15%

---

## 🎯 교재 구조 (설계 중)

### Part I: 기초 개념 (Ch 1-3, ~80 페이지)
- **Ch1: 동기와 문제 제기**
  - 왜 전통적 객체 중심 접근은 불충분한가?
  - 인지 문제의 예
  - SCC의 핵심 아이디어

- **Ch2: 응집도의 개념**
  - Soft cohesion field u_t
  - Proto-cohesion diagnostic vector (Bind, Sep, Inside, Persist)
  - 직관적 예제

- **Ch3: 핵심 연산자**
  - Closure, Distinction, 그 외

### Part II: 형식 이론 (Ch 4-7, ~120 페이지)
- **Ch4: 형식 우주와 공리**
- **Ch5: 에너지와 최적화**
- **Ch6: 주요 정리**
- **Ch7: 위상 전이**

### Part III: 구현 (Ch 8-9, ~60 페이지)
- **Ch8: Python 패키지 (scc/)**
- **Ch9: 알고리즘과 실험**

### Part IV: 응용 (Ch 10-11, ~60 페이지)
- **Ch10: 예제와 케이스 스터디**
- **Ch11: 확장과 미래 방향**

### 본문 (Front/Back Matter)
- Foreword
- Preface (호읍→읽는 방법)
- Acknowledgements
- Glossary
- Index

**예상 총 페이지:** 320-400 페이지

---

## 👥 팀 역할 분담

| 역할 | 담당자 | 작업 |
|------|--------|------|
| **Template Expert** | template-expert | Task #1: SNmono.cls 여백 조정 |
| **Architect** | architect | Task #2: 구조 설계 및 목차 작성 |
| **Writer (Part I-II)** | (대기 중) | Task #3: Ch1-2 작성 |
| **Writer (Part III-IV)** | (대기 중) | Task #4: Ch3-4 + 나머지 |
| **Auditor/Lead** | (lead) | Task #5: 최종 검수 및 통합 |

---

## 📅 작업 순서

### Phase 1: 준비 (지금)
1. **에러 검증** — pytest 실행 (진행 중)
2. **템플릿 준비** — SNmono.cls 여백 조정 (template-expert)
3. **구조 설계** — 목차 및 페이지 버짓 (architect)

### Phase 2: 집필
4. **Part I (Ch1-2)** 작성 — 25-30 페이지
5. **Part II (Ch3-4)** 작성 — 40-50 페이지
6. **Part III (Ch5-6)** 작성 — 30-40 페이지
7. **Part IV (Ch7-8)** 작성 — 30-40 페이지
8. **전문 (Front Matter)** 작성

### Phase 3: 검수 및 완성
9. **통합 및 컴파일** — PDF 생성
10. **최종 검수** — 일관성, 레이아웃, 색인
11. **완성 및 배포**

---

## ✅ 체크리스트

### Task #1: 템플릿 여백 조정
- [ ] SNmono.cls 분석
- [ ] 여백 파라미터 수정
- [ ] 테스트 컴파일
- [ ] 최적화된 파일 저장

### Task #2: 구조 설계
- [ ] Part별 목표 정의
- [ ] Chapter 세부 구성 (각 4-8개 섹션)
- [ ] 페이지 예산 분배
- [ ] 상세 TOC 작성
- [ ] 그림/표 리스트 작성

### Task #3-4: 집필
- [ ] 각 Chapter 초안 작성
- [ ] 수식 및 예제 포함
- [ ] 그림/표 자리 표시
- [ ] LaTeX 마크업 확인

### Task #5: 최종 검수
- [ ] 전체 일관성 검증
- [ ] 참고문헌 및 색인
- [ ] PDF 컴파일 및 레이아웃
- [ ] 최종 보고

---

## 📂 디렉토리 구조

```
/Users/ojaehong/ex_2/docs/04-04/textbook_build/
  PHASE15_TEXTBOOK_PLAN.md          ← 이 문서
  TEXTBOOK_STRUCTURE.md             ← 상세 구조 (Task #2)
  
  templates/
    SNmono_optimized.cls            ← 여백 조정 버전 (Task #1)
  
  chapters/
    ch01_motivation.tex
    ch02_concepts.tex
    ch03_formal_universe.tex
    ...
  
  figures/
    (그림 파일들)
  
  source/
    main.tex                        ← 마스터 파일
    preface.tex
    foreword.tex
    ...
```

---

## 🔗 참고

- **Canonical Spec v2.1:** Authoritative formal reference
- **Agent Instructions.md:** Theory development protocol
- **Existing papers:** `/Users/ojaehong/ex_2/papers/` 참고 가능

---

## 🚀 다음 스텝

**대기 중:**
1. pytest 결과 확인 (진행 중)
2. template-expert가 여백 조정 완료 대기
3. architect가 구조 설계 완료 대기

**그 다음:**
4. 구조 승인 후 집필 팀원 추가 소환
5. 병렬로 여러 Chapter 작성
6. 중간 검수 및 피드백
7. 최종 통합

---

**Status:** 🟡 **진행 중 — 팀메이트 작업 대기**
