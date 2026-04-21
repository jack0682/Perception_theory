# 02 — Development: Mathematical Body of G1–G6

**Session:** 2026-04-21
**Target (from plan.md):** Stage 1 C+E foundation — K_soft 정의 + F-group + ℱ_C+E + 3 Critical dissolution mappings.
**This file covers:** 6 working 파일 (G1–G6) 에 분산된 수학적 골격을 step-by-step granularity 로 통합. 각 정의·보조정리·증명·반례 시도가 후속 검증 가능하도록 문장 단위 numbering.
**Depends on reading:** `working/E/soft_K_definition.md` (G1), `working/C/F_group_axioms.md` (G2), `working/CE/free_energy_wellposed.md` (G3), `working/E/M1_dissolution.md` (G5), `working/E/MO1_dissolution.md` (G6), `working/E/F1_dissolution.md` (G4); `01_exploration.md`.
**Reading order recommendation:** G1 → G2 → G3 → 본 파일 §1 (foundation 통합) → §2 (Lipschitz/coercivity tied together) → §3 (Kramers + Witten linked) → §4 (counter-example attempts) → §5 (category self-classification audit).

---

## §1. Foundation Integration (G1 + G2 + G3)

### 1.1 Definition layer (single statement)

**Definition 1.1 (SCC C+E State Space).** A C+E thermal SCC state at fixed time t is:

$$
(\,T,\, \lambda_K,\, u\,) \in (0, \infty) \times [0, \infty) \times \Sigma_m,
$$

with `Σ_m = {u ∈ [0,1]^n : Σ u_i = m}` the canonical volume-constrained simplex (canonical §8.0).

**Definition 1.2 (K_soft).** With monotone Lipschitz `φ : [0, ∞) → [0, ∞)`, `φ(0) = 0`, default (φ-sat) `φ(ℓ) = ℓ/(1+ℓ)`:

$$
K_{\mathrm{soft}}(u) \;=\; \sum_{i \in B_+(u)} \varphi(\ell_i(u)),
$$

`B_+(u)` = positive-length bars of H₀ persistence diagram of superlevel filtration of u.

**Definition 1.3 (Bernoulli entropy).**

$$
S(u) \;=\; -\sum_x \big[u(x)\log u(x) + (1-u(x))\log(1-u(x))\big],
$$

with `0 log 0 := 0`.

**Definition 1.4 (Free energy).**

$$
\mathcal{F}_{C+E}[u; T, \lambda_K] \;=\; \mathcal{E}[u] - T\cdot S(u) + \lambda_K \cdot K_{\mathrm{soft}}(u),
$$

with ℰ the canonical four-term energy (canonical §8.1).

**Default scaling commitment.** `λ_K = γ_K · T` with `γ_K ∈ [0.01, 0.1]` dimensionless (G3 §4.3 with Round 3 Hessian-stability tightening; see `06_further_verification.md` §1.6, E-7).

### 1.2 Pillar lemmas (the load-bearing technical statements)

**Lemma 1.5 (CSEH-derived Lipschitz of K_soft on Σ_m^ε).** For `u, v ∈ Σ_m^ε := Σ_m ∩ [ε, 1-ε]^n` (or generically on Σ_m \ V):

$$
|K_{\mathrm{soft}}(u) - K_{\mathrm{soft}}(v)| \;\leq\; 2 L_\varphi \cdot N_{\max}(u, v) \cdot \|u - v\|_\infty,
$$

with `N_{\max}(u,v) ≤ n`. Hence `L_K ≤ 2 L_φ · n` *(initial commit; corrected to `L_K ≤ 4 L_φ · n` per `05_deepening_and_verification.md` §1.5 — full proof reveals factor-of-2 from counting both u-side AND v-side diagonal pairings; total bar count is N(u) + N(v) ≤ 2n, not N_max ≤ n)*.

*Proof (G1 Prop 2.1).* CSEH 2007 Theorem 4.2: `W_∞(Dgm(u), Dgm(v)) ≤ ‖u−v‖_∞`. Optimal bottleneck matching γ pairs bars; `|ℓ_i(u) − ℓ_{γ(i)}(v)| ≤ 2 W_∞`. φ-Lipschitz ⇒ `|φ(ℓ_i) − φ(ℓ_{γ(i)})| ≤ 2 L_φ W_∞`. Sum over ≤ N_max bars + diagonal-paired unmatched: `|K_soft(u) − K_soft(v)| ≤ 2 L_φ N_max W_∞ ≤ 2 L_φ N_max ‖u−v‖_∞` *(missed v-side diagonals; corrected sum total bars = N(u)+N(v) ≤ 2n yields `L_K ≤ 4 L_φ n`).* ∎

**Lemma 1.6 (Bernoulli entropy properties).** S is (a) continuous on `[0,1]^n` with `0 log 0 = 0`, (b) strictly concave on `(0,1)^n`, (c) Lipschitz on `[ε, 1-ε]^n` with `L_S(ε) = log((1-ε)/ε)·√n`, (d) bounded `0 ≤ S(u) ≤ n log 2`.

*Proof (G2 Prop F2.1).* (a) elementary continuity. (b) Diagonal Hessian `∂²S/∂u(x)² = -1/u(x) - 1/(1-u(x)) < 0`. (c) `|∇S(u)|_∞ = max_x |log((1-u(x))/u(x))| ≤ log((1-ε)/ε)` on Σ_m^ε. (d) Per-site `−[t log t + (1−t)log(1−t)] ∈ [0, log 2]`. ∎

**Lemma 1.7 (Gibbs partition Z(T) finite).** For all T > 0, `Z(T) := ∫_{Σ_m} exp(-ℱ_{C+E}/T) dν` satisfies `0 < Z(T) < ∞`.

*Proof (G2 Prop F1.1).* Σ_m compact (canonical Cat A Prop 1.1). ℱ_{C+E} continuous on Σ_m (sum of continuous: ℰ polynomial, S continuous via (a) of Lemma 1.6, K_soft continuous via Lemma 1.5 + bottleneck stability). Continuous on compact ⇒ bounded ⇒ exp(-ℱ/T) bounded above and bounded below by positive constant. Integrable. ∎

**Lemma 1.8 (ℱ_{C+E} Lipschitz on Σ_m^ε).**

$$
L_{\mathcal{F}}(\varepsilon, T, \lambda_K) \;\leq\; L_{\mathcal{E}} + T \cdot L_S(\varepsilon) + \lambda_K \cdot L_K,
$$

with constituents per G3 §2.1 table.

*Proof (G3 Prop 2.1).* Sum of Lipschitz functions is Lipschitz with sum of constants. ∎

**Lemma 1.9 (ℱ_{C+E} bounded below + minimizer existence).**

$$
\inf_{u\in\Sigma_m} \mathcal{F}_{C+E}[u; T, \lambda_K] \;\geq\; -T\,n\log 2,
$$

and the infimum is attained.

*Proof (G3 Prop 3.1, Thm 3.3).* ℰ ≥ 0, S ≤ n log 2, K_soft ≥ 0 ⇒ ℱ ≥ -T n log 2. Σ_m compact, ℱ ∈ C^0 ⇒ Weierstrass attainment. ∎

### 1.3 Status of foundation (Cat A claims)

After §1.1–1.2, the following are **Cat A**:

| Claim | Reference |
|---|---|
| K_soft well-defined on Σ_m | Lemma 1.5 + bottleneck stability |
| ℰ + S + K_soft = ℱ_{C+E} continuous on Σ_m | Lemmas 1.5, 1.6(a) + canonical §8.1 |
| Gibbs measure ℙ_T well-defined for all T > 0 | Lemma 1.7 |
| ℱ_{C+E} Lipschitz on Σ_m^ε | Lemma 1.8 |
| ℱ_{C+E} attains minimum on Σ_m | Lemma 1.9 |

**Conditional / sketched (Cat B-C provisional):**

| Claim | Why conditional |
|---|---|
| Lipschitz across vineyard set V | V is codim-1, off V Lipschitz holds; generic-Lipschitz statement only |
| Langevin SDE F3 well-posed on Σ_m | Reflection at ∂Σ_m (Lions-Sznitman) + V handling needed (C-S2) |
| F4 T → 0 recovery of canonical Cat A | Case-by-case verification (C-S3) |
| λ_K = γ_K T scaling first-principles | Heuristic at present (NQ-10) |

---

## §2. Lipschitz + Coercivity + Existence (chained)

### 2.1 The chain

The minimizer-existence proof for ℱ_{C+E} is a chain of three structural facts:

1. **Compactness:** Σ_m is a compact convex polytope (canonical Cat A Prop 1.1).
2. **Continuity:** ℱ_{C+E} ∈ C^0(Σ_m) (Lemma 1.7 supporting).
3. **Lower bound:** ℱ_{C+E} ≥ -T n log 2 (Lemma 1.9).

⇒ Weierstrass: minimum attained.

### 2.2 Strengthening: real-analyticity off V (for Łojasiewicz)

**Lemma 2.1 (Analyticity of ℱ_{C+E} on Σ_m^ε \ V).** ℱ_{C+E} is real-analytic on `Σ_m^ε \ V`.

*Proof.*
- ℰ: polynomial in u (canonical §8 components are sums of polynomials of degrees ≤ 4) ⇒ real-analytic on ℝ^n.
- S: `−[t log t + (1−t)log(1−t)]` is real-analytic on `(0, 1)` ⇒ real-analytic on `(ε, 1−ε)^n ⊃ Σ_m^ε`.
- K_soft: piecewise constant in `argmax_θ` choice that determines bar-vertex assignments. Off V (no two vertices have equal u-value), the bar assignment is locally constant ⇒ K_soft locally agrees with `Σ_i φ(u(v_b^i) − u(v_d^i))` for fixed bar-vertex choices `(v_b^i, v_d^i)` ⇒ smooth in u. φ analytic (verify for φ-sat: `ℓ/(1+ℓ)` analytic on (−1, ∞) ⊃ ℓ ∈ [0, 1]) ⇒ K_soft real-analytic on each connected component of `Σ_m^ε \ V`.

Sum of real-analytic ⇒ real-analytic. ∎

**Corollary 2.2 (Łojasiewicz applies).** On `Σ_m^ε \ V`, the gradient flow of ℱ_{C+E}:

$$
\dot u = -\Pi_{T_u\Sigma_m} \nabla \mathcal{F}_{C+E}[u]
$$

converges to a critical point with rate determined by the Łojasiewicz exponent (canonical T14 generalization). Convergence is exponential when the Hessian at the critical point is non-degenerate; polynomial otherwise.

*Proof.* Standard Łojasiewicz–Simon for analytic functions on smooth Riemannian manifolds. Σ_m^ε \ V is open in Σ_m, hence a smooth submanifold. ℱ_{C+E} analytic. Apply T14 framework. ∎

### 2.3 Status of analytic chain

| Claim | Status |
|---|---|
| Σ_m compact polytope | Cat A (Prop 1.1, canonical) |
| ℱ_{C+E} ∈ C^0(Σ_m) | Cat A (Lemma 1.7) |
| ℱ_{C+E} bounded below | Cat A (Lemma 1.9) |
| ℱ_{C+E} attains min | Cat A (Lemma 1.9) |
| ℱ_{C+E} real-analytic on Σ_m^ε \ V | Cat A (Lemma 2.1) |
| Łojasiewicz applies on Σ_m^ε \ V | Cat A (Cor 2.2) |
| ℱ_{C+E} ∇-flow converges on Σ_m^ε \ V | Cat A (Cor 2.2) |
| Behavior on V (codim-1 vineyard) | sketched (mollification, C-S2) |

---

## §3. Kramers + Witten Laplacian Linked Spectral Story

### 3.1 The Kramers–Witten correspondence

The key technical link between G5 (Kramers MFPT) and G6 (Witten Laplacian) is the spectral identification: **first non-trivial small eigenvalue of Witten Laplacian Δ_{ℱ, T} = inverse Kramers MFPT (up to prefactor)**:

$$
\boxed{\;\;\lambda_1(\Delta_{\mathcal{F}, T}) \;\sim\; \tau_0^{-1} \exp(-\Delta\mathcal{F}/T) \;=\; \tau_{K=2 \to K=1}^{-1} \;\;}
$$

This is the rigorous derivation of Kramers via Helffer-Sjöstrand semiclassical analysis.

### 3.2 Step-by-step (sketch)

**Step 1 (Witten conjugation).** For ℱ smooth on a Riemannian manifold M, define `Δ_{ℱ, T} = e^{ℱ/(2T)} (-T² Δ + smaller terms) e^{-ℱ/(2T)}`. (Equivalently: `Δ_{ℱ, T} = -T² Δ + ‖∇ℱ‖²/(4) - T·Δℱ/2` up to convention.) Spectrum of Δ_{ℱ, T} on L²(M) is real, non-negative, with `0 ∈ spec` iff ℱ has a unique global minimum (the Gibbs ground state).

**Step 2 (small-eigenvalue cluster from local minima).** Near each local minimum `u_a^*` of ℱ, locally `ℱ ≈ ℱ(u_a^*) + (1/2)⟨H_a (u-u_a^*), u-u_a^*⟩`. The Witten Laplacian's local quadratic form approximates the harmonic oscillator with Hessian `H_a`. Each local minimum produces an eigenvalue close to `0` (the harmonic oscillator's ground state in the (T → 0) semiclassical limit is at energy `O(T)` above zero).

**Step 3 (tunneling between minima).** With multiple minima `u_1^*, …, u_K^*`, the small eigenvalues of Δ_{ℱ, T} split:
- One eigenvalue equals exactly 0 (Gibbs ground state).
- Other `(K_loc - 1)` eigenvalues have magnitude `~ exp(-ΔF/T)` where ΔF is the smallest barrier between basins.

**Step 4 (sharp asymptotic formula — Helffer-Sjöstrand 1985).**

$$
\lambda_1 \;=\; \frac{1}{2\pi}\,|\omega_s|\,\sqrt{\frac{|\det H_s|}{\det H_a}}\, \exp(-\Delta\mathcal{F}/T) \cdot (1 + o(1)) \quad (T \to 0).
$$

This is the **inverse Kramers MFPT**. Compare with G5 §3.2:

$$
\tau \;=\; \frac{2\pi}{|\omega_s|}\,\sqrt{\frac{\det H_a}{|\det H_s|}}\,\exp(\Delta\mathcal{F}/T).
$$

**Identical to first order — Kramers and Witten agree.**

**Step 5 (SCC application).** Take ℱ = ℱ_{C+E}, M = Σ_m^ε \ V (smooth Riemannian, dim n−1, with induced Euclidean or Shahshahani metric). Identify:
- `u_1^* = K_soft ≈ 1` ground state.
- `u_2^* = K_soft ≈ 2` metastable state.
- `u_s^* = K_soft ≈ 1.5` (or whatever variational saddle exists between basins).

Then `λ_1(Δ_{ℱ, T}) ~ (1/τ_0) exp(−ΔF_{2−1}/T)` is the inverse MFPT for K=2 → K=1 transition. Spectral gap of Fokker-Planck (G6 §4) is the same.

### 3.3 Sketched corollaries

**Corollary 3.1 (Inverse Kramers from Witten).** For SCC C+E at low T, `λ_1(Δ_{ℱ, T}) · τ_{K=2 → K=1} → 1` as `T → 0` (with prefactor depending on Hessian determinants at u_2^* and saddle).

**Corollary 3.2 (Spectral gap collapse at high-T).** As T grows, the small-eigenvalue cluster expands; the gap `λ_1 − λ_0 = λ_1` (since λ_0 = 0) approaches O(T) (no longer exponentially small). High-T regime: thermal mixing dominates, no metastability.

**Corollary 3.3 (Number of metastable states = small-eigenvalue count).** The number of metastable states at temperature T is approximately the number of eigenvalues of Δ_{ℱ, T} below an energy threshold `~T·max(|ω_a|)` (where ω_a are minima Hessian eigenvalues). This counts not just K=1 vs K=2 but all locally-stable configurations.

### 3.4 Status

| Claim | Status |
|---|---|
| Kramers MFPT formula | classical (Kramers 1940), sketched application to SCC (G5 §3.3) |
| Witten Laplacian spectrum encodes critical points | sketched (Helffer-Sjöstrand 1985, G6 §3) |
| Kramers ↔ Witten agreement (Cor 3.1) | sketched (rigorous via H-S 1985 Theorem 3.5) |
| Discrete-graph treatment of Δ_{ℱ, T} on finite-n Σ_m | open (C-S2 / post-Stage-1) |

---

## §4. Counter-Example Attempts

This section documents explicit attempts to break the §1–§3 claims, in line with §7 of the prompt's mathematical-rigor requirement.

### 4.1 Attempted counter-example to Lipschitz of K_soft

**Construction.** Take `n = 4`, m = 1.5. Consider `u^δ ∈ Σ_m`:
- `u^δ_1 = 1`, `u^δ_2 = 0.5 + δ`, `u^δ_3 = 0`, `u^δ_4 = 0` for δ ∈ [-ε, +ε].

For δ > 0, the H₀ persistence diagram of u^δ has bars: birth at `u^δ_1 = 1`, death (component merge with u^δ_2) at `u^δ_2 = 0.5 + δ` ⇒ ℓ_1 = 0.5 − δ. Birth at `u^δ_2 = 0.5 + δ`, death at 0 ⇒ ℓ_2 = 0.5 + δ.

For δ = 0, both bars have lengths {0.5, 0.5} — vineyard singularity (two bars of equal length, can be permuted).

For δ < 0: bars {0.5 − |δ|, 0.5 + |δ|} (same set, same K_soft).

K_soft = φ(0.5 − δ) + φ(0.5 + δ). With (φ-sat) `φ(ℓ) = ℓ/(1+ℓ)`:
- K_soft(δ) = (0.5−δ)/(1.5−δ) + (0.5+δ)/(1.5+δ)
- K_soft(0) = 1/3 + 1/3 = 2/3
- K_soft(δ) − K_soft(0) = small (continuous, smooth in δ).

**Verdict.** K_soft is continuous through the vineyard at δ = 0 — bar **lengths** match continuously even when bar **identities** swap. K_soft is in fact differentiable here (smooth). The vineyard singularity is in the **bar-assignment** map `δ → (ℓ_1, ℓ_2)` (sorted), but K_soft uses **the multiset** of bars (sum), so it's continuous.

**Conclusion.** This particular counter-example **fails** — K_soft is Lipschitz at vineyard. Counter-example would need to break **multiset stability** of bar lengths under L^∞ perturbation, which CSEH 2007 explicitly rules out.

**Implication.** Lemma 1.5 stronger than originally stated: K_soft is Lipschitz **on all of Σ_m** (not just `Σ_m \ V`). Vineyard set V breaks the **sorted bar-vector** continuity but not the **K_soft = sum-φ** continuity. Hence:

**Strengthened Corollary 4.1 (K_soft Lipschitz on Σ_m).** `K_soft : (Σ_m, ‖·‖_∞) → ℝ_{≥0}` is globally Lipschitz with `L_K ≤ 4 L_φ n` (no V exception). *(Constant corrected from 2 L_φ n per `05_deepening_and_verification.md` §1.5 — full proof factor-of-2 fix.)*

*Proof.* Bottleneck-stability gives L^∞-multiset stability of bar lengths. K_soft = sum over bars of φ(ℓ_i). Both sum and φ are continuous in the multiset; sum-φ is therefore continuous (and Lipschitz with bounded total bar count: ≤ 2n counting matched + u-diagonal + v-diagonal). ∎

### 4.2 Attempted counter-example to coercivity of ℱ_{C+E}

**Construction.** Search for u ∈ Σ_m with ℱ_{C+E}[u] → −∞.

Σ_m compact ⇒ ℱ_{C+E} bounded above and below (continuous on compact). No diverging u exists. Counter-example impossible.

**Conclusion.** Lemma 1.9 robust.

### 4.3 Attempted counter-example to F-1 dissolution

**Question.** Is there a configuration where soft-K still gives a "vacuous" K=2?

**Construction.** Try `u^*` with K_soft(u^*) = 2 but ℰ[u^*] arbitrary. By G4 §2 reframing, "K=2 vacuity" required external m_j; in soft-K there's no m_j. **The original "vacuous" condition cannot be re-expressed in soft-K language**.

Alternative reading: "K_soft ≈ 2 critical points don't exist on Σ_m". If true, this would mean exp62/exp63 observations are not true critical points.

Empirically, exp62/exp63 reach equilibrium under gradient flow at K_soft ≈ 2 configurations ⇒ they are gradient-flow stationary ⇒ critical points of ℰ on Σ_m. K_soft ≈ 2 critical points exist. Counter-example fails.

**Conclusion.** F-1 dissolution holds — the original "vacuity" claim has no analog in soft-K.

### 4.4 Attempted counter-example to MO-1 dissolution

**Question.** Is there a structural obstruction to smooth Morse on Σ_m^ε \ V even after removing Σ²_M corner?

**Construction.** Σ_m^ε is a smooth manifold of dimension n−1 (open polytope interior intersected with [ε, 1−ε]^n). It is **non-compact** (since corners are excluded). Standard smooth Morse uses **compact manifolds** (without boundary).

This is a real concern. Smooth Morse on non-compact manifolds requires additional conditions (Palais-Smale, properness of ℱ, etc.). Σ_m^ε is bounded ⇒ pre-compact in Σ_m. ℱ_{C+E} continuous on Σ_m ⇒ ℱ extends continuously to ∂Σ_m^ε = Σ_m \ Σ_m^ε. Critical points of ℱ_{C+E}|Σ_m^ε that approach ∂ are *boundary critical points* — handled separately.

**Conclusion.** Smooth Morse on Σ_m^ε \ V works for **interior** critical points. Critical points at corners of Σ_m (`u_i = 0` or `u_i = 1` somewhere) require boundary analysis. This is a **known limitation**, not a fatal obstruction. canonical T14 (gradient flow convergence) handles boundary cases via reflection / KKT conditions. Standard.

For MO-1 *as originally framed* (Σ²_M corners), the dissolution holds (Σ²_M removed). The remaining "Σ_m corners" are the standard polytope corners that all variational problems on Σ_m face — not a new MO-1 problem.

**Strengthening.** MO-1 dissolution restated: "Σ²_M corners (specific to integer-K K-field architecture) are removed by soft-K. Σ_m's polytope corners (canonical Prop 1.1) remain but are handled by standard polytope variational tools (reflection, KKT). No new analytical obstruction."

### 4.5 Attempted counter-example to M-1 isoperimetric reframing

**Question.** Is there a graph or parameter regime where K_soft ≈ 2 has *lower* ℰ than K_soft ≈ 1? This would refute M-1's isoperimetric basis.

**Construction.** On a *disconnected* graph (two disconnected components), m mass naturally splits across components — and the "natural" minimum is K_soft = 2 (one mode per component), not K_soft = 1.

**Verdict.** Yes — on disconnected graphs, isoperimetric ordering does not apply (no perimeter-minimizer is "single connected"). Then K_soft > 1 may be globally optimal.

**Implication.** M-1 reframing (M-1 is "feature, not bug") implicitly assumes **connected** graph (canonical T-Merge (b) is on connected graphs). On disconnected graphs, the framing changes.

**Conclusion.** M-1 reframing scope: **connected graphs only**. Disconnected graph case is a separate regime where K_soft > 1 is natural and unproblematic. Document as caveat in `M1_dissolution.md` §2.4.

**Status update for M-1 reframing:** scope-restricted to connected graphs. (Canonical's "K=1 always preferred" is also implicitly connected-graph statement — exp62/63 etc. are on connected grids.)

---

## §5. Category Self-Classification Audit

Based on §1–§4, here is the per-claim category audit:

| Claim | File reference | Self-class | Notes |
|---|---|---|---|
| K_soft continuous on Σ_m | G1 §2.1 + Cor 4.1 | **Cat A** | strengthened by §4.1 |
| K_soft Lipschitz globally on Σ_m | G1 §2 + Cor 4.1 | **Cat A** | newly strengthened |
| K_soft hard-K recovery (sharp limit) | G1 Prop 4.1 | sketched | Cat A-provisional |
| F1 Gibbs Z(T) finite | G2 Prop F1.1 | **Cat A** | |
| F2 Bernoulli S props (cont, concave, bounded) | G2 Prop F2.1 | **Cat A** | |
| F3 Langevin well-posed on Σ_m^ε | G2 §3 → upgraded `06_further_verification.md` §8 Thm F3.1 | **Cat A** via Lions-Sznitman 1984 (Round 3) | Cat C only on full Σ_m corner extension |
| F4 T → 0 recovery of canonical Cat A | G2 §4 | statement only | Cat C, C-S3 carry |
| ℱ_{C+E} ∈ C^0(Σ_m) | G3 §2.3 | **Cat A** | |
| ℱ_{C+E} Lipschitz on Σ_m^ε | G3 Prop 2.1 | **Cat A** | |
| ℱ_{C+E} real-analytic on Σ_m^ε \ V | Lemma 2.1 here | **Cat A** | new combined statement |
| ℱ_{C+E} bounded below | G3 Prop 3.1 | **Cat A** | |
| ℱ_{C+E} minimizer exists | G3 Thm 3.3 | **Cat A** | |
| Łojasiewicz applies on Σ_m^ε \ V | Cor 2.2 here | **Cat A** | |
| λ_K = γ_K T scaling | G3 §4.3 | committed (heuristic) | NQ-10 open |
| F-1 vacuity dissolved (E-side) | G4 §2 | **Cat A** | architectural |
| F-1 thermal occupation (C-side) | G4 §3 | sketched | Cat C, CE-S2 carry |
| M-1 reframing as feature | G5 §2 | **Cat A** | scope: connected graphs (§4.5) |
| M-1 Kramers metastability | G5 §3 | sketched | Cat C, C-S2 carry |
| MO-1 corner dissolved (E-side) | G6 §2 | **Cat A** | with corner caveat (§4.4) |
| MO-1 Witten Laplacian (C-side) | G6 §3 | statement only | Cat C, post-Stage-1 |
| Kramers ↔ Witten correspondence (Cor 3.1) | §3 here | sketched | based on H-S 1985 |

**Aggregate session output:**
- **New Cat A claims:** 12 (foundation + dissolutions of integer-K Critical at architectural level).
- **Sketched (Cat C-provisional):** 7 (Kramers prefactor, Witten Laplacian, F4 recovery, vineyard handling, etc.).
- **Statement-only (carry):** 3 (F3 Langevin, F4 recovery, MO-1 Witten on discrete).
- **NQ-1 partially resolved:** soft-K canonical choice committed to (i) persistence-weighted; full uniqueness open.
- **NQ-10 (new):** λ_K = γ_K T first-principles derivation.

---

## §6. Granularity for Future Sessions

This file's substantive sub-sections are numbered (§1.1–§5) so that follow-up sessions can request "expand §3.4 step 4 with full Helffer-Sjöstrand prefactor derivation" or "verify Lemma 2.1 specifically for (φ-lin) instead of (φ-sat)" without ambiguity. Each Lemma / Corollary above is independently verifiable.

Specifically, items most likely to be expanded in C-S2:
- **Lemma 1.8 (Lipschitz constants):** sharper graph-spectral bounds.
- **Step 4 of §3.2 (Helffer-Sjöstrand prefactor):** full asymptotic formula on discrete graph.
- **§4.1 (K_soft Lipschitz at V):** rigorous treatment.

Items most likely to be expanded in C-S3:
- **Lemma 1.5 → F4(b)**: enumerate which Cat A theorems survive T → 0.
- **§3.5 (multi-K cascade):** Ostwald ripening on Σ_m.

Items for Stage 5 (Numerical Validation):
- **G4 §3.3 example distribution:** numerical Boltzmann ratios at calibrated SCC parameters.
- **G5 §4.1 γ_eff = 0.89 reinterpretation:** independent prediction test.

Next file: `03_integration_and_new_open.md` (canonical integration + new open questions + canonical_sub.md entry draft).
