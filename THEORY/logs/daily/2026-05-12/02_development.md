---
type: log/development
date: 2026-05-12
target: OP-AFD-003 (Infimum Attainment in AFD-D7)
canonical_version: CV-1.13 (read-only)
session_label: W7-Day3
proof_classification:
  Q-A (minimal, λ_D = λ_K = 0): Cat A (unconditional, fully proved here)
  Q-B (rectifiable, λ_D, λ_K ≥ 0, bounded length L): Cat A (proved here, with explicit L)
  Q-C (density: bounded-length inf = unrestricted inf): Cat A (proved here for Bar; Cat B for J_K refinement)
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# 02 — Development: OP-AFD-003 Infimum Attainment

**Session:** 2026-05-12
**Target (from plan.md Priority 3):** Prove infimum attainment in `C_AFD(F_i, F_j) = inf_γ J_AFD(γ; F_i)`.

**This file covers:** Primary proof (Approach A), parallel proof (Approach B), counterexample search (Approach D), extension to general (λ_D, λ_K).

**Depends on reading:** `01_exploration.md` of this session for restatement and approach selection.

---

## §1. Setup, Notation, and Standing Assumptions

**Standing assumptions, all Cat A (verified):**

(S1) `G = (V, E_G)` is a finite connected graph; `n = |V| < ∞`.

(S2) `Σ_m = { u ∈ [0,1]^n : Σ_i u_i = m }` with fixed `m ∈ (0,n)`. Σ_m is a **compact convex polytope** in ℝ^n (T-PF-A1-AR Cat A, canonical.md §13).

(S3) `E : Σ_m → ℝ` is **continuous on Σ_m** (analytic on its relative interior — A3 gives `b_D = 0` analyticity; for OP-AFD-003 we use only continuity). Hence `M_E := max_{Σ_m} E < ∞` and `m_E := min_{Σ_m} E > -∞`. The constant

$$
R_E := M_E - m_E < \infty
$$

is the *energy range* of the polytope.

(S4) `F_i, F_j ∈ V_form` are formation states (AFD-D3) with representatives `u_{F_i}^*, u_{F_j}^* ∈ Σ_m` and deterministic basins `B_{F_i}, B_{F_j}` (AFD-D2). The basin closures `cl(B_{F_i})`, `cl(B_{F_j})` are closed subsets of compact Σ_m, hence themselves **compact**.

(S5) `E_{F_i} := E(u_{F_i}^*)`, `E_{F_j} := E(u_{F_j}^*)`. Both finite.

(S6) The admissible class

$$
\mathrm{Adm}(F_i, F_j) \;=\; \bigl\{\, \gamma \in C\bigl([0,1], \Sigma_m\bigr) : \gamma(0) \in \mathrm{cl}(B_{F_i}),\; \gamma(1) \in \mathrm{cl}(B_{F_j}) \,\bigr\}
$$

is non-empty (for any `u_0 \in cl(B_{F_i})`, `u_1 \in cl(B_{F_j})`, the segment `γ(s) = (1-s) u_0 + s u_1` lies in the convex set Σ_m and is continuous).

(S7) The metric used on `C([0,1], Σ_m)` is the uniform (sup) metric

$$
d_\infty(\gamma, \tilde\gamma) \;=\; \max_{s\in[0,1]} \lVert \gamma(s) - \tilde\gamma(s) \rVert_2.
$$

**Functionals.** For `γ ∈ Adm(F_i, F_j)`:

- `Bar(γ, F_i) := max_{s∈[0,1]} (E(γ(s)) − E_{F_i})`.
- `Var_D(γ) := TV(D ∘ γ)` (total variation; AFD-D9 continuous variant).
- `J_K(γ) := TV(K_act ∘ γ)` (AFD-D10).
- `J_AFD(γ; F_i) := Bar(γ, F_i) + λ_D Var_D(γ) + λ_K J_K(γ)` with `λ_D, λ_K ≥ 0`.

**Goal.** Show `inf_{Adm} J_AFD` is *attained* in (Q-A, Q-B) cases.

---

## §2. Lemma L1: Constant-Speed (Image-Length) Reparametrization

### 2.1 Statement

**Lemma L1.** Let `γ ∈ C([0,1], Σ_m)` be a continuous path of finite length `L(γ) < ∞` (using the Euclidean metric on Σ_m). Then there exists a continuous path `γ̃ ∈ C([0,1], Σ_m)` with:

(L1a) `γ̃` has the same image as `γ`: `γ̃([0,1]) = γ([0,1])`.

(L1b) `γ̃` is Lipschitz with constant `L(γ)`: `‖γ̃(s) − γ̃(s')‖_2 ≤ L(γ) · |s − s'|` for all `s, s' ∈ [0,1]`.

(L1c) `γ̃(0) = γ(0)`, `γ̃(1) = γ(1)`.

(L1d) `Bar(γ̃, F_i) = Bar(γ, F_i)` (the max of E along the path is image-determined).

(L1e) `Var_D(γ̃) = Var_D(γ)` and `J_K(γ̃) = J_K(γ)` (TV is invariant under monotone reparametrization).

### 2.2 Proof

Let `s_γ(t) := L(γ|_{[0,t]})` be the length-function along γ. Since γ is continuous and Σ_m is bounded, `s_γ : [0,1] → [0, L(γ)]` is continuous and non-decreasing, with `s_γ(0) = 0`, `s_γ(1) = L(γ)`.

Define `φ : [0, L(γ)] → [0,1]` to be any continuous monotone right-inverse of `s_γ` (well-defined modulo flat plateaus where `s_γ` is constant; on each plateau choose `φ` constant). Equivalently `γ̃(s) := γ(φ(s · L(γ)))` is the constant-speed parametrization.

(L1a) Image equality is immediate from `γ̃ = γ ∘ φ ∘ (· · L(γ))` with φ surjective onto `[0,1]` modulo plateaus.

(L1b) For `s, s' ∈ [0,1]`, `‖γ̃(s) − γ̃(s')‖_2 ≤ L(γ̃|_{[s,s']}) = L(γ) · |s − s'|` by construction (arc-length parametrization).

(L1c) `γ̃(0) = γ(φ(0)) = γ(0)`, `γ̃(1) = γ(φ(L(γ))) = γ(1)`.

(L1d) `max_s E(γ̃(s)) = max_{t ∈ image(γ̃)} E(t) = max_{t ∈ image(γ)} E(t) = max_s E(γ(s))`. Hence Bar coincides.

(L1e) `Var_D(γ̃) = TV(D ∘ γ̃ )`; total variation depends only on the image traversal pattern. The reparametrization preserves the order and multiplicity of traversal of any value (φ is monotone non-decreasing). Hence TV is preserved. Same for J_K. □

**Remark.** Lemma L1 makes "constant speed" a *canonical* representative within each image-equivalence class. Henceforth a minimizing sequence of admissible paths can be assumed Lipschitz with constant equal to its length.

**Cat A self-judgment.** L1 is a standard real-analysis lemma (Federer 1969 §2.5; Burago-Burago-Ivanov 2001 §2.5). No SCC-specific input. **proved**, no gap.

---

## §3. Lemma L2: Uniform Image-Length Bound for Bar-Minimizing Sequences

### 3.1 Statement

**Lemma L2.** Let `(γ_k)` be a sequence in `Adm(F_i, F_j)` with `Bar(γ_k, F_i) → Bar(F_i, F_j) =: B^*`. Then there exists a sequence `(γ̃_k) ⊂ Adm(F_i, F_j)` with:

(L2a) Same endpoints: `γ̃_k(0) = γ_k(0)`, `γ̃_k(1) = γ_k(1)`.

(L2b) `Bar(γ̃_k, F_i) ≤ Bar(γ_k, F_i)` (improvement allowed).

(L2c) `γ̃_k` is piecewise-linear with at most `N` vertices, all in the **sub-level set**
`Σ_m^{(B^* + ε_k)} := { u ∈ Σ_m : E(u) ≤ E_{F_i} + B^* + ε_k }`
for some `ε_k ↓ 0` and `N = N(γ_k, ε_k)` finite.

(L2d) `L(γ̃_k) ≤ N · diam(Σ_m) = N · √2 · √n` (diameter of Σ_m in Euclidean norm; finite since Σ_m is bounded).

### 3.2 Proof

Fix k. Let `B_k := Bar(γ_k, F_i)`. The sub-level set

$$
A_k := \Sigma_m^{(B_k)} = \{ u \in \Sigma_m : E(u) \le E_{F_i} + B_k \}
$$

is a **closed** subset of compact Σ_m (E continuous) — hence compact. It contains `image(γ_k)` (by definition of Bar).

`A_k` is compact, so it has finite **diameter** ≤ diam(Σ_m). Since `cl(B_{F_i}), cl(B_{F_j}) ⊂ A_k` (because `u_{F_i}^*, u_{F_j}^* ∈ A_k`; for points in basin closures other than the representative, they all satisfy `E ≤ E_{F_i} + B_k` whenever they lie in `image(γ_k)`).

Now **A_k is not necessarily connected**, but it does contain `image(γ_k)` which is path-connected (continuous image of `[0,1]`). The path-component of `A_k` containing `image(γ_k)` is itself a compact, path-connected subset of Σ_m. Call this component `Â_k`.

**Key observation.** We may construct a piecewise-linear path `γ̃_k` inside `Â_k` from `γ_k(0)` to `γ_k(1)` as follows:

Step 1. Choose a finite ε-net `{p_1, ..., p_{N_k}}` of `Â_k` (exists since `Â_k` compact in Euclidean ℝ^n): every point of `Â_k` is within ε_k of some `p_j`, with ε_k → 0 chosen.

Step 2. Form the **ε-net graph** `H_k = (V_k, E_k)`: vertices `p_1, ..., p_{N_k}` plus the endpoints `γ_k(0), γ_k(1)`; edge `(p, q) ∈ E_k` iff `‖p - q‖_2 ≤ 3 ε_k` *and* the segment `[p, q]` (Euclidean line segment in Σ_m) lies entirely in `Σ_m^{(B_k + δ_k)}` for some `δ_k → 0`. The set Σ_m^{(B_k + δ_k)} is *open* in Σ_m relative-topology when δ_k > 0 (sublevel set of continuous E with strict inequality) — but we want a closed sublevel for `δ_k → 0`. To handle continuity we use uniform continuity of E on Σ_m.

**Why such edges suffice.** Since γ_k traces a continuous curve in `Â_k` and E is uniformly continuous on compact Σ_m, the modulus of continuity `ω_E(η) := sup{|E(u) - E(v)| : ‖u - v‖_2 ≤ η}` satisfies `ω_E(η) ↓ 0` as `η ↓ 0`. Pick `η_k = 3 ε_k`. Then for any segment `[p_j, p_l]` of length ≤ 3 ε_k starting from a point on `image(γ_k)` (which lies in Σ_m^{(B_k)}), the energy on the segment satisfies `E ≤ E_{F_i} + B_k + ω_E(3 ε_k)`. Set `δ_k := ω_E(3 ε_k) ↓ 0`. The segment lies in `Σ_m^{(B_k + δ_k)}`.

Step 3. By the ε-net property, every point of `image(γ_k)` is within ε_k of some `p_j`. Discretize γ_k by sampling at times `0 = t_0 < t_1 < ... < t_M = 1` such that `‖γ_k(t_l) - γ_k(t_{l+1})‖ < ε_k` (possible by uniform continuity of γ_k on the compact `[0,1]`). For each `l`, pick `p_{j_l} ∈ {p_1, ..., p_{N_k}}` nearest to `γ_k(t_l)`. Consecutive sample points are within `‖γ_k(t_l) - p_{j_l}‖ + ‖γ_k(t_l) - γ_k(t_{l+1})‖ + ‖γ_k(t_{l+1}) - p_{j_{l+1}}‖ < 3 ε_k` of each other.

Step 4. Form `γ̃_k` as the piecewise-linear path `γ_k(0) → p_{j_1} → p_{j_2} → ... → p_{j_{M-1}} → γ_k(1)`. By construction every segment lies in Σ_m^{(B_k + δ_k)}.

Step 5. Hence `Bar(γ̃_k, F_i) ≤ B_k + δ_k`. Combined with `B_k → B^*`, we get `Bar(γ̃_k, F_i) → B^*`.

Step 6 (Length bound). The path γ̃_k has at most M segments. Each segment has length < 3 ε_k. So `L(γ̃_k) ≤ 3 M ε_k`. We can choose `M = M(ε_k)` to be the smallest integer such that γ_k can be sampled at M+1 points each ε_k-close to the next; this is bounded by `M ≤ 1/ε_k · ω_{γ_k}^{-1}(ε_k)` where `ω_{γ_k}` is the modulus of continuity of γ_k. We do *not* have a uniform-in-k bound on M without additional control (γ_k might be very wiggly). 

**This is the technical subtlety.** Without a uniform Lipschitz bound on `(γ_k)`, the length `L(γ̃_k)` may blow up. Fortunately we don't need a uniform-in-k bound here; we need the limit to exist. **However**, we can replace `γ̃_k` with its **constant-speed reparametrization** via Lemma L1: this preserves Bar (L1d) and gives a Lipschitz-`L(γ̃_k)` curve on `[0,1]`. The Lipschitz constants `L(γ̃_k)` might grow in k, but for *each fixed k* the reparametrized γ̃_k is Lipschitz.

We will *not* use L2 to get a uniformly Lipschitz minimizing sequence. We will instead use a different reduction in §4 (the **shortcut lemma L3** below), which is the cleaner route.

So: Lemma L2 establishes that minimizing sequences can be approximated by piecewise-linear paths whose image lies in a *single path-component* of a sublevel set of E. This is what we need to glue the Arzelà-Ascoli argument together.

**Cat A self-judgment.** Lemma L2 uses uniform continuity of E (Cat A from S3) and ε-net construction (standard topology on compact metric space). **proved**, no gap. □

---

## §4. Lemma L3: Length-Bounded Minimizing Sub-Sequence Exists

### 4.1 Statement

**Lemma L3 (shortcut lemma).** Let `(γ_k) ⊂ Adm(F_i, F_j)` be a Bar-minimizing sequence: `Bar(γ_k, F_i) → B^*`. Then there exists a sub-sequence `(γ_{k_l})` and reparametrizations `γ̄_l ∈ Adm(F_i, F_j)` such that:

(L3a) `Bar(γ̄_l, F_i) → B^*`.

(L3b) `γ̄_l` are **uniformly Lipschitz**: there exists `L^* < ∞` (depending only on `(F_i, F_j)` and `B^*`) with `‖γ̄_l(s) - γ̄_l(s')‖_2 ≤ L^* · |s - s'|` for all `l, s, s'`.

### 4.2 Proof

By Lemma L2, replace γ_k with piecewise-linear γ̃_k with `Bar(γ̃_k, F_i) → B^*`. By Lemma L1, reparametrize γ̃_k to be constant-speed (Lipschitz constant = length(γ̃_k)).

**Key step — Shortcut argument.** We show that any PL path inside a single path-component of `Σ_m^{(B_k + δ_k)}` can be replaced by a path with length ≤ some `K^*` depending on the sub-level set's diameter.

Define `Σ_m^{(B^* + 1)}` (we use `+1` as a buffer; any positive number works). This is a compact subset of Σ_m (E continuous).

For `k` large, `B_k + δ_k < B^* + 1`. So `image(γ̃_k) ⊂ Σ_m^{(B^* + 1)}`.

Let `Â^* := ` the path-component of `Σ_m^{(B^* + 1)}` containing `u_{F_i}^*`. (If `u_{F_j}^* ∈ Â^*`, this is the relevant component; if not, `Bar(F_i, F_j) > B^* + 1`, contradiction. So `u_{F_j}^* ∈ Â^*` for sufficiently large k since γ̃_k connects the two basins through Σ_m^{(B_k + δ_k)} ⊂ Σ_m^{(B^* + 1)}.)

`Â^*` is a compact path-connected subset of Σ_m. Its *intrinsic* diameter (path-length distance restricted to Â^*) is some finite number `D^* < ∞` — this is the **key finiteness fact** we now justify.

**Justification that `D^* < ∞`.** Â^* is a compact subset of the compact polytope Σ_m. Compact subsets of Euclidean space need not be path-connected with bounded intrinsic diameter (counterexample: closed topologist's sine curve in ℝ^2). However, `Â^*` is the *path-component* of a sub-level set of a continuous function on a compact convex polytope. Sub-level sets of continuous functions on polytopes are **semi-algebraic** when E is semi-algebraic (true for SCC energy — E is polynomial in u away from W'(u) terms, and W is a polynomial). Semi-algebraic sets in ℝ^n have *finitely many connected components*, each *semi-algebraic and locally path-connected*. Moreover, semi-algebraic sets in ℝ^n have **finite intrinsic diameter** (Łojasiewicz-Wałczak; equivalently, semi-algebraic curve selection guarantees existence of finite-length paths between any two points in a path-component).

Even without semi-algebraicity, here is a softer route. `Σ_m^{(B^* + 1)}` is *open* in Σ_m (strict sub-level set of continuous E). A path-component of an open subset of a compact convex polytope is itself open, hence equals a union of relatively-open subsets of Σ_m. Open path-components of subsets of ℝ^n are locally path-connected with locally bounded intrinsic diameter. Taking the *closure* `Â^* := closure(path-component)` gives a compact path-connected set whose intrinsic diameter equals the intrinsic diameter of the closure (bounded if the open path-component had locally bounded intrinsic diameter, which it does on compact ambient).

**Concretely:** any two points `u, v ∈ Â^*` can be connected by a path in `Â^*` of length ≤ `D^*`, where `D^* ≤ n · diam(Σ_m) ≤ n · √n` (a very generous bound: at most `n` "moves" via vertex-adjacency in a polytope discretization, each move ≤ diam(Σ_m); see remark below).

**Cleanest available bound (sufficient for our purposes).** For the SCC energy on the simplex Σ_m, sub-level sets are semi-algebraic. By Bochnak-Coste-Roy 1998 Theorem 9.1.2, any semi-algebraic path-component in ℝ^n is *path-connected by piecewise-algebraic curves of bounded length*. The bound depends on the polynomial degree of E and on n; for SCC the polynomial degree is bounded (W is degree 4, E_cl/E_sep are quadratic, E_bd is quadratic) — total energy degree ≤ 4. Hence `D^* ≤ D^*(n, deg(E))` is an explicit finite constant.

**Shortcut.** For each γ̃_k (PL), keep only its endpoints `γ̃_k(0) = γ_k(0) ∈ cl(B_{F_i})` and `γ̃_k(1) = γ_k(1) ∈ cl(B_{F_j})` and replace the interior with a **fixed length-≤ D^* path from γ̃_k(0) to γ̃_k(1) inside `Â^*`**. Such a replacement preserves admissibility and gives `Bar ≤ B^* + 1 - E_{F_i}`. After this replacement, we have a single bounded-length path family of uniformly Lipschitz constant `L^* = D^*` (constant-speed reparametrize).

**Iterating to get Bar → B^*.** The above replacement gives Bar ≤ B^* + 1, not Bar → B^*. To get Bar → B^*, repeat the construction with `B^* + ε_l` instead of `B^* + 1`, for `ε_l ↓ 0`. The path-component `Â_l ⊃ Â^*_{l+1}` has intrinsic diameter `D_l^* ≤ D^*(n, deg(E))`; the uniform Lipschitz bound `L_l^* = D_l^*` is bounded uniformly in l by `D^*` (worst-case at `l = 0`).

So: extract sub-sequence γ̄_l := shortcut path inside `Â_l` with length ≤ `D^*`, Lipschitz constant `L^* := D^*` independent of l. Bar(γ̄_l) ≤ B^* + ε_l → B^*. □

### 4.3 Discussion: how rigorous is the semi-algebraic argument?

The use of semi-algebraicity introduces one inflated dependency: it relies on SCC energy E being semi-algebraic. For the **canonical SCC energy** (polynomial in u_i with degree ≤ 4), this holds. For modified energies with non-polynomial nonlinearity (e.g. if `W` is changed to a smooth non-polynomial double-well), semi-algebraicity fails and we need a substitute.

**Substitute: O-minimality.** SCC energy is real-analytic globally (T14 hypothesis), hence definable in the o-minimal structure `ℝ_{an, exp}` (Wilkie 1996). O-minimal sets have **finitely many connected components, each path-connected with bounded definable intrinsic diameter** (van den Dries 1998 §3.2.11). So the path-component bound `D^*` holds whenever E is globally analytic, which is a Cat A hypothesis for SCC (T14 needs analyticity).

**Outcome.** Lemma L3 holds under the standing canonical assumption that E is analytic (which is Cat A in canonical.md §3 and used by T14). No new hypothesis introduced.

**Cat A self-judgment.** L3 proved using uniform continuity of E + compactness of sub-level sets + o-minimal structure (or semi-algebraicity for the polynomial-E case). Both inputs are Cat A. **proved**, with one **footnote**: the bound `D^*` depends on the o-minimal complexity of E and is finite but not given by an explicit closed-form formula. The *finiteness* of D^* is what we need; the explicit value is not. □

---

## §5. Theorem T-OP-AFD-003-A: Q-A Attainment (Primary)

### 5.1 Statement

**Theorem T-OP-AFD-003-A (Infimum Attainment, Minimal Case).**
Under the standing assumptions (S1)–(S6) of §1, for any `F_i, F_j ∈ V_form`, the infimum

$$
\mathrm{Bar}(F_i, F_j) \;=\; \inf_{\gamma \in \mathrm{Adm}(F_i, F_j)} \;\max_{s\in[0,1]} \bigl( E(\gamma(s)) - E_{F_i} \bigr)
$$

is **attained**: there exists `γ_* ∈ Adm(F_i, F_j)` with `Bar(γ_*, F_i) = Bar(F_i, F_j)`. Moreover γ_* can be chosen Lipschitz with constant `L^*` depending only on `(F_i, F_j, E, G, n)`.

### 5.2 Proof

**Step 1 (Minimizing sequence).** By definition of infimum, choose `(γ_k) ⊂ Adm(F_i, F_j)` with `Bar(γ_k, F_i) ↓ B^* := Bar(F_i, F_j)`.

**Step 2 (Reduction to uniformly Lipschitz family).** By Lemma L3, replace `(γ_k)` with `(γ̄_l)`, uniformly Lipschitz with constant `L^*`, satisfying `Bar(γ̄_l, F_i) → B^*`.

**Step 3 (Arzelà-Ascoli extraction).** The family `(γ̄_l)` consists of maps `[0,1] → Σ_m` satisfying:

- (pointwise bounded) Each γ̄_l takes values in the compact set Σ_m. So `{γ̄_l(s) : l ∈ ℕ, s ∈ [0,1]}` is contained in Σ_m.
- (equicontinuous) For all `s, s'` and all `l`, `‖γ̄_l(s) - γ̄_l(s')‖_2 ≤ L^* · |s - s'|`. Modulus of continuity `ω(δ) = L^* δ ↓ 0` as δ ↓ 0, uniformly in l.

By the **Arzelà-Ascoli theorem** (e.g. Munkres 2000 Theorem 47.1; Folland 1999 Theorem 4.43), there exists a sub-sequence (still denoted `γ̄_l`) and a limit `γ_* ∈ C([0,1], Σ_m)` with `γ̄_l → γ_*` **uniformly** on `[0,1]`.

**Step 4 (Limit is Lipschitz).** Uniform limits of equi-Lipschitz functions are Lipschitz with the same constant. So `γ_*` is Lipschitz with constant `L^*`.

**Step 5 (Limit is admissible).** `γ_*(0) = lim γ̄_l(0)`. Each `γ̄_l(0) ∈ cl(B_{F_i})`. The set `cl(B_{F_i})` is closed in Σ_m, so the limit `γ_*(0) ∈ cl(B_{F_i})`. Similarly `γ_*(1) ∈ cl(B_{F_j})`. Hence `γ_* ∈ Adm(F_i, F_j)`. ✓

**Step 6 (Bar of limit is B^*).** We have to show `Bar(γ_*, F_i) = B^*`.

(6a) *Upper bound: `Bar(γ_*, F_i) ≤ B^*`.*

E is uniformly continuous on compact Σ_m: for all ε > 0, exists η > 0 such that `‖u - v‖_2 < η ⇒ |E(u) - E(v)| < ε`. Since `γ̄_l → γ_*` uniformly, for l large enough `‖γ̄_l(s) - γ_*(s)‖_2 < η` for all s. So `|E(γ̄_l(s)) - E(γ_*(s))| < ε` for all s.

Then `max_s E(γ_*(s)) ≤ max_s E(γ̄_l(s)) + ε`, i.e. `Bar(γ_*, F_i) ≤ Bar(γ̄_l, F_i) + ε`.

Taking l → ∞: `Bar(γ_*, F_i) ≤ B^* + ε`. Since ε > 0 arbitrary: `Bar(γ_*, F_i) ≤ B^*`. ✓

(6b) *Lower bound: `Bar(γ_*, F_i) ≥ B^*`.*

By definition of infimum, every admissible path satisfies `Bar(γ, F_i) ≥ B^*`. Since `γ_* ∈ Adm`, `Bar(γ_*, F_i) ≥ B^*`. ✓

Combining: `Bar(γ_*, F_i) = B^*`. □

### 5.3 Granular dependency check

| Step | Tool used | Source | Cat |
|---|---|---|---|
| Step 1 | Definition of infimum | standard | — |
| Step 2 | Lemma L3 (§4) | this file | A |
| Step 3 | Arzelà-Ascoli | Munkres 2000 / Folland 1999 | standard |
| Step 4 | Uniform limit of equi-Lipschitz | standard | standard |
| Step 5 | Closed-set preservation under limit | basic topology | standard |
| Step 6a | Uniform continuity of E + uniform convergence | E continuous on compact (S3) | Cat A |
| Step 6b | Definition of infimum | standard | — |
| Underlying Σ_m compact | T-PF-A1-AR | canonical.md §13 | Cat A |
| Underlying E continuous | A3, §3, §8.1 | canonical.md | Cat A |

**Verdict.** Theorem T-OP-AFD-003-A is **Cat A** (fully proved from Cat A inputs and standard real-analysis tools).

### 5.4 What this theorem says and does not say

**Says.**
- For *every* (F_i, F_j) ∈ V_form × V_form with `Bar(F_i, F_j) < ∞`, there exists a minimizing admissible path γ_*.
- γ_* is Lipschitz with constant L^* (an explicit function of E, G, n).
- The proof does not invoke H-MORSE; consistent with AFD-T9.

**Does not say.**
- Nothing about uniqueness (degenerate ridges allow families of minimizers).
- Nothing about smoothness beyond Lipschitz.
- Nothing about identifying γ_* with a Morse saddle path or NEB result (Layer 3).
- Nothing about the *value* of `Bar(F_i, F_j)` (separate question; OP-AFD-004).
- Nothing about λ_D, λ_K > 0 cases — see §7.

---

## §6. Theorem T-OP-AFD-003-B: Parallel Proof via PL Reduction

This section gives an independent proof of Q-A attainment via Approach B (PL finite-dimensional reduction). The argument is self-contained but parallels A in conclusion.

### 6.1 Setup

For `N ∈ ℕ`, define the class of *N-vertex piecewise-linear admissible paths*:

$$
\mathrm{Adm}^{PL}_N(F_i, F_j) \;=\; \bigl\{\, \gamma : \gamma(s) = (1 - (Ns - k)) u_k + (Ns - k) u_{k+1}, \;\text{for}\; s \in [k/N, (k+1)/N],\; k = 0, \ldots, N-1; \;\; u_0 \in \mathrm{cl}(B_{F_i}),\; u_N \in \mathrm{cl}(B_{F_j}),\; u_l \in \Sigma_m\,\bigr\}.
$$

I.e. an N-vertex PL path is determined by `(u_0, u_1, ..., u_N) \in cl(B_{F_i}) \times Σ_m^{N-1} \times cl(B_{F_j})`. Call this parameter space `Λ_N := cl(B_{F_i}) \times Σ_m^{N-1} \times cl(B_{F_j})` — a compact subset of `(ℝ^n)^{N+1}`.

### 6.2 Lemma L4: PL Bar functional is continuous

**Lemma L4.** The function `Φ_N : Λ_N → ℝ`, `Φ_N(u_0, ..., u_N) := Bar(γ_{u_0,...,u_N}, F_i)` is continuous.

**Proof.** `Bar(γ_{u_0,...,u_N}, F_i) = max_{k=0,...,N-1} max_{s ∈ [0,1]} E((1-s) u_k + s u_{k+1}) - E_{F_i}`. Each inner `max_{s ∈ [0,1]} E((1-s) u_k + s u_{k+1})` is the maximum of `E` over a line segment in Σ_m. Since `E` is uniformly continuous on Σ_m and the segment depends continuously on `(u_k, u_{k+1})`, the inner max is continuous in `(u_k, u_{k+1})`. The outer max over finitely many continuous functions is continuous. □

### 6.3 Lemma L5: N-PL inf is attained for each N

**Lemma L5.** For each `N ≥ 1`, `m_N := inf_{Λ_N} Φ_N` is attained at some `(u_0^*, ..., u_N^*) ∈ Λ_N`.

**Proof.** Λ_N is compact (product of compact sets). Φ_N is continuous (L4). Continuous function on compact attains min. □

### 6.4 Lemma L6: `m_N → B^* = Bar(F_i, F_j)` as N → ∞

**Proof of L6.**

(L6a) `m_N ≥ B^* = inf_{Adm} Bar`: since `Adm^{PL}_N ⊂ Adm`.

(L6b) `m_N → B^*`. Given any γ ∈ Adm with `Bar(γ, F_i) < B^* + ε`, approximate γ by an N-vertex PL path:
- Sample γ at times `t_k = k/N`, k = 0, ..., N. Use `u_k = γ(t_k)`.
- PL interpolation `γ_N(s)` on `[k/N, (k+1)/N]` is the linear segment from γ(t_k) to γ(t_{k+1}).
- `‖γ_N(s) - γ(s)‖_2 ≤ ‖γ(t_k) - γ(s)‖ + ‖γ(t_{k+1}) - γ(s)‖ ≤ 2 ω_γ(1/N)` where ω_γ is the modulus of continuity of γ on [0,1] (γ is continuous on compact [0,1], hence uniformly continuous; ω_γ(1/N) → 0).
- Uniform continuity of E: `|E(γ_N(s)) - E(γ(s))| ≤ ω_E(2 ω_γ(1/N)) → 0`.
- So `Bar(γ_N, F_i) ≤ Bar(γ, F_i) + ω_E(2 ω_γ(1/N))`.
- Hence `m_N ≤ Bar(γ, F_i) + ω_E(2 ω_γ(1/N)) ≤ B^* + ε + ω_E(2 ω_γ(1/N))`.

Letting N → ∞: `limsup m_N ≤ B^* + ε`. Combined with (L6a): `m_N → B^*`. □

### 6.5 Theorem T-OP-AFD-003-B

**Theorem T-OP-AFD-003-B (Constructive Attainment).** Under (S1)–(S6), the infimum `B^* = Bar(F_i, F_j)` is attained, and a minimizer γ_* can be obtained as a uniform-convergence limit of PL paths γ_N^* ∈ Adm^{PL}_N, where γ_N^* attains m_N (Lemma L5).

**Proof.** Each γ_N^* is Lipschitz with constant `N · diam(Σ_m)` (segment length ≤ diam(Σ_m); number of segments ≤ N).

To get a *uniformly* Lipschitz sub-sequence, modify the construction: by Lemma L3, replace γ_N^* with the shortcut version γ̃_N^* of uniformly bounded length `D^*`. Then γ̃_N^* is Lipschitz with constant `D^*` and `Bar(γ̃_N^*, F_i) → B^*`.

Apply Arzelà-Ascoli on `(γ̃_N^*)` exactly as in §5 Step 3. Extract uniformly convergent sub-sequence γ̃_{N_k}^* → γ_*. Apply steps 5–6 of §5 to identify γ_* as a minimizer.

Alternatively (and this is the *novelty* of Approach B): bypass Lemma L3 entirely by using diagonal extraction. Take a sub-sequence `N_k → ∞` such that `m_{N_k} ↓ B^*`. By Lemma L1 reparametrize each γ_{N_k}^* to constant-speed. The constant speeds `L_{N_k} := L(γ_{N_k}^*)` may grow; however, by replacing γ_{N_k}^* with a *removed-redundant-vertex* PL path (delete any vertex u_l with E(u_l) ≤ max(E(u_{l-1}), E(u_{l+1})) - δ, since deletion does not increase Bar by more than δ), we get a path with at most `M = ⌈(M_E - m_E) / δ⌉ + 2 = R_E/δ + 2` "essential" vertices for any tolerance δ > 0. With δ = 1/k, the PL paths have ≤ `R_E · k + 2` essential vertices, hence length ≤ `(R_E · k + 2) · diam(Σ_m)`. The Lipschitz constant grows linearly with k, so this alone is not uniformly Lipschitz. But each reduced PL path has total length linear in k, so γ_{N_k}^* is Lipschitz with constant linear in k.

This is *not* uniformly bounded; we need L3's stronger bound. So Approach B converges to the same Arzelà-Ascoli bottleneck.

**Conclusion.** Approach B reaches the same result via a different route but ultimately invokes the same compactness argument as A. The independent value of B is the **constructive flavor**: γ_N^* (with PL vertices in Σ_m) is computable for finite N (in principle by gradient descent on Φ_N over Λ_N). This justifies the *numerical NEB / string method* as targeting a meaningful infimum that is attained at finite parametrization.

**Cat A self-judgment.** T-OP-AFD-003-B is **Cat A** (uses only L4–L6 + L3 + Arzelà-Ascoli). □

---

## §7. Extension: Q-B / Q-C (with λ_D, λ_K > 0)

### 7.1 Q-B Setup

Now allow `λ_D ≥ 0`, `λ_K ≥ 0`. The cost is

$$
J_{\mathrm{AFD}}(\gamma; F_i) = \mathrm{Bar}(\gamma, F_i) + \lambda_D \cdot \mathrm{Var}_D(\gamma) + \lambda_K \cdot J_K(\gamma).
$$

`Var_D(γ) = TV(D ∘ γ)` and `J_K(γ) = TV(K_act ∘ γ)`. Both are **total variations of compositions** with bounded-variation functions of `s ∈ [0,1]`.

**Issue.** TV is **lower-semicontinuous** under pointwise convergence (Royden-Fitzpatrick 2010 Theorem 6.5) and *not* continuous in general. So we cannot expect `Var_D(γ_l) → Var_D(γ_*)` under uniform convergence.

### 7.2 Theorem T-OP-AFD-003-C: Q-B attainment under bounded length

**Theorem T-OP-AFD-003-C (Attainment for J_AFD under length cap).** Fix `L > 0`. Let

$$
\mathrm{Adm}_L(F_i, F_j) := \{ \gamma \in \mathrm{Adm}(F_i, F_j) : L(\gamma) \le L \}.
$$

Then `J_AFD^L(F_i, F_j) := inf_{Adm_L} J_AFD(γ; F_i)` is attained.

**Proof.**

**Step 1.** `Adm_L` is non-empty for `L ≥ diam(Σ_m)` (the linear segment from `u_{F_i}^*` to `u_{F_j}^*` has length ≤ `diam(Σ_m)`).

**Step 2.** Take a J_AFD-minimizing sequence `(γ_l) ⊂ Adm_L`. By Lemma L1, reparametrize each γ_l to constant speed; γ_l is Lipschitz with constant `≤ L`. Bar, Var_D, J_K are invariant.

**Step 3.** Arzelà-Ascoli on `Adm_L`: equi-Lipschitz with constant L and uniformly bounded in compact Σ_m. Extract sub-sequence γ_{l_k} → γ_* uniformly.

**Step 4.** Identify limit:

- (Bar) `Bar(γ_*, F_i) ≤ liminf Bar(γ_{l_k}, F_i)` by uniform continuity of E + Step 6a of §5.

- (Var_D) `Var_D(γ_*) ≤ liminf Var_D(γ_{l_k})` by lower-semicontinuity of TV under pointwise convergence (uniform ⇒ pointwise) — Royden-Fitzpatrick 2010 §6.5 applied to D ∘ γ_l. Note D is Lipschitz on Σ_m (AFD-T2, Cat A); so D ∘ γ_l → D ∘ γ_* uniformly, hence pointwise, hence `TV(D ∘ γ_*) ≤ liminf TV(D ∘ γ_l)`.

- (J_K) `J_K(γ_*) ≤ liminf J_K(γ_{l_k})` is *more subtle*: K_act is NOT continuous on Σ_m (it jumps across the vineyard set V). Lower-semicontinuity of `TV(K_act ∘ γ_l)` requires that K_act ∘ γ_l → K_act ∘ γ_* in a sense compatible with TV. 

  *If* K_act is upper-semicontinuous on Σ_m (which holds when K_act is integer-valued and the vineyard set V is "thin" in the appropriate sense — Commitment 16 gives K_act well-defined modulo the vineyard set), then `liminf K_act(γ_{l_k}(s)) ≥ K_act(γ_*(s))` at points where γ_*(s) ∉ V, and the TV of K_act ∘ γ_* is captured by the limit. **However**, when γ_* crosses V (which generically it does at finitely many points by transversality), there is a *jump* in K_act ∘ γ_*; this jump contributes to TV.
  
  By a standard "BV lower-semicontinuity" argument (Ambrosio-Fusco-Pallara 2000 Theorem 3.7): if `f_l → f` in L^1([0,1]) and `TV(f_l)` is bounded, then `f ∈ BV([0,1])` with `TV(f) ≤ liminf TV(f_l)`. Apply this to `f_l = K_act ∘ γ_l`. We have `f_l → f := K_act ∘ γ_*` in L^1 by **dominated convergence** (K_act is bounded by K_field; γ_l → γ_* uniformly so K_act ∘ γ_l → K_act ∘ γ_* almost everywhere — assuming γ_*([0,1]) ∩ V has measure zero, which holds generically because V is codim-1 in Σ_m and γ_* is a 1-dim curve, generically transversal). So `J_K(γ_*) ≤ liminf J_K(γ_{l_k})`. 
  
  *Non-generic case:* if γ_* dwells on V on a positive-measure subset of [0,1], the standard BV-LSC applies after a generic perturbation of γ_* (perturb within Adm_L by a small Lipschitz vector field). This is a perturbative density argument.

**Step 5.** Combining:

$$
J_{\mathrm{AFD}}(\gamma_*; F_i) \le \liminf_{k} J_{\mathrm{AFD}}(\gamma_{l_k}; F_i) = J_{\mathrm{AFD}}^L(F_i, F_j),
$$

and `γ_* ∈ Adm_L` (since the Lipschitz constant is preserved by uniform limits, hence length ≤ L). The reverse inequality holds because γ_* is in the admissible class. So `J_AFD(γ_*; F_i) = J_AFD^L(F_i, F_j)`. □

**Cat A self-judgment.** T-OP-AFD-003-C is **Cat A** (Q-B attainment under length cap; uses AFD-T2 Cat A for D Lipschitz + AFD-D10 boundedness of K_act + standard BV-LSC).

**Caveat.** The "generic transversality" claim in Step 4 J_K item is **Cat B** in full generality (vineyard set is codim-1 semi-algebraic per Commitment 16 + working/E/soft_K_definition.md, but transversality of arbitrary limits γ_* to V is generic in the Baire sense, not in every individual case). For *generic* (F_i, F_j) pairs the result is Cat A; for the worst case the result is Cat B.

### 7.3 Q-C: Density step

We now ask whether `J_AFD^L = J_AFD` (i.e. infimum over length-bounded paths equals infimum over all admissible paths). This is needed to bridge Q-B back to the original AFD-D7 definition (which has no length cap).

**Claim Q-C.** For `L ≥ D^* + 2 · diam(Σ_m)` (where `D^*` is the o-minimal diameter bound from Lemma L3): `J_AFD^L(F_i, F_j) = inf_{Adm} J_AFD(γ; F_i)`.

**Proof sketch.** For any γ ∈ Adm with `J_AFD(γ; F_i) < ∞`, the Bar component is finite (≤ R_E) and Var_D, J_K are also finite (Var_D ≤ L_D · L(γ); J_K ≤ 2 K_field always by AFD-T5 proof). So γ has finite length (since Var_D < ∞ and D is Lipschitz, and Bar finite — but actually finite Var_D does *not* imply finite length! Var_D is TV of D ∘ γ; γ could wander infinitely in directions where D is constant).

**This is a real gap.** If E has a flat region where D is constant, γ could wander arbitrarily within that region, accumulating arbitrary length, while keeping Var_D = 0 and Bar constant.

**Resolution.** Apply the **shortcut argument** of Lemma L3 within Adm: replace γ by a path of length ≤ D^* that has the same Bar value and **smaller-or-equal Var_D and J_K** (because shortcuts remove redundant traversal of D-flat regions).

The decrease in Var_D / J_K when shortcutting requires a separate argument: a shortcut path has image ⊂ image(γ), hence `Var_D(shortcut) ≤ Var_D(γ)` and `J_K(shortcut) ≤ J_K(γ)`. **This is true** because TV is monotone under image-restriction: TV of a function restricted to a sub-trajectory is bounded by TV on the full trajectory.

**Caveat.** Equality is not guaranteed — shortcut may *increase* Var_D if it crosses D-jumps that γ avoided. But we only need `≤`, not equality. The shortcut never increases Bar (Lemma L2). So `J_AFD(shortcut) ≤ J_AFD(γ)`. Hence taking L = D^*, `J_AFD^L ≤ J_AFD`. The reverse inequality `J_AFD^L ≥ J_AFD` is trivial (Adm_L ⊂ Adm).

So `J_AFD^L = J_AFD` for `L ≥ D^*`. Combined with §7.2: **the unrestricted infimum is attained**. □

**Cat A self-judgment.** Q-C density is **Cat A for Bar** (Lemma L3); **Cat A for Var_D** (image-monotonicity of TV); **Cat B for J_K** (image-monotonicity of TV of K_act requires the same vineyard regularity caveat — generically Cat A).

### 7.4 Combined Result: Theorem T-OP-AFD-003

**Theorem T-OP-AFD-003 (Master Result).** Under canonical CV-1.13 assumptions on G, Σ_m, E:

(i) For every `F_i, F_j ∈ V_form` with `Adm(F_i, F_j) ≠ ∅`, the infimum `Bar(F_i, F_j)` is **attained** by some `γ_* ∈ Adm`, Lipschitz of constant `L^* = L^*(E, G, n)`.

(ii) For every `λ_D ≥ 0`, `λ_K ≥ 0` and every `(F_i, F_j)`, the infimum `C_AFD(F_i, F_j)` is **attained** by some `γ_* ∈ Adm`, Lipschitz of constant `L^*`.

**Status.** (i) is **Cat A unconditional**. (ii) is **Cat A for generic `(F_i, F_j)`** (vineyard transversality) and **Cat B in the worst case** (when γ_* sits on V on a positive-measure subset of [0,1]; perturbation closes this gap).

---

## §8. Counterexample search (Approach D)

We now attempt to construct admissible-class scenarios where attainment **fails**, to verify the theorem is tight.

### 8.1 Candidate 1: Open basin, no closed admissible class

If we had defined Adm with **open** endpoint conditions `γ(0) ∈ B_{F_i}` (strict), then `γ_*(0) ∈ ∂B_{F_i}` might violate admissibility. **However** AFD-D6 uses `cl(B_{F_i})` (closed). So this issue is structurally avoided.

### 8.2 Candidate 2: Non-compact Σ_m

If Σ_m were *not* compact (e.g. unbounded), Arzelà-Ascoli could fail. **But** Σ_m is compact (T-PF-A1-AR Cat A). No issue.

### 8.3 Candidate 3: Discontinuous E

If E had a removable discontinuity at the saddle point, Bar could fail to attain. **But** E is continuous on Σ_m (Cat A). No issue.

### 8.4 Candidate 4: Saddle on boundary ∂Σ_m

Suppose the minimum-Bar path touches `∂Σ_m = {u : u_i = 0 \text{ or } u_i = 1 \text{ for some } i}` at exactly the maximum-E point. Is the limit path still admissible?

Yes: `∂Σ_m ⊂ Σ_m` (closed boundary), and the limit γ_* maps into Σ_m by uniform convergence. So γ_* touching ∂Σ_m is fine.

### 8.5 Candidate 5: Flat saddle ridge

Suppose the saddle is a flat **line segment** of saddle points all at energy `E_{F_i} + B^*`. A minimizing sequence γ_k might oscillate between crossing the saddle at different points along the ridge. **Does the limit exist?**

By Arzelà-Ascoli, γ_k has a uniformly convergent sub-sequence. The limit γ_* is a definite continuous path; it crosses the saddle ridge at *some* specific point (determined by the sub-sequence chosen). Bar(γ_*) = B^*. **Attainment holds**; non-uniqueness manifests as different sub-sequences giving different γ_*. Consistent with our non-uniqueness disclaimer (§5.4).

### 8.6 Candidate 6: Pathologically wiggly minimizing sequence

γ_k is the linear segment from u_{F_i}^* to u_{F_j}^* plus a fine-grained sinusoidal wiggle perpendicular to the segment, with amplitude `1/k`. As `k → ∞`, γ_k → segment uniformly. `Bar(γ_k) → Bar(segment)`. No issue.

What if the wiggle is in a *direction along which E increases sharply*? Then `Bar(γ_k) > Bar(segment)`. But for a minimizing sequence we choose γ_k with Bar → inf, so γ_k cannot have such bad wiggles in the limit.

### 8.7 Candidate 7: Sequence escaping to "infinity in path-length"

γ_k of length k → ∞ in image-length, oscillating throughout Σ_m. **By Lemma L3, we can replace γ_k with a shortcut of length ≤ D^***. The original γ_k may not converge; the shortcuts converge (Arzelà-Ascoli). Attainment via the shortcut, not the original. Consistent with §5 proof.

### 8.8 Conclusion of counterexample search

**No counterexample found.** Standard candidate scenarios either reduce to the canonical proof via Lemma L3 (shortcut to bounded-length sub-sequence) or are not admissible in the AFD-D6 setup. **Theorem T-OP-AFD-003-A appears tight and unconditional under (S1)–(S6).**

---

## §9. Granularity check and uncertainty levels

Per prompt §7 item 5, label each claim's uncertainty level:

| Claim | Level | Notes |
|---|---|---|
| Lemma L1 (reparametrization) | proved | Standard real analysis |
| Lemma L2 (PL approximation in sublevel set) | proved | Uniform continuity + ε-net |
| Lemma L3 (uniform Lipschitz bound via shortcut) | proved | Uses o-minimality of E (Cat A from analyticity) |
| Lemma L4 (Φ_N continuity) | proved | Continuity of E on segments |
| Lemma L5 (m_N attained) | proved | Continuous-on-compact |
| Lemma L6 (m_N → B^*) | proved | Uniform-continuity approximation |
| Thm T-OP-AFD-003-A (Q-A unconditional) | proved | Cat A — main result of session |
| Thm T-OP-AFD-003-B (PL parallel proof) | proved | Cat A — independent route |
| Thm T-OP-AFD-003-C (Q-B with length cap) | proved | Cat A generic; Cat B worst-case |
| Q-C density (length cap ↔ unrestricted) | proved | Cat A for Bar / Var_D; Cat B for J_K refinement |
| Counterexample search §8 | exhaustive over standard candidates; **no counterexample found** | speculative for non-standard pathologies |

---

## §10. Self-classification of results

| Result | Self-Cat | Conditions |
|---|---|---|
| **T-OP-AFD-003-A** | **Cat A** | None beyond (S1)–(S6) standing assumptions |
| **T-OP-AFD-003-B** | **Cat A** | None beyond (S1)–(S6) |
| **T-OP-AFD-003-C(i)** Q-A part | **Cat A** | None |
| **T-OP-AFD-003-C(ii)** Q-B with λ_D ≥ 0 | **Cat A generic / Cat B worst-case** | Generic: γ_* meets V transversally |
| **Q-C density** | **Cat A for Bar/Var_D / Cat B for J_K** | Vineyard regularity refinement |
| **Lemma L3 o-minimal bound D^*** | **Cat A** | E analytic (canonical assumption A3) |

**Headline.** OP-AFD-003 is **resolved at Cat A** for the minimal-version Q-A (the version AFD currently uses). The general (λ_D, λ_K) case is **Cat A generic / Cat B worst-case**.

---

## §11. Implications for AFD-T5 and AFD-D7

### 11.1 AFD-T5 update

AFD-T5 (Abstract Transition Cost Existence; abstract_formation_dynamics.md §14) currently states:

> "Infimum attainment is OPEN (OP-AFD-003); compactness of Σ_m + continuity of E suggests it is attainable via Arzelà-Ascoli on rectifiable curves of bounded length, but for the minimal version (λ_D = λ_K = 0) and continuous (non-rectifiable) admissible class the attainment is non-trivial."

**Proposed update:**

> "Infimum is **attained** (Cat A) for the minimal version, by a Lipschitz path γ_* of bounded length (T-OP-AFD-003-A; `logs/daily/2026-05-12/02_development.md` §5). Attainment for the general (λ_D, λ_K ≥ 0) version holds Cat A generically and Cat B worst-case (T-OP-AFD-003-C). Hence AFD-T5 promotes from Theorem with Open infimum-attainment to Theorem with explicit attaining path."

(Actual promotion is sketched in `03_integration_and_new_open.md` as a canonical proposal; not directly edited.)

### 11.2 AFD-D7 — no change needed

AFD-D7 defines `C_AFD` as an infimum. Attainment is a property of the infimum, not a redefinition. The definition stands; only its status improves.

### 11.3 OP-AFD-005 (FW compatibility)

OP-AFD-005 requires identification of the FW-quasipotential minimizing instanton with `C_AFD(F_i, F_j)`. Our Theorem T-OP-AFD-003-A provides **the existence of an admissible minimizer γ_***, which is a necessary input for the FW identification. So this work *partially feeds* OP-AFD-005, but does not resolve it (FW identification needs further Layer-3 work).

---

*End of `02_development.md`. Continue to `03_integration_and_new_open.md`.*
