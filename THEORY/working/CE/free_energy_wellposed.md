# Free Energy Cross-Object — ℱ_C+E Well-Definedness (G3)

**Status:** working (commit, 2026-04-21)
**Author origin:** `logs/daily/2026-04-21/01_exploration.md` §3.1.
**Canonical refs:** `canonical.md` §8 (energy on Σ_m), §13 Cat A T1 (existence on compact via Weierstrass), §13 Cat A T11 (Γ-conv), §14 CN5 (four-term independence — preserved here).
**Working refs:** `working/E/soft_K_definition.md` (G1), `working/C/F_group_axioms.md` (G2).
**Dependencies:** G1 (K_soft Lipschitz), G2 (F1 Gibbs normalizability, F2 entropy continuity).

---

## §1. The Cross-Object

### 1.1 Definition

**Definition (Free energy).** For `T > 0` and `λ_K ≥ 0`:

$$
\boxed{\;\;\mathcal{F}_{\mathrm{C+E}}[u] \;=\; \mathcal{E}[u] \;-\; T\cdot S[u] \;+\; \lambda_K\cdot K_{\mathrm{soft}}(u)\;\;}
$$

where:
- `ℰ[u] = λ_cl ℰ_cl + λ_sep ℰ_sep + λ_bd ℰ_bd + λ_tr ℰ_tr` is the canonical energy (canonical §8.1);
- `S[u]` is the Bernoulli entropy (G2, F2.0);
- `K_soft(u)` is the persistence-weighted soft count (G1, Def 1).

**Five terms.** ℰ contributes 4 sub-terms (Cl, Sep, Bd, Tr), `−T·S` contributes a fifth (entropic), `+λ_K·K_soft` a sixth (topological-complexity penalty). Conceptually independent (CN5 preserved + extended): each term addresses a logically distinct structural requirement (cohesion, separation, morphology, transport, local participation uncertainty, mode count regularization). No mathematical merging — the five terms remain syntactically separate.

**Note on transport term.** For single-time-slice (within-slice) analysis, `ℰ_tr` involves coupling between `u_t` and `u_s` for s ≠ t. The Gibbs measure F1 of G2 §1.1 is over a single Σ_m at fixed t. To handle ℰ_tr in this thermal framework, one can: (i) take ℰ_tr = 0 for within-slice analysis (F4.b recovery argument), (ii) extend the state space to product `Σ_m^t × Σ_m^s` for two-time analysis (carried to E-S2). This file treats (i) for ℰ-sum below; the ℰ_tr term is included in the formula for completeness but does not enter Lipschitz/coercivity bounds in this section.

### 1.2 Three terms' roles (semantic separation)

- **ℰ:** "static" SCC energy — drives field toward closure-supported, distinguished, morphologically articulated configurations. T-independent.
- **−T·S:** thermodynamic entropy contribution — at higher T, the system "smooths out" toward higher-entropy configurations (less concentrated, less peaked). Sign convention: negative (entropy is *added* as a benefit), so `−T·S` is *subtracted*, which when minimized ⇒ S maximized in the Gibbs balance.
- **+λ_K·K_soft:** complexity / mode-count regularization — penalizes configurations with many distinct modes. With `λ_K > 0`, single-mode is preferred over multi-mode at fixed ℰ-S balance.

---

## §2. Lipschitz on Σ_m^ε

### 2.1 Constituent Lipschitz constants

Recall `Σ_m^ε := Σ_m ∩ [ε, 1-ε]^n` (the ε-interior of the volume manifold). On `Σ_m^ε`:

| Functional | Lipschitz constant on `(Σ_m^ε, ‖·‖_∞)` | Source |
|---|---|---|
| `ℰ_cl(u) = Σ(u - Cl(u))²` | `L_{cl} ≤ 2(1 + a_cl/4) · √n` | direct: ∇ℰ_cl = 2(I - J_Cl)^T(u - Cl(u)); each entry bounded by `(1 + ‖J_Cl‖_op)·diam` ≤ `(1 + a_cl/4)·diam`. |
| `ℰ_sep(u) = Σ u(1 - D(x; 1-u))` | `L_{sep} ≤ (1 + a_D · (1 + λ_D))·√n` | direct: ∇ℰ_sep involves D and ∂D/∂u; ‖∂D/∂u‖_op ≤ a_D·max(1, λ_D)/4 (sigmoid Lipschitz). |
| `ℰ_bd = α Σ_{x,y} N(x,y)(u_x - u_y)² + β Σ u²(1-u)²` | `L_{bd} ≤ 4α·d_max·√n + 2β·max_u\|W'(u)\|·√n ≤ (4α·d_max + β/2)·√n` | direct: smoothness term is quadratic; double-well max of `|W'| = max|2u(1-u)(1-2u)| ≤ 1/(3√3) ≤ 0.193`, so `2β·max|W'| ≤ 0.4β`. |
| `S(u)` | `L_S(ε) = log((1-ε)/ε) · √n` | G2 Prop F2.1(d). |
| `K_soft(u)` | `L_K ≤ 4 L_φ · n` | G1 Cor 2.2 (corrected 2026-04-21 evening per `logs/daily/2026-04-21/05_deepening_and_verification.md` §1.5). |

### 2.2 Total Lipschitz of ℱ_C+E

**Proposition 2.1.** ℱ_C+E is Lipschitz on `Σ_m^ε` with respect to `‖·‖_∞` (and hence `‖·‖_2`):

$$
L_{\mathcal{F}}(\varepsilon, T, \lambda_K) \;\leq\; L_{cl}(\lambda_{cl}) + L_{sep}(\lambda_{sep}) + L_{bd}(\lambda_{bd}) + T\cdot L_S(\varepsilon) + \lambda_K\cdot L_K.
$$

For default canonical parameters (a_cl = 3, λ_D = 1, a_D = 4, α = 1, β = 30, ε = 0.05) and (φ-sat) for K_soft:

- L_cl ≤ 2 · 1.75 · √n ≈ 3.5√n
- L_sep ≤ 1 + 4·2 = 9√n (loose)
- L_bd ≤ (4·4 + 15)·√n = 31√n (using d_max = 4 on a 2D grid)
- T·L_S(0.05) = T · log(19) · √n ≈ 2.94T·√n
- λ_K·L_K ≤ λ_K · 4n (corrected 2026-04-21 evening)

Order of magnitude: `L_F ≈ O((1 + T)·√n + λ_K·n)` on Σ_m^ε at canonical params (constant 4 vs 2 on K-term doesn't change order).

### 2.3 Lipschitz on full Σ_m (incl. corners)

ℰ remains continuous to corners (polynomial in u). S extends continuously to corners (G2 Prop F2.1(b)) but its gradient blows up — so S is not Lipschitz at corners. K_soft is continuous on full Σ_m (G1 §2.3 — bottleneck stability holds globally) but its gradient is undefined on vineyard set V (codim-1).

**Conclusion.** `ℱ_C+E ∈ C^0(Σ_m)` (continuous on full Σ_m, incl. corners). Lipschitz globally only on `Σ_m^ε`. Variational analysis (existence) uses only continuity (§3); thermal dynamics analysis (§5 / F3 well-posedness) uses Lipschitz on `Σ_m^ε`.

---

## §3. Coercivity and Minimizer Existence

### 3.1 Coercivity (in the sense of Σ_m compact)

Σ_m is compact, so coercivity in the sense of "level sets are compact" is automatic. The relevant question is whether ℱ_C+E is **bounded below** on Σ_m so that minimizers exist.

**Proposition 3.1 (Lower bound).**

$$
\inf_{u \in \Sigma_m} \mathcal{F}_{\mathrm{C+E}}[u] \;\geq\; 0 \;-\; T\cdot n \log 2 \;+\; 0 \;=\; -T\,n\log 2.
$$

*Proof.* ℰ ≥ 0 (canonical §8.2–8.4: ℰ_cl, ℰ_sep, ℰ_bd, ℰ_tr each are sums of squares or non-negative terms). S ≤ n log 2 (G2 Prop F2.1(a)). K_soft ≥ 0 (G1 P1). Sum: ℱ ≥ 0 - T·n log 2 + 0 = -T·n log 2. ∎

**Proposition 3.2 (Upper bound on minimum).**

$$
\inf_{u\in\Sigma_m} \mathcal{F}_{\mathrm{C+E}}[u] \;\leq\; \mathcal{F}_{\mathrm{C+E}}[u_{\mathrm{uniform}}] \;=\; \mathcal{E}[u_{\mathrm{uniform}}] - T\cdot S[u_{\mathrm{uniform}}] + 0,
$$

with `S[u_{uniform}] = n[c log(1/c) + (1-c)log(1/(1-c))]` where `c = m/n`. K_soft(u_uniform) = 0 (G1 P1). So upper bound is finite.

### 3.2 Minimizer existence (Weierstrass)

**Theorem 3.3 (Existence of ℱ_C+E minimizer on Σ_m).** For all `T ≥ 0` and `λ_K ≥ 0`, ℱ_C+E attains its infimum on Σ_m.

*Proof.* Σ_m is compact (canonical Cat A Prop 1.1). ℱ_C+E ∈ C^0(Σ_m) (§2.3). Bounded below (Prop 3.1). Weierstrass extreme value theorem applies. ∎

**Status: Cat A** (Weierstrass on compact + continuity, both established).

### 3.3 Multiple minimizers (uniqueness fails generally)

ℱ_C+E is **not convex** (ℰ_bd contains the double-well term `β · u²(1-u)²` which is non-convex). Uniqueness of minimizer is **not** expected; multiple critical points (local minima, saddles) are the norm. Hessian analysis at minimizers is part of M-1 dissolution (G5 §3 Kramers, G6 §3 Witten Laplacian).

The **Gibbs measure ℙ_T** (F1) integrates over all minimizers (and saddles) with thermal weights `exp(-ℱ/T)`. At T → 0, ℙ_T concentrates on the global minimum set. At T > 0, multiple basins are populated with relative weight `exp(-ΔF/T)`.

---

## §4. λ_K Scaling Argument (Q2 from plan.md)

### 4.1 Three candidate scalings

Per plan.md Q2 and pre_brainstorm §C (H-C1, H-C2, H-C3):

- **(λ_K-T) Linear in T:** `λ_K = γ_K · T` for fixed dimensionless `γ_K > 0`.
- **(λ_K-1) T-independent:** `λ_K = γ_K`.
- **(λ_K-β) Inverse-T:** `λ_K = γ_K · β = γ_K / T` (so `λ_K → ∞` as T → 0).

### 4.2 Analysis of each scaling

**(λ_K-T):** As T → 0, `λ_K · K_soft → 0`. Hence ℱ → ℰ at T → 0 ⇒ canonical v1.2 reduction of F4.a is **clean**. The Gibbs density acquires factor `exp(-T γ_K K_soft / T) = exp(-γ_K K_soft)` — i.e., K_soft enters as a **T-independent prior** in the partition function. Two interpretations: (a) effective entropy `S_{eff} = S - γ_K K_soft / 1` if normalized differently; (b) "topological complexity bias" with bias strength independent of T.

**(λ_K-1):** As T → 0, `λ_K · K_soft → λ_K · K_soft (deterministic)`. So canonical v1.2 reduction includes a *new* term `λ_K · K_soft` even at T = 0. This **does not** recover canonical v1.2 cleanly — F4.a reduction is to a *modified* deterministic theory.

**(λ_K-β):** As T → 0, `λ_K → ∞`, and `λ_K · K_soft → ∞` for any K_soft > 0 — only `K_soft = 0` is admissible. This forces uniform configuration at T = 0 (since K_soft(u_uniform) = 0). Conflicts with canonical's non-trivial minimizer (T8-Core).

### 4.3 Recommended scaling: (λ_K-T) with γ_K small

**Recommendation.** Use `λ_K = γ_K · T` with **γ_K small**. **(φ-sat) commit:** `γ_K ∈ [0.01, 0.1]` dimensionless under (φ-sat) `φ(ℓ) = ℓ/(1+ℓ)` *(upper bound tightened 2026-04-21 evening per `logs/daily/2026-04-21/06_further_verification.md` §1.6 — Hessian stability requires `γ_K · n ≲ 1 + β/(4T)` ≈ 0.13 at canonical n = 64, β = 30, T = 1, with φ'' = -2/(1+ℓ)³ giving negative-semidefinite ∇²K_soft of op-norm ≤ 4n)*.

**(φ-lin) generalization (Round 8 per E-11):** for φ_lin(ℓ) = min(ℓ/ℓ_0, 1), `φ_lin''(ℓ) = 0` a.e. ⇒ ∇²K_soft = 0 a.e. (only Dirac at ℓ_0 kink). Hessian-stability constraint **lifted** ⇒ `γ_K` admissible range much wider for (φ-lin). The `[0.01, 0.1]` range above is **(φ-sat) specific**.

**Justifications:**

1. **Clean F4 recovery.** As T → 0, ℱ → ℰ exactly (modulo the T·S term which also vanishes). Canonical v1.2's variational characterization is recovered.

2. **Information-theoretic dimensional consistency.** Both `S` and `K_soft` are "information measures" (S = Shannon entropy of per-site Bernoulli; K_soft = persistence-weighted complexity). With `γ_K · T` scaling, the Gibbs density becomes:

$$
\mathbb{P}_T[u] \propto \exp\!\Big(-\frac{\mathcal{E}[u]}{T}\Big) \cdot \exp\!\big(S[u] - \gamma_K K_{\mathrm{soft}}(u)\big).
$$

The "**effective entropy**" `S - γ_K K_soft` combines two information measures with the same dimension (dimensionless, log-units). γ_K is the relative weight of the two information sources.

3. **Limiting behaviors.**
   - **γ_K = 0:** pure thermal SCC without K_soft regularization. Gibbs of ℰ alone with entropy.
   - **γ_K → ∞:** K_soft penalty dominates ⇒ system forced to K_soft = 0 (uniform configuration) regardless of ℰ/T. Pathological.
   - **γ_K = O(1):** K_soft and S contribute comparably to the prior. Crossover (γ_K · K_soft ≈ S) is the regime of "phase competition" in mode count.

### 4.4 Status

**Recommendation (λ_K = γ_K T) committed for present session.** Choice of γ_K value is open (parametric); commit only the *scaling form*. Full derivation of γ_K from first principles or from RG analysis (pre_brainstorm H-B16) is open.

**NQ-10 (new):** First-principles determination of γ_K. Carried to subsequent sessions.

---

## §5. Critical Compatibility Checks

### 5.1 Does ℱ_C+E conflict with canonical CN5 (four-term independence)?

**No.** CN5 asserts the four ℰ-terms are *conceptually* independent. ℱ_C+E adds *two more* terms (-T·S and λ_K K_soft), each addressing a new conceptual axis (thermodynamic uncertainty; mode-count complexity). The "four-term independence" generalizes naturally to "six-term independence" — no merging of pre-existing terms, no loss of independence claim.

**Sub-check:** is `−T·S` mergeable with `+λ_K·K_soft`? Both are information-measure terms with similar units. **Conceptually distinct:**
- `S` measures *per-site participation uncertainty* (local, point-wise sum).
- `K_soft` measures *global topological mode count* (filtration-based, global).

Both are scalars, but they probe different structural aspects. Merging them (e.g., into a single "complexity prior") would obscure this distinction — explicitly avoided per CN5 spirit.

### 5.2 Does ℱ_C+E conflict with canonical CN12 (Q_morph persistence-based)?

**No, supports.** K_soft uses the same H₀ persistence machinery as Q_morph. The two are different functions (`Q_morph` is normalized for ℓ_max + Artic; `K_soft` is sum over all bars), but both rooted in CN12's filtration commitment. ℱ_C+E's K_soft term is a thermal-weighted regularization compatible with CN12.

### 5.3 Does ℱ_C+E conflict with canonical CN6/CN8/CN14 (kinetic metastability)?

**No, substantiates.** CN6 ("K kinetically determined"), CN8 ("formations metastable not globally optimal"), CN14 ("closure expands metastability") are interpreted thermally:
- CN6: "kinetically determined" → Kramers-rate determined (G5 §3).
- CN8: "metastable" → finite-T local minimum of ℱ_C+E with Boltzmann population `exp(-ΔF/T)` (G4 §3).
- CN14: "closure expands metastability" → closure increases barrier height, hence Kramers timescale; quantified in G5 §4.

These were previously zero-T claims (P-F gap). F-group + ℱ_C+E *fill* this gap.

### 5.4 Does ℱ_C+E conflict with canonical Cat A theorems?

**No.** Cat A theorems are statements about ℰ, Σ_m, Cl_t, etc. — all preserved. ℱ_C+E is a strict extension (ℰ is recovered as T → 0 with γ_K · T → 0).

The 9+1 integer-K theorems (`working/integer_K_dependency_map.md` §2) are the only canonical results affected, and these are explicitly Retire/Re-prove targets of the C+E reformulation. No silent retraction.

---

## §6. Status Summary

| Statement | Claim | Status |
|---|---|---|
| ℱ_C+E ∈ C^0(Σ_m) | continuous everywhere | proved (§2.3) |
| ℱ_C+E Lipschitz on Σ_m^ε | yes, with explicit bound | proved (Prop 2.1) |
| ℱ_C+E bounded below on Σ_m | yes, ≥ −T·n log 2 | proved (Prop 3.1) |
| Minimizer exists | yes (Weierstrass) | proved (Thm 3.3) |
| Minimizer unique | no (non-convex) | conditional on Hessian |
| Gibbs ℙ_T exists & finite | yes (G2 §1.2) | proved |
| λ_K scaling: λ_K = γ_K · T recommended | yes | committed (§4.3) |
| F4 recovery (T → 0) | yes (Laplace) | sketched, full carry to C-S3 |

**Category self-classification of "ℱ_C+E well-defined and minimized on Σ_m":** **Cat A**.

---

## §7. Carry / Next

- **G4–G6:** use ℱ_C+E as the foundational object. Each dissolution shows how integer-K Critical (F-1, M-1, MO-1) fade or transform under this thermal-soft-K free energy.
- **C-S2:** F3 Langevin well-posedness via ℱ_C+E gradient regularity.
- **CE-S2:** (T, λ_K) phase diagram — pre_brainstorm H-C4 four-corner exploration.
- **C-S3:** F4 T → 0 recovery proofs.

Next file: `working/E/M1_dissolution.md` (G5 — most substantive of three dissolutions per plan §G5).
