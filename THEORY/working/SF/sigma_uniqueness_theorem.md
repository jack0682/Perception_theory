# sigma_uniqueness_theorem.md — σ-Uniqueness Theorem (NQ-188 Working File)

**Status:** Working — Cat A target candidate (single-formation σ-class enumeration on $D_4$ free-BC grid).
**Spawned:** Round-2 spawn 2026-04-27 (NQ-188).
**Author origin:** W5 σ-framework supporting structures merge (CV-1.5, 2026-04-27) flagged σ-uniqueness as the natural follow-up to T-σ-Lemma-1's $\mathrm{Aut}(G)$-orbit invariance.
**Canonical refs:** §11.1 Commitment 14 (orbital character constitutive); §13 T-σ-Lemma-1/2/3; §13 T-σ-Theorem-3/4; §14 CN10 (contrastive vs reductive); §14 CN17 (σ-Labeled Formation Quantization).
**Working refs:** `working/SF/symmetry_moduli.md` §2 ($\mathcal{M}_1$ moduli space); `working/SF/mode_count.md` (Prop 1.3a Hessian closed form); `working/MF/single_high_F_equivalence.md` (OAT-7 σ-class vs PH coarseness).
**External refs:** Sagan 2001, *The Symmetric Group*; Specht 1935, *Math. Z.* 39:696–711; James–Kerber 1981, *The Representation Theory of the Symmetric Group*.

**Hard constraints (CN10 + canonical promotion):**
- Direct canonical edits: 0. This file is W7+ promotion candidate, not a §13 entry yet.
- σ-tuple is SCC-intrinsic Hessian-spectral mathematics (CN10 contrastive), not borrowed atomic shell terminology.
- Open problems (F-1, M-1, MO-1) are NOT silently resolved.

---

## §1. Mission

**NQ-188 statement.** *Within a fixed (G, parameters) regime — graph $G$ with automorphism group $\mathrm{Aut}(G)$, parameter triple $(\alpha, \beta, c)$ in spinodal interior — how many distinct σ-classes does the local-minimizer set $\mathcal{L}(G, \alpha, \beta, c) \subset \Sigma_m^{\circ}$ partition into?*

**Cat A target.** Enumerate $|\sigma\text{-classes}|$ on small $D_4$ free-BC grids ($L \in \{4, 6, 8\}$) by direct computation of the σ-tuple for each minimizer in $\mathcal{L}$ and grouping by σ-equivalence (§2 below). The empirical count is the first quantitative statement.

**Why it matters.** σ-tuple is the §11.1 Commitment 14 invariant designating "formation identity". If $|\sigma\text{-classes}|$ is small and bounded by a structural quantity (e.g., $\mathcal{F}_{\max}$ or a function of $\mathrm{Aut}(G)$), then σ-tuple is a *strong discriminative invariant* — every formation can be uniquely tagged by an element of a finite catalog. If $|\sigma\text{-classes}|$ grows freely with grid size, the σ-tuple is at most a relative invariant. The uniqueness conjecture (§6) probes which case obtains.

**Relation to OP-0008/OP-0009.** OP-0008 (σ^A K-jump non-determinism) and OP-0009 (Multi-Formation Ontological Foundations) extend σ-classes into multi-formation regime via $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$. NQ-188 fixes the single-formation case first; multi-formation σ-uniqueness is W7+ deferred.

---

## §2. σ-class definition

**Definition 2.1 (σ-equivalence).** Two minimizers $u_1^*, u_2^* \in \mathcal{L}(G, \alpha, \beta, c)$ are **σ-equivalent**, written $u_1^* \sim_\sigma u_2^*$, iff $\sigma(u_1^*) = \sigma(u_2^*)$ as ordered tuples (Commitment 14):
$$\sigma(u^*) = \big(\mathcal{F}(u^*);\ \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^K\big),$$
with the (O5')(O7) ordering conventions: ascending $\lambda_k$, then Mulliken character order on irrep ties, then lexicographic on basis representative.

**Tuple equality includes irrep labels modulo conjugation.** Per T-σ-Theorem-4 (i'), orbit representatives can have conjugate stabilizers ($\langle r^k s_y r^{-k}\rangle$ for $k \in \{0, 1, 2, 3\}$). The σ-equivalence relation is on the **conjugacy class of irrep labels** under $\mathrm{Aut}(G)$, not on labelings tied to a specific representative. Practical computation: pick any orbit representative; σ comes out the same modulo conjugation.

**Definition 2.1' (canonical conjugation-translation rule — joint with NQ-190 §3 Claim 3.1; Critic carry-forward #1, W5 Day 4 PM Wave 3 revision 2026-04-30).** $\sigma(u_1^*) \equiv \sigma(u_2^*)$ iff there exists $\pi \in \mathrm{Aut}(G)$ such that:

- **(a)** $\pi^{-1} G_{u_1^*} \pi = G_{u_2^*}$ — stabilizers are conjugate via $\pi$.
- **(b)** For all $k$, $\rho_k(u_2^*) = \rho_k(u_1^*) \circ \pi^{-1}$ — irrep labels translate under $\pi$.
- **(c)** On Schur-degenerate eigenspaces of $\dim \geq 2$ (multi-dim irreps, e.g., $D_4$ E-irrep), equivalence requires equality of *isomorphism class* of the irrep (not basis choice). Use the canonical conjugacy-class label $[\rho_k]$ throughout.
- **(d)** When $\pi$ is non-unique (degenerate stabilizer cosets), pick the lex-smallest $\pi$ in a fixed total order on $\mathrm{Aut}(G)$. This is the **Mulliken-order convention on $\mathrm{Aut}(G)$** (Commitment 14 O7 sibling).

*Remark on (c).* The Schur Lemma (Serre 1977 §2.2) guarantees that any two realizations of the same irrep on a degenerate eigenspace differ by an invertible intertwiner; the isomorphism class is therefore basis-independent, and $[\rho_k]$ is well-defined without choosing a basis. This absorbs all inner-automorphism ambiguity of $G_{u^*}$ on multi-dim eigenspaces.

*Remark on (d).* Non-uniqueness of $\pi$ arises precisely when $N_{\mathrm{Aut}(G)}(G_{u^*})/G_{u^*}$ (the outer-coset normalizer) acts non-trivially. The lex-smallest convention (Mulliken ordering) makes the choice canonical and decidable in finite $\mathrm{Aut}(G)$.

**Cross-reference.** NQ-190 §3 Claim 3.1 adopts Definition 2.1' verbatim for the inter-graph (graph-isomorphism) setting; see NQ-190 §3 for the $\phi$-transport version of conditions (a)–(d).

**Definition 2.2 (σ-class).** A **σ-class** is an equivalence class of $\mathcal{L}(G, \alpha, \beta, c)$ under $\sim_\sigma$. Write
$$[\sigma_0] := \{u^* \in \mathcal{L} : \sigma(u^*) \equiv \sigma_0 \text{ (mod conjugation)}\}.$$

**The σ-class count.** $|\sigma\text{-classes}(G, \alpha, \beta, c)| := \#\{[\sigma_0] : \sigma_0 = \sigma(u^*) \text{ for some } u^* \in \mathcal{L}\}$. This is the cardinality of the σ-tuple image of $\mathcal{L}$.

**Trivial bounds.** $1 \leq |\sigma\text{-classes}| \leq |\mathcal{L}|$. The first inequality is saturated when $\mathcal{L}$ itself is a single $\mathrm{Aut}(G)$-orbit (e.g., $L = 4$ at $\beta$ slightly above $\beta_{\mathrm{crit}}^{(2)}$ where only the first pitchfork is active; T-σ-Theorem-4 single σ-class). The second is saturated only if every minimizer has a distinct σ-tuple — unlikely on highly symmetric $G$ where graph automorphisms naturally cluster minimizers.

---

## §3. $\mathrm{Aut}(G)$-orbit vs σ-class

**Definition 3.1 ($\mathrm{Aut}(G)$-orbit).** $\mathrm{Orb}(u^*) := \{\pi \cdot u^* : \pi \in \mathrm{Aut}(G)\}$, the orbit of $u^*$ under the graph-automorphism action.

**Lemma 3.2 (Orbit ⊆ σ-class).** *Every $\mathrm{Aut}(G)$-orbit is contained in a single σ-class.*

*Proof.* Let $u_2^* = \pi \cdot u_1^*$ for $\pi \in \mathrm{Aut}(G)$. Then $\mathcal{F}(u_2^*) = \mathcal{F}(u_1^*)$ (graph-automorphism preserves local-maxima count by adjacency preservation). The Hessian commutes with $\mathrm{Aut}(G)$ (T-σ-Lemma-1 (i)), so $H(u_2^*) = \pi H(u_1^*) \pi^{-1}$, giving identical eigenvalue multisets $\{\lambda_k\}$. The eigenvector is $\phi_k(u_2^*) = \pi \phi_k(u_1^*)$, so $\mathcal{N}(\phi_k(u_2^*)) = \mathcal{N}(\phi_k(u_1^*))$ (T-σ-Lemma-2 (ii)). The irrep label $[\rho_k]$ for $u_2^*$ is the conjugate of $[\rho_k]$ for $u_1^*$ under $\pi^{-1} G_{u_1^*} \pi = G_{u_2^*}$ — these are **conjugate irreps**, equal modulo conjugacy. By Definition 2.1's "modulo conjugation" clause, $\sigma(u_1^*) \equiv \sigma(u_2^*)$. $\Box$

**Lemma 3.3 (Strict inclusion in general).** *A σ-class can contain multiple $\mathrm{Aut}(G)$-orbits if those orbits share the same σ-tuple.*

*Sketch.* Two minimizers $u_1^*, u_2^*$ lying on geometrically distinct $\mathrm{Aut}(G)$-orbits (e.g., one localized at axis $y = 0$ from one pitchfork branch, another arising from a higher-$\beta$ multi-peak configuration) can produce identical $(\mathcal{F}, \{(n_k, [\rho_k], \lambda_k)\})$ if their Hessian spectra and irrep decompositions coincide. The most direct example: at fixed $\beta$, two distinct $D_4$-orbits — say a $p$-dominant and a $g$-dominant minimizer (NQ-141 nomenclature) — share the same $\mathcal{F}$ count and identical $D_4$ irrep distribution, producing equal σ-tuples. (Requires explicit computation to confirm; if confirmed, σ-class strictly coarser than orbit.)

**Diagram.**
$$\underbrace{\mathrm{Orb}(u_1^*)}_{\subset\ [\sigma_0]} \cup \underbrace{\mathrm{Orb}(u_2^*)}_{\subset\ [\sigma_0]} \cup \cdots \subseteq [\sigma_0] \subseteq \mathcal{L}.$$

**Quotient hierarchy.** $\mathcal{L} \twoheadrightarrow \mathcal{L}/\mathrm{Aut}(G) \twoheadrightarrow \mathcal{L}/\sim_\sigma$. The first quotient is $\mathcal{M}_1$ (working/SF/symmetry_moduli.md §2.1); the second is the σ-class quotient. Both are surjective; equality holds iff every σ-class is a single orbit (open question, not assumed here).

---

## §4. Counting σ-classes — finite-group representation theory

**Combinatorial structure.** A σ-tuple $\sigma = (\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^K)$ has three independent combinatorial dimensions:

1. **$\mathcal{F}$-coordinate.** Integer in $[0, \mathcal{F}_{\max}(G, \alpha, \beta, c)]$. On 32×32 $D_4$ grid R23: $\mathcal{F}_{\max} = 63$ empirically.
2. **Sequence length $K$.** Bounded by Commitment 14 (O3) cutoff $K = \min\{k : \mu_k > 10\mu_{0+}\}$. On 32×32 grid: $K \approx 12$ empirically (NQ-141 mode-ℓ analysis).
3. **Per-mode triple $(n_k, [\rho_k], \lambda_k)$.**
   - $n_k \in \{2, 3, \ldots, k+1+\mathcal{C}_{\mathrm{frust}}\}$ per Lemma 2 (iii)+(v); on balanced-Laplacian regime $n_k \in \{2, \ldots, k+1\}$.
   - $[\rho_k] \in \widehat{G_u}$, where $\widehat{G_u}$ is the irrep set of the residual symmetry group. For $D_4$: $\widehat{D_4} = \{A_1, A_2, B_1, B_2, E\}$ (5 irreps). For $\mathbb{Z}_2$ (post-pitchfork stabilizer per T-σ-Theorem-4 (i)): $\widehat{\mathbb{Z}_2} = \{[+1], [-1]\}$ (2 irreps).
   - $\lambda_k \in \mathbb{R}_{>0}$ (continuous; not a finite combinatorial coordinate). The σ-tuple as defined is "labelled" by exact $\lambda_k$ values, but practical equivalence quotients $\lambda_k$ at finite resolution.

**Bound 4.1 (Combinatorial upper bound).** Treating $\lambda_k$ at fixed resolution $\Delta\lambda$ over $[\mu_2, 10\mu_2]$:
$$|\sigma\text{-classes}| \leq (\mathcal{F}_{\max} + 1) \cdot \prod_{k=1}^{K}\big[\,n_{\max} \cdot |\widehat{G_u}| \cdot M_\lambda\,\big]$$
where $M_\lambda := \lceil 9\mu_2/\Delta\lambda \rceil$ is the eigenvalue resolution count and $n_{\max} \leq K + 1$. For $D_4$ on 32×32, $K = 12$, $|\widehat{D_4}| = 5$, $\mathcal{F}_{\max} = 63$, $\Delta\lambda = 0.01\mu_2$: bound is exponentially large ($\sim 64 \cdot (12 \cdot 5 \cdot 900)^{12} \approx 10^{55}$). **This bound is uninformative for a uniqueness statement** — combinatorial space is far too large for σ-class concentration to be detected by counting alone. Empirical concentration (§5) is the only path to a meaningful $|\sigma\text{-classes}|$ count.

**Specht polynomial analogy.** The σ-tuple is conceptually parallel to a multi-set of Specht-irrep labels (Specht 1935; James–Kerber 1981 §6) on each Hessian eigenspace. The uniqueness question parallels: "how many distinct Specht patterns appear in $\mathcal{L}$?" — a question that does not admit closed-form answers without strong structural restrictions on $G$.

**Sagan (2001) framework.** §1.5 of *The Symmetric Group* discusses that the irreducible representations of $S_n$ are indexed by partitions of $n$, but σ-tuples here are over $\widehat{G_u}$ with $G_u \subseteq \mathrm{Aut}(G)$ (residual symmetry group), not $S_n$. The analogue is that σ-tuples form a *labeled set* indexed by $(\mathcal{F}, \widehat{G_u}^{\otimes K})$ with $\lambda$-ordering — a structured combinatorial object whose enumeration depends on $\mathrm{Aut}(G)$ structure.

---

## §5. R23 empirical test (OAT-7 synergy)

**Dataset.** R23 fullscale (`CODE/scripts/results/exp_orbital_fullscale.json`): 56 stable minimizers on 32×32 $D_4$ free-BC grid at $\beta = 30$, $\alpha = 1$, $c = 0.5$. Per `working/MF/single_high_F_equivalence.md` §4.3, NQ-141 covers $\mathcal{F} \in [5, 63]$ across 6 orbital letters $\{p, d, f, g, h, i\}$ with 324 mode-ℓ pair observations (0 exceptions in σ-irrep correspondence via $\ell \bmod 4 \to D_4$ irrep table).

**σ-class extraction protocol.**

1. For each $u^* \in \mathcal{L}_{R23}$, compute the constrained Hessian $H(u^*)$ via Prop 1.3a (closed form on $D_4$ grid: $4\alpha L_G + \beta W''(u^*) \cdot \mathrm{diag}$).
2. Diagonalize on $\mathbf{1}^\perp$; extract $K$ smallest eigenvalues $\{\lambda_k\}_{k=1}^K$ with $K = 12$ per O3 cutoff.
3. Compute nodal counts $\mathcal{N}(\phi_k)$ per Lemma 2 (i).
4. Compute residual stabilizer $G_{u^*} := \mathrm{Stab}_{D_4}(u^*)$ via $D_4$-action membership test.
5. Project each $\phi_k$ onto $\widehat{G_{u^*}}$ isotypic components per Lemma 1 (ii); assign $[\rho_k]$ as the dominant component.
6. Record $\mathcal{F}(u^*)$ via local-maxima enumeration on $G$.
7. Apply (O5')(O7) ordering to produce canonical σ-tuple.

**Equivalence test.** Two minimizers $u_1^*, u_2^*$ have σ-equivalent tuples iff:
- $\mathcal{F}(u_1^*) = \mathcal{F}(u_2^*)$ (integer match);
- $K(u_1^*) = K(u_2^*)$ (sequence length match);
- $\mathcal{N}(\phi_k^{(1)}) = \mathcal{N}(\phi_k^{(2)})$ for $k = 1, \ldots, K$ (nodal-count match);
- $[\rho_k^{(1)}]$ and $[\rho_k^{(2)}]$ are conjugate in $\widehat{G_{u^*}}$ for all $k$;
- $|\lambda_k^{(1)} - \lambda_k^{(2)}| < \epsilon_\lambda$ for some tolerance $\epsilon_\lambda$ (default: $10^{-6} \mu_2$ per `exp_hessian_uniform_v2.json` precision).

**Expected outcome.** Per OAT-7's PH-vs-σ analysis (working/MF/single_high_F_equivalence.md §5), the (F=51, K=5) pair with $p$-dominant vs $g$-dominant modes belongs to **distinct σ-classes** but identical PH classes. This implies $|\sigma\text{-classes}| > |\text{PH classes}|$; σ refines PH. Empirically: 6 orbital letters × per-letter sub-clusters ≈ 8–14 σ-classes (rough estimate; actual count requires running the protocol above on R23).

**Falsifiable prediction (BC-188-emp).** $|\sigma\text{-classes}(R23)| \in [6, 20]$, strictly less than the 56 minimizer count. Run via:
```python
# CODE/scripts/sigma_class_count_R23.py (proposed)
from scc import GraphState, ParameterRegistry, find_formation
import json
data = json.load(open("results/exp_orbital_fullscale.json"))
sigma_tuples = [compute_sigma_tuple(u) for u in data["minimizers"]]
classes = group_by_equivalence(sigma_tuples, eps_lambda=1e-6)
print(f"sigma-class count: {len(classes)}")
```

This empirical extraction is the first NQ-188 deliverable; W5 Day 4+ scope.

---

## §6. Uniqueness conjecture

**Conjecture BC-188-1 (Parameter Independence of σ-Class Count).** *On fixed $G = D_4$ free-BC $L \times L$ grid, fixed mass $m$, the σ-class count*
$$|\sigma\text{-classes}(G, \alpha, \beta, c)|$$
*depends only on $(G, \mathcal{F}_{\max}(G, \alpha, \beta, c))$ — not on the precise $(\alpha, \beta, c)$ specifics within the spinodal-interior stable-minimizer regime.*

**Heuristic motivation.** σ-tuples are determined by the discrete Hessian-eigenvector structure (Laplacian eigenfunctions on $G$) and their $D_4$ irrep decomposition (a finite catalog). As $(\alpha, \beta, c)$ vary smoothly within spinodal interior, eigenvalues $\lambda_k$ shift continuously, but the **ordering and irrep assignment** of σ-tuple entries stay invariant outside of pitchfork-bifurcation surfaces. Between bifurcations, the σ-class structure is constant; at bifurcation crossings, σ-classes may split or merge by exactly one entry.

**Stronger Conjecture BC-188-2 (Universality).** *$|\sigma\text{-classes}|$ is a function only of $|\mathrm{Aut}(G)|$ and $\mathcal{F}_{\max}$:*
$$|\sigma\text{-classes}(G, \cdot, \cdot, \cdot)| = f_{\sigma}(|\mathrm{Aut}(G)|,\ \mathcal{F}_{\max}).$$
This is a universality claim: the σ-class count is determined by the symmetry group order and the maximum nodal count, independent of graph specifics. **Status: speculative.** Evidence is needed across multiple $G$ classes (cycles, tori, complete graphs, random graphs at fixed $|\mathrm{Aut}(G)|$).

**Verification path.**
- **Step 1 (Cat A target).** Run §5 protocol on R23 ($L = 32$) to get $|\sigma\text{-classes}|$ at $\beta = 30, c = 0.5$. ETA: 1 week.
- **Step 2 (Cat B intermediate).** Run on $L \in \{8, 16\}$ at the same parameters; check that the count scales predictably with $\mathcal{F}_{\max}(L)$.
- **Step 3 (Cat A or Cat B definitive).** Vary $\beta \in [\beta_{\mathrm{crit}}^{(2)}, 50]$ and $c \in [(3-\sqrt{3})/6, 0.7]$ at $L = 16$; check whether $|\sigma\text{-classes}|$ stays constant within $\mathcal{F}$-fixed parameter strata.

**Risk of refutation.** If $\beta$-sweep at fixed $\mathcal{F}_{\max}$ shows σ-class count drift, BC-188-1 falls and σ-tuple is parameter-sensitive (Cat C status). The uniqueness theorem then requires a different formulation (e.g., σ-class as a function of $(G, \mathcal{F}_{\max}, \beta)$).

---

## §7. σ-class uniqueness as foundational lemma

**Strong invariant claim.** If BC-188-1 holds and $|\sigma\text{-classes}|$ is small (e.g., $\leq 20$ for R23), then σ-tuple is a **strong discriminative invariant** — every formation can be canonically tagged by a finite catalog of σ-classes that does not depend on parameter fine-tuning.

**Cat A target reformulation.**

> **T-σ-Uniqueness (NQ-188 candidate, single-formation, $D_4$ free-BC).** Let $G$ be the $D_4$ free-BC $L \times L$ grid with $L \in \{4, 8, 16, 32\}$, parameters $(\alpha, \beta, c)$ in spinodal interior with $\beta \in (\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{merge}})$ (single-formation regime), and $\mathcal{L}(G, \alpha, \beta, c) \subset \Sigma_m^{\circ}$ the set of Morse-0 stable local minimizers. Then:
>
> **(i)** $|\sigma\text{-classes}(G, \alpha, \beta, c)|$ is finite.
>
> **(ii)** $|\sigma\text{-classes}|$ depends only on $(G, \mathcal{F}_{\max}(G, \alpha, \beta, c))$ and not on $(\alpha, \beta, c)$ specifics within strata of fixed $\mathcal{F}_{\max}$ (Conjecture BC-188-1).
>
> **(iii)** For $L = 32$, $\beta = 30$, $c = 0.5$ (R23 regime): $|\sigma\text{-classes}|$ is bounded by the orbital-letter count (6) times an irrep-assignment factor; empirical target $|\sigma\text{-classes}| \in [6, 20]$.
>
> *Status:* (i) **Cat A** (finiteness — combinatorial $\mathcal{F}$-bound + $\widehat{G_u}$ finiteness + Lemma 2 (iii)/(v) bounded $n_k$); (ii) **Cat B target** (parameter independence — empirical verification needed across spinodal interior); (iii) **Cat A target** (R23 enumeration — direct computation).

**Proof sketch of (i).**

*Finiteness argument.* Bound 4.1 establishes $|\sigma\text{-classes}| \leq C \cdot |\widehat{G_u}|^K \cdot \mathcal{F}_{\max}$ at fixed resolution $\Delta\lambda$. For finite graphs, $G_u \subseteq \mathrm{Aut}(G)$ is finite, so $\widehat{G_u}$ is finite. $K$ is finite per (O3) cutoff. $\mathcal{F}_{\max}$ is finite per $\mathcal{F}(u^*) \leq |X|$ (every site is a candidate local max). Hence $|\sigma\text{-classes}|$ is finite. $\Box$ **Cat A.**

*Proof sketch of (ii).* Parameter continuity. As $(\alpha, \beta, c)$ vary smoothly within spinodal interior away from pitchfork bifurcations, $\mathcal{L}(G, \alpha, \beta, c)$ varies smoothly (implicit function theorem on $\nabla\mathcal{E} = 0$ equation). σ-tuples assigned by Lemma 1 (ii) project + Lemma 2 (i) nodal count are determined by Hessian eigenvector signs and irrep labels — both **locally constant** in parameter (eigenvalue ordering and irrep types do not change without crossing a bifurcation surface). On parameter strata where $\mathcal{F}_{\max}$ is constant, σ-class count is locally constant. **Cat B target** — full proof requires bifurcation-surface analysis which is open.

**Proof sketch of (iii).** Reduce R23 σ-class computation to direct enumeration via §5 protocol. Empirical target. **Cat A target — pending §5 execution.**

---

## §8. Connection to T-σ-Lemma-3 + V5b family

V5b (T-V5b-T canonical + V5b-T-zero sub-statement + V5b-F sub-statement) decomposes into 3 distinct σ-classes corresponding to 3 sub-statements per CV-1.5.1 promotion:

**V5b-T sub-class (Cat A definitional).** Translation Goldstone σ-tuple on translation-invariant graphs. Universal nodal count $n = 2$ per T-σ-Lemma-3 (iii). σ-tuple structure: $(\mathcal{F}; (2, [\rho_{\mathrm{Goldstone}}], 0), \ldots)$. Eigenvalue $\lambda_0 = 0$ exact (continuous symmetry breaking on infinite/torus graphs).

**V5b-T-zero sub-class (Cat A definitional).** σ-tuple with $\lambda_0 = 0$ exact (degenerate Goldstone), distinct from V5b-T because zero is achieved at finite-graph translation-invariant cases. σ-tuple structure: $(\mathcal{F}; (2, [\rho_{\mathrm{trans}}], 0), \ldots)$ with the leading entry encoding the discrete translation pseudosymmetry.

**V5b-F sub-class (Cat C, NQ-173 dependent).** σ-tuple on boundary-modified graphs where partial Goldstone is broken: $\mu \approx C(\beta) |\partial S|/n$ — *finite but small* (boundary suppression of would-be Goldstone). σ-tuple structure: $(\mathcal{F}; (2, [\rho_{\mathrm{partial-Goldstone}}], C(\beta)|\partial S|/n), \ldots)$. The $\lambda_0$ entry distinguishes it from V5b-T/V5b-T-zero.

**Implication for σ-uniqueness.** The V5b family produces 3 distinct σ-classes within a single graph topology by varying boundary conditions. This shows σ-class structure depends on **graph** $G$ (including boundary conditions), confirming the (G, parameters) refinement in NQ-188's regime statement. σ-uniqueness as Cat A holds **per graph topology**; transitions between topology classes (free-BC ↔ periodic ↔ boundary-modified) shift the σ-class catalog.

**Open question NQ-188-V5b.** Are the V5b-T, V5b-T-zero, V5b-F σ-classes the only σ-classes arising from the Goldstone family on 2D translation-modified graphs, or are there higher Goldstone-derived σ-classes (e.g., commensurability-split doublets per T-V5b-T-(c))? — W6+ deferred.

---

## §9. Cat target

**Cat A target (R23 enumeration).** Direct σ-class computation on R23 32×32 fullscale dataset. ETA 1 week. Deliverable: `CODE/scripts/sigma_class_count_R23.py` + JSON output `CODE/scripts/results/sigma_class_R23.json`. Anchors §7 statement (iii).

**Cat A target ($L = 8$ definitive enumeration).** Run on $L = 8$ where $\mathcal{F}_{\max} \approx 6$ and $\mathcal{L}$ is small enough for exhaustive enumeration via random initialization sweeps + xNES population dump. Target: definitive count $|\sigma\text{-classes}(L = 8)|$ as Cat A. Anchors §7 statement (i) at small scale.

**Cat B target ($\beta$-sweep parameter independence).** Vary $\beta \in [\beta_{\mathrm{crit}}^{(2)}, 50]$ at $L = 16$ in 10 increments; compute σ-class count at each. Check stratified constancy. Anchors §7 statement (ii) (BC-188-1).

**Cat C conjecture (asymptotic scaling formula).**
$$|\sigma\text{-classes}(G_L, \alpha, \beta, c)|\ \overset{?}{\sim}\ f_{\sigma}(\mathcal{F}_{\max}(L), |\mathrm{Aut}(G_L)|).$$
Possible forms:
- *Linear in $\mathcal{F}_{\max}$*: $f \sim a + b \cdot \mathcal{F}_{\max}$.
- *Logarithmic*: $f \sim c \log \mathcal{F}_{\max}$.
- *Bounded*: $f \leq |\widehat{D_4}|^K = 5^K$ for $K$ fixed by O3 cutoff.

The bounded case is most physical: σ-tuples form a finite catalog whose size is set by symmetry-group representation theory, not by graph size.

---

## §10. External references

- Sagan, B. E. (2001). *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* (2nd ed.). Springer Graduate Texts in Mathematics 203. Cited for representation-theoretic framework on $S_n$ irreps; the $\widehat{G_u}$ irrep theory used in σ-tuple irrep-label assignment is the analog over $\mathrm{Aut}(G) \supseteq G_u$.
- Specht, W. (1935). "Die irreduziblen Darstellungen der symmetrischen Gruppe." *Mathematische Zeitschrift* 39:696–711. Original Specht polynomials; foundation for irrep enumeration via partitions, conceptually parallel to the $(\mathcal{F}, K)$-stratified σ-tuple enumeration.
- James, G. D., & Kerber, A. (1981). *The Representation Theory of the Symmetric Group*. Encyclopedia of Mathematics and Its Applications 16. Cambridge University Press. §6 character tables and partition-indexed irreps; foundational for the $\widehat{G_u}$ irrep theory invoked in §4–5.
- Serre, J.-P. (1977). *Linear Representations of Finite Groups*. Springer GTM 42. (Already canonical via T-σ-Lemma-1; recapped here for Maschke + Schur.)
- Sattinger, D. H. (1979). *Group Theoretic Methods in Bifurcation Theory*. Springer LNM 762. Equivariant Crandall–Rabinowitz framework underlying T-σ-Theorem-4 and the §3.3 axis-selection; relevant for σ-class transitions across bifurcation surfaces.

---

## §11. W7+ priority + Cross-references

**W7+ priority.** W5 Day 4+ scope: §5 R23 protocol execution + §9 Cat A target $L = 8$ enumeration. W6 scope: BC-188-1 $\beta$-sweep verification. W7+ scope: BC-188-2 universality across graph classes + multi-formation extension via $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ (per OP-0008/OP-0009).

**Cross-references.**
- **Canonical §11.1 Commitment 14 (W5 added 2026-04-29 (O5')(O7))**: σ-tuple definition + ordering conventions invoked throughout §2, §5.
- **Canonical §13 T-σ-Lemma-1**: Aut(G)-orbit invariance of σ-tuple modulo $G_u$-conjugation (§3 Lemma 3.2).
- **Canonical §13 T-σ-Lemma-2**: nodal-count properties (§5 protocol step 3).
- **Canonical §13 T-σ-Lemma-3**: Goldstone-ℓ=1 angular saturation; anchors V5b family σ-class distinctions (§8).
- **Canonical §13 T-σ-Theorem-3**: σ at uniform on $D_4$ free-BC grid; provides closed-form σ-tuple at uniform critical point (used in §5 baseline).
- **Canonical §13 T-σ-Theorem-4**: σ at first pitchfork; orbit-representative remark (i') is the foundation for "modulo conjugation" clause in Definition 2.1 (§2).
- **Canonical §14 CN17**: σ-Labeled Formation Quantization; NQ-141 R23 empirical anchor; OAT-7 σ-class vs PH coarseness (working/MF/single_high_F_equivalence.md).
- **Working `working/MF/single_high_F_equivalence.md` §4.4–§5 (OAT-7)**: PH-coarser-than-σ scenario; (F=51, K=5) $p$ vs $g$ pair empirical evidence.
- **Working `working/MF/multi_formation_sigma.md` §5.5, §10**: NQ-188 multi-formation extension noted; $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ framework deferred to W7+.
- **Working `working/SF/symmetry_moduli.md` §2 ($\mathcal{M}_1$)**: K=1 single-formation moduli space quotient $\mathcal{L}/\mathrm{Aut}(G)$; σ-class quotient $\mathcal{L}/\sim_\sigma$ is a further quotient (§3 hierarchy).
- **Working `working/SF/mode_count.md` Prop 1.3a**: closed-form Hessian on $D_4$ grid; computational base for §5 protocol step 1.
- **Working `working/SF/cardinality_open.md` §8**: Morse index structure relevant to bifurcation-surface analysis underlying BC-188-1 proof of (ii).
- **Working `working/SF/sigma_theorem4_higher_order.md` §3, §10 (NQ-187; W5 Day 4 PM Wave 3 cross-link, carry-forward #10)**: 5th-order $D_4$-equivariant non-existence + sextic $\epsilon^2$ first-order splitting. Refines the σ-class denominator on R23: σ-classes that collapse at leading-order Hessian (T-σ-Theorem-4 (ii) $K_0 = K_1$) split at $\epsilon^2$, increasing the empirical $|\sigma\text{-classes}|$ count under §5 protocol when the higher-order spectrum is resolved.
- **Working `working/SF/sigma_lie_algebra_structure.md` §4, §9 (NQ-258; W5 Day 4 PM Wave 3 cross-link)**: σ-tuple recognized as the $\mathrm{Aut}(G)_{u^*}$-irrep decomposition of $T_{u^*}\Sigma_m$; this is the Lie-algebra/representation-theoretic restatement of Definition 2.1 used in §4 (irrep-label assignment via isotypic projection). NQ-258 McKay-spirit conjecture upper-bounds $|\sigma\text{-classes}|$ via $|\mathrm{Irr}(N_\Gamma(P))|$ at fixed Sylow $P$.
- **Open Problems**: OP-0008 (σ^A K-jump non-determinism), OP-0009 (Multi-Formation Ontological Foundations) — both extend NQ-188 to multi-formation regime.

---

## §12. Hard constraints (compliance)

- [x] **Direct canonical edits: 0.** This file proposes a Cat A target via the W7+ promotion pipeline; canonical §13 entries are not modified.
- [x] **CN10 (contrastive vs reductive).** σ-tuple is SCC-intrinsic Hessian-spectral mathematics. Atomic-orbital terminology ($p, d, f, g, h, i$) is a *contrastive label* used only as a nomenclature shorthand for the $\ell \bmod 4 \to D_4$ irrep decomposition; the σ-uniqueness theorem statements (§7) are framed in terms of $\widehat{G_u}$ representation theory, not borrowed atomic structure. The orbital-letter count "6" appears as an empirical R23 dataset summary (§5, §7), not as a theoretical primitive.
- [x] **F-1 / M-1 / MO-1 not silently resolved.** F-1 (W4 split-resolved via T-Merge (b) + T-PreObj-1 (i)) and M-1 (W4 layer-clarified) are referenced but not invoked. MO-1 (sidestepped for single-formation σ scope) remains open per §13 OP-0003 rider; multi-formation σ-uniqueness extension would re-engage MO-1 stratified Morse, deferred to W7+.
- [x] **No re-introduction of Research OS structure.** No 5-role daily-log mapping; single working file per topic per CLAUDE.md policy.
- [x] **Cat target distinctions explicit.** Cat A (R23 enumeration, $L = 8$ definitive), Cat B ($\beta$-sweep parameter independence), Cat C (asymptotic scaling) clearly demarcated per §9.
- [x] **Open questions registered.** NQ-188 (this file); NQ-188-V5b (§8 Goldstone-derived σ-class enumeration); BC-188-1 (parameter independence); BC-188-2 (universality); BC-188-emp (R23 empirical bound).

---

## §13. Cat A (conditional under canonical conjugation rule) vs Cat A (unconditional)

**Conditionality statement (Critic carry-forward #2, W5 Day 4 PM).** All Cat A claims in this file are *conditional* on Definition 2.1' (the canonical conjugation-translation rule, §2 above) being adopted as a canonical convention.

Specifically:

- **Cat A (conditional)** — T-σ-Uniqueness (i) (finiteness of $|\sigma\text{-classes}|$, §7): The proof via Bound 4.1 is complete *given* that "σ-class" means equivalence under Definition 2.1'. Without a canonical conjugation rule, two minimizers in the same $\mathrm{Aut}(G)$-orbit could be miscounted as distinct classes (basis-choice artifact on $D_4$ E-irrep eigenspaces). Definition 2.1' closes this loophole.

- **Cat A (conditional)** — R23 enumeration target (§7 (iii), §9): The σ-class count from the §5 protocol depends on step 5 (irrep-label assignment via isotypic projection). Without clause (c) of Definition 2.1', two runs on the same minimizer with different eigenbasis choices could yield different $[\rho_k]$ labels on degenerate eigenspaces, inflating the empirical class count. Definition 2.1' makes the empirical protocol basis-independent.

- **Cat A (unconditional)** — Lemma 3.2 (Orbit ⊆ σ-class): this statement is unconditional; it follows from T-σ-Lemma-1's $\mathrm{Aut}(G)$-orbit invariance regardless of conjugation convention. The new rule only affects whether *different* orbits collapse to the same σ-class.

**CV-1.6 candidate.** Definition 2.1' is a proposed canonical convention addition (CV-1.6 candidate) to canonical.md §11.1 Commitment 14 ordering conventions. Adoption requires: (1) promotion via daily log, (2) cross-sign-off from NQ-190 §3, (3) canonical §11.1 edit adding clauses (a)–(d) under Commitment 14. Until CV-1.6 is adopted, all Cat A claims above carry the "(conditional)" qualifier.

---

## §14. Wave 3 Revision Log (W5 Day 4 PM)

**Timestamp:** 2026-04-30, Wave 3 W5 Day 4 PM revision.

**Critic finding addressed:** Critic re-review `logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.2 — joint issue NQ-188/NQ-190: "modulo conjugation" under-specified on Schur-degenerate multi-dim irreps (e.g., $D_4$ E-irrep); carry-forward item #1.

**Changes made:**

1. **§2 Definition 2.1'** — replaced informal "modulo conjugation" paragraph + previous partial (T1/T2/T3) formulation with the four-clause canonical conjugation-translation rule (a)–(d), including Schur-orthogonality remark on (c) and Mulliken-order convention on (d). Added cross-reference to NQ-190 §3 Claim 3.1.

2. **§13 (new)** — added "Cat A (conditional) vs Cat A (unconditional)" section clarifying that finiteness proof and R23 empirical protocol are conditional on Definition 2.1' adoption; T-σ-Uniqueness Cat A claims carry "(conditional)" qualifier pending CV-1.6 canonical adoption.

3. **Cross-link installed** — §2 Definition 2.1' now cites NQ-190 §3 Claim 3.1 (carry-forward #10, missing pair NQ-188 ↔ NQ-190).

4. **No canonical/ edits** — working-only per promotion pipeline policy.

5. **CN10, CN5, u_t primitive** — unchanged; no new theorems introduced; change is a canonical-translation-rule cleanup.

---

**End of working file.** Promotion pipeline next stage: §5 R23 protocol execution → empirical $|\sigma\text{-classes}|$ count → §7 statement (iii) Cat A claim → W6 review → W7+ canonical §13 candidate entry "T-σ-Uniqueness".
