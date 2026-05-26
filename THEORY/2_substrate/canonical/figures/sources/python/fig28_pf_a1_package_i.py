"""F28 — P-F-A1 Package I: stochastic foundation for T* on Sigma_M (CV-1.8 -> CV-1.9).

Four-step canonical chain: AR -> SDE -> GI -> PE.
T-P-F-e0 shown as prerequisite (dashed side box).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import _style; _style.apply()

OUT = _style.output_dir()

fig, ax = plt.subplots(figsize=(12.0, 5.8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5.8)
ax.axis('off')

BOX_W, BOX_H = 2.35, 2.10
Y_CHAIN = 2.60   # vertical centre of main chain

# ── main chain boxes ───────────────────────────────────────────────
chain = [
    ('T-PF-A1-AR', 'Affine Reduction', 'Cat A  (CV-1.8)',
     r'$\widetilde{\Sigma}_M$ is a bounded' '\nconvex polytope.'
     '\nLions-Sznitman domain\ncondition satisfied.', 1.60),
    ('T-PF-A1-SDE', 'Reflected SDE', 'Cat A  (CV-1.8)',
     'Well-posed Langevin on\n'
     r'$\widetilde{\Sigma}_M$:' ' existence\n+ uniqueness (Tanaka\npathwise).', 4.50),
    ('T-PF-A1-GI', 'Unique Gibbs\nInvariant Measure', 'Cat A  (CV-1.9)',
     r'Unique $\pi_{T_*} \propto e^{-\tilde{\mathcal{E}}/T_*}$.' '\n'
     'Zero-current + L²(π)\nkernel argument.\n'
     r'Stationarity proved.', 7.50),
    ('T-PF-A1-PE', 'Poincaré Ineq. +\nExponential Ergodicity', 'Cat A  (CV-1.9)',
     r'$\lambda_1 \geq \frac{\pi^2}{n}e^{-\mathrm{osc}/T_*}$.' '\n'
     'Payne-Weinberger\n+ Holley-Stroock.\n'
     'TV convergence explicit.', 10.40),
]

for (tid, name, cat, body, cx) in chain:
    box = FancyBboxPatch((cx - BOX_W/2, Y_CHAIN - BOX_H/2), BOX_W, BOX_H,
                          boxstyle='round,pad=0.09',
                          fc='white', ec='black', lw=0.95)
    ax.add_patch(box)
    ax.text(cx, Y_CHAIN + BOX_H/2 - 0.22, tid,
            ha='center', va='top', fontsize=9.0, fontweight='bold')
    ax.text(cx, Y_CHAIN + BOX_H/2 - 0.52, name,
            ha='center', va='top', fontsize=8.0, style='italic')
    ax.text(cx, Y_CHAIN - BOX_H/2 + 0.25, cat,
            ha='center', va='bottom', fontsize=7.5)
    ax.text(cx, Y_CHAIN + 0.08, body,
            ha='center', va='center', fontsize=7.0, linespacing=1.40)

# Arrows between chain boxes
x_pairs = [
    (1.60 + BOX_W/2, 4.50 - BOX_W/2),
    (4.50 + BOX_W/2, 7.50 - BOX_W/2),
    (7.50 + BOX_W/2, 10.40 - BOX_W/2),
]
for x0, x1 in x_pairs:
    ap = FancyArrowPatch((x0, Y_CHAIN), (x1, Y_CHAIN),
                          arrowstyle='->', mutation_scale=13,
                          lw=1.1, color='black', shrinkA=3, shrinkB=3)
    ax.add_patch(ap)

# ── T-P-F-e0 prerequisite box (dashed, above GI) ──────────────────
cx_pfe0, y_pfe0 = 7.50, 5.15
side_w, side_h = 3.10, 0.78
side_box = FancyBboxPatch((cx_pfe0 - side_w/2, y_pfe0 - side_h/2), side_w, side_h,
                            boxstyle='round,pad=0.07',
                            fc='white', ec='black', lw=0.7, ls='dashed')
ax.add_patch(side_box)
ax.text(cx_pfe0, y_pfe0 + 0.17, 'T-P-F-ε₀   (Cat A, CV-1.7)',
        ha='center', va='center', fontsize=8.5, fontweight='bold')
ax.text(cx_pfe0, y_pfe0 - 0.16,
        r'$\mu_\varepsilon \Rightarrow \mu_0$ weakly as $\varepsilon\to0$'
        '  —  Gibbs regularity prerequisite',
        ha='center', va='center', fontsize=7.5, style='italic')

ap2 = FancyArrowPatch((cx_pfe0, y_pfe0 - side_h/2),
                       (cx_pfe0, Y_CHAIN + BOX_H/2),
                       arrowstyle='->', mutation_scale=9,
                       lw=0.75, color='black', ls='dashed',
                       shrinkA=3, shrinkB=3)
ax.add_patch(ap2)

# ── footer callout ─────────────────────────────────────────────────
footer = (
    r'P-F-A1 Package I: well-posed SDE on $\widetilde{\Sigma}_M$'
    ' + unique Gibbs invariant measure'
    r' + exponential ergodicity with explicit rate $\lambda_1$.'
    '\n'
    r'Package II (Eyring-Kramers explicit rates) is OP-0021 (W9+).   '
    r'$T_*$ canonical registration remains open.'
)
ax.text(6.0, 0.38, footer,
        ha='center', va='center', fontsize=7.5, style='italic',
        bbox=dict(boxstyle='round,pad=0.30', fc='white', ec='black',
                  lw=0.55, alpha=0.95))

ax.set_title(
    r'P-F-A1 Package I — Stochastic Foundation for $T_*$ on $\widetilde{\Sigma}_M$'
    '   (CV-1.8 -> CV-1.9, fully Cat A)',
    fontsize=10.5, pad=8)

plt.tight_layout()
out = OUT / 'fig28-pf-a1-package-i'
plt.savefig(out.with_suffix('.png'), dpi=200, bbox_inches='tight')
print(f'Saved → {out}.png')
