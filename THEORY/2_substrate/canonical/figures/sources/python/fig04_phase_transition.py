"""F4 — Phase transition spectral threshold (Theorem T8-Core).

beta/alpha  >  4 lambda_2 / |W''(c)|

Plot the threshold curve in (c, beta/alpha) space for several graph
families.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import _style; _style.apply()

# ── spinodal range and W''(c) ──────────────────────────────────────
c_min = (3 - np.sqrt(3)) / 6
c_max = (3 + np.sqrt(3)) / 6
c = np.linspace(c_min + 0.005, c_max - 0.005, 300)

def Wpp(c):
    return 2.0 - 12.0 * c + 12.0 * c ** 2

# ── graph families  ────────────────────────────────────────────────
families = [
    (0.10, ':',  r'dense grid graph,  $\lambda_2 = 0.10$'),
    (0.50, '--', r'bounded-diameter graph,  $\lambda_2 = 0.50$'),
    (1.00, '-',  r'expander graph,  $\lambda_2 = 1.00$'),
]

# ── plot ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7.5, 5.5))

for lam2, ls, label in families:
    th = 4.0 * lam2 / np.abs(Wpp(c))
    ax.plot(c, th, color='black', linestyle=ls, linewidth=1.3, label=label)

# Region annotations
ax.text(0.5, 18.0, 'NON-UNIFORM MINIMIZER\n(formation regime)',
        ha='center', va='center', fontsize=10, style='italic')
ax.text(0.5, 0.18, 'UNIFORM MINIMIZER\n(no formation, below threshold)',
        ha='center', va='center', fontsize=10, style='italic')

# Vertical lines at spinodal endpoints
for cv, lbl in [(c_min, '$c_-$'), (c_max, '$c_+$')]:
    ax.axvline(cv, color='black', linewidth=0.5, linestyle='-', alpha=0.4)
    ax.text(cv, 70, lbl, ha='center', va='bottom', fontsize=10)

ax.set_xlabel('volume fraction  $c = m / n$')
ax.set_ylabel(r'phase-transition ratio  $\beta / \alpha$')
ax.set_title('Phase transition threshold  (Theorem T8-Core)\n'
             r'$\beta/\alpha  >  4\lambda_2 / |W^{\prime\prime}(c)|$  '
             r'(spectral universality on connected graphs)')
ax.set_yscale('log')
ax.set_ylim(0.05, 80)
ax.set_xlim(c_min - 0.025, c_max + 0.025)
ax.legend(loc='upper center', fontsize=9)
ax.grid(True, which='both')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = _style.output_dir() / 'fig04-phase-transition'
plt.savefig(out.with_suffix('.svg'))
plt.savefig(out.with_suffix('.png'), dpi=200)
print(f'Saved: {out}.svg / .png')
