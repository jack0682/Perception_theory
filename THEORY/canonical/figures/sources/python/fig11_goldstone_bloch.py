"""F11 — Goldstone Bloch dispersion (Theorem T-V5b-T).

(a)  2D torus T^2: two Goldstone branches near Gamma point with
     commensurability splitting  →  doublet (2-fold).
(b)  1D cycle C_n: single Goldstone branch  →  1-fold.

Bloch eigenvalues approximated from a phenomenological model that
captures the universal Goldstone behavior near k = 0.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import _style; _style.apply()

# ── model parameters ───────────────────────────────────────────────
c_speed = 1.0
delta_split = 0.18  # commensurability splitting magnitude (2D doublet)

def omega_2d_branch(k_path, branch=0):
    """Two Goldstone branches with linear dispersion + small splitting."""
    base = c_speed * np.abs(k_path)
    if branch == 0:
        return base
    return base + delta_split * (1 - np.exp(-2.0 * np.abs(k_path)))

def omega_1d(k_path):
    return c_speed * np.abs(k_path)

# ── Brillouin path ─────────────────────────────────────────────────
n_pts = 400
k = np.linspace(-np.pi, np.pi, n_pts)

# ── plot ───────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# (a) 2D torus — doublet
ax = axes[0]
omega_lower = omega_2d_branch(k, branch=0)
omega_upper = omega_2d_branch(k, branch=1)
ax.plot(k, omega_lower, color='black', linewidth=1.2,
        label='lower Goldstone branch')
ax.plot(k, omega_upper, color='black', linewidth=1.2, linestyle='--',
        label='upper Goldstone branch')
ax.fill_between(k, omega_lower, omega_upper, color='black', alpha=0.06)
# Splitting annotation
ax.annotate('', xy=(0.5, omega_2d_branch(0.5, 1)),
            xytext=(0.5, omega_2d_branch(0.5, 0)),
            arrowprops=dict(arrowstyle='<->', color='black', linewidth=0.7))
ax.text(0.55, (omega_2d_branch(0.5, 0) + omega_2d_branch(0.5, 1)) / 2,
        '  commensurability\n  splitting',
        fontsize=8, style='italic', va='center')
ax.text(0, -0.35, '  doublet (2-fold)', ha='center', fontsize=9, style='italic')
ax.set_xlabel(r'wavevector  $k$  (along high-symmetry path)')
ax.set_ylabel(r'frequency  $\omega(k)$')
ax.set_title('(a)  2D torus  $T^2$:  Goldstone doublet (2-fold)')
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$\Gamma$', r'$\pi/2$', r'$\pi$'])
ax.legend(loc='upper center', fontsize=8)
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-0.5, 4.0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# (b) 1D cycle — single branch
ax = axes[1]
omega1 = omega_1d(k)
ax.plot(k, omega1, color='black', linewidth=1.4, label='Goldstone branch')
ax.text(0, -0.35, '  1-fold', ha='center', fontsize=9, style='italic')
ax.set_xlabel(r'wavevector  $k$')
ax.set_ylabel(r'frequency  $\omega(k)$')
ax.set_title('(b)  1D cycle  $C_n$:  Goldstone (1-fold)')
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$\Gamma$', r'$\pi/2$', r'$\pi$'])
ax.legend(loc='upper center', fontsize=8)
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-0.5, 4.0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.suptitle('Theorem T-V5b-T  —  Pre-Objective Goldstone on translation-invariant graphs\n'
             '(nodal count = 2 universal across graph classes)',
             y=1.04)
plt.tight_layout()
out = Path(__file__).resolve().parents[2] / 'output' / 'fig11-goldstone-bloch'
plt.savefig(out.with_suffix('.svg'))
plt.savefig(out.with_suffix('.png'), dpi=200)
print(f'Saved: {out}.svg / .png')
