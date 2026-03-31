#!/usr/bin/env python3
"""Experiment 9: Temporal Transport and Persistence
Demonstrates the self-referential transport kernel across time steps.

Scenarios:
1. Static persistence: same graph, verify Persist ≈ 1
2. Gentle perturbation: slightly modified field, verify transport tracks
3. Spatial shift: shifted adjacency, verify transport follows
4. Formation splitting: two formations merge/split over time
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.transport import (
    cohesion_fingerprint, graph_distance_matrix, transport_cost,
    sinkhorn_partial_ot, transport_field, transport_fixed_point,
    persist_transport,
)

GRID = (10, 10)
BETA = 20.0
C = 0.3


def make_params(**overrides):
    defaults = dict(beta_bd=BETA, volume_fraction=C, n_restarts=3, max_iter=2000)
    defaults.update(overrides)
    return ParameterRegistry(**defaults)


def print_transport_result(name, tr, u_t):
    """Print summary of a TransportResult."""
    persist = persist_transport(tr.u_t, tr.u_s, tr.M, theta_core=0.8)
    core_t = np.sum(tr.u_t >= 0.8)
    core_s = np.sum(tr.u_s >= 0.8)
    field_diff = np.linalg.norm(tr.u_s - tr.u_t) / np.sqrt(len(tr.u_t))
    print(f"\n  [{name}]")
    print(f"  FP converged: {tr.converged} in {tr.iterations} iters")
    print(f"  FP residuals: {[f'{r:.2e}' for r in tr.fp_residuals]}")
    print(f"  Transport energy: {tr.transport_energy:.6f}")
    print(f"  Persist (transport): {persist:.4f}")
    print(f"  Core sites: t={core_t}, s={core_s}")
    print(f"  Field diff ||u_s - u_t||/√n: {field_diff:.6f}")
    print(f"  u_t: mean={tr.u_t.mean():.4f}, max={tr.u_t.max():.4f}")
    print(f"  u_s: mean={tr.u_s.mean():.4f}, max={tr.u_s.max():.4f}")


def scenario_static():
    """Scenario 1: Static persistence — same graph, formation should persist perfectly."""
    print("\n" + "="*70)
    print("Scenario 1: Static persistence (same graph, same energy)")
    print("="*70)

    graph = GraphState.grid_2d(*GRID)
    params = make_params()
    result = find_formation(graph, params)
    u_t = result.u

    print(f"  Formation found: E={result.energy:.6f}, {result.diagnostics}")

    tr = transport_fixed_point(
        u_t, graph, params,
        sigma=2.0, gamma=1.0, eps_ot=1.0, lambda_tr=0.1,
        max_fp_iter=10, fp_tol=1e-4,
    )
    print_transport_result("Static", tr, u_t)
    return persist_transport(tr.u_t, tr.u_s, tr.M, theta_core=0.8)


def scenario_gentle_perturbation():
    """Scenario 2: Gentle perturbation — slightly noisy field."""
    print("\n" + "="*70)
    print("Scenario 2: Gentle perturbation (add small noise to field)")
    print("="*70)

    graph = GraphState.grid_2d(*GRID)
    params = make_params()
    result = find_formation(graph, params)
    u_t = result.u

    print(f"  Formation found: E={result.energy:.6f}, {result.diagnostics}")

    # Add small noise to the formation
    rng = np.random.RandomState(42)
    noise = 0.05 * rng.randn(graph.n)
    u_perturbed = np.clip(u_t + noise, 0.0, 1.0)
    # Re-normalize volume
    u_perturbed *= (u_t.sum() / u_perturbed.sum())
    u_perturbed = np.clip(u_perturbed, 0.0, 1.0)

    diff_init = np.linalg.norm(u_perturbed - u_t) / np.sqrt(graph.n)
    print(f"  Initial perturbation ||noise||/√n: {diff_init:.6f}")

    tr = transport_fixed_point(
        u_perturbed, graph, params,
        sigma=2.0, gamma=1.0, eps_ot=1.0, lambda_tr=0.1,
        max_fp_iter=10, fp_tol=1e-4,
    )
    print_transport_result("Gentle perturbation", tr, u_t)
    return persist_transport(tr.u_t, tr.u_s, tr.M, theta_core=0.8)


def scenario_spatial_shift():
    """Scenario 3: Spatial shift — roll the field by a few sites."""
    print("\n" + "="*70)
    print("Scenario 3: Spatial shift (roll field on grid)")
    print("="*70)

    rows, cols = GRID
    graph = GraphState.grid_2d(rows, cols)
    params = make_params()
    result = find_formation(graph, params)
    u_t = result.u

    print(f"  Formation found: E={result.energy:.6f}, {result.diagnostics}")

    # Shift the field by 1 column on the grid
    u_2d = u_t.reshape(rows, cols)
    u_shifted = np.roll(u_2d, shift=1, axis=1).ravel()

    diff_shift = np.linalg.norm(u_shifted - u_t) / np.sqrt(graph.n)
    print(f"  Shift displacement ||u_shifted - u_t||/√n: {diff_shift:.6f}")

    tr = transport_fixed_point(
        u_shifted, graph, params,
        sigma=2.0, gamma=1.0, eps_ot=1.0, lambda_tr=0.1,
        max_fp_iter=10, fp_tol=1e-4,
    )
    print_transport_result("Spatial shift", tr, u_t)
    return persist_transport(tr.u_t, tr.u_s, tr.M, theta_core=0.8)


def scenario_formation_split():
    """Scenario 4: Formation with different volume fractions."""
    print("\n" + "="*70)
    print("Scenario 4: Different volume fractions (formation change)")
    print("="*70)

    graph = GraphState.grid_2d(*GRID)

    # Formation at c=0.3
    params_t = make_params(volume_fraction=0.3)
    result_t = find_formation(graph, params_t)
    u_t = result_t.u
    print(f"  Formation t (c=0.3): E={result_t.energy:.6f}, {result_t.diagnostics}")

    # Formation at c=0.4 (larger)
    params_s = make_params(volume_fraction=0.4)
    result_s = find_formation(graph, params_s)
    u_s_ref = result_s.u
    print(f"  Formation s (c=0.4): E={result_s.energy:.6f}, {result_s.diagnostics}")

    # Transport from t to s (using s's parameters for optimization)
    tr = transport_fixed_point(
        u_t, graph, params_s,
        sigma=2.0, gamma=1.0, eps_ot=1.0, lambda_tr=0.1,
        max_fp_iter=10, fp_tol=1e-4,
    )
    print_transport_result("Volume change", tr, u_t)
    return persist_transport(tr.u_t, tr.u_s, tr.M, theta_core=0.8)


def main():
    print("Experiment 9: Temporal Transport and Persistence")
    print(f"Grid: {GRID}, β={BETA}, c={C}")

    t0 = time.time()

    results = {}
    results['static'] = scenario_static()
    results['gentle'] = scenario_gentle_perturbation()
    results['shift'] = scenario_spatial_shift()
    results['split'] = scenario_formation_split()

    elapsed = time.time() - t0

    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    print(f"  {'Scenario':<25s} {'Persist':>10s}")
    print(f"  {'-'*25} {'-'*10}")
    for name, val in results.items():
        print(f"  {name:<25s} {val:>10.4f}")
    print(f"\n  Total time: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
