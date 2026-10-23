# Unit 2: Non-Uniform Random Variate Generation: Inversion & Transformations

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


## 2.9 The Walker-Vose Alias Method for Arbitrary Discrete Distributions

When conducting agent-based simulations, Markov chain simulations with large discrete state spaces, or categorical sampling in natural language models, one must repeatedly draw variates from a discrete probability mass function defined on $K$ categories:

$$P(X = k) = p_k, \quad k \in \{1, 2, \dots, K\}, \quad \sum_{k=1}^K p_k = 1$$

A standard cumulative distribution function (CDF) inversion algorithm constructs the running prefix sums $S_j = \sum_{k=1}^j p_k$ and performs a binary search for a uniform draw $U \sim \mathcal{U}(0, 1)$. This requires $O(\log_2 K)$ search operations per generated variate. If $K$ is on the order of $10^5$ or $10^6$ (as in vocabulary token sampling or large network node activation), binary search incurs severe branch mispredictions and memory latency.

In 1974, Alastair J. Walker introduced the **Alias Method**, which was subsequently refined into an optimal $O(K)$ setup and $O(1)$ sampling algorithm by Michael D. Vose in 1991.

### 1. Theoretical Foundation of the Alias Decomposition
The mathematical insight of the Alias Method is that any discrete probability distribution with $K$ outcomes can be expressed as an equiprobable mixture of $K$ two-point distributions.

Imagine $K$ rectangular urns (or bins) of equal width $1/K$ and total height $1.0$. The total area across all $K$ bins is $K \times (1/K) = 1.0$. The probability distribution $\{p_1, \dots, p_K\}$ can be scaled by $K$ so that each category $k$ has normalized weight $q_k = K \cdot p_k$. The average normalized weight is:

$$\frac{1}{K} \sum_{k=1}^K q_k = \frac{K}{K} \sum_{k=1}^K p_k = 1.0$$

Some categories have $q_k < 1.0$ (they are "underfull"), while others have $q_k \ge 1.0$ (they are "overfull"). The Alias Theorem guarantees that one can redistribute the excess mass from overfull categories into underfull categories such that every bin $i \in \{1, \dots, K\}$ contains mass from at most **two** distinct categories:
1. The primary outcome $i$, occupying probability weight $F_i \in (0, 1]$.
2. An "alias" outcome $A_i \in \{1, \dots, K\}$, occupying the remaining weight $1 - F_i$.

### 2. The Vose Construction Algorithm
The preprocessing phase partitions categories into two worklists:
- **Small**: indices with $q_k < 1.0$.
- **Large**: indices with $q_k \ge 1.0$.

While both lists are non-empty:
1. Remove an index $s$ from **Small** and an index $l$ from **Large**.
2. Set the threshold probability table entry $F_s = q_s$.
3. Set the alias table entry $A_s = l$.
4. Reduce the remaining weight of category $l$ by the shortfall of $s$:
$$q_l \leftarrow q_l - (1.0 - q_s)$$
5. If the updated $q_l < 1.0$, insert $l$ into **Small**; otherwise, return $l$ to **Large**.

Because exactly one element is permanently removed from the active pools at each iteration, the construction terminates in at most $K$ steps, yielding exact $O(K)$ computational and memory complexity.

### 3. Constant Time Sampling Step
To generate a single realization $X \sim \{p_1, \dots, p_K\}$ in real-time simulation:
1. Generate a single uniform variate $U \sim \mathcal{U}(0, 1)$.
2. Compute the continuous coordinate $V = K \cdot U$.
3. Let $i = \lfloor V \rfloor + 1 \in \{1, \dots, K\}$ be the randomly selected bin index.
4. Let $W = V - \lfloor V \rfloor \in [0, 1)$ be the fractional position within that bin.
5. If $W < F_i$, return outcome $i$; otherwise, return outcome $A_i$.

This execution path consists of a single floating-point multiplication, a floor conversion, one array lookup, and a single branch, achieving strict $O(1)$ time complexity regardless of whether $K = 10$ or $K = 10,000,000$.

## 2.10 The Ratio-of-Uniforms Method

The **Ratio-of-Uniforms (RoU)** method, developed by Albert J. Kinderman and John F. Monahan (1977), is an elegant rejection-based simulation technique that transforms two independent uniform variates into a random variable from an arbitrary target continuous distribution. Unlike the classical Acceptance-Rejection method of von Neumann, RoU does not require finding an explicit dominating proposal density $g(x)$ that bounds $f(x)$ pointwise.

### 1. Mathematical Formulation
Let $X$ be a continuous random variable with probability density function:
$$f(x) = \frac{1}{Z} h(x), \quad x \in \mathbb{R}$$
where $h(x) \ge 0$ is a computable unnormalized density function and $Z = \int_{\mathbb{R}} h(x)\,dx$ is an intractable normalizing constant.

Consider the planar region $C_h \subset \mathbb{R}^2$ defined by:
$$C_h = \left\{ (u, v) \in \mathbb{R}^2 : 0 \le u \le \sqrt{h(v/u)} \right\}$$

*Theorem (Kinderman-Monahan)*: If a pair $(U, V)$ is distributed uniformly over the region $C_h$, then the ratio:
$$X = \frac{V}{U}$$
has exact probability density function $f(x) = h(x) / Z$.

*Proof*: The area of the region $C_h$ is given by the double integral:
$$\text{Area}(C_h) = \iint_{C_h} du\,dv = \int_{-\infty}^\infty \left[ \int_0^{\sqrt{h(v/u)}} du \right] dv$$
Perform the bivariate change of variables: $x = v/u$ and $u = u$. The Jacobian matrix of the transformation $(u, v) \mapsto (u, x)$ where $v = ux$ is:
$$J = \begin{pmatrix} \frac{\partial u}{\partial u} & \frac{\partial u}{\partial x} \\ \frac{\partial v}{\partial u} & \frac{\partial v}{\partial x} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ x & u \end{pmatrix} \implies |\det(J)| = u$$
Substituting this into the area integral:
$$\text{Area}(C_h) = \int_{-\infty}^\infty \int_0^{\sqrt{h(x)}} u\,du\,dx = \int_{-\infty}^\infty \left[ \frac{u^2}{2} \right]_0^{\sqrt{h(x)}} dx = \frac{1}{2} \int_{-\infty}^\infty h(x)\,dx = \frac{Z}{2}$$

Because $(U, V)$ is uniform on $C_h$, its joint density is constant:
$$f_{U, V}(u, v) = \frac{1}{\text{Area}(C_h)} = \frac{2}{Z}, \quad (u, v) \in C_h$$
Applying the transformation $(U, V) \to (U, X)$ with $V = UX$:
$$f_{U, X}(u, x) = f_{U, V}(u, ux) \cdot |\det(J)| = \frac{2}{Z} \cdot u, \quad 0 \le u \le \sqrt{h(x)}$$
Integrating out the nuisance coordinate $u$ to find the marginal density of $X$:
$$f_X(x) = \int_0^{\sqrt{h(x)}} \frac{2u}{Z}\,du = \frac{2}{Z} \left[ \frac{u^2}{2} \right]_0^{\sqrt{h(x)}} = \frac{h(x)}{Z}$$
which is identically the target probability density function.

### 2. Computational Bounding Box Construction
To sample uniformly from $C_h$, one constructs the minimal enclosing bounding box $[0, u_{\max}] \times [v_{\min}, v_{\max}]$, where:
$$u_{\max} = \sup_{x} \sqrt{h(x)}$$
$$v_{\min} = \inf_{x} \left( x \sqrt{h(x)} \right)$$
$$v_{\max} = \sup_{x} \left( x \sqrt{h(x)} \right)$$

Provided that $h(x)$ and $x^2 h(x)$ are bounded on $\mathbb{R}$, this bounding box is finite. The algorithm generates independent uniforms $U \sim \mathcal{U}(0, u_{\max})$ and $V \sim \mathcal{U}(v_{\min}, v_{\max})$. If $U^2 \le h(V / U)$, the variate $X = V / U$ is accepted; otherwise, the pair is rejected and the step is repeated.

For standard normal variates $h(x) = e^{-x^2/2}$, we obtain $u_{\max} = 1$, $v_{\min} = -\sqrt{2/e} \approx -0.8578$, and $v_{\max} = \sqrt{2/e} \approx 0.8578$. The acceptance probability is $\text{Area}(C_h) / [u_{\max}(v_{\max} - v_{\min})] = \sqrt{\pi/2} / (2 \sqrt{2/e}) = \sqrt{\pi e} / 4 \approx 0.7306$, yielding an exceptionally efficient Gaussian generator without transcendental trigonometric evaluations.

## 2.11 Simulation of High-Dimensional Gaussian Processes and Circulant Embedding

In spatial statistics, geostatistics, and functional data analysis, simulations require generating continuous sample paths from a **Gaussian Process (GP)**:

$$X(t) \sim \mathcal{GP}(m(t), K(t, s)), \quad t, s \in \mathcal{T} \subset \mathbb{R}^d$$

where $m(t) = \mathbb{E}[X(t)]$ is the mean function and $K(t, s) = \mathrm{Cov}(X(t), X(s))$ is a symmetric positive semi-definite covariance kernel (such as the Matérn, Squared Exponential, or Ornstein-Uhlenbeck kernel).

### 1. The Standard Cholesky Factorization Approach
When evaluating the Gaussian process at $N$ discrete locations $\mathbf{t} = (t_1, \dots, t_N)^T$, the joint distribution is multivariate normal:
$$\mathbf{X} \sim \mathcal{N}(\mathbf{m}, \mathbf{\Sigma}), \quad \mathbf{\Sigma}_{ij} = K(t_i, t_j)$$

The classical method computes the Cholesky decomposition of the covariance matrix:
$$\mathbf{\Sigma} = \mathbf{L} \mathbf{L}^T$$
where $\mathbf{L}$ is a lower-triangular matrix. Given an independent standard normal vector $\mathbf{Z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_N)$, the simulated Gaussian process realization is:
$$\mathbf{X} = \mathbf{m} + \mathbf{L} \mathbf{Z}$$

While mathematically exact and applicable to irregularly spaced coordinates, Cholesky factorization requires $O(N^3)$ arithmetic operations to compute the decomposition and $O(N^2)$ memory to store the matrix. For a two-dimensional grid of size $1024 \times 1024$, the number of locations is $N = 2^{20} \approx 10^6$, requiring $\approx 10^{18}$ floating-point operations and multiple terabytes of memory, rendering Cholesky factorization impossible.

### 2. Fast Circulant Embedding and FFT Simulation
When sample locations form a regular equispaced lattice on a stationary domain (where $K(t, s) = \kappa(t - s)$ depends only on the spatial displacement vector), the covariance matrix $\mathbf{\Sigma}$ exhibits a symmetric **Toeplitz** structure (in 1D) or **Block Toeplitz with Toeplitz Blocks (BTTB)** structure (in higher dimensions).

Dietrich and Newsam (1993) and Wood and Chan (1994) introduced the **Circulant Embedding** technique to reduce the computational complexity from $O(N^3)$ to $O(N \log N)$ using the Fast Fourier Transform (FFT).

1. **Embedding into a Circulant Matrix**: The $N \times N$ Toeplitz covariance matrix $\mathbf{\Sigma}$ is embedded into a larger $M \times M$ circulant matrix $\mathbf{C}$ (typically with $M = 2N$):
$$\mathbf{C} = \begin{pmatrix} \mathbf{\Sigma} & \mathbf{B} \\ \mathbf{B}^T & \mathbf{\Sigma} \end{pmatrix}$$
where $\mathbf{B}$ is chosen such that the rows of $\mathbf{C}$ are periodic circular shifts of each other.

2. **Spectral Decomposition via Discrete Fourier Transform**: Every circulant matrix is diagonalized by the unitary Discrete Fourier Transform matrix $\mathbf{F}$:
$$\mathbf{C} = \mathbf{F}^* \mathbf{\Lambda} \mathbf{F}$$
where $\mathbf{\Lambda} = \mathrm{diag}(\lambda_0, \dots, \lambda_{M-1})$ are the eigenvalues of $\mathbf{C}$, which are computed in $O(M \log M)$ operations by taking the FFT of the first column of $\mathbf{C}$:
$$\boldsymbol{\lambda} = \mathrm{FFT}(\mathbf{c}_0)$$

3. **Non-Negative Definiteness Condition**: If all eigenvalues satisfy $\lambda_j \ge 0$, $\mathbf{C}$ is positive semi-definite. A complex normal vector $\mathbf{W} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I}_M)$ is generated with independent real and imaginary standard Gaussian components:
$$\mathbf{Y} = \mathbf{F}^* (\mathbf{\Lambda}^{1/2} \mathbf{W}) = \mathrm{IFFT}(\sqrt{\boldsymbol{\lambda}} \odot \mathrm{FFT}(\mathbf{Z}))$$
Extracting the first $N$ elements of the real part of $\mathbf{Y}$ yields an exact realization of the Gaussian process $\mathbf{X}$ with covariance $\mathbf{\Sigma}$. The entire generation completes in $O(N \log N)$ operations, enabling real-time simulation of multi-million point Gaussian random fields.


## 2.12 Exact Simulation of Truncated Distributions

In survival analysis, econometric modeling of censored earnings, and truncated regression (Tobit models), statisticians must draw variates from standard distributions conditioned on belonging to a restricted interval:

$$X \sim f(x \mid a \le X \le b) = \frac{f(x)}{F(b) - F(a)} \mathbb{I}(a \le x \le b)$$

When the truncation interval $[a, b]$ falls in the central body of the distribution, naive acceptance-rejection—drawing $X \sim f$ and discarding draws outside $[a, b]$—works well. However, when simulating rare tail events where $a \gg 0$ (e.g., simulating standard normal variates conditioned on $Z \ge 6$), the probability of landing in the interval is $P(Z \ge 6) \approx 9.86 \times 10^{-10}$. Naive rejection sampling requires an average of over one billion simulation draws per accepted variate, resulting in complete computational stalling.

### 1. Inversion of Truncated Normal CDFs
Using the probability integral transform on the truncated CDF:
$$F_T(x) = \frac{\Phi(x) - \Phi(a)}{\Phi(b) - \Phi(a)} = U \sim \mathcal{U}(0, 1)$$
Solving for $x$ yields:
$$X = \Phi^{-1}\left( \Phi(a) + U \cdot [\Phi(b) - \Phi(a)] \right)$$
While mathematically exact, this formula suffers from catastrophic numerical floating-point underflow when $a$ is large. In standard 64-bit IEEE double precision, $\Phi(6) = 1.0 - \epsilon$ evaluates to $1.0$, causing $\Phi(b) - \Phi(a)$ to round to zero and producing `NaN` or infinite values.

### 2. Christian Robert's Optimal Translated Exponential Proposal
Christian P. Robert (1995) designed an optimal rejection algorithm for simulating truncated normal variates $Z \sim \mathcal{N}(0, 1) \mathbb{I}(Z \ge a)$ that achieves bounded, near-unity acceptance rates for arbitrarily large truncation thresholds $a$.

Robert proposed utilizing a translated exponential distribution:
$$g(z; \lambda) = \lambda e^{-\lambda(z - a)}, \quad z \ge a$$
The acceptance ratio is:
$$\frac{f(z)}{g(z; \lambda)} = \frac{\frac{1}{\sqrt{2\pi}} e^{-z^2/2}}{\lambda e^{-\lambda(z - a)}} = \frac{e^{\lambda a}}{\lambda \sqrt{2\pi}} \exp\left( -\frac{z^2}{2} + \lambda z \right) = \frac{e^{\lambda a + \lambda^2/2}}{\lambda \sqrt{2\pi}} \exp\left( -\frac{(z - \lambda)^2}{2} \right)$$
To maximize the acceptance probability, we minimize the supremum of the ratio over $z \ge a$. The quadratic exponent achieves its maximum at $z = \lambda$ if $\lambda \ge a$, or at $z = a$ if $\lambda < a$. 
Robert proved that the optimal scale parameter $\lambda^*$ is:
$$\lambda^*(a) = \frac{a + \sqrt{a^2 + 4}}{2}$$
Under this optimal parameter, the acceptance ratio simplifies remarkably:
$$\alpha(z) = \exp\left( -\frac{(z - \lambda^*(a))^2}{2} \right)$$
The simulation algorithm proceeds as follows:
1. Generate $E_1, E_2 \sim \text{Exp}(1)$ independently.
2. Set proposed value $Z = a + E_1 / \lambda^*$.
3. If $E_2 \ge \frac{(Z - \lambda^*)^2}{2}$, accept $Z$; otherwise reject and repeat.

Because the acceptance probability satisfies $P(\text{accept}) \ge 0.76$ for all $a \ge 0$, and approaches $1.0$ as $a \to \infty$, this algorithm produces exact extreme tail draws in milliseconds with zero numerical underflow.

## 2.13 Simulation of Hawkes Processes and Self-Exciting Point Processes

Point processes model the stochastic arrival of discrete events in continuous time $t \in [0, T]$. In seismology (aftershocks), high-frequency financial microstructure (order book transactions), and epidemiology (contagion propagation), event arrivals exhibit temporal clustering: the occurrence of an event increases the instantaneous probability of subsequent events. Alan G. Hawkes (1971) formalized this behavior in the **Hawkes Self-Exciting Process**.

The conditional intensity function $\lambda(t \mid \mathcal{H}_t)$ given event history $\mathcal{H}_t = \{t_i : t_i < t\}$ is:
$$\lambda(t \mid \mathcal{H}_t) = \mu + \sum_{t_i < t} \alpha \, e^{-\beta(t - t_i)}$$
where $\mu > 0$ is the baseline background rate, $\alpha > 0$ is the excitation magnitude, and $\beta > \alpha$ is the exponential decay rate. The ratio $n = \alpha / \beta < 1$ represents the branching ratio, ensuring stability.

### The Lewis-Shedler Thinning Algorithm for Hawkes Processes
Because $\lambda(t)$ jumps discontinuously at each arrival time and decays continuously between arrivals, direct inversion of the cumulative intensity is intractable. P. A. W. Lewis and G. S. Shedler (1979) introduced the **Thinning Algorithm** (a continuous-time Poisson analog of rejection sampling):

1. Set current time $t = 0$ and event counter $k = 0$.
2. Compute the maximum instantaneous intensity immediately after the most recent event:
$$\lambda_{\max} = \lambda(t \mid \mathcal{H}_t) = \mu + \sum_{t_i < t} \alpha e^{-\beta(t - t_i)}$$
3. Generate a candidate inter-arrival time from a homogeneous Poisson process with rate $\lambda_{\max}$:
$$\Delta t \sim \text{Exp}(\lambda_{\max}), \quad t_{\text{cand}} = t + \Delta t$$
If $t_{\text{cand}} > T$, terminate simulation.
4. Evaluate the exact decaying intensity at the candidate time:
$$\lambda(t_{\text{cand}}) = \mu + \sum_{t_i < t} \alpha e^{-\beta(t_{\text{cand}} - t_i)}$$
5. Draw $U \sim \mathcal{U}(0, 1)$. If $U \le \frac{\lambda(t_{\text{cand}})}{\lambda_{\max}}$, the candidate arrival is accepted:
$$k \leftarrow k + 1, \quad t_k = t_{\text{cand}}, \quad t \leftarrow t_{\text{cand}}$$
Otherwise, the candidate arrival is "thinned" (rejected), and we set $t \leftarrow t_{\text{cand}}$ without recording an arrival.
6. Repeat from Step 2 until the time horizon $T$ is reached.


## 2.14 The Ziggurat Algorithm for Ultra-Fast Continuous Sampling

While the Box-Muller transform and the polar method generate standard Gaussian variates effectively, both algorithms require evaluating expensive transcendental functions: Box-Muller computes square roots, natural logarithms, and trigonometric sines and cosines, consuming dozens of clock cycles per generated pair.

George Marsaglia and Wai Wan Tsang (2000) introduced the **Ziggurat Algorithm**, which generates continuous random variates (particularly standard Normal and Exponential variables) using almost exclusively table lookups and integer comparisons, executing in fewer than 10 CPU clock cycles on modern hardware.

### 1. Geometric Construction of the Ziggurat
Let $f(x)$ be a monotonically decreasing probability density function on $[0, \infty)$ (such as the positive half of the standard normal density $f(x) = \sqrt{2/\pi} e^{-x^2/2}$).

The area under $f(x)$ is partitioned into $M$ horizontal rectangular slices (typically $M = 256$, fitting into an 8-bit index). Slices are indexed $i = 0, 1, \dots, M-1$ from bottom to top:
- Each rectangular layer $i$ extends horizontally from $0$ to $x_i$ and vertically from $y_{i-1}$ to $y_i = f(x_i)$.
- Crucially, the endpoints $x_i$ are precomputed such that **every layer has identical area $V$**:
$$V = x_i (y_i - y_{i-1}) = x_{M-1} (1 - y_{M-2}) = \text{constant}$$
The bottom slice $i = 0$ is special: it consists of a central rectangle of width $x_0$ and height $y_0 = f(x_0)$, plus an infinite right-hand tail $T = \int_{x_0}^\infty f(x)\,dx$ such that the combined area equals $V$.

Because the layers have equal area $V$, selecting a layer $i$ uniformly at random from $\{0, 1, \dots, M-1\}$ gives an exact equiprobable mixture.

### 2. The Rapid Sampling Loop
To generate a standard normal variate:
1. Generate an independent 32-bit random integer $J$.
2. Extract the lower 8 bits of $J$ to select layer index $i \in \{0, \dots, 255\}$.
3. Use the remaining 24 bits of $J$ (converted to a uniform fraction $U \in [0, 1)$) to propose a horizontal coordinate:
$$X = U \cdot x_i$$
4. **Fast Interior Acceptance Test**: If $X < x_{i+1}$, the proposed point lies strictly inside the core interior of the ziggurat layer (underneath the density curve). Accept $X$ immediately!
5. **Slow Boundary Test**: If $X \ge x_{i+1}$, the proposed point falls in the outer margin near the density boundary. Only then does the algorithm evaluate:
$$Y = y_{i-1} + U_2 \cdot (y_i - y_{i-1})$$
If $Y \le f(X)$, accept $X$; otherwise, reject and repeat.
6. **Tail Draw**: If layer $i = 0$ was selected and $X \ge x_0$, sample directly from the tail using Robert's transformed exponential tail algorithm.

Because $M = 256$ slices provide an exceptionally tight stepped approximation to the smooth Gaussian curve, the fast interior acceptance test in Step 4 succeeds **over $98.5\%$ of the time**. The ziggurat algorithm avoids transcendental evaluations on $98.5\%$ of all generated variates, making it the fastest known algorithm for standard continuous distributions.


## 2.15 Directional Distributions and Manifold Sampling

In spatial navigation, crystallography, structural bioinformatics (protein backbone torsion angles), and paleomagnetism, random variables are not unconstrained Euclidean vectors, but unit directions residing on non-Euclidean manifolds such as the unit sphere $\mathbb{S}^{d-1} = \{ \mathbf{x} \in \mathbb{R}^d : \|\mathbf{x}\|_2 = 1 \}$ or the rotation group $\mathrm{SO}(3)$.

### 1. The Von Mises-Fisher Distribution on the Sphere
The **Von Mises-Fisher (vMF)** distribution models directional clustering on $\mathbb{S}^{d-1}$ around a mean direction $\boldsymbol{\mu} \in \mathbb{S}^{d-1}$ with concentration parameter $\kappa \ge 0$:
$$f(\mathbf{x}; \boldsymbol{\mu}, \kappa) = C_d(\kappa) \exp\left( \kappa \, \boldsymbol{\mu}^T \mathbf{x} \right)$$
where $C_d(\kappa) = \frac{\kappa^{d/2 - 1}}{(2\pi)^{d/2} I_{d/2 - 1}(\kappa)}$ is the normalizing constant involving the modified Bessel function of the first kind.

To simulate a vMF variate $\mathbf{X}$ efficiently without multidimensional rejection (Wood 1994):
1. Decompose the target vector into the parallel component $W = \boldsymbol{\mu}^T \mathbf{X} \in [-1, 1]$ and an orthogonal tangent vector $\mathbf{V} \in \mathbb{S}^{d-2}$:
$$\mathbf{X} = W \boldsymbol{\mu} + \sqrt{1 - W^2} \, \mathbf{Q} \mathbf{V}$$
where $\mathbf{Q}$ is an orthonormal basis spanning the orthogonal complement of $\boldsymbol{\mu}$.
2. The scalar coordinate $W$ has density $f_W(w) \propto (1 - w^2)^{(d-3)/2} e^{\kappa w}$, which is sampled using an acceptance-rejection scheme with an envelope based on the Beta distribution.
3. The orthogonal unit vector $\mathbf{V}$ is sampled uniformly over the equatorial sphere $\mathbb{S}^{d-2}$ by drawing standard Gaussian vectors and normalizing to unit length: $\mathbf{V} = \mathbf{Z} / \|\mathbf{Z}\|_2$ with $\mathbf{Z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_{d-1})$.


## 2.16 Computational Laboratory: Discrete Sampling at Scale with the Alias Method

In computational linguistics and generative modeling, sampling next-token predictions involves drawing from categorical distributions with vocabulary sizes $K \in [32,000, 256,000]$.

Comparing the execution profile across $10^7$ independent categorical draws:
- **Cumulative Binary Search**: Requires $O(\log_2 K) \approx 15$ to 18 memory lookups and branch evaluations per draw, triggering extensive CPU branch mispredictions and taking 14.2 seconds.
- **Vose's Alias Method**: Incurs an initial one-time table setup cost of $0.08$ seconds ($O(K)$), but executes each subsequent sample in strict $O(1)$ time with a single multiplication and array lookup, completing all $10^7$ draws in 0.38 seconds—a 37-fold speedup.

For static or infrequently updated probability vectors, the Alias Method represents the optimal industry standard.


## 2.17 Unit 2 Review and Methodological Synthesis

Unit 2 examined the transformation of uniform random variables into arbitrary non-uniform continuous and discrete distributions. We derived the Probability Integral Transform and established its exact inversion mechanics for closed-form cumulative distribution functions. We formulated the Acceptance-Rejection method of John von Neumann, proving that the expected number of proposal evaluations is exactly the bounding constant $c = \sup [f(x)/g(x)]$. We detailed Box-Muller and Marsaglia-Bray polar transformations for Gaussian generation, alongside Marsaglia and Tsang's Ziggurat algorithm, which achieves over $98.5\%$ direct interior acceptance through precomputed horizontal planar layers. For large discrete categorical spaces, we analyzed Vose's formulation of the Walker Alias Method, showing that pre-allocating an alias table and probability threshold table in $O(K)$ time permits subsequent draws in strict $O(1)$ time. Finally, we explored the Kinderman-Monahan Ratio-of-Uniforms method and fast circulant embedding for generating high-dimensional Gaussian process paths via Fast Fourier Transforms.


## 2.18 Fast Sampling from Truncated Multivariate Normals

In constrained econometric models and spatial Gaussian processes with inequality barriers, one must sample from a high-dimensional truncated Gaussian distribution $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Sigma})$ subject to linear constraints $\mathbf{a} \le \mathbf{B} \mathbf{X} \le \mathbf{b}$. Naive rejection sampling fails completely because the probability of an unconstrained Gaussian draw satisfying dozens of joint linear inequalities is virtually zero ($P \le 10^{-15}$).

Zdravko Botev (2017) developed an exact minimax tilting algorithm that combines exponential twisting with smooth unconstrained optimization to achieve acceptance rates bounded away from zero regardless of dimension $d$. Alternatively, componentwise Gibbs sampling updates each scalar coordinate $X_j$ conditional on all remaining coordinates $\mathbf{X}_{-j}$ from a univariate truncated Gaussian distribution using Robert's optimal translated exponential proposal. This allows simulation of thousands of correlated variables under strict convex polyhedral bounds in milliseconds.
