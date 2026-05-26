"""F13 — SCC hero theorem dependency DAG, updated to CV-1.11.

Foundation → Phase+Stability → W4 → W5 → W6 Stochastic → W6 Boundary+Selection.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import _style; _style.apply()

OUT = _style.output_dir()

fig, ax = plt.subplots(figsize=(11.0, 13.0))
ax.set_xlim(0, 10)
ax.set_ylim(-1.0, 12.5)
ax.axis('off')

# ── bands ──────────────────────────────────────────────────────────
bands = [
    ('Foundation',                   10.3, 12.2),
    ('Phase + Stability',             7.8, 10.3),
    ('W4 Capstone',                   5.5,  7.8),
    ('W5 Multi-Formation Bridge',     3.6,  5.5),
    ('W6  Stochastic Foundation',     1.3,  3.6),
    ('W6  Boundary + Selection',     -1.0,  1.3),
]
for label, y0, y1 in bands:
    ax.axhspan(y0, y1, color='black', alpha=0.05, zorder=0)
    ax.text(-0.2, (y0 + y1) / 2, label, va='center', ha='right',
            fontsize=8, style='italic', clip_on=False)

for y in [10.3, 7.8, 5.5, 3.6, 1.3]:
    ax.axhline(y, color='black', lw=0.4, ls='--', alpha=0.35)

# ── nodes: (label_top, label_bottom, x, y) ─────────────────────────
BOX_W, BOX_H = 1.80, 0.70
nodes = {
    # Foundation
    'T20':     ('[ T20 ]',            'Axiom Consistency',                      2.0, 11.2),
    'T1':      ('[ T1 ]',             'Existence',                              5.0, 11.2),
    'T6':      ('[ T6 ]',             'Closure FP (Banach)',                     8.0, 11.2),
    # Phase + Stability
    'T8':      ('[ T8-Core ]',        'Phase Transition',                       1.6,  9.0),
    'T7':      ('[ T7-Enhanced ]',    'Metastability',                          3.7,  9.0),
    'T11':     ('[ T11 ]',            'Γ-Convergence',                          6.0,  9.0),
    'T14':     ('[ T14 ]',            'Gradient Flow',                          8.3,  9.0),
    # W4 Capstone
    'PreObj':  ('[ T-PreObj-1 ]',     'Pre-Objective Mechanism  (W4)',           3.2,  6.65),
    'V5bT':    ('[ T-V5b-T ]',        'Pre-Objective Goldstone  (W4)',           7.2,  6.65),
    # W5 Bridge
    'L1F':     ('[ T-L1-F ]',         'Hard-Bar / Active-Count Bridge  (W5)',   4.2,  4.55),
    # W6 Stochastic Foundation
    'Pfe0':    ('[ T-P-F-ε₀ ]',       'Gibbs Continuity  (eps->0)',             1.2,  2.45),
    'AR':      ('[ T-PF-A1-AR ]',     'Affine Reduction',                       3.2,  2.45),
    'SDE':     ('[ T-PF-A1-SDE ]',    'Reflected SDE',                          5.2,  2.45),
    'GI':      ('[ T-PF-A1-GI ]',     'Unique Gibbs  π_{T*}',                   7.0,  2.45),
    'PE':      ('[ T-PF-A1-PE ]',     'Poincaré + Ergodicity',                  8.8,  2.45),
    # W6 Boundary + Selection
    'OP6B':    ('[ T-OP6-B ]',        'Boundary Precision\nOP-0006 RESOLVED',   1.8,  0.20),
    'KSelPF':  ('[ T-K-Select-PF ]',  'Equil. K-Selection\nOP-0005-EQ partial', 4.8,  0.20),
    'KSelOBS': ('[ T-K-Select-OBS ]', 'Obs. K-Selection\nOP-0005-OBS partial',  8.0,  0.20),
}

pos = {}
for key, (top, bot, x, y) in nodes.items():
    pos[key] = (x, y)
    box = FancyBboxPatch((x - BOX_W/2, y - BOX_H/2), BOX_W, BOX_H,
                          boxstyle='round,pad=0.07',
                          fc='white', ec='black', lw=0.85, zorder=2)
    ax.add_patch(box)
    ax.text(x, y + 0.12, top, ha='center', va='center',
            fontsize=8.5, fontweight='bold', zorder=3)
    ax.text(x, y - 0.17, bot, ha='center', va='center',
            fontsize=7.0, style='italic', zorder=3)

# ── arrows ─────────────────────────────────────────────────────────
edges = [
    ('T20', 'T8'), ('T1', 'T8'), ('T1', 'T7'), ('T1', 'T11'), ('T1', 'T14'),
    ('T6', 'T8'), ('T6', 'T7'),
    ('T8', 'PreObj'), ('T7', 'PreObj'), ('T11', 'PreObj'), ('T14', 'PreObj'),
    ('PreObj', 'V5bT'), ('PreObj', 'L1F'), ('PreObj', 'OP6B'),
    ('L1F', 'KSelPF'), ('L1F', 'KSelOBS'),
    ('AR', 'SDE'), ('SDE', 'GI'), ('GI', 'PE'),
    ('GI', 'KSelPF'), ('GI', 'KSelOBS'),
]
for src, dst in edges:
    x0, y0 = pos[src]
    x1, y1 = pos[dst]
    ap = FancyArrowPatch(
        posA=(x0, y0), posB=(x1, y1),
        arrowstyle='->', mutation_scale=10,
        lw=0.65, color='black',
        shrinkA=24, shrinkB=24,
        connectionstyle='arc3,rad=0.0', zorder=1
    )
    ax.add_patch(ap)

ax.set_title('Logical dependencies among the SCC hero theorems  (CV-1.11, 2026-05-06)',
             fontsize=11, pad=10)
ax.text(5.0, -0.9,
        'Each arrow: lower theorem uses the upper one in its proof or formulation.   '
        '[A] = Cat A resolved   [B] = Cat B partial',
        ha='center', va='top', fontsize=8, style='italic')

plt.tight_layout()
out = OUT / 'fig13-hero-dependency-dag'
plt.savefig(out.with_suffix('.png'), dpi=200, bbox_inches='tight')
print(f'Saved → {out}.png')
