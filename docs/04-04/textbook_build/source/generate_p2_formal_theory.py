#!/usr/bin/env python3
"""Generate Part 2 (Formal Theory) figures for the SCC textbook.

Produces ~25 figures: closure convergence, double-well, energy terms,
energy landscape, bifurcation, spectral universality.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D

from scc import GraphState, ParameterRegistry, find_formation, closure, distinction
from scc.energy import (EnergyComputer, double_well, double_well_deriv,
                         double_well_second_deriv, energy_cl, energy_sep, energy_bd)
from scc.diagnostics import bind_predicate, sep_predicate, inside_predicate
from scc.operators import aggregation

OUT = os.path.join(os.path.dirname(__file__), '..', 'figures', 'P2_formal')
os.makedirs(OUT, exist_ok=True)

FIGW = 170 / 25.4
DPI = 300

def savefig(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f"  ✓ {name}")

def field_to_grid(u, rows, cols):
    return u.reshape(rows, cols)

# ================================================================
# Fig 1-3: Closure convergence frames
# ================================================================
def fig_closure_convergence():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    rng = np.random.default_rng(42)
    u = np.clip(rng.uniform(0.1, 0.9, g.n), 0, 1)

    frames = [('u₀ (initial)', u.copy())]
    for k in range(1, 21):
        u = closure(u, g, p)
        if k in [1, 3, 5, 10, 20]:
            frames.append((f'Cl^{k}(u₀)', u.copy()))

    # Individual frames
    for i, (label, u_frame) in enumerate(frames):
        fig, ax = plt.subplots(figsize=(FIGW * 0.35, FIGW * 0.35))
        u_grid = field_to_grid(u_frame, 10, 10)
        im = ax.imshow(u_grid, cmap='viridis', vmin=0, vmax=1, origin='lower', interpolation='nearest')
        ax.set_title(label, fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)
        savefig(fig, f'closure_convergence_frame{i+1}.pdf')

    # Combined strip
    fig, axes = plt.subplots(1, len(frames), figsize=(FIGW, FIGW * 0.2))
    for i, (label, u_frame) in enumerate(frames):
        im = axes[i].imshow(field_to_grid(u_frame, 10, 10), cmap='viridis',
                            vmin=0, vmax=1, origin='lower', interpolation='nearest')
        axes[i].set_title(label, fontsize=7)
        axes[i].set_xticks([]); axes[i].set_yticks([])
    fig.suptitle('Closure Operator Convergence: Cl^k(u₀)', fontsize=11, y=1.05)
    fig.subplots_adjust(right=0.9)
    cax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    plt.colorbar(im, cax=cax, label='u(x)')
    savefig(fig, 'closure_convergence_strip.pdf')

    # Convergence rate plot
    g2 = GraphState.grid_2d(10, 10)
    u_test = np.clip(rng.uniform(0.1, 0.9, g2.n), 0, 1)
    residuals = []
    for k in range(30):
        u_next = closure(u_test, g2, p)
        residuals.append(np.linalg.norm(u_next - u_test))
        u_test = u_next
    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.35))
    ax.semilogy(range(len(residuals)), residuals, 'o-', markersize=3, color='#1f77b4')
    ax.set_xlabel('Iteration k')
    ax.set_ylabel('‖Cl^{k+1}(u) − Cl^k(u)‖')
    ax.set_title('Closure Contraction Rate (a_cl = 3.5 < 4)')
    ax.grid(True, alpha=0.3)
    savefig(fig, 'closure_contraction_rate.pdf')

# ================================================================
# Fig 4: Double-well W(u) = u²(1-u)²
# ================================================================
def fig_double_well():
    u = np.linspace(0, 1, 500)
    W = double_well(u)
    Wp = double_well_deriv(u)

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.85, FIGW * 0.32))

    axes[0].plot(u, W, 'b-', linewidth=2)
    axes[0].set_xlabel('u')
    axes[0].set_ylabel('W(u)')
    axes[0].set_title('Double-Well: W(u) = u²(1−u)²')
    axes[0].axvline(x=0, color='red', linestyle=':', alpha=0.5, label='Minima')
    axes[0].axvline(x=1, color='red', linestyle=':', alpha=0.5)
    axes[0].axvline(x=0.5, color='orange', linestyle='--', alpha=0.5, label='Maximum')
    # Spinodal region
    s1, s2 = (3 - np.sqrt(3)) / 6, (3 + np.sqrt(3)) / 6
    axes[0].axvspan(s1, s2, alpha=0.1, color='yellow', label=f'Spinodal ({s1:.3f}, {s2:.3f})')
    axes[0].legend(fontsize=7)
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(u, Wp, 'r-', linewidth=2)
    axes[1].axhline(y=0, color='gray', linestyle='-', alpha=0.3)
    axes[1].set_xlabel('u')
    axes[1].set_ylabel("W'(u)")
    axes[1].set_title("W'(u) = 2u(1−u)(1−2u)")
    axes[1].grid(True, alpha=0.3)

    savefig(fig, 'doublewell_curve.pdf')

# ================================================================
# Fig 5-8: Individual energy terms
# ================================================================
def fig_energy_terms():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    res = find_formation(g, p)
    u_form = res.u

    rng = np.random.default_rng(42)
    ec = EnergyComputer(g, p)

    # Sweep a parameter and show each energy term
    alphas = np.linspace(0, 1, 50)
    u_uniform = np.full(g.n, p.volume_fraction)
    e_cl_vals, e_sep_vals, e_bd_vals = [], [], []

    for alpha in alphas:
        u_interp = (1 - alpha) * u_uniform + alpha * u_form
        e_cl_vals.append(energy_cl(u_interp, g, p))
        e_sep_vals.append(energy_sep(u_interp, g, p))
        e_bd_vals.append(energy_bd(u_interp, g, p))

    terms = [
        ('E_cl (Closure Energy)', e_cl_vals, '#1f77b4', 'energy_cl.pdf',
         '‖Cl(u) − u‖² measures closure fixed-point deviation'),
        ('E_sep (Separation Energy)', e_sep_vals, '#ff7f0e', 'energy_sep.pdf',
         '‖D(u) − (1−u)‖² measures distinction quality'),
        ('E_bd (Boundary Energy)', e_bd_vals, '#2ca02c', 'energy_bd.pdf',
         '2α·u^T·L·u + β·Σ W(u_i) — Ginzburg-Landau functional'),
    ]

    for title, vals, color, fname, desc in terms:
        fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.35))
        ax.plot(alphas, vals, '-', color=color, linewidth=2)
        ax.set_xlabel('α (interpolation: uniform → formation)')
        ax.set_ylabel('Energy')
        ax.set_title(title, fontsize=10)
        ax.text(0.5, -0.22, desc, transform=ax.transAxes, ha='center', fontsize=7, color='gray')
        ax.grid(True, alpha=0.3)
        savefig(fig, fname)

    # Combined
    fig, ax = plt.subplots(figsize=(FIGW * 0.55, FIGW * 0.38))
    ax.plot(alphas, e_cl_vals, '-', label='E_cl', linewidth=2)
    ax.plot(alphas, e_sep_vals, '-', label='E_sep', linewidth=2)
    ax.plot(alphas, e_bd_vals, '-', label='E_bd', linewidth=2)
    ax.set_xlabel('α (uniform → formation)')
    ax.set_ylabel('Energy')
    ax.set_title('Three Energy Terms Along Interpolation Path')
    ax.legend()
    ax.grid(True, alpha=0.3)
    savefig(fig, 'energy_terms_combined.pdf')

# ================================================================
# Fig 9-10: Energy landscape (3D + contour)
# ================================================================
def fig_energy_landscape():
    # 2D slice of energy landscape
    # Use a 3×3 grid for visualization speed
    g = GraphState.grid_2d(3, 3)
    p = ParameterRegistry(volume_fraction=0.4, max_iter=500, n_restarts=1)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    # Pick two directions in the field space
    rng = np.random.default_rng(42)
    res = find_formation(g, p)
    u_star = res.u
    v1 = rng.standard_normal(g.n); v1 -= v1.mean(); v1 /= np.linalg.norm(v1)
    v2 = rng.standard_normal(g.n); v2 -= v2.mean(); v2 -= v1 * (v2 @ v1); v2 /= np.linalg.norm(v2)

    xs = np.linspace(-2, 2, 60)
    ys = np.linspace(-2, 2, 60)
    X, Y = np.meshgrid(xs, ys)
    Z = np.zeros_like(X)

    for i in range(len(xs)):
        for j in range(len(ys)):
            u_test = u_star + xs[i] * v1 + ys[j] * v2
            u_test = np.clip(u_test, 0, 1)
            Z[j, i], _ = ec.energy(u_test)

    # 3D surface
    fig = plt.figure(figsize=(FIGW * 0.55, FIGW * 0.45))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, rasterized=True)
    ax.set_xlabel('Direction 1')
    ax.set_ylabel('Direction 2')
    ax.set_zlabel('E(u)')
    ax.set_title('Energy Landscape (2D slice)')
    ax.view_init(elev=30, azim=45)
    savefig(fig, 'energy_landscape_3d.pdf')

    # Contour
    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.4))
    cs = ax.contourf(X, Y, Z, levels=30, cmap='viridis')
    ax.contour(X, Y, Z, levels=15, colors='white', linewidths=0.3, alpha=0.5)
    ax.plot(0, 0, 'r*', markersize=15, label='Formation u*')
    plt.colorbar(cs, ax=ax, label='E(u)')
    ax.set_xlabel('Direction 1')
    ax.set_ylabel('Direction 2')
    ax.set_title('Energy Contours Around Formation')
    ax.legend()
    savefig(fig, 'energy_landscape_contour.pdf')

# ================================================================
# Fig 11: Bifurcation diagram
# ================================================================
def fig_bifurcation():
    g = GraphState.grid_2d(10, 10)
    lam2 = g.fiedler

    # Phase transition: β/α > 4λ₂ / |W''(c)| with c in spinodal
    c_vals = np.linspace(0.22, 0.78, 100)
    Wpp = np.array([double_well_second_deriv(c) for c in c_vals])

    # Threshold ratio at c = volume_fraction = 0.3
    c0 = 0.3
    Wpp_c0 = abs(double_well_second_deriv(c0))
    beta_alpha_crit = 4 * lam2 / Wpp_c0

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.85, FIGW * 0.35))

    # Left: W''(c) and spinodal region
    axes[0].plot(c_vals, Wpp, 'b-', linewidth=2)
    axes[0].axhline(y=0, color='gray', linestyle='-', alpha=0.3)
    s1, s2 = (3 - np.sqrt(3)) / 6, (3 + np.sqrt(3)) / 6
    axes[0].axvspan(s1, s2, alpha=0.15, color='red', label=f'Spinodal')
    axes[0].axvline(x=c0, color='green', linestyle='--', label=f'c = {c0}')
    axes[0].set_xlabel('c (volume fraction)')
    axes[0].set_ylabel("W''(c)")
    axes[0].set_title("Double-Well Second Derivative")
    axes[0].legend(fontsize=7)
    axes[0].grid(True, alpha=0.3)

    # Right: bifurcation diagram (β vs α)
    alphas = np.linspace(0.1, 5, 100)
    beta_crit = beta_alpha_crit * alphas
    axes[1].plot(alphas, beta_crit, 'r-', linewidth=2, label=f'β_c = {beta_alpha_crit:.2f}·α')
    axes[1].fill_between(alphas, beta_crit, 50, alpha=0.1, color='red', label='Phase separation')
    axes[1].fill_between(alphas, 0, beta_crit, alpha=0.1, color='blue', label='Uniform stable')
    axes[1].set_xlabel('α (smoothness)')
    axes[1].set_ylabel('β (double-well)')
    axes[1].set_title(f'Phase Diagram (λ₂ = {lam2:.4f})')
    axes[1].legend(fontsize=7)
    axes[1].set_xlim(0, 5)
    axes[1].set_ylim(0, 50)
    axes[1].grid(True, alpha=0.3)

    savefig(fig, 'bifurcation_diagram.pdf')

# ================================================================
# Fig 12: Spectral universality (λ₂ vs β_c)
# ================================================================
def fig_spectral_universality():
    results = []
    graph_types = {
        'Grid 5×5': GraphState.grid_2d(5, 5),
        'Grid 8×8': GraphState.grid_2d(8, 8),
        'Grid 10×10': GraphState.grid_2d(10, 10),
        'Grid 12×12': GraphState.grid_2d(12, 12),
        'Grid 15×15': GraphState.grid_2d(15, 15),
    }

    c0 = 0.3
    Wpp_c0 = abs(double_well_second_deriv(c0))
    alpha = 1.0

    for name, g in graph_types.items():
        lam2 = g.fiedler
        beta_c = 4 * alpha * lam2 / Wpp_c0
        results.append((name, lam2, beta_c))

    # Also add some random graphs
    rng = np.random.default_rng(42)
    for i, n in enumerate([25, 50, 64, 100]):
        W = np.zeros((n, n))
        # Erdos-Renyi with p chosen to be connected
        p_edge = 4 * np.log(n) / n
        mask = rng.random((n, n)) < p_edge
        W = (mask | mask.T).astype(float)
        np.fill_diagonal(W, 0)
        g = GraphState.from_dense(W)
        try:
            lam2 = g.fiedler
            beta_c = 4 * alpha * lam2 / Wpp_c0
            results.append((f'ER(n={n})', lam2, beta_c))
        except Exception:
            pass

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.4))

    # Separate grid and random
    grid_pts = [(l, b) for name, l, b in results if 'Grid' in name]
    rand_pts = [(l, b) for name, l, b in results if 'ER' in name]

    if grid_pts:
        gl, gb = zip(*grid_pts)
        ax.scatter(gl, gb, c='#1f77b4', s=60, marker='s', label='Grid', zorder=3)
    if rand_pts:
        rl, rb = zip(*rand_pts)
        ax.scatter(rl, rb, c='#ff7f0e', s=60, marker='^', label='Erdős–Rényi', zorder=3)

    # Regression line
    all_l = [l for _, l, _ in results]
    all_b = [b for _, _, b in results]
    coeffs = np.polyfit(all_l, all_b, 1)
    l_fit = np.linspace(min(all_l) * 0.8, max(all_l) * 1.2, 100)
    ax.plot(l_fit, np.polyval(coeffs, l_fit), 'k--', alpha=0.5, label=f'Linear fit (slope={coeffs[0]:.2f})')

    from scipy.stats import pearsonr
    r, _ = pearsonr(all_l, all_b)
    ax.text(0.05, 0.95, f'R² = {r**2:.4f}', transform=ax.transAxes, fontsize=9, va='top')

    ax.set_xlabel('Fiedler eigenvalue λ₂')
    ax.set_ylabel('Critical β_c')
    ax.set_title('Spectral Universality: β_c ∝ λ₂')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'spectral_universality.pdf')

# ================================================================
# Fig 13-14: Operator visualizations (Cl, D)
# ================================================================
def fig_operators():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    rng = np.random.default_rng(42)

    # Start with a noisy field
    u = np.clip(rng.uniform(0.1, 0.6, g.n), 0, 1)
    # Create a region of high values
    for r in range(3, 7):
        for c in range(3, 7):
            u[r * 10 + c] = 0.8 + rng.uniform(-0.05, 0.05)

    cl_u = closure(u, g, p)
    d_u = distinction(u, g, p)
    p_u = aggregation(u, g)

    fig, axes = plt.subplots(2, 2, figsize=(FIGW * 0.7, FIGW * 0.65))
    titles = ['u (input field)', 'P(u) (aggregation)', 'Cl(u) (closure)', 'D(u) (distinction)']
    fields = [u, p_u, cl_u, d_u]
    for ax, title, f in zip(axes.flat, titles, fields):
        im = ax.imshow(f.reshape(10, 10), cmap='viridis', vmin=0, vmax=1,
                       origin='lower', interpolation='nearest')
        ax.set_title(title, fontsize=9)
        ax.set_xticks([]); ax.set_yticks([])
    fig.subplots_adjust(right=0.85)
    cax = fig.add_axes([0.88, 0.15, 0.02, 0.7])
    plt.colorbar(im, cax=cax, label='value')
    fig.suptitle('SCC Operator Triad', fontsize=11, y=1.02)
    savefig(fig, 'operator_triad.pdf')

# ================================================================
# Fig 15-16: Sigma_m constraint visualization
# ================================================================
def fig_sigma_m():
    # Illustrate the simplex constraint in 2D (n=3)
    fig, ax = plt.subplots(figsize=(FIGW * 0.45, FIGW * 0.4))

    # Triangle: u1 + u2 + u3 = m, 0 <= ui <= 1
    # Project to 2D: fix u3 = m - u1 - u2
    m = 0.9  # volume
    u1 = np.linspace(0, min(1, m), 200)
    u2_max = np.minimum(1, m - u1)
    u2_min = np.maximum(0, m - u1 - 1)

    ax.fill_between(u1, u2_min, u2_max, alpha=0.3, color='#1f77b4', label=f'Σ_m (m={m})')
    ax.plot(u1, u2_max, 'b-', linewidth=1)
    ax.plot(u1, u2_min, 'b-', linewidth=1)
    ax.set_xlabel('u₁')
    ax.set_ylabel('u₂')
    ax.set_title(f'Volume Constraint Σ_m ∩ [0,1]ⁿ (n=3, m={m})')
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_aspect('equal')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'sigma_m_constraint.pdf')

# ================================================================
# Fig 17: Gradient flow trajectory
# ================================================================
def fig_gradient_flow():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    rng = np.random.default_rng(42)
    u = np.full(g.n, p.volume_fraction) + rng.normal(0, p.eps_init, g.n)
    u = np.clip(u, 0, 1)
    m = p.volume_fraction * g.n
    u = u * (m / u.sum())

    from scc.optimizer import project_volume
    energies = []
    grad_norms = []
    dt = p.dt_init

    for it in range(300):
        e, _ = ec.energy(u)
        grad = ec.gradient(u)
        energies.append(e)
        grad_norms.append(np.linalg.norm(grad))
        u = project_volume(u - dt * grad, m)

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.85, FIGW * 0.32))
    axes[0].plot(energies, 'b-', linewidth=1.5)
    axes[0].set_xlabel('Iteration')
    axes[0].set_ylabel('E(u)')
    axes[0].set_title('Energy Descent')
    axes[0].grid(True, alpha=0.3)

    axes[1].semilogy(grad_norms, 'r-', linewidth=1.5)
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('‖∇E‖')
    axes[1].set_title('Gradient Norm')
    axes[1].grid(True, alpha=0.3)

    fig.suptitle('Projected Gradient Flow on Σ_m', fontsize=11, y=1.02)
    savefig(fig, 'gradient_flow.pdf')

# ================================================================
# Fig 18: Resolvent (co-belonging) visualization
# ================================================================
def fig_resolvent():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    from scc.operators import resolvent_diagonal
    res = find_formation(g, p)
    u = res.u
    C_diag = resolvent_diagonal(u, g, p)

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.75, FIGW * 0.32))
    im1 = axes[0].imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1,
                          origin='lower', interpolation='nearest')
    axes[0].set_title('u (field)', fontsize=9)
    axes[0].set_xticks([]); axes[0].set_yticks([])

    im2 = axes[1].imshow(C_diag.reshape(10, 10), cmap='magma', origin='lower', interpolation='nearest')
    axes[1].set_title('C(x,x) (resolvent diagonal)', fontsize=9)
    axes[1].set_xticks([]); axes[1].set_yticks([])

    for ax, im in [(axes[0], im1), (axes[1], im2)]:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)

    fig.suptitle('Co-Belonging via Resolvent', fontsize=11, y=1.02)
    savefig(fig, 'resolvent_cobelonging.pdf')

# ================================================================
# Fig 19-20: Hessian spectrum and BB step size
# ================================================================
def fig_hessian_spectrum():
    # Use the E_bd Hessian which is analytically known: 4α·L + β·W''(c)·I
    g = GraphState.grid_2d(8, 8)
    p = ParameterRegistry()

    # Laplacian eigenvalues
    L_dense = g.L.toarray()
    lam_L = np.linalg.eigvalsh(L_dense)

    # E_bd Hessian eigenvalues at uniform c
    c = p.volume_fraction
    Wpp = double_well_second_deriv(c)
    eigvals = 4.0 * p.alpha_bd * lam_L + p.beta_bd * Wpp

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.35))
    ax.bar(range(len(eigvals)), np.sort(eigvals), width=1, color='#1f77b4', alpha=0.7)
    ax.set_xlabel('Index (sorted)')
    ax.set_ylabel('Eigenvalue')
    ax.set_title(f'E_bd Hessian Spectrum at u = {c} (uniform)')
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Stability boundary')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'hessian_spectrum.pdf')

# ================================================================
# Run all
# ================================================================
if __name__ == '__main__':
    print("=== P2: Formal Theory Figures ===")
    fig_closure_convergence()
    fig_double_well()
    fig_energy_terms()
    fig_energy_landscape()
    fig_bifurcation()
    fig_spectral_universality()
    fig_operators()
    fig_sigma_m()
    fig_gradient_flow()
    fig_resolvent()
    fig_hessian_spectrum()
    print(f"\n✓ P2 complete. Figures in {OUT}")
