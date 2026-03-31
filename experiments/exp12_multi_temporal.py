#!/usr/bin/env python3
"""Experiment 12: Multi-Formation Temporal Transport.

Demonstrates K-formation temporal transport with independent plans + simplex correction.

Scenarios:
1. K=2 well-separated formations -- independent transport
2. K=2 with perturbation -- test robustness
3. K=3 on larger grid -- scalability
4. Simplex violation analysis -- when does independent transport break down?
"""
import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_formations, transport_k_formations, multi_diagnostic_vector
from scc.transport import persist_transport


def print_header(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def report_results(sources, results, diags, grid):
    """Print per-formation diagnostics and cross-formation metrics."""
    K = len(results)
    n = grid.n

    for k in range(K):
        r = results[k]
        d = diags[k]
        p = persist_transport(r.u_t, r.u_s, r.M)
        print(f"  Formation {k}: Bind={d.bind:.3f}  Sep={d.sep:.3f}  "
              f"Inside={d.inside:.3f}  Persist={p:.3f}  "
              f"converged={r.converged}  iters={r.iterations}")

    # Simplex violation
    S = sum(r.u_s for r in results)
    max_viol = float((S - 1.0).max())
    mean_viol = float(np.mean(np.maximum(0, S - 1.0)))
    print(f"  Simplex: max_violation={max_viol:.4f}  mean_violation={mean_viol:.6f}")

    # Pairwise overlap between transported fields
    for j in range(K):
        for k in range(j + 1, K):
            overlap = float(results[j].u_s @ results[k].u_s) / n
            print(f"  Overlap({j},{k}): {overlap:.4f} per site")


def scenario_1():
    """K=2 well-separated formations on 10x10 grid."""
    print_header("Scenario 1: K=2 well-separated (10x10)")
    grid = GraphState.grid_2d(10, 10)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )

    t0 = time.time()
    sources = find_k_formations(grid, params, K=2,
                                lambda_rep=10.0, max_iter=500, n_restarts=2)
    t_find = time.time() - t0
    print(f"  find_k_formations: {t_find:.1f}s")

    t0 = time.time()
    results = transport_k_formations(
        sources, grid, params,
        max_fp_iter=10, eps_ot=1.0, sigma=1.0, gamma=1.0,
    )
    t_transport = time.time() - t0
    print(f"  transport_k_formations: {t_transport:.1f}s")

    diags = multi_diagnostic_vector(sources, None, results, grid, params)
    report_results(sources, results, diags, grid)


def scenario_2():
    """K=2 with perturbation -- add noise to source fields before transport."""
    print_header("Scenario 2: K=2 with perturbation (10x10)")
    grid = GraphState.grid_2d(10, 10)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )

    sources = find_k_formations(grid, params, K=2,
                                lambda_rep=10.0, max_iter=500, n_restarts=2)

    # Perturb source fields: add noise then re-project
    from scc.optimizer import project_volume
    rng = np.random.RandomState(99)
    n = grid.n
    m = params.volume_fraction * n
    for r in sources:
        noise = 0.05 * rng.randn(n)
        r.u = np.clip(r.u + noise, 0, 1)
        r.u = project_volume(r.u, m)

    t0 = time.time()
    results = transport_k_formations(
        sources, grid, params,
        max_fp_iter=10, eps_ot=1.0,
    )
    elapsed = time.time() - t0
    print(f"  transport (perturbed): {elapsed:.1f}s")

    diags = multi_diagnostic_vector(sources, None, results, grid, params)
    report_results(sources, results, diags, grid)


def scenario_3():
    """K=3 on 15x15 grid -- scalability test."""
    print_header("Scenario 3: K=3 on 15x15 grid")
    grid = GraphState.grid_2d(15, 15)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.3,
    )

    t0 = time.time()
    sources = find_k_formations(grid, params, K=3,
                                lambda_rep=15.0, max_iter=500, n_restarts=2)
    t_find = time.time() - t0
    print(f"  find_k_formations (K=3, 15x15): {t_find:.1f}s")

    t0 = time.time()
    results = transport_k_formations(
        sources, grid, params,
        max_fp_iter=8, eps_ot=1.0,
    )
    t_transport = time.time() - t0
    print(f"  transport_k_formations: {t_transport:.1f}s")

    diags = multi_diagnostic_vector(sources, None, results, grid, params)
    report_results(sources, results, diags, grid)


def scenario_4():
    """Simplex violation analysis: sweep lambda_rep and measure violation after transport."""
    print_header("Scenario 4: Simplex violation vs lambda_rep")
    grid = GraphState.grid_2d(10, 10)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )
    n = grid.n

    lambda_reps = [0.1, 1.0, 5.0, 10.0, 25.0, 50.0, 100.0]
    print(f"  {'lambda_rep':>10s}  {'max_viol':>10s}  {'mean_viol':>10s}  "
          f"{'overlap':>10s}  {'Persist_0':>10s}  {'Persist_1':>10s}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

    for lrep in lambda_reps:
        sources = find_k_formations(grid, params, K=2,
                                    lambda_rep=lrep, max_iter=400, n_restarts=1)
        results = transport_k_formations(
            sources, grid, params,
            max_fp_iter=5, eps_ot=1.0,
        )

        S = sum(r.u_s for r in results)
        max_viol = float((S - 1.0).max())
        mean_viol = float(np.mean(np.maximum(0, S - 1.0)))
        overlap = float(results[0].u_s @ results[1].u_s) / n

        p0 = persist_transport(results[0].u_t, results[0].u_s, results[0].M)
        p1 = persist_transport(results[1].u_t, results[1].u_s, results[1].M)

        print(f"  {lrep:>10.1f}  {max_viol:>10.4f}  {mean_viol:>10.6f}  "
              f"  {overlap:>10.4f}  {p0:>10.3f}  {p1:>10.3f}")


def main():
    print("Experiment 12: Multi-Formation Temporal Transport")
    print(f"{'=' * 60}")
    t0 = time.time()

    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()

    total = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"  Total time: {total:.1f}s")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
