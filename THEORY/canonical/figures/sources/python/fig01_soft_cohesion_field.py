"""F1 — Soft cohesion field u_t : X_t -> [0,1].

A typical formation on a 2D grid: graded participation values rendered
as a grayscale heatmap with overlaid level contours.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import _style; _style.apply()

# ── grid + synthesized formation field ─────────────────────────────
N = 50
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
X, Y = np.meshgrid(x, y)

cx, cy, R, a = 0.5, 0.5, 0.18, 25.0
r = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
u = 1.0 / (1.0 + np.exp(a * (r - R)))

# ── plot ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6.5, 5.5))
im = ax.imshow(u, cmap='gray_r', origin='lower', extent=[0, 1, 0, 1],
               vmin=0, vmax=1, aspect='equal')
contours = ax.contour(X, Y, u, levels=[0.1, 0.3, 0.5, 0.7, 0.9],
                      colors='black', linewidths=0.7, alpha=0.7)
ax.clabel(contours, inline=True, fontsize=7, fmt='%.1f')

ax.set_xlabel('site coordinate $x$')
ax.set_ylabel('site coordinate $y$')
ax.set_title('Soft cohesion field  $u_t : X_t \\to [0,1]$\n'
             '(formation on a 2D grid; level sets $0.1, 0.3, 0.5, 0.7, 0.9$)')
ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)

cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('$u_t(x)$  —  degree of cohesive participation')
cbar.outline.set_linewidth(0.6)

plt.tight_layout()
out = Path(__file__).resolve().parents[2] / 'output' / 'fig01-soft-cohesion-field'
plt.savefig(out.with_suffix('.svg'))
plt.savefig(out.with_suffix('.png'), dpi=200)
print(f'Saved: {out}.svg / .png')
