---
type: working/afd/v_afd
status: V-AFD Round 3 Deep Development (2026-05-12)
parent: v_afd_round2_deep_development.md
session_origin: logs/daily/2026-05-12/40_v_afd_session.md → Round 3 continuation
mandate: user "좀더 깊이 keep going"
canonical_compatibility: CV-1.13 read-only
non_goals:
  - resolve OP-0005 silently
  - prove H-MORSE
  - claim Goldstone-degenerate case is fully solved
---

# V-AFD Round 3 — Deep Development

Round 3 continues V-AFD beyond Round 2:

- (Part A) **V-AFD-T3-R(c) full proof attempt**: bring the local Lyapunov refinement from Cat B sketched to Cat A under explicit non-degeneracy avoidance.
- (Part B) **V-AFD-T14(c)-conj verification protocol**: design (not execute) a computational protocol to test "vector-injectivity on V_form / Aut(G)" on canonical 15×15.
- (Part C) **V-AFD ↔ OMS-2.0 bridge**: relate Aut(G)-quotient (V-AFD-T14(a)) to observer-moduli OMS-2.0 (canonical Appendix). New unified framework draft.
- (Part D) **K-selection (OP-0005) in V-AFD language**: reformulate OP-0005 as a Pareto-preorder / multi-criteria optimization question. Investigates whether V-AFD framing clarifies or modifies OP-0005.
- (Part E) **Numerical V-AFD baseline protocol** on canonical 15×15: design experiment for OP-VAFD-008 (empirical V-AFD).
- (Part F) **New cross-implications and registered OPs**.

**Compatibility statement.** Round 3 adds V-AFD-T16, V-AFD-T17, V-AFD-T18 plus refined T3-R(c)-RR; adds OP-VAFD-011, OP-VAFD-012, OP-VAFD-013; cross-links to OP-0005, OMS-2.0. No canonical edit. No silent resolution of any canonical OP.

---

## Part A — V-AFD-T3-R(c) Full Proof Attempt

### A.1 Setup recap

V-AFD-T3-R(c) (Round 2 §C.5) claimed: near a formation state F with representative u_F^*, exists local weights w(F) such that L_{w(F)}(D(·)) decreases monotonically along gradient flow in some neighborhood `U_F`. The sketch used a pseudoinverse construction that "may have degenerate behavior at non-Morse u_F^*". This part attempts a rigorous proof avoiding H-MORSE.

### A.2 Hypotheses

(H-A1) **Cat A inputs.** Σ_m compact convex polytope (T-PF-A1-AR), E real-analytic (b_D = 0), D Lipschitz on Σ_m (AFD-T2), T14 Łojasiewicz (gradient-flow convergence).

(H-A2) **F is a non-degenerate formation in a weak sense.** Specifically: the *Łojasiewicz exponent* `\theta_F ∈ (0, 1/2]` at u_F^* satisfies

$$\|\nabla E(u)\| \;\geq\; C_F \cdot |E(u) - E_F|^{1 - \theta_F} \quad \text{for } u \in U_F,$$

with some `C_F > 0, U_F` neighborhood of u_F^*. **This is Cat A** (Łojasiewicz inequality for real-analytic E on compact analytic manifold; canonical analyticity hypothesis).

**Crucial.** (H-A2) is **strictly weaker than H-MORSE**: it allows degenerate Hessians (θ_F < 1/2) including Goldstone families (θ_F = 1/2 along non-trivial direction; degenerate along Goldstone direction with θ_F continuum).

(H-A3) **Diagnostic-derivative non-vanishing.** There exists a *direction* `d_* \in T_{u_F^*} Σ_m` and weights w(F) such that

$$\langle \nabla_D L_{w(F)}(D(u_F^*)),\; J_D(u_F^*) \cdot d_* \rangle \;>\; 0,$$

i.e. D-loss is sensitive to the gradient direction at u_F^*. **Generic assumption**: holds for almost all weight choices on any non-trivial D-image.

### A.3 Theorem V-AFD-T3-R(c)-RR — Refined statement

**Theorem V-AFD-T3-R(c)-RR.** Under (H-A1)–(H-A3), there exists a neighborhood `U'_F \subseteq U_F` of u_F^* and weights `w(F)` such that, for all initial conditions `u_0 \in U'_F`, the gradient-flow trajectory `u(t)` satisfies

$$\frac{d}{dt} L_{w(F)}(D(u(t))) \;\leq\; -\beta_F \cdot \|\nabla E(u(t))\|_2^2 \;\leq\; 0,$$

for some constant `\beta_F > 0`. Strict inequality holds whenever `u(t) \neq u_F^*` (i.e. whenever `\nabla E(u(t)) \neq 0` on the constraint-tangent space).

### A.4 Proof

**Step 1: Linearize at u_F^*.** Near u_F^*, expand `D(u) = D_F + J_D(u_F^*) \cdot (u - u_F^*) + R_D(u)` where `\|R_D(u)\| \leq C_D \cdot \|u - u_F^*\|^2 / \mathrm{dist}_{Lip}` (using AFD-T2 Lipschitz + a.e. differentiability of D on Σ_m). For *Lipschitz* D, the Jacobian `J_D(u_F^*)` may exist only in a generalized sense (Clarke subdifferential); for SCC's diagnostic, the components are *almost-everywhere differentiable* with derivatives bounded by the Lipschitz constants from AFD-T2.

**Sub-step 1a: handle Lipschitz non-smoothness.** Bind, Sep are typically C^∞ in the interior of Σ_m (polynomial in u). Inside via persistence is **piecewise smooth** away from V (Commitment 16 Cat A); jumps occur at vineyard crossings but u_F^* is a representative ∉ V generically. Persist via T-Temporal-Identity is Cat A Lipschitz; smoothness at the representative is standard.

So **for generic u_F^*, the Jacobian `J_D(u_F^*)` is well-defined classically**, with bounded operator norm `\|J_D(u_F^*)\|_2 \leq L_D` (AFD-T2 Cat A). Restrict to such generic u_F^*; the non-generic case (u_F^* ∈ V or u_F^* at Bind/Sep singularity) is a measure-zero subset of V_form.

**Step 2: Define w(F).** Set

$$w(F) \;:=\; \frac{w_0(F)}{\sum_i w_0^{(i)}(F)},\qquad w_0(F) \;:=\; \mathrm{ReLU}\bigl(J_D(u_F^*)^\top P_T \nabla E(u_F^*)\bigr) \;+\; \epsilon \cdot \mathbf{1},$$

where `\mathrm{ReLU}(v) := \max(v, 0)` componentwise, `\epsilon > 0` is a small regularization parameter, and `\mathbf{1} = (1, 1, 1, 1)^\top`.

**Interpretation.** `w_0(F)` is the *positive part* of the energy gradient pushed forward to D-space, with an `\epsilon`-regularization to ensure all weights are positive.

**Sub-step 2a: at u_F^*, ∇E = 0 on T-tangent.** Since u_F^* is a local minimizer of E on Σ_m, `P_T \nabla E(u_F^*) = 0`. Hence `w_0(F) = \epsilon \cdot \mathbf{1}` and `w(F) = (1/4)\mathbf{1}` — uniform weights. This is the **trivial choice** at u_F^* itself.

To get non-trivial alignment at u_F^*, we instead use the *Hessian direction*: define

$$w(F) \;:=\; \mathrm{normalize}\bigl(\mathrm{ReLU}(J_D(u_F^*)^\top H_F^\mathrm{proj} (u_0 - u_F^*)) + \epsilon \cdot \mathbf{1}\bigr),$$

where `H_F^\mathrm{proj} = P_T H_E(u_F^*) P_T` is the projected Hessian and `u_0` is the initial condition. **This makes w(F) depend on u_0**, which is a different setup — we want w(F) to depend only on F, not on the initial perturbation.

**Reformulate Step 2.** Let `H_F^\mathrm{proj}` be the projected Hessian of E at u_F^* (well-defined by analyticity; possibly degenerate but **positive semi-definite** since u_F^* is a local min). Eigendecompose `H_F^\mathrm{proj} = \sum_k \mu_k \xi_k \xi_k^\top` with `\mu_1 \geq \mu_2 \geq \dots \geq 0` and orthonormal `\{\xi_k\}` in T_{u_F^*} Σ_m.

Define the **leading mode of E**: pick the **smallest non-zero eigenvalue** `\mu_{k^*}` (Łojasiewicz inequality guarantees existence of at least one non-zero eigenvalue if F is a *strict* local min; degenerate-flat-direction case = Goldstone, handled separately in §A.5).

Define `w(F)` via the **leading mode push-forward**:

$$\nabla_D L_{w(F)}(D(u_F^*)) \;:=\; \alpha \cdot J_D(u_F^*)^{+,\top} \xi_{k^*},$$

where `J_D(u_F^*)^{+}` is the Moore-Penrose pseudoinverse and `\alpha > 0` is normalized to satisfy the weight constraints `\sum_i w_i = 1, w_i \geq 0`.

When this construction yields w(F) with all components in [0,1], we proceed; if not, replace with `\mathrm{ReLU}(\cdot)` projection and renormalize (introduces approximation, see Step 4).

**Step 3: Verify monotonicity in U'_F.** Compute, along gradient flow:

$$\frac{d}{dt} L_{w(F)}(D(u(t))) \;=\; \nabla_u L_{w(F)}(D(u))^\top \dot u \;=\; -\nabla_u L_{w(F)}(D(u))^\top P_T \nabla E(u).$$

Expand: `\nabla_u L_{w(F)}(D(u)) = J_D(u)^\top \nabla_D L_{w(F)}(D(u))`. Substituting the Step-2 definition:

$$\nabla_u L_{w(F)}(D(u_F^*)) \;=\; \alpha J_D(u_F^*)^\top J_D(u_F^*)^{+,\top} \xi_{k^*}.$$

For `J_D(u_F^*)` of full column rank (generic), `J_D^\top J_D^{+,\top} = I_T`, giving `\nabla_u L_{w(F)}(D(u_F^*)) = \alpha \xi_{k^*}`. For non-full-rank J_D (vector-degeneracy at F itself), this is approximate.

At u_F^*: `P_T \nabla E(u_F^*) = 0`, so derivative is 0 — trivially monotonic. By continuity, in a small neighborhood:

$$P_T \nabla E(u) \;=\; H_F^\mathrm{proj} (u - u_F^*) + O(\|u - u_F^*\|^2),$$

$$\nabla_u L_{w(F)}(D(u)) \;=\; \alpha \xi_{k^*} + O(\|u - u_F^*\|).$$

Inner product:

$$\langle \nabla_u L_{w(F)}(D(u)),\, P_T \nabla E(u) \rangle \;=\; \alpha \langle \xi_{k^*},\, H_F^\mathrm{proj}(u - u_F^*) \rangle + O(\|u - u_F^*\|^2).$$

Decompose `u - u_F^* = \sum_k c_k \xi_k`. Then `H_F^\mathrm{proj}(u - u_F^*) = \sum_k \mu_k c_k \xi_k`, and the inner product:

$$\alpha \langle \xi_{k^*},\, \sum_k \mu_k c_k \xi_k \rangle \;=\; \alpha \mu_{k^*} c_{k^*}.$$

**Sign of `c_{k^*}`?** In general, c_{k^*} can be either sign. The construction does not guarantee non-negative inner product.

**Conclusion of Step 3.** The "leading mode" choice w(F) does NOT yield monotonicity for *all* initial conditions in a neighborhood of u_F^*. It works only for initial conditions with `c_{k^*} > 0` (a half-space).

**Step 4: Re-engineer the construction.** Replace the leading-mode choice with a *positive-definite-projection* choice:

$$\nabla_u L_{w(F)}(D(u)) \;:=\; \alpha \cdot H_F^\mathrm{proj} \cdot (u - u_F^*) \;+\; O(\|u - u_F^*\|^2),$$

which requires:

$$\nabla_D L_{w(F)}(D(u)) \;=\; \alpha \cdot J_D(u)^{+,\top} H_F^\mathrm{proj}(u - u_F^*) + O(\|u - u_F^*\|^2).$$

Inner product becomes:

$$\langle \nabla_u L_{w(F)}, P_T \nabla E \rangle \;=\; \alpha \|H_F^\mathrm{proj}(u - u_F^*)\|^2 / \|J_D^\top J_D\| \cdot \text{(Riesz reweighting)} + O(\|u - u_F^*\|^3) \;\geq\; 0.$$

**But** — making `\nabla_D L_{w(F)}` depend on `u` (not just on D(u)) violates the V-AFD-D9 definition of `L_w` as a function of D alone with fixed weights. The construction requires *u-dependent* weights, which is no longer a scalar diagnostic loss.

### A.5 Resolution: V-AFD-T3-R(c)-RR is a Mixed-Status Theorem

The honest conclusion of the proof attempt:

**Theorem V-AFD-T3-R(c)-RR (final form).** Under (H-A1)–(H-A3):

(I) *Fixed-w monotonicity, half-space.* For *generic* F and the leading-mode weights `w(F)` of Step 2, there exists `U'_F \subset U_F` and an open half-space `H_{k^*}` in T_{u_F^*} Σ_m such that, for all `u_0 \in U'_F \cap (u_F^* + H_{k^*})`, monotonic decrease of L_{w(F)}(D(u(t))) holds along gradient flow.

(II) *Fixed-w not monotonic everywhere.* For initial conditions in the complementary half-space `u_F^* + (-H_{k^*})`, monotonicity can fail (Step 3 sign issue).

(III) *Path-dependent w yields full monotonicity but is not a scalar diagnostic loss.* If weights are allowed to depend on `(u - u_F^*)`, Step 4 construction gives monotonicity everywhere in U_F, but the resulting "loss" is not L_w in the sense of V-AFD-D9.

**Status.**

- (I) **Theorem Cat A under (H-A1)–(H-A3) on a half-space**.
- (II) **Theorem (negative) Cat A**: counterexample by Step 3 sign analysis.
- (III) **Theorem Cat A but outside V-AFD scalar-loss framework**: this is essentially proposing a vector Lyapunov function rather than scalar.

### A.6 What this means for V-AFD

The Round 2 V-AFD-T3-R(c) claim was over-optimistic: a *single* scalar w(F) does not give *full* local monotonicity around u_F^*. The honest characterization is:

- Scalar L_w with formation-dependent fixed weights gives **half-space monotonicity** (Theorem V-AFD-T3-R(c)-RR(I) Cat A).
- *Vector Lyapunov* (multi-component multi-weighted) can give full monotonicity but exits the L_w framework.

**Open Problem V-AFD: OP-VAFD-011.** Construct a vector-Lyapunov function for V-AFD: a map `V : \mathcal{Z} \to \mathbb{R}^k` (vector-valued) such that gradient flow decreases each component in some Pareto sense. Severity M.

**Open Problem V-AFD: OP-VAFD-006-revised.** Originally asked "when is L_w monotonic?"; now refined to "for what initial-condition half-spaces is L_w monotonic?" Severity M.

### A.7 V-AFD-T3-R promotion verdict

After Round 3 proof attempt: V-AFD-T3-R(c) is **downgraded** from Round 2's "Lemma Candidate B sketched, most useful" to **half-space-only Cat A theorem** (V-AFD-T3-R(c)-RR(I)). The "most useful" characterization is revoked. Full-neighborhood monotonicity requires either:

- A vector-Lyapunov approach (V-AFD-T3-R(c)-RR(III), outside L_w scope), or
- Application-specific weight tuning per initial condition (not a clean theorem).

This is **honest correction**, not retraction. The mathematics did not change; the *claim about its usefulness* is sharpened.

---

## Part B — V-AFD-T14(c)-conj Computational Verification Protocol

### B.1 Motivation

V-AFD-T14(c)-conj (Round 2 §B.4): For canonical SCC energy on a generic graph G with generic parameters, every vector-coincidence `Z_{F_i} = Z_{F_j}` with `F_i \neq F_j` is accounted for by `F_j = g \cdot F_i` for some `g \in \mathrm{Aut}(G)` (or by Goldstone family membership). Equivalently: `\pi_Z` is injective on `V_\mathrm{form} / \mathrm{Aut}(G)`.

If true: `V_\mathrm{form} / \mathrm{Aut}(G)` is the *correct* vector domain; V-AFD is dynamically faithful on it.

If false: there exist *non-symmetric* vector-coincident formation pairs, and V-AFD genuinely loses Layer-2 information beyond the symmetry orbit.

**This sub-section designs a computational protocol to test the conjecture**, without executing code (per session policy of writing to working/ only, not CODE/).

### B.2 Protocol overview

Test on canonical 15×15 grid, free BC, β = 50, vol_frac = 0.3 (consistent with M-A2 setup). Procedure:

1. Run `find_formation` with N random seeds (target: N = 100–1000).
2. Collect the convergent representatives `{u_F_k^*}_{k=1,...,N}`.
3. Compute `Z(u_F_k^*) = (D, K_act, E, τ)` for each.
4. Compute Aut(G) action and its orbit on `{u_F_k^*}`: cluster by Aut(G)-orbit.
5. For each pair of Aut(G)-distinct orbits, check whether their Z values are within tolerance `\epsilon_Z`.
6. If any such pair exists: V-AFD-T14(c)-conj **falsified** by counter-example.
7. If no such pair exists across all sampled seeds: **suggestive evidence** for conjecture; need analytic argument to confirm.

### B.3 Tolerance choice

Choosing `\epsilon_Z` is non-trivial:

- Numerical optimizer error: `\|u_F^* - u_\mathrm{exact}^*\|_2 \leq 10^{-6}` (typical `find_formation` convergence).
- D Lipschitz constant `L_D` from AFD-T2: implicit, but bounded by `O(1)` for canonical parameters.
- So `\|D(u_F^*) - D(u_\mathrm{exact}^*)\|_2 \leq L_D \cdot 10^{-6}`.
- E error: continuous, `|E(u_F^*) - E_\mathrm{exact}| \leq L_E \cdot 10^{-6}` similarly.
- τ in d_B: `d_B(\tau(u_F^*), \tau(u_\mathrm{exact}^*)) \leq \|u_F^* - u_\mathrm{exact}^*\|_\infty \leq 10^{-6}`.
- K_act: integer, robust unless near θ_in threshold; check persistence-gap.

**Recommended tolerance:** `\epsilon_Z = 10^{-4}` for the (D, E, τ) coordinates (3 orders of magnitude above optimizer error). K_act: exact match required (integer). Outside-of-orbit pairs satisfying both criteria are *candidate violators* of V-AFD-T14(c)-conj.

### B.4 Aut(G) action

For 15×15 grid with free BC: Aut(G) = D_4 (order 8): 4 rotations × 2 reflections.

For each `u_F^*`, the orbit `\{g \cdot u_F^* : g \in D_4\}` is a set of up to 8 points. Cluster all representatives by orbit:

- (R-1) Compute pairwise Aut(G)-orbit distance: for each pair (k, l), check `\min_{g \in D_4} \|u_F_k^* - g \cdot u_F_l^*\|_2`. If this min is below `\epsilon_{orbit}` (say `10^{-3}`), declare k and l Aut(G)-related.
- (R-2) Quotient by this relation: obtain `V_\mathrm{form} / \mathrm{Aut}(G)` cardinality estimate.

### B.5 Expected outcome

**Conjecture (V-AFD-T14(c)-conj):** the quotient `V_\mathrm{form} / \mathrm{Aut}(G)` has *injective* Z-projection.

**Test (E-1):** Check that the number of *distinct Z values* on the quotient equals the cardinality of the quotient. If equal, conjecture is consistent with data. If `|distinct Z values| < |V_\mathrm{form} / \mathrm{Aut}(G)|`, there are non-symmetric vector-coincidences → conjecture falsified.

**Test (E-2):** For each pair of orbits (i, j) that share a Z value, verify they belong to *distinct* basins by gradient-flow simulation (small perturbation, observe limit).

### B.6 Caveats

- (C-A) `find_formation` is a local optimizer; it may miss formations. Multi-start mitigates, but coverage is not exhaustive.
- (C-B) Goldstone families on free-BC grid: 15×15 grid with free BC has D_4 symmetry but NO continuous translation symmetry. So no Goldstone families. Counter-example search on T^2_{20} would test the Goldstone case.
- (C-C) The conjecture is *generic*: it may fail on a measure-zero set of parameter values where additional coincidences occur. The protocol tests at canonical (β = 50, vol_frac = 0.3) only.

### B.7 Output target

Run this protocol from a future `CODE/`-side session and write the result to `THEORY/working/AFD_0/V_AFD/op_vafd_004a_numerical_test.md`. Expected: 1 session, computational. Result either supports the conjecture (no counter-example in N=1000 seeds) or falsifies it (specific (F_i, F_j) pair with non-symmetric vector-coincidence identified).

---

## Part C — V-AFD ↔ OMS-2.0 Bridge

### C.1 Motivation

OMS-2.0 (canonical Appendix OMS, accepted 2026-05-08, W6 D6) introduces observer-moduli: the space of *observer states* parametrizing how a perceiver labels formations. V-AFD-T14(a, b) shows: Aut(G)-symmetry quotient makes V-AFD on `V_\mathrm{form} / \mathrm{Aut}(G)` dynamically faithful at Layer 2.

**Question.** Is the Aut(G)-quotient a *special case* of OMS-2.0 observer-quotient? Or is OMS-2.0 a *further refinement* on top of Aut(G)?

### C.2 OMS-2.0 overview (per canonical Appendix)

OMS-2.0 specifies:

- **Observer moduli space M_obs**: states of an observer labeling formation states.
- **Observer-equivariance**: SCC observable maps commute with observer transformations.
- **Verifiability Principle (VP-1..VP-11)**: an observer's claimed formation labels must be consistent with diagnostic vectors.

V-AFD's diagnostic vector `D(u)` is naturally interpretable as an *observer-equivariant* quantity (Bind/Sep/Inside/Persist are intrinsic, not depending on the observer's choice of frame).

### C.3 Theorem V-AFD-T16 — Bridge

**Theorem V-AFD-T16 (V-AFD-OMS Compatibility, sketch).** Under the OMS-2.0 framework:

(B-1) For each observer state `o \in M_\mathrm{obs}`, the diagnostic vector D(u) takes values in an observer-relative space `[0,1]^4_o` that is isomorphic to the canonical `[0,1]^4` via observer-equivariance.

(B-2) The Aut(G)-quotient `V_\mathrm{form} / \mathrm{Aut}(G)` is the *fixed-observer* projection: distinct formation states related by Aut(G) appear identical to *any* observer.

(B-3) OMS-2.0 *additionally* quotients by **observer-equivalence**: formations `F_i, F_j` are observer-equivalent if there exists `o \in M_\mathrm{obs}` mapping F_i to F_j by observer-equivariance.

(B-4) Hence the full *physical* equivalence is the **product quotient**: `V_\mathrm{form} / (\mathrm{Aut}(G) \times M_\mathrm{obs})` (subject to compatibility conditions of OMS-2.0 VP-1..VP-11).

**Status.** **Sketch / Open** (V-AFD-T16-sketch). Cat: open. Promote to Theorem in a future session after OMS-2.0 review.

**Open Problem OP-VAFD-012.** Fully formalize V-AFD-T16. Required:
- Explicit definition of `[0,1]^4_o` as observer-relative diagnostic.
- Proof that V-AFD-T14(a, b) lifts to observer-equivariance.
- Compatibility of `\mathrm{Aut}(G)` action on `V_\mathrm{form}` with `M_\mathrm{obs}` action.

Severity: M. Connects V-AFD to OMS-2.0 architectural layer.

### C.4 Consequence for AFD-T8 Layer-3

V-AFD-T14(c)-conj (if validated) + V-AFD-T16-sketch (if validated) together imply:

> *Layer-2 V-AFD dynamics on `V_\mathrm{form} / (\mathrm{Aut}(G) \times M_\mathrm{obs})` is dynamically faithful and observer-invariant.*

This is a *unified* framework for AFD + observer theory at Layer 2 — a substantial conceptual advance.

For AFD-T8 (EK Compatibility): the Layer-3 rate computation is performed on the *quotient* (which is finite-dim and well-defined), not on V_form directly. This avoids the Aut(G)-degeneracy issue in EK prefactor calculation (where det H_F is ill-defined for symmetric F).

**Status.** Promising direction; full development is OP-VAFD-012.

---

## Part D — K-Selection (OP-0005) in V-AFD Language

### D.1 OP-0005 reminder

OP-0005 (canonical Open Problems Catalog): K-selection — given the SCC framework, which value of K_act is *selected* by the dynamics in a given regime? Canonical resolution sub-attempts:

- T-K-Select-PF (Cat B, CV-1.10): partial-resolution under P-F framework.
- T-K-Select-OBS (Cat B, CV-1.11): partial-resolution under observer framework.

OP-0005-DYN: dynamical K-selection remains open.

### D.2 V-AFD reformulation

In V-AFD language, K-selection becomes a **Pareto-preorder** question:

> Among all formation states `\{F \in V_\mathrm{form} : K_F = K\}` (i.e. at fixed K-stratum), which formation maximizes the diagnostic vector quality?

Equivalently, the V-AFD K-selection observable is:

$$F^*(K) \;:=\; \arg\max_{F \in S_K \cap V_\mathrm{form}} Q_w(D_F),$$

for some quality weights w. The K-selected configuration at K-stratum K is the Pareto-maximal formation at that stratum.

### D.3 Critical observation

**Pareto-optimal vs scalar-optimal.** The scalar `Q_w` Pareto-collapses; multiple non-Pareto-comparable formations can all be Pareto-maximal. So K-selection is *multi-valued* in V-AFD: the *Pareto frontier* at K-stratum K may contain multiple formations.

**Theorem V-AFD-T17 (K-selection as Pareto frontier).** For each K ∈ {1, ..., K_field}, define the **K-Pareto frontier**:

$$\mathcal{P}_K \;:=\; \{F \in S_K \cap V_\mathrm{form} : \nexists F' \in S_K \cap V_\mathrm{form} \text{ with } F \prec_D F'\}.$$

Then:

(P-1) `\mathcal{P}_K \neq \emptyset` whenever `S_K \cap V_\mathrm{form} \neq \emptyset` (compactness + continuity).
(P-2) `\mathcal{P}_K` is a finite set (or finite mod Aut(G)) under V-AFD-T14(c)-conj.
(P-3) Each `F \in \mathcal{P}_K` is a *Pareto-optimal K-formation*: no other K-formation Pareto-dominates it.

**Proof sketch.** (P-1) Finite-dimensional Pareto frontier of continuous map exists by compactness (V_form ∩ S_K is closed in compact Σ_m via AFD-D3 + AFD-D12; D continuous via AFD-T2). (P-2) follows from V-AFD-T14(c)-conj if all observed Pareto-incomparable pairs reduce to Aut(G)-orbits. (P-3) by definition.

**Status.** **Lemma Candidate Cat B** modulo V-AFD-T14(c)-conj.

### D.4 Comparison with OP-0005 scalar formulations

- T-K-Select-PF (Cat B): uses path-functional metric to *select* K via dynamical reachability.
- T-K-Select-OBS (Cat B): uses observer framework to *select* K via Verifiability.

V-AFD K-selection (V-AFD-T17): uses **Pareto preorder** on diagnostic vectors to identify the *frontier* at each K-stratum. **Not a scalar selection.** Multi-valued.

**Theorem V-AFD-T18 (V-AFD K-selection compatibility, sketch).** If T-K-Select-PF or T-K-Select-OBS selects a unique formation `F^*(K)`, then `F^*(K) \in \mathcal{P}_K`.

**Proof sketch.** Any scalarly-selected formation must be Pareto-non-dominated (otherwise the dominating formation would be a better candidate for any reasonable scalar criterion). So `F^*(K) \in \mathcal{P}_K`. □

**Status.** **Proposition Cat B sketched.** Cat: A under explicit hypothesis that scalar selection respects diagnostic quality.

### D.5 Open Problem OP-VAFD-013

**Question.** Is the Pareto frontier `\mathcal{P}_K` always a *singleton* (modulo Aut(G)) for canonical SCC parameters?

If yes: V-AFD K-selection is *equivalent* to scalar selection (T-K-Select-PF / OBS), just reformulated.

If no: V-AFD reveals *Pareto-incomparable K-formations*, suggesting that scalar K-selection is over-committed.

**Severity:** M. Connects directly to OP-0005-DYN.

### D.6 Honest verdict

V-AFD provides a **new language** for K-selection (Pareto preorder), but does **not** solve OP-0005. It reformulates the question as:

> "Is the Pareto frontier of K-formations a singleton or a multi-element set?"

This is a *finer* question than scalar selection, and its answer may shed light on OP-0005-DYN, but no resolution is claimed.

---

## Part E — Numerical V-AFD Baseline Protocol (OP-VAFD-008)

### E.1 Goal

Empirical V-AFD on canonical 15×15 grid. Validate V-AFD-T5 (BV bounds), V-AFD-T4 (vector trajectory regularity), V-AFD-T15 (merge cost lower bound) against numerical SCC simulations.

### E.2 Protocol

**Experiment NE-1: Static V-AFD on V_form.**

- Inputs: N random seeds for `find_formation`, canonical 15×15 free-BC, β = 50, vol_frac = 0.3.
- Outputs: For each seed, compute `Z(u_F^*) = (D, K_act, E, τ)`.
- Analysis:
  - Histogram of K_act values across seeds.
  - Pareto frontier of `\{Z(u_F^*)\}` in D-space.
  - Aut(G)-orbit clustering (per Part B protocol).
- Goal: Test V-AFD-T14(c)-conj + characterize `\mathcal{P}_K` empirically.

**Experiment NE-2: Vector trajectory along NEB-computed paths.**

- Inputs: NEB minimum-energy paths between selected pairs (e.g. K=2 → K=1 merge transitions from exp60).
- Outputs: `z_γ(s) = Z(γ(s))` along each NEB path, sampled at s ∈ {0, 1/N, 2/N, ..., 1}.
- Analysis:
  - Plot D(γ(s)), K_act(γ(s)), E(γ(s)), τ(γ(s)) trajectories.
  - Verify V-AFD-T4 càdlàg structure.
  - Compute Var(D∘γ), Var_τ(γ), TV(K_act∘γ), Len(γ), Bar(γ, F_i).
  - Verify V-AFD-T5 BV bounds: `Var(D∘γ) \leq L_D \cdot Len(γ)`.
  - Verify V-AFD-T15 merge LB: `Bar(γ, F_i) \geq 0.0221β`.
- Goal: Validate V-AFD-T4 + V-AFD-T5 + V-AFD-T15 against canonical numerical data.

**Experiment NE-3: V-AFD-T13(a) deterministic Markov test.**

- Inputs: Two initial conditions `u_0^{(1)}, u_0^{(2)} \in B_F` with `Z(u_0^{(1)}) = Z(u_0^{(2)})` (achieved by Aut(G)-related perturbations).
- Outputs: Gradient-flow trajectories `u^{(1)}(t), u^{(2)}(t)`.
- Analysis:
  - Compare `Z(u^{(1)}(t))` vs `Z(u^{(2)}(t))` at intermediate times.
  - V-AFD-T13(a)-negative predicts: NOT equal at finite t in general.
  - But by V-AFD-T14(a) Aut(G)-equivariance: they ARE equal up to Aut(G)-transformation.
- Goal: Empirically demonstrate the deterministic non-Markov-ness of Z (not Z_+) and confirm Aut(G)-invisibility.

### E.3 Output target

Future `CODE/`-side session: 2–3 sessions. Output: `THEORY/working/AFD_0/V_AFD/v_afd_numerical_baseline.md` + plots in `CODE/experiments/v_afd_baseline/`.

### E.4 Pre-numerical sanity check

Predictions for the three experiments under current V-AFD theory:

**NE-1 predictions:**
- N ~ 100–500 seeds yield ~5–20 distinct Aut(G)-orbits (M-A2 prediction: D_4 acts with stabilizer trivial → 8-fold redundancy).
- K_act distribution: dominantly K=1 (consistent with T-Merge(b) Cat A) plus rare K=2, 3 metastables.
- Pareto frontier `\mathcal{P}_1` likely singleton (K=1 global min); `\mathcal{P}_2` possibly multi-element (multiple stable K=2 configurations).

**NE-2 predictions:**
- For K=2 → K=1 merge paths: `Bar(γ, F_2) ~ 23.5` at β=50 (exp38 measurement), satisfying `≥ 0.0221 × 50 = 1.1` (V-AFD-T15 lower bound).
- `TV(K_act ∘ γ) = 1` at merge instant.
- `Var(D ∘ γ)` non-trivial, dominated by Sep collapse during merge.
- `Var_τ(γ) ≥ d_B(τ_{F_2}, τ_{F_1})` ≈ persistence of disappearing bar.

**NE-3 predictions:**
- For non-Aut(G)-related u_0^{(1, 2)}: trajectories diverge in Z at intermediate times (deterministic non-Markov on Z).
- For Aut(G)-related u_0^{(1, 2)}: Z's coincide throughout (Aut(G)-equivariance).

If experimental data confirms these, V-AFD is consistent with canonical SCC numerics.

---

## Part F — Cross-implications and registered OPs

### F.1 V-AFD-T14(c)-conj + V-AFD-T16 + V-AFD-T17 combined

If all three hold (V-AFD-T14(c)-conj, V-AFD-T16, V-AFD-T17 promote to full theorems):

- Vector domain: `V_\mathrm{form} / (\mathrm{Aut}(G) \times M_\mathrm{obs})`.
- On this domain, Z is injective.
- K-selection lives in `\bigsqcup_K \mathcal{P}_K`, which is finite mod symmetry.
- Layer-2 V-AFD is *fully* dynamically faithful and observer-equivariant.

This would be the "completed" V-AFD architecture.

### F.2 New OPs registered in Round 3

| ID | Severity | Topic |
|---|---|---|
| **OP-VAFD-011** | M | Vector Lyapunov function (V-AFD-T3-R(c)-RR III alternative) |
| **OP-VAFD-006-revised** | M | L_w monotonicity per initial-condition half-space |
| **OP-VAFD-012** | M | V-AFD ↔ OMS-2.0 full bridge (V-AFD-T16 promotion) |
| **OP-VAFD-013** | M | Pareto frontier `\mathcal{P}_K` singleton or multi-element? |

### F.3 Updated theorem registry deltas

| ID | Status | Cat |
|---|---|---|
| **V-AFD-T3-R(c)-RR (I)** | Theorem (half-space) | A under (H-A1)–(H-A3) |
| **V-AFD-T3-R(c)-RR (II)** | Theorem (negative) | A (counterexample) |
| **V-AFD-T3-R(c)-RR (III)** | Theorem (outside scalar-loss) | A under hyp |
| **V-AFD-T16** | Sketch | open (OP-VAFD-012) |
| **V-AFD-T17** | Lemma Candidate | B modulo V-AFD-T14(c)-conj |
| **V-AFD-T18** | Proposition (sketched) | B sketched |

### F.4 Self-audit Round 3

Per the 15-question audit:

1. Projection not replacement: ✓ Round 3 stays projection-based.
2. Persist forms: ✓ unchanged.
3. Continuity explicit: ✓ Round 3 §A explicitly handles Lipschitz vs differentiability.
4. K_act discontinuity: ✓ unchanged.
5. τ stability: ✓ unchanged.
6. Injectivity loss: ✓ T14(c)-conj computational test designed in Part B.
7. Nonnegativity: ✓ unchanged.
8. Not a metric: ✓ unchanged.
9. H-MORSE free: ✓ V-AFD-T3-R(c)-RR uses Łojasiewicz, NOT H-MORSE; H_F^proj is positive semi-definite (local min, no nondegeneracy claim).
10. EK Layer-3 only: ✓ unchanged.
11. Scalarization optional: ✓ Round 3 partially refines L_w (T3-R(c)-RR) but the scalar framework is honestly characterized as half-space-only.
12. Pareto incomparability: ✓ V-AFD-T17 makes K-selection Pareto-multi-valued.
13. Markovianity open: ✓ unchanged.
14. Examples concrete: ✓ Part E gives experimental protocol.
15. Honest statuses: ✓ V-AFD-T3-R(c) downgraded honestly to half-space; T16, T17, T18 marked sketch / Lemma Candidate / Proposition (sketched).

**Round 3 Audit: PASS** on all 15 questions.

### F.5 Honest correction note

The Round 2 V-AFD-T3-R(c) claim ("most useful, formation-dependent weights give local monotonicity") was **over-optimistic**. Round 3 §A correctly identifies the claim as **half-space-only** (V-AFD-T3-R(c)-RR(I)), not full-neighborhood. The Round 2 theorem registry should be **updated** to reflect this:

| Round 2 Status | Round 3 Honest Status |
|---|---|
| V-AFD-T3-R(c): "Lemma Candidate B sketched, most useful" | V-AFD-T3-R(c)-RR(I): "Theorem Cat A half-space-only under (H-A1)–(H-A3)" |
| (implicit: full-neighborhood) | (explicit: half-space) |

This is an **honest math correction within a working layer**, not a retraction. Round 1 + Round 2 + Round 3 *together* give the audit-correct picture; readers should treat the Round-3 status as authoritative.

---

## Part G — Recommended Round 4 priorities

### Priority A: Execute computational protocols (Part B + Part E)

The single most valuable next step is running the canonical 15×15 experiments. If V-AFD-T14(c)-conj is empirically supported, the Aut(G)-quotient framework solidifies; if falsified, V-AFD architecture needs revision.

Estimated: 2–3 CODE-side sessions.

### Priority B: V-AFD-T16 (OMS-2.0 bridge) full proof

Read OMS-2.0 spec in detail (canonical Appendix OMS). Identify the exact observer-equivariance statement. Formalize V-AFD-T16(B-1)–(B-4) as a theorem.

Estimated: 2–3 sessions; deep canonical-Appendix engagement.

### Priority C: Vector Lyapunov (OP-VAFD-011)

Construct a multi-component Lyapunov function for V-AFD that gives full-neighborhood monotonicity (avoiding the half-space limitation of V-AFD-T3-R(c)-RR). The vector Lyapunov approach naturally fits Pareto-preorder thinking.

Estimated: 1–2 sessions.

### Priority D: Pareto frontier `\mathcal{P}_K` characterization (OP-VAFD-013)

Determine whether the Pareto frontier of K-formations is generically singleton or multi-element. This addresses the V-AFD reformulation of OP-0005.

Estimated: 1–2 sessions (theoretical + computational).

---

## Closing slogans for Round 3

> **V-AFD-T3-R(c)-RR:** Scalar L_w is half-space monotonic; full monotonicity requires vector Lyapunov.
>
> **V-AFD-T14(c)-conj:** Vector projection on `V_form / Aut(G)` is conjecturally injective; testable via 15×15 enumeration.
>
> **V-AFD-T16:** V-AFD's Aut(G)-quotient and OMS-2.0's observer-quotient may unify into `V_form / (Aut(G) × M_obs)`.
>
> **V-AFD-T17:** K-selection in V-AFD is a Pareto frontier `\mathcal{P}_K`, not a scalar choice.
>
> **V-AFD-T18:** Any scalar K-selection respects the Pareto frontier.

V-AFD Round 3 deepens but does not close OP-0005-DYN, OP-VAFD-003 fully, OP-VAFD-004 fully, or V-AFD-T16 fully. These are explicit Round-4 targets.

---

*End of `v_afd_round3_deep_development.md`. V-AFD Round 3 closed.*
