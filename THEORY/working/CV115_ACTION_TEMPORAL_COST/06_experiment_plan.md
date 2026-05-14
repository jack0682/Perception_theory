---
id: ACT-06
type: working/theory
status: open — 실험 계획
created: 2026-05-12
scope: exp89_endpoint_vs_action_temporal_cost.py
---

> [!nav] Linked: [[MOC_action_temporal_cost]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# 06. 실험 계획 — exp89_endpoint_vs_action_temporal_cost.py

---

## 목표

**Endpoint cost와 action cost의 composition residual 비교**.

이론적 예측:
- `endpoint_residual > 0` (L-ENDPOINT-NONSEMI)
- `action_residual ≈ 0` (T-ACT-DP, 수치 오차 수준)
- `soft_action_residual ≈ 0` (T-ACT-GIBBS, 수치 오차 수준)
- `kernel_semigroup_residual ≈ machine epsilon`
- `sinkhorn_plan_residual > 0` (T-SINKHORN-PLAN-SEMIGROUP-FAILS, 일반적으로)

---

## 실험 구조

### 파라미터

```python
GRID_SIZE   = 15          # 15×15 2D grid; N = 225 sites
K_FORM      = 2           # 2 formations (stable-K 조건 만족)
MOTION_SIZES = [1.0, 2.0, 3.0]   # formation 이동 거리 (site 단위)
N_TRIALS    = 5           # 랜덤 시드 5개
GAMMA       = 1.0         # fingerprint 가중치
EPSILON     = [0.01, 0.1, 1.0]   # Gibbs kernel 온도
```

### 시간 격자

$t \to s \to r$: 3단계, $\Delta t = 1$.

---

## 실험 절차

### Step 1: Formation 생성

2D 15×15 grid에서 K=2 formation 생성.

```python
# t 시각 formation 생성
g_t = GraphState.grid_2d(15, 15)
params = ParameterRegistry()
u_t = find_formation(g_t, params, K=2).u  # shape (225,)

# s 시각: gentle deformation (등속 이동)
# 각 formation 중심을 motion_size만큼 이동
u_s = move_formation(u_t, motion_size=motion_size, direction="right")

# r 시각: 추가 이동 (t→s와 동일 방향/거리)
u_r = move_formation(u_s, motion_size=motion_size, direction="right")
```

### Step 2: Endpoint Cost 계산

```python
def endpoint_cost(u_a, u_b, graph):
    """
    c_endpoint[i,j] = ||x_i - x_j||^2 (공간 좌표 기반)
    또는 site index 기반 squared distance.
    """
    coords = graph.node_coords  # (N, 2)
    diff = coords[:, None, :] - coords[None, :, :]  # (N, N, 2)
    return np.sum(diff**2, axis=-1)  # (N, N)

c_endpoint_tr = endpoint_cost(u_t, u_r, g_t)

# Effective: min_y[c(t,s) + c(s,r)]
c_endpoint_ts = endpoint_cost(u_t, u_s, g_t)
c_endpoint_sr = endpoint_cost(u_s, u_r, g_t)
c_endpoint_eff = np.min(
    c_endpoint_ts[:, :, None] + c_endpoint_sr[None, :, :],
    axis=1
)  # (N_t, N_r)

endpoint_residual = np.max(np.abs(c_endpoint_tr - c_endpoint_eff))
```

### Step 3: Action Cost 계산

```python
def local_action(u_a, u_b, graph_a, graph_b, dt=1.0, gamma=1.0):
    """
    a[i,j] = d(i,j)^2/dt + gamma * ||phi_b(j) - phi_a(i)||^2 / dt
    """
    coords_a = graph_a.node_coords   # (N_a, 2)
    coords_b = graph_b.node_coords   # (N_b, 2)
    
    # 공간 거리 항
    diff_coord = coords_a[:, None, :] - coords_b[None, :, :]
    spatial = np.sum(diff_coord**2, axis=-1) / dt  # (N_a, N_b)
    
    # SCC fingerprint
    phi_a = compute_fingerprint(u_a, graph_a)  # (N_a, 3)
    phi_b = compute_fingerprint(u_b, graph_b)  # (N_b, 3)
    diff_phi = phi_a[:, None, :] - phi_b[None, :, :]
    finger = gamma * np.sum(diff_phi**2, axis=-1) / dt  # (N_a, N_b)
    
    return spatial + finger

def hard_min_cost(a_ts, a_sr):
    """
    c^act_tr[i,k] = min_j [a_ts[i,j] + a_sr[j,k]]
    """
    # (N_t, N_s) + (N_s, N_r) -> (N_t, N_r)
    return np.min(a_ts[:, :, None] + a_sr[None, :, :], axis=1)

a_ts = local_action(u_t, u_s, g_t, g_s)
a_sr = local_action(u_s, u_r, g_s, g_r)

# Direct: 전체 경로 action 직접 계산
# (2-hop: i→j→k 합산의 전체 min)
c_action_tr_direct = hard_min_cost(a_ts, a_sr)  # 이것이 곧 effective

# Effective (이론상 같아야 함):
c_action_tr_eff = hard_min_cost(a_ts, a_sr)

action_residual = np.max(np.abs(c_action_tr_direct - c_action_tr_eff))
# 기대: ≈ 0 (machine epsilon)
```

**비고**: 2-hop 경우 direct = effective (T-ACT-DP에서 j가 유일 중간점). 3-hop에서 의미 있는 검증 가능.

### 3-hop 검증 (direct vs DP)

```python
# t→s→r→q: 4단계
u_q = move_formation(u_r, motion_size=motion_size, direction="right")
a_rq = local_action(u_r, u_q, g_r, g_q)

# Direct: t→q 전체 3-hop min
c_direct_tq = hard_min_cost_3hop(a_ts, a_sr, a_rq)
# c_direct_tq[i,l] = min_{j,k} [a_ts[i,j] + a_sr[j,k] + a_rq[k,l]]

# DP: t→r 먼저 계산 후 r→q
c_tr = hard_min_cost(a_ts, a_sr)      # (N_t, N_r)
c_dp_tq = hard_min_cost(c_tr, a_rq)   # (N_t, N_q)

action_dp_residual = np.max(np.abs(c_direct_tq - c_dp_tq))
# 기대: ≈ 0 (T-ACT-DP 검증)
```

### Step 4: Soft-Min / Gibbs Kernel 계산

```python
def gibbs_kernel(a, epsilon):
    """K[i,j] = exp(-a[i,j]/epsilon)"""
    return np.exp(-a / epsilon)

def gibbs_long(K_ts, K_sr):
    """K_tr = K_ts @ K_sr"""
    return K_ts @ K_sr

for eps in EPSILON:
    K_ts = gibbs_kernel(a_ts, eps)   # (N_t, N_s)
    K_sr = gibbs_kernel(a_sr, eps)   # (N_s, N_r)
    
    # Direct long kernel: exp(-A_{t:r}/eps) 합산
    # 2-hop: K_tr_direct = K_ts @ K_sr (이것이 정의)
    K_tr_product = gibbs_long(K_ts, K_sr)
    
    # Soft cost
    c_soft_tr_direct = -eps * np.log(K_tr_product + 1e-300)
    
    # Soft effective
    c_soft_ts = -eps * np.log(K_ts + 1e-300)  # (N_t, N_s)
    c_soft_sr = -eps * np.log(K_sr + 1e-300)  # (N_s, N_r)
    c_soft_tr_eff = -eps * np.log(
        np.sum(np.exp(-(c_soft_ts[:, :, None] + c_soft_sr[None, :, :]) / eps), axis=1)
        + 1e-300
    )
    
    soft_action_residual = np.max(np.abs(c_soft_tr_direct - c_soft_tr_eff))
    kernel_semigroup_residual = np.max(np.abs(K_tr_product - K_ts @ K_sr))
    # kernel_semigroup_residual ≈ 0 (항등적으로 T-ACT-GIBBS)
```

### Step 5: Sinkhorn Plan Residual

```python
from scc.transport import sinkhorn_log_domain

def sinkhorn_plan(K, u_a, u_b, n_iter=100):
    """Sinkhorn(K; marginal u_a, u_b) = diag(a) K diag(b)"""
    log_K = np.log(K + 1e-300)
    # log-domain Sinkhorn
    log_a = np.zeros(len(u_a))
    log_b = np.zeros(len(u_b))
    for _ in range(n_iter):
        log_a = np.log(u_a + 1e-300) - np.log(np.exp(log_K + log_b[None, :]).sum(axis=1) + 1e-300)
        log_b = np.log(u_b + 1e-300) - np.log(np.exp(log_K + log_a[:, None]).sum(axis=0) + 1e-300)
    a = np.exp(log_a)
    b = np.exp(log_b)
    return np.diag(a) @ K @ np.diag(b)

for eps in EPSILON:
    K_ts = gibbs_kernel(a_ts, eps)
    K_sr = gibbs_kernel(a_sr, eps)
    K_tr = K_ts @ K_sr  # T-ACT-GIBBS
    
    M1 = sinkhorn_plan(K_ts, u_t, u_s)   # M^sink(K_ts)
    M2 = sinkhorn_plan(K_sr, u_s, u_r)   # M^sink(K_sr)
    M_tr = sinkhorn_plan(K_tr, u_t, u_r)  # M^sink(K_tr)
    
    sinkhorn_plan_residual = np.max(np.abs(M1 @ M2 - M_tr))
    # 기대: > 0 (T-SINKHORN-PLAN-SEMIGROUP-FAILS)
```

---

## 출력 항목

```python
results = {
    "trial": trial_idx,
    "motion_size": motion_size,
    "epsilon": eps,
    "endpoint_residual": endpoint_residual,       # > 0 기대
    "action_residual": action_residual,            # ≈ 0 기대
    "action_dp_residual": action_dp_residual,      # ≈ 0 기대 (3-hop DP)
    "soft_action_residual": soft_action_residual,  # ≈ 0 기대
    "kernel_semigroup_residual": kernel_semigroup_residual,  # ≈ 0 기대
    "sinkhorn_plan_residual": sinkhorn_plan_residual,        # > 0 기대
}
```

---

## 기대 결과 요약

| 측정값 | 이론 예측 | 이유 |
|---|---|---|
| `endpoint_residual` | $> 0$ (= $\|z-x\|^2/2$) | L-ENDPOINT-NONSEMI |
| `action_residual` | $\approx 0$ | T-ACT-DP |
| `action_dp_residual` | $\approx 0$ | T-ACT-DP (3-hop) |
| `soft_action_residual` | $\approx 0$ | T-ACT-GIBBS |
| `kernel_semigroup_residual` | $\approx 10^{-14}$ | T-ACT-GIBBS (항등적) |
| `sinkhorn_plan_residual` | $> 0$ (일반적) | T-SINKHORN-PLAN-SEMIGROUP-FAILS |

---

## 구현 경로

파일 위치: `CODE/experiments/exp89_endpoint_vs_action_temporal_cost.py`

필요한 함수 목록:

```
compute_fingerprint(u, graph) -> (N, 3)
local_action(u_a, u_b, graph_a, graph_b, dt, gamma) -> (N_a, N_b)
hard_min_cost(a_ts, a_sr) -> (N_t, N_r)
hard_min_cost_3hop(a_ts, a_sr, a_rq) -> (N_t, N_q)
gibbs_kernel(a, epsilon) -> (N_a, N_b)
sinkhorn_plan(K, u_a, u_b, n_iter) -> (N_a, N_b)
move_formation(u, motion_size, direction) -> (N,)
```

기존 SCC 모듈에서 재사용 가능:
- `scc.graph.GraphState` — grid 생성, 좌표
- `scc.operators.closure` — fingerprint Cl 성분
- `scc.operators.distinction` — fingerprint D 성분
- `scc.transport.sinkhorn_log_domain` — Sinkhorn plan (수정 필요할 수 있음)

---

*작성: 2026-05-12.*
