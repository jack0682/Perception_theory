# 00_plan.md — W6 D5 Plan

**Date:** 2026-05-07 (Thu, W6 Day 5)
**Prepared:** EOD 2026-05-06 closeout session

---

## Starting State

| Item | Value |
|---|---|
| Canonical version | CV-1.11 |
| Count | 54A / 14B / 5C / 5R = 78 claims |
| Proved fraction | ~69% |
| pytest | 215 passed, 1 xfailed |
| Latest canonical | T-K-Select-OBS Cat B (Session Y) |
| Working candidates | T-Temporal-Identity (exp83 PASS) + T-σ-Inherit (exp84 PASS) |
| Next canonical target | T-Temporal-Identity Cat B (Option A) or T-σ-Inherit Cat B (Option B) |

---

## Primary Options

### Option A — T-Temporal-Identity Cat B Review (RECOMMENDED)

**Goal:** Tighten assumptions, define narrow Cat B scope, produce canonical-ready theorem statement.

**Scope:**
- Parts (a) existence of R_{t→s}: constructive, Cat B path clear.
- Parts (b) uniqueness (stable-K + margin condition Δ_sep): Cat B path; Δ_sep formula needed.
- Part (d) reduction to persist_transport (K=1): routine algebra, Cat B.
- Part (c) kernel independence: keep Cat C (blocked by OP-0011 component confinement).

**Hard constraints:**
- Do NOT claim OP-0011 / OP-0012 fully resolved.
- Do NOT claim temporal K-dynamics (OP-0005-DYN).
- Do NOT start Package II / Kramers.
- Narrow claim only: finite graph, fixed PersComp, admissible transport, margin condition.

**Expected output:**
- Working file `temporal_identity_perscomp_transport.md` tightened.
- Cat B theorem statement (parts a,b,d) with explicit assumptions A1–Ak.
- Cat B promotion criteria defined (what remains for canonical).

**Canonical promotion decision:** deferred to dedicated promotion session (not today unless all Cat B criteria clearly met and user authorizes).

---

### Option B — T-σ-Inherit Cat B Review

**Goal:** Clarify σ-inheritance Cat B scope after exp84 validation.

**Scope:**
- Parts (a,b): σ(C_i) definition, centroid/mass. Cat B path.
- Part (d-direction): split direction via principal axis. Cat B path.
- Part (e): birth case (no inheritance). Cat B.
- Parts (c, d-σ_standard): σ_standard / Wigner projection. Keep Cat C (OP-0008 W9+).

**Hard constraints:**
- Do NOT claim σ_standard / Wigner projection resolved.
- Do NOT use K-field slots as σ-identity carrier (OP-0009 conflict).
- Keep σ(C_i) slot-independent.

---

### Option C — Architecture Synthesis

**Goal:** Update perception stack document; prepare T-MF-Synthesis dependency graph.

**Output:**
- `scc_relation_onn_ortsf_perception_stack.md` fleshed out (stub exists from closeout).
- T-MF-Synthesis Cat B dependency checklist: T-Temporal-Identity + T-σ-Inherit canonical required.
- SCC → RelationWorld → ONN → ORTSF pipeline documented with inter-layer formal links.

---

### Option D — Maintenance

**Goal:** Residue search, dirty-file audit, commit hygiene.

**Tasks:**
- Grep for stale CV-1.10 references in working files.
- Check exp83/84/85 non-overclaim language.
- Verify theorem_status.md T-Temporal-Identity and T-σ-Inherit sections are consistent with working files.
- git log --oneline review; suggest commit message if needed.

---

## Recommended First Task

**Option A — T-Temporal-Identity Cat B Review**

Rationale: exp83 ALL PASSED provides fresh numerical anchor. Working file is mature (Session V–X). The narrow Cat B scope (parts a,b,d) has no deep blockers. Completing this would move the count from 14B to 15B and clear the path toward T-MF-Synthesis Cat B.

---

## Non-Goals

- No Package II / Eyring-Kramers.
- No Kramers rates from Package I.
- No OP-0009 architecture migration (W11–W12).
- No T-MF-Synthesis promotion before T-Temporal-Identity + T-σ-Inherit canonical.
- No OP-0005 fully resolved.
- No new scc/ modules unless user explicitly requests.

---

## Hard Constraints (inherit from CV-1.11 policy)

1. Soft cohesion field u_t : X_t → [0,1] is primitive. Objects are derivative.
2. Four energy terms conceptually independent (CN5). Φ_obs is likelihood only.
3. No silent OP resolution.
4. Promotion pipeline: working → reviewed → canonical (one-way only).
5. No Research OS resurrection.
6. Tests: 215+1xfailed must remain clean after any code changes.

---

*End of W6 D5 plan. Prepared EOD 2026-05-06 closeout.*
