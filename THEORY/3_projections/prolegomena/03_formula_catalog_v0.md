---
type: working/prolegomena/formula-catalog
version: v0
date: 2026-05-23
status: full formal mathematical statements for M1-M44 (LaTeX-rendered)
purpose: 01 의 44 prose 조건을 완전한 수학적 형태로 정리. 각 M_k = (Setup + Data + Constraint + Form).
companions: 01_mathematical_conditions_v0.md, 02_framework_skeleton_v0.md
---

> [!nav] Parent: [[INDEX|working/INDEX.md]] · Companions: [[01_mathematical_conditions_v0|01 Prose]] · [[02_framework_skeleton_v0|02 Layers]]

# Formula Catalog — Full Mathematical Statements of M1–M44

## §1 — Notation

**Categories**.
- $\mathcal{C}$: ambient category for the primitive structure (large, locally small).
- $\mathcal{S} \in \mathrm{Ob}(\mathcal{C})$: primitive structure object.
- $\bar{\mathcal{C}} \supseteq \mathcal{C}$: completion admitting the limits we need (e.g., ind-completion $\mathrm{Ind}(\mathcal{C})$, pro-completion, or Lex-completion).
- $\mathcal{O}$: frame category. Objects $=$ frames, morphisms $=$ partial comparison maps.
- $\pi: \mathcal{E} \to \mathcal{O}$: a Grothendieck fibration. Fiber $X^o := \pi^{-1}(o) \in \mathrm{Ob}(\mathcal{C})$.
- $\mathrm{Sub}(\mathcal{S})$: poset of subobjects of $\mathcal{S}$ in $\mathcal{C}$.
- $\mathfrak{L}$: small label category.
- $G_o$: small category at frame $o$, generally a groupoid (not a group).

**Algebra**.
- $\mathcal{A}$: unital $\ast$-algebra over $\mathbb{C}$. When normed/topologized: $C^\ast$-algebra; when concrete and weakly closed: von Neumann algebra $\mathcal{M} \subset \mathcal{B}(\mathcal{H})$.
- $S(\mathcal{A}) := \{\, \omega: \mathcal{A} \to \mathbb{C} \mid \omega \text{ linear}, \; \omega(a^\ast a) \geq 0, \; \omega(1) = 1 \,\}$: state space.
- $\mathcal{H}$: Hilbert space (typically the GNS Hilbert space $\mathcal{H}_\omega$).
- $\mathcal{A}'$: commutant; $Z(\mathcal{A})$: center.
- $\mathcal{D}(L), \mathcal{D}(\delta)$: domain of an unbounded operator / derivation.

**Dynamics**.
- $\varphi = (\varphi_t)_{t \in \mathbb{R}}$: strongly continuous one-parameter group of $\ast$-automorphisms of $\mathcal{A}$.
- $\delta := \dfrac{d}{dt} \varphi_t \big\vert_{t=0}$: infinitesimal generator (closed derivation $\mathcal{D}(\delta) \subset \mathcal{A} \to \mathcal{A}$).
- $\sigma^\omega = (\sigma_t^\omega)_{t \in \mathbb{R}}$: Tomita–Takesaki modular automorphism group of a faithful normal state $\omega$.
- $\Delta_\omega, J_\omega$: modular operator and modular conjugation.
- $L$ (in differential setting): generator on a manifold of states; Liouville / Markov / Lindblad operator depending on context.

**Boundary / coupling**.
- $\partial \mathcal{S}$: boundary subobject of $\mathcal{S}$ (in $\mathcal{C}$, fixed by the category).
- $\mathcal{H}_{\mathrm{bdry}}$: vector space of admissible boundary perturbations.
- $h \in C(\mathbb{R}; \mathcal{H}_{\mathrm{bdry}})$: time-dependent boundary datum, $h(t)$.
- $g: \mathcal{S} \times \mathcal{H}_{\mathrm{bdry}} \to T\mathcal{S}$: coupling field with $g(\cdot, 0) \equiv 0$.

**Correlation / response**.
- $A_t := \varphi_t(A)$ for $A \in \mathcal{A}$.
- $C_A(\tau) := \omega(A_\tau A_0) - \omega(A)^2$ (centered two-point correlation).
- $C(x, y; \tau) := \omega(A_x(\tau) A_y(0)) - \omega(A_x)\omega(A_y)$ for local observables $A_x, A_y$ indexed by $x, y \in X$.
- $\chi_{AB}(\tau) := \dfrac{\delta \omega(A_\tau)}{\delta h_B(0)}$: Kubo response.

**Reserved (PAI, *not used below*)**: $\Delta_{\mathrm{interp}}, \mathcal{I}_{\mathrm{perc}}, \mathcal{I}_{\mathrm{act}}, \mathcal{A}_{\mathrm{PA}}, \mathrm{IPF}, \mathrm{PA\text{-}formation}$.

---

## §2 — Negation (M1–M5)

### M1 — $\mathcal{S}$ is not a Set-morphism

Setup: $\mathcal{S} \in \mathrm{Ob}(\mathcal{C})$.

Statement:
$$
\neg \Big( \exists A, B \in \mathrm{Ob}(\mathbf{Set}),\; \exists f \in \mathrm{Hom}_{\mathbf{Set}}(A, B),\; \mathcal{S} \cong U(f) \text{ for any forgetful } U: \mathcal{C} \to \mathrm{Arr}(\mathbf{Set}) \Big).
$$

Here $\mathrm{Arr}(\mathbf{Set})$ is the arrow category of $\mathbf{Set}$. The clause rules out the template "$\mathcal{S} =$ a fixed function on a fixed set". Equivalently, $\mathcal{S}$ has no underlying-arrow-of-sets functorial representation.

### M2 — No primitive topology

Setup: $\mathcal{C}$ is equipped with no a-priori forgetful functor $U: \mathcal{C} \to \mathbf{Top}$.

Statement: $U$ does not appear in the signature of $\mathcal{C}$. Instead, there exists a *constructed* functor
$$
\mathcal{D}: \mathcal{C} \to \mathbf{Top},
$$
defined post-hoc from the data of $\mathcal{S}$ (correlation, spectrum, modular flow); $\mathcal{D}(\mathcal{S})$ is a *derived* topological space. The pair $(\mathcal{S}, \mathcal{D})$ is required to satisfy: changing the construction recipe $\mathcal{D} \mapsto \mathcal{D}'$ does not change the *primitive datum* $\mathcal{S}$.

### M3 — Flow is primitive

Setup: $\mathcal{C}$ admits a tangent endofunctor $T: \mathcal{C} \to \mathcal{C}$ and a notion of differentiable morphism.

Data: a strongly continuous one-parameter group
$$
\varphi: \mathbb{R} \to \mathrm{Aut}_{\mathcal{C}}(\mathcal{S}), \qquad \varphi(0) = \mathrm{id}_{\mathcal{S}}, \qquad \varphi(s+t) = \varphi(s) \circ \varphi(t).
$$
Generator $L \in \Gamma(T\mathcal{S} \to \mathcal{S})$ defined by $L(x) := \dfrac{d}{dt} \varphi_t(x)\big\vert_{t=0}$.

Constraint:
$$
L\big\vert_{h=0} \not\equiv 0 \quad \text{in } \Gamma(T\mathcal{S}),
$$
i.e., the section is not identically zero when the boundary coupling vanishes. The pair $(\mathcal{S}, \varphi)$ (equivalently $(\mathcal{S}, L)$) is the primitive datum; $\mathcal{S}$ alone (without $\varphi$) is not the primitive.

### M4 — No global section

Setup: contravariant sheaf-of-states functor $\Gamma(-, \mathcal{S}): \mathcal{O}^{\mathrm{op}} \to \mathbf{Set}$, with $\Gamma(o, \mathcal{S}) := X^o$ (frame-local states).

Statement:
$$
\Gamma_{\mathrm{global}}(\mathcal{S}) := \varprojlim_{o \in \mathcal{O}} \Gamma(o, \mathcal{S}) = \emptyset.
$$
Equivalently, there is no compatible family $\{ s_o \in \Gamma(o, \mathcal{S}) \}_{o \in \mathrm{Ob}(\mathcal{O})}$ simultaneously over all frames. Only frame-local sections are admissible; no Kochen–Specker-style global valuation exists.

### M5 — Non-separability

Setup: $(\mathcal{C}, \otimes, 1)$ is symmetric monoidal.

Statement:
$$
\neg \Big( \exists A, B \in \mathrm{Ob}(\mathcal{C}),\; A, B \not\cong 1,\; \exists \text{ iso } \varphi: \mathcal{S} \xrightarrow{\sim} A \otimes B \text{ in } \mathcal{C} \Big).
$$
The non-existence is *canonical*: any iso $\mathcal{S} \cong A \otimes B$ that does exist is required to be non-natural in $\mathcal{S}$ (an accidental coincidence relative to extra data, not a structural decomposition).

---

## §3 — Frame Indexing (M6–M9)

### M6 — Observables are sections over frames

Setup: $\pi: \mathcal{E} \to \mathcal{O}$ a Grothendieck fibration in $\mathcal{C}$.

Data: for each $o \in \mathrm{Ob}(\mathcal{O})$, fiber $X^o := \pi^{-1}(o) \in \mathrm{Ob}(\mathcal{C})$. For each $f: o \to o'$ in $\mathcal{O}$, a Cartesian morphism $f^\ast: X^{o'} \to X^o$ (pullback functor).

Statement: every observable of $\mathcal{S}$ is, by definition, a section over some frame:
$$
\mathrm{Obs}(\mathcal{S}) := \bigsqcup_{o \in \mathrm{Ob}(\mathcal{O})} \Gamma(o, X^o) \;/\; (\text{compatibility along } f^\ast).
$$
There is no notion of "observable" independent of a frame index $o$.

### M7 — Partial morphisms only

Setup: as M6.

Statement:
$$
\forall o, o' \in \mathrm{Ob}(\mathcal{O}) \text{ with } o \neq o': \quad \mathrm{Hom}_{\mathcal{O}}(o, o') \cup \mathrm{Hom}_{\mathcal{O}}(o', o) \subseteq \{\text{partial maps only}\},
$$
i.e., (i) $\mathrm{Hom}_{\mathcal{O}}(o, o')$ may be empty; (ii) when non-empty, its elements need not be invertible; (iii) $\not\exists$ canonical iso $o \xrightarrow{\sim} o'$ in $\mathcal{O}$. Concretely: $\mathcal{O}$ is a small category, generally not a groupoid (consistent with M28).

### M8 — Frame category is derived [S]

Setup: theory $T = (\mathrm{Axioms}, \mathrm{Constructions})$.

Statement: $\mathcal{O} \notin \mathrm{Axioms}(T)$. Instead,
$$
\exists \text{ functorial construction } \Phi: \mathrm{Axioms}(T) \to \mathbf{Cat} \quad \text{with} \quad \Phi(\mathrm{Axioms}(T)) = \mathcal{O}.
$$
Candidates for $\Phi$: (i) spectrum of self-reference structure, $\mathrm{Spec}_{\mathrm{self}}(\mathcal{S})$; (ii) state-selection groupoid via Connes–Rovelli thermal time; (iii) Doering–Isham context category $\mathcal{V}(\mathcal{M})$ of an underlying von Neumann algebra $\mathcal{M}$. The specific $\Phi$ is theory-dependent; existence of *some* $\Phi$ is the requirement.

### M9 — Non-atomic frames [O]

Setup: $\mathcal{O}$ a small category.

Statement: $\mathrm{Ob}(\mathcal{O})$ is *not* restricted to atomic objects. The admissible class $\mathcal{A}_{\mathcal{O}} \subseteq \mathrm{Ob}(\mathcal{O})$ includes at least:
$$
\text{(a) ordinary objects;} \quad \text{(b) groupoid-internal objects;} \quad \text{(c) homotopy colimits of sub-frames.}
$$
Open problem: characterize the maximal $\mathcal{A}_{\mathcal{O}}$ consistent with M6, M7, M10.

---

## §4 — World Limit (M10–M14)

### M10 — Universal limit object

Setup: $\mathcal{O}$ small, $X^{(-)}: \mathcal{O} \to \mathcal{C}$ the fiber functor (M6).

Statement: in $\bar{\mathcal{C}}$,
$$
\exists! \, \mathcal{W} \in \mathrm{Ob}(\bar{\mathcal{C}}), \quad \mathcal{W} \cong \varprojlim_{o \in \mathcal{O}} X^o \quad (\text{canonical iso unique}).
$$
The limit cone $(\mathcal{W}, (\pi_o: \mathcal{W} \to X^o))$ exists and is universal: for any other cone $(Y, (q_o: Y \to X^o))$ there is a unique $u: Y \to \mathcal{W}$ with $\pi_o \circ u = q_o$. Concrete realizations: inductive limit $\varinjlim \mathcal{A}(O)$ in AQFT (Brunetti–Fredenhagen–Verch); pro-object in $\mathrm{Ind}/\mathrm{Pro}$ completions.

### M11 — Universal property only

Setup: $\mathcal{W}$ from M10.

Statement: the representable functor
$$
h_{\mathcal{W}} := \mathrm{Hom}_{\bar{\mathcal{C}}}(-, \mathcal{W}): \bar{\mathcal{C}}^{\mathrm{op}} \to \mathbf{Set}
$$
determines $\mathcal{W}$ up to unique iso (Yoneda). Conversely, $\mathcal{W}$ is *not* specified by any internal description of its elements: there is no construction
$$
\mathrm{Elements}(\mathcal{W}) := \{ \text{meaningful intrinsic description} \},
$$
apart from the data of cones into $\mathcal{W}$. Element-level access to $\mathcal{W}$ is unavailable; access is via maps into $\mathcal{W}$.

### M12 — Coupling enters as boundary perturbation

Setup: $\mathcal{S}$ admits a subobject $\partial \mathcal{S} \hookrightarrow \mathcal{S}$ (boundary) and a complementary interior. $\mathcal{H}_{\mathrm{bdry}}$ is the space of admissible boundary data.

Data: $h \in C^1(\mathbb{R}; \mathcal{H}_{\mathrm{bdry}})$.

Statement: the evolution equation for $\mathcal{S}$ takes the form
$$
\partial_t \mathcal{S}(t) = L(\mathcal{S}(t)) \oplus B(\mathcal{S}(t), h(t)),
$$
where $L: \mathcal{S} \to T\mathcal{S}$ is the autonomous (bulk) generator and $B: \mathcal{S} \times \mathcal{H}_{\mathrm{bdry}} \to T\mathcal{S}$ acts only on the boundary stratum: $\mathrm{supp}(B(\cdot, h)) \subseteq \partial \mathcal{S}$. There is *no* bulk source term $S: \mathbb{R} \to T\mathcal{S}$ added to $L$.

### M13 — Multiplicative coupling, non-vanishing autonomous generator

Setup: as M12.

Data: $g: \mathcal{S} \times \mathcal{H}_{\mathrm{bdry}} \to T\mathcal{S}$ with $g(\cdot, 0) \equiv 0$.

Statement:
$$
\text{(i)} \;\; L\big\vert_{h=0} \not\equiv 0, \qquad \text{(ii)} \;\; B(\mathcal{S}, h) = g(\mathcal{S}, h), \;\; g(\mathcal{S}, 0) = 0.
$$
Equivalent SDE/CDE form on the manifold of states:
$$
d\mathcal{S}_t = L(\mathcal{S}_t) \, dt + g(\mathcal{S}_t) \, dh_t, \qquad L(\cdot) \not\equiv 0, \;\; g(\cdot, 0) = 0.
$$
Negation: the additive forcing $d\mathcal{S}_t = L(\mathcal{S}_t) \, dt + h(t) \, dt$ is excluded; coupling modulates rather than initiates the dynamics.

### M14 — Decoupling regime exists [S]

Setup: M12–M13, with admissible norms $\lVert \cdot \rVert_{T\mathcal{S}}$ on $T\mathcal{S}$ and $\lVert \cdot \rVert_{\mathrm{bdry}}$ on $\mathcal{H}_{\mathrm{bdry}}$.

Statement: there exists a parameter family $(\mathcal{S}^{(\varepsilon)}, h^{(\varepsilon)})_{\varepsilon > 0}$ such that
$$
\varepsilon := \frac{\lVert g(\mathcal{S}^{(\varepsilon)}, h^{(\varepsilon)}) \rVert_{T\mathcal{S}}}{\lVert L(\mathcal{S}^{(\varepsilon)}) \rVert_{T\mathcal{S}}} \;\xrightarrow{\varepsilon \to 0}\; 0,
$$
along which the trajectory $\varepsilon \to 0$ is well-defined and converges to a solution of $\partial_t \mathcal{S} = L(\mathcal{S})$.

---

## §5 — Autonomous Order (M15–M18)

### M15 — Autonomous flow is non-trivial

Setup: $\varphi$ from M3 acting on $(\mathcal{A}, \omega)$.

Statement:
$$
\exists A \in \mathcal{A} \text{ such that } \;\; \frac{d}{dt} \omega(\varphi_t(A)) \bigg\vert_{t=0,\, h=0} \neq 0.
$$
Equivalently, $\omega \circ \delta \not\equiv 0$ on $\mathcal{D}(\delta)$. No autonomous fixed-state cancels all observables.

### M16 — Non-trivial invariant measure / state

Setup: state space $\Sigma_{\mathrm{state}} := S(\mathcal{A})$ (or a regular subset thereof); semigroup action $P_t: \Sigma_{\mathrm{state}} \to \Sigma_{\mathrm{state}}$ induced by $\varphi$.

Statement:
$$
\exists \mu \in \mathrm{Prob}(\Sigma_{\mathrm{state}}) \text{ with } P_t^\ast \mu = \mu \;\; \forall t, \quad \vert \mathrm{supp}(\mu)\vert \geq 2, \quad H(\mu) > 0.
$$
$H$ is the Boltzmann entropy $H(\mu) = -\int \log(d\mu / d\lambda) \, d\mu$ relative to a reference $\lambda$ when absolutely continuous, or Kolmogorov–Sinai entropy of $(\Sigma_{\mathrm{state}}, P_t, \mu)$ when no $\lambda$ exists. $\mu$ is not a Dirac mass on any fixed point.

### M17 — Baseline non-vanishing two-point function

Setup: $\omega \in S(\mathcal{A})$, $A \in \mathcal{A}$ with $\omega(A)$ finite; $A_\tau := \varphi_\tau(A)$.

Statement:
$$
\forall A \in \mathcal{A} \text{ with } A - \omega(A) \cdot 1 \neq 0, \;\; \exists \tau \in \mathbb{R}: \quad C_A(\tau) := \omega(A_\tau A_0) - \omega(A)^2 \neq 0.
$$
The map $\tau \mapsto C_A(\tau)$ is not identically zero for any non-constant observable $A$.

### M18 — Generator origin is axiomatic [O]

Setup: theory $T = (\mathrm{Primitives}, \mathrm{Axioms}, \mathrm{Constructions})$.

Statement: $L \in \mathrm{Primitives}(T)$; $\not\exists$ $\mathrm{Constructions}(T)$-recipe $R: \mathrm{ExternalData} \to L$. Any such $R$ would have to specify
$$
R: \{\text{prior physics} + \text{boundary} + \text{symmetry} + \text{initial regularity}\} \to L,
$$
and no such canonical $R$ is committed. $L$ is posited; its parametric class is constrained by M3, M13, M15.

---

## §6 — First-/Second-order Operations (M19–M22)

### M19 — Stable substructure as first-order image of $L$

Setup: $\mathrm{Sub}_{\mathrm{stable}}(\mathcal{S}) \subseteq \mathrm{Sub}(\mathcal{S})$ (stable subobjects, in the sense of M22).

Statement: there is a first-order operator
$$
\mathrm{Op}_1: \Gamma(T\mathcal{S} \to \mathcal{S}) \to 2^{\mathrm{Sub}(\mathcal{S})}, \quad \text{with} \quad \mathrm{Op}_1(L) \subseteq \mathrm{Sub}(\mathcal{S}),
$$
and
$$
\mathrm{Sub}_{\mathrm{stable}}(\mathcal{S}) \subseteq \mathrm{Op}_1(L).
$$
$\mathrm{Op}_1$ is first-order in the sense: $\mathrm{Op}_1(L)$ depends only on the 1-jet of $L$ (values and first derivatives at points of $\mathcal{S}$), not on iterated compositions of $L$.

### M20 — Type classification is a functor $\Lambda$

Setup: $\mathfrak{L}$ small category (label category).

Statement: there is a functor
$$
\Lambda: \mathrm{Sub}(\mathcal{S}) \to \mathfrak{L},
$$
with $\Lambda(F \hookrightarrow F') \in \mathrm{Hom}_{\mathfrak{L}}(\Lambda(F), \Lambda(F'))$ when $F \subseteq F'$. $\Lambda$ is *second-order* in that it depends on more than the 1-jet of $L$ on $F$ (it requires evaluating persistence and consistency, M22).

### M21 — Label category has no distinguished initial / terminal

Setup: $\mathfrak{L}$ from M20.

Statement:
$$
\not\exists \bot \in \mathrm{Ob}(\mathfrak{L}) \text{ with } \vert \mathrm{Hom}_{\mathfrak{L}}(\bot, X)\vert = 1 \;\; \forall X \in \mathrm{Ob}(\mathfrak{L}),
$$
$$
\not\exists \top \in \mathrm{Ob}(\mathfrak{L}) \text{ with } \vert \mathrm{Hom}_{\mathfrak{L}}(X, \top)\vert = 1 \;\; \forall X \in \mathrm{Ob}(\mathfrak{L}).
$$
No label is structurally preferred ($\Lambda$ does not collapse stable substructures into a privileged class).

### M22 — Decision invariants of $\Lambda$ [S]

Setup: $F \in \mathrm{Sub}(\mathcal{S})$; $\varphi$ as in M3; $h$ as in M12.

Definitions:
$$
\text{(a) Persistence: } \tau_{\mathrm{pers}}(F) := \sup\{\, T \geq 0 \mid \exists \text{ continuous } F_t \in \mathrm{Sub}(\mathcal{S}) \text{ with } F_0 = F,\; F_t \subseteq \varphi_t(\mathcal{S}),\; F_T \sim_{\mathcal{S}} F \,\}.
$$
$$
\text{(b) Consistency: } \mathrm{Cmp}(F, F') := \mathbf{1}\!\left[F \cap F' \in \mathrm{Sub}_{\mathrm{stable}}(\mathcal{S})\right] \cdot \kappa(F, F'), \quad \kappa(F, F') := 1 - \frac{\omega(F \cdot F')}{\omega(F)\,\omega(F')}.
$$
$$
\text{(c) Responsiveness: } \chi_F(h) := \frac{\delta F}{\delta h}\bigg\vert_{h=0} \in T\mathrm{Sub}(\mathcal{S}).
$$
Statement: $\Lambda(F)$ depends only on the triple $(\tau_{\mathrm{pers}}(F), \mathrm{Cmp}(F, \cdot), \chi_F)$.

---

## §7 — Algebraic Setting (M23–M26)

### M23 — State is a positive normalized linear functional [S]

Setup: $\mathcal{A}$ unital $\ast$-algebra over $\mathbb{C}$.

Statement:
$$
S(\mathcal{A}) := \{\, \omega: \mathcal{A} \to \mathbb{C} \mid \omega(\lambda a + \mu b) = \lambda \omega(a) + \mu \omega(b), \;\; \omega(a^\ast a) \geq 0 \;\; \forall a \in \mathcal{A}, \;\; \omega(1) = 1 \,\}.
$$
A state $\omega$ is *not* a fixed vector in a fixed Hilbert space. GNS construction $(\mathcal{H}_\omega, \pi_\omega, \Omega_\omega)$ is *derived*:
$$
\omega(a) = \langle \Omega_\omega, \pi_\omega(a) \Omega_\omega \rangle,
$$
where $\pi_\omega$ is the GNS representation and $\Omega_\omega$ the cyclic vector. Distinct $\omega$ yield inequivalent $(\mathcal{H}_\omega, \pi_\omega)$ in general.

### M24 — Frame-indexed family of admissible states

Setup: $\mathcal{O}$ from M6, $\mathcal{A}$ from M23.

Statement: the admissible vacua form
$$
\mathrm{VAC} := \big\{\, \omega_o \in S(\mathcal{A}) \mid \omega_o \text{ satisfies (B1)–(B3)} \,\big\}_{o \in \mathrm{Ob}(\mathcal{O})},
$$
with (B1) faithfulness, (B2) translation invariance under $\varphi$ at $o$, (B3) cluster decomposition / minimum variance under $L_o$. $\vert \mathrm{VAC}\vert > 1$ in general, and the equivalence
$$
\omega_o \sim \omega_{o'} \;\iff\; \exists \text{ unitary } U: \mathcal{H}_{\omega_o} \to \mathcal{H}_{\omega_{o'}} \text{ with } U \pi_{\omega_o}(a) U^\ast = \pi_{\omega_{o'}}(a)
$$
partitions $\mathrm{VAC}$ into more than one class: $\vert \mathrm{VAC}/{\sim}\vert > 1$.

### M25 — Threshold structure [S]

Setup: $\omega \in S(\mathcal{A})$; a norm $\lVert \cdot \rVert_C$ on the space of two-point correlation functions $C_\omega: \mathbb{R} \to \mathbb{C}$, e.g., $\lVert C \rVert_C := \sup_\tau \vert C(\tau)\vert $.

Statement: there exists $\theta_O > 0$ such that
$$
\mathrm{Baseline}(\theta_O) := \big\{\, \omega \in S(\mathcal{A}) \mid \exists A \in \mathcal{A}: \;\; 0 < \lVert C_A^\omega \rVert_C < \theta_O \,\big\} \neq \emptyset,
$$
where $C_A^\omega(\tau) = \omega(A_\tau A) - \omega(A)^2$. The number $\theta_O$ is a property of the theory, not of any particular $\omega$. Substructure emergence (M26) is gated by $\lVert C \rVert \geq \theta_O$.

### M26 — Substructure emergence condition [S]

Setup: $\omega \in S(\mathcal{A})$, $F \subseteq \mathrm{Sub}(\mathcal{S})$; $\pi: \mathcal{E} \to \mathcal{O}$ with frame $o$; $G_o$ groupoid (M28).

Definitions:
$$
\mathrm{Thresh}(F, \omega) := \big[\, \lVert C_{A_F}^\omega \rVert_C \geq \theta_O \,\big], \quad A_F \in \mathcal{A} \text{ a representing observable of } F,
$$
$$
\mathrm{Inv}(F, G_o) := \big[\, \forall g \in \mathrm{Mor}(G_o) \text{ with source/target containing } F: \; g \cdot F = F \,\big],
$$
$$
\mathrm{Cohesion}(F) := \big[\, \lVert A_F(x) \rVert \leq C \, e^{-\gamma \, d(x, \mathrm{supp}_{\mathrm{core}}(F))} \,\big] \quad \text{(exponential decay outside core)}.
$$
Statement:
$$
\mathrm{Thresh}(F, \omega) \;\wedge\; \mathrm{Inv}(F, G_o) \;\wedge\; \mathrm{Cohesion}(F) \;\implies\; F \in \mathrm{Sub}_{\mathrm{stable}}(\mathcal{S}).
$$

---

## §8 — Invariance (M27–M30)

### M27 — Substructure identity by $G_o$-orbit [S]

Setup: $G_o$ as in M28 acting on $\mathrm{Sub}(\mathcal{S})$ by $g \cdot F$ (functorial right/left action).

Statement: define identity classes by
$$
[F]_{G_o} := \big\{\, g \cdot F \mid g \in \mathrm{Mor}(G_o), \;\; s(g) = F \text{ or } t(g) = F \,\big\}.
$$
Two substructures represent the same identity iff $[F]_{G_o} = [F']_{G_o}$. The quotient $\mathrm{Sub}(\mathcal{S}) / G_o$ is the *identity space*.

### M28 — $G_o$ is a groupoid / general category [S]

Setup: small category $G_o$ with object set including frame data at $o$.

Statement: $G_o$ is *not* a group:
$$
\exists g \in \mathrm{Mor}(G_o) \text{ with no inverse}: \;\; \not\exists h \in \mathrm{Mor}(G_o) \text{ with } h \circ g = \mathrm{id}_{s(g)} \;\wedge\; g \circ h = \mathrm{id}_{t(g)}.
$$
Examples of generators of $G_o$: eye movement, body movement (typically invertible); attention shift (typically invertible); modality shift (partially invertible); temporal gap, memory recall, linguistic re-description (typically non-invertible). $G_o$ is generated by these as a category with at least one non-invertible generator.

### M29 — Cross-fiber invariance [O] — *PAI entry point*

Setup: $\pi: \mathcal{E} \to \mathcal{O}$ from M6; for $o \neq o'$ in $\mathrm{Ob}(\mathcal{O})$, distinct fibers $X^o, X^{o'}$.

Data: a class
$$
\mathcal{M}_{\mathrm{cross}} \;\subseteq\; \bigsqcup_{o \neq o'} \mathrm{Hom}_{\mathcal{C}}(X^o, X^{o'})
$$
of *partial isomorphisms across fibers* (e.g., visual–tactile modality bridges), satisfying compatibility with the fibration $\pi$.

Statement: a substructure $F = (F_o \subseteq X^o)_{o \in \mathrm{Ob}(\mathcal{O})}$ is *cross-fiber invariant* iff
$$
\forall \mu \in \mathcal{M}_{\mathrm{cross}}, \;\; \mu: X^o \to X^{o'}: \quad \mu(F_o) = F_{o'} \quad \text{on } \mathrm{dom}(\mu).
$$
The required compatibility class $\mathcal{M}_{\mathrm{cross}}$ has *no canonical native model* in current frameworks: cohesive $\infty$-topos provides categorical scaffold only; BFV provides functor compatibility only; QBism has no cross-frame structure. This is the OP-NEW-C of 02 §6.

### M30 — Partial coverage [O]

Setup: as M6.

Statement: $\exists F \in \mathrm{Sub}(\mathcal{S})$ with
$$
\mathrm{Ob}_F := \{\, o \in \mathrm{Ob}(\mathcal{O}) \mid F_o := F \cap X^o \neq \emptyset \,\} \;\subsetneq\; \mathrm{Ob}(\mathcal{O}),
$$
i.e., $F$ is *not* supported across all frames. The sub-collection $\mathrm{Ob}_F \subseteq \mathrm{Ob}(\mathcal{O})$ is admissible and characterized by an auxiliary predicate $\mathrm{Cover}(F)$ (partial-coverage taxonomy). Open: precise specification of admissible $\mathrm{Ob}_F$.

---

## §9 — Derived Structures (M31–M34)

### M31 — Spatial metric from correlation decay [S]

Setup: $X = (X, \nu)$ a measurable space carrying local observables $A_x \in \mathcal{A}$ ($x \in X$); $\omega \in S(\mathcal{A})$ faithful.

Definition:
$$
C(x, y) := \omega(A_x A_y) - \omega(A_x)\,\omega(A_y), \qquad d_\omega(x, y) := -\log \lvert C(x, y) \rvert \;\;(\text{mod gauge}).
$$
Statement: $d_\omega$ is a pseudo-metric on $X / (\text{gauge equivalence})$. Refinements: Connes spectral distance
$$
d_D(x, y) := \sup \big\{\, \lvert f(x) - f(y) \rvert \mid f \in \mathcal{A}_{\mathrm{sa}}, \; \lVert [D, f] \rVert \leq 1 \,\big\}
$$
for a Dirac operator $D$, recovers $d_\omega$ in appropriate semiclassical limits.

### M32 — Modular time [O]

Setup: $\mathcal{M}$ a von Neumann algebra; $\omega \in S(\mathcal{M})$ faithful normal; $(\mathcal{H}_\omega, \pi_\omega, \Omega_\omega)$ GNS triple. Define on the $\ast$-algebra $\pi_\omega(\mathcal{M}) \Omega_\omega \subseteq \mathcal{H}_\omega$ the antilinear operator
$$
S_\omega: \pi_\omega(a) \Omega_\omega \mapsto \pi_\omega(a^\ast) \Omega_\omega.
$$
Let $S_\omega = J_\omega \Delta_\omega^{1/2}$ be its polar decomposition ($J_\omega$ antiunitary, $\Delta_\omega \geq 0$ self-adjoint).

Statement: the modular automorphism group is
$$
\sigma_t^\omega(a) := \Delta_\omega^{it} \, a \, \Delta_\omega^{-it}, \qquad t \in \mathbb{R},
$$
characterized by the KMS condition at $\beta = 1$:
$$
\omega(a \, \sigma_t^\omega(b)) = \omega(\sigma_{t - i}^\omega(b) \, a), \qquad \forall a, b \in \mathcal{M}_{\mathrm{analytic}}.
$$
The Tomita–Takesaki theorem guarantees $\sigma_t^\omega \in \mathrm{Aut}(\mathcal{M})$. The generator
$$
\delta_\omega := i \, \frac{d}{dt} \sigma_t^\omega \bigg\vert_{t=0} = i \, [\log \Delta_\omega, \cdot]
$$
is the modular Hamiltonian (on the appropriate domain). Open: applicability to non-Type-III $\mathcal{M}$ and to non-faithful $\omega$.

### M33 — Carrier $X$ is derived

Setup: $\mathcal{A}$ a (commutative or non-commutative) $C^\ast$-algebra; $\omega, \rho$ admissible.

Statement: the carrier $X$ is constructed, not given:
$$
\text{commutative:} \quad X := \mathrm{Spec}(\mathcal{A}), \quad \mathcal{A} \cong C_0(X) \quad \text{(Gelfand–Naimark)},
$$
$$
\text{non-commutative, measure-based:} \quad X := \mathrm{supp}(\rho) \quad \text{(Finster causal fermion)},
$$
$$
\text{correlation-based:} \quad X := \mathrm{Compl}\big( \mathcal{A} \,/\, \{A \sim A' \iff d_\omega(A, A') = 0\} \big).
$$
In every case $X \notin \mathrm{Primitives}(T); \;\; X \in \mathrm{Derived}(T)$.

### M34 — Value space is derived [S]

Setup: data consists of pairwise comparison relations $\{ A_\alpha \preceq_x A_\beta \}_{\alpha, \beta, x}$, indexed by observables $A$ and locations $x \in X$.

Statement: the value space $V$ is
$$
V := \mathrm{Compl}\Big( \operatorname*{colim}_{x \in X} (\preceq_x) \Big),
$$
where the colimit is taken in the category of preorders, and $\mathrm{Compl}$ is order-theoretic completion (e.g., Dedekind–MacNeille). The interval $[0, 1] \subseteq V$ appears as a special case when $\preceq_x$ are totally orderable with bounded range. $V$ is constructed; it is not posited a priori.

---

## §10 — Accessibility / Probing (M35–M39)

### M35 — Variational accessibility

Setup: $\mathcal{S} \in \mathcal{B}$ a Banach (or Fréchet) manifold of admissible structures; $h \in \mathcal{H}_{\mathrm{bdry}}$; the map $\mathcal{S}_h: \mathbb{R} \to \mathcal{B}$, $t \mapsto \mathcal{S}_h(t)$ solves the dynamics of M12–M13.

Statement: the Fréchet derivative
$$
\frac{\delta \mathcal{S}}{\delta h(t)} \;\in\; \mathcal{L}\big(\mathcal{H}_{\mathrm{bdry}}; \; T_{\mathcal{S}_h(t)} \mathcal{B}\big)
$$
exists and is continuous in $t$. Equivalently: for all admissible variations $\delta h \in \mathcal{H}_{\mathrm{bdry}}$, the solution map $h \mapsto \mathcal{S}_h$ is differentiable.

### M36 — Inter-frame morphisms transmit comparison

Setup: $\pi: \mathcal{E} \to \mathcal{O}$ from M6.

Statement: the pullback functor associated to $f \in \mathrm{Hom}_{\mathcal{O}}(o, o')$,
$$
f^\ast: X^{o'} \to X^o,
$$
is *informative*: for any non-trivial section $s \in \Gamma(o', X^{o'})$, the section $f^\ast(s) \in \Gamma(o, X^o)$ is distinguishable from generic sections (i.e., $f^\ast$ is not constant on the relevant equivalence classes). Functoriality:
$$
(f' \circ f)^\ast = f^\ast \circ f'^\ast, \qquad (\mathrm{id}_o)^\ast = \mathrm{id}_{X^o}.
$$
When $\mathrm{Hom}_{\mathcal{O}}(o, o') = \emptyset$, no comparison is possible (consistent with M7).

### M37 — Partial functors to standard categories [S]

Setup: $\mathcal{C}' \in \{\mathbf{Top}, \mathbf{Prob}, \mathbf{Cat}, \mathbf{Vect}_{\mathbb{C}}, \ldots\}$.

Statement: there exist functors
$$
F: \mathcal{C} \to \mathcal{C}' \quad (\text{partial: defined on a full subcategory } \mathcal{C}_F \subseteq \mathcal{C})
$$
which are *not* surjective on objects and *not* faithful, but are functorial on their domain. Examples: Gelfand transform $\mathcal{A} \mapsto C(\mathrm{Spec}\,\mathcal{A})$ ($\mathcal{C} = $ comm. $C^\ast$-algebras, $\mathcal{C}' = \mathbf{Top}$); GNS construction $\omega \mapsto (\mathcal{H}_\omega, \pi_\omega)$; spectral measure $A \mapsto \mu_A$ ($\mathcal{C}' = \mathbf{Prob}$). No single $F$ is a global embedding.

### M38 — Linear response (Kubo) is well-defined

Setup: $\omega \in S(\mathcal{A})$; $A, B \in \mathcal{A}$; $h_B(t)$ a perturbation entering as $\delta H = h_B(t) B$ in the modified Hamiltonian (or its derivation analog).

Statement:
$$
\chi_{AB}(\tau) := \frac{\delta \omega(A_\tau)}{\delta h_B(0)}
$$
exists as a distribution in $\tau$, satisfies causality ($\chi_{AB}(\tau) = 0$ for $\tau < 0$ in time-ordered convention), and the Kubo formula holds:
$$
\chi_{AB}(\tau) = i \, \Theta(\tau) \, \omega\big( [A_\tau, B] \big).
$$
Fluctuation–dissipation (combined with M17): in equilibrium $\omega$,
$$
C_{AB}(\tau) = -\frac{1}{\pi} \int_{-\infty}^{\infty} d\omega' \;\; \frac{\mathrm{Im}\,\chi_{AB}(\omega')}{1 - e^{-\beta \omega'}} \, e^{-i \omega' \tau},
$$
i.e., $\chi$ and $C$ are related by an explicit analytic continuation.

### M39 — Internal Gödelian self-reference

Setup: $\mathcal{L}_{\mathrm{int}}(\mathcal{S})$ an internal language interpreting first-order arithmetic; $\mathrm{Provable}_{\mathcal{S}}: \mathrm{Sent}(\mathcal{L}_{\mathrm{int}}) \to \{0, 1\}$ a recursively enumerable provability predicate within $\mathcal{S}$.

Statement: there exists a fixed point
$$
\gamma_{\mathcal{S}} \in \mathrm{Sent}(\mathcal{L}_{\mathrm{int}}) \quad \text{with} \quad \mathcal{S} \models \big(\gamma_{\mathcal{S}} \iff \neg \, \mathrm{Provable}_{\mathcal{S}}(\ulcorner \gamma_{\mathcal{S}} \urcorner) \big),
$$
obtained from a Gödelian diagonal construction.

Categorical encoding (Lawvere 1969): in any cartesian closed category $\mathcal{E}$ with a point-surjective $\varphi: A \to B^A$, every endomorphism $f: B \to B$ has a fixed point. Contrapositive: a fixed-point-free $f$ forces non-surjectivity of every candidate $\varphi$; instantiated for $\mathcal{E} = $ internal logic of $\mathcal{S}$, $B = \Omega$ (truth value object), $f = \neg$ (negation), this yields $\gamma_{\mathcal{S}}$ as above.

---

## §11 — Continuity / Integration (M40–M44)

### M40 — Continuous emergence [S]

Setup: parameter space $\mathrm{Param} \ni p$ (e.g., temperature $T$, coupling $\lambda$, threshold $\theta$); $E_{\mathrm{emerge}}: \mathrm{Param} \to \mathrm{Sub}(\mathcal{S})$ the emergence map.

Statement: there exist a critical parameter $p_c \in \mathrm{Param}$ and a natural order parameter $m(p) := \lVert F(p) \rVert$ (under some seminorm) such that
$$
m(p) = \left( \frac{\lvert p - p_c \rvert}{p_c} \right)^{\beta} \big( 1 + o(1) \big), \qquad p \to p_c,
$$
with critical exponent $\beta > 0$ (continuous, second-order or higher); no discontinuous jump at $p_c$. Equivalent in renormalization-group terms: $p_c$ is a fixed point with continuous spectrum of relevant operators.

### M41 — Integrated time slice

Setup: time slice state $\omega_t \in S(\mathcal{A})$ ($t \in \mathbb{R}$); decomposition $\mathcal{A} = \mathcal{A}_1 \otimes \mathcal{A}_2$ (when proposed).

Statement: *no canonical* tensor factorization exists, i.e.,
$$
\neg \Big( \exists \text{ natural family } (\mathcal{A}_1, \mathcal{A}_2, \omega_t^{(1)} \in S(\mathcal{A}_1), \omega_t^{(2)} \in S(\mathcal{A}_2)) \text{ with } \omega_t = \omega_t^{(1)} \otimes \omega_t^{(2)} \;\; \forall t \Big).
$$
Naturality is in the categorical sense: any such factorization, if it existed for one $t$, would be required (by naturality in $t$) to extend to all $t$; this extension is the obstruction.

### M42 — Distinguished modular generator [S]

Setup: as M32. $\mathcal{M}$ a von Neumann algebra; $\omega$ faithful normal; $\sigma_t^\omega$ modular flow.

Statement: the modular Hamiltonian
$$
H_\omega := -\log \Delta_\omega \quad (\text{self-adjoint, generally unbounded})
$$
is a *distinguished* generator in the following sense: in any GNS representation $\pi_\omega: \mathcal{M} \to \mathcal{B}(\mathcal{H}_\omega)$, the operator $H_\omega$ is canonically attached to $\omega$, and $\tau = 0$ (the identity automorphism $\sigma_0^\omega = \mathrm{id}$) is canonically marked. The clock data $(\omega, \sigma_t^\omega, H_\omega)$ is intrinsic to $\omega$, not added externally.

### M43 — Measurement as observable selection [O]

Setup: $\mathcal{A}$ $\ast$-algebra, $\omega \in S(\mathcal{A})$.

Statement (candidate): a measurement is the data of (i) a positive operator-valued measure (POVM)
$$
E: \mathrm{Borel}(Y) \to \mathcal{A} \quad (Y \text{ a measurable outcome space}), \qquad E(Y) = 1, \;\; E(B) \geq 0,
$$
and (ii) the induced probability outcome distribution
$$
\mathbb{P}_\omega^E(B) := \omega(E(B)), \qquad B \in \mathrm{Borel}(Y).
$$
The measurement map is
$$
\mathrm{Meas}: \mathrm{POVM}(\mathcal{A}) \times S(\mathcal{A}) \to \mathrm{Prob}(Y), \qquad (E, \omega) \mapsto \mathbb{P}_\omega^E.
$$
Open: precise categorical home (POVM in CP-map category? process matrix? operator-system morphism?); refinement to Lüders / sequential measurements.

### M44 — Time interval / germ / jet primitive [S]

Setup: $\mathcal{D}(\mathbb{R}) := C_c^\infty(\mathbb{R})$ test functions; $\mathcal{S}'(\mathbb{R}) = $ tempered distributions; $(\omega_t)_{t \in \mathbb{R}}$ an admissible family of states.

Statement: the primitive temporal datum is the smeared pairing
$$
\langle \psi, \omega \rangle := \int_{\mathbb{R}} \psi(t) \, \omega_t \, dt, \qquad \psi \in \mathcal{D}(\mathbb{R}),
$$
defined as a Bochner integral when $\omega_t$ is sufficiently regular (norm-continuous / weakly measurable). Pointwise $\omega_{t_0}$ is recovered only as a $\delta$-distributional limit $\psi \to \delta_{t_0}$; in general this limit need not exist as a state. Equivalent: the primitive object is a section of the germ sheaf $\mathrm{Germs}_{\mathbb{R}}(S(\mathcal{A}))$, not a point evaluation.

---

## §12 — Open conditions (O-grade), short legend

| $M_k$ | Open characterization (the gap, in one line) |
|---|---|
| M9 | Maximal admissible class of non-atomic frames under M6, M7, M10. |
| M18 | Canonical reduction map $R: \mathrm{ExternalData} \to L$. |
| M29 | Canonical native model of $\mathcal{M}_{\mathrm{cross}}$ (PAI core; OP-NEW-C). |
| M30 | Partial-coverage taxonomy $\mathrm{Cover}(F)$ for $\mathrm{Ob}_F \subsetneq \mathrm{Ob}(\mathcal{O})$. |
| M32 | Modular flow on non-Type-III or non-faithful $\omega$; canonical $\beta$. |
| M43 | Categorical home of POVM-based measurement (CP / process / op-system). |

---

## §13 — PAI vocabulary (NOT formalized here)

Symbols $\Delta_{\mathrm{interp}}(F), \mathcal{I}_{\mathrm{perc}}, \mathcal{I}_{\mathrm{act}}, \mathcal{A}_{\mathrm{PA}}(u), d_{\mathrm{PA}}, \mathrm{IPF}$ do *not* appear in any $M_k$ formula above. Their definition is the subject of OP-PAI-001..006; formalization is deferred.

---

## §14 — Symbol-dependency table

| introduced in | reused in |
|---|---|
| $\mathcal{C}, \mathcal{S}$ (preamble) | M1, M2, M3, M5, M19, M35, M41 |
| $\mathcal{O}, \pi, X^o$ (M6) | M4, M7, M8, M9, M10, M11, M24, M29, M30, M36 |
| $\varphi, L$ (M3) | M12, M13, M14, M15, M16, M17, M22, M40 |
| $\mathcal{H}_{\mathrm{bdry}}, h, g$ (M12, M13) | M14, M22, M35, M38 |
| $\mathcal{A}, \omega, S(\mathcal{A})$ (M23) | M15, M16, M17, M24, M25, M26, M32, M38, M41, M43 |
| $C_A(\tau), \theta_O$ (M17, M25) | M26, M31, M38 |
| $G_o$ (M27, M28) | M26, M29 |
| $\mathcal{M}_{\mathrm{cross}}$ (M29) | (M30 indirectly) |
| $\Delta_\omega, J_\omega, \sigma_t^\omega$ (M32) | M42 |
| $\mathrm{spec}(\mathcal{A}), \mathrm{supp}(\rho)$ (M33) | M31, M34 |
| POVM $E$ (M43) | (measurement-specific) |

---

## §15 — Changelog

- **v0 (2026-05-23)**: full mathematical statements for M1–M44 with explicit Setup / Data / Constraint per condition. All formulas LaTeX-rendered (`$...$` inline, `$$...$$` display). Notation key §1 unified. 6 O-grade conditions formulated as candidate definitions with open clause stated. PAI vocabulary kept out of all formulas (§13).

---

*Formula Catalog v0 — 2026-05-23.*
