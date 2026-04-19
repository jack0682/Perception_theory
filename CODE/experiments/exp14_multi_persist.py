#!/usr/bin/env python3
"""Experiment 14: Multi-Formation Persistence Analysis.

Tests how well-separated formations maintain separation and persistence
under various conditions.

Experiments:
E1. Separation persistence under gentle transition (eps_ot sweep)
E2. Joint vs Independent transport quality (mode comparison)
E3. Joint Hessian spectral gap (beta sweep)
E5. Overlap vs Persist correlation (lambda_rep sweep)
"""
import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import (find_k_formations, transport_k_formations,
                        inter_formation_distances, classify_regime, formation_overlap)
from scc.transport import persist_transport
from scc.energy import EnergyComputer


def print_header(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def experiment_E1_separation_persistence():
    """E1: Verify d_min preservation under gentle perturbation."""
    print_header("E1: Separation Persistence Under Gentle Transition")

    grid = GraphState.grid_2d(15, 15)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=50.0,  # Strong phase separation
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.3,
    )

    # Find K=2 well-separated formations
    sources = find_k_formations(grid, params, K=2,
                                lambda_rep=50.0, max_iter=1000, n_restarts=3)

    # Compute initial d_min
    d_min_t = inter_formation_distances([s.u for s in sources], grid)
    regime = classify_regime([s.u for s in sources], grid)
    print(f"  Initial d_min: {d_min_t[0,1]:.0f}, regime: {regime}")

    # Transport with different perturbation levels (simulated via eps_ot)
    # Higher eps_ot = more diffuse transport = more perturbation
    for eps_ot in [0.1, 0.5, 1.0, 2.0, 5.0]:
        results = transport_k_formations(
            sources, grid, params,
            lambda_rep=50.0,
            sigma=1.0, gamma=1.0, eps_ot=eps_ot, max_fp_iter=10,
        )

        fields_s = [r.u_s for r in results]
        d_min_s = inter_formation_distances(fields_s, grid)
        regime_s = classify_regime(fields_s, grid)

        # Per-formation Persist
        persists = [persist_transport(r.u_t, r.u_s, r.M) for r in results]

        # Simplex violation
        S = sum(fields_s)
        max_viol = float(np.max(np.maximum(0, S - 1.0)))

        print(f"  eps_ot={eps_ot:.1f}: d_min_s={d_min_s[0,1]:.0f} "
              f"(Δd={d_min_s[0,1]-d_min_t[0,1]:.0f}), "
              f"regime={regime_s}, "
              f"Persist=[{persists[0]:.3f},{persists[1]:.3f}], "
              f"max_viol={max_viol:.4f}")


def experiment_E5_overlap_persist():
    """E5: Overlap vs Persist as lambda_rep varies."""
    print_header("E5: Overlap-Persist Correlation (lambda_rep sweep)")

    grid = GraphState.grid_2d(12, 12)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=30.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.4,
    )

    print(f"  {'lambda_rep':>10s}  {'d_min':>5s}  {'overlap':>8s}  {'regime':>20s}  "
          f"{'Persist_0':>9s}  {'Persist_1':>9s}  {'max_viol':>8s}")
    print(f"  {'-'*80}")

    for lam_rep in [0.1, 0.5, 1.0, 5.0, 10.0, 50.0, 100.0]:
        sources = find_k_formations(grid, params, K=2,
                                    lambda_rep=lam_rep, max_iter=1000, n_restarts=2)

        fields_t = [s.u for s in sources]
        d_min = inter_formation_distances(fields_t, grid)
        overlap = formation_overlap(fields_t)
        regime = classify_regime(fields_t, grid)

        results = transport_k_formations(
            sources, grid, params,
            lambda_rep=lam_rep,
            sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10,
        )

        persists = [persist_transport(r.u_t, r.u_s, r.M) for r in results]
        S = sum(r.u_s for r in results)
        max_viol = float(np.max(np.maximum(0, S - 1.0)))

        print(f"  {lam_rep:10.1f}  {d_min[0,1]:5.0f}  {overlap[0,1]:8.4f}  "
              f"{regime:>20s}  {persists[0]:9.3f}  {persists[1]:9.3f}  {max_viol:8.4f}")


def _numerical_hessian(ec, u, h=1e-5):
    """Compute Hessian via finite differences on the gradient."""
    n = len(u)
    H = np.zeros((n, n))
    g0 = ec.gradient(u)
    for i in range(n):
        u_p = u.copy()
        u_p[i] += h
        g_p = ec.gradient(u_p)
        H[:, i] = (g_p - g0) / h
    # Symmetrize
    return 0.5 * (H + H.T)


def experiment_E2_transport_comparison():
    """E2: Compare independent vs correction vs reoptimize transport."""
    print_header("E2: Transport Mode Comparison (K=2, weakly-interacting)")

    grid = GraphState.grid_2d(12, 12)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=30.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.4,
    )

    # Find weakly-interacting formations (low repulsion -> some overlap)
    sources = find_k_formations(grid, params, K=2, lambda_rep=2.0,
                                max_iter=1000, n_restarts=3)

    fields_t = [s.u for s in sources]
    d_min = inter_formation_distances(fields_t, grid)
    overlap = formation_overlap(fields_t)
    regime = classify_regime(fields_t, grid)
    print(f"  Source: d_min={d_min[0,1]:.0f}, overlap={overlap[0,1]:.2f}, regime={regime}")

    modes = ['none', 'correction']
    # Try to add reoptimize if available
    try:
        test_results = transport_k_formations(sources, grid, params,
                                              phase2_mode='reoptimize',
                                              lambda_rep=2.0, max_fp_iter=3)
        modes.append('reoptimize')
    except TypeError:
        print("  (reoptimize mode not yet available)")

    print(f"\n  {'mode':>12s}  {'Persist_0':>9s}  {'Persist_1':>9s}  "
          f"{'max_viol':>8s}  {'energy':>10s}")
    print(f"  {'-'*60}")

    for mode in modes:
        try:
            results = transport_k_formations(
                sources, grid, params,
                lambda_rep=2.0,
                phase2_mode=mode,
                sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10,
            )
        except TypeError:
            # phase2_mode not supported yet — fall back to default
            results = transport_k_formations(
                sources, grid, params,
                lambda_rep=2.0,
                sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=10,
            )

        persists = [persist_transport(r.u_t, r.u_s, r.M) for r in results]

        S = sum(r.u_s for r in results)
        max_viol = float(np.max(np.maximum(0, S - 1.0)))

        ec = EnergyComputer(grid, params)
        ec.normalize_weights()
        total_E = sum(ec.energy(r.u_s)[0] for r in results)

        print(f"  {mode:>12s}  {persists[0]:9.3f}  {persists[1]:9.3f}  "
              f"{max_viol:8.4f}  {total_E:10.4f}")


def experiment_E3_spectral_gap():
    """E3: Measure joint Hessian spectral gap vs per-formation gaps."""
    print_header("E3: Joint Hessian Spectral Gap")

    grid = GraphState.grid_2d(10, 10)

    print(f"  {'beta':>6s}  {'mu_1':>8s}  {'mu_2':>8s}  {'min_mu':>8s}  "
          f"{'mu_joint':>9s}  {'coupling':>9s}  {'d_min':>5s}  {'overlap':>7s}")
    print(f"  {'-'*70}")

    for beta in [20, 50, 100, 200]:
        params = ParameterRegistry(
            a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
            a_D=5.0, lambda_D=1.0, tau_D=0.0,
            alpha_bd=1.0, beta_bd=float(beta),
            w_cl=1.0, w_sep=1.0, w_bd=1.0,
            volume_fraction=0.3,
        )

        lambda_rep = 10.0
        sources = find_k_formations(grid, params, K=2,
                                    lambda_rep=lambda_rep, max_iter=1000, n_restarts=2)

        # Per-formation spectral gaps
        ec = EnergyComputer(grid, params)
        ec.normalize_weights()

        n = grid.n
        P = np.eye(n) - np.ones((n, n)) / n

        mu_per = []
        for s in sources:
            H = _numerical_hessian(ec, s.u)
            H_proj = P @ H @ P
            eigs = np.linalg.eigvalsh(H_proj)
            pos_eigs = eigs[eigs > 1e-8]
            mu = float(pos_eigs[0]) if len(pos_eigs) > 0 else 0.0
            mu_per.append(mu)

        min_mu = min(mu_per)

        # Joint Hessian (2n x 2n block matrix with coupling)
        H1 = _numerical_hessian(ec, sources[0].u)
        H2 = _numerical_hessian(ec, sources[1].u)

        H_joint = np.zeros((2*n, 2*n))
        H_joint[:n, :n] = H1 + lambda_rep * np.diag(sources[1].u)
        H_joint[n:, n:] = H2 + lambda_rep * np.diag(sources[0].u)

        V_coupling = lambda_rep * np.eye(n)
        H_joint[:n, n:] = V_coupling
        H_joint[n:, :n] = V_coupling

        # Project onto joint tangent space (remove mean constraint per formation)
        P_joint = np.eye(2*n)
        P1 = np.zeros((2*n, 2*n))
        P1[:n, :n] = np.ones((n, n)) / n
        P2 = np.zeros((2*n, 2*n))
        P2[n:, n:] = np.ones((n, n)) / n
        P_joint = P_joint - P1 - P2
        H_joint_proj = P_joint @ H_joint @ P_joint

        eigs_joint = np.linalg.eigvalsh(H_joint_proj)
        pos_eigs_joint = eigs_joint[eigs_joint > 1e-8]
        mu_joint = float(pos_eigs_joint[0]) if len(pos_eigs_joint) > 0 else 0.0

        coupling_norm = float(np.linalg.norm(V_coupling))

        d_min = inter_formation_distances([s.u for s in sources], grid)
        overlap = formation_overlap([s.u for s in sources])

        print(f"  {beta:6d}  {mu_per[0]:8.1f}  {mu_per[1]:8.1f}  {min_mu:8.1f}  "
              f"{mu_joint:9.1f}  {coupling_norm:9.1f}  {d_min[0,1]:5.0f}  {overlap[0,1]:7.1f}")


def experiment_E6_merge_split():
    """E6: Merge-split transition as lambda_rep decreases."""
    print_header("E6: Merge-Split Transition (K=2, lambda_rep sweep)")

    grid = GraphState.grid_2d(10, 10)
    params = ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=20.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )

    print(f"  {'lam_rep':>8s}  {'d_min':>5s}  {'overlap':>7s}  {'regime':>20s}  "
          f"{'K_eff':>5s}  {'Persist':>14s}  {'viol':>6s}")
    print(f"  {'-'*80}")

    for lam_rep in [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.1, 0.01]:
        sources = find_k_formations(grid, params, K=2,
                                     lambda_rep=lam_rep, max_iter=1000, n_restarts=2)

        fields_t = [s.u for s in sources]
        d = inter_formation_distances(fields_t, grid)
        o = formation_overlap(fields_t)
        regime = classify_regime(fields_t, grid)

        # Transport with correction
        results = transport_k_formations(
            sources, grid, params, lambda_rep=lam_rep,
            phase2_mode='correction',
            sigma=1.0, gamma=1.0, eps_ot=1.0, max_fp_iter=5,
        )

        persists = [persist_transport(r.u_t, r.u_s, r.M) for r in results]

        S = sum(r.u_s for r in results)
        max_viol = float(np.max(np.maximum(0, S - 1.0)))

        # K_effective: count formations with substantial core
        K_eff = sum(1 for r in results
                    if np.sum(r.u_s > 0.5) > 5)  # at least 5 core nodes

        print(f"  {lam_rep:8.2f}  {d[0,1]:5.0f}  {o[0,1]:7.0f}  {regime:>20s}  "
              f"{K_eff:5d}  [{persists[0]:.3f},{persists[1]:.3f}]  {max_viol:6.4f}")


def main():
    print("Experiment 14: Multi-Formation Persistence Analysis")
    print(f"{'=' * 60}")
    t0 = time.time()

    experiment_E1_separation_persistence()
    experiment_E5_overlap_persist()
    experiment_E2_transport_comparison()
    experiment_E3_spectral_gap()
    experiment_E6_merge_split()

    total = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"  Total time: {total:.1f}s")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
