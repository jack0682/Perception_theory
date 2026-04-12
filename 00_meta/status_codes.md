---
id: META-0004
type: meta/status_codes
status: accepted
last_updated: 2026-04-12
---

# Status Codes & State Machine

## Document Status Lifecycle

Every document in the Research OS progresses through a state machine. This defines valid transitions and their semantics.

```
seed → draft → active ⇄ tentative → validated → accepted → [canonical]
         ↓                              ↓
      [deprecated]              [challenged] → [archived]
```

### States (Detailed)

#### **seed**
- **Definition:** Rough idea, raw notes, brainstorm output
- **Content:** Incomplete thoughts, speculative, unvetted
- **Transitions:**
  - → `draft` (when organized)
  - → `archived` (if abandoned)
- **Example:** Raw margin notes from literature review
- **Duration:** Hours to days
- **Review Required:** None (informal)

#### **draft**
- **Definition:** First coherent pass; author believes it's worth pursuing
- **Content:** Has structure (intro, claims, reasoning) but incomplete verification
- **Transitions:**
  - → `active` (ready for investigation)
  - → `archived` (decision to not pursue)
- **Example:** Proof outline with some lemmas but gaps remain
- **Duration:** Days
- **Review Required:** None formally (but self-review complete)

#### **active**
- **Definition:** Currently under investigation; resource allocation justified
- **Content:** Substantial work in progress; revisions expected
- **Transitions:**
  - → `tentative` (ready for external critique)
  - → `active` (continued work)
  - → `archived` (blocked or abandoned)
- **Example:** Proof with all major steps, some gaps remain; experiments running
- **Duration:** Days to weeks
- **Review Required:** Self + informal team feedback

#### **tentative**
- **Definition:** Proposed for validation; no critical errors known
- **Content:** Appears complete; awaits testing/review/experiment
- **Transitions:**
  - → `validated` (evidence supports it)
  - → `challenged` (counterexample or error found)
  - → `active` (returned for revision)
  - → `archived` (deprioritized)
- **Example:** Claim with proof outline; experiments not yet run
- **Duration:** Days to weeks
- **Review Required:** Formal critique round (Critic Agent)

#### **challenged**
- **Definition:** Serious flaw identified; integrity questioned
- **Content:** Counterexample, logical gap, or empirical failure documented
- **Transitions:**
  - → `active` (back to investigation with new info)
  - → `archived` (flaw fatal; no fix feasible)
  - → `validated` (only if challenge is refuted with proof)
- **Example:** Proof with error found in Lemma 3; C-0001 contradicted by exp65
- **Duration:** Hours to days (decision point)
- **Review Required:** Critic + Lead decision

#### **validated**
- **Definition:** Experimental or empirical evidence strongly supports it
- **Content:** Complete; experimental results consistent with claim
- **Transitions:**
  - → `accepted` (ready for canonical)
  - → `active` (if new doubt arises)
  - → `challenged` (if new evidence contradicts)
- **Example:** Claim C-0001 + proof P-0001 + experiments E-0001:E-0010 all consistent
- **Duration:** Stable (until new evidence)
- **Review Required:** Formal validation (Experiment Agent + Critic)

#### **accepted**
- **Definition:** Canonical or near-canonical; production use approved
- **Content:** Complete, verified, formally correct (to extent human verification allows)
- **Transitions:**
  - → `deprecated` (superseded by newer result)
  - → `challenged` (only if major flaw found)
- **Example:** Theorem T1 in Canonical Spec v1.2 with proof P-0001 and Category A status
- **Duration:** Indefinite (or until superseded)
- **Review Required:** Lead + Canonical promotion review

#### **deprecated**
- **Definition:** Superseded by newer result or understanding; kept for historical record
- **Content:** Complete and archived; reference only
- **Transitions:**
  - → `archived` (if never referenced)
  - → `active` (if revived due to new insight)
- **Example:** Canonical Spec v1.0 (superseded by v1.2)
- **Duration:** Indefinite
- **Review Required:** None

#### **archived**
- **Definition:** End state; no longer active research; historical record only
- **Content:** Complete; may be unfinished, failed, or superseded
- **Transitions:**
  - None (terminal state, but can be revived if needed)
- **Example:** Failed proof attempt P-0001_v1; abandoned approach from 03-26
- **Duration:** Indefinite
- **Review Required:** None

---

## Document Type × Status Interaction

Not all status transitions are appropriate for all document types. Key constraints:

| Document Type | Typical Entry | Valid Next States | Promotion Path | Terminal State |
|---|---|---|---|---|
| **Question (Q-xxxx)** | draft | active → resolved or archived | N/A | archived |
| **Claim (C-xxxx)** | draft | active → tentative → validated → accepted | → canonical | deprecated \| archived |
| **Proof (P-xxxx)** | draft | active → tentative → validated → accepted | → canonical | archived |
| **Experiment (E-xxxx)** | seed → draft | active → validated | → results | archived |
| **Result (R-xxxx)** | draft | active → tentative → validated → accepted | → canonical | archived |
| **Assumption (A-xxxx)** | draft | active → tentative → accepted | → registry | deprecated |
| **Discussion (DISC-xxxx)** | seed → draft | active → tentative | N/A | archived |

---

## Severity Levels (For Problems/Open Issues)

Used in `severity` field of YAML header. Primarily for:
- Open problems (OP-xxxx)
- Challenged documents
- Active research blockers

### Severity Codes

- **🔴 CRITICAL** — Blocks progress on foundational questions; must be resolved to proceed (e.g., F-1, M-1, MO-1)
- **🟠 HIGH** — Significant gap; affects multiple claims; should resolve soon (e.g., boundary definition)
- **🟡 MEDIUM** — Isolated issue; affects one or two results; can tolerate for now
- **🟢 LOW** — Minor gap; documentation issue; nice-to-have resolution

### Examples from 2026-04-12 Audit

| Problem | Status | Severity | Rationale |
|---------|--------|----------|-----------|
| F-1: K=2 vacuous | ⚠️ unresolved | 🔴 CRITICAL | Undermines K-field theory foundation |
| M-1: K=1 always preferred | ⚠️ unresolved | 🔴 CRITICAL | Contradicts K=2 global minimum claims |
| MO-1: Morse theory fails | ⚠️ unresolved | 🟠 HIGH | Affects M₂ analysis; workaround possible |
| Type A/B classification | ✅ challenged | 🟠 HIGH | exp65 fails to validate; needs reanalysis |
| Implicit assumptions in Spec | ⚠️ unresolved | 🟠 HIGH | Must clarify "fixed K, fixed m" constraints |
| Boundary definition precision | ⚠️ tentative | 🟡 MEDIUM | D-0004 in progress; not yet blocking |
| Transport kernel exact form | ⚠️ tentative | 🟡 MEDIUM | Provisional form works; refinement optional |

---

## Promotion Rules (Summarized)

Formal promotion rules in `promotion_rules.md`. Quick reference:

### To `tentative` (Ready for Critique)

- ✅ Complete draft (no outstanding "TBD" markers)
- ✅ Logical structure valid (no circular reasoning)
- ✅ No obvious errors (self-review passed)
- ✅ Dependencies documented (depends_on list complete)

### To `validated` (Empirical Evidence)

For **claims (C-xxxx)**:
- ✅ Proof attempt exists (P-xxxx) and is `accepted`
- ✅ At least 3 experimental tests (E-xxxx) support the claim
- ✅ No counterexamples (X-xxxx) exist
- ✅ Critic Agent has reviewed and found no critical flaws

For **experiments (E-xxxx)**:
- ✅ Specification complete (spec.md written)
- ✅ Multiple runs executed with consistent results
- ✅ Results documented (R-xxxx)
- ✅ Sanity checks passed (no obviously absurd values)

### To `accepted` (Canonical Readiness)

- ✅ `validated` status confirmed
- ✅ Formal proof (if C-xxxx) checked line-by-line
- ✅ No outstanding challenges or open issues
- ✅ Canonical Spec inclusion approved by Lead
- ✅ CHANGELOG entry written

### To `deprecated`

- ✅ Newer version exists and is `accepted`
- ✅ Clear supersession relationship documented
- ✅ Historical note added explaining why

### To `archived`

- ✅ No outstanding dependencies
- ✅ Decision made (abandoned, superseded, or historical)
- ✅ Referenced path provided for historians

---

## Transition Rules (Meta-Level)

### When Status CAN Change

1. **Author-initiated:** seed → draft → active (self-directed)
2. **Critic-initiated:** active/tentative → challenged (when flaw found)
3. **Lead-initiated:** tentative → validated, validated → accepted (formal approval)
4. **Experiment-initiated:** tentative → challenged (empirical refutation)

### When Status CANNOT Change

- ❌ Cannot skip states (e.g., draft → accepted directly)
- ❌ Cannot return from `archived` without explicit decision
- ❌ Cannot go tentative → active without documenting what changed
- ❌ Cannot go accepted → challenged without Critic review + Lead approval

---

## State Machine Diagram

```
[seed] —(organize)→ [draft] —(start)→ [active] ⇆ [tentative]
         ↑                                              ↓
      (revive)                                    (critique)
         ↑                                              ↓
      [archived] ←—(abandon)—— [active/draft]   [challenged] —(refute)→ [validated]
                                                      ↓
                                                   (fix)
                                                      ↓
                                                  [active]
                                                      ↓
                                                   (verify)
                                                      ↓
                                                 [validated] —(promote)→ [accepted] —(supersede)→ [deprecated]
                                                      ↓
                                                   (fail)
                                                      ↓
                                                  [archived]
```

---

## Visibility & Access Control (Future)

Status also affects visibility and who can modify:

- **seed/draft:** Author only
- **active:** Author + Lead + relevant agents
- **tentative:** Team (all agents, read-write for reviews)
- **validated:** Team (all agents, read-only except Log)
- **accepted:** Archive (read-only for all)
- **deprecated/archived:** Archive (read-only for all)

(Access control not yet implemented; policy defined for future implementation.)

---

**Last updated:** 2026-04-12  
**See also:** promotion_rules.md  
**Owner:** Research OS Architect
