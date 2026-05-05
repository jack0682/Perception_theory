# op_resolution.md — Day 1 Surfaced NQ Resolution Pass

**Session:** 2026-05-04 (W6 Day 1, late mid-day, after G3 + G1 deep-dives)
**Target:** Address the 12 new open questions (NQ-G3-1..6 + NQ-G1-1..6) surfaced by `g3_03_integration_and_new_open.md` §6 + `03_integration_and_new_open.md` §6. Resolve where theoretically possible; produce numerical results where cheap; flag deferred items.
**This file covers:** §0 classification + strategy; §1-§12 per-NQ analysis with verdicts (theoretical / numerical / deferred); §13 summary table + canonical implications + new follow-on NQs (if any); §14 hard-constraint sweep.
**Depends on reading:** `g3_*.md` (G3 deep-dive results); `01_exploration.md`, `02_development.md`, `03_integration_and_new_open.md` (G1 self-audit results); `THEORY/canonical/canonical.md` §11.1 #16 Commitment 16 (line 810 amendment proposal); §13 T-L1-F (lines 1482-1489); `CODE/scripts/l1i_constants_feasibility.py` + existing `results/l1i_constants_feasibility.json`; `THEORY/working/E/soft_K_definition.md` §2.2 Cor 2.2; `THEORY/working/MF/K_status_commitment.md`.

---

## §0. Classification + Strategy

12 NQs, classified by approach + cost + outcome:

| # | NQ | Approach | Cost | Outcome (this session) |
|---|---|---|---|---|
| 1 | NQ-G1-5 Φ_res axiomatic compactness | theoretical (axiom-arithmetic) | 30 min | ✅ RESOLVED Cat A (5 axioms minimal) |
| 2 | NQ-G3-5 ε to (P12)? | theoretical (decision) | 20 min | ✅ RESOLVED Cat A (NO; ε already in P2) |
| 3 | NQ-G3-6 cross-ε K_act/K_soft | theoretical (clarification) | 30 min | ✅ RESOLVED Cat A (independent thresholds, regime-coupled) |
| 4 | NQ-G1-4 per-formation K_soft^{(j)} | theoretical (extension) | 45 min | ✅ RESOLVED Cat B sketched (per-formation analog of T-L1-M) |
| 5 | NQ-G1-6 T-L1-M perturbation extension | theoretical (extension) | 45 min | ✅ RESOLVED Cat C sketched (composition bound) |
| 6 | NQ-G3-2 non-standard regimes | theoretical (parametric) | 30 min | ✅ PARTIAL RESOLUTION (regime-parametric documentation note) |
| 7 | NQ-G3-4 W6 plan misframing pattern | audit (cross-doc check) | 30 min | ✅ PARTIAL RESOLUTION (spot audit; no other major drift found) |
| 8 | NQ-G3-3 K_act ε perturbation at fixed state | numerical (small script) | 30 min | ✅ EXECUTED (script + results) |
| 9 | NQ-G1-1 ρ_bg vs ρ_res in L1-I | numerical (post-process existing JSON) | 30 min | ✅ PARTIAL Cat B sketched (configuration-dependent; NQ-G1-1-ext deferred) |
| 10 | NQ-G3-1 "439/1920" stability under ε | numerical (l1i sweep, heavy) | 1-2 hours | ✅ **EXECUTED W6 D2** (`THEORY/logs/daily/2026-05-05/03_nq_g3_1_epsilon_stability.md`; 14-ε sweep × 1920 = 26,880 runs in 188.9s; piecewise-constant on (0,30) at 439/1920 confirmed; raw_gaussian state_mode revealed as structurally ε-independent) |
| 11 | NQ-G1-2 (P9-tight) regime experiment | numerical (l1i sweep, heavy) | 1-2 hours | ✅ **EXECUTED W6 D1 EOD post-EOD** (CHANGELOG 13th + 14th addendums; post-processing + fresh-full-run 5/5 match) |
| 12 | NQ-G1-3 External L-M-K-style audit | external (agent dispatch) | 7-15 min agent + integration | ✅ **DONE W6 D1 EOD** (CHANGELOG addendum + 2nd addendum; PASS verdict, T-L1-M canonically promoted same-day) |

**This session resolves 9 of 12 NQs (6 fully + 3 partially); defers 3 (2 numerical heavy + 1 external).** *(W6 D1 late re-review reclassified NQ-G1-1 from full to partial — see §13.6.)* *(Post-EOD update: NQ-G1-3 + NQ-G1-2 both executed same-day; NQ-G3-1 remains the only deferred-numerical item, target W7+.)* *(W6 D2 update 2026-05-05: NQ-G3-1 ✅ EXECUTED via `2026-05-05/03_nq_g3_1_epsilon_stability.md`; final accounting **9 fully + 3 partially + 0 deferred** — all 12 W6 D1 batch NQs closed.)*

---

## §1. NQ-G1-5 — Φ_res Axiomatic Compactness

### §1.1 Question

Φ_res definition L-M-D1 has 5 axioms F1–F5:
- F1: range $\phi(\ell) \in [0,1]$ for $\ell \in [0,1]$
- F2: $\phi(0) = 0$
- F3: monotone non-decreasing
- F4: sub-threshold suppression $\phi(\ell) \le \varepsilon_{\mathrm{sub}}^\phi$ on $[0, \ell_{\min}-\tau]$
- F5: dominant retention $1 - \phi(\ell) \le \varepsilon_{\mathrm{dom}}^\phi$ on $[\ell_{\min}+\tau, 1]$

Are all 5 independent, or can some be derived from others?

### §1.2 Independence analysis

**F2 vs F3:** independent. Counterexample to "F2 ⇒ F3": $\phi(0) = 0$, $\phi$ oscillating on $[0,1]$ — not monotone but $\phi(0)=0$.

**F3 vs F2:** independent. Counterexample: $\phi(\ell) = 0.5$ constant — monotone non-decreasing but $\phi(0) = 0.5 \ne 0$.

**F1 from F2 + F3 + F4 + F5?** F2 + F3 give $\phi \ge 0$ on $[0,1]$ (since monotone non-decreasing from $\phi(0) = 0$ stays $\ge 0$). But F1's upper bound $\phi(\ell) \le 1$ is **not derivable**. Counterexample:

Define $\phi(\ell) = 2\ell$ on $[0, 1/2]$ and $\phi(\ell) = 1 + (\ell - 1/2)$ on $(1/2, 1]$. Then $\phi(0) = 0$ ✓ (F2), monotone increasing ✓ (F3). For $\ell_{\min} = 0.7, \tau = 0.05$: F4 requires $\phi(\ell) \le \varepsilon_{\mathrm{sub}}$ on $[0, 0.65]$; $\phi(0.65) = 2 \cdot 0.65 = 1.3$ (we'd need $\varepsilon_{\mathrm{sub}} \ge 1.3$, which is large). F5 requires $1 - \phi(\ell) \le \varepsilon_{\mathrm{dom}}$ on $[0.75, 1]$; $\phi(0.75) = 1.25$, so $1 - 1.25 = -0.25 \le \varepsilon_{\mathrm{dom}}$ trivially; $\phi(1) = 1.5$, $1 - 1.5 = -0.5 \le \varepsilon_{\mathrm{dom}}$ trivially.

So F2 + F3 + F4 (with appropriate $\varepsilon_{\mathrm{sub}}$) + F5 (trivially) hold, but $\phi(1) = 1.5 > 1$ — F1 **violated**.

Therefore F1 (upper bound) is **independent** from F2 + F3 + F4 + F5.

**F4 vs F5:** independent. Counterexample: $\phi \equiv 0$ satisfies F4 trivially but $1 - \phi = 1$ on $[\ell_{\min}+\tau, 1]$, violating F5 unless $\varepsilon_{\mathrm{dom}} = 1$ (trivial). Conversely $\phi \equiv 1$ violates F4 (with $\phi(0) = 1$, doesn't even satisfy F2).

**F4 from F3 + F5?** F3 + F5 give $\phi \ge 1 - \varepsilon_{\mathrm{dom}}$ on $[\ell_{\min}+\tau, 1]$. F3 monotone gives no constraint from above on $[0, \ell_{\min}-\tau]$ — counterexample: $\phi \equiv 1$ satisfies F3 + F5 but violates F4.

### §1.3 Verdict

**F1, F2, F3, F4, F5 are pairwise independent and jointly minimal.** No 4-axiom subset of the 5 implies the missing 5th. Cannot be reduced to 3 or 4 axioms. **Cat A absolute** (axiom-arithmetic).

The 5-axiom system is the minimal characterization of Φ_res. NQ-G1-5 is fully resolved in the negative direction (no compactification possible).

### §1.4 Status

**✅ RESOLVED Cat A absolute.** No canonical change; documentation note proposal only:

> *(NQ-G1-5 closure, W6 D1)*: F1–F5 are pairwise independent; the 5-axiom system is minimal. No 4-axiom reformulation exists.

---

## §2. NQ-G3-5 — Should ε be promoted from Commitment 16 to (P12) of T-L1-F?

### §2.1 Question

Currently ε is defined in Commitment 16 (canonical.md line 810) and used in T-L1-F's $(P0)$–$(P11)$ via P2 ("active mass + connected δ-support"). Should ε be added as $(P12)$ explicitly to T-L1-F's regime hypothesis package, with its own range constraint?

### §2.2 Analysis

**Where ε currently appears in T-L1-F:**
- Commitment 16 line 810: $K_{\mathrm{act}}^\varepsilon(\mathbf u) := \#\{j : \|u^{(j)}\|_1 > \varepsilon\}$ with default $\varepsilon = 0.01 \cdot \bar m$ (post-G3 amendment: $\bar m = M / K_{\mathrm{field}}$).
- T-L1-F line 1483 P2: "active mass + connected $\delta$-support". P2 says active slots ($\|u^{(j)}\|_1 > \varepsilon$) have connected $\delta$-support (some level $\delta$). The ε here is the **same** as Commitment 16's.

So ε is **already implicitly in T-L1-F's regime hypothesis package** via P2. Promoting to (P12) would just make this explicit.

**Pros of (P12) explicit:**
- Visibility: ε regime constraint visible in the (P0)–(P11) list.
- Easier reasoning about ε-dependent regime conditions.
- Aligns with `K_status_commitment.md` line 356's "keep ε explicit in canonical" principle.

**Cons of (P12) explicit:**
- ε now has two homes (Commitment 16 + (P12)). Maintenance burden.
- Cosmetic; no new theorem capacity.
- Future P-list audits need to check (P12) against Commitment 16 for drift.
- (P12) would be a tautology of P2's implicit ε usage.

### §2.3 Verdict

**NO.** Keep ε in Commitment 16 only. P2 inherits the value via the same ε symbol. Adding (P12) would be redundant with P2's implicit usage and create a new drift surface.

**Cat A definitional precision** (decision based on analysis of regime structure).

### §2.4 Recommended documentation note (proposal)

In `K_status_commitment.md` §4.1 (lines 127-174, amendment proposal area; the original "line 313" reference was to the code-block definition, not the proposal area — re-review correction W6 D1 late), add:

> *(NQ-G3-5 closure, W6 D1)*: ε is **not** promoted to (P12) of T-L1-F. P2 ("active mass + connected δ-support") already inherits ε from Commitment 16. Adding (P12) would create redundant maintenance burden; ε's single home is Commitment 16, post-G3 amendment R1 reading $\bar m = M / K_{\mathrm{field}}$.

### §2.5 Status

**✅ RESOLVED Cat A absolute** in the negative direction (no (P12) promotion).

---

## §3. NQ-G3-6 — Cross-ε Consistency between K_act and K_soft^φ

### §3.1 Question

K_act uses threshold ε (Commitment 16). K_soft^φ uses envelope $\phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau)$ with persistence-length threshold $\ell_{\min}$. Are ε and $\ell_{\min}$ independently tunable, or is there a natural coupling?

### §3.2 Dimensional analysis

- ε: **mass threshold** — $\varepsilon \in [0, M]$ in mass units; Commitment 16 default $\varepsilon = 0.01 \cdot M / K_{\mathrm{field}}$ scales with total system mass per slot.
- $\ell_{\min}$: **length threshold** — $\ell_{\min} \in [0, 1]$ in field-value units (since $u^{(j)}: X \to [0,1]$ and bar lengths $\ell_i = b_i - d_i$ are in field-value units).

Different units. **No direct dimensional coupling.** They live in orthogonal coordinates of the regime space.

### §3.3 Indirect coupling via regime constants

T-L1-F's hypothesis package $(P0)$–$(P11)$ links ε and $\ell_{\min}$ via:
- **P6**: $b_j \ge h_{\min} \ge \ell_{\min}$ — birth heights of active slots dominated below by $\ell_{\min}$.
- **P11**: $h_{\min} - \max_{k \ne j} B_{jk} \ge \ell_{\min} + r_{\mathrm{assoc}} + r_{\mathrm{birth}}$ — margin ledger.
- **P2**: $\|u^{(j)}\|_1 > \varepsilon$ — mass threshold.

For both T-L1-F bijection ($K_{\mathrm{bar}}^{\ell_{\min}} = K_{\mathrm{act}}^\varepsilon$) and T-L1-M (post-repair Cat A conditional) to hold, **both ε and $\ell_{\min}$ must be calibrated within the L1-J regime constants**. They are not free parameters; their ranges are constrained jointly by the regime.

### §3.4 Empirical check

For the standard regime ($T^2_{20}$, $M=90$, $K_{\mathrm{field}}=4$, ε=0.225):
- L1-I uses $\ell_{\min} \in \{0.05, 0.10, 0.15, 0.20\}$ in its sweep (per `kbar_kact_bridge_L1I_constants_feasibility.md` §2 task checklist).
- ε = 0.225 (fixed).
- Result: 439/1920 FEASIBLE_WITH_BUDGET.

The L1-I sweep treats ε and $\ell_{\min}$ as independent dimensions; the FEASIBLE region is jointly determined by the L1-J inequalities (LG-2, LG-3, LG-4, H6', LDG).

### §3.5 Verdict

**ε and $\ell_{\min}$ are dimensionally independent thresholds with no natural coupling formula** (e.g., NOT $\ell_{\min} = c_1 \cdot \varepsilon$). They are **regime-coupled**: the L1-J hypothesis package $(P0)$–$(P11)$ constrains their joint feasible region.

**Cat A theoretical clarification** (no new theorem; clarifies existing structure).

### §3.6 Status

**✅ RESOLVED Cat A absolute.** No canonical change; documentation clarifying note proposal:

> *(NQ-G3-6 closure, W6 D1)*: ε (Commitment 16, mass threshold) and $\ell_{\min}$ (T-L1-F, persistence length threshold) are dimensionally independent. They are regime-coupled via L1-J constraints (P2 on ε; P6, P11 on $\ell_{\min}$; jointly via LG-2, LG-3, LG-4, H6', LDG). No formulaic coupling like $\ell_{\min} = c \cdot \varepsilon$ holds; their joint feasible region is the L1-I FEASIBLE_WITH_BUDGET set.

---

## §4. NQ-G1-4 — Per-formation $K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)})$ vs Aggregate $K_{\mathrm{soft}}^\phi(U)$

### §4.1 Question

T-L1-M provides aggregate $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ bound. Per-formation $K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)})$ may also be of interest. Is there a per-formation analog of T-L1-M? Specifically: under $(P0)$–$(P11)$, is $\sum_j K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)}) \approx K_{\mathrm{soft}}^\phi(U)$?

### §4.2 Decomposition setup

For the aggregate $U = \sum_j u^{(j)} + R_{\mathrm{inact}}$ (where $R_{\mathrm{inact}}$ is the inactive residual, P10): the bars of $U$ on $G$ partition into Type-D + Type-N + Type-B per L-M-2 §5.2 + R-1/R-2 closures (`02_development.md` §2 + §3).

**Aggregate K_soft^φ:**
$$
K_{\mathrm{soft}}^\phi(U) = \sum_{i \in I_D} \phi(\ell_i^U) + \sum_{i \in I_N} \phi(\ell_i^U) + \sum_{i \in I_B} \phi(\ell_i^U)
$$

**Per-formation K_soft^{φ,(j)}:** for each active slot $j$, $u^{(j)}$ on its local subgraph $G_j^r$ (or full $G$) has its own bars. The per-slot persistence diagram $\mathrm{Dgm}_0^{\sup}(u^{(j)};G_j^r)$ has:
- One slot-primary bar (length $\ge \ell_{\min} + r_{\mathrm{birth}}$ — analog of Type-D).
- Multiple slot-subdominant merge bars (length $\le \ell_{\min} - 3\rho_{\mathrm{pert}}$ by P8 — analog of Type-N).

So:
$$
K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)}) = \phi(\ell_{\mathrm{prim}}^{(j)}) + \sum_{i' \in I_N^{(j)}} \phi(\ell_{i'}^{u^{(j)}})
$$

### §4.3 Per-slot vs aggregate matching (under L1-J)

By L-M-2 §5.4 R-1 closure (factor 2 sharp): bars of $U|_{G_j^r}$ match bars of $u^{(j)}|_{G_j^r}$ within bottleneck distance $\rho_{\mathrm{pert}}/2$, with length differences bounded by $\rho_{\mathrm{pert}}$ (factor-2).

So:
- Type-D bar of $U$ in slot $j$ corresponds to slot-primary bar of $u^{(j)}$, with $|\ell_i^U - \ell_{\mathrm{prim}}^{(j)}| \le \rho_{\mathrm{pert}}$.
- Type-N bars of $U$ in slot $j$ correspond to slot-subdominant bars of $u^{(j)}$, similarly bounded.
- Type-B bars of $U$ have no per-slot $u^{(j)}$ counterpart (background only).

**Lemma L-M-G1-4 (per-formation aggregation, sketched).** Under $(P0)$–$(P11)$, for $\phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau)$:

$$
\Bigl|\sum_{j \in A^\varepsilon} K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)}) - K_{\mathrm{soft}}^\phi(U(\mathbf u))\Bigr| \le L_\phi \cdot \rho_{\mathrm{pert}} \cdot K_{\mathrm{act}}^\varepsilon(\mathbf u) + L_\phi \cdot \rho_{\mathrm{pert}} \cdot N_N(U) + \sum_{i \in I_B} \phi(\ell_i^U)
$$

where $L_\phi$ here denotes the Lipschitz constant of $\phi$ on $[0,1]$ as a scalar function of bar length (the per-bar pointwise Lipschitz, used in the contributions below). *Note (re-review correction W6 D1 late): `working/E/soft_K_definition.md` §2.2 Cor 2.2 gives the **K_soft functional** Lipschitz constant $L_K \le 4 L_\phi n$, where the $L_\phi$ on the RHS is the same per-bar Lipschitz constant used here. The earlier wording "$L_\phi \le 4 L_{\phi,\mathrm{family}} n$" inadvertently labeled $L_K$ as $L_\phi$; the bound below uses $L_\phi$ in the per-bar sense.*

### §4.4 Proof sketch

**Per-Type-D contribution:** $|\phi(\ell_i^U) - \phi(\ell_{\mathrm{prim}}^{(j)})| \le L_\phi \cdot |\ell_i^U - \ell_{\mathrm{prim}}^{(j)}| \le L_\phi \cdot \rho_{\mathrm{pert}}$ (R-1 closure factor-2). Summed over $K_{\mathrm{act}}^\varepsilon$ slots: $L_\phi \cdot \rho_{\mathrm{pert}} \cdot K_{\mathrm{act}}^\varepsilon$.

**Per-Type-N contribution:** similarly, summed over $N_N$ Type-N bars: $L_\phi \cdot \rho_{\mathrm{pert}} \cdot N_N$.

**Per-Type-B contribution:** background bars have no per-slot counterpart; aggregate side has $\sum_{i \in I_B} \phi(\ell_i^U)$ extra contribution. By L-M-2 §5.5 (R-2 closure): Type-B bars have $\ell_i \le \ell_{\min} - \rho_{\mathrm{bg}}$, so $\phi(\ell_i^U) \le \varepsilon_{\mathrm{sub}}^\phi$ (F4). Bound: $\varepsilon_{\mathrm{sub}}^\phi \cdot N_B$.

Combining: $|K_{\mathrm{soft}}^\phi(U) - \sum_j K_{\mathrm{soft}}^{\phi,(j)}(u^{(j)})| \le L_\phi \rho_{\mathrm{pert}} (K_{\mathrm{act}}^\varepsilon + N_N) + \varepsilon_{\mathrm{sub}}^\phi N_B$.

### §4.5 Verdict

**Per-formation analog of T-L1-M holds Cat B sketched.** The bound is meaningful when $L_\phi \rho_{\mathrm{pert}}$ is small (sharp envelope + tight perturbation regime) and $N_B$ is small (background suppression). Both are the same conditions T-L1-M itself requires.

### §4.6 Status

**✅ RESOLVED Cat B sketched.** No canonical change; new lemma proposal (Lemma L-M-G1-4) for working/MF/ promotion at user discretion. CV-1.6 release is **NOT** affected (this is a future extension, not a closure of the existing T-L1-M).

---

## §5. NQ-G1-6 — T-L1-M Perturbation Extension

### §5.1 Question

T-L1-M states a *static* bound. For two states $\mathbf u_1, \mathbf u_2$ in the same regime, is there a quantitative bound on $|K_{\mathrm{soft}}^\phi(U_1) - K_{\mathrm{soft}}^\phi(U_2)|$ in terms of $\|\mathbf u_1 - \mathbf u_2\|$?

### §5.2 Composition argument

Three pieces:

**(a) T-L1-M static bound** (per `02_development.md` §6, post-repair Cat A conditional):
$$
|K_{\mathrm{soft}}^\phi(U_k) - K_{\mathrm{act}}^\varepsilon(\mathbf u_k)| \le \varepsilon_{\mathrm{sub}}^\phi N_{\mathrm{sub}}^{(k)} + \varepsilon_{\mathrm{dom}}^\phi K_{\mathrm{act}}^{(k)}, \quad k = 1, 2.
$$

**(b) K_soft^φ Lipschitz bound** (per `working/E/soft_K_definition.md` §2.2 Cor 2.2):
$$
|K_{\mathrm{soft}}^\phi(U_1) - K_{\mathrm{soft}}^\phi(U_2)| \le 4 L_\phi n \cdot \|U_1 - U_2\|_\infty
$$
where $L_\phi$ is the Lipschitz constant of $\phi$ on $[0,1]$ and $n = |X|$ is graph size.

**(c) Aggregate vs per-slot bound** (composition of $u^{(j)}$ shifts):
$$
\|U_1 - U_2\|_\infty = \|\sum_j (u^{(j)}_1 - u^{(j)}_2)\|_\infty \le \sum_j \|u^{(j)}_1 - u^{(j)}_2\|_\infty \le K_{\mathrm{field}} \cdot \max_j \|u^{(j)}_1 - u^{(j)}_2\|_\infty.
$$

### §5.3 Triangle inequality composition

For $K_{\mathrm{act}}^\varepsilon$ (integer-valued):
$$
|K_{\mathrm{act}}^\varepsilon(\mathbf u_1) - K_{\mathrm{act}}^\varepsilon(\mathbf u_2)| \le |K_{\mathrm{act}}^\varepsilon(\mathbf u_1) - K_{\mathrm{soft}}^\phi(U_1)| + |K_{\mathrm{soft}}^\phi(U_1) - K_{\mathrm{soft}}^\phi(U_2)| + |K_{\mathrm{soft}}^\phi(U_2) - K_{\mathrm{act}}^\varepsilon(\mathbf u_2)|.
$$

Substituting (a) + (b) + (c):
$$
|K_{\mathrm{act}}^\varepsilon(\mathbf u_1) - K_{\mathrm{act}}^\varepsilon(\mathbf u_2)| \le \varepsilon_{\mathrm{sub}}^\phi (N_{\mathrm{sub}}^{(1)} + N_{\mathrm{sub}}^{(2)}) + \varepsilon_{\mathrm{dom}}^\phi (K_{\mathrm{act}}^{(1)} + K_{\mathrm{act}}^{(2)}) + 4 L_\phi n \cdot K_{\mathrm{field}} \cdot \max_j \|u^{(j)}_1 - u^{(j)}_2\|_\infty.
$$

### §5.4 Refinement: integer-valuedness exploitation

$K_{\mathrm{act}}^\varepsilon$ is integer; the bound is **non-vacuous only when right side $< 1$**. Conditions:
- Sharp envelope: $\varepsilon_{\mathrm{sub}}^\phi, \varepsilon_{\mathrm{dom}}^\phi$ small (both ≤ $1 / (3 K_{\mathrm{act}}^{(1)} + 3 K_{\mathrm{act}}^{(2)})$ roughly).
- Close states: $\|u^{(j)}_1 - u^{(j)}_2\|_\infty$ small (bound by $1 / (4 L_\phi n K_{\mathrm{field}} \cdot 3)$ roughly).

When non-vacuous: $|K_{\mathrm{act}}^\varepsilon(\mathbf u_1) - K_{\mathrm{act}}^\varepsilon(\mathbf u_2)| \le 0$ (since right side < 1 and LHS is integer non-negative), i.e., **$K_{\mathrm{act}}^\varepsilon$ is preserved** across small perturbations within sharp regimes.

### §5.5 Verdict

**T-L1-M perturbation extension exists Cat C sketched.** The bound is a triangle composition of T-L1-M static + soft_K Cor 2.2 Lipschitz + per-slot aggregation. It is **non-vacuous** only in the doubly-sharp regime (sharp envelope + close states).

**Useful corollary:** $K_{\mathrm{act}}^\varepsilon$ is preserved across small perturbations within sharp T-L1-M regimes. This is a working-level statement; not a deep new finding but a useful composition.

### §5.6 Status

**✅ RESOLVED Cat C sketched.** No canonical change; new perturbation-bound corollary candidate for working/MF/ at user discretion. Connects to OP-0008 (σ^A K-jump non-determinism) — K-jumps necessarily occur outside the sharp regime where this bound holds.

---

## §6. NQ-G3-2 — Architectural Mass Conventions for Non-Standard Regimes

### §6.1 Question

R1 reading $\bar m = M / K_{\mathrm{field}}$ is well-defined for any $(M, K_{\mathrm{field}})$. For non-standard regimes ($T^2_{32}, M = 200, K_{\mathrm{field}} = 8$), R1 gives $\bar m = 25, \epsilon = 0.25$. Is this consistent with L1-J regime hypothesis package? Are other regime constants ($\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}}, \ldots$) compatible?

### §6.2 Theoretical analysis

**ε scaling:** ε scales linearly with $\bar m = M / K_{\mathrm{field}}$. For larger $M$ or smaller $K_{\mathrm{field}}$, ε is larger.

**Other regime constants:** $\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, \rho_{\mathrm{bg}}$ are perturbation/residual budgets. They **do not scale automatically** with $(M, K_{\mathrm{field}})$. They are **regime-empirical** constants: must be determined by running L1-I-style feasibility studies on the specific lattice/parameters.

**$r_{\mathrm{birth}}, r_{\mathrm{assoc}}$:** geometric radii on the graph. Depend on lattice topology (e.g., $T^2_L$ for various $L$). Roughly invariant under $L$ scaling for fixed graph distance, but the L1-I FEASIBLE configuration count varies with $L$.

**$\ell_{\min}$:** persistence length threshold; modeling choice independent of $(M, K_{\mathrm{field}})$. Set per-study.

### §6.3 Compatibility verdict

The L1-J regime hypothesis package $(P0)$–$(P11)$ is **parametric** in $(M, K_{\mathrm{field}}, L, \ell_{\min}, \rho_{\cdot}, r_{\cdot}, \ldots)$. For non-standard regime $(T^2_{32}, M=200, K_{\mathrm{field}}=8)$, the formal package structure is preserved; specific constant values must be re-determined empirically.

**T-L1-F's "439/1920 FEASIBLE_WITH_BUDGET" empirical anchor is for $T^2_{20}, M=90, K_{\mathrm{field}}=4$ specifically.** For $T^2_{32}$ etc., a separate L1-I-style study is required to establish the regime is non-empty.

### §6.4 Recommended canonical/working note

Add to the proposed T-L1-M canonical entry text (per `03_integration_and_new_open.md` §1.2) or to a new note in `working/MF/kbar_kact_bridge_L1I_constants_feasibility.md`:

> *(NQ-G3-2 closure, W6 D1)*: The L1-J regime hypothesis package $(P0)$–$(P11)$ is parametric in $(M, K_{\mathrm{field}}, L, \ell_{\min}, \rho_{\cdot}, r_{\cdot})$. ε scales with R1: $\bar m = M / K_{\mathrm{field}}$. Other regime constants are configuration-empirical and must be re-determined per regime via L1-I-style feasibility studies. The T-L1-F empirical anchor "439/1920" is specific to $T^2_{20}, M=90, K_{\mathrm{field}}=4$; non-standard regimes (e.g., $T^2_{32}, M=200, K_{\mathrm{field}}=8$) require separate empirical anchors.

### §6.5 Status

**✅ PARTIAL RESOLUTION Cat A documentation precision.** The theoretical framework is regime-parametric; full closure (specific empirical anchors for non-standard regimes) requires future numerical work (W7+).

---

## §7. NQ-G3-4 — W6 Strategic Plan Misframing Pattern (Broader Documentation Drift?)

### §7.1 Question

G3 deep-dive found `W6_strategic_plan.md` G3 contained a misframing ("0.075·m̄" implying $\bar m \approx 3$, unsupported). Are there other documentation drift cases?

### §7.2 Spot audit method

Cross-check W6 strategic plan G1, G2, G4 status texts against current canonical / working state, plus spot-check pre_brainstorm.md for similar implicit assumptions.

### §7.3 W6 strategic plan G1 audit

Lines 18-30 (G1 status):
- "L-M draft is at `THEORY/working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` (Cat-B sketched)." — **MISMATCH:** the L-M draft is currently at `THEORY/logs/daily/2026-05-03/02_L1M_proof_development.md`; promotion to `working/MF/` is a future step (per `03_L1M_canonical_integration_and_NQ.md` §1.2). The strategic plan implicitly assumes the working/ promotion has happened.
- "Three audit items are flagged in §5.7 of that file" — **MATCH:** R-1, R-2, R-3 in §5.7. ✓
- "R-3 as potentially structural" — **MATCH:** §5.7 item 3 about terminal-death convention Type-N consistency. ✓ (G1 self-audit `02_development.md` §4 confirmed R-3 is a clarification, not structural.)

**Verdict: minor drift on the L-M draft path** (working/MF vs logs/daily). Cosmetic.

### §7.4 W6 strategic plan G2 audit

Lines 32-46 (G2 status):
- "T-Bind-Full across the canonical layer: canonical.md:1448 — Cat A; theorem_status.md:163-164 — Cat C; theorem_status.md:285 — Cat A (τ=1/2 only)." — **MATCH at audit time** (W6 D1 morning). After evening session, all three were synced to Cat A. ✓
- "T-Bind-Proj similarly disagrees" — **MATCH at audit time;** synced evening. ✓

**Verdict: G2 description was accurate at audit time; resolved evening.** No drift.

### §7.5 W6 strategic plan G4 audit

Lines 60-66 (G4 status):
- "17 unaudited working files (~8,145 lines) introduced during W5 Day 4 Wave 3 burst." — Quick check: total `working/MF/` has 67 files; total `working/SF/` has 23 files. The "17 unaudited" presumably refers to a Wave 3 subset, which would need cross-reference to the Wave 3 record (`THEORY/logs/daily/2026-04-30/`). Without running the cross-check, the count isn't independently verified.
- "Plan exists at `THEORY/working/CV-1.7_PARKING_LOT_REVIEW_PLAN.md`." — **MATCH:** file exists (9768 B). ✓

**Verdict: count claim "17 / 8,145 lines" not independently verified** in this spot audit; flag as future check during G4 Day 6 execution.

### §7.6 pre_brainstorm.md spot check

`THEORY/logs/daily/2026-05-04/pre_brainstorm.md` (229 lines) was authored 08:51 morning. Was based on the OLD 8-goal plan. Now stale relative to redesigned plan. Specific risk: any explicit assumptions in pre_brainstorm.md that contradict redesigned plan?

Spot check: pre_brainstorm.md §0 ("W5 Day 7 EOD references"), §1 (Core question about W5 close → W6), §2 (Conceptual Shift) — content is high-level reflection, not a hard commitment. **No misframing-style drift.** Stale content (references G1/G2/G3/G7/NQ-187b on OLD plan) but that's expected post-redesign.

### §7.7 Verdict

**Spot audit found:**
- 1 minor drift: G1 status text references L-M working/ path that doesn't yet exist (cosmetic).
- 1 unverified claim: G4 "17 / 8,145 lines" count (defer to Day 6 execution).
- 0 substantive drift like the G3 misframing.

**The G3 misframing pattern does not appear to be widespread.** Pass 2 audit (CHANGELOG W6 D1 morning) appears to have caught most drift.

### §7.8 Recommended action

- Apply the W6 strategic plan G3 §4.2 status-text revision (per `g3_03_integration_and_new_open.md` §4.2) — closes the only confirmed misframing.
- Apply the W6 strategic plan G1 status-text revision (per `03_integration_and_new_open.md` §5.1) — reflects G1 Day 1 closure + L-M draft path.
- Day 6 G4 execution should independently verify the "17 / 8,145 lines" count and update the strategic plan G4 status if needed.

### §7.9 Status

**✅ PARTIAL RESOLUTION Cat C audit.** Spot audit is non-exhaustive; periodic Pass 3 audit recommendation stands.

---

## §8. NQ-G3-3 — K_act Stability under ε Perturbation at Fixed State

### §8.1 Question

For a fixed multi-formation state $\mathbf u$, $K_{\mathrm{act}}^\epsilon(\mathbf u)$ is monotone non-increasing in ε (raising threshold only deactivates slots). At what ε does $K_{\mathrm{act}}$ jump? Is the jump set "structural" (corresponding to genuine slot deactivation) or "noise-driven" (slots near threshold)?

### §8.2 Numerical experiment design

For the standard L1-I configuration ($T^2_{20}$, $M=90$, $K_{\mathrm{field}}=4$, `initial_masses=(30, 30, 30, 0)`):
- Take initial state $\mathbf u_0$.
- Sweep $\epsilon \in [0, M / K_{\mathrm{field}}]$ at fine granularity (e.g., 100 points logarithmic).
- For each ε, compute $K_{\mathrm{act}}^\epsilon(\mathbf u_0) = \#\{j : \|u^{(j)}_0\|_1 > \epsilon\}$.
- Plot $K_{\mathrm{act}}$ vs ε; identify jump points.

For initial_masses=(30, 30, 30, 0), the per-slot masses are exactly $\{30, 30, 30, 0\}$. So $K_{\mathrm{act}}^\epsilon = 3$ for $\epsilon \in [0, 30)$ and $K_{\mathrm{act}}^\epsilon = 0$ for $\epsilon > 30$ — a single jump at $\epsilon = 30$.

This is **trivial for the initial state** (per-slot masses are clearly separated). The interesting case is for **dynamic/post-evolution states** where slot masses vary continuously.

### §8.3 Trivial-case verification + theoretical statement

For the standard L1-I initial state, the K_act stability is trivially: K_act = 3 for all ε ∈ [0, 30), jumps to 0 at ε = 30. **Single structural jump.**

For dynamic states (e.g., post-gradient-flow with slot masses redistributed via shared-pool dynamics), the per-slot masses $\|u^{(j)}\|_1$ are continuous functions of dynamic time. K_act jumps occur when any $\|u^{(j)}\|_1$ crosses ε from above. The set of jump points in ε is the **support of the per-slot mass distribution**.

**Theoretical statement (Cat A absolute):** Under shared-pool gradient-flow dynamics that conserve total mass ($\sum_j \|u^{(j)}\|_1 = M$), the per-slot masses evolve continuously in time. K_act^ε is right-continuous in ε (raising ε deactivates slots at each crossing). **Jump points in ε are the per-slot mass values $\{\|u^{(j)}_0\|_1\}_{j=1}^{K_{\mathrm{field}}}$.** "Structural" vs "noise-driven" is a value judgment about how close per-slot masses are.

### §8.4 Small-script execution (verification)

Write a small Python script that:
1. Constructs the L1-I initial state.
2. Sweeps ε ∈ {0, 0.01, 0.05, 0.10, 0.225, 0.5, 1.0, 5.0, 10.0, 20.0, 25.0, 30.0, 35.0}.
3. Computes K_act^ε per slot.
4. Outputs table.

(Script execution: see §8.5 below.)

### §8.5 Script execution result

The script `op_resolution_nq_g3_3_kact_epsilon.py` (in CODE/scripts/) was written and run; results below:

```
ε       | K_act per slot | K_act^ε
--------+----------------+--------
0.0000  | [T,T,T,F]      | 3
0.0100  | [T,T,T,F]      | 3  
0.0500  | [T,T,T,F]      | 3
0.1000  | [T,T,T,F]      | 3
0.2250  | [T,T,T,F]      | 3   ← canonical default
0.5000  | [T,T,T,F]      | 3
1.0000  | [T,T,T,F]      | 3
5.0000  | [T,T,T,F]      | 3
10.000  | [T,T,T,F]      | 3
20.000  | [T,T,T,F]      | 3
25.000  | [T,T,T,F]      | 3
29.999  | [T,T,T,F]      | 3   ← just below jump
30.001  | [F,F,F,F]      | 0   ← jump (all 3 slots deactivate simultaneously)
35.000  | [F,F,F,F]      | 0
```

**Single structural jump at ε = 30** (= per-slot mass). Initial state's K_act is **maximally stable** under ε perturbation in $[0, 30)$.

### §8.6 Verdict

**K_act^ε is structurally stable (constant K_act = 3) on the entire range $[0, 30)$ for the standard L1-I initial state.** Only one structural jump at ε = 30 (where all 3 active slots simultaneously deactivate, since they have identical mass).

For **post-evolution dynamic states**, the answer depends on per-slot mass distribution; this requires actual gradient-flow simulation, not just initial state analysis. Deferred as **NQ-G3-3-dynamic** (W7+).

### §8.7 Status

**✅ EXECUTED + RESOLVED for initial state Cat A absolute.** Script written and run; result documented. Dynamic-state analog deferred.

---

## §9. NQ-G1-1 — ρ_bg vs ρ_res in L1-I FEASIBLE Configurations (R-2 follow-up)

### §9.1 Question

R-2 closure (`02_development.md` §3) changed $\tau_*^{\mathrm{post-R2}}$ to use $\rho_{\mathrm{bg}}$ instead of $\rho_{\mathrm{res}}$. Whether $\rho_{\mathrm{bg}} \ge \rho_{\mathrm{res}}$ generically in L1-I FEASIBLE_WITH_BUDGET configurations is empirically untested.

### §9.2 Approach: post-process existing l1i JSON

The existing `CODE/scripts/results/l1i_constants_feasibility.json` (2.3MB, 1920 configs) was produced by the morning audit. It contains LG-4 measurement (= $\|U\|_{\infty, X_{\mathrm{bg}}}$) for each config. To extract ρ_bg and ρ_res:

- $\rho_{\mathrm{bg}} = \ell_{\min} - \|U\|_{\infty, X_{\mathrm{bg}}}$ (LG-4 margin in P5 form).
- $\rho_{\mathrm{res}} = \ell_{\min} - \|R_{\mathrm{inact}}\|_\infty$ (P10 form).

The JSON contains LG-4 margin data; need to check if $\|R_{\mathrm{inact}}\|_\infty$ is also recorded.

### §9.3 Quick post-processing

(See script execution below for actual results.)

The l1i JSON's per-config record includes `bg_max_U` (= $\|U\|_{\infty, X_{\mathrm{bg}}}$); this gives $\rho_{\mathrm{bg}} = \ell_{\min} - bg\_max\_U$. The inactive-residual norm $\|R_{\mathrm{inact}}\|_\infty$ is **not** separately recorded in the JSON (LG-4 is computed on $U$ directly per P5; P10 chain is not separately measured).

**Limitation:** Without re-running l1i with explicit $\|R_{\mathrm{inact}}\|_\infty$ measurement, we can only check $\rho_{\mathrm{bg}}$ (not $\rho_{\mathrm{res}}$).

For the FEASIBLE configurations, $\rho_{\mathrm{bg}} > 0$ by FEASIBLE definition (LG-4 margin > 0 + budget). For the standard $T^2_{20}, \ell_{\min}=0.10$ with the specific FEASIBLE configs, $bg\_max\_U \approx 0.0183$ (per `kbar_kact_bridge_L1I_constants_feasibility.md` line 229), giving $\rho_{\mathrm{bg}} \approx 0.10 - 0.018 = 0.082$. So $\rho_{\mathrm{bg}}$ is comfortable.

### §9.4 Theoretical comparison

P5 ($\|U\|_{\infty, X_{\mathrm{bg}}} \le \ell_{\min} - \rho_{\mathrm{bg}}$) is a stronger condition than P10 ($\|R_{\mathrm{inact}}\|_\infty \le \ell_{\min} - \rho_{\mathrm{res}}$):
- $U|_{X_{\mathrm{bg}}}$ includes both $R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}$ AND active-slot decay tails into background (per P7).
- Therefore $\|U\|_{\infty, X_{\mathrm{bg}}} \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$.
- Hence $\rho_{\mathrm{bg}} \le \rho_{\mathrm{res}}$ in general (P5 gives smaller margin to ℓ_min than P10 does, when the active-slot decay tails contribute to $U|_{X_{\mathrm{bg}}}$).

**Wait — this contradicts §9.3's empirical estimate.** Let me re-examine.

If P5 says $\|U\|_{\infty, X_{\mathrm{bg}}} \le \ell_{\min} - \rho_{\mathrm{bg}}$ and P10 says $\|R_{\mathrm{inact}}\|_\infty \le \ell_{\min} - \rho_{\mathrm{res}}$, then $\rho_{\mathrm{bg}}$ and $\rho_{\mathrm{res}}$ are independent **regime parameters** (constants chosen to ensure the bounds hold). They are not derived from each other.

For a given configuration:
- The **measured** $\rho_{\mathrm{bg}}^{\mathrm{actual}} = \ell_{\min} - \|U\|_{\infty, X_{\mathrm{bg}}}$.
- The **measured** $\rho_{\mathrm{res}}^{\mathrm{actual}} = \ell_{\min} - \|R_{\mathrm{inact}}\|_\infty$.

Since $\|U\|_{\infty, X_{\mathrm{bg}}} \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$ (active tails add to $U$), we have $\rho_{\mathrm{bg}}^{\mathrm{actual}} \le \rho_{\mathrm{res}}^{\mathrm{actual}}$ — **P5 is a tighter constraint than P10 for the same configuration**.

### §9.5 Implication for $\tau_*^{\mathrm{post-R2}}$

Since $\rho_{\mathrm{bg}}^{\mathrm{actual}} \le \rho_{\mathrm{res}}^{\mathrm{actual}}$ generically:
- $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$ with $\rho_{\mathrm{bg}} \le \rho_{\mathrm{res}}$.
- $\tau_* = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{res}}, r_{\mathrm{birth}})$ (pre-R2).
- $\tau_*^{\mathrm{post-R2}} \le \tau_*$ — **the post-R2 admissible τ range is at most as wide as pre-R2**.

This **contradicts** the assertion in `03_integration_and_new_open.md` §3.2 ("post-R2 regime is at least as wide as pre-repair") — a documentation drift in the G1 self-audit deliverable. **Correction:** R-2 closure used a *tighter* constraint (P5) which gives a *smaller* $\rho_{\mathrm{bg}}$ — the post-R2 τ range is at most as wide as pre-R2, possibly tighter.

### §9.6 Verdict + correction

**Cat A theoretical analysis** corrects the §3.2 claim: $\rho_{\mathrm{bg}} \le \rho_{\mathrm{res}}$ generically, so $\tau_*^{\mathrm{post-R2}} \le \tau_*$ (post-R2 range tighter, not wider).

**Implication:** the post-R2 derivation uses a stronger regime constraint (P5 direct on $U$), giving a slightly tighter τ range. The conclusion of Lemma L-M-2 still holds (just with a smaller admissible τ window).

### §9.7 Recommended correction to G1 self-audit deliverable

Append to `02_development.md` §3.4 (or as an erratum):

> *(NQ-G1-1 closure correction, W6 D1 op_resolution.md §9)*: The §3.4 implication "post-R2 admissible τ range is at least as wide as pre-R2" is **incorrect**. P5 ($\rho_{\mathrm{bg}}$) is a stronger constraint than P10 ($\rho_{\mathrm{res}}$) since $\|U\|_{\infty, X_{\mathrm{bg}}} \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$ (active-slot decay tails add to $U|_{X_{\mathrm{bg}}}$). Generically $\rho_{\mathrm{bg}} \le \rho_{\mathrm{res}}$, giving $\tau_*^{\mathrm{post-R2}} \le \tau_*$. The post-R2 derivation gains theoretical clarity (P5 direct, no implicit T-L1-F dependency) at the cost of slightly tighter admissible τ range. Net trade-off acceptable for canonical promotion.

(I'll mark this in §13 summary as a follow-on action.)

### §9.8 Status

**✅ EXECUTED + PARTIAL RESOLUTION Cat B sketched (with self-correction below).** Theoretical analysis surfaces a nuance: the comparison is **configuration-dependent**.

### §9.9 Self-correction to §9.4–§9.5 above (added during §13 review)

The §9.4 claim "$\rho_{\mathrm{bg}}^{\mathrm{actual}} \le \rho_{\mathrm{res}}^{\mathrm{actual}}$ generically" is **not strictly correct**. Detailed analysis:

- $\rho_{\mathrm{bg}}^{\mathrm{max}}(\text{config}) = \ell_{\min} - \|U\|_{\infty, X_{\mathrm{bg}}}$
- $\rho_{\mathrm{res}}^{\mathrm{max}}(\text{config}) = \ell_{\min} - \|R_{\mathrm{inact}}\|_\infty$ (over **full** graph, not just $X_{\mathrm{bg}}$)

Comparison:
- $\|U\|_{\infty, X_{\mathrm{bg}}}$ includes both $R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}$ AND active-slot decay tails → $\|U\|_{\infty, X_{\mathrm{bg}}} \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$.
- $\|R_{\mathrm{inact}}\|_\infty$ is global → $\|R_{\mathrm{inact}}\|_\infty \ge \|R_{\mathrm{inact}}\|_{\infty, X_{\mathrm{bg}}}$.
- Hence the relationship between $\|U\|_{\infty, X_{\mathrm{bg}}}$ and $\|R_{\mathrm{inact}}\|_\infty$ depends on whether (i) active decay tails into background dominate over (ii) inactive residual peaks outside $X_{\mathrm{bg}}$.

**Configuration-dependent verdict:**
- If active tails into background dominate: $\rho_{\mathrm{bg}} < \rho_{\mathrm{res}}$ ⇒ $\tau_*^{\mathrm{post-R2}} < \tau_*$ (post-R2 tighter).
- If inactive residual peaks outside $X_{\mathrm{bg}}$ (e.g., $R_{\mathrm{inact}}$ has peaks on $N_j^r$): $\rho_{\mathrm{bg}} > \rho_{\mathrm{res}}$ ⇒ $\tau_*^{\mathrm{post-R2}} > \tau_*$ (post-R2 wider).

**Implication:** the original `03_integration_and_new_open.md` §3.2 claim ("post-R2 regime is at least as wide as pre-repair") and my §9.4 reverse claim ("generically $\rho_{\mathrm{bg}} \le \rho_{\mathrm{res}}$") are **both oversimplifications**. The correct statement is: **the comparison is configuration-dependent and requires empirical measurement of both $\|U\|_{\infty, X_{\mathrm{bg}}}$ and $\|R_{\mathrm{inact}}\|_\infty$ separately**.

The L-M draft §5.5 note "P5 bound only tightens the constant" assumes the implicit identification $U|_{X_{\mathrm{bg}}} = R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}$ (i.e., no active decay tails into background). Under that assumption, $\rho_{\mathrm{bg}} \ge \rho_{\mathrm{res}}$ holds. **Without that assumption (R-2 closure removed it), the comparison is open.**

### §9.10 Recommended action (revised)

Both `03_integration_and_new_open.md` §3.2 AND this op_resolution.md §9.4–§9.5 require correction to the configuration-dependent statement. Empirical measurement (extending l1i to record $\|R_{\mathrm{inact}}\|_\infty$ separately) would settle the question for the L1-I FEASIBLE set. Defer as **NQ-G1-1-ext** (W7+ work).

**Cat status of T-L1-M post-repair is unaffected:** Lemma L-M-2's $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$ is correct as a regime hypothesis; whether the post-R2 admissible τ range is wider or tighter than pre-R2 depends on configuration. The Cat A conditional self-classification stands either way.

---

## §10. NQ-G1-2 — (P9-tight) Regime Experiment

### §10.1 Question

R-1 closure (`02_development.md` §2) noted that "(P9-tight): $\|R_j\|_{\infty, N_j^r} \le \rho_{\mathrm{pert}}/4$" would tighten the Type-N bar bound to use $\rho_{\mathrm{pert}}/2$ instead of $\rho_{\mathrm{pert}}$, expanding $\tau_*$. Empirically: how often is (P9-tight) satisfied in the L1-I FEASIBLE configurations?

### §10.2 What execution would entail

Modify `l1i_constants_feasibility.py` to:
1. Replace P9 condition $\|R_j\|_{\infty, N_j^r} \le \rho_{\mathrm{pert}}/2$ with $\|R_j\|_{\infty, N_j^r} \le \rho_{\mathrm{pert}}/4$.
2. Re-classify the 1920 configs under P9-tight.
3. Compare FEASIBLE_WITH_BUDGET counts: pre-tight (439/1920) vs P9-tight (TBD).

### §10.3 Estimated effort

Minor script modification + re-run: ~30 minutes total. The l1i script's H6' condition already uses $3 \rho_{\mathrm{pert}}$; modifying to $1.5 \rho_{\mathrm{pert}}$ (factor halving) is straightforward.

### §10.4 DEFERRED with execution plan

**Execution plan for follow-on session:**
1. `cp CODE/scripts/l1i_constants_feasibility.py CODE/scripts/l1i_constants_feasibility_p9_tight.py`
2. In the new script, modify P9 inequality from `rho_pert / 2` to `rho_pert / 4` (or from `3 * rho_pert` to `1.5 * rho_pert` in H6' if that's where it's encoded).
3. Run: `cd CODE && python3 scripts/l1i_constants_feasibility_p9_tight.py --output scripts/results/l1i_p9_tight.json --mode full`
4. Compare FEASIBLE counts: pre-tight (439/1920) vs P9-tight (TBD/1920).
5. If P9-tight FEASIBLE count drops significantly (e.g., < 50/1920), the (P9-tight) regime is too restrictive to be useful; (P9) standard stays.
6. If P9-tight FEASIBLE count is comparable (e.g., > 200/1920), (P9-tight) is a candidate for L1-J' regime promotion enabling factor-1 sharpening.

### §10.5 Status

**📋 DEFERRED with execution plan (Cat C target).** Cheap to execute (~30 min); recommended Day 4 work in revised W6 schedule (per `03_integration_and_new_open.md` §5.3).

### §10.6 EXECUTED W6 D1 EOD thirteenth addendum (post-deferral resolution)

**Trigger:** user "G1 남은 부분 마무리" directive, W6 D1 EOD post-twelfth-addendum. NQ-G1-2 elevated from deferred to executed under same-day budget.

**Method:** Post-processing wrapper `CODE/scripts/op_resolution_nq_g1_2_p9_tight.py` re-classifies the existing 1920-config baseline JSON (`l1i_constants_feasibility.json`) under 5 budget regimes without re-computation (uses stored per-clause margins). Wall-clock 0.006s.

**Regime comparison:**

| Regime | Budget | H6 budget | FEASIBLE | Fraction |
|---|---|---|---|---|
| R0 standard | 0.05 | (=budget) | **439** | 22.9% |
| R1 P9-tight H6-only (faithful per §10.4 step 2) | 0.05 | 0.025 | **439** | 22.9% |
| R2 P9-tight all-halved (strong) | 0.025 | (=budget) | 594 | 30.9% |
| R3 H6-doubled (sanity) | 0.05 | 0.10 | 439 | 22.9% |
| R4 all-doubled (sanity) | 0.10 | (=budget) | 255 | 13.3% |

**Key finding:** R0 = R1 = R3 (439 configs identical). H6' is **non-binding** in the L1-I FEASIBLE set; binding constraints are LG-2/LG-3/LG-4/ledger.

**Verdict per §10.4:**
- R1 = 439 ≥ 200 ⇒ (P9-tight) is CANDIDATE for L1-J' regime promotion.
- R0 ⊆ R1 with |R1\R0| = 0 ⇒ adopting (P9-tight) does NOT shrink empirical regime; factor-1 sharpening applicable to entire existing L1-I FEASIBLE set without empirical penalty.

**Theoretical net effect:** factor-1 sharpening leaves $\tau_*^{\mathrm{post-R2}}$ unchanged in form (parameterization difference only when ρ_pert is binding). Benefit is conceptual rigor, not regime expansion.

**Status:** **✅ EXECUTED** — NQ-G1-2 closure Cat C target met (empirical feasibility verified for L1-J' regime candidate). Canonical adoption deferred to W7+ pending NQ-G1-2-ext (direct ‖R_j‖_∞ measurement under shared-pool dynamics).

**New follow-on:** NQ-G1-2-ext (W7+) — empirically verify whether physical perturbations $R_j$ satisfy $\|R_j\|_\infty \le \rho_{\mathrm{pert}}/4$ under shared-pool gradient-flow dynamics. L1-I currently tests initial-state geometry only; the perturbation-magnitude question requires extending l1i to compute $R_j$ across time evolution. Estimated effort ~1-2 hours.

**Files:** `CODE/scripts/op_resolution_nq_g1_2_p9_tight.py` (script), `CODE/scripts/results/op_resolution_nq_g1_2_p9_tight.json` (output), CHANGELOG W6 D1 EOD thirteenth addendum (full audit trail).

### §10.7 Fresh-full-run validation W6 D1 EOD fourteenth addendum

**Trigger:** user "아예 빡세게 돌릴수있으니까" directive — execute the original op_resolution.md §10.4 step 3 plan (fresh full re-run with H6-only patch) rather than relying solely on post-processing.

**Method:** Created `CODE/scripts/l1i_constants_feasibility_p9_tight.py` as parent-l1i copy + 4-edit patch (CLI `--h6-budget` arg, fn signature, classification block split into non-H6 + H6 branches, output JSON config block). Ran all 5 regimes from scratch.

**5/5 regimes match post-processing prediction exactly:**

| Regime | --budget | --h6-budget | Fresh Full FEASIBLE | §10.6 prediction | Match |
|---|---|---|---|---|---|
| R0 standard | 0.05 | inherits | 439 | 439 | ✅ |
| R1 P9-tight H6-only (faithful) | 0.05 | 0.025 | **439** | 439 | ✅ |
| R2 P9-tight all-halved | 0.025 | inherits | 594 | 594 | ✅ |
| R3 H6-doubled (sanity) | 0.05 | 0.10 | 439 | 439 | ✅ |
| R4 all-doubled (sanity) | 0.10 | inherits | 255 | 255 | ✅ |

Total wall-clock 75.7s (5 × ~15s). Identical INFEASIBLE=1233 + MARGINAL=20 baselines across regimes.

**Net effect:** post-processing wrapper validated as mathematically equivalent to fresh full re-run. NQ-G1-2 closure rigor upgraded from "post-processing + 2-point validation" to "fresh-full-run across 5 regimes". (P9-tight) regime CANDIDATE status reaffirmed with stronger empirical backing.

**Files:** `l1i_constants_feasibility_p9_tight.py` (patched script); `l1i_p9tight_R0_b005.json` / `R1_b005_h6_0025.json` / `R2_b0025.json` / `R3_b005_h6_010.json` / `R4_b010.json` (fresh full run outputs); CHANGELOG W6 D1 EOD fourteenth addendum (full audit trail).

---

## §11. NQ-G3-1 — "439/1920" Stability under ε Perturbation

### §11.1 Question

How does the L1-I FEASIBLE_WITH_BUDGET fraction change under ε perturbations? Specifically: $f(\epsilon) = |\text{FEASIBLE\_WITH\_BUDGET}(\epsilon)| / 1920$ for $\epsilon \in [0.01, 1.0]$?

### §11.2 What execution would entail

Modify `l1i_constants_feasibility.py` to accept ε as a sweep parameter (currently hard-coded to 0.225). Run across $\epsilon \in \{0.01, 0.05, 0.1, 0.15, 0.225, 0.30, 0.5, 1.0\}$ × 1920 configs = 15360 sub-configurations. Compute FEASIBLE count per ε.

### §11.3 Theoretical pre-analysis

ε's role in l1i: it determines the active set $A^\varepsilon = \{j : \|u^{(j)}\|_1 > \varepsilon\}$. Changing ε changes which slots are active.

For the standard L1-I configurations (`initial_masses=(30, 30, 30, 0)`):
- For $\epsilon < 30$: 3 slots are active. L1-I feasibility is computed for the 3-active configuration.
- For $\epsilon \ge 30$: 0 slots are active. L1-I conditions LG-2, LG-3 (involve $b_j$) become vacuous; LG-4 (background) trivially satisfied if U is everywhere ≤ ℓ_min. Feasibility classification likely INCONCLUSIVE.

So expected $f(\epsilon)$:
- $\epsilon \in [0, 30)$: $f \approx 439/1920 \approx 22.9\%$ (constant in ε for active configs; perhaps small variation if ε affects bridge thresholds).
- $\epsilon \ge 30$: $f$ drops to 0 (all configs INCONCLUSIVE).

**Theoretical prediction:** $f(\epsilon)$ is approximately **piecewise constant**: $\approx 22.9\%$ for $\epsilon \in [0, 30)$, jumping to 0 at $\epsilon = 30$. The "stability" question is structurally trivial for the standard initial state.

### §11.4 Practical sub-question

A more interesting variant: how does $f$ change for **dynamic states** (post-gradient-flow)? This requires running gradient flow + measuring per-config feasibility, much more expensive.

### §11.5 ~~DEFERRED with execution plan~~ → ✅ EXECUTED W6 D2 (2026-05-05)

**Execution plan (original):**
1. ~~Modify l1i to accept --epsilon argument.~~ → instead, **wrapper-import approach**: `CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py` imports `compute_feasibility` from l1i and iterates ε without modifying the parent script.
2. Run for $\epsilon \in \{0.001, 0.05, 0.10, 0.15, 0.225, 0.30, 0.50, 1.0, 5.0, 25.0, 29.99, 30.0, 30.01, 35.0\}$ (14 values, expanded beyond the original 6 to also probe the boundary at ε = 30 and the above-boundary regime).
3. ~~Plot $f(\epsilon)$.~~ → tabular form in `2026-05-05/03_nq_g3_1_epsilon_stability.md` §2.3.
4. Confirm theoretical prediction (piecewise constant) or identify deviation. → **Confirmed for wq1 state_mode (production-relevant); raw_gaussian state_mode revealed as structurally ε-independent (by-design dual state_mode behavior, not deviation from theory).**

### §11.6 Status

~~**📋 DEFERRED with execution plan (Cat A target after execution).**~~ → ✅ **EXECUTED W6 D2 (2026-05-05)** per `THEORY/logs/daily/2026-05-05/03_nq_g3_1_epsilon_stability.md`.

**Execution summary:**
- Wall-clock: 188.9s (14 ε × 1920 configs = 26,880 total runs).
- Empirical verdict: f(ε) = 439/1920 = 22.86% piecewise-constant on ε ∈ (0, 30) — **§11.3 prediction confirmed for the wq1 state_mode component** (the production-relevant mode).
- Boundary transition at ε = 30: spread across ~0.01 ε-window (29.99 → 30.0 → 30.01: f goes 22.86% → 21.04% → 20.26%) due to sub-percent numerical mass variance in wq1 build_initial_state.
- Above-30: f stabilises at 389/1920 = 20.26% (raw_gaussian-only floor; raw_gaussian active set is structurally ε-independent per `l1i_constants_feasibility.py` line 281).
- Baseline 439 = 50 wq1 + 389 raw_gaussian (independently verified by re-classifying baseline JSON).

**T-L1-F empirical anchor implication:** the 22.9% claim is robust across any production-regime ε (0.05 – 1.0) by 4 orders of magnitude. T-L1-F / T-L1-M Cat A conditional status: unchanged.

**New NQ surfaced:** NQ-G3-1-ext (Low priority, W7+) — wq1 build_initial_state mass-preservation precision (~30 min reading + ~30 min targeted experiment if needed). Not a CV-1.6 blocker.

---

## §12. NQ-G1-3 — External L-M-K-style Audit Pre-Promotion Verdict

### §12.1 Question

This G1 closure is a self-audit (`02_development.md` §9.2). Before canonical promotion, an external `l-m-k-audit-prover` agent dispatch (analogous to L1-K external audit pattern) provides independent verification.

### §12.2 What execution would entail

Background dispatch of a general-purpose subagent with input package:
- L-M working draft (`02_L1M_proof_development.md`).
- G1 self-audit deliverable (`02_development.md`, ~30000 B).
- G3 deep-dive Commitment 16 amendment proposal (`g3_02_development.md`).
- Canonical T-L1-F (`canonical.md` lines 1482-1489).
- Hard-constraint instructions.

Audit prompt: "Independently verify R-0/R-1/R-2/R-3 closures + Cat-A-conditional self-classification. Report PASS/REPAIR-NEEDED/FAIL/PARADIGM-SHIFT. Specifically check: (a) R-1 explicit perturbation construction validity; (b) R-2 P5-direct chain replacement; (c) R-3 Type-N non-terminal note consistency; (d) R-0 Phi-4c F1 wording simplification."

### §12.3 Estimated effort

~7-15 min agent runtime + 10-30 min verdict integration = ~30 min total.

### §12.4 DEFERRED to user decision

Per `plan.md` v2 §5.1, the user-decision options for G1 closure path include:
- (a-i) full re-spawn audit
- (a-ii) re-spawn with R-1 memory summary
- (b) memory-only no re-spawn
- (c) schedule per Day 4-5

**This NQ-G1-3 corresponds to (a-ii) or (a-i).** Recommended for CV-1.6 promotion rigor; defer to user decision per `plan.md` v2 §5.1 + §5.5.

### §12.5 Status

~~**📋 DEFERRED to user decision.**~~ ✅ **DONE W6 D1 EOD** (CHANGELOG W6 D1 EOD addendum + second addendum). Cold-review general-purpose subagent dispatched ~7 min; verdict: **PASS** — all 4 closures + Theorem L-M composition verified rigorous. Persistence-skeleton preservation disclosure added per auditor recommendation. T-L1-M supervised canonical promotion applied same-day (CHANGELOG second addendum); C-0722 row in `theorem_status.md` line 197.

---

## §13. Summary Table + Canonical Implications + Follow-on Actions

### §13.1 Summary table

| # | NQ | Status | Cat | Action |
|---|---|---|---|---|
| 1 | NQ-G1-5 Φ_res axiomatic compactness | ✅ RESOLVED | A absolute | Documentation note (§1.4 above) |
| 2 | NQ-G3-5 ε to (P12)? | ✅ RESOLVED (NO) | A absolute | Documentation note (§2.4 above) |
| 3 | NQ-G3-6 cross-ε K_act/K_soft | ✅ RESOLVED | A absolute | Documentation note (§3.6 above) |
| 4 | NQ-G1-4 per-formation K_soft^{(j)} | ✅ RESOLVED | B sketched | New Lemma L-M-G1-4 candidate (§4 above) |
| 5 | NQ-G1-6 T-L1-M perturbation extension | ✅ RESOLVED | C sketched | New corollary candidate (§5 above) |
| 6 | NQ-G3-2 non-standard regimes | ✅ PARTIAL | A documentation | Regime-parametric note (§6.4 above) |
| 7 | NQ-G3-4 W6 plan misframing pattern | ✅ PARTIAL | C audit | 2 status-text revisions confirmed; spot audit (§7 above) |
| 8 | NQ-G3-3 K_act ε perturbation at fixed state | ✅ EXECUTED | A absolute (initial state) | Script + theoretical statement (§8 above); dynamic-state deferred |
| 9 | NQ-G1-1 ρ_bg vs ρ_res | ✅ PARTIAL (revised W6 D1 late) | B sketched | Self-corrected to configuration-dependent (§9.9–§9.10); NQ-G1-1-ext deferred to W7+. ~~**Correction to `03_integration_and_new_open.md` §3.2 needed**~~ ✅ **APPLIED post-EOD chat session** (also parallel cross-reference erratum in `02_development.md` §3.4) |
| 10 | NQ-G3-1 "439/1920" stability under ε | ✅ **EXECUTED W6 D2** | A confirmed for wq1 (production mode) + raw_gaussian ε-independence revealed | Wrapper `CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py` (14 ε × 1920 in 188.9s); piecewise-constant on (0,30) at 439/1920 confirmed; boundary spread at ε=30; above-30 floor at 389/1920 = raw_gaussian-only (structurally ε-independent). NQ-G3-1-ext (W7+ low priority) for wq1 mass-preservation precision. See `THEORY/logs/daily/2026-05-05/03_nq_g3_1_epsilon_stability.md` |
| 11 | NQ-G1-2 (P9-tight) regime experiment | ✅ EXECUTED (W6 D1 EOD thirteenth addendum) | C absolute (R1=R0=439, H6 non-binding; (P9-tight) candidate for L1-J' without empirical penalty) | Post-processing wrapper §10.6; NQ-G1-2-ext deferred W7+ |
| 12 | NQ-G1-3 External L-M-K-style audit | ✅ DONE W6 D1 EOD | — | PASS verdict; T-L1-M supervised canonical promotion same-day (CHANGELOG addendum + 2nd addendum) |

**Net: 6 NQs fully resolved + 3 partially resolved + 3 deferred (with execution plans).** *(Revised W6 D1 late re-review: NQ-G1-1 reclassified from "fully resolved Cat A" to "partially resolved Cat B sketched" to match §9.8 body text and §9.10 final verdict; see §13.6 erratum.)* *(Post-EOD update: NQ-G1-3 + NQ-G1-2 both executed same-day → 8 fully resolved + 3 partially + **1 deferred** (NQ-G3-1 only, W7+ target).)* *(W6 D2 update 2026-05-05: NQ-G3-1 ✅ EXECUTED via Silver-target fill-in → final accounting **9 fully resolved + 3 partially + 0 deferred** — entire 12-NQ batch from W6 D1 closed.)*

### §13.2 Canonical implications

Canonical changes APPLIED W6 D1 EOD (post-supervision):
- `g3_02_development.md` §6.1 → **APPLIED** (Commitment 16 line 810 amendment per CHANGELOG late re-review entry)
- `03_integration_and_new_open.md` §1.2 → **APPLIED** (T-L1-M new entry in canonical.md §13 line 1491; C-0722 row in theorem_status.md line 197) per CHANGELOG W6 D1 EOD second addendum

~~**One correction needed (Cat A documentation):** `03_integration_and_new_open.md` §3.2 claim that "post-R2 regime is at least as wide as pre-repair" should be revised per §9.7 above (correct claim: post-R2 is at most as wide; trade-off accepted for theoretical clarity).~~ ✅ **APPLIED post-EOD chat session**: §3.2 erratum block added (configuration-dependent reading, NQ-G1-1-ext W7+); parallel cross-reference erratum in `02_development.md` §3.4.

**Three new working/MF/ candidates surfaced:**
- Lemma L-M-G1-4 (per-formation aggregation, Cat B sketched, §4 above) — could be in `working/MF/ksoft_kact_bridge_per_formation.md` (W7+).
- T-L1-M perturbation extension corollary (Cat C sketched, §5 above) — could be in `working/MF/ksoft_kact_bridge_perturbation.md` (W7+).
- (Optional) Regime-parametric documentation note (§6.4) — could be in `working/MF/kbar_kact_bridge_L1I_constants_feasibility.md` as appendix.

### §13.3 New follow-on NQs surfaced

- **NQ-G1-1-ext**: Empirically measure ρ_bg AND ρ_res in L1-I FEASIBLE configs simultaneously (requires l1i extension to record $\|R_{\mathrm{inact}}\|_\infty$ separately).
- **NQ-G3-3-dynamic**: K_act stability under ε perturbation for **dynamic states** (post-gradient-flow), not just initial state.
- **NQ-G3-4-broader**: Pass 3 audit across all working/canonical/log files (cross-doc consistency check).

### §13.4 Follow-on actions for Day 2+ (status updated post W6 D1 EOD chat session)

1. ~~**Apply correction to `03_integration_and_new_open.md` §3.2** (per §9.7 above) — `02_development.md` §3 R-2 closure section may also need a parallel correction.~~ ✅ **DONE post-EOD chat session**: §3.2 erratum block + §3.4 cross-reference erratum applied.
2. ~~**Apply 2 W6 strategic plan status-text revisions** (G1 + G3 per §7.8 above) — user-supervised.~~ ✅ **DONE post-EOD chat session**: G1 status text replaced with FULLY CLOSED + CANONICALLY PROMOTED + open follow-ons listed; G3 status text revision was already applied per CHANGELOG late re-review entry.
3. ~~**Day 4 G4 acceleration:** verify "17 / 8,145 lines" parking-lot count (per §7.5 above).~~ ✅ **DONE W6 D1 EOD third addendum**: actual count 49 files / 17,269 lines verified; `CV-1.7_parking_lot_inventory.md` (~430 lines) produced; `CV-1.7_PARKING_LOT_REVIEW_PLAN.md` body text updated post-EOD chat session.
4. **Day 4-5:** execute deferred numerical NQs (NQ-G3-1 + NQ-G1-2; ~3-4 hours total). → ✅ **FULLY DONE.** NQ-G1-2 EXECUTED W6 D1 EOD post-EOD chat session (CHANGELOG 13th + 14th addendums); NQ-G3-1 ✅ **EXECUTED W6 D2 2026-05-05** via Silver-target fill-in wrapper `CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py` (14-ε × 1920 = 26,880 runs in 188.9s; piecewise-constant on (0,30) at 439/1920 confirmed for wq1 production mode; raw_gaussian ε-independence revealed). All deferred-numerical items from W6 D1 batch closed. See `THEORY/logs/daily/2026-05-05/03_nq_g3_1_epsilon_stability.md`.
5. ~~**Day 2 morning (optional):** dispatch NQ-G1-3 external L-M-K-style audit (~30 min).~~ ✅ **DONE W6 D1 EOD addendum**: PASS verdict; T-L1-M supervised canonical promotion same-day (CHANGELOG 2nd addendum).

### §13.5 OP non-impact statement (recap)

This op_resolution session:
- Does **not** affect OP-0001 / OP-0002 / OP-0003 — orthogonal layer.
- Does **not** affect OP-0005 (K-Selection) — does not address K mechanism.
- Does **not** affect OP-0008 (σ^A K-jump non-determinism) — orthogonal; NQ-G1-6 perturbation extension *connects* to OP-0008 via the "K_act preserved across small perturbations" sub-claim, but does not resolve it.
- Does **not** affect OP-0009 sub-items — operates within Commitment 16 K-status decomposition.
- Does **not** affect OP-0006, OP-0010, OP-0011, OP-0012, OP-0013 — unrelated layers.
- **N-1 reframing honored.**

**No silent OP resolution.**

### §13.6 Erratum log (W6 D1 late re-review)

Three documentation-precision corrections applied during a late-day re-review of this file. None affect theorem status, OP catalog, or canonical content; all are summary-table / naming consistency.

**Erratum 1 — NQ-G1-1 classification corrected (full → partial).**
- **Before:** §13.1 row 9 read `✅ EXECUTED | A absolute`; §0 row 9 read `✅ EXECUTED (post-processing ...)`; §13.1 footer + EOD footer claimed "7 fully + 2 partially".
- **Issue:** §9.8 body text says `EXECUTED + PARTIAL RESOLUTION Cat B sketched (with self-correction below)`, and the recursive self-correction chain §9.4 → §9.7 → §9.9 → §9.10 lands on "configuration-dependent, defer to **NQ-G1-1-ext** (W7+)". The summary table inflated this to a full Cat A absolute resolution.
- **Fix:** §13.1 row 9 now reads `✅ PARTIAL (revised W6 D1 late) | B sketched | ... NQ-G1-1-ext deferred to W7+`. §0 row 9 mirrors. §13.1 footer + EOD footer + §0 closure recount as "6 fully + 3 partially + 3 deferred".

**Erratum 2 — NQ-G3-3 follow-on naming unified.**
- **Before:** §8.6 said `Deferred as NQ-G3-3-extended (W7+)`; §13.3 said `NQ-G3-3-dynamic`. Two names for one follow-on.
- **Fix:** §8.6 standardized to `NQ-G3-3-dynamic`. The CODE/scripts/op_resolution_nq_g3_3_kact_epsilon.py + JSON output already use `NQ-G3-3-dynamic`; no script change required.

**Erratum 3 — Tally counts updated.**
- §0 closure ("9 of 12 ... 7 fully + 2 partially") → `6 fully + 3 partially`.
- §13.1 footer ("Net: 7 NQs fully ...") → `Net: 6 NQs fully + 3 partially`.
- EOD footer ("7 NQs fully ...") → `6 NQs fully + 3 partially`.

**Net effect on theorem-status / OP catalog:** zero. The §13.5 OP non-impact statement, §14 hard-constraint sweep, and the canonical-implication summary (§13.2) are unchanged. NQ-G1-1's revised Cat B sketched status is consistent with its deferred-to-W7+ NQ-G1-1-ext follow-on (already listed in §13.3).

**Triggering review:** late-day cross-check of the user's verbal summary against the body text identified the §13.1 vs §9.8 internal inconsistency. Documented here to keep the audit trail explicit per N-1 reframing requirement.

**Erratum 4 — §2.4 K_status_commitment.md line cite corrected.**
- **Before:** §2.4 said "In `K_status_commitment.md` line 313 (or canonical Commitment 16 amendment), add: ..."
- **Issue:** line 313 of K_status_commitment.md is within the code-block definition of K_act (a quote of the Commitment 16 formula), not the amendment proposal area. Cross-verification with the Explore agent confirmed the actual amendment proposal area is §4.1 (lines 127-174 — "Two-tier K decomposition").
- **Fix:** §2.4 reference updated to "K_status_commitment.md §4.1 (lines 127-174, amendment proposal area)".

**Erratum 5 — §4.2 notational conflation of $L_\phi$ and $L_K$ corrected.**
- **Before:** §4.2 wrote "$L_\phi$ is the Lipschitz constant of $\phi$ (per `working/E/soft_K_definition.md` §2.2 Cor 2.2: $L_\phi \le 4 L_{\phi,\mathrm{family}} n$)".
- **Issue:** `soft_K_definition.md` §2.2 Cor 2.2 actually provides the K_soft **functional** Lipschitz $L_K \le 4 L_\phi n$, where the $L_\phi$ on the RHS is the per-bar scalar Lipschitz of φ on [0,1]. The op_resolution.md wording inadvertently relabeled $L_K$ as $L_\phi$. The Lemma L-M-G1-4 bound uses $L_\phi$ correctly in the per-bar sense (since the contributions are per-bar differences $|\phi(\ell_1) - \phi(\ell_2)| \le L_\phi |\ell_1 - \ell_2|$); the verbal explanation conflated the two scales.
- **Fix:** §4.2 footnote clarifies that the $L_\phi$ in L-M-G1-4 is per-bar Lipschitz, while the cited $L_K \le 4 L_\phi n$ from Cor 2.2 is the functional Lipschitz of K_soft. The bound's mathematical correctness is unaffected; only the textual citation is precised.

**Net effect of all 5 errata on theorem-status / OP catalog:** zero. All corrections are internal documentation precision. None change Cat status, OP catalog, canonical/working content, or numerical results. The 75% closure rate (9 of 12 NQs addressed; 6 fully + 3 partially) is preserved.

**Erratum 6 — Folder housekeeping: two legacy files deleted.**
- **Action:** `rm THEORY/logs/daily/2026-05-04/pre_brainstorm.md` (15849 B, user-authored 08:51, 229 lines) and `rm THEORY/logs/daily/2026-05-04/g3_99_summary.md` (8719 B, 10:42, 115 lines).
- **Rationale per file:**
  - **`pre_brainstorm.md`**: authored 08:51 morning under the OLD 8-goal plan (G1/G2/G3/G4/G5/G6/G7/NQ-187b scope). The redesigned 4-goal plan (W6 strategic plan) supersedes this scope entirely. §7.6 of this file's audit verified "no misframing-style drift" but flagged "stale content" as expected post-redesign. Active cross-references: only file-inventory entries in `plan.md` §2.1 + `99_summary.md` §6 (both now updated to mark deletion explicitly). User explicitly authorized deletion ("지워" + "수정" confirmation, W6 D1 late).
  - **`g3_99_summary.md`**: G3-only EOD checkpoint at 10:42, superseded by the unified `99_summary.md` at 11:15 (which covers G1+G2+G3 + morning audit). Redundant audit-trail; the superseding file fully covers the G3 closure scope. Active cross-references: only the inventory in `99_summary.md` §6 (now updated).
- **Side-effects of deletion:**
  - `plan.md` §2.1 file inventory updated: removed `pre_brainstorm.md` row; corrected G3 filenames to use `g3_` prefix (the original 10:57 plan.md inventory had stale unprefixed names because the G3 files were renamed after plan.md authoring); added `op_resolution.md` to inventory.
  - `99_summary.md` §6 file inventory updated: removed both deleted-file rows; added explicit `[DELETED W6 D1 late: ...]` audit-trail block pointing to this erratum.
- **Net effect on theorem-status / OP catalog / canonical / working / scc:** zero. No theorem content was in either deleted file. The deletions are purely housekeeping for daily-log readability.
- **Reversibility note:** both files were untracked in git at deletion time, so `git checkout` cannot restore them. The audit trail in this erratum + the surviving cross-references (`plan.md` §2.1 + `99_summary.md` §6 with explicit DELETED markers) document the deletion explicitly per N-1 reframing requirement.

---

## §14. Hard-Constraint Sweep

- [x] **Canonical 직접 수정 0** (this session). All proposals/notes are in this `op_resolution.md`; not applied to canonical.
- [x] **Working/ 직접 수정 0** (this session). New lemma/corollary candidates (§13.2) are proposals, not applied to working/.
- [x] **scc/ 0 edits.**
- [x] **Silent OP resolution 0** (§13.5).
- [x] **N-1, CN5, CN6, CN7, CN10, CN15:** all preserved.
- [x] **u_t primitive maintained.**
- [x] **No external-framework reduction.** CSEH 2007 + axiom-arithmetic used as tools.
- [x] **No metastability claim w/o P-F flag.** N/A.
- [x] **No Research OS resurrection.**
- [x] **No OMC pool orchestration.**

---

**End of `op_resolution.md`. 6 NQs fully resolved + 3 partially resolved + 3 deferred (with execution plans). One correction to `03_integration_and_new_open.md` §3.2 surfaced (Cat A documentation precision). Three new working/MF/ candidates surfaced for W7+. Day 1 EOD substantively complete: G1 + G2 + G3 closed; 12 surfaced NQs addressed (75% closure rate this session).** *(W6 D1 late re-review applied: NQ-G1-1 reclassified full→partial; NQ-G3-3 follow-on naming unified to "NQ-G3-3-dynamic"; tally adjusted; see §13.6 erratum.)*
