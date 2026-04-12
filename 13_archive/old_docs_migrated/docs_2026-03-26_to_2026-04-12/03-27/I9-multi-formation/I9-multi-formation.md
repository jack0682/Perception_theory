# Iteration 9 — Multi-Formation Theory

**Date:** 2026-03-27
**Status:** Architectural Decision + Formal Extension
**Vulnerability Addressed:** V6 (Multi-formation blocked — HIGH severity, "Very Hard" fix)

---

## 0. The Problem

The current theory handles **one** formation: a single soft cohesion field $u_t : X_t \to [0,1]$. Real scenes contain **multiple** cohesive formations — a cup on a table next to a book, three people in a room, overlapping clouds. This is not an edge case; it is the generic situation.

The single-formation limitation is architecturally load-bearing, not merely a matter of scope:

1. **Contraction uniqueness.** The contraction regime ($a_{\mathrm{cl}} < 4$) guarantees a unique closure fixed point on $[0,1]^n$, so the closure operator itself cannot distinguish multiple formations.
2. **Distinction incoherence.** The distinction operator $\mathbf{D}_t(x; 1-u_t)$ computes against $1 - u_t$, the global complement. With two formations $u^{(1)}$ and $u^{(2)}$, formation 1's "exterior" includes formation 2 — but formation 2 is not exterior to itself. The distinction operator conflates other-formation with true-exterior.
3. **Energy landscape collapse.** The energy $\mathcal{E}(u)$ has a single field as input. There is no mechanism for two formations to exert repulsive pressure on each other or to negotiate shared boundary regions.

This document evaluates four architectural options, makes a binding decision, formalizes the chosen architecture, develops the $K=2$ special case, and connects the extension to existing theory.

---

## Part 1: Architecture Options — Deep Analysis

### Option A: Non-Contraction / Iterative Peeling

**Concept.** Run the single-formation theory $K$ times. Find $u^{(1)} = \arg\min \mathcal{E}(u)$. Then mask the support of $u^{(1)}$ and find $u^{(2)} = \arg\min \mathcal{E}(u \mid \mathrm{supp}(u) \cap \mathrm{supp}(u^{(1)}) = \emptyset)$. Repeat.

**Detailed assessment:**

*Strengths:*
- Requires zero theory changes. The existing energy, operators, and theorems apply unmodified at each step.
- Computationally simple: $K$ independent optimizations.
- Each individual formation inherits all proved results (T1, T6a/b, T8-Core, T14, etc.).

*Weaknesses:*
- **Order dependence.** The first formation found monopolizes the most energetically favorable region. The second formation is constrained to the residual. Swapping the order may yield different formations. This is not a minor implementation detail — it means the multi-formation decomposition is not well-defined.
- **No interaction model.** Formations do not influence each other. There is no repulsive term preventing overlap, no attractive term encouraging merging, no mechanism for competition over shared boundary regions. Two formations that should repel (distinct objects) behave identically to two formations that should attract (merging blobs).
- **Masking is crisp.** The exclusion constraint $\mathrm{supp}(u^{(1)}) \cap \mathrm{supp}(u^{(2)}) = \emptyset$ introduces a hard boundary into a theory committed to soft, graded fields. This violates Fixed Commitment FC1 (primacy of soft cohesion fields).
- **Volume budget allocation.** Each formation needs its own $m^{(k)}$. How is the total cohesive budget $m$ distributed among $K$ formations? This requires an external allocation rule not derivable from the theory.

*Verdict:* **Rejected.** The order dependence and crisp masking are fatal. This approach imports external structure (ordering, hard boundaries, budget allocation) rather than deriving multi-formation behavior from the theory's own principles. It is an engineering workaround, not a theoretical extension.

---

### Option B: K-Field Theory

**Concept.** Replace the scalar field $u_t : X_t \to [0,1]$ with a vector field $(u^1_t, \ldots, u^K_t) : X_t \to [0,1]^K$ where each component $u^k_t$ is the cohesion field of the $k$-th formation. Impose a simplex-like constraint:

$$\sum_{k=1}^{K} u^k_t(x) \leq 1 \quad \text{for all } x \in X_t$$

ensuring that each site's total cohesive participation is bounded. The residual $1 - \sum_k u^k_t(x)$ represents the degree to which site $x$ is exterior to all formations.

**Detailed assessment:**

*Strengths:*
- **Principled interaction.** The simplex constraint creates natural competition: if formation $k$ claims site $x$, there is less capacity for formation $j$ to claim it. This is a soft, graded form of mutual exclusion — exactly what the theory's ontology demands.
- **Formation-specific distinction.** The distinction operator for formation $k$ can compute against $1 - u^k_t$, which now correctly includes both the exterior and other formations. Or, more precisely, against $\sum_{j \neq k} u^j_t + (1 - \sum_j u^j_t)$, distinguishing between "occupied by another formation" and "truly exterior."
- **Joint energy.** A single energy functional $\mathcal{E}(u^1, \ldots, u^K)$ governs all formations simultaneously, with cross-terms encoding interactions.
- **Overlap handling.** The inequality $\sum_k u^k(x) \leq 1$ permits partial overlap: two formations can both claim fractional participation at a boundary site.

*Weaknesses:*
- **$K$ must be chosen.** The number of formations is an input, not an output. This contradicts Commitment Note CN6 ("$K$ must be emergent"). However, this can be partially addressed by allowing formations to "die" (converge to $u^k \equiv 0$) during optimization, starting from $K_{\max}$ and letting the energy select the actual number.
- **State space.** The field is now $n \times K$-dimensional, where $n = |X_t|$. For $K = 10$ on a $100 \times 100$ grid, this is $10^5$ dimensions. The energy landscape becomes vastly more complex.
- **Symmetry.** The $K$ fields are interchangeable — permuting the labels $\{1, \ldots, K\}$ yields an equivalent configuration. This creates a $K!$-fold symmetry in the energy landscape that complicates optimization (modes are equivalent under relabeling).

*Verdict:* **Strong candidate.** The principled interaction, soft overlap handling, and joint energy are exactly what the theory needs. The $K$-selection problem and state space are real but addressable.

---

### Option C: Spectral $\mathbf{C}_t$ Decomposition

**Concept.** Use the eigenstructure of the co-belonging operator $\mathbf{C}_t = (I - \alpha W_{\mathrm{sym}})^{-1}$ to identify distinct cohesive clusters. The leading eigenvectors of $\mathbf{C}_t$ (equivalently, of $W_{\mathrm{sym}}$) partition the site space into regions of high mutual co-belonging. $K$ emerges as the number of significant eigenvalues or the spectral gap structure.

**Detailed assessment:**

*Strengths:*
- **$K$ is emergent.** The number of formations is read off from the spectral structure — the number of eigenvalues above a threshold, or the position of a spectral gap. This aligns with CN6.
- **Mathematically elegant.** Spectral decomposition of graph operators is well-understood. The resolvent $\mathbf{C}_t$ already captures multi-hop relational structure; its eigenstructure naturally encodes cluster information.
- **Uses existing infrastructure.** $\mathbf{C}_t$ is already a primitive operator with axioms (C1–C4) and a provisional realization. This approach leverages existing theory rather than importing new structure.

*Weaknesses:*
- **$\mathbf{C}_t$ is diagnostic-only (FC12).** Fixed Commitment 12 states that $\mathbf{C}_t$ enters predicates but not the energy functional. Making $\mathbf{C}_t$ the primary mechanism for multi-formation decomposition elevates it from diagnostic to structurally load-bearing — a role it was explicitly excluded from. This would require revising FC12.
- **Circular dependence.** $\mathbf{C}_t$ depends on $u_t$ (through $W_{\mathrm{sym}}$). But if $u_t$ is a single field, $\mathbf{C}_t$ reflects the structure of that single field. To identify multiple formations, you need multiple fields; but to construct $\mathbf{C}_t$, you need the fields already. The spectral decomposition can identify clusters within a *given* field, but it cannot generate the multi-field structure from scratch.
- **No energy, no dynamics.** Spectral decomposition identifies structure but provides no variational principle for how formations interact, compete, merge, or split. It is a diagnostic tool, not a generative mechanism. Multi-formation theory needs dynamics (energy minimization, gradient flow), not just classification.
- **Post-hoc, not constitutive.** This approach reads multi-formation structure out of a single field after the fact, rather than building it into the theory's primitive ontology. A single $u_t$ that contains two "bumps" is decomposed into two formations by spectral analysis — but the theory never committed to those bumps being separate formations. The decomposition is imposed, not derived.

*Verdict:* **Rejected as primary architecture.** The diagnostic-only status (FC12), circular dependence, and absence of dynamics are disqualifying. However, spectral $\mathbf{C}_t$ analysis may serve as a valuable *diagnostic* for the chosen architecture — a way to assess whether a multi-field decomposition is coherent.

---

### Option D: Bounded Scope / Localization

**Concept.** Define formations locally via connected components of superlevel sets $\{x : u_t(x) \geq \theta\}$. Each connected component at threshold $\theta$ is a candidate formation. This is already implicit in the $H_0$ persistence machinery used for $\mathcal{Q}_{\mathrm{morph}}$.

**Detailed assessment:**

*Strengths:*
- **Simple and already present.** The persistence-based $\mathcal{Q}_{\mathrm{morph}} = \ell_{\max} \cdot \mathrm{Artic}$ already computes $H_0$ connected components. Multi-formation identification is a natural extension: instead of taking only the longest bar, take all bars above a persistence threshold.
- **$K$ is emergent.** The number of significant connected components at each threshold level is determined by the field, not imposed externally.
- **No theory changes needed.** The existing energy and operators are untouched; formations are identified post-hoc from the single field.

*Weaknesses:*
- **No interaction model.** Like Option A, formations identified by localization do not influence each other. There is no repulsive energy between formations, no competition mechanism, no principled overlap handling.
- **Single field, multiple readings.** The theory still optimizes a single $u_t$. Two "formations" in this approach are just two bumps in one field. They cannot have independent closure properties, independent distinction operators, or independent diagnostic vectors. They share all operators.
- **Distinction remains incoherent.** The distinction operator still computes against $1 - u_t$ globally. A site in formation 1's boundary that is adjacent to formation 2 will have its distinction score contaminated by formation 2's cohesion.
- **Overlap is impossible.** Connected components of superlevel sets are disjoint by construction. Two formations cannot claim partial participation at the same site. This is a hard partition of the field, not a soft decomposition.

*Verdict:* **Rejected as primary architecture.** Useful as a diagnostic and for the $K=1$ case (where it already operates via $\mathcal{Q}_{\mathrm{morph}}$), but fundamentally inadequate for genuine multi-formation theory. The absence of interaction and the impossibility of overlap are fatal.

---

## Part 2: Architecture Decision

### Decision: Option B — K-Field Theory

**Binding.** The multi-formation extension of Soft Cognitive Cohesion adopts the $K$-field architecture.

### Justification

**1. Ontological priority preserved.** The soft cohesion field remains the primitive entity. We simply acknowledge that the world may contain multiple primitive fields, each representing a distinct cohesive formation. The vector $(u^1_t, \ldots, u^K_t)$ is not a departure from the theory's ontology — it is its natural pluralization. Each $u^k_t$ is individually a soft cohesion field satisfying the same ontological status as the original $u_t$. The simplex constraint $\sum_k u^k(x) \leq 1$ is the soft, graded analogue of the intuition that "the same site cannot fully participate in two distinct formations simultaneously."

**2. Self-referentiality extended.** The $K$-field architecture maintains the operator triad (self-completion, self-contrast, self-integration) for each formation, while adding inter-formation operators that are themselves derived from the cohesion fields:

- Each $\mathrm{Cl}^k_t$ completes $u^k_t$ using its own relational structure (self-completion).
- Each $\mathbf{D}^k_t$ compares $u^k_t$ against its complement, which now correctly decomposes into other-formation and true-exterior contributions (self-contrast, refined).
- Each $\mathbf{C}^k_t$ integrates $u^k_t$'s global structure (self-integration).
- Inter-formation repulsion derives from the simplex constraint and the energy, not from external structure.

**3. Interaction is constitutive.** The joint energy $\mathcal{E}(u^1, \ldots, u^K)$ with cross-terms makes formation interaction a first-class part of the theory. Formations compete for sites, negotiate boundaries, and can merge or split — all governed by the energy principle, not by post-hoc rules.

**4. Computational tractability.** The state space is $nK$-dimensional with the simplex constraint. For moderate $K$ (say $K \leq 20$) and moderate $n$ (say $n \leq 10^4$), this is within reach of modern optimization. The $K!$ label symmetry is a nuisance but is handled by standard techniques (canonical ordering by mass, deterministic initialization).

**5. $K$-selection via formation death.** Start with $K_{\max}$ formations and allow the energy to annihilate unnecessary ones (drive them to $u^k \equiv 0$). The volume constraint generalizes: $\sum_k m^{(k)} = M$ (total cohesive budget), with individual $m^{(k)}$ free to vary. A formation with $m^{(k)} \to 0$ has effectively died. This addresses CN6 ($K$ must be emergent): $K_{\max}$ is a capacity bound, not a commitment; the actual number of formations is determined by the energy landscape. A sparsity-inducing penalty on the number of active formations (analogous to $\ell_1$ regularization) can further encourage parsimony.

**Why not the others:**
- Option A (peeling) violates ontological priority by importing order and crisp masking.
- Option C (spectral) contradicts FC12 and provides no dynamics.
- Option D (localization) cannot model interaction or overlap.

### Commitment Notes for Multi-Formation

**CN15: Multi-formation is K-field.** The canonical multi-formation extension uses $K$ coupled soft cohesion fields with a simplex participation constraint.

**CN16: Simplex, not partition.** The constraint $\sum_k u^k(x) \leq 1$ is an inequality, not an equality. Sites may be partially or fully exterior to all formations. The theory does not require that every site be claimed.

**CN17: $K_{\max}$ is capacity, not commitment.** The actual number of active formations is determined by the energy landscape, not fixed a priori. Formations may be born (split from existing formations) or die (driven to zero mass).

---

## Part 3: Formalization of K-Field Theory

### 3.1. Extended Formal Universe

The multi-formation formal universe is:

$$\mathfrak{C}^{\mathrm{multi}} = \Big( T,\ \{X_t\},\ \{u^1_t, \ldots, u^K_t\},\ \{\mathrm{Cl}^k_t\},\ \{\mathbf{N}_t, \mathbf{C}^k_t, \mathbf{D}^k_t\},\ \{\mathbf{M}^k_{t \to s}\} \Big)$$

where:
- Each $u^k_t : X_t \to [0,1]$ is a soft cohesion field for formation $k$.
- The **simplex constraint** holds: $\sum_{k=1}^K u^k_t(x) \leq 1$ for all $x \in X_t$.
- Each formation $k$ has its own closure operator $\mathrm{Cl}^k_t$, co-belonging $\mathbf{C}^k_t$, distinction $\mathbf{D}^k_t$, and transport kernel $\mathbf{M}^k_{t \to s}$.
- The adjacency $\mathbf{N}_t$ is shared — it is a property of the relational support space, not of any particular formation.

### 3.2. Formation-Specific Operators

**Closure.** Each formation's closure operates on its own field but is influenced by the presence of others through modified aggregation:

$$\mathrm{Cl}^k_t(u^k)(x) = \sigma\Big( a_{\mathrm{cl}} \big( (1-\eta) u^k(x) + \eta (P^k_t u^k)(x) - \tau \big) \Big)$$

where $P^k_t$ is the aggregation operator restricted to formation $k$'s own relational support. Critically, the aggregation weights may be modulated by the presence of other formations:

$$(P^k_t f)(x) = \frac{\sum_y K_t(x,y) \cdot \omega^k_t(y) \cdot f(y)}{\sum_y K_t(x,y) \cdot \omega^k_t(y) + \varepsilon}$$

where $\omega^k_t(y) = 1 - \sum_{j \neq k} u^j_t(y)$ is the *available capacity* at site $y$ for formation $k$. Sites heavily occupied by other formations contribute less to formation $k$'s aggregation. This is a soft, graded form of mutual exclusion at the operator level.

**Distinction.** Formation $k$'s exterior is everything not belonging to formation $k$:

$$\mathbf{D}^k_t(x; e^k_t) \quad \text{where} \quad e^k_t(x) = 1 - u^k_t(x)$$

This can optionally be decomposed:

$$e^k_t(x) = \underbrace{\sum_{j \neq k} u^j_t(x)}_{\text{other-formation}} + \underbrace{1 - \sum_j u^j_t(x)}_{\text{true exterior}}$$

The distinction operator sees both contributions, which is correct: a formation should be distinguished from both other formations and from the background.

**Co-belonging.** Each formation has its own co-belonging structure:

$$\mathbf{C}^k_t = (I - \alpha W^k_{\mathrm{sym}})^{-1}$$

where $W^k_{\mathrm{sym}}$ is the symmetrized adjacency weighted by $u^k_t$ alone.

### 3.3. Multi-Formation Energy

The joint energy decomposes into intra-formation terms and inter-formation interaction:

$$\mathcal{E}(u^1, \ldots, u^K) = \sum_{k=1}^K \mathcal{E}_{\mathrm{self}}(u^k) + \sum_{j < k} \mathcal{E}_{\mathrm{inter}}(u^j, u^k)$$

where the self-energy is the standard single-formation energy:

$$\mathcal{E}_{\mathrm{self}}(u^k) = \lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}(u^k) + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}(u^k) + \lambda_{\mathrm{bd}} \mathcal{E}_{\mathrm{bd}}(u^k) + \lambda_{\mathrm{tr}} \mathcal{E}_{\mathrm{tr}}(u^k)$$

and the interaction energy is:

$$\mathcal{E}_{\mathrm{inter}}(u^j, u^k) = \lambda_{\mathrm{rep}} \sum_{x \in X_t} u^j_t(x) \cdot u^k_t(x) + \lambda_{\mathrm{bdy}} \sum_{x,y} \mathbf{N}_t(x,y) \cdot u^j_t(x) \cdot u^k_t(y)$$

The interaction has two components:

1. **Pointwise repulsion** ($\lambda_{\mathrm{rep}}$ term): Penalizes overlap at the same site. Two formations claiming the same site incurs an energy cost proportional to the product of their participation degrees. This is soft mutual exclusion — not a hard constraint, but an energetic preference for disjointness.

2. **Boundary repulsion** ($\lambda_{\mathrm{bdy}}$ term): Penalizes adjacency of two formations across the relational structure. If formation $j$ has high cohesion at site $x$ and formation $k$ has high cohesion at adjacent site $y$, this incurs a cost. This drives formations to maintain separation in the relational topology, not just at individual sites.

### 3.4. Constraint Manifold

The optimization domain is:

$$\Sigma^K_M = \Big\{ (u^1, \ldots, u^K) \in [0,1]^{nK} : \sum_k u^k(x) \leq 1\ \forall x,\ \sum_k \sum_x u^k(x) = M \Big\}$$

where $M$ is the total cohesive budget. The set $\Sigma^K_M$ is compact (closed and bounded in $\mathbb{R}^{nK}$) and convex (intersection of half-planes and a hyperplane).

### 3.5. Existence Theorem (Sketch)

**Theorem (Multi-Formation Minimizer Existence).** On $\Sigma^K_M$, the energy $\mathcal{E}(u^1, \ldots, u^K)$ attains its minimum.

*Proof sketch:* $\Sigma^K_M$ is compact (closed subset of $[0,1]^{nK}$, the total mass constraint is a closed condition, and the simplex inequality is a closed condition). The energy $\mathcal{E}$ is continuous on $\Sigma^K_M$ (each term is a continuous function of the fields, by composition of continuous operators). By the extreme value theorem, a continuous function on a compact set attains its minimum. $\square$

This is the direct generalization of T1. The proof is essentially identical — compactness of $\Sigma^K_M$ does the work.

### 3.6. Non-Trivial Multi-Formation Existence (Phase Transition)

**Theorem (Multi-Formation Phase Transition, sketch).** Under the same conditions as T8-Core, if $M$ is sufficiently large (roughly $M > m^*$ where $m^*$ is the minimum mass for a single non-trivial formation), and the repulsion parameter $\lambda_{\mathrm{rep}}$ is sufficiently large, then the global energy minimizer on $\Sigma^K_M$ has at least two active formations (formations $j, k$ with $\sum_x u^j(x) > 0$ and $\sum_x u^k(x) > 0$).

*Argument:* Consider a configuration with all mass in one formation: $u^1 = u^*$ (the single-formation minimizer with mass $M$), $u^k = 0$ for $k > 1$. If $M$ is large enough that the single formation has mass exceeding $2m^*$, we can consider splitting: $u^1 = v^1$, $u^2 = v^2$ with $v^1$ and $v^2$ supported on complementary regions, each with mass $\geq m^*$. The self-energy of the split configuration may be higher (each formation is smaller and less optimally shaped), but the repulsion energy vanishes (disjoint supports). For sufficiently large $\lambda_{\mathrm{rep}}$ (or sufficiently large $M$ creating significant overlap pressure), the repulsion savings dominate the self-energy cost, making the split configuration energetically favorable.

A full proof requires quantitative control on the self-energy increase vs. repulsion savings, which depends on the geometry of $X_t$ and the parameters. This is an open problem meriting rigorous treatment.

---

## Part 4: K=2 Theory

### 4.1. Explicit Energy for Two Formations

For $K = 2$, the state is $(u, v) : X_t \to [0,1]^2$ with $u(x) + v(x) \leq 1$ for all $x$. The energy is:

$$\mathcal{E}(u, v) = \mathcal{E}_{\mathrm{self}}(u) + \mathcal{E}_{\mathrm{self}}(v) + \mathcal{E}_{\mathrm{inter}}(u, v)$$

Expanding the interaction:

$$\mathcal{E}_{\mathrm{inter}}(u, v) = \lambda_{\mathrm{rep}} \sum_x u(x) v(x) + \lambda_{\mathrm{bdy}} \sum_{x,y} N(x,y)\, u(x)\, v(y)$$

The total energy for $K=2$ is therefore:

$$\mathcal{E}(u,v) = \lambda_{\mathrm{cl}} \big[\mathcal{E}_{\mathrm{cl}}(u) + \mathcal{E}_{\mathrm{cl}}(v)\big] + \lambda_{\mathrm{sep}} \big[\mathcal{E}_{\mathrm{sep}}(u) + \mathcal{E}_{\mathrm{sep}}(v)\big] + \lambda_{\mathrm{bd}} \big[\mathcal{E}_{\mathrm{bd}}(u) + \mathcal{E}_{\mathrm{bd}}(v)\big] + \lambda_{\mathrm{rep}} \sum_x u(x) v(x) + \lambda_{\mathrm{bdy}} \sum_{x,y} N(x,y)\, u(x)\, v(y)$$

(Transport terms omitted for the within-time analysis.)

### 4.2. Gradient Structure

The gradient with respect to $u$ is:

$$\frac{\partial \mathcal{E}}{\partial u(x)} = \lambda_{\mathrm{cl}} \frac{\partial \mathcal{E}_{\mathrm{cl}}}{\partial u(x)} + \lambda_{\mathrm{sep}} \frac{\partial \mathcal{E}_{\mathrm{sep}}}{\partial u(x)} + \lambda_{\mathrm{bd}} \frac{\partial \mathcal{E}_{\mathrm{bd}}}{\partial u(x)} + \lambda_{\mathrm{rep}}\, v(x) + \lambda_{\mathrm{bdy}} \sum_y N(x,y)\, v(y)$$

The first three terms are exactly the single-formation gradient (already implemented in the code, `scc/energy.py`). The last two terms are the **repulsive contribution from formation $v$**:

- $\lambda_{\mathrm{rep}} v(x)$: pointwise repulsion. Where $v$ is high, $u$ is pushed down.
- $\lambda_{\mathrm{bdy}} \sum_y N(x,y) v(y)$: neighborhood repulsion. Where $v$'s neighbors are high, $u$ is pushed down. This is exactly $\lambda_{\mathrm{bdy}} (P_t v)(x) \cdot d_x$, a smoothed version of $v$'s presence.

The gradient with respect to $v$ is symmetric (swap $u \leftrightarrow v$).

The Hessian cross-term is:

$$\frac{\partial^2 \mathcal{E}}{\partial u(x) \partial v(y)} = \lambda_{\mathrm{rep}} \delta_{xy} + \lambda_{\mathrm{bdy}} N(x,y)$$

This is a positive matrix (since $\lambda_{\mathrm{rep}}, \lambda_{\mathrm{bdy}} > 0$ and $N \geq 0$), confirming that the interaction is **repulsive**: increasing $v$ at any site increases the energy gradient pushing $u$ down.

### 4.3. Merge vs. Remain Distinct

Two formations remain distinct when the repulsive interaction energy exceeds the self-energy benefit of merging. Define:

- $\mathcal{E}_{\mathrm{split}} = \mathcal{E}_{\mathrm{self}}(u^*) + \mathcal{E}_{\mathrm{self}}(v^*) + \mathcal{E}_{\mathrm{inter}}(u^*, v^*)$ where $u^*, v^*$ are the optimal split.
- $\mathcal{E}_{\mathrm{merge}} = \mathcal{E}_{\mathrm{self}}(w^*)$ where $w^*$ is the optimal single formation with mass $m_u + m_v$, with $\mathcal{E}_{\mathrm{inter}} = 0$ (only one field).

**The merge-split criterion:** Two formations remain distinct iff $\mathcal{E}_{\mathrm{split}} < \mathcal{E}_{\mathrm{merge}}$.

Key observations:

1. **Sufficiently separated formations always remain distinct.** If $u$ and $v$ have disjoint supports separated by distance $d$ in the graph, then $\mathcal{E}_{\mathrm{inter}}(u, v) = 0$ (both repulsion terms vanish). The self-energy of two well-separated formations is approximately equal to the self-energy of one formation at each location. But a single merged formation spanning both locations would have a much larger boundary energy (the connecting region between the two locations contributes to $\mathcal{E}_{\mathrm{bd}}$). So $\mathcal{E}_{\mathrm{split}} < \mathcal{E}_{\mathrm{merge}}$.

2. **Overlapping formations may merge.** If $u$ and $v$ have significant overlap, $\mathcal{E}_{\mathrm{inter}}$ is large. But a single merged formation at the same location has zero interaction cost and may have lower self-energy (one coherent formation vs. two competing ones). Whether merging wins depends on $\lambda_{\mathrm{rep}}$ relative to the self-energy difference.

3. **Critical separation distance.** There exists a critical distance $d^*$ such that formations separated by $d > d^*$ remain distinct, while formations separated by $d < d^*$ merge. This distance depends on the parameters ($\lambda_{\mathrm{rep}}, \lambda_{\mathrm{bd}}, \beta$) and the graph structure. Deriving $d^*$ quantitatively is an open problem.

### 4.4. The Repulsive Interaction Term — Ontological Justification

The repulsion between formations is not an ad hoc regularizer. It has a clear ontological interpretation within the theory:

**Cohesive exclusion.** A site's capacity for cohesive participation is finite (bounded by 1). If site $x$ participates strongly in formation $u$, its capacity to participate in formation $v$ is diminished. The simplex constraint $u(x) + v(x) \leq 1$ enforces this at the constraint level; the repulsive energy term enforces it at the variational level, creating a smooth gradient rather than a hard boundary.

**Distinction coherence.** A formation's distinction depends on contrast with its exterior. If two formations overlap, each formation's distinction is reduced — the "exterior" contains another formation's cohesion, which looks like interior from the exterior operator's perspective. The repulsive term penalizes this configuration, driving formations toward states where their distinction operators are coherent.

---

## Part 5: Connection to Existing Theory

### 5.1. Proto-Cohesion for K Formations

Each formation $k$ has its own diagnostic vector:

$$\mathbf{d}^k = \Big(\mathsf{Bind}^k_t,\ \mathsf{Sep}^k_t,\ \mathsf{Inside}^k_t,\ \mathsf{Persist}^k_W\Big) \in [0,1]^4$$

where:

- $\mathsf{Bind}^k_t = 1 - \|u^k_t - \mathrm{Cl}^k_t(u^k_t)\|_2 / \sqrt{n}$
- $\mathsf{Sep}^k_t = \sum_x \mathbf{C}^k_t(x,x) \mathbf{D}^k_t(x; 1-u^k_t) / \sum_x \mathbf{C}^k_t(x,x)$
- $\mathsf{Inside}^k_t = \mathcal{Q}_{\mathrm{morph}}(u^k_t)$
- $\mathsf{Persist}^k_W$ uses formation-specific transport $\mathbf{M}^k_{t \to s}$

The **scene diagnostic** is the collection $\{\mathbf{d}^1, \ldots, \mathbf{d}^K\}$ together with a scene-level summary:

$$\mathbf{d}_{\mathrm{scene}} = \Big(\min_k \mathsf{Bind}^k,\ \min_k \mathsf{Sep}^k,\ \min_k \mathsf{Inside}^k,\ \min_k \mathsf{Persist}^k\Big)$$

which represents the "weakest link" — the diagnostic quality of the worst formation.

### 5.2. Diagnostic Vector Generalization

The per-formation diagnostic vector is unchanged in form — it is still $[0,1]^4$. What changes is the operator context:

- $\mathrm{Cl}^k_t$ uses formation-specific aggregation (modulated by other formations' presence).
- $\mathbf{D}^k_t$ computes against $1 - u^k_t$, which includes other formations.
- $\mathbf{C}^k_t$ integrates formation $k$'s own structure.

This means the diagnostic vector naturally adapts to the multi-formation setting without redefinition. A formation in isolation and a formation in a crowded scene are assessed by the same predicates — the difference is in the operator values, not the predicate structure.

### 5.3. Temporal Transport for K Formations

Each formation has its own transport kernel $\mathbf{M}^k_{t \to s}$. The key challenge is **formation correspondence**: which formation at time $t$ corresponds to which formation at time $s$?

**Approach: Transport-derived correspondence.** Rather than imposing correspondence externally, derive it from the transport cost. Define the formation-level transport cost:

$$C_{jk} = \min_{\pi \in \Pi(u^j_t, u^k_s)} \sum_{x,y} \pi(x,y) \cdot c(x,y; u^j_t, u^k_s)$$

where $\Pi(u^j_t, u^k_s)$ is the set of transport plans between $u^j_t$ and $u^k_s$. The optimal assignment $\sigma^* = \arg\min_\sigma \sum_k C_{k,\sigma(k)}$ gives the correspondence.

This preserves the theory's self-referential character: correspondence is derived from the cohesion fields themselves, not imposed externally. Formation splitting (one formation at time $t$ corresponding to two at time $s$) and merging (two at $t$ corresponding to one at $s$) are handled by allowing fractional assignment.

**Persistence in the multi-formation setting:**

$$\mathsf{Persist}^k_W = \min_{t < s \in W} \max_{j} \frac{\sum_{x \in \mathrm{Core}^k_t} \sum_{y \in \mathrm{Core}^j_s} \mathbf{M}^{k \to j}_{t \to s}(x,y) \cdot u^j_s(y)}{\rho_{\mathrm{persist}}}$$

The $\max_j$ finds the best-matching formation at time $s$, allowing for relabeling.

### 5.4. Recovery of Single-Formation Theory

When $K = 1$, the multi-formation theory reduces exactly to the existing theory:

- The simplex constraint $u^1(x) \leq 1$ is automatically satisfied (since $u^1 \in [0,1]$).
- The interaction energy vanishes (no second formation).
- All operators reduce to their single-formation forms ($\omega^1_t(y) = 1$ since there are no other formations).
- The diagnostic vector is unchanged.

This is a necessary consistency check: the multi-formation theory is a proper extension, not a replacement.

### 5.5. Compatibility with Existing Results

All proved results (T1, T6a/b, T8-Core, T14, etc.) remain valid for each individual formation, with the caveat that the operator context includes other formations' influence. Specifically:

- **T1 generalizes** to multi-formation minimizer existence on $\Sigma^K_M$ (proved above in §3.5).
- **T6a/b** (closure fixed point existence/uniqueness) applies to each $\mathrm{Cl}^k_t$ individually, since the contraction property depends only on the sigmoid parameters, not on the multi-formation context.
- **T8-Core** (phase transition) requires re-examination for the joint energy. The Hessian at the uniform state now includes cross-formation terms. This is an open problem.
- **T14** (gradient flow convergence via Łojasiewicz) extends if the multi-formation energy remains analytic, which it does (the interaction terms $u^j(x) u^k(x)$ and $N(x,y) u^j(x) u^k(y)$ are polynomial, hence analytic).

---

## Part 6: Open Problems Introduced

The $K$-field architecture resolves V6 but introduces new open problems:

### OP-MF1. Quantitative Merge-Split Criterion
Derive the critical separation distance $d^*$ and the critical repulsion strength $\lambda^*_{\mathrm{rep}}$ as functions of the graph structure and energy parameters.

### OP-MF2. Multi-Formation Phase Transition (Rigorous)
Prove the multi-formation phase transition theorem rigorously: under what conditions does the global minimizer on $\Sigma^K_M$ have exactly $K^* > 1$ active formations? Relate $K^*$ to $M$, $\lambda_{\mathrm{rep}}$, and the graph geometry.

### OP-MF3. Formation Birth and Death Dynamics
In the gradient flow of the multi-formation energy, characterize formation birth (a new formation nucleating from the background) and formation death (a formation's mass converging to zero). What are the critical points where the number of active formations changes?

### OP-MF4. Label Symmetry Breaking
The $K!$ permutation symmetry of the labels $\{1, \ldots, K\}$ creates equivalent minima. Develop a canonical ordering (by mass, by center of mass, by energy) to break this symmetry for computational purposes.

### OP-MF5. Interaction Parameter Regime
Determine the natural scale of $\lambda_{\mathrm{rep}}$ and $\lambda_{\mathrm{bdy}}$ relative to the self-energy parameters. Should they be set by Hessian normalization (as with $\lambda_{\mathrm{sep}}/\lambda_{\mathrm{bd}}$)? Is there a principled derivation from the simplex constraint?

### OP-MF6. Spectral Diagnostic
Can the spectral structure of $\mathbf{C}_t$ (computed from the joint field $\bar{u} = \max_k u^k$, or from individual $u^k$ fields) serve as a diagnostic for whether the $K$-field decomposition is coherent? This would give Option C a role as a diagnostic within Option B's architecture.

---

## Part 7: Summary of Deliverables

| Item | Status |
|------|--------|
| Four options evaluated | Complete |
| Architecture decision (K-field) | **Binding** |
| Extended formal universe | Specified |
| Formation-specific operators | Defined |
| Multi-formation energy with interaction | Formalized |
| Existence theorem | Proved (sketch) |
| K=2 explicit energy | Derived |
| K=2 gradient structure | Derived |
| Merge-split criterion | Qualitative (quantitative is open) |
| Proto-cohesion for K formations | Defined |
| Temporal transport for K formations | Sketched |
| Single-formation recovery | Verified |
| New open problems | 6 identified |
| New commitment notes | 3 (CN15–CN17) |

---

## Part 8: Impact Assessment

**V6 status: Resolved architecturally.** The $K$-field theory provides a principled, self-referential, variationally grounded multi-formation extension. The architecture is decided; the formalization is complete at the specification level. Quantitative results (phase transition, merge-split bounds) remain open.

**Score impact:** Multi-formation theory: 0/10 → 7/10 (architecture + formalization; quantitative results needed for 9+).

**Downstream effects:**
- The distinction operator's incoherence (V6's secondary symptom) is resolved by formation-specific distinction.
- The contraction uniqueness (V6's primary cause) is circumvented — each formation has its own closure operator with a unique fixed point, but there are $K$ such operators, yielding multiple formations from multiple closure landscapes.
- CN6 ("$K$ must be emergent") is addressed by the formation death mechanism.
- FC12 ($\mathbf{C}_t$ diagnostic-only) is preserved — multi-formation structure comes from the energy, not from $\mathbf{C}_t$ spectral analysis.
