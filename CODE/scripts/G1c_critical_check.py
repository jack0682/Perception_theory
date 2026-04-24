"""G1c: Verify Theorem 2 (i) at L=16 — is F=1 disk critical of full SCC or not?"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd, grad_cl, grad_sep


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


def main():
    L = 16
    beta = 30.0
    alpha = 1.0
    c = 0.5
    graph = GraphState.grid_2d(L, L)

    # Find pure E_bd F=1 disk (centered)
    p_pure = ParameterRegistry(
        alpha_bd=alpha, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=5000,
    )

    # Use centered blob IC
    r0 = np.sqrt(c * L * L / np.pi)
    x_idx, y_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    r = np.sqrt((x_idx - L/2)**2 + (y_idx - L/2)**2).flatten()
    u_init = 0.5 * (1.0 - np.tanh((r - r0) / 1.0))

    res = find_formation(graph, p_pure, normalize=False, verbose=False, u_init=u_init)
    u_disk = res.u
    print(f"Pure E_bd L=16: F={count_local_maxima(u_disk, L)}, energy={res.energy:.3f}")

    # Check gradient under full SCC at u_disk
    p_full = ParameterRegistry(
        alpha_bd=alpha, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
    )
    g_bd = grad_bd(u_disk, graph, p_full)
    g_cl = grad_cl(u_disk, graph, p_full)
    g_sep = grad_sep(u_disk, graph, p_full)
    g_full = g_bd + g_cl + g_sep

    # Project to 1^perp
    g_bd_p = g_bd - g_bd.mean()
    g_cl_p = g_cl - g_cl.mean()
    g_sep_p = g_sep - g_sep.mean()
    g_full_p = g_full - g_full.mean()

    print(f"\n|| gradients at L=16 F=1 disk under full SCC ||:")
    print(f"  ||g_bd_proj||  = {np.linalg.norm(g_bd_p):.6f}  (should be ~0 for pure E_bd critical)")
    print(f"  ||g_cl_proj||  = {np.linalg.norm(g_cl_p):.6f}")
    print(f"  ||g_sep_proj|| = {np.linalg.norm(g_sep_p):.6f}")
    print(f"  ||g_full_proj||= {np.linalg.norm(g_full_p):.6f}")

    # cosine
    nc = np.linalg.norm(g_cl_p)
    ns = np.linalg.norm(g_sep_p)
    if nc > 1e-6 and ns > 1e-6:
        cos_cs = np.dot(g_cl_p, g_sep_p) / (nc * ns)
        print(f"  cos(g_cl, g_sep) = {cos_cs:.4f}")

    # Run full SCC from u_disk
    p_full_opt = ParameterRegistry(
        alpha_bd=alpha, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        n_restarts=1, max_iter=5000,
    )
    res_full = find_formation(graph, p_full_opt, normalize=False, verbose=False, u_init=u_disk)
    F_full = count_local_maxima(res_full.u, L)
    print(f"\nFull SCC from u_disk: F={F_full}, energy={res_full.energy:.3f}")
    print(f"  (Theorem 2 (ii) predicts F ≥ 2 if disk destabilized)")
    disp = np.linalg.norm(res_full.u - u_disk)
    print(f"  Displacement ||u_final - u_disk|| = {disp:.4f}")


if __name__ == "__main__":
    main()
