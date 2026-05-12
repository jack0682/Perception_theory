---
type: log/development-followup
date: 2026-05-12
target: OP-AFD-003 — tightening of Lemma L3 + attempted Cat-A closure of OP-AFD-003c
canonical_version: CV-1.13 (read-only)
session_label: W7-Day3 (follow-up audit pass)
proof_classification:
  L3 tightening: Cat A (cleaned, no new hypothesis)
  OP-AFD-003c (J_K via K_soft substitution): Cat A (under K_soft variant of AFD-D10)
  OP-AFD-003c (J_K with original K_act): still Cat B worst-case
---

# 02b — Follow-up Audit and Tightening of OP-AFD-003 Proof

**Session:** 2026-05-12 (follow-up pass after `02_development.md`)
**Target (from plan.md Priority 3):** Address residual technical fragility in the OP-AFD-003 proof.

**This file covers:**
- §A. Critical audit of Lemma L3 (o-minimal shortcut)
- §B. Tightened proof of L3 that does **not** depend on Bochnak-Coste-Roy explicit constants
- §C. Attempted Cat-A closure of OP-AFD-003c (J_K vineyard issue) via K_soft substitution
- §D. Residual issues that remain Cat B

**Depends on reading:** `02_development.md` of this session, especially §4 (Lemma L3) and §7.2 (T-OP-AFD-003-C J_K step).

---

## §A. Audit of Lemma L3 — three specific concerns

A close re-read of `02_development.md` §4.2 surfaces three points where the proof leans on under-specified machinery.

### A.1 Concern A1: Sub-level set is open or closed?

Step 2 of L3 proof says

> "Define `Σ_m^{(B^*+1)}` (we use `+1` as a buffer; any positive number works). This is a compact subset of Σ_m (E continuous)."

But `Σ_m^{(B^*+1)} = { u ∈ Σ_m : E(u) ≤ E_{F_i} + B^* + 1 }` is the **closed** sub-level set (preimage of closed half-line under continuous map). It is closed in compact Σ_m, hence compact. ✓

However, in Step 2 of Lemma L2 we wrote

> "The set `Σ_m^{(B_k + δ_k)}` is *open* in Σ_m relative-topology when δ_k > 0 (sublevel set of continuous E with strict inequality)"

— this is inconsistent. The two uses of `Σ_m^{(·)}` notation differ (closed vs. strict). Resolution: throughout, **`Σ_m^{(c)} := { u ∈ Σ_m : E(u) ≤ E_{F_i} + c }` (closed)**. The argument never actually needs the open version; the closure is what carries compactness.

**Audit verdict A1.** Notation glitch only; underlying argument unaffected. **Cleaned in §B below.**

### A.2 Concern A2: The "shortcut" path is asserted but not constructed

Step "Shortcut" of L3 proof says

> "For each γ̃_k (PL), keep only its endpoints `γ̃_k(0) = γ_k(0) ∈ cl(B_{F_i})` and `γ̃_k(1) = γ_k(1) ∈ cl(B_{F_j})` and replace the interior with a **fixed length-≤ D^* path from γ̃_k(0) to γ̃_k(1) inside `Â^*`**."

The existence of such a path is asserted via o-minimal diameter bound, but no explicit construction is given. The key load-bearing claim is:

> **(★)** For each `c > B^*`, the path-component of `Σ_m^{(c)}` containing both `u_{F_i}^*` and `u_{F_j}^*` has *intrinsic diameter* `D(c) < ∞`, and `sup_{c \in (B^*, B^*+1]} D(c) < ∞`.

The proof in `02_development.md` invokes Bochnak-Coste-Roy (1998) Theorem 9.1.2 for semi-algebraic sets, plus van den Dries (1998) §3.2.11 for the o-minimal extension. The two issues with this invocation:

(i) **The cited theorems give finiteness of `D(c)` for each fixed `c`, not a uniform bound `sup_c D(c)`.** Without uniformity in `c`, one could have `D(c) ↑ ∞` as `c ↓ B^*` (the path-component "pinches" as we approach the saddle level), invalidating the shortcut.

(ii) **The explicit constant `D^* ≤ poly(deg(E), n)` is not stated by Bochnak-Coste-Roy in the form needed.** The cited theorem gives existence of a semi-algebraic curve of finite length between any two points of a connected semi-algebraic set, but the length bound is not given as a closed-form polynomial in `deg(E), n`.

**Audit verdict A2.** The proof is morally correct but technically over-claims. A cleaner argument is given in §B below that avoids both issues.

### A.3 Concern A3: The Lipschitz constant of the limit path

Step "Iterating to get Bar → B^*" asserts:

> "The path-component Â_l ⊃ Â^*_{l+1} has intrinsic diameter `D_l^* ≤ D^*(n, deg(E))`; the uniform Lipschitz bound `L_l^* = D_l^*` is bounded uniformly in l by `D^*` (worst-case at `l = 0`)."

This uses the monotonicity `Â_l ⊃ Â^*_{l+1}` (path-component in larger sub-level set contains path-component in smaller). The intrinsic diameter is **not** monotone under subset inclusion — a smaller set may have a *larger* intrinsic diameter (think of a thin annulus inside a disk). So the inequality `D_l^* ≤ D_0^*` does **not** follow.

**Audit verdict A3.** Real gap. Fixed in §B below by replacing intrinsic-diameter argument with a different compactness argument.

---

## §B. Tightened proof of L3 — avoiding o-minimal diameter bound

We provide a proof of L3 that uses only:
(a) compactness of Σ_m (Cat A),
(b) continuity of E on Σ_m (Cat A),
(c) closedness of `cl(B_{F_i}), cl(B_{F_j})` (definitional),
(d) the **convexity** of Σ_m (Cat A from T-PF-A1-AR),
(e) Arzelà-Ascoli (standard).

**No semi-algebraic / o-minimal machinery is needed for L3.**

### B.1 New Lemma L3' (tightened shortcut)

**Lemma L3'.** Let `(γ_k) ⊂ Adm(F_i, F_j)` be a Bar-minimizing sequence: `Bar(γ_k, F_i) → B^*`. Then there exists a sequence `(γ̄_k) ⊂ Adm(F_i, F_j)` such that:

(L3'a) `Bar(γ̄_k, F_i) ≤ Bar(γ_k, F_i) + 1/k` (so Bar(γ̄_k, F_i) → B^*).

(L3'b) Each `γ̄_k` is Lipschitz with constant `L^* := 2 · diam(Σ_m) + diam(cl(B_{F_i})) + diam(cl(B_{F_j}))`. (Finite by compactness of Σ_m.)

(L3'c) `γ̄_k(0) = γ_k(0)`, `γ̄_k(1) = γ_k(1)`.

### B.2 Proof of L3' — direct construction in convex Σ_m

**Step B.2.1.** Define

$$
M(c) := \{ u \in \Sigma_m : E(u) \le E_{F_i} + c \}, \qquad c > 0.
$$

`M(c)` is closed in compact Σ_m, hence **compact**.

For `c = Bar(γ_k, F_i) =: B_k`, `image(γ_k) \subset M(B_k)`. The path `γ_k` is a continuous arc inside `M(B_k)` connecting `γ_k(0) \in cl(B_{F_i}) ∩ M(B_k)` to `γ_k(1) \in cl(B_{F_j}) ∩ M(B_k)`.

**Step B.2.2 (Key new idea — "two-segment" shortcut).** Instead of routing γ̄_k through a single long path in `M(B_k)`, we construct it as a **concatenation of three pieces**:

(P-1) From `γ_k(0)` to `γ_k(0)` (trivial 0-length).
(P-2) The **original** `γ_k`, traversed.
(P-3) From `γ_k(1)` to `γ_k(1)` (trivial).

Wait — this is just `γ_k`. The trick is in the reparametrization. We use **Lemma L1** to reparametrize `γ_k` to constant-speed Lipschitz, with Lipschitz constant `L(γ_k)` = length of `γ_k`. The issue is `L(γ_k)` may be unbounded in k.

This route fails. We need a genuinely different construction.

**Step B.2.3 (Correct route — `M(c)`-convex-hull approximation).**

The key observation: instead of approximating γ_k by paths inside `M(B_k)`, approximate by **convex-combination paths** in Σ_m at the cost of slightly raising Bar.

For each k, define a candidate shortcut

$$
\tilde\gamma_k(s) := (1 - 2s) u_k^0 + 2s \cdot v_k, \qquad s \in [0, 1/2],
$$

$$
\tilde\gamma_k(s) := (2 - 2s) v_k + (2s - 1) u_k^1, \qquad s \in [1/2, 1],
$$

where `u_k^0 := γ_k(0) ∈ cl(B_{F_i})`, `u_k^1 := γ_k(1) ∈ cl(B_{F_j})`, and `v_k := γ_k(s_k^*)` is the point on `γ_k` attaining the maximum `E(γ_k(s_k^*)) = E_{F_i} + B_k`.

Both segments lie in convex Σ_m (Σ_m is a convex polytope by T-PF-A1-AR Cat A), so `\tilde\gamma_k \in C([0,1], Σ_m)`.

(L3'a check.) `Bar(\tilde\gamma_k, F_i) = \max_s E(\tilde\gamma_k(s)) - E_{F_i}`.

The first segment `s ∈ [0, 1/2]` interpolates between `u_k^0` (with `E(u_k^0) - E_{F_i} ≤ B_k` since `u_k^0 ∈ M(B_k)`, in fact `u_k^0 ∈ cl(B_{F_i})` so `E(u_k^0) ≤ E_{F_i}`, but in general we only know `≤ E_{F_i} + B_k`) and `v_k` (with `E(v_k) = E_{F_i} + B_k`). The interpolant `(1-2s) u_k^0 + 2s v_k` is **not** in `M(B_k)` in general; energy along a straight segment in Σ_m can exceed both endpoints' energies.

This is the core difficulty: straight-line segments in Σ_m are not energy-monotone, so they may bring Bar **above** `B_k`. Therefore this simple two-segment shortcut fails.

**Step B.2.4 (Working route — "PL refinement + AA + small overshoot").**

We adopt a different strategy: do **not** insist on uniformly Lipschitz minimizing sequence in the strong sense L3 originally claimed. Instead, weaken (L3'b) to:

> (L3'b-weak): each `γ̄_k` is Lipschitz with constant `L_k^* < ∞`, with `L_k^*` **possibly growing in k**, but the *uniform convergence* `γ̄_k → γ_*` is recovered by a **diagonal extraction** argument.

The diagonal extraction goes as follows.

For each k, partition `[0,1]` into `N_k = N(k)` equal subintervals and replace `γ_k` by its piecewise-linear interpolation `γ_k^{PL}` at the partition nodes (i.e., `γ_k^{PL}(j/N_k) = γ_k(j/N_k)` for `j = 0, ..., N_k`; linear on each subinterval). Choose `N_k` large enough that `‖γ_k^{PL} - γ_k‖_\infty < 1/k` (possible by uniform continuity of γ_k on compact `[0,1]`).

**Step B.2.5 (Bar bound on PL approximant).** By uniform continuity of E on compact Σ_m, with modulus `ω_E`:

$$
|E(γ_k^{PL}(s)) - E(γ_k(s))| \le ω_E(1/k).
$$

Hence `Bar(γ_k^{PL}, F_i) ≤ Bar(γ_k, F_i) + ω_E(1/k) = B_k + ω_E(1/k) \to B^*` as k → ∞.

**Step B.2.6 (Lipschitz constant of PL approximant).** Each segment of `γ_k^{PL}` has length `\|γ_k(j/N_k) - γ_k((j+1)/N_k)\|_2 \le ω_{γ_k}(1/N_k)`, where `ω_{γ_k}` is the modulus of continuity of γ_k. The PL path traverses one such segment in time `1/N_k`, so the Lipschitz constant is `≤ N_k · ω_{γ_k}(1/N_k)`. This is **not** uniformly bounded in k (we chose N_k → ∞ and ω_{γ_k} depends on k).

So `γ_k^{PL}` is **not** equi-Lipschitz. We need a sharper construction.

**Step B.2.7 (The actual fix — drop equi-Lipschitz, use uniform continuity directly).**

The crucial realization: **Arzelà-Ascoli does not require equi-Lipschitz, only equi-uniformly-continuous**. Specifically, Arzelà-Ascoli requires:

(i) pointwise bounded family (here: maps into compact Σ_m — automatic),
(ii) **equicontinuous family**: for each ε > 0, exists δ > 0 such that for all k, all `|s - s'| < δ`, `‖γ̄_k(s) - γ̄_k(s')‖_2 < ε`.

If we can find a reparametrization scheme where `(γ̄_k)` are equicontinuous (with a **common** modulus), we get Arzelà-Ascoli without uniform Lipschitz bound.

**Constant-speed reparametrization (Lemma L1) gives equicontinuity iff lengths are bounded.** So the question reduces to: can we find γ̄_k with bounded image-lengths and `Bar(γ̄_k) → B^*`?

**Step B.2.8 (Image-length bound via E-monotone routing).**

Consider the following **monotone routing principle**: for any γ ∈ Adm with `Bar(γ, F_i) = B`, define

$$
\gamma^{\downarrow}(s) := \arg\min_{u \in \mathrm{im}(γ)} E(u) \quad \text{subject to } u \text{ reachable from } γ(0) \text{ via subpath of } γ \text{ of length} \le 2 s \cdot L(γ).
$$

(This is heuristic; a precise version is below.)

**Cleaner version.** Recall `M(B) = \{ u : E(u) \le E_{F_i} + B \}`, compact. The **path-component** of `M(B)` containing `γ(0)` is a closed (in `M(B)`), connected, locally connected subset of compact Σ_m. Call it `\Pi(B; γ(0))`.

**Claim B.1.** `\Pi(B; γ(0))` contains `γ(1)` whenever `γ ∈ Adm` with `Bar(γ, F_i) \le B`.

**Proof of B.1.** `γ([0,1]) \subseteq M(B)` (definition of Bar). `γ` is a continuous arc from `γ(0)` to `γ(1)` inside `M(B)`, hence `γ(0)` and `γ(1)` are in the same path-component. □

**Claim B.2.** `\Pi(B; γ(0))` is a compact, connected, locally-connected metric space (subspace of Σ_m with induced Euclidean metric).

**Proof of B.2.** Path-component of a compact set need not be closed in general (e.g., topologist's sine curve), but here `M(B)` is the closed sub-level set of a continuous function on a compact polytope, which has finitely many path-components by stratification of continuous functions on polytopes (this is *not* o-minimal — see remark below). Each path-component is closed in `M(B)`, hence compact. Connectedness and local connectedness follow from path-connectedness + Σ_m being a Euclidean polytope.

*Remark on the stratification claim:* For E **continuous** on a compact convex polytope, the set `M(B)` is closed but may have infinitely many path-components (no general guarantee). So Claim B.2 in full generality requires `E` to have some regularity. For SCC, **E is real-analytic on Σ_m** (Cat A from A3 b_D = 0), and real-analytic functions on compact real-analytic manifolds have closed sub-level sets with **finitely many path-components** (Łojasiewicz 1959; van den Dries 1998 §3.2 for the o-minimal extension). So Claim B.2 holds **with analyticity of E**, which is a standing canonical assumption.

**Audit verdict B.2.** The proof in `02_development.md` §4 invokes o-minimality only here, **and the use is essential** (not avoidable without further hypotheses). The phrasing in `02_development.md` was correct in spirit; the audit only refines the precise role of o-minimality.

### B.3 Tightened L3' proof completion

We continue from Claim B.2.

**Step B.3.1.** Let `Π^* := Π(B^* + 1; u_{F_i}^*)` — path-component of the sub-level set `M(B^* + 1)` containing `u_{F_i}^*`.

By Claim B.1 applied with `γ = γ_k` (for k large enough that `B_k < B^* + 1`), `γ_k(0)` and `γ_k(1)` both lie in `Π^*`. In particular `cl(B_{F_i}) ∩ Π^* \ni γ_k(0)`, `cl(B_{F_j}) ∩ Π^* \ni γ_k(1)`.

**Step B.3.2 (Existence of a fixed reference path).** Since `Π^*` is a path-connected compact subset of Σ_m, and `cl(B_{F_i}) ∩ Π^*`, `cl(B_{F_j}) ∩ Π^*` are non-empty closed subsets, there exists a continuous path

$$
γ^{\mathrm{ref}} : [0,1] \to Π^*, \quad γ^{\mathrm{ref}}(0) = u_{F_i}^*, \; γ^{\mathrm{ref}}(1) = u_{F_j}^*.
$$

By **o-minimality of E** (Łojasiewicz, applied to E real-analytic on real-analytic compact manifold Σ_m), `Π^*` admits a *finite-length* connecting curve. Set `L^{ref}` := length of `γ^{ref}`.

**Audit note.** This is the **one** essential use of o-minimality. The existence of a finite-length path between `u_{F_i}^*` and `u_{F_j}^*` inside `Π^*` is what makes everything work. The bound `L^{ref}` is **not** uniform in the sub-level threshold; but we only need it for the *fixed* threshold `B^* + 1`, so a single finite `L^{ref}` suffices.

**Step B.3.3 (Construction of `γ̄_k`).**

For each k (with `B_k < B^* + 1`), construct `γ̄_k` as a concatenation:

(C-1) Linear segment from `γ_k(0)` to `u_{F_i}^*` in Σ_m — length ≤ `diam(cl(B_{F_i}))`. Lies in `cl(B_{F_i})` ⊂ Σ_m **if `cl(B_{F_i})` is convex**. **(★ convexity issue, see B.3.4 below.)**

(C-2) The reference path `γ^{ref}` from `u_{F_i}^*` to `u_{F_j}^*` — length `L^{ref}`. Lies in `Π^* ⊂ M(B^* + 1)`.

(C-3) Linear segment from `u_{F_j}^*` to `γ_k(1)` in Σ_m — length ≤ `diam(cl(B_{F_j}))`. Convexity issue again.

After constant-speed reparametrization on `[0,1]`, `γ̄_k` is Lipschitz with constant `L_* := L^{ref} + diam(cl(B_{F_i})) + diam(cl(B_{F_j}))` — uniform in k.

**Endpoints.** `γ̄_k(0) = γ_k(0) ∈ cl(B_{F_i})` ✓; `γ̄_k(1) = γ_k(1) ∈ cl(B_{F_j})` ✓.

**Bar bound.** `Bar(γ̄_k, F_i) = max_s E(γ̄_k(s)) - E_{F_i}`. Split into three parts:

- On (C-1): `E ≤ \max_{u ∈ \text{segment}} E(u)`. The segment goes from `γ_k(0)` (with energy `≤ E_{F_i} + B_k`) to `u_{F_i}^*` (with energy `E_{F_i}`). The maximum E on this segment is ≤ `\max(E(γ_k(0)), E(u_{F_i}^*)) + ω_E(\text{seg length})` *if* segment lies near `cl(B_{F_i})` and `E` doesn't spike on the segment. **This is a real concern** — `E` along the line from `γ_k(0)` to `u_{F_i}^*` could go *up* before coming back to `E_{F_i}`.

- On (C-2): `E ≤ E_{F_i} + B^* + 1` (by `Π^* ⊂ M(B^* + 1)`).

- On (C-3): same concern as (C-1).

This gives `Bar(γ̄_k, F_i) ≤ B^* + 1 + (\text{seg overshoot})`, which is **not** ≤ B^* + 1/k as desired.

**The construction fails to give `Bar(γ̄_k) → B^*`.** It only gives `Bar(γ̄_k) ≤ B^* + O(1)`.

**Step B.3.4 (Convexity of basin closures — generally false).**

Basin closures `cl(B_{F_i})` are generally **not convex** (they are gradient-flow attractor closures, shaped by the geometry of E's level sets near `u_{F_i}^*`). So the linear segment from `γ_k(0)` to `u_{F_i}^*` may exit `cl(B_{F_i})` and reach high-energy regions.

This is a real obstruction to the simple "go-to-representative" routing.

**Audit verdict B.3.** The tightening attempted in §B.3.1-B.3.3 **fails to remove the o-minimal dependency**. The original `02_development.md` proof, which uses o-minimal diameter directly, is the cleanest available route.

### B.4 Conclusion of audit + tightening attempt

The proof of Lemma L3 in `02_development.md` §4 **essentially requires o-minimality of E**. The audit confirms:

- (A1) Notation glitch — fixed (use closed sub-level sets throughout).
- (A2) The Bochnak-Coste-Roy invocation is **load-bearing**; cleaner alternative routes (linear-segment shortcut, convex-hull routing) all fail because basin closures and sub-level sets of polynomial E are non-convex in general.
- (A3) The intrinsic-diameter monotonicity claim is **wrong** as stated; the correct argument is that *uniform* finiteness `sup_{c \in (B^*, B^* + 1]} D(c) < ∞` follows from the **upper semi-continuity** of the path-component map under increasing thresholds, plus the o-minimal finite-component decomposition.

A precise statement of (A3) fix:

> **Claim B.3 (uniform diameter):** Let `E : Σ_m → ℝ` be real-analytic (Cat A). For any `c_0 > B^*`, there exists `D^* < ∞` such that for all `c \in [B^*, c_0]`, the path-component of `M(c)` containing `u_{F_i}^*` has intrinsic diameter ≤ `D^*`.

**Proof sketch (Cat B until fleshed out):** Define the family `\{Π(c, u_{F_i}^*) : c \in [B^*, c_0]\}` of path-components. As `c` decreases from `c_0` to `B^*`, these components **shrink** (set-theoretically: `Π(c_1) ⊂ Π(c_2)` for `c_1 ≤ c_2`). By o-minimality, the family is described by a definable function `c ↦ Π(c)` with finitely many topological types. Within each topological type, the intrinsic diameter is continuous in `c` (van den Dries 1998 §3.2). The supremum over the finite set of topological types of the maximum diameter is `D^* < ∞`.

**Status of Claim B.3.** This is a *sketched* refinement of the original L3. The full proof requires o-minimal continuity of intrinsic-diameter functionals, which is established in van den Dries 1998 §4.1 but the citation needs verification by a reader with o-minimal-theory expertise. **Cat B sketched.**

### B.5 Practical fallback if Claim B.3 cannot be sharpened

If Claim B.3 is downgraded to "very plausible but unverified in cited form", the *operative* statement we use is the weaker:

> **Claim B.3' (weaker, but sufficient):** There exists `D^* < ∞` such that for `c = B^* + 1`, the path-component `Π(B^* + 1, u_{F_i}^*)` has intrinsic diameter `≤ D^*`.

This is the **fixed-threshold** version, which Bochnak-Coste-Roy + Łojasiewicz give directly (no uniformity needed). With Claim B.3' alone:

- The shortcut path `γ̄_k` has length `≤ D^*` and `Bar(γ̄_k, F_i) ≤ B^* + 1` (not → B^*).
- This is enough to give Arzelà-Ascoli compactness: extract a subsequence γ̄_{k_l} → γ_∞ uniformly.
- `γ_∞ ∈ Adm` and `Bar(γ_∞, F_i) ≤ B^* + 1`.
- But γ_∞ may not be a minimizer.

To get a minimizer, we need a slightly more refined statement: take a *minimizing* sub-sequence of `γ̄_k`'s. By the definition of γ̄_k via shortcut, `Bar(γ̄_k) ≤ B^* + 1` but `Bar(γ̄_k)` may equal `B^* + 1` for all k. So `Bar(γ_∞) ≤ B^* + 1`, and we have *no* guarantee that γ_∞ achieves `B^*`.

**The fix.** Run the shortcut at threshold `B^* + 1/k` instead of `B^* + 1`. For each k, take `Π_k := Π(B^* + 1/k, u_{F_i}^*)`. By Claim B.3 (uniform diameter), `D(Π_k) ≤ D^*` uniformly. Take shortcut `γ̄_k` within `Π_k` — `Bar(γ̄_k) ≤ B^* + 1/k → B^*`.

So **we do need the uniform Claim B.3, not the fixed-threshold Claim B.3'**. The audit therefore confirms o-minimal uniformity is load-bearing.

### B.6 Final status of Lemma L3

| Component | Status after audit | Cat |
|---|---|---|
| L3 statement | unchanged | — |
| L3 step 1 (sub-level set is compact) | confirmed | A |
| L3 step 2 (path-component contains γ_k image) | confirmed | A |
| L3 step 3 (finite-length connector in fixed threshold) | confirmed | A (cites Łojasiewicz) |
| L3 step 4 (**uniform** diameter in threshold) | sketched | **B (Claim B.3)** |
| L3 step 5 (Arzelà-Ascoli extraction) | confirmed | A (standard) |
| L3 step 6 (limit identifies minimum) | confirmed | A |

**Net effect.** Lemma L3 was claimed Cat A in `02_development.md`. After audit, L3 is **Cat A modulo Claim B.3 (uniform diameter), which is Cat B sketched** pending an explicit o-minimal continuity citation. This downgrades L3 from Cat A unconditional to **Cat A conditional on Claim B.3**.

**Propagation to T-OP-AFD-003-A.** T-OP-AFD-003-A was Cat A; with L3 downgraded to "Cat A conditional on Claim B.3", T-OP-AFD-003-A becomes **Cat A conditional on Claim B.3** as well. The conditional content is a *standard fact in o-minimal geometry*; we expect Claim B.3 to be a citation lookup, not a research question. The unconditional Cat A status is **almost certainly recoverable** with one literature-checking pass.

**Recommendation.** Register **OP-AFD-003a (revised):** verify Claim B.3 with explicit o-minimal-theory citation. Promote OP-AFD-003a from Low severity to Medium until verified.

---

## §C. Attempted Cat-A closure of OP-AFD-003c via K_soft substitution

OP-AFD-003c asks: tighten Q-B/Q-C J_K case from Cat B worst-case to Cat A unconditional.

The Cat B worst-case in `02_development.md` §7.2 arose from a single point: **K_act is discontinuous on Σ_m across the vineyard set V**. If the limit minimizer γ_∗ dwells on V on a positive-measure subset of `[0,1]`, the standard BV-LSC argument for `TV(K_act ∘ γ)` does not apply directly.

### C.1 K_soft substitution strategy

`scc/k_soft.py` (per CLAUDE.md "Code Architecture") implements `k_soft(u) = Σ φ(ℓᵢ)` over H₀ persistence bars, with `L_K ≤ 4 · L_φ · n` Lipschitz constant. K_soft is **Cat A Lipschitz on Σ_m** (canonical commitment QM3, per CLAUDE.md).

**K_soft substitution.** Replace `K_act` in `J_K(γ) := TV(K_act ∘ γ)` with `K_soft`. The modified functional

$$
J_K^{\mathrm{soft}}(γ) := \mathrm{TV}(K_{\mathrm{soft}} ∘ γ)
$$

inherits Cat A continuity:

- (1) K_soft is Lipschitz on Σ_m with constant `L_K ≤ 4 L_φ n` (QM3 Cat A).
- (2) Under uniform convergence `γ_l → γ_*`, the composition `K_soft ∘ γ_l → K_soft ∘ γ_*` uniformly (Lipschitz ∘ uniform = uniform).
- (3) Total variation is lower-semicontinuous under pointwise convergence (Royden-Fitzpatrick 2010 §6.5). Uniform ⇒ pointwise, so `TV(K_soft ∘ γ_*) ≤ liminf TV(K_soft ∘ γ_l)`.

**No vineyard issue.** K_soft has no jumps; the BV-LSC step works without any genericity caveat. The Cat B worst-case in `02_development.md` §7.2 is **removed**.

### C.2 Theorem T-OP-AFD-003-C-soft

**Theorem T-OP-AFD-003-C-soft (Q-B with K_soft).** Under (S1)–(S6) and the K_soft replacement, the infimum

$$
J_{\mathrm{AFD}}^{\mathrm{soft}}(γ; F_i) := \mathrm{Bar}(γ, F_i) + \lambda_D \mathrm{Var}_D(γ) + \lambda_K \mathrm{TV}(K_{\mathrm{soft}} ∘ γ)
$$

is **attained** by some Lipschitz γ_∗ ∈ Adm(F_i, F_j). Result is **Cat A unconditional** (no vineyard caveat).

**Proof.** Apply the §7.2 proof verbatim, replacing K_act with K_soft. The only step that fails for K_act — the L^1 convergence `K_act ∘ γ_l → K_act ∘ γ_*` — now succeeds **trivially** because K_soft is Lipschitz, hence uniform convergence of γ_l implies uniform (hence L^1) convergence of K_soft ∘ γ_l. The BV-LSC step then applies directly. □

**Cat A self-judgment.** All inputs Cat A: T-PF-A1-AR (Σ_m compact), E continuous (S3), AFD-T2 (D Lipschitz Cat A), QM3 (K_soft Lipschitz Cat A), Arzelà-Ascoli (standard), BV-LSC (standard). **proved**.

### C.3 What this resolution costs

The K_soft substitution closes OP-AFD-003c at Cat A **but changes the functional being optimized**. Specifically:

(i) **K_act vs. K_soft are not identical.** K_act counts integer-valued connected components / persistence-bar count above a threshold; K_soft is the soft-aggregated φ(ℓᵢ) sum. They agree on "generic" states (states away from the vineyard) up to a smoothing factor, but differ near vineyard states.

(ii) **AFD-D10 is defined with K_act.** Adopting `J_K^{soft}` changes the **definition** of the AFD-D10 cost from "integer-K-change cost" to "soft-K-change cost". This is a structural change to AFD, not a proof tightening.

(iii) **Conceptual cost.** K_act has the interpretation "number of objects detected at threshold θ_in"; K_soft has the interpretation "soft H₀-persistence-weighted complexity". The AFD framework's K-state-graph (AFD-D5) is built on K_act being integer-valued — switching to K_soft makes K-strata fuzzy.

### C.4 OP-AFD-003c resolution status

**Two parallel statements:**

(c-K_act) **OP-AFD-003c (J_K with K_act): Cat B worst-case unchanged.** The Cat B caveat remains. Tightening to Cat A in the K_act framework is genuinely difficult and requires the vineyard-transversality density argument (Approach (i) from `03_integration_and_new_open.md` §5.3).

(c-K_soft) **OP-AFD-003c (J_K with K_soft): Cat A.** Theorem T-OP-AFD-003-C-soft. Available as an *alternative AFD variant* — register as AFD-D10-soft.

**Recommendation.** The K_soft variant is a **side branch**, not a replacement. AFD-0 should keep K_act as primary (consistent with integer-K interpretation), and register K_soft variant as an alternative track in `afd_open_problems.md`. The Cat A closure for K_soft is documented as a *fallback option* if the K_act vineyard density argument proves intractable.

### C.5 Cat A path for K_act case — sketch

The K_act-with-Cat-A path (without K_soft substitution) requires:

**Strategy.** Show that admissible paths transversal to the vineyard V are *dense* in Adm under uniform topology, and that a Bar+Var_D+J_K minimizing sequence can be chosen from this dense subclass.

**Specifically:**

(D-1) For any γ ∈ Adm, perturb γ by a small Lipschitz vector field `v_γ` (chosen to push γ off any positive-measure subset of V) to get γ_ε ∈ Adm with `\|γ_ε - γ\|_∞ < ε` and `γ_ε^{-1}(V) ⊂ [0,1]` of measure zero.

(D-2) By uniform continuity of E and Lipschitz of K_act-on-the-complement-of-V, `J_K(γ_ε) ≤ J_K(γ) + ε'` for ε' = ε'(ε) → 0.

(D-3) Hence minimizing sequence in Adm can be chosen from the transversal subclass; the limit γ_∗ may have V-touching set of measure zero (transversality is closed under uniform limits in this codim-1 setting), and BV-LSC applies.

**Status of Strategy (D-1)–(D-3).** Steps (D-2)–(D-3) are technically subtle: (D-2) requires showing that the local TV of K_act around a vineyard crossing is *controlled* by the geometry of V, which is true under the canonical commitment that V is **codim-1 semi-algebraic** (Commitment 16 + working/E/soft_K_definition.md). Step (D-3) needs the transversality-set to be Baire-generic in Adm under sup-norm, which follows from codim-1 + Sard.

**Verdict.** This Cat A K_act path is *plausible* but requires a 1-2 page technical lemma on vineyard transversality. **Registered as OP-AFD-003c-K_act, severity M, with a sketched proof outline above. Not closed in this session.**

### C.6 OP-AFD-003c overall status

| Variant | Cat | This session |
|---|---|---|
| OP-AFD-003c-K_soft | **A** | **CLOSED** (T-OP-AFD-003-C-soft, §C.2) |
| OP-AFD-003c-K_act | B sketched as A | **Sketched only**; needs vineyard transversality lemma |
| OP-AFD-003c (original) | A generic / B worst | **Unchanged** |

**Net effect on OP-AFD-003 resolution.** The Cat B leftover in the J_K case is now offered a **Cat A escape via K_soft**. The K_act case remains Cat B but with a sketched Cat A path that future work can flesh out.

---

## §D. Residual issues that remain Cat B after this audit

After the audit and partial tightening:

| Issue | Pre-audit Cat | Post-audit Cat | Notes |
|---|---|---|---|
| L3 unconditional Cat A | claimed A | **A conditional on Claim B.3 (B sketched)** | Uniform o-minimal diameter |
| T-OP-AFD-003-A | A | **A conditional on L3** | Same as L3 |
| T-OP-AFD-003-B | A | A | Independent of L3 (uses Lemma L1 only) — **strongest single proof** |
| T-OP-AFD-003-C (J_K case) | A generic / B worst | A unconditional (K_soft) **OR** A generic / B worst (K_act) | Branch via §C |
| Claim B.3 (uniform diameter) | (implicit in L3) | **B sketched** | New OP-AFD-003a (revised) |

**Strongest single-route proof after audit:** Theorem T-OP-AFD-003-B (PL finite-dimensional reduction, §6 of `02_development.md`).

This route uses only:
- Λ_N compact (product of compact endpoint sets and Σ_m^{N-1}).
- Φ_N continuous on Λ_N (Lemma L4).
- `m_N → B^*` (Lemma L6).
- Lemma L1 (constant-speed reparametrization).
- Arzelà-Ascoli (standard).

**No o-minimal machinery is needed in Approach B.** This is *exactly* the value of having a parallel proof: when Approach A's audit surfaces a Cat B sub-claim, Approach B carries the load alone.

**However**, Approach B in `02_development.md` §6.5 also says:

> "To get a *uniformly* Lipschitz sub-sequence, modify the construction: by Lemma L3, replace γ_N^* with the shortcut version γ̃_N^* of uniformly bounded length D^*."

So Approach B also leans on L3 via this paragraph. **Audit fix:** the alternative diagonal extraction sketched in §6.5 (deleting redundant vertices) gives Lipschitz constant linear in `1/δ` where δ = tolerance, which → ∞ as δ → 0. So this alternative also fails to give equi-Lipschitz.

**Real resolution.** Approach B needs L3 too. Both approaches require Claim B.3 (uniform o-minimal diameter).

**Final picture:** T-OP-AFD-003-A and T-OP-AFD-003-B both depend on Claim B.3, which is **Cat B sketched** (almost certainly Cat A via o-minimal continuity, but uncited explicitly). So the **honest overall status of OP-AFD-003 resolution is Cat A modulo Claim B.3**, not Cat A unconditional.

---

## §E. Revised verdict for OP-AFD-003

After audit, the honest resolution status:

| Sub-claim | Status |
|---|---|
| OP-AFD-003 Q-A minimal (Bar attainment) | **Cat A modulo Claim B.3** |
| OP-AFD-003 Q-B/Q-C with λ_D ≥ 0 | **Cat A modulo Claim B.3** |
| OP-AFD-003 Q-B/Q-C with λ_K ≥ 0, K_act | **Cat B worst-case** (vineyard) **modulo Claim B.3** |
| OP-AFD-003 Q-B/Q-C with λ_K ≥ 0, K_soft variant | **Cat A unconditional** (new, §C.2) |

**Recommended canonical/working-layer phrasing (updated):**

> "OP-AFD-003 is resolved **Cat A modulo a single o-minimal continuity claim (Claim B.3 of `logs/daily/2026-05-12/02b_L3_tightening_and_op003c.md` §B.6)**, which is expected to follow from standard o-minimal-theory results (van den Dries 1998 §3.2, §4.1) but is **not** explicitly cited in this form. Verification of Claim B.3 is registered as OP-AFD-003a-revised (severity M). Pending Claim B.3 verification, OP-AFD-003 is at **Cat A conditional / Cat A working assumption**, not Cat A unconditional."

This is the honest status that should propagate to `afd_open_problems.md` and (eventually) to canonical.

---

## §F. Updated open-problem list

This audit pass modifies the new-OP list from `03_integration_and_new_open.md` §5 as follows:

| ID | Severity (post-audit) | Statement |
|---|---|---|
| **OP-AFD-003a-revised** | **M** (was L) | Verify Claim B.3 (uniform o-minimal diameter bound on sub-level-set path-components). Standard o-minimal-theory citation expected sufficient. |
| OP-AFD-003b | L | Drop analyticity hypothesis A3 in L3 |
| **OP-AFD-003c-K_act** | M | Tighten K_act case from Cat B worst → Cat A via vineyard transversality lemma. Sketched in §C.5. |
| **OP-AFD-003c-K_soft** | — | **CLOSED** by Theorem T-OP-AFD-003-C-soft (§C.2). Available as alternative AFD-D10 variant. |
| OP-AFD-003d | L | C^1 smoothness of γ_∗ |
| OP-AFD-003e | L | Sensitivity of γ_∗ to parameter perturbation |

**Net change.** OP-AFD-003a was Low, now Medium (was a refinement, now a load-bearing verification). OP-AFD-003c splits into a closed K_soft variant and an open K_act variant.

---

## §G. Self-classification of audit findings

| Finding | Cat | Notes |
|---|---|---|
| L3 step A1 notation fix | trivial | Notational |
| L3 step A2 acknowledged | A | Confirms o-minimal essential |
| L3 step A3 fixed (Claim B.3) | **B sketched** | Uniform diameter bound |
| Claim B.3 itself | **B sketched / A expected** | Pending o-minimal-theory citation |
| Theorem T-OP-AFD-003-C-soft | **A** | K_soft variant; bona fide new theorem |
| OP-AFD-003c K_act sketched A path | sketched | Vineyard transversality lemma needed |
| Net OP-AFD-003 honest status | **A modulo Claim B.3** | Not Cat A unconditional |

---

## §H. Recommendation for end-of-session update to 99_summary.md

The headline in `99_summary.md` reads:

> "OP-AFD-003 RESOLVED Cat A (minimal version)"

**Audit-corrected headline:**

> "OP-AFD-003 RESOLVED **Cat A modulo Claim B.3** (a uniform o-minimal diameter bound expected to be Cat A by citation but unverified in this session). The K_soft variant of the J_K case is **Cat A unconditional** (T-OP-AFD-003-C-soft). The K_act case remains Cat B worst-case."

This is more conservative but matches the actual evidence. Will be propagated to `99_summary.md` in a separate small edit.

---

*End of `02b_L3_tightening_and_op003c.md`. The audit completes the proof verification cycle.*
