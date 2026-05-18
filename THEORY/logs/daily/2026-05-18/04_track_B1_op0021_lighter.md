---
type: log/daily/track-report
date: 2026-05-18
track: B1 — LIGHTER (OP-0021 Mori-Zwanzig + pf_tstar_langevin 5-gap)
session_label: W8-Day1 Track B1
canonical_version: CV-1.17 (untouched)
status: COMPLETE — broad_survey_B1.md (P1 baseline) 산출 — W9 staging only
---

> [!nav] Linked: [[00_plan]] · [[broad_survey_B1|working/MF/broad_survey_B1.md]] · [[pf_tstar_langevin]]


# 04 — Track B1 LIGHTER Report (W8-Day1, OP-0021)

**Pre-work xref check** (00_plan.md §Track B 의무):

```bash
grep -r "Mori-Zwanzig|OP-0021|T_\*" THEORY/canonical/ THEORY/working/
```

결과: 20+ working file hit, 핵심 ancestor `pf_tstar_langevin.md`, `pf_a1_lions_sznitman_freidlin_route.md`, `CV114_H_MORSE_PACKAGEII/07_Eyring_Kramers_requirements.md`, `CV114_H_MORSE_PACKAGEII/08_candidate_lemma_chain.md`, `n1_kramers_extension.md`. 본 broad_survey_B1 의 novel positioning = *Mori-Zwanzig Route A literature pointer* + *pf_tstar_langevin §11 의 light gap 5개 정식 표 등록*.

---

## §1. 산출물

| Path | Lines | 목적 |
|---|---|---|
| `THEORY/working/MF/broad_survey_B1.md` | ~140 | Mori-Zwanzig Route A literature + 5 light gap (W9 sketch 의 직접 입력) |

---

## §2. 5 light gap 요약 (broad_survey_B1.md §4)

| Gap | Description | Effort |
|---|---|---|
| Gap-1 | NOP-F Lemma 20 의 RG-Fisher coupling 명시 (Cardy §5.4) | 2 sessions |
| Gap-2 | NOP-J Lemma 24 의 finite-graph Fisher (Amari Ch.2) | 1 session |
| Gap-3 | candidate 2c (1/β_commit) 의 zero-noise compatibility (Freidlin-Wentzell 3rd ed.) | 0.5 session |
| Gap-4 | F_M reflection 의 $T_*$ correction factor (Lions-Sznitman 1984) | 1 session |
| Gap-5 | Eyring-Kramers prefactor 의 $T_*$ dependency 분해 (Bovier-Eckhoff-Gayrard-Klein 2004) | 2 sessions |

총 effort: **~6.5 sessions** (W9 ~1.5 주). Gap-3 + Gap-4 가 가장 가벼움 (W9 Day 1-2 진입).

---

## §3. Mori-Zwanzig Route A (W9 진입 입력)

- Slow variable 후보: $K_\mathrm{act}$ vs σ-tuple vs cross-formation overlap (broad_survey_B1.md §3.2).
- Memory kernel exponential decay → Markovian Langevin reduction (success condition §3.4 (iii)) — H-MORSE row Cat A 가 입력 가능 (Day 4 SEAL prep 이후).
- 4 외부 reference: Zwanzig 2001 Ch.8, Givon-Kupferman-Stuart 2004, Chorin-Hald-Kupferman 2002, Lin-Lu 2017.
- 실패 모드: slow/fast 분리 부재, memory long-tail, reflection boundary 위배 (§3.5).

---

## §4. Day 1 핵심 metric 와의 관계

00_plan.md §"Decision gate" 의 핵심 metric = OP-0008 attack 입력 (Track B2). 본 Track B1 는 *Day 1 metric 직접 기여 없음* — *W9 staging input 만*. W8 plan §11 Path 1/2/3 *공통* 항목 (W9+ Mori-Zwanzig) 의 *입력 자료*.

---

## §5. Hard constraint 자가 점검

- [x] canonical 직접 수정 0
- [x] silent OP resolution 0 — OP-0021 OPEN 유지, 5 gap 모두 *Cat C ready* 만
- [x] Research OS 재도입 0
- [x] reductive 환원 0 — Mori-Zwanzig / Fisher metric / Freidlin-Wentzell 모두 contrastive
- [x] primitive 전도 0
- [x] dual-naming inconsistency 존중 — OP-0021 의 두 명명 ($T_*$ vs Stochastic Dynamics) 의 *기존 carry-forward* 그대로 인용; *해소 시도 부재*

---

## §6. 자가 평가

- broad_survey_B1.md = **140+ 줄**, 9 sections + 5 light gap + Mori-Zwanzig 외부 reference + unlock chain.
- 본 lighter survey 가 W9 의 `op0021_mori_zwanzig_sketch.md` + `op0021_tstar_emergence.md` 두 file 의 *직접 입력*.
- prompt body §5 의 quality 기준 (multi-approach ≥ 3) 은 Route A (Mori-Zwanzig) 단독; *Route B (RG)* + *Route C (Information geometry)* 후속 가능성을 §4 Gap-1, Gap-2 에 표시.

---

*Track B1 종료. lighter survey complete. W9 staging input 준비 완료. canonical 0 edits.*
