# Editorial and Mathematical QA Review: Statistical Simulation and Monte Carlo Methods (Stat H-307)

## Academic Rigor and Consistency Review
- All eight units reviewed for mathematical statistics, probability theory, computational simulation rigor, and curriculum alignment with Dhaka University B.S. Honours Statistics curriculum (Stat H-307: Statistical Simulation & Monte Carlo Methods).
- Unit 1: Foundations of pseudorandom number generation, Hull-Dobell theorem for LCG maximal period, Marsaglia's lattice hyperplane theorem, PCG and counter-based PRNGs (Philox, Threefry), TestU01 BigCrush testing suite, and CSPRNGs (ChaCha20, Blum-Blum-Shub).
- Unit 2: Non-uniform random variate generation, continuous CDF inversion proofs, discrete Alias Method (Walker-Vose $O(1)$ sampling), Box-Muller and Marsaglia-Bray transforms, Marsaglia-Tsang Ziggurat algorithm, Ratio-of-Uniforms method, and fast circulant embedding for Gaussian process paths.
- Unit 3: Resampling methods, Quenouille-Tukey Jackknife, Efron's non-parametric empirical bootstrap, higher-order asymptotic accuracy via Edgeworth expansions, studentized bootstrap-t, bias-corrected and accelerated ($BC_a$) bootstrap, Moving Block Bootstrap (MBB) and Politis-Romano Stationary Bootstrap, $m$-out-of-$n$ subsampling, and Wild Bootstrap for heteroskedastic regression.
- Unit 4: Classical Monte Carlo integration, Strong Law of Large Numbers, asymptotic CLT standard errors, dimension-independent convergence $O(n^{-1/2})$, Quasi-Monte Carlo (QMC) with Halton and Sobol' sequences, Koksma-Hlawka inequality, ANOVA effective dimensions, Randomized QMC (RQMC), and Multilevel Monte Carlo (MLMC) for SDEs.
- Unit 5: Variance reduction techniques, Antithetic Variates method under monotonic transformations, Control Variates with known expectations ($1 - R^2$ reduction), Stratified Sampling with Neyman optimal allocation, Latin Hypercube Sampling (LHS) and Stein's theorem, Adaptive Importance Sampling, Cross-Entropy rare-event simulation, and regularized multi-response control variates.
- Unit 6: Markov Chain Monte Carlo foundations, Harris recurrence, irreducibility, aperiodicity, detailed balance, Metropolis-Hastings algorithms, Random Walk Metropolis and Roberts-Gelman-Gilks optimal scaling theorem ($0.234$ rule), geometric ergodicity, Foster-Lyapunov drift conditions, rank-normalized split-$\hat{R}$, and parallel tempering for multimodal targets.
- Unit 7: Gibbs sampling as exact Metropolis-Hastings, Albert-Chib latent Gaussian data augmentation for probit models, Hamiltonian Monte Carlo (HMC) with symplectic leapfrog integrator, No-U-Turn Sampler (NUTS) with dual averaging step size adaptation, Radford Neal's Slice Sampling, Stochastic Gradient Langevin Dynamics (SGLD), and Propp-Wilson Coupling from the Past (CFTP).
- Unit 8: Sequential Monte Carlo (SMC), state-space filtering recursions, Sequential Importance Resampling (SIR) particle filter, effective sample size $N_{\text{eff}}$, Pitt-Shephard Auxiliary Particle Filter (APF), Approximate Bayesian Computation (ABC) and ABC-SMC, Particle MCMC (PMMH) and the Pseudo-Marginal theorem, and the Ensemble Kalman Filter (EnKF) for planetary-scale data assimilation.

## Verification of KaTeX Mathematical Notation
- All KaTeX mathematical expressions verified with 0 syntax errors.
- Verified absence of unescaped dollar signs and conflicting delimiters.

## Computational Simulation Verification
- Four interactive simulations verified: `sim-prng-lcg`, `sim-rejection-sampling`, `sim-importance-sampling`, `sim-mcmc-metropolis`.
- Standardized UI controls: accessible labels, aria-live polite numeric summaries, reset handlers, SVG visualizers, zero NaN or undefined values.
