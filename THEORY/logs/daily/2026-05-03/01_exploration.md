# 01_exploration.md — L1-M Soft-Count Corollary, Approach Generation

**Session:** 2026-05-03 (W5 Day 7, post-T-L1-F canonical promotion)
**Target (from plan.md §2):** Develop **L1-M — Soft-Count Corollary under $\Phi_{\mathrm{res}}$**: under T-L1-F's $(P0)$–$(P11)$ and $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$, prove
$$
\bigl|K_{\mathrm{soft}}^\phi(U(\mathbf u))-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
$$
**This file covers:** §4.1 Restatement, §4.2 Multi-approach (4 candidates), §4.3 Primary-approach selection.
**Depends on reading:** `canonical.md` §13 Cat A T-L1-F; `theorem_status.md` CV-1.5.2; `working/MF/ksoft_kact_bridge_lemma.md` §5.3 + §13; `working/MF/wq_lat1b_phi_envelope_refinement_results.md` §5.1, §6, §8.3; `working/E/soft_K_definition.md` §1, §2.1; `working/MF/ksoft_kact_bridge_proof_status.md` C-09/C-10/C-11; `logs/daily/2026-05-02/01_T_L1_F_canonical_promotion_closure.md` §2.

---

## §1. Target Restatement

### §1.1 The plan-as-given

plan.md §2 specifies the target as:
$$
K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi)
$$
under $(P0)$–$(P11)$ and $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$, written rigorously as the absolute-value inequality
$$
\bigl|K_{\mathrm{soft}}^\phi(U(\mathbf u))-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi. \tag{L1-M}
$$
plan.md §4.3 marks this as a **THEOREM_CANDIDATE_DRAFT** under $(P0)$–$(P11) + \Phi_{\mathrm{res}} + \text{(E)}$, with Cat-A pending audit.

### §1.2 Reformulation in my own language

Three layers must be distinguished cleanly.

1. **The hard count anchor.** Under T-L1-F (CV-1.5.2 Cat-A conditional), the *integer* $K_{\mathrm{bar}}^{\ell_{\min}}(U;G)$ — number of $H_0$ terminal-death bars of length $\ge\ell_{\min}$ in the superlevel persistence diagram of the aggregate $U$ — coincides with $K_{\mathrm{act}}^\varepsilon(\mathbf u)$, the integer count of slots with mass $>\varepsilon$.

2. **The soft observable.** $K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i(U))$ is a *real-valued* sum over all positive-length bars, weighted by an envelope $\phi:[0,1]\to[0,\infty)$. It is a different kind of object: $\mathbb R_{\ge 0}$-valued, smooth (when $\phi$ is), envelope-dependent, and sensitive to the entire bar-length distribution including sub-resolution noise.

3. **The bridge.** The L1-M question is: *for which envelopes $\phi$ does $K_{\mathrm{soft}}^\phi(U)$ track $K_{\mathrm{bar}}^{\ell_{\min}}(U)$ — and consequently $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ — up to a controllable error?* WQ-LAT-1.B already answered the empirical version: hard threshold, sharp logistic ($s\ge 50$), shifted-saturating ($\beta\ge 20$) are stable; default $\phi$-sat is not. L1-M asks for the *theoretical* version: a class $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ of envelopes for which $|K_{\mathrm{soft}}^\phi - K_{\mathrm{bar}}^{\ell_{\min}}|$ admits an explicit bound from the bar-length distribution + the envelope's structural parameters.

### §1.3 What is data, what is question, what is success, what is failure

- **Data:** the multi-formation state $\mathbf u\in\widetilde\Sigma_M^{K_{\mathrm{field}}}(G)$, the aggregate $U=\sum_j u^{(j)}$, its $H_0$ superlevel persistence diagram $\mathrm{Dgm}_0^{\sup}(U;G)$ with bar-length list $\{\ell_i(U)\}_i$, the regime parameters $(P0)$–$(P11)$, and an envelope $\phi$ from a class $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$.
- **Question:** find the smallest absolute-value bound on $|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)|$ in terms of (i) the bar-length distribution of $U$, (ii) the envelope's structural parameters $(\ell_{\min},\tau,s/\beta)$, and (iii) the regime constants from $(P0)$–$(P11)$.
- **Success:** an inequality of the form (L1-M) with each of $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ explicitly defined, computable from $\{\ell_i(U)\}_i$ and $\phi$, and bounded above by quantities derivable from envelope sub-class + regime constants.
- **Failure:** any of (a) the inequality requires a hypothesis that is not a consequence of $(P0)$–$(P11) + \Phi_{\mathrm{res}}$, (b) the envelope class $\Phi_{\mathrm{res}}$ admits a member for which one of $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ is unbounded, (c) the inequality is vacuous (right-hand side $\ge|A|$ trivially).

### §1.4 Surfacing implicit assumptions

plan.md §4.5 and §4.3 quietly carry three assumptions that L1-M must make explicit.

- **(A-impl-1) The bar-set is finite.** $G$ is a finite graph (T-L1-F P0 stipulates this). Hence $\#\{i:\ell_i(U)>0\}\le|X|$. This makes all three $\rho$-terms finite sums.
- **(A-impl-2) Every active slot's dominant bar has length $\ge\ell_{\min}$.** This is a *consequence* of T-L1-F + P6 (birth height $b_j\ge h_{\min}\ge\ell_{\min}$) + P0 (terminal-death). Each dominant bar $\mathcal A_{\mathrm{bar}}(j)$ has length $b_j-d_j$ where $d_j=0$ (terminal-death convention) and $b_j\ge\ell_{\min}$, hence $\ell_{\mathcal A_{\mathrm{bar}}(j)}\ge\ell_{\min}$. So in fact dominant bars sit in $[\ell_{\min},1]$. This rules out the degenerate case where every bar is exactly at threshold.
- **(A-impl-3) "Edge-band control (E)" is an extra hypothesis on top of $(P0)$–$(P11) + \Phi_{\mathrm{res}}$.** plan.md §4.3 lists (E) as separate. But P8 (tightened H6: $\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}$) and P9 ($\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2$) jointly constrain *non-dominant* bars to lie below $\ell_{\min}-3\rho_{\mathrm{pert}}+O(\rho_{\mathrm{pert}})=\ell_{\min}-2\rho_{\mathrm{pert}}$, leaving a per-slot built-in margin of $\sim 2\rho_{\mathrm{pert}}$ between the highest non-dominant bar and $\ell_{\min}$. This suggests (E) might be derivable rather than postulated — if so, the L1-M hypothesis package collapses to $(P0)$–$(P11) + \Phi_{\mathrm{res}}$. *(This is a substantive observation flagged for §4.4.4 below.)*

### §1.5 What L1-M is *not*

- Not a proof that $K_{\mathrm{soft}}^\phi$ is a global identification with $K_{\mathrm{act}}$; only a controlled approximation under explicit conditions (per plan.md §4.6 non-claim).
- Not a resolution of OP-0005 (K-Selection); L1-M counts what is there, not which K is selected.
- Not a resolution of OP-0008 ($\sigma^A$ K-jump non-determinism); L1-M operates strictly inside the resolved regime where T-L1-F holds, while OP-0008 is overlap-regime territory.
- Not a derivation of $\Phi_{\mathrm{res}}$ from primitive SCC dynamics; $\Phi_{\mathrm{res}}$ is a working envelope class designed to make the inequality hold, not a class natively privileged by SCC.

---

## §2. Multi-Approach Generation

I generate four candidate approaches. Each is mathematically independent — distinct tools, distinct success modes, distinct failure modes.

### §2.1 Approach A1 — Bar-by-bar absolute deviation + three-region partition (plan-aligned)

**Core idea.** Apply $|\sum_i x_i|\le\sum_i|x_i|$ to the per-bar deviation $\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}$, partition the bar set $\{\ell_i\}_i$ into three regions $\{\ell_i<\ell_{\min}-\tau\}$, $\{|\ell_i-\ell_{\min}|\le\tau\}$, $\{\ell_i\ge\ell_{\min}+\tau\}$, and identify each region's contribution with $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ respectively. Then combine with T-L1-F's $K_{\mathrm{bar}}^{\ell_{\min}}=K_{\mathrm{act}}^\varepsilon$ identity.

**Form of the result.** A theorem-candidate of the form (L1-M), with each $\rho$-term defined as an explicit sum over its region, and envelope-sub-class bounds (Phi-1: $\rho_{\mathrm{sub}}=\rho_\phi=0$; Phi-4c $s=100$: $\rho_{\mathrm{sub}},\rho_\phi\le e^{-s\tau}$ tail; Phi-3d $\beta=20$: $\rho_{\mathrm{sub}}=0$, $\rho_\phi\le e^{-\beta\tau}$).

**Tools.** Triangle inequality + direct bar-set partition + T-L1-F substitution. No external persistence-stability theorem required (the inequality is purely envelope-arithmetic).

**Success when.** $\phi$ is in $\Phi_{\mathrm{res}}$ and the bar-length distribution of $U$ has either no mass in the edge band $[\ell_{\min}-\tau,\ell_{\min}+\tau]$ or sharpness parameter sufficiently large to suppress edge-band contribution.

**Failure mode.** If the bar-length distribution of $U$ has many bars in the edge band $[\ell_{\min}-\tau,\ell_{\min}+\tau]$ and $\phi$ has finite sharpness, $\rho_{\mathrm{edge}}^\phi$ can be of order $|\{\text{edge-band bars}\}|$ — potentially large enough to break the bound. Hypothesis (E) is needed to rule this out; without (E) the result is vacuous.

**Interaction with canonical.** Substitution into T-L1-F is one line. No reverse interaction (does not weaken T-L1-F or any other canonical theorem). Adds new envelope-class $\Phi_{\mathrm{res}}$ to canonical vocabulary if promoted.

### §2.2 Approach A2 — Sharpness-driven asymptotic via mollified hard threshold

**Core idea.** Treat $\phi_{\mathrm{logistic}}^s$ and $\phi_{\mathrm{shift\text{-}sat}}^\beta$ as one-parameter families that converge pointwise (and in $L^\infty([0,1]\setminus[\ell_{\min}-\tau,\ell_{\min}+\tau])$) to $\phi_{\mathrm{hard}}$ as $s\to\infty$ or $\beta\to\infty$. Quantify the convergence rate (exponential in $s\tau$, $\beta\tau$). Then for any $\varepsilon_*>0$, choose sharpness so that $\|\phi-\phi_{\mathrm{hard}}\|_{L^\infty([0,1]\setminus[\ell_{\min}-\tau,\ell_{\min}+\tau])}<\varepsilon_*$. The corollary becomes a parametric statement: "given target tolerance $\varepsilon_*$, there exists sharpness $s^*$ such that for all $\phi\in\Phi_{\mathrm{res}}$ with sharpness $\ge s^*$, $|K_{\mathrm{soft}}^\phi-K_{\mathrm{act}}^\varepsilon|\le N(U)\varepsilon_*+\rho_{\mathrm{edge}}^\phi$" where $N(U)=\#\{\text{positive bars}\}$.

**Form of the result.** A parameter-controllable approximation theorem; the sharpness parameter is the main control. Envelope sub-classes at finite sharpness become *quantitative approximations* to $\phi_{\mathrm{hard}}$, with explicit error rates.

**Tools.** $L^\infty$ approximation + counting bars + (the same T-L1-F substitution at the end).

**Success when.** Sharpness can be increased freely. Useful for *designing* an envelope to achieve a target accuracy, given $U$'s bar distribution.

**Failure mode.** If the SCC application (e.g., variational use as a differentiable surrogate) imposes a fixed sharpness — e.g., gradient-based optimization needs bounded $\phi'$, so $s$ cannot be too large — the asymptotic statement gives no usable bound. Also, A2 is silent on the edge band: $\rho_{\mathrm{edge}}^\phi$ is not controlled by sharpness alone (a logistic of slope $s$ still spans $\sim 4/s$ in transition width, so bars in $[\ell_{\min}-2/s,\ell_{\min}+2/s]$ contribute $\sim$ const each; if there are many such bars, contribution adds linearly).

**Interaction with canonical.** No interaction with existing theorems. Could *replace* $\Phi_{\mathrm{res}}$ definition with a sharpness-parameterized family: "$\Phi_{\mathrm{res}}^s := \{\phi:\|\phi-\phi_{\mathrm{hard}}\|_{L^\infty\text{ off edge band}}\le 1/s\}$", which is cleaner axiomatically.

### §2.3 Approach A3 — Functional-analytic supremum-bound on the bar-length distribution support

**Core idea.** Treat the bar-length list $\{\ell_i(U)\}_i$ as a finite empirical measure $\nu_U=\sum_i\delta_{\ell_i(U)}$ on $[0,1]$. Then $K_{\mathrm{soft}}^\phi(U)=\int\phi\,d\nu_U$ and $K_{\mathrm{bar}}^{\ell_{\min}}(U)=\int\mathbf 1_{[\ell_{\min},1]}\,d\nu_U$. Their difference is $\int(\phi-\mathbf 1_{[\ell_{\min},1]})\,d\nu_U$, which is bounded by $\|\phi-\mathbf 1_{[\ell_{\min},1]}\|_{L^\infty(\mathrm{supp}\,\nu_U)}\cdot|\nu_U|$ where $|\nu_U|=\#\{\text{positive bars}\}$. The bound depends on (a) how $\phi$ deviates from $\phi_{\mathrm{hard}}$ on the support of $\nu_U$, and (b) the cardinality of the bar set.

**Form of the result.** $|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)|\le\|\phi-\phi_{\mathrm{hard}}\|_{L^\infty(\mathrm{supp}\,\nu_U)}\cdot N_+(U)$ where $N_+(U)=|\nu_U|$. Combined with T-L1-F: $|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)|\le N_+(U)\cdot\|\phi-\phi_{\mathrm{hard}}\|_{L^\infty(\mathrm{supp}\,\nu_U)}$.

**Tools.** Hölder's inequality / $\int f\,d\nu\le\|f\|_\infty|\nu|$ + bottleneck stability of $\mathrm{Dgm}_0^{\sup}$ (CSEH 2007) for any future perturbation analysis.

**Success when.** $\phi$ is close to $\phi_{\mathrm{hard}}$ in $L^\infty$ on the support of the bar-length distribution. This is essentially a *uniform-deviation* statement, which is too crude when the bar distribution clusters near $\ell_{\min}$ (the deviation $|\phi-\phi_{\mathrm{hard}}|$ is largest exactly there).

**Failure mode.** A3 systematically over-estimates: it does not distinguish between bars far from $\ell_{\min}$ (where $|\phi-\phi_{\mathrm{hard}}|$ is small) and bars near $\ell_{\min}$ (where the deviation is order 1 for finite-sharpness envelopes). Hence $\|\phi-\phi_{\mathrm{hard}}\|_{L^\infty(\mathrm{supp}\,\nu_U)}$ can be order 1 even when most bars are well separated. This makes A3 the *coarsest* bound; A1's region-by-region refinement is strictly tighter.

**Interaction with canonical.** Connects naturally to QM3 (Q_morph continuity via persistence stability, Cat A) since CSEH bottleneck stability is the same anchor. A3 could be promoted as a baseline lemma; A1 then refines it.

### §2.4 Approach A4 — Edge-band control as a *consequence* of the L1-J regime

**Core idea.** Don't treat (E) as a separate hypothesis. Show instead that under $(P0)$–$(P11)$, the bar-length distribution of $U$ has a *built-in margin* around $\ell_{\min}$: dominant bars (one per active slot) lie in $[\ell_{\min},1]$ with $b_j\ge h_{\min}\ge\ell_{\min}$ (P6); non-dominant bars on $G_j^r$ lie below $\ell_{\min}-3\rho_{\mathrm{pert}}+O(\rho_{\mathrm{pert}})$ via P8 + P9. Background bars (off all $N_j^r$) are bounded by $\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}$ (P10) + LG-7 coverage (derived from P5 + P0). Hence the edge band $[\ell_{\min}-\tau,\ell_{\min}+\tau]$ for any $\tau<\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{res}})$ contains *no* bars except dominant ones (which are in $[\ell_{\min},1]$, so they may sit at the lower edge if $b_j=\ell_{\min}$ exactly, but generically $b_j>\ell_{\min}+\rho_{\mathrm{birth}}$ via P11's margin ledger).

**Form of the result.** A *strengthened* L1-M: the hypothesis (E) becomes a *theorem* under $(P0)$–$(P11)$, and L1-M's hypothesis package collapses to $(P0)$–$(P11) + \Phi_{\mathrm{res}}$ alone. The corollary becomes:
$$
|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon|\le\rho_{\mathrm{sub}}+\rho_\phi
$$
with $\rho_{\mathrm{edge}}^\phi$ identically zero (no bars in the edge band) provided $\tau<\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{res}},\rho_{\mathrm{birth}})$.

**Tools.** P8 (tightened H6) + P9 (NE-2 perturbation control) + P10 (inactive residual suppression) + P11 (margin ledger) — all already in the L1-J regime. Plus a careful tracking of what kinds of bars can have what kinds of lengths under the L1-J neighborhood architecture.

**Success when.** $(P0)$–$(P11)$ hold (which is the setting we already restrict to) AND $\tau$ is chosen small enough relative to the regime margins. Since $\tau$ is a *parameter of the envelope class*, we can simply require $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ with $\tau\le\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{res}},\rho_{\mathrm{birth}})/2$.

**Failure mode.** If the regime constants $(\rho_{\mathrm{pert}},\rho_{\mathrm{res}},\rho_{\mathrm{birth}})$ are very small, the admissible $\tau$ shrinks, restricting the envelope class to *very sharp* logistics or hard threshold. Acceptable in principle; reduces to A1 for hard threshold.

**Interaction with canonical.** Substantive — replaces an ad-hoc hypothesis (E) with a derivation from canonical regime constants. Strengthens L1-M's standalone status: the corollary needs no extra hypothesis beyond what T-L1-F itself uses, plus the envelope class.

### §2.5 Independence verification (per prompt §5)

The four approaches are mathematically independent:

| Pair | Independent in tool? | Independent in failure mode? | Independent in success regime? |
|---|---|---|---|
| A1 vs A2 | Yes (triangle ineq vs $L^\infty$ approximation) | Yes (A1 fails on dense edge band; A2 fails at fixed sharpness) | Yes (A1 envelope-fixed, A2 sharpness-tunable) |
| A1 vs A3 | Yes (per-region partition vs uniform-norm) | Yes (A1 sensitive to edge band; A3 sensitive to global bar count) | Partially overlap (both work for hard threshold) |
| A1 vs A4 | Yes (envelope arithmetic vs regime-constant tracking) | Distinct (A1 fails when (E) breaks; A4 fails when regime margins shrink) | Yes (A4 derives (E), A1 assumes (E)) |
| A2 vs A3 | Yes (parametric family vs uniform bound) | Distinct (A2 needs sharpness slack; A3 needs uniformly-small deviation) | Different (A2 is asymptotic, A3 is non-asymptotic) |
| A2 vs A4 | Yes (envelope-side vs regime-side analysis) | Distinct | Yes (A2 about envelope tuning; A4 about regime constants) |
| A3 vs A4 | Yes (functional-analytic vs combinatorial-regime) | Distinct | Largely orthogonal |

All six pairwise comparisons exhibit distinct tool, failure, and success structure. The four approaches form a genuinely independent set.

---

## §3. Primary Approach Selection

### §3.1 Selection: **A1 with A4 enhancement**

**Primary:** **A1 (bar-by-bar absolute deviation + three-region partition)**, applied with the **A4 strengthening** (derivation of edge-band control from $(P0)$–$(P11)$ rather than postulation as separate hypothesis).

This combination yields the tightest publishable corollary:
- A1 gives the explicit $\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi$ decomposition that plan.md §4.5 prescribes and that aligns with the C-09/C-10/C-11 lemma chain in `working/MF/ksoft_kact_bridge_proof_status.md`.
- A4 *eliminates* the need for an extra hypothesis (E) by showing edge-band emptiness is built into the L1-J regime, modulo the choice of $\tau$. The L1-M hypothesis package thus reduces to $(P0)$–$(P11) + \Phi_{\mathrm{res}}(\ell_{\min},\tau)$ with an admissibility condition $\tau\le\tau_*$ derivable from regime constants.

### §3.2 Why A1 is primary (ranked rationale)

1. **Plan alignment.** plan.md §4.2 prescribes precisely the three-region error decomposition. Selecting A1 keeps the session output directly aligned with the user's pre-arranged work-package structure; downstream documents (`ksoft_kact_bridge_L1M_soft_count_corollary.md`, mirroring L1-J/L1-L style) will integrate without restructuring.
2. **Lowest external dependency.** A1 needs only triangle inequality + the T-L1-F substitution. A2 needs parametric convergence rates that introduce additional sharpness-vs-$\tau$ trade-off bookkeeping. A3 needs CSEH bottleneck stability for any non-trivial extension (and even then is the coarsest bound).
3. **Direct envelope-sub-class verification.** Each entry in plan.md §4.5's L1-M.5 status table — Phi-1 (EXACT), Phi-4c (theorem candidate with edge-band control), Phi-3d (theorem candidate with edge-band control), arbitrary $\phi$ (FORBIDDEN) — corresponds directly to a per-region calculation in A1. Filling the table is a mechanical exercise after A1 is written.
4. **Compatibility with WQ-LAT-1.B empirics.** WQ-LAT-1.B's tabulated ranges (range = 0.000 for Phi-1, 0.001 for Phi-4c, 0.005 for Phi-3d, 0.943 for Phi-0 default) are exactly the per-envelope $\rho$-bounds that A1 produces. A1 explains the empirical pattern; A2 and A3 do not (A2 is parametric and predicts asymptotic behavior; A3 is over-loose).
5. **Cleanest auditability.** A theorem-candidate stated as "for each $\phi$-sub-class, the $\rho$-bound has the following closed form" is most easily checked by independent audit (the L1-M-AUDIT next-step in plan.md §8). Per-bar arithmetic requires no analyst-specific intuition; A2/A3 require functional-analytic background that the L1-K external auditor may not have.

### §3.3 Why A4 strengthens A1 (rather than replacing it)

A4 derives the edge-band hypothesis (E) from regime constants. This does not change the *form* of the corollary — the inequality $|K_{\mathrm{soft}}^\phi-K_{\mathrm{act}}^\varepsilon|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi$ remains. A4's role is to show that $\rho_{\mathrm{edge}}^\phi=0$ under $(P0)$–$(P11) + \tau\le\tau_*$, which simplifies the bound to $\rho_{\mathrm{sub}}+\rho_\phi$ in the resolved regime.

Key insight: $\rho_{\mathrm{edge}}^\phi$ is the *most fragile* of the three error terms in A1. By eliminating it via A4, the corollary becomes structurally sound *for any* $\phi\in\Phi_{\mathrm{res}}$, without the need for case-by-case (E) verification. This is a non-trivial improvement over plan.md's stated form, and it should be developed in §02.

### §3.4 Why A2 and A3 are preserved as alternatives

**A2 is preserved** because it provides the *quantitative rate* at which $\phi_{\mathrm{logistic}}^s$ and $\phi_{\mathrm{shift\text{-}sat}}^\beta$ approximate $\phi_{\mathrm{hard}}$. This rate ($e^{-s\tau}$, $e^{-\beta\tau}$) is *embedded* in A1's per-region $\rho_{\mathrm{sub}},\rho_\phi$ bounds. If A1 fails (e.g., a future SCC application uses an envelope at finite sharpness with bars dense in the edge band), A2 provides the natural fallback: tune sharpness to drive $\rho$ below threshold. A2 is the envelope-design tool.

**A3 is preserved** because it provides the *baseline* uniform-norm bound, useful as a sanity check and as a connection to QM3's CSEH 2007 anchor. A3 by itself is too coarse for L1-M, but the moment we extend L1-M to a perturbation analysis (e.g., $|K_{\mathrm{soft}}^\phi(U_1)-K_{\mathrm{soft}}^\phi(U_2)|$ for nearby states), A3's CSEH machinery becomes the load-bearing tool. A3 is the perturbation tool.

A2 and A3 will reappear in §03 as future-work threads.

### §3.5 Excluded approaches (for record)

I considered and excluded:

- **A5: Wasserstein-1 between persistence-weighted measures.** Initially attractive — lift bar lists to measures on $[0,1]$ and bound $W_1$. But this collapses: comparing $\nu_U^\phi=\sum_i\phi(\ell_i)\delta_{\ell_i}$ vs $\nu_U^{\mathrm{hard}}=\sum_i\mathbf 1_{\ell_i\ge\ell_{\min}}\delta_{\ell_i}$ has $W_1=0$ (same support, just different masses), so the comparison reduces to $|\sum_i\phi(\ell_i)-\sum_i\mathbf 1_{\ell_i\ge\ell_{\min}}|$, which is exactly A1's starting point. No new content.
- **A6: Functional-derivative analysis at the envelope level.** Treat $\phi\mapsto K_{\mathrm{soft}}^\phi$ as a linear functional on $C([0,1])$ and compute its Fréchet derivative $\delta K_{\mathrm{soft}}^\phi/\delta\phi=\nu_U$. Then $|K_{\mathrm{soft}}^\phi-K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}|\le\sup_t|\phi(t)-\phi_{\mathrm{hard}}(t)|\cdot|\nu_U|$. This is a re-derivation of A3.
- **A7: SCC-intrinsic argument via dual-mode self-referentiality.** Try to use closure $Cl_t$ + distinction $D_t$ structure to derive a relationship between bar lengths and slot identification. This conflates two layers — the bridge is at the *aggregate* level (single field $U$), where dual-mode structure does not directly act. SCC-intrinsic arguments belong to the per-slot $u^{(j)}$ level, which is already absorbed into T-L1-F via $K_{\mathrm{act}}$.

---

## §4. Output Plan for §02

`02_development.md` will contain (numbering deliberately aligned with §§ for cross-reference):

- **§1.** Notation summary (objects, regime constants, envelope class $\Phi_{\mathrm{res}}$).
- **§2.** Envelope class $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ — formal definition (axioms F1–F5) + verification of WQ-LAT-1.B empirical sub-classes.
- **§3.** Three-region bar partition + lemma L-M-1 (envelope-pure inequality $|K_{\mathrm{soft}}^\phi-K_{\mathrm{bar}}^{\ell_{\min}}|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi$).
- **§4.** Envelope sub-class bounds — Phi-1 (exact), Phi-4c (logistic, $\rho_{\mathrm{sub}}\le e^{-s\tau}$, $\rho_\phi\le e^{-s\tau}$), Phi-3d (shift-sat, $\rho_{\mathrm{sub}}=0$, $\rho_\phi\le e^{-\beta\tau}$).
- **§5.** Edge-band derivation lemma L-M-2 (A4 strengthening): under $(P0)$–$(P11)$, no bar of $U$ lies in $(\ell_{\min}-\tau_*,\ell_{\min})$ for $\tau_*$ derivable from $(\rho_{\mathrm{pert}},\rho_{\mathrm{res}},\rho_{\mathrm{birth}})$.
- **§6.** L1-M Theorem-Candidate: combining L-M-1 + L-M-2 + T-L1-F substitution.
- **§7.** Counterexample attempts: (a) finite-sharpness logistic with edge-band-dense bars (A1 fails without A4); (b) default $\phi$-sat envelope (forbidden by axiom F4 of $\Phi_{\mathrm{res}}$).
- **§8.** Status and Cat-classification self-judgment.

---

**End of `01_exploration.md`.**

**Next file:** `02_development.md` — primary-approach development.
