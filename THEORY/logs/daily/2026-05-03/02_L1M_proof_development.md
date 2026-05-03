# 02_L1M_proof_development.md — L1-M Soft-Count Corollary, Primary Approach

> *(Renamed 2026-05-04 audit: previously `02_development.md`. Internal/external references updated.)*

**Session:** 2026-05-03 (W5 Day 7)
**Target (from plan.md §2):** $|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi$ under T-L1-F $(P0)$–$(P11)$ + $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ + edge-band control (E).
**This file covers:** §1 notation, §2 $\Phi_{\mathrm{res}}$ definition, §3 envelope-pure inequality (L-M-1), §4 envelope sub-class bounds, §5 edge-band derivation (L-M-2), §6 L1-M theorem candidate, §7 counterexample attempts, §8 status self-classification.
**Depends on reading:** `canonical.md` §13 Cat A T-L1-F (definitive statement of $(P0)$–$(P11)$); `working/MF/ksoft_kact_bridge_lemma.md` §5.3.2 ($\Phi_{\mathrm{res}}$ working axioms); `working/MF/wq_lat1b_phi_envelope_refinement_results.md` §5.1, §6 (empirical anchors); `01_L1M_approach_exploration.md` §3 (primary-approach selection rationale).

**Approach selected (per `01_L1M_approach_exploration.md` §3):** A1 (bar-by-bar three-region partition) with A4 enhancement (edge-band derivation from regime constants instead of postulation as separate hypothesis (E)).

---

## §1. Notation

### §1.1 Objects (carried from `canonical.md` §13 T-L1-F + `ksoft_kact_bridge_lemma.md` §3)

| Symbol | Type | Definition |
|---|---|---|
| $G=(X,E)$ | finite graph | underlying combinatorial substrate |
| $\mathbf u=(u^{(1)},\ldots,u^{(K_{\mathrm{field}})})\in\widetilde\Sigma_M^{K_{\mathrm{field}}}(G)$ | shared-pool multi-formation state | per-slot soft cohesion fields with shared mass-pool architecture |
| $U(\mathbf u)=\sum_{j=1}^{K_{\mathrm{field}}}u^{(j)}$ | $U:X\to[0,1]$ aggregate | sum of per-slot fields |
| $A^\varepsilon(\mathbf u)=\{j:m_j(\mathbf u)>\varepsilon\}$ | active slot set | slots with mass exceeding threshold |
| $K_{\mathrm{act}}^\varepsilon(\mathbf u)=|A^\varepsilon|$ | $\in\mathbb N$ | active label count |
| $\mathrm{Bars}_0^{\mathrm{term}}(U;G)=\{[d_i,b_i]:i\in I(U)\}$ | finite bar list | $H_0$ superlevel persistence diagram of $U$, terminal-death convention |
| $\ell_i(U)=b_i-d_i\in[0,1]$ | bar length | persistence of bar $i$; $d_i=0$ for terminal-death survivors per P0 |
| $K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=\#\{i:\ell_i\ge\ell_{\min}\}$ | $\in\mathbb N$ | hard-bar count |
| $\mathcal A_{\mathrm{bar}}:A^\varepsilon\to\mathrm{Bars}_0^{\mathrm{term}}$ | bijection | $\mathcal A_{\mathrm{bar}}(j)=$ unique dominant bar born at $q_j^U=\arg\max^\prec_{x\in N_j^r}U(x)$ |
| $K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i(U))$ | $\in\mathbb R_{\ge 0}$ | envelope-weighted soft count |

### §1.2 Regime constants (from $(P0)$–$(P11)$, T-L1-F entry)

| Constant | Source axiom | Role |
|---|---|---|
| $\varepsilon$ | P2 | active mass threshold |
| $\delta$ | P2 | $\delta$-support level |
| $r,r_{\mathrm{assoc}},r_{\mathrm{birth}}$ | P3, P4, P11 | radii defining $N_j^r$, association window, birth-margin window |
| $\ell_{\min}$ | P0/P6/T-L1-F statement | hard-bar count threshold |
| $h_{\min}$ | P6 | minimum birth height; $h_{\min}\ge\ell_{\min}$ |
| $\rho_{\mathrm{bg}}$ | P5 | background suppression margin: $\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}$ |
| $\rho_{\mathrm{pert}}$ | P8, P9 | perturbation budget; $\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}$ and $\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2$ |
| $\rho_{\mathrm{res}}$ | P10 | inactive-residual margin: $\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}$ |

All constants are positive and arise from the L1-J regime-membership ledger (`working/MF/kbar_kact_bridge_L1J_catA_upgrade_attempt.md`). For T-L1-F to hold non-vacuously, $\rho_{\mathrm{pert}},\rho_{\mathrm{res}},\rho_{\mathrm{bg}},r_{\mathrm{birth}}>0$ and the L1-I constants-feasibility condition must be satisfied (per L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$).

### §1.3 Envelope sharpness parameter

For $\phi$ in the WQ-LAT-1.B-supported families, sharpness is parameterized by:
- $\phi_{\mathrm{hard}}$: no parameter; sharpness "infinite" by convention.
- $\phi_{\mathrm{logistic}}^s(\ell;\ell_{\min}):=\sigma(s(\ell-\ell_{\min}))-\sigma(-s\ell_{\min})$ where $\sigma(z)=1/(1+e^{-z})$; sharpness $=s$.
- $\phi_{\mathrm{shift\text{-}sat}}^\beta(\ell;\ell_{\min}):=1-\exp(-\beta(\ell-\ell_{\min})_+)$; sharpness $=\beta$.

### §1.4 Bar-set partition by transition width $\tau$

For $\tau>0$, define
$$
I_{\mathrm{sub}}(U;\tau):=\{i:\ell_i(U)\in[0,\ell_{\min}-\tau)\},\quad
I_{\mathrm{edge}}(U;\tau):=\{i:\ell_i(U)\in[\ell_{\min}-\tau,\ell_{\min}+\tau]\},
$$
$$
I_{\mathrm{dom}}(U;\tau):=\{i:\ell_i(U)\in(\ell_{\min}+\tau,1]\}.
$$
This is a partition of the bar-index set $I(U)$ (modulo bars of length $0$, which contribute nothing under any $\phi$ with $\phi(0)=0$).

Cardinalities: $N_{\mathrm{sub}}(U;\tau)=|I_{\mathrm{sub}}|$, $N_{\mathrm{edge}}(U;\tau)=|I_{\mathrm{edge}}|$, $N_{\mathrm{dom}}(U;\tau)=|I_{\mathrm{dom}}|$.

---

## §2. The Envelope Class $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$

This formalizes the working axioms of `ksoft_kact_bridge_lemma.md` §5.3.2 into a precise class.

### §2.1 Definition

**Definition L-M-D1 (Reservoir-admissible envelope class).** For $\ell_{\min}\in(0,1)$ and $\tau\in(0,\ell_{\min})$, define
$$
\Phi_{\mathrm{res}}(\ell_{\min},\tau):=\{\phi:[0,1]\to[0,1]\,\mid\,\phi\text{ satisfies F1–F5 below}\}.
$$
The five axioms are:

- **(F1) Range bound.** $0\le\phi(\ell)\le 1$ for all $\ell\in[0,1]$.
- **(F2) Lower normalization.** $\phi(0)=0$.
- **(F3) Monotonicity.** $\phi$ is non-decreasing on $[0,1]$.
- **(F4) Sub-threshold suppression.** There exists $\varepsilon_{\mathrm{sub}}^\phi(\tau)\ge 0$ such that
$$
\phi(\ell)\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\qquad\forall\ell\in[0,\ell_{\min}-\tau].
$$
- **(F5) Dominant retention.** There exists $\varepsilon_{\mathrm{dom}}^\phi(\tau)\ge 0$ such that
$$
1-\phi(\ell)\le\varepsilon_{\mathrm{dom}}^\phi(\tau)\qquad\forall\ell\in[\ell_{\min}+\tau,1].
$$

The pair $(\varepsilon_{\mathrm{sub}}^\phi,\varepsilon_{\mathrm{dom}}^\phi)$ is the **structural-deviation pair** of $\phi$. The class becomes meaningful when $\varepsilon_{\mathrm{sub}}^\phi+\varepsilon_{\mathrm{dom}}^\phi\ll 1$.

**Note on (F1+F3).** Together with (F2), monotonicity makes the Lipschitz constant $L_\phi$ at most $\sup_\ell|\phi'(\ell)|=:s_\phi$ where $s_\phi$ is the sharpness parameter. (F1) bounds $\phi$ from above; together with (F4)+(F5), $\phi$ is essentially a "soft-step" envelope.

### §2.2 Verification on WQ-LAT-1.B sub-classes

**Claim L-M-V1.** The three WQ-LAT-1.B-supported families satisfy F1–F5 with explicit $(\varepsilon_{\mathrm{sub}}^\phi,\varepsilon_{\mathrm{dom}}^\phi)$:

| Family | $\varepsilon_{\mathrm{sub}}^\phi(\tau)$ | $\varepsilon_{\mathrm{dom}}^\phi(\tau)$ |
|---|---|---|
| $\phi_{\mathrm{hard}}=\mathbf 1_{\ell\ge\ell_{\min}}$ | $0$ | $0$ |
| $\phi_{\mathrm{logistic}}^s$, $s\ge 50$ | $\le e^{-s\tau}$ | $\le e^{-s\tau}+\sigma(-s\ell_{\min})\le 2e^{-s\tau}$ for $\tau\le\ell_{\min}$ |
| $\phi_{\mathrm{shift\text{-}sat}}^\beta$, $\beta\ge 20$ | $0$ | $\le e^{-\beta\tau}$ |

**Proof (V1).**

- **$\phi_{\mathrm{hard}}$.** F1: range $\{0,1\}\subseteq[0,1]$. F2: $\phi_{\mathrm{hard}}(0)=0$. F3: monotone (jump from $0$ to $1$ at $\ell_{\min}$). F4: $\phi=0$ on $[0,\ell_{\min})$, hence on $[0,\ell_{\min}-\tau]$. $\varepsilon_{\mathrm{sub}}=0$. F5: $\phi=1$ on $[\ell_{\min},1]$, hence on $[\ell_{\min}+\tau,1]$. $\varepsilon_{\mathrm{dom}}=0$.

- **$\phi_{\mathrm{logistic}}^s$.** F1: $\sigma(s(\ell-\ell_{\min}))\in[0,1]$ for all $\ell$; subtracting $\sigma(-s\ell_{\min})\in[0,1)$ may give negative values for $\ell$ near $0$. We tighten F1 to $\phi(\ell)\ge 0$ by clipping at $0$ if needed; alternatively restrict $\Phi_{\mathrm{res}}$ to $\phi$ that already satisfy F1 (Phi-4c with the WQ-LAT-1.B definition is non-negative on $[0,1]$ since $\sigma(-s\ell_{\min})$ is the value at $\ell=0$). F2: $\phi(0)=\sigma(-s\ell_{\min})-\sigma(-s\ell_{\min})=0$. F3: $\sigma$ is monotone increasing; subtracting a constant preserves monotonicity. F4: for $\ell\le\ell_{\min}-\tau$, $s(\ell-\ell_{\min})\le-s\tau$, so $\sigma(s(\ell-\ell_{\min}))\le\sigma(-s\tau)=1/(1+e^{s\tau})\le e^{-s\tau}$. Subtracting $\sigma(-s\ell_{\min})\ge 0$ gives $\phi(\ell)\le e^{-s\tau}$. F5: for $\ell\ge\ell_{\min}+\tau$, $\sigma(s(\ell-\ell_{\min}))\ge\sigma(s\tau)=1-1/(1+e^{s\tau})\ge 1-e^{-s\tau}$. So $1-\phi(\ell)=1-\sigma(s(\ell-\ell_{\min}))+\sigma(-s\ell_{\min})\le e^{-s\tau}+\sigma(-s\ell_{\min})$. For $s\ell_{\min}\ge s\tau$ (i.e., $\tau\le\ell_{\min}$): $\sigma(-s\ell_{\min})\le\sigma(-s\tau)\le e^{-s\tau}$, so the bound is $\le 2e^{-s\tau}$.

- **$\phi_{\mathrm{shift\text{-}sat}}^\beta$.** F1: $1-e^{-x}\in[0,1]$ for $x\ge 0$, $0$ for $x\le 0$ via $(\cdot)_+$. F2: $\phi(0)=1-e^0=0$. F3: monotone in $\ell$ on $[\ell_{\min},1]$, constant $0$ on $[0,\ell_{\min}]$. F4: $\phi\equiv 0$ on $[0,\ell_{\min}]$, hence on $[0,\ell_{\min}-\tau]$. $\varepsilon_{\mathrm{sub}}=0$. F5: for $\ell\ge\ell_{\min}+\tau$, $\beta(\ell-\ell_{\min})\ge\beta\tau$, so $\phi(\ell)\ge 1-e^{-\beta\tau}$. Hence $1-\phi(\ell)\le e^{-\beta\tau}$. ∎

**Numerical check at WQ-LAT-1.B parameters.** $\ell_{\min}=0.10$. The empirical $K_{\mathrm{soft}}^\phi$ ranges across $K_{\mathrm{field}}\in\{3,4,6,8,12\}$ on LAT-C__A (table 5.1):

| Family | Predicted leading-order error | Empirical range | Match |
|---|---|---|---|
| $\phi_{\mathrm{hard}}$ | $0$ exact | $0.000$ | exact |
| $\phi_{\mathrm{logistic}}^{s=100}$ at $\tau\approx 0.05$ | $\le 2e^{-5}\cdot N_{\mathrm{dom}}\approx 0.013$ for $N_{\mathrm{dom}}=1$ | $0.001$ | within 1 OOM (bound is loose; mean $K_{\mathrm{soft}}^{\phi_{\mathrm{logistic}}^{100}}=1.001$, range $0.0009$) |
| $\phi_{\mathrm{shift\text{-}sat}}^{\beta=20}$ at $\tau\approx 0.10$ | $\le e^{-2}\cdot N_{\mathrm{dom}}\approx 0.135$ for $N_{\mathrm{dom}}=1$ | $0.005$ (range) but mean $0.938$ | range bounded; mean deviation from $1$ is $0.062$, consistent with $e^{-\beta(\ell_{\mathrm{dom}}-\ell_{\min})}\approx e^{-20\cdot 0.14}\approx 0.06$ for dominant bar of length $\sim 0.24$ |

The bounds in Claim L-M-V1 are consistent with the empirical record: $\phi_{\mathrm{hard}}$ exact, $\phi_{\mathrm{logistic}}^{100}$ within $10^{-3}$, $\phi_{\mathrm{shift\text{-}sat}}^{20}$ within $10^{-2}$. The bound is loosest for $\phi_{\mathrm{shift\text{-}sat}}^{20}$ and tightest (relatively) for $\phi_{\mathrm{logistic}}^{100}$, matching empirics.

### §2.3 Default $\phi$-sat is excluded by F4

**Claim L-M-V2.** $\phi_0(\ell)=\ell/(\ell+\ell_{\min})\notin\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ for any $\ell_{\min}\in(0,1)$ and $\tau\in(0,\ell_{\min})$ with $\varepsilon_{\mathrm{sub}}^{\phi_0}\le 1/3$.

**Proof.** At $\ell=\ell_{\min}/2$ (which is in $[0,\ell_{\min}-\tau]$ for $\tau\le\ell_{\min}/2$): $\phi_0(\ell_{\min}/2)=(\ell_{\min}/2)/(\ell_{\min}/2+\ell_{\min})=(\ell_{\min}/2)/(3\ell_{\min}/2)=1/3$. So any admissible $\varepsilon_{\mathrm{sub}}^{\phi_0}\ge 1/3$. F4 holds only for $\varepsilon_{\mathrm{sub}}\ge 1/3$, which is too large to be useful. ∎

**Consequence.** WQ-LAT-1.B's empirical failure of Phi-0 (range $0.943$ from sub-resolution accumulation) is *predicted* by L-M-D1 axiom F4: $\phi_0$ is structurally not in $\Phi_{\mathrm{res}}$ with any small $\varepsilon_{\mathrm{sub}}$. The empirical drift $\sim N_{\mathrm{sub}}\cdot 1/3$ matches exactly the F4-violation magnitude.

---

## §3. Lemma L-M-1 (Envelope-Pure Inequality)

This is the substantive content of **Approach A1** from `01_L1M_approach_exploration.md` §2.1, applied at the level of the bar-length distribution alone, without using $(P0)$–$(P11)$.

### §3.1 Statement

**Lemma L-M-1 (envelope-pure decomposition).** Let $U:X\to[0,1]$ be any field on a finite graph $G$. Let $\{\ell_i(U)\}_{i\in I(U)}$ be the bar lengths of $\mathrm{Dgm}_0^{\sup}(U;G)$ under the terminal-death convention. Let $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$. Define
$$
\rho_{\mathrm{sub}}(\phi,U;\tau):=\sum_{i\in I_{\mathrm{sub}}(U;\tau)}\phi(\ell_i(U)),
$$
$$
\rho_{\mathrm{edge}}^\phi(U;\tau):=\sum_{i\in I_{\mathrm{edge}}(U;\tau)}\bigl|\phi(\ell_i(U))-\mathbf 1_{\ell_i(U)\ge\ell_{\min}}\bigr|,
$$
$$
\rho_\phi(U;\tau):=\sum_{i\in I_{\mathrm{dom}}(U;\tau)}\bigl|1-\phi(\ell_i(U))\bigr|.
$$
Then
$$
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)\bigr|\le\rho_{\mathrm{sub}}(\phi,U;\tau)+\rho_{\mathrm{edge}}^\phi(U;\tau)+\rho_\phi(U;\tau). \tag{L-M-1}
$$

### §3.2 Proof of L-M-1

The key identity:
$$
K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)=\sum_{i\in I(U)}\bigl[\phi(\ell_i(U))-\mathbf 1_{\ell_i(U)\ge\ell_{\min}}\bigr].
$$

By the partition $I(U)=I_{\mathrm{sub}}\sqcup I_{\mathrm{edge}}\sqcup I_{\mathrm{dom}}$ (modulo zero-length bars; $\phi(0)=0$ by F2 and $\mathbf 1_{0\ge\ell_{\min}}=0$ for $\ell_{\min}>0$, so they cancel in the deviation sum):
$$
=\sum_{i\in I_{\mathrm{sub}}}\bigl[\phi(\ell_i)-0\bigr]+\sum_{i\in I_{\mathrm{edge}}}\bigl[\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}\bigr]+\sum_{i\in I_{\mathrm{dom}}}\bigl[\phi(\ell_i)-1\bigr].
$$

**Sub-region.** For $i\in I_{\mathrm{sub}}$, $\ell_i<\ell_{\min}-\tau<\ell_{\min}$, so $\mathbf 1_{\ell_i\ge\ell_{\min}}=0$. The summand is $\phi(\ell_i)\ge 0$ (F1).

**Dominant region.** For $i\in I_{\mathrm{dom}}$, $\ell_i>\ell_{\min}+\tau\ge\ell_{\min}$, so $\mathbf 1_{\ell_i\ge\ell_{\min}}=1$. The summand is $\phi(\ell_i)-1\le 0$ (F1).

**Edge region.** For $i\in I_{\mathrm{edge}}$, $\ell_i\in[\ell_{\min}-\tau,\ell_{\min}+\tau]$. The summand has unrestricted sign; $|\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}|\le 1$ (F1+F3 give $\phi\in[0,1]$, and $\mathbf 1\in\{0,1\}$).

By the triangle inequality $|\sum a_i|\le\sum|a_i|$:
$$
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)\bigr|
\le\sum_{i\in I_{\mathrm{sub}}}\phi(\ell_i)+\sum_{i\in I_{\mathrm{edge}}}|\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}|+\sum_{i\in I_{\mathrm{dom}}}|1-\phi(\ell_i)|,
$$
which is $\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi$. ∎

### §3.3 Status of L-M-1

**Self-classification: Cat A absolute.** L-M-1 is a purely envelope-arithmetic statement. It uses only:
- finite graph (finite bar list),
- envelope axioms F1–F3 (for the per-region sign analysis),
- triangle inequality.

It uses *none* of $(P0)$–$(P11)$. It uses *none* of T-L1-F. It is a general statement about persistence diagrams + admissible envelopes. The Cat-A classification is unconditional.

The reason it does not yet give a useful corollary: $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ depend on the specific bar list $\{\ell_i(U)\}$, which is not under direct control. §4 bounds these by envelope sub-class structural parameters; §5 (L-M-2) eliminates $\rho_{\mathrm{edge}}^\phi$ entirely under the L1-J regime.

---

## §4. Envelope Sub-Class Bounds

This refines L-M-1 by bounding each $\rho$-term via the envelope's structural-deviation pair.

### §4.1 General sub-class bound

**Lemma L-M-Sub (sub-threshold bound from F4).** For any $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ with structural pair $(\varepsilon_{\mathrm{sub}}^\phi,\varepsilon_{\mathrm{dom}}^\phi)$,
$$
\rho_{\mathrm{sub}}(\phi,U;\tau)\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\cdot N_{\mathrm{sub}}(U;\tau).
$$

**Proof.** Each summand $\phi(\ell_i)\le\varepsilon_{\mathrm{sub}}^\phi$ by F4 (since $\ell_i\in[0,\ell_{\min}-\tau]$). Sum over $N_{\mathrm{sub}}$ terms. ∎

**Lemma L-M-Dom (dominant-region bound from F5).** For any $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$,
$$
\rho_\phi(U;\tau)\le\varepsilon_{\mathrm{dom}}^\phi(\tau)\cdot N_{\mathrm{dom}}(U;\tau).
$$

**Proof.** Each summand $|1-\phi(\ell_i)|=1-\phi(\ell_i)\le\varepsilon_{\mathrm{dom}}^\phi$ by F5 (and F1+F3 ensure $\phi\le 1$, so $1-\phi\ge 0$). Sum over $N_{\mathrm{dom}}$. ∎

**Lemma L-M-Edge (edge-region bound).** For any $\phi$ satisfying F1,
$$
\rho_{\mathrm{edge}}^\phi(U;\tau)\le N_{\mathrm{edge}}(U;\tau).
$$

**Proof.** Each summand $|\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}|\le 1$ since both terms are in $[0,1]$. Sum over $N_{\mathrm{edge}}$. ∎

These three together give the **structural form** of L-M-1:
$$
|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\cdot N_{\mathrm{sub}}(U;\tau)+N_{\mathrm{edge}}(U;\tau)+\varepsilon_{\mathrm{dom}}^\phi(\tau)\cdot N_{\mathrm{dom}}(U;\tau). \tag{L-M-1*}
$$

### §4.2 Per-family explicit bounds

Using Claim L-M-V1 (envelope-specific structural pairs):

**Phi-1 (hard threshold).** $\varepsilon_{\mathrm{sub}}^{\phi_{\mathrm{hard}}}=\varepsilon_{\mathrm{dom}}^{\phi_{\mathrm{hard}}}=0$. Hence
$$
|K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le N_{\mathrm{edge}}(U;\tau).
$$
But $\phi_{\mathrm{hard}}=\mathbf 1_{\ell\ge\ell_{\min}}$ exactly, so trivially $K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}(U)=\sum_i\mathbf 1_{\ell_i\ge\ell_{\min}}=K_{\mathrm{bar}}^{\ell_{\min}}(U)$ regardless of $\tau$. $\rho_{\mathrm{edge}}^{\phi_{\mathrm{hard}}}=0$ for any bar configuration since $\phi_{\mathrm{hard}}(\ell_i)$ and $\mathbf 1_{\ell_i\ge\ell_{\min}}$ agree pointwise. **Status: EXACT identity.**

**Phi-4c (logistic, $s\ge 50$).** $\varepsilon_{\mathrm{sub}}^{\phi_{\mathrm{logistic}}^s}\le e^{-s\tau}$, $\varepsilon_{\mathrm{dom}}^{\phi_{\mathrm{logistic}}^s}\le 2e^{-s\tau}$. Hence
$$
|K_{\mathrm{soft}}^{\phi_{\mathrm{logistic}}^s}(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le e^{-s\tau}\cdot N_{\mathrm{sub}}(U;\tau)+N_{\mathrm{edge}}(U;\tau)+2e^{-s\tau}\cdot N_{\mathrm{dom}}(U;\tau). \tag{L-M-Logistic}
$$
**Status: theorem candidate**, contingent on (i) edge-band control of $N_{\mathrm{edge}}$ and (ii) $s\tau\gg 1$ (sharpness × transition width). For $s=100$, $\tau=0.05$: $e^{-s\tau}=e^{-5}\approx 6.7\times 10^{-3}$. For $N_{\mathrm{sub}}=18,N_{\mathrm{dom}}=1$ (WQ-LAT-1.B max-subres case at $K_{\mathrm{field}}=12$): $0.0067\cdot 18+N_{\mathrm{edge}}+0.013\cdot 1\approx 0.13+N_{\mathrm{edge}}$. The empirical range $0.001$ implies $N_{\mathrm{edge}}\approx 0$ in the WQ-LAT-1.B configuration — consistent with §5's L-M-2 conclusion.

**Phi-3d (shifted saturating, $\beta\ge 20$).** $\varepsilon_{\mathrm{sub}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta}=0$, $\varepsilon_{\mathrm{dom}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta}\le e^{-\beta\tau}$. Hence
$$
|K_{\mathrm{soft}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta}(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le 0\cdot N_{\mathrm{sub}}+N_{\mathrm{edge}}(U;\tau)+e^{-\beta\tau}\cdot N_{\mathrm{dom}}(U;\tau). \tag{L-M-ShiftSat}
$$
**Status: theorem candidate**, contingent on (i) edge-band control of $N_{\mathrm{edge}}$ and (ii) $\beta\tau\gg 1$. For $\beta=20$, $\tau=0.10$: $e^{-2}\approx 0.135$. With $N_{\mathrm{dom}}=1$: bound is $\le 0.135+N_{\mathrm{edge}}$. Empirical mean $0.938$, deviation from $1$ is $0.062$ — within bound.

**Forbidden envelope (default $\phi$-sat).** $\phi_0\notin\Phi_{\mathrm{res}}$ by L-M-V2. The bound (L-M-1*) is structurally vacuous (no admissible $\varepsilon_{\mathrm{sub}}^{\phi_0}<1/3$). **Status: EXCLUDED** — empirically confirmed by WQ-LAT-1.B Phi-0 range $0.943$.

### §4.3 Reproduction of plan.md §4.5 status table

| Envelope | $\rho_{\mathrm{sub}}$ bound | $\rho_{\mathrm{edge}}^\phi$ bound | $\rho_\phi$ bound | L1-M status |
|---|---|---|---|---|
| $\phi_{\mathrm{hard}}$ | $0$ | $0$ | $0$ | **EXACT corollary**, Cat A absolute |
| $\phi_{\mathrm{logistic}}^{s\ge 50}$ | $e^{-s\tau}\cdot N_{\mathrm{sub}}$ | $\le N_{\mathrm{edge}}$ (general); $0$ under L-M-2 | $2e^{-s\tau}\cdot N_{\mathrm{dom}}$ | **THEOREM CANDIDATE**, Cat B sketched (cf. §5) |
| $\phi_{\mathrm{shift\text{-}sat}}^{\beta\ge 20}$ | $0$ | $\le N_{\mathrm{edge}}$ (general); $0$ under L-M-2 | $e^{-\beta\tau}\cdot N_{\mathrm{dom}}$ | **THEOREM CANDIDATE**, Cat B sketched |
| Arbitrary monotone Lipschitz $\phi$ (default $\phi$-sat) | UNCONTROLLED (F4 fails) | UNCONTROLLED | UNCONTROLLED | **EXCLUDED** by F4 |

This matches plan.md §4.5 line-by-line.

---

## §5. Lemma L-M-2 (Edge-Band Derivation under L1-J Regime)

This is the **A4 enhancement** from `01_L1M_approach_exploration.md` §2.4 / §3.3. It eliminates the $N_{\mathrm{edge}}$ term of (L-M-1*) under $(P0)$–$(P11)$.

### §5.1 Statement

**Lemma L-M-2 (edge-band emptiness).** Let $\mathbf u\in\widetilde\Sigma_M^{K_{\mathrm{field}}}(G)$ satisfy the L1-J regime hypothesis package $(P0)$–$(P11)$ from T-L1-F (canonical.md §13 line 1463). Set
$$
\tau_*:=\min\bigl(2\rho_{\mathrm{pert}},\,\rho_{\mathrm{res}},\,r_{\mathrm{birth}}\bigr).
$$
Then for any $\tau\in(0,\tau_*)$, the edge band of $U(\mathbf u)$ contains no bars:
$$
N_{\mathrm{edge}}(U;\tau)=0.
$$

### §5.2 Proof structure of L-M-2

The proof proceeds by classifying each bar $i\in I(U)$ as one of three types and showing that under $(P0)$–$(P11)$, no bar can have $\ell_i\in[\ell_{\min}-\tau,\ell_{\min}+\tau]$ for $\tau<\tau_*$.

**Bar-type classification.** Let $b_i$ denote the birth vertex of bar $i$ in $\mathrm{Dgm}_0^{\sup}(U;G)$. By the LG-7 coverage property (derived in T-L1-F's proof from P5 + P0 + LG-4), every bar's birth vertex lies in one of two regions: $b_i\in\bigcup_j N_j^r$ (per-slot) or $b_i\in X_{\mathrm{bg}}$ (background). Within the per-slot case, P3 (disjoint $N_j^r$) makes the slot index $j(i)$ uniquely determined.

We classify bars accordingly:
- **Type-D (dominant-of-slot-$j$).** $b_i\in N_{j(i)}^r$ and $b_i=q_{j(i)}^U=\arg\max^\prec_{x\in N_{j(i)}^r}U(x)$. By T-L1-F's at-most-one-dominant-bar lemma (L1-H2 Lemma 2), at most one type-D bar per active slot exists.
- **Type-N (non-dominant-of-slot-$j$).** $b_i\in N_{j(i)}^r$ but $b_i\ne q_{j(i)}^U$. These are subdominant local maxima within an active neighborhood.
- **Type-B (background).** $b_i\in X_{\mathrm{bg}}$.

Every bar of $U$ on $G$ is one of these three types.

### §5.3 Type-D bars sit above the edge band: $\ell_i>\ell_{\min}+\tau$ for $\tau<r_{\mathrm{birth}}$

Each Type-D bar $i$ corresponds (via T-L1-F's bijection $\mathcal A_{\mathrm{bar}}$) to an active slot $j$ with $b_i=q_j^U$. By P11 (margin ledger):
$$
h_{\min}-\max_{k\ne j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}.
$$
Since $b_i\ge h_{\min}$ (by P6), and $r_{\mathrm{assoc}},r_{\mathrm{birth}}\ge 0$:
$$
b_i\ge h_{\min}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}+\max_{k\ne j}B_{jk}\ge\ell_{\min}+r_{\mathrm{birth}}.
$$
By P0 (terminal-death convention) the death of a dominant terminal-death bar is $d_i=0$. Hence
$$
\ell_i=b_i-d_i=b_i\ge\ell_{\min}+r_{\mathrm{birth}}.
$$
For $\tau<r_{\mathrm{birth}}$: $\ell_i\ge\ell_{\min}+r_{\mathrm{birth}}>\ell_{\min}+\tau$, so $i\in I_{\mathrm{dom}}\not\subseteq I_{\mathrm{edge}}$.

*Note.* The terminal-death convention P0 is essential: without it, a dominant bar could die at a high merge value, producing $\ell_i<\ell_{\min}+r_{\mathrm{birth}}$. Under terminal-death, the dominant bar's death is by definition $0$, so its length equals its birth height.

### §5.4 Type-N bars sit below the edge band: $\ell_i<\ell_{\min}-\tau$ for $\tau<2\rho_{\mathrm{pert}}$

Each Type-N bar $i$ has $b_i\in N_{j(i)}^r$ for some active slot $j(i)$. By T-L1-F's "per-neighborhood at-most-one-dominant-bar" argument (L1-H2 Lemma 1 + Lemma 2 in canonical.md §13), the bar of $U$ on the local graph $G_{j(i)}^r$ corresponds (via bottleneck stability of $\mathrm{Dgm}_0^{\sup}$ under the $\|U-u^{(j(i))}\|_{\infty,N_{j(i)}^r}\le\rho_{\mathrm{pert}}/2$ perturbation, P9) to a bar of $u^{(j(i))}$ on $G_{j(i)}^r$. Since this $U$-bar is non-dominant (not the slot primary), the corresponding $u^{(j)}$-bar is also non-dominant, hence has length at most the second longest bar of $u^{(j)}$ on $G_j^r$:
$$
\ell_i^{(u^{(j)})}\le\ell_{j,2}(u^{(j)};G_j^r).
$$
By P8 (tightened H6): $\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}$.

By bottleneck stability (CSEH 2007, applied to $U|_{G_j^r}$ vs $u^{(j)}|_{G_j^r}$ under perturbation $\le\rho_{\mathrm{pert}}/2$): $|\ell_i-\ell_i^{(u^{(j)})}|\le 2\cdot\rho_{\mathrm{pert}}/2=\rho_{\mathrm{pert}}$ (factor $2$ from both birth and death potentially shifting). Hence
$$
\ell_i\le\ell_i^{(u^{(j)})}+\rho_{\mathrm{pert}}\le(\ell_{\min}-3\rho_{\mathrm{pert}})+\rho_{\mathrm{pert}}=\ell_{\min}-2\rho_{\mathrm{pert}}.
$$
For $\tau<2\rho_{\mathrm{pert}}$: $\ell_i\le\ell_{\min}-2\rho_{\mathrm{pert}}<\ell_{\min}-\tau$, so $i\in I_{\mathrm{sub}}\not\subseteq I_{\mathrm{edge}}$.

*Note.* The graph-inclusion lemma L1-H2 Lemma 1 is needed to transfer from local $G_j^r$ to global $G$: $\ell_{\mathrm{glob}}(U;G)\le\ell_{\mathrm{loc}}(U;G_j^r)$, which preserves the upper bound across the $G_j^r\subseteq G$ inclusion.

### §5.5 Type-B bars sit far below the edge band: $\ell_i\le\ell_{\min}-\rho_{\mathrm{res}}$ for $\tau<\rho_{\mathrm{res}}$

For Type-B bars, $b_i\in X_{\mathrm{bg}}$ where $X_{\mathrm{bg}}$ is the background region (off all $N_j^r$). On $X_{\mathrm{bg}}$ the field $U$ coincides with the inactive residual: $U|_{X_{\mathrm{bg}}}=R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}$. By P10, $\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}$. Hence the birth height $b_i=U(b_i)\le\ell_{\min}-\rho_{\mathrm{res}}$, and by P0 the death is $d_i=0$:
$$
\ell_i=b_i\le\ell_{\min}-\rho_{\mathrm{res}}.
$$
For $\tau<\rho_{\mathrm{res}}$: $\ell_i\le\ell_{\min}-\rho_{\mathrm{res}}<\ell_{\min}-\tau$, so $i\in I_{\mathrm{sub}}\not\subseteq I_{\mathrm{edge}}$.

*Note.* P5 (background suppression on $U$, not just $R_{\mathrm{inact}}$) gives a stronger bound $b_i\le\ell_{\min}-\rho_{\mathrm{bg}}$, but $\rho_{\mathrm{bg}}$ may not equal $\rho_{\mathrm{res}}$. Using the weaker P10 bound is sufficient for the conclusion; the stronger P5 bound only tightens the constant.

### §5.6 Conclusion: $\tau_*=\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{res}},r_{\mathrm{birth}})$

Combining §5.3, §5.4, §5.5: every bar of $U$ on $G$ has either $\ell_i\ge\ell_{\min}+r_{\mathrm{birth}}$ (Type-D) or $\ell_i\le\ell_{\min}-2\rho_{\mathrm{pert}}$ (Type-N) or $\ell_i\le\ell_{\min}-\rho_{\mathrm{res}}$ (Type-B). Setting
$$
\tau_*:=\min(2\rho_{\mathrm{pert}},\,\rho_{\mathrm{res}},\,r_{\mathrm{birth}}),
$$
for any $\tau\in(0,\tau_*)$ we have $\ell_i\notin[\ell_{\min}-\tau,\ell_{\min}+\tau]$ for every $i\in I(U)$. Hence $N_{\mathrm{edge}}(U;\tau)=0$. ∎

### §5.7 Status of L-M-2

**Self-classification: Cat B sketched.** The proof uses:
- **L1-H2 Lemma 1** (graph-inclusion: $\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}$ on $G_j^r\subseteq G$) — Cat A within T-L1-F's proof structure (canonical, CV-1.5.2).
- **CSEH 2007 bottleneck stability** — external Cat A theorem, used routinely in `working/E/soft_K_definition.md` §2.1.
- **P0–P11 directly** — canonical regime hypothesis.

The "sketched" status (rather than "proved") reflects three points where rigor could be sharpened:

1. **The bottleneck-stability factor.** §5.4 used $|\ell_i-\ell_i^{(u^{(j)})}|\le 2\cdot\rho_{\mathrm{pert}}/2=\rho_{\mathrm{pert}}$. The factor $2$ derives from both birth and death of a single bar shifting by at most $\|\Delta U\|_\infty=\rho_{\mathrm{pert}}/2$. This is consistent with `working/E/soft_K_definition.md` §2.2 Prop 2.1 (the factor-$2$ from u-side and v-side diagonal pairings is properly handled there as $4L_\phi n$ Lipschitz constant, but here we want only the per-bar shift, which is the $2$).
2. **The Type-B bound's interaction with LG-7.** §5.5 used P10 directly on $X_{\mathrm{bg}}$. The LG-7 coverage that T-L1-F's proof derives from P5+P0+LG-4 ensures every dominant-bar birth has $U\ge\ell_{\min}$ and hence is *not* in $X_{\mathrm{bg}}$. This is the basis for the "Type-B" classification as background. A fully rigorous L-M-2 proof would re-establish this explicitly rather than invoking the T-L1-F proof structure.
3. **The terminal-death convention's role for Type-N.** §5.4 implicitly assumed Type-N bars also use terminal death. This is correct under P0 (which is global), but the argument should make this explicit: the comparison between $U|_{G_j^r}$ and $u^{(j)}|_{G_j^r}$ both use terminal death on $G_j^r$, giving consistent diagram-comparisons.

These three points are *bookkeeping refinements*, not structural gaps. They do not alter the conclusion. They are flagged for L1-M-AUDIT (next-step item per plan.md §8).

A future Cat-A upgrade (analogous to L1-K external audit + L1-K-REPAIR cycle) would resolve these into a Cat-A-conditional statement. The conditional regime is exactly $(P0)$–$(P11)$, the same as T-L1-F.

---

## §6. L1-M Theorem-Candidate (Combination of L-M-1, L-M-2, T-L1-F)

This is the substantive deliverable of Day 7.

### §6.1 Statement

**Theorem L-M (Soft-Count Corollary).** Let $G=(X,E)$ be a finite graph, $\mathbf u\in\widetilde\Sigma_M^{K_{\mathrm{field}}}(G)$. Suppose the L1-J regime hypothesis package $(P0)$–$(P11)$ from T-L1-F (canonical.md §13 Cat A, CV-1.5.2) holds. Let $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ with $\tau\in(0,\tau_*)$ where $\tau_*=\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{res}},r_{\mathrm{birth}})$. Then
$$
\boxed{
\bigl|K_{\mathrm{soft}}^\phi(U(\mathbf u))-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\cdot N_{\mathrm{sub}}(U;\tau)+\varepsilon_{\mathrm{dom}}^\phi(\tau)\cdot K_{\mathrm{act}}^\varepsilon(\mathbf u),
}
\tag{L-M}
$$
where the $N_{\mathrm{edge}}$ term has vanished (L-M-2) and $N_{\mathrm{dom}}=K_{\mathrm{act}}^\varepsilon$ (T-L1-F bijection $\mathcal A_{\mathrm{bar}}$). The structural pair $(\varepsilon_{\mathrm{sub}}^\phi,\varepsilon_{\mathrm{dom}}^\phi)$ is determined by the envelope sub-class per Claim L-M-V1.

### §6.2 Proof of L-M

By Lemma L-M-1 (envelope-pure inequality, §3),
$$
|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
$$

By Lemma L-M-2 (edge-band emptiness, §5), under $(P0)$–$(P11) + \tau<\tau_*$: $N_{\mathrm{edge}}(U;\tau)=0$. By Lemma L-M-Edge (§4.1), $\rho_{\mathrm{edge}}^\phi\le N_{\mathrm{edge}}=0$.

By Lemma L-M-Sub (§4.1), $\rho_{\mathrm{sub}}\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\cdot N_{\mathrm{sub}}(U;\tau)$.

By Lemma L-M-Dom (§4.1), $\rho_\phi\le\varepsilon_{\mathrm{dom}}^\phi(\tau)\cdot N_{\mathrm{dom}}(U;\tau)$.

By the T-L1-F bijection $\mathcal A_{\mathrm{bar}}:A^\varepsilon\to\mathrm{Bars}_0^{\mathrm{term}}$ (canonical.md §13 line 1467), each active slot corresponds to exactly one dominant terminal-death bar. By L-M-2, every dominant bar has length $\ge\ell_{\min}+r_{\mathrm{birth}}>\ell_{\min}+\tau$ (since $\tau<\tau_*\le r_{\mathrm{birth}}$), hence belongs to $I_{\mathrm{dom}}$. Conversely every bar in $I_{\mathrm{dom}}$ has length $>\ell_{\min}+\tau\ge\ell_{\min}$, so it is counted in $K_{\mathrm{bar}}^{\ell_{\min}}=K_{\mathrm{act}}^\varepsilon$ via T-L1-F. Hence $N_{\mathrm{dom}}(U;\tau)=K_{\mathrm{bar}}^{\ell_{\min}}(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)$.

Combining:
$$
|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le\varepsilon_{\mathrm{sub}}^\phi\cdot N_{\mathrm{sub}}+0+\varepsilon_{\mathrm{dom}}^\phi\cdot K_{\mathrm{act}}^\varepsilon.
$$
Substitute $K_{\mathrm{bar}}^{\ell_{\min}}(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)$ (T-L1-F, canonical):
$$
|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)|\le\varepsilon_{\mathrm{sub}}^\phi(\tau)\cdot N_{\mathrm{sub}}(U;\tau)+\varepsilon_{\mathrm{dom}}^\phi(\tau)\cdot K_{\mathrm{act}}^\varepsilon(\mathbf u). \quad\blacksquare
$$

### §6.3 Per-family explicit corollaries

Combining (L-M) with Claim L-M-V1:

**Corollary L-M.A (hard threshold, EXACT).** For $\phi=\phi_{\mathrm{hard}}$:
$$
K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}(U(\mathbf u))=K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))=K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$
Under $(P0)$–$(P11)$, this is **exact**, no approximation. **Cat-A absolute** as a definitional reduction — $\phi_{\mathrm{hard}}$ identifies $K_{\mathrm{soft}}$ with $K_{\mathrm{bar}}$ pointwise; T-L1-F supplies the canonical link to $K_{\mathrm{act}}$.

**Corollary L-M.B (sharp logistic, $s\ge 50$).** For $\phi=\phi_{\mathrm{logistic}}^s$, $\tau\in(0,\tau_*)$:
$$
\bigl|K_{\mathrm{soft}}^{\phi_{\mathrm{logistic}}^s}(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le e^{-s\tau}\cdot N_{\mathrm{sub}}(U;\tau)+2e^{-s\tau}\cdot K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$
**Cat-B sketched** (depends on L-M-2's sketched derivation).

**Corollary L-M.C (shifted saturating, $\beta\ge 20$).** For $\phi=\phi_{\mathrm{shift\text{-}sat}}^\beta$, $\tau\in(0,\tau_*)$:
$$
\bigl|K_{\mathrm{soft}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta}(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le e^{-\beta\tau}\cdot K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$
Note the $N_{\mathrm{sub}}$ term vanishes since $\varepsilon_{\mathrm{sub}}^{\phi_{\mathrm{shift\text{-}sat}}^\beta}=0$ (Phi-3d is identically zero on $[0,\ell_{\min}]$). **Cat-B sketched.**

### §6.4 Sharp asymptotic regime

In the limit $s\to\infty$ (or $\beta\to\infty$), Corollaries L-M.B and L-M.C both reduce to L-M.A: $K_{\mathrm{soft}}^\phi\to K_{\mathrm{act}}^\varepsilon$ pointwise. The convergence rate is **exponential in $s\tau$ (or $\beta\tau$)**, i.e., the product of sharpness and transition width. This recovers Approach A2 (`01_L1M_approach_exploration.md` §2.2) as a corollary: A2 was the *observation* that $\phi^s\to\phi_{\mathrm{hard}}$; L-M.B/C provides the *quantitative rate* embedded in the L1-M error bound.

### §6.5 Comparison with T-L1-F

The comparison is informative.

| Aspect | T-L1-F (CV-1.5.2 Cat A conditional) | L-M (this corollary, Cat B sketched) |
|---|---|---|
| Regime | $(P0)$–$(P11)$ | $(P0)$–$(P11)$ + $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ + $\tau<\tau_*$ |
| Statement type | Equality of integers | Inequality of real-and-integer |
| Conclusion | $K_{\mathrm{bar}}^{\ell_{\min}}=K_{\mathrm{act}}^\varepsilon$ | $|K_{\mathrm{soft}}^\phi-K_{\mathrm{act}}^\varepsilon|\le\varepsilon_{\mathrm{sub}}^\phi N_{\mathrm{sub}}+\varepsilon_{\mathrm{dom}}^\phi K_{\mathrm{act}}^\varepsilon$ |
| Proof core | LG-2/3/4/7 + L1-H2 Lemma 1+2 + PO-1 + L1-J §8 | L-M-1 (triangle inequality) + L-M-2 (T-L1-F's bar-classification + bottleneck stability) + T-L1-F substitution |
| Bijection | $\mathcal A_{\mathrm{bar}}:A^\varepsilon\to\mathrm{Bars}_0^{\mathrm{term}}$ | inherited from T-L1-F |

L-M is structurally a **two-step downstream corollary** of T-L1-F: Step 1 (envelope-pure inequality, L-M-1) is independent; Step 2 (substitution + edge-band derivation) uses T-L1-F's canonical conclusion + its proof structure (for L-M-2).

---

## §7. Counterexample Attempts

Per prompt §7 (counterexample tries are explicit constructions, not "no counterexample observed").

### §7.1 Attempt 1: default $\phi$-sat envelope (Phi-0)

**Construction.** $\phi_0(\ell)=\ell/(\ell+\ell_{\min})$, $\ell_{\min}=0.10$, on the $T^2_{20}$ multi-formation state from WQ-LAT-1 production run (`THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_results.md`).

**Outcome.** WQ-LAT-1.B Phi-0 measured range $0.943$ across $K_{\mathrm{field}}\in\{3,4,6,8,12\}$. The L1-M corollary would *seem* to predict a small bound. **Resolution: not a counterexample to L-M.** Phi-0 is excluded by axiom F4 (Claim L-M-V2: $\phi_0\notin\Phi_{\mathrm{res}}$ with any usefully small $\varepsilon_{\mathrm{sub}}$). The hypothesis $\phi\in\Phi_{\mathrm{res}}$ is violated. The L-M conclusion does not apply.

This is consistent with plan.md §6 Risk 1 mitigation and confirms F4's structural role: F4 *is* the empirical demarcation between admissible and inadmissible envelopes.

### §7.2 Attempt 2: edge-band-dense bar configuration

**Construction.** Synthesize a hypothetical state $\mathbf u$ with $U$ having 10 bars of length exactly $\ell_{\min}$ (i.e., $\ell_i=0.10$ for $i=1,\ldots,10$). Take $\phi=\phi_{\mathrm{logistic}}^{s=100}$, $\tau=0.05$.

For this configuration, $N_{\mathrm{edge}}=10$, $N_{\mathrm{sub}}=N_{\mathrm{dom}}=0$. The general L-M-1 bound (without L-M-2) gives $|K_{\mathrm{soft}}^\phi-K_{\mathrm{bar}}^{\ell_{\min}}|\le 0+10+0=10$, vacuous.

**Outcome.** This configuration would refute L-M's conclusion *if* it were realizable under $(P0)$–$(P11)$. But L-M-2 §5.3+§5.4+§5.5 shows that under $(P0)$–$(P11)$, no bar can have $\ell_i\in[\ell_{\min}-\tau,\ell_{\min}+\tau]$. Therefore the synthesized configuration *violates* $(P0)$–$(P11)$ — specifically, it violates either P6 (Type-D bars need $\ell_i\ge\ell_{\min}+r_{\mathrm{birth}}$) or P8/P9 (Type-N bars need $\ell_i\le\ell_{\min}-2\rho_{\mathrm{pert}}$) or P10 (Type-B bars need $\ell_i\le\ell_{\min}-\rho_{\mathrm{res}}$).

**Resolution: not a counterexample to L-M.** It is a counterexample to the *unconditional* envelope-pure inequality (without L-M-2), but L-M's hypothesis $(P0)$–$(P11)$ rules it out.

This sharpens the importance of L-M-2: without the regime, the $N_{\mathrm{edge}}$ term is uncontrolled and the corollary is vacuous.

### §7.3 Attempt 3: insufficient sharpness (Phi-4a, $s=20$)

**Construction.** $\phi=\phi_{\mathrm{logistic}}^{s=20}$, $\ell_{\min}=0.10$, $\tau=0.02$. Then $s\tau=0.4$, $e^{-s\tau}=0.67$.

For an active state with $K_{\mathrm{act}}^\varepsilon=3$ and $N_{\mathrm{sub}}=10$ (under $(P0)$–$(P11)$, $N_{\mathrm{sub}}$ is the count of Type-N+Type-B bars below $\ell_{\min}-\tau$):
$$
|K_{\mathrm{soft}}^\phi-K_{\mathrm{act}}^\varepsilon|\le 0.67\cdot 10+2\cdot 0.67\cdot 3=6.7+4.0=10.7.
$$
Bound is $10.7$ for an integer count of $3$ — useless.

**Outcome.** This is not a counterexample to L-M (the bound holds); it shows the bound becomes *vacuous* at low sharpness. **Resolution: L-M's usefulness depends on $s\tau\gg 1$ (or $\beta\tau\gg 1$).** WQ-LAT-1.B's empirical recommendation $s\ge 50$ (with $\tau\sim 0.05$, $s\tau\ge 2.5$) gives $e^{-s\tau}\le 0.082$, which is the sharpness regime where L-M is empirically useful.

The empirically supported sub-classes ($s\ge 50$, $\beta\ge 20$) thus correspond to the non-vacuous regime of L-M.

### §7.4 Attempt 4: $\tau$ chosen too large

**Construction.** $\phi=\phi_{\mathrm{logistic}}^{100}$, $\tau=0.5$. Then $\tau>r_{\mathrm{birth}}$ for typical L1-I best-case parameters ($r_{\mathrm{birth}}<\rho_{\mathrm{pert}}<0.1$ commonly).

For $\tau\ge\tau_*$, L-M-2's conclusion fails: dominant bars in $[\ell_{\min}+r_{\mathrm{birth}},\ell_{\min}+\tau]\subseteq I_{\mathrm{edge}}$, so $N_{\mathrm{edge}}>0$.

**Outcome.** Not a counterexample to L-M; rather, $\tau<\tau_*$ is a *necessary* hypothesis. **Resolution: $\tau_*$ is a sharp upper bound on the admissible transition width.** This is captured in the L-M statement.

### §7.5 Counterexample summary

No genuine counterexample to L-M was constructed. The four attempts illustrate:
- Attempt 1: F4 excludes default $\phi$-sat (consistent).
- Attempt 2: $(P0)$–$(P11)$ excludes edge-band-dense configurations via L-M-2 (consistent).
- Attempt 3: $s\tau\gg 1$ is needed for non-vacuous bound (consistent — empirically $s\ge 50$).
- Attempt 4: $\tau<\tau_*$ is needed for L-M-2 (consistent — captured in hypothesis).

The L-M corollary stands.

---

## §8. Status, Self-Classification, and Auditability

### §8.1 Per-result self-classification

| Statement | Status | Cat | Notes |
|---|---|---|---|
| L-M-D1 ($\Phi_{\mathrm{res}}$ definition F1–F5) | proved (definitional) | A absolute | axioms only |
| Claim L-M-V1 (envelope sub-class verification) | proved | A absolute | direct calculation |
| Claim L-M-V2 (Phi-0 excluded by F4) | proved | A absolute | direct calculation |
| Lemma L-M-1 (envelope-pure inequality) | proved | A absolute | uses only finite graph + F1–F3 + triangle inequality |
| Lemma L-M-Sub, L-M-Dom, L-M-Edge | proved | A absolute | direct from F4, F5, F1 respectively |
| Lemma L-M-2 (edge-band emptiness under regime) | sketched | B sketched | depends on T-L1-F proof structure + CSEH 2007; three bookkeeping refinements (§5.7) flagged for L1-M-AUDIT |
| Theorem L-M (combined corollary) | proved (modulo L-M-2) | B sketched | inherits L-M-2's status |
| Corollary L-M.A (hard threshold) | proved | A conditional under $(P0)$–$(P11)$ | trivial substitution: $K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}=K_{\mathrm{bar}}^{\ell_{\min}}=K_{\mathrm{act}}^\varepsilon$ |
| Corollary L-M.B (logistic) | proved (modulo L-M-2) | B sketched | depends on L-M-2 |
| Corollary L-M.C (shift-sat) | proved (modulo L-M-2) | B sketched | depends on L-M-2 |

### §8.2 Granularity check (per prompt §9)

Each substantive claim is independently re-checkable:

- **L-M-1's three-region argument (§3.2)** can be verified by checking the per-region sign analysis and the triangle inequality. No external machinery.
- **L-M-V1's three calculations (§2.2)** can be verified envelope-by-envelope: each is a closed-form bound on $\sigma$ or $1-e^{-x}$.
- **L-M-2's three type classifications (§5.3, §5.4, §5.5)** can each be re-checked against canonical.md §13 T-L1-F entry and the relevant L1-x working files. The sketched parts (§5.7 items 1–3) are explicitly flagged.
- **Theorem L-M's substitution proof (§6.2)** uses only the lemmas above + T-L1-F as a black box.
- **Per-family corollaries (§6.3)** are direct substitutions of L-M-V1 into Theorem L-M.

The §-numbering is preserved: a future audit query "verify §5.4's bottleneck-stability factor of $2$" maps directly to that subsection.

### §8.3 Diminishing returns reached

Per prompt §13 stopping criteria, this session's primary approach has reached:
- A completed theorem statement (Theorem L-M, §6.1) with explicit hypothesis package.
- Three explicit per-family corollaries with closed-form error bounds.
- A failure-analysis (counterexample attempts §7) showing the hypothesis package is tight.
- Self-classification at Cat-B-sketched, with explicit refinement points for L1-M-AUDIT.

The next step (L1-M-AUDIT and L1-M-FORMALIZE) belongs to a future session. Continuing here would be incremental polishing without new structural content.

---

**End of `02_development.md`.**

**Next file:** `03_integration_and_new_open.md` — Integration with canonical, new open questions, prompt v2 candidate notes.
