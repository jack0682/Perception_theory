"""stereo_scc — SCC-Stereo Soft-to-Crisp Stabilization module.

Implements the framework from stereo_scc_canonical_memo_v1.1.md:
  - Soft cohesion fields on 3D point clouds (fields.py)
  - K_act via persistent connected components (topology.py)
  - Stereo backprojection and pullback (stereo_geometry.py)
  - Ginzburg-Landau energies and merger barriers (energies.py)
  - Kramers rates and K-selection Markov chain (kramers.py)
  - Visualization utilities (visualization.py)

Key definitions:
  K_act(u) = #PersComp(u)  [persistent connected components, NOT slot-count]
  B_K(P)   = {u in F_0(P): K_act(u) = K}  [topological sector]
  Z_K(P)   = integral over B_K(P) of exp(-E/T) Du  [partition function]
"""
from stereo_scc.fields import make_grid_2d, make_depth_separated_grid, gaussian_field, normalize_field
from stereo_scc.topology import persistent_component_count, component_persistence_curve
from stereo_scc.stereo_geometry import depth_from_disparity, backproject_pixels, pullback_field_to_pixels
from stereo_scc.energies import ginzburg_landau_energy, energy_gradient, merger_barrier_estimate
from stereo_scc.kramers import kramers_rate, build_rate_matrix, simulate_markov_chain, stationary_distribution

__all__ = [
    "make_grid_2d", "make_depth_separated_grid", "gaussian_field", "normalize_field",
    "persistent_component_count", "component_persistence_curve",
    "depth_from_disparity", "backproject_pixels", "pullback_field_to_pixels",
    "ginzburg_landau_energy", "energy_gradient", "merger_barrier_estimate",
    "kramers_rate", "build_rate_matrix", "simulate_markov_chain", "stationary_distribution",
]
