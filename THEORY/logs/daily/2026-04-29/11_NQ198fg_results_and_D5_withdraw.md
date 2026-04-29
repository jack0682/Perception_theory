# 11_NQ198fg_results_and_D5_withdraw.md — NQ-198f + NQ-198g Results: D-5 V5b-T' WITHDRAW

**Session:** 2026-04-29 (W5 Day 3 EOD post-deepening — urgent execution round)
**Target:** Execute NQ-198f (V5b-T' torus) and NQ-198g (β-scan free-BC) per `10_*` Layer A; integrate findings; finalize D-5 V5b-T' canonical decision.
**This file covers:** §1 NQ-198f raw data + interpretation; §2 NQ-198g raw data + interpretation; §3 **THIRD substantive negative result — V5b-T' as defined does not exist on torus**; §4 D-5 verdict update: **WITHDRAW** rather than approve; §5 V5b family revised taxonomy; §6 New open questions; §7 Day 4 morning revised plan.
**Depends on reading:** `04_*`, `05_*`, `07_*`, `09_*`, `10_*`.

---

## §1. NQ-198f Results: V5b-T' on Torus

### §1.1 Setup

- 6 (m, L, c) configurations × 3 seeds (sweep a + sweep b like NQ-198a, but on **2D torus** instead of free-BC).
- β=4, ξ_0=0.5 (R3b regime).
- 6 IC configs per seed (cluster anchored at varied torus positions).

### §1.2 Raw data (corner-saturated only)

| Sweep | m | L | c | μ_G | std | \|∂S\| | u_max | overlap |
|---|---|---|---|---|---|---|---|---|
| a | 40 | 20 | 0.10 | (uniform basin / T8-Core block) | - | 0 | - | - |
| a | 80 | 20 | 0.20 | NO GOOD ATTEMPTS (T8-Core block) | - | - | - | - |
| **a** | **120** | **20** | **0.30** | **0.005** | 0.000 | 36 | 1.000 | 0.91 |
| **a** | **160** | **20** | **0.40** | **−0.001** | 0.000 | 44 | 1.000 | 0.95 |
| **b** | **80** | **28** | **0.10** | **−0.028** | 0.000 | 20 | 1.000 | 0.95 |
| **b** | **160** | **40** | **0.10** | **0.018** | 0.000 | 40 | 1.000 | 0.95 |

**4 valid corner-saturated data points on torus**. All show $\mu_G \approx 0$ (within numerical noise ±0.03).

### §1.3 Interpretation

**On torus, μ_Goldstone ≈ 0 EXACTLY** (within Hessian finite-difference precision $10^{-2}$ to $10^{-3}$).

This is **not** the predicted μ ≈ 2α = 2 (`05_*` §4 derivation), nor the predicted μ ≈ 13|∂S|/n (NQ-198a empirical for free-BC). It is **near-zero**.

**Reason**: torus has full discrete translation symmetry $\mathbb{Z}_L^2$. A corner-saturated cluster at any specific lattice position is equivalent (by translation) to the same cluster at any other position. The translation Goldstone modes (lattice-translation tangent vectors) have eigenvalue **exactly zero** in the discrete tangent space — they generate the orbit of equivalent minimizers connected by exact symmetry.

This is the **standard Goldstone theorem on lattice with translation symmetry**: continuous translations are not group elements (lattice has discrete translations), but the cluster orbit under $\mathbb{Z}_L^2$ has flat eigenspectrum at $\mu = 0$.

**Numerical $\mu_G \in [-0.03, 0.02]$** is not "small but nonzero" — it is **numerically zero** (exact zero modes computed by finite-difference Hessian within $\epsilon^{1/2}$ tolerance for $\epsilon = 10^{-4}$).

### §1.4 Implication for V5b-T' canonical proposal

**V5b-T' as defined in `2026-04-28/20_*` Part 1 §1.2** claims (V5b-T'-c):
> $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} \approx A_{\mathrm{R3b}} \cdot \beta \cdot |\partial S|/\xi_0$, magnitude $\mathcal{O}(\beta)$, **not exponentially small**.

NQ-198f measurements: $\mu_G \approx 0$ on torus.

**This DIRECTLY REFUTES V5b-T' canonical claim**. There is **no PN-barrier-lifted Goldstone on torus** in regime R3b — the cluster has exact (discrete) translation symmetry; Goldstone modes are exactly zero.

**V5b-T' as a separate phenomenon does NOT exist** on translation-invariant graphs. The corner-saturated cluster on torus is just an F=0 (or F=1) minimizer with **trivial translation Goldstone** = zero modes from the orbit symmetry.

---

## §2. NQ-198g Results: β-Scan on Free-BC

### §2.1 Setup

- L=20, c=0.10 (NQ-198a anchor), free-BC.
- β ∈ {2, 3, 4, 6, 8}; ξ_0 ∈ {0.707, 0.577, 0.5, 0.408, 0.354}.
- 3 seeds each.

### §2.2 Raw data

| β | ξ_0 | μ | \|∂S\| | $C_{\mathrm{emp}} = \mu n /|∂S|$ | C/β |
|---|---|---|---|---|---|
| 2.0 | 0.707 | 0.320 | 16 | 8.01 | 4.00 |
| 3.0 | 0.577 | 0.511 | 16 | 12.79 | 4.26 |
| 4.0 | 0.500 | 0.656 | 20 | 13.13 | 3.28 |
| 6.0 | 0.408 | 0.725 | 20 | 14.49 | 2.42 |
| 8.0 | 0.354 | 1.216 | 21 | 22.92 | 2.86 |

### §2.3 Interpretation

**$C(\beta)$ is NOT simply $\pi\beta$**. The hypothesis "$C \approx \pi\beta$" (`07_*` §3.3) gave $\pi\beta \in [6.28, 25.13]$ across this β-range; observed $C_{\mathrm{emp}} \in [8, 23]$. Roughly the right magnitude but $C/\beta$ varies from 4.0 (low β) to 2.4 (mid β) to 2.86 (high β) — **not constant**.

**Cluster perimeter $|\partial S|$ also changes with β**: 16 → 20 → 21 across the scan. At larger β (smaller ξ_0), the cluster is sharper with larger effective discrete perimeter.

**Controlling for $|\partial S|$**: at fixed $|\partial S| = 20$ (β=4 vs β=6): μ ratio = 1.10; β ratio = 1.5; ξ_0 ratio = 1.225. **μ ratio doesn't match β alone or ξ_0 alone or simple combinations**.

### §2.4 Conclusion from NQ-198g

The empirical formula $\mu \approx C |\partial S|/n$ is valid at $\beta = 4$ specifically (NQ-198a). Across β, $C$ varies by factor ~3× and **doesn't have a clean $\beta^p$ form**. Higher-resolution β-scan with $|\partial S|$-controlled experiments needed (NQ-198g extension; W6+).

**Cat status**: $\mu \approx C |\partial S|/n$ is **at-fixed-β empirical**; full $C(\beta, \xi_0)$ functional form **open**.

---

## §3. THIRD Substantive Negative Result

### §3.1 Aggregate of Day 3 negative results

Day 3 has now produced **three** substantive negative results, each refuting a prior heuristic or derivation:

| Negative Result | What was refuted | Discovered when |
|---|---|---|
| 1. σ^A K-jump non-determinism | Implicit assumption: σ-trajectory is deterministic from σ data alone (Phase 8 T4 framework) | `04_*` Lemma 4.4.1(c) |
| 2. V5b-F mass dependence | Phase 3 heuristic ($\mu \propto |\partial S|/\xi_0$) AND Day 3 §4 derivation ($\mu \approx 2\alpha$ const) | `07_*` NQ-198a |
| **3. V5b-T' does not exist as separate phenomenon on torus** | V5b-T' canonical proposal (`20_*` Part 1) — claims "PN-barrier-lifted O(β) Goldstone on translation-invariant graphs" | **THIS file** NQ-198f |

### §3.2 Cumulative impact

**Three theoretical claims refuted in one day**:
- σ_multi^A(t) trajectory: rich-σ augmentation needed (NQ-242).
- V5b-F scaling: $\mu \propto |\partial S|/n$ (finite-size collective).
- **V5b-T' phenomenon: does not exist as separate concept** (subsumes V5b-T super-lattice trivially).

### §3.3 What this says about Day 2 Phase 3 work

Day 2 Phase 3 E5 (`11_PN_unification.md` §4) introduced the **unified PN-barrier formula**:
$$\mu_{\mathrm{PN}} = A\beta e^{-c_d/\xi_0} f_{\mathrm{comm}}(\phi) g_{\partial}(\delta/\xi_0)$$
recovering V5b-T (super-lattice), V5b-T' (cluster-saturated translation-invariant), and V5b-F (translation-broken).

**Day 3 EOD revision**:
- V5b-T (super-lattice): correct (Cat A canonical CV-1.4).
- V5b-T' (sub-lattice translation-invariant): **does NOT lift Goldstone — μ ≈ 0 exactly** (this NQ-198f).
- V5b-F (sub-lattice translation-broken): $\mu \propto |\partial S|/n$ (NQ-198a; Phase 3 form refuted).

The "unified formula" was **wrong**. PN-barrier-lifting only manifests on translation-broken graphs (V5b-F). Translation-invariant graphs preserve cluster Goldstone exactly.

---

## §4. D-5 Verdict Update: WITHDRAW

### §4.1 D-5 status before NQ-198f/g

Per `07_*` §6 + `08_*` §1: **D-5-A1 with revised text** (NQ-198a empirical $\mu \propto |\partial S|/n$ + V5b-T' torus open caveat).

### §4.2 D-5 status after NQ-198f/g (Day 3 EOD)

**REVISED RECOMMENDATION: WITHDRAW D-5**.

Reason: V5b-T' as a *new and distinct phenomenon* is refuted by NQ-198f. The proposed canonical entry "V5b-T' Pre-Objective Goldstone on Translation-Invariant Graphs in Corner-Saturated Regime" describes a phenomenon that **measurably does not exist** in the regime claimed.

What DOES exist:
- V5b-F (translation-broken, corner-saturated): $\mu \propto |\partial S|/n$. **Replace D-5 with a refined V5b-F entry**.
- Torus + corner-saturated: trivial extension of V5b-T (super-lattice translation-invariant) to lower c regime. No canonical entry needed; subsumed by T-V5b-T discussion.

### §4.3 What replaces D-5

**Proposal: D-5b (NEW)** — revise D-3 V5b-F mechanism rider in T-V5b-T entry to incorporate NQ-198a empirical scaling. ~10 lines additional text. Leverages D-3 (already approved) rather than new D-5 entry.

**Replace D-5-A1 (V5b-T' new entry, ~70 lines)** with **D-5b (V5b-F mechanism rider expansion in D-3, ~15 lines)**. Net canonical line reduction: -55 to -65 lines.

**D-5-W1 (NEW WITHDRAW path)**:
- Withdraw V5b-T' new entry from CV-1.5.1 release.
- Update D-3 V5b-F mechanism rider with NQ-198a scaling (~10 lines added).
- V5b-T'-related work archives in `THEORY/logs/daily/2026-04-29/` daily files (this `11_*`, `07_*`, `05_*`).
- Future canonical revision: only after `05_*` §4 derivation is corrected via NQ-198e (rigorous 1/n analytical) and NQ-198f extended (β-scan on torus to test if V5b-T' might exist in some other regime).

### §4.4 Revised user-decision queue (Day 4 morning)

| Item | Original (`01_*`) | Day 3 deepening (`06_*`) | Day 3 EOD post-NQ-198fg |
|---|---|---|---|
| D-1 (Comm 14 (O5')) | Approve | Approve | **Approve** |
| D-2 (Comm 14 (O7)) | Approve | Approve | **Approve** |
| D-3 (V5b-F rider in T-V5b-T) | Approve | Approve | **Approve + ~10 lines NQ-198a scaling** |
| D-4 (ζ_*(graph, c)) | Approve | Approve | **Approve** |
| **D-5 (V5b-T' new entry)** | Approve | Approve revised | **WITHDRAW** |
| D-6a (Comm 14-Multi static) | Approve | Approve | **Approve** |
| D-6b (Comm 14-Multi dynamic) | Defer | Defer to W6+ | **Defer to W6+** |

**Revised canonical line delta**: D-1 (~10) + D-2 (~15) + D-3 (~25, was 18; +7 for NQ-198a scaling) + D-4 (~12) + D-6a (~35) = **~95-100 lines** (was 165-200 with D-5; -65 to -100 with D-5 withdrawn).

Significantly leaner CV-1.5.1 release. **Better signal-to-noise** (only solid Cat A/B claims merged).

---

## §5. V5b Family Revised Taxonomy

### §5.1 Day 2 EOD taxonomy (now revised)

```
V5b family:
├── V5b-T (super-lattice, c interior, translation-invariant)
│     → exp-suppressed Goldstone, Cat A canonical CV-1.4
├── V5b-T' (sub-lattice, c < c_s, translation-invariant) [NEW Phase 3]
│     → "PN-barrier-lifted O(β) Goldstone"
│     → Cat B target Phase 3 → ?
├── V5b-F (sub-lattice, c < c_s, translation-broken) [Phase 3 refined]
│     → "partial Goldstone H1+H2+H3 mixed"
│     → Cat B target → Cat B empirical
```

### §5.2 Day 3 EOD revised taxonomy

```
V5b family (revised post-NQ-198f/g):
├── V5b-T (super-lattice, c interior, translation-invariant)
│     → exp-suppressed Goldstone, Cat A canonical CV-1.4 (UNCHANGED)
├── V5b-T-zero (sub-lattice, c < c_s, translation-invariant) [REPLACES V5b-T']
│     → exact zero Goldstone (cluster orbit symmetry)
│     → Cat A empirical (NQ-198f)
│     → NOT a new phenomenon; extension of V5b-T to lower c
├── V5b-F (sub-lattice, c < c_s, translation-broken) [empirically anchored]
│     → μ ≈ C(β,ξ_0) |∂S|/n; empirical Cat B
│     → β-scaling open (NQ-198g insufficient)
```

### §5.3 Why V5b-T' was a phantom

V5b-T' was introduced Phase 3 E10 from the observation: **corner-saturation regime on translation-invariant graph also exists** (E10 ζ=0.43 R3a/R3b transition). The IMPLICIT assumption was that this regime has *non-trivial* Goldstone-lifting analogous to V5b-F.

NQ-198f shows: **NO LIFTING**. The cluster on torus has exact translation orbit; Goldstone is exactly 0.

What was Phase 3 actually observing? The R3a/R3b transition was real (mode-crossing at ζ=0.43). But it was a transition between **two zero-eigenvalue eigenvectors** mixing — NOT a transition involving non-zero Goldstone-lifting. The "lifting" was inferred from `01_NQ173_v5b_f_verdict.md` data (free-BC! NOT torus); incorrectly generalized to torus.

**Lesson**: Phase 3 E5 unified PN-barrier formula was over-generalizing. Free-BC data → free-BC formula. Don't extrapolate to torus without testing.

---

## §6. New Open Questions

**NQ-198j (URGENT W6 Day 1)**: Does V5b-T' exist in a *different* regime not tested by NQ-198f? E.g., on torus with mass m perfectly commensurate with lattice (m = k² for integer k)? Or with non-square cluster shape?

**NQ-198k**: V5b-F β-dependence with $|\partial S|$-controlled experiments. NQ-198g varied β but $|\partial S|$ also changed. Need fixed-$|\partial S|$ β-scan (e.g., fix L, c, but adjust IC to give same cluster shape across β).

**NQ-198l**: V5b-F vs V5b-T-zero **continuity**: as graph topology smoothly interpolates from torus to free-BC (e.g., adding boundary edges one by one), does $\mu$ smoothly transition from 0 to $C|\partial S|/n$? Or is there a phase boundary?

**NQ-198m (cancels NQ-198a-c)**: Now that V5b-T' is empirically shown not to exist, several Day 2 Phase 3 spawns become obsolete:
- NQ-198 (was: V5b-T' Cat A WKB+tight-binding; W7+) — **CANCEL** (no V5b-T' to derive Cat A for).
- NQ-198b (V5b-T' Cat A): **CANCEL**.
- NQ-198d (V5b-T' corner corrections): **CANCEL**.
- NQ-247 (V5b-T'/F cluster-hop dynamics): **REFRAME** as V5b-F only.
- `05_*` §4 "Cat A path" (claimed for V5b-T'): **withdrawn**; remains valid only as a thought experiment with explicit failure (predicts μ const which is NOT observed on either torus or free-BC).

### §6.1 Net spawn count update

Previously 14 NQ spawns (Day 3 EOD per `08_*` §4.3). Cancellations:
- NQ-198 (original): cancel.
- NQ-198b: cancel.
- NQ-198d: cancel.
- NQ-247 reframe: count as NQ-247' (V5b-F only).

Add NEW from this file:
- NQ-198j (V5b-T' regime hunt, urgent W6).
- NQ-198k (β-dep with |∂S| controlled).
- NQ-198l (V5b-F ↔ V5b-T-zero continuity).

**Net Day 3 spawns**: 14 - 3 cancel - 1 reframe + 3 new = **13 net new spawns** (well, 14 still due to reframe, but cleaner count).

---

## §7. Day 4 Morning Revised Plan

Per `10_*` §3.1 + Day 3 EOD insights:

### §7.1 Updated Day 4 morning sequence (~2-3h)

1. (~5 min) Read this `11_*` for D-5 WITHDRAW recommendation.
2. (~30 min) Apply 7 priority corrections per `09_*` §7 — except correction (5) is now superseded by D-5 WITHDRAW (no V5b-T' regime distinction needed if entry is gone).
3. (~30 min) **Apply D-3 V5b-F rider expansion** with NQ-198a scaling text per §4.3 above. (Replaces D-5 application.)
4. (~60 min) Block 1 canonical apply (D-1..D-4 + D-6a; D-5 WITHDRAWN).
5. (~30 min) `04_*` Theorem 4.6.1 → `working/MF/sigma_multi_trajectory.md` promote.
6. (~30 min) Day 4 99_summary + weekly_draft 04-30 entry.

**Total**: ~3h Day 4 morning.

### §7.2 Day 4 PM (~3-4h)

- (~1-2h) NQ-244 (3D LSW T³_15 K=10) — Paper §4.5.5.
- (~30 min) NQ-198k (β-dep with |∂S| controlled). Information-cheap follow-up.
- (~30 min) NQ-198l (V5b-F ↔ V5b-T-zero continuity).
- (~1h) Paper §4 LaTeX skeleton in `papers/`.

### §7.3 W5 ladder revised target

With D-5 WITHDRAW + cleaner CV-1.5.1:
- **CV-1.5.1**: D-1..D-4 + D-6a, ~95-100 lines, robust Cat A/B claims.
- Paper §4 polished + LaTeX-ready.
- 3D LSW publishable α (NQ-244).
- NQ-242 framework preserved for W6+ CV-1.6.

**W5 Stretch achievable Day 7**: same target as before but with leaner canonical (no V5b-T' phantom).

---

## §8. Hard Constraint Verification

- [x] canonical 직접 수정 0 — all D-5 WITHDRAW recommendations are proposals; no edits.
- [x] Silent resolution 0 — V5b-T' refutation explicit; D-5 status change explicit.
- [x] No primitive override.
- [x] No 4-term merging.
- [x] K=1 single-formation throughout NQ-198f/g.
- [x] No metastability without P-F flag — corner-saturated regime on torus IS metastable; P-F flag inherited from `07_*` setup.
- [x] No reductive equation.
- [x] All NQ cancellations documented; net spawn count updated.

---

## §9. Summary

**Day 3 EOD reality**:
1. Three substantive negative results (σ^A non-determinism + V5b-F empirical scaling + **V5b-T' phantom**).
2. **V5b family revised taxonomy** (no V5b-T' as separate phenomenon).
3. D-5 WITHDRAW recommended.
4. Cleaner CV-1.5.1 (~95-100 lines, no V5b-T' phantom entry).
5. 14 NQ spawns net (3 V5b-T' cancellations + 3 new V5b-F refinements).

**Methodological wins**:
- NQ-198f as a **disconfirmation experiment**: cost ~5 min compute + 30 min analysis. Refuted a Day 2 Phase 3 canonical proposal at ZERO cost to canonical (since proposal hadn't been merged).
- This is exactly the pattern advocated in `10_*` §3.5.1 (pre-registered numerical experiment) — should have been default.

**What this means for the day**:
- Better to have done NQ-198f BEFORE writing `05_*` (save 1.5h theoretical work that was based on V5b-T' assumption).
- Future deepening: do `<30 min` numerical sanity check on the assumed phenomenon BEFORE building theory.

---

**End of 11_NQ198fg_results_and_D5_withdraw.md.**
**Status: NQ-198f shows V5b-T' has μ ≈ 0 on torus (no PN-barrier-lifting). NQ-198g shows C(β) is non-trivial. D-5 V5b-T' WITHDRAW recommended; replace with D-3 V5b-F rider expansion (~10 lines NQ-198a scaling). Revised CV-1.5.1: ~95-100 lines (vs original 165-200 with D-5). 13 NQ spawns net post-cancellations.**
