"""NQ-168: 2D Goldstone doublet commensurability splitting — quantitative characterization.

4 hypotheses (falsification priority: D → A → B/C):
  D: Δλ → 0 as L → ∞  (finite-size artifact)
  A: Δλ ∝ center-lattice misalignment (FK/PN mechanism)
  B: Δλ ∝ ζ (linear in lattice scale)
  C: Δλ → 0 when λ_cl = 0 (SCC-closure driven)

Protocol:
  1. N=5 random seeds × L ∈ {20, 30, 40}, ζ=1.0 (super-lattice), β=1.0 (β/β_crit ≈ 10)
  2. Build F=1 single-disk minimizer on torus, pure E_bd (λ_cl=λ_sep=0, λ_bd=1)
  3. Compute lowest 4 Hessian eigenvalues + eigenvectors (projected)
  4. Compute disk center position (x_c, y_c) and fractional lattice alignment
  5. Measure Δλ = λ_1 - λ_0, compute overlap of each mode with δu_x, δu_y
  6. Repeat with λ_cl = 0.1, 0.5 for hypothesis C test

Run: cd CODE && python3 scripts/nq168_commensurability.py
Output: scripts/results/nq168_commensurability.json
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


def build_torus_graph(L):
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di) % L, (j + dj) % L
                nidx = ni * L + nj
                rows.append(idx)
                cols.append(nidx)
    data_arr = np.ones(len(rows))
    W = sp.csr_matrix((data_arr, (rows, cols)), shape=(n, n))
    return GraphState(W)


def count_local_maxima_torus(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            is_max = all(g[(i + di) % L, (j + dj) % L] < v
                         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)])
            if is_max:
                F += 1
    return F


def center_of_mass_torus(u, L):
    """Center of mass on torus using circular statistics."""
    g = u.reshape(L, L)
    ix, iy = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    theta_x = 2 * np.pi * ix / L
    theta_y = 2 * np.pi * iy / L
    w = g
    cx = np.angle(np.sum(w * np.exp(1j * theta_x))) / (2 * np.pi) * L
    cy = np.angle(np.sum(w * np.exp(1j * theta_y))) / (2 * np.pi) * L
    cx = cx % L
    cy = cy % L
    return float(cx), float(cy)


def fractional_alignment(cx, cy, L):
    """Fractional offset from nearest lattice point (0=commensurate, 0.5=maximally incommensurate)."""
    fx = abs(cx - round(cx)) % 1.0
    fx = min(fx, 1.0 - fx)
    fy = abs(cy - round(cy)) % 1.0
    fy = min(fy, 1.0 - fy)
    return float(fx), float(fy)


def translation_modes(u, L):
    """Normalized δu_x, δu_y (translation Goldstone basis)."""
    g = u.reshape(L, L)
    du_x = (np.roll(g, -1, axis=0) - g).flatten()
    du_y = (np.roll(g, -1, axis=1) - g).flatten()
    du_x /= (np.linalg.norm(du_x) + 1e-14)
    du_y /= (np.linalg.norm(du_y) + 1e-14)
    return du_x, du_y


def compute_hessian_lowest(u_star, graph, params, n_modes=4, eps=1e-4):
    """Finite-difference Hessian projected onto tangent space, lowest n_modes."""
    n = graph.n
    g0 = grad_bd(u_star, graph, params)
    H = np.zeros((n, n))
    for i in range(n):
        u_p = u_star.copy()
        u_p[i] += eps
        g_p = grad_bd(u_p, graph, params)
        H[:, i] = (g_p - g0) / eps
    H = (H + H.T) / 2.0
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    idx = np.argsort(eigvals)
    return eigvals[idx[:n_modes]], eigvecs[:, idx[:n_modes]]


def find_F1_minimizer(L, beta, c, seed, lambda_cl=0.0, lambda_sep=0.0):
    """Find F=1 torus-disk minimizer from random IC centered at (cx, cy)."""
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=lambda_cl, w_sep=lambda_sep, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    np.random.seed(seed * 37 + 7)
    cx = np.random.uniform(0.5, L - 0.5)
    cy = np.random.uniform(0.5, L - 0.5)
    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
    dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
    r = np.sqrt(dx**2 + dy**2).flatten()
    ic_width = max(xi_0, 0.2)
    u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_width))
    u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
    try:
        res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
        if not res.converged:
            return None
        F = count_local_maxima_torus(res.u, L)
        return {'u': res.u, 'F': F, 'energy': float(res.energy),
                'graph': graph, 'params': params, 'seed': seed,
                'init_cx': float(cx), 'init_cy': float(cy)}
    except Exception as e:
        return {'error': str(e)}


def analyze_one(result, L):
    """Given a F=1 minimizer result, compute spectral + commensurability data."""
    u = result['u']
    graph = result['graph']
    params = result['params']

    # Center of mass
    cx, cy = center_of_mass_torus(u, L)
    fx, fy = fractional_alignment(cx, cy, L)

    # Translation modes
    du_x, du_y = translation_modes(u, L)

    # Hessian spectrum (lowest 4 modes)
    try:
        eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=4)
    except Exception as e:
        return {'error': str(e)}

    # Overlaps of each eigenmode with translation directions
    overlaps = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_x = float(abs(np.dot(v, du_x)))
        ov_y = float(abs(np.dot(v, du_y)))
        overlaps.append({'mode': k, 'eigenvalue': float(eigvals[k]),
                         'overlap_x': ov_x, 'overlap_y': ov_y,
                         'max_overlap': float(max(ov_x, ov_y))})

    # Δλ = λ_1 - λ_0 (first two physical modes; mode 0 is near-zero tangent)
    lam_phys = [ev for ev in eigvals if ev > 1e-5]  # skip near-zero tangent
    delta_lam = float(lam_phys[1] - lam_phys[0]) if len(lam_phys) >= 2 else None
    lam_0_phys = float(lam_phys[0]) if lam_phys else None
    lam_1_phys = float(lam_phys[1]) if len(lam_phys) >= 2 else None

    return {
        'L': L,
        'seed': result['seed'],
        'F': result['F'],
        'energy': result['energy'],
        'center_x': cx,
        'center_y': cy,
        'fractional_x': fx,
        'fractional_y': fy,
        'misalignment': float(np.sqrt(fx**2 + fy**2)),
        'all_eigvals': [float(e) for e in eigvals],
        'lam_0_phys': lam_0_phys,
        'lam_1_phys': lam_1_phys,
        'delta_lam': delta_lam,
        'mode_overlaps': overlaps,
    }


def run_L_sweep(Ls, N_seeds, beta, c, zeta_label, lambda_cl, lambda_sep):
    """Run full sweep and collect results."""
    all_results = []
    for L in Ls:
        print(f"\n  L={L} (ζ={zeta_label}, β={beta}, λ_cl={lambda_cl})")
        for seed in range(N_seeds):
            t0 = time.time()
            res = find_F1_minimizer(L, beta, c, seed, lambda_cl, lambda_sep)
            if res is None or 'error' in res:
                print(f"    seed={seed}: FAILED ({res})")
                continue
            if res['F'] != 1:
                print(f"    seed={seed}: F={res['F']} (not F=1, skip)")
                continue
            rec = analyze_one(res, L)
            if 'error' in rec:
                print(f"    seed={seed}: analysis error ({rec['error']})")
                continue
            rec['lambda_cl'] = lambda_cl
            dt = time.time() - t0
            print(f"    seed={seed}: cx={rec['center_x']:.2f} cy={rec['center_y']:.2f} "
                  f"fx={rec['fractional_x']:.3f} fy={rec['fractional_y']:.3f} "
                  f"Δλ={rec['delta_lam']:.4e} ({dt:.1f}s)")
            all_results.append(rec)
    return all_results


def test_hypothesis_D(results_by_L):
    """Δλ vs L scaling — hypothesis D: Δλ → 0 (artifact) or constant (physical)."""
    print("\n=== Hypothesis D: Δλ vs L scaling ===")
    Ls = sorted(results_by_L.keys())
    mean_deltas = {}
    for L in Ls:
        deltas = [r['delta_lam'] for r in results_by_L[L] if r['delta_lam'] is not None]
        if deltas:
            mean_deltas[L] = np.mean(deltas)
            print(f"  L={L}: n={len(deltas)}, Δλ mean={mean_deltas[L]:.4e}, "
                  f"min={min(deltas):.4e}, max={max(deltas):.4e}")
    if len(mean_deltas) >= 2:
        Lv = sorted(mean_deltas.keys())
        dv = [mean_deltas[L] for L in Lv]
        # If Δλ decreasing fast: artifact; if roughly constant: physical
        trend = dv[-1] / dv[0] if dv[0] > 0 else None
        print(f"  Δλ ratio (L_max/L_min): {trend:.3f}" if trend else "  Trend: undefined")
        if trend is not None and trend < 0.1:
            print("  → Hypothesis D SUPPORTED (Δλ → 0, artifact)")
        elif trend is not None and trend > 0.5:
            print("  → Hypothesis D FALSIFIED (Δλ roughly constant, physical)")
        else:
            print("  → Hypothesis D UNCERTAIN (moderate decrease)")
    return mean_deltas


def test_hypothesis_A(results):
    """Δλ ∝ misalignment (FK-PN mechanism)."""
    print("\n=== Hypothesis A: Δλ ∝ misalignment ===")
    pairs = [(r['misalignment'], r['delta_lam'])
             for r in results if r['delta_lam'] is not None and r['misalignment'] is not None]
    if len(pairs) < 3:
        print("  INSUFFICIENT DATA")
        return None
    mis = np.array([p[0] for p in pairs])
    dl = np.array([p[1] for p in pairs])
    corr = float(np.corrcoef(mis, dl)[0, 1]) if len(pairs) >= 3 else None
    print(f"  n={len(pairs)}, corr(misalignment, Δλ) = {corr:.3f}" if corr else "  corr: undefined")
    if corr is not None and corr > 0.7:
        print("  → Hypothesis A SUPPORTED (strong positive correlation)")
    elif corr is not None and abs(corr) < 0.3:
        print("  → Hypothesis A WEAKLY SUPPORTED (weak correlation)")
    else:
        print("  → Hypothesis A UNCERTAIN")
    return corr


def main():
    print("=" * 70)
    print("NQ-168: Goldstone commensurability splitting analysis")
    print("=" * 70)

    # Parameters: ζ = ξ₀/a = sqrt(1/β)/1 ≈ 1.0 → β = 1.0
    beta = 1.0   # ξ₀ = 1.0 = lattice spacing → ζ = 1.0 (super-lattice)
    c = 0.5
    N_seeds = 5
    Ls_main = [20, 30, 40]

    report = {
        'beta': beta,
        'c': c,
        'zeta': float(np.sqrt(1.0 / beta)),  # ξ₀/a
        'N_seeds': N_seeds,
        'Ls': Ls_main,
        'results': [],
        'hypothesis_tests': {},
    }

    # Main run: pure E_bd (λ_cl=0)
    print(f"\n--- Phase 1: pure E_bd (λ_cl=0), N={N_seeds} seeds × L ∈ {Ls_main} ---")
    all_results = run_L_sweep(Ls_main, N_seeds, beta, c, zeta_label='1.0',
                               lambda_cl=0.0, lambda_sep=0.0)
    report['results'] = all_results

    # Group by L for hypothesis D
    by_L = {}
    for r in all_results:
        L = r['L']
        by_L.setdefault(L, []).append(r)

    mean_delta_by_L = test_hypothesis_D(by_L)
    report['hypothesis_tests']['D'] = {
        'mean_delta_by_L': {str(k): float(v) for k, v in mean_delta_by_L.items()},
    }

    corr_A = test_hypothesis_A(all_results)
    report['hypothesis_tests']['A'] = {'corr_misalignment_delta': corr_A}

    # Hypothesis C: test with λ_cl = 0.5 at L=30 only (quick test)
    print(f"\n--- Phase 2: hypothesis C test (λ_cl=0.5) at L=30 ---")
    results_C = run_L_sweep([30], 3, beta, c, zeta_label='1.0',
                             lambda_cl=0.5, lambda_sep=0.0)
    report['results_C_test'] = results_C
    if results_C:
        dl_pure = [r['delta_lam'] for r in all_results if r['L'] == 30 and r['delta_lam'] is not None]
        dl_cl = [r['delta_lam'] for r in results_C if r['delta_lam'] is not None]
        if dl_pure and dl_cl:
            ratio_C = np.mean(dl_cl) / np.mean(dl_pure)
            report['hypothesis_tests']['C'] = {
                'mean_delta_pure_Ebd': float(np.mean(dl_pure)),
                'mean_delta_with_cl': float(np.mean(dl_cl)),
                'ratio': float(ratio_C),
                'supported': bool(ratio_C < 0.3),
            }
            print(f"  Hypothesis C: Δλ ratio (with_cl / pure_Ebd) = {ratio_C:.3f}")
            if ratio_C < 0.3:
                print("  → Hypothesis C SUPPORTED (closure suppresses splitting)")
            else:
                print("  → Hypothesis C NOT SUPPORTED (closure does not suppress splitting)")

    # Save results
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq168_commensurability.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n=== RESULTS SAVED: {out_path} ===")

    # Summary
    print("\n" + "=" * 70)
    print("NQ-168 SUMMARY")
    print("=" * 70)
    F1_count = len(all_results)
    delta_all = [r['delta_lam'] for r in all_results if r['delta_lam'] is not None]
    if delta_all:
        print(f"F=1 minimizers found: {F1_count}")
        print(f"Δλ range: [{min(delta_all):.4e}, {max(delta_all):.4e}]")
        print(f"Δλ mean: {np.mean(delta_all):.4e}")
    if mean_delta_by_L:
        print(f"Δλ by L: {', '.join(f'L={k}:{v:.3e}' for k,v in sorted(mean_delta_by_L.items()))}")


if __name__ == "__main__":
    main()
