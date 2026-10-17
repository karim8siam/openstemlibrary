# Unit 6: Exponential Families of Distributions: Natural Parameters, Completeness, and Information Bounds

## 6.1 Standard and Canonical (Natural) Representations of Exponential Families

In the vast landscape of parametric probability models, one structural family stands out above all others for its exceptional analytical elegance, geometric regularity, and computational tractability: the **Exponential Family of distributions**. First identified systematically by Georges Darmois, Bernard Koopman, and E. J. G. Pitman in the mid-1930s, the exponential family encompasses almost all standard classical distributions—including the Gaussian, Bernoulli, Binomial, Poisson, Geometric, Negative Binomial, Multinomial, Exponential, Gamma, Beta, and von Mises distributions.

### The General Representation
Let $(\mathcal{X}, \mathcal{A}, \mu)$ be a measurable space equipped with a $\sigma$-finite reference measure $\mu$. A parametric family of probability distributions $\mathcal{P} = \{P_{\boldsymbol{\theta}} : \boldsymbol{\theta} \in \Theta\}$ dominated by $\mu$ is said to be a **$k$-parameter Exponential Family** if the generalized probability density function (or probability mass function) can be expressed in the factored exponential form:

$$f(\mathbf{x}; \boldsymbol{\theta}) = \exp\left( \sum_{j=1}^k c_j(\boldsymbol{\theta}) T_j(\mathbf{x}) - d(\boldsymbol{\theta}) + S(\mathbf{x}) \right) \mathbf{1}_{\mathcal{X}_0}(\mathbf{x})$$

where:
1. $T_1(\mathbf{x}), T_2(\mathbf{x}), \dots, T_k(\mathbf{x})$ are real-valued Borel measurable functions defined on the sample space $\mathcal{X}$, termed the **sufficient statistics**.
2. $c_1(\boldsymbol{\theta}), c_2(\boldsymbol{\theta}), \dots, c_k(\boldsymbol{\theta})$ are real-valued functions of the parameter vector $\boldsymbol{\theta} \in \Theta$.
3. $d(\boldsymbol{\theta})$ is a real-valued scalar function ensuring that the density integrates to unity over $\mathcal{X}$.
4. $S(\mathbf{x})$ is a real-valued measurable function of the data vector alone.
5. $\mathcal{X}_0 \subseteq \mathcal{X}$ is the support of the distribution, which **must be strictly invariant with respect to $\boldsymbol{\theta}$**.

Equivalently, setting $h(\mathbf{x}) = \exp(S(\mathbf{x})) \mathbf{1}_{\mathcal{X}_0}(\mathbf{x})$ and $C(\boldsymbol{\theta}) = \exp(-d(\boldsymbol{\theta}))$, the family can be written in multiplicative standard form:

$$f(\mathbf{x}; \boldsymbol{\theta}) = C(\boldsymbol{\theta}) h(\mathbf{x}) \exp\left( \sum_{j=1}^k c_j(\boldsymbol{\theta}) T_j(\mathbf{x}) \right)$$

Notice that by the Fisher-Neyman Factorization Theorem (Unit 5), the $k$-dimensional vector:

$$\mathbf{T}(\mathbf{X}) = (T_1(\mathbf{X}), T_2(\mathbf{X}), \dots, T_k(\mathbf{X}))^T$$

is immediately and automatically a **sufficient statistic** for the parameter vector $\boldsymbol{\theta}$.

### The Pitman-Koopman-Darmois Theorem: The Characterization of Sufficiency

A fundamental question that occupied mathematical statisticians in the 1930s was whether families of distributions possessing fixed-dimension sufficient statistics were rare curiosities or formed a well-defined mathematical class. In independent papers published between 1935 and 1936, Georges Darmois in France, Bernard Koopman in the United States, and E. J. G. Pitman in the United Kingdom resolved this problem completely.

**Theorem (Pitman-Koopman-Darmois Theorem)**: Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed random sample from a family of continuous distributions $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ with common support $\mathcal{X}_0$ that does not depend on the parameter $\theta$. Assume that the probability density function $f(x; \theta)$ is continuously differentiable with respect to $x$. If there exists a sufficient statistic $\mathbf{T}(X_1, \dots, X_n)$ whose dimension $k$ remains strictly bounded as the sample size $n$ approaches infinity ($k \le K < \infty$ for all $n \ge K$), then $\mathcal{P}$ is necessarily an **Exponential Family**.

The implications of this theorem are profound for computational and mathematical statistics:
1. **Universal Dimension Reduction**: If a statistical model does not belong to the exponential family, the dimension of the minimal sufficient statistic typically grows linearly with sample size ($k = n$). For example, for the Cauchy distribution $\text{Cauchy}(\theta, 1)$ or the Student's $t$-distribution, no data reduction is possible without losing Fisher information: the minimal sufficient statistic is the entire order statistic $(X_{(1)}, \dots, X_{(n)})$. To compute likelihoods, one must retain all $n$ raw data points in memory.
2. **Support Invariance is Crucial**: If the support depends upon the parameter $\theta$, non-exponential families can admit finite-dimensional sufficient statistics. For instance, in the Uniform distribution $\text{Uniform}(0, \theta)$, the support is $[0, \theta]$, and the single scalar order statistic $X_{(n)} = \max(X_1, \dots, X_n)$ is sufficient for all $n$. However, because the support boundary shifts with $\theta$, the family violates the support invariance axiom and falls outside the exponential family framework.


### The Canonical (Natural) Representation
The standard representation often obscures the underlying convex geometry because the functions $c_j(\boldsymbol{\theta})$ may be non-linear. To reveal the natural geometry of the family, we execute a reparameterization.
Define the **natural (or canonical) parameters**:

$$\eta_j = c_j(\boldsymbol{\theta}) \quad \text{for } j = 1, 2, \dots, k$$

Grouping them into the natural parameter vector $\boldsymbol{\eta} = (\eta_1, \eta_2, \dots, \eta_k)^T \in \mathbb{R}^k$, and the sufficient statistics into $\mathbf{T}(\mathbf{x}) = (T_1(\mathbf{x}), \dots, T_k(\mathbf{x}))^T$, the linear combination in the exponent becomes the standard Euclidean inner product:

$$\sum_{j=1}^k c_j(\boldsymbol{\theta}) T_j(\mathbf{x}) = \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) = \langle \boldsymbol{\eta}, \mathbf{T}(\mathbf{x}) \rangle$$

The normalizing constant $C(\boldsymbol{\theta})$ is determined by the total probability axiom:

$$\int_{\mathcal{X}} f(\mathbf{x}; \boldsymbol{\eta}) \, d\mu(\mathbf{x}) = \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) + S(\mathbf{x}) \right) d\mu(\mathbf{x}) = 1$$

Factoring out the term depending solely on $\boldsymbol{\eta}$, we define the **log-partition function** (also known as the cumulant function or free energy):

$$A(\boldsymbol{\eta}) = \ln \left( \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) \right) e^{S(\mathbf{x})} \, d\mu(\mathbf{x}) \right)$$

This yields the celebrated **Canonical (Natural) Exponential Family Representation**:

$$f(\mathbf{x}; \boldsymbol{\eta}) = \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right) h(\mathbf{x})$$

where $h(\mathbf{x}) = e^{S(\mathbf{x})} \mathbf{1}_{\mathcal{X}_0}(\mathbf{x})$ is the base reference measure density.

## 6.2 The Natural Parameter Space and its Fundamental Convexity

The set of all natural parameter vectors for which the density can be normalized into a legitimate probability measure is called the **natural parameter space**.

**Definition (Natural Parameter Space)**: The natural parameter space $\Xi \subseteq \mathbb{R}^k$ of an exponential family is defined as the set of all vectors $\boldsymbol{\eta} \in \mathbb{R}^k$ for which the normalizing integral is strictly finite:

$$\Xi = \left\{ \boldsymbol{\eta} \in \mathbb{R}^k : \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x}) < \infty \right\}$$

A remarkable mathematical property of the exponential family is that its natural parameter space is universally convex.

**Theorem (Convexity of the Natural Parameter Space)**: The natural parameter space $\Xi$ is a **convex subset** of $\mathbb{R}^k$. Furthermore, the log-partition function $A(\boldsymbol{\eta})$ is a **strictly convex function** on $\Xi$ (provided the statistics $T_1, \dots, T_k$ are affinely independent).

**Proof**:
Let $\boldsymbol{\eta}_1, \boldsymbol{\eta}_2 \in \Xi$, and let $\alpha \in (0, 1)$. Define the convex combination $\boldsymbol{\eta}_\alpha = \alpha \boldsymbol{\eta}_1 + (1 - \alpha) \boldsymbol{\eta}_2$.
We must show that $\boldsymbol{\eta}_\alpha \in \Xi$.
Consider the normalizing integral for $\boldsymbol{\eta}_\alpha$:
$$M(\boldsymbol{\eta}_\alpha) = \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}_\alpha^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x}) = \int_{\mathcal{X}} \left[ \exp\left( \boldsymbol{\eta}_1^T \mathbf{T}(\mathbf{x}) \right) \right]^\alpha \left[ \exp\left( \boldsymbol{\eta}_2^T \mathbf{T}(\mathbf{x}) \right) \right]^{1 - \alpha} h(\mathbf{x}) \, d\mu(\mathbf{x})$$
Express $h(\mathbf{x}) = [h(\mathbf{x})]^\alpha [h(\mathbf{x})]^{1 - \alpha}$ and apply **Hölder's Inequality** with conjugate exponents $p = 1/\alpha > 1$ and $q = 1/(1 - \alpha) > 1$ (satisfying $1/p + 1/q = \alpha + (1 - \alpha) = 1$):
$$M(\boldsymbol{\eta}_\alpha) \le \left( \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}_1^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x}) \right)^\alpha \left( \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}_2^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x}) \right)^{1 - \alpha} = [M(\boldsymbol{\eta}_1)]^\alpha [M(\boldsymbol{\eta}_2)]^{1 - \alpha}$$
Because $\boldsymbol{\eta}_1, \boldsymbol{\eta}_2 \in \Xi$, both $M(\boldsymbol{\eta}_1) < \infty$ and $M(\boldsymbol{\eta}_2) < \infty$.
Therefore, their weighted geometric product is strictly finite:
$$M(\boldsymbol{\eta}_\alpha) < \infty \implies \boldsymbol{\eta}_\alpha \in \Xi$$
Thus, $\Xi$ is a convex set.

Taking natural logarithms across Hölder's inequality:
$$\ln M(\boldsymbol{\eta}_\alpha) \le \alpha \ln M(\boldsymbol{\eta}_1) + (1 - \alpha) \ln M(\boldsymbol{\eta}_2)$$
Recalling that $A(\boldsymbol{\eta}) = \ln M(\boldsymbol{\eta})$:
$$A(\alpha \boldsymbol{\eta}_1 + (1 - \alpha) \boldsymbol{\eta}_2) \le \alpha A(\boldsymbol{\eta}_1) + (1 - \alpha) A(\boldsymbol{\eta}_2)$$
This is precisely the definition of a convex function.
By Hölder's equality condition, equality holds if and only if $\exp(\boldsymbol{\eta}_1^T \mathbf{T}(\mathbf{x})) = c \exp(\boldsymbol{\eta}_2^T \mathbf{T}(\mathbf{x}))$ almost surely for some constant $c > 0$, which implies $(\boldsymbol{\eta}_1 - \boldsymbol{\eta}_2)^T \mathbf{T}(\mathbf{x}) = \ln c$.
If the coordinate functions $T_1(\mathbf{x}), \dots, T_k(\mathbf{x})$ and the constant 1 are linearly independent with respect to the reference measure $\mu$ (affinely independent), then $\boldsymbol{\eta}_1 = \boldsymbol{\eta}_2$.
Therefore, $A(\boldsymbol{\eta})$ is **strictly convex** on $\Xi$. $\blacksquare$

### Regular Versus Curved Exponential Families
A $k$-parameter exponential family is classified based on the relationship between its parameter dimension and its sufficient statistics:
1. **Full-Rank (Regular) Exponential Family**: The natural parameter space $\Xi$ has a non-empty interior in $\mathbb{R}^k$ (contains an open $k$-dimensional rectangle or ball), and the dimension of $\boldsymbol{\theta}$ equals the dimension of the sufficient statistic: $\dim(\boldsymbol{\theta}) = k$. In full-rank families, classical asymptotic and finite-sample properties hold with maximal power.
2. **Curved Exponential Family**: The original parameter space $\Theta \subseteq \mathbb{R}^d$ has dimension $d$ strictly smaller than the dimension $k$ of the minimal sufficient statistic: $d < k$. The mapping $\boldsymbol{\theta} \mapsto \boldsymbol{\eta}(\boldsymbol{\theta})$ defines a $d$-dimensional curved manifold embedded within the $k$-dimensional natural parameter space $\mathbb{R}^k$. A famous example is the normal distribution $\mathcal{N}(\mu, \mu^2)$ where the variance equals the square of the mean ($d = 1$, but $k = 2$ with $\mathbf{T} = (\sum X_i, \sum X_i^2)$). Bradley Efron (1975) developed the concept of **statistical curvature** to quantify the information loss that occurs in curved exponential families relative to full-rank families.

## 6.3 The Log-Partition Function: Mean Vector and Covariance Matrix Generation

In classical calculus, evaluating the moments of a multivariate distribution requires executing complicated multidimensional integrals. In the exponential family, the log-partition function $A(\boldsymbol{\eta})$ acts as a master **cumulant generating potential**: differentiating $A(\boldsymbol{\eta})$ algebraically generates the moments and cumulants of the sufficient statistics without performing any integration!

### The Gradient of $A(\boldsymbol{\eta})$ Generates the Mean Vector
Recall that:

$$\exp(A(\boldsymbol{\eta})) = \int_{\mathcal{X}} \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

When $\boldsymbol{\eta}$ resides in the interior of the natural parameter space $\Xi^\circ$, the integrand is dominated by integrable functions in a neighborhood of $\boldsymbol{\eta}$. By the Leibniz Integral Rule and the Dominated Convergence Theorem, we can differentiate under the integral sign with respect to the $j$-th natural coordinate $\eta_j$:

$$\frac{\partial}{\partial \eta_j} \exp(A(\boldsymbol{\eta})) = \int_{\mathcal{X}} \frac{\partial}{\partial \eta_j} \exp\left( \sum_{m=1}^k \eta_m T_m(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x}) = \int_{\mathcal{X}} T_j(\mathbf{x}) \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

Using the chain rule on the left side: $\frac{\partial}{\partial \eta_j} \exp(A(\boldsymbol{\eta})) = \exp(A(\boldsymbol{\eta})) \frac{\partial A(\boldsymbol{\eta})}{\partial \eta_j}$. Dividing through by $\exp(A(\boldsymbol{\eta}))$:

$$\frac{\partial A(\boldsymbol{\eta})}{\partial \eta_j} = \int_{\mathcal{X}} T_j(\mathbf{x}) \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x}) = \int_{\mathcal{X}} T_j(\mathbf{x}) f(\mathbf{x}; \boldsymbol{\eta}) \, d\mu(\mathbf{x})$$

Notice that the right-hand side is precisely the definition of the mathematical expectation of $T_j(\mathbf{X})$ under parameter $\boldsymbol{\eta}$! Therefore:

$$\mathbb{E}_{\boldsymbol{\eta}}[T_j(\mathbf{X})] = \frac{\partial A(\boldsymbol{\eta})}{\partial \eta_j}$$

In vector gradient notation, the **mean vector of the sufficient statistics** is given by the gradient of the log-partition function:

$$\mathbb{E}_{\boldsymbol{\eta}}[\mathbf{T}(\mathbf{X})] = \nabla A(\boldsymbol{\eta})$$

### The Hessian Matrix of $A(\boldsymbol{\eta})$ Generates the Covariance Matrix
Differentiating a second time under the integral sign with respect to $\eta_m$:

$$\frac{\partial^2 A(\boldsymbol{\eta})}{\partial \eta_j \partial \eta_m} = \frac{\partial}{\partial \eta_m} \int_{\mathcal{X}} T_j(\mathbf{x}) \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

Applying the product rule to the exponential term:

$$\frac{\partial^2 A(\boldsymbol{\eta})}{\partial \eta_j \partial \eta_m} = \int_{\mathcal{X}} T_j(\mathbf{x}) \left( T_m(\mathbf{x}) - \frac{\partial A(\boldsymbol{\eta})}{\partial \eta_m} \right) \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

Rewriting in terms of mathematical expectations:

$$\frac{\partial^2 A(\boldsymbol{\eta})}{\partial \eta_j \partial \eta_m} = \mathbb{E}_{\boldsymbol{\eta}}\left[ T_j(\mathbf{X}) \left( T_m(\mathbf{X}) - \mathbb{E}_{\boldsymbol{\eta}}[T_m(\mathbf{X})] \right) \right]$$

Since $\mathbb{E}_{\boldsymbol{\eta}}\left[ \mathbb{E}_{\boldsymbol{\eta}}[T_j(\mathbf{X})] (T_m(\mathbf{X}) - \mathbb{E}_{\boldsymbol{\eta}}[T_m(\mathbf{X})]) \right] = 0$, this is identically equal to the covariance:

$$\text{Cov}_{\boldsymbol{\eta}}(T_j(\mathbf{X}), T_m(\mathbf{X})) = \mathbb{E}_{\boldsymbol{\eta}}\left[ \left( T_j(\mathbf{X}) - \mathbb{E}_{\boldsymbol{\eta}}[T_j(\mathbf{X})] \right) \left( T_m(\mathbf{X}) - \mathbb{E}_{\boldsymbol{\eta}}[T_m(\mathbf{X})] \right) \right] = \frac{\partial^2 A(\boldsymbol{\eta})}{\partial \eta_j \partial \eta_m}$$

In matrix Hessian notation, the **covariance matrix of the sufficient statistics** is given by the Hessian of the log-partition function:

$$\text{Cov}_{\boldsymbol{\eta}}(\mathbf{T}(\mathbf{X})) = \nabla^2 A(\boldsymbol{\eta})$$

Because a covariance matrix is always positive semi-definite (and strictly positive-definite if the statistics are affinely independent), this provides an independent proof that the Hessian $\nabla^2 A(\boldsymbol{\eta}) \succ 0$ is positive-definite, confirming that $A(\boldsymbol{\eta})$ is strictly convex on $\Xi^\circ$.

### Fisher Information in Canonical Exponential Families
In Unit 1, Fisher Information was defined as the variance of the score function.
In a canonical exponential family, the log-likelihood is:

$$\ell(\boldsymbol{\eta}; \mathbf{x}) = \ln f(\mathbf{x}; \boldsymbol{\eta}) = \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) + \ln h(\mathbf{x})$$

The score vector is the gradient with respect to $\boldsymbol{\eta}$:

$$\mathbf{S}(\boldsymbol{\eta}) = \nabla_{\boldsymbol{\eta}} \ell(\boldsymbol{\eta}; \mathbf{x}) = \mathbf{T}(\mathbf{x}) - \nabla A(\boldsymbol{\eta}) = \mathbf{T}(\mathbf{x}) - \mathbb{E}_{\boldsymbol{\eta}}[\mathbf{T}(\mathbf{X})]$$

Notice that the score vector is simply the centered sufficient statistic!
The Fisher Information matrix is the covariance of the score vector:

$$\mathbf{I}(\boldsymbol{\eta}) = \text{Cov}_{\boldsymbol{\eta}}(\mathbf{S}(\boldsymbol{\eta})) = \text{Cov}_{\boldsymbol{\eta}}(\mathbf{T}(\mathbf{X})) = \nabla^2 A(\boldsymbol{\eta})$$

Thus, in canonical exponential families, the **Fisher Information matrix is identically equal to the Hessian of the log-partition function**:

$$\mathbf{I}(\boldsymbol{\eta}) = \nabla^2 A(\boldsymbol{\eta})$$

This fundamental identity connects information geometry directly with convex analysis: the Riemannian metric tensor of the statistical manifold is precisely the Hessian of the potential function $A(\boldsymbol{\eta})$.

## 6.4 Moment Generating Functions of Sufficient Statistics

The moment generating function of the sufficient statistic $\mathbf{T}(\mathbf{X})$ can also be evaluated directly from the log-partition function without integrating.

Let $\mathbf{t} \in \mathbb{R}^k$. The MGF of $\mathbf{T}(\mathbf{X})$ under parameter $\boldsymbol{\eta}$ is:

$$M_{\mathbf{T}}(\mathbf{t}; \boldsymbol{\eta}) = \mathbb{E}_{\boldsymbol{\eta}}\left[ e^{\mathbf{t}^T \mathbf{T}(\mathbf{X})} \right] = \int_{\mathcal{X}} e^{\mathbf{t}^T \mathbf{T}(\mathbf{x})} \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

Combine the exponential terms:

$$M_{\mathbf{T}}(\mathbf{t}; \boldsymbol{\eta}) = e^{-A(\boldsymbol{\eta})} \int_{\mathcal{X}} \exp\left( (\boldsymbol{\eta} + \mathbf{t})^T \mathbf{T}(\mathbf{x}) \right) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

Recognizing the integral as $\exp(A(\boldsymbol{\eta} + \mathbf{t}))$:

$$M_{\mathbf{T}}(\mathbf{t}; \boldsymbol{\eta}) = e^{-A(\boldsymbol{\eta})} \exp(A(\boldsymbol{\eta} + \mathbf{t})) = \exp\left( A(\boldsymbol{\eta} + \mathbf{t}) - A(\boldsymbol{\eta}) \right)$$

Taking natural logarithms, the cumulant generating function of $\mathbf{T}(\mathbf{X})$ is:

$$K_{\mathbf{T}}(\mathbf{t}; \boldsymbol{\eta}) = \ln M_{\mathbf{T}}(\mathbf{t}; \boldsymbol{\eta}) = A(\boldsymbol{\eta} + \mathbf{t}) - A(\boldsymbol{\eta})$$

This proves that $A(\boldsymbol{\eta})$ is the universal cumulant generating function for the sufficient statistics: evaluating the $r$-th mixed partial derivatives of $A(\boldsymbol{\eta})$ yields the exact $r$-th joint cumulants of $(T_1, \dots, T_k)$ across all orders!

## 6.5 Completeness of the Natural Sufficient Statistic in Full-Rank Families

In Unit 5, we saw that completeness is the crucial condition required by the Lehmann-Scheffé theorem to guarantee the uniqueness of UMVUEs and by Basu's theorem to prove statistical independence. In full-rank exponential families, completeness is guaranteed automatically.

**Theorem (Completeness of Full-Rank Exponential Families)**: Let $\mathcal{P} = \{f(\mathbf{x}; \boldsymbol{\eta}) : \boldsymbol{\eta} \in \Xi\}$ be a $k$-parameter canonical exponential family. If the natural parameter space $\Xi$ contains a non-empty open rectangle:

$$\mathcal{O} = (\eta_{1, \min}, \eta_{1, \max}) \times (\eta_{2, \min}, \eta_{2, \max}) \times \dots \times (\eta_{k, \min}, \eta_{k, \max}) \subseteq \Xi$$

then the natural sufficient statistic:

$$\mathbf{T}(\mathbf{X}) = (T_1(\mathbf{X}), T_2(\mathbf{X}), \dots, T_k(\mathbf{X}))^T$$

is a **complete statistic** for the family $\mathcal{P}$.

**Proof Strategy via Fourier Inversion**:
Suppose $g(\mathbf{t})$ is any Borel measurable function of $\mathbf{T}$ such that:
$$\mathbb{E}_{\boldsymbol{\eta}}[g(\mathbf{T}(\mathbf{X}))] = 0 \quad \text{for all } \boldsymbol{\eta} \in \Xi$$
Let $\nu$ denote the push-forward measure of $h(\mathbf{x}) \, d\mu(\mathbf{x})$ under $\mathbf{T}$. The expectation can be written as an integral over the range space $\mathbb{R}^k$:
$$\int_{\mathbb{R}^k} g(\mathbf{t}) \exp\left( \boldsymbol{\eta}^T \mathbf{t} - A(\boldsymbol{\eta}) \right) d\nu(\mathbf{t}) = 0$$
Multiplying by $\exp(A(\boldsymbol{\eta})) > 0$:
$$\int_{\mathbb{R}^k} g(\mathbf{t}) \exp\left( \boldsymbol{\eta}^T \mathbf{t} \right) d\nu(\mathbf{t}) = 0 \quad \text{for all } \boldsymbol{\eta} \in \mathcal{O}$$
Decompose $g(\mathbf{t}) = g^+(\mathbf{t}) - g^-(\mathbf{t})$ into its positive and negative parts:
$$\int_{\mathbb{R}^k} \exp\left( \boldsymbol{\eta}^T \mathbf{t} \right) g^+(\mathbf{t}) \, d\nu(\mathbf{t}) = \int_{\mathbb{R}^k} \exp\left( \boldsymbol{\eta}^T \mathbf{t} \right) g^-(\mathbf{t}) \, d\nu(\mathbf{t})$$
Fix any point $\boldsymbol{\eta}_0 \in \mathcal{O}$. Define two positive finite measures on $(\mathbb{R}^k, \mathcal{B}(\mathbb{R}^k))$:
$$d\nu_1(\mathbf{t}) = \exp\left( \boldsymbol{\eta}_0^T \mathbf{t} \right) g^+(\mathbf{t}) \, d\nu(\mathbf{t}), \quad d\nu_2(\mathbf{t}) = \exp\left( \boldsymbol{\eta}_0^T \mathbf{t} \right) g^-(\mathbf{t}) \, d\nu(\mathbf{t})$$
The integral equation states that for all $\mathbf{s} \in \mathbb{R}^k$ such that $\boldsymbol{\eta}_0 + \mathbf{s} \in \mathcal{O}$:
$$\int_{\mathbb{R}^k} e^{\mathbf{s}^T \mathbf{t}} \, d\nu_1(\mathbf{t}) = \int_{\mathbb{R}^k} e^{\mathbf{s}^T \mathbf{t}} \, d\nu_2(\mathbf{t})$$
Because $\boldsymbol{\eta}_0$ is in the interior $\mathcal{O}$, this equality holds on an open neighborhood of $\mathbf{s} = \mathbf{0}$.
Analytically continuing this relation from real arguments $\mathbf{s}$ to purely imaginary arguments $i\mathbf{u}$ (where $\mathbf{u} \in \mathbb{R}^k$ and $i = \sqrt{-1}$), the identity theorem for complex analytic functions guarantees that:
$$\int_{\mathbb{R}^k} e^{i \mathbf{u}^T \mathbf{t}} \, d\nu_1(\mathbf{t}) = \int_{\mathbb{R}^k} e^{i \mathbf{u}^T \mathbf{t}} \, d\nu_2(\mathbf{t}) \quad \text{for all } \mathbf{u} \in \mathbb{R}^k$$
Notice that the left and right sides are the **characteristic functions (multidimensional Fourier transforms)** of the measures $\nu_1$ and $\nu_2$!
By the uniqueness theorem of Fourier transforms (Lévy's Inversion Theorem), two measures having identical characteristic functions must be identical:
$$\nu_1(B) = \nu_2(B) \quad \text{for all measurable sets } B \in \mathcal{B}(\mathbb{R}^k)$$
Equating their Radon-Nikodym derivatives:
$$\exp\left( \boldsymbol{\eta}_0^T \mathbf{t} \right) g^+(\mathbf{t}) = \exp\left( \boldsymbol{\eta}_0^T \mathbf{t} \right) g^-(\mathbf{t}) \quad \nu\text{-almost everywhere}$$
Dividing by $\exp(\boldsymbol{\eta}_0^T \mathbf{t}) > 0$:
$$g^+(\mathbf{t}) = g^-(\mathbf{t}) \implies g(\mathbf{t}) = g^+(\mathbf{t}) - g^-(\mathbf{t}) = 0 \quad \nu\text{-almost everywhere}$$
Therefore:
$$P_{\boldsymbol{\eta}}(g(\mathbf{T}(\mathbf{X})) = 0) = 1 \quad \text{for all } \boldsymbol{\eta} \in \Xi$$
This proves that $\mathbf{T}(\mathbf{X})$ is a **complete statistic**. $\blacksquare$

This theorem guarantees that for Gaussian, Poisson, Gamma, Beta, and Binomial distributions, the natural sufficient statistics are unconditionally complete. Every unbiased estimator based on them is automatically the unique UMVUE.

## 6.6 Convex Duality and the Expectation Parameters

The natural parameter vector $\boldsymbol{\eta} \in \Xi$ provides an extrinsic mathematical representation of the distribution. An alternative, deeply intuitive intrinsic parameterization is provided by the **expectation parameters** (or mean-value parameters):

$$\boldsymbol{\mu} = \mathbb{E}_{\boldsymbol{\eta}}[\mathbf{T}(\mathbf{X})] = \nabla A(\boldsymbol{\eta})$$

Because $A(\boldsymbol{\eta})$ is strictly convex on $\Xi$, the gradient mapping:

$$\nabla A: \Xi^\circ \to \mathcal{M}$$

is a smooth, one-to-one diffeomorphism from the interior of the natural parameter space $\Xi^\circ$ onto the interior of the **marginal polytope** (the convex hull of the support of $\mathbf{T}$):

$$\mathcal{M} = \left\{ \boldsymbol{\mu} \in \mathbb{R}^k : \boldsymbol{\mu} = \int_{\mathcal{X}} \mathbf{T}(\mathbf{x}) f(\mathbf{x}; \boldsymbol{\eta}) \, d\mu(\mathbf{x}) \text{ for some } \boldsymbol{\eta} \in \Xi \right\}$$

### Legendre-Fenchel Convex Duality
The relationship between the natural parameters $\boldsymbol{\eta}$ and expectation parameters $\boldsymbol{\mu}$ is governed by **Legendre-Fenchel convex duality**.
The convex conjugate (Legendre transform) of the log-partition function $A(\boldsymbol{\eta})$ is defined by:

$$A^*(\boldsymbol{\mu}) = \sup_{\boldsymbol{\eta} \in \Xi} \left\{ \boldsymbol{\eta}^T \boldsymbol{\mu} - A(\boldsymbol{\eta}) \right\}$$

The supremum is achieved at the unique point $\boldsymbol{\eta}$ where the gradient equals $\boldsymbol{\mu}$: $\nabla A(\boldsymbol{\eta}) = \boldsymbol{\mu}$.
Substituting this optimal $\boldsymbol{\eta}(\boldsymbol{\mu})$:

$$A^*(\boldsymbol{\mu}) = \boldsymbol{\eta}(\boldsymbol{\mu})^T \boldsymbol{\mu} - A(\boldsymbol{\eta}(\boldsymbol{\mu}))$$

The dual function $A^*(\boldsymbol{\mu})$ has a profound physical interpretation: it is precisely the **negative Shannon entropy** (or Boltzmann-Gibbs entropy) of the distribution!
Furthermore, the gradient of the dual function inverts the mapping:

$$\nabla A^*(\boldsymbol{\mu}) = \boldsymbol{\eta}$$

This establishes a perfect symmetric duality between natural parameters and expectation parameters:
- $\nabla A(\boldsymbol{\eta}) = \boldsymbol{\mu}$ maps natural parameters to expected moments.
- $\nabla A^*(\boldsymbol{\mu}) = \boldsymbol{\eta}$ maps expected moments back to natural parameters.

### Maximum Entropy Characterization
Exponential families arise naturally as the unique solutions to constrained entropy maximization problems (the Principle of Maximum Entropy, E. T. Jaynes, 1957).

**Theorem (Maximum Entropy Law)**: Among all probability distributions on $\mathcal{X}$ satisfying specified moment constraints:

$$\mathbb{E}[T_j(\mathbf{X})] = \mu_j \quad \text{for } j = 1, 2, \dots, k$$

the unique probability distribution that maximizes the Shannon differential entropy:

$$H(P) = -\int_{\mathcal{X}} f(\mathbf{x}) \ln f(\mathbf{x}) \, d\mu(\mathbf{x})$$

is the **Exponential Family distribution** $f(\mathbf{x}; \boldsymbol{\eta}) = \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right)$, where $\boldsymbol{\eta} = \nabla A^*(\boldsymbol{\mu})$ is chosen to satisfy the moment constraints.

This proves that exponential families are the most unbiased, least informative, and maximally neutral distributions compatible with observed empirical moments.

## 6.7 Conjugate Prior Distributions in Bayesian Statistics

In Bayesian inference, an analyst specifies a prior probability distribution $\pi(\boldsymbol{\theta})$ over the parameter space $\Theta$. Upon observing data $\mathbf{x}$, Bayes' theorem updates the prior to the posterior distribution:

$$\pi(\boldsymbol{\theta} \mid \mathbf{x}) \propto \pi(\boldsymbol{\theta}) \cdot L(\boldsymbol{\theta}; \mathbf{x})$$

A family of prior distributions is called **conjugate** to a likelihood model if the posterior distribution belongs to the exact same parametric family as the prior.

In 1979, Persi Diaconis and Donald Ylvisaker proved that **canonical exponential families possess natural conjugate priors of exceptional simplicity**.

Let $f(\mathbf{x}; \boldsymbol{\eta}) = \exp\left( \boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}) \right) h(\mathbf{x})$ be a canonical exponential family.
Define the prior distribution over the natural parameter vector $\boldsymbol{\eta} \in \Xi$ by:

$$\pi(\boldsymbol{\eta}; n_0, \mathbf{t}_0) = \exp\left( \boldsymbol{\eta}^T \mathbf{t}_0 - n_0 A(\boldsymbol{\eta}) - B(n_0, \mathbf{t}_0) \right)$$

where $n_0 > 0$ represents the prior "effective sample size", $\mathbf{t}_0 \in \mathbb{R}^k$ represents prior "pseudo-observations", and $B(n_0, \mathbf{t}_0)$ is the normalizing constant.

Now, observe a sample $\mathbf{X}_1, \dots, \mathbf{X}_n$ with observed sufficient statistic $\mathbf{T}_{\text{obs}} = \sum_{i=1}^n \mathbf{T}(\mathbf{X}_i)$.
The likelihood of the sample is:

$$L(\boldsymbol{\eta}; \mathbf{X}_1, \dots, \mathbf{X}_n) = \exp\left( \boldsymbol{\eta}^T \mathbf{T}_{\text{obs}} - n A(\boldsymbol{\eta}) \right) \prod_{i=1}^n h(\mathbf{X}_i)$$

Multiplying the prior by the likelihood:

$$\pi(\boldsymbol{\eta} \mid \mathbf{X}_1, \dots, \mathbf{X}_n) \propto \exp\left( \boldsymbol{\eta}^T \mathbf{t}_0 - n_0 A(\boldsymbol{\eta}) \right) \cdot \exp\left( \boldsymbol{\eta}^T \mathbf{T}_{\text{obs}} - n A(\boldsymbol{\eta}) \right)$$

Combine the linear exponents:

$$\pi(\boldsymbol{\eta} \mid \mathbf{X}_1, \dots, \mathbf{X}_n) \propto \exp\left( \boldsymbol{\eta}^T \left( \mathbf{t}_0 + \mathbf{T}_{\text{obs}} \right) - (n_0 + n) A(\boldsymbol{\eta}) \right)$$

Notice that the posterior distribution belongs to the **exact same parametric family** with updated hyperparameters:

$$n_{\text{post}} = n_0 + n, \quad \mathbf{t}_{\text{post}} = \mathbf{t}_0 + \mathbf{T}_{\text{obs}}$$

Bayesian updating in exponential families reduces to simple arithmetic addition:
- Prior sample size $n_0$ increases by the observed sample size $n$.
- Prior pseudo-statistic $\mathbf{t}_0$ increases by the observed sufficient statistic $\mathbf{T}_{\text{obs}}$.

Examples include the Beta-Binomial, Dirichlet-Multinomial, Gamma-Poisson, and Normal-Inverse-Gamma conjugate updating models.

## 6.8 The Cramér-Rao Lower Bound and Attainment in Exponential Families

In point estimation, a fundamental lower bound limits the precision achievable by any unbiased estimator.

**Theorem (Cramér-Rao Inequality)**: Let $W(\mathbf{X})$ be an unbiased estimator of a scalar parameter function $\tau(\theta)$ under a regular parametric family with Fisher Information $I(\theta)$. Then the variance of $W$ is bounded below by:

$$\text{Var}_\theta(W) \ge \frac{[\tau'(\theta)]^2}{I(\theta)}$$

### Characterization of Equality Attainment
When is the Cramér-Rao Lower Bound attained with exact equality?
By the Cauchy-Schwarz inequality used in the proof of the Cramér-Rao inequality, equality holds if and only if the estimator $W(\mathbf{X})$ is a linear function of the score function $S(\theta; \mathbf{X}) = \frac{\partial}{\partial \theta} \ln f(\mathbf{X}; \theta)$:

$$W(\mathbf{x}) - \tau(\theta) = k(\theta) \frac{\partial}{\partial \theta} \ln f(\mathbf{x}; \theta) \quad \text{almost surely for all } \theta \in \Theta$$

for some function $k(\theta) \ne 0$.
Integrating this differential equation with respect to $\theta$:

$$\frac{\partial}{\partial \theta} \ln f(\mathbf{x}; \theta) = \frac{W(\mathbf{x}) - \tau(\theta)}{k(\theta)} = \frac{W(\mathbf{x})}{k(\theta)} - \frac{\tau(\theta)}{k(\theta)}$$

Integrating with respect to $\theta$:

$$\ln f(\mathbf{x}; \theta) = W(\mathbf{x}) \int \frac{1}{k(\theta)} \, d\theta - \int \frac{\tau(\theta)}{k(\theta)} \, d\theta + \ln h(\mathbf{x})$$

Exponentiating both sides:

$$f(\mathbf{x}; \theta) = \exp\left( c(\theta) W(\mathbf{x}) - d(\theta) \right) h(\mathbf{x})$$

where $c(\theta) = \int \frac{1}{k(\theta)} \, d\theta$ and $d(\theta) = \int \frac{\tau(\theta)}{k(\theta)} \, d\theta$.

This establishes a definitive theorem:

**Theorem (Cramér-Rao Efficiency Attainment)**: The Cramér-Rao Lower Bound is achieved by an unbiased estimator if and only if the underlying family of distributions is an **Exponential Family**, and the parameter function being estimated is $\tau(\theta) = \mathbb{E}_\theta[W(\mathbf{X})]$, where $W(\mathbf{X})$ is the natural sufficient statistic!

No estimator outside the Exponential Family can ever achieve the Cramér-Rao Lower Bound across its entire parameter space.

## 6.9 Information Geometry, the Fisher-Rao Metric, and Dually Flat Manifolds

In modern mathematical statistics, a parametric family of distributions $\mathcal{S} = \{P_{\boldsymbol{\theta}} : \boldsymbol{\theta} \in \Theta\}$ is conceptualized as a smooth differential manifold—termed a **statistical manifold**—where each point on the manifold represents an entire probability distribution. The pioneer of this geometric synthesis, Shun-ichi Amari (1985), demonstrated that canonical exponential families possess an extraordinary geometric structure known as **dual flatness**.

### The Fisher-Rao Riemannian Metric
In classical differential geometry, a manifold is equipped with a Riemannian metric tensor $g_{ij}(\boldsymbol{\theta})$ that defines inner products on the tangent spaces, measuring infinitesimal distances between neighboring points.
C. R. Rao (1945) proved that the unique, geometrically invariant Riemannian metric on a statistical manifold is given by the **Fisher Information matrix**:

$$g_{ij}(\boldsymbol{\theta}) = I_{ij}(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}\left[ \frac{\partial \ln f}{\partial \theta_i} \frac{\partial \ln f}{\partial \theta_j} \right]$$

The geodesic distance between two probability distributions $P_{\boldsymbol{\theta}_1}$ and $P_{\boldsymbol{\theta}_2}$ under this metric is known as the **Fisher-Rao distance**:

$$d_{\text{FR}}(P_{\boldsymbol{\theta}_1}, P_{\boldsymbol{\theta}_2}) = \inf_{\gamma} \int_0^1 \sqrt{ \left( \frac{d\boldsymbol{\theta}}{dt} \right)^T \mathbf{I}(\boldsymbol{\theta}(t)) \left( \frac{d\boldsymbol{\theta}}{dt} \right) } \, dt$$

where the infimum is taken over all smooth paths $\gamma(t)$ connecting $\boldsymbol{\theta}_1$ to $\boldsymbol{\theta}_2$.

### Dual Affine Connections and Flatness
In a canonical exponential family, the Fisher Information matrix is the Hessian of the log-partition function: $\mathbf{I}(\boldsymbol{\eta}) = \nabla^2 A(\boldsymbol{\eta})$.
Amari introduced a one-parameter family of affine connections $\nabla^{(\alpha)}$ indexed by $\alpha \in \mathbb{R}$:
- The connection $\nabla^{(1)}$ is termed the **exponential connection ($e$-connection)**.
- The connection $\nabla^{(-1)}$ is termed the **mixture connection ($m$-connection)**.

A statistical manifold is said to be $e$-flat if its Riemann curvature tensor with respect to the $e$-connection vanishes identically: $R^{(e)} = 0$.
A manifold is $m$-flat if $R^{(m)} = 0$.

In a full-rank exponential family:
1. The natural parameterization $\boldsymbol{\eta}$ forms an **affine coordinate system with respect to the $e$-connection**. The manifold is strictly $e$-flat. Geodesics under the $e$-connection are straight lines in the natural parameter space: $\boldsymbol{\eta}(t) = (1 - t)\boldsymbol{\eta}_1 + t \boldsymbol{\eta}_2$.
2. The expectation parameterization $\boldsymbol{\mu}$ forms an **affine coordinate system with respect to the $m$-connection**. The manifold is strictly $m$-flat. Geodesics under the $m$-connection are straight lines in the expectation parameter space: $\boldsymbol{\mu}(t) = (1 - t)\boldsymbol{\mu}_1 + t \boldsymbol{\mu}_2$.

Because the manifold is simultaneously $e$-flat and $m$-flat with respect to mutually dual affine connections, canonical exponential families are **dually flat Riemannian spaces**.

## 6.10 Kullback-Leibler Divergence, Relative Entropy, and Bregman Divergences

While the Fisher-Rao metric measures infinitesimal local distances, the global separation between two probability distributions $P$ and $Q$ is quantified by the **Kullback-Leibler (KL) divergence** (or relative entropy):

$$D_{\text{KL}}(P \parallel Q) = \int_{\mathcal{X}} f_P(\mathbf{x}) \ln\left( \frac{f_P(\mathbf{x})}{f_Q(\mathbf{x})} \right) d\mu(\mathbf{x})$$

By Jensen's Inequality, $D_{\text{KL}}(P \parallel Q) \ge 0$, with equality if and only if $P = Q$ almost surely.

### Representation via the Log-Partition Function
Consider two members of a canonical exponential family with natural parameters $\boldsymbol{\eta}_1$ and $\boldsymbol{\eta}_2$:

$$f(\mathbf{x}; \boldsymbol{\eta}_1) = \exp\left( \boldsymbol{\eta}_1^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}_1) \right) h(\mathbf{x}), \quad f(\mathbf{x}; \boldsymbol{\eta}_2) = \exp\left( \boldsymbol{\eta}_2^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta}_2) \right) h(\mathbf{x})$$

The log-density ratio is:

$$\ln\left( \frac{f(\mathbf{x}; \boldsymbol{\eta}_1)}{f(\mathbf{x}; \boldsymbol{\eta}_2)} \right) = (\boldsymbol{\eta}_1 - \boldsymbol{\eta}_2)^T \mathbf{T}(\mathbf{x}) - \left[ A(\boldsymbol{\eta}_1) - A(\boldsymbol{\eta}_2) \right]$$

Taking the expectation under $P_{\boldsymbol{\eta}_1}$:

$$D_{\text{KL}}(P_{\boldsymbol{\eta}_1} \parallel P_{\boldsymbol{\eta}_2}) = (\boldsymbol{\eta}_1 - \boldsymbol{\eta}_2)^T \mathbb{E}_{\boldsymbol{\eta}_1}[\mathbf{T}(\mathbf{X})] - A(\boldsymbol{\eta}_1) + A(\boldsymbol{\eta}_2)$$

Recalling that $\boldsymbol{\mu}_1 = \mathbb{E}_{\boldsymbol{\eta}_1}[\mathbf{T}(\mathbf{X})] = \nabla A(\boldsymbol{\eta}_1)$, we obtain:

$$D_{\text{KL}}(P_{\boldsymbol{\eta}_1} \parallel P_{\boldsymbol{\eta}_2}) = A(\boldsymbol{\eta}_2) - A(\boldsymbol{\eta}_1) - (\boldsymbol{\eta}_2 - \boldsymbol{\eta}_1)^T \nabla A(\boldsymbol{\eta}_1)$$

Notice that the right-hand side is precisely the definition of the **Bregman divergence** $B_A(\boldsymbol{\eta}_2, \boldsymbol{\eta}_1)$ associated with the strictly convex function $A$:

$$D_{\text{KL}}(P_{\boldsymbol{\eta}_1} \parallel P_{\boldsymbol{\eta}_2}) = B_A(\boldsymbol{\eta}_2, \boldsymbol{\eta}_1)$$

The KL divergence represents the vertical discrepancy between the convex surface $A(\boldsymbol{\eta}_2)$ and its tangent plane linearized at $\boldsymbol{\eta}_1$!

### The Generalized Pythagorean Theorem
In Euclidean geometry, the Pythagorean theorem states that if two vectors $\mathbf{a} - \mathbf{b}$ and $\mathbf{b} - \mathbf{c}$ are orthogonal, then $\|\mathbf{a} - \mathbf{c}\|^2 = \|\mathbf{a} - \mathbf{b}\|^2 + \|\mathbf{b} - \mathbf{c}\|^2$.
In information geometry, a remarkable generalized Pythagorean theorem governs dually flat exponential manifolds.

**Theorem (Generalized Pythagorean Theorem)**: Let $P_{\boldsymbol{\eta}_1}$, $P_{\boldsymbol{\eta}_2}$, and $P_{\boldsymbol{\eta}_3}$ be three distributions on an exponential manifold. If the $e$-geodesic connecting $\boldsymbol{\eta}_1$ to $\boldsymbol{\eta}_2$ is orthogonal (under the Fisher metric) to the $m$-geodesic connecting $\boldsymbol{\eta}_2$ to $\boldsymbol{\eta}_3$:

$$(\boldsymbol{\eta}_1 - \boldsymbol{\eta}_2)^T (\boldsymbol{\mu}_2 - \boldsymbol{\mu}_3) = 0$$

then the Kullback-Leibler divergence decomposes additively:

$$D_{\text{KL}}(P_{\boldsymbol{\eta}_1} \parallel P_{\boldsymbol{\eta}_3}) = D_{\text{KL}}(P_{\boldsymbol{\eta}_1} \parallel P_{\boldsymbol{\eta}_2}) + D_{\text{KL}}(P_{\boldsymbol{\eta}_2} \parallel P_{\boldsymbol{\eta}_3})$$

This Pythagorean decomposition provides the mathematical foundation for maximum likelihood estimation, projection onto linear exponential sub-families, and information projection (I-projection) in machine learning.

## 6.11 Curved Exponential Families and Efron's Statistical Curvature

When the parameter of interest $\theta \in \Theta \subseteq \mathbb{R}$ is scalar, but the minimal sufficient statistic $\mathbf{T}(\mathbf{X}) \in \mathbb{R}^k$ has dimension $k > 1$, the model forms a **curved exponential family**. The mapping $\theta \mapsto \boldsymbol{\eta}(\theta)$ traces out a 1-dimensional curved curve within the $k$-dimensional natural parameter space $\mathbb{R}^k$.

Bradley Efron (1975) introduced the fundamental concept of **statistical curvature** to quantify how severely a curved exponential model deviates from a full-rank family.

### Definition of Statistical Curvature
Let $\mathbf{T}(\mathbf{X})$ be the $k$-dimensional natural sufficient statistic with covariance matrix $\boldsymbol{\Sigma}_{\boldsymbol{\eta}} = \nabla^2 A(\boldsymbol{\eta}) = \mathbf{I}(\boldsymbol{\eta})$.
Differentiating the natural parameter curve $\boldsymbol{\eta}(\theta)$ with respect to $\theta$:
- The velocity vector is $\dot{\boldsymbol{\eta}}(\theta) = \frac{d\boldsymbol{\eta}}{d\theta} \in \mathbb{R}^k$.
- The acceleration vector is $\ddot{\boldsymbol{\eta}}(\theta) = \frac{d^2\boldsymbol{\eta}}{d\theta^2} \in \mathbb{R}^k$.

The Fisher Information for the scalar parameter $\theta$ from a single observation is:

$$I(\theta) = \dot{\boldsymbol{\eta}}(\theta)^T \mathbf{I}(\boldsymbol{\eta}(\theta)) \dot{\boldsymbol{\eta}}(\theta) = \|\dot{\boldsymbol{\eta}}(\theta)\|_{\mathbf{I}}^2$$

The statistical curvature $\gamma_\theta \ge 0$ is defined as the norm of the component of the acceleration vector $\ddot{\boldsymbol{\eta}}(\theta)$ that is **orthogonal** to the velocity vector $\dot{\boldsymbol{\eta}}(\theta)$ under the Fisher Riemannian metric:

$$\gamma_\theta^2 = \frac{\ddot{\boldsymbol{\eta}}_\perp^T \mathbf{I}(\boldsymbol{\eta}) \ddot{\boldsymbol{\eta}}_\perp}{I(\theta)^2} = \frac{\ddot{\boldsymbol{\eta}}^T \mathbf{I} \ddot{\boldsymbol{\eta}} \cdot \dot{\boldsymbol{\eta}}^T \mathbf{I} \dot{\boldsymbol{\eta}} - (\dot{\boldsymbol{\eta}}^T \mathbf{I} \ddot{\boldsymbol{\eta}})^2}{(\dot{\boldsymbol{\eta}}^T \mathbf{I} \dot{\boldsymbol{\eta}})^3}$$

Notice that if the parameterization $\boldsymbol{\eta}(\theta)$ is a straight line in natural coordinates ($\ddot{\boldsymbol{\eta}} \propto \dot{\boldsymbol{\eta}}$), the orthogonal component vanishes: $\gamma_\theta = 0$. Thus, a model has zero statistical curvature if and only if it is a full-rank (linear) exponential family.

### Asymptotic Consequences of Statistical Curvature
Efron proved that statistical curvature governs the second-order asymptotic efficiency of the Maximum Likelihood Estimator (MLE) $\hat{\theta}_n$:
1. **Asymptotic Variance Inflation**: In large samples, while the first-order asymptotic variance of $\hat{\theta}_n$ achieves the Cramér-Rao bound $\frac{1}{n I(\theta)}$, the second-order expansion reveals:
   $$\text{Var}_\theta(\hat{\theta}_n) = \frac{1}{n I(\theta)} + \frac{\gamma_\theta^2}{2 n^2 I(\theta)} + \mathcal{O}(n^{-3})$$
   The statistical curvature $\gamma_\theta^2$ directly quantifies the asymptotic variance inflation of the MLE!
2. **Fisher Information Loss**: In a sample of size $n$, the Fisher Information contained in the MLE $\hat{\theta}_n$ satisfies:
   $$I_{\hat{\theta}_n}(\theta) = n I(\theta) - \gamma_\theta^2 I(\theta) + \mathcal{O}(n^{-1})$$
   The quantity $\gamma_\theta^2 I(\theta)$ represents the permanent, irreversible loss of Fisher Information incurred by reducing the $k$-dimensional sufficient statistic $\mathbf{T}$ to the scalar MLE $\hat{\theta}_n$. To recover this lost information, an analyst must condition on an ancillary statistic measuring the distance from the data to the curved manifold.

## 6.12 Hypothesis Testing: Monotone Likelihood Ratios and the Karlin-Rubin Theorem

Exponential families provide the natural structural domain for the Neyman-Pearson theory of optimal hypothesis testing.

### Monotone Likelihood Ratio (MLR)
A 1-parameter family of distributions $\{f(x; \theta) : \theta \in \Theta \subseteq \mathbb{R}\}$ is said to possess a **Monotone Likelihood Ratio (MLR)** in a scalar statistic $T(X)$ if for any two parameter values $\theta_1 < \theta_2$, the likelihood ratio:

$$\frac{f(x; \theta_2)}{f(x; \theta_1)}$$

is a non-decreasing (monotone) function of $T(x)$.

Every 1-parameter canonical exponential family:

$$f(x; \theta) = \exp(\eta(\theta) T(x) - A(\theta)) h(x)$$

possesses a Monotone Likelihood Ratio in $T(X)$ if and only if the natural parameter $\eta(\theta)$ is a strictly increasing function of $\theta$.

### The Karlin-Rubin Theorem
In 1956, Samuel Karlin and Herman Rubin proved that families possessing an MLR admit **Uniformly Most Powerful (UMP)** tests for one-sided hypotheses.

**Theorem (Karlin-Rubin Theorem)**: Suppose $X$ has a distribution with an MLR in $T(X)$. Consider testing the one-sided null hypothesis:

$$H_0: \theta \le \theta_0 \quad \text{versus} \quad H_1: \theta > \theta_0$$

Then for any significance level $\alpha \in (0, 1)$, the test that rejects $H_0$ if and only if $T(X) > c$:

$$\phi(x) = \begin{cases} 1 & \text{if } T(x) > c \\ \gamma & \text{if } T(x) = c \\ 0 & \text{if } T(x) < c \end{cases}$$

where the critical value $c$ and randomization constant $\gamma \in [0, 1]$ are chosen such that $\mathbb{E}_{\theta_0}[\phi(X)] = \alpha$, is the **Uniformly Most Powerful (UMP) test of size $\alpha$**.

Furthermore, the power function $\beta(\theta) = \mathbb{E}_\theta[\phi(X)]$ is strictly increasing in $\theta$ for all $\theta$ where $\beta(\theta) < 1$.

The Karlin-Rubin Theorem establishes that for 1-parameter exponential families, one-sided hypothesis tests based on the natural sufficient statistic are unbeatable: no competing test can achieve greater statistical power against any alternative $\theta > \theta_0$.

## 6.13 Generalized Linear Models (GLMs) and Exponential Dispersion Families

In modern statistical practice and applied regression modeling, classical linear regression models are generalized to accommodate non-Gaussian response variables (such as binary binary classification, Poisson event counts, and Gamma survival durations) through the framework of **Generalized Linear Models (GLMs)**, developed by John Nelder and Robert Wedderburn in 1972.

GLMs model the response variable $Y$ using an **Exponential Dispersion Family**:

$$f(y; \theta, \phi) = \exp\left( \frac{y \theta - b(\theta)}{a(\phi)} + c(y, \phi) \right)$$

where:
1. $\theta$ is the natural parameter of location.
2. $\phi > 0$ is the **dispersion parameter** (governing variance scaling). Typically, $a(\phi) = \phi / w$, where $w > 0$ is a known observation weight.
3. $b(\theta)$ is the log-partition function, termed the **cumulant function**.

### Mean and Variance Functions in GLMs
Applying the moment-generating properties of exponential families (Section 6.3):
1. **Expected Value**:
   $$\mu = \mathbb{E}[Y] = b'(\theta)$$
2. **Variance**:
   $$\text{Var}(Y) = b''(\theta) a(\phi) = V(\mu) a(\phi)$$
   where $V(\mu) = b''(\theta(\mu))$ is the **variance function**, which characterizes how the variance of the response variable depends systematically on its expected value $\mu$.

Prominent examples of variance functions include:
- **Gaussian**: $b(\theta) = \theta^2 / 2 \implies V(\mu) = 1$ (constant variance, homoskedastic).
- **Poisson**: $b(\theta) = e^\theta \implies V(\mu) = \mu$ (variance equals mean).
- **Binomial ($m$ trials)**: $b(\theta) = m \ln(1 + e^\theta) \implies V(\mu) = \mu(1 - \mu/m)$.
- **Gamma**: $b(\theta) = -\ln(-\theta) \implies V(\mu) = \mu^2$ (constant coefficient of variation).
- **Inverse Gaussian**: $b(\theta) = -\sqrt{-2\theta} \implies V(\mu) = \mu^3$.

### The Link Function and Canonical Links
A GLM connects the expected value $\mu_i = \mathbb{E}[Y_i]$ to a linear predictor $\eta_i = \mathbf{x}_i^T \boldsymbol{\beta}$ through a monotonic, differentiable **link function** $g$:

$$g(\mu_i) = \eta_i = \mathbf{x}_i^T \boldsymbol{\beta} = \sum_{j=1}^p x_{ij} \beta_j$$

The **canonical link function** is chosen such that the linear predictor directly equals the natural parameter:

$$\eta_i = \theta_i \iff g(\mu) = (b')^{-1}(\mu)$$

Under canonical links:
- For Gaussian data: $g(\mu) = \mu$ (identity link).
- For Bernoulli data: $g(\mu) = \ln\left(\frac{\mu}{1 - \mu}\right)$ (logit link, yielding logistic regression).
- For Poisson data: $g(\mu) = \ln\mu$ (log link, yielding Poisson log-linear regression).
- For Gamma data: $g(\mu) = 1/\mu$ (reciprocal link).

Under canonical link functions, the sufficient statistics for the regression coefficients $\boldsymbol{\beta}$ are simply $\mathbf{X}^T \mathbf{y} = \sum_{i=1}^n \mathbf{x}_i y_i$, the log-likelihood is strictly concave in $\boldsymbol{\beta}$, and the Newton-Raphson algorithm coincides with Fisher's method of scoring (Iteratively Reweighted Least Squares / IRLS), guaranteeing global quadratic convergence to the unique maximum likelihood estimator.

## 6.14 The Diaconis-Ylvisaker Theorem: Linear Posterior Expectations in Conjugate Bayesian Inference

In Section 6.7, we observed that canonical exponential families admit natural conjugate prior distributions that update algebraically. A foundational theorem by Persi Diaconis and Donald Ylvisaker (1979) establishes an even deeper structural property: the posterior expectation of the mean parameter is **strictly linear in the sufficient statistic**.

Let $\mathbf{X} \sim f(\mathbf{x}; \boldsymbol{\eta}) = \exp(\boldsymbol{\eta}^T \mathbf{T}(\mathbf{x}) - A(\boldsymbol{\eta})) h(\mathbf{x})$ be a canonical exponential family, and let $\boldsymbol{\mu}(\boldsymbol{\eta}) = \mathbb{E}_{\boldsymbol{\eta}}[\mathbf{T}(\mathbf{X})] = \nabla A(\boldsymbol{\eta})$ denote the expectation parameter.
Consider the natural conjugate prior on $\boldsymbol{\eta}$:

$$\pi(\boldsymbol{\eta}; n_0, \mathbf{t}_0) = \exp\left( \boldsymbol{\eta}^T \mathbf{t}_0 - n_0 A(\boldsymbol{\eta}) - B(n_0, \mathbf{t}_0) \right)$$

where $n_0 > 0$ and $\mathbf{t}_0 / n_0 = \boldsymbol{\mu}_0 \in \mathcal{M}^\circ$ represents the prior expected value of $\boldsymbol{\mu}$.

**Theorem (Diaconis-Ylvisaker Linear Posterior Expectation Theorem)**: Under the natural conjugate prior $\pi(\boldsymbol{\eta}; n_0, \mathbf{t}_0)$, the posterior expectation of the mean parameter $\boldsymbol{\mu} = \nabla A(\boldsymbol{\eta})$ given an observed sample $\mathbf{X}_1, \dots, \mathbf{X}_n$ with sample mean sufficient statistic $\bar{\mathbf{T}} = \frac{1}{n}\sum_{i=1}^n \mathbf{T}(\mathbf{X}_i)$ is a **strictly convex linear combination** of the prior mean $\boldsymbol{\mu}_0$ and the sample average $\bar{\mathbf{T}}$:

$$\mathbb{E}\left[ \nabla A(\boldsymbol{\eta}) \mid \mathbf{X}_1, \dots, \mathbf{X}_n \right] = \frac{n_0 \boldsymbol{\mu}_0 + n \bar{\mathbf{T}}}{n_0 + n} = (1 - w) \boldsymbol{\mu}_0 + w \bar{\mathbf{T}}$$

where the shrinkage weight is:

$$w = \frac{n}{n_0 + n} \in (0, 1)$$

**Proof**:
Let $\mathbf{t}_n = \mathbf{t}_0 + n \bar{\mathbf{T}}$ and $n^* = n_0 + n$. The posterior density of $\boldsymbol{\eta}$ is:
$$\pi(\boldsymbol{\eta} \mid \text{data}) = \exp\left( \boldsymbol{\eta}^T \mathbf{t}_n - n^* A(\boldsymbol{\eta}) - B(n^*, \mathbf{t}_n) \right)$$
Consider the integral of the gradient $\nabla_{\boldsymbol{\eta}} \pi(\boldsymbol{\eta} \mid \text{data})$ over the interior of the natural parameter space $\Xi^\circ$:
$$\int_{\Xi} \nabla_{\boldsymbol{\eta}} \pi(\boldsymbol{\eta} \mid \text{data}) \, d\boldsymbol{\eta}$$
Differentiating the posterior density:
$$\nabla_{\boldsymbol{\eta}} \pi(\boldsymbol{\eta} \mid \text{data}) = \left( \mathbf{t}_n - n^* \nabla A(\boldsymbol{\eta}) \right) \pi(\boldsymbol{\eta} \mid \text{data})$$
By the divergence theorem, the integral of the gradient of a probability density vanishing on the boundary of $\Xi$ is identically zero:
$$\int_{\Xi} \left( \mathbf{t}_n - n^* \nabla A(\boldsymbol{\eta}) \right) \pi(\boldsymbol{\eta} \mid \text{data}) \, d\boldsymbol{\eta} = \mathbf{0}$$
Separating the two terms:
$$\mathbf{t}_n \int_{\Xi} \pi(\boldsymbol{\eta} \mid \text{data}) \, d\boldsymbol{\eta} - n^* \int_{\Xi} \nabla A(\boldsymbol{\eta}) \pi(\boldsymbol{\eta} \mid \text{data}) \, d\boldsymbol{\eta} = \mathbf{0}$$
Since the posterior integrates to unity ($\int \pi \, d\boldsymbol{\eta} = 1$):
$$\mathbf{t}_n - n^* \mathbb{E}\left[ \nabla A(\boldsymbol{\eta}) \mid \text{data} \right] = \mathbf{0}$$
Dividing through by $n^* = n_0 + n$:
$$\mathbb{E}\left[ \nabla A(\boldsymbol{\eta}) \mid \text{data} \right] = \frac{\mathbf{t}_n}{n^*} = \frac{\mathbf{t}_0 + n \bar{\mathbf{T}}}{n_0 + n} = \frac{n_0 \boldsymbol{\mu}_0 + n \bar{\mathbf{T}}}{n_0 + n}$$
This proves that the Bayes estimator under quadratic loss is an exact convex weighted average of the prior mean and the sample evidence. $\blacksquare$

Diaconis and Ylvisaker further established the remarkable converse: under mild regularity conditions, if the posterior expectation of the mean parameter is linear in the sample mean for all sample sizes $n$, the underlying distribution **must belong to the Exponential Family**, and the prior must be the natural conjugate prior!

## 6.15 Sufficiency, Algorithmic Information, and Minimum Description Length (MDL)

In algorithmic information theory (A. N. Kolmogorov, 1965) and Jorma Rissanen's **Minimum Description Length (MDL)** principle (1978), statistical modeling is viewed as data compression. The goal of science is to identify regularities in data that permit the shortest possible binary encoding of the observed experience.

### The Two-Part Code Interpretation of Sufficiency
Consider transmitting an observed dataset $\mathbf{x} = (x_1, \dots, x_n)$ across a noiseless binary communications channel to a receiver.
A two-part code transmits:
1. **The Model (Hypothesis)**: A compressed binary description of the estimated parameter or sufficient statistic $T(\mathbf{x})$.
2. **The Residual Data given the Model**: The index of the specific dataset $\mathbf{x}$ within the conditional equivalence class $T^{-1}(\{T(\mathbf{x})\})$.

The total code length (in Shannon bits) is:

$$L(\mathbf{x}) = L(T(\mathbf{x})) + L(\mathbf{x} \mid T(\mathbf{x}))$$

By Shannon's Source Coding Theorem, the ideal code length for transmitting $\mathbf{x}$ under a probability model $P_{\boldsymbol{\theta}}$ is:

$$L(\mathbf{x}; \boldsymbol{\theta}) = -\log_2 P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x}) = -\log_2 P_{\boldsymbol{\theta}}(T(\mathbf{X}) = T(\mathbf{x})) - \log_2 P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = T(\mathbf{x}))$$

Now, observe what happens when $T$ is a **sufficient statistic**:
By definition of sufficiency, the conditional distribution $P(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = T(\mathbf{x}))$ **contains zero dependence on $\boldsymbol{\theta}$**.
Therefore, the second part of the code—the residual data given the sufficient statistic—has a code length:

$$L(\mathbf{x} \mid T(\mathbf{x})) = -\log_2 P(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = T(\mathbf{x}))$$

which is completely universal and independent of $\boldsymbol{\theta}$!
All the regularities and structure in the data that can be compressed by learning the parameter $\boldsymbol{\theta}$ are entirely captured by the first part: $-\log_2 P_{\boldsymbol{\theta}}(T(\mathbf{X}) = T(\mathbf{x}))$. The residual is pure, incompressible random noise (uniform across the partition cell).

This algorithmic equivalence demonstrates that a sufficient statistic in mathematical statistics is identically equal to a **minimal sufficient description in computer science**, bridging classical likelihood theory with algorithmic information theory.

## Fully worked question 1: Canonical Exponential Family Classification of the Beta, Gamma, and Normal Distributions

### Question
Classify each of the following continuous parametric families into the canonical Exponential Family format $f(x; \boldsymbol{\eta}) = \exp\left( \boldsymbol{\eta}^T \mathbf{T}(x) - A(\boldsymbol{\eta}) \right) h(x)$:
1. The **Beta family** $\text{Beta}(\alpha, \beta)$ on $x \in (0, 1)$, with parameters $\alpha > 0, \beta > 0$.
2. The **Gamma family** $\text{Gamma}(\alpha, \beta)$ on $x > 0$, with shape $\alpha > 0$ and rate $\beta > 0$.
3. The **Univariate Normal family** $\mathcal{N}(\mu, \sigma^2)$ on $x \in \mathbb{R}$, with mean $\mu \in \mathbb{R}$ and variance $\sigma^2 > 0$.
For each family, explicitly identify:
- The natural parameter vector $\boldsymbol{\eta}$.
- The sufficient statistic vector $\mathbf{T}(x)$.
- The base measure density $h(x)$.
- The log-partition function $A(\boldsymbol{\eta})$.
- The natural parameter space $\Xi$ and verify its convexity.

### Solution, step 1: The Beta Family Classification
The probability density function of $X \sim \text{Beta}(\alpha, \beta)$ for $x \in (0, 1)$ is:

$$f(x; \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1} = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha - 1} (1 - x)^{\beta - 1}$$

Express the powers in exponential form using $x^{\alpha - 1} = \exp((\alpha - 1)\ln x)$ and $(1 - x)^{\beta - 1} = \exp((\beta - 1)\ln(1 - x))$:

$$f(x; \alpha, \beta) = \exp\left( (\alpha - 1)\ln x + (\beta - 1)\ln(1 - x) + \ln\Gamma(\alpha + \beta) - \ln\Gamma(\alpha) - \ln\Gamma(\beta) \right) \mathbf{1}_{(0, 1)}(x)$$

Define the natural parameters:

$$\eta_1 = \alpha - 1, \quad \eta_2 = \beta - 1$$

The natural parameter vector is $\boldsymbol{\eta} = (\eta_1, \eta_2)^T$.
The sufficient statistic vector is:

$$\mathbf{T}(x) = \begin{pmatrix} \ln x \\ \ln(1 - x) \end{pmatrix}$$

The base measure density is:

$$h(x) = \mathbf{1}_{(0, 1)}(x)$$

Expressing $\alpha = \eta_1 + 1$ and $\beta = \eta_2 + 1$, the log-partition function is:

$$A(\boldsymbol{\eta}) = \ln\Gamma(\eta_1 + 1) + \ln\Gamma(\eta_2 + 1) - \ln\Gamma(\eta_1 + \eta_2 + 2)$$

The natural parameter space requires $\alpha > 0$ and $\beta > 0$, which translates to:

$$\Xi = \{(\eta_1, \eta_2) \in \mathbb{R}^2 : \eta_1 > -1, \; \eta_2 > -1\} = (-1, \infty) \times (-1, \infty)$$

Because $\Xi$ is the Cartesian product of two open convex half-lines, $\Xi$ is an open convex quadrant in $\mathbb{R}^2$.

### Solution, step 2: The Gamma Family Classification
The probability density function of $X \sim \text{Gamma}(\alpha, \beta)$ for $x > 0$ is:

$$f(x; \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x} = \exp\left( (\alpha - 1)\ln x - \beta x + \alpha \ln\beta - \ln\Gamma(\alpha) \right) \mathbf{1}_{(0, \infty)}(x)$$

Define the natural parameters:

$$\eta_1 = \alpha - 1, \quad \eta_2 = -\beta$$

The natural parameter vector is $\boldsymbol{\eta} = (\eta_1, \eta_2)^T$.
The sufficient statistic vector is:

$$\mathbf{T}(x) = \begin{pmatrix} \ln x \\ x \end{pmatrix}$$

The base measure density is:

$$h(x) = \mathbf{1}_{(0, \infty)}(x)$$

Inverting the reparameterization gives $\alpha = \eta_1 + 1$ and $\beta = -\eta_2$.
The log-partition function is:

$$A(\boldsymbol{\eta}) = \ln\Gamma(\eta_1 + 1) - (\eta_1 + 1)\ln(-\eta_2)$$

The natural parameter space requires $\alpha > 0 \implies \eta_1 > -1$ and $\beta > 0 \implies \eta_2 < 0$:

$$\Xi = \{(\eta_1, \eta_2) \in \mathbb{R}^2 : \eta_1 > -1, \; \eta_2 < 0\} = (-1, \infty) \times (-\infty, 0)$$

This is an open convex quadrant in the fourth quadrant of $\mathbb{R}^2$.

### Solution, step 3: The Univariate Normal Family Classification
The probability density function of $X \sim \mathcal{N}(\mu, \sigma^2)$ for $x \in \mathbb{R}$ is:

$$f(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{x^2}{2\sigma^2} + \frac{\mu x}{\sigma^2} - \frac{\mu^2}{2\sigma^2} - \frac{1}{2}\ln(\sigma^2) \right)$$

Define the natural parameters:

$$\eta_1 = \frac{\mu}{\sigma^2}, \quad \eta_2 = -\frac{1}{2\sigma^2}$$

The natural parameter vector is $\boldsymbol{\eta} = (\eta_1, \eta_2)^T$.
The sufficient statistic vector is:

$$\mathbf{T}(x) = \begin{pmatrix} x \\ x^2 \end{pmatrix}$$

The base measure density is:

$$h(x) = \frac{1}{\sqrt{2\pi}}$$

Inverting the reparameterization: $\sigma^2 = -\frac{1}{2\eta_2}$ and $\mu = -\frac{\eta_1}{2\eta_2}$.
Substitute these into the normalizing term:

$$\frac{\mu^2}{2\sigma^2} = \frac{(-\eta_1 / (2\eta_2))^2}{2(-1/(2\eta_2))} = \frac{\eta_1^2 / (4\eta_2^2)}{-1/\eta_2} = -\frac{\eta_1^2}{4\eta_2}$$

$$\frac{1}{2}\ln(\sigma^2) = \frac{1}{2}\ln\left( -\frac{1}{2\eta_2} \right) = -\frac{1}{2}\ln(-2\eta_2)$$

Therefore, the log-partition function is:

$$A(\boldsymbol{\eta}) = -\frac{\eta_1^2}{4\eta_2} - \frac{1}{2}\ln(-2\eta_2)$$

The natural parameter space requires $\mu \in \mathbb{R} \implies \eta_1 \in \mathbb{R}$ and $\sigma^2 > 0 \implies \eta_2 < 0$:

$$\Xi = \{(\eta_1, \eta_2) \in \mathbb{R}^2 : \eta_1 \in \mathbb{R}, \; \eta_2 < 0\} = \mathbb{R} \times (-\infty, 0)$$

This is the open lower half-plane in $\mathbb{R}^2$, which is strictly convex. $\blacksquare$

## Fully worked question 2: Derivation of the Mean Vector and Covariance Matrix of Natural Sufficient Statistics via the Gradient and Hessian of $A(\boldsymbol{\eta})$

### Question
Consider the univariate Gaussian family $\mathcal{N}(\mu, \sigma^2)$ expressed in natural canonical form from Question 1:

$$\boldsymbol{\eta} = \begin{pmatrix} \eta_1 \\ \eta_2 \end{pmatrix} = \begin{pmatrix} \mu / \sigma^2 \\ -1 / (2\sigma^2) \end{pmatrix}, \quad \mathbf{T}(X) = \begin{pmatrix} X \\ X^2 \end{pmatrix}$$

with log-partition function:

$$A(\eta_1, \eta_2) = -\frac{\eta_1^2}{4\eta_2} - \frac{1}{2}\ln(-2\eta_2)$$

1. Compute the gradient vector $\nabla A(\boldsymbol{\eta}) = \left( \frac{\partial A}{\partial \eta_1}, \frac{\partial A}{\partial \eta_2} \right)^T$.
2. Verify that $\mathbb{E}[X] = \mu$ and $\mathbb{E}[X^2] = \mu^2 + \sigma^2$ using the gradient components.
3. Compute all second-order partial derivatives to construct the $2 \times 2$ Hessian matrix $\nabla^2 A(\boldsymbol{\eta})$.
4. Express the entries of $\nabla^2 A(\boldsymbol{\eta})$ in terms of $(\mu, \sigma^2)$ and verify that they match the exact theoretical variances and covariance: $\text{Var}(X) = \sigma^2$, $\text{Cov}(X, X^2) = 2\mu\sigma^2$, and $\text{Var}(X^2) = 2\sigma^4 + 4\mu^2\sigma^2$.

### Solution, step 1: Computation of the Gradient
We compute the partial derivatives of $A(\eta_1, \eta_2) = -\frac{\eta_1^2}{4\eta_2} - \frac{1}{2}\ln(-2\eta_2)$:

First, with respect to $\eta_1$:

$$\frac{\partial A}{\partial \eta_1} = -\frac{2\eta_1}{4\eta_2} = -\frac{\eta_1}{2\eta_2}$$

Second, with respect to $\eta_2$:

$$\frac{\partial A}{\partial \eta_2} = -\frac{\eta_1^2}{4} \frac{\partial}{\partial \eta_2}(\eta_2^{-1}) - \frac{1}{2} \frac{\partial}{\partial \eta_2}\ln(-2\eta_2) = -\frac{\eta_1^2}{4}(-\eta_2^{-2}) - \frac{1}{2}\left( \frac{-2}{-2\eta_2} \right) = \frac{\eta_1^2}{4\eta_2^2} - \frac{1}{2\eta_2}$$

The gradient vector is:

$$\nabla A(\boldsymbol{\eta}) = \begin{pmatrix} -\frac{\eta_1}{2\eta_2} \\ \frac{\eta_1^2}{4\eta_2^2} - \frac{1}{2\eta_2} \end{pmatrix}$$

### Solution, step 2: Verification of the Mean Vector
Substitute the natural parameter relations $\eta_1 = \mu / \sigma^2$ and $\eta_2 = -1 / (2\sigma^2)$:
1. For the first component:
   $$\mathbb{E}[T_1(X)] = \mathbb{E}[X] = -\frac{\eta_1}{2\eta_2} = -\frac{\mu / \sigma^2}{2(-1 / (2\sigma^2))} = -\frac{\mu / \sigma^2}{-1 / \sigma^2} = \mu$$
   This matches the theoretical population mean $\mathbb{E}[X] = \mu$.
2. For the second component:
   Notice that $\left(-\frac{\eta_1}{2\eta_2}\right)^2 = \mu^2$, and $-\frac{1}{2\eta_2} = -\frac{1}{2(-1/(2\sigma^2))} = \sigma^2$.
   Therefore:
   $$\mathbb{E}[T_2(X)] = \mathbb{E}[X^2] = \left(-\frac{\eta_1}{2\eta_2}\right)^2 - \frac{1}{2\eta_2} = \mu^2 + \sigma^2$$
   This matches the raw second moment identity: $\mathbb{E}[X^2] = \text{Var}(X) + (\mathbb{E}[X])^2 = \sigma^2 + \mu^2$.

### Solution, step 3: Computation of the Hessian Matrix
Differentiate each first derivative to find the second-order partial derivatives:
1. $\frac{\partial^2 A}{\partial \eta_1^2}$:
   $$\frac{\partial^2 A}{\partial \eta_1^2} = \frac{\partial}{\partial \eta_1}\left( -\frac{\eta_1}{2\eta_2} \right) = -\frac{1}{2\eta_2}$$
2. $\frac{\partial^2 A}{\partial \eta_1 \partial \eta_2}$:
   $$\frac{\partial^2 A}{\partial \eta_1 \partial \eta_2} = \frac{\partial}{\partial \eta_2}\left( -\frac{\eta_1}{2\eta_2} \right) = -\frac{\eta_1}{2} \left(-\eta_2^{-2}\right) = \frac{\eta_1}{2\eta_2^2}$$
3. $\frac{\partial^2 A}{\partial \eta_2^2}$:
   $$\frac{\partial^2 A}{\partial \eta_2^2} = \frac{\partial}{\partial \eta_2}\left( \frac{\eta_1^2}{4}\eta_2^{-2} - \frac{1}{2}\eta_2^{-1} \right) = \frac{\eta_1^2}{4}(-2\eta_2^{-3}) - \frac{1}{2}(-\eta_2^{-2}) = -\frac{\eta_1^2}{2\eta_2^3} + \frac{1}{2\eta_2^2}$$

The Hessian matrix is:

$$\nabla^2 A(\boldsymbol{\eta}) = \begin{pmatrix} -\frac{1}{2\eta_2} & \frac{\eta_1}{2\eta_2^2} \\ \frac{\eta_1}{2\eta_2^2} & -\frac{\eta_1^2}{2\eta_2^3} + \frac{1}{2\eta_2^2} \end{pmatrix}$$

### Solution, step 4: Conversion to Parameter Moments and Verification
Now express each entry of the Hessian in terms of $(\mu, \sigma^2)$:
1. Entry $(1, 1)$:
   $$\text{Var}(T_1(X)) = \text{Var}(X) = -\frac{1}{2\eta_2} = -\frac{1}{2(-1/(2\sigma^2))} = \sigma^2$$
   This matches the population variance.
2. Entry $(1, 2)$:
   $$\text{Cov}(T_1(X), T_2(X)) = \text{Cov}(X, X^2) = \frac{\eta_1}{2\eta_2^2} = \left(-\frac{\eta_1}{2\eta_2}\right) \left(-\frac{1}{\eta_2}\right) = \mu (2\sigma^2) = 2\mu \sigma^2$$
   To verify independently from normal moment theory:
   $$\text{Cov}(X, X^2) = \mathbb{E}[X^3] - \mathbb{E}[X]\mathbb{E}[X^2] = (\mu^3 + 3\mu\sigma^2) - \mu(\mu^2 + \sigma^2) = \mu^3 + 3\mu\sigma^2 - \mu^3 - \mu\sigma^2 = 2\mu\sigma^2$$
   The Hessian matches the theoretical covariance.
3. Entry $(2, 2)$:
   $$\text{Var}(T_2(X)) = \text{Var}(X^2) = -\frac{\eta_1^2}{2\eta_2^3} + \frac{1}{2\eta_2^2}$$
   Notice that $-\frac{\eta_1^2}{2\eta_2^3} = 4 \left( \frac{\eta_1^2}{4\eta_2^2} \right) \left( -\frac{1}{2\eta_2} \right) = 4 \mu^2 \sigma^2$.
   And $\frac{1}{2\eta_2^2} = 2 \left( -\frac{1}{2\eta_2} \right)^2 = 2 (\sigma^2)^2 = 2\sigma^4$.
   Therefore:
   $$\text{Var}(X^2) = 4\mu^2\sigma^2 + 2\sigma^4$$
   To verify independently:
   $$\text{Var}(X^2) = \mathbb{E}[X^4] - (\mathbb{E}[X^2])^2$$
   For a normal distribution, $\mathbb{E}[X^4] = \mu^4 + 6\mu^2\sigma^2 + 3\sigma^4$, and $(\mathbb{E}[X^2])^2 = (\mu^2 + \sigma^2)^2 = \mu^4 + 2\mu^2\sigma^2 + \sigma^4$.
   Subtracting:
   $$\text{Var}(X^2) = (\mu^4 + 6\mu^2\sigma^2 + 3\sigma^4) - (\mu^4 + 2\mu^2\sigma^2 + \sigma^4) = 4\mu^2\sigma^2 + 2\sigma^4$$
   The Hessian entry matches the theoretical variance. $\blacksquare$

## Fully worked question 3: Proof of Completeness of the Natural Sufficient Statistic in Full-Rank Exponential Families

### Question
Let $f(x; \eta) = \exp(\eta T(x) - A(\eta)) h(x)$ be a 1-parameter canonical exponential family with natural parameter $\eta \in \Xi \subseteq \mathbb{R}$. Suppose that the natural parameter space $\Xi$ contains an open interval $(a, b)$ with $-\infty < a < b < \infty$.
1. State the mathematical condition for the statistic $T(X)$ to be complete.
2. Express the expectation $\mathbb{E}_\eta[g(T(X))] = 0$ as a bilateral Laplace-Stieltjes transform.
3. Decompose the function $g(t) = g^+(t) - g^-(t)$ and define two non-negative finite measures.
4. Apply the identity theorem for analytic functions and the uniqueness of the Fourier transform to prove that $g(T(X)) = 0$ almost surely, thereby establishing completeness.

### Solution, step 1: Definition of Completeness
Let $g: \mathbb{R} \to \mathbb{R}$ be a Borel measurable function. The statistic $T(X)$ is complete for the family $\{P_\eta : \eta \in \Xi\}$ if:

$$\mathbb{E}_\eta[g(T(X))] = 0 \quad \text{for all } \eta \in (a, b) \implies P_\eta(g(T(X)) = 0) = 1 \quad \text{for all } \eta \in (a, b)$$

### Solution, step 2: Representation as a Laplace Transform
Let $\nu$ denote the measure induced on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ by the transformation $T(X)$ under the base measure $h(x) \, d\mu(x)$:

$$\nu(B) = \int_{T^{-1}(B)} h(x) \, d\mu(x), \quad B \in \mathcal{B}(\mathbb{R})$$

The mathematical expectation of $g(T(X))$ under parameter $\eta$ is:

$$\mathbb{E}_\eta[g(T(X))] = \int_\mathcal{X} g(T(x)) \exp(\eta T(x) - A(\eta)) h(x) \, d\mu(x) = e^{-A(\eta)} \int_{-\infty}^\infty g(t) e^{\eta t} \, d\nu(t)$$

Since $e^{-A(\eta)} > 0$ for all $\eta \in (a, b)$, the equation $\mathbb{E}_\eta[g(T(X))] = 0$ is equivalent to:

$$\int_{-\infty}^\infty g(t) e^{\eta t} \, d\nu(t) = 0 \quad \text{for all } \eta \in (a, b)$$

This is a two-sided (bilateral) Laplace transform of the signed measure $g(t) \, d\nu(t)$.

### Solution, step 3: Jordan Decomposition into Positive Measures
Decompose the function $g(t)$ into its positive and negative parts:

$$g(t) = g^+(t) - g^-(t)$$

where $g^+(t) = \max(g(t), 0) \ge 0$ and $g^-(t) = \max(-g(t), 0) \ge 0$.
The integral equation becomes:

$$\int_{-\infty}^\infty g^+(t) e^{\eta t} \, d\nu(t) = \int_{-\infty}^\infty g^-(t) e^{\eta t} \, d\nu(t) \quad \text{for all } \eta \in (a, b)$$

Fix a point $\eta_0 \in (a, b)$. Choose $\epsilon > 0$ such that the open interval $(\eta_0 - \epsilon, \eta_0 + \epsilon) \subset (a, b)$.
Define two non-negative measures on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$:

$$d\nu_1(t) = e^{\eta_0 t} g^+(t) \, d\nu(t), \quad d\nu_2(t) = e^{\eta_0 t} g^-(t) \, d\nu(t)$$

For any $s \in (-\epsilon, \epsilon)$, the parameter $\eta = \eta_0 + s$ lies inside $(a, b)$. Therefore:

$$\int_{-\infty}^\infty e^{s t} \, d\nu_1(t) = \int_{-\infty}^\infty e^{s t} e^{\eta_0 t} g^+(t) \, d\nu(t) = \int_{-\infty}^\infty e^{(\eta_0 + s) t} g^+(t) \, d\nu(t)$$

Equating to the negative part:

$$\int_{-\infty}^\infty e^{s t} \, d\nu_1(t) = \int_{-\infty}^\infty e^{s t} \, d\nu_2(t) \quad \text{for all } s \in (-\epsilon, \epsilon)$$

Setting $s = 0$ proves that the two measures have identical finite total mass:

$$\nu_1(\mathbb{R}) = \nu_2(\mathbb{R}) = C < \infty$$

If $C = 0$, then $g^+(t) = g^-(t) = 0$ $\nu$-almost everywhere, immediately completing the proof. Assume $C > 0$.

### Solution, step 4: Analytic Continuation and Fourier Uniqueness
Consider the complex-valued functions defined for $z = s + i u \in \mathbb{C}$ with $s = \text{Re}(z) \in (-\epsilon, \epsilon)$:

$$\Phi_1(z) = \int_{-\infty}^\infty e^{z t} \, d\nu_1(t), \quad \Phi_2(z) = \int_{-\infty}^\infty e^{z t} \, d\nu_2(t)$$

Because $\int e^{s t} \, d\nu_k(t) < \infty$ for all $s \in (-\epsilon, \epsilon)$, dominated convergence guarantees that $\Phi_1(z)$ and $\Phi_2(z)$ are **holomorphic (complex analytic) functions** on the vertical strip:

$$\Omega = \{z \in \mathbb{C} : -\epsilon < \text{Re}(z) < \epsilon\}$$

From Step 3, $\Phi_1(s) = \Phi_2(s)$ for all real $s \in (-\epsilon, \epsilon)$.
The real segment $(-\epsilon, \epsilon)$ has an accumulation point in $\Omega$.
By the **Identity Theorem for Holomorphic Functions**, two analytic functions that agree on a set containing an accumulation point must agree on the entire domain of analyticity $\Omega$:

$$\Phi_1(z) = \Phi_2(z) \quad \text{for all } z \in \Omega$$

In particular, evaluating this identity on the purely imaginary line $z = i u$ (where $\text{Re}(z) = 0 \in (-\epsilon, \epsilon)$):

$$\Phi_1(i u) = \int_{-\infty}^\infty e^{i u t} \, d\nu_1(t) = \int_{-\infty}^\infty e^{i u t} \, d\nu_2(t) = \Phi_2(i u) \quad \text{for all } u \in \mathbb{R}$$

Notice that $\Phi_1(i u)$ and $\Phi_2(i u)$ are the **characteristic functions (Fourier-Stieltjes transforms)** of the finite positive measures $\nu_1$ and $\nu_2$.
By the **Uniqueness Theorem of Fourier Transforms** (Lévy's Inversion Theorem):

$$\nu_1(B) = \nu_2(B) \quad \text{for all Borel sets } B \in \mathcal{B}(\mathbb{R})$$

Taking the Radon-Nikodym derivative with respect to $\nu$:

$$e^{\eta_0 t} g^+(t) = e^{\eta_0 t} g^-(t) \quad \nu\text{-almost everywhere}$$

Dividing by $e^{\eta_0 t} > 0$:

$$g^+(t) = g^-(t) \quad \nu\text{-almost everywhere}$$

Therefore, $g(t) = g^+(t) - g^-(t) = 0$ $\nu$-almost everywhere.
Consequently:

$$P_\eta(g(T(X)) = 0) = 1 \quad \text{for all } \eta \in (a, b)$$

This proves that $T(X)$ is a complete statistic. $\blacksquare$
