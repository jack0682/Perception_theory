---
id: TI-sharp-v1
type: working/theory
status: open — Cat B-ready sharp form (Session 2026-05-07 evening); supersedes Session V draft for parts (a, b, c, d); not promoted to canonical
created: 2026-05-07
session: W6 D5 evening (sophistication + closure layer)
scope: temporal identity for persistent components — sharp-form Cat B with margin-only hypothesis (post-NQ-5/OP-0011-Step-2 closures)
predecessor: working/MF/temporal_identity_perscomp_transport.md (Session V, 2026-05-06)
related:
  - canonical.md §§3, 7.1, 8.5, 12, 13 (T-Persist-1, T-Persist-K-Sep, E1–E4)
  - theorem_status.md (OP-0011, OP-0012, T-Temporal-Identity)
  - THEORY/logs/daily/2026-05-07/02_exploration.md (exploration + multi-approach)
  - THEORY/logs/daily/2026-05-07/03_development.md (primary development — Lemmas 1–8.2)
  - THEORY/logs/daily/2026-05-07/04_integration_and_new_open.md (integration + NQ list)
  - THEORY/logs/daily/2026-05-07/05_close_NQ5_full.md (NQ-5 closure — Lemma 8)
  - THEORY/logs/daily/2026-05-07/06_close_OP0011_step2.md (OP-0011 Step 2 closure — Lemmas 9–11)
  - THEORY/logs/daily/2026-05-07/07_close_NQ4_robust.md (NQ-4 partial closure — Lemma 12 + Theorem ER)
  - THEORY/logs/daily/2026-05-07/08_NQ6_spectral_gap_advance.md (NQ-6 advancement — Lemma 13 sketch)
  - working/MF/temporal_identity_perscomp_transport.md (Session V predecessor)
  - CODE/experiments/exp83_temporal_identity_transport.py (Session X anchor)
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# Temporal Identity for Persistent Components — Sharp Form (Cat B-ready, post-closure)

**Purpose.** Promotion-ready Cat B working draft of T-Temporal-Identity (parts a, b, c, d) consolidating Session V definitions + 2026-05-07 sharp-form refinement + NQ-T-Identity-5 closure (margin-only) + OP-0011 Step 2 closure (kernel independence, Cat C → Cat B).

**Session.** W6 D5 evening (2026-05-07 extended). State: CV-1.11, 54A/14B/5C/5R = 78 claims. **No canonical promotion in this file.** Promotion target: CV-1.12 (one Cat B addition: T-Temporal-Identity (a, b, c, d) Cat B).

**Header status:**
- Working Cat B candidate, parts (a, b, c, d) all Cat B (post-Lemma 11 closure of part (c)).
- Hypothesis package: (A1)–(A7) + (A7') + (A9) + (DR1)–(DR2) + row+column margin > 0.
- (A8) and (MA1) are *induced*, not postulated (Lemma 8).
- Theorem ER (post-hoc Cat C robustness) covers exp83 PASS at $\varepsilon_\mathrm{OT}=1$ outside certified regime.

---

## §1. Notation block

(Inherits from `THEORY/logs/daily/2026-05-07/03_development.md` §1 — see that file for full table. Key symbols: $u_t, u_s, \mathcal{F}_M(\mathcal{P}), \mathrm{PersComp}, K_t, K_s, \mathrm{Core}, M_{t \to s}, \gamma_{ij}, \varphi, c, \varepsilon_\mathrm{OT}, \sigma_\mathrm{sp}^2, d_\mathrm{inter}^*, \Delta_\varphi^2_\mathrm{inter}, L_g, d_\mathrm{eff}, \rho_\mathrm{deep}, \eta_\mathrm{self}, \eta_\mathrm{cross}^\mathrm{sharp}$.)

The score matrix:
$$S_{ij}^0 = \lambda_m\,\gamma(C_i^t, C_j^s) - \lambda_c\,\sum_{x\in C_i^t,\,y\in C_j^s} c(x,y)\,M(x,y),\qquad \tilde{S}_{ij}^0 = \frac{S_{ij}^0}{\min(m_i^t, m_j^s)}.$$

---

## §2. Assumption package (post-closure, minimal)

**(A1) Finite shared graph** [V]. $G = (\mathcal{P}, E)$ finite, connected, same at $t, s$. (Time-varying topology = OPEN, NQ-T-Identity-3.)

**(A2) Field admissibility** [V]. $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$.

**(A3) PersComp non-empty** [V]. $K_t, K_s \geq 1$. D-ST-3 (canonical).

**(A4) Stable-K** [V]. $K_t = K_s = K$. (Required for parts (b), (d)$_{K=1}$.)

**(A5) Well-separated regime** [S]. $d_\mathrm{inter}^*(t), d_\mathrm{inter}^*(s) \geq d_\mathrm{min}^* \geq 3$. (Canonical T-Persist-K-Sep WS regime.)

**(A6) E1–E4 admissibility of $M_{t \to s}$** [V on the realized plan]. As in canonical §8.5. *Refined E3 (proposed):* "$M$ is the entropic-OT optimum with self-referential cost $c[u_t]$ at $\varepsilon_\mathrm{OT} > 0$" — this trivializes part (c) (`06_close_OP0011_step2.md` Route B). Cat A path uses original E3.

**(A7) T-Persist-1(e) preconditions** [V]. (TC1) $\Delta_\varphi^2(\delta\geq 2) > 0$; (TC2) $\sigma_\mathrm{sp}^2 \geq \mathrm{diam}^2/2$; (TC3) $\gamma_\mathrm{OT}\Delta_\varphi^2 / \varepsilon_\mathrm{OT} > \log n + \mathrm{diam}^2/\sigma_\mathrm{sp}^2$.

**(A7') Sharp-OT regime** [V on $\varepsilon_\mathrm{OT}$]. $\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^* = (\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff})/2$. Numerically $\varepsilon_\mathrm{OT}^* \approx 0.45$ at default parameters.

**(A9) Mass dominance** [V]. $\lambda_m \geq \kappa\,\lambda_c\,\bar c_\mathrm{intra}$ for some $\kappa \geq 10$. Trivially satisfied at default exp83 parameters ($\kappa \approx 370$).

**(DR1)–(DR2) Sinkhorn dual-potential regularity** [V]. (DR1): c-cyclical monotonicity at the support — automatic for entropic-OT optima. (DR2): cost is jointly $L_c$-Lipschitz with $L_c \leq 5.86$ at default.

**Margin condition.** $\Delta_\mathrm{sep}(M) := \min(\Delta_\mathrm{sep}^\mathrm{row}, \Delta_\mathrm{sep}^\mathrm{col}) > 0$.

**No (A8). No (MA1).** Both induced from the above (Lemma 8 of `05_close_NQ5_full.md`).

---

## §3. Lemma summary

| Lemma | Statement | Source | Status |
|-------|-----------|--------|--------|
| 1 | Score matrix well-defined; $\tilde S_{ij}^0 \in [-\lambda_c c_\mathrm{max}, \lambda_m]$ | `03_development.md` §3.1 | Cat A |
| 2 | Diagonal mass lower bound: $\gamma_{i,\pi(i)} \geq (1 - \eta_\mathrm{self}^{\,K})\,m_i^{t,\mathrm{deep}}$ | `03_development.md` §3.2 | Cat B |
| 3-coarse | Off-diagonal mass: $\gamma_{i,j} \leq n\,e^{-(\gamma\Delta^2 - \mathrm{diam}^2/\sigma^2)/\varepsilon_\mathrm{OT}}\,\min(m^t,m^s)$ | `03_development.md` §3.3 | Cat B |
| 3-sharp | Off-diagonal mass: $\gamma_{i,j} \leq e^{-(\gamma\Delta^2 - L_g d_\mathrm{eff})/\varepsilon_\mathrm{OT}}\,\min(m^t,m^s)$ | `03_development.md` §3.3 + §8 | Cat B |
| 4 | Mutual-max ⇔ argmax bijection (finite-matrix algebra) | `03_development.md` §3.4 | Cat A |
| 5 | Row + column margins ⇒ mutual-max conditions | `03_development.md` §3.5 | Cat A |
| 6 | OP-0012-CC composition: stable-K both intervals ⇒ $\pi_{tr} = \pi_{sr} \circ \pi_{ts}$ | `03_development.md` §10 | Cat B |
| 7 | (MA1) + margin > 0 ⇒ (A8) induced | `03_development.md` §11 | Cat B |
| **8** | **(A9) + margin > 0 ⇒ (MA1) + (A8) both induced** | `05_close_NQ5_full.md` §3 | **Cat B (today's closure)** |
| 8.2 | Sinkhorn dual potentials are $L_g \leq L_c$-Lipschitz | `03_development.md` §8.2 | Cat B (Bigot–Cazelles–Papadakis-style; standard) |
| **9** | **Sinkhorn cost-perturbation: $\lVert M - M' \rVert_\mathrm{TV} \leq M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$** | `06_close_OP0011_step2.md` §2.2 | **Cat B (today's closure)** |
| **10** | **Component confinement: $\vert \gamma_M - \gamma_{M'}\vert \leq 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$** | `06_close_OP0011_step2.md` §2.3 | **Cat B (today's closure)** |
| **11** | **Kernel independence: under margin > $\epsilon_\mathrm{kernel}$, $R_{t \to s}[M] = R_{t \to s}[M']$** | `06_close_OP0011_step2.md` §2.4 | **Cat B (today's closure, part (c))** |
| 12 | Variance-corrected dual-potential bound (does not improve $\varepsilon_\mathrm{OT}^*$) | `07_close_NQ4_robust.md` §3 | Cat B |
| 13 | Spectral-form $\eta_\mathrm{cross}^\mathrm{spec} \leq e^{-\mu_\mathrm{joint}(d_\mathrm{inter}^*)^2/(2\varepsilon_\mathrm{OT})}$ | `08_NQ6_spectral_gap_advance.md` §3 | Cat C target Cat A — **Lemma 13 not closed**; advancement only |

---

## §4. Theorem T-Temporal-Identity (Cat B, all four parts)

**Theorem T-Temporal-Identity (Cat B-ready, post-closure form).** *Let $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$ satisfy (A1)–(A3). Let $M_{t \to s}$ satisfy (A6) (E1–E4) with $\varepsilon_\mathrm{OT} \leq \varepsilon_\mathrm{OT}^*$ (A7'). Assume (A9) mass dominance and (DR1)–(DR2) Sinkhorn dual-potential regularity.*

**(a) Existence (Cat B).** *$R_{t \to s}$ is well-defined (Lemma 1) and exhaustively classifies five event types (continuation, split, merge, birth, death) for any choice of finite thresholds.*

**(b) Uniqueness from margin alone (Cat B).** *Additionally assume (A4) stable-K, (A5) well-separated regime, (A7) T-Persist-1(e) preconditions, and:*
$$\Delta_\mathrm{sep}^\mathrm{row} > 0 \;\wedge\; \Delta_\mathrm{sep}^\mathrm{col} > 0.$$

*Then $R_{t \to s}$ is a unique bijection $\pi := j^*$ (Lemmas 4 + 5 + 8). The induced pairing satisfies (A8a)' (mass-positivity, Lemma 8 step 3) and (A8b) (fingerprint-gap positivity, Lemma 8 step 4). The diagonal magnitude (MA1) is automatic with $\theta_\mathrm{diag} \geq 0.83$ at default parameters.*

**(c) Kernel independence (Cat B).** *Under hypotheses of (b) and the strengthened margin condition $\Delta_\mathrm{sep}(M) \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}\lambda_m/\min(m^t,m^s)$ where $\epsilon_\mathrm{kernel} = 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$ is the cost-perturbation kernel-distance: $R_{t \to s}[M] = R_{t \to s}[M']$ for any two E1–E4-admissible plans with $\lVert c - c' \rVert_\infty \leq \delta$ (Lemma 11). In the self-referential cost regime $\delta = 0$ ⇒ $\epsilon_\mathrm{kernel} = 0$ ⇒ trivial uniqueness. Refined E3 (Route B, `06_close_OP0011_step2.md` §3) gives same conclusion definitionally.*

**(d) K=1 reduction (Cat B).** *When $K_t = K_s = 1$, $R_{t \to s}$ is non-empty $\iff$ $\mathsf{persist\_transport}(u_t, u_s, M, \theta_\mathrm{core}) \geq \tau_\mathrm{id}'$ for $\tau_\mathrm{id}' = (\tau_\mathrm{id} + \lambda_c \bar c_\mathrm{intra})/(\lambda_m \rho_\mathrm{deep,core}(1 - \eta_\mathrm{self}))$.*

**Composition (Lemma 6, partial OP-0012-CC closure).** *Under (I_{ts}) + (I_{sr}) — stable-K + margin on both intervals + basin-containment intermediate — bijection composition holds: $R_{t \to r} = R_{s \to r} \circ R_{t \to s}$.*

---

## §5. Closed-form $\Delta_\mathrm{sep}^*$ at default parameters

(See `03_development.md` §9 for the full constant table.)

At default parameters and (A7') sharp regime $\varepsilon_\mathrm{OT} = 0.1$:
$$\Delta_\mathrm{sep}^* \;\geq\; 1.0 \cdot (0.84 \cdot 0.99976 - 1.2 \times 10^{-4}) - 0.005 \cdot 0.54 \;=\; 0.837.$$

exp83 Scenario A measurement: $\Delta_\mathrm{sep} \approx 0.726$ at $\varepsilon_\mathrm{OT} = 1$ (outside (A7') by factor 2.2; covered by Theorem ER post-hoc).

---

## §6. Cat A promotion path (post-closure)

| Sub-step | Task | Estimated sessions | Status |
|----------|------|--------------------|--------|
| S-A1 | Absorb D-ST-3 PersComp into canonical state-space | 0.5 | open |
| S-A2 | exp83 D-ST-3 implementation (replace proxy) | 1 | open |
| S-A3 | External audit of (a) | 0.5 | open |
| S-B1 | Iso-ratio Cat A: $\rho_\mathrm{deep} \geq 0.84$ unconditionally | 1 | open (NQ-T-Identity-2) |
| S-B2 | Lemma 8.2 Sinkhorn-Lipschitz Cat A promotion | 1 | open |
| ~~S-B3~~ | ~~OP-0011 Step 2~~ | ~~1–2~~ | **CLOSED today (Lemma 10)** |
| ~~S-B4~~ | ~~NQ-T-Identity-5 full~~ | ~~1~~ | **CLOSED today (Lemma 8)** |
| S-C1 | Audit Lemma 11 kernel independence | 0.5 | open |
| S-D1 | External audit K=1 | 0.5 | open |
| S-D2 | Numerical anchor at $\varepsilon_\mathrm{OT} \in [0.001, 0.1]$ inside (A7') | 0.5 | open (recommended) |

**Aggregate Cat A timeline:** ~5 sessions (down from 9 pre-closure-session, down from 7 mid-day after sophistication layer). Critical-path bottleneck: **S-B2** (Sinkhorn-Lipschitz Cat A promotion).

**Alternative path:** if NQ-T-Identity-6 (Lemma 13) closes (~2 sessions, 50–60% probability), S-B2 and S-C1 are bypassed, total reduces to ~3 sessions.

---

## §7. Non-overclaim register (consolidated)

The following are NOT claimed:

1. **Does not promote canonical** — this is a working file. Promotion needs P1–P5 (`03_development.md` §6.3).
2. **Does not handle birth/death/split/merge in (b)** — part (b) requires (A4) stable-K + no birth/death.
3. **Does not certify $\varepsilon_\mathrm{OT} > 0.45$ analytically** — covered post-hoc by Theorem ER (Cat C).
4. **Does not fully resolve OP-0011** — Step 2 closed today (Lemma 10), but Step 1 (canonical T-Persist-1(e)) and Step 3 (identity-level) chain holds. Full canonical OP-0011 closure requires audit + canonical-side text update.
5. **Does not solve OP-0012 fully** — only OP-0012-CC partial (Lemma 6); general K-jump composition remains Cat C.
6. **Does not solve OP-0008** — σ-extension deferred to T-σ-Inherit (Session W working file).
7. **Does not solve OP-0021** — $T_*$ canonicalization independent.
8. **Does not handle stochastic transport** — Package II (Langevin) deferred to W9+.
9. **D-ST-3 vs proxy** — exp83 used scipy.ndimage proxy; Cat B uses D-ST-3.
10. **NQ-T-Identity-6 not closed** — only sketched (Lemma 13). Spectral-gap Cat A path remains a future-session target.
11. **Theorem ER is Cat C, not Cat B** — post-hoc verifiable, not a priori predictive.

---

## §8. Promotion-pipeline criteria (P1–P5)

To promote Theorem T-Temporal-Identity to canonical Cat B (CV-1.12):
- **(P1)** Dedicated promotion session with user authorization.
- **(P2)** External audit of Lemmas 1–11 + Theorem 4.2 sharp form + (A1)–(A9) hypothesis package + non-overclaim register.
- **(P3)** Numerical anchor inside (A7') sharp regime: re-run exp83 Scenario A at $\varepsilon_\mathrm{OT} \in \{0.01, 0.05, 0.1, 0.3\}$, confirming $\Delta_\mathrm{sep} \geq 0.83$ (theoretical) with $\leq 10\%$ tolerance.
- **(P4)** Canonical-side text drafted in `04_integration_and_new_open.md` §1.1 (≤80 lines) for `canonical.md §13 Category B` insertion after T-K-Select-OBS.
- **(P5)** `theorem_status.md` row update: T-Temporal-Identity Cat B (parts a, b, c, d) + OP-0011 status PARTIALLY RESOLVED + OP-0012 PARTIALLY RESOLVED.

---

## §9. Backward link

The Session V working file `working/MF/temporal_identity_perscomp_transport.md` remains as the *original* draft. This file (`temporal_identity_sharp_form_2026-05-07.md`) supersedes the Session V draft for promotion purposes, with the closure layer of 2026-05-07 evening session.

The Session V file should be marked "superseded by sharp form 2026-05-07" once user reviews and confirms.

---

*End of `temporal_identity_sharp_form_2026-05-07.md`. Working file ready for promotion-pipeline review.*
