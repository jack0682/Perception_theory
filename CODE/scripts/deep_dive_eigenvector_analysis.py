"""Deep Dive Phase 1+2+3: Combined rigorous analysis.

(1) Eigenvector projection onto translation vs Fiedler directions
    — decisively identify near-zero mode's nature

(2) Decoupled large-L test
    — at L=40 torus, all tested ζ have β/β_crit >> 1
    — if genuine Goldstone exists, should observe 2-fold near-zero doublet

(3) Critical scaling analysis
    — scan β near β_crit at fixed L
    — extract exponent: λ_0 ~ (β - β_crit)^ν

Run: cd CODE && python3 scripts/deep_dive_eigenvector_analysis.py
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
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
    data = np.ones(len(rows))
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def count_local_maxima_torus(u, L):
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


def compute_hessian_spectrum_and_vectors(u_star, graph, params, n_modes=6, eps=1e-4):
    """Full eigendecomposition."""
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
    return eigvals[idx], eigvecs[:, idx]


def find_torus_F1(L, beta, c=0.5, n_tries=15):
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=10000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    ic_width = max(xi_0, 0.3)
    best = None
    for seed in range(n_tries):
        np.random.seed(seed * 23 + 1)
        cx = np.random.uniform(0, L)
        cy = np.random.uniform(0, L)
        i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        r = np.sqrt(dx**2 + dy**2).flatten()
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_width))
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


def translation_mode(u, L, direction='x'):
    """Compute δu_x = u(· + e1) - u on torus, or δu_y."""
    g = u.reshape(L, L)
    if direction == 'x':
        shifted = np.roll(g, -1, axis=0)
    else:
        shifted = np.roll(g, -1, axis=1)
    delta = (shifted - g).flatten()
    # Project to 1^perp
    delta -= delta.mean()
    return delta


def get_fiedler_modes(graph, L, k=4):
    """Get first k Laplacian eigenvectors (non-trivial)."""
    L_mat = graph.L.astype(np.float64)
    try:
        eigvals, eigvecs = spla.eigsh(L_mat, k=k+1, which='SM')
    except Exception:
        return None, None
    # First eigenvalue should be ~0 (constant). Skip.
    idx = np.argsort(eigvals)
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    return eigvals[1:k+1], eigvecs[:, 1:k+1]


def projection_analysis(u_disk, graph, params, L, n_modes=6):
    """Analyze eigenvector overlaps with translation/Fiedler directions."""
    eigvals, eigvecs = compute_hessian_spectrum_and_vectors(u_disk, graph, params, n_modes=n_modes)
    # Skip tangent (eigvals[0])
    low_vals = eigvals[1:n_modes+1]
    low_vecs = eigvecs[:, 1:n_modes+1]

    # Translation modes
    dux = translation_mode(u_disk, L, 'x')
    duy = translation_mode(u_disk, L, 'y')
    dux /= np.linalg.norm(dux) + 1e-12
    duy /= np.linalg.norm(duy) + 1e-12

    # Fiedler-like modes (lowest Laplacian eigenvectors)
    L_eigvals, L_eigvecs = get_fiedler_modes(graph, L, k=6)

    # For each eigenmode of H, compute overlap with dux, duy, and Laplacian modes
    print(f"\n  Eigenvector analysis (low {n_modes} modes above tangent):")
    print(f"  {'k':>3} {'λ_k':>10} {'|<φ_k,δu_x>|':>14} {'|<φ_k,δu_y>|':>14} {'|<φ_k,Fied1>|':>14} {'|<φ_k,Fied2>|':>14}")
    data = []
    for k in range(min(n_modes, len(low_vals))):
        vec = low_vecs[:, k] / (np.linalg.norm(low_vecs[:, k]) + 1e-12)
        ovx = abs(np.dot(vec, dux))
        ovy = abs(np.dot(vec, duy))
        ovLs = []
        if L_eigvecs is not None:
            for l in range(min(2, L_eigvecs.shape[1])):
                L_vec = L_eigvecs[:, l]
                L_vec = L_vec - L_vec.mean()
                L_vec = L_vec / (np.linalg.norm(L_vec) + 1e-12)
                ovLs.append(abs(np.dot(vec, L_vec)))
        print(f"  {k:>3} {low_vals[k]:>10.4e} {ovx:>14.4f} {ovy:>14.4f} "
              f"{ovLs[0] if len(ovLs)>0 else 0.0:>14.4f} "
              f"{ovLs[1] if len(ovLs)>1 else 0.0:>14.4f}")
        data.append({
            'k': int(k),
            'eigval': float(low_vals[k]),
            'overlap_dux': float(ovx),
            'overlap_duy': float(ovy),
            'overlap_fied1': float(ovLs[0]) if len(ovLs) > 0 else 0.0,
            'overlap_fied2': float(ovLs[1]) if len(ovLs) > 1 else 0.0,
        })

    # Check if lowest mode is dominated by translation (Goldstone) or Fiedler (critical)
    m = data[0]
    max_trans = max(m['overlap_dux'], m['overlap_duy'])
    max_fied = max(m['overlap_fied1'], m['overlap_fied2'])
    if max_trans > 0.7:
        verdict = f"TRANSLATION-dominant ({max_trans:.2f}) → Goldstone-like"
    elif max_fied > 0.7:
        verdict = f"FIEDLER-dominant ({max_fied:.2f}) → Critical/Fiedler-soft"
    elif max_trans > max_fied + 0.2:
        verdict = f"More translation ({max_trans:.2f} vs {max_fied:.2f}) → leaning Goldstone"
    elif max_fied > max_trans + 0.2:
        verdict = f"More Fiedler ({max_fied:.2f} vs {max_trans:.2f}) → leaning critical"
    else:
        verdict = f"Mixed (trans {max_trans:.2f}, Fied {max_fied:.2f})"
    print(f"  → LOWEST MODE VERDICT: {verdict}")
    return data, verdict


# ==================== PHASE 1: L=16 eigenvector analysis ====================
def phase1_L16_eigenvector():
    print("="*70)
    print("PHASE 1: L=16 eigenvector projection (identify soft mode)")
    print("="*70)

    L = 16
    c = 0.5
    zetas = [0.2, 0.5, 0.8, 1.0]
    results = []
    for zeta in zetas:
        beta = 1.0 / zeta**2
        beta_crit = 4 * 2 * (1 - np.cos(2*np.pi/L))
        if beta < beta_crit * 1.05:
            print(f"\n  ζ={zeta}: β={beta:.3f} < β_crit={beta_crit:.3f}, skipping")
            continue
        print(f"\n--- L={L}, ζ={zeta:.2f}, β={beta:.3f}, β/β_crit={beta/beta_crit:.2f} ---")
        found = find_torus_F1(L, beta, c=c, n_tries=10)
        if found is None:
            print(f"  No F=1 disk")
            continue
        u_disk, energy, graph, params = found
        print(f"  F=1 disk, energy={energy:.3f}")
        data, verdict = projection_analysis(u_disk, graph, params, L, n_modes=5)
        results.append({
            'L': L, 'zeta': zeta, 'beta': beta, 'beta_crit': float(beta_crit),
            'beta_over_crit': float(beta / beta_crit),
            'energy': float(energy),
            'projections': data,
            'verdict': verdict,
        })
    return results


# ==================== PHASE 2: L=40 decoupled test ====================
def phase2_L40_decoupled():
    print("\n" + "="*70)
    print("PHASE 2: L=40 decoupled test (β/β_crit >> 1 for all ζ)")
    print("="*70)

    L = 40
    c = 0.5
    beta_crit = 4 * 2 * (1 - np.cos(2*np.pi/L))  # ~ 0.049
    print(f"β_crit (L=40) = {beta_crit:.4f}")

    # Choose β values that give various ζ while β/β_crit >> 1
    # At L=40, with β=1.0: ζ=1, β/β_crit = 20 (decoupled!)
    # With β=0.25: ζ=2, β/β_crit = 5 (still OK)
    zetas_test = [0.5, 0.8, 1.0, 1.5]
    results = []
    for zeta in zetas_test:
        beta = 1.0 / zeta**2
        bc_ratio = beta / beta_crit
        if bc_ratio < 3:
            print(f"\n  ζ={zeta}: β/β_crit={bc_ratio:.2f} < 3, skipping (too close to critical)")
            continue
        print(f"\n--- L={L}, ζ={zeta:.2f}, β={beta:.3f}, β/β_crit={bc_ratio:.2f} ---")
        t0 = time.time()
        found = find_torus_F1(L, beta, c=c, n_tries=8)
        if found is None:
            print(f"  No F=1 disk")
            continue
        u_disk, energy, graph, params = found
        print(f"  F=1 disk, energy={energy:.3f}, runtime_minimizer={time.time()-t0:.1f}s")
        t1 = time.time()
        data, verdict = projection_analysis(u_disk, graph, params, L, n_modes=5)
        print(f"  Hessian+projection runtime: {time.time()-t1:.1f}s")
        results.append({
            'L': L, 'zeta': zeta, 'beta': beta, 'beta_crit': float(beta_crit),
            'beta_over_crit': float(bc_ratio),
            'energy': float(energy),
            'projections': data,
            'verdict': verdict,
        })
    return results


# ==================== PHASE 3: Critical scaling at L=16 ====================
def phase3_critical_scaling():
    """Scan β near β_crit (L=16) to extract exponent of λ_0 ~ (β - β_crit)^ν."""
    print("\n" + "="*70)
    print("PHASE 3: Critical scaling near β_crit at L=16")
    print("="*70)

    L = 16
    c = 0.5
    beta_crit = 4 * 2 * (1 - np.cos(2*np.pi/L))  # ~ 0.609
    print(f"β_crit (L=16) = {beta_crit:.4f}")

    # β ranges: 1.5·β_crit, 2·β_crit, 3·β_crit, 5·β_crit, 10·β_crit
    ratios = [1.5, 2.0, 3.0, 5.0, 10.0]
    betas = [r * beta_crit for r in ratios]

    results = []
    for r_c, beta in zip(ratios, betas):
        print(f"\n--- β={beta:.3f}, β/β_crit={r_c}")
        t0 = time.time()
        found = find_torus_F1(L, beta, c=c, n_tries=10)
        if found is None:
            print(f"  No F=1 disk")
            continue
        u_disk, energy, graph, params = found
        eigvals, _ = compute_hessian_spectrum_and_vectors(u_disk, graph, params, n_modes=5)
        lam_0 = float(eigvals[1])
        lam_1 = float(eigvals[2])
        beta_minus_crit = beta - beta_crit
        print(f"  λ_0={lam_0:.4e}, λ_1={lam_1:.4e}, β-β_crit={beta_minus_crit:.3f}")
        results.append({
            'beta': beta, 'beta_crit': float(beta_crit),
            'beta_over_crit': float(r_c),
            'beta_minus_crit': float(beta_minus_crit),
            'lam_0': lam_0, 'lam_1': lam_1,
            'energy': float(energy),
        })

    # Extract exponent: log(λ_0) = ν·log(β - β_crit) + const
    if len(results) >= 3:
        bmc = np.array([r['beta_minus_crit'] for r in results])
        lam0 = np.array([r['lam_0'] for r in results])
        mask = (bmc > 0) & (lam0 > 0)
        if mask.sum() >= 3:
            log_bmc = np.log(bmc[mask])
            log_lam = np.log(lam0[mask])
            slope, intercept = np.polyfit(log_bmc, log_lam, 1)
            print(f"\n  Fit: log(λ_0) = {intercept:.3f} + {slope:.3f} × log(β - β_crit)")
            print(f"  → λ_0 ~ (β - β_crit)^{slope:.3f}")
            print(f"  Landau mean-field prediction: ν = 1")
            print(f"  Result {'consistent' if 0.8 < slope < 1.2 else 'deviates'} with Landau ν=1")
    return results


def main():
    print("\n" + "#"*70)
    print("# DEEP DIVE: 3-phase rigorous analysis")
    print("#"*70)

    t0 = time.time()

    r1 = phase1_L16_eigenvector()
    r3 = phase3_critical_scaling()  # Relatively cheap
    r2 = phase2_L40_decoupled()  # Most expensive

    out = os.path.join(os.path.dirname(__file__), 'results', 'deep_dive_analysis.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'phase1': r1, 'phase2': r2, 'phase3': r3}, f, indent=2)

    print(f"\nTotal runtime: {time.time() - t0:.1f}s")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
