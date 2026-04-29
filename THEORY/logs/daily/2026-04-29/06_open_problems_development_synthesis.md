# 06_open_problems_development_synthesis.md — Day 3 Deepening Pass: Synthesis

**Session:** 2026-04-29 (W5 Day 3, post-Block-5 deepening pass)
**Target:** Synthesize the substantive findings from `04_D6b_sigma_trajectory_development.md` and `05_NQ198_V5bTprime_PN_barrier_attempt.md`. Identify which open problems advanced; new NQ spawns; updated W6+ priority order; impact on user-decision queue (D-1..D-6b + new D-7 proposal).
**This file covers:** §1 What advanced; §2 New NQ spawn inventory; §3 Updated W6+ priority order; §4 Impact on `01_canonical_promotion_queue_review.md` user-decision queue; §5 Day 4 morning suggested actions; §6 Hard constraint verification.
**Depends on reading:** `04_D6b_sigma_trajectory_development.md` (D-6b development), `05_NQ198_V5bTprime_PN_barrier_attempt.md` (V5b-T' Cat A attempt), `00_phase9_10_reconciliation.md`, `01_canonical_promotion_queue_review.md`.

---

## §1. What Advanced (Day 3 Deepening Pass)

### §1.1 D-6b Dynamic σ_multi^A(t) Trajectory — UPGRADED

**Status before deepening (per `01_*` §2 D-6b)**: "Cat B sketch only — recommend defer indefinitely. V3 used simplified σ-tuple; rigorous K-jump theory not addressed."

**Status after `04_*` deepening**: **Cat B target with structured framework**. Three lemmas + one proposition + one synthesis theorem:

- **Lemma 4.2.1** (smooth-segment piecewise constancy): $\sigma_{\mathrm{multi}}(t)$ is piecewise constant on smooth segments via Kato-Rellich + Wigner-von Neumann.
- **Lemma 4.4.1** (K-jump left/right limits + σ^A non-determinism): both limits exist; $\Phi: \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ is **non-deterministic in $\sigma^A(t^{*-})$ alone** — substantive negative result requiring merger-geometry data.
- **Proposition 4.5.1** (σ^D partial determinism): cohomology pull-back along merger embedding modulo symmetry emergence.
- **Theorem 4.6.1** (synthesis): càdlàg trajectory characterization, Cat B target.

**Cat A path** (5 weeks+): NQ-242 full Hessian σ-tuple time-series + NQ-242b avoided-crossing accumulation + NQ-242c explicit non-determinism construction + NQ-242d symmetry emergence.

### §1.2 V5b-T' PN-Barrier Cat A — PARTIAL DERIVATION + FAILURE ANALYSIS

**Status before deepening (per `2026-04-28/11_*` §4.1)**: Heuristic formula $\mu \approx A_{\mathrm{R3b}} \cdot \beta \cdot |\partial S|/\xi_0$ proposed by analogy to Peierls-Nabarro dislocation theory. $A_{\mathrm{R3b}}$ undetermined.

**Status after `05_*` deepening**: **Cat B sketch with diagnosed failure mode**. Sharp-interface + discrete lattice hybrid derivation gives:
$$\mu_{\mathrm{Gold}}^{\mathrm{V5b-T'}} \approx 2\alpha = 2\beta\xi_0^2 \tag{6.1}$$
**independent of $|\partial S|$**. Matches empirical magnitude at NQ-173 setup ($\mu \in [1, 4]$ observed; $\mu \approx 2$ predicted) but **disagrees with Phase 3 heuristic on cluster-mass scaling**.

**This is a substantive negative result**: Phase 3 V5b-T'-(c) over-claims $|\partial S|$ dependence; rigorous derivation suggests scaling is mass-independent.

**Cat A path** (3-7 weeks): NQ-198b (WKB + tight-binding), NQ-198c (discrete Allen-Cahn lattice correction), NQ-198d (corner-saturation regime corrections).

**Decisive numerical test** (NQ-198a, ~30 min compute): vary cluster mass at fixed $\beta, \xi_0$ to confirm/refute mass-independence prediction.

### §1.3 What Did NOT Advance (Honest Inventory)

- **NQ-217 (continuum limit Γ-convergence)**: not touched.
- **NQ-200 (non-involution canonical iso K ≥ 3)**: not touched.
- **NQ-244 (3D LSW α at $T^3_{15}$ K=10)**: not touched.
- **OP-0001..OP-0007**: untouched (per Day 3 hard constraints).
- **F-1 / M-1 / MO-1**: untouched (single-formation; deepening was multi-formation focused).

### §1.4 Methodological Note: Negative Results Are Substantive

Both `04_*` and `05_*` produced **substantive negative results**:

- `04_*`: σ^A K-jump inheritance is **non-deterministic in σ^A alone** (Lemma 4.4.1c).
- `05_*`: V5b-T' PN-barrier scaling is **independent of $|\partial S|$** (Phase 3 heuristic over-claims).

These are not "failures to prove"; they are **discoveries that the original heuristic claims were quantitatively wrong or qualitatively incomplete**. This is exactly the kind of progress that meta-prompt §7 (rigorous failure analysis) calls for, and it has implications for D-5 / D-6b user decisions (see §4 below).

---

## §2. New NQ Spawn Inventory

| NQ | Subject | Cat target | Effort | Priority | Spawned in |
|---|---|---|---|---|---|
| **NQ-198a** | V5b-T' Goldstone mass-dependence numerical test | Cat B test | ~30 min compute | **HIGH (W6 Day 1)** | `05_*` §7 |
| **NQ-198b** | V5b-T' Cat A via WKB + tight-binding | Cat A | 3-5 weeks | MEDIUM (W7+) | `05_*` §7 |
| **NQ-198c** | V5b-T' Cat A via discrete Allen-Cahn lattice | Cat A | 2-4 weeks | MEDIUM (W6-W7) | `05_*` §7 |
| **NQ-198d** | V5b-T' corner-saturation corrections | Refinement | 1-2 weeks | LOW (W7+) | `05_*` §7 |
| **NQ-242** | σ_multi^A(t) full Hessian time-series + rigorous K-jump | Cat A | 4-6 weeks | **HIGH (W6)** | `04_*` §6 |
| **NQ-242b** | Avoided-crossing non-accumulation rigorous proof | Cat A refinement | 1-2 weeks | LOW (W7+) | `04_*` §6 |
| **NQ-242c** | σ^A non-determinism explicit construction | Cat A | 2-3 weeks | MEDIUM (W6+) | `04_*` §6 |
| **NQ-242d** | σ^D symmetry-emergence characterization | Cat A | 2-3 weeks | MEDIUM (W6+) | `04_*` §6 |
| **NQ-247** | V5b-T'/V5b-F cluster-hop dynamics | Cat B | 1-2 weeks (numerical) | MEDIUM (W6+) | `04_*` §6 |
| **NQ-248** | Multi-formation Morse stratification | Cat A | 6-10 weeks (theoretical heavy) | LOW (W7+) | `04_*` §6 |

**Total new spawns: 10** (substantive open problems with explicit Cat targets and effort estimates).

**Cf. Day 2 cumulative spawns: 57.** Day 3 deepening adds 10, all directly tied to the development in `04_*` and `05_*`.

---

## §3. Updated W6+ Priority Order

Per Day 3 deepening, the W6 morning priorities (post-CV-1.5.1 release if approved) should be:

### Tier 1 (W6 Day 1, immediate post-canonical merge)

1. **NQ-198a** (~30 min): Resolve V5b-T'-(c) mass-dependence ambiguity. Decisive between §4 derivation and Phase 3 heuristic. Information-cheap.
2. **NQ-244** (~1-2h): 3D LSW α at $T^3_{15}$ K=10 — Phase 10 V5 insufficient-statistics resolution. Yields publishable α value for Paper §4.5.5.

Both are numerical, fit in W6 Day 1 morning.

### Tier 2 (W6 Days 2-5)

3. **NQ-242** (full Hessian σ-tuple time series + rigorous K-jump): foundational for D-6b Cat A path.
4. **NQ-242c** (σ^A non-determinism explicit): refines Theorem 4.6.1 Lemma 4.4.1(c).
5. **NQ-198c** (discrete Allen-Cahn): closer to Cat A for V5b-T'-(c).

### Tier 3 (W7+)

6. NQ-198b (WKB tight-binding).
7. NQ-242b (avoided-crossing accumulation).
8. NQ-242d (σ^D symmetry emergence).
9. NQ-247 (cluster-hop dynamics).
10. NQ-198d (corner corrections).
11. NQ-248 (multi-formation Morse).

### Carried from Day 2 / earlier

- NQ-174b/c/d/e (ζ_*(d, G, c) analytic + 1D cycle extended sweep + ζ=0.45 anomaly).
- NQ-200 (non-involution canonical iso K ≥ 3).
- NQ-217 (continuum limit Γ-convergence).
- NQ-229b (hybrid γ optimal characterization).

---

## §4. Impact on User-Decision Queue

### §4.1 D-3 V5b-F mechanism rider — UNCHANGED

Per `00_*` §2 D-3, V5b-F static mechanism FINAL. `05_*` §8.1 confirms: V5b-F text in `2026-04-28/01_*` §3.4 cites $\mu \in [1, 4]$ as **empirical observation** (NOT functional-form claim); no over-claim. **No D-3 text revision required.**

### §4.2 D-5 V5b-T' canonical entry — TEXT REVISION RECOMMENDED

Per `05_*` §5.3 + §8.2:

**Original V5b-T'-(c) text** (from `2026-04-28/20_*` Part 1):
> *μ_Gold^lifted ≈ A_R3b · β · (cluster perimeter)/ξ_0 (regime R3b). Empirically: O(β) magnitude.*

**Recommended replacement**:
> *PN-barrier-lifted eigenvalue magnitude: μ_Gold^lifted ~ O(α) = O(β · ξ_0²). Empirically O(β) at NQ-173 setup (β=4, ξ_0=0.5; observed range 1-4). [CAVEAT: |∂S| dependence currently uncertain — Phase 3 heuristic suggested μ ∝ |∂S|/ξ_0; Day 3 §4 derivation suggests μ ≈ const independent of |∂S|; mass-dependence test NQ-198a W6+ resolves.]*

**Updated D-5 options (revised from `01_*` §2 D-5)**:
- **D-5-A1 (revised)**: Approve D-5 with revised V5b-T'-(c) text per §4.2 above. Cat B target with explicit mass-dependence open caveat. Recommended.
- **D-5-A2**: Approve D-5 with original Phase 3 text but flag NQ-198a as urgent W6 priority. Less honest about uncertainty.
- **D-5-D1**: Defer D-5 to W6 Day 1 after NQ-198a numerical test — only ~30 min delay, then merge with confirmed scaling.

**Day 3 deepening recommendation**: **D-5-D1** (short-defer pending NQ-198a). Reasons:
- 30-min numerical test resolves the question definitively.
- Avoids canonical edit + erratum cycle (canonical merge with caveat → erratum after numerical test).
- Maintains canonical-content quality standard.

If user prefers immediate merge: **D-5-A1** (revised text with explicit caveat).

### §4.3 D-6b Commitment 14-Multi dynamic — UPGRADED

Per `01_*` §2 D-6b: original recommendation was "DEFER INDEFINITELY (Cat B sketch only)".

Per `04_*` §7.3 deepening:

**Updated D-6b options**:
- **D-6b-1**: Approve D-6b for CV-1.5.1 with the augmentation per `04_*` §5.2 (~10-15 lines, leaner than original ~20-30 estimate). Cat B target with explicit non-determinism caveat — Theorem 4.6.1 framework.
- **D-6b-2 (RECOMMENDED, REVISED)**: Defer D-6b but with **shorter horizon** — W6+ via NQ-242. Path B (rich σ-augmentation) becomes a clear research goal. Cat B target → Cat A in CV-1.6 single canonical edit.
- **D-6b-3**: Defer D-6b indefinitely. (Original recommendation; superseded by Day 3 deepening.)

**Day 3 deepening recommendation**: **D-6b-2** (shorter-horizon defer). Reasons:
- Theorem 4.6.1 Cat B target framework is canonically draftable but premature.
- W6+ NQ-242 will refine to Cat A; cleaner to do single canonical edit.
- Still mature enough that user *could* approve D-6b-1 if they prefer to capture the framework now.

### §4.4 D-7 (NEW PROPOSAL): NQ-198a Urgent W6 Spawn

Per `05_*` §8.3:

**D-7 (NEW)**: Authorize NQ-198a (V5b-T' mass-dependence numerical test) as **W6 Day 1 priority**, ~30 min compute. Resolves V5b-T'-(c) scaling-form ambiguity. Independent of D-1..D-6b approval status.

**Decision options**:
- **D-7-A**: Authorize NQ-198a as W6 Day 1 priority.
- **D-7-D**: Defer NQ-198a to general W6+ NQ pool.

**Recommendation**: **D-7-A** (authorize). Information-cheap; resolves a substantive uncertainty in D-5 V5b-T'-(c) text.

---

## §5. Day 4 Morning Suggested Actions

### Path 1: User approves Recommended (D-1..D-5 + D-6a) + D-7

**Day 4 morning**:
1. Pre-flight tests (`pytest -q` → 180 baseline).
2. Apply canonical edits per `01_*` §5 protocol; **D-5 with revised V5b-T'-(c) text per §4.2 above**.
3. Apply theorem_status.md + CHANGELOG.md per `03_*` §4.1.
4. Output `01a_canonical_promotion_log.md`.
5. Post-edit tests (180 must remain).
6. Schedule NQ-198a for W6 Day 1.

Estimated time: ~75 min (canonical edits + verification + NQ-198a scheduling).

### Path 2: User approves D-5-D1 (short-defer for NQ-198a)

**Day 4 morning**:
1. Same Block 1 application as Path 1, **EXCEPT skip D-5** (defer V5b-T' new entry).
2. Day 4 PM run NQ-198a.
3. Day 4 EOD or Day 5 morning: re-evaluate V5b-T' text based on NQ-198a results; finalize D-5 text; apply.

Estimated time: ~45 min Block 1 + ~30 min NQ-198a + ~30 min D-5 text finalization = ~105 min.

### Path 3: User defers all

**Day 4 morning**: NQ-244 (3D LSW $T^3_{15}$ K=10) directly. ~1-2h compute. Day 4 PM: data analysis + Paper §4.5.5 update.

### Path 4: User approves D-6b-1 (capture Theorem 4.6.1 framework now)

**Day 4 morning**: Same as Path 1, plus apply ~10-15 lines D-6b text per `04_*` §5.2. Estimated time: ~85 min.

---

## §6. Hard Constraint Verification

- [x] canonical 직접 수정 0 — this synthesis file is documentation/recommendation only.
- [x] No silent resolution — all changes to user-decision recommendations are explicit (§4 D-5 revision, §4 D-6b upgrade, §4 D-7 new proposal).
- [x] No primitive override.
- [x] No 4-energy-term merging.
- [x] K not dual-treated.
- [x] No metastability without P-F flag.
- [x] No reductive equation — all inheritance / cohomology / Modica-Mortola references are **structural correspondence**, not reduction.
- [x] All NQ spawns explicitly labeled with Cat target + effort estimate + priority tier.
- [x] All decision-impact recommendations show updated options matrix.

---

## §7. Summary

**Day 3 deepening pass produced**:

| Output file | Substantive contribution |
|---|---|
| `04_*` (D-6b) | Cat B sketch → Cat B target with Theorem 4.6.1 framework. **Substantive negative result**: σ^A K-jump inheritance non-deterministic. |
| `05_*` (V5b-T' Cat A) | Sharp-interface + lattice hybrid derivation: μ ≈ 2βξ_0² independent of \|∂S\|. **Substantive negative result**: Phase 3 heuristic over-claims \|∂S\| dependence. |
| `06_*` (this synthesis) | 10 new NQ spawns; W6+ priority order; user-decision impact (D-5 text revision; D-6b upgrade; D-7 new). |

**Aggregate effect**:
- 2 Day-2 propositions advanced (D-6b structural rigor; V5b-T' analytic attempt).
- 2 substantive negative results discovered (improving theory honesty).
- 10 new NQ spawns with explicit priorities.
- 3 user-decision items refined (D-5 text revision; D-6b options expanded; D-7 added).

**Without canonical edits or silent resolutions**, the deepening pass advances open problems and improves user-decision quality. Day 4 user decisions are now **better informed**: they can choose between immediate merge with caveat (D-5-A1), short-defer for verification (D-5-D1), or comprehensive framework capture (D-6b-1).

---

**End of 06_open_problems_development_synthesis.md.**
**Status: Day 3 deepening pass synthesized. 10 new NQ spawns; 3 user-decision refinements; W6+ priority order updated. D-7 proposal added (NQ-198a urgent W6 ~30 min). 99_summary.md update next.**
