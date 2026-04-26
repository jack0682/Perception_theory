# plan.md — 2026-04-26 Session Plan (W4 Extended Close — Day 8)

**Session type:** W4 extended close (V5b verification cycle). Per user direction (2026-04-26 mid-session): "아직 내용은 전부 W4로 간주해" — 04-26 work treated as W4 final-day continuation, NOT W5 Day 1.
**W4 scope (extended):** 2026-04-19 ~ **2026-04-26** (8 days). V5b verification cycle pushed W4 close from initial 04-25 to 04-26 EOD.
**Prerequisite:** W4 initial close (2026-04-25) + canonical v1.3 merge committed by user. Theorem 2 family + σ-framework Commitment 14 + F-1/M-1/MO-1 resolution.
**Session working directory:** `THEORY/logs/daily/2026-04-26/`.
**Weekly buffer target:** `logs/weekly/2026-04-W4/weekly_draft_storming.md` (extended) — NOT W5.

---

## §1. 세션 목표 (Target)

**"Theorem 1 V5b의 sub-lattice (ζ < 0.3) ↔ super-lattice (ζ > 0.5) crossover 경계를 ζ-scan으로 정량화. ζ_* ≈ 0.3-0.4 추정의 수치 확정 또는 falsification."**

W4 04-24 V5b는 6 iteration (V1→V5b) + 2 in-session retraction (V4 premature, V5a partial wrong)을 거쳤지만 sub/super 영역의 **boundary는 미정량**. 04-25 NQ-128 (sub-lattice ζ=0.183) + NQ-168 (super-lattice ζ=1.0)는 양 끝 점만 확인했음. **W5 Day 1은 V5b의 가장 큰 잔존 ambiguity인 crossover boundary를 결정**.

---

## §2. Deliverables (P0/P1)

### G0 — NQ-170 ζ-scan Numerical (P0 MUST)

**목표**: ζ ∈ {0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0} × L=20 torus disk × N=3 seeds 실험. Mode 1의 translation overlap (δu_x, δu_y)를 측정하여 ζ vs Goldstone overlap 함수 형태 확정.

**예상 결과 (V5b prediction)**:
- ζ ≤ 0.2: max(overlap_x, overlap_y) < 0.5 (orbital, no Goldstone)
- ζ ≥ 0.5: max(overlap_x, overlap_y) > 0.9 (Goldstone present)
- ζ ∈ [0.3, 0.4]: smooth transition

**스크립트**: `CODE/scripts/nq170_zeta_scan.py` (신규).

**Outputs**:
- `02_NQ170_zeta_scan.md` — 결과 분석 + V5b crossover boundary update
- `CODE/scripts/results/nq170_zeta_scan.json` — 원자료

**Success criterion**:
1. ζ vs Goldstone overlap 함수가 monotone (smooth crossover 증거)
2. crossover boundary ζ_* 정의 (예: max overlap = 0.5 위치)에 대한 정량값 (R² > 0.7)
3. 또는 falsification: 크로스오버가 sharp transition / non-monotone / region-dependent 등 V5b smooth crossover 가설 부정

---

### G1 — Theorem 1 V5b 상태 update (P1)

**목표**: NQ-170 결과에 따라 Theorem 1 V5b의 Cat 등급을 재평가:
- Sub-lattice branch (Cat A): NQ-128로 이미 확인 (04-25)
- Super-lattice branch (Cat A existence + commensurability split): NQ-168로 확인 (04-25)
- Crossover branch (Cat B → Cat A 가능?): NQ-170 결과에 따라

**Outputs**: `03_V5b_status_update.md` — Theorem 1 V5b 6 iteration 후 정직한 상태 평가 + W6+ canonical 승급 가능성 검토.

---

## §3. 우선순위 표

| 우선순위 | 작업 | Skip 시 결과 |
|---------|------|------------|
| **P0 (MUST)** | G0 NQ-170 ζ-scan numerical | V5b crossover 미해결, T2 → T1 격상 불가 |
| **P1** | G1 V5b 상태 update | T2 stage 정체 |

---

## §4. Non-goals (명시적 제외)

- **V5b canonical 직접 승급** — ζ-scan 결과만으로는 부족 (graph-class extension + nodal count도 필요).
- **NQ-168b position-dependent mechanism** — 별도 세션 (W5 Day 2+).
- **NQ-148 (σ-jump formalization)** — C1' cluster, 별도 theory session.
- **Multi-formation σ (Phase 5)** — single-formation σ user decision (Lemma 1/2/3 § 13 추가) 후.
- **W4 commit 대기 작업 추가** — user 직접 commit 예정.

---

## §5. 작업 흐름

**Morning (09:00-11:00, 2h)**:
- 09:00-09:30: NQ-170 스크립트 작성 (`nq170_zeta_scan.py`).
- 09:30-10:30: 실행 (7 ζ × 3 seeds = 21 minimizers, 예상 ~30분-1h).
- 10:30-11:00: 결과 1차 분석.

**Afternoon (13:00-16:00, 3h)**:
- 13:00-15:00: `02_NQ170_zeta_scan.md` 작성 — 결과 분석 + crossover boundary 정량 + V5b 검증.
- 15:00-16:00: `03_V5b_status_update.md` 작성 — V5b 6 iteration 후 정직한 상태 평가.

**Evening (17:00-19:00, 2h)**:
- `99_summary.md` 작성.
- W5 weekly_draft_storming.md에 04-26 entry append.
- W5 Day 2 plan.md 준비.

---

## §6. 성공 기준

**P0 (반드시 달성)**:
- [ ] `02_NQ170_zeta_scan.md` 완성 + `nq170_zeta_scan.json` results
- [ ] crossover boundary ζ_* 정량값 도출 또는 V5b crossover 가설 falsification
- [ ] V5b sub/super-lattice prediction 21 minimizer 전체에 대한 confirmation rate

**P1**:
- [ ] V5b 상태 update report (T2 유지 / T1 승급 path / falsification 중 결정)

**Hard constraints (무조건)**:
- [ ] Canonical.md 직접 수정 없음 (W4 merge가 user commit 대기 중이므로 추가 변경 보류)
- [ ] Silent resolution 없음
- [ ] V5b canonical 승급 선언 없음 (graph-class extension 후 W6+ 결정)

---

## §7. 종료 기준

**정상 종료**: G0 완료 + G1 V5b 상태 update + 99_summary

**Minimal 종료**: G0 (NQ-170 numerical)만 완료

**Blocker 종료**: V5b crossover 가설 ζ-scan에서 명시적 falsification → 99_summary에 정직 기록 + W5 Day 2 priority 재평가

---

## §8. Stage 가이드라인

**Silent resolution 금지**:
- ζ-scan 결과가 sub/super lattice 양쪽 prediction과 모두 양립 시 — 두 경우의 implication 모두 분석.
- crossover ζ_* 값이 V5b 추정 (0.3-0.4)을 벗어나면 — falsification 명시.

**Promotion pipeline 준수**:
- NQ-170 결과는 working buffer (logs/daily/, weekly_draft) 까지만. canonical 승급 W6+ user 결정.
- V5b 6 iteration 후의 honest assessment가 본 세션의 가치.

---

**End of plan.md for 2026-04-26 (W5 Day 1).**
**Target: V5b crossover quantification — 6 iteration의 잔존 ambiguity 해소.**
