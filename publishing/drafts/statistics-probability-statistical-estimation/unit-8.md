# Unit 8: Bayesian Estimation, Conjugacy & Loss Function Decision Theory

In classical frequentist statistics, parameters are treated as fixed, deterministic constants whose true values are unknown to the investigator. In contrast, the Bayesian paradigm treats unobserved parameters as random variables equipped with probability distributions that quantify epistemic uncertainty—the degree of belief or knowledge possessed by an investigator before and after observing empirical evidence. Grounded in the foundational writings of Thomas Bayes (1763), Pierre-Simon Laplace (1774), and formalized by Harold Jeffreys, L. J. Savage, and Abraham Wald, Bayesian estimation synthesizes prior beliefs with the likelihood of observed data via Bayes' Theorem to yield the posterior distribution. In this concluding unit of statistical estimation, we develop the mathematical machinery of Bayesian inference, explore conjugate and objective prior distributions (including Jeffreys' invariant rule), derive optimal point estimators under varied loss functions, construct Highest Posterior Density (HPD) credible regions, prove the Bernstein–von Mises asymptotic equivalence theorem, formulate empirical Bayes and James–Stein shrinkage estimation, investigate Markov Chain Monte Carlo (MCMC) algorithms, and examine Wald's Complete Class Theorem on decision-theoretic admissibility.

## 8.1 The Bayesian Paradigmatic Shift: Epistemic Uncertainty and Bayes' Theorem

In the Bayesian framework, all uncertain quantities—both observable experimental data $\mathbf{X}$ and unobservable parameters $\boldsymbol{\theta}$—are embedded within a unified joint probability space $(\mathcal{X} \times \Theta, \mathcal{F}, \mathbb{P})$.

### The Components of a Bayesian Model:
1. **The Prior Distribution**: $\pi(\boldsymbol{\theta})$ denotes the probability density function (or probability measure) defined on the parameter space $\Theta$. It formalizes all knowledge, physical domain constraints, historical experimental data, or subjective uncertainty regarding $\boldsymbol{\theta}$ prior to observing the current sample $\mathbf{X}$.
2. **The Sampling Model (Likelihood)**: $f(\mathbf{x} \mid \boldsymbol{\theta})$ represents the conditional probability density of the data $\mathbf{X} = \mathbf{x}$ given the parameter $\boldsymbol{\theta}$. When viewed as a function of $\boldsymbol{\theta}$ for fixed observed data $\mathbf{x}$, it is the likelihood function $L(\boldsymbol{\theta}; \mathbf{x})$.
3. **The Marginal Likelihood (Evidence / Normalizing Constant)**: The total integrated probability of the observed data across all candidate states of nature is:
   $$m(\mathbf{x}) = \int_\Theta f(\mathbf{x} \mid \boldsymbol{\theta}) \pi(\boldsymbol{\theta}) \, d\boldsymbol{\theta}$$
   In discrete models, the integral is replaced by countable summation. The evidence $m(\mathbf{x})$ acts as a normalizer ensuring that the posterior integrates to unity.
4. **The Posterior Distribution**: Combining prior beliefs with empirical evidence via **Bayes' Theorem** produces the conditional distribution of $\boldsymbol{\theta}$ given the observed data $\mathbf{X} = \mathbf{x}$:
   $$\pi(\boldsymbol{\theta} \mid \mathbf{x}) = \frac{f(\mathbf{x} \mid \boldsymbol{\theta}) \pi(\boldsymbol{\theta})}{m(\mathbf{x})} = \frac{f(\mathbf{x} \mid \boldsymbol{\theta}) \pi(\boldsymbol{\theta})}{\int_\Theta f(\mathbf{x} \mid \boldsymbol{\theta}) \pi(\boldsymbol{\theta}) \, d\boldsymbol{\theta}}$$

### The Proportionality Principle
Because the marginal evidence $m(\mathbf{x})$ is a deterministic constant with respect to $\boldsymbol{\theta}$ once the data $\mathbf{x}$ are observed, Bayesian inference is almost universally summarized by the fundamental proportionality:

$$\pi(\boldsymbol{\theta} \mid \mathbf{x}) \propto f(\mathbf{x} \mid \boldsymbol{\theta}) \times \pi(\boldsymbol{\theta})$$

$$\text{Posterior} \propto \text{Likelihood} \times \text{Prior}$$

The posterior distribution $\pi(\boldsymbol{\theta} \mid \mathbf{x})$ constitutes the complete, definitive answer to any Bayesian estimation problem. It encapsulates all available information regarding $\boldsymbol{\theta}$ in light of both prior knowledge and empirical observations. Any point estimate, interval estimate, or decision is derived as an optimal summary of this posterior density.

## 8.2 Prior Elicitation: Informative, Conjugate, and Objective Jeffreys' Priors

The choice of prior distribution $\pi(\boldsymbol{\theta})$ is central to Bayesian methodology. Depending on the scientific context, priors are classified into three major categories:

### 1. Informative Priors
When prior clinical trials, historical telemetry, or physical laws provide tangible quantitative information, experts calibrate hyperparameters (e.g., prior mean $\mu_0$ and prior precision $\tau_0$) to match empirical moments. Informative priors allow historical data to directly improve estimation precision in small current samples.

### 2. Vague / Diffuse Priors
When an investigator has minimal advance knowledge, they may assign a prior with immense dispersion (such as a Gaussian prior $\mathcal{N}(0, 10^6)$ or a Uniform prior on a wide interval $[-M, M]$). In such cases, the posterior distribution is dominated entirely by the likelihood function.

### 3. Objective / Non-Informative Priors (Jeffreys' Invariant Rule)
A naive approach to non-informative priors is assigning a flat, uniform prior $\pi(\theta) \propto 1$ across the parameter space (Laplace's Principle of Insufficient Reason). However, this rule suffers from a severe mathematical contradiction: **a uniform prior is not transformation-invariant**!
If $\pi_\theta(\theta) = 1$ is flat, and we reparameterize the problem by a non-linear mapping $\psi = g(\theta)$ (e.g., $\psi = \theta^2$ or $\psi = 1/\theta$), the Jacobian rule of density transformation states:

$$\pi_\psi(\psi) = \pi_\theta(g^{-1}(\psi)) \left| \frac{d\theta}{d\psi} \right| = 1 \cdot \left| (g^{-1})'(\psi) \right| \ne \text{constant}$$

The prior is non-uniform in $\psi$! Claiming total ignorance about $\theta$ mathematically forces the investigator to assert strong prior opinions about $\psi = \theta^2$.

### Theorem: Jeffreys' Invariant Prior Rule (1946)
Sir Harold Jeffreys resolved this paradox by defining an objective prior directly proportional to the square root of the Fisher Information:

$$\pi_J(\boldsymbol{\theta}) \propto \sqrt{ \det(\mathbf{I}(\boldsymbol{\theta})) }$$

where $\mathbf{I}(\boldsymbol{\theta})$ is the Fisher Information matrix per observation.

#### Proof of Invariance:
Let $\boldsymbol{\psi} = \mathbf{g}(\boldsymbol{\theta})$ be a smooth, one-to-one reparameterization with Jacobian $\mathbf{J} = \frac{\partial \boldsymbol{\theta}}{\partial \boldsymbol{\psi}}$.
From Section 2.7, Fisher Information transforms tensorially as:

$$\mathbf{I}_\psi(\boldsymbol{\psi}) = \mathbf{J}^T \mathbf{I}_\theta(\boldsymbol{\theta}) \mathbf{J}$$

Taking determinants on both sides:

$$\det(\mathbf{I}_\psi(\boldsymbol{\psi})) = \det(\mathbf{J}^T) \det(\mathbf{I}_\theta(\boldsymbol{\theta})) \det(\mathbf{J}) = [\det(\mathbf{J})]^2 \det(\mathbf{I}_\theta(\boldsymbol{\theta}))$$

Taking the square root:

$$\sqrt{\det(\mathbf{I}_\psi(\boldsymbol{\psi}))} = |\det(\mathbf{J})| \sqrt{\det(\mathbf{I}_\theta(\boldsymbol{\theta}))} = \left| \det\left( \frac{\partial \boldsymbol{\theta}}{\partial \boldsymbol{\psi}} \right) \right| \pi_J(\boldsymbol{\theta})$$

This matches the exact multivariable change-of-variables formula for probability densities!
Jeffreys' prior is **intrinsically invariant under all smooth reparameterizations of the parameter space**.
Classical Jeffreys' priors include:
- **Location parameter $\mu$ in $\mathcal{N}(\mu, \sigma^2)$**: $I(\mu) = 1/\sigma^2$ (constant), so $\pi_J(\mu) \propto 1$ (flat Lebesgue measure on $\mathbb{R}$).
- **Scale parameter $\sigma$ in $\mathcal{N}(\mu, \sigma^2)$**: $I(\sigma) = 2/\sigma^2$, so $\pi_J(\sigma) \propto 1/\sigma$ (log-uniform prior on $(0, \infty)$).
- **Binomial success probability $p$**: $I(p) = \frac{1}{p(1-p)}$, so $\pi_J(p) \propto \frac{1}{\sqrt{p(1-p)}} = \text{Beta}(1/2, 1/2)$ (arcsine prior).


### Bernardo's Objective Reference Priors in Multiparameter Models
While Jeffreys' prior $\pi_J(\boldsymbol{\theta}) \propto \sqrt{\det(\mathbf{I}(\boldsymbol{\theta}))}$ works exquisitely in single-parameter problems, it can fail catastrophically in multiparameter settings.
In a famous counterexample, Charles Stein considered the normal model:

$$X_i \sim \mathcal{N}(\mu_i, \sigma^2), \quad i = 1, 2, \dots, p$$

where the parameter of interest is the squared length $\eta = \sum_{i=1}^p \mu_i^2$.
Evaluating Jeffreys' joint prior yields $\pi_J(\mu_1, \dots, \mu_p, \sigma) \propto \sigma^{-(p+1)}$. When $p$ is large (e.g., $p = 50$), the posterior distribution for $\eta$ suffers from severe marginalization paradoxes, producing posterior credible intervals that are systematically shifted away from the true parameter value.
To overcome this defect, José-Miguel Bernardo (1979), with further developments by James Berger, formulated the theory of **Reference Priors**.
Instead of treating all parameters symmetrically, reference analysis partitions the parameters into ordered groups:

$$\boldsymbol{\theta} = (\theta_1, \theta_2, \dots, \theta_k)$$

where $\theta_1$ is the primary parameter of interest and $\theta_2, \dots, \theta_k$ are nuisance parameters.
The reference prior is derived by maximizing the expected Kullback–Leibler divergence (Shannon mutual information) between the prior and the posterior distribution:

$$\pi_R(\boldsymbol{\theta}) = \arg\max_\pi \lim_{k \to \infty} \frac{1}{k} I(\boldsymbol{\theta}; \mathbf{X}^{(k)})$$

subject to a sequence of compact nested subsets. By maximizing information flow sequentially from data to parameter, Bernardo's reference algorithm eliminates marginalization paradoxes and produces objective Bayesian credible intervals that achieve exact frequentist coverage to higher orders of asymptotic approximation.

## 8.3 Conjugate Prior Distributions: Exponential Family Algebra and Hyperparameter Updating

When evaluating the posterior distribution analytically, integrating complex likelihoods can yield intractable normalizing constants. In 1961, Howard Raiffa and Robert Schlaifer introduced the concept of **conjugate prior distributions**.

### Definition of Conjugacy
A family of prior probability distributions $\mathcal{P}_{\text{prior}}$ on $\Theta$ is said to be **conjugate** to a parametric sampling model $\mathcal{F} = \{f(\mathbf{x} \mid \boldsymbol{\theta})\}$ if for every prior $\pi(\boldsymbol{\theta}) \in \mathcal{P}_{\text{prior}}$ and every possible data realization $\mathbf{x}$, the resulting posterior distribution $\pi(\boldsymbol{\theta} \mid \mathbf{x})$ belongs to the **very same distribution family** $\mathcal{P}_{\text{prior}}$.

Under conjugacy, updating prior beliefs in light of data reduces to an algebraic update of hyperparameters:

$$\text{Prior Parameters } (\alpha_0, \beta_0) + \text{Data Evidence } (n, T(\mathbf{x})) \implies \text{Posterior Parameters } (\alpha_n, \beta_n)$$

### Conjugacy in Natural Exponential Families
A foundational theorem established by George A. Barnard and refined by Diaconis and Ylvisaker (1979) proves that **every natural exponential family admits a natural conjugate prior**.
Consider a single-parameter exponential family in canonical form:

$$f(x \mid \theta) = h(x) \exp\left( \theta T(x) - A(\theta) \right)$$

For an i.i.d. sample of size $n$, the joint likelihood is:

$$f_n(\mathbf{x} \mid \theta) = \left( \prod_{i=1}^n h(x_i) \right) \exp\left( \theta \sum_{i=1}^n T(x_i) - n A(\theta) \right)$$

Define the natural conjugate prior parameterized by hyperparameters $(n_0, t_0)$:

$$\pi(\theta \mid n_0, t_0) = K(n_0, t_0) \exp\left( \theta t_0 - n_0 A(\theta) \right)$$

Multiply prior and likelihood to obtain the posterior:

$$\pi(\theta \mid \mathbf{x}) \propto \pi(\theta \mid n_0, t_0) \times f_n(\mathbf{x} \mid \theta) \propto \exp\left( \theta \left[ t_0 + \sum_{i=1}^n T(x_i) \right] - [n_0 + n] A(\theta) \right)$$

Notice the analytical form: this is identical to the prior family with updated hyperparameters:

$$n_n = n_0 + n, \quad t_n = t_0 + \sum_{i=1}^n T(x_i)$$

The hyperparameter $n_0$ represents the **effective prior sample size**, and $t_0$ represents the **effective prior sum of observations**. Bayesian updating simply sums the pseudo-observations from the prior and the real observations from the sample!

### Canonical Conjugate Pairs:
1. **Bernoulli / Binomial Likelihood $\leftrightarrow$ Beta Prior**:
   $$p \sim \text{Beta}(\alpha_0, \beta_0) \implies p \mid X \sim \text{Beta}(\alpha_0 + X, \, \beta_0 + n - X)$$
2. **Poisson Likelihood $\leftrightarrow$ Gamma Prior**:
   $$\lambda \sim \text{Gamma}(\alpha_0, \beta_0) \implies \lambda \mid \mathbf{X} \sim \text{Gamma}\left(\alpha_0 + \sum X_i, \, \beta_0 + n\right)$$
3. **Normal Likelihood (Mean unknown, variance $\sigma_0^2$ known) $\leftrightarrow$ Normal Prior**:
   $$\mu \sim \mathcal{N}(\mu_0, \sigma_0^2 / n_0) \implies \mu \mid \mathbf{X} \sim \mathcal{N}\left( \frac{n_0 \mu_0 + n \bar{X}}{n_0 + n}, \, \frac{\sigma_0^2}{n_0 + n} \right)$$
4. **Exponential / Gamma Likelihood (Scale unknown) $\leftrightarrow$ Inverse-Gamma Prior**:
   $$\theta \sim \text{Inv-Gamma}(\alpha_0, \beta_0) \implies \theta \mid \mathbf{X} \sim \text{Inv-Gamma}\left(\alpha_0 + n, \, \beta_0 + \sum X_i\right)$$

## 8.4 Bayesian Point Estimation: Posterior Expected Loss and Bayes Risk

How does a Bayesian extract an optimal single numerical point estimate $\hat{\theta}$ from the full posterior distribution $\pi(\theta \mid \mathbf{x})$? In Bayesian decision theory, point estimation is formalized as a statistical game against nature.

### The Decision-Theoretic Framework
Let $\mathcal{A} \subseteq \mathbb{R}$ denote the action space (the set of possible point estimates $a = \hat{\theta}$).
Let $L(\theta, a)$ be a designated **loss function** measuring the economic or scientific penalty incurred by choosing estimate $a$ when the true state of nature is $\theta$.
The **Posterior Expected Loss** (or posterior risk) of an action $a$ given observed data $\mathbf{x}$ is:

$$\rho(a, \mathbf{x}) = \mathbb{E}_{\theta \mid \mathbf{x}}[L(\theta, a)] = \int_\Theta L(\theta, a) \pi(\theta \mid \mathbf{x}) \, d\theta$$

The **Bayes Point Estimator** $\hat{\theta}_{\text{Bayes}}(\mathbf{x})$ is the decision rule that minimizes the posterior expected loss for the realized sample $\mathbf{x}$:

$$\hat{\theta}_{\text{Bayes}}(\mathbf{x}) = \arg\min_{a \in \mathcal{A}} \rho(a, \mathbf{x}) = \arg\min_{a \in \mathcal{A}} \int_\Theta L(\theta, a) \pi(\theta \mid \mathbf{x}) \, d\theta$$

### Integrated Bayes Risk
Prior to data collection, the overall expected risk of an estimation rule $\delta(\mathbf{X})$ across all conceivable data realizations and parameter values is the **Bayes Risk**:

$$r(\pi, \delta) = \mathbb{E}_{\mathbf{X}, \theta}[L(\theta, \delta(\mathbf{X}))] = \int_\Theta \left( \int_\mathcal{X} L(\theta, \delta(\mathbf{x})) f(\mathbf{x} \mid \theta) \, d\mathbf{x} \right) \pi(\theta) \, d\theta$$

By Fubini's Theorem, interchanging the order of integration reveals that minimizing $r(\pi, \delta)$ globally across all decision rules $\delta$ is mathematically achieved by minimizing the posterior expected loss $\rho(a, \mathbf{x})$ pointwise for each individual observed dataset $\mathbf{x}$.

## 8.5 Optimal Point Estimators under Standard Loss Functions

The choice of loss function $L(\theta, a)$ dictates the optimal summary of the posterior distribution:

### 1. Squared Error Loss $\implies$ Posterior Mean
Let $L(\theta, a) = (a - \theta)^2$.
The posterior expected loss is:

$$\rho(a, \mathbf{x}) = \mathbb{E}_{\theta \mid \mathbf{x}}[(a - \theta)^2] = \int_\Theta (a - \theta)^2 \pi(\theta \mid \mathbf{x}) \, d\theta$$

Differentiating with respect to $a$ and setting to zero:

$$\frac{d\rho}{da} = 2 \int_\Theta (a - \theta) \pi(\theta \mid \mathbf{x}) \, d\theta = 2 a \int_\Theta \pi(\theta \mid \mathbf{x}) \, d\theta - 2 \int_\Theta \theta \pi(\theta \mid \mathbf{x}) \, d\theta = 0$$

Since $\int \pi(\theta \mid \mathbf{x}) \, d\theta = 1$:

$$2 a - 2 \mathbb{E}[\theta \mid \mathbf{x}] = 0 \implies a^* = \mathbb{E}[\theta \mid \mathbf{x}]$$

The second derivative is $\frac{d^2\rho}{da^2} = 2 > 0$, confirming a unique global minimum.
**Theorem:** Under Squared Error Loss, the optimal Bayes point estimator is uniquely the **Posterior Mean**:

$$\hat{\theta}_{\text{SEL}} = \mathbb{E}[\theta \mid \mathbf{X}] = \int_\Theta \theta \, \pi(\theta \mid \mathbf{X}) \, d\theta$$

### 2. Absolute Error Loss $\implies$ Posterior Median
Let $L(\theta, a) = |a - \theta|$.
The posterior expected loss is:

$$\rho(a, \mathbf{x}) = \int_{-\infty}^a (a - \theta) \pi(\theta \mid \mathbf{x}) \, d\theta + \int_a^\infty (\theta - a) \pi(\theta \mid \mathbf{x}) \, d\theta$$

Differentiating with respect to $a$ via Leibniz's rule:

$$\frac{d\rho}{da} = \int_{-\infty}^a \pi(\theta \mid \mathbf{x}) \, d\theta - \int_a^\infty \pi(\theta \mid \mathbf{x}) \, d\theta = \mathbb{P}(\theta \le a \mid \mathbf{x}) - \mathbb{P}(\theta > a \mid \mathbf{x})$$

Setting the derivative to zero:

$$\mathbb{P}(\theta \le a \mid \mathbf{x}) = \mathbb{P}(\theta > a \mid \mathbf{x}) = \frac{1}{2}$$

**Theorem:** Under Absolute Error Loss, the optimal Bayes point estimator is the **Posterior Median**:

$$\hat{\theta}_{\text{AEL}} = \text{Median}(\pi(\theta \mid \mathbf{X}))$$

### 3. Zero-One Loss $\implies$ Maximum A Posteriori (MAP) Mode
Let $L_\epsilon(\theta, a) = \begin{cases} 0 & \text{if } |a - \theta| \le \epsilon \\ 1 & \text{if } |a - \theta| > \epsilon \end{cases}$.
Taking the limit as the tolerance width $\epsilon \to 0^+$:
Minimizing posterior loss is equivalent to maximizing the posterior probability mass in an infinitesimal neighborhood around $a$.
**Theorem:** Under Zero-One Loss, the optimal Bayes estimator is the **Maximum A Posteriori (MAP) Estimator** (the mode of the posterior):

$$\hat{\theta}_{\text{MAP}} = \arg\max_{\theta \in \Theta} \pi(\theta \mid \mathbf{X}) = \arg\max_{\theta \in \Theta} [f(\mathbf{X} \mid \theta) \pi(\theta)]$$

Notice that if the prior is flat ($\pi(\theta) \propto 1$), the MAP estimator coincides identically with the Maximum Likelihood Estimator ($\hat{\theta}_{\text{MAP}} = \hat{\theta}_{\text{MLE}}$)!


### Asymmetric Loss Functions: The LINEX Loss Model
In engineering risk analysis and financial portfolio management, the consequences of overestimation and underestimation are rarely symmetric. For example:
- In dam design, underestimating the 100-year flood level leads to catastrophic structural overtopping and loss of life. Overestimating the flood level merely leads to modest financial expenditure in building a higher concrete wall.
- In pharmaceutical manufacturing, underestimating toxic contaminant concentrations is fatal; overestimating causes harmless batch scrapping.
To accommodate directional penalties, Varian (1975) introduced the **Linear-Exponential (LINEX) Loss Function**:

$$L(\Delta) = b \left[ e^{a \Delta} - a \Delta - 1 \right], \quad a \ne 0, \, b > 0$$

where $\Delta = \hat{\theta} - \theta$ is the estimation error.
Notice the behavior of the LINEX loss:
- If $a > 0$, an overestimation error ($\Delta > 0$) causes exponential penalty growth $e^{a \Delta}$, while an underestimation error ($\Delta < 0$) causes only linear penalty growth $-a \Delta$.
- If $a < 0$, underestimation is penalized exponentially.
- As $a \to 0$, Taylor expanding $e^{a \Delta} = 1 + a \Delta + \frac{a^2 \Delta^2}{2} + \mathcal{O}(a^3)$ shows that $L(\Delta) \approx \frac{b a^2}{2} \Delta^2$, which reproduces standard squared error loss.

### Theorem: The Optimal Bayes Estimator under LINEX Loss
The posterior expected loss is:

$$\rho(a, \mathbf{x}) = b \, \mathbb{E}_{\theta \mid \mathbf{x}}[e^{a(a - \theta)}] - a b (a - \mathbb{E}[\theta \mid \mathbf{x}]) - b$$

Differentiating with respect to $a$ and setting to zero:

$$\frac{d\rho}{da} = a b \, e^{a a} \mathbb{E}[e^{-a \theta} \mid \mathbf{x}] - a b = 0 \implies e^{a a} \mathbb{E}[e^{-a \theta} \mid \mathbf{x}] = 1$$

Taking the natural logarithm on both sides:

$$a a + \ln \mathbb{E}[e^{-a \theta} \mid \mathbf{x}] = 0$$

Solving for the optimal point estimate $\hat{\theta}_{\text{LINEX}}$:

$$\hat{\theta}_{\text{LINEX}} = -\frac{1}{a} \ln \mathbb{E}_{\theta \mid \mathbf{x}}\left[ e^{-a \theta} \right]$$

Notice the extraordinary analytical beauty of this result: $\mathbb{E}[e^{-a \theta} \mid \mathbf{x}] = M_{\theta \mid \mathbf{x}}(-a)$ is precisely the **Moment Generating Function of the posterior distribution** evaluated at $-a$!
If the posterior distribution is Gaussian $\theta \mid \mathbf{x} \sim \mathcal{N}(\mu_n, \sigma_n^2)$, its MGF is $M(-a) = \exp\left( -a \mu_n + \frac{a^2 \sigma_n^2}{2} \right)$.
Substituting this into the LINEX formula:

$$\hat{\theta}_{\text{LINEX}} = -\frac{1}{a} \left( -a \mu_n + \frac{a^2 \sigma_n^2}{2} \right) = \mu_n - \frac{a}{2} \sigma_n^2$$

The optimal estimate is the posterior mean $\mu_n$ shifted by an exact risk premium $\frac{a}{2} \sigma_n^2$ proportional to the posterior variance! If underestimation is dangerous ($a < 0$), the estimator automatically shifts upward by $\frac{|a|}{2} \sigma_n^2$ to safeguard against failure.

## 8.6 Bayesian Credible Intervals vs Frequentist Confidence Intervals: HPD Regions

In Bayesian statistics, parameter uncertainty after observing data is directly communicated through **Credible Intervals**.

### Definition of a Credible Region
A subset $C \subseteq \Theta$ is called a **$100(1 - \alpha)\%$ Bayesian Credible Region** for $\boldsymbol{\theta}$ if its posterior probability equals $1 - \alpha$:

$$\mathbb{P}(\boldsymbol{\theta} \in C \mid \mathbf{x}) = \int_C \pi(\boldsymbol{\theta} \mid \mathbf{x}) \, d\boldsymbol{\theta} = 1 - \alpha$$

### Epistemological Contrast with Frequentist Intervals:
- **Frequentist Interval $[L(\mathbf{x}), U(\mathbf{x})]$**: The endpoints are random; the parameter is fixed. The probability statement $\mathbb{P}(L \le \theta \le U) = 0.95$ applies to the long-run coverage rate of the random procedure over infinite hypothetical repetitions. For a realized numerical interval $[12.4, 15.8]$, the parameter is either inside or outside.
- **Bayesian Credible Interval**: The data $\mathbf{x}$ are fixed; the parameter $\theta$ is random. The probability statement:
  $$\mathbb{P}(12.4 \le \theta \le 15.8 \mid \text{Data}) = 0.95$$
  is literally and directly true! The investigator can state that given the realized data and prior, the subjective probability that $\theta$ lies in $[12.4, 15.8]$ is exactly $95\%$.

### Highest Posterior Density (HPD) Regions
Among all possible subsets satisfying $\mathbb{P}(\theta \in C \mid \mathbf{x}) = 1 - \alpha$, which one should be chosen?
The optimal choice is the **Highest Posterior Density (HPD) Region**, which minimizes the total volume (length) of the credible set:

$$C_{\text{HPD}} = \{ \boldsymbol{\theta} \in \Theta : \pi(\boldsymbol{\theta} \mid \mathbf{x}) \ge k_\alpha \}$$

where $k_\alpha$ is the horizontal density cutoff chosen such that $\int_{C_{\text{HPD}}} \pi(\boldsymbol{\theta} \mid \mathbf{x}) \, d\boldsymbol{\theta} = 1 - \alpha$.
HPD regions possess two defining geometric properties:
1. Every parameter value inside the region has a higher posterior density than any point outside the region.
2. The HPD region achieves the **shortest possible expected volume** among all credible sets of the same nominal level $1 - \alpha$.
If the posterior distribution is symmetric and unimodal (such as Gaussian or Student's $t$), the HPD region coincides with the equal-tailed credible interval. If the posterior is skewed or bimodal, the HPD region naturally splits into disjoint intervals, reflecting multiple plausible parameter clusters.

## 8.7 Asymptotic Bernstein–von Mises Theorem (The Bayesian Central Limit Theorem)

What happens to Bayesian estimators as the sample size $n$ approaches infinity? Do prior beliefs permanently bias the scientific conclusion?

The celebrated **Bernstein–von Mises Theorem** (Laplace, 1810; Bernstein, 1917; von Mises, 1931) proves that as $n \to \infty$, the posterior distribution forgets the prior entirely and converges to a normal distribution centered at the MLE!

### Theorem: The Bernstein–von Mises Theorem
Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} P_{\theta_0}$ satisfy standard Cramér regularity conditions. Let the prior density $\pi(\theta)$ be continuous and strictly positive in an open neighborhood of the true parameter $\theta_0$ ($\pi(\theta_0) > 0$).
Let $\hat{\theta}_n$ be the Maximum Likelihood Estimator, and let $I_1(\theta_0)$ be the Fisher Information per observation.
Then the total variation distance between the posterior distribution of the localized parameter $h = \sqrt{n}(\theta - \hat{\theta}_n)$ and the standard Gaussian distribution converges to zero in probability:

$$\left\| \pi\left( \sqrt{n}(\theta - \hat{\theta}_n) \in \cdot \mid \mathbf{X} \right) - \mathcal{N}\left(0, \frac{1}{I_1(\theta_0)}\right) \right\|_{\text{TV}} \xrightarrow{P_{\theta_0}} 0 \quad \text{as } n \to \infty$$

#### Profound Implications:
1. **Prior Disappearance**: The influence of any reasonable prior $\pi(\theta)$ decays as $\mathcal{O}(1/n)$. In large samples, the prior vanishes, and data dominate the posterior completely.
2. **Asymptotic Equivalence of Frequentist and Bayesian Inference**: In large samples:
   - The Bayes posterior mean $\mathbb{E}[\theta \mid \mathbf{X}]$ converges to the MLE $\hat{\theta}$.
   - The posterior variance converges to the inverse Fisher Information $\frac{1}{n I_1(\theta_0)}$.
   - The Bayesian $95\%$ HPD credible interval converges identically to the frequentist $95\%$ Wald confidence interval!
This grand synthesis proves that frequentist and Bayesian methodologies reach identical inferential conclusions in large samples.

## 8.8 Empirical Bayes and Hierarchical Models: James–Stein Shrinkage

In classical Bayesian analysis, hyperparameters are fixed a priori. In **Empirical Bayes (EB)**, introduced by Herbert Robbins (1956), hyperparameters are estimated directly from the ensemble of observed data across multiple experimental units, enabling **borrowing of strength**.

### The James–Stein Paradox (1961)
Consider observing $p$ independent physical quantities:

$$X_i \sim \mathcal{N}(\theta_i, 1), \quad i = 1, 2, \dots, p$$

We wish to estimate the vector $\boldsymbol{\theta} = (\theta_1, \dots, \theta_p)^T$ under total squared error loss:

$$L(\boldsymbol{\theta}, \mathbf{a}) = \sum_{i=1}^p (a_i - \theta_i)^2 = \|\mathbf{a} - \boldsymbol{\theta}\|^2$$

The natural point estimator is the Maximum Likelihood Estimator (and UMVUE):

$$\hat{\boldsymbol{\theta}}_{\text{MLE}} = \mathbf{X} = (X_1, X_2, \dots, X_p)^T$$

Its expected risk is constant across all $\boldsymbol{\theta} \in \mathbb{R}^p$:

$$R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{\text{MLE}}) = \mathbb{E}[\|\mathbf{X} - \boldsymbol{\theta}\|^2] = \sum_{i=1}^p \mathbb{E}[(X_i - \theta_i)^2] = \sum_{i=1}^p 1 = p$$

For over forty years, mathematical statisticians assumed that $\mathbf{X}$ was the undisputed optimal estimator.
In 1961, Charles Stein and Willard James proved a shocking mathematical theorem that shook the foundations of mathematical statistics:
**For dimension $p \ge 3$, the Maximum Likelihood Estimator $\mathbf{X}$ is strictly inadmissible!**

### The James–Stein Shrinkage Estimator
James and Stein constructed the non-linear shrinkage estimator:

$$\hat{\boldsymbol{\theta}}_{\text{JS}} = \left( 1 - \frac{p - 2}{\|\mathbf{X}\|^2} \right) \mathbf{X} = \left( 1 - \frac{p - 2}{\sum_{i=1}^p X_i^2} \right) \begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_p \end{pmatrix}$$

Stein proved that for all $p \ge 3$ and for **every single parameter vector** $\boldsymbol{\theta} \in \mathbb{R}^p$:

$$R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{\text{JS}}) = \mathbb{E}[\|\hat{\boldsymbol{\theta}}_{\text{JS}} - \boldsymbol{\theta}\|^2] < p = R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{\text{MLE}})$$

The James–Stein estimator achieves strictly lower total mean squared error everywhere in $\mathbb{R}^p$.
The Bayesian derivation of James–Stein reveals that it is precisely an Empirical Bayes estimator: placing an exchangeable prior $\theta_i \sim \mathcal{N}(0, \tau^2)$ on the parameters and estimating the prior variance $\tau^2$ from the marginal norm $\|\mathbf{X}\|^2$ naturally produces the shrinkage factor $1 - \frac{p - 2}{\|\mathbf{X}\|^2}$. Shrinking raw estimates toward a common ensemble mean eliminates high-dimensional noise.

## 8.9 Markov Chain Monte Carlo (MCMC) Foundations: Metropolis-Hastings and Gibbs Sampling

When hierarchical or non-conjugate priors are specified, the marginal evidence $m(\mathbf{x}) = \int f(\mathbf{x} \mid \boldsymbol{\theta}) \pi(\boldsymbol{\theta}) \, d\boldsymbol{\theta}$ involves an intractable high-dimensional integral. In the 1990s, the adoption of **Markov Chain Monte Carlo (MCMC)** algorithms revolutionized applied statistics by allowing researchers to sample directly from the posterior distribution $\pi(\boldsymbol{\theta} \mid \mathbf{x})$ without ever calculating the normalizing constant $m(\mathbf{x})$.

### 1. The Metropolis–Hastings Algorithm (Metropolis et al., 1953; Hastings, 1970)
To sample from an intractable target density $\pi(\boldsymbol{\theta} \mid \mathbf{x}) = \frac{p(\boldsymbol{\theta}, \mathbf{x})}{m(\mathbf{x})}$:
At iteration $t$ with current state $\boldsymbol{\theta}^{(t)}$:
1. Draw a candidate proposal $\boldsymbol{\theta}^*$ from a proposal transition distribution $q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta}^{(t)})$.
2. Compute the **Metropolis–Hastings Acceptance Ratio**:
   $$\alpha(\boldsymbol{\theta}^{(t)}, \boldsymbol{\theta}^*) = \min\left\{ 1, \, \frac{\pi(\boldsymbol{\theta}^* \mid \mathbf{x}) q(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^*)}{\pi(\boldsymbol{\theta}^{(t)} \mid \mathbf{x}) q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta}^{(t)})} \right\} = \min\left\{ 1, \, \frac{p(\boldsymbol{\theta}^*, \mathbf{x}) q(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^*)}{p(\boldsymbol{\theta}^{(t)}, \mathbf{x}) q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta}^{(t)})} \right\}$$
   Notice that the intractable normalizer $m(\mathbf{x})$ cancels out completely!
3. Draw $U \sim \text{Uniform}(0, 1)$. If $U \le \alpha$, accept the proposal and set $\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^*$; otherwise reject and set $\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)}$.

By the detailed balance condition, the stationary distribution of the generated ergodic Markov chain $\{\boldsymbol{\theta}^{(t)}\}$ is uniquely the true posterior distribution $\pi(\boldsymbol{\theta} \mid \mathbf{x})$.

### 2. The Gibbs Sampler (Geman and Geman, 1984; Gelfand and Smith, 1990)
When the parameter vector $\boldsymbol{\theta} = (\theta_1, \dots, \theta_k)^T$ can be decomposed such that the full conditional distributions $\pi(\theta_j \mid \boldsymbol{\theta}_{-j}, \mathbf{x})$ are known standard distributions, the Gibbs sampler updates parameters cyclically one variable at a time:
- Draw $\theta_1^{(t+1)} \sim \pi(\theta_1 \mid \theta_2^{(t)}, \theta_3^{(t)}, \dots, \theta_k^{(t)}, \mathbf{x})$
- Draw $\theta_2^{(t+1)} \sim \pi(\theta_2 \mid \theta_1^{(t+1)}, \theta_3^{(t)}, \dots, \theta_k^{(t)}, \mathbf{x})$
- $\dots$
- Draw $\theta_k^{(t+1)} \sim \pi(\theta_k \mid \theta_1^{(t+1)}, \theta_2^{(t+1)}, \dots, \theta_{k-1}^{(t+1)}, \mathbf{x})$

Because proposals in Gibbs sampling are drawn directly from exact full conditionals, the acceptance probability is identically $1$ (zero rejected draws).


### MCMC Convergence Diagnostics: Gelman-Rubin $\hat{R}$ and Effective Sample Size
When executing MCMC sampling (such as Metropolis–Hastings or Gibbs sampling), the generated Markov chain requires an initial burn-in phase to reach its stationary distribution. Furthermore, successive MCMC draws are autocorrelated rather than independent.
Statisticians deploy two essential convergence diagnostics:

#### 1. The Gelman–Rubin Potential Scale Reduction Factor ($\hat{R}$)
Andrew Gelman and Donald Rubin (1992) proposed running $M \ge 3$ independent parallel chains starting from dispersed initial values.
Let $N$ denote the number of iterations per chain after discarding burn-in.
- Calculate the between-chain variance $B$:
  $$B = \frac{N}{M - 1} \sum_{m=1}^M (\bar{\theta}_m - \bar{\theta}_{\cdot\cdot})^2$$
- Calculate the average within-chain variance $W$:
  $$W = \frac{1}{M} \sum_{m=1}^M s_m^2 = \frac{1}{M(N - 1)} \sum_{m=1}^M \sum_{t=1}^N (\theta_{mt} - \bar{\theta}_m)^2$$
- The pooled marginal posterior variance estimate is:
  $$\widehat{\text{Var}}(\theta \mid \mathbf{x}) = \frac{N - 1}{N} W + \frac{1}{N} B$$
The potential scale reduction factor is:
$$\hat{R} = \sqrt{ \frac{\widehat{\text{Var}}(\theta \mid \mathbf{x})}{W} }$$
If the chains have mixed and converged to the target distribution, between-chain variance matches within-chain variance, so $\hat{R} \approx 1.0$. In modern Bayesian practice, convergence is diagnosed only when $\hat{R} < 1.05$ across all monitored parameters.

#### 2. Effective Sample Size (ESS)
Due to positive autocorrelation $\rho_k$ between successive iterations, $N$ dependent MCMC draws contain less information than $N$ independent draws.
The integrated autocorrelation time is:
$$\tau = 1 + 2 \sum_{k=1}^\infty \rho_k$$
The **Effective Sample Size (ESS)** is:
$$\text{ESS} = \frac{N}{\tau} = \frac{N}{1 + 2 \sum_{k=1}^\infty \rho_k}$$
The ESS quantifies the equivalent number of independent Monte Carlo samples generated by the chain. For reliable posterior credible intervals, practitioners demand $\text{ESS} \ge 1,000$.

## 8.10 Decision-Theoretic Admissibility: Wald's Complete Class Theorem

We conclude the mathematical foundations of statistical estimation by connecting Bayesian decision theory back to frequentist admissibility.

### Definition of Admissibility
Let $R(\theta, \delta) = \mathbb{E}_\theta[L(\theta, \delta(\mathbf{X}))]$ denote the frequentist risk function of an estimator $\delta$.
An estimator $\delta$ is said to be **inadmissible** if there exists another estimator $\delta^*$ such that:

$$R(\theta, \delta^*) \le R(\theta, \delta) \quad \forall \theta \in \Theta$$

with strict inequality $R(\theta_0, \delta^*) < R(\theta_0, \delta)$ for at least one parameter value $\theta_0$.
If no such dominating estimator $\delta^*$ exists, $\delta$ is **admissible**.

### Theorem: Wald's Complete Class Theorem (1950)
In any statistical decision problem with a compact parameter space and continuous risk function:
1. Every Bayes estimator with respect to a proper prior with full support is **admissible**.
2. **Every admissible estimator is either a Bayes estimator or the limit of a sequence of Bayes estimators.**

Wald's Complete Class Theorem establishes the absolute mathematical supremacy of Bayesian decision rules:
**If an analyst wishes to construct an optimal, non-dominated estimator in any scientific or engineering problem, that estimator must be derived as a Bayes estimator under some prior distribution!** Any estimator that cannot be represented as a Bayes rule is mathematically defective and can be improved upon.

---

## Fully worked question 1: Full Conjugate Bayesian Updating and HPD Credible Interval Derivation for Normal Mean with Unknown Variance

### Question
A precision metrology laboratory measures the thickness $\mu$ of ultra-thin gold coatings deposited onto semiconductor microchips. Measurements follow a normal distribution with unknown mean $\mu$ and unknown precision $\tau = 1/\sigma^2$:

$$X_i \sim \mathcal{N}(\mu, \tau^{-1})$$

The joint prior on $(\mu, \tau)$ is chosen from the conjugate **Normal-Gamma family**:
- Precision prior: $\tau \sim \text{Gamma}(\alpha_0, \beta_0)$ with density $\pi(\tau) = \frac{\beta_0^{\alpha_0}}{\Gamma(\alpha_0)} \tau^{\alpha_0 - 1} e^{-\beta_0 \tau}$
- Conditional mean prior: $\mu \mid \tau \sim \mathcal{N}\left(\mu_0, \frac{1}{\kappa_0 \tau}\right)$
Prior hyperparameters are set based on historical manufacturing specifications:
$\mu_0 = 50.0$ nm, $\kappa_0 = 4$ (prior effective sample size), $\alpha_0 = 3$, and $\beta_0 = 12.0$.

A new production batch yields an independent sample of $n = 16$ microchip measurements with sample mean $\bar{x} = 52.5$ nm and sample sum of squared deviations $\sum_{i=1}^{16} (x_i - \bar{x})^2 = 45.0$ nm$^2$.

1. Write down the joint prior density $\pi(\mu, \tau)$ and joint sample likelihood $L(\mu, \tau; \mathbf{x})$.
2. Derive the exact joint posterior distribution $\pi(\mu, \tau \mid \mathbf{x})$, proving that it is also a Normal-Gamma distribution, and compute the four updated posterior hyperparameters $(\mu_n, \kappa_n, \alpha_n, \beta_n)$.
3. Integrate out the precision $\tau$ to find the marginal posterior distribution $\pi(\mu \mid \mathbf{x})$. Show that the standardized variable:
   $$\frac{\mu - \mu_n}{\sqrt{\beta_n / (\kappa_n \alpha_n)}} \sim t_{2\alpha_n}$$
   follows a Student's $t$-distribution.
4. Compute the Bayes point estimate under squared error loss $\hat{\mu}_{\text{SEL}}$ and construct the exact $95\%$ Highest Posterior Density (HPD) credible interval for the gold coating thickness $\mu$, using $t_{22, 0.975} = 2.074$.

### Solution, step 1: Joint prior and likelihood
The joint prior density is the product of the conditional normal and marginal gamma priors:

$$\pi(\mu, \tau) = \pi(\mu \mid \tau) \pi(\tau) = \left[ \sqrt{\frac{\kappa_0 \tau}{2\pi}} \exp\left( -\frac{\kappa_0 \tau}{2} (\mu - \mu_0)^2 \right) \right] \left[ \frac{\beta_0^{\alpha_0}}{\Gamma(\alpha_0)} \tau^{\alpha_0 - 1} e^{-\beta_0 \tau} \right]$$

$$= C_0 \, \tau^{\alpha_0 - 1/2} \exp\left( -\tau \left[ \beta_0 + \frac{\kappa_0}{2} (\mu - \mu_0)^2 \right] \right)$$

The joint likelihood of the $n$ observations is:

$$L(\mu, \tau; \mathbf{x}) = \left( \frac{\tau}{2\pi} \right)^{n/2} \exp\left( -\frac{\tau}{2} \sum_{i=1}^n (x_i - \mu)^2 \right)$$

Expand the sum of squares: $\sum (x_i - \mu)^2 = \sum (x_i - \bar{x})^2 + n(\bar{x} - \mu)^2 = S_x + n(\bar{x} - \mu)^2$, where $S_x = \sum (x_i - \bar{x})^2$.

### Solution, step 2: Posterior derivation and hyperparameter updates
Multiply likelihood and prior to obtain the joint posterior:

$$\pi(\mu, \tau \mid \mathbf{x}) \propto \tau^{\alpha_0 + n/2 - 1/2} \exp\left( -\tau \left[ \beta_0 + \frac{1}{2} S_x + \frac{\kappa_0}{2}(\mu - \mu_0)^2 + \frac{n}{2}(\mu - \bar{x})^2 \right] \right)$$

Combine the two quadratic terms in $\mu$:

$$\kappa_0 (\mu - \mu_0)^2 + n(\mu - \bar{x})^2 = (\kappa_0 + n)\mu^2 - 2(\kappa_0 \mu_0 + n \bar{x})\mu + \kappa_0 \mu_0^2 + n \bar{x}^2$$

Complete the square in $\mu$:
Let $\kappa_n = \kappa_0 + n$ and $\mu_n = \frac{\kappa_0 \mu_0 + n \bar{x}}{\kappa_0 + n}$. Then:

$$\kappa_0 (\mu - \mu_0)^2 + n(\mu - \bar{x})^2 = \kappa_n (\mu - \mu_n)^2 + \frac{\kappa_0 n}{\kappa_0 + n} (\bar{x} - \mu_0)^2$$

Substitute this back into the exponential term:

$$\pi(\mu, \tau \mid \mathbf{x}) \propto \tau^{\alpha_n - 1/2} \exp\left( -\tau \left[ \beta_n + \frac{\kappa_n}{2}(\mu - \mu_n)^2 \right] \right)$$

where the four updated hyperparameters are:
1. **Precision degrees of freedom**: $\alpha_n = \alpha_0 + \frac{n}{2}$
2. **Mean sample weight**: $\kappa_n = \kappa_0 + n$
3. **Posterior Mean**: $\mu_n = \frac{\kappa_0 \mu_0 + n \bar{x}}{\kappa_0 + n}$
4. **Precision scale**: $\beta_n = \beta_0 + \frac{1}{2} S_x + \frac{\kappa_0 n}{2(\kappa_0 + n)} (\bar{x} - \mu_0)^2$

Now evaluate numerical values with $n = 16$, $\mu_0 = 50.0$, $\kappa_0 = 4$, $\alpha_0 = 3$, $\beta_0 = 12.0$, $\bar{x} = 52.5$, $S_x = 45.0$:
- $\kappa_n = 4 + 16 = 20$
- $\mu_n = \frac{4(50.0) + 16(52.5)}{20} = \frac{200 + 840}{20} = \frac{1040}{20} = 52.0$ nm
- $\alpha_n = 3 + \frac{16}{2} = 3 + 8 = 11$
- For $\beta_n$:
  $$\frac{\kappa_0 n}{2(\kappa_0 + n)} (\bar{x} - \mu_0)^2 = \frac{4 \times 16}{2(20)} (52.5 - 50.0)^2 = \frac{64}{40} (2.5)^2 = 1.6 \times 6.25 = 10.0$$
  $$\beta_n = 12.0 + \frac{45.0}{2} + 10.0 = 12.0 + 22.5 + 10.0 = 44.5$$

The joint posterior is strictly **Normal-Gamma** with updated parameters:
$$(\mu_n, \kappa_n, \alpha_n, \beta_n) = (52.0, \, 20, \, 11, \, 44.5)$$

### Solution, step 3: Marginal posterior distribution of $\mu$
To find the marginal posterior of $\mu$, integrate out the precision $\tau$:

$$\pi(\mu \mid \mathbf{x}) = \int_0^\infty \pi(\mu, \tau \mid \mathbf{x}) \, d\tau \propto \int_0^\infty \tau^{\alpha_n - 1/2} \exp\left( -\tau \left[ \beta_n + \frac{\kappa_n}{2}(\mu - \mu_n)^2 \right] \right) d\tau$$

Recognizing the kernel of a Gamma integral $\int_0^\infty u^{a - 1} e^{-b u} \, du = \frac{\Gamma(a)}{b^a}$:

$$\pi(\mu \mid \mathbf{x}) \propto \left[ \beta_n + \frac{\kappa_n}{2}(\mu - \mu_n)^2 \right]^{-(\alpha_n + 1/2)} \propto \left[ 1 + \frac{\kappa_n}{2\beta_n}(\mu - \mu_n)^2 \right]^{-(2\alpha_n + 1)/2}$$

Rewrite in standard Student's $t$ form with $\nu = 2\alpha_n$ degrees of freedom:

$$\pi(\mu \mid \mathbf{x}) \propto \left[ 1 + \frac{1}{\nu} \left( \frac{\mu - \mu_n}{\sigma_\mu} \right)^2 \right]^{-(\nu + 1)/2}$$

where:
- Degrees of freedom: $\nu = 2\alpha_n = 2 \times 11 = 22$
- Scale factor: $\sigma_\mu = \sqrt{\frac{\beta_n}{\kappa_n \alpha_n}}$

The marginal posterior of $\mu$ is a shifted and scaled **Student's $t$-distribution**:

$$\frac{\mu - \mu_n}{\sqrt{\frac{\beta_n}{\kappa_n \alpha_n}}} \sim t_{2\alpha_n} = t_{22}$$

### Solution, step 4: Bayes estimate and 95% HPD credible interval
1. **Bayes Point Estimate under Squared Error Loss**:
   Since the Student's $t$-distribution is symmetric about its location parameter, the posterior mean is:
   $$\hat{\mu}_{\text{SEL}} = \mathbb{E}[\mu \mid \mathbf{x}] = \mu_n = 52.0 \text{ nm}$$
2. **Scale Factor Calculation**:
   $$\sigma_\mu = \sqrt{\frac{\beta_n}{\kappa_n \alpha_n}} = \sqrt{\frac{44.5}{20 \times 11}} = \sqrt{\frac{44.5}{220}} = \sqrt{0.20227} \approx 0.44975 \text{ nm}$$
3. **95% HPD Credible Interval**:
   Because the posterior density $\pi(\mu \mid \mathbf{x})$ is symmetric and unimodal, the HPD region coincides with the equal-tailed Student's $t$ interval:
   $$\mu_n \pm t_{22, 0.975} \, \sigma_\mu$$
   With $t_{22, 0.975} = 2.074$:
   $$\text{Margin of Error} = 2.074 \times 0.44975 \approx 0.9328 \text{ nm}$$
   Endpoints:
   - Lower limit: $52.0 - 0.9328 = 51.0672$ nm
   - Upper limit: $52.0 + 0.9328 = 52.9328$ nm

The exact $95\%$ Highest Posterior Density (HPD) Credible Interval for the gold coating thickness is:

$$[51.07, \, 52.93] \text{ nm}$$

**Bayesian Interpretation:** Given the prior specifications and the $16$ observed microchip measurements, there is a literal $95\%$ probability that the true mean gold thickness $\mu$ lies between $51.07$ nm and $52.93$ nm.

---

## Fully worked question 2: Jeffreys' Prior and Posterior Dirichlet Updating for Multinomial Models

### Question
A genetic sequencing laboratory tests the distribution of four RNA nucleotide bases $\mathbf{p} = (p_A, p_C, p_G, p_U)^T$ in an engineered viral strand. The categorical counts $\mathbf{X} = (X_1, X_2, X_3, X_4)^T$ follow a Multinomial distribution $\text{Multinomial}(n, \mathbf{p})$ with probability mass function:

$$f(\mathbf{x} \mid \mathbf{p}) = \frac{n!}{\prod_{j=1}^4 x_j!} \prod_{j=1}^4 p_j^{x_j}, \quad \sum_{j=1}^4 p_j = 1, \quad \sum_{j=1}^4 x_j = n$$

1. Derive the $3 \times 3$ Fisher Information matrix $\mathbf{I}(\mathbf{p})$ using the independent parameter coordinates $(p_1, p_2, p_3)^T$ with $p_4 = 1 - p_1 - p_2 - p_3$.
2. Compute the determinant $\det(\mathbf{I}(\mathbf{p}))$ and prove that **Jeffreys' invariant prior** for the multinomial distribution is a Dirichlet distribution $\text{Dirichlet}(1/2, 1/2, 1/2, 1/2)$.
3. An RNA sequencing run of length $n = 100$ bases observes counts:
   $$\mathbf{x} = (x_A, x_C, x_G, x_U) = (35, 15, 40, 10)$$
   Derive the posterior distribution $\pi(\mathbf{p} \mid \mathbf{x})$ under Jeffreys' prior and compute the Bayes point estimate of $\mathbf{p}$ under squared error loss.
4. Compare the Bayes estimate to the Maximum Likelihood Estimate $\hat{\mathbf{p}}_{\text{MLE}}$ and explain how Jeffreys' prior performs shrinkage that protects against zero-probability estimation in sparse sequencing data.

### Solution, step 1: Fisher Information matrix derivation
Let $k = 4$. Parameterize the model using the first $k - 1 = 3$ probabilities, with $p_4 = 1 - \sum_{j=1}^3 p_j$.
The log-likelihood for a single observation is:

$$\ln f(\mathbf{x} \mid \mathbf{p}) = \sum_{j=1}^3 x_j \ln(p_j) + x_4 \ln\left( 1 - \sum_{j=1}^3 p_j \right) + \ln(n!) - \sum_{j=1}^4 \ln(x_j!)$$

Compute the first partial derivatives with respect to $p_i$ ($i = 1, 2, 3$):

$$\frac{\partial \ln f}{\partial p_i} = \frac{x_i}{p_i} - \frac{x_4}{1 - \sum_{j=1}^3 p_j} = \frac{x_i}{p_i} - \frac{x_4}{p_4}$$

Now compute the second partial derivatives:
1. Diagonal elements ($i = j$):
   $$\frac{\partial^2 \ln f}{\partial p_i^2} = -\frac{x_i}{p_i^2} - \frac{x_4}{p_4^2}$$
2. Off-diagonal elements ($i \ne j$):
   $$\frac{\partial^2 \ln f}{\partial p_i \partial p_j} = -\frac{x_4}{p_4^2}$$

Take negative expectations under $n = 1$, where $\mathbb{E}[X_j] = p_j$:
- Diagonal elements:
  $$I_{ii} = -\mathbb{E}\left[ -\frac{X_i}{p_i^2} - \frac{X_4}{p_4^2} \right] = \frac{p_i}{p_i^2} + \frac{p_4}{p_4^2} = \frac{1}{p_i} + \frac{1}{p_4}$$
- Off-diagonal elements:
  $$I_{ij} = -\mathbb{E}\left[ -\frac{X_4}{p_4^2} \right] = \frac{p_4}{p_4^2} = \frac{1}{p_4}$$

In matrix notation:

$$\mathbf{I}(\mathbf{p}) = \text{diag}\left( \frac{1}{p_1}, \frac{1}{p_2}, \frac{1}{p_3} \right) + \frac{1}{p_4} \mathbf{1} \mathbf{1}^T$$

where $\mathbf{1} = (1, 1, 1)^T$.

### Solution, step 2: Determinant and Jeffreys' Prior
Apply the Matrix Determinant Lemma: for any diagonal matrix $\mathbf{D}$ and column vector $\mathbf{u}$:

$$\det(\mathbf{D} + \mathbf{u} \mathbf{u}^T) = \det(\mathbf{D}) \left( 1 + \mathbf{u}^T \mathbf{D}^{-1} \mathbf{u} \right)$$

Here $\mathbf{D} = \text{diag}(1/p_1, 1/p_2, 1/p_3)$ and $\mathbf{u} = \frac{1}{\sqrt{p_4}} \mathbf{1}$.
- $\det(\mathbf{D}) = \frac{1}{p_1 p_2 p_3}$
- $\mathbf{u}^T \mathbf{D}^{-1} \mathbf{u} = \frac{1}{p_4} \sum_{j=1}^3 p_j = \frac{1 - p_4}{p_4} = \frac{1}{p_4} - 1$

Therefore:

$$\det(\mathbf{I}(\mathbf{p})) = \left( \frac{1}{p_1 p_2 p_3} \right) \left( 1 + \frac{1}{p_4} - 1 \right) = \frac{1}{p_1 p_2 p_3} \frac{1}{p_4} = \frac{1}{p_1 p_2 p_3 p_4}$$

Now apply Jeffreys' rule:

$$\pi_J(\mathbf{p}) \propto \sqrt{ \det(\mathbf{I}(\mathbf{p})) } = \sqrt{ \frac{1}{p_1 p_2 p_3 p_4} } = p_1^{-1/2} p_2^{-1/2} p_3^{-1/2} p_4^{-1/2}$$

Notice that this is precisely the density of a **Dirichlet distribution**:

$$\pi_J(\mathbf{p}) \propto \prod_{j=1}^4 p_j^{1/2 - 1} = \text{Dirichlet}\left( \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2} \right)$$

Jeffreys' invariant prior for the general $k$-category multinomial distribution is uniquely $\text{Dirichlet}(1/2, \dots, 1/2)$.

### Solution, step 3: Posterior distribution and Bayes estimate
The multinomial likelihood is $L(\mathbf{p}; \mathbf{x}) \propto \prod_{j=1}^4 p_j^{x_j}$.
Multiply by Jeffreys' prior:

$$\pi(\mathbf{p} \mid \mathbf{x}) \propto \left( \prod_{j=1}^4 p_j^{1/2 - 1} \right) \left( \prod_{j=1}^4 p_j^{x_j} \right) = \prod_{j=1}^4 p_j^{(x_j + 1/2) - 1}$$

The posterior distribution is also a Dirichlet distribution:

$$\mathbf{p} \mid \mathbf{x} \sim \text{Dirichlet}\left( x_1 + \frac{1}{2}, \, x_2 + \frac{1}{2}, \, x_3 + \frac{1}{2}, \, x_4 + \frac{1}{2} \right)$$

Given counts $\mathbf{x} = (35, 15, 40, 10)$ with $n = 100$:
The updated parameters are:
- $\alpha_A = 35 + 0.5 = 35.5$
- $\alpha_C = 15 + 0.5 = 15.5$
- $\alpha_G = 40 + 0.5 = 40.5$
- $\alpha_U = 10 + 0.5 = 10.5$
Total sum: $\alpha_0^* = 35.5 + 15.5 + 40.5 + 10.5 = 102.0$.

Under squared error loss, the Bayes point estimate is the **Posterior Mean**:

$$\hat{p}_{j, \text{Bayes}} = \mathbb{E}[p_j \mid \mathbf{x}] = \frac{\alpha_j}{\alpha_0^*} = \frac{x_j + 0.5}{n + 2}$$

Compute the estimates:
- $\hat{p}_A = \frac{35.5}{102.0} \approx 0.3480$
- $\hat{p}_C = \frac{15.5}{102.0} \approx 0.1520$
- $\hat{p}_G = \frac{40.5}{102.0} \approx 0.3971$
- $\hat{p}_U = \frac{10.5}{102.0} \approx 0.1029$

Check: $0.3480 + 0.1520 + 0.3971 + 0.1029 = 1.0000$.

### Solution, step 4: Comparison with MLE and zero-frequency protection
The Maximum Likelihood Estimates are simply the sample proportions $\hat{p}_{j, \text{MLE}} = \frac{x_j}{n}$:
- $\hat{p}_{A, \text{MLE}} = 0.3500$
- $\hat{p}_{C, \text{MLE}} = 0.1500$
- $\hat{p}_{G, \text{MLE}} = 0.4000$
- $\hat{p}_{U, \text{MLE}} = 0.1000$

Notice how Jeffreys' Bayes estimator shrinks every estimate slightly toward the uniform prior mean ($1/4 = 0.25$):
- High frequencies ($G, A$) are shrunk downward ($0.400 \to 0.397$, $0.350 \to 0.348$).
- Low frequencies ($C, U$) are shrunk upward ($0.150 \to 0.152$, $0.100 \to 0.103$).

**Crucial Protection in Sparse Sequencing:**
If a rare genetic mutation or rare nucleotide had $0$ counts ($x_j = 0$), the MLE would declare $\hat{p}_j = 0 / n = 0$—asserting that the variant is physically impossible! In genomic risk modeling, assigning zero probability can produce catastrophic log-loss penalties ($-\ln(0) = \infty$) when the variant appears in future patients.
Jeffreys' estimator automatically assigns pseudo-counts of $0.5$, yielding:
$$\hat{p}_j = \frac{0 + 0.5}{n + 2} > 0$$
This guarantees that all categories retain non-zero probability, providing robust regularization across high-dimensional sparse data.

---

## Fully worked question 3: James-Stein Shrinkage Estimator Derivation and Geometric Proof of Dominance over Maximum Likelihood in Dimension $p \ge 3$

### Question
An agricultural research agency monitors crop yields across $p = 10$ distinct microclimate agricultural zones. Standardized yield anomalies $\mathbf{X} = (X_1, X_2, \dots, X_{10})^T$ follow a multivariate normal distribution with unknown mean vector $\boldsymbol{\theta} = (\theta_1, \dots, \theta_{10})^T \in \mathbb{R}^{10}$ and known identity covariance matrix $\mathbf{I}_{10}$:

$$\mathbf{X} \sim \mathcal{N}_{10}(\boldsymbol{\theta}, \mathbf{I}_{10})$$

Estimation performance is evaluated under total squared error loss:

$$L(\boldsymbol{\theta}, \mathbf{a}) = \|\mathbf{a} - \boldsymbol{\theta}\|^2 = \sum_{i=1}^{10} (a_i - \theta_i)^2$$

Consider the class of shrinkage estimators:

$$\hat{\boldsymbol{\theta}}_c = \left( 1 - \frac{c}{\|\mathbf{X}\|^2} \right) \mathbf{X}$$

1. State Stein's Unbiased Risk Estimate (SURE) lemma for multivariate Gaussian vectors.
2. Using Stein's lemma, derive the exact analytical risk function $R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_c) = \mathbb{E}[\|\hat{\boldsymbol{\theta}}_c - \boldsymbol{\theta}\|^2]$ as a function of the shrinkage constant $c$, dimension $p$, and the non-centrality expectation $\mathbb{E}[1 / \|\mathbf{X}\|^2]$.
3. Find the optimal constant $c^*$ that minimizes the risk, and prove that the resulting James–Stein estimator strictly dominates the Maximum Likelihood Estimator $\hat{\boldsymbol{\theta}}_{\text{MLE}} = \mathbf{X}$ for all $\boldsymbol{\theta} \in \mathbb{R}^{10}$.
4. A realized field measurement yields norm $\|\mathbf{x}\|^2 = \sum_{i=1}^{10} x_i^2 = 32.0$. Evaluate the shrinkage factor and calculate the exact percentage reduction in Mean Squared Error achieved by James–Stein estimation when the true parameter vector is centered at the origin $\boldsymbol{\theta} = \mathbf{0}$.

### Solution, step 1: Stein's Lemma (Integration by Parts for Gaussian Distributions)
Let $\mathbf{X} \sim \mathcal{N}_p(\boldsymbol{\theta}, \sigma^2 \mathbf{I}_p)$. Let $\mathbf{g}: \mathbb{R}^p \to \mathbb{R}^p$ be an almost differentiable vector field such that $\mathbb{E}[\|\nabla \cdot \mathbf{g}(\mathbf{X})\|] < \infty$.
Charles Stein (1981) established the celebrated identity:

$$\mathbb{E}\left[ (\mathbf{X} - \boldsymbol{\theta})^T \mathbf{g}(\mathbf{X}) \right] = \sigma^2 \mathbb{E}\left[ \nabla \cdot \mathbf{g}(\mathbf{X}) \right] = \sigma^2 \mathbb{E}\left[ \sum_{i=1}^p \frac{\partial g_i(\mathbf{X})}{\partial X_i} \right]$$

### Solution, step 2: Risk derivation via Stein's Lemma
Express the shrinkage estimator as $\hat{\boldsymbol{\theta}}_c = \mathbf{X} + \mathbf{g}(\mathbf{X})$, where:

$$\mathbf{g}(\mathbf{X}) = -\frac{c}{\|\mathbf{X}\|^2} \mathbf{X}$$

The estimation error is:

$$\hat{\boldsymbol{\theta}}_c - \boldsymbol{\theta} = (\mathbf{X} - \boldsymbol{\theta}) + \mathbf{g}(\mathbf{X})$$

Compute the squared Euclidean loss:

$$\|\hat{\boldsymbol{\theta}}_c - \boldsymbol{\theta}\|^2 = \|\mathbf{X} - \boldsymbol{\theta}\|^2 + 2(\mathbf{X} - \boldsymbol{\theta})^T \mathbf{g}(\mathbf{X}) + \|\mathbf{g}(\mathbf{X})\|^2$$

Take mathematical expectations:

$$R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_c) = \mathbb{E}[\|\mathbf{X} - \boldsymbol{\theta}\|^2] + 2 \mathbb{E}[(\mathbf{X} - \boldsymbol{\theta})^T \mathbf{g}(\mathbf{X})] + \mathbb{E}[\|\mathbf{g}(\mathbf{X})\|^2]$$

Evaluate the three terms with $\sigma^2 = 1$:
1. First term: $\mathbb{E}[\|\mathbf{X} - \boldsymbol{\theta}\|^2] = \sum_{i=1}^p \text{Var}(X_i) = p$.
2. Third term:
   $$\|\mathbf{g}(\mathbf{X})\|^2 = \left\| -\frac{c}{\|\mathbf{X}\|^2} \mathbf{X} \right\|^2 = \frac{c^2}{\|\mathbf{X}\|^4} \|\mathbf{X}\|^2 = \frac{c^2}{\|\mathbf{X}\|^2}$$
3. Second term: Apply Stein's Lemma to $\mathbf{g}(\mathbf{X}) = -\frac{c}{\|\mathbf{X}\|^2} \mathbf{X}$:
   Compute the divergence $\nabla \cdot \mathbf{g}(\mathbf{X}) = \sum_{i=1}^p \frac{\partial g_i}{\partial X_i}$:
   For each component $g_i(\mathbf{X}) = -c X_i (\|\mathbf{X}\|^2)^{-1}$:
   $$\frac{\partial g_i}{\partial X_i} = -c (\|\mathbf{X}\|^2)^{-1} - c X_i (-1)(\|\mathbf{X}\|^2)^{-2} (2 X_i) = -\frac{c}{\|\mathbf{X}\|^2} + \frac{2c X_i^2}{\|\mathbf{X}\|^4}$$
   Sum across all $p$ coordinates:
   $$\sum_{i=1}^p \frac{\partial g_i}{\partial X_i} = -\frac{p c}{\|\mathbf{X}\|^2} + \frac{2c \sum_{i=1}^p X_i^2}{\|\mathbf{X}\|^4} = -\frac{p c}{\|\mathbf{X}\|^2} + \frac{2c \|\mathbf{X}\|^2}{\|\mathbf{X}\|^4} = -\frac{p c}{\|\mathbf{X}\|^2} + \frac{2c}{\|\mathbf{X}\|^2} = -\frac{c(p - 2)}{\|\mathbf{X}\|^2}$$
   By Stein's Lemma:
   $$\mathbb{E}[(\mathbf{X} - \boldsymbol{\theta})^T \mathbf{g}(\mathbf{X})] = \mathbb{E}[\nabla \cdot \mathbf{g}(\mathbf{X})] = -c(p - 2) \mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right]$$

Now combine all three terms:

$$R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_c) = p - 2c(p - 2) \mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right] + c^2 \mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right]$$

Factoring out the expectation:

$$R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_c) = p - \left[ 2c(p - 2) - c^2 \right] \mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right]$$

### Solution, step 3: Optimal shrinkage constant $c^*$ and proof of dominance
To minimize the risk $R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_c)$, we maximize the bracketed quadratic term:

$$\psi(c) = 2c(p - 2) - c^2$$

Differentiating with respect to $c$ and setting to zero:

$$\psi'(c) = 2(p - 2) - 2c = 0 \implies c^* = p - 2$$

Substitute $c^* = p - 2$ back into the risk formula:

$$R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{\text{JS}}) = p - (p - 2)^2 \mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right]$$

Notice that for $p \ge 3$:
1. $(p - 2)^2 > 0$.
2. Because $\mathbf{X} \sim \mathcal{N}_p(\boldsymbol{\theta}, \mathbf{I}_p)$, the squared norm $\|\mathbf{X}\|^2$ follows a non-central Chi-square distribution $\chi_p^2(\|\boldsymbol{\theta}\|^2)$. For $p \ge 3$, the reciprocal expectation exists and is strictly positive: $\mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right] > 0$.

Therefore, the subtracted term is **strictly positive** for every $\boldsymbol{\theta} \in \mathbb{R}^p$:

$$(p - 2)^2 \mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right] > 0 \implies R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{\text{JS}}) < p = R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{\text{MLE}})$$

This rigorously proves that the James–Stein estimator strictly dominates the Maximum Likelihood Estimator for all $p \ge 3$ across the entire parameter space!

### Solution, step 4: Numerical evaluation and percentage risk reduction
For $p = 10$, the optimal shrinkage constant is:

$$c^* = p - 2 = 10 - 2 = 8$$

The James–Stein estimator is:

$$\hat{\boldsymbol{\theta}}_{\text{JS}} = \left( 1 - \frac{8}{\|\mathbf{X}\|^2} \right) \mathbf{X}$$

Given realized norm $\|\mathbf{x}\|^2 = 32.0$:

$$\text{Shrinkage factor} = 1 - \frac{8}{32.0} = 1 - 0.25 = 0.75$$

Every component of the observed vector $\mathbf{x}$ is shrunk toward zero by $25\%$!

**Risk at $\boldsymbol{\theta} = \mathbf{0}$:**
When $\boldsymbol{\theta} = \mathbf{0}$, $\|\mathbf{X}\|^2 \sim \chi_{10}^2$ is a central Chi-square variable with $10$ degrees of freedom.
Recall the expected reciprocal of a Chi-square distribution:

$$\mathbb{E}\left[ \frac{1}{\chi_\nu^2} \right] = \frac{1}{\nu - 2} \quad \text{for } \nu > 2$$

For $\nu = 10$:

$$\mathbb{E}\left[ \frac{1}{\|\mathbf{X}\|^2} \right] = \frac{1}{10 - 2} = \frac{1}{8}$$

Substitute this into the exact risk formula:

$$R(\mathbf{0}, \hat{\boldsymbol{\theta}}_{\text{JS}}) = 10 - (10 - 2)^2 \left( \frac{1}{8} \right) = 10 - 8^2 \left( \frac{1}{8} \right) = 10 - 8 = 2$$

Compare this to the risk of the classical Maximum Likelihood Estimator:

$$R(\mathbf{0}, \hat{\boldsymbol{\theta}}_{\text{MLE}}) = p = 10$$

Compute the percentage reduction in Mean Squared Error:

$$\text{Risk Reduction} = \frac{10 - 2}{10} = \frac{8}{10} = 80\%!$$

At the origin, the James–Stein shrinkage estimator achieves an extraordinary **$80\%$ reduction in Mean Squared Error** relative to the classical MLE. Even as $\|\boldsymbol{\theta}\| \to \infty$, its risk approaches $p$ from below, guaranteeing that James–Stein estimation is strictly superior across all states of nature.
