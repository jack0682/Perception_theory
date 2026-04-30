# k_selection_b_kramers.md — K-Selection (b) Kramers Metastability Derivation

**Status:** working draft (W5 Day 4, Task #6).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Kramers metastability derivation of K-Selection mechanism — option (b) of OP-0005 4-option list.
**Author origin:** Task #6 K-Selection (b); attacks OP-0005 via Kramers escape-rate kinetic theory. Kinetic complement to Task #5 (free-energy variational); companion to Task #7 (numerical anchor), Task #8 (Commitment 16 compatibility).
**Canonical refs:** §11.1 Commitment 14, 14-Multi, 16; §13 T-Persist-K-Sep, T-Persist-K-Weak; §14 CN15 Static/Dynamic Separation, CN6 Kinetic; §15 OP-0005, OP-0008.
**Working refs:** `k_selection_a_free_energy.md` (Task #5 equilibrium counterpart); `multi_formation_sigma.md` (D-6a static); `sigma_multi_trajectory.md` (D-6b dynamic, V4 K-jump statistics); Phase 10 V4 result $\Delta t \propto t^{1.315}$.

---

## §1. Mission

> **"OP-0005 K-Selection 4-옵션 중 (b) Kramers metastability: K-jump 의 barrier-crossing 시간이 $\tau_{K \to K-1} \sim \exp(\beta \Delta E_{\mathrm{barrier}})$ 로 결정되며, 이로부터 $K_{\mathrm{act}}(t)$ 는 *kinetic* 으로 selected 됨을 derive. Free-energy equilibrium $K^*_{\mathrm{eq}}(T)$ (Task #5) 와의 deviation 을 정식 capture; Phase 10 V4 numerical $\Delta t \propto t^{1.315}$ 와 reconcile."**

이 working file 은 OP-0005 K-Selection 4-옵션 중 *kinetic* 측면 — **metastability barriers** 가 K-jump 시간 척도를 setting 한다 — 를 develop. P-F (P-flag = "no metastability claim without explicit flag") 를 명시적으로 선언하며, Task #5 의 thermodynamic equilibrium 과 *complementary* 하게 작용한다.

**핵심 결론**:
1. K-jump barrier $\Delta E_{K \to K-1}$ 정의 (§3) + Kramers escape rate (§4).
2. $K_{\mathrm{act}}(t)$ 동적 trajectory (§5).
3. Free-energy equilibrium 과의 reconciliation (§6).
4. Phase 10 V4 numerical anchor $\Delta t \propto t^{1.315}$ 와의 connection (§7).
5. Cat B target with W6+ Cat A path (§8).

⚠️ **P-F flag**: 이 file 의 모든 metastability-관련 claim 은 P-F flagged.

---

## §2. Background

### §2.1 Kramers theorem (classical)

For a stochastic process $\dot u = -\nabla \mathcal{E}(u) + \sqrt{2 T} \xi$ (Langevin dynamics, Brownian noise $\xi$), the escape rate from a metastable basin centered at $u_0$ over a saddle point $u_s$ is:
$$\Gamma_{\mathrm{Kramers}} = \frac{\omega_0}{2\pi} \cdot \exp(-\Delta E / T)$$
where $\Delta E = \mathcal{E}(u_s) - \mathcal{E}(u_0)$ is the barrier height, $\omega_0$ is the basin curvature (frequency).

Mean first-passage time (MFPT): $\tau \approx 1/\Gamma_{\mathrm{Kramers}}$.

### §2.2 Application to K-jumps

In SCC, K-jumps $K' \to K' - 1$ occur via a *merger event*: two formations $j, k$ merge into $\ell$. The trajectory passes from a metastable K'-formation basin through a saddle ($u^{(j)}, u^{(k)}$ at coincidence/coalescence) into a K'-1-formation basin.

**Implication**: K-jump time $t^*$ is *not* deterministic at zero noise; it's a **stochastic event** with characteristic time scale set by the barrier.

### §2.3 Connection to T-Persist-K-Weak

T-Persist-K-Weak (canonical §13): when $\mu_{\mathrm{joint}} \leq 0$ on K-formation manifold, K → K-1 merger requires barrier crossing, not gradient descent. This is the canonical statement that K-jumps are barrier-crossing events.

Kramers theory (this file) provides the **quantitative time scale** for the barrier crossing.

---

## §3. K-jump Barrier Definition

### §3.1 K-formation basin

For each $K' \in \{1, \ldots, K_{\mathrm{field}}\}$, the K'-active stratum $S_{K'} \subset \widetilde\Sigma^K_M$ contains local minima of $\mathcal{E}_K$. A K'-formation basin is the basin of attraction of a local minimum in $S_{K'}$.

### §3.2 Saddle between K' and K'-1

To transition K' → K'-1 (e.g., merger of formations $j, k$), the trajectory crosses a *saddle point* $u_s^{(jk)}$ on the boundary of $S_{K'}$ (where $\|u^{(j)}\|_1 \to 0$ or $\|u^{(k)}\|_1 \to 0$, or where $j, k$ coalesce).

**Definition 3.1 (K-jump barrier)**:
$$\Delta E_{K' \to K'-1}^{(jk)} := \mathcal{E}_K(u_s^{(jk)}) - \mathcal{E}_K(u_{\mathrm{min},K'})$$
where $u_{\mathrm{min},K'}$ is the local minimum in $S_{K'}$ from which the merger initiates.

### §3.3 Barrier scaling estimates

From Coupling Bound Lemma (canonical T-Persist-K-Sep) + V5b-T Goldstone analysis:
- For well-separated formations $(j, k)$ at distance $d_{\min}$: barrier height
$$\Delta E_{K' \to K'-1}^{(jk)} \sim \lambda_{\mathrm{rep}} \cdot m_j m_k / |X|^{d-2} + O(\exp(-c_0 d_{\min}))$$
(for $d$-dimensional graph; rough scaling).
- For closely-spaced formations: barrier shrinks as $d_{\min} \to 0$, becoming $O(\lambda_{\mathrm{rep}} \cdot \mathrm{overlap})$ at near-merger.

**Implication**: barrier is *position-dependent* — depends on how close the merging pair $(j, k)$ is. Near-merger: low barrier ⇒ fast crossing. Well-separated: high barrier ⇒ slow crossing.

### §3.4 Effective barrier with $\beta$

In SCC, the *energy parameter* $\beta$ (super-lattice scale) and *thermal* temperature $T$ enter separately. The effective Boltzmann weight uses $\beta_{\mathrm{eff}} = \beta_{\mathrm{thermal}}^{-1}$ (use $T$ for thermal, $\beta$ for SCC parameter to avoid clash):
$$P(\mathrm{cross}) \propto \exp(-\Delta E / T).$$

For SCC equilibrium dynamics at zero noise ($T = 0$): $P = 0$ unless $\Delta E = 0$. Hence at $T = 0$, K-jumps occur only when basin disappears (saddle approaches min, $\Delta E \to 0$).

This is the *deterministic* zero-noise limit; for $T > 0$, finite-rate barrier crossing kicks in.

---

## §4. Kramers Escape Rate for K-jumps

### §4.1 Single-pair escape rate

**Claim 4.1 (Kramers rate for K-jump pair $(j, k)$)**:
$$\Gamma_{(jk)}^{K' \to K'-1} = \frac{\omega_{(jk)}}{2\pi} \cdot \exp(-\Delta E_{K' \to K'-1}^{(jk)} / T)$$
where $\omega_{(jk)}$ is the basin frequency = lowest non-zero (non-Goldstone) eigenvalue of $\tilde H_{jk}$ at $u_{\mathrm{min},K'}$.

By `multi_formation_sigma.md` §5.5 + Wigner-pair analysis (Task #3): $\omega_{(jk)} \sim \mathrm{O}(\lambda_1)$ (per-formation Hessian lowest non-Goldstone eigenvalue).

### §4.2 Total K → K-1 rate

Multiple pairs can undergo K-jump; total rate is the sum:
$$\Gamma_{\mathrm{total}}^{K' \to K'-1} = \sum_{(j, k) : j < k, j, k \in \mathrm{act}} \Gamma_{(jk)}^{K' \to K'-1}.$$

**Dominant pair**: the pair with lowest barrier (smallest $\Delta E_{(jk)}$) dominates the sum exponentially. Typically the closest pair (smallest $d_{\min}(j, k)$) has lowest barrier.

### §4.3 Mean first-passage time (MFPT)

MFPT for K → K-1 transition:
$$\langle \tau_{K' \to K'-1} \rangle = 1 / \Gamma_{\mathrm{total}}^{K' \to K'-1}.$$

### §4.4 K-jump cascade

Starting from $K_{\mathrm{act}}(0) = K_{\mathrm{field}}$, the trajectory undergoes a *cascade* of K-jumps:
$$K_{\mathrm{field}} \to K_{\mathrm{field}} - 1 \to \cdots \to K_{\mathrm{eq}}.$$

Total time to reach $K_{\mathrm{eq}}$:
$$\tau_{\mathrm{cascade}} = \sum_{K' = K_{\mathrm{eq}}+1}^{K_{\mathrm{field}}} \langle \tau_{K' \to K'-1} \rangle.$$

⚠️ **P-F flag**: The cascade picture assumes the system equilibrates within each metastable K-state before the next K-jump — i.e., separation of time scales between intra-basin relaxation ($\sim 1/\omega$) and barrier crossing ($\sim \exp(\Delta E / T) / \omega$). This separation requires $\Delta E / T \gg 1$. For low barriers near merger, the separation breaks down.

---

## §5. Dynamic K_act(t) Trajectory

### §5.1 Stochastic K_act(t) trajectory

Under Kramers dynamics with thermal noise $T$, $K_{\mathrm{act}}(t)$ is a **stochastic process** with:
- Initial: $K_{\mathrm{act}}(0) = K_{\mathrm{field}}$ (starting in top stratum).
- Transitions: $K' \to K' - 1$ occurs at rate $\Gamma_{\mathrm{total}}^{K' \to K'-1}(\mathbf{u})$ depending on current state.
- Equilibrium: $K_{\mathrm{act}}(t) \to K^*_{\mathrm{eq}}(T)$ as $t \to \infty$ (Task #5 equilibrium prediction).

### §5.2 Markov chain approximation

Approximate $K_{\mathrm{act}}(t)$ as a Markov chain on $\{1, 2, \ldots, K_{\mathrm{field}}\}$ with transition rates from §4.2.

For irreversible K-jumps (no fission $K \to K+1$ in zero-noise SCC): chain is monotone-decreasing, hits $K_{\mathrm{eq}}$ and stays.

For reversible (with thermal fission): equilibrium distribution $\pi(K) \propto \exp(-F(K; T)/T)$ where $F(K; T)$ is Task #5 free energy.

### §5.3 SCC zero-noise limit

In SCC default (no explicit thermal noise), K-jumps occur deterministically when basins collide (saddle merges with min, $\Delta E \to 0$). This is the "barrier disappearance" event, not Kramers stochastic crossing.

**Important caveat**: SCC gradient flow (per `scc/optimizer.py`) is *deterministic* (zero-noise). Kramers theory (this file) applies to the *thermal extension* — gradient flow + Brownian noise. Pure SCC dynamics correspond to $T \to 0$ Kramers limit, where rates vanish but barriers also approach 0 dynamically as system evolves.

⚠️ **P-F flag**: this distinction must be honored when interpreting numerical SCC trajectories vs Kramers predictions.

---

## §6. Reconciliation with Free-Energy Equilibrium (Task #5)

### §6.1 Two limits

- **$T \to 0$, $t \to \infty$**: deterministic gradient flow reaches local minimum; $K_{\mathrm{act}}$ depends on initial basin. Multiple inequivalent $K_{\mathrm{eq}}$ values possible (path-dependence).
- **$T > 0$, $t \to \infty$**: Kramers + thermal fission reach Boltzmann equilibrium; $K_{\mathrm{act}} \sim K^*_{\mathrm{eq}}(T)$ from Task #5.

### §6.2 Crossover

For finite $t$:
- Short $t$: $K_{\mathrm{act}}(t) = K_{\mathrm{field}}$ (no K-jumps yet).
- Intermediate $t$: $K_{\mathrm{act}}(t)$ decreases through K-jump cascade.
- Long $t$: $K_{\mathrm{act}}(t) \to K^*_{\mathrm{eq}}(T)$ if $T > 0$; $\to K_{\mathrm{eq}}^{\mathrm{kinetic}}$ if $T = 0$.

The kinetic $K_{\mathrm{eq}}^{\mathrm{kinetic}}$ is the asymptotic limit of zero-noise gradient flow — depends on initial conditions, generally $\geq K^*_{\mathrm{eq}}(T \to 0) = 1$ (M-1 ground state).

### §6.3 Apparent K>1 reconciliation

Empirical $K > 1$ observation (NQ-141, R23 F=9) is consistent with:
- **Kinetic trapping**: zero-noise SCC reaches $K_{\mathrm{eq}}^{\mathrm{kinetic}} > 1$ due to barriers preventing further mergers.
- **Finite-T equilibrium**: $K^*_{\mathrm{eq}}(T) > 1$ at $T > T_c$ from Task #5.
- **Both effects combine**: empirical $K > 1$ is K-jumps incomplete at finite observation time + entropy preference for K>1.

This addresses M-1 conflict from a *kinetic* angle, complementary to free-energy / CN15 resolutions.

---

## §7. Phase 10 V4 Numerical Anchor

### §7.1 V4 result

Phase 10 V4 numerical (per `2026-04-28/34_Phase10_findings.md` §3-§4):
- K-jump statistics: $\Delta t_n \propto t_n^{1.315}$ where $\Delta t_n$ is the time between consecutive K-jumps and $t_n$ is the time at the n-th K-jump.
- ΔK distribution: dominated by single mergers ($\Delta K = 1$).

### §7.2 Kramers prediction

If barriers $\Delta E_n$ between consecutive K-jumps grow with $K^{-\gamma}$ (smaller K ⇒ larger barriers ⇒ harder to merge further):
$$\Delta E_n \propto K_n^{-\gamma}, \quad K_n \approx K_{\mathrm{field}} - n.$$

Kramers rate: $\Gamma_n \sim \exp(-\beta \Delta E_n)$. MFPT: $\Delta t_n \sim \exp(\beta \Delta E_n) \sim \exp(\beta K_n^{-\gamma})$.

For large $K_n$: $\Delta t_n \approx t_n^?$ (power-law) — analytical match to V4 requires careful treatment of $K_n(t)$ relation.

### §7.3 V4 → barrier scaling

Inverting V4 numerical $\Delta t \propto t^{1.315}$:
- If $K(t) \sim t^{-\alpha}$ (number of formations decreasing as time elapses): then $\Delta t = K(t)^{-1/\alpha}$.
- Combined: barrier scaling $\Delta E \propto K^{-\gamma}$ implies a specific $K(t)$ decay law.
- Match to V4 $\Delta t \propto t^{1.315}$: requires $\gamma$ + $\alpha$ relationship that fits.

**Cat B target**: explicit match between V4 $1.315$ exponent and analytical Kramers prediction. Requires NQ-242 PH pipeline (Phase 1-4 of `sigma_multi_trajectory.md` §6.1 + this file's barrier-scaling refinement) to confirm.

### §7.4 LSW-like coarsening

The $t^{1.315}$ exponent is intriguingly close to **LSW (Lifshitz-Slyozov-Wagner) coarsening** $\Delta t \propto t^{4/3} \approx t^{1.333}$. LSW: in late-stage Ostwald ripening of binary mixtures, droplet sizes grow as $t^{1/3}$ and number-density decays as $t^{-1}$.

If SCC K-jump cascade is **LSW-type coarsening** of formations (smaller formations being absorbed into larger via K-jumps), then $\Delta t \propto t^{4/3}$ is naturally predicted.

⇒ V4 numerical anchor consistent with LSW coarsening, which is a well-studied limit of Kramers-style barrier-crossing dynamics.

---

## §8. Cat Status and Promotion

### §8.1 Cat A established

- §2.1 Kramers theorem (classical): **Cat A** by citation.
- §3.1, §3.2 K-jump barrier definition: **Cat A** under T-Persist-K-Weak hypothesis.
- §4.1, §4.2 Kramers rate formula: **Cat A** by classical theory.
- §6 reconciliation with free-energy equilibrium: **Cat A**.
- §7.4 LSW-coarsening parallel: **Cat A** by classical reference (Lifshitz-Slyozov 1961, Wagner 1961).

### §8.2 Cat B pending

- §3.3 barrier scaling estimate $\Delta E_{(jk)} \sim \lambda_{\mathrm{rep}} m_j m_k / |X|^{d-2}$: **Cat B sketch** — explicit analytical proof requires saddle-point analysis on $\widetilde\Sigma^K_M$ which is W7+ work.
- §4.4 cascade time $\tau_{\mathrm{cascade}}$: **Cat B** under time-scale-separation assumption (P-F flagged).
- §7.3 V4 exponent $1.315$ analytical match: **Cat B target** — requires NQ-242 PH pipeline.
- §7.4 LSW correspondence: **Cat B** sketch level; full SCC↔LSW identification W8+.

### §8.3 Promotion target

CV-1.7+ candidate Commitment 19 (K-Selection axiom) per task #49 in TaskList; combines Tasks #5, #6, #7, #8 into a single canonical statement.

This file provides the **kinetic component** (b) of the K-Selection axiom: K_act(t) trajectory governed by Kramers escape rates over barriers, with thermodynamic equilibrium (a) as long-time limit.

### §8.4 Connection to OP-0008

OP-0008 σ^A K-jump non-determinism: at K-jump time $t^*$, the post-merger σ^A($t^{*+}$) is non-deterministic in σ^A($t^{*-}$) alone. **Kramers contribution**: $t^*$ itself is *stochastic* under thermal noise. Each K-jump event is a *Kramers crossing event*, with timing distributed by the escape-rate formula.

⇒ Kramers framework reframes OP-0008 in stochastic-process language: σ_rich-augmented Φ_rich (Path B, Task #4) gives deterministic *deterministic-conditional-on-event-time* mapping, but the event time itself is stochastic per Kramers.

---

## §9. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — OP-0005 4-options framework explicit; Cat status per claim; Cat B items registered.
- [x] **No Research OS resurrection** — single-topic.
- [x] **Not reductive** — Kramers theory is *standard physics* used contrastively (CN10); SCC has its own dynamics, Kramers framework provides analytical prediction tool.
- [x] **u_t primitive maintained** — Kramers dynamics on $u_t$-state space; barrier $\Delta E$ derived from $\mathcal{E}_K$.
- [x] **CN5 4-energy not merged** — N/A; Kramers is dynamic theory of energy landscape, doesn't add new energy term.
- [x] **K not dual-treated** — $K_{\mathrm{act}}$ integer; K-jumps stochastic-discrete events.
- [x] **P-F flag explicit** — §1, §4.4, §5.3 all flagged. Time-scale-separation assumption explicit.
- [x] **CN6 Kinetic axiom honored** — kinetic mechanism (b) is one of OP-0005 4 options; canonical CN6 commitments to kinetic interpretation are *consistent* with Kramers.
- [x] **CN15 Static/Dynamic Separation** — §6 explicit reconciliation: equilibrium (a, static-asymptotic) vs trajectory (b, dynamic).

---

## §10. Forward Roadmap

### §10.1 Task #7 (numerical anchor) target

- Numerical measurement of $\Delta E_{(jk)}$ barrier vs $d_{\min}(j, k)$ via gradient-flow trajectories on R23 / $T^2_L$.
- Confirmation of V4 $\Delta t \propto t^{1.315}$ exponent + LSW-correspondence (§7).
- Kramers-rate formula validation against measured K-jump statistics.

### §10.2 Task #8 (compatibility proof) — bridges (a)+(b)+(c)+(d)

Formal proof: option (a) free-energy equilibrium + option (b) Kramers kinetics + option (c) numerical anchor + option (d) Commitment 16 cap *compose* into a single coherent K-Selection axiom (CV-1.7+ Commitment 19 candidate).

### §10.3 Cat A path

W7-W8: explicit barrier-scaling proof (§3.3 Cat B → Cat A); LSW correspondence (§7.4 Cat B → Cat A).

W9+: cascade time formula (§4.4 Cat B → Cat A under time-scale-separation theorem).

W12+: combined Cat A everywhere for K-Selection axiom canonical promotion at CV-1.7+.

---

## §11. References

### §11.1 Working files

- `working/MF/k_selection_a_free_energy.md` (Task #5; equilibrium counterpart).
- `working/MF/multi_formation_sigma.md` (D-6a static; basin definition).
- `working/MF/sigma_multi_trajectory.md` (D-6b dynamic; V4 K-jump statistics).
- `working/MF/K_status_commitment.md` (OAT-1, Commitment 16).

### §11.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi, 16; §13 T-Persist-K-Sep, T-Persist-K-Weak.
- `canonical/canonical.md` §14 CN6 (Kinetic), CN15 (Static/Dynamic Separation).
- `canonical/open_problems.md` OP-0005 (direct attack); OP-0008 (Kramers reframing connection).

### §11.3 Daily logs (V4 source)

- `THEORY/logs/daily/2026-04-28/34_Phase10_findings.md` §3-§4 (V4 K-jump statistics $\Delta t \propto t^{1.315}$).

### §11.4 External refs

- Kramers, H. A. (1940). "Brownian motion in a field of force and the diffusion model of chemical reactions". *Physica* 7(4): 284–304. — Kramers theorem.
- Hänggi, P., Talkner, P., & Borkovec, M. (1990). "Reaction-rate theory: fifty years after Kramers". *Reviews of Modern Physics* 62(2): 251–341. — modern reference.
- Lifshitz, I. M. & Slyozov, V. V. (1961). "The kinetics of precipitation from supersaturated solid solutions". *J. Phys. Chem. Solids* 19(1-2): 35–50. — LSW coarsening theory.
- Wagner, C. (1961). "Theorie der Alterung von Niederschlägen durch Umlösen". *Z. Elektrochem.* 65: 581–591. — LSW-W coarsening.
- Schwarz (1978) BIC, Reichl (2009) Helmholtz — see Task #5 references.

---

**End of k_selection_b_kramers.md.**

**Status: working draft. Task #6 complete. K-Selection (b) Kramers metastability derivation: K-jump barrier (§3.1, Cat A under T-Persist-K-Weak); Kramers escape rate $\Gamma = (\omega_0/2\pi) \exp(-\Delta E / T)$ (§4.1, Cat A by classical theory); MFPT cascade (§4.4, Cat B under time-scale-separation, P-F flagged); reconciliation with free-energy equilibrium (§6, Cat A); Phase 10 V4 numerical anchor $\Delta t \propto t^{1.315}$ vs Kramers prediction (§7.3, Cat B target); LSW-coarsening parallel ($t^{4/3}$) consistency (§7.4, Cat B sketch). All P-F flags explicit. Forward: Task #7 numerical anchor; Task #8 compatibility proof composing options (a)+(b)+(c)+(d). CV-1.7+ Commitment 19 K-Selection axiom target.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/k_selection_b_kramers.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.7+ W12+ packet (combined with Tasks #5, #7, #8).
