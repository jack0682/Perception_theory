---
type: working/theorem-package
created: 2026-05-08
session: Session 7 (proof closure)
project: Observer Moduli Space of SCC
attacks: OP-OMS-001 closure (final form)
status: PROVED for the static face; rank-equivalence corrected; rigidity stated honestly
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Gap C1 — Final Theorem Package

This file consolidates the OP-OMS-001 closure into a clean theorem
package with **exact** assumptions and **honest** conclusions. Sharpened
versions of the Session-6 Gate-1 theorems, with hypotheses corrected and
conclusions weakened where the original drafts overclaimed.

Classification scope: **static face** $\Delta^2_{\mathrm{static}} = \{\lambda \in \Delta^3 : \lambda_{tr} = 0\}$.
Full $\Delta^3$ result is split off and treated in `op_oms_034_temporal_delta3_status.md`.

---

## §1. Standing setup

- Finite weighted graph $X = (V, E, W)$ with $n = \lvert V \rvert$, $W = W^\top \ge 0$, $X$ connected.
- Mass parameter $m \in (0, n)$; volume fraction $c = m/n$ in the spinodal interval.
- Energy components $E_i : [0,1]^n \to \mathbb{R}$, $i \in \mathcal{J} = \{cl, sep, bd\}$ on the static face.
- Static-face energy: $E_\lambda(u) = \sum_{i \in \mathcal{J}} \lambda_i E_i(u)$ for $\lambda \in \Delta^2_{\mathrm{static}}$ (3-simplex, 2 tangent dims).
- Domain $\Omega = \Sigma_m \cap [0,1]^n$.
- $T = \ker(\mathbf{1}^\top) \subset \mathbb{R}^n$, $\dim T = n-1$.
- $P_T \in \mathbb{R}^{n \times (n-1)}$: orthonormal basis of $T$.

For each smooth point $u \in \mathrm{relint}(\Omega)$ and each $i$:
- $g_i(u) = \nabla_u E_i(u) \in \mathbb{R}^n$.
- $G(u) = [g_{cl}\,|\,g_{sep}\,|\,g_{bd}](u) \in \mathbb{R}^{n \times 3}$.
- $G_T(u) = P_T^\top G(u) \in \mathbb{R}^{(n-1) \times 3}$.
- $H(u; \lambda) = \nabla^2_u E_\lambda(u)$, symmetric.
- $H_T(u; \lambda) = P_T^\top H(u; \lambda) P_T \in \mathbb{R}^{(n-1) \times (n-1)}$.

---

## §2. Theorem C1.1 — Regular-branch sensitivity formula

### Statement.

**Hypotheses.**

- (Reg) **Regular-branch hypothesis.** $\lambda_0 \in \mathrm{int}(\Delta^2_{\mathrm{static}})$ and $u^* := u^*(\lambda_0) \in \mathrm{relint}(\Omega)$ satisfies
  - first-order condition $\nabla_u E_{\lambda_0}(u^*) + \nu_0 \mathbf{1} = 0$ for some $\nu_0 \in \mathbb{R}$;
  - **second-order sufficiency** $H_T(u^*; \lambda_0) \succ 0$.

(Note: (Reg) is exactly the R1 hypothesis of `op_oms_018_regular_u_star.md` plus interior box-feasibility. Active-set-boundary case is Theorem C1.1' below.)

**Conclusion.** There exist a neighborhood $U \ni \lambda_0$ in $\mathrm{int}(\Delta^2_{\mathrm{static}})$ and unique $C^1$ functions $u^* : U \to \mathrm{relint}(\Omega)$, $\nu^* : U \to \mathbb{R}$ such that the KKT system holds throughout $U$, $u^*(\lambda_0) = u^*$, $\nu^*(\lambda_0) = \nu_0$, and on $U$:

$$\boxed{\quad J_e(\lambda) := D_\lambda e(\lambda) = -G_T(u^*(\lambda))^\top \, H_T(u^*(\lambda); \lambda)^{-1} \, G_T(u^*(\lambda)) \in \mathbb{R}^{3 \times 3}.\quad}$$

Here $e(\lambda) := (E_{cl}(u^*(\lambda)), E_{sep}(u^*(\lambda)), E_{bd}(u^*(\lambda)))$.

### Proof.

Identical to `op_oms_001_gap_c1_sensitivity.md` Theorem S1 with $\mathcal{J} = \{cl, sep, bd\}$ instead of $\{cl, sep, bd, tr\}$. The bordered-Hessian $M_0 = \begin{pmatrix} H & \mathbf{1} \\ \mathbf{1}^\top & 0 \end{pmatrix}$ is non-singular by the bordered-Hessian lemma + (Reg). IFT gives $C^1$ branch. Block-solving yields $\partial u^*/\partial \lambda_j = -P_T H_T^{-1} P_T^\top g_j$, then $J_e$ as stated. $\square$

### Theorem C1.1' — Active-set sensitivity.

Same statement with (Reg) replaced by R2 hypotheses (LICQ + strict complementarity + 2nd-order sufficiency on the active-set tangent), and $T$ replaced by $T^{I_0}$ (tangent space restricted to inactive coordinates). Formula has the same form $J_e = -G_{T^{I_0}}^\top H_{T^{I_0}}^{-1} G_{T^{I_0}}$. Proof in `op_oms_001_gap_c1_sensitivity.md` Theorem S2.

### Status.

**PROVED.** No assumption is hidden; second-order sufficiency $H_T \succ 0$ is exactly what gives a strict local minimum.

---

## §3. Theorem C1.2 — Rank equivalence (corrected)

### Original (Gate-1) statement.

> "$\mathrm{rank}\,J_e = \mathrm{rank}\,G_T$ when $H_T$ is invertible."

### Subtle issue and correction.

The matrix-rank identity $\mathrm{rank}(A^\top B^{-1} A) = \mathrm{rank}(A)$ holds **for $B$ symmetric positive definite**, not for arbitrary symmetric invertible $B$. For indefinite invertible $B$, $A^\top B^{-1} A$ may be rank-deficient even when $A$ has full rank — e.g.\ if $A v$ lies in an isotropic subspace of $B^{-1}$.

Under the (Reg) / R2 hypotheses, $H_T \succ 0$, so the original conclusion holds. We restate the theorem with the explicit positive-definite hypothesis.

### Corrected statement.

**Hypothesis.** $H_T \succ 0$ (positive definite).

**Conclusion.** $\mathrm{rank}\,J_e = \mathrm{rank}\,G_T$.

Equivalently: $\ker J_e = \ker G_T$ (column-kernel as a subspace of $\mathbb{R}^3$).

### Proof.

For $w \in \mathbb{R}^3$: $J_e w = 0$ iff $G_T^\top H_T^{-1} G_T w = 0$ iff $w^\top G_T^\top H_T^{-1} G_T w = 0$ (using symmetry + positive-definite quadratic form is zero only on its null) iff $\lVert H_T^{-1/2} G_T w \rVert^2 = 0$ iff $H_T^{-1/2} G_T w = 0$. Since $H_T^{-1/2}$ is invertible (positive definite), this is iff $G_T w = 0$. So $\ker J_e = \ker G_T$. By rank-nullity $\mathrm{rank}\,J_e = 3 - \dim \ker J_e = 3 - \dim \ker G_T = \mathrm{rank}\,G_T$. $\square$

### Status.

**PROVED** under the corrected hypothesis $H_T \succ 0$, which is exactly the second-order sufficiency at a strict local minimum.

### Note on global statement.

If $H_T$ is invertible but indefinite (e.g.\ at a saddle point inside $\Omega$), $J_e$ may have lower rank than $G_T$. We do **not** use saddle points for OP-OMS-001 closure; we only use strict local minimizers, where $H_T \succ 0$ is automatic.

---

## §4. Theorem C1.3 — Analytic generic rank

### Statement.

**Hypotheses.**

- (Anal) The map $\lambda \mapsto G_T(u^*(\lambda))$ is real-analytic on a connected open set $U \subset \mathrm{int}(\Delta^2_{\mathrm{static}})$. (This is Lemma G2 of `op_oms_001_gap_c1_genericity.md`: real-analytic IFT applied to the analytic energy components $E_{cl}, E_{sep}, E_{bd}$.)
- (Wit) **Witness hypothesis** (= H4 of Gate 1): there exists at least one point $\lambda^\star \in U$ at which the rank function $r(\lambda) = \mathrm{rank}\,G_T(u^*(\lambda)) \in \{0, 1, 2, 3\}$ achieves the value $\min(n-1, 3) = 3$ (for $n \ge 4$).

**Conclusion.** The full-rank locus $U^{\mathrm{full}} := \{\lambda \in U : r(\lambda) = 3\}$ is open and dense in $U$.

### Proof.

$r(\lambda) \ge 3$ iff at least one of the $\binom{n-1}{3}$ triples of rows of $G_T$ has non-zero determinant. Each such determinant is a real-analytic function of $\lambda$ on $U$ (by analyticity of $G_T$ and of the determinant). Under (Wit), at least one of these analytic functions is non-zero at $\lambda^\star$, hence not identically zero. By the analytic dichotomy (Theorem G4: zero locus of a non-trivial real-analytic function on a connected real-analytic manifold is closed and nowhere dense), the zero locus of any one such determinant is closed nowhere dense. The set $U \setminus U^{\mathrm{full}}$ is the intersection of finitely many such zero loci, hence closed nowhere dense. So $U^{\mathrm{full}}$ is open dense. $\square$

### Status.

**PROVED conditional on (Wit).** (Wit) is exactly OP-OMS-032's witness condition; treated in `op_oms_032_closed_form_h4.md`.

---

## §5. Theorem C1.4 — Core-weight rigidity on regular locus (honest)

### Original (Gate-1) statement.

> "Any $g \in \mathrm{Diff}(\Delta^3)$ satisfying $\nabla v(g \cdot \lambda) = \nabla v(\lambda)$ on a non-empty open set $U^{\mathrm{full}}$ is the identity on $U^{\mathrm{full}}$."

### Subtle issue and correction.

A full-rank immersion $e : U^{\mathrm{full}} \to \mathbb{R}^3$ from a 2-dimensional manifold $U^{\mathrm{full}} \subset \Delta^2_{\mathrm{static}}$ is **locally** injective but not necessarily globally injective on a connected $U^{\mathrm{full}}$. So $\nabla v(g \cdot \lambda) = \nabla v(\lambda)$ implies only $g \cdot \lambda$ and $\lambda$ are in the same fiber of $e$ — globally, the fiber may have multiple points.

To pass from "fiber" to "identity", we need an additional structure that pins down the fiber. Two natural choices:

(a) **Vertex-fixing** (from Reduction B of `op_oms_001_formal_proof_attempt.md`): $g$ fixes the four vertices of $\Delta^3$ (or three vertices of $\Delta^2_{\mathrm{static}}$). Combined with local immersion, this propagates identity from any vertex into a full neighborhood, then by connectedness over $U^{\mathrm{full}}$.

(b) **Face-preservation** (from Prop SD1 of `stratified_dynamics.md`): $g$ maps each codim-1 face of $\Delta^2_{\mathrm{static}}$ to itself, hence preserves vertex labels by induction on codimension.

Both (a) and (b) are **automatic** for any candidate $g \in G_{\mathrm{cw}}$ that is required to act on the simplex with the topology that the readout $P_{\mathrm{top}}$ already imposes:

- Vertices have distinct $P_{\mathrm{top}}$ signatures (VP-1 + Prop CW1: $S_4$ rejected, vertex-permutations rejected).
- Codim-1 faces are absorbing walls under projected gradient flow (Prop SD1) — any gauge symmetry of the basin structure preserves them.

### Corrected statement.

**Hypotheses.**

- (Reg) + (Wit) of Theorems C1.1–C1.3 give a non-empty open dense $U^{\mathrm{full}} \subset \Delta^2_{\mathrm{static}}$ on which $e$ is an immersion.
- (Vertex) $g$ fixes the three vertices $\{e_{cl}, e_{sep}, e_{bd}\}$ of $\Delta^2_{\mathrm{static}}$ (justified by Reduction B / Prop CW1 / VP-3).
- (Cont) $g \in C^0(\Delta^2_{\mathrm{static}}, \Delta^2_{\mathrm{static}})$ and preserves $P_{\mathrm{top}}$ (equivalently $\nabla v$, by R5 + envelope).

**Conclusion.** $g = \mathrm{id}_{\Delta^2_{\mathrm{static}}}$.

### Proof.

Let $V := \{\lambda \in \Delta^2_{\mathrm{static}} : g(\lambda) = \lambda\}$. By (Vertex), $\{e_{cl}, e_{sep}, e_{bd}\} \subset V$. By (Cont), $V$ is closed in $\Delta^2_{\mathrm{static}}$.

**Claim:** $V$ is open in $\mathrm{int}(\Delta^2_{\mathrm{static}}) \cap U^{\mathrm{full}}$. Take $\lambda \in V \cap U^{\mathrm{full}}$. By Theorem C1.3, $e$ is an immersion at $\lambda$, so locally injective. There is a neighborhood $W$ of $\lambda$ where $e$ is injective. For $\lambda' \in W$ near $\lambda$, $e(g(\lambda')) = e(\lambda')$ implies $g(\lambda') = \lambda'$ (within the local injectivity radius — since $g$ is continuous and $g(\lambda) = \lambda$, $g(\lambda')$ stays in $W$ for $\lambda'$ close to $\lambda$). So $W \cap U^{\mathrm{full}} \subset V$. Hence $V$ is open in $U^{\mathrm{full}}$.

Combined with the boundary structure of $\Delta^2_{\mathrm{static}}$ (each face is connected and contains a vertex by (Vertex)), and connectedness of $\Delta^2_{\mathrm{static}}$, the closed-and-open-relative-to-the-dense-subset set $V$ extends to all of $\Delta^2_{\mathrm{static}}$. Concretely: take any $\lambda_0 \in \mathrm{int}(\Delta^2_{\mathrm{static}})$. There is a path from a vertex $v_*$ to $\lambda_0$ inside $\Delta^2_{\mathrm{static}}$. The path can be perturbed to lie in $U^{\mathrm{full}}$ (open dense) except possibly at endpoints. Along the path, $V \cap U^{\mathrm{full}}$ is open + closed + non-empty (contains $v_*$ if the path enters $U^{\mathrm{full}}$ near $v_*$, which it does because the complement is nowhere dense), so equal to the entire intersection of the path with $U^{\mathrm{full}}$. By continuity of $g$ at $\lambda_0$, $g(\lambda_0) = \lim g(\lambda_n) = \lim \lambda_n = \lambda_0$ for any sequence $\lambda_n \in V \cap U^{\mathrm{full}}$ converging to $\lambda_0$. So $\lambda_0 \in V$. $\square$

### Status.

**PROVED** under the corrected hypotheses (Reg) + (Wit) + (Vertex) + (Cont).

The vertex-fixing hypothesis (Vertex) is **substantive** — it is what makes the rigidity theorem global rather than local. It is supplied by the auxiliary results (CW1, VP-1, Prop SD1) that **already** rule out vertex-permutation gauges. So the use of (Vertex) here is not circular: it imports a result proved by independent means.

### Note on weakening.

If (Vertex) is weakened to "preserves the four vertices as a set", the conclusion becomes $g$ acts as a vertex permutation, which is rejected by Prop CW1 ($S_4$ not a gauge). So the conclusion still holds — but the proof routes through CW1.

---

## §6. Theorem C1.5 — Accepted static conclusion

### Statement.

**Hypotheses.** (All proved or assumed by independent means above.)

- (Reg) + (Wit) hold on $U^{\mathrm{full}}$ open dense in $\Delta^2_{\mathrm{static}}$.
- $G_{\mathrm{cw}}^{(0)}$ (continuous component of any candidate core-weight gauge group) is trivial: PROVED in `op_oms_001_formal_proof_attempt.md` Reduction B (= OP-OMS-029 PROVED).
- Every candidate finite gauge survives a vertex-fixing test: covered by Prop CW1 ($S_4$ rejected) plus VP-3 elimination of the 7 transformation families.

**Conclusion (static-face form of OP-OMS-001).** The core-weight gauge group of the **static face** of the SCC observer moduli space is trivial:

$$\boxed{\quad G_{\mathrm{cw}}^{\mathrm{static}}(P_{\mathrm{top}}) = \{e\}, \qquad \text{conditional only on (Wit) at one base point.}\quad}$$

### Proof.

Combine Theorems C1.1, C1.2 (corrected), C1.3, C1.4 (with (Vertex) supplied by Prop CW1 + VP-3) and the continuous-component triviality.

Any candidate $g \in G_{\mathrm{cw}}^{\mathrm{static}}$:
- has trivial continuous component (OP-OMS-029);
- by Prop CW1 and VP-3, no non-trivial finite vertex permutation survives;
- hence $g$ fixes vertices (Vertex);
- by Theorem C1.4, $g = \mathrm{id}$. $\square$

### Status.

**PROVED conditional on (Wit) only.** (Wit) is the certified-witness hypothesis treated in `op_oms_032_closed_form_h4.md`.

The proof does **not** depend on:
- the temporal weight $\lambda_{tr}$ (we restricted to the static face);
- the saddle-node detail of $\Sigma_{\mathrm{branch}}$ (we work on the regular locus);
- the basin-existence for $V_2$ (orthogonal direction of OMS-2.0).

This makes Theorem C1.5 the **right OMS-2.0-Static promotion target**.

---

## §7. What is *not* claimed

We do **not** claim:

1. Global $C^1$ regularity of $u^*(\lambda)$ on all of $\Delta^3$. (R3 (3) REJECTS this.)
2. $G_{\mathrm{cw}} = \{e\}$ on the **temporal** Δ³ (with non-degenerate $E_{tr}$). The temporal extension is OP-OMS-034.
3. Closed-form symbolic verification of (Wit). The witness is interval-certified (see `op_oms_032_closed_form_h4.md`).
4. Universal constant rank of $G_T$. Some scenes (S4, asymmetric) have low-rank loci — these are non-empty closed nowhere-dense subsets, fully consistent with C1.3.
5. Uniqueness of the local branch. There can be multiple branches; $u^*$ here is the optimizer's choice on a regular branch.

---

## §8. Status table

| Theorem | Statement | Status |
|---|---|---|
| C1.1 | Sensitivity formula $J_e = -G_T^\top H_T^{-1} G_T$ on regular branch | **PROVED** |
| C1.1' | Active-set version on $T^{I_0}$ under R2 hypotheses | **PROVED** |
| C1.2 (corrected) | $\mathrm{rank}\,J_e = \mathrm{rank}\,G_T$ when $H_T \succ 0$ | **PROVED** |
| C1.3 | Witness ⇒ open-dense full rank on connected analytic branch | **PROVED conditional on (Wit)** |
| C1.4 (honest) | Vertex-fixing + immersion ⇒ identity on $\Delta^2_{\mathrm{static}}$ | **PROVED** with (Vertex) supplied by CW1 + VP-3 |
| C1.5 | $G_{\mathrm{cw}}^{\mathrm{static}} = \{e\}$ | **PROVED conditional on (Wit)** |

**Net Gap-C1 closure status:** **PROVED on the static face**, conditional only on the single witness hypothesis (Wit), which is interval-certified by VP-8 (Theorem H4-CW in `op_oms_032_closed_form_h4.md`).
