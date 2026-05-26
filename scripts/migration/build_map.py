#!/usr/bin/env python3
"""Generate rename_map.tsv (path-keyed old->new) for the perception-action stack reorg.

Rules are dir-group based with per-file overrides. Already-clear filenames keep
their basename; cryptic dirs are dissolved into the 5-layer stack; the 15 colliding
basenames are de-duplicated; high-traffic hub basenames are FROZEN (never renamed).

Output columns: old_path  new_path  old_basename  new_basename  link_safe_basename
"""
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Hub basenames that must NEVER be renamed (only moved). High inbound-link count.
FROZEN = {
    "THEORY_INDEX", "INDEX", "canonical", "DECLARATION", "theorem_status",
    "hypothesis_tree", "auxiliary_structures_master", "MOC_canonical_authority",
    "MOC_hypothesis_tree", "MOC_sigma_rich_framework", "MOC_open_problems_blockers",
    "MOC_Q1_boundary_T8", "MOC_Q2_multi_formation", "MOC_Q3_stochastic_dynamics",
    "MOC_Q4_K_selection", "MOC_Q5_temporal_identity", "MOC_Q6_sigma_inherit",
    "MOC_research_journal",
    "perception_action_interpretation_pivot_2026_05_21", "PAI_ROADMAP",
    # seals are referenced by exact basename
    "CV-1.13_SEAL", "CV-1.15_SEAL", "CV-1.16_SEAL", "CV-1.17_SEAL",
    "CV-1.18_SEAL", "CV-1.19_SEAL", "CV-1.20_SEAL",
}

# ---- explicit per-file destinations (relative to ROOT). dir, not filename. ----
# loose THEORY/working/*.md
LOOSE = {
    "THEORY/working/INDEX.md": "THEORY/2_substrate/INDEX.md",
    "THEORY/working/README.md": "THEORY/2_substrate/substrate_readme.md",
    "THEORY/working/macro_audit_2026-05-20.md": "THEORY/0_axis/macro_audit_2026-05-20.md",
    "THEORY/working/cold_failure_analysis_2026-05-20.md": "THEORY/0_axis/cold_failure_analysis_2026-05-20.md",
    "THEORY/working/MOC_Q1_boundary_T8.md": "THEORY/2_substrate/Q1_boundary/MOC_Q1_boundary_T8.md",
    "THEORY/working/MOC_Q2_multi_formation.md": "THEORY/2_substrate/Q2_multiformation/MOC_Q2_multi_formation.md",
    "THEORY/working/MOC_Q3_stochastic_dynamics.md": "THEORY/2_substrate/Q3_dynamics/MOC_Q3_stochastic_dynamics.md",
    "THEORY/working/MOC_Q4_K_selection.md": "THEORY/2_substrate/Q4_kselection/MOC_Q4_K_selection.md",
    "THEORY/working/MOC_Q5_temporal_identity.md": "THEORY/4_temporal/MOC_Q5_temporal_identity.md",
    "THEORY/working/MOC_Q6_sigma_inherit.md": "THEORY/4_temporal/MOC_Q6_sigma_inherit.md",
    "THEORY/working/MOC_sigma_rich_framework.md": "THEORY/2_substrate/sigma_framework/MOC_sigma_rich_framework.md",
    "THEORY/working/MOC_open_problems_blockers.md": "THEORY/2_substrate/MOC_open_problems_blockers.md",
}

# canonical/ -> 2_substrate/canonical/ ; declaration+pivot+roadmap -> 0_axis/
CANON = {
    "THEORY/canonical/DECLARATION.md": "THEORY/0_axis/DECLARATION.md",
    "THEORY/canonical/PAI_ROADMAP.md": "THEORY/0_axis/PAI_ROADMAP.md",
    "THEORY/canonical/perception_action_interpretation_pivot_2026_05_21.md": "THEORY/0_axis/perception_action_interpretation_pivot_2026_05_21.md",
    "THEORY/canonical/README.md": "THEORY/2_substrate/canonical/canonical_readme.md",
    "THEORY/canonical/figures/README.md": "THEORY/2_substrate/canonical/figures/figures_readme.md",
}
CANON_SEALS = "THEORY/2_substrate/canonical/seals/"

# SCC_CANONICAL/ -> 2_substrate/canonical/structural/ (rename: strip numeric prefix)
SCT_MAP = {
    "SCC_CANONICAL/00_manifest.md": "sct_manifest.md",
    "SCC_CANONICAL/01_ontology.md": "sct_ontology.md",
    "SCC_CANONICAL/02_axioms_and_primitives.md": "sct_axioms_and_primitives.md",
    "SCC_CANONICAL/03_energy_and_diagnostics.md": "sct_energy_and_diagnostics.md",
    "SCC_CANONICAL/04_theorem_registry.md": "sct_theorem_registry.md",
    "SCC_CANONICAL/05_open_problems.md": "sct_open_problems.md",
    "SCC_CANONICAL/06_forbidden_claims.md": "sct_forbidden_claims.md",
    "SCC_CANONICAL/07_changelog.md": "sct_changelog.md",
    "SCC_CANONICAL/MOC_SCC_CT_v0.1.md": "MOC_SCC_CT_v0.1.md",
}
SCT_DIR = "THEORY/2_substrate/canonical/structural/"

# working/MF: temporal-split files -> 4_temporal ; sigma_rich* -> sigma_framework ;
# pattern-classified into Q dirs; default -> multiformation/
MF_TEMPORAL = {
    "temporal_identity_sharp_form_2026-05-07.md",
    "temporal_identity_perscomp_transport.md",
    "sigma_inherit_k_jump.md",
    "sigma_multi_trajectory.md",
    "cobelonging_vs_sigmaD.md",
}
MF_Q4 = ("k_select", "k_selection", "ksoft", "kbar_kact", "k_status", "f_kstep",
         "reservoir_reinterpretation", "pre_objective_k", "shared_pool",
         "commitment_19", "op_0009", "soft_k_definition")
MF_Q3 = ("pf_tstar", "pf_a1", "n1_kramers", "bernshtein", "self_ref_fp",
         "scc_mass_gap", "foundational_bridges", "mathematical_scaffolding")
MF_Q2 = ("from_single", "emergent_multi", "multi_formation_sigma", "formation_birth",
         "single_high_f", "cn15", "stereo", "cross_validation_stereo", "tst5a")

# dir-group prefix rules (applied if no explicit override matched)
DIR_RULES = [
    ("THEORY/working/sensing_pipeline/", "THEORY/1_sensing/"),
    ("THEORY/working/prolegomena/", "THEORY/3_projections/prolegomena/"),
    ("THEORY/working/temporal/", "THEORY/4_temporal/temporal_audit/"),
    ("THEORY/working/CV114_TEMPORAL_COMPOSITION/", "THEORY/4_temporal/composition/"),
    ("THEORY/working/CV115_ACTION_TEMPORAL_COST/", "THEORY/4_temporal/action_cost/"),
    ("THEORY/working/C/", "THEORY/2_substrate/Q1_boundary/"),
    ("THEORY/working/CE/", "THEORY/2_substrate/Q1_boundary/"),
    ("THEORY/working/E/", "THEORY/2_substrate/foundations/dissolutions/"),
    ("THEORY/working/SF/", "THEORY/2_substrate/sigma_framework/"),
    ("THEORY/working/foundation/proofs/", "THEORY/2_substrate/foundations/manifold/proofs/"),
    ("THEORY/working/foundation/", "THEORY/2_substrate/foundations/manifold/"),
    ("THEORY/working/cssl/", "THEORY/2_substrate/foundations/cssl/"),
    ("THEORY/working/AFD_0/", "THEORY/2_substrate/foundations/AFD/"),
    ("THEORY/working/observer_moduli/", "THEORY/2_substrate/foundations/observer_moduli/"),
    ("THEORY/working/field_equation_framework/", "THEORY/2_substrate/foundations/field_equation/"),
    ("THEORY/working/CV114_H_MORSE_PACKAGEII/", "THEORY/2_substrate/Q3_dynamics/h_morse_packageII/"),
    ("THEORY/canonical/figures/", "THEORY/2_substrate/canonical/figures/"),
    ("THEORY/canonical/", "THEORY/2_substrate/canonical/"),
]


def mf_dest(name):
    low = name.lower()
    if name in MF_TEMPORAL:
        return "THEORY/4_temporal/identity_inheritance/" + name
    if low.startswith("sigma_rich"):
        return "THEORY/2_substrate/sigma_framework/" + name
    if any(p in low for p in MF_Q4):
        return "THEORY/2_substrate/Q4_kselection/" + name
    if any(p in low for p in MF_Q3):
        return "THEORY/2_substrate/Q3_dynamics/" + name
    if any(p in low for p in MF_Q2):
        return "THEORY/2_substrate/Q2_multiformation/" + name
    return "THEORY/2_substrate/multiformation/" + name


def compute_new(old):
    name = Path(old).name
    if old in LOOSE:
        return LOOSE[old]
    if old in CANON:
        return CANON[old]
    if old in SCT_MAP:
        return SCT_DIR + SCT_MAP[old]
    if old == "THEORY_INDEX.md":
        return old  # frozen at root
    if re.match(r"THEORY/canonical/CV-1\.\d+_SEAL\.md$", old):
        return CANON_SEALS + name
    if old.startswith("THEORY/working/MF/"):
        return mf_dest(name)
    for pre, dest in DIR_RULES:
        if old.startswith(pre):
            return dest + old[len(pre):]
    return None  # unmapped -> leave in place


def main():
    # files in scope: everything under THEORY/working, THEORY/canonical, SCC_CANONICAL,
    # plus THEORY_INDEX.md. (0_axis files already placed are out of scope.)
    scope = []
    for base in ["THEORY/working", "THEORY/canonical", "SCC_CANONICAL"]:
        scope += [str(p.relative_to(ROOT)) for p in (ROOT / base).rglob("*") if p.is_file()]
    scope.append("THEORY_INDEX.md")

    rows = []
    for old in sorted(scope):
        new = compute_new(old)
        if new is None or new == old:
            continue
        rows.append([old, new, Path(old).stem, Path(new).stem])

    # --- de-dup pass: any moved file whose new basename collides (with another
    # moved file OR a stationary file) gets its immediate parent-dir name prefixed,
    # unless the basename is frozen. Iterate to a fixed point. ---
    def current_basename_index():
        bn = defaultdict(list)
        for p in ROOT.rglob("*.md"):
            if "/.git/" in str(p):
                continue
            rel = str(p.relative_to(ROOT))
            if rel in {r[0] for r in rows}:
                continue
            bn[Path(rel).stem].append(rel)
        for r in rows:
            bn[Path(r[1]).stem].append(r[1])
        return bn

    for _ in range(5):
        bn = current_basename_index()
        coll = {b for b, v in bn.items() if len(v) > 1}
        changed = False
        for r in rows:
            nb = Path(r[1]).stem
            if nb in coll and nb not in FROZEN:
                parent = Path(r[1]).parent.name
                newname = f"{parent}_{nb}.md"
                r[1] = str(Path(r[1]).parent / newname)
                r[3] = Path(r[1]).stem
                changed = True
        if not changed:
            break

    # Build the full post-migration basename set to flag collisions.
    moved_old = {r[0] for r in rows}
    post = {}  # new_path -> count via basename
    # start from files NOT moved (stay in place) excluding those being moved
    final_paths = []
    for p in ROOT.rglob("*.md"):
        if "/.git/" in str(p):
            continue
        rel = str(p.relative_to(ROOT))
        if rel in moved_old:
            continue
        final_paths.append(rel)
    for r in rows:
        final_paths.append(r[1])
    bn = defaultdict(list)
    for fp in final_paths:
        bn[Path(fp).stem].append(fp)

    collisions = {b for b, v in bn.items() if len(v) > 1}

    # mark link safety; frozen basenames asserted unique (will verify)
    out = ["\t".join(["old_path", "new_path", "old_basename", "new_basename", "link_safe_basename"])]
    collision_rows = []
    for old, new, ob, nb in rows:
        safe = "yes" if nb not in collisions else "COLLISION"
        if nb in collisions:
            collision_rows.append((old, new, nb))
        out.append("\t".join([old, new, ob, nb, safe]))

    (ROOT / "scripts/migration/rename_map.tsv").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"rows: {len(rows)}")
    print(f"post-migration basename collisions: {sorted(collisions)}")
    # frozen sanity: each frozen basename must be globally unique post-migration
    bad_frozen = [f for f in FROZEN if f in collisions]
    print(f"FROZEN-but-colliding (must fix): {bad_frozen}")
    if collision_rows:
        print("collision rows:")
        for old, new, nb in collision_rows:
            print(f"  {nb}: {old} -> {new}")


if __name__ == "__main__":
    main()
