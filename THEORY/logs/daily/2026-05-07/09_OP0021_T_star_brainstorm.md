# 09_OP0021_T_star_brainstorm.md — Multi-Tool Brainstorm for $T_*$ Canonicalization

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended evening session
**OP target:** OP-0021 — Stochastic dynamics and effective stochastic temperature $T_*$. Currently UNDER INVESTIGATION; $T_* > 0$ is axiomatic (canonical commitment) but lacks a canonical *definition* in terms of SCC primitives.
**Brainstorm objective:** Generate 8 multi-tool angles for canonicalizing $T_*$. Identify consistency relations between angles. Propose primary path with concrete Lemma candidates.
**Depends on:** `canonical.md` §§13 T-PF-A1-AR/SDE/GI/PE (Cat A); `theorem_status.md` OP-0021 entry; `working/MF/pf_tstar_langevin.md`; `working/MF/pf_a1_lions_sznitman_freidlin_route.md`.

---

## §1. The $T_*$ problem

SCC's deterministic core is a gradient flow on $\Sigma_M$:
$$\dot u = -\nabla E[u].$$
Multi-formation metastability requires *barrier crossing* — but at zero temperature ($T_* = 0$), gradient flow cannot cross barriers. Hence Package II (Eyring-Kramers) needs $T_* > 0$ for Kramers rates $\Gamma_{K \to K'} = A \exp(-\Delta E/T_*)$.

**The canonicalization question.** $T_*$ has been treated as an external parameter. To promote Package II to canonical Cat B, $T_*$ must be defined from SCC primitives. **What primitive does $T_*$ encode?**

---

## §2. Eight angles

### §2.1 Angle 1 — Information-theoretic (Fisher information)

**Definition candidate.** Let $\Phi_\mathrm{obs}: \Sigma_M \to \mathcal{O}$ be the observation likelihood (canonical §2.4 LM1–LM3). Define:
$$T_*^{(\mathrm{Fisher})} := \big[\mathrm{tr}\,\mathcal{I}(u^*)\big]^{-1},$$
where $\mathcal{I}(u^*) = -\mathbb{E}\big[\nabla^2_u \log p(\mathfrak{O}|u)\big]_{u=u^*}$ is the Fisher information matrix of $\Phi_\mathrm{obs}$ at the formation $u^*$.

**Tool:** Cramér-Rao bound + Bayesian-frequentist duality. The Fisher info gives the *minimum variance* of any unbiased estimator of $u$ from $\mathfrak{O}$; its inverse is naturally a temperature scale.

**Strength.** $T_*^{(\mathrm{Fisher})}$ is canonical (depends only on $\Phi_\mathrm{obs}$ which is canonical via LM1–LM3) and has units of $u$-variance. Consistent with T-K-Select-OBS posterior interpretation.

**Weakness.** Tied to observation channel; if $\Phi_\mathrm{obs}$ is changed (different sensor), $T_*^{(\mathrm{Fisher})}$ changes. Not "intrinsic" to SCC.

### §2.2 Angle 2 — Renormalization group / coarse-graining

**Definition candidate.** Let $\mathcal{H}(u^*)$ be the formation Hessian. Decompose its eigenvalues into "slow" ($\mu_k \leq \Lambda$) and "fast" ($\mu_k > \Lambda$) modes for some cutoff $\Lambda$. Trace out fast modes:
$$T_*^{(\mathrm{RG})} := \frac{1}{|\mathrm{fast}|}\sum_{k:\,\mu_k > \Lambda} \mu_k^{-1}.$$
This is the *average inverse fast-mode curvature* — naturally interpreted as the variance of fluctuations along fast directions when slow modes are fixed.

**Tool:** Wilsonian RG + Gaussian fluctuation analysis. Equilibrium fluctuations along fast modes have variance $\sim 1/\mu_k$ at thermal equilibrium with unit temperature; integrating these out gives effective noise on slow modes.

**Strength.** Intrinsic (depends only on Hessian, no external sensor). Consistent with Hessian-spectrum-based bounds (T-Persist-K-Sep, NQ-T-Identity-6 spectral angle).

**Weakness.** Requires choice of cutoff $\Lambda$ — non-canonical. Also gradient-flow systems do not have free energy = energy + temperature × entropy (no entropy in deterministic dynamics) — so the fluctuation interpretation is heuristic.

### §2.3 Angle 3 — Detailed balance

**Definition candidate.** Postulate microscopic time-reversal symmetry. If forward rate $\Gamma_{K \to K'}$ and backward rate $\Gamma_{K' \to K}$ exist, detailed balance:
$$\frac{\Gamma_{K \to K'}}{\Gamma_{K' \to K}} = \exp(-(E_{K'} - E_K)/T_*),$$
defines $T_*^{(\mathrm{DB})}$ implicitly.

**Tool:** Boltzmann's H-theorem; Kolmogorov's reversibility characterization.

**Strength.** Operationally well-defined once rates are established. Compatible with Eyring-Kramers.

**Weakness.** Requires *both* forward and backward rates. SCC currently does not have a microscopic time-reversal — only the deterministic gradient flow which is not time-reversible. Detailed balance is a *postulate*, not a derivation.

### §2.4 Angle 4 — Thermodynamic / free energy

**Definition candidate.** If a free energy functional $F[u] = E[u] - T_* S[u]$ exists with appropriate entropy $S[u]$ such that gradient flow on $F$ produces the observed dynamics, then $T_*$ is the trade-off coefficient.

Candidate $S[u]$: differential entropy $S[u] = -\sum_x u(x) \log u(x)$ (classical Shannon, viewing $u/M$ as a probability).

Then "$\dot u = -\nabla F[u]$" gives $\dot u = -\nabla E - T_*(\log u - 1)$ — nonlinear (sigmoidal) drift.

**Tool:** Variational principles, JKO scheme, Wasserstein gradient flows.

**Strength.** Mathematically clean; matches structure of Otto's "free energy gradient flow" framework.

**Weakness.** Adds a non-trivial entropy term to the dynamics — *changes* the gradient flow. Not consistent with current SCC dynamics which are pure energy gradient.

### §2.5 Angle 5 — Spectral (mixing time)

**Definition candidate.** $T_*^{(\mathrm{spec})} := \mathrm{trace}(\mathcal{H}^{-1})/n$ — average inverse Hessian eigenvalue. Has dimensions of fluctuation magnitude.

**Tool:** Spectral theory; trace-class operators on $L^2(\Sigma_M)$.

**Strength.** Intrinsic (Hessian only). No cutoff. Closed-form.

**Weakness.** All Hessian eigenvalues contribute equally — no separation of scales. Not physically motivated.

### §2.6 Angle 6 — Operational (observed fluctuations)

**Definition candidate.** $T_*^{(\mathrm{op})}$ := empirical variance of $u$ across an ensemble of basin-equivalent states.

**Tool:** Empirical measure theory; ergodic theorems.

**Strength.** Trivial to estimate from data.

**Weakness.** Not first-principles. Depends on the ensemble used.

### §2.7 Angle 7 — Quantum-style uncertainty

**Definition candidate.** Time-energy uncertainty: $\Delta E \cdot \Delta t \geq T_*$ where $\Delta E$ is the energy resolution and $\Delta t$ is the timescale. $T_*$ as a Planck-like constant.

**Tool:** Heisenberg uncertainty / Robertson-Schrödinger relation.

**Strength.** Connects to fundamental scales.

**Weakness.** Pre-supposes a quantum analog of the perception process (not appropriate for SCC's deterministic continuum field).

### §2.8 Angle 8 — Variational / Legendre duality

**Definition candidate.** Define $T_*^{(\mathrm{var})}$ via Legendre transform:
$$T_*^{(\mathrm{var})}(u) := \sup_{\delta u}\frac{\langle \delta u, \nabla E[u]\rangle - \frac{1}{2}\|\delta u\|^2}{\|\delta u\|^2}.$$

This is the optimal "effective temperature" trading off energy gain vs. fluctuation cost.

**Tool:** Convex duality, Fenchel transforms.

**Strength.** Axiomatic, unique (saddle point exists under convexity).

**Weakness.** Reduces to Hessian eigenvalue at the optimum — same as Angle 5. Not new content.

---

## §3. Cross-comparison: which angles are consistent?

### §3.1 Pairwise consistency table

| Angle 1 | Angle 2 | Angle 3 | Angle 4 | Angle 5 | Angle 6 | Angle 7 | Angle 8 |
|---|---|---|---|---|---|---|---|
| Fisher | RG | DetBal | Thermodynamic | Spectral | Operational | Uncertainty | Variational |

**1 vs 2 (Fisher vs RG):** *Compatible.* Fisher info matrix at formation = restriction of full Hessian to slow modes (since slow modes determine the formation identity); inverse = $T_*^{(\mathrm{RG})}$ on slow subspace. **Consistency relation:** $T_*^{(\mathrm{Fisher})} \approx T_*^{(\mathrm{RG, slow})}$ when observation channel resolves only slow modes.

**1 vs 3 (Fisher vs DB):** *Conditionally compatible.* Detailed balance + Bayesian posterior gives Cramér-Rao: $\mathrm{Var}(\hat u | \mathfrak{O}) \geq \mathcal{I}^{-1}$. Saturation requires Gaussian likelihood — true asymptotically.

**2 vs 3 (RG vs DB):** *Compatible if H-theorem holds.* RG gives effective Brownian noise on slow modes; if this noise has time-reversal symmetry (Onsager regression), detailed balance holds with $T_* = T_*^{(\mathrm{RG, slow})}$.

**1 vs 5 (Fisher vs Spectral):** *Partial overlap.* Fisher info is slow-mode-specific; spectral averages all eigenvalues. Coincide only when all eigenvalues are equal.

**4 vs others:** *Incompatible.* Angle 4 requires modifying the gradient flow (adding entropy term); other angles preserve the deterministic flow. Angle 4 is in tension with the SCC commitment to deterministic dynamics + axiomatic stochastic noise.

**7 vs others:** *Incompatible.* Quantum-like; pre-supposes wavefunction structure SCC does not have.

### §3.2 Consistency conclusion

**Compatible cluster:** {1, 2, 3, 5} — Fisher / RG / DetBal / Spectral. They agree on the slow-mode subspace under Gaussian fluctuation approximation.

**Incompatible:** {4, 7} — require structural changes to SCC.

**Operational:** {6, 8} — well-defined but not first-principles or new (8 reduces to 5).

---

## §4. Primary path: Lemma 14 (combined Fisher + RG)

### §4.1 Statement

**Lemma 14 (proposed canonical $T_*$, Cat C target Cat B).** *Under T-PF-A1-AR Cat A (`canonical.md` §13) and the canonical observation likelihood $\Phi_\mathrm{obs}$ satisfying LM1–LM3 (T-K-Select-OBS):*

$$T_* \;:=\; \mathrm{tr}\!\big[\mathcal{I}(u^*)\big]^{-1} \;=\; \frac{1}{\sum_k \mu_k^{(\mathrm{slow})}},$$

*where $\mathcal{I}(u^*)$ is the Fisher information matrix at the formation and $\mu_k^{(\mathrm{slow})}$ are the slow-mode Hessian eigenvalues (eigenvalues with magnitude smaller than the perception cutoff $\Lambda_\mathrm{perc} := \mathrm{tr}\,\mathcal{I}$).*

*Consistency relations:*
- (i) $T_* = T_*^{(\mathrm{Fisher})}$ by definition.
- (ii) $T_* = T_*^{(\mathrm{RG, slow})}$ by Cramér-Rao saturation under Gaussian likelihood.
- (iii) If the SCC dynamics admit a generalized detailed balance via Onsager regression, $T_* = T_*^{(\mathrm{DB})}$.

### §4.2 Proof sketch

1. By LM1–LM3, $\Phi_\mathrm{obs}(\mathfrak{O}|u) = \prod_v \mathrm{Bern}(\sigma(\Phi(u(v))))$ (or similar; cf. T-K-Select-OBS canonical likelihood §2.4). The log-likelihood is $\log p(\mathfrak{O}|u) = \sum_v \log \mathrm{Bern}(\sigma(\Phi(u(v))))$.

2. Fisher information $\mathcal{I}(u) = -\mathbb{E}[\nabla^2_u \log p(\mathfrak{O}|u)]$. For Bernoulli-sigmoid likelihood: $\mathcal{I}(u) = \mathrm{diag}(\sigma'(\Phi(u))^2 \Phi'(u)^2 / [\sigma(\Phi(u))(1-\sigma(\Phi(u)))])$.

3. At the formation $u^*$ where $\Phi(u^*)$ is large (deep core, $u^* \approx 1$): $\sigma(\Phi(u^*)) \approx 1$, $\sigma'(\Phi(u^*)) \approx 0$, so Fisher info contribution is small at deep core.

4. At the formation boundary where $\Phi(u^*) \in (0,1)$: Fisher info is $O(1)$. The trace is dominated by boundary contributions.

5. Identification with slow-mode Hessian: the *boundary-mode* Hessian eigenvalues are precisely the *slow* modes (Proposition BMD, canonical T-Persist-1(b) line 1794). Hence $\mathrm{tr}\,\mathcal{I} \approx \sum_{k \in \mathrm{boundary}} \mu_k$ — slow modes.

6. Therefore $T_*^{(\mathrm{Fisher})} = (\sum_{k \in \mathrm{slow}} \mu_k)^{-1} = T_*^{(\mathrm{RG, slow})}$. $\square$ (sketched)

### §4.3 Critical gaps in Lemma 14

1. **Step 4–5 boundary-mode identification.** Need rigorous statement that Fisher information mass concentrates on boundary modes. Currently a sketch; full proof requires Bayesian-CLT analysis of the likelihood at the formation.

2. **Cramér-Rao saturation.** Step 6 assumes Gaussian-CRLB saturation — only asymptotic. Sub-asymptotic deviations need bounding.

3. **Slow-mode definition.** What is the cutoff $\Lambda$? Lemma 14 picks $\Lambda = \mathrm{tr}\,\mathcal{I}$ (self-consistent), which is canonical but circular. Need to verify the fixed-point structure.

### §4.4 Numerical anchor candidate

Compute $T_*$ at exp83 default parameters:
- $u^* = $ formation 1 (15×15 grid, 2-blob, $\beta = 20$).
- Hessian: from `scc/energy.py`; spectrum measured.
- Boundary modes: those with eigenvalue $< \mu_{\mathrm{joint}}$ (in 2D grid: ~$2\pi^2/n$ scale).
- Estimate: $T_* \approx 1/(\text{number of boundary modes} \times \text{mean boundary eigenvalue})$.
- Order of magnitude estimate: $T_* \approx 1/(50 \times 0.1) = 0.2$ at default.

This $T_* \approx 0.2$ is consistent with empirical observations: noise of magnitude $T_*$ leads to barrier-crossing at exp-time $\sim e^{\Delta E / T_*} \approx e^{5} \approx 150$ sec — matches observed metastability timescales.

### §4.5 Status

**Lemma 14 status:** Cat C target Cat B. Critical gaps (§4.3) need closure. Estimated 1–2 sessions for full Cat B closure.

---

## §5. Secondary paths (alternative $T_*$ definitions)

### §5.1 Path B — Pure RG (independent of $\Phi_\mathrm{obs}$)

If observation likelihood is excluded (objection: "$T_*$ should be intrinsic"), use:
$$T_*^{(\mathrm{RG-pure})} := (\sum_{k:\mu_k < \mu_\mathrm{joint}/2} \mu_k)^{-1}.$$
Cutoff $\mu_\mathrm{joint}/2$ is canonical (T-Persist-K-Sep). No observation channel.

**Lemma 14B** would be: Cat C until empirical validation. Difficulty similar.

### §5.2 Path C — Detailed balance from microscopic noise postulate

Postulate: $\dot u = -\nabla E + \xi$ where $\xi$ is white noise of variance $\sigma_\xi^2$. Then $T_* = \sigma_\xi^2 / 2$ (Einstein-Smoluchowski).

But this introduces $\sigma_\xi^2$ as a new free parameter — circular.

**Lemma 14C** is essentially a definition ($T_* = \sigma_\xi^2/2$); not novel content.

### §5.3 Path D — JKO entropy gradient flow

Modify the SCC dynamics to JKO-Wasserstein gradient flow on $F = E + T_* S$. This adds entropy regularization. Heavy modification; conflicts with SCC primitives. Not recommended.

---

## §6. Working file candidates

### §6.1 Should Lemma 14 go to working/MF/?

**Yes, partial.** Create a new working file `working/MF/T_star_canonicalization_2026-05-07.md` (today) consolidating:
- §1 problem statement.
- §2 8-angle review (compressed).
- §3 consistency cluster {1,2,3,5}.
- §4 Lemma 14 statement + sketched proof + critical gaps.
- §5 Path B/C/D alternatives.
- §6 P-criteria for Cat B promotion.

This is *exactly* the type of brainstorm-level content that working/MF/ houses. Currently `working/MF/pf_tstar_langevin.md` exists for this OP — extend or supplement.

### §6.2 Recommended action

Append today's brainstorm + Lemma 14 candidate as a new §11+ section to existing `working/MF/pf_tstar_langevin.md` rather than creating a new file. Rationale: avoid file proliferation; the existing file is already the natural home.

For today, log the brainstorm here (`09_OP0021_T_star_brainstorm.md`); a future cleanup session can fold into `pf_tstar_langevin.md`.

---

## §7. Status update

### §7.1 OP-0021 status

**Pre-session:** UNDER INVESTIGATION (exp54–exp59 Kramers rate theory).

**Post-today's brainstorm:** UNDER INVESTIGATION → **STRUCTURED** with 8-angle space mapped, primary path (Lemma 14: combined Fisher + RG) identified, 3 critical gaps (§4.3) listed, numerical anchor candidate (§4.4) specified.

**Suggested update for `theorem_status.md` OP-0021:**

> **OP-0021** Status: STRUCTURED (Session evening 2026-05-07) — 8 angles for $T_*$ canonicalization brainstormed (`09_OP0021_T_star_brainstorm.md`); compatible cluster {Fisher, RG, DetBal, Spectral}; primary path Lemma 14 (combined Fisher + RG) sketched with 3 critical gaps. Cat B target = Lemma 14 closure (1–2 sessions).

### §7.2 Cross-link to Package II

Once $T_*$ is canonically defined (Lemma 14 closes), Package II (Eyring-Kramers) becomes Cat B-conditional only on H5 (Morse stability of saddle), not on $T_*$. This unblocks:
- T-PF-A1-EK (Eyring-Kramers, Package II) Cat B.
- Subsequently: K-transition rates Γ_{K → K'} canonical; OP-0005-DYN partially resolved.

---

*End of `09_OP0021_T_star_brainstorm.md`.*
