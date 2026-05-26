"""F8 — Gradient flow on the constraint manifold Sigma_m.

For n=3 sites with mass m=1, Sigma_m is the standard 2-simplex.
Project to the (u_1, u_2) plane (with u_3 = 1 − u_1 − u_2).

Energy proxy: 4-term-like with smoothness on a 3-cycle graph plus
double-well.  Plot energy contours + projected gradient flow paths.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pathlib import Path
import _style; _style.apply()

# ── energy on n=3 sites (3-cycle graph), Sigma_m = simplex ─────────
def energy(u1, u2, alpha=1.0, beta=12.0):
    u3 = 1.0 - u1 - u2
    smooth = ((u1 - u2) ** 2 + (u2 - u3) ** 2 + (u3 - u1) ** 2)
    dwell = (u1 ** 2 * (1 - u1) ** 2
             + u2 ** 2 * (1 - u2) ** 2
             + u3 ** 2 * (1 - u3) ** 2)
    return alpha * smooth + beta * dwell

def grad(u1, u2, alpha=1.0, beta=12.0, eps=1e-4):
    """Numerical gradient on the (u1, u2) plane, projected."""
    e0 = energy(u1, u2, alpha, beta)
    g1 = (energy(u1 + eps, u2, alpha, beta) - e0) / eps
    g2 = (energy(u1, u2 + eps, alpha, beta) - e0) / eps
    return g1, g2

# ── grid + contour data ────────────────────────────────────────────
res = 220
u1_grid = np.linspace(0.001, 0.999, res)
u2_grid = np.linspace(0.001, 0.999, res)
U1, U2 = np.meshgrid(u1_grid, u2_grid)
mask = (U1 + U2 < 1.0)
E = np.where(mask, energy(U1, U2), np.nan)

# ── plot ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7.5, 7.0))

# Energy contours (mono — only black lines, no fill)
levels = np.linspace(np.nanmin(E), np.nanmin(E) + 1.6, 12)
cs = ax.contour(U1, U2, E, levels=levels, colors='black', linewidths=0.6, alpha=0.6)
ax.clabel(cs, inline=True, fontsize=6, fmt='%.2f')

# Simplex boundary (triangle)
triangle = Polygon([(0, 0), (1, 0), (0, 1)], closed=True,
                   fill=False, edgecolor='black', linewidth=1.2)
ax.add_patch(triangle)

# Vertices labels
for (vx, vy, label, ha, va) in [
        (-0.02, -0.02, '$u_3 = 1$', 'right', 'top'),
        (1.02, -0.02, '$u_1 = 1$', 'left', 'top'),
        (-0.02, 1.02, '$u_2 = 1$', 'right', 'bottom')]:
    ax.text(vx, vy, label, ha=ha, va=va, fontsize=10)

# Gradient flow trajectories from several starting points
starts = [(0.30, 0.55), (0.55, 0.30), (0.30, 0.30),
          (0.20, 0.65), (0.65, 0.20)]
dt, n_steps = 0.005, 700
for (s1, s2) in starts:
    pts = [(s1, s2)]
    u1, u2 = s1, s2
    for _ in range(n_steps):
        g1, g2 = grad(u1, u2)
        # Project onto tangent plane of simplex (sum-zero direction subtraction)
        m = (g1 + g2) / 2.0
        g1p, g2p = g1 - m, g2 - m
        u1 -= dt * g1p
        u2 -= dt * g2p
        if u1 < 0.005 or u2 < 0.005 or (u1 + u2) > 0.995:
            break
        pts.append((u1, u2))
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color='black', linewidth=1.0)
    ax.plot(pts[0, 0], pts[0, 1], 'o', color='black', markersize=4,
            markerfacecolor='white', markeredgewidth=0.7)
    ax.plot(pts[-1, 0], pts[-1, 1], 's', color='black', markersize=5)

# Center (uniform field) marked
ax.plot(1/3, 1/3, '*', color='black', markersize=10,
        markerfacecolor='white', markeredgewidth=0.8)
ax.text(1/3 + 0.02, 1/3 + 0.02, 'uniform $u \\equiv c$\n(saddle)',
        fontsize=8, style='italic')

ax.set_xlabel('$u_1$')
ax.set_ylabel('$u_2$')
ax.set_title('Theorem T14  —  projected gradient flow on  $\\Sigma_m$\n'
             '(simplex with $n = 3$, $m = 1$;  double-well + smoothness energy)')
ax.set_aspect('equal')
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend (manual)
ax.plot([], [], 'o', color='black', markersize=4, markerfacecolor='white',
        markeredgewidth=0.7, label='initial $u^{(0)}$')
ax.plot([], [], 's', color='black', markersize=5, label='endpoint  (critical)')
ax.plot([], [], '*', color='black', markersize=8, markerfacecolor='white',
        markeredgewidth=0.8, label='uniform field  (saddle)')
ax.plot([], [], color='black', linewidth=1.0, label='gradient flow trajectory')
ax.legend(loc='upper right', fontsize=8)

plt.tight_layout()
out = _style.output_dir() / 'fig08-gradient-flow'
plt.savefig(out.with_suffix('.svg'))
plt.savefig(out.with_suffix('.png'), dpi=200)
print(f'Saved: {out}.svg / .png')
