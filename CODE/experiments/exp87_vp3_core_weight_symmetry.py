"""VP-3: Core-Weight Symmetry Test for Observer Moduli Space.

Tests whether candidate λ-space transformations are genuine gauge symmetries of P_top.
Attacks OP-OMS-001: Is G_core-weight = {e} or does a non-trivial group act on Δ³?

Transformation families tested:
  A — Closure-separation swap: λ → (λ_sep, λ_cl, λ_bd, λ_tr)
  B — Closure-boundary swap: λ → (λ_bd, λ_sep, λ_cl, λ_tr)
  C — Boundary-closure compensation curve: λ_cl += δ, λ_bd -= δ, δ in grid
  D — Boundary-separation compensation: λ_sep += δ, λ_bd -= δ, δ in grid
  E — Transport ablation (static scene): λ_tr → 0, rescale others to Δ³
  F — Radial push toward simplex centroid: λ → (1-t)λ + t*(0.25,0.25,0.25,0.25)
  G — Random tangent perturbation: λ → proj_Δ³(λ + ε*v), v random unit tangent

For each pair (λ, g(λ)):
  - Δd = ||d(λ) - d(g(λ))||₂
  - ΔK = |K_core(λ) - K_core(g(λ))|
  - ΔT = topological distance (same metric as VP-1: 3|ΔK_core| + 1.5|ΔK_mid| + |Δl_sec| + |Δl_thr|)
  - ΔP_top = Δd + 0.5*ΔT (combined readout distance)

Success criterion: g is NOT a symmetry if ΔP_top > 0.05 for >50% of samples.
g is a candidate symmetry if ΔP_top < 0.05 for >90% of samples.

Scenes:
  S1: Grid 8×8 (two spatial sub-clusters)
  S2: Path graph n=30 (elongated single formation)
  S3: Grid 6×6 with central high-weight clique (structured topology)
  S4: Two disjoint cliques (K_core sensitivity test)

Output:
  results/observer_moduli/vp3_symmetry_results.json  — full data
  results/observer_moduli/vp3_symmetry_summary.md    — human-readable verdict
"""
from __future__ import annotations

import sys
import os
import json
import time
import numpy as np
from typing import NamedTuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.diagnostics import (
    diagnostic_vector, bind_predicate, sep_predicate,
    inside_predicate, persist_predicate, _persistence_h0_graph
)

RESULTS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "results", "observer_moduli"
)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Topological signature (replicated from exp86)
# ---------------------------------------------------------------------------

class TopoSig(NamedTuple):
    l_max: float
    l_second: float
    l_third: float
    artic: float
    K_core: int
    K_mid: int
    K_low: int


def _full_h0_bars(u: np.ndarray, graph: GraphState) -> list[float]:
    n = graph.n
    if n == 0:
        return []
    if n == 1:
        return [float(u[0])]

    order = np.argsort(-u)
    W_coo = graph.W.tocoo()
    adj: list[list[int]] = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    active = np.zeros(n, dtype=bool)
    finite_bars: list[float] = []

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        u_val = float(u[idx])
        active[idx] = True
        birth_val[idx] = u_val
        root_idx = idx

        for nb in adj[idx]:
            if not active[nb]:
                continue
            r_nb = find(nb)
            r_idx = find(root_idx)
            if r_nb == r_idx:
                continue
            # younger component (lower birth = smaller u = born later) dies
            if birth_val[r_nb] < birth_val[r_idx]:
                dying, surviving = r_nb, r_idx
            else:
                dying, surviving = r_idx, r_nb
            bar_len = birth_val[dying] - u_val
            if bar_len > 1e-12:
                finite_bars.append(bar_len)
            parent[dying] = surviving
            root_idx = surviving

    # infinite bar: longest-lived component
    root_final = find(order[0])
    infinite_bar = birth_val[root_final] - 0.0
    all_bars = finite_bars + [infinite_bar]
    return all_bars


def _component_count_at_threshold(u: np.ndarray, graph: GraphState,
                                   theta: float) -> int:
    n = graph.n
    active = u >= theta
    if not np.any(active):
        return 0
    W_coo = graph.W.tocoo()
    parent = np.arange(n, dtype=int)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i, j in zip(W_coo.row, W_coo.col):
        if active[i] and active[j]:
            union(i, j)

    roots = set()
    for i in range(n):
        if active[i]:
            roots.add(find(i))
    return len(roots)


def full_topo_sig(u: np.ndarray, graph: GraphState,
                   theta_core: float = 0.9,
                   theta_mid: float = 0.5,
                   theta_low: float = 0.2) -> TopoSig:
    bars = _full_h0_bars(u, graph)
    bars_sorted = sorted(bars, reverse=True)
    l_max    = bars_sorted[0] if len(bars_sorted) > 0 else 0.0
    l_second = bars_sorted[1] if len(bars_sorted) > 1 else 0.0
    l_third  = bars_sorted[2] if len(bars_sorted) > 2 else 0.0
    artic    = (1.0 - l_second / l_max) if l_max > 1e-10 else 0.0
    K_core = _component_count_at_threshold(u, graph, theta_core)
    K_mid  = _component_count_at_threshold(u, graph, theta_mid)
    K_low  = _component_count_at_threshold(u, graph, theta_low)
    return TopoSig(l_max=l_max, l_second=l_second, l_third=l_third,
                   artic=artic, K_core=K_core, K_mid=K_mid, K_low=K_low)


def topo_distance(t1: TopoSig, t2: TopoSig) -> float:
    """Same formula as VP-1 counterexample criterion."""
    return (3.0 * abs(t1.K_core - t2.K_core)
            + 1.5 * abs(t1.K_mid - t2.K_mid)
            + abs(t1.l_second - t2.l_second)
            + abs(t1.l_third - t2.l_third))


# ---------------------------------------------------------------------------
# Scene construction
# ---------------------------------------------------------------------------

def make_scene_S1() -> GraphState:
    """8×8 grid — two spatial sub-clusters (left/right half with weak bridge)."""
    g = GraphState.grid_2d(8, 8)
    # Weaken the central column edges to create two clusters
    W = g.W.tolil()
    for row in range(8):
        left_node  = row * 8 + 3
        right_node = row * 8 + 4
        if W[left_node, right_node] != 0:
            W[left_node, right_node] = 0.1
            W[right_node, left_node] = 0.1
    from scipy.sparse import csr_matrix
    W_csr = csr_matrix(W)
    import importlib
    from scc.graph import GraphState as GS
    # Rebuild with weakened adjacency
    g2 = GS(W_csr)
    return g2


def make_scene_S2() -> GraphState:
    """Path graph n=30 — elongated single formation."""
    import scipy.sparse as sp
    n = 30
    diag = np.ones(n - 1)
    W = sp.diags([diag, diag], [-1, 1], shape=(n, n), format="csr")
    return GraphState(W)


def make_scene_S3() -> GraphState:
    """6×6 grid — structured topology."""
    return GraphState.grid_2d(6, 6)


def make_scene_S4_two_cliques() -> GraphState:
    """Two disjoint 5-cliques connected by a single weak bridge edge."""
    import scipy.sparse as sp
    n = 10
    # Build adjacency matrix
    rows, cols, data = [], [], []
    # Clique 1: nodes 0-4
    for i in range(5):
        for j in range(5):
            if i != j:
                rows.append(i); cols.append(j); data.append(1.0)
    # Clique 2: nodes 5-9
    for i in range(5, 10):
        for j in range(5, 10):
            if i != j:
                rows.append(i); cols.append(j); data.append(1.0)
    # Bridge: node 4 — node 5 (weak)
    rows.extend([4, 5]); cols.extend([5, 4]); data.extend([0.05, 0.05])
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


SCENES = {
    "S1_grid8x8_bicluster": None,  # filled lazily
    "S2_path30": None,
    "S3_grid6x6": None,
    "S4_two_cliques": None,
}


def load_scenes() -> dict:
    return {
        "S1_grid8x8_bicluster": make_scene_S1(),
        "S2_path30": make_scene_S2(),
        "S3_grid6x6": make_scene_S3(),
        "S4_two_cliques": make_scene_S4_two_cliques(),
    }


# ---------------------------------------------------------------------------
# Lambda sampling
# ---------------------------------------------------------------------------

def sample_lambda_grid(n_per_dim: int = 4) -> list[np.ndarray]:
    """Sample λ ∈ Δ³ on a coarse grid plus extreme corners for discrimination."""
    lambdas = []
    # Lattice interior samples
    vals = np.linspace(0.05, 0.80, n_per_dim)
    for a in vals:
        for b in vals:
            for c in vals:
                d_val = 1.0 - a - b - c
                if 0.04 <= d_val <= 0.90:
                    lam = np.array([a, b, c, d_val])
                    lambdas.append(lam)
    # Extreme corner samples (one weight dominates) — critical for discrimination
    extremes = [
        np.array([0.85, 0.05, 0.05, 0.05]),  # closure-dominant
        np.array([0.05, 0.85, 0.05, 0.05]),  # separation-dominant
        np.array([0.05, 0.05, 0.85, 0.05]),  # boundary-dominant
        np.array([0.05, 0.05, 0.05, 0.85]),  # transport-dominant
        np.array([0.45, 0.45, 0.05, 0.05]),  # cl+sep balanced
        np.array([0.45, 0.05, 0.45, 0.05]),  # cl+bd balanced
        np.array([0.05, 0.45, 0.45, 0.05]),  # sep+bd balanced
        np.array([0.33, 0.33, 0.33, 0.01]),  # three-way balanced
    ]
    lambdas.extend(extremes)
    return lambdas


def project_simplex(v: np.ndarray) -> np.ndarray:
    """Project v onto Δ³ (non-negative, sums to 1)."""
    v = np.maximum(v, 0.0)
    s = v.sum()
    if s < 1e-12:
        return np.full(4, 0.25)
    return v / s


# ---------------------------------------------------------------------------
# Transformation families
# ---------------------------------------------------------------------------

def transform_A_cl_sep_swap(lam: np.ndarray) -> np.ndarray:
    """A: Swap λ_cl and λ_sep."""
    r = lam.copy()
    r[0], r[1] = lam[1], lam[0]
    return r


def transform_B_cl_bd_swap(lam: np.ndarray) -> np.ndarray:
    """B: Swap λ_cl and λ_bd."""
    r = lam.copy()
    r[0], r[2] = lam[2], lam[0]
    return r


def transform_C_bd_cl_compensation(lam: np.ndarray, delta: float) -> np.ndarray:
    """C: λ_cl += δ, λ_bd -= δ (boundary-closure compensation)."""
    r = lam.copy()
    r[0] = lam[0] + delta
    r[2] = lam[2] - delta
    return project_simplex(r)


def transform_D_bd_sep_compensation(lam: np.ndarray, delta: float) -> np.ndarray:
    """D: λ_sep += δ, λ_bd -= δ (boundary-separation compensation)."""
    r = lam.copy()
    r[1] = lam[1] + delta
    r[2] = lam[2] - delta
    return project_simplex(r)


def transform_E_transport_ablation(lam: np.ndarray) -> np.ndarray:
    """E: Set λ_tr = 0, rescale other components to Δ³."""
    r = lam.copy()
    r[3] = 0.0
    return project_simplex(r)


def transform_F_radial_centroid(lam: np.ndarray, t: float) -> np.ndarray:
    """F: Push λ toward simplex centroid (1/4,1/4,1/4,1/4)."""
    centroid = np.full(4, 0.25)
    return (1.0 - t) * lam + t * centroid


def transform_G_random_tangent(lam: np.ndarray, epsilon: float,
                                rng: np.random.Generator) -> np.ndarray:
    """G: Add random tangent perturbation projected back to Δ³."""
    v = rng.standard_normal(4)
    v = v - v.mean()  # project to tangent plane of Δ³
    v = v / (np.linalg.norm(v) + 1e-12)
    return project_simplex(lam + epsilon * v)


# ---------------------------------------------------------------------------
# Core measurement
# ---------------------------------------------------------------------------

def run_optimizer_for_lambda(graph: GraphState, lam: np.ndarray,
                              volume_fraction: float = 0.3) -> tuple[np.ndarray, dict]:
    """Run SCC optimizer for given λ ∈ Δ³ and return (u*, diagnostics)."""
    params = ParameterRegistry()
    # Energy weights: w_cl/w_sep/w_bd/w_tr are the correct ParameterRegistry attributes.
    # λ ∈ Δ³ maps directly to these weights (normalization happens inside EnergyComputer).
    params.w_cl  = float(lam[0])
    params.w_sep = float(lam[1])
    params.w_bd  = float(lam[2])
    params.w_tr  = float(lam[3])
    params.volume_fraction = volume_fraction

    try:
        result = find_formation(graph, params)
        u_star = result.u
        d = diagnostic_vector(u_star, graph, params)
        return u_star, {
            "bind": float(d.bind),
            "sep": float(d.sep),
            "inside": float(d.inside),
            "persist": float(d.persist),
        }
    except Exception as e:
        n = graph.n
        u_star = np.full(n, volume_fraction)
        return u_star, {"bind": 0.0, "sep": 0.0, "inside": 0.0, "persist": 0.0,
                        "error": str(e)}


def measure_pair(graph: GraphState, lam_A: np.ndarray,
                 lam_B: np.ndarray, volume_fraction: float = 0.3) -> dict:
    """Measure all distances between readouts of λ_A and λ_B on given scene."""
    u_A, d_A = run_optimizer_for_lambda(graph, lam_A, volume_fraction)
    u_B, d_B = run_optimizer_for_lambda(graph, lam_B, volume_fraction)

    t_A = full_topo_sig(u_A, graph)
    t_B = full_topo_sig(u_B, graph)

    d_A_vec = np.array([d_A["bind"], d_A["sep"], d_A["inside"], d_A["persist"]])
    d_B_vec = np.array([d_B["bind"], d_B["sep"], d_B["inside"], d_B["persist"]])
    delta_d  = float(np.linalg.norm(d_A_vec - d_B_vec))
    delta_T  = float(topo_distance(t_A, t_B))
    delta_P  = float(delta_d + 0.5 * delta_T)
    delta_K  = int(abs(t_A.K_core - t_B.K_core))

    return {
        "lam_A": lam_A.tolist(),
        "lam_B": lam_B.tolist(),
        "d_A": d_A,
        "d_B": d_B,
        "topo_A": {"K_core": int(t_A.K_core), "K_mid": int(t_A.K_mid),
                   "l_max": float(t_A.l_max), "l_second": float(t_A.l_second),
                   "l_third": float(t_A.l_third)},
        "topo_B": {"K_core": int(t_B.K_core), "K_mid": int(t_B.K_mid),
                   "l_max": float(t_B.l_max), "l_second": float(t_B.l_second),
                   "l_third": float(t_B.l_third)},
        "delta_d": delta_d,
        "delta_T": delta_T,
        "delta_P_top": delta_P,
        "delta_K_core": delta_K,
        "is_asymmetric": bool(delta_P > 0.05),
        "K_core_changed": bool(delta_K > 0),
    }


# ---------------------------------------------------------------------------
# Transformation test runners
# ---------------------------------------------------------------------------

def test_transformation_A(scenes: dict, lambdas: list, vf: float = 0.3) -> dict:
    """Test A: Closure-separation swap."""
    print("  [A] Closure-separation swap ...")
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas:
            if abs(lam[0] - lam[1]) < 0.02:
                continue  # skip near-symmetric points
            lam_B = transform_A_cl_sep_swap(lam)
            rec = measure_pair(graph, lam, lam_B, vf)
            rec["scene"] = scene_name
            rec["transform"] = "A_cl_sep_swap"
            records.append(rec)
    return _summarize_records(records, "A: Closure-Separation Swap")


def test_transformation_B(scenes: dict, lambdas: list, vf: float = 0.3) -> dict:
    print("  [B] Closure-boundary swap ...")
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas:
            if abs(lam[0] - lam[2]) < 0.02:
                continue
            lam_B = transform_B_cl_bd_swap(lam)
            rec = measure_pair(graph, lam, lam_B, vf)
            rec["scene"] = scene_name
            rec["transform"] = "B_cl_bd_swap"
            records.append(rec)
    return _summarize_records(records, "B: Closure-Boundary Swap")


def test_transformation_C(scenes: dict, lambdas: list, vf: float = 0.3) -> dict:
    print("  [C] Boundary-closure compensation ...")
    deltas = [0.05, 0.10, 0.15]
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas:
            for delta in deltas:
                if lam[2] < delta + 0.02:
                    continue
                if lam[0] + delta > 0.95:
                    continue
                lam_B = transform_C_bd_cl_compensation(lam, delta)
                rec = measure_pair(graph, lam, lam_B, vf)
                rec["scene"] = scene_name
                rec["transform"] = f"C_bd_cl_comp_d{delta:.2f}"
                rec["delta_param"] = float(delta)
                records.append(rec)
    return _summarize_records(records, "C: Boundary-Closure Compensation")


def test_transformation_D(scenes: dict, lambdas: list, vf: float = 0.3) -> dict:
    print("  [D] Boundary-separation compensation ...")
    deltas = [0.05, 0.10, 0.15]
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas:
            for delta in deltas:
                if lam[2] < delta + 0.02:
                    continue
                if lam[1] + delta > 0.95:
                    continue
                lam_B = transform_D_bd_sep_compensation(lam, delta)
                rec = measure_pair(graph, lam, lam_B, vf)
                rec["scene"] = scene_name
                rec["transform"] = f"D_bd_sep_comp_d{delta:.2f}"
                rec["delta_param"] = float(delta)
                records.append(rec)
    return _summarize_records(records, "D: Boundary-Separation Compensation")


def test_transformation_E(scenes: dict, lambdas: list, vf: float = 0.3) -> dict:
    print("  [E] Transport ablation (static scene) ...")
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas:
            if lam[3] < 0.03:
                continue
            lam_B = transform_E_transport_ablation(lam)
            rec = measure_pair(graph, lam, lam_B, vf)
            rec["scene"] = scene_name
            rec["transform"] = "E_transport_ablation"
            records.append(rec)
    return _summarize_records(records, "E: Transport Ablation (Static)")


def test_transformation_F(scenes: dict, lambdas: list, vf: float = 0.3) -> dict:
    print("  [F] Radial push toward centroid ...")
    t_vals = [0.1, 0.2, 0.3]
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas:
            for t in t_vals:
                lam_B = transform_F_radial_centroid(lam, t)
                rec = measure_pair(graph, lam, lam_B, vf)
                rec["scene"] = scene_name
                rec["transform"] = f"F_radial_t{t:.1f}"
                rec["t_param"] = float(t)
                records.append(rec)
    return _summarize_records(records, "F: Radial Toward Centroid")


def test_transformation_G(scenes: dict, lambdas: list, vf: float = 0.3,
                           n_random: int = 3, epsilon: float = 0.08) -> dict:
    print("  [G] Random tangent perturbation ...")
    rng = np.random.default_rng(seed=42)
    records = []
    for scene_name, graph in scenes.items():
        for lam in lambdas[:15]:
            for _ in range(n_random):
                lam_B = transform_G_random_tangent(lam, epsilon, rng)
                rec = measure_pair(graph, lam, lam_B, vf)
                rec["scene"] = scene_name
                rec["transform"] = f"G_random_eps{epsilon:.2f}"
                rec["epsilon"] = float(epsilon)
                records.append(rec)
    return _summarize_records(records, "G: Random Tangent Perturbation")


def _summarize_records(records: list[dict], name: str) -> dict:
    if not records:
        return {"name": name, "n_pairs": 0, "verdict": "NO_DATA"}

    n = len(records)
    n_asymmetric = sum(1 for r in records if r["is_asymmetric"])
    n_K_changed  = sum(1 for r in records if r["K_core_changed"])
    frac_asym = n_asymmetric / n
    frac_K    = n_K_changed / n

    delta_Ps = [r["delta_P_top"] for r in records]
    delta_ds = [r["delta_d"]     for r in records]
    delta_Ts = [r["delta_T"]     for r in records]

    if frac_asym > 0.50:
        verdict = "NOT_A_SYMMETRY"
    elif frac_asym < 0.10:
        verdict = "CANDIDATE_SYMMETRY"
    else:
        verdict = "PARTIAL_SYMMETRY"

    return {
        "name": name,
        "n_pairs": n,
        "n_asymmetric": n_asymmetric,
        "frac_asymmetric": round(frac_asym, 3),
        "n_K_core_changed": n_K_changed,
        "frac_K_core_changed": round(frac_K, 3),
        "delta_P_top_mean": round(float(np.mean(delta_Ps)), 4),
        "delta_P_top_max":  round(float(np.max(delta_Ps)), 4),
        "delta_d_mean": round(float(np.mean(delta_ds)), 4),
        "delta_T_mean": round(float(np.mean(delta_Ts)), 4),
        "verdict": verdict,
        "records": records,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print("=== VP-3: Core-Weight Symmetry Test ===")
    print("Loading scenes ...")
    scenes = load_scenes()
    print(f"  Loaded {len(scenes)} scenes: {list(scenes.keys())}")

    lambdas = sample_lambda_grid(n_per_dim=4)
    print(f"  Lambda samples: {len(lambdas)}")

    # volume_fraction = 0.3 (default: 30% of nodes in formation mass)
    vf = 0.3

    all_results = {}

    print("\nRunning transformation family A ...")
    all_results["A"] = test_transformation_A(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['A']['verdict']} | "
          f"frac_asymmetric={all_results['A']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['A']['delta_P_top_mean']:.4f}")

    print("\nRunning transformation family B ...")
    all_results["B"] = test_transformation_B(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['B']['verdict']} | "
          f"frac_asymmetric={all_results['B']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['B']['delta_P_top_mean']:.4f}")

    print("\nRunning transformation family C ...")
    all_results["C"] = test_transformation_C(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['C']['verdict']} | "
          f"frac_asymmetric={all_results['C']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['C']['delta_P_top_mean']:.4f}")

    print("\nRunning transformation family D ...")
    all_results["D"] = test_transformation_D(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['D']['verdict']} | "
          f"frac_asymmetric={all_results['D']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['D']['delta_P_top_mean']:.4f}")

    print("\nRunning transformation family E (transport ablation) ...")
    all_results["E"] = test_transformation_E(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['E']['verdict']} | "
          f"frac_asymmetric={all_results['E']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['E']['delta_P_top_mean']:.4f}")

    print("\nRunning transformation family F (radial) ...")
    all_results["F"] = test_transformation_F(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['F']['verdict']} | "
          f"frac_asymmetric={all_results['F']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['F']['delta_P_top_mean']:.4f}")

    print("\nRunning transformation family G (random tangent) ...")
    all_results["G"] = test_transformation_G(scenes, lambdas, vf)
    print(f"  Verdict: {all_results['G']['verdict']} | "
          f"frac_asymmetric={all_results['G']['frac_asymmetric']:.3f} | "
          f"ΔP_top_mean={all_results['G']['delta_P_top_mean']:.4f}")

    elapsed = time.time() - t0
    print(f"\nTotal elapsed: {elapsed:.1f}s")

    # ----- Summary table -----
    print("\n=== VP-3 SUMMARY ===")
    print(f"{'Transform':<10} {'Verdict':<22} {'N_pairs':>7} "
          f"{'frac_asym':>10} {'ΔP_mean':>8} {'ΔK_frac':>8}")
    print("-" * 75)
    for key, res in all_results.items():
        print(f"{key:<10} {res['verdict']:<22} {res['n_pairs']:>7} "
              f"{res['frac_asymmetric']:>10.3f} {res['delta_P_top_mean']:>8.4f} "
              f"{res['frac_K_core_changed']:>8.3f}")

    # ----- OP-OMS-001 Classification -----
    print("\n=== OP-OMS-001 CLASSIFICATION ===")
    not_sym = [k for k, r in all_results.items() if r["verdict"] == "NOT_A_SYMMETRY"]
    candidate = [k for k, r in all_results.items() if r["verdict"] == "CANDIDATE_SYMMETRY"]
    partial = [k for k, r in all_results.items() if r["verdict"] == "PARTIAL_SYMMETRY"]
    print(f"  NOT_A_SYMMETRY (confirmed asymmetric): {not_sym}")
    print(f"  CANDIDATE_SYMMETRY (possible gauge direction): {candidate}")
    print(f"  PARTIAL_SYMMETRY (scene-dependent): {partial}")

    if candidate or partial:
        print("\n  => G_cw may be non-trivial — investigate candidate symmetries further.")
        op_status = "PARTIALLY_RESOLVED"
    else:
        print("\n  => All tested transformations are NOT symmetries of P_top.")
        print("     G_core-weight = {e} default is COMPUTATIONALLY SUPPORTED.")
        op_status = "COMPUTATIONALLY_SUPPORTED_DEFAULT"

    # ----- Save JSON -----
    output = {
        "experiment": "VP-3 Core-Weight Symmetry Test",
        "date": "2026-05-08",
        "op_attacks": "OP-OMS-001",
        "total_elapsed_s": round(elapsed, 1),
        "op_oms_001_classification": op_status,
        "transformation_results": {
            k: {kk: vv for kk, vv in v.items() if kk != "records"}
            for k, v in all_results.items()
        },
        "detailed_records": {k: v.get("records", []) for k, v in all_results.items()},
    }

    json_path = os.path.join(RESULTS_DIR, "vp3_symmetry_results.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {json_path}")

    # ----- Save Markdown Summary -----
    md_lines = [
        "# VP-3 Symmetry Test Summary",
        "",
        f"**Date:** 2026-05-08  ",
        f"**Experiment:** exp87_vp3_core_weight_symmetry.py  ",
        f"**Attacks:** OP-OMS-001 (core-weight gauge group)  ",
        f"**Elapsed:** {elapsed:.1f}s  ",
        "",
        "## Verdict Table",
        "",
        "| Transform | Description | Verdict | frac_asym | ΔP_top_mean | ΔK_frac |",
        "|---|---|---|---|---|---|",
    ]
    desc_map = {
        "A": "Closure-separation swap",
        "B": "Closure-boundary swap",
        "C": "Boundary-closure compensation",
        "D": "Boundary-separation compensation",
        "E": "Transport ablation (static)",
        "F": "Radial toward centroid",
        "G": "Random tangent perturbation",
    }
    for k, res in all_results.items():
        md_lines.append(
            f"| {k} | {desc_map[k]} | **{res['verdict']}** | "
            f"{res['frac_asymmetric']:.3f} | {res['delta_P_top_mean']:.4f} | "
            f"{res['frac_K_core_changed']:.3f} |"
        )

    md_lines += [
        "",
        f"## OP-OMS-001 Classification",
        "",
        f"**Status:** {op_status}",
        "",
    ]
    if not_sym:
        md_lines.append(f"**Confirmed NOT symmetries:** {', '.join(not_sym)}")
    if candidate:
        md_lines.append(f"**Candidate symmetries (need further investigation):** {', '.join(candidate)}")
    if partial:
        md_lines.append(f"**Partial/scene-dependent:** {', '.join(partial)}")

    md_lines += [
        "",
        "## Interpretation",
        "",
        ("All tested λ-space transformations produce measurably different P_top readouts "
         "on at least half the test cases — confirming that no nontrivial gauge direction "
         "has been found on Δ³ for P_top." if not candidate and not partial else
         "Some candidate symmetries require further investigation."),
        "",
        "**Prop CW3 (Conservative default G_cw={e}) is COMPUTATIONALLY SUPPORTED.**"
        if op_status == "COMPUTATIONALLY_SUPPORTED_DEFAULT" else
        "**G_cw may be non-trivial — further investigation needed.**",
    ]

    md_path = os.path.join(RESULTS_DIR, "vp3_symmetry_summary.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))
    print(f"Summary saved: {md_path}")

    return output


if __name__ == "__main__":
    main()
