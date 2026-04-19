# THEORY/working/ — 진행 중인 이론 정리 (Active Theory Organization)

**주제별 작업장.** 진행 중인 이론 전개, 미완 증명, 검토 중인 가설, 재구성 중인 개념 전부 여기.

## 조직 원칙

### 파일 1개 = 주제 1개

- 파일명은 해당 주제를 간결히 표현 (`F-1_kinetic.md`, `multi_formation_stability.md`, `transport_confinement.md` 등)
- 한 주제에 대한 모든 현재 사고를 하나의 파일에서 통합 추적 — 이 파일이 "이 주제에서 우리가 지금 어디까지 왔는가"의 단일 soft truth
- 다른 주제로 이어지면 새 파일; 합쳐지면 하나로 병합

### 형식은 자유

Research OS의 프론트매터·등록부 접두사는 **사용하지 않는다**. 필요시 다음 정도만:

```markdown
# <주제명>

**Status:** exploring | developing | near-promotion
**Last touched:** YYYY-MM-DD
**Canonical refs:** canonical.md §X.Y (관련 부분)
**Open questions (working):** ...

---

<본문 — 완전 자유>

## Next

- <다음에 뭘 할지>
```

## Promotion (승급) 흐름

```
logs/daily/YYYY-MM-DD.md  (날것 기록)
         ↓ 주제별로 재구성 — 이 폴더로 끌어올림
working/<topic>.md         (당신이 지금 위치)
         ↓ 증명 완료 + 검토 + 실험/테스트 통과
canonical/canonical.md     (승급 완료 — 되돌아오지 않음)
```

### working → canonical 승급 체크리스트

`canonical/`로 올리기 전에:
1. 증명이 자체 완결적인가 (가정·논리·결론 전부 명시)?
2. 기존 canonical과 모순 없는가 (grep으로 관련 섹션 교차 확인)?
3. 실험/테스트가 있다면 통과하는가?
4. 조건부 결과라면 조건이 명시되었는가?
5. `canonical/theorem_status.md`에 들어갈 행 초안이 준비되었는가?

다 yes면 승급. 승급 후 이 `working/<topic>.md`는:
- 완전히 canonical로 흡수되었으면 `_archive/working_promoted/`로 이동 (이력 보존)
- 일부만 승급되고 남은 부분이 활성이면 남겨두기 + 상단에 "부분 승급" 표기

## 뭘 쓰지 않는가

- **등록부 접두사 없음** — `Q-xxxx.md`, `P-xxxx.md` 같은 네이밍 금지
- **프론트매터 필수 아님** — `id:`, `type:`, `status:` 메타데이터 강제하지 않음
- **날짜 기반 하위 디렉토리 없음** — 주제 기반만

이것들이 2026-04-12 Research OS의 실패 요인. 재도입 금지.
