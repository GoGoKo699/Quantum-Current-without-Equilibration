# Thirty milestones for understanding the project

The single educational anchor is **Breuer–Petruccione, *The Theory of Open Quantum Systems***. The [source bridge](BREUER_PETRUCCIONE_BRIDGE.md) identifies the original 2002 work, the verified 2007 publisher record, chapter pointers and notation. Below, **BP 1, 2, 3, 6, 7** mean chapters of that one book. Primary algorithm papers remain attribution sources in the scientific account.

The map has **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. Background moves from a single orbital to the complete physical and computational task. The narrative builds the source bound and coherent circuit locally, then integrates estimation, output accuracy, physical examples and fair comparison. Targets depend on the project, not on a particular learner's background. This is an understanding map, not a record of learner attempts or a claim to cover every technical detail.

## Background and preliminaries — M01–M14

### M01 — What does one orbital's occupation describe?

- **Target:** Explain occupation as an expectation between zero and one, distinct from a list of particle positions.
- **Dependencies and connection:** None. This is the local object from which the covariance description is assembled.
- **Read:** BP 2; [bridge §1](BREUER_PETRUCCIONE_BRIDGE.md#1-two-state-descriptions-with-different-normalizations); [model](../science/model.md).

### M02 — How does hopping carry phase information?

- **Target:** Relate a Hermitian hopping matrix to coherent superpositions and interference between paths.
- **Dependencies and connection:** M01. Connect local orbital labels to the Hamiltonian whose phases affect a transport signal.
- **Read:** BP 2; [model](../science/model.md); [flux example](../science/local_slab.md#a-resolved-phase-sensitive-transport-signal).

### M03 — How can a mixed source have a reversible preparation?

- **Target:** Distinguish a density operator, a classical mixture and a purification retaining a reference register.
- **Dependencies and connection:** M01–M02. Establish what source preparation must preserve before a circuit can be inverted.
- **Read:** BP 2; [bridge §1](BREUER_PETRUCCIONE_BRIDGE.md#1-two-state-descriptions-with-different-normalizations); [source access](../science/access_and_precision.md).

### M04 — Why is a fermionic covariance not a density matrix?

- **Target:** Explain the bounds on covariance eigenvalues, its particle-number trace, and closure for quadratic dynamics.
- **Dependencies and connection:** M01–M03. Join occupations and coherences into the many-fermion observable framework.
- **Read:** BP 2–3; [bridge §1](BREUER_PETRUCCIONE_BRIDGE.md#1-two-state-descriptions-with-different-normalizations); [model](../science/model.md).

### M05 — What information does a quantum operation retain?

- **Target:** Explain outcomes, Kraus operators and an isometric dilation; distinguish a channel's reduced description from its retained environment.
- **Dependencies and connection:** M03. Supply the operational meaning needed for a reversible simulation of loss.
- **Read:** BP 2–3; [bridge §5](BREUER_PETRUCCIONE_BRIDGE.md#5-a-trajectory-can-be-sampled-or-retained-coherently); [compiler](../science/first_event_compiler.md).

### M06 — What does the Markov assumption specify?

- **Target:** Interpret a time-independent generator and its semigroup without identifying it with an arbitrary microscopic reservoir.
- **Dependencies and connection:** M04–M05. Connect local quantum operations into continuous open-system evolution.
- **Read:** BP 3; [physical assumptions](../science/model.md#physical-model-and-requested-output).

### M07 — How do the two contacts drive the covariance?

- **Target:** Separate the Hamiltonian commutator, contact damping and left source term; identify the energy-independent occupations.
- **Dependencies and connection:** M04, M06. Build the specific driven network from the open-system framework.
- **Read:** BP 3; [bridge §2](BREUER_PETRUCCIONE_BRIDGE.md#2-from-a-master-equation-to-the-target-current); [model](../science/model.md).

### M08 — What is an unnormalized no-exit state?

- **Target:** Interpret its lost trace as exit probability, rather than renormalizing it away during a probability calculation.
- **Dependencies and connection:** M03, M05–M07. Introduce a single conditioned branch before combining all exit events.
- **Read:** BP 6; [auxiliary process](../science/model.md#auxiliary-absorption-experiment).

### M09 — How do exit densities become a lead probability?

- **Target:** Relate survival, its rate of decrease, and integrated left/right exit densities for absorption at both contacts.
- **Dependencies and connection:** M07–M08. Turn conditioned evolution into a normalized observable experiment.
- **Read:** BP 1, 6; [bridge §3](BREUER_PETRUCCIONE_BRIDGE.md#3-no-jump-evolution-supplies-an-auxiliary-experiment); [source balance](../science/source_balance.md).

### M10 — Which stopping-time moments affect computation?

- **Target:** Distinguish mean, maximum and root-mean-square duration and explain survival-integral formulas.
- **Dependencies and connection:** M09. Prepare the probabilistic language that separates rare slow events from uniform long runs.
- **Read:** BP 1, 7; [source-bound consequences](../science/source_balance.md#interpretation-and-useful-consequences); [estimation](../science/estimation.md).

### M11 — What does dissipative passivity imply locally?

- **Target:** Use the negative Hermitian part of the generator to explain contraction while allowing nonnormal dynamics.
- **Dependencies and connection:** M06–M08. Connect physical damping to the operator inequality later integrated into a capacity bound.
- **Read:** BP 3, 6; [source-balance proof](../science/source_balance.md#proof).

### M12 — What makes an input circuit efficiently accessible?

- **Target:** Distinguish procedural coefficient evaluation from arbitrary data loading; charge source preparation, normalization and inverses.
- **Dependencies and connection:** M02–M03, M05. Join the physical instance to an explicit computational input model.
- **Read:** [bridge §6](BREUER_PETRUCCIONE_BRIDGE.md#6-mean-time-is-not-the-cost-of-ordinary-amplitude-estimation); [access and precision](../science/access_and_precision.md).

### M13 — What changes when probabilities are estimated coherently?

- **Target:** Distinguish repeated measured trajectories from an algorithm that calls preparation and inverse circuits; retain both cost and error obligations.
- **Dependencies and connection:** M05, M09–M10, M12. Connect an observable probability to the kind of quantum computation used here.
- **Read:** BP 7 for the measured route; [bridge §5–6](BREUER_PETRUCCIONE_BRIDGE.md#5-a-trajectory-can-be-sampled-or-retained-coherently); [estimation](../science/estimation.md).

### M14 — What is the complete source-to-output task?

- **Target:** State the network, source distribution, scalar output, accuracy, confidence and paid access without confusing a covariance with a prepared quantum state.
- **Dependencies and connection:** M01–M13. Integrate the background into the full problem before examining the contribution.
- **Read:** [bridge §1–3](BREUER_PETRUCCIONE_BRIDGE.md#1-two-state-descriptions-with-different-normalizations); [model](../science/model.md); [access](../science/access_and_precision.md).

## Narrative and innovation — M15–M30

### M15 — How does source balance bound occupancy?

- **Target:** Derive the integrated passivity identity and use the source inequality to obtain a covariance bounded by the identity.
- **Dependencies and connection:** M07, M11, M14. This local operator mechanism starts the algorithm's resource argument.
- **Read:** BP 3 as foundation; [source-balance proof](../science/source_balance.md#proof).

### M16 — Why do dark sectors not destroy the current theorem?

- **Target:** Identify the reducing dark subspace, source orthogonality and current convergence even when the full covariance keeps rotating.
- **Dependencies and connection:** M09, M15. Establish the theorem's scope before using an infinite-time integral.
- **Read:** BP 3, 6 as foundation; [theorem and proof](../science/source_balance.md#the-theorem); [near-dark limit](../science/examples.md#a-continuous-time-near-dark-example).

### M17 — Why is the mean residence controlled by capacity?

- **Target:** Trace the source-driven integral to obtain the dimension-over-injection bound and explain why an arbitrary initial state lacks it.
- **Dependencies and connection:** M10, M15–M16. Convert occupancy into an algorithmically useful time scale.
- **Read:** [bridge §4](BREUER_PETRUCCIONE_BRIDGE.md#4-source-compatibility-controls-the-mean); [source balance](../science/source_balance.md).

### M18 — How much of a slow tail may be omitted?

- **Target:** Derive survival and truncated-second-moment bounds from the mean; choose a horizon at the requested additive accuracy.
- **Dependencies and connection:** M10, M17. Supply the finite-horizon and stopping-moment inputs for estimation.
- **Read:** [source-bound consequences](../science/source_balance.md#interpretation-and-useful-consequences); [error budget](../science/estimation.md#truncation-and-compiler-error-budget).

### M19 — What does one absorbing interval have to implement?

- **Target:** Partition the interval into no-exit and lead-labelled jump operators and explain why collective sink copies avoid a contact-area normalization penalty.
- **Dependencies and connection:** M05, M08–M09, M12. Build a local computational primitive from the physical process.
- **Read:** BP 6 as foundation; [finite Kraus stack](../science/first_event_compiler.md#a-short-interval-as-a-finite-kraus-stack).

### M20 — How is the continuum interval made finite?

- **Target:** Explain positive quadrature, Taylor approximation and dimension-independent error control without identifying quadrature nodes as measured jump times.
- **Dependencies and connection:** M11, M19. Make the local instrument finite at a charged precision.
- **Read:** [compiler](../science/first_event_compiler.md#a-short-interval-as-a-finite-kraus-stack); [related compilation tools](../references/RELATED_WORK.md#channel-compilation).

### M21 — What completes the approximate isometry?

- **Target:** Interpret the stacked Gram matrix, the amplification polynomial and the residual failure event; retain failure rather than postselecting it away.
- **Dependencies and connection:** M05, M19–M20. Connect the finite approximation to a unitary circuit with a quantified instrument error.
- **Read:** [oblivious amplification](../science/first_event_compiler.md#a-short-interval-as-a-finite-kraus-stack); [finite compiler checks](../verification/README.md).

### M22 — Where does the first event's information go?

- **Target:** Follow the event-work permutation and its inverse; explain exact work reuse and the memory cost of retaining the full nonzero label.
- **Dependencies and connection:** M03, M12, M21. Extend one segment into a reversible stopped trajectory without a growing environment tape.
- **Read:** [first-event memory](../science/first_event_compiler.md#reversible-first-event-memory); [workspace accounting](../science/access_and_precision.md#precision-and-workspace).

### M23 — Why use doubling exit-time bands?

- **Target:** Combine a late band's probability envelope with the stopped prefix's second moment; expose valid halt flags at geometric boundaries.
- **Dependencies and connection:** M18, M22. Link the physical residence bound to the variable-time circuit structure.
- **Read:** [dyadic estimator](../science/estimation.md#dyadic-variable-time-estimation).

### M24 — What does padding contribute to estimation?

- **Target:** Explain the known nonzero probability scale, subtraction of padding and probability-sensitive error allocation; keep the maximum-time term paid.
- **Dependencies and connection:** M13, M23. Apply the inherited variable-time theorem to each band, including empty bands.
- **Read:** [estimation proof](../science/estimation.md#dyadic-variable-time-estimation); [estimator attribution](../references/RELATED_WORK.md#variable-time-estimation).

### M25 — How do approximation and circuit costs fit together?

- **Target:** Combine tail, source and per-segment errors with stopping-moment stability, confidence and gate/ancilla costs into the stated bound.
- **Dependencies and connection:** M12, M18–M24. Integrate the local components into the full implemented scalar algorithm.
- **Read:** [estimation](../science/estimation.md); [access and precision](../science/access_and_precision.md).

### M26 — Which precision dependence is sharp, and in which model?

- **Target:** Convert normalized, total and relative current accuracy; interpret the clock-interferometer lower bound only under hidden unitary-step access.
- **Dependencies and connection:** M14, M25. Match the complete algorithm to its output units and to the actual lower-bound model.
- **Read:** [output precision](../science/access_and_precision.md#which-precision-is-physically-requested); [oracle sharpness](../science/examples.md#sharpness-in-the-discrete-step-oracle-model).

### M27 — What physical signal survives very slow side modes?

- **Target:** Explain the small weight of long-lived tails, the disconnected-limit qualification, and the explicitly resolved local flux response.
- **Dependencies and connection:** M16–M18, M26. Connect the theorem to physical witnesses at a stated signal accuracy.
- **Read:** [analytic examples](../science/examples.md); [local slab and flux](../science/local_slab.md); [verification](../verification/README.md).

### M28 — How can classical computation also avoid the original gap?

- **Target:** Explain observable-residual certification and controlled-loss frequency sampling, including their solve, arithmetic and sampling costs.
- **Dependencies and connection:** M10–M12, M17, M26. Build the strongest relevant comparison before drawing a computational conclusion.
- **Read:** BP 7 as sampling foundation; [classical certificates](../science/comparison.md#a-classical-current-certificate-that-does-not-use-the-decay-gap); [frequency sampler](../science/frequency_sampling.md).

### M29 — What changes across physical transport regimes?

- **Target:** Separate fixed additive and relative signals, conditional diffusive/localized substitutions, measured-trajectory variance and finite examples.
- **Dependencies and connection:** M25–M28. Compare complete methods at the same physical precision without treating a small gap as hardness.
- **Read:** [matched comparison](../science/comparison.md); [signal interpretation](BREUER_PETRUCCIONE_BRIDGE.md#7-read-the-physical-consequence-at-the-requested-precision).

### M30 — What does the complete contribution establish?

- **Target:** Connect physical source balance, charged coherent construction, scalar estimation and matched baselines; distinguish inherited tools, proved bounds, finite evidence and unproved practical advantage.
- **Dependencies and connection:** M14–M29. Synthesize the scientific story and its boundaries as one source-to-output result.
- **Read:** [model and route](../science/model.md); [bridge](BREUER_PETRUCCIONE_BRIDGE.md); [related work](../references/RELATED_WORK.md); [comparison](../science/comparison.md); [verification scope](../verification/README.md).
