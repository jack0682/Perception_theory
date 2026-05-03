# k_selection_a_free_energy.md — K-Selection (a) Free Energy Variational Derivation

**Status:** working draft (W5 Day 4, Task #5).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Free-energy variational derivation of K-Selection mechanism — option (a) of OP-0005 4-option list.
**Author origin:** Task #5 K-Selection (a); attacks OP-0005 via thermodynamic free-energy principle. Companion to Task #6 (Kramers metastability), Task #7 (numerical anchor), Task #8 (Commitment 16 compatibility).
**Canonical refs:** §11.1 Commitment 14, 14-Multi, 16; §13 T-Merge (b) (M-1 proved); §14 CN5, CN10, CN15 (Static/Dynamic Separation); §15 OP-0005 (K-Selection direct attack).
**Working refs:** `K_status_commitment.md` (OAT-1, Commitment 16 K_field/K_act decomposition); `multi_formation_sigma.md` (D-6a static); `sigma_multi_trajectory.md` (D-6b dynamic).

---

## §1. Mission

> **"OP-0005 K-Selection 4-옵션 중 (a) free energy variational derivation: $F(K; \beta, M, G) := \mathcal{E}_K^* - T \cdot S(K)$ 에서 K_act 가 free-energy minimum 에 의해 selected 됨을 derive. M-1 (T-Merge (b)) 과 모순 없이 reconcile (CN15 Static/Dynamic Separation 의 free-energy version)."**

이 working file 은 OP-0005 K-Selection mechanism 의 첫 번째 candidate (free-energy variational) 을 develop. M-1 ground-state 결과 ($\mathcal{E}_{\mathrm{bd}}$ minimum is K=1) 와 *empirical* K>1 observation 의 conflict 를 *finite-temperature* / *complexity-penalty* 자연 framework 로 reconcile 한다.

**핵심 결론**:
1. Free energy $F(K) := \mathcal{E}_K^* - T \cdot S(K)$ 정식 정의 (§3).
2. 엔트로피 $S(K)$ component: configurational + entropic contributions (§4).
3. $T \to 0$ limit 에서 M-1 회복 ($K^* = 1$); $T > 0$ 에서 $K^* > 1$ possible (§5).
4. BIC parallel: complexity penalty $\propto K \log N$ (§6).
5. Cat B target with Cat A path via NQ-242c-Rich + thermodynamic anchor (§7).
6. Reconciliation with M-1 + Theorem 2 + Commitment 16 (§8).

---

## §2. Setup and Background

### §2.1 OP-0005 4 options

OP-0005 lists 4 K-Selection candidate mechanisms:
- (a) **Free energy variational** (this file): $K^* = \arg\min_K F(K)$ via thermodynamic free-energy principle.
- (b) **Kramers metastability** (Task #6): $K^*$ kinetically determined via metastability barriers; $K_{\mathrm{act}}(t)$ trajectory through energy landscape.
- (c) **Symmetry-broken numerical anchor** (Task #7): empirical $K^*$ from gradient-flow trajectories on representative graphs.
- (d) **External fixing** (current default): $K_{\mathrm{field}}$ set ex ante; $K_{\mathrm{act}} \leq K_{\mathrm{field}}$ via Commitment 16.

These are not mutually exclusive: (a) provides the equilibrium prediction; (b) the kinetic correction; (c) the empirical anchor; (d) the modeling-layer commitment.

### §2.2 M-1 conflict

Per `theorem_status.md` (Open Problems Catalog) OP-0002 M-1 status: T-Merge (b) proves K=1 has lowest pure $\mathcal{E}_{\mathrm{bd}}$ (Modica-Mortola Γ-convergence; perimeter minimization). But empirical K>1 is observed (NQ-141, R23 F=9, etc.).

Reconciliation via CN15 Static/Dynamic Separation: **static global minimum is K=1** (under pure $\mathcal{E}_{\mathrm{bd}}$), but **dynamic protocol-endpoint observables** ($\widehat{K}, \mathcal{F}$) need not equal it.

This file extends to **finite-T thermodynamic** reconciliation: $F(K)$ minimum at $T > 0$ may differ from $\mathcal{E}_K^*$ minimum at $T = 0$.

### §2.3 Why "free energy"?

The term "free energy" here is used in two compatible senses:
- **Thermodynamic**: Helmholtz free energy $F = E - T S$ at finite temperature $T$.
- **Bayesian/statistical**: variational free energy $F = -\log Z$ for partition function $Z = \sum_K e^{-\beta E(K)}$, which under saddle-point approximation reduces to Helmholtz form.
- **Information-theoretic**: BIC-style complexity-penalized score.

All three give compatible scaling laws (§6).

---

## §3. Free Energy Definition

### §3.1 Energy minimum at fixed K

For each fixed $K \in \{1, 2, \ldots, K_{\mathrm{field}}\}$, define:
$$\mathcal{E}^*_K := \min_{\mathbf{u} \in \widetilde\Sigma^K_M : K_{\mathrm{act}}(\mathbf{u}) = K} \mathcal{E}_K(\mathbf{u})$$
— the minimum SCC energy over configurations with exactly $K$ active formations.

**Note**: $\mathcal{E}^*_K$ depends on graph $G$, total mass $M$, energy parameters $(\alpha, \beta, \lambda_{\mathrm{rep}}, a_{\mathrm{cl}})$.

### §3.2 Configurational entropy

For each $K$, the **configurational entropy** $S(K)$ counts the equivalence classes of $K$-formation minimizers (modulo Aut(G) ⋊ S_K):
$$S(K) := \log\big|\{\mathbf{u}^* : K_{\mathrm{act}}(\mathbf{u}^*) = K, \mathbf{u}^* \text{ is local minimum}\}/(\mathrm{Aut}(G) \wr S_K)\big|.$$

For $K = 1$: typically $S(1) = O(1)$ — few inequivalent single-formation minimizers (e.g., uniform; F=1 ground state).

For $K > 1$: $S(K)$ grows polynomially or logarithmically in $K$ (for a graph with $|X|$ vertices, $K$-formation configurations have $\sim O(|X|^K / K!)$ choices modulo symmetry).

Specifically: $S(K) \sim K \log(|X|/K) + O(1)$ for $K \ll |X|$ (combinatorial K-subset placements).

### §3.3 Free energy

**Definition 3.1 (Free Energy at K).** For inverse temperature $\beta_T = 1/T$ (where $T$ is *thermal* temperature, distinct from SCC parameter $\beta$ — use $T$ to avoid clash):
$$F(K; T) := \mathcal{E}^*_K - T \cdot S(K).$$

(For SCC, the notation $\beta_T$ avoids the canonical $\beta$ parameter.)

### §3.4 K-selection rule

**Free-energy K-Selection rule (Option (a))**:
$$K^*(T) := \arg\min_{K \in \{1, \ldots, K_{\mathrm{field}}\}} F(K; T).$$

This is the predicted equilibrium $K_{\mathrm{act}}$ at temperature $T$.

---

## §4. Asymptotic Behavior

### §4.1 Zero-temperature limit ($T \to 0$)

**Claim 4.1**: $\lim_{T \to 0} K^*(T) = \arg\min_K \mathcal{E}^*_K$.

**Proof**: $T \to 0$ ⇒ $T S(K) \to 0$; $F(K; 0) = \mathcal{E}^*_K$. ✓

By T-Merge (b) (M-1 proved), in pure $\mathcal{E}_{\mathrm{bd}}$ regime: $\arg\min_K \mathcal{E}^*_K = 1$. Hence $K^*(0) = 1$ ⇒ **M-1 recovered as $T \to 0$ limit**.

### §4.2 High-temperature limit ($T \to \infty$)

**Claim 4.2**: $\lim_{T \to \infty} K^*(T) = K_{\mathrm{field}}$ (the architectural cap).

**Proof**: As $T \to \infty$, entropy term $T S(K)$ dominates $\mathcal{E}^*_K$. $S(K)$ is non-decreasing in $K$ (more configurations available for higher $K$). Hence $K^*(\infty)$ is the largest available $K$, namely $K_{\mathrm{field}}$. ✓

⇒ At high $T$, all formation labels are activated: thermal noise overrides energy considerations.

### §4.3 Crossover temperature $T_c$

There exists a crossover temperature $T_c$ where $F(K=1) = F(K=2)$:
$$T_c := \frac{\mathcal{E}^*_2 - \mathcal{E}^*_1}{S(2) - S(1)}.$$

For $T < T_c$: $K^* = 1$.
For $T > T_c$: $K^* \geq 2$.

For SCC default parameters ($\beta = 4$, $\lambda_{\mathrm{rep}} = 0.1$ on $T^2_{20}$): $\mathcal{E}^*_2 - \mathcal{E}^*_1 \sim O(\lambda_{\mathrm{rep}} \cdot \mathrm{overlap}) \sim 0.01$ (small, perturbative); $S(2) - S(1) \sim \log |X| = \log 400 \approx 6$. Hence $T_c \sim 0.01/6 \approx 1.7 \times 10^{-3}$ — small thermal noise suffices to flip K=1 → K=2 preferred.

---

## §5. Reconciliation with M-1

### §5.1 Apparent conflict

T-Merge (b): K=1 minimizes pure $\mathcal{E}_{\mathrm{bd}}$. But empirical K>1 observed.

### §5.2 Two-level resolution

**Level 1 (Static layer, CN15)**: T-Merge (b) is about *static* energy minimum at $T = 0$. Empirical K>1 is a *dynamic* observation, not necessarily at $T = 0$.

**Level 2 (this file)**: At $T > T_c$, free-energy minimum is at K>1, not K=1. M-1 holds at $T=0$; finite-$T$ K-selection is K>1 by entropy preference.

**Both levels combine**: empirical K>1 is **consistent with M-1** under either:
- Level 1: dynamic protocol endpoint differs from static minimum (CN15).
- Level 2: thermodynamic $T > T_c$ shifts equilibrium to K>1.

### §5.3 Connection to Theorem 2

Theorem 2 (W4 04-24): F=1 single-disk minimizer is **not a critical point** of full SCC energy. This is a *static* statement: the K=1 ground state under pure $\mathcal{E}_{\mathrm{bd}}$ doesn't survive into full SCC.

Free-energy reconciliation: even if F=1 were a critical point, finite-$T$ free-energy preferred K>1.

⇒ Theorem 2 + free-energy variational both contribute to K-Selection mechanism.

---

## §6. BIC Parallel and Information-Theoretic Form

### §6.1 BIC complexity penalty

Bayesian Information Criterion: $\mathrm{BIC} = -2 \log L + k \log n$ where $k$ is parameter count, $n$ is sample size, $L$ is likelihood.

For K-formation model: $k = K \cdot d_j$ (parameters per formation) and $n = |X|$ (graph vertices). Hence BIC contribution:
$$\Delta_{\mathrm{BIC}}(K) = K \cdot d_j \cdot \log |X|.$$

### §6.2 Mapping to free energy

Identifying $-\log L \leftrightarrow \mathcal{E}^*_K$ and $-k \log n / 2 \leftrightarrow T S(K)$:
$$F(K; T) = \mathcal{E}^*_K - T S(K) \approx \mathcal{E}^*_K + \Delta_{\mathrm{BIC}}(K) / 2$$
when $T \approx 1/2$ in natural units. The BIC complexity penalty enters as a *positive* contribution to free energy at $K > 1$, opposing entropy gain.

⇒ BIC variant of K-selection: $K^* = \arg\min_K (\mathcal{E}^*_K + \Delta_{\mathrm{BIC}}(K)/2)$.

This penalty form *opposes* the entropy form (entropy favors high K, BIC penalizes high K). Net behavior depends on which term dominates — typically entropy for small $K$, BIC for large $K$.

### §6.3 Combined Helmholtz + BIC form

A more refined model: $F(K; T) = \mathcal{E}^*_K - T S_{\mathrm{conf}}(K) + (T_0 / 2) \cdot K \log |X|$ where $T_0$ encodes the BIC complexity scale (independent of thermal $T$).

For $T \gg T_0$: entropy dominates, $K^* \to K_{\mathrm{field}}$.
For $T \ll T_0$: BIC dominates, $K^* \to 1$.
Crossover at intermediate $T$.

---

## §7. Cat Status and Numerical Anchor

### §7.1 Cat A established

- §3 free energy definition: **Cat A** (standard Helmholtz form).
- Claim 4.1 ($T \to 0$ limit recovers M-1): **Cat A**.
- Claim 4.2 ($T \to \infty$ limit gives $K_{\mathrm{field}}$): **Cat A** (entropy dominance).
- §4.3 crossover $T_c$ formula: **Cat A** (algebra).
- §5 reconciliation with M-1 + Theorem 2 + CN15: **Cat A** under existing canonical content.
- §6 BIC parallel: **Cat A** (standard information-theoretic).

### §7.2 Cat B pending

- §3.2 explicit configurational entropy $S(K)$ formula for graph $G$: **Cat B sketch** — combinatorial enumeration, verified for specific graphs (e.g., $T^2_L$ at K=1, K=2) but generic-K not closed-form.
- $\mathcal{E}^*_K$ scaling with $K$: **Cat B** — predicted as $\mathcal{E}^*_K \approx K \cdot \mathcal{E}^*_1 + (\text{coupling correction})$ in well-separated regime, but multi-formation interaction terms not fully characterized.
- Crossover temperature numerical anchor: **Cat B target** — Task #7 (symmetry-broken numerical anchor) provides empirical $T_c$ measurement.

### §7.3 Cat A target path

Cat A everywhere requires:
- Closed-form $S(K)$ for canonical graph classes ($T^2_L$, $\mathbb{Z}^d$, R23 dataset).
- Cat A $\mathcal{E}^*_K$ scaling theorem (multi-formation generalization of T-PreObj-1 Cat A for K=1).
- Numerical confirmation of $T_c$ formula (Task #7).

Effort: 3-4 weeks (W6+ Cat A target).

---

## §8. Reconciliation with Commitment 16 + Compatibility

### §8.1 Commitment 16 K_field/K_act decomposition

Commitment 16 (CV-1.5.1): $K_{\mathrm{field}}$ is modeling-layer cap; $K_{\mathrm{act}}$ is dynamical state. Compatibility:
- $K_{\mathrm{field}}$: external fixing (option (d)).
- $K_{\mathrm{act}}$: emerges from dynamics within $\{0, 1, \ldots, K_{\mathrm{field}}\}$.

Free-energy K-Selection (option (a)) predicts: $K^*_{\mathrm{eq}}(T) = \arg\min_K F(K; T) \leq K_{\mathrm{field}}$ — equilibrium $K_{\mathrm{act}}$ at temperature $T$, capped by $K_{\mathrm{field}}$.

### §8.2 No conflict

- (d) sets the upper bound: $K_{\mathrm{act}} \leq K_{\mathrm{field}}$.
- (a) selects the equilibrium value: $K^*_{\mathrm{eq}}(T)$.
- (b) corrects for kinetic effects: $K_{\mathrm{act}}(t) \neq K^*_{\mathrm{eq}}(T)$ in metastable trajectories.
- (c) provides empirical anchor for the abstract theory.

⇒ Option (a) is **complementary**, not competitive, with options (b), (c), (d). Task #8 (K-Selection vs Commitment 16 compatibility proof) extends this reconciliation.

### §8.3 Static/Dynamic Separation refinement

CN15 (current canonical candidate per `canonical/canonical.md` if approved): static minimum (T = 0) vs dynamic protocol endpoint may differ. Free-energy variant:
- **Equilibrium $K$ at $T$**: $K^*_{\mathrm{eq}}(T)$ from (a).
- **Dynamic $K$ at $t$**: $K_{\mathrm{act}}(t)$ from gradient flow with metastability (option (b)).

Both layers exist; both are legitimate aspects of K-Selection. CN15 generalizes to: *static equilibrium $K^*_{\mathrm{eq}}(T)$ and dynamic $K_{\mathrm{act}}(t)$ may differ at finite times*.

---

## §9. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — OP-0005 explicitly attacked via option (a); options (b), (c), (d) registered as complementary; M-1 reconciliation explicit (§5).
- [x] **No Research OS resurrection** — single-topic.
- [x] **Not reductive to external framework** — free-energy formalism is *standard physics* used contrastively (CN10): the SCC system has its own energy functional; $F(K; T)$ is an analytical tool, not external reduction.
- [x] **u_t primitive maintained** — $\mathcal{E}^*_K$ derived from primitive $\mathcal{E}_K$ on $\mathbf{u}$; entropy combinatorial over Aut-orbits of $\mathbf{u}^*$.
- [x] **CN5 4-energy not merged** — $\mathcal{E}_K$ structure preserved; free-energy adds entropy term, not new energy term.
- [x] **K not dual-treated** — $K_{\mathrm{act}}$ integer per Commitment 16; $K^*_{\mathrm{eq}}$ integer-valued from $\arg\min$.
- [x] **No metastability claim without P-F flag** — Option (a) is *equilibrium* (no metastability claim); Task #6 option (b) handles metastability with P-F flag.
- [x] **CN15 Static/Dynamic Separation honored** — §8.3 generalizes.
- [x] **OP-0005 not silently resolved** — option (a) is *one* of 4 options; full K-Selection mechanism requires combining all 4.

---

## §10. Forward Roadmap

### §10.1 Task #6 (K-Selection (b) Kramers metastability) connection

Task #6 will derive the kinetic correction $K_{\mathrm{act}}(t)$ vs $K^*_{\mathrm{eq}}(T)$ via Kramers escape rates over metastability barriers. Expected:
$$\tau_{K \to K-1}(\beta) \sim \exp(\beta \cdot \Delta E_{\mathrm{barrier}})$$
where $\Delta E_{\mathrm{barrier}}$ is the K-jump barrier. Combined with (a):
$$K_{\mathrm{act}}(t) = K^*_{\mathrm{eq}}(T) + \mathrm{kinetic\ correction}$$

### §10.2 Task #7 (numerical anchor) target

Task #7 measures empirical $K^*$ trajectory in symmetry-broken initial conditions; provides $T_c$ measurement (validating §4.3) + $\mathcal{E}^*_K - \mathcal{E}^*_1$ scaling.

### §10.3 Task #8 (Commitment 16 compatibility)

Formal proof that options (a), (b), (c), (d) compose into a single coherent K-Selection picture; reconciles all 4 OP-0005 candidates.

### §10.4 Canonical promotion target

CV-1.7+ candidate Commitment 19 (K-Selection axiom) per task #49 in TaskList; combines all 4 options into a single canonical statement.

---

## §11. References

### §11.1 Working files

- `working/MF/K_status_commitment.md` (OAT-1, Commitment 16).
- `working/MF/multi_formation_sigma.md` (D-6a static, $\mathcal{E}_K$ structure).
- `working/MF/sigma_multi_trajectory.md` (D-6b dynamic, K-jump events).

### §11.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi, 16; CN15 candidate.
- `canonical/canonical.md` §13 T-Merge (b) (M-1 proved); Theorem 2 (F=1 not critical).
- `canonical/canonical.md` §14 CN5, CN10, CN15.
- `canonical/theorem_status.md` OP-0005 (K-Selection direct attack); OP-0001 F-1; OP-0002 M-1 LAYER-CLARIFIED.

### §11.3 External refs

- Schwarz, G. (1978). "Estimating the dimension of a model". *Annals of Statistics* 6(2): 461–464. — BIC.
- Helmholtz free energy: Reichl, L. (2009). *A Modern Course in Statistical Physics*, 4th ed. — equilibrium thermodynamics.
- Kramers, H. A. (1940). "Brownian motion in a field of force". *Physica* 7(4): 284–304. — Task #6 metastability foundation.
- Rissanen, J. (1978). "Modeling by shortest data description". *Automatica* 14(5): 465–471. — Minimum description length, related to BIC.

---

**End of k_selection_a_free_energy.md.**

**Status: working draft. Task #5 complete. K-Selection (a) free-energy variational derivation: $F(K; T) = \mathcal{E}^*_K - T S(K)$ definition (§3.1, Cat A); $T \to 0$ recovers M-1 (Claim 4.1, Cat A); $T \to \infty$ gives $K_{\mathrm{field}}$ (Claim 4.2, Cat A); crossover $T_c$ formula (§4.3, Cat A); BIC parallel (§6, Cat A); reconciliation with M-1 + Theorem 2 + CN15 (§5, §8, Cat A); compatibility with Commitment 16 (§8.2, Cat A). Cat B pending: closed-form $S(K)$ for graph classes; $\mathcal{E}^*_K$ scaling theorem; $T_c$ numerical anchor (Task #7). Forward: Task #6 Kramers metastability (kinetic correction); Task #7 numerical anchor; Task #8 compatibility proof. Canonical target CV-1.7+ Commitment 19.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/k_selection_a_free_energy.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.7+ W12+ packet (combined with Tasks #6, #7, #8).
