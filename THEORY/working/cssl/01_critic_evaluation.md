---
type: working/cssl/critic-evaluation
date: 2026-05-20
session_origin: W8-Day3 evening (post-EOD, critic agent invocation on 00_concept_handoff.md)
canonical_version: CV-1.18 (SEALED untouched throughout)
status: critic-evaluation (read-only review of 00_concept_handoff CSSL proposal)
reviewer: critic agent (Opus 4.7 1M)
reviews: 00_concept_handoff.md (CSSL proposal, W8-Day3 evening user-prepared)
verdict_one_line: WORTH PURSUING WITH SUBSTANTIAL MODIFICATIONS — core insight (surgery-admissible kernel decomposition) is mathematically interesting and non-trivial; but four of the four named theorem candidates collapse under scrutiny in their current form, the proposed energy ζ E_pers is structurally incompatible with canonical analyticity (CN4 / b_D=0 commitment), and the document conflates "the canonical H-MORSE problem" with a problem the canonical theory does NOT in fact pose. Recoverable as one Cat C numerical investigation + one revised Cat B target + several explicit open problems; NOT recoverable as a CV-1.19 SEAL-prep candidate without substantial reformulation.
mode: ADVERSARIAL (escalated from THOROUGH after Phase 2 surfaced 1 CRITICAL + 4 MAJOR findings on first pass)
constraint_compliance:
  - canonical 0 edits: ✓ (read-only tools)
  - DECLARATION 0 edits: ✓
  - scc/ 0 edits: ✓
  - Promotion-pipeline barrier respected: ✓ (output goes to working/cssl/, not canonical/)
  - Soft-cohesion primitive maintained in review: ✓
  - 4 energy terms treated as conceptually independent: ✓
---

> [!nav] Linked: [[00_concept_handoff|CSSL concept handoff (audit target)]] · [[../../canonical/canonical|CV-1.18 canonical (untouched)]] · [[../../canonical/DECLARATION|DECL-1.0]] · [[../../logs/daily/2026-05-20/99_summary|W8-Day3 summary]] · canonical §3.7 §9.3 §13 L-HMORSE-LOCAL / L-HMORSE-DECOMP / L-BOUNDARY-MODE-EXCLUSION / T-σ-Lemma-1 / V5b-T-zero / T-PF-A1-SDE

# CSSL — Critic Evaluation (W8-Day3 evening, post-EOD)

**Headline verdict: REVISE (substantial). Not REJECT; not ACCEPT-WITH-RESERVATIONS.**

The CSSL proposal contains one genuinely interesting structural insight (item §G.1 below: explicit kernel-decomposition allowance for topology-change events) that, if properly formalized, could become a Cat C numerical target or a long-horizon Cat B candidate. But the proposal as written has *four classes* of issues that block any Cat A/B promotion:

1. **A misdescription of the canonical problem**: §0 of 00_concept_handoff frames the H-MORSE problem as "ker H_eff^AA = Goldstone-only subspace at *non-uniform* critical points". Canonical L-HMORSE-LOCAL (Cat B, CV-1.16) does NOT make this claim — its (C4) symmetry-broken condition *explicitly* excludes V5b-T-zero translation-invariant orbits, *not* surgery events. (Detail in §A.)
2. **An energy design that violates CN4 analyticity**: the ζ E_pers persistence-homology term is generically non-differentiable at every event-emitting field configuration. Embedding PH events as an *energy* (vs *diagnostic*) breaks the analyticity commitment that grounds T14 (Łojasiewicz). (Detail in §D.4 and §F.2.)
3. **Theorem candidates that are circular or undefined**: three of four theorem candidates (T-MORSE-SURGERY-DICHOTOMY, T-SKELETON-PERSISTENCE-CORRESPONDENCE, T-SURGERY-ADMISSIBLE-HMORSE) use undefined primitives (E_surg as a *subspace*, "surgery event direction" v_surg, "ridge-critical point") that the proposal does not construct. T-WILD-DEGENERACY-EXCLUSION is the only candidate with a near-definable statement, but its proof requires inputs (coercivity + non-saturation lower bound) that the proposal does not provide. (Detail in §E.)
4. **A blurring of derived-vs-primitive ontology**: §9 defines critical skeleton S(u) as a *graph-vertex set* and §12 builds an energy term *from* this set. This re-promotes a derived structure (S(u) is a function of u_t) into an energy-determining role — exactly the kind of structural inversion that the SCC theory explicitly disallows (Commitment 12: C_t demoted to *derived* precisely because it would otherwise inflate non-primitive structure into the energy). (Detail in §F.3.)

None of these are fatal: each has a recovery path that the proposal could adopt. But each requires explicit revision before this work could enter the canonical promotion pipeline.

The CSSL idea also makes one direct claim that is *empirically supported by today's canonical machinery* and one claim that is *structurally already covered* by canonical V5b-T-zero — see §A.3 and §A.4. Recognizing the former carefully is the real opportunity in this proposal.

---

## §0 Pre-commitment predictions (made BEFORE detailed investigation)

Before reading §0-§17 of 00_concept_handoff in detail, I predicted (based on the abstract + §0 problem statement + my pre-knowledge of canonical CV-1.18 H-MORSE state):

| # | Predicted likely failure mode | Verified? |
|---|---|---|
| P1 | Confusion between "non-uniform critical point" (canonical: post-formation u^* in symmetry-broken regime) and "topology-change moments" (proposal: split/merge events in *time*) | YES — see §A.1 (CRITICAL finding). The proposal treats them as *the same problem* but they are at *different layers*. |
| P2 | Persistence homology embedded as an *energy term* will violate analyticity (CN4 b_D=0 commitment) — PH event maps are piecewise constant in u | YES — see §D.4 (CRITICAL finding). |
| P3 | "Ridge density r_i(u) = Σ w_ij (u_i - u_j)²" looks identical to (4×) the boundary smoothness sub-term in E_bd — adding "-φ(r_i)" to energy would *cancel/anti-stabilize* part of E_bd | YES — see §D.1 (MAJOR finding). This is a sign-error problem: the proposal *adds* concentration where canonical *penalizes* roughness. |
| P4 | "Surgery event subspace E_surg" will be defined circularly — defined as "the kernel directions corresponding to surgery events" with no independent construction | YES — see §E.4 (CRITICAL finding). |
| P5 | Multi-formation events (merge/split) involve *temporal dynamics* (Q5/Q6) which depend on OP-0021 T_* (axiomatic, OPEN) — proposal will silently use static Hessian but talk about dynamic events | YES — see §B.4 and §F.6 (MAJOR finding). |

Actual vs predicted: I expected 3-4 issues at MAJOR severity. Actual count after Phase 4 gap analysis + Phase 4.5 self-audit + Phase 4.75 realist check: **1 CRITICAL + 4 MAJOR + 6 MINOR + 9 explicit gaps + 2 ambiguity risks**. Escalated to ADVERSARIAL mode after Phase 2 verification surfaced more issues than predicted; ADVERSARIAL mode found 2 additional MAJOR issues (§F.3, §F.7) by checking *adjacent* canonical commitments not initially in scope (§3.7 distinction, §5.3 boundary band, §16 OP-0009 multi-formation foundations).

---

## §A — Formalize the conceptual transition (Task 1)

**Mandate.** §18 task 1: Formalize "ker H_eff^AA = Goldstone-only" → "ker H_eff^AA = G ⊕ E_surg at isolated topology events; wild degeneracy excluded everywhere."

### §A.1 What the canonical problem actually is — and is NOT

**CRITICAL Finding #1.** The proposal's framing of "ker H_eff^AA = Goldstone-only" as the canonical condition is **not what canonical L-HMORSE-LOCAL claims**. This is a substantive misdescription that the proposal builds on.

*Evidence (verified against canonical.md):*

- Canonical §13 L-HMORSE-LOCAL (Cat B, CV-1.16) defines D-HMORSE-LOCAL with five conditions: (C1) critical on free subspace, (C2′) active set well-defined, (C3) single-formation `K_act = 1`, (C4) symmetry-broken (`No nontrivial σ ∈ Aut(G) satisfies u*(σ(x)) = u*(x) for all x` — explicitly: "rules out V5b-T-zero translation-invariant orbits, D_4-symmetric center configurations, etc."), (C5) non-boundary-localized lowest mode. (canonical.md:1934–1944)
- The statement (canonical.md:1953) gives `μ_min(Π_T^free H_E Π_T^free) ≥ c_HML > 0` — a *strict positivity* bound, NOT a "Goldstone subspace only" kernel structure.
- The (C4) condition does NOT enforce "no kernel directions" — it *removes the class of critical points* (V5b-T-zero) where exact-zero kernels exist (those are canonically *excluded* from the L-HMORSE-LOCAL regime, see canonical.md:1964: "translation-invariant graphs admit exact-zero Goldstone eigenvalues from `Z_L^d` orbit. Hence 'Local' qualifier is essential.").
- Canonical V5b-T-zero (Cat A definitional, CV-1.5.1, canonical.md:1328) explicitly *registers* the "ker ≠ {0}" case: `μ_Gold^{V5b-T-zero}(u*) = 0 exactly` from `Z_L^d` orbit-tangent directions on translation-invariant graphs.

*What this means for CSSL.* The proposal's premise "currently we require ker H_eff^AA = G only and we want to extend this to allow G ⊕ E_surg" is *factually wrong*. Canonical SCC does NOT currently require "Goldstone-only kernel"; canonical L-HMORSE-LOCAL says "positive lower bound on `Π_T^free` Hessian *after restricting to graphs and minimizers where V5b-T-zero is excluded*". The actual canonical scope:

| Regime | Canonical treatment | Cat |
|---|---|---|
| Uniform critical `u* = c·1` on translation-invariant graph | V5b-T-zero: `μ_Gold = 0` exact (orbit-tangent directions form zero subspace) | A (definitional) |
| Post-formation `u*` with (C4) symmetry-broken | L-HMORSE-LOCAL: `μ_min > 0` (strict positivity) | B (unconditional) |
| Post-formation `u*` failing (C4): `D_4`-center, V5b-T translation orbits, mirror configurations | Excluded from L-HMORSE-LOCAL by hypothesis; structurally handled by σ-framework / V5b-T-zero | A / definitional |
| Critical *configurations during topology change* (merge saddle, split neck, birth nucleation) | NOT covered by L-HMORSE-LOCAL; these are *saddle points* (typically Morse index ≥ 1), which OP-HMORSE-SADDLE (open) was registered for | OP-HMORSE-SADDLE (open) |
| Critical configurations during *dynamic* topology transitions (Kramers crossings of saddle in K-jump events) | OP-0008 (σ^A K-jump non-determinism) + OP-0005-DYN + OP-0021 T_* registration (DEPRECATED Routes A/B; Route C only) | C / open |

*Why this matters.* The CSSL proposal positions itself as extending L-HMORSE-LOCAL. But L-HMORSE-LOCAL is about *post-formation static stability* (Morse-index-0 critical points with a single formation). Topology-change events (merge/split/birth/death) live at *different mathematical objects*: they are *saddle points* of the static energy landscape (not Morse-0 minima), and they are entered/exited via *time-dynamics* (T-PF-A1-SDE reflected Langevin, OP-0005-DYN Kramers rates).

The CSSL proposal is therefore **not** an extension of L-HMORSE-LOCAL; it is — at best — an extension of OP-HMORSE-SADDLE (saddle-point Hessian regularity, OPEN, canonical.md:594) + a dynamics question (OP-0005-DYN, OP-0008). The framing in 00_concept_handoff §0 conflates these.

*Fix.* The CSSL proposal must be reframed as a *saddle-point* characterization problem, not as an extension of the (Morse-0) L-HMORSE-LOCAL. Specifically:

> "At topology-change configurations (Morse index ≥ 1 saddles, NOT Morse-0 minima), the active-set Hessian has a finite-dimensional kernel direction corresponding to the surgery-event normal coordinate."

This is a *separate* mathematical claim from anything L-HMORSE-LOCAL addresses. If reformulated this way, it becomes a candidate to attack OP-HMORSE-SADDLE — which is canonically OPEN and a *different* open problem from the current L-HMORSE-LOCAL Cat B → Cat A path (OP-HMORSE-LOCAL-A, canonical.md:593).

```
CoT (target = formalize correctly):
Step 1 (premise). L-HMORSE-LOCAL.scope = {Morse-0 minima with K_act=1, symmetry-broken (C4), non-boundary-localized (C5)}.
Step 2 (premise). Topology-change configurations (merge/split/birth/death) are saddle points, NOT Morse-0 minima.
Step 3 (inference). Therefore CSSL.scope ⊄ L-HMORSE-LOCAL.scope. CSSL is about a DIFFERENT set of critical points.
Step 4 (consequence). The proposal's "extend ker H_eff^AA from G to G ⊕ E_surg" cannot extend L-HMORSE-LOCAL — they live at different critical points.
Step 5 (anchor). CSSL belongs to OP-HMORSE-SADDLE (Hessian regularity at *saddle* configurations), which is open and registered (canonical.md:594).
```

**Verdict:** This is the highest-priority fix. The proposal must rename/reframe its target before any other technical content can be evaluated against the right baseline. **Confidence: HIGH.** **Realist check: this is not a numerical sensitivity — it is a category error about which canonical lemma is being extended. Severity remains CRITICAL.**

### §A.2 The conceptual transition correctly stated

Under the corrected framing (§A.1 fix), the conceptual transition becomes:

**Stable phase (post-formation Morse-0 minimum, satisfying L-HMORSE-LOCAL (C1)–(C5)):**
$$\text{ker}\bigl(\Pi_T^{\text{free}} H_{\mathcal{E}}(u^*) \Pi_T^{\text{free}}\bigr) = \{0\} \quad \text{(strictly positive — canonical Cat B)}$$

(Note: NOT "Goldstone subspace" — L-HMORSE-LOCAL excludes Goldstone-bearing regimes via (C4); the *kernel is empty* on the free tangent subspace, not "Goldstone only".)

**Surgery configuration (proposed: saddle point at topology-change moment, satisfying TBD-CSSL conditions):**
$$\text{ker}\bigl(\Pi_T^{\text{free}} H_{\mathcal{E}}(u^{\text{sad}}) \Pi_T^{\text{free}}\bigr) = \mathcal{E}_{\text{surg}}(u^{\text{sad}})$$

where `E_surg` is a finite-dimensional subspace corresponding to surgery event normal coordinates. **For this to be a well-defined claim, the proposal must independently construct `E_surg` from a geometric structure (e.g., the normal direction to a codim-1 stratum in `F_M(G)` separating K=1 from K=2 sectors).** It currently does not.

**Wild-degeneracy exclusion (the only well-formed part of the original §17 boxed condition):**
$$\dim\,\text{ker}\bigl(\Pi_T^{\text{free}} H_{\mathcal{E}}(u^{\text{sad}}) \Pi_T^{\text{free}}\bigr) = \dim \mathcal{E}_{\text{surg}}(u^{\text{sad}}) \quad \text{(no other kernel directions)}$$

This formulation requires (i) a definition of `E_surg` independent of "the kernel directions" (circularity avoidance), (ii) a saddle-point analysis (Morse index ≥ 1), and (iii) a regime hypothesis distinguishing "tame" from "wild" saddles. **None of these are provided by the current proposal**.

### §A.3 What canonical machinery *does* support, directly

**Realist check / steelman acknowledgment.** The CSSL intuition is *non-trivially correct* in one direction: T-PF-A1-SDE (Cat A, canonical §13, canonical.md:1668) establishes reflected Langevin well-posedness on the field polytope. K-jump events (registered as OP-0008, canonical.md:581, Cat C/B with sub-problems CONT/MERGE/SPLIT/DIST per Session W) DO correspond to topology-changing transitions in the persistent component count `K_act` (D-ST-3, canonical §3.11). T-K-Select-PF (Cat B, CV-1.10, canonical.md:1835) gives equilibrium K-selection via Package I — implying that the system *does* visit different K-sectors `B_K` via the SDE.

So a *correctly formulated* version of CSSL would say something like:

> "At codimension-1 boundaries `∂B_K ⊂ F_M(G)` between K-sectors (where `K_act(u)` is discontinuous), there exist critical configurations whose static Hessian has a one-dimensional kernel transverse to the boundary, corresponding to the K-jump normal coordinate."

This is a well-defined Cat B-target claim that uses *only canonical machinery* (T-PF-A1-AR field polytope, T-K-Select-PF K-sectors, K_act as #PersComp). It is also a *much weaker* claim than CSSL §11's "six surgery event types" (merge/split/birth/death/hole birth/hole death). The proposal is reaching for *all* of topology change; canonical machinery currently supports only the *K-jump codimension-1 normal direction*.

**Confidence: HIGH** that this restricted reformulation is consistent with canonical CV-1.18; **MEDIUM** that it admits a Cat B proof in 5–10 sessions of W9+ work.

### §A.4 The §17 "boxed condition" — what survives

The proposal's final summary §17 boxes three statements:

1. `ker H_eff^AA = G` (stable phase) — **FALSE under canonical L-HMORSE-LOCAL** (kernel is actually `{0}` on free tangent subspace under (C4); the `G` description applies to V5b-T-zero regime which is *separately* canonical).
2. `ker H_eff^AA = G ⊕ E_surg` (surgery phase) — **UNDEFINED**: E_surg has no independent construction.
3. `ker H_eff^AA ⊋ G ⊕ E_surg forbidden` (wild) — **UNVERIFIABLE** until #2 is defined.

**What survives**: a coarse two-state description. After §A.1 fix, this can be reformulated:

> "At static Morse-0 minima satisfying (C4)+(C5), Hessian is strictly positive (canonical L-HMORSE-LOCAL). At codim-1 K-sector boundaries (T-K-Select-PF + T-PF-A1-AR), Hessian has exactly one zero direction normal to the boundary (proposed claim; W9+ Cat B target)."

Even this reformulation requires constructing `dim E_surg = 1` from independent codimension-1 geometry, not from "kernel directions".

---

## §B — Critical skeleton S(u) (Task 2)

**Mandate.** §18 task 2: Define skeleton via A(u)={i:δ<u_i<1-δ}, r_i(u)=Σ_{j~i} w_ij (u_i-u_j)², R(u) = local maxima of r_i inside A(u), S(u) = ridge-critical points inducing local topology change.

### §B.1 Algebraic identity: r_i(u) reproduces the boundary smoothness term per-site

**MAJOR Finding #1 (graph-discrete subtlety).** The ridge density `r_i(u) = Σ_{j~i} w_ij (u_i - u_j)²` is **identical** (up to a global factor) to the per-site decomposition of canonical `E_bd` smoothness term.

*Evidence (verified against canonical §8.4):* Canonical `E_bd = α Σ_{x,y} N(x,y)(u_x - u_y)² + β Σ_x u_x²(1-u_x)²` where the sum is over **ordered pairs** (canonical.md:723). Per-site decomposition: define `e_bd^{site}(i; u) := α Σ_{j~i} w_ij (u_i - u_j)²` (one direction, half the ordered-pair sum); then `r_i(u) = e_bd^{site}(i; u) / α` exactly.

In other words, the proposal's `r_i(u)` is not a new construct — it is the *integrand* of the canonical boundary smoothness term, per site.

*Consequences.*

1. **Sign convention conflict (CRITICAL for energy design).** Canonical `E_bd` *minimizes* the sum-over-sites of `r_i(u)/α` (smoothness penalty: low r_i preferred). The CSSL proposal §12.1 *maximizes* `Σ_i φ(r_i)` (ridge concentration: high r_i preferred). These have *opposite signs*. Adding `-κ Σ φ(r_i)` to E directly anti-stabilizes the canonical boundary smoothness gradient. Details in §D.1.
2. **Definition is reasonable in graph-discrete setting**, but is *not new*: r_i(u) is just the per-site discrete-gradient-squared, which already exists in canonical implementation (`CODE/scc/energy.py` per-site E_bd contributions). Canonical `T-OP6-B` (Cat A, §5.3b) and canonical persistent gradient ridge `B_PersRidge(u)` already extract a "ridge boundary" structure from `|∇_G u|²` via persistence homology of the *gradient magnitude field*. The proposal's R(u) is a *less rigorous* version of `B_PersRidge` and reinvents (badly) what canonical already has at Cat A.

*Anchor check.* canonical §5.3b (canonical.md:367–404, T-OP6-B Cat A) constructs:
$$B_{\text{PersRidge}}(u) = \{x \in X : (b_x, d_x) \in \text{Bars}_0(\vert \nabla_G u\vert; G),\ b_x - d_x > \rho_{\text{bd}}\}$$
with `|∇_G u(x)| = √(Σ_{y~x} (u(x) - u(y))²) = √(r_x(u)/w_norm)`. So `B_PersRidge` is *already* the persistence-filtered ridge set of exactly the proposal's `r_i(u)`. The proposal's S(u) construction "ridge-critical points inducing topology change" is essentially asking for the *connected-component birth/death structure* of `B_PersRidge(u)` — which is what `T-OP6-B`'s persistence barcode `Bars_0(|∇_G u|; G)` *measures*.

**Fix (recovery path).** Drop the proposal's invented R(u)/S(u) definitions. Re-anchor on canonical `B_PersRidge(u)` (Cat A) and persistence barcode. Then S(u) becomes:

> S(u) := connected components of `B_PersRidge(u)` whose persistence bar `[b, d)` straddles a K_act-jump in the superlevel-set filtration of u.

This is canonically grounded (T-OP6-B + D-ST-3) and *much sharper* than the proposal's "local maxima of r_i inside A(u)".

**Confidence: HIGH** that the proposal's R(u)/S(u) is inferior to canonical `B_PersRidge` and that a reformulation using canonical machinery is mathematically tighter.

### §B.2 Active boundary band A(u) = {i : δ < u_i < 1-δ} — definitional check

The proposal's A(u) restates canonical §5.3 boundary band `Bd_t(u) = {x : θ_1 < u_t(x) < θ_2}` (canonical.md:341–349). This is reasonable but **not** what the canonical H-MORSE analysis uses. L-HMORSE-LOCAL uses `T_{u^*}^free` (the **free tangent subspace**, defined as `{v : Σv = 0, v_x = 0 for x ∈ A*}`), which is the *complement* of the corner-saturated active set `A* = {x : u*(x) ∈ {0,1}}` (canonical.md:1932). The CSSL `A(u)` is the open band; canonical's `T^free` is the *complement of the active set* — these are nearly opposite notions of "active".

**Naming-conflict risk.** "Active boundary band A(u)" vs "active set A*(u)" in canonical notation. **MINOR** but the proposal should rename `A(u) → BdBand(u)` or similar to avoid notational collision in any canonical-promotion path.

### §B.3 Local maxima of r_i (R(u)) — graph-discrete subtlety

The proposal §9.3 defines `R(u) = {i ∈ A(u) : r_i(u) ≥ r_j(u) for nearby j}`. On a finite graph, "local maximum" is ambiguous: graph 1-neighborhood, 2-neighborhood, or radius-k? On regular graphs the local-maximum set is well-defined; on irregular graphs (boundary regions, SBM) the same point may be locally-max for radius-1 but not radius-2. This is a **MAJOR** ambiguity for any Cat A/B promotion path.

*Empirical anchor needed.* `exp25_hessian_diagonal.py` (canonical L-BOUNDARY-MODE-EXCLUSION anchor, canonical.md:2167) tests boundary-mode dominance numerically — it would need extension to test R(u) stability under graph perturbation before R(u) can be a definable invariant.

### §B.4 Ridge-critical point definition — undefined

The proposal §9.4 defines `S(u) = {i ∈ R(u) : i is a ridge-critical point AND induces local topology change}`. Neither "ridge-critical point" nor "induces local topology change" is defined.

*Reading 1 ("ridge-critical" = critical point of r_i restricted to the band).* This requires viewing `r : V → R` as a *function on graph vertices* and asking when its gradient (graph-difference) vanishes. On a finite graph this is well-defined but typically *empty* (the discrete function r_i has gradient zero only at flat plateaus, which are non-generic).

*Reading 2 ("ridge-critical" = saddle of u itself with index 1 in graph-Morse sense).* This requires discrete Morse theory (Forman 1998) or Banchoff's piecewise-linear Morse theory — neither of which the proposal references. This is also the framework needed for "topology change" to be unambiguous.

**MAJOR finding.** The proposal must commit to either Forman discrete Morse, Banchoff PL Morse, or persistent-homology critical-pair language. Each has *different* notions of "critical point" and "topology change". Currently §9.4 is undefined. (See §F.3 for the more general Morse-index robustness issue.)

---

## §C — Tame vs wild singularities (Task 3)

**Mandate.** §18 task 3: Distinguish tame (finite-index Morse saddle, bounded curvature, persistent) from wild (lattice spike, checkerboard, fractal, non-persistent).

### §C.1 The proposal's six conditions for tame singularity — audit

Proposal §10 lists six conditions for "tame":

1. Local critical index finite. ✓ Reasonable but requires graph Morse framework (see §B.4).
2. Local topology change corresponds to persistent homology change. ✓ Well-defined under PH framework (canonical D-ST-3 superlevel-set H_0 barcode).
3. Curvature concentration bounded. ✗ "Curvature" on a graph is ambiguous. On `R^n`: |∇²u|; on a graph: discrete Laplacian? Ridge curvature? `∇_G² u`? The proposal's E_wild = (Δ_G u_i)² (§12.2) suggests they mean discrete Laplacian, but this is not stated in §10.
4. Lattice-scale oscillation excluded. ✓ Reasonable; needs an explicit scale (e.g., minimum persistence > k·lattice_spacing).
5. Post-event return to H-Morse stable phase. ✗ This is a *dynamic* claim (involves time-evolution after the event). Without a dynamics model, this is undefined. Under T-PF-A1-SDE (reflected Langevin), post-event behavior depends on `T_*` (OP-0021, axiomatic per CV-1.18) and the post-event basin geometry — neither of which the proposal addresses.
6. Singularity emits finite-dimensional subspace. **CIRCULAR** — this is the *conclusion* that the surgery-admissible H-Morse theorem T-SURGERY-ADMISSIBLE-HMORSE is supposed to *prove*. Using it as a *definition* of "tame" turns the dichotomy into a tautology. See §E.4.

**MAJOR finding (circularity).** Condition 6 makes "tame" ≡ "satisfies T-SURGERY-ADMISSIBLE-HMORSE". Then T-SURGERY-ADMISSIBLE-HMORSE becomes "tame singularities satisfy the kernel decomposition" = "things satisfying the kernel decomposition satisfy the kernel decomposition". This is the *fundamental* circularity flaw in the §10 + §11 + §14 chain.

*Fix.* Conditions for "tame" must be *intrinsic* (definable from u alone or from u + (G, params), no reference to Hessian kernel). A defensible candidate:

> u is tame at a critical configuration u^c iff: (i) the Forman discrete Morse index at u^c is finite and ≤ 2; (ii) the persistent homology bar entering at u^c has persistence ≥ ρ_pers > 0 (canonical D-ST-3 threshold); (iii) the discrete bi-Laplacian |Δ_G² u^c|_∞ ≤ M for an a priori bound M = M(α, β, n); (iv) the active boundary band thickness `|BdBand(u^c)|/n ≤ ρ_bd-band` per T-OP6-B Cat A.

This formulation uses only intrinsic and *canonical-grounded* quantities; it admits an independent Cat C numerical investigation. **Confidence: HIGH** that this reformulation is necessary for the dichotomy to be meaningful; **MEDIUM** that it admits Cat B promotion in 5-10 sessions.

### §C.2 Combining PH + bounded curvature + lattice exclusion

The proposal asks how these three "combine". A defensible answer:

- *PH persistence* `≥ ρ_pers`: rules out high-frequency birth/death (lattice noise) but does NOT bound smoothness/curvature.
- *Bounded curvature* `|Δ_G² u| ≤ M`: rules out spike formation (per-site singularity) but does NOT prevent topological micro-events at low persistence.
- *Lattice-scale exclusion* (minimum persistence > k·lattice_spacing): rules out lattice-scale artifacts (numerical pinning) but is redundant with PH persistence if calibrated.

These are *complementary* (PH covers topology-noise, bi-Laplacian covers point-spike, lattice covers numerical-pinning), not redundant. Each has a canonical anchor:

| Condition | Canonical anchor | Cat |
|---|---|---|
| PH persistence | D-ST-3 / B_PersRidge / `ρ_pers > 0` (CV-1.6) | A |
| Bi-Laplacian bound | T-OP6-B `H4: κ_max · ξ ≤ 0.1` (canonical.md:385) | A under H4 |
| Lattice-scale | Implicit in canonical `ξ = (2α/β)^(1/2)` interface width | A via H1-H4 |

So the *separate* ingredients are canonically grounded. The proposal's job would be to *combine* them into a single coherent dichotomy. This is a non-trivial but reasonable Cat C target.

### §C.3 The wild singularity zoo

The proposal §10 enumerates: random spike, lattice-scale checkerboard, fractal boundary, non-persistent topological noise, unbounded curvature blow-up, numerical artifact.

*Comments:*
- "Random spike": prevented by bi-Laplacian bound (H4-style).
- "Lattice-scale checkerboard": is exactly the highest-eigenvalue mode of L_G (eigenvalue `4d` on regular d-graph). Prevented by `α · λ_max(L_G)` cost in E_bd, but only if α is large enough.
- "Fractal boundary": ill-defined on finite graph; on continuum, requires Hausdorff dimension > codim-1. Could be operationalized as: minimum-persistence component count > polynomial in n.
- "Non-persistent topological noise": directly addressed by PH persistence threshold.
- "Unbounded curvature blow-up": only meaningful in continuum limit; on finite graph, prevented by `u ∈ [0,1]`.
- "Numerical artifact": not a mathematical category; it is an implementation concern.

Of the six, three are genuine mathematical categories (spike, checkerboard, fractal) and three are either continuum-only (curvature blow-up), already-covered (non-persistent), or implementation-level (artifact). The dichotomy *as a definition* needs to address only the three genuine categories.

---

## §D — Energy design audit (Task 4)

**Mandate.** §18 task 4: For E_CSSL = E_SCC + κ E_ridge + η E_wild + ζ E_pers, audit well-posedness (coercivity, lower bound, analyticity), preservation of natural formation emergence, compatibility with existing canonical E.

### §D.1 κ E_ridge = -κ Σ φ(r_i) — sign conflict and spike risk

**MAJOR Finding #2.** As predicted (§0 P3), `E_ridge = -κ Σ φ(r_i)` *subtracts* from total energy in proportion to per-site `r_i = Σ_{j~i} w_ij (u_i-u_j)²`. Since canonical `E_bd` *adds* `2α Σ_i r_i / w_norm` to total energy (per §B.1), the CSSL total energy in the smoothness sub-term becomes:

$$E_{\text{smooth-total}}(u) = 2\alpha \sum_i r_i(u) - \kappa \sum_i \phi(r_i(u))$$

For small r_i (deep interior or deep exterior), `φ(r_i) ≈ r_i` (linear). Then the smoothness coefficient effectively becomes `(2α − κ)`. If `κ > 2α`, **E_bd smoothness becomes destabilizing — the field develops arbitrary high-frequency oscillation, exactly the "wild" behavior the proposal wants to exclude.**

Even with bounded saturating φ (e.g., `φ(r) = r/(1+r)`):
- Near small r (smooth fields): φ ≈ r, sign conflict as above.
- Near large r (sharp boundaries): φ ≈ 1, gradient `dφ/dr ≈ 1/(1+r)² → 0`, so E_ridge becomes flat — but this means E_ridge ceases to *reward* sharp boundaries above the saturation scale. So the only regime where E_ridge actively promotes ridges is the *small-r regime*, where it *fights E_bd*.

**The proposal's design intent (sharpen ridges) is in direct tension with canonical E_bd's smoothness gradient.** A correctly-designed sharpening term would need to:

1. Be active *only on the boundary band* (not on saturated interior/exterior).
2. Promote ridge *concentration* (higher r_i clustered at fewer sites) without promoting ridge *intensity* (uniformly higher r_i everywhere).
3. Not change the sign of the smoothness sub-gradient in the deep-interior regime.

A defensible candidate (not in proposal):
$$E_{\text{ridge-corrected}}(u) = -\kappa \sum_i \mathbb{1}_{i \in \text{BdBand}(u)} \cdot \phi(r_i(u) - r_{\text{thr}}^+) \cdot (1 - 4u_i(1-u_i))$$

where the indicator restricts to boundary band sites, `r_thr^+` shifts the cost to large-r only, and `(1-4u(1-u))` further restricts to corners (W''(u) > 0). This is constructable but is NOT what the proposal proposes.

**Confidence: HIGH** that the proposal's `E_ridge` as written either (a) does nothing measurable (φ saturating, gradient → 0 above ridge threshold) or (b) actively destabilizes E_bd (φ linear in active range). Either way, it is not well-posed as a sharpening term. **Realist check: this is not a parameter-tuning issue; it is a sign-structure issue. The proposal has the wrong sign in the small-r regime regardless of φ choice. Severity: MAJOR (not CRITICAL because the term can be redesigned, but the current design must be discarded).**

### §D.2 η E_wild = η Σ (Δ_G u_i)² — coercivity and over-smoothing

`E_wild = η Σ (Δ_G u_i)² = η ‖L_G u‖² = η u^T L_G² u`. This is the discrete bi-Laplacian energy.

*Properties:*
- Convex, PSD quadratic form. ✓ Coercive on `1^⊥` (since `L_G² ≥ λ_2(L_G)² · Π_{1^⊥}`).
- Analytic on `Σ_m`. ✓
- Lower bound: ≥ 0, achieved at u ∈ ker(L_G) = constant fields = `c · 1`. ✓
- Penalizes high-frequency modes more strongly than `E_bd` smoothness (factor `λ_k(L_G)²` vs `λ_k(L_G)`). ✓ for the proposal's stated goal (suppress checkerboard).

*Concerns:*
1. **Over-smoothing of legitimate boundary structure.** Phase-separated minimizers have `u ≈ {0,1}` step profiles. At a step, `|Δ_G u|² ~ O(1)` per boundary site. Total `E_wild ~ η · |Boundary|`. For η too large, this drives `Boundary → 0` (no formation). The proposal's goal is to "kill checkerboard but not boundary"; this requires `η · 1 ≪ β · 1` per boundary site, i.e., `η ≪ β`. Easy to satisfy in principle.
2. **Interaction with T-OP6-B persistent ridge.** T-OP6-B (canonical Cat A) constructs ridges with width `ξ = √(2α/β)`. If `η ≫ α`, the bi-Laplacian sub-cost dominates Allen-Cahn smoothness and the ridge width shifts. This is a *parameter regime* concern, not a fundamental flaw.

**MINOR.** E_wild is well-posed if `η ≪ β` is maintained. Should be added to the proposal as an explicit parameter constraint analogous to canonical `β/α > 4λ_2/|W''(c)|` (T8-Core).

### §D.3 ζ E_pers — persistence homology as an energy term

**CRITICAL Finding #2.** Persistence homology cannot be embedded as a *differentiable* energy term without losing analyticity. This violates canonical commitment **CN4** (canonical.md:897, "b_D = 0 for the distinction operator. Energy analyticity (required for T14, Łojasiewicz convergence) takes precedence over the explicit gradient term").

*Evidence.* The PH barcode `Bars_0(u; G)` is computed as the sequence of (birth, death) events of `H_0` components in the superlevel-set filtration `X_θ = {i : u_i ≥ θ}` parametrized by `θ ∈ [0,1]`. Key facts (Edelsbrunner-Harer 2010, Cohen-Steiner-Edelsbrunner-Harer 2007):

1. The barcode is **piecewise constant** in u: it changes only when `u_i = u_j` for some pair `(i,j)` that newly enters the filtration order.
2. At these *transition* configurations, the barcode is *discontinuous* (a bar appears, disappears, or merges).
3. The barcode is Lipschitz-continuous in the bottleneck distance metric, but **not differentiable** in any pointwise gradient sense.

Therefore "penalty for low-persistence topological noise" cannot be a smooth function of u; at best it is piecewise smooth with finitely many discontinuities. The discontinuities occur on `(n-1)`-dimensional sub-manifolds of `Σ_m` defined by `{u : u_i = u_j for some i,j}` (the "filtration transition" set).

*Consequences for canonical analyticity.*
- Canonical T14 (Łojasiewicz gradient inequality) requires `E` analytic on `Σ_m`. Adding any non-analytic term breaks this.
- Canonical L-HMORSE-DECOMP (Cat B, canonical.md:1996) requires `b_D = 0` (CN4 analyticity) and canonical A3 — both rely on smoothness of E.
- T-PF-A1-SDE (Cat A, canonical.md:1668) requires `∇Ẽ` Lipschitz on the field polytope (T-PF-A1-AR provides this; relies on `E_SCC` smoothness).

Adding `ζ E_pers` directly to E breaks all of: T14 Łojasiewicz, L-HMORSE-DECOMP, T-PF-A1-SDE Lipschitz, T-PF-A1-GI Gibbs (which requires Lipschitz of `∇Ẽ`). This is not a small effect — it cascades through Cat A theorems.

**Possible recovery paths (none in proposal):**

1. **PH as diagnostic only, not energy.** This is what canonical does for D-ST-3 and B_PersRidge — PH is used to *define observables* (`K_act`, persistent ridge boundary), but does not enter the variational energy. **HIGHLY RECOMMENDED.**
2. **Smoothed PH cost (Adams et al. 2017 persistence images, or Bubenik 2015 persistence landscapes).** These are continuous-in-u proxies for persistence diagrams. They are *Lipschitz* but not analytic; they would still break T14 Łojasiewicz. Could work for *gradient flow* (continuous E) but not for *analytic* SCC theory.
3. **Restrict PH-energy effect to a separate energy regime not coupled to L-HMORSE.** E.g., add E_pers only to an "outer regularization loop" that runs after each SCC minimization step. This is fundamentally an *engineering* solution, not a theoretical one, and violates the proposal's own §4 commitment ("no external operation mode").

**Confidence: HIGH** that `ζ E_pers` as written is incompatible with canonical CN4 + T14 + T-PF-A1-AR/SDE/GI/PE. **Realist check: this is a structural incompatibility, not a numerical sensitivity. It survives all four realist questions. Severity: CRITICAL.**

**Fix.** The proposal must demote `E_pers` to a *diagnostic* (not an energy term). This is consistent with canonical practice (D-ST-3 K_act and B_PersRidge are both diagnostics) and is what §16D of the proposal itself ambivalently considers ("aenergy에 직접 넣는 것이 가능한가, 아니면 diagnostic으로만 써야 하는가?"). The honest answer: diagnostic only.

### §D.4 Compatibility audit summary

| Term | Coercivity | Lower bound | Analyticity | Preserves T8 formation | Compatible with canonical E? |
|---|---|---|---|---|---|
| E_ridge = -κ Σ φ(r_i) | NO (∞ at φ saturating singularity-free direction unless careful; depends on κ vs α) | YES bounded below by `-κ n · sup_r φ(r) ≥ -κ n` if φ bounded | YES if φ analytic | NO if κ > 2α (anti-stabilizes E_bd smoothness) | CONDITIONAL (κ < 2α and φ active only above r_thr; current proposal does neither) |
| E_wild = η Σ (Δ_G u_i)² | YES on 1^⊥ | YES ≥ 0 | YES | YES if η ≪ β | YES under explicit parameter constraint |
| E_pers = penalty for low-persistence | YES (bounded barcode = finite) | YES if bounded | **NO** (piecewise constant in u) | YES intent but breaks variational structure | **NO** (breaks CN4 + T14 + T-PF-A1 cascade) |

**Net verdict on E_CSSL energy design:** Of three new terms, one (E_wild) is well-posed under explicit constraint; one (E_ridge) is misdesigned (sign-structure issue, recoverable with substantial revision); one (E_pers) is fundamentally incompatible with canonical analyticity (must be demoted to diagnostic). The proposal's energy design **as written** cannot enter canonical without violating Cat A theorems.

### §D.5 Spike-formation risk under E_ridge maximization

The proposal §16D asks: "ridge concentration → ill-posed spike formation?"

*Direct analysis.* If `φ` saturates as `φ(r) = r/(1+r)`, then for any fixed total `Σ r_i ≤ R_max`, the maximum of `Σ φ(r_i)` over distribution of r's is achieved by concentrating all mass at one site: `r_{i*} = R_max, r_{i ≠ i*} = 0`. This gives `Σ φ = R_max/(1+R_max) ≈ 1`. Spreading mass uniformly across n sites gives `Σ φ = n · (R_max/n)/(1+R_max/n) ≈ R_max/(1+R_max/n) ≈ R_max for small R_max/n`.

Wait — for *small* r per site, spreading mass actually *increases* the sum (φ is concave). So with bounded `φ`, the maximum is *not* a spike but a *uniform distribution*. Saturating φ actively *disfavors* spike concentration in this regime.

But for *large* r per site (r ≥ 1), φ is in the saturated regime, gradient `dφ/dr → 0`. So concentrating mass above the saturation threshold provides no marginal benefit. This means E_ridge with saturating φ has the perverse property of being *active* exactly where boundary smoothness is *not* yet sharp, and *inactive* where boundaries already are sharp. This is the wrong incentive structure.

*With unbounded φ* (e.g., `φ(r) = r`): E_ridge = -κ Σ r_i = -κ (E_bd_smooth / α). This is just an effective shift `α → α - κ/(some const)`. Same as §D.1 analysis: no actual sharpening, just smoothness coefficient reduction. **Confirms MAJOR finding.**

*With explicitly spike-promoting φ (e.g., `φ(r) = r²`):* This DOES promote concentration, but at the cost of unbounded marginal benefit per spike site. Would create coercivity failure (any field with one site at r → ∞ has E → -∞). NOT well-posed.

**Summary:** Under any of (a) bounded-saturating φ, (b) linear φ, (c) super-linear φ, the `E_ridge` term as written is either (a) doing nothing useful (wrong incentive), (b) equivalent to a smoothness-coefficient reduction (no sharpening), or (c) ill-posed (coercivity failure). **The "ridge concentration → spike formation" question has answer: depends on φ, but no φ choice gives the proposal's stated intent in a well-posed form. MAJOR finding (recoverable with substantial redesign).**

### §D.6 Can PH events be made "differentiable enough" for energy embedding?

Direct answer: **NO.** PH barcodes are Lipschitz under bottleneck distance (Chazal et al. 2009 stability theorem) but not differentiable in u. Persistence images and landscapes (Adams 2017, Bubenik 2015) are continuous proxies but introduce discretization/scale parameters that themselves break analyticity. The fundamental theoretical limit: PH event coordinates are *combinatorial* (which pair of sites attains the next filtration threshold), and combinatorial choices are not differentiable.

For the proposal to embed PH in *energy* in any way compatible with canonical CN4, would require fundamentally new mathematics (e.g., a smooth "persistence-like" functional with analytic dependence on u). No such functional exists in the topological data analysis literature.

**Recommendation: PH used as diagnostic only, never as energy.** This is what canonical D-ST-3 and B_PersRidge already do.

---

## §E — Theorem candidates (Task 5)

For each of T-MORSE-SURGERY-DICHOTOMY, T-SKELETON-PERSISTENCE-CORRESPONDENCE, T-WILD-DEGENERACY-EXCLUSION, T-SURGERY-ADMISSIBLE-HMORSE: proof sketch outline, dependencies, counter-example check.

### §E.1 T-MORSE-SURGERY-DICHOTOMY — undefined event partition

**Statement (proposal §14):** Under tame skeleton regularization, almost-everywhere in time the formation is H-Morse stable; at isolated topology-change moments, kernel admits surgery decomposition.

**Dependencies it would need:**
- Definition of "tame" not dependent on conclusion (currently circular per §C.1).
- Definition of "almost-everywhere in time" with measure (Lebesgue on T? Markov-invariant measure under T-PF-A1-SDE? Stationary distribution under T-K-Select-PF?).
- Independent characterization of "isolated topology-change moments" as a set of measure zero in time.
- L-HMORSE-LOCAL (Cat B) for the stable regime — but L-HMORSE-LOCAL requires (C4) symmetry-broken (canonical.md:1941), which is *not automatic* between topology events; need to show (C4) is preserved.

**Proof sketch (if attempted with current framework):**
1. By T-PF-A1-SDE (canonical Cat A): SDE has unique strong solution with Gibbs invariant measure.
2. By T-PF-A1-GI + T-PF-A1-PE (canonical Cat A): trajectory is ergodic, spends time in `B_K` sectors proportional to `p_K`.
3. By T-K-Select-PF (Cat B): K-sector transitions are codimension-1 events.
4. At sector boundaries: ???? (no canonical statement about Hessian kernel structure at codim-1 K-jump points).

The chain breaks at step 4. **The proposal does not provide step 4.** It just asserts that kernel structure changes "from G to G⊕E_surg" without constructing the codim-1 normal direction.

**Counter-example check.** Consider a 1D cycle `C_n` with `c = 1/2` and `β/α` slightly super-critical. The system has multiple metastable minimizers `u^{*,k}` with different orientations. K-jump events (rare under T-PF-A1-SDE) connect different `u^{*,k}` via saddles. At those saddles:
- The Hessian has Morse index ≥ 1 (definitionally — they are saddles, not minima).
- There may or may not be additional Goldstone-type zero modes from translation on `C_n` (V5b-T-zero would apply here).
- There is no canonical statement that the "surgery direction" is *one*-dimensional. (For symmetric `C_n`, by reflection symmetry, the saddle may have a 2D unstable manifold.)

So even in the simplest test case, the proposal's dichotomy (G ⊕ E_surg = G ⊕ 1D) is not numerically supported in advance. **Cat C numerical investigation needed, not Cat B candidate.**

*Recommended status:* **OPEN PROBLEM** (W9+). The theorem candidate as stated cannot be proved without (i) a non-circular tame definition (§C.1), (ii) an independent construction of E_surg (§A.2), and (iii) saddle-point Hessian regularity (OP-HMORSE-SADDLE, canonical.md:594, OPEN).

```
CoC chain (negative result):
target: T-MORSE-SURGERY-DICHOTOMY as stated is provable.
prior_anchors: T-PF-A1-SDE Cat A, T-K-Select-PF Cat B, L-HMORSE-LOCAL Cat B (post §A.1 reframe), OP-HMORSE-SADDLE OPEN.
causation_chain (failure path):
  - T-PF-A1-SDE → ergodicity in F_M(G) (I1)
  - I1 + T-K-Select-PF → trajectory visits B_K sectors with prob p_K (I2)
  - I2 → K-jump events occur at sector boundaries (I3)
  - I3 + ??? → Hessian kernel structure at boundaries (BREAK: requires OP-HMORSE-SADDLE, OPEN)
  - Therefore: T-MORSE-SURGERY-DICHOTOMY blocked at I3 → I4 step.
inverse_causation_check:
  - if OP-HMORSE-SADDLE resolved Cat B → theorem becomes Cat C candidate (still requires non-circular tame def).
  - if (C4) preservation between events demonstrated → upgrade path but not yet present.
```

### §E.2 T-SKELETON-PERSISTENCE-CORRESPONDENCE — partially supported, sharper statement available

**Statement (proposal §14):** Tame singular boundary → critical skeleton event ↔ PH H_k birth/death/merge/split event.

**Recovery path.** Drop the proposal's R(u)/S(u) construction; use canonical `B_PersRidge` (T-OP6-B Cat A) directly. Then the correspondence is *already* the persistence stability theorem (Chazal et al.):

> H_0 barcode of `|∇_G u|` field is Lipschitz under bottleneck distance to H_0 barcode of `|∇_G u'|` field, with constant 1.

This is a Cat A statement *already in the literature* (Cohen-Steiner-Edelsbrunner-Harer 2007). What's *not* covered by canonical is: the bijection between skeleton events (as the proposal defines them) and `H_0` ↔ `H_1` PH events. But once R(u)/S(u) are dropped in favor of B_PersRidge, the correspondence is direct.

**Realistic verdict:** Cat A *exists in literature* (PH stability theorem). The proposal's "novel" correspondence claim collapses to a standard result once the redundant R(u) construction is removed.

**Confidence: HIGH** that the correspondence is provable as a Cat A theorem *by citation*, not new mathematics. The proposal's framing of this as a "candidate new theorem" is **overclaim — it is already established**.

*Recommended status:* **Cat A direct via PH stability theorem citation**, no new mathematics needed.

### §E.3 T-WILD-DEGENERACY-EXCLUSION — proof requires explicit coercivity bounds

**Statement (proposal §14):** Under sufficient E_wild and bounded saturating E_ridge, lattice-scale spike / checkerboard / non-persistent artifact cannot survive as bounded-energy critical point.

**Dependencies:**
- E_wild coercivity (§D.2): YES under η > 0, on `1^⊥`.
- E_ridge bounded (§D.1, §D.5): requires bounded φ — but then E_ridge is impotent as a sharpening term (§D.5).
- Critical-point analysis: need `∇E_CSSL = 0` to imply absence of wild configurations.

**Proof sketch (if attempted):**
- Wild configurations have `Σ (Δ_G u_i)² ~ O(n)` (checkerboard mode has `Δ_G u ≈ d·u` per site, so `(Δ_G u_i)² ~ d²`, sum `~ n·d²`).
- E_wild contribution at wild config: `~ η n d²`. Coercivity: as wild-ness increases, energy increases.
- Standard SCC E at wild config: bounded.
- E_ridge bounded.
- Therefore total E at wild config ≥ E_clean - η_0 + η n d² → ∞ as n → ∞.

So **wild configs have unboundedly larger energy** than clean configs for any η > 0 and fixed n. **Wild configs cannot be minimizers above some energy threshold.**

*However*: "cannot be a *critical point*" requires `∇E = 0`, not just "not minimizer". Wild configs CAN be saddle critical points (any quadratic form has critical points at saddles where some directions are unstable but `∇E = 0` is satisfied). So the proposal's claim "no bounded-energy critical point" needs to be sharpened to "no bounded-energy *local minimum*".

**Recovery as Cat B candidate.** Reformulate as:

> *"For η > 0 sufficiently large (η > η*(α, β, n)), no wild configuration (defined by [explicit conditions, e.g., bi-Laplacian > M_wild]) is a local minimum of E_CSSL."*

This is provable via straightforward energy comparison + Hessian PD check at clean minimizers. Cat B candidate (conditional on explicit `η*`). **Confidence: MEDIUM** — proof technique is standard but requires careful constant tracking.

*Recommended status:* **Cat B target** (5–10 sessions to formalize η* lower bound for explicit graph families). NOT Cat A (requires explicit hypothesis on η).

### §E.4 T-SURGERY-ADMISSIBLE-HMORSE — circular and undefined

**Statement (proposal §14):** Surgery-admissible non-uniform critical → active-set Hessian kernel = G ⊕ E_surg + spectral gap perpendicular to (G ⊕ E_surg).

**CRITICAL flaw (circular).** "Surgery-admissible" is defined (§11) as having `ker H_eff^AA = G ⊕ E_surg`. The theorem then says: things with this kernel structure satisfy this kernel structure + spectral gap. The theorem reduces to: *spectral gap holds perpendicular to the kernel*. This is **always true** by definition of "kernel" — `H | (ker H)^⊥` has trivial kernel (i.e., positive eigenvalues if H is PSD; nonzero eigenvalues in general).

**The theorem as stated is vacuous.**

To rescue: replace "surgery-admissible" with an *intrinsic* definition (Tame conditions from §C.1 + independent E_surg construction from §A.2). The theorem then becomes:

> "*For critical configurations satisfying Tame(u^c) (intrinsic conditions on u^c, not on kernel), the active-set Hessian kernel has dimension = dim E_surg^{intrinsic}(u^c) + dim G_residual(u^c) + 0 (no wild kernel directions, by T-WILD-DEGENERACY-EXCLUSION)."*

Even this rescued form requires:
- Tame intrinsic definition: TBD.
- E_surg intrinsic construction (e.g., as normal coordinates to codim-1 strata of `F_M(G)`): TBD.
- G_residual: the Goldstone subspace of the residual symmetry at u^c (canonical T-σ-Lemma-1 framework, Cat A).
- Wild exclusion: needs T-WILD-DEGENERACY-EXCLUSION as a prerequisite (recoverable Cat B per §E.3).

The rescued theorem is then a **3-input composition**: requires Tame definition + E_surg construction + T-σ-Lemma-1 + T-WILD-DEGENERACY-EXCLUSION. All four inputs are either TBD or not-yet-Cat-A.

*Recommended status:* **NOT PROVABLE in current form.** After rescue: Cat C numerical candidate (W9+); requires all four inputs to be at Cat B or better before Cat B promotion.

**Confidence: HIGH** that the theorem as stated is vacuous. **Realist check: this is a definitional defect, not an estimation defect. Severity: CRITICAL.**

### §E.5 Summary table — four theorem candidates

| # | Theorem | Current cat | Realistic cat after fix | Blocker |
|---|---|---|---|---|
| 1 | T-MORSE-SURGERY-DICHOTOMY | Undefined | OPEN PROBLEM | Tame def (circular) + E_surg construction + OP-HMORSE-SADDLE |
| 2 | T-SKELETON-PERSISTENCE-CORRESPONDENCE | Overclaim | Cat A by citation | Drop R(u) construction; use canonical B_PersRidge + PH stability |
| 3 | T-WILD-DEGENERACY-EXCLUSION | Underspecified | Cat B target | Define wild explicitly; η* lower bound |
| 4 | T-SURGERY-ADMISSIBLE-HMORSE | Vacuous (circular) | OPEN PROBLEM | All of the above; reframe non-circularly |

**Net: 0 out of 4 theorem candidates are Cat A/B-promotable in current form. After substantial reformulation: 1 Cat A (by citation), 1 Cat B (target), 2 open problems.**

---

## §F — Risk catalog (Task 6)

### §F.1 Ridge concentration → spike formation?

See §D.5. Answer: under any φ choice, the E_ridge term either does not promote concentration (bounded-saturating), or destabilizes E_bd (linear), or is ill-posed (super-linear). **MAJOR; recoverable with E_ridge redesign.**

### §F.2 PH events differentiable enough for energy embedding?

See §D.3, §D.4, §D.6. Answer: **NO, fundamentally not.** Must be diagnostic only. **CRITICAL; recoverable only by demoting E_pers to diagnostic.**

### §F.3 Graph Morse index — robust definition?

The proposal does not commit to a Morse framework. Three candidates:

1. **Forman discrete Morse (1998):** vector-field-based, defined on cell complexes. Index counts pairs of "matched" cells. Works on simplicial complexes including graphs (1-skeleton). Provable Morse-theoretic relations to PH (Mischaikow-Nanda 2013).
2. **Banchoff PL Morse:** defined on PL functions on simplicial complexes via index counting at vertices. Index = (count of lower neighbors) - (count of higher neighbors) classification.
3. **Persistent-pair language (Edelsbrunner-Harer 2010):** every critical pair (birth, death) in PH is a "saddle" of a specific type; index inferred from filtration order.

These give **different** counts for the same configuration. The proposal must commit to one before "finite Morse index" in §10 is meaningful.

**MAJOR (definitional ambiguity).** Recommended commitment: Forman discrete Morse, as it has direct relations to canonical PH (D-ST-3) and is the standard for graph-based discrete computation.

*Realist check.* This is a definitional choice; once committed, the rest of the proposal can be checked against that choice. Severity: MAJOR (not CRITICAL because it's a tractable choice). Confidence: HIGH that it must be addressed.

### §F.4 True neck saddle vs numerical/lattice artifact discrimination?

This is real, but the answer is already in canonical: **persistence threshold `ρ_pers > 0`** (D-ST-3) distinguishes "true" events (persistence ≥ ρ_pers) from "numerical noise" (persistence < ρ_pers). The proposal's E_pers term is supposed to enforce this; but per §D.3 it cannot be an energy term. **As a diagnostic threshold** (the canonical approach), the discrimination is well-posed.

**MINOR; resolved by canonical D-ST-3 + ρ_pers threshold.**

### §F.5 Soft-cohesion ontology preservation (u_t primitive)?

The proposal's §9 defines S(u) as a *derived* graph-vertex set, function of u. This is consistent with u_t primitive. **HOWEVER**: §12.1 defines E_ridge using ridges, and §13 defines surgery events using S(u). If S(u) is used to **construct an energy term**, then the *form of the energy* depends on a derived quantity from u — this is a *second-order* form of structural inversion (the energy gradient becomes self-referential via S(u)).

This is *not* by itself a violation of u_t primitive (the *primitive* is still u_t), but it does create:
- **Self-referentiality of a derived structure into the energy:** the gradient `∇E_CSSL` depends on derivatives of S(u) w.r.t. u (chain rule), which are *combinatorial* (graph vertex set membership). Not differentiable.
- **Cascading non-analyticity:** any derived combinatorial structure used in energy breaks CN4 + T14.

**MAJOR.** The proposal's energy formulation, even ignoring PH, has this combinatorial-derivation problem from S(u). Compare to canonical: `E_cl` uses `Cl(u)` which is *analytic* in u (sigmoid composition); `E_sep` uses `D(x; 1-u)` which is analytic; `E_bd` uses sums-of-squares, analytic; `E_tr` uses smooth kernels. None of canonical E uses *combinatorial* objects (vertex sets, indicator functions, persistence diagrams) as energy ingredients. The CSSL proposal would be the first.

*Fix:* Energy terms must be analytic in u. Combinatorial diagnostic structures (S(u), R(u), B_PersRidge) are fine as diagnostics, never as energy.

### §F.6 Does CSSL become segmentation theory / free-boundary theory?

The proposal §16D explicitly asks this. Honest answer:

**Risk level: MAJOR.** The CSSL framework, as written:
- Constructs explicit boundary/ridge structures (S(u)).
- Builds energy terms around these structures.
- Reasons about "the boundary's shape" as if it were a geometric object.

This is the *exact pattern* of free-boundary theory (Modica-Mortola, Cahn-Hilliard) and image-segmentation theory (Mumford-Shah, Chan-Vese). Canonical SCC strongly distinguishes itself from these via §10 ("The theory does not reduce to segmentation, clustering, or tracking", canonical.md:861), and CN10 prohibits reductive identification with such frameworks.

If CSSL adopts:
- Explicit ridge/boundary structures as energy inputs,
- Sharp-interface limits,
- Free-boundary regularity language,

then it effectively *is* free-boundary theory under canonical CN10 prohibition. **This is the structural-philosophical risk most cited in §16D.**

*Realist mitigation.* The risk is real but can be mitigated by:
1. Keeping all energy terms analytic in u (§F.5 fix).
2. Treating S(u) as a *diagnostic only* (§B.1 + §F.4 fix).
3. Framing CSSL contributions as "characterizing the static and dynamic behavior of u_t at codim-1 K-sector boundaries within `F_M(G)` under T-PF-A1-SDE", not as "introducing boundary regularity as a primitive".

With all three mitigations, CSSL becomes a *consistent extension* (CN10-compliant) rather than a *reductive collapse*. **Without** the mitigations, CSSL drifts into free-boundary theory. **Confidence: HIGH** that mitigations are necessary; **MEDIUM** that they are sufficient.

### §F.7 Compatibility with canonical CN10 (no reductive reduction)?

CN10 (canonical.md:2204): *"Comparing SCC's operators or structures to those of other frameworks ... is permitted and encouraged. Reducing SCC to any of these frameworks — claiming it 'is just' Allen-Cahn, or 'is just' clustering, or 'is just' phase-field theory — is prohibited. The comparison is contrastive, not reductive."*

The CSSL proposal references "Allen-Cahn / Modica-Mortola류" (§0, §5) and "phase-field" (§0) language. Per the system prompt requirement, these MUST be *contrastive* (standard tools for comparison), NOT reductive (framework reductions).

*Audit of CSSL language:*
- "Allen-Cahn / Modica-Mortola류의 phase-field처럼 부드러운 diffuse interface를 가진다" (§0): **Contrastive** ✓ (compares CSSL boundary structure to AC profile shape).
- "Allen-Cahn류 scaling에서 boundary 폭은 √(α/β)" (§3.2): **Borderline.** This uses AC scaling to *derive* properties of the CSSL energy — verges on reductive. Should be reframed as: "Under E_bd alone (which structurally resembles Allen-Cahn at the smoothness sub-term), boundary width scales as √(α/β); this scaling is preserved under (α, β) → (sα, sβ)."
- Surgery/persistence-homology language (§9-§14): These are *standard topological tools*, contrastively cited, not reductively claiming CSSL = persistence-homology theory.

**Net CN10 compliance:** Mostly OK; one phrase in §3.2 should be rewritten to make the contrastive vs reductive boundary explicit. **MINOR.**

### §F.8 Additional risks (gap analysis)

**Found via Phase 4 gap analysis (what is MISSING from the proposal):**

| # | Missing element | Severity |
|---|---|---|
| 1 | No specification of which Morse framework (Forman vs Banchoff vs persistence) | MAJOR (§F.3) |
| 2 | No construction of `E_surg` independent of "kernel of Hessian" | CRITICAL (§A.2, §E.4) |
| 3 | No definition of "induces local topology change" for S(u) | MAJOR (§B.4) |
| 4 | No analysis of E_pers analyticity (just deferred to §16D question) | CRITICAL (§D.3) |
| 5 | No connection to OP-HMORSE-SADDLE (the actually-relevant OPEN problem) | MAJOR (§A.1) |
| 6 | No analysis of how T-PF-A1-SDE dynamics generate K-jump events at codim-1 boundaries | MAJOR (§A.3) |
| 7 | No regime conditions analogous to canonical D-HMORSE-LOCAL (C1)–(C5) | MAJOR (§A.4) |
| 8 | No numerical sketch / anchor (canonical Cat B/C always has explicit numerical anchor) | MAJOR (canonical standard) |
| 9 | No discussion of when CSSL applies vs when V5b-T-zero applies (overlapping regimes) | MAJOR (§A.1) |
| 10 | No CoT/CoC structure (W8-Day3 introduced these as enforcement standard) | MINOR (formatting) |

---

## §G — Cat assignment recommendation (Task 7)

### §G.1 Per-element Cat assignment

| Element | Proposal label | Recommended honest Cat | Rationale |
|---|---|---|---|
| Conceptual transition (§A.1 reformulated) | "extend ker H_eff^AA from G to G ⊕ E_surg" | **OPEN PROBLEM** | Requires (i) reframing as saddle problem (not L-HMORSE-LOCAL extension), (ii) independent E_surg construction. Belongs to **OP-HMORSE-SADDLE** family (canonical.md:594). |
| Critical skeleton S(u) | New construction | **Drop in favor of canonical B_PersRidge** (Cat A via T-OP6-B) | Proposal's R(u)/S(u) reinvents canonical persistence-ridge construction. |
| Tame vs wild dichotomy | New definition | **Cat C numerical investigation** | Requires Forman Morse commitment + intrinsic conditions; tractable in 5–10 sessions of W9+ work. |
| E_ridge = -κ Σ φ(r_i) | New energy term | **REJECT current form** | Sign-structure issue (§D.1). Reformulation possible (§D.1 fix) but speculative; current form not promotable. |
| E_wild = η Σ (Δ_G u_i)² | New energy term | **Cat B target** under η ≪ β | Well-posed bi-Laplacian energy. Coercive, PSD, analytic. Needs parameter constraint analogous to T8-Core. |
| E_pers PH-based | New energy term | **REJECT as energy; keep as diagnostic** | Fundamentally incompatible with CN4 + T14 + T-PF-A1 analyticity cascade (§D.3). |
| T-MORSE-SURGERY-DICHOTOMY | Theorem candidate | **OPEN PROBLEM** | Requires Tame def + E_surg construction + OP-HMORSE-SADDLE; no individual ingredient at Cat B yet. |
| T-SKELETON-PERSISTENCE-CORRESPONDENCE | Theorem candidate | **Cat A by citation** | Persistence stability theorem (Cohen-Steiner et al. 2007) covers it once R(u)/S(u) is dropped. |
| T-WILD-DEGENERACY-EXCLUSION | Theorem candidate | **Cat B target** | Provable via energy comparison once "wild" defined explicitly and η* lower bound established. 5–10 sessions. |
| T-SURGERY-ADMISSIBLE-HMORSE | Theorem candidate | **OPEN PROBLEM (vacuous in current form)** | Requires non-circular Tame + E_surg construction. |

### §G.2 What can enter canonical CV-1.19?

**Direct answer: NONE of CSSL in its current form.**

W8-Day3 99_summary already identified Decision A's CV-1.19 SEAL-prep candidates: S1 (Łojasiewicz `c_G` Cat B verified) + S3 (full SCC kernel-mult identity Cat A on standard regimes). Those are independently grounded by W8-Day3 work and are *not* affected by the CSSL proposal. They should proceed to CV-1.19 SEAL-prep on their own merits.

**CSSL recommended pipeline:**
1. **W9 immediate (1 session):** Reframe CSSL as saddle-problem extension to OP-HMORSE-SADDLE (not L-HMORSE-LOCAL extension). Update working file to reflect §A.1 reframing.
2. **W9-W10 (2-3 sessions):** Demote E_pers to diagnostic (§D.3). Redesign or drop E_ridge (§D.1, §D.5). Commit to Forman discrete Morse (§F.3). State explicit conditions for "tame" (§C.1).
3. **W10-W12 (3-5 sessions):** Numerical investigation of T-WILD-DEGENERACY-EXCLUSION Cat B target (η* lower bound for explicit graph families).
4. **W12+ (5-10 sessions):** Independent construction of E_surg as codim-1 K-sector boundary normal coordinates. If successful, attempt T-MORSE-SURGERY-DICHOTOMY as Cat C numerical candidate.
5. **W15+ (open horizon):** OP-HMORSE-SADDLE attack via CSSL framework. If successful, T-SURGERY-ADMISSIBLE-HMORSE becomes Cat B candidate.

This is a **5–15 session horizon** for the CSSL framework to produce *one* Cat B canonical row + several supporting Cat C anchors. The current proposal **massively underestimates the gap** between concept-handoff and canonical-promotion.

### §G.3 Pre-existing OP catalog impact

Reviewing CSSL against canonical OPEN problems (theorem_status.md):

| OP | Status | CSSL impact |
|---|---|---|
| OP-HMORSE-SADDLE (saddle-point Hessian regularity; canonical.md:594) | OPEN | **CSSL is most relevant to this**, *not* L-HMORSE-LOCAL-A. Reframe required. |
| OP-HMORSE-LOCAL-A (Cat A path for L-HMORSE-LOCAL) | OPEN | NOT CSSL's target; orthogonal direction. |
| OP-0008 σ^A K-jump non-determinism | Cat C partial | CSSL's "merge/split events" relate; canonical has Cat B for centroid+orientation (Session W). |
| OP-0009 Multi-Formation Ontological Foundations | OPEN | Touched if CSSL claims about K_act-jump structure; sub-OP-0009-K already RESOLVED via Commitment 16 K_field/K_act decomposition. |
| OP-0021 T_* registration (Routes A/B DEPRECATED CV-1.18; Route C only) | OPEN with sub-OPs | CSSL "surgery events" need temporal dynamics → depend on T_* → blocked by OP-0021 progress. |
| OP-0005-DYN Kramers transition rates | OPEN (W9+) | Direct dependence: CSSL "topology events as Kramers crossings" relies on this. |

**Net:** CSSL straddles 5 OPEN canonical OPs, none of which it currently advances individually. A focused attack on OP-HMORSE-SADDLE *via* CSSL framework is a plausible direction, but requires the full §G.2 pipeline to land.

---

## §H — Integration recommendations for CV-1.19+ SEAL pipeline

### §H.1 CV-1.19 (W8-Day4 next) — keep CSSL OUT

The proposal as written is not CV-1.19 SEAL-ready. Recommended CV-1.19 content (per W8-Day3 99_summary Decision A):

- S1 (Łojasiewicz c_G Cat B verified) → canonical §13 Cat B row insertion.
- S3 (full SCC kernel-mult identity Cat A on standard regimes) → canonical §13 Cat A row insertion (with case A/B unconditional + case C with H-INV explicit).

These are independent of CSSL and have completed verification.

### §H.2 CSSL-related additions to working layer ONLY

Recommended working-layer (THEORY/working/cssl/) state after W8-Day3 evening:

- `00_concept_handoff.md` (existing, user-prepared).
- `01_critic_evaluation.md` (this file).
- `02_cssl_reframe_OP_HMORSE_SADDLE.md` (W9 candidate — reframe per §A.1).
- `03_energy_redesign_post_critic.md` (W9-W10 candidate — drop E_pers, redesign E_ridge per §D.1, §D.3).
- `04_tame_definition_intrinsic.md` (W10 candidate — Forman commitment + intrinsic conditions per §C.1).

**No canonical/* edits until at least §G.2 step 3 completed.**

### §H.3 Working-layer trajectory recommendation

CSSL is a **multi-month research line**, not a 1-2 session canonical promotion candidate. Treat it accordingly:

- **Month 1 (W9-W12):** Reframe + redesign + define. Goal: produce 1 well-defined Cat B target (T-WILD-DEGENERACY-EXCLUSION) + 1 well-defined OPEN problem (T-SURGERY-ADMISSIBLE-HMORSE reframed for OP-HMORSE-SADDLE).
- **Month 2-3 (W13-W20):** Numerical investigation + first Cat B promotion attempt.
- **Month 3+ (W21+):** OP-HMORSE-SADDLE attack via CSSL framework, if first Cat B lands.

### §H.4 Distinction from CV-1.19 Cat A/B promotion candidates

CV-1.19 (W8-Day4 candidate, per Decision A) already has plenty of canonical-promotable content. CSSL must not delay or distract from CV-1.19 SEAL execution. Critic recommendation: **CSSL fork to its own working track, independent of CV-1.19 pipeline**. Annotate hypothesis_tree.md HT-3.10 with CSSL as a *long-horizon research line*, status OPEN, not blocker for any current SEAL.

---

## §I — Explicit risk-mitigation roadmap (5-10 sessions of W9+ work)

### §I.1 Sequenced session plan

| Session | Mandate | Output | Gate |
|---|---|---|---|
| **W9-S1** | §A.1 Reframe: CSSL → OP-HMORSE-SADDLE saddle-problem | `02_cssl_reframe_OP_HMORSE_SADDLE.md` | Critic sign-off that L-HMORSE-LOCAL is no longer the comparison target. |
| **W9-S2** | §F.3 Forman Morse commitment + §C.1 Tame intrinsic definition | `04_tame_definition_intrinsic.md` | Definition is non-circular and uses only canonical anchors. |
| **W9-S3** | §D.3 Demote E_pers to diagnostic | Edit `00_concept_handoff.md` §12.3 with explicit "diagnostic only" marker | CN4 analyticity preserved. |
| **W9-S4** | §D.1 Redesign or drop E_ridge | `03_energy_redesign_post_critic.md` | Either (a) explicit redesign with §D.1 corrections OR (b) drop E_ridge entirely. |
| **W10-S1** | §E.2 Cat A by citation: persistence stability for skeleton ↔ PH correspondence | Working-file proof sketch citing Chazal et al. 2009 + Cohen-Steiner et al. 2007 | Direct citation chain, no new mathematics. |
| **W10-S2** | §E.3 Cat B target: T-WILD-DEGENERACY-EXCLUSION with explicit η*(α, β, n) | `05_wild_exclusion_cat_b_target.md` | Explicit lower bound derivation + numerical sanity check on canonical regimes. |
| **W10-S3** | §A.2 Cat C numerical: E_surg as codim-1 K-sector boundary normal | `06_e_surg_codim1_construction.md` | Construction is independent of "Hessian kernel"; uses T-K-Select-PF + T-PF-A1-AR codim-1 boundary geometry. |
| **W11-S1** | Integration audit: CSSL ↔ canonical CN4, CN10, CN12, Commitment 5 (4 distinct E terms), Commitment 12 (C_t derived) | `07_cssl_canonical_compatibility.md` | All canonical commitments preserved; no reductive collapse to free-boundary or Allen-Cahn. |
| **W11-S2** | Cat C numerical experiments: tame vs wild dichotomy on canonical graphs (P_3, C_n, K_n, T^2_L, free-BC grid) | `CODE/experiments/exp_cssl_tame_dichotomy.py` + results MD | Numerical anchor for any future Cat B claim. |
| **W12-S1** | First Cat B promotion attempt: T-WILD-DEGENERACY-EXCLUSION → working Cat B candidate | `working/cssl/promotion_draft_v1.md` | Critic re-review (this critic agent re-invoked). |

### §I.2 Stop conditions

If at any session-gate the prerequisite fails, the CSSL line should pause and accept the failure honestly:

- W9-S1 fail (reframing impossible): CSSL withdrawn; no further work.
- W9-S2 fail (Tame circular regardless): CSSL withdrawn.
- W10-S2 fail (η* unattainable): T-WILD-DEGENERACY-EXCLUSION downgraded to Cat C only.
- W11-S2 fail (numerical evidence shows wild configs ARE stable critical points): T-WILD-DEGENERACY-EXCLUSION refuted; CSSL pivots or withdrawn.

These are honest failure paths consistent with the SCC theory's negative-results methodology (per user memory: "user values substantive refutations").

### §I.3 Avoid known anti-patterns

Based on CSSL-adjacent prior failures registered in canonical:

- **Avoid F-1 / M-1 / MO-1 pattern.** These were "Foundational vacuity" problems that took W4 to resolve (T-PreObj-1 family). Don't re-introduce vacuity by defining CSSL primitives circularly.
- **Avoid V5b iteration trap.** V5b underwent 8 iterations before reaching canonical (V5b-T + V5b-F + V5b-T-zero). CSSL is similarly speculative; budget for 5+ rejection-revise cycles.
- **Avoid Phase 5 / `c_G` normalization-mismatch pattern.** Today's Priority 1 found a 2.09 vs 1.171 discrepancy due to W''(1/2) convention. CSSL must commit to one convention (CV-1.18 I6 W''(1/2) = -1) and not silently switch.
- **Avoid retraction #2 pattern (Model A → Model B both wrong).** Today's Priority 3 showed both Model A and Model B are refuted for SCC dynamics. CSSL must not assume "if A doesn't work, B obviously works" — both can fail.

### §I.4 Critic re-review schedule

Recommended critic re-invocations:

- After **W9-S2** (Tame definition committed): re-check non-circularity.
- After **W10-S2** (T-WILD-DEGENERACY-EXCLUSION η* derivation): re-check coercivity argument.
- After **W11-S1** (canonical compatibility audit): re-check CN compliance.
- After **W12-S1** (first Cat B promotion attempt): full critic re-review with same protocol as this evaluation.

---

## §J — Self-audit and realist check log

Per critic protocol Phase 4.5 + 4.75:

**Self-audit (re-read findings before finalizing):**

| Finding | Confidence | Author refutable? | Flaw/preference? | Action |
|---|---|---|---|---|
| §A.1 (canonical misdescription) | HIGH | NO — verified against canonical.md:1934–1944 | FLAW | Keep at CRITICAL. |
| §D.1 (E_ridge sign conflict) | HIGH | NO — algebraic identity §B.1 | FLAW | Keep at MAJOR. |
| §D.3 (E_pers analyticity) | HIGH | NO — PH stability theorem standard | FLAW | Keep at CRITICAL. |
| §E.4 (T-SURGERY-ADMISSIBLE-HMORSE vacuous) | HIGH | NO — definitional circularity in §10 condition 6 | FLAW | Keep at CRITICAL. |
| §F.3 (Morse framework undefined) | HIGH | YES if author specifies offline | FLAW | Keep at MAJOR. |
| §F.5 (combinatorial S(u) in energy) | MEDIUM | YES if author redesigns | FLAW | Keep at MAJOR. |
| §B.3 (R(u) local-max ambiguity) | MEDIUM | YES if author clarifies | FLAW | Keep at MAJOR. |
| §E.2 (T-SKELETON-PH-CORRESPONDENCE overclaim) | HIGH | NO — citation available | FLAW (but overclaim, downgrade direction) | Downgrade: actually a *credit* to author (correspondence holds, but trivially via citation). |
| §F.6 (segmentation drift risk) | MEDIUM | YES under §F.6 mitigations | PREFERENCE-ADJACENT (depends on framing) | Keep at MAJOR with mitigation roadmap. |
| §B.2 (A(u) notation conflict) | HIGH | YES trivially (rename) | PREFERENCE | Downgrade to MINOR. |

After self-audit: 3 CRITICAL (§A.1, §D.3, §E.4), 4 MAJOR (§D.1, §F.3, §F.5, §F.6), several MINORs. Confirmed.

**Realist check (Phase 4.75) — pressure-test severity:**

| Finding | Realistic worst case | Mitigating factors | Detection speed | Inflation check? | Action |
|---|---|---|---|---|---|
| §A.1 | Author proceeds with wrong target lemma; entire framework attacks wrong canonical surface | None (the target is structurally wrong) | Would be caught by next critic re-review (any reviewer reading L-HMORSE-LOCAL) | NO inflation | Stays CRITICAL |
| §D.1 | Author publishes E_ridge that anti-stabilizes E_bd; numerical experiments would show "ridges destabilize but boundary becomes rough" | Numerical experiment would catch this immediately | Hours-days under canonical numerical anchor protocol | NO inflation | Stays MAJOR (not CRITICAL because numerical detection is fast) |
| §D.3 | Author publishes E_pers; CV-1.19 SEAL pipeline crashes due to T14 Łojasiewicz Cat A breakage | All downstream Cat A/B theorems (T-PF-A1-SDE, L-HMORSE-DECOMP, etc.) would lose anchor | Detection would be *slow* (latent until someone re-verifies T14 chain) | NO inflation | Stays CRITICAL — destroys >5 Cat A theorems' grounding |
| §E.4 | Vacuous theorem "proved"; no actual content | Standard mathematical refereeing catches vacuous tautology | Fast (any cold reviewer) | NO inflation | Stays CRITICAL — definitional defect, not estimation |
| §F.3 | Author uses Forman; another reader assumes Banchoff; cross-paper confusion | Commit to one framework, document choice | Fast once committed | NO inflation | Stays MAJOR |
| §F.5 | Combinatorial chain rule fails at every persistence transition; E gradient undefined | Demote S(u) to diagnostic | Fast (any analyticity check) | NO inflation | Stays MAJOR |
| §F.6 | CSSL drifts into free-boundary theory; CN10 prohibits | Mitigation roadmap §F.6 mostly tractable | Slow (philosophical/structural, not numerical) | Some inflation possible (free-boundary is broad church); keep at MAJOR with mitigation roadmap | Stays MAJOR |

Realist downgrades: NONE. All CRITICAL/MAJOR findings survive realist check at original severity. **No mitigation rationale supports downgrade.**

---

## §K — Adversarial mode summary

Started in THOROUGH mode (Phase 1 + Phase 2). After Phase 2 surfaced 1 CRITICAL (§A.1) + 3 MAJOR (§D.1, §D.3 escalated to CRITICAL in Phase 4, §F.3) findings, escalated to ADVERSARIAL mode for Phases 3-5.

ADVERSARIAL mode discoveries (issues not initially in scope):

1. **§F.5 (combinatorial S(u) → non-analytic energy chain)** — discovered by checking canonical CN4 in context of *all* energy ingredients, not just E_pers.
2. **§F.7 (CN10 contrastive vs reductive boundary)** — discovered by checking proposal language against canonical CN10 statement word-by-word.
3. **§E.2 (T-SKELETON-PH-CORRESPONDENCE overclaim)** — discovered by checking PH stability theorem literature; proposal "novel theorem" is actually a citation.
4. **§B.1 (r_i = canonical E_bd integrand)** — discovered by algebraic identity check against canonical §8.4 ordered-pair sum convention.

ADVERSARIAL mode did NOT manufacture issues; all four are genuine and survive self-audit + realist check.

---

## §L — Open questions (unscored, for author to consider)

These are speculative directions or under-confidence observations, not findings:

1. **Is there a defensible CSSL that lives entirely at the diagnostic layer?** Cosmetic version: drop E_ridge, E_wild, E_pers from the energy; keep all CSSL constructions (S(u), tame/wild dichotomy, surgery event detection) as *diagnostics*. Then CSSL becomes a "topology-event observer" framework parallel to D-ST-3 K_act + B_PersRidge boundary. Much less ambitious, but canonical-compatible. (W11+ candidate.)
2. **Is there a connection between proposal §6 "controlled singular skeleton" and canonical T-OP6-B `H4: κ_max · ξ ≤ 0.1`?** T-OP6-B uses bounded interface curvature as a condition; CSSL's "tame" condition includes bounded curvature. Cross-check could be productive.
3. **The CSSL §11 surgery event table (birth/death/merge/split/hole birth/hole death) maps to which canonical OP-0008 sub-problems?** OP-0008 has 4 sub-problems (CONT, MERGE, SPLIT, DIST, canonical.md:581 + theorem_status.md). Cross-map could clarify which sub-OPs CSSL addresses (merge/split → OP-0008-MERGE/SPLIT canonical Cat B; birth/death/hole-events → likely OP-0008-DIST or new sub-OPs).
4. **Is "surgery-admissible" weaker than "Morse-non-degenerate"?** In standard Morse theory, a critical point is *non-degenerate* iff its Hessian is invertible. The CSSL "surgery-admissible" allows finite-dimensional kernel of known structure. This is a *degenerate Morse* concept, related to *Morse-Bott* theory (kernel = tangent to critical manifold). Could CSSL be reformulated via Morse-Bott on the K-sector boundary? (W13+ candidate research direction.)
5. **What is the relationship between E_surg and "Goldstone modes at K-jump"?** If sector transitions break some residual symmetry (e.g., translation-permutation between K=2 and K=1 single-formation), the resulting "Goldstone direction at sector boundary" might coincide with E_surg. T-σ-Lemma-1 (Cat A) machinery might apply. Worth investigating.
6. **Could ζ E_pers be replaced by ζ · BottleneckDist²(Bars(u), Bars_target)?** Persistence-image / persistence-landscape distance to a *target* barcode is continuous (Lipschitz) but still non-analytic. Probably not useful for E, but might work as a *constraint* (Bottleneck(Bars(u), Bars_target) ≤ ρ).

---

## §M — One-line summary for parent agent

CSSL proposal is **REVISE (substantial)**: 1 genuinely interesting research line (Cat C numerical investigation of wild-exclusion + Cat B target after fixes) hidden under 3 CRITICAL flaws (wrong canonical target, PH-as-energy breaks CN4, circular tame definition) and 4 MAJOR flaws (E_ridge sign-structure, S(u) combinatorial in energy, Morse framework undefined, segmentation-drift risk). **Worth pursuing with substantial modifications** as a 5-15 session W9+ working-layer research line; **NOT** a CV-1.19 SEAL-prep candidate; **NOT** worth deferring or rejecting outright.

---

*W8-Day3 evening critic evaluation complete. CV-1.18 SEALED untouched. No canonical/* edits. CSSL recommended fork to working/cssl/ research line, independent of CV-1.19 SEAL pipeline. Re-review schedule per §I.4.*
