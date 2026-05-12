---
id: CC-StableK-04
type: working/theory
status: open — 실험 계획 (미구현)
created: 2026-05-12
session: W7 carry-forward
scope: OP-0012-CC-StableK 수치 검증 실험 계획
target_file: CODE/experiments/exp_cc_stablek_composition.py
dependencies: CODE/scc/transport.py (sinkhorn_partial_ot), CODE/scc/multi.py, CODE/scc/diagnostics.py
---

# 04. 실험 계획 — K=2 Stable Temporal Sequence Composition Test

---

## 실험 목적

T-CC-StableK의 핵심 주장을 수치적으로 검증:

> Δ > 2ε_comp이면 R_{t→r}^direct = R_{s→r} ∘ R_{t→s}

세 시점 (t, s, r)에서 K=2 stable configuration을 생성하고,  
두 대응 방법 (직접 vs 합성)의 일치 여부를 비교한다.

---

## 실험 설계

### 기본 설정 (exp83 계승)

```python
GRID_SIZE = 15           # 15×15 grid (225 nodes), exp83 기준
K = 2                    # 성분 수 고정 (stable-K)
EPS_OT = 0.1             # sharp regime (A7') 기준값
LAMBDA_M = 1.0
LAMBDA_C = 0.005
RHO_PERS = 0.5           # PersComp threshold
TAU_ID = 0.1             # 대응 임계값
MASS_FRACTION = 0.85     # sinkhorn_partial_ot mass fraction
N_TRIALS = 15            # 각 motion 크기별 5개, 총 3×5=15
```

### 세 시점 장 생성

```python
# t 시점: K=2 Gaussian blob (well-separated)
u_t: 두 blob, centers (4,4), (11,11), radius=2.0
     
# s 시점: 소량 이동 (stable-K 유지)
u_s: 두 blob, centers (4+dx_1, 4+dy_1), (11+dx_2, 11+dy_2)
     이동 크기 Δxy ∈ {small=1, medium=2, large=3}

# r 시점: s에서 추가 이동 (동일 방향, 동일 크기)
u_r: 두 blob, s 위치에서 추가 Δxy 이동
```

안전 조건: blob 중심 간 거리 ≥ 6 (well-separated, no merge).

### 수송 계획 계산

```python
# 세 가지 수송 계획 계산
M_ts = sinkhorn_partial_ot(cost_ts, mu=u_t, nu=u_s, eps=EPS_OT, mass_fraction=MASS_FRACTION)
M_sr = sinkhorn_partial_ot(cost_sr, mu=u_s, nu=u_r, eps=EPS_OT, mass_fraction=MASS_FRACTION)
M_tr = sinkhorn_partial_ot(cost_tr, mu=u_t, nu=u_r, eps=EPS_OT, mass_fraction=MASS_FRACTION)
# cost_{ab}(x,y) = ‖φ(x) - φ(y)‖² + σ_sp^{-2}‖x-y‖²
```

### 대응 계산

```python
# 직접 대응
comps_t, comps_r = extract_perscomp(u_t, rho_pers), extract_perscomp(u_r, rho_pers)
S_tr = component_score_matrix(u_t, u_r, M_tr, comps_t, comps_r, LAMBDA_M, LAMBDA_C)
pi_tr_direct = argmax_bijection(S_tr)  # argmax per row under mutual-max condition

# 합성 대응
comps_s = extract_perscomp(u_s, rho_pers)
S_ts = component_score_matrix(u_t, u_s, M_ts, comps_t, comps_s, LAMBDA_M, LAMBDA_C)
S_sr = component_score_matrix(u_s, u_r, M_sr, comps_s, comps_r, LAMBDA_M, LAMBDA_C)
pi_ts = argmax_bijection(S_ts)
pi_sr = argmax_bijection(S_sr)
pi_comp = compose_bijections(pi_sr, pi_ts)  # π_{sr} ∘ π_{ts}
```

---

## 측정 항목

각 trial마다 다음을 기록:

| 측정값 | 설명 | 계산 방법 |
|--------|------|-----------|
| `delta_ts` | [t,s] margin Δ_sep | min(row_margin, col_margin) of S_ts |
| `delta_sr` | [s,r] margin Δ_sep | min(row_margin, col_margin) of S_sr |
| `delta_min` | 전체 margin min | min(delta_ts, delta_sr) |
| `eps_comp_measured` | 측정된 합성 오차 | max_{i,k} \|S_tr[i,k] - S_comp[i,k]\| |
| `match` | 직접 vs 합성 일치 여부 | pi_tr_direct == pi_comp (bool) |
| `gap` | Δ_min - 2·eps_comp | delta_min - 2·eps_comp_measured |
| `result` | PASS/FAIL | PASS if match, FAIL otherwise |
| `fail_reason` | FAIL 원인 | margin 부족 / K 불안정 / 수치 오류 등 |

```python
S_comp[i,k] = max_j [S_ts[i,j]/min(m_t[i],m_s[j]) + S_sr[j,k]/min(m_s[j],m_r[k])]
# 합성 점수의 상한 추정 (실제 S_tr과 비교용)
```

---

## 예상 결과 테이블

| Trial 유형 | Δ_min 예상 | ε_comp 예상 | gap > 0 | 예상 결과 |
|-----------|-----------|-----------|---------|----------|
| Small motion (Δxy=1) | ≥ 0.7 | ≈ 0.05 | yes | **PASS** |
| Medium motion (Δxy=2) | ≈ 0.4 | ≈ 0.15 | yes (좁음) | **PASS** |
| Large motion (Δxy=3) | ≈ 0.1 | ≈ 0.15 | no | **FAIL** (예상) |

FAIL 예상 시 예상 원인:
- Large motion: 성분 간격이 줄어들어 margin 감소; 합성 오차가 margin 초과

---

## 검증할 이론 주장

| 주장 | 검증 방법 |
|------|----------|
| CC-1: bijection 존재 | K_t=K_s=K_r=2 확인, S_ts/S_sr 각각 bijection 유도 확인 |
| CC-3: argmax stability | gap = Δ_min - 2·ε_comp > 0 → match=True 비율 ≥ 90% |
| T-CC-StableK | 전체 PASS율 + gap vs match 상관관계 |

추가 검증:
- ε_comp의 ε_OT 의존성: ε_OT ∈ {0.1, 0.5, 1.0}에서 ε_comp 변화 관찰
- gap = 0 근방에서의 실패율 (임계 거동 확인)

---

## 구현 계획

### 신규 함수

```python
# CODE/scc/transport.py 또는 CODE/scc/temporal_identity.py 에 추가

def component_score_matrix(u_t, u_s, M, comps_t, comps_s, lambda_m, lambda_c, cost=None):
    """K_t × K_s 점수 행렬 계산 (정규화 포함)."""
    ...

def argmax_bijection(S_tilde):
    """정규화 점수 행렬에서 mutual-max bijection 추출."""
    ...

def compose_bijections(pi_sr, pi_ts):
    """π_{sr} ∘ π_{ts} 계산."""
    return {i: pi_sr[pi_ts[i]] for i in pi_ts}

def measure_composition_error(S_tr_tilde, S_ts_tilde, S_sr_tilde, comps_s):
    """직접 점수와 합성 점수 상한의 최대 차이 측정."""
    ...
```

### 기존 함수 재사용

```python
# 이미 구현됨 (exp83 기준):
from scc.transport import sinkhorn_partial_ot
from scc.diagnostics import DiagnosticVector
# PersComp: scipy.ndimage 프록시 (D-ST-3 전용 구현은 exp83 미포함)
```

### 출력 형식

```python
# 각 trial별 결과 dict
{
    "trial_id": int,
    "motion_size": float,
    "delta_ts": float,
    "delta_sr": float,
    "delta_min": float,
    "eps_comp_measured": float,
    "gap": float,
    "pi_tr_direct": list,    # [K] permutation
    "pi_comp": list,         # [K] composed permutation
    "match": bool,
    "result": "PASS"/"FAIL",
    "fail_reason": str or None
}

# 집계 결과
{
    "total": 15,
    "passed": int,
    "failed": int,
    "pass_rate": float,
    "gap_positive_but_fail": int,   # 이론 위반 케이스 수
    "mean_eps_comp": float,
    "mean_delta_min": float
}
```

---

## 목표 파일명

```
CODE/experiments/exp_cc_stablek_composition.py
CODE/experiments/results/exp_cc_stablek_composition.json
```

번호는 현존 실험 번호 (exp57 이후) 확인 후 할당.

---

## 구현 사전 조건

1. `component_score_matrix` 함수 구현 (~30줄)
2. `argmax_bijection` 함수 구현 (~15줄)
3. `measure_composition_error` 함수 구현 (~20줄)
4. Gaussian blob 장 생성 유틸리티 (exp83에서 이식 가능)
5. `extract_perscomp` 함수 (exp83 프록시 이식 가능)

추정 구현 시간: 1–2시간 (exp83 코드 재사용 시).

---

## 이론 검증과 연결

실험 결과가 이론에 미치는 영향:

| 결과 | 이론적 함의 |
|------|-----------|
| PASS율 ≥ 90% (gap > 0 케이스) | T-CC-StableK 수치적 지지, Cat B 달성 근거 |
| gap > 0임에도 FAIL | Lemma CC-3 또는 CC-2 수정 필요 |
| ε_comp ∝ ε_OT 관계 확인 | CC-4 Route A bound 지지 |
| ε_comp ≈ 0 (self-referential) | CC-4 Route B 성립 확인 |

---

*작성: 2026-05-12. 미구현 상태; 구현 전 이론 파일 (02, 03) 안정화 권장.*
