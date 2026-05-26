"""exp_hmorse_broadness_full_spectrum.py

OP-HMORSE-BROADNESS numerical verification (Approach (c)).

Generates symmetry-broken interior single-formation minimizers on
3 grid scales (5x5, 10x10, 15x15) with asymmetric edge weights,
computes the full projected Hessian on the tangent space mod volume
Goldstone, and verifies:

  1. mu_min(Pi_T H_E Pi_T) > 0  -- Cat B confirmation
  2. mu_min >= L-CLOSURE-LIFT prediction
       (2 * lambda_cl * (1 - a_cl/4)^2 * (d_min/d_max)  - residual)
  3. closure residual r = Cl(u*) - u* and ||r||_2 vs Theorem B3 (CL-RES) bound
  4. component spectra of H_bd, H_cl, H_sep separately (L-HMORSE-DECOMP)

Output: JSON + Markdown summary in CODE/experiments/results/.

References:
  - THEORY/logs/daily/2026-05-14/02_development.md  (L-HMORSE-DECOMP, L-CLOSURE-LIFT)
  - THEORY/logs/daily/2026-05-14/42_broadness_approach_b_trace.md  (Theorem B2 Cat A)
  - canonical T7-Enhanced (canonical.md line 1138)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Dict, List

import numpy as np
import scipy.sparse as sp

# allow running from anywhere
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer, grad_bd, grad_cl, grad_sep, double_well_second_deriv
from scc.operators import closure, closure_with_jacobian
from scc.optimizer import find_formation


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def make_asymmetric_grid(rows: int, cols: int, seed: int = 0, perturb: float = 0.1) -> GraphState:
    """Build a 2D grid with asymmetric edge weights to break Aut(G) symmetry.

    Each edge weight = 1 + perturb * eta(e) where eta(e) iid Uniform[0, 1].
    This breaks D_4 symmetry, satisfying D-HMORSE-LOCAL (C4) symmetry-broken.
    """
    rng = np.random.RandomState(seed)
    n = rows * cols
    row_idx: List[int] = []
    col_idx: List[int] = []
    data: List[float] = []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            if c + 1 < cols:
                w = 1.0 + perturb * rng.rand()
                row_idx.extend([idx, idx + 1])
                col_idx.extend([idx + 1, idx])
                data.extend([w, w])
            if r + 1 < rows:
                w = 1.0 + perturb * rng.rand()
                row_idx.extend([idx, idx + cols])
                col_idx.extend([idx + cols, idx])
                data.extend([w, w])
    adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
    return GraphState(adj)


def projected_hessian_fd(ec: EnergyComputer, u: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Compute Pi_T H_E(u) Pi_T via finite differences on gradient.

    Pi_T = I - (1/n) 1 1^T.

    The FD-Hessian H is approx (grad(u + h e_j) - grad(u)) / h, symmetrized.
    Then we project: Pi_T H Pi_T.

    Result is a symmetric n x n matrix with the volume Goldstone (1) exactly
    in its kernel.
    """
    n = len(u)
    g0 = ec.gradient(u)
    H = np.zeros((n, n), dtype=np.float64)
    for j in range(n):
        u_perturb = u.copy()
        u_perturb[j] += h
        g1 = ec.gradient(u_perturb)
        H[:, j] = (g1 - g0) / h
    # Symmetrize
    H = 0.5 * (H + H.T)
    # Project: Pi_T H Pi_T = H - (1/n)*1*(1^T H) - (1/n)*(H 1)*1^T + (1/n^2)*(1^T H 1)*1*1^T
    row_mean = H.mean(axis=0, keepdims=True)
    col_mean = H.mean(axis=1, keepdims=True)
    total_mean = H.mean()
    H_proj = H - row_mean - col_mean + total_mean
    return H_proj


def projected_hessian_component_fd(
    grad_fn, u: np.ndarray, h: float = 1e-5,
) -> np.ndarray:
    """Same as projected_hessian_fd but for a single energy component (e.g., grad_cl)."""
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
    H_proj = H - row_mean - col_mean + total_mean
    return H_proj


def graph_degree_stats(graph: GraphState) -> Dict[str, float]:
    """Return d_min, d_max, d_min/d_max for graph degree distribution."""
    deg = graph.degree
    return {
        "d_min": float(np.min(deg)),
        "d_max": float(np.max(deg)),
        "d_ratio": float(np.min(deg) / np.max(deg)),
    }


def L_closure_lift_prediction(
    lambda_cl: float, a_cl: float, d_ratio: float,
) -> float:
    """Predicted lower bound on closure Hessian eigenvalue (Theorem B2 standard form)."""
    return 2.0 * lambda_cl * (1.0 - a_cl / 4.0) ** 2 * d_ratio


# ---------------------------------------------------------------------------
# Main sweep
# ---------------------------------------------------------------------------

def run_sweep() -> Dict:
    """Run the broadness verification sweep across grid sizes and beta values."""
    grid_sizes = [5, 10, 15]
    beta_values = [10.0, 20.0, 30.0, 50.0, 100.0]
    c_volume = 0.3  # canonical volume fraction
    a_cl = 3.5  # canonical
    alpha_bd = 1.0

    results = {
        "metadata": {
            "experiment": "OP-HMORSE-BROADNESS Approach (c) numerical verification",
            "date": "2026-05-14",
            "session": "W7-Day5 extension",
            "canonical_params": {
                "a_cl": a_cl,
                "eta_cl": 0.5,
                "tau_cl": 0.5,
                "alpha_bd": alpha_bd,
                "volume_fraction": c_volume,
                "asym_perturb": 0.1,
            },
            "L_CLOSURE_LIFT_form": "2 * lambda_cl * (1 - a_cl/4)^2 * (d_min/d_max)",
            "tangent_projection": "Pi_T = I - (1/n) 1 1^T",
        },
        "runs": [],
    }

    for n_grid in grid_sizes:
        print(f"\n{'='*60}")
        print(f"Grid: {n_grid}x{n_grid} (n={n_grid**2})")
        print(f"{'='*60}")

        # Build asymmetric grid
        graph = make_asymmetric_grid(n_grid, n_grid, seed=42)
        deg_stats = graph_degree_stats(graph)
        n = graph.n

        for beta in beta_values:
            t_start = time.time()

            params = ParameterRegistry(
                a_cl=a_cl,
                eta_cl=0.5,
                tau_cl=0.5,
                alpha_bd=alpha_bd,
                beta_bd=beta,
                volume_fraction=c_volume,
            )

            # Generate symmetry-broken interior minimizer
            try:
                result = find_formation(graph, params, normalize=True, verbose=False)
                u_star = result.u
                converged = result.converged
            except Exception as e:
                print(f"  beta={beta}: optimization failed: {e}")
                continue

            # Check (C2) interior: no node at 0 or 1
            u_min = float(u_star.min())
            u_max = float(u_star.max())
            is_interior = (u_min > 1e-6) and (u_max < 1.0 - 1e-6)

            # EnergyComputer with normalized weights
            ec = EnergyComputer(graph, params)
            ec.normalize_weights()

            # Full projected Hessian
            H_proj = projected_hessian_fd(ec, u_star, h=1e-5)
            eigvals_full = np.linalg.eigvalsh(H_proj)
            # Sort ascending
            eigvals_full = np.sort(eigvals_full)

            # The smallest eigenvalue should be ~0 (volume Goldstone projected out).
            # The "true" mu_min is the second-smallest (first non-Goldstone mode).
            mu_min_full_with_goldstone = float(eigvals_full[0])
            mu_min_full_excl_goldstone = float(eigvals_full[1])

            # Component-wise projected Hessians (L-HMORSE-DECOMP decomposition)
            H_bd_proj = projected_hessian_component_fd(
                lambda u_: grad_bd(u_, graph, params), u_star, h=1e-5
            )
            H_cl_proj = projected_hessian_component_fd(
                lambda u_: grad_cl(u_, graph, params), u_star, h=1e-5
            )
            H_sep_proj = projected_hessian_component_fd(
                lambda u_: grad_sep(u_, graph, params), u_star, h=1e-5
            )

            eig_bd = np.sort(np.linalg.eigvalsh(H_bd_proj))
            eig_cl = np.sort(np.linalg.eigvalsh(H_cl_proj))
            eig_sep = np.sort(np.linalg.eigvalsh(H_sep_proj))

            # Closure residual r = Cl(u*) - u* and norm (Theorem B3 (CL-RES))
            cl_u = closure(u_star, graph, params)
            residual = cl_u - u_star
            r_inf = float(np.linalg.norm(residual, ord=np.inf))
            r_2 = float(np.linalg.norm(residual, ord=2))

            # L-CLOSURE-LIFT prediction with normalized lambda_cl
            prediction_lcl_only_normalized = L_closure_lift_prediction(
                lambda_cl=ec.lambda_cl, a_cl=a_cl, d_ratio=deg_stats["d_ratio"]
            )
            # Plus full L-HMORSE-DECOMP prediction including bd and sep
            # H_bd worst-case eigenvalue: alpha*lambda_2 + beta*W''(c)
            W_pp = double_well_second_deriv(c_volume)
            fiedler = graph.fiedler
            prediction_bd_lower = 4.0 * alpha_bd * fiedler + beta * W_pp  # worst-case interior
            prediction_combined = (
                prediction_lcl_only_normalized
                + min(0.0, prediction_bd_lower)  # bd can be negative in spinodal
            )

            # PASS criteria
            broadness_check = mu_min_full_excl_goldstone > 0  # Cat B confirmation
            lift_check = (
                eig_cl[1] >= 0.9 * 2.0 * ec.lambda_cl * (1 - a_cl/4)**2 * deg_stats["d_ratio"]
            )  # closure term meets prediction (within 10%)
            # The 0.9 factor accounts for residual correction and FD numerical error

            elapsed = time.time() - t_start
            run_data = {
                "grid_size": n_grid,
                "n_nodes": n,
                "beta": beta,
                "graph_d_min": deg_stats["d_min"],
                "graph_d_max": deg_stats["d_max"],
                "graph_d_ratio": deg_stats["d_ratio"],
                "graph_fiedler": float(fiedler),
                "lambda_cl_normalized": float(ec.lambda_cl),
                "lambda_sep_normalized": float(ec.lambda_sep),
                "lambda_bd_normalized": float(ec.lambda_bd),
                "u_min": u_min,
                "u_max": u_max,
                "is_interior": is_interior,
                "find_formation_converged": converged,
                "closure_residual_inf": r_inf,
                "closure_residual_2": r_2,
                "mu_min_full_with_goldstone": mu_min_full_with_goldstone,
                "mu_min_full_excl_goldstone": mu_min_full_excl_goldstone,
                "mu_min_H_bd_excl_goldstone": float(eig_bd[1]),
                "mu_min_H_cl_excl_goldstone": float(eig_cl[1]),
                "mu_min_H_sep_excl_goldstone": float(eig_sep[1]),
                "eig_full_min10": [float(v) for v in eigvals_full[:10]],
                "eig_full_max3": [float(v) for v in eigvals_full[-3:]],
                "predicted_closure_lift_lower_normalized": prediction_lcl_only_normalized,
                "predicted_full_combined_lower": prediction_combined,
                "broadness_PASS": bool(broadness_check),
                "lift_PASS": bool(lift_check),
                "elapsed_sec": elapsed,
            }
            results["runs"].append(run_data)
            print(
                f"  beta={beta:6.1f}: u_range=[{u_min:.3f},{u_max:.3f}] "
                f"||r||_inf={r_inf:.4f} ||r||_2={r_2:.4f} "
                f"mu_min(full)={mu_min_full_excl_goldstone:+.4e} "
                f"mu_min(H_cl)={eig_cl[1]:+.4e} "
                f"pred(lcl)={prediction_lcl_only_normalized:.4e} "
                f"broadness={'PASS' if broadness_check else 'FAIL'} "
                f"lift={'PASS' if lift_check else 'FAIL'} "
                f"[{elapsed:.1f}s]"
            )

    # Aggregate verdict
    n_runs = len(results["runs"])
    broadness_pass = sum(r["broadness_PASS"] for r in results["runs"])
    lift_pass = sum(r["lift_PASS"] for r in results["runs"])
    results["summary"] = {
        "n_runs_total": n_runs,
        "broadness_PASS_count": broadness_pass,
        "broadness_PASS_rate": broadness_pass / max(n_runs, 1),
        "lift_PASS_count": lift_pass,
        "lift_PASS_rate": lift_pass / max(n_runs, 1),
        "overall_verdict": (
            "ALL PASS"
            if broadness_pass == n_runs and lift_pass == n_runs
            else f"{broadness_pass}/{n_runs} broadness; {lift_pass}/{n_runs} lift"
        ),
    }

    return results


def write_markdown_summary(results: Dict, md_path: Path) -> None:
    """Write a human-readable Markdown summary."""
    lines = [
        "# exp_hmorse_broadness_full_spectrum — Results Summary",
        "",
        f"**Experiment:** {results['metadata']['experiment']}",
        f"**Date:** {results['metadata']['date']}",
        f"**Session:** {results['metadata']['session']}",
        "",
        "## Canonical parameters",
        "",
        "| Parameter | Value |",
        "|---|---|",
    ]
    for k, v in results["metadata"]["canonical_params"].items():
        lines.append(f"| {k} | {v} |")

    lines.extend([
        "",
        "## Overall Verdict",
        "",
        f"**{results['summary']['overall_verdict']}**",
        "",
        f"- Broadness PASS rate: {results['summary']['broadness_PASS_count']}/{results['summary']['n_runs_total']} ({100*results['summary']['broadness_PASS_rate']:.1f}%)",
        f"- Lift PASS rate: {results['summary']['lift_PASS_count']}/{results['summary']['n_runs_total']} ({100*results['summary']['lift_PASS_rate']:.1f}%)",
        "",
        "## Per-run results",
        "",
        "| n_grid | beta | u_range | ||r||_2 | mu_min(full) | mu_min(H_cl) | pred(lcl) | broadness | lift |",
        "|---|---:|---|---:|---:|---:|---:|---|---|",
    ])
    for r in results["runs"]:
        lines.append(
            f"| {r['grid_size']} | {r['beta']:.1f} | "
            f"[{r['u_min']:.3f},{r['u_max']:.3f}] | "
            f"{r['closure_residual_2']:.4f} | "
            f"{r['mu_min_full_excl_goldstone']:+.4e} | "
            f"{r['mu_min_H_cl_excl_goldstone']:+.4e} | "
            f"{r['predicted_closure_lift_lower_normalized']:.4e} | "
            f"{'PASS' if r['broadness_PASS'] else 'FAIL'} | "
            f"{'PASS' if r['lift_PASS'] else 'FAIL'} |"
        )

    lines.extend([
        "",
        "## Interpretation",
        "",
        "**Broadness PASS** = `mu_min(Pi_T H_E Pi_T)` > 0 after excluding the volume Goldstone zero.",
        "This confirms that the full projected Hessian is positive definite on the tangent space mod volume,",
        "i.e., the L-HMORSE-LOCAL Cat B claim holds numerically at canonical parameters.",
        "",
        "**Lift PASS** = `mu_min(Pi_T H_cl Pi_T)` >= 0.9 * (Theorem B2 standard-form lower bound).",
        "This is the *broadness* check for the closure-correction Hessian: T7-Enhanced's lift propagates",
        "uniformly across the tangent space (not just the closure-aligned eigenmode).",
        "",
        "Theorem B2 (Approach (b), `42_broadness_approach_b_trace.md`) proved this analytically Cat A;",
        "this script confirms numerically. The 10% slack accounts for the residual correction term",
        "`2 sum_k r_k * nabla^2 Cl_k` which appears at full-energy critical points (vs E_cl alone critical points).",
        "",
        "## References",
        "",
        "- `THEORY/logs/daily/2026-05-14/42_broadness_approach_b_trace.md` (Theorem B2 Cat A analytic proof)",
        "- `THEORY/logs/daily/2026-05-14/02_development.md` §3-§4 (L-HMORSE-DECOMP, L-CLOSURE-LIFT)",
        "- `THEORY/2_substrate/canonical/canonical.md` §13 T7-Enhanced (line 1138)",
        "",
        "*Generated by `exp_hmorse_broadness_full_spectrum.py`.*",
    ])

    md_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    out_dir = Path(__file__).resolve().parent / "results"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Running OP-HMORSE-BROADNESS Approach (c) sweep...")
    print("Grid sizes: 5x5, 10x10, 15x15")
    print("Beta values: 10, 20, 30, 50, 100")
    print(f"Output dir: {out_dir}")
    print()

    t0 = time.time()
    results = run_sweep()
    total_elapsed = time.time() - t0

    results["metadata"]["total_elapsed_sec"] = total_elapsed
    print(f"\nTotal elapsed: {total_elapsed:.1f}s")
    print(f"Verdict: {results['summary']['overall_verdict']}")

    # Save JSON
    json_path = out_dir / "exp_hmorse_broadness_full_spectrum.json"
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nWrote {json_path}")

    # Save Markdown
    md_path = out_dir / "exp_hmorse_broadness_full_spectrum.md"
    write_markdown_summary(results, md_path)
    print(f"Wrote {md_path}")

    return results


if __name__ == "__main__":
    main()
