---
type: working/theory
created: 2026-05-08
session: Session 5
project: Observer Moduli Space of SCC
stage: OMS-1.1 → OMS-1.2 candidate
attacks: OP-OMS-005, OP-OMS-016
---

# Effective Degrees of Freedom — Theory

Foundation for VP-6. States the formal definitions of "dimension" relevant to
OMS, the effective response dimension via the readout Jacobian, and two
propositions (ED1, ED2) connecting formal/quotient/effective dimensions.

Classification: **DEFINED** | **PROVED** | **PROOF SKETCH** |
**HYPOTHESIZED** | **OPEN**.

---

## §1. Three notions of dimension

Let $\Theta = (q, \lambda, \xi) \in \mathcal{M}_{\mathrm{obs}}$ be the observer
configuration and $\mathfrak{M} = \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$ the moduli space.
Three distinct dimensional notions enter OMS, and conflating them is the
single most common overclaim in this corner of the literature (AUDIT-002,
AUDIT-016).

### DEF-ED1. Raw / formal dimension. [DEFINED]

$$\dim_{\mathrm{raw}}(\mathcal{M}_{\mathrm{obs}}) = \sum_i \dim(\mathrm{factor}_i).$$

For the canonical OMS factorization $[q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$
(DEF-4): $\dim_{\mathrm{raw}} = 1 + 3 + 4 = 8$ (with $B_\xi = (0,4) \times (0,\varepsilon_{\max}] \times (0,1) \times (0,1)$).

### DEF-ED2. Constraint-reduced dimension. [DEFINED]

After applying the simplex normalization ($\sum \lambda_i = 1$, $-1$ DOF) and any
fixed parameters used in a given study (e.g.\ $b_D=0$, $\xi$ frozen, criticality
hypothesis $q = q_c(X_t)$):

$$\dim_{\mathrm{constraint}}(\mathcal{M}_{\mathrm{obs}}) = \dim_{\mathrm{raw}} - n_{\mathrm{constraints}}.$$

For the **minimal moduli model** ($K=1$, $\xi$ frozen, criticality):
$\dim_{\mathrm{constraint}} = 4 - 1 = 3$ (the 3-simplex $\Delta^3 \subset \mathbb{R}^4$).

### DEF-ED3. Gauge-reduced dimension. [DEFINED]

For a gauge action of group $G$ of dimension $\dim_{\mathrm{Lie}}(G) = \kappa$
(zero for finite $G$), at a point with trivial stabilizer:

$$\dim_{\mathrm{gauge}}(\mathfrak{M}) = \dim_{\mathrm{constraint}} - \kappa.$$

OMS-1.1 fact: $G_{\mathrm{SCC}}^{(0)}$ is finite (Prop 5). Therefore
$\dim_{\mathrm{gauge}}(\mathfrak{M}) = \dim_{\mathrm{constraint}}(\mathcal{M}_{\mathrm{obs}})$.

### DEF-ED4. Effective response dimension. [DEFINED]

Let $R : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}^p$ be the smooth part of the readout map (e.g.\ the
diagnostic vector $d_\Theta$ together with continuous topological summaries
$\ell_{\max}, \ell_{\mathrm{sec}}, A, c_{\max}$ — see DEF-22).

For $\Theta_0 \in \mathcal{M}_{\mathrm{obs}}$ where $R$ is differentiable, denote the readout Jacobian
along the relevant tangent space $T_{\Theta_0}\mathcal{M}_{\mathrm{obs}}^{\mathrm{free}}$ by:

$$J_R(\Theta_0) := D_{\Theta_0} R \in \mathbb{R}^{p \times d_{\mathrm{constraint}}}.$$

Singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_{\min(p, d_{\mathrm{constraint}})}$.

For a **threshold** $\varepsilon > 0$ (absolute or relative), define the
$\varepsilon$-effective dimension:

$$d_{\mathrm{eff}}(\Theta_0; \varepsilon) := \mathrm{rank}_\varepsilon\bigl(J_R(\Theta_0)\bigr) := \#\{i : \sigma_i \ge \varepsilon\}.$$

Two threshold conventions, both used in VP-6:

- absolute: $\sigma_i \ge \varepsilon$ in the natural readout units.
- relative: $\sigma_i / \sigma_1 \ge \varepsilon$, gauge-fixing the overall scale.

### Naming caution.

$d_{\mathrm{eff}}$ is a property of the **readout map** at a base point, not a
property of the moduli space alone. Two readouts $R, R'$ may yield different
$d_{\mathrm{eff}}$ at the same $\Theta_0$. The OMS commitment is to use
$P_{\mathrm{top}}$ smooth components (DEF-22) as the canonical $R$.

---

## §2. Proposition ED1 — Finite gauge does not reduce formal dimension

**Statement.** Let $G$ act on $\mathcal{M}_{\mathrm{obs}}$ with $\dim_{\mathrm{Lie}}(G) = 0$ (finite or, more
generally, discrete). Then at any point $\Theta_0$ with finite stabilizer,
$\dim_{\mathrm{gauge}}(\mathfrak{M}) = \dim_{\mathrm{constraint}}(\mathcal{M}_{\mathrm{obs}})$. The readout Jacobian $J_R$ may
nevertheless have $\mathrm{rank}\, J_R(\Theta_0) < \dim_{\mathrm{constraint}}$ — this is an
independent dimensional defect that is **not** caused by the gauge quotient.

**Proof.** [PROVED] For finite $G$, the orbit map $\pi : \mathcal{M}_{\mathrm{obs}} \to \mathfrak{M}$ is a
covering on the dense subset of trivial-stabilizer points, and a finite-to-one
locally Euclidean map at orbifold strata; in either case it preserves local
dimension as a manifold-with-corners (or as an orbifold). The independence
of the second statement is by example: the readout $R$ may have
$\mathrm{rank}\, J_R < \dim_{\mathrm{constraint}}$ without any gauge being present —
e.g.\ a $G = \{e\}$ action on $\Delta^2$ with a constant readout has
$\mathrm{rank} \, 0$ everywhere yet $\dim_{\mathrm{gauge}} = 2$. $\square$

**Audit consequence.** A low-rank Jacobian is **not** evidence for a hidden
gauge group. (Failure to distinguish the two is W3 in the audit log; see
also AUDIT-018 on latent symmetry scope.)

---

## §3. Proposition ED2 — Constant-rank response submanifold

**Statement.** Suppose $R : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}^p$ is $C^1$ on an open neighborhood
$U \subset \mathcal{M}_{\mathrm{obs}}$ of $\Theta_0$ and has constant rank $r$ on $U$. Then $R(U)$ is an
immersed $r$-dimensional submanifold of $\mathbb{R}^p$, and the level sets
$\{R = R(\Theta_0)\}$ in $U$ are $C^1$ submanifolds of $\mathcal{M}_{\mathrm{obs}}$ of dimension
$\dim_{\mathrm{constraint}} - r$. The level sets are precisely the
**perceptual indifference leaves** at $\Theta_0$: all observers in a leaf
produce the same smooth readout up to first order.

**Proof sketch.** [PROVED — direct application of the constant rank theorem]
Apply the constant rank theorem (e.g.\ Lee, *Smooth Manifolds*, Thm 4.12).
The image $R(U)$ has the structure of an immersed submanifold of dimension
$r$; the fiber $R^{-1}(R(\Theta_0)) \cap U$ has the structure of an
embedded submanifold of complementary dimension. $\square$

**Caveat.** Constant rank is a **strong** local hypothesis. In the SCC setting
it can fail at:

1. **Branch-switching surfaces** (OP-OMS-018): where $u^*(\lambda)$ jumps,
   $R$ may not even be continuous.
2. **Simplex strata**: at the boundary $\lambda_i = 0$ the active set of the
   constraint changes; rank may drop discontinuously (Prop SD1 in
   `stratified_dynamics.md`).
3. **Saddle-critical loci**: where two singular values cross.

In these cases the local picture is *piecewise* an ED2 submanifold; the
union over branches is a stratified set. See `op_oms_018_regular_u_star.md`
§3 for the precise claim.

**Status.** PROVED in the form stated, conditional on the constant-rank
hypothesis. The empirical question — whether constant rank actually holds
on representative SCC neighborhoods — is OP-OMS-024 (registered below).

---

## §4. Hypothesis RG1 (revised) — Effective dimension is low

**Statement (revised 2026-05-08).** Let $R = R^{P_{\mathrm{top}}}_{\mathrm{smooth}}$ be the
smooth-component readout (DEF-22 + Persist for the dynamic case). Then on
**branch-clean** finite-difference stencils ($u^*(\lambda \pm h e_j)$ on the
same $K_{\mathrm{core}}$ branch as $u^*(\lambda)$), at typical $\Theta$ in the
interior of $\Delta^3$:

$$d_{\mathrm{eff}}(\Theta; \varepsilon=0.05) \in \{1, 2\} \quad \text{(static face, } k_{\mathrm{tan}} = 2\text{)}$$
$$d_{\mathrm{eff}}(\Theta; \varepsilon=0.05) \in \{1, 2, 3\} \quad \text{(full } \Delta^3\text{, } k_{\mathrm{tan}} = 3\text{)}$$

with the lower end (1–2) the typical case and the upper end the exception.

The original Hypothesis RG1 from `rg_relevance_flow.md` predicted $d_{\mathrm{eff}} \in [2, 4]$
across the full 8-dimensional $\mathcal{M}_{\mathrm{obs}}$. The revised range above is a sharper
*per-stratum* estimate restricted to the simplex $\lambda$-axes (with
$q, \xi$ held at canonical values). VP-6 tests the revised hypothesis.

**Status.** HYPOTHESIZED. Will be classified COMPUTATIONALLY SUPPORTED /
HYPOTHESIZED / REJECTED depending on VP-6 results.

---

## §5. Why this matters for OMS

ED1 + ED2 combined explain the most common motivation for OMS:

> The observer space is "small" not because the formal dimension is small,
> but because the readout cannot distinguish many local directions.

This is a **first-order** statement about the smooth response map. It does
not contradict:

- Branch-switching surfaces (which **are** distinguishable: they correspond
  to observer-type transitions, VP-1 / VP-4 evidence).
- Topological discriminators ($K_{\mathrm{core}}$, $n_{\mathrm{high}}$ — discrete; not
  in the smooth Jacobian).

So a low $d_{\mathrm{eff}}$ across a branch is fully compatible with $\mathfrak{M}$
having multiple perceptual types — the types are separated by branch
boundaries (codim-1 discontinuities), not by Jacobian-detectable continuous
directions.

This reconciliation is registered as the OMS-1.1 → OMS-1.2 conceptual
update.

---

## §6. New open problems registered

### OP-OMS-024 — Constant-rank regions for $P_{\mathrm{top}}$.

Identify open subsets of the simplex on which $R$ has constant rank and
classify the rank distribution. Required for ED2 to apply.

### OP-OMS-025 — Empirical correspondence.

Relate the per-base-point $d_{\mathrm{eff}}(\Theta; \varepsilon)$ from VP-6
to empirically observed perceptual style dimensions (EP-1).

### OP-OMS-026 — Branch-switching loci.

Characterize the codim-1 surfaces in $\Delta^3$ on which $u^*(\lambda)$
exchanges branches — the **observer-type transition surfaces**. These are
the loci where ED2 fails.

(All three registered in `open_problems.md`.)
