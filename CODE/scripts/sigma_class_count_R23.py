"""sigma_class_count_R23.py — Approximate σ-class enumeration on R23 fullscale dataset (56 minimizers).

OBJECTIVE
---------
For each of the 56 stable (Morse=0) minimizers in the R23 fullscale dataset
(exp_orbital_fullscale.json, 32x32 free-BC grid, β=30, α=1, c=0.5),
enumerate the approximate number of distinct σ-classes by grouping minimizers
whose pre-stored Hessian eigenvalue tuples are identical up to 4-decimal rounding.

APPROXIMATION CAVEAT (MANDATORY)
---------------------------------
This script computes an APPROXIMATE σ-class enumeration. The true σ-class
(Commitment 14, canonical §11.1) requires:

  σ(u*) = (F(u*); {(n_k, [ρ_k], λ_k)}_{k})

where [ρ_k] is an irreducible representation (irrep) label of the stabilizer
Aut(G)_{u*}, not merely an eigenvalue. Two minimizers with identical sorted
eigenvalue tuples may still belong to distinct σ-classes if their irrep labels
differ (e.g., A_1 vs A_2 eigenvectors with the same eigenvalue — as occurs at
the D_4 Mulliken tie-break, Commitment 14 O7, CV-1.5.1).

The eigenvalue-only proxy here is a LOWER BOUND on the true number of σ-classes
(it can merge distinct classes that happen to have equal eigenvalues) and an
UPPER BOUND on the true number when rounding is coarse.

TRUE σ-CLASS ENUMERATION (NQ-188 §5 protocol) requires:
  1. Computing Aut(G)_{u*} for each minimizer (NQ-259, W6 deliverable).
  2. Decomposing T_{u*}Σ_m into Aut(G)_{u*}-irreps via character theory.
  3. Identifying the irrep label [ρ_k] for each Hessian eigenvalue block.

That full protocol is a W7+ deliverable. This script provides the eigenvalue-proxy
estimate needed for NQ-258 §5.2 and sigma_lie_algebra_structure.md §8.

ALGORITHM
---------
1. Load R23 cluster_summaries; filter to morse_index == 0 (stable minimizers).
2. For each minimizer: extract the pre-stored eigenvalues list from cluster_summaries.
   These are the n_hessian_modes=12 lowest eigenvalues of H(u*) projected to
   T_{u*}Σ_m (the tangent space with zero-mean constraint, stored from G1b exp).
3. Skip eigenvalue[0] (tangent direction, near zero ~1e-6); use remaining physical
   eigenvalues.
4. Round each eigenvalue to ROUND_DECIMALS=4 significant figures.
5. Sort the rounded tuple (ascending).
6. Augment with F_local_max (formation size) to form the proxy σ-class key:
   key = (F, sorted_rounded_eigenvalue_tuple).
7. Group by key → σ-class count.
8. Report: n_classes_approx, class_size_distribution, per-class breakdown.
9. Save to results/sigma_class_count_R23.json.

Run: cd CODE && python3 scripts/sigma_class_count_R23.py

NQ reference: NQ-258 McKay-spirit conjecture (Cat C, sigma_lie_algebra_structure.md §5)
              NQ-188 §5 protocol target (full irrep-aware enumeration, W7+)
              NQ-259 prerequisite: Aut(G)_{u*} computation for exact σ-classes
"""

import sys
import os
import json
from pathlib import Path
from collections import Counter, defaultdict

# --- Path setup -----------------------------------------------------------
# scc package lives in CODE/scc; add CODE/ to sys.path for import.
# This script lives in CODE/scripts/; parent is CODE/.
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np

# --- Configuration --------------------------------------------------------
R23_PATH = Path(__file__).parent.parent / "results" / "exp_orbital_fullscale.json"
OUTPUT_PATH = Path(__file__).parent / "results" / "sigma_class_count_R23.json"

# Rounding precision for eigenvalue proxy.
# 4 decimals chosen to absorb numerical noise (~1e-4) while separating
# physically distinct eigenvalues (which differ by ~0.1 on R23 data).
ROUND_DECIMALS = 4

# Include F_local_max in the σ-proxy key? (Yes: formations of different size
# cannot be σ-equivalent by definition — Commitment 14 includes F(u*) as the
# first entry of the σ-tuple.)
USE_F_IN_KEY = True

# Minimum number of physical eigenvalues required (after dropping tangent mode).
MIN_EIGS = 2


def load_r23(path: Path) -> dict:
    """Load R23 fullscale JSON and return parsed dict."""
    if not path.exists():
        raise FileNotFoundError(
            f"R23 dataset not found at {path}.\n"
            "Run the fullscale orbital experiment first:\n"
            "  cd CODE && python3 experiments/exp_orbital_fullscale.py\n"
            "(This generates CODE/results/exp_orbital_fullscale.json)"
        )
    with open(path) as f:
        return json.load(f)


def extract_stable_clusters(data: dict) -> list:
    """Filter cluster_summaries to Morse-0 (stable) minimizers."""
    clusters = data.get("cluster_summaries", [])
    stable = [c for c in clusters if c.get("morse_index") == 0]
    return stable


def build_sigma_proxy_key(cluster: dict, round_decimals: int, use_f: bool):
    """Build the approximate σ-class key for a single cluster.

    Returns:
        key: hashable tuple used for grouping.
        meta: dict with raw eigenvalue data for diagnostics.
    """
    eigs_raw = cluster.get("eigenvalues", [])
    F = cluster.get("F_local_max", -1)

    if not eigs_raw:
        return None, {"error": "no eigenvalues stored"}

    eigs = np.array(eigs_raw, dtype=float)

    # Drop the tangent-space eigenvalue (should be near zero).
    # Convention: eigs[0] ≈ 1e-6 is the volume-constraint tangent direction.
    # Physical spectrum starts at eigs[1].
    TANGENT_THRESHOLD = 1e-3
    physical_eigs = eigs[eigs > TANGENT_THRESHOLD]

    if len(physical_eigs) < MIN_EIGS:
        return None, {
            "error": f"too few physical eigenvalues: {len(physical_eigs)}",
            "raw_eigs": list(eigs_raw),
        }

    # Round to ROUND_DECIMALS decimal places.
    rounded = tuple(round(float(e), round_decimals) for e in sorted(physical_eigs))

    if use_f:
        key = (int(F), rounded)
    else:
        key = rounded

    meta = {
        "F": int(F),
        "n_physical_eigs": len(physical_eigs),
        "physical_eigs_sorted": [float(e) for e in sorted(physical_eigs)],
        "rounded_key": rounded,
    }
    return key, meta


def enumerate_sigma_classes(
    stable_clusters: list,
    round_decimals: int = ROUND_DECIMALS,
    use_f: bool = USE_F_IN_KEY,
) -> dict:
    """Main enumeration: group stable minimizers by approximate σ-class key.

    Returns a dict with full statistics.
    """
    key_to_clusters = defaultdict(list)
    skipped = []

    for i, cluster in enumerate(stable_clusters):
        key, meta = build_sigma_proxy_key(cluster, round_decimals, use_f)
        cluster_id = {
            "cluster_key": cluster.get("cluster_key"),
            "F_local_max": cluster.get("F_local_max"),
            "K_step": cluster.get("K_step"),
            "rep_seed": cluster.get("rep_seed"),
            "rep_energy": cluster.get("rep_energy"),
            "morse_index": cluster.get("morse_index"),
            "eigenvalues": cluster.get("eigenvalues", []),
            "proxy_meta": meta,
        }
        if key is None:
            skipped.append(cluster_id)
        else:
            key_to_clusters[key].append(cluster_id)

    # Convert defaultdict to serializable format.
    # Keys are tuples; convert to str for JSON.
    classes = []
    for key, members in key_to_clusters.items():
        classes.append(
            {
                "sigma_proxy_key": str(key),
                "F_value": members[0]["F_local_max"] if use_f else None,
                "eigenvalue_tuple": list(members[0]["proxy_meta"]["rounded_key"]),
                "n_members": len(members),
                "member_seeds": [m["rep_seed"] for m in members],
                "member_energies": [m["rep_energy"] for m in members],
                "member_K_steps": [m["K_step"] for m in members],
            }
        )

    # Sort classes by size descending, then by key string.
    classes.sort(key=lambda x: (-x["n_members"], x["sigma_proxy_key"]))

    # Class size distribution.
    sizes = [c["n_members"] for c in classes]
    size_counts = Counter(sizes)

    return {
        "total_minimizers": len(stable_clusters),
        "n_valid": len(stable_clusters) - len(skipped),
        "n_skipped": len(skipped),
        "n_classes_approx": len(classes),
        "class_size_distribution": {str(k): v for k, v in sorted(size_counts.items())},
        "classes": classes,
        "skipped": skipped,
    }


def print_report(result: dict, config: dict) -> None:
    """Print human-readable report to stdout."""
    print("=" * 70)
    print("APPROXIMATE σ-CLASS ENUMERATION — R23 Fullscale (NQ-188 proxy)")
    print("=" * 70)
    print()
    print(f"Dataset:      {R23_PATH}")
    print(f"Grid:         {config.get('grid')} (n = {32*32} vertices)")
    print(f"Parameters:   α={config.get('alpha')}, β={config.get('beta')}, c={config.get('c')}")
    print(f"Rounding:     {ROUND_DECIMALS} decimal places")
    print(f"F in key:     {USE_F_IN_KEY}")
    print()
    print(f"Total stable minimizers (Morse=0): {result['total_minimizers']}")
    print(f"Valid (sufficient eigenvalues):    {result['n_valid']}")
    print(f"Skipped:                           {result['n_skipped']}")
    print()
    print(f"APPROXIMATE σ-class count:  {result['n_classes_approx']}")
    print()
    print("Class size distribution:")
    for size, count in sorted(result["class_size_distribution"].items()):
        print(f"  Classes of size {size}: {count}")
    print()
    print("Top σ-classes (by size):")
    print(f"  {'Rank':>4}  {'F':>4}  {'Size':>5}  {'Eigenvalue tuple (proxy)':>50}")
    for rank, cls in enumerate(result["classes"][:15], 1):
        eig_str = str(cls["eigenvalue_tuple"][:4]) + ("..." if len(cls["eigenvalue_tuple"]) > 4 else "")
        print(f"  {rank:>4}  {cls['F_value']:>4}  {cls['n_members']:>5}  {eig_str:>50}")
    print()
    print("=" * 70)
    print("CAVEAT: This is an EIGENVALUE-ONLY PROXY for σ-class.")
    print("True σ-class requires irrep labels [ρ_k] of Aut(G)_{u*} (NQ-188 §5 protocol).")
    print("Full irrep-aware enumeration is a W7+ deliverable (requires NQ-259).")
    print("=" * 70)


def main():
    # --- Load data ---
    try:
        data = load_r23(R23_PATH)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        print()
        print("FALLBACK: R23 dataset not available at expected path.")
        print("Saving a stub JSON with dataset_available=false.")
        stub = {
            "dataset_available": False,
            "expected_path": str(R23_PATH),
            "note": (
                "Run the fullscale orbital experiment to generate the dataset: "
                "cd CODE && python3 experiments/exp_orbital_fullscale.py"
            ),
            "parameters_used": {
                "round_decimals": ROUND_DECIMALS,
                "use_f_in_key": USE_F_IN_KEY,
                "min_eigs": MIN_EIGS,
            },
        }
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_PATH, "w") as f:
            json.dump(stub, f, indent=2)
        print(f"Stub written to {OUTPUT_PATH}")
        return

    config = data.get("config", {})
    stable = extract_stable_clusters(data)

    print(f"Loaded R23: {len(data.get('cluster_summaries', []))} total clusters, "
          f"{len(stable)} stable (Morse=0).")

    # --- Enumerate σ-classes ---
    result = enumerate_sigma_classes(stable, ROUND_DECIMALS, USE_F_IN_KEY)

    # --- Report ---
    print_report(result, config)

    # --- Save JSON ---
    output = {
        "dataset_available": True,
        "source": str(R23_PATH),
        "parameters_used": {
            "round_decimals": ROUND_DECIMALS,
            "use_f_in_key": USE_F_IN_KEY,
            "min_eigs": MIN_EIGS,
            "grid": config.get("grid"),
            "alpha": config.get("alpha"),
            "beta": config.get("beta"),
            "c": config.get("c"),
        },
        "total_minimizers": result["total_minimizers"],
        "n_classes_approx": result["n_classes_approx"],
        "class_size_distribution": result["class_size_distribution"],
        "nq_notes": {
            "nq_188": "Full irrep-aware σ-class enumeration (W7+, requires NQ-259).",
            "nq_258": "McKay-spirit conjecture: σ-tuple derivable from Sylow normalizer (Cat C).",
            "nq_259": "Aut(G)_{u*} explicit computation on R23 — prerequisite for true σ-class (W6).",
            "approximation": (
                "This file gives eigenvalue-proxy σ-classes only. "
                "Two minimizers with identical sorted eigenvalue tuples may still be "
                "in distinct σ-classes if their irrep labels differ (e.g., A_1 vs A_2 "
                "at the D_4 Mulliken tie-break, Commitment 14 O7)."
            ),
        },
        "classes_detail": result["classes"],
        "skipped": result["skipped"],
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
