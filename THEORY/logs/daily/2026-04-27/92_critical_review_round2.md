# 92_critical_review_round2.md — Second-Round Deep Re-Review

**Session:** 2026-04-27 (W5 Day 1, post-evening-corrections, second user re-audit)
**Trigger:** User feedback "아직 좀 부족한데 제대로 좀더 재검토해서 분석해줘" (second iteration).
**Purpose:** Beyond the 3 explicit math errors caught in `91_critical_review.md`, identify *structural* gaps in the σ-framework canonical merge — well-definedness corner cases, hidden hypotheses, missing dimensions of generality, anchoring/circularity issues, and σ-framework completeness assessment.
**Output:** This document + targeted canonical refinements + 99_summary §11 round-2 update + CHANGELOG second addendum.

---

## §1. Categorization of Round-2 Issues

| # | Type | Severity | Issue |
|---|------|---------|-------|
| **H** | **Well-definedness gap** | HIGH | σ-tuple ordering is **not specified** when two eigenvalues are equal but irreps differ (the exact case T-σ-Theorem-4 (v) creates on $D_4$ where $K_0 = K_1$). Commitment 14 (O5) is silent on this. Without a tie-break convention, σ is not a deterministic discrete invariant — it's a multi-set with ambiguous ordering. |
| **I** | **Dimensional under-generality** | MEDIUM | T-σ-Lemma-3 stated for "2D bulk graph"; canonical T-V5b-T-(e) claims "Goldstone nodal = 2 *universal* on translation-invariant graphs" (1D, 2D, 3D, torus). Lemma 3 doesn't fully anchor that universality — only 2D localized. Need extension to 1D cycle and torus geometries. |
| **J** | **Multi-irrep eigenspace ambiguity** | MEDIUM | T-σ-Lemma-1 (iii) asserts well-defined irrep label "When $\dim V_k = 1$". For $\dim V_k > 1$ with multiple irreps (e.g., $D_4$ orbit pair giving $A_1 \oplus B_1$), Commitment 14 (O5) says use "multi-set" but σ-tuple representation is not clear. Need explicit canonical convention. |
| **K** | **Hidden hypothesis in Theorem 3** | MEDIUM | Theorem 3 stated for "spinodal interior" $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$. At spinodal *boundary* (where $W''(c) = 0$), the closed form becomes $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}}$ (Laplacian alone) — degenerate critical case. Outside spinodal ($W''(c) > 0$): $\mu_k > 0$ trivially, no bifurcation. The "spinodal interior" hypothesis hides where the action is. Should be more explicit. |
| **L** | **Theorem 4 orbit invariance not explicit** | MEDIUM | I noted in `01e` §1 that 4 orbit elements exist ($c\mathbf{1} \pm a_\epsilon \phi_{(1, 0)}$ + $c\mathbf{1} \pm a_\epsilon \phi_{(0, 1)}$). Theorem 4 picks one representative ($+a_\epsilon \phi_{(1,0)}$) with stabilizer $\langle s_y\rangle$. The σ-tuple is the same across the orbit modulo conjugation of stabilizer. Canonical entry doesn't make this explicit; if interpreted naively, different orbit elements give different irrep labels (trivial vs sign roles swap), even though they're σ-equivalent. |
| **M** | **σ-framework anchoring vs T-V5b-T completeness** | LOW (clarification) | Today's σ supporting structures (Lemma 1/2/3 + Theorem 3/4) anchor parts of T-V5b-T but NOT all sub-statements. Specifically: Lemma 3 (iii) anchors (V5b-T-e) nodal=2 (after extension to general dim, see I). But (V5b-T-a) sub-lattice "orbital, no Goldstone", (V5b-T-c) commensurability splitting, (V5b-T-d) ζ_* graph dependence — these have NO σ supporting structure derivation; they're empirical. This should be explicitly registered as canonical-anchored vs canonical-empirical. |
| **N** | **Lemma 3 (i) framing is awkward** | LOW (stylistic) | The corrected (i) emphasizes the explicit value $-\pi \int u^* dr$. But the *primary* content of Lemma 3 is qualitative: "Goldstone subspace maps **injectively** into ℓ=1 angular subspace, with rank 2". The explicit value is secondary. Reframing (i) to lead with the rank statement, then give the value as a corollary, is cleaner. |
| **O** | **Lemma 3 reference Cor 2.2 ambiguous** | LOW | Lemma 3 references "Cor 2.2" (interface tail bound) without file path. Cor 2.2 is in W4-04-24 `02_development.md` §5.4. Need explicit file reference. |
| **P** | **Higher-order Theorem 4 splitting** | LOW (open-question) | $K_0 = K_1$ holds at *leading order* in $\epsilon$. Higher-order normal-form coefficients (5th, 6th equivariants) could split them at $O(\epsilon^{3/2})$ or $O(\epsilon^2)$. The σ-tuple at $u^*_\epsilon$ on $D_4$ is leading-order-degenerate but possibly splits at sub-leading. Theorem 4 currently claims leading-order only and silent on sub-leading. Should flag as NQ. |
| **Q** | **Sanity-test snippet promised but not delivered** | LOW (process) | `91_critical_review.md` §6.G promised to "add this sanity-test snippet to `04_nq174_setup.md` Day 2 morning checklist" — I didn't actually do it. Follow-through gap. |
| **R** | **σ-framework forward gaps register** | MEDIUM (planning) | Today's 5 supporting structures don't cover: σ-tuple uniqueness theorem (how many distinct σ-classes per parameter regime), σ-stability under parameter variation (cascade analysis NQ-186 placeholder only), multi-formation σ extension (G3 W5+ work), crisp-object recovery from σ. These are explicitly NOT today's scope but should be registered as σ-framework's known forward gaps (open problems sub-register). |

**Severity assessment**: 1 HIGH (H), 5 MEDIUM (I, J, K, L, R), 5 LOW (M, N, O, P, Q).

---

## §2. Issue H — σ-tuple Tie-Breaking Convention (HIGH)

### 2.1 The problem

T-σ-Theorem-4 (v) σ-signature on $D_4$:
$$\sigma(u^*_\epsilon)\big|_{D_4} = \big(\mathcal{F}; (2, [+1], 4|W''(c)|\epsilon),\ (2, [-1], 4|W''(c)|\epsilon),\ \ldots\big).$$

Both first two entries have **identical eigenvalue** $\lambda = 4|W''(c)|\epsilon$ but **different irrep labels** ($[+1]$ trivial vs $[-1]$ sign).

Commitment 14 (canonical §11.1, line 768): "$\{(n_k, [\rho_k], \lambda_k)\}_{k=0}^{K-1}$" with no specified tie-break rule for $\lambda_k = \lambda_{k+1}$.

If the σ-tuple is supposed to be a deterministic discrete invariant (Aut(G)-orbit unique), the lack of tie-break makes Theorem 4's σ-signature **not well-defined** — the two entries could be ordered $([+1], [-1])$ or $([-1], [+1])$.

I added "lex-ordering convention places trivial irrep before sign irrep" in T-σ-Theorem-4 (v) but this is **not** in Commitment 14. The convention is local to Theorem 4's entry. For consistency across canonical, the convention must be **promoted to Commitment 14 itself**.

### 2.2 Proposed Commitment 14 refinement

Add a new sub-clause (O7) to Commitment 14:

> **(O7) Tie-breaking for degenerate eigenvalues.** When $\lambda_k = \lambda_{k+1}$ but $[\rho_k] \neq [\rho_{k+1}]$, order entries by the **canonical character-table order** of the residual stabilizer's irreps. For $D_4 = \{A_1, A_2, B_1, B_2, E\}$: order $A_1, A_2, B_1, B_2, E$ (Mulliken convention). For $\mathbb{Z}_2 = \{[+1], [-1]\}$: order $[+1], [-1]$ (trivial first). For $\mathbb{Z}_n$ cyclic: order $[1], [\omega], [\omega^2], \ldots$ by phase. For general finite groups: order by isomorphism-class invariants (smallest dimension first; within same dimension, order by character of generator).

This is a canonical-level addition that makes σ a deterministic discrete invariant.

### 2.3 Action

**Edit Commitment 14** in canonical.md §11.1 to add (O7). This is a **non-trivial canonical change** beyond the §13 entries — but the σ-tuple's well-definedness is structurally required. I will write the proposed addition but **defer to user decision** for the canonical commit (per plan.md §6 hard constraint: G0 outside changes need user approval).

Recommended action: register as W5 Day 2+ user decision item (similar to "Option α/β/γ" decision but at Commitment level).

---

## §3. Issue I — Lemma 3 Dimensional Generality

### 3.1 Current statement scope

T-σ-Lemma-3 (canonical line 1213): "Let $u^* \in \Sigma_m^{\circ}$ be a localized Morse-0 minimizer on a 2D bulk graph (support distance $\geq d_*$ from boundary, characteristic interface width $\xi_0$)..."

T-V5b-T-(e) claim: "Goldstone mode has Courant nodal count $n_k = 2$ **universally** on translation-invariant graphs..."

The "universally" includes 1D cycles, 2D tori, 3D tori, etc. Lemma 3 covers only 2D bulk (free-BC); doesn't extend to torus or other dimensions.

### 3.2 Extension to general dimension

The IBP saturation identity generalizes to $d$-dim with $d$ translation modes $\delta u_{x_1}, \ldots, \delta u_{x_d}$ and the analog "ℓ=1" basis being the unit-vector-direction basis $\hat e_i = (i_{x_i} - x_*)/r$ (in $d$ dimensions, "ℓ=1" is the first spherical-harmonic family, which has dim $d$).

For each $\mu \in \{1, \ldots, d\}$:
$$\mathcal{P}_{\ell=1, \mu}[\delta u_{x_\mu}] = -c_d \int_0^\infty u^*(r)\, dr,\qquad c_d = \begin{cases} 1 & d = 1, \\ \pi & d = 2, \\ 2\pi & d = 3, \\ \ldots\end{cases}$$
($c_d = $ surface-area coefficient of unit $(d-1)$-sphere divided by 2, modulo conventions.)

Cross-axis projection (e.g., $\mathcal{P}_{\ell=1, \mu}[\delta u_{x_\nu}]$ for $\mu \neq \nu$) vanishes by orthogonality of $\hat e_\mu$ and $\hat e_\nu$.

Hence **rank** $\mathcal{P}_{\ell=1}|_{\mathrm{Goldstone subspace}} = d$ — the $d$-dim Goldstone subspace maps injectively onto the $d$-dim ℓ=1 angular subspace. ✓

For nodal count = 2: $\delta u_{x_\mu} = u^*(\cdot + e_\mu) - u^*$ has sign pattern $\sgn(\delta u_{x_\mu}(i)) = -\sgn(i_{x_\mu} - x_{*,\mu})$. The nodal partition is the half-space $\{i : i_{x_\mu} < x_{*,\mu}\}$ vs $\{i_{x_\mu} > x_{*,\mu}\}$, separated by codimension-1 hyperplane $\{i_{x_\mu} = x_{*,\mu}\}$. Each half-space is connected on the lattice (in any dimension, on grid or torus). Hence $\mathcal{N}(\delta u_{x_\mu}) = 2$ universally.

For 1D cycle: $\delta u_x(i) = u^*(i+1) - u^*(i)$ on cycle has 2 zero crossings (one through support center, one on opposite side via periodic wrap). Nodal partition: 2 arcs. $\mathcal{N} = 2$. ✓

For torus: same as bulk-localized 2D — translation modes are exactly graph automorphisms; IBP holds with periodic boundary condition (no boundary terms). $\mathcal{N} = 2$ per axis.

### 3.3 Refined Lemma 3 statement (dimensional generality)

Replace "2D bulk graph" with "translation-invariant graph or 2D bulk-localized minimizer", and extend (iii) to all dimensions.

### 3.4 Action

Edit canonical T-σ-Lemma-3 to add dimensional generality. This **fully anchors T-V5b-T-(e)** — currently the "universal" claim relies on a Lemma that only covers 2D. Post-extension: the universality is grounded.

---

## §4. Issue J — Multi-Irrep Eigenspace σ-tuple Convention

### 4.1 The problem

Lemma 1 (iii): irrep label well-defined when $\dim V_k = 1$. For $\dim V_k > 1$ with multi-irrep decomposition, Lemma 1 (ii) gives the multi-set $\{(\dim V_k^{[\rho]}, [\rho])\}$.

Commitment 14 (O5) says: "$[\rho_k] \in \mathrm{Irr}(\mathrm{Stab}_G(u^*))$ is its irrep label". This implicitly assumes single irrep per eigenspace.

For a 2-dim eigenspace $V_k = V_k^{[A_1]} \oplus V_k^{[B_1]}$ (both 1-dim irreps as in $\{(p, 0), (0, p)\}$ pair, $p$ even), the σ-tuple should list:
- (a) Single entry $(2, [A_1] \oplus [B_1], \lambda_k)$ with combined irrep tag.
- (b) Two entries $(1, [A_1], \lambda_k)$ and $(1, [B_1], \lambda_k)$ for each 1-dim sub-eigenspace.

The convention isn't specified. Both interpretations have advantages:
- (a) preserves the "one entry per Hessian eigenvalue" structure but loses 1-1 correspondence with eigenvectors.
- (b) preserves 1-1 correspondence but inflates the cutoff $K$ count.

### 4.2 Recommended convention

For consistency with T-σ-Theorem-3 (which lists $\sigma(c\mathbf{1})|_{L=4}$ as "$(2, [E], \mu_2)$" for the 2-dim $E$ irrep — interpretation (a)) and T-σ-Theorem-3 worked example "$(3, [A_1 \oplus B_1], \mu_4)$" — interpretation (a):

**Convention (a) chosen**: "Each Hessian eigenvalue with multiplicity > 1 gets ONE σ-tuple entry; the irrep field is a sum/multi-set of constituent irreps. Each constituent irrep retains its own dimension contribution. Nodal count $n_k$ is the multi-set $\{n^{[\rho]}_k\}$ per irrep component (or summed if convention prefers single number)."

Issue: nodal count for a multi-irrep eigenspace requires choosing a basis. The Schur-block isotypic basis (Lemma 1 §3 Step 3 isotypic projector $P_{[\rho]}$) gives canonical basis vectors, each with its own nodal count. So $n_k$ is well-defined as a multi-set per irrep.

### 4.3 Action

**Add convention to Commitment 14 (O5')** — companion to O7 from §2:

> **(O5') Multi-irrep eigenspace convention.** When $\dim V_k > 1$ with $V_k = \bigoplus_{[\rho]} V_k^{[\rho]}$ (Lemma 1 (ii)) containing $r > 1$ distinct irreps, the σ-tuple entry for eigenvalue $\lambda_k$ is $(\{n^{[\rho]}_k\}_{[\rho]}, \{[\rho]\}_{[\rho]}, \lambda_k)$ — a multi-set of nodal counts and irrep labels at this eigenvalue. The lex-ordering of the multi-set follows O7.

Same as O7: register as canonical change, defer to user decision.

---

## §5. Issue K — Theorem 3 Hidden Spinodal Hypothesis

### 5.1 The hidden hypothesis

T-σ-Theorem-3 says "$c$ in spinodal interior". This restricts $W''(c) < 0$. Outside spinodal, $W''(c) > 0$ and:
- $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c) > 0$ trivially for all $\beta > 0$ (Hessian positive without need for $\beta < \beta_{\mathrm{crit}}$).
- No first pitchfork bifurcation; uniform $u = c\mathbf{1}$ is globally unique stable minimum.
- Theorem 4 setup (post-bifurcation) doesn't apply.

At spinodal *boundary* ($c = (3 \pm \sqrt{3})/6$, $W''(c) = 0$):
- $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}}$ (Laplacian eigenvalue alone, no shift).
- $\mu_2 = 4\alpha\lambda_2^{\mathrm{Lap}} > 0$ (always positive on connected graph).
- $\beta_{\mathrm{crit}}^{(2)} = \infty$ (no bifurcation).

So spinodal interior is precisely the regime where Theorem 3 + Theorem 4 form the bifurcation theory. Outside spinodal: trivial, no bifurcation. At boundary: degenerate, transition.

### 5.2 Refined statement hypothesis

Add to T-σ-Theorem-3 *Hypothesis* explicitly:

> *Hypothesis:* $c \in $ spinodal interior $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ ensures $W''(c) < 0$, which is the regime where $\mu_k$ formula has nontrivial sign structure (some $\mu_k$ can become negative as $\beta$ increases past $\beta_{\mathrm{crit}}^{(2)}$, triggering the first pitchfork bifurcation — Theorem 4 setup). Outside spinodal ($W''(c) > 0$): $\mu_k > 0$ trivially for all $\beta > 0$; no bifurcation; uniform is globally stable. At spinodal boundary: $W''(c) = 0$, $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}}$ Laplacian-pure; degenerate critical case.

This makes the role of the spinodal hypothesis explicit and clarifies what's outside scope.

### 5.3 Action

Refine canonical T-σ-Theorem-3 hypothesis statement.

---

## §6. Issue L — Theorem 4 Orbit Invariance Explicit Treatment

### 6.1 The problem

`01e` §1 noted: the post-bifurcation minimizer has 4 orbit elements ($c\mathbf{1} \pm a_\epsilon \phi_{(1, 0)}$ and $c\mathbf{1} \pm a_\epsilon \phi_{(0, 1)}$). I picked $+a_\epsilon \phi_{(1, 0)}$ as representative; stabilizer $\langle s_y\rangle$.

For $+a_\epsilon \phi_{(0, 1)}$: stabilizer is $\langle s_x\rangle$ (by 90° rotation). Mode along $\phi_{(0, 1)}$ is $s_x$-trivial, mode along $\phi_{(1, 0)}$ is $s_x$-sign. Roles of trivial/sign **swap** vs my chosen representative.

Aut(G)-orbit invariance (Lemma 1 / Commitment 14 (O5)): σ is invariant under conjugation of stabilizer. $\langle s_x\rangle$ and $\langle s_y\rangle$ are conjugate via $r$ (90° rotation). So $[\rho]_{\langle s_y\rangle} = [\rho]_{\langle s_x\rangle}$ up to conjugation.

This is fine in principle but **the σ-tuple presentation depends on representative choice** — if user computes σ for $+a_\epsilon \phi_{(0, 1)}$ representative, they get $([+1]_{s_x}, [-1]_{s_x})$ but with the *first* mode being $\phi_{(0, 1)}$ — so the (irrep, mode) pairing is different.

Implication: σ-tuple is well-defined up to **representative choice in Aut(G)-orbit**, not as a strictly canonical sequence per minimizer. The σ-equivalence class is invariant; the explicit tuple is representative-dependent.

### 6.2 Action

Add to T-σ-Theorem-4 statement (after (i)):

> **(i') Orbit-representative choice.** The σ-tuple computed below is for the orbit representative $u^*_\epsilon = c\mathbf{1} + a_\epsilon \phi_{(1, 0)}$. Other orbit elements ($c\mathbf{1} - a_\epsilon \phi_{(1, 0)}$, $c\mathbf{1} \pm a_\epsilon \phi_{(0, 1)}$) yield σ-tuples with conjugate stabilizers ($\langle r^k s_y r^{-k}\rangle$); the σ-equivalence class (modulo stabilizer conjugation per Commitment 14 (O5) Aut(G)-orbit invariance) is unique. Practical computation: pick any orbit representative; σ comes out the same modulo conjugation.

### 6.3 Action

Edit canonical T-σ-Theorem-4 to add (i') orbit-representative remark.

---

## §7. Issue M — σ-Anchoring vs T-V5b-T Completeness

### 7.1 What today's supporting structures DO anchor in T-V5b-T

| T-V5b-T sub-statement | Anchored by |
|----------------------|-------------|
| (V5b-T-a) Sub-lattice: orbital, no Goldstone (max overlap < 0.5) | NOT anchored by any of L1/L2/L3/T3/T4 — empirical only (NQ-170c) |
| (V5b-T-b) Super-lattice: $d$-fold pseudo-Goldstone (max overlap > 0.9) | Partially anchored by L3 + Theorem 1 (W4-04-24, sketched) — NOT today's scope |
| (V5b-T-c) 2D commensurability splitting (direction flipping) | NOT anchored — empirical only |
| (V5b-T-d) ζ_*(G) graph-class dependent | NOT anchored — empirical (NQ-174 to quantify) |
| (V5b-T-e) Goldstone nodal = 2 universal | **Anchored** by L3 (iii) — but only after Issue I extension to general dimension |

So today's σ supporting structures partially anchor T-V5b-T (specifically (e) after extension; (b) only sketched via Theorem 1). The other T-V5b-T sub-statements remain canonical-empirical (proved by numerical experiment, not by σ-framework analytical derivation).

### 7.2 Action (clarification)

Add to T-V5b-T entry a "*σ-framework anchoring status*" footer noting which sub-statements are σ-anchored vs σ-empirical. Or add to T-σ-Lemma-3 a "*Anchoring of T-V5b-T*" cross-reference clarifying which sub-statement it grounds.

This is documentation hygiene, not a math correction. Recommended: add to T-σ-Lemma-3 entry as "*Anchors T-V5b-T-(e); other sub-statements (a, b, c, d) remain canonical-empirical pending future σ-derivations.*"

---

## §8. Issue N — Lemma 3 (i) Reframing for Primary Content

### 8.1 Current focus

T-σ-Lemma-3 (i) emphasizes the explicit IBP value $-\pi \int u^* dr$. But the *primary qualitative content* of Lemma 3 is:
- **Goldstone subspace maps injectively into ℓ=1 angular subspace, with rank = (dimension of translation Goldstone subspace).**

The explicit value is **ancillary** — it tells us the projection magnitude but the *injectivity* is what makes "Goldstone is contained in ℓ=1 sector" precise.

### 8.2 Refined (i) statement

> **(i) Goldstone-ℓ=1 injectivity.** The map $\mathcal{P}_{\ell=1}|_{\mathrm{span}(\delta u_{x_\mu})_{\mu=1}^d}: \mathbb{R}^d \to \mathbb{R}^d$ is injective (rank $d$), making the $d$-dim Goldstone subspace the natural image of the ℓ=1 angular sector restriction.
>
> **Explicit IBP identity (corollary):** $\mathcal{P}_{\ell=1, \mu}[\delta u_{x_\nu}] = -c_d \int_0^\infty u^*(r)\, dr \cdot \delta_{\mu\nu} + O(\xi_0/L)$, with $c_d = $ surface-area constant of $(d-1)$-sphere $/2$ (e.g., $c_2 = \pi$ for 2D). For tanh disk: $|\mathcal{P}_{\ell=1, \mu}[\delta u_{x_\mu}]| \approx c_d r_0$.

### 8.3 Action

Edit T-σ-Lemma-3 (i) to lead with the rank/injectivity statement.

---

## §9. Issue O — Reference Cleanup

### 9.1 Current

T-σ-Lemma-3 (canonical line 1224, sketched in `01c` §3.2) references "tanh-disk ansatz from Cor 2.2 (Cat A)" without specifying file.

### 9.2 Correct file path

Cor 2.2 is in `THEORY/logs/daily/2026-04-24/02_development.md` §5.4 (interface tail bound, exponential decay).

### 9.3 Action

Update canonical T-σ-Lemma-3 reference to include file path.

---

## §10. Issue P — Higher-Order Theorem 4 Splitting (NQ register)

### 10.1 Open question

$K_0 = K_1$ at leading order on $D_4$ free-BC due to cubic-equivariant ratio $A_2/A_1 = 4$. Higher-order normal-form coefficients (5th, 6th equivariants) could split the degeneracy at $O(\epsilon^{3/2})$ or $O(\epsilon^2)$.

If splitting occurs: at $\beta = \beta_{\mathrm{crit}} + \epsilon$ the σ-tuple has $\mu_0 = K_0\epsilon$ + $\mu_1 = K_0\epsilon - O(\epsilon^{3/2})$ (or similar). At small but finite $\epsilon$, the eigenvalues *appear equal* numerically and σ-tuple's tie-breaking convention (Issue H) determines order.

### 10.2 Action

Register as **NQ-187 (W5+ spawn)**: "Higher-order $\epsilon$-corrections to $K_0$ vs $K_1$ on $D_4$ free-BC: do they split, and at what order?"

Add to W5+ NQ list in summary.

---

## §11. Issue Q — Sanity-Test Snippet Follow-Through

### 11.1 What was promised

`91_critical_review.md` §6.G: "Add this sanity-test snippet to `04_nq174_setup.md` Day 2 morning checklist."

### 11.2 What was done

Nothing. Pure follow-through gap.

### 11.3 Action

Edit `04_nq174_setup.md` to add the sanity test snippet at top of §6 Day 2 Execution Checklist.

---

## §12. Issue R — σ-framework Forward Gaps Register

### 12.1 What today's 5 supporting structures DON'T cover

Beyond the 11 NQ already spawned (NQ-176..NQ-186), the σ-framework has structural completion gaps:

| Gap | Description | W5+ priority |
|-----|-------------|--------------|
| **σ-uniqueness theorem** | How many distinct σ-classes exist for a given graph + parameter regime? Currently empirical (R23 NQ-141: 1 class on 32×32 D4). | NQ-188 (Round 2 spawn) |
| **σ-stability under parameter variation** | Discrete jumps in σ as $\beta$ crosses bifurcation points. Cascade structure NQ-186 placeholder. | (Existing NQ-186) |
| **Multi-formation σ** | Single-formation only today; G3 W5 Day 3-4 work | (W5 G3) |
| **σ ↔ crisp object recovery** | How to extract crisp threshold from σ-tuple (matches Commitment 11 derivative-objecthood)? | NQ-189 (Round 2 spawn) |
| **σ topological invariance** | Is σ invariant under graph homeomorphism (smooth perturbation of edge weights)? | NQ-190 (Round 2 spawn) |

### 12.2 Action

Register NQ-187 (Theorem 4 higher-order), NQ-188 (σ-uniqueness), NQ-189 (σ-crisp recovery), NQ-190 (σ-topological invariance).

Add to canonical Commitment 14 footer or to theorem_status.md "spawn NQ" row.

---

## §13. Action Plan Summary

### Canonical edits (to apply):

1. **T-σ-Lemma-3 (i)**: reframe as rank/injectivity primary, value as corollary. Extend to general dimension. Add anchoring footer for T-V5b-T-(e).
2. **T-σ-Theorem-3**: add explicit spinodal hypothesis discussion.
3. **T-σ-Theorem-4 (i')**: add orbit-representative remark.
4. **Commitment 14 (O5', O7)**: add multi-irrep convention + tie-breaking convention. **Defer to user decision** (Commitment-level change beyond G0 scope).
5. **T-V5b-T**: add σ-framework anchoring status footer.

### Daily file edits:

6. **04_nq174_setup.md**: add sanity-test snippet (Issue Q follow-through).
7. **99_summary.md**: add §11 round-2 audit summary.

### Theorem status / CHANGELOG:

8. **theorem_status.md**: register NQ-187/188/189/190.
9. **CHANGELOG.md**: append "Addendum 2 (2026-04-27 night)" with round-2 audit results.

### Items deferred to user decision (non-trivial canonical changes):

- Commitment 14 (O5') multi-irrep convention — touches §11.1 Fixed Commitments.
- Commitment 14 (O7) tie-breaking convention — touches §11.1 Fixed Commitments.

These are commitment-level additions that should be reviewed before merge. I'll write the proposed text in `92` but not edit canonical directly.

### What remains if NOT applied:

Canonical T-σ-Theorem-4 (v) σ-tuple has unspecified ordering when $\lambda_k = \lambda_{k+1}$ (strictly: σ is a multi-set, not a sequence). For practical purposes, the locally-stated "lex-order trivial first" convention in T-σ-Theorem-4 entry gives a working interpretation, but global canonical convention is missing.

Recommendation: address Commitment 14 (O5')/(O7) in W5 Day 2+ as a follow-up canonical merge.

---

## §14. Net Severity Assessment (Round 2)

- **1 HIGH** (H σ-tuple tie-breaking) — affects σ well-definedness; partially mitigated by local convention in T-σ-Theorem-4; full fix needs Commitment 14 update (deferred).
- **5 MEDIUM** (I, J, K, L, R): I (Lemma 3 dimensional generality) FIXED in canonical; J (multi-irrep) partial fix via local convention; K (spinodal hypothesis) FIXED in canonical; L (Theorem 4 orbit) FIXED in canonical; R (forward gaps) registered as NQ-187..NQ-190.
- **5 LOW** (M, N, O, P, Q): M (anchoring clarity) FIXED; N (reframe) FIXED; O (reference) FIXED; P (NQ register) added as NQ-187; Q (sanity test) FIXED.

**Theorem Cat status changes from Round 2**: NONE. All 5 σ-supporting structures remain Cat A. Issue I (dimensional extension of Lemma 3) is a *strengthening* (covers more cases, still Cat A). Issue H (tie-breaking) is a *well-definedness sharpening* (no change to Cat status).

**Counts unchanged**: 43A / 57 claims / 75% fully proved.

---

## §15. Lessons Learned (Round 2)

1. **Canonical merge of supporting lemmas should include "anchor mapping"** — explicit table of which canonical claims each supporting structure grounds. This prevents claims like T-V5b-T-(e) "universal" being only partially supported by a 2D-only Lemma.

2. **σ-tuple well-definedness requires full ordering convention** — not just for primary eigenvalue ordering but for tie-breaking, multi-irrep, and orbit-representative cases. Commitment 14 needs O5'/O6/O7 sub-clauses (today only has O1-O5).

3. **Worked examples should specify hypothesis boundary cases** — Theorem 3 was implicitly only for spinodal interior; the explicit boundary case (spinodal boundary, outside spinodal) handling clarifies what's covered and what isn't.

4. **Round-1 vs Round-2 catch ratio: ~3:7 (today)** — Round-1 caught 3 critical-math errors via Cauchy-Schwarz / contradiction / character-table sanity checks. Round-2 caught 7 more issues via *structural* audit (anchoring, generality, well-definedness, reference, follow-through). Both rounds substantive; the *structural* audit isn't replaceable by numerical sanity checks.

5. **The σ-framework completion is iterative**: Today's 5 structures + NQ-176..NQ-186 (Round 1 spawn, 11) + NQ-187..NQ-190 (Round 2 spawn, 4) = 15 NQs pointing to ~5-10 future canonical entries. The framework will likely require 2-3 more canonical merges (W6, W7, W8) before reaching σ-completeness.

---

**End of 92_critical_review_round2.md.**
**Next: apply canonical edits per §13 action plan, defer Commitment 14 changes to user.**
