# 02_NQ173_v5b_f_results.md — V5b-F Partial Goldstone Characterization (skeleton + a priori predictions)

**Session:** 2026-04-27 (W5 Day 1, G1 Block 4)
**Target (from plan.md §3 Block 4):** NQ-173 V5b-F partial Goldstone H1/H2/H3 characterization on free BC L=20, ζ ∈ {0.5, 0.7, 1.0} × N=5 seeds.
**This file covers:** §1 Question + §2 H1/H2/H3 hypotheses + §3 Setup + §4 a priori expectations + §5 result template (to be filled by user execution of `nq173_v5b_f_partial_goldstone.py`) + §6 verdict template.
**Depends on reading:** `04-26/04_NQ170c_graph_extension_nodal.md` §2.2 (V5b-F new finding origin); `pre_brainstorm.md` §2 (H1/H2/H3 a priori prediction H1+H2 mixed most likely); `CODE/scripts/nq173_v5b_f_partial_goldstone.py` (this session's script).
**Status:** Script written + syntax + import verified. Numerical run **deferred to user execution** (long-running ~10-15 min). Verdict skeleton awaits results.

---

## §1. Question

**Background:** W4-04-26 NQ-170c found that on 2D free BC L=20, F=1 minimizers exhibit *partial* mode-agnostic Goldstone overlap:
- ζ=0.5: max overlap 0.83 (V5b prediction: < 0.5 for sub-lattice OR > 0.9 for super-lattice — **fails both**)
- ζ=1.0: max overlap 0.75 (similarly fails both)

This is an **intermediate** regime not predicted by V5b. The phenomenon was registered as V5b-F (Cat C new finding, NQ-173 carry).

**NQ-173 question:** What is the *mechanism* of partial Goldstone on boundary-modified graphs?

---

## §2. Three Hypotheses

### H1: Bulk-localized Goldstone

**Statement:** Translation symmetry holds approximately in the *interior bulk* (far from boundary). The partial overlap arises because the eigenvector is a near-perfect translation Goldstone in the interior but is *modified near the boundary* by the broken translation invariance there.

**Test:** Bulk-only translation overlap (eigenvector and translation modes restricted to interior 4 ≤ x, y ≤ 16, then re-normalized) should approach > 0.95 if H1.

**Mechanism:** Free BC is *locally* translation-invariant in the bulk. The eigenvector "feels" only the local Hessian, which is bulk-Laplacian-like; translation Goldstone is the natural lowest mode. Boundary lifting only reduces *full-space* overlap by the boundary-region contribution.

### H2: Mode mixing (linear superposition)

**Statement:** The eigenvector is an *exact* linear combination
$$\hat\phi = \alpha\,\hat\psi_{\mathrm{translation}} + \beta\,\hat\psi_{\mathrm{boundary-localized}},$$
where $\hat\psi_{\mathrm{translation}}$ is the would-be Goldstone (interior translation) and $\hat\psi_{\mathrm{boundary-localized}}$ is a boundary edge mode that the SCC Hessian admits.

**Test:** Mode decomposition coefficients ($\alpha, \beta, \gamma$ onto $(\delta u_x, \delta u_y, \text{complement})$): expect $\alpha \approx 0.83$ matching W4-04-26 NQ-170c overlap measurement, $\beta$ small but nonzero, $\gamma$ accounting for boundary mode.

**Mechanism:** The Hessian's lowest non-tangent modes near boundary include both *translation pseudo-mode* (extended) and *edge modes* (localized at corners or edges). They are not orthogonal in general, and the actual eigenvector is a hybridization.

### H3: PN barrier modification (full-space Goldstone with finite eigenvalue)

**Statement:** The mode is *fully* Goldstone in character (covers entire support), but the boundary lifts the eigenvalue from "near zero" to "moderately small" (e.g., $\lambda \sim 0.1 - 1$). The Peierls–Nabarro barrier is enhanced by boundary effect.

**Test:** Spectral position — Goldstone candidate is *not* at lowest non-tangent mode (because boundary lifts λ); but its eigenvalue is still smaller than other "non-Goldstone" modes. Quantitative: Goldstone-candidate λ < other modes' λ but $\geq 10^{-2}$.

**Mechanism:** The boundary acts as an *external pinning potential* that lifts translation Goldstone from zero eigenvalue. Continuous translation symmetry is broken from "approximate" to "weakly explicitly broken".

---

## §3. Setup

- **Graph:** 2D free BC L=20 (n=400 sites)
- **Volume fraction:** c = 0.10 (40-site mass)
- **β values:** β = 1/ζ², so ζ ∈ {0.5, 0.7, 1.0} ↔ β ∈ {4.0, 2.04, 1.0}
- **Seeds:** N=5 per ζ; multi-IC strategy (3 IC widths each: ξ_0, ξ_0/2, ξ_0·2)
- **Total attempts:** 3 × 5 = 15 minimizer trials; F=1 selected
- **Hessian computation:** finite-difference (eps=1e-4), restricted to 1⊥, lowest 6 modes
- **Mode-agnostic detection:** iterate over all 6 modes; record max Goldstone overlap (no `mode_overlaps[1]` hardcode per W4-04-26 NQ-172 lesson)
- **Interior band for H1 test:** 4 (vs plan's narrower 8≤x,y≤12 = 5×5; using wider 4≤x,y≤16 = 12×12 = 144 sites = 36% per pre_brainstorm §2.4 recommendation)

**Script:** `CODE/scripts/nq173_v5b_f_partial_goldstone.py`. Output: `CODE/scripts/results/nq173_v5b_f.json`.

---

## §4. A Priori Expectations (from `pre_brainstorm.md` §2)

### Most likely: H1 + H2 mixed (~70% probability)

Per `pre_brainstorm.md` §2.3: "**H1 + H2 mixed가 most likely**". The reasoning:

- **Translation symmetry IS valid in interior** (no graph automorphism breaking) → H1 should be partially correct.
- **Boundary lifting IS exact** (free BC differs from torus precisely at boundary) → H2 should be partially correct.
- The two are *not exclusive*: an eigenvector localized partially in bulk + partially at boundary, with bulk-component dominantly translation-Goldstone-like, IS the natural picture.

**Predicted measurements if H1+H2 mixed:**
- Bulk-only overlap: 0.85 - 0.95 (high but not saturated; some interior boundary leakage)
- α coefficient: 0.75 - 0.90 (matches W4-04-26 NQ-170c overlap of 0.75 - 0.83)
- α² + β² ≈ 0.65 - 0.85 (translation-subspace dominant but not exclusive)

### Less likely: H1 alone (~15%)

If bulk-only overlap > 0.95 AND α² + β² > 0.95 → H1 alone supported. Would mean boundary effect is purely a "rescaling" of the eigenvector but not a structural mixing.

### Least likely: H3 (~10%)

H3 requires Goldstone-candidate eigenvalue to be $> 0.01$ but $<$ other modes' eigenvalues. From W4-04-26 NQ-170c: Goldstone candidate at ζ=0.5 was λ = 1.749 (mode 5, not the lowest mode 0). This is *consistent with H3* — but H3 alone wouldn't explain why bulk-overlap pattern differs from full-space. So H3 alone unlikely; H3 ⊕ H1 plausible.

### ~5% inconclusive

If all three indicators are mid-range without dominant pattern.

---

## §5. Results Template (to be filled after script execution)

### Per-(ζ, seed) table (15 rows)

| ζ | seed | F1 found | mode_idx | λ | max_ov_full | max_ov_bulk | bmf | α | β | γ | α²+β² |
|---|------|---------|---------|---|-------------|-------------|-----|---|---|---|-------|
| 0.5 | 0 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.5 | 1 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.5 | 2 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.5 | 3 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.5 | 4 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.7 | 0 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.7 | 1 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.7 | 2 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.7 | 3 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 0.7 | 4 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 1.0 | 0 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 1.0 | 1 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 1.0 | 2 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 1.0 | 3 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 1.0 | 4 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |

### Per-ζ aggregates

| ζ | F1 success rate | mean λ | mean max_ov_full | mean max_ov_bulk | mean bmf | mean α²+β² |
|---|----------------|--------|------------------|------------------|----------|-----------|
| 0.5 | ? / 5 | ? | ? | ? | ? | ? |
| 0.7 | ? / 5 | ? | ? | ? | ? | ? |
| 1.0 | ? / 5 | ? | ? | ? | ? | ? |

### Cross-ζ comparison (mechanism diagnostics)

| Indicator | ζ=0.5 | ζ=0.7 | ζ=1.0 | Trend with ζ ↑ | H1/H2/H3 verdict |
|-----------|-------|-------|-------|----------------|------------------|
| max_ov_full | ? | ? | ? | ? | full-space overlap behavior |
| max_ov_bulk | ? | ? | ? | ? | H1 (should ↑ → 0.95+ if H1) |
| bmf (bulk mass fraction) | ? | ? | ? | ? | H1 (should be high if mode bulk-localized) |
| α²+β² | ? | ? | ? | ? | H2 (should be < 1 by γ amount if H2) |
| best mode λ | ? | ? | ? | ? | H3 (small but > 0 if H3) |

---

## §6. Verdict Decision Tree (to be applied to filled §5)

```
Is mean(max_ov_bulk) > 0.95 across all ζ?
├ Yes → Is mean(α²+β²) > 0.95?
│       ├ Yes → H1 alone supported. V5b-F mechanism = "bulk-localized translation Goldstone, boundary rescales but doesn't mix"
│       └ No  → H1 + H2 mixed (bulk Goldstone + significant complement γ). V5b-F = bulk-Goldstone-with-mode-mixing.
└ No  → Is mean(α²+β²) > 0.85 with α ≈ measured max_ov_full?
        ├ Yes → H2 dominant (mode mixing at full-space level; bulk-overlap not improving because mixing is bulk-extensive too)
        └ No  → H3 candidate (full-Goldstone with PN barrier). Check best-mode λ < other modes' λ.
                ├ Yes → H3 supported.
                └ No  → Inconclusive (H1+H2 mixed but no dominant mechanism). V5b-F status: Cat C unchanged, refined statement.
```

---

## §7. Cat C → B Path (if H1 supported)

**If H1 supported (bulk-only overlap > 0.95):** V5b-F mechanism is **quantified** (not just qualitative). Status promotion candidate:

- V5b-F before NQ-173: **Cat C** (qualitative observation of intermediate overlap, no mechanism).
- V5b-F after NQ-173 H1 verdict: **Cat B target** (mechanism = bulk-localized translation Goldstone, lifted by boundary; quantitative bound on bulk overlap, qualitative on boundary lifting magnitude).

**Cat A would require** quantitative formula for boundary lifting amplitude as function of (ζ, L, geometry). Out of NQ-173 scope; NQ-173b (W6+ candidate).

**If H1 NOT supported:** V5b-F remains Cat C with refined statement (mechanism mixed bulk + boundary; refined description but no Cat B quantification).

---

## §8. Canonical Impact (deferred decision per plan.md §6 hard constraint)

**Per plan.md §6**: V5b-F canonical addition is *forbidden Day 1* — defer to W5 Day 2+ post-verdict decision.

If H1 verdict supports V5b-F → Cat B target: would propose addition of "boundary lifting reference" to existing T-V5b-T entry (canonical.md §13 line 1117), e.g.:

> *Distinct from non-translation-invariant graphs (V5b-F)*: Free BC, barbell, SBM exhibit *partial* Goldstone (overlap 0.5–0.85) due to boundary lifting; mechanism is **bulk-localized translation Goldstone with boundary modification** (NQ-173 H1, W5 Day 1 verdict). Cat B target.

This would be the only canonical change required. Defer to W5 Day 2+ user decision.

---

## §9. Carry-Forward to `03_v5b_f_status_update.md`

Once §5 results are filled:
- Verdict from §6 decision tree → V5b-F status update.
- Implications for canonical (§8) → user decision input.
- Spawn-NQ for unresolved questions:
  - NQ-173b (W6+): quantitative boundary lifting formula.
  - NQ-179 (W6+ candidate, from `pre_brainstorm.md` §3.2): V5b-F mechanism's relevance to multi-formation σ inter-formation gap (could be analogous "boundary").

---

**End of 02_NQ173_v5b_f_results.md (skeleton).**
**Awaits:** user execution of `cd CODE && python3 scripts/nq173_v5b_f_partial_goldstone.py`. Expected runtime ~10-15 min.
**Then:** fill §5 tables from `nq173_v5b_f.json` and apply §6 decision tree to write `03_v5b_f_status_update.md`.
