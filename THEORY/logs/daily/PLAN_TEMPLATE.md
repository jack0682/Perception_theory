# Plan Template — 매일 저녁 작성

> **사용법:** 전날 저녁 다음날 날짜의 디렉토리(`THEORY/logs/daily/YYYY-MM-DD/`)를 미리 생성하고, 이 템플릿을 `plan.md`로 복사한 뒤 각 섹션을 채워 넣는다. 빈 섹션은 "없음" 또는 "N/A"로 명시.

---

# Plan — YYYY-MM-DD

## Target

<오늘 풀어갈 단일 open problem 또는 focused subtopic. 한 문장 또는 짧은 문단. 예:
"N-1 (Soft-Hard Switching Asymmetry) 의 K 층위에서, K를 H_0 persistence bar length 가중합으로 soft화하는 접근이 E(u*_M) vs E(u*_{M/K}) 비교를 어떻게 바꾸는지 검토."
>

## Why now

<오늘 이 문제를 선택한 이유. 1~3문장. 어제 세션의 carry-forward인지, 리프레이밍에서 새로 드러난 것인지, 외부 자극인지.>

## Context refs (에이전트가 반드시 읽어야 할 소재)

- `THEORY/canonical/canonical.md` §X.Y — <관련 섹션>
- `THEORY/canonical/theorem_status.md` — <해당 OP-ID 또는 P-ID>
- `THEORY/working/<file>.md` — <있다면>
- 어제 로그: `THEORY/logs/daily/YYYY-MM-DD/<files>.md` — <해당 항목>
- 외부 자료: <필요시. PDF, 논문, 다른 프로젝트>

## Current hypotheses / approaches under consideration

<자유 서술. 오늘 아침 시점의 직관, 의심, 대안. 에이전트가 이 안에서만 움직이는 것은 아님 — 출발점.>

- 가설 1: ...
- 가설 2: ...
- 반례 의심: ...

## Session goals

<오늘 산출물로 기대하는 것. 구체적이고 검증 가능한 형태. 너무 많으면 실패 — 1~3개 권장.>

1. ...
2. ...
3. ...

## Non-goals (scope 제한)

<오늘 다루지 않을 것. 관련은 있으나 오늘은 밀어둘 것. 명시하지 않으면 scope creep 발생.>

- ...
- ...

## Carry-forward (어제로부터)

<전 세션에서 넘어온 open item. 없으면 "없음".>

- ...

## Success criterion for today

<단일 문장. "오늘 세션이 성공이라면 무엇을 얻고 있어야 하는가". 이 기준에 의해 저녁 재검토시 판단.>

---

## 메모

- 이 파일은 저녁에 작성되고 다음날 아침 에이전트에게 주어지는 **입력 문서**. 에이전트의 출력은 같은 디렉토리의 `01_*.md`, `02_*.md` ... 에 쌓인다.
- 에이전트가 받는 MAIN_PROMPT가 이 파일을 자동으로 읽도록 구성되어 있음 (`THEORY/logs/daily/MAIN_PROMPT.md` 참고).
- 저녁 작성은 자동화하지 않음 — 사용자 직접 판단.
