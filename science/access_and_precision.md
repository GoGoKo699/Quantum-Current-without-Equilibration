# Compiled inputs and output accuracy

## Access is part of the problem

Let $`n=\lceil\log_2N\rceil`$. Specify a reversible circuit for a block encoding of $`h/\alpha_h`$, with a known $`\alpha_h\ge\|h\|`$. Its implementation, controls, inverse, and clean work registers are charged. Also specify reversible evaluation of the diagonal rates, controlled rotations for their square roots, and source preparation

```math
V_L|0\rangle=|\Phi_L\rangle,\qquad
\operatorname{Tr}_{\rm ref}|\Phi_L\rangle\langle\Phi_L|=\Gamma_L/W.
```

Both $`V_L`$ and $`V_L^\dagger`$ must be implemented. Let $`C_P`$ be their gate cost. Let $`C_0`$ contain classical preprocessing, compilation, normalization computation, and any input loading. $`W`$ is known or computed at this charged cost; access to rate values alone does not supply their trace or the required distribution for free.

Use $`a=\alpha_h+\|\Gamma\|`$ and a constant-size interval $`\Delta=\Theta(1/a)`$. Let $`C_{\rm seg}(\zeta)`$ denote the gate cost of the short-interval unitary, including its control and inverse, event compression, finite arithmetic, and synthesis, at channel error $`\zeta`$. The [compiler](first_event_compiler.md) supplies a polylogarithmic precision overhead over the given block-encoding and rate circuits. Writing $`C_B`$ for these compiled access costs suppresses only stated polylogarithmic factors; it never denotes a cost-free black box.

The resulting [estimation bound](estimation.md) is

```math
C_0+\widetilde O\!\left(
\frac{(aN/W)C_B+C_P}{\epsilon}
\right).
```

Since $`W\le N\|\Gamma\|`$, $`aN/W\ge1`$; the interval-count offset is absorbed by this leading term. The tilde hides logarithms in $`aN/(W\epsilon)`$, confidence, and circuit precision, including quadrature, Taylor, arithmetic, and stopping-register operations. There is no claimed leading constant, native $`T`$ count, error-correction architecture, or hardware crossover.

## A concrete input family with no QRAM

For a bounded-degree geometric graph, neighbors and hopping values can be computed reversibly from a vertex label and a short edge label. Bounded rates are evaluated from the same labels. Standard sparse-access block encoding then has normalization controlled by degree times the largest entry, with the evaluation circuit and its work counted. Padding invalid vertex labels uses an isolated zero-source sector and does not alter the target; the mathematical capacity bound can still use the actual number of orbitals.

For a rectangular full-face left contact with $`M`$ sites at common rate $`\gamma`$, use reversible integer indexing and uniform superposition preparation over $`0,\ldots,M-1`$, followed by copying the site label to a reference. This gives

```math
|\Phi_L\rangle=M^{-1/2}\sum_{x\in L}|x\rangle|x\rangle,
\qquad W=\gamma M.
```

Non-power-of-two ranges can be prepared with charged arithmetic and rotations to the chosen precision. This is an explicit circuit for one distribution, not free access to an arbitrary stored array. A succinct deterministic disorder generator defines a restricted input family: its seed, evaluation time, and bit precision are part of the input. It does not efficiently load every independently measured disorder realization.

If $`N`$ arbitrary coefficients must be read and compiled, include that setup cost before claiming any subvolume end-to-end scaling. Reusing a compiled instance across several observables may amortize setup, but changes the comparison and must be stated.

## Precision and workspace

The truncation horizon in physical units is $`T=\Theta(N/(W\epsilon))`$. Segment error is chosen inverse polynomially small in the interval count and $`1/\epsilon`$ so accumulated probability bias and stopped-time second moments remain bounded. Thus finite descriptions need logarithmic accuracy overhead, with arithmetic costs evaluated at that precision. A computed source distribution and a computed $`W`$ also need error budgets; a source trace-distance error $`O(\epsilon)`$ changes any exit probability by $`O(\epsilon)`$.

For a generator approximation with norm error $`d_A`$, Duhamel's formula for two contraction semigroups gives $`\|K(t)-\widetilde K(t)\|\le t d_A`$. A full absorbing-channel approximation is budgeted uniformly through the same segment-error argument, including rate and source errors. The headline formula assumes the supplied circuits meet those tolerances; precision in input parameters is not supplied by the theorem.

The trajectory keeps one position register, its source reference, a first-event time, the entire event/segment-work label, and reusable short-segment work. Their size is logarithmic in the horizon plus the actual source and compiler workspace. The variable-time estimation wrapper can retain a logarithmic number of stopping flags and its estimation registers. It does not require an environment register for every interval. A logarithmic-memory statement concerns dependence on $`N`$ and the horizon when the specified access circuits themselves have polylogarithmic workspace.

## Which precision is physically requested?

For absolute total-current error $`\eta`$, substituting $`\epsilon=\eta/W`$ yields

```math
C_0+\widetilde O\!\left(
\frac{aN C_B+W C_P}{\eta}\right).
```

The contact-area improvement cancels in the leading propagation term. If the desired relative error is $`\delta`$ and a lower bound $`p_R\ge p_*>0`$ is supplied, taking $`\epsilon=\Theta(\delta p_*)`$ is sufficient. No uniform relative guarantee at a vanishing current follows from a fixed additive-error theorem. The [comparison](comparison.md) treats normalized, total, and interference-scale signals separately.
