# Matched current-computation resources

This account compares methods for the same filled-source/empty-drain Markovian free-fermion current. It supports a gap-independent scalar task and a conditional circuit bound. It establishes neither a lower bound against all classical algorithms nor a practical hardware advantage.

## Output and paid input

Let

```math
 A=-ih-\Gamma/2,\qquad \Gamma=\Gamma_L+\Gamma_R,
 \quad W=\mathrm{Tr}\Gamma_L>0,
 \quad S=N/W.
```

The source-driven covariance and current fraction in the [physical model](model.md) are

```math
 C=\int_0^\infty e^{At}\Gamma_L e^{A^\dagger t}\,dt,
 \qquad J_R=\mathrm{Tr}(\Gamma_R C),
 \qquad p=J_R/W.
```

The current is integrated over the energy-independent Markov source. It is not a single-energy transmission or a finite-temperature conductance. The source-compatible auxiliary first-exit process has mean lifetime at most $`S`$. Its small decay gap is not, by itself, an obstruction to estimating $`p`$ classically or quantum mechanically.

For the circuit comparison, let $`a`$ be the charged short-time simulation normalization, of order the available Hamiltonian block-encoding normalization plus the maximum contact rate. Let $`C_B`$ be the actual controlled/inverse block-access cost, $`C_P`$ the controlled/inverse source-purification cost, and $`C_0`$ the setup cost. The [coherent theorem](estimation.md), under its stated access assumptions, is

```math
 G_Q(\epsilon)=C_0+
 \widetilde O\!\left(\frac{aS C_B+C_P}{\epsilon}\right).
```

For absolute current error $`\eta`$, $`\epsilon=\eta/W`$, so

```math
 G_Q(\eta)=C_0+
 \widetilde O\!\left(\frac{aN C_B+W C_P}{\eta}\right).
```

In particular, a large contact area does not improve the leading size bound at fixed absolute error in total current. A subvolume end-to-end cost requires succinct coefficients or paid reuse across multiple calculations. Loading an arbitrary measured disorder sample costs at least its input length; an efficient procedural instance is a different, explicit input model.

## A classical current certificate that does not use the decay gap

Define the right-absorption effect

```math
 E_R=\int_0^\infty e^{A^\dagger t}\Gamma_R e^{At}\,dt.
```

The integral is well defined on the dissipative sector and vanishes on the reducing dark sector. Passivity gives

```math
 0\le E_R\le I,\qquad A^\dagger E_R+E_R A=-\Gamma_R,
 \qquad J_R=\mathrm{Tr}(E_R\Gamma_L).
```

For any Hermitian approximation $`\widehat C`$, form its Lyapunov residual

```math
 R=A\widehat C+\widehat C A^\dagger+\Gamma_L.
```

A trace calculation gives the exact scalar error identity

```math
 J_R-\mathrm{Tr}(\Gamma_R\widehat C)
 =\mathrm{Tr}(E_RR).
```

Consequently, writing $`R=R_+-R_-`$ for its positive and negative parts,

```math
 -\mathrm{Tr}R_-
 \le J_R-\widehat J_R\le\mathrm{Tr}R_+,
 \qquad
 |p-\widehat p|\le
 \frac{\max\{\mathrm{Tr}R_+,\mathrm{Tr}R_-\}}W
 \le\frac{\|R\|_1}W.
```

This certificate uses a trace/nuclear norm, not merely the operator-norm residual. The always valid weaker bound is $`N\|R\|/W`$. A residual of low rank can be evaluated through a small Gram matrix rather than an $`N\times N`$ eigendecomposition. If $`R\ge0`$, as for standard positive-residual Gramian approximations, $`\widehat J_R`$ is a lower bound and the interval width is $`\mathrm{Tr}R`$. These facts do not promise rapid low-rank convergence, but they prevent an unfair inference that a small dissipative gap necessarily requires inverse-gap accuracy to certify the current. Finite-time propagation is the special case $`R=e^{AT}\Gamma_L e^{A^\dagger T}`$.

The certificate is an adjoint/observable-weighted residual argument. It is not a novel general Lyapunov solver. Low-rank ADI and rational Krylov methods remain serious competitors; source rank is contact area, but the stationary covariance can still have extensive rank. Low rank of the source does not guarantee low rank of the answer. See Li and White, *Low Rank Solution of Lyapunov Equations*, SIAM J. Matrix Anal. Appl. **24**, 260–280 (2002), DOI [10.1137/S0895479801384937](https://doi.org/10.1137/S0895479801384937), and Wolf and Panzer, [arXiv:1309.3985](https://arxiv.org/abs/1309.3985), for the established ADI/model-reduction setting.

## Sampling is already gap independent

A measured quantum first-exit trajectory has expected evolution work at most $`aS`$. Its right-exit indicator is Bernoulli with variance $`p(1-p)`$. With a suitable known bound or an adaptive sampling procedure, additive error $`\epsilon`$ with failure probability $`\zeta`$ requires

```math
 M=O\!\left[\left(\frac{p(1-p)}{\epsilon^2}
                  +\frac1\epsilon\right)\log\frac1\zeta\right].
```

Thus expected measured-trajectory quantum work is

```math
 C_0+\widetilde O\!\left[(aS C_B+C_P)
 \left(\frac p{\epsilon^2}+\frac1\epsilon\right)\right].
```

For fixed relative error $`\delta`$ and $`p>0`$, this is
$`\widetilde O((aS C_B+C_P)/(\delta^2p))`$, whereas the retained coherent worst-case theorem gives
$`\widetilde O((aS C_B+C_P)/(\delta p))`$. In a diffusive scaling where $`p`$ itself decreases with length, these bounds have the same length exponent; the proved comparison is the precision improvement in $`\delta`$. The simpler $`S/\epsilon^2`$ baseline misses this variance benefit.

A classical trajectory for this process is a coherent wavefunction over sites. Replacing it by a particle random walk changes the observable unless a justified dephasing/semiclassical approximation applies. Sparse full-vector evolution typically costs $`O(N)`$ per unit simulation time, with light-cone or compressibility reductions where available. These are upper bounds for particular methods, not universal classical lower bounds. Expected-time sampling and bounded coherent circuit runtime must be labelled separately; heavy tails can make high-probability runtime accounting materially different.

## Energy-domain competitors compute the entire integral

On the active sector, Parseval gives

```math
 J_R=\frac1{2\pi}\int_{-\infty}^{\infty}
 \mathrm{Tr}\!\left[
 \Gamma_R G(E)\Gamma_LG(E)^\dagger\right]dE,
 \qquad G(E)=(E I-h+i\Gamma/2)^{-1}.
```

A real-axis singularity on an exactly dark subspace is interpreted through the active-space restriction or a vanishing positive regularization; contacts annihilate that dark sector. An RGF or sparse-direct cost at one energy must therefore be multiplied by the actual integration cost. Narrow resonances preclude an unsupported constant or polylogarithmic uniform-quadrature count.

There is nevertheless a constructive gap-independent classical regularization. Put $`A_\kappa=A-\kappa I`$ and use $`G_\kappa(E)=(EI-h+i\Gamma/2+i\kappa I)^{-1}`$. The regularized right probability is

```math
 p_\kappa=\mathbb E[e^{-2\kappa\tau}\mathbf1_R],
 \qquad 0\le p-p_\kappa\le 2\kappa\mathbb E\tau\le2\kappa S.
```

Choosing $`\kappa=\epsilon/(4S)`$ assigns at most $`\epsilon/2`$ bias, while every real-energy resolvent satisfies $`\|G_\kappa(E)\|\le1/\kappa`$. Thus neither numerical solve conditioning nor convergence need be governed by the original arbitrarily small gap. A deterministic quadrature still requires an honest node/error analysis; denote its charged number of nodes by $`Q_E(\epsilon)`$. The regularization controls the original-gap dependence but does not make this count free. Alternatively, the [bounded Cauchy frequency/source sampler](frequency_sampling.md) proves a finite algorithm for equal-rate contacts using $`O(\epsilon^{-2}\log(1/\zeta))`$ samples at bounded physical scales. It includes finite random bits, certified shifted solves and the full bias allocation. Each sample pays one sparse solve and a drain norm; the per-solve work below is not free.

For a geometrically local cube of side $`L`$ in three dimensions, nested dissection has the standard separator recurrence $`F(L)=8F(L/2)+O(L^6)`$, giving $`O(L^6)=O(N^2)`$ factorization work in arithmetic without adverse pivoting fill. Factors occupy $`O(L^4)`$ entries. With $`r=\Theta(L^2)`$ contact right-hand sides, their back-solves are also $`O(L^6)`$. Ordinary slice RGF gives $`O(L^7)`$ at one energy. These are geometry-based method bounds; numerical bit precision, integration nodes $`Q`$, pivoting behaviour and iterative alternatives remain charged. The Waintal et al. review explicitly explains modern sparse elimination and RGF competition: *Computational quantum transport: a scattering approach perspective*, [arXiv:2407.16257v3](https://arxiv.org/html/2407.16257v3), especially Sections 6.2–6.5. Its 2D nested-dissection example cannot be quoted as the full 3D Markov-current runtime.

## Physical precision on a local slab

The [explicit irregular three-dimensional slab](local_slab.md) has full-face contacts, bounded local coefficients and a side barrier. It gives finite nonseparable transmitting examples with small gaps. Its asymptotic transmission is not assumed in the unconditional current theorem.

For this family with $`B=O(L^3)`$, bounded $`a,\gamma`$, and efficiently computed onsite terms, the following are **conditional substitutions into the current theorem**:

| Required physical precision | Assumption | Coherent leading bound, ignoring access polylogs |
|---|---|---:|
| Constant additive current fraction $`\epsilon`$ | none | $`\widetilde O(L/\epsilon)`$ |
| Relative error $`\delta`$, transmitting regime | $`p=\Theta(1)`$ | $`\widetilde O(L/\delta)`$ |
| Relative error $`\delta`$, diffusive regime | $`p=\Theta(\ell/L)`$ | $`\widetilde O(L^2/(\delta\ell))`$ |
| Relative error $`\delta`$, localized regime | $`p=\Theta(e^{-L/\xi})`$ | $`\widetilde O(L e^{L/\xi}/\delta)`$ |
| Absolute total-current error $`\eta`$ | none | $`\widetilde O(L^3/\eta)`$ |

Here $`\ell`$ and $`\xi`$ denote an assumed transport length and localization length. The generic coherent Anderson slab does not come with a proved diffusion law in this analysis. A transmitting promise can be imposed explicitly, but must not be represented as proved for an entire ensemble from the small tests. A coarse ensemble current may be predictable by diffusion/homogenization, whereas resolving a sample-specific order-one correction to total current demands $`\epsilon=O(L^{-2})`$ and restores the volume-size bound. The energy-integrated Markov current should not inherit single-energy universal-conductance-fluctuation amplitudes without a separate analysis.

## Nearest quantum baselines and retained conclusion

Simon, Berry and Somma, [arXiv:2605.16195v1](https://arxiv.org/html/2605.16195v1), already give compressed-access algorithms for finite-time matrix equations and free-fermion dynamics, with explicit classical locality comparisons. Chen and Chan, [arXiv:2411.00434v2](https://arxiv.org/html/2411.00434v2), already supply procedural-disorder access and scalar electronic observables; one-particle compression is inherited. Benedetti, Rosmanis and Rosenkranz, [arXiv:2508.04689](https://arxiv.org/abs/2508.04689), study quantum Lyapunov state preparation under assumptions different from general nonnormal boundary damping. Guan, Wang and Ying, [arXiv:2009.03618](https://arxiv.org/abs/2009.03618), already estimate quantum-walk absorption probabilities through linear systems. None should be described as a full-state or long-time physical simulation that necessarily pays the same inverse gap.

The supported contribution is a physically specified infinite-time scalar current guarantee controlled by source-weighted residence, with coherent precision estimation and explicit circuit costs under the stated block-access and simulation assumptions. The useful physical examples show why equilibration time is an unsuitable universal cost proxy. Gap removal alone does not establish a classical separation: classical regularization, observable residual certification and energy-domain solvers can also avoid the original gap. Comparisons favourable to a particular dense, sparse-direct, Krylov or trajectory method remain comparisons to that method. A universal classical lower bound, guaranteed practical crossover and generic diffusion-law proof are not supplied.
