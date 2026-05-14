> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 10_new_open_problems.md — New Open Problems (NOPs) from 2026-05-07 Closures

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended evening session
**Objective:** Catalog **genuinely new open problems (NOPs)** that emerged from today's closures and advancements, distinct from the existing NQ-T-Identity-{1..6} list. For each NOP: state the problem, generate multi-tool angles (≥3 mathematically independent), propose candidate first lemma, assess priority and difficulty. Send substantive NOPs to `working/MF/` for promotion-pipeline tracking.

**Predecessors:** today's `02–09` files; `working/MF/temporal_identity_sharp_form_2026-05-07.md`.

---

## §1. Inventory of NOPs

Today's closures and advancements expose 10 genuinely new structural problems beyond the existing NQ list. Numbered NOP-A through NOP-J.

| NOP | Title | Surfaced from | Priority |
|-----|-------|---------------|----------|
| NOP-A | Sharp ↔ Spectral bound reconciliation | Lemma 3-sharp (§8) vs Lemma 13 (§12) | High |
| NOP-B | σ_rich Lipschitz constant (OP-0008-DIST) | Session W; today no progress | High |
| NOP-C | Multi-step (N≥3) temporal identity coherence | Lemma 6 only handles N=2 | Mid |
| NOP-D | Self-referential fixed-point cost-perturbation stability | Lemma 10 single-step only | Mid |
| NOP-E | D-ST-3 vs `scipy.ndimage` proxy phase boundary | exp83 proxy gap | Mid |
| NOP-F | $T_*$ emergence (not definition) from deterministic dynamics | Lemma 14 sketch, §4 | High |
| NOP-G | Geometric identity: $\mu_\mathrm{joint}\,d_\mathrm{inter}^{*2}$ ↔ first-passage time | Lemma 13 exponent form | Low |
| NOP-H | σ_rich ↔ σ_standard agreement range | OP-0008 sub-problems | Mid |
| NOP-I | Topology of $\Sigma_M^K / S_K$ configuration space | OP-0009 K-field quotient | Low |
| NOP-J | Information geometry on $\mathcal{F}_M$: Fisher metric ↔ Hessian | Lemma 14 §4.1 | Mid-High |

---

## §2. NOP-A — Sharp ↔ Spectral bound reconciliation

### §2.1 Statement

The off-diagonal mass bound $\eta_\mathrm{cross}$ has two distinct closed forms:

**Sharp form (Lemma 3-sharp, `03_development.md` §8.3):**
$$\eta_\mathrm{cross}^\mathrm{sharp} = \exp\!\left(-\frac{\gamma_\mathrm{OT}\,\Delta_\varphi^2_\mathrm{inter} - L_g\,d_\mathrm{eff}}{\varepsilon_\mathrm{OT}}\right).$$

**Spectral form (Lemma 13 sketch, `08_NQ6_spectral_gap_advance.md` §3):**
$$\eta_\mathrm{cross}^\mathrm{spec} = \exp\!\left(-\frac{\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2}{2\varepsilon_\mathrm{OT}}\right).$$

The exponents differ structurally: sharp form's $\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff}$ has an $\varepsilon_\mathrm{OT}$-dependent ceiling at $\varepsilon_\mathrm{OT}^* \approx 0.45$; spectral form's $\mu_\mathrm{joint}\,d_\mathrm{inter}^{*2}/2$ has no ceiling.

**The question.** Which one is correct? Are they fundamentally equivalent (different parametrizations of the same underlying bound) or do they encode genuinely different physics?

If equivalent, Lemma 13 must reduce to Lemma 3-sharp under the right change of variables. If not, the apparent contradiction (Lemma 13 says "no ceiling", Lemma 3-sharp says "ceiling at 0.45") signals that one of them has a hidden hypothesis that breaks at the limiting regime.

### §2.2 Multi-tool angles

**Angle A1 — Direct algebraic reduction.** Show that under the formation-conditioned regime, the Lipschitz constant $L_g$ depends on $\mu_\mathrm{joint}$:
$$L_g \cdot d_\mathrm{eff} = \mathrm{some function of}\; \mu_\mathrm{joint},\,d_\mathrm{inter}^*.$$
Specifically, conjecture: $L_g \approx 1/\sqrt{\mu_\mathrm{joint} d_\mathrm{inter}^{*2}}$ in the linearized regime. Then sharp exponent and spectral exponent become functionally equivalent.

**Angle A2 — Concentration-of-measure perspective.** Sharp form uses Lipschitz dual potentials → log-Sobolev-type concentration. Spectral form uses Hessian → Bakry-Émery curvature-dimension condition. The two are related via the Brascamp-Lieb inequality: log-Sobolev constant $\geq$ Hessian eigenvalue (under uniform convexity). This gives:
$$L_g^2 \cdot \mathrm{diam}^2 \;\geq\; 1/\mu_\mathrm{joint}.$$
So sharp form's exponent is *bounded above* by spectral form's. Spectral form is *tighter*.

**Angle A3 — Both bounds are valid, sharp is conservative.** The sharp form is a *worst-case* bound (Lipschitz over all $g$); the spectral form uses the *additional* structure of the Hessian eigenvalues which is a strictly tighter constraint. Therefore Lemma 13, if rigorous, *supersedes* Lemma 3-sharp.

**Angle A4 — Empirical test.** exp83-variant at $\varepsilon_\mathrm{OT} \in \{0.5, 1, 2, 5\}$ measuring $\eta_\mathrm{cross}$ directly. If matches spectral form (no ceiling), Lemma 13 is empirically validated. If matches sharp form (ceiling at 0.45), Lemma 13 needs reformulation.

### §2.3 Candidate first lemma

**Lemma 15 (NOP-A reconciliation, Cat C target Cat B):** *Under (A1)–(A8)+(A7') + the linearized-formation regime (small perturbations from the K-formation manifold), the sharp form Lipschitz constant satisfies:*
$$L_g^2 \;\leq\; \frac{C_\mathrm{geom}}{\mu_\mathrm{joint} \cdot d_\mathrm{inter}^{*2}},$$
*where $C_\mathrm{geom} = O(1)$ is a graph-geometric constant. Hence sharp exponent ≤ spectral exponent, and Lemma 13 (spectral form) is the tighter bound.*

**Status:** Cat C, sketched. Difficulty: 1 session.

### §2.4 Priority and recommendation

**Priority: HIGH.** Resolves the apparent contradiction between two of today's main results. Important for canonical-side coherence. **Recommended:** address before promotion session.

---

## §3. NOP-B — σ_rich Lipschitz constant (= OP-0008-DIST)

### §3.1 Statement

OP-0008-DIST (registered Session W, 2026-05-06): *σ-stability under perturbation.* The σ-rich signature $\sigma_\mathrm{rich}(C; u, P)$ uses subgraph + restricted field. Question: under small perturbations $\delta u$, how does $\sigma_\mathrm{rich}$ change?

A bound of the form
$$\|\sigma_\mathrm{rich}(C; u + \delta u) - \sigma_\mathrm{rich}(C; u)\| \;\leq\; L_\sigma \cdot \|\delta u\|$$
is required for σ to be a stable observable under noise.

**Today no progress on this.** Listed as "OPEN, no structured path yet" in Session W. Now that T-Temporal-Identity Cat B is essentially closed, σ-inheritance becomes the next natural target — and σ-stability is a prerequisite.

### §3.2 Multi-tool angles

**Angle B1 — Spectral perturbation theorem.** σ_standard uses Wigner-projection eigenvectors. By Davis-Kahan theorem, eigenspace perturbation $\|\delta v\| \leq \|\delta H\|/\mathrm{gap}$. Combined with Hessian perturbation $\|\delta H\| \leq L_H \|\delta u\|$: σ-Lipschitz with constant $L_H/\mathrm{gap}$.

**Angle B2 — Functional analysis (variational).** σ_rich = restricted field on subgraph; perturbation propagates through restriction operator (linear, bounded). σ-Lipschitz constant = subgraph operator norm.

**Angle B3 — Geometric (Riemannian).** View σ as a section of a fiber bundle over $\mathcal{F}_M$; Lipschitz = section's gradient norm.

**Angle B4 — Concentration-of-measure.** Treat σ as a random variable under noise; concentration around mean = σ-stability.

### §3.3 Candidate first lemma

**Lemma 16 (σ_rich Lipschitz, Cat C):** *Under (A1)–(A3) + σ-rich definition (`canonical.md` Commitment 18 candidate):*
$$\|\sigma_\mathrm{rich}(C; u + \delta u, P) - \sigma_\mathrm{rich}(C; u, P)\|_2 \;\leq\; L_\sigma \cdot \|\delta u|_C\|_2,$$
*with $L_\sigma \leq O(\rho_\mathrm{pers}^{-1})$ depending on the persistence threshold (smaller threshold ⇒ more sensitive σ).*

**Proof sketch.** σ_rich = (mass, centroid, inertia tensor) on subgraph. Each component is polynomial in $u$:
- mass = $\sum_x u(x)$, Lipschitz constant 1.
- centroid = mass-weighted average of position, Lipschitz constant $\propto |C|/m$.
- inertia tensor = mass-weighted second moment, Lipschitz constant $\propto |C|^2/m$.

In each case, mass appears in denominator (via $1/m$); since $m \geq \rho_\mathrm{pers}|C|$ (D-ST-3), the Lipschitz constant is bounded by $|C|^2/(\rho_\mathrm{pers}|C|) = |C|/\rho_\mathrm{pers}$. $\square$

**Status:** Cat C, sketched. Cat B target: 1–2 sessions.

### §3.4 Priority

**Priority: HIGH.** Required for T-σ-Inherit Cat B (next session candidate Option B). Without σ-Lipschitz, σ-inheritance under perturbation is undefined.

---

## §4. NOP-C — Multi-step temporal identity coherence

### §4.1 Statement

Lemma 6 (`03_development.md` §10) closes OP-0012-CC for **N=2** composition (single intermediate state $u_s$). For perception streams, N is large (10s, 100s of frames). Does the bijection chain remain coherent over long N?

**The error accumulation problem.** Per-step error: $\eta_\mathrm{self}^{\,K} \approx 1.2 \times 10^{-4}$ at sharp regime. Over N steps: $1 - (1 - \eta_\mathrm{self}^{\,K})^N \approx N \eta_\mathrm{self}^{\,K}$. For N = 10000 (long stream): $\approx 1.2$ — *trivially exceeds 1*, so the diagonal mass bound becomes vacuous.

**The question.** Find an N-coherent bijection theorem that does not degrade per-step.

### §4.2 Multi-tool angles

**Angle C1 — Markov chain ergodicity.** Treat $\pi: \mathrm{Comp} \to \mathrm{Comp}$ as a transition kernel. Show that the chain converges to a stationary distribution; long-time behavior is well-defined.

**Angle C2 — Cocycle / homotopy theory.** A coherent bijection chain is a *cocycle* over time. Cohomology obstructions = identity inconsistencies.

**Angle C3 — Renormalization.** Coarse-grain time: $N$ steps → $\sqrt{N}$ "super-steps". Show error scales sub-additively.

**Angle C4 — Ergodic theorem.** $\frac{1}{N}\sum$ of per-step errors converges to ensemble mean — averaging effect.

### §4.3 Candidate first lemma

**Lemma 17 (multi-step coherence, Cat C):** *Under hypotheses of Lemma 6 + ergodic regularity hypothesis (REG): the per-step error has a sub-additive limit*
$$\lim_{N \to \infty} \frac{1}{N} \log\!\left(\frac{\gamma_{t \to t+N}(C, C^{\pi_\mathrm{cum}(C)})}{m_C^t}\right) = -\eta_\infty,$$
*where $\eta_\infty < 1$ is the long-time decay rate, smaller than the per-step Lemma 6 error $\eta_\mathrm{self}^{\,K}$.*

**Status:** Cat C, sketched. Difficulty: 2 sessions.

### §4.4 Priority

**Priority: MID.** Important for long-stream robustness but not blocking promotion. Defer.

---

## §5. NOP-D — Self-referential fixed-point cost-perturbation stability

### §5.1 Statement

Lemma 10 (`06_close_OP0011_step2.md` §2.3) bounds $|\gamma_M - \gamma_{M'}| \leq 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$ for cost difference $\delta$. But the SCC self-referential cost $c[u]$ depends on $u$ via the fingerprint $\varphi(u)$; perturbing $u$ by $\delta u$ changes cost by $\delta c \approx L_\varphi \|\delta u\|$.

Iteratively: at each Sinkhorn fixed-point iteration, the cost is updated, perturbing the next plan. Question: is the sequence of plans Cauchy? Does the Schauder fixed-point exist for any $\varepsilon_\mathrm{OT} > 0$?

### §5.2 Multi-tool angles

**Angle D1 — Banach fixed-point.** The map $u \mapsto M^*(c[u]) \to \tilde u$ is a contraction under $\varepsilon_\mathrm{OT}$ small + $L_\varphi$ small. Banach gives unique fixed point.

**Angle D2 — Schauder fixed-point.** Map is continuous from compact $\Sigma_M$ to itself. Schauder gives fixed point existence (already canonical T-Persist-1(e) line 1805).

**Angle D3 — Contraction-mapping bound.** Make the contraction constant explicit: $\rho < 1$ iff $L_\varphi \cdot 2 M_\mathrm{tot}/\varepsilon_\mathrm{OT}^2 < 1$, i.e., $\varepsilon_\mathrm{OT} > \sqrt{2 L_\varphi M_\mathrm{tot}}$. **Insight:** cost-perturbation contraction needs $\varepsilon_\mathrm{OT}$ large — opposite of (A7') which needs $\varepsilon_\mathrm{OT}$ small. Tension.

**Angle D4 — Implicit function theorem.** Fixed-point uniqueness via IFT applied to the map; Jacobian invertibility.

### §5.3 Candidate first lemma

**Lemma 18 (self-referential plan stability, Cat C):** *Under (A1)–(A6) + Lipschitz fingerprint (DR2'): the self-referential Sinkhorn iteration $u^{(k+1)} = (M^*(c[u^{(k)}]))^\top \mathbf{1}$ converges geometrically with rate $\rho \leq 2 L_\varphi M_\mathrm{tot}/\varepsilon_\mathrm{OT}^2 < 1$ provided $\varepsilon_\mathrm{OT} > \sqrt{2 L_\varphi M_\mathrm{tot}}$.*

At default exp83 parameters: $L_\varphi \leq 1.43$ (canonical line 1807), $M_\mathrm{tot} \approx 50$ (mass): $\sqrt{2 \cdot 1.43 \cdot 50} \approx 12$. So convergence guaranteed for $\varepsilon_\mathrm{OT} > 12$ — far above the (A7') sharp regime.

**This reveals a tension:** (A7') sharp regime ($\varepsilon_\mathrm{OT} \leq 0.45$) is *outside* the contraction regime ($\varepsilon_\mathrm{OT} > 12$). Self-referential fixed-point iteration may diverge in (A7') sharp regime. **This is a non-trivial open problem.**

### §5.4 Priority

**Priority: MID-HIGH.** Reveals a tension between the two regimes. May affect Lemma 11's kernel-independence claim if iteration doesn't converge. Important to resolve before canonical promotion.

---

## §6. NOP-E — D-ST-3 vs proxy phase boundary

### §6.1 Statement

D-ST-3 (canonical) requires threshold-stable connected components (CC of $\{u \geq \rho_\mathrm{pers}\}$ surviving $\pm \tau$ perturbation). exp83 uses `scipy.ndimage` CC at threshold (no $\pm \tau$ check).

**Question.** Under what conditions are the two equivalent? When do they diverge?

### §6.2 Multi-tool angles

**Angle E1 — Persistent homology.** D-ST-3 ≈ 0-dimensional persistence of super-level filtration. Bars with persistence $> 2\tau$ are D-ST-3 components. Proxy is a single threshold = $\rho_\mathrm{pers}$.

**Angle E2 — Morse-theoretic.** D-ST-3 = stable critical points; proxy = arbitrary critical points. Difference: critical points "between" $\rho_\mathrm{pers} - \tau$ and $\rho_\mathrm{pers} + \tau$ are D-ST-3-unstable but proxy-stable.

**Angle E3 — Quantitative bound.** Number of differing components = number of critical values in $[\rho_\mathrm{pers} - \tau, \rho_\mathrm{pers} + \tau]$. By Morse density: bounded.

**Angle E4 — Probabilistic.** Under random perturbation, proxy components are stable with probability $1 - O(\tau)$; D-ST-3 always stable.

### §6.3 Candidate first lemma

**Lemma 19 (proxy-D-ST-3 equivalence, Cat C):** *Under (A1)–(A2) + the formation regularity assumption (REG-PC): $u$ has no critical values in $[\rho_\mathrm{pers} - \tau, \rho_\mathrm{pers} + \tau]$. Then the proxy and D-ST-3 components agree.*

**Status:** Cat C, easy. (REG-PC) is a generic condition (Sard's theorem-style). Cat B target: 0.5 session.

### §6.4 Priority

**Priority: MID.** Required for S-A2 (canonical D-ST-3 absorption). Should be addressed during promotion session.

---

## §7. NOP-F — $T_*$ emergence from deterministic dynamics

### §7.1 Statement

Lemma 14 (`09_OP0021_T_star_brainstorm.md` §4) defines $T_*$ via Fisher information / RG. But this is a *definition*, not a *derivation*: $T_*$ is given by external structure (observation likelihood / Hessian).

**Deeper question.** Can $T_*$ *emerge* from the deterministic SCC gradient flow alone? I.e., does $\dot u = -\nabla E$ on $\Sigma_M$, in some appropriate sense (chaos, ergodicity, large-time), produce effective stochastic dynamics with a derived $T_*$?

### §7.2 Multi-tool angles

**Angle F1 — Anosov flow / hyperbolic dynamics.** If gradient flow is mixing on the formation basin (after restriction to slow modes), it has positive Lyapunov exponent → effective noise.

**Angle F2 — Mori-Zwanzig projection.** Project gradient flow onto slow-mode subspace; project-out fast modes appear as memory + noise (generalized Langevin equation).

**Angle F3 — Stochastic reduction (Khasminskii averaging).** Under fast-mode averaging, slow-mode dynamics become stochastic with $T_*$ emerging from fast-mode statistics.

**Angle F4 — Foias-Saut weak attractor.** Gradient flow has compact attractor; fluctuations on attractor have intrinsic scale.

**Angle F5 — Quantum-classical correspondence.** Treat finite-dimensional gradient flow as classical limit of a quantum system; ℏ-scale fluctuations emerge.

### §7.3 Candidate first lemma

**Lemma 20 (Mori-Zwanzig $T_*$ emergence, Cat C target Cat B):** *Under the hypothesis (FAST-SLOW): SCC Hessian spectrum decomposes into slow modes ($\mu < \mu_\mathrm{joint}/2$) and fast modes ($\mu > \mu_\mathrm{joint}/2$). Under Mori-Zwanzig projection of gradient flow onto slow modes:*
$$\dot u_\mathrm{slow} = -\nabla E_\mathrm{slow}(u_\mathrm{slow}) + \xi(t),$$
*where $\xi(t)$ is generalized noise with autocorrelation $\langle \xi(0)\xi(t)\rangle \approx T_* \delta(t)$ and*
$$T_* = \frac{1}{n_\mathrm{fast}}\sum_{k:\mu_k > \mu_\mathrm{joint}/2} \mu_k^{-1} = T_*^{(\mathrm{RG})}.$$

This **derives** $T_*^{(\mathrm{RG})}$ from the deterministic gradient flow + projection — not posit it.

**Status:** Cat C, sketched. Difficulty: 2–3 sessions. **High intellectual reward.**

### §7.4 Priority

**Priority: HIGH.** Resolves a deep foundational question about whether $T_*$ is derivable or axiomatic. Compatible with Lemma 14 (Mori-Zwanzig + Fisher converge to same $T_*^{(\mathrm{RG})}$).

---

## §8. NOP-G — Geometric identity $\mu_\mathrm{joint} d_\mathrm{inter}^{*2} \leftrightarrow$ first-passage time

### §8.1 Statement

Lemma 13's exponent $\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2/(2\varepsilon_\mathrm{OT})$ resembles first-passage / mean exit time for diffusion in a quadratic potential. Coincidence or geometric identity?

### §8.2 Multi-tool angles

**Angle G1 — Brownian bridge analysis.** First-passage time from minimum to saddle in quadratic well = $\mu^{-1}(d/\sigma)^2 \cdot \exp(\Delta E/T)$. Match to Lemma 13 form.

**Angle G2 — Heat kernel asymptotics.** Probability of diffusion path traveling distance $d$ in time $\tau$ at temperature $T$: $\sim \exp(-d^2/(2\tau T))$.

**Angle G3 — Onsager-Machlup variational.** Most-likely path between minima minimizes action $\int (\dot u + \nabla E)^2/(2T)$; identifying the $\mu d^2/(2T)$ scaling.

### §8.3 Candidate first lemma

**Lemma 21 (geometric identity, Cat C):** *Lemma 13's spectral exponent $\mu_\mathrm{joint}\,d_\mathrm{inter}^{*2}/2$ equals the first-passage exit-time scaling for a Brownian particle in the joint formation Hessian basin.*

**Status:** Cat C, sketched. Low priority.

### §8.4 Priority

**Priority: LOW.** Aesthetic / confirmatory. Defer.

---

## §9. NOP-H — σ_rich ↔ σ_standard agreement range

### §9.1 Statement

σ_rich (subgraph-based) and σ_standard (Wigner-projection-based) are two formulations of the σ-signature. Canonical commitments register both as candidates. **Question:** in what regime do they agree? Outside, which is correct?

### §9.2 Multi-tool angles

**Angle H1 — Formation-conditioned spectral analysis.** For deep-core regions, Wigner projection and subgraph restriction give similar inertia tensors. Equivalence at order $O(1/|C|)$.

**Angle H2 — Generic vs degenerate Hessian.** Wigner projection is well-defined when Hessian is non-degenerate; σ_rich is always well-defined. σ_standard fails at bifurcation; σ_rich does not.

**Angle H3 — Empirical comparison (NQ-242).** Existing experiments on σ_rich vs σ_standard. Identify regime where they diverge.

### §9.3 Candidate first lemma

**Lemma 22 (σ-equivalence, Cat C):** *Under (A1)–(A3) + non-degenerate joint Hessian (NB): σ_rich(C) and σ_standard(C) agree up to $O(\mu_\mathrm{joint}^{-1})$ correction.*

### §9.4 Priority

**Priority: MID.** Required for OP-0008 sub-problem clarification.

---

## §10. NOP-I — Topology of $\Sigma_M^K / S_K$ configuration space

### §10.1 Statement

K-formation manifold under S_K-quotient. **Question:** topological invariants (homotopy, homology, fundamental group)?

### §10.2 Multi-tool angles

**Angle I1 — Configuration space.** $\Sigma_M^K / S_K = \mathrm{Sym}^K(\Sigma_M)$, K-th symmetric power. Standard configuration-space topology.

**Angle I2 — Equivariant cohomology.** $\Sigma_M^K$ has S_K action; equivariant cohomology gives the quotient invariants.

**Angle I3 — Stratification.** Singular stratum where formations coincide; smooth stratum is regular.

### §10.3 Candidate first lemma

**Lemma 23 (configuration topology, Cat C):** *$\Sigma_M^K / S_K$ is homotopy-equivalent to the classifying space $B(S_K)$ at low dimensions, with smooth stratum the complement of the diagonal.*

### §10.4 Priority

**Priority: LOW.** Foundational interest, no immediate canonical impact. Defer.

---

## §11. NOP-J — Information geometry on $\mathcal{F}_M$: Fisher metric ↔ Hessian

### §11.1 Statement

Fisher information matrix $\mathcal{I}(u^*)$ defines a Riemannian metric on $\Sigma_M$. Hessian of $E$ also defines a metric. **Question:** when do they coincide? Connection to $T_*$?

### §11.2 Multi-tool angles

**Angle J1 — Cramér-Rao saturation.** Fisher metric = Hessian of likelihood. SCC energy is *not* a likelihood, but the relation can be made precise via gauge-fixing.

**Angle J2 — Amari's information geometry.** Dual flat structures on $\mathcal{F}_M$; Pythagorean theorem for KL divergence.

**Angle J3 — Otto calculus.** Wasserstein metric vs Fisher metric vs Hessian metric. Three distinct geometries on the same simplex.

### §11.3 Candidate first lemma

**Lemma 24 (information-Hessian compatibility, Cat C):** *Under the canonical observation likelihood $\Phi_\mathrm{obs}$ + LM1–LM3, the Fisher metric is conformal to the boundary-restriction of the SCC Hessian, with conformal factor $T_*^{(\mathrm{Fisher})}$.*

### §11.4 Priority

**Priority: MID-HIGH.** Compatible with NOP-F (T_* emergence); may unify the angles.

---

## §12. Aggregated NOP priority and disposition

| NOP | Priority | Working file? | Estimated sessions |
|-----|----------|---------------|--------------------|
| NOP-A (Sharp ↔ Spectral) | High | YES (`working/MF/sharp_vs_spectral_2026-05-07.md`) | 1 |
| NOP-B (σ_rich Lipschitz) | High | YES (extends `working/MF/sigma_rich_*.md`) | 1–2 |
| NOP-C (Multi-step coherence) | Mid | NO (defer) | 2 |
| NOP-D (Self-ref FP stability) | Mid-High | YES (`working/MF/self_ref_fp_stability.md`) | 1–2 |
| NOP-E (D-ST-3 ↔ proxy) | Mid | NO (resolve in promotion session as S-A2) | 0.5 |
| NOP-F ($T_*$ emergence) | High | YES (extend `working/MF/pf_tstar_langevin.md`) | 2–3 |
| NOP-G (Geometric identity) | Low | NO | 1 |
| NOP-H (σ_rich ↔ σ_standard) | Mid | NO (in OP-0008 working files) | 1 |
| NOP-I (Config space topology) | Low | NO (defer) | 1 |
| NOP-J (Info geometry) | Mid-High | YES (combined with NOP-F) | 1 |

**Total NOP load:** 13–17 session-equivalents if all addressed. Realistic priority sequencing for next 2 weeks:

**Week 7:** NOP-B (σ-Lipschitz) — unblocks T-σ-Inherit Cat B.
**Week 8:** NOP-A (Sharp ↔ Spectral) + NOP-D (Self-ref FP) — coherence before promotion.
**Week 9:** NOP-F + NOP-J ($T_*$ emergence + info geometry) — Package II foundation.

---

## §13. Working/MF/ files to create

### §13.1 Recommended new working files

The following NOPs warrant new working files for promotion-pipeline tracking:

1. **`working/MF/sharp_vs_spectral_2026-05-07.md`** — NOP-A reconciliation. Working draft from §2 of this file.
2. **`working/MF/self_ref_fp_stability.md`** — NOP-D self-referential cost-perturbation stability. From §5.

### §13.2 Existing files to extend (today)

These NOPs extend existing working files:

3. **`working/MF/pf_tstar_langevin.md`** — append NOP-F + NOP-J ($T_*$ emergence + info geometry; angles + Lemma 14 + Lemma 20).
4. **`working/MF/sigma_rich_orientation_derivation.md`** (or similar) — append NOP-B σ_rich Lipschitz Lemma 16.

For today's session, I will create the two NEW working files (NOP-A and NOP-D) and extend the most natural existing file (NOP-F into pf_tstar_langevin.md). NOP-B is deferred to T-σ-Inherit Cat B Review session.

---

## §14. Updates to `theorem_status.md` (proposed; do not insert directly)

When a future audit session updates `theorem_status.md`, add NOPs to a new "New Open Problems Pipeline (Session 2026-05-07)" subsection of the Open Problems Catalog. Suggested format:

> **NOP-A** — Sharp/Spectral bound reconciliation. **HIGH.** From Lemma 3-sharp vs Lemma 13. Lemma 15 candidate. Estimated 1 session.
>
> **NOP-B** — σ_rich Lipschitz / OP-0008-DIST. **HIGH.** Lemma 16 candidate. Estimated 1–2 sessions.
>
> **NOP-D** — Self-referential FP cost-perturbation stability. **MID-HIGH.** Tension between (A7') and contraction regime. Lemma 18 candidate. 1–2 sessions.
>
> **NOP-F** — $T_*$ emergence from deterministic dynamics. **HIGH.** Lemma 20 (Mori-Zwanzig). 2–3 sessions.
>
> **NOP-J** — Information geometry on $\mathcal{F}_M$. **MID-HIGH.** Lemma 24 (Fisher ↔ Hessian compatibility). 1 session.
>
> *(NOP-C, E, G, H, I — lower priority, deferred.)*

---

*End of `10_new_open_problems.md`.*
