---
type: log/daily/track-report
date: 2026-05-18
track: C — Sanity Infra
session_label: W8-Day1 Track C
canonical_version: CV-1.17 (untouched)
status: PASS
---

> [!nav] Linked: [[00_plan]] · [[00_index]] · [[01_pre_brainstorm]]


# 06 — Track C Report (W8-Day1, Sanity Infra)

**Pre-work xref check** (00_plan.md §Track C 의무):

```bash
grep -r "canonical_k2_hash|subthreshold_demo_check|sanity_canonical_xref" CODE/ THEORY/
```

결과: 3 hits, 모두 **W8 plan / 00_plan / 00_index** 내부. 본 어휘는 신규. 기존 `scc/` 또는 `tests/` 와 충돌 없음.

---

## §1. 산출물

| Path | Lines | 목적 |
|---|---|---|
| `CODE/experiments/__init__.py` | 0 | experiments/ 를 import 가능한 패키지로 (tests 에서 `from experiments.exp90_... import ...` 위함) |
| `CODE/experiments/exp90_sanity_canonical_xref.py` | ~190 | `canonical_k2_hash()` + `subthreshold_demo_check()` 정의 + 4-step demo |
| `CODE/tests/test_sanity_canonical_xref.py` | ~120 | 10 tests (6 hash + 4 subthreshold) |

`scc/` 모듈은 0 lines 변경 (W8 anti-goal §5 준수).

---

## §2. 두 도구의 *operational substantive* 가치 (W8 plan §10 risk mitigation)

### §2.1 `canonical_k2_hash`

**입력**: `fields: Sequence[np.ndarray]` (K 개 formation), `theta_core: float = 0.5`.

**알고리즘**:
1. 각 formation $u^k$ 에서 `core_k = sorted({i : u^k(i) > theta_core})` 추출
2. `canonical = sorted({core_1, ..., core_K})` — **set-of-sets** sort
3. `SHA256(repr(canonical))` 의 hex digest 반환

**핵심 성질**:
- **Permutation invariance** (test_permutation_invariance): formation 라벨 swap 시 hash 불변 — *V-AFD/R-2 의 K-tuple label reshuffle 형 duplicate* 자동 감지.
- **Structural distinguishability** (test_distinguishes_structural_difference): split 위치 1 site 차이 시 hash 다름 — *trivially identical* 만 동일 처리.
- **Idempotence** (test_idempotence): 동일 입력 → 동일 출력. 64-char hex.
- **K≥2 generality** (test_k_geq_2_permutation_invariance): K=3 도 invariant. K=2 는 audited target 이지만 알고리즘 자체는 K≥2 모두 작동.
- **Threshold dependence** (test_threshold_dependence): 다른 θ_core 는 다른 hash 가능 — Day 2-5 의 θ_core sweep 결과 비교 시 일관성 보장.

**Day 2-5 운영 룰**: 새 K=2 결과 산출 시 hash 기록 → 기존 결과 hash 와 비교 → 일치 시 duplicate flag.

### §2.2 `subthreshold_demo_check`

**입력**: `fields, graph, params, lambda_rep=10.0, Lambda_threshold=0.5, l_ratio_threshold=0.3`.

**산출**: `SubthresholdReport(l_second, l_max, l_ratio, Lambda, is_subthreshold, regime)`.

**핵심 메트릭**:
- $l_{\mathrm{second}} / l_{\mathrm{max}}$ — graph Laplacian 의 Fiedler / max 비. low 면 두 번째 모드가 *spectrally suppressed* 임.
- $\Lambda_{\mathrm{coupling}}$ — `scc.multi.coupling_strength()` 의 unified 결합 강도 (per `UNIFIED-REGIME-PARAMETRIZATION.md §3.1`).

**판정**: `is_subthreshold ⟺ (Λ < Λ_th) AND (l_ratio < l_ratio_th)`.

**의미**: "sub-threshold demo" = K=2 가 *분리되어 있고* 그래프 spectrum 의 두 번째 모드도 *약함*. 이 regime 에서:
- K-tuple-smooth 형 claim (R-2 B2/B3 의 형식) 은 *수치 실패* 패턴 보임 — manual audit 필수.
- *strongly-interacting* 라벨이 자동으로 붙지 않음 → reviewer 가 *결합 강도 위배* 를 즉시 감지.

**Day 2-5 운영 룰**: 새 K=2 결과는 본 함수 호출 → SubthresholdReport 산출 → 일지 / 보고에 *강제 기록*. 누락 시 audit 불가.

---

## §3. 검증 (verification)

### §3.1 신규 test PASS

```
$ python3 -m pytest tests/test_sanity_canonical_xref.py -v
============================== 10 passed in 0.08s ==============================
```

10/10 PASS:
- 6 hash tests
- 4 subthreshold tests

### §3.2 exp90 demo 출력 (4 steps)

```
[1] canonical_k2_hash — permutation invariance
  hash(A)         = 2782406fe4f8dcb0...
  hash(B=swap(A)) = 2782406fe4f8dcb0...
  invariance      : PASS
  distinct(A,C)   : PASS
[2] subthreshold_demo_check — well-separated case
   Lambda = 0.0, is_subthreshold = True, regime = weakly-interacting
[3] subthreshold_demo_check — overlapping case
   Lambda = 80.0, is_subthreshold = False, regime = strongly-interacting
[4] Hash idempotence on real K=2 optimizer output (15×15 grid)
   idempotent : PASS
```

### §3.3 기존 pytest regression (215+1xf preserved)

별도 background run 결과 확인 (Track A/B 진행 중 보고 — 본 파일 §3.3 끝에 보강 예정).

---

## §4. Anti-pattern 회피 자가 점검

| 회피 항목 | 결과 |
|---|---|
| `scc/` 수정 | 0 (W8 anti-goal §5) |
| Engineering proxy 도입 (Gaussian similarity, etc.) | 0 — graph Laplacian + 기존 `coupling_strength()` 만 사용 |
| 새 framework letter | 0 — `canonical_k2_hash` / `subthreshold_demo_check` 는 *기능명*, framework 라벨 아님 |
| V-AFD/R-2/z_t 부활 | 0 — 본 도구는 그 패턴의 *감지* 목적 |
| Silent OP resolution | 0 — 어느 OP 도 closed 주장 안 함 |

---

## §5. Day 2-5 입력 형태

- Day 2 exp91 (K-soft hard-K recovery) 가 K=2 결과 산출 시 → 본 두 함수 호출 강제 (W8 plan §6 Daily Discipline #2).
- Day 3 exp92 (Wigner projection robustness) 의 8×8/12×12 toy 도 동일.
- 의심스러운 새 결과 (R-2-style "smooth K-tuple") 발견 시 → `subthreshold_demo_check.is_subthreshold = True` 면 *수동 audit* 트리거.

---

## §6. Notes for future sessions

- 본 두 함수는 *operational tool*, *수학적 결과* 아님. Cat 분류 부착 불요.
- `θ_core = 0.5` 의 *원리적 근거 없음* (prompt body §12 #2 carry-forward) — Day 2-5 에서 θ_core 가변 시 hash 가 *config-specific* 임을 인지하고 비교.
- `Λ_threshold = 0.5`, `l_ratio_threshold = 0.3` 도 동일 — *configuration-specific* default. Day 2-5 에서 실측 분포에 따라 조정 가능.

---

*Track C 종료. PASS. canonical 0 edits. scc/ 0 edits. 10 신규 tests + 1 신규 experiment.*
