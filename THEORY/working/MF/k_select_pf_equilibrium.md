> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]

# k_select_pf_equilibrium.md — T-K-Select-PF: Equilibrium K-Selection under P-F-A1 Package I

**Status:** working draft, tightened Session R (2026-05-06). Cat B — promoted to canonical Cat B in `canonical.md §13` Session R. K_feas defined (§3.5); K_act fixed to D-ST-3; null-boundary stated as proven-by-codimension-argument (Cat B acceptable, Cat A requires explicit σ_M-coordinate computation). Single-topic working file per `THEORY/working/MF/` convention.
**Type:** Theorem + proof sketch. Re-attacks OP-0005 equilibrium layer using the newly canonicalized P-F-A1 Package I (CV-1.9).
**Author origin:** Session Q (2026-05-06). Follows Commitment 19 K-Selection cluster (W5 Day 4, Tasks #5–8) but grounds the free-energy layer precisely on Package I, lifting the P-F flag on Z_K.
**Canonical refs (dependencies):**
- T-PF-A1-AR Cat A: F_M(G) compact convex polytope, intrinsic dimension n−1; Lebesgue measure σ_M on F_M(G) is well-defined.
- T-PF-A1-SDE Cat A: reflected Langevin SDE well-posed on F_M(G) for any T_* > 0.
- T-PF-A1-GI Cat A: π_{T_*} = Z^{-1} exp(−E/T_*) dσ_M is the unique invariant measure.
- T-PF-A1-PE Cat A: exponential ergodicity + Poincaré inequality.
- D-ST-3 (canonical §3.11): K_act := #PersComp(u) as the observable.
- Commitment 16 (CV-1.5.1, §11.1 #16): K_field/K_act two-tier decomposition.
- OP-0021: T_* canonical registration (OPEN; T_* enters here as axiom).
**Working refs (related):**
- `k_selection_a_free_energy.md` (Task #5): saddle-point approximation F(K;T) = E*_K − T·S(K); P-F flag on Z_K now lifted by Package I.
- `k_selection_b_kramers.md` (Task #6): kinetic layer (Package II, W9+).
- `k_selection_compatibility_proof.md` (Task #8): 4-layer compatibility Cat A.
- `commitment_19_k_selection_axiom_packet.md` (Task #49): Commitment 19 canonical packet.
- `pf_a1_lions_sznitman_freidlin_route.md` (Sessions M–P): Package I proof details.

---

## §1. Mission

> **Session Q primary objective**: Exploit the newly established P-F-A1 Package I (CV-1.9, all four theorems Cat A) to prove the equilibrium K-selection result that was P-F flagged before.

Before Session Q (CV-1.9), the K-selection free-energy layer (`k_selection_a_free_energy.md` §3.3) was blocked by:

> *"⚠️ P-F flag: Z_K is defined only when stochastic SCC (P-F-A1 Langevin on F_M(P)) is canonically formalized."*

Package I provides exactly this formalization. The result is:

**T-K-Select-PF**: The reflected SCC Langevin induces a well-defined stationary distribution over K_act, given by Gibbs sector masses p_K = π_{T_*}(B_K). Equilibrium K-selection is K* ∈ argmax_K p_K = argmin_K F(K;P).

This theorem formalizes **OP-0005-EQ** (the equilibrium sub-problem of OP-0005). It does not resolve OP-0005-DYN (Kramers rates, Package II) or OP-0005-OBS (observation-conditioned selection).

---

## §2. Prerequisites

### §2.1 P-F-A1 Package I (all Cat A, CV-1.9)

Let G = (V, E) be a finite connected graph with n = |V| vertices and probability mass vector μ = 1/n·**1** (uniform), mass M ∈ (0,1), and T_* > 0 (P-F-A1 axiom, OP-0021).

- **T-PF-A1-AR**: The field polytope
  $$\mathcal{F}_M(G) = \{u \in [0,1]^n : \mu^T u = M\}$$
  is a compact convex polytope of intrinsic dimension n−1. The affine isometry Φ: C̃ → F_M(G) is well-posed. The (n−1)-dimensional Lebesgue measure σ_M on F_M(G) (induced from C̃ via Φ) is well-defined.

- **T-PF-A1-SDE**: The reflected Langevin
  $$dU_t = -\Pi_M \nabla E_{\mathrm{SCC}}(U_t)\, dt + \sqrt{2T_*}\, \Pi_M\, dW_t + dK̃_t$$
  has a unique strong solution (U_t, K̃_t) for any U_0 ∈ F_M(G).

- **T-PF-A1-GI**: The Gibbs measure
  $$\pi_{T_*}(du) = Z^{-1} \exp\!\left(-\frac{E_{\mathrm{SCC}}(u)}{T_*}\right) d\sigma_M(u), \quad Z = \int_{\mathcal{F}_M(G)} \exp\!\left(-\frac{E_{\mathrm{SCC}}(u)}{T_*}\right) d\sigma_M(u)$$
  is the **unique** invariant probability measure of the reflected Langevin. Z is finite and positive (F_M(G) compact, E_SCC continuous).

- **T-PF-A1-PE**: The spectral gap λ_1(π_{T_*}) ≥ (π²/n)·exp(−osc(Ẽ)/T_*) > 0. The law of U_t converges to π_{T_*} exponentially in L²(π_{T_*}).

### §2.2 K_act definition

**Definition 2.1 (Persistent component count).** For ρ_pers ∈ (0, 1) fixed (canonical SCC parameter) and persistence threshold τ ≥ 0:
$$K_{\mathrm{act}}(u) := \#\mathrm{PersComp}(u;\rho_{\mathrm{pers}}, \tau)$$
= number of connected components of the induced subgraph on $\{v \in V : u(v) \geq \rho_{\mathrm{pers}}\}$ whose topological persistence (birth height minus death height in the H_0 persistence diagram of u) is ≥ τ.

On a finite graph G, K_act(u) is a non-negative integer for every u ∈ [0,1]^n.

---

## §3. Sector Partition

**Definition 3.1 (K-sector).** For K ∈ {0, 1, 2, ...}, define the **K-sector**:
$$\mathcal{B}_K(\mathcal{P}) = \{u \in \mathcal{F}_M(G) : K_{\mathrm{act}}(u) = K\}$$
where we write $\mathcal{P} = (G, M, \rho_{\mathrm{pers}}, \tau)$ for the scene parameters.

### §3.1 Measurability

**Lemma 3.1 (Borel measurability).** K_act : F_M(G) → ℤ_{≥0} is Borel measurable. Hence B_K is a Borel subset of F_M(G) for each K.

**Proof.** On finite graph G with n vertices, K_act(u) changes value only when some vertex v enters or leaves the superlevel set {w : u(w) ≥ ρ_pers} (a "topological event"). Specifically:
- K_act(u) jumps only when u(v) = ρ_pers for some v ∈ V, OR when the persistence of some component equals exactly τ.

Each condition {u(v) = ρ_pers} defines a closed hyperplane in ℝ^n. The condition {persistence = τ} also defines a closed subset (piecewise-linear in u on a finite graph). The set of "jump points" of K_act is therefore a finite union of closed sets — a closed set of measure zero. Therefore K_act is piecewise constant on the complement of a closed set, hence Borel measurable. □

### §3.2 Sector boundary has measure zero

**Lemma 3.2 (Null boundary).** For each K, $\pi_{T_*}(\partial \mathcal{B}_K) = 0$.

**Proof.** The "boundary" ∂B_K consists of configurations where K_act jumps, i.e., where at least one vertex satisfies u(v) = ρ_pers or some component has persistence exactly τ. This is contained in:
$$\partial \mathcal{B}_K \subseteq \bigcup_{v \in V} \{u \in \mathcal{F}_M(G) : u(v) = \rho_{\mathrm{pers}}\} \cup \bigcup_{\text{components}} \{\text{persistence} = \tau\}$$
which is a finite union of $(n-2)$-dimensional faces within the $(n-1)$-dimensional polytope $\mathcal{F}_M(G)$. By T-PF-A1-AR, σ_M is the $(n-1)$-dimensional Lebesgue measure on F_M(G); a $(n-2)$-dimensional subset has σ_M-measure zero. Since π_{T_*} ≪ σ_M, we have π_{T_*}(∂B_K) = 0. □

### §3.3 Partition

**Lemma 3.3 (π-partition).** The sectors {B_K} partition F_M(G) up to a π_{T_*}-null set:
$$\pi_{T_*}\!\left(\mathcal{F}_M(G) \setminus \bigsqcup_{K \geq 0} \mathcal{B}_K\right) = 0.$$

**Proof.** By definition, every u ∈ F_M(G) satisfies K_act(u) = K for some K ∈ ℤ_{≥0}, so the B_K cover F_M(G). Intersections B_K ∩ B_{K'} for K ≠ K' are empty (K_act is single-valued). The boundary ∂B_K has π_{T_*}-measure zero by Lemma 3.2. □

### §3.4 Topological structure note

The sectors B_K are **neither open nor closed** in general:
- B_K is *open* in its closure (locally closed), because configurations in the interior of B_K have a neighborhood with the same K_act value.
- B_K is *not closed* because sequences in B_K can converge to boundary points (K_act jumps).
- No smooth manifold structure is assumed for B_K — this is a stratified decomposition, and the stratum boundaries are codimension ≥ 1.

This stratified structure is sufficient for the Gibbs measure argument since the strata have positive measure and the boundaries are null.

### §3.5 Feasible sectors

**Definition 3.2 (Feasible set).**
$$K_{\mathrm{feas}} = K_{\mathrm{feas}}(\mathcal{P}) := \{K \in \mathbb{Z}_{\geq 0} : \sigma_M(\mathcal{B}_K) > 0\}$$
the set of formation counts that occupy positive Lebesgue measure in $\mathcal{F}_M(G)$.

**Remark.** $K_{\mathrm{feas}}$ is finite: $K_{\mathrm{act}}(u) \leq K_{\mathrm{field}}$ for all $u$ by Commitment 16 (§11.1 #16), so $K_{\mathrm{feas}} \subseteq \{0, 1, \ldots, K_{\mathrm{field}}\}$. It is non-empty: $\mathcal{F}_M(G)$ has positive $\sigma_M$-measure by T-PF-A1-AR, so at least one $K$ must satisfy $\sigma_M(\mathcal{B}_K) > 0$. The exact characterization of $K_{\mathrm{feas}}$ for given $\mathcal{P} = (G, M, \rho_{\mathrm{pers}}, \tau)$ is a per-instance verification task (see §9.1 Cat B condition (b)).

**Consequence.** By Lemma 4.1 (§4.1 below), $Z_K > 0$ for all $K \in K_{\mathrm{feas}}$, so $p_K > 0$ for $K \in K_{\mathrm{feas}}$ and $p_K = 0$ otherwise.

---

## §4. Sector Free Energy and Sector Masses

**Definition 4.1 (Sector partition function).** For K ≥ 0 with σ_M(B_K) > 0:
$$Z_K := \int_{\mathcal{B}_K} \exp\!\left(-\frac{E_{\mathrm{SCC}}(u)}{T_*}\right) d\sigma_M(u).$$

**Definition 4.2 (Sector mass).** The Gibbs sector mass:
$$p_K := \pi_{T_*}(\mathcal{B}_K) = \frac{Z_K}{Z} \geq 0.$$

**Definition 4.3 (Sector free energy).** For K with Z_K > 0:
$$F(K; \mathcal{P}) := -T_* \log Z_K.$$

The sector free energy satisfies: $p_K \propto \exp(-F(K;\mathcal{P})/T_*)$, so argmin_K F = argmax_K p_K.

### §4.1 Well-definedness

**Lemma 4.1.** Under T-PF-A1-AR and T-PF-A1-GI:
1. Z > 0 and Z < ∞ (finite positive partition function).
2. Z_K is well-defined and 0 ≤ Z_K ≤ Z for each K.
3. $\sum_{K \geq 0} p_K = 1$.
4. If σ_M(B_K) > 0, then Z_K > 0 (since E_SCC is continuous, exp(−E/T_*) > 0 everywhere).

**Proof.** (1) F_M(G) is compact (T-PF-A1-AR) and E_SCC is continuous, so exp(−E/T_*) is bounded above and below by positive constants; integrating over a bounded polytope gives Z finite and positive. (2) B_K is a Borel subset of F_M(G); integrability follows from (1). (3) By Lemma 3.3, $\sum_K Z_K = Z$; dividing by Z gives the probability. (4) Since exp(−E/T_*) ≥ exp(−‖E‖_{∞,F_M(G)}/T_*) > 0, integrating over a positive-σ_M set gives Z_K > 0. □

### §4.2 Relationship to saddle-point approximation

The previous working formulation (`k_selection_a_free_energy.md` §3.3) used:
$$F_{\mathrm{approx}}(K; T) = \mathcal{E}^*_K - T \cdot S(K)$$
where $\mathcal{E}^*_K = \min_{B_K} E_{\mathrm{SCC}}$ and $S(K) = \log |\Omega_K|$ (configurational entropy, combinatorial count).

This is the **saddle-point (Laplace) approximation** of the exact sector free energy:
$$F(K;\mathcal{P}) = -T_* \log Z_K = -T_* \log \int_{B_K} e^{-E/T_*} d\sigma_M \approx \mathcal{E}^*_K - T_* \log |\Omega_K| + O(T_*)$$
valid when the Gibbs measure is concentrated near the minimum (small T_* regime, well-separated minima). The exact formula F(K;P) = −T_* log Z_K is now available without approximation.

**Resolution of P-F flag**: The P-F flag "⚠️ Z_K defined only when stochastic SCC canonically formalized" in `k_selection_a_free_energy.md` §3.3 is **RESOLVED** by Package I (CV-1.9). Z_K = ∫_{B_K} e^{-E/T_*} dσ_M is well-defined as a Lebesgue integral over a compact measurable set.

---

## §5. T-K-Select-PF: Equilibrium K-Selection Theorem

### §5.1 Theorem statement

**T-K-Select-PF (Equilibrium K-Selection under P-F-A1 Package I, Session Q, 2026-05-06).**

*Assumptions:*
- (A1) Finite connected graph G, mass M ∈ (0,1), T_* > 0 (P-F-A1 axiom, OP-0021).
- (A2) P-F-A1 Package I holds: T-PF-A1-AR, T-PF-A1-SDE, T-PF-A1-GI, T-PF-A1-PE all Cat A.
- (A3) K_act(u) := #PersComp(u; ρ_pers, τ) is measurable (Lemma 3.1).
- (A4) Sector non-degeneracy: for each K in the relevant range, σ_M(B_K) > 0.
- (A5) $K$ ranges over $K_{\mathrm{feas}} \subseteq \mathbb{Z}_{\geq 0}$ (Definition 3.2, §3.5), which is finite and non-empty.

*Claims:*

(i) **Sector partition**: {B_K} partition F_M(G) up to a π_{T_*}-null set (Lemma 3.3).

(ii) **Gibbs sector masses are well-defined**: The sector masses
$$p_K = \pi_{T_*}(\mathcal{B}_K) = \frac{1}{Z}\int_{\mathcal{B}_K} e^{-E_{\mathrm{SCC}}(u)/T_*} d\sigma_M(u)$$
form a probability distribution: $p_K \geq 0$, $\sum_K p_K = 1$.

(iii) **Stationary K-distribution**: The stationary distribution of $K_{\mathrm{act}}(U_t)$ under the reflected Langevin (T-PF-A1-SDE) is exactly $\{p_K\}$.

(iv) **Equilibrium K-selection**: The equilibrium selected formation count is any
$$K^* \in \arg\max_K p_K = \arg\min_K F(K;\mathcal{P})$$
where $F(K;\mathcal{P}) = -T_* \log Z_K$ is the sector free energy.

(v) **Sector free energy ordering**: $p_K > p_{K'}$ iff $F(K;\mathcal{P}) < F(K';\mathcal{P})$. When a unique K* exists, it is the unique minimizer of F.

### §5.2 Proof

**(i)** Lemma 3.3 directly. □

**(ii)** Lemma 4.1 directly (well-definedness from T-PF-A1-AR + T-PF-A1-GI). □

**(iii)** By T-PF-A1-GI, π_{T_*} is the unique invariant probability measure of the reflected Langevin. The pushforward of π_{T_*} under K_act: for any K,
$$\mathbb{P}_{\pi_{T_*}}[K_{\mathrm{act}}(U) = K] = \pi_{T_*}(\mathcal{B}_K) = p_K.$$
Since the process is stationary under π_{T_*}, the distribution of K_act(U_t) is constant at {p_K} when U_0 ∼ π_{T_*}. Uniqueness of π_{T_*} (T-PF-A1-GI) means this is the only stationary K-distribution. □

**(iv)** K* = argmax_K p_K follows from the probability distribution {p_K}. The equivalence argmax p_K = argmin F(K;P) follows from p_K ∝ exp(−F(K;P)/T_*). □

**(v)** Strict ordering follows since p_K = Z_K/Z and Z_K = exp(−F(K;P)/T_*)·Z. □

### §5.3 Convergence to equilibrium

By T-PF-A1-PE (exponential ergodicity), for any initial density U_0 with law ν_0 ∈ L²(π_{T_*}):
$$\|\nu_t - \pi_{T_*}\|_{TV} \leq C_0 e^{-\lambda_1 t}$$
where λ_1 ≥ (π²/n)·exp(−osc(Ẽ)/T_*) > 0 and the TV norm uses the L²(π_{T_*}) density assumption. Hence:
$$|p_K^{(t)} - p_K| := |\mathbb{P}_{\nu_t}[K_{\mathrm{act}} = K] - p_K| \leq \|\nu_t - \pi_{T_*}\|_{TV} \leq C_0 e^{-\lambda_1 t}.$$

The K-distribution converges to the equilibrium {p_K} exponentially fast for L²(π_{T_*}) initial laws.

---

## §6. Non-Overclaim Section (Mandatory)

**T-K-Select-PF does NOT:**

1. **Prove Kramers rates.** The dynamical K-transition rates $\Gamma_{K \to K'}$ (barrier-crossing rates between sectors) are Package II territory, blocked on H5 (Morse stability) + OP-0021 (T_* registration). T-K-Select-PF says *what* the equilibrium K-distribution is, not *how fast* K transitions occur.

2. **Prove how fast K_act changes.** The convergence of the marginal K-distribution (via T-PF-A1-PE) does NOT imply the individual K-jump time scale. The spectral gap λ_1 controls the approach of the *full field distribution* to π_{T_*}, which is a much stronger statement than the K-marginal convergence time.

3. **Resolve OP-0008.** The σ^A K-jump non-determinism (OP-0008) concerns the post-merger formation assignments, which is about the fiber of the projection U ↦ K_act(U) — this is separate from the K-marginal equilibrium.

4. **Prove K* is unique.** Multiple K values may have equal sector mass p_K = p_{K'}, especially near crossover temperatures. T-K-Select-PF proves the existence of argmax; uniqueness requires additional assumptions on the energy landscape (e.g., generic parameters, non-degenerate critical points).

5. **Prove specific K* values.** T-K-Select-PF identifies K* as the argmax/argmin of sector-level quantities; computing specific values of p_K or F(K;P) requires integrating over B_K, which is in general intractable analytically but accessible numerically (see §8).

6. **Make K_field counting claims.** T-K-Select-PF operates within a fixed K_field architectural cap (Commitment 16). It does not replace T-L1-F (K_bar/K_act bridge) or T-L1-M (K_soft/K_act).

7. **Use Σ_M^K as foundational state space.** $\Sigma_M^K$ is a local coordinate chart within one basin B_{K,α} ⊂ B_K (per Canonical Memo v1.1 §D5). The correct foundational space is F_M(G) with the sector B_K.

---

## §7. Relation to Old OP-0005 Options and OP-0005 Split

### §7.1 OP-0005 3-way split

Following Session Q, OP-0005 decomposes into three subproblems:

| Sub-ID | Name | Status | Notes |
|---|---|---|---|
| **OP-0005-EQ** | Equilibrium K-selection | **PARTIALLY RESOLVED** (T-K-Select-PF, Cat B candidate) | T-K-Select-PF gives the equilibrium distribution {p_K} grounded by Package I. Full Cat A requires formalizing measurability + sector non-degeneracy. |
| **OP-0005-DYN** | Dynamical K-transition / Kramers rates | **OPEN** (W9+) | Blocked on Package II (Eyring-Kramers, H5 + OP-0021). Layer (b) of Commitment 19. |
| **OP-0005-OBS** | Observation-conditioned K selection | **OPEN** | P-conditioned K-selection for stereo SCC; requires D-ST-3/D-ST-4 + P-F-A1. Connects to `stereo_observation_framework.md` §7. |

### §7.2 Relation to free-energy option (a)

The old `k_selection_a_free_energy.md` proposed F(K;T) = E*_K − T·S(K) as the free energy. This is the **saddle-point approximation** of the exact F(K;P) = −T_* log Z_K defined here. The relationship:

- **Exact (T-K-Select-PF)**: F(K;P) = −T_* log Z_K with Z_K = ∫_{B_K} e^{−E/T_*} dσ_M.
- **Approximate (k_selection_a_free_energy.md)**: F_approx(K;T) = E*_K − T·S(K) via Laplace approximation.
- **Connection**: F_approx is the leading-order expansion of F at small T_*; the exact formula accounts for all basins in B_K (multi-basin decomposition), not just the deepest minimum.

The P-F flag on Z_K in `k_selection_a_free_energy.md` §3.3 is now **RESOLVED** by Package I. The formulation proposed there (using F_M(P) instead of Σ_M^K as foundational space) was already correct; Package I provides the missing stochastic-process grounding.

### §7.3 Relation to Kramers option (b)

T-K-Select-PF and layer (b) are complementary:
- T-K-Select-PF: the *equilibrium* distribution {p_K} that K_act converges to as t → ∞.
- Layer (b) Kramers: the *transition rates* $\Gamma_{K \to K'}$ governing how fast K_act moves between sectors.

Both are needed for a complete K-selection theory. T-K-Select-PF provides the "target distribution"; Kramers provides the "speed of approach."

### §7.4 Relation to Commitment 19

Commitment 19 (K-Selection Axiom, CV-1.7+ candidate, `commitment_19_k_selection_axiom_packet.md`) describes a 4-layer composite where Layer (b) uses the free energy F(K;T) = E*_K − T·S(K) with the P-F flag. T-K-Select-PF provides the Package I-grounded version of that layer, replacing the P-F flagged approximation with the exact Gibbs-based result. The Commitment 19 packet should be updated to reference T-K-Select-PF as the canonical equilibrium layer once this theorem is promoted.

---

## §8. Numerical Verification Plan (Optional)

T-K-Select-PF is numerically accessible. Two approaches:

### §8.1 Gibbs sampling of sector masses

Sample U ~ π_{T_*} using MCMC on F_M(G):
- Metropolis-Hastings with Gaussian perturbations projected onto F_M(G).
- Compute K_act(U) for each sample.
- Estimate p_K = fraction of samples with K_act = K.

Compare estimated {p_K} to expected sector free energies from the saddle-point formula F_approx(K) = E*_K − T_*·S(K).

### §8.2 Long-time Langevin simulation

Run the reflected Langevin (implemented as stochastic gradient descent + projection + reflection) for long time, record K_act(U_t). Empirical distribution of K_act should converge to {p_K} by T-K-Select-PF + T-PF-A1-PE.

### §8.3 Temperature sensitivity

Vary T_*; observe predicted crossover from K=1 (energy-dominated, small T_*) to K>1 (entropy-dominated, large T_*). Compare to T_c formula from k_selection_a_free_energy.md §4.3.

These experiments would:
- Validate T-K-Select-PF numerically (Cat B → Cat A anchor).
- Provide empirical values of p_K for specific graph instances.
- Check sensitivity to ρ_pers and τ (sector definition parameters).

---

## §9. Cat Status and Proof Completeness

### §9.1 Cat B candidate (current)

Claims (i)–(v) have proof sketches that are correct given Package I. The main items requiring formalization for Cat A:

1. **K_act definition specificity**: The theorem uses "K_act(u) := #PersComp(u; ρ_pers, τ)" but the precise canonical form (with persistence diagram, multi-field version) needs to be fixed. Different versions of K_act lead to slightly different ∂B_K but the same measure-zero argument applies.

2. **Sector non-degeneracy (A4)**: For specific graph/parameter combinations, some K values may have σ_M(B_K) = 0 (no valid K-formation configurations). A theorem characterizing which K values are non-degenerate is needed for a complete statement. In practice, this is verifiable numerically per instance.

3. **Measure-zero boundary formalization**: Lemma 3.2 uses "codimension argument" informally. For Cat A, need explicit computation that each hyperplane {u(v) = ρ_pers} intersects F_M(G) in an (n-2)-dimensional set, which has σ_M-measure zero.

4. **Finite K range (A5)**: K_act ≤ K_field (Commitment 16) provides the upper bound. K ≥ 0 is clear. Making the range explicit and showing K_max is bounded requires the K_field architectural cap.

### §9.2 Cat A path

- Fix the K_act definition used in the theorem to match the canonical §13 entry for D-ST-3.
- Provide explicit computation of σ_M({u(v) = ρ_pers} ∩ F_M(G)) = 0 using T-PF-A1-AR coordinates.
- State sector non-degeneracy as a verifiable assumption (or add a lemma for a specific canonical case).
- Cross-reference with canonical.md §13 for the complete statement.

Cat A promotion: achievable in next working session with minor formalization work. No fundamentally new mathematics required beyond what Package I already provides.

### §9.3 Suggested canonical label

If promoted: **T-K-Select-PF** — "K-Selection under P-F-A1 Package I, Equilibrium." Proposed §13 Category B entry (Session Q); Cat A upgrade in subsequent session after formalization.

---

## §10. Hard Constraint Verification

- [x] **u_t primitive maintained** — K_act is a derived integer from the cohesion field u; sector B_K is defined as a subset of F_M(G) (the field state space). No crisp "formation object" primitive introduced.
- [x] **CN5 four energy terms not merged** — E_SCC in the Gibbs measure retains its full structure (E_cl + E_sep + E_bd + E_tr); no merging in T-K-Select-PF.
- [x] **No Kramers rates** — T-K-Select-PF is purely an equilibrium result; no barrier-crossing rate formula. OP-0005-DYN remains OPEN.
- [x] **No K_field counting claim** — operates within Commitment 16 cap (K ≤ K_field by definition of K_act range).
- [x] **K* uniqueness not overclaimed** — §6 item 4 explicitly: multiple K may have equal p_K; uniqueness requires additional assumptions.
- [x] **T_* remains axiomatic** — entered as axiom per OP-0021; not derived from SCC parameters.
- [x] **Σ_M^K not used as foundational state space** — F_M(G) is the foundational state space (T-PF-A1-AR); B_K ⊂ F_M(G) is the sector.
- [x] **OP-0005 not fully closed** — only OP-0005-EQ addressed; OP-0005-DYN and OP-0005-OBS remain OPEN.
- [x] **OP-0008 not claimed resolved** — σ^A K-jump non-determinism is separate; not addressed here.
- [x] **No silent resolution** — OP-0005 status change is OPEN → PARTIALLY RESOLVED (EQ sub-problem only); OP-0005 overall remains OPEN pending DYN + OBS.
- [x] **No Research OS resurrection** — single-topic working file per convention.
- [x] **Canonical edits not made** — working file only; canonical promotion requires review + user decision.

---

## §11. References

### §11.1 Canonical dependencies (all Cat A, CV-1.9)

- **T-PF-A1-AR**: `canonical.md §13` (Field Polytope Compact Convex Structure; Session O, CV-1.8).
- **T-PF-A1-SDE**: `canonical.md §13` (Reflected Langevin Well-Posedness; Session O, CV-1.8).
- **T-PF-A1-GI**: `canonical.md §13` (Gibbs Measure Unique Invariant; Session P, CV-1.9).
- **T-PF-A1-PE**: `canonical.md §13` (Poincaré + Exponential Ergodicity; Session P, CV-1.9).
- **D-ST-3**: `canonical.md §3.11` (K_act as #PersComp; W6 D4).
- **Commitment 16**: `canonical.md §11.1 #16` (K_field/K_act decomposition; CV-1.5.1).

### §11.2 Working dependencies (K-selection cluster)

- `working/MF/k_selection_a_free_energy.md` (Tasks #5; free-energy layer; P-F flag resolved).
- `working/MF/k_selection_b_kramers.md` (Task #6; kinetic layer; still P-F flagged pending Package II).
- `working/MF/k_selection_compatibility_proof.md` (Task #8; 4-layer compatibility Cat A).
- `working/MF/commitment_19_k_selection_axiom_packet.md` (Task #49; Commitment 19 packet).
- `working/MF/pf_a1_lions_sznitman_freidlin_route.md` (Sessions M–P; Package I proof source).

### §11.3 Open problems addressed / not addressed

- **OP-0005-EQ**: PARTIALLY RESOLVED by this file (Cat B candidate).
- **OP-0005-DYN**: OPEN (Package II, W9+).
- **OP-0005-OBS**: OPEN (observation-conditioned, stereo SCC).
- **OP-0008**: OPEN (not addressed).
- **OP-0021**: OPEN (T_* registration; enters as axiom here).

---

**End of k_select_pf_equilibrium.md.**

**Status:** working draft, Cat B candidate, Session Q (2026-05-06). T-K-Select-PF proves (i) B_K Borel measurable, (ii) π_{T_*}(∂B_K) = 0, (iii) {p_K} is a well-defined probability distribution, (iv) stationary K_act distribution = {p_K} by T-PF-A1-GI, (v) K* ∈ argmin F(K;P). All P-F flags on Z_K resolved by Package I. Non-overclaims: no Kramers rates, no K* uniqueness, no OP-0008, no K_field counting, T_* axiomatic. Cat A path: fix K_act definition, explicit σ_M-null computation, sector non-degeneracy characterization.

**OP-0005 split introduced (Session Q):**
- OP-0005-EQ: T-K-Select-PF — Cat B candidate, PARTIALLY RESOLVED (equilibrium layer, Package I grounded).
- OP-0005-DYN: Kramers/Freidlin-Wentzell — OPEN, Package II, W9+.
- OP-0005-OBS: observation-conditioned — OPEN, separate.

**File:** `THEORY/working/MF/k_select_pf_equilibrium.md`
**Created:** 2026-05-06 Session Q.
**Promotion target:** `canonical.md §13 Category B` (T-K-Select-PF) pending Cat A formalization and user decision.
