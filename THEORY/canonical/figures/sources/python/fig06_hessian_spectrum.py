"""F6 — T7-Enhanced Hessian eigenvalue spectrum.

Compares closure-Hessian eigenvalues at a fixed point of:
(a)  non-idempotent closure (‖J_Cl‖_op < 1) — n/n positive eigenvalues
(b)  idempotent closure (J^2 = J)         — at most n−k positive
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import _style; _style.apply()

# ── synthesize representative Jacobians ────────────────────────────
np.random.seed(7)
n = 20

# (a) non-idempotent: random matrix with controlled spectral norm in (0, 1)
A = np.random.randn(n, n)
U, S, Vt = np.linalg.svd(A)
S_scaled = 0.3 + 0.5 * (S / S.max())            # singular values in [0.3, 0.8]
J_nonidem = U @ np.diag(S_scaled) @ Vt
H_nonidem = 2.0 * (np.eye(n) - J_nonidem).T @ (np.eye(n) - J_nonidem)
eigs_nonidem = np.sort(np.linalg.eigvalsh(H_nonidem))[::-1]

# (b) idempotent: rank-(n-k) projection
k = 6
basis = np.linalg.qr(np.random.randn(n, n))[0]
J_idem = basis[:, :n - k] @ basis[:, :n - k].T   # projection of rank n-k
H_idem = 2.0 * (np.eye(n) - J_idem).T @ (np.eye(n) - J_idem)
eigs_idem = np.sort(np.linalg.eigvalsh(H_idem))[::-1]
eigs_idem[eigs_idem < 1e-9] = 0.0

# ── plot ───────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(9, 5.2), sharex=True)
idx = np.arange(1, n + 1)
ymax = 1.15 * max(eigs_nonidem.max(), eigs_idem.max())

# (a)
ax = axes[0]
ax.bar(idx, eigs_nonidem, color='black', edgecolor='black', width=0.7)
ax.set_ylabel('eigenvalue  $\\mu_i$')
ax.set_title(f'(a)  Non-idempotent closure  '
             rf'($\| J_{{Cl}}\|_{{op}} < 1$):  '
             rf'{n}/{n} strictly positive')
ax.set_ylim(0, ymax)
ax.text(0.99, 0.93,
        r'$H_{cl} = 2\,(I - J_{Cl})^{\top}(I - J_{Cl})$  is strictly PD',
        transform=ax.transAxes, ha='right', va='top',
        fontsize=9, style='italic')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# (b) — idempotent: zero eigenvalues marked with hollow markers above bars
ax = axes[1]
ax.bar(idx, eigs_idem, color='black', edgecolor='black', width=0.7)
zero_idx = idx[eigs_idem < 1e-9]
ax.scatter(zero_idx, np.zeros_like(zero_idx) + 0.02 * ymax,
           marker='x', color='black', s=40, linewidths=0.9, zorder=3)
ax.text(zero_idx.mean(), 0.10 * ymax,
        f'  $k = {k}$ zero eigenvalues  =  flat directions',
        ha='center', va='bottom', fontsize=9, style='italic')
ax.set_xlabel('eigenvalue index  $i$')
ax.set_ylabel('eigenvalue  $\\mu_i$')
ax.set_title(f'(b)  Idempotent closure  '
             rf'($J_{{Cl}}^{{2}} = J_{{Cl}}$, range dim $= {n - k}$):  '
             rf'{n - k}/{n} positive,  {k} zero')
ax.set_ylim(0, ymax)
ax.set_xticks(idx)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.suptitle('Theorem T7-Enhanced  —  non-idempotent metastability advantage',
             y=1.02)
plt.tight_layout()
out = Path(__file__).resolve().parents[2] / 'output' / 'fig06-hessian-spectrum'
plt.savefig(out.with_suffix('.svg'))
plt.savefig(out.with_suffix('.png'), dpi=200)
print(f'Saved: {out}.svg / .png')
