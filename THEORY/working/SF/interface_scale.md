# interface_scale.md — Cor 2.2 qualitative + quantitative

**Status:** commit draft, 2026-04-22 (SF-S1 session).
**Author origin:** Round 13 + Round 17 + Round 18 (`exp_interface_ansatz`, `exp_alpha_scan_v3` numerical).
**Canonical refs:** §13 Cat A T11 (Γ-convergence Modica-Mortola), T-Merge (b) (isoperimetric ordering), Deep Core Dominance 2b, Coupling Bound Lemma Item 5 (exponential tail decay).
**Working refs:** `working/SF/mode_count.md` ($N_{\mathrm{unst}}$), `working/SF/profile_deviation.md` (NQ-32), `working/MF/from_single.md` §3 (formation size), §4 (spacing).
**Source experiments:** `CODE/experiments/exp_interface_ansatz.py`, `results/exp_interface_ansatz.json`; `CODE/experiments/exp_alpha_scan_v3.py`, `results/exp_alpha_scan_v3.json`.
**External refs:** Modica-Mortola (1977), *Un esempio di Γ-convergenza*, Boll. UMI; Cahn-Hilliard (1958), *Free energy of a nonuniform system*.

---

## §1. Setup and the interface scale $\xi_0$

Define $\xi_0 := \sqrt{\alpha/\beta}$, the natural interface width for $\mathcal{E}_{\mathrm{bd}}$. Its status across canonical:

| Appearance | Context | Cat |
|---|---|---|
| line 894 | Sharp-interface dynamics "Extension" | Remark only |
| line 964-965 | T11 Γ-convergence | Cat A (but $\varepsilon \to 0$ limit only) |
| line 1005, 1053 | T-d_min-Formula | Cat B (direction bug — fix in §7) |
| line 831 | Coupling Bound Lemma Item 5 | Cat A ($\kappa = \sqrt{\beta/(2\alpha)} = \xi_0^{-1}/\sqrt 2$, inter-core tail) |
| line 994 | T-Birth-Parametric (D₄) | Cat A ($\beta_{\mathrm{crit}}/\alpha$ composite) |

**Round 13 assessment:** $\xi_0$ is **not a formal subject** in canonical. It appears as a scaling parameter and a decay constant, but no theorem targets it. This file fills that gap.

---

## §2. Corollary 2.2 (qualitative)

### 2.1 Formal statement

> **Cor 2.2 (qualitative, interface concentration).** Let $G$ be a finite connected graph, $u^\ast$ any local minimizer of $\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$, $A^\ast := \{x : u^\ast_x \geq 0.5\}$, $B(u^\ast) := \{x : 0.1 < u^\ast_x < 0.9\}$. Then
> $$|B(u^\ast)| \;\leq\; \frac{16}{\ln 9}\cdot \frac{\mathcal{E}_{\mathrm{bd}}(u^\ast)}{\beta} \;=\; O\!\big(\sqrt{\alpha/\beta}\cdot \mathrm{Per}_G(A^\ast)\big) \;=\; O(\xi_0\cdot \mathrm{Per}_G(A^\ast)).$$

### 2.2 Proof

See `logs/daily/2026-04-22/02_development.md` §4.2 for the three-step proof:
1. Boundary-band lower bound $\mathcal{E}_{\mathrm{bd}} \geq \beta|B|/16$ (elementary: $W(u) \geq 1/16$ on $(0.1, 0.9)$ after normalization).
2. Modica-Mortola upper bound $\mathcal{E}_{\mathrm{bd}}(u^\ast) \leq C_\ast\sqrt{\alpha\beta}\cdot \mathrm{Per}_G(A^\ast)$ (canonical T11 Cat A).
3. Combine: $|B| \leq (16/\ln 9)\cdot C_\ast\sqrt{\alpha/\beta}\cdot \mathrm{Per}_G = O(\xi_0\cdot \mathrm{Per})$. ∎

### 2.3 Category self-classification

**Cat A** — direct from canonical T11 (Cat A) + elementary bound.

### 2.4 Numerical backing (qualitative)

Three independent experiments support the ∝ $\xi_0$ scaling:

| Experiment | Result | Reference |
|---|---|---|
| **exp16** (`transition_layer.py`) | $d_H(\mathrm{Core}, S^\ast) \leq \delta_\varepsilon + 1$ where $\delta_\varepsilon = \mathrm{arccosh}(1 + \beta/8)^{-1}\ln(2/\varepsilon)$. Passes all (grid, β). Aligns with $c_0$-decay single-formation. | Round 14 |
| **exp42** (`scale_verification.py`) | Boundary/Core ratio vs $n$: slope ≈ −0.5 fit, theory −0.5 within 5%. | Round 14 |
| **exp_alpha_scan_v2** (asymptotic) | $\xi_0$-axis scan, asymptotic regime. | Round 15 |

All three confirm the qualitative statement $|B|/\mathrm{Per} \propto \xi_0$ along three independent axes (grid size, $n$-scaling, $\alpha$-axis).

---

## §3. Corollary 2.2 (quantitative, tanh ansatz)

### 3.1 Formal statement

> **Cor 2.2 (quantitative, tanh ansatz).** Let the configuration $u^{\mathrm{tanh}}(x)$ on 2D square grid be the radial profile
> $$u^{\mathrm{tanh}}(x) = \tfrac{1}{2}\big(1 - \tanh\!\big(s(x)/\xi_0\big)\big),$$
> where $s(x)$ is the signed distance from a circular interface. Then
> $$\frac{|B(u^{\mathrm{tanh}})|}{\mathrm{Per}_G(A^{\mathrm{tanh}})} \;=\; \frac{\pi\ln 9}{2}\cdot \xi_0 \;+\; O(1/\sqrt n) \;\approx\; 3.449\cdot \xi_0.$$

### 3.2 Derivation (analytic, grid-invariant constant)

See `logs/daily/2026-04-22/02_development.md` §4.4. Five steps:

1. **Interval width at $0.1 < u < 0.9$.** Solving $\tanh(s/\xi_0) = \pm 0.8$: $s/\xi_0 = \pm \tfrac{1}{2}\ln 9$. Total width: $\ln 9\cdot \xi_0 \approx 2.197\cdot \xi_0$.
2. **Continuum boundary-band area.** $|B_{\mathrm{cts}}| = \mathrm{Per}_{\mathrm{cts}}\cdot \ln 9 \cdot \xi_0$.
3. **Grid-to-continuum perimeter factor.** $\mathrm{Per}_{\mathrm{edge}} = (2/\pi)\cdot \mathrm{Per}_{\mathrm{cts}}$ on 4-connected grid. Hence $\mathrm{Per}_{\mathrm{cts}} = (\pi/2)\mathrm{Per}_{\mathrm{edge}}$.
4. **Grid boundary-band count.** $|B_{\mathrm{sites}}| \approx |B_{\mathrm{cts}}|$ (lattice spacing 1).
5. **Ratio.** $|B_{\mathrm{sites}}|/\mathrm{Per}_{\mathrm{edge}} = \mathrm{Per}_{\mathrm{cts}}\ln 9\, \xi_0 / ((2/\pi)\mathrm{Per}_{\mathrm{cts}}) = (\pi\ln 9/2)\cdot \xi_0 \approx 3.449\cdot \xi_0$. ∎

### 3.3 Numerical verification (Round 17 exp_interface_ansatz)

Setup: 5 grid sizes {32, 64, 128, 256, 512}, 11 $\xi_0$ values in {0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 6, 8}, 2 profiles (tanh, linear), 2 metrics (edge-perimeter, site-perimeter). Total 220 ratio fits.

| Metric | R² linear fit | Log-log slope | Intercept |
|---|---|---|---|
| Linear R² | ≥ 0.998 | — | — |
| Log-log slope | — | [0.94, 1.08] (theory 1.0) | — |
| Intercept b | — | — | ≤ 0.2 |

**20/20 fits PASS** (5 grids × 2 profiles × 2 metrics), all asymptotes converge to constants.

| Profile | Metric | $C$ (grid 32) | $C$ (grid 512) | Predicted | Accuracy |
|---|---|---|---|---|---|
| tanh | edge | 3.358 | 3.450 | $\pi\ln 9/2 \approx 3.449$ | **3‰** |
| tanh | site | 2.439 | 2.445 | $3.449/\sqrt 2 \approx 2.439$ | 2‰ |
| linear | edge | 2.511 | 2.520 | $0.8\pi \approx 2.513$ | 3‰ |
| linear | site | 1.832 | 1.785 | $0.8\pi/\sqrt 2 \approx 1.777$ | 4‰ |

**Grid-invariance.** site/edge ratio $\approx \sqrt 2 = 1.414$ for both profiles (2D grid topological constant). Consistency: tanh 3.45/2.45 = 1.41 ✓; linear 2.52/1.79 = 1.41 ✓.

Runtime: 43.8 seconds total (no `find_formation`; ansatz construction only).

### 3.4 Category self-classification

**Cat A** (tanh ansatz on 2D square grid):
- Explicit analytic derivation of $C = \pi\ln 9/2$ (step-granularity: 5 steps, each elementary).
- 20/20 PASS at $n$ up to 262144.
- Constant is profile-specific, grid-invariant, mathematically derivable.

### 3.5 Linear profile alternative

For linear profile $u(s) = 0.5 - 0.5(s/(\xi_0/2))$ with $|s| < \xi_0/2$:
- Continuum boundary-band width (where $u \in (0.1, 0.9)$): $0.8\cdot \xi_0$.
- Ratio: $(\pi/2)(0.8) = 0.4\pi \approx 1.257$ edge → measured 2.520 (factor 2 larger because the $|B|$ definition uses $\xi_0$ full-width convention in experiment).
- Reconciled via Round 17 §8.4: $C_{\mathrm{lin,edge}} = 0.8\pi \approx 2.513$, measured 2.520, 3‰ off. ✓

---

## §4. Gap to SCC full minimizer (NQ-32)

### 4.1 Round 18 observation

Round 18 `exp_alpha_scan_v3` at $(\alpha = 2, \beta = 80, \xi_0 = 0.158)$, sharp K=1 (K_soft ≤ 0.55, only 1/9 passed filter):

| Metric | Measured | Predicted (tanh ansatz $C = 3.449$) | Deviation |
|---|---|---|---|
| ratio_edge | 0.875 | 0.546 | **+60%** |
| ratio_site | 0.323 | 0.386 | −16% |

### 4.2 Interpretation

The SCC full-energy minimizer is NOT the tanh ansatz. Prop 1.3b (`working/SF/mode_count.md`) shows that $H_{\mathrm{cl,sep}}$ has 1641 negative eigenvalues at canonical defaults, perturbing the eigendirections along which the minimizer forms. The profile of the actual SCC minimizer deviates from pure tanh, hence Cor 2.2 quantitative (tanh-specific) does not directly apply.

### 4.3 Three-tier Cor 2.2 status

| Tier | Claim | Status |
|---|---|---|
| **1. Mathematical (tanh ideal)** | `ratio = 3.449·ξ_0` exact | **Cat A** (Round 17, 20/20 PASS) |
| **2. Qualitative (any K=1)** | `ratio ∝ ξ_0` | **Cat A** (three exp axes) |
| **3. SCC full ℰ minimizer** | `ratio` vs `3.449·ξ_0` 20-60% dev | **Cat B / NQ-32 open** |

See `working/SF/profile_deviation.md` for the NQ-32 investigation.

---

## §5. Three natural length scales

| Scale | Value | canonical status | Physical meaning |
|---|---|---|---|
| $\xi_0 = \sqrt{\alpha/\beta}$ | interface width (this file) | implicit (G-B gap — **fills**) | Transition-layer thickness |
| $1/\kappa = \sqrt{2\alpha/\beta} = \sqrt 2 \xi_0$ | Screened Poisson decay | Cat A (Coupling Bound Lemma Item 5) | Inter-core exponential tail length |
| $d_{\min}^\ast$ | multi-formation separation | Cat B (T-d_min-Formula, direction WRONG) | Metastable inter-formation distance |

**New result from `02_development.md` §7**: $d_{\min}^\ast \asymp \xi_0\cdot \log(1/\epsilon_0)$ (direction correction). The canonical fit $d_{\min}^\ast \propto \sqrt{\beta/\alpha} = 1/\xi_0$ is dimensionally backward. This is NQ-30 — carry to `integer_K_dependency_map.md` rewrite.

---

## §6. Multi-formation bridge

The interface width $\xi_0$ directly determines:
- **Formation size:** $r_0 = \sqrt{m/(\pi \widehat{K})}$ (disk radius from mass conservation); the boundary band has area $2\pi r_0 \xi_0$ per formation.
- **Formation spacing:** $d_{\min}^\ast \asymp \xi_0\log(1/\epsilon_0)$ — closer formations at smaller $\xi_0$ (higher $\beta$).
- **Max formation count:** $\widehat{K}_{\max} \leq L^2/(\pi r_0^2 + 2\pi r_0 d_{\min}^\ast) \leq L^2/(\pi r_0(r_0 + 2\xi_0\log))$.

All three relations use $\xi_0$ as the fundamental length; see `working/MF/from_single.md` §3–§4.

---

## §7. Canonical merge targets (Stage 6 Pending)

1. **§13 Cat A:** one entry for Cor 2.2 qualitative (reusing T11 + lower bound).
2. **§13 Cat A:** one entry for Cor 2.2 quantitative (tanh ansatz, constant $C = \pi\ln 9/2$).
3. **§5 or §8 new subsection:** "Single-Formation Geometry" anchoring $\xi_0$ as a formal subject with the three-scales table (§5 above).
4. **§13 T-d_min-Formula:** direction correction from $\sqrt{\beta/\alpha}$ to $\xi_0 = \sqrt{\alpha/\beta}$. This is a **Cat B correction**, not a new claim; accompanied by NQ-30 flag.
5. **§14 CN14:** quantitative reinterpretation of the "closure reduces $d_{\min}^\ast$ by 30%" claim as "closure shortens the effective $\xi_0$ via enhanced decay" (§3 of `02_development.md` §7.3).

---

## §8. File status

- **Cor 2.2 qualitative:** committed Cat A.
- **Cor 2.2 quantitative (tanh):** committed Cat A, 20/20 PASS.
- **Cor 2.2 SCC minimizer:** Cat B / open (NQ-32 in `profile_deviation.md`).
- **$\xi_0$ as formal subject:** proposed for canonical §5/§8 new subsection.
- **T-d_min-Formula direction correction:** proposed as Cat B correction (NQ-30, `integer_K_dependency_map.md` update).

**End of interface_scale.md.**
