#!/usr/bin/env python3
"""
P1: Foundation figures for SCC Textbook (Ch1-3).
Generates 20-25 PDF figures for Part I.

Usage:
    python3 docs/04-04/textbook_build/figures/gen_P1_foundations.py
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

from scc import (
    GraphState, ParameterRegistry, find_formation, EnergyComputer,
    closure, distinction, diagnostic_vector, compute_diagnostics,
)

# Output directory
OUT = Path(__file__).parent / "P1_foundations"
OUT.mkdir(exist_ok=True)

# Consistent style
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'font.family': 'serif',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

RNG = np.random.default_rng(42)


def save(fig, name):
    """Save figure as PDF."""
    path = OUT / f"{name}.pdf"
    fig.savefig(path, format='pdf')
    plt.close(fig)
    print(f"  ✓ {name}.pdf")


# ─────────────────────────────────────────────
# 1.1 Object-centric vs Cohesion-centric (3 figures)
# ─────────────────────────────────────────────

def fig_object_vs_cohesion():
    """Side-by-side: discrete objects vs continuous cohesion field."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))

    # Left: Object-centric (crisp boundaries)
    grid = np.zeros((8, 8))
    # Two "objects" with sharp boundaries
    grid[1:4, 1:4] = 1.0
    grid[4:7, 5:8] = 1.0
    ax1.imshow(grid, cmap='Blues', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title('Object-Centric View', fontsize=12)
    ax1.set_xlabel('Discrete boundaries')
    ax1.set_xticks([]); ax1.set_yticks([])

    # Right: Cohesion-centric (continuous field)
    x = np.linspace(0, 7, 80)
    y = np.linspace(0, 7, 80)
    X, Y = np.meshgrid(x, y)
    field = 0.7 * np.exp(-((X-2)**2 + (Y-2)**2) / 2.0) + \
            0.6 * np.exp(-((X-5.5)**2 + (Y-5.5)**2) / 1.5)
    field = np.clip(field, 0, 1)
    im = ax2.imshow(field, cmap='viridis', vmin=0, vmax=1, extent=[0,7,0,7], origin='lower')
    ax2.set_title('Cohesion-Centric View', fontsize=12)
    ax2.set_xlabel('Continuous field $u_t \\in [0,1]$')
    ax2.set_xticks([]); ax2.set_yticks([])
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$u_t$')

    fig.tight_layout()
    save(fig, 'object_vs_cohesion')


def fig_cohesion_gradient():
    """Gradual cohesion: no sharp boundary."""
    fig, ax = plt.subplots(figsize=(5, 4))
    x = np.linspace(0, 9, 100)
    y = np.linspace(0, 9, 100)
    X, Y = np.meshgrid(x, y)
    field = 0.85 * np.exp(-((X-4.5)**2 + (Y-4.5)**2) / 6.0)
    im = ax.imshow(field, cmap='viridis', vmin=0, vmax=1, extent=[0,9,0,9], origin='lower')
    ax.set_title('Soft Cohesion: No Sharp Boundary')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    plt.colorbar(im, ax=ax, label='$u_t(x)$')
    save(fig, 'cohesion_gradient')


def fig_crisp_recovery():
    """Threshold-based crisp recovery from soft field."""
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    x = np.linspace(0, 9, 80)
    y = np.linspace(0, 9, 80)
    X, Y = np.meshgrid(x, y)
    field = 0.9 * np.exp(-((X-4.5)**2 + (Y-4.5)**2) / 5.0)

    # Soft field
    im0 = axes[0].imshow(field, cmap='viridis', vmin=0, vmax=1, extent=[0,9,0,9], origin='lower')
    axes[0].set_title('Soft Field $u_t$')
    plt.colorbar(im0, ax=axes[0], shrink=0.7)

    # Threshold at 0.5
    crisp = (field >= 0.5).astype(float)
    axes[1].imshow(crisp, cmap='Blues', vmin=0, vmax=1, extent=[0,9,0,9], origin='lower')
    axes[1].set_title('Crisp ($\\tau = 0.5$)')

    # Threshold at 0.3
    crisp2 = (field >= 0.3).astype(float)
    axes[2].imshow(crisp2, cmap='Blues', vmin=0, vmax=1, extent=[0,9,0,9], origin='lower')
    axes[2].set_title('Crisp ($\\tau = 0.3$)')

    for ax in axes:
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'crisp_recovery')


# ─────────────────────────────────────────────
# 1.2 Soft Cohesion Field examples (5 figures)
# ─────────────────────────────────────────────

def fig_soft_field_5x5():
    """Soft field on 5x5 grid."""
    g = GraphState.grid_2d(5, 5)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u

    fig, ax = plt.subplots(figsize=(4, 3.5))
    field_2d = u.reshape(5, 5)
    im = ax.imshow(field_2d, cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax.set_title('$u_t$ on $5 \\times 5$ Grid')
    ax.set_xlabel('Column'); ax.set_ylabel('Row')
    plt.colorbar(im, ax=ax, label='$u_t(x)$')
    # Annotate values
    for i in range(5):
        for j in range(5):
            ax.text(j, i, f'{field_2d[i,j]:.2f}', ha='center', va='center',
                    fontsize=7, color='white' if field_2d[i,j] > 0.5 else 'black')
    save(fig, 'soft_field_5x5')


def fig_soft_field_10x10():
    """Soft field on 10x10 grid."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u

    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax.set_title('$u_t$ on $10 \\times 10$ Grid')
    ax.set_xlabel('Column'); ax.set_ylabel('Row')
    plt.colorbar(im, ax=ax, label='$u_t(x)$')
    save(fig, 'soft_field_10x10')


def fig_soft_field_20x20():
    """Soft field on 20x20 grid."""
    g = GraphState.grid_2d(20, 20)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u

    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(u.reshape(20, 20), cmap='viridis', vmin=0, vmax=1)
    ax.set_title('$u_t$ on $20 \\times 20$ Grid')
    ax.set_xlabel('Column'); ax.set_ylabel('Row')
    plt.colorbar(im, ax=ax, label='$u_t(x)$')
    save(fig, 'soft_field_20x20')


def fig_uniform_vs_formation():
    """Uniform field vs optimized formation."""
    g = GraphState.grid_2d(10, 10)
    n = g.n
    p = ParameterRegistry()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))

    # Uniform
    m = p.volume_fraction * g.n
    u_uniform = np.full(n, m / n)
    ax1.imshow(u_uniform.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title(f'Uniform: $u_i = {m/n:.3f}$')
    ax1.set_xticks([]); ax1.set_yticks([])

    # Formation
    r = find_formation(g, p)
    im = ax2.imshow(r.u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax2.set_title(f'Formation (E = {r.energy:.3f})')
    ax2.set_xticks([]); ax2.set_yticks([])
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$u_t$')

    fig.tight_layout()
    save(fig, 'uniform_vs_formation')


def fig_gaussian_init():
    """Gaussian bump initialization on grid."""
    n = 10
    x = np.arange(n)
    y = np.arange(n)
    X, Y = np.meshgrid(x, y)
    center = (n-1) / 2
    u = np.exp(-((X - center)**2 + (Y - center)**2) / (2 * 2.0**2))
    # Normalize to volume constraint
    m = 5.0
    u = u * (m / u.sum())
    u = np.clip(u, 0, 1)

    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(u, cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax.set_title('Gaussian Bump Initialization')
    ax.set_xlabel('Column'); ax.set_ylabel('Row')
    plt.colorbar(im, ax=ax, label='$u_t(x)$')
    save(fig, 'gaussian_init')


# ─────────────────────────────────────────────
# 1.3 Proto-cohesion diagnostic: Bind (3 figures)
# ─────────────────────────────────────────────

def fig_bind_comparison():
    """Low vs high Bind."""
    g = GraphState.grid_2d(10, 10)
    n = g.n
    p = ParameterRegistry()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))

    # Low bind: nearly uniform
    m = p.volume_fraction * g.n
    u_low = np.full(n, m / n) + RNG.normal(0, 0.01, n)
    u_low = np.clip(u_low, 0, 1)
    u_low *= m / u_low.sum()
    d_low = compute_diagnostics(u_low, g, p)
    ax1.imshow(u_low.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title(f'Low Bind = {d_low.bind:.3f}')
    ax1.set_xticks([]); ax1.set_yticks([])

    # High bind: formation
    r = find_formation(g, p)
    d_high = r.diagnostics
    im = ax2.imshow(r.u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax2.set_title(f'High Bind = {d_high.bind:.3f}')
    ax2.set_xticks([]); ax2.set_yticks([])
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$u_t$')

    fig.suptitle('Bind: $\\|u_t\\|_2 / \\sqrt{n}$', fontsize=13)
    fig.tight_layout()
    save(fig, 'bind_comparison')


def fig_bind_formula():
    """Visual explanation of Bind computation."""
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    g = GraphState.grid_2d(8, 8)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u

    # Step 1: field
    axes[0].imshow(u.reshape(8, 8), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[0].set_title('Step 1: Field $u_t$')

    # Step 2: squared
    u2 = u**2
    axes[1].imshow(u2.reshape(8, 8), cmap='viridis', vmin=0, vmax=max(u2), interpolation='nearest')
    axes[1].set_title('Step 2: $u_t^2$')

    # Step 3: norm
    bind = np.sqrt(np.sum(u2)) / np.sqrt(len(u))
    axes[2].bar(['$\\|u\\|_2 / \\sqrt{n}$'], [bind], color='steelblue', width=0.4)
    axes[2].set_ylim(0, 1)
    axes[2].set_title(f'Step 3: Bind = {bind:.3f}')

    for ax in axes[:2]:
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'bind_formula')


# ─────────────────────────────────────────────
# 1.3 Sep (3 figures)
# ─────────────────────────────────────────────

def fig_sep_comparison():
    """Low vs high Sep."""
    g = GraphState.grid_2d(10, 10)
    n = g.n
    p = ParameterRegistry()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))

    # Low sep: spread out field (intermediate values everywhere)
    m = p.volume_fraction * g.n
    u_low = np.full(n, m / n)
    u_low = np.clip(u_low, 0, 1)
    d_low = compute_diagnostics(u_low, g, p)
    ax1.imshow(u_low.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title(f'Low Sep = {d_low.sep:.3f}')
    ax1.set_xticks([]); ax1.set_yticks([])

    # High sep: concentrated
    r = find_formation(g, p)
    d_high = r.diagnostics
    im = ax2.imshow(r.u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax2.set_title(f'High Sep = {d_high.sep:.3f}')
    ax2.set_xticks([]); ax2.set_yticks([])
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$u_t$')

    fig.suptitle('Sep: Weighted average of $D_t(x)$', fontsize=13)
    fig.tight_layout()
    save(fig, 'sep_comparison')


def fig_distinction_field():
    """Distinction operator D_t visualization."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u
    D = distinction(u, g, p)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
    ax1.imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title('Field $u_t$')
    im = ax2.imshow(D.reshape(10, 10), cmap='RdYlBu_r', interpolation='nearest')
    ax2.set_title('Distinction $D_t(x)$')
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$D_t$')
    for ax in (ax1, ax2):
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'distinction_field')


def fig_sep_formula():
    """u vs (1-u) comparison showing separation."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
    ax1.imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title('$u_t$ (formation)')
    im = ax2.imshow((1 - u).reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax2.set_title('$1 - u_t$ (complement)')
    plt.colorbar(im, ax=ax2, shrink=0.8)
    for ax in (ax1, ax2):
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'sep_u_vs_complement')


# ─────────────────────────────────────────────
# 1.3 Inside (3 figures)
# ─────────────────────────────────────────────

def fig_inside_comparison():
    """Low vs high Inside."""
    g = GraphState.grid_2d(10, 10)
    n = g.n
    p = ParameterRegistry()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))

    # Low inside: ring-like (no core)
    rows, cols = 10, 10
    u_ring = np.zeros(n)
    for idx in range(n):
        r, c = divmod(idx, cols)
        dist = np.sqrt((r - 4.5)**2 + (c - 4.5)**2)
        if 2.5 < dist < 4.5:
            u_ring[idx] = 0.8
    m = p.volume_fraction * g.n
    if u_ring.sum() > 0:
        u_ring *= m / u_ring.sum()
    u_ring = np.clip(u_ring, 0, 1)
    d_low = compute_diagnostics(u_ring, g, p)
    ax1.imshow(u_ring.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title(f'Ring: Inside = {d_low.inside:.3f}')
    ax1.set_xticks([]); ax1.set_yticks([])

    # High inside: concentrated blob
    r = find_formation(g, p)
    d_high = r.diagnostics
    im = ax2.imshow(r.u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    ax2.set_title(f'Blob: Inside = {d_high.inside:.3f}')
    ax2.set_xticks([]); ax2.set_yticks([])
    plt.colorbar(im, ax=ax2, shrink=0.8, label='$u_t$')

    fig.suptitle('Inside: $H_0$ Morphological Persistence', fontsize=13)
    fig.tight_layout()
    save(fig, 'inside_comparison')


def fig_inside_homogenization():
    """H0 homogenization process for Inside predicate."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u = r.u.copy()

    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    # Original
    axes[0].imshow(u.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[0].set_title('Original $u_t$')

    # Simulated H0 steps (averaging with neighbors)
    P = g.P.toarray() if hasattr(g.P, 'toarray') else g.P

    for step, ax in zip([3, 10, 30], axes[1:]):
        u_h = u.copy()
        for _ in range(step):
            u_h = 0.5 * u_h + 0.5 * (P @ u_h)
        ax.imshow(u_h.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
        ax.set_title(f'$H_0^{{{step}}}(u_t)$')

    for ax in axes:
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle('$H_0$ Homogenization: Detecting Topological Interior', fontsize=13)
    fig.tight_layout()
    save(fig, 'inside_homogenization')


# ─────────────────────────────────────────────
# 1.3 Persist (3 figures)
# ─────────────────────────────────────────────

def fig_persist_comparison():
    """High vs low persistence over time."""
    g = GraphState.grid_2d(10, 10)
    n = g.n
    p = ParameterRegistry()
    r = find_formation(g, p)
    u_t = r.u.copy()

    fig, axes = plt.subplots(2, 3, figsize=(9, 6))

    # Top row: high persistence (stable formation)
    for i, (step, ax) in enumerate(zip([0, 5, 10], axes[0])):
        # Small perturbation
        u_step = u_t + RNG.normal(0, 0.02 * step, n)
        u_step = np.clip(u_step, 0, 1)
        m = p.volume_fraction * g.n
        u_step *= m / u_step.sum()
        u_step = np.clip(u_step, 0, 1)
        ax.imshow(u_step.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
        overlap = np.sum(np.minimum(u_t, u_step)) / max(u_t.sum(), u_step.sum())
        ax.set_title(f't={step}, P={overlap:.3f}')
        ax.set_xticks([]); ax.set_yticks([])
    axes[0][0].set_ylabel('High Persist', fontsize=11)

    # Bottom row: low persistence (drifting)
    for i, (step, ax) in enumerate(zip([0, 5, 10], axes[1])):
        u_step = u_t + RNG.normal(0, 0.15 * (step + 1), n)
        u_step = np.clip(u_step, 0, 1)
        u_step *= m / u_step.sum()
        u_step = np.clip(u_step, 0, 1)
        ax.imshow(u_step.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
        overlap = np.sum(np.minimum(u_t, u_step)) / max(u_t.sum(), u_step.sum())
        ax.set_title(f't={step}, P={overlap:.3f}')
        ax.set_xticks([]); ax.set_yticks([])
    axes[1][0].set_ylabel('Low Persist', fontsize=11)

    fig.suptitle('Persist: Core Overlap $\\sum \\min(u_t, u_{t-1}) / \\max(\\sum u_t, \\sum u_{t-1})$', fontsize=13)
    fig.tight_layout()
    save(fig, 'persist_comparison')


def fig_persist_overlap():
    """Visual of overlap computation."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    u_prev = r.u.copy()
    # Slightly shifted
    u_curr = np.roll(u_prev.reshape(10, 10), 1, axis=1).ravel()
    u_curr = np.clip(u_curr, 0, 1)
    m = p.volume_fraction * g.n
    u_curr *= m / u_curr.sum()

    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    axes[0].imshow(u_prev.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[0].set_title('$u_{t-1}$')
    axes[1].imshow(u_curr.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[1].set_title('$u_t$')

    overlap = np.minimum(u_prev, u_curr)
    im = axes[2].imshow(overlap.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    persist_val = overlap.sum() / max(u_prev.sum(), u_curr.sum())
    axes[2].set_title(f'$\\min(u_{{t-1}}, u_t)$, P={persist_val:.3f}')
    plt.colorbar(im, ax=axes[2], shrink=0.8)

    for ax in axes:
        ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, 'persist_overlap')


# ─────────────────────────────────────────────
# 1.4 Diagnostic vector overview
# ─────────────────────────────────────────────

def fig_diagnostic_vector():
    """The 4-component diagnostic vector as bar chart."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    d = r.diagnostics

    fig, ax = plt.subplots(figsize=(5, 3.5))
    labels = ['Bind', 'Sep', 'Inside', 'Persist']
    values = [d.bind, d.sep, d.inside, d.persist]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    bars = ax.bar(labels, values, color=colors, width=0.5, edgecolor='black', linewidth=0.5)

    # Value labels
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.3f}', ha='center', va='bottom', fontsize=10)

    ax.set_ylim(0, 1.15)
    ax.set_ylabel('Value $\\in [0, 1]$')
    ax.set_title('Proto-Cohesion Diagnostic Vector $\\mathbf{d}$')
    ax.axhline(y=1.0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    fig.tight_layout()
    save(fig, 'diagnostic_vector')


def fig_diagnostic_radar():
    """Radar plot of diagnostic vector."""
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    r = find_formation(g, p)
    d = r.diagnostics

    labels = ['Bind', 'Sep', 'Inside', 'Persist']
    values = [d.bind, d.sep, d.inside, d.persist]
    values += values[:1]  # close polygon

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4.5, 4.5), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='steelblue', alpha=0.25)
    ax.plot(angles, values, color='steelblue', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 1)
    ax.set_title('Diagnostic Vector $\\mathbf{d} = (B, S, I, P)$', y=1.08, fontsize=13)
    save(fig, 'diagnostic_radar')


# ─────────────────────────────────────────────
# 1.5 Volume constraint
# ─────────────────────────────────────────────

def fig_volume_constraint():
    """Simplex constraint visualization."""
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    g = GraphState.grid_2d(10, 10)
    n = g.n
    p = ParameterRegistry()
    m = p.volume_fraction * g.n

    # Three different fields with same mass
    # 1: uniform
    u1 = np.full(n, m / n)
    axes[0].imshow(u1.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[0].set_title(f'Uniform ($\\sum u = {u1.sum():.1f}$)')

    # 2: concentrated
    r = find_formation(g, p)
    u2 = r.u
    axes[1].imshow(u2.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[1].set_title(f'Concentrated ($\\sum u = {u2.sum():.1f}$)')

    # 3: random (projected)
    u3 = RNG.uniform(0, 1, n)
    u3 = u3 * (m / u3.sum())
    u3 = np.clip(u3, 0, 1)
    u3 = u3 * (m / u3.sum())
    im = axes[2].imshow(u3.reshape(10, 10), cmap='viridis', vmin=0, vmax=1, interpolation='nearest')
    axes[2].set_title(f'Random ($\\sum u = {u3.sum():.1f}$)')
    plt.colorbar(im, ax=axes[2], shrink=0.8)

    for ax in axes:
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle(f'Volume Constraint: $\\Sigma_m = \\{{u \\geq 0 : \\sum u_i = m\\}}$, $m = {m:.1f}$', fontsize=13)
    fig.tight_layout()
    save(fig, 'volume_constraint')


# ─────────────────────────────────────────────
# 1.6 Graph structure examples
# ─────────────────────────────────────────────

def fig_graph_examples():
    """Different graph topologies."""
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))

    for ax, (nsize, label) in zip(axes, [(5, '5x5'), (10, '10x10'), (15, '15x15')]):
        g = GraphState.grid_2d(nsize, nsize)
        p = ParameterRegistry()
        r = find_formation(g, p)
        ax.imshow(r.u.reshape(nsize, nsize), cmap='viridis', vmin=0, vmax=1)
        d = r.diagnostics
        ax.set_title(f'{label}: B={d.bind:.2f}')
        ax.set_xticks([]); ax.set_yticks([])

    fig.suptitle('Formation on Different Grid Sizes', fontsize=13)
    fig.tight_layout()
    save(fig, 'graph_examples')


def fig_1d_field():
    """1D soft cohesion field."""
    n = 50
    # Create 1D path graph adjacency
    import scipy.sparse as sp
    diags = np.ones(n - 1)
    A = sp.diags([diags, diags], [-1, 1], shape=(n, n), format='csr')
    L = sp.diags([A.sum(axis=1).A1], [0]) - A

    # Simple formation: Gaussian
    x = np.arange(n)
    u = 0.9 * np.exp(-(x - 25)**2 / (2 * 5**2))
    u = np.clip(u, 0, 1)

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.fill_between(x, 0, u, alpha=0.3, color='steelblue')
    ax.plot(x, u, 'b-', linewidth=2, label='$u_t(x)$')
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='$\\tau = 0.5$')
    ax.set_xlabel('Node $x$')
    ax.set_ylabel('$u_t(x)$')
    ax.set_ylim(0, 1.05)
    ax.set_title('1D Soft Cohesion Field')
    ax.legend(loc='upper right')
    fig.tight_layout()
    save(fig, '1d_field')


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 50)
    print("P1: Generating Foundation Figures")
    print("=" * 50)

    print("\n[1.1] Object vs Cohesion...")
    fig_object_vs_cohesion()
    fig_cohesion_gradient()
    fig_crisp_recovery()

    print("\n[1.2] Soft Field Examples...")
    fig_soft_field_5x5()
    fig_soft_field_10x10()
    fig_soft_field_20x20()
    fig_uniform_vs_formation()
    fig_gaussian_init()

    print("\n[1.3a] Bind...")
    fig_bind_comparison()
    fig_bind_formula()

    print("\n[1.3b] Sep...")
    fig_sep_comparison()
    fig_distinction_field()
    fig_sep_formula()

    print("\n[1.3c] Inside...")
    fig_inside_comparison()
    fig_inside_homogenization()

    print("\n[1.3d] Persist...")
    fig_persist_comparison()
    fig_persist_overlap()

    print("\n[1.4] Diagnostic Vector...")
    fig_diagnostic_vector()
    fig_diagnostic_radar()

    print("\n[1.5] Volume Constraint...")
    fig_volume_constraint()

    print("\n[1.6] Graph & 1D...")
    fig_graph_examples()
    fig_1d_field()

    total = len(list(OUT.glob("*.pdf")))
    print(f"\n{'='*50}")
    print(f"P1 Complete: {total} PDF figures generated in {OUT}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
