# pre_brainstorm.md — 2026-05-03 W5 Day 7 (post-T-L1-F canonical promotion, pre-L1-M soft-count corollary)

**Title:** 2026-05-03 Pre-Brainstorm — From Hard Count to Soft Count.
**Type:** Pre-session brainstorm. Sits next to `plan.md` as the looser conceptual frame for Day 7.
**Status:** Drafted 2026-05-02 EOD after T-L1-F was promoted to CV-1.5.2 Cat-A conditional and the day was closed at `01_T_L1_F_canonical_promotion_closure.md`. Read this before plan.md execution Day 7 morning.
**Use:** Mental frame for the day. Not the execution contract; that is plan.md. This file captures *why* Day 7 should feel like a transition from discrete to continuous count, and what conceptual hazards to avoid in that transition.

---

## §0. Day 7 Feeling in One Sentence

Day 6 promoted the **discrete count bridge** ($K_{\mathrm{bar}}=K_{\mathrm{act}}$) to canonical Cat-A conditional. Day 7 asks: **what does the soft, real-valued, envelope-dependent count $K_{\mathrm{soft}}^\phi$ measure once the hard count is settled?** The natural answer is "a controlled approximation under $\Phi_{\mathrm{res}}$" — but the substance is in *what controls fail* and *why*, not in declaring a single equality.

---

## §1. Core Question

> Now that $K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=K_{\mathrm{act}}^\varepsilon(\mathbf u)$ is canonically established (T-L1-F, CV-1.5.2) in the resolved regime $(P0)$–$(P11)$, what does the soft count $K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i(U))$ measure?

Sub-questions:

- Is it the same quantity as $K_{\mathrm{bar}}$ up to a small envelope-dependent error?
- Is it a *different* quantity that happens to agree with $K_{\mathrm{bar}}$ in a sharp-interface limit?
- Is it a *non-rigorous* relaxation that should be re-grounded against $K_{\mathrm{bar}}$?

The Day 7 conceptual project is to give a precise, conditional, controlled answer.

---

## §2. Conceptual Shift (Discrete → Continuous Count)

Three count quantities now sit at three layers (per `latent_index_space_design.md` §10):

- $K_{\mathrm{bar}}^{\ell_{\min}}(U;G)$ — **integer, threshold-gated, terminal-death $H_0$ count**. Crisp morphology count. CANONICAL via T-L1-F.
- $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ — **integer, label-counting, mass-thresholded count**. Chart-level diagnostic. CANONICAL via Commitment 16 + T-L1-F.
- $K_{\mathrm{soft}}^\phi(U)$ — **real-valued, weighted, envelope-dependent morphology score**. NOT yet canonical. WORKING-GRADE; pre-canonical sketch in `ksoft_kact_bridge_lemma.md` §5.3.

The task on Day 7 is **NOT to prove global equality $K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}$**. The task is to:

1. Acknowledge that $K_{\mathrm{soft}}^\phi$ is a different KIND of object (real-valued, not integer-valued).
2. Define a class $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ of "well-behaved" envelopes for which $K_{\mathrm{soft}}^\phi$ tracks $K_{\mathrm{bar}}^{\ell_{\min}}$ up to a controlled error.
3. Combine with T-L1-F to get a controlled-error bridge to $K_{\mathrm{act}}^\varepsilon$.

This is the **conceptual shift** that L1-M formalizes.

---

## §3. Main Insight from WQ-LAT-1.B

The `wq_lat1b_phi_envelope_refinement_results.md` outcome is the load-bearing empirical observation:

- **Default $\phi$-sat ($\phi(\ell)=\ell/(\ell+\ell_{\min})$) FAILED chart-invariance.** Range 0.943 across $K_{\mathrm{field}}\in\{3,4,6,8,12\}$ on LAT-C__A at $\ell_{\min}=0.10$. Mean drifted 0.916 → 1.859. The default smooth envelope assigned $\sim 0.09$ to bars of length $\sim 0.01$, and as $K_{\mathrm{field}}$ grew under split-bump refinement, sub-resolution bars accumulated from 4 to 18, summing to $\sim 1.6$ extra contribution.
- **Hard threshold $\phi_{\mathrm{hard}}=\mathbf 1_{\ell\ge\ell_{\min}}$ SUCCEEDED.** Range 0.000. Exactly equals $K_{\mathrm{bar}}^{\ell_{\min}}$ by definition.
- **Sharp logistic $\phi_s$ at $s=100$ SUCCEEDED.** Range 0.001. Smooth approximation of the hard threshold.
- **Shifted-saturating $\phi_\beta$ at $\beta=20$ SUCCEEDED.** Range 0.005. Differentiable everywhere; suppresses sub-threshold bars.

**Conclusion:** $\phi$ is not cosmetic. It is **structurally load-bearing**. The choice between $\phi$-sat and $\phi_{\mathrm{hard}}$ is not a matter of taste — it controls whether the soft count is chart-invariant.

The natural reading: $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ should be the class of $\phi$ that satisfy:

1. $\phi(0)=0$ (no zero-length bar contribution);
2. $\phi(\ell)\approx 0$ for $\ell<\ell_{\min}-\tau$ (sub-threshold suppression);
3. $\phi(\ell)\approx 1$ for $\ell\ge\ell_{\min}+\tau$ (dominant retention);
4. transition controlled by sharpness parameter ($s,\beta$, etc.) on the band $[\ell_{\min}-\tau,\ell_{\min}+\tau]$.

Default $\phi$-sat fails (1)–(3) simultaneously: it assigns positive mass everywhere, has no sharp transition, and accumulates sub-threshold contributions.

---

## §4. Possible Theorem Shape

The natural L1-M statement has TWO chained inequalities:

**Step 1 (envelope-pure):** for any state $\mathbf u$ and any $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$,

\[
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
\]

**Step 2 (combine with T-L1-F):** under $(P0)$–$(P11)$, $K_{\mathrm{bar}}^{\ell_{\min}}(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)$ canonically (CV-1.5.2). Substituting:

\[
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
\]

So L1-M is structurally a **two-step corollary**: (envelope-pure inequality) + (canonical T-L1-F substitution). The first step is the substantive content; the second step is mechanical.

A useful big-O form:

\[
K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi).
\]

---

## §5. Important Distinctions

Day 7 should keep these distinctions cleanly separated:

- **Hard threshold $\phi_{\mathrm{hard}}$ vs smooth envelope $\phi_s,\phi_\beta$.** Hard is exact integer; smooth is approximation with sharpness parameter. L1-M should treat them as two SUB-CASES, not bundle them.
- **Dominant bars (length $\ge\ell_{\min}+\tau$) vs sub-threshold bars (length $<\ell_{\min}-\tau$) vs edge-band bars ($|\ell-\ell_{\min}|\le\tau$).** The error decomposition is exactly the partition into these three.
- **Real-valued $K_{\mathrm{soft}}^\phi\in\mathbb R_{\ge 0}$ vs integer $K_{\mathrm{act}}\in\mathbb N$.** They cannot be globally equal; only approximately equal.
- **Resolved regime (T-L1-F applies) vs overlap regime (T-L1-F fails).** L1-M only operates in the resolved regime. Outside, $K_{\mathrm{bar}}\neq K_{\mathrm{act}}$ already, so $K_{\mathrm{soft}}^\phi\neq K_{\mathrm{act}}$ is also expected.
- **Approximation-of-$K_{\mathrm{bar}}$ vs surrogate-for-variational-$K_{\mathrm{bar}}$.** L1-M is the first; the latter (using $K_{\mathrm{soft}}^\phi$ as a differentiable surrogate in optimization) is downstream and not in scope for Day 7.

---

## §6. Brainstorm Questions

These are the open questions Day 7 should consider — not all need to be resolved, but they should be acknowledged in `kbar_kact_bridge_L1M_soft_count_corollary.md` §future-work:

- Should $\Phi_{\mathrm{res}}$ be defined by **threshold suppression + dominant retention + normalization**, or is there a cleaner axiomatic definition?
- Is **hard threshold the canonical count** and smooth $\phi$ only an approximation? (The CV-1.5.2 status of T-L1-F via $K_{\mathrm{bar}}=K_{\mathrm{act}}$ uses hard threshold; soft count is downstream.)
- Can $\phi_{\mathrm{logistic}}^s$ converge to $\phi_{\mathrm{hard}}$ as $s\to\infty$? (Yes, pointwise + uniformly on $[0,\ell_{\min}-\tau]\cup[\ell_{\min}+\tau,\infty)$; transition band shrinks.) What is the rate?
- What is the **cleanest error norm**? Sup-norm of bar lengths? $L^1$? Per-bar pointwise vs aggregate? The $|K_{\mathrm{soft}}-K_{\mathrm{bar}}|$ form is the simplest; per-bar error is finer.
- Should **edge-band bars be excluded by a margin hypothesis** (E)? "No bars in $[\ell_{\min}-\tau,\ell_{\min}+\tau]$" is clean but restrictive; bound $\rho_{\mathrm{edge}}^\phi\le 2\tau\cdot|\{i:|\ell_i-\ell_{\min}|\le\tau\}|$ is more general.
- Can $K_{\mathrm{soft}}^\phi$ become a **differentiable surrogate** for $K_{\mathrm{bar}}$ that's useful in variational SCC dynamics? (Not in scope for Day 7, but flag for future work.)
- Is L1-M useful for **future $\sigma$-rich / K-jump diagnostics**? (Likely yes — soft count is sensitive to bar prominence, which captures aggregate-merger events that integer count misses. But this is OP-0008 territory and beyond Day 7.)
- How does L1-M relate to the **WQ-LAT-1.C $\Phi_{\mathrm{res}}$ correction** already flagged in `ksoft_kact_bridge_lemma.md` §5.3.3? L1-M should be the rigorous version of WQ-LAT-1.C under T-L1-F.
- Is there a **statement of the L1-M theorem that does NOT require T-L1-F**? Step 1 (envelope-pure inequality) holds without T-L1-F; only Step 2 (substitution) uses T-L1-F. The envelope-pure inequality is a general statement about persistence diagrams + envelope class.

---

## §7. Non-Claims to Guard

Day 7 must NOT assert:

- **Global $K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}$.** Only conditional + with explicit error.
- **Use of arbitrary monotone Lipschitz $\phi$.** WQ-LAT-1.B disproves this category. L1-M is restricted to $\Phi_{\mathrm{res}}$.
- **OP-0005 (K-Selection) solved.** L1-M is a counting bridge; not a K-selection mechanism.
- **OP-0008 ($\sigma^A$ K-jump non-determinism) solved.** L1-M is restricted to the resolved regime; K-jump non-determinism is overlap-regime territory.
- **$\sigma_{\mathrm{rich}}$ sufficiency.** L1-M does not address $\sigma$-inheritance.
- **Reservoir framework canonical.** Reservoir reading remains working-grade; L1-M does not promote it.
- **P7 generally derived from all SCC states.** Inherited limitation from T-L1-F (per L1-L).
- **Application / robotics / vision claims.** L1-M is finite-graph multi-formation theory only.

These non-claims should be repeated explicitly in the L1-M document §non-claims, mirroring the T-L1-F entry style in `theorem_status.md` CV-1.5.2.

---

## §8. Tomorrow's Desired Mental Posture

The goal is **not** to force softness to equal discreteness. The goal is to understand:

- **when** a soft morphology score $K_{\mathrm{soft}}^\phi$ faithfully shadows a resolved hard count $K_{\mathrm{bar}}^{\ell_{\min}}$, and
- **when** its deviation $|K_{\mathrm{soft}}^\phi-K_{\mathrm{bar}}|$ becomes meaningful information rather than envelope artifact.

The CV-1.5.2 hard count is the **anchor**. Soft count is a real-valued shadow with envelope-dependent fidelity. L1-M characterizes that fidelity precisely under the L1-J regime + $\Phi_{\mathrm{res}}$ + edge-band control.

Day 7 should feel like: **the discrete result has been canonized; now we calibrate the continuous neighborhood around it.** The continuous neighborhood is structurally informative — it tells us how robust the count is to choice of envelope, and identifies which envelopes preserve the discrete answer up to controlled error.

---

## §9. W5 Close Ceremony Note

Day 7 is also the **W5 close**. `weekly_summary.md` finalize for W5 and W6 strategic plan are scheduled in parallel (per Day 6 plan §3 Block 5). The L1-M corollary work IS the substantive content for W5 close: T-L1-F (Day 6 promotion) + L1-M (Day 7 corollary draft) is a coherent W5-end research arc — the resolved-regime hard count + its controlled soft-count companion.

W5 ends with:
- **CV-1.5.2 canonical** (T-L1-F Cat-A conditional).
- **L1-M working draft** (soft-count corollary candidate).
- **W6 strategic plan** seeded by Day 7.

W5's identity at close: "Multi-formation resolved-regime counting, hard and soft, both layers established."

---

## §10. Closing Gaze

The L1 chain (L1-A through L1-L) is the substantive content of W5 in the multi-formation theory. T-L1-F is its canonical pinnacle. L1-M is the first downstream corollary.

What comes after L1-M:
- **L1-M-AUDIT** (next external audit, parallel to L1-K).
- **L1-M-FORMALIZE** (full proof write-up).
- **OP-0008 return path** (use the resolved-regime baseline + soft-count companion to attack $\sigma^A$ K-jump non-determinism in the overlap regime).
- **L1-N dynamics-compatible regime persistence** (find SCC initial states in the L1-J regime, integrate forward, measure regime-membership trajectories).
- **L1-L-FORMALIZE** (full Combes-Thomas / discrete Agmon derivation of P7 from primitive SCC; substantive).

Day 7 contributes one durable artifact: the L1-M working document. The rest is parking-lot for W6 and beyond.
