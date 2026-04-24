# 10_C2_phase3_user_scripts.md — Phase 3 Heavy Numerical: User Execution Protocol

**Session:** 2026-04-24 (evening)
**Plan reference:** `07_C2_attack_plan.md` Phase 3.
**Scripts (already written):**
- `CODE/scripts/phase3_C2_L_sweep.py` — F_min(L) for L ∈ {8, 12, 16, 20, 24, 32}
- `CODE/scripts/phase3_C2_lambda_phase_diagram.py` — F_min(λ_cl, λ_sep) at L=16

---

## §1. 사용자 실행 명령

### 명령 1 — L sweep (Phase 3.1)

```bash
cd /home/jack/Perception_theory/CODE && python3 scripts/phase3_C2_L_sweep.py 2>&1 | tee scripts/results/phase3_L_sweep_log.txt
```

**예상 runtime**: 30-60분 (L=8..32, 10 restarts each, CPU). L=32 가 가장 비쌈.

**Output**:
- `scripts/results/phase3_C2_L_sweep.json` — incremental save 됨 (L 끝날 때마다)
- 콘솔 + log file: progress

**Expected behavior**:
- 각 L 에서 pure E_bd minimizer 가 F=1 일 것
- Full SCC F_full_min 이 L 의 함수로 변화 (Phase 2 L=12 에서 F=9 관측됨)
- L=32 에서 F_full_min 이 R23 의 5 와 가까운지 확인

### 명령 2 — λ phase diagram (Phase 3.2)

```bash
cd /home/jack/Perception_theory/CODE && python3 scripts/phase3_C2_lambda_phase_diagram.py 2>&1 | tee scripts/results/phase3_phase_diagram_log.txt
```

**예상 runtime**: 30-45분 (16 grid points × 8 restarts × ~30s each, L=16).

**Output**:
- `scripts/results/phase3_C2_phase_diagram.json`
- 콘솔: F_min table 4×4 lambda grid

**Expected behavior**:
- $(0, 0)$ (pure E_bd): F=1
- $(λ, 0)$ (pure cl): F 가 λ 와 함께 증가 — closure-only 효과 (NQ-134 part 1)
- $(0, λ)$ (pure sep): F 가 λ 와 함께 변화 — sep-only 효과 (NQ-134 part 2)
- $(1, 1)$: F=많음 (full SCC)

---

## §2. 실행 후 결과 returnschema

사용자가 실행 후 다음 한 줄로 결과 전달:

```bash
cat scripts/results/phase3_C2_L_sweep.json scripts/results/phase3_C2_phase_diagram.json
```

또는:

```bash
ls -la scripts/results/phase3_C2*
```

본 모델이 JSON 받으면:
- F_min(L) 분석 → R23 F_*=5 prediction 확정/반증
- F_min(λ_cl, λ_sep) 분석 → NQ-134 (cl/sep separation) closed
- Phase 4 integration 으로 진행

---

## §3. 사용자 실행 대기 중 본 모델의 작업

§5 / §6 주의: prompt 의 "결과 대기중일때는 쉬는것이 아닌 이후 계획을 계속 실행" 준수.

대기 중 작업 (Phase 4 partial):
1. **Theorem 2 final draft 작성** (Phase 1 + Phase 2 결과만으로 가능한 부분)
2. **F-1, M-1, MO-1 의 σ-language 최종 statement 작성**
3. **`06_open_problems_digest.md` C2 cluster 갱신** (Phase 2 후 status)
4. **추가 lemma 도출 시도** — Phase 1 의 g_cl/g_sep scaling 으로부터 derivable 한 corollary

다음 파일: `11_C2_phase4_partial_integration.md` — Phase 4 partial (Phase 3 결과 도착 전 가능한 통합).

---

## §4. Fallback (사용자 실행 실패 시)

만약 사용자 환경에서 script 실행 실패:
- **Fallback A**: L=12, n_restarts=4 으로 축소 (3-5분 runtime). 이미 Phase 2b 에서 L=12 실행 완료, 추가 데이터.
- **Fallback B**: 사용자가 결과 없이 본 모델이 Phase 4 partial 만으로 종료. Theorem 2 의 (i)+(ii) Cat A 는 이미 Phase 2 만으로 확보.

---

## §5. Critical reminder

사용자가 결과 전달 시 본 모델은:
1. JSON 파싱 → F_min(L) 와 F_min(λ_cl, λ_sep) 표 추출
2. Phase 1 prediction 과 비교 → 일치 / 불일치 진단
3. **F_*(L) scaling 의 Cat 분류** → A 또는 B
4. NQ-133 (F-jump explanation) 의 numerical-supported answer 정형화
5. Phase 4 final integration → `12_C2_final.md` 작성

**End of 10_C2_phase3_user_scripts.md.**

---

## §6. 사용자에게의 메시지 (요약)

다음 두 명령을 실행해 주세요:

```bash
cd /home/jack/Perception_theory/CODE && python3 scripts/phase3_C2_L_sweep.py 2>&1 | tee scripts/results/phase3_L_sweep_log.txt
cd /home/jack/Perception_theory/CODE && python3 scripts/phase3_C2_lambda_phase_diagram.py 2>&1 | tee scripts/results/phase3_phase_diagram_log.txt
```

실행 종료 후 다음 한 줄로 결과 전달:

```bash
ls scripts/results/phase3_C2*
```

또는 JSON 내용 직접 paste 도 좋습니다. **그 동안 본 모델은 Phase 4 partial integration (`11_*.md`) 을 계속 진행합니다.**
