> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 03b_op_0005_layer_b_kramers_pf_dependence.md — OP-0005 Layer B: Kramers Under P-F

**Session:** 2026-05-06 (W6 Day 3 G3.3, sub-file of `03_pf_framework_escalation_core.md`).
**Goal:** How OP-0005 Layer B (Kramers K-selection) is reformulated under P-F framework (P-F-A4/A5/A6).
**Status:** Cat C outline. Full derivation W9 D2.

---

## §1. Current State of Layer B (working/MF/k_selection_b_kramers.md)

Layer B proposes K-selection via Kramers escape rates:
$$k_{K \to K-1} = \frac{\omega_0}{2\pi} \exp\!\left(-\frac{\Delta E_{\mathrm{barrier}}^{(K \to K-1)}}{k_B T}\right)$$

The file establishes:
1. The rate formula (above).
2. N-1 asymmetry recovery: $\Delta E_{\mathrm{birth}} > \Delta E_{\mathrm{merger}} \Rightarrow k_{K \to K+1} \ll k_{K \to K-1}$ at low $T$.
3. Noiseless limit: both rates → 0, forward rate dominated → NQ-253 §4.3 Claim 4.3 recovered.
4. Equilibrium distribution via detailed balance: $P(K_{\mathrm{eq}})/P(K_{\mathrm{eq}}-1) = k_{K-1 \to K}/k_{K \to K-1}$.

**Current gap:** The file uses $T$ (temperature) but SCC has no declared temperature. The "barrier $\Delta E_{\mathrm{barrier}}$" is defined as a property of the energy landscape but the underlying stochastic process is not specified.

---

## §2. Layer B Under P-F Framework

With P-F-A1 (Langevin on $\Sigma_M$) and P-F-A4/A5/A6:

**Step 1: Replace $k_B T$ with $T_*$.**
$$k_{K \to K-1} = \frac{|\lambda_-|}{2\pi} \sqrt{\frac{\det H_{\hat{\mathbf{u}}_K}}{\left|\det' H_{\mathbf{u}_{\mathrm{saddle}}^{K \to K-1}}\right|}} \cdot \exp\!\left(-\frac{\Delta E^{(K \to K-1)}}{T_*}\right)$$
where:
- $\hat{\mathbf{u}}_K \in \Sigma_M$ = the K-formation local minimizer (exists by T-Persist-K-Sep assumption).
- $\mathbf{u}_{\mathrm{saddle}}^{K \to K-1} \in \Sigma_M$ = the saddle point connecting the K-formation basin to the (K-1)-formation basin.
- $\lambda_-$ = the unique negative eigenvalue of $H_{\mathbf{u}_{\mathrm{saddle}}}$ restricted to $T_{\mathbf{u}_{\mathrm{saddle}}} \Sigma_M$.
- $\Delta E^{(K \to K-1)} = \mathcal{E}(\mathbf{u}_{\mathrm{saddle}}) - \mathcal{E}(\hat{\mathbf{u}}_K)$.

**Step 2: $\mathcal{P}$-conditioning (from stereo_observation_framework.md §6).**
When the observation $\mathfrak{O}_t$ is conditioned on a visible point cloud $\mathcal{P}_t$, the energy is:
$$\mathcal{E}_{\mathrm{cond}}(\mathbf{u} | \mathcal{P}_t) = \mathcal{E}_{\mathrm{SCC}}(\mathbf{u}) + \mathcal{L}_{\mathrm{obs}}(\mathfrak{O}_t | \mathbf{u})$$
Barriers become $\mathcal{P}$-dependent: $\Delta E^{(K \to K-1)}(\mathcal{P}_t)$ varies with the observation geometry.

**Step 3: Detailed balance → equilibrium K distribution.**
Under P-F-A3 stationary distribution $p_*$, the effective K-distribution is:
$$P_{\mathrm{eq}}(K | \mathcal{P}_t, T_*) \propto \exp\!\left(-\frac{F(K; \mathcal{P}_t)}{T_*}\right)$$
where $F(K; \mathcal{P}_t) = -T_* \log Z_K(\mathcal{P}_t)$ is the free energy of the K-formation basin (see `stereo_observation_framework.md` §7 for $Z_K(\mathcal{P}) = \int_{\mathcal{B}_K(\mathcal{P})} \exp(-\mathcal{E}_{\mathrm{SCC}}/T_*) D\tilde{u}$).

---

## §3. What This Resolves in OP-0005 Layer B

With P-F framework:

| Layer B gap (current) | Resolution under P-F |
|---|---|
| $T$ undefined | $T_*$ defined via P-F-A1 (effective temperature of Langevin noise) |
| "barrier" purely geometric | Barrier enters Kramers formula with rigorous Eyring-Kramers prefactor |
| Detailed balance informal | Formal: $p_*$ Boltzmann distribution on $\Sigma_M$ gives exact detailed balance |
| N-1 asymmetry qualitative | Quantitative: $\Delta E^{(+)} > \Delta E^{(-)}$ + Arrhenius → rate ratio computable |
| $\mathcal{P}$-conditioning ad hoc | Formal: $\mathcal{P}$-conditional energy landscape from MAP framework (stereo_observation_framework.md §4) |

---

## §4. Open Problems Remaining After P-F Integration

1. **Saddle existence on $\Sigma_M$:** Does a saddle point $\mathbf{u}_{\mathrm{saddle}}^{K \to K-1}$ connecting K-formation and (K-1)-formation basins exist generically? This is a non-trivial geometric question on the energy landscape. Related to OP-0012 (basin topology). W9 D2-D3.

2. **Hessian negative eigenvalue at saddle:** Non-degeneracy assumption (one negative eigenvalue at saddle) needs empirical verification. NQ-ST-1 proposal: compute $\det H_{\min,K}$ at representative R23 minimizers. W7 D1 (NQ-G1-2-ext) + W8 D2.

3. **Multiple saddles:** If multiple saddles connect K-formation and (K-1)-formation basins, the total rate is a sum $\sum_{\mathrm{saddles}} k_{\mathrm{saddle}}$. The dominant saddle determines the effective rate. Which saddle dominates depends on: (a) barrier height (exponential factor); (b) prefactor (algebraic factor). W9 D3.

4. **Born-Oppenheimer condition:** For the effective K-jump master equation to be valid (treating $K_{\mathrm{act}}$ as a slow variable integrating out $\tilde{u}_t$), need $\tau_{\mathrm{fast}} \ll \tau_{\mathrm{MFPT}}(K \to K-1)$. Verification requires both timescales computable. Depends on P-F-A5 + timescale separation (stereo_observation_framework.md §5). W9 D2.

---

**End of `03b_op_0005_layer_b_kramers_pf_dependence.md`. G3.3 cluster complete (3 files). Layer B reformulation under P-F outlined; 4 remaining open problems for W9 D2-D3.**
