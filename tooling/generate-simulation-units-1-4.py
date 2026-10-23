#!/usr/bin/env python3
"""
Generate Units 1 to 4 for Statistical Simulation and Monte Carlo Methods.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1 = r"""# Unit 1: Uniform Random Number Generation & Pseudorandom Foundations

In computational statistics, quantitative empirical modeling, and stochastic analysis, the ability to generate a sequence of numbers that appear completely random is the foundational prerequisite for all numerical simulation algorithms. Modern scientific algorithms—from Markov chain Monte Carlo in high-dimensional Bayesian inference to parametric bootstrap confidence intervals—rely upon uniform pseudorandom number generators.

However, a digital computer is an inherently deterministic finite-state Turing machine. Executing a deterministic algorithmic instruction on a given set of initial bits will always yield an identical, predictable output. True physical randomness, derived from thermal noise, quantum radioactive decay, or photon shot noise, is computationally slow to harvest, non-reproducible for auditing purposes, and difficult to interface with high-throughput scientific pipelines.

Consequently, scientific computing relies upon **Pseudorandom Number Generators (PRNGs)**: mathematical recursion algorithms that generate sequences of numbers that exhibit statistical properties indistinguishable from independent and identically distributed (i.i.d.) draws from the continuous standard uniform distribution $\mathcal{U}(0, 1)$, while remaining completely reproducible when initialized with the same integer **seed**.

## 1.1 Formal Properties and Criteria for High-Quality PRNGs

A mathematically rigorous pseudorandom number generator can be formalized as a 5-tuple $(\mathcal{S}, s_0, f, \mathcal{U}, g)$:
1. $\mathcal{S}$: A finite set of internal algorithmic states.
2. $s_0 \in \mathcal{S}$: The initial state, commonly designated as the **seed**.
3. $f: \mathcal{S} \to \mathcal{S}$: The deterministic state transition function:
   $$s_{n+1} = f(s_n)$$
4. $\mathcal{U}$: The output alphabet or observation space, typically the discrete set of normalized rationals in $[0, 1)$.
5. $g: \mathcal{S} \to \mathcal{U}$: The output mapping function that maps the internal state to a floating-point uniform variate:
   $$u_n = g(s_n) \in (0, 1)$$

Because the state space $\mathcal{S}$ is strictly finite on digital architectures, there must exist two discrete indices $j < k$ such that $s_j = s_k$. Since the transition function $f$ is deterministic, the sequence must enter an infinite periodic cycle:
$$s_{n + k - j} = s_n \quad \text{for all } n \ge j$$
The length of this repeating sequence is termed the **period length** $\rho \le |\mathcal{S}|$.

For a generator to be deemed scientifically acceptable for modern statistical simulation, it must satisfy four fundamental criteria:
- **Maximal Period Length**: The period $\rho$ must vastly exceed the number of random numbers consumed by any prospective simulation run. If an intensive Monte Carlo experiment consumes $10^{12}$ draws, a period length of at least $2^{64}$ (or ideally $2^{19937}-1$) is required to avoid cycling.
- **Equidistribution in High Dimensions**: If consecutive $k$-tuples of generated numbers $(u_n, u_{n+1}, \dots, u_{n+k-1})$ are plotted in the unit hypercube $[0, 1)^k$, they must fill the hypercube uniformly without clustering, voids, or dimensional defect.
- **Statistical Independence and Absence of Serial Autocorrelation**: Lag-$k$ autocovariances $\mathbb{E}[u_n u_{n+k}] - \frac{1}{4}$ must be statistically indistinguishable from zero across all measurable lags.
- **Algorithmic Efficiency and Reproducibility**: The state transition $f(s)$ must execute in minimal clock cycles, utilizing bitwise shifts, additions, or hardware integer registers.

## 1.2 Linear Congruential Generators: Mechanics and the Hull-Dobell Theorem

The earliest and most extensively studied family of pseudorandom number generators is the **Linear Congruential Generator (LCG)**, introduced by Derrick Henry Lehmer in 1949.

An LCG is parametrized by four positive integers:
1. $m > 0$: The **modulus**.
2. $a \in (0, m)$: The **multiplier**.
3. $c \in [0, m)$: The **increment**.
4. $X_0 \in [0, m)$: The initial **seed**.

The integer state sequence evolves according to the first-order linear recurrence modulo $m$:

$$X_{n+1} = (a X_n + c) \pmod m$$

The uniform floating-point variates are obtained by normalizing the integer state:

$$u_{n+1} = \frac{X_{n+1}}{m} \in [0, 1)$$

When the increment is strictly zero ($c = 0$), the generator is termed a **Multiplicative Congruential Generator (MCG)** or Lehmer generator:
$$X_{n+1} = a X_n \pmod m$$

### The Hull-Dobell Theorem
Because the modulus is $m$, the period $\rho$ cannot exceed $m$. An LCG achieves the **full period** of $\rho = m$ if and only if the parameters satisfy the conditions established by T. E. Hull and A. R. Dobell in 1962:

*Theorem (Hull-Dobell, 1962)*: The linear congruential sequence $X_{n+1} = (a X_n + c) \pmod m$ has full period $m$ for any initial seed $X_0$ if and only if:
1. $c$ and $m$ are relatively prime: $\gcd(c, m) = 1$.
2. For every prime factor $p$ dividing $m$, $(a - 1)$ is divisible by $p$:
   $$p \mid m \implies a \equiv 1 \pmod p$$
3. If $m$ is divisible by 4, then $(a - 1)$ must also be divisible by 4:
   $$4 \mid m \implies a \equiv 1 \pmod 4$$

*Proof Intuition*:
By repeated expansion of the recurrence relation:
$$X_n = a^n X_0 + c \sum_{j=0}^{n-1} a^j = a^n X_0 + c \left( \frac{a^n - 1}{a - 1} \right) \pmod m$$
For the sequence to visit all $m$ states before repeating, the cycle length of the additive component must divide $m$, while the powers $a^n$ must avoid collapsing into sub-orbits of smaller order. The divisibility conditions on $(a - 1)$ prevent premature convergence in prime modular rings.

For Multiplicative Congruential Generators ($c = 0$), the state $X = 0$ is absorbing ($a \cdot 0 \equiv 0$). Hence, the maximum possible period is $m - 1$. When $m$ is chosen as a prime number (e.g., the Mersenne prime $m = 2^{31} - 1 = 2,147,483,647$), a full period of $m - 1$ is attained if and only if the multiplier $a$ is a **primitive root modulo $m$** (meaning the smallest positive integer $k$ such that $a^k \equiv 1 \pmod m$ is $k = m - 1$). The classical `MINSTD` generator of Park and Miller (1988) selected $a = 7^5 = 16,807$ and $m = 2^{31} - 1$.

## 1.3 Marsaglia's Theorem: The Lattice Structure of LCGs

In 1968, George Marsaglia published a seminal paper in the *Proceedings of the National Academy of Sciences* entitled **"Random Numbers Fall Mainly in the Planes"**. Marsaglia proved that despite passing one-dimensional goodness-of-fit tests, consecutive vectors of numbers produced by any linear congruential generator exhibit a severe, intrinsic crystalline lattice defect.

### Mathematical Formulation of Marsaglia's Theorem
Consider formed vectors of $k$ consecutive normalized variates in $k$-dimensional Euclidean space:
$$\mathbf{P}_n = (u_n, u_{n+1}, \dots, u_{n+k-1}) \in [0, 1)^k$$

*Theorem (Marsaglia, 1968)*: For any linear congruential generator with modulus $m$, all $k$-tuples $\mathbf{P}_n$ lie on a finite family of parallel $(k-1)$-dimensional hyperplanes. The maximum number of parallel hyperplanes $H_k$ covering all points in $[0, 1)^k$ satisfies:

$$H_k \le (k! \cdot m)^{1/k}$$

For a 32-bit generator where $m = 2^{31} \approx 2.15 \times 10^9$:
- In $k = 2$ dimensions: $H_2 \le \sqrt{2 \times 2^{31}} \approx 65,536$ lines.
- In $k = 3$ dimensions: $H_3 \le (6 \times 2^{31})^{1/3} \approx 2,344$ planes.
- In $k = 10$ dimensions: $H_{10} \le (10! \times 2^{31})^{1/10} \approx 39$ hyperplanes!

In 10-dimensional space, the generated vectors lie on at most 39 parallel planes, leaving vast empty swaths of the 10-dimensional hypercube completely unvisited! Any multi-variable statistical simulation (e.g., simulating a 10-asset financial portfolio or 10-step particle transport) using an LCG is severely corrupted by this geometric regularity.

### The Infamous RANDU Disaster
During the 1960s, IBM distributed the `RANDU` pseudorandom generator with System/360 mainframes. RANDU was an MCG defined by:
$$m = 2^{31}, \quad a = 65539 = 2^{16} + 3, \quad c = 0$$

Expanding three consecutive states:
$$X_{n+2} = a X_{n+1} \pmod{2^{31}} = (2^{16} + 3) X_{n+1} \pmod{2^{31}}$$
Notice that:
$$a^2 = (2^{16} + 3)^2 = 2^{32} + 6 \cdot 2^{16} + 9 \equiv 6(2^{16} + 3) - 9 \pmod{2^{31}} = 6a - 9 \pmod{2^{31}}$$
Multiplying by $X_n$:
$$X_{n+2} - 6 X_{n+1} + 9 X_n \equiv 0 \pmod{2^{31}}$$

In 3-dimensional space, every point $(u_n, u_{n+1}, u_{n+2})$ produced by RANDU lies on only **15 parallel two-dimensional planes**! Thousands of scientific papers published in the late 1960s and 1970s suffered severe numerical artifacts as a direct consequence of RANDU's structural defect.

## 1.4 Modern High-Performance Generators: Mersenne Twister, Xorshift, and PCG

To escape the geometric flaws and short periods of linear congruential generators, modern computational statistics deploys advanced algorithmic families based on linear feedback shift registers, linear permutations, and cellular automata.

### 1. The Mersenne Twister (MT19937)
Developed by Makoto Matsumoto and Takuji Nishimura in 1997, the **Mersenne Twister** is a generalized twisted feedback shift register (GFSR) algorithm.
- **Period Length**: The period is a Mersenne prime:
  $$\rho = 2^{19937} - 1 \approx 4.3 \times 10^{6001}$$
  This period is astronomically large, far exceeding the total number of subatomic particles in the observable universe ($\approx 10^{80}$).
- **High-Dimensional Equidistribution**: MT19937 is proven to be uniformly distributed in up to 623 dimensions for 32-bit accuracy.
- **Tempering Transform**: After advancing the 624-word state vector via matrix linear recurrence over $\mathbb{F}_2$, MT19937 applies a four-stage bitwise tempering transformation (shifts and bitwise ANDs) to eliminate high-order correlation.
MT19937 is the default pseudorandom engine in R, Python (`random` module), MATLAB, and GNU Scientific Library (GSL).

### 2. Xorshift and Xoshiro Generators
Formulated by George Marsaglia (2003) and refined by Sebastiano Vigna and David Blackman (2018), the **Xoshiro256** family uses linear state updates composed strictly of bitwise XOR, SHIFT, and ROTATE operations:
$$\mathbf{s}_{n+1} = \mathbf{s}_n \oplus (\mathbf{s}_n \ll a) \oplus (\mathbf{s}_n \gg b)$$
With periods of $2^{256} - 1$, these generators execute in less than 2 nanoseconds per variate on modern superscalar CPUs, outperforming MT19937 in speed and memory footprint while passing the most stringent empirical test batteries.

### 3. Permuted Congruential Generators (PCG)
Developed by Melissa O'Neill in 2014, the **PCG** family combines the mathematical elegance of an LCG state update with a non-linear permutation function applied to the output:
- State update: $X_{n+1} = a X_n + c \pmod{2^{64}}$ (linear and simple).
- Output function: $u_{n+1} = \text{Rotate}(\text{XOR-Fold}(X_{n+1}))$ (non-linear permutation).
The permutation function destroys the linear lattice structure of the LCG, rendering the output cryptographically robust against hyperplane degradation while preserving compact memory and state-skipping capabilities.

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Generator Class</th>
<th>Algorithm Representative</th>
<th>State Space / Period</th>
<th>Lattice Defect</th>
<th>CPU Efficiency</th>
<th>Primary Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td>Linear Congruential</td>
<td>`MINSTD` / ANSI C</td>
<td>$2^{31} - 1 \approx 2.1 \times 10^9$</td>
<td>Severe (Marsaglia hyperplanes)</td>
<td>Ultra-fast (1 multiply, 1 add)</td>
<td>Legacy embedded hardware</td>
</tr>
<tr>
<td>Twisted Feedback</td>
<td>Mersenne Twister MT19937</td>
<td>$2^{19937} - 1 \approx 10^{6001}$</td>
<td>None up to 623 dimensions</td>
<td>Moderate (624-word buffer)</td>
<td>General scientific modeling</td>
</tr>
<tr>
<td>Shift-Register / XOR</td>
<td>Xoshiro256++</td>
<td>$2^{256} - 1 \approx 1.1 \times 10^{77}$</td>
<td>None in high dimensions</td>
<td>Extremely fast (bitwise ops)</td>
<td>High-throughput simulations</td>
</tr>
<tr>
<td>Permuted Congruential</td>
<td>PCG-XSH-RR</td>
<td>$2^{128} \approx 3.4 \times 10^{38}$</td>
<td>Inaccessible (scrambled)</td>
<td>Fast (registers only)</td>
<td>Modern statistical computing</td>
</tr>
</tbody>
</table>
</div>

## 1.5 Statistical Randomness Testing: Empirical Batteries and the NIST Test Suite

A generator cannot be deemed statistically valid based on theoretical period length alone. It must be subjected to rigorous empirical testing batteries that evaluate whether generated bit streams display statistical characteristics indistinguishable from true Bernoulli coin tosses ($p = 0.5$).

### 1. Classical Empirical Tests
1. **The Monobit Frequency Test**: Tests whether the proportion of 1s in a bit sequence of length $N$ equals 0.5.
   Under the null hypothesis $H_0$, let $S_N = \sum_{i=1}^N (2X_i - 1)$. The test statistic is:
   $$Z = \frac{S_N}{\sqrt{N}} \xrightarrow{d} \mathcal{N}(0, 1)$$
2. **The Runs Test**: Evaluates whether the number of runs (uninterrupted sequences of identical bits) matches theoretical expectations. An excess of runs signals rapid oscillation, while too few runs indicate clustering.
3. **The Serial Independence Test**: Tests for non-zero lag-$k$ autocorrelation by evaluating the bivariate distribution of overlapping $k$-bit pairs.
4. **The Spectral Fourier Test**: Applies the Discrete Fourier Transform to detect hidden periodicities and periodic harmonic spikes in the generator bit stream.

### 2. Comprehensive Test Suites: NIST SP 800-22 and Dieharder
In modern statistical research, individual tests are replaced by comprehensive software batteries:
- **NIST SP 800-22**: Formulated by the United States National Institute of Standards and Technology, comprising 15 statistical tests including cumulative sums, block frequency, longest run of ones, rank of binary matrices, non-overlapping template matching, and linear complexity via the Berlekamp-Massey algorithm.
- **The Dieharder Suite**: Developed by Robert Brown, expanding Marsaglia's original *Diehard* battery to include the birthday spacings test, monkey tests, parking lot test, minimum distance test, and squeeze test.
A generator is approved for scientific use only if the p-values across all tests in the battery are uniformly distributed on $[0, 1)$ across repeated simulation replicates.

## Fully worked question 1: LCG Period Length and Full Period Validation

### Question
An applied statistician implements a custom Linear Congruential Generator for a parallel Monte Carlo simulation. The proposed generator has modulus $m = 2^{16} = 65,536$, multiplier $a = 1,365$, and increment $c = 1,367$.
1. Using the Hull-Dobell Theorem, prove rigorously whether this generator achieves the full period of $\rho = 65,536$.
2. If the increment were changed to $c = 1,368$, determine the impact on the period length.
3. Calculate the upper bound on the maximum number of parallel hyperplanes in $k = 3$ dimensions for this generator under Marsaglia's Theorem.

### Solution, step 1: Verification of the Hull-Dobell Conditions for $c = 1,367$
To achieve full period $\rho = m = 65,536$, the parameters must satisfy all three Hull-Dobell conditions:
- **Condition 1**: $\gcd(c, m) = 1$.
  The modulus is $m = 2^{16}$. Its only prime factor is $p = 2$.
  The increment is $c = 1,367$. Since $1,367$ is an odd number ($1367 \equiv 1 \pmod 2$), it shares no factors with $2^{16}$.
  $$\gcd(1367, 65536) = 1$$
  Condition 1 is strictly satisfied.
- **Condition 2**: Every prime factor $p$ dividing $m$ must divide $(a - 1)$.
  The sole prime factor of $m$ is $p = 2$.
  We evaluate $a - 1$:
  $$a - 1 = 1365 - 1 = 1364$$
  Since $1364 = 2 \times 682$, $1364$ is divisible by 2 ($1364 \equiv 0 \pmod 2$).
  Condition 2 is strictly satisfied.
- **Condition 3**: If $4 \mid m$, then $4 \mid (a - 1)$.
  Since $m = 65536 = 4 \times 16384$, $4$ divides $m$.
  We test divisibility of $a - 1$ by 4:
  $$\frac{a - 1}{4} = \frac{1364}{4} = 341$$
  Because $341$ is an integer without remainder, $4 \mid (a - 1)$.
  Condition 3 is strictly satisfied.

*Conclusion*: All three Hull-Dobell conditions are satisfied. The generator achieves the full period of $\rho = 65,536$.

### Solution, step 2: Impact of Altering the Increment to $c = 1,368$
If the increment is changed to $c = 1,368$:
- The modulus is $m = 65,536 = 2^{16}$.
- The increment $c = 1,368$ is an even integer:
  $$1368 = 2^3 \times 171$$
- Evaluating the greatest common divisor:
  $$\gcd(c, m) = \gcd(1368, 65536) = 8 \ne 1$$
Condition 1 of the Hull-Dobell theorem is violated. The sequence cannot visit any odd state if initialized at an even state, and the maximum period collapses to at most $m / 8 = 8,192$. The generator fails to achieve full period.

### Solution, step 3: Calculation of Marsaglia's Hyperplane Bound in Dimension $k = 3$
Under Marsaglia's theorem, all consecutive 3-tuples $(u_n, u_{n+1}, u_{n+2})$ lie on a family of parallel hyperplanes whose count $H_3$ cannot exceed:
$$H_3 \le (3! \cdot m)^{1/3}$$
Substituting $m = 65,536$ and $3! = 6$:
$$3! \cdot m = 6 \times 65,536 = 393,216$$
Taking the cube root:
$$H_3 \le (393,216)^{1/3} \approx 73.26$$
Rounding down to the nearest integer, all generated points in the 3-dimensional unit cube are confined to at most **73 parallel planes**. This represents severe dimensional lattice clustering, rendering the generator unsuitable for 3D spatial simulation.

## Fully worked question 2: Frequency and Runs Testing on a Generated Bitstream

### Question
A pseudorandom generator produces a candidate binary bit stream of length $N = 100$ bits:
- Number of ones: $n_1 = 58$.
- Number of zeros: $n_0 = 42$.
- Total observed number of runs: $R = 41$.

1. Conduct the NIST Monobit Frequency Test at significance level $\alpha = 0.05$ to evaluate whether the proportion of ones is consistent with true randomness.
2. Conduct the Wald-Wolfowitz Runs Test at $\alpha = 0.05$ to assess serial independence.
3. Formulate the joint conclusion regarding the null hypothesis of randomness.

### Solution, step 1: Execution of the Monobit Frequency Test
Under the null hypothesis $H_0$, each bit is an independent Bernoulli trial with $P(X_i = 1) = 0.5$.
Map each bit to $Y_i \in \{-1, +1\}$ via $Y_i = 2X_i - 1$:
- Total sum of $Y_i$:
  $$S_N = \sum_{i=1}^N Y_i = n_1 - n_0 = 58 - 42 = +16$$
The test statistic is:
$$Z_{\text{freq}} = \frac{S_N}{\sqrt{N}} = \frac{16}{\sqrt{100}} = \frac{16}{10} = 1.60$$
The two-tailed p-value under the standard Gaussian distribution is:
$$p = 2 \left( 1 - \Phi(|Z_{\text{freq}}|) \right) = 2 \left( 1 - \Phi(1.60) \right) = 2 (1 - 0.9452) = 2 \times 0.0548 = 0.1096$$
Since $p = 0.1096 > 0.05$, we fail to reject $H_0$. The frequency of ones is statistically consistent with standard uniform expectation.

### Solution, step 2: Execution of the Wald-Wolfowitz Runs Test
A run is defined as a contiguous sequence of identical bits. Under $H_0$, conditional on $n_1 = 58$ and $n_0 = 42$, the theoretical expectation of the number of runs $R$ is:
$$\mathbb{E}[R] = \frac{2 n_1 n_0}{N} + 1 = \frac{2 \times 58 \times 42}{100} + 1 = \frac{4872}{100} + 1 = 48.72 + 1 = 49.72$$
The theoretical variance of $R$ is:
$$\mathrm{Var}(R) = \frac{2 n_1 n_0 (2 n_1 n_0 - N)}{N^2 (N - 1)} = \frac{4872 \times (4872 - 100)}{10000 \times 99} = \frac{4872 \times 4772}{990,000} = \frac{23,249,184}{990,000} \approx 23.484$$
The standard error is:
$$\sigma_R = \sqrt{23.484} \approx 4.846$$
The standardized test statistic using continuity correction (since $R = 41 < \mathbb{E}[R]$):
$$Z_{\text{runs}} = \frac{R + 0.5 - \mathbb{E}[R]}{\sigma_R} = \frac{41 + 0.5 - 49.72}{4.846} = \frac{-8.22}{4.846} \approx -1.696$$
The two-tailed p-value is:
$$p = 2 \left( 1 - \Phi(1.696) \right) \approx 2 (1 - 0.9551) = 2 \times 0.0449 = 0.0898$$
At the $\alpha = 0.05$ significance level, $p = 0.0898 > 0.05$. We fail to reject $H_0$ at the $5\%$ level, although the observed runs count is moderately low.

### Solution, step 3: Joint Statistical Synthesis
Both the frequency test ($p = 0.1096$) and the runs test ($p = 0.0898$) yield p-values exceeding the $5\%$ significance threshold. Therefore, the bitstream passes both preliminary randomness screening tests at $\alpha = 0.05$. However, because the runs p-value is close to the margin, larger test streams ($N = 10^6$ bits) and the NIST SP 800-22 battery must be evaluated before certifying the PRNG for high-stakes cryptographic or scientific simulation.

## Fully worked question 3: Multiplicative Congruential Generator Orbit and Primitive Roots

### Question
Consider a small-scale Multiplicative Congruential Generator:
$$X_{n+1} = a X_n \pmod m$$
with prime modulus $m = 31$.
1. Determine whether $a = 3$ is a primitive root modulo 31 and compute its exact period length.
2. Determine whether $a = 7$ is a primitive root modulo 31.
3. Compare the efficiency and period length of the two candidate multipliers.

### Solution, step 1: Evaluation of $a = 3$ Modulo 31
A multiplier $a$ is a primitive root modulo prime $m = 31$ if the multiplicative order of $a$ modulo 31 is $\phi(31) = 30$.
By Lagrange's theorem, the order of any element must divide 30. The divisors of 30 are $\{1, 2, 3, 5, 6, 10, 15, 30\}$.
To verify if $a = 3$ has order 30, it suffices to show that $3^k \not\equiv 1 \pmod{31}$ for all maximal proper divisors of 30: $k \in \{6, 10, 15\}$.

We compute successive modular powers of $a = 3$:
- $3^1 \equiv 3 \pmod{31}$
- $3^2 = 9 \pmod{31}$
- $3^3 = 27 \equiv -4 \pmod{31}$
- $3^5 = 3^3 \times 3^2 \equiv (-4) \times 9 = -36 \equiv -5 \pmod{31}$
- $3^6 = 3^5 \times 3 \equiv (-5) \times 3 = -15 \equiv 16 \pmod{31} \ne 1$
- $3^{10} = (3^5)^2 \equiv (-5)^2 = 25 \equiv -6 \pmod{31} \ne 1$
- $3^{15} = 3^{10} \times 3^5 \equiv (-6) \times (-5) = 30 \equiv -1 \pmod{31} \ne 1$

Since $3^6 \not\equiv 1$, $3^{10} \not\equiv 1$, and $3^{15} \not\equiv 1 \pmod{31}$, the order of 3 cannot be any proper divisor of 30.
Therefore, the multiplicative order of $a = 3$ is exactly 30:
$$\rho = 30$$
The multiplier $a = 3$ is a primitive root modulo 31 and achieves the maximal possible period of $\rho = m - 1 = 30$.

### Solution, step 2: Evaluation of $a = 7$ Modulo 31
We test $a = 7$ modulo 31:
- $7^1 \equiv 7 \pmod{31}$
- $7^2 = 49 \equiv 18 \equiv -13 \pmod{31}$
- $7^3 = 7 \times 18 = 126 = 4 \times 31 + 2 \equiv 2 \pmod{31}$
- $7^5 = 7^3 \times 7^2 \equiv 2 \times (-13) = -26 \equiv 5 \pmod{31}$
- $7^6 = (7^3)^2 \equiv 2^2 = 4 \pmod{31} \ne 1$
- $7^{15} = (7^5)^3 \equiv 5^3 = 125 = 4 \times 31 + 1 \equiv 1 \pmod{31}$

Notice that $7^{15} \equiv 1 \pmod{31}$!
Because $7^{15} \equiv 1$, the order of 7 divides 15. Testing the divisors of 15 ($\{1, 3, 5\}$):
- $7^1 \equiv 7 \ne 1$
- $7^3 \equiv 2 \ne 1$
- $7^5 \equiv 5 \ne 1$
Thus, the exact order of $a = 7$ modulo 31 is:
$$\text{ord}_{31}(7) = 15$$
Since its order is $15 < 30$, $a = 7$ is **not a primitive root modulo 31**. The sequence cycles after only 15 iterations.

### Solution, step 3: Comparative Conclusion
The multiplier $a = 3$ generates the maximal period of 30 states, visiting every integer in $\{1, 2, \dots, 30\}$ exactly once before repeating. In contrast, $a = 7$ generates an orbit of length 15, leaving half of the potential state space completely unvisited. In pseudorandom generator design, only verified primitive roots modulo prime moduli guarantee maximal orbit exploration.
"""

(DRAFT_DIR / "unit-1.md").write_text(u1.strip() + "\n", encoding="utf-8")
print("Unit 1 generated.")
# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2 = r"""# Unit 2: Non-Uniform Random Variate Generation: Inversion & Transformations

Once a dependable source of independent standard uniform random variables $U \sim \mathcal{U}(0, 1)$ is established, the central computational challenge shifts to transforming these uniform variates into random draws from arbitrary continuous and discrete probability distributions. Whether simulating loss severities in non-life insurance (Pareto or log-normal), customer inter-arrival times in queueing theory (exponential or gamma), or asset return shocks in quantitative portfolio risk management (multivariate normal or Student's $t$), non-uniform random variate generation constitutes the computational engine of statistical simulation.

Two primary direct generation paradigms exist: the **Inverse Transform Method** (applicable whenever the cumulative distribution function possesses a tractable inverse) and **Transformation Methods** (which exploit algebraic, geometric, or stochastic relationships connecting standard distributions).

## 2.1 The Probability Integral Transform and Inverse Transform Method

The foundational theorem underpinning non-uniform variate generation is the **Probability Integral Transform**.

### 1. Continuous Probability Integral Transform Theorem
*Theorem (Inverse CDF Transform)*: Let $X$ be a continuous random variable with cumulative distribution function (CDF) $F(x) = P(X \le x)$ that is strictly increasing and continuous on its support. If $U \sim \mathcal{U}(0, 1)$, then the transformed random variable:

$$X = F^{-1}(U)$$

has cumulative distribution function exactly equal to $F(x)$.

*Mathematical Proof*:
Since $F$ is strictly increasing, the inverse function $F^{-1}: (0, 1) \to \mathbb{R}$ is uniquely defined and strictly monotonic.
For any real $x$:
$$P(X \le x) = P(F^{-1}(U) \le x)$$
Applying the strictly increasing function $F$ to both sides of the inequality inside the probability:
$$P(F^{-1}(U) \le x) = P(F(F^{-1}(U)) \le F(x)) = P(U \le F(x))$$
Because $U \sim \mathcal{U}(0, 1)$, its cumulative distribution function is $P(U \le u) = u$ for all $u \in [0, 1]$. Therefore:
$$P(U \le F(x)) = F(x)$$
This establishes that $P(X \le x) \equiv F(x)$, proving the theorem.

Conversely, if $X$ is any continuous random variable with CDF $F(x)$, the transformed variable $Y = F(X)$ follows a standard uniform distribution: $Y \sim \mathcal{U}(0, 1)$.

### 2. Generalized Inverse for Discrete and Non-Monotonic CDFs
When the CDF $F(x)$ has flat regions (zero probability density) or discrete step jumps (discrete random variables), the standard inverse does not exist. Actuaries and mathematical statisticians define the **Generalized Inverse (Quantile Function)**:

$$F^{-}(u) = \inf \{x \in \mathbb{R} : F(x) \ge u\} \quad \text{for } u \in (0, 1)$$

*Theorem (Generalized Inverse Transform)*: For any cumulative distribution function $F(x)$ (continuous, discrete, or mixed), if $U \sim \mathcal{U}(0, 1)$, then $X = F^{-}(U)$ has distribution function $F(x)$.

*Proof*: By definition of the infimum, the event $F^{-}(u) \le x$ occurs if and only if $u \le F(x)$. Hence:
$$P(F^{-}(U) \le x) = P(U \le F(x)) = F(x)$$
This universal property ensures that any arbitrary one-dimensional random variable can be sampled via uniform quantile inversion.

## 2.2 Analytical Inversion for Common Continuous Distributions

Whenever $F(x)$ can be inverted in closed algebraic form, the inverse transform method is optimal in terms of exactness and monotonic synchronization:

### 1. The Exponential Distribution ($\text{Exp}(\lambda)$)
Let $X \sim \text{Exp}(\lambda)$ with rate parameter $\lambda > 0$. The CDF is:
$$F(x) = 1 - e^{-\lambda x} \quad \text{for } x \ge 0$$
Setting $U = F(X)$:
$$U = 1 - e^{-\lambda X} \implies 1 - U = e^{-\lambda X} \implies -\lambda X = \ln(1 - U) \implies X = -\frac{\ln(1 - U)}{\lambda}$$
Because $U \sim \mathcal{U}(0, 1)$, the complementary variable $1 - U$ also follows $\mathcal{U}(0, 1)$ identically. Thus, in computational implementations, the inversion formula is universally simplified to:
$$X = -\frac{\ln(U)}{\lambda}$$
saving one floating-point subtraction per generated variate.

### 2. The Weibull Distribution ($\text{Weibull}(\alpha, \beta)$)
The Weibull CDF with shape $\alpha > 0$ and scale $\beta > 0$ is:
$$F(x) = 1 - \exp\left( -\left(\frac{x}{\beta}\right)^\alpha \right) \quad \text{for } x \ge 0$$
Inverting $U = F(X)$:
$$X = \beta \left( -\ln(1 - U) \right)^{1/\alpha} = \beta (-\ln U)^{1/\alpha}$$

### 3. The Pareto Distribution ($\text{Pareto}(\alpha, x_m)$)
Widely used in extreme value theory and insurance catastrophe modeling:
$$F(x) = 1 - \left( \frac{x_m}{x} \right)^\alpha \quad \text{for } x \ge x_m > 0, \; \alpha > 0$$
Inverting $U = F(X)$:
$$1 - U = \left( \frac{x_m}{X} \right)^\alpha \implies X = \frac{x_m}{(1 - U)^{1/\alpha}} = x_m U^{-1/\alpha}$$

### 4. The Cauchy Distribution ($\text{Cauchy}(x_0, \gamma)$)
The standard Cauchy density $f(x) = \frac{1}{\pi (1 + x^2)}$ integrates to:
$$F(x) = \frac{1}{2} + \frac{1}{\pi} \arctan\left(\frac{x - x_0}{\gamma}\right)$$
Inverting yields:
$$X = x_0 + \gamma \tan\left( \pi \left( U - \frac{1}{2} \right) \right)$$

## 2.3 Discrete Variate Inversion and Walker's Alias Algorithm

For a discrete random variable taking values $\{x_1, x_2, \dots, x_k\}$ with probability mass function $P(X = x_j) = p_j$ (where $\sum_{j=1}^k p_j = 1$), the generalized inverse corresponds to sequential search through cumulative probability intervals:
$$F(x_j) = \sum_{i=1}^j p_i$$
To sample $X$:
1. Generate $U \sim \mathcal{U}(0, 1)$.
2. Return $x_j$ where $j$ is the unique index such that:
   $$F(x_{j-1}) < U \le F(x_j)$$

While binary search reduces lookup time to $\mathcal{O}(\log k)$, large-scale discrete sampling (such as word distributions in natural language processing with $k = 100,000$ categories) demands $\mathcal{O}(1)$ constant-time sampling. This is achieved by **Walker's Alias Algorithm** (Alastair Walker, 1977).

### The Alias Method Mechanics
The alias method represents any discrete probability distribution over $k$ outcomes as an equiprobable mixture of $k$ two-point distributions.
Each bucket $j \in \{1, 2, \dots, k\}$ contains:
- A primary outcome $j$ with probability weight $q_j \in [0, 1]$.
- An **alias outcome** $A_j \in \{1, \dots, k\}$ with complementary probability weight $1 - q_j$.

**Sampling Algorithm ($\mathcal{O}(1)$ time)**:
1. Generate $U \sim \mathcal{U}(0, 1)$.
2. Compute index $I = \lfloor k \cdot U \rfloor + 1 \in \{1, 2, \dots, k\}$.
3. Compute fractional remainder $V = k \cdot U - (I - 1) \in [0, 1)$.
4. If $V < q_I$, return outcome $I$; otherwise, return alias outcome $A_I$.
Walker's alias algorithm requires exactly two floating-point operations and one conditional comparison, completely independent of the alphabet size $k$.

## 2.4 The Box-Muller Transformation for Gaussian Variates

The standard normal distribution $\mathcal{N}(0, 1)$ with density $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ has a cumulative distribution function $\Phi(z) = \int_{-\infty}^z \phi(t)\,dt$ that cannot be expressed in terms of elementary functions, rendering direct algebraic inversion impossible without rational Chebyshev approximations.

In 1958, George Box and Mervin Muller devised an exact geometric transformation that converts a pair of independent standard uniform variates into a pair of independent standard Gaussian variates.

### Derivation via Bivariate Polar Coordinates
Consider two independent standard normal random variables $Z_1, Z_2 \sim \mathcal{N}(0, 1)$. Their joint probability density is:
$$f(z_1, z_2) = \frac{1}{2\pi} \exp\left( -\frac{z_1^2 + z_2^2}{2} \right)$$
Transform to polar coordinates $(R, \Theta)$ in $\mathbb{R}^2$:
$$z_1 = R \cos\Theta, \quad z_2 = R \sin\Theta$$
where $R = \sqrt{z_1^2 + z_2^2} \ge 0$ and $\Theta = \arctan(z_2 / z_1) \in [0, 2\pi)$.

The Jacobian determinant of the transformation is:
$$J = \begin{vmatrix} \frac{\partial z_1}{\partial R} & \frac{\partial z_1}{\partial \Theta} \\ \frac{\partial z_2}{\partial R} & \frac{\partial z_2}{\partial \Theta} \end{vmatrix} = \begin{vmatrix} \cos\Theta & -R\sin\Theta \\ \sin\Theta & R\cos\Theta \end{vmatrix} = R(\cos^2\Theta + \sin^2\Theta) = R$$

The joint density in polar coordinates is:
$$f_{R, \Theta}(r, \theta) = f(r\cos\theta, r\sin\theta) \cdot |J| = \frac{1}{2\pi} e^{-r^2/2} \cdot r = \left( \frac{1}{2\pi} \right) \cdot \left( r e^{-r^2/2} \right)$$
Because the joint density factors into a function of $\theta$ alone and a function of $r$ alone, $R$ and $\Theta$ are **mutually independent random variables**:
1. $\Theta$ is uniformly distributed on $[0, 2\pi)$:
   $$\Theta = 2\pi U_1, \quad U_1 \sim \mathcal{U}(0, 1)$$
2. The radius $R$ has cumulative distribution function:
   $$F_R(r) = \int_0^r s e^{-s^2/2}\,ds = \left[ -e^{-s^2/2} \right]_0^r = 1 - e^{-r^2/2}$$
   Let $U_2 = 1 - e^{-R^2/2} \sim \mathcal{U}(0, 1)$. Inverting:
   $$R^2 = -2\ln(1 - U_2) \implies R = \sqrt{-2\ln U_2}$$

Substituting back into Cartesian coordinates produces the **Box-Muller Equations**:

$$Z_1 = \sqrt{-2\ln U_1} \cos(2\pi U_2)$$
$$Z_2 = \sqrt{-2\ln U_1} \sin(2\pi U_2)$$
Both $Z_1$ and $Z_2$ are rigorously independent, standard normally distributed variates.

### The Marsaglia-Bray Polar Rejection Method
While mathematically elegant, the standard Box-Muller transform requires evaluating trigonometric functions ($\cos$ and $\sin$), which are computationally expensive on CPU hardware. George Marsaglia and Thomas Bray (1964) eliminated the trigonometric evaluations via acceptance-rejection in the unit disk:
1. Generate $V_1, V_2 \sim \mathcal{U}(-1, 1)$ by setting $V_i = 2U_i - 1$.
2. Compute squared radial distance $W = V_1^2 + V_2^2$.
3. If $W \ge 1$ or $W = 0$, reject and return to Step 1.
4. If $W < 1$ (the point lies inside the unit disk):
   $$\cos\Theta = \frac{V_1}{\sqrt{W}}, \quad \sin\Theta = \frac{V_2}{\sqrt{W}}$$
   Substituting into the Box-Muller formula yields:
   $$Z_1 = V_1 \sqrt{\frac{-2\ln W}{W}}, \quad Z_2 = V_2 \sqrt{\frac{-2\ln W}{W}}$$
The acceptance probability is the area of the unit disk divided by the bounding square: $P(\text{accept}) = \frac{\pi}{4} \approx 0.7854$. Because no trigonometric calls are executed, the polar method is significantly faster.

## 2.5 Multivariate Normal Simulation via Cholesky Decomposition

In multidimensional statistical modeling, financial econometrics, and spatial statistics, actuaries and researchers must generate correlated random vectors:
$$\mathbf{X} = (X_1, X_2, \dots, X_p)^T \sim \mathcal{N}_p(\mathbf{\mu}, \mathbf{\Sigma})$$
where $\mathbf{\mu} \in \mathbb{R}^p$ is the mean vector and $\mathbf{\Sigma} \in \mathbb{R}^{p \times p}$ is a symmetric, positive semi-definite covariance matrix.

### The Cholesky Factorization Algorithm
By the spectral theorem of linear algebra, any symmetric positive-definite matrix $\mathbf{\Sigma}$ can be uniquely decomposed into the product of a lower triangular matrix $\mathbf{L}$ with strictly positive diagonal entries and its transpose:

$$\mathbf{\Sigma} = \mathbf{L} \mathbf{L}^T$$

Let $\mathbf{Z} = (Z_1, \dots, Z_p)^T$ be a vector of $p$ independent standard normal variates ($Z_j \sim \mathcal{N}(0, 1)$), so that:
$$\mathbb{E}[\mathbf{Z}] = \mathbf{0}, \quad \mathrm{Cov}(\mathbf{Z}) = \mathbf{I}_p$$

Define the affine linear transformation:
$$\mathbf{X} = \mathbf{\mu} + \mathbf{L} \mathbf{Z}$$

We verify the mean and covariance of the transformed vector:
1. **Expectation**:
   $$\mathbb{E}[\mathbf{X}] = \mathbb{E}[\mathbf{\mu} + \mathbf{L} \mathbf{Z}] = \mathbf{\mu} + \mathbf{L} \mathbb{E}[\mathbf{Z}] = \mathbf{\mu}$$
2. **Covariance**:
   $$\mathrm{Cov}(\mathbf{X}) = \mathbb{E}[(\mathbf{X} - \mathbf{\mu})(\mathbf{X} - \mathbf{\mu})^T] = \mathbb{E}[(\mathbf{L}\mathbf{Z})(\mathbf{L}\mathbf{Z})^T] = \mathbf{L} \mathbb{E}[\mathbf{Z} \mathbf{Z}^T] \mathbf{L}^T = \mathbf{L} \mathbf{I}_p \mathbf{L}^T = \mathbf{L} \mathbf{L}^T = \mathbf{\Sigma}$$

Because any linear combination of Gaussian random variables is itself Gaussian, $\mathbf{X}$ is guaranteed to follow the exact multivariate normal distribution $\mathcal{N}_p(\mathbf{\mu}, \mathbf{\Sigma})$.

## Fully worked question 1: Inverse Transform Generation of Logistic and Pareto Variates

### Question
1. Derive the closed-form inverse transform generator for a Logistic distribution with location $\mu$ and scale $s > 0$, whose cumulative distribution function is:
   $$F(x) = \frac{1}{1 + e^{-(x - \mu)/s}} \quad \text{for } x \in \mathbb{R}$$
2. A catastrophic casualty insurance line models claim severities $X$ (in thousands of dollars) using a Pareto Type I distribution with minimum loss threshold $x_m = 50$ and tail index $\alpha = 2.5$.
   Given two pseudorandom uniform draws $u_1 = 0.150$ and $u_2 = 0.850$, compute the two corresponding simulated insurance claims.

### Solution, step 1: Derivation of the Logistic Inverse CDF Formula
Let $U \sim \mathcal{U}(0, 1)$. Set $U = F(X)$:
$$U = \frac{1}{1 + e^{-(X - \mu)/s}}$$
Take the reciprocal of both sides:
$$\frac{1}{U} = 1 + e^{-(X - \mu)/s} \implies e^{-(X - \mu)/s} = \frac{1}{U} - 1 = \frac{1 - U}{U}$$
Take the natural logarithm of both sides:
$$-\frac{X - \mu}{s} = \ln\left( \frac{1 - U}{U} \right) = \ln(1 - U) - \ln(U)$$
Multiply by $-s$:
$$X - \mu = s \left[ \ln(U) - \ln(1 - U) \right] = s \ln\left( \frac{U}{1 - U} \right)$$
Add $\mu$:
$$X = \mu + s \ln\left( \frac{U}{1 - U} \right) = \mu + s \cdot \text{logit}(U)$$
*Conclusion*: To generate a Logistic variate, compute $X = \mu + s \ln(U / (1 - U))$.

### Solution, step 2: Pareto Inverse Transform Equation
The Pareto cumulative distribution function is:
$$F(x) = 1 - \left( \frac{x_m}{x} \right)^\alpha \quad \text{for } x \ge x_m$$
Setting $U = F(X)$:
$$1 - U = \left( \frac{x_m}{X} \right)^\alpha \implies \left( \frac{X}{x_m} \right)^\alpha = \frac{1}{1 - U} \implies X = x_m (1 - U)^{-1/\alpha}$$
Alternatively, since $1 - U \stackrel{d}{=} U$, we can write:
$$X = x_m U^{-1/\alpha}$$

### Solution, step 3: Numerical Evaluation for $u_1$ and $u_2$
Given parameters $x_m = 50$ and $\alpha = 2.5$:
$$-1 / \alpha = -1 / 2.5 = -0.40$$

- **For $u_1 = 0.150$** (using $1 - U$ convention):
  $$X_1 = 50 \times (1 - 0.150)^{-0.40} = 50 \times (0.850)^{-0.40}$$
  Compute $(0.850)^{-0.40}$:
  $$\ln(0.850) \approx -0.1625189 \implies -0.40 \times (-0.1625189) = +0.0650076$$
  $$e^{0.0650076} \approx 1.067167$$
  $$X_1 = 50 \times 1.067167 \approx 53.358 \text{ (i.e., } \$53,358\text{)}$$

- **For $u_2 = 0.850$**:
  $$X_2 = 50 \times (1 - 0.850)^{-0.40} = 50 \times (0.150)^{-0.40}$$
  Compute $(0.150)^{-0.40}$:
  $$\ln(0.150) \approx -1.897120 \implies -0.40 \times (-1.897120) = +0.758848$$
  $$e^{0.758848} \approx 2.135817$$
  $$X_2 = 50 \times 2.135817 \approx 106.791 \text{ (i.e., } \$106,791\text{)}$$

Notice the heavy-tailed property: as $u \to 1$, simulated claims accelerate rapidly into catastrophic loss territory.

## Fully worked question 2: Step-by-Step Box-Muller Bivariate Normal Generation

### Question
A stochastic differential equation simulation for financial option pricing requires two independent standard Gaussian innovations $Z_1, Z_2 \sim \mathcal{N}(0, 1)$.
The pseudorandom generator supplies two uniform draws:
$$u_1 = 0.3250, \quad u_2 = 0.6500$$
1. Using the analytical Box-Muller transformation, calculate $Z_1$ and $Z_2$ explicitly to 4 decimal places.
2. If these innovations drive a bivariate stock portfolio with means $\mu_1 = 100, \mu_2 = 50$, standard deviations $\sigma_1 = 15, \sigma_2 = 8$, and correlation coefficient $\rho = 0.60$, compute the corresponding simulated asset price vector $\mathbf{X} = (X_1, X_2)^T$.

### Solution, step 1: Execution of the Box-Muller Transformation
The Box-Muller formulas are:
$$Z_1 = \sqrt{-2\ln(u_1)} \cos(2\pi u_2)$$
$$Z_2 = \sqrt{-2\ln(u_1)} \sin(2\pi u_2)$$

1. Compute the radial amplitude $R = \sqrt{-2\ln(u_1)}$:
   $$\ln(u_1) = \ln(0.3250) \approx -1.123930$$
   $$-2\ln(u_1) = -2 \times (-1.123930) = 2.247860$$
   $$R = \sqrt{2.247860} \approx 1.499287$$

2. Compute the angular argument $\Theta = 2\pi u_2$:
   $$\Theta = 2\pi \times 0.6500 = 1.3000 \pi \approx 4.084070 \text{ radians} \quad (234.0^\circ)$$

3. Compute trigonometric projections:
   $$\cos(1.30\pi) = \cos(234^\circ) \approx -0.587785$$
   $$\sin(1.30\pi) = \sin(234^\circ) \approx -0.809017$$

4. Evaluate standard Gaussian variates:
   $$Z_1 = 1.499287 \times (-0.587785) \approx -0.8813$$
   $$Z_2 = 1.499287 \times (-0.809017) \approx -1.2129$$

### Solution, step 2: Construction of the Cholesky Decomposition
The covariance matrix for the bivariate asset vector is:
$$\mathbf{\Sigma} = \begin{pmatrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{pmatrix} = \begin{pmatrix} 15^2 & 0.60 \times 15 \times 8 \\ 0.60 \times 15 \times 8 & 8^2 \end{pmatrix} = \begin{pmatrix} 225 & 72 \\ 72 & 64 \end{pmatrix}$$

We find the lower triangular Cholesky factor $\mathbf{L} = \begin{pmatrix} l_{11} & 0 \\ l_{21} & l_{22} \end{pmatrix}$ such that $\mathbf{L} \mathbf{L}^T = \mathbf{\Sigma}$:
1. $l_{11} = \sigma_1 = 15$.
2. $l_{21} = \frac{\rho \sigma_1 \sigma_2}{l_{11}} = \frac{72}{15} = 4.80 = \rho \sigma_2 = 0.60 \times 8 = 4.80$.
3. $l_{22} = \sqrt{\sigma_2^2 - l_{21}^2} = \sqrt{64 - 4.80^2} = \sqrt{64 - 23.04} = \sqrt{40.96} = 6.40 = \sigma_2 \sqrt{1 - \rho^2}$.

The Cholesky matrix is:
$$\mathbf{L} = \begin{pmatrix} 15 & 0 \\ 4.80 & 6.40 \end{pmatrix}$$

### Solution, step 3: Evaluation of Correlated Vector $\mathbf{X}$
Applying the linear transformation $\mathbf{X} = \mathbf{\mu} + \mathbf{L} \mathbf{Z}$:
$$X_1 = \mu_1 + l_{11} Z_1 = 100 + 15 \times (-0.8813) = 100 - 13.2195 = 86.7805 \approx 86.78$$
$$X_2 = \mu_2 + l_{21} Z_1 + l_{22} Z_2 = 50 + 4.80 \times (-0.8813) + 6.40 \times (-1.2129)$$
$$X_2 = 50 - 4.2302 - 7.7626 = 50 - 11.9928 = 38.0072 \approx 38.01$$

The simulated correlated portfolio asset price vector is $\mathbf{X} = (86.78, 38.01)^T$.

## Fully worked question 3: Walker's Alias Table Construction for Categorical Sampling

### Question
An algorithmic agent simulates state transitions for a discrete Markov process with $k = 4$ states $\{1, 2, 3, 4\}$.
The discrete probability mass function is:
$$p_1 = 0.10, \quad p_2 = 0.40, \quad p_3 = 0.30, \quad p_4 = 0.20$$
1. Formulate the scaled probabilities $n \cdot p_j$ and construct the complete Alias Table (probability cutoff vector $\mathbf{q}$ and alias pointer vector $\mathbf{A}$) using Walker's construction algorithm.
2. Given a uniform pseudorandom variate $u = 0.6800$, trace the $\mathcal{O}(1)$ alias sampling algorithm to determine the simulated state.

### Solution, step 1: Construction of Walker's Alias Table
The number of categories is $k = 4$.
- Scaled probabilities $w_j = k \cdot p_j$:
  $$w_1 = 4 \times 0.10 = 0.40$$
  $$w_2 = 4 \times 0.40 = 1.60$$
  $$w_3 = 4 \times 0.30 = 1.20$$
  $$w_4 = 4 \times 0.20 = 0.80$$

Partition the indices into two dynamic worklists based on whether $w_j < 1$ or $w_j \ge 1$:
- **Small list** ($w_j < 1$): $S = [1, 4]$ (with weights $w_1 = 0.40, w_4 = 0.80$).
- **Large list** ($w_j \ge 1$): $L = [2, 3]$ (with weights $w_2 = 1.60, w_3 = 1.20$).

We execute the iterative pairing steps:
- **Iteration 1**:
  Pop small index $s = 1$ ($w_1 = 0.40$) and large index $l = 2$ ($w_2 = 1.60$).
  Set cutoff: $q_1 = w_1 = 0.40$.
  Set alias pointer: $A_1 = l = 2$.
  Adjust large weight: $w_2 \leftarrow w_2 - (1 - w_1) = 1.60 - 0.60 = 1.00$.
  Since new $w_2 = 1.00 \ge 1$, re-insert $2$ into $L$.
  Lists remaining: $S = [4]$, $L = [2, 3]$ (with weights $w_4 = 0.80, w_2 = 1.00, w_3 = 1.20$).

- **Iteration 2**:
  Pop small index $s = 4$ ($w_4 = 0.80$) and large index $l = 3$ ($w_3 = 1.20$).
  Set cutoff: $q_4 = w_4 = 0.80$.
  Set alias pointer: $A_4 = l = 3$.
  Adjust large weight: $w_3 \leftarrow w_3 - (1 - w_4) = 1.20 - 0.20 = 1.00$.
  Re-insert $3$ into $L$.
  Lists remaining: $S = []$, $L = [2, 3]$ (both with weights $1.00$).

- **Finalization**:
  The small list is empty. For all remaining indices in $L$ (indices 2 and 3), set their cutoffs to $1.00$:
  $$q_2 = 1.00, \quad A_2 = 2$$
  $$q_3 = 1.00, \quad A_3 = 3$$

The resulting Alias Table is:
<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Bucket $j$</th>
<th>Primary Outcome</th>
<th>Cutoff Probability $q_j$</th>
<th>Alias Outcome $A_j$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>State 1</td>
<td>0.40</td>
<td>State 2</td>
</tr>
<tr>
<td>2</td>
<td>State 2</td>
<td>1.00</td>
<td>State 2</td>
</tr>
<tr>
<td>3</td>
<td>State 3</td>
<td>1.00</td>
<td>State 3</td>
</tr>
<tr>
<td>4</td>
<td>State 4</td>
<td>0.80</td>
<td>State 3</td>
</tr>
</tbody>
</table>
</div>

### Solution, step 2: Tracing the $\mathcal{O}(1)$ Alias Lookup for $u = 0.6800$
Given $u = 0.6800$ and $k = 4$:
1. Scale by $k$:
   $$X = k \cdot u = 4 \times 0.6800 = 2.7200$$
2. Determine bucket index $I$:
   $$I = \lfloor X \rfloor + 1 = \lfloor 2.7200 \rfloor + 1 = 2 + 1 = 3$$
3. Determine fractional remainder $V$:
   $$V = X - \lfloor X \rfloor = 2.7200 - 2.0000 = 0.7200$$
4. Compare $V$ with cutoff probability $q_I$:
   For bucket $I = 3$, the cutoff is $q_3 = 1.00$.
   Since $V = 0.7200 < q_3 = 1.00$, we select the primary outcome of bucket 3:
   $$\text{Simulated State} = 3$$
The algorithm executed in pure constant time without searching!
"""

(DRAFT_DIR / "unit-2.md").write_text(u2.strip() + "\n", encoding="utf-8")
print("Unit 2 generated.")
# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3 = r"""# Unit 3: Rejection Sampling & Envelope Methods

While the Inverse Transform Method provides an exact, monotonic mechanism for sampling univariate random variables, many of the most fundamental probability distributions in mathematical statistics—such as the standard Gamma distribution with non-integer shape parameters $\alpha \notin \mathbb{N}$, the general Beta distribution $\text{Beta}(\alpha, \beta)$, and non-standard Bayesian posterior densities known only up to an intractable normalizing constant—possess cumulative distribution functions that cannot be inverted analytically or evaluated efficiently.

To generate random draws from complex or unnormalized target probability densities, John von Neumann formulated the seminal **Acceptance-Rejection Sampling Principle** in 1951. Rejection sampling constructs an artificial geometric envelope over the target density, draws candidate points from an easily sampled instrumental proposal distribution, and probabilistically filters candidates to produce exact, independent draws from the target distribution.

## 3.1 The Fundamental Acceptance-Rejection Principle

Let $f(x)$ denote the target probability density function from which we desire to simulate random draws, defined on support $\mathcal{X} \subseteq \mathbb{R}^d$. The target density may be unnormalized:
$$f(x) = \frac{\tilde{f}(x)}{Z_f}$$
where $\tilde{f}(x) \ge 0$ is analytically computable, but the normalizing constant $Z_f = \int_{\mathcal{X}} \tilde{f}(x)\,dx$ is difficult or impossible to integrate.

Let $g(x)$ be an **instrumental proposal density** satisfying two conditions:
1. Candidate variates $Y \sim g(y)$ can be simulated easily and rapidly (e.g., via inversion or standard Gaussian/exponential generators).
2. The support of $g$ covers the support of $f$:
   $$\{x : f(x) > 0\} \subseteq \{x : g(x) > 0\}$$

Assume there exists a finite bounding constant $c \ge 1$ such that the envelope function $c \cdot g(x)$ blankets the target density everywhere on its support:

$$\frac{f(x)}{g(x)} \le c \iff f(x) \le c \cdot g(x) \quad \text{for all } x \in \mathcal{X}$$

The minimum valid envelope constant is the supremum of the density ratio:

$$c = \sup_{x \in \mathcal{X}} \frac{f(x)}{g(x)}$$

### The Acceptance-Rejection Algorithm
1. **Generate Candidate**: Draw a candidate variate $Y \sim g(y)$.
2. **Generate Uniform Filter**: Draw an independent uniform variate $U \sim \mathcal{U}(0, 1)$.
3. **Acceptance Test**:
   - If:
     $$U \le \frac{f(Y)}{c \cdot g(Y)}$$
     **Accept** the candidate and output $X = Y$.
   - Otherwise, **reject** $Y$, discard both $Y$ and $U$, and return to Step 1.

## 3.2 Mathematical Proof of Validity and Geometric Intuition

The mathematical validity of rejection sampling rests on establishing that the conditional distribution of accepted candidates matches the target density $f(x)$ exactly.

### Rigorous Theorem and Proof
*Theorem (Von Neumann Rejection Sampling)*: The conditional distribution of the random variable $Y$, given that the acceptance event $A = \left\{ U \le \frac{f(Y)}{c \cdot g(Y)} \right\}$ occurs, has probability density identically equal to $f(x)$:

$$f_{Y \mid A}(x) = f(x)$$

Furthermore, the overall marginal probability of acceptance on any single trial is:

$$P(A) = \frac{1}{c}$$

*Proof*:
Let $A$ denote the acceptance event $\left\{ U \le \frac{f(Y)}{c \cdot g(Y)} \right\}$.
We first compute the overall marginal probability of acceptance $P(A)$ by conditioning on candidate $Y$:
$$P(A) = \mathbb{E}\left[ P(A \mid Y) \right] = \int_{\mathcal{X}} P\left( U \le \frac{f(y)}{c \cdot g(y)} \Bigg| Y = y \right) g(y)\,dy$$
Because $U \sim \mathcal{U}(0, 1)$ independently of $Y$, for any ratio $r \in [0, 1]$, $P(U \le r) = r$.
Since $\frac{f(y)}{c \cdot g(y)} \le 1$ by definition of $c$:
$$P\left( U \le \frac{f(y)}{c \cdot g(y)} \Bigg| Y = y \right) = \frac{f(y)}{c \cdot g(y)}$$
Substituting into the integral:
$$P(A) = \int_{\mathcal{X}} \left( \frac{f(y)}{c \cdot g(y)} \right) g(y)\,dy = \frac{1}{c} \int_{\mathcal{X}} f(y)\,dy$$
Since $f(y)$ is a valid probability density function, $\int_{\mathcal{X}} f(y)\,dy = 1$. Therefore:
$$P(A) = \frac{1}{c}$$

Next, we evaluate the cumulative distribution function of accepted candidates for any set $\mathcal{B} \subseteq \mathcal{X}$:
$$P(Y \in \mathcal{B} \mid A) = \frac{P(Y \in \mathcal{B} \cap A)}{P(A)} = \frac{\int_{\mathcal{B}} P(A \mid Y = y) g(y)\,dy}{1 / c}$$
Substituting $P(A \mid Y = y) = \frac{f(y)}{c \cdot g(y)}$:
$$P(Y \in \mathcal{B} \mid A) = c \int_{\mathcal{B}} \left( \frac{f(y)}{c \cdot g(y)} \right) g(y)\,dy = c \int_{\mathcal{B}} \frac{f(y)}{c}\,dy = \int_{\mathcal{B}} f(y)\,dy$$
Differentiating with respect to the boundary of $\mathcal{B}$ yields the target probability density $f(x)$ identically. This completes the proof.

### The Number of Trials to Acceptance
Let $N$ denote the number of candidate draws required to achieve one accepted variate. Because successive trials are mutually independent with constant success probability $p = 1/c$, $N$ follows a **Geometric Distribution**:
$$N \sim \text{Geometric}\left( p = \frac{1}{c} \right)$$
$$P(N = k) = (1 - p)^{k-1} p = \left( 1 - \frac{1}{c} \right)^{k-1} \frac{1}{c} \quad \text{for } k = 1, 2, 3, \dots$$
The expected number of candidate proposals evaluated per accepted draw is:
$$\mathbb{E}[N] = \frac{1}{p} = c$$
The bounding constant $c$ directly quantifies the **computational waste**:
- If $c = 1.25$, on average $1.25$ proposals are evaluated per accepted draw ($80\%$ acceptance efficiency).
- If $c = 20$, on average $20$ candidate evaluations are wasted per sample ($5\%$ efficiency).
Minimizing $c$ through tight envelope design is paramount.

## 3.3 Sampling the Gamma Distribution via Rejection Envelopes

The standard Gamma distribution $\text{Gamma}(\alpha, 1)$ with shape parameter $\alpha > 0$ has density:
$$f(x) = \frac{1}{\Gamma(\alpha)} x^{\alpha - 1} e^{-x} \quad \text{for } x > 0$$
When $\alpha = 1$, the distribution collapses to standard Exponential $\text{Exp}(1)$, which is sampled directly via inversion $X = -\ln U$.
When $\alpha = k \in \mathbb{N}$ is an integer, $X$ represents the sum of $k$ independent $\text{Exp}(1)$ variables:
$$X = -\sum_{i=1}^k \ln U_i = -\ln\left( \prod_{i=1}^k U_i \right)$$

However, for arbitrary non-integer shape parameters $\alpha > 1$, rejection sampling is indispensable.

### Gamma Generation for $\alpha > 1$: Marsaglia and Tsang's Method
A seminal, universally adopted algorithm formulated by George Marsaglia and Wai Wan Tsang (2000) transforms standard normal variates into Gamma variates.
Let $d = \alpha - 1/3$ and $c = 1 / \sqrt{9d}$.
1. Generate $Z \sim \mathcal{N}(0, 1)$ and $U \sim \mathcal{U}(0, 1)$.
2. Set $V = (1 + c Z)^3$.
3. If $V \le 0$, reject and return to Step 1.
4. If $\ln U < \frac{1}{2} Z^2 + d - d V + d \ln V$:
   Accept and return $X = d \cdot V$.
Marsaglia-Tsang achieves an acceptance rate exceeding $95\%$ across all $\alpha \ge 1$, requiring on average only $1.05$ normal draws per Gamma variate.

## 3.4 Sampling the Beta Distribution via Uniform and Triangular Envelopes

The standard Beta distribution $\text{Beta}(\alpha, \beta)$ with parameters $\alpha, \beta > 0$ has density:
$$f(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1} \quad \text{for } x \in (0, 1)$$
where $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ is the normalizing Beta function.

### Case 1: Sampling when $\alpha \ge 1$ and $\beta \ge 1$ (Unimodal Density)
When both parameters are at least 1, the density is bounded and unimodal on $[0, 1]$, achieving its mode at:
$$x^* = \frac{\alpha - 1}{\alpha + \beta - 2}$$
The maximum density value is:
$$f(x^*) = \frac{1}{B(\alpha, \beta)} (x^*)^{\alpha - 1} (1 - x^*)^{\beta - 1}$$
We can select a standard uniform proposal density $g(x) = 1$ on $[0, 1]$.
The envelope constant is simply the mode height:
$$c = \sup_{x \in [0, 1]} \frac{f(x)}{1} = f(x^*)$$
The acceptance criterion simplifies to:
$$U_2 \le \frac{f(U_1)}{c} = \left( \frac{U_1}{x^*} \right)^{\alpha - 1} \left( \frac{1 - U_1}{1 - x^*} \right)^{\beta - 1}$$
where $U_1, U_2 \sim \mathcal{U}(0, 1)$. Notice that the normalizing constant $B(\alpha, \beta)$ cancels out completely!

### Case 2: General Beta via Independent Gamma Variates
An alternative, exact transformation method utilizes Johnk's theorem: if $Y_1 \sim \text{Gamma}(\alpha, 1)$ and $Y_2 \sim \text{Gamma}(\beta, 1)$ are independent random variables, then:
$$X = \frac{Y_1}{Y_1 + Y_2} \sim \text{Beta}(\alpha, \beta)$$
This identity holds for all positive parameters $\alpha, \beta > 0$, bypassing the bounded mode requirement.

## 3.5 Adaptive Rejection Sampling (ARS) for Log-Concave Densities

When sampling from complex unnormalized densities where finding an analytical proposal density $g(x)$ is difficult, Walter Gilks and Pascal Wild (1992) devised **Adaptive Rejection Sampling (ARS)**.

ARS applies to any **log-concave density** $f(x)$, meaning the log-density:
$$h(x) = \ln f(x)$$
is a concave function: $h''(x) \le 0$ for all $x$. Standard log-concave distributions include the Normal, Gamma ($\alpha \ge 1$), Beta ($\alpha, \beta \ge 1$), Logistic, and Extreme Value distributions.

### The Tangent Hull Envelope
Because $h(x)$ is concave, any tangent line constructed at an evaluation point $x_k$:
$$T_k(x) = h(x_k) + (x - x_k) h'(x_k)$$
lies strictly above the curve everywhere: $T_k(x) \ge h(x)$ for all $x$.

Given an initial set of grid points $S_n = \{x_1 < x_2 < \dots < x_n\}$:
1. Construct the piecewise linear upper hull $u_n(x) = \min_k T_k(x)$.
2. The envelope density is the normalized piecewise exponential function:
   $$g_n(x) = \frac{\exp(u_n(x))}{\int \exp(u_n(t))\,dt}$$
   which can be sampled directly via piecewise exponential inversion.
3. If a candidate $Y$ is drawn and rejected, the evaluation $h(Y)$ and derivative $h'(Y)$ are added to the support set:
   $$S_{n+1} = S_n \cup \{Y\}$$
Each rejected candidate refines the upper hull, making the envelope tighter and driving the acceptance probability asymptotically toward $100\%$!

## Fully worked question 1: Optimal Envelope Constant for Normal Generation via Exponential

### Question
To simulate standard normal variates $Z \sim \mathcal{N}(0, 1)$ without computing trigonometric functions, an actuary uses the absolute normal (half-normal) target density:
$$f(x) = \sqrt{\frac{2}{\pi}} e^{-x^2/2} \quad \text{for } x \ge 0$$
using a standard exponential proposal density with rate parameter $\lambda > 0$:
$$g(x) = \lambda e^{-\lambda x} \quad \text{for } x \ge 0$$
Once a half-normal variate $X$ is accepted, a random sign $S \in \{-1, +1\}$ is applied ($Z = S \cdot X$) with equal probability.

1. Derive the density ratio function $R(x; \lambda) = \frac{f(x)}{g(x)}$ and find the optimal parameter $\lambda^*$ that minimizes the bounding constant $c(\lambda)$.
2. Calculate the optimal bounding constant $c^*$ and the resulting acceptance probability $P(\text{accept})$.
3. State the exact acceptance condition for candidate $Y \sim \text{Exp}(\lambda^*)$.

### Solution, step 1: Optimization of the Rate Parameter $\lambda$
The density ratio is:
$$R(x; \lambda) = \frac{f(x)}{g(x)} = \frac{\sqrt{\frac{2}{\pi}} e^{-x^2/2}}{\lambda e^{-\lambda x}} = \frac{1}{\lambda} \sqrt{\frac{2}{\pi}} \exp\left( \lambda x - \frac{x^2}{2} \right)$$
To find the bounding constant $c(\lambda) = \sup_{x \ge 0} R(x; \lambda)$, we maximize the exponent:
$$h(x) = \lambda x - \frac{x^2}{2}$$
Differentiating with respect to $x$:
$$h'(x) = \lambda - x = 0 \implies x^* = \lambda$$
Evaluating at $x^* = \lambda$:
$$h(x^*) = \lambda^2 - \frac{\lambda^2}{2} = \frac{\lambda^2}{2}$$
Thus, for any fixed $\lambda > 0$, the maximum ratio is:
$$c(\lambda) = R(\lambda; \lambda) = \frac{1}{\lambda} \sqrt{\frac{2}{\pi}} e^{\lambda^2/2}$$

To minimize $c(\lambda)$ with respect to $\lambda$, take the natural logarithm:
$$\ln c(\lambda) = -\ln\lambda + \frac{1}{2}\ln(2/\pi) + \frac{\lambda^2}{2}$$
Differentiating with respect to $\lambda$ and equating to zero:
$$\frac{d}{d\lambda} \ln c(\lambda) = -\frac{1}{\lambda} + \lambda = 0 \implies \lambda^2 = 1 \implies \lambda^* = 1$$
*Conclusion*: The optimal proposal parameter is $\lambda^* = 1$ (the standard exponential distribution $\text{Exp}(1)$).

### Solution, step 2: Calculation of the Bounding Constant $c^*$ and Efficiency
Substituting $\lambda^* = 1$ into $c(\lambda)$:
$$c^* = c(1) = \frac{1}{1} \sqrt{\frac{2}{\pi}} e^{1/2} = \sqrt{\frac{2 e}{\pi}}$$
Evaluating numerically:
$$2 e = 2 \times 2.7182818 \approx 5.4365636$$
$$\frac{2e}{\pi} \approx \frac{5.4365636}{3.14159265} \approx 1.730787$$
$$c^* = \sqrt{1.730787} \approx 1.315489 \approx 1.3155$$

The acceptance probability is:
$$P(\text{accept}) = \frac{1}{c^*} = \frac{1}{1.315489} \approx 0.7602 \quad (76.02\%)$$
The expected number of exponential candidate evaluations per accepted half-normal variate is $\mathbb{E}[N] = c^* \approx 1.3155$.

### Solution, step 3: Exact Algorithmic Acceptance Condition
For $\lambda = 1$, the candidate is $Y = -\ln U_1 \sim \text{Exp}(1)$.
The acceptance test is:
$$U_2 \le \frac{f(Y)}{c^* g(Y)} = \frac{\sqrt{\frac{2}{\pi}} e^{-Y^2/2}}{\sqrt{\frac{2e}{\pi}} e^{-Y}} = \frac{e^{-Y^2/2}}{e^{1/2} e^{-Y}} = \exp\left( -\frac{Y^2}{2} + Y - \frac{1}{2} \right) = \exp\left( -\frac{(Y - 1)^2}{2} \right)$$
Taking natural logarithms of both sides:
$$\ln U_2 \le -\frac{(Y - 1)^2}{2} \iff -\ln U_2 \ge \frac{(Y - 1)^2}{2}$$
Notice that $E_2 = -\ln U_2 \sim \text{Exp}(1)$ is another independent exponential random variable!
The rejection algorithm becomes extraordinarily elegant:
1. Generate two independent exponential variates $Y, E_2 \sim \text{Exp}(1)$ (via $-\ln U_1, -\ln U_2$).
2. Check if $E_2 \ge \frac{(Y - 1)^2}{2}$.
   - If true, accept $X = Y$.
   - If false, reject and repeat.
3. Draw random sign $S \in \{-1, +1\}$ and return $Z = S \cdot Y$.
This completely avoids transcendental sine, cosine, and square root operations.

## Fully worked question 2: Rejection Sampling from a Bounded Beta Distribution

### Question
An industrial reliability engineer models the proportion of daily component degradation $X \in (0, 1)$ using a $\text{Beta}(3, 2)$ distribution with probability density function:
$$f(x) = \frac{1}{B(3, 2)} x^{3 - 1} (1 - x)^{2 - 1} = 12 x^2 (1 - x) \quad \text{for } 0 \le x \le 1$$
The engineer designs an acceptance-rejection algorithm using a standard uniform proposal distribution $g(x) = 1$ on $[0, 1]$.
1. Determine the analytical mode $x^*$ of the target distribution and compute the optimal bounding constant $c$.
2. Compute the exact theoretical acceptance probability and expected number of proposal draws per sample.
3. Three candidate uniform proposals are generated:
   - Trial 1: Candidate $y_1 = 0.20$, filter $u_1 = 0.40$.
   - Trial 2: Candidate $y_2 = 0.80$, filter $u_2 = 0.85$.
   - Trial 3: Candidate $y_3 = 0.60$, filter $u_3 = 0.70$.
   Determine which candidates are accepted or rejected.

### Solution, step 1: Optimization of the Bounding Constant $c$
The density ratio for $g(x) = 1$ is:
$$R(x) = \frac{f(x)}{1} = 12 x^2 (1 - x) = 12 (x^2 - x^3)$$
To find the maximum on $[0, 1]$, differentiate with respect to $x$:
$$R'(x) = 12 (2x - 3x^2) = 12 x (2 - 3x) = 0$$
The interior critical point is:
$$x^* = \frac{2}{3}$$
Second derivative test:
$$R''(x^*) = 12(2 - 6x^*) = 12\left(2 - 6 \times \frac{2}{3}\right) = 12(2 - 4) = -24 < 0 \implies \text{local maximum}$$
Evaluating at mode $x^* = 2/3$:
$$c = R(2/3) = 12 \left( \frac{2}{3} \right)^2 \left( 1 - \frac{2}{3} \right) = 12 \times \frac{4}{9} \times \frac{1}{3} = \frac{48}{27} = \frac{16}{9} \approx 1.7778$$

### Solution, step 2: Calculation of Acceptance Probability and Expected Iterations
The theoretical probability of acceptance is:
$$P(\text{accept}) = \frac{1}{c} = \frac{1}{16 / 9} = \frac{9}{16} = 0.5625 \quad (56.25\%)$$
The expected number of trials required to accept a single variate is:
$$\mathbb{E}[N] = c = \frac{16}{9} \approx 1.78 \text{ trials}$$

### Solution, step 3: Evaluation of the Three Candidate Trials
The acceptance test condition for candidate $y_i$ with filter $u_i$ is:
$$u_i \le \frac{f(y_i)}{c \cdot g(y_i)} = \frac{12 y_i^2 (1 - y_i)}{16 / 9} = \frac{108}{16} y_i^2 (1 - y_i) = \frac{27}{4} y_i^2 (1 - y_i) = 6.75 \cdot y_i^2 (1 - y_i)$$

- **Trial 1 ($y_1 = 0.20, u_1 = 0.40$)**:
  $$\frac{f(y_1)}{c} = 6.75 \times (0.20)^2 \times (1 - 0.20) = 6.75 \times 0.04 \times 0.80 = 6.75 \times 0.032 = 0.216$$
  Compare with filter $u_1 = 0.40$:
  $$u_1 = 0.40 > 0.216$$
  *Result*: **Rejected**.

- **Trial 2 ($y_2 = 0.80, u_2 = 0.85$)**:
  $$\frac{f(y_2)}{c} = 6.75 \times (0.80)^2 \times (1 - 0.80) = 6.75 \times 0.64 \times 0.20 = 6.75 \times 0.128 = 0.864$$
  Compare with filter $u_2 = 0.85$:
  $$u_2 = 0.85 \le 0.864$$
  *Result*: **Accepted**! Output $X = 0.80$.

- **Trial 3 ($y_3 = 0.60, u_3 = 0.70$)**:
  $$\frac{f(y_3)}{c} = 6.75 \times (0.60)^2 \times (1 - 0.60) = 6.75 \times 0.36 \times 0.40 = 6.75 \times 0.144 = 0.972$$
  Compare with filter $u_3 = 0.70$:
  $$u_3 = 0.70 \le 0.972$$
  *Result*: **Accepted**! Output $X = 0.60$.

## Fully worked question 3: Gamma Sampling via Cauchy Envelope

### Question
To simulate Gamma variates $X \sim \text{Gamma}(\alpha = 2, \beta = 1)$ with density:
$$f(x) = x e^{-x} \quad \text{for } x > 0$$
a computational statistician considers a half-Cauchy proposal density:
$$g(x) = \frac{2}{\pi (1 + x^2)} \quad \text{for } x > 0$$
1. Formulate the ratio $R(x) = f(x)/g(x)$ and prove that $R(x)$ is bounded on $(0, \infty)$.
2. Calculate the optimal bounding constant $c = \sup_{x > 0} R(x)$ and determine the acceptance efficiency $1/c$.
3. Contrast the efficiency of this Cauchy proposal with an exponential proposal $g(x) = \lambda e^{-\lambda x}$.

### Solution, step 1: Formulation and Boundedness of the Density Ratio
The density ratio is:
$$R(x) = \frac{f(x)}{g(x)} = \frac{x e^{-x}}{\frac{2}{\pi (1 + x^2)}} = \frac{\pi}{2} x (1 + x^2) e^{-x} = \frac{\pi}{2} (x + x^3) e^{-x}$$
We examine the boundary behavior:
- At $x \to 0^+$:
  $$\lim_{x \to 0^+} R(x) = \frac{\pi}{2} (0 + 0) e^0 = 0$$
- As $x \to \infty$:
  $$\lim_{x \to \infty} R(x) = \frac{\pi}{2} \lim_{x \to \infty} \frac{x^3 + x}{e^x} = 0$$
  by repeated application of L'Hôpital's rule.
Because $R(x) \ge 0$ for all $x > 0$, is continuous on $(0, \infty)$, and vanishes at both boundaries, by the Extreme Value Theorem, $R(x)$ must achieve a finite global maximum $c$ on $(0, \infty)$.

### Solution, step 2: Finding the Maximum Ratio $c$
Differentiating $h(x) = (x^3 + x) e^{-x}$:
$$h'(x) = (3x^2 + 1) e^{-x} - (x^3 + x) e^{-x} = (-x^3 + 3x^2 - x + 1) e^{-x}$$
Setting $h'(x) = 0 \iff x^3 - 3x^2 + x - 1 = 0$.
Notice:
- At $x = 2$: $2^3 - 3(4) + 2 - 1 = 8 - 12 + 2 - 1 = -3$.
- At $x = 3$: $3^3 - 3(9) + 3 - 1 = 27 - 27 + 3 - 1 = +2$.
By the Intermediate Value Theorem, a unique root lies in $(2, 3)$.
Solving via Newton-Raphson iteration:
$$x_{n+1} = x_n - \frac{x_n^3 - 3x_n^2 + x_n - 1}{3x_n^2 - 6x_n + 1}$$
Starting from $x_0 = 2.70$:
- $f(2.70) = 2.70^3 - 3(2.70^2) + 2.70 - 1 = 19.683 - 21.87 + 2.70 - 1 = -0.487$.
- $f'(2.70) = 3(7.29) - 6(2.70) + 1 = 21.87 - 16.20 + 1 = 6.67$.
- $x_1 = 2.70 - (-0.487 / 6.67) \approx 2.70 + 0.073 = 2.773$.
Iterating yields root $x^* \approx 2.7693$.

Evaluating $h(x^*)$:
$$(x^*)^3 + x^* \approx 2.7693^3 + 2.7693 \approx 21.237 + 2.769 = 24.006$$
$$e^{-x^*} = e^{-2.7693} \approx 0.062706$$
$$h(x^*) = 24.006 \times 0.062706 \approx 1.5053$$
The bounding constant is:
$$c = \frac{\pi}{2} h(x^*) \approx 1.570796 \times 1.5053 \approx 2.3645$$

The acceptance probability is:
$$P(\text{accept}) = \frac{1}{c} \approx \frac{1}{2.3645} \approx 0.423 \quad (42.3\%)$$

### Solution, step 3: Comparison with Exponential Proposal
Consider an exponential proposal $g_{\text{exp}}(x) = \lambda e^{-\lambda x}$.
The ratio is:
$$R_{\text{exp}}(x) = \frac{x e^{-x}}{\lambda e^{-\lambda x}} = \frac{1}{\lambda} x e^{-(1 - \lambda)x}$$
For this ratio to be bounded as $x \to \infty$, we must have $1 - \lambda > 0 \implies \lambda < 1$.
The maximum occurs at $x^* = \frac{1}{1 - \lambda}$:
$$c(\lambda) = \frac{1}{\lambda(1 - \lambda)} e^{-1}$$
Minimizing over $\lambda \in (0, 1)$ yields $\lambda^* = 0.50$:
$$c_{\text{exp}} = \frac{1}{0.50 \times 0.50} e^{-1} = 4 e^{-1} \approx \frac{4}{2.71828} \approx 1.4715$$
The acceptance efficiency for the exponential proposal is:
$$P(\text{accept})_{\text{exp}} = \frac{1}{1.4715} \approx 0.6796 \quad (67.96\%)$$

*Conclusion*: The exponential proposal achieves $68\%$ efficiency, substantially outperforming the Cauchy proposal ($42\%$). Because Cauchy tails ($1/x^2$) decay much slower than Gamma tails ($x e^{-x}$), the Cauchy envelope is unnecessarily thick in the tails, causing heavy rejection.
"""

(DRAFT_DIR / "unit-3.md").write_text(u3.strip() + "\n", encoding="utf-8")
print("Unit 3 generated.")
# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4 = r"""# Unit 4: Monte Carlo Integration & Precision

In scientific computing, quantitative finance, and high-dimensional Bayesian inference, researchers frequently encounter definite integrals that cannot be evaluated analytically:
$$\theta = \int_{\mathcal{D}} g(\mathbf{x})\,d\mathbf{x}$$
where $\mathcal{D} \subseteq \mathbb{R}^d$ is a multidimensional integration domain. When the dimension $d$ exceeds 3 or 4, classical deterministic numerical quadrature rules (such as the Trapezoidal rule, Simpson's rule, and Gauss-Legendre quadrature) suffer an exponential computational collapse known as the **Curse of Dimensionality**.

**Monte Carlo Integration**, conceived by Stanislaw Ulam, John von Neumann, and Nicholas Metropolis during the Manhattan Project at Los Alamos in the late 1940s, circumvents the curse of dimensionality by reformulating deterministic integration problems as stochastic expectations.

## 4.1 Foundations of Crude Monte Carlo Integration

Let $\theta$ denote the integral of a real-valued function $h(\mathbf{x})$ over a domain $\mathcal{D}$ with respect to a continuous probability density function $f(\mathbf{x})$:

$$\theta = \mathbb{E}_f[h(\mathbf{X})] = \int_{\mathcal{D}} h(\mathbf{x}) f(\mathbf{x})\,d\mathbf{x}$$

If the original integral is an unweighted Lebesgue integral over a bounded hypercube $\mathcal{D} = [a_1, b_1] \times \dots \times [a_d, b_d]$ with total hypervolume $V = \prod_{j=1}^d (b_j - a_j)$:
$$I = \int_{\mathcal{D}} g(\mathbf{x})\,d\mathbf{x} = V \int_{\mathcal{D}} g(\mathbf{x}) \left( \frac{1}{V} \right) d\mathbf{x} = V \cdot \mathbb{E}[g(\mathbf{U})]$$
where $\mathbf{U} \sim \mathcal{U}(\mathcal{D})$ is uniformly distributed across the domain.

### 1. The Monte Carlo Estimator
Let $\mathbf{X}_1, \mathbf{X}_2, \dots, \mathbf{X}_n$ be an independent and identically distributed (i.i.d.) random sample drawn from density $f(\mathbf{x})$. The **Crude Monte Carlo Estimator** of $\theta$ is the sample mean of the evaluated function values:

$$\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^n h(\mathbf{X}_i)$$

### 2. Theoretical Statistical Properties
1. **Unbiasedness**:
   $$\mathbb{E}[\hat{\theta}_n] = \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n h(\mathbf{X}_i) \right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[h(\mathbf{X}_i)] = \frac{1}{n} (n \theta) = \theta$$
   The estimator is strictly unbiased for any finite sample size $n \ge 1$.
2. **Strong Consistency (Convergence Almost Surely)**:
   Assuming the function is absolutely integrable ($\mathbb{E}[|h(\mathbf{X})|] < \infty$), by the **Kolmogorov Strong Law of Large Numbers**:
   $$P\left( \lim_{n \to \infty} \hat{\theta}_n = \theta \right) = 1$$
3. **Finite-Sample Variance**:
   Assuming square integrability ($\sigma^2 = \mathrm{Var}_f(h(\mathbf{X})) = \int (h(\mathbf{x}) - \theta)^2 f(\mathbf{x})\,dx < \infty$):
   $$\mathrm{Var}(\hat{\theta}_n) = \mathrm{Var}\left( \frac{1}{n} \sum_{i=1}^n h(\mathbf{X}_i) \right) = \frac{1}{n^2} \sum_{i=1}^n \mathrm{Var}(h(\mathbf{X}_i)) = \frac{\sigma^2}{n}$$
   The standard error of the Monte Carlo estimator decays at the universal rate:
   $$\text{SE}(\hat{\theta}_n) = \frac{\sigma}{\sqrt{n}} = \mathcal{O}\left( \frac{1}{\sqrt{n}} \right)$$

## 4.2 Asymptotic Error Distribution and Confidence Intervals

By the **Lindeberg-Lévy Central Limit Theorem**, as the simulation sample size $n \to \infty$, the standardized estimation error converges in distribution to the standard Gaussian distribution:

$$\frac{\hat{\theta}_n - \theta}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

In practice, the true population variance $\sigma^2$ is unknown and must be estimated consistently from the simulated trajectory using the sample variance:

$$S_n^2 = \frac{1}{n - 1} \sum_{i=1}^n \left( h(\mathbf{X}_i) - \hat{\theta}_n \right)^2 = \frac{1}{n - 1} \left( \sum_{i=1}^n h(\mathbf{X}_i)^2 - n \hat{\theta}_n^2 \right)$$

By Slutsky's theorem:

$$\frac{\hat{\theta}_n - \theta}{S_n / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

### Asymptotic Confidence Intervals
An asymptotic $(1 - \alpha) \times 100\%$ confidence interval for the true integral $\theta$ is:

$$\mathcal{CI}_{1-\alpha} = \left[ \hat{\theta}_n - z_{1 - \alpha/2} \frac{S_n}{\sqrt{n}}, \; \hat{\theta}_n + z_{1 - \alpha/2} \frac{S_n}{\sqrt{n}} \right]$$

where $z_{1 - \alpha/2} = \Phi^{-1}(1 - \alpha/2)$ is the upper standard normal critical quantile (e.g., $z_{0.975} \approx 1.960$ for a $95\%$ confidence interval).

## 4.3 Deterministic Quadrature vs Monte Carlo: The Curse of Dimensionality

To appreciate why Monte Carlo integration is irreplaceable in modern science, consider the mathematical convergence rates of classical deterministic numerical integration algorithms in $d$-dimensional space.

### 1. Deterministic Numerical Quadrature Error Rates
To evaluate an integral over the unit hypercube $[0, 1]^d$ using a grid-based quadrature rule:
- Let $k$ denote the number of grid subdivisions along each individual coordinate axis.
- The total number of evaluation nodes across the hypercube is:
  $$n = k^d \implies k = n^{1/d}$$

For standard classical quadrature rules:
1. **Riemann Sum / Midpoint Rule**: The error scales as $\mathcal{O}(1 / k) = \mathcal{O}(n^{-1/d})$.
2. **Trapezoidal Rule**: For twice-differentiable integrands, the error scales as $\mathcal{O}(1 / k^2) = \mathcal{O}(n^{-2/d})$.
3. **Simpson's Rule**: For four-times differentiable integrands, the error scales as $\mathcal{O}(1 / k^4) = \mathcal{O}(n^{-4/d})$.

### 2. The Dimensionality Transition Point
Notice the critical mathematical contrast:
- **Deterministic Quadrature**: Error $= \mathcal{O}(n^{-r / d})$, where $r$ is the algebraic order of the quadrature method. The convergence rate **degrades exponentially as dimension $d$ grows**!
- **Monte Carlo Integration**: Error $= \mathcal{O}(n^{-1/2})$, completely **independent of the dimension $d$**!

We equate the convergence exponents:
$$\frac{r}{d} = \frac{1}{2} \implies d = 2r$$
- For the Trapezoidal rule ($r = 2$):
  - In $d = 1$: Quadrature achieves $\mathcal{O}(n^{-2})$, far faster than Monte Carlo $\mathcal{O}(n^{-1/2})$.
  - In $d = 4$: Quadrature achieves $\mathcal{O}(n^{-2/4}) = \mathcal{O}(n^{-1/2})$, breaking even with Monte Carlo.
  - In $d = 10$: Quadrature achieves $\mathcal{O}(n^{-0.20})$, while Monte Carlo maintains $\mathcal{O}(n^{-0.50})$.
  - In $d = 100$: Quadrature achieves $\mathcal{O}(n^{-0.02})$, requiring $10^{100}$ evaluations for two digits of precision, whereas Monte Carlo requires $10^4$ evaluations for the exact same accuracy!

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Dimension ($d$)</th>
<th>Midpoint Rule ($r=1$)</th>
<th>Trapezoidal Rule ($r=2$)</th>
<th>Simpson's Rule ($r=4$)</th>
<th>Monte Carlo (Any $d$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$d = 1$</td>
<td>$\mathcal{O}(n^{-1.0})$</td>
<td>$\mathcal{O}(n^{-2.0})$</td>
<td>$\mathcal{O}(n^{-4.0})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d = 2$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
<td>$\mathcal{O}(n^{-1.0})$</td>
<td>$\mathcal{O}(n^{-2.0})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d = 4$</td>
<td>$\mathcal{O}(n^{-0.25})$</td>
<td>$\mathcal{O}(n^{-0.50})$</td>
<td>$\mathcal{O}(n^{-1.0})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d = 8$</td>
<td>$\mathcal{O}(n^{-0.125})$</td>
<td>$\mathcal{O}(n^{-0.25})$</td>
<td>$\mathcal{O}(n^{-0.50})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d \ge 10$</td>
<td>Hopeless ($\mathcal{O}(n^{-0.10})$)</td>
<td>Hopeless ($\mathcal{O}(n^{-0.20})$)</td>
<td>Slow ($\mathcal{O}(n^{-0.40})$)</td>
<td><strong>Robust: $\mathcal{O}(n^{-0.5})$</strong></td>
</tr>
</tbody>
</table>
</div>

Monte Carlo integration is the only computationally tractable method for multidimensional problems when $d \ge 8$.

## 4.4 Sample Size Determination and Computational Budgeting

A central question in experimental simulation design is: **how many Monte Carlo samples $n$ must be drawn to guarantee that the estimate $\hat{\theta}_n$ lies within a prescribed margin of error $\epsilon$ with high probability?**

### 1. Absolute Error Bound
Let the researcher demand that the absolute error does not exceed $\epsilon > 0$ with confidence $1 - \alpha$:
$$P(|\hat{\theta}_n - \theta| \le \epsilon) \ge 1 - \alpha$$
Under the asymptotic normal approximation:
$$z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}} \le \epsilon \implies \sqrt{n} \ge \frac{z_{1 - \alpha/2} \sigma}{\epsilon}$$
Squaring both sides yields the minimum sample size:

$$n \ge \left( \frac{z_{1 - \alpha/2} \cdot \sigma}{\epsilon} \right)^2$$

*Key Observation*: To gain one additional decimal digit of precision (reducing $\epsilon$ by a factor of 10), the required sample size $n$ must increase by a factor of **100** ($10^2$).

### 2. Relative Error Bound
When the magnitude of $\theta$ is unknown or very small (e.g., simulating rare failure events in structural safety where $\theta = 10^{-6}$), an absolute error bound is meaningless. The researcher specifies a **relative precision error** $\epsilon_r \in (0, 1)$:
$$P\left( \left| \frac{\hat{\theta}_n - \theta}{\theta} \right| \le \epsilon_r \right) \ge 1 - \alpha$$
The relative standard error requirement is:
$$z_{1 - \alpha/2} \frac{\sigma / \sqrt{n}}{\theta} \le \epsilon_r \implies n \ge \left( \frac{z_{1 - \alpha/2}}{\epsilon_r} \right)^2 \left( \frac{\sigma}{\theta} \right)^2$$
The ratio $CV = \sigma / \theta$ is the **Coefficient of Variation** of the summand $h(\mathbf{X})$.

For a rare-event probability $\theta = P(X \in \mathcal{E})$ estimated via indicator variables $h(\mathbf{X}) = I(\mathbf{X} \in \mathcal{E})$:
$$\sigma^2 = \theta(1 - \theta) \approx \theta \quad \text{for small } \theta$$
$$\left( \frac{\sigma}{\theta} \right)^2 = \frac{\theta(1 - \theta)}{\theta^2} = \frac{1 - \theta}{\theta} \approx \frac{1}{\theta}$$
The required sample size is:
$$n \ge \left( \frac{z_{1 - \alpha/2}}{\epsilon_r} \right)^2 \frac{1}{\theta}$$
If $\theta = 10^{-5}$ and the researcher desires a $10\%$ relative error ($\epsilon_r = 0.10$) at $95\%$ confidence ($z \approx 1.96$):
$$n \ge \left( \frac{1.96}{0.10} \right)^2 \times 10^5 \approx 384.16 \times 10^5 \approx 38.4 \text{ million simulations!}$$
Crude Monte Carlo becomes computationally inefficient for rare-event estimation, necessitating advanced variance reduction techniques (such as Importance Sampling).

## Fully worked question 1: Monte Carlo Integration of a Gaussian Tail Probability

### Question
An environmental safety regulator must compute the extreme upper-tail probability:
$$\theta = P(Z > 3.0) = \frac{1}{\sqrt{2\pi}} \int_3^\infty e^{-x^2/2}\,dx$$
for a standard Gaussian pollutant concentration index $Z \sim \mathcal{N}(0, 1)$.
1. Formulate a Crude Monte Carlo estimator $\hat{\theta}_n$ based on $n$ independent standard normal draws $Z_1, \dots, Z_n$.
2. In a preliminary simulation of $n = 10,000$ draws, exactly 14 draws exceed 3.0.
   - Compute the point estimate $\hat{\theta}$.
   - Compute the sample standard error $\text{SE}(\hat{\theta})$.
   - Construct the asymptotic $95\%$ confidence interval for $\theta$.
3. Compute the required sample size $n^*$ to achieve a relative error of $\epsilon_r = 0.05$ ($5\%$) at $95\%$ confidence.

### Solution, step 1: Formulation of the Crude Monte Carlo Estimator
The target probability is an expectation:
$$\theta = \mathbb{E}[I(Z > 3.0)]$$
where $I(A)$ is the indicator function of event $A$.
The Crude Monte Carlo estimator is the empirical proportion of draws exceeding 3.0:
$$\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^n I(Z_i > 3.0)$$
Since $I(Z_i > 3.0)$ is a Bernoulli random variable with parameter $\theta$:
$$\mathbb{E}[\hat{\theta}_n] = \theta, \quad \mathrm{Var}(\hat{\theta}_n) = \frac{\theta(1 - \theta)}{n}$$

### Solution, step 2: Numerical Point Estimate, Standard Error, and 95% CI
Given $n = 10,000$ and $\sum I(Z_i > 3.0) = 14$:
1. **Point Estimate**:
   $$\hat{\theta} = \frac{14}{10,000} = 0.00140 \quad (1.40 \times 10^{-3})$$
   (The exact theoretical value from standard normal tables is $1 - \Phi(3.0) \approx 0.0013499$).

2. **Sample Standard Error**:
   $$\hat{\sigma}^2 = \hat{\theta}(1 - \hat{\theta}) = 0.00140 \times (1 - 0.00140) = 0.00140 \times 0.99860 \approx 0.00139804$$
   $$\text{SE}(\hat{\theta}) = \sqrt{\frac{\hat{\sigma}^2}{n}} = \sqrt{\frac{0.00139804}{10,000}} = \sqrt{1.39804 \times 10^{-7}} \approx 0.0003739 \approx 3.74 \times 10^{-4}$$

3. **Asymptotic 95% Confidence Interval**:
   Using $z_{0.975} = 1.960$:
   $$\text{Margin of Error} = 1.960 \times \text{SE}(\hat{\theta}) = 1.960 \times 0.0003739 \approx 0.0007328$$
   $$\mathcal{CI}_{0.95} = [0.00140 - 0.000733, \; 0.00140 + 0.000733] = [0.000667, \; 0.002133]$$
   Notice the wide uncertainty relative to the estimate: the margin of error is more than $50\%$ of the point estimate!

### Solution, step 3: Sample Size Determination for 5% Relative Error
We require:
$$\frac{z_{0.975} \cdot \text{SE}}{\theta} \le 0.05 \implies n^* \ge \left( \frac{1.960}{0.05} \right)^2 \left( \frac{1 - \theta}{\theta} \right)$$
Using the estimate $\hat{\theta} = 0.00135$:
$$\frac{1.960}{0.05} = 39.2 \implies 39.2^2 = 1,536.64$$
$$\frac{1 - \theta}{\theta} \approx \frac{1 - 0.00135}{0.00135} = \frac{0.99865}{0.00135} \approx 739.74$$
Multiplying:
$$n^* \ge 1,536.64 \times 739.74 \approx 1,136,714$$
*Conclusion*: Achieving $5\%$ relative precision on this tail probability requires over **1.14 million** independent Monte Carlo simulation draws.

## Fully worked question 2: Multidimensional Monte Carlo Volume Estimation

### Question
A mathematical physicist calculates the hypervolume $V_{10}$ of a 10-dimensional unit hypersphere:
$$S_{10} = \left\{ \mathbf{x} = (x_1, \dots, x_{10})^T \in \mathbb{R}^{10} : \sum_{j=1}^{10} x_j^2 \le 1 \right\}$$
The hypersphere is embedded inside the 10-dimensional hypercube $\mathcal{C}_{10} = [-1, 1]^{10}$ with volume $V_{\text{cube}} = 2^{10} = 1,024$.
1. In a Monte Carlo experiment, $n = 100,000$ points are drawn uniformly at random from $\mathcal{C}_{10}$. Exactly 249 points fall inside the hypersphere ($\sum x_j^2 \le 1$).
   - Estimate the hypervolume $\hat{V}_{10}$.
   - Compute the standard error of the hypervolume estimate.
   - Construct the $95\%$ confidence interval.
2. The exact analytical hypervolume of a $d$-dimensional sphere of radius $R = 1$ is:
   $$V_d = \frac{\pi^{d/2}}{\Gamma(d/2 + 1)}$$
   Compute the exact analytical value for $d = 10$ and evaluate the estimation error.

### Solution, step 1: Monte Carlo Volume Estimation and Standard Error
Let $\mathbf{U}_i \sim \mathcal{U}([-1, 1]^{10})$ be uniformly distributed on the hypercube of volume $V_{\text{cube}} = 1,024$.
The indicator function is:
$$I_i = I\left( \sum_{j=1}^{10} U_{ij}^2 \le 1 \right)$$
The proportion of points falling inside the hypersphere is:
$$\hat{p} = \frac{\sum_{i=1}^n I_i}{n} = \frac{249}{100,000} = 0.00249$$

1. **Volume Estimate**:
   $$\hat{V}_{10} = V_{\text{cube}} \cdot \hat{p} = 1,024 \times 0.00249 = 2.54976 \approx 2.550$$

2. **Standard Error of $\hat{V}_{10}$**:
   The variance of $\hat{p}$ is $\frac{p(1 - p)}{n}$:
   $$\mathrm{Var}(\hat{p}) = \frac{0.00249 \times (1 - 0.00249)}{100,000} = \frac{0.00249 \times 0.99751}{100,000} \approx 2.4838 \times 10^{-8}$$
   $$\text{SE}(\hat{p}) = \sqrt{2.4838 \times 10^{-8}} \approx 0.0001576$$
   The standard error of the volume estimate is:
   $$\text{SE}(\hat{V}_{10}) = V_{\text{cube}} \cdot \text{SE}(\hat{p}) = 1,024 \times 0.0001576 \approx 0.16138 \approx 0.161$$

3. **95% Confidence Interval for $\hat{V}_{10}$**:
   $$\text{Margin of Error} = 1.960 \times 0.16138 \approx 0.3163$$
   $$\mathcal{CI}_{0.95} = [2.5498 - 0.3163, \; 2.5498 + 0.3163] = [2.2335, \; 2.8661]$$

### Solution, step 2: Exact Analytical Volume Comparison
For $d = 10$:
- $d / 2 = 5$.
- $\Gamma(d/2 + 1) = \Gamma(6) = 5! = 120$.
- $\pi^{d/2} = \pi^5 \approx 3.14159265^5 \approx 306.01968$.

The exact theoretical hypervolume is:
$$V_{10} = \frac{\pi^5}{5!} = \frac{306.01968}{120} \approx 2.550164$$

Comparing the Monte Carlo estimate with the analytical truth:
$$\text{Estimate} = 2.54976, \quad \text{True} = 2.55016$$
$$\text{Absolute Error} = |2.54976 - 2.55016| = 0.00040$$
$$\text{Relative Error} = \frac{0.00040}{2.55016} \approx 0.016\%$$
The exact volume lies comfortably within the $95\%$ confidence interval $[2.2335, 2.8661]$, confirming the precision of the multidimensional Monte Carlo approach.

## Fully worked question 3: Evaluating Integrals with Singularities via Variable Transformation

### Question
An econometrician models continuous income polarization by evaluating the definite integral:
$$\theta = \int_0^1 \frac{e^x}{\sqrt{x}}\,dx$$
1. Explain why direct crude Monte Carlo sampling using $U \sim \mathcal{U}(0, 1)$ encounters severe variance inflation at the lower boundary $x \to 0^+$.
2. Apply the change-of-variable transformation $x = y^2$ to eliminate the algebraic singularity.
3. Formulate the transformed Monte Carlo estimator and prove that its variance is strictly finite and substantially smaller than the untransformed estimator.

### Solution, step 1: Analysis of the Singularity in the Untransformed Estimator
Under direct crude Monte Carlo, let $U \sim \mathcal{U}(0, 1)$:
$$h(u) = \frac{e^u}{\sqrt{u}}$$
The estimator is $\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^n \frac{e^{U_i}}{\sqrt{U_i}}$.
We examine the second moment of the integrand:
$$\mathbb{E}[h(U)^2] = \int_0^1 \left( \frac{e^u}{\sqrt{u}} \right)^2 du = \int_0^1 \frac{e^{2u}}{u}\,du$$
Since $e^{2u} \ge 1$ for all $u \ge 0$:
$$\int_0^1 \frac{e^{2u}}{u}\,du \ge \int_0^1 \frac{1}{u}\,du = [\ln u]_0^1 = 0 - (-\infty) = \infty$$
The second moment is **infinite** ($\mathbb{E}[h(U)^2] = \infty$), which implies that:
$$\mathrm{Var}(h(U)) = \infty$$
Because the variance is infinite, the Central Limit Theorem fails completely! The estimator converges at a rate far slower than $\mathcal{O}(n^{-1/2})$, producing extreme outliers whenever a draw falls close to 0.

### Solution, step 2: The Variable Transformation $x = y^2$
Let $x = y^2 \implies dx = 2y\,dy$.
When $x = 0$, $y = 0$; when $x = 1$, $y = 1$.
Substitute into the integral:
$$\theta = \int_0^1 \frac{e^x}{\sqrt{x}}\,dx = \int_0^1 \frac{e^{y^2}}{\sqrt{y^2}} (2y\,dy) = \int_0^1 \frac{e^{y^2}}{y} (2y)\,dy = 2 \int_0^1 e^{y^2}\,dy$$
The term $y$ in the numerator and denominator cancels out completely, eliminating the algebraic singularity!

### Solution, step 3: Transformed Monte Carlo Estimator and Variance Bounding
Let $Y \sim \mathcal{U}(0, 1)$. The transformed Monte Carlo estimator is:
$$\hat{\theta}_n^* = \frac{1}{n} \sum_{i=1}^n 2 e^{Y_i^2}$$
where $Y_i \sim \mathcal{U}(0, 1)$ i.i.d.
We evaluate the boundedness of the transformed integrand $g(y) = 2 e^{y^2}$ on $[0, 1]$:
- At $y = 0$: $g(0) = 2 e^0 = 2$.
- At $y = 1$: $g(1) = 2 e^1 = 2e \approx 5.4366$.
Because $g(y)$ is strictly bounded on $[0, 1]$ ($2 \le g(y) \le 2e$):
$$\mathrm{Var}(g(Y)) = \int_0^1 (2 e^{y^2})^2 dy - \theta^2 = 4 \int_0^1 e^{2y^2} dy - \theta^2 < 4 e^2 - \theta^2 < \infty$$
By the bounded range property, the variance cannot exceed:
$$\mathrm{Var}(g(Y)) \le \frac{(2e - 2)^2}{4} = (e - 1)^2 \approx (1.718)^2 \approx 2.95$$
The transformed estimator has finite, well-behaved variance and satisfies the Central Limit Theorem with standard $\mathcal{O}(n^{-1/2})$ convergence, transforming an intractable numerical problem into a stable simulation.
"""

(DRAFT_DIR / "unit-4.md").write_text(u4.strip() + "\n", encoding="utf-8")
print("Unit 4 generated.")
