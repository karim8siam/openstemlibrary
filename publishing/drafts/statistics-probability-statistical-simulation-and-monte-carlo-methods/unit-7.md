# Unit 7: The Gibbs Sampler & Bayesian Computational Inference

In multi-parameter Bayesian inference, designing a joint proposal distribution $q(\mathbf{\theta}^* \mid \mathbf{\theta})$ that explores a complex, correlated high-dimensional parameter space efficiently via standard Metropolis-Hastings can be extraordinarily difficult. In 1984, Stuart and Donald Geman introduced the **Gibbs Sampler** in the context of spatial image processing (named after physicist Josiah Willard Gibbs). In 1990, Alan Gelfand and Adrian Smith demonstrated that the Gibbs sampler provides a universal computational engine for estimating complex Bayesian models.

Instead of proposing simultaneous moves for all $p$ parameters at once, the Gibbs sampler updates the parameters **one variable at a time** (or one block at a time) by sampling directly from the **full conditional posterior distribution** of each parameter given the current values of all other parameters and the observed data.

## 7.1 Mechanics of the Gibbs Sampler: Systematic and Random Scan

Let $\mathbf{\theta} = (\theta_1, \theta_2, \dots, \theta_p)^T \in \Theta$ be a parameter vector with joint posterior distribution $\pi(\mathbf{\theta} \mid \mathbf{y})$.
Let $\mathbf{\theta}_{-j} = (\theta_1, \dots, \theta_{j-1}, \theta_{j+1}, \dots, \theta_p)^T$ denote the subvector of all parameters excluding $\theta_j$.

The **Full Conditional Distribution** of parameter $\theta_j$ is the conditional distribution of $\theta_j$ given all remaining parameters and the data:
$$\pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) = \frac{\pi(\theta_1, \dots, \theta_p \mid \mathbf{y})}{\int \pi(\theta_1, \dots, \theta_j^*, \dots, \theta_p \mid \mathbf{y})\,d\theta_j^*} \propto \pi(\mathbf{\theta} \mid \mathbf{y})$$

### 1. The Systematic Scan Gibbs Sampler
Given an initial state $\mathbf{\theta}^{(0)} = (\theta_1^{(0)}, \dots, \theta_p^{(0)})^T$, iteration $t+1$ executes a deterministic sweep through all $p$ coordinates:
1. Sample $\theta_1^{(t+1)} \sim \pi(\theta_1 \mid \theta_2^{(t)}, \theta_3^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$.
2. Sample $\theta_2^{(t+1)} \sim \pi(\theta_2 \mid \theta_1^{(t+1)}, \theta_3^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$.
   $\dots$
$j$. Sample $\theta_j^{(t+1)} \sim \pi(\theta_j \mid \theta_1^{(t+1)}, \dots, \theta_{j-1}^{(t+1)}, \theta_{j+1}^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$.
   $\dots$
$p$. Sample $\theta_p^{(t+1)} \sim \pi(\theta_p \mid \theta_1^{(t+1)}, \dots, \theta_{p-1}^{(t+1)}, \mathbf{y})$.

Notice that as each new parameter $\theta_j^{(t+1)}$ is drawn, it is immediately used in the conditioning sets of all subsequent updates within the same iteration.

### 2. The Gibbs Sampler as Metropolis-Hastings with Acceptance $\alpha \equiv 1$
A profound theoretical insight is that the Gibbs sampler is mathematically equivalent to a multi-stage Metropolis-Hastings algorithm where the acceptance probability is **identically 100%**:

*Theorem*: Consider updating coordinate $j$ using candidate proposal $q(\mathbf{\theta}^* \mid \mathbf{\theta}) = \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \cdot I(\mathbf{\theta}_{-j}^* = \mathbf{\theta}_{-j})$.
The Metropolis-Hastings acceptance ratio is:
$$\alpha(\mathbf{\theta}, \mathbf{\theta}^*) = \min\left( 1, \; \frac{\pi(\mathbf{\theta}^* \mid \mathbf{y}) q(\mathbf{\theta} \mid \mathbf{\theta}^*)}{\pi(\mathbf{\theta} \mid \mathbf{y}) q(\mathbf{\theta}^* \mid \mathbf{\theta})} \right)$$
By definition of conditional probability:
$$\pi(\mathbf{\theta}^* \mid \mathbf{y}) = \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y})$$
$$\pi(\mathbf{\theta} \mid \mathbf{y}) = \pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y})$$
Substituting into the acceptance ratio:
$$\frac{\pi(\mathbf{\theta}^* \mid \mathbf{y}) q(\mathbf{\theta} \mid \mathbf{\theta}^*)}{\pi(\mathbf{\theta} \mid \mathbf{y}) q(\mathbf{\theta}^* \mid \mathbf{\theta})} = \frac{\left[ \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y}) \right] \left[ \pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) \right]}{\left[ \pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y}) \right] \left[ \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \right]} \equiv 1$$
Every single candidate draw is accepted with probability $\alpha \equiv 1.0$! Zero proposals are rejected.

## 7.2 Data Augmentation and Latent Variable Models

In many statistical models, the observed data likelihood $p(\mathbf{y} \mid \mathbf{\theta})$ is analytically intractable, but the complete data likelihood $p(\mathbf{y}, \mathbf{z} \mid \mathbf{\theta})$ involving unobserved **latent variables** $\mathbf{z}$ is simple and conjugate. In 1987, Martin Tanner and Wing Hung Wong formulated the **Data Augmentation Framework**.

### The Tanner-Wong Two-Step Iteration
1. **Imputation Step (I-Step)**: Sample the missing latent variables from their predictive distribution given current parameters:
   $$\mathbf{z}^{(t+1)} \sim p(\mathbf{z} \mid \mathbf{y}, \mathbf{\theta}^{(t)})$$
2. **Posterior Step (P-Step)**: Sample the parameters from their complete-data posterior distribution given augmented data:
   $$\mathbf{\theta}^{(t+1)} \sim p(\mathbf{\theta} \mid \mathbf{y}, \mathbf{z}^{(t+1)})$$
As $t \to \infty$, the marginal sequence $\{\mathbf{\theta}^{(t)}\}$ converges in distribution to the exact observed posterior $\pi(\mathbf{\theta} \mid \mathbf{y})$.

### The Albert-Chib Algorithm for Bayesian Probit Regression
Consider a binary probit regression model where observed responses $y_i \in \{0, 1\}$ follow:
$$P(y_i = 1 \mid \mathbf{x}_i, \mathbf{\beta}) = \Phi(\mathbf{x}_i^T \mathbf{\beta})$$
The likelihood function $\prod_{i=1}^n \Phi(\mathbf{x}_i^T \mathbf{\beta})^{y_i} [1 - \Phi(\mathbf{x}_i^T \mathbf{\beta})]^{1 - y_i}$ is non-conjugate with respect to a Gaussian prior $\mathbf{\beta} \sim \mathcal{N}(\mathbf{\beta}_0, \mathbf{\Sigma}_0)$.

In 1993, James Albert and Siddhartha Chib introduced continuous latent variables $Z_i \sim \mathcal{N}(\mathbf{x}_i^T \mathbf{\beta}, 1)$ such that:
$$y_i = \begin{cases} 1 & \text{if } Z_i > 0 \\ 0 & \text{if } Z_i \le 0 \end{cases}$$

Under this formulation, the full conditionals are analytically tractable standard distributions:
1. **Update Latent Variables**: For each $i = 1, \dots, n$:
   - If $y_i = 1$, sample $Z_i \sim \mathcal{N}(\mathbf{x}_i^T \mathbf{\beta}, 1)$ truncated to the positive interval $(0, \infty)$.
   - If $y_i = 0$, sample $Z_i \sim \mathcal{N}(\mathbf{x}_i^T \mathbf{\beta}, 1)$ truncated to the negative interval $(-\infty, 0]$.
2. **Update Regression Coefficients**: Conditional on continuous vector $\mathbf{Z} = (Z_1, \dots, Z_n)^T$, the model is standard linear regression $\mathbf{Z} = \mathbf{X}\mathbf{\beta} + \mathbf{\epsilon}$ with $\mathbf{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$. With prior $\mathbf{\beta} \sim \mathcal{N}(\mathbf{\beta}_0, \mathbf{\Sigma}_0)$:
   $$\mathbf{\beta} \mid \mathbf{Z}, \mathbf{y} \sim \mathcal{N}\left( (\mathbf{\Sigma}_0^{-1} + \mathbf{X}^T\mathbf{X})^{-1} (\mathbf{\Sigma}_0^{-1}\mathbf{\beta}_0 + \mathbf{X}^T\mathbf{Z}), \; (\mathbf{\Sigma}_0^{-1} + \mathbf{X}^T\mathbf{X})^{-1} \right)$$
The Albert-Chib sampler transforms non-linear categorical inference into linear Gaussian updates.

## 7.3 Gibbs Sampling for Bayesian Multiple Linear Regression

Consider the classical multiple linear regression model:
$$\mathbf{y} = \mathbf{X}\mathbf{\beta} + \mathbf{\epsilon}, \quad \mathbf{\epsilon} \sim \mathcal{N}_n(\mathbf{0}, \sigma^2 \mathbf{I}_n)$$
where $\mathbf{y} \in \mathbb{R}^n$ is the response vector, $\mathbf{X} \in \mathbb{R}^{n \times p}$ is the design matrix, $\mathbf{\beta} \in \mathbb{R}^p$ is the regression coefficient vector, and $\sigma^2 > 0$ is the residual variance.

We place independent semi-conjugate priors on $\mathbf{\beta}$ and $\sigma^2$:
- $\mathbf{\beta} \sim \mathcal{N}_p(\mathbf{\beta}_0, \mathbf{\Sigma}_0)$ (Gaussian prior).
- $\sigma^2 \sim \text{Inverse-Gamma}(a_0, b_0)$ with density $p(\sigma^2) \propto (\sigma^2)^{-(a_0 + 1)} \exp(-b_0 / \sigma^2)$.

### The Full Conditional Posterior Distributions
1. **Full Conditional of $\mathbf{\beta}$ given $\sigma^2$ and $\mathbf{y}$**:
   $$\mathbf{\beta} \mid \sigma^2, \mathbf{y} \sim \mathcal{N}_p(\mathbf{\beta}_n, \mathbf{\Sigma}_n)$$
   where:
   $$\mathbf{\Sigma}_n = \left( \mathbf{\Sigma}_0^{-1} + \frac{1}{\sigma^2} \mathbf{X}^T \mathbf{X} \right)^{-1}$$
   $$\mathbf{\beta}_n = \mathbf{\Sigma}_n \left( \mathbf{\Sigma}_0^{-1} \mathbf{\beta}_0 + \frac{1}{\sigma^2} \mathbf{X}^T \mathbf{y} \right)$$
2. **Full Conditional of $\sigma^2$ given $\mathbf{\beta}$ and $\mathbf{y}$**:
   $$\sigma^2 \mid \mathbf{\beta}, \mathbf{y} \sim \text{Inverse-Gamma}(a_n, b_n)$$
   where:
   $$a_n = a_0 + \frac{n}{2}$$
   $$b_n = b_0 + \frac{1}{2} (\mathbf{y} - \mathbf{X}\mathbf{\beta})^T (\mathbf{y} - \mathbf{X}\mathbf{\beta}) = b_0 + \frac{1}{2} \sum_{i=1}^n (y_i - \mathbf{x}_i^T\mathbf{\beta})^2$$

The Gibbs sampler alternates between drawing $\mathbf{\beta}^{(t+1)} \sim \mathcal{N}_p(\mathbf{\beta}_n, \mathbf{\Sigma}_n)$ using Cholesky factorization and drawing $\sigma^{2(t+1)} \sim \text{Inverse-Gamma}(a_n, b_n)$ via inverted Gamma sampling.

## Fully worked question 1: Gibbs Sampling for a Bivariate Gaussian Distribution

### Question
A bivariate target distribution is a zero-mean Gaussian vector $(X, Y)^T \sim \mathcal{N}_2(\mathbf{0}, \mathbf{\Sigma})$ with unit variances $\sigma_X^2 = \sigma_Y^2 = 1.0$ and correlation coefficient $\rho = 0.80$:
$$\mathbf{\Sigma} = \begin{pmatrix} 1.0 & 0.80 \\ 0.80 & 1.0 \end{pmatrix}$$
1. Derive the full conditional distributions $X \mid Y = y$ and $Y \mid X = x$.
2. Starting from initial state $(x_0, y_0) = (2.0, 2.0)$, execute two complete iterations of the systematic scan Gibbs sampler using the following standard normal draws:
   - For $x_1$: $z_{x1} = -0.50$.
   - For $y_1$: $z_{y1} = +0.25$.
   - For $x_2$: $z_{x2} = +1.10$.
   - For $y_2$: $z_{y2} = -0.40$.
3. Compute the lag-1 autocorrelation between successive states of $X$ in the Gibbs sequence.

### Solution, step 1: Derivation of the Full Conditional Distributions
For a bivariate normal vector with means 0, unit variances, and correlation $\rho$:
- The conditional distribution of $X$ given $Y = y$ is univariate Gaussian:
  $$X \mid Y = y \sim \mathcal{N}\left( \rho y, \; 1 - \rho^2 \right)$$
- Symmetrically:
  $$Y \mid X = x \sim \mathcal{N}\left( \rho x, \; 1 - \rho^2 \right)$$
Given $\rho = 0.80$:
$$\rho^2 = 0.80^2 = 0.64 \implies 1 - \rho^2 = 1 - 0.64 = 0.36$$
$$\sigma_{\text{cond}} = \sqrt{1 - \rho^2} = \sqrt{0.36} = 0.60$$
Thus, the sampling rules are:
$$X \mid Y = y \sim \mathcal{N}(0.80 y, \; 0.60^2) \implies X = 0.80 y + 0.60 Z_X$$
$$Y \mid X = x \sim \mathcal{N}(0.80 x, \; 0.60^2) \implies Y = 0.80 x + 0.60 Z_Y$$

### Solution, step 2: Execution of Two Gibbs Iterations
Starting state: $x_0 = 2.0, y_0 = 2.0$.

- **Iteration 1**:
  1. Sample $x_1 \sim \mathcal{N}(0.80 y_0, 0.60^2)$ using $z_{x1} = -0.50$:
     $$\mu_{x1} = 0.80 \times 2.0 = 1.60$$
     $$x_1 = 1.60 + 0.60 \times (-0.50) = 1.60 - 0.30 = 1.30$$
  2. Sample $y_1 \sim \mathcal{N}(0.80 x_1, 0.60^2)$ using new $x_1 = 1.30$ and $z_{y1} = +0.25$:
     $$\mu_{y1} = 0.80 \times 1.30 = 1.04$$
     $$y_1 = 1.04 + 0.60 \times (+0.25) = 1.04 + 0.15 = 1.19$$
  *State after Iteration 1*: $(x_1, y_1) = (1.30, 1.19)$.

- **Iteration 2**:
  1. Sample $x_2 \sim \mathcal{N}(0.80 y_1, 0.60^2)$ using $y_1 = 1.19$ and $z_{x2} = +1.10$:
     $$\mu_{x2} = 0.80 \times 1.19 = 0.952$$
     $$x_2 = 0.952 + 0.60 \times (+1.10) = 0.952 + 0.660 = 1.612$$
  2. Sample $y_2 \sim \mathcal{N}(0.80 x_2, 0.60^2)$ using new $x_2 = 1.612$ and $z_{y2} = -0.40$:
     $$\mu_{y2} = 0.80 \times 1.612 = 1.2896$$
     $$y_2 = 1.2896 + 0.60 \times (-0.40) = 1.2896 - 0.2400 = 1.0496$$
  *State after Iteration 2*: $(x_2, y_2) = (1.612, 1.050)$.

### Solution, step 3: Lag-1 Autocorrelation of the Sequence
Notice the recurrence relation for the $X$ sequence across full iterations:
$$X_{t+1} = \rho Y_t + \sigma_{\text{cond}} Z_{X, t+1} = \rho (\rho X_t + \sigma_{\text{cond}} Z_{Y, t}) + \sigma_{\text{cond}} Z_{X, t+1}$$
$$X_{t+1} = \rho^2 X_t + \rho \sigma_{\text{cond}} Z_{Y, t} + \sigma_{\text{cond}} Z_{X, t+1}$$
This is an autoregressive process of order 1 ($\text{AR}(1)$) with autoregressive coefficient $\phi = \rho^2$!
Therefore, the lag-1 autocorrelation between successive Gibbs iterations is:
$$\mathrm{Corr}(X_t, X_{t+1}) = \rho^2 = 0.80^2 = 0.64$$
Notice that if $\rho \to 1.0$ (extreme correlation), $\rho^2 \to 1.0$, and the Gibbs sampler moves in tiny orthogonal steps along coordinate axes, suffering extreme slow mixing.

## Fully worked question 2: Conjugate Normal-Inverse-Gamma Gibbs Sampling

### Question
A pharmaceutical quality assurance lab measures tablet dissolution time. An observed sample of $n = 10$ measurements yields:
$$\sum_{i=1}^{10} y_i = 120.0 \implies \bar{y} = 12.0, \quad \sum_{i=1}^{10} (y_i - \bar{y})^2 = 18.0$$
The data are modeled as $y_i \mid \mu, \sigma^2 \sim \mathcal{N}(\mu, \sigma^2)$.
Priors are:
- $\mu \sim \mathcal{N}(\mu_0 = 10.0, \sigma_0^2 = 4.0)$.
- $\sigma^2 \sim \text{Inverse-Gamma}(a_0 = 2.0, b_0 = 5.0)$.

1. Derive the full conditional posterior distribution formulas for $\mu \mid \sigma^2, \mathbf{y}$ and $\sigma^2 \mid \mu, \mathbf{y}$.
2. In a Gibbs sampler step, the current variance is $\sigma^{2(t)} = 2.0$. Compute the numerical mean and variance of the full conditional distribution for $\mu$.
3. If the newly sampled mean is $\mu^{(t+1)} = 11.50$, compute the updated shape $a_n$ and scale $b_n$ for the full conditional distribution of $\sigma^2$.

### Solution, step 1: Full Conditional Formulations
1. **Full Conditional of $\mu \mid \sigma^2, \mathbf{y}$**:
   Since the prior is Gaussian and likelihood is Gaussian:
   $$\mu \mid \sigma^2, \mathbf{y} \sim \mathcal{N}\left( \mu_n, \; \sigma_n^2 \right)$$
   where:
   $$\frac{1}{\sigma_n^2} = \frac{1}{\sigma_0^2} + \frac{n}{\sigma^2} \implies \sigma_n^2 = \left( \frac{1}{\sigma_0^2} + \frac{n}{\sigma^2} \right)^{-1}$$
   $$\mu_n = \sigma_n^2 \left( \frac{\mu_0}{\sigma_0^2} + \frac{n \bar{y}}{\sigma^2} \right)$$

2. **Full Conditional of $\sigma^2 \mid \mu, \mathbf{y}$**:
   Since the prior is Inverse-Gamma and likelihood is Gaussian:
   $$\sigma^2 \mid \mu, \mathbf{y} \sim \text{Inverse-Gamma}(a_n, b_n)$$
   where:
   $$a_n = a_0 + \frac{n}{2}$$
   $$b_n = b_0 + \frac{1}{2} \sum_{i=1}^n (y_i - \mu)^2$$

### Solution, step 2: Numerical Update of $\mu$ for $\sigma^2 = 2.0$
Given $n = 10, \bar{y} = 12.0, \mu_0 = 10.0, \sigma_0^2 = 4.0$, and $\sigma^2 = 2.0$:
- Posterior precision:
  $$\frac{1}{\sigma_n^2} = \frac{1}{4.0} + \frac{10}{2.0} = 0.25 + 5.00 = 5.25$$
  $$\sigma_n^2 = \frac{1}{5.25} \approx 0.190476$$
- Posterior mean:
  $$\frac{\mu_0}{\sigma_0^2} = \frac{10.0}{4.0} = 2.50$$
  $$\frac{n \bar{y}}{\sigma^2} = \frac{10 \times 12.0}{2.0} = \frac{120.0}{2.0} = 60.0$$
  $$\mu_n = 0.190476 \times (2.50 + 60.0) = 0.190476 \times 62.50 \approx 11.9048$$
*Conditional Distribution*: $\mu \mid \sigma^2 = 2.0, \mathbf{y} \sim \mathcal{N}(11.905, \; 0.1905)$.

### Solution, step 3: Numerical Update of $\sigma^2$ for $\mu = 11.50$
Given $a_0 = 2.0, b_0 = 5.0, n = 10$, and $\mu = 11.50$:
1. Updated shape parameter:
   $$a_n = a_0 + \frac{n}{2} = 2.0 + \frac{10}{2} = 2.0 + 5.0 = 7.0$$
2. Sum of squared deviations:
   $$\sum_{i=1}^{10} (y_i - \mu)^2 = \sum_{i=1}^{10} (y_i - \bar{y})^2 + n (\bar{y} - \mu)^2$$
   Given $\sum (y_i - \bar{y})^2 = 18.0$, $\bar{y} = 12.0$, and $\mu = 11.50$:
   $$n (\bar{y} - \mu)^2 = 10 \times (12.0 - 11.50)^2 = 10 \times (0.50)^2 = 10 \times 0.25 = 2.50$$
   $$\sum_{i=1}^{10} (y_i - \mu)^2 = 18.0 + 2.50 = 20.50$$
3. Updated scale parameter:
   $$b_n = b_0 + \frac{1}{2} \sum_{i=1}^{10} (y_i - \mu)^2 = 5.0 + \frac{1}{2}(20.50) = 5.0 + 10.25 = 15.25$$

*Conditional Distribution*: $\sigma^2 \mid \mu = 11.50, \mathbf{y} \sim \text{Inverse-Gamma}(a_n = 7.0, \; b_n = 15.25)$.

## Fully worked question 3: Albert-Chib Data Augmentation for Probit Regression

### Question
Consider an Albert-Chib Bayesian probit regression model with a single predictor $x$ and no intercept:
$$P(y_i = 1 \mid x_i, \beta) = \Phi(x_i \beta)$$
Prior is $\beta \sim \mathcal{N}(0, \sigma_0^2 = 10)$.
Two observations are recorded:
- Observation 1: $x_1 = 1.0, y_1 = 1$.
- Observation 2: $x_2 = 2.0, y_2 = 0$.

The Gibbs sampler is at state $\beta = 0.50$.
1. Specify the exact conditional distributions of the latent variables $Z_1$ and $Z_2$ given $\beta = 0.50$.
2. In the imputation step, pseudorandom uniform draws yield:
   - For $Z_1$: draw $U_1 = 0.400$.
   - For $Z_2$: draw $U_2 = 0.600$.
   Compute the sampled values $Z_1$ and $Z_2$ using truncated normal inversion.
3. Compute the parameters of the updated full conditional distribution $\beta \mid Z_1, Z_2$.

### Solution, step 1: Conditional Distributions of Latent Variables $Z_1, Z_2$
Under the Albert-Chib model, the latent variable is $Z_i \sim \mathcal{N}(x_i \beta, 1)$:
- For $i = 1$ ($y_1 = 1$): $Z_1 > 0$.
  Mean: $\mu_{Z1} = x_1 \beta = 1.0 \times 0.50 = 0.50$.
  $Z_1 \sim \mathcal{N}(0.50, 1)$ truncated to $(0, \infty)$.
- For $i = 2$ ($y_2 = 0$): $Z_2 \le 0$.
  Mean: $\mu_{Z2} = x_2 \beta = 2.0 \times 0.50 = 1.00$.
  $Z_2 \sim \mathcal{N}(1.00, 1)$ truncated to $(-\infty, 0]$.

### Solution, step 2: Truncated Normal Sampling via Uniform Inversion
To sample $Z \sim \mathcal{N}(\mu, 1)$ truncated to $(a, b)$:
$$Z = \mu + \Phi^{-1}\left( \Phi(a - \mu) + U \cdot [\Phi(b - \mu) - \Phi(a - \mu)] \right)$$

1. **Sampling $Z_1$ on $(0, \infty)$ with $\mu = 0.50, U_1 = 0.400$**:
   - $a = 0, b = \infty$.
   - $a - \mu = 0 - 0.50 = -0.50$.
   - $\Phi(-0.50) = 1 - \Phi(0.50) \approx 1 - 0.69146 = 0.30854$.
   - $\Phi(\infty) = 1.0$.
   - Interpolated probability:
     $$P_1 = 0.30854 + 0.400 \times (1.0 - 0.30854) = 0.30854 + 0.400 \times 0.69146 = 0.30854 + 0.27658 = 0.58512$$
   - Invert: $\Phi^{-1}(0.58512) \approx +0.2150$.
   - Sampled value:
     $$Z_1 = \mu + \Phi^{-1}(P_1) = 0.50 + 0.2150 = 0.7150$$

2. **Sampling $Z_2$ on $(-\infty, 0]$ with $\mu = 1.00, U_2 = 0.600$**:
   - $a = -\infty, b = 0$.
   - $\Phi(-\infty) = 0.0$.
   - $b - \mu = 0 - 1.00 = -1.00$.
   - $\Phi(-1.00) = 1 - \Phi(1.00) \approx 1 - 0.84134 = 0.15866$.
   - Interpolated probability:
     $$P_2 = 0.0 + 0.600 \times 0.15866 = 0.095196$$
   - Invert: $\Phi^{-1}(0.095196) \approx -1.3094$.
   - Sampled value:
     $$Z_2 = \mu + \Phi^{-1}(P_2) = 1.00 - 1.3094 = -0.3094$$

### Solution, step 3: Update of $\beta$ Conditional on $\mathbf{Z} = (0.7150, -0.3094)^T$
Conditional on $\mathbf{Z}$, the model is standard linear regression:
$$\mathbf{Z} = \mathbf{X}\beta + \mathbf{\epsilon}, \quad \mathbf{\epsilon} \sim \mathcal{N}_2(\mathbf{0}, \mathbf{I})$$
where $\mathbf{X} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1.0 \\ 2.0 \end{pmatrix}$, and prior $\beta \sim \mathcal{N}(0, \sigma_0^2 = 10)$:
- $\mathbf{X}^T \mathbf{X} = 1.0^2 + 2.0^2 = 1.0 + 4.0 = 5.0$.
- Posterior variance:
  $$\sigma_\beta^2 = \left( \frac{1}{\sigma_0^2} + \mathbf{X}^T \mathbf{X} \right)^{-1} = \left( \frac{1}{10} + 5.0 \right)^{-1} = (0.10 + 5.0)^{-1} = \frac{1}{5.10} \approx 0.19608$$
- Cross product:
  $$\mathbf{X}^T \mathbf{Z} = x_1 Z_1 + x_2 Z_2 = 1.0 \times (0.7150) + 2.0 \times (-0.3094) = 0.7150 - 0.6188 = +0.0962$$
- Posterior mean:
  $$\mu_\beta = \sigma_\beta^2 \left( \frac{\mu_0}{\sigma_0^2} + \mathbf{X}^T \mathbf{Z} \right) = 0.19608 \times (0 + 0.0962) = 0.19608 \times 0.0962 \approx +0.01886$$

*Full Conditional*: $\beta \mid \mathbf{Z}, \mathbf{y} \sim \mathcal{N}(\mu_\beta = 0.0189, \; \sigma_\beta^2 = 0.1961)$.
The step transforms non-linear categorical inference into elementary linear Gaussian regression.


## 7.9 Hamiltonian Monte Carlo (HMC) and Symplectic Integration

In high-dimensional parameter spaces ($d \ge 50$), Random Walk Metropolis and Gibbs sampling suffer from diffusive behavior: the distance traveled scales only as $\sqrt{n}$. To escape diffusion, Radford Neal (2011) adapted physical mechanics into **Hamiltonian Monte Carlo (HMC)**, originally introduced by Simon Duane, Anthony Kennedy, Brian Pendleton, and Duncan Roweth in 1987.

HMC translates Bayesian posterior sampling into the physical simulation of a particle sliding frictionless over a multi-dimensional energy potential.

### 1. The Hamiltonian Dynamical System
Let $\mathbf{q} \in \mathbb{R}^d$ represent the position vector (the parameters of interest), with potential energy equal to the negative unnormalized log-posterior:
$$U(\mathbf{q}) = -\log \pi(\mathbf{q})$$

We introduce fictitious auxiliary momentum variables $\mathbf{p} \in \mathbb{R}^d$, typically drawn from a multivariate Gaussian distribution $\mathbf{p} \sim \mathcal{N}(\mathbf{0}, \mathbf{M})$, where $\mathbf{M}$ is a symmetric positive-definite mass matrix. The kinetic energy is:
$$K(\mathbf{p}) = \frac{1}{2} \mathbf{p}^T \mathbf{M}^{-1} \mathbf{p}$$

The total energy of the physical system is the **Hamiltonian**:
$$H(\mathbf{q}, \mathbf{p}) = U(\mathbf{q}) + K(\mathbf{p}) = -\log \pi(\mathbf{q}) + \frac{1}{2} \mathbf{p}^T \mathbf{M}^{-1} \mathbf{p}$$

The time evolution of the system follows **Hamilton's equations of motion**:
$$\frac{d\mathbf{q}}{dt} = \frac{\partial H}{\partial \mathbf{p}} = \mathbf{M}^{-1} \mathbf{p}$$
$$\frac{d\mathbf{p}}{dt} = -\frac{\partial H}{\partial \mathbf{q}} = -\nabla U(\mathbf{q}) = \nabla \log \pi(\mathbf{q})$$

Three fundamental physical properties guarantee the validity of HMC:
1. **Conservation of Energy**: $\frac{dH}{dt} = \sum_i \left( \frac{\partial H}{\partial q_i} \frac{dq_i}{dt} + \frac{\partial H}{\partial p_i} \frac{dp_i}{dt} \right) = \sum_i \left( \frac{\partial H}{\partial q_i} \frac{\partial H}{\partial p_i} - \frac{\partial H}{\partial p_i} \frac{\partial H}{\partial q_i} \right) = 0$.
2. **Reversibility**: Negating the momentum $\mathbf{p} \to -\mathbf{p}$ reverses the trajectory precisely.
3. **Volume Preservation (Liouville's Theorem)**: The phase space flow $(\mathbf{q}(0), \mathbf{p}(0)) \mapsto (\mathbf{q}(t), \mathbf{p}(t))$ has a Jacobian determinant identically equal to $1.0$, meaning phase space volume is strictly conserved: $|\det(J)| = 1$.

### 2. The Symplectic Leapfrog Integrator
Because continuous differential equations cannot be solved analytically for arbitrary posteriors, HMC discretizes time into steps of size $\epsilon$ using the **Leapfrog Integrator**:
$$\mathbf{p}\left(t + \frac{\epsilon}{2}\right) = \mathbf{p}(t) - \frac{\epsilon}{2} \nabla U(\mathbf{q}(t))$$
$$\mathbf{q}(t + \epsilon) = \mathbf{q}(t) + \epsilon \mathbf{M}^{-1} \mathbf{p}\left(t + \frac{\epsilon}{2}\right)$$
$$\mathbf{p}(t + \epsilon) = \mathbf{p}\left(t + \frac{\epsilon}{2}\right) - \frac{\epsilon}{2} \nabla U(\mathbf{q}(t + \epsilon))$$

Unlike naive Euler integration (which spirals away due to numerical energy drift), the leapfrog integrator is **symplectic**: it exactly preserves an approximate "shadow Hamiltonian" $\tilde{H} = H + O(\epsilon^2)$.

After $L$ leapfrog steps from $(\mathbf{q}, \mathbf{p})$ to proposed state $(\mathbf{q}^*, \mathbf{p}^*)$, the Metropolis acceptance probability is:
$$\alpha = \min\left( 1, \exp\left( -H(\mathbf{q}^*, \mathbf{p}^*) + H(\mathbf{q}, \mathbf{p}) \right) \right) = \min\left( 1, \exp(-\Delta H) \right)$$
Because $\Delta H = O(\epsilon^2)$ is purely due to discretization error, $\alpha$ remains close to $1.0$ (typically tuned to $65\% - 80\%$) even across vast distances in hundreds of dimensions.

## 7.10 The No-U-Turn Sampler (NUTS) and Autonomous Tuning

While HMC overcomes random walk diffusion, its performance is sensitive to two hyperparameters: the step size $\epsilon$ and the trajectory length $L$. If $L$ is too small, the algorithm degenerates into random walk exploration. If $L$ is too large, the simulated particle loops back along its orbital trajectory, wasting expensive gradient evaluations.

Matthew D. Hoffman and Andrew Gelman (2014) introduced the **No-U-Turn Sampler (NUTS)** to automate trajectory termination.

### 1. The U-Turn Criterion
The trajectory should be terminated the instant the particle begins folding back on itself, meaning the Euclidean distance between the current position $\mathbf{q}$ and the initial position $\mathbf{q}_0$ stops increasing:

$$\frac{d}{dt} \frac{1}{2} \|\mathbf{q} - \mathbf{q}_0\|_2^2 < 0 \iff (\mathbf{q} - \mathbf{q}_0)^T \frac{d\mathbf{q}}{dt} < 0 \iff (\mathbf{q} - \mathbf{q}_0)^T \mathbf{p} < 0$$

### 2. Recursive Binary Tree Building
To preserve exact time-reversibility and detailed balance, NUTS builds a balanced binary tree by simulating leapfrog steps forward and backward in time with equal probability. If the sub-trajectories in either direction satisfy the U-turn condition:
$$(\mathbf{q}^+ - \mathbf{q}^-)^T \mathbf{p}^+ < 0 \quad \text{or} \quad (\mathbf{q}^+ - \mathbf{q}^-)^T \mathbf{p}^- < 0$$
where $\mathbf{q}^+$ and $\mathbf{q}^-$ are the leftmost and rightmost endpoints of the tree, trajectory expansion halts. A point is then sampled from the tree trajectory using progressive multinomial sampling.

### 3. Dual Averaging Step Size Adaptation
NUTS tunes step size $\epsilon$ during warmup using Yurii Nesterov's primal-dual subgradient method (**Dual Averaging**). The step size is adjusted at each iteration to match a target acceptance rate $\delta_{\text{target}}$ (typically $0.80$ in Stan and PyMC):
$$\bar{w}_{t+1} = \left( 1 - \frac{1}{t + t_0} \right) \bar{w}_t + \frac{1}{t + t_0} (\delta_{\text{target}} - \alpha_t)$$
$$\log \epsilon_{t+1} = \mu - \frac{\sqrt{t}}{\gamma} \bar{w}_{t+1}$$
This automated adaptation eliminates manual tuning, making NUTS the core computational engine of modern probabilistic programming.

## 7.11 Slice Sampling

Introduced by Radford M. Neal (2003), **Slice Sampling** provides an auxiliary variable MCMC method that samples from continuous distributions without requiring explicit proposal distribution tuning.

### 1. Univariate Slice Sampling
Let $f(x) \propto h(x)$ be an unnormalized target density. Introduce an auxiliary vertical variable $y \in \mathbb{R}$:
$$p(x, y) = \begin{cases} 1, & 0 \le y \le h(x) \\ 0, & \text{otherwise} \end{cases}$$
The marginal distribution of $x$ is:
$$\int_0^{h(x)} 1\,dy = h(x) \propto f(x)$$

Univariate slice sampling alternates between two steps:
1. **Vertical Slice Draw**: Given current state $x_0$, draw $y \sim \mathcal{U}(0, h(x_0))$. This defines a horizontal slice through the density:
$$S = \{ x \in \mathbb{R} : h(x) \ge y \}$$
2. **Horizontal Coordinate Draw**: Sample a new position $x_1$ uniformly from the horizontal slice set $S$.

### 2. Stepping-Out and Shrinkage Procedures
Because the exact boundaries of the slice $S$ cannot be determined analytically for general densities, Neal developed the **stepping-out** and **shrinkage** algorithms:
1. **Stepping-Out**: An initial interval $[L, R]$ of width $w$ is positioned randomly around $x_0$: $L = x_0 - U \cdot w$ and $R = L + w$ with $U \sim \mathcal{U}(0, 1)$. The interval is expanded outward in steps of size $w$ until both ends fall outside the slice ($h(L) < y$ and $h(R) < y$).
2. **Shrinkage**: A candidate point $x^*$ is proposed uniformly from $[L, R]$. If $h(x^*) \ge y$, $x^*$ is accepted. If $h(x^*) < y$, the candidate falls outside the slice; the interval $[L, R]$ is shrunk directly to $x^*$ (setting $L = x^*$ if $x^* < x_0$, or $R = x^*$ if $x^* > x_0$), and a new proposal is drawn from the narrowed interval.

Because rejected points immediately shrink the candidate interval, slice sampling adapts automatically to local curvature: the step size expands rapidly in flat plateaus and contracts automatically in steep ravines, achieving near-$100\%$ efficiency without tuning parameters.


## 7.12 Variational Inference vs. Markov Chain Monte Carlo

In modern computational statistics and machine learning, Bayesian posterior approximation is divided into two competing paradigms: **Markov Chain Monte Carlo (MCMC)** and **Variational Inference (VI)**. While MCMC approaches posterior estimation via stochastic simulation, VI recasts posterior inference as a deterministic optimization problem.

### 1. The Evidence Lower Bound (ELBO)
Let $\mathbf{x}$ be observed data and $\mathbf{z}$ be latent variables or model parameters with joint density $p(\mathbf{x}, \mathbf{z}) = p(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z})$. We specify a family of tractable approximate distributions $\mathcal{Q} = \{ q_\phi(\mathbf{z}) \}$ and search for the variational parameters $\phi^*$ that minimize the Kullback-Leibler (KL) divergence to the exact posterior:

$$\phi^* = \arg\min_\phi \mathcal{D}_{\text{KL}}(q_\phi(\mathbf{z}) \parallel p(\mathbf{z} \mid \mathbf{x})) = \arg\min_\phi \int q_\phi(\mathbf{z}) \log \left( \frac{q_\phi(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{x})} \right) d\mathbf{z}$$

Because the posterior $p(\mathbf{z} \mid \mathbf{x}) = p(\mathbf{x}, \mathbf{z}) / p(\mathbf{x})$ contains the intractable evidence $p(\mathbf{x})$, the KL divergence cannot be minimized directly. However, decomposing the marginal log-likelihood reveals:

$$\log p(\mathbf{x}) = \int q_\phi(\mathbf{z}) \log p(\mathbf{x})\,d\mathbf{z} = \int q_\phi(\mathbf{z}) \log \left( \frac{p(\mathbf{x}, \mathbf{z})}{q_\phi(\mathbf{z})} \cdot \frac{q_\phi(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{x})} \right) d\mathbf{z}$$
$$\log p(\mathbf{x}) = \underbrace{\mathbb{E}_{q_\phi}\left[ \log \frac{p(\mathbf{x}, \mathbf{z})}{q_\phi(\mathbf{z})} \right]}_{\text{ELBO}(\phi)} + \underbrace{\mathcal{D}_{\text{KL}}(q_\phi(\mathbf{z}) \parallel p(\mathbf{z} \mid \mathbf{x}))}_{\ge 0}$$

Because the KL divergence is strictly non-negative, the **Evidence Lower Bound (ELBO)** forms a rigorous lower bound on the marginal likelihood:
$$\log p(\mathbf{x}) \ge \text{ELBO}(\phi) = \mathbb{E}_{q_\phi}[\log p(\mathbf{x}, \mathbf{z})] - \mathbb{E}_{q_\phi}[\log q_\phi(\mathbf{z})]$$
Maximizing $\text{ELBO}(\phi)$ with respect to $\phi$ is mathematically identical to minimizing $\mathcal{D}_{\text{KL}}(q_\phi \parallel p(\cdot \mid \mathbf{x}))$.

### 2. Methodological Trade-Off Comparison
<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Dimension / Property</th>
<th>Markov Chain Monte Carlo (MCMC / HMC)</th>
<th>Variational Inference (VI / CAVI / SVI)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Asymptotic Guarantee</strong></td>
<td>Exact in the limit ($n \to \infty$ simulation draws). Guarantees consistent posterior estimation.</td>
<td>Inherently biased. Confined to the variational family $\mathcal{Q}$ even with infinite computation.</td>
</tr>
<tr>
<td><strong>Computational Speed</strong></td>
<td>Slow to moderate. Requires serial evaluation of thousands of sequential proposal steps.</td>
<td>Fast. Leverages numerical optimization (gradient ascent, SGD) to converge in seconds.</td>
</tr>
<tr>
<td><strong>Scalability to Big Data</strong></td>
<td>Difficult. Standard MCMC requires evaluating the likelihood over all $N$ data points at each step.</td>
<td>Seamless. Stochastic Variational Inference (SVI) evaluates mini-batches using Robbins-Monro updates.</td>
</tr>
<tr>
<td><strong>Uncertainty / Variance</strong></td>
<td>Captures full non-Gaussian geometry, multimodality, skewness, and exact parameter correlations.</td>
<td>Underestimates posterior variance; mean-field factorization assumes independence, suppressing covariances.</td>
</tr>
<tr>
<td><strong>Diagnostic Verification</strong></td>
<td>Rigorous diagnostics ($\hat{R} \le 1.01$, ESS, trace plots, divergence flags).</td>
<td>Difficult to assess error without comparing against an expensive MCMC gold standard.</td>
</tr>
</tbody>
</table>
</div>

In modern workflows, VI is routinely deployed for rapid exploratory data analysis, initial hyperparameter screening, and initializing MCMC warmup trajectories, while Hamiltonian Monte Carlo is employed for final regulatory and scientific hypothesis reporting.


## 7.13 Coupling from the Past (CFTP) and Perfect Simulation

In standard MCMC simulation, the practitioner faces an insurmountable theoretical obstacle: the Markov chain only converges to the stationary distribution $\pi$ asymptotically as $n \to \infty$. In any finite simulation of $N$ steps, the distribution of state $X_N$ is only approximately equal to $\pi$, and determining the exact warmup time required to render the remaining bias negligible is notoriously difficult.

James G. Propp and David B. Wilson (1996) shocked the probability community by inventing **Coupling from the Past (CFTP)**, an algorithm that generates **exact, unbiased, perfect draws** from the stationary distribution $\pi$ of a Markov chain in finite computational time.

### 1. Monotonicity and the Coalescence Criterion
Consider a discrete or continuous state space $\mathcal{X}$ equipped with a partial order $\preceq$, with unique minimum element $\hat{0}$ and maximum element $\hat{1}$ (such as the Ising model of ferromagnetic spins on a lattice).

Suppose the Markov transition update can be represented by a deterministic update function $\phi: \mathcal{X} \times \mathcal{U} \to \mathcal{X}$ driven by independent uniform random numbers $U_t \sim \mathcal{U}$:
$$X_{t+1} = \phi(X_t, U_t)$$
The update function is said to be **monotone** if:
$$x \preceq y \implies \phi(x, u) \preceq \phi(y, u) \quad \forall u \in \mathcal{U}$$

### 2. Why Running Forward Fails vs. Coupling From the Past
If one starts two Markov chains at time $t = 0$ from different states and runs them forward until they meet (coalesce) at time $T$, the distribution at coalescence time $T$ is **biased**: stopping at the random time $T$ selects for trajectories that coalesce rapidly, violating stationarity.

Propp and Wilson realized that the coalescence must occur at fixed time $t = 0$ by starting chains in the infinite past:
1. Fix observation time $t = 0$.
2. Choose a starting time in the past $T_1 = -1$.
3. Run chains starting from **all possible states** $x \in \mathcal{X}$ from time $T_1$ up to $t = 0$, using the random sequence $(U_{-1})$.
4. If all trajectories coalesce into a single state at $t = 0$, output that common state $X_0$.
5. If trajectories have not coalesced, double the starting horizon: $T_2 = -2, -4, -8, \dots, -2^k$.
6. **Crucial Coupling Principle**: When restarting from $T_{k+1} = -2^{k+1}$, one **must reuse the exact same random numbers** $U_t$ that were used previously for $t \in [-2^k, 0)$. Only new random numbers are drawn for the extended interval $[-2^{k+1}, -2^k)$.

*The Sandwiching Property*: Thanks to monotonicity, one does not need to simulate trajectories from all $2^N$ possible states: one only simulates the two extreme chains starting from $\hat{0}$ and $\hat{1}$. If the top chain and bottom chain coalesce by time $t = 0$:
$$X_0^{\hat{0}} = X_0^{\hat{1}} = X_0$$
then every intermediate chain is squeezed between them and must also have coalesced to $X_0$.

*Theorem (Propp-Wilson)*: The coalesced state $X_0$ is distributed **exactly according to the stationary measure $\pi$**, with zero burn-in bias and zero approximation error.


## 7.14 Stochastic Gradient Langevin Dynamics (SGLD)

When fitting Bayesian models to massive datasets containing $N = 10^7$ or $10^8$ observations, standard Hamiltonian Monte Carlo and Metropolis algorithms become computationally prohibitive: computing the gradient of the log-posterior requires evaluating $N$ terms at every leapfrog step:
$$\nabla \log \pi(\boldsymbol{\theta} \mid \mathbf{X}) = \nabla \log p(\boldsymbol{\theta}) + \sum_{i=1}^N \nabla \log p(\mathbf{x}_i \mid \boldsymbol{\theta})$$

Max Welling and Yee Whye Teh (2011) formulated **Stochastic Gradient Langevin Dynamics (SGLD)**, integrating stochastic gradient descent with continuous Langevin diffusion to enable scalable Bayesian MCMC on big data.

### 1. Mini-Batch Gradient Approximations
At step $t$, SGLD computes an unbiased stochastic estimate of the log-likelihood gradient using a small random mini-batch $S_t \subset \{1, \dots, N\}$ of size $n \ll N$ (e.g., $n = 256$):
$$\mathbf{g}_t(\boldsymbol{\theta}_t) = \nabla \log p(\boldsymbol{\theta}_t) + \frac{N}{n} \sum_{i \in S_t} \nabla \log p(\mathbf{x}_i \mid \boldsymbol{\theta}_t)$$
The parameter vector updates according to:
$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \frac{\epsilon_t}{2} \mathbf{g}_t(\boldsymbol{\theta}_t) + \boldsymbol{\eta}_t, \quad \boldsymbol{\eta}_t \sim \mathcal{N}(\mathbf{0}, \epsilon_t \mathbf{I})$$
where $\epsilon_t$ is a decaying learning rate schedule satisfying the Robbins-Monro conditions:
$$\sum_{t=1}^\infty \epsilon_t = \infty \quad \text{and} \quad \sum_{t=1}^\infty \epsilon_t^2 < \infty$$

### 2. Transition from Optimization to Posterior Sampling
In the early iterations where $\epsilon_t$ is large, the gradient drift term $\frac{\epsilon_t}{2} \mathbf{g}_t$ dominates the injected Gaussian noise $\sqrt{\epsilon_t}$, causing the algorithm to act like mini-batch SGD and rapidly descend toward high-density posterior modes.

As $t \to \infty$ and $\epsilon_t \to 0$, the mini-batch sampling noise (which scales as $\epsilon_t^2$) decays much faster than the injected thermal noise $\sqrt{\epsilon_t}$. The injected noise dominates the sub-sampling error, causing the discrete trajectory to converge weakly to the continuous Langevin diffusion whose stationary distribution is the true Bayesian posterior. SGLD eliminates the costly $O(N)$ Metropolis accept-reject step entirely, enabling Bayesian inference on big data streams.


## 7.15 Computational Laboratory: Gibbs Sampling vs. Variational Bayes in Topic Modeling

Latent Dirichlet Allocation (LDA) models the semantic composition of text corpora by assigning words to latent topics. Fitting an LDA model with $K = 50$ topics to a corpus of 100,000 documents:
- **Collapsed Gibbs Sampling (Griffiths & Steyvers)**: Iterates sequentially through every word token in the corpus. While achieving high posterior perplexity and capturing multi-word semantic subtleties, each sweep requires 45 minutes of computation, taking 15 hours to converge over 20 sweeps.
- **Stochastic Variational Inference (Hoffman et al.)**: Optimizes the variational ELBO using mini-batches of 256 documents. SVI reaches 95% of the optimal perplexity in only 12 minutes—a 75-fold reduction in wall-clock time.

This empirical comparison highlights the complementary roles of VI (for rapid discovery and real-time processing) and Gibbs/HMC (for high-precision scientific parameter quantification).


## 7.16 Unit 7 Review and Methodological Synthesis

Unit 7 focused on advanced MCMC architectures and modern Hamiltonian dynamics. We analyzed the Gibbs sampler as an exact Metropolis-Hastings scheme with acceptance probability identically equal to 1.0, examining systematic-scan and random-scan variations. We formulated Hamiltonian Monte Carlo (HMC), demonstrating how auxiliary Gaussian momentum variables transform posterior sampling into frictionless physical motion governed by Hamilton's equations. We analyzed the volume-preserving, time-reversible properties of the symplectic Leapfrog integrator and the No-U-Turn Sampler (NUTS), which automates trajectory termination via recursive binary trees and dual averaging step size adaptation. We studied Radford Neal's Slice Sampling with stepping-out and shrinkage procedures, which adaptively navigates varying posterior scales without parameter tuning. Finally, we contrasted MCMC against Variational Inference (VI) and Stochastic Gradient Langevin Dynamics (SGLD), and surveyed Propp and Wilson's Coupling from the Past (CFTP) for exact, unbiased perfect simulation.


## 7.17 Systematic Debugging of Markov Chain Monte Carlo Algorithms

When developing custom MCMC samplers or diagnosing convergence failures in probabilistic programming models, following a systematic troubleshooting hierarchy prevents widespread inference errors:

1. **Analytical Test Verification via Prior Simulation**: Before fitting empirical data, simulate synthetic datasets from known parameter priors $\boldsymbol{\theta}_0 \sim p(\boldsymbol{\theta})$ and $\mathbf{x} \sim p(\mathbf{x} \mid \boldsymbol{\theta}_0)$. Verify that the posterior credibility intervals cover the true parameters $\boldsymbol{\theta}_0$ at nominal theoretical frequencies across 1,000 independent simulation replications (Simulation-Based Calibration).
2. **Detection of Geometric Funnels via Divergent Transitions**: In Hamiltonian Monte Carlo, any single divergent transition signifies that the simulated trajectory has encountered a region of infinite curvature where numerical leapfrog integration breaks down. Reparameterizing the model from a centered formulation $\theta \sim \mathcal{N}(\mu, \sigma^2)$ to a non-centered formulation $\tilde{\theta} \sim \mathcal{N}(0, 1)$ with $\theta = \mu + \sigma \tilde{\theta}$ straightens the target geometry and eliminates divergences.
3. **Energy Bayesian Fraction of Missing Information (E-BFMI)**: In HMC, compute the energy metric:
$$\text{E-BFMI} = \frac{\sum_{t=1}^N (E_t - E_{t-1})^2}{\sum_{t=1}^N (E_t - \bar{E})^2}$$
A value of $\text{E-BFMI} < 0.3$ indicates that the momentum distribution cannot effectively explore the energy state space, diagnosing poor momentum mass matrix adaptation or heavy tail pathologies.


## 7.18 Simulated Annealing for Global Non-Convex Optimization

In structural bioinformatics, portfolio optimization with cardinality constraints, and neural architecture search, objective loss functions $f(\mathbf{x})$ exhibit complex non-convex landscapes with thousands of deceptive local minima. Deterministic gradient descent gets trapped permanently in the nearest local basin of attraction.

Scott Kirkpatrick, C. Daniel Gelatt, and Mario P. Vecchi (1983) adapted the Metropolis MCMC algorithm into **Simulated Annealing (SA)**, treating optimization as the physical process of slowly cooling molten metal to find its crystalline ground state. 

At cooling iteration $k$, a proposed move $\mathbf{x}_{\text{prop}} \sim q(\cdot \mid \mathbf{x}_k)$ is accepted with probability:
$$\alpha = \min\left( 1, \exp\left( -\frac{f(\mathbf{x}_{\text{prop}}) - f(\mathbf{x}_k)}{T_k} \right) \right)$$
When the temperature $T_k$ is high, the algorithm readily accepts uphill moves ($f(\mathbf{x}_{\text{prop}}) > f(\mathbf{x}_k)$), freely exploring the global state space. As temperature $T_k \to 0$ according to a logarithmic cooling schedule $T_k = T_0 / \log(k + 1)$ (Hajek 1988), the chain freezes into the deepest global minimum with probability approaching 1.0.
