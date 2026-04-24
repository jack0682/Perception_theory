"""Phase 3.1: L sweep — find F_min(L) for full SCC.

Tests Theorem 2 prediction: F_min depends on L. Comparison to R23 F_*=5 at L=32.

For each L in {8, 12, 16, 20, 24, 32}:
  1. Find pure E_bd minimizer (F_pure should be 1 for all L)
  2. Run full-SCC find_formation with N_RESTARTS multi-IC
  3. Record minimum F across all restarts -> F_min_full(L)
  4. Save (L, F_pure, F_min_full, energy stats) to JSON

Estimated runtime: L=8..32 with N_RESTARTS=10 -> ~30-60 min total on CPU.
GPU not required.

Run: cd CODE && python3 scripts/phase3_C2_L_sweep.py
Output: scripts/results/phase3_C2_L_sweep.json
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation


def count_local_maxima(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L and g[ni, nj] >= v:
                    ok = False
                    break
            if ok:
                F += 1
    return F


def run_one_L(L, n_restarts=10, beta=30.0, c=0.5, verbose=True):
    """Test full-SCC F_min at given L."""
    n = L * L
    graph = GraphState.grid_2d(L, L)

    # Pure E_bd baseline
    p_pure = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=3, max_iter=3000,
    )
    res_pure = find_formation(graph, p_pure, normalize=False, verbose=False)
    F_pure = count_local_maxima(res_pure.u, L)
    if verbose:
        print(f"  L={L} pure E_bd: F={F_pure}, energy={res_pure.energy:.3f}")

    # Full SCC with multi-restart
    p_full = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        n_restarts=n_restarts, max_iter=3000,
    )

    F_list = []
    E_list = []
    for r in range(n_restarts):
        np.random.seed(42 + r)
        # Random IC
        u_init = np.random.uniform(0.3, 0.7, size=n)
        try:
            res = find_formation(graph, p_full, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F_list.append(count_local_maxima(res.u, L))
                E_list.append(float(res.energy))
        except Exception as e:
            if verbose:
                print(f"    restart {r}: failed ({e})")

    if not F_list:
        return {'L': L, 'F_pure': F_pure, 'F_full_min': None,
                'F_full_list': [], 'error': 'no converged restart'}

    F_min = min(F_list)
    F_max = max(F_list)
    F_mean = float(np.mean(F_list))
    E_min = min(E_list)
    if verbose:
        print(f"  L={L} full SCC: F_min={F_min}, F_max={F_max}, F_mean={F_mean:.1f}, E_min={E_min:.3f}, n={len(F_list)}")

    return {
        'L': L, 'F_pure': int(F_pure),
        'F_full_min': int(F_min), 'F_full_max': int(F_max), 'F_full_mean': float(F_mean),
        'F_full_list': [int(f) for f in F_list],
        'E_full_min': float(E_min), 'E_full_list': E_list,
        'n_restarts_converged': len(F_list),
    }


def main():
    L_list = [8, 12, 16, 20, 24, 32]
    n_restarts = 10
    output_path = os.path.join(os.path.dirname(__file__), 'results', 'phase3_C2_L_sweep.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"=== Phase 3.1 L sweep ===")
    print(f"L list: {L_list}")
    print(f"n_restarts per L: {n_restarts}")
    print()

    results = []
    t0 = time.time()
    for L in L_list:
        print(f"--- L={L} ---")
        t_start = time.time()
        r = run_one_L(L, n_restarts=n_restarts, verbose=True)
        r['runtime_sec'] = time.time() - t_start
        print(f"  runtime: {r['runtime_sec']:.1f}s")
        results.append(r)
        # Save incrementally
        with open(output_path, 'w') as f:
            json.dump({'L_list': L_list, 'n_restarts': n_restarts,
                       'beta': 30.0, 'c': 0.5, 'results': results}, f, indent=2)

    print(f"\nTotal runtime: {time.time() - t0:.1f}s")
    print(f"Results saved to: {output_path}")
    print(f"\n=== F_min(L) summary ===")
    for r in results:
        if r['F_full_min'] is not None:
            print(f"  L={r['L']:3d}: F_pure={r['F_pure']}, F_full_min={r['F_full_min']}, F_full_mean={r['F_full_mean']:.1f}")
        else:
            print(f"  L={r['L']:3d}: ERROR {r.get('error', 'unknown')}")


if __name__ == "__main__":
    main()
