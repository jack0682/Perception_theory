#!/usr/bin/env python3
"""Generate all figures for the cognitive science paper.

Output: /home/jack/ex/papers/figures/*.pdf
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import csv

from scc import GraphState, ParameterRegistry, find_formation
from scc.operators import distinction
from scc.diagnostics import compute_diagnostics
from scc.transport import (
    cohesion_fingerprint, graph_distance_matrix, transport_cost,
    sinkhorn_partial_ot,
)

OUTDIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(OUTDIR, exist_ok=True)

# Consistent color palette
COLORS = {
    'Bind': '#2196F3',    # blue
    'Sep': '#FF9800',     # orange
    'Inside': '#4CAF50',  # green
    'Persist': '#9C27B0', # purple
}


# ============================================================
# Figure 2: Diagnostic Vector Radar Plots
# ============================================================
def fig2_radar():
    """4 formation types with different diagnostic profiles."""
    g = GraphState.grid_2d(10, 10)

    configs = {
        'Full SCC\n(well-formed)': ParameterRegistry(
            w_cl=1.0, w_sep=1.0, w_bd=1.0, beta_bd=20.0,
            volume_fraction=0.5, n_restarts=3, max_iter=2000),
        'BD-only\n(bound, low sep)': ParameterRegistry(
            w_cl=0.0, w_sep=0.0, w_bd=1.0, beta_bd=20.0,
            volume_fraction=0.5, n_restarts=3, max_iter=2000),
        'SEP-dominant\n(over-separated)': ParameterRegistry(
            w_cl=0.0, w_sep=10.0, w_bd=1.0, beta_bd=20.0,
            volume_fraction=0.5, n_restarts=3, max_iter=2000),
        'Weak formation\n(low beta)': ParameterRegistry(
            w_cl=1.0, w_sep=1.0, w_bd=1.0, beta_bd=1.0,
            volume_fraction=0.5, n_restarts=3, max_iter=2000),
    }

    categories = ['Bind', 'Sep', 'Inside', 'Persist']
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]  # close the loop

    fig, axes = plt.subplots(1, 4, figsize=(16, 4), subplot_kw=dict(polar=True))

    for ax, (name, params) in zip(axes, configs.items()):
        result = find_formation(g, params, normalize=True, verbose=False)
        d = result.diagnostics
        values = [d.bind, d.sep, d.inside, d.persist]
        values += values[:1]

        ax.fill(angles, values, alpha=0.25, color='#2196F3')
        ax.plot(angles, values, 'o-', linewidth=2, color='#2196F3', markersize=6)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=10)
        ax.set_ylim(0, 1)
        ax.set_yticks([0.25, 0.5, 0.75, 1.0])
        ax.set_yticklabels(['', '0.5', '', '1.0'], fontsize=7)
        ax.set_title(name, fontsize=11, pad=15)

        # Annotate values
        for angle, val, cat in zip(angles[:-1], values[:-1], categories):
            ax.annotate(f'{val:.2f}', xy=(angle, val), fontsize=8,
                       ha='center', va='bottom', color='#333')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig2_radar.pdf'), bbox_inches='tight', dpi=150)
    plt.close()
    print("fig2_radar.pdf generated")


# ============================================================
# Figure 3: Formation Heat Maps
# ============================================================
def fig3_heatmaps():
    """Heat maps of cohesion fields on grids."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    for ax, (rows, cols) in zip(axes, [(10, 10), (15, 15), (20, 20)]):
        g = GraphState.grid_2d(rows, cols)
        p = ParameterRegistry(
            beta_bd=20.0, volume_fraction=0.5,
            n_restarts=3, max_iter=3000)
        result = find_formation(g, p, normalize=True, verbose=False)
        d = result.diagnostics

        u_grid = result.u.reshape(rows, cols)
        im = ax.imshow(u_grid, cmap='inferno', vmin=0, vmax=1,
                       interpolation='nearest', origin='lower')
        ax.set_title(f'{rows}x{cols} grid\n'
                     f'B={d.bind:.2f} S={d.sep:.2f} I={d.inside:.2f}',
                     fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    cbar = fig.colorbar(im, ax=axes, shrink=0.8, label='Cohesion u(x)')
    plt.suptitle('Formation Fields on Grid Graphs', fontsize=13, y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig3_heatmaps.pdf'), bbox_inches='tight', dpi=150)
    plt.close()
    print("fig3_heatmaps.pdf generated")


# ============================================================
# Figure 4: Energy Ablation Bar Chart
# ============================================================
def fig4_ablation():
    """Grouped bar chart from exp3 results."""
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            'experiments', 'exp3_results.csv')

    # Read CSV
    data = {}
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cfg = row['config']
            if cfg not in data:
                data[cfg] = {'Bind': [], 'Sep': [], 'Inside': []}
            data[cfg]['Bind'].append(float(row['Bind']))
            data[cfg]['Sep'].append(float(row['Sep_old']))
            data[cfg]['Inside'].append(float(row['Inside']))

    configs = ['BD-only', 'BD+CL', 'BD+SEP', 'Full-SCC', 'SEP-dominant', 'SEP-only']
    metrics = ['Bind', 'Sep', 'Inside']
    colors = [COLORS['Bind'], COLORS['Sep'], COLORS['Inside']]

    means = {cfg: {m: np.mean(data[cfg][m]) for m in metrics} for cfg in configs}
    stds = {cfg: {m: np.std(data[cfg][m]) for m in metrics} for cfg in configs}

    x = np.arange(len(configs))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 5))

    for i, (metric, color) in enumerate(zip(metrics, colors)):
        vals = [means[cfg][metric] for cfg in configs]
        errs = [stds[cfg][metric] for cfg in configs]
        ax.bar(x + i * width, vals, width, yerr=errs, label=metric,
               color=color, alpha=0.85, capsize=3)

    ax.set_xticks(x + width)
    ax.set_xticklabels(configs, fontsize=9, rotation=15, ha='right')
    ax.set_ylabel('Diagnostic Score', fontsize=11)
    ax.set_ylim(0, 1.15)
    ax.legend(fontsize=10, loc='upper right')
    ax.set_title('Energy Ablation: Independent Contributions of Each Term', fontsize=12)
    ax.axhline(y=0.8, color='gray', linestyle='--', alpha=0.3, label='_nolegend_')
    ax.grid(axis='y', alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig4_ablation.pdf'), bbox_inches='tight', dpi=150)
    plt.close()
    print("fig4_ablation.pdf generated")


# ============================================================
# Figure 5: Self-Referential Loop Diagram
# ============================================================
def fig5_loop():
    """Self-referential operator loop schematic."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Nodes on a circle
    R = 1.4
    nodes = {
        'Field $u_t$': (0, R),
        'Operators\n$\\mathrm{Cl}_t, D_t, C_t$': (R * np.cos(np.pi/6), -R * np.sin(np.pi/6)),
        'Energy $\\mathcal{E}$': (-R * np.cos(np.pi/6), -R * np.sin(np.pi/6)),
    }

    for name, (x, y) in nodes.items():
        circle = plt.Circle((x, y), 0.55, fill=True, facecolor='#E3F2FD',
                           edgecolor='#1976D2', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold')

    # Arrows
    positions = list(nodes.values())
    labels = ['defines', 'computes', 'gradient\nflow']
    for i in range(3):
        x1, y1 = positions[i]
        x2, y2 = positions[(i + 1) % 3]
        dx, dy = x2 - x1, y2 - y1
        d = np.sqrt(dx**2 + dy**2)
        # Shorten arrows to not overlap circles
        shrink = 0.6 / d
        ax.annotate('', xy=(x2 - dx * shrink, y2 - dy * shrink),
                    xytext=(x1 + dx * shrink, y1 + dy * shrink),
                    arrowprops=dict(arrowstyle='->', lw=2, color='#1976D2'))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # Offset label perpendicular to arrow
        nx, ny = -dy / d * 0.25, dx / d * 0.25
        ax.text(mx + nx, my + ny, labels[i], ha='center', va='center',
               fontsize=9, fontstyle='italic', color='#555')

    ax.set_title('Self-Referential Structure', fontsize=13, pad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig5_loop.pdf'), bbox_inches='tight', dpi=150)
    plt.close()
    print("fig5_loop.pdf generated")


# ============================================================
# Figure 6: Lambda sweep (sweet spot)
# ============================================================
def fig6_sweep():
    """Diagnostic scores vs lambda_sep/lambda_bd ratio."""
    g = GraphState.grid_2d(10, 10)
    ratios = [0, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0, 1000.0]
    results = {'ratio': [], 'Bind': [], 'Sep': [], 'Inside': []}

    for ratio in ratios:
        p = ParameterRegistry(
            w_sep=ratio, w_bd=1.0, w_cl=1.0,
            beta_bd=20.0, volume_fraction=0.5,
            n_restarts=2, max_iter=1000)
        r = find_formation(g, p, normalize=True, verbose=False)
        d = r.diagnostics
        results['ratio'].append(ratio if ratio > 0 else 0.001)
        results['Bind'].append(d.bind)
        results['Sep'].append(d.sep)
        results['Inside'].append(d.inside)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    for metric in ['Bind', 'Sep', 'Inside']:
        ax.plot(results['ratio'], results[metric], 'o-',
               color=COLORS[metric], linewidth=2, markersize=6, label=metric)

    ax.set_xscale('log')
    ax.set_xlabel('$\\lambda_{\\mathrm{sep}} / \\lambda_{\\mathrm{bd}}$', fontsize=12)
    ax.set_ylabel('Diagnostic Score', fontsize=11)
    ax.set_ylim(0.7, 1.05)
    ax.legend(fontsize=10)
    ax.set_title('Formation Quality vs. Separation Weight', fontsize=12)
    ax.axvline(x=1.0, color='gray', linestyle='--', alpha=0.4)
    ax.text(1.2, 0.72, 'sweet spot', fontsize=9, color='gray')
    ax.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig6_sweep.pdf'), bbox_inches='tight', dpi=150)
    plt.close()
    print("fig6_sweep.pdf generated")


# ============================================================
# Figure 7: Fingerprint Gap by Depth
# ============================================================
def fig7_fingerprint_gap():
    """Bar chart: fingerprint gap² by component, grouped by depth."""
    GRID = (20, 20)
    THETA_CORE = 0.8

    graph = GraphState.grid_2d(*GRID)
    params = ParameterRegistry(
        beta_bd=50.0, volume_fraction=0.3, n_restarts=5, max_iter=5000,
    )
    result = find_formation(graph, params, normalize=True, verbose=False)
    u = result.u

    phi = cohesion_fingerprint(u, graph, params)
    core_mask = u >= THETA_CORE
    noncore = ~core_mask

    if not np.any(core_mask) or not np.any(noncore):
        print("fig7_fingerprint_gap.pdf SKIPPED (no core/noncore split)")
        return

    phi_ext_mean = phi[noncore].mean(axis=0)

    # Classify depth using adjacency
    W_dense = graph.W.toarray()
    boundary_core = np.zeros(graph.n, bool)
    for i in np.where(core_mask)[0]:
        neighbors = np.where(W_dense[i, :] > 0)[0]
        if np.any(~core_mask[neighbors]):
            boundary_core[i] = True

    shallow_core = boundary_core
    deep_core = core_mask & ~boundary_core

    comp_names = ['u', 'Cl', 'D', 'C']
    deep_gaps = []
    shallow_gaps = []

    for j in range(4):
        if np.any(deep_core):
            deep_gaps.append((phi[deep_core, j].mean() - phi_ext_mean[j]) ** 2)
        else:
            deep_gaps.append(0.0)
        if np.any(shallow_core):
            shallow_gaps.append((phi[shallow_core, j].mean() - phi_ext_mean[j]) ** 2)
        else:
            shallow_gaps.append(0.0)

    x = np.arange(len(comp_names))
    width = 0.35

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(x - width / 2, deep_gaps, width, label='Deep core (δ≥2)',
           color='#1976D2', alpha=0.85)
    ax.bar(x + width / 2, shallow_gaps, width, label='Shallow core (δ=1)',
           color='#FF7043', alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(comp_names, fontsize=11)
    ax.set_ylabel('Gap² (vs exterior)', fontsize=11)
    ax.set_title('Fingerprint Gap by Depth and Component', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig_fingerprint_gap.pdf'),
                bbox_inches='tight', dpi=150)
    plt.close()
    print("fig_fingerprint_gap.pdf generated")


# ============================================================
# Figure 8: Transport Concentration
# ============================================================
def fig8_transport_concentration():
    """Line plot: core-to-core transport fraction vs gamma/eps_OT ratio."""
    GRID = (15, 15)
    THETA_CORE = 0.8

    graph = GraphState.grid_2d(*GRID)
    n = graph.n
    params = ParameterRegistry(
        beta_bd=50.0, volume_fraction=0.3, n_restarts=5, max_iter=5000,
    )
    result = find_formation(graph, params, normalize=True, verbose=False)
    u = result.u

    phi = cohesion_fingerprint(u, graph, params)
    dist_matrix = graph_distance_matrix(graph)
    core_mask = u >= THETA_CORE
    noncore = ~core_mask

    if not np.any(core_mask) or not np.any(noncore):
        print("fig_transport_concentration.pdf SKIPPED (no core/noncore split)")
        return

    # Compute fingerprint gap for theory bound
    phi_core_mean = phi[core_mask].mean(axis=0)
    phi_ext_mean = phi[noncore].mean(axis=0)
    delta_phi_sq = float(np.sum((phi_core_mean - phi_ext_mean) ** 2))

    gammas = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    eps_ot = 0.5
    ratios = [g / eps_ot for g in gammas]
    core_fracs = []
    theory_bounds = []

    for gamma in gammas:
        cost = transport_cost(phi, phi, dist_matrix, sigma=2.0, gamma=gamma)
        M, info = sinkhorn_partial_ot(cost, u, u, eps_ot, max_iter=200, tol=1e-8)

        row_mass = M[core_mask, :].sum()
        if row_mass > 1e-15:
            core_frac = M[np.ix_(core_mask, core_mask)].sum() / row_mass
        else:
            core_frac = 0.0
        core_fracs.append(core_frac)

        exponent = -gamma * delta_phi_sq / eps_ot
        lb = max(0.0, 1.0 - n * np.exp(exponent)) if exponent > -500 else 1.0
        theory_bounds.append(lb)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(ratios, core_fracs, 'o-', color='#1976D2', linewidth=2,
            markersize=7, label='Measured core fraction', zorder=3)
    ax.plot(ratios, theory_bounds, 's--', color='#E53935', linewidth=1.5,
            markersize=5, label='Theory lower bound', alpha=0.8, zorder=2)

    ax.set_xlabel('$\\gamma / \\varepsilon_{OT}$', fontsize=12)
    ax.set_ylabel('Core-to-core transport fraction', fontsize=11)
    ax.set_title('Transport Concentration vs. Fingerprint Weight', fontsize=12)
    ax.set_ylim(-0.05, 1.05)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'fig_transport_concentration.pdf'),
                bbox_inches='tight', dpi=150)
    plt.close()
    print("fig_transport_concentration.pdf generated")


if __name__ == '__main__':
    print("Generating figures for cognitive science paper...")
    print()
    fig2_radar()
    fig3_heatmaps()
    fig4_ablation()
    fig5_loop()
    fig6_sweep()
    fig7_fingerprint_gap()
    fig8_transport_concentration()
    print()
    print(f"All figures saved to {OUTDIR}/")
