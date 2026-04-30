# sigma_fingerprint_qrcode.md — σ-Fingerprint Algorithm Specification (Bridge B-4 NQ-264)

**Status:** working draft (W5 Day 4 PM Wave 3 lead-side direct work, 2026-04-30).
**Type:** Bridge B-4 working file — strong + computable σ-fingerprint specification.
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §11.1 Commitment 14 σ-framework; §13 T-σ-Theorem-3 closed form; NQ-188 σ-class enumeration.
**Working refs:** `foundational_bridges_2026.md` §5 Bridge B-4; `sigma_uniqueness_theorem.md` (NQ-188); `sigma_lie_algebra_structure.md` (Aut(G)_{u*}); `sigma_class_count_R23.json` (56 R23 minimizers).
**External:** Bar-Natan, D., van der Veen, R. (2026). Knot-invariant QR-code fingerprints (citation pending).

---

## §1. Mission

Goal: design a **strong + computable σ-fingerprint** distinguishing 56 R23 minimizers (NQ-188) without full Hessian diagonalization.

**Motivation:** Full Hessian diagonalization is O(n³) per minimizer × 56 minimizers (R23). On L=32, n=1024, this is computationally heavy for systematic σ-class enumeration. Bar-Natan-van der Veen (2026) QR-code knot invariants achieve **strong + polynomial-time** fingerprinting in knot theory; SCC needs an analog.

**Cat target:** B (empirical strength on R23; conditional on broader graph-class verification).

---

## §2. σ-Fingerprint Definition

### §2.1 Fingerprint structure

For a single-formation minimizer $u^* \in \Sigma_m$ on graph $G$:
$$\boxed{\text{Fingerprint}(u^*) := (\mathcal{F}, K_{\mathrm{step}}, \text{Bind-vec}, \text{Sep-vec}, \text{Inside-vec}, \text{nodal-multi}, \text{Aut-irrep-multi}, \text{centroid-orbit-rep})}$$

where:
- $\mathcal{F}(u^*) = $ peak count (threshold-free).
- $K_{\mathrm{step}}(u^*; \tau_{0.5}) = $ connected-component count at threshold 0.5.
- **Bind-vec**: $((\text{Bind}_{\tau_1}, \tau_1), (\text{Bind}_{\tau_2}, \tau_2), \ldots)$ — Bind diagnostic at multiple thresholds.
- **Sep-vec**: similarly multi-threshold Sep.
- **Inside-vec**: similarly multi-threshold Inside.
- **nodal-multi**: multiset of nodal-domain counts at peaks.
- **Aut-irrep-multi**: multiset $\{(\dim, [\rho_k])\}$ of Aut(G)_{u*}-irrep labels (no eigenvalues).
- **centroid-orbit-rep**: canonical representative of centroid orbit under Aut(G)-action.

### §2.2 Computational complexity per component

| Component | Algorithm | Complexity |
|---|---|---|
| $\mathcal{F}$ | scan local maxima | O(n·deg) |
| $K_{\mathrm{step}}$ | union-find on superlevel set | O(n·α(n)) |
| Bind/Sep/Inside vectors | sum/integrate over u | O(n) per τ × O(log n) τ values = O(n log n) |
| Nodal-multi | basin segmentation + count | O(n·log n) |
| Aut-irrep-multi | Aut(G)_{u*} computation + character projection | O(\|Aut(G)\|·n) |
| Centroid-orbit-rep | compute centroid + orbit via Aut(G) | O(n + \|Aut(G)\|) |

**Total complexity:** O(n log n + \|Aut(G)\|·n) per minimizer.

For R23 D_4 free-BC L=32: |Aut(G)| = 8, n = 1024 → fingerprint computation ~10000 operations per minimizer × 56 minimizers ~ 6×10⁵ operations total.

**Compare to full Hessian:** O(n³) = O(10⁹) per minimizer × 56 = 6×10¹⁰ operations.

**Speedup factor:** ~10⁵×.

---

## §3. Strength Claim (Cat B target)

### §3.1 Empirical claim
**Conjecture (Cat B target, NQ-264):** *The σ-fingerprint distinguishes all 56 R23 stable Morse-0 minimizers; i.e., no two distinct R23 minimizers have identical σ-fingerprints.*

### §3.2 Theoretical claim (Cat C target)
**Conjecture (Cat C):** *On any finite connected graph $G$ satisfying (G1)-(G4), the σ-fingerprint distinguishes all NQ-188 σ-classes (i.e., σ-fingerprint refines or equals σ-class equivalence).*

### §3.3 Strict refinement?
The σ-fingerprint includes **Aut-irrep-multi** (multiset of irrep labels, no eigenvalues), whereas σ-standard (NQ-188) is a tuple including **eigenvalues** $\lambda_k$. The σ-fingerprint is therefore **coarser than σ-standard** (drops eigenvalue numerical data). 

**Question:** does the σ-fingerprint distinguish σ-classes equivalently to σ-standard?

If yes (§3.1 confirmed), the σ-fingerprint is an **eigenvalue-free σ-class invariant** — significant computational simplification.

If no (some σ-classes collapse), the σ-fingerprint is strictly coarser — useful for fast pre-filtering, but full σ-class enumeration still requires σ-standard.

---

## §4. Numerical Verification Protocol

CODE/scripts/sigma_fingerprint_R23.py (proposed Task #26):

```python
"""σ-Fingerprint enumeration on R23 56 stable minimizers (NQ-264 Cat B target).

Setup:
- Load R23 fullscale dataset (56 stable Morse-0 minimizers).
- For each u^*: compute σ-fingerprint per §2 spec.
- Tally:
  - n_distinct_fingerprints: count of distinct fingerprints.
  - collisions: minimizer pairs with identical fingerprints.
- Verify: n_distinct_fingerprints == 56 (strict refinement of σ-class).

Output: CODE/scripts/results/sigma_fingerprint_R23.json with:
  - n_minimizers
  - n_distinct_fingerprints
  - fingerprint_table (per-minimizer)
  - collision_pairs (if any)
  - timing per fingerprint component

Effort: ~6h compute on R23 + small fingerprint algorithm implementation.
"""
```

**Cat B criterion (§3.1):** if n_distinct_fingerprints = 56 (no collisions), σ-fingerprint distinguishes all R23 minimizers — Cat B target achieved.

**Falsification criterion:** if n_distinct_fingerprints < 56 (collisions exist), σ-fingerprint is strictly coarser than σ-class. Document collision configurations as candidate σ-class refinement targets.

---

## §5. Connection to σ_rich (Wave 3 OP-0008 Path B)

σ_rich (sigma_rich_augmentation.md §2) extends σ-standard with centroid + orientation + Wigner data. The σ-fingerprint defined here uses centroid-orbit-rep (a coarse centroid invariant) + Aut-irrep-multi (no eigenvalues).

**Hierarchy of σ-invariants** (from coarsest to finest):
1. σ-fingerprint (this file): eigenvalue-free, Aut-irrep multiset, centroid orbit.
2. σ-standard (NQ-188): includes eigenvalues, full irrep tuple.
3. σ_rich (Wave 3 OP-0008 Path B): σ-standard + centroid + orientation + Wigner.

**Refinement chain (conjectural):** σ-fingerprint ⊇ σ-standard ⊇ σ_rich (each finer than the previous).

**Verification path:**
- §4 verifies σ-fingerprint = σ-standard (if Cat B target succeeds).
- `sigma_rich_refinement_theorem.md` (Wave 3 lead direct work) verifies σ_rich ⊊ σ-standard (strict refinement).

If both hold: σ-fingerprint = σ-standard ⊋ σ_rich.

---

## §6. Connection to NQ-187 Critical Finding

NQ-187 numerical (Wave 3, p≈1) shows leading-order non-degeneracy $\mu_0 \neq \mu_1$ on D_4 free-BC L≤16. This means σ-standard's eigenvalue tuple component is NON-trivial (eigenvalues are distinct, not degenerate).

**Implication for σ-fingerprint:** the **Aut-irrep-multi** component (without eigenvalues) might not distinguish post-pitchfork minimizers that differ only in eigenvalue ratios. 

**Conjecture (refined):** σ-fingerprint distinguishes σ-classes only when irrep multiplicities differ; for σ-classes with identical irrep multi-set but distinct eigenvalue tuples, σ-fingerprint collapses them (collision).

This is **expected** for the eigenvalue-free fingerprint; the trade-off is computational simplification at the cost of fine-grained eigenvalue distinction.

---

## §7. Cat target

- §2 fingerprint spec: Cat A (definitional, immediate).
- §3.1 empirical strength on R23: Cat B target (NQ-264, W6+ via numerical verification).
- §3.2 theoretical refinement claim: Cat C target (general graphs, W7+).
- §5 hierarchy chain: Cat C target (depends on σ_rich_refinement_theorem.md + this file's empirical results).

**Net Cat target for the file:** B (with §2 Cat A definitional spine + §3.2/§5 Cat C extensions).

---

## §8. CV-1.7+ promotion path

Not for CV-1.6 (release W6 Day 7 EOD; this file is W7+ scope).

For CV-1.7:
- §2 fingerprint spec: ~30 canonical lines as σ-framework supporting structure (single Cat A entry).
- §3-§5 remain working/SF.

**Effort:** ~30 canonical lines for §2 only.

---

## §9. Hard constraint verification

- [x] **u_t primitive maintained**: σ-fingerprint operates on cohesion field minimizer; primitive unchanged.
- [x] **CN10 contrastive throughout**: Bar-Natan-van der Veen (2026) knot QR-code is structural inspiration only; SCC is not knot theory. §1 explicit.
- [x] **CN5 4-energy not merged**: σ-fingerprint computed on full $\mathcal{E}$ minimizers (4 terms preserved).
- [x] **OP not silently resolved**: NQ-188 σ-class enumeration not resolved by this file; σ-fingerprint provides a fast pre-filter.

---

## §10. Cross-references

### §10.1 Working files
- `working/SF/sigma_uniqueness_theorem.md` (NQ-188 σ-class definition).
- `working/SF/sigma_lie_algebra_structure.md` (Aut(G)_{u*} stabilizer + irrep characters).
- `working/SF/sigma_rich_refinement_theorem.md` (Wave 3, refinement chain comparison).
- `working/MF/foundational_bridges_2026.md` §5 Bridge B-4.
- `working/MF/sigma_rich_augmentation.md` (Wave 3 OP-0008 Path B σ_rich).

### §10.2 External references
- Bar-Natan, D., van der Veen, R. (2026). *"Knot invariants from QR-code-like fingerprints."* arXiv pending. ⚠️ citation to verify.

### §10.3 Numerical infrastructure
- `CODE/scripts/sigma_class_count_R23.py` (Wave 2, 56 R23 minimizers count).
- `CODE/scripts/sigma_class_count_R23.json` (data).
- `CODE/scripts/sigma_fingerprint_R23.py` (Task #26, this file's numerical companion).

---

**End of sigma_fingerprint_qrcode.md.**

**Status:** working draft, Cat B target via NQ-264. σ-fingerprint algorithm specified (8 components, O(n log n + |Aut(G)|·n) complexity per minimizer). 10⁵× speedup vs full Hessian. Empirical strength claim on R23 (Cat B target). Theoretical refinement chain conjecture (Cat C). CV-1.7+ promotion candidate (§2 spec only).
