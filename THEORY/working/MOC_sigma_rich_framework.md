---
type: MOC
cluster: sigma-rich-cross-cut
id: MOC_sigma_rich_framework
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: σ-Rich Fingerprint (Cross-cutting Q1 / Q2 / Q4)

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]] · [[INDEX|working/INDEX.md]]
> Authority: [[canonical]] σ-Rich definitions; SigmaRich namedtuple
> Status: Working framework, Lipschitz-certified

## Purpose

σ-Rich fingerprint = (sigma_standard, centroids, orientations, wigner_data) 는 응집장의 위상·기하 fingerprint 다. **Q1 (경계 미세구조), Q2 (다중 formation σ), Q4 (K-soft Lipschitz bridge)** 모두에 횡단적으로 사용되므로 cross-cutting MOC 로 분리.

## Core Files — MF/ side

- [[sigma_rich_phi_proof]] — φ-proof for σ-rich
- [[sigma_rich_centroid_derivation]] — Centroid derivation
- [[sigma_rich_orientation_derivation]] — Orientation derivation
- [[sigma_rich_wigner_derivation]] — Wigner derivation
- [[sigma_rich_lipschitz_2026-05-07]] — Lipschitz continuity (L_K ≤ 4·L_φ·n)
- [[sigma_rich_augmentation]] — Augmentation scheme
- [[sigma_rich_VR_phase1]] — VR phase 1
- [[sigma_rich_vs_standard_R23]] — vs standard R23 comparison
- [[commitment_18_sigma_rich_packet]] — Commitment 18 packet
- [[commitments_18_19_drafts]] — Commitments 18/19 combined

## Core Files — SF/ side (algebraic / topological)

- [[sigma_rich_refinement_theorem]] — Refinement theorem
- [[sigma_fingerprint_algorithm]] — Fingerprint algorithm
- [[sigma_fingerprint_qrcode]] — QR-code representation
- [[sigma_class_category]] — Class / category
- [[sigma_lie_algebra_structure]] — Lie algebra structure
- [[sigma_topological_invariance]] — Topological invariance
- [[sigma_uniqueness_theorem]] — Uniqueness theorem
- [[sigma_trajectory_perturbation]] — Trajectory perturbation
- [[sigma_to_crisp_recovery]] — σ → crisp recovery
- [[schramm_sigma_locality_theorem]] — Schramm σ locality
- [[theorem_2g_schramm_restatement]] — Theorem 2g Schramm restatement
- [[formation_fundamental_group]] — Fundamental group
- [[step_cohesion]] — Step cohesion
- [[symmetry_moduli]] — Symmetry moduli
- [[thermal_extension]] — Thermal extension
- [[r22_a2_a1_audit]] — R22 A2/A1 audit

## Code Module

- `CODE/scc/sigma_rich.py` — SigmaRich namedtuple; derived diagnostic of $u_t$.

## Reading Order

1. [[sigma_rich_phi_proof]] (φ 기저)
2. [[sigma_rich_centroid_derivation]] · [[sigma_rich_orientation_derivation]] · [[sigma_rich_wigner_derivation]]
3. [[sigma_rich_lipschitz_2026-05-07]] (Lipschitz certificate)
4. [[sigma_rich_refinement_theorem]]
5. [[sigma_fingerprint_algorithm]]
6. [[schramm_sigma_locality_theorem]] (topological 연결)

## Dependencies

- Requires: [[MOC_Q1_boundary_T8]] (T8 stable formation).
- Feeds into: [[MOC_Q2_multi_formation]] (multi σ), [[MOC_Q4_K_selection]] (K-soft), [[MOC_Q6_sigma_inherit]] (σ-Inheritance time변화).
- Blocked by: H-σ4 (T-σ-Theorem-4 Cat A).

## Current Status (CV-1.16)

- **Canonical:** SigmaRich definition; Lipschitz certificate $L_K \le 4 L_\phi n$.
- **Working:** Lie algebra structure, fundamental group, QR-code representation.
- **Open:** H-σ4 (T-σ-Theorem-4 Cat A), Wigner-projection (T-σ-Inherit Cat C blocker).

## Related Clusters

- [[MOC_Q1_boundary_T8]] · [[MOC_Q2_multi_formation]] · [[MOC_Q4_K_selection]] · [[MOC_Q6_sigma_inherit]]
- [[MOC_hypothesis_tree]] (H-σ4)

---

*MOC_sigma_rich_framework, 2026-05-14.*
