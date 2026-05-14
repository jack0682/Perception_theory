> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 01 — Canonical Audit

Agent A (Canonical Auditor) — repository-wide audit of H-MORSE, Package II, and related open problems.

---

## 1. Current canonical status

| Item | Value |
|------|-------|
| CV version | **CV-1.13** (sealed 2026-05-10) |
| Hypothesis tree | HT-3.5 |
| Claim count | **59A / 14B / 5C / 5R = 83 claims** (~71% fully proved) |
| T-Temporal-Identity | **Cat A** (all 4 parts a/b/c/d; W7-CV1.13 seal) |
| H-SINK | **FULLY CLOSED Cat A** (full plan stability via Partial-H-SINK; W7-FINAL) |
| P-F-A1 Package I | **fully Cat A** (T-PF-A1-AR/SDE/GI/PE; CV-1.8–CV-1.9) |
| T-P-F-ε0 | **Cat A** (Gibbs continuity at ε=0; CV-1.7) |
| T-P-F-ε0-K | **Cat B** conditional on H5 (Morse stability); CV-1.7 |
| T-K-Select-PF / T-K-Select-OBS | **Cat B** each (CV-1.10 / CV-1.11) |

**Cat A/B/C/R distribution.** 59 / 14 / 5 / 5 (see `theorem_status.md` for the registry; same numbers stated in CV-1.13_SEAL.md and hypothesis_tree.md HT-3.5).

---

## 2. H-MORSE references (full inventory)

The repository uses **two distinct names** for the Morse-nondegeneracy hypothesis:

### 2.1 "H-MORSE" as a hypothesis-tree node

`THEORY/canonical/hypothesis_tree.md`:

| Line | Content |
|------|---------|
| 29 | `> **H-MORSE / Package II** — Eyring-Kramers + T_* 정규 등록 (Phase 2)` |
| 35 | `*CV-1.13 closed ... Next priority: H-MORSE / Package II (Phase 2) or T-σ-Inherit OP-0008.*` |
| 45 | `\| **H-MORSE** \| Morse 안정성 \| OPEN \| Q3 Package II \| 최상 \| Phase 2 \|` |
| 87 | `H-MORSE ──┐` (critical-path diagram, Phase 2 entry) |
| 168–184 | Q3 block: H-MORSE = "∀ critical point u* of E on Σ_m, Hessian H(u*)\|_{T_{u*}Σ_m} has μ_min > 0 (mod symmetry-zero eigenvalues)". Approach: T7-Enhanced based + Allen-Cahn Morse transition. Numerical: μ_min ∈ [0.96, 60.2] across configurations. Effect of closing: T-PF-ε0-K Cat B → Cat A; Package II entry; H-SR auxiliary. |

**Status:** **OPEN, MAJOR (top priority Phase 2).**

### 2.2 "H5 (Morse stability)" as an embedded hypothesis

In `THEORY/canonical/canonical.md` and `THEORY/working/MF/pf_tstar_langevin.md`, the same condition is registered as **(H5) Morse stability** inside the T-P-F-ε0-K assumption package:

| File | Line | Content |
|------|------|---------|
| `canonical.md` | 1710 | `*(H5)* Morse stability: saddle ũ*_sad and minimum ũ*_min are non-degenerate critical points of E + εR stable for ε ∈ [0, ε_0] (no critical-point bifurcation);` |
| `canonical.md` | 1721 | `*Assumptions:* (H5) Morse stability holds generically (non-degenerate SCC saddles) but is not globally verified for E_SCC + εR.` |
| `canonical.md` | 1723 | `*Status:* **Cat B** — conditional on H5 (Morse stability). Cat A promotion path: (i) prove H5 for E_SCC saddles, (ii) establish spectral gap / Poincaré inequality on F_M(P).` |
| `pf_tstar_langevin.md` | 370 | The full registered H5 statement (saddle and minimum stable under perturbation εR). |
| `pf_tstar_langevin.md` | 401 | `4. **H5 (Morse stability):** Hypothesis H5 is assumed, not proved for E_SCC. For the specific Bernoulli perturbation R = -T_* S_Bern, H5 holds generically (by Morse theory, critical points are preserved under small perturbations) but has not been verified at the global level for the non-convex SCC energy.` |
| `pf_tstar_langevin.md` | 414 | T-P-F-ε0-K Cat B, depends on H5. |
| `pf_tstar_langevin.md` | 429 | "Prove H5 (Morse stability) for E_SCC + εR at the relevant saddles. (Required for Eyring-Kramers only)" |
| `pf_a1_lions_sznitman_freidlin_route.md` | 22, 389, 399, 408, 414, 430, 468, 481, 487, 495–496 | Multiple references to H5 as the gating Morse-stability hypothesis for Package II / Eyring-Kramers. |

### 2.3 Name collision warning

**Inside the T-OP6-B theorem (canonical.md §5.3b)**, `H5` is reused for a DIFFERENT hypothesis: "Hard-cut stereo adjacency (G_t^P from D-ST-1)". This is **not** the Morse stability hypothesis. The collision is local to T-OP6-B's H1–H5 package and does not affect the H-MORSE audit; the **Morse-stability H5** is exclusively the T-P-F-ε0-K hypothesis.

### 2.4 Classification

H-MORSE / H5-Morse is:
- a **hypothesis node** in the hypothesis tree (HT-3.5, Q3, Phase 2, OPEN, top priority);
- an **embedded assumption** in T-P-F-ε0-K (Cat B);
- **not** a registered theorem;
- **not** an OP entry (the closely related items are OP-0021 = T_* registration and the implicit "Morse stability" gap in T-P-F-ε0-K).

---

## 3. Package II references (full inventory)

### 3.1 canonical.md

| Line | Content |
|------|---------|
| 56 | `- P-F-A1 Package II (Eyring–Kramers): OPEN — conditional on H5 + OP-0021 (T_* registration).` |
| 498 (working file, but reflected in canonical) | `Package II (Eyring-Kramers) Cat B-conditional only on H5.` |
| 1611 | Non-overclaim block under T-P-F-ε0: "This theorem does NOT prove: spectral gap or mixing time, Eyring-Kramers pre-exponential factor, ... H5 Morse stability ..." |
| 1684 | Non-overclaim under T-PF-A1-PE: "Sharp Eyring-Kramers constants (Package II, conditional on H5) and canonical $T_*$ (OP-0021) not claimed." |
| 1719 | Non-overclaim under T-P-F-ε0-K: "It does NOT prove: ... Eyring-Kramers pre-exponential factor A (Hessian-at-saddle term), $T_*$ existence or uniqueness ..." |
| 1723 | "Cat A promotion path: (i) prove H5 for E_SCC saddles, (ii) establish spectral gap / Poincaré inequality on F_M(P)." |

### 3.2 hypothesis_tree.md

| Line | Content |
|------|---------|
| 88 | `Package II (Eyring-Kramers)` (critical path diagram) |
| 184 | `*Package II (OPEN): H-MORSE + H-T* 전제. 목표: Eyring-Kramers Γ_K, K→K-1 barrier crossing.*` |

### 3.3 working/MF/

`pf_a1_lions_sznitman_freidlin_route.md` has full Package II / Package I separation:

- Package I = AR + SDE + GI + PE (all Cat A; canonical CV-1.9).
- Package II = Freidlin-Wentzell quasipotential + Eyring-Kramers (OPEN; conditional on H5 + T_* registration).

Line 22: `II. Conditional metastability | Freidlin-Wentzell quasipotential + Eyring-Kramers | Conditional on H5 (Morse) + T_* registration`

Lines 389, 487, 495–496: explicit confirmation that Package II requires (a) H5 Morse stability, (b) Freidlin-Wentzell large-deviation, (c) T_* canonical registration.

### 3.4 Status summary

**Package II = OPEN. Three explicit gates:**
1. H-MORSE / H5 Morse stability (`H-MORSE` in hypothesis_tree, `H5` in canonical T-P-F-ε0-K)
2. T_* canonical registration (OP-0021)
3. Freidlin-Wentzell quasipotential + Eyring-Kramers prefactor

Closing all three is conjectured ~2–4 sessions in `pf_a1_lions_sznitman_freidlin_route.md §VIII`, but in practice each gate is a multi-session effort.

---

## 4. Related open problems

### 4.1 OP-0021 — T_* canonical registration

`hypothesis_tree.md` line 44: `**H-T*** | T_* 정규 등록 (OP-0021) | OPEN | Q3/Q4 수치화 | 최상 | Phase 2`

Two paths:
- **Path A (Mori-Zwanzig, NOP-F, Lemma 20):** memory kernel decay rate → effective temperature. Five gaps, sketch level.
- **Path B (RG fixed point, NOP-J, Lemma 24):** $T_*^\mathrm{Fisher} = T_*^\mathrm{RG}$ equivalence sketched.

Closing OP-0021 unlocks: T-K-Select-PF/OBS numerical predictions; Package II entry (combined with H-MORSE); D-ST-4 rate claims.

### 4.2 OP-0005 — K-Selection

Three-way split:
- **OP-0005-EQ:** PARTIALLY RESOLVED (T-K-Select-PF Cat B, CV-1.10).
- **OP-0005-OBS:** PARTIALLY RESOLVED (T-K-Select-OBS Cat B, CV-1.11).
- **OP-0005-DYN:** **OPEN.** Kramers rates / non-equilibrium K-distribution dynamics — needs Package II.

### 4.3 OP-0008 — σ-inheritance / K-jump non-determinism

Four sub-problems (CONT, MERGE, SPLIT, DIST):
- DIST: CLOSED Cat B (Lemma 16, 2026-05-07)
- CONT: PARTIALLY STRUCTURED
- MERGE: centroid + orientation Cat B; σ_standard Cat C (Wigner-projection W9+)
- SPLIT: direction Cat B; σ_standard Cat C

OPEN at Cat A. Cat A path requires Wigner-projection canonicalization (W9+ scope).

### 4.4 OP-0009 — Multi-Formation Ontological Foundations

7 sub-items. Mostly W11–W12 scope. Not blocking H-MORSE.

### 4.5 No registered "OP-MORSE" or "OP-H5"

The Morse-stability hypothesis is referenced as `H5` (T-P-F-ε0-K assumption) and `H-MORSE` (hypothesis tree node) but has **no canonical OP entry**. Recommend (working only, not canonical here): register **OP-MORSE** to formalize the status, with three sub-tasks corresponding to the Path A/B/C/D candidates in `02_H_MORSE_statement_reconstruction.md`.

---

## 5. Non-overclaim block

CV-1.13 closes **only** single-formation temporal identity.

CV-1.13 does **NOT** prove:
- multi-formation temporal identity (T-σ-Inherit OP-0008, OPEN)
- metastable transition rates (Package II, OPEN)
- Eyring-Kramers prefactor (Package II, OPEN)
- dynamic K-selection (OP-0005-DYN, OPEN)
- $T_*$ canonical registration (OP-0021, OPEN; T_* remains axiomatic)
- Morse nondegeneracy of any critical point of the full SCC energy (H-MORSE / H5, OPEN, this audit)
- spectral gap or mixing time of the reflected Langevin on $\Sigma_m$ (only Poincaré / ergodicity in T-PF-A1-PE, Cat A but with $C_P$ exponentially large)

The literal numerical claim "μ_min ∈ [0.96, 60.2] across configurations" in `hypothesis_tree.md` Q3 is **numerical evidence**, not a theorem. It supports the plausibility of a local Morse statement but is not a Cat A bound.

This audit does **not** change any canonical claim status. No canonical files are modified.
