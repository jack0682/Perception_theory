"""F32 — W6 Canonical Timeline (May 4–8 2026, CV-1.6 → CV-1.11).

Horizontal event timeline: day bands + theorem milestones + CV version bumps.
Companion to fig23 (W5 timeline).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import _style; _style.apply()

OUT = _style.output_dir()

fig, ax = plt.subplots(figsize=(13.0, 6.2))
ax.set_xlim(-0.15, 5.15)
ax.set_ylim(-1.0, 5.8)
ax.axis('off')

# ── Day bands (D1–D6) ──────────────────────────────────────────────
days = [
    (0.0, 'D1\nMay 4'),
    (1.0, 'D2\nMay 5'),
    (2.0, 'D3\nMay 5–6'),
    (3.0, 'D4\nMay 6'),
    (4.0, 'D5\nMay 7'),
    (5.0, 'D6\nMay 8'),
]
for i, (x, label) in enumerate(days):
    color = '0.94' if i % 2 == 0 else '0.98'
    ax.axvspan(x - 0.5, x + 0.5, color=color, zorder=0, lw=0)
    ax.text(x, 5.55, label, ha='center', va='top', fontsize=8.5,
            fontweight='bold', color='0.35')

# ── Main timeline axis ──────────────────────────────────────────────
ax.axhline(2.5, xmin=0.0, xmax=1.0, color='black', lw=0.9, zorder=1)

# ── Events: (day_x, y_offset, marker_y, label, note) ─────────────────
# y_offset: text y above/below the axis
# style: 'A' = Cat A (filled circle), 'B' = Cat B (open circle), 'CV' = version bump, 'OP' = OP resolution
events = [
    # D1: T-ST-5a Cat A, CV-1.6
    (0.0,  3.55, 'A',
     'T-ST-5a  Cat A',
     'Stereo-SCC\n+ Goldstone (T-V5b-T)'),
    (0.0,  1.40, 'CV',
     'CV-1.6  sealed',
     'Stereo-SCC branch\nadded to canonical'),

    # D3: T-OP6-B Cat A, T-P-F-ε0 Cat A, CV-1.7
    (2.0,  4.10, 'A',
     'T-OP6-B  Cat A',
     'Boundary Precision\n(OP-0006 RESOLVED)'),
    (2.0,  3.00, 'A',
     'T-P-F-ε₀  Cat A',
     'Gibbs Continuity\n(eps -> 0)'),
    (2.0,  1.40, 'CV',
     'CV-1.7  sealed',
     'OP-0006 closed\nT-P-F-ε₀-K Cat B'),

    # D3–D4: P-F-A1 Package I (AR→SDE→GI→PE)
    (3.0,  4.55, 'A',
     'P-F-A1 Package I  Cat A',
     'AR->SDE->GI->PE\n(Sessions M-P)'),
    (3.0,  1.40, 'CV',
     'CV-1.8 / CV-1.9',
     'Reflected SDE + Gibbs\ninvariant + ergodicity'),

    # D4: T-K-Select-PF/OBS Cat B, OP-0005 3-way split, CV-1.10
    (3.5,  3.20, 'B',
     'T-K-Select-PF/OBS  Cat B',
     'EQ + OBS branches partial\n(OP-0005 3-way split)'),
    (3.5,  1.40, 'CV',
     'CV-1.10',
     'OP-0005 EQ/OBS/DYN\ntriple split registered'),

    # D5: DECLARATION, HT-3.0, CV-1.11
    (4.0,  3.70, 'OP',
     'DECL-1.0  +  HT-3.0',
     'DECLARATION.md\nhypothesis_tree.md'),
    (4.0,  1.40, 'CV',
     'CV-1.11  sealed',
     '54A / 14B / 5C / 5R\n= 78 claims  (~69%)'),

    # D6: OMS-2.0 Full
    (5.0,  3.55, 'OP',
     'OMS-2.0  Accepted — Full',
     'Observer Moduli Space\nAppendix OMS  §A–§M'),
]

AXIS_Y = 2.5

for evt in events:
    if len(evt) == 5:
        x, y_text, style, label, note = evt
    else:
        continue

    y_text_pos = y_text
    text_va = 'bottom' if y_text_pos > AXIS_Y else 'top'
    dot_y = AXIS_Y

    # Draw vertical tick from axis to text
    line_y0 = AXIS_Y + (0.18 if y_text_pos > AXIS_Y else -0.18)
    line_y1 = y_text_pos + (-0.22 if y_text_pos > AXIS_Y else 0.22)
    ax.plot([x, x], [line_y0, line_y1], color='black', lw=0.6, ls=':',
            zorder=1, alpha=0.7)

    # Dot on timeline
    if style == 'A':
        ax.plot(x, dot_y, 'o', color='black', ms=7, zorder=3)
    elif style == 'B':
        ax.plot(x, dot_y, 'o', mfc='white', mec='black', ms=7, mew=1.3, zorder=3)
    elif style == 'CV':
        ax.plot(x, dot_y, 's', color='black', ms=5, zorder=3)
    elif style == 'OP':
        ax.plot(x, dot_y, 'D', color='black', ms=5.5, zorder=3)

    # Label text (bold)
    ax.text(x, y_text_pos + (0.05 if y_text_pos > AXIS_Y else -0.05),
            label, ha='center', va=text_va, fontsize=8.0, fontweight='bold')
    # Note text (italic, smaller)
    ax.text(x, y_text_pos + (0.30 if y_text_pos > AXIS_Y else -0.30),
            note, ha='center', va=text_va, fontsize=6.8, style='italic',
            color='0.25')

# ── OP-0006 RESOLVED banner ────────────────────────────────────────
ax.annotate('OP-0006\nRESOLVED',
            xy=(2.0, AXIS_Y), xytext=(2.0, -0.25),
            ha='center', va='top', fontsize=7.5, color='black',
            bbox=dict(boxstyle='round,pad=0.20', fc='white', ec='black', lw=0.7),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.6))

# ── Legend ─────────────────────────────────────────────────────────
leg_items = [
    plt.Line2D([0], [0], marker='o', color='w', mfc='black', ms=7,
               label='Cat A theorem proved'),
    plt.Line2D([0], [0], marker='o', color='w', mfc='white', mec='black',
               ms=7, mew=1.3, label='Cat B (partial)'),
    plt.Line2D([0], [0], marker='s', color='w', mfc='black', ms=5,
               label='CV version bump'),
    plt.Line2D([0], [0], marker='D', color='w', mfc='black', ms=5.5,
               label='Infrastructure / OP milestone'),
]
ax.legend(handles=leg_items, loc='lower left', fontsize=7.5,
          bbox_to_anchor=(0.01, 0.01), frameon=True)

# ── Title / footer ─────────────────────────────────────────────────
ax.set_title(
    'W6 Canonical Timeline (2026-05-04 to 2026-05-08)\n'
    r'CV-1.6 $\to$ CV-1.11  —  78 claims (54A / 14B / 5C / 5R, ~69% proved)',
    fontsize=10.5, pad=8)

ax.text(2.5, -0.80,
        'OP-0006 RESOLVED (D3).   OP-0005 -> 3-way split EQ/OBS/DYN (D4).   '
        'OMS-2.0 Accepted — Full (D6).   Next: CV-1.12 via H-SINK.',
        ha='center', va='top', fontsize=7.5, style='italic', color='0.30')

plt.tight_layout()
out = OUT / 'fig32-w6-canonical-timeline'
plt.savefig(out.with_suffix('.png'), dpi=200, bbox_inches='tight')
print(f'Saved → {out}.png')
