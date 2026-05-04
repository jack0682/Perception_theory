# r22_a2_a1_audit.md — (β) R22 Cubic-Equivariant Derivation Audit Placeholder

**Status:** placeholder / scope-only. Created 2026-05-04 W6 D1 EOD per Issue #3 deeper audit (parking-lot Issue #3 development).
**Type:** Audit working file. Target: independently re-derive $A_2/A_1$ on $D_4$ free-BC grid from first principles; verify R22 derivation in `working/SF/symmetry_moduli.md` §3.3 (lines 100-156).
**Estimated effort:** 1-2 weeks W6+ once executed (can run parallel to (γ) audit).
**Priority:** **medium** of three reconciliation paths α/β/γ per `sigma_theorem4_canonical_revision.md` §4.4. **Likely outcome: PASS** (R22 derivation appears correct per W6 D1 EOD reconciliation).

---

## §1. Mission

> **"Independently re-derive $A_2/A_1$ on $D_4$ free-BC grid for the post-bifurcation reduced Lyapunov function $F(a,b) = \tfrac{\mu}{2}(a^2+b^2) + A_1(a^4+b^4) + A_2 a^2 b^2$. Verify R22's claim $A_2/A_1 = 4$ at continuum + finite-L correction."**

---

## §2. R22 Derivation Recap (from `symmetry_moduli.md` §3.3 lines 100-156)

### §2.1 Setup

Continuum domain: $D_4$ free-BC unit square $[0,1]^2$. Eigenmodes (Fielder doublet):
$$\phi_{1,0}(x, y) = \sqrt{2} \cos(\pi x), \qquad \phi_{0,1}(x, y) = \sqrt{2} \cos(\pi y).$$
Both have eigenvalue $\lambda_1 = \pi^2$ (degenerate doublet at the spinodal).

### §2.2 Reduction

Substitute $u(x, y) = c + a \phi_{1,0} + b \phi_{0,1}$ into the SCC energy. The double-well term contributes (line 109):
$$\int W(c + \delta u) \, dx \, dy = W(c) - \tfrac{1}{2} \int (\delta u)^2 + \int (\delta u)^4$$
(at $c = 1/2$, $W(u) = u^2(1-u)^2$ has $W_4$-coefficient $+1$, no cubic by $\mathbb Z_2$ symmetry).

Quartic expansion (line 113):
$$\int (a \phi_{10} + b \phi_{01})^4 = a^4 I_4 + 4 a^3 b J + 6 a^2 b^2 K + 4 a b^3 J + b^4 I_4$$
where $I_4 = \int \phi_{10}^4$, $K = \int \phi_{10}^2 \phi_{01}^2$, $J = \int \phi_{10}^3 \phi_{01}$.

By reflection symmetry $\phi_{10}(1-x, y) = -\phi_{10}(x, y)$, **$J = 0$**.

### §2.3 Integral evaluations

- $I_4 = \int_0^1 \int_0^1 (\sqrt 2 \cos \pi x)^4 \, dx \, dy = 4 \int_0^1 \cos^4 \pi x \, dx = 4 \cdot \tfrac{3}{8} = \tfrac{3}{2}$.
- $K = \int (\sqrt 2 \cos \pi x)^2 (\sqrt 2 \cos \pi y)^2 \, dx \, dy = 4 \cdot \tfrac{1}{2} \cdot \tfrac{1}{2} = 1$.
- **$K / I_4 = 2/3$** (raw integral ratio).

### §2.4 W-potential expansion coefficients

Reduced Lyapunov function:
$$F(a, b) = \tfrac{\mu}{2}(a^2 + b^2) + A_1 (a^4 + b^4) + A_2 a^2 b^2$$
with:
- $A_1 = \beta_{\mathrm{bd}} \cdot I_4 = (3/2) \beta_{\mathrm{bd}}$ (factor 1 on $a^4 I_4$ in expansion).
- $A_2 = 6 \beta_{\mathrm{bd}} K = 6 \beta_{\mathrm{bd}}$ (factor 6 on $6 a^2 b^2 K$ in expansion — multinomial coefficient).
- **$A_2 / A_1 = 6 K / I_4 = 6 \cdot (2/3) = 4$** ✓ (R22 claim).

### §2.5 Lattice (finite-$L$) correction

Per `symmetry_moduli.md` §3.4 lines 164-173: $I_4^{\mathrm{lattice}} = (3/2)(1 + O(1/L^2))$, $K^{\mathrm{lattice}} = 1 \cdot (1 + O(1/L^2))$. Ratio $A_2/A_1 = 4$ preserved up to $O(1/L^2)$ correction; axis selection holds at any $L \geq 4$ (50% margin between $1/16 < 1/24$).

---

## §3. Audit Verification Checklist

When executed, this audit should verify:

1. **Multinomial coefficient**: confirm $\binom{4}{2,2}/2 = 6$ appearing in the $a^2 b^2$ cross-term coefficient.
2. **Reflection-symmetry vanishing**: confirm $J = 0$ via parity analysis.
3. **Integral evaluations**: independently compute $I_4 = 3/2$, $K = 1$ on continuum $[0,1]^2$.
4. **Reduced-potential normalization**: verify the factor $\beta_{\mathrm{bd}}$ absorption is consistent with the SCC energy convention used in `scc/energy.py` (cross-check `EnergyComputer` definition).
5. **Discrete-to-continuum convergence**: independently compute $A_2^L/A_1^L$ at $L \in \{4, 8, 16, 32, 64\}$ via discrete sums (cross-check with `nq187b_L_extrapolation.md` §2.6 corrected table).
6. **Axis-aligned minimum existence**: verify the equilibrium $(A, 0)$ with $A^2 = -\mu/(4 A_1)$ is genuine minimum (not saddle).
7. **Hessian at minimum**: independently compute $F_{aa}, F_{bb}$ at the axis-aligned $(A, 0)$; verify ratio $F_{aa}/F_{bb} = 2$ at leading order.
8. **Diagonal saddle structure**: verify the $(B, B)$ orbit gives $F_{\mathrm{diag}}$ with one negative Hessian eigenvalue (Morse index 1).

### §3.1 Expected outcome

Per the W6 D1 EOD reconciliation insight in `sigma_theorem4_canonical_revision.md` §2.5: R22 derivation is **likely correct**. The "two-orders-of-magnitude discrepancy" between naive $K/I_4 = 2/3$ and R22 $A_2/A_1 = 4$ is **resolved by the multinomial factor 6** — they are the same continuum quantity in different normalizations.

The audit's primary value is **independent verification + finite-$L$ extrapolation cross-check**. Likely outcome: PASS at continuum + small $O(1/L^2)$ correction at finite $L$.

If the audit identifies an actual error in R22 derivation (β-fail outcome): T-σ-Theorem-4 Cat C retraction candidate per `sigma_theorem4_canonical_revision.md` §4.5 Path β-fail. Per current evidence, **β-fail probability ≈ 5%**.

---

## §4. Cross-References

- `working/SF/symmetry_moduli.md` §3.3 + §3.4 — R22 derivation source (lines 100-173).
- `working/SF/sigma_theorem4_canonical_revision.md` §2.5 (Issue #3 deeper audit) — reconciliation framework.
- `working/SF/nq187b_L_extrapolation.md` §2.6 (post-W6 D1 EOD update) — discrete sum tables.
- `working/SF/sigma_m_hessian_convention_audit.md` (companion (γ) audit, also placeholder).
- `THEORY/canonical/canonical.md` §13 T-σ-Theorem-4 entry — canonical (ii) statement (audited via β path).

---

## §5. Status

**Placeholder only**. To be developed when (β) audit executes (W6+ medium priority per `sigma_theorem4_canonical_revision.md` §4.4). Cross-referenced by:
- `sigma_theorem4_canonical_revision.md` §4.2 + §4.4 + §4.5 (path β-fail decision)
- `nq187b_L_extrapolation.md` §2.6.1 (β-audit confirmation expected)
- `sigma_theorem4_higher_order.md` §11

This file's existence resolves a previously-broken cross-reference (file did not exist before 2026-05-04 W6 D1 EOD).

---

**End of placeholder. Promotion target**: β-path audit completion → input to T-σ-Theorem-4 Cat A re-promotion decision at CV-1.7+ post `sigma_theorem4_canonical_revision.md` §4.5 path tree.
