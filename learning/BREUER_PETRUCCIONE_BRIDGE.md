# From open-system trajectories to a scalar transport algorithm

The single educational anchor is **Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems*** (Oxford University Press, original 2002). The [publisher's paperback/online record](https://academic.oup.com/book/27757) is dated 2007, DOI [10.1093/acprof:oso/9780199213900.001.0001](https://doi.org/10.1093/acprof:oso/9780199213900.001.0001). The chapter references below follow that record. Page numbers are omitted because editions differ.

Use the [30-milestone map](MILESTONES.md) alongside this bridge. The book supplies the open-system foundation; the project's topic pages supply its covariance reduction, source-bound proof, reversible circuit construction and estimation theorem. Research references establish attribution, rather than adding further educational anchors.

## Reading the anchor with a purpose

| Anchor location | Use in this project | Continue here |
|---|---|---|
| Chapter 1: classical probability and stochastic processes | Survival functions, exit-time means and sampling uncertainty | [Source balance](../science/source_balance.md) |
| Chapter 2: quantum probability | Density operators, effects and outcome probabilities | [Physical model](../science/model.md) |
| Chapter 3: quantum master equations | Markov generators, complete positivity and source/drain dynamics | [Physical model](../science/model.md) and [source balance](../science/source_balance.md) |
| Chapter 6: stochastic dynamics in Hilbert space | Conditioned evolution and trajectory descriptions | [Auxiliary absorption](../science/model.md#auxiliary-absorption-experiment) |
| Chapter 7: stochastic simulation | Measured-trajectory interpretation and sampling | [Matched comparison](../science/comparison.md#sampling-is-already-gap-independent) |

These are chapter-level pointers verified against the publisher's contents, not a claim that the book proves this algorithm or uses its notation. The explanations that follow connect the objects needed here.

## 1. Two state descriptions with different normalizations

A one-particle state is a positive matrix $`\rho`$ with trace one. Its diagonal gives site probabilities; off-diagonal entries describe coherence between sites. A purification is a normalized vector on a larger system whose reduced state is $`\rho`$. It lets a mixed source distribution enter a reversible circuit without measuring away its preparation record.

The many-fermion covariance is instead

```math
C_{xy}=\langle c_y^\dagger c_x\rangle,\qquad 0\preceq C\preceq I.
```

Its diagonal entries are orbital occupations. Its trace is a mean particle number, and can exceed one. A quadratic number-conserving Hamiltonian and linear injection/extraction jumps close an equation for this $`N\times N`$ matrix. Computing a covariance is already a classical reduction from the full fermionic Hilbert space; the quantum algorithm must be compared against that reduction.

## 2. From a master equation to the target current

Take a Hermitian one-particle Hamiltonian $`h`$ and diagonal contact-rate matrices $`\Gamma_L,\Gamma_R\succeq0`$. Left injection and right extraction at energy-independent occupations give

```math
A=-ih-(\Gamma_L+\Gamma_R)/2,\qquad
\dot C=AC+CA^\dagger+\Gamma_L.
```

The empty-network source solution is $`C_L=\int_0^\infty e^{At}\Gamma_Le^{A^\dagger t}dt`$. With $`W=\mathrm{Tr}\Gamma_L>0`$, the output is

```math
J_R=\mathrm{Tr}(\Gamma_R C_L),\qquad p_R=J_R/W.
```

Here $`W`$ is the bare injection rate. Physical injection into occupied orbitals is Pauli blocked. The [model](../science/model.md) fixes this convention; it is essential when giving the current an auxiliary one-particle interpretation.

## 3. No-jump evolution supplies an auxiliary experiment

Prepare $`\rho_L=\Gamma_L/W`$, propagate with $`K(t)=e^{At}`$, and permit absorption at **both** contacts. The unnormalized surviving state is $`K(t)\rho_LK(t)^\dagger`$. Its trace is the probability that no exit has yet occurred. Its lost trace is partitioned into left and right absorption.

```math
s(t)=\mathrm{Tr}[K(t)\rho_LK(t)^\dagger],\qquad
f_R(t)=\mathrm{Tr}[\Gamma_RK(t)\rho_LK(t)^\dagger],
\qquad p_R=\int_0^\infty f_R(t)dt.
```

The generator in this auxiliary experiment is related to, but is not the many-body no-jump generator of, the injection/extraction trajectory description. Reflection into the left contact is allowed. Thus its right-exit probability is a current per bare injection rate, not a fraction of successful physical injections. Chapter 6 motivates conditioned dynamics; the [project proof](../science/source_balance.md) establishes the particular equivalence being used.

## 4. Source compatibility controls the mean

The generator obeys $`A+A^\dagger=-\Gamma`$, where $`\Gamma=\Gamma_L+\Gamma_R`$. Since $`\Gamma_L\preceq\Gamma`$,

```math
\int_0^T K(t)\Gamma K(t)^\dagger dt=I-K(T)K(T)^\dagger,
\qquad 0\preceq C_L\preceq I.
```

Integrating survival gives

```math
\mathbb E\tau=\int_0^\infty s(t)dt
=\frac{\mathrm{Tr}C_L}{W}\le\frac NW=:S.
```

A nearly dark mode can have a very long lifetime but a small source weight. This bound controls their combined contribution. An arbitrary initial one-particle state need not satisfy it. Exactly dark, unreachable modes may prevent full-state convergence while carrying no lead current. The [source-balance page](../science/source_balance.md) proves these statements without assuming that $`A`$ is normal.

## 5. A trajectory can be sampled or retained coherently

In a measured trajectory, each sampled exit is a classical record. Repeating trajectories estimates $`p_R`$. Chapter 7 supplies the conceptual sampling route; the [comparison](../science/comparison.md) charges its variance and expected residence time.

For coherent estimation, each segment instead belongs to one reversible unitary. A jump, its lead, the time interval, and all nonzero temporary event work must remain distinguishable. The [compiler](../science/first_event_compiler.md) moves that complete information into one first-event record and reuses the segment workspace. It stops later segments on exited branches and reverses the construction explicitly. Tracing an environment in a mathematical channel description does not authorize erasing it inside this circuit.

The finite interval uses a no-exit operator and positive quadrature jump operators. Their stacked Gram matrix approximates the identity; oblivious amplification completes the approximate isometry. These implementation steps extend the textbook foundation and are proved and attributed in the compiler page.

## 6. Mean time is not the cost of ordinary amplitude estimation

Source balance gives $`s(T)\le S/T`$, so a horizon $`T=O(S/\epsilon)`$ bounds the omitted exit probability. Running ordinary amplitude estimation on that whole horizon would repeatedly pay its maximum length.

The [dyadic estimator](../science/estimation.md) instead divides exit times into doubling bands. A late band has small probability, while the stopped prefix has a bounded second moment. Known padding supplies a nonzero probability scale even for a band containing no right exits. Existing variable-time amplitude estimation combines those facts into

```math
C_0+\widetilde O\!\left(
\frac{(aN/W)C_B+C_P}{\epsilon}\right).
```

The book is not the source of this quantum estimation theorem. Its precise imported theorem, compiler error budget, maximum-time term and gate interpretation are given in [estimation](../science/estimation.md). [Access and precision](../science/access_and_precision.md) defines every charged resource, including setup, source preparation, controls and inverses.

## 7. Read the physical consequence at the requested precision

The [local slab](../science/local_slab.md) resolves a flux-dependent current difference while side modes decay very slowly. It is finite physical evidence, not a generic diffusion theorem or classical hardness argument. For total-current error $`\eta`$, substitute $`\epsilon=\eta/W`$; the leading propagation term becomes proportional to $`N/\eta`$. Relative error also depends on the current's magnitude.

Classical current-residual certificates and the [frequency sampler](../science/frequency_sampling.md) also avoid dependence on the original smallest decay rate. The synthesis is therefore an observable-specific algorithm and its paid implementation, with [matched baselines](../science/comparison.md), rather than an inference of practical advantage from a small gap. The [finite checks](../verification/README.md) test constructions and examples; the topic pages and cited primary theorems carry the universal arguments.
