---
id: SCC-CT-CH-IX
type: canonical/forbidden-claims
chapter: IX
version: SCC-CT v0.1
sealed: 2026-05-14
---

> [!nav] Linked: [[MOC_SCC_CT_v0.1]] · [[THEORY_INDEX]]


# IX. Forbidden Claims

## §1. Purpose

This chapter is **not** about claims that are false. It is about claims that — even if eventually true — must not be asserted at the current state of SCC-CT v0.1, because:

1. They were historically *prematurely* asserted and *retracted* (Cat R historical).
2. They constitute *overclaim wording* that, even when paraphrasing a real result, misrepresents what has actually been proved.
3. They are *definitional tautologies* dressed as theorems (V-AFD / R-2 failure mode).
4. They cross the *ontological commitment* boundary established in `01_ontology.md` (e.g., re-introducing the object as primitive).

This chapter exists to **prevent regression**. Without explicit forbidden-claim registration, the theory drifts into rhetoric that the prior canonical state did not support, and audit cycles repeat themselves.

## §2. Cat R historical retractions (5 entries)

These are the 5 formally Cat R entries counted in the 97-claim total (`04_theorem_registry.md §5`).

### §2.1 Original A1 (weak extensivity)

**Claim:** $\mathrm{Cl}_t(u)(x) \geq u(x)$ for all $u \in [0,1]^n$ pointwise.

**Why retracted:** Conflicts with A3 contraction. Sigmoid closure cannot simultaneously satisfy A1 (requires $a_{\mathrm{cl}} \geq 5.49$) and A3 ($a_{\mathrm{cl}} < 4$).

**Replacement:** **A1′** Conditional Extensivity — $\mathrm{Cl}_t(u)(x) \geq u(x)$ holds only when $u(x) \leq c^*$ for some self-support threshold. Above $c^*$, closure acts as relaxation (self-regulation).

**Forbidden wording:**
- ❌ "Closure is monotonically extensive."
- ❌ "$\mathrm{Cl}(u) \geq u$ unconditional."
- ✓ Correct: "A1′ Conditional Extensivity holds below $c^*$; above $c^*$, closure self-regulates."

### §2.2 Theorem 3.3 ($\bar r_0 = O(n^{-1/d})$ for general $\tau$)

**Claim:** Effective formation radius scales as $\bar r_0 \sim n^{-1/d}$ for general threshold $\tau$.

**Why retracted:** Numerically falsified. For $\tau \neq 1/2$, $\bar r_0$ remains $O(1)$ (not vanishing with $n$). Honest recount 2026-04-07.

**Forbidden wording:**
- ❌ "Formation radius vanishes inversely in graph size."
- ✓ Correct: "At $\tau = 1/2$ on regular grids, $\bar r_0$ scales as $n^{-1/d}$. For general $\tau$, $\bar r_0 = O(1)$ (does not vanish)."

### §2.3 T-Merge (c)(d)(e) — Unconstrained mountain pass

**Claim:** Merge path between two well-separated formations admits mountain-pass critical points on $\Sigma_M^K$.

**Why retracted:** The merge path does NOT exist on $\Sigma_M^K$. The Mountain Pass Theorem is therefore inapplicable. (2026-04-07 Erratum.)

**Forbidden wording:**
- ❌ "Mountain pass theorem applies to formation merger."
- ❌ "Merge barrier height via MP theorem."
- ✓ Correct: "Merge barriers exist *kinetically* (MK-3 numerical: $\beta^{0.89}$ scaling) but their analytical characterization on $\Sigma_M^K$ is OPEN. Mountain pass on the proper manifold does not apply."

### §2.4 D-5 V5b-T′ Goldstone (2D torus PN-barrier)

**Claim:** Existence of Peierls-Nabarro barrier for translation-invariant Goldstone modes on 2D torus.

**Why retracted:** NQ-198f revealed this as a phantom — actual eigenvalue is exactly $\mu = 0$ (no PN barrier). V5b-T′ WITHDRAWN (W5 Day 3 EOD, 2026-04-29).

**Replacement:** **V5b-T-zero** sub-statement (Cat A definitional, $\mu = 0$ exact).

**Forbidden wording:**
- ❌ "PN barrier on 2D torus for V5b-T."
- ❌ "Goldstone-broken on translation-invariant graphs."
- ✓ Correct: "V5b-T-zero (Cat A definitional): translation-invariant graphs admit exact-zero Goldstone eigenvalues from $\mathbb{Z}_L^d$ orbit."

### §2.5 Literal $\rho_{\mathrm{deep}} \geq 0.84$ unconditional

**Claim:** $\rho_{\mathrm{deep}}(u^*) \geq 0.84$ for canonical single-formation minimizers, unconditional.

**Why retracted:** Counterexample on elongated formations (e.g., $3 \times 10$ rectangle gives $\rho_{\mathrm{deep}} \approx 0.27$). 2026-05-10 W7-CV113A.

**Replacement:** **S-B1-SYM** Cat B — symbolic identity $\rho_{\mathrm{deep}} \geq \theta_{\mathrm{core}}(1 - 4C_{\mathrm{iso}}/\sqrt{m})$ under HWF-1 (iso_ratio $\leq C_{\mathrm{iso}}$); the literal "0.84" is recovered as $\rho_{\mathrm{sym}}(0.2, 25, 1.0)$ at sharp regime.

**Plus** Lemma S-B1-Weak Cat A — $\rho_{\mathrm{deep}} > \rho_* \approx 0.003$ unconditional (positivity only, sufficient for Δ_sep > 0).

**Forbidden wording:**
- ❌ "ρ_deep ≥ 0.84 unconditional."
- ✓ Correct: "ρ_deep ≥ 0.84 under HWF-1 well-formedness (S-B1-SYM Cat B); ρ_deep > 0.003 unconditional (Lemma S-B1-Weak Cat A); literal 0.84 recovered at sharp parameter regime."

## §3. Forbidden overclaim wording (Cat R-prime; ban list, not counted)

These are *patterns of speech* that overclaim what SCC-CT actually proves. Banned at every documentation layer.

### §3.1 "Temporal theorem proved" (without qualification)

**Why forbidden:** T-Temporal-Identity has 4 parts (a, b, c, d). All Cat A as of CV-1.13 SEALED, but:
- (c) is **Cat A conditional** on margin $\Delta_{\mathrm{sep}} \geq \Delta_{\mathrm{sep}}^* + 2\epsilon_{\mathrm{kernel}}$.
- All 4 parts apply to **single-formation** only. Multi-formation temporal identity is OPEN.
- Composition (3+ time steps) is OP-0012 PARTIALLY STRUCTURED.

**Allowed wording:**
- ✓ "T-Temporal-Identity (a, b, c, d) Cat A for single-formation, stable-K + margin regime (CV-1.13 SEALED)."
- ✓ "Multi-formation temporal identity is OPEN; 3+-step composition is OP-0012 partially structured."

**Forbidden:**
- ❌ "Temporal identity is proved."
- ❌ "Temporal theorem holds in general."

### §3.2 "Transport fixed point fully established"

**Why forbidden:** Schauder fixed-point gives existence; does NOT give uniqueness or stability. Earlier informal claims of "Brouwer-completed self-referential OT" overclaim.

**Allowed:**
- ✓ "Self-referential OT has fixed point via Schauder; uniqueness/stability conditional on H-SINK (Cat A) and confinement (Cat A) — full self-referential uniqueness still OPEN."

**Forbidden:**
- ❌ "Self-referential OT is fully closed."
- ❌ "Transport plan is uniquely determined."

### §3.3 "Multi-formation solved"

**Why forbidden:** Only T-L1-F count bridge (conditional Cat A under (P0)-(P11)) and T-K-Select-PF/OBS (Cat B) at canonical level. OP-0009 (7 ontological sub-problems) is PARTIALLY RESOLVED at 1/7. OP-0005-DYN (Kramers rates) is OPEN.

**Allowed:**
- ✓ "Multi-formation count bridge T-L1-F is Cat A under regime hypothesis (P0)-(P11); ontology OP-0009 PARTIALLY RESOLVED 1/7; dynamics OP-0005-DYN OPEN."

**Forbidden:**
- ❌ "Multi-formation theory is complete."

### §3.4 "Sep term essentiality proved"

**Why forbidden:** $\mathcal{E}_{\mathrm{sep}}$ is *conceptually* independent (CN5 — cannot merge into other terms). But the *quantitative ablation* showing exactly when full SCC differs from BD-only is incomplete. R10 separation-dominance regime determination is OPEN.

**Allowed:**
- ✓ "Sep is conceptually independent (CN5). Quantitative essentiality regime: OPEN. Numerical: full SCC vs BD-only differ in attraction basins (exp57); analytical threshold not characterized."

**Forbidden:**
- ❌ "Sep is essential to SCC."
- ❌ "Removing Sep changes everything."

### §3.5 "Paper ready as-is"

**Why forbidden:** Multiple revision rounds documented (`THEORY/CHANGELOG.md`). Paper drafts have been revised, withdrawn, restructured multiple times. No paper is "ready as-is."

**Allowed:**
- ✓ "Paper draft prepared at CV-1.X (date); pending revision cycles for [specific points]."

**Forbidden:**
- ❌ "Paper is publication-ready."
- ❌ "Paper text is finalized."

### §3.6 "H-MORSE Cat A unconditional"

**Why forbidden:** V5b-T-zero (canonical Cat A) provides structural counterexample. Translation-invariant graphs admit exact-zero Goldstone eigenvalues from $\mathbb{Z}_L^d$ orbit. Per CV114 audit (2026-05-11): unconditional Cat A H-MORSE is **impossible**.

**Allowed:**
- ✓ "L-HMORSE-LOCAL Cat B (CV-1.16) under D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5)."
- ✓ "L-CLOSURE-LIFT Cat A (CV-1.16) for the closure-Hessian Gauss-Newton component."
- ✓ "H-MORSE-Local Cat A (target OP-HMORSE-LOCAL-A) requires additional residual + (C2′) refinements (~2 sessions ETA)."

**Forbidden:**
- ❌ "H-MORSE Cat A."
- ❌ "Morse stability proved unconditionally."
- ❌ "Hessian is positive definite at all critical points." (V5b-T-zero falsifies.)

### §3.7 "L-CLOSURE-LIFT replaces T7-Enhanced"

**Why forbidden:** L-CLOSURE-LIFT *supersedes* T7-Enhanced *as the broadness statement* — it generalizes the closure-spectrum lower bound from "along closure direction" (T7-Enhanced narrow) to "uniformly on tangent space" (L-CLOSURE-LIFT broad). But T7-Enhanced as a canonical Cat A entry is **preserved** in `THEORY/2_substrate/canonical/canonical.md` (line 1152) for historical context and CN14 (multi-formation stability expansion).

**Allowed:**
- ✓ "L-CLOSURE-LIFT (CV-1.16 Cat A) supersedes T7-Enhanced as the broadness statement."
- ✓ "T7-Enhanced (canonical Cat A) preserved as historical context."

**Forbidden:**
- ❌ "T7-Enhanced replaced by L-CLOSURE-LIFT."
- ❌ "T7-Enhanced is obsolete."

### §3.8 "Cat A by construction" / Definitional tautology PROVED

**Why forbidden:** V-AFD (2026-05-12) and R-2 (2026-05-13) failure modes. Both produced "Cat A" claims that were *definitional* (a theorem stated as PROVED because it was *defined* to be true by construction). Both archived within ~24h after fresh-context audit.

**Allowed:**
- ✓ "Definition D-X registered (no Cat assignment; not a theorem)."
- ✓ "Proposition P-X Cat A — definitional consequence of D-Y." (Honest annotation.)

**Forbidden:**
- ❌ "T-X PROVED Cat A by construction."
- ❌ "Cat A holds tautologically."

### §3.9 "2λ₂ critical ratio"

**Why forbidden:** Notation error from unordered-pair summation. Under canonical ordered-pair convention (§II.3), the correct ratio is **4λ₂**, not 2λ₂.

**Allowed:**
- ✓ "$\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ (T8-Core, ordered-pair summation convention)."

**Forbidden:**
- ❌ "$\beta/\alpha > 2\lambda_2/\lvert W''(c) \rvert$."
- ❌ "Phase transition at $2\lambda_2$ ratio."

### §3.10 "Object-level statements"

**Why forbidden:** SCC-CT operates **before** objects (§I.2). Any statement of the form "this proves that object X..." re-introduces the object primitive and violates the central ontological commitment.

**Allowed:**
- ✓ "Pre-objective formation $u^*$ on graph $G$ satisfies ..."
- ✓ "Object reading of $u^*$ at threshold $\theta$ recovers $A^\theta = \{x : u^*(x) \geq \theta\}$."

**Forbidden:**
- ❌ "SCC identifies object X with cohesion field property Y."
- ❌ "Object semantics directly follow from SCC."

### §3.11 "Cesàro / Linear transition operator $\mathbf{T}_t$"

**Why forbidden:** $\mathbf{T}_t$ demoted from canonical primitive in v2.0 (zero realizations, zero theorems, zero predicate roles). Cesàro form of $\mathbf{C}_t$ demoted in v2.0 cycle 2 (does not preserve pairwise structure).

**Allowed:**
- ✓ "$\mathbf{C}_t$ resolvent diagnostic form $(I - \alpha_C W_{\mathrm{sym}})^{-1}$ (derived; not primitive)."
- ✓ "$g_t$, $\mathrm{Bd}_t$, $\mathcal{Q}_{\mathrm{morph}}$ replace transition-operator role."

**Forbidden:**
- ❌ Re-introducing $\mathbf{T}_t$ as primitive.
- ❌ Cesàro $\mathbf{C}_t$ form.

### §3.12 "External label / classifier-driven Sep"

**Why forbidden:** Re-introduces object primitive via the back door. Sep is defined against *self-induced exterior* $1 - u$, not against any external label set.

**Allowed:**
- ✓ "Sep uses self-induced exterior $1 - u$ (canonical D1)."

**Forbidden:**
- ❌ Sep formula with external class set / label vocabulary.

## §4. Audit pattern (R-rules from session pre-brainstorms)

The following are *operational rules* for future SCC-CT extensions, distilled from the V-AFD (2026-05-12) and R-2 (2026-05-13) archive cycles and the W7-Day5 two-pass closure success:

### R1 — No language refactor

New framework names (V-AFD, R-2, etc.) are **forbidden**. Work in canonical/CV114 vocabulary only.

### R2 — Canonical alignment pre-check

Before any new lemma: `grep -r "<lemma name or key formula>" THEORY/canonical/ THEORY/working/MF/ SF/ temporal/ CV*/`. Duplication triggers immediate citation + difference documentation.

### R3 — Numerical demo obligation

Every new Cat B / Cat A claim requires canonical 15×15 grid (or appropriate substrate) numerical verification.

### R4 — Cat status honest

PROVED / SKETCH / CONJECTURE / OPEN only. Definitional tautology dressed as PROVED is forbidden.

### R5 — Round 4 external audit

After working content: fresh-context Explore agent must check "is this already canonical?" before promotion.

### R6 — Lifetime ceiling

New working folder must produce first Cat B result within ~3 days. Otherwise pause + meta-review.

### R7 — Cat A target precision

Before claiming "Cat A unconditional" for any target, grep the corresponding `THEORY/working/CV*/05_counterexample_search.md` (or equivalent counterexample catalog). If counterexamples exist, correct target to Cat B / Local / Generic *before* execution.

## §5. Why this chapter exists

Without explicit forbidden-claim registration, the theory drifts. Specifically:

- **2026-04-07 Erratum** corrected multiple overcounted Cat A claims. Without §IX, the overclaims would have persisted.
- **V-AFD / R-2 archive cycles** (5/12, 5/13) demonstrated that *internal-audit-only* validation can produce Cat A claims that crumble under external audit.
- **W7-Day5 two-pass closure** (this session) succeeded *because* the morning Track 2 honestly produced Cat B SKETCH with named CONJECTURE — the evening could then attack the CONJECTURE without revising premature claims.

The discipline of §IX is the discipline of *not regressing*. Every forbidden-wording entry above corresponds to an actual historical incident in `THEORY/CHANGELOG.md`.

---

*Chapter IX sealed within SCC-CT v0.1. References: `THEORY/2_substrate/canonical/canonical.md` §13 (Retracted section); `THEORY/CHANGELOG.md` (V-AFD discard 2026-05-13; R-2 archive 2026-05-13; CV-1.16 P7 promotion 2026-05-14); `THEORY/logs/daily/2026-05-13/41_v_afd_discard.md`, `51_r2_archive.md`; `THEORY/logs/daily/2026-05-14/01_pre_brainstorm.md §7 Rule R1-R6`. Next: `07_changelog.md`.*
