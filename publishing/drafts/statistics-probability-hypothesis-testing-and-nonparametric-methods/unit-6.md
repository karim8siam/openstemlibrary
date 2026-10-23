# Unit 6: Goodness-of-Fit & Empirical Distribution Tests: Chi-Square, Kolmogorov-Smirnov & Lilliefors

In Units 1 through 5, our inferential framework operated within a pre-specified parametric family $\{f(x; \theta) : \theta \in \Theta\}$, where the functional form of the probability distribution—such as Gaussian, Poisson, or Exponential—was assumed known a priori, and hypothesis testing focused exclusively on constraining the finite-dimensional parameter vector $\theta$. In empirical scientific research, however, the validity of any parametric test hinges critically on whether the underlying data-generating mechanism actually belongs to the postulated distributional family. If an investigator applies a two-sample $F$-test for variances or a normal-theory likelihood ratio test to heavy-tailed or skewed observations, the nominal Type I error rate $\alpha$ can be catastrophically distorted. **Goodness-of-fit testing** addresses this deeper foundational question: given an independent and identically distributed sample $X_1, X_2, \dots, X_n$ drawn from an unknown cumulative distribution function $F(x)$ on $\mathbb{R}$, how do we test the global distributional null hypothesis $H_0 : F(x) = F_0(x)$ for all $x \in \mathbb{R}$ (a simple goodness-of-fit hypothesis) or $H_0 : F(x) \in \{F_0(x; \boldsymbol{\theta}) : \boldsymbol{\theta} \in \Theta \subseteq \mathbb{R}^s\}$ (a composite goodness-of-fit hypothesis with nuisance parameters)?

Historically and mathematically, goodness-of-fit procedures divide into two major methodological paradigms. The first paradigm, initiated by Karl Pearson in his landmark 1900 paper—widely regarded as the birth of modern mathematical statistics—discretizes the sample space into $k$ mutually exclusive cells and compares the observed cell frequencies against their theoretical multinomial expectations via quadratic forms, culminating in Pearson's $\chi^2$ test, R. A. Fisher's theorem on degrees-of-freedom reduction under efficient parameter estimation, and contingency table tests of independence, homogeneity, and stratified association (Cochran-Mantel-Haenszel). The second paradigm, developed in the 1930s by Andrey Kolmogorov, Nikolai Smirnov, Harald Cramér, and Richard von Mises, avoids arbitrary cell binning altogether by directly comparing the **Empirical Distribution Function (EDF)** $F_n(x)$ against the continuous target CDF $F_0(x)$ in function space. In this unit, we establish the rigorous asymptotic and finite-sample theory of both paradigms, including the Glivenko-Cantelli Theorem, Donsker's functional central limit theorem and the Brownian bridge limit, Kolmogorov-Smirnov supremum statistics, quadratic EDF statistics (Cramér-von Mises and Anderson-Darling), and specialized normality tests (Lilliefors and Shapiro-Wilk).

## 6.1 Karl Pearson's Chi-Square Goodness-of-Fit Test and Fisher's Degrees-of-Freedom Theorem

Let $X_1, X_2, \dots, X_n$ be i.i.d. observations from a distribution $F$, and suppose we partition the sample space $\mathcal{X}$ into $k$ mutually exclusive and exhaustive cells (categories or intervals) $C_1, C_2, \dots, C_k$ such that $\bigcup_{j=1}^k C_j = \mathcal{X}$ and $C_i \cap C_j = \emptyset$ for $i \ne j$. Let $O_j = \sum_{i=1}^n \mathbb{I}(X_i \in C_j)$ denote the observed frequency of sample observations falling into cell $C_j$, so that $\sum_{j=1}^k O_j = n$. Under a simple null hypothesis $H_0 : F = F_0$, each observation falls into cell $C_j$ with known theoretical probability:

$$p_{j0} = \mathbb{P}_{H_0}(X_i \in C_j) = \int_{C_j} dF_0(x) > 0, \quad \text{where } \sum_{j=1}^k p_{j0} = 1$$

Consequently, under $H_0$, the vector of observed cell counts $\mathbf{O} = (O_1, O_2, \dots, O_k)^\top$ follows an exact **Multinomial distribution** $\text{Multinomial}(n; p_{10}, p_{20}, \dots, p_{k0})$ with expected cell frequencies $E_j = \mathbb{E}_{H_0}[O_j] = n p_{j0}$. In 1900, Karl Pearson proposed measuring the discrepancy between the observed counts $O_j$ and expected counts $E_j$ via the weighted sum of squared residuals:

$$X^2 = \sum_{j=1}^k \frac{(O_j - E_j)^2}{E_j} = \sum_{j=1}^k \frac{(O_j - n p_{j0})^2}{n p_{j0}} = \sum_{j=1}^k \frac{O_j^2}{n p_{j0}} - n$$

Why does division by $E_j = n p_{j0}$ convert a singular multinomial covariance matrix into an exact asymptotic $\chi^2_{k-1}$ distribution? Let us prove Pearson's theorem using multivariate normal asymptotics and projection matrix algebra.

### Theorem 6.1 (Pearson's Asymptotic Chi-Square Goodness-of-Fit Theorem)
Under the simple null hypothesis $H_0 : p_j = p_{j0} > 0$ ($j = 1, \dots, k$) with $\sum_{j=1}^k p_{j0} = 1$, as the sample size $n \to \infty$, Pearson's statistic $X^2$ converges in distribution to a central Chi-Square distribution with $k - 1$ degrees of freedom:

$$X^2 = \sum_{j=1}^k \frac{(O_j - n p_{j0})^2}{n p_{j0}} \xrightarrow{d} \chi^2_{k-1}$$

Furthermore, the Generalized Likelihood Ratio Test (GLRT) statistic $G^2 = -2 \ln \Lambda = 2 \sum_{j=1}^k O_j \ln\left(\frac{O_j}{E_j}\right)$ is asymptotically equivalent to $X^2$ under $H_0$: $G^2 - X^2 \xrightarrow{P} 0$, so $G^2 \xrightarrow{d} \chi^2_{k-1}$.

#### Proof:
For each observation $i \in \{1, \dots, n\}$, define the $k$-dimensional standardized indicator vector $\mathbf{Y}_i = (Y_{i1}, \dots, Y_{ik})^\top$, where $Y_{ij} = \frac{\mathbb{I}(X_i \in C_j) - p_{j0}}{\sqrt{p_{j0}}}$. Under $H_0$, $\mathbb{E}[\mathbf{Y}_i] = \mathbf{0}$, and the covariance matrix $\boldsymbol{\Sigma} = \text{Cov}(\mathbf{Y}_i)$ has diagonal entries $\Sigma_{jj} = \frac{p_{j0}(1 - p_{j0})}{p_{j0}} = 1 - p_{j0}$ and off-diagonal entries $\Sigma_{jl} = \frac{-p_{j0} p_{l0}}{\sqrt{p_{j0} p_{l0}}} = -\sqrt{p_{j0} p_{l0}}$ for $j \ne l$.
In matrix notation, define the unit vector $\mathbf{u} = (\sqrt{p_{10}}, \sqrt{p_{20}}, \dots, \sqrt{p_{k0}})^\top \in \mathbb{R}^k$, which has Euclidean norm $\|\mathbf{u}\|^2 = \mathbf{u}^\top \mathbf{u} = \sum_{j=1}^k p_{j0} = 1$. Then the covariance matrix $\boldsymbol{\Sigma}$ takes the clean rank-$(k-1)$ projection form:

$$\boldsymbol{\Sigma} = \mathbf{I}_k - \mathbf{u} \mathbf{u}^\top$$

Notice that $\boldsymbol{\Sigma}$ is symmetric and **idempotent**:

$$\boldsymbol{\Sigma}^2 = (\mathbf{I}_k - \mathbf{u}\mathbf{u}^\top)(\mathbf{I}_k - \mathbf{u}\mathbf{u}^\top) = \mathbf{I}_k - 2\mathbf{u}\mathbf{u}^\top + \mathbf{u}(\mathbf{u}^\top\mathbf{u})\mathbf{u}^\top = \mathbf{I}_k - \mathbf{u}\mathbf{u}^\top = \boldsymbol{\Sigma}$$

Now consider the sample sum vector $\mathbf{Z}_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n \mathbf{Y}_i$, whose $j$-th coordinate is precisely $Z_{nj} = \frac{O_j - n p_{j0}}{\sqrt{n p_{j0}}}$. Notice that Pearson's statistic is simply the squared Euclidean norm of $\mathbf{Z}_n$:

$$X^2 = \sum_{j=1}^k Z_{nj}^2 = \mathbf{Z}_n^\top \mathbf{Z}_n$$

By the Multivariate Central Limit Theorem, as $n \to \infty$, $\mathbf{Z}_n \xrightarrow{d} \mathbf{Z} \sim \mathcal{N}_k(\mathbf{0}, \boldsymbol{\Sigma})$, where $\boldsymbol{\Sigma} = \mathbf{I}_k - \mathbf{u}\mathbf{u}^\top$ is an idempotent projection matrix of rank equal to its trace:

$$\text{rank}(\boldsymbol{\Sigma}) = \text{tr}(\boldsymbol{\Sigma}) = \text{tr}(\mathbf{I}_k) - \text{tr}(\mathbf{u}\mathbf{u}^\top) = k - \sum_{j=1}^k p_{j0} = k - 1$$

By the spectral theorem for quadratic forms in normal variables (since $\mathbf{Z}^\top \mathbf{Z} = \mathbf{Z}^\top \boldsymbol{\Sigma} \mathbf{Z}$ with probability $1$ because $\mathbf{u}^\top \mathbf{Z}_n = \frac{1}{\sqrt{n}}\sum_{j=1}^k (O_j - n p_{j0}) = 0$), $\mathbf{Z}_n^\top \mathbf{Z}_n \xrightarrow{d} \mathbf{Z}^\top \mathbf{Z} \sim \chi^2_{\text{rank}(\boldsymbol{\Sigma})} = \chi^2_{k-1}$. Finally, expanding $G^2 = 2 \sum_{j=1}^k O_j \ln\left(1 + \frac{O_j - E_j}{E_j}\right)$ via a second-order Taylor series $\ln(1 + \delta) = \delta - \frac{1}{2}\delta^2 + O(\delta^3)$ gives $G^2 = 2 \sum_{j=1}^k (E_j + (O_j - E_j))\left[\frac{O_j - E_j}{E_j} - \frac{(O_j - E_j)^2}{2 E_j^2} + O_p(n^{-3/2})\right] = \sum_{j=1}^k \frac{(O_j - E_j)^2}{E_j} + o_p(1) = X^2 + o_p(1)$, completing the proof.

What happens when the null hypothesis $H_0 : p_j = p_j(\boldsymbol{\theta})$ is **composite**, depending on an unknown $s$-dimensional parameter vector $\boldsymbol{\theta} = (\theta_1, \dots, \theta_s)^\top \in \Theta \subseteq \mathbb{R}^s$ ($s < k - 1$)? Karl Pearson originally believed in 1900 that replacing $p_{j0}$ by $p_j(\hat{\boldsymbol{\theta}})$ did not alter the asymptotic $\chi^2_{k-1}$ distribution! R. A. Fisher (1922, 1924) proved Pearson wrong in a monumental clash of statistical titans, showing that estimating $s$ independent parameters by **multinomial Maximum Likelihood (or Minimum Chi-Square)** projects the standardized residual vector $\hat{\mathbf{Z}}_n$ onto a lower-dimensional subspace of dimension $k - 1 - s$.

### Theorem 6.2 (Fisher's Degrees-of-Freedom Reduction Theorem and Chernoff-Lehmann Phenomenon)
Suppose the cell probabilities $p_j(\boldsymbol{\theta}) > 0$ ($j = 1, \dots, k$) are continuously differentiable functions of $\boldsymbol{\theta} \in \Theta \subseteq \mathbb{R}^s$ ($s < k - 1$) such that the $k \times s$ Jacobian matrix $\mathbf{B}(\boldsymbol{\theta})$ with entries $B_{jr}(\boldsymbol{\theta}) = \frac{1}{\sqrt{p_j(\boldsymbol{\theta})}} \frac{\partial p_j(\boldsymbol{\theta})}{\partial \theta_r}$ has full column rank $s$.
1. If $\hat{\boldsymbol{\theta}}_{\text{MLE}}$ is the **multinomial (grouped-data) Maximum Likelihood Estimator** maximizing $\sum_{j=1}^k O_j \ln p_j(\boldsymbol{\theta})$ (or the Minimum Chi-Square estimator minimizing $\sum_{j=1}^k \frac{(O_j - n p_j(\boldsymbol{\theta}))^2}{n p_j(\boldsymbol{\theta})}$), then as $n \to \infty$:
   $$X^2(\hat{\boldsymbol{\theta}}_{\text{MLE}}) = \sum_{j=1}^k \frac{\left(O_j - n p_j(\hat{\boldsymbol{\theta}}_{\text{MLE}})\right)^2}{n p_j(\hat{\boldsymbol{\theta}}_{\text{MLE}})} \xrightarrow{d} \chi^2_{k - 1 - s}$$
2. (**Chernoff-Lehmann Theorem, 1954**): If instead $\tilde{\boldsymbol{\theta}}_n$ is estimated from the **ungrouped raw data** $X_1, \dots, X_n$ before binning, then $X^2(\tilde{\boldsymbol{\theta}}_n)$ converges in distribution to a weighted sum of independent $\chi^2_1$ variables:
   $$X^2(\tilde{\boldsymbol{\theta}}_n) \xrightarrow{d} \sum_{m=1}^{k - 1 - s} W_m + \sum_{r=1}^s \lambda_r W_{k - 1 - s + r}, \quad \text{where } W_m \stackrel{\text{i.i.d.}}{\sim} \chi^2_1 \text{ and } \lambda_r \in [0, 1)$$
   Hence the limiting distribution of $X^2(\tilde{\boldsymbol{\theta}}_n)$ is stochastically **bounded between** $\chi^2_{k - 1 - s}$ and $\chi^2_{k - 1}$.

In practice, to ensure the validity of the multinomial normal approximation, **Cochran's Rule (1952, 1954)** recommends choosing bins so that **every expected cell frequency is at least $1$ ($E_j \ge 1$) and at least $80\%$ of the cells satisfy $E_j \ge 5$**; if tail cells violate this criterion, adjacent tail cells should be pooled (merging cells reduces $k$ accordingly).

## 6.2 Contingency Table Tests of Independence, Homogeneity & Stratified Association

Pearson's $\chi^2$ framework extends naturally to bivariate and multivariate categorical data arranged in **contingency tables**. Suppose a random sample of size $n$ is cross-classified according to two categorical attributes: Factor $A$ with $R$ levels (rows $i = 1, \dots, R$) and Factor $B$ with $C$ levels (columns $j = 1, \dots, C$), forming an $R \times C$ contingency table with observed cell counts $O_{ij}$, row totals $R_i = \sum_{j=1}^C O_{ij}$, column totals $C_j = \sum_{i=1}^R O_{ij}$, and grand total $n = \sum_{i=1}^R \sum_{j=1}^C O_{ij}$.

Two distinct experimental sampling designs lead to the exact same algebraic test statistic:
1. **Test of Independence (Single Multinomial Sample of size $n$)**: A single random sample of size $n$ is drawn from a bivariate population where $\pi_{ij} = \mathbb{P}(\text{Row } i, \text{Col } j)$, $\pi_{i\cdot} = \sum_{j=1}^C \pi_{ij}$, and $\pi_{\cdot j} = \sum_{i=1}^R \pi_{ij}$. We test the null hypothesis of statistical independence:
   $$H_0 : \pi_{ij} = \pi_{i\cdot} \pi_{\cdot j} \quad \text{for all } i = 1, \dots, R \text{ and } j = 1, \dots, C$$
   Here there are $k = RC$ cells, so the unconstrained multinomial has $RC - 1$ degrees of freedom. Under $H_0$, we estimate $R - 1$ independent row marginals ($\hat{\pi}_{i\cdot} = R_i / n$) and $C - 1$ independent column marginals ($\hat{\pi}_{\cdot j} = C_j / n$), so $s = (R - 1) + (C - 1)$ parameters are estimated. By Fisher's theorem, the degrees of freedom are:
   $$\text{df} = (RC - 1) - (R - 1) - (C - 1) = RC - R - C + 1 = (R - 1)(C - 1)$$
2. **Test of Homogeneity ($R$ Independent Multinomial Samples of Fixed Row Sizes $R_1, \dots, R_R$)**: Independent samples of fixed sizes $R_i$ are drawn from $R$ distinct subpopulations, and we test whether the conditional column distributions are identical across all subpopulations:
   $$H_0 : \pi_{1 \mid j} = \pi_{2 \mid j} = \dots = \pi_{R \mid j} = \pi_{\cdot j} \quad \text{for all } j = 1, \dots, C$$
   Under both designs, the MLE of the expected cell count under $H_0$ is $\hat{E}_{ij} = \frac{R_i C_j}{n}$, and Pearson's $\chi^2$ statistic is:
   $$X^2 = \sum_{i=1}^R \sum_{j=1}^C \frac{\left(O_{ij} - \hat{E}_{ij}\right)^2}{\hat{E}_{ij}} = \sum_{i=1}^R \sum_{j=1}^C \frac{\left(O_{ij} - \frac{R_i C_j}{n}\right)^2}{\frac{R_i C_j}{n}} \xrightarrow{d} \chi^2_{(R-1)(C-1)}$$

In the special case of a **$2 \times 2$ contingency table** with cell counts $(O_{11}, O_{12}; O_{21}, O_{22})$, Pearson's statistic simplifies algebraically to:

$$X^2 = \frac{n (O_{11} O_{22} - O_{12} O_{21})^2}{R_1 R_2 C_1 C_2} \xrightarrow{d} \chi^2_1$$

To improve the continuous $\chi^2_1$ approximation to the discrete hypergeometric conditional distribution (Fisher's exact test) when sample sizes are moderate, Frank Yates (1934) introduced **Yates' Continuity Correction**, which subtracts $n/2$ from the absolute cross-product difference $|O_{11} O_{22} - O_{12} O_{21}|$ (equivalent to subtracting $0.5$ from each $|O_{ij} - \hat{E}_{ij}|$):

$$X^2_{\text{Yates}} = \sum_{i=1}^2 \sum_{j=1}^2 \frac{\left( \max\left\{0, |O_{ij} - \hat{E}_{ij}| - 0.5\right\} \right)^2}{\hat{E}_{ij}} = \frac{n \left( \max\left\{0, |O_{11} O_{22} - O_{12} O_{21}| - \frac{n}{2}\right\} \right)^2}{R_1 R_2 C_1 C_2}$$

When observational studies are confounded by a third stratifying variable $Z$ with $K$ strata ($k = 1, \dots, K$, such as hospital centers or age brackets), pooling the $K$ tables crudely into a single marginal $2 \times 2$ table can induce **Simpson's Paradox**. To test conditional independence $H_0 : \psi_1 = \psi_2 = \dots = \psi_K = 1$ across $K$ stratified $2 \times 2$ tables (where $\psi_k = \frac{\pi_{11k}\pi_{22k}}{\pi_{12k}\pi_{21k}}$ is the odds ratio in stratum $k$), William Cochran (1954) and Nathan Mantel and William Haenszel (1959) developed the **Cochran-Mantel-Haenszel (CMH) Test**. Conditional on the margins $(R_{1k}, R_{2k}, C_{1k}, C_{2k}, n_k)$ in stratum $k$, the upper-left cell count $O_{11k}$ follows a central Hypergeometric distribution under $H_0$ with exact mean and variance:

$$\mu_{11k} = \mathbb{E}_{H_0}[O_{11k}] = \frac{R_{1k} C_{1k}}{n_k}, \qquad V_{11k} = \text{Var}_{H_0}(O_{11k}) = \frac{R_{1k} R_{2k} C_{1k} C_{2k}}{n_k^2 (n_k - 1)}$$

Summing the deviations $O_{11k} - \mu_{11k}$ across all $K$ independent strata yields the **Cochran-Mantel-Haenszel statistic**:

$$X^2_{\text{CMH}} = \frac{\left( \left| \sum_{k=1}^K \left( O_{11k} - \frac{R_{1k} C_{1k}}{n_k} \right) \right| - c_{\text{cc}} \right)^2}{\sum_{k=1}^K \frac{R_{1k} R_{2k} C_{1k} C_{2k}}{n_k^2 (n_k - 1)}} \xrightarrow{d} \chi^2_1$$

where $c_{\text{cc}} = 0.5$ (with continuity correction) or $0$ (uncorrected), alongside the **Mantel-Haenszel Common Odds Ratio Estimator** $\hat{\psi}_{\text{MH}} = \frac{\sum_{k=1}^K O_{11k} O_{22k} / n_k}{\sum_{k=1}^K O_{12k} O_{21k} / n_k}$.

## 6.3 The Empirical Distribution Function (EDF), Glivenko-Cantelli Theorem & Brownian Bridge

While Pearson's $\chi^2$ test is versatile for categorical and discrete data, applying it to continuous random variables $X_1, \dots, X_n$ suffers from two serious theoretical drawbacks: (1) arbitrary choice of bin boundaries $C_1, \dots, C_k$ can alter the test conclusion, and (2) grouping continuous observations into coarse intervals discards exact intra-bin ordering information and destroys statistical power against local alternatives. To preserve full information in continuous samples, we construct the **Empirical Distribution Function (EDF)** $F_n(x)$, defined for every real number $x \in \mathbb{R}$ as the proportion of sample observations less than or equal to $x$:

$$F_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i \le x) = \frac{\#\{i : X_i \le x\}}{n}, \quad -\infty < x < \infty$$

In terms of the order statistics $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$, $F_n(x)$ is a right-continuous step function (a càdlàg function in the Skorokhod space $D[-\infty, \infty]$) that jumps upward by $1/n$ at each distinct observation:

$$F_n(x) = \begin{cases} 0 & \text{if } x < X_{(1)} \\ \frac{k}{n} & \text{if } X_{(k)} \le x < X_{(k+1)} \quad (k = 1, \dots, n-1) \\ 1 & \text{if } x \ge X_{(n)} \end{cases}$$

For any fixed real number $x \in \mathbb{R}$, the indicator variable $\mathbb{I}(X_i \le x) \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(F(x))$, so the count $n F_n(x) \sim \text{Binomial}(n, F(x))$. Consequently, $F_n(x)$ is an unbiased estimator of $F(x)$ with exact pointwise moments and covariance structure:
- **Pointwise Mean and Variance**: $\mathbb{E}[F_n(x)] = F(x)$, and $\text{Var}(F_n(x)) = \frac{F(x)[1 - F(x)]}{n}$.
- **Exact Covariance Function** (for any $x, y \in \mathbb{R}$):
  $$\text{Cov}\left( F_n(x), F_n(y) \right) = \frac{F(\min(x, y)) - F(x) F(y)}{n}$$
- **Pointwise Strong Consistency and Asymptotic Normality**: By Kolmogorov's Strong Law of Large Numbers, $F_n(x) \xrightarrow{\text{a.s.}} F(x)$ for each fixed $x$, and by the Lindeberg-Lévy Central Limit Theorem, $\sqrt{n}(F_n(x) - F(x)) \xrightarrow{d} \mathcal{N}\left(0, F(x)[1 - F(x)]\right)$.

Remarkably, Valerio Glivenko and Francesco Paolo Cantelli (1933) proved that the pointwise almost-sure convergence of $F_n(x)$ to $F(x)$ is automatically **uniform across the entire real line $\mathbb{R}$**, a result celebrationally termed the *Fundamental Theorem of Mathematical Statistics*.

### Theorem 6.3 (The Glivenko-Cantelli Theorem)
Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with common cumulative distribution function $F(x)$. Define the Kolmogorov supremum distance $D_n = \|F_n - F\|_\infty = \sup_{x \in \mathbb{R}} |F_n(x) - F(x)|$. Then as $n \to \infty$, $F_n$ converges uniformly to $F$ almost surely:

$$\mathbb{P}\left( \lim_{n \to \infty} \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| = 0 \right) = 1$$

#### Proof:
Fix any integer $m \ge 1$, and partition the probability interval $[0, 1]$ into $m$ subintervals of length $1/m$ via the generalized quantile points $-\infty = x_0 < x_1 \le x_2 \le \dots \le x_{m-1} < x_m = +\infty$, where $x_j = \inf\{x \in \mathbb{R} : F(x) \ge j/m\}$ for $j = 1, \dots, m-1$. By right-continuity and monotonicity of $F$, on each open interval $(x_{j-1}, x_j)$, the oscillation of $F$ cannot exceed $1/m$: $F(x_j^-) - F(x_{j-1}) \le \frac{1}{m}$.
Now let $x \in \mathbb{R}$ be arbitrary; if $x$ lies in the open interval $(x_{j-1}, x_j)$ for some $j \in \{1, \dots, m\}$, monotonicity of both $F_n$ and $F$ implies:

$$F_n(x_{j-1}) - F(x_j^-) \le F_n(x) - F(x) \le F_n(x_j^-) - F(x_{j-1})$$

Since $F(x_j^-) \le F(x_{j-1}) + \frac{1}{m}$, both bounds are controlled by the finite grid of endpoints $\{x_1, \dots, x_{m-1}\}$:

$$F_n(x_{j-1}) - F(x_{j-1}) - \frac{1}{m} \le F_n(x) - F(x) \le F_n(x_j^-) - F(x_j^-) + \frac{1}{m}$$

Taking the supremum over all $x \in \mathbb{R}$ yields the deterministic sandwich inequality:

$$D_n = \sup_{x \in \mathbb{R}} |F_n(x) - F(x)| \le \max_{1 \le j \le m-1} \max\left\{ \left|F_n(x_j) - F(x_j)\right|, \; \left|F_n(x_j^-) - F(x_j^-)\right| \right\} + \frac{1}{m}$$

Because $\{x_1, \dots, x_{m-1}\}$ is a **finite** set of $2(m-1)$ evaluation points, applying the classical Strong Law of Large Numbers to each of the $2(m-1)$ points guarantees that with probability one, $\lim_{n \to \infty} \max_{1 \le j \le m-1} \max\{|F_n(x_j) - F(x_j)|, |F_n(x_j^-) - F(x_j^-)|\} = 0$. Therefore, with probability one:

$$\limsup_{n \to \infty} D_n \le \frac{1}{m}$$

Since $m \ge 1$ was completely arbitrary, taking a countable intersection over $m = 1, 2, \dots$ yields $\mathbb{P}(\lim_{n \to \infty} D_n = 0) = 1$.

Moreover, Monroe Donsker (1952) proved the **Functional Central Limit Theorem for the Empirical Process**: when $F$ is continuous, the scaled empirical process $\alpha_n(x) = \sqrt{n}\left(F_n(x) - F(x)\right)$, transformed via $t = F(x) \in [0, 1]$ into the uniform empirical process $U_n(t) = \sqrt{n}\left(G_n(t) - t\right)$ on $[0, 1]$, converges weakly in $D[0, 1]$ to a **Standard Brownian Bridge** (pinned Wiener process) $\{\mathbb{B}(t) : 0 \le t \le 1\}$:

$$U_n(t) \Longrightarrow \mathbb{B}(t) \stackrel{d}{=} W(t) - t W(1), \quad t \in [0, 1]$$

where $\{W(t) : t \ge 0\}$ is a standard Brownian motion, and $\mathbb{B}(t)$ is a continuous zero-mean Gaussian process with $\mathbb{B}(0) = \mathbb{B}(1) = 0$ and covariance kernel $\text{Cov}(\mathbb{B}(s), \mathbb{B}(t)) = \min(s, t) - st$. Even in finite samples, the Massart (1990) sharp **Dvoretzky-Kiefer-Wolfowitz (DKW) Inequality** provides an exact non-asymptotic concentration bound for all $n \ge 1$ and $\epsilon > 0$:

$$\mathbb{P}\left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| > \epsilon \right) \le 2 \exp\left( -2 n \epsilon^2 \right)$$

## 6.4 One-Sample and Two-Sample Kolmogorov-Smirnov (K-S) Supremum Tests

Armed with the Empirical Distribution Function $F_n(x)$, Andrey Kolmogorov (1933) and Nikolai Smirnov (1939) constructed exact distribution-free goodness-of-fit tests based on the $L^\infty$ supremum norm between $F_n(x)$ and a continuous null CDF $F_0(x)$. For testing the simple hypothesis $H_0 : F(x) = F_0(x)$ for all $x \in \mathbb{R}$ (where $F_0$ is completely specified and continuous), define the one-sided and two-sided **Kolmogorov-Smirnov (K-S) statistics**:

$$D_n^+ = \sup_{x \in \mathbb{R}} \left[ F_n(x) - F_0(x) \right], \qquad D_n^- = \sup_{x \in \mathbb{R}} \left[ F_0(x) - F_n(x) \right], \qquad D_n = \sup_{x \in \mathbb{R}} \left| F_n(x) - F_0(x) \right| = \max\left( D_n^+, D_n^- \right)$$

Notice that $D_n^+$ tests against the one-sided stochastic dominance alternative $H_1^+ : F(x) \ge F_0(x)$ (values of $X$ stochastically smaller than $F_0$), whereas $D_n^-$ tests against $H_1^- : F(x) \le F_0(x)$ (values of $X$ stochastically larger than $F_0$). How do we compute $D_n^+$, $D_n^-$, and $D_n$ from a finite sample $X_1, \dots, X_n$ without taking an uncountable supremum over $x \in \mathbb{R}$? Because $F_n(x)$ is constant equal to $(i-1)/n$ on each open interval $(X_{(i-1)}, X_{(i)})$ while $F_0(x)$ is monotonically non-decreasing, the differences $F_n(x) - F_0(x)$ and $F_0(x) - F_n(x)$ achieve their extrema strictly at the order statistics $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$:

$$D_n^+ = \max_{1 \le i \le n} \left[ \frac{i}{n} - F_0\left(X_{(i)}\right) \right], \qquad D_n^- = \max_{1 \le i \le n} \left[ F_0\left(X_{(i)}\right) - \frac{i - 1}{n} \right], \qquad D_n = \max\left( D_n^+, D_n^- \right)$$

### Theorem 6.4 (Distribution-Free Property and Kolmogorov-Smirnov Limiting Distributions)
Let $X_1, \dots, X_n$ be i.i.d. from a continuous CDF $F_0(x)$.
1. **Exact Finite-Sample Distribution-Freeness**: The exact distributions of $D_n^+$, $D_n^-$, and $D_n$ under $H_0$ are **completely independent of $F_0$**, and equal the distributions of the uniform K-S statistics for $U_1, \dots, U_n \stackrel{\text{i.i.d.}}{\sim} \text{Uniform}(0, 1)$.
2. **Smirnov's Asymptotic Distribution for One-Sided $D_n^+$ and $D_n^-$**: For every $\lambda > 0$:
   $$\lim_{n \to \infty} \mathbb{P}_{H_0}\left( \sqrt{n} D_n^+ \le \lambda \right) = \lim_{n \to \infty} \mathbb{P}_{H_0}\left( \sqrt{n} D_n^- \le \lambda \right) = 1 - e^{-2\lambda^2} \quad \implies \quad \mathbb{P}_{H_0}\left( \sqrt{n} D_n^+ > \lambda \right) \to e^{-2\lambda^2}$$
3. **Kolmogorov's Asymptotic Distribution for Two-Sided $D_n$**: For every $\lambda > 0$, $\sqrt{n} D_n \xrightarrow{d} \sup_{0 \le t \le 1} |\mathbb{B}(t)|$, whose exact CDF is the alternating theta-function series:
   $$\lim_{n \to \infty} \mathbb{P}_{H_0}\left( \sqrt{n} D_n \le \lambda \right) = K(\lambda) = 1 - 2 \sum_{j=1}^\infty (-1)^{j-1} e^{-2 j^2 \lambda^2} = \frac{\sqrt{2\pi}}{\lambda} \sum_{j=1}^\infty \exp\left( -\frac{(2j - 1)^2 \pi^2}{8 \lambda^2} \right)$$

#### Proof of Distribution-Freeness and Asymptotic Convergence:
By the Probability Integral Transform, when $X_i \sim F_0$ with $F_0$ continuous, the transformed random variables $U_i = F_0(X_i)$ are i.i.d. $\text{Uniform}(0, 1)$, and their order statistics are $U_{(i)} = F_0(X_{(i)})$. Substituting $U_{(i)} = F_0(X_{(i)})$ into the computational formulas above yields:

$$D_n^+ = \max_{1 \le i \le n} \left( \frac{i}{n} - U_{(i)} \right), \qquad D_n^- = \max_{1 \le i \le n} \left( U_{(i)} - \frac{i - 1}{n} \right)$$

Because the joint distribution of $(U_{(1)}, \dots, U_{(n)})$ is the Dirichlet/uniform order-statistic distribution on the simplex $0 < u_1 < \dots < u_n < 1$ with density $n!$ independent of $F_0$, $D_n^+$, $D_n^-$, and $D_n$ are strictly distribution-free! Furthermore, by Donsker's Theorem and the Continuous Mapping Theorem applied to the continuous functionals $g^+(f) = \sup_{t \in [0, 1]} f(t)$ and $g(f) = \sup_{t \in [0, 1]} |f(t)|$ on $D[0, 1]$, we have $\sqrt{n} D_n^+ \xrightarrow{d} \sup_{0 \le t \le 1} \mathbb{B}(t)$ and $\sqrt{n} D_n \xrightarrow{d} \sup_{0 \le t \le 1} |\mathbb{B}(t)|$. Applying the reflection principle of André to the pinned Brownian bridge $\mathbb{B}(t)$ across the single barrier $+\lambda$ yields $\mathbb{P}(\sup_{0 \le t \le 1} \mathbb{B}(t) \ge \lambda) = e^{-2\lambda^2}$, while repeated inclusion-exclusion reflections across the double barriers $\pm \lambda$ yield Kolmogorov's alternating series $1 - K(\lambda) = 2 \sum_{j=1}^\infty (-1)^{j-1} e^{-2 j^2 \lambda^2}$. For common significance levels $\alpha$, the asymptotic critical values $\lambda_\alpha$ of $\sqrt{n} D_n$ are $\lambda_{0.10} = 1.224$, $\lambda_{0.05} = 1.358$, and $\lambda_{0.01} = 1.628$ (so $d_{n, 0.05} \approx 1.358 / \sqrt{n}$).

Nikolai Smirnov also extended this framework to the **Two-Sample Kolmogorov-Smirnov Problem**: given two independent random samples $X_1, \dots, X_{n_1} \stackrel{\text{i.i.d.}}{\sim} F(x)$ and $Y_1, \dots, Y_{n_2} \stackrel{\text{i.i.d.}}{\sim} G(x)$ with empirical distribution functions $F_{n_1}(x)$ and $G_{n_2}(x)$, we test $H_0 : F(x) = G(x)$ for all $x \in \mathbb{R}$ via:

$$D_{n_1, n_2} = \sup_{x \in \mathbb{R}} \left| F_{n_1}(x) - G_{n_2}(x) \right|, \qquad D_{n_1, n_2}^+ = \sup_{x \in \mathbb{R}} \left[ F_{n_1}(x) - G_{n_2}(x) \right]$$

Under $H_0$ when $F = G$ is continuous, all $\binom{n_1 + n_2}{n_1}$ orderings of the combined sample of size $N = n_1 + n_2$ are equally likely, rendering $D_{n_1, n_2}$ strictly distribution-free in finite samples, and as $n_1, n_2 \to \infty$, the scaled statistic converges to the exact same Kolmogorov distribution:

$$\sqrt{\frac{n_1 n_2}{n_1 + n_2}} D_{n_1, n_2} \xrightarrow{d} \sup_{0 \le t \le 1} |\mathbb{B}(t)| \sim K(\lambda)$$

## 6.5 Quadratic EDF Statistics (Cramér-von Mises, Anderson-Darling) and Normality Tests (Lilliefors & Shapiro-Wilk)

Although the Kolmogorov-Smirnov statistic $D_n = \sup_x |F_n(x) - F_0(x)|$ is intuitively appealing, it suffers from two well-known limitations: (1) it depends only on the single point of maximum vertical deviation rather than integrating deviations across the entire support, and (2) because the variance of the empirical process $\text{Var}(F_n(x)) = F_0(x)[1 - F_0(x)] / n$ reaches its maximum $1/(4n)$ at the median ($F_0(x) = 0.5$) and vanishes at both tails ($F_0(x) \to 0$ or $1$), $D_n$ is most sensitive to shifts near the center of the distribution and exhibits relatively low power against heavy-tailed deviations!

To overcome this tail insensitivity, Harald Cramér (1928), Richard von Mises (1931), Nikolai Smirnov (1936), and Theodore W. Anderson and Donald A. Darling (1952) introduced the **Quadratic Empirical Distribution Function Family** based on weighted $L^2$ norms of $F_n(x) - F_0(x)$:

$$Q_n = n \int_{-\infty}^\infty \left[ F_n(x) - F_0(x) \right]^2 \psi\left(F_0(x)\right) dF_0(x) \xrightarrow{d} \int_0^1 \mathbb{B}^2(t) \psi(t) \, dt$$

where $\psi(t) \ge 0$ is a non-negative weight function on $(0, 1)$:
1. **Cramér-von Mises Statistic ($\omega^2_n$, with uniform weight $\psi(t) = 1$)**:
   $$\omega^2_n = n \int_{-\infty}^\infty \left[ F_n(x) - F_0(x) \right]^2 dF_0(x) = \frac{1}{12n} + \sum_{i=1}^n \left[ F_0\left(X_{(i)}\right) - \frac{2i - 1}{2n} \right]^2$$
   Notice how simply $\omega^2_n$ is computed from the ordered uniform transforms $U_{(i)} = F_0(X_{(i)})$ by comparing them against the mid-ranks $(2i-1)/(2n)$! By the Karhunen-Loève orthogonal eigenfunction expansion of the Brownian bridge $\mathbb{B}(t) = \sum_{j=1}^\infty \frac{\sqrt{2}}{\pi j} \sin(\pi j t) Z_j$ (where $Z_j \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, 1)$), Parseval's identity yields $\omega^2_n \xrightarrow{d} \int_0^1 \mathbb{B}^2(t) \, dt = \sum_{j=1}^\infty \frac{Z_j^2}{\pi^2 j^2}$.
2. **Anderson-Darling Statistic ($A^2_n$, with inverse-variance tail weight $\psi(t) = \frac{1}{t(1 - t)}$)**:
   By choosing $\psi(t) = [t(1 - t)]^{-1}$ equal to the reciprocal of the Brownian bridge variance, the Anderson-Darling statistic standardizes the empirical process across all quantiles and places heavy emphasis on the upper and lower tails:
   $$A^2_n = n \int_{-\infty}^\infty \frac{\left[ F_n(x) - F_0(x) \right]^2}{F_0(x)\left[ 1 - F_0(x) \right]} \, dF_0(x) = -n - \frac{1}{n} \sum_{i=1}^n (2i - 1) \left[ \ln F_0\left(X_{(i)}\right) + \ln\left( 1 - F_0\left(X_{(n + 1 - i)}\right) \right) \right]$$
   Under $H_0$, $A^2_n \xrightarrow{d} \int_0^1 \frac{\mathbb{B}^2(t)}{t(1 - t)} \, dt = \sum_{j=1}^\infty \frac{Z_j^2}{j(j + 1)}$.

What happens when we test the **composite hypothesis of normality** $H_0 : X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2)$ with unknown mean $\mu$ and unknown variance $\sigma^2$? If a practitioner plugs the sample mean $\bar{X}$ and sample standard deviation $S$ into the K-S statistic:

$$\hat{D}_n = \sup_{x \in \mathbb{R}} \left| F_n(x) - \Phi\left( \frac{x - \bar{X}}{S} \right) \right|$$

and compares $\hat{D}_n$ against standard Kolmogorov critical values ($1.358 / \sqrt{n}$ at $\alpha = 0.05$), the test is **severely conservative** (true Type I error drops from $0.05$ to $\approx 0.005$, accompanied by massive loss of power) because $\bar{X}$ and $S$ are fitted to the sample itself, pulling $\Phi((x - \bar{X})/S)$ much closer to $F_n(x)$ than the true population $\Phi((x - \mu)/\sigma)$!
- **Lilliefors Test for Normality (1967)**: Hubert Lilliefors recognized that while the distribution of $\hat{D}_n$ is much smaller than $D_n$, by location-scale invariance of $\frac{X_{(i)} - \bar{X}}{S}$, the distribution of $\hat{D}_n$ under $H_0$ is still **completely independent of the unknown $(\mu, \sigma^2)$**! Lilliefors derived the exact adjusted critical values for $\hat{D}_n$ via Monte Carlo simulation: at $\alpha = 0.05$, the Lilliefors critical value is $d_{\text{Lilliefors}, 0.05} \approx \frac{0.886}{\sqrt{n}}$ (more than $35\%$ smaller than Kolmogorov's $\frac{1.358}{\sqrt{n}}$!), and at $\alpha = 0.01$, $d_{\text{Lilliefors}, 0.01} \approx \frac{1.031}{\sqrt{n}}$. (Lilliefors 1969 derived the analogous adjustment for the Exponential distribution with estimated mean $\bar{X}$, where $d_{\text{Exp}, 0.05} \approx \frac{1.06}{\sqrt{n}}$).
- **Shapiro-Wilk $W$ Test for Normality (1965)**: Samuel Shapiro and Martin Wilk constructed an analysis-of-variance regression test comparing the square of the Best Linear Unbiased Estimator (BLUE) of $\sigma$ from order statistics against the sample sum of squares:
  $$W = \frac{\left( \sum_{i=1}^n a_i X_{(i)} \right)^2}{\sum_{i=1}^n (X_i - \bar{X})^2}, \quad \text{where } \mathbf{a} = (a_1, \dots, a_n)^\top = \frac{\mathbf{m}^\top \mathbf{V}^{-1}}{\left( \mathbf{m}^\top \mathbf{V}^{-2} \mathbf{m} \right)^{1/2}}$$
  Here $\mathbf{m} = (m_1, \dots, m_n)^\top$ is the vector of expected values of standard normal order statistics $m_i = \mathbb{E}[Z_{(i)}]$ and $\mathbf{V} = \text{Cov}(\mathbf{Z}_{(\cdot)})$ is their $n \times n$ covariance matrix. By the Cauchy-Schwarz inequality, $0 < W \le 1$, with values of $W$ close to $1$ supporting normality and small left-tail values ($W \le w_\alpha$) rejecting normality. Extensive simulation studies (Razali & Wah, 2011; Stephens, 1974) demonstrate that the **Shapiro-Wilk $W$ test and the Anderson-Darling $A^2$ test are the two most powerful omnibus tests of normality** across skewed, leptokurtic, and platykurtic alternatives.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Goodness-of-Fit Test</th><th>Test Statistic Formulation</th><th>Null Hypothesis Type</th><th>$\alpha = 0.05$ Asymptotic / Adjusted Threshold</th><th>Primary Strength & Sensitivity Profile</th></tr>
</thead>
<tbody>
<tr><td><strong>Pearson's Chi-Square ($X^2$)</strong></td><td>$\sum_{j=1}^k \frac{(O_j - E_j)^2}{E_j}$</td><td>Simple or Composite ($s$ params)</td><td>$\chi^2_{k - 1 - s, \, 0.05}$</td><td>Universal for discrete & categorical multinomials</td></tr>
<tr><td><strong>Kolmogorov-Smirnov ($D_n$)</strong></td><td>$\sup_x |F_n(x) - F_0(x)|$</td><td>Simple continuous $F_0(x)$</td><td>$1.358 / \sqrt{n}$</td><td>Exact finite-sample bounds; sensitive to median shift</td></tr>
<tr><td><strong>Cramér-von Mises ($\omega^2_n$)</strong></td><td>$\frac{1}{12n} + \sum_{i=1}^n \left(U_{(i)} - \frac{2i-1}{2n}\right)^2$</td><td>Simple continuous $F_0(x)$</td><td>$0.461$</td><td>Smooth $L^2$ integration across entire support</td></tr>
<tr><td><strong>Anderson-Darling ($A^2_n$)</strong></td><td>$n \int \frac{(F_n - F_0)^2}{F_0(1 - F_0)} dF_0$</td><td>Simple or Composite</td><td>$2.492$ (simple) / $0.752$ (normal)</td><td>High power in upper and lower distribution tails</td></tr>
<tr><td><strong>Lilliefors Test ($\hat{D}_n$)</strong></td><td>$\sup_x |F_n(x) - \Phi((x - \bar{X})/S)|$</td><td>Composite $\mathcal{N}(\mu, \sigma^2)$</td><td>$0.886 / \sqrt{n}$</td><td>Corrects severe conservatism of plug-in K-S test</td></tr>
<tr><td><strong>Shapiro-Wilk ($W$)</strong></td><td>$\frac{(\sum a_i X_{(i)})^2}{\sum (X_i - \bar{X})^2}$</td><td>Composite $\mathcal{N}(\mu, \sigma^2)$</td><td>Left-tail $W \le w_{n, 0.05}$</td><td>Highest omnibus power against non-normality</td></tr>
</tbody>
</table></div>

## 6.6 Power Comparison, Consistency of Omnibus Tests & Practical Diagnostics

A fundamental distinction between parametric tests (such as the $t$-test or Neyman-Pearson test) and nonparametric EDF tests ($D_n, \omega^2_n, A^2_n$) lies in their **global consistency** against arbitrary fixed alternatives $F_1 \ne F_0$.

### Theorem 6.5 (Universal Consistency of Kolmogorov-Smirnov and Quadratic EDF Tests)
Let $F_0$ be a continuous null CDF, and let $F_1$ be **any** alternative CDF such that $F_1(x_0) \ne F_0(x_0)$ for at least one point $x_0 \in \mathbb{R}$. Then for any fixed significance level $\alpha \in (0, 1)$, the power of the level-$\alpha$ Kolmogorov-Smirnov test approaches $1$ as $n \to \infty$:

$$\lim_{n \to \infty} \mathbb{P}_{F_1}\left( \sqrt{n} D_n > \lambda_\alpha \right) = 1$$

#### Proof:
Let $\Delta = \sup_{x \in \mathbb{R}} |F_1(x) - F_0(x)| \ge |F_1(x_0) - F_0(x_0)| > 0$. By the reverse triangle inequality in the supremum norm $\|\cdot\|_\infty$:

$$D_n = \|F_n - F_0\|_\infty = \|(F_1 - F_0) - (F_1 - F_n)\|_\infty \ge \|F_1 - F_0\|_\infty - \|F_n - F_1\|_\infty = \Delta - \|F_n - F_1\|_\infty$$

Multiplying by $\sqrt{n}$ gives $\sqrt{n} D_n \ge \sqrt{n} \Delta - \sqrt{n} \|F_n - F_1\|_\infty$. Under $F_1$, by the Dvoretzky-Kiefer-Wolfowitz inequality, $\sqrt{n} \|F_n - F_1\|_\infty = O_p(1)$ is tight in probability, whereas $\sqrt{n} \Delta \to +\infty$ as $n \to \infty$. Consequently, $\mathbb{P}_{F_1}(\sqrt{n} D_n > \lambda_\alpha) \to 1$.

 alongside formal hypothesis tests, visual probability plots—specifically the **Quantile-Quantile (Q-Q) Plot** graphing the sample order statistics $X_{(i)}$ against the theoretical standard quantiles $F_0^{-1}\left(\frac{i - 0.5}{n}\right)$—provide an indispensable diagnostic companion. Notice that the square root of the Shapiro-Wilk statistic $\sqrt{W}$ is essentially the sample Pearson correlation coefficient between the ordered observations $X_{(i)}$ and the normal scores $m_i$ on the normal Q-Q plot!

### Smirnov's Exact Finite-Sample Combinatorial Recursion and Steck's Determinant
In finite samples of size $n$, how are the exact critical values $d_{n, \alpha}$ of the Kolmogorov-Smirnov statistics $D_n^+$ and $D_n$ computed without relying on the large-sample Brownian bridge limit? For the one-sided statistic $D_n^+ = \max_{1 \le i \le n} \left( \frac{i}{n} - U_{(i)} \right)$, Z. W. Birnbaum and Fred H. Tingey (1951) proved an exact closed-form combinatorial formula for the survival probability $\mathbb{P}_{H_0}(D_n^+ > c)$ for any threshold $c \in (0, 1)$ by integrating over the ordered uniform polytope $\left\{ (u_1, \dots, u_n) : 0 < u_1 < \dots < u_n < 1 \text{ and } u_i > \frac{i}{n} - c \right\}$ using Abel's generalization of the binomial theorem:

$$\mathbb{P}_{H_0}\left( D_n^+ > c \right) = (1 - c)^n + c \sum_{j=1}^{\lfloor n(1 - c) \rfloor} \binom{n}{j} \left( 1 - c - \frac{j}{n} \right)^{n - j} \left( c + \frac{j}{n} \right)^{j - 1}$$

For the two-sample Kolmogorov-Smirnov test with sample sizes $n_1$ and $n_2$ ($N = n_1 + n_2$), when $n_1 = n_2 = m$, the combined sample path can be represented as a lattice walk from $(0, 0)$ to $(m, m)$ taking $m$ unit horizontal steps ($+1, 0$) corresponding to $X$-observations and $m$ unit vertical steps ($0, +1$) corresponding to $Y$-observations. Under the null hypothesis $H_0 : F = G$, all $\binom{2m}{m}$ lattice paths from $(0, 0)$ to $(m, m)$ are strictly equiprobable! The event $\left\{ D_{m, m} < \frac{c}{m} \right\}$ is equivalent to the geometric condition that the lattice path never touches or crosses the two diagonal boundary lines $y = x + c$ and $y = x - c$. By applying the **André Reflection Principle** repeatedly across the two diagonal boundaries $y - x = \pm c$, Nikolai Smirnov and B. V. Gnedenko derived the exact finite-sample combinatorial distribution:

$$\mathbb{P}_{H_0}\left( D_{m, m} < \frac{c}{m} \right) = \frac{1}{\binom{2m}{m}} \sum_{j = -\infty}^\infty (-1)^j \binom{2m}{m - j c}$$

This exact reflection series explains both why the finite-sample distribution of $D_{m, m}$ is purely combinatorial and how the alternating series $K(\lambda) = \sum_{j = -\infty}^\infty (-1)^j e^{-2 j^2 \lambda^2}$ emerges naturally in the Stirling asymptotic limit as $m \to \infty$ with $c = \lambda \sqrt{2m}$.

### Neyman's Smooth Test of Goodness-of-Fit and Orthogonal Legendre Polynomials
To bridge the gap between omnibus EDF tests (which spread their power thinly across infinite-dimensional space) and parametric likelihood ratio tests (which concentrate power along a single parametric direction), Jerzy Neyman (1937) introduced the **Smooth Test of Goodness-of-Fit**. Transforming the raw observations via $U_i = F_0(X_i) \in [0, 1]$, testing $H_0 : F = F_0$ is equivalent to testing whether $U_1, \dots, U_n \stackrel{\text{i.i.d.}}{\sim} \text{Uniform}(0, 1)$. Neyman embedded the uniform density $g_0(u) = 1$ on $[0, 1]$ into a smooth $d$-dimensional exponential family generated by the first $d$ orthonormal **Legendre polynomials** $\pi_1(u), \pi_2(u), \dots, \pi_d(u)$ on $[0, 1]$, where $\int_0^1 \pi_r(u) \, du = 0$ and $\int_0^1 \pi_r(u) \pi_s(u) \, du = \delta_{rs}$:
- $\pi_1(u) = \sqrt{12}\left(u - \frac{1}{2}\right)$ (captures linear shift in location/mean)
- $\pi_2(u) = \sqrt{5}\left[6\left(u - \frac{1}{2}\right)^2 - \frac{1}{2}\right]$ (captures quadratic dispersion/scale change)
- $\pi_3(u) = \sqrt{7}\left[20\left(u - \frac{1}{2}\right)^3 - 3\left(u - \frac{1}{2}\right)\right]$ (captures cubic skewness asymmetry)
- $\pi_4(u) = 3\left[70\left(u - \frac{1}{2}\right)^4 - 15\left(u - \frac{1}{2}\right)^2 + \frac{3}{8}\right]$ (captures quartic kurtosis/tail heaviness)

Under the smooth exponential family density $g(u; \boldsymbol{\theta}) = \exp\left( \sum_{r=1}^d \theta_r \pi_r(u) - \psi(\boldsymbol{\theta}) \right)$, the Rao Score Test statistic for testing $H_0 : \theta_1 = \theta_2 = \dots = \theta_d = 0$ decomposes into the sum of squares of $d$ orthogonal sample components:

$$\Psi^2_d = \sum_{r=1}^d V_r^2, \quad \text{where } V_r = \frac{1}{\sqrt{n}} \sum_{i=1}^n \pi_r\left(F_0(X_i)\right) \xrightarrow{d} \mathcal{N}(0, 1) \implies \Psi^2_d \xrightarrow{d} \chi^2_d$$

By choosing a small order $d \in \{2, 3, 4\}$, Neyman's smooth test achieves substantially higher local Pitman power against low-frequency location, scale, skewness, and kurtosis alternatives than either Pearson's $\chi^2$ test with many bins or the Kolmogorov-Smirnov supremum test, while decomposing the departure from $H_0$ into interpretable orthogonal moment components!

### Asymptotic Pitman and Bahadur Efficiency of Goodness-of-Fit Procedures
When selecting among competing goodness-of-fit procedures in applied scientific work, how do Pearson's $\chi^2$ test, the Kolmogorov-Smirnov supremum test $D_n$, the Cramér-von Mises quadratic test $\omega^2_n$, and the Anderson-Darling tail-weighted test $A^2_n$ compare in terms of local Pitman power and nonlocal Bahadur efficiency? Let us examine the fundamental structural trade-offs revealed by asymptotic empirical process theory:

1. **Discretization Loss in Pearson's $\chi^2$ Test**: When the underlying random variable $X$ is genuinely continuous, partitioning the real line into $k$ intervals discards all intra-interval positional information. Moreover, as the number of cells $k$ increases, the degrees of freedom $k - 1$ of the limiting central $\chi^2_{k-1}$ distribution grow, which increases the null variance $2(k - 1)$ of the test statistic and dilutes the noncentrality parameter $\lambda = n \sum_{j=1}^k \frac{(p_{j1} - p_{j0})^2}{p_{j0}}$ across more degrees of freedom. Consequently, against smooth location or scale shifts of a continuous distribution, Pearson's $\chi^2$ test has strictly zero Pitman Asymptotic Relative Efficiency ($\text{ARE} = 0$) relative to parametric score tests unless the bin boundaries are specifically optimized, and systematically trails Empirical Distribution Function tests such as $\omega^2_n$ and $A^2_n$.
2. **Supremum ($L^\infty$) versus Integrated Quadratic ($L^2$) EDF Statistics**: Because the Kolmogorov-Smirnov statistic $D_n = \sup_{x \in \mathbb{R}} |F_n(x) - F_0(x)|$ evaluates only the single largest pointwise vertical discrepancy, its sensitivity is governed by the supremum of the deterministic shift function $\delta(x) = F_1(x) - F_0(x)$. In contrast, the Cramér-von Mises statistic $\omega^2_n$ integrates $[\delta(x)]^2$ over the entire support with respect to $dF_0(x)$, accumulating smooth global departures across every quantile. By the Karhunen-Loève spectral decomposition of the Brownian bridge $\mathbb{B}(t) = \sum_{j=1}^\infty \frac{\sqrt{2}}{\pi j} \sin(\pi j t) Z_j$, the first principal component $Z_1$ (which corresponds to a global location shift $\sin(\pi t)$) receives weight $\frac{1}{\pi^2} \approx 0.1013$ out of the total variance $\sum_{j=1}^\infty \frac{1}{\pi^2 j^4} = \frac{1}{90}$ in $\omega^2_n$, accounting for over $91\%$ of the total null variance of the Cramér-von Mises statistic! This spectral concentration explains why $\omega^2_n$ and $A^2_n$ achieve substantially higher statistical power than $D_n$ against smooth shifts in mean, variance, skewness, and tail thickness.

---

## Worked Questions and Solutions

### Question 1: Composite Poisson Chi-Square Goodness-of-Fit Test with Parameter Estimation and Tail Pooling
A telecommunications network engineer records the number of packet transmission errors per millisecond across $n = 200$ independent 1-millisecond intervals, obtaining the following frequency distribution: $0$ errors in $104$ intervals, $1$ error in $66$ intervals, $2$ errors in $22$ intervals, $3$ errors in $6$ intervals, $4$ errors in $2$ intervals, and $\ge 5$ errors in $0$ intervals.
1. Estimate the unknown Poisson rate parameter $\lambda$ via Maximum Likelihood under the composite null hypothesis $H_0 : X \sim \text{Poisson}(\lambda)$, and compute the theoretical Poisson cell probabilities $\hat{p}_j$ and expected cell counts $\hat{E}_j = n \hat{p}_j$ for $j = 0, 1, 2, 3, \ge 4$.
2. Apply Cochran's expected cell frequency rule ($\hat{E}_j \ge 5$) to pool sparse upper-tail cells, and determine the exact reduced degrees of freedom $\text{df} = k - 1 - s$ via Fisher's Theorem.
3. Compute both Karl Pearson's $X^2$ statistic and the Likelihood Ratio $G^2$ statistic on the pooled cells, and test $H_0$ at significance level $\alpha = 0.05$.

### Solution, step 1: Maximum likelihood estimation of $\lambda$ and expected Poisson frequencies
From the observed frequency distribution across the $n = 200$ intervals, the total number of packet transmission errors is:

$$\sum_{i=1}^{200} X_i = 0(104) + 1(66) + 2(22) + 3(6) + 4(2) + 5(0) = 0 + 66 + 44 + 18 + 8 = 136\text{ errors}$$

Therefore, the Maximum Likelihood Estimator of the Poisson rate parameter $\lambda$ is the sample mean:

$$\hat{\lambda} = \bar{X} = \frac{136}{200} = 0.68\text{ errors/ms}$$

Using the Poisson probability mass function $\hat{p}_j = \frac{e^{-0.68} (0.68)^j}{j!}$ with $e^{-0.68} \approx 0.506617$, we compute the fitted probabilities and expected frequencies $\hat{E}_j = 200 \hat{p}_j$:
- **$j = 0$**: $\hat{p}_0 = e^{-0.68} = 0.506617 \implies \hat{E}_0 = 200(0.506617) = 101.323$ (Observed $O_0 = 104$)
- **$j = 1$**: $\hat{p}_1 = 0.68 e^{-0.68} = 0.344500 \implies \hat{E}_1 = 200(0.344500) = 68.900$ (Observed $O_1 = 66$)
- **$j = 2$**: $\hat{p}_2 = \frac{(0.68)^2}{2} e^{-0.68} = 0.117130 \implies \hat{E}_2 = 200(0.117130) = 23.426$ (Observed $O_2 = 22$)
- **$j = 3$**: $\hat{p}_3 = \frac{(0.68)^3}{6} e^{-0.68} = 0.026549 \implies \hat{E}_3 = 200(0.026549) = 5.310$ (Observed $O_3 = 6$)
- **$j \ge 4$**: $\hat{p}_{\ge 4} = 1 - (\hat{p}_0 + \hat{p}_1 + \hat{p}_2 + \hat{p}_3) = 1 - 0.994796 = 0.005204 \implies \hat{E}_{\ge 4} = 200(0.005204) = 1.041$ (Observed $O_{\ge 4} = 2$)

### Solution, step 2: Application of Cochran's Rule and Fisher's degrees-of-freedom calculation
Inspecting the expected frequencies above, the tail cell $j \ge 4$ has $\hat{E}_{\ge 4} = 1.041 < 5$. To satisfy the strict $E_j \ge 5$ guideline in every cell, we pool the cell $j = 3$ and $j \ge 4$ into a single combined tail category $C_4 = \{X \ge 3\}$:
- **Pooled Cell $j \ge 3$**: Observed count $O_{\ge 3} = O_3 + O_{\ge 4} = 6 + 2 = 8$; Expected count $\hat{E}_{\ge 3} = \hat{E}_3 + \hat{E}_{\ge 4} = 5.310 + 1.041 = 6.351 \ge 5$.

After pooling, there are $k = 4$ active cells: $\{0\}, \{1\}, \{2\}, \{\ge 3\}$. Because $s = 1$ parameter ($\lambda$) was estimated from the sample data under $H_0$, Fisher's Degrees-of-Freedom Reduction Theorem gives:

$$\text{df} = k - 1 - s = 4 - 1 - 1 = 2\text{ degrees of freedom}$$

### Solution, step 3: Evaluation of $X^2$ and $G^2$ and statistical decision
We now evaluate Pearson's $X^2 = \sum_{j=1}^4 \frac{(O_j - \hat{E}_j)^2}{\hat{E}_j}$ across the $k = 4$ pooled cells:

$$X^2 = \frac{(104 - 101.323)^2}{101.323} + \frac{(66 - 68.900)^2}{68.900} + \frac{(22 - 23.426)^2}{23.426} + \frac{(8 - 6.351)^2}{6.351}$$

$$X^2 = \frac{7.166}{101.323} + \frac{8.410}{68.900} + \frac{2.033}{23.426} + \frac{2.719}{6.351} = 0.0707 + 0.1221 + 0.0868 + 0.4281 = 0.7077$$

Similarly, the Likelihood Ratio goodness-of-fit statistic $G^2 = 2 \sum_{j=1}^4 O_j \ln(O_j / \hat{E}_j)$ is:

$$G^2 = 2 \left[ 104 \ln\left(\frac{104}{101.323}\right) + 66 \ln\left(\frac{66}{68.900}\right) + 22 \ln\left(\frac{22}{23.426}\right) + 8 \ln\left(\frac{8}{6.351}\right) \right] = 2(2.711 - 2.838 - 1.382 + 1.849) \approx 0.680$$

At significance level $\alpha = 0.05$ with $\text{df} = 2$, the critical value is $\chi^2_{2, \, 0.05} = 5.9915$ (and the exact $p$-value is $\mathbb{P}(\chi^2_2 \ge 0.7077) = e^{-0.7077/2} \approx 0.702$). Since $X^2 = 0.7077 < 5.9915$, we do not reject $H_0$: the packet error counts are in outstanding agreement with a Poisson distribution of rate $\hat{\lambda} = 0.68$.

---

### Question 2: Exact One-Sample Kolmogorov-Smirnov, Cramér-von Mises, and Lilliefors Normality Tests
A materials laboratory measures the tensile fracture stress $X$ (in hundreds of MPa) of $n = 5$ ceramic fibers, obtaining the ordered observations:

$$X_{(1)} = 1.20, \quad X_{(2)} = 1.50, \quad X_{(3)} = 1.80, \quad X_{(4)} = 2.40, \quad X_{(5)} = 3.10$$

1. Test the **simple** null hypothesis $H_0 : X \sim \mathcal{N}(\mu_0 = 2.00, \sigma_0^2 = 0.25)$ (so $\sigma_0 = 0.50$) by computing the exact values of $D_5^+$, $D_5^-$, $D_5$, and the Cramér-von Mises statistic $\omega^2_5$, and compare $D_5$ against the exact $n = 5, \alpha = 0.05$ K-S critical value $d_{5, 0.05} = 0.565$.
2. Now test the **composite** hypothesis of normality $H_0 : X \sim \mathcal{N}(\mu, \sigma^2)$ with unknown $(\mu, \sigma^2)$ by computing the sample mean $\bar{X}$, sample standard deviation $S$, and Lilliefors statistic $\hat{D}_5$, and compare against the Lilliefors critical value $d_{\text{Lilliefors}, 5, 0.05} = 0.337$.
3. Explain why $\hat{D}_5 < D_5$ and why applying the unadjusted K-S critical value $0.565$ to $\hat{D}_5$ would misstate the significance threshold.

### Solution, step 1: Simple K-S statistics ($D_5^+, D_5^-, D_5$) and Cramér-von Mises statistic $\omega^2_5$
Under the simple null hypothesis $H_0 : X \sim \mathcal{N}(2.00, 0.50^2)$, the standardized values $z_i = \frac{X_{(i)} - 2.00}{0.50}$ and their standard normal CDF values $U_{(i)} = F_0(X_{(i)}) = \Phi(z_i)$ are:
- $i = 1$ ($X_{(1)} = 1.20$): $z_1 = \frac{1.20 - 2.00}{0.50} = -1.60 \implies U_{(1)} = \Phi(-1.60) = 0.0548$
- $i = 2$ ($X_{(2)} = 1.50$): $z_2 = \frac{1.50 - 2.00}{0.50} = -1.00 \implies U_{(2)} = \Phi(-1.00) = 0.1587$
- $i = 3$ ($X_{(3)} = 1.80$): $z_3 = \frac{1.80 - 2.00}{0.50} = -0.40 \implies U_{(3)} = \Phi(-0.40) = 0.3446$
- $i = 4$ ($X_{(4)} = 2.40$): $z_4 = \frac{2.40 - 2.00}{0.50} = +0.80 \implies U_{(4)} = \Phi(+0.80) = 0.7881$
- $i = 5$ ($X_{(5)} = 3.10$): $z_5 = \frac{3.10 - 2.00}{0.50} = +2.20 \implies U_{(5)} = \Phi(+2.20) = 0.9861$

We now compute the step-wise positive deviations $\frac{i}{5} - U_{(i)}$ and negative deviations $U_{(i)} - \frac{i-1}{5}$:
- $i = 1$: $\frac{1}{5} - 0.0548 = 0.1452$; $\quad 0.0548 - 0.0000 = 0.0548$
- $i = 2$: $\frac{2}{5} - 0.1587 = 0.2413$; $\quad 0.1587 - 0.2000 = -0.0413$
- $i = 3$: $\frac{3}{5} - 0.3446 = \mathbf{0.2554}$; $\quad 0.3446 - 0.4000 = -0.0554$
- $i = 4$: $\frac{4}{5} - 0.7881 = 0.0119$; $\quad 0.7881 - 0.6000 = \mathbf{0.1881}$
- $i = 5$: $\frac{5}{5} - 0.9861 = 0.0139$; $\quad 0.9861 - 0.8000 = 0.1861$

Taking the maxima yields:

$$D_5^+ = 0.2554 \text{ (at } i = 3\text{)}, \qquad D_5^- = 0.1881 \text{ (at } i = 4\text{)}, \qquad D_5 = \max(0.2554, 0.1881) = 0.2554$$

For the Cramér-von Mises statistic $\omega^2_5 = \frac{1}{12(5)} + \sum_{i=1}^5 \left(U_{(i)} - \frac{2i-1}{10}\right)^2$, the mid-ranks are $(0.1, 0.3, 0.5, 0.7, 0.9)$:

$$\omega^2_5 = 0.01667 + (-0.0452)^2 + (-0.1413)^2 + (-0.1554)^2 + (0.0881)^2 + (0.0861)^2 = 0.01667 + 0.06133 = 0.0780$$

Since $D_5 = 0.2554 < d_{5, 0.05} = 0.565$ (and $\omega^2_5 = 0.0780 < 0.461$), we do not reject the simple null hypothesis $H_0$.

### Solution, step 2: Composite Lilliefors test with estimated $(\bar{X}, S)$
From the raw sample $(1.20, 1.50, 1.80, 2.40, 3.10)$, the sample mean $\bar{X}$ and sample standard deviation $S$ are:

$$\bar{X} = \frac{1.20 + 1.50 + 1.80 + 2.40 + 3.10}{5} = \frac{10.00}{5} = 2.000$$

$$S^2 = \frac{(-0.80)^2 + (-0.50)^2 + (-0.20)^2 + (0.40)^2 + (1.10)^2}{5 - 1} = \frac{0.64 + 0.25 + 0.04 + 0.16 + 1.21}{4} = \frac{2.30}{4} = 0.575 \implies S \approx 0.75829$$

Standardizing via $\hat{z}_i = \frac{X_{(i)} - 2.000}{0.75829}$ gives $\hat{z} = (-1.0550, -0.6594, -0.2638, +0.5275, +1.4506)$, with fitted normal CDF values $\hat{U}_{(i)} = \Phi(\hat{z}_i)$:

$$\hat{U}_{(1)} = 0.1457, \quad \hat{U}_{(2)} = 0.2548, \quad \hat{U}_{(3)} = 0.3960, \quad \hat{U}_{(4)} = 0.7011, \quad \hat{U}_{(5)} = 0.9266$$

Evaluating $\hat{D}_5^+ = \max_i \left(\frac{i}{5} - \hat{U}_{(i)}\right)$ and $\hat{D}_5^- = \max_i \left(\hat{U}_{(i)} - \frac{i-1}{5}\right)$ gives:
- $\hat{D}_5^+ = \max(0.0543, 0.1452, \mathbf{0.2040}, 0.0989, 0.0734) = 0.2040$ (achieved at $i = 3$)
- $\hat{D}_5^- = \max(\mathbf{0.1457}, 0.0548, -0.0040, 0.1011, 0.1266) = 0.1457$ (achieved at $i = 1$)
- Therefore, $\hat{D}_5 = \max(0.2040, 0.1457) = 0.2040$. Comparing $\hat{D}_5 = 0.2040$ against the exact Lilliefors threshold $d_{\text{Lilliefors}, 5, 0.05} = 0.337$, we do not reject normality.

### Solution, step 3: Explanation of why $\hat{D}_5 < D_5$ and critical value distortion
Notice that replacing the hypothesized $\sigma_0 = 0.50$ by the sample standard deviation $S = 0.7583$ inflated the dispersion of the fitted normal curve to match the wide spread of $X_{(1)} = 1.20$ and $X_{(5)} = 3.10$, reducing the supremum discrepancy from $D_5 = 0.2554$ down to $\hat{D}_5 = 0.2040$. Because $(\bar{X}, S)$ automatically absorb sample location and scale fluctuations, the null distribution of $\hat{D}_n$ is compressed toward zero, requiring the much tighter Lilliefors threshold $0.337$ instead of Kolmogorov's $0.565$.

---

### Question 3: Stratified $2 \times 2$ Clinical Trial Analysis and Simpson's Paradox—Cochran-Mantel-Haenszel (CMH) Test
A multi-center oncology trial compares a novel targeted immunotherapy ($T$) against standard chemotherapy ($C$) for 1-year progression-free survival (Response = Yes vs. No) across $K = 2$ patient risk strata: **Stratum 1 (Early-Stage Disease, $n_1 = 150$)** and **Stratum 2 (Advanced-Stage Disease, $n_2 = 150$)**.
- **Stratum 1 (Early-Stage)**: Immunotherapy $T$ has $a_1 = 80$ responders and $b_1 = 20$ non-responders ($R_{11} = 100$, response rate $80\%$); Chemotherapy $C$ has $c_1 = 35$ responders and $d_1 = 15$ non-responders ($R_{21} = 50$, response rate $70\%$). Column totals: $C_{11} = 115$ Yes, $C_{21} = 35$ No; $n_1 = 150$.
- **Stratum 2 (Advanced-Stage)**: Immunotherapy $T$ has $a_2 = 20$ responders and $b_2 = 30$ non-responders ($R_{12} = 50$, response rate $40\%$); Chemotherapy $C$ has $c_2 = 25$ responders and $d_2 = 75$ non-responders ($R_{22} = 100$, response rate $25\%$). Column totals: $C_{12} = 45$ Yes, $C_{22} = 105$ No; $n_2 = 150$.
1. Show that pooling the two strata into a single marginal $2 \times 2$ table triggers **Simpson's Paradox**, where the marginal response rates are identical ($66.7\%$ vs. $40\%$? Wait: let us compute the exact marginal table and stratum-specific odds ratios $\hat{\psi}_1$ and $\hat{\psi}_2$).
2. Compute the conditional hypergeometric expectations $\mu_{11k}$ and variances $V_{11k}$ for $k = 1, 2$, and evaluate both the uncorrected and continuity-corrected Cochran-Mantel-Haenszel statistics $X^2_{\text{CMH}}$.
3. Calculate the Mantel-Haenszel common odds ratio estimator $\hat{\psi}_{\text{MH}}$ and interpret the clinical conclusion at $\alpha = 0.05$.

### Solution, step 1: Stratum-specific odds ratios versus pooled marginal table
In **Stratum 1 (Early-Stage)**, the response rate is $80/100 = 80.0\%$ for Immunotherapy $T$ versus $35/50 = 70.0\%$ for Chemotherapy $C$, with stratum-specific sample odds ratio:

$$\hat{\psi}_1 = \frac{a_1 d_1}{b_1 c_1} = \frac{80 \times 15}{20 \times 35} = \frac{1200}{700} \approx 1.714 > 1$$

In **Stratum 2 (Advanced-Stage)**, the response rate is $20/50 = 40.0\%$ for Immunotherapy $T$ versus $25/100 = 25.0\%$ for Chemotherapy $C$, with stratum-specific sample odds ratio:

$$\hat{\psi}_2 = \frac{a_2 d_2}{b_2 c_2} = \frac{20 \times 75}{30 \times 25} = \frac{1500}{750} = 2.000 > 1$$

Notice that within **both** strata, Immunotherapy $T$ outperforms Chemotherapy $C$ with an odds ratio between $1.71$ and $2.00$, and individually neither smaller stratum reaches significance on its own ($X^2_1 = 1.863$, $X^2_2 = 3.561 < 3.841$). Combining information across strata properly via CMH avoids confounding by baseline disease stage while pooling statistical power!

### Solution, step 2: Hypergeometric moments and Cochran-Mantel-Haenszel statistic $X^2_{\text{CMH}}$
For each stratum $k \in \{1, 2\}$, we compute the conditional hypergeometric mean $\mu_{11k} = \frac{R_{1k} C_{1k}}{n_k}$ and variance $V_{11k} = \frac{R_{1k} R_{2k} C_{1k} C_{2k}}{n_k^2 (n_k - 1)}$:
- **Stratum 1 ($n_1 = 150$)**: $O_{11,1} = a_1 = 80$, and:
  $$\mu_{11,1} = \frac{100 \times 115}{150} = 76.6667, \qquad V_{11,1} = \frac{100 \times 50 \times 115 \times 35}{150^2 \times 149} = \frac{20,125,000}{3,352,500} \approx 6.0030$$
- **Stratum 2 ($n_2 = 150$)**: $O_{11,2} = a_2 = 20$, and:
  $$\mu_{11,2} = \frac{50 \times 45}{150} = 15.0000, \qquad V_{11,2} = \frac{50 \times 100 \times 45 \times 105}{150^2 \times 149} = \frac{23,625,000}{3,352,500} \approx 7.0470$$

Summing the deviations and variances across the two independent strata gives:

$$\sum_{k=1}^2 \left(O_{11k} - \mu_{11k}\right) = (80 - 76.6667) + (20 - 15.0000) = 3.3333 + 5.0000 = 8.3333, \qquad \sum_{k=1}^2 V_{11k} = 6.0030 + 7.0470 = 13.0500$$

Therefore, the uncorrected and continuity-corrected CMH test statistics are:

$$X^2_{\text{CMH, uncorr}} = \frac{(8.3333)^2}{13.0500} = \frac{69.4444}{13.0500} \approx 5.321, \qquad X^2_{\text{CMH, corr}} = \frac{(8.3333 - 0.5)^2}{13.0500} = \frac{61.3611}{13.0500} \approx 4.702$$

### Solution, step 3: Mantel-Haenszel Common Odds Ratio $\hat{\psi}_{\text{MH}}$ and clinical interpretation
The Mantel-Haenszel common odds ratio estimator is:

$$\hat{\psi}_{\text{MH}} = \frac{\frac{a_1 d_1}{n_1} + \frac{a_2 d_2}{n_2}}{\frac{b_1 c_1}{n_1} + \frac{b_2 c_2}{n_2}} = \frac{\frac{80 \times 15}{150} + \frac{20 \times 75}{150}}{\frac{20 \times 35}{150} + \frac{30 \times 25}{150}} = \frac{1200 + 1500}{700 + 750} = \frac{2700}{1450} \approx 1.862$$

At significance level $\alpha = 0.05$, both $X^2_{\text{CMH, uncorr}} = 5.321 > \chi^2_{1, \, 0.05} = 3.8415$ ($p = 0.021$) and $X^2_{\text{CMH, corr}} = 4.702 > 3.8415$ ($p = 0.030$) reject the null hypothesis of conditional independence $H_0 : \psi = 1$. Controlling for disease stage, patients receiving targeted immunotherapy have $1.862$ times higher odds of 1-year progression-free survival than patients receiving standard chemotherapy.
