# 22 — Deepening Round 20: NQ-36 Resolved + Static/Dynamic Decoupling (2026-04-22 night)

**Trigger:** Single-formation audit (summary §16.5 NQ-36) + user-executed fine β-scan.
**Experiment:** `exp_k_hat_validation.py --grid 32 --c 0.7 --seeds 30 --skip-square --skip-torus --beta-list "3.0,4.0,...,10.0"`
**Runtime:** 105.1 s.
**Output:** `CODE/experiments/results/exp_nq36_betascan.json`.
**Predecessor:** R19 (c=0.7 coarse scan bracketed β_c ∈ (3, 10)).

---

## §1. NQ-36 resolution

### 1.1 Data (1D cycle C_1024, c=0.7, α=1.0, 30 seeds per β)

| β | N_unst | $\widehat K$ (mean ± std) | Range | Regime |
|---|---|---|---|---|
| 3.0 | 298 | 1.00±0.00 | 1-1 | single |
| 4.0 | 348 | 1.00±0.00 | 1-1 | single |
| 5.0 | 394 | 1.00±0.00 | 1-1 | single |
| 6.0 | 438 | 1.00±0.00 | 1-1 | single |
| 7.0 | 482 | 1.00±0.00 | 1-1 | single |
| 8.0 | **499 (saturated)** | 1.00±0.00 | 1-1 | single |
| **9.0** | 499 | **3.97±1.56** | **1-7** | **bistable / transition** |
| 10.0 | 499 | 9.50±1.96 | 6-14 | multi |

### 1.2 Sharp β_c bracketed

**β_c ∈ (8, 9)**, best estimate $\beta_c(c=0.7) \approx 8.5 \pm 0.5$ at L=1024.

**Bistable region** at β=9: 30 seeds span range 1-7, i.e., the same parameter set produces K=1 metastable for some realizations and K~7 for others. Standard deviation 1.56 ≈ mean × 0.4 — extremely wide distribution compared to β=10 (std/mean ≈ 0.21) or β=8 (exactly deterministic).

## §2. Static/Dynamic Decoupling — Cat A empirical

### 2.1 N_unst saturation occurs at β=8, K̂ transition at β=9

**Critical observation**: By β=8, the Hessian already has N_unst = 499 negative eigenvalues — all non-constant modes are linearly unstable. Prop 1.3a says: "uniform is a local maximum along all n-1 constrained directions". In static terms, the uniform state is maximally unstable.

**Yet K̂ = 1.00 deterministically at β=8**. Gradient flow from noise initialization coarsens to single formation despite all eigendirections being unstable.

**At β=9, no change in N_unst** (still 499, saturated). But K̂ explodes to 3.97 with bistable variance.

### 2.2 The decoupling statement (Cat A empirical)

> **R20 Decoupling (Cat A empirical, L=1024, c=0.7).** On 1D cycle, the static spectral threshold (N_unst saturation at β_sat ≈ 8) and the dynamic formation threshold (β_c ≈ 8.5) are **distinct** and **not causally related** — N_unst remains constant across β_c while K̂ discontinuously transitions.

**Implication**: The quantity $N_{\mathrm{unst}}(\beta)$ does NOT determine $\widehat K(\beta)$ even qualitatively. The dynamic threshold is governed by a **separate mechanism** beyond Hessian spectrum.

### 2.3 Candidate dynamical mechanism

Between β=8 and β=9, what changes? N_unst is saturated, so the change must be in:

- **Nonlinear basin structure** — relative basin volumes of K=1 vs K>1 minimizers shift.
- **Saddle-node connectivity** — gradient flow trajectories from uniform may switch basins due to saddle-node bifurcation of intermediate saddles.
- **Timescale separation** — K=1 attractor's basin of attraction in the dynamic sense (gradient flow, finite time) shrinks despite remaining a static minimizer.

None of these appear in Prop 1.3a/b or Conjecture 2.1. They require **nonlinear metastability analysis** — Kramers escape rates, tree structure of bifurcation cascades, or direct numerical basin volume estimation.

## §3. Impact on Conjecture 2.1 (all versions)

### 3.1 Review of Conjecture 2.1 evolution

- **v1-v3** (R1-R16): $\widehat K \sim \sqrt{N_{\mathrm{unst}}}$ (Weyl square root)
- **v4** (R17): Added c-regime split (c<1/2 rich, c=1/2 unity)
- **v5** (R18+R19): 2D has c≥0.5 unity regime; 1D cycle has c-dependent $\beta_c$

All five versions share the premise: **$\widehat K$ is some function of $N_{\mathrm{unst}}$**.

### 3.2 R20 refutes the premise

At c=0.7 on 1D cycle:
- N_unst is **monotone increasing** in β (up to saturation at β≈8).
- $\widehat K$ is **discontinuous step function**: ≡1 for β<8.5, then jumps to ~4 then ~10.

There is **no continuous functional relationship** $\widehat K = f(N_{\mathrm{unst}})$ compatible with this data. The mapping $N_{\mathrm{unst}} \to \widehat K$ is **not even well-defined** (N_unst = 499 corresponds to K̂=1 at β=8 AND K̂≈10 at β=10).

### 3.3 Conclusion — Conjecture 2.1 abandoned

**All Conjecture 2.1 versions (v1-v5) refuted.** The framework "$\widehat K = f(N_{\mathrm{unst}})$" for any function $f$ is incompatible with R20 data.

**Replacement framework needed** — likely:
- $\widehat K = F(\beta, c, G; \text{initial condition manifold})$ as a **dynamic** object.
- N_unst is **necessary but not sufficient**: N_unst ≥ 1 is needed for any non-uniform formation, but does not determine $\widehat K$.
- Separate theory needed for the **emergence-to-coarsening transition** (β_c), drawing on Kramers, basin volumes, or saddle-node cascades.

## §4. Canonical impact

### 4.1 Retractions required (weekly merge)

1. **Conjecture 2.1 (all versions in working/MF/from_single.md §2)** — retract entirely.
2. **Round 6 §2.3e 3-regime dynamical extension** — already flagged for retraction per R19, R20 reinforces this.
3. **symmetry_moduli.md §3.7.5 Conjecture 2.1-Bott** — already flagged, R20 strengthens.
4. **cardinality_open.md §4.2** — the link "$c_0$ has many high-K configurations → $\widehat K$ samples them" is now explicitly broken; gradient flow selects K=1 basin almost always below β_c even when many higher-K minimizers exist statically.

### 4.2 Preserved Cat A (unaffected by R20)

All static-only theorems are unaffected:
- Prop 1.3a, Prop 1.3b (a)-(e), Prop 1.3a-Bott, Prop 1.3a-thermal, Prop 1.3b-thermal.
- Cor 2.2 qualitative + quantitative (tanh).
- G-C Universal $c_0$-Counting Theorem (static count).
- G-D $\Phi_4$ axis selection, $C_n$ Lock-In.

These describe **static structure** (Hessian, energy landscape, critical point count), which R20 does NOT refute.

### 4.3 New canonical statement candidate

> **C-2026-04-22-R20 (Cat A empirical).** For 1D cycle $C_{1024}$ at c=0.7, α=1.0:
> - N_unst saturates at β_sat ≈ 8 (all non-constant modes unstable).
> - Dynamic formation transition occurs at β_c ≈ 8.5 ± 0.5.
> - Bistable coexistence region at β_c with K̂ range 1-7 across 30 seeds.
> - Above β_c, K̂ grows approximately linearly with β (K̂=9.5 at β=10, K̂~30+ at β=30 per R19).

**Implication**: Static spectral data alone does not determine dynamic formation count.

## §5. New open questions

- **NQ-38 (new, high priority)**: What determines β_c? Candidate mechanisms to rank:
  - (a) Secondary bifurcation on primary branch (Round 10 framework).
  - (b) Basin volume crossover (basin of K=1 shrinks below basin of K>1).
  - (c) Saddle-node collision rate exceeding barrier rate.
- **NQ-39**: β_c as function of $c$ on 1D cycle — R17 (c=0.3) shows no threshold (always multi), R18 (c=0.5) always K=1, R19+R20 (c=0.7) threshold ≈ 8.5. Predict β_c(c) curve.
- **NQ-40**: β_c on 2D square/torus — R19 bracketed β=30 (square has K̂=1.08 with 1-2 range, torus perfect K̂=1). Sharper scan at β=20, 50 needed.

## §6. Session update (post-R20)

- R1-R19: 101 Cat A/B
- **R20: +3 Cat A empirical** (NQ-36 bracket, static/dynamic decoupling statement, Conjecture 2.1 refutation)
- **Grand total: 104 Cat A/B** (20 rounds)
- **Conjecture 2.1 (v1-v5): RETRACTED**
- **Q-items: Q1-Q60** (+Q58 decoupling canonical entry, +Q59 C-R20 canonical, +Q60 Conjecture 2.1 formal retraction)

## §7. Files created/affected

- **Created**: `logs/daily/2026-04-22/22_deepening_round20.md` (this file).
- **Created**: `CODE/experiments/results/exp_nq36_betascan.json` (β=3-10 fine scan).
- **Affects (weekly merge retraction list)**:
  - `working/MF/from_single.md` §2 — Conjecture 2.1 full retraction.
  - `working/SF/mode_count.md` §2.3e — dynamic extension retraction (confirmed).
  - `working/SF/symmetry_moduli.md` §3.7.5 — Conjecture 2.1-Bott retraction (confirmed).
  - `working/SF/cardinality_open.md` §4.2 — static-dynamic link clarification.

---

**End of Round 20 log.**
**Session status: 20 rounds, 104 Cat A/B, Conjecture 2.1 (all v1-v5) retracted, static-dynamic decoupling established as Cat A empirical.**
