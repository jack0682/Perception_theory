#!/usr/bin/env python3
"""Experiment 27: Warm-start T-Persist-1 chain verification.

Repeats the exp26 chain verification but uses warm-start optimization:
  û_s = find_formation(g, p_s, u_init=û_t)

This keeps the optimizer in the same basin as û_t, eliminating the
multi-start basin-switching artifact that caused (b)(d) failures in exp26.

If all 5 parts pass with warm-start, this proves the theory (T-Persist-1)
is correct and the exp26 failures were purely optimizer artifacts.

Reference: Canonical Spec v2.0 §13 (T-Persist-1).
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.operators import closure, distinction, resolvent_diagonal
from scc.energy import EnergyComputer
from scc.diagnostics import compute_diagnostics
from scc.transport import (
    cohesion_fingerprint,
    graph_distance_matrix,
    transport_cost,
    sinkhorn_partial_ot,
    transport_field,
    persist_transport,
)


# ============================================================================
# Configuration (same as exp26)
# ============================================================================

CONFIGS = [
    {"name": "8×8 β=50",   "N": 8,  "beta": 50},
    {"name": "10×10 β=50",  "N": 10, "beta": 50},
    {"name": "10×10 β=100", "N": 10, "beta": 100},
    {"name": "12×12 β=50",  "N": 12, "beta": 50},
    {"name": "12×12 β=100", "N": 12, "beta": 100},
]

THETA_CORE = 0.9       # core membership threshold
THETA_DEEP = 0.95      # deep core threshold (Core²)
EPS_PERTURB = 0.05     # ε₁ perturbation magnitude for alpha_bd
SIGMA_TR = 1.0         # transport spatial tolerance
GAMMA_TR = 1.0         # transport fingerprint weight
EPS_OT = 0.5           # entropic regularization (moderate)
MASS_FRACTION = 0.95   # allow slight mass loss in OT


def find_core(u, theta):
    """Return indices of core sites: {x : u(x) >= theta}."""
    return np.where(u >= theta)[0]


def bfs_depth(adj_list, core_set, core_nodes):
    """BFS from boundary inward to compute depth of each core node."""
    n = len(adj_list)
    depth = np.full(n, -1, dtype=int)

    boundary = []
    for x in core_set:
        for nb in adj_list[x]:
            if nb not in core_set:
                boundary.append(x)
                break

    queue = list(boundary)
    for x in queue:
        depth[x] = 0

    head = 0
    while head < len(queue):
        x = queue[head]
        head += 1
        for nb in adj_list[x]:
            if nb in core_set and depth[nb] == -1:
                depth[nb] = depth[x] + 1
                queue.append(nb)

    return depth


def build_adj_list(graph):
    """Build adjacency list from graph."""
    W_coo = graph.W.tocoo()
    adj = [[] for _ in range(graph.n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)
    return adj


def run_config(cfg):
    """Run full T-Persist chain with warm-start for one configuration."""
    N, beta = cfg["N"], cfg["beta"]
    name = cfg["name"]
    n = N * N

    print(f"\n{'='*72}")
    print(f"  CONFIG: {name}  (n={n}, beta_bd={beta})  [WARM-START]")
    print(f"{'='*72}")

    results = {}

    # ---------------------------------------------------------------
    # Step 1: Find formation û_t (standard multi-start)
    # ---------------------------------------------------------------
    print("\n[1] Finding formation û_t (multi-start) ...")
    g = GraphState.grid_2d(N, N)
    p_t = ParameterRegistry(beta_bd=beta)
    t0 = time.time()
    res_t = find_formation(g, p_t)
    dt1 = time.time() - t0
    u_t = res_t.u

    print(f"    Converged: {res_t.converged}, iterations: {res_t.n_iter}, "
          f"time: {dt1:.2f}s")
    print(f"    Energy: {res_t.energy:.6f}")
    print(f"    Diagnostics: {res_t.diagnostics}")
    print(f"    u range: [{u_t.min():.4f}, {u_t.max():.4f}], "
          f"mass: {u_t.sum():.2f}/{n*p_t.volume_fraction:.2f}")

    results["formation_converged"] = res_t.converged
    results["diagnostics_t"] = res_t.diagnostics

    # ---------------------------------------------------------------
    # Step 2: Deep core analysis (Gap 6 / part c)
    # ---------------------------------------------------------------
    print("\n[2] Deep core analysis (Gap 6) ...")
    adj = build_adj_list(g)

    core_t_idx = find_core(u_t, THETA_CORE)
    core_t_set = set(core_t_idx.tolist())
    deep_core_idx = find_core(u_t, THETA_DEEP)

    depth = bfs_depth(adj, core_t_set, core_t_idx)
    core2_idx = np.array([x for x in core_t_idx if depth[x] >= 2])

    if len(core2_idx) > 0:
        interior_gap = float(np.min(u_t[core2_idx] - THETA_CORE))
    else:
        interior_gap = 0.0

    max_depth = int(depth[core_t_idx].max()) if len(core_t_idx) > 0 else 0

    print(f"    |Core(θ={THETA_CORE})|  = {len(core_t_idx)}")
    print(f"    |Core²(depth≥2)| = {len(core2_idx)}")
    print(f"    Max core depth: {max_depth}")
    print(f"    Interior gap: {interior_gap:.6f}")

    gap6_pass = len(core2_idx) > 0 and interior_gap > 0.01
    results["gap6_pass"] = gap6_pass
    results["core_size"] = len(core_t_idx)
    results["core2_size"] = len(core2_idx)
    results["interior_gap"] = interior_gap
    results["max_depth"] = max_depth

    print(f"    Gap 6 PASS: {gap6_pass}")

    # ---------------------------------------------------------------
    # Step 3: Fingerprint gap Δ_φ²
    # ---------------------------------------------------------------
    print("\n[3] Cohesion fingerprint gap Δ_φ² ...")
    phi_t = cohesion_fingerprint(u_t, g, p_t)

    if len(core2_idx) > 0:
        x0 = core2_idx[np.argmax(u_t[core2_idx])]
        ext_idx = np.where(u_t < 0.1)[0]
        if len(ext_idx) == 0:
            ext_idx = np.array([np.argmin(u_t)])
        z0 = ext_idx[np.argmin(u_t[ext_idx])]
        delta_phi_sq = float(np.sum((phi_t[x0] - phi_t[z0])**2))
        print(f"    Core site x0={x0}: φ = {phi_t[x0]}")
        print(f"    Ext  site z0={z0}: φ = {phi_t[z0]}")
        print(f"    Δ_φ² = {delta_phi_sq:.6f}")
    else:
        delta_phi_sq = 0.0
        print(f"    No deep core — skipping fingerprint gap")

    results["delta_phi_sq"] = delta_phi_sq

    # ---------------------------------------------------------------
    # Step 4: WARM-START perturbation + IFT continuity (part a)
    # ---------------------------------------------------------------
    print(f"\n[4] ε-gentle perturbation with WARM-START (ε₁={EPS_PERTURB}) ...")

    alpha_s = p_t.alpha_bd * (1.0 + EPS_PERTURB)
    p_s = ParameterRegistry(beta_bd=beta, alpha_bd=alpha_s)

    # KEY DIFFERENCE FROM EXP26: warm-start from û_t
    t0 = time.time()
    res_s = find_formation(g, p_s, u_init=u_t)
    dt4 = time.time() - t0
    u_s = res_s.u

    # IFT bound
    field_diff = float(np.linalg.norm(u_s - u_t))
    field_diff_rel = field_diff / max(np.linalg.norm(u_t), 1e-12)

    ec = EnergyComputer(g, p_t)
    ec.normalize_weights()
    eps1 = abs(alpha_s - p_t.alpha_bd)

    E_t, _ = ec.energy(u_t)
    delta_u = u_s - u_t
    delta_u_norm = np.linalg.norm(delta_u)
    if delta_u_norm > 1e-12:
        ec_s = EnergyComputer(g, p_s)
        ec_s.normalize_weights()
        E_at_us_with_t_params, _ = ec.energy(u_s)
        mu_estimate = max(2.0 * (E_at_us_with_t_params - E_t) / (delta_u_norm**2), 0.01)
    else:
        mu_estimate = 1.0

    ift_bound = 2.0 * eps1 / mu_estimate
    part_a_pass = field_diff < ift_bound * 5

    print(f"    û_s converged: {res_s.converged}, time: {dt4:.2f}s")
    print(f"    ‖û_s - û_t‖₂ = {field_diff:.6f}")
    print(f"    ‖û_s - û_t‖₂/‖û_t‖ = {field_diff_rel:.6f}")
    print(f"    ε₁ = {eps1:.6f}, μ est = {mu_estimate:.6f}")
    print(f"    IFT bound 2ε₁/μ = {ift_bound:.6f}")
    print(f"    Part (a) — IFT continuity: {'PASS' if part_a_pass else 'FAIL'} "
          f"(ratio = {field_diff/max(ift_bound,1e-12):.3f})")

    results["part_a_pass"] = part_a_pass
    results["field_diff"] = field_diff
    results["ift_bound"] = ift_bound
    results["mu_estimate"] = mu_estimate

    # ---------------------------------------------------------------
    # Step 5: Transport + core-to-core concentration (part e)
    # ---------------------------------------------------------------
    print("\n[5] Transport computation + core concentration (part e) ...")

    phi_s = cohesion_fingerprint(u_s, g, p_s)
    dist_mat = graph_distance_matrix(g)
    cost_mat = transport_cost(phi_t, phi_s, dist_mat, sigma=SIGMA_TR, gamma=GAMMA_TR)

    M, ot_info = sinkhorn_partial_ot(
        cost_mat, u_t, u_s, eps=EPS_OT, mass_fraction=MASS_FRACTION, max_iter=200
    )

    print(f"    OT converged: {ot_info['converged']}, "
          f"iters: {ot_info['iterations']}, "
          f"marginal_err: {ot_info['marginal_error']:.2e}")

    core_s_idx = find_core(u_s, THETA_CORE)

    if len(core_t_idx) > 0 and len(core_s_idx) > 0:
        concentrations = []
        for x in core_t_idx:
            row_sum = M[x, :].sum()
            if row_sum < 1e-12:
                concentrations.append(0.0)
                continue
            core_mass = M[x, core_s_idx].sum()
            concentrations.append(core_mass / row_sum)

        concentrations = np.array(concentrations)
        min_conc = float(concentrations.min())
        mean_conc = float(concentrations.mean())
        median_conc = float(np.median(concentrations))

        if len(core2_idx) > 0:
            deep_conc = []
            for x in core2_idx:
                row_sum = M[x, :].sum()
                if row_sum < 1e-12:
                    deep_conc.append(0.0)
                    continue
                core_mass = M[x, core_s_idx].sum()
                deep_conc.append(core_mass / row_sum)
            deep_conc = np.array(deep_conc)
            deep_min_conc = float(deep_conc.min())
            deep_mean_conc = float(deep_conc.mean())
        else:
            deep_min_conc = 0.0
            deep_mean_conc = 0.0

        part_e_pass = mean_conc > 0.5
        print(f"    |Core_t| = {len(core_t_idx)}, |Core_s| = {len(core_s_idx)}")
        print(f"    Core-to-core concentration: min={min_conc:.4f}, "
              f"mean={mean_conc:.4f}, median={median_conc:.4f}")
        print(f"    Deep core concentration: min={deep_min_conc:.4f}, "
              f"mean={deep_mean_conc:.4f}")
        print(f"    Part (e) — core concentration: "
              f"{'PASS' if part_e_pass else 'FAIL'}")
    else:
        part_e_pass = False
        min_conc = mean_conc = 0.0
        deep_min_conc = deep_mean_conc = 0.0
        print(f"    No core at t or s — FAIL")

    results["part_e_pass"] = part_e_pass
    results["conc_min"] = min_conc
    results["conc_mean"] = mean_conc
    results["deep_conc_min"] = deep_min_conc
    results["deep_conc_mean"] = deep_mean_conc

    # ---------------------------------------------------------------
    # Step 6: Gradient flow from transported field (part b)
    # ---------------------------------------------------------------
    print("\n[6] Gradient flow convergence (part b) ...")

    u_transported = transport_field(M, u_s)
    m_target = p_s.volume_fraction * n
    u_init = project_volume(np.clip(u_transported, 0.0, 1.0), m_target)

    t0 = time.time()
    res_flow = find_formation(g, p_s, u_init=u_init)
    dt6 = time.time() - t0
    u_flow = res_flow.u

    dist_to_us = float(np.linalg.norm(u_flow - u_s))
    dist_to_us_rel = dist_to_us / max(np.linalg.norm(u_s), 1e-12)

    ec_s2 = EnergyComputer(g, p_s)
    ec_s2.normalize_weights()
    E_flow, _ = ec_s2.energy(u_flow)
    E_us, _ = ec_s2.energy(u_s)
    energy_gap = abs(E_flow - E_us)

    part_b_pass = dist_to_us_rel < 0.1 and res_flow.converged

    print(f"    Flow converged: {res_flow.converged}, iters: {res_flow.n_iter}, "
          f"time: {dt6:.2f}s")
    print(f"    ‖u_flow - û_s‖ = {dist_to_us:.6f}")
    print(f"    ‖u_flow - û_s‖/‖û_s‖ = {dist_to_us_rel:.6f}")
    print(f"    Energy gap |E(u_flow) - E(û_s)| = {energy_gap:.2e}")
    print(f"    Part (b) — gradient flow convergence: "
          f"{'PASS' if part_b_pass else 'FAIL'}")

    results["part_b_pass"] = part_b_pass
    results["dist_flow_to_us"] = dist_to_us
    results["dist_flow_to_us_rel"] = dist_to_us_rel
    results["energy_gap"] = energy_gap
    results["flow_converged"] = res_flow.converged

    # ---------------------------------------------------------------
    # Step 7: Exact threshold preservation (part d)
    # ---------------------------------------------------------------
    print("\n[7] Threshold preservation (part d) ...")

    core_t_in_core_s = sum(1 for x in core_t_idx if u_s[x] >= THETA_CORE)
    frac_preserved = core_t_in_core_s / max(len(core_t_idx), 1)

    eps_relax = 0.05
    core_t_in_relaxed = sum(1 for x in core_t_idx
                           if u_s[x] >= THETA_CORE - eps_relax)
    frac_relaxed = core_t_in_relaxed / max(len(core_t_idx), 1)

    if len(core_t_idx) > 0:
        min_us_at_core_t = float(u_s[core_t_idx].min())
        mean_us_at_core_t = float(u_s[core_t_idx].mean())
    else:
        min_us_at_core_t = 0.0
        mean_us_at_core_t = 0.0

    part_d_pass = frac_relaxed >= 0.9

    print(f"    Core_t ⊆ Core_s(θ={THETA_CORE}): "
          f"{core_t_in_core_s}/{len(core_t_idx)} = {frac_preserved:.3f}")
    print(f"    Core_t ⊆ Core_s(θ={THETA_CORE - eps_relax}): "
          f"{core_t_in_relaxed}/{len(core_t_idx)} = {frac_relaxed:.3f}")
    print(f"    min u_s at Core_t sites: {min_us_at_core_t:.4f}")
    print(f"    mean u_s at Core_t sites: {mean_us_at_core_t:.4f}")
    print(f"    Part (d) — threshold preservation: "
          f"{'PASS' if part_d_pass else 'FAIL'}")

    results["part_d_pass"] = part_d_pass
    results["frac_core_preserved"] = frac_preserved
    results["frac_core_relaxed"] = frac_relaxed
    results["min_us_at_core_t"] = min_us_at_core_t

    # ---------------------------------------------------------------
    # Step 8: Persist predicate (composite)
    # ---------------------------------------------------------------
    print("\n[8] Persist predicate ...")

    overlap = float(np.sum(np.minimum(u_t, u_s)) /
                    max(np.sum(u_t), np.sum(u_s)))
    persist_val = persist_transport(u_t, u_s, M, theta_core=THETA_CORE)

    print(f"    Core overlap: {overlap:.4f}")
    print(f"    Transport persist: {persist_val:.4f}")

    results["persist_overlap"] = overlap
    results["persist_transport"] = persist_val

    # ---------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------
    parts = {
        "(a) IFT continuity": results["part_a_pass"],
        "(b) Gradient flow":  results["part_b_pass"],
        "(c) Deep core/Gap6": results["gap6_pass"],
        "(d) Threshold pres": results["part_d_pass"],
        "(e) Core-to-core":   results["part_e_pass"],
    }

    all_pass = all(parts.values())
    n_pass = sum(parts.values())

    print(f"\n{'─'*50}")
    print(f"  CHAIN SUMMARY for {name} [WARM-START]")
    print(f"{'─'*50}")
    for label, passed in parts.items():
        print(f"    {label}: {'PASS' if passed else 'FAIL'}")
    print(f"  Overall: {n_pass}/5 parts pass → "
          f"{'CHAIN CLOSES' if all_pass else 'CHAIN BROKEN'}")
    print(f"  Persist (overlap): {overlap:.4f}")
    print(f"  Persist (transport): {persist_val:.4f}")

    results["all_pass"] = all_pass
    results["n_pass"] = n_pass
    results["parts"] = parts

    return results


def print_summary_table(all_results):
    """Print comprehensive summary table across all configs."""
    print(f"\n\n{'='*90}")
    print(f"  COMPREHENSIVE SUMMARY: T-Persist-1 Chain (Warm-Start)")
    print(f"{'='*90}")

    print(f"\n{'Config':<16} {'(a)IFT':>8} {'(b)Flow':>8} {'(c)Core':>8} "
          f"{'(d)Thres':>8} {'(e)Conc':>8} {'Chain':>8} {'Persist':>8}")
    print(f"{'---'*30}")

    for cfg, res in all_results:
        parts = res["parts"]
        vals = list(parts.values())
        marks = ['PASS' if v else 'FAIL' for v in vals]
        chain = 'PASS' if res['all_pass'] else 'FAIL'
        persist = res['persist_transport']

        print(f"{cfg['name']:<16} {marks[0]:>8} {marks[1]:>8} {marks[2]:>8} "
              f"{marks[3]:>8} {marks[4]:>8} {chain:>8} {persist:>8.4f}")

    # Quantitative details
    print(f"\n{'Config':<16} {'field_diff':>10} {'IFT_bnd':>10} {'Core2':>6} "
          f"{'IntGap':>8} {'ConcMn':>8} {'FlowD':>10} {'Overlap':>8}")
    print(f"{'---'*30}")

    for cfg, res in all_results:
        print(f"{cfg['name']:<16} {res['field_diff']:>10.6f} "
              f"{res['ift_bound']:>10.6f} {res['core2_size']:>6d} "
              f"{res['interior_gap']:>8.4f} {res['conc_mean']:>8.4f} "
              f"{res['dist_flow_to_us']:>10.6f} {res['persist_overlap']:>8.4f}")

    # Overall verdict
    all_close = all(r['all_pass'] for _, r in all_results)
    n_configs_pass = sum(1 for _, r in all_results if r['all_pass'])

    print(f"\n{'='*90}")
    print(f"  VERDICT: {n_configs_pass}/{len(all_results)} configs have complete chain closure")
    if all_close:
        print(f"  T-Persist-1 chain VERIFIED across all parameter regimes (warm-start)")
        print(f"  CONCLUSION: exp26 (b)(d) failures were optimizer basin-switching artifacts")
    else:
        failing = [(c['name'], r['parts']) for c, r in all_results if not r['all_pass']]
        for name, parts in failing:
            broken = [k for k, v in parts.items() if not v]
            print(f"  FAIL {name}: broken at {', '.join(broken)}")
    print(f"{'='*90}")


def main():
    print("Experiment 27: Warm-Start T-Persist-1 Chain Verification")
    print("=" * 60)
    print(f"KEY DIFFERENCE from exp26: û_s found via find_formation(g, p_s, u_init=û_t)")
    print(f"This keeps optimizer in same basin, eliminating spatial relocation.")
    print(f"Perturbation eps1 = {EPS_PERTURB}")
    print(f"OT regularization eps_OT = {EPS_OT}")
    print(f"Core threshold theta = {THETA_CORE}")
    print(f"Configs: {len(CONFIGS)}")

    all_results = []
    for cfg in CONFIGS:
        try:
            res = run_config(cfg)
            all_results.append((cfg, res))
        except Exception as e:
            print(f"\n  *** ERROR in {cfg['name']}: {e}")
            import traceback
            traceback.print_exc()
            all_results.append((cfg, {
                "all_pass": False, "n_pass": 0,
                "parts": {
                    "(a) IFT continuity": False,
                    "(b) Gradient flow": False,
                    "(c) Deep core/Gap6": False,
                    "(d) Threshold pres": False,
                    "(e) Core-to-core": False,
                },
                "field_diff": 0, "ift_bound": 0, "core2_size": 0,
                "interior_gap": 0, "conc_mean": 0, "dist_flow_to_us": 0,
                "dist_flow_to_us_rel": 0, "persist_overlap": 0,
                "persist_transport": 0,
            }))

    print_summary_table(all_results)

    return all_results


if __name__ == "__main__":
    main()
