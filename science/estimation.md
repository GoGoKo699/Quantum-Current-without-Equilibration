# Dyadic current estimation

## Statement and access requirements

Let a one-particle absorption experiment start in a supplied purification of
$`\rho_L=\Gamma_L/W`$, with $`A=-ih-\Gamma/2`$,
$`\Gamma=\Gamma_L+\Gamma_R`$, and $`W=\operatorname{Tr}\Gamma_L>0`$.
Suppose its mean exit time obeys $`\mathbb E\tau\le S`$, where the source-balance
theorem supplies $`S=N/W`$. The aim is one number: the probability $`p_R`$ of
right absorption.

Assume compiled circuits for a block encoding of $`h/\alpha_h`$, reversible
evaluation of the nonnegative diagonal rates, and a purification of
$`\Gamma_L/W`$. Their controlled versions and inverses are required and charged.
Let $`\gamma_{\max}\ge\|\Gamma\|`$, $`a=\alpha_h+\gamma_{\max}`$, and
$`\Delta=1/(32a)`$. The normalization $`W`$ is supplied or computed at charged
setup cost. A completely arbitrary diagonal table or arbitrary source state is
not an efficient input by assumption.

For $`0<\epsilon<1/8`$ and failure probability $`\zeta`$, the construction below
estimates $`p_R`$ to additive error $`\epsilon`$ with probability at least
$`1-\zeta`$, using

```math
C_0+\widetilde O\!\left(
\frac{(1+aS)C_B+C_P}{\epsilon}
\right)
```

elementary gates. Here $`C_B`$ charges one controlled input block-encoding or
rate-arithmetic call, its inverse, and the associated register operations;
$`C_P`$ charges source preparation, its inverse, and reflection about its clean
input. The tilde hides polynomial logarithms in $`aS/\epsilon`$, $`1/\zeta`$,
and the precision and register sizes required by those circuits. Equivalently,
one can avoid conventions about $`C_B`$ and state the exact modular bound
$`C_0+\widetilde O((B C_{\rm step}+C_P)/\epsilon)`$, with
$`B=1+S/\Delta`$ and $`C_{\rm step}`$ the actual finite-gate cost of the
short-interval circuit below. If the supplied input circuits have expensive
precision dependence, that dependence belongs in $`C_{\rm step}`$.

The result uses existing variable-time amplitude estimation. It neither
establishes a classical lower bound nor a hardware crossover.

## Truncation and compiler-error budget

Round an exact physical exit upward to an interval endpoint and call its index
$`X`$. Then

```math
\mathbb EX\le1+S/\Delta=:B,\qquad
\Pr(X>n)\le B/n.
```

Choose $`n_*\ge16B/\epsilon`$. The unobserved right-exit tail is at most
$`\epsilon/16`$. A prefix of $`n`$ compiled intervals changes any live
survival or lead/time-bin probability by at most $`O(n\eta)`$. This follows
by telescoping the instrument diamond errors. One may dephase event labels
when analyzing these probabilities, because later operations never recombine
them. This analytical dephasing is not a reset performed by the algorithm.

For an integer stopping index,

```math
\mathbb E\min(X,n)^2
=\sum_{k=0}^{n-1}(2k+1)\Pr(X>k)\le2nB.
```

The compiled stopped process therefore has squared RMS duration bounded by
$`O(Bn)+O(\eta n^3)`$, in interval units. For
$`m=O(\log(1/\epsilon))`$ dyadic output bins, take
$`\eta\le c\epsilon/(m n_*)`$, with a sufficiently small absolute constant
$`c`$. Then all bin biases are within their allocated error and
$`\eta n^3=O(Bn)`$ for every $`n\le n_*`$. All demanded precision is
logarithmic in $`B/\epsilon`$. Source-preparation error may be set to
$`O(\epsilon/m)`$; unlike interval error, it is not incurred anew each step.

## Dyadic variable-time estimation

Use endpoints $`n_j`$ doubling from $`\Theta(B)`$ through $`n_*`$. Let
$`p_j`$ be right absorption in the first bin or in
$`(n_{j-1},n_j]`$. A known envelope
$`q_j=\min(1,c'B/n_{j-1})`$ bounds the actual compiled bin probability, with
an appropriate constant $`c'`$ accounting for the previous error budget.
For the first bin take $`q_0=1`$.

The bin circuit stops at its first event or deadline $`n_j`$. For the
variable-time theorem it is sufficient to expose halt flags at geometrically
spaced boundaries, rounding the stopping cost upward by at most a constant
factor. Each stage sets a fresh halt flag; later stages control on all earlier
flags being unset. Final good status asks whether the retained event belongs
to the right lead and selected bin. Thus the stages have valid controlled
inverses and satisfy the stopped-subspace requirement.

Pad the circuit with a fair selector: one branch halts immediately and is good
with known probability $`q_j`$; the other runs the trajectory. Its good
probability is

```math
\widetilde p_j=(q_j+p_j)/2=\Theta(q_j),
```

so a known nonzero lower bound exists even when $`p_j=0`$. Subtract the known
padding after estimation. Set relative tolerance
$`r_j=\Theta(\delta_j/q_j)`$, where
$`\delta_j=\Theta(\epsilon/m)`$. Chakraborty, Gilyén and Jeffery,
arXiv:1804.01973v2, Theorem 23, gives gate cost, up to its explicit logarithms,

```math
\frac{n_j C_{\rm step}q_j
+C_{\rm step}\sqrt{Bn_jq_j}
+C_P\sqrt{q_j}}{\delta_j}
=O\!\left(\frac{B C_{\rm step}+C_P}{\delta_j}\right).
```

This follows from their relative-error cost
$`\widetilde O((T_{\max}+(T_{\rm rms}+C_P)/\sqrt p)/r)`$, with
$`p=\Theta(q_j)`$. In particular the $`T_{\max}`$ term is charged; it is not
discarded in favor of an expected runtime. Calling ordinary fixed-time
amplitude estimation instead would not prove the stated result.

Summing the bins, assigning failure probability $`O(\zeta/m)`$ to each,
and adding tail, input and compilation errors proves the claimed bound. The
extra factors $`m^2`$ from equal error allocation are logarithmic. The
longest prefix also costs $`O(B C_{\rm step}/\epsilon)`$, within the same
bound. Treating elementary gates as unit-cost queried operations and charging
the theorem's register reflections converts its query accounting to this
circuit-gate statement; it does not posit a variable-cost black-box oracle.

The algorithm estimates the probability of the actual finite unitary circuit.
It needs instrument-probability and stopping-moment approximation, not an
operator-norm approximation between incompatible continuum and finite
environment purifications.


## Attribution and scope

The source-balanced physical task and its charged first-event implementation combine inherited passivity, Taylor LCU, Kraus stacking, oblivious amplification, and variable-time estimation. The [compiler](first_event_compiler.md) retains the complete precision-dependent segment work in one event record. The [comparison](comparison.md) treats measured trajectories and steady-state classical solvers under the same physical output.
