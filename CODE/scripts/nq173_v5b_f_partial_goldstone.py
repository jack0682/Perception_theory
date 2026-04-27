"""NQ-173: V5b-F partial Goldstone characterization on boundary-modified graphs.

W4-04-26 NQ-170c flagged the V5b-F new finding (Cat C):
  free BC L=20 ζ ∈ {0.5, 1.0}: F=1 minimizers exhibit *partial* mode-agnostic
  Goldstone overlap (0.83 / 0.75) — between V5b-T sub-lattice (< 0.5) and
  super-lattice (> 0.9) prediction. Mechanism unclear.

This script tests three hypotheses for the V5b-F mechanism (W5 plan §3 Block 4):

  H1: Bulk-localized Goldstone — translation symmetry holds in interior, broken
      only near boundary. Test: bulk-only translation overlap (interior region
      restriction) > 0.95.

  H2: Mode mixing — eigenvector is linear combination
      eigvec ≈ α·(translation Goldstone) + β·(boundary-localized mode).
      Test: α coefficient measured by inner product, expected α ≈ 0.83
      (matches W4 04-26 NQ-170c overlap on free BC ζ=0.5).

  H3: PN barrier modification — full-space Goldstone with finite (not zero)
      Hessian eigenvalue due to boundary lifting. Test: spectral position
      (lowest non-tangent), λ small (< 0.1).

  H1+H2 mixed (a priori most likely per pre_brainstorm §2.3): both
  partially supported.

Setup:
  Graph: 2D free BC L=20.
  ζ ∈ {0.5, 0.7, 1.0} (3 values; ζ=0.7 added between V5b-T sub/super
       boundary for sweep coverage).
  Seeds: N=5 per ζ, multi-IC strategy (3 IC widths each).
  Total: 3 × 5 = 15 minimizers attempted; F=1 selected.

Per-minimizer measurements:
  - Mode mass spatial distribution: bulk_mass_fraction(eigvec, interior_band)
    with interior region 4 ≤ x,y ≤ 16 (per pre_brainstorm §2.4 wider definition).
  - Bulk-only translation overlap (interior-restricted norm).
  - Mode decomposition coefficients (α, β, γ) onto (δu_x, δu_y, complement).
  - Spectral position + eigenvalue.

Mode-agnostic detection (per W4-04-26 NQ-172 lesson + pre_brainstorm §8.4):
  Iterate over all 6 lowest non-tangent eigenmodes; record max overlap.
  Do NOT hardcode `mode_overlaps[1]` or any specific mode index.

Run: cd CODE && python3 scripts/nq173_v5b_f_partial_goldstone.py
Output: scripts/results/nq173_v5b_f.json

Expected runtime: ~10-15 min for 15 minimizers (similar to NQ-170c).
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


# === Graph constructor ===

def build_free_bc_2d(L):
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L:
                    rows.append(idx); cols.append(ni * L + nj)
    return GraphState(sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))), n


# === F count ===

def count_local_maxima_free_bc(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            neighbors = []
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L:
                    neighbors.append(g[ni, nj])
            if all(nv < v for nv in neighbors):
                F += 1
    return F


# === Translation modes (free BC: forward differences with zero-padding at last row/col) ===

def translation_modes_free_bc(u, L):
    g = u.reshape(L, L)
    du_x = np.zeros((L, L))
    du_x[:-1, :] = g[1:, :] - g[:-1, :]
    du_y = np.zeros((L, L))
    du_y[:, :-1] = g[:, 1:] - g[:, :-1]
    out = []
    for name, m in [('x', du_x.flatten()), ('y', du_y.flatten())]:
        norm = np.linalg.norm(m)
        out.append((name, m / norm if norm > 1e-14 else m))
    return out


# === V5b-F-specific analysis ===

def bulk_mask(L, interior_band):
    """Boolean mask for interior vertices: interior_band <= x,y < L - interior_band."""
    mask = np.zeros((L, L), dtype=bool)
    mask[interior_band:L - interior_band, interior_band:L - interior_band] = True
    return mask.flatten()


def bulk_mass_fraction(eigvec, L, interior_band):
    """Fraction of mode mass (squared, normalized) inside interior band."""
    mask = bulk_mask(L, interior_band)
    bulk_mass = float(np.sum(eigvec[mask]**2))
    total_mass = float(np.sum(eigvec**2))
    return bulk_mass / total_mass if total_mass > 1e-14 else 0.0


def bulk_only_translation_overlap(eigvec, u, L, interior_band):
    """Compute mode-agnostic Goldstone overlap restricted to interior region.

    Restrict both the eigenvector AND the translation modes (δu_x, δu_y) to the
    interior bulk region, re-normalize, then compute |<eigvec_bulk, du_bulk>|.
    """
    mask = bulk_mask(L, interior_band)
    # Build translation modes from u
    g = u.reshape(L, L)
    du_x_full = np.zeros((L, L))
    du_x_full[:-1, :] = g[1:, :] - g[:-1, :]
    du_y_full = np.zeros((L, L))
    du_y_full[:, :-1] = g[:, 1:] - g[:, :-1]
    du_x_bulk = du_x_full.flatten()[mask]
    du_y_bulk = du_y_full.flatten()[mask]
    eigvec_bulk = eigvec[mask]

    def safe_overlap(a, b):
        na = np.linalg.norm(a)
        nb = np.linalg.norm(b)
        if na < 1e-14 or nb < 1e-14:
            return 0.0
        return float(abs(np.dot(a, b) / (na * nb)))

    ov_x = safe_overlap(eigvec_bulk, du_x_bulk)
    ov_y = safe_overlap(eigvec_bulk, du_y_bulk)
    return max(ov_x, ov_y), ov_x, ov_y


def mode_decomposition(eigvec, du_x, du_y):
    """Decompose eigvec into (α·du_x + β·du_y) + γ·complement.

    α, β: projection coefficients onto (already-normalized) translation basis.
    γ: residual norm (complement to translation subspace).
    Returns (α, β, γ) with α²+β²+γ² = 1 ideally (after normalization).
    """
    # Orthonormalize du_x, du_y first (Gram-Schmidt)
    dux_n = du_x / (np.linalg.norm(du_x) + 1e-14)
    duy_orth = du_y - np.dot(du_y, dux_n) * dux_n
    duy_n = duy_orth / (np.linalg.norm(duy_orth) + 1e-14)

    # Project eigvec
    alpha = float(np.dot(eigvec, dux_n))
    beta = float(np.dot(eigvec, duy_n))
    complement = eigvec - alpha * dux_n - beta * duy_n
    gamma = float(np.linalg.norm(complement))

    # Normalize so α²+β²+γ² = 1
    total = np.sqrt(alpha**2 + beta**2 + gamma**2)
    if total > 1e-14:
        return alpha / total, beta / total, gamma / total
    return 0.0, 0.0, 0.0


# === Hessian computation (reused from NQ-170c pattern) ===

def compute_hessian_lowest(u_star, graph, params, n_modes=6, eps=1e-4):
    n = graph.n if hasattr(graph, 'n') else u_star.shape[0]
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


# === Find F=1 minimizer (multi-IC) ===

def find_F1_minimizer_free_bc(L, beta, c, seed):
    graph, n = build_free_bc_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    ic_widths = [max(xi_0, 0.2), xi_0 * 0.5, xi_0 * 2.0]

    attempts = []
    for ic_id in range(3):
        np.random.seed(seed * 53 + 13 + ic_id * 1000)
        cx = np.random.uniform(0.5, L - 0.5)
        cy = np.random.uniform(0.5, L - 0.5)
        i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        dx = np.abs(i_idx - cx)
        dy = np.abs(j_idx - cy)
        r = np.sqrt(dx**2 + dy**2).flatten()

        u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_widths[ic_id]))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=n), 0.01, 0.99)

        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if not res.converged:
                continue
            F = count_local_maxima_free_bc(res.u, L)
            attempts.append({'F': F, 'energy': float(res.energy), 'u': res.u, 'ic_id': ic_id})
        except Exception:
            continue

    if not attempts:
        return None
    f1 = [a for a in attempts if a['F'] == 1]
    best = min(f1, key=lambda a: a['energy']) if f1 else min(attempts, key=lambda a: (a['F'], a['energy']))
    best['F1_found'] = bool(f1)
    best['graph'] = graph
    best['params'] = params
    best['n'] = n
    best['attempts_F'] = [a['F'] for a in attempts]
    return best


# === Per-minimizer V5b-F analysis ===

def analyze_v5b_f(result, L, zeta):
    """Test H1/H2/H3 for a single F=1 minimizer."""
    u = result['u']
    graph = result['graph']
    params = result['params']
    n = result['n']

    # Translation modes (full-space)
    trans_modes_full = translation_modes_free_bc(u, L)
    tangent = np.ones(n) / np.sqrt(n)

    # Hessian + lowest 6 modes
    eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=6)

    # Reconstruct un-normalized translation modes for mode_decomposition
    g = u.reshape(L, L)
    du_x_full = np.zeros((L, L))
    du_x_full[:-1, :] = g[1:, :] - g[:-1, :]
    du_y_full = np.zeros((L, L))
    du_y_full[:, :-1] = g[:, 1:] - g[:, :-1]
    du_x_unnorm = du_x_full.flatten()
    du_y_unnorm = du_y_full.flatten()

    interior_band = 4  # Per pre_brainstorm §2.4: wider interior 4 ≤ x,y ≤ 16 (12×12 = 144 sites)

    mode_data = []
    best_goldstone_idx = -1
    best_goldstone_overlap = -1.0

    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]

        # Skip if it's the volume tangent (large overlap with 1/√n)
        ov_t = float(abs(np.dot(v, tangent)))
        if ov_t > 0.5:
            continue

        # Full-space mode-agnostic Goldstone overlap
        overlaps_full = {f'overlap_full_{name}': float(abs(np.dot(v, m)))
                         for name, m in trans_modes_full}
        max_overlap_full = max(overlaps_full.values())

        # H1: bulk_mass_fraction
        bmf = bulk_mass_fraction(v, L, interior_band)

        # H1: bulk_only_translation_overlap
        max_overlap_bulk, ov_x_bulk, ov_y_bulk = bulk_only_translation_overlap(
            v, u, L, interior_band)

        # H2: mode_decomposition (alpha, beta, gamma)
        alpha, beta, gamma = mode_decomposition(v, du_x_unnorm, du_y_unnorm)

        # Track best Goldstone candidate (highest full-space overlap)
        if max_overlap_full > best_goldstone_overlap:
            best_goldstone_overlap = max_overlap_full
            best_goldstone_idx = k

        mode_data.append({
            'mode_idx': k,
            'eigenvalue': float(eigvals[k]),
            'ov_tangent': ov_t,
            'max_overlap_full': max_overlap_full,
            'overlaps_full': overlaps_full,
            'max_overlap_bulk': max_overlap_bulk,
            'ov_x_bulk': ov_x_bulk,
            'ov_y_bulk': ov_y_bulk,
            'bulk_mass_fraction': bmf,
            'mode_decomp_alpha': alpha,
            'mode_decomp_beta': beta,
            'mode_decomp_gamma': gamma,
            'alpha2_plus_beta2': alpha**2 + beta**2,
        })

    # Goldstone candidate selection: mode with max full-space overlap (mode-agnostic)
    if mode_data:
        best_data = next((md for md in mode_data if md['mode_idx'] == best_goldstone_idx), None)
    else:
        best_data = None

    return {
        'L': L,
        'zeta': float(zeta),
        'F1_found': result['F1_found'],
        'energy': float(result['energy']),
        'attempts_F': result['attempts_F'],
        'all_modes': mode_data,
        'goldstone_candidate': best_data,
        'interior_band_used': interior_band,
    }


# === Main sweep ===

def main():
    L = 20
    c = 0.10  # volume fraction
    zetas = [0.5, 0.7, 1.0]
    n_seeds = 5
    results = []
    t0 = time.time()

    for zeta in zetas:
        # ζ = ξ_0 / a, ξ_0 = sqrt(1/β), a = 1 ⟹ β = 1/ζ²
        beta = 1.0 / zeta**2
        for seed in range(n_seeds):
            print(f"[ζ={zeta} seed={seed}] β={beta:.3f} starting...")
            res = find_F1_minimizer_free_bc(L, beta, c, seed)
            if res is None:
                print(f"  FAIL: no minimizer found")
                results.append({
                    'zeta': float(zeta),
                    'seed': seed,
                    'beta': float(beta),
                    'status': 'failed',
                })
                continue
            analysis = analyze_v5b_f(res, L, zeta)
            analysis['seed'] = seed
            analysis['beta'] = float(beta)
            analysis['status'] = 'ok'
            best = analysis['goldstone_candidate']
            if best is not None:
                print(f"  F1={analysis['F1_found']} mode_idx={best['mode_idx']} "
                      f"λ={best['eigenvalue']:.3e} max_ov_full={best['max_overlap_full']:.3f} "
                      f"max_ov_bulk={best['max_overlap_bulk']:.3f} "
                      f"bmf={best['bulk_mass_fraction']:.3f} "
                      f"α²+β²={best['alpha2_plus_beta2']:.3f}")
            results.append(analysis)

    elapsed = time.time() - t0
    print(f"\nTotal elapsed: {elapsed:.1f}s for {len(zetas)*n_seeds} attempts")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'nq173_v5b_f.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'L': L, 'c': c, 'zetas': zetas, 'n_seeds': n_seeds,
                'graph_class': '2D_free_BC',
                'interior_band': 4,
                'elapsed_s': elapsed,
                'mode_agnostic': True,
                'no_mode_index_hardcode': True,
                'description': 'V5b-F partial Goldstone characterization (H1/H2/H3 test, NQ-173)',
            },
            'results': results,
        }, f, indent=2, default=lambda o: float(o) if hasattr(o, 'item') else str(o))
    print(f"\nWrote {out_path}")


if __name__ == '__main__':
    main()
