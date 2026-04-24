"""C3-T: Torus exact Goldstone direct test.

Theorem 1 case T (revised): on torus T_L = (Z/L)^2 with periodic BC, translation
is exact automorphism. Single disk minimizer should have λ_0 << λ_1 (exact
Goldstone; up to Peierls-Nabarro lattice correction).

Test:
  1. Build torus graph (periodic 2D L×L)
  2. Find pure E_bd F=1 minimizer
  3. Compute full Hessian spectrum (pure E_bd)
  4. Check λ_0/λ_1 ratio << 1
  5. L-scan to check Peierls-Nabarro scaling λ_0 ~ exp(-c * r_0 / a)

Note: on torus, translation produces DEGENERATE minima (discrete orbit).
Continuous limit: exact zero modes. Discrete: Peierls-Nabarro barrier.

Expected: λ_0/λ_1 << 0.1 (vs G1 center-aligned free-BC: ratio ~0.999).

Run: cd CODE && python3 scripts/C3T_torus_goldstone.py
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
    """Build L×L torus graph (periodic BC in both directions)."""
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            # 4-connectivity with periodic BC
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di) % L, (j + dj) % L
                nidx = ni * L + nj
                rows.append(idx)
                cols.append(nidx)
    data = np.ones(len(rows))
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def count_local_maxima_torus(u, L):
    """Local maxima on torus (periodic BC)."""
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di) % L, (j + dj) % L
                if g[ni, nj] >= v:
                    ok = False
                    break
            if ok:
                F += 1
    return F


def com_torus(u, L):
    """COM on torus (modular arithmetic via circular mean)."""
    g = u.reshape(L, L)
    total = g.sum()
    if total < 1e-6:
        return L/2, L/2
    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    # Circular mean
    angle_i = 2 * np.pi * i_idx / L
    angle_j = 2 * np.pi * j_idx / L
    mean_cos_i = (g * np.cos(angle_i)).sum() / total
    mean_sin_i = (g * np.sin(angle_i)).sum() / total
    mean_cos_j = (g * np.cos(angle_j)).sum() / total
    mean_sin_j = (g * np.sin(angle_j)).sum() / total
    ci = np.arctan2(mean_sin_i, mean_cos_i) * L / (2 * np.pi) % L
    cj = np.arctan2(mean_sin_j, mean_cos_j) * L / (2 * np.pi) % L
    return float(ci), float(cj)


def compute_hessian_spectrum_pure_bd(u_star, graph, params, n_modes=6, eps=1e-4):
    """FD Hessian for pure E_bd, then project to 1^perp, take lowest n_modes."""
    n = graph.n
    g0 = grad_bd(u_star, graph, params)

    H = np.zeros((n, n))
    for i in range(n):
        u_p = u_star.copy()
        u_p[i] += eps
        g_p = grad_bd(u_p, graph, params)
        H[:, i] = (g_p - g0) / eps
    H = (H + H.T) / 2.0

    # Project to 1^perp
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = P @ H @ P

    eigvals = np.linalg.eigvalsh(H_proj)
    eigvals.sort()
    return eigvals[:n_modes + 1]  # include tangent


def find_torus_disk(L, beta=30.0, c=0.5, n_tries=20):
    """Find F=1 torus disk minimizer."""
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=5000,
    )
    best = None
    r0 = np.sqrt(c * L * L / np.pi)
    for seed in range(n_tries):
        np.random.seed(seed * 17 + 3)
        # Random position blob IC
        cx = np.random.uniform(0, L)
        cy = np.random.uniform(0, L)
        i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        # Torus distance
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        r = np.sqrt(dx**2 + dy**2).flatten()
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / 1.0))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F = count_local_maxima_torus(res.u, L)
                if F == 1 and (best is None or res.energy < best[1]):
                    best = (res.u, res.energy, graph, params)
        except Exception:
            pass
    return best


def main():
    print("=" * 70)
    print("C3-T: Torus exact Goldstone test")
    print("=" * 70)

    L_list = [8, 12, 16]
    beta = 30.0
    alpha = 1.0
    c = 0.5
    xi_0 = np.sqrt(alpha / beta)
    print(f"ξ_0 = {xi_0:.4f}")

    results = []
    for L in L_list:
        print(f"\n--- L={L} torus ---")
        t0 = time.time()
        r0 = np.sqrt(c * L * L / np.pi)
        found = find_torus_disk(L, beta=beta, c=c, n_tries=15)
        if found is None:
            print(f"  No F=1 torus minimizer found.")
            continue
        u_disk, energy, graph, params = found
        F = count_local_maxima_torus(u_disk, L)
        ci, cj = com_torus(u_disk, L)
        print(f"  F={F}, energy={energy:.3f}, COM=({ci:.2f},{cj:.2f})")

        print(f"  Computing Hessian spectrum (pure E_bd, n={L*L})...")
        eigs = compute_hessian_spectrum_pure_bd(u_disk, graph, params, n_modes=8, eps=1e-4)
        print(f"  Eigenvalues [0:8]: {[f'{e:.5f}' for e in eigs[:8]]}")

        # eigs[0] = tangent (~0), eigs[1] = Mode 0 (Goldstone candidate)
        lam_t = eigs[0]
        lam_0 = eigs[1]  # lowest non-tangent
        lam_1 = eigs[2] if len(eigs) > 2 else None
        lam_2 = eigs[3] if len(eigs) > 3 else None

        print(f"  λ_tangent = {lam_t:.6f} (should be ~0)")
        print(f"  λ_0 = {lam_0:.6f}")
        if lam_1:
            print(f"  λ_1 = {lam_1:.6f}")
            ratio = lam_0 / lam_1
            print(f"  λ_0 / λ_1 = {ratio:.4f}")
        if lam_2:
            print(f"  λ_2 = {lam_2:.6f}")
            ratio_02 = lam_0 / lam_2
            print(f"  λ_0 / λ_2 = {ratio_02:.4f}")

        # Torus: translation in x and y both produce Goldstone-like modes.
        # So eigs[1] and eigs[2] should BOTH be small (2 Goldstone modes).
        # Then eigs[3] is first orbital. Check:
        if lam_2 and lam_1:
            # λ_0, λ_1 should be near-equal (two Goldstone modes)
            print(f"  Symmetry check λ_0 vs λ_1 (should be ≈ if two Goldstone): " +
                  f"|diff|/mean = {abs(lam_0 - lam_1)/((lam_0 + lam_1)/2):.3f}")

        t = time.time() - t0
        print(f"  Runtime: {t:.1f}s")

        results.append({
            'L': L, 'F': F, 'energy': float(energy),
            'com': [ci, cj], 'r_0': float(r0), 'xi_0': float(xi_0),
            'eigs': [float(e) for e in eigs.tolist()],
            'lam_tangent': float(lam_t),
            'lam_0': float(lam_0),
            'lam_1': float(lam_1) if lam_1 else None,
            'lam_2': float(lam_2) if lam_2 else None,
            'ratio_01': float(lam_0 / lam_1) if lam_1 and lam_1 > 1e-10 else None,
            'ratio_02': float(lam_0 / lam_2) if lam_2 and lam_2 > 1e-10 else None,
            'runtime_sec': t,
        })

    # Peierls-Nabarro scaling check
    if len(results) >= 2:
        print("\n" + "=" * 70)
        print("Peierls-Nabarro scaling: λ_0 vs r_0 (or L)")
        print("=" * 70)
        for r in results:
            print(f"  L={r['L']}: r_0={r['r_0']:.2f}, λ_0={r['lam_0']:.5f}, "
                  f"λ_0/λ_2={r.get('ratio_02', 'NA')}")

        Ls = np.array([r['L'] for r in results])
        lam_0s = np.array([r['lam_0'] for r in results])
        if all(lam_0s > 1e-10):
            # Fit log λ_0 vs L (or -r_0)
            log_l = np.log(lam_0s)
            r_0s = np.array([r['r_0'] for r in results])
            slope_r, _ = np.polyfit(r_0s, log_l, 1) if len(r_0s) > 1 else (None, None)
            if slope_r is not None:
                print(f"  log(λ_0) vs r_0 slope: {slope_r:.4f}")
                print(f"  PN prediction: negative slope (λ_0 decays exponentially with r_0)")

    # Save
    out = os.path.join(os.path.dirname(__file__), 'results', 'C3T_torus_goldstone.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'beta': beta, 'alpha': alpha, 'c': c,
                   'L_list': L_list, 'xi_0': float(xi_0), 'results': results}, f, indent=2)
    print(f"\nSaved: {out}")

    # Summary
    print("\n" + "=" * 70)
    print("C3-T SUMMARY")
    print("=" * 70)
    print("Theorem 1 case T (torus) prediction: λ_0 << λ_1 (two Goldstone + first orbital).")
    for r in results:
        ratio = r.get('ratio_02')
        if ratio is not None:
            if ratio < 0.1:
                verdict = "✓ EXACT GOLDSTONE"
            elif ratio < 0.5:
                verdict = "~ partial"
            else:
                verdict = "✗ no Goldstone"
        else:
            verdict = "— insufficient"
        print(f"  L={r['L']}: λ_0/λ_2 = {ratio} → {verdict}")


if __name__ == "__main__":
    main()
