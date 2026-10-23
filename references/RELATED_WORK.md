# Related work and attribution

The contribution developed in this repository is a source-compatible scalar-current guarantee with a compiled coherent first-event circuit. Its ingredients have substantial prior history. The account below separates those ingredients from the resulting physical task and resource statement. The comparison was checked against the indicated primary-source versions on 23 October 2026. It is a bounded literature comparison, not a certificate of priority or an exhaustive review.

## Physical current and residence time

**Jin, Filippone and Giamarchi (2020), [Generic transport formula for a system driven by Markovian reservoirs](https://arxiv.org/abs/2008.11747v1)**, and **Purkayastha (2022), [Lyapunov equation in open quantum systems and non-Hermitian physics](https://arxiv.org/abs/2201.00677v3)**, establish the transport and covariance/Lyapunov setting. The present filled-source/empty-drain model is a restricted energy-independent Markovian-reservoir problem. Its covariance equation and current interpretation are established physics, rather than a new reservoir formalism.

**Sinkovicz, Kiss and Asbóth (2016), [Generalized Kac's Lemma for Recurrence Time in Iterated Open Quantum Systems](https://arxiv.org/abs/1510.09031v2)**, relates mean recurrence to steady-state weight. **Davy, Kühmayer, Gigan and Rotter (2021), [Mean path length invariance in wave-scattering beyond the diffusive regime](https://arxiv.org/abs/2011.07146v1)**, investigates wave dwell/path-length invariance beyond diffusion. Their precise experiments and recurrence models differ from the auxiliary absorption process here, but they establish the broad ancestry of dimension/flux residence identities. This repository does not claim a new conservation law. Its [source-balance theorem](../science/source_balance.md) proves the particular operator identity needed for the algorithm, including nonnormal generators and unreachable dark sectors.

## Variable-time estimation

<a id="cgj2018"></a>
**Chakraborty, Gilyén and Jeffery, [The power of block-encoded matrix powers](https://arxiv.org/abs/1804.01973v2)**, arXiv v2 (2018), ICALP (2019), Theorem 23, supplies the variable-time amplitude-estimation theorem used here. Its cost depends on maximum time, root-mean-square stopping time, source preparation, and success probability. This is an imported quantum primitive.

**Huang, Li, Zhang, Wu and Zhang, [Breaking the Multiplicative Overhead in Quantum Entropy Estimation](https://arxiv.org/pdf/2609.40179)** (2026), Section 3.3 and Appendix C, explicitly develops probability-sensitive, calibrated variable-time estimation. The padding construction in its Eq. (28) ensures a known probability scale even when the target probability vanishes. The [dyadic estimator](../science/estimation.md) applies this existing approach to exit-time bands whose probability and second moment are controlled by source balance. The estimator itself is not presented as a new generic amplitude-estimation method. The linked PDF was inspected; its abstract-page version metadata was unavailable during this check.

## Channel compilation

**Li and Wang, [Simulating Markovian open quantum systems using higher-order series expansion](https://arxiv.org/abs/2212.02051v2)** (2023), uses Duhamel expansions, positive Gaussian quadrature, and quantum channel implementations with polylogarithmic precision overhead. These are precedents for the short-time approximation strategy.

<a id="borras2026"></a>
**Borras and Marvian, [Quantum simulation algorithms based on quantum trajectories](https://arxiv.org/html/2509.10425v2)**, arXiv v2 (8 April 2026), contains CP-map block encoding and oblivious amplification for isometries in Lemmas 1–2. Its complete trajectory algorithm assumes a representation with a scalar total jump rate, Eq. (19). Boundary-only loss is not generally such a representation. The present [compiler](../science/first_event_compiler.md) uses those local tools, an absorbing construction with at most one event, and an explicit reversible permutation retaining the complete nonzero segment-work label. The local tools and quadrature are inherited; the specific work-return/history argument is part of this repository's construction. The arXiv abstract metadata uses the shorter title *Quantum algorithms based on quantum trajectories*; the linked v2 full text supplies the title used here.

## Closest quantum task-level comparisons

<a id="simon2026"></a>
**Simon, Berry and Somma, [Efficient quantum algorithm for linear matrix differential equations and applications to open quantum systems](https://arxiv.org/abs/2605.16195v1)** (2026), gives finite-time matrix-entry estimation and an end-to-end free-fermion open-system application, with explicit access and classical comparisons. It already supplies compressed one-particle computation and broad dissipative matrix-equation algorithms. The distinction here is the infinite-time, source-balanced scalar boundary current, its residence-time truncation and stopped estimator, and its explicit event-history implementation. A generic claim of the first compressed free-fermion open-system algorithm would therefore be incorrect.

<a id="benedetti2026"></a>
**Benedetti, Rosmanis and Rosenkranz, [Probabilistic quantum algorithm for Lyapunov equations and matrix inversion](https://arxiv.org/abs/2508.04689v2)**, published version (17 April 2026), prepares mixed states proportional in expectation to Lyapunov solutions. The quoted Lyapunov guarantees assume normal coefficient matrices and stable spectral/norm cutoffs. A boundary generator is generally nonnormal, and the required output here is an unnormalized scalar current. Their normalized-solution guarantee therefore does not directly supply the present result; scalar extraction and source normalization must still be charged. Appendix F is a useful route to further quantum Lyapunov/Sylvester comparisons.

**Guan, Wang and Ying, [An HHL-Based Algorithm for Computing Hitting Probabilities of Quantum Random Walks](https://arxiv.org/abs/2009.03618v2)** (2021), is direct absorption-probability ancestry. It reduces hitting probabilities to matrix inversion, with condition-dependent quantum linear algebra. This prevents any claim that quantum absorption-probability computation is introduced here. The relevant distinction is the source-compatible mean-residence guarantee and complete controlled/inverse circuit cost.

**Chen and Chan, [Quantum linear algebra for disordered electrons](https://arxiv.org/abs/2411.00434v2)** (2025), develops block-encoded disordered Hamiltonians, Green functions, density matrices, conductivity, and quantum trace/amplitude estimation. Its procedural input model and one-particle compression are close predecessors. The reservoir observable and source-balance mechanism studied here differ from its broadened Green-function and Kubo-type targets. The paper also explicitly discusses polynomial, rather than automatic exponential-in-volume, advantage in local lattices.

## Transducers and amortized query costs

**Belovs, Jeffery and Yolcu, [Taming Quantum Time Complexity](https://arxiv.org/abs/2311.15873v3)** (2024), develops transducers, query compression, and subroutine composition. **Cornelissen, Apers and Gribling, [Improved quantum volume estimation with transducers and amortized quantum walks](https://arxiv.org/abs/2609.40217v2)** (5 October 2026), includes bounded-mean estimation in Theorem 3.7 and padded indicators in Theorem 3.8. Generic expected/amortized query-order consequences cannot be treated as novel merely by rephrasing them as absorption estimation. Query complexity, circuit time, and workspace remain different obligations. Cornelissen et al. explicitly discuss a loss of time efficiency for part of their construction. This repository gives the particular segment, inverse, and event-record circuits rather than inferring a gate bound solely from a generic compressed query count.

## Classical transport comparison

<a id="waintal2026"></a>
**Waintal et al., [Computational quantum transport: a scattering approach perspective](https://arxiv.org/abs/2407.16257v3)** (23 July 2026), is a pedagogical review of coherent scattering, Green functions, and sparse-elimination algorithms. These methods, together with Lyapunov, ADI, rational Krylov and source-probed time propagation, are necessary competitors. The Markov current is an energy-integrated quantity, so a cost for one energy point is not automatically its complete cost. The [matched comparison](../science/comparison.md) retains integration and solve costs, current-specific residual certificates, and the accuracy needed for the physical signal. A small dissipative gap is not a classical runtime lower bound. No universal classical separation or hardware advantage follows from the gap-independent quantum upper bound or the discrete oracle lower bound.

## What is added and what remains conditional

The supported scientific statement combines a physically fixed source, a gap-independent residence bound, a coherent first-event circuit with retained information and explicit inverses, and probability-sensitive estimation of the scalar current. The [input account](../science/access_and_precision.md) charges preparation, normalization, finite arithmetic, controls and setup. The [examples](../science/examples.md) exhibit appreciable transmission with very slow modes, without certifying classical hardness.

A practical advantage for a particular material, disorder distribution, or fault-tolerant implementation requires a matched complete resource comparison. Conditional transport promises, finite numerical witnesses, oracle lower bounds and hardware performance are distinct forms of evidence.

The [structured bibliography](references.bib) records the source identities and inspected versions.
