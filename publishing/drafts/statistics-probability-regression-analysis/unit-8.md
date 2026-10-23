# Unit 8: Nonlinear Regression, Robust Regression & Generalized Linear Models (Logistic & Poisson)

Intrinsically nonlinear regression models Y_i = f(x_i, theta) + epsilon_i (Michaelis-Menten, Gompertz, logistic growth, exponential decay); Nonlinear Least Squares (NLS) optimization: Gauss-Newton Taylor linearization, Levenberg-Marquardt damping, and asymptotic covariance sigma^2 (J^T J)^(-1); Robust regression for heavy-tailed contamination: L_1 Least Absolute Deviations (LAD), Huber M-estimation, Iteratively Reweighted Least Squares (IRLS), and Tukey's biweight; Generalized Linear Models (GLMs): exponential dispersion family, linear predictor eta = X beta, canonical link functions g(mu), and Fisher Scoring / IRLS; Binary Logistic Regression (logit link, odds ratios, Wald/deviance tests, Hosmer-Lemeshow) and Poisson Log-Linear Regression for count data and overdispersion.

## 8.1 Intrinsically Nonlinear Regression Models vs Linearizable Functional Forms

Throughout Units 1 through 7, every regression model—no matter how curved in the predictor space $\mathbf{x}$ (such as polynomial regression, cubic B-splines, or Fourier series)—shared one defining structural property: the conditional expectation function $\mathbb{E}[Y_i \mid \mathbf{x}_i] = \mathbf{x}_i^T \boldsymbol{\beta}$ had partial derivatives with respect to the unknown parameters $\beta_j$ that depended **only on the known covariates $\mathbf{x}_i$ and never on the unknown parameters $\boldsymbol{\beta}$ themselves**.

In chemical kinetics, enzyme biochemistry, pharmacokinetics, population ecology, and solid-state physics, mechanistic differential equations frequently generate response trajectories of the general form:

$$Y_i = f(\mathbf{x}_i, \boldsymbol{\theta}) + \varepsilon_i, \quad i = 1, 2, \dots, n$$

where $\boldsymbol{\theta} = (\theta_1, \theta_2, \dots, \theta_p)^T \in \Theta \subset \mathbb{R}^p$ is a $p \times 1$ parameter vector and $f(\mathbf{x}_i, \boldsymbol{\theta})$ is a known smooth nonlinear expectation function. A regression function $f(\mathbf{x}, \boldsymbol{\theta})$ is Nonlinear in the Parameters whenever at least one partial derivative $\frac{\partial f(\mathbf{x}_i, \boldsymbol{\theta})}{\partial \theta_j}$ is a function of the unknown parameter vector $\boldsymbol{\theta}$.

Statisticians classify nonlinear mechanistic curves into two fundamental categories:
1. **Intrinsically Linear (Transformably Linear) Models**: The deterministic function $f(\mathbf{x}, \boldsymbol{\theta})$ can be transformed into an exact linear form $\mathbf{x}^T \boldsymbol{\beta}$ by a monotonic transformation of the response or covariates. For example, in a multiplicative exponential growth model with **multiplicative log-normal errors** $Y_i = \theta_1 e^{\theta_2 x_i} \cdot u_i$, taking natural logarithms yields $\ln(Y_i) = \ln(\theta_1) + \theta_2 x_i + \ln(u_i)$, which is an exact simple linear regression with $\beta_0 = \ln(\theta_1)$ and $\varepsilon_i = \ln(u_i)$.
2. **Intrinsically Nonlinear Models**: Either the functional form $f(\mathbf{x}, \boldsymbol{\theta})$ cannot be algebraically linearized by any transformation (such as a two-compartment pharmacokinetic sum of exponentials $f(x, \boldsymbol{\theta}) = \theta_1 e^{-\theta_2 x} + \theta_3 e^{-\theta_4 x}$ or a three-parameter asymptotic exponential $f(x, \boldsymbol{\theta}) = \theta_1 - \theta_2 e^{-\theta_3 x}$), **or** the stochastic disturbance $\varepsilon_i$ enters **additively** on the original scale ($Y_i = f(x_i, \boldsymbol{\theta}) + \varepsilon_i$ with $\text{Var}(\varepsilon_i) = \sigma^2$).

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Mechanistic Model</th><th>Nonlinear Regression Function $f(x, \boldsymbol{\theta})$</th><th>Scientific Interpretation of Parameters</th><th>Classical Linearization &amp; Error Distortion</th></tr>
</thead>
<tbody>
<tr><td><strong>Michaelis–Menten Enzyme Kinetics</strong></td><td>$f(x, \boldsymbol{\theta}) = \dfrac{\theta_1 x}{\theta_2 + x}$</td><td>$\theta_1 = V_{\max}$ (asymptotic maximum reaction velocity); $\theta_2 = K_m$ (half-saturation substrate concentration where $f(K_m) = V_{\max}/2$).</td><td><strong>Lineweaver–Burk Double Reciprocal</strong>: $\dfrac{1}{Y} = \dfrac{1}{\theta_1} + \dfrac{\theta_2}{\theta_1}\left(\dfrac{1}{x}\right)$. Severely distorts additive errors ($\text{Var}(1/Y_i) \approx \sigma^2 / \mu_i^4$), giving huge leverage to small noisy $x_i$!</td></tr>
<tr><td><strong>Mono-Molecular / Mitscherlich Growth</strong></td><td>$f(x, \boldsymbol{\theta}) = \theta_1 \left(1 - \theta_2 e^{-\theta_3 x}\right)$</td><td>$\theta_1$: upper carrying capacity asymptote; $\theta_1(1-\theta_2)$: initial response at $x=0$; $\theta_3 > 0$: exponential rate constant.</td><td>Intrinsically nonlinear in $(\theta_1, \theta_2, \theta_3)$ unless the asymptote $\theta_1$ is known a priori.</td></tr>
<tr><td><strong>Three-Parameter Logistic Sigmoid</strong></td><td>$f(x, \boldsymbol{\theta}) = \dfrac{\theta_1}{1 + \exp\left[-(\theta_2 + \theta_3 x)\right]}$</td><td>$\theta_1$: saturation ceiling; $-\theta_2/\theta_3$: inflection point (where $f = \theta_1 / 2$); $\theta_3$: steepness rate parameter.</td><td>Linearizable via $\ln\!\left(\frac{\theta_1 - Y}{Y}\right) = -\theta_2 - \theta_3 x$ only if ceiling $\theta_1$ is known and $0 < Y < \theta_1$.</td></tr>
<tr><td><strong>Gompertz Asymmetric Growth</strong></td><td>$f(x, \boldsymbol{\theta}) = \theta_1 \exp\left(-\theta_2 e^{-\theta_3 x}\right)$</td><td>$\theta_1$: upper asymptote; inflection occurs earlier at $f = \theta_1 / e \approx 0.368 \theta_1$ (used in tumor &amp; actuarial modeling).</td><td>Intrinsically nonlinear when fitted with additive homoscedastic errors $Y_i = f(x_i, \boldsymbol{\theta}) + \varepsilon_i$.</td></tr>
</tbody>
</table></div>

### Why Naive Algebraic Linearization Fails Under Additive Homoscedastic Errors
Consider the Michaelis–Menten enzyme kinetics model $Y_i = \frac{\theta_1 x_i}{\theta_2 + x_i} + \varepsilon_i$ where $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$ represents constant-variance instrument measurement noise on reaction velocity $Y_i$. Biochemists historically inverted both sides to form the **Lineweaver–Burk plot**, regressing $1/Y_i$ on $1/x_i$. By the Delta Method (Section 7.5), if $\text{Var}(Y_i) = \sigma^2$ is constant, then $\text{Var}(1/Y_i) \approx \frac{\sigma^2}{\mu_i^4}$! Thus, at low substrate concentrations $x_i \to 0$ (where $\mu_i$ is small and $1/x_i$ is huge), the transformed error variance explodes as $\mu_i^{-4}$, turning the least-accurate measurements at the lowest concentrations into extreme high-leverage points that corrupt the OLS slope! Fitting the model directly on its natural scale via **Nonlinear Least Squares (NLS)** preserves homoscedasticity and achieves full asymptotic efficiency.

## 8.2 Nonlinear Least Squares (NLS), Gauss-Newton Taylor Linearization, Levenberg-Marquardt, and Asymptotic Inference

In the nonlinear regression model $Y_i = f(\mathbf{x}_i, \boldsymbol{\theta}) + \varepsilon_i$ with $\mathbb{E}[\boldsymbol{\varepsilon}] = \mathbf{0}_n$ and $\text{Cov}(\boldsymbol{\varepsilon}) = \sigma^2 \mathbf{I}_n$, the **Nonlinear Least Squares (NLS) Estimator** $\hat{\boldsymbol{\theta}}$ minimizes the residual sum of squares objective function $S(\boldsymbol{\theta})$:

$$S(\boldsymbol{\theta}) = \sum_{i=1}^n \left[ Y_i - f(\mathbf{x}_i, \boldsymbol{\theta}) \right]^2 = \|\mathbf{Y} - \mathbf{f}(\boldsymbol{\theta})\|_2^2$$

where $\mathbf{f}(\boldsymbol{\theta}) = (f(\mathbf{x}_1, \boldsymbol{\theta}), \dots, f(\mathbf{x}_n, \boldsymbol{\theta}))^T \in \mathbb{R}^n$. Let $\mathbf{J}(\boldsymbol{\theta}) \in \mathbb{R}^{n \times p}$ denote the $n \times p$ **local Jacobian (sensitivity) matrix** of first partial derivatives of the expectation surface with respect to $\boldsymbol{\theta}$:

$$[\mathbf{J}(\boldsymbol{\theta})]_{ij} = \frac{\partial f(\mathbf{x}_i, \boldsymbol{\theta})}{\partial \theta_j}, \quad i = 1, \dots, n, \; j = 1, \dots, p$$

Setting the gradient of $S(\boldsymbol{\theta})$ equal to zero gives the **$p$ Nonlinear Normal Equations**:

$$\nabla_{\boldsymbol{\theta}} S(\boldsymbol{\theta}) = -2 \mathbf{J}(\boldsymbol{\theta})^T \left[ \mathbf{Y} - \mathbf{f}(\boldsymbol{\theta}) \right] = \mathbf{0}_p \iff \sum_{i=1}^n \left. \frac{\partial f(\mathbf{x}_i, \boldsymbol{\theta})}{\partial \theta_j} \right|_{\boldsymbol{\theta} = \hat{\boldsymbol{\theta}}} \left[ Y_i - f(\mathbf{x}_i, \hat{\boldsymbol{\theta}}) \right] = 0 \quad (j = 1, \dots, p)$$

Because both $\mathbf{J}(\hat{\boldsymbol{\theta}})$ and $\mathbf{f}(\hat{\boldsymbol{\theta}})$ are nonlinear functions of $\hat{\boldsymbol{\theta}}$, this system of $p$ nonlinear equations admits **no closed-form analytical solution** and must be solved iteratively.

### 1. The Gauss–Newton Taylor Linearization Algorithm
Given a current parameter iterate $\boldsymbol{\theta}^{(m)}$ at iteration $m$, we approximate the nonlinear expectation vector $\mathbf{f}(\boldsymbol{\theta})$ around $\boldsymbol{\theta}^{(m)}$ via a first-order multivariate Taylor series expansion:

$$\mathbf{f}(\boldsymbol{\theta}) \approx \mathbf{f}(\boldsymbol{\theta}^{(m)}) + \mathbf{J}(\boldsymbol{\theta}^{(m)}) \left( \boldsymbol{\theta} - \boldsymbol{\theta}^{(m)} \right)$$

Substituting this linear approximation into $\mathbf{Y} = \mathbf{f}(\boldsymbol{\theta}) + \boldsymbol{\varepsilon}$ and rearranging terms yields the **Local Linearized Pseudo-Model** at iteration $m$:

$$\underbrace{\mathbf{Y} - \mathbf{f}(\boldsymbol{\theta}^{(m)})}_{\mathbf{e}^{(m)} \text{ (current residuals)}} \approx \mathbf{J}(\boldsymbol{\theta}^{(m)}) \underbrace{\left( \boldsymbol{\theta} - \boldsymbol{\theta}^{(m)} \right)}_{\boldsymbol{\delta}^{(m)} \text{ (step increment)}} + \boldsymbol{\varepsilon}$$

Notice that for fixed $\boldsymbol{\theta}^{(m)}$, estimating the parameter increment vector $\boldsymbol{\delta}^{(m)} = \boldsymbol{\theta}^{(m+1)} - \boldsymbol{\theta}^{(m)}$ is simply an **Ordinary Least Squares regression of the current residual vector $\mathbf{e}^{(m)} = \mathbf{Y} - \mathbf{f}(\boldsymbol{\theta}^{(m)})$ on the current $n \times p$ Jacobian matrix $\mathbf{J}_m = \mathbf{J}(\boldsymbol{\theta}^{(m)})$**! Solving the linearized normal equations $(\mathbf{J}_m^T \mathbf{J}_m) \hat{\boldsymbol{\delta}}^{(m)} = \mathbf{J}_m^T \mathbf{e}^{(m)}$ gives the **Gauss–Newton Iteration**:

$$\boldsymbol{\theta}^{(m+1)} = \boldsymbol{\theta}^{(m)} + \left( \mathbf{J}_m^T \mathbf{J}_m \right)^{-1} \mathbf{J}_m^T \left[ \mathbf{Y} - \mathbf{f}(\boldsymbol{\theta}^{(m)}) \right]$$

To understand how Gauss–Newton relates to full Newton–Raphson optimization, observe that the exact $p \times p$ Hessian matrix of $S(\boldsymbol{\theta})$ is:

$$\nabla_{\boldsymbol{\theta}}^2 S(\boldsymbol{\theta}) = 2 \mathbf{J}(\boldsymbol{\theta})^T \mathbf{J}(\boldsymbol{\theta}) - 2 \sum_{i=1}^n e_i(\boldsymbol{\theta}) \nabla_{\boldsymbol{\theta}}^2 f(\mathbf{x}_i, \boldsymbol{\theta})$$

Because $\mathbb{E}[e_i(\boldsymbol{\theta})] \approx 0$ near the true parameter $\boldsymbol{\theta}$ (and the residuals are small when the model fits well), Gauss–Newton drops the second-derivative intrinsic curvature term $-2 \sum e_i \nabla^2 f_i$ and approximates the Hessian by the positive semi-definite matrix $2 \mathbf{J}_m^T \mathbf{J}_m$ (which is identical to Fisher's Method of Scoring under normal errors!).

### 2. Levenberg–Marquardt Trust-Region Damping
When the initial guess $\boldsymbol{\theta}^{(0)}$ is far from the optimum or when the Jacobian columns are nearly collinear, $\mathbf{J}_m^T \mathbf{J}_m$ can be nearly singular, causing the undamped Gauss–Newton step $\hat{\boldsymbol{\delta}}^{(m)}$ to overshoot wildly and *increase* $S(\boldsymbol{\theta})$. Kenneth Levenberg (1944) and Donald Marquardt (1963) resolved this instability by adding a positive ridge damping parameter $\lambda_m > 0$ (or diagonal scaling $\lambda_m \text{diag}(\mathbf{J}_m^T \mathbf{J}_m)$) to the approximate Hessian:

$$\left( \mathbf{J}_m^T \mathbf{J}_m + \lambda_m \mathbf{I}_p \right) \hat{\boldsymbol{\delta}}^{(m)} = \mathbf{J}_m^T \mathbf{e}^{(m)}$$

The **Levenberg–Marquardt Algorithm** interpolates smoothly between steepest-descent gradient descent (as $\lambda_m \to \infty$, $\hat{\boldsymbol{\delta}}^{(m)} \approx \frac{1}{\lambda_m} \mathbf{J}_m^T \mathbf{e}^{(m)} = -\frac{1}{2\lambda_m} \nabla S$, guaranteeing descent in a small trust region) and quadratic Gauss–Newton convergence (as $\lambda_m \to 0$ near the minimum).

### 3. Asymptotic Distribution and Inference at Convergence
In finite samples, the NLS estimator $\hat{\boldsymbol{\theta}}$ is slightly biased ($\mathbb{E}[\hat{\boldsymbol{\theta}}] \neq \boldsymbol{\theta}$), the residuals do not sum to zero in general ($\sum e_i \neq 0$ unless $\mathbf{1}_n \in \mathcal{C}(\mathbf{J}(\hat{\boldsymbol{\theta}}))$), and $\text{SST} \neq \text{SSR} + \text{SSE}$. However, as $n \to \infty$ under Jennrich's regularity conditions ($\frac{1}{n}\mathbf{J}(\boldsymbol{\theta})^T\mathbf{J}(\boldsymbol{\theta}) \to \mathbf{Q}(\boldsymbol{\theta}) \succ \mathbf{0}$), $\hat{\boldsymbol{\theta}}$ is consistent and asymptotically normal:

$$\hat{\boldsymbol{\theta}} \overset{\text{approx}}{\sim} \mathcal{N}_p \left( \boldsymbol{\theta}, \; s^2 \left[ \hat{\mathbf{J}}^T \hat{\mathbf{J}} \right]^{-1} \right), \qquad \text{where } s^2 = \frac{S(\hat{\boldsymbol{\theta}})}{n - p} \text{ and } \hat{\mathbf{J}} = \mathbf{J}(\hat{\boldsymbol{\theta}})$$

## 8.3 Robust Regression for Heavy-Tailed Contamination: L_1 LAD, Huber M-Estimation, IRLS & Tukey's Biweight

As demonstrated in Unit 4, Ordinary Least Squares is exquisitely sensitive to vertical outliers because its quadratic loss function $\rho_{\text{OLS}}(e_i) = \frac{1}{2} e_i^2$ has an **unbounded influence function** $\psi_{\text{OLS}}(e_i) = \rho_{\text{OLS}}'(e_i) = e_i$: a single gross outlier ($|e_i| \to \infty$) exerts infinite pull on the normal equations $\sum_{i=1}^n \psi(e_i) \mathbf{x}_i = \mathbf{0}_p$, resulting in a finite-sample breakdown point of $\varepsilon^* = \frac{1}{n} \to 0$. When disturbances follow heavy-tailed distributions (such as Laplace, Cauchy, or Student $t_3$) or contain unremovable contamination, **Robust Regression** replaces the squared loss $\frac{1}{2}e_i^2$ with a symmetric, less rapidly growing loss function $\rho(u)$.

Let $\hat{\sigma}$ denote a robust, outlier-resistant scale estimator of the residuals—most commonly the normalized **Median Absolute Deviation (MAD)**:

$$\hat{\sigma}_{\text{MAD}} = \frac{\text{median}_{1 \le i \le n} \left| e_i - \text{median}(e) \right|}{0.6745}$$

where the divisor $\Phi^{-1}(0.75) \approx 0.6745$ makes $\hat{\sigma}_{\text{MAD}}$ a consistent estimator of $\sigma$ when errors are $\mathcal{N}(0, \sigma^2)$ while maintaining a $50\%$ breakdown point! Defining the scaled residual $u_i = \frac{Y_i - \mathbf{x}_i^T \boldsymbol{\beta}}{\hat{\sigma}}$, Peter Huber (1964, 1973) formulated the class of **Regression M-Estimators** (Maximum-Likelihood-Type Estimators), which minimize:

$$Q_M(\boldsymbol{\beta}) = \sum_{i=1}^n \rho\left( \frac{Y_i - \mathbf{x}_i^T \boldsymbol{\beta}}{\hat{\sigma}} \right)$$

Differentiating with respect to $\boldsymbol{\beta}$ and setting the gradient to zero yields the **$p$ Robust Estimating Equations** in terms of the **score (influence) function** $\psi(u) = \rho'(u)$:

$$\sum_{i=1}^n \psi\left( \frac{Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}}{\hat{\sigma}} \right) \mathbf{x}_i = \mathbf{0}_p$$

### The Iteratively Reweighted Least Squares (IRLS) Algorithm for M-Estimation
How do we solve the nonlinear system $\sum_{i=1}^n \psi(u_i) \mathbf{x}_i = \mathbf{0}_p$? Notice the algebraic trick of defining the **robust weight function** $w(u) = \frac{\psi(u)}{u}$ (with $w(0) = \lim_{u \to 0} \frac{\psi(u)}{u} = \psi'(0)$), so that $\psi(u_i) = w(u_i) u_i = w_i \left(\frac{Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}}{\hat{\sigma}}\right)$. Substituting this into the estimating equations and multiplying by $\hat{\sigma}$ transforms the system into:

$$\sum_{i=1}^n w_i \left( Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}} \right) \mathbf{x}_i = \mathbf{0}_p \iff \left( \mathbf{X}^T \mathbf{W}(\hat{\boldsymbol{\beta}}) \mathbf{X} \right) \hat{\boldsymbol{\beta}} = \mathbf{X}^T \mathbf{W}(\hat{\boldsymbol{\beta}}) \mathbf{Y}$$

where $\mathbf{W}(\hat{\boldsymbol{\beta}}) = \text{diag}(w_1, w_2, \dots, w_n)$! This immediately generates the **Iteratively Reweighted Least Squares (IRLS)** algorithm:
1. Start with an initial robust estimate $\hat{\boldsymbol{\beta}}^{(0)}$ (such as $L_1$ regression), compute residuals $e_i^{(m)}$ and $\hat{\sigma}_{\text{MAD}}$, and evaluate standardized residuals $u_i^{(m)} = e_i^{(m)} / \hat{\sigma}_{\text{MAD}}$.
2. Compute the observation weights $w_i^{(m)} = w(u_i^{(m)}) = \psi(u_i^{(m)}) / u_i^{(m)}$ and form $\mathbf{W}^{(m)} = \text{diag}(w_1^{(m)}, \dots, w_n^{(m)})$.
3. Update the parameter vector via Weighted Least Squares: $\hat{\boldsymbol{\beta}}^{(m+1)} = \left(\mathbf{X}^T \mathbf{W}^{(m)} \mathbf{X}\right)^{-1} \mathbf{X}^T \mathbf{W}^{(m)} \mathbf{Y}$, repeating until convergence!

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Estimator Family</th><th>Objective Loss $\rho(u)$</th><th>Influence Score $\psi(u) = \rho'(u)$</th><th>IRLS Weight $w(u) = \psi(u)/u$</th></tr>
</thead>
<tbody>
<tr><td><strong>Ordinary Least Squares ($L_2$)</strong></td><td>$\dfrac{1}{2} u^2$</td><td>$u$ (unbounded linear)</td><td>$w(u) = 1$ (constant equal weight)</td></tr>
<tr><td><strong>Least Absolute Deviations ($L_1$ / LAD)</strong></td><td>$|u|$ (Laplace MLE)</td><td>$\text{sgn}(u) \in \{-1, +1\}$</td><td>$w(u) = \dfrac{1}{|u|}$ (solved via Barrodale–Roberts simplex LP)</td></tr>
<tr><td><strong>Huber Monotone M-Estimator</strong> ($k = 1.345$ for $95\%$ normal efficiency)</td><td>$\begin{cases} \frac{1}{2}u^2, & |u| \le k \\ k|u| - \frac{1}{2}k^2, & |u| > k \end{cases}$</td><td>$\begin{cases} u, & |u| \le k \\ k \, \text{sgn}(u), & |u| > k \end{cases}$</td><td>$\begin{cases} 1, & |u| \le k \\ \dfrac{k}{|u|}, & |u| > k \end{cases}$ (downweights tails as $1/|u|$)</td></tr>
<tr><td><strong>Tukey's Redescending Biweight (Bisquare)</strong> ($c = 4.685$ for $95\%$ normal efficiency)</td><td>$\begin{cases} \frac{c^2}{6}\left[1 - \left(1 - \frac{u^2}{c^2}\right)^3\right], & |u| \le c \\ \frac{c^2}{6}, & |u| > c \end{cases}$</td><td>$\begin{cases} u\left(1 - \frac{u^2}{c^2}\right)^2, & |u| \le c \\ 0, & |u| > c \end{cases}$</td><td>$\begin{cases} \left(1 - \frac{u^2}{c^2}\right)^2, & |u| \le c \\ 0, & |u| > c \end{cases}$ (completely rejects $|u| > c$!)</td></tr>
</tbody>
</table></div>

Note that while monotone M-estimators (Huber) and $L_1$ regression bound the influence of vertical outliers in $Y$, they remain vulnerable to **bad high-leverage points in $\mathbf{X}$** because the estimating equation multiplies $\psi(u_i)$ by the unbounded covariate vector $\mathbf{x}_i$. Achieving high breakdown ($50\%$) against simultaneous $(\mathbf{x}_i, Y_i)$ leverage contamination requires **Generalized M-estimators (Bounded-Influence GM / Mallows–Schweppe)**, Peter Rousseeuw's **Least Trimmed Squares (LTS)** (which minimizes the sum of the smallest $h \approx \lfloor n/2 \rfloor + \lfloor (p+1)/2 \rfloor$ squared residuals), or **MM-Estimation** (which initializes Tukey's biweight IRLS from a $50\%$-breakdown S-estimator).

## 8.4 Generalized Linear Models (GLMs): Exponential Dispersion Family, Canonical Links & Fisher Scoring IRLS

When the response variable $Y_i$ is intrinsically discrete or bounded—such as a binary clinical outcome $Y_i \in \{0, 1\}$, a binomial proportion $Y_i / m_i \in [0, 1]$, a non-negative integer Poisson count $Y_i \in \{0, 1, 2, \dots\}$, or a strictly positive skewed Gamma survival time $Y_i > 0$—classical linear regression $Y_i = \mathbf{x}_i^T \boldsymbol{\beta} + \varepsilon_i$ breaks down fundamentally: an unbounded linear predictor $\mathbf{x}_i^T \boldsymbol{\beta} \in (-\infty, \infty)$ predicts impossible negative counts or probabilities outside $[0, 1]$, and the variance of $Y_i$ is functionally tied to its mean $\mu_i$.

In a landmark 1972 paper, **John Nelder and Robert Wedderburn** unified linear, logistic, probit, Poisson, and Gamma regression under the **Generalized Linear Model (GLM)** framework, which consists of three structural components:

### 1. The Random Component: Exponential Dispersion Family
Each independent response $Y_i$ follows a probability density or mass function in the **Exponential Dispersion Family** with canonical (natural) parameter $\theta_i$ and dispersion parameter $\phi > 0$:

$$f(y_i; \theta_i, \phi) = \exp\left\{ \frac{y_i \theta_i - b(\theta_i)}{a(\phi)} + c(y_i, \phi) \right\}$$

where $a(\phi) = \phi / w_i$ ($w_i$ being a known prior weight) and $b(\theta_i)$ is a twice-differentiable convex **cumulant function**. Applying Bartlett's first and second log-likelihood identities ($\mathbb{E}[\frac{\partial \ell_i}{\partial \theta_i}] = 0$ and $\mathbb{E}[\frac{\partial^2 \ell_i}{\partial \theta_i^2}] + \mathbb{E}[(\frac{\partial \ell_i}{\partial \theta_i})^2] = 0$) immediately determines the mean $\mu_i$ and variance $\text{Var}(Y_i)$ in terms of derivatives of $b(\theta_i)$:

$$\frac{\partial \ell_i}{\partial \theta_i} = \frac{Y_i - b'(\theta_i)}{a(\phi)} \implies \mu_i = \mathbb{E}[Y_i] = b'(\theta_i)$$

$$\frac{\partial^2 \ell_i}{\partial \theta_i^2} = -\frac{b''(\theta_i)}{a(\phi)} \implies \text{Var}(Y_i) = a(\phi) \, b''(\theta_i) = a(\phi) \, V(\mu_i)$$

where $V(\mu_i) = b''\left((b')^{-1}(\mu_i)\right) = \frac{d\mu_i}{d\theta_i}$ is the **GLM Variance Function**, capturing how the variance of $Y_i$ depends on its mean $\mu_i$!

### 2. The Systematic Component: Linear Predictor $\eta_i$
The $p$ covariates enter purely through the linear predictor $\eta_i = \mathbf{x}_i^T \boldsymbol{\beta}$ ($\boldsymbol{\eta} = \mathbf{X}\boldsymbol{\beta}$).

### 3. The Link Function $g(\mu_i) = \eta_i$
A smooth, strictly monotonic differentiable **link function** $g(\cdot)$ maps the restricted domain of the conditional mean $\mu_i = \mathbb{E}[Y_i \mid \mathbf{x}_i]$ onto the entire real line $(-\infty, \infty)$ of the linear predictor:

$$\eta_i = g(\mu_i) = \mathbf{x}_i^T \boldsymbol{\beta} \iff \mu_i = g^{-1}(\mathbf{x}_i^T \boldsymbol{\beta})$$

Notice the fundamental distinction between transforming the data $\mathbb{E}[g(Y_i)]$ (Section 7.5) and transforming the population mean $g(\mathbb{E}[Y_i])$ in a GLM: a log-link GLM sets $\ln(\mathbb{E}[Y_i]) = \mathbf{x}_i^T\boldsymbol{\beta}$ without ever taking $\ln(Y_i)$, so observed zeros $Y_i = 0$ pose no problem whatsoever! The special link function $g(\mu_i) = \theta_i = (b')^{-1}(\mu_i)$ that equates the linear predictor directly to the natural parameter ($\theta_i = \eta_i = \mathbf{x}_i^T\boldsymbol{\beta}$) is called the **Canonical Link Function**. Under the canonical link, $\mathbf{X}^T \mathbf{Y}$ is a minimal sufficient statistic for $\boldsymbol{\beta}$, and the observed Hessian equals the expected Fisher Information matrix!

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Distribution</th><th>Cumulant $b(\theta)$</th><th>Mean $\mu = b'(\theta)$</th><th>Variance Function $V(\mu)$</th><th>Canonical Link $\theta = g(\mu)$</th></tr>
</thead>
<tbody>
<tr><td><strong>Normal $\mathcal{N}(\mu, \sigma^2)$</strong></td><td>$\dfrac{\theta^2}{2}$</td><td>$\mu = \theta$</td><td>$V(\mu) = 1$ ($\phi = \sigma^2$)</td><td><strong>Identity</strong>: $g(\mu) = \mu$</td></tr>
<tr><td><strong>Bernoulli / Binomial</strong></td><td>$\ln(1 + e^\theta)$</td><td>$\pi = \dfrac{e^\theta}{1 + e^\theta}$</td><td>$V(\pi) = \pi(1 - \pi)$ ($\phi = 1$)</td><td><strong>Logit</strong>: $g(\pi) = \ln\!\left(\dfrac{\pi}{1 - \pi}\right)$</td></tr>
<tr><td><strong>Poisson $\text{Pois}(\mu)$</strong></td><td>$e^\theta$</td><td>$\mu = e^\theta$</td><td>$V(\mu) = \mu$ ($\phi = 1$)</td><td><strong>Log</strong>: $g(\mu) = \ln(\mu)$</td></tr>
<tr><td><strong>Gamma $\text{Gamma}(\nu, \mu)$</strong></td><td>$-\ln(-\theta)$</td><td>$\mu = -\dfrac{1}{\theta}$</td><td>$V(\mu) = \mu^2$ ($\phi = \nu^{-1}$)</td><td><strong>Negative Reciprocal</strong>: $g(\mu) = -\dfrac{1}{\mu}$ (or Log)</td></tr>
</tbody>
</table></div>

### 4. Maximum Likelihood Estimation via Fisher Scoring and IRLS
By the chain rule $\frac{\partial \ell_i}{\partial \beta_j} = \frac{\partial \ell_i}{\partial \theta_i} \frac{d \theta_i}{d \mu_i} \frac{d \mu_i}{d \eta_i} \frac{\partial \eta_i}{\partial \beta_j}$, where $\frac{d\theta_i}{d\mu_i} = \frac{1}{V(\mu_i)}$, $\frac{d\mu_i}{d\eta_i} = \frac{1}{g'(\mu_i)}$, and $\frac{\partial \eta_i}{\partial \beta_j} = x_{ij}$, the **GLM Score Equations** and **Fisher Information Matrix** $\mathcal{I}(\boldsymbol{\beta})$ are:

$$\mathbf{U}(\boldsymbol{\beta}) = \frac{1}{\phi} \sum_{i=1}^n \frac{Y_i - \mu_i}{V(\mu_i) \, g'(\mu_i)} \mathbf{x}_i = \mathbf{0}_p, \qquad \mathcal{I}(\boldsymbol{\beta}) = \frac{1}{\phi} \mathbf{X}^T \mathbf{W} \mathbf{X}$$

where $\mathbf{W} = \text{diag}(w_1, \dots, w_n)$ has **GLM working weights** $w_i = \frac{1}{V(\mu_i) [g'(\mu_i)]^2}$ (which simplify to $w_i = V(\mu_i)$ under the canonical link since $g'(\mu_i) = 1/V(\mu_i)$!).Defining the **working dependent variable (adjusted response)** $z_i = \eta_i + (Y_i - \mu_i) g'(\mu_i)$, each Fisher Scoring step $\boldsymbol{\beta}^{(m+1)} = \boldsymbol{\beta}^{(m)} + [\mathcal{I}(\boldsymbol{\beta}^{(m)})]^{-1} \mathbf{U}(\boldsymbol{\beta}^{(m)})$ reduces to an **Iteratively Reweighted Least Squares (IRLS)** update:

$$\boldsymbol{\beta}^{(m+1)} = \left( \mathbf{X}^T \mathbf{W}^{(m)} \mathbf{X} \right)^{-1} \mathbf{X}^T \mathbf{W}^{(m)} \mathbf{z}^{(m)}, \qquad \widehat{\text{Cov}}(\hat{\boldsymbol{\beta}}) = \hat{\phi} \left( \mathbf{X}^T \hat{\mathbf{W}} \mathbf{X} \right)^{-1}$$

## 8.5 Binary Logistic Regression: Logit Link, Odds Ratios, Deviance Tests, and IRLS

When the response variable is a binary Bernoulli indicator $Y_i \in \{0, 1\}$ (or a grouped binomial count $Y_i \sim \text{Binomial}(m_i, \pi_i)$) representing the occurrence of an event such as disease presence, loan default, or customer churn, our target is the conditional success probability $\pi(\mathbf{x}_i) = \mathbb{P}(Y_i = 1 \mid \mathbf{x}_i) = \mathbb{E}[Y_i \mid \mathbf{x}_i] \in (0, 1)$.

Fitting a naive **Linear Probability Model (LPM)** $\pi(\mathbf{x}_i) = \mathbf{x}_i^T \boldsymbol{\beta}$ via Ordinary Least Squares suffers from three fatal statistical defects:
1. **Unbounded Predictions**: Because $\mathbf{x}_i^T \boldsymbol{\beta}$ is linear and unbounded, it inevitably predicts nonsensical probabilities $\hat{\pi}_i < 0$ or $\hat{\pi}_i > 1$ for extreme covariate values.
2. **Inherent Heteroscedasticity**: Since $Y_i \in \{0, 1\}$ is Bernoulli, its error term $\varepsilon_i = Y_i - \pi_i$ takes only two discrete values ($1 - \pi_i$ and $-\pi_i$) with variance $\text{Var}(\varepsilon_i) = \pi_i(1 - \pi_i)$, violating homoscedasticity and invalidating OLS standard errors.
3. **Constant Marginal Effects**: A one-unit increase in $x_j$ changes $\pi$ by $\beta_j$ identically whether $\pi = 0.50$ or $\pi = 0.99$.

### 1. The Logistic Sigmoid Function, Logit Link, and Odds Ratio Interpretation
**Binary Logistic Regression** resolves all three defects by modeling $\pi(\mathbf{x}_i)$ via the **standard logistic cumulative distribution function (sigmoid curve)** $\pi(\eta) = \frac{e^\eta}{1 + e^\eta} = \frac{1}{1 + e^{-\eta}} \in (0, 1)$, whose inverse is the canonical **Logit (Log-Odds) Link Function**:

$$\eta_i = \text{logit}(\pi_i) = \ln\left( \frac{\pi_i}{1 - \pi_i} \right) = \beta_0 + \beta_1 x_{i1} + \dots + \beta_k x_{ik} = \mathbf{x}_i^T \boldsymbol{\beta}$$

Here, the ratio $\Omega(\mathbf{x}_i) = \frac{\pi(\mathbf{x}_i)}{1 - \pi(\mathbf{x}_i)} = \exp(\mathbf{x}_i^T \boldsymbol{\beta}) \in (0, \infty)$ is the **Odds of Success** at covariate vector $\mathbf{x}_i$. How do we interpret an individual slope coefficient $\beta_j$? Increase predictor $x_j$ by $1$ unit while holding all other covariates constant:

$$\ln\left(\text{Odds}(x_j + 1)\right) - \ln\left(\text{Odds}(x_j)\right) = \beta_j \iff \text{OR}_j = \frac{\text{Odds}(x_j + 1)}{\text{Odds}(x_j)} = e^{\beta_j}$$

Thus, $\beta_j$ is the **change in log-odds per unit increase in $x_j$**, and $\exp(\beta_j)$ is the **Multiplicative Odds Ratio ($\text{OR}_j$)**! If $\beta_j > 0$, $e^{\beta_j} > 1$ (odds increase by $100(e^{\beta_j} - 1)\%$ per unit increase in $x_j$); if $\beta_j = 0$, $e^{\beta_j} = 1$ (odds unchanged); if $\beta_j < 0$, $0 < e^{\beta_j} < 1$ (odds decrease). Furthermore, on the probability scale, differentiating $\pi(\mathbf{x})$ with respect to $x_j$ gives the **Marginal Probability Effect**:

$$\frac{\partial \pi(\mathbf{x})}{\partial x_j} = \beta_j \, \pi(\mathbf{x}) \left[ 1 - \pi(\mathbf{x}) \right]$$

which achieves its steepest slope $\frac{1}{4}\beta_j$ at the median effective dose ($\pi = 0.50$, where $\mathbf{x}^T\boldsymbol{\beta} = 0$, so $\text{LD}_{50} = -\beta_0 / \beta_1$ in simple logistic regression) and flattens gracefully toward zero as $\pi \to 0$ or $\pi \to 1$.

### 2. Log-Likelihood, IRLS Working Equations, Wald Tests, and Deviance Goodness-of-Fit
For $n$ independent Bernoulli observations $Y_i \in \{0, 1\}$, the log-likelihood function is:

$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ Y_i \ln(\pi_i) + (1 - Y_i) \ln(1 - \pi_i) \right] = \sum_{i=1}^n \left[ Y_i (\mathbf{x}_i^T \boldsymbol{\beta}) - \ln\left(1 + e^{\mathbf{x}_i^T \boldsymbol{\beta}}\right) \right]$$

Setting the score vector to zero gives the **Logistic Likelihood Equations** $\mathbf{U}(\hat{\boldsymbol{\beta}}) = \mathbf{X}^T (\mathbf{Y} - \hat{\boldsymbol{\pi}}) = \mathbf{0}_p$. Specializing the GLM IRLS algorithm of Section 8.4 to the canonical logit link ($V(\pi_i) = \pi_i(1 - \pi_i)$, $g'(\pi_i) = \frac{1}{\pi_i(1 - \pi_i)}$, $\phi = 1$), the **IRLS weight matrix** and **working response** at iteration $m$ are:

$$\mathbf{W}^{(m)} = \text{diag}\left( \pi_1^{(m)}(1 - \pi_1^{(m)}), \dots, \pi_n^{(m)}(1 - \pi_n^{(m)}) \right), \qquad z_i^{(m)} = \mathbf{x}_i^T \boldsymbol{\beta}^{(m)} + \frac{Y_i - \pi_i^{(m)}}{\pi_i^{(m)}(1 - \pi_i^{(m)})}$$

At convergence, $\hat{\boldsymbol{\beta}} \overset{\text{approx}}{\sim} \mathcal{N}_p\left(\boldsymbol{\beta}, (\mathbf{X}^T \hat{\mathbf{W}} \mathbf{X})^{-1}\right)$. Hypothesis testing in logistic regression employs:
1. **Wald Test**: $z_j = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)} \overset{d}{\to} \mathcal{N}(0, 1)$ (or $W_j = z_j^2 \sim \chi_1^2$), and the $95\%$ CI for the Odds Ratio is $\exp\left(\hat{\beta}_j \pm 1.96 \, \text{SE}(\hat{\beta}_j)\right)$. *(Caution: the Hauck–Donner effect shows that for huge $|\hat{\beta}_j|$, $\hat{\pi}_i(1 - \hat{\pi}_i) \to 0$ inflates $\text{SE}(\hat{\beta}_j)$, making the Wald statistic lose power; the Likelihood Ratio / Deviance test is always preferred!).*
2. **Residual Deviance $D$ and Likelihood Ratio Drop-in-Deviance Test**: The **Residual Deviance** is twice the log-likelihood ratio between the saturated model ($\tilde{\pi}_i = Y_i / m_i$) and the fitted model:
   $$D = -2 \left[ \ell(\hat{\boldsymbol{\beta}}) - \ell_{\text{sat}} \right] = 2 \sum_{i=1}^n \left[ Y_i \ln\left(\frac{Y_i}{\hat{\mu}_i}\right) + (m_i - Y_i) \ln\left(\frac{m_i - Y_i}{m_i - \hat{\mu}_i}\right) \right]$$
   To test a nested Reduced model $M_R$ ($p_R$ parameters) against a Full model $M_F$ ($p_F$ parameters), the **Drop-in-Deviance (Likelihood Ratio) Statistic** is:
   $$\Delta D = D_R - D_F = -2 \left[ \ell(\hat{\boldsymbol{\beta}}_R) - \ell(\hat{\boldsymbol{\beta}}_F) \right] \xrightarrow{d} \chi_{p_F - p_R}^2 \quad \text{under } H_0$$
   For ungrouped binary data ($m_i = 1$), overall goodness of fit is evaluated via the **Hosmer–Lemeshow Test**, which partitions observations into $G = 10$ deciles of predicted risk $\hat{\pi}_i$ and compares observed vs. expected event counts via a $\chi_{G-2}^2 = \chi_8^2$ statistic.

## 8.6 Poisson Log-Linear Regression for Count Data, Rate Offsets, Overdispersion & Quasi-Poisson / Negative Binomial Models

When the response variable $Y_i \in \{0, 1, 2, \dots\}$ represents a non-negative integer count of discrete events occurring within a fixed spatial or temporal window—such as hospital emergency admissions per day, highway traffic accidents per intersection, or defective microchips per silicon wafer—the benchmark generalized linear model is **Poisson Log-Linear Regression**.

### 1. The Poisson Log-Linear Model, Rate Ratios, and Exposure Offsets
Assume $Y_i \sim \text{Poisson}(\mu_i)$ independently with probability mass function $f(y_i; \mu_i) = \frac{e^{-\mu_i} \mu_i^{y_i}}{y_i!}$ for $y_i = 0, 1, 2, \dots$, where the mean and variance satisfy the **equidispersion property** $\mathbb{E}[Y_i] = \text{Var}(Y_i) = \mu_i > 0$. Using the canonical **logarithmic link function** $g(\mu_i) = \ln(\mu_i) = \eta_i$ guarantees that the predicted mean count $\mu_i = \exp(\mathbf{x}_i^T \boldsymbol{\beta}) > 0$ is strictly positive for all $\boldsymbol{\beta} \in \mathbb{R}^p$:

$$\ln(\mu_i) = \beta_0 + \beta_1 x_{i1} + \dots + \beta_k x_{ik} = \mathbf{x}_i^T \boldsymbol{\beta} \iff \mu_i = \exp\left( \mathbf{x}_i^T \boldsymbol{\beta} \right) = e^{\beta_0} e^{\beta_1 x_{i1}} \cdots e^{\beta_k x_{ik}}$$

Because the covariates act multiplicatively on the expected count $\mu_i$, exponentiating an individual regression slope $\beta_j$ yields the **Incidence Rate Ratio ($\text{IRR}_j$)** (or **Relative Risk**):

$$\text{IRR}_j = \frac{\mathbb{E}[Y \mid x_j + 1, \mathbf{x}_{(-j)}]}{\mathbb{E}[Y \mid x_j, \mathbf{x}_{(-j)}]} = \exp(\beta_j)$$

That is, a one-unit increase in $x_j$ multiplies the expected count by $e^{\beta_j}$ (a $100(e^{\beta_j} - 1)\%$ percentage change).

In many epidemiological and actuarial studies, the counts $Y_i$ are observed over unequal **exposure denominators** $t_i > 0$ (such as person-years at risk, population size, or kilometers of highway), and we wish to model the underlying **event rate** $\lambda_i = \frac{\mu_i}{t_i}$. Taking logarithms of $\frac{\mu_i}{t_i} = \exp(\mathbf{x}_i^T \boldsymbol{\beta})$ gives:

$$\ln\left( \frac{\mu_i}{t_i} \right) = \mathbf{x}_i^T \boldsymbol{\beta} \iff \ln(\mu_i) = \underbrace{1.0 \cdot \ln(t_i)}_{\text{Offset Term}} + \mathbf{x}_i^T \boldsymbol{\beta} \iff \mu_i = t_i \exp(\mathbf{x}_i^T \boldsymbol{\beta})$$

Here, $\ln(t_i)$ enters the linear predictor as an **Offset Variable**—a known regressor whose slope coefficient is constrained to equal exactly $1.0$ without being estimated!

### 2. Score Equations, IRLS Weights, and Poisson Deviance
The Poisson log-likelihood is $\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ Y_i (\mathbf{x}_i^T\boldsymbol{\beta}) - \exp(\mathbf{x}_i^T\boldsymbol{\beta}) - \ln(Y_i!) \right]$, yielding the score equations $\mathbf{U}(\hat{\boldsymbol{\beta}}) = \mathbf{X}^T(\mathbf{Y} - \hat{\boldsymbol{\mu}}) = \mathbf{0}_p$, the IRLS weight matrix $\mathbf{W} = \text{diag}(\mu_1, \dots, \mu_n)$, working response $z_i = \eta_i + \frac{Y_i - \mu_i}{\mu_i}$, and asymptotic covariance $\widehat{\text{Cov}}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}^T \hat{\mathbf{W}} \mathbf{X})^{-1}$. The **Poisson Residual Deviance** and **Pearson Chi-Square Statistic** are:

$$D = 2 \sum_{i=1}^n \left[ Y_i \ln\left(\frac{Y_i}{\hat{\mu}_i}\right) - (Y_i - \hat{\mu}_i) \right], \qquad X^2 = \sum_{i=1}^n \frac{(Y_i - \hat{\mu}_i)^2}{\hat{\mu}_i}$$

(with $0 \ln(0) \equiv 0$). Notice that whenever an intercept is included, the first score equation $\sum_{i=1}^n (Y_i - \hat{\mu}_i) = 0$ forces the sum of fitted counts to equal the sum of observed counts ($\sum \hat{\mu}_i = \sum Y_i$), simplifying the deviance to $D = 2 \sum_{i=1}^n Y_i \ln(Y_i / \hat{\mu}_i)$.

### 3. Overdispersion Diagnostics and Quasi-Poisson vs Negative Binomial Remedies
In real-world count data, unobserved individual heterogeneity (frailty) or event clustering almost always causes the empirical variance to exceed the conditional mean ($\text{Var}(Y_i) > \mu_i$), a phenomenon called **Overdispersion**. When a well-specified Poisson model holds ($\phi = 1$), both $D / (n - p)$ and $X^2 / (n - p)$ should hover near $1.0$. If the estimated **dispersion parameter** $\hat{\phi}$:

$$\hat{\phi} = \frac{X^2}{n - p} = \frac{1}{n - p} \sum_{i=1}^n \frac{(Y_i - \hat{\mu}_i)^2}{\hat{\mu}_i} \gg 1.0$$

exceeds unity substantially, standard Poisson standard errors are severely biased downward (producing spuriously large Wald $z$-statistics). Two standard remedies are used:
1. **Quasi-Poisson GLM (Wedderburn Quasi-Likelihood)**: Postulates $\mathbb{E}[Y_i] = \mu_i$ and $\text{Var}(Y_i) = \phi \mu_i$ ($\phi > 1$). Because $\phi$ cancels out of the score equation $\frac{1}{\phi}\mathbf{X}^T(\mathbf{Y} - \boldsymbol{\mu}) = \mathbf{0}_p$, the point estimates $\hat{\boldsymbol{\beta}}$ are identical to ordinary Poisson MLE, while all standard errors are multiplied by the overdispersion inflation factor $\sqrt{\hat{\phi}}$, and drop-in-deviance tests use $F = \frac{(D_R - D_F)/q}{\hat{\phi}} \sim F_{q, n-p}$.
2. **Negative Binomial Regression (Poisson–Gamma Mixture)**: Assumes $Y_i \mid u_i \sim \text{Poisson}(\mu_i u_i)$ where the unobserved frailty $u_i \sim \text{Gamma}(\alpha^{-1}, \alpha^{-1})$ has mean $1$ and variance $\alpha > 0$. Integrating out $u_i$ yields a Negative Binomial marginal distribution with mean $\mathbb{E}[Y_i] = \mu_i$ and **quadratic variance function** $\text{Var}(Y_i) = \mu_i + \alpha \mu_i^2$, allowing full likelihood inference and testing $H_0: \alpha = 0$.

## Worked Questions and Solutions

### Question 1: Nonlinear Least Squares (NLS): One-Step Gauss-Newton Linearization & Asymptotic Standard Errors for Michaelis-Menten Kinetics

A biochemistry laboratory measures initial enzymatic reaction velocity $Y_i$ across $n = 4$ substrate concentrations $x_i \in \{1, 2, 4, 8\}$ (in mM) to estimate the **Michaelis–Menten nonlinear regression model**:

$$Y_i = f(x_i, \boldsymbol{\theta}) + \varepsilon_i = \frac{\theta_1 x_i}{\theta_2 + x_i} + \varepsilon_i, \qquad \begin{array}{c|cccc} x_i & 1 & 2 & 4 & 8 \\ \hline Y_i & 4.2 & 6.5 & 8.4 & 10.2 \end{array}$$

Starting from the initial parameter vector $\boldsymbol{\theta}^{(0)} = (\theta_1^{(0)}, \theta_2^{(0)})^T = (12.0, \; 2.0)^T$:

1. Derive the analytical partial derivatives $J_{i1}(\boldsymbol{\theta}) = \frac{\partial f(x_i, \boldsymbol{\theta})}{\partial \theta_1}$ and $J_{i2}(\boldsymbol{\theta}) = \frac{\partial f(x_i, \boldsymbol{\theta})}{\partial \theta_2}$, and evaluate the $4 \times 1$ initial residual vector $\mathbf{e}^{(0)} = \mathbf{Y} - \mathbf{f}(\boldsymbol{\theta}^{(0)})$, the initial sum of squared residuals $S(\boldsymbol{\theta}^{(0)})$, and the $4 \times 2$ Jacobian matrix $\mathbf{J}_0 = \mathbf{J}(\boldsymbol{\theta}^{(0)})$.
2. Compute $\mathbf{J}_0^T \mathbf{J}_0$, $\mathbf{J}_0^T \mathbf{e}^{(0)}$, the Gauss–Newton step increment $\hat{\boldsymbol{\delta}}^{(0)} = (\mathbf{J}_0^T \mathbf{J}_0)^{-1} \mathbf{J}_0^T \mathbf{e}^{(0)}$, and the updated parameter vector $\boldsymbol{\theta}^{(1)} = \boldsymbol{\theta}^{(0)} + \hat{\boldsymbol{\delta}}^{(0)}$.
3. Verify that $S(\boldsymbol{\theta}^{(1)}) < S(\boldsymbol{\theta}^{(0)})$, and taking $\boldsymbol{\theta}^{(1)}$ as the converged NLS estimate with $\mathbf{J}_0^T \mathbf{J}_0$ as the approximate information matrix, compute the asymptotic standard errors $\text{SE}(\hat{\theta}_1)$ and $\text{SE}(\hat{\theta}_2)$.

### Solution, step 1: Derive analytical Jacobian entries and evaluate e^(0), S(theta^(0)), and J_0
Differentiating $f(x_i, \boldsymbol{\theta}) = \frac{\theta_1 x_i}{\theta_2 + x_i}$ with respect to $\theta_1$ and $\theta_2$ gives the Jacobian columns:

$$J_{i1}(\boldsymbol{\theta}) = \frac{\partial f(x_i, \boldsymbol{\theta})}{\partial \theta_1} = \frac{x_i}{\theta_2 + x_i}, \qquad J_{i2}(\boldsymbol{\theta}) = \frac{\partial f(x_i, \boldsymbol{\theta})}{\partial \theta_2} = -\frac{\theta_1 x_i}{(\theta_2 + x_i)^2}$$

At $\boldsymbol{\theta}^{(0)} = (12.0, \; 2.0)^T$, we evaluate $f_i^{(0)} = \frac{12 x_i}{2 + x_i}$, $e_i^{(0)} = Y_i - f_i^{(0)}$, $J_{i1}^{(0)} = \frac{x_i}{2 + x_i}$, and $J_{i2}^{(0)} = -\frac{12 x_i}{(2 + x_i)^2}$ across the $n = 4$ points:
- $x_1 = 1$: $f_1^{(0)} = \frac{12}{3} = 4.000 \implies e_1^{(0)} = 4.2 - 4.0 = +0.200$, $J_{11}^{(0)} = \frac{1}{3} \approx 0.3333$, $J_{12}^{(0)} = -\frac{12}{9} \approx -1.3333$.
- $x_2 = 2$: $f_2^{(0)} = \frac{24}{4} = 6.000 \implies e_2^{(0)} = 6.5 - 6.0 = +0.500$, $J_{21}^{(0)} = \frac{2}{4} = 0.5000$, $J_{22}^{(0)} = -\frac{24}{16} = -1.5000$.
- $x_3 = 4$: $f_3^{(0)} = \frac{48}{6} = 8.000 \implies e_3^{(0)} = 8.4 - 8.0 = +0.400$, $J_{31}^{(0)} = \frac{4}{6} \approx 0.6667$, $J_{32}^{(0)} = -\frac{48}{36} \approx -1.3333$.
- $x_4 = 8$: $f_4^{(0)} = \frac{96}{10} = 9.600 \implies e_4^{(0)} = 10.2 - 9.6 = +0.600$, $J_{41}^{(0)} = \frac{8}{10} = 0.8000$, $J_{42}^{(0)} = -\frac{96}{100} = -0.9600$.

The initial sum of squared residuals is $S(\boldsymbol{\theta}^{(0)}) = (0.2)^2 + (0.5)^2 + (0.4)^2 + (0.6)^2 = 0.04 + 0.25 + 0.16 + 0.36 = 0.8100$, and:

$$\mathbf{J}_0 = \begin{pmatrix} 1/3 & -4/3 \\ 1/2 & -3/2 \\ 2/3 & -4/3 \\ 4/5 & -24/25 \end{pmatrix}, \qquad \mathbf{e}^{(0)} = \begin{pmatrix} 0.20 \\ 0.50 \\ 0.40 \\ 0.60 \end{pmatrix}$$

### Solution, step 2: Compute J_0^T J_0, J_0^T e^(0), and execute the Gauss-Newton step
We compute the $2 \times 2$ matrix $\mathbf{J}_0^T \mathbf{J}_0$ and the $2 \times 1$ vector $\mathbf{J}_0^T \mathbf{e}^{(0)}$:
- $(\mathbf{J}_0^T \mathbf{J}_0)_{11} = (1/3)^2 + (1/2)^2 + (2/3)^2 + (4/5)^2 = \frac{1}{9} + \frac{1}{4} + \frac{4}{9} + \frac{16}{25} = 0.5556 + 0.2500 + 0.6400 = 1.4456$
- $(\mathbf{J}_0^T \mathbf{J}_0)_{22} = (-4/3)^2 + (-3/2)^2 + (-4/3)^2 + (-0.96)^2 = \frac{16}{9} + \frac{9}{4} + \frac{16}{9} + 0.9216 = 3.5556 + 2.2500 + 0.9216 = 6.7272$
- $(\mathbf{J}_0^T \mathbf{J}_0)_{12} = (1/3)(-4/3) + (1/2)(-3/2) + (2/3)(-4/3) + (0.8)(-0.96) = -\frac{4}{9} - \frac{3}{4} - \frac{8}{9} - 0.768 = -1.3333 - 0.7500 - 0.7680 = -2.8513$
- $(\mathbf{J}_0^T \mathbf{e}^{(0)})_1 = (1/3)(0.2) + (1/2)(0.5) + (2/3)(0.4) + (0.8)(0.6) = 0.0667 + 0.2500 + 0.2667 + 0.4800 = 1.0633$
- $(\mathbf{J}_0^T \mathbf{e}^{(0)})_2 = (-4/3)(0.2) + (-3/2)(0.5) + (-4/3)(0.4) + (-0.96)(0.6) = -0.2667 - 0.7500 - 0.5333 - 0.5760 = -2.1260$

With $\det(\mathbf{J}_0^T \mathbf{J}_0) = (1.4456)(6.7272) - (-2.8513)^2 = 9.7248 - 8.1301 = 1.5947$:

$$(\mathbf{J}_0^T \mathbf{J}_0)^{-1} = \frac{1}{1.5947} \begin{pmatrix} 6.7272 & 2.8513 \\ 2.8513 & 1.4456 \end{pmatrix} = \begin{pmatrix} 4.2185 & 1.7880 \\ 1.7880 & 0.9065 \end{pmatrix}$$

$$\hat{\boldsymbol{\delta}}^{(0)} = (\mathbf{J}_0^T \mathbf{J}_0)^{-1} \mathbf{J}_0^T \mathbf{e}^{(0)} = \begin{pmatrix} 4.2185(1.0633) + 1.7880(-2.1260) \\ 1.7880(1.0633) + 0.9065(-2.1260) \end{pmatrix} = \begin{pmatrix} 4.4857 - 3.8013 \\ 1.9012 - 1.9272 \end{pmatrix} = \begin{pmatrix} +0.6844 \\ -0.0260 \end{pmatrix}$$

Updating $\boldsymbol{\theta}^{(1)} = \boldsymbol{\theta}^{(0)} + \hat{\boldsymbol{\delta}}^{(0)}$ gives:

$$\boldsymbol{\theta}^{(1)} = \begin{pmatrix} 12.0000 \\ 2.0000 \end{pmatrix} + \begin{pmatrix} +0.6844 \\ -0.0260 \end{pmatrix} = \begin{pmatrix} 12.6844 \\ 1.9740 \end{pmatrix}$$

### Solution, step 3: Verify reduction in S(theta^(1)) and compute asymptotic standard errors
Evaluating $f(x_i, \boldsymbol{\theta}^{(1)}) = \frac{12.6844 x_i}{1.9740 + x_i}$ at $x_i \in \{1, 2, 4, 8\}$ gives fitted values $\mathbf{f}(\boldsymbol{\theta}^{(1)}) = (4.265, \; 6.384, \; 8.493, \; 10.174)^T$ and residuals $\mathbf{e}^{(1)} = (-0.065, \; +0.116, \; -0.093, \; +0.026)^T$, whose sum of squares is:

$$S(\boldsymbol{\theta}^{(1)}) = (-0.065)^2 + (0.116)^2 + (-0.093)^2 + (0.026)^2 = 0.0042 + 0.0135 + 0.0086 + 0.0007 = 0.0270 \ll S(\boldsymbol{\theta}^{(0)}) = 0.8100$$

A single Gauss–Newton step reduced the residual sum of squares by **$96.7\%$**! With $n - p = 4 - 2 = 2$ error degrees of freedom, the error variance estimate is $s^2 = \frac{0.0270}{2} = 0.0135$, and the asymptotic standard errors are:

$$\text{SE}(\hat{\theta}_1) = \sqrt{s^2 \left[(\mathbf{J}^T\mathbf{J})^{-1}\right]_{11}} = \sqrt{0.0135 \times 4.2185} = \sqrt{0.05695} \approx 0.2386$$

$$\text{SE}(\hat{\theta}_2) = \sqrt{s^2 \left[(\mathbf{J}^T\mathbf{J})^{-1}\right]_{22}} = \sqrt{0.0135 \times 0.9065} = \sqrt{0.01224} \approx 0.1106$$

### Question 2: Binary Logistic Regression: Odds Ratios, Predicted Probabilities, Wald Intervals, and Drop-in-Deviance LRT

A cardiovascular epidemiology team fits a binary logistic regression model $\ln\!\left(\frac{\pi_i}{1 - \pi_i}\right) = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2}$ across $n = 250$ patients to predict $5$-year coronary heart disease incidence $Y_i \in \{0, 1\}$ from standardized systolic blood pressure $x_{i1}$ (in SD units) and smoking status $x_{i2} \in \{0 = \text{non-smoker}, 1 = \text{smoker}\}$. Maximum likelihood estimation via Fisher Scoring IRLS yields:

$$\begin{array}{l|cc}
\text{Parameter} & \text{Estimate } \hat{\beta}_j & \text{Standard Error } \text{SE}(\hat{\beta}_j) \\ \hline
\text{Intercept } (\beta_0) & -1.800 & 0.240 \\
\text{Blood Pressure } (\beta_1) & +0.600 & 0.150 \\
\text{Smoker } (\beta_2) & +0.900 & 0.300
\end{array}$$

The maximized log-likelihoods are: Null (intercept-only) model $\ell_0 = -142.50$; Reduced model with $x_1$ only $\ell(x_1) = -131.20$; Full model with $(x_1, x_2)$ $\ell(x_1, x_2) = -126.40$.

1. Compute the point estimates and $95\%$ Wald confidence intervals for the **Odds Ratios** $\text{OR}_1 = e^{\beta_1}$ and $\text{OR}_2 = e^{\beta_2}$, and interpret each in clinical terms.
2. For a smoking patient ($x_2 = 1$) whose systolic blood pressure is $1.5$ SD above the mean ($x_1 = 1.5$), compute the linear predictor $\hat{\eta}_0$, the predicted disease probability $\hat{\pi}_0$, the IRLS working variance weight $\hat{w}_0 = \hat{\pi}_0(1 - \hat{\pi}_0)$, and the marginal probability effect $\frac{\partial \hat{\pi}_0}{\partial x_1}$ of blood pressure at this patient's risk profile.
3. Conduct both the overall **Likelihood Ratio (Drop-in-Deviance) Test** of $H_0: \beta_1 = \beta_2 = 0$ ($\chi_{0.05, 2}^2 = 5.991$) and the partial drop-in-deviance test vs. Wald test for smoking status $H_0: \beta_2 = 0$ ($\chi_{0.05, 1}^2 = 3.841$).

### Solution, step 1: Compute Odds Ratios OR_1, OR_2 and their 95% Wald confidence intervals
Using $\widehat{\text{OR}}_j = \exp(\hat{\beta}_j)$ and the $95\%$ log-odds interval $\hat{\beta}_j \pm 1.96 \, \text{SE}(\hat{\beta}_j)$ exponentiated to the odds-ratio scale:
1. **Blood Pressure ($x_1$, per $1\text{ SD}$ increase)**:
   $$\widehat{\text{OR}}_1 = e^{0.600} \approx 1.8221, \qquad 95\% \text{ CI for } \beta_1: \; 0.600 \pm 1.96(0.150) = 0.600 \pm 0.294 = [0.306, \; 0.894]$$
   $$95\% \text{ CI for } \text{OR}_1: \quad \left[ e^{0.306}, \; e^{0.894} \right] = [1.358, \; 2.445]$$
   Holding smoking status constant, each $1\text{ SD}$ increase in systolic blood pressure increases the odds of coronary heart disease by **$82.2\%$** ($95\%$ CI: $35.8\%$ to $144.5\%$).
2. **Smoking Status ($x_2 = 1$ vs. $x_2 = 0$)**:
   $$\widehat{\text{OR}}_2 = e^{0.900} \approx 2.4596, \qquad 95\% \text{ CI for } \beta_2: \; 0.900 \pm 1.96(0.300) = 0.900 \pm 0.588 = [0.312, \; 1.488]$$
   $$95\% \text{ CI for } \text{OR}_2: \quad \left[ e^{0.312}, \; e^{1.488} \right] = [1.366, \; 4.428]$$
   At any given blood pressure level, smokers have **$2.46$ times the odds** of coronary heart disease compared to non-smokers.

### Solution, step 2: Evaluate linear predictor, probability pi_0, IRLS weight w_0, and marginal effect at (x_1=1.5, x_2=1)
For a patient with $x_{01} = 1.5$ and $x_{02} = 1$, the estimated log-odds linear predictor $\hat{\eta}_0$ is:

$$\hat{\eta}_0 = -1.800 + 0.600(1.5) + 0.900(1) = -1.800 + 0.900 + 0.900 = 0.000$$

Applying the inverse-logit sigmoid function $\hat{\pi}_0 = \frac{1}{1 + e^{-\hat{\eta}_0}}$:

$$\hat{\pi}_0 = \frac{1}{1 + e^{0.000}} = \frac{1}{1 + 1} = 0.5000 \quad (50.0\% \text{ predicted risk})$$

Because $\hat{\pi}_0 = 0.50$ sits right at the inflection point of the logistic curve, this patient achieves the **maximal possible IRLS working weight** and maximal marginal sensitivity:

$$\hat{w}_0 = \hat{\pi}_0(1 - \hat{\pi}_0) = (0.50)(0.50) = 0.2500, \qquad \left. \frac{\partial \hat{\pi}}{\partial x_1} \right|_{\mathbf{x}_0} = \hat{\beta}_1 \hat{\pi}_0 (1 - \hat{\pi}_0) = (0.600)(0.2500) = +0.1500$$

Thus, at this risk profile, a $1\text{ SD}$ increase in blood pressure increases the absolute probability of disease by approximately $15.0$ percentage points.

### Solution, step 3: Conduct overall and partial Drop-in-Deviance Likelihood Ratio Tests vs Wald Test
1. **Overall Model Likelihood Ratio Test ($H_0: \beta_1 = \beta_2 = 0$, $q = 2$ df)**:
   $$G^2 = D_0 - D_F = -2 \left[ \ell_0 - \ell(x_1, x_2) \right] = -2 \left[ -142.50 - (-126.40) \right] = 2(16.10) = 32.20 \gg \chi_{0.05, 2}^2 = 5.991$$
   The model as a whole is highly statistically significant ($p < 10^{-7}$).
2. **Partial Drop-in-Deviance vs. Wald Test for Smoking ($H_0: \beta_2 = 0$, $q = 1$ df)**:
   - **Drop-in-Deviance (LRT)**: $\Delta D = -2 \left[ \ell(x_1) - \ell(x_1, x_2) \right] = -2 \left[ -131.20 - (-126.40) \right] = 2(4.80) = 9.60 > \chi_{0.05, 1}^2 = 3.841$.
   - **Wald Chi-Square**: $W_2 = \left(\frac{\hat{\beta}_2}{\text{SE}(\hat{\beta}_2)}\right)^2 = \left(\frac{0.900}{0.300}\right)^2 = 3.00^2 = 9.00 > 3.841$.
   Both tests confirm that smoking status adds highly significant predictive power beyond blood pressure.

### Question 3: Huber Robust M-Estimation via IRLS & Overdispersed Quasi-Poisson Log-Linear Regression with Offset

This two-part problem examines Iteratively Reweighted Least Squares (IRLS) in both Robust Regression and Generalized Linear Models:

1. **Part A (Huber Robust Regression IRLS)**: In a simple linear regression $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$, an analyst observes $n = 5$ data points at $x_i \in \{-2, -1, 0, 1, 2\}$ with responses $\mathbf{Y} = (1.0, \; 2.0, \; 3.0, \; 4.0, \; 10.0)^T$ (where $Y_5 = 10.0$ is a severe outlier above the clean line $Y = 3 + x$).
   - Compute the ordinary least squares estimates $(\hat{\beta}_{0,\text{OLS}}, \hat{\beta}_{1,\text{OLS}})$.
   - Starting from the initial median/resistant fit $\hat{\beta}_0^{(0)} = 3.0, \; \hat{\beta}_1^{(0)} = 1.0$ with robust scale $\hat{\sigma} = 1.0$ and Huber tuning constant $k = 1.345$, compute the scaled residuals $u_i^{(0)}$, the **Huber IRLS weights** $w_i^{(0)} = \min(1, \, k/|u_i^{(0)}|)$, and perform one **IRLS Weighted Least Squares update** to find $(\hat{\beta}_0^{(1)}, \hat{\beta}_1^{(1)})$. Compare its resistance to the outlier against OLS!
2. **Part B (Overdispersed Quasi-Poisson Regression with Exposure Offset)**: An epidemiologist fits a Poisson log-linear model $\ln(\mu_i) = \ln(t_i) + \beta_0 + \beta_1 x_i$ (where $t_i$ is person-years of exposure and $x_i \in \{0, 1\}$ is occupational hazard exposure) across $n = 50$ industrial plants ($p = 2$). The Poisson MLE gives $\hat{\beta}_0 = -4.605$, $\hat{\beta}_1 = +0.6931$ with naive Poisson standard error $\text{SE}_{\text{Pois}}(\hat{\beta}_1) = 0.120$, and Pearson chi-square statistic $X^2 = \sum_{i=1}^{50} (Y_i - \hat{\mu}_i)^2 / \hat{\mu}_i = 192.0$.
   - Compute the Incidence Rate Ratio $\widehat{\text{IRR}}_1 = e^{\hat{\beta}_1}$, the expected count $\hat{\mu}_0$ for an exposed plant ($x_0 = 1$) with $t_0 = 500$ person-years, the overdispersion estimate $\hat{\phi}$, and the **Quasi-Poisson adjusted standard error** and $95\%$ confidence interval for $\text{IRR}_1$.

### Solution, step 1: Part A1: Compute the OLS fit and evaluate its distortion by the outlier Y_5 = 10
For $x_i \in \{-2, -1, 0, 1, 2\}$, we have $\bar{x} = 0$ and $S_{xx} = 4 + 1 + 0 + 1 + 4 = 10$. With $\mathbf{Y} = (1, 2, 3, 4, 10)^T$:
- $\bar{Y} = \frac{1 + 2 + 3 + 4 + 10}{5} = \frac{20}{5} = 4.00 \implies \hat{\beta}_{0,\text{OLS}} = 4.00$
- $S_{xy} = (-2)(1) + (-1)(2) + (0)(3) + (1)(4) + (2)(10) = -2 - 2 + 0 + 4 + 20 = 20 \implies \hat{\beta}_{1,\text{OLS}} = \frac{20}{10} = 2.00$

Notice how the single contaminated observation $Y_5 = 10.0$ (whose true clean value would be $5.0$) doubled the OLS slope from $\beta_1 = 1.00$ to $\hat{\beta}_{1,\text{OLS}} = 2.00$ and shifted the intercept from $3.00$ to $4.00$!

### Solution, step 2: Part A2: Compute Huber IRLS weights and the one-step robust WLS update
At the initial resistant fit $\hat{Y}_i^{(0)} = 3.0 + 1.0 x_i = (1, 2, 3, 4, 5)^T$ with $\hat{\sigma} = 1.0$ and $k = 1.345$, the initial residuals $e_i^{(0)} = Y_i - \hat{Y}_i^{(0)}$ and standardized residuals $u_i^{(0)} = e_i^{(0)} / 1.0$ are:

$$\mathbf{u}^{(0)} = (0.0, \; 0.0, \; 0.0, \; 0.0, \; 5.0)^T$$

Since $|u_i^{(0)}| = 0 \le 1.345$ for $i = 1, 2, 3, 4$, those four clean points receive full Huber weight $w_1^{(0)} = w_2^{(0)} = w_3^{(0)} = w_4^{(0)} = 1.000$. For the outlier $i = 5$ ($|u_5^{(0)}| = 5.0 > 1.345$), Huber's weight function downweights observation $5$ to:

$$w_5^{(0)} = \frac{k}{|u_5^{(0)}|} = \frac{1.345}{5.0} = 0.2690$$

Now perform Weighted Least Squares with weights $\mathbf{w}^{(0)} = (1, \, 1, \, 1, \, 1, \, 0.269)^T$:
- $\sum w_i = 4.2690$, $\quad \sum w_i x_i = -2 - 1 + 0 + 1 + 0.269(2) = -1.4620 \implies \bar{x}_w = \frac{-1.4620}{4.2690} = -0.34247$
- $\sum w_i Y_i = 1 + 2 + 3 + 4 + 0.269(10) = 12.6900 \implies \bar{Y}_w = \frac{12.6900}{4.2690} = 2.97259$
- $\sum w_i x_i^2 = 4 + 1 + 0 + 1 + 0.269(4) = 7.0760 \implies S_{xx,w} = 7.0760 - 4.2690(-0.34247)^2 = 7.0760 - 0.5007 = 6.5753$
- $\sum w_i x_i Y_i = -2 - 2 + 0 + 4 + 0.269(20) = 5.3800 \implies S_{xy,w} = 5.3800 - 4.2690(-0.34247)(2.97259) = 5.3800 + 4.3459 = 9.7259$

Therefore, the Huber M-estimates are:

$$\hat{\beta}_1^{(1)} = \frac{S_{xy,w}}{S_{xx,w}} = \frac{9.7259}{6.5753} = 1.4792, \qquad \hat{\beta}_0^{(1)} = \bar{Y}_w - \hat{\beta}_1^{(1)} \bar{x}_w = 2.97259 - (1.4792)(-0.34247) = 3.4792$$

(And under Tukey's redescending biweight with $c = 4.685$, since $|u_5^{(0)}| = 5.0 > 4.685$, the outlier receives weight $w_5 = 0$, recovering the exact clean parameters $\hat{\beta}_0 = 3.00, \; \hat{\beta}_1 = 1.00$!).

### Solution, step 3: Part B: Evaluate IRR, expected count with offset, overdispersion phi_hat, and Quasi-Poisson CI
In the Poisson log-linear rate model $\ln(\mu_i) = \ln(t_i) + \beta_0 + \beta_1 x_i$:
1. **Incidence Rate Ratio ($\text{IRR}_1$) and Expected Count at $t_0 = 500, x_0 = 1$**:
   $$\widehat{\text{IRR}}_1 = \exp(\hat{\beta}_1) = \exp(0.6931) = 2.000 \quad (\text{occupational exposure doubles the incident rate})$$
   $$\hat{\mu}_0 = t_0 \exp(\hat{\beta}_0 + \hat{\beta}_1 x_0) = 500 \exp(-4.605 + 0.6931) = 500 (0.01) (2.000) = 10.00 \text{ expected events}$$

2. **Overdispersion Parameter $\hat{\phi}$ and Quasi-Poisson Standard Error**:
   With $n - p = 50 - 2 = 48$ degrees of freedom and $X^2 = 192.0$:
   $$\hat{\phi} = \frac{X^2}{n - p} = \frac{192.0}{48} = 4.00 \implies \sqrt{\hat{\phi}} = 2.00$$
   Because the empirical count variance is $4$ times larger than the Poisson mean, the naive Poisson standard error $\text{SE}_{\text{Pois}}(\hat{\beta}_1) = 0.120$ is understated by a factor of $2$! The **Quasi-Poisson standard error** is:
   $$\text{SE}_{\text{QP}}(\hat{\beta}_1) = \sqrt{\hat{\phi}} \, \text{SE}_{\text{Pois}}(\hat{\beta}_1) = 2.00 \times 0.120 = 0.240$$
   Consequently, the $95\%$ Quasi-Poisson confidence interval for $\text{IRR}_1 = e^{\beta_1}$ is:
   $$\exp\left( 0.6931 \pm 1.96(0.240) \right) = \exp(0.6931 \pm 0.4704) = \left[ e^{0.2227}, \; e^{1.1635} \right] = [1.249, \; 3.201]$$
