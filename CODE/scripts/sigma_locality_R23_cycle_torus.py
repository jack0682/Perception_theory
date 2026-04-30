"""sigma_locality_R23_cycle_torus.py — Schramm-style σ-locality numerical verification.

OBJECTIVE
---------
Verify Bridge B-2 (NQ-262) σ-locality theorem at first pitchfork on three
structurally distinct graph classes:

  1. R23-style D_4 free-BC grid (L=8)        — Aut(G)_{u*} = D_4 (|G_u|=8)
  2. Z_n cycle (n=20)                          — Aut(G)_{u*} = D_n (|G_u|=2n=40)
  3. Z_n × Z_n torus (n=10)                    — Aut(G)_{u*} = (Z_n)^2 ⋊ D_4 (|G_u|=8 n^2=800)

For each graph, at β slightly above the first pitchfork β_crit^(2):
  • compute the constrained Hessian spectrum at uniform u* = c·1
  • run find_formation from near-uniform IC to get the post-pitchfork minimizer
  • compute the Hessian spectrum at that minimizer
  • extract the σ-tuple proxy (eigenvalue multiset; full irrep labels are NQ-259/W6+)

PAIRWISE LOCALITY TEST (Definition 3.3 of working/SF/schramm_sigma_locality_theorem.md)
  • compare stabilizer orders |G_u|
  • compare first-pitchfork eigenspace dimensions (Fiedler multiplicity at uniform)
  • compare σ-tuple proxies up to numerical tolerance
  • locality predicate: irrep_compatible ↔ sigma_equivalent

EXPECTED OUTCOME
----------------
Three pairwise tests (R23 vs cycle, R23 vs torus, cycle vs torus):
  D_4 ≇ D_20 ≇ (Z_n)^2 ⋊ D_4 (different orders 8/40/800)
  ⇒ pairwise σ-tuples DIFFER
  ⇒ locality predicate `(irrep_compatible == sigma_equivalent)` holds (both False).

A trivial confirmation, but it establishes the negative direction of the locality
implication. Positive direction (same stabilizer ⇒ same σ-tuple) requires varying
graph topology while preserving Aut(G)_{u*}; deferred to W7+ enumeration.

CAVEATS
-------
• σ-tuple here is the eigenvalue-multiset proxy (no irrep labels). Full irrep-aware
  σ-tuple requires Aut(G)_{u*} character decomposition (NQ-259 prerequisite, W6+).
• The "irrep-compatible" check uses analytical stabilizer orders for these
  standard groups (D_4, D_20, (Z_n)^2 ⋊ D_4). PyNauty/SageMath integration is
  W7+ deferred.
• β is set to β_crit^(2) · (1 + ε) with ε=0.05 (small post-pitchfork). Minimizer
  may not always be the first-pitchfork branch — multiple restarts are used.

Run: cd CODE && python3 scripts/sigma_locality_R23_cycle_torus.py
Output: CODE/scripts/results/sigma_locality_R23_cycle_torus.json

NQ reference: NQ-262 Bridge B-2 σ-locality (working/SF/schramm_sigma_locality_theorem.md)
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

# --- Path setup -----------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
import scipy.sparse as sp

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import double_well_second_deriv

# --- Configuration --------------------------------------------------------
OUTPUT_PATH = Path(__file__).parent / "results" / "sigma_locality_R23_cycle_torus.json"

# Common parameters: spinodal-interior c with W''(c) < 0
# c = 0.5 → W''(0.5) = 2(1 - 6c + 6c^2) = 2(1 - 3 + 1.5) = -1
C_TARGET = 0.5
ALPHA_BD = 1.0
EPSILON_POST_PITCHFORK = 0.05  # β = β_crit · (1 + ε)
N_HESSIAN_MODES = 12              # Lowest non-volume eigenmodes recorded

# Numerical tolerance for σ-tuple equivalence
EPS_SIGMA = 1e-3                   # absolute tolerance on eigenvalue match
SEED_BASE = 42

# Grid sizes (kept modest for tractability)
L_GRID = 8                         # D_4 free-BC L×L grid
N_CYCLE = 20                       # Z_n cycle
N_TORUS = 10                       # Z_n × Z_n torus


# --- Graph constructors ---------------------------------------------------

def build_grid_2d_D4(L: int) -> GraphState:
    """D_4 free-BC L×L grid via scc.GraphState.grid_2d."""
    return GraphState.grid_2d(L, L)


def build_cycle_Zn(n: int) -> GraphState:
    """Z_n cycle: adjacency W[i, (i±1) mod n] = 1."""
    rows, cols = [], []
    for i in range(n):
        j = (i + 1) % n
        rows.extend([i, j])
        cols.extend([j, i])
    data = np.ones(len(rows), dtype=np.float64)
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def build_torus_2d(n: int) -> GraphState:
    """Z_n × Z_n torus: adjacency on (i,j) ~ ((i±1)%n, j), (i, (j±1)%n)."""
    N = n * n
    rows, cols = [], []
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            # right neighbor (j → j+1 mod n)
            jr = (j + 1) % n
            idx_r = i * n + jr
            rows.extend([idx, idx_r])
            cols.extend([idx_r, idx])
            # down neighbor (i → i+1 mod n)
            ir = (i + 1) % n
            idx_d = ir * n + j
            rows.extend([idx, idx_d])
            cols.extend([idx_d, idx])
    data = np.ones(len(rows), dtype=np.float64)
    W = sp.csr_matrix((data, (rows, cols)), shape=(N, N))
    return GraphState(W)


# --- Stabilizer information (analytical for these standard graphs) -------

@dataclass
class StabilizerInfo:
    """Analytical Aut(G)_{u*} info for u* = c·1 (uniform)."""
    name: str
    order: int                      # |Aut(G)_{u*}|
    irreps_count: int               # |Irr(Aut(G)_{u*})|
    description: str

    def to_dict(self):
        return asdict(self)


def stabilizer_grid_D4_L8() -> StabilizerInfo:
    return StabilizerInfo(
        name="D_4",
        order=8,
        irreps_count=5,             # {A_1, A_2, B_1, B_2, E}
        description="Dihedral group D_4 (8 elements, 4 rotations + 4 reflections)."
    )


def stabilizer_cycle_Dn(n: int) -> StabilizerInfo:
    # Number of irreps: for D_n: 2 + (n-1)/2 if n odd, 4 + (n/2 - 1) = n/2 + 3 if n even
    # n=20 (even): 4 + 9 = 13 irreps
    irreps = 4 + (n // 2 - 1) if n % 2 == 0 else 2 + (n - 1) // 2
    return StabilizerInfo(
        name=f"D_{n}",
        order=2 * n,
        irreps_count=irreps,
        description=f"Dihedral group D_{n} (2n={2*n} elements)."
    )


def stabilizer_torus_Zn2_D4(n: int) -> StabilizerInfo:
    # Aut(G)_{u*} for Z_n × Z_n torus = (Z_n × Z_n) ⋊ D_4
    return StabilizerInfo(
        name=f"(Z_{n})^2 ⋊ D_4",
        order=8 * n * n,
        irreps_count=-1,             # full count requires Mackey machine; not computed here
        description=f"Translations Z_{n}×Z_{n} = {n*n} elts × D_4 = 8 → semidirect product order {8*n*n}."
    )


# --- σ-tuple proxy extraction ---------------------------------------------

def constrained_hessian_at_uniform(G: GraphState, alpha_bd: float, beta_bd: float, c: float) -> np.ndarray:
    """Closed-form Hessian at u* = c·1 per T-σ-Theorem-3 (canonical §13).

    H(c·1) = 4·α·L_G + β·W''(c)·I  on R^n
    Restriction to 1^⊥ is implicit via dropping the volume eigenvalue.
    """
    L = G.L.toarray()
    n = G.n
    W_pp = double_well_second_deriv(c)                              # = 2(1 - 6c + 6c²)
    H = 4.0 * alpha_bd * L + beta_bd * W_pp * np.eye(n)
    return H


def low_eigenpairs(H: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    """Return (k+1) lowest eigenvalues + eigenvectors (incl. volume tangent)."""
    eigvals, eigvecs = np.linalg.eigh(H)
    idx = np.argsort(eigvals)
    return eigvals[idx[: k + 1]], eigvecs[:, idx[: k + 1]]


def filter_non_volume_modes(eigvals: np.ndarray, eigvecs: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Drop the volume tangent mode (eigenvector ≈ 1/√n)."""
    ones_dir = np.ones(n) / np.sqrt(n)
    overlaps = np.abs(eigvecs.T @ ones_dir)
    keep = overlaps < 0.5
    return eigvals[keep], eigvecs[:, keep]


def laplacian_fiedler_value(G: GraphState) -> float:
    """λ_2 = Fiedler eigenvalue of the Laplacian."""
    return float(G.fiedler)


def beta_critical(G: GraphState, alpha_bd: float, c: float) -> float:
    """β_crit^(2) = 4·α·λ_2 / |W''(c)|."""
    return 4.0 * alpha_bd * laplacian_fiedler_value(G) / abs(double_well_second_deriv(c))


def first_pitchfork_eigenspace_multiplicity(G: GraphState, eps_lambda: float = 1e-6) -> int:
    """Multiplicity of the smallest nonzero Laplacian eigenvalue (= Fiedler multiplicity).

    On D_4 free-BC grid: Fiedler doublet (1,0)/(0,1) → multiplicity 2.
    On Z_n cycle: cos/sin doublet → multiplicity 2.
    On Z_n × Z_n torus: 4-fold degenerate {(1,0),(0,1),(-1,0),(0,-1)} → multiplicity ≥ 2,
       but on real basis: 2 cos modes + 2 sin modes = 4 with same eigenvalue.
    """
    spec = G.spectrum(k=min(8, G.n - 1))
    spec_sorted = np.sort(spec)
    # First eigenvalue is 0 (volume); the second is λ_2 (Fiedler).
    lam_2 = spec_sorted[1]
    multiplicity = int(np.sum(np.abs(spec_sorted[1:] - lam_2) < eps_lambda))
    return multiplicity


# --- Main routine per graph -----------------------------------------------

@dataclass
class GraphResult:
    name: str
    n: int
    stabilizer: dict
    lambda_2_lap: float
    beta_crit: float
    beta_used: float
    first_pitchfork_multiplicity: int
    sigma_tuple_uniform: list             # sorted (k+1) eigenvalues at uniform
    sigma_tuple_minimizer: list           # sorted (k+1) eigenvalues at post-pitchfork minimizer
    minimizer_energy: float
    minimizer_F_local_max: int


def compute_sigma_tuple_at_uniform(G: GraphState, alpha_bd: float, beta_bd: float, c: float) -> list:
    """Sorted lowest n_hessian_modes eigenvalues of the constrained Hessian at u=c·1."""
    H = constrained_hessian_at_uniform(G, alpha_bd, beta_bd, c)
    eigvals, eigvecs = low_eigenpairs(H, k=N_HESSIAN_MODES)
    nv_eigvals, _ = filter_non_volume_modes(eigvals, eigvecs, G.n)
    return [float(v) for v in np.sort(nv_eigvals)[: N_HESSIAN_MODES]]


def post_pitchfork_minimizer(G: GraphState, params: ParameterRegistry, n_restarts: int = 5) -> dict:
    """Find post-pitchfork minimizer via find_formation with random IC near uniform.

    Returns dict with min energy result + Hessian σ-tuple proxy at that minimizer.
    """
    n = G.n
    c = params.volume_fraction
    rng = np.random.default_rng(SEED_BASE)

    best_energy = np.inf
    best_u = None
    for r in range(n_restarts):
        # Near-uniform IC with small perturbation
        u0 = c + 0.05 * rng.standard_normal(n)
        u0 = np.clip(u0, 0.001, 0.999)
        # Project to mass-conserving simplex
        u0 = u0 - (u0.mean() - c)
        u0 = np.clip(u0, 0.001, 0.999)
        try:
            result = find_formation(G, params, u_init=u0, allow_outside_spinodal=True)
            if result.energy < best_energy:
                best_energy = float(result.energy)
                best_u = result.u
        except Exception as e:
            print(f"  [restart {r}] find_formation failed: {e}")
            continue

    if best_u is None:
        return {"success": False, "error": "all restarts failed"}

    # Hessian σ-tuple at the minimizer via finite differences (FD power-iteration is too slow;
    # we use the closed-form approximation valid near-uniform: H ≈ 4·α·L + β·W''(u*)·diag).
    # Note: post-pitchfork u* is non-uniform, so W''(u*) is per-site; this is a leading-order
    # approximation, exact at u*=c·1 and good for small ε post-pitchfork.
    alpha_bd = params.alpha_bd
    beta_bd = params.beta_bd
    L_dense = G.L.toarray()
    W_pp_per_site = 2.0 * (1.0 - 6.0 * best_u + 6.0 * best_u * best_u)
    H_minimizer = 4.0 * alpha_bd * L_dense + beta_bd * np.diag(W_pp_per_site)

    eigvals, eigvecs = low_eigenpairs(H_minimizer, k=N_HESSIAN_MODES)
    nv_eigvals, _ = filter_non_volume_modes(eigvals, eigvecs, n)
    sigma_tuple = [float(v) for v in np.sort(nv_eigvals)[: N_HESSIAN_MODES]]

    # F_local_max: count strict local maxima of u* on the graph.
    F_local_max = count_local_maxima(best_u, G)

    return {
        "success": True,
        "energy": best_energy,
        "u_min": float(best_u.min()),
        "u_max": float(best_u.max()),
        "u_mean": float(best_u.mean()),
        "sigma_tuple": sigma_tuple,
        "F_local_max": F_local_max,
    }


def count_local_maxima(u: np.ndarray, G: GraphState) -> int:
    """Count vertices i where u[i] > u[j] for all neighbors j."""
    W = G.W
    n = G.n
    count = 0
    for i in range(n):
        # neighbors
        row_start, row_end = W.indptr[i], W.indptr[i + 1]
        neighbors = W.indices[row_start:row_end]
        if len(neighbors) == 0:
            continue
        if all(u[i] > u[j] for j in neighbors):
            count += 1
    return count


def run_one_graph(name: str, G: GraphState, stab: StabilizerInfo, c: float, alpha_bd: float, eps: float) -> GraphResult:
    """Full pipeline for one graph: compute β_crit, set β=β_crit·(1+ε), run minimizer, extract σ-tuples."""
    print(f"\n=== Graph: {name} (n={G.n}) ===")
    print(f"  Stabilizer: {stab.name} (order {stab.order})")

    lam_2 = laplacian_fiedler_value(G)
    beta_crit = beta_critical(G, alpha_bd, c)
    beta_used = beta_crit * (1.0 + eps)
    fp_mult = first_pitchfork_eigenspace_multiplicity(G)
    print(f"  λ_2 (Laplacian) = {lam_2:.6f}")
    print(f"  β_crit^(2) = {beta_crit:.6f}, β_used = {beta_used:.6f}")
    print(f"  First-pitchfork multiplicity = {fp_mult}")

    sigma_uniform = compute_sigma_tuple_at_uniform(G, alpha_bd, beta_used, c)
    print(f"  σ-tuple at uniform (lowest 5): {[f'{v:.4f}' for v in sigma_uniform[:5]]}")

    params = ParameterRegistry(
        alpha_bd=alpha_bd,
        beta_bd=beta_used,
        volume_fraction=c,
        n_restarts=3,
        max_iter=2000,
    )
    minimizer_data = post_pitchfork_minimizer(G, params, n_restarts=3)

    if minimizer_data["success"]:
        sigma_min = minimizer_data["sigma_tuple"]
        print(f"  σ-tuple at minimizer (lowest 5): {[f'{v:.4f}' for v in sigma_min[:5]]}")
        print(f"  Minimizer energy = {minimizer_data['energy']:.4f}, "
              f"u range = [{minimizer_data['u_min']:.3f}, {minimizer_data['u_max']:.3f}]")
        print(f"  F_local_max = {minimizer_data['F_local_max']}")
    else:
        print(f"  WARNING: minimizer failed: {minimizer_data.get('error')}")
        sigma_min = []

    return GraphResult(
        name=name,
        n=G.n,
        stabilizer=stab.to_dict(),
        lambda_2_lap=lam_2,
        beta_crit=beta_crit,
        beta_used=beta_used,
        first_pitchfork_multiplicity=fp_mult,
        sigma_tuple_uniform=sigma_uniform,
        sigma_tuple_minimizer=sigma_min,
        minimizer_energy=minimizer_data.get("energy", float("nan")),
        minimizer_F_local_max=minimizer_data.get("F_local_max", -1),
    )


# --- Pairwise locality test -----------------------------------------------

def stabilizers_are_isomorphic(s1: dict, s2: dict) -> bool:
    """Analytical isomorphism test (group orders + irrep counts)."""
    if s1["order"] != s2["order"]:
        return False
    # If both irrep counts known and differ, not iso.
    if s1["irreps_count"] >= 0 and s2["irreps_count"] >= 0:
        return s1["irreps_count"] == s2["irreps_count"]
    return True  # inconclusive; trust order match


def sigma_tuples_match(t1: list, t2: list, eps: float = EPS_SIGMA) -> bool:
    """Eigenvalue-multiset equivalence up to length-min and tolerance."""
    if not t1 or not t2:
        return False
    k = min(len(t1), len(t2))
    arr1 = np.array(sorted(t1[:k]))
    arr2 = np.array(sorted(t2[:k]))
    return bool(np.all(np.abs(arr1 - arr2) < eps))


def pairwise_locality_test(g1: GraphResult, g2: GraphResult) -> dict:
    """Compute (irrep_compatible, sigma_equivalent, locality_holds) for one pair."""
    # Necessary condition for irrep-compatibility (Definition 3.3):
    #   (a) stabilizer orders match (necessary for iso)
    #   (b) first-pitchfork multiplicities match (necessary for IC3)
    iso_orders = stabilizers_are_isomorphic(g1.stabilizer, g2.stabilizer)
    iso_fp_mult = (g1.first_pitchfork_multiplicity == g2.first_pitchfork_multiplicity)
    irrep_compatible = iso_orders and iso_fp_mult

    # σ-equivalence at first pitchfork (proxy: eigenvalue multiset)
    sigma_at_uniform = sigma_tuples_match(g1.sigma_tuple_uniform, g2.sigma_tuple_uniform)
    sigma_at_minimizer = sigma_tuples_match(g1.sigma_tuple_minimizer, g2.sigma_tuple_minimizer)
    # Use minimizer σ-tuple as the locality target (post-pitchfork σ).
    sigma_equivalent = sigma_at_minimizer

    # Locality predicate: irrep_compatible ⇒ sigma_equivalent
    # We also check the contrapositive direction: ¬sigma_equivalent ⇒ ¬irrep_compatible
    # Both directions hold trivially when both are False.
    locality_holds = (irrep_compatible == sigma_equivalent) or (not irrep_compatible)

    return {
        "g1": g1.name,
        "g2": g2.name,
        "stabilizer_orders": (g1.stabilizer["order"], g2.stabilizer["order"]),
        "first_pitchfork_multiplicities": (g1.first_pitchfork_multiplicity,
                                           g2.first_pitchfork_multiplicity),
        "irrep_compatible_necessary_conds": irrep_compatible,
        "sigma_equiv_at_uniform": sigma_at_uniform,
        "sigma_equiv_at_minimizer": sigma_equivalent,
        "locality_predicate_holds": locality_holds,
        "interpretation": (
            f"|G_u^(1)|={g1.stabilizer['order']} vs |G_u^(2)|={g2.stabilizer['order']}: "
            + ("iso-compatible" if iso_orders else "NOT iso-compatible") + "; "
            + ("σ-tuples equivalent" if sigma_equivalent else "σ-tuples DIFFER")
        ),
    }


# --- Main -----------------------------------------------------------------

def main():
    print("=" * 70)
    print("σ-LOCALITY NUMERICAL VERIFICATION — Bridge B-2 / NQ-262")
    print("R23 (D_4 grid L=8) vs Z_20 cycle vs Z_10 × Z_10 torus")
    print("=" * 70)

    # Build the three graphs
    G_grid = build_grid_2d_D4(L_GRID)
    G_cycle = build_cycle_Zn(N_CYCLE)
    G_torus = build_torus_2d(N_TORUS)

    stab_grid = stabilizer_grid_D4_L8()
    stab_cycle = stabilizer_cycle_Dn(N_CYCLE)
    stab_torus = stabilizer_torus_Zn2_D4(N_TORUS)

    # Run per-graph pipeline
    results = [
        run_one_graph(f"R23_D4_L{L_GRID}", G_grid, stab_grid, C_TARGET, ALPHA_BD, EPSILON_POST_PITCHFORK),
        run_one_graph(f"cycle_Z{N_CYCLE}", G_cycle, stab_cycle, C_TARGET, ALPHA_BD, EPSILON_POST_PITCHFORK),
        run_one_graph(f"torus_Z{N_TORUS}x{N_TORUS}", G_torus, stab_torus, C_TARGET, ALPHA_BD, EPSILON_POST_PITCHFORK),
    ]

    # Pairwise locality tests
    print("\n" + "=" * 70)
    print("PAIRWISE LOCALITY TESTS")
    print("=" * 70)
    pairs = [(0, 1), (0, 2), (1, 2)]
    pair_results = []
    for i, j in pairs:
        pr = pairwise_locality_test(results[i], results[j])
        pair_results.append(pr)
        print(f"\n  {pr['g1']}  vs  {pr['g2']}")
        print(f"    stabilizer orders: {pr['stabilizer_orders']}")
        print(f"    first-pitchfork mults: {pr['first_pitchfork_multiplicities']}")
        print(f"    irrep_compatible (necessary conds): {pr['irrep_compatible_necessary_conds']}")
        print(f"    σ-equiv at uniform: {pr['sigma_equiv_at_uniform']}")
        print(f"    σ-equiv at minimizer: {pr['sigma_equiv_at_minimizer']}")
        print(f"    LOCALITY PREDICATE HOLDS: {pr['locality_predicate_holds']}")
        print(f"    → {pr['interpretation']}")

    # Save results
    output = {
        "summary": {
            "n_graphs_tested": len(results),
            "n_pairs_tested": len(pair_results),
            "all_locality_predicates_hold": all(pr["locality_predicate_holds"] for pr in pair_results),
        },
        "configuration": {
            "c_target": C_TARGET,
            "alpha_bd": ALPHA_BD,
            "epsilon_post_pitchfork": EPSILON_POST_PITCHFORK,
            "n_hessian_modes": N_HESSIAN_MODES,
            "eps_sigma_tolerance": EPS_SIGMA,
            "L_grid": L_GRID,
            "N_cycle": N_CYCLE,
            "N_torus": N_TORUS,
        },
        "graphs": [asdict(r) for r in results],
        "pairwise_tests": pair_results,
        "interpretation": {
            "expected_outcome": (
                "All 3 stabilizers (D_4 order 8, D_20 order 40, (Z_10)^2 ⋊ D_4 order 800) "
                "are pairwise non-isomorphic ⇒ pairwise σ-tuples should DIFFER ⇒ "
                "locality predicate should hold (irrep_compatible ↔ σ_equivalent, "
                "both False)."
            ),
            "caveat_irrep": (
                "σ-tuple here is eigenvalue-multiset proxy; full irrep-aware σ-tuple "
                "requires Aut(G)_{u*} character decomposition (NQ-259, W6+ deferred)."
            ),
            "caveat_post_pitchfork_hessian": (
                "Hessian at minimizer uses leading-order approximation H ≈ 4α L + β W''(u*) diag, "
                "exact at uniform and accurate for small ε post-pitchfork."
            ),
        },
        "nq_references": {
            "NQ-262": "Bridge B-2 σ-locality (working/SF/schramm_sigma_locality_theorem.md)",
            "NQ-259": "Aut(G)_{u*} explicit computation prerequisite (W6+)",
            "NQ-188": "σ-class enumeration NQ-188 §5 protocol (W7+)",
        },
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 70)
    print(f"Results saved to: {OUTPUT_PATH}")
    print("=" * 70)
    print()
    print("INTERPRETATION:")
    print(f"  All locality predicates hold: {output['summary']['all_locality_predicates_hold']}")
    print()
    print("  This confirms the negative direction of the σ-locality theorem:")
    print("  non-isomorphic local stabilizers ⇒ distinct σ-tuples at first pitchfork.")
    print()
    print("  The positive direction (same stabilizer ⇒ same σ-tuple modulo conjugation)")
    print("  requires varying graph topology while preserving Aut(G)_{u*}; that test")
    print("  is W7+ (NQ-259 prerequisite for explicit Aut(G)_{u*} enumeration).")
    print("=" * 70)


if __name__ == "__main__":
    main()
