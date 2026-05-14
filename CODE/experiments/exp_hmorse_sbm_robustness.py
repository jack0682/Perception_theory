"""exp_hmorse_sbm_robustness.py

OP-HMORSE-SBM numerical robustness extension (CV-1.17 candidate).

Extends `exp_hmorse_broadness_full_spectrum.py` methodology beyond canonical
2D grids to three heterogeneous graph classes:

  1. SBM (Stochastic Block Model): 2 planted communities, asymmetric inter/intra
     edge probabilities. Tests whether L-HMORSE-LOCAL Cat B holds on graphs
     where community structure creates strong off-diagonal block coupling.
  2. Barbell graph: 2 cliques connected by a bridge path. Tests near-disconnected
     regime where d_min/d_max ratio is extreme.
  3. Small-world (Watts-Strogatz): ring lattice with random rewiring. Tests
     long-range edge effects on Hessian spectrum.

For each graph: asymmetric edge weight perturbation (breaks Aut(G), satisfies
D-HMORSE-LOCAL (C4)); find_formation to symmetry-broken minimizer; projected
Hessian via FD on gradient; eigendecomposition; verify mu_min > 0 and
L-CLOSURE-LIFT prediction.

Output: CODE/experiments/results/exp_hmorse_sbm_robustness.{json,md}.

References:
  - CV-1.16 L-HMORSE-LOCAL Cat B unconditional (canonical §13 Cat B)
  - exp_hmorse_broadness_full_spectrum.py (canonical 2D grid sweep)
  - THEORY/logs/daily/2026-05-14/03_integration_and_new_open.md §2.2 OP-HMORSE-SBM
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Dict, List

import numpy as np
import scipy.sparse as sp
import networkx as nx

# allow running from anywhere
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer, grad_bd, grad_cl, grad_sep, double_well_second_deriv
from scc.operators import closure
from scc.optimizer import find_formation


# ---------------------------------------------------------------------------
# Graph builders
# ---------------------------------------------------------------------------

def _to_graphstate_from_nx(G_nx: nx.Graph, perturb: float, seed: int) -> GraphState:
    """Convert networkx graph to GraphState with asymmetric edge weights."""
    rng = np.random.RandomState(seed + 1)
    n = G_nx.number_of_nodes()
    row_idx, col_idx, data = [], [], []
    # Ensure deterministic node ordering
    nodes = sorted(G_nx.nodes())
    node_to_idx = {v: i for i, v in enumerate(nodes)}
    for u, v in G_nx.edges():
        i, j = node_to_idx[u], node_to_idx[v]
        if i == j:  # skip self-loops if any
            continue
        w = 1.0 + perturb * rng.rand()
        row_idx.extend([i, j])
        col_idx.extend([j, i])
        data.extend([w, w])
    adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
    return GraphState(adj)


def make_sbm(n_per_block: int, p_intra: float, p_inter: float,
             seed: int, perturb: float = 0.1) -> GraphState:
    """SBM with 2 blocks. ~n_per_block nodes per block; ensure connectivity."""
    G_nx = nx.stochastic_block_model(
        [n_per_block, n_per_block],
        [[p_intra, p_inter], [p_inter, p_intra]],
        seed=seed,
    )
    # ensure connectivity by adding a bridge if needed
    if not nx.is_connected(G_nx):
        # add edges between disconnected components
        comps = list(nx.connected_components(G_nx))
        for c1, c2 in zip(comps[:-1], comps[1:]):
            G_nx.add_edge(min(c1), min(c2))
    return _to_graphstate_from_nx(G_nx, perturb, seed)


def make_barbell(clique_size: int, bridge_len: int,
                 seed: int, perturb: float = 0.1) -> GraphState:
    """Barbell: two cliques of clique_size connected by a path of bridge_len."""
    G_nx = nx.barbell_graph(clique_size, bridge_len)
    return _to_graphstate_from_nx(G_nx, perturb, seed)


def make_smallworld(n: int, k: int, p_rewire: float,
                    seed: int, perturb: float = 0.1) -> GraphState:
    """Watts-Strogatz small-world. n nodes, k nearest neighbors, p_rewire."""
    G_nx = nx.watts_strogatz_graph(n, k, p_rewire, seed=seed)
    return _to_graphstate_from_nx(G_nx, perturb, seed)


# ---------------------------------------------------------------------------
# Hessian + helper utilities (copied/adapted from exp_hmorse_broadness)
# ---------------------------------------------------------------------------

def projected_hessian_fd(ec: EnergyComputer, u: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Pi_T H_E(u) Pi_T via finite differences."""
    n = len(u)
    g0 = ec.gradient(u)
    H = np.zeros((n, n), dtype=np.float64)
    for j in range(n):
        u_perturb = u.copy()
        u_perturb[j] += h
        g1 = ec.gradient(u_perturb)
        H[:, j] = (g1 - g0) / h
    H = 0.5 * (H + H.T)
    row_mean = H.mean(axis=0, keepdims=True)
    col_mean = H.mean(axis=1, keepdims=True)
    total_mean = H.mean()
    return H - row_mean - col_mean + total_mean


def graph_degree_stats(graph: GraphState) -> Dict[str, float]:
    deg = graph.degree
    return {
        "d_min": float(np.min(deg)),
        "d_max": float(np.max(deg)),
        "d_mean": float(np.mean(deg)),
        "d_ratio": float(np.min(deg) / np.max(deg)),
    }


def L_closure_lift_prediction(lambda_cl: float, a_cl: float, d_ratio: float) -> float:
    return 2.0 * lambda_cl * (1.0 - a_cl / 4.0) ** 2 * d_ratio


# ---------------------------------------------------------------------------
# Single-config runner
# ---------------------------------------------------------------------------

def run_one_config(
    graph_label: str,
    graph: GraphState,
    beta: float,
    a_cl: float = 3.5,
    alpha_bd: float = 1.0,
    c_volume: float = 0.2,
) -> Dict:
    """Build params, optimize, compute Hessian, verify PASS criteria."""
    t_start = time.time()
    deg_stats = graph_degree_stats(graph)
    n = graph.n

    params = ParameterRegistry(
        a_cl=a_cl,
        eta_cl=0.5,
        tau_cl=0.5,
        alpha_bd=alpha_bd,
        beta_bd=beta,
        volume_fraction=c_volume,
    )

    try:
        result = find_formation(
            graph, params, normalize=True, verbose=False,
            allow_outside_spinodal=True,  # SBM/barbell may push outside
        )
        u_star = result.u
        converged = result.converged
    except Exception as e:
        return {
            "graph": graph_label,
            "n_nodes": n,
            "beta": beta,
            "error": str(e),
            "PASS": False,
        }

    u_min, u_max = float(u_star.min()), float(u_star.max())

    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    H_proj = projected_hessian_fd(ec, u_star, h=1e-5)
    eigvals_full = np.sort(np.linalg.eigvalsh(H_proj))
    mu_min_full = float(eigvals_full[1])  # excl volume Goldstone

    # H_cl component spectrum
    H_cl_proj = projected_hessian_fd_component(
        lambda u_: grad_cl(u_, graph, params), u_star, h=1e-5
    )
    eig_cl = np.sort(np.linalg.eigvalsh(H_cl_proj))
    mu_min_H_cl = float(eig_cl[1])

    # closure residual
    cl_u = closure(u_star, graph, params)
    residual = cl_u - u_star
    r_inf, r_2 = float(np.linalg.norm(residual, ord=np.inf)), float(np.linalg.norm(residual, ord=2))

    pred_lcl = L_closure_lift_prediction(
        lambda_cl=ec.lambda_cl, a_cl=a_cl, d_ratio=deg_stats["d_ratio"]
    )

    broadness_PASS = mu_min_full > 0
    lift_PASS = mu_min_H_cl >= 0.9 * pred_lcl

    elapsed = time.time() - t_start

    return {
        "graph": graph_label,
        "n_nodes": n,
        "beta": beta,
        "graph_d_min": deg_stats["d_min"],
        "graph_d_max": deg_stats["d_max"],
        "graph_d_mean": deg_stats["d_mean"],
        "graph_d_ratio": deg_stats["d_ratio"],
        "graph_fiedler": float(graph.fiedler),
        "lambda_cl_norm": float(ec.lambda_cl),
        "u_min": u_min,
        "u_max": u_max,
        "is_interior": (u_min > 1e-6 and u_max < 1.0 - 1e-6),
        "converged": converged,
        "closure_residual_inf": r_inf,
        "closure_residual_2": r_2,
        "mu_min_full_excl_goldstone": mu_min_full,
        "mu_min_H_cl_excl_goldstone": mu_min_H_cl,
        "eig_full_min5": [float(v) for v in eigvals_full[:5]],
        "predicted_closure_lift": pred_lcl,
        "broadness_PASS": bool(broadness_PASS),
        "lift_PASS": bool(lift_PASS),
        "elapsed_sec": elapsed,
        "PASS": bool(broadness_PASS),
    }


def projected_hessian_fd_component(grad_fn, u: np.ndarray, h: float = 1e-5) -> np.ndarray:
    n = len(u)
    g0 = grad_fn(u)
    H = np.zeros((n, n), dtype=np.float64)
    for j in range(n):
        u_perturb = u.copy()
        u_perturb[j] += h
        g1 = grad_fn(u_perturb)
        H[:, j] = (g1 - g0) / h
    H = 0.5 * (H + H.T)
    row_mean = H.mean(axis=0, keepdims=True)
    col_mean = H.mean(axis=1, keepdims=True)
    total_mean = H.mean()
    return H - row_mean - col_mean + total_mean


# ---------------------------------------------------------------------------
# Main sweep
# ---------------------------------------------------------------------------

def run_sweep() -> Dict:
    beta_values = [10.0, 30.0, 100.0]
    results = {
        "metadata": {
            "experiment": "OP-HMORSE-SBM numerical robustness extension",
            "date": "2026-05-14",
            "session": "W7-Day5 extension (post CV-1.16 SEAL)",
            "graph_classes": ["SBM", "barbell", "small-world (Watts-Strogatz)"],
            "beta_values": beta_values,
            "canonical_params": {
                "a_cl": 3.5,
                "eta_cl": 0.5,
                "tau_cl": 0.5,
                "alpha_bd": 1.0,
                "volume_fraction": 0.2,
                "asym_perturb": 0.1,
            },
            "rationale": (
                "Verify L-HMORSE-LOCAL Cat B holds beyond canonical 2D grids. "
                "SBM tests community-coupled regime; barbell tests near-disconnected "
                "(extreme d_min/d_max); small-world tests long-range edge effects."
            ),
        },
        "runs": [],
    }

    # SBM configs
    sbm_configs = [
        ("SBM_n40_p_intra0.3_inter0.05", make_sbm(20, 0.3, 0.05, seed=42)),
        ("SBM_n60_p_intra0.4_inter0.05", make_sbm(30, 0.4, 0.05, seed=43)),
    ]
    # Barbell configs
    barbell_configs = [
        ("barbell_8_4", make_barbell(8, 4, seed=44)),
        ("barbell_12_6", make_barbell(12, 6, seed=45)),
    ]
    # Small-world configs
    smallworld_configs = [
        ("WS_n40_k4_p0.1", make_smallworld(40, 4, 0.1, seed=46)),
        ("WS_n60_k6_p0.2", make_smallworld(60, 6, 0.2, seed=47)),
    ]

    all_configs = sbm_configs + barbell_configs + smallworld_configs

    for label, graph in all_configs:
        print(f"\n{'='*60}\n{label} (n={graph.n}, fiedler={graph.fiedler:.4f})\n{'='*60}")
        for beta in beta_values:
            run = run_one_config(label, graph, beta)
            results["runs"].append(run)
            if "error" in run:
                print(f"  beta={beta:6.1f}: ERROR — {run['error']}")
            else:
                print(
                    f"  beta={beta:6.1f}: u=[{run['u_min']:.3f},{run['u_max']:.3f}] "
                    f"d_ratio={run['graph_d_ratio']:.3f} "
                    f"||r||_2={run['closure_residual_2']:.3f} "
                    f"mu_min(full)={run['mu_min_full_excl_goldstone']:+.4e} "
                    f"mu_min(H_cl)={run['mu_min_H_cl_excl_goldstone']:+.4e} "
                    f"pred(lcl)={run['predicted_closure_lift']:.3e} "
                    f"broad={'PASS' if run['broadness_PASS'] else 'FAIL'} "
                    f"lift={'PASS' if run['lift_PASS'] else 'FAIL'} "
                    f"[{run['elapsed_sec']:.1f}s]"
                )

    n_runs = len(results["runs"])
    bp = sum(r.get("broadness_PASS", False) for r in results["runs"])
    lp = sum(r.get("lift_PASS", False) for r in results["runs"])
    err = sum(1 for r in results["runs"] if "error" in r)
    results["summary"] = {
        "n_runs_total": n_runs,
        "n_errors": err,
        "broadness_PASS_count": bp,
        "broadness_PASS_rate": bp / max(n_runs, 1),
        "lift_PASS_count": lp,
        "lift_PASS_rate": lp / max(n_runs, 1),
        "overall_verdict": (
            "ALL PASS"
            if bp == n_runs and lp == n_runs and err == 0
            else f"{bp}/{n_runs} broadness; {lp}/{n_runs} lift; {err} errors"
        ),
    }
    return results


def write_markdown_summary(results: Dict, md_path: Path) -> None:
    lines = [
        "# exp_hmorse_sbm_robustness — Results Summary",
        "",
        f"**Experiment:** {results['metadata']['experiment']}",
        f"**Date:** {results['metadata']['date']}",
        f"**Session:** {results['metadata']['session']}",
        f"**Graph classes:** {', '.join(results['metadata']['graph_classes'])}",
        f"**Beta values:** {results['metadata']['beta_values']}",
        "",
        "## Overall Verdict",
        "",
        f"**{results['summary']['overall_verdict']}**",
        "",
        f"- Broadness PASS: {results['summary']['broadness_PASS_count']}/{results['summary']['n_runs_total']} ({100*results['summary']['broadness_PASS_rate']:.1f}%)",
        f"- Lift PASS: {results['summary']['lift_PASS_count']}/{results['summary']['n_runs_total']} ({100*results['summary']['lift_PASS_rate']:.1f}%)",
        f"- Errors: {results['summary']['n_errors']}",
        "",
        "## Per-run results",
        "",
        "| Graph | n | beta | d_ratio | u_range | ||r||_2 | mu_min(full) | mu_min(H_cl) | pred(lcl) | broad | lift |",
        "|---|---:|---:|---:|---|---:|---:|---:|---:|---|---|",
    ]
    for r in results["runs"]:
        if "error" in r:
            lines.append(
                f"| {r['graph']} | {r['n_nodes']} | {r['beta']:.1f} | — | — | — | ERROR | — | — | — | — |"
            )
            continue
        lines.append(
            f"| {r['graph']} | {r['n_nodes']} | {r['beta']:.1f} | "
            f"{r['graph_d_ratio']:.3f} | "
            f"[{r['u_min']:.3f},{r['u_max']:.3f}] | "
            f"{r['closure_residual_2']:.3f} | "
            f"{r['mu_min_full_excl_goldstone']:+.4e} | "
            f"{r['mu_min_H_cl_excl_goldstone']:+.4e} | "
            f"{r['predicted_closure_lift']:.3e} | "
            f"{'PASS' if r['broadness_PASS'] else 'FAIL'} | "
            f"{'PASS' if r['lift_PASS'] else 'FAIL'} |"
        )

    lines.extend([
        "",
        "## Interpretation",
        "",
        "**Broadness PASS** = mu_min(Pi_T H_E Pi_T) > 0 after excluding the volume Goldstone zero.",
        "Tests L-HMORSE-LOCAL Cat B (CV-1.16 canonical) on non-grid graph classes.",
        "",
        "**Lift PASS** = mu_min(Pi_T H_cl Pi_T) >= 0.9 * Theorem B2 standard-form prediction.",
        "Tests L-CLOSURE-LIFT Cat A (CV-1.16 canonical) broadness on heterogeneous graphs.",
        "",
        "### Graph class characteristics",
        "",
        "- **SBM:** community-coupled regime; tests whether L-CLOSURE-LIFT broadness propagates through block off-diagonal structure.",
        "- **Barbell:** near-disconnected regime; bridge nodes have low degree, extreme d_min/d_max ratio.",
        "- **Small-world (WS):** long-range rewired edges; tests whether Hessian spectrum is robust to non-local edge structure.",
        "",
        "### Expected vs observed",
        "",
        "The L-CLOSURE-LIFT prediction `2 lambda_cl (1 - a_cl/4)^2 * (d_min/d_max)` accounts for degree heterogeneity via the d_min/d_max factor. On non-regular graphs (especially barbell), this factor can be small, making the prediction tighter. Numerical lift typically exceeds prediction (similar margin to canonical grids per exp_hmorse_broadness_full_spectrum).",
        "",
        "## References",
        "",
        "- CV-1.16 L-HMORSE-LOCAL Cat B (canonical §13 Cat B, sealed 2026-05-14)",
        "- `CODE/experiments/exp_hmorse_broadness_full_spectrum.py` (canonical 2D grid baseline, 15/15 PASS)",
        "- `THEORY/logs/daily/2026-05-14/03_integration_and_new_open.md` §2.2 OP-HMORSE-SBM",
        "- `THEORY/canonical/CV-1.16_SEAL.md` §CV-1.17 Targets",
        "",
        "*Generated by `exp_hmorse_sbm_robustness.py`.*",
    ])
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    out_dir = Path(__file__).resolve().parent / "results"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Running OP-HMORSE-SBM robustness sweep...")
    print("Graph classes: SBM, barbell, small-world (Watts-Strogatz)")
    print(f"Output dir: {out_dir}")
    print()

    t0 = time.time()
    results = run_sweep()
    total_elapsed = time.time() - t0
    results["metadata"]["total_elapsed_sec"] = total_elapsed
    print(f"\nTotal elapsed: {total_elapsed:.1f}s")
    print(f"Verdict: {results['summary']['overall_verdict']}")

    json_path = out_dir / "exp_hmorse_sbm_robustness.json"
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nWrote {json_path}")

    md_path = out_dir / "exp_hmorse_sbm_robustness.md"
    write_markdown_summary(results, md_path)
    print(f"Wrote {md_path}")

    return results


if __name__ == "__main__":
    main()
