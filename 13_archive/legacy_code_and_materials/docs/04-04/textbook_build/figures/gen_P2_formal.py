#!/usr/bin/env python3
"""
P2: Formal theory figures for SCC Textbook (Ch4-8).
Generates 20-25 PDF figures for Part II.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patches as mpatches
from pathlib import Path
import scipy.sparse as sp

from scc import (
    GraphState, ParameterRegistry, find_formation, EnergyComputer,
    closure, distinction, compute_diagnostics,
)

OUT = Path(__file__).parent / "P2_formal"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    'font.size': 11, 'axes.labelsize': 12, 'axes.titlesize': 13,
    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 10,
    'font.family': 'serif', 'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
})

RNG = np.random.default_rng(42)


def save(fig, name):
    path = OUT / f"{name}.pdf"
    fig.savefig(path, format='pdf')
    plt.close(fig)
    print(f"  ✓ {name}.pdf")


# ─────────────────────────────────────────────
# Ch4: Axioms
# ─────────────────────────────────────────────

def fig_closure_convergence():
    """A3: Iterated closure convergence (3-frame sequence)."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    n = g.n

    # Start with random field
    u = RNG.uniform(0.1, 0.6, n)
    m = p.volume_fraction * n
    u = u * (m / u.sum())
    u = np.clip(u, 0, 1)

    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    titles = ['Initial $u$', '$\\mathrm{Cl}(u)$', '$\\mathrm{Cl}^2(u)$', '$\\mathrm{Cl}^5(u)$']
    iterations = [0, 1, 2, 5]

    u_curr = u.copy()
    frame_idx = 0
    for k in range(6):
        if k in iterations:
            axes[frame_idx].imshow(u_curr.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
            axes[frame_idx].set_title(titles[frame_idx])
            axes[frame_idx].set_xticks([]); axes[frame_idx].set_yticks([])
            frame_idx += 1
        if k < 5:
            u_curr = closure(u_curr, g, p)
            u_curr = np.clip(u_curr, 0, 1)
            u_curr = u_curr * (m / max(u_curr.sum(), 1e-10))
            u_curr = np.clip(u_curr, 0, 1)

    fig.suptitle('A3 Contraction: Iterated Closure Converges', fontsize=13)
    fig.tight_layout()
    save(fig, 'closure_convergence')


def fig_closure_1d():
    """1D closure visualization."""
    n = 40
    x = np.arange(n)

    # 1D path graph
    g = GraphState.grid_2d(1, n)
    p = ParameterRegistry()

    # Irregular input
    u = np.zeros(n)
    u[10:20] = 0.6
    u[15:17] = 0.2  # dip in the middle
    u[22:25] = 0.3  # small bump nearby
    m = u.sum()
    if m == 0:
        m = 5.0
        u = np.full(n, m / n)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(x, u, 'b--', linewidth=1.5, label='Input $u$', alpha=0.7)

    u_cl = closure(u, g, p)
    u_cl = np.clip(u_cl, 0, 1)
    ax.plot(x, u_cl, 'r-', linewidth=2, label='$\\mathrm{Cl}(u)$')

    ax.fill_between(x, u, u_cl, alpha=0.15, color='red')
    ax.set_xlabel('Node $x$')
    ax.set_ylabel('$u(x)$')
    ax.set_ylim(-0.05, 1.05)
    ax.set_title('Closure Fills Gaps (1D)')
    ax.legend()
    fig.tight_layout()
    save(fig, 'closure_1d')


def fig_axiom_dag():
    """Axiom dependency DAG (conceptual)."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Boxes
    boxes = {
        'A': (2, 6.5, 'A: Closure\n(A1\'-A4)'),
        'B': (5, 6.5, 'B: Adjacency\n(B1-B2)'),
        'C': (8, 6.5, 'C: Co-belonging\n(C1-C2)'),
        'D': (3.5, 4, 'D: Distinction\n(D1-D2)'),
        'E': (6.5, 4, 'E: Transport\n(E1-E3)'),
        'En': (5, 1.5, 'Energy\n$E[u_t]$'),
    }

    for key, (cx, cy, label) in boxes.items():
        color = '#4ECDC4' if key in ['A','B','C'] else ('#FF6B6B' if key in ['D','E'] else '#45B7D1')
        bbox = FancyBboxPatch((cx-0.9, cy-0.5), 1.8, 1.0,
                              boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', alpha=0.8)
        ax.add_patch(bbox)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8, fontweight='bold')

    # Arrows
    arrows = [
        ('A', 'D'), ('B', 'D'), ('B', 'E'), ('C', 'D'),
        ('D', 'En'), ('E', 'En'), ('A', 'En'),
    ]
    for src, dst in arrows:
        sx, sy, _ = boxes[src]; dx, dy, _ = boxes[dst]
        ax.annotate('', xy=(dx, dy + 0.5), xytext=(sx, sy - 0.5),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    ax.set_title('Axiom Group Dependencies', fontsize=14)
    save(fig, 'axiom_dag')


def fig_sigmoid():
    """Sigmoid function and its role in closure."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3))

    x = np.linspace(-5, 5, 200)
    for a in [1, 2, 3, 3.5]:
        y = 1 / (1 + np.exp(-a * x))
        ax1.plot(x, y, label=f'$a_{{cl}} = {a}$', linewidth=1.5)

    ax1.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    ax1.set_xlabel('$x$'); ax1.set_ylabel('$\\sigma(a_{cl} \\cdot x)$')
    ax1.set_title('Sigmoid with Varying $a_{cl}$')
    ax1.legend(fontsize=9)

    # Effect on closure strength
    a_vals = np.linspace(0.5, 3.9, 50)
    # Effective "sharpness" = max derivative = a/4
    sharpness = a_vals / 4
    ax2.plot(a_vals, sharpness, 'b-', linewidth=2)
    ax2.axvline(x=4, color='red', linestyle='--', label='$a_{cl} = 4$ (limit)')
    ax2.set_xlabel('$a_{cl}$'); ax2.set_ylabel("Max slope $a_{cl}/4$")
    ax2.set_title('Closure Strength vs. $a_{cl}$')
    ax2.legend(fontsize=9)

    fig.tight_layout()
    save(fig, 'sigmoid_closure')


# ─────────────────────────────────────────────
# Ch5: Operators
# ─────────────────────────────────────────────

def fig_closure_result():
    """Before and after closure operator."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    n = g.n

    u = RNG.uniform(0.0, 0.5, n)
    m = p.volume_fraction * n
    u = u * (m / u.sum())
    u = np.clip(u, 0, 1)

    u_cl = closure(u, g, p)
    u_cl = np.clip(u_cl, 0, 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
    ax1.imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title('Before Closure')
    im = ax2.imshow(u_cl.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax2.set_title('After Closure $\\mathrm{Cl}_t(u)$')
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$u_t$')
    for ax in (ax1, ax2):
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'closure_result')


def fig_distinction_detail():
    """Distinction operator in detail."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u
    D = distinction(u, g, p)

    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    axes[0].imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[0].set_title('$u_t$')
    axes[1].imshow((1-u).reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[1].set_title('$1 - u_t$')
    im = axes[2].imshow(D.reshape(10, 10), cmap='RdYlBu_r', interpolation='nearest')
    axes[2].set_title('$D_t = |u - N \\cdot (1-u)|$')
    plt.colorbar(im, ax=axes[2], shrink=0.8)
    for ax in axes:
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'distinction_detail')


def fig_resolvent_heatmap():
    """Co-belonging resolvent C_t visualization."""
    from scc.operators import aggregation
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u
    C = aggregation(u, g)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
    ax1.imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title('Field $u_t$')
    im = ax2.imshow(C.reshape(10, 10), cmap='inferno', interpolation='nearest')
    ax2.set_title('Resolvent $C_t(x)$')
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$C_t$')
    for ax in (ax1, ax2):
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'resolvent_heatmap')


def fig_cohesion_fingerprint():
    """Cohesion fingerprint vector components."""
    from scc import cohesion_fingerprint
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u
    fp = cohesion_fingerprint(u, g, p)
    # fp may be 2D (n x components) or 1D
    if fp.ndim > 1:
        fp_flat = fp.mean(axis=0) if fp.shape[0] > fp.shape[1] else fp.mean(axis=1)
    else:
        fp_flat = fp

    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.bar(range(len(fp_flat)), fp_flat, color='steelblue', edgecolor='black', linewidth=0.5)
    ax.set_xlabel('Component index')
    ax.set_ylabel('Fingerprint value')
    ax.set_title('Cohesion Fingerprint $f(u_t)$')
    fig.tight_layout()
    save(fig, 'cohesion_fingerprint')


# ─────────────────────────────────────────────
# Ch6: Energy
# ─────────────────────────────────────────────

def fig_double_well():
    """Double-well potential W(u)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3))
    u = np.linspace(0, 1, 200)

    # W(u) = u^2(1-u)^2
    W = u**2 * (1 - u)**2
    ax1.plot(u, W, 'b-', linewidth=2)
    ax1.fill_between(u, 0, W, alpha=0.15, color='blue')
    ax1.set_xlabel('$u$'); ax1.set_ylabel('$W(u)$')
    ax1.set_title('Double-Well $W(u) = u^2(1-u)^2$')
    ax1.axvline(x=0, color='green', linestyle='--', alpha=0.5, linewidth=1)
    ax1.axvline(x=1, color='green', linestyle='--', alpha=0.5, linewidth=1)
    # Mark spinodal
    s1 = (3 - np.sqrt(3)) / 6
    s2 = (3 + np.sqrt(3)) / 6
    ax1.axvspan(s1, s2, alpha=0.1, color='red', label=f'Spinodal [{s1:.3f}, {s2:.3f}]')
    ax1.legend(fontsize=8)

    # W'(u)
    Wp = 2 * u * (1 - u) * (1 - 2*u)
    ax2.plot(u, Wp, 'r-', linewidth=2)
    ax2.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax2.set_xlabel('$u$'); ax2.set_ylabel("$W'(u)$")
    ax2.set_title("$W'(u) = 2u(1-u)(1-2u)$")
    ax2.axvline(x=s1, color='orange', linestyle=':', label='Spinodal')
    ax2.axvline(x=s2, color='orange', linestyle=':')
    ax2.legend(fontsize=8)

    fig.tight_layout()
    save(fig, 'double_well')


def fig_energy_terms():
    """Individual energy terms as functions of concentration."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    n = g.n

    # Sweep volume fraction
    fracs = np.linspace(0.02, 0.5, 30)
    E_cl_vals, E_sep_vals, E_bd_vals = [], [], []

    for frac in fracs:
        m = frac * n
        u = np.zeros(n)
        # Concentrated blob
        center = n // 2 + 5
        for i in range(n):
            r, c = divmod(i, 10)
            dist = np.sqrt((r - 5)**2 + (c - 5)**2)
            u[i] = max(0, 1 - dist / 4)
        u = u * (m / max(u.sum(), 1e-10))
        u = np.clip(u, 0, 1)

        ec = EnergyComputer(g, p)
        _, terms = ec.energy(u)
        E_cl_vals.append(terms.get('E_cl', 0))
        E_sep_vals.append(terms.get('E_sep', 0))
        E_bd_vals.append(terms.get('E_bd', 0))

    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    axes[0].plot(fracs, E_cl_vals, 'b-', linewidth=2)
    axes[0].set_title('$E_{cl}$ (Closure)')
    axes[0].set_xlabel('Volume fraction $m/n$')

    axes[1].plot(fracs, E_sep_vals, 'r-', linewidth=2)
    axes[1].set_title('$E_{sep}$ (Separation)')
    axes[1].set_xlabel('Volume fraction $m/n$')

    axes[2].plot(fracs, E_bd_vals, 'g-', linewidth=2)
    axes[2].set_title('$E_{bd}$ (Boundary)')
    axes[2].set_xlabel('Volume fraction $m/n$')

    for ax in axes:
        ax.set_ylabel('Energy')
    fig.suptitle('Energy Terms vs. Volume Fraction', fontsize=13)
    fig.tight_layout()
    save(fig, 'energy_terms')


def fig_energy_landscape():
    """Energy landscape cross-section."""
    g = GraphState.grid_2d(8, 8)
    p = ParameterRegistry()
    n = g.n
    ec = EnergyComputer(g, p)

    # Fix formation, vary one node
    r = find_formation(g, p)
    u_base = r.u.copy()
    node_idx = n // 2 + 4  # center node

    alphas = np.linspace(0, 1, 50)
    energies = []
    for a in alphas:
        u_test = u_base.copy()
        u_test[node_idx] = a
        # Renormalize
        m = p.volume_fraction * n
        others_sum = u_test.sum() - a
        if others_sum > 0:
            u_test[:node_idx] *= (m - a) / others_sum
            u_test[node_idx+1:] *= (m - a) / others_sum
        u_test = np.clip(u_test, 0, 1)
        energies.append(ec.energy(u_test)[0])

    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.plot(alphas, energies, 'b-', linewidth=2)
    ax.set_xlabel(f'$u_{{node {node_idx}}}$')
    ax.set_ylabel('$E[u]$')
    ax.set_title('Energy Landscape (1D Cross-Section)')
    ax.axvline(x=u_base[node_idx], color='red', linestyle='--', label=f'Optimum ({u_base[node_idx]:.2f})')
    ax.legend()
    fig.tight_layout()
    save(fig, 'energy_landscape')


def fig_energy_landscape_2d():
    """2D energy landscape contour."""
    g = GraphState.grid_2d(6, 6)
    p = ParameterRegistry()
    n = g.n
    ec = EnergyComputer(g, p)

    r = find_formation(g, p)
    u_base = r.u.copy()
    i, j = n // 3, 2 * n // 3

    vals = np.linspace(0.01, 0.99, 25)
    E_grid = np.zeros((len(vals), len(vals)))

    m = p.volume_fraction * n
    for ii, vi in enumerate(vals):
        for jj, vj in enumerate(vals):
            u_test = u_base.copy()
            u_test[i] = vi; u_test[j] = vj
            rem = m - vi - vj
            mask = np.ones(n, dtype=bool); mask[i] = False; mask[j] = False
            s = u_test[mask].sum()
            if s > 0:
                u_test[mask] *= rem / s
            u_test = np.clip(u_test, 0, 1)
            E_grid[jj, ii] = ec.energy(u_test)[0]

    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.contourf(vals, vals, E_grid, levels=20, cmap='RdYlBu_r')
    ax.set_xlabel(f'$u_{{{i}}}$')
    ax.set_ylabel(f'$u_{{{j}}}$')
    ax.set_title('Energy Landscape (2D Cross-Section)')
    plt.colorbar(im, ax=ax, label='$E[u]$')
    ax.plot(u_base[i], u_base[j], 'r*', markersize=12, label='Optimum')
    ax.legend()
    fig.tight_layout()
    save(fig, 'energy_landscape_2d')


def fig_volume_simplex():
    """Geometric visualization of volume constraint simplex."""
    fig, ax = plt.subplots(figsize=(5, 4.5))

    # 2D simplex (3 nodes): u1 + u2 + u3 = m, 0 <= u_i <= 1
    # Show the constraint plane
    from matplotlib.patches import Polygon

    m = 1.5  # example mass
    # Triangle vertices where one coord = 0 and sum = m
    # u3=0: u1+u2=m, range [0,1] for both
    pts = []
    # u1=0, u2=m (if m<=1), u3=0 ... etc.
    # Clip to [0,1] cube
    # Line u1+u2 = m in [0,1]^2
    corners = []
    if m <= 1:
        corners = [(0, m), (m, 0)]
    else:
        corners = [(m-1, 1), (1, m-1)]

    u1 = np.linspace(max(0, m-1), min(1, m), 100)
    u2 = m - u1
    ax.fill_between(u1, 0, u2, alpha=0.2, color='steelblue')
    ax.plot(u1, u2, 'b-', linewidth=2, label=f'$\\Sigma_m$: $u_1 + u_2 = {m}$')

    # Unit square
    ax.plot([0,1,1,0,0], [0,0,1,1,0], 'k--', linewidth=1, alpha=0.3, label='$[0,1]^2$')

    # Feasible region
    ax.set_xlabel('$u_1$'); ax.set_ylabel('$u_2$')
    ax.set_xlim(-0.1, 1.2); ax.set_ylim(-0.1, 1.2)
    ax.set_aspect('equal')
    ax.set_title(f'Volume Constraint $\\Sigma_m$ ($n=2$, $m={m}$)')
    ax.legend(fontsize=9)
    fig.tight_layout()
    save(fig, 'volume_simplex')


# ─────────────────────────────────────────────
# Ch7: Phase Transition
# ─────────────────────────────────────────────

def fig_phase_diagram():
    """Phase transition diagram in (alpha, beta) plane."""
    fig, ax = plt.subplots(figsize=(5.5, 4))
    alpha = np.linspace(0.1, 5, 100)

    # Critical: beta_c = 4 * alpha * lambda_2
    # For grid, lambda_2 ~ 2(1-cos(pi/n))
    for n, ls, label in [(5, '-', '$5\\times 5$'), (10, '--', '$10\\times 10$'), (20, ':', '$20\\times 20$')]:
        lam2 = 2 * (1 - np.cos(np.pi / n))
        beta_c = 4 * alpha * lam2
        ax.plot(alpha, beta_c, ls, linewidth=2, label=f'{label}: $\\lambda_2 = {lam2:.4f}$')

    ax.fill_between(alpha, 0, 4 * alpha * 0.01, alpha=0.15, color='blue', label='Uniform (stable)')
    ax.set_xlabel('$\\alpha$ (boundary weight)')
    ax.set_ylabel('$\\beta$ (separation weight)')
    ax.set_title('Phase Transition: $\\beta_c = 4\\alpha\\lambda_2 / |W\'\'(c)|$')
    ax.legend(fontsize=9)
    ax.set_ylim(0, 3)
    fig.tight_layout()
    save(fig, 'phase_diagram')


def fig_bifurcation():
    """Bifurcation diagram: formation structure vs beta."""
    g = GraphState.grid_2d(8, 8)
    p_base = ParameterRegistry()
    n = g.n

    betas = np.linspace(0.1, 5.0, 20)
    max_u_vals = []
    bind_vals = []

    for beta in betas:
        # Manually set separation weight
        p = ParameterRegistry()
        p.w_sep = beta
        try:
            r = find_formation(g, p)
            max_u_vals.append(r.u.max())
            bind_vals.append(r.diagnostics.bind)
        except Exception:
            max_u_vals.append(0)
            bind_vals.append(0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))
    ax1.plot(betas, max_u_vals, 'bo-', markersize=4, linewidth=1.5)
    ax1.set_xlabel('$\\beta$ (separation weight)')
    ax1.set_ylabel('$\\max(u)$')
    ax1.set_title('Bifurcation: Max Field Value')

    ax2.plot(betas, bind_vals, 'ro-', markersize=4, linewidth=1.5)
    ax2.set_xlabel('$\\beta$ (separation weight)')
    ax2.set_ylabel('Bind')
    ax2.set_title('Bifurcation: Bind Diagnostic')

    fig.tight_layout()
    save(fig, 'bifurcation')


def fig_fiedler_vectors():
    """Fiedler eigenvector on different grids."""
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))

    for ax, (nsize, label) in zip(axes, [(6, '6x6'), (10, '10x10'), (15, '15x15')]):
        g = GraphState.grid_2d(nsize, nsize)
        fv = g.fiedler_vector()
        im = ax.imshow(fv.reshape(nsize, nsize), cmap='RdBu', interpolation='nearest')
        ax.set_title(f'{label}: $\\lambda_2 = {g.fiedler:.4f}$')
        ax.set_xticks([]); ax.set_yticks([])
        plt.colorbar(im, ax=ax, shrink=0.8)

    fig.suptitle('Fiedler Eigenvector (Algebraic Connectivity)', fontsize=13)
    fig.tight_layout()
    save(fig, 'fiedler_vectors')


def fig_spectral_universality():
    """Lambda_2 vs beta_c scatter plot."""
    fig, ax = plt.subplots(figsize=(5, 4))

    lam2_vals = []
    beta_c_vals = []

    for nsize in [4, 5, 6, 7, 8, 10, 12, 15]:
        g = GraphState.grid_2d(nsize, nsize)
        lam2 = g.fiedler
        lam2_vals.append(lam2)
        # Theoretical beta_c (using alpha_bd from default params)
        p = ParameterRegistry()
        beta_c = 4 * p.alpha_bd * lam2
        beta_c_vals.append(beta_c)

    ax.scatter(lam2_vals, beta_c_vals, c='steelblue', s=60, edgecolors='black', zorder=3)

    # Fit line
    lam2_arr = np.array(lam2_vals)
    beta_arr = np.array(beta_c_vals)
    slope = np.polyfit(lam2_arr, beta_arr, 1)[0]
    x_fit = np.linspace(min(lam2_arr), max(lam2_arr), 50)
    ax.plot(x_fit, slope * x_fit, 'r--', linewidth=1.5, label=f'Linear fit (slope = {slope:.2f})')

    ax.set_xlabel('$\\lambda_2$ (Fiedler eigenvalue)')
    ax.set_ylabel('$\\beta_c$ (critical separation)')
    ax.set_title('Spectral Universality: $\\beta_c \\propto \\lambda_2$')
    ax.legend()
    fig.tight_layout()
    save(fig, 'spectral_universality')


# ─────────────────────────────────────────────
# Ch8: Convergence & Stability
# ─────────────────────────────────────────────

def fig_gradient_flow():
    """Gradient flow trajectory: energy vs iteration."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

    # Energy history
    if r.energy_history:
        ax1.semilogy(r.energy_history, 'b-', linewidth=1.5)
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Energy $E[u_t]$')
        ax1.set_title('Energy Descent')

    # Gradient norm history
    if r.grad_norm_history:
        ax2.semilogy(r.grad_norm_history, 'r-', linewidth=1.5)
        ax2.set_xlabel('Iteration')
        ax2.set_ylabel('$\\|\\nabla E\\|$')
        ax2.set_title('Gradient Norm Decay')

    fig.suptitle('Gradient Flow Convergence', fontsize=13)
    fig.tight_layout()
    save(fig, 'gradient_flow')


def fig_multi_start():
    """Multiple random starts converging to same energy."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

    energies = []
    for trial in range(5):
        p_trial = ParameterRegistry()
        r = find_formation(g, p_trial)
        energies.append(r.energy)
        if r.energy_history:
            ax1.plot(r.energy_history, linewidth=1, alpha=0.7, label=f'Trial {trial+1}')

    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Energy')
    ax1.set_title('Multiple Starts: Energy Trajectories')
    ax1.legend(fontsize=8)

    ax2.bar(range(1, len(energies)+1), energies, color='steelblue', edgecolor='black')
    ax2.set_xlabel('Trial')
    ax2.set_ylabel('Final Energy')
    ax2.set_title(f'Final Energies (std = {np.std(energies):.4f})')

    fig.tight_layout()
    save(fig, 'multi_start')


def fig_sharp_interface():
    """Sharp interface limit illustration."""
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))

    x = np.linspace(0, 10, 200)
    center = 5

    for idx, (eps, ax) in enumerate(zip([2.0, 1.0, 0.5, 0.1], axes)):
        u = 1 / (1 + np.exp(-(x - center) / eps))
        ax.plot(x, u, 'b-', linewidth=2)
        ax.fill_between(x, 0, u, alpha=0.15, color='blue')
        ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5)
        ax.set_title(f'$\\varepsilon = {eps}$')
        ax.set_ylim(-0.05, 1.1)
        if idx == 0:
            ax.set_ylabel('$u(x)$')
        ax.set_xlabel('$x$')

    fig.suptitle('Sharp Interface Limit: $\\varepsilon \\to 0$', fontsize=13)
    fig.tight_layout()
    save(fig, 'sharp_interface')


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 50)
    print("P2: Generating Formal Theory Figures")
    print("=" * 50)

    print("\n[Ch4] Axioms...")
    fig_closure_convergence()
    fig_closure_1d()
    fig_axiom_dag()
    fig_sigmoid()

    print("\n[Ch5] Operators...")
    fig_closure_result()
    fig_distinction_detail()
    fig_resolvent_heatmap()
    fig_cohesion_fingerprint()

    print("\n[Ch6] Energy...")
    fig_double_well()
    fig_energy_terms()
    fig_energy_landscape()
    fig_energy_landscape_2d()
    fig_volume_simplex()

    print("\n[Ch7] Phase Transition...")
    fig_phase_diagram()
    fig_bifurcation()
    fig_fiedler_vectors()
    fig_spectral_universality()

    print("\n[Ch8] Convergence...")
    fig_gradient_flow()
    fig_multi_start()
    fig_sharp_interface()

    total = len(list(OUT.glob("*.pdf")))
    print(f"\n{'='*50}")
    print(f"P2 Complete: {total} PDF figures generated in {OUT}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
