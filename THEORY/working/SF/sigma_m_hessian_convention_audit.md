# sigma_m_hessian_convention_audit.md — (γ) Σ_m-Hessian Convention Audit Placeholder

**Status:** placeholder / scope-only. Created 2026-05-04 W6 D1 EOD per Issue #3 deeper audit (parking-lot Issue #3 development).
**Type:** Audit working file. Target: identify whether canonical T-σ-Theorem-4 (ii) "Mode 0 = Mode 1 = $4|W''(c)|\epsilon$ at leading order" is a uniform-point statement (γ-i, scope clarification) or an axis-minimum statement with formula error (γ-ii, formula correction).
**Estimated effort:** 3-5 days W6+ once executed.
**Priority:** **highest** of the three reconciliation paths α/β/γ per `sigma_theorem4_canonical_revision.md` §4.4.

---

## §1. Mission

> **"Determine which Hessian-evaluation point + which Σ_m-projection convention NQ-187 uses, and cross-check against canonical T-σ-Theorem-4 (ii) and R22 derivation. Resolve the apparent 'leading-order ratio 2 vs degenerate' contradiction."**

The canonical T-σ-Theorem-4 (ii) statement reads (per `theorem_status.md` C-0716):
> "Continuum-limit Mode 0 = Mode 1 = $4|W''(c)|\epsilon$ degenerate; discrete-grid measured $\mu_1/\mu_0 \approx 2$"

R22 derivation (`symmetry_moduli.md` lines 148-150) computes axis-aligned minimum Hessian $F_{aa}/F_{bb} = 2$ — non-degenerate at leading order.

NQ-187 measurement (`sigma_theorem4_canonical_revision.md` §2.1) measures Hessian "at first-pitchfork minimizer" — also at the post-bifurcation minimum, finds $\mu_1/\mu_0 \approx 2$.

**Question**: where does the "$4|W''(c)|\epsilon$ degenerate" claim come from, and does it correspond to the same evaluation point as R22 + NQ-187?

---

## §2. Audit Scope (when executed)

### §2.1 Σ_m-projection conventions to test

Two common conventions in the literature:

- **Convention I (centered/intrinsic)**: project gradient + Hessian onto tangent simplex $T_u\Sigma_m = \{v \in \mathbb R^n : \sum_i v_i = 0\}$. Equivalently, subtract the mean: $v_i \to v_i - \bar v$.
- **Convention II (Lagrange multiplier extrinsic)**: use Lagrange multiplier reduction. The constrained Hessian on $\Sigma_m$ is $H - \lambda \mathrm{Id}_{\perp}$ where $\lambda$ is the multiplier and $\mathrm{Id}_\perp$ projects onto the constraint normal $\mathbf 1 / \sqrt{n}$.

These two conventions should give the **same eigenvalues for tangent-space directions**, but differ on the multiplier's role and the absorbed constant.

### §2.2 Evaluation points

Three candidate evaluation points for the Hessian:
- **(P1)** Uniform point $u = c \mathbf{1}$ (the spinodal saddle / bifurcation point).
- **(P2)** Post-bifurcation axis-aligned minimum $u^* = c\mathbf{1} + a_\epsilon \phi_{(1,0)} + O(\epsilon)$ with $a_\epsilon = c_R \sqrt{\epsilon}$.
- **(P3)** Post-bifurcation diagonal saddle $u_{\mathrm{diag}} = c\mathbf{1} + b_\epsilon (\phi_{(1,0)} + \phi_{(0,1)}) + O(\epsilon)$.

### §2.3 Cross-check matrix

For each (Convention, Evaluation point) combination, compute $(\mu_0, \mu_1)$ symbolically on $L = 4$ grid:

| Convention \ Point | (P1) Uniform | (P2) Axis min | (P3) Diagonal saddle |
|---|---|---|---|
| (Conv I) Centered | TBD | TBD | TBD |
| (Conv II) Lagrangian | TBD | TBD | TBD |

Predicted (R22 §3.3): At (P2) under either convention, $F_{aa}/F_{bb} = 2$, leading order $\mu_0 / \mu_1 = 2$ with $\mu_0 = 4|W''(c)|\epsilon, \mu_1 = 2|W''(c)|\epsilon$ (assuming $\mu = -2\epsilon|W''(c)|$ convention).

Predicted (canonical ii): At (P1) under Conv I (centered), Fiedler doublet eigenvalues $\mu_0 = \mu_1 = -2\epsilon|W''(c)|$ degenerate at leading order; 4th-order correction lifts degeneracy with $A_2/A_1 = 4$ structure.

### §2.4 Decision criterion

If NQ-187 measures (P2, Conv I) and obtains $\mu_1/\mu_0 = 2$: **agreement with R22 axis-minimum prediction**. The canonical (ii) (which describes (P1) uniform-point degeneracy) is **a different statement, not falsified by NQ-187**. Resolution: **path γ-i** (scope clarification, no formula error).

If NQ-187 measures (P2) but obtains $\mu_1/\mu_0 = 2$ where canonical (ii) was intended to describe (P2): **canonical (ii) formula error**. Resolution: **path γ-ii** (formula correction).

If NQ-187 + canonical convention map differs in ways not captured above: deeper audit needed.

---

## §3. Cross-References

- `working/SF/symmetry_moduli.md` §3.3 — R22 axis-aligned analysis (lines 100-156).
- `working/SF/sigma_theorem4_canonical_revision.md` §2.5 (Issue #3 deeper audit insight) — refined reconciliation framework.
- `working/SF/nq187b_L_extrapolation.md` §2.6.1-§2.6.2 (Issue #3 reconciliation) — multinomial factor 6 + measurement-position analysis.
- `THEORY/canonical/canonical.md` §13 T-σ-Theorem-4 entry — canonical (ii) statement.
- `THEORY/canonical/theorem_status.md` line 196 — C-0716 row with continuum-vs-discrete caveat.

---

## §4. Status

**Placeholder only**. To be developed when (γ) audit executes (W6 Day 1-3 priority per `sigma_theorem4_canonical_revision.md` §4.4). Cross-referenced by:
- `sigma_theorem4_canonical_revision.md` §4.3 + §4.4
- `nq187b_L_extrapolation.md` §2.6.2 (open question registration)
- `sigma_theorem4_higher_order.md` §11 (NQ-187b cross-validation)

This file's existence resolves a previously-broken cross-reference (file did not exist before 2026-05-04 W6 D1 EOD).

---

**End of placeholder. Promotion target**: γ-path audit completion → input to T-σ-Theorem-4 Cat A re-promotion decision at CV-1.7+ post `sigma_theorem4_canonical_revision.md` §4.5 path tree.
