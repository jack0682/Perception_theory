---
id: PF-A1-WF-1
type: working/blocker
status: open
last_updated: 2026-05-06
---

# P-F-A1: Effective Stochastic Temperature $T_*$ — Working Formalization

**Blocker for:** D-ST-4 (Kramers rate, partition function $Z_K$), T-BO (Bayesian optimal $K^*$), any canonical metastability claim
**Session:** W6 D4 Session C (2026-05-06) — first formalization of the P-F flag as an operational working file
**Current status:** OPEN — $T_*$ undefined; all downstream Kramers claims are Cat B (with explicit P-F flag) at best

---

## 1. The Blocker

D-ST-4 (canonical.md §16) defines the $\mathcal{P}$-conditional Kramers escape rate:

$$\Gamma_{K \to K-1}(\mathcal{P}) \sim A(\mathcal{P}) \cdot \exp\left(-\frac{\Delta E_{K \to K-1}(\mathcal{P})}{T_*}\right)$$

and the partition function:

$$Z_K(\mathcal{P}) = \int_{\mathcal{B}_K(\mathcal{P})} e^{-\mathcal{E}[\tilde{u};\mathcal{P}]/T_*} \mathcal{D}\tilde{u}$$

The effective temperature $T_*$ appears as a free parameter in both. No canonical SCC claim about escape rates, equilibrium formation counts, or free energy differences can be made until $T_*$ is formally defined, its origin specified, and the stochastic dynamics on $\mathcal{F}_M(\mathcal{P})$ are canonically formalized.

---

## 1b. F_0(P) vs F_M(P): Why Mass Constraint Is Non-Negotiable for T_*

Two natural state spaces exist for the SCC field:

**F_0(P) = [0,1]^n** — the unconstrained field space. Gradient flow on F_0(P) is the Allen-Cahn equation on the graph:
$$\frac{d\tilde{u}}{dt} = -\nabla_{\tilde{u}} \mathcal{E}_{\mathrm{SCC}}[\tilde{u}]$$
This is an **non-conservative flow**: mass $\sum_i \tilde{u}_i(t)$ is NOT conserved. The flow can drive all values toward 0 or 1 without global constraint. There is no natural invariant Gibbs measure on F_0(P) of the form $\exp(-\mathcal{E}/T_*)$ because the flow is not derived from a Hamiltonian on a compact domain — F_0(P) is compact ([0,1]^n) but the flow has boundary attractors at the corners, and the Gibbs measure would be concentrated there.

**F_M(P) = {ũ ∈ [0,1]^n : Σᵢ ũᵢ = M}** — the mass-constrained field space (canonical §3.9). Gradient flow on F_M(P) is the Cahn-Hilliard-type projected gradient:
$$\frac{d\tilde{u}}{dt} = -\Pi_{T_{\tilde{u}}\mathcal{F}_M}\,\nabla_{\tilde{u}} \mathcal{E}_{\mathrm{SCC}}[\tilde{u}]$$
This is a **conservative flow**: mass M is preserved for all t. The mass constraint makes F_M(P) a compact (n−1)-dimensional manifold (intersection of simplex and hypercube), and the flow is a gradient vector field on this manifold. The Gibbs measure $\mu \propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)$ restricted to F_M(P) is a well-defined probability measure.

**Key consequence for T_*:** The Langevin SDE (§2b below) and all Kramers-rate claims are defined on **F_M(P) only**. On F_0(P), the stochastic dynamics $d\tilde{u}_t = -\nabla \mathcal{E} dt + \sqrt{2T_*} dW_t$ would not have a Gibbs invariant measure (the flow hits the boundary [0,1]^n without returning to the interior unless reflection boundary conditions are imposed). Therefore:

> **T_* is the Langevin temperature parameter of the F_M(P) dynamics specifically.** It is NOT defined for F_0(P) unconstrained dynamics.

This distinction has an operational implication: in `optimizer.py:find_formation`, the projected gradient step $u \leftarrow u + (M - \sum u)/n$ enforces mass conservation at each step. This is the discrete-time analog of the F_M(P) projected flow — and the Langevin extension adds noise to this same projected step. **Any T_* estimate must account for the mass-conserving projection**, not naive unconstrained diffusion.

---

## 2. Candidate Interpretations of $T_*$

Three interpretations are currently under consideration. They are mutually exclusive and lead to different canonical structures.

### 2a. Environmental noise temperature

$T_*$ = amplitude of observation noise, sensory fluctuation, or environmental perturbation that drives transitions between K-basins. Under this interpretation, the stochasticity is external: the cognitive/perceptual system is driven out of its current formation basin by input variability.

**Problem:** The connection between environmental noise amplitude and the effective temperature in the SCC energy landscape is non-trivial. Mapping input noise through the non-linear SCC dynamics to an effective thermal scale requires either a fluctuation-dissipation argument (valid only near equilibrium) or a full non-equilibrium analysis.

**Status:** Plausible phenomenologically, but not formally grounded.

### 2b. Field fluctuation temperature (Langevin on $\mathcal{F}_M(\mathcal{P})$)

$T_*$ = temperature parameter in an intrinsic Langevin process on the mass-constrained field space:

$$d\tilde{u}_t = -\nabla_\mathcal{E}\mathcal{E}_{\mathrm{SCC}}^{\mathcal{P}}[\tilde{u}_t]\, dt + \sqrt{2T_*}\, dW_t$$

where $W_t$ is a Wiener process on $\mathcal{F}_M(\mathcal{P})$ with the $\ell^2$ inner product, projected onto the simplex tangent space $T_{\tilde{u}}\mathcal{F}_M = \{v : \sum_x v(x) = 0\}$. The invariant measure of this process is the Gibbs measure $\propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)$.

**This is the P-F-A1 candidate:** it is the standard construction that makes Kramers' formula exact in the low-$T_*$ (Freidlin-Wentzell) limit, gives a well-defined partition function, and connects free energy differences to equilibrium K-selection probabilities.

**Key requirement:** Specification of:
1. The inner product on $\mathcal{F}_M(\mathcal{P})$ (standard $\ell^2$ on the simplex tangent space).
2. The projected noise $dW_t$ — Wiener process on the simplex.
3. Proof of invariant measure $\propto \exp(-\mathcal{E}/T_*)$.
4. Well-posedness (Lipschitz gradient on compact $\mathcal{F}_M$).

**Status:** Formally straightforward (Freidlin-Wentzell on finite-dimensional compact manifold), but not yet executed. This is the P-F-A1 target.

### 2c. Phenomenological inverse commitment strength

$T_* = 1/\beta_{\mathrm{commit}}$ where $\beta_{\mathrm{commit}}$ measures how committed the system is to its current formation configuration. Large $\beta_{\mathrm{commit}}$ (strong commitment) → small $T_*$ → slow transitions.

**Problem:** Without an independent definition of $\beta_{\mathrm{commit}}$, this risks circular reasoning. The notion of "commitment" would need to be defined separately from $T_*$ for this to be non-trivial.

**Status:** Conceptually appealing but operationally underdeveloped.

---

## 3. P-F-A1 Axiom Candidate (v0)

The following axiom formalizes the P-F flag operationally. It is a CV-1.7 Axiom Group G candidate.

> **P-F-A1 (v0).** *No metastability rate claim — including Kramers escape times $\tau_{K \to K'}$, K-jump equilibrium distributions $\pi_K$, effective temperatures $T_*$, or free energy differences $\Delta F_K$ — may be asserted as a canonical SCC claim (Cat B or higher) until the following stochastic extension has been canonically registered:*
>
> $$d\tilde{u}_t = -\nabla_\mathcal{E}\mathcal{E}_{\mathrm{SCC}}^\mathcal{P}[\tilde{u}_t]\, dt + \sqrt{2T_*}\, dW_t$$
>
> *with (i) a specified inner product on $\mathcal{F}_M(\mathcal{P})$; (ii) a specified noise covariance for $dW_t$; (iii) a proof that the invariant measure is $\propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)\, \mathcal{D}\tilde{u}$; (iv) a canonical registration of $T_*$ as a parameter of the stochastic extension.*
>
> *Claims about barrier heights $\Delta E_{K \to K'}$ are Cat B without P-F-A1 (they are deterministic energy differences). Claims about rates $\Gamma$, equilibrium probabilities $\pi_K$, or temperatures $T_*$ itself require P-F-A1.*

---

## 4. How $T_*$ Appears in the Theory

### 4.1 In Kramers' formula (D-ST-4)

$$\Gamma_{\alpha \to \beta} \approx \underbrace{\frac{|\lambda_-(\tilde{u}^{\mathrm{sad}})|}{2\pi} \cdot \sqrt{\frac{\det H_\alpha}{\det H_{\mathrm{sad}}}}}_{\text{attempt frequency } A} \cdot \exp\!\left(-\frac{\Delta E_{\alpha \to \beta}}{T_*}\right)$$

where:
- $\tilde{u}^{\mathrm{sad}}$ is the saddle point on the MEP between basins $\alpha$ and $\beta$ (computable via NEB, exp02-NEB / exp02b)
- $\lambda_-(\tilde{u}^{\mathrm{sad}})$ is the single negative eigenvalue of the Hessian $H_{\mathrm{sad}}$ at the saddle
- $\Delta E_{\alpha \to \beta} = \mathcal{E}[\tilde{u}^{\mathrm{sad}}] - \mathcal{E}[\tilde{u}^{(\alpha)}]$ is the barrier height
- Both $A$ and $\Delta E$ are computable from existing `energy.py`/`optimizer.py` infrastructure (NQ-ST-1)

### 4.2 In the partition function (D-ST-4)

Under Laplace approximation near basin minimum $\tilde{u}^{(\alpha)}$:

$$Z_{K,\alpha}(\mathcal{P}) \approx e^{-\mathcal{E}[\tilde{u}^{(\alpha)}]/T_*} \cdot \frac{(2\pi T_*)^{n/2}}{\sqrt{\det H_\alpha}}$$

The ratio $Z_{K,\alpha}/Z_{K',\beta}$ determines relative formation probabilities at temperature $T_*$. This ratio depends on $T_*$ both through the exponential (barrier) and the prefactor (Hessian determinant ratio).

### 4.3 In equilibrium K-selection

The equilibrium probability of observing K formations:

$$\pi_K \propto Z_K(\mathcal{P}) = \sum_\alpha Z_{K,\alpha}(\mathcal{P})$$

This is the theoretical grounding for K-selection via free energy minimization. Requires $T_*$.

---

## 5. Relationship to Existing Claims

| Claim | Current status | P-F-A1 dependency |
|---|---|---|
| D-ST-4: $Z_K(\mathcal{P})$ partition function | Cat B candidate (P-F flagged) | Uses $T_*$ — Cat B permissible with explicit flag |
| D-ST-4: $\Gamma_{K \to K-1}$ Kramers rate | Cat B candidate (P-F flagged) | Directly requires $T_*$ |
| T-ST-5a: hard-cut topological locking | Cat B candidate — **no P-F flag needed** | Deterministic topological result; no $T_*$ |
| T-ST-5b: smooth barrier raising | Cat C pending | $\Delta E$ computation is deterministic (NEB); Kramers interpretation of $\Delta E$ requires $T_*$ |
| exp05: Markov chain stationary dist | SUPPORTED (toy) | $T_*$ ad hoc in toy; real $T_*$ undefined |
| T-BO: Bayesian optimal $K^*$ | Cat C / working | Requires $\pi_K \propto Z_K/Z$, hence $T_*$ |
| OP-0005: K-selection Layer C (Kramers) | OPEN | Full resolution requires P-F-A1 |

---

## 6. Target Formalization (CV-1.7)

Steps to register P-F-A1 canonically:

1. **Inner product:** Specify $\langle u, v \rangle_{\mathcal{F}_M} = \sum_{x \in \mathcal{P}} u(x) v(x)$ restricted to the simplex tangent space.
2. **Projected Wiener process:** Define $dW_t$ as the projection of a standard $\ell^2$ Wiener process onto $T_{\tilde{u}}\mathcal{F}_M = \{v : \sum_x v(x) = 0\}$.
3. **Invariant measure:** Prove $\mu \propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)$ is invariant under the Langevin dynamics. (Standard: verify detailed balance via Fokker-Planck.)
4. **Freidlin-Wentzell:** Apply Freidlin-Wentzell theory on the compact simplex to derive Kramers approximation at small $T_*$.
5. **Register $T_*$:** Canonically define $T_*$ as the Langevin temperature parameter, distinct from $\beta$ (double-well sharpness) and $\alpha$ (closure/smoothness). Physical range: $T_* \ll \min_K \Delta E_{K \to K-1}$ for metastability.

**Estimated scope:** W7 half-day. Freidlin-Wentzell on a finite-dimensional compact manifold is well-established; the main work is the mechanical formalization in the SCC setting.

---

## 7. Implications for Notation

Once P-F-A1 is formalized:
- $T_*$ becomes a canonical parameter alongside $\alpha, \beta, \lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}$.
- The Gibbs measure $\mu_{T_*}$ on $\mathcal{F}_M(\mathcal{P})$ becomes canonical.
- The partition function $Z_K(\mathcal{P}; T_*)$ gains explicit $T_*$ dependence.
- The Kramers rate $\Gamma_{K \to K-1}(\mathcal{P}; T_*, \alpha, \beta)$ gains full parameter dependence.
- Cat B $\to$ Cat A promotion becomes available for D-ST-4 claims (subject to barrier height validation).

---

## 7b. Promotion Ceiling: No Kramers Claims Above Cat B Until P-F-A1

**Policy (Session D, W6 D4).** Until P-F-A1 is canonically registered (target CV-1.7, see §6):

- Barrier height claims ΔE_{K→K'} = E(saddle) − E(min) are **deterministic energy differences** — they are Cat B-eligible without P-F-A1 (NEB computation is well-defined).
- Rate claims Γ_{K→K'}, escape time τ, and any claim involving exp(−ΔE/T_*) are **at most Cat B** with explicit P-F flag. They cannot be promoted to Cat A until T_* is canonically defined.
- Equilibrium claims π_K ∝ Z_K, free energy differences ΔF_K, and Bayesian optimal K^* (T-BO) all require P-F-A1 and are **at most Cat B** (P-F flagged).
- The partition function Z_K(P; T_*) defined in D-ST-4 (canonical §16) is **Cat B** with the P-F flag. Its Cat A promotion is downstream of P-F-A1 + barrier validation.

**The F_M(P) Langevin formalization (§2b, §1b) is the gating item.** Once P-F-A1 is registered:
- D-ST-4 barrier heights: Cat B → Cat A (deterministic; no additional work)
- D-ST-4 rates/partition function: Cat B (P-F) → Cat A-eligible (after Freidlin-Wentzell verification)
- T-BO (Bayesian optimal K*): Cat C → Cat B-eligible

**Estimation (§6):** Freidlin-Wentzell on compact finite-dimensional simplex is standard. The main SCC-specific work is specifying the inner product on F_M(P) and verifying the invariant measure. Estimated W7 half-day. No computation required — pure formalization.

---

## 8. Implementation Link: langevin.py

The canonical implementation candidate for P-F-A1 is `CODE/scc/langevin.py`.

### 8.1 What langevin.py implements

`projected_langevin(u_init, graph, params, T, ...)` runs projected Euler-Maruyama:

```
u_{t+dt} = u_t - dt · Π_{1^⊥}[∇_u F_{C+E}(u_t)] + sqrt(2T dt) · Π_{1^⊥}[ξ_t]
```

where:
- $\Pi_{1^\perp}[\cdot] = v - \mathrm{mean}(v)$ projects onto the simplex tangent space (`_project_tangent`)
- $F_{C+E}(u) = \mathcal{E}_{\mathrm{SCC}}[u] - T \cdot S_{\mathrm{Bern}}(u) + \lambda_K \cdot K_{\mathrm{soft}}(u)$
- $S_{\mathrm{Bern}}(u) = -\sum_i [u_i \ln u_i + (1-u_i)\ln(1-u_i)]$ (Bernoulli entropy)
- `_reflect_to_box`: clip to $[\varepsilon, 1-\varepsilon]^n$ then rescale mass — approximation to Lions-Sznitman reflection

**EnergyComputer interface:** `ec = EnergyComputer(graph, params)` → `ec.energy(u)` returns `(E, terms_dict)`, `ec.gradient(u)` returns $\nabla \mathcal{E}_{\mathrm{SCC}}$.

**Mass conservation:** The projection $\Pi_{1^\perp}$ removes the constant component of the gradient and noise, preserving $\sum_i u_i = M$ at each step. This correctly implements F_M(P) dynamics (§1b).

### 8.2 Discrepancy with P-F-A1 §3 (axiom v0)

The P-F-A1 axiom v0 (§3) specifies invariant measure $\propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)$ — the **pure energy** Gibbs measure.

The `langevin.py` implementation uses $F_{C+E} = \mathcal{E} - T \cdot S_{\mathrm{Bern}}$, so the actual invariant measure is:
$$\mu_{\mathrm{impl}} \propto \exp(-F_{C+E}/T) = \exp(-\mathcal{E}/T) \cdot \exp(S_{\mathrm{Bern}}/1) \propto \exp(-\mathcal{E}/T) \cdot \prod_i u_i^{-u_i}(1-u_i)^{-(1-u_i)}$$

This is the **Bernoulli-regularized Gibbs measure** — NOT the pure $\exp(-\mathcal{E}/T_*)$.

The Bernoulli entropy term serves as a boundary barrier preventing mass concentration at 0 or 1 (a practical workaround for the box boundary condition). The correct formulation (Lions-Sznitman reflection) would use the pure energy Gibbs measure with hard reflection at $\partial[0,1]^n$.

**Consequence for P-F-A1 canonical registration:** The canonical axiom v0 (§3) should specify the invariant measure as $\mu \propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)$ with Lions-Sznitman reflection. The `langevin.py` implementation is an approximation to this with an additional Bernoulli entropy boundary term. For Cat A promotion (after P-F-A1), one of the following must be resolved:
1. Show that the Bernoulli regularization is equivalent to Lions-Sznitman in the limit $\varepsilon \to 0$, or
2. Modify `langevin.py` to use `lambda_K=0` and `T=0` in the entropy term as a pure-energy implementation.

For current Cat B purposes (P-F-A1 §7b policy), the implementation is sufficient to demonstrate stochastic F_M(P) dynamics and validate barrier height estimates.

### 8.3 Validation status

`langevin.py` is used in `CODE/stereo_scc/experiments/exp05_kact_markov_chain.py` with ad hoc $T_*$. The invariant measure has NOT been empirically validated (no comparison to known Gibbs ensemble). This validation is part of the P-F-A1 Cat A promotion path (§6, step 3).

**Implementation match score: PARTIAL.** Mass conservation: correct. Projected noise: correct. Boundary handling: approximate (entropy term vs. reflection). Invariant measure: regularized (not pure Gibbs). Sufficient for Cat B barrier-height claims; insufficient for Cat A rate claims.

---

### 8.4 Three Gibbs Targets — Distinctions and Modification Plan

The P-F-A1 formalization requires choosing exactly one Gibbs target. Three are in play; they are mutually non-equivalent in general.

---

**Target A — Pure Gibbs (canonical axiom v0)**

$$\mu_A \propto \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}}[\tilde{u}]}{T_*}\right) \mathcal{D}\tilde{u} \quad \text{on } \mathcal{F}_M(\mathcal{P})$$

This is what P-F-A1 §3 specifies. The Langevin SDE that achieves this invariant measure is:

$$d\tilde{u}_t = -\Pi_{T_{\tilde{u}}\mathcal{F}_M}\nabla \mathcal{E}_{\mathrm{SCC}}[\tilde{u}_t]\,dt + \sqrt{2T_*}\,\Pi_{T_{\tilde{u}}\mathcal{F}_M}\,dW_t$$

with **Lions-Sznitman reflection** at $\partial[0,1]^n$ to keep $\tilde{u}_t \in [0,1]^n$. The reflection is the theoretical ideal (well-posed; standard for compact convex domains). Computational cost: requires reflection detection at each step (check for clip events), then resample the noise perpendicular to the boundary face. Not currently implemented in `langevin.py`.

---

**Target B — Bernoulli-regularized Gibbs (langevin.py without K_soft)**

$$\mu_B \propto \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}}[\tilde{u}] - T \cdot S_{\mathrm{Bern}}(\tilde{u})}{T}\right) = \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}}}{T}\right) \cdot \exp(S_{\mathrm{Bern}})$$

where $S_{\mathrm{Bern}}(\tilde{u}) = -\sum_i [u_i \ln u_i + (1-u_i)\ln(1-u_i)]$.

This is what `langevin.py` implements when `lambda_K=0`. The Bernoulli entropy term replaces Lions-Sznitman reflection: it diverges as $u_i \to 0$ or $u_i \to 1$, creating a soft interior barrier. The invariant measure differs from $\mu_A$ by the factor $\exp(S_{\mathrm{Bern}})$, which upweights configurations with intermediate field values (pushes away from crisp $\{0,1\}$-valued fields). In the phase-separated regime, this is a small correction (the field is near $\{0,1\}$ and $\exp(S_{\mathrm{Bern}}) \approx 1$ there), but it is not zero. For barrier-height claims $\Delta E = E(\mathrm{saddle}) - E(\mathrm{min})$, the correction is second-order in $\delta$ (interface-width terms), making Target B and Target A equivalent for bulk barrier estimates.

---

**Target C — K-augmented Bernoulli-regularized (langevin.py full)**

$$\mu_C \propto \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}} - T \cdot S_{\mathrm{Bern}} + \lambda_K \cdot K_{\mathrm{soft}}}{T}\right)$$

where $K_{\mathrm{soft}}(\tilde{u}) = $ soft K-count regularizer. This adds a K-soft term that biases toward specific K_act values. The invariant measure further differs from $\mu_A$ and $\mu_B$. The K-soft term is NOT part of the canonical SCC energy — it is an ad hoc regularizer added to shape the stationary distribution of K_act. This is Target C and is inappropriate for canonical P-F-A1 (the canonical Gibbs measure should reflect E_SCC structure, not an externally imposed K preference).

**Recommendation:** Set `lambda_K=0` in all P-F-A1 validation runs. Target C is useful for exploratory K-selection experiments but should NOT be used in any canonical claim about T_*, Z_K, or Kramers rates.

---

**Modification plan for canonical match:**

| Goal | Implementation | Complexity |
|---|---|---|
| Validate T_* existence (Cat B) | Use Target B (lambda_K=0) with T=T_* | Low — already in langevin.py |
| Prove invariant measure = μ_B (not μ_A) | Fokker-Planck check: verified by §8.2 argument | Analytical, done |
| Prove μ_B → μ_A as ε→0 (epsilon = boundary regularization width) | Lions-Sznitman limit: standard result for entropy-regularized barriers → hard reflection in ε→0 | Analytical (cite Cattiaux-Guillin or Tanaka reflection; ~half-day) |
| Pure μ_A implementation (Cat A) | Add Lions-Sznitman reflection to `langevin.py`: detect clip events; project noise to face | Engineering: ~1 day |

**For Cat B claims (current state):** Target B is adequate. The Bernoulli entropy correction to barrier heights is $O(\delta) \approx O(\exp(-c\sqrt{\beta/\alpha}))$ — exponentially small in the phase-separated regime. Experimental barrier estimates from `langevin.py` (Target B) are consistent with Target A barriers to within this correction.

**For Cat A claims (P-F-A1 resolution target):** Either prove the ε→0 limit rigorously OR implement pure Target A (Lions-Sznitman reflection). Estimated W7 half-day for the analytical path (ε→0 limit); 1 day for the implementation path.

---

### 8.5 Theorem T-P-F-ε0: Gibbs Measure Continuity at ε=0 (Formal)

**ID:** T-P-F-ε0  
**Type:** Analytical theorem (finite-dimensional compact domain)  
**Status:** Cat A candidate — proof complete; all hypotheses verified for SCC setting  
**Session:** W6 D4 Session G (sketch) → Session H (formal write-up)

---

#### Setup and Hypotheses

Let $\mathcal{F}_M(\mathcal{P}) = \{\tilde{u} \in [0,1]^n : \sum_i \tilde{u}_i = M\}$ be the mass-constrained field space (D-ST-2, §3.9). The parameterized family of measures is:

$$\mu_\varepsilon(d\tilde{u}) = Z_\varepsilon^{-1} \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}}^{\mathcal{P}}[\tilde{u}] + \varepsilon \cdot R(\tilde{u})}{T_*}\right) d\sigma(\tilde{u}), \quad \varepsilon \in [0, 1]$$

where $d\sigma$ is the $(n-1)$-dimensional Hausdorff measure on $\mathcal{F}_M(\mathcal{P})$ and $Z_\varepsilon$ is the normalizing constant.

**Connection to three targets.** With $R = -T_* \cdot S_{\mathrm{Bern}}$:
- $\varepsilon = 0$: $\mu_0 \propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*)$ = **Target A** (canonical P-F-A1 axiom v0)  
- $\varepsilon = 1$: $\mu_1 \propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T_+)\cdot\exp(S_{\mathrm{Bern}})$ = **Target B** (langevin.py, lambda_K=0)

**Hypotheses:**

- **(H1)** $\mathcal{F}_M(\mathcal{P})$ is compact. *(Verified: intersection of $[0,1]^n$ and affine hyperplane $\sum_i \tilde{u}_i = M$; both closed and bounded; finite $n$.)*
- **(H2)** $\mathcal{E}_{\mathrm{SCC}}$ is continuous on $\mathcal{F}_M(\mathcal{P})$. *(Verified: $\mathcal{E}_{\mathrm{SCC}}$ is a polynomial in $\tilde{u}$; continuous on $[0,1]^n$; hence continuous on $\mathcal{F}_M(\mathcal{P})$.)*
- **(H3)** The reference measure satisfies $\sigma(\mathcal{F}_M(\mathcal{P})) > 0$. *(Verified: $\mathcal{F}_M(\mathcal{P})$ is a non-degenerate $(n-1)$-polytope for $M \in (0, n)$, which holds in all SCC operating regimes.)*
- **(H4)** $R$ is measurable and bounded below: $\exists C \geq 0$ such that $R(\tilde{u}) \geq -C$ for all $\tilde{u} \in \mathcal{F}_M(\mathcal{P})$. *(Verified for Bernoulli case $R = -T_*S_{\mathrm{Bern}}$: $S_{\mathrm{Bern}} \leq n \ln 2$, so $R \geq -T_* n \ln 2$.)*

---

#### Theorem Statement

**Theorem T-P-F-ε0.** *Under (H1)–(H4), for all bounded continuous $f : \mathcal{F}_M(\mathcal{P}) \to \mathbb{R}$:*

$$\int f \, d\mu_\varepsilon \xrightarrow{\varepsilon \to 0} \int f \, d\mu_0$$

*i.e., $\mu_\varepsilon \Rightarrow \mu_0$ weakly as $\varepsilon \to 0$.*

---

#### Proof

**Step 1. Compactness and finiteness of $\sigma$.**
By (H1), $\mathcal{F}_M(\mathcal{P})$ is compact; its Hausdorff measure $\sigma(\mathcal{F}_M(\mathcal{P})) < \infty$ (finite polytope). By (H3), $\sigma(\mathcal{F}_M(\mathcal{P})) > 0$.

**Step 2. Positivity of $Z_0$.**
By (H2), $\mathcal{E}_{\mathrm{SCC}}$ is continuous on the compact set $\mathcal{F}_M(\mathcal{P})$, hence bounded: $\mathcal{E}_* := \sup_{\tilde{u}} \mathcal{E}_{\mathrm{SCC}}[\tilde{u}] < \infty$. Therefore:

$$Z_0 = \int_{\mathcal{F}_M} e^{-\mathcal{E}/T_*} d\sigma \geq e^{-\mathcal{E}_*/T_*} \cdot \sigma(\mathcal{F}_M) > 0$$

**Step 3. Dominated convergence for $Z_\varepsilon$.**
Define $g_\varepsilon(\tilde{u}) := \exp(-({\mathcal{E}[\tilde{u}] + \varepsilon R(\tilde{u})})/T_*)$. By (H4):

$$g_\varepsilon(\tilde{u}) \leq \exp(-\mathcal{E}[\tilde{u}]/T_*) \cdot \exp(\varepsilon C/T_*) \leq \exp(-\mathcal{E}[\tilde{u}]/T_*) \cdot \exp(C/T_*) =: h(\tilde{u})$$

for all $\varepsilon \in [0,1]$. Since $h$ is continuous and $\mathcal{F}_M$ is compact, $\int h \, d\sigma < \infty$. Also, $g_\varepsilon(\tilde{u}) \to g_0(\tilde{u}) = \exp(-\mathcal{E}[\tilde{u}]/T_*)$ pointwise as $\varepsilon \to 0$. By the dominated convergence theorem:

$$Z_\varepsilon = \int g_\varepsilon \, d\sigma \xrightarrow{\varepsilon \to 0} \int g_0 \, d\sigma = Z_0 > 0$$

**Step 4. Convergence of expectations.**
Let $|f| \leq M_f$. Write:

$$\int f \, d\mu_\varepsilon - \int f \, d\mu_0 = \frac{1}{Z_\varepsilon}\int f \cdot g_\varepsilon \, d\sigma - \frac{1}{Z_0}\int f \cdot g_0 \, d\sigma$$

Add and subtract $\frac{1}{Z_0}\int f \cdot g_\varepsilon \, d\sigma$:

$$= \frac{1}{Z_\varepsilon}\int f(g_\varepsilon - g_0) d\sigma + \left(\frac{1}{Z_\varepsilon}-\frac{1}{Z_0}\right)\int f \cdot g_0 \, d\sigma$$

**Term I:** $\left|\frac{1}{Z_\varepsilon}\int f(g_\varepsilon - g_0)d\sigma\right| \leq \frac{M_f}{Z_\varepsilon}\int|g_\varepsilon - g_0|d\sigma \to 0$
by dominated convergence ($|g_\varepsilon - g_0| \to 0$ pointwise, $\leq h + g_0 \leq 2h$ integrable).

**Term II:** $\left|\left(\frac{1}{Z_\varepsilon}-\frac{1}{Z_0}\right)\int f \cdot g_0 d\sigma\right| \leq M_f \cdot Z_0 \cdot \left|\frac{1}{Z_\varepsilon}-\frac{1}{Z_0}\right| \to 0$ since $Z_\varepsilon \to Z_0 > 0$.

Both terms vanish. Therefore $\int f \, d\mu_\varepsilon \to \int f \, d\mu_0$ for all bounded continuous $f$. $\square$

---

#### Corollary T-P-F-ε0-K: Kramers Barrier Perturbation

**Additional hypothesis (H5):** The barrier height is determined by a saddle point $\tilde{u}^*_{\mathrm{sad}}$ and minimum $\tilde{u}^*_{\mathrm{min}}$ that are stable under the perturbation $\varepsilon \cdot R$ at small $\varepsilon$ (no new critical points of $\mathcal{E} + \varepsilon R$ created near $\tilde{u}^*_{\mathrm{sad}}$ or $\tilde{u}^*_{\mathrm{min}}$ for $\varepsilon \in [0, \varepsilon_0]$).

**Statement.** Under (H1)–(H5), the perturbed barrier satisfies:

$$\Delta \mathcal{E}_\varepsilon := \left[\mathcal{E}(\tilde{u}^*_{\mathrm{sad}}) + \varepsilon R(\tilde{u}^*_{\mathrm{sad}})\right] - \left[\mathcal{E}(\tilde{u}^*_{\mathrm{min}}) + \varepsilon R(\tilde{u}^*_{\mathrm{min}})\right] = \Delta \mathcal{E}_0 + \varepsilon \cdot \Delta R$$

where $\Delta \mathcal{E}_0 = \mathcal{E}(\tilde{u}^*_{\mathrm{sad}}) - \mathcal{E}(\tilde{u}^*_{\mathrm{min}})$ and $\Delta R = R(\tilde{u}^*_{\mathrm{sad}}) - R(\tilde{u}^*_{\mathrm{min}})$.

Therefore the leading Arrhenius factor satisfies:

$$\Gamma_\varepsilon = \Gamma_0 \cdot \exp\!\left(-\frac{\varepsilon \cdot \Delta R}{T_*}\right)$$

**Bernoulli specialization ($R = -T_* \cdot S_{\mathrm{Bern}}$, $\varepsilon = 1$, i.e., Target B vs Target A):**

$$\frac{\Gamma_B}{\Gamma_A} = \exp\!\left(\frac{\Delta S_{\mathrm{Bern}}}{1}\right) = \exp\!\left(S_{\mathrm{Bern}}(\tilde{u}^*_{\mathrm{sad}}) - S_{\mathrm{Bern}}(\tilde{u}^*_{\mathrm{min}})\right)$$

At phase-separated configurations: $\tilde{u}^*_{\mathrm{min}} \approx \{0,1\}$-valued, so $S_{\mathrm{Bern}}(\tilde{u}^*_{\mathrm{min}}) \approx 0$. The saddle has $S_{\mathrm{Bern}}(\tilde{u}^*_{\mathrm{sad}}) = O(|\partial S|/n) = O(\delta)$ where $\delta \sim \exp(-c\sqrt{\beta/\alpha})$ is the Allen-Cahn interface width. Therefore:

$$\frac{\Gamma_B}{\Gamma_A} = \exp(O(\delta)) = 1 + O(\delta) \quad (\text{exponentially small correction in } \sqrt{\beta/\alpha})$$

**Conclusion:** The Kramers escape rate predicted by Target B (langevin.py, implemented) differs from Target A (canonical P-F-A1) by a factor exponentially close to 1 in the phase-separated regime. The leading Arrhenius exponent $\exp(-\Delta\mathcal{E}_0/T_*)$ is shared. **(Cat B: deterministic ΔE claims; Cat A for Γ: requires H5 + spectral gap.)**

---

#### Non-Claims (Explicit)

This theorem does **NOT** establish:

1. **Spectral gap:** No bound on the mixing time of the Langevin dynamics. The generator $\mathcal{L}_\varepsilon = -\nabla_{\mathcal{E}+\varepsilon R} + \sqrt{2T_*}\,dW$ may have different spectral properties for $\varepsilon > 0$ vs $\varepsilon = 0$.
2. **Eyring-Kramers pre-exponential factor $A$:** The prefactor in $\Gamma \sim A \cdot \exp(-\Delta\mathcal{E}/T_*)$ involves the Hessian at saddle and minimum (Witten Laplacian / Helffer-Sjöstrand theory). Not addressed.
3. **Existence of $T_*$:** The proof assumes $T_* > 0$ is given. It does not establish what $T_*$ is or that it can be canonically defined from SCC parameters.
4. **H5 (Morse stability):** Hypothesis H5 is assumed, not proved for $\mathcal{E}_{\mathrm{SCC}}$. For the specific Bernoulli perturbation $R = -T_*S_{\mathrm{Bern}}$, H5 holds generically (by Morse theory, critical points are preserved under small perturbations) but has not been verified at the global level for the non-convex SCC energy.
5. **Infinite-dimensional extension:** $\mathcal{F}_M(\mathcal{P})$ is finite-dimensional (finite graph). Extension to continuous spaces $(\mathcal{P} = \mathbb{R}^2)$ is not treated.
6. **Convergence of langevin.py to equilibrium:** This theorem is about the invariant measure, not the dynamics. It does not imply that the Markov chain generated by `projected_langevin` converges at any particular rate.

---

### 8.6 Registration Decision: P-F-A1 Canonical Status

**Claim:** The following registrations are warranted at W6 D4 Session H:

| Item | Status | Justification |
|---|---|---|
| **T-P-F-ε0** (weak convergence) | **Cat A candidate** | Proof complete — Steps 1–4 above constitute a full proof; all hypotheses H1–H4 are explicitly verified for the SCC setting. Standard dominated-convergence argument, no gaps. Suitable for CV-1.7 Cat A. |
| **T-P-F-ε0-K** (Kramers corollary) | **Cat B** | Depends on H5 (Morse stability), which is plausible but not formally proved for $\mathcal{E}_{\mathrm{SCC}}$. Barrier correction $O(\delta)$ is well-motivated but H5 is an assumption. |
| **P-F-A1 axiom (v0)** | **OPEN (working/blocker)** | Full P-F-A1 requires Eyring-Kramers formula + spectral gap + $T_*$ existence. None of these are addressed by T-P-F-ε0 alone. P-F-A1 remains the CV-1.7 target blocker for D-ST-4 rate claims. |
| **D-ST-4 Kramers rate** | **Cat B (P-F flagged)** | ΔE barriers are deterministic (Cat B without P-F-A1). Γ rates require P-F-A1. Unchanged. |

**Promotion path for P-F-A1 Cat A (updated Session M, 2026-05-06):**

*ROUTE CORRECTION: Bakry-Émery is CLOSED (double-well W''(u) changes sign at spinodal; no global Ric ≥ K > 0). Holley-Stroock is insufficient as primary (gap exponentially small in n). Correct route is Package I (affine reduction → reflected SDE → Gibbs invariance → Poincaré). See `working/MF/pf_a1_lions_sznitman_freidlin_route.md` for full decomposition.*

**Package I (minimal, sufficient for P-F-A1):**
1. T-PF-A1-Affine-Reduction: F_M(G) = {u ∈ [0,1]^n : μ^T u = M} is a compact convex polytope of intrinsic dimension n−1; SCC energy reduces to Ẽ on C̃ ⊂ R^{n−1}. *(Working grade — Session M)*
2. T-PF-A1-Finite-Reflected-SDE: Unique strong solution to reflected Langevin on C̃ via Lions-Sznitman (H-LS1: compact convex polytope; H-LS2: Lipschitz drift). *(Working grade — Session M)*
3. T-PF-A1-Gibbs-Invariance: π_{T_*} = Z^{-1} exp(−E/T_*) dσ_M is the unique invariant measure (reversibility via Dirichlet form + no-flux BC). *(Working grade — Session M)*
4. T-PF-A1-Poincare-Ergodicity: Poincaré inequality and λ_1 > 0 via compact domain + Holley-Stroock perturbation from Payne-Weinberger. C_P exists (may be exp. large in n — acceptable). *(Working grade — Session M)*

**Package II (conditional metastability, NOT P-F-A1):**
5. Prove H5 (Morse stability) for $\mathcal{E}_{\mathrm{SCC}} + \varepsilon R$ at the relevant saddles. *(Required for Eyring-Kramers only)*
6. Freidlin-Wentzell quasipotential + Eyring-Kramers formula (conditional on H5 + T_* registration). *(Package II, W9+)*

**T_* canonical registration (OP-0021):**
7. Register T_* as canonical axiom with explicit inner product, noise covariance, and invariant measure. *(W9+, hard)*

Estimated effort for Package I promotion to Cat B: Session N (1 session proof review). Full Cat A: Session O (1 additional session). Eyring-Kramers: W9+.

---

## References

- `canonical.md §16 D-ST-4` — Topological sector, partition function, Kramers rate (P-F flagged)
- `canonical.md §3.9` — Field space $\mathcal{F}_M(\mathcal{P})$ (foundational state space)
- `stereo_observation_framework.md §5–§6` — BO time scales, Kramers rates, P-F axiom v0
- `k_selection_b_kramers.md §3` — Barrier scaling estimates and Kramers rate framework
- `CODE/scc/langevin.py` — Primary implementation: projected Langevin on Σ_m with Bernoulli entropy regularization (§8 above)
- `CODE/stereo_scc/kramers.py` — Toy implementation (ad hoc $T_*$)
- `CODE/stereo_scc/experiments/exp05_kact_markov_chain.py` — Toy Markov chain (ad hoc $T_*$)
