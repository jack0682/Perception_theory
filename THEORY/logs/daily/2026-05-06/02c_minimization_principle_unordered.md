# 02c_minimization_principle_unordered.md — Minimization Principle on Unordered Configuration Space

**Session:** 2026-05-06 (W6 Day 3 G3.2, sub-file of `02_op_0009_pre_substantive_start.md`).
**Goal:** §3 of OP-0009-Pre — $S_K$-equivariance of $\mathcal{E}$; induced energy $\widetilde{\mathcal{E}}$ on $\widetilde{\widetilde\Sigma}^K_M$; existence and uniqueness sketch.
**Status (Cat C sketch, Silver):** §3.1-§3.2 substantive; §3.3-§3.5 sketch.
**Depends on:** `02a` (formalism) + `02b` (reduction map π).

---

## §3.1 S_K-Equivariance of the SCC Energy

The K-field SCC energy (canonical I9) is:
$$\mathcal{E}(\mathbf{u}) = \sum_{j=1}^K \left[ \lambda_{\mathrm{cl}} E_{\mathrm{cl}}(u^{(j)}) + \lambda_{\mathrm{sep}} E_{\mathrm{sep}}(u^{(j)}) + \lambda_{\mathrm{bd}} E_{\mathrm{bd}}(u^{(j)}) + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}(u^{(j)}, u^{(j-1)}) \right] + \lambda_{\mathrm{rep}} \sum_{1 \leq j < k \leq K} \langle u^{(j)}, u^{(k)} \rangle$$

**Claim.** $\mathcal{E}(\sigma \cdot \mathbf{u}) = \mathcal{E}(\mathbf{u})$ for all $\sigma \in S_K$.

**Proof.** Check each term under $\sigma \cdot \mathbf{u} = (u^{(\sigma^{-1}(1))}, \ldots, u^{(\sigma^{-1}(K))})$:

*(a) Single-slot terms* $\sum_j E_*(u^{(j)})$ where $E_* \in \{E_{\mathrm{cl}}, E_{\mathrm{sep}}, E_{\mathrm{bd}}\}$:
$$\sum_{j=1}^K E_*([{\sigma \cdot \mathbf{u}}]^{(j)}) = \sum_{j=1}^K E_*(u^{(\sigma^{-1}(j))}) = \sum_{j'=1}^K E_*(u^{(j')}) \quad \text{(re-index } j' = \sigma^{-1}(j) \text{).}$$
$S_K$-invariant. ✓

*(b) Transport term* $\sum_j E_{\mathrm{tr}}(u^{(j)}, u^{(j-1)})$: Remark that in the canonical formulation, $E_{\mathrm{tr}}$ involves the *cohesion fingerprint* $\varphi(u^{(j)}) = (u^{(j)}, \mathrm{Cl}(u^{(j)}), D(\cdot; 1 - u^{(j)}), \ldots)$, which is single-slot. The transport energy is of the form $E_{\mathrm{tr}} = d_{\mathrm{OT}}(\tilde{u}_t, M_{t-1 \to t}^* \tilde{u}_{t-1})$ between *time steps*, not between slots. In the static K-field setting, $\lambda_{\mathrm{tr}} = 0$ or $E_{\mathrm{tr}}$ is defined slot-independently (each slot's temporal transport is independent of slot labeling). Under this reading: $E_{\mathrm{tr}}$ is also a sum of single-slot terms $\sum_j E_{\mathrm{tr}}^{(j)}$, giving $S_K$-invariance by the same re-indexing argument. ✓

*[P-F flag: if $E_{\mathrm{tr}}$ couples slots in a time-step-dependent way, this argument requires revision. In the static multi-formation problem, $\lambda_{\mathrm{tr}} = 0$; the above applies.]*

*(c) Inter-field repulsion* $\lambda_{\mathrm{rep}} \sum_{j < k} \langle u^{(j)}, u^{(k)} \rangle$:
$$\lambda_{\mathrm{rep}} \sum_{j < k} \langle [\sigma \cdot \mathbf{u}]^{(j)}, [\sigma \cdot \mathbf{u}]^{(k)} \rangle = \lambda_{\mathrm{rep}} \sum_{j < k} \langle u^{(\sigma^{-1}(j))}, u^{(\sigma^{-1}(k))} \rangle.$$
The map $(j, k) \mapsto (\sigma^{-1}(j), \sigma^{-1}(k))$ is a bijection on $\{(j,k) : 1 \leq j < k \leq K\}$ → $\{(j', k') : j' \neq k'\}$ (unordered pairs, since $\sigma^{-1}$ is a bijection). Re-summing over unordered pairs $\{j', k'\}$:
$$= \lambda_{\mathrm{rep}} \sum_{\{j', k'\}} \langle u^{(j')}, u^{(k')} \rangle = \lambda_{\mathrm{rep}} \sum_{j' < k'} \langle u^{(j')}, u^{(k')} \rangle.$$
$S_K$-invariant. ✓

**Conclusion:** $\mathcal{E}$ is $S_K$-equivariant (invariant). By the functoriality of $\pi$ (see `02b` §2.5), there exists a unique:
$$\widetilde{\mathcal{E}} : \widetilde{\widetilde\Sigma}^K_M \to \mathbb{R}, \qquad \widetilde{\mathcal{E}}([\mathbf{u}]) = \mathcal{E}(\mathbf{u})$$
well-defined on the quotient space. $\square$

---

## §3.2 Induced Energy $\widetilde{\mathcal{E}}$ on $\widetilde{\widetilde\Sigma}^K_M$

By §3.1, the energy landscape of SCC on the ordered K-field space $\Sigma^K_M$ *descends* to a well-defined energy landscape on the unordered configuration space $\widetilde{\widetilde\Sigma}^K_M$:

$$\widetilde{\mathcal{E}} : \widetilde{\widetilde\Sigma}^K_M \to \mathbb{R}, \qquad \widetilde{\mathcal{E}}([\mathbf{u}]) = \mathcal{E}(\mathbf{u}) \text{ for any representative } \mathbf{u}.$$

**Energy landscape on quotient:** The gradient flow and energy minimization on $\Sigma^K_M$ factorize through $\pi$: any minimum $\hat{\mathbf{u}} \in \Sigma^K_M$ of $\mathcal{E}$ maps to a minimum $\pi(\hat{\mathbf{u}})$ of $\widetilde{\mathcal{E}}$ on $\widetilde{\widetilde\Sigma}^K_M$.

**Computational interpretation:** The SCC optimizer (`scc/optimizer.py`) finds ordered representative minimizers $\hat{\mathbf{u}}$. The "true" minimizer in the ontologically correct sense is $[\hat{\mathbf{u}}] = \pi(\hat{\mathbf{u}})$. The K! other ordered representations $\sigma \cdot \hat{\mathbf{u}}$ ($\sigma \in S_K$) are all equally valid ordered representatives of the same unordered minimizer class — they are modeling-layer artifacts of the representative choice, not distinct physical states.

---

## §3.3 Minimization on $\widetilde{\widetilde\Sigma}^K_M$: Existence

**Claim (sketch).** $\widetilde{\mathcal{E}}$ attains a minimum on $\widetilde{\widetilde\Sigma}^K_M$.

*Proof sketch:* $\widetilde{\widetilde\Sigma}^K_M$ is compact (continuous image of compact $\Sigma^K_M$). $\widetilde{\mathcal{E}}$ is continuous on $\widetilde{\widetilde\Sigma}^K_M$ (since $\mathcal{E}$ is continuous on $\Sigma^K_M$ and the quotient map $\pi$ is a quotient with compact fiber, so $\widetilde{\mathcal{E}}$ inherits continuity). By the extreme value theorem, $\widetilde{\mathcal{E}}$ attains its minimum on the compact space. $\square$ (Cat C; the continuity of $\widetilde{\mathcal{E}}$ on the quotient uses that $\mathcal{E}$ is continuous on $\Sigma^K_M$ and $S_K$-invariant; standard result for quotient by compact group. W7 D3: verify full argument.)

**Relationship to T-1 (Cat A, canonical §13):** T-1 establishes existence of a minimizer in $\Sigma_M$ for the single-formation problem. The K-field existence theorem T-Persist-K (Cat A conditional) covers the K-formation existence in $\Sigma^K_M$. The unordered version here is a *corollary* at the class level — existence in $\Sigma^K_M$ implies existence in $\widetilde{\widetilde\Sigma}^K_M$ via $\pi$.

---

## §3.4 Open Stratum Minimizers: Uniqueness Sketch

**On the open stratum:** If $\hat{\mathbf{u}} \in \Sigma^K_{M,\mathrm{free}}$ is a local minimizer of $\mathcal{E}$ in $\Sigma^K_M$, then $[\hat{\mathbf{u}}] \in \pi(\Sigma^K_{M,\mathrm{free}})$ is a local minimizer of $\widetilde{\mathcal{E}}$.

**Claim (sketch).** Under non-degeneracy assumptions (Hessian $H_{\hat{\mathbf{u}}}[\mathcal{E}]$ positive definite on $T_{\hat{\mathbf{u}}} \Sigma^K_M$), the class $[\hat{\mathbf{u}}]$ is a *non-degenerate* local minimizer of $\widetilde{\mathcal{E}}$ in the open stratum quotient.

*Proof sketch:* The Hessian of $\widetilde{\mathcal{E}}$ at $[\hat{\mathbf{u}}]$ (in appropriate local coordinates of the open stratum quotient) equals the Hessian of $\mathcal{E}$ at $\hat{\mathbf{u}}$ restricted to the quotient tangent space (the $S_K$-invariant part of $T_{\hat{\mathbf{u}}} \Sigma^K_M$). Non-degeneracy of $H[\mathcal{E}]$ on $\Sigma^K_M$ implies non-degeneracy of the induced Hessian on the quotient.

**Uniqueness issue at symmetric strata:** If a global minimizer $\hat{\mathbf{u}}$ lands on a symmetric stratum ($u^{(j)} = u^{(k)}$ for some $j, k$), then the fiber $\pi^{-1}([\hat{\mathbf{u}}])$ is a single point (orbit size 1 at the fixed point), and uniqueness at the class level is automatic. However, the meaning changes: a symmetric-stratum minimizer represents a *degenerate* multi-formation state where two formations are identical — this is physically the "barely distinguishable" regime. The T-Persist-K separation assumptions (L1-J regime) precisely avoid this degenerate case.

---

## §3.5 Connection to T-Persist-K Separation Assumptions

**T-Persist-K-Sep (canonical ~line 1300, Cat A conditional):** Formation separation requires $\langle u^{(j)}, u^{(k)} \rangle \leq \delta_{\mathrm{sep}}$ for $j \neq k$ — i.e., well-separated formations.

**At class level:** Well-separated formations correspond exactly to minimizers in the *open stratum* $\Sigma^K_{M,\mathrm{free}}$ (since identical support $u^{(j)} = u^{(k)}$ would give $\langle u^{(j)}, u^{(k)} \rangle = m$, far exceeding $\delta_{\mathrm{sep}}$). The L1-J regime's separation assumptions implicitly place minimizers in the open stratum.

**Consequence:** Under T-Persist-K-Sep assumptions, the minimizer class $[\hat{\mathbf{u}}]$ lies in the open stratum quotient — the "safe" part of $\widetilde{\widetilde\Sigma}^K_M$ where local sections are continuous and the quotient is locally a manifold.

---

**End of `02c_minimization_principle_unordered.md`. §3 complete: $\mathcal{E}$ is $S_K$-equivariant (proved); $\widetilde{\mathcal{E}}$ well-defined on quotient; existence by compactness (sketch); open-stratum uniqueness under non-degeneracy (sketch); connection to T-Persist-K-Sep. Day 3 Silver criterion §3: MET (Cat C sketch as planned).**
