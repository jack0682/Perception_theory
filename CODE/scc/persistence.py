"""Persistence-based morphological quality measure Q_morph.

Wrappers for test compatibility (grid_size-based API).
Core implementation in scc.diagnostics._persistence_h0_graph.
"""

from __future__ import annotations

import numpy as np

from scc.graph import GraphState
from scc.diagnostics import _persistence_h0_graph, inside_predicate


def persistence_h0(u: np.ndarray, grid_size: tuple[int, int] | int) -> list[tuple[float, float]]:
    """Compute H0 persistence diagram of superlevel-set filtration.

    Parameters
    ----------
    u : field values (length n = rows*cols for grid)
    grid_size : (rows, cols) tuple or single int for square grid

    Returns
    -------
    List of (birth, death) pairs for each bar, sorted by length descending.
    The longest bar (surviving component) has death=0.
    """
    if isinstance(grid_size, int):
        grid_size = (grid_size, grid_size)
    rows, cols = grid_size
    graph = GraphState.grid_2d(rows, cols)

    l_max, l_second = _persistence_h0_graph(u, graph)

    # Reconstruct bars from the Union-Find computation
    # Re-run the full computation to get all bars
    n = graph.n
    order = np.argsort(-u)

    W_coo = graph.W.tocoo()
    adj: list[list[int]] = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    active = np.zeros(n, dtype=bool)
    bars: list[tuple[float, float]] = []

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        active[idx] = True
        birth_val[idx] = u[idx]

        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            if birth_val[ri] >= birth_val[rn]:
                bars.append((float(birth_val[rn]), float(u[idx])))
                parent[rn] = ri
            else:
                bars.append((float(birth_val[ri]), float(u[idx])))
                parent[ri] = rn

    # Add the infinite bar (surviving component): birth=max(u), death=0
    bars.append((float(np.max(u)), 0.0))

    # Sort by bar length descending
    bars.sort(key=lambda bd: bd[0] - bd[1], reverse=True)
    return bars


def q_morph(u: np.ndarray, grid_size: tuple[int, int] | int) -> float:
    """Morphological quality measure Q_morph = l_max * Artic.

    l_max: length of longest persistence bar.
    Artic = 1 - l_second/l_max: articulation ratio.
    """
    if isinstance(grid_size, int):
        grid_size = (grid_size, grid_size)
    rows, cols = grid_size
    graph = GraphState.grid_2d(rows, cols)
    return inside_predicate(u, graph)
