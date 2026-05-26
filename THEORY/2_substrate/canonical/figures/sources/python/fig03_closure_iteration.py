"""F3 — Closure operator iteration trajectory.

(a)  1D field profiles u^(k) at iterations 0, 1, 3, 10, infty
(b)  Geometric convergence ‖u^(k+1) − u^(k)‖_2 vs k  (Banach contraction)
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import _style; _style.apply()

# ── 1D domain + closure operator ───────────────────────────────────
N = 100
x = np.linspace(0, 1, N)

def P_op(u):
    """3-point local aggregation."""
    pu = np.zeros_like(u)
    pu[1:-1] = (u[:-2] + u[1:-1] + u[2:]) / 3.0
    pu[0] = (u[0] + u[1]) / 2.0
    pu[-1] = (u[-2] + u[-1]) / 2.0
    return pu

a_cl, eta, tau = 3.0, 0.5, 0.5  # contraction regime: a_cl < 4

def Cl(u):
    z = a_cl * ((1 - eta) * u + eta * P_op(u) - tau)
    return 1.0 / (1.0 + np.exp(-z))

# ── iterate ────────────────────────────────────────────────────────
np.random.seed(42)
u0 = 0.5 + 0.18 * np.cos(2 * np.pi * x * 3) + 0.12 * np.random.randn(N)
u0 = np.clip(u0, 0.05, 0.95)

n_iter = 60
us = [u0.copy()]
diffs = []
u = u0.copy()
for _ in range(n_iter):
    u_new = Cl(u)
    diffs.append(np.linalg.norm(u_new - u))
    us.append(u_new.copy())
    u = u_new

# ── plot ───────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# (a) profiles
ax = axes[0]
specs = [(0, ':', 0.8), (1, '-.', 0.9), (3, '--', 1.0),
         (10, '-', 1.2), (n_iter, '-', 1.6)]
for it, ls, lw in specs:
    label = f'$u^{{({it})}}$' if it < n_iter else r'$u^{(\infty)}$  (fixed point)'
    ax.plot(x, us[it], color='black', linestyle=ls, linewidth=lw, label=label)
ax.set_xlabel('site coordinate $x$')
ax.set_ylabel('$u^{(k)}(x)$')
ax.set_title('(a)  Iteration profiles converge to fixed point')
ax.set_ylim(-0.05, 1.05)
ax.legend(loc='center right', fontsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# (b) convergence curve (log scale)
ax = axes[1]
ks = np.arange(1, n_iter + 1)
ax.semilogy(ks, diffs, color='black', linewidth=1.3, label=r'$\| u^{(k+1)} - u^{(k)} \|_2$')
ax.semilogy(ks, diffs[0] * (a_cl / 4) ** ks, color='black', linewidth=0.8,
            linestyle='--', label=fr'theoretical rate  $a_{{cl}}/4 = {a_cl/4:.2f}$')
ax.set_xlabel('iteration  $k$')
ax.set_ylabel(r'$\| u^{(k+1)} - u^{(k)} \|_2$')
ax.set_title('(b)  Geometric convergence  (Banach contraction, $a_{cl} < 4$)')
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, which='both')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.suptitle(f'Closure operator iteration  '
             rf'($a_{{cl}} = {a_cl}$,  $\eta = {eta}$,  $\tau = {tau}$)',
             y=1.02)
plt.tight_layout()
out = _style.output_dir() / 'fig03-closure-iteration'
plt.savefig(out.with_suffix('.svg'))
plt.savefig(out.with_suffix('.png'), dpi=200)
print(f'Saved: {out}.svg / .png')
