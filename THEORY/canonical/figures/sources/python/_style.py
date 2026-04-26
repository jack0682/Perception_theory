"""Shared matplotlib style for all SCC canonical figures.

Strict academic-infographic mono aesthetic:
- Black ink on white, no color, no gradients, no decoration.
- Single sans-serif font. Thin line weights.
- Reference: Communications in Mathematical Physics, Annals of Math.
"""
import matplotlib.pyplot as plt


def apply():
    plt.rcParams.update({
        # Background
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'savefig.facecolor': 'white',
        'savefig.bbox': 'tight',
        # Line weight
        'axes.edgecolor': 'black',
        'axes.linewidth': 0.6,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'lines.linewidth': 1.0,
        'lines.color': 'black',
        # Typography
        'font.family': 'sans-serif',
        'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
        'font.size': 10,
        'axes.labelsize': 10,
        'axes.titlesize': 11,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9,
        'figure.titlesize': 12,
        # Tick + grid
        'xtick.color': 'black',
        'ytick.color': 'black',
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.major.width': 0.6,
        'ytick.major.width': 0.6,
        'grid.linewidth': 0.3,
        'grid.alpha': 0.4,
        'grid.color': 'black',
        # Image / colormap
        'image.cmap': 'gray_r',
        # Legend
        'legend.frameon': True,
        'legend.framealpha': 1.0,
        'legend.edgecolor': 'black',
        'legend.fancybox': False,
        # Save
        'savefig.dpi': 200,
    })
