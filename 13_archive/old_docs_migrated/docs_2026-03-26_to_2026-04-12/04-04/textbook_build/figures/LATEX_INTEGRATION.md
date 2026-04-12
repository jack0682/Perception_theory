# LaTeX Figure Integration Guide

**Date:** 2026-04-04  
**For:** SCC Textbook (Phase 15)

---

## Directory Structure

```
figures/
├── P1_foundations/    ← Part I figures (Ch1-3)
├── P2_formal/        ← Part II figures (Ch4-8)
├── P3_experiments/   ← Part III figures (Ch9-13)
├── P4_applications/  ← Part IV figures (Ch14-15)
├── MANIFEST.csv      ← Master figure list
├── QUALITY_REPORT.md ← Quality check results
└── check_quality.py  ← Automated checker
```

## Including Figures in LaTeX

### Single Figure (standard)

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\textwidth]{figures/P1_foundations/soft_field_10x10.pdf}
  \caption{Soft cohesion field $u_t \in [0,1]^{X_t}$ on a $10 \times 10$ grid.}
  \label{fig:soft-field-10x10}
\end{figure}
```

### Side-by-Side Figures (comparison)

```latex
\begin{figure}[htbp]
  \centering
  \begin{subfigure}[b]{0.48\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/P1_foundations/bind_low.pdf}
    \caption{Low Bind ($\approx 0.2$)}
    \label{fig:bind-low}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.48\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/P1_foundations/bind_high.pdf}
    \caption{High Bind ($\approx 0.85$)}
    \label{fig:bind-high}
  \end{subfigure}
  \caption{Comparison of low and high Bind values on a $10 \times 10$ grid.}
  \label{fig:bind-comparison}
\end{figure}
```

### Three-Panel Figure (time sequence)

```latex
\begin{figure}[htbp]
  \centering
  \begin{subfigure}[b]{0.32\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/P3_experiments/persist_t0.pdf}
    \caption{$t = 0$}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.32\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/P3_experiments/persist_t5.pdf}
    \caption{$t = 5$}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.32\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/P3_experiments/persist_t10.pdf}
    \caption{$t = 10$}
  \end{subfigure}
  \caption{Temporal evolution of a soft cohesion formation, showing field persistence over 10 steps.}
  \label{fig:persist-sequence}
\end{figure}
```

### Full-Width Figure (landscape or complex)

```latex
\begin{figure*}[htbp]
  \centering
  \includegraphics[width=\textwidth]{figures/P3_experiments/lambda2_universality.pdf}
  \caption{Spectral universality: $\beta_c$ vs.\ $\lambda_2$ across 32 graph topologies ($R^2 = 0.9924$).}
  \label{fig:lambda2-universality}
\end{figure*}
```

---

## Sizing Recommendations

| Figure Type | Width Setting | Typical Use |
|------------|--------------|-------------|
| Single figure | `width=0.85\textwidth` | Most standalone figures |
| Side-by-side (2) | `width=0.48\textwidth` each | Comparisons (low/high, before/after) |
| Three-panel | `width=0.32\textwidth` each | Time sequences, parameter sweeps |
| Full-width | `width=\textwidth` | Scatter plots, complex diagrams |
| Small inline | `width=0.6\textwidth` | Simple concept diagrams |

## Positioning Guidelines

| Placement | Code | When to Use |
|-----------|------|-------------|
| Top of page | `[t]` | Reference figures, notation |
| Here if possible | `[htbp]` | Most figures (default) |
| Bottom | `[b]` | Less critical figures |
| Float page | `[p]` | Very large figures |

**General rule:** Use `[htbp]` as default. LaTeX will find the best position.

## File Format Preferences

1. **PDF (vector)** — Preferred for all figures. Scales without quality loss, small file size.
2. **PNG (raster)** — Only for heatmaps or photos where vector is impractical. Use 300dpi minimum.
3. **SVG** — Convert to PDF before including (`inkscape -D input.svg -o output.pdf`).

## Color Scheme Consistency

All figures should use:
- **Field heatmaps:** `viridis` colormap (matplotlib default)
- **Comparison plots:** Blue (#1f77b4) vs Orange (#ff7f0e)
- **Phase diagrams:** Red (unstable) / Blue (stable) / Green (metastable)
- **Background:** White (for print compatibility)
- **Colorbar labels:** Always include range `[0, 1]` for fields, units for physical quantities

## Label and Font Standards

```python
import matplotlib
matplotlib.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'font.family': 'serif',
    'text.usetex': False,  # Set True if LaTeX available
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})
```

## Required LaTeX Packages

```latex
\usepackage{graphicx}     % \includegraphics
\usepackage{subcaption}   % subfigure environment
\usepackage{float}        % [H] placement
```

## Naming Convention

```
{topic}_{detail}.pdf

Examples:
  soft_field_5x5.pdf
  bind_high.pdf
  energy_landscape_cross.pdf
  phase_transition_alpha_beta.pdf
  lambda2_universality.pdf
  transport_kernel.pdf
```

## Caption Style

- **1-2 sentences max**
- First sentence: what the figure shows
- Second sentence (optional): key finding or reference
- Use math mode for symbols: `$u_t$`, `$\lambda_2$`, `$\beta_c$`

**Examples:**
- "Soft cohesion field on a $10 \times 10$ grid with Gaussian initialization."
- "Phase transition diagram in the $(\alpha, \beta)$ plane. The critical boundary $\beta_c = 4\alpha\lambda_2$ separates uniform and patterned regimes."
- "Bind comparison: low ($\approx 0.2$, left) vs.\ high ($\approx 0.85$, right)."

---

*Guide prepared for SCC Textbook Phase 15 figure integration.*
