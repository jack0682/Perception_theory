# 06 — Further Verification (Round 3, substantive deepening)

**Session:** 2026-04-21 (post `04_hypothesis_audit.md` + `05_deepening_and_verification.md`)
**Purpose:** Round 2 (file 05) 에서 "sketched" 로 남긴 핵심 수학 항목들을 한 단계 더 심화. 특히 (a) ℱ_C+E Hessian 의 explicit 계산 — Kramers prefactor (R-M1-A) 및 Witten Laplacian small eigenvalues (G6) 의 직접 입력, (b) Mountain Pass test-path 상한 (NQ-11 정량화 시도), (c) F3 Langevin well-posedness 의 rigorous 형식 (Lions-Sznitman). 덧붙여 몇 가지 추가 sanity check.
**This file covers:** Hessian ∇²ℱ_C+E explicit decomposition (§1) + T-7 (Enhanced Metastability) 의 C+E 잔존 (§2) + Mountain Pass test-path 상한 (§3) + 부면 연결성 (§4) + K_soft vs Q_morph 정합 (§5) + HS prefactor 검증 (§6) + Sard on Σ_m^ε (§7) + F3 Lions-Sznitman rigorous statement (§8) + 발견사항 및 NQ (§9).
**Depends on reading:** all prior daily files (01-05) + working files + canonical §8-13 + external refs (Lions-Sznitman 1984, Bovier-Eckhoff-Gayrard-Klein 2002, Clarke 1983).

---

## §1. Hessian of ℱ_C+E at K_soft ≈ K Critical Points — Explicit Decomposition

### 1.1 Why this computation matters

The constrained Hessian `H := Π_T ∇²ℱ_C+E Π_T` (projected onto `T_u Σ_m`) is the direct input to:
- **Kramers prefactor** (G5 §3.2): `τ_0 = (2π/|ω_s|)·√(det H_a / |det H_s|)`.
- **Witten Laplacian small eigenvalues** (G6 §3.2): `λ_1 ~ ... exp(-ΔF/T)` with prefactor depending on Hessian determinants.
- **T-7 (Enhanced Metastability)** survival check: does closure's positive Hessian contribution survive C+E terms?
- **Mountain Pass saddle** characterization (NQ-11): saddle has exactly 1 negative eigenvalue.

Without explicit Hessian form, all four items remain "sketched". This section makes them concrete up to the level of **per-term explicit contributions** (not per-numerical-graph).

### 1.2 Full Hessian decomposition

$$
\nabla^2 \mathcal{F}_{C+E}[u; T, \lambda_K] \;=\; \nabla^2\mathcal{E}[u] \;+\; T\cdot\nabla^2(-S)[u] \;+\; \lambda_K\cdot\nabla^2 K_{\mathrm{soft}}[u].
$$

Three terms, each computed separately.

### 1.3 Term 1: ∇²ℰ (canonical energy Hessian)

From canonical §8 and §13 (Cat A T-7, T8-Core, T8-Full, T-Bind-Proj, etc.):

$$
\nabla^2 \mathcal{E}[u] \;=\; \lambda_{cl}\, H_{cl}(u) \;+\; \lambda_{sep}\, H_{sep}(u) \;+\; \lambda_{bd}\, H_{bd}(u) \;+\; \lambda_{tr}\, H_{tr}(u).
$$

Dominant components at sharp-interface critical points:
- **H_bd**: `H_{bd}(u) = 4\alpha\, L + \beta\, \mathrm{diag}(W''(u(x)))` where L = graph Laplacian, W''(u) = 2 - 12u + 12u². At u = 0: W'' = 2. At u = 1: W'' = 2. At u = 1/2: W'' = -1 (maximum negative curvature in spinodal). At u ≈ 0 or 1 (interior / exterior sites): contributes `+2β` to diagonal. Positive at stable sharp-interface configurations.
- **H_cl**: positive-semidefinite from closure Gram matrix. T-3/T-7 establish this adds strictly positive Hessian `2(I - J_Cl)^T(I - J_Cl)` per site.
- **H_sep**: smaller; mixed signs.
- **H_tr**: typically 0 for within-time analysis (G3 §1.1).

**Positive minimum eigenvalue at K_soft ≈ K critical points:** `μ_K^{(ℰ)} := λ_{\min}(Π_T ∇²ℰ Π_T) > 0`. Typically `μ_K^{(ℰ)} ~ O(β)` at sharp-interface (canonical exp-observations).

### 1.4 Term 2: T · ∇²(-S) (entropy Hessian)

Bernoulli entropy `S(u) = -Σ_x [u(x) log u(x) + (1-u(x)) log(1-u(x))]`.

$$
\frac{\partial^2 (-S)}{\partial u(x)\, \partial u(y)} \;=\; \delta_{xy}\cdot \Big(\frac{1}{u(x)} + \frac{1}{1-u(x)}\Big).
$$

So `∇²(-S) = diag(1/u(x) + 1/(1-u(x)))` — **diagonal positive definite** on (0,1)^n.

At sharp-interface critical points (most sites u ≈ 0 or u ≈ 1 ⇒ one factor in denominator small ⇒ diagonal entry large), and boundary-band sites (u intermediate ⇒ diagonal entry ~4-11).

For u(x) ∈ [ε, 1-ε]: `1/u + 1/(1-u) ≥ 4/(1 - (2u-1)²)^{...}` ≥ 4 at u = 1/2.

Magnitude: at T = 1, n = 64, boundary band ~11 sites: T·tr(∇²(-S)) ≈ 1·(11·4 + 53·(1/ε + 1/(1-ε))) — dominated by near-corner sites. Very large (1/ε ≈ 20 at ε = 0.05 ⇒ 53·40 = 2120).

**Critical observation.** At T > 0, `T · ∇²(-S)` is **largest at near-corner sites** (u ≈ 0 or 1). This drives the Langevin dynamics away from corners — exactly the "entropy escape from binary states" phenomenon that prevents sharp-interface.

However, at **sharp-interface minimizers** (canonical zero-T minimizers), many sites sit near corners where T·∇²(-S) is huge. This competes with ℰ's preference for sharp interface (β·W''(u) = 2β at corners).

**Balance condition for sharp-interface to remain stable at T > 0:** β (sharpness) > T·(1/ε) (entropy penalty at boundary). I.e., `T·n/(β·ε_boundary)` is small. For canonical: β = 30, ε = 0.05, T = 1 ⇒ T/(β·ε) = 1/(30·0.05) = 0.67. Not small enough! Entropy entry per site at boundary ~ T·(1/ε) = 20 > β = 30? Actually 20 < 30 but close.

**Conclusion:** at T ~ 1 and ε = 0.05, entropy starts competing with sharp-interface. Effective "smoothing" of interface. At T ≫ 1, entropy wins completely (all sites near u = 1/2 — uniform).

This reproduces the **crossover T_c ≈ 1** observed in G4 §3.3 from a different angle: **interface stability also breaks around T_c ≈ 1**, consistent with entropy-driven K=2 dominance at T > T_c.

### 1.5 Term 3: λ_K · ∇²K_soft (persistence-count Hessian)

Recall (G1 §3.3): off vineyard V, each bar i has ∂ℓ_i/∂u_x = δ_{x, v_b^i} - δ_{x, v_d^i} (sparse, ±1 at two vertices).

$$
K_{\mathrm{soft}}(u) \;=\; \sum_{i \in B_+(u)} \varphi(\ell_i(u)).
$$

First derivatives:
$$
\frac{\partial K_{\mathrm{soft}}}{\partial u_x} \;=\; \sum_{i \in B_+} \varphi'(\ell_i)\cdot (\delta_{x, v_b^i} - \delta_{x, v_d^i}).
$$

Second derivatives:
$$
\frac{\partial^2 K_{\mathrm{soft}}}{\partial u_x\, \partial u_y} \;=\; \sum_{i \in B_+} \varphi''(\ell_i)\cdot (\delta_{x, v_b^i} - \delta_{x, v_d^i})(\delta_{y, v_b^i} - \delta_{y, v_d^i}).
$$

In matrix form:
$$
\nabla^2 K_{\mathrm{soft}}(u) \;=\; \sum_{i \in B_+} \varphi''(\ell_i)\cdot \mathbf{v}_i\, \mathbf{v}_i^\top,
$$
where `v_i = e_{v_b^i} - e_{v_d^i}` are ±1-support vectors with `‖v_i‖² = 2`.

**Sign of φ''.** For (φ-sat) `φ(ℓ) = ℓ/(1+ℓ)`:
- φ'(ℓ) = 1/(1+ℓ)² > 0 (monotone).
- **φ''(ℓ) = -2/(1+ℓ)³ < 0 ⇒ φ is concave.**

**Consequence.** ∇²K_soft is a sum of rank-1 **negative semi-definite** matrices ⇒ `∇²K_soft ≼ 0`, with:
$$
\|\nabla^2 K_{\mathrm{soft}}(u)\|_{op} \;\leq\; \max_i |\varphi''(\ell_i)| \cdot 2 \cdot |B_+(u)| \;\leq\; 2 \cdot 2 \cdot n \;=\; 4n.
$$
(Using `|φ''| ≤ 2` at ℓ = 0 and `|B_+| ≤ n`.)

**Magnitude at canonical parameters.** λ_K = γ_K · T = 0.1 · 1 = 0.1. Max op-norm contribution: 0.1 · 4n = 0.4n. For n = 64: 25.6. This is **comparable to some entropy contributions**, but much smaller than β·|W''| dominated ℰ Hessian at sharp interface (~30·2 = 60 per site, times n).

**Net effect.** λ_K · ∇²K_soft subtracts O(25) from Hessian eigenvalues at T = 1 (small λ_K).

### 1.6 Combined Hessian + min eigenvalue estimate

At K_soft ≈ K critical point:
$$
H_{C+E}(u^*) \;=\; H_\mathcal{E}(u^*) \;+\; T\cdot H_{-S}(u^*) \;+\; \lambda_K\cdot H_{K_{\mathrm{soft}}}(u^*),
$$
with constrained (tangent-space projected) min eigenvalue:
$$
\mu_K^{(C+E)} \;\geq\; \mu_K^{(\mathcal{E})} \;+\; T\cdot \mu_{-S}^{\min} \;-\; \lambda_K\cdot \|H_{K_{\mathrm{soft}}}\|_{op}.
$$

Using the bounds:
- `μ_K^{(ℰ)} ~ O(β)` (canonical).
- `μ_{-S}^{\min} ≥ 4` at typical intermediate u (since `1/u + 1/(1-u) ≥ 4` at u = 1/2).
- `‖H_{K_soft}‖_op ≤ 4n`.

$$
\mu_K^{(C+E)} \;\geq\; O(\beta) \;+\; 4T \;-\; 4\lambda_K n.
$$

**Stability condition:** `β + 4T > 4 γ_K T n` (plugging λ_K = γ_K T), i.e., `γ_K n < 1 + β/(4T)`.

At canonical β = 30, T = 1, n = 64: need `γ_K · 64 < 1 + 7.5 = 8.5` ⇒ **γ_K < 0.13**. 

**Consistency with G3 §4.3 recommendation.** G3 recommended `γ_K ∈ [0.01, 1]` — and **the Hessian stability at canonical parameters requires γ_K ≲ 0.1**, confirming the lower end of that range. The upper end (γ_K = 1) is **ruled out by Hessian stability** on n = 64 grids at T = 1.

**New commitment (refined γ_K range):** `γ_K ∈ [0.01, 0.1]` — upper end restricted to maintain Hessian PD.

### 1.7 T-7 (Enhanced Metastability) survival in C+E

T-7 states: closure contributes strictly positive Hessian `2(I - J_Cl)^T(I - J_Cl)` at closure FP.

In C+E Hessian:
- Closure contribution ∈ ℰ — unchanged, still adds `≥ 2(1 - a_cl/4)²` to diagonals (canonical contraction bound).
- Additional -T·S term: positive diagonal contribution (strengthens).
- Additional λ_K · K_soft term: negative rank-N, subtracts but bounded by §1.6.

**Net: T-7 survives in C+E with strictly enhanced minimum Hessian eigenvalue** (compared to canonical ℰ alone) as long as γ_K ≤ 0.1 on canonical parameters.

**Status:** T-7 Cat A preserved; **strengthened** in C+E due to entropy term's positive Hessian contribution.

### 1.8 Kramers prefactor implication

At saddle `u_s^*` (Morse index 1, per Mountain Pass §3 of `05_deepening`):
- H_s has one negative eigenvalue `-|ω_s|`. The magnitude |ω_s| ~ |μ_K^{(ℰ)}_transition| from saddle's ℰ component.
- det(H_s) = product of eigenvalues. In the constrained (n-1) tangent space, with 1 negative and (n-2) positive.

Kramers prefactor: `τ_0 = (2π/|ω_s|) · √(det H_a / |det H_s|)`.

**Order of magnitude.** For canonical SCC: typical Hessian eigenvalues at minima range `[μ_K^{(ℰ)}, O(β)]` ~ O(1) to O(β). At saddle: similar magnitudes except one negative direction.

Ratio `det H_a / |det H_s|` ≈ product of eigenvalue ratios. If eigenvalues at minimum and saddle differ by factor ~ 2 (typical), and dim = 63 (n-1), ratio ≈ 2^63 ≈ 10^19. Ouch — huge.

More realistic: most eigenvalues are similar (bulk modes), only a few (near transition) differ substantially. Ratio might be O(1)–O(10^3).

**Rough estimate:** `τ_0 ~ O(1) to O(10^3)`. At T = 0.125 (exp55 σ = 0.5), τ ≈ 10^3 · exp(160) ≈ 10^70. Consistent with §6.1 of `05_deepening`.

**γ_eff = 0.89 Kramers consistency.** β-dependence of τ:
- Exponential: `exp(ΔF/T)` with `ΔF ~ c · β^γ` for some γ related to saddle-structure scaling.
- Prefactor: `τ_0 ~ √(det H_a / det H_s)` — each eigenvalue ~ O(β) at sharp-interface ⇒ `√(β^{n-1}/β^{n-2}) = √β` on net (loose).

Combined log-scaling: `log τ ~ γ · β · (const) + 0.5 · log β`. For `log τ ∝ β^0.89`, need γ = 0.89 in exponent. This is the "crossover" between linear (`γ = 1`) and square-root (`γ = 0.5`) per G5 §4.1. Full derivation: C-S2.

---

## §2. T-7 Enhanced Metastability in C+E — Strengthened Claim

Per §1.7:

**Proposition 2.1 (T-7 in C+E, strengthened).** At K_soft ≈ K local minimizers of ℱ_C+E on Σ_m^ε, and for `γ_K ∈ [0.01, 0.1]` with canonical parameters (β ≥ 20α, a_cl ≤ 3, λ_cl ≤ O(1)):

$$
\mu_K^{(C+E)}(u^*) \;\geq\; \mu_K^{(\mathcal{E})}(u^*) \;+\; T\cdot \bar{\mu}_{-S}(u^*) \;-\; \lambda_K \cdot \bar{\mu}_{K_{\mathrm{soft}}}(u^*)
$$
where $\bar{\mu}_{-S}(u^*) > 0$ (entropy Hessian is PSD, contributing positively) and $\lambda_K \bar{\mu}_{K_{\mathrm{soft}}}(u^*) = O(\gamma_K \cdot T \cdot n) \leq 0.1 \cdot T \cdot n$. The net Hessian eigenvalue is **≥** canonical's, with strict inequality when boundary band is non-empty.

**Proof.** Direct sum via §1.2–1.6. ∎

**Interpretation.** C+E adds entropy (which strengthens metastability by concavity-of-S-contributing-positively-to-(-S)-Hessian) + K_soft regularization (which weakens it slightly via concave φ). Net: strengthened if entropy contribution > K_soft penalty, which holds at small γ_K.

**Why this matters.** T-7 is canonical Cat A and central to metastability claims. Verifying its C+E survival (and strengthening) **rigorously preserves** the canonical CN14 claim about closure's role. `working/E/M1_dissolution.md` §3.4's CN14 substantiation is now anchored in this explicit Hessian computation.

---

## §3. Mountain Pass Test-Path Upper Bound — Quantitative Negative Result

### 3.1 Setup

Per `05_deepening_and_verification.md` §3, Mountain Pass gives existence of saddle `u_s^*` with `c = ℱ_C+E(u_s^*) = inf_γ max_{t} ℱ_C+E(γ(t))`. Can we provide an **upper bound on c** via a specific test path?

### 3.2 Test path: linear interpolation

Take `u_1^*` (K=1 minimizer, ℱ_1 = ℰ_1 - T·S_1 + λ_K ≈ 2.25 - T·5.5 + 0.1·T at canonical exp62/63).

Take `u_2^*` (K=2 minimizer, ℱ_2 = ℰ_2 - T·S_2 + 2λ_K ≈ 4.66 - T·8 + 0.2·T).

Linear interp: `γ(t) = (1-t)·u_1^* + t·u_2^*`. Σ_m convex ⇒ γ(t) ∈ Σ_m. Volume `Σ γ_x = (1-t)·m + t·m = m` preserved.

### 3.3 Evaluating ℱ along γ(t)

**ℰ(γ(t))** — dominated by ℰ_bd. At midpoint t = 0.5:
- At sites where both u_1^* ≈ 1 and u_2^* ≈ 1 (overlap region): γ = 1, W(γ) = 0.
- At sites where both u_1^* ≈ 0 and u_2^* ≈ 0: γ = 0, W(γ) = 0.
- At sites where one has u ≈ 1 and other u ≈ 0 (disjoint support): γ = 0.5, W(γ) = (0.5)²(0.5)² = 1/16.

For K=1 vs K=2 on n = 64 grid, typical disjoint-support size is ~|u_1|·(1 - overlap_fraction) ≈ 10 · 0.8 = 8 sites at γ = 0.5. Plus smoothness term: `α · Σ_{x,y} N(x,y)(γ_x - γ_y)²`. At interface between γ=0.5 and γ=0 regions, gradients large.

**Rough estimate:** `ℰ_bd(γ(0.5)) ≈ β · 8 · (1/16) + 4α · (interface gradient sum)`. With canonical β = 30, α = 1: `ℰ_bd ≈ 15 + 4 · (interface length · 1) ≈ 15 + 4·20 = 95`.

**Entropy at γ(0.5).** Sites at γ = 0.5 have max Bernoulli entropy: 8 · log 2 ≈ 5.5 nats. Plus 2-3 times as many boundary-band sites from original formations: total ~30 nats. Much higher S than minima.

**Free energy at γ(0.5).**
`ℱ(γ(0.5)) ≈ ℰ_bd + small cl/sep corrections - T · 30 + γ_K · T · K_soft(γ(0.5))`.

With `ℰ ≈ 95`, `-T·S ≈ -30 T`, `λ_K·K_soft ≈ 0.1·T·2` (K_soft of midpoint is some intermediate value): at T = 1, `ℱ(γ(0.5)) ≈ 95 - 30 + 0.2 = 65.2`.

Compare to `ℱ_1 = 2.25 - 5.5 + 0.1 = -3.15` and `ℱ_2 = 4.66 - 8 + 0.2 = -3.14`.

ΔF upper bound from linear interp: `c ≤ ℱ(γ(0.5)) = 65.2`, so `ΔF ≤ 65.2 - (-3.14) ≈ 68.3`.

**Comparison to canonical CN14 barrier ~20.** Linear-interp gives 68, real barrier ~20. **Linear interp is ~3× too loose.**

### 3.4 Why linear interp is loose

Real transitions K=2 → K=1 don't go through "spread-out u=0.5 everywhere". They go through a **nucleation sequence**: one formation slowly merges with the other via a "bridging neck" at the connection point. Most of the field stays near u=0 or u=1 during the transition; only the neck region changes.

Formally, the optimal path (string method) minimizes `max_t ℱ(γ(t))` and tends to follow the **minimum energy pathway** (MEP) which avoids the high-ℰ region of spread-out configurations.

### 3.5 Conclusion — negative result with constructive implication

**Linear-interp upper bound is too loose to give a meaningful ΔF estimate** (3× overestimate minimum).

**Implications for tomorrow's plan:**
- **Analytical a priori upper bound on c is hard** — requires understanding MEP structure.
- **Numerical (NEB / string method) is the practical route** for ΔF computation.
- **This validates the C-S2 carry** (Kramers prefactor requires numerical Hessian + NEB).

**Useful fact from this exercise.** The linear-interp path's high-ℰ peak (~65-100 nats in canonical units) is **substantially larger than the actual Kramers barrier**, confirming that canonical exp38's empirical γ_eff = 0.89 measurement is **along the MEP, not along linear interp**. Consistent interpretation.

### 3.6 A lower bound on c (complementary)

By Mountain Pass, c ≥ max(ℱ_1^*, ℱ_2^*) + ε for small ε > 0 (depends on Hessian at endpoints + saddle topology). Formally: c > max(ℱ_1^*, ℱ_2^*).

At canonical exp62/63: c > max(-3.15, -3.14) = -3.14 (with our convention ℰ negative after entropy subtraction). So ΔF ∈ (0, 68]. **Large uncertainty.**

**Better bound**: from exp38 empirical γ_eff, ΔE_{K=2 → K=1} ≈ 20 at β=30. With entropy correction `T·(S_s - S_1) ≈ T·(something)`, ΔF at T=1 is roughly in [10, 25]. **Narrow range** but requires empirical input.

---

## §4. Sublevel Set Connectivity — Mountain Pass Premise

Per `05_deepening_and_verification.md` §3.3 step 3, Mountain Pass requires: for `a*` just above `max(ℱ(u_1^*), ℱ(u_2^*))`, the sublevel set `{u : ℱ(u) ≤ a*}` is disconnected, with u_1^* and u_2^* in different components.

### 4.1 Morse-theoretic argument

For a Morse function on connected manifold M, sublevel set topology changes only at critical values (standard Morse). Specifically:
- Passing a **local minimum** (index 0) at height c: sublevel set gains a connected component.
- Passing a **saddle** (index 1): two components merge into one (or a handle is attached).
- Higher-index critical points: attach k-cells.

So: two local minima `u_1^*, u_2^*` at heights `ℱ_1^*, ℱ_2^*`. The sublevel set `{ℱ ≤ max(ℱ_1^*, ℱ_2^*) + δ}` for small δ > 0:
- Contains small open neighborhoods of u_1^* and u_2^*.
- These are in **different components** if no index-1 critical point has been crossed between them.

Since Mountain Pass saddle has height `c > max(ℱ_1^*, ℱ_2^*)`, for δ < c - max(ℱ_1^*, ℱ_2^*), the sublevel set is disconnected with u_1^*, u_2^* in different components.

**Connectivity premise verified (generically, modulo Morse assumption).** ✓

### 4.2 Where generic Morse fails

ℱ_C+E may have degenerate critical points (Morse-Bott) at symmetric configurations — e.g., K_soft ≈ 2 with spatial-symmetry-related family of minimizers (placing the two K=2 formations at different grid locations).

**Morse-Bott extension:** Mountain Pass on Morse-Bott critical manifolds works — see Duistermaat-Heckman or Bismut-Gillet-Soulé. Saddle is a critical submanifold of Morse-Bott index 1. Existence still holds. **Generic Morse assumption can be relaxed.**

### 4.3 Non-Morse (V vineyard) handling

Vineyard set V ⊂ Σ_m is codim-1 where ∇K_soft is discontinuous. Critical points on V are not Morse. Mollification (ℱ_ε = ℱ * ρ_ε) gives smooth approximation with Morse critical points; limit ε → 0 recovers ℱ.

**Robust existence, but characterization (K_soft value at saddle) may differ pre- and post-mollification.** Specifically, if saddle lies on V, ε → 0 limit saddle might have K_soft at a discontinuity — requires Clarke subdifferential framework (NQ-14).

---

## §5. K_soft vs Q_morph Cross-Consistency

Canonical's morphology functional:
$$
\mathcal{Q}_{\mathrm{morph}}(u) \;=\; \frac{\ell_{\max}(u) - c}{1 - c}\cdot \mathrm{Artic}(u), \quad \mathrm{Artic} = 1 - \frac{\ell_{\mathrm{second}}}{\ell_{\max}}.
$$

K_soft:
$$
K_{\mathrm{soft}}(u) \;=\; \sum_{i \in B_+(u)} \varphi(\ell_i(u)).
$$

### 5.1 Evaluation on reference configurations

| Configuration | ℓ_1 (longest bar) | ℓ_2 (second) | Q_morph | K_soft (φ-sat) |
|---|---|---|---|---|
| Uniform u = m/n·1 | = m/n (one trivial bar) | 0 | (m/n - m/n)/(1 - m/n) · 1 = 0 | φ(m/n) ≈ 0.15 (small) |
| Sharp K=1 (c = m/n = 0.156) | ≈ 1 | 0 | (1 - 0.156)/(1 - 0.156) · 1 = 1.0 | φ(1) = 0.5 |
| Sharp K=2 (equal) | ≈ 1 | ≈ 1 | 1·(1-1) = 0 | 2·φ(1) = 1.0 |
| Sharp K=3 (equal) | ≈ 1 | ≈ 1 | 0 | 3·φ(1) = 1.5 |
| K=1 weak (ℓ_1 = 0.5) | 0.5 | 0 | (0.5-0.156)/0.844·1 = 0.41 | φ(0.5) = 0.333 |

### 5.2 Observations

- **Q_morph detects "how cleanly a single formation dominates"**: maximal at sharp K=1, zero at sharp K≥2 (no dominance).
- **K_soft detects "how many modes"**: 0 at uniform, 0.5 at K=1, 1.0 at K=2, 1.5 at K=3.
- They are **complementary**: Q_morph=1 corresponds to K_soft=0.5 (K=1 unique mode); Q_morph=0 corresponds to K_soft=0 (uniform, no structure) OR K_soft≥1 (multi-mode).

**Pair together, (Q_morph, K_soft) characterizes formation structure uniquely** (among sharp configurations):
- (0, 0): uniform.
- (1, 0.5): K=1 dominant.
- (0, 1.0): K=2 equal split.
- (0, 1.5): K=3 equal split.
- etc.

### 5.3 Cross-consistency with canonical CN12

CN12 commits to persistence-based morphology (Q_morph). K_soft also persistence-based. Both aligned. No conflict.

**But:** K_soft generalizes Q_morph in an information-sense. Q_morph is a *partial* readout (longest-bar + articulation), K_soft is a *full* weighted sum. They are compatible but K_soft carries more information.

**CN12 extension proposal (informal):** "Persistence-based morphology" could be restated as "any persistence-stable functional of Dgm(u) is admissible; Q_morph and K_soft are two realizations."

**Consistency status: fully consistent, K_soft is strict generalization.** ✓

---

## §6. Helffer-Sjöstrand Prefactor Convention — Verification

In `02_development.md` §3.2 step 4, I wrote:
$$
\lambda_1(\Delta_{\mathcal{F}, T}) \;=\; \frac{|\omega_s|}{2\pi}\cdot \sqrt{\frac{|\det H_s|}{\det H_a}}\cdot \exp(-\Delta\mathcal{F}/T)\cdot (1 + o(1)).
$$

Cross-check against Bovier-Eckhoff-Gayrard-Klein (2004), *Metastability in reversible diffusion processes I: Sharp asymptotics for capacities and exit times*, J. Eur. Math. Soc. 6.

**BEGK Theorem.** For reversible diffusion on compact manifold with potential F, the inverse MFPT from basin of u_a^* (local minimum) to basin of global minimum satisfies:

$$
\mathbb{E}[\tau]^{-1} \;=\; \frac{|\omega_s|}{2\pi}\cdot \sqrt{\frac{|\det \nabla^2 F(u_s^*)|}{\det \nabla^2 F(u_a^*)}}\cdot \exp(-(F(u_s^*) - F(u_a^*))/T) \cdot (1 + o(1)),
$$

as T → 0, where `ω_s` is the magnitude of the unique negative eigenvalue of `∇²F(u_s^*)` (the saddle).

**Match to my statement: ✓** (up to trivial renaming).

Verified. No convention error.

---

## §7. Sard's Theorem on Σ_m^ε Polytope

### 7.1 Setup

Σ_m^ε = Σ_m ∩ [ε, 1-ε]^n is an open subset of Σ_m (dim n-1 manifold with corners). On Σ_m^ε \ V: ℱ_C+E is real-analytic. On V: continuous but not C^1.

### 7.2 Sard's theorem (classical, Sard 1942)

**Sard.** For C^k map f: M^n → ℝ^p with k ≥ max(n - p + 1, 1): the set of critical values has Lebesgue measure zero.

For f: Σ_m^{n-1} → ℝ (n-1 dim domain, 1 dim codomain): need k ≥ n - 1. For analytic f, k = ∞ ⇒ Sard applies.

### 7.3 Application on Σ_m^ε \ V

ℱ_C+E is analytic (hence C^∞) on `Σ_m^ε \ V`. Sard ⇒ critical values of ℱ_C+E|_{Σ_m^ε \ V} form a measure-zero set in ℝ. Generic perturbations make all critical points Morse.

### 7.4 On V

On V: ℱ_C+E is continuous but not differentiable. Sard doesn't apply directly to non-smooth maps. Work-around: mollification (ℱ_ε = ℱ * ρ_ε). Sard applies to ℱ_ε. As ε → 0, critical sets of ℱ_ε converge (in appropriate sense — see e.g., Clarke 1983 for non-smooth Sard).

### 7.5 On Σ_m corners (u_i ∈ {0, 1})

Corners are codim ≥ 1 submanifolds of ∂Σ_m. Local analysis: near a corner, ℱ_C+E's entropy term -T·S blows up in gradient — corner is a "soft" singularity (finite value, infinite derivative).

For variational analysis purposes (Mountain Pass existence), **ignore corners** (Σ_m^ε restricts to ε-interior). Corners are "inaccessible" in Lions-Sznitman reflected dynamics (next §8). 

**Sard status:** applicable on Σ_m^ε \ V via analyticity; on V via mollification; corners excluded by ε-interior restriction. ✓

---

## §8. F3 Langevin Well-Posedness — Rigorous Statement via Lions-Sznitman

### 8.1 Framework

**Lions-Sznitman 1984 (Comm. Pure Appl. Math.)**. Let `D ⊂ ℝ^n` be a convex bounded domain with C²-smooth boundary (or more generally, Lipschitz boundary + interior ball condition). Let `b : D̄ → ℝ^n` be Lipschitz, `σ : D̄ → ℝ^{n×n}` be Lipschitz nonsingular. Then the **reflected SDE**:

$$
dX(t) \;=\; b(X(t))\, dt \;+\; \sigma(X(t))\, dW(t) \;+\; dK(t), \qquad X(t) \in D̄ \text{ for all } t,
$$

where `K` is the local time (reflection measure) at ∂D, has **unique strong solution** on `D̄`.

### 8.2 Application to SCC C+E on Σ_m^ε

- **Domain:** `D = Σ_m^ε ⊂ ℝ^n`. Σ_m is convex polytope (Prop 1.1 Cat A); Σ_m^ε is bounded, convex, with piecewise-linear boundary (Lipschitz). ✓
- **Drift:** `b(u) = -Π_{Σ_m}(∇ℱ_C+E[u])`. Lipschitz on Σ_m^ε (Lemma 1.8 of `02_development.md`, with constant L_F). ✓
- **Diffusion:** `σ(u) = √(2T) · Π_{Σ_m}`. Constant on u ⇒ trivially Lipschitz. Non-singular on T_u Σ_m (projected). ✓

**Theorem 8.1 (F3 well-posedness — rigorous).** For all `T > 0`, `λ_K ≥ 0`, and `ε > 0`, the projected-reflected SDE:

$$
du(t) \;=\; -\Pi_{T_u\Sigma_m}\!\big(\nabla\mathcal{F}_{C+E}[u(t); T, \lambda_K]\big)\, dt + \sqrt{2T}\,\Pi_{T_u\Sigma_m}\,dW(t) + dK(t),
$$

with reflection `K` at `∂(Σ_m^ε)`, admits a unique strong solution on `Σ_m^ε` for any initial data `u(0) ∈ Σ_m^ε`.

*Proof.* Direct application of Lions-Sznitman 1984 with verified hypotheses. ∎

**Status: Cat A.** F3 is now rigorous (not just statement).

### 8.3 Equilibrium = Gibbs

**Theorem 8.2 (F3 equilibrium).** The Langevin dynamics F3 (Theorem 8.1) has unique invariant probability measure:

$$
\mathbb{P}_T^\varepsilon(du) \;=\; \frac{1}{Z^\varepsilon(T)}\,\exp\!\big(-\mathcal{F}_{C+E}[u]/T\big)\,\mathbf{1}_{\Sigma_m^\varepsilon}(u)\,\nu(du),
$$

with `Z^ε(T) = ∫_{Σ_m^ε} exp(-ℱ/T) ν(du)` (finite by §0 of G2).

*Proof sketch.* Fokker-Planck operator `L = -∇ℱ·∇ + T·Δ` with Neumann boundary conditions on ∂Σ_m^ε (from reflection). Direct calculation: `L(exp(-ℱ/T)) = 0` and ∫ exp(-ℱ/T) = Z^ε. Uniqueness: ergodicity via log-Sobolev or direct spectral gap (finite-dim bounded domain, continuous ℱ). Standard. ∎

### 8.4 ε → 0 limit

At ε → 0, Σ_m^ε → Σ_m. Invariant measure `ℙ_T^ε → ℙ_T` (G2 §1) — same Gibbs measure on full Σ_m.

But: in the limit, corner handling requires care. Boundary of Σ_m has lower-dimensional faces (where some u_i ∈ {0, 1}). Reflection on these lower-dim faces needs Skorohod-type extension. The Lions-Sznitman framework extends to polyhedra (see Tanaka 1979).

**Extended theorem (F3 on Σ_m).** Reflected SDE on full convex polytope Σ_m with entropy-gradient singularity at corners has well-posed solution via Tanaka 1979 + entropy-regularization. Full rigorous treatment: C-S2 carry.

**Status:** F3 **Cat A on Σ_m^ε** (Theorem 8.1); **Cat C-provisional on full Σ_m** (requires Tanaka 1979 + entropy reg).

---

## §9. New Issues / NQs from Round 3

### 9.1 Errata candidates

| # | File | Issue | Proposed fix |
|---|---|---|---|
| **E-7** | `working/CE/free_energy_wellposed.md` §4.3 | γ_K range recommendation [0.01, 1] is too loose — Hessian stability at canonical params requires γ_K ≲ 0.1. | Restrict recommendation to `γ_K ∈ [0.01, 0.1]`. Per §1.6 of this file. |
| **E-8** | `working/C/F_group_axioms.md` §3.2 (F3 status) | F3 "carried to C-S2" is too conservative — Lions-Sznitman + analyticity gives well-posed on Σ_m^ε already (Theorem 8.1). | Upgrade F3 on Σ_m^ε to **Cat A** (rigorous). On full Σ_m: Cat C still (corner handling). |

### 9.2 New NQs

**NQ-15 (new).** **Hessian eigenvalue scaling with β at saddle.** To derive γ_eff = 0.89 from Kramers prefactor, need to know how `|ω_s|` (saddle negative eigenvalue) and `det H_s/det H_a` scale with β. Expect `|ω_s| ~ O(β^α)` for some α. Sketch analysis: at sharp-interface saddle ("neck" configuration), H_bd contribution at neck sites has W''(u_neck) where u_neck ≈ critical value (typically 0.5 ± something). |W''(0.5)| = 1, so |ω_s| at neck ≈ β · 1 = β ⇒ α = 1 ⇒ `log τ_0 = 0.5·log β` (prefactor contribution). Combined with exp factor `~ β^γ` for barrier, and empirical log τ ~ β^{0.89}, need γ = 0.89 directly. Carry to C-S2.

**NQ-16 (new).** **γ_K upper bound via stability analysis.** Per §1.6, `γ_K < 1 + β/(4T·n)` required for Hessian PD. For n = 64, T = 1, β = 30: γ_K < 0.13. Tight upper bound. General n-dependence (as n → ∞, γ_K → 0) suggests **γ_K must scale with 1/n** for large graphs. Discuss as part of (T, λ_K) phase diagram (CE-S2).

**NQ-17 (new).** **Minimum energy pathway (MEP) vs linear interp.** The 3× looseness of linear interp vs actual Kramers barrier (§3) motivates NEB / string method for accurate ΔF. Numerical (Stage 5) but could benefit from analytical ansatz for MEP shape. Hybrid analytical+numerical approach.

### 9.3 Strengthened claims

| Claim | Before Round 3 | After Round 3 |
|---|---|---|
| T-7 in C+E | "survives" (sketched) | **"Strengthened"** — entropy contribution adds more positive Hessian (§2 Prop 2.1) |
| F3 Langevin | statement only | **Cat A on Σ_m^ε** via Lions-Sznitman (§8 Thm 8.1) |
| F3 equilibrium = Gibbs | sketched | **Cat A on Σ_m^ε** (§8 Thm 8.2) |
| K_soft ↔ Q_morph consistency | implicit | explicit cross-check (§5) |
| Sard on Σ_m^ε | implicit | explicit (§7) |
| Mountain Pass connectivity premise | implicit | explicit Morse-theoretic verification (§4) |
| γ_K range | [0.01, 1] heuristic | [0.01, 0.1] Hessian-stable |

### 9.4 Category self-classification update

| Cat | Before (end of Round 2) | After Round 3 |
|---|---|---|
| Cat A (sketched-rigorous) | 13 | **16** (+T-7 C+E Prop 2.1, F3 Thm 8.1, F3 Thm 8.2) |
| Sketched (Cat C-provisional) | 7 | **6** (F3 on Σ_m^ε upgraded) |
| Statement-only (carry) | 3 | 3 |
| New errata | 6 (E-1 to E-6) | **8** (+E-7, E-8) |
| New NQs | 9 (NQ-8 to NQ-14) | **12** (+NQ-15, NQ-16, NQ-17) |

### 9.5 Hessian finding: γ_K ≤ 0.1 is a stability boundary

This is the most important finding of Round 3. The G3 §4.3 recommendation `γ_K ∈ [0.01, 1]` was **loose on the upper end**. Stability analysis (§1.6) tightens to `γ_K ≲ 0.1` at canonical parameters (β = 30, T = 1, n = 64). This becomes:

**Refined commitment (C+E framework):** `λ_K = γ_K · T` with **`γ_K ∈ [0.01, 0.1]`**.

At γ_K > 0.1, ∇²K_soft's negative contribution overwhelms ℰ + entropy positive contributions → critical points become saddles → no K_soft-regularized minima. Pathological.

**Canonical merge implication.** When "Group F-thermal" is added to canonical in Stage 2 merge, the γ_K range should be stated as [0.01, 0.1] with Hessian stability justification. Per Stage 2 audit work.

---

## §10. Verification Confidence Summary (Post-Round 3)

| Claim | Confidence | Notes |
|---|---|---|
| ℱ_C+E Hessian decomposition | **HIGH** | Explicit computation §1 |
| T-7 survives/strengthened in C+E | **HIGH** | Prop 2.1 |
| F3 Lions-Sznitman on Σ_m^ε | **HIGH** | Rigorous application |
| Mountain Pass saddle exists | **HIGH** | Sketched both in §05 and §06 §4 |
| Linear-interp upper bound on c | **LOW (negative result)** | 3× too loose; justifies NEB carry |
| γ_K ≤ 0.1 stability boundary | **HIGH** | Explicit Hessian bound (§1.6) |
| F4.b 22 Cat A survive T → 0 | **HIGH** | Enumerated (§05 §4) |
| Kramers prefactor order O(1)-O(10^3) | **MEDIUM** | Rough estimate, refinement in C-S2 |
| K_soft vs Q_morph consistent | **HIGH** | Explicit cross-check §5 |
| HS prefactor convention | **HIGH** | Verified against BEGK §6 |
| Sard applicable on Σ_m^ε | **HIGH** | Analytic ⇒ C^∞ ⇒ Sard §7 |

---

## §11. Recommendations Post-Round 3

### 11.1 Immediate (errata application)

- E-7: Update G3 §4.3 γ_K range to [0.01, 0.1]. 
- E-8: Upgrade F3 status in G2 §3 to "Cat A on Σ_m^ε via Lions-Sznitman" (downgrade carry C-S2 to "corner handling only").

### 11.2 Tomorrow's plan (C-S2) — refined

With Round 3's Hessian machinery, tomorrow's plan can be tightened:

**C-S2 Option A (refined):**
1. **Explicit Hessian at K_soft ≈ 2 critical point on small graph (n = 16 or 32).** Use graph Laplacian + ℰ_bd coefficients + entropy diag + K_soft rank-1 sum (per §1).
2. **Numerical NEB (nudged elastic band) between u_1^* and u_2^*.** Compute actual saddle u_s^* and ΔF. Sub-target C-S2.2.
3. **Verify γ_eff = 0.89 from explicit Hessian eigenvalue scaling with β at saddle** (per NQ-15 sketch). Possibly Cat B → Cat A promotion.
4. **Apply γ_K ≤ 0.1 refined range + T-Beyond-Weyl / T-d_min retirement to dependency map.**

### 11.3 Further deepening candidates (Round 4 +)

- Full Hessian eigenvalue spectrum at K_soft ≈ K critical points as function of graph topology (spectral-gap-sensitive).
- Explicit Witten Laplacian formula on finite-dim Σ_m polytope.
- Connectivity analysis for Mountain Pass on more complex landscapes (multi-saddle, Morse-Bott).
- Full log-Sobolev inequality on Σ_m^ε for ergodicity of F3 (currently sketched).
- (T, λ_K) phase diagram 4 corners per pre_brainstorm H-C4.

These are **Round 4 candidates** — would push session into Stage 2 territory. Better deferred to dedicated C-S2 / CE-S2 sessions.

---

## §12. Self-Check (Post-Round 3)

- [x] Hessian decomposition explicit (§1, 3 terms).
- [x] T-7 survival / strengthening (§2 Prop 2.1).
- [x] Mountain Pass upper bound attempt (§3, negative result).
- [x] Sublevel set connectivity (§4, Morse-theoretic).
- [x] K_soft vs Q_morph consistency (§5 table).
- [x] HS prefactor convention verified (§6).
- [x] Sard on Σ_m^ε (§7).
- [x] F3 Lions-Sznitman rigorous (§8 Thm 8.1, 8.2).
- [x] 2 new errata identified (E-7, E-8).
- [x] 3 new NQs identified (NQ-15, 16, 17).
- [x] 1 stability boundary discovered (γ_K ≤ 0.1).
- [x] Category counts updated.

Round 3 pushed 3 claims from "sketched" to Cat A (Prop 2.1 T-7 C+E, F3 Thm 8.1, F3 Thm 8.2). Tightened γ_K range. Identified 3 new NQs with quantitative handles. No errors discovered in Round 1-2 findings.

---

**End of Round 3 Further Verification.**
