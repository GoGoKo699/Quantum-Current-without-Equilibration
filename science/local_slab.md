# A nonseparable local transmitting slab

Consider an $`L\times L\times L`$ cubic lattice with unit nearest-neighbour hopping, fully specified bounded coordinate-dependent onsite terms, and rate $`\gamma`$ on every site of each opposite $`x`$-face. Attach a finite side arm through a bounded-height barrier to one interior site. A single arm of $`B+1`$ vertices gives

```math
 N=L^3+B+1,\qquad W=\gamma L^2,
 \qquad S=\frac{L^3+B+1}{\gamma L^2}.
```

Index arithmetic, coordinate mixing, diagonal-rate tests and uniform-face source preparation have explicit short reversible circuits. No table of $`N`$ arbitrary onsite coefficients is assumed. The [verification implementation](../verification/local_slab_check.py) uses a completely specified 32-bit coordinate-mixing function; its samples are deterministic irregular potentials, not a proof of i.i.d. disorder or of a diffusion law. For an asymptotic register-size family the integer width and its arithmetic cost must scale with the coordinate bit length.

Finite tests with $`L=3`$, $`\gamma=1`$, barriers of heights between 5.03 and 5.33 and all arm hoppings equal to one give:

| Barrier vertices $`B`$ | $`N`$ | Population decay gap | $`p`$ | Mean lifetime | $`N/W`$ |
|---:|---:|---:|---:|---:|---:|
| 1 | 29 | $`1.0850\times10^{-2}`$ | 0.391956 | 1.61467 | 3.22222 |
| 2 | 30 | $`4.3211\times10^{-4}`$ | 0.391934 | 1.67063 | 3.33333 |
| 3 | 31 | $`1.7896\times10^{-5}`$ | 0.391810 | 1.72639 | 3.44444 |
| 4 | 32 | $`7.0894\times10^{-7}`$ | 0.391779 | 1.78224 | 3.55556 |
| 5 | 33 | $`2.8892\times10^{-8}`$ | 0.391777 | 1.83806 | 3.66667 |
| 6 | 34 | $`1.1369\times10^{-9}`$ | 0.391779 | 1.89396 | 3.77778 |

The numeric trace-residual current certificates are below $`8\times10^{-15}`$ in these floating-point checks; they are not interval-arithmetic error bounds. The same code checks $`L=2,3,4`$ at $`B=1`$. These are nonseparable transmitting examples with small gaps. They establish no asymptotic transport regime or solver speedup. At an absolute fraction tolerance $`10^{-3}`$, their main transmitted current is resolved without resolving the slowest mode. Detecting the much smaller change due to a longer barrier requires a correspondingly smaller output tolerance.


## A resolved phase-sensitive transport signal

A useful output can compare the same sample at two flux values. Put a Peierls phase on each positive $`y`$ bond,

```math
h_{(x,y,z),(x,y+1,z)}=e^{i\phi x},
```

with its complex conjugate on the reverse bond; other nearest-neighbour hoppings remain one. Each elementary $`xy`$ plaquette then has a nontrivial loop phase of magnitude $`\phi`$. This modifies the phase-coherent transport without changing contact normalization, sparsity or coefficient magnitudes. The chosen $`\phi=\pi/2`$ phases are powers of $`i`$, so the procedural access circuit requires only elementary phase selection.

For the same $`L=3`$ sample, the verified integrated Markov currents are:

| Barrier $`B`$ | $`p_R(0)`$ | $`p_R(\pi/2)`$ | Difference | Decay gap at $`\pi/2`$ |
|---:|---:|---:|---:|---:|
| 1 | 0.391956 | 0.259242 | 0.132714 | $`1.0905\times10^{-2}`$ |
| 6 | 0.391779 | 0.258288 | 0.133491 | $`1.4872\times10^{-9}`$ |

Two scalar runs, each with additive current-fraction error $`10^{-3}`$, estimate the difference within $`2\times10^{-3}`$; the overall success probability is obtained by the usual confidence amplification and union bound. Both runs, their controls, inverses and output costs are charged. The signal remains resolved despite the long-lived side mode. This demonstrates a concrete phase-sensitive current task in the finite nonseparable sample. It does not establish its classical hardness, an asymptotic flux-response law or practical quantum advantage.

## Reproduction and meaning

Run `python3 verification/local_slab_check.py` from the repository root. The script writes `verification/results/local_slab_check.json` and checks occupancy, absorption normalization, the residence bound and residual certificates. Its exact finite model is defined in `model()`; no generated disorder file is required. The [verification guide](../verification/README.md) states the numerical scope.

For an explicit source-to-output circuit bound, the cubic backbone has degree at most six, a single attached arm adds at most one neighbour to its attachment site, and the two contact faces each have $`L^2`$ vertices. Uniform face preparation uses two uniform coordinate registers plus the fixed face coordinate. Row-neighbour lookup, onsite arithmetic and contact-rate tests have reversible descriptions. A 32-bit coordinate mixer specifies the small examples exactly; extending the family beyond that coordinate range requires choosing and charging a wider mixer, rather than claiming an infinite independent-disorder ensemble from a fixed finite seed.

The observable tested at useful accuracy is the main integrated Markov current fraction and its flux response, each at explicitly charged scalar precision. The finite examples resolve the flux response at $`10^{-3}`$ accuracy per run while allowing much slower modes to have negligible weight at that tolerance. It does not resolve every narrow resonance or the small difference between the last barrier lengths. The [comparison](comparison.md) explains the corresponding output precision and fair classical alternatives.
