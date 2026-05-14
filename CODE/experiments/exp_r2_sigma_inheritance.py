#!/usr/bin/env python3
"""R-2 OP-R2-9 σ-Inheritance numerical verification (Phase B5).

Verifies Lemmas B2 (centroid mass-weighted) and B3 (orientation parallel-axis)
on canonical 15x15 grid K=2 -> K=1 merge event.

Method:
  1. Load canonical 15x15 setup (beta=50, vol_frac=0.3).
  2. Compute K=2 and K=1 minimizers via find_k_formations / find_formation.
  3. Construct path gamma(alpha) via linear interpolation (per exp38 convention).
  4. At each step:
       - Compute PD_0 bars + per-bar support via custom Union-Find.
       - For each bar, compute mass m_b, centroid c_b, orientation tensor I_b
         using vertex positions on grid (pos(x_ij) = (i, j)).
  5. Detect merge event alpha_* where K=2 -> K=1 transition occurs in PD_0.
  6. Verify Lemma B2: compare c_merged(alpha_* + delta) vs
       (m1*c1 + m2*c2)/(m1+m2) computed at alpha_* - delta.
  7. Verify Lemma B3: compare I_merged(alpha_* + delta) vs
       I_1 + I_2 + (m1*m2/(m1+m2)) * (c1-c2)(c1-c2)^T at alpha_* - delta.
  8. Save predictions vs measurements + relative errors to JSON.

Output: results/exp_r2_sigma_inheritance.json

References:
  THEORY/working/R2_DCR/R2_op_R2_9_sigma_inheritance.md (Lemmas B2, B3, B4)
  CODE/experiments/exp38_barrier_height.py (canonical 15x15 setup template)
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations


# ---------------------------------------------------------------------------
# Canonical 15x15 setup (matches exp38_barrier_height.py)
# ---------------------------------------------------------------------------

def make_params(beta=50.0, vol_frac=0.3):
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


# ---------------------------------------------------------------------------
# PD_0 with per-bar vertex support (custom Union-Find)
# ---------------------------------------------------------------------------

def persistence_with_supports(u, graph):
    """Compute H_0 persistence bars + per-bar vertex supports.

    Returns:
      bars: list of dicts with keys:
        - birth: birth level (u-value at component formation)
        - death: death level (u-value at merge / 0 if surviving)
        - length: birth - death
        - support: set of vertex indices in the bar's component just before merge
        - root_vertex: the local-maximum vertex that birthed this bar
    Bars sorted by length descending.
    """
    n = graph.n
    order = np.argsort(-u)  # decreasing u order

    W_coo = graph.W.tocoo()
    adj = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    root_vertex = np.full(n, -1, dtype=int)
    component_vertices = {i: {i} for i in range(n)}  # root_idx -> set of vertex indices
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
        # component_vertices[idx] already {idx}

        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            # Older component (higher birth) wins; younger dies
            if birth_val[ri] >= birth_val[rn]:
                # rn dies into ri
                dying_root = root_vertex[rn]
                bars.append({
                    "birth": float(birth_val[rn]),
                    "death": float(u[idx]),
                    "length": float(birth_val[rn] - u[idx]),
                    "support": set(component_vertices[rn]),
                    "root_vertex": int(dying_root),
                })
                # merge rn into ri
                component_vertices[ri].update(component_vertices[rn])
                component_vertices[ri].add(idx)
                del component_vertices[rn]
                parent[rn] = ri
            else:
                # ri dies into rn
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

    # Surviving component (infinite bar): take the unique remaining root
    surviving_roots = list(component_vertices.keys())
    assert len(surviving_roots) == 1, f"Expected 1 surviving root, got {len(surviving_roots)}"
    sr = surviving_roots[0]
    bars.append({
        "birth": float(np.max(u)),
        "death": 0.0,
        "length": float(np.max(u)),
        "support": set(component_vertices[sr]),
        "root_vertex": int(root_vertex[sr]),
    })

    bars.sort(key=lambda b: b["length"], reverse=True)
    return bars


# ---------------------------------------------------------------------------
# Per-bar σ-attributes (D-R2-7)
# ---------------------------------------------------------------------------

def bar_attributes(bar, u, positions):
    """Compute mass, centroid, orientation tensor of a bar.

    Arguments:
      bar: dict from persistence_with_supports, with key "support"
      u: cohesion field
      positions: array of shape (n, d) — vertex positions

    Returns:
      dict with keys: mass, centroid, orientation
    """
    support = list(bar["support"])
    if len(support) == 0:
        return {"mass": 0.0, "centroid": np.zeros(positions.shape[1]),
                "orientation": np.zeros((positions.shape[1], positions.shape[1]))}

    u_supp = u[support]
    pos_supp = positions[support]

    mass = float(np.sum(u_supp))
    if mass < 1e-12:
        return {"mass": 0.0, "centroid": pos_supp.mean(axis=0),
                "orientation": np.zeros((positions.shape[1], positions.shape[1]))}

    centroid = (u_supp[:, None] * pos_supp).sum(axis=0) / mass

    delta = pos_supp - centroid[None, :]
    orientation = (u_supp[:, None, None] * delta[:, :, None] * delta[:, None, :]).sum(axis=0)

    return {"mass": mass, "centroid": centroid, "orientation": orientation}


# ---------------------------------------------------------------------------
# Grid vertex positions
# ---------------------------------------------------------------------------

def grid_positions(rows, cols):
    """Vertex positions for grid_2d(rows, cols)."""
    return np.array([[i, j] for i in range(rows) for j in range(cols)], dtype=float)


# ---------------------------------------------------------------------------
# Merge event detection
# ---------------------------------------------------------------------------

def count_bars_above_threshold(bars, threshold):
    """Count bars with length >= threshold."""
    return sum(1 for b in bars if b["length"] >= threshold)


def find_merge_event(path_bars, threshold):
    """Find the step index at which K_read drops from 2 to 1.

    path_bars: list of bar-list-per-step
    threshold: persistence-length cutoff for K_read
    Returns (s_minus, s_plus) where s_minus is last index with K_read>=2, s_plus is first with K_read<=1.
    Returns None if no transition found.
    """
    K_vals = [count_bars_above_threshold(bars, threshold) for bars in path_bars]
    for i in range(len(K_vals) - 1):
        if K_vals[i] >= 2 and K_vals[i + 1] <= 1:
            return i, i + 1, K_vals
    return None, None, K_vals


# ---------------------------------------------------------------------------
# Predictions from Lemmas B2, B3
# ---------------------------------------------------------------------------

def predict_centroid_B2(attr1, attr2):
    """Lemma B2: mass-weighted average centroid."""
    m_tot = attr1["mass"] + attr2["mass"]
    if m_tot < 1e-12:
        return None
    return (attr1["mass"] * attr1["centroid"] + attr2["mass"] * attr2["centroid"]) / m_tot


def predict_orientation_B3(attr1, attr2):
    """Lemma B3: parallel-axis theorem."""
    m_tot = attr1["mass"] + attr2["mass"]
    if m_tot < 1e-12:
        return None
    diff = attr1["centroid"] - attr2["centroid"]
    cross_term = (attr1["mass"] * attr2["mass"] / m_tot) * np.outer(diff, diff)
    return attr1["orientation"] + attr2["orientation"] + cross_term


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_experiment(grid_rows=15, grid_cols=15, beta=50.0, vol_frac=0.3,
                   lam_rep=10.0, n_steps=51, persistence_threshold=0.05):
    """Run the OP-R2-9 numerical verification.

    Note on threshold: persistence_threshold corresponds to R-2's theta in
    K_read^theta. Canonical rho_pers may differ; we choose 0.05 as a generic
    cutoff to detect 2 bars in K=2 regime.
    """
    print(f"=== OP-R2-9 σ-Inheritance numerical verification ===")
    print(f"Grid: {grid_rows}x{grid_cols}, beta={beta}, vol_frac={vol_frac}, lam_rep={lam_rep}")
    print(f"Persistence threshold: {persistence_threshold}")
    print()

    graph = GraphState.grid_2d(grid_rows, grid_cols)
    n = graph.n
    positions = grid_positions(grid_rows, grid_cols)

    params = make_params(beta=beta, vol_frac=vol_frac)
    m_total = params.volume_fraction * n

    # ----- Step 1: find K=2 and K=1 minimizers -----
    print("[Step 1] Finding K=2 formations...")
    t0 = time.time()
    np.random.seed(42)
    result_k2 = find_k_formations(graph, params, K=2, lambda_rep=lam_rep)
    # result_k2 may be a list of FormationResult OR an object with .fields / .u_list
    if isinstance(result_k2, list):
        u_k2_fields = [r.u if hasattr(r, "u") else r for r in result_k2]
    elif hasattr(result_k2, "fields") and result_k2.fields is not None:
        u_k2_fields = result_k2.fields
    elif hasattr(result_k2, "u_list"):
        u_k2_fields = result_k2.u_list
    else:
        u_k2_fields = getattr(result_k2, "us", None)
    if u_k2_fields is None or len(u_k2_fields) < 2:
        raise RuntimeError(f"find_k_formations returned no fields: {result_k2}")

    u_k2_fields = [np.asarray(u) for u in u_k2_fields]
    u_k2_combined = np.clip(np.sum(u_k2_fields, axis=0), 0.0, 1.0)
    u_k2_combined = project_volume(u_k2_combined, m_total)
    print(f"  K=2 fields found in {time.time() - t0:.1f}s; combined mass = {u_k2_combined.sum():.2f}")

    print("[Step 2] Finding K=1 minimizer...")
    t0 = time.time()
    result_k1 = find_formation(graph, params)
    u_k1 = result_k1.u if hasattr(result_k1, "u") else result_k1
    print(f"  K=1 minimizer found in {time.time() - t0:.1f}s; mass = {u_k1.sum():.2f}")

    # ----- Step 3: construct linear path -----
    print(f"[Step 3] Constructing linear path with n_steps={n_steps}...")
    alphas = np.linspace(0.0, 1.0, n_steps)
    path_u = [project_volume((1 - a) * u_k2_combined + a * u_k1, m_total) for a in alphas]

    # ----- Step 4: compute PD_0 + per-bar attributes at each step -----
    print("[Step 4] Computing PD_0 and per-bar attributes along path...")
    path_bars = []
    path_attrs = []  # list of list of attribute dicts (per bar per step)
    for j, u in enumerate(path_u):
        bars = persistence_with_supports(u, graph)
        # Filter: only retain bars with support size >= 2 to avoid singleton-noise
        bars = [b for b in bars if len(b["support"]) >= 2]
        path_bars.append(bars)
        attrs = [bar_attributes(b, u, positions) for b in bars]
        path_attrs.append(attrs)
    print(f"  Path computed: {n_steps} steps, bar counts: {[len(b) for b in path_bars[::10]]} (every 10th)")

    # ----- Step 5: detect merge event -----
    print("[Step 5] Detecting merge event...")
    s_minus, s_plus, K_vals = find_merge_event(path_bars, persistence_threshold)
    print(f"  K_read trajectory: {K_vals}")
    if s_minus is None:
        print(f"  WARNING: No K=2 -> K=1 transition detected at threshold {persistence_threshold}.")
        print(f"  Trying different thresholds...")
        for thr in [0.01, 0.02, 0.10, 0.15, 0.20, 0.30]:
            sm, sp, kv = find_merge_event(path_bars, thr)
            if sm is not None:
                print(f"  Found transition at threshold {thr}: step {sm} -> {sp}; K_vals = {kv}")
                s_minus, s_plus = sm, sp
                persistence_threshold = thr
                break

    if s_minus is None:
        return {
            "status": "no_transition_found",
            "K_vals": K_vals,
            "alphas": alphas.tolist(),
            "bar_counts_per_step": [len(b) for b in path_bars],
        }

    print(f"  Merge event: step {s_minus} (alpha={alphas[s_minus]:.3f}) -> step {s_plus} (alpha={alphas[s_plus]:.3f})")

    # ----- Step 6: extract pre-merge and post-merge bars -----
    bars_pre = path_bars[s_minus]
    attrs_pre = path_attrs[s_minus]
    bars_post = path_bars[s_plus]
    attrs_post = path_attrs[s_plus]

    # Pre-merge: two largest bars b_1, b_2
    bar1_pre, attr1_pre = bars_pre[0], attrs_pre[0]
    bar2_pre, attr2_pre = bars_pre[1], attrs_pre[1]

    # Post-merge: the single dominant bar
    bar_post = bars_post[0]
    attr_post = attrs_post[0]

    # ----- Step 7: verify Lemma B2 (centroid) -----
    print("[Step 6] Verifying Lemma B2 (centroid)...")
    c_predicted = predict_centroid_B2(attr1_pre, attr2_pre)
    c_measured = attr_post["centroid"]
    centroid_err = np.linalg.norm(c_predicted - c_measured)
    centroid_rel = centroid_err / (np.linalg.norm(c_measured) + 1e-12)
    print(f"  Predicted centroid (B2): {c_predicted}")
    print(f"  Measured centroid:       {c_measured}")
    print(f"  Absolute error: {centroid_err:.4f}, Relative: {centroid_rel*100:.2f}%")

    # ----- Step 8: verify Lemma B3 (orientation) -----
    print("[Step 7] Verifying Lemma B3 (orientation parallel-axis)...")
    I_predicted = predict_orientation_B3(attr1_pre, attr2_pre)
    I_measured = attr_post["orientation"]
    orient_err_frob = np.linalg.norm(I_predicted - I_measured, ord='fro')
    orient_rel = orient_err_frob / (np.linalg.norm(I_measured, ord='fro') + 1e-12)
    print(f"  Predicted orientation tensor (B3):")
    print(f"    {I_predicted}")
    print(f"  Measured orientation tensor:")
    print(f"    {I_measured}")
    print(f"  Frobenius error: {orient_err_frob:.4f}, Relative: {orient_rel*100:.2f}%")

    # ----- Step 9: pack results -----
    results = {
        "status": "ok",
        "config": {
            "grid_rows": grid_rows, "grid_cols": grid_cols,
            "beta": beta, "vol_frac": vol_frac, "lam_rep": lam_rep,
            "n_steps": n_steps,
            "persistence_threshold_used": persistence_threshold,
        },
        "merge_event": {
            "s_minus": int(s_minus), "s_plus": int(s_plus),
            "alpha_minus": float(alphas[s_minus]),
            "alpha_plus": float(alphas[s_plus]),
            "K_vals_per_step": K_vals,
        },
        "lemma_B2_centroid": {
            "predicted": c_predicted.tolist(),
            "measured": c_measured.tolist(),
            "abs_error": float(centroid_err),
            "rel_error_percent": float(centroid_rel * 100),
            "pass_threshold_1pct": bool(centroid_rel < 0.01),
            "pass_threshold_5pct": bool(centroid_rel < 0.05),
        },
        "lemma_B3_orientation": {
            "predicted": I_predicted.tolist(),
            "measured": I_measured.tolist(),
            "frob_error": float(orient_err_frob),
            "rel_error_percent": float(orient_rel * 100),
            "pass_threshold_2pct": bool(orient_rel < 0.02),
            "pass_threshold_5pct": bool(orient_rel < 0.05),
        },
        "pre_merge_attrs": {
            "bar_1": {
                "mass": float(attr1_pre["mass"]),
                "centroid": attr1_pre["centroid"].tolist(),
                "support_size": len(bar1_pre["support"]),
                "bar_length": bar1_pre["length"],
            },
            "bar_2": {
                "mass": float(attr2_pre["mass"]),
                "centroid": attr2_pre["centroid"].tolist(),
                "support_size": len(bar2_pre["support"]),
                "bar_length": bar2_pre["length"],
            },
        },
        "post_merge_attrs": {
            "merged_bar": {
                "mass": float(attr_post["mass"]),
                "centroid": attr_post["centroid"].tolist(),
                "support_size": len(bar_post["support"]),
                "bar_length": bar_post["length"],
            },
        },
    }
    return results


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    results = run_experiment()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "exp_r2_sigma_inheritance.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print()
    print(f"=== Results saved to {out_path} ===")

    if results["status"] == "ok":
        print()
        print("=== SUMMARY ===")
        print(f"Lemma B2 (centroid): relative error {results['lemma_B2_centroid']['rel_error_percent']:.2f}%")
        print(f"  Pass <1%: {results['lemma_B2_centroid']['pass_threshold_1pct']}")
        print(f"  Pass <5%: {results['lemma_B2_centroid']['pass_threshold_5pct']}")
        print(f"Lemma B3 (orientation): relative error {results['lemma_B3_orientation']['rel_error_percent']:.2f}%")
        print(f"  Pass <2%: {results['lemma_B3_orientation']['pass_threshold_2pct']}")
        print(f"  Pass <5%: {results['lemma_B3_orientation']['pass_threshold_5pct']}")
