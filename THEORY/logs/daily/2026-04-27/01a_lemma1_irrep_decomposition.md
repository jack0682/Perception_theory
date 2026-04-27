# 01a_lemma1_irrep_decomposition.md — Lemma 1 (σ-Framework, Irrep Decomposition Well-Defined)

**Session:** 2026-04-27 (W5 Day 1, G0 Block 1)
**Target (from plan.md §3 Block 1 09:30–10:30):** Lemma 1 full statement + proof + canonical wording draft.
**This file covers:** Statement (with finite-graph hypothesis explicit per `pre_brainstorm.md` §1.1), 4-step proof, references, Cat A self-classification, ready-to-paste §13 entry text.
**Depends on reading:** `04-24/02_development.md` §3 (W4-04-24 Lemma 1 first proof), `01_sigma_lemmas_review.md` §4.1 (finite-graph correction), `canonical.md` §11.1 Commitment 14 (σ-signature).

---

## §1. Statement

> **Lemma 1 (σ-Framework, Irrep Decomposition Well-Defined).** Let $G = (X, E)$ be a **finite** simple connected graph with $|X| = n$, and let $u^* \in \Sigma_m$ be a Morse-index-0 local minimum of the SCC energy $\mathcal{E}$ on the volume-constrained simplex. Let
> $$G_u := \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*) = \{\pi \in \mathrm{Aut}(G) : \pi \cdot u^* = u^*\} \leq \mathrm{Aut}(G)$$
> be the residual graph-automorphism stabilizer of $u^*$. Then:
>
> **(i)** $G_u$ acts linearly on the constraint tangent space $T_{u^*}\Sigma_m = \mathbf{1}^\perp$ via permutation of vertex coordinates: $(\pi \cdot v)_i = v_{\pi^{-1}(i)}$.
>
> **(ii)** The constrained Hessian
> $$H(u^*) := \pi_{\mathbf{1}^\perp}\,\nabla^2\mathcal{E}(u^*)\,\pi_{\mathbf{1}^\perp},\qquad \pi_{\mathbf{1}^\perp} = I - \tfrac{1}{n}\mathbf{1}\mathbf{1}^\top,$$
> commutes with the $G_u$-action: $H(u^*)\,\rho(\pi) = \rho(\pi)\,H(u^*)$ for all $\pi \in G_u$, where $\rho(\pi)$ is the permutation representation restricted to $\mathbf{1}^\perp$.
>
> **(iii)** Each Hessian eigenspace $V_k := \ker(H(u^*) - \lambda_k I)|_{\mathbf{1}^\perp}$ is $G_u$-invariant and decomposes canonically into isotypic components
> $$V_k \;=\; \bigoplus_{[\rho] \in \widehat{G_u}} V_k^{[\rho]},\qquad V_k^{[\rho]} := P_{[\rho]} V_k,\quad P_{[\rho]} := \frac{\dim\rho}{|G_u|}\sum_{\pi \in G_u}\overline{\chi_\rho(\pi)}\,\rho_{\mathrm{reg}}(\pi),$$
> where $\widehat{G_u}$ is the set of irreducible-representation isomorphism classes of $G_u$, $\chi_\rho$ is the character of $[\rho]$, and $\rho_{\mathrm{reg}}$ is the regular representation. The multi-set $\{(\dim V_k^{[\rho]}, [\rho])\}_{[\rho] \in \widehat{G_u}}$ is canonical (independent of basis choice).
>
> **(iv)** When $\dim V_k = 1$, $V_k = V_k^{[\rho]}$ for a unique $[\rho] \in \widehat{G_u}$, and the σ-framework irrep label $[\rho_k] := [\rho]$ in `canonical.md` §11.1 Commitment 14 (O5) is well-defined.

---

## §2. Hypothesis Importance Notes

### 2.1 Finiteness of $G$ is essential

If $G$ is allowed to be infinite (e.g., $\mathbb{Z}^d$), then $\mathrm{Aut}(G)$ may be infinite (e.g., contains all integer translations); $G_u$ may then be infinite, and Maschke's theorem (Step 3 below) is **inapplicable** without further hypotheses (compact Lie group + Haar measure, or amenable group + Følner sequence). The canonical theory is set on finite graphs (`canonical.md` §3.1), so the hypothesis is satisfied. Stating it explicitly avoids overreach when the σ-framework is later extended to thermodynamic-limit settings.

### 2.2 Trivial-stabilizer case $G_u = \{e\}$

For generic (asymmetric) minimizers $u^*$, $G_u = \{e\}$. Then $\widehat{G_u} = \{[\mathrm{trivial}]\}$ (the single 1-dimensional trivial irrep). Each $V_k$ decomposes as $V_k = V_k^{[\mathrm{trivial}]}$ (the entire space). Lemma 1 is vacuously true but content-free: the irrep label provides no discrimination.

Informative content of Lemma 1 concentrates at minimizers with non-trivial $G_u$ — typically: high-symmetry uniform configurations ($G_u = \mathrm{Aut}(G)$, e.g. $D_4$ on grid), and post-bifurcation minimizers with reduced but non-trivial stabilizer (e.g. $D_4 \to \mathbb{Z}_2$ at first pitchfork — see Theorem 4).

### 2.3 Morse-0 hypothesis

Required so that $H(u^*)$ has only positive eigenvalues on $\mathbf{1}^\perp$ (no zero modes from Hessian degeneracy of the energy itself; near-zero eigenvalues from broken pseudo-symmetry — Goldstone — are permitted and addressed by Lemma 3 / Theorem 1).

---

## §3. Proof

### Step 1 — $G_u$ acts on $T_{u^*}\Sigma_m = \mathbf{1}^\perp$.

The natural permutation action of $\mathrm{Aut}(G)$ on $\mathbb{R}^X$ is $(\pi \cdot v)_i = v_{\pi^{-1}(i)}$. This action permutes coordinates linearly, hence is a linear representation. It preserves:

- The simplex $\Sigma_m = \{u : \sum u_i = m,\ u_i \in [0,1]\}$ (sums and box constraints invariant).
- $\mathbf{1}$ (since $(\pi \cdot \mathbf{1})_i = 1$ for all $i$), hence $\mathbf{1}^\perp = \{v : \sum v_i = 0\}$ is preserved.
- The energy: $\mathcal{E}(\pi \cdot u) = \mathcal{E}(u)$ for $\pi \in \mathrm{Aut}(G)$ (energy depends on $u$ only through graph-structured terms — `working/SF/symmetry_moduli.md` §1.2).

Restricting to $G_u = \mathrm{Stab}(u^*)$: the action is well-defined on $\mathbf{1}^\perp = T_{u^*}\Sigma_m$. ✓

### Step 2 — $H(u^*)$ commutes with $G_u$.

For $\pi \in \mathrm{Aut}(G)$ and $v \in \mathbb{R}^X$, energy invariance gives
$$\mathcal{E}(u + \epsilon v) = \mathcal{E}(\pi \cdot (u + \epsilon v)) = \mathcal{E}(\pi \cdot u + \epsilon\,\pi \cdot v).$$

Twice-differentiating in $\epsilon$ at $\epsilon = 0$:
$$v^\top \nabla^2\mathcal{E}(u)\,v = (\pi\cdot v)^\top \nabla^2\mathcal{E}(\pi\cdot u)\,(\pi\cdot v).$$

For $\pi \in G_u$: $\pi \cdot u^* = u^*$, so
$$v^\top \nabla^2\mathcal{E}(u^*)\,v = (\pi\cdot v)^\top \nabla^2\mathcal{E}(u^*)\,(\pi\cdot v) = v^\top \pi^\top \nabla^2\mathcal{E}(u^*)\,\pi\,v.$$

By polarization (Hessians symmetric), $\nabla^2\mathcal{E}(u^*) = \pi^\top \nabla^2\mathcal{E}(u^*)\,\pi$, i.e. $\pi^{-1} = \pi^\top$ (orthogonality of permutation matrices) gives commutation $\nabla^2\mathcal{E}(u^*)\,\pi = \pi\,\nabla^2\mathcal{E}(u^*)$.

Restriction to $\mathbf{1}^\perp$: $\pi$ commutes with $\pi_{\mathbf{1}^\perp} = I - n^{-1}\mathbf{1}\mathbf{1}^\top$ (since $\pi \mathbf{1} = \mathbf{1}$). Hence $H(u^*) = \pi_{\mathbf{1}^\perp}\nabla^2\mathcal{E}(u^*)\pi_{\mathbf{1}^\perp}$ also commutes with $\pi$. ✓

### Step 3 — Isotypic decomposition (Maschke + Schur orthogonality).

$G_u$ is a finite group (Step 2.1; subgroup of finite $\mathrm{Aut}(G)$). It acts on the finite-dimensional real vector space $\mathbf{1}^\perp$. Since $G_u$ acts by permutation matrices (orthogonal), the standard inner product on $\mathbf{1}^\perp$ is $G_u$-invariant; equivalently the action is unitarizable.

By Maschke's theorem, every finite-dimensional representation of a finite group over $\mathbb{R}$ (or $\mathbb{C}$) decomposes as a direct sum of irreducible subrepresentations. Grouping by isomorphism class:
$$\mathbf{1}^\perp = \bigoplus_{[\rho] \in \widehat{G_u}} W^{[\rho]},\qquad W^{[\rho]} = m_\rho \cdot V_\rho,$$
the **isotypic decomposition** with multiplicities $m_\rho \geq 0$.

By Step 2, $H(u^*)$ commutes with $G_u$. Schur's lemma applied to each isotypic component implies $H(u^*)$ preserves each $W^{[\rho]}$:
$$H(u^*) \, W^{[\rho]} \subseteq W^{[\rho]}.$$

Therefore each Hessian eigenspace $V_k = \ker(H(u^*) - \lambda_k I)|_{\mathbf{1}^\perp}$ also decomposes:
$$V_k = \bigoplus_{[\rho] \in \widehat{G_u}} V_k^{[\rho]},\qquad V_k^{[\rho]} = V_k \cap W^{[\rho]} = P_{[\rho]} V_k,$$
where the **isotypic projector** is the standard formula
$$P_{[\rho]} = \frac{\dim\rho}{|G_u|} \sum_{\pi \in G_u} \overline{\chi_\rho(\pi)} \cdot \rho_{\mathrm{reg}}(\pi)$$
(Serre, *Linear Representations of Finite Groups*, 1977, §2.6).

The projector $P_{[\rho]}$ depends only on $G_u$ and the irrep class $[\rho]$ — not on a basis choice. Hence the multi-set $\{(\dim V_k^{[\rho]}, [\rho])\}_{[\rho] \in \widehat{G_u}}$ is canonical. ✓

### Step 4 — Single-irrep label for 1-dimensional eigenspaces.

If $\dim V_k = 1$, then in $V_k = \bigoplus_{[\rho]} V_k^{[\rho]}$ exactly one summand has dimension 1 and the rest are zero (dimensions sum to 1, all nonneg). Call that single $[\rho]$ the irrep label $[\rho_k]$ of mode $k$.

Uniqueness: the projector decomposition is into mutually orthogonal subspaces ($V_k^{[\rho]} \cap V_k^{[\rho']} = \{0\}$ for $[\rho] \neq [\rho']$), so the single non-trivial $[\rho]$ is unique. ✓

This $[\rho_k]$ is the irrep label appearing in `canonical.md` §11.1 Commitment 14 (O5). $\Box$

---

## §4. Remarks

**(R1.1) Real vs complex Maschke.** The argument in Step 3 uses Maschke over $\mathbb{R}$ for the real action on $\mathbf{1}^\perp \subset \mathbb{R}^X$. Over $\mathbb{C}$, the irrep classification differs slightly (real-irreducible 2-dim representations may split as conjugate-pair complex 1-dim irreps). The canonical convention follows the $D_4$ example in W4-04-24: real-irreducible $E$ kept as a single 2-dim irrep label (no complex splitting). This is the natural choice when Hessian is symmetric real.

**(R1.2) Eigenvalue multiplicity from symmetry.** Whenever $V_k$ contains a multi-dim irrep $V_\rho$ ($\dim\rho > 1$), the entire $V_\rho$-copy lies in $V_k$ — that is, $\dim V_k \geq \dim\rho$. Single-irrep $\dim V_k = 1$ requires $V_k$ to lie entirely in some 1-dim irrep (e.g., $A_1, A_2, B_1, B_2$ for $D_4$). 2-dim irreps ($E$ for $D_4$) automatically produce $\dim V_k \geq 2$. This is the source of the "Fiedler doublet" at uniform $u \equiv c$ on $D_4$ grid (Theorem 3): the $E$-irrep eigenspace has $\dim 2$ at $\lambda_2$.

**(R1.3) When $\dim V_k > 1$ but no single irrep accounts for it.** If $V_k$ contains multiple distinct irreps (accidental degeneracy not forced by symmetry — generically codim $\geq 1$), $[\rho_k]$ in canonical Commitment 14 (O5) is replaced by the multi-set $\{(\dim V_k^{[\rho]}, [\rho])\}$. Canonical convention (W4-04-24): record the full multi-set; in the σ-tuple, list each irrep separately ordered lexicographically.

**(R1.4) Degenerate-pair selection for Goldstone case.** When $V_k$ corresponds to a 2-dim $E$ irrep that is the translation Goldstone (Theorem 1), the basis $(\delta u_x, \delta u_y)$ is not canonically distinguished within the $E$-isotypic; any orthonormal basis $(a\delta u_x + b\delta u_y, -b\delta u_x + a\delta u_y)$ also spans it. This non-uniqueness is **intrinsic** to the 2-dim irrep (no basis is canonical without additional structure). The canonical convention: σ records *the irrep* $E$, not a particular basis.

---

## §5. Self-Classification

| Step | Tool | Cat |
|------|------|-----|
| 1 | Definition of permutation action | A |
| 2 | Polarization + orthogonality of permutation matrices | A |
| 3 | Maschke + Schur orthogonality (Serre 1977) | A |
| 4 | Direct dimension count | A |

**Cat A** — fully proved using standard finite-group representation theory, contingent on finite-graph hypothesis.

Confidence: **proved** (not sketched).

---

## §6. Failure Modes Considered

**FM1: Non-finite $G_u$.** Fails Step 3 (Maschke). Mitigation: explicit finite-graph hypothesis (§2.1).

**FM2: Energy not $\mathrm{Aut}(G)$-invariant.** Fails Step 2 polarization. Mitigation: SCC canonical operators are graph-symmetric (`working/SF/symmetry_moduli.md` §1.2); requirement is structural in the canonical theory.

**FM3: $u^*$ on the boundary of $\Sigma_m$ (some $u^*_i = 0$ or $1$).** Constraint manifold has corners; Hessian projection $\pi_{\mathbf{1}^\perp}$ may need refinement (additional KKT inequality multipliers). Lemma 1 stated for **interior** Morse-0 minimizer (consistent with `canonical.md` §3.4 KKT, which gives interior strict feasibility for generic parameters). Boundary case is the MO-1 sidestepped scope (single-formation σ on $\Sigma_m^{\circ}$).

**FM4: $H(u^*)$ defined inconsistently (unrestricted vs restricted).** The unrestricted Hessian $\nabla^2\mathcal{E}(u^*) \in \mathbb{R}^{X \times X}$ has an extra zero eigenvalue along $\mathbf{1}$ (volume mode). Restriction $H(u^*) = \pi_{\mathbf{1}^\perp}\,\nabla^2\mathcal{E}\,\pi_{\mathbf{1}^\perp}$ removes this. Since $\mathbf{1}$ is $G_u$-invariant, removing it preserves commutation. ✓

---

## §7. Canonical Wording (ready-to-paste §13 entry)

```markdown
**T-σ-Lemma-1. σ-Framework Irrep Decomposition Well-Defined.** *(New, 2026-04-27, W5 Day 1.)*
Let $G = (X, E)$ be a finite simple connected graph and $u^* \in \Sigma_m^{\circ}$ a Morse-index-0 local minimum of the SCC energy $\mathcal{E}$. Let $G_u := \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$ act on $T_{u^*}\Sigma_m = \mathbf{1}^\perp$ by coordinate permutation. Then:

**(i)** The constrained Hessian $H(u^*) = \pi_{\mathbf{1}^\perp}\,\nabla^2\mathcal{E}(u^*)\,\pi_{\mathbf{1}^\perp}$ commutes with the $G_u$-action.

**(ii)** Each Hessian eigenspace $V_k = \ker(H(u^*) - \lambda_k I)|_{\mathbf{1}^\perp}$ decomposes canonically into $G_u$-isotypic components
$$V_k = \bigoplus_{[\rho] \in \widehat{G_u}} V_k^{[\rho]},\qquad V_k^{[\rho]} = P_{[\rho]} V_k,\quad P_{[\rho]} = \frac{\dim\rho}{|G_u|}\sum_{\pi \in G_u}\overline{\chi_\rho(\pi)}\,\pi.$$

**(iii)** When $\dim V_k = 1$, the irrep label $[\rho_k] \in \widehat{G_u}$ in Commitment 14 (O5) is uniquely defined.

*Proof:* Step 1 (action well-defined): permutation action preserves $\mathbf{1}^\perp$ and energy $\mathcal{E}$ ($\mathrm{Aut}(G)$-invariance, `working/SF/symmetry_moduli.md` §1.2). Step 2 (Hessian commutation): polarization of $\mathcal{E}(u^* + \epsilon v) = \mathcal{E}(u^* + \epsilon\pi v)$ for $\pi \in G_u$ gives $\nabla^2\mathcal{E}(u^*) \pi = \pi \nabla^2\mathcal{E}(u^*)$. Step 3 (Maschke + Schur): finite-group action on finite-dim real space decomposes via isotypic projectors $P_{[\rho]}$ (Serre 1977, §2.6); commutation forces $H$ to preserve each isotypic component. Step 4 (1-dim case): exactly one irrep summand has dimension 1, the rest zero. $\Box$

*Status:* **Cat A** (representation theory + Schur orthogonality, standard).

*Hypotheses:* finite graph $G$ (essential for Maschke); Morse-0 interior minimizer (consistent with current σ-framework single-formation scope on $\Sigma_m^{\circ}$).

*Trivial-stabilizer remark:* For generic $u^*$ with $G_u = \{e\}$, the lemma is vacuously true; informative content concentrates at minimizers with non-trivial $G_u$ (uniform configurations, symmetric minimizers).

*References:* Serre, *Linear Representations of Finite Groups* (1977) Ch 2; W4-04-24 `02_development.md` §3; W5 Day 1 `01a_lemma1_irrep_decomposition.md`.
```

---

## §8. Open Questions Spawned

- **NQ-176 (W5 spawn):** When $\dim V_k > 1$ but $V_k$ contains multiple distinct irreps (accidental degeneracy), how should the σ-tuple list them? Lexicographic by character-table position? By dimension? The current canonical convention (multi-set) preserves information but doesn't impose ordering.
- **NQ-177 (W5 spawn, from CJ1 in `pre_brainstorm.md` §4):** Functoriality. Graph homomorphism $f : G \to G'$ should induce a map on minimizers $f_* : \mathrm{Form}(G) \to \mathrm{Form}(G')$. Does the σ-irrep label transform naturally? This would make σ a *graph functor*. (Forwards to NQ-191 in W6+ candidate list.)

---

**End of 01a_lemma1_irrep_decomposition.md.**
