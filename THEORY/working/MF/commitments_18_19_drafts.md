# commitments_18_19_drafts.md — CV-1.7+ Commitment 18 & 19 Draft Texts

**Status:** working draft (W5 Day 4 PM Wave 3 lead-side direct work, 2026-04-30).
**Type:** CV-1.7+ canonical §11.1 amendment proposal drafts.
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §11.1 Commitments 1-17; OP-0005 K-Selection; OP-0008 σ^A K-jump non-determinism.
**Working refs:** `sigma_rich_augmentation.md` (Wave 3, σ_rich); `k_selection_mechanism.md` (in flight, OP-0005 candidates).

---

## §1. Mission

Wave 3 introduced two major theoretical extensions:
- **σ_rich augmentation** (sigma_rich_augmentation.md): Path B for OP-0008 K-jump deterministic inheritance.
- **K-Selection candidates (a/b/c)** (k_selection_mechanism.md): three candidate mechanisms for OP-0005.

Both are **CV-1.7+ scope** (not CV-1.6 release target). This file drafts canonical §11.1 amendment text for two new commitments to be considered after empirical anchoring.

---

## §2. Commitment 18 (σ_rich Augmentation) — CV-1.7 candidate

### §2.1 Draft text

```markdown
18. **σ_rich Augmentation for K-Jump Deterministic Inheritance (CV-1.7 candidate, W5 Day 4 PM Wave 3 proposed).**

The single-formation σ-tuple defined by Commitment 14 admits a *rich* augmentation:
$$\sigma_{\mathrm{rich}}(u) := \big(\sigma_{\mathrm{standard}}(u),\, \{\mathrm{centroid}_j(u)\},\, \{\mathrm{orientation}_j(u)\},\, \{\mathrm{Wigner\text{-}vN}_{jk}(u)\}\big)$$
where:
- $\mathrm{centroid}_j = \sum_x x \cdot u^j(x) / \sum_x u^j(x)$ (per-formation centroid).
- $\mathrm{orientation}_j = $ principal axis of inertia tensor $M_j = \sum_x u^j(x)(x-c_j)(x-c_j)^T$.
- $\mathrm{Wigner\text{-}vN}_{jk} = $ avoided-crossing 2x2 matrix in paired-Goldstone subspace.

All four components are derived diagnostics of $u_t$ (CN10 contrastive preserved); σ_rich does NOT introduce a new energy term (CN5 four-term independence preserved).

**Path B for OP-0008 σ^A K-jump non-determinism**: under K-jump events $K_{\mathrm{act}} \to K_{\mathrm{act}} - 1$ (mergers), the inheritance map $\Phi_{\mathrm{rich}}: \sigma_{\mathrm{rich}}(t^{*-}) \to \sigma_{\mathrm{rich}}(t^{*+})$ is **deterministic** (Cat A target via NQ-242c+d construction). The standard σ_A inheritance map (Path A) is non-deterministic; the σ_rich enrichment captures merger-geometry data sufficient for deterministic inheritance.

Adoption requires:
- Numerical anchor: σ_rich strictly refines σ_standard on R23 (NQ-264 Cat B target via `sigma_rich_refinement_theorem.md`).
- CODE implementation: `scc/sigma_rich.py` (W5 Day 4 PM Wave 3, ✅ implemented + tests pass).
- Canonical promotion of Φ_rich K-jump map (NQ-242c-Rich Cat A target).

References: 
- `working/MF/sigma_rich_augmentation.md` (Wave 3 W5 Day 4 PM, 533 lines).
- `working/SF/sigma_rich_refinement_theorem.md` (Wave 3 lead, Cat A target refinement claim).
- `CODE/scc/sigma_rich.py` (Wave 3 implementation).
- `THEORY/canonical/theorem_status.md` OP-0008 (HIGH severity).
```

**Effort:** ~50 canonical lines.

**CV target:** CV-1.7 (post-CV-1.6 release; depends on NQ-242c+d Cat A completion).

---

## §3. Commitment 19 (K-Selection Axiom) — CV-1.7+ candidate

### §3.1 Draft text

```markdown
19. **K-Selection Axiom — Path-Conditional Mechanism for $K_{\mathrm{act}}$ Determination (CV-1.7+ candidate, W5 Day 4 PM Wave 3 proposed).**

OP-0005 K-Selection is HIGH-severity OPEN: Commitment 16 distinguishes $K_{\mathrm{field}}$ (architectural) from $K_{\mathrm{act}}$ (dynamic-emergent), but the **mechanism selecting $K_{\mathrm{act}}$ in degenerate energy strata** is not yet canonically registered.

Three candidate mechanisms (per `working/MF/k_selection_mechanism.md` Wave 3):
(a) **Free energy variational principle**: $K_{\mathrm{act}} = \arg\min_K F(K; \beta, T, m)$ where $F = E + T \cdot (-S_{\mathrm{config}})$ at finite T (P-F flagged).
(b) **Kramers metastability**: $K_{\mathrm{act}}$ determined by initial conditions + barrier-crossing rates per Kramers (1940). Connection to N-1 Soft-Hard Switching Asymmetry per `working/MF/n1_kramers_extension.md`.
(c) **Symmetry-broken selection**: $K_{\mathrm{act}} = \arg\min_K |\mathrm{Aut}(G)_{u_K^*}|$ (most "broken" stabilizer).

**Adoption requires empirical anchor (NQ-301/302/303 W6+ numerical):**
- Test each candidate on R23 90-run dataset; check if any matches observed $K_{\mathrm{act}}$ distribution.
- If a candidate matches at empirical level (e.g., χ² test), promote that candidate to Commitment 19 (single mechanism).
- If no candidate matches, document OP-0005 as fundamentally model-dependent (Quanta 2026-04 AC analog per `foundational_bridges_2026.md` Bridge B-7).

**Compatibility with Commitment 16:** all three candidates preserve $K_{\mathrm{field}}$/$K_{\mathrm{act}}$ decomposition; they only constrain $K_{\mathrm{act}}$ selection within $K_{\mathrm{field}}$ bound.

**Compatibility with CN15 Static/Dynamic Separation (CV-1.6 candidate):** all three candidates respect the static/dynamic separation; static $K=1$ on pure $\mathcal{E}_{\mathrm{bd}}$ vs dynamic $K_{\mathrm{act}}$ on full $\mathcal{E}$ remains distinct.

References:
- `working/MF/k_selection_mechanism.md` (Wave 3 W5 Day 4 PM, in flight via op-0005-architect).
- `working/MF/n1_kramers_extension.md` (Wave 3 lead, N-1 ↔ K-Selection (b) connection).
- `working/MF/cn15_static_dynamic_separation.md` (Wave 3 lead, CV-1.6 candidate).
- `working/MF/foundational_bridges_2026.md` Bridge B-7 (AC philosophical analog).
- `THEORY/canonical/theorem_status.md` OP-0005 (HIGH severity).
```

**Effort:** ~70 canonical lines.

**CV target:** CV-1.7+ (depends on NQ-301/302/303 numerical anchoring; W6+ priority).

---

## §4. Adoption flow

### §4.1 CV-1.7 (Commitment 18 path)

Pre-conditions:
1. NQ-242c-Standard non-determinism confirm (numerical, ~2-3 weeks W6+).
2. NQ-242c-Rich determinism confirm (numerical, ~2-3 weeks W6+).
3. NQ-264 σ-fingerprint refinement test on R23 (~6h compute, W6+).
4. Φ_rich K-jump inheritance Cat A proof (W7+).

If all 4 satisfied → Commitment 18 promoted at CV-1.7 (~W7+ release).

### §4.2 CV-1.7+ (Commitment 19 path)

Pre-conditions:
1. NQ-301 free energy K-Selection numerical (R23 + finite T scan; W6+).
2. NQ-302 symmetry-broken K-Selection R23 numerical (W6+).
3. NQ-303 Bayesian K-detection (W7+).
4. Empirical match assessment for one of (a/b/c).

If a candidate matches empirically → Commitment 19 with that candidate at CV-1.7+ (~W8+ release).

If no candidate matches → document as model-dependent (no Commitment 19, just open problem).

---

## §5. Hard constraint verification

- [x] **u_t primitive maintained**: σ_rich and K-Selection candidates all derived diagnostics on $u_t$ field.
- [x] **CN10 contrastive throughout**: σ_rich Wigner-vN reference (Wigner-von Neumann 1929) is structural; Bridge B-7 AC analog explicitly contrastive.
- [x] **CN5 4-energy not merged**: σ_rich is derived diagnostic, not new energy term; K-Selection candidates (a/b/c) operate on full $\mathcal{E}$ (4 terms preserved).
- [x] **OP not silently resolved**: OP-0008 (Path B candidate, NOT adoption) and OP-0005 (3 candidates, NOT adoption) both preserved at OPEN status.
- [x] **No metastability claim without P-F flag**: Commitment 19 (b) Kramers metastability explicitly P-F flagged.

---

## §6. Net CV roadmap

| CV | Target W | Commitments |
|---|---|---|
| CV-1.5.1 | W5 D3 (DONE) | C-14 + C-14-Multi + C-16 |
| CV-1.6 | W6 D7 EOD | + C-17 (4-tool); + CN15; + N-1 Kramers sub-statement |
| CV-1.7 | W7+ (~W7-W9) | + C-18 (σ_rich) — depends on NQ-242c+d Cat A |
| CV-1.7+ | W8+ (~W8-W11) | + C-19 (K-Selection axiom) — depends on NQ-301/302/303 + empirical match |
| v2.0 | W11-W12 | full OP-0009 resolution + Paper 4 NEW |

---

**End of commitments_18_19_drafts.md.**

**Status:** CV-1.7+ Commitment 18 (σ_rich) + Commitment 19 (K-Selection axiom) draft texts. ~50 + ~70 canonical lines respectively. Both depend on numerical anchoring (NQ-242c+d for C-18; NQ-301/302/303 for C-19). Working-only at CV-1.6 release; promoted post-CV-1.6 release.
