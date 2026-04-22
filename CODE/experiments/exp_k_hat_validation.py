#!/usr/bin/env python3
"""
exp_k_hat_validation.py — Round 14 Conjecture 2.1 numerical validation.

Target (Round 14 §3):
  K̂(G; β) = 1 + Vol(Iso_0(M)/Stab) · N_unst^(1/d_eff(G)) + O(1)

Protocol:
  For each (β, graph):
    1. Initialize u^(0) = c·1 + ε·Gaussian noise, mass-projected.
    2. Run find_formation (gradient descent to local min).
    3. Count formations via connected-components of thresholded u > 0.5.
    4. Repeat N_SEEDS times.
    5. Report K̂ = mean(K), std(K).

Scans:
  A — 2D square grid (free BC), β sweep.
  B — 2D torus (periodic BC), β sweep. Predicted extensive K̂ ∼ L·√N_unst.
  C — 1D cycle, β sweep. Predicted K̂ ∼ N_unst (d_eff=1, linear).

Runtime: ~10-30 min at default settings (user adjustable).

Usage (from CODE/):
  python3 experiments/exp_k_hat_validation.py                    # default
  python3 experiments/exp_k_hat_validation.py --seeds 50         # fewer seeds for speed
  python3 experiments/exp_k_hat_validation.py --grid 32          # smaller grid
  python3 experiments/exp_k_hat_validation.py --skip-cycle       # skip 1D
  python3 experiments/exp_k_hat_validation.py --beta-list 0.5,1,5 # custom β

Output: experiments/results/exp_k_hat_validation.json
"""
import sys
import os
import time
import json
import argparse
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation


# ------------------------- graph builders -------------------------

def build_square_free(L: int) -> GraphState:
    """2D square lattice with free (Neumann) boundary conditions."""
    return GraphState.grid_2d(L, L)


def build_torus_2d(L: int) -> GraphState:
    """2D torus: periodic boundary in both directions."""
    n = L * L
    rows, cols, vals = [], [], []
    for i in range(L):
        for j in range(L):
            u_idx = i * L + j
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = (i + di) % L
                nj = (j + dj) % L
                v_idx = ni * L + nj
                rows.append(u_idx)
                cols.append(v_idx)
                vals.append(1.0)
    W = sp.csr_matrix((vals, (rows, cols)), shape=(n, n))
    return GraphState(W=W)


def build_cycle_1d(n: int) -> GraphState:
    """1D cycle C_n."""
    rows, cols, vals = [], [], []
    for i in range(n):
        for di in [1, -1]:
            j = (i + di) % n
            rows.append(i)
            cols.append(j)
            vals.append(1.0)
    W = sp.csr_matrix((vals, (rows, cols)), shape=(n, n))
    return GraphState(W=W)


# ------------------------- formation counting -------------------------

def count_formations_square(u: np.ndarray, L: int, threshold: float = 0.5) -> int:
    """Count connected components of {u > threshold} on 2D LxL grid (4-nearest).

    Uses BFS / flood fill on the 2D lattice structure.
    """
    mask = (u.reshape(L, L) > threshold)
    visited = np.zeros_like(mask, dtype=bool)
    count = 0
    for i in range(L):
        for j in range(L):
            if mask[i, j] and not visited[i, j]:
                # BFS
                count += 1
                stack = [(i, j)]
                while stack:
                    a, b = stack.pop()
                    if not (0 <= a < L and 0 <= b < L):
                        continue
                    if visited[a, b] or not mask[a, b]:
                        continue
                    visited[a, b] = True
                    stack.extend([(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)])
    return count


def count_formations_torus(u: np.ndarray, L: int, threshold: float = 0.5) -> int:
    """Count CC on 2D torus (periodic 4-nearest)."""
    mask = (u.reshape(L, L) > threshold)
    visited = np.zeros_like(mask, dtype=bool)
    count = 0
    for i in range(L):
        for j in range(L):
            if mask[i, j] and not visited[i, j]:
                count += 1
                stack = [(i, j)]
                while stack:
                    a, b = stack.pop()
                    a = a % L
                    b = b % L
                    if visited[a, b] or not mask[a, b]:
                        continue
                    visited[a, b] = True
                    stack.extend([(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)])
    return count


def count_formations_cycle(u: np.ndarray, threshold: float = 0.5) -> int:
    """Count connected arcs on 1D cycle."""
    n = len(u)
    mask = (u > threshold)
    if not mask.any():
        return 0
    if mask.all():
        return 1
    # Count transitions from 0 → 1 in circular pattern
    # On cycle: # components = # of 0→1 transitions
    transitions = 0
    for i in range(n):
        if mask[i] and not mask[(i - 1) % n]:
            transitions += 1
    return transitions


# ------------------------- Laplacian / N_unst -------------------------

def compute_laplacian_spectrum(graph: GraphState, k: int | None = None) -> np.ndarray:
    """Return sorted Laplacian eigenvalues. If k given, only smallest k."""
    L = graph.L.toarray()
    eigs = np.linalg.eigvalsh(0.5 * (L + L.T))
    eigs = np.sort(eigs)
    if k is not None:
        return eigs[:k]
    return eigs


def predict_N_unst(lap_eigs: np.ndarray, beta_bd: float, w_bd: float, c: float) -> int:
    """Round 2 Prop 1.3a: N_unst^bd = #{k ≥ 2 : 2 w_bd λ_k < β_bd |W''(c)|}.

    (Using the convention where the gradient term is w_bd · u^T L u, and
    double-well coefficient is β_bd. Hessian eigenvalue is 2 w_bd λ_k + β_bd W''(c).)
    """
    W_ddot = 12.0 * c * c - 12.0 * c + 2.0
    threshold = beta_bd * abs(W_ddot) / (2.0 * w_bd)
    nontrivial = lap_eigs[1:]
    return int(np.sum(nontrivial < threshold))


# ------------------------- single run -------------------------

def run_one(
    graph: GraphState,
    params: ParameterRegistry,
    L: int,
    count_fn,
    seed: int,
    noise_amplitude: float = 0.05,
    verbose: bool = False,
) -> dict:
    """Initialize from u_uniform + noise, run find_formation, count K."""
    n = graph.n
    c = params.volume_fraction
    rng = np.random.default_rng(seed)
    perturb = rng.standard_normal(n)
    perturb -= perturb.mean()
    u_init = c + noise_amplitude * perturb
    u_init = np.clip(u_init, 1e-3, 1 - 1e-3)
    u_init *= (c * n) / u_init.sum()

    t0 = time.time()
    try:
        result = find_formation(graph, params, u_init=u_init, verbose=False)
        elapsed = time.time() - t0
        u = result.u
        K = count_fn(u)
        return {
            'seed': seed,
            'K': K,
            'energy': float(result.energy),
            'converged': bool(result.converged),
            'elapsed_s': elapsed,
        }
    except Exception as e:
        return {'seed': seed, 'K': -1, 'error': str(e), 'elapsed_s': time.time() - t0}


# ------------------------- full scan -------------------------

def scan_graph(
    name: str,
    graph: GraphState,
    L_param: int,
    count_fn,
    beta_list: list,
    n_seeds: int,
    alpha: float,
    c: float,
    verbose: bool = True,
) -> dict:
    """Scan β for one graph class, compute K̂ distribution per β."""
    if verbose:
        print(f"\n{'=' * 60}")
        print(f"SCAN: {name} (n={graph.n})")
        print(f"{'=' * 60}")

    # Precompute Laplacian spectrum for N_unst prediction
    try:
        lap_eigs = compute_laplacian_spectrum(graph, k=min(graph.n, 500))
        # If not full spectrum, N_unst prediction may undercount at high β
        full_spectrum_available = len(lap_eigs) >= graph.n
    except Exception as e:
        print(f"  WARNING: spectrum computation failed: {e}")
        lap_eigs = None
        full_spectrum_available = False

    results = []
    for beta in beta_list:
        t_start = time.time()
        # Build params
        params = ParameterRegistry(
            beta_bd=beta,
            w_bd=alpha,
            volume_fraction=c,
            w_cl=1.0,
            w_sep=1.0,
            max_iter=200,
        )

        # N_unst prediction
        if lap_eigs is not None:
            n_unst_pred = predict_N_unst(lap_eigs, beta, alpha, c)
        else:
            n_unst_pred = -1

        # Run seeds
        Ks = []
        per_seed = []
        for s in range(n_seeds):
            out = run_one(graph, params, L_param, count_fn, seed=s + 1000)
            per_seed.append(out)
            if out.get('K', -1) >= 0:
                Ks.append(out['K'])

        Ks = np.array(Ks) if Ks else np.array([0])
        elapsed = time.time() - t_start

        summary = {
            'beta': beta,
            'N_unst_predicted': n_unst_pred,
            'spectrum_covers_all': full_spectrum_available,
            'K_mean': float(Ks.mean()),
            'K_std': float(Ks.std()),
            'K_median': float(np.median(Ks)),
            'K_min': int(Ks.min()),
            'K_max': int(Ks.max()),
            'K_histogram': {int(v): int(np.sum(Ks == v)) for v in np.unique(Ks)},
            'n_seeds_ok': len(Ks),
            'n_seeds_fail': n_seeds - len(Ks),
            'elapsed_s': elapsed,
        }
        results.append(summary)

        if verbose:
            print(f"  β={beta:>7.3f} | N_unst~{n_unst_pred:>4} | "
                  f"K̂={summary['K_mean']:.2f}±{summary['K_std']:.2f} "
                  f"(range {summary['K_min']}-{summary['K_max']}, "
                  f"{summary['n_seeds_ok']}/{n_seeds} seeds, {elapsed:.1f}s)")

    return {
        'name': name,
        'n_nodes': graph.n,
        'L_param': L_param,
        'alpha': alpha,
        'c': c,
        'n_seeds': n_seeds,
        'spectrum_covers_all': full_spectrum_available,
        'results': results,
    }


# ------------------------- main -------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grid', type=int, default=24,
                        help='Grid side (2D) or 2× cycle length. Default 24.')
    parser.add_argument('--seeds', type=int, default=30,
                        help='Random seeds per (β, graph). Default 30.')
    parser.add_argument('--alpha', type=float, default=1.0,
                        help='w_bd (gradient smoothness). Default 1.0.')
    parser.add_argument('--c', type=float, default=0.3,
                        help='volume fraction (mass/n). Default 0.3 (Regime I).')
    parser.add_argument('--beta-list', type=str,
                        default='0.5,1.0,3.0,10.0,30.0',
                        help='Comma-separated list of β_bd values.')
    parser.add_argument('--skip-square', action='store_true')
    parser.add_argument('--skip-torus', action='store_true')
    parser.add_argument('--skip-cycle', action='store_true')
    parser.add_argument('--output', type=str,
                        default='experiments/results/exp_k_hat_validation.json')
    args = parser.parse_args()

    L = args.grid
    c = args.c
    alpha = args.alpha
    n_seeds = args.seeds
    beta_list = [float(b) for b in args.beta_list.split(',')]

    print("=" * 72)
    print("exp_k_hat_validation.py — Round 14 Conjecture 2.1 validation")
    print("=" * 72)
    print(f"Grid/cycle size: L={L}")
    print(f"β list: {beta_list}")
    print(f"Seeds per β: {n_seeds}")
    print(f"(α, c) = ({alpha}, {c})")
    print(f"Output: {args.output}")

    total_t0 = time.time()
    scans = {}

    # Scan A: 2D square (free BC)
    if not args.skip_square:
        g = build_square_free(L)
        count_fn = lambda u: count_formations_square(u, L)
        scans['square'] = scan_graph(
            f'2D square (free BC) {L}x{L}', g, L, count_fn,
            beta_list, n_seeds, alpha, c,
        )

    # Scan B: 2D torus
    if not args.skip_torus:
        g = build_torus_2d(L)
        count_fn = lambda u: count_formations_torus(u, L)
        scans['torus'] = scan_graph(
            f'2D torus {L}x{L}', g, L, count_fn,
            beta_list, n_seeds, alpha, c,
        )

    # Scan C: 1D cycle (use 4*L to have comparable n; actually use L*L to match 2D)
    if not args.skip_cycle:
        n_cycle = L * L
        g = build_cycle_1d(n_cycle)
        count_fn = lambda u: count_formations_cycle(u)
        scans['cycle'] = scan_graph(
            f'1D cycle C_{n_cycle}', g, n_cycle, count_fn,
            beta_list, n_seeds, alpha, c,
        )

    total_t = time.time() - total_t0

    # Save
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.path.basename(args.output),
    )
    if not args.output.startswith('/'):
        # relative: place under experiments/results/
        results_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'results',
        )
        os.makedirs(results_dir, exist_ok=True)
        out_path = os.path.join(results_dir, os.path.basename(args.output))
    else:
        out_path = args.output
        os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)

    payload = {
        'config': {
            'L': L,
            'c': c,
            'alpha': alpha,
            'n_seeds': n_seeds,
            'beta_list': beta_list,
        },
        'total_elapsed_s': total_t,
        'scans': scans,
    }
    with open(out_path, 'w') as f:
        json.dump(payload, f, indent=2, default=float)

    print(f"\n{'=' * 72}")
    print(f"DONE in {total_t:.1f}s. Results saved to: {out_path}")
    print("=" * 72)

    # Print comparison summary
    print("\n--- CROSS-GRAPH COMPARISON ---")
    print(f"{'β':>8} | ", end='')
    for key in ['square', 'torus', 'cycle']:
        if key in scans:
            print(f"{key:>20} | ", end='')
    print()
    print("-" * 72)

    for i, beta in enumerate(beta_list):
        print(f"{beta:>8.3f} | ", end='')
        for key in ['square', 'torus', 'cycle']:
            if key in scans:
                r = scans[key]['results'][i]
                s = f"K̂={r['K_mean']:.2f} (N~{r['N_unst_predicted']})"
                print(f"{s:>20} | ", end='')
        print()

    # Extensive-vs-intensive test
    if 'square' in scans and 'torus' in scans:
        print("\n--- EXTENSIVE vs INTENSIVE (Round 14 §3.2 test) ---")
        print(f"{'β':>8} | {'K̂_torus/K̂_sq':>18} | predicted ~{L}")
        for i, beta in enumerate(beta_list):
            r_sq = scans['square']['results'][i]
            r_t = scans['torus']['results'][i]
            ratio = r_t['K_mean'] / max(r_sq['K_mean'], 1e-6)
            print(f"{beta:>8.3f} | {ratio:>18.2f}")


if __name__ == '__main__':
    main()
