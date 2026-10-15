# tooling/generate-unit-7.py
import os

out_path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

unit7_text = r"""# Unit 7: Numerical Optimization in Statistics: Newton–Raphson, Fisher Scoring, Nelder–Mead, and the EM Algorithm

## 7.1 Optimization Landscapes in Statistical Estimation: Convexity, Information Matrices, and Curvature

In parametric statistical theory, estimating unknown model parameters almost invariably reduces to an optimization problem. Whether fitting a Generalized Linear Model (GLM) via Maximum Likelihood Estimation (MLE), training a support vector machine via quadratic programming, minimizing penalized sum-of-squares in regularized regression (Ridge, Lasso), or calibrating deep neural networks, computational algorithms must locate the optimal parameter vector $\boldsymbol{\theta}^* \in \mathbb{R}^p$ that extremizes an objective criterion:

$$\boldsymbol{\theta}^* = \arg\max_{\boldsymbol{\theta} \in \Theta} \ell(\boldsymbol{\theta}) \quad \text{or} \quad \boldsymbol{\theta}^* = \arg\min_{\boldsymbol{\theta} \in \Theta} f(\boldsymbol{\theta})$$

where $\ell(\boldsymbol{\theta}) = \ln L(\boldsymbol{\theta} \mid \mathbf{y})$ represents the log-likelihood function of the observed data.

Unlike general mathematical programming, statistical optimization exhibits unique geometric characteristics governed by **information geometry**, sample sizes, and the Fisher information metric.

### Gradient Vectors and the Score Function

Let $\ell(\boldsymbol{\theta})$ be a twice-continuously differentiable log-likelihood function defined over an open parameter space $\Theta \subseteq \mathbb{R}^p$.

The first-order partial derivatives form the **Gradient Vector**, known in mathematical statistics as the **Score Vector** $\mathbf{S}(\boldsymbol{\theta}) = \mathbf{g}(\boldsymbol{\theta}) \in \mathbb{R}^p$:

$$\mathbf{g}(\boldsymbol{\theta}) = \nabla \ell(\boldsymbol{\theta}) = \begin{bmatrix} \frac{\partial \ell(\boldsymbol{\theta})}{\partial \theta_1} \\ \frac{\partial \ell(\boldsymbol{\theta})}{\partial \theta_2} \\ \vdots \\ \frac{\partial \ell(\boldsymbol{\theta})}{\partial \theta_p} \end{bmatrix}$$

At the Maximum Likelihood Estimate $\hat{\boldsymbol{\theta}}$, Fermat's stationary condition requires the score vector to vanish:

$$\mathbf{g}(\hat{\boldsymbol{\theta}}) = \mathbf{0}$$

### The Hessian Matrix and Observed vs Expected Information

The second-order partial derivatives characterize the local geometric curvature of the objective function. They form the symmetric $p \times p$ **Hessian Matrix** $\mathbf{H}(\boldsymbol{\theta}) \in \mathbb{R}^{p \times p}$:

$$H_{jk}(\boldsymbol{\theta}) = \frac{\partial^2 \ell(\boldsymbol{\theta})}{\partial \theta_j \partial \theta_k}$$

In statistical estimation, we distinguish between two fundamental information matrices:

#### 1. The Observed Information Matrix $\mathcal{J}(\boldsymbol{\theta})$:
The negative of the Hessian matrix evaluated at the parameter point:

$$\mathcal{J}(\boldsymbol{\theta}) = -\mathbf{H}(\boldsymbol{\theta}) = -\nabla^2 \ell(\boldsymbol{\theta})$$

The observed information measures the sample-specific local curvature of the log-likelihood surface around $\boldsymbol{\theta}$. If the observed information is large and positive definite, the log-likelihood surface drops off sharply around the peak, indicating that the sample data constrains the parameter tightly with small standard errors.

#### 2. The Expected (Fisher) Information Matrix $\mathcal{I}(\boldsymbol{\theta})$:
The mathematical expectation of the observed information over the data-generating distribution:

$$\mathcal{I}(\boldsymbol{\theta}) = \mathbb{E}_{\mathbf{Y} \mid \boldsymbol{\theta}} [\mathcal{J}(\boldsymbol{\theta})] = \mathbb{E}_{\mathbf{Y} \mid \boldsymbol{\theta}} \left[ -\nabla^2 \ell(\boldsymbol{\theta}) \right]$$

Under standard Fisher regularity conditions:
1. The support of the distribution $\mathcal{X}$ does not depend on parameter $\boldsymbol{\theta}$.
2. The log-likelihood is twice differentiable with exchangeable integration and differentiation.

The expected information satisfies the fundamental **Information Identity**:

$$\mathcal{I}(\boldsymbol{\theta}) = \text{Var}_{\boldsymbol{\theta}}(\mathbf{g}(\boldsymbol{\theta})) = \mathbb{E}_{\boldsymbol{\theta}} \left[ \mathbf{g}(\boldsymbol{\theta}) \mathbf{g}(\boldsymbol{\theta})^\top \right]$$

Because $\mathcal{I}(\boldsymbol{\theta})$ is the covariance matrix of the score vector, it is **strictly positive semi-definite (PSD) everywhere** across the parameter space:

$$\mathbf{v}^\top \mathcal{I}(\boldsymbol{\theta}) \mathbf{v} \ge 0 \quad \text{for all } \mathbf{v} \in \mathbb{R}^p$$

This guarantee of positive semi-definiteness is a massive computational advantage of Fisher scoring over standard Newton–Raphson.

### Convexity, Condition Numbers, and Ill-Conditioned Valleys

An objective function $f(\boldsymbol{\theta})$ is **strictly convex** on $\Theta$ if for all $\boldsymbol{\theta}_1 \ne \boldsymbol{\theta}_2$ and $\alpha \in (0, 1)$:
$$f(\alpha \boldsymbol{\theta}_1 + (1 - \alpha)\boldsymbol{\theta}_2) < \alpha f(\boldsymbol{\theta}_1) + (1 - \alpha) f(\boldsymbol{\theta}_2)$$
Equivalently, for twice-differentiable functions, convexity is characterized by the Hessian:
$$\nabla^2 f(\boldsymbol{\theta}) \succ 0 \quad \text{(strictly positive definite for all } \boldsymbol{\theta} \in \Theta)$$

For strictly convex optimization problems (such as Ordinary Least Squares, Logistic Regression, Poisson GLMs with canonical links, and Lasso regression), any local minimum is guaranteed to be the unique **global minimum**.

#### The Condition Number of the Hessian:
The difficulty of minimizing a convex quadratic function $f(\boldsymbol{\theta}) \approx \frac{1}{2} \boldsymbol{\theta}^\top \mathbf{A} \boldsymbol{\theta}$ is governed by the **Condition Number** of the Hessian:

$$\kappa(\mathbf{A}) = \frac{\lambda_{max}(\mathbf{A})}{\lambda_{min}(\mathbf{A})}$$

- If $\kappa \approx 1$, the contour level sets are spherical circles. Gradient descent steps point directly toward the global minimum.
- If $\kappa \gg 1$ (e.g. $\kappa = 10^6$, common in collinear statistical models), the level sets form elongated, narrow ellipsoidal ravines. First-order gradient methods oscillate violently from side to side across the steep canyon walls while making glacial progress along the flat valley floor (the "zigzagging" pathology).

---

## 7.2 Gradient-Based Unconstrained Optimization: Gradient Descent, Newton–Raphson, and Quasi-Newton (BFGS)

To locate the optimum of an unconstrained statistical objective function, iterative descent algorithms generate a sequence of parameter vectors $\boldsymbol{\theta}^{(0)}, \boldsymbol{\theta}^{(1)}, \dots, \boldsymbol{\theta}^{(t)}$ that monotonically improve the criterion.

### Gradient Descent and Line Search Strategies

To minimize a cost function $f(\boldsymbol{\theta})$ (or maximize $\ell(\boldsymbol{\theta})$), the **Gradient Descent** algorithm steps in the direction of steepest local descent:

$$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \gamma_t \nabla f(\boldsymbol{\theta}^{(t)})$$

where $\gamma_t > 0$ is the **step size (learning rate)**.

#### Step Size Selection and the Backtracking Armijo Line Search:
Choosing a fixed step size $\gamma$ is perilous: if $\gamma$ is too small, convergence takes millions of iterations; if $\gamma$ is too large, the algorithm overshoots the minimum and diverges to infinity.

To guarantee robust convergence, modern optimization deploys the **Armijo Backtracking Line Search**:
1. Choose baseline parameters: contraction factor $\tau \in (0, 1)$ (typically $\tau = 0.5$) and sufficient decrease factor $c \in (0, 1)$ (typically $c = 10^{-4}$).
2. Start with trial step $\gamma = 1.0$.
3. Check the **Armijo Condition**:
   $$f(\boldsymbol{\theta}^{(t)} - \gamma \nabla f(\boldsymbol{\theta}^{(t)})) \le f(\boldsymbol{\theta}^{(t)}) - c \, \gamma \|\nabla f(\boldsymbol{\theta}^{(t)})\|_2^2$$
4. If the condition is violated, shrink the step: $\gamma \leftarrow \tau \gamma$, and repeat until sufficient decrease is achieved.

Gradient descent with Armijo backtracking exhibits guaranteed convergence to a stationary point, but its asymptotic rate of convergence is strictly **linear**:
$$\|\boldsymbol{\theta}^{(t+1)} - \boldsymbol{\theta}^*\| \le C \left( \frac{\kappa - 1}{\kappa + 1} \right) \|\boldsymbol{\theta}^{(t)} - \boldsymbol{\theta}^*\|$$
When $\kappa$ is large, $\frac{\kappa - 1}{\kappa + 1} \approx 1 - \frac{2}{\kappa}$, making convergence painfully slow.

### The Newton–Raphson Algorithm

To overcome the linear convergence limitation of gradient descent, the **Newton–Raphson Method** incorporates second-order curvature information.

#### Quadratic Taylor Series Approximation:
Approximate the log-likelihood function $\ell(\boldsymbol{\theta})$ around current estimate $\boldsymbol{\theta}^{(t)}$ using a second-order Taylor expansion:

$$\ell(\boldsymbol{\theta}) \approx \ell(\boldsymbol{\theta}^{(t)}) + \mathbf{g}(\boldsymbol{\theta}^{(t)})^\top (\boldsymbol{\theta} - \boldsymbol{\theta}^{(t)}) + \frac{1}{2} (\boldsymbol{\theta} - \boldsymbol{\theta}^{(t)})^\top \mathbf{H}(\boldsymbol{\theta}^{(t)}) (\boldsymbol{\theta} - \boldsymbol{\theta}^{(t)})$$

Differentiating with respect to $\boldsymbol{\theta}$ and setting the gradient to zero:
$$\nabla \ell(\boldsymbol{\theta}) \approx \mathbf{g}(\boldsymbol{\theta}^{(t)}) + \mathbf{H}(\boldsymbol{\theta}^{(t)}) (\boldsymbol{\theta} - \boldsymbol{\theta}^{(t)}) = \mathbf{0}$$

Solving for $\boldsymbol{\theta}$ yields the **Newton–Raphson Update Equation**:

$$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - [\mathbf{H}(\boldsymbol{\theta}^{(t)})]^{-1} \mathbf{g}(\boldsymbol{\theta}^{(t)}) = \boldsymbol{\theta}^{(t)} + [\mathcal{J}(\boldsymbol{\theta}^{(t)})]^{-1} \mathbf{g}(\boldsymbol{\theta}^{(t)})$$

```text
Newton-Raphson Quadratic Leap:
  Objective ^
            |          True Objective Function f(\theta)
            |        .-----------------------------.
            |       /                               \
            |      /   Quadratic Model Q(\theta)     \
            |     /   .-----------------------.       \
            |    /   /                         \       \
        0.0 +---+---+---------------------------+-------+---> \theta
               \theta^{(t)}                  \theta^{(t+1)}
               (Current)                      (Exact Minimum of Q)
```

#### The Quadratic Convergence Property:
If $\boldsymbol{\theta}^{(0)}$ is sufficiently close to $\boldsymbol{\theta}^*$ and the Hessian $\mathbf{H}(\boldsymbol{\theta}^*)$ is non-singular, Newton–Raphson converges with **quadratic convergence speed**:

$$\|\boldsymbol{\theta}^{(t+1)} - \boldsymbol{\theta}^*\| \le C \|\boldsymbol{\theta}^{(t)} - \boldsymbol{\theta}^*\|^2$$

Each iteration approximately **doubles the number of accurate significant digits**! Once inside the basin of attraction, the algorithm terminates in 4 to 6 iterations.

#### Severe Breakdown Modes of Newton–Raphson:
1. **Non-Positive Definite Hessians**: Far from the optimum in non-convex landscapes, $\mathbf{H}(\boldsymbol{\theta}^{(t)})$ may have negative eigenvalues. The Newton step then climbs toward a local maximum or saddle point rather than descending!
2. **Computational Scaling**: Evaluating the exact analytical Hessian requires computing $p(p+1)/2$ second derivatives. Solving the linear system $\mathbf{H} \boldsymbol{\Delta} = -\mathbf{g}$ via Cholesky or LU factorization costs $\mathcal{O}(p^3)$ FLOPs per step. When $p = 10,000$, a single Newton step requires $10^{12}$ operations, becoming computationally impossible.

### Quasi-Newton Methods: BFGS and Limited-Memory L-BFGS

To achieve super-linear convergence without computing or inverting the full $p \times p$ Hessian matrix at each step, Charles Broyden, Roger Fletcher, Donald Goldfarb, and David Shanno (1970) formulated the **BFGS Algorithm**.

Instead of computing $\mathbf{H}^{-1}$ explicitly, BFGS maintains a running symmetric positive-definite approximation of the inverse Hessian matrix $\mathbf{B}_t \approx [\nabla^2 f(\boldsymbol{\theta}^{(t)})]^{-1}$.

#### The BFGS Update Formula:
Let $\mathbf{s}_t = \boldsymbol{\theta}^{(t+1)} - \boldsymbol{\theta}^{(t)}$ denote the parameter displacement, and $\mathbf{y}_t = \mathbf{g}_{t+1} - \mathbf{g}_t$ denote the gradient displacement.
The updated inverse Hessian approximation $\mathbf{B}_{t+1}$ must satisfy the **Secant Equation**:
$$\mathbf{B}_{t+1} \mathbf{y}_t = \mathbf{s}_t$$
BFGS constructs the unique symmetric rank-two update that preserves positive definiteness:

$$\mathbf{B}_{t+1} = (\mathbf{I} - \rho_t \mathbf{s}_t \mathbf{y}_t^\top) \mathbf{B}_t (\mathbf{I} - \rho_t \mathbf{y}_t \mathbf{s}_t^\top) + \rho_t \mathbf{s}_t \mathbf{s}_t^\top$$

where $\rho_t = \frac{1}{\mathbf{y}_t^\top \mathbf{s}_t}$.
- Each step requires only matrix-vector multiplications ($\mathcal{O}(p^2)$ operations instead of $\mathcal{O}(p^3)$).
- **L-BFGS (Limited-Memory BFGS)**: For massive models, storing $\mathbf{B}_t$ ($p \times p$ numbers) is impossible. L-BFGS stores only the last $m$ displacement vectors $\{\mathbf{s}_k, \mathbf{y}_k\}_{k=t-m}^t$ (typically $m \in [5, 20]$), computing the search direction via a two-loop recursion in strictly $\mathcal{O}(m p)$ memory and time.

---

## 7.3 Fisher Scoring and Iteratively Reweighted Least Squares (IRLS) for GLMs

In statistical modeling, Generalized Linear Models (GLMs), developed by John Nelder and Robert Wedderburn in 1972, extend classical linear regression to non-Gaussian exponential dispersion families (Binomial, Poisson, Gamma, Inverse Gaussian).

To fit GLMs, statisticians deploy a specialized second-order algorithm known as **Fisher Scoring**, which translates optimization directly into an iterative weighted least-squares problem: **Iteratively Reweighted Least Squares (IRLS)**.

### Fisher Scoring Algorithm

The **Fisher Scoring Method** replaces the sample-dependent observed information matrix $\mathcal{J}(\boldsymbol{\theta}) = -\mathbf{H}(\boldsymbol{\theta})$ in Newton–Raphson with the **Expected (Fisher) Information Matrix** $\mathcal{I}(\boldsymbol{\theta})$:

$$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + [\mathcal{I}(\boldsymbol{\theta}^{(t)})]^{-1} \mathbf{g}(\boldsymbol{\theta}^{(t)})$$

#### Comparative Theoretical Virtues of Fisher Scoring vs Newton–Raphson:
1. **Guaranteed Descent Direction**: Because $\mathcal{I}(\boldsymbol{\theta})$ is the covariance matrix of the score vector, it is guaranteed to be positive semi-definite everywhere. The search direction $\mathbf{d} = \mathcal{I}^{-1} \mathbf{g}$ satisfies:
   $$\mathbf{g}^\top \mathbf{d} = \mathbf{g}^\top \mathcal{I}^{-1} \mathbf{g} \ge 0$$
   Fisher scoring can **never** climb in the wrong direction or get trapped by negative curvature.
2. **Canonical Link Equivalence**: When a GLM uses its **canonical link function** (e.g. logit for Binomial, log for Poisson), the observed information and expected information are mathematically identical:
   $$\mathcal{J}(\boldsymbol{\theta}) \equiv \mathcal{I}(\boldsymbol{\theta})$$
   Under canonical links, Fisher scoring and Newton–Raphson execute the **exact same arithmetic steps**.

### The Exponential Dispersion Family and GLM Architecture

In a univariate GLM, the response variable $Y_i$ has a distribution belonging to the **Exponential Dispersion Family** with density:

$$f(y_i \mid \theta_i, \phi) = \exp\left( \frac{y_i \theta_i - b(\theta_i)}{a(\phi)} + c(y_i, \phi) \right)$$

where:
- $\theta_i$ is the **natural (canonical) parameter**.
- $b(\theta_i)$ is the **cumulant generator function**.
- $\phi$ is the **dispersion parameter**.

By standard properties of exponential families:
$$\mathbb{E}[Y_i] = \mu_i = b'(\theta_i)$$
$$\text{Var}(Y_i) = b''(\theta_i) a(\phi) = V(\mu_i) a(\phi)$$
where $V(\mu)$ is the **variance function**.

The GLM links the linear predictor $\eta_i = \mathbf{x}_i^\top \boldsymbol{\beta}$ to the mean $\mu_i$ via a monotonic, differentiable **link function** $g(\cdot)$:

$$\eta_i = g(\mu_i) \implies \mu_i = g^{-1}(\eta_i)$$

### Derivation of the IRLS Algorithm

Let us derive the score vector and Fisher information matrix for parameter vector $\boldsymbol{\beta} \in \mathbb{R}^p$.

#### 1. The Score Vector:
Using the chain rule:
$$\frac{\partial \ell_i}{\partial \beta_j} = \frac{\partial \ell_i}{\partial \theta_i} \frac{\partial \theta_i}{\partial \mu_i} \frac{\partial \mu_i}{\partial \eta_i} \frac{\partial \eta_i}{\partial \beta_j}$$
Notice that:
- $\frac{\partial \ell_i}{\partial \theta_i} = \frac{y_i - b'(\theta_i)}{a(\phi)} = \frac{y_i - \mu_i}{a(\phi)}$.
- Since $\mu_i = b'(\theta_i)$, $\frac{\partial \mu_i}{\partial \theta_i} = b''(\theta_i) = V(\mu_i) \implies \frac{\partial \theta_i}{\partial \mu_i} = \frac{1}{V(\mu_i)}$.
- $\frac{\partial \eta_i}{\partial \beta_j} = x_{ij}$.
- Let $g'(\mu_i) = \frac{\partial \eta_i}{\partial \mu_i}$, so $\frac{\partial \mu_i}{\partial \eta_i} = \frac{1}{g'(\mu_i)}$.

Combining terms:
$$\frac{\partial \ell_i}{\partial \beta_j} = \frac{y_i - \mu_i}{a(\phi) V(\mu_i) g'(\mu_i)} x_{ij}$$

Define the **working weights** $W_i$:
$$W_i = \frac{1}{V(\mu_i) [g'(\mu_i)]^2}$$
In matrix notation, let $\mathbf{W} = \text{diag}(W_1, \dots, W_n) \in \mathbb{R}^{n \times n}$.

The overall score vector across all $n$ observations is:

$$\mathbf{g}(\boldsymbol{\beta}) = \frac{1}{a(\phi)} \mathbf{X}^\top \mathbf{W} \mathbf{D} (\mathbf{y} - \boldsymbol{\mu})$$

where $\mathbf{D} = \text{diag}(g'(\mu_1), \dots, g'(\mu_n))$.

#### 2. The Fisher Information Matrix:
The Expected Information Matrix is:

$$\mathcal{I}(\boldsymbol{\beta}) = \mathbb{E}\left[ \mathbf{g}(\boldsymbol{\beta}) \mathbf{g}(\boldsymbol{\beta})^\top \right] = \frac{1}{a(\phi)} \mathbf{X}^\top \mathbf{W} \mathbf{X}$$

#### 3. The Fisher Scoring Step as Weighted Least Squares:
Substitute $\mathbf{g}$ and $\mathcal{I}$ into the Fisher scoring equation:
$$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + [\mathcal{I}(\boldsymbol{\beta}^{(t)})]^{-1} \mathbf{g}(\boldsymbol{\beta}^{(t)})$$
$$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t \mathbf{D}_t (\mathbf{y} - \boldsymbol{\mu}_t)$$
Factor out $(\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t$:
$$\boldsymbol{\beta}^{(t+1)} = (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t \left[ \mathbf{X} \boldsymbol{\beta}^{(t)} + \mathbf{D}_t (\mathbf{y} - \boldsymbol{\mu}_t) \right]$$

Define the **adjusted working response vector** $\mathbf{z}_t \in \mathbb{R}^n$:

$$z_{i, t} = \eta_{i, t} + (y_i - \mu_{i, t}) g'(\mu_{i, t})$$

The update equation simplifies to:

$$\boldsymbol{\beta}^{(t+1)} = (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t \mathbf{z}_t$$

This is the exact mathematical solution to a **Weighted Least Squares (WLS)** regression of the working response $\mathbf{z}_t$ on the design matrix $\mathbf{X}$ with diagonal weight matrix $\mathbf{W}_t$!

#### The IRLS Loop:
1. Initialize $\boldsymbol{\beta}^{(0)}$ (or initialize $\mu_i^{(0)} = y_i + \delta$).
2. Compute linear predictors $\eta_{i, t} = \mathbf{x}_i^\top \boldsymbol{\beta}^{(t)}$ and fitted means $\mu_{i, t} = g^{-1}(\eta_{i, t})$.
3. Compute working weights $W_{i, t} = \frac{1}{V(\mu_{i, t}) [g'(\mu_{i, t})]^2}$ and working responses $z_{i, t} = \eta_{i, t} + (y_i - \mu_{i, t}) g'(\mu_{i, t})$.
4. Solve the weighted least squares problem $\boldsymbol{\beta}^{(t+1)} = (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t \mathbf{z}_t$ via Householder QR.
5. Repeat until $\|\boldsymbol{\beta}^{(t+1)} - \boldsymbol{\beta}^{(t)}\|_\infty < \epsilon$.

This celebrated derivation explains why `glm()` in R and `statsmodels.api.GLM` in Python execute so efficiently: every iteration leverages highly optimized compiled QR routines for weighted regression.

---

## 7.4 Derivative-Free Optimization: The Nelder–Mead Simplex Algorithm

In many complex statistical settings, computing analytical gradients $\mathbf{g}(\boldsymbol{\theta})$ or Hessians $\mathbf{H}(\boldsymbol{\theta})$ is impossible. For example, the likelihood function may be evaluated via stochastic Monte Carlo simulation (Simulated Method of Moments), black-box physics codes, or non-smooth step functions.

In 1965, John Nelder and Roger Mead developed the **Nelder–Mead Simplex Algorithm** (the default optimization method of `optim(method = "Nelder-Mead")` in R and `scipy.optimize.minimize(method = "Nelder-Mead")` in Python).

Nelder–Mead is a **derivative-free heuristic** that adapts a geometric simplex to the local contours of the objective surface.

### Anatomy of a Simplex

In a $p$-dimensional parameter space $\mathbb{R}^p$, a **simplex** is a geometric polytope formed by $p + 1$ distinct vertex vectors:

$$\mathcal{S} = \{ \mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_{p+1} \}$$

- In $p = 1$ dimension, a simplex is a line segment (2 vertices).
- In $p = 2$ dimensions, a simplex is a triangle (3 vertices).
- In $p = 3$ dimensions, a simplex is a tetrahedron (4 vertices).

At each iteration, the objective function $f(\mathbf{x})$ is evaluated at all $p + 1$ vertices, and the vertices are sorted in ascending order of function values:

$$f(\mathbf{x}_1) \le f(\mathbf{x}_2) \le \dots \le f(\mathbf{x}_p) \le f(\mathbf{x}_{p+1})$$

We define:
- $\mathbf{x}_1$: The **best vertex** ($\mathbf{x}_l$, lowest cost).
- $\mathbf{x}_p$: The **second-worst vertex** ($\mathbf{x}_s$).
- $\mathbf{x}_{p+1}$: The **worst vertex** ($\mathbf{x}_h$, highest cost).
- $\bar{\mathbf{x}}$: The **centroid** of all vertices *excluding* the worst vertex:
  $$\bar{\mathbf{x}} = \frac{1}{p} \sum_{i=1}^p \mathbf{x}_i$$

### The Four Fundamental Geometric Transformations

The algorithm attempts to replace the worst vertex $\mathbf{x}_{p+1}$ with a superior point using four geometric transformations governed by standard tuning parameters $(\alpha, \gamma, \rho, \sigma) = (1.0, 2.0, 0.5, 0.5)$:

```text
Nelder-Mead Geometric Transformations:
              x_e (Expansion: gamma=2.0)
               ^
               |
              x_r (Reflection: alpha=1.0)
               ^
               |
         [Centroid \bar{x}]
          /        \
        x_1         x_2
         \         /
          x_{p+1} (Worst Vertex)
```

1. **Reflection ($\alpha = 1.0$)**:
   Reflect the worst vertex through the centroid:
   $$\mathbf{x}_r = \bar{\mathbf{x}} + \alpha (\bar{\mathbf{x}} - \mathbf{x}_{p+1})$$
   Evaluate $f_r = f(\mathbf{x}_r)$.
   - If $f(\mathbf{x}_1) \le f_r < f(\mathbf{x}_p)$: The reflected point is better than the second-worst, but not strictly the best. Replace $\mathbf{x}_{p+1} \leftarrow \mathbf{x}_r$, and terminate the iteration.

2. **Expansion ($\gamma = 2.0$)**:
   If the reflected point is strictly better than the current best ($f_r < f(\mathbf{x}_1)$), the search direction is highly promising. Expand further along the ray:
   $$\mathbf{x}_e = \bar{\mathbf{x}} + \gamma (\mathbf{x}_r - \bar{\mathbf{x}})$$
   Evaluate $f_e = f(\mathbf{x}_e)$.
   - If $f_e < f_r$: Replace $\mathbf{x}_{p+1} \leftarrow \mathbf{x}_e$.
   - Otherwise: Replace $\mathbf{x}_{p+1} \leftarrow \mathbf{x}_r$.

3. **Contraction ($\rho = 0.5$)**:
   If the reflected point is worse than the second-worst ($f_r \ge f(\mathbf{x}_p)$), the simplex has overshot the valley. Perform a contraction:
   - **Outside Contraction ($f(\mathbf{x}_p) \le f_r < f(\mathbf{x}_{p+1})$)**:
     $$\mathbf{x}_{oc} = \bar{\mathbf{x}} + \rho (\mathbf{x}_r - \bar{\mathbf{x}})$$
     If $f(\mathbf{x}_{oc}) \le f_r$, accept $\mathbf{x}_{p+1} \leftarrow \mathbf{x}_{oc}$.
   - **Inside Contraction ($f_r \ge f(\mathbf{x}_{p+1})$)**:
     $$\mathbf{x}_{ic} = \bar{\mathbf{x}} - \rho (\bar{\mathbf{x}} - \mathbf{x}_{p+1})$$
     If $f(\mathbf{x}_{ic}) < f(\mathbf{x}_{p+1})$, accept $\mathbf{x}_{p+1} \leftarrow \mathbf{x}_{ic}$.

4. **Shrink ($\sigma = 0.5$)**:
   If contraction fails to produce a point better than the worst vertex, the simplex shrinks all vertices toward the best point $\mathbf{x}_1$:
   $$\mathbf{x}_i \leftarrow \mathbf{x}_1 + \sigma (\mathbf{x}_i - \mathbf{x}_1) \quad \text{for all } i = 2, \dots, p+1$$
   Shrinking requires evaluating the objective function at $p$ new points.

#### Convergence Properties:
Nelder–Mead is robust and requires zero derivatives. However, it is a heuristic: in dimensions $p > 20$, the simplex frequently collapses into a degenerate lower-dimensional subspace or stalls at non-stationary points.

---

## 7.5 The Expectation–Maximization (EM) Algorithm: Latent Variables, Jensen's Inequality, and Monotonic Convergence

In many statistical models, maximum likelihood estimation is complicated by the presence of **latent (unobserved) variables** or **missing data**. Canonical examples include:
- Gaussian Mixture Models (where cluster memberships are unobserved).
- Censored survival times.
- Hidden Markov Models (HMMs).
- Factor analysis.

In 1977, Arthur Dempster, Nan Laird, and Donald Rubin published their seminal paper formulating the **Expectation–Maximization (EM) Algorithm**. The EM algorithm transforms an intractable incomplete-data optimization problem into a sequence of simple complete-data optimizations with guaranteed monotonic likelihood convergence.

### Mathematical Framework: Incomplete vs Complete Data

Let:
- $\mathbf{Y}$: The **observed data vector**.
- $\mathbf{Z}$: The **unobserved latent data (or missing data)**.
- $\mathbf{X} = (\mathbf{Y}, \mathbf{Z})$: The hypothetical **complete data**.

The goal is to compute the Maximum Likelihood Estimate of parameter $\boldsymbol{\theta}$ based on the **observed data log-likelihood**:

$$\ell(\boldsymbol{\theta} \mid \mathbf{Y}) = \ln p(\mathbf{Y} \mid \boldsymbol{\theta}) = \ln \int p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}) \, d\mathbf{Z}$$

Because the integral (or sum) appears **inside the logarithm**, the observed log-likelihood $\ln \int \dots$ does not decouple into simple additive terms, making direct differentiation intractable.

Conversely, the **complete-data log-likelihood**:

$$\ell_c(\boldsymbol{\theta} \mid \mathbf{Y}, \mathbf{Z}) = \ln p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta})$$

belongs to a simple exponential family that would be trivial to maximize if $\mathbf{Z}$ were known.

### The EM Master Function: The Q-Function

Because $\mathbf{Z}$ is unknown, we cannot maximize $\ell_c(\boldsymbol{\theta} \mid \mathbf{Y}, \mathbf{Z})$ directly.
Instead, the EM algorithm takes the conditional expectation of the complete log-likelihood with respect to the latent variables $\mathbf{Z}$, conditioned on the observed data $\mathbf{Y}$ and current parameter estimate $\boldsymbol{\theta}^{(t)}$.

The central mathematical object of the EM algorithm is the **$Q$-Function**:

$$Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)}) = \mathbb{E}_{\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}} \left[ \ln p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}) \right] = \int \left[ \ln p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta}) \right] p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}) \, d\mathbf{z}$$

```text
The EM Iteration Cycle:
     Current Parameter \theta^{(t)}
                 |
                 v
        [ Expectation (E-step) ]
                 |
                 v Compute Q(\theta | \theta^{(t)})
        [ Maximization (M-step) ]
                 |
                 v \theta^{(t+1)} = argmax Q(\theta | \theta^{(t)})
     Updated Parameter \theta^{(t+1)}  (Guaranteed: \ell(\theta^{(t+1)}) >= \ell(\theta^{(t)}))
```

#### The Two-Step Algorithmic Cycle:
1. **The Expectation Step (E-step)**:
   Calculate the conditional distribution of the latent variables given the current parameter estimate:
   $$p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}) = \frac{p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}^{(t)})}{\int p(\mathbf{Y}, \mathbf{z}' \mid \boldsymbol{\theta}^{(t)}) d\mathbf{z}'}$$
   and formulate the expected complete-data log-likelihood $Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)})$.

2. **The Maximization Step (M-step)**:
   Update the parameter estimate by globally maximizing the $Q$-function:
   $$\boldsymbol{\theta}^{(t+1)} = \arg\max_{\boldsymbol{\theta} \in \Theta} Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)})$$

### Proof of Monotonic Likelihood Ascent via Jensen's Inequality

The defining theoretical property of the EM algorithm is that **the observed log-likelihood increases monotonically at every single iteration**:

$$\ell(\boldsymbol{\theta}^{(t+1)} \mid \mathbf{Y}) \ge \ell(\boldsymbol{\theta}^{(t)} \mid \mathbf{Y})$$

#### Rigorous Mathematical Proof:
Express the complete joint density as the product of the marginal and conditional densities:
$$p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}) = p(\mathbf{Y} \mid \boldsymbol{\theta}) p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta})$$

Taking the natural logarithm of both sides:
$$\ln p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}) = \ln p(\mathbf{Y} \mid \boldsymbol{\theta}) + \ln p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta})$$
Rearranging for the observed log-likelihood $\ell(\boldsymbol{\theta}) = \ln p(\mathbf{Y} \mid \boldsymbol{\theta})$:
$$\ell(\boldsymbol{\theta}) = \ln p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}) - \ln p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta})$$

Take the conditional expectation of both sides with respect to $p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})$:
$$\mathbb{E}_{\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}} [\ell(\boldsymbol{\theta})] = \mathbb{E}_{\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}} \left[ \ln p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta}) \right] - \mathbb{E}_{\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}} \left[ \ln p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}) \right]$$

Because $\ell(\boldsymbol{\theta})$ does not depend on $\mathbf{Z}$, its expectation is simply $\ell(\boldsymbol{\theta})$:
$$\ell(\boldsymbol{\theta}) = Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)}) - H(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)})$$
where:
$$H(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)}) = \mathbb{E}_{\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}} \left[ \ln p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}) \right] = \int [\ln p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta})] p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}) \, d\mathbf{z}$$

Now evaluate the change in log-likelihood from step $t$ to step $t+1$:
$$\ell(\boldsymbol{\theta}^{(t+1)}) - \ell(\boldsymbol{\theta}^{(t)}) = \left[ Q(\boldsymbol{\theta}^{(t+1)} \mid \boldsymbol{\theta}^{(t)}) - Q(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^{(t)}) \right] - \left[ H(\boldsymbol{\theta}^{(t+1)} \mid \boldsymbol{\theta}^{(t)}) - H(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^{(t)}) \right]$$

We evaluate the two bracketed terms separately:
1. **First Term ($Q$-Difference)**:
   By definition of the M-step, $\boldsymbol{\theta}^{(t+1)}$ maximizes $Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)})$. Therefore:
   $$Q(\boldsymbol{\theta}^{(t+1)} \mid \boldsymbol{\theta}^{(t)}) \ge Q(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^{(t)}) \implies \Delta Q \ge 0$$

2. **Second Term ($H$-Difference and Jensen's Inequality)**:
   Consider the difference:
   $$H(\boldsymbol{\theta}^{(t+1)} \mid \boldsymbol{\theta}^{(t)}) - H(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^{(t)}) = \int \ln \left( \frac{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t+1)})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})} \right) p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}) \, d\mathbf{z}$$
   Recall that the natural logarithm is a strictly concave function ($\ln''(x) = -1/x^2 < 0$).
   By **Jensen's Inequality**, for any concave function $\phi$, $\mathbb{E}[\phi(X)] \le \phi(\mathbb{E}[X])$.
   Therefore:
   $$\int \ln \left( \frac{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t+1)})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})} \right) p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}) \, d\mathbf{z} \le \ln \left( \int \frac{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t+1)})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})} p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}) \, d\mathbf{z} \right)$$
   The terms $p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})$ cancel in the integral:
   $$= \ln \left( \int p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t+1)}) \, d\mathbf{z} \right) = \ln(1) = 0$$

Thus:
$$H(\boldsymbol{\theta}^{(t+1)} \mid \boldsymbol{\theta}^{(t)}) - H(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^{(t)}) \le 0$$
$$- \left[ H(\boldsymbol{\theta}^{(t+1)} \mid \boldsymbol{\theta}^{(t)}) - H(\boldsymbol{\theta}^{(t)} \mid \boldsymbol{\theta}^{(t)}) \right] \ge 0$$

Combining both inequalities:

$$\ell(\boldsymbol{\theta}^{(t+1)}) - \ell(\boldsymbol{\theta}^{(t)}) \ge 0 \implies \ell(\boldsymbol{\theta}^{(t+1)}) \ge \ell(\boldsymbol{\theta}^{(t)})$$

This completes the mathematical proof that **the observed log-likelihood increases monotonically at every single EM step**.

---

## Fully worked question 1: Detailed Step-by-Step Derivation of IRLS for Logistic Regression and Equivalence to Fisher Scoring

### Question
In epidemiological research, an investigator fits a binary logistic regression model predicting myocardial infarction:

$$Y_i \sim \text{Bernoulli}(p_i), \quad i = 1, \dots, n$$

where the success probability $p_i = \mathbb{P}(Y_i = 1 \mid \mathbf{x}_i)$ is linked to a linear predictor $\eta_i = \mathbf{x}_i^\top \boldsymbol{\beta}$ via the canonical logit link:

$$\text{logit}(p_i) = \ln\left( \frac{p_i}{1 - p_i} \right) = \mathbf{x}_i^\top \boldsymbol{\beta} \implies p_i = \frac{1}{1 + e^{-\mathbf{x}_i^\top \boldsymbol{\beta}}}$$

1. Formulate the total log-likelihood function $\ell(\boldsymbol{\beta})$ of the sample.
2. Derive the exact gradient vector (score vector) $\mathbf{g}(\boldsymbol{\beta}) = \nabla \ell(\boldsymbol{\beta})$ and the observed Hessian matrix $\mathbf{H}(\boldsymbol{\beta}) = \nabla^2 \ell(\boldsymbol{\beta})$.
3. Derive the Expected (Fisher) Information Matrix $\mathcal{I}(\boldsymbol{\beta}) = \mathbb{E}[-\mathbf{H}(\boldsymbol{\beta})]$ and prove that $\mathbf{H}(\boldsymbol{\beta})$ is strictly non-stochastic, establishing exact mathematical equivalence between Newton–Raphson and Fisher Scoring.
4. Formulate the Iteratively Reweighted Least Squares (IRLS) representation, defining the working diagonal weight matrix $\mathbf{W}$ and adjusted working response vector $\mathbf{z}$.
5. Given a toy dataset of $n = 3$ subjects with single predictor $x$:
   $$\mathbf{y} = [1, \, 0, \, 1]^\top, \quad \mathbf{x} = [0.5, \, -1.0, \, 1.5]^\top, \quad (\text{no intercept model: } \eta_i = \beta x_i)$$
   Starting from initial guess $\beta^{(0)} = 0.0$, compute the first iteration values:
   - Predicted probabilities $p_i^{(0)}$
   - Working weights $W_i^{(0)}$
   - Working responses $z_i^{(0)}$
   - Updated parameter estimate $\beta^{(1)}$ to four decimal places.

---

### Solution, step 1: Formulate the logistic regression log-likelihood

**Solution, step 1: Formulate the logistic regression log-likelihood.**

For a binary Bernoulli observation $y_i \in \{0, 1\}$:
$$\mathbb{P}(Y_i = y_i) = p_i^{y_i} (1 - p_i)^{1 - y_i}$$

The log-likelihood for observation $i$ is:
$$\ell_i(\boldsymbol{\beta}) = y_i \ln p_i + (1 - y_i) \ln(1 - p_i) = y_i \ln\left( \frac{p_i}{1 - p_i} \right) + \ln(1 - p_i)$$
Substitute the logit link $\ln(p_i / (1 - p_i)) = \mathbf{x}_i^\top \boldsymbol{\beta}$ and $1 - p_i = \frac{1}{1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}}}$:
$$\ell_i(\boldsymbol{\beta}) = y_i (\mathbf{x}_i^\top \boldsymbol{\beta}) - \ln(1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}})$$

Summing across all $n$ independent observations:

$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ y_i (\mathbf{x}_i^\top \boldsymbol{\beta}) - \ln(1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}}) \right]$$

---

### Solution, step 2: Derive score vector and observed Hessian matrix

**Solution, step 2: Derive score vector and observed Hessian matrix.**

1. **Gradient (Score Vector)**:
   Differentiate $\ell(\boldsymbol{\beta})$ with respect to $\beta_j$:
   $$\frac{\partial \ell}{\partial \beta_j} = \sum_{i=1}^n \left[ y_i x_{ij} - \frac{e^{\mathbf{x}_i^\top \boldsymbol{\beta}}}{1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}}} x_{ij} \right]$$
   Since $p_i = \frac{e^{\mathbf{x}_i^\top \boldsymbol{\beta}}}{1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}}}$:
   $$\frac{\partial \ell}{\partial \beta_j} = \sum_{i=1}^n (y_i - p_i) x_{ij}$$

   In compact matrix notation:
   $$\mathbf{g}(\boldsymbol{\beta}) = \nabla \ell(\boldsymbol{\beta}) = \mathbf{X}^\top (\mathbf{y} - \mathbf{p})$$
   where $\mathbf{p} = (p_1, \dots, p_n)^\top$.

2. **Hessian Matrix**:
   Differentiate $\frac{\partial \ell}{\partial \beta_j}$ with respect to $\beta_k$:
   $$H_{jk}(\boldsymbol{\beta}) = \frac{\partial^2 \ell}{\partial \beta_j \partial \beta_k} = \sum_{i=1}^n \left( -\frac{\partial p_i}{\partial \beta_k} \right) x_{ij}$$
   Using the quotient rule on $p_i = \frac{1}{1 + e^{-\mathbf{x}_i^\top \boldsymbol{\beta}}}$:
   $$\frac{\partial p_i}{\partial \beta_k} = p_i (1 - p_i) x_{ik}$$
   Therefore:
   $$H_{jk}(\boldsymbol{\beta}) = -\sum_{i=1}^n p_i (1 - p_i) x_{ij} x_{ik}$$

   In matrix notation, let $\mathbf{W} \in \mathbb{R}^{n \times n}$ be the diagonal matrix of binomial variances:
   $$\mathbf{W} = \text{diag}(p_1 (1 - p_1), \, p_2 (1 - p_2), \, \dots, \, p_n (1 - p_n))$$
   The Hessian matrix is:
   $$\mathbf{H}(\boldsymbol{\beta}) = -\mathbf{X}^\top \mathbf{W} \mathbf{X}$$

---

### Solution, step 3: Expected information and equivalence of Newton–Raphson and Fisher Scoring

**Solution, step 3: Expected information and equivalence of Newton–Raphson and Fisher Scoring.**

Notice that the Hessian matrix:
$$\mathbf{H}(\boldsymbol{\beta}) = -\mathbf{X}^\top \mathbf{W}(\boldsymbol{\beta}) \mathbf{X}$$
depends on the parameters $\boldsymbol{\beta}$ and explanatory variables $\mathbf{X}$, but does **not depend on the random observations $\mathbf{y}$**!

Therefore, taking the expectation over $\mathbf{y}$:
$$\mathcal{I}(\boldsymbol{\beta}) = \mathbb{E}[-\mathbf{H}(\boldsymbol{\beta})] = -\mathbf{H}(\boldsymbol{\beta}) = \mathbf{X}^\top \mathbf{W} \mathbf{X}$$

Because $\mathcal{J}(\boldsymbol{\beta}) \equiv \mathcal{I}(\boldsymbol{\beta})$, the Newton–Raphson algorithm and the Fisher Scoring algorithm are **mathematically and numerically identical**:

$$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top (\mathbf{y} - \mathbf{p}_t)$$

---

### Solution, step 4: IRLS formulation

**Solution, step 4: IRLS formulation.**

Rewrite the update step by factoring out $(\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t$:

$$\boldsymbol{\beta}^{(t+1)} = (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t \left[ \mathbf{X} \boldsymbol{\beta}^{(t)} + \mathbf{W}_t^{-1} (\mathbf{y} - \mathbf{p}_t) \right]$$

Define the working response vector $\mathbf{z}_t$:

$$\mathbf{z}_t = \mathbf{X} \boldsymbol{\beta}^{(t)} + \mathbf{W}_t^{-1} (\mathbf{y} - \mathbf{p}_t)$$

In scalar components, for observation $i$:
$$z_{i, t} = \eta_{i, t} + \frac{y_i - p_{i, t}}{p_{i, t}(1 - p_{i, t})}$$
$$W_{i, t} = p_{i, t}(1 - p_{i, t})$$

The update is computed as a standard Weighted Least Squares regression:

$$\boldsymbol{\beta}^{(t+1)} = (\mathbf{X}^\top \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}_t \mathbf{z}_t$$

---

### Solution, step 5: Numerical iteration 1 computation

**Solution, step 5: Numerical iteration 1 computation.**

We are given:
- $\mathbf{y} = [1, \, 0, \, 1]^\top$
- $\mathbf{x} = [0.5, \, -1.0, \, 1.5]^\top$
- Initial parameter: $\beta^{(0)} = 0.0$.

1. **Linear Predictors and Probabilities at Step 0**:
   $$\eta_i^{(0)} = \beta^{(0)} x_i = 0.0 \times x_i = 0.0 \quad \text{for all } i$$
   $$p_i^{(0)} = \frac{1}{1 + e^{-0}} = \frac{1}{1 + 1} = 0.50 \quad \text{for all } i$$
   $$\mathbf{p}^{(0)} = [0.50, \, 0.50, \, 0.50]^\top$$

2. **Working Weights $W_i^{(0)}$**:
   $$W_i^{(0)} = p_i^{(0)} (1 - p_i^{(0)}) = 0.50 \times 0.50 = 0.25 \quad \text{for all } i$$
   $$\mathbf{W}_0 = \text{diag}(0.25, \, 0.25, \, 0.25)$$

3. **Working Responses $z_i^{(0)}$**:
   Using $z_i^{(0)} = \eta_i^{(0)} + \frac{y_i - p_i^{(0)}}{W_i^{(0)}} = 0.0 + \frac{y_i - 0.50}{0.25} = 4(y_i - 0.50)$:
   - For $i = 1$ ($y_1 = 1$): $z_1^{(0)} = 4(1 - 0.5) = 4(0.5) = \mathbf{2.0}$
   - For $i = 2$ ($y_2 = 0$): $z_2^{(0)} = 4(0 - 0.5) = 4(-0.5) = \mathbf{-2.0}$
   - For $i = 3$ ($y_3 = 1$): $z_3^{(0)} = 4(1 - 0.5) = 4(0.5) = \mathbf{2.0}$
   $$\mathbf{z}_0 = [2.0, \, -2.0, \, 2.0]^\top$$

4. **Updated Parameter Estimate $\beta^{(1)}$**:
   In our 1-parameter model:
   $$\mathbf{X}^\top \mathbf{W}_0 \mathbf{X} = \sum_{i=1}^3 x_i^2 W_i^{(0)} = 0.25 \sum_{i=1}^3 x_i^2$$
   $$\sum_{i=1}^3 x_i^2 = (0.5)^2 + (-1.0)^2 + (1.5)^2 = 0.25 + 1.00 + 2.25 = 3.50$$
   $$\mathbf{X}^\top \mathbf{W}_0 \mathbf{X} = 0.25 \times 3.50 = 0.875$$

   Now evaluate $\mathbf{X}^\top \mathbf{W}_0 \mathbf{z}_0$:
   $$\mathbf{X}^\top \mathbf{W}_0 \mathbf{z}_0 = \sum_{i=1}^3 x_i W_i^{(0)} z_i^{(0)} = 0.25 \sum_{i=1}^3 x_i z_i^{(0)}$$
   $$\sum_{i=1}^3 x_i z_i^{(0)} = (0.5)(2.0) + (-1.0)(-2.0) + (1.5)(2.0) = 1.0 + 2.0 + 3.0 = 6.0$$
   $$\mathbf{X}^\top \mathbf{W}_0 \mathbf{z}_0 = 0.25 \times 6.0 = 1.50$$

   Therefore:
   $$\beta^{(1)} = \frac{\mathbf{X}^\top \mathbf{W}_0 \mathbf{z}_0}{\mathbf{X}^\top \mathbf{W}_0 \mathbf{X}} = \frac{1.50}{0.875} = \frac{6}{3.5} = \frac{12}{7} \approx \mathbf{1.7143}$$

In a single IRLS step, the parameter estimate updates from $0.0$ to $\beta^{(1)} \approx 1.7143$.

---

## Fully worked question 2: Mathematical Proof of Monotonic Likelihood Increase in the EM Algorithm via Jensen's Inequality

### Question
The Expectation–Maximization (EM) algorithm is deployed to estimate parameter vector $\boldsymbol{\theta}$ in a latent variable model with observed data $\mathbf{Y}$ and unobserved latent variables $\mathbf{Z}$.

Let $p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta})$ be the complete-data joint probability density function.
The observed data log-likelihood is:
$$\ell(\boldsymbol{\theta}) = \ln p(\mathbf{Y} \mid \boldsymbol{\theta})$$

The EM algorithm constructs the $Q$-function:
$$Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)}) = \mathbb{E}_{\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}} [\ln p(\mathbf{Y}, \mathbf{Z} \mid \boldsymbol{\theta})]$$
and updates the parameter via:
$$\boldsymbol{\theta}^{(t+1)} = \arg\max_{\boldsymbol{\theta}} Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)})$$

1. Define the Kullback–Leibler (KL) divergence between two probability distributions $q(\mathbf{z})$ and $p(\mathbf{z})$:
   $$\mathcal{D}_{KL}(q \,\|\, p) = \int q(\mathbf{z}) \ln\left( \frac{q(\mathbf{z})}{p(\mathbf{z})} \right) d\mathbf{z}$$
   Using Jensen's inequality for convex functions, prove Gibbs' Inequality: $\mathcal{D}_{KL}(q \,\|\, p) \ge 0$, with equality if and only if $q(\mathbf{z}) = p(\mathbf{z})$ almost everywhere.
2. For any arbitrary probability distribution $q(\mathbf{z})$ over the latent space, prove that the observed log-likelihood admits the exact variational decomposition:
   $$\ell(\boldsymbol{\theta}) = \mathcal{L}(q, \boldsymbol{\theta}) + \mathcal{D}_{KL}(q(\mathbf{Z}) \,\|\, p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}))$$
   where $\mathcal{L}(q, \boldsymbol{\theta}) = \int q(\mathbf{z}) \ln\left( \frac{p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta})}{q(\mathbf{z})} \right) d\mathbf{z}$ is the Evidence Lower Bound (ELBO).
3. Using the ELBO decomposition, demonstrate what occurs during the **E-step** when $q(\mathbf{z})$ is set to $p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})$.
4. Prove that $\ell(\boldsymbol{\theta}^{(t+1)}) \ge \ell(\boldsymbol{\theta}^{(t)})$, establishing monotonic non-decreasing convergence.

---

### Solution, step 1: Proof of Gibbs' Inequality via Jensen's Inequality

**Solution, step 1: Proof of Gibbs' Inequality via Jensen's Inequality.**

The Kullback–Leibler divergence is:
$$\mathcal{D}_{KL}(q \,\|\, p) = \int q(\mathbf{z}) \ln\left( \frac{q(\mathbf{z})}{p(\mathbf{z})} \right) d\mathbf{z} = -\int q(\mathbf{z}) \ln\left( \frac{p(\mathbf{z})}{q(\mathbf{z})} \right) d\mathbf{z} = -\mathbb{E}_q \left[ \ln\left( \frac{p(\mathbf{Z})}{q(\mathbf{Z})} \right) \right]$$

Recall that the negative logarithm $-\ln(t)$ is a strictly convex function on $(0, \infty)$ (since its second derivative $\frac{d^2}{dt^2}(-\ln t) = \frac{1}{t^2} > 0$).

By **Jensen's Inequality**, for any strictly convex function $\phi$ and random variable $X$:
$$\mathbb{E}[\phi(X)] \ge \phi(\mathbb{E}[X])$$

Applying this with $\phi(t) = -\ln(t)$ and $X = \frac{p(\mathbf{Z})}{q(\mathbf{Z})}$:
$$-\mathbb{E}_q \left[ \ln\left( \frac{p(\mathbf{Z})}{q(\mathbf{Z})} \right) \right] \ge -\ln\left( \mathbb{E}_q \left[ \frac{p(\mathbf{Z})}{q(\mathbf{Z})} \right] \right)$$

Evaluate the inner expectation:
$$\mathbb{E}_q \left[ \frac{p(\mathbf{Z})}{q(\mathbf{Z})} \right] = \int q(\mathbf{z}) \frac{p(\mathbf{z})}{q(\mathbf{z})} \, d\mathbf{z} = \int p(\mathbf{z}) \, d\mathbf{z} = 1$$

Substitute this back:
$$\mathcal{D}_{KL}(q \,\|\, p) \ge -\ln(1) = 0$$

Furthermore, because $-\ln(t)$ is strictly convex, equality holds if and only if $X = \frac{p(\mathbf{Z})}{q(\mathbf{Z})}$ is constant with probability 1. Since both $p$ and $q$ integrate to 1, this constant must be 1, meaning $q(\mathbf{z}) = p(\mathbf{z})$ almost everywhere.

This proves **Gibbs' Inequality**:

$$\mathcal{D}_{KL}(q \,\|\, p) \ge 0$$

---

### Solution, step 2: Variational decomposition of the log-likelihood (ELBO)

**Solution, step 2: Variational decomposition of the log-likelihood (ELBO).**

Let $q(\mathbf{z})$ be an arbitrary probability density function on the latent space $\mathcal{Z}$ satisfying $\int q(\mathbf{z}) d\mathbf{z} = 1$.

Start from the observed log-likelihood $\ell(\boldsymbol{\theta}) = \ln p(\mathbf{Y} \mid \boldsymbol{\theta})$:
$$\ell(\boldsymbol{\theta}) = \ln p(\mathbf{Y} \mid \boldsymbol{\theta}) \int q(\mathbf{z}) \, d\mathbf{z} = \int q(\mathbf{z}) \ln p(\mathbf{Y} \mid \boldsymbol{\theta}) \, d\mathbf{z}$$

By Bayes' rule:
$$p(\mathbf{Y} \mid \boldsymbol{\theta}) = \frac{p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta})}$$

Multiply top and bottom by $q(\mathbf{z})$:
$$p(\mathbf{Y} \mid \boldsymbol{\theta}) = \frac{p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta})}{q(\mathbf{z})} \cdot \frac{q(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta})}$$

Take the logarithm:
$$\ln p(\mathbf{Y} \mid \boldsymbol{\theta}) = \ln\left( \frac{p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta})}{q(\mathbf{z})} \right) + \ln\left( \frac{q(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta})} \right)$$

Integrate with respect to $q(\mathbf{z}) d\mathbf{z}$:
$$\ell(\boldsymbol{\theta}) = \int q(\mathbf{z}) \ln\left( \frac{p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta})}{q(\mathbf{z})} \right) d\mathbf{z} + \int q(\mathbf{z}) \ln\left( \frac{q(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta})} \right) d\mathbf{z}$$

Recognize the two terms:
1. The first term is the **Evidence Lower Bound (ELBO)** $\mathcal{L}(q, \boldsymbol{\theta})$:
   $$\mathcal{L}(q, \boldsymbol{\theta}) = \int q(\mathbf{z}) \ln\left( \frac{p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta})}{q(\mathbf{z})} \right) d\mathbf{z}$$
2. The second term is the Kullback–Leibler divergence $\mathcal{D}_{KL}(q(\mathbf{Z}) \,\|\, p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}))$.

Therefore:

$$\ell(\boldsymbol{\theta}) = \mathcal{L}(q, \boldsymbol{\theta}) + \mathcal{D}_{KL}(q(\mathbf{Z}) \,\|\, p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}))$$

Because $\mathcal{D}_{KL} \ge 0$, this establishes that $\mathcal{L}(q, \boldsymbol{\theta})$ is a strict **lower bound** on the log-likelihood:
$$\ell(\boldsymbol{\theta}) \ge \mathcal{L}(q, \boldsymbol{\theta})$$

---

### Solution, step 3: Action of the E-step

**Solution, step 3: Action of the E-step.**

In the E-step, the parameter is fixed at its current value $\boldsymbol{\theta}^{(t)}$. We maximize the lower bound $\mathcal{L}(q, \boldsymbol{\theta}^{(t)})$ with respect to the distribution $q$:

$$\max_q \mathcal{L}(q, \boldsymbol{\theta}^{(t)}) \iff \min_q \mathcal{D}_{KL}(q(\mathbf{Z}) \,\|\, p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)}))$$

By Gibbs' Inequality, the KL divergence attains its absolute minimum of **zero** if and only if:

$$q^*(\mathbf{z}) = p(\mathbf{z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t)})$$

When $q$ is set to the exact posterior of the latent variables:
$$\mathcal{D}_{KL} = 0 \implies \mathcal{L}(q^*, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)})$$

The lower bound becomes **tangent to the true log-likelihood curve** at $\boldsymbol{\theta}^{(t)}$!

Furthermore, evaluate $\mathcal{L}(q^*, \boldsymbol{\theta})$:
$$\mathcal{L}(q^*, \boldsymbol{\theta}) = \int q^*(\mathbf{z}) \ln p(\mathbf{Y}, \mathbf{z} \mid \boldsymbol{\theta}) \, d\mathbf{z} - \int q^*(\mathbf{z}) \ln q^*(\mathbf{z}) \, d\mathbf{z}$$
$$= Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)}) + \text{Entropy}(q^*)$$
Since the entropy of $q^*$ does not depend on $\boldsymbol{\theta}$, maximizing $\mathcal{L}(q^*, \boldsymbol{\theta})$ with respect to $\boldsymbol{\theta}$ is **identical to maximizing the $Q$-function**!

---

### Solution, step 4: Complete proof of monotonic ascent

**Solution, step 4: Complete proof of monotonic ascent.**

Now evaluate the progression across the two steps:

1. **E-step Tangency**:
   $$\ell(\boldsymbol{\theta}^{(t)}) = \mathcal{L}(q^*, \boldsymbol{\theta}^{(t)})$$

2. **M-step Maximization**:
   The M-step updates $\boldsymbol{\theta}^{(t+1)} = \arg\max_{\boldsymbol{\theta}} Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)}) = \arg\max_{\boldsymbol{\theta}} \mathcal{L}(q^*, \boldsymbol{\theta})$. Therefore:
   $$\mathcal{L}(q^*, \boldsymbol{\theta}^{(t+1)}) \ge \mathcal{L}(q^*, \boldsymbol{\theta}^{(t)})$$

3. **Lower Bound Property**:
   By the variational decomposition, for any $\boldsymbol{\theta}$, including $\boldsymbol{\theta}^{(t+1)}$:
   $$\ell(\boldsymbol{\theta}^{(t+1)}) = \mathcal{L}(q^*, \boldsymbol{\theta}^{(t+1)}) + \mathcal{D}_{KL}(q^*(\mathbf{Z}) \,\|\, p(\mathbf{Z} \mid \mathbf{Y}, \boldsymbol{\theta}^{(t+1)}))$$
   Since $\mathcal{D}_{KL} \ge 0$:
   $$\ell(\boldsymbol{\theta}^{(t+1)}) \ge \mathcal{L}(q^*, \boldsymbol{\theta}^{(t+1)})$$

Chaining the inequalities together:

$$\ell(\boldsymbol{\theta}^{(t+1)}) \ge \mathcal{L}(q^*, \boldsymbol{\theta}^{(t+1)}) \ge \mathcal{L}(q^*, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)})$$

Therefore:

$$\ell(\boldsymbol{\theta}^{(t+1)}) \ge \ell(\boldsymbol{\theta}^{(t)})$$

This completes the mathematical proof that the observed log-likelihood **monotonically increases at every iteration of the EM algorithm**.

---

## Fully worked question 3: Newton–Raphson vs Fisher Scoring Convergence Rate and Numerical Step Computation for a Gamma GLM

### Question
An environmental engineer models rainfall depth $Y_i > 0$ using a **Gamma Generalized Linear Model** with a reciprocal link function (the canonical link):

$$Y_i \sim \text{Gamma}(\mu_i, \nu), \quad g(\mu_i) = \frac{1}{\mu_i} = \eta_i = \mathbf{x}_i^\top \boldsymbol{\beta}$$

The probability density function of $Y \sim \text{Gamma}(\mu, \nu)$ is:
$$f(y \mid \mu, \nu) = \frac{1}{\Gamma(\nu)} \left( \frac{\nu}{\mu} \right)^\nu y^{\nu - 1} \exp\left( -\frac{\nu y}{\mu} \right), \quad y > 0$$
where $\nu > 0$ is the known shape parameter.

1. Show that the Gamma distribution belongs to the exponential dispersion family, and identify the natural parameter $\theta$, cumulant function $b(\theta)$, and variance function $V(\mu)$.
2. Derive the log-likelihood function $\ell(\boldsymbol{\beta})$, the score vector $\mathbf{g}(\boldsymbol{\beta})$, and the observed Hessian matrix $\mathbf{H}(\boldsymbol{\beta})$.
3. Derive the Expected (Fisher) Information Matrix $\mathcal{I}(\boldsymbol{\beta})$ and prove whether Newton–Raphson and Fisher Scoring are identical for this canonical Gamma GLM.
4. An empirical calibration collects $n = 3$ precipitation observations:
   $$\mathbf{y} = [0.8, \, 1.2, \, 2.0]^\top, \quad \mathbf{x} = [1.0, \, 2.0, \, 3.0]^\top, \quad \nu = 1.0 \quad (\text{standard Exponential})$$
   Under model $\frac{1}{\mu_i} = \beta x_i$, starting from initial estimate $\beta^{(0)} = 0.50$:
   - Compute the fitted means $\mu_i^{(0)}$
   - Compute the score value $g(\beta^{(0)})$
   - Compute the information value $\mathcal{I}(\beta^{(0)})$
   - Calculate the updated parameter $\beta^{(1)}$ to four decimal places.

---

### Solution, step 1: Exponential dispersion formulation of the Gamma distribution

**Solution, step 1: Exponential dispersion formulation of the Gamma distribution.**

Rewrite the density $f(y \mid \mu, \nu)$:
$$f(y \mid \mu, \nu) = \exp\left( \ln\left[ \frac{1}{\Gamma(\nu)} \left( \frac{\nu}{\mu} \right)^\nu y^{\nu - 1} \exp\left( -\frac{\nu y}{\mu} \right) \right] \right)$$
$$= \exp\left( -\frac{\nu y}{\mu} - \nu \ln \mu + \nu \ln\nu + (\nu - 1)\ln y - \ln\Gamma(\nu) \right)$$
Multiply and divide by $\nu = 1/\phi$ (where dispersion $\phi = 1/\nu$):
$$= \exp\left( \frac{y (-1/\mu) - \ln\mu}{1/\nu} + (\nu - 1)\ln y + \nu\ln\nu - \ln\Gamma(\nu) \right)$$

This matches the canonical exponential dispersion family format:
$$f(y \mid \theta, \phi) = \exp\left( \frac{y \theta - b(\theta)}{a(\phi)} + c(y, \phi) \right)$$
where:
1. **Natural Parameter**:
   $$\theta = -\frac{1}{\mu} \implies \mu = -\frac{1}{\theta}$$
2. **Cumulant Generator Function**:
   $$b(\theta) = \ln\mu = \ln\left( -\frac{1}{\theta} \right) = -\ln(-\theta)$$
3. **Dispersion Parameter**:
   $$a(\phi) = \phi = \frac{1}{\nu}$$
4. **Mean and Variance Functions**:
   $$\mathbb{E}[Y] = b'(\theta) = -\frac{1}{-\theta} (-1) = -\frac{1}{\theta} = \mu$$
   $$\text{Var}(Y) = b''(\theta) a(\phi) = \frac{1}{\theta^2} \phi = \mu^2 \phi$$
   Therefore, the **variance function** is:
   $$V(\mu) = \mu^2$$

---

### Solution, step 2: Log-likelihood, score vector, and observed Hessian

**Solution, step 2: Log-likelihood, score vector, and observed Hessian.**

With canonical link $\eta_i = \frac{1}{\mu_i} = \mathbf{x}_i^\top \boldsymbol{\beta}$, the natural parameter is:
$$\theta_i = -\frac{1}{\mu_i} = -\mathbf{x}_i^\top \boldsymbol{\beta}$$

1. **Log-Likelihood Function**:
   $$\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ \frac{y_i (-\mathbf{x}_i^\top \boldsymbol{\beta}) - (-\ln(\mathbf{x}_i^\top \boldsymbol{\beta}))}{1/\nu} \right] + \text{constant}$$
   $$\ell(\boldsymbol{\beta}) = \nu \sum_{i=1}^n \left[ -y_i (\mathbf{x}_i^\top \boldsymbol{\beta}) + \ln(\mathbf{x}_i^\top \boldsymbol{\beta}) \right] + \text{constant}$$

2. **Score Vector (Gradient)**:
   Differentiate with respect to $\beta_j$:
   $$\frac{\partial \ell}{\partial \beta_j} = \nu \sum_{i=1}^n \left[ -y_i x_{ij} + \frac{x_{ij}}{\mathbf{x}_i^\top \boldsymbol{\beta}} \right] = \nu \sum_{i=1}^n \left( \frac{1}{\mathbf{x}_i^\top \boldsymbol{\beta}} - y_i \right) x_{ij}$$
   Since $\mu_i = \frac{1}{\mathbf{x}_i^\top \boldsymbol{\beta}}$:
   $$\frac{\partial \ell}{\partial \beta_j} = \nu \sum_{i=1}^n (\mu_i - y_i) x_{ij}$$

   In matrix notation:
   $$\mathbf{g}(\boldsymbol{\beta}) = \nu \mathbf{X}^\top (\boldsymbol{\mu} - \mathbf{y})$$

3. **Observed Hessian Matrix**:
   Differentiate $\frac{\partial \ell}{\partial \beta_j}$ with respect to $\beta_k$:
   $$H_{jk}(\boldsymbol{\beta}) = \frac{\partial^2 \ell}{\partial \beta_j \partial \beta_k} = \nu \sum_{i=1}^n \frac{\partial \mu_i}{\partial \beta_k} x_{ij}$$
   Since $\mu_i = (\mathbf{x}_i^\top \boldsymbol{\beta})^{-1}$:
   $$\frac{\partial \mu_i}{\partial \beta_k} = -\frac{x_{ik}}{(\mathbf{x}_i^\top \boldsymbol{\beta})^2} = -\mu_i^2 x_{ik}$$
   Therefore:
   $$H_{jk}(\boldsymbol{\beta}) = -\nu \sum_{i=1}^n \mu_i^2 x_{ij} x_{ik}$$

   In matrix notation:
   $$\mathbf{H}(\boldsymbol{\beta}) = -\nu \mathbf{X}^\top \text{diag}(\mu_1^2, \dots, \mu_n^2) \mathbf{X}$$

---

### Solution, step 3: Expected information and equivalence proof

**Solution, step 3: Expected information and equivalence proof.**

Notice that the Hessian matrix:
$$\mathbf{H}(\boldsymbol{\beta}) = -\nu \mathbf{X}^\top \text{diag}(\mu_i^2) \mathbf{X}$$
depends solely on the model means $\mu_i = 1 / (\mathbf{x}_i^\top \boldsymbol{\beta})$ and covariates $\mathbf{X}$. It is **completely independent of the random realizations $y_i$**!

Therefore:
$$\mathcal{I}(\boldsymbol{\beta}) = \mathbb{E}[-\mathbf{H}(\boldsymbol{\beta})] = -\mathbf{H}(\boldsymbol{\beta}) = \nu \mathbf{X}^\top \text{diag}(\mu_1^2, \dots, \mu_n^2) \mathbf{X}$$

Because $\mathcal{J}(\boldsymbol{\beta}) \equiv \mathcal{I}(\boldsymbol{\beta})$, the Newton–Raphson algorithm and the Fisher Scoring algorithm are **strictly mathematically identical** for this canonical Gamma GLM!

---

### Solution, step 4: Numerical computation of update step 1

**Solution, step 4: Numerical computation of update step 1.**

We are given:
- $\nu = 1.0$
- $\mathbf{y} = [0.8, \, 1.2, \, 2.0]^\top$
- $\mathbf{x} = [1.0, \, 2.0, \, 3.0]^\top$
- Model: $\frac{1}{\mu_i} = \beta x_i$
- Initial parameter: $\beta^{(0)} = 0.50$.

1. **Calculate Fitted Means at Step 0**:
   $$\mu_i^{(0)} = \frac{1}{\beta^{(0)} x_i} = \frac{1}{0.50 \times x_i} = \frac{2.0}{x_i}$$
   - For $i = 1$ ($x_1 = 1.0$): $\mu_1^{(0)} = \frac{2.0}{1.0} = \mathbf{2.0}$
   - For $i = 2$ ($x_2 = 2.0$): $\mu_2^{(0)} = \frac{2.0}{2.0} = \mathbf{1.0}$
   - For $i = 3$ ($x_3 = 3.0$): $\mu_3^{(0)} = \frac{2.0}{3.0} \approx \mathbf{0.666667}$

2. **Calculate the Score Function $g(\beta^{(0)})$**:
   $$g(\beta) = \nu \sum_{i=1}^3 x_i (\mu_i - y_i) = 1.0 \sum_{i=1}^3 x_i (\mu_i - y_i)$$
   Compute each observation's contribution:
   - $i = 1$: $x_1 (\mu_1 - y_1) = 1.0 \times (2.0 - 0.8) = 1.0 \times 1.2 = \mathbf{1.20}$
   - $i = 2$: $x_2 (\mu_2 - y_2) = 2.0 \times (1.0 - 1.2) = 2.0 \times (-0.2) = \mathbf{-0.40}$
   - $i = 3$: $x_3 (\mu_3 - y_3) = 3.0 \times (0.666667 - 2.0) = 3.0 \times (-1.333333) = \mathbf{-4.00}$

   Summing across all 3 observations:
   $$g(\beta^{(0)}) = 1.20 - 0.40 - 4.00 = \mathbf{-3.20}$$

3. **Calculate Fisher Information $\mathcal{I}(\beta^{(0)})$**:
   $$\mathcal{I}(\beta) = \nu \sum_{i=1}^3 x_i^2 \mu_i^2 = 1.0 \sum_{i=1}^3 (x_i \mu_i)^2$$
   Notice that $x_i \mu_i = x_i \left( \frac{1}{\beta x_i} \right) = \frac{1}{\beta} = \frac{1}{0.50} = 2.0$ for **all** observations!
   $$(x_i \mu_i)^2 = (2.0)^2 = 4.0 \quad \text{for each observation } i$$

   Summing across all 3 observations:
   $$\mathcal{I}(\beta^{(0)}) = 4.0 + 4.0 + 4.0 = \mathbf{12.0}$$

4. **Compute the Updated Parameter $\beta^{(1)}$**:
   The Fisher scoring update step is:
   $$\beta^{(1)} = \beta^{(0)} + [\mathcal{I}(\beta^{(0)})]^{-1} g(\beta^{(0)})$$
   $$\beta^{(1)} = 0.50 + \frac{-3.20}{12.0} = 0.50 - \frac{3.2}{12.0} = 0.50 - \frac{8}{30} = 0.50 - 0.266667$$

   $$\beta^{(1)} = \mathbf{0.2333}$$

The parameter estimate updates from $\beta^{(0)} = 0.5000$ to $\beta^{(1)} \approx 0.2333$ in a single iteration.
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(unit7_text)

print("Successfully written deep Unit 7!")
