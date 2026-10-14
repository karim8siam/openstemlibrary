# tooling/add-depth-unit-2-3.py
import re

unit2_content = r"""

---

## Inverse Sampling (Negative Hypergeometric Sampling) for Rare Attributes

In conventional simple random sampling without replacement (SRSWOR), the total sample size $n$ is fixed in advance, and the number of sample units $m$ possessing a rare attribute of interest (e.g. individuals infected with an emergent pathogen, businesses committing tax fraud, or rare ecological species) is a stochastic random variable. When the true population proportion $P = M / N$ is very small (for example, $P < 0.01$ or $P < 0.001$), standard fixed-sample designs suffer from a severe risk of zero-event realizations: with high probability, the realized sample may contain zero or only one positive event ($m \le 1$). In such circumstances, the standard sample proportion $\hat{P} = m / n$ has unacceptable relative error, and the sample variance estimator $s^2 / n$ collapses, preventing the construction of meaningful confidence intervals.

To resolve the catastrophic fragility of fixed-sample designs in rare-event settings, J. B. S. Haldane (1945) and D. J. Finney (1949) formulated **Inverse Sampling** (also known as Negative Hypergeometric Sampling).

### The Inverse Sampling Protocol
Instead of fixing the sample size $n$, the survey investigator predetermines a fixed target integer $m \ge 2$ of units possessing the rare attribute. Sampling proceeds sequentially without replacement, unit by unit, until exactly $m$ units possessing the rare attribute are uncovered. 

Under this protocol:
1. The number of positive units observed, $m$, is a fixed deterministic constant.
2. The total number of units sampled, $n$, is a random variable taking integer values in the range $\{m, m + 1, \dots, N - M + m\}$.

### The Negative Hypergeometric Probability Distribution
Let $M$ denote the unknown total number of units in the population possessing the rare attribute, and $N$ denote the known total population size. Sampling terminates at step $n$ if and only if:
1. Exactly $m - 1$ positive units were observed in the first $n - 1$ draws.
2. The $n$-th drawn unit possesses the rare attribute.

Under simple random sampling without replacement, the probability mass function of the stopping sample size $n$ is governed by the **Negative Hypergeometric Distribution**:
$$P(n \mid M, N, m) = \frac{\binom{M}{m - 1} \binom{N - M}{(n - 1) - (m - 1)}}{\binom{N}{n - 1}} \times \frac{M - (m - 1)}{N - (n - 1)}$$

Using combinatorial identities, this probability mass function simplifies to:
$$P(n \mid M, N, m) = \frac{\binom{n - 1}{m - 1} \binom{N - n}{M - m}}{\binom{N}{M}}$$

### Unbiased Estimation of the Population Proportion: Haldane's Estimator
In a naive attempt to estimate the proportion $P = M / N$, one might consider the empirical sample fraction:
$$\tilde{P} = \frac{m}{n}$$
However, because $n$ appears in the denominator and is stochastic, Jensen's inequality implies:
$$E\left( \frac{m}{n} \right) > \frac{m}{E(n)} \approx P$$
The naive estimator $m / n$ is systematically positively biased for the true proportion!

To eliminate this bias, Haldane (1945) derived the unique uniformly minimum-variance unbiased estimator (UMVUE) of the population proportion $P = M / N$:
$$\hat{P}_{inv} = \frac{m - 1}{n - 1}$$

#### Mathematical Proof of Strict Unbiasedness:
We evaluate the expectation of $\hat{P}_{inv}$ over all possible values of $n$:
$$E(\hat{P}_{inv}) = \sum_{n=m}^{N - M + m} \left( \frac{m - 1}{n - 1} \right) P(n \mid M, N, m)$$
$$= \sum_{n=m}^{N - M + m} \left( \frac{m - 1}{n - 1} \right) \frac{\binom{n - 1}{m - 1} \binom{N - n}{M - m}}{\binom{N}{M}}$$

Notice the cancellation between the algebraic factor and the binomial coefficient:
$$\frac{m - 1}{n - 1} \binom{n - 1}{m - 1} = \frac{m - 1}{n - 1} \frac{(n - 1)!}{(m - 1)! (n - m)!} = \frac{(n - 2)!}{(m - 2)! (n - m)!} = \binom{n - 2}{m - 2}$$

Substitute this back into the expectation sum:
$$E(\hat{P}_{inv}) = \frac{1}{\binom{N}{M}} \sum_{n=m}^{N - M + m} \binom{n - 2}{m - 2} \binom{N - n}{M - m}$$

Change index of summation by setting $k = n - 1$. As $n$ ranges from $m$ to $N - M + m$, $k$ ranges from $m - 1$ to $N - M + m - 1$:
$$\sum_{k=m - 1}^{N - M + m - 1} \binom{k - 1}{(m - 1) - 1} \binom{(N - 1) - k}{(M - 1) - (m - 1)} = \binom{N - 1}{M - 1}$$
by the classical Vandermonde convolution identity.

Therefore:
$$E(\hat{P}_{inv}) = \frac{\binom{N - 1}{M - 1}}{\binom{N}{M}} = \frac{\frac{(N - 1)!}{(M - 1)! (N - M)!}}{\frac{N!}{M! (N - M)!}} = \frac{M}{N} = P$$
This proves that Haldane's estimator $\hat{P}_{inv} = \frac{m - 1}{n - 1}$ is strictly design-unbiased for any finite population size $N$ and any target count $m \ge 2$.

### Unbiased Estimation of the Sampling Variance
Finney (1949) demonstrated that the exact sampling variance of $\hat{P}_{inv}$ is:
$$V(\hat{P}_{inv}) = \frac{P (1 - P)}{E(n - 1)} \left( 1 - \frac{E(n)}{N} \right) \approx \frac{P^2 (1 - P)}{m - 1} \left( 1 - \frac{m}{N P} \right)$$

Because the true proportion $P$ is unknown, Finney derived the strictly unbiased sample estimator of variance:
$$\hat{V}(\hat{P}_{inv}) = \frac{\hat{P}_{inv} (1 - \hat{P}_{inv})}{n - 2} \left( 1 - \frac{n - 1}{N} \right) = \frac{\left( \frac{m - 1}{n - 1} \right) \left( 1 - \frac{m - 1}{n - 1} \right)}{n - 2} \left( \frac{N - n + 1}{N} \right)$$

This variance estimator is strictly non-negative and requires only that the target quota satisfies $m \ge 3$.

### Practical Synthesis and Quality Guidance
Inverse sampling provides an invaluable safeguard for public health monitoring and industrial quality inspection:
1. **Guaranteed Precision**: The coefficient of variation of the estimate is governed entirely by the predetermined choice of $m$:
   $$\text{CV}(\hat{P}_{inv}) \approx \frac{1}{\sqrt{m - 1}}$$
   If the investigator desires a coefficient of variation of $20\%$, setting $m = 26$ guarantees $\text{CV} \approx 1/\sqrt{25} = 0.20$, regardless of how rare the attribute is in the population.
2. **Budget Monitoring**: Because the sample size $n$ is stochastic, the field budget cannot be strictly predicted in advance. The expected sample size is $E(n) \approx m / P$. To avoid budget overruns when $P$ is far lower than hypothesized, agencies typically institute a truncation cap $n_{max}$: if $m$ positive cases are not encountered by draw $n_{max}$, sampling terminates, and truncated Bayesian models are deployed.
"""

unit3_content = r"""

---

## The Lavallée–Hidiroglou (L-H) Stratification Algorithm for Skewed Business Populations

A pervasive challenge in national economic statistics—including annual manufacturing censuses, retail trade inquiries, and financial service audits—is that business populations are **extraordinarily skewed**. In almost every industrial sector, the Pareto principle holds with extreme force: a tiny fraction of mega-corporations (less than $1\%$ to $5\%$ of enterprises) accounts for more than $70\%$ to $80\%$ of total national revenue, capital investment, and employment, while hundreds of thousands of small artisan workshops and sole proprietorships make up the remaining long tail.

If classical equal-allocation or simple proportional stratified sampling is applied to such skewed populations, the resulting estimates suffer from massive variance. Even the Dalenius–Hodges cumulative square-root rule struggles because it assumes continuous variables and does not isolate the extreme right-hand outliers into a dedicated certainty stratum.

To resolve this economic reality, Pierre Lavallée and Michael A. Hidiroglou (1988) formulated the **Lavallée–Hidiroglou (L-H) Stratification Algorithm**, which has become the official international standard deployed by Statistics Canada, Eurostat, and the U.S. Census Bureau for enterprise surveys.

### Architecture of the L-H Stratification Framework
Let $N$ denote the total number of enterprises in the business register, sorted in ascending order of an auxiliary measure of size $x$ (such as annual gross turnover or tax register payroll):
$$x_{(1)} \le x_{(2)} \le \dots \le x_{(N)}$$

The population is partitioned into $L$ non-overlapping strata defined by boundary cutoffs:
$$b_0 < b_1 < b_2 < \dots < b_{L-1} < b_L$$
where $b_0 = x_{(1)}$ and $b_L = x_{(N)}$.

The L-H architecture divides the strata into two fundamentally distinct operational regimes:
1. **Take-Some Strata ($h = 1, 2, \dots, L - 1$)**: The first $L - 1$ strata contain small and medium enterprises. A probability sample of size $n_h < N_h$ is selected from stratum $h$ using SRSWOR.
2. **Take-All (Certainty) Stratum ($h = L$)**: The top stratum contains the largest mega-enterprises whose size exceeds the critical threshold $b_{L-1}$ ($x_i \ge b_{L-1}$). In this stratum, **every single enterprise is sampled with certainty**:
   $$n_L = N_L \implies f_L = \frac{n_L}{N_L} = 1.0$$
   Because all units in the take-all stratum are observed, its sampling variance is identically zero:
   $$V(\hat{Y}_L) = N_L^2 \left( \frac{1 - f_L}{n_L} \right) S_L^2 = N_L^2 (0) S_L^2 = 0$$

### Optimization Formulation and Objective Function
The goal of the L-H algorithm is to determine the stratum boundary vector $\mathbf{b} = (b_1, b_2, \dots, b_{L-1})^\top$ and sample allocations $n_h$ that **minimize the total survey sample size $n$**:
$$\min_{\mathbf{b}, \{n_h\}} n = N_L + \sum_{h=1}^{L-1} n_h$$
subject to the regulatory constraint that the coefficient of variation ($\text{CV}$) of the estimated national total $\hat{Y} = \sum_{h=1}^L \hat{Y}_h$ does not exceed a prescribed precision threshold $c$ (typically $c = 0.05$ or $5\%$):
$$\text{CV}(\hat{Y}) = \frac{\sqrt{V(\hat{Y})}}{Y} \le c \implies V(\hat{Y}) \le c^2 Y^2$$

Because the take-all stratum contributes zero variance, the total sampling variance is:
$$V(\hat{Y}) = \sum_{h=1}^{L-1} N_h^2 \left( \frac{1 - f_h}{n_h} \right) S_h^2 = \sum_{h=1}^{L-1} \frac{N_h^2 S_h^2}{n_h} - \sum_{h=1}^{L-1} N_h S_h^2$$

Assuming Neyman optimal allocation across the $L - 1$ take-some strata, the required sample size in stratum $h$ ($h = 1, \dots, L - 1$) is:
$$n_h = (n - N_L) \frac{N_h S_h}{\sum_{k=1}^{L-1} N_k S_k}$$

Substituting $n_h$ into the variance constraint and solving for the required take-some sample size $(n - N_L)$ yields:
$$n - N_L = \frac{\left( \sum_{h=1}^{L-1} N_h S_h \right)^2}{c^2 Y^2 + \sum_{h=1}^{L-1} N_h S_h^2}$$

Therefore, the total sample size $n(\mathbf{b})$ as a function of the boundary vector $\mathbf{b}$ is:
$$n(\mathbf{b}) = N_L(\mathbf{b}) + \frac{\left( \sum_{h=1}^{L-1} N_h(\mathbf{b}) S_h(\mathbf{b}) \right)^2}{c^2 Y^2 + \sum_{h=1}^{L-1} N_h(\mathbf{b}) S_h^2(\mathbf{b})}$$

### Sethi's Differential Equations and Iterative Solution
To minimize $n(\mathbf{b})$ with respect to the cutoff boundaries, Lavallée and Hidiroglou differentiated $n(\mathbf{b})$ with respect to $b_h$, adapting V. K. Sethi's (1963) boundary formulation.
Setting $\frac{\partial n}{\partial b_h} = 0$ yields a system of non-linear equations for the optimal boundaries:
$$b_h = \frac{\bar{Y}_h + \bar{Y}_{h+1}}{2} + \left( \frac{S_{h+1}^2 - S_h^2}{2 (\bar{Y}_{h+1} - \bar{Y}_h)} \right) \quad (h = 1, \dots, L-2)$$

For the take-all boundary $b_{L-1}$ separating the medium take-some enterprises from the certainty mega-enterprises, the stationarity condition yields:
$$b_{L-1} = \bar{Y}_{L-1} + \frac{S_{L-1}^2}{\bar{Y}_L - \bar{Y}_{L-1}} \left[ 1 + \frac{c^2 Y^2 + \sum_{k=1}^{L-1} N_k S_k^2}{\left( \sum_{k=1}^{L-1} N_k S_k \right)^2} \right]$$

Because the stratum parameters ($N_h, \bar{Y}_h, S_h^2$) depend on the unknown boundaries $b_h$, this system cannot be solved in closed form. The L-H algorithm executes an **iterative numerical fixed-point algorithm**:
1. **Initialization**: Set initial boundaries $b_h^{(0)}$ using the Dalenius–Hodges cumulative $\sqrt{f}$ rule on the auxiliary variable $x$.
2. **Evaluation**: Given boundaries $b_h^{(t)}$, assign all population units into strata $1, \dots, L$. Calculate the stratum counts $N_h^{(t)}$, means $\bar{X}_h^{(t)}$, and variances $S_{xh}^{2(t)}$.
3. **Updating**: Compute updated boundaries $b_h^{(t+1)}$ by evaluating Sethi's equations using the current stratum moments.
4. **Convergence Check**: Repeat steps 2 and 3 until the boundaries stabilize:
   $$\max_{1 \le h \le L-1} \left| b_h^{(t+1)} - b_h^{(t)} \right| < \epsilon$$
   where $\epsilon$ is a predefined numerical tolerance (typically $10^{-4}$).

### Why the L-H Algorithm Revolutionized Official Economic Statistics:
1. **Total Elimination of Extreme Outlier Variance**: By isolating the largest $1\%$ to $3\%$ of enterprises into the take-all stratum, the sampling variance of the top tier is reduced to exactly zero.
2. **Minimal Operational Cost**: In empirical applications at national statistical offices, the L-H algorithm routinely reduces the required national sample size by **$40\%$ to $60\%$** compared to standard unstratified or proportionally stratified sampling for the exact same target precision ($\text{CV} \le 5\%$).
3. **Zero Risk of Mega-Enterprise Non-Coverage**: No multi-billion-dollar enterprise can be omitted by bad sampling luck, ensuring that published macroeconomic aggregates remain completely stable and defensible over time.
"""

filepath2 = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-2.md'
with open(filepath2, 'r', encoding='utf-8') as f:
    text2 = f.read()

split2 = '## Practical Synthesis, Quality Diagnostics and Computational Verification'
if split2 in text2:
    parts = text2.split(split2)
    new2 = parts[0] + unit2_content + '\n---\n\n## Practical Synthesis, Quality Diagnostics and Computational Verification' + parts[1]
    with open(filepath2, 'w', encoding='utf-8') as f:
        f.write(new2)
    print("SUCCESSFULLY EXPANDED UNIT 2!")
else:
    print("Unit 2 split phrase not found!")

filepath3 = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-3.md'
with open(filepath3, 'r', encoding='utf-8') as f:
    text3 = f.read()

split3 = '## Practical Synthesis, Quality Diagnostics and Computational Verification'
if split3 in text3:
    parts = text3.split(split3)
    new3 = parts[0] + unit3_content + '\n---\n\n## Practical Synthesis, Quality Diagnostics and Computational Verification' + parts[1]
    with open(filepath3, 'w', encoding='utf-8') as f:
        f.write(new3)
    print("SUCCESSFULLY EXPANDED UNIT 3!")
else:
    print("Unit 3 split phrase not found!")
