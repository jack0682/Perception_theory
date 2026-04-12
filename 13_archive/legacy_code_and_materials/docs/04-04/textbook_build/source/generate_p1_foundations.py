#!/usr/bin/env python3
"""Generate Part 1 (Foundations) figures for the SCC textbook.

Produces ~25 figures: soft field visualizations, diagnostic examples,
Gestalt motivation, and field evolution sequences.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable

from scc import GraphState, ParameterRegistry, find_formation, closure, distinction
from scc.diagnostics import bind_predicate, sep_predicate, inside_predicate, diagnostic_vector

OUT = os.path.join(os.path.dirname(__file__), '..', 'figures', 'P1_foundations')
os.makedirs(OUT, exist_ok=True)

# --- Shared settings ---
FIGW = 170 / 25.4  # A4 text width in inches
DPI = 300

def savefig(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f"  ✓ {name}")

def field_to_grid(u, rows, cols):
    return u.reshape(rows, cols)

def plot_field(ax, u_grid, title=None, vmin=0, vmax=1, cmap='viridis'):
    im = ax.imshow(u_grid, cmap=cmap, vmin=vmin, vmax=vmax, origin='lower', interpolation='nearest')
    if title:
        ax.set_title(title, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    return im

# ================================================================
# Fig 1-3: Soft cohesion fields on 5×5, 10×10, 20×20 grids
# ================================================================
def fig_soft_fields():
    rng = np.random.default_rng(42)
    for size, label in [(5, '5x5'), (10, '10x10'), (20, '20x20')]:
        g = GraphState.grid_2d(size, size)
        p = ParameterRegistry()
        res = find_formation(g, p)
        u_grid = field_to_grid(res.u, size, size)

        fig, ax = plt.subplots(figsize=(FIGW * 0.45, FIGW * 0.45))
        im = plot_field(ax, u_grid, f'Soft Cohesion Field ({label} grid)')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax, label='u(x)')
        savefig(fig, f'soft_field_{label}.pdf')

# ================================================================
# Fig 4-6: Bind predicate examples (high, low, comparison)
# ================================================================
def fig_bind():
    rng = np.random.default_rng(42)
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()

    # High bind: actual formation
    res_high = find_formation(g, p)
    u_high = res_high.u
    bind_high = bind_predicate(u_high, g, p)

    # Low bind: random field projected to simplex
    u_low = rng.uniform(0, 1, g.n)
    u_low = u_low * (p.volume_fraction * g.n / u_low.sum())
    u_low = np.clip(u_low, 0, 1)
    bind_low = bind_predicate(u_low, g, p)

    for u, label, bval in [(u_high, 'high', bind_high), (u_low, 'low', bind_low)]:
        fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.8, FIGW * 0.35))
        u_grid = field_to_grid(u, 10, 10)
        cl_u = closure(u, g, p)
        cl_grid = field_to_grid(cl_u, 10, 10)

        im1 = plot_field(axes[0], u_grid, f'u (field)')
        im2 = plot_field(axes[1], cl_grid, f'Cl(u)')
        fig.suptitle(f'Bind = {bval:.3f} ({label})', fontsize=11, y=1.02)
        for ax in axes:
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(im1, cax=cax)
        savefig(fig, f'bind_{label}.pdf')

    # Comparison bar chart
    fig, ax = plt.subplots(figsize=(FIGW * 0.4, FIGW * 0.3))
    ax.bar(['Formation\n(high Bind)', 'Random\n(low Bind)'], [bind_high, bind_low],
           color=['#2ca02c', '#d62728'], width=0.5)
    ax.set_ylabel('Bind score')
    ax.set_ylim(0, 1.05)
    ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    ax.set_title('Bind Predicate Comparison')
    savefig(fig, 'bind_comparison.pdf')

# ================================================================
# Fig 7-9: Sep predicate examples
# ================================================================
def fig_sep():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()

    # High sep: a well-formed formation
    res = find_formation(g, p)
    u_high = res.u
    sep_high = sep_predicate(u_high, g, p)

    # Low sep: a diffuse field (everything ~0.3)
    u_low = np.full(g.n, 0.3)
    sep_low = sep_predicate(u_low, g, p)

    for u, label, sval in [(u_high, 'high', sep_high), (u_low, 'low', sep_low)]:
        fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.8, FIGW * 0.35))
        u_grid = field_to_grid(u, 10, 10)
        d_u = distinction(u, g, p)
        d_grid = field_to_grid(d_u, 10, 10)

        plot_field(axes[0], u_grid, 'u (field)')
        im2 = plot_field(axes[1], d_grid, 'D(u) (distinction)')
        fig.suptitle(f'Sep = {sval:.3f} ({label})', fontsize=11, y=1.02)
        for ax in axes:
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(im2, cax=cax)
        savefig(fig, f'sep_{label}.pdf')

    fig, ax = plt.subplots(figsize=(FIGW * 0.4, FIGW * 0.3))
    ax.bar(['Formation\n(high Sep)', 'Diffuse\n(low Sep)'], [sep_high, sep_low],
           color=['#2ca02c', '#d62728'], width=0.5)
    ax.set_ylabel('Sep score')
    ax.set_ylim(0, 1.05)
    ax.set_title('Sep Predicate Comparison')
    savefig(fig, 'sep_comparison.pdf')

# ================================================================
# Fig 10-12: Inside predicate examples
# ================================================================
def fig_inside():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()

    # High inside: actual formation
    res = find_formation(g, p)
    u_high = res.u
    inside_high = inside_predicate(u_high, g)

    # Low inside: two disconnected blobs
    u_low = np.zeros(g.n)
    for r in range(2, 4):
        for c in range(2, 4):
            u_low[r * 10 + c] = 0.9
    for r in range(7, 9):
        for c in range(7, 9):
            u_low[r * 10 + c] = 0.9
    inside_low = inside_predicate(u_low, g)

    for u, label, ival in [(u_high, 'high', inside_high), (u_low, 'low', inside_low)]:
        fig, ax = plt.subplots(figsize=(FIGW * 0.45, FIGW * 0.4))
        u_grid = field_to_grid(u, 10, 10)
        im = plot_field(ax, u_grid, f'Inside = {ival:.3f} ({label})')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)
        savefig(fig, f'inside_{label}.pdf')

    fig, ax = plt.subplots(figsize=(FIGW * 0.4, FIGW * 0.3))
    ax.bar(['Single blob\n(high Inside)', 'Two blobs\n(low Inside)'], [inside_high, inside_low],
           color=['#2ca02c', '#d62728'], width=0.5)
    ax.set_ylabel('Inside score')
    ax.set_ylim(0, 1.05)
    ax.set_title('Inside Predicate Comparison')
    savefig(fig, 'inside_comparison.pdf')

# ================================================================
# Fig 13-15: Persist over time (t=0, t=5, t=10)
# ================================================================
def fig_persist():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    res0 = find_formation(g, p)
    u_prev = res0.u.copy()

    # Simulate slight perturbations over time
    rng = np.random.default_rng(123)
    snapshots = [(0, u_prev.copy())]
    u_curr = u_prev.copy()
    for t in range(1, 11):
        noise = rng.normal(0, 0.02, g.n)
        u_curr = np.clip(u_curr + noise, 0, 1)
        u_curr = u_curr * (p.volume_fraction * g.n / max(u_curr.sum(), 1e-10))
        u_curr = np.clip(u_curr, 0, 1)
        if t in [0, 5, 10]:
            snapshots.append((t, u_curr.copy()))

    fig, axes = plt.subplots(1, len(snapshots), figsize=(FIGW * 0.9, FIGW * 0.3))
    for i, (t, u) in enumerate(snapshots):
        u_grid = field_to_grid(u, 10, 10)
        im = plot_field(axes[i], u_grid, f't = {t}')
    fig.suptitle('Formation Persistence Over Time', fontsize=11, y=1.05)
    fig.subplots_adjust(right=0.88)
    cax = fig.add_axes([0.9, 0.15, 0.02, 0.7])
    plt.colorbar(im, cax=cax, label='u(x)')
    savefig(fig, 'persist_sequence.pdf')

    for t, u in snapshots:
        fig, ax = plt.subplots(figsize=(FIGW * 0.35, FIGW * 0.35))
        im = plot_field(ax, field_to_grid(u, 10, 10), f't = {t}')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)
        savefig(fig, f'persist_t{t}.pdf')

# ================================================================
# Fig 16-17: Gestalt motivation diagrams
# ================================================================
def fig_gestalt():
    # Proximity: dots that group by distance
    fig, axes = plt.subplots(1, 3, figsize=(FIGW * 0.9, FIGW * 0.25))

    # Proximity
    rng = np.random.default_rng(42)
    cluster1 = rng.normal([2, 2], 0.3, (15, 2))
    cluster2 = rng.normal([5, 5], 0.3, (15, 2))
    scatter = rng.uniform(0, 7, (5, 2))
    axes[0].scatter(cluster1[:, 0], cluster1[:, 1], c='#1f77b4', s=30)
    axes[0].scatter(cluster2[:, 0], cluster2[:, 1], c='#ff7f0e', s=30)
    axes[0].scatter(scatter[:, 0], scatter[:, 1], c='gray', s=15, alpha=0.5)
    axes[0].set_title('Proximity', fontsize=10)
    axes[0].set_xlim(-1, 8)
    axes[0].set_ylim(-1, 8)
    axes[0].set_aspect('equal')
    axes[0].set_xticks([])
    axes[0].set_yticks([])

    # Similarity: shape-based grouping
    angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
    for i, a in enumerate(angles):
        x, y = 3 + 2 * np.cos(a), 3 + 2 * np.sin(a)
        if i % 2 == 0:
            axes[1].plot(x, y, 'o', markersize=12, color='#2ca02c')
        else:
            axes[1].plot(x, y, 's', markersize=12, color='#d62728')
    axes[1].set_title('Similarity', fontsize=10)
    axes[1].set_xlim(0, 6)
    axes[1].set_ylim(0, 6)
    axes[1].set_aspect('equal')
    axes[1].set_xticks([])
    axes[1].set_yticks([])

    # Continuity: smooth curve vs jagged
    x = np.linspace(0, 6, 100)
    axes[2].plot(x, 2 + np.sin(x), '-', color='#1f77b4', linewidth=2, label='Smooth')
    axes[2].plot(x, 4 + 0.5 * np.sin(3 * x), '--', color='#ff7f0e', linewidth=2, label='Continuous')
    axes[2].set_title('Continuity', fontsize=10)
    axes[2].set_xlim(0, 6)
    axes[2].set_ylim(0, 6)
    axes[2].legend(fontsize=7)
    axes[2].set_xticks([])
    axes[2].set_yticks([])

    fig.suptitle('Gestalt Grouping Principles', fontsize=11, y=1.02)
    savefig(fig, 'gestalt_principles.pdf')

    # SCC vs Gestalt mapping diagram
    fig, ax = plt.subplots(figsize=(FIGW * 0.7, FIGW * 0.4))
    ax.axis('off')
    gestalt = ['Proximity', 'Similarity', 'Continuity', 'Closure', 'Common Fate']
    scc = ['Adjacency N_t', 'Closure Cl_t', 'Smoothness E_bd', 'Cl_t fixed pt', 'Transport M_{t→s}']
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, len(gestalt) + 0.5)
    ax.text(2, len(gestalt) + 0.2, 'Gestalt Principle', ha='center', fontsize=10, fontweight='bold')
    ax.text(8, len(gestalt) + 0.2, 'SCC Counterpart', ha='center', fontsize=10, fontweight='bold')
    for i, (gp, sc) in enumerate(zip(gestalt, scc)):
        y = len(gestalt) - 1 - i
        ax.text(2, y, gp, ha='center', va='center', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#e6f0ff', edgecolor='#1f77b4'))
        ax.text(8, y, sc, ha='center', va='center', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff0e6', edgecolor='#ff7f0e'))
        ax.annotate('', xy=(5.8, y), xytext=(4.2, y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    ax.set_title('Gestalt → SCC Correspondence', fontsize=11, pad=15)
    savefig(fig, 'gestalt_scc_mapping.pdf')

# ================================================================
# Fig 18-20: Field evolution sequence
# ================================================================
def fig_evolution():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()

    # Run optimization and capture intermediate states
    from scc.energy import EnergyComputer
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    rng = np.random.default_rng(42)
    u = np.full(g.n, p.volume_fraction) + rng.normal(0, p.eps_init, g.n)
    u = np.clip(u, 0, 1)
    m = p.volume_fraction * g.n
    u = u * (m / u.sum())
    u = np.clip(u, 0, 1)

    snapshots = [('Init', u.copy())]
    dt = p.dt_init
    for it in range(500):
        grad = ec.gradient(u)
        u_new = u - dt * grad
        from scc.optimizer import project_volume
        u_new = project_volume(u_new, m)
        u = u_new
        if it + 1 in [10, 50, 100, 500]:
            snapshots.append((f'Iter {it+1}', u.copy()))

    fig, axes = plt.subplots(1, len(snapshots), figsize=(FIGW, FIGW * 0.22))
    for i, (label, u_snap) in enumerate(snapshots):
        u_grid = field_to_grid(u_snap, 10, 10)
        im = plot_field(axes[i], u_grid, label)
    fig.suptitle('Gradient Descent Evolution: u₀ → Formation', fontsize=11, y=1.05)
    fig.subplots_adjust(right=0.88)
    cax = fig.add_axes([0.9, 0.15, 0.015, 0.7])
    plt.colorbar(im, cax=cax, label='u(x)')
    savefig(fig, 'field_evolution_sequence.pdf')

# ================================================================
# Fig 21: Diagnostic vector spider/radar chart
# ================================================================
def fig_diagnostic_radar():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    res = find_formation(g, p)
    dv = res.diagnostics

    categories = ['Bind', 'Sep', 'Inside', 'Persist']
    values = [dv.bind, dv.sep, dv.inside, dv.persist]
    values += values[:1]  # close polygon

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(FIGW * 0.4, FIGW * 0.4), subplot_kw=dict(polar=True))
    ax.fill(angles, values, alpha=0.25, color='#1f77b4')
    ax.plot(angles, values, 'o-', color='#1f77b4', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 1)
    ax.set_title('Diagnostic Vector d = (Bind, Sep, Inside, Persist)', fontsize=10, pad=20)
    savefig(fig, 'diagnostic_radar.pdf')

# ================================================================
# Fig 22-23: Crisp recovery zones
# ================================================================
def fig_crisp_recovery():
    g = GraphState.grid_2d(15, 15)
    p = ParameterRegistry()
    res = find_formation(g, p)
    u = res.u
    u_grid = field_to_grid(u, 15, 15)

    # Zone classification
    zones = np.zeros_like(u)
    zones[u >= p.theta_core] = 3  # core
    zones[(u >= p.theta_in) & (u < p.theta_core)] = 2  # interior
    zones[(u >= p.theta_ext) & (u < p.theta_in)] = 1  # boundary
    zones[u < p.theta_ext] = 0  # exterior

    zone_grid = field_to_grid(zones, 15, 15)

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.8, FIGW * 0.35))
    im1 = plot_field(axes[0], u_grid, 'Soft Field u(x)')
    divider = make_axes_locatable(axes[0])
    cax1 = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im1, cax=cax1)

    cmap_zones = plt.colormaps.get_cmap('RdYlGn').resampled(4)
    im2 = axes[1].imshow(zone_grid, cmap=cmap_zones, vmin=0, vmax=3, origin='lower', interpolation='nearest')
    axes[1].set_title('Crisp Recovery Zones')
    axes[1].set_xticks([])
    axes[1].set_yticks([])
    divider2 = make_axes_locatable(axes[1])
    cax2 = divider2.append_axes("right", size="5%", pad=0.05)
    cbar2 = plt.colorbar(im2, cax=cax2, ticks=[0.375, 1.125, 1.875, 2.625])
    cbar2.ax.set_yticklabels(['Ext', 'Bdy', 'Int', 'Core'], fontsize=7)

    savefig(fig, 'crisp_recovery_zones.pdf')

# ================================================================
# Fig 24-25: What is NOT a formation (contrast examples)
# ================================================================
def fig_non_formations():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    res = find_formation(g, p)
    u_good = res.u

    rng = np.random.default_rng(99)

    examples = [
        ('Formation', u_good),
        ('Uniform (no structure)', np.full(g.n, 0.3)),
        ('Random noise', np.clip(rng.uniform(0, 1, g.n), 0, 1)),
        ('Sparse dots', np.where(rng.random(g.n) < 0.1, 0.95, 0.0)),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(FIGW, FIGW * 0.22))
    for i, (label, u) in enumerate(examples):
        u_grid = field_to_grid(u, 10, 10)
        plot_field(axes[i], u_grid, label)
        dv = diagnostic_vector(u, g, p)
        axes[i].text(0.5, -0.12, f'min={dv.min_score:.2f}', transform=axes[i].transAxes,
                     ha='center', fontsize=7, color='gray')
    fig.suptitle('Formation vs Non-Formations', fontsize=11, y=1.02)
    savefig(fig, 'formation_vs_non.pdf')

# ================================================================
# Run all
# ================================================================
if __name__ == '__main__':
    print("=== P1: Foundations Figures ===")
    fig_soft_fields()
    fig_bind()
    fig_sep()
    fig_inside()
    fig_persist()
    fig_gestalt()
    fig_evolution()
    fig_diagnostic_radar()
    fig_crisp_recovery()
    fig_non_formations()
    print(f"\n✓ P1 complete. Figures in {OUT}")
