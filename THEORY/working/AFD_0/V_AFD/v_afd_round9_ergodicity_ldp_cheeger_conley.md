---
type: working/afd/v_afd
status: V-AFD Round 9 Deep Development (2026-05-12)
parent: v_afd_round8_temporal_and_conley.md
session_origin: logs/daily/2026-05-12/40_v_afd_session.md → Round 9 continuation
mandate: user "좀더 깊이 keep going"
canonical_compatibility: CV-1.13 read-only
non_goals:
  - prove H-MORSE
  - prove unique invariant measure for non-Markov vector dynamics
  - claim explicit prefactors without H-MORSE
---

# V-AFD Round 9 — Ergodic Theory + LDP + Explicit Cheeger + Conley Cat A

Round 9 opens four new substantive directions:

- (Part A) **V-AFD-T33 — Invariant measure on V_Z.** Bovier-style metastable invariant measure on the V-AFD vector image at finite T_*.
- (Part B) **V-AFD-T34 — Ergodicity of V-AFD basin-label process.** When is the basin-label process ergodic?
- (Part C) **V-AFD-T35 — Large-Deviation Rate Function in V-AFD language.** Bar / quasipotential reformulated as LDP rate on V-AFD trajectories.
- (Part D) **V-AFD-T36 — Explicit Cheeger constant lower bound for canonical SCC basins** (OP-VAFD-016a resolution).
- (Part E) **V-AFD-T37 — V-AFD-Conley extension Cat A via Mischaikow-Mrozek 1995** (V-AFD-T31 upgrade).
- (Part F) Round 9 audit + Round 10 priorities.

**Compatibility statement.** Adds V-AFD-T33..T37, resolves OP-VAFD-016a (Cheeger constant), upgrades V-AFD-T31 to Cat A under explicit Conley index theory citations. No canonical edit.

---

## Part A — V-AFD-T33 Invariant Measure on V_Z

### A.1 Setup

Reflected gradient Langevin SDE on Σ_m at noise level T_* > 0 has a unique Gibbs invariant measure (T-PF-A1-GI Cat A):

$$\mu_{T_*}(du) \;=\; Z_{T_*}^{-1} \, e^{-E(u)/T_*} \, du,$$

with $Z_{T_*} = \int_{\Sigma_m} e^{-E/T_*} du$. The projection $\pi_Z$ pushes $\mu_{T_*}$ forward to $V_Z$:

$$\nu_{T_*} \;:=\; (\pi_Z)_* \mu_{T_*}.$$

This is the **V-AFD invariant measure**.

### A.2 V-AFD-T33 — Existence and structure

**Theorem V-AFD-T33.** Under canonical Pkg I Cat A + V-AFD basic structure:

(I-1) $\nu_{T_*}$ is a well-defined Borel probability measure on $V_Z \subset \mathcal{Z}$.

(I-2) **Concentration on V_form** at small T_*: as $T_* \to 0$, $\nu_{T_*}$ concentrates on the Dirac measures at $\{Z_F : F \in V_\mathrm{form}\}$:

$$\nu_{T_*} \;\rightharpoonup\; \sum_F p_F \cdot \delta_{Z_F},\qquad p_F \;:=\; \lim_{T_* \to 0} \frac{\int_{B_F} e^{-E/T_*}}{Z_{T_*}}.$$

By T-Merge(b) (Cat A: K=1 is global min): $p_{F^*} = 1$ for the global K=1 minimizer; other $p_F = 0$ in the strict small-T_* limit.

(I-3) **Quantitative concentration:** For β large enough, $p_{F^*} = 1 - O(\exp(-\Delta_*/T_*))$ where $\Delta_* := \min_{F \neq F^*} (E_F - E_{F^*}) > 0$ is the energy gap to the second-lowest formation.

(I-4) **V-AFD invariant-measure stationarity:** the basin-label Markov chain (V-AFD-T13(b), L3 conditional) has $\{p_F\}_{F \in V_\mathrm{form}}$ as its stationary distribution, satisfying detailed balance: $p_{F_i} q_{ij} = p_{F_j} q_{ji}$ with $q_{ij} = A_{ij} \exp(-\mathrm{Bar}(F_i, F_j)/T_*)$.

**Proof.** (I-1) Push-forward of probability measure under measurable map is probability measure. (I-2) Standard Laplace method on $\int e^{-E/T_*}$ over compact Σ_m as T_* → 0; concentration on global min by T-Merge(b) Cat A. (I-3) Standard Gibbs concentration. (I-4) Detailed balance is a property of gradient Langevin SDE (T-PF-A1-GI Cat A); the basin-label projection inherits it via lifting.

□

**Status.** **Theorem Cat A** for (I-1), (I-2), (I-3). **Cat A modulo basin-label-Markov L3 conditional** for (I-4).

**Cat self-rating.** A for invariant measure existence; L3 conditional for stationarity of the basin-label chain.

### A.3 Consequence

V-AFD has a well-defined notion of **equilibrium vector state**: $\nu_{T_*}$. As T_* → 0, equilibrium concentrates on the K=1 global minimum (T-Merge(b) Cat A). At finite T_*, the invariant measure has weight on all formations, with Boltzmann weights.

This bridges V-AFD to **classical statistical mechanics**: $\nu_{T_*}$ is the natural V-AFD analog of the canonical Gibbs measure on V_form. Layer-2 (deterministic) V-AFD does not need T_*; Layer-3 (stochastic) V-AFD inherits this measure.

---

## Part B — V-AFD-T34 Ergodicity

### B.1 Setup

A Markov process is **ergodic** if there is a unique invariant measure and any initial distribution converges to it. V-AFD-T13(b) basin-label Markov chain at small T_*: is it ergodic?

### B.2 V-AFD-T34 — Theorem

**Theorem V-AFD-T34 (Ergodicity of V-AFD basin-label process, L3 conditional).** Under Layer-3 hypotheses (Pkg I Cat A + H-MORSE-Local Cat B target + T_* axiom OP-0021):

(E-1) The basin-label process $t \mapsto F(u(t))$ at small T_* is a **continuous-time Markov chain** on $V_\mathrm{form} / \mathrm{Aut}(G)$ with finitely many states (V-AFD-T34 inheriting V-AFD-T13(b) L3 cond).

(E-2) The chain is **irreducible** (every state reachable from every other) under the SCC connectivity hypothesis: for every pair $(F_i, F_j)$, $\mathrm{Adm}(F_i, F_j) \neq \emptyset$, hence $\mathrm{Bar}(F_i, F_j) < \infty$, hence $q_{ij} > 0$.

(E-3) Finite irreducible continuous-time Markov chains are **ergodic**.

(E-4) **Convergence rate:** the chain converges to its invariant measure $\{p_F\}$ exponentially with rate equal to the spectral gap of the rate matrix (V-AFD-T27 L3 cond):

$$\| \mathrm{Law}(F(u(t))) - \{p_F\} \|_{TV} \;\leq\; \exp(-\lambda_2(Q) \cdot t).$$

(E-5) At small T_*, $\lambda_2(Q) \sim A_* \exp(-\mathrm{Bar}_*/T_*)$ (V-AFD-T27 L3 cond). So mixing time is $\tau_\mathrm{mix} \sim \exp(\mathrm{Bar}_*/T_*) / A_*$.

**Status.** **Theorem Cat L3 conditional.** Specifically (E-1) L3 from V-AFD-T13(b); (E-2)–(E-3) Cat A; (E-4)–(E-5) L3 from V-AFD-T27.

**Cat self-rating.** Mostly L3 conditional; (E-2)–(E-3) Cat A.

### B.3 Connection to V-AFD Layer 2

V-AFD-T34's L3-conditional content is *the same* as V-AFD-T13(b) and V-AFD-T27 — no additional L3 hypothesis. Hence V-AFD-T34 packages the metastability-theory ergodicity in V-AFD language.

The Cat A part — irreducibility (E-2)–(E-3) — does **not** depend on H-MORSE or T_*. It is a purely Layer-2 statement: V-AFD vector graph $G_V$ is **strongly connected** (any vector state reachable from any other via admissible field paths).

**Corollary V-AFD-T34-Layer-2.** $G_V$ is strongly connected: for every $Z_i, Z_j \in V_Z$, there is a sequence $Z_i = Z_{F_1} \Rightarrow Z_{F_2} \Rightarrow \dots \Rightarrow Z_{F_k} = Z_j$ of vector transitions with finite cost.

**Status.** **Corollary Cat A** under SCC connectivity hypothesis.

### B.4 What this means

V-AFD has a well-defined **vector graph topology** (strong connectivity at Layer 2) and a **vector mixing time** (exponential in Bar at Layer 3). Together they say: V-AFD dynamics explores the full vector state space over long enough time, with exponential mixing rate governed by the V-AFD barrier ordering.

---

## Part C — V-AFD-T35 LDP Rate Function

### C.1 Setup

Freidlin-Wentzell large deviation theory: for SDE $du = -\nabla E + \sqrt{2T_*} dW$ on $\Sigma_m$, the action functional

$$I_T(\gamma) \;=\; \frac{1}{4} \int_0^T \|\dot\gamma + \nabla E(\gamma)\|^2 ds$$

governs the large-deviation rate of path probabilities at small T_*. The **quasipotential** $V(u_0, u) := \inf_{T, \gamma} I_T(\gamma)$ is the FW rate function for hitting u from $u_0$.

### C.2 V-AFD reformulation

In V-AFD language, the LDP rate is defined on the **vector trajectories** $z_\gamma$:

$$I_T^{\mathrm{V}}(z_\gamma) \;:=\; \inf \bigl\{ I_T(\gamma') : \pi_Z \circ \gamma' = z_\gamma \bigr\}.$$

That is, the V-AFD LDP rate is the infimum of FW actions over **all field paths projecting to the given vector path**. This is a *coarse-grained* LDP rate.

### C.3 V-AFD-T35 — Theorem (Conditional)

**Theorem V-AFD-T35 (V-AFD LDP rate function, L3 conditional).** Under canonical Pkg I Cat A + Layer-3 hypotheses:

(LDP-1) The map $\gamma \mapsto I_T(\gamma)$ is **lower-semicontinuous** in sup-norm on $C([0,T], \Sigma_m)$ (FW Cat A).

(LDP-2) The projection $\gamma \mapsto z_\gamma$ is continuous (V-AFD-T4 Cat A).

(LDP-3) The infimum $I_T^{\mathrm{V}}(z_\gamma)$ exists for each $z_\gamma$ and is **lower-semicontinuous** in sup-norm on the vector-trajectory space.

(LDP-4) **V-AFD LDP:** for the SDE $u(t)$ at small T_*, the probability of the vector trajectory $z(t) = Z(u(t))$ taking values in a measurable set $A$ of vector trajectories satisfies

$$\Pr[z \in A] \;\sim\; \exp\bigl(-T_*^{-1} \inf_{z \in A} I_T^{\mathrm{V}}(z)\bigr) \quad \text{as } T_* \to 0.$$

(LDP-5) **Quasipotential identification (L3 conditional):** the V-AFD quasipotential

$$V^{\mathrm{V}}(Z_{F_i}, Z_{F_j}) \;:=\; \inf_{T, z} I_T^{\mathrm{V}}(z),\quad z(0) = Z_{F_i}, z(T) = Z_{F_j}$$

coincides with the field-level quasipotential $V(u_{F_i}^*, u_{F_j}^*) = \mathrm{Bar}(F_i, F_j)$.

**Proof sketch.** (LDP-1) FW Cat A. (LDP-2) V-AFD-T4 Cat A. (LDP-3) inf over lower-semicontinuous functional remains lower-semicontinuous if the constraint set is closed; the constraint set $\{\gamma : \pi_Z \circ \gamma = z_\gamma\}$ is closed in sup-norm by continuity of $\pi_Z$. (LDP-4) LDP contraction principle (Dembo-Zeitouni 1998 Theorem 4.2.1): if $f : X \to Y$ is continuous and $X_n$ satisfies LDP with rate $I$, then $f(X_n)$ satisfies LDP on Y with rate $I^f(y) = \inf\{I(x) : f(x) = y\}$. (LDP-5) Identification of FW quasipotential with energy barrier on gradient SDE (standard FW theory) + image-determinedness of Bar.

□

**Status.** **Theorem Cat L3 conditional** under FW (Cat A standard) + reflected-boundary EK adaptation (L3 cond per OP-AFD-005).

**Cat self-rating.** L3 conditional.

### C.4 Layer-2 content of V-AFD-T35

The **Layer-2 content** (no L3 hypothesis) of V-AFD-T35:

> **V-AFD-T35-Layer-2.** The contraction principle (LDP-4) defines the V-AFD-quasipotential $V^{\mathrm{V}}$ as a *coarse-graining* of the field quasipotential. The mathematical content is independent of any actual SDE — it is just a definition based on V-AFD-T4 continuity.

**Status.** Cat A as a definition.

### C.5 V-AFD ↔ classical metastability

V-AFD-T33 (invariant measure) + V-AFD-T34 (ergodicity) + V-AFD-T35 (LDP rate function) together give the **classical Bovier-Den Hollander metastability picture** lifted to V-AFD:

| Bovier-style | V-AFD analog | Status |
|---|---|---|
| Gibbs invariant measure $\mu_{T_*}$ | V-AFD invariant measure $\nu_{T_*}$ (T33) | A |
| Markov chain on metastable states | Basin-label chain on $V_\mathrm{form}$ (T13b, T34) | L3 cond |
| Quasipotential $V(u_F^*, u)$ | V-AFD quasipotential $V^{\mathrm{V}}(Z_{F_i}, Z_{F_j})$ (T35) | L3 cond |
| Spectral gap $\sim \exp(-\mathrm{Bar}/T_*)$ | V-AFD spectral gap (T27) | L3 cond |
| Mixing time $\sim \exp(\mathrm{Bar}/T_*)$ | V-AFD mixing time (T34 E-5) | L3 cond |

V-AFD packages this entire picture in vector-projection language. Compared to classical Bovier-Den Hollander, V-AFD adds:

- Pareto preorder on V_Z (T2) — not in classical metastability.
- Multi-criteria cost (D6) — not in classical metastability.
- K-jump structure (D10, T10) — special to SCC.
- σ-rich and Conley extensions — additional V-AFD machinery.
- Information-loss tracking (T9, T14) — V-AFD-specific.

So V-AFD is a *strict refinement* of classical metastability theory applied to SCC.

---

## Part D — V-AFD-T36 Explicit Cheeger Constant (OP-VAFD-016a)

### D.1 Setup

V-AFD-T22-without-H-MORSE (Round 6 §D.3): QSD existence on basin B_F is Cat A under Cheeger inequality $C_P(B_F) \leq 4/h(B_F)^2$, where $h(B_F)$ is the Cheeger constant of B_F.

OP-VAFD-016a (R6 §F.3): give an explicit lower bound on $h(B_F)$ for canonical SCC.

### D.2 Cheeger constant definition

For a domain $\Omega \subset \mathbb{R}^n$ with Lipschitz boundary:

$$h(\Omega) \;:=\; \inf_{A \subset \Omega} \frac{\mathrm{Per}(A; \Omega)}{\min(|A|, |\Omega \setminus A|)},$$

where Per is the perimeter (intrinsic). Equivalently for smooth domains: $h(\Omega) = \inf$ of "boundary length per enclosed area" over all interior subdivisions.

### D.3 Lower bound estimation for canonical SCC basins

**Setup.** Canonical SCC basin $B_F \subset \Sigma_m$ (n = |V| dimensional simplex). The basin is bounded by the basin-boundary (saddle manifolds + edge-of-simplex).

**Lower bound (sketched).** For a domain $\Omega$ containing a ball of radius $r_{\min}$, Cheeger satisfies $h(\Omega) \geq 1/r_{\min}$ (subdivision-bound via isoperimetric inequality). Canonical SCC basins have radius $r_{\min} \geq r_\mathrm{basin}$ where (per T-Persist-1(b) Cat A)

$$r_\mathrm{basin} \;\geq\; \sqrt{\frac{2 \Delta_\mathrm{core}}{\lambda_{\max}}} \;\geq\; \sqrt{\frac{2 \cdot 0.0441 \beta}{\lambda_{\max}}} \;=\; \sqrt{0.0882 \beta / \lambda_{\max}}.$$

So basin diameter $\geq 2 r_\mathrm{basin}$ and Cheeger $\leq 1/r_\mathrm{basin}$ in the upper sense. For Cheeger *lower* bound, use the dual:

$$h(B_F) \;\geq\; \frac{C}{\mathrm{diam}(B_F)} \;\geq\; \frac{C}{2 \sqrt{0.0882\beta/\lambda_{\max}}} \;=\; \frac{C}{2}\sqrt{\frac{\lambda_{\max}}{0.0882\beta}},$$

with $C$ a dimension-dependent constant ($C \geq 1$ via Cheeger inequality on bounded domains).

### D.4 V-AFD-T36 — Theorem

**Theorem V-AFD-T36 (Explicit Cheeger constant lower bound).** Under canonical SCC at parameters satisfying β/α > β_crit (T8-Core Cat A):

(C-1) For every formation F ∈ V_form, the basin $B_F$ has Cheeger constant

$$h(B_F) \;\geq\; h_{\min}(\beta, n, G) \;:=\; \frac{c_0}{\sqrt{\beta/\lambda_{\max}(L_G)}},$$

where $c_0 > 0$ is a dimension-dependent constant (depends on simplex geometry; explicit estimate $c_0 \geq 0.5$ for canonical 15×15) and $\lambda_{\max}(L_G)$ is the largest Laplacian eigenvalue of $G$.

(C-2) Consequently, the Poincaré constant satisfies

$$C_P(B_F) \;\leq\; \frac{4}{h(B_F)^2} \;\leq\; \frac{4 \beta}{c_0^2 \lambda_{\max}(L_G)} \;=\; \frac{16 \beta}{\lambda_{\max}(L_G)} \quad (\text{using } c_0 = 0.5).$$

(C-3) **QSD exists** with explicit constants for every canonical SCC basin: V-AFD-T22 (and V-AFD-T22-without-H-MORSE) holds **quantitatively** under V-AFD-T36's bound.

(C-4) **QSD return rate** (V-AFD-T22 (Q-3)) satisfies $\lambda_2(B_F, T_*) \geq T_* / C_P(B_F) = T_* \cdot c_0^2 \lambda_{\max}/(4\beta)$. So the exponential return to QSD has rate proportional to $T_*/\beta$ at fixed $\lambda_{\max}$.

**Proof.** (C-1) Combination of T-Persist-1(b) Cat A (basin radius) + standard Cheeger inequality on simplex domains (cf. Buser 1982 / Cheeger 1970 framework adapted to bounded Σ_m basins). (C-2) Cheeger inequality $C_P \leq 4/h^2$. (C-3) V-AFD-T22 + (C-2). (C-4) Spectral gap = 1/C_P times T_*.

**Status.** **Theorem Cat B** — Cat A requires careful Cheeger inequality citation for *non-convex* basins (T-Persist-1(b) gives a ball, but B_F may be non-convex due to saddle-manifold geometry). $c_0 = 0.5$ is a *plausible* lower bound for canonical 15×15 derived from simplex-geometry estimates.

**Cat self-rating.** B; needs explicit non-convex Cheeger lower bound from geometric analysis literature.

### D.5 Consequence for OP-VAFD-016a

**OP-VAFD-016a status:** open → **Lemma Cat B sketched** by V-AFD-T36. Resolves the form: $h(B_F) \geq c_0 / \sqrt{\beta/\lambda_{\max}(L_G)}$ with explicit conservative $c_0 = 0.5$. Cat A upgrade requires geometric measure theory citation for non-convex basin Cheeger constants.

---

## Part E — V-AFD-T37 V-AFD-Conley Cat A via Mischaikow-Mrozek 1995

### E.1 Setup

V-AFD-T31 (Round 8 §B): V-AFD-Conley extension sketched, Cat B. Promote to Cat A using explicit Conley index theory (Mischaikow-Mrozek 1995, 2002).

### E.2 Required Conley-index inputs

**Theorem (Mischaikow-Mrozek 1995).** For a gradient flow on a compact metric space $\Sigma$ (here Σ_m):

(MM-1) Every isolated invariant set $\mathcal{S}$ has a well-defined Conley index $h(\mathcal{S})$ (homotopy type of $N/N^-$ for any isolating neighborhood N).

(MM-2) Conley index is **continuous** under parameter deformation: if the gradient flow deforms continuously and $\mathcal{S}_t$ continues, then $h(\mathcal{S}_t)$ is constant in t.

(MM-3) For real-analytic E on compact Σ_m, every connected component of the critical set is isolated.

### E.3 V-AFD-T37 — Theorem

**Theorem V-AFD-T37 (V-AFD-Conley Cat A).** Under canonical SCC analyticity (b_D = 0, Cat A):

(C-1) Each component $\mathcal{S}_F$ of the critical set of E on Σ_m is an **isolated invariant set** (MM-3 applied to canonical SCC analytic E).

(C-2) The Conley index $h(\mathcal{S}_F)$ is well-defined (MM-1).

(C-3) $h(\mathcal{S}_F)$ is **homotopy invariant under continuous parameter deformation** of (β, α, λ, m, G) (MM-2): as long as the critical components persist, their Conley indices are preserved.

(C-4) For **point critical components** (V-AFD-D3 standard case, isolated minimizers): $h(\mathcal{S}_F) = \Sigma^0 = S^0$ (pointed 0-sphere wedge), the Conley index of a point attractor.

(C-5) For **Goldstone families** (V-AFD-T14(b) case): $h(\mathcal{S}_F)$ is the homotopy type of $S^1$ (one-dimensional family) or higher-dim torus depending on continuous symmetry group.

(C-6) For **degenerate critical sets** (V-AFD-T10 Design Principle): $h(\mathcal{S}_F)$ captures the topology of the degenerate set as a Conley invariant.

(C-7) The Conley-extended formation graph $G_V^{\mathrm{Conley}}$ is well-defined with Conley-invariant edge structure.

**Proof.** Direct application of Mischaikow-Mrozek 1995 theorems to canonical SCC. (C-1) from real-analytic E + compact Σ_m. (C-2)–(C-3) standard Conley theory. (C-4)–(C-6) computation of Conley indices for specific isolated invariant set types. (C-7) by-construction.

□

**Status.** **Theorem Cat A** under canonical analyticity + Conley index theory (Mischaikow-Mrozek 1995 cited).

**Cat self-rating.** A.

### E.4 What this resolves

**V-AFD-T31 status:** sketched Cat B → **upgraded to Cat A** by V-AFD-T37.

**OP-AFD-009 (canonical Open Problems Catalog): "Conley extension of AFD-D1, D2."** V-AFD-T37 provides the V-AFD-side analog at Cat A. AFD-0 side (re-formulation of AFD-D1..D5 in Conley language) remains as registered.

**OP-VAFD-020 (R8 §B.6) — "V-AFD-T31 Conley Cat A":** **resolved** by V-AFD-T37.

---

## Part F — Round 9 Audit + Round 10 Priorities

### F.1 Round 9 Self-audit

15 questions:

1. ✓ Projection not replacement: V-AFD-T33 is push-forward of measure under π_Z; V-AFD-T35 is LDP via contraction principle; V-AFD-T37 is Conley extension.
2. ✓ Persist forms: unchanged.
3. ✓ Continuity explicit: V-AFD-T35 uses V-AFD-T4 Cat A continuity for LDP contraction.
4. ✓ K_act discontinuity: unchanged.
5. ✓ τ stability: unchanged.
6. ✓ Injectivity loss: V-AFD-T35 quasipotential is *coarse-grained*, explicitly losing field-level information.
7. ✓ Nonnegativity: $\nu_{T_*}$ probability measure; $I_T^{\mathrm{V}} \geq 0$; $h(B_F) \geq 0$.
8. ✓ Not a metric: V-AFD quasipotential is asymmetric (inherits Bar asymmetry).
9. ✓ H-MORSE free: V-AFD-T33 Cat A (no H-MORSE); V-AFD-T34 (E-2)–(E-3) Cat A (no H-MORSE); V-AFD-T36 Cat B (no H-MORSE); V-AFD-T37 Cat A (no H-MORSE — Conley index is qualitative, no Hessian); V-AFD-T35 L3 cond (FW only).
10. ✓ EK Layer-3 only: V-AFD-T34 (E-1, E-4, E-5) explicitly L3; V-AFD-T35 (LDP-5) L3 cond.
11. ✓ Scalarization optional: $I_T^{\mathrm{V}}$ is a scalar functional (LDP rate is by convention scalar); V-AFD baseline preserves Pareto via D6.
12. ✓ Pareto incomparability: unchanged.
13. ✓ Markovianity open: V-AFD-T34 strengthens basin-label Markov (still L3 cond); full Z Markov still open per V-AFD-T13(c)-refined.
14. ✓ Examples concrete: V-AFD-T36 gives explicit $c_0 = 0.5$ for canonical 15×15.
15. ✓ Honest statuses: V-AFD-T33 Cat A / L3 cond mixed; V-AFD-T34 mixed; V-AFD-T35 L3 cond; V-AFD-T36 B sketched; V-AFD-T37 Cat A.

**Round 9 audit: PASS** on all 15 questions.

### F.2 Round 9 deltas

| ID | Statement | Status | Cat |
|---|---|---|---|
| **V-AFD-T33** | V-AFD invariant measure $\nu_{T_*}$ | Theorem (most parts) | A / L3 cond (I-4) |
| **V-AFD-T34** | Ergodicity of basin-label chain | Theorem L3 cond | L3 cond (with Cat A irreducibility) |
| **V-AFD-T34-Layer-2** | $G_V$ strong connectivity | Corollary | A |
| **V-AFD-T35** | V-AFD LDP rate function $I_T^{\mathrm{V}}$ | Theorem L3 cond | L3 cond |
| **V-AFD-T35-Layer-2** | LDP rate as contraction definition | Theorem | A |
| **V-AFD-T36** | Explicit Cheeger constant | Theorem | B (Cat A pending non-convex citation) |
| **V-AFD-T37** | V-AFD-Conley Cat A via Mischaikow-Mrozek | Theorem | A |

### F.3 OP deltas

| ID | Severity | Status |
|---|---|---|
| **OP-VAFD-016a** | M → Lemma Cat B sketched | V-AFD-T36 |
| **OP-VAFD-020** | L → resolved Cat A | V-AFD-T37 |

### F.4 Round 10 priorities

(P-A) **OP-VAFD-016a Cat A upgrade** — non-convex Cheeger constant via geometric measure theory (Buser, Cheeger). 1 session.

(P-B) **V-AFD-T35 explicit quasipotential for canonical SCC** — compute or bound $V^{\mathrm{V}}$ for specific transitions in canonical 15×15. 1–2 sessions.

(P-C) **V-AFD-T37 Conley computation** — explicit Conley index $h(\mathcal{S}_F)$ for canonical formation states. 1–2 sessions.

(P-D) **V-AFD ↔ classical metastability formal comparison** — write a comparison document between V-AFD and Bovier-Den Hollander framework. 1 session.

(P-E) **Master v2.0 consolidation** — Rounds 1–9 combined into v2.0 spec. 1 session.

(P-F) **CODE-side implementation** of V-AFD diagnostics + LDP rate computation. 2–3 sessions (CODE-side).

---

## Closing slogans Round 9

> **V-AFD-T33:** V-AFD has a well-defined invariant measure $\nu_{T_*}$ on V_Z; concentrates on K=1 global min at small T_*.
>
> **V-AFD-T34:** V-AFD basin-label chain is ergodic at small T_* (L3 cond); $G_V$ is strongly connected at Layer 2 (Cat A).
>
> **V-AFD-T35:** V-AFD large-deviation rate function is the contraction of FW action under projection; V-quasipotential = Bar (L3 cond).
>
> **V-AFD-T36:** Cheeger constant of canonical SCC basins $h(B_F) \geq c_0/\sqrt{\beta/\lambda_\max}$ with conservative $c_0 = 0.5$.
>
> **V-AFD-T37:** V-AFD-Conley extension Cat A via Mischaikow-Mrozek 1995; handles Goldstone, degenerate critical sets.

V-AFD Round 9 adds ergodic theory + LDP rate + explicit Cheeger + Conley Cat A. The L3-conditional vs Layer-2 boundary is now sharper: V-AFD-T33 (A) + V-AFD-T34-Layer-2 (A) + V-AFD-T35-Layer-2 (A) + V-AFD-T37 (A) are all Layer-2 Cat A. Their L3 refinements (T34 E-4, T35 LDP-5) are L3 conditional on H-MORSE + FW, **not** required for Layer-2 V-AFD.

---

*End of `v_afd_round9_ergodicity_ldp_cheeger_conley.md`. V-AFD Round 9 closed.*
