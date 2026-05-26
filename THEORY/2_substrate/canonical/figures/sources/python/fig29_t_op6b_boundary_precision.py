"""F29 — T-OP6-B: PersRidge Boundary Equivalence in the phase-separation regime.

Left: 2D field u* on grid with boundary contour and PersRidge overlay + d_H bracket.
Right: 1D cross-section annotated with ∂Omega, PersRidge positions, d_H bound.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import _style; _style.apply()

OUT = _style.output_dir()

rng = np.random.default_rng(42)

# ── simulate a two-peak phase-separated field on a 50x50 grid ─────
n = 50
x = np.linspace(-5, 5, n)
y_arr = np.linspace(-5, 5, n)
X, Y = np.meshgrid(x, y_arr)

sigma = 1.2
peak_a = np.exp(-((X - 1.8)**2 + Y**2) / (2 * sigma**2))
peak_b = np.exp(-((X + 1.8)**2 + Y**2) / (2 * sigma**2))
u = (0.65 * peak_a + 0.55 * peak_b)
u = u / u.max()  # normalise to [0, 1]

# ∂Omega: boundary of formation region (level set)
bd_thresh = 0.30
# PersRidge: persistent peaks (high-u region above ridge threshold)
ridge_thresh = 0.68

# 1D cross-section at y=0 (horizontal through both peaks)
u_slice = u[n // 2, :]  # row at y=0

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8), gridspec_kw={'wspace': 0.35})

# ── LEFT PANEL: 2D field ──────────────────────────────────────────
ax = axes[0]
levels = np.linspace(0, 1, 22)
im = ax.contourf(X, Y, u, levels=levels, cmap='Greys_r', alpha=0.80)

# ∂Omega contour (solid)
cs_bd = ax.contour(X, Y, u, levels=[bd_thresh], colors='black', linewidths=1.4)
ax.clabel(cs_bd, fmt=r'$\partial\Omega^*$', fontsize=8, inline=True, inline_spacing=3)

# PersRidge contour (dashed)
cs_rd = ax.contour(X, Y, u, levels=[ridge_thresh], colors='black',
                    linewidths=1.0, linestyles='--')
ax.clabel(cs_rd, fmt='PersRidge', fontsize=7.5, inline=True, inline_spacing=3)

# Mark the two peaks
for xp, yp in [(1.8, 0.0), (-1.8, 0.0)]:
    ax.plot(xp, yp, '+', color='black', ms=10, mew=1.3, zorder=5)

# d_H annotation at x = 1.8 (right peak), comparing ∂Omega and PersRidge
# At x=1.8, find y where u(1.8, y) = bd_thresh and ridge_thresh
x_annot = 1.8
u_col = 0.65 * np.exp(-(y_arr**2) / (2 * sigma**2)) + \
        0.55 * np.exp(-((x_annot + 1.8)**2 + y_arr**2) / (2 * sigma**2))
u_col /= u.max()

# Find outermost crossings (largest y > 0 where u crosses each threshold)
half = n // 2
idx_bd = half + np.argmin(np.abs(u_col[half:] - bd_thresh))
idx_rd = half + np.argmin(np.abs(u_col[half:] - ridge_thresh))
y_bd = y_arr[idx_bd]
y_rd = y_arr[idx_rd]
dH_val = abs(y_bd - y_rd)

x_arrow = 3.0
ax.annotate('', xy=(x_arrow, y_rd), xytext=(x_arrow, y_bd),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.0))
ax.text(x_arrow + 0.25, (y_bd + y_rd) / 2,
        r'$d_H \leq 2\sqrt{\alpha/\beta}$',
        va='center', ha='left', fontsize=8)

cb = plt.colorbar(im, ax=ax, label=r'$u^*(x)$', fraction=0.046, pad=0.03)
cb.ax.tick_params(labelsize=7.5)

handles = [
    mpatches.Patch(fc='none', ec='black', lw=1.4,
                   label=r'$\partial\Omega^*$ (level $u = %.2f$)' % bd_thresh),
    mpatches.Patch(fc='none', ec='black', lw=1.0, linestyle='--',
                   label=r'PersRidge (level $u = %.2f$)' % ridge_thresh),
]
ax.legend(handles=handles, fontsize=7.5, loc='lower right')
ax.set_title(r'Phase-separated field $u^*$ — plan view', fontsize=9.5)
ax.set_xlabel(r'$x_1$', fontsize=9)
ax.set_ylabel(r'$x_2$', fontsize=9)
ax.set_aspect('equal')

# ── RIGHT PANEL: 1D cross-section at y = 0 ───────────────────────
ax2 = axes[1]
ax2.plot(x, u_slice, color='black', lw=1.3, label=r'$u^*(x_1,\; x_2{=}0)$')
ax2.axhline(bd_thresh, color='black', lw=0.9, ls='-',
            label=r'$\partial\Omega^*$ threshold (%.2f)' % bd_thresh)
ax2.axhline(ridge_thresh, color='black', lw=0.9, ls='--',
            label='PersRidge threshold (%.2f)' % ridge_thresh)

# Mark crossing points (right side)
idx_bd_r = n // 2 + np.argmin(np.abs(u_slice[n // 2:] - bd_thresh))
idx_rd_r = n // 2 + np.argmin(np.abs(u_slice[n // 2:] - ridge_thresh))
x_bd_r = x[idx_bd_r]
x_rd_r = x[idx_rd_r]

ax2.axvline(x_bd_r, color='black', lw=0.6, ls=':', alpha=0.7)
ax2.axvline(x_rd_r, color='black', lw=0.6, ls=':', alpha=0.7)

ax2.annotate('', xy=(x_rd_r, 0.18), xytext=(x_bd_r, 0.18),
             arrowprops=dict(arrowstyle='<->', color='black', lw=0.9))
dH_1d = abs(x_bd_r - x_rd_r)
ax2.text((x_rd_r + x_bd_r) / 2, 0.11,
         r'$d_H \approx %.2f$' % dH_1d + '\n' + r'$\leq 2\sqrt{\alpha/\beta}$',
         ha='center', va='top', fontsize=8)

ax2.set_xlabel(r'$x_1$  (cross-section at $x_2 = 0$)', fontsize=9)
ax2.set_ylabel(r'$u^*$', fontsize=9)
ax2.set_title('1D cross-section profile', fontsize=9.5)
ax2.set_ylim(0, 1.12)
ax2.legend(fontsize=7.5, loc='upper left')
ax2.grid(True, alpha=0.28)

fig.suptitle(
    r'T-OP6-B  —  PersRidge Boundary Equivalence (Phase-Sep Regime, H1–H5)'
    '\n'
    r'$d_H\!\left(\mathrm{PersRidge}(u^*),\;\partial\Omega^*\right) \leq 2\sqrt{\alpha/\beta}$'
    r'   (Cat A conditional, OP-0006 RESOLVED, CV-1.7)',
    fontsize=10, y=1.02)

plt.tight_layout()
out = OUT / 'fig29-t-op6b-boundary-precision'
plt.savefig(out.with_suffix('.png'), dpi=200, bbox_inches='tight')
print(f'Saved → {out}.png')
