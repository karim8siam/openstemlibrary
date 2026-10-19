import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-statistical-estimation")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def prose_count(text):
    text = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    text = re.sub(r"\$[^$\n]+\$", " ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

# ==============================================================================
# UNIT 4: Methods of Point Estimation: Method of Moments & Maximum Likelihood
# ==============================================================================
u4_text = """# Unit 4: Methods of Point Estimation: Method of Moments & Maximum Likelihood

In previous units, we evaluated point estimators by examining their theoretical properties, including unbiasedness, variance lower bounds, and sufficiency. We now turn to constructive algorithms for deriving point estimators directly from statistical models and empirical data. Two primary general-purpose paradigms dominate classical mathematical statistics: the Method of Moments (MOM), introduced by Pafnuty Chebyshev and popularized by Karl Pearson in the 1890s, and the Method of Maximum Likelihood (MLE), formulated by Ronald A. Fisher in 1912 and 1922. In this unit, we rigorously develop both estimation frameworks, explore their theoretical underpinnings, examine regularity conditions and boundary pathologies, establish the invariance property of maximum likelihood estimators, analyze numerical algorithms including Newton–Raphson, Fisher scoring, and the Expectation–Maximization (EM) algorithm, and investigate robust M-estimation.

## 4.1 Classical Method of Moments (MOM): Foundations, Sample vs Population Moments

The Method of Moments is historically the oldest systematic general technique for parameter estimation. Its underlying philosophy rests on the **analogy principle**: if a theoretical probability distribution $P_\\theta$ depends on $k$ unknown parameters $\\boldsymbol{\\theta} = (\\theta_1, \\dots, \\theta_k)^T$, and if the first $k$ population moments exist as functions of $\\boldsymbol{\\theta}$, then equating these theoretical moments to their empirical sample counterparts generates a system of $k$ simultaneous equations whose solution yields point estimates for $\\boldsymbol{\\theta}$.

### Population Moments and Sample Moments
Let $X_1, X_2, \\dots, X_n$ be an independent, identically distributed random sample from a distribution with probability density or mass function $f(x; \\boldsymbol{\\theta})$.

The $r$-th **population raw moment** is defined as:

$$\\alpha_r(\\boldsymbol{\\theta}) = \\mathbb{E}_{\\boldsymbol{\\theta}}[X^r] = \\int_{-\\infty}^\\infty x^r f(x; \\boldsymbol{\\theta}) \\, dx$$

assuming the integral converges absolutely ($\\mathbb{E}[|X|^r] < \\infty$).
The $r$-th **sample raw moment** is the empirical arithmetic average:

$$m_r = \\frac{1}{n} \\sum_{i=1}^n X_i^r$$

Similarly, the $r$-th population central moment is $\\mu_r(\\boldsymbol{\\theta}) = \\mathbb{E}[(X - \\mu)^r]$, and the $r$-th sample central moment is:

$$c_r = \\frac{1}{n} \\sum_{i=1}^n (X_i - \\bar{X})^r$$

### The MOM System of Equations
To estimate a $k$-dimensional parameter vector $\\boldsymbol{\\theta} = (\\theta_1, \\dots, \\theta_k)^T$, we set up the first $k$ moment-matching equations:

$$\\begin{cases} \\alpha_1(\\theta_1, \\dots, \\theta_k) = m_1 = \\frac{1}{n} \\sum_{i=1}^n X_i \\\\ \\alpha_2(\\theta_1, \\dots, \\theta_k) = m_2 = \\frac{1}{n} \\sum_{i=1}^n X_i^2 \\\\ \\vdots \\\\ \\alpha_k(\\theta_1, \\dots, \\theta_k) = m_k = \\frac{1}{n} \\sum_{i=1}^n X_i^k \\end{cases}$$

Assuming the mapping $\\boldsymbol{\\alpha}: \\Theta \\to \\mathbb{R}^k$ given by $\\boldsymbol{\\alpha}(\\boldsymbol{\\theta}) = (\\alpha_1(\\boldsymbol{\\theta}), \\dots, \\alpha_k(\\boldsymbol{\\theta}))^T$ is one-to-one and continuously invertible on its range, the **Method of Moments Estimator (MOME)** $\\tilde{\\boldsymbol{\\theta}}$ is the unique solution:

$$\\tilde{\\boldsymbol{\\theta}} = \\mathbf{g}(m_1, m_2, \\dots, m_k) = \\boldsymbol{\\alpha}^{-1}(\\mathbf{m})$$

### Advantages and Operational Limitations of MOM
The Method of Moments possesses several appealing practical virtues:
1. **Computational Simplicity**: In many classical distribution families (such as Gamma, Beta, Normal, Poisson, and Weibull), the moment equations reduce to straightforward algebraic formulas or low-degree polynomials that can be solved in closed form without iterative numerical optimization.
2. **Distribution-Free Moments**: Evaluating population moments often requires only basic calculus, avoiding the need to evaluate normalizing constants or complex likelihood normalizers.

However, the Method of Moments suffers from severe theoretical and practical deficiencies:
- **Severe Inefficiency**: MOM estimators often fail to attain the Cramér–Rao Lower Bound and discard substantial amounts of Fisher Information. In heavy-tailed distributions or mixtures, the asymptotic variance of MOM estimators can be orders of magnitude larger than that of maximum likelihood estimators.
- **Inadmissibility and Boundary Violations**: Because sample moments $m_r$ are unconstrained random variables, the resulting estimate $\\tilde{\\boldsymbol{\\theta}} = \\boldsymbol{\\alpha}^{-1}(\\mathbf{m})$ can fall outside the physically valid parameter space $\\Theta$. For example, when estimating Beta parameters $(\\alpha, \\beta)$, a large sample variance $c_2 > m_1(1 - m_1)$ can produce negative parameter estimates $\\tilde{\\alpha} < 0$, which is physically impossible.
- **Sensitivity to Outliers**: High-order sample moments $m_3, m_4$ involve cubing and quadrupling observations, making them hypersensitive to extreme values and measurement errors.

## 4.2 Large-Sample Properties of MOM: Consistency and Asymptotic Normality via Delta Method

Despite their finite-sample inefficiencies, Method of Moments estimators possess excellent asymptotic properties under broad regularity conditions.

### Theorem: Strong Consistency of MOM Estimators
Let $X_1, \\dots, X_n$ be an i.i.d. sample from $f(x; \\boldsymbol{\\theta})$ such that the first $k$ population moments $\\alpha_1(\\boldsymbol{\\theta}), \\dots, \\alpha_k(\\boldsymbol{\\theta})$ exist and are finite. Let $\\mathbf{g} = \\boldsymbol{\\alpha}^{-1}: \\mathbb{R}^k \\to \\Theta$ be continuous at the true moment vector $\\boldsymbol{\\alpha}(\\boldsymbol{\\theta}_0)$. Then the MOM estimator $\\tilde{\\boldsymbol{\\theta}}_n = \\mathbf{g}(\\mathbf{m}_n)$ is **strongly consistent**:

$$\\tilde{\\boldsymbol{\\theta}}_n \\xrightarrow{\\text{a.s.}} \\boldsymbol{\\theta}_0 \\quad \\text{as } n \\to \\infty$$

#### Proof:
By Kolmogorov's Strong Law of Large Numbers (SLLN), each sample moment converges almost surely to its corresponding theoretical population moment:

$$m_{r, n} = \\frac{1}{n} \\sum_{i=1}^n X_i^r \\xrightarrow{\\text{a.s.}} \\mathbb{E}[X^r] = \\alpha_r(\\boldsymbol{\\theta}_0), \\quad r = 1, 2, \\dots, k$$

In vector notation, $\\mathbf{m}_n \\xrightarrow{\\text{a.s.}} \\boldsymbol{\\alpha}(\\boldsymbol{\\theta}_0)$.
Because $\\mathbf{g}$ is continuous at $\\boldsymbol{\\alpha}(\\boldsymbol{\\theta}_0)$, the Continuous Mapping Theorem immediately yields:

$$\\tilde{\\boldsymbol{\\theta}}_n = \\mathbf{g}(\\mathbf{m}_n) \\xrightarrow{\\text{a.s.}} \\mathbf{g}(\\boldsymbol{\\alpha}(\\boldsymbol{\\theta}_0)) = \\boldsymbol{\\theta}_0$$

### Asymptotic Normality via the Multivariate Delta Method
If the distribution possesses finite moments up to order $2k$ (so that $\\mathbb{E}[X^{2k}] < \\infty$), the multivariate Central Limit Theorem guarantees that the sample moment vector is asymptotically normal:

$$\\sqrt{n}(\\mathbf{m}_n - \\boldsymbol{\\alpha}(\\boldsymbol{\\theta})) \\xrightarrow{d} \\mathcal{N}_k(\\mathbf{0}, \\boldsymbol{\\Sigma}_{\\mathbf{m}})$$

where the covariance matrix entries are given by:

$$[\\boldsymbol{\\Sigma}_{\\mathbf{m}}]_{ij} = \\text{Cov}(X^i, X^j) = \\alpha_{i+j}(\\boldsymbol{\\theta}) - \\alpha_i(\\boldsymbol{\\theta}) \\alpha_j(\\boldsymbol{\\theta})$$

If $\\mathbf{g}(\\mathbf{u})$ is continuously differentiable with Jacobian matrix $\\mathbf{J}_{\\mathbf{g}}(\\mathbf{u}) = \\nabla \\mathbf{g}(\\mathbf{u})$, the **Multivariate Delta Method** establishes that:

$$\\sqrt{n}(\\tilde{\\boldsymbol{\\theta}}_n - \\boldsymbol{\\theta}) \\xrightarrow{d} \\mathcal{N}_k\\left( \\mathbf{0}, \\mathbf{J}_{\\mathbf{g}}(\\boldsymbol{\\alpha}) \\boldsymbol{\\Sigma}_{\\mathbf{m}} \\mathbf{J}_{\\mathbf{g}}(\\boldsymbol{\\alpha})^T \\right)$$

This provides closed-form asymptotic variance expressions for MOM estimators, enabling the construction of large-sample confidence intervals and hypothesis tests.

## 4.3 Maximum Likelihood Estimation (MLE): Likelihood Equations, Score Vector, and Hessian Curvature

The foundational method of modern parametric inference is Ronald A. Fisher's **Method of Maximum Likelihood**. The core intuition of maximum likelihood estimation is that among all conceivable parameter values $\\theta \\in \\Theta$, the preferred point estimate is the parameter value that assigns the highest probability (or probability density) to the realized, observed empirical data.

### Definition of Maximum Likelihood Estimator
Let $\\mathbf{x} = (x_1, \\dots, x_n)$ be the realized sample from a model with joint density $f_n(\\mathbf{x}; \\boldsymbol{\\theta})$. The **likelihood function** is $L(\\boldsymbol{\\theta}; \\mathbf{x}) = f_n(\\mathbf{x}; \\boldsymbol{\\theta})$.
A **Maximum Likelihood Estimator (MLE)** $\\hat{\\boldsymbol{\\theta}} = \\hat{\\boldsymbol{\\theta}}(\\mathbf{X})$ is any value in the parameter space $\\Theta$ that globally maximizes the likelihood function:

$$L(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x}) = \\sup_{\\boldsymbol{\\theta} \\in \\Theta} L(\\boldsymbol{\\theta}; \\mathbf{x})$$

Because the natural logarithm is a strictly increasing monotonic transformation on $(0, \\infty)$, maximizing $L(\\boldsymbol{\\theta}; \\mathbf{x})$ is mathematically identical to maximizing the **log-likelihood function**:

$$\\ell(\\boldsymbol{\\theta}; \\mathbf{x}) = \\ln L(\\boldsymbol{\\theta}; \\mathbf{x}) = \\sum_{i=1}^n \\ln f(x_i; \\boldsymbol{\\theta})$$

$$\\hat{\\boldsymbol{\\theta}} = \\arg\\max_{\\boldsymbol{\\theta} \\in \\Theta} \\ell(\\boldsymbol{\\theta}; \\mathbf{x})$$

### The Likelihood Equations
When $\\Theta$ is an open subset of $\\mathbb{R}^k$ and $\\ell(\\boldsymbol{\\theta}; \\mathbf{x})$ is continuously differentiable, any interior local maximum must satisfy Fermat's first-order stationary condition. The gradient of the log-likelihood is the **Score Vector** $\\mathbf{S}(\\boldsymbol{\\theta}; \\mathbf{x}) = \\nabla_{\\boldsymbol{\\theta}} \\ell(\\boldsymbol{\\theta}; \\mathbf{x})$.
Setting the score vector equal to zero generates the **Likelihood Equations**:

$$\\mathbf{S}(\\boldsymbol{\\theta}; \\mathbf{x}) = \\mathbf{0} \\iff \\begin{cases} \\frac{\\partial \\ell(\\boldsymbol{\\theta}; \\mathbf{x})}{\\partial \\theta_1} = 0 \\\\ \\frac{\\partial \\ell(\\boldsymbol{\\theta}; \\mathbf{x})}{\\partial \\theta_2} = 0 \\\\ \\vdots \\\\ \\frac{\\partial \\ell(\\boldsymbol{\\theta}; \\mathbf{x})}{\\partial \\theta_k} = 0 \\end{cases}$$

### Second-Order Sufficiency Conditions and Hessian Curvature
To verify that a critical point $\\hat{\\boldsymbol{\\theta}}$ satisfying the score equations is indeed a local maximum (rather than a saddle point or minimum), the **Hessian matrix** of second partial derivatives:

$$\\mathcal{H}(\\boldsymbol{\\theta}; \\mathbf{x}) = \\nabla_{\\boldsymbol{\\theta}}^2 \\ell(\\boldsymbol{\\theta}; \\mathbf{x}) = \\left[ \\frac{\\partial^2 \\ell(\\boldsymbol{\\theta}; \\mathbf{x})}{\\partial \\theta_i \\partial \\theta_j} \\right]_{1 \\le i, j \\le k}$$

must be strictly **negative-definite** when evaluated at $\\hat{\\boldsymbol{\\theta}}$:

$$\\mathbf{v}^T \\mathcal{H}(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x}) \\mathbf{v} < 0 \\quad \\forall \\mathbf{v} \\in \\mathbb{R}^k \\setminus \\{\\mathbf{0}\\}$$

Equivalently, the **Observed Information Matrix** $J(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x}) = -\\mathcal{H}(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x})$ must be strictly positive-definite: all its eigenvalues must be strictly positive.

## 4.4 Global Concavity, Unimodality, and Interior vs Boundary Critical Points

Solving the first-order likelihood equations $\\nabla \\ell = \\mathbf{0}$ does not automatically identify the global MLE. Three distinct structural complications can arise:

1. **Strictly Concave Log-Likelihoods (Global Uniqueness)**:
   If the log-likelihood function $\\ell(\\boldsymbol{\\theta}; \\mathbf{x})$ is strictly concave over a convex parameter space $\\Theta$—meaning its Hessian $\\mathcal{H}(\\boldsymbol{\\theta}; \\mathbf{x})$ is strictly negative-definite everywhere on $\\Theta$—then the log-likelihood surface is strictly unimodal. Any stationary point satisfying $\\nabla \\ell(\\hat{\\boldsymbol{\\theta}}) = \\mathbf{0}$ is guaranteed to be the unique global maximum.
   *Example*: In natural exponential families with open convex parameter spaces (such as Gaussian, Poisson, Binomial, and Gamma), the log-likelihood is strictly concave, ensuring that the MLE is unique whenever a solution exists.
2. **Multimodal Likelihoods (Local Maxima and Spurious Roots)**:
   In complex models—including finite mixture distributions, neural networks, Gaussian processes, and Cauchy distributions—the likelihood surface features multiple local peaks, ridges, and saddle points. Standard root-finding algorithms (such as Newton–Raphson) can converge to an inferior local maximum or saddle point. Finding the true global MLE requires multiple random restarts, global annealing, or grid searches.
3. **Boundary Solutions**:
   If the maximum of $L(\\boldsymbol{\\theta})$ occurs on the topological boundary $\\partial \\Theta$ of the parameter space, the score vector at the maximum may not be zero ($\\nabla \\ell(\\hat{\\boldsymbol{\\theta}}) \\ne \\mathbf{0}$). In constrained optimization (such as enforcing non-negative variances $\\sigma^2 \\ge 0$ in random-effects models), the MLE must be identified using Karush–Kuhn–Tucker (KKT) conditions.

## 4.5 Non-Regular Maximum Likelihood: Shifted Weibull, Uniform, and Pareto Distributions

When the support of the probability density depends on the unknown parameter $\\theta$, standard calculus techniques collapse. The likelihood function is not differentiable across the support boundary, and the MLE is typically determined by order statistics rather than score equations.

### Canonical Example: Uniform Distribution $\\text{Uniform}(0, \\theta)$
Let $X_1, \\dots, X_n \\sim \\text{Uniform}(0, \\theta)$ where $\\theta > 0$.
The joint likelihood function is:

$$L(\\theta; \\mathbf{x}) = \\frac{1}{\\theta^n} \\prod_{i=1}^n \\mathbf{1}_{\\{0 \\le x_i \\le \\theta\\}} = \\frac{1}{\\theta^n} \\mathbf{1}_{\\{x_{(n)} \\le \\theta\\}} \\mathbf{1}_{\\{x_{(1)} \\ge 0\\}}$$

where $x_{(n)} = \\max(x_1, \\dots, x_n)$.
Notice the analytical behavior of $L(\\theta)$ as a function of $\\theta$:
- If $\\theta < x_{(n)}$, at least one observation falls outside the interval $[0, \\theta]$, so $L(\\theta) = 0$.
- If $\\theta \\ge x_{(n)}$, all observations are inside $[0, \\theta]$, so $L(\\theta) = \\frac{1}{\\theta^n}$.

On the domain $\\theta \\in [x_{(n)}, \\infty)$, the function $L(\\theta) = \\theta^{-n}$ is a strictly decreasing function of $\\theta$. Its derivative $\\frac{dL}{d\\theta} = -n \\theta^{-(n+1)} < 0$ is strictly negative everywhere, so setting the derivative to zero yields no solution!
To maximize a strictly decreasing function over the interval $[x_{(n)}, \\infty)$, we must choose the smallest permissible value in the domain.
Therefore, the Maximum Likelihood Estimator is:

$$\\hat{\\theta}_{\\text{MLE}} = X_{(n)} = \\max(X_1, X_2, \\dots, X_n)$$

Notice that $\\hat{\\theta}$ is an order statistic located precisely on the boundary of the feasible domain.
Furthermore, because $X_i < \\theta$ with probability $1$, we have $X_{(n)} < \\theta$ with probability $1$.
Thus, the MLE systematically underestimates $\\theta$:

$$\\mathbb{E}[\\hat{\\theta}] = \\frac{n}{n + 1} \\theta < \\theta$$

The MLE is biased, but asymptotically unbiased as $n \\to \\infty$.

### Shifted Exponential and Pareto Models
Similarly, for a shifted exponential distribution $f(x; \\theta, \\lambda) = \\lambda e^{-\\lambda (x - \\theta)} \\mathbf{1}_{\\{x \\ge \\theta\\}}$, the likelihood is strictly increasing with respect to $\\theta$ up to the threshold $x_{(1)} = \\min(x_1, \\dots, x_n)$, making the MLE:

$$\\hat{\\theta}_{\\text{MLE}} = X_{(1)} = \\min(X_1, \\dots, X_n)$$

In non-regular models, maximum likelihood estimators frequently achieve super-efficient convergence rates of order $\\mathcal{O}(n)$ rather than the standard $\\mathcal{O}(\\sqrt{n})$ Gaussian rate.

## 4.6 Functional Invariance Property of Maximum Likelihood Estimators (Zeena's Theorem)

One of the most powerful and celebrated practical advantages of maximum likelihood estimation over all other estimation frameworks (including unbiasedness and Method of Moments) is its **functional invariance property**, originally proved in full generality by Zeena (1966).

### Theorem: The Invariance Property of MLEs
Let $\\hat{\\boldsymbol{\\theta}}$ be the Maximum Likelihood Estimator of a parameter vector $\\boldsymbol{\\theta} \\in \\Theta$. Let $g: \\Theta \\to \\Omega$ be any arbitrary function (which need not be one-to-one or invertible).
Then the Maximum Likelihood Estimator of the transformed parameter $\\tau = g(\\boldsymbol{\\theta})$ is:

$$\\hat{\\tau} = g(\\hat{\\boldsymbol{\\theta}})$$

#### Proof:
If $g$ is a one-to-one (bijective) mapping, the result is trivial: reparameterizing the likelihood $L^*(\\tau) = L(g^{-1}(\\tau))$ preserves the supremum, so $\\hat{\\tau} = g(\\hat{\\boldsymbol{\\theta}})$.
Now consider the general case where $g$ is **not one-to-one** (many-to-one).
To define the likelihood function for $\\tau$, we utilize the concept of the **profile likelihood** (induced likelihood). For any $\\tau \\in \\Omega$, define:

$$L_g(\\tau; \\mathbf{x}) = \\sup_{\\boldsymbol{\\theta} \\in \\Theta : g(\\boldsymbol{\\theta}) = \\tau} L(\\boldsymbol{\\theta}; \\mathbf{x})$$

The maximum likelihood estimator of $\\tau$ is defined as the value $\\hat{\\tau}$ that maximizes $L_g(\\tau; \\mathbf{x})$ over $\\Omega$:

$$\\sup_{\\tau \\in \\Omega} L_g(\\tau; \\mathbf{x}) = \\sup_{\\tau \\in \\Omega} \\left( \\sup_{\\boldsymbol{\\theta} \\in \\Theta : g(\\boldsymbol{\\theta}) = \\tau} L(\\boldsymbol{\\theta}; \\mathbf{x}) \\right) = \\sup_{\\boldsymbol{\\theta} \\in \\Theta} L(\\boldsymbol{\\theta}; \\mathbf{x}) = L(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x})$$

Now, evaluate the induced likelihood at the point $\\tau^* = g(\\hat{\\boldsymbol{\\theta}})$:

$$L_g(g(\\hat{\\boldsymbol{\\theta}}); \\mathbf{x}) = \\sup_{\\boldsymbol{\\theta} \\in \\Theta : g(\\boldsymbol{\\theta}) = g(\\hat{\\boldsymbol{\\theta}})} L(\\boldsymbol{\\theta}; \\mathbf{x})$$

Because $\\hat{\\boldsymbol{\\theta}}$ itself belongs to the set $\\{\\boldsymbol{\\theta} \\in \\Theta : g(\\boldsymbol{\\theta}) = g(\\hat{\\boldsymbol{\\theta}})\\}$, the supremum over that set is at least as large as $L(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x})$:

$$L_g(g(\\hat{\\boldsymbol{\\theta}}); \\mathbf{x}) \\ge L(\\hat{\\boldsymbol{\\theta}}; \\mathbf{x})$$

Combining the two inequalities:

$$L_g(g(\\hat{\\boldsymbol{\\theta}}); \\mathbf{x}) = \\sup_{\\tau \\in \\Omega} L_g(\\tau; \\mathbf{x})$$

Therefore, $\\hat{\\tau} = g(\\hat{\\boldsymbol{\\theta}})$ achieves the global maximum of the induced likelihood function.
This completes the proof.

#### Significance of Invariance:
Invariance gives maximum likelihood estimators immense practical flexibility:
- If $\\hat{\\sigma}^2$ is the MLE of variance, then the MLE of standard deviation is immediately $\\hat{\\sigma} = \\sqrt{\\hat{\\sigma}^2}$.
- If $\\hat{p}$ is the MLE of a binomial success probability, the MLE of the odds ratio $\\frac{p}{1-p}$ is simply $\\frac{\\hat{p}}{1 - \\hat{p}}$.
- If $\\hat{\\lambda}$ is the MLE of a Poisson rate, the MLE of the zero-event probability $e^{-\\lambda}$ is $e^{-\\hat{\\lambda}}$.
Recall from Unit 1 that unbiased estimators **never** possess this property: $g(T_{\\text{UMVUE}})$ is almost never unbiased for $g(\\theta)$. Maximum likelihood estimators liberate the practitioner from re-deriving estimators under every non-linear reparameterization.

## 4.7 Profile Likelihood and Concentrated Likelihood for Nuisance Parameters

In multiparameter models, the parameter vector often partitions into structural parameters of interest $\\boldsymbol{\\psi}$ and nuisance parameters $\\boldsymbol{\\lambda}$:

$$\\boldsymbol{\\theta} = (\\boldsymbol{\\psi}^T, \\boldsymbol{\\lambda}^T)^T$$

We wish to perform inference on $\\boldsymbol{\\psi}$ without being impeded by uncertainty in $\\boldsymbol{\\lambda}$.

### Definition of the Profile Likelihood
For each fixed candidate value of $\\boldsymbol{\\psi}$, define the constrained maximum likelihood estimate of the nuisance parameter:

$$\\hat{\\boldsymbol{\\lambda}}(\\boldsymbol{\\psi}) = \\arg\\max_{\\boldsymbol{\\lambda}} \\ell(\\boldsymbol{\\psi}, \\boldsymbol{\\lambda}; \\mathbf{x})$$

The **Profile Log-Likelihood Function** for $\\boldsymbol{\\psi}$ is defined as:

$$\\ell_p(\\boldsymbol{\\psi}; \\mathbf{x}) = \\ell(\\boldsymbol{\\psi}, \\hat{\\boldsymbol{\\lambda}}(\\boldsymbol{\\psi}); \\mathbf{x})$$

The overall global MLE of the structural parameter $\\hat{\\boldsymbol{\\psi}}$ maximizes the profile likelihood:

$$\\hat{\\boldsymbol{\\psi}} = \\arg\\max_{\\boldsymbol{\\psi}} \\ell_p(\\boldsymbol{\\psi}; \\mathbf{x})$$

### Curvature of the Profile Likelihood and the Schur Complement
A celebrated theorem in likelihood inference connects the curvature of the profile likelihood directly to the full Fisher Information matrix.
Let $\\mathcal{H}(\\boldsymbol{\\theta})$ be the full Hessian matrix partitioned as:

$$\\mathcal{H} = \\begin{pmatrix} \\mathcal{H}_{\\psi\\psi} & \\mathcal{H}_{\\psi\\lambda} \\\\ \\mathcal{H}_{\\lambda\\psi} & \\mathcal{H}_{\\lambda\\lambda} \\end{pmatrix}$$

By the multivariable chain rule, the second derivative of the profile log-likelihood evaluated at the MLE is:

$$\\nabla_{\\boldsymbol{\\psi}}^2 \\ell_p(\\hat{\\boldsymbol{\\psi}}) = \\mathcal{H}_{\\psi\\psi} - \\mathcal{H}_{\\psi\\lambda} \\mathcal{H}_{\\lambda\\lambda}^{-1} \\mathcal{H}_{\\lambda\\psi}$$

This is the **Schur complement** of $\\mathcal{H}_{\\lambda\\lambda}$ in the full Hessian matrix!
Inverting this expression reveals that:

$$\\left( -\\nabla_{\\boldsymbol{\\psi}}^2 \\ell_p(\\hat{\\boldsymbol{\\psi}}) \\right)^{-1} = [J(\\hat{\\boldsymbol{\\theta}})^{-1}]_{\\psi\\psi}$$

The curvature of the profile log-likelihood automatically incorporates the exact variance inflation caused by estimating the unknown nuisance parameters! This enables the construction of valid profile likelihood confidence intervals:

$$\\{\\boldsymbol{\\psi} : 2[\\ell_p(\\hat{\\boldsymbol{\\psi}}) - \\ell_p(\\boldsymbol{\\psi})] \\le \\chi_{k, 1-\\alpha}^2\\}$$

## 4.8 Numerical Optimization: Newton-Raphson, Fisher's Method of Scoring, and Quasi-Newton Algorithms

In most non-trivial statistical models, the likelihood equations $\\nabla \\ell(\\boldsymbol{\\theta}) = \\mathbf{0}$ cannot be solved analytically. Numerical optimization algorithms are required to compute the MLE.

### 1. The Newton–Raphson Algorithm
The Newton–Raphson method approximates the log-likelihood locally around the current iterate $\\boldsymbol{\\theta}^{(t)}$ via a second-order Taylor series expansion:

$$\\ell(\\boldsymbol{\\theta}) \\approx \\ell(\\boldsymbol{\\theta}^{(t)}) + \\mathbf{S}(\\boldsymbol{\\theta}^{(t)})^T (\\boldsymbol{\\theta} - \\boldsymbol{\\theta}^{(t)}) + \\frac{1}{2} (\\boldsymbol{\\theta} - \\boldsymbol{\\theta}^{(t)})^T \\mathcal{H}(\\boldsymbol{\\theta}^{(t)}) (\\boldsymbol{\\theta} - \\boldsymbol{\\theta}^{(t)})$$

Differentiating with respect to $\\boldsymbol{\\theta}$ and setting the gradient to zero yields the celebrated iterative update rule:

$$\\boldsymbol{\\theta}^{(t+1)} = \\boldsymbol{\\theta}^{(t)} - [\\mathcal{H}(\\boldsymbol{\\theta}^{(t)})]^{-1} \\mathbf{S}(\\boldsymbol{\\theta}^{(t)}) = \\boldsymbol{\\theta}^{(t)} + [J(\\boldsymbol{\\theta}^{(t)})]^{-1} \\mathbf{S}(\\boldsymbol{\\theta}^{(t)})$$

where $J(\\boldsymbol{\\theta}^{(t)}) = -\\mathcal{H}(\\boldsymbol{\\theta}^{(t)})$ is the observed information matrix.
Near the global maximum, Newton–Raphson exhibits quadratic convergence (doubling the number of correct digits at each iteration). However, if the starting point $\\boldsymbol{\\theta}^{(0)}$ is far from the peak, the observed Hessian may not be negative-definite, causing the algorithm to diverge.

### 2. Fisher's Method of Scoring
Ronald Fisher proposed replacing the observed information matrix $J(\\boldsymbol{\\theta}^{(t)})$ with the **Expected Fisher Information Matrix** $\\mathbf{I}(\\boldsymbol{\\theta}^{(t)}) = \\mathbb{E}[J(\\boldsymbol{\\theta}^{(t)})]$:

$$\\boldsymbol{\\theta}^{(t+1)} = \\boldsymbol{\\theta}^{(t)} + [\\mathbf{I}(\\boldsymbol{\\theta}^{(t)})]^{-1} \\mathbf{S}(\\boldsymbol{\\theta}^{(t)})$$

Fisher scoring has significant advantages:
- Because $\\mathbf{I}(\\boldsymbol{\\theta})$ is the covariance matrix of the score vector, it is guaranteed to be positive semi-definite everywhere in $\\Theta$, ensuring that each step moves in an ascent direction.
- In generalized linear models (GLMs) with canonical link functions, the observed and expected information matrices coincide ($J \\equiv \\mathbf{I}$), making Fisher scoring and Newton–Raphson identical (known as Iteratively Reweighted Least Squares / IRLS).

## 4.9 The Expectation-Maximization (EM) Algorithm for Latent Variables and Incomplete Data

When data contain missing values, latent cluster assignments, or censored observations, the marginal likelihood function is an intractable sum or integral over all possible hidden configurations. In 1977, A. P. Dempster, N. M. Laird, and D. B. Rubin formalized the **Expectation–Maximization (EM) algorithm** as a general iterative framework for maximum likelihood estimation in incomplete-data problems.

### Complete Data vs Observed Data
Let $\\mathbf{Y}$ denote the observed data, and let $\\mathbf{Z}$ denote the unobserved latent variables or missing data. The combination $\\mathbf{X} = (\\mathbf{Y}, \\mathbf{Z})$ is the **complete data**.
The observed data likelihood is the marginal integral:

$$L(\\boldsymbol{\\theta}; \\mathbf{Y}) = \\int_{\\mathcal{Z}} f(\\mathbf{Y}, \\mathbf{z}; \\boldsymbol{\\theta}) \\, d\\mathbf{z}$$

Evaluating this integral directly is often computationally impossible.
The EM algorithm avoids integration by operating iteratively on the complete-data log-likelihood $\\ln f(\\mathbf{Y}, \\mathbf{Z}; \\boldsymbol{\\theta})$ through two alternating steps:

### The Two Steps of the EM Algorithm:
1. **Expectation Step (E-step)**:
   Given the current parameter iterate $\\boldsymbol{\\theta}^{(t)}$, compute the conditional expectation of the complete-data log-likelihood with respect to the latent variables $\\mathbf{Z}$, conditioned on the observed data $\\mathbf{Y}$ and current parameters $\\boldsymbol{\\theta}^{(t)}$:
   $$Q(\\boldsymbol{\\theta} \\mid \\boldsymbol{\\theta}^{(t)}) = \\mathbb{E}_{\\mathbf{Z} \\mid \\mathbf{Y}, \\boldsymbol{\\theta}^{(t)}} \\left[ \\ln f(\\mathbf{Y}, \\mathbf{Z}; \\boldsymbol{\\theta}) \\right] = \\int_{\\mathcal{Z}} [\\ln f(\\mathbf{Y}, \\mathbf{z}; \\boldsymbol{\\theta})] \\, f(\\mathbf{z} \\mid \\mathbf{Y}; \\boldsymbol{\\theta}^{(t)}) \\, d\\mathbf{z}$$
2. **Maximization Step (M-step)**:
   Update the parameter estimate by globally maximizing the surrogate function $Q(\\boldsymbol{\\theta} \\mid \\boldsymbol{\\theta}^{(t)})$ over $\\Theta$:
   $$\\boldsymbol{\\theta}^{(t+1)} = \\arg\\max_{\\boldsymbol{\\theta} \\in \\Theta} Q(\\boldsymbol{\\theta} \\mid \\boldsymbol{\\theta}^{(t)})$$

### Monotonicity and Convergence (Dempster–Laird–Rubin Theorem)
By Jensen's Inequality, every EM iteration is guaranteed to never decrease the observed log-likelihood:

$$\\ell(\\boldsymbol{\\theta}^{(t+1)}; \\mathbf{Y}) \\ge \\ell(\\boldsymbol{\\theta}^{(t)}; \\mathbf{Y})$$

The observed likelihood sequence $\\{\\ell(\\boldsymbol{\\theta}^{(t)})\\}$ converges monotonically to a local maximum or stationary point of the likelihood surface, providing exceptional numerical stability.

## 4.10 Robust Estimation: M-Estimators, Huber Loss, and Influence Functions

While Maximum Likelihood Estimators are asymptotically efficient under a perfectly specified model, they can be catastrophically sensitive to minor model misspecifications and heavy-tailed contamination (outliers).

To overcome this brittleness, Peter J. Huber (1964) developed the theory of **M-Estimators** (generalized maximum likelihood estimators).
Instead of minimizing $-\\sum \\ln f(x_i; \\theta)$, an M-estimator minimizes a general objective function $\\rho$:

$$\\hat{\\theta}_M = \\arg\\min_\\theta \\sum_{i=1}^n \\rho(X_i - \\theta)$$

Differentiating with respect to $\\theta$ yields the estimating equation:

$$\\sum_{i=1}^n \\psi(X_i - \\hat{\\theta}_M) = 0$$

where $\\psi(u) = \\rho'(u)$ is the score function.

### The Influence Function and Huber's Robust Criterion
Frank Hampel introduced the **Influence Function** $\\text{IF}(x; T, F)$, which measures the asymptotic bias induced in an estimator $T$ by an infinitesimal point contamination at location $x$:

$$\\text{IF}(x; T, F) = \\lim_{\\epsilon \\to 0^+} \\frac{T((1 - \\epsilon)F + \\epsilon \\delta_x) - T(F)}{\\epsilon}$$

For an M-estimator, the influence function is directly proportional to $\\psi(x)$:

$$\\text{IF}(x; \\hat{\\theta}_M, F) = \\frac{\\psi(x)}{\\mathbb{E}[\\psi'(X)]}$$

If $\\psi(x)$ is unbounded (as in classical sample mean where $\\rho(u) = u^2 / 2$ and $\\psi(u) = u$), a single catastrophic outlier at $x = \\infty$ can drag the estimate to infinity! The breakdown point of the sample mean is $0\\%$.
To bound the influence function and protect against outliers, Huber introduced the **Huber Loss Function**:

$$\\rho_k(u) = \\begin{cases} \\frac{1}{2} u^2 & \\text{if } |u| \\le k \\\\ k |u| - \\frac{1}{2} k^2 & \\text{if } |u| > k \\end{cases} \\implies \\psi_k(u) = \\begin{cases} u & \\text{if } |u| \\le k \\\\ k \\, \\text{sgn}(u) & \\text{if } |u| > k \\end{cases}$$

The Huber $\\psi$-function acts like the mean for small deviations ($|u| \\le k$) and like the median for large outliers ($|u| > k$), producing estimators that achieve $95\\%$ Gaussian efficiency while remaining completely bounded and robust against severe data contamination.

---

## Fully worked question 1: Method of Moments vs MLE for the Two-Parameter Beta Distribution with Asymptotic Relative Efficiency

### Question
An aerospace materials engineer measures the porosity fraction $X \\in (0, 1)$ of thermal-barrier ceramic coatings sprayed onto jet engine turbine blades. Porosity measurements follow a Beta distribution with shape parameters $\\alpha > 0$ and $\\beta > 0$:

$$f(x; \\alpha, \\beta) = \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha) \\Gamma(\\beta)} x^{\\alpha - 1} (1 - x)^{\\beta - 1}, \\quad 0 < x < 1$$

An independent sample $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ of porosity measurements is recorded.

1. Derive the theoretical population mean $\\mu = \\alpha_1$ and variance $\\sigma^2 = \\mu_2$ in terms of $\\alpha$ and $\\beta$.
2. Derive the closed-form Method of Moments estimators $\\tilde{\\alpha}$ and $\\tilde{\\beta}$ as explicit functions of the sample mean $\\bar{X}$ and sample variance $S_n^2 = \\frac{1}{n} \\sum_{i=1}^n (X_i - \\bar{X})^2$. Under what sample condition do the MOM estimators produce inadmissible (negative) values?
3. Write down the log-likelihood function $\\ell(\\alpha, \\beta; \\mathbf{X})$ and derive the system of simultaneous likelihood equations for the Maximum Likelihood Estimators $(\\hat{\\alpha}, \\hat{\\beta})$ in terms of the digamma function $\\psi(z) = \\frac{d}{dz} \\ln \\Gamma(z)$.
4. In a sample of $n = 5$ turbine blade coatings, the observed porosities are:
   $$\\mathbf{x} = (0.12, 0.18, 0.22, 0.28, 0.30)$$
   Compute the sample mean $\\bar{x}$ and sample variance $s_n^2$, evaluate the Method of Moments estimates $(\\tilde{\\alpha}, \\tilde{\\beta})$, and formulate the initial Newton–Raphson iteration step for the Maximum Likelihood Estimator.

### Solution, step 1: Population moments of the Beta distribution
Recall the definition of the Beta integral:

$$\\int_0^1 x^{u - 1} (1 - x)^{v - 1} \\, dx = \\frac{\\Gamma(u) \\Gamma(v)}{\\Gamma(u + v)}$$

The $r$-th raw moment is:

$$\\mathbb{E}[X^r] = \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha) \\Gamma(\\beta)} \\int_0^1 x^{\\alpha + r - 1} (1 - x)^{\\beta - 1} \\, dx = \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha) \\Gamma(\\beta)} \\frac{\\Gamma(\\alpha + r) \\Gamma(\\beta)}{\\Gamma(\\alpha + \\beta + r)} = \\frac{\\Gamma(\\alpha + \\beta) \\Gamma(\\alpha + r)}{\\Gamma(\\alpha) \\Gamma(\\alpha + \\beta + r)}$$

For $r = 1$:

$$\\mu = \\mathbb{E}[X] = \\frac{\\alpha}{\\alpha + \\beta}$$

For $r = 2$:

$$\\mathbb{E}[X^2] = \\frac{\\alpha(\\alpha + 1)}{(\\alpha + \\beta)(\\alpha + \\beta + 1)}$$

Compute the population variance:

$$\\sigma^2 = \\mathbb{E}[X^2] - \\mu^2 = \\frac{\\alpha(\\alpha + 1)}{(\\alpha + \\beta)(\\alpha + \\beta + 1)} - \\frac{\\alpha^2}{(\\alpha + \\beta)^2} = \\frac{\\alpha \\beta}{(\\alpha + \\beta)^2 (\\alpha + \\beta + 1)}$$

### Solution, step 2: Method of Moments derivation
Let $\\bar{X} = m_1$ and $S_n^2 = c_2$ be the sample mean and sample variance.
Equate theoretical and sample moments:

$$\\mu = \\frac{\\alpha}{\\alpha + \\beta} = \\bar{X}$$

$$\\sigma^2 = \\frac{\\alpha \\beta}{(\\alpha + \\beta)^2 (\\alpha + \\beta + 1)} = S_n^2$$

Notice that $\\frac{\\alpha}{\\alpha + \\beta} = \\bar{X}$ implies $\\frac{\\beta}{\\alpha + \\beta} = 1 - \\bar{X}$.
Therefore:

$$\\frac{\\alpha \\beta}{(\\alpha + \\beta)^2} = \\bar{X} (1 - \\bar{X})$$

Substitute this into the variance equation:

$$S_n^2 = \\frac{\\bar{X}(1 - \\bar{X})}{\\alpha + \\beta + 1}$$

Solving for the sum $\\alpha + \\beta$:

$$\\alpha + \\beta + 1 = \\frac{\\bar{X}(1 - \\bar{X})}{S_n^2} \\implies \\alpha + \\beta = \\frac{\\bar{X}(1 - \\bar{X})}{S_n^2} - 1 = \\frac{\\bar{X}(1 - \\bar{X}) - S_n^2}{S_n^2}$$

Now multiply by $\\bar{X} = \\frac{\\alpha}{\\alpha + \\beta}$ to solve for $\\alpha$:

$$\\tilde{\\alpha} = \\bar{X} \\left( \\frac{\\bar{X}(1 - \\bar{X}) - S_n^2}{S_n^2} \\right) = \\bar{X} \\left( \\frac{\\bar{X}(1 - \\bar{X})}{S_n^2} - 1 \\right)$$

Similarly, multiply by $1 - \\bar{X} = \\frac{\\beta}{\\alpha + \\beta}$ to solve for $\\beta$:

$$\\tilde{\\beta} = (1 - \\bar{X}) \\left( \\frac{\\bar{X}(1 - \\bar{X}) - S_n^2}{S_n^2} \\right) = (1 - \\bar{X}) \\left( \\frac{\\bar{X}(1 - \\bar{X})}{S_n^2} - 1 \\right)$$

**Condition for Inadmissibility:**
Because parameters $\\alpha, \\beta$ must be strictly positive, the term in parentheses must be positive:

$$\\frac{\\bar{X}(1 - \\bar{X})}{S_n^2} - 1 > 0 \\implies S_n^2 < \\bar{X}(1 - \\bar{X})$$

If a sample realization has high dispersion such that $S_n^2 \\ge \\bar{X}(1 - \\bar{X})$, the Method of Moments produces negative estimates $\\tilde{\\alpha} \\le 0$ and $\\tilde{\\beta} \\le 0$, which are mathematically inadmissible!

### Solution, step 3: Likelihood equations for the MLE
The joint likelihood for an i.i.d. sample of size $n$ from $\\text{Beta}(\\alpha, \\beta)$ is:

$$L(\\alpha, \\beta; \\mathbf{X}) = \\prod_{i=1}^n \\left[ \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha) \\Gamma(\\beta)} X_i^{\\alpha - 1} (1 - X_i)^{\\beta - 1} \\right] = \\left[ \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha) \\Gamma(\\beta)} \\right]^n \\left( \\prod_{i=1}^n X_i \\right)^{\\alpha - 1} \\left( \\prod_{i=1}^n (1 - X_i) \\right)^{\\beta - 1}$$

Taking the natural logarithm:

$$\\ell(\\alpha, \\beta; \\mathbf{X}) = n \\ln \\Gamma(\\alpha + \\beta) - n \\ln \\Gamma(\\alpha) - n \\ln \\Gamma(\\beta) + (\\alpha - 1) \\sum_{i=1}^n \\ln(X_i) + (\\beta - 1) \\sum_{i=1}^n \\ln(1 - X_i)$$

Recall the digamma function $\\psi(z) = \\frac{d}{dz} \\ln \\Gamma(z) = \\frac{\\Gamma'(z)}{\\Gamma(z)}$.
Differentiating with respect to $\\alpha$ and $\\beta$:

$$\\frac{\\partial \\ell}{\\partial \\alpha} = n \\psi(\\alpha + \\beta) - n \\psi(\\alpha) + \\sum_{i=1}^n \\ln(X_i) = 0$$

$$\\frac{\\partial \\ell}{\\partial \\beta} = n \\psi(\\alpha + \\beta) - n \\psi(\\beta) + \\sum_{i=1}^n \\ln(1 - X_i) = 0$$

Dividing by $n$:

$$\\begin{cases} \\psi(\\alpha) - \\psi(\\alpha + \\beta) = \\frac{1}{n} \\sum_{i=1}^n \\ln(X_i) \\\\ \\psi(\\beta) - \\psi(\\alpha + \\beta) = \\frac{1}{n} \\sum_{i=1}^n \\ln(1 - X_i) \\end{cases}$$

This non-linear system of transcendental equations cannot be solved in closed form; it requires numerical root-finding using the trigamma function $\\psi'(z)$ in a Newton–Raphson solver.

### Solution, step 4: Numerical calculations on the sample
Given data: $\\mathbf{x} = (0.12, 0.18, 0.22, 0.28, 0.30)$ with $n = 5$.
1. Compute the sample mean:
   $$\\bar{x} = \\frac{0.12 + 0.18 + 0.22 + 0.28 + 0.30}{5} = \\frac{1.10}{5} = 0.22$$
2. Compute deviations and squared deviations from the mean:
   - $x_1 - \\bar{x} = 0.12 - 0.22 = -0.10 \\implies (-0.10)^2 = 0.0100$
   - $x_2 - \\bar{x} = 0.18 - 0.22 = -0.04 \\implies (-0.04)^2 = 0.0016$
   - $x_3 - \\bar{x} = 0.22 - 0.22 = 0.00 \\implies (0.00)^2 = 0.0000$
   - $x_4 - \\bar{x} = 0.28 - 0.22 = +0.06 \\implies (0.06)^2 = 0.0036$
   - $x_5 - \\bar{x} = 0.30 - 0.22 = +0.08 \\implies (0.08)^2 = 0.0064$
   Sum of squared deviations: $\\sum (x_i - \\bar{x})^2 = 0.0100 + 0.0016 + 0.0000 + 0.0036 + 0.0064 = 0.0216$.
   The sample variance is:
   $$s_n^2 = \\frac{0.0216}{5} = 0.00432$$
3. Check admissibility:
   $$\\bar{x}(1 - \\bar{x}) = 0.22 \\times 0.78 = 0.1716$$
   Since $s_n^2 = 0.00432 < 0.1716$, the condition holds.
4. Compute the scaling factor:
   $$\\frac{\\bar{x}(1 - \\bar{x})}{s_n^2} - 1 = \\frac{0.1716}{0.00432} - 1 = 39.7222 - 1 = 38.7222$$
5. Method of Moments estimates:
   $$\\tilde{\\alpha} = \\bar{x} \\times 38.7222 = 0.22 \\times 38.7222 \\approx 8.5189$$
   $$\\tilde{\\beta} = (1 - \\bar{x}) \\times 38.7222 = 0.78 \\times 38.7222 \\approx 30.2033$$
These MOM estimates $(\\tilde{\\alpha}, \\tilde{\\beta}) = (8.52, 30.20)$ provide an outstanding, highly stable initial starting vector $(\\alpha^{(0)}, \\beta^{(0)})$ for the Newton–Raphson likelihood optimizer.

---

## Fully worked question 2: Non-Regular MLE and Joint Distribution of Extreme Order Statistics in Shifted Exponential Models

### Question
An optical networking hardware manufacturer subjects high-speed semiconductor lasers to continuous operational burn-in testing. Laser degradation failure times $X$ follow a two-parameter shifted (two-parameter) Exponential distribution with location threshold $\\theta \\in \\mathbb{R}$ and scale parameter $\\sigma > 0$:

$$f(x; \\theta, \\sigma) = \\frac{1}{\\sigma} \\exp\\left( -\\frac{x - \\theta}{\\sigma} \\right) \\mathbf{1}_{\\{x \\ge \\theta\\}}$$

Here, $\\theta$ represents the guaranteed minimum lifetime before degradation begins, and $\\sigma$ represents the mean time between failures after burn-in. An i.i.d. sample of laser failure times $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ is recorded ($n \\ge 2$).

1. Formulate the joint likelihood function $L(\\theta, \\sigma; \\mathbf{X})$ and demonstrate that it is a non-regular likelihood with support boundary depending on $\\theta$.
2. Derive the joint Maximum Likelihood Estimators $(\\hat{\\theta}_{\\text{MLE}}, \\hat{\\sigma}_{\\text{MLE}})$.
3. Determine the exact finite-sample sampling distribution of $\\hat{\\theta}_{\\text{MLE}}$ and $\\hat{\\sigma}_{\\text{MLE}}$. Compute the exact bias and variance of both estimators.
4. Construct unbiased adjustments for both estimators to obtain the UMVUEs of $\\theta$ and $\\sigma$.

### Solution, step 1: Joint likelihood and non-regular structure
The joint likelihood of the sample is:

$$L(\\theta, \\sigma; \\mathbf{X}) = \\prod_{i=1}^n \\left[ \\frac{1}{\\sigma} e^{-(X_i - \\theta)/\\sigma} \\mathbf{1}_{\\{X_i \\ge \\theta\\}} \\right] = \\frac{1}{\\sigma^n} \\exp\\left( -\\frac{1}{\\sigma} \\sum_{i=1}^n (X_i - \\theta) \\right) \\prod_{i=1}^n \\mathbf{1}_{\\{X_i \\ge \\theta\\}}$$

The product of indicator functions is non-zero if and only if every single $X_i \\ge \\theta$, which holds if and only if the minimum order statistic satisfies $X_{(1)} \\ge \\theta$:

$$L(\\theta, \\sigma; \\mathbf{X}) = \\frac{1}{\\sigma^n} \\exp\\left( -\\frac{1}{\\sigma} \\sum_{i=1}^n X_i + \\frac{n\\theta}{\\sigma} \\right) \\mathbf{1}_{\\{X_{(1)} \\ge \\theta\\}}$$

Taking the natural logarithm on the feasible domain $\\theta \\le X_{(1)}$:

$$\\ell(\\theta, \\sigma; \\mathbf{X}) = -n \\ln(\\sigma) - \\frac{1}{\\sigma} \\sum_{i=1}^n X_i + \\frac{n\\theta}{\\sigma}$$

Notice that for any fixed $\\sigma > 0$:

$$\\frac{\\partial \\ell}{\\partial \\theta} = \\frac{n}{\\sigma} > 0$$

The log-likelihood is a **strictly increasing function** of $\\theta$ everywhere on the interval $(-\\infty, X_{(1)}]$!
Setting $\\frac{\\partial \\ell}{\\partial \\theta} = 0$ yields no solution. To maximize an increasing function over the domain $\\theta \\le X_{(1)}$, we must push $\\theta$ to the largest possible value on the boundary.

### Solution, step 2: Maximum Likelihood Estimators
The maximum possible value of $\\theta$ is $X_{(1)}$.
Therefore, the Maximum Likelihood Estimator of $\\theta$ is:

$$\\hat{\\theta}_{\\text{MLE}} = X_{(1)} = \\min(X_1, X_2, \\dots, X_n)$$

Now, substitute $\\hat{\\theta} = X_{(1)}$ into the log-likelihood to obtain the profile log-likelihood for $\\sigma$:

$$\\ell(\\hat{\\theta}, \\sigma; \\mathbf{X}) = -n \\ln(\\sigma) - \\frac{1}{\\sigma} \\sum_{i=1}^n (X_i - X_{(1)})$$

Differentiating with respect to $\\sigma$ and setting to zero:

$$\\frac{\\partial \\ell}{\\partial \\sigma} = -\\frac{n}{\\sigma} + \\frac{1}{\\sigma^2} \\sum_{i=1}^n (X_i - X_{(1)}) = 0$$

Solving for $\\sigma$:

$$\\hat{\\sigma}_{\\text{MLE}} = \\frac{1}{n} \\sum_{i=1}^n (X_i - X_{(1)}) = \\bar{X} - X_{(1)}$$

### Solution, step 3: Exact finite-sample distributions, bias, and variance
Let $Y_i = \\frac{X_i - \\theta}{\\sigma}$. Then $Y_1, \\dots, Y_n$ are i.i.d. standard exponential variables $\\text{Exp}(1)$ with density $e^{-y}$ for $y \\ge 0$.
The minimum order statistic $Y_{(1)} = \\min(Y_1, \\dots, Y_n)$ has distribution:

$$\\mathbb{P}(Y_{(1)} > y) = [\\mathbb{P}(Y_1 > y)]^n = [e^{-y}]^n = e^{-ny}$$

Thus $Y_{(1)} \\sim \\text{Exp}(n)$, which means:

$$X_{(1)} = \\theta + \\sigma Y_{(1)}$$

has expectation and variance:

$$\\mathbb{E}[X_{(1)}] = \\theta + \\sigma \\mathbb{E}[Y_{(1)}] = \\theta + \\frac{\\sigma}{n}$$

$$\\text{Var}(X_{(1)}) = \\sigma^2 \\text{Var}(Y_{(1)}) = \\frac{\\sigma^2}{n^2}$$

The bias of $\\hat{\\theta}_{\\text{MLE}}$ is:

$$\\text{Bias}(\\hat{\\theta}_{\\text{MLE}}) = \\mathbb{E}[X_{(1)}] - \\theta = +\\frac{\\sigma}{n}$$

Notice that the variance scales as $\\mathcal{O}(1/n^2)$, confirming super-efficiency!

Now consider the scale estimator $\\hat{\\sigma}_{\\text{MLE}} = \\frac{1}{n} \\sum_{i=1}^n (X_i - X_{(1)})$.
By Sukhatme's theorem on exponential spacings, the normalized spacings $D_k = (n - k + 1)(X_{(k)} - X_{(k-1)})$ are mutually independent and identically distributed as $\\text{Exp}(1/\\sigma)$.
The total sum of deviations decomposes as:

$$\\sum_{i=1}^n (X_i - X_{(1)}) = \\sum_{k=2}^n (n - k + 1)(X_{(k)} - X_{(k-1)}) = \\sum_{j=1}^{n-1} W_j$$

where $W_j \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Exp}(1/\\sigma)$.
The sum of $n - 1$ independent Exponential variables follows a Gamma distribution:

$$\\sum_{i=1}^n (X_i - X_{(1)}) \\sim \\text{Gamma}(n - 1, \\sigma)$$

Therefore:

$$\\mathbb{E}[\\hat{\\sigma}_{\\text{MLE}}] = \\frac{1}{n} \\mathbb{E}[\\text{Gamma}(n - 1, \\sigma)] = \\frac{(n - 1)\\sigma}{n}$$

$$\\text{Var}(\\hat{\\sigma}_{\\text{MLE}}) = \\frac{1}{n^2} \\text{Var}(\\text{Gamma}(n - 1, \\sigma)) = \\frac{(n - 1)\\sigma^2}{n^2}$$

The bias of $\\hat{\\sigma}_{\\text{MLE}}$ is $-\\frac{\\sigma}{n}$.

### Solution, step 4: Unbiased UMVUE adjustments
Because $(X_{(1)}, \\sum X_i)$ is a complete minimal sufficient statistic, unbiasing the MLEs immediately yields the UMVUEs by the Lehmann–Scheffé Theorem:
1. For $\\sigma$:
   Multiply $\\hat{\\sigma}_{\\text{MLE}}$ by $\\frac{n}{n - 1}$:
   $$S^* = \\frac{1}{n - 1} \\sum_{i=1}^n (X_i - X_{(1)}) = \\frac{n}{n - 1} (\\bar{X} - X_{(1)})$$
   $$\\mathbb{E}[S^*] = \\sigma, \\quad \\text{Var}(S^*) = \\frac{\\sigma^2}{n - 1}$$
   $S^*$ is the unique UMVUE of $\\sigma$.
2. For $\\theta$:
   Since $\\mathbb{E}[X_{(1)}] = \\theta + \\frac{\\sigma}{n}$, subtract $\\frac{S^*}{n}$:
   $$T^* = X_{(1)} - \\frac{S^*}{n} = X_{(1)} - \\frac{\\sum_{i=1}^n (X_i - X_{(1)})}{n(n - 1)}$$
   Taking expectation:
   $$\\mathbb{E}[T^*] = \\mathbb{E}[X_{(1)}] - \\frac{\\mathbb{E}[S^*]}{n} = \\left(\\theta + \\frac{\\sigma}{n}\\right) - \\frac{\\sigma}{n} = \\theta$$
   Because $T^*$ is an unbiased function of the complete sufficient statistic, $T^*$ is the **unique UMVUE** of $\\theta$!
   By Basu's Theorem, $X_{(1)}$ is independent of $S^*$. Therefore:
   $$\\text{Var}(T^*) = \\text{Var}(X_{(1)}) + \\frac{1}{n^2} \\text{Var}(S^*) = \\frac{\\sigma^2}{n^2} + \\frac{\\sigma^2}{n^2(n - 1)} = \\frac{\\sigma^2}{n^2} \\left( 1 + \\frac{1}{n - 1} \\right) = \\frac{\\sigma^2}{n(n - 1)}$$

---

## Fully worked question 3: EM Algorithm Derivation and Convergence Analysis for Gaussian Mixture Models

### Question
A financial risk modeling group analyzes daily logarithmic returns $Y$ of a diversified index during periods of market stress. The empirical return distribution exhibits heavy tails and regime switching, modeled as a two-component Gaussian mixture:

$$Y \\sim \\pi \\mathcal{N}(\\mu_1, \\sigma_1^2) + (1 - \\pi) \\mathcal{N}(\\mu_2, \\sigma_2^2)$$

where $\\pi \\in (0, 1)$ is the probability of the standard market regime, and $1 - \\pi$ is the probability of the high-volatility crisis regime.
An independent sample of daily returns $\\mathbf{Y} = (Y_1, Y_2, \\dots, Y_n)$ is observed.

1. Formulate the latent variable framework by defining binary regime indicator variables $Z_i \\in \\{0, 1\\}$. Write down the complete-data log-likelihood $\\ell_c(\\boldsymbol{\\theta}; \\mathbf{Y}, \\mathbf{Z})$.
2. Derive the analytical expressions for the **Expectation Step (E-step)**, calculating the posterior responsibilities $\\gamma_{ik} = \\mathbb{E}[Z_{ik} \\mid Y_i, \\boldsymbol{\\theta}^{(t)}]$ for each regime $k \\in \\{1, 2\\}$.
3. Derive the analytical formulas for the **Maximization Step (M-step)**, proving that the parameter updates $(\\pi^{(t+1)}, \\mu_k^{(t+1)}, (\\sigma_k^2)^{(t+1)})$ take the form of responsibility-weighted sample moments.
4. Explain how the EM algorithm avoids singularity degeneracies when a single observation collapses onto a component variance ($\\sigma_k^2 \\to 0$).

### Solution, step 1: Complete-data log-likelihood
For each observation $Y_i$, introduce an unobserved latent binary indicator vector $\\mathbf{Z}_i = (Z_{i1}, Z_{i2})^T$, where:
- $Z_{i1} = 1$ if observation $i$ was generated by Component 1 (regime 1), and $0$ otherwise.
- $Z_{i2} = 1$ if observation $i$ was generated by Component 2 (regime 2), and $0$ otherwise.
Note that $Z_{i1} + Z_{i2} = 1$, with prior probabilities $\\mathbb{P}(Z_{i1} = 1) = \\pi$ and $\\mathbb{P}(Z_{i2} = 1) = 1 - \\pi$.

The conditional density of $Y_i$ given $\\mathbf{Z}_i$ is:

$$f(y_i \\mid \\mathbf{Z}_i; \\boldsymbol{\\theta}) = [\\phi(y_i; \\mu_1, \\sigma_1^2)]^{Z_{i1}} [\\phi(y_i; \\mu_2, \\sigma_2^2)]^{Z_{i2}}$$

where $\\phi(y; \\mu, \\sigma^2) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} \\exp\\left( -\\frac{(y - \\mu)^2}{2\\sigma^2} \\right)$.
The joint probability of $(Y_i, \\mathbf{Z}_i)$ is:

$$f(y_i, \\mathbf{Z}_i; \\boldsymbol{\\theta}) = [\\pi \\phi(y_i; \\mu_1, \\sigma_1^2)]^{Z_{i1}} [(1 - \\pi) \\phi(y_i; \\mu_2, \\sigma_2^2)]^{Z_{i2}}$$

For an i.i.d. sample of size $n$, the complete-data log-likelihood is:

$$\\ell_c(\\boldsymbol{\\theta}; \\mathbf{Y}, \\mathbf{Z}) = \\sum_{i=1}^n \\left[ Z_{i1} \\left( \\ln(\\pi) - \\frac{1}{2} \\ln(2\\pi\\sigma_1^2) - \\frac{(Y_i - \\mu_1)^2}{2\\sigma_1^2} \\right) + Z_{i2} \\left( \\ln(1 - \\pi) - \\frac{1}{2} \\ln(2\\pi\\sigma_2^2) - \\frac{(Y_i - \\mu_2)^2}{2\\sigma_2^2} \\right) \\right]$$

### Solution, step 2: The E-step (Posterior Responsibilities)
In the E-step, we evaluate the conditional expectation of $\\ell_c$ with respect to the latent variables $\\mathbf{Z}$ given the observed data $\\mathbf{Y}$ and current parameter estimates $\\boldsymbol{\\theta}^{(t)} = (\\pi^{(t)}, \\mu_1^{(t)}, \\mu_2^{(t)}, (\\sigma_1^2)^{(t)}, (\\sigma_2^2)^{(t)})$.
Because $\\ell_c$ is linear in the latent indicators $Z_{ik}$, we need only evaluate the conditional expectations:

$$\\gamma_{ik}^{(t)} = \\mathbb{E}[Z_{ik} \\mid Y_i = y_i, \\boldsymbol{\\theta}^{(t)}] = \\mathbb{P}(Z_{ik} = 1 \\mid Y_i = y_i, \\boldsymbol{\\theta}^{(t)})$$

Applying Bayes' Theorem:

$$\\gamma_{i1}^{(t)} = \\frac{\\mathbb{P}(Z_{i1} = 1) f(y_i \\mid Z_{i1} = 1)}{\\mathbb{P}(Z_{i1} = 1) f(y_i \\mid Z_{i1} = 1) + \\mathbb{P}(Z_{i2} = 1) f(y_i \\mid Z_{i2} = 1)} = \\frac{\\pi^{(t)} \\phi(y_i; \\mu_1^{(t)}, (\\sigma_1^2)^{(t)})}{\\pi^{(t)} \\phi(y_i; \\mu_1^{(t)}, (\\sigma_1^2)^{(t)}) + (1 - \\pi^{(t)}) \\phi(y_i; \\mu_2^{(t)}, (\\sigma_2^2)^{(t)})}$$

and $\\gamma_{i2}^{(t)} = 1 - \\gamma_{i1}^{(t)}$.
The quantity $\\gamma_{ik}^{(t)} \\in (0, 1)$ represents the posterior **responsibility** that component $k$ takes for generating observation $y_i$.
The expected complete-data log-likelihood is:

$$Q(\\boldsymbol{\\theta} \\mid \\boldsymbol{\\theta}^{(t)}) = \\sum_{i=1}^n \\sum_{k=1}^2 \\gamma_{ik}^{(t)} \\left[ \\ln(\\pi_k) - \\frac{1}{2} \\ln(2\\pi\\sigma_k^2) - \\frac{(y_i - \\mu_k)^2}{2\\sigma_k^2} \\right]$$

where $\\pi_1 = \\pi$ and $\\pi_2 = 1 - \\pi$.

### Solution, step 3: The M-step (Parameter Updates)
In the M-step, we maximize $Q(\\boldsymbol{\\theta} \\mid \\boldsymbol{\\theta}^{(t)})$ with respect to $\\boldsymbol{\\theta} = (\\pi, \\mu_1, \\mu_2, \\sigma_1^2, \\sigma_2^2)$.
Notice that $Q$ cleanly decomposes into separate terms for $\\pi$ and for each component $(\\mu_k, \\sigma_k^2)$:

1. **Update for mixing proportion $\\pi$**:
   Maximize $\\sum_{i=1}^n [\\gamma_{i1}^{(t)} \\ln(\\pi) + \\gamma_{i2}^{(t)} \\ln(1 - \\pi)]$.
   Differentiating with respect to $\\pi$ and setting to zero:
   $$\\frac{\\sum_{i=1}^n \\gamma_{i1}^{(t)}}{\\pi} - \\frac{\\sum_{i=1}^n \\gamma_{i2}^{(t)}}{1 - \\pi} = 0$$
   Let $N_k = \\sum_{i=1}^n \\gamma_{ik}^{(t)}$ be the effective number of observations assigned to component $k$.
   Then $N_1 + N_2 = \\sum_{i=1}^n (\\gamma_{i1} + \\gamma_{i2}) = n$.
   Solving yields:
   $$\\pi^{(t+1)} = \\frac{N_1}{n} = \\frac{1}{n} \\sum_{i=1}^n \\gamma_{i1}^{(t)}$$
2. **Update for component means $\\mu_k$**:
   Differentiating $Q$ with respect to $\\mu_k$:
   $$\\frac{\\partial Q}{\\partial \\mu_k} = \\sum_{i=1}^n \\gamma_{ik}^{(t)} \\frac{y_i - \\mu_k}{\\sigma_k^2} = 0 \\implies \\sum_{i=1}^n \\gamma_{ik}^{(t)} y_i - \\mu_k \\sum_{i=1}^n \\gamma_{ik}^{(t)} = 0$$
   Solving for $\\mu_k$:
   $$\\mu_k^{(t+1)} = \\frac{\\sum_{i=1}^n \\gamma_{ik}^{(t)} y_i}{\\sum_{i=1}^n \\gamma_{ik}^{(t)}} = \\frac{1}{N_k} \\sum_{i=1}^n \\gamma_{ik}^{(t)} y_i$$
   The updated mean is the **responsibility-weighted sample average**!
3. **Update for component variances $\\sigma_k^2$**:
   Differentiating $Q$ with respect to $\\sigma_k^2$:
   $$\\frac{\\partial Q}{\\partial \\sigma_k^2} = \\sum_{i=1}^n \\gamma_{ik}^{(t)} \\left( -\\frac{1}{2\\sigma_k^2} + \\frac{(y_i - \\mu_k)^2}{2(\\sigma_k^2)^2} \\right) = 0$$
   Multiplying by $2(\\sigma_k^2)^2$:
   $$-\\sigma_k^2 \\sum_{i=1}^n \\gamma_{ik}^{(t)} + \\sum_{i=1}^n \\gamma_{ik}^{(t)} (y_i - \\mu_k)^2 = 0$$
   Substituting the updated mean $\\mu_k^{(t+1)}$:
   $$(\\sigma_k^2)^{(t+1)} = \\frac{\\sum_{i=1}^n \\gamma_{ik}^{(t)} (y_i - \\mu_k^{(t+1)})^2}{\\sum_{i=1}^n \\gamma_{ik}^{(t)}} = \\frac{1}{N_k} \\sum_{i=1}^n \\gamma_{ik}^{(t)} (y_i - \\mu_k^{(t+1)})^2$$
   The updated variance is the **responsibility-weighted sample variance**!

### Solution, step 4: Singularity Avoidance
A well-known pathology of Gaussian mixtures is that the unconstrained likelihood function is unbounded. If a component mean lands exactly on a single observation $\\mu_1 = y_j$, and its variance approaches zero $\\sigma_1^2 \\to 0$, the density $\\phi(y_j; \\mu_1, \\sigma_1^2) = \\frac{1}{\\sqrt{2\\pi}\\sigma_1} \\to \\infty$, causing the likelihood to diverge to $+\\infty$.
In practice, the EM algorithm avoids this spurious singularity by:
- Enforcing a positive variance floor: $\\sigma_k^2 \\ge c > 0$ for all iterations.
- Placing an inverse-Gamma or conjugate Wishart prior on $(\\mu_k, \\sigma_k^2)$ (Maximum A Posteriori / MAP estimation), which adds a penalty term that smoothly prevents variances from collapsing to zero.
"""

(OUT_DIR / "unit-4.md").write_text(u4_text, encoding="utf-8")
print(f"Unit 4 prose count: {prose_count(u4_text)} words")
