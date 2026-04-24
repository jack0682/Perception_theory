"""Phase 3.2: (lambda_cl, lambda_sep) phase diagram for F_min.

Tests the prediction: F_min depends monotonically on the lambda ratio.
Limits:
  - (lambda_cl, lambda_sep) = (0, 0)  -> F_min = 1 (pure E_bd)
  - (lambda_cl, 0)                    -> F_min(λ_cl): closure-only effect (NQ-134 part 1)
  - (0, lambda_sep)                   -> F_min(λ_sep): sep-only effect (NQ-134 part 2)
  - (1, 1)                            -> F_min = full SCC

Grid: L=16 (manageable), N_RESTARTS=8 per param point, ~9 grid points.
Estimated runtime: ~30-45 min.

Run: cd CODE && python3 scripts/phase3_C2_lambda_phase_diagram.py
Output: scripts/results/phase3_C2_phase_diagram.json
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


def run_one_lambda(L, w_cl, w_sep, n_restarts=8, beta=30.0, c=0.5):
    n = L * L
    graph = GraphState.grid_2d(L, L)
    p = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=w_cl, w_sep=w_sep, w_bd=1.0,
        n_restarts=n_restarts, max_iter=3000,
    )
    F_list = []
    E_list = []
    for r in range(n_restarts):
        np.random.seed(7 + r * 13)
        u_init = np.random.uniform(0.3, 0.7, size=n)
        try:
            res = find_formation(graph, p, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F_list.append(count_local_maxima(res.u, L))
                E_list.append(float(res.energy))
        except Exception:
            pass
    if not F_list:
        return {'F_min': None, 'F_max': None, 'F_mean': None, 'n': 0}
    return {
        'F_min': int(min(F_list)),
        'F_max': int(max(F_list)),
        'F_mean': float(np.mean(F_list)),
        'F_list': [int(f) for f in F_list],
        'E_min': float(min(E_list)),
        'n': len(F_list),
    }


def main():
    L = 16
    n_restarts = 8

    # Grid: lambda_cl x lambda_sep
    lambdas = [0.0, 0.5, 1.0, 2.0]
    output_path = os.path.join(os.path.dirname(__file__), 'results', 'phase3_C2_phase_diagram.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"=== Phase 3.2 (lambda_cl, lambda_sep) phase diagram ===")
    print(f"L={L}, n_restarts={n_restarts}, lambdas={lambdas}")
    print()

    results = {}
    t0 = time.time()
    for w_cl in lambdas:
        for w_sep in lambdas:
            key = f"({w_cl},{w_sep})"
            print(f"--- {key} ---")
            t = time.time()
            r = run_one_lambda(L, w_cl, w_sep, n_restarts=n_restarts)
            r['runtime_sec'] = time.time() - t
            r['w_cl'] = w_cl
            r['w_sep'] = w_sep
            results[key] = r
            if r['F_min'] is not None:
                print(f"  F_min={r['F_min']}, F_max={r['F_max']}, F_mean={r['F_mean']:.1f}, runtime={r['runtime_sec']:.1f}s")
            else:
                print(f"  ERROR: no convergence")
            with open(output_path, 'w') as f:
                json.dump({'L': L, 'n_restarts': n_restarts,
                           'beta': 30.0, 'c': 0.5,
                           'lambdas': lambdas,
                           'results': results}, f, indent=2)

    print(f"\nTotal runtime: {time.time() - t0:.1f}s")
    print(f"Saved: {output_path}")

    # Summary table
    print(f"\n=== F_min table ({L}x{L}) ===")
    print("            " + "  ".join(f"sep={w:5.1f}" for w in lambdas))
    for w_cl in lambdas:
        row = [f"{results[f'({w_cl},{w_sep})']['F_min']!s:>6}" for w_sep in lambdas]
        print(f"cl={w_cl:5.1f}     " + "    ".join(row))


if __name__ == "__main__":
    main()
