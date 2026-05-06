# k_select_obs_posterior.md — T-K-Select-OBS: Observation-Conditioned K-Selection via Posterior Sector Mass

**Status:** working draft, Cat B candidate. Session S (2026-05-06) initial draft. Session T (2026-05-06) review: Cat B status confirmed; §3.5 K_feas^obs tightening added; no overclaims. Single-topic working file per `THEORY/working/MF/` convention.
**Type:** Theorem + proof sketch. Attacks OP-0005-OBS using T-K-Select-PF (canonical Cat B, CV-1.10) + P-F-A1 Package I (all Cat A, CV-1.9) + an explicit observation likelihood model.
**Author origin:** Session S (2026-05-06). Follows `stereo_observation_framework.md` (W6 D2 evening, working draft) which defines the full observation layer including $\mathfrak{O}_t$, $b_t$, and prior/likelihood separation. Extends T-K-Select-PF (OP-0005-EQ) to the observation-conditioned setting (OP-0005-OBS).
**Canonical refs (dependencies):**
- T-PF-A1-AR Cat A: $\mathcal{F}_M(G)$ compact convex polytope; $\sigma_M$ well-defined.
- T-PF-A1-GI Cat A: $\pi_{T_*} = Z^{-1}e^{-E/T_*}d\sigma_M$ unique invariant; $\pi_{T_*} \ll \sigma_M$.
- T-K-Select-PF Cat B: $\{p_K = \pi_{T_*}(\mathcal{B}_K)\}$ prior sector masses; $K_\mathrm{feas}$ defined.
- D-ST-3 (canonical §3.11): $K_\mathrm{act}$ as $\#\mathrm{PersComp}(u;\rho_\mathrm{pers},\tau)$.
- D-ST-5 (canonical §16): $b_t : X_L^\mathrm{valid} \to \mathcal{P}_t$ backprojection; prior/likelihood separation.
- OP-0021: $T_*$ axiomatic.
**Working refs (related):**
- `stereo_observation_framework.md` (W6 D2 evening): full stereo observation layer, MAP structure, CN5 compliance, BO + Kramers framework.
- `k_select_pf_equilibrium.md` (Sessions Q–R, CV-1.10): prior sector mass theorem (parent result).
- `k_selection_a_free_energy.md` (Task #5): saddle-point approximation of sector free energy.
- `stereo_scc_canonical_memo_v1.1.md`: canonical stereo memo with full $\mathfrak{O}_t$ definition.

---

## §1. Mission

**Session S primary objective:** Define observation-conditioned K-selection for OP-0005-OBS.

T-K-Select-PF (CV-1.10, Cat B) gives the *prior* K-distribution $\{p_K\}$ under the equilibrium Gibbs measure $\pi_{T_*}$. But in stereo SCC, the system is not in free equilibrium — it observes scene data $\mathfrak{O}_t$. The observation should shift the K-distribution toward the K consistent with the data.

**Core idea (Bayesian K-selection):**

$$\underbrace{p_K}_{\text{prior (T-K-Select-PF)}} \xrightarrow{\text{Bayes}} \underbrace{p_K(\mathfrak{O}_t)}_{\text{posterior}} \;=\; \frac{\displaystyle\int_{\mathcal{B}_K} \mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)\,e^{-E(u)/T_*}\,d\sigma_M(u)}{\displaystyle\int_{\mathcal{F}_M(G)} \mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)\,e^{-E(u)/T_*}\,d\sigma_M(u)}$$

The prior $\{p_K\}$ (T-K-Select-PF) is a special case when $\mathcal{L}_\mathrm{obs} \equiv 1$ (no observation).

This theorem formalizes **OP-0005-OBS** (the observation-conditioned sub-problem of OP-0005). It does not resolve OP-0005-DYN (Kramers rates, Package II) or OP-0005-EQ (already Cat B via T-K-Select-PF).

---

## §2. Prerequisites

### §2.1 P-F-A1 Package I (all Cat A, CV-1.9) — inherited from T-K-Select-PF

- **T-PF-A1-AR**: $\mathcal{F}_M(G)$ compact convex polytope of intrinsic dimension $n-1$; $\sigma_M$ (Lebesgue on $\mathcal{F}_M(G)$) well-defined.
- **T-PF-A1-GI**: $\pi_{T_*} = Z^{-1}e^{-E_\mathrm{SCC}(u)/T_*}d\sigma_M(u)$ unique invariant; $Z$ finite positive.

### §2.2 T-K-Select-PF (Cat B, CV-1.10) — parent theorem

For K-sectors $\mathcal{B}_K = \{u \in \mathcal{F}_M(G) : K_\mathrm{act}(u) = K\}$ and feasible set $K_\mathrm{feas} = \{K : \sigma_M(\mathcal{B}_K) > 0\}$:
- $\pi_{T_*}(\partial\mathcal{B}_K) = 0$ (null boundary).
- Prior sector masses $p_K = Z_K/Z$, $Z_K = \int_{\mathcal{B}_K}e^{-E/T_*}d\sigma_M$, form a probability distribution on $K_\mathrm{feas}$.

### §2.3 Observation likelihood model

**Definition 2.1 (Observation tuple).** Following `stereo_observation_framework.md` §3.2:
$$\mathfrak{O}_t = (f_L,\, f_R,\, \Pi_{LR},\, b_L,\, b_R,\, c)$$
- $f_L : X_L \to \mathbb{R}^d$, $f_R : X_R \to \mathbb{R}^d$: left/right appearance (pixel or feature) fields.
- $\Pi_{LR} : X_L \rightharpoonup X_R$: stereo correspondence (partial map).
- $b_L = b_t : X_L^\mathrm{valid} \rightharpoonup \mathcal{P}_t$: backprojection from valid left pixels to 3D point cloud (D-ST-5, §16).
- $b_R$: right backprojection (symmetric).
- $c : X_L \to [0,1]$: disparity confidence mask.

For an abstract (non-stereo-specific) formulation, $\mathfrak{O}_t$ may be taken as any observation that is external to the SCC prior.

**Definition 2.2 (Observation likelihood).** The likelihood $\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)$ is the probability of observing $\mathfrak{O}_t$ given latent cohesion field $u \in \mathcal{F}_M(G)$.

Canonical form (stereo, CN5-compliant):
$$\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u) = \exp\!\left(-\Phi_\mathrm{obs}(u;\mathfrak{O}_t)\right)$$

where the **observation energy** (negative log-likelihood):
$$\Phi_\mathrm{obs}(u;\mathfrak{O}_t) = \lambda_\mathrm{photo}\sum_{x_L \in X_L^\mathrm{valid}} c(x_L)\,\Psi\!\bigl(f_L(x_L),\,f_R(\Pi_{LR}(x_L)),\,u(b_L(x_L))\bigr)$$

with $\Psi \geq 0$ a photometric consistency measure (e.g., $\Psi = \|f_L - f_R\|^2$). $\Phi_\mathrm{obs}$ does NOT enter $E_\mathrm{SCC}$ — it is in the likelihood, not the prior (CN5).

**Likelihood model conditions (LM1–LM3):**
- **(LM1) Measurability:** $u \mapsto \mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)$ is Borel measurable on $\mathcal{F}_M(G)$ for each fixed $\mathfrak{O}_t$.
- **(LM2) Positivity:** $\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u) > 0$ for all $u \in \mathcal{F}_M(G)$. (Equivalent: $\Phi_\mathrm{obs}(u;\mathfrak{O}_t) < +\infty$ for all $u$.)
- **(LM3) Posterior normalizability:** $Z^{obs}(\mathfrak{O}_t) = \int_{\mathcal{F}_M(G)} \mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)\,e^{-E(u)/T_*}\,d\sigma_M(u) > 0$.

*Remark.* LM1–LM3 hold automatically when $\Phi_\mathrm{obs}$ is continuous and bounded (as for the photometric form above, since $\mathcal{F}_M(G)$ is compact by T-PF-A1-AR). LM2 means no observation evidence is infinitely decisive. LM3 is implied by LM2 (positive integrand over positive-measure set) + T-PF-A1-AR compactness.

---

## §3. Posterior Measure and Sector Masses

**Definition 3.1 (Observation-conditioned posterior).** Under LM1–LM3:
$$\pi_t^{obs}(du) = \bigl(Z^{obs}\bigr)^{-1}\,\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)\,e^{-E_\mathrm{SCC}(u)/T_*}\,d\sigma_M(u)$$

where:
$$Z^{obs}(\mathfrak{O}_t) = \int_{\mathcal{F}_M(G)} \mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)\,e^{-E_\mathrm{SCC}(u)/T_*}\,d\sigma_M(u)$$

$\pi_t^{obs}$ is a well-defined probability measure on $\mathcal{F}_M(G)$: it is the Gibbs prior $\pi_{T_*}$ re-weighted by the likelihood $\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid \cdot)$.

**Definition 3.2 (Posterior sector partition function).** For $K \in K_\mathrm{feas}$:
$$Z_K^{obs}(\mathfrak{O}_t) = \int_{\mathcal{B}_K} \mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)\,e^{-E_\mathrm{SCC}(u)/T_*}\,d\sigma_M(u)$$

**Definition 3.3 (Posterior sector mass).** The observation-conditioned K-probability:
$$p_K(\mathfrak{O}_t) = \pi_t^{obs}(\mathcal{B}_K) = \frac{Z_K^{obs}(\mathfrak{O}_t)}{Z^{obs}(\mathfrak{O}_t)}$$

**Definition 3.4 (Observation-conditioned sector free energy).**
$$F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t) = -T_*\log Z_K^{obs}(\mathfrak{O}_t)$$

Equivalently: $p_K(\mathfrak{O}_t) \propto \exp(-F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t)/T_*)$.

**Observation-conditioned K-selection:**
$$K^*(\mathfrak{O}_t) \in \arg\min_{K \in K_\mathrm{feas}} F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t) = \arg\max_{K \in K_\mathrm{feas}} p_K(\mathfrak{O}_t)$$

### §3.1 Relation to prior sector masses

The posterior is the prior re-weighted:
$$p_K(\mathfrak{O}_t) = \frac{\mathbb{E}_{\pi_{T_*}}\!\left[\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid U)\,\mathbf{1}[K_\mathrm{act}(U)=K]\right]}{\mathbb{E}_{\pi_{T_*}}\!\left[\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid U)\right]}$$

When $\mathcal{L}_\mathrm{obs} \equiv 1$: $p_K(\mathfrak{O}_t) = p_K$ (T-K-Select-PF recovered). The observation $\mathfrak{O}_t$ shifts the K-distribution toward sectors where $\mathcal{L}_\mathrm{obs}$ is large.

### §3.2 Posterior null boundary

**Lemma 3.1.** $\pi_t^{obs}(\partial\mathcal{B}_K) = 0$.

**Proof.** $\pi_t^{obs} \ll \sigma_M$ (by definition: $\pi_t^{obs}$ has density $\propto \mathcal{L}_\mathrm{obs} e^{-E/T_*}$ w.r.t. $\sigma_M$, positive by LM2). Since $\pi_{T_*} \ll \sigma_M$ (T-PF-A1-GI) and $\partial\mathcal{B}_K$ is $\sigma_M$-null (T-K-Select-PF Cat B, codimension argument), $\pi_t^{obs}(\partial\mathcal{B}_K) = 0$. □

### §3.3 Posterior feasibility and K_feas^obs(O_t)

**Definition 3.5 (Posterior feasible set).** For fixed $\mathfrak{O}_t$, define:
$$K_\mathrm{feas}^{obs}(\mathfrak{O}_t) = \{K \in \mathbb{Z}_{\geq 0} : Z_K^{obs}(\mathfrak{O}_t) > 0\}$$

**Lemma 3.2 (Posterior feasibility equals prior feasibility under LM2).**
Under LM1–LM3 (in particular LM2: $\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u) > 0$ for all $u$):
$$K_\mathrm{feas}^{obs}(\mathfrak{O}_t) = K_\mathrm{feas}$$

**Proof.** For $K \in K_\mathrm{feas}$: $\sigma_M(\mathcal{B}_K) > 0$ by definition. $Z_K^{obs} = \int_{\mathcal{B}_K}\mathcal{L}_\mathrm{obs}\,e^{-E/T_*}d\sigma_M \geq \inf_{\mathcal{B}_K}(\mathcal{L}_\mathrm{obs}\,e^{-E/T_*})\cdot\sigma_M(\mathcal{B}_K) > 0$, where the infimum is positive since $\mathcal{L}_\mathrm{obs} > 0$ (LM2) and $e^{-E/T_*} > 0$ on the compact set $\mathcal{F}_M(G)$ (bounded $E$). Hence $K \in K_\mathrm{feas}^{obs}(\mathfrak{O}_t)$.

For $K \notin K_\mathrm{feas}$: $\sigma_M(\mathcal{B}_K) = 0$ by definition of $K_\mathrm{feas}$, so $Z_K^{obs} = 0$, hence $K \notin K_\mathrm{feas}^{obs}(\mathfrak{O}_t)$. □

**Remark.** LM2 (strict positivity) is the assumption that guarantees $K_\mathrm{feas}^{obs} = K_\mathrm{feas}$. If LM2 is relaxed to LM2' ($\mathcal{L}_\mathrm{obs} \geq 0$, not identically zero), then $K_\mathrm{feas}^{obs}(\mathfrak{O}_t) \subseteq K_\mathrm{feas}$ could be a strict subset — the observation evidence may rule out entire K-sectors. This is a useful extension but requires separate treatment (T-K-Select-OBS currently assumes LM2).

The observation-conditioned K-selection formula (§3, Definition 3.4) uses $K_\mathrm{feas}$ and $K_\mathrm{feas}^{obs}$ interchangeably under LM2. The argmin in claim (iii) of T-K-Select-OBS is over $K_\mathrm{feas}^{obs}(\mathfrak{O}_t) = K_\mathrm{feas}$.

---

## §4. T-K-Select-OBS: Observation-Conditioned K-Selection Theorem

### §4.1 Theorem statement

**T-K-Select-OBS (Observation-Conditioned K-Selection, Session S, 2026-05-06).**

*Assumptions:*
- **(A1)** P-F-A1 Package I: T-PF-A1-AR, T-PF-A1-GI Cat A (CV-1.9).
- **(A2)** T-K-Select-PF Cat B (CV-1.10): sectors $\mathcal{B}_K$ Borel measurable, $K_\mathrm{feas}$ finite non-empty, prior masses $\{p_K\}$ well-defined.
- **(A3)** Likelihood model: $\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u)$ satisfies (LM1)–(LM3) for fixed $\mathfrak{O}_t$.
- **(A4)** $T_* > 0$ (P-F-A1 axiom, OP-0021).

*Claims:*

(i) **Posterior well-definedness:** $\pi_t^{obs}$ is a well-defined probability measure on $\mathcal{F}_M(G)$. $Z^{obs} = \sum_{K \in K_\mathrm{feas}} Z_K^{obs}$ is finite and positive.

(ii) **Posterior sector masses:** $\{p_K(\mathfrak{O}_t)\}_{K \in K_\mathrm{feas}}$ form a probability distribution: $p_K(\mathfrak{O}_t) \geq 0$ and $\sum_K p_K(\mathfrak{O}_t) = 1$.

(iii) **Observation-conditioned K-selection:** $K^*(\mathfrak{O}_t) \in \arg\min_K F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t) = \arg\max_K p_K(\mathfrak{O}_t)$.

(iv) **Prior–posterior relationship:** $p_K(\mathfrak{O}_t) = p_K\,\cdot\,\mathbb{E}_{\pi_{T_*}}\!\left[\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid U) \mid K_\mathrm{act}(U)=K\right] \cdot Z/Z^{obs}$. The prior $\{p_K\}$ is recovered when $\mathcal{L}_\mathrm{obs} \equiv 1$.

(v) **Observation-conditioned free energy:** $p_K(\mathfrak{O}_t) > p_{K'}(\mathfrak{O}_t)$ iff $F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t) < F_\mathrm{obs}(K';\mathcal{P},\mathfrak{O}_t)$.

### §4.2 Proof

**(i)** By LM1 + LM3 + T-PF-A1-AR: $Z^{obs} = \int_{\mathcal{F}_M(G)} \mathcal{L}_\mathrm{obs} e^{-E/T_*} d\sigma_M$. Integrand is measurable (LM1 × Borel $e^{-E/T_*}$), non-negative (LM2), bounded above (LM2: $\mathcal{L}_\mathrm{obs} \leq \sup \mathcal{L}_\mathrm{obs} < +\infty$ since $\Phi_\mathrm{obs}$ continuous on compact $\mathcal{F}_M(G)$), positive (LM3). Compact domain + bounded integrand → $Z^{obs} < +\infty$; LM3 → $Z^{obs} > 0$. Hence $\pi_t^{obs}$ is a well-defined probability. □

**(ii)** Each $Z_K^{obs} \geq 0$ (non-negative integrand). $\sum_K Z_K^{obs} = Z^{obs}$ (disjoint Borel sectors cover $\mathcal{F}_M(G)$ up to $\pi_t^{obs}$-null set by Lemma 3.1 + T-K-Select-PF). Dividing by $Z^{obs} > 0$ gives probability. □

**(iii)** $K^*(\mathfrak{O}_t) = \arg\max_K p_K(\mathfrak{O}_t)$ exists since $K_\mathrm{feas}$ is finite (A2). Equivalence with $\arg\min F_\mathrm{obs}$: $p_K(\mathfrak{O}_t) \propto Z_K^{obs} = \exp(-F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t)/T_*)$. □

**(iv)** From $p_K(\mathfrak{O}_t) = Z_K^{obs}/Z^{obs}$ and $Z_K^{obs} = \int_{\mathcal{B}_K}\mathcal{L}_\mathrm{obs} e^{-E/T_*}d\sigma_M = Z \cdot p_K \cdot \mathbb{E}_{\pi_{T_*}}[\mathcal{L}_\mathrm{obs}|K_\mathrm{act}=K]$. Substituting: $p_K(\mathfrak{O}_t) = p_K \cdot \mathbb{E}_{\pi_{T_*}}[\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t|U)|K_\mathrm{act}(U)=K] \cdot Z/Z^{obs}$. When $\mathcal{L}_\mathrm{obs} \equiv 1$: all conditional expectations = 1, $Z^{obs} = Z$, recovered $p_K(\mathfrak{O}_t) = p_K$. □

**(v)** Strict ordering from $Z_K^{obs}/Z_K^{obs'} = \exp(-(F_\mathrm{obs}(K)-F_\mathrm{obs}(K'))/T_*)$. □

---

## §5. Non-Overclaim Section (Mandatory)

**T-K-Select-OBS does NOT:**

1. **Prove Kramers rates.** OP-0005-DYN (Package II, Eyring-Kramers, H5 + OP-0021) remains completely OPEN. T-K-Select-OBS is a static Bayesian statement, not a dynamical one.

2. **Prove observation dynamics.** The posterior $\pi_t^{obs}$ is defined for each fixed $\mathfrak{O}_t$. How the posterior evolves as $\mathfrak{O}_t$ changes over time (temporal integration, sequential Bayesian update) is not claimed.

3. **Prove uniqueness of $K^*(\mathfrak{O}_t)$.** Multiple $K$ values may share equal posterior mass. Uniqueness requires additional assumptions (e.g., non-degenerate likelihood).

4. **Prove a specific likelihood model.** T-K-Select-OBS holds for any likelihood satisfying LM1–LM3. Which specific model to use (e.g., photometric $\Phi_\mathrm{obs}$, depth consistency, optical flow) is a modeling decision not settled by this theorem.

5. **Add $E_\mathrm{photo}$ to $E_\mathrm{SCC}$.** The photometric likelihood $\mathcal{L}_\mathrm{obs}$ (containing $\Phi_\mathrm{obs}$) is strictly in the likelihood layer, NOT in the SCC prior. $E_\mathrm{SCC}$ retains exactly four terms (CN5). The MAP objective $E_\mathrm{SCC} + \lambda_\mathrm{photo} E_\mathrm{photo}$ is prior + likelihood, not an extended prior.

6. **Prove temporal tracking or σ-inheritance.** How $K_\mathrm{act}(t) \to K_\mathrm{act}(t+\delta t)$ transitions are not addressed; σ-signatures after K-jumps are OP-0008 (OPEN).

7. **Prove object detection.** K-selection is not object detection: $K_\mathrm{act}$ counts persistent SCC components, not identified discrete objects. The observation shifts the field distribution; it does not impose object labels.

8. **Prove $K^*(\mathfrak{O}_t)$ equals number of visual objects.** The number of persistent components in the posterior-weighted field distribution need not equal the "number of objects" in any pre-theoretic sense.

---

## §6. CN5 Compliance and Stereo Observation Bridge

### §6.1 CN5 compliance

CN5 (canonical.md §14): "The four energy terms address four logically independent structural requirements." CN5 governs the **prior** $E_\mathrm{SCC}$.

The likelihood $\mathcal{L}_\mathrm{obs}$ is **not** an SCC energy term. It is external observation information. The MAP objective
$$\tilde{u}_t^* = \arg\min_{u \in \mathcal{F}_M(G)}\bigl[E_\mathrm{SCC}(u) + \Phi_\mathrm{obs}(u;\mathfrak{O}_t)\bigr]$$
respects CN5: prior + likelihood, not a five-term energy. This is the canonical treatment established in `stereo_observation_framework.md` §4.2 and confirmed by exp04 (W6 D4).

### §6.2 Stereo bridge: connecting $\mathfrak{O}_t$ to canonical stereo definitions

The observation tuple in §2.3 condenses the canonical stereo tuple of `stereo_observation_framework.md` §3.2:
$$\mathfrak{O}_t^\mathrm{canonical} = (X_L,\,X_R,\,f_L,\,f_R,\,\Pi_{LR},\,\delta,\,z,\,c)$$

The backprojection $b_L = b_t : X_L^\mathrm{valid} \to \mathcal{P}_t$ (D-ST-5, canonical §16) is derived from the depth field $z$ and intrinsic matrix $K_\mathrm{cam}$:
$$b_t(x_L) = z(x_L)\,K_\mathrm{cam}^{-1}\begin{pmatrix}u_L \\ v_L \\ 1\end{pmatrix}$$

Under this bridge:
- $u \in \mathcal{F}_M(G)$ is a field on $\mathcal{P}_t$ (3D point cloud).
- $u^{pix}(x_L) = u(b_t(x_L))$ for $x_L \in X_L^\mathrm{valid}$ is the pullback to pixel space (D-ST-5).
- The photometric likelihood $\Phi_\mathrm{obs}(u;\mathfrak{O}_t) = \lambda_\mathrm{photo}\sum_{x_L} c(x_L)\,\Psi(f_L(x_L), f_R(\Pi_{LR}(x_L)), u^{pix}(x_L))$ depends on $u$ only through the pullback $u^{pix}$.

**Condition LM2 (positivity)** holds for $\Psi = \|f_L - f_R\|^2\cdot u$: $\Phi_\mathrm{obs}$ is finite for all $u$ (bounded $u$, bounded images, finite $X_L^\mathrm{valid}$).
**Condition LM1** holds: $u \mapsto u^{pix}$ is continuous; $\Psi$ is continuous in $u^{pix}$; composition is Borel measurable.
**Condition LM3** follows from LM2 + T-PF-A1-AR compactness.

Hence the stereo photometric likelihood satisfies LM1–LM3, and T-K-Select-OBS applies.

### §6.3 Observation operators $H_L, H_R$ (alternative formulation)

From `stereo_scc_canonical_memo_v1.1.md` and `stereo_observation_framework.md`, alternative formulation using observation operators:
$$\mathcal{L}_\mathrm{obs}(\mathfrak{O}_t \mid u) = \mathcal{L}_L(f_L \mid H_L u) \cdot \mathcal{L}_R(f_R \mid H_R u)$$

where $H_L u = u^{pix}_L$ (left pullback, linear operator on $\mathcal{F}_M(G)$) and similarly for $H_R$. This factored form is appropriate when left/right observations are conditionally independent given $u$. Both formulations satisfy LM1–LM3 under the same continuity conditions.

---

## §7. OP-0005 Status Post-Session S

| Sub-ID | Name | Status |
|---|---|---|
| **OP-0005-EQ** | Equilibrium K-selection | **PARTIALLY RESOLVED** — T-K-Select-PF canonical Cat B (Session R, CV-1.10) |
| **OP-0005-DYN** | Dynamical K-transition / Kramers rates | **OPEN** — Package II, W9+ |
| **OP-0005-OBS** | Observation-conditioned K selection | **STRUCTURED** — T-K-Select-OBS Cat B candidate (Session S). Mathematical structure complete; requires: (a) canonical likelihood model; (b) temporal extension; (c) experimental validation. |

OP-0005 overall remains OPEN.

---

## §8. Numerical Verification Plan (exp54)

**`CODE/experiments/exp54_posterior_k_selection_toy.py`** — Toy posterior K-selection.

### §8.1 Setup

- **Graph**: 12×12 or 16×16 grid graph G. $n = 144$ or $256$ nodes.
- **Parameters**: $\alpha = 1.0$, $\beta = 30$, $M = 0.3$ (two-formation regime; T-Birth-Parametric applies).
- **Prior**: $\pi_{T_*}$ with $T_* = 0.05$ — concentrates near energy minima.

### §8.2 Observation design (two regimes)

**Regime 1 — prior favors K=1, observation pushes K=2:**
- Start from K=1 energy minimum $u_1^*$ (single blob).
- Construct synthetic image $I$ with two spatially separated bright patches.
- Likelihood: $\mathcal{L}_\mathrm{obs}(u) = \exp(-\lambda_\mathrm{photo}\|u - I\|^2)$ with $\lambda_\mathrm{photo} = 2.0$.
- Expected: posterior shifts $p_K(\mathfrak{O}_t)$ toward K=2.

**Regime 2 — prior favors K=2, observation pushes K=1:**
- Start from K=2 energy minimum $u_2^* = (u^{(1)*}, u^{(2)*})$ (two blobs).
- Construct $I$ with single broad bright patch (compatible with K=1).
- Expected: posterior shifts toward K=1.

### §8.3 Computation

**Method A (Gibbs sampling + K-marginal):**
```python
# Metropolis-Hastings on F_M(G)
# Unnormalized density: exp(-(E_SCC(u) + lambda_photo * ||u - I||^2) / T_star)
# Estimate p_K(O) = fraction of samples with K_act(u) = K
```

**Method B (Sector energy comparison):**
1. Find $u_K^* = \arg\min_{u \in \mathcal{B}_K} [E_\mathrm{SCC}(u) + \lambda_\mathrm{photo}\|u-I\|^2]$ for K=1,2 (MAP per-sector).
2. Compute $F_\mathrm{obs}(K) \approx E_\mathrm{SCC}(u_K^*) + \lambda_\mathrm{photo}\|u_K^* - I\|^2$ (zero-temperature approximation).
3. Compare $F_\mathrm{obs}(1)$ vs $F_\mathrm{obs}(2)$: lower = posterior-preferred K.

Method B is implementable with existing `find_formation` in `optimizer.py` (initialize in K-sector via multi-formation initialization).

### §8.4 Expected outputs

| Test | Expected output | Validates |
|---|---|---|
| Regime 1 (prior K=1, obs K=2) | $p_2(\mathfrak{O}_t) > p_2$ (prior) | Likelihood shifts K upward |
| Regime 2 (prior K=2, obs K=1) | $p_1(\mathfrak{O}_t) > p_1$ (prior) | Likelihood shifts K downward |
| $\lambda_\mathrm{photo} \to 0$ | $p_K(\mathfrak{O}_t) \to p_K$ (prior) | Recover T-K-Select-PF |
| $\lambda_\mathrm{photo} \to +\infty$ | $p_K(\mathfrak{O}_t) \to \delta_{K^*(\mathfrak{O}_t)}$ | Observation dominates |

### §8.5 Implementation note

Requires no new SCC code — uses existing:
- `scc/optimizer.py:find_formation` for MAP per-sector.
- `scc/energy.py:EnergyComputer` for $E_\mathrm{SCC}$.
- `scc/graph.py:GraphState.grid_2d` for graph construction.
- MCMC loop (new, ~50 lines) for Method A posterior sampling.

---

## §9. Cat Status and Proof Completeness

### §9.1 Cat B candidate (current)

The theorem has a complete proof given Package I + T-K-Select-PF + LM1–LM3. The main items requiring formalization:

1. **Likelihood model specification (Cat B structural parameter)**: LM1–LM3 are stated abstractly. For Cat A, the specific likelihood model (photometric form $\Phi_\mathrm{obs}$, operator form $H_L, H_R$) must be canonically fixed and verified against (LM1)–(LM3).

2. **Posterior dynamics**: T-K-Select-OBS is static (fixed $\mathfrak{O}_t$). For a temporal SCC observation stream $\{\mathfrak{O}_t\}$, a sequential Bayesian update framework is needed (not addressed here; OP-0005-OBS further open problem).

3. **Sector non-degeneracy under posterior**: $K_\mathrm{feas}$ defined via $\sigma_M(\mathcal{B}_K) > 0$ (prior measure). Under the posterior, $Z_K^{obs} > 0$ for $K \in K_\mathrm{feas}$ follows from LM2 (positive likelihood on positive-measure set). This is automatic given LM2 + T-K-Select-PF.

4. **Null boundary under posterior**: Lemma 3.1 is immediate from $\pi_t^{obs} \ll \sigma_M$; this is already rigorous.

**Observation**: Claims (i)–(v) are essentially complete given (A1)–(A3). The mathematical content is standard Bayes theorem on a well-defined probability space (provided by Package I). The theorem's scientific value is in the structural framing: it connects the SCC Gibbs measure to the observation layer in a CN5-compliant way, and it reduces OP-0005-OBS to the problem of choosing a good likelihood model.

### §9.2 Cat A path

- Canonicalize the likelihood model (specific $\Phi_\mathrm{obs}$ or $(H_L, H_R)$ form).
- Verify LM1–LM3 for the canonical form explicitly.
- Provide experimental validation (exp54 above).
- Address temporal extension (if required for Cat A).

Cat A promotion: achievable after (a) canonical likelihood model choice and (b) exp54 validation. No new mathematics beyond Package I + Bayes theorem.

### §9.3 Suggested canonical label

If promoted: **T-K-Select-OBS** — "Observation-Conditioned K-Selection via Posterior Sector Mass." Proposed §13 Category B entry (Session S Cat B candidate); Cat A after likelihood canonicalization.

---

## §10. Hard Constraint Verification

- [x] **$u_t$ primitive maintained** — $u \in \mathcal{F}_M(G)$ is the soft cohesion field; $K_\mathrm{act}(u)$ derived. Posterior is over $u$, not over discrete objects.
- [x] **CN5 four energy terms not merged** — $E_\mathrm{SCC} = E_\mathrm{cl} + E_\mathrm{sep} + E_\mathrm{bd} + E_\mathrm{tr}$ in the prior; $E_\mathrm{photo}$ in the likelihood only. No fifth SCC energy term introduced.
- [x] **No Kramers rates** — T-K-Select-OBS is a static Bayesian statement. No barrier-crossing rates, no Eyring-Kramers formula, no Package II claim.
- [x] **No object detection** — $K_\mathrm{act}$ counts persistent SCC components; no discrete object identity imposed.
- [x] **$K^*(\mathfrak{O}_t)$ uniqueness not overclaimed** — §5 item 3 explicitly: multiple $K$ may have equal posterior mass.
- [x] **$T_*$ axiomatic** — OP-0021; not derived from SCC parameters or observation.
- [x] **OP-0005 not fully closed** — only OP-0005-OBS structured (Cat B candidate); OP-0005-DYN OPEN; OP-0005-EQ already Cat B (T-K-Select-PF).
- [x] **OP-0008 not claimed resolved** — σ-inheritance at K-jumps separate; not addressed.
- [x] **No silent resolution** — OP-0005-OBS status: OPEN → STRUCTURED (Cat B candidate). OP-0005 overall remains OPEN.
- [x] **No σ-inheritance claim** — σ-posterior at K-jump is OP-0008; not in scope here.
- [x] **Canonical edits not made** — working file only; canonical promotion requires review + user decision.

---

## §11. References

### §11.1 Canonical dependencies (all Cat A, CV-1.9)

- **T-PF-A1-AR**: `canonical.md §13` (Field Polytope Compact Convex; CV-1.8 → CV-1.9).
- **T-PF-A1-GI**: `canonical.md §13` (Gibbs Unique Invariant; CV-1.9).
- **T-K-Select-PF**: `canonical.md §13 Category B` (Prior K-Selection; CV-1.10).
- **D-ST-3**: `canonical.md §3.11` ($K_\mathrm{act}$ as #PersComp; W6 D4).
- **D-ST-5**: `canonical.md §16` (Backprojection $b_t$, pullback, prior/likelihood separation; W6 D4).

### §11.2 Working dependencies

- `working/MF/stereo_observation_framework.md` (W6 D2 evening): full observation layer, MAP structure, BO + Kramers framework, CN5 compliance. Primary reference for §6.
- `working/MF/k_select_pf_equilibrium.md` (Sessions Q–R, CV-1.10): parent theorem.
- `working/MF/k_selection_a_free_energy.md` (Task #5): saddle-point approximation.
- `working/MF/stereo_scc_canonical_memo_v1.1.md`: canonical stereo memo.

### §11.3 Open problems addressed / not addressed

- **OP-0005-OBS**: STRUCTURED by this file (Cat B candidate, Session S).
- **OP-0005-EQ**: PARTIALLY RESOLVED (T-K-Select-PF, canonical Cat B, CV-1.10).
- **OP-0005-DYN**: OPEN (Package II, W9+).
- **OP-0008**: OPEN (σ-posterior at K-jump; not addressed here).
- **OP-0021**: OPEN ($T_*$ registration; axiomatic here).

---

**End of k_select_obs_posterior.md.**

**Status:** working draft, Cat B candidate, Session S (2026-05-06). T-K-Select-OBS proves: given Package I + T-K-Select-PF + positive measurable likelihood LM1–LM3, the observation-conditioned posterior $\pi_t^{obs}$ is a well-defined probability measure on $\mathcal{F}_M(G)$; posterior sector masses $\{p_K(\mathfrak{O}_t)\}$ form a probability distribution; $K^*(\mathfrak{O}_t) \in \arg\min_K F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t)$. Prior {p_K} recovered when $\mathcal{L}_\mathrm{obs} \equiv 1$. CN5 preserved: $E_\mathrm{photo}$ in likelihood only. Non-overclaims: no Kramers, no temporal dynamics, no $K^*$ uniqueness, no object detection, no σ-inheritance, $T_*$ axiomatic.

**OP-0005-OBS: OPEN → STRUCTURED (Cat B candidate). OP-0005 overall OPEN.**

**File:** `THEORY/working/MF/k_select_obs_posterior.md`
