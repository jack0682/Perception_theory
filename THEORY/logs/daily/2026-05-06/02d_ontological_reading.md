# 02d_ontological_reading.md — Ontological Reading: [u] as Pre-Objective Entity

**Session:** 2026-05-06 (W6 Day 3 G3.2, sub-file of `02_op_0009_pre_substantive_start.md`).
**Goal:** §4 of OP-0009-Pre — Commitment 1 auto-satisfaction at class level; $[\mathbf{u}]$ ontologically primary; CN10 refined flow; K-field as modeling-layer.
**Status (substantive, Silver):** §4.1-§4.3 substantive.

---

## §4.1 Commitment 1 Automatic Satisfaction

**Commitment 1 (canonical.md ~line 757):**
> *"The primitive ontological entity is the graded cohesion field $u_t : X_t \to [0,1]$, not a crisp subset, a class label, or an instance ID."*

**The conflict diagnosed:** The ordered K-field $\mathbf{u} = (u^{(1)}, \ldots, u^{(K)})$ assigns an index $j \in \{1, \ldots, K\}$ to each formation field. This index *acts as an instance ID* — it distinguishes formation 1 from formation 2, even when $u^{(1)} = u^{(2)}$ (symmetric stratum) or when the physical formation is the same. The index $j$ is a class label: the $j$-th object.

**Resolution:** The ontologically correct entity is the *unordered class* $[\mathbf{u}] \in \widetilde{\widetilde\Sigma}^K_M$, not the ordered tuple $\mathbf{u}$.

**Claim.** $[\mathbf{u}]$ satisfies Commitment 1 automatically.

*Proof:*
- Each element $u^{(j)}$ of the multiset $[\mathbf{u}] = \{u^{(1)}, \ldots, u^{(K)}\}$ is a soft cohesion field $u^{(j)} : X_t \to [0,1]$. It is graded, not crisp. ✓
- The class $[\mathbf{u}]$ contains no instance ID: there is no distinguished "first" or "second" formation. The multiset structure treats all elements symmetrically. ✓
- The class $[\mathbf{u}]$ contains no class label: no field is labeled "formation of type A" vs "type B" at the primitive level. ✓
- Each individual $u^{(j)} \in [\mathbf{u}]$ is a cohesion field value, not a crisp subset or object-boundary. ✓

**Therefore:** The pre-objective promise of Commitment 1 is preserved at the level of $[\mathbf{u}]$. The multi-formation system is characterized by a *collection* of cohesion fields (with multiplicity), none of which carries individuation information at the primitive level.

**What went wrong:** The historical tension (OAT-6 mission statement in `pre_objective_K_field_tension.md`) arose because the *implementation* of multi-formation SCC used ordered K-fields for computational tractability, and the ordered representation was *read ontologically* rather than as a modeling-layer tool. The quotient formalism resolves this: ordered representatives are valid *coordinate systems* on $\widetilde{\widetilde\Sigma}^K_M$, but the ontology is at the coordinate-free class level.

---

## §4.2 [u] Ontologically Primary; Ordered u as Modeling-Layer Lift

**Ontological layers in multi-formation SCC:**

| Level | Entity | Ontological status | Role |
|---|---|---|---|
| **Primitive** | $u_t : X_t \to [0,1]$ | Ontologically primary (Commitment 1) | Single cohesion field |
| **Class level** | $[\mathbf{u}] = \{u^{(1)}, \ldots, u^{(K)}\} \in \widetilde{\widetilde\Sigma}^K_M$ | **Ontologically primary for multi-formation** | Multi-cohesion-field state, no labeling |
| **Modeling layer** | $\mathbf{u} = (u^{(1)}, \ldots, u^{(K)}) \in \Sigma^K_M$ | Modeling-layer analytical lift | Computational coordinate; local section of $\pi$ |
| **Derived layer** | $(K_{\mathrm{field}}, K_{\mathrm{act}}) \in \mathbb{Z}_{\geq 0}^2$ | Derived counting quantities | Commitment 16; orbit-invariant |
| **Cog-sci** | "Formation 1", "Formation 2" | Post-individuation labeling | Downstream cognitive interpretation |

**Key insight:** The step from Class level → Modeling layer is the *only* step where individuation is introduced. It is a mathematical analytical convenience (choosing an ordered representative for computation), not an ontological claim. The ordered K-field architecture (I9) operates at the Modeling layer, which is legitimate as long as the ontological commitment remains at the Class level.

**Commitment 11 (canonical.md ~line 761):**
> *"Crisp objects may be recovered from the soft system by thresholding or stabilization, but they are derivative constructs, not foundational primitives."*

At the Class level, the $u^{(j)}$ in $[\mathbf{u}]$ are soft cohesion fields (not crisp), consistent with Commitment 11. Crisp formation boundaries — if recovered by thresholding each $u^{(j)}$ — are derivative, not primitive.

---

## §4.3 CN10 Refined: One-Way Ontological Flow

**CN10 (canonical.md ~line 1546):** Contrastive one-way ontological flow: SCC → derived objects, never objects → SCC.

**Original chain (CN10):**
$$u_t \xrightarrow{\text{multi-formation lift}} \mathbf{u} \xrightarrow{\text{counting}} (K_{\mathrm{field}}, K_{\mathrm{act}}) \xrightarrow{\text{interpretation}} \text{cog-sci objects}$$

**Refined chain (Day 3 G3.2):**
$$u_t \xrightarrow{\text{multi-field class}} [\mathbf{u}] \xrightarrow{\text{local section (modeling layer)}} \mathbf{u} \xrightarrow{\text{orbit-invariant counting}} K_{\mathrm{act}} \xrightarrow{\text{interpretation}} \text{cog-sci objects}$$

The arrows labeled by their character:
- $u_t \to [\mathbf{u}]$: **emergence** — multi-formation configuration as a class; no labeling introduced.
- $[\mathbf{u}] \to \mathbf{u}$: **modeling-layer lift** — choose an ordered representative (local section $s$); introduces labeling as computational convenience.
- $\mathbf{u} \to K_{\mathrm{act}}$: **derivation** — orbit-invariant quantity; $K_{\mathrm{act}}([\mathbf{u}]) = K_{\mathrm{act}}(\mathbf{u})$ independent of representative choice.
- $K_{\mathrm{act}} \to$ cog-sci: **interpretation** — downstream cognitive layer; not part of SCC theory itself.

**CN10 compliance:** Each arrow is one-way and in the SCC → objects direction. The modeling-layer lift $[\mathbf{u}] \to \mathbf{u}$ does not *reverse* the direction; it is an analytical tool that operates *within* the theory, not an ontological reduction to object-prior notions.

**What this resolves in OP-0009-Pre:** The `pre_objective_K_field_tension.md` §2.2 *prima facie* violation ("K-field architecture imports K already-individuated objects") is resolved at the Class level: the architecture imports K *unindividuated cohesion fields* (the elements of $[\mathbf{u}]$) and the ordered representation is a post-hoc analytical coordinate. The guarantee "K>1 by construction" (I9) is a *structural* claim about the modeling layer — it says the computational representation has $K$ slots, not that $K$ pre-existing objects are assumed.

---

## §4.4 Comparison with Tool A2 Quotient Verification (mathematical_scaffolding_4tools.md)

`mathematical_scaffolding_4tools.md` §3 Tool A2 proposed the quotient $\widetilde{\widetilde\Sigma}^K_M = \widetilde\Sigma^K_M / S_{K_{\mathrm{field}}}$ as a candidate for the ontologically primary K-formation space. Day 3 G3.2 makes this explicit:

- **Tool A2 claim:** quotient by $S_K$ gives the correct unordered space. ✓ (now proved via §1-§2-§3)
- **Tool A2 gap:** the *energy descent* and *reduction map continuity* were not spelled out. Now addressed in `02b` + `02c`.
- **Tool A2 gap:** the *ontological reading* (how $[\mathbf{u}]$ satisfies Commitment 1) was implicit. Now made explicit in §4.1-§4.3 above.

**Conclusion:** Day 3 G3.2 is the explicit mathematical substantiation of Tool A2's claim. It establishes that Tool A2 was correct but incomplete.

---

**End of `02d_ontological_reading.md`. §4 complete: Commitment 1 automatically satisfied by $[\mathbf{u}]$ (proved); ontological layer table; CN10 refined flow with modeling-layer lift; Tool A2 gap-filling. Day 3 Silver criterion §4: MET.**
