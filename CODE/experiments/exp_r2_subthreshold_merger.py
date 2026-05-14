#!/usr/bin/env python3
"""R-2 OP-R2-9 sub-threshold merger demonstration (Phase C2b).

Verifies the §12 construction of R2_op_R2_9_sigma_inheritance.md: that R-2's
bar-attribute trajectory captures a structural event (sub-threshold bar death)
that K-tuple AFD-0's K_act trajectory cannot register.

Construction:
  - Path graph P_7 with vertices v_0..v_6, positions pos(v_i) = i.
  - Continuous family u_t for t in [0, 1]:
      u_t(v_0) = 0.0
      u_t(v_1) = 0.9   (dominant peak, constant)
      u_t(v_2) = 0.4   (constant)
      u_t(v_3) = 0.1 + 0.2*t   (saddle, rising)
      u_t(v_4) = 0.3 - 0.2*t   (secondary peak, eroding)
      u_t(v_5) = 0.1   (constant)
      u_t(v_6) = 0.0
  - Persistence threshold rho_pers = 0.5.
  - Critical time t_* = 0.5 (where u(v_3) = u(v_4) = 0.2).

Predictions:
  1. K_read^{0.5}(u_t) = 1 for all t in [0, 1].
  2. |PD_0(u_t)| = 2 for t < t_*; = 1 for t >= t_*.
  3. R-2 bar-1 absorbing-component centroid: 1.308 (t < t_*), ~1.667-1.824 (t > t_*).
     Discrete jump |Delta c_{b_1}| ~ 0.36-0.52 at t_*.
  4. K-tuple AFD-0 centroid (full positive-u support): smooth, no jump.

Output: results/exp_r2_subthreshold_merger.json
"""
import sys, os, json
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# Graph construction
# ---------------------------------------------------------------------------

def make_path_graph(n_vertices=7):
    """Path graph P_n with n vertices, edges (i, i+1)."""
    row_idx, col_idx = [], []
    for i in range(n_vertices - 1):
        row_idx.extend([i, i + 1])
        col_idx.extend([i + 1, i])
    data = np.ones(len(row_idx))
    W = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n_vertices, n_vertices))

    class SimpleGraph:
        def __init__(self, W):
            self.W = W
            self.n = W.shape[0]
    return SimpleGraph(W)


# ---------------------------------------------------------------------------
# Field u_t
# ---------------------------------------------------------------------------

def u_t(t):
    """Cohesion field parametrized by t in [0, 1]."""
    return np.array([
        0.0,           # v_0
        0.9,           # v_1: dominant peak
        0.4,           # v_2
        0.1 + 0.2 * t, # v_3: saddle rises
        0.3 - 0.2 * t, # v_4: secondary peak erodes
        0.1,           # v_5
        0.0,           # v_6
    ])


# ---------------------------------------------------------------------------
# PD_0 with per-bar vertex supports
# ---------------------------------------------------------------------------

def persistence_with_supports(u, graph):
    """Compute H_0 persistence bars + per-bar vertex supports via Union-Find.

    Returns list of dicts with keys: birth, death, length, support, root_vertex.
    Sorted by length descending.
    """
    n = graph.n
    order = np.argsort(-u)

    W_coo = graph.W.tocoo()
    adj = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    root_vertex = np.full(n, -1, dtype=int)
    component_vertices = {i: {i} for i in range(n)}
    active = np.zeros(n, dtype=bool)
    bars = []

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        active[idx] = True
        birth_val[idx] = u[idx]
        root_vertex[idx] = idx

        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            if birth_val[ri] >= birth_val[rn]:
                dying_root = root_vertex[rn]
                bars.append({
                    "birth": float(birth_val[rn]),
                    "death": float(u[idx]),
                    "length": float(birth_val[rn] - u[idx]),
                    "support": set(component_vertices[rn]),
                    "root_vertex": int(dying_root),
                })
                component_vertices[ri].update(component_vertices[rn])
                component_vertices[ri].add(idx)
                del component_vertices[rn]
                parent[rn] = ri
            else:
                dying_root = root_vertex[ri]
                bars.append({
                    "birth": float(birth_val[ri]),
                    "death": float(u[idx]),
                    "length": float(birth_val[ri] - u[idx]),
                    "support": set(component_vertices[ri]),
                    "root_vertex": int(dying_root),
                })
                component_vertices[rn].update(component_vertices[ri])
                component_vertices[rn].add(idx)
                del component_vertices[ri]
                parent[ri] = rn

    # Surviving bar(s)
    for sr in list(component_vertices.keys()):
        bars.append({
            "birth": float(np.max(u[list(component_vertices[sr])])),
            "death": 0.0,
            "length": float(np.max(u[list(component_vertices[sr])])),
            "support": set(component_vertices[sr]),
            "root_vertex": int(root_vertex[sr]),
        })

    bars.sort(key=lambda b: b["length"], reverse=True)
    return bars


# ---------------------------------------------------------------------------
# Bar attributes (R-2 D-R2-7)
# ---------------------------------------------------------------------------

def bar_centroid(bar, u, positions):
    """Centroid of bar support, u-weighted."""
    support = list(bar["support"])
    if len(support) == 0:
        return None
    u_supp = u[support]
    pos_supp = positions[support]
    mass = float(np.sum(u_supp))
    if mass < 1e-12:
        return float(pos_supp.mean())
    return float((u_supp * pos_supp).sum() / mass)


def absorbing_component_centroid(u, graph, peak_vertex, level):
    """Compute centroid of the H_0 component containing peak_vertex at superlevel level.

    R-2 absorbing-component definition: the component containing the dominant
    peak at the level just above the saddle.
    """
    n = graph.n
    above = np.where(u > level)[0]
    if peak_vertex not in above:
        return None, 0.0, []

    # BFS from peak_vertex restricted to above-level vertices
    W_coo = graph.W.tocoo()
    adj = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    above_set = set(above.tolist())
    visited = {peak_vertex}
    stack = [peak_vertex]
    while stack:
        x = stack.pop()
        for nb in adj[x]:
            if nb in above_set and nb not in visited:
                visited.add(nb)
                stack.append(nb)

    component = sorted(visited)
    u_comp = u[component]
    positions = np.arange(n, dtype=float)
    pos_comp = positions[component]
    mass = float(np.sum(u_comp))
    if mass < 1e-12:
        return None, mass, component
    centroid = float((u_comp * pos_comp).sum() / mass)
    return centroid, mass, component


def k_tuple_F1_centroid(u, positions):
    """K-tuple AFD-0 centroid: u-weighted over full positive-u support."""
    above = u > 1e-9
    u_pos = u[above]
    pos_pos = positions[above]
    mass = float(u_pos.sum())
    if mass < 1e-12:
        return None
    return float((u_pos * pos_pos).sum() / mass)


# ---------------------------------------------------------------------------
# K_read counting
# ---------------------------------------------------------------------------

def k_read(bars, rho_pers):
    """K_read^{rho_pers, H_0} = count of bars with length >= rho_pers."""
    return sum(1 for b in bars if b["length"] >= rho_pers)


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_experiment(n_steps=101, rho_pers=0.5):
    """Run sub-threshold merger demonstration on P_7."""
    print("=== R-2 sub-threshold merger demonstration ===")
    print(f"Graph: P_7 (7-vertex path); rho_pers = {rho_pers}; n_steps = {n_steps}")
    print()

    graph = make_path_graph(7)
    positions = np.arange(7, dtype=float)  # pos(v_i) = i

    t_values = np.linspace(0.0, 1.0, n_steps)
    t_star_predicted = 0.5

    trajectory = []
    for t in t_values:
        u = u_t(t)
        bars = persistence_with_supports(u, graph)
        # Filter trivial 1-vertex bars at zero (boundary v_0, v_6 which are u=0)
        bars = [b for b in bars if b["length"] > 1e-9]

        n_bars = len(bars)
        kr = k_read(bars, rho_pers)

        # R-2 bar-1 absorbing-component centroid:
        # peak vertex of bar_1 = v_1 (always). Level = u(v_3) + tiny epsilon (just above saddle).
        u_saddle = u[3]
        eps = 1e-6
        c_b1_absorbing, m_b1, comp_b1 = absorbing_component_centroid(u, graph, peak_vertex=1, level=u_saddle + eps)

        # K-tuple AFD-0 centroid (full positive-u support)
        c_F1_ktuple = k_tuple_F1_centroid(u, positions)

        # Bar 2 attributes (if present)
        bar_2_info = None
        if n_bars >= 2:
            bar_2 = bars[1]
            bar_2_info = {
                "length": bar_2["length"],
                "birth": bar_2["birth"],
                "death": bar_2["death"],
                "support": sorted(bar_2["support"]),
                "centroid": bar_centroid(bar_2, u, positions),
            }

        trajectory.append({
            "t": float(t),
            "u": u.tolist(),
            "n_bars": n_bars,
            "K_read": kr,
            "bar_1": {
                "length": bars[0]["length"],
                "support": sorted(bars[0]["support"]),
            } if n_bars >= 1 else None,
            "bar_2": bar_2_info,
            "R2_absorbing_centroid_b1": c_b1_absorbing,
            "R2_absorbing_mass_b1": m_b1,
            "R2_absorbing_component_b1": comp_b1,
            "ktuple_F1_centroid": c_F1_ktuple,
        })

    # ----- Analyze trajectory -----
    K_read_values = [s["K_read"] for s in trajectory]
    n_bars_values = [s["n_bars"] for s in trajectory]
    c_b1_R2 = [s["R2_absorbing_centroid_b1"] for s in trajectory]
    c_F1_K = [s["ktuple_F1_centroid"] for s in trajectory]

    K_read_invariant = all(k == K_read_values[0] for k in K_read_values)

    # Detect transition in n_bars
    nbars_transition_idx = None
    for i in range(1, len(n_bars_values)):
        if n_bars_values[i] != n_bars_values[i - 1]:
            nbars_transition_idx = i
            break

    # R-2 centroid jump magnitude near transition
    if nbars_transition_idx is not None:
        c_pre = c_b1_R2[nbars_transition_idx - 1]
        c_post = c_b1_R2[nbars_transition_idx]
        R2_centroid_jump = abs((c_post or 0) - (c_pre or 0)) if c_pre is not None and c_post is not None else None
    else:
        R2_centroid_jump = None

    # K-tuple smoothness: largest step in c_F1
    if c_F1_K[0] is not None:
        ktuple_max_step = max(abs(c_F1_K[i] - c_F1_K[i - 1]) for i in range(1, len(c_F1_K))
                              if c_F1_K[i] is not None and c_F1_K[i - 1] is not None)
    else:
        ktuple_max_step = None

    # R-2 max step in absorbing centroid
    R2_max_step = None
    valid_pairs = [(c_b1_R2[i], c_b1_R2[i - 1]) for i in range(1, len(c_b1_R2))
                   if c_b1_R2[i] is not None and c_b1_R2[i - 1] is not None]
    if valid_pairs:
        R2_max_step = max(abs(a - b) for a, b in valid_pairs)

    print(f"K_read^{rho_pers} invariant across trajectory: {K_read_invariant}")
    print(f"  Values: min={min(K_read_values)}, max={max(K_read_values)}, all={K_read_values[0] if K_read_invariant else 'varies'}")
    print()
    print(f"n_bars transition detected at step {nbars_transition_idx} (t={t_values[nbars_transition_idx]:.3f})" if nbars_transition_idx else "No n_bars transition.")
    print(f"  n_bars trajectory (sampled): {n_bars_values[::20]}")
    print()
    print(f"R-2 absorbing-centroid c_b1 trajectory:")
    print(f"  At t=0.00: {c_b1_R2[0]:.4f}")
    if nbars_transition_idx is not None:
        print(f"  At t={t_values[nbars_transition_idx - 1]:.4f} (pre): {c_b1_R2[nbars_transition_idx - 1]:.4f}")
        print(f"  At t={t_values[nbars_transition_idx]:.4f}  (post): {c_b1_R2[nbars_transition_idx]:.4f}")
    print(f"  At t=1.00: {c_b1_R2[-1]:.4f}")
    print(f"  R-2 centroid jump magnitude near transition: {R2_centroid_jump:.4f}" if R2_centroid_jump else "  No jump detected.")
    print(f"  R-2 max step in c_b1 across trajectory: {R2_max_step:.4f}" if R2_max_step is not None else "")
    print()
    print(f"K-tuple AFD-0 centroid c_F1 (full positive-u support):")
    print(f"  At t=0.00: {c_F1_K[0]:.4f}")
    print(f"  At t=1.00: {c_F1_K[-1]:.4f}")
    print(f"  Max step across trajectory: {ktuple_max_step:.6f}" if ktuple_max_step else "")
    print()

    # Verdict: R-2 captures discrete event; K-tuple smooth
    R2_jump_significant = R2_centroid_jump is not None and R2_centroid_jump > 0.1
    ktuple_smooth = ktuple_max_step is not None and ktuple_max_step < 0.02
    R2_captures_more = R2_max_step is not None and ktuple_max_step is not None and R2_max_step > 10 * ktuple_max_step

    print("=== VERDICT ===")
    print(f"K_read invariance throughout:                            {K_read_invariant}")
    print(f"n_bars drops at transition (structural event):           {nbars_transition_idx is not None}")
    print(f"R-2 absorbing-centroid jumps (>0.1):                     {R2_jump_significant}")
    print(f"K-tuple centroid smooth (max step <0.02):                {ktuple_smooth}")
    print(f"R-2 captures discrete event K-tuple misses (10x ratio):  {R2_captures_more}")
    print()

    R2_graduates = K_read_invariant and (nbars_transition_idx is not None) and R2_jump_significant and ktuple_smooth and R2_captures_more

    print(f"==> R-2 LOAD-BEARING SCOPE EXTENSION CONFIRMED: {R2_graduates}")
    if R2_graduates:
        print("==> R-2 graduates as load-bearing language layer.")
    else:
        print("==> R-2 does NOT clearly demonstrate load-bearing scope extension. Archive recommended.")

    # ----- Pack results -----
    results = {
        "config": {
            "graph": "P_7 (7-vertex path)",
            "n_steps": n_steps,
            "rho_pers": rho_pers,
            "predicted_t_star": t_star_predicted,
        },
        "summary": {
            "K_read_invariant": bool(K_read_invariant),
            "K_read_value": int(K_read_values[0]) if K_read_invariant else None,
            "n_bars_transition_step": nbars_transition_idx,
            "n_bars_transition_t": float(t_values[nbars_transition_idx]) if nbars_transition_idx else None,
            "R2_centroid_jump_at_transition": float(R2_centroid_jump) if R2_centroid_jump else None,
            "R2_max_step_across_trajectory": float(R2_max_step) if R2_max_step else None,
            "ktuple_max_step_across_trajectory": float(ktuple_max_step) if ktuple_max_step else None,
            "R2_captures_more_than_ktuple": bool(R2_captures_more),
            "R2_graduates_load_bearing": bool(R2_graduates),
        },
        "key_timepoints": {
            "t_0": {
                "u": u_t(0.0).tolist(),
                "PD_0_bars_count": trajectory[0]["n_bars"],
                "K_read": trajectory[0]["K_read"],
                "R2_absorbing_c_b1": c_b1_R2[0],
                "ktuple_c_F1": c_F1_K[0],
            },
            "t_pre_transition": {
                "t": float(t_values[nbars_transition_idx - 1]) if nbars_transition_idx else None,
                "PD_0_bars_count": trajectory[nbars_transition_idx - 1]["n_bars"] if nbars_transition_idx else None,
                "R2_absorbing_c_b1": c_b1_R2[nbars_transition_idx - 1] if nbars_transition_idx else None,
                "ktuple_c_F1": c_F1_K[nbars_transition_idx - 1] if nbars_transition_idx else None,
            } if nbars_transition_idx else None,
            "t_post_transition": {
                "t": float(t_values[nbars_transition_idx]) if nbars_transition_idx else None,
                "PD_0_bars_count": trajectory[nbars_transition_idx]["n_bars"] if nbars_transition_idx else None,
                "R2_absorbing_c_b1": c_b1_R2[nbars_transition_idx] if nbars_transition_idx else None,
                "ktuple_c_F1": c_F1_K[nbars_transition_idx] if nbars_transition_idx else None,
            } if nbars_transition_idx else None,
            "t_1": {
                "u": u_t(1.0).tolist(),
                "PD_0_bars_count": trajectory[-1]["n_bars"],
                "K_read": trajectory[-1]["K_read"],
                "R2_absorbing_c_b1": c_b1_R2[-1],
                "ktuple_c_F1": c_F1_K[-1],
            },
        },
        "full_trajectory_sampled_every_5_steps": [trajectory[i] for i in range(0, n_steps, 5)],
    }

    # Convert numpy types and sets to JSON-serializable forms
    def to_serializable(obj):
        if isinstance(obj, set):
            return sorted(int(x) if isinstance(x, (np.integer,)) else x for x in obj)
        if isinstance(obj, dict):
            return {k: to_serializable(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [to_serializable(v) for v in obj]
        if isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        if isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return obj

    results_clean = to_serializable(results)
    return results_clean


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    results = run_experiment()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "exp_r2_subthreshold_merger.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print()
    print(f"Results saved to {out_path}")
