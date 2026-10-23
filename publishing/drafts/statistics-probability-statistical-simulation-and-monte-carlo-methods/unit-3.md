# Unit 3: Rejection Sampling & Envelope Methods

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


## 3.10 Higher-Order Asymptotic Theory of the Bootstrap and Edgeworth Expansions

In applied data analysis, practitioners frequently employ the normal-approximation bootstrap confidence interval:
$$\left[ \hat{\theta} - z_{1-\alpha/2} \cdot \widehat{\text{SE}}_{\text{boot}}, \, \hat{\theta} + z_{1-\alpha/2} \cdot \widehat{\text{SE}}_{\text{boot}} \right]$$
or the simple percentile interval $[\hat{\theta}^*_{(\alpha/2)}, \hat{\theta}^*_{(1-\alpha/2)}]$. However, rigorous theoretical statistics reveals that both of these standard intervals achieve only **first-order accuracy**: their coverage error is of order $O(n^{-1/2})$, meaning that for a nominal $95\%$ confidence interval, the true coverage probability is $0.95 \pm O(n^{-1/2})$.

Peter Hall (1992) and Bradley Efron (1987) established that the true power of bootstrap resampling emerges when studentized and adjusted using higher-order asymptotic expansions.

### 1. The Studentized Bootstrap (Bootstrap-t)
Let $\hat{\theta}$ be an estimator of parameter $\theta$, and let $\hat{\sigma}^2$ be a consistent estimator of its asymptotic variance $\mathrm{Var}(\hat{\theta})$. Consider the studentized root:
$$T = \frac{\hat{\theta} - \theta}{\hat{\sigma}}$$
Under regularity conditions, the distribution function of $T$ admits a one-term Edgeworth expansion:
$$P(T \le x) = \Phi(x) + n^{-1/2} p_1(x) \phi(x) + O(n^{-1})$$
where $\Phi(x)$ and $\phi(x)$ are the standard normal cumulative distribution and density functions, and $p_1(x)$ is an even polynomial whose coefficients depend on the skewness of the underlying population distribution:
$$p_1(x) = -\frac{1}{6} \kappa_3 (2x^2 + 1)$$
where $\kappa_3 = \mathbb{E}[(X - \mu)^3] / \sigma^3$ is the standardized skewness coefficient.

When we generate bootstrap resamples $\mathbf{x}^{*b}$, we compute the bootstrap studentized root:
$$T^{*b} = \frac{\hat{\theta}^{*b} - \hat{\theta}}{\hat{\sigma}^{*b}}$$
The bootstrap distribution function $P^*(T^* \le x)$ admits an identical Edgeworth expansion:
$$P^*(T^* \le x) = \Phi(x) + n^{-1/2} \hat{p}_1(x) \phi(x) + O_p(n^{-1})$$
Because $\hat{p}_1(x) - p_1(x) = O_p(n^{-1/2})$, taking the difference between the true distribution and the bootstrap distribution eliminates the leading $O(n^{-1/2})$ error term:
$$P(T \le x) - P^*(T^* \le x) = O_p(n^{-1})$$

Consequently, a two-sided confidence interval constructed using the quantiles $t^*_{\alpha/2}$ and $t^*_{1-\alpha/2}$ of the studentized bootstrap root achieves **second-order accuracy**:
$$P\left( \hat{\theta} - t^*_{1-\alpha/2} \hat{\sigma} \le \theta \le \hat{\theta} - t^*_{\alpha/2} \hat{\sigma} \right) = 1 - \alpha + O(n^{-1})$$
The coverage error drops from $O(n^{-1/2})$ to $O(n^{-1})$, providing vastly superior finite-sample calibration in skewed or heavy-tailed environments.

### 2. The $BC_a$ (Bias-Corrected and Accelerated) Bootstrap
While the bootstrap-$t$ is second-order accurate, it is not transformation-invariant and can exhibit erratic instability if $\hat{\sigma}^*$ is volatile. Efron (1987) introduced the **$BC_a$ bootstrap**, which achieves second-order accuracy ($O(n^{-1})$ coverage error) while simultaneously being fully transformation-invariant.

The $BC_a$ confidence interval endpoints are given by percentiles of the original unstudentized bootstrap distribution $\hat{\theta}^{*(1)} \le \dots \le \hat{\theta}^{*(B)}$, but evaluated at adjusted probability indices $\alpha_1, \alpha_2$:
$$\alpha_1 = \Phi\left( \hat{z}_0 + \frac{\hat{z}_0 + z_{\alpha/2}}{1 - a(\hat{z}_0 + z_{\alpha/2})} \right)$$
$$\alpha_2 = \Phi\left( \hat{z}_0 + \frac{\hat{z}_0 + z_{1-\alpha/2}}{1 - a(\hat{z}_0 + z_{1-\alpha/2})} \right)$$

Two fundamental diagnostic parameters govern the adjustment:
1. **The Bias-Correction Parameter ($\hat{z}_0$)**: Measures median bias on the normal scale:
$$\hat{z}_0 = \Phi^{-1} \left( \frac{1}{B} \sum_{b=1}^B \mathbb{I}(\hat{\theta}^{*b} < \hat{\theta}) \right)$$
If the bootstrap distribution is symmetric and centered exactly at $\hat{\theta}$, then $\hat{z}_0 = \Phi^{-1}(0.5) = 0$.
2. **The Acceleration Parameter ($a$)**: Quantifies the rate of change of the standard error of $\hat{\theta}$ with respect to the true parameter $\theta$. It is calculated from the leave-one-out jackknife values $\hat{\theta}_{(-i)}$:
$$a = \frac{\sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^3}{6 \left[ \sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^2 \right]^{3/2}}$$
where $\bar{\theta}_{(\cdot)} = \frac{1}{n} \sum_{i=1}^n \hat{\theta}_{(-i)}$. The parameter $a$ accounts for skewness in the underlying score function. When $a = 0$ and $\hat{z}_0 = 0$, the $BC_a$ interval reduces identically to the standard percentile interval.

## 3.11 Resampling Dependent Data: Block Bootstraps and Frequency-Domain Methods

The classical i.i.d. bootstrap operates on the fundamental assumption that observations $X_1, \dots, X_n$ are mutually independent. When applied to time series, spatial lattices, or longitudinal panels, i.i.d. sampling destroys the temporal auto-covariance structure $\gamma(h) = \mathrm{Cov}(X_t, X_{t+h})$. To preserve temporal dependence, statisticians employ **Block Bootstrap** methods.

### 1. Moving Block Bootstrap (MBB) and Circular Block Bootstrap (CBB)
Introduced independently by Hans R. Künsch (1989) and Regina Y. Liu (1988), the **Moving Block Bootstrap** resamples contiguous blocks of length $b$.

Let $\{X_1, X_2, \dots, X_n\}$ be a stationary time series. Define the $i$-th overlapping block of length $b$ as:
$$B_i = (X_i, X_{i+1}, \dots, X_{i+b-1}), \quad i \in \{1, 2, \dots, n - b + 1\}$$
There are $q = n - b + 1$ such blocks. To construct a bootstrap series of length $n$, we draw $k = \lceil n/b \rceil$ blocks independently with replacement from $\{B_1, \dots, B_q\}$ and concatenate them:
$$\mathbf{X}^* = (B_{I_1}, B_{I_2}, \dots, B_{I_k})$$

The **Circular Block Bootstrap (CBB)** wraps the time series periodically onto a circle, setting $X_{n+j} = X_j$. This ensures that every observation $X_t$ appears in exactly $b$ possible blocks, eliminating edge-effect bias in the mean.

### 2. The Stationary Bootstrap of Politis and Romano
A significant theoretical limitation of both MBB and CBB is that the concatenated bootstrap time series $\mathbf{X}^*$ is non-stationary: observations within a block share their original dependence, but observations across block boundaries are mutually independent.

Dimitris N. Politis and Joseph P. Romano (1994) resolved this issue with the **Stationary Bootstrap**. Instead of fixing the block length $b$, the block length $L$ is treated as an independent geometric random variable:
$$P(L = k) = (1 - p)^{k-1} p, \quad k \in \{1, 2, \dots\}, \quad \mathbb{E}[L] = \frac{1}{p} = b$$
At each step, with probability $1 - p$, the next observation is the sequential successor $X_{t+1}$ (wrapping circularly); with probability $p$, a new starting index is sampled uniformly from $\{1, \dots, n\}$.

*Theorem (Stationary Bootstrap Validity)*: Conditional on the original data $\mathbf{X}$, the pseudo-time series $\mathbf{X}^*$ generated by the Politis-Romano algorithm is strictly stationary almost surely.

The optimal expected block length $b = 1/p$ balances variance and bias:
$$b_{\text{opt}} \propto n^{1/3}$$
If $b$ is chosen too small, the long-range autocorrelation is severed, causing severe downward bias in variance estimation. If $b$ is chosen too large, sample diversity is reduced, increasing simulation variance.

## 3.12 Subsampling and the $m$-out-of-$n$ Bootstrap

Despite its versatility, the standard $n$-out-of-$n$ bootstrap exhibits well-known catastrophic failure modes in non-regular estimation problems:
1. **Extreme Value Estimation**: Estimating the maximum of a uniform distribution $\theta = \max(X_1, \dots, X_n)$ where $X_i \sim \mathcal{U}(0, \theta)$. The probability that the bootstrap sample maximum $\hat{\theta}^* = \max(\mathbf{X}^*)$ equals the sample maximum $\hat{\theta}$ is:
$$P^*(\hat{\theta}^* = \hat{\theta}) = 1 - \left(1 - \frac{1}{n}\right)^n \to 1 - e^{-1} \approx 0.632$$
The bootstrap distribution places a discrete probability mass of $63.2\%$ at the single point $\hat{\theta}$, whereas the true normalized distribution $n(\theta - \hat{\theta})$ is continuous exponential.
2. **Parameters on the Boundary**: Estimating $\theta \ge 0$ when the true parameter is $\theta = 0$.
3. **Heavy-Tailed Distributions**: Resampling data from stable Paretian distributions with infinite second moments ($\mathbb{E}[X^2] = \infty$).

### The $m$-out-of-$n$ Bootstrap Remedy
Peter J. Bickel, Friedrich Götze, and Willem R. van Zwet (1997) proved that these failure modes can be universally resolved by drawing resamples of size $m$ strictly smaller than $n$, such that:
$$m \to \infty \quad \text{and} \quad \frac{m}{n} \to 0 \quad \text{as } n \to \infty$$

Under the $m$-out-of-$n$ scheme, the normalized bootstrap statistic:
$$\tau_m (\hat{\theta}_m^* - \hat{\theta}_n)$$
converges in probability to the true limiting distribution of $\tau_n (\hat{\theta}_n - \theta)$, restoring consistency where the standard bootstrap fails. Politis and Romano's general theory of **Subsampling** extends this further by sampling without replacement from all $\binom{n}{m}$ subsets, requiring zero distributional assumptions beyond the existence of an asymptotic limit law.


## 3.13 The Wild Bootstrap for Heteroskedastic Regression Models

In linear regression models $Y_i = \mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i$, standard residual bootstrap resamples the centered residuals $\hat{\epsilon}_i = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}$ with equal probability $1/n$. However, this formulation assumes homoskedasticity: $\mathrm{Var}(\epsilon_i \mid \mathbf{x}_i) = \sigma^2$. When the error variance depends on covariates ($\mathrm{Var}(\epsilon_i \mid \mathbf{x}_i) = \sigma^2(\mathbf{x}_i)$), standard residual resampling spreads the variance uniformly across all design points, destroying the heteroskedastic structure and invalidating inferences.

C. F. J. Wu (1986) and Enno Mammen (1993) introduced the **Wild Bootstrap** to resolve heteroskedasticity.

### 1. Mathematical Formulation
Instead of shuffling residuals across different observations, the Wild Bootstrap keeps each residual tied strictly to its own observation index $i$, but scales it by an independent random multiplier $v_i$:

$$Y_i^* = \mathbf{x}_i^T \hat{\boldsymbol{\beta}} + \hat{\epsilon}_i \cdot v_i$$

where $v_1, \dots, v_n$ are independent and identically distributed random variables drawn from an auxiliary distribution $G$ satisfying:
$$\mathbb{E}[v_i] = 0 \quad \text{and} \quad \mathrm{Var}(v_i) = \mathbb{E}[v_i^2] = 1$$
Because $\mathbb{E}[Y_i^* \mid \mathbf{x}_i] = \mathbf{x}_i^T \hat{\boldsymbol{\beta}}$ and $\mathrm{Var}(Y_i^* \mid \mathbf{x}_i) = \hat{\epsilon}_i^2 \mathrm{Var}(v_i) = \hat{\epsilon}_i^2$, the bootstrap resample mimics both the conditional mean and the observation-specific heteroskedastic variance.

### 2. Multiplier Distributions
To achieve higher-order asymptotic accuracy, the third moment of $v_i$ should match the skewness of the underlying distribution ($\mathbb{E}[v_i^3] = 1$):

1. **Mammen's Two-Point Distribution**:
$$v_i = \begin{cases} -(\sqrt{5} - 1)/2 \approx -0.6180, & \text{with probability } p = \frac{\sqrt{5} + 1}{2\sqrt{5}} \approx 0.7236 \\ (\sqrt{5} + 1)/2 \approx 1.6180, & \text{with probability } 1 - p = \frac{\sqrt{5} - 1}{2\sqrt{5}} \approx 0.2764 \end{cases}$$
Mammen's distribution satisfies $\mathbb{E}[v] = 0$, $\mathbb{E}[v^2] = 1$, and $\mathbb{E}[v^3] = 1$, eliminating the leading skewness error term in asymptotic expansions.
2. **The Rademacher Distribution**:
$$v_i = \begin{cases} -1, & \text{with probability } 0.5 \\ +1, & \text{with probability } 0.5 \end{cases}$$
While $\mathbb{E}[v_i^3] = 0$ (symmetric), Emmanuel Flachaire (2005) and Colin Cameron et al. (2008) demonstrated that Rademacher multipliers exhibit superior finite-sample power and avoid spurious tail distortion when testing symmetric hypotheses.
3. **Standard Normal Multiplier**: $v_i \sim \mathcal{N}(0, 1)$, widely known as the Gaussian wild bootstrap.

## 3.14 The Smoothed Bootstrap and Kernel Resampling

The standard empirical distribution function $F_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i \le x)$ is a step function with jump discontinuities of size $1/n$ at each observed data point. Consequently, standard bootstrap resamples $\mathbf{x}^*$ consist entirely of ties and duplicate values from the observed sample. 

When estimating quantities sensitive to the local continuity of the density—such as quantiles, density modes, or when data are generated by an inherently continuous physical process—the discrete nature of $F_n$ introduces non-negligible bias. Bernard Silverman (1986) introduced the **Smoothed Bootstrap** to sample from a continuous non-parametric density estimate.

### Algorithmic Mechanics
Let $\hat{f}_h(x)$ be the standard Rosenblatt-Parzen kernel density estimator:
$$\hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^n K\left( \frac{x - X_i}{h} \right)$$
where $K(\cdot)$ is a symmetric probability density kernel (such as the Gaussian kernel) with $\int u K(u)\,du = 0$ and $\int u^2 K(u)\,du = \sigma_K^2 = 1$, and $h > 0$ is the smoothing bandwidth.

Drawing a variate $X^*$ from $\hat{f}_h(x)$ is computationally equivalent to:
1. Drawing an observation $X_I$ uniformly at random from the original sample $\{X_1, \dots, X_n\}$ with replacement.
2. Drawing a continuous perturbation $\epsilon \sim K$ from the kernel distribution.
3. Setting:
$$X^* = X_I + h \cdot \epsilon$$

Because convolution adds variance ($\mathrm{Var}(X^*) = S_n^2 + h^2$), Silverman developed the **Variance-Corrected Smoothed Bootstrap**:
$$X_{\text{corrected}}^* = \bar{X} + \frac{1}{\sqrt{1 + h^2 / S_n^2}} \left( X_I - \bar{X} + h \cdot \epsilon \right)$$
This linear shrinkage adjustment ensures that the bootstrap resample possesses exactly the sample mean $\bar{X}$ and sample variance $S_n^2$ of the original dataset while sampling from a smooth continuous continuum.


## 3.15 Permutation Tests vs. Bootstrap Resampling: An Epistemological Comparison

In non-parametric inference, computational statisticians frequently choose between two prominent computer-intensive resampling methodologies: **Permutation Tests** (Randomization Tests) and the **Bootstrap**. While both methods liberate the analyst from rigid parametric Gaussian assumptions, their mathematical structures, null hypotheses, and exchangeability assumptions are fundamentally distinct.

### 1. Permutation Tests and the Exchangeability Criterion
Developed conceptually by Ronald A. Fisher (1935) and formalized by E. J. G. Pitman (1937), permutation tests assess null hypotheses by evaluating how frequently an observed test statistic occurs under all possible relabelings of the data.

Consider a two-sample comparison: sample 1 has observations $X_1, \dots, X_{n_1}$ from distribution $F_X$, and sample 2 has observations $Y_1, \dots, Y_{n_2}$ from distribution $F_Y$. The null hypothesis is identity of distributions:
$$H_0: F_X = F_Y$$
Under $H_0$, the assignment of observations to treatment or control is an arbitrary label. The pooled vector of observations $\mathbf{Z} = (X_1, \dots, X_{n_1}, Y_1, \dots, Y_{n_2})$ of size $N = n_1 + n_2$ satisfies **Exchangeability**: every permutation $\pi \in \mathcal{S}_N$ of the indices is equally probable under the null measure.

The exact two-sided $p$-value is:
$$p = \frac{1}{N!} \sum_{\pi \in \mathcal{S}_N} \mathbb{I}(|T(\mathbf{Z}_\pi)| \ge |T_{\text{obs}}|)$$
When $N$ is moderately large, evaluating all $N!$ or $\binom{N}{n_1}$ permutations is computationally impossible. A **Monte Carlo Permutation Test** draws $B$ random permutations uniformly from $\mathcal{S}_N$:
$$\hat{p} = \frac{1 + \sum_{b=1}^B \mathbb{I}(|T(\mathbf{Z}_{\pi_b})| \ge |T_{\text{obs}}|)}{1 + B}$$
The inclusion of $+1$ in numerator and denominator guarantees that $\hat{p}$ is a strictly valid $p$-value under $H_0$, with Type I error rate $P(\hat{p} \le \alpha) \le \alpha$ for any sample size $N$ and any number of simulation draws $B$.

### 2. Methodological Differences
<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Feature / Property</th>
<th>Permutation Testing (Randomization)</th>
<th>Bootstrap Resampling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Primary Purpose</strong></td>
<td>Hypothesis testing ($p$-values, significance decisions).</td>
<td>Parameter estimation, standard errors, confidence intervals.</td>
</tr>
<tr>
<td><strong>Sampling Mechanism</strong></td>
<td>Sampling <em>without replacement</em> from the pooled data.</td>
<td>Sampling <em>with replacement</em> from the observed sample.</td>
</tr>
<tr>
<td><strong>Underlying Assumption</strong></td>
<td>Exchangeability under the sharp null hypothesis ($F_X = F_Y$).</td>
<td>Observations are i.i.d. draws from true population $F$.</td>
</tr>
<tr>
<td><strong>Finite-Sample Validity</strong></td>
<td>Exact test. Type I error is strictly controlled at $\alpha$ for any $N$.</td>
<td>Asymptotic test. Confidence interval coverage error is $O(n^{-1/2})$ or $O(n^{-1})$.</td>
</tr>
<tr>
<td><strong>Generalizability</strong></td>
<td>Restricted: cannot easily test non-sharp hypotheses (e.g., $H_0: \mu_X - \mu_Y = 0$ when $\sigma_X^2 \ne \sigma_Y^2$).</td>
<td>Broad: applies to almost any estimable functional $\theta = T(F)$.</td>
</tr>
</tbody>
</table>
</div>

Permutation tests represent the gold standard when testing sharp null hypotheses under randomized experimental designs, whereas bootstrap resampling is the premier computational technology for constructing confidence intervals for complex estimators.


## 3.16 Donald Rubin's Bayesian Bootstrap

In 1981, Donald B. Rubin introduced the **Bayesian Bootstrap**, providing a fully Bayesian interpretation of non-parametric bootstrap resampling.

### 1. Theoretical Formulation
The classical Efron bootstrap places random multinomial probabilities on the observed data points $\mathbf{x} = (x_1, \dots, x_n)$:
$$\mathbf{w} \sim \frac{1}{n} \text{Multinomial}\left(n, \left(\frac{1}{n}, \dots, \frac{1}{n}\right)\right)$$
This integer-weighting scheme causes some observations to be selected multiple times while roughly $36.8\%$ are omitted entirely.

Rubin proposed viewing the unknown distribution function as a random step function $F(x) = \sum_{i=1}^n w_i \mathbb{I}(x_i \le x)$, where the probability weights $\mathbf{w} = (w_1, \dots, w_n)$ form a continuous random vector on the unit simplex $\Delta^{n-1} = \{ \mathbf{w} \in \mathbb{R}^n : w_i \ge 0, \sum w_i = 1 \}$. 

Under an improper non-informative Haldane prior on the multinomial probabilities ($p(\mathbf{w}) \propto \prod w_i^{-1}$), the posterior distribution of the weights given the observations is a symmetric **Dirichlet Distribution**:
$$\mathbf{w} \sim \text{Dirichlet}(1, 1, \dots, 1)$$

### 2. Algorithmic Implementation
To generate one Bayesian bootstrap realization:
1. Generate $n-1$ independent uniform random variates $U_1, \dots, U_{n-1} \sim \mathcal{U}(0, 1)$.
2. Sort them in ascending order and append boundary constants: $0 = U_{(0)} \le U_{(1)} \le \dots \le U_{(n-1)} \le U_{(n)} = 1$.
3. Compute the successive uniform spacings:
$$w_i = U_{(i)} - U_{(i-1)}, \quad i = 1, \dots, n$$
Equivalently, draw $E_1, \dots, E_n \sim \text{Exp}(1)$ and set $w_i = E_i / \sum_{j=1}^n E_j$.
4. Evaluate the parameter functional on the weighted distribution: $\theta^* = T\left( \sum_{i=1}^n w_i \delta_{x_i} \right)$.

The Bayesian bootstrap produces a smooth, continuous posterior distribution over the parameter space, eliminating the artificial discreteness artifacts of integer-count resampling.


## 3.17 Computational Laboratory: Bootstrap Confidence Interval Calibration on Skewed Credit Losses

In institutional risk modeling, estimating the Value at Risk (VaR) or expected shortfall from highly skewed, heavy-tailed empirical loss data poses severe calibration challenges. 

When analyzing a corporate loan default portfolio ($n = 250$ loss events with sample skewness $\hat{\kappa}_3 = 2.8$):
- Standard normal-approximation intervals provide only $87.4\%$ empirical coverage for a nominal $95\%$ confidence level due to failure to account for positive asymmetry.
- The basic percentile bootstrap achieves $91.2\%$ coverage, exhibiting systematic downward bias in the upper tail.
- The studentized bootstrap ($t$-bootstrap) and $BC_a$ bootstrap achieve $94.8\%$ and $95.1\%$ coverage respectively, correctly shifting the confidence bounds upward to accommodate tail skewness.

This demonstrates why higher-order accurate bootstrap intervals are indispensable for regulatory capital estimation.


## 3.18 Unit 3 Review and Methodological Synthesis

Unit 3 explored computer-intensive non-parametric resampling methods, focusing on the Jackknife and the Bootstrap. We derived Tukey's jackknife bias correction and pseudo-value variance estimation, analyzing its failure on non-smooth functionals such as the sample median. We formulated Bradley Efron's non-parametric bootstrap, establishing that drawing with replacement from the empirical distribution function $F_n$ approximates sampling from the true population distribution $F$. Using Edgeworth expansions, we demonstrated that while percentile and normal-approximation bootstrap intervals achieve only first-order accuracy with $O(n^{-1/2})$ coverage error, studentized bootstrap-t and bias-corrected accelerated ($BC_a$) intervals achieve second-order accuracy with $O(n^{-1})$ coverage error. For dependent time series, we introduced the Moving Block Bootstrap and the Politis-Romano Stationary Bootstrap with geometric block lengths to preserve auto-covariance structures. Finally, we demonstrated how the $m$-out-of-$n$ bootstrap and subsampling resolve non-regular estimation problems where the standard bootstrap fails.


## 3.19 Resampling for Clustered and Panel Data Structures

In econometric panel datasets, longitudinal clinical trials, and multi-stage educational surveys, observations are grouped into natural clusters (e.g., patients within hospitals, students within classrooms, or repeated observations across time for a firm). Observations within the same cluster share unobserved random shocks, violating the fundamental mutual independence assumption of the standard bootstrap.

When data exhibit intra-cluster correlation, applying naive observation-level bootstrap resampling severely underestimates standard errors and produces anti-conservative confidence intervals. The **Cluster Bootstrap** (Cameron, Gelbach, and Miller 2008) resamples entire clusters with replacement:
$$\mathcal{C}_1^*, \mathcal{C}_2^*, \dots, \mathcal{C}_G^* \sim \text{Uniform with replacement from } \{\mathcal{C}_1, \dots, \mathcal{C}_G\}$$
By treating each cluster as an independent statistical unit and preserving the entire internal covariance matrix within each cluster, the cluster bootstrap provides asymptotically valid inference for panel regression estimators without requiring parametric specification of the intra-cluster error covariance structure.
