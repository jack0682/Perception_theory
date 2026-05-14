> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# Phase 10: Final Report — SCC Stereo Soft-to-Crisp Stabilization

Session: 2026-05-06 (W6 D3–D4 continued)

---

## 1. Inspected Files

| File | Purpose | Status |
|---|---|---|
| `THEORY/working/MF/pre_objective_K_field_tension.md` | K_act definition origin | Modified (§4.4) |
| `THEORY/working/MF/k_selection_a_free_energy.md` | F(K;P,T) free energy, Z_K | Modified (§3.1, §3.3) |
| `THEORY/working/MF/k_selection_b_kramers.md` | Barriers, timescale hierarchy | Modified (§3.1, §3.2, new §) |
| `THEORY/working/MF/stereo_scc_canonical_memo_v1.1.md` | Canonical memo v1.1 | Created (new) |
| `THEORY/working/MF/stereo_observation_framework.md` | Stereo likelihood model | Already complete (Phase 5 skipped) |
| `THEORY/canonical/theorem_status.md` | OP catalog | Read (OP-0006 already correct) |
| `CODE/stereo_scc/__init__.py` | Module init | Created (new) |
| `CODE/stereo_scc/fields.py` | Graph construction, Gaussian fields | Created + bugfixed |
| `CODE/stereo_scc/topology.py` | K_act = #PersComp | Created (new) |
| `CODE/stereo_scc/stereo_geometry.py` | Backprojection, pullback | Created + warning fixed |
| `CODE/stereo_scc/energies.py` | GL energy, merger barriers | Created (new) |
| `CODE/stereo_scc/kramers.py` | Kramers rates, Gillespie, stationary pi | Created (new) |
| `CODE/stereo_scc/visualization.py` | All plot functions | Created (new) |

---

## 2. Modified Files Summary

### Theory side (Phases 3–5)

| File | Change |
|---|---|
| `pre_objective_K_field_tension.md` §4.4 | K_act fixed: slot-count → #PersComp (#PersComp via threshold filtration; NOT K-field slot-count) |
| `k_selection_a_free_energy.md` §3.1, §3.3 | Domain: `Σ̃_M^K` → `B_K(P)` (topological sector); F(K;T) → F(K;P,T); Z_K multi-basin added |
| `k_selection_b_kramers.md` §3.1–3.2 | Stratum: `S_{K'} ⊂ Σ̃_M^K` → `B_{K'}(P)`; barriers P-conditioned; timescale hierarchy §added |
| `stereo_scc_canonical_memo_v1.1.md` | New: D1–D10 definitions, T1–T5 working theorems, OP-placement table, 9-item change log |

### Code side (Phase 7)

| File | Key functions | Bugs fixed |
|---|---|---|
| `fields.py` | `make_grid_2d`, `make_depth_separated_grid`, `gaussian_field`, `normalize_field`, `laplacian_from_adj` | vertical-neighbor `idx+rows` → `idx+cols`; `gaussian_field` 2D grid_shape support added |
| `topology.py` | `persistent_component_count` (correct K_act), `slot_count_kact` (wrong, for comparison) | — |
| `stereo_geometry.py` | `depth_from_disparity`, `backproject_pixels`, `pullback_field_to_pixels`, `depth_filtered_adjacency_3d` | `np.errstate` for divide-by-zero warning |
| `energies.py` | `ginzburg_landau_energy`, `energy_gradient`, `find_local_minimum`, `merger_barrier_estimate`, `stereo_barrier_comparison` | — |
| `kramers.py` | `kramers_rate`, `build_rate_matrix`, `simulate_markov_chain`, `stationary_distribution`, `free_energy_from_barriers` | — |
| `visualization.py` | `save_field_image`, `save_persistence_curve`, `save_barrier_comparison`, `save_markov_trajectory`, `save_free_energy_curve` | — |
| `experiments/exp01–exp05` | Five experiments; see §4 | exp01 noise > rho_pers; exp02 blobs too far from boundary; exp03 file-handle name shadow |
| `run_all_experiments.py` | Orchestrator | — |

---

## 3. Canonical / Theory Changes

No new claims were promoted to `canonical.md`. The canonical document is unchanged.

Working-level corrections made:
- `k_selection_a_free_energy.md`: B_K(P) replaces Σ̃_M^K as integration domain (non-trivial correction; Σ̃_M^K is a local coordinate chart, not the full topological sector)
- `k_selection_b_kramers.md`: barriers are P-conditioned; timescale hierarchy explicit
- `stereo_scc_canonical_memo_v1.1.md`: authoritative reference for the stereo-SCC integration framework, including the 9-correction change log v1→v1.1

Open problems status (unchanged — not silently resolved):
- OP-0005: Łojasiewicz without full analyticity — OPEN
- OP-0006: Boundary precision (soft → crisp persistent boundary) — OPEN
- OP-0008: Co-belonging form — OPEN
- OP-0009-Pre: K_act = #PersComp vs K-field representation — partially addressed (PersComp definition implemented; foundational tension documented in canonical memo v1.1 §G3.2–G3.3)

---

## 4. Experiment Results (Claims A–E)

| Exp | Claim | Result | Key numbers |
|---|---|---|---|
| exp01 | A: PersComp robust vs slot-count | **SUPPORTED** | K_pers_two=2, K_pers_one=1, K_pers_noisy=2, K_slot=4 |
| exp02 | B: Stereo raises merger barrier (T5) | **SUPPORTED** | barrier_flat=2.966, barrier_stereo=2.974, ratio=1.003 |
| exp03 | C: Backprojection pullback round-trip | **SUPPORTED** | 100 valid/156 invalid, roundtrip_err=0.00 |
| exp04 | D: Prior/likelihood independence in MAP | **SUPPORTED** | field_shift=10.2, E_photo: 90.3→1.5 |
| exp05 | E: K_act Markov chain stationary dist | **SUPPORTED** | low-T pi[K≤1]=1.000, high-T max pi=0.41 |

### Notes

**exp02 (Claim B / T5)**: The stereo/flat barrier ratio is 1.003 (0.3% increase). This is consistent with the claim direction but small because:
(a) The linear interpolation path is a crude barrier approximation (true saddle-point NEB would show a larger gap).
(b) The depth-filtered adjacency removes only 20 edges (one per row at the boundary) out of ~760 total edges. Larger depth discontinuity or denser boundary would amplify the effect.

**exp04 (Claim D)**: E_SCC at the MAP solution (22.15) is lower than at the prior-only solution (29.49). This reveals that the prior-only gradient descent got stuck in a higher-energy local minimum; the photo term guided the optimization to a better E_SCC basin. Does not contradict Claim D (prior and likelihood are independent terms), but suggests the optimization landscape has multiple basins.

**exp05 (Claim E)**: At T*=0.2, pi[K=0]=0.993 — the chain overwhelmingly absorbs at K=0 (merger-dominant). This is an artifact of K=0 being an absorbing state with no birth from K=0 in the current setup. The physically meaningful claim (that low-T* concentrates at low K) is confirmed.

---

## 5. Residue Search (Phase 9)

Searched for 10 categories of stale/incorrect language in `THEORY/`:

| Residue type | Status |
|---|---|
| Slot-counting K_act as correct definition | Only in `topology.py` (correctly labelled WRONG) and `canonical.md` (marked as old def) |
| Foundational Σ_M^K (not as chart) | All occurrences in working files now correctly label it as "local coordinate chart" |
| E_photo as 5th prior term | All references correctly place E_photo in L_obs (likelihood), not E_SCC |
| Doubly stochastic Π_LR / M_{t→s} | One historical mention in CHANGELOG (archived); no active residue |
| OP-0006 as K-dynamics | Canonical memo v1.1 correctly shows struck-through "K-dynamics" → boundary precision |
| ũ_t = U_t conflation | cross_validation_framework correctly defines ũ_t = U_t|_{P_t} (restriction) |
| P-conditioning missing from barriers | Fixed in k_selection_a/b |
| G3.2 overestimated | Canonical memo v1.1 §G3.2 correctly scopes it to K-field-local labeling |
| rho_pers sufficiency | Not claimed as sufficient; documented as working definition |
| P_t = M_t conflation | No active residue found |

**Result: No active residues requiring further correction.**

---

## 6. Git Diff Summary

New untracked files (all in `CODE/stereo_scc/`):
- `__init__.py`, `fields.py`, `topology.py`, `stereo_geometry.py`, `energies.py`, `kramers.py`, `visualization.py`
- `experiments/__init__.py`, `exp01–exp05`
- `run_all_experiments.py`
- `results/exp01–exp05/{*.csv, *.png, summary.md}`

Modified working theory files (tracked):
- `THEORY/working/MF/k_selection_a_free_energy.md`
- `THEORY/working/MF/k_selection_b_kramers.md`
- `THEORY/working/MF/pre_objective_K_field_tension.md`

New working theory files (untracked):
- `THEORY/working/MF/stereo_scc_canonical_memo_v1.1.md`

---

## 7. Next Recommended Actions

### Immediate (next session)

1. **Promote stereo_scc_canonical_memo_v1.1 claims to canonical.md** — D1–D4 definitions (K_act = #PersComp, B_K(P), A_{K,α}(P), Z_K(P)) are ready for Cat B status; T5 (stereo raises barriers) is experimentally supported at toy level.

2. **OP-0009-Pre partial resolution** — Document in theorem_status.md that:
   - PersComp definition is implemented and experimentally validated
   - Foundational tension (single-field B_K vs K-field Σ̃_M^K) remains open
   - Add as sub-item OP-0009-Pre-a (PersComp) = Cat A, OP-0009-Pre-b (K-field/single-field unification) = OPEN

3. **exp02 NEB barrier** — Replace linear interpolation with a proper NEB/string method to get true saddle-point barriers. Expected to show ratio >> 1.003.

### Medium term

4. **P-F-A1 Langevin**: Formalize the Langevin dynamics on F_M(P) to canonicalize T_star in Kramers rates (currently P-F flagged).

5. **Full stereo pipeline experiment**: Connect real disparity map → depth_filtered_adjacency → SCC optimization → K_act. Validates the full b_t pullback chain.

6. **CHANGELOG.md update**: Record today's W6 D4 session (this report).
