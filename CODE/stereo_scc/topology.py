"""Topological analysis: K_act via persistent connected components.

K_act(u) = #PersComp(u) via threshold filtration + persistence > rho_pers.

This is the CORRECT definition per Canonical Memo v1.1 §D4.
NOT the slot-count |{j: ||u^(j)||_inf > eps}| which is a K-field artifact.

See: stereo_scc_canonical_memo_v1.1.md §D4, §D5
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import scipy.sparse.csgraph as csgraph


def connected_components_threshold(
    adj: sp.spmatrix,
    u: np.ndarray,
    threshold: float,
) -> tuple[int, np.ndarray]:
    """Count connected components of the subgraph {x: u(x) > threshold}.

    Args:
        adj: Sparse adjacency matrix (n, n)
        u: Cohesion field, shape (n,)
        threshold: Level-set threshold

    Returns:
        n_components: Number of connected components (integer)
        labels: Component label for each node (-1 if below threshold)
    """
    mask = u > threshold
    if not mask.any():
        return 0, np.full(len(u), -1, dtype=int)

    # Restrict adjacency to superlevel set
    adj_sub = adj.toarray()[np.ix_(mask, mask)]
    n_comp, comp_labels_sub = csgraph.connected_components(
        sp.csr_matrix(adj_sub), directed=False
    )

    labels = np.full(len(u), -1, dtype=int)
    active_idx = np.where(mask)[0]
    labels[active_idx] = comp_labels_sub
    return n_comp, labels


def component_persistence_curve(
    adj: sp.spmatrix,
    u: np.ndarray,
    n_thresholds: int = 200,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute the persistence filtration curve: #components vs threshold.

    Sweeps threshold from u.max() down to 0, tracking connected component
    births and deaths (H_0 persistent homology on the graph).

    Args:
        adj: Sparse adjacency (n, n)
        u: Cohesion field, shape (n,)
        n_thresholds: Number of threshold levels to sweep

    Returns:
        thresholds: Array of threshold values (decreasing)
        n_components: Number of components at each threshold
    """
    thresholds = np.linspace(u.max(), 0.0, n_thresholds)
    n_components = np.zeros(n_thresholds, dtype=int)
    for i, t in enumerate(thresholds):
        n_comp, _ = connected_components_threshold(adj, u, t)
        n_components[i] = n_comp
    return thresholds, n_components


def _extract_persistence_bars(
    adj: sp.spmatrix,
    u: np.ndarray,
    n_thresholds: int = 500,
) -> list[tuple[float, float]]:
    """Extract (birth, death) pairs for H_0 persistent components.

    Uses the elder rule: when two components merge at threshold t,
    the younger one (born at lower threshold) dies; the older one persists.

    Returns:
        bars: List of (birth, death) threshold pairs. Death=0 for essential bars.
    """
    thresholds = np.linspace(u.max(), 0.0, n_thresholds)
    bars: list[tuple[float, float]] = []

    prev_n = 0
    component_births: dict[int, float] = {}

    for t in thresholds:
        n_comp, labels = connected_components_threshold(adj, u, t)

        if n_comp > prev_n:
            for c in range(n_comp):
                if c not in component_births:
                    component_births[c] = t

        if n_comp < prev_n:
            n_deaths = prev_n - n_comp
            birth_times = sorted(component_births.values())
            for birth_t in birth_times[-n_deaths:]:
                bars.append((birth_t, t))
                for k, v in list(component_births.items()):
                    if v == birth_t:
                        del component_births[k]
                        break

        prev_n = n_comp

    # Remaining components persist to threshold 0 (essential bars)
    for birth_t in component_births.values():
        bars.append((birth_t, 0.0))

    return bars


def persistent_component_count(
    adj: sp.spmatrix,
    u: np.ndarray,
    rho_pers: float = 0.05,
    n_thresholds: int = 500,
) -> int:
    """K_act(u) = #PersComp(u): number of components with persistence > rho_pers.

    This implements the correct K_act definition (Canonical Memo v1.1 §D4):
    apply threshold filtration, keep only components with
    persistence = (birth_threshold - death_threshold) > rho_pers.

    Args:
        adj: Sparse adjacency (n, n)
        u: Cohesion field, shape (n,)
        rho_pers: Persistence threshold (minimum bar length to count)
        n_thresholds: Resolution of the filtration sweep

    Returns:
        K_act: Integer number of persistent components
    """
    bars = _extract_persistence_bars(adj, u, n_thresholds)
    persistent = sum(1 for (birth, death) in bars if (birth - death) > rho_pers)
    return persistent


def slot_count_kact(
    u_fields: list[np.ndarray],
    epsilon: float,
) -> int:
    """K-field slot-count: |{j: max(u^(j)) > epsilon}|.

    THIS IS THE WRONG DEFINITION per Canonical Memo v1.1 §D4.
    Included here for comparison only. This is a K-field architecture artifact.

    Args:
        u_fields: List of per-formation fields u^(1), ..., u^(K_field)
        epsilon: Activation threshold

    Returns:
        K_act_slot: Slot-count integer (biased upward relative to PersComp)
    """
    return sum(1 for u in u_fields if u.max() > epsilon)
