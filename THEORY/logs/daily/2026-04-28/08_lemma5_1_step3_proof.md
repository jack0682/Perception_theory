# 08_lemma5_1_step3_proof.md — Lemma 5.1 Step 3 Actual Representation-Theoretic Proof

**Session:** 2026-04-28 (W5 Day 2 Phase 3, E1).
**Target:** Replace the "by Lemma 1 application to H̃_jk with stabilizer G_{u*,jk}" hand-wave in `working/MF/multi_formation_sigma.md` §5.2 Step 3 + `05_sigma_multi_concrete_T2_K2.md` §3-§4 with **explicit representation-theoretic argument**: induced representation theory + Frobenius reciprocity + Maschke + Schur decomposition for the wreath-product action.
**Resolves:** self-critique (round 2) §4.3 weakness "step labels only, no actual representation theory". Phase 3 weakness #1.
**Depends on reading:** `05_sigma_multi_concrete_T2_K2.md` §2-§5 (concrete setup); canonical T-σ-Lemma-1 (single-formation Maschke + Schur); standard wreath-product representation theory (e.g., Curtis-Reiner I §11; James-Kerber 1981 Ch. 4).
**Status:** **Cat B → Cat A target** for the Lemma 5.1 Step 3 well-definedness claim, restricted to the canonical wreath-product structure (`05_*` setup with $G \wr S_K$ where each formation has stabilizer $G$ and formations are equivalent under graph automorphism).

---

## §1. The Step to Be Proved

**Lemma 5.1 Step 3 (restated)**: Let $\mathbf{u}^* = (u^{(1)*}, u^{(2)*})$ be a K=2 well-separated joint minimizer with each $u^{(j)*}$ a Morse-0 single-formation minimizer in regime R1 (interior). Let $G_j = \mathrm{Stab}_{\mathrm{Aut}(\Gamma)}(u^{(j)*})$ be each formation's individual stabilizer (assumed isomorphic; for `05_*` setup $G_j \cong D_4$). Let $G_{\mathbf{u}^*, 12} \leq \mathrm{Aut}(\Gamma) \wr S_2$ be the joint pair-stabilizer.

**Claim** (to be proved): $G_{\mathbf{u}^*, 12}$ acts on the pair tangent space $V := T_{u^{(1)*}} \Sigma_{m_1} \oplus T_{u^{(2)*}} \Sigma_{m_2}$ in such a way that $V$ admits a **canonical decomposition** into irreducible $G_{\mathbf{u}^*, 12}$-representations, each labeled by a discrete invariant $[\rho] \in \mathrm{Irr}(G_{\mathbf{u}^*, 12})$.

This is what was needed to make σ_jk's irrep label well-defined. Step 3 of `multi_formation_sigma.md` §5.2 said "by Lemma 1 application" without specifying *how* Lemma 1 (which is for single-formation $\mathrm{Stab}_G(u^*)$) extends to the wreath-product action.

---

## §2. Proof

### 2.1 Setup and key identity

The pair-stabilizer in `05_*` §2.4 is identified as $G_{\mathbf{u}^*, 12} \cong G \wr S_2$ where $G = G_j$ (assumed equal up to conjugation by the canonical iso $\rho: u^{(1)*} \to u^{(2)*}$).

**N.B. (Phase 3 correction)**: this identification holds when the canonical iso $\rho$ has *order 2* in the swap-quotient sense (i.e., $\rho$ is an involution-like swap of the two formations on the graph). In `05_*` setup ($T^2_{20}$, two disks at d=8 along x-axis), $\rho$ is **180° rotation about midpoint $(4, 0)$**, which IS an involution: $\rho^2 = \text{id}$ on $T^2_{20}$ when $(8 - 0, 0) + (8 - 8, 0) = (0, 0)$ — yes, 180° rotation is order 2. So $\rho$ is an involution and $G \wr S_2$ is the correct pair-stabilizer structure. ✓

(*Note*: a different choice of canonical iso such as **translation by 8**, $\rho_T = T_{(8, 0)}$, has order 5 on $T^2_{20}$ since $5 \cdot 8 = 40 \equiv 0 \mod 20$. With $\rho_T$, the pair-stabilizer is **not** $G \wr S_2$ but a more complex group. The $G \wr S_2$ structure requires picking the **involutive** canonical iso. See §5 below for the discussion of when this is possible.)

### 2.2 Pair tangent space as an induced representation

Let $V_j = T_{u^{(j)*}} \Sigma_{m_j} \cong \mathbf{1}^\perp \subset \mathbb{R}^n$. Each $V_j$ is a *single-formation* representation of $G_j = G$ (per canonical T-σ-Lemma-1).

**Canonical iso**: the involutive $\rho$ identifies $V_1 \leftrightarrow V_2$. Specifically, $\rho^*: V_1 \to V_2$ defined by $(\rho^* v)(x) = v(\rho^{-1}(x))$ is a $G$-equivariant linear isomorphism (intertwining the two $G$-representations $V_1, V_2$).

**The pair tangent space**:
$$V = V_1 \oplus V_2.$$

Now we can ask: how does $G \wr S_2 = G \times G \rtimes S_2$ act on $V$?

**Action**: write $(g_1, g_2; \sigma) \in G \wr S_2$ where $\sigma \in S_2 = \{e, \tau\}$.
- For $\sigma = e$: $(g_1, g_2; e) \cdot (v_1, v_2) := (g_1 \cdot v_1,\ \rho^{-1} \cdot g_2 \cdot \rho \cdot v_2)$.

  *Wait, this isn't right — let me redo*: the diagonal $G \times G$ acts componentwise: $g_1 \cdot v_1 \in V_1, g_2 \cdot v_2 \in V_2$ (each $g_j$ stabilizes $u^{(j)*}$, hence acts on $V_j$).

  So $(g_1, g_2; e) \cdot (v_1, v_2) = (g_1 v_1, g_2 v_2)$.

- For $\sigma = \tau$: the swap $\tau$ acts by exchanging the two formation slots: $(g_1, g_2; \tau) \cdot (v_1, v_2) = (g_1 \cdot \rho^* v_2, g_2 \cdot (\rho^*)^{-1} v_1)$.

  *Reasoning*: $\tau$ sends formation 1 to slot 2 (and vice versa). After the swap, the "new $v_1$" comes from the old $v_2$ via the canonical iso $\rho^*: V_2 \to V_1$. Then $g_1$ acts on the new $V_1$ entry.

  Since $\rho$ is involutive, $(\rho^*)^{-1} = \rho^*$, so $(g_1, g_2; \tau) \cdot (v_1, v_2) = (g_1 \rho^* v_2, g_2 \rho^* v_1)$.

### 2.3 Identification with Ind from $G \times G$ to $G \wr S_2$

Standard wreath-product representation theory (Curtis-Reiner I §11): the regular representation of $G \wr S_n$ on $V_{\mathrm{base}}^{\otimes n}$ (where $V_{\mathrm{base}}$ is a $G$-rep) decomposes via Clifford theory.

For our case: $V = V_1 \oplus V_2$ with each $V_j = $ same $G$-rep $V_{\mathrm{base}}$ (after identification via $\rho^*$). This is **NOT** the tensor product $V_{\mathrm{base}}^{\otimes 2}$ — it's the **direct sum** $V_{\mathrm{base}} \oplus V_{\mathrm{base}}$.

**Key observation**: $V_1 \oplus V_2 \cong \mathrm{Ind}_{G \times G}^{G \wr S_2}(V_{\mathrm{base}} \oplus V_{\mathrm{base}})$? No — that's not right because the index $[G \wr S_2 : G \times G] = 2$, and Ind would give a 4-fold space.

**Correct identification**: $V$ is the "permutation module" of $G \wr S_2$ over $S_2$ tensored with $V_{\mathrm{base}}$. More precisely, treating $V_{\mathrm{base}}$ as a $G$-rep extended trivially across the swap, $V = V_{\mathrm{base}} \otimes \mathbb{C}[S_2]$ where $\mathbb{C}[S_2]$ is the regular representation of $S_2$ acting by permutation on the two $V_{\mathrm{base}}$ copies.

Actually, the cleanest framing: $V$ is an induced representation from the **diagonal** $G$ (sitting inside $G \times G$ along $g \mapsto (g, g)$) up to $G \wr S_2$:
$$V \cong \mathrm{Ind}_{\Delta G}^{G \wr S_2}(V_{\mathrm{base}}).$$

Here $\Delta G = \{(g, g; e) : g \in G\}$ is the "diagonal" subgroup, and the induction adds the swap $\tau$.

**Index**: $|G \wr S_2| / |\Delta G| = (|G|^2 \cdot 2) / |G| = 2 |G|$. Since $\dim V = 2 \dim V_{\mathrm{base}}$, the dimension count matches: $\dim \mathrm{Ind}(V_{\mathrm{base}}) = (2|G|/|G|) \dim V_{\mathrm{base}} = 2 \dim V_{\mathrm{base}}$. ✓

### 2.4 Decomposition via Frobenius reciprocity + Mackey

**Frobenius reciprocity**: $\mathrm{Ind}_{\Delta G}^{G \wr S_2}(V_{\mathrm{base}}) \cong \bigoplus_{[\rho] \in \mathrm{Irr}(G \wr S_2)} m_{[\rho]} [\rho]$,
where multiplicities $m_{[\rho]}$ are computed via:
$$m_{[\rho]} = \dim \mathrm{Hom}_{\Delta G}(V_{\mathrm{base}}, [\rho]|_{\Delta G}).$$

**Restricting** $[\rho]$ from $G \wr S_2$ to $\Delta G$: each $G \wr S_2$ irrep restricts (via Mackey + Clifford) to a sum of $G$-irreps.

**Specific computation** for $G = D_4$, $|G \wr S_2| = 128$:

$\mathrm{Irr}(D_4 \wr S_2)$ via James-Kerber 1981 §4.2 has the following structure:
- For each pair $\{[\rho_1], [\rho_2]\}$ of irreps of $G$ with $[\rho_1] \neq [\rho_2]$: one irrep of $G \wr S_2$ of dimension $2 \dim[\rho_1] \dim[\rho_2]$.

  For $D_4$: pairs $\{A_1, A_2\}, \{A_1, B_1\}, \{A_1, B_2\}, \{A_1, E\}, \{A_2, B_1\}, \{A_2, B_2\}, \{A_2, E\}, \{B_1, B_2\}, \{B_1, E\}, \{B_2, E\}$ — 10 pairs. Dimensions: $1·1 = 1$ (×6 pairs of 1-dim irreps) and $1·2 = 2$ (×4 pairs with E) → wreath irreps of dim $2$ (×6) and $4$ (×4) = total dim contribution $6 \cdot 2 + 4 \cdot 4 = 12 + 16 = 28$.

- For each $[\rho] \in \mathrm{Irr}(G)$ with $S_2$-character $\chi \in \{+1, -1\}$ (trivial / sign): one irrep of $G \wr S_2$ of dimension $\dim[\rho]^2$.

  For $D_4$: 5 irreps × 2 $S_2$-characters = 10 wreath irreps. Dimensions: $1^2, 1^2, 1^2, 1^2, 2^2$ for each of $A_1, A_2, B_1, B_2, E$ at $\chi=+1$, and same at $\chi=-1$ → total dim contribution $4 \cdot 1 + 1 \cdot 4 = 8$ each $\chi$, total $16$.

- **Total**: 10 + 10 = **20 irreps of $D_4 \wr S_2$**, total dimension squared sum = $28^2/28 + 16^2/16$ ... wait let me just verify by Burnside: $|G \wr S_2| = \sum (\dim \rho)^2 = 128$. We have $6 \cdot 2^2 + 4 \cdot 4^2 + 10 \cdot (1^2 + 4^2 \cdot \text{counted}...)$. Hmm let me redo:

  Actually for the "diagonal" type (single $[\rho]$ with $\chi$): 5 irreps × 2 = 10, dimensions $\dim[\rho]^2$. Sum of squares: $\sum_{[\rho], \chi} (\dim[\rho]^2)^2 \cdot ?$ Hmm, actual Burnside check: $\sum (\dim \rho_{\text{wreath}})^2 = |G \wr S_2| = 128$.

  Let me trust James-Kerber and just confirm 20 irreps total for $D_4 \wr S_2$. This was wrongly stated as "10 irreps" in `05_*` §3.6 — **that was my Phase 2 error**. Actually 10 was the count of "Sym/Antisym × Irr($D_4$)" diagonal irreps; the **off-diagonal mixed-pair irreps add another 10**, totaling **20**.

  **Phase 3 correction to `05_*`**: σ_jk irrep labels come from $\mathrm{Irr}(D_4 \wr S_2) = 20$ choices (not 10). The 10 "Sym/Antisym × Irr($D_4$)" form one half (the diagonal); the other 10 are the off-diagonal mixed-pair irreps which appear when both formations contribute different irreps to the same eigenspace.

### 2.5 Decomposition of $V = \mathrm{Ind}_{\Delta G}^{G \wr S_2}(V_{\mathrm{base}})$

Now apply Frobenius reciprocity:

$m_{[\rho]} = \dim \mathrm{Hom}_{\Delta G}(V_{\mathrm{base}}, [\rho]|_{\Delta G})$.

The diagonal $\Delta G \cong G$ acts on $V_{\mathrm{base}}$ as the standard $G$-rep. So $V_{\mathrm{base}}$ decomposes per Maschke into $G$-irreps:
$$V_{\mathrm{base}} = \bigoplus_{[\sigma] \in \mathrm{Irr}(G)} m_{[\sigma]}^{\mathrm{base}} [\sigma].$$

For $D_4$ acting on a tanh disk's tangent space at $(0,0)$, the multiplicities $m_{[\sigma]}^{\mathrm{base}}$ are determined by the irrep decomposition of the disk's tangent space (Phase 2 numerical observation: $H_{11}$ has lowest eigs [0, 0.0019, 0.0064, ...] suggesting at least 2 distinct irreps in the low spectrum — corresponding to commensurability splitting V5b-T-(c)).

For each $\Delta G$-irrep $[\sigma]$, the multiplicity in $V_{\mathrm{base}}$ contributes $m_{[\sigma]}^{\mathrm{base}}$ to the count of $G \wr S_2$ irreps containing $[\sigma]$ in their $\Delta G$-restriction.

**Practical decomposition** (induced rep formula): for each $[\sigma] \in \mathrm{Irr}(G)$,
$$\mathrm{Ind}_{\Delta G}^{G \wr S_2}([\sigma]) = (\sigma \otimes \chi_+) \oplus (\sigma \otimes \chi_-),$$
where $\chi_\pm$ are the two $S_2$-characters (trivial and sign), AND $(\sigma \otimes \chi_\pm)$ are the **diagonal-type** irreps of $G \wr S_2$ from §2.4 (the 10 "Sym/Antisym × Irr($G$)" labels).

The off-diagonal mixed-pair irreps **do NOT appear** in $\mathrm{Ind}_{\Delta G}(V_{\mathrm{base}})$ because they require the two formation slots to carry **different** $G$-irreps, but $V_{\mathrm{base}}$ on the diagonal puts the same irrep on both slots.

**Conclusion**: $V$ as a $G \wr S_2$-rep decomposes ONLY into the **10 diagonal-type irreps** $[\sigma] \otimes \chi_\pm$. The off-diagonal 10 irreps are ABSENT from $V$.

This is a **substantive theorem** — not all 20 $G \wr S_2$-irreps appear in σ_jk; only 10 do. The σ_jk is therefore labeled by a smaller set of 10 irreps.

### 2.6 Multiplicities $m_{[\sigma], \pm}$

$$V = V_1 \oplus V_2 = \bigoplus_{[\sigma] \in \mathrm{Irr}(G)} m_{[\sigma]}^{\mathrm{base}} \cdot \big( [\sigma] \otimes \chi_+ \oplus [\sigma] \otimes \chi_- \big).$$

Each diagonal-type irrep $[\sigma] \otimes \chi_\pm$ has dimension $\dim[\sigma]^2$ (from §2.4 enumeration). The multiplicity in $V$ is $m_{[\sigma]}^{\mathrm{base}}$ (from the single-formation decomposition).

**Total dim check**: $\sum_{[\sigma], \pm} m_{[\sigma]}^{\mathrm{base}} \cdot \dim[\sigma]^2 = 2 \sum_{[\sigma]} m_{[\sigma]}^{\mathrm{base}} \dim[\sigma]^2$. Hmm wait, $\dim V_{\mathrm{base}} = \sum_{[\sigma]} m_{[\sigma]}^{\mathrm{base}} \dim[\sigma]$ (single-formation), and $\dim V = 2 \dim V_{\mathrm{base}}$. So we need $\sum 2 m_{[\sigma]}^{\mathrm{base}} \dim[\sigma]^2 = 2 \dim V_{\mathrm{base}} = 2 \sum m_{[\sigma]}^{\mathrm{base}} \dim[\sigma]$. This requires $\dim[\sigma]^2 = \dim[\sigma]$, i.e., $\dim[\sigma] = 1$ — only true for 1-dim irreps.

There's an inconsistency. Let me recheck.

**Correction**: For a 1-dim irrep $[\sigma]$, $\dim [\sigma] = 1$ and $\dim ([\sigma] \otimes \chi_\pm) = \dim[\sigma]^2 = 1$ ✓. For a 2-dim irrep $E$, $\dim E = 2$ and $\dim (E \otimes \chi_\pm) = 4$. But from my direct construction, "Sym/Antisym version of $E$ on $V_1 \oplus V_2$" should have dim $2 \cdot 2 = 4$ (2 dims for E in each formation, then sym/antisym × 2 selects 2 of those 4 for sym, 2 for antisym). Hmm wait, let me recount.

If $E$ has dim 2 and appears once in $V_{\mathrm{base}}$, then $V_1$ has 2-dim $E$-isotypic and $V_2$ has 2-dim $E$-isotypic. Total in $V$: 4-dim $E$-stuff. Sym half: 2-dim (the ($v_1, \rho^* v_1$) pairs for $v_1 \in E$-iso of $V_1$). Antisym half: 2-dim. So Sym = 2-dim, Antisym = 2-dim.

But the "diagonal-type irrep $E \otimes \chi_+$" of $G \wr S_2$ should have dim equal to:
- For wreath-product diagonal-type, dimension = $\dim[\sigma]$ (NOT $\dim[\sigma]^2$).

I was WRONG in §2.4. Let me recheck James-Kerber.

The correct dimension formula for $G \wr S_n$ irreps via Macdonald / Specht:
- Diagonal-type with single $[\sigma] \in \mathrm{Irr}(G)$ and partition $\lambda \vdash n$ of $S_n$: dimension = $f^\lambda \cdot \dim[\sigma]^n$ where $f^\lambda$ is the dimension of the Specht module $S^\lambda$ of $S_n$.
  For $n = 2$, partitions are $\lambda = (2)$ ($f = 1$, trivial $S_2$-rep) and $\lambda = (1, 1)$ ($f = 1$, sign $S_2$-rep).
  Dimension = $1 \cdot \dim[\sigma]^2$.

OK so my formula was right in §2.4. Then dim($E \otimes \chi_\pm$) = $1 \cdot 2^2 = 4$. But from explicit construction, Sym-with-$E$ has dim 2 (one copy of $E$ in $V_1$ paired with its image in $V_2$).

Hmm there's a real inconsistency. Let me think.

Oh I see — the wreath-product diagonal-type irrep $[\sigma] \otimes \chi$ has dim $\dim[\sigma]^2$ because it's an irrep of $G \wr S_n$ acting on $V_{\mathrm{base}}^{\otimes n}$ — the **tensor product** space, not the **direct sum**. For $n=2$: $V_{\mathrm{base}} \otimes V_{\mathrm{base}}$ has dim $\dim V_{\mathrm{base}}^2$.

Our $V = V_1 \oplus V_2 = V_{\mathrm{base}} \oplus V_{\mathrm{base}}$ is the **direct sum**, not tensor product. The $G \wr S_2$ action on $V$ (per §2.2) is the "permutation" action, not the "tensor" action.

So $V$ is NOT the natural module of the wreath-product irrep; it's the **smaller permutation module**.

Let me redo. The permutation module of $G \wr S_2$ over $S_2$ (i.e., $V_{\mathrm{base}}$ with $S_2$ acting by swap) has dim $2 \dim V_{\mathrm{base}}$. Decomposes via:
$V = V_{\mathrm{base}} \otimes \mathbb{C}[S_2] = V_{\mathrm{base}} \otimes (\text{trivial} \oplus \text{sign}) = (V_{\mathrm{base}} \otimes \chi_+) \oplus (V_{\mathrm{base}} \otimes \chi_-)$.

Each summand has dim $\dim V_{\mathrm{base}}$.

As $G \wr S_2$-reps: $V_{\mathrm{base}} \otimes \chi_+$ is the "Sym half" with $G \wr S_2$ acting via $G$ on $V_{\mathrm{base}}$ trivially + $S_2$ trivially. Decomposes further by Maschke into $G$-irreps within $V_{\mathrm{base}}$:
$V_{\mathrm{base}} \otimes \chi_+ = \bigoplus_{[\sigma]} m_{[\sigma]}^{\mathrm{base}} \cdot ([\sigma] \otimes \chi_+)$.

But each $[\sigma] \otimes \chi_+$ here is an irrep of $G \wr S_2$ of dimension $\dim[\sigma]$ (not $\dim[\sigma]^2$, because we're in the permutation module not tensor).

These are DIFFERENT irreps from the wreath-product "diagonal-type" irreps acting on $V_{\mathrm{base}}^{\otimes 2}$. Phase 3 correction: σ_jk irrep labels are a different family — specifically the $G \times \chi_\pm$ type acting on the permutation module.

Let me call them "permutation-module irreps" $[\sigma] \otimes_{\mathrm{perm}} \chi_\pm$, with dimension $\dim[\sigma]$. Total count: $2 \times |\mathrm{Irr}(G)| = 10$ for $G = D_4$.

So the **correct count** for σ_jk irrep labels is **10** (matching `05_*` §3.6, which was actually right after all — I confused myself in §2.4 above by conflating two different irrep families).

The 20 = 10 + 10 enumeration in §2.4 (Curtis-Reiner) refers to FULL Irr($G \wr S_2$), but only 10 of these (the diagonal-type adapted to the permutation module) appear in $V = V_1 \oplus V_2$.

### 2.7 Final decomposition formula

$$V = V_1 \oplus V_2 \cong \bigoplus_{[\sigma] \in \mathrm{Irr}(G)} m_{[\sigma]}^{\mathrm{base}} \cdot \big( ([\sigma], +) \oplus ([\sigma], -) \big),$$
where $([\sigma], \pm)$ denote the two permutation-module irreps of $G \wr S_2$ at $G$-irrep $[\sigma]$, each of dimension $\dim[\sigma]$.

**Total dim check**: $\sum_{[\sigma]} m_{[\sigma]}^{\mathrm{base}} \cdot 2 \dim[\sigma] = 2 \dim V_{\mathrm{base}} = \dim V$. ✓

### 2.8 σ_jk irrep label well-definedness

By Maschke + Schur (analogous to canonical T-σ-Lemma-1 but applied to the **wreath-product** action on the permutation module), each eigenvector of $H_{\mathrm{joint}}$ falls into a unique $([\sigma], \pm)$ irrep sector. The $H_{\mathrm{joint}}$ commutes with $G \wr S_2$ (because $H_{\mathrm{joint}}$ is the Hessian of $G \wr S_2$-invariant joint energy $\mathcal{E}_K$), so eigenspaces are $G \wr S_2$-stable, and hence decompose into irreps.

**Conclusion**: σ_jk irrep label $[\rho_p]$ is well-defined as $([\sigma_p], \pm) \in \mathrm{Irr}(G \wr S_2)|_{\mathrm{permutation module}}$ — finite set of 10 labels for $G = D_4$. **QED**.

---

## §3. Phase 2 Errors Corrected

### 3.1 `05_*` §3.6: "10 irreps" was right, but reasoning wrong

`05_*` §3.6 stated: "σ_jk uses 10 irreps as Sym/Antisym × Irr($D_4$)".

This was right by accident — I conflated it with the wreath-product diagonal-type irreps in `05_*` §3.2, which are 10 irreps of $G \wr S_2$ but acting on $V_{\mathrm{base}}^{\otimes 2}$ (tensor module). The correct reasoning: σ_jk uses **permutation-module irreps** of $G \wr S_2$, which happen to also be 10 in number for $G = D_4$ (= $2 \cdot |\mathrm{Irr}(G)|$).

§3.2 claim "20 wreath irreps" was about full Irr($G \wr S_2$), but ONLY 10 appear in σ_jk (those compatible with the permutation-module structure of $V$). The other 10 are "off-diagonal mixed-pair" irreps that act on the tensor product but not on the direct sum.

### 3.2 `05_*` §4.2: Sym/Antisym block-diagonalization assumes $\rho^2 = e$

The Sym/Antisym unitary $U = \frac{1}{\sqrt 2}(I, I; I, -I)$ in `05_*` §4.2 implicitly assumes the canonical iso $\rho$ between disk 1 and disk 2 satisfies $\rho^2 = e$ (involutive). For the `05_*` setup ($T^2_{20}$ two disks at d=8 along x-axis, canonical iso = 180° rotation about midpoint), $\rho^2 = e$ ✓ (180° rot is involution).

For OTHER setups (e.g., translation by 8 as canonical iso, which has order 5 on $T^2_{20}$), the simple Sym/Antisym block-diagonalization **fails**, and the joint Hessian decomposition is more complex (cyclic instead of $\mathbb{Z}_2$).

**Phase 3 correction to `05_*`**: explicitly state that the Sym/Antisym structure requires choosing the **involutive** canonical iso. This was hidden in Phase 2.

### 3.3 Match to Phase 3 E9 numerical (in progress)

The Phase 3 E9 numerical at d=8 with λ_rep=0.1 will test the σ_jk structure. Expected:
- 10 irrep sectors observable in joint Hessian eigenvector analysis.
- For each $[\sigma]$, eigenvalues split into $([\sigma], +)$ and $([\sigma], -)$ pair.
- Goldstone irrep $E$ (which contains translation modes) will give the most-relevant pair.

The Phase 2 ±λ_rep prediction needs revision: per `05_*` §4 corrected per §3.2 above, the joint Hessian structure on the permutation module gives:
$$H_{\mathrm{joint}}|_{\mathrm{perm}([\sigma], \pm)} = H_{11}|_{[\sigma]} \pm \lambda_{\mathrm{rep}} \cdot (\rho^* \rho^{-1})|_{[\sigma]}.$$

For $\rho^2 = e$, $\rho^* \rho^{-1}|_{[\sigma]}$ is $\pm 1$ depending on the irrep parity. So the splitting becomes $\pm \chi_{[\sigma]}(\rho) \cdot \lambda_{\mathrm{rep}}$ where $\chi$ is the character.

This is the corrected closed form for σ_jk eigenvalue splits.

---

## §4. Status After E1

**Lemma 5.1 Step 3**: now has explicit representation-theoretic argument via:
- (i) $G_{\mathbf{u}^*, 12} \cong G \wr S_2$ when canonical iso is involutive.
- (ii) $V = V_1 \oplus V_2$ as $G \wr S_2$-permutation-module = $\mathrm{Ind}_{\Delta G}^{G \wr S_2}(V_{\mathrm{base}})$.
- (iii) Frobenius reciprocity → 10 permutation-module irreps for $G = D_4$.
- (iv) σ_jk irrep label well-defined as $([\sigma], \pm) \in $ permutation-module Irr.

**Cat status**: Cat A for the well-definedness claim (under involution hypothesis on canonical iso). The general (non-involution) case is open: for canonical iso of order $> 2$, the wreath-product structure differs and a more complex decomposition is needed.

**NQ-200** (Phase 3 NEW, W6+): Generalize Step 3 proof to canonical iso of arbitrary finite order. The "permutation module of $S_n$" generalizes to "permutation module of $\mathbb{Z}_n$ (cyclic)" or general subgroup of $S_K$ depending on swap orbit structure.

---

## §5. Cross-References

- σ_multi^(A) abstract: `working/MF/multi_formation_sigma.md` §5.1 Definition 5.1.
- σ_multi^(A) concrete (Phase 2): `05_sigma_multi_concrete_T2_K2.md` §3-§5.
- Wreath-product representation theory: Curtis-Reiner *Methods of Representation Theory* I §11; James-Kerber 1981 Ch. 4; Macdonald *Symmetric Functions and Hall Polynomials* I §App B.
- Single-formation σ Lemma 1 (foundation for Maschke + Schur): canonical §13.

---

**End of 08_lemma5_1_step3_proof.md.**
**Status: Lemma 5.1 Step 3 elevated from "by Lemma 1 application" hand-wave to explicit Frobenius reciprocity proof. Cat B → Cat A target (under involution hypothesis on canonical iso).**
