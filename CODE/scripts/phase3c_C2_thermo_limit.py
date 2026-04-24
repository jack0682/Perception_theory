"""Phase 3C: Thermodynamic limit experiment for F_*(L).

Goal: determine F_*(L) scaling as L grows, plus diagnose pure-E_bd anomalies.

Improvements over phase3_C2_L_sweep.py:
  1. Denser L: {8, 10, 12, 14, 16, 20, 24, 32}
  2. Mixed IC for full SCC: random + Fiedler-perturbed (closer to R23 protocol)
  3. More restarts (15 per L)
  4. Pure E_bd: 8 restarts (diagnose F=0 anomaly at L=24, 32)
  5. Save F-distribution per IC strategy

Estimated runtime: ~45-60 minutes CPU.

Run: cd CODE && python3 scripts/phase3c_C2_thermo_limit.py
Output: scripts/results/phase3c_C2_thermo_limit.json
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse.linalg as spla
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


def make_random_ic(n, seed):
    np.random.seed(seed)
    return np.random.uniform(0.3, 0.7, size=n)


def make_fiedler_ic(graph, n, seed, c=0.5, amplitude=0.2):
    """Fiedler-perturbed IC: u = c + amplitude * sign-randomized Fiedler vector."""
    np.random.seed(seed)
    # Compute lowest few eigenvectors
    L_mat = graph.L.astype(np.float64)
    try:
        eigvals, eigvecs = spla.eigsh(L_mat, k=4, which='SM')
    except Exception:
        eigvals, eigvecs = spla.eigsh(L_mat, k=4, sigma=0.0)
    # Combine eigenvectors with random weights (R23-like eigenmode_combo)
    weights = np.random.uniform(-1, 1, size=4)
    weights /= np.linalg.norm(weights)
    perturb = eigvecs @ weights
    perturb /= np.max(np.abs(perturb)) + 1e-12
    u = c + amplitude * perturb
    return np.clip(u, 0.05, 0.95)


def run_one_L(L, n_restarts_full=15, n_restarts_pure=8, beta=30.0, c=0.5, verbose=True):
    n = L * L
    graph = GraphState.grid_2d(L, L)

    # --- Pure E_bd with multiple restarts ---
    p_pure = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=4000,
    )
    F_pure_list = []
    E_pure_list = []
    for r in range(n_restarts_pure):
        # Mix random and Fiedler IC for pure
        if r % 2 == 0:
            u_init = make_random_ic(n, 100 + r)
        else:
            u_init = make_fiedler_ic(graph, n, 100 + r)
        try:
            res = find_formation(graph, p_pure, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F_pure_list.append(count_local_maxima(res.u, L))
                E_pure_list.append(float(res.energy))
        except Exception:
            pass
    F_pure_min = min(F_pure_list) if F_pure_list else None
    F_pure_mode = max(set(F_pure_list), key=F_pure_list.count) if F_pure_list else None
    if verbose:
        print(f"  L={L} pure E_bd ({len(F_pure_list)}/{n_restarts_pure}): F={F_pure_list}")
        print(f"    F_min={F_pure_min}, F_mode={F_pure_mode}, E_min={min(E_pure_list) if E_pure_list else None}")

    # --- Full SCC with mixed IC ---
    p_full = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        n_restarts=2, max_iter=4000,
    )

    F_full_list = []
    E_full_list = []
    F_full_by_ic = {'random': [], 'fiedler': []}
    for r in range(n_restarts_full):
        if r < n_restarts_full // 2:
            u_init = make_random_ic(n, 200 + r)
            ic_type = 'random'
        else:
            u_init = make_fiedler_ic(graph, n, 200 + r)
            ic_type = 'fiedler'
        try:
            res = find_formation(graph, p_full, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F = count_local_maxima(res.u, L)
                F_full_list.append(F)
                E_full_list.append(float(res.energy))
                F_full_by_ic[ic_type].append(F)
        except Exception:
            pass

    if not F_full_list:
        return {'L': L, 'F_pure_min': F_pure_min, 'F_pure_list': F_pure_list,
                'F_full_min': None, 'error': 'no full convergence'}

    F_full_min = min(F_full_list)
    F_full_mean = float(np.mean(F_full_list))
    F_full_median = float(np.median(F_full_list))
    if verbose:
        print(f"  L={L} full SCC ({len(F_full_list)}/{n_restarts_full}):")
        print(f"    random IC F: {sorted(F_full_by_ic['random'])}")
        print(f"    fiedler IC F: {sorted(F_full_by_ic['fiedler'])}")
        print(f"    F_min={F_full_min}, F_median={F_full_median:.1f}, F_mean={F_full_mean:.1f}")

    return {
        'L': L,
        'F_pure_list': [int(f) for f in F_pure_list],
        'F_pure_min': int(F_pure_min) if F_pure_min is not None else None,
        'F_pure_mode': int(F_pure_mode) if F_pure_mode is not None else None,
        'E_pure_min': float(min(E_pure_list)) if E_pure_list else None,
        'F_full_min': int(F_full_min),
        'F_full_max': int(max(F_full_list)),
        'F_full_mean': float(F_full_mean),
        'F_full_median': float(F_full_median),
        'F_full_list': [int(f) for f in F_full_list],
        'F_full_by_ic_random': sorted([int(f) for f in F_full_by_ic['random']]),
        'F_full_by_ic_fiedler': sorted([int(f) for f in F_full_by_ic['fiedler']]),
        'E_full_min': float(min(E_full_list)),
        'n_restarts_pure': len(F_pure_list),
        'n_restarts_full': len(F_full_list),
    }


def main():
    L_list = [8, 10, 12, 14, 16, 20, 24, 32]
    output = os.path.join(os.path.dirname(__file__), 'results', 'phase3c_C2_thermo_limit.json')
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print("=== Phase 3C Thermodynamic Limit Experiment ===")
    print(f"L list: {L_list}")
    print(f"Pure E_bd restarts per L: 8 (mixed random + Fiedler IC)")
    print(f"Full SCC restarts per L: 15 (random + Fiedler IC)")
    print()

    results = []
    t0 = time.time()
    for L in L_list:
        print(f"--- L={L} ---")
        t = time.time()
        r = run_one_L(L, n_restarts_full=15, n_restarts_pure=8, verbose=True)
        r['runtime_sec'] = time.time() - t
        print(f"  runtime: {r['runtime_sec']:.1f}s\n")
        results.append(r)
        with open(output, 'w') as f:
            json.dump({'L_list': L_list, 'beta': 30.0, 'c': 0.5,
                       'n_restarts_full': 15, 'n_restarts_pure': 8,
                       'results': results}, f, indent=2)

    print(f"\nTotal runtime: {time.time() - t0:.1f}s")
    print(f"Saved: {output}\n")

    # Summary table for scaling
    print("=== F_*(L) Scaling Summary ===")
    print(f"{'L':>4} {'F_pure_min':>11} {'F_pure_mode':>11} {'F_full_min':>11} {'F_full_med':>11} {'F_random_min':>13} {'F_fiedler_min':>14}")
    for r in results:
        if r.get('F_full_min') is None:
            print(f"{r['L']:>4}  ERROR")
            continue
        rmin = min(r['F_full_by_ic_random']) if r['F_full_by_ic_random'] else 'NA'
        fmin = min(r['F_full_by_ic_fiedler']) if r['F_full_by_ic_fiedler'] else 'NA'
        print(f"{r['L']:>4} {r['F_pure_min']!s:>11} {r['F_pure_mode']!s:>11} {r['F_full_min']:>11} {r['F_full_median']:>11.1f} {str(rmin):>13} {str(fmin):>14}")

    # Power-law fit
    print("\n=== Power-law fit: log F_full_min vs log L ===")
    Ls = np.array([r['L'] for r in results if r.get('F_full_min') is not None and r['F_full_min'] > 0])
    Fs = np.array([r['F_full_min'] for r in results if r.get('F_full_min') is not None and r['F_full_min'] > 0])
    if len(Ls) >= 3:
        logL = np.log(Ls)
        logF = np.log(Fs)
        slope, intercept = np.polyfit(logL, logF, 1)
        print(f"  Power: F_full_min ~ {np.exp(intercept):.3f} * L^{slope:.3f}")
        print(f"  Linear vs L^2 vs L^1.5 — observed slope = {slope:.3f}")
    else:
        print("  Insufficient data for fit")


if __name__ == "__main__":
    main()
