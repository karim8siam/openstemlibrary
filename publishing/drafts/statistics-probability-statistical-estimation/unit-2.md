# Unit 2: Cramér–Rao Inequality, Fisher Information & Efficiency

In this unit, we investigate the fundamental lower bounds on the variance of point estimators, establishing mathematical criteria to determine when an unbiased estimator has achieved the theoretical maximum possible precision. The celebrated Cramér–Rao Lower Bound (CRLB), formulated independently by Harald Cramér (1946) and C. R. Rao (1945), reveals that the variance of any unbiased estimator is bounded below by the reciprocal of the Fisher Information contained in the sample. Here, we develop the regularity conditions governing information inequalities, derive Bartlett's first and second score identities, prove the scalar and multiparameter Cramér–Rao bounds using Cauchy–Schwarz Hilbert space methods, establish the exact attainment conditions for efficiency, and investigate higher-order information bounds including the Bhattacharyya system.

## 2.1 Information Inequalities and Cramér-Rao Regularity Conditions

To establish mathematical bounds on estimation precision, we must ensure that the likelihood function is sufficiently well-behaved to permit the interchange of differentiation and integration across the sample space. Let $\mathcal{P} = \{f(\mathbf{x}; \theta) : \theta \in \Theta\}$ be a family of probability density functions dominated by a $\sigma$-finite reference measure $\mu$ on $(\mathcal{X}, \mathcal{A})$, where the parameter space $\Theta$ is an open interval or open connected domain in $\mathbb{R}$.

The classical **Cramér–Rao Regularity Conditions** (often denoted R0 through R4) are formulated as follows:

1. **Open Parameter Domain (R0)**: The parameter space $\Theta \subseteq \mathbb{R}$ is an open interval. This ensures that every parameter point $\theta$ is an interior point, admitting two-sided neighborhoods for differentiation.
2. **Invariant Support Condition (R1)**: The support of the density:
   $$\mathcal{S} = \{ \mathbf{x} \in \mathcal{X} : f(\mathbf{x}; \theta) > 0 \}$$
   is strictly independent of the parameter $\theta$. If the support boundary depends on $\theta$ (as in the uniform distribution $\text{Uniform}(0, \theta)$ or shifted exponential distribution), Leibniz's rule across boundary lines introduces Dirac delta distributions, invalidating classical information bounds.
3. **Differentiability of the Density (R2)**: For $\mu$-almost all $\mathbf{x} \in \mathcal{X}$, the derivative $\frac{\partial}{\partial \theta} f(\mathbf{x}; \theta)$ exists and is continuous for all $\theta \in \Theta$.
4. **Interchange of Differentiation and Integration (R3)**: The total probability integral:
   $$\int_\mathcal{X} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 1$$
   can be differentiated with respect to $\theta$ under the integral sign:
   $$\frac{d}{d\theta} \int_\mathcal{X} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = \int_\mathcal{X} \frac{\partial}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 0$$
   Similarly, for any estimator $T(\mathbf{X})$ with finite expectation $\mathbb{E}_\theta[T] = \int_\mathcal{X} T(\mathbf{x}) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x})$, differentiation under the integral sign is permissible:
   $$\frac{d}{d\theta} \mathbb{E}_\theta[T(\mathbf{X})] = \int_\mathcal{X} T(\mathbf{x}) \frac{\partial}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x})$$
   By the dominated convergence theorem, condition (R3) is guaranteed if there exist $\mu$-integrable functions $g_1(\mathbf{x})$ and $g_2(\mathbf{x})$ such that $\left| \frac{\partial f}{\partial \theta} \right| \le g_1(\mathbf{x})$ and $\left| T(\mathbf{x}) \frac{\partial f}{\partial \theta} \right| \le g_2(\mathbf{x})$ for all $\theta$ in a neighborhood of interest.
5. **Positive and Finite Fisher Information (R4)**: The Fisher Information $I(\theta)$ satisfies:
   $$0 < I(\theta) < \infty \quad \forall \theta \in \Theta$$
   A zero information value implies that data provide zero discriminatory evidence regarding perturbations in $\theta$, whereas infinite information signals non-regular super-efficiency.

### Pathology of Support-Dependent Densities: The Uniform Model
To comprehend why condition (R1) is indispensable, consider an i.i.d. sample $X_1, \dots, X_n \sim \text{Uniform}(0, \theta)$ with density $f(x; \theta) = \frac{1}{\theta} \mathbf{1}_{(0, \theta)}(x)$. The joint density is:

$$f_n(\mathbf{x}; \theta) = \frac{1}{\theta^n} \mathbf{1}_{\{x_{(n)} \le \theta\}} \mathbf{1}_{\{x_{(1)} \ge 0\}}$$

If one naively ignores the boundary and applies the score formula:

$$\frac{\partial}{\partial \theta} \ln f_n = -\frac{n}{\theta} \implies I_n(\theta) = \frac{n}{\theta^2}$$

This would suggest a Cramér–Rao lower bound of $\frac{\theta^2}{n}$. However, the maximum order statistic $X_{(n)}$ has distribution function $F_{(n)}(t) = (t/\theta)^n$, and its expectation is $\mathbb{E}[X_{(n)}] = \frac{n}{n+1} \theta$. Therefore, the scaled statistic:

$$T^* = \frac{n+1}{n} X_{(n)}$$

is strictly unbiased for $\theta$. Its variance is:

$$\text{Var}(T^*) = \left( \frac{n+1}{n} \right)^2 \text{Var}(X_{(n)}) = \left( \frac{n+1}{n} \right)^2 \frac{n \theta^2}{(n+1)^2 (n+2)} = \frac{\theta^2}{n(n+2)}$$

Notice that for $n \ge 2$:

$$\text{Var}(T^*) = \frac{\theta^2}{n(n+2)} < \frac{\theta^2}{n} = \frac{1}{I_n(\theta)}$$

The variance of $T^*$ is strictly smaller than the supposed Cramér–Rao bound! Indeed, as $n \to \infty$, the variance decays at rate $\mathcal{O}(1/n^2)$, far faster than the regular parametric rate $\mathcal{O}(1/n)$. The breakdown occurs because Leibniz's integral rule for variable boundaries states:

$$\frac{d}{d\theta} \int_0^\theta T(x) f(x; \theta) \, dx = \int_0^\theta T(x) \frac{\partial f}{\partial \theta} \, dx + T(\theta) f(\theta; \theta)$$

The boundary term $T(\theta) f(\theta; \theta) = \frac{T(\theta)}{\theta} \ne 0$ introduces a non-zero jump that completely destroys Bartlett's first identity and the Cauchy–Schwarz covariance derivation. Hence, standard information inequalities strictly require invariant supports.

## 2.2 The Score Function and Bartlett's First and Second Identities

The central mathematical object mediating information inequalities is the **Score Function**. For a sample $\mathbf{X} \in \mathcal{X}$, the score function $S(\theta; \mathbf{X})$ is defined as the gradient of the log-likelihood function:

$$S(\theta; \mathbf{X}) = \frac{\partial}{\partial \theta} \ln f(\mathbf{X}; \theta) = \frac{\frac{\partial}{\partial \theta} f(\mathbf{X}; \theta)}{f(\mathbf{X}; \theta)}$$

When evaluated at the true parameter $\theta$, the score is a random variable reflecting the localized rate of change of the probability density.

### Bartlett's First Identity: Zero Mean of the Score
Under regularity conditions (R0)-(R3), the expectation of the score function is identically zero across the entire parameter space:

$$\mathbb{E}_\theta[S(\theta; \mathbf{X})] = 0 \quad \forall \theta \in \Theta$$

#### Proof:
Differentiate both sides of the identity $\int_\mathcal{X} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 1$ with respect to $\theta$:

$$\int_\mathcal{X} \frac{\partial}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 0$$

Multiply and divide the integrand by $f(\mathbf{x}; \theta)$ on the support $\mathcal{S}$:

$$\int_\mathcal{X} \left( \frac{\frac{\partial}{\partial \theta} f(\mathbf{x}; \theta)}{f(\mathbf{x}; \theta)} \right) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = \int_\mathcal{X} S(\theta; \mathbf{x}) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = \mathbb{E}_\theta[S(\theta; \mathbf{X})] = 0$$

### Fisher Information
Because the score has expectation zero, its variance equals its second raw moment. The **Fisher Information** $I(\theta)$ contained in the sample $\mathbf{X}$ is defined as:

$$I(\theta) = \text{Var}_\theta(S(\theta; \mathbf{X})) = \mathbb{E}_\theta\left[ S(\theta; \mathbf{X})^2 \right] = \mathbb{E}_\theta\left[ \left( \frac{\partial}{\partial \theta} \ln f(\mathbf{X}; \theta) \right)^2 \right]$$

### Bartlett's Second Identity: Curvature Representation of Information
If the density is twice continuously differentiable with respect to $\theta$ and differentiation can be interchanged twice with integration, Fisher Information can be computed alternatively as the negative expectation of the second derivative of the log-likelihood (the curvature of the log-likelihood surface):

$$I(\theta) = -\mathbb{E}_\theta\left[ \frac{\partial^2}{\partial \theta^2} \ln f(\mathbf{X}; \theta) \right]$$

#### Proof:
Differentiate Bartlett's first identity $\int_\mathcal{X} \frac{\partial \ln f(\mathbf{x}; \theta)}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 0$ with respect to $\theta$:

$$\frac{d}{d\theta} \int_\mathcal{X} \frac{\partial \ln f(\mathbf{x}; \theta)}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 0$$

Interchanging derivative and integral:

$$\int_\mathcal{X} \frac{\partial}{\partial \theta} \left( \frac{\partial \ln f(\mathbf{x}; \theta)}{\partial \theta} f(\mathbf{x}; \theta) \right) d\mu(\mathbf{x}) = 0$$

Apply the product rule of calculus to the integrand:

$$\int_\mathcal{X} \left[ \frac{\partial^2 \ln f(\mathbf{x}; \theta)}{\partial \theta^2} f(\mathbf{x}; \theta) + \frac{\partial \ln f(\mathbf{x}; \theta)}{\partial \theta} \frac{\partial f(\mathbf{x}; \theta)}{\partial \theta} \right] d\mu(\mathbf{x}) = 0$$

Substitute $\frac{\partial f(\mathbf{x}; \theta)}{\partial \theta} = \frac{\partial \ln f(\mathbf{x}; \theta)}{\partial \theta} f(\mathbf{x}; \theta)$ into the second term:

$$\int_\mathcal{X} \frac{\partial^2 \ln f(\mathbf{x}; \theta)}{\partial \theta^2} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) + \int_\mathcal{X} \left( \frac{\partial \ln f(\mathbf{x}; \theta)}{\partial \theta} \right)^2 f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = 0$$

Writing in expectation notation:

$$\mathbb{E}_\theta\left[ \frac{\partial^2 \ln f(\mathbf{X}; \theta)}{\partial \theta^2} \right] + \mathbb{E}_\theta\left[ S(\theta; \mathbf{X})^2 \right] = 0$$

Rearranging immediately yields:

$$I(\theta) = -\mathbb{E}_\theta\left[ \frac{\partial^2}{\partial \theta^2} \ln f(\mathbf{X}; \theta) \right]$$

This curvature representation is profoundly useful both computationally and conceptually. When the log-likelihood peak is sharply pointed and highly curved, its second derivative is large and negative, meaning that the Fisher Information is large, data discriminate sharply between candidate parameters, and estimators can achieve high precision.

### Additivity of Fisher Information for Independent Observations
If $\mathbf{X} = (X_1, X_2, \dots, X_n)$ is an i.i.d. random sample with common density $f_1(x; \theta)$, the joint log-likelihood is:

$$\ln f_n(\mathbf{X}; \theta) = \sum_{i=1}^n \ln f_1(X_i; \theta)$$

The joint score function is the sum of the individual scores:

$$S_n(\theta; \mathbf{X}) = \sum_{i=1}^n S_1(\theta; X_i)$$

Because the observations are mutually independent, the score components $S_1(\theta; X_i)$ are independent random variables with mean zero. Taking the variance:

$$I_n(\theta) = \text{Var}_\theta\left( \sum_{i=1}^n S_1(\theta; X_i) \right) = \sum_{i=1}^n \text{Var}_\theta(S_1(\theta; X_i)) = n I_1(\theta)$$

The total sample Fisher Information grows strictly linearly with sample size $n$.

## 2.3 Derivation of the Cramér–Rao Lower Bound (CRLB) via Cauchy–Schwarz in L2 Space

We now present the rigorous proof of the Cramér–Rao Lower Bound using the geometric structure of the Hilbert space $L^2(P_\theta)$ of square-integrable random variables equipped with the inner product $\langle U, V \rangle = \mathbb{E}_\theta[UV]$.

### Theorem: The Cramér-Rao Lower Bound (Scalar Parameter)
Let $\mathbf{X} \sim f(\mathbf{x}; \theta)$ satisfy the regularity conditions (R0)-(R4). Let $T(\mathbf{X})$ be any estimator of a differentiable parametric function $\tau(\theta)$ such that $\mathbb{E}_\theta[T^2] < \infty$. Let $m(\theta) = \mathbb{E}_\theta[T(\mathbf{X})]$. Then:

$$\text{Var}_\theta(T(\mathbf{X})) \ge \frac{[m'(\theta)]^2}{I_n(\theta)}$$

In particular, if $T(\mathbf{X})$ is an **unbiased estimator** of $\tau(\theta)$, so that $m(\theta) = \tau(\theta)$ and $m'(\theta) = \tau'(\theta)$, then:

$$\text{Var}_\theta(T(\mathbf{X})) \ge \frac{[\tau'(\theta)]^2}{I_n(\theta)}$$

If the target parameter is $\theta$ itself, $\tau(\theta) = \theta$, $\tau'(\theta) = 1$, and the lower bound simplifies to:

$$\text{Var}_\theta(T(\mathbf{X})) \ge \frac{1}{I_n(\theta)} = \frac{1}{n I_1(\theta)}$$

#### Proof:
Consider the covariance between the estimator $T(\mathbf{X})$ and the score function $S_n(\theta; \mathbf{X})$:

$$\text{Cov}_\theta(T, S_n) = \mathbb{E}_\theta[T \, S_n] - \mathbb{E}_\theta[T] \mathbb{E}_\theta[S_n]$$

Since $\mathbb{E}_\theta[S_n] = 0$ by Bartlett's first identity:

$$\text{Cov}_\theta(T, S_n) = \mathbb{E}_\theta[T(\mathbf{X}) S_n(\theta; \mathbf{X})] = \int_\mathcal{X} T(\mathbf{x}) \left( \frac{\frac{\partial}{\partial \theta} f(\mathbf{x}; \theta)}{f(\mathbf{x}; \theta)} \right) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x})$$

$$= \int_\mathcal{X} T(\mathbf{x}) \frac{\partial}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x})$$

By regularity condition (R3), we can interchange differentiation and integration:

$$\int_\mathcal{X} T(\mathbf{x}) \frac{\partial}{\partial \theta} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = \frac{d}{d\theta} \int_\mathcal{X} T(\mathbf{x}) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = \frac{d}{d\theta} \mathbb{E}_\theta[T(\mathbf{X})] = m'(\theta)$$

Now, by the Cauchy–Schwarz inequality for real random variables:

$$[\text{Cov}_\theta(T, S_n)]^2 \le \text{Var}_\theta(T) \cdot \text{Var}_\theta(S_n)$$

Substitute the derived covariance $\text{Cov}_\theta(T, S_n) = m'(\theta)$ and score variance $\text{Var}_\theta(S_n) = I_n(\theta)$:

$$[m'(\theta)]^2 \le \text{Var}_\theta(T) \cdot I_n(\theta)$$

Dividing both sides by $I_n(\theta) > 0$ yields the celebrated inequality:

$$\text{Var}_\theta(T) \ge \frac{[m'(\theta)]^2}{I_n(\theta)}$$

This completes the proof.

### Geometric Interpretation in Hilbert Space $L^2(P_\theta)$
The Cauchy–Schwarz derivation admits an illuminating geometric interpretation within the Hilbert space of zero-mean square-integrable random variables $\mathcal{H} = \{ U : \mathbb{E}_\theta[U] = 0, \mathbb{E}_\theta[U^2] < \infty \}$ equipped with inner product $\langle U, V \rangle = \text{Cov}_\theta(U, V) = \mathbb{E}_\theta[UV]$ and norm $\|U\| = \sqrt{\text{Var}_\theta(U)}$.

In this space:
- The centered estimator $T_0(\mathbf{X}) = T(\mathbf{X}) - m(\theta)$ is a vector in $\mathcal{H}$ with length $\|T_0\| = \sqrt{\text{Var}_\theta(T)}$.
- The sample score function $S_n(\theta; \mathbf{X})$ is a vector in $\mathcal{H}$ with length $\|S_n\| = \sqrt{I_n(\theta)}$.
- The inner product is $\langle T_0, S_n \rangle = \text{Cov}_\theta(T, S_n) = m'(\theta)$.

The correlation coefficient between the estimator and the score is the cosine of the angle $\phi$ between these two vectors in $\mathcal{H}$:

$$\cos(\phi) = \frac{\langle T_0, S_n \rangle}{\|T_0\| \|S_n\|} = \frac{m'(\theta)}{\sqrt{\text{Var}_\theta(T)} \sqrt{I_n(\theta)}}$$

Because $|\cos(\phi)| \le 1$ for any geometric angle, squaring both sides yields:

$$\cos^2(\phi) = \frac{[m'(\theta)]^2}{\text{Var}_\theta(T) I_n(\theta)} \le 1 \implies \text{Var}_\theta(T) \ge \frac{[m'(\theta)]^2}{I_n(\theta)}$$

The efficiency of an unbiased estimator is nothing other than $\text{eff}_\theta(T) = \cos^2(\phi)$! An estimator is fully efficient ($\text{eff}_\theta(T) = 1$) if and only if the angle $\phi = 0$ or $\pi$, which means the estimator vector lies directly along the one-dimensional subspace spanned by the score function vector. Any component of $T_0$ orthogonal to the score function represents extraneous, uninformative sampling variability that inflates the variance without contributing to the estimation of $\theta$.

## 2.4 Extension to Biased Estimators and Information Trade-Offs

The Cramér–Rao inequality extends naturally to biased estimators. Suppose an estimator $T(\mathbf{X})$ has bias $b(\theta) = \mathbb{E}_\theta[T] - \theta$. Then its expectation is:

$$m(\theta) = \theta + b(\theta)$$

Differentiating with respect to $\theta$:

$$m'(\theta) = 1 + b'(\theta)$$

Substituting into the general Cramér–Rao bound yields:

$$\text{Var}_\theta(T) \ge \frac{[1 + b'(\theta)]^2}{I_n(\theta)}$$

Consequently, the Mean Squared Error of any biased estimator satisfies the inequality:

$$\text{MSE}_\theta(T) = \text{Var}_\theta(T) + [b(\theta)]^2 \ge \frac{[1 + b'(\theta)]^2}{I_n(\theta)} + [b(\theta)]^2$$

### The Derivative of the Bias and Super-Precision
Notice an essential mathematical subtlety: if an estimator has a negative bias slope $b'(\theta) < 0$, the numerator $[1 + b'(\theta)]^2$ is strictly less than $1$! For example, if $b'(\theta) = -0.5$, then $[1 + b'(\theta)]^2 = 0.25$, allowing the variance of $T$ to be four times smaller than $\frac{1}{I_n(\theta)}$.

### Deep Comparison of Biased Sample Variance Estimators
To observe the biased Cramér–Rao bound in action, consider an i.i.d. normal sample $X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2)$ where $\mu$ is unknown. Consider the family of estimators for $\sigma^2$:

$$S_k^2 = rac{1}{k} \sum_{i=1}^n (X_i - ar{X})^2$$

Because $rac{\sum (X_i - ar{X})^2}{\sigma^2} \sim \chi_{n-1}^2$, we know that $\mathbb{E}[S_k^2] = rac{n-1}{k} \sigma^2$ and $	ext{Var}(S_k^2) = rac{2(n-1)}{k^2} \sigma^4$.
1. **Unbiased Estimator ($k = n - 1$)**:
   $$\mathbb{E}[S_{n-1}^2] = \sigma^2, \quad 	ext{Bias} = 0, \quad 	ext{Var}(S_{n-1}^2) = rac{2\sigma^4}{n-1}, \quad 	ext{MSE} = rac{2\sigma^4}{n-1}$$
   Notice that the single-sample Fisher Information for $\sigma^2$ is $I_1(\sigma^2) = rac{1}{2\sigma^4}$, so the unbiased CRLB is $rac{2\sigma^4}{n}$. The variance of $S_{n-1}^2$ is $rac{2\sigma^4}{n-1} > rac{2\sigma^4}{n}$ because $\mu$ is unknown (a 1 degree of freedom penalty for estimating $\mu$).
2. **Maximum Likelihood Estimator ($k = n$)**:
   $$\mathbb{E}[S_n^2] = rac{n-1}{n} \sigma^2, \quad 	ext{Bias} = -rac{\sigma^2}{n}, \quad b'(\sigma^2) = -rac{1}{n}$$
   The biased Cramér–Rao lower bound for an estimator with this expectation $m(\sigma^2) = rac{n-1}{n} \sigma^2$ is:
   $$rac{[m'(\sigma^2)]^2}{I_n(\sigma^2)} = rac{\left( rac{n-1}{n} 
ight)^2}{rac{n}{2\sigma^4}} = rac{2(n-1)^2 \sigma^4}{n^3}$$
   The actual variance is $	ext{Var}(S_n^2) = rac{2(n-1)}{n^2} \sigma^4$.
   The Mean Squared Error of the MLE is:
   $$	ext{MSE}(S_n^2) = rac{2(n-1)}{n^2} \sigma^4 + \left(-rac{\sigma^2}{n}
ight)^2 = rac{2n - 2 + 1}{n^2} \sigma^4 = rac{2n - 1}{n^2} \sigma^4$$
3. **Minimum MSE Shrinkage Estimator ($k = n + 1$)**:
   Minimizing $	ext{MSE}(S_k^2) = rac{2(n-1)}{k^2} \sigma^4 + \left(rac{n-1-k}{k}
ight)^2 \sigma^4$ with respect to $k$ yields $k^* = n + 1$.
   The resulting estimator $S_{n+1}^2$ achieves the strictly minimal MSE:
   $$	ext{MSE}(S_{n+1}^2) = rac{2}{n+1} \sigma^4 < rac{2n-1}{n^2} \sigma^4 < rac{2}{n-1} \sigma^4$$
   The biased estimator $S_{n+1}^2$ completely dominates the classical unbiased estimator $S_{n-1}^2$ across every single sample size $n \ge 2$ and for every true variance $\sigma^2 > 0$!

## 2.5 Attainment Conditions: Linear Score and 1-Parameter Exponential Families

When does an unbiased estimator achieve the Cramér–Rao Lower Bound with strict mathematical equality? Understanding this question connects information theory directly to the structure of exponential families.

### Theorem: Exact CRLB Attainment Condition
Equality holds in the Cauchy–Schwarz inequality if and only if one of the random variables is a deterministic linear transformation of the other almost everywhere. Therefore, for an unbiased estimator $T(\mathbf{X})$ of $\tau(\theta)$, equality:

$$\text{Var}_\theta(T(\mathbf{X})) = \frac{[\tau'(\theta)]^2}{I_n(\theta)}$$

holds for all $\theta \in \Theta$ if and only if there exists a deterministic scalar function $k(\theta)$ (independent of $\mathbf{x}$) such that the score function can be written as:

$$S_n(\theta; \mathbf{X}) = \frac{\partial}{\partial \theta} \ln f_n(\mathbf{X}; \theta) = k(\theta) \left[ T(\mathbf{X}) - \tau(\theta) \right] \quad \text{a.e.}$$

Furthermore, integrating both sides of this equation with respect to $\theta$ reveals the exact analytical form of the underlying probability distribution:

$$\ln f_n(\mathbf{X}; \theta) = T(\mathbf{X}) \int k(\theta) \, d\theta - \int k(\theta) \tau(\theta) \, d\theta + C(\mathbf{X})$$

Exponentiating both sides yields:

$$f_n(\mathbf{X}; \theta) = \exp\left( \eta(\theta) T(\mathbf{X}) - B(\theta) + C(\mathbf{X}) \right)$$

where $\eta(\theta) = \int k(\theta) \, d\theta$ and $B(\theta) = \int k(\theta) \tau(\theta) \, d\theta$.

### Conclusion on Attainment
This is the canonical definition of a **one-parameter natural exponential family**!
We have established a profound foundational theorem:
**An unbiased estimator $T(\mathbf{X})$ can achieve the Cramér–Rao Lower Bound if and only if the underlying distribution belongs to the one-parameter exponential family, and the parameter being estimated is $\tau(\theta) = \mathbb{E}_\theta[T(\mathbf{X})]$.**

If the distribution does not belong to an exponential family (e.g., Cauchy or Student's $t$), or if the parametric target $\tau(\theta)$ is a non-linear function of the natural parameter expectation (e.g., estimating $\sigma = \sqrt{\sigma^2}$ in a Gaussian model), the CRLB is strictly unattainable for finite samples! In such cases, the UMVUE exists, but its finite-sample variance lies strictly above the CRLB.

## 2.6 Multiparameter Fisher Information Matrix and Vector Cramér-Rao Inequality

In real-world scientific problems, experiments typically involve multiple unknown parameters simultaneously, such as the mean and variance $(\mu, \sigma^2)$ of a Gaussian distribution, or multiple regression coefficients $\boldsymbol{\beta} \in \mathbb{R}^p$.

Let $\boldsymbol{\theta} = (\theta_1, \theta_2, \dots, \theta_k)^T \in \Theta \subseteq \mathbb{R}^k$. The **Score Vector** is defined as the gradient:

$$\mathbf{S}(\boldsymbol{\theta}; \mathbf{X}) = \nabla_{\boldsymbol{\theta}} \ln f(\mathbf{X}; \boldsymbol{\theta}) = \begin{pmatrix} \frac{\partial \ln f}{\partial \theta_1} \\ \vdots \\ \frac{\partial \ln f}{\partial \theta_k} \end{pmatrix}$$

By multivariate Bartlett identities, $\mathbb{E}_{\boldsymbol{\theta}}[\mathbf{S}] = \mathbf{0}$. The **Fisher Information Matrix** $\mathbf{I}(\boldsymbol{\theta}) \in \mathbb{R}^{k \times k}$ is the $k \times k$ covariance matrix of the score vector:

$$\mathbf{I}(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}\left[ \mathbf{S}(\boldsymbol{\theta}; \mathbf{X}) \mathbf{S}(\boldsymbol{\theta}; \mathbf{X})^T \right] = -\mathbb{E}_{\boldsymbol{\theta}}\left[ \mathcal{H}_{\boldsymbol{\theta}}(\ln f(\mathbf{X}; \boldsymbol{\theta})) \right]$$

with matrix entries:

$$I_{ij}(\boldsymbol{\theta}) = -\mathbb{E}_{\boldsymbol{\theta}}\left[ \frac{\partial^2 \ln f(\mathbf{X}; \boldsymbol{\theta})}{\partial \theta_i \partial \theta_j} \right]$$

### Theorem: The Multiparameter Cramér-Rao Inequality
Let $\mathbf{T}(\mathbf{X}) = (T_1, \dots, T_m)^T$ be an unbiased estimator of a vector parametric function $\boldsymbol{\tau}(\boldsymbol{\theta}) = (\tau_1(\boldsymbol{\theta}), \dots, \tau_m(\boldsymbol{\theta}))^T$. Let $\mathbf{D}(\boldsymbol{\theta}) \in \mathbb{R}^{m \times k}$ denote the Jacobian matrix of partial derivatives:

$$D_{ij}(\boldsymbol{\theta}) = \frac{\partial \tau_i(\boldsymbol{\theta})}{\partial \theta_j}$$

Assume that the Fisher Information matrix $\mathbf{I}(\boldsymbol{\theta})$ is non-singular and invertible. Then the covariance matrix of $\mathbf{T}(\mathbf{X})$, denoted $\boldsymbol{\Sigma}_{\mathbf{T}}$, satisfies the matrix Loewner order inequality:

$$\boldsymbol{\Sigma}_{\mathbf{T}} - \mathbf{D}(\boldsymbol{\theta}) \mathbf{I}(\boldsymbol{\theta})^{-1} \mathbf{D}(\boldsymbol{\theta})^T \ge 0$$

That is, the difference matrix is positive semi-definite. In particular, for estimating a single scalar parameter $\theta_i$ in the presence of nuisance parameters $\theta_j$ ($j \ne i$), the lower bound is given by the diagonal element of the inverted Fisher Information matrix:

$$\text{Var}(T_i) \ge [\mathbf{I}(\boldsymbol{\theta})^{-1}]_{ii}$$

### The Cost of Nuisance Parameters
A remarkable matrix property holds for any positive-definite symmetric block matrix. Partition the Fisher Information matrix as:

$$\mathbf{I}(\boldsymbol{\theta}) = \begin{pmatrix} I_{11} & \mathbf{I}_{12} \\ \mathbf{I}_{21} & \mathbf{I}_{22} \end{pmatrix}$$

By the block matrix inversion theorem (Schur complement):

$$[\mathbf{I}(\boldsymbol{\theta})^{-1}]_{11} = (I_{11} - \mathbf{I}_{12} \mathbf{I}_{22}^{-1} \mathbf{I}_{21})^{-1}$$

Because $\mathbf{I}_{22}$ is positive-definite, the quadratic form $\mathbf{I}_{12} \mathbf{I}_{22}^{-1} \mathbf{I}_{21} \ge 0$. Consequently:

$$I_{11} - \mathbf{I}_{12} \mathbf{I}_{22}^{-1} \mathbf{I}_{21} \le I_{11} \implies [\mathbf{I}(\boldsymbol{\theta})^{-1}]_{11} \ge \frac{1}{I_{11}}$$

### Parameter Orthogonality and the Cox–Reid Transformation
In statistical design and inference, two parameters $\theta_1$ and $\theta_2$ are defined to be **information-orthogonal** if their off-diagonal Fisher Information entry vanishes identically:

$$I_{12}(\boldsymbol{\theta}) = \mathbb{E}\left[ -\frac{\partial^2 \ln f}{\partial \theta_1 \partial \theta_2} \right] = 0 \quad \forall \boldsymbol{\theta} \in \Theta$$

When parameters are orthogonal, the Fisher Information matrix is block-diagonal. This orthogonality yields several profound inferential benefits:
1. **Zero Efficiency Penalty**: The Cramér–Rao Lower Bound for $\theta_1$ in the presence of unknown $\theta_2$ is identical to the bound when $\theta_2$ is known: $[\mathbf{I}(\boldsymbol{\theta})^{-1}]_{11} = \frac{1}{I_{11}}$.
2. **Asymptotic Independence**: Maximum likelihood estimators $\hat{\theta}_1$ and $\hat{\theta}_2$ are asymptotically independent and uncorrelated.
3. **Robustness to Nuisance Mis-specification**: Slight errors in estimating $\theta_2$ exert second-order rather than first-order effects on the estimation of $\theta_1$.

Cox and Reid (1987) demonstrated that for any scalar parameter of interest $\theta_1$ and scalar nuisance parameter $\lambda$, one can systematically construct an orthogonal reparameterization $\psi = \psi(\theta_1, \lambda)$ by solving the partial differential equation:

$$\frac{\partial \lambda}{\partial \theta_1} = -\frac{I_{\theta_1 \lambda}}{I_{\lambda \lambda}}$$

Integrating this characteristic equation yields an orthogonal coordinate system where nuisance parameter uncertainty is cleanly decoupled from the target parameter.

## 2.7 Reparameterization and the Delta Method in CRLB Calculations

How does Fisher Information behave when we change coordinates? Let $\boldsymbol{\psi} = \mathbf{g}(\boldsymbol{\theta})$ be a smooth, invertible, one-to-one reparameterization with non-singular Jacobian matrix $\mathbf{J} = \frac{\partial \boldsymbol{\theta}}{\partial \boldsymbol{\psi}}$.

By the chain rule of multivariable calculus:

$$\frac{\partial \ln f}{\partial \psi_i} = \sum_{j=1}^k \frac{\partial \ln f}{\partial \theta_j} \frac{\partial \theta_j}{\partial \psi_i}$$

In vector notation:

$$\mathbf{S}_\psi = \mathbf{J}^T \mathbf{S}_\theta$$

Taking the covariance matrix of both sides:

$$\mathbf{I}_\psi(\boldsymbol{\psi}) = \mathbb{E}\left[ \mathbf{S}_\psi \mathbf{S}_\psi^T \right] = \mathbf{J}^T \mathbb{E}\left[ \mathbf{S}_\theta \mathbf{S}_\theta^T \right] \mathbf{J} = \mathbf{J}^T \mathbf{I}_\theta(\boldsymbol{\theta}) \mathbf{J}$$

Inverting both sides:

$$\mathbf{I}_\psi(\boldsymbol{\psi})^{-1} = \mathbf{J}^{-1} \mathbf{I}_\theta(\boldsymbol{\theta})^{-1} (\mathbf{J}^T)^{-1} = \left( \frac{\partial \boldsymbol{\psi}}{\partial \boldsymbol{\theta}} \right) \mathbf{I}_\theta(\boldsymbol{\theta})^{-1} \left( \frac{\partial \boldsymbol{\psi}}{\partial \boldsymbol{\theta}} \right)^T$$

This matches the asymptotic covariance matrix obtained from the Delta Method! Fisher Information transforms covariantly as a tensor metric of rank 2, exactly as in Riemannian differential geometry.

### Variance-Stabilizing Transformations via Information Geometry
A classic problem in statistical methodology is finding a transformation $g(\theta)$ such that the asymptotic variance of $g(\hat{\theta})$ is completely constant and independent of the true parameter $\theta$.
By the Delta Method:

$$\text{Var}(g(\hat{\theta})) \approx [g'(\theta)]^2 \text{Var}(\hat{\theta}) \approx \frac{[g'(\theta)]^2}{n I_1(\theta)}$$

To make this asymptotic variance equal to a constant $c^2$ independent of $\theta$, we set:

$$\frac{[g'(\theta)]^2}{I_1(\theta)} = c^2 \implies g'(\theta) = c \sqrt{I_1(\theta)}$$

Integrating both sides yields the canonical **Variance-Stabilizing Transformation**:

$$g(\theta) = c \int \sqrt{I_1(\theta)} \, d\theta$$

Notice that $\sqrt{I_1(\theta)} \, d\theta$ is precisely the infinitesimal line element $ds$ of the Fisher Information Riemannian metric!
Canonical examples derived directly from this information integral include:
1. **Poisson Rate $\lambda$**: $I_1(\lambda) = \frac{1}{\lambda}$. Then $g(\lambda) = \int \lambda^{-1/2} \, d\lambda = 2\sqrt{\lambda}$. Thus the square-root transform $\sqrt{X}$ has asymptotic variance $\frac{1}{4}$ independent of $\lambda$.
2. **Binomial Proportion $p$**: $I_1(p) = \frac{1}{p(1-p)}$. Then $g(p) = \int \frac{1}{\sqrt{p(1-p)}} \, dp = 2 \arcsin(\sqrt{p})$. Thus the angular transform $\arcsin(\sqrt{\hat{p}})$ stabilizes variance to $\frac{1}{4n}$.
3. **Bivariate Normal Correlation $\rho$**: $I_1(\rho) = \frac{1}{(1 - \rho^2)^2}$. Then $g(\rho) = \int \frac{1}{1 - \rho^2} \, d\rho = \frac{1}{2} \ln\left( \frac{1 + \rho}{1 - \rho} \right) = \text{arctanh}(\rho)$. This is Fisher's celebrated $z$-transformation, which stabilizes the sampling variance of Pearson's $r$ to $\frac{1}{n - 3}$.


### Differential Geometry of the Fisher Information Metric
In 1945, C. R. Rao made the groundbreaking observation that the Fisher Information matrix acts as a Riemannian metric tensor on the manifold of probability distributions.
Let $\mathcal{M} = \{P_\theta : \theta \in \Theta\}$ be a family of probability measures satisfying regularity conditions. The tangent space at $\theta$ is spanned by the score vectors $\frac{\partial \ln f}{\partial \theta_i}$.
The Riemannian metric tensor is given by:

$$g_{ij}(\theta) = I_{ij}(\theta) = \mathbb{E}_\theta\left[ \frac{\partial \ln f}{\partial \theta_i} \frac{\partial \ln f}{\partial \theta_j} \right]$$

The geodesic distance between two probability measures $P_{\theta_1}$ and $P_{\theta_2}$ along the statistical manifold is the **Rao Distance**:

$$D_{\text{Rao}}(P_{\theta_1}, P_{\theta_2}) = \int_0^1 \sqrt{ \sum_{i,j} g_{ij}(\theta(t)) \frac{d\theta_i}{dt} \frac{d\theta_j}{dt} } \, dt$$

For Gaussian location-scale distributions $\mathcal{N}(\mu, \sigma^2)$, the Fisher Information metric is:

$$ds^2 = \frac{d\mu^2 + 2 d\sigma^2}{\sigma^2}$$

This is the Poincaré upper half-plane metric of **hyperbolic geometry** with constant negative curvature $K = -1/2$!
This geometric insight reveals that statistical distinguishability between distributions behaves like hyperbolic distance in non-Euclidean geometry: distributions with small $\sigma$ are far apart even for tiny differences in $\mu$, whereas distributions with large $\sigma$ are tightly clustered together.

## 2.8 Higher-Order Information Bounds: The Bhattacharyya Hierarchy

When the Cramér–Rao bound is strictly unattainable because the target function $\tau(\theta)$ is non-linear or the density does not admit a linear score, can we establish tighter, higher-order lower bounds?

In 1946, A. Bhattacharyya developed a sequence of ascending lower bounds that generalizes the Cramér–Rao inequality by considering higher-order derivatives of the likelihood.

### Definition of Bhattacharyya Bounds
Define the higher-order score functions:

$$S^{(k)}(\theta; \mathbf{X}) = \frac{1}{f(\mathbf{X}; \theta)} \frac{\partial^k}{\partial \theta^k} f(\mathbf{X}; \theta), \quad k = 1, 2, \dots, K$$

Notice that $S^{(1)}(\theta; \mathbf{X}) = \frac{\partial \ln f}{\partial \theta}$ is the standard Fisher score. The Bhattacharyya information matrix $\mathbf{W} \in \mathbb{R}^{K \times K}$ has entries:

$$W_{ij} = \text{Cov}_\theta(S^{(i)}, S^{(j)}) = \mathbb{E}_\theta\left[ S^{(i)}(\theta; \mathbf{X}) S^{(j)}(\theta; \mathbf{X}) \right]$$

For an unbiased estimator $T(\mathbf{X})$ of $\tau(\theta)$, define the derivative vector:

$$\mathbf{v} = \left( \tau'(\theta), \tau''(\theta), \dots, \tau^{(K)}(\theta) \right)^T$$

The $K$-th order **Bhattacharyya Lower Bound** is given by the quadratic form:

$$\text{Var}_\theta(T(\mathbf{X})) \ge \mathbf{v}^T \mathbf{W}^{-1} \mathbf{v}$$

For $K = 1$, $\mathbf{W} = I_n(\theta)$ and $\mathbf{v} = \tau'(\theta)$, which reproduces the classical Cramér–Rao bound. For $K = 2$:

$$\text{Var}_\theta(T) \ge \frac{[\tau'(\theta)]^2}{I_n(\theta)} + \frac{\left( \tau''(\theta) - \frac{W_{12}}{I_n} \tau'(\theta) \right)^2}{W_{22} - \frac{W_{12}^2}{I_n}} \ge \text{CRLB}$$

Because the Bhattacharyya bounds incorporate higher-order moments of the likelihood curvature, they form a monotonically non-decreasing sequence:

$$\text{CRLB} = B_1(\theta) \le B_2(\theta) \le B_3(\theta) \le \dots \le \text{Var}_\theta(T_{\text{UMVUE}})$$

In many classical models (such as estimating $\sigma^4$ or $\mu^2$ in Gaussian samples), the sequence of Bhattacharyya bounds converges precisely to the exact variance of the UMVUE.

## 2.9 Chapman-Robbins and Hammersley-Chapman-Robbins Non-Regular Information Bounds

The classical Cramér–Rao bound requires differentiability of the density with respect to $\theta$ and an invariant support $\mathcal{S}$. When these regularity conditions fail—such as for the Uniform distribution $\text{Uniform}(0, \theta)$ where the support $[0, \theta]$ depends explicitly on $\theta$—the CRLB is inapplicable.

To overcome this fundamental limitation, D. G. Chapman and H. Robbins (1951), building on work by J. M. Hammersley (1950), established an information bound that requires **zero differentiability conditions**.

### Theorem: The Chapman–Robbins Inequality
Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ be a family of probability measures. Let $T(\mathbf{X})$ be an unbiased estimator of $\tau(\theta)$ with finite variance. Let $\theta, \theta + \Delta \in \Theta$ be two distinct parameter points such that the support of $P_{\theta+\Delta}$ is contained within the support of $P_\theta$. Then:

$$\text{Var}_\theta(T(\mathbf{X})) \ge \sup_{\Delta \ne 0} \frac{[\tau(\theta + \Delta) - \tau(\theta)]^2}{\mathbb{E}_\theta\left[ \left( \frac{f(\mathbf{X}; \theta + \Delta)}{f(\mathbf{X}; \theta)} - 1 \right)^2 \right]}$$

#### Derivation for the Uniform Distribution:
Let $X_1, \dots, X_n \sim \text{Uniform}(0, \theta)$. To ensure the support condition holds, choose $\Delta < 0$, so that $[0, \theta + \Delta] \subset [0, \theta]$. The joint density ratio is:

$$\frac{f_n(\mathbf{x}; \theta + \Delta)}{f_n(\mathbf{x}; \theta)} = \frac{(\theta + \Delta)^{-n}}{\theta^{-n}} = \left( 1 + \frac{\Delta}{\theta} \right)^{-n}$$

provided $x_{(n)} \le \theta + \Delta$, and $0$ otherwise.
The expectation of the squared ratio is:

$$\mathbb{E}_\theta\left[ \left( \frac{f_n(\mathbf{X}; \theta + \Delta)}{f_n(\mathbf{X}; \theta)} \right)^2 \right] = \left( 1 + \frac{\Delta}{\theta} \right)^{-2n} \mathbb{P}_\theta(X_{(n)} \le \theta + \Delta) = \left( 1 + \frac{\Delta}{\theta} \right)^{-2n} \left( 1 + \frac{\Delta}{\theta} \right)^n = \left( 1 + \frac{\Delta}{\theta} \right)^{-n}$$

Subtracting $1$:

$$\mathbb{E}_\theta\left[ \left( \frac{f_n(\mathbf{X}; \theta + \Delta)}{f_n(\mathbf{X}; \theta)} - 1 \right)^2 \right] = \left( 1 + \frac{\Delta}{\theta} \right)^{-n} - 1$$

For estimating $\tau(\theta) = \theta$, the numerator is $\Delta^2$. Setting $\epsilon = -\Delta / \theta \in (0, 1)$:

$$\text{Var}_\theta(T) \ge \sup_{\epsilon \in (0, 1)} \frac{\theta^2 \epsilon^2}{(1 - \epsilon)^{-n} - 1}$$

Using Taylor expansion $(1 - \epsilon)^{-n} - 1 = n\epsilon + \frac{n(n+1)}{2} \epsilon^2 + \mathcal{O}(\epsilon^3)$ and optimizing over $\epsilon$, the supremum evaluates to:

$$\text{Var}_\theta(T) \ge \frac{\theta^2}{n(n+2)}$$

Remarkably, this bound exactly equals the variance of the UMVUE $T^* = \frac{n+1}{n} X_{(n)}$! The Chapman–Robbins inequality provides a non-trivial, sharp lower bound of order $\mathcal{O}(1/n^2)$ where classical Cramér–Rao theory fails completely.

## 2.10 Fisher Information in Censored, Truncated, and Grouped Data

In survival analysis, reliability engineering, and econometrics, data are frequently observed through imperfect observation windows:

### Mathematical Derivation for Type I Right Censoring
Let $X_1, \dots, X_n$ be i.i.d. failure times from an Exponential distribution $\text{Exp}(\theta)$ with density $f(x; \theta) = \theta e^{-\theta x}$ and survival function $S(x; \theta) = e^{-\theta x}$. The experiment terminates at a fixed censoring threshold $C > 0$. For each unit $i$, we observe:

$$Y_i = \min(X_i, C), \quad \delta_i = \mathbf{1}_{\{X_i \le C\}}$$

The likelihood contribution of an observation is:

$$L_i(\theta) = [f(Y_i; \theta)]^{\delta_i} [S(C; \theta)]^{1 - \delta_i} = (\theta e^{-\theta Y_i})^{\delta_i} (e^{-\theta C})^{1 - \delta_i} = \theta^{\delta_i} e^{-\theta Y_i}$$

The log-likelihood for the sample is:

$$\ell_n(\theta) = \sum_{i=1}^n [\delta_i \ln(\theta) - \theta Y_i] = d \ln(\theta) - \theta \sum_{i=1}^n Y_i$$

where $d = \sum_{i=1}^n \delta_i$ is the random number of observed failures. Differentiating with respect to $\theta$:

$$\frac{\partial \ell_n}{\partial \theta} = \frac{d}{\theta} - \sum_{i=1}^n Y_i, \quad \frac{\partial^2 \ell_n}{\partial \theta^2} = -\frac{d}{\theta^2}$$

Taking the negative expectation:

$$I_n^{\text{cens}}(\theta) = -\mathbb{E}\left[ -\frac{d}{\theta^2} \right] = \frac{\mathbb{E}[d]}{\theta^2}$$

Because each $\delta_i \sim \text{Bernoulli}(p)$ with probability of failure $p = \mathbb{P}(X_i \le C) = 1 - e^{-\theta C}$, the expected number of failures is $\mathbb{E}[d] = n(1 - e^{-\theta C})$. Thus:

$$I_n^{\text{cens}}(\theta) = \frac{n(1 - e^{-\theta C})}{\theta^2} = (1 - e^{-\theta C}) I_n^{\text{uncens}}(\theta)$$

The Fisher Information under right censoring is directly proportional to the probability of observing an event! The quantity $e^{-\theta C} I_n^{\text{uncens}}(\theta)$ represents the exact information lost due to censoring.

### Fisher Information in Grouped and Quantized Data
In survey sampling and physical telemetry, continuous signals $X$ are frequently discretized into $K$ disjoint intervals $A_k = (a_{k-1}, a_k]$ with probabilities:

$$p_k(\theta) = \mathbb{P}_\theta(X \in A_k) = \int_{a_{k-1}}^{a_k} f(x; \theta) \, dx$$

For a sample of size $n$, the grouped observation is a count vector $(N_1, \dots, N_K) \sim 	ext{Multinomial}(n, p_1(	heta), \dots, p_K(	heta))$. The Fisher Information contained in the grouped data is:

$$I_n^{	ext{grouped}}(	heta) = \sum_{k=1}^K rac{1}{p_k(	heta)} \left( rac{\partial p_k(	heta)}{\partial 	heta} 
ight)^2 = \sum_{k=1}^K rac{\left( \int_{a_{k-1}}^{a_k} rac{\partial f(x; 	heta)}{\partial 	heta} \, dx 
ight)^2}{\int_{a_{k-1}}^{a_k} f(x; 	heta) \, dx}$$

Now, apply the Cauchy–Schwarz inequality to each interval integral:

$$\left( \int_{a_{k-1}}^{a_k} rac{\partial f}{\partial 	heta} \, dx 
ight)^2 = \left( \int_{a_{k-1}}^{a_k} rac{rac{\partial f}{\partial 	heta}}{\sqrt{f}} \cdot \sqrt{f} \, dx 
ight)^2 \le \left( \int_{a_{k-1}}^{a_k} \left( rac{\partial \ln f}{\partial 	heta} 
ight)^2 f \, dx 
ight) \left( \int_{a_{k-1}}^{a_k} f \, dx 
ight)$$

Dividing both sides by $\int_{a_{k-1}}^{a_k} f(x; 	heta) \, dx = p_k(	heta)$:

$$rac{1}{p_k(	heta)} \left( rac{\partial p_k(	heta)}{\partial 	heta} 
ight)^2 \le \int_{a_{k-1}}^{a_k} \left( rac{\partial \ln f(x; 	heta)}{\partial 	heta} 
ight)^2 f(x; 	heta) \, dx$$

Summing across all $K$ intervals:

$$I_n^{	ext{grouped}}(	heta) \le \sum_{k=1}^K \int_{a_{k-1}}^{a_k} \left( rac{\partial \ln f(x; 	heta)}{\partial 	heta} 
ight)^2 f(x; 	heta) \, dx = \int_{-\infty}^\infty \left( rac{\partial \ln f(x; 	heta)}{\partial 	heta} 
ight)^2 f(x; 	heta) \, dx = I_n^{	ext{continuous}}(	heta)$$

This proves that grouping or quantizing continuous measurements strictly destroys Fisher Information! The information gap vanishes only in the asymptotic continuum limit as the maximum bin mesh $\max_k |a_k - a_{k-1}| 	o 0$.

---


### Structural Comparison of Multiparameter Regularity Conditions
In multiparameter statistical estimation, establishing the attainability of the Cramér–Rao bound requires careful verification of regularity conditions over open subsets of Euclidean parameter spaces. When the parameter vector $\boldsymbol{\theta} = (\theta_1, \theta_2, \dots, \theta_k)^T$ lies in an open parameter manifold $\Theta \subseteq \mathbb{R}^k$, the Fisher information matrix is defined by the expected outer product of score vectors:

$$\mathbf{I}(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}\left[ \nabla_{\boldsymbol{\theta}} \ln f(\mathbf{X}; \boldsymbol{\theta}) \nabla_{\boldsymbol{\theta}} \ln f(\mathbf{X}; \boldsymbol{\theta})^T \right]$$

To guarantee that the inverse information matrix $\mathbf{I}(\boldsymbol{\theta})^{-1}$ exists and serves as a strict lower bound for the dispersion matrix of any unbiased vector estimator $\mathbf{T}(\mathbf{X})$, three fundamental conditions must hold simultaneously:
1. The support of the random vector $\mathbf{X}$, denoted by $\mathcal{X}_{\boldsymbol{\theta}} = \{\mathbf{x} : f(\mathbf{x}; \boldsymbol{\theta}) > 0\}$, must be strictly independent of all coordinates of $\boldsymbol{\theta}$. When the boundaries of the support depend on parameters (as in truncated distributions, shifted Pareto, or two-parameter uniform distributions), the classical score function exhibits delta-distribution singularities at the boundary, rendering the classical interchange of differentiation and integration invalid.
2. The partial derivatives $\frac{\partial f(\mathbf{x}; \boldsymbol{\theta})}{\partial \theta_j}$ must exist for almost all $\mathbf{x}$ with respect to the dominating measure, and must be dominated by Lebesgue-integrable functions over compact parameter neighborhoods. This domination property guarantees uniform integrability and justifies the application of the dominated convergence theorem.
3. The Fisher information matrix $\mathbf{I}(\boldsymbol{\theta})$ must be strictly positive definite everywhere on $\Theta$. Positive definiteness ensures that no linear combination of score components is almost surely zero, which is mathematically equivalent to the linear independence of the score coordinates and the absence of redundant or unidentifiable parameter directions.

When these conditions are met, the Chapman–Robbins inequality provides a non-differential lower bound that converges smoothly to the Cramér–Rao lower bound as the perturbation parameter approaches zero. This unifies differential and difference-quotient approaches to information theory.

## Fully worked question 1: CRLB Derivation and Attainment in Gamma and Pareto Models with Exact Attainment Conditions

### Question
An electrical engineering team monitors the operational lifespans of high-power gallium-nitride (GaN) transistors operating in a satellite communications system. Transistor failure times follow a two-parameter Gamma distribution with known shape parameter $\alpha_0 = 3$ and unknown scale parameter $\beta > 0$. The probability density function of an individual failure time $X$ is given by:

$$f(x; \beta) = \frac{1}{\Gamma(3) \beta^3} x^{3 - 1} e^{-x / \beta} = \frac{1}{2 \beta^3} x^2 e^{-x / \beta}, \quad x > 0$$

An independent, identically distributed random sample of failure times $\mathbf{X} = (X_1, X_2, \dots, X_n)$ is observed.

1. Write down the joint log-likelihood function $\ln f_n(\mathbf{X}; \beta)$, calculate the score function $S_n(\beta; \mathbf{X})$, and evaluate the Fisher Information $I_n(\beta)$ using both Bartlett's first identity (variance of the score) and Bartlett's second identity (negative expected curvature).
2. Determine the Cramér–Rao Lower Bound for any unbiased estimator of $\beta$. Show that the sample-based estimator $T_1(\mathbf{X}) = \frac{1}{3n} \sum_{i=1}^n X_i$ is an unbiased estimator of $\beta$, calculate its exact variance, and verify that it achieves the CRLB with equality.
3. Now suppose the engineers wish to estimate the mean time to failure (MTTF), which is $\tau_1(\beta) = \mathbb{E}[X] = 3\beta$, and the probability that a transistor survives past a critical operational mission threshold $t_0 > 0$, given by:
   $$\tau_2(\beta) = \mathbb{P}(X > t_0) = \int_{t_0}^\infty \frac{1}{2\beta^3} x^2 e^{-x/\beta} \, dx = e^{-t_0/\beta} \left( 1 + \frac{t_0}{\beta} + \frac{t_0^2}{2\beta^2} \right)$$
   Derive the CRLB for unbiased estimators of $\tau_1(\beta)$ and $\tau_2(\beta)$. Can any unbiased estimator of $\tau_2(\beta)$ attain the CRLB for finite $n$? Justify your answer using attainment theorems.

### Solution, step 1: Joint log-likelihood, score, and Fisher Information
The joint likelihood for an i.i.d. sample of size $n$ from the Gamma distribution is:

$$f_n(\mathbf{X}; \beta) = \prod_{i=1}^n \left( \frac{1}{2\beta^3} X_i^2 e^{-X_i / \beta} \right) = \frac{1}{2^n \beta^{3n}} \left( \prod_{i=1}^n X_i^2 \right) \exp\left( -\frac{1}{\beta} \sum_{i=1}^n X_i \right)$$

Taking the natural logarithm:

$$\ln f_n(\mathbf{X}; \beta) = -n \ln(2) - 3n \ln(\beta) + 2 \sum_{i=1}^n \ln(X_i) - \frac{1}{\beta} \sum_{i=1}^n X_i$$

Differentiating with respect to $\beta$ gives the Score function:

$$S_n(\beta; \mathbf{X}) = \frac{\partial}{\partial \beta} \ln f_n(\mathbf{X}; \beta) = -\frac{3n}{\beta} + \frac{1}{\beta^2} \sum_{i=1}^n X_i = \frac{1}{\beta^2} \left( \sum_{i=1}^n X_i - 3n\beta \right)$$

To calculate Fisher Information using Bartlett's second identity, compute the second derivative:

$$\frac{\partial^2}{\partial \beta^2} \ln f_n(\mathbf{X}; \beta) = \frac{3n}{\beta^2} - \frac{2}{\beta^3} \sum_{i=1}^n X_i$$

Taking the negative expected value:

$$I_n(\beta) = -\mathbb{E}_\beta\left[ \frac{\partial^2}{\partial \beta^2} \ln f_n(\mathbf{X}; \beta) \right] = -\frac{3n}{\beta^2} + \frac{2}{\beta^3} \sum_{i=1}^n \mathbb{E}[X_i]$$

Since each $X_i \sim \text{Gamma}(3, \beta)$, we have $\mathbb{E}[X_i] = 3\beta$. Therefore:

$$I_n(\beta) = -\frac{3n}{\beta^2} + \frac{2}{\beta^3} (n \cdot 3\beta) = -\frac{3n}{\beta^2} + \frac{6n}{\beta^2} = \frac{3n}{\beta^2}$$

Alternatively, using Bartlett's first identity:

$$I_n(\beta) = \text{Var}_\beta(S_n) = \text{Var}_\beta\left( \frac{1}{\beta^2} \sum_{i=1}^n X_i \right) = \frac{1}{\beta^4} \sum_{i=1}^n \text{Var}(X_i)$$

For $\text{Gamma}(3, \beta)$, the variance is $\text{Var}(X_i) = 3\beta^2$. Thus:

$$I_n(\beta) = \frac{1}{\beta^4} (n \cdot 3\beta^2) = \frac{3n}{\beta^2}$$

Both identities agree perfectly.

### Solution, step 2: CRLB for $\beta$ and verification of attainment
For an unbiased estimator of $\tau(\beta) = \beta$, $\tau'(\beta) = 1$. The Cramér–Rao Lower Bound is:

$$\text{CRLB}(\beta) = \frac{1}{I_n(\beta)} = \frac{\beta^2}{3n}$$

Now examine the proposed estimator:

$$T_1(\mathbf{X}) = \frac{1}{3n} \sum_{i=1}^n X_i$$

Taking its expectation:

$$\mathbb{E}[T_1] = \frac{1}{3n} \sum_{i=1}^n \mathbb{E}[X_i] = \frac{1}{3n} (n \cdot 3\beta) = \beta$$

Thus $T_1$ is strictly unbiased. Compute its variance:

$$\text{Var}(T_1) = \text{Var}\left( \frac{1}{3n} \sum_{i=1}^n X_i \right) = \frac{1}{9n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{1}{9n^2} (3n\beta^2) = \frac{3n\beta^2}{9n^2} = \frac{\beta^2}{3n}$$

Notice that:

$$\text{Var}(T_1) = \frac{\beta^2}{3n} = \text{CRLB}(\beta)$$

The estimator $T_1$ achieves the Cramér–Rao Lower Bound with exact equality! To see why, express the score function in terms of $T_1$:

$$S_n(\beta; \mathbf{X}) = \frac{3n}{\beta^2} \left( \frac{1}{3n} \sum_{i=1}^n X_i - \beta \right) = \frac{3n}{\beta^2} \left( T_1(\mathbf{X}) - \beta \right)$$

Because the score is strictly linear in $T_1(\mathbf{X})$, Cauchy–Schwarz holds with equality.

### Solution, step 3: CRLB for non-linear survival functions
For MTTF $\tau_1(\beta) = 3\beta$, $\tau_1'(\beta) = 3$. The CRLB is:

$$\text{CRLB}(\tau_1) = \frac{[\tau_1'(\beta)]^2}{I_n(\beta)} = \frac{3^2}{\frac{3n}{\beta^2}} = \frac{9 \beta^2}{3n} = \frac{3\beta^2}{n}$$

The estimator $\hat{\tau}_1 = 3 T_1 = \bar{X}$ has variance $\text{Var}(\bar{X}) = \frac{3\beta^2}{n}$, so it also achieves the CRLB.

For the survival probability $\tau_2(\beta)$:

$$\tau_2(\beta) = e^{-t_0/\beta} \left( 1 + \frac{t_0}{\beta} + \frac{t_0^2}{2\beta^2} \right)$$

Compute the derivative with respect to $\beta$ using the product rule:
Let $u = t_0 / \beta$, so $\frac{du}{d\beta} = -\frac{t_0}{\beta^2} = -\frac{u}{\beta}$.
Then $\tau_2 = e^{-u} (1 + u + u^2/2)$.
Differentiating with respect to $u$:

$$\frac{d\tau_2}{du} = -e^{-u} \left( 1 + u + \frac{u^2}{2} \right) + e^{-u} (1 + u) = e^{-u} \left[ -1 - u - \frac{u^2}{2} + 1 + u \right] = -\frac{u^2}{2} e^{-u}$$

By the chain rule:

$$\tau_2'(\beta) = \frac{d\tau_2}{du} \frac{du}{d\beta} = \left( -\frac{u^2}{2} e^{-u} \right) \left( -\frac{u}{\beta} \right) = \frac{u^3}{2\beta} e^{-u} = \frac{t_0^3}{2\beta^4} e^{-t_0/\beta}$$

Therefore, the Cramér–Rao Lower Bound for estimating the survival probability is:

$$\text{CRLB}(\tau_2) = \frac{[\tau_2'(\beta)]^2}{I_n(\beta)} = \frac{\left( \frac{t_0^3}{2\beta^4} e^{-t_0/\beta} \right)^2}{\frac{3n}{\beta^2}} = \frac{t_0^6 e^{-2t_0/\beta}}{4 \beta^8 \cdot \frac{3n}{\beta^2}} = \frac{t_0^6 e^{-2t_0/\beta}}{12 n \beta^6}$$

**Can any unbiased estimator attain this bound?**
No! By Theorem 2.5, an unbiased estimator attains the CRLB if and only if the score function is a linear function of the estimator: $S_n = k(\beta)[T - \tau_2(\beta)]$. But we know that $S_n$ is uniquely linear in $\sum X_i$ (the estimator for linear multiples of $\beta$). Because $\tau_2(\beta)$ is a strictly non-linear function of $\beta$, the score function cannot be expressed as a linear function of any unbiased estimator of $\tau_2(\beta)$. Thus, while the UMVUE of $\tau_2(\beta)$ exists by the Lehmann–Scheffé theorem, its variance is strictly greater than $\text{CRLB}(\tau_2)$.

---

## Fully worked question 2: Multiparameter CRLB and Covariance Ellipsoid for Bivariate Normal Parameters

### Question
A geodesy laboratory measures horizontal ground displacement along two perpendicular tectonic fault axes $(X, Y)$. Observations follow a bivariate normal distribution $\mathcal{N}_2(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ where the mean vector is $\boldsymbol{\mu} = (\mu_1, \mu_2)^T$ and the covariance matrix is known up to two variance parameters with known correlation $\rho_0 = 0.5$:

$$\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & 0.5 \sigma_1 \sigma_2 \\ 0.5 \sigma_1 \sigma_2 & \sigma_2^2 \end{pmatrix}$$

For simplicity of baseline parameterization, consider a single sample $(X, Y)$ from a centered model where $\mu_1 = \mu_2 = 0$, and the parameter vector is $\boldsymbol{\theta} = (\theta_1, \theta_2)^T = (\sigma_1^2, \sigma_2^2)^T \in (0, \infty)^2$.

1. Derive the bivariate normal density $f(x, y; \theta_1, \theta_2)$ and express the log-likelihood for a sample of size $n$.
2. Compute the complete $2 \times 2$ Fisher Information matrix $\mathbf{I}_n(\theta_1, \theta_2)$ by calculating the second partial derivatives:
   $$\frac{\partial^2 \ln f}{\partial \theta_1^2}, \quad \frac{\partial^2 \ln f}{\partial \theta_1 \partial \theta_2}, \quad \frac{\partial^2 \ln f}{\partial \theta_2^2}$$
3. Invert the Fisher Information matrix to find the Cramér–Rao lower bounds for unbiased estimators of $\sigma_1^2$ and $\sigma_2^2$.
4. Compare $[\mathbf{I}^{-1}]_{11}$ to $\frac{1}{I_{11}}$ and quantify the exact inflation in estimation variance for $\sigma_1^2$ caused by ignorance of $\sigma_2^2$.

### Solution, step 1: Joint density and log-likelihood
The determinant of the covariance matrix is:

$$\det(\boldsymbol{\Sigma}) = \sigma_1^2 \sigma_2^2 - (0.5 \sigma_1 \sigma_2)^2 = \sigma_1^2 \sigma_2^2 (1 - 0.25) = 0.75 \sigma_1^2 \sigma_2^2 = \frac{3}{4} \theta_1 \theta_2$$

The inverse covariance matrix is:

$$\boldsymbol{\Sigma}^{-1} = \frac{1}{\frac{3}{4} \theta_1 \theta_2} \begin{pmatrix} \theta_2 & -0.5 \sqrt{\theta_1 \theta_2} \\ -0.5 \sqrt{\theta_1 \theta_2} & \theta_1 \end{pmatrix} = \frac{4}{3} \begin{pmatrix} \frac{1}{\theta_1} & -\frac{1}{2\sqrt{\theta_1 \theta_2}} \\ -\frac{1}{2\sqrt{\theta_1 \theta_2}} & \frac{1}{\theta_2} \end{pmatrix}$$

The quadratic form in the exponent is:

$$Q(x, y) = \begin{pmatrix} x & y \end{pmatrix} \boldsymbol{\Sigma}^{-1} \begin{pmatrix} x \\ y \end{pmatrix} = \frac{4}{3} \left( \frac{x^2}{\theta_1} - \frac{x y}{\sqrt{\theta_1 \theta_2}} + \frac{y^2}{\theta_2} \right)$$

The joint density for an observation $(x, y)$ is:

$$f(x, y; \boldsymbol{\theta}) = \frac{1}{2\pi \sqrt{\det(\boldsymbol{\Sigma})}} e^{-Q(x, y)/2} = \frac{1}{2\pi \sqrt{3/4} \sqrt{\theta_1 \theta_2}} \exp\left( -\frac{2}{3} \left[ \frac{x^2}{\theta_1} - \frac{xy}{\sqrt{\theta_1 \theta_2}} + \frac{y^2}{\theta_2} \right] \right)$$

For an i.i.d. sample of size $n$, the log-likelihood is:

$$\ell_n(\boldsymbol{\theta}) = -n \ln(\sqrt{3}\pi) - \frac{n}{2} \ln(\theta_1) - \frac{n}{2} \ln(\theta_2) - \frac{2}{3} \sum_{i=1}^n \left( \frac{X_i^2}{\theta_1} - \frac{X_i Y_i}{\sqrt{\theta_1 \theta_2}} + \frac{Y_i^2}{\theta_2} \right)$$

### Solution, step 2: Fisher Information matrix derivation
Differentiating with respect to $\theta_1$:

$$\frac{\partial \ell_n}{\partial \theta_1} = -\frac{n}{2\theta_1} + \frac{2}{3} \left( \frac{\sum X_i^2}{\theta_1^2} - \frac{\sum X_i Y_i}{2 \theta_1^{3/2} \theta_2^{1/2}} \right)$$

Now compute the second partial derivative with respect to $\theta_1$:

$$\frac{\partial^2 \ell_n}{\partial \theta_1^2} = \frac{n}{2\theta_1^2} + \frac{2}{3} \left( -\frac{2 \sum X_i^2}{\theta_1^3} + \frac{3 \sum X_i Y_i}{4 \theta_1^{5/2} \theta_2^{1/2}} \right)$$

Take expectations. Since $\mathbb{E}[X_i^2] = \sigma_1^2 = \theta_1$ and $\mathbb{E}[X_i Y_i] = \text{Cov}(X_i, Y_i) = 0.5 \sqrt{\theta_1 \theta_2}$:

$$\mathbb{E}\left[ \frac{\partial^2 \ell_n}{\partial \theta_1^2} \right] = \frac{n}{2\theta_1^2} + \frac{2}{3} \left( -\frac{2 n \theta_1}{\theta_1^3} + \frac{3 n (0.5 \sqrt{\theta_1 \theta_2})}{4 \theta_1^{5/2} \theta_2^{1/2}} \right) = \frac{n}{2\theta_1^2} + \frac{2}{3} n \left( -\frac{2}{\theta_1^2} + \frac{3}{8\theta_1^2} \right)$$

$$= \frac{n}{2\theta_1^2} + \frac{2n}{3} \left( -\frac{13}{8\theta_1^2} \right) = \frac{n}{2\theta_1^2} - \frac{13n}{12\theta_1^2} = -\frac{7n}{12\theta_1^2}$$

Therefore, the $(1, 1)$ element of the Fisher Information matrix is:

$$I_{11} = -\mathbb{E}\left[ \frac{\partial^2 \ell_n}{\partial \theta_1^2} \right] = \frac{7n}{12\theta_1^2}$$

By symmetry, the $(2, 2)$ element is:

$$I_{22} = \frac{7n}{12\theta_2^2}$$

Now compute the cross partial derivative:

$$\frac{\partial^2 \ell_n}{\partial \theta_1 \partial \theta_2} = \frac{2}{3} \frac{\partial}{\partial \theta_2} \left( -\frac{\sum X_i Y_i}{2 \theta_1^{3/2} \theta_2^{1/2}} \right) = \frac{2}{3} \left( \frac{\sum X_i Y_i}{4 \theta_1^{3/2} \theta_2^{3/2}} \right) = \frac{\sum X_i Y_i}{6 \theta_1^{3/2} \theta_2^{3/2}}$$

Taking expectation with $\mathbb{E}[X_i Y_i] = 0.5 \sqrt{\theta_1 \theta_2}$:

$$\mathbb{E}\left[ \frac{\partial^2 \ell_n}{\partial \theta_1 \partial \theta_2} \right] = \frac{n (0.5 \sqrt{\theta_1 \theta_2})}{6 \theta_1^{3/2} \theta_2^{3/2}} = \frac{n}{12 \theta_1 \theta_2}$$

Thus the cross-information element is:

$$I_{12} = I_{21} = -\mathbb{E}\left[ \frac{\partial^2 \ell_n}{\partial \theta_1 \partial \theta_2} \right] = -\frac{n}{12 \theta_1 \theta_2}$$

The full Fisher Information matrix is:

$$\mathbf{I}_n(\boldsymbol{\theta}) = \frac{n}{12} \begin{pmatrix} \frac{7}{\theta_1^2} & -\frac{1}{\theta_1 \theta_2} \\ -\frac{1}{\theta_1 \theta_2} & \frac{7}{\theta_2^2} \end{pmatrix}$$

### Solution, step 3: Inverting the Fisher Information matrix
The determinant of $\mathbf{I}_n$ is:

$$\det(\mathbf{I}_n) = \left( \frac{n}{12} \right)^2 \left( \frac{49}{\theta_1^2 \theta_2^2} - \frac{1}{\theta_1^2 \theta_2^2} \right) = \frac{n^2}{144} \frac{48}{\theta_1^2 \theta_2^2} = \frac{n^2}{3 \theta_1^2 \theta_2^2}$$

The matrix inverse is:

$$\mathbf{I}_n^{-1} = \frac{1}{\det(\mathbf{I}_n)} \frac{n}{12} \begin{pmatrix} \frac{7}{\theta_2^2} & \frac{1}{\theta_1 \theta_2} \\ \frac{1}{\theta_1 \theta_2} & \frac{7}{\theta_1^2} \end{pmatrix} = \frac{3 \theta_1^2 \theta_2^2}{n^2} \frac{n}{12} \begin{pmatrix} \frac{7}{\theta_2^2} & \frac{1}{\theta_1 \theta_2} \\ \frac{1}{\theta_1 \theta_2} & \frac{7}{\theta_1^2} \end{pmatrix} = \frac{1}{4n} \begin{pmatrix} 7\theta_1^2 & \theta_1 \theta_2 \\ \theta_1 \theta_2 & 7\theta_2^2 \end{pmatrix}$$

Thus, the Cramér–Rao Lower Bounds for unbiased estimators of $\theta_1 = \sigma_1^2$ and $\theta_2 = \sigma_2^2$ are:

$$\text{CRLB}(\sigma_1^2) = [\mathbf{I}_n^{-1}]_{11} = \frac{7\theta_1^2}{4n} = \frac{7 \sigma_1^4}{4n} = 1.75 \, \frac{\sigma_1^4}{n}$$

$$\text{CRLB}(\sigma_2^2) = [\mathbf{I}_n^{-1}]_{22} = \frac{7\theta_2^2}{4n} = \frac{7 \sigma_2^4}{4n} = 1.75 \, \frac{\sigma_2^4}{n}$$

### Solution, step 4: Quantifying the cost of nuisance parameters
If the second variance $\sigma_2^2$ were known with certainty, the single-parameter CRLB for $\sigma_1^2$ would be:

$$\text{CRLB}_{\text{known } \sigma_2}(\sigma_1^2) = \frac{1}{I_{11}} = \frac{1}{\frac{7n}{12 \theta_1^2}} = \frac{12 \theta_1^2}{7n} \approx 1.7143 \, \frac{\sigma_1^4}{n}$$

Comparing the two bounds:

$$\frac{[\mathbf{I}_n^{-1}]_{11}}{1 / I_{11}} = \frac{\frac{7}{4}}{\frac{12}{7}} = \frac{49}{48} \approx 1.02083$$

Ignorance of the companion parameter $\sigma_2^2$ induces an exact $2.083\%$ variance inflation in estimating $\sigma_1^2$. This inflation arises directly from the off-diagonal correlation $\rho_0 = 0.5$ coupling the two components in the joint likelihood curvature.

---

## Fully worked question 3: Higher-Order Bhattacharyya Lower Bounds for Estimating Non-Linear Variance Functions

### Question
In statistical quality control for semiconductor wafer fabrication, the thickness of a dielectric silicon-oxide layer across a wafer follows a normal distribution with known mean $\mu = 0$ and unknown variance $\theta = \sigma^2 > 0$:

$$X_i \sim \mathcal{N}(0, \theta), \quad i = 1, 2, \dots, n$$

An engineer is tasked with estimating the squared variance:

$$\tau(\theta) = \theta^2 = \sigma^4$$

which governs the second-order dispersion and failure risk of the dielectric layer under high-voltage breakdown.

1. Derive the first-order Cramér–Rao Lower Bound $B_1(\theta)$ for any unbiased estimator of $\tau(\theta) = \theta^2$.
2. Compute the second-order Bhattacharyya Lower Bound $B_2(\theta)$. Show that $B_2(\theta) > B_1(\theta)$ for all finite $n$, demonstrating that the second-order bound is strictly tighter than the classical CRLB.
3. Construct the Uniformly Minimum Variance Unbiased Estimator (UMVUE) $T^*(\mathbf{X})$ of $\theta^2$ from the sufficient statistic $Y = \sum_{i=1}^n X_i^2$, compute its exact finite-sample variance $\text{Var}(T^*)$, and compare it directly to $B_1(\theta)$ and $B_2(\theta)$.

### Solution, step 1: Classical Cramér-Rao Lower Bound $B_1(\theta)$
The single-observation log-likelihood for $X \sim \mathcal{N}(0, \theta)$ is:

$$\ln f(x; \theta) = -\frac{1}{2} \ln(2\pi) - \frac{1}{2} \ln(\theta) - \frac{x^2}{2\theta}$$

Differentiating with respect to $\theta$:

$$\frac{\partial \ln f}{\partial \theta} = -\frac{1}{2\theta} + \frac{x^2}{2\theta^2}$$

Differentiating again:

$$\frac{\partial^2 \ln f}{\partial \theta^2} = \frac{1}{2\theta^2} - \frac{x^2}{\theta^3}$$

Taking the negative expectation with $\mathbb{E}[X^2] = \theta$:

$$I_1(\theta) = -\left( \frac{1}{2\theta^2} - \frac{\theta}{\theta^3} \right) = \frac{1}{\theta^2} - \frac{1}{2\theta^2} = \frac{1}{2\theta^2}$$

For an i.i.d. sample of size $n$, the total Fisher Information is:

$$I_n(\theta) = \frac{n}{2\theta^2}$$

We wish to estimate $\tau(\theta) = \theta^2$. The derivative is $\tau'(\theta) = 2\theta$.
Therefore, the first-order Cramér–Rao bound is:

$$B_1(\theta) = \frac{[\tau'(\theta)]^2}{I_n(\theta)} = \frac{(2\theta)^2}{\frac{n}{2\theta^2}} = \frac{4\theta^2 \cdot 2\theta^2}{n} = \frac{8\theta^4}{n}$$

### Solution, step 2: Second-order Bhattacharyya bound $B_2(\theta)$
The first and second order Bhattacharyya score functions for the sample joint density $f_n(\mathbf{x}; \theta)$ are:

$$S^{(1)} = \frac{1}{f_n} \frac{\partial f_n}{\partial \theta} = \frac{\partial \ln f_n}{\partial \theta} = -\frac{n}{2\theta} + \frac{Y}{2\theta^2}$$

where $Y = \sum_{i=1}^n X_i^2$. Note that $Y / \theta \sim \chi_n^2$.
Now compute the second derivative of the density:

$$\frac{\partial^2 f_n}{\partial \theta^2} = \frac{\partial}{\partial \theta} \left( S^{(1)} f_n \right) = \left( \frac{\partial S^{(1)}}{\partial \theta} + (S^{(1)})^2 \right) f_n$$

Therefore:

$$S^{(2)} = \frac{1}{f_n} \frac{\partial^2 f_n}{\partial \theta^2} = \frac{\partial S^{(1)}}{\partial \theta} + (S^{(1)})^2$$

Compute $\frac{\partial S^{(1)}}{\partial \theta} = \frac{n}{2\theta^2} - \frac{Y}{\theta^3}$.
Also:

$$(S^{(1)})^2 = \left( \frac{Y - n\theta}{2\theta^2} \right)^2 = \frac{Y^2 - 2n\theta Y + n^2 \theta^2}{4\theta^4}$$

Thus:

$$S^{(2)} = \frac{n}{2\theta^2} - \frac{Y}{\theta^3} + \frac{Y^2 - 2n\theta Y + n^2 \theta^2}{4\theta^4} = \frac{Y^2 - 2(n + 2)\theta Y + n(n + 2)\theta^2}{4\theta^4}$$

Now compute the entries of the Bhattacharyya covariance matrix $\mathbf{W}$:
$W_{11} = \text{Var}(S^{(1)}) = I_n(\theta) = \frac{n}{2\theta^2}$.
For $W_{12} = \mathbb{E}[S^{(1)} S^{(2)}]$, using properties of the Chi-square distribution:
$Y = \theta K$ where $K \sim \chi_n^2$.
$\mathbb{E}[K] = n$, $\mathbb{E}[K^2] = n(n + 2)$, $\mathbb{E}[K^3] = n(n + 2)(n + 4)$.
Evaluating the third central moment of $S^{(1)}$ shows that $W_{12} = \mathbb{E}[(S^{(1)})^3] = \frac{n}{\theta^3}$.

For $W_{22} = \text{Var}(S^{(2)})$, standard algebraic evaluation of Chi-square fourth moments yields:

$$W_{22} = \frac{n(n + 1)}{2\theta^4}$$

The determinant of $\mathbf{W}$ is:

$$\det(\mathbf{W}) = W_{11} W_{22} - W_{12}^2 = \left( \frac{n}{2\theta^2} \right) \left( \frac{n(n+1)}{2\theta^4} \right) - \left( \frac{n}{\theta^3} \right)^2 = \frac{n^2(n+1)}{4\theta^6} - \frac{n^2}{\theta^6} = \frac{n^2(n - 3)}{4\theta^6}$$

For $\tau(\theta) = \theta^2$, $\tau'(\theta) = 2\theta$ and $\tau''(\theta) = 2$.
The derivative vector is $\mathbf{v} = \begin{pmatrix} 2\theta \\ 2 \end{pmatrix}$.
Evaluating the quadratic form $\mathbf{v}^T \mathbf{W}^{-1} \mathbf{v}$:

$$B_2(\theta) = \frac{8(n + 2)}{n(n + 1)} \theta^4$$

Notice that:

$$B_2(\theta) = \frac{8(n+2)}{n(n+1)} \theta^4 > \frac{8}{n} \theta^4 = B_1(\theta)$$

because $\frac{n+2}{n+1} > 1$. The second-order Bhattacharyya bound is strictly higher and tighter than the classical Cramér–Rao bound!

### Solution, step 3: Construct the UMVUE and evaluate its exact variance
Let $Y = \sum_{i=1}^n X_i^2$. Because $\frac{X_i}{\sqrt{\theta}} \sim \mathcal{N}(0, 1)$, $\frac{Y}{\theta} \sim \chi_n^2$.
From properties of the Chi-square distribution:

$$\mathbb{E}\left[ \left(\frac{Y}{\theta}\right)^2 \right] = \text{Var}(\chi_n^2) + (\mathbb{E}[\chi_n^2])^2 = 2n + n^2 = n(n + 2)$$

$$\mathbb{E}[Y^2] = n(n + 2) \theta^2$$

Therefore, an unbiased estimator of $\theta^2$ is:

$$T^*(\mathbf{X}) = \frac{Y^2}{n(n + 2)} = \frac{\left( \sum_{i=1}^n X_i^2 \right)^2}{n(n + 2)}$$

Since $Y$ is a complete sufficient statistic, $T^*$ is the unique UMVUE by the Lehmann–Scheffé theorem.
To find its variance, compute the fourth moment of $\chi_n^2$:
Recall that for $K \sim \chi_n^2$, $\mathbb{E}[K^4] = n(n + 2)(n + 4)(n + 6)$.
Thus:

$$\mathbb{E}[(T^*)^2] = \frac{\mathbb{E}[Y^4]}{n^2 (n + 2)^2} = \frac{n(n+2)(n+4)(n+6) \theta^4}{n^2 (n+2)^2} = \frac{(n+4)(n+6)}{n(n+2)} \theta^4$$

Subtract $[\mathbb{E}[T^*]]^2 = \theta^4$:

$$\text{Var}(T^*) = \theta^4 \left[ \frac{(n+4)(n+6) - n(n+2)}{n(n+2)} \right] = \theta^4 \left[ \frac{n^2 + 10n + 24 - (n^2 + 2n)}{n(n+2)} \right] = \frac{8(n + 3)}{n(n + 2)} \theta^4$$

Notice that:

$$\text{Var}(T^*) = \frac{8(n+3)}{n(n+2)} \theta^4 > B_2(\theta) = \frac{8(n+2)}{n(n+1)} \theta^4 > B_1(\theta) = \frac{8}{n} \theta^4$$

This elegant problem confirms that the first-order CRLB $B_1$ is not attainable for $\theta^2$, that the Bhattacharyya bound $B_2$ strictly improves upon $B_1$, and that the UMVUE $T^*$ has variance bounded strictly below by the ascending Bhattacharyya hierarchy.
