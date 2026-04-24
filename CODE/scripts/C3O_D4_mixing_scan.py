"""C3-O: D_4 correction mixing scaling — NQ-138.

In continuum (SO(2)) each angular ℓ produces 2-fold degenerate modes (cos/sin).
$D_4$ lattice breaks this into 1-dim irreps (B_1 ⊕ B_2 for ℓ=2, A_1 ⊕ A_2 for ℓ=4, etc.).

The splitting Δλ within the (cos ℓθ, sin ℓθ) doublet scales as (ξ_0/r_0)^k
for some k — to be determined empirically.

Test:
  1. Find F=1 center-aligned disk at L ∈ {10, 14, 18, 24}
  2. Compute Hessian spectrum
  3. Identify near-degenerate "bands" (groups with Δλ < 0.5)
  4. Measure intra-band splitting
  5. Fit log(Δλ) vs log(ξ_0/r_0)

Run: cd CODE && python3 scripts/C3O_D4_mixing_scan.py
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


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


def compute_hessian_pure_bd(u_star, graph, params, n_modes=12, eps=1e-4):
    """FD Hessian for pure E_bd, project to 1^perp, take lowest n_modes."""
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
    # sort ascending
    idx = np.argsort(eigvals)
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    return eigvals[:n_modes + 1], eigvecs[:, :n_modes + 1]


def find_bands(eigvals, tol=0.3):
    """Group near-degenerate eigenvalues into bands.

    Returns list of (start_idx, end_idx, mean_val) for each band.
    """
    bands = []
    i = 0
    while i < len(eigvals):
        j = i
        while j + 1 < len(eigvals) and eigvals[j+1] - eigvals[j] < tol:
            j += 1
        bands.append((i, j, float(np.mean(eigvals[i:j+1])), float(eigvals[j] - eigvals[i])))
        i = j + 1
    return bands


def find_F1_center_disk(L, beta=30.0, c=0.5, n_tries=15):
    graph = GraphState.grid_2d(L, L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=5000,
    )
    best = None
    r0 = np.sqrt(c * L * L / np.pi)
    for seed in range(n_tries):
        np.random.seed(seed * 11 + 5)
        # Centered blob IC
        i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        r = np.sqrt((i_idx - L/2)**2 + (j_idx - L/2)**2).flatten()
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / 1.0))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F = count_local_maxima(res.u, L)
                if F == 1 and (best is None or res.energy < best[1]):
                    best = (res.u, res.energy, graph, params)
        except Exception:
            pass
    return best


def main():
    print("=" * 70)
    print("C3-O: D_4 mixing scaling (NQ-138)")
    print("=" * 70)

    L_list = [10, 14, 18, 24]
    beta = 30.0
    alpha = 1.0
    c = 0.5
    xi_0 = np.sqrt(alpha / beta)
    print(f"ξ_0 = {xi_0:.4f}")

    results = []
    for L in L_list:
        print(f"\n--- L={L} ---")
        t0 = time.time()
        r_0 = np.sqrt(c * L * L / np.pi)

        found = find_F1_center_disk(L, beta=beta, c=c, n_tries=12)
        if found is None:
            print(f"  No F=1 center disk found at L={L}")
            continue
        u_disk, energy, graph, params = found
        F = count_local_maxima(u_disk, L)
        print(f"  F={F}, energy={energy:.3f}")

        eigvals, _ = compute_hessian_pure_bd(u_disk, graph, params, n_modes=16, eps=1e-4)
        bands = find_bands(eigvals, tol=0.3)

        print(f"  ξ_0/r_0 = {xi_0/r_0:.4f}")
        print(f"  Eigenvalues [0:12]: {[f'{e:.4f}' for e in eigvals[:12]]}")
        print(f"  Bands (tol=0.3):")
        for i, (si, ei, mval, span) in enumerate(bands[:6]):
            print(f"    Band {i}: idx[{si}:{ei+1}], mean={mval:.4f}, span={span:.4f}, n_modes={ei-si+1}")

        results.append({
            'L': L, 'F': F, 'energy': float(energy),
            'r_0': float(r_0), 'xi_0': float(xi_0),
            'xi_over_r': float(xi_0 / r_0),
            'eigs': [float(e) for e in eigvals.tolist()],
            'bands': [{'start': int(si), 'end': int(ei), 'mean': mval, 'span': span}
                      for (si, ei, mval, span) in bands[:8]],
            'runtime_sec': time.time() - t0,
        })

    # Extract splitting for each common band (e.g., band 1 if present in all)
    print("\n" + "=" * 70)
    print("Band-splitting scaling fit")
    print("=" * 70)
    # For each L, take band 1 (excluding tangent band 0)
    for band_idx in [1, 2, 3]:
        Ls_b = []
        spans_b = []
        xi_ovr_b = []
        means_b = []
        for r in results:
            if len(r['bands']) > band_idx:
                b = r['bands'][band_idx]
                if b['span'] > 1e-8:
                    Ls_b.append(r['L'])
                    spans_b.append(b['span'])
                    xi_ovr_b.append(r['xi_over_r'])
                    means_b.append(b['mean'])
        if len(Ls_b) >= 2:
            print(f"\n  Band {band_idx} splitting scaling:")
            for l, s, x, m in zip(Ls_b, spans_b, xi_ovr_b, means_b):
                print(f"    L={l}: mean={m:.4f}, span={s:.5f}, ξ_0/r_0={x:.5f}")
            # Log-log fit
            log_x = np.log(np.array(xi_ovr_b))
            log_s = np.log(np.array(spans_b))
            slope, intercept = np.polyfit(log_x, log_s, 1)
            print(f"    Fit: log(span) = {intercept:.3f} + {slope:.3f} * log(ξ_0/r_0)")
            print(f"    → span ~ (ξ_0/r_0)^{slope:.2f}")

    out = os.path.join(os.path.dirname(__file__), 'results', 'C3O_D4_mixing_scan.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'beta': beta, 'alpha': alpha, 'c': c,
                   'L_list': L_list, 'results': results}, f, indent=2)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
