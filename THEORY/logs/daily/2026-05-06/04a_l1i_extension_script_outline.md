> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 04a_l1i_extension_script_outline.md — NQ-G1-2-ext Script Outline

**Session:** 2026-05-06 (W6 Day 3 G3.4, sub-file of `04_nq_g1_2_ext_design.md`).
**Goal:** Pseudo-code + module dependency map for the NQ-G1-2-ext wrapper script.
**Status:** Design spec only. W7 D1 morning: implement as `CODE/experiments/exp58_nq_g1_2_ext.py`.

---

## §1. Module Dependency Map

```
exp58_nq_g1_2_ext.py
  ├── scc.graph          GraphState.torus_2d(20, 20)
  ├── scc.params         ParameterRegistry (ε=0.225, Commitment 16 default)
  ├── scc.multi          build_initial_state (wq1 config loader), gradient_step_k_field
  ├── scc.energy         EnergyComputer (for Hessian verification, optional)
  ├── scc.optimizer      find_formation (single-slot; reused inside multi-step)
  └── scc.diagnostics    DiagnosticVector (optional; for slot-level sanity check)
```

**Key entry points** (verify these exist before W7 D1):
- `scc.multi.build_initial_state(config, graph, params)` → $\mathbf{u}_0 \in \Sigma^K_M$ (wq1 construction)
- `scc.multi.gradient_step_k_field(u_field, graph, params)` → $\mathbf{u}_{t+1}$ (one projected gradient step)
- No new module needed; script wraps existing multi.py infrastructure.

---

## §2. Script Pseudo-Code

```python
# exp58_nq_g1_2_ext.py
# NQ-G1-2-ext: Post-flow R_j residual measurement over 960 wq1 configs.

import json, numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import build_initial_state, gradient_step_k_field

# --- Config ---
GRAPH = GraphState.torus_2d(20, 20)        # T^2_20, n=400
PARAMS = ParameterRegistry(epsilon=0.225)  # Commitment 16 default
K_FIELD = 4
N_STEPS = 1000
MEASURE_INTERVAL = 50                      # 20 snapshots at t=50,100,...,1000
OUTPUT_PATH = "results/nq_g1_2_ext_results.json"

# --- Load 960 wq1 configs ---
# From NQ-G3-1 baseline JSON (wq1 configs only; exclude raw_gaussian)
wq1_configs = load_wq1_configs("results/nq_g3_1_baseline.json")  # 960 configs
assert len(wq1_configs) == 960

results = []

for cfg_idx, cfg in enumerate(wq1_configs):
    # Build initial state
    u0 = build_initial_state(cfg, GRAPH, PARAMS)   # shape: (K_FIELD, n)

    # Compute ideal reference for each slot j at t=0
    # u_ideal^(j): Gaussian centered at centroid(u0[j]) with same mass
    u_ideal = [compute_ideal_gaussian(u0[j], GRAPH) for j in range(K_FIELD)]

    trajectory_residuals = {}   # t -> list of ||R_j||_inf per slot

    u = u0.copy()

    for step in range(1, N_STEPS + 1):
        u = gradient_step_k_field(u, GRAPH, PARAMS)

        if step % MEASURE_INTERVAL == 0:
            slot_residuals = []
            for j in range(K_FIELD):
                R_j = u[j] - u_ideal[j]   # elementwise residual
                r_inf = np.max(np.abs(R_j))
                slot_residuals.append(float(r_inf))
            trajectory_residuals[step] = slot_residuals

    # Per-config summary
    # max over time and slots of ||R_j||_inf
    all_residuals = [r for rs in trajectory_residuals.values() for r in rs]
    max_residual = max(all_residuals)
    avg_residual = np.mean(all_residuals)

    results.append({
        "cfg_idx": cfg_idx,
        "max_R_inf": max_residual,
        "avg_R_inf": avg_residual,
        "trajectory": trajectory_residuals   # full trace for histogramming
    })

    if cfg_idx % 100 == 0:
        print(f"[{cfg_idx}/960] max_R_inf={max_residual:.4f}")

# --- Save ---
with open(OUTPUT_PATH, "w") as f:
    json.dump(results, f, indent=2)
print(f"Saved {len(results)} configs to {OUTPUT_PATH}")
```

---

## §3. `compute_ideal_gaussian` Helper

The "ideal" Gaussian reference for slot $j$ is:
$$u^{(j),\mathrm{ideal}}_i = \frac{m_j}{Z_j} \exp\!\left(-\frac{\lVert i - c_j \rVert^2}{2\sigma_j^2}\right)$$
where:
- $c_j = \sum_i i \cdot u^{(j)}_i / m_j$ = centroid of slot $j$ at the **initial** state.
- $\sigma_j$ = width parameter (set to match the "typical" Gaussian width for mass $m_j$ on $T^2_{20}$; default: $\sigma_j = \sqrt{m_j / (2\pi)}$ in continuous approximation).
- $Z_j$ = normalization to ensure $\sum_i u^{(j),\mathrm{ideal}}_i = m_j$ (renormalize to same mass as initial slot).

**Important:** $u^{(j),\mathrm{ideal}}$ is computed **once from $u_0$** and held fixed for the entire trajectory. This means:
- $R_j(t) = u^{(j)}(t) - u^{(j),\mathrm{ideal}}$ measures deviation from the initial ideal, not a time-varying ideal.
- This is the correct definition for the T-L1-F regime check: P9 asks whether the shape deviates from a Gaussian-like profile, not whether it tracks an evolving Gaussian.

```python
def compute_ideal_gaussian(u0_j, graph):
    """
    u0_j: initial cohesion field for slot j, shape (n,)
    graph: GraphState with node positions
    Returns: u_ideal of same mass as u0_j, Gaussian centered at centroid(u0_j)
    """
    mass = np.sum(u0_j)
    if mass < 1e-8:
        return np.zeros_like(u0_j)   # empty slot

    positions = graph.node_positions   # (n, 2) for torus_2d
    centroid = np.sum(positions * u0_j[:, None], axis=0) / mass

    # Torus-aware distances (wrap-around)
    diffs = positions - centroid[None, :]
    diffs = diffs - np.round(diffs / graph.grid_size) * graph.grid_size   # wrap
    sq_dist = np.sum(diffs**2, axis=1)

    sigma = np.sqrt(mass / (2 * np.pi))   # continuous-limit width
    raw = np.exp(-sq_dist / (2 * sigma**2))
    normalized = raw * (mass / np.sum(raw))   # rescale to same mass
    return normalized
```

---

## §4. Implementation Notes for W7 D1

1. **Verify** `scc.multi.gradient_step_k_field` signature (may be named `step_k_field` or similar — check `CODE/scc/multi.py` before running).
2. **Verify** `build_initial_state` accepts wq1 config format from NQ-G3-1 JSON.
3. **Baseline JSON path** (`nq_g3_1_baseline.json`): verify exists in `CODE/results/` before running.
4. **Wall-clock check:** Run 10 configs first, time it. If > 10s per config → parallelize with `multiprocessing.Pool`.
5. **Output size:** 960 configs × 20 snapshots × 4 slots = 76,800 residual values. JSON ~3 MB. Acceptable.

---

**End of `04a_l1i_extension_script_outline.md`. NQ-G1-2-ext implementation map complete. W7 D1 execution target: `exp58_nq_g1_2_ext.py`.**
