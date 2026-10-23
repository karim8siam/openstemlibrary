# Unit 1: Uniform Random Number Generation & Pseudorandom Foundations

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


## 1.10 Theoretical Foundations of Pseudo-Randomness and Algorithmic Information

In rigorous mathematical statistics, the concept of randomness cannot be satisfactorily defined by purely empirical observations. A deterministic computer executing finite instruction sequences cannot produce genuine ontological indeterminacy. Instead, computational statistics relies on algorithmic information theory, developed independently by Andrey Kolmogorov, Ray Solomonoff, and Gregory Chaitin, to formalize what distinguishes an effectively random sequence from a patterned sequence.

### 1. Kolmogorov Complexity and Incompressibility
Let $s$ be a finite binary string of length $m$, denoted $s \in \{0, 1\}^m$. The Kolmogorov complexity $K_U(s)$ with respect to a universal Turing machine $U$ is defined as the length of the shortest computer program $p$ that, when executed on $U$, halts and outputs the exact string $s$:

$$K_U(s) = \min_{p} \{ |p| : U(p) = s \}$$

A sequence $s$ of length $m$ is defined to be algorithmically incompressible, or Kolmogorov random, if its descriptive complexity is approximately equal to its length:

$$K_U(s) \ge m - c$$

where $c$ is a small universal constant independent of $m$. If a sequence can be produced by a program significantly shorter than its own length, the sequence contains structural redundancies and deterministic patterns. 

By definition, any pseudo-random number generator (PRNG) initialized with an $s$-bit seed and generating an $m$-bit sequence (where $m \gg s$) produces output whose Kolmogorov complexity is bounded by $K_U(s) \le |seed| + O(1) \ll m$. Therefore, PRNG streams are completely compressible and fail algorithmic randomness in the Kolmogorov sense. What makes them statistically viable is computational indistinguishability: no polynomial-time statistical test $T$ can distinguish the output of a cryptographic-grade PRNG from a truly uniform random sequence with non-negligible advantage.

### 2. Martin-Löf Randomness and Statistical Tests
Per Martin-Löf resolved the question of randomness for infinite sequences $\mathbf{x} = (x_1, x_2, \dots) \in \{0, 1\}^\infty$ using effective measure theory. An effective null set is an intersection of a nested sequence of open sets whose Lebesgue measure decreases computably to zero. An infinite sequence is Martin-Löf random if it does not belong to any effective null set.

In statistical practice, every goodness-of-fit test, serial correlation test, or spectral lattice analysis constitutes a computable statistical hypothesis test corresponding to an effective null set. If a PRNG possesses a structural flaw, it systematically falls into the rejection region of a specific computable null set, demonstrating non-randomness.

## 1.11 Multi-Stream Random Number Generation and Parallel Architectures

Modern high-performance statistical computing operates on massively parallel multi-core central processing units (CPUs) and graphics processing units (GPUs) capable of executing tens of thousands of concurrent simulation threads. In such distributed architectures, utilizing a single shared sequential PRNG is impossible due to memory lock contention and race conditions. Furthermore, naively seeding parallel threads with sequential integers (such as thread ID $k = 0, 1, 2, \dots$) causes catastrophic inter-stream correlations, known as seed clustering.

### 1. The Block Splitting and Leapfrog Methods
Two classical strategies for distributing a single linear congruential or recurrence-based generator across $P$ parallel worker threads are:

1. **Block Splitting (Skip-Ahead)**: The total sequence length $M$ is partitioned into $P$ non-overlapping blocks of length $L = \lfloor M/P \rfloor$. Worker $p$ (for $p = 0, \dots, P-1$) is assigned the subsequence starting at state $x_{pL}$. To implement block splitting efficiently without computing $L$ sequential iterations, the state transition matrix $A$ is raised to the power $L$ using binary exponentiation (repeated squaring):
$$x_{pL} = A^L x_0 \pmod m$$
Because matrix multiplication modulo $m$ requires only $O(k^3 \log_2 L)$ operations for a state of dimension $k$, the jump-ahead step executes in microseconds even for $L = 10^{15}$.

2. **Leapfrogging (Interleaving)**: Instead of contiguous blocks, worker $p$ consumes every $P$-th element of the sequence, starting from index $p$:
$$x_{p + jP} = A^{jP} x_p \pmod m$$
The primary drawback of leapfrogging in high-dimensional simulations is that spatial and serial correlations in the base generator become cross-thread correlations, causing synchronized biases across parallel Monte Carlo estimates.

### 2. Counter-Based Pseudo-Random Number Generators
For modern GPU acceleration, the recurrence-based paradigm (where state $x_{n+1} = f(x_n)$ must be stored and updated in thread-local registers) has been superseded by Counter-Based PRNGs (CBPRNGs), pioneered by John K. Salmon, Mark A. Moraes, Ron O. Dror, and David E. Shaw (2011).

In a CBPRNG, the $n$-th pseudo-random variate is computed by evaluating a stateless, highly non-linear cryptographic permutation function $F$ parameterized by a key $K$ and a counter $C$:

$$R_n = F_K(n)$$

Prominent counter-based generators include:
- **Philox**: Employs integer multiplication and Feistel-style mixing networks over 64-bit or 32-bit words (e.g., Philox4x32-10, Philox4x64-10). It provides high statistical dispersion with minimal register overhead.
- **Threefry**: A stripped-down cryptographic permutation derived from the Threefish block cipher (part of Skein, an SHA-3 finalist). It uses only XOR, addition, and word rotation (ARX operations), executing without integer multiplication instructions.

Because counter-based generators require zero inter-thread communication and allow arbitrary $O(1)$ random access to any position in a stream of length $2^{128}$ or $2^{256}$, each thread $k$ can simply evaluate $F_K(k \cdot 2^{64} + t)$ for local iteration $t$. The risk of stream overlap or inter-thread collision is mathematically infinitesimal.

## 1.12 Empirical Testing Batteries: The TestU01 Suite in Depth

Empirical statistical testing of pseudo-random number generators was revolutionized by Pierre L'Ecuyer and Richard Simard with the release of the **TestU01** library in 2007. TestU01 remains the gold standard benchmark against which all scientific PRNGs are evaluated, comprising far more rigorous batteries than the historical DIEHARD suite of George Marsaglia or the NIST SP 800-22 standard.

TestU01 organizes its batteries into three escalating levels of stringency:
- **SmallCrush**: 10 tests, evaluating roughly $1.6 \times 10^9$ random numbers in seconds.
- **Crush**: 96 tests, evaluating approximately $5 \times 10^{11}$ random numbers in roughly one hour.
- **BigCrush**: 106 tests, consuming more than $4 \times 10^{12}$ random numbers and several hours of high-precision computation.

A test is flagged as an unambiguous failure if its resulting $p$-value falls outside the extreme interval $[10^{-15}, 1 - 10^{-15}]$. The principal statistical tests implemented in TestU01 include:

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Test Name</th>
<th>Mathematical Phenomenon Tested</th>
<th>Degrees of Freedom / Statistic</th>
<th>Common Failing Generators</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Collision Test</strong></td>
<td>Frequency of duplicate values when throwing $n$ balls into $k$ urns ($n \ll k$). Deviations detect clustering.</td>
<td>Poisson approximation or normal approximation to total collision count $C$.</td>
<td>Short-period LCGs, 32-bit linear congruential engines.</td>
</tr>
<tr>
<td><strong>Birthday Spacings</strong></td>
<td>Sort $n$ random points on $[0, 1)$, compute spacings $S_i$, and count duplicate spacings.</td>
<td>Asymptotically Poisson distributed with parameter $\lambda = n^3 / (4m)$.</td>
<td>Nearly all linear congruential generators with modulus $m \le 2^{64}$.</td>
</tr>
<tr>
<td><strong>Matrix Rank Test</strong></td>
<td>Construct $n$ random binary matrices of dimension $L \times k$ and compute their algebraic ranks over $\mathbb{F}_2$.</td>
<td>Chi-square goodness-of-fit against theoretical rank probabilities under uniform distribution.</td>
<td>Lagged Fibonacci generators, subtract-with-borrow engines.</td>
</tr>
<tr>
<td><strong>Serial Over/Underflow</strong></td>
<td>Higher-order multivariate serial dependencies across $t$-dimensional hypercubes.</td>
<td>Chi-square statistic on cell occupancy counts across $d$-dimensional grid partitions.</td>
<td>Tausworthe generators with poor feedback polynomials.</td>
</tr>
<tr>
<td><strong>Weight Distrib / Hamming</strong></td>
<td>Calculates Hamming weight (number of 1-bits) in blocks of consecutive random words.</td>
<td>Binomial distribution $\mathcal{B}(B, 0.5)$ compared via chi-square test.</td>
<td>Inadequately mixed shift-register generators.</td>
</tr>
<tr>
<td><strong>Linear Complexity Test</strong></td>
<td>Applies the Berlekamp-Massey algorithm to find the shortest linear feedback shift register producing the bit sequence.</td>
<td>Jump complexity distribution around $L/2$ compared to theoretical distribution.</td>
<td>Mersenne Twister MT19937 (fails dramatically due to linear structure over $\mathbb{F}_2$).</td>
</tr>
</tbody>
</table>
</div>

The failure of the famous **Mersenne Twister (MT19937)** on the Linear Complexity tests of BigCrush underscores why modern scientific computing is transitioning toward non-linear permutations such as PCG (Permuted Congruential Generator) and Philox: while MT19937 has an astronomical period of $2^{19937} - 1$, its transition function is strictly linear over the Galois field $\mathbb{F}_2$, rendering it vulnerable to matrix-rank and linear-complexity deficiencies in high-dimensional simulations.


## 1.13 Cryptographic Randomness and Operating System Entropy Harvesting

In security-sensitive simulation applications—such as privacy-preserving synthetic data generation, cryptographic key renewal, and randomized clinical trial blinding—standard scientific PRNGs like Xoshiro256** and Mersenne Twister cannot be used. Because standard PRNGs possess linear or invertible state transitions, an adversary observing a modest sequence of outputs (e.g., 624 consecutive 32-bit integers for MT19937) can run Gaussian elimination over $\mathbb{F}_2$ to reconstruct the entire internal register state, thereby predicting all future and past outputs with $100\%$ certainty.

### 1. Cryptographically Secure Pseudo-Random Number Generators (CSPRNGs)
A pseudo-random bit generator $G: \{0, 1\}^k \to \{0, 1\}^m$ is defined to be **Cryptographically Secure (CSPRNG)** if it passes the **Next-Bit Test** (Yao 1982).
*Definition (Next-Bit Test)*: For all polynomial-time statistical algorithms $A$, and for all indices $i \in \{1, \dots, m-1\}$:
$$P\left( A(s_1, s_2, \dots, s_i) = s_{i+1} \right) \le \frac{1}{2} + \epsilon(k)$$
where $\epsilon(k)$ is a negligible function decaying faster than $k^{-c}$ for all constants $c > 0$. If no computational adversary can predict the next bit with advantage better than a fair coin flip, the generator is indistinguishable from true randomness.

Two primary classes of CSPRNGs dominate modern systems:
1. **Number-Theoretic Generators (e.g., Blum-Blum-Shub)**:
$$x_{n+1} = x_n^2 \pmod M$$
where $M = p \cdot q$ is a Blum integer (the product of two large prime numbers $p \equiv q \equiv 3 \pmod 4$). The security of BBS reduces directly to the computational hardness of the Quadratic Residuosity problem and integer factorization. While provably secure, BBS requires large multi-precision integer modular multiplications, rendering it too slow for high-throughput scientific simulations.
2. **Symmetric Keystream Generators (e.g., ChaCha20)**:
Developed by Daniel J. Bernstein, ChaCha20 operates on a $4 \times 4$ matrix of 32-bit words using twenty rounds of Addition-Rotation-XOR (ARX) operations. ChaCha20 produces pseudo-random output at speeds exceeding 3 gigabytes per second on standard hardware while resisting all known differential, linear, and algebraic cryptanalytic attacks.

### 2. Operating System Entropy Architecture
Modern operating systems supply non-deterministic randomness to statistical environments through special kernel device interfaces such as `/dev/urandom` and the `getrandom()` system call.

The kernel maintains an internal **Entropy Pool** populated by environmental hardware noise:
- Microsecond timing jitter from external physical interrupts (keyboard keystrokes, network packet arrivals, disk seek latency).
- Direct CPU hardware instructions such as Intel/AMD `RDRAND` and `RDSEED`, which measure thermal noise in on-die ring oscillators.

These asynchronous entropy inputs are processed through a cryptographic compression function (such as BLAKE2s or SHA-256) into a master pool. An internal CSPRNG (typically ChaCha20) continuously outputs pseudo-random numbers keyed by the pool. Even if the external hardware noise ceases temporarily, the cryptographic back-tracking resistance ensures that compromise of the current state reveals zero information about previous simulation realizations.


## 1.14 Hardware Random Number Generators and NIST SP 800-90 Standards

In mission-critical statistical simulations, military modeling, and regulatory lottery systems, purely algorithmic pseudo-random number generators are coupled with or verified against **True Random Number Generators (TRNGs)**. TRNGs harvest entropy from fundamental microscopic quantum or thermal physical processes that are ontologically non-deterministic according to the laws of modern physics.

### 1. Physical Entropy Harvesting Mechanisms
Hardware TRNG devices convert physical analog noise into discrete binary digits using three primary mechanisms:
1. **Thermal Johnson-Nyquist Noise**: The random thermal agitation of charge carriers inside an electrical conductor or resistor at non-zero temperature $T$. The mean-square noise voltage across bandwidth $\Delta f$ is given by:
$$\overline{v_n^2} = 4 k_B T R \, \Delta f$$
where $k_B$ is the Boltzmann constant, $T$ is absolute temperature, and $R$ is resistance. Amplifying and sampling this continuous voltage waveform produces unpredictable noise bits.
2. **Avalanche Breakdown in Zener Diodes**: Operating a reverse-biased semiconductor $p$-$n$ junction in its breakdown avalanche regime generates quantum shot noise as charge carriers multiply via impact ionization.
3. **Ring Oscillator Phase Jitter**: Linking an odd number of inverter gates in a closed loop creates an autonomous clock whose phase drifts unpredictably due to localized thermal fluctuations and transistor switching noise. By sampling a high-frequency jittery ring oscillator with a slower stable reference clock, unpredictable transition bits are captured.

### 2. Conditioning and NIST SP 800-90A/B Architecture
Raw physical noise is rarely uniformly distributed: thermal drift, ambient temperature shifts, and circuit component asymmetry introduce substantial DC bias ($P(1) \ne 0.5$) and serial autocorrelation. To transform raw physical entropy into uniform, independent random bits, raw bits must pass through a **Conditioning Component** as specified by the National Institute of Standards and Technology (NIST) Special Publication 800-90B:
- **Von Neumann De-biasing**: Takes pairs of non-overlapping raw bits $(b_1, b_2)$. If the pair is $01$, output $0$; if $10$, output $1$; if $00$ or $11$, discard the pair entirely. Because $P(01) = P(0) P(1) = P(10) = P(1) P(0)$ under independence, the output stream is guaranteed to have zero bias ($P(0) = P(1) = 0.5$), though roughly $75\%$ of raw throughput is discarded.
- **Cryptographic Hash Conditioning**: Blocks of raw physical bits are processed through cryptographic sponge functions (such as SHA-3/Keccak or AES-CBC-MAC). The compression guarantees that the min-entropy of the output is strictly bounded and distributed uniformly over $\{0, 1\}^m$.

In high-performance hybrid architectures, hardware TRNGs provide continuous asynchronous seed re-keying into user-space CSPRNG algorithms, ensuring that simulations maintain multi-gigahertz throughput with genuine physical unpredictability.


## 1.15 Historical Evolution of Computational Pseudo-Randomness

The quest for computational pseudo-randomness mirrors the evolution of modern scientific computing itself. In 1946, John von Neumann suggested the **Middle-Square Method** to generate random numbers for the Monte Carlo neutron diffusion calculations at Los Alamos National Laboratory. The algorithm squared a 4-digit number and extracted the middle 4 digits to produce the next seed:
$$x_0 = 5772156649 \implies x_0^2 = 33317792380594909201 \implies x_1 = 7923805949$$
Von Neumann famously remarked: *"Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin."* The middle-square method suffered from fatal short loops: once a sequence generated zero or certain repetitive patterns (such as $3792 \to 3792$), the sequence collapsed permanently.

In 1951, Derrick H. Lehmer introduced the linear congruential generator $x_{n+1} = a x_n \pmod m$, providing the first mathematically tractable family with provable maximal periods. Throughout the 1960s to 1980s, generators such as IBM's notorious `RANDU` ($a = 65539, m = 2^{31}$) were widely distributed, leading to millions of flawed scientific papers due to undetected hyperplanar lattice collapses.

The modern era began with Makoto Matsumoto and Takuji Nishimura (1998), who invented the **Mersenne Twister (MT19937)** based on a twisted generalized feedback shift register over $\mathbb{F}_2$ with period $2^{19937}-1$. In 2014, Melissa E. O'Neill designed the **Permuted Congruential Generator (PCG)** family, proving that applying non-linear permutation functions (such as bitwise rotations and XSH-RR operations) to linear state updates eliminates the lattice flaws of LCGs while maintaining ultra-compact state memory and multi-gigahertz speeds.


## 1.16 Computational Laboratory: Benchmarking PRNG Throughput and Lattice Detection

In professional simulation engineering, choosing a PRNG requires balancing generation throughput against spectral lattice security. In this laboratory case study, we evaluate three prominent generators: standard 32-bit Linear Congruential Generator (LCG), Mersenne Twister MT19937, and PCG64 (Permuted Congruential Generator).

When benchmarked across $10^9$ random double-precision floats on modern x86-64 hardware with AVX-512 vectorization:
- **32-bit LCG**: Executes in approximately 0.65 seconds, but fails the Marsaglia planes test when points $(U_i, U_{i+1}, U_{i+2})$ are projected into three dimensions, clustering onto only 1,600 parallel hyperplanes.
- **MT19937**: Requires 1.82 seconds and 2.5 kilobytes of internal cache state, failing the linear complexity tests of TestU01 BigCrush.
- **PCG64**: Executes in 0.58 seconds using only 128 bits of state, passing all 106 tests in BigCrush without detectable lattice defects.

Statistical practitioners must therefore retire legacy LCG and default to PCG64 or Philox for high-dimensional scientific simulations.


## 1.17 Unit 1 Review and Methodological Synthesis

In this foundational unit, we analyzed the mathematical and computational mechanics of pseudo-random number generation. We established that deterministic finite-state automata cannot produce true Kolmogorov incompressibility, but achieve statistical indistinguishability under polynomial-time tests. We analyzed the geometric failure modes of Linear Congruential Generators through Marsaglia's lattice theorem, proving that points in dimension $d$ fall onto at most $(d! m)^{1/d}$ hyperplanes. We contrasted historical LCGs and Mersenne Twister MT19937 with modern 64-bit state generators, specifically Permuted Congruential Generators (PCG) and counter-based generators (Philox and Threefry). In high-performance parallel computing, counter-based PRNGs enable stateless, communication-free random number generation with $O(1)$ random access, preventing inter-stream collisions across multi-GPU nodes. Finally, we surveyed empirical testing frameworks, demonstrating why the TestU01 BigCrush battery represents the rigorous benchmark for validating modern simulation engines.
