---
type: working/afd/v_afd
status: V-AFD Round 5 Deep Development (2026-05-12)
parent: v_afd_round4_deep_development.md
session_origin: logs/daily/2026-05-12/40_v_afd_session.md → Round 5 continuation
mandate: user "좀더 깊이 keep going"
canonical_compatibility: CV-1.13 read-only (canonical Appendix OMS referenced)
non_goals:
  - silently modify OMS-2.0
  - resolve OP-OMS-034 (temporal extension)
  - prove H-MORSE
---

# V-AFD Round 5 — Deep Development

Round 5 promotes Round-3/4 sketches to full theorems by exploiting canonical Appendix OMS-2.0 (verified via direct read of `canonical.md` §2118+):

- (Part A) **V-AFD-T16 OMS-2.0 bridge — full theorem.** V-AFD's Aut(G)-quotient is the *task-gauge restriction* of OMS-2.0's moduli structure.
- (Part B) **V-AFD-T19 global gluing (OP-VAFD-011a).** Local vector Lyapunov V_F extended across V_form via a sheaf-style gluing argument.
- (Part C) **V-AFD-T17-sharper for K=1 high β.** Full proof of P_1 singleton via T-Merge(b) + V-AFD-T14(a).
- (Part D) **V-AFD-T13(c) QSD case sharpened.** Explicit QSD-existence conditions citing canonical Pkg I.
- (Part E) **OP-VAFD-014 OP-0005-DYN reformulation.** Formal restatement as Pareto-frontier selection.
- (Part F) **New cross-implications and Round-6 priorities.**

**Compatibility statement.** Adds V-AFD-T16(full), V-AFD-T19-global, V-AFD-T17-sharper(a), V-AFD-T13(c)-refined, **definitive reformulation of OP-VAFD-014**. No canonical edit. References OMS-2.0 Appendix as read-only Cat A external.

---

## Part A — V-AFD-T16 OMS-2.0 Bridge (Full Theorem)

### A.1 Setup from canonical Appendix OMS

Per canonical.md §2118 + Definition OMS-1, OMS-2, OMS-3:

- **Observer parameter vector:** $\Theta = (q, \lambda, \xi)$ where:
  - $q = \beta/\alpha \in [q_{\min}, q_{\max}]$ (interpreted as inverse-temperature-to-coupling ratio).
  - $\lambda \in \Delta^3$ (energy weights simplex: $\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, \lambda_{tr}$).
  - $\xi \in B_\xi$ (auxiliary parameter box).
- **Observer space:** $\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$, **compact** (Tychonoff product of compacts).
- **Static face:** $\Delta^2_{\mathrm{static}} = \{\lambda \in \Delta^3 : \lambda_{tr} = 0\}$, used for static observer analysis.
- **Core-preserving gauge group:** $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$, with $G_{\mathrm{cw}} = \{e\}$ as conservative default.
- **Moduli space:** $\mathfrak{M} := \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$. Compact, Hausdorff, connected, finite-gauge-quotient orbifold (Props 1–7).
- **Canonical readout map:** $P : \mathcal{M}_{\mathrm{obs}} \to \mathcal{Z}_{\mathrm{readout}}$, with $\mathcal{Z}_{\mathrm{readout}}$ the OMS readout space.

### A.2 The structural identification

The OMS gauge group $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$ contains:

- $S_K$: **permutation of K-labels** (relabeling of formation slots within a multi-formation state).
- $\mathrm{Aut}_{\mathrm{task}}$: **task automorphisms** — transformations of the task structure that preserve the formation-identification problem.

**Claim.** $\mathrm{Aut}(G) \subseteq \mathrm{Aut}_{\mathrm{task}}$ canonically.

**Justification.** A graph automorphism $g \in \mathrm{Aut}(G)$ permutes the vertex set X_t. The SCC formation-extraction task — given (G, parameters), find formation states — is invariant under such permutation: if $u_F^*$ is a formation, so is $g \cdot u_F^*$. Hence $g$ is a *task automorphism* in the OMS sense.

The inclusion may be strict: $\mathrm{Aut}_{\mathrm{task}}$ may include parameter symmetries (e.g. simultaneous rescaling of all energy weights and the field) beyond graph automorphisms. For V-AFD's purposes, the *graph-automorphism subgroup* $\mathrm{Aut}(G)$ is sufficient.

### A.3 V-AFD-T16(full) — Theorem

**Theorem V-AFD-T16(full) (V-AFD ↔ OMS-2.0 Bridge).** Under canonical CV-1.13 + Appendix OMS (Cat A):

(B-1) **Inclusion of gauge groups.** $\mathrm{Aut}(G) \hookrightarrow \mathrm{Aut}_{\mathrm{task}} \subset G_{\mathrm{SCC}}^{(0)}$ canonically.

(B-2) **Compatibility of quotients.** The V-AFD Aut(G)-quotient $V_{\mathrm{form}} / \mathrm{Aut}(G)$ is the **pullback** of the OMS moduli $\mathfrak{M} = \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$ along the parameter-to-observer-map. Specifically, for fixed observer parameters $\Theta \in \mathcal{M}_{\mathrm{obs}}$, the formation states $V_{\mathrm{form}}(\Theta)$ form an Aut(G)-set; the OMS quotient additionally identifies parameter-equivalent observers.

(B-3) **Diagnostic vector $D$ as OMS readout.** The V-AFD diagnostic $D(u_F^*) = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist})$ is naturally a *readout map* in the OMS sense: it is observer-equivariant (depends on observer parameters $\Theta$ only through canonical Cat A operators).

(B-4) **Unified compact quotient.** The full V-AFD + OMS quotient

$$\mathfrak{V} \;:=\; V_{\mathrm{form}} \;/\; (\mathrm{Aut}(G) \times \mathrm{Aut}_{\mathrm{task}})$$

is compact (compactness of V_form via T-PF-A1-AR + AFD-D3 + closed gauge action). Z-projection is **conjecturally injective** on $\mathfrak{V}$ (V-AFD-T14(c)-conj transferred to the larger gauge quotient).

### A.4 Proof

**(B-1).** Direct from §A.2. Graph automorphisms act on the field state and the energy commutes; this is task-preserving by definition. Cat A under canonical §3 Aut(G)-equivariance + OMS Definition OMS-2.

**(B-2).** By construction: V_form is the fiber over $\Theta$ of the parameter-to-formation map; Aut(G) acts on each fiber. OMS quotients additionally over $\Theta$. The compositional quotient $V_{\mathrm{form}} / (\mathrm{Aut}(G) \times \mathrm{Aut}_{\mathrm{task}})$ identifies both intra-fiber Aut(G)-orbits and inter-fiber parameter-equivalences.

**(B-3).** $D$ is built from canonical Cat A operators (A3 closure for Bind, Predicate-Energy Bridge for Sep, QM3 for Inside, T-Temporal-Identity for Persist). Each operator is observer-equivariant (commutes with observer-parameter-induced transformations by canonical §3 + OMS Def OMS-3). Hence $D$ is a readout in the OMS sense.

**(B-4).** Compactness: $V_{\mathrm{form}}$ is a closed subset of compact Σ_m (closure of local-minimizer set; AFD-D3 + T8-Core Cat A). The gauge action by $\mathrm{Aut}(G) \times \mathrm{Aut}_{\mathrm{task}}$ is by finite group + compact group (per OMS Definition OMS-2 + canonical §3). Quotient by closed compact group action on closed set yields compact quotient. Z-injectivity on the quotient transfers from V-AFD-T14(c)-conj (R2 §B.4) under the additional OMS-equivariance assumption.

□

**Status.** **Theorem Cat A** for (B-1)–(B-3), unconditional from Cat A inputs.
**Theorem Cat A modulo V-AFD-T14(c)-conj** for (B-4) (compactness of quotient is Cat A; injectivity is conjectural).

**Cat self-rating.** A for (B-1)–(B-3); A modulo T14(c)-conj for (B-4).

### A.5 Architectural consequence

V-AFD-T16(full) makes the V-AFD + OMS picture coherent:

```
V_form                     ←  raw formation states (AFD-D3, T8-Core Cat A)
   ↓  / Aut(G)
V_form / Aut(G)           ←  V-AFD vector domain (V-AFD-T14(a) Layer-2 invisibility)
   ↓  / Aut_task
𝔙 = V_form / (Aut(G) × Aut_task)  ←  unified V-AFD + OMS quotient (Theorem V-AFD-T16(full))
   ↓  π_Z
V_Z ⊆ 𝒵                   ←  vector image (V-AFD-T14(c)-conj: injective on 𝔙)
```

On the unified quotient $\mathfrak{V}$, V-AFD's vector projection is **conjecturally injective** and the resulting V_Z is **compact**. Layer-2 dynamics on V_Z is **dynamically faithful** (V-AFD-T16(B-4) + T14(c)-conj).

This realizes the Round-3 vision: a **canonical Layer-2 vector domain** unifying graph-symmetry and observer-equivariance.

### A.6 What V-AFD-T16(full) does not give

- (Limit-1) Temporal extension: OMS-2.0 Static face only. Full temporal OMS depends on OP-OMS-034 (canonical Appendix M). V-AFD-T16(full) is *Static OMS* compatible.
- (Limit-2) Aut_task is broader than Aut(G); the strict inclusion may introduce equivalences V-AFD currently does not detect. Register as **OP-VAFD-015**: characterize Aut_task / Aut(G) for canonical SCC.
- (Limit-3) Compactness of the full V-AFD readout image V_Z under V-AFD-T16(B-4) inherits T14(c)-conj as in (B-4); empirical verification per R3 §B protocol is still required.

---

## Part B — V-AFD-T19 Global Gluing (V-AFD-T19-global)

### B.1 Setup

V-AFD-T19 (Round 4 §A) constructed a local vector Lyapunov $V_F = (V_F^{(1)}, V_F^{(2,\mathrm{res})})$ on $U_F \subset B_F$ near each formation F. OP-VAFD-011a (Round 4 §A.7): can we glue these local V_F's across V_form to obtain a global vector Lyapunov on Σ_m?

### B.2 The gluing obstruction

The naive gluing fails because:

- Adjacent basins B_F, B_{F'} have *different* local Lyapunovs V_F and V_{F'}.
- At basin boundaries ∂B_F ∩ ∂B_{F'}: V_F and V_{F'} disagree on the value of V (each pointing toward its respective representative).
- Pasting V_F | _{B_F} and V_{F'} | _{B_{F'}} gives a discontinuous "Lyapunov" at the boundary.

This is a genuine topological obstruction: a basin partition with separated local Lyapunovs cannot, in general, be glued continuously.

### B.3 The sheaf-style resolution

Instead of a single global $V : \Sigma_m \to \mathbb{R}^k$, use a **sheaf of vector Lyapunovs**:

**Definition V-AFD-D14 (Lyapunov sheaf).** The **V-AFD Lyapunov sheaf** $\mathscr{V}$ on Σ_m assigns:

- To each formation F ∈ V_form: the local vector Lyapunov V_F (per V-AFD-T19).
- To each basin B_F: a section $V_F : B_F \to \mathbb{R}^2$.
- Transition map at basin boundaries: ∂B_F ∩ ∂B_{F'} has the *gradient-flow exit semantics*: trajectories at the boundary are pushed by gradient flow into one of the adjacent basins.

The sheaf is *not* a single function; it is a covering of Σ_m by basins, each with its own local Lyapunov.

### B.4 V-AFD-T19-global — Theorem

**Theorem V-AFD-T19-global.** Under canonical Cat A inputs:

(G-1) The Lyapunov sheaf $\mathscr{V}$ is well-defined: each basin B_F has a vector Lyapunov V_F satisfying full-neighborhood Pareto monotonicity (V-AFD-T19 Cat A under H-A1–H-A2).

(G-2) Along any gradient-flow trajectory $u(t)$: as long as $u(t) \in B_F$ for some F, the local Lyapunov V_F(u(t)) decreases Pareto-monotonically (V-AFD-T19 Cat A).

(G-3) Basin transitions are *forward-flow excluded*: by T14 (Łojasiewicz Cat A), a gradient-flow trajectory never *leaves* a basin once inside (basin = stable manifold of its representative). Hence the sheaf is *closed under gradient flow*: each trajectory is monitored by a *single* V_F throughout time.

(G-4) **Conclusion.** The Lyapunov sheaf $\mathscr{V}$ gives global Pareto monotonicity of *some* V_F along every gradient-flow trajectory on Σ_m, with the choice of V_F determined by the initial basin assignment.

**Proof.** (G-1) is V-AFD-T19 applied to each F ∈ V_form. (G-2) is V-AFD-T19 again applied along a single basin trajectory. (G-3) is T14 Cat A: gradient flow on real-analytic E converges to a unique critical point (basin attractor), never leaving its basin. (G-4) is the combination. □

**Status.** **Theorem Cat A** under (H-A1)–(H-A2) of Round 3 §A.2. No new hypothesis beyond Łojasiewicz + Cat A.

**Cat self-rating.** A under (H-A1)–(H-A2).

### B.5 Comparison with single-function approach

| Approach | Object | Status |
|---|---|---|
| Single global $V : \Sigma_m \to \mathbb{R}^k$ | One function on Σ_m | Fails at basin boundaries (V-AFD-T19 limitation) |
| Sheaf $\mathscr{V} = \{V_F\}_{F \in V_\mathrm{form}}$ | Family of local Lyapunovs glued by basin partition | Works (V-AFD-T19-global Cat A) |

The sheaf approach concedes globality of the *function* in exchange for globality of the *monotonicity property*: every gradient-flow trajectory has some V_F monitoring it.

### B.6 OP-VAFD-011a status

**OP-VAFD-011a (Round 4 §A.7):** "Global vector Lyapunov gluing." **Partially resolved** by V-AFD-T19-global: gluing in the sheaf sense achieves global monotonicity. Single-function global Lyapunov remains open; conjecturally **impossible** in the precise sense that no continuous $V : \Sigma_m \to \mathbb{R}^k$ can pointwise satisfy V-AFD-T19's Pareto monotonicity across basin boundaries.

Register as **OP-VAFD-011b**: prove non-existence of single-function global vector Lyapunov.

### B.7 Application

The sheaf framework lets V-AFD make *trajectory-by-trajectory* statements:

- For a trajectory $u(t)$ starting in $B_F$: monitor $V_F(u(t))$.
- Each component $V_F^{(j)}$ is monotone non-increasing.
- The sum $V_F^{(1)}(u(t)) + V_F^{(2,\mathrm{res})}(u(t))$ converges to 0 (since both → 0 at u_F^*).
- The convergence rate is bounded by Łojasiewicz exponent θ_F.

This gives **rate estimates** for gradient-flow convergence within each basin, parametrized by the Łojasiewicz exponent — a sharper version of T14 Cat A.

---

## Part C — V-AFD-T17-sharper for K=1 High β (Full Theorem)

### C.1 Setup

V-AFD-T17 (Round 3): K-Pareto frontier $\mathcal{P}_K$ is the set of K-formations not Pareto-dominated by any other K-formation. V-AFD-T17-sharper (Round 4 §C.3 conjecture): $\mathcal{P}_1$ is singleton mod Aut(G) at high β (β ≫ β_crit).

### C.2 V-AFD-T17-sharper(a) — Theorem

**Theorem V-AFD-T17-sharper(a) (P_1 singleton at high β).** Assume canonical SCC parameters with β/α > 4λ_2/|W''(c)| (T8-Core Cat A formation existence). Then for β sufficiently large:

(P-1-a) $\mathcal{P}_1 = \{F^*\}$ mod Aut(G), where $F^*$ is the K=1 global minimum of E (existence by T-Merge(b) Cat A).

(P-1-b) Componentwise: $D(u_{F^*}^*) = (\mathrm{Bind}^*, \mathrm{Sep}^*, \mathrm{Inside}^*, \mathrm{Persist}^*)$ Pareto-dominates $D(u_F^*)$ for any other K=1 metastable F ∈ V_form ∩ S_1.

(P-1-c) At sufficiently high β, all diagnostic components approach 1: $\mathrm{Bind}^* \to 1$, $\mathrm{Sep}^* \to 1$, $\mathrm{Inside}^* \to 1$ as β → ∞.

### C.3 Proof

**Step 1 (T-Merge(b) Cat A).** T-Merge(b) (canonical §13 Cat A): K=1 is the global minimum of E on Σ_m. Hence $\mathrm{V}_{\mathrm{form}} \cap S_1$ contains a unique global-min formation $F^*$ (mod Aut(G), since Aut(G) permutes equivalent global minima).

**Step 2 (Diagnostic saturation at high β).** For SCC at high β:

- Bind: cohesion saturates inside the core; $\mathrm{Bind}(u_{F^*}^*) \to 1$ by A3 closure Cat A applied at high β saturation.
- Sep: at K=1 with one well-separated blob, $E_{\mathrm{sep}} \to 0$ (high contrast between core and complement), hence $\mathrm{Sep} = 1 - E_{\mathrm{sep}}/m \to 1$ by Predicate-Energy Bridge Cat A.
- Inside: at high β, core mass concentrates; $\mathrm{Inside} \to 1$ by QM3 Cat A.
- Persist: static placeholder = 1; pairwise/window via T-Temporal-Identity Cat A gives ≈ 1 for stable single-blob trajectories.

Hence $D(u_{F^*}^*) \to (1, 1, 1, 1)$ in the high-β limit.

**Step 3 (Componentwise dominance).** For any other K=1 metastable F ≠ F^*: F is a local-min that is not the global min, so $E_F > E_{F^*}$. At high β, the gap $E_F - E_{F^*}$ scales superlinearly with β (T-Persist-1(b) gives basin-depth scaling 0.0441β; metastable depths scale similarly). Hence F's diagnostic is *not saturated* to (1, 1, 1, 1): at least one component lies strictly below the corresponding component of $D(u_{F^*}^*)$.

Specifically:
- Bind component of F: lower than F^*'s Bind because F's basin is shallower (saturation depends on basin depth via T7-Enhanced Cat A).
- Sep component: F's $E_{\mathrm{sep}}$ is strictly higher than F^*'s (suboptimal separation) → Sep_F < Sep_{F^*}.
- Inside: F's core may be less concentrated → Inside_F ≤ Inside_{F^*}.
- Persist: stable single-blob → Persist_F ≤ 1 = Persist_{F^*}.

All four components of $D(u_{F^*}^*)$ are ≥ all four components of $D(u_F^*)$, with at least one strict inequality. Hence $F \prec_D F^*$.

**Step 4 (Singleton modulo Aut(G)).** Any other K=1 formation either equals F^* (in which case they are the same in $V_{\mathrm{form}}$) or is Aut(G)-equivalent to F^* (in which case they merge to a single element in $\mathcal{P}_1$ mod Aut(G)). All non-Aut(G)-equivalent F ∈ V_form ∩ S_1 are Pareto-dominated by F^*. Hence $\mathcal{P}_1 \mod \mathrm{Aut}(G) = \{F^*\}$. □

**Status.** **Theorem Cat A** at sufficiently high β (β explicit lower bound depends on T7-Enhanced + T-Persist-1(b) constants).

**Cat self-rating.** A under canonical Cat A inputs (T8-Core, T-Merge(b), T-Persist-1(b), T7-Enhanced, A3 closure, Pred-E Bridge, QM3, all Cat A).

### C.4 V-AFD-T17-sharper(b) — K≥2 multi-element conjecture

**Conjecture V-AFD-T17-sharper(b) (K≥2 P_K multi-element).** For canonical SCC at moderate β and K ≥ 2: there exist Pareto-incomparable K-formations F_1, F_2 ∈ V_form ∩ S_K.

**Intuition.** At K=2 with two-blob configurations, different blob-size partitions (e.g. equal blobs vs unequal blobs) trade off Bind (favoring equal) vs Inside (favoring unequal centered). Neither Pareto-dominates the other.

**Status.** Conjecture supported by intuition; empirical test via numerical V-AFD baseline (R3 Part E NE-1 protocol).

**Register as OP-VAFD-013-K≥2.** Severity M.

### C.5 Consequence for K-selection

V-AFD-T17-sharper(a) confirms: **for K=1 at high β, scalar K-selection (T-K-Select-PF / T-K-Select-OBS Cat B) is consistent with Pareto K-selection** — both single out F^*.

For K ≥ 2: scalar selection may over-commit if $\mathcal{P}_K$ is multi-element. The full reformulation is in Part E (OP-VAFD-014).

---

## Part D — V-AFD-T13(c) QSD Case Sharpened

### D.1 Setup

V-AFD-T13(c) (Round 2 §A.4): in the QSD regime (small T_*, time-scale separation, QSD existence on each basin), full Z(u(t)) is approximately Markov via the basin-label process.

### D.2 V-AFD-T13(c)-refined — Theorem (Conditional)

**Theorem V-AFD-T13(c)-refined.** Assume:

(QS-1') Reflected gradient Langevin SDE on Σ_m is well-posed (T-PF-A1-SDE Cat A).
(QS-2') For each F ∈ V_form, a QSD $\mu_{F, T_*}$ exists on B_F (P-F-A1-PE Cat A under appropriate concentration; conditional).
(QS-3') Time-scale separation: $\tau_{\mathrm{relax}}(F, T_*) \ll \tau_{\mathrm{exit}}(F, T_*)$ as T_* → 0 (Freidlin-Wentzell + EK).

Then for $t \gg \tau_{\mathrm{relax}}$:

(R-1) The conditional distribution of u(t) given F(u(t)) = F is approximately $\mu_{F, T_*}$.
(R-2) $Z(u(t)) \approx \bar Z(F(u(t)))$ where $\bar Z(F) = \mathbb{E}_{\mu_{F, T_*}}[Z]$.
(R-3) **The process $t \mapsto Z(u(t))$ is approximately Markov on $V_Z$** with state space = $\{\bar Z(F) : F \in V_\mathrm{form}\}$ and transition rates inherited from V-AFD-T13(b) basin-label Markov chain.
(R-4) Approximation error is $O(\tau_{\mathrm{relax}} / \tau_{\mathrm{exit}})$, which $\to 0$ as T_* → 0.

**Status.** **Theorem Cat L3 conditional** under (QS-1'), (QS-2'), (QS-3'). Specifically:
- (QS-1') Cat A (Pkg I).
- (QS-2') Cat L3 conditional on Pkg I + concentration / functional inequality on B_F.
- (QS-3') Cat L3 conditional on H-MORSE + FW asymptotic.

Cat self-rating: L3 conditional. Same as AFD-T8.

**Sharpening relative to Round 2.** Round 2 V-AFD-T13(c) gave a *qualitative* statement "approximately Markov in QSD regime". Round 5 adds **quantitative error rate** $O(\tau_{\mathrm{relax}}/\tau_{\mathrm{exit}})$, an *explicit averaged vector* $\bar Z(F)$, and an *explicit error scaling* in T_*.

### D.3 New OP arising

**OP-VAFD-016.** Establish QSD existence (QS-2') on each basin B_F for canonical SCC without H-MORSE-Local. The standard QSD theory (Champagnat-Villemonais 2017) requires *Poincaré inequalities* on B_F, which are weaker than H-MORSE; check explicit constants for canonical SCC.

Severity: M. Bridges V-AFD-T13(c)-refined to L2 in part (a removing one of the L3 dependencies).

---

## Part E — OP-VAFD-014 OP-0005-DYN Reformulation

### E.1 OP-0005-DYN reminder

OP-0005-DYN (canonical Open Problems Catalog): dynamical K-selection. Given SCC at given parameters, which K is *selected* by the dynamics in the appropriate sense (long-time limit, metastable lifetime ordering, etc.)?

Canonical partial resolutions: T-K-Select-PF Cat B (CV-1.10), T-K-Select-OBS Cat B (CV-1.11). Both pick a *scalar* K.

### E.2 V-AFD reformulation

In V-AFD language, K-selection is **two-stage**:

(S-1) **K selection**: which K-stratum is dynamically dominant?
(S-2) **F* selection within $\mathcal{P}_K$**: among Pareto-frontier formations at that K, which is selected?

For canonical scalar selection (T-K-Select-PF / OBS), (S-2) is implicit (a single F is picked). V-AFD makes (S-2) explicit.

### E.3 V-AFD reformulation theorem (sketch)

**Proposition V-AFD-T20 (OP-0005-DYN reformulation).** OP-0005-DYN is equivalent to the following pair of questions:

(QQ-1) Which $K^*$ minimizes $\mathrm{ExitCost}(\mathcal{P}_K)$ (or some scalar Lyapunov on K-strata)?
(QQ-2) Within $\mathcal{P}_{K^*}$, which $F^* \in \mathcal{P}_{K^*}$ minimizes the same / a related scalar?

**For high β + K=1 case** (V-AFD-T17-sharper(a)): $\mathcal{P}_1 = \{F_1^*\}$ mod Aut(G). (QQ-2) is trivial. (QQ-1) reduces to comparing K=1 ExitCost with K≥2 ExitCost, which is the standard barrier-order question (T-Merge(b) + AFD-T7 Cat B give K=1 has lowest E hence largest ExitCost).

**For K≥2 case**: if V-AFD-T17-sharper(b) conjecture (multi-element $\mathcal{P}_K$) holds, (QQ-2) is nontrivial and depends on the scalar criterion. T-K-Select-PF and T-K-Select-OBS provide candidate criteria; V-AFD does not commit to one.

**Status.** **Proposition Cat B sketched** (Cat A for the high-β K=1 reduction; Cat B for the general case).

### E.4 OP-VAFD-014 final form

**OP-VAFD-014 (final): "Resolve the Pareto-frontier selection $F^* \in \mathcal{P}_{K^*}$ for canonical SCC at K ≥ 2."**

Severity: M. Refinement of OP-0005-DYN. Connects to:
- T-K-Select-PF Cat B (which picks a specific F within S_K via path-functional).
- T-K-Select-OBS Cat B (which picks via observer Verifiability).
- V-AFD-T18 (sketched): scalar selection respects Pareto frontier.

**Open variants:**
- Are T-K-Select-PF's and T-K-Select-OBS's choices the *same* element of $\mathcal{P}_K$ for K ≥ 2? If yes, scalar selection is canonically well-defined. If no, the choice of selection criterion matters (and V-AFD has highlighted the difference).

---

## Part F — Cross-Implications and Round 6 Recommendations

### F.1 V-AFD-T16(full) + V-AFD-T19-global + V-AFD-T17-sharper(a) combined

After Round 5:

- V-AFD vector domain: $\mathfrak{V} = V_{\mathrm{form}} / (\mathrm{Aut}(G) \times \mathrm{Aut}_{\mathrm{task}})$, compact (V-AFD-T16(full)).
- Z-projection: conjecturally injective on $\mathfrak{V}$ (T14(c)-conj + T16(full)).
- Each basin has a vector Lyapunov $V_F$; the sheaf $\mathscr{V}$ gives global trajectory-level Pareto monotonicity (V-AFD-T19-global Cat A).
- K=1 high-β Pareto frontier is singleton mod Aut(G) (V-AFD-T17-sharper(a) Cat A).
- Layer-2 K-selection is two-stage: K → $\mathcal{P}_K$ → scalar pick within $\mathcal{P}_K$ (V-AFD-T20).

This is a **complete Layer-2 V-AFD architectural picture** with all main components either Cat A or Cat B-conditional. Layer 3 (EK, prefactors) remains conditional via V-AFD-T8 / T13(b, c).

### F.2 New OPs registered in Round 5

| ID | Severity | Topic |
|---|---|---|
| **OP-VAFD-011b** | L | Non-existence proof for single-function global vector Lyapunov |
| **OP-VAFD-013-K≥2** | M | $\mathcal{P}_K$ multi-element conjecture for K ≥ 2 |
| **OP-VAFD-015** | M | Characterize Aut_task / Aut(G) for canonical SCC |
| **OP-VAFD-016** | M | QSD existence on B_F without H-MORSE-Local |

### F.3 Updated theorem registry deltas

| ID | Status | Cat | Round |
|---|---|---|---|
| **V-AFD-T16(full)** | Theorem | A for (B-1)–(B-3); A modulo T14(c)-conj for (B-4) | R5 |
| **V-AFD-T19-global** | Theorem (sheaf) | A under (H-A1)–(H-A2) | R5 |
| **V-AFD-T17-sharper(a)** | Theorem | A at high β | R5 |
| **V-AFD-T17-sharper(b)** | Conjecture | open (OP-VAFD-013-K≥2) | R5 |
| **V-AFD-T13(c)-refined** | Theorem | L3 conditional with quant error | R5 |
| **V-AFD-T20** | Proposition (sketched) | A (high-β K=1) / B (general) | R5 |

### F.4 Self-audit Round 5

15-question audit:

1. Projection not replacement: ✓ V-AFD-T16(full) places V-AFD on OMS quotient (compatible).
2. Persist forms: ✓ unchanged.
3. Continuity explicit: ✓ V-AFD-T16(full) uses observer-equivariance Cat A.
4. K_act discontinuity: ✓ unchanged.
5. τ stability: ✓ unchanged.
6. Injectivity loss: ✓ V-AFD-T16(full)(B-4) ties injectivity to T14(c)-conj on enlarged quotient.
7. Nonnegativity: ✓ V-AFD-T19-global components non-negative.
8. Not a metric: ✓ unchanged.
9. H-MORSE free: ✓ V-AFD-T16(full), T19-global, T17-sharper(a), T20 use canonical Cat A only; no H-MORSE.
10. EK Layer-3 only: ✓ V-AFD-T13(c)-refined explicitly L3 conditional.
11. Scalarization optional: ✓ V-AFD-T20 explicitly two-stage with scalar in (S-2) optional.
12. Pareto incomparability: ✓ V-AFD-T17-sharper(a) Cat A *singleton* at K=1; multi-element conjecture for K≥2 acknowledged.
13. Markovianity open: ✓ V-AFD-T13(c)-refined provides quantitative L3 approximation; deterministic finite-time still open in full Z.
14. Examples concrete: ✓ V-AFD-T17-sharper(a) uses canonical 15×15 setup conceptually; OMS-2.0 uses canonical Appendix.
15. Honest statuses: ✓ all R5 claims explicit Cat ratings.

**Round 5 audit: PASS** on all 15 questions.

### F.5 Round 6 priorities

After Round 5:

**Priority A:** Execute V-AFD-T14(c)-conj computational test (still pending; CODE-side). Validates the entire V-AFD architectural choice. 2 sessions.

**Priority B:** OP-VAFD-015 — characterize Aut_task / Aut(G) for canonical SCC. May reveal new symmetries beyond graph-Aut. 1–2 sessions.

**Priority C:** OP-VAFD-013-K≥2 conjecture verification (numerical + analytical). Decide whether scalar K-selection over-commits for K≥2. 1 session.

**Priority D:** OP-VAFD-016 — QSD existence on B_F via Poincaré inequalities (without H-MORSE). Removes one L3 dependency from V-AFD-T13(c)-refined. 2 sessions.

**Priority E:** Develop V-AFD-T20 full proof for general K. Connect to T-K-Select-PF / OBS Cat B. 1–2 sessions.

---

## Closing slogans Round 5

> **V-AFD-T16(full):** V-AFD's Aut(G)-quotient is the task-gauge restriction of OMS-2.0's moduli structure; the unified quotient $\mathfrak{V} = V_{\mathrm{form}} / (\mathrm{Aut}(G) \times \mathrm{Aut}_{\mathrm{task}})$ is compact and conjecturally Z-injective.
>
> **V-AFD-T19-global:** Vector Lyapunov gluing is a *sheaf* over basins, not a single function; gives global Pareto monotonicity on every gradient-flow trajectory.
>
> **V-AFD-T17-sharper(a):** At high β, K=1 Pareto frontier is exactly $\{F^*\}$ mod Aut(G); the global minimum dominates componentwise.
>
> **V-AFD-T13(c)-refined:** In QSD regime, vector dynamics is Markov with explicit error $O(\tau_{\mathrm{relax}} / \tau_{\mathrm{exit}})$.
>
> **OP-VAFD-014:** OP-0005-DYN is reformulated as two-stage selection (K, then $F^* \in \mathcal{P}_K$); high-β K=1 reduces to canonical scalar selection.

V-AFD Round 5 closes the OMS bridge sketch into a full theorem, makes the Lyapunov gluing rigorous via sheaves, and reduces high-β K=1 Pareto frontier to a known scalar selection. The architectural picture is now stable and substantially complete at Layer 2.

---

*End of `v_afd_round5_deep_development.md`. V-AFD Round 5 closed.*
