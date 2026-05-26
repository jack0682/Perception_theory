> [!nav] Linked: [[THEORY_INDEX]] · [[MOC_canonical_authority]] · [[INDEX|working/INDEX.md]]

# Actional Perception — Relational Field Formation

This repository develops a mathematical theory of **actional perception**: perception as the formation of a *field of possible robot intervention*, from which objects, affordances, action units, trajectories, and control modes emerge as projections of one field. The goal is to dissolve the double-translation gap where a system interprets the world once for perception and again for action. See `THEORY/0_axis/DECLARATION.md` (DECL-2.0) and `THEORY/0_axis/CANONICAL_AXIS.md`.

In short:

> Objects are not primitive.  
> A soft cohesion field comes first; objects, affordances, and actions are later projections of stabilized field patterns. **Objecthood is stabilized affordance structure.**

The cohesion-field *morphology* (closure, separation, boundary, temporal transport; 102 sealed claims) is the **substrate** — the carrier the intervention field rides on, documented below — not the whole theory.

---

## 1. Starting Point

Let $G_t=(X_t,N_t)$ be a relational graph at time $t$. The set $X_t$ is not a set of already individuated objects. It is a set of sites on which relations can be defined.

The primitive state is a soft cohesion field:

$$
u_t:X_t\to[0,1]
$$

The value $u_t(x)$ does not mean that $x$ belongs to a pre-existing object. It measures how strongly $x$ participates in a forming cohesive structure.

The basic state space is the fixed-mass field space

$$
\Sigma_m(G_t)=\{u:X_t\to[0,1]\mid \sum_x u(x)=m\}
$$

Within this space, cohesion can spread, concentrate, split, merge, and stabilize. Objecthood is an interpretation of the resulting stable pattern.

---

## 2. Theory Flow

### Single-Field Formation

The first stage studies one field on one graph.

The guiding question is:

> Can object-like formation be explained without object labels?

This stage establishes:

- finite relational graphs as the substrate,
- fixed-mass field spaces,
- closure as self-support,
- distinction as contrast against the surrounding field,
- boundaries as transition bands rather than sharp lines,
- energy-based stabilization,
- gradient-flow convergence,
- persistent homology as a morphology diagnostic.

A key result is that a single field does not have to stabilize as one simple blob. Under the full formation energy, structured multi-peak formations can appear before object labels are introduced.

In other words, structure can precede objecthood.

### Multiple Interacting Fields

The next stage studies several formation channels interacting over the same substrate.

Here the question “how many are there?” splits into several different count notions:

| Reading | Meaning | Mathematical symbol |
|---|---|---|
| model resolution | number of labelled field slots allowed by the model | $K_{\mathrm{field}}$ |
| active channel count | number of slots carrying non-negligible mass | $K_{\mathrm{act}}$ |
| topological component count | number of dominant connected components in the aggregate field | $K_{\mathrm{bar}}$ |
| soft morphology count | smooth persistence-weighted count | $K_{\mathrm{soft}}$ |

The main point is that these counts should not be conflated. The number of slots allowed by the model, the number of active slots, and the number of dominant components in the aggregate field can differ.

### Count Bridge

Three lamps may all be on, while their light merges into one bright region. Similarly, three labelled formation channels may remain active while the aggregate field has only one dominant topological component.

This makes the following baseline question necessary:

> In a well-resolved regime, when does the active channel count agree with the dominant topological component count?

The current canonical result answers this conditionally:

$$
\begin{aligned}
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)
&=K_{\mathrm{act}}^\varepsilon(\mathbf u),\\
U&=\sum_j u^{(j)}.
\end{aligned}
$$

This is not a global identity. It holds in a resolved regime where active regions are separated, bridges between regions stay low, inactive residuals are suppressed, and local secondary components do not become globally dominant.

The theorem identifies when ordinary counting is valid.

---

## 3. Mathematical Tools

| Tool | Role |
|---|---|
| finite graph theory | relational substrate and discrete field domain |
| constrained variational analysis | stable states under a fixed mass budget |
| fixed point theory | closure and self-support |
| gradient flows | stabilization dynamics |
| spectral graph theory | instabilities, bifurcations, and Hessian modes |
| persistent homology | connected morphology and component counts |
| representation theory | structural signatures under graph symmetries |
| layered state spaces | active-set changes and labelled-field boundaries |

Each tool controls a specific ambiguity. Variational methods address stable existence; persistence measures aggregate morphology; spectral tools detect splitting and instability; layered state spaces prevent model labels from being confused with field-native structure.

---

## 4. Current Status

> **정본 현재 상태 (2026-05-26):** CV-1.20 SEALED · 71A/20B/6C/5R = **102 claims** · DECL-2.0 · HT-3.12. 증명된 핵심은 *field morphology* (Tier 1); objecthood·actional·𝕌 는 DIRECTION(OPEN). 야망-증명 기울기는 `THEORY/0_axis/SCOPE_LEDGER.md`. 아래 표·§8의 일부 항목은 옛 버전(HT-1.0, CV-1.12 등) 인용일 수 있으며 그 경우 SCOPE_LEDGER가 정본이다.

The authoritative status file is:

```text
THEORY/2_substrate/canonical/theorem_status.md
```

Current summary:

| Item | Status |
|---|---|
| single-field foundation | canonical |
| pre-objective multi-peak formation | proved |
| graph-class extension | proved |
| static signatures for multiple fields | canonical definitional layer |
| hard topological count vs active count bridge | proved under explicit conditions |
| soft count bridge | open |
| field-capacity equilibrium selection (P-F regime) | Cat B — T-K-Select-PF |
| temporal identity across dynamic events (all parts) | Cat B — T-Temporal-Identity |
| dynamic count-jump inheritance | open |
| blocking hypotheses (H-T*, H-MORSE, H-SINK, H-SR, H-WS) | open — see hypothesis_tree.md |

---

## 5. Non-Claims

The theory does not claim that:

- objects are primitive,
- the number of model slots is the true object count,
- active channels always equal topological components,
- every smooth count is stable,
- the field-capacity selection problem is solved,
- structure inheritance after dynamic merge or split events is solved.

These distinctions are central. The same field configuration can be counted in different ways, and those counts agree only under specific conditions.

---

## 6. Repository Structure

```text
CODE/
  scc/           Python package
  tests/         pytest tests
  experiments/   research experiments
  scripts/       diagnostics and result generation

THEORY/                  perception-action stack
  0_axis/        center: DECLARATION (DECL-2.0), CANONICAL_AXIS, PAI_GLOSSARY, audit
  1_sensing/     raw → field
  2_substrate/   cohesion morphology + canonical/ (settled spec, theorem registry, open problems)
  3_projections/ PAI projections (object / affordance / action / control)
  4_temporal/    identity / transport / succession
  logs/          research history
```

Key documents:

- `THEORY/2_substrate/canonical/canonical.md` — settled theory specification (CV-1.20, 102 claims; current state: `THEORY/0_axis/SCOPE_LEDGER.md`)
- `THEORY/2_substrate/canonical/theorem_status.md` — theorem index + open problem registry
- `THEORY/2_substrate/canonical/hypothesis_tree.md` — hypothesis dependency tree (HT-1.0)
- `THEORY/2_substrate/multiformation/scc_multiformation_origin_to_current_korean_explanation_2026-05-03.md` — full Korean origin-to-current explanation

---

## 7. Running Code

Run Python commands from `CODE/`.

```bash
cd CODE
python3 -m pytest tests/ -v
```

Quick smoke check:

```bash
cd CODE
python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"
```

---

## 8. Next Direction

The current phase shifts from expanding the theorem count to closing floating hypotheses.

The theory has accumulated 14 Cat B theorems — results proved under explicit structural assumptions that have not yet been independently verified. Until those assumptions are closed, the conditional results cannot be upgraded to Cat A and the full logical chain from axioms to main claims remains incomplete.

The five blocking hypotheses are tracked in `THEORY/2_substrate/canonical/hypothesis_tree.md` (HT-1.0):

| Hypothesis | Blocks |
|---|---|
| H-T* — canonical registration of $T_*$ | P-F-A1 Package II, K-Select-DYN |
| H-MORSE — Morse stability of $E$ near $u^*$ | Package II (Eyring–Kramers) |
| H-SINK — Sinkhorn map is Lipschitz in graph metric | T-Temporal-Identity Cat A |
| H-SR — spectral repulsion under perturbation | T-Temporal-Identity Cat A |
| H-WS — well-separation in equilibrium regime | T-Temporal-Identity Cat A |

The critical path is: H-T* + H-MORSE → Package II → K-Select-DYN. In parallel, H-SINK + H-SR + H-WS → T-Temporal-Identity Cat A → CV-1.12.

Horizontal expansion (new open problems, new theorem areas) is paused until hypothesis debt is materially reduced.

