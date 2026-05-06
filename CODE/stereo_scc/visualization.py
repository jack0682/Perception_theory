"""Visualization utilities for stereo-SCC experiments.

All functions save to file (no interactive display) to support
headless experiment execution.
"""
from __future__ import annotations

import os
import numpy as np


def save_field_image(
    u: np.ndarray,
    grid_shape: tuple[int, int],
    filename: str,
    title: str = "Cohesion field u",
    vmin: float = 0.0,
    vmax: float = 1.0,
) -> None:
    """Save a 2D cohesion field as a heatmap image.

    Args:
        u: Field values, shape (n,) where n = rows*cols
        grid_shape: (rows, cols)
        filename: Output file path (.png)
        title: Plot title
        vmin, vmax: Color scale range
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rows, cols = grid_shape
    fig, ax = plt.subplots(figsize=(5, 5))
    im = ax.imshow(u.reshape(rows, cols), vmin=vmin, vmax=vmax, cmap="viridis", origin="lower")
    plt.colorbar(im, ax=ax)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    fig.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close(fig)


def save_persistence_curve(
    thresholds: np.ndarray,
    n_components: np.ndarray,
    filename: str,
    rho_pers: float | None = None,
    K_act: int | None = None,
    title: str = "Persistence filtration: #components vs threshold",
) -> None:
    """Save persistence filtration curve.

    Args:
        thresholds: Threshold values (decreasing)
        n_components: Component count at each threshold
        filename: Output path (.png)
        rho_pers: If given, mark the persistence threshold
        K_act: If given, annotate the persistent component count
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(thresholds, n_components, "b-", lw=2)
    ax.set_xlabel("Threshold θ")
    ax.set_ylabel("# connected components")
    ax.set_title(title)

    if K_act is not None:
        ax.axhline(K_act, color="r", ls="--", lw=1.5, label=f"K_act={K_act} (PersComp)")
        ax.legend()

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    fig.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close(fig)


def save_barrier_comparison(
    labels: list[str],
    barriers: list[float],
    filename: str,
    title: str = "Merger barriers: flat vs stereo",
) -> None:
    """Bar chart comparing merger barriers across conditions.

    Args:
        labels: Condition names
        barriers: Barrier values
        filename: Output path (.png)
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.arange(len(labels))
    ax.bar(x, barriers, color=["steelblue", "firebrick"] + ["gray"] * max(0, len(labels) - 2))
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=15)
    ax.set_ylabel("Barrier height ΔE")
    ax.set_title(title)

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    fig.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close(fig)


def save_markov_trajectory(
    times: np.ndarray,
    states: np.ndarray,
    filename: str,
    K_max: int | None = None,
    title: str = "K_act(t) Markov trajectory",
) -> None:
    """Step-function plot of K_act(t) Markov chain trajectory.

    Args:
        times: Event times
        states: K_act state at each event
        filename: Output path (.png)
        K_max: Maximum K for y-axis
        title: Plot title
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.step(times, states, where="post", lw=2, color="darkblue")
    ax.set_xlabel("Time t")
    ax.set_ylabel("K_act(t)")
    ax.set_title(title)
    if K_max is not None:
        ax.set_ylim(-0.5, K_max + 0.5)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    fig.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close(fig)


def save_free_energy_curve(
    K_values: np.ndarray,
    F_values: np.ndarray,
    filename: str,
    T_star: float | None = None,
    title: str = "Effective free energy F(K)",
) -> None:
    """Plot F(K) vs K curve.

    Args:
        K_values: Formation count values
        F_values: Free energy values (same shape)
        filename: Output path (.png)
        T_star: Temperature annotation
        title: Plot title
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(K_values, F_values, "o-", lw=2, color="darkgreen")
    k_min = K_values[np.argmin(F_values)]
    ax.axvline(k_min, color="r", ls="--", lw=1.5, label=f"K*={k_min}")
    ax.set_xlabel("K")
    ax.set_ylabel("F(K) - F(0)")
    label = title + (f" (T*={T_star:.3f})" if T_star is not None else "")
    ax.set_title(label)
    ax.legend()
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    fig.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close(fig)
