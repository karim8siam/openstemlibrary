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
# UNIT 5: Asymptotic Properties of Maximum Likelihood Estimators (Target >= 4000 words)
# ==============================================================================
u5_text = """# Unit 5: Asymptotic Properties of Maximum Likelihood Estimators

While finite-sample optimality properties like UMVUE and the Cramér–Rao bound provide rigorous benchmarks in simple models, they are often difficult or impossible to establish in complex non-linear models. In contrast, the asymptotic theory of estimation investigates the limiting behavior of estimators as the sample size $n$ approaches infinity ($n \\to \\infty$). In this large-sample regime, Maximum Likelihood Estimators (MLEs) display universal, remarkable optimality properties: under mild regularity conditions, the MLE is guaranteed to be strongly consistent, asymptotically normally distributed, and asymptotically efficient (attaining the Cramér–Rao bound in the limit). In this unit, we rigorously formulate the modes of stochastic convergence, prove Cramér's consistency and asymptotic normality theorems, establish the Hájek–Le Cam asymptotic minimax efficiency bound, analyze the Efron–Hinkley theorem on observed information, develop the Huber–White sandwich covariance estimator under model misspecification, examine the classical likelihood test trinity, and investigate Hodges' superefficiency pathology.

## 5.1 Stochastic Convergence Modes in Asymptotic Statistics

Asymptotic statistical theory relies on formal modes of convergence for sequences of random variables defined on a probability space $(\\Omega, \\mathcal{F}, P)$. Let $\\{T_n\\}_{n \\ge 1}$ be a sequence of estimators (random variables) and let $\\theta$ be a fixed constant or target parameter.

### 1. Convergence in Probability (Weak Consistency)
A sequence of estimators $T_n$ converges in probability to $\\theta$, denoted $T_n \\xrightarrow{P} \\theta$, if for every $\\epsilon > 0$:

$$\\lim_{n \\to \\infty} \\mathbb{P}(|T_n - \\theta| \\ge \\epsilon) = 0$$

An estimator satisfying $T_n \\xrightarrow{P} \\theta$ is said to be **weakly consistent**. Weak consistency ensures that in sufficiently large samples, the probability of any noticeable estimation error arbitrarily close to zero vanishes.

### 2. Almost Sure Convergence (Strong Consistency)
A sequence $T_n$ converges almost surely (with probability $1$) to $\\theta$, denoted $T_n \\xrightarrow{\\text{a.s.}} \\theta$, if:

$$\\mathbb{P}\\left( \\lim_{n \\to \\infty} T_n = \\theta \\right) = 1$$

Equivalently, for every $\\epsilon > 0$, $\\lim_{N \\to \\infty} \\mathbb{P}\\left( \\bigcup_{n=N}^\\infty \\{|T_n - \\theta| \\ge \\epsilon\\} \\right) = 0$. An estimator satisfying $T_n \\xrightarrow{\\text{a.s.}} \\theta$ is **strongly consistent**. Strong consistency implies weak consistency by the dominated convergence theorem.

### 3. Convergence in Mean Square ($L^2$ Consistency)
A sequence $T_n$ converges in mean square to $\\theta$, denoted $T_n \\xrightarrow{L^2} \\theta$, if:

$$\\lim_{n \\to \\infty} \\mathbb{E}[(T_n - \\theta)^2] = 0$$

Because $\\mathbb{E}[(T_n - \\theta)^2] = \\text{MSE}(T_n) = \\text{Var}(T_n) + [\\text{Bias}(T_n)]^2$, an estimator is $L^2$-consistent if and only if its variance and bias simultaneously vanish as $n \\to \\infty$. By Chebyshev's Inequality, $L^2$ convergence implies convergence in probability.

### 4. Convergence in Distribution (Weak Convergence)
A sequence of random variables $T_n$ with cumulative distribution functions $F_n(t) = \\mathbb{P}(T_n \\le t)$ converges in distribution to a limiting random variable $Z$ with CDF $F(t)$, denoted $T_n \\xrightarrow{d} Z$, if:

$$\\lim_{n \\to \\infty} F_n(t) = F(t)$$

for all continuity points $t$ of $F$. In statistical estimation, we typically analyze the normalized estimation error $\\sqrt{n}(T_n - \\theta)$ and prove that it converges in distribution to a Gaussian law $\\mathcal{N}(0, V)$.

## 5.2 Weak and Strong Consistency of MLEs: Cramér's Theorem and Wald's Global Conditions

Under what conditions is the Maximum Likelihood Estimator guaranteed to converge to the true parameter $\\theta_0$? We distinguish between local consistency (Cramér, 1946) and global consistency (Wald, 1949).

### Cramér's Local Consistency Theorem
Let $X_1, X_2, \\dots, X_n$ be an i.i.d. sample from a density $f(x; \\theta)$ with true parameter $\\theta_0$ residing in an open interval $\\Theta \\subseteq \\mathbb{R}$. Assume the Cramér regularity conditions (C1)-(C6) hold:
1. The support $\\mathcal{S} = \\{x : f(x; \\theta) > 0\\}$ is independent of $\\theta$.
2. For almost all $x$, $\\ln f(x; \\theta)$ is three times continuously differentiable with respect to $\\theta$ on an open neighborhood of $\\theta_0$.
3. For all $\\theta \\in \\Theta$, the expected Fisher Information $I_1(\\theta) = \\mathbb{E}_\\theta\\left[ \\left( \\frac{\\partial \\ln f}{\\partial \\theta} \\right)^2 \\right]$ is finite and strictly positive ($0 < I_1(\\theta) < \\infty$).
4. There exists a measurable function $M(x)$ and an $\\epsilon > 0$ such that for all $\\theta \\in (\\theta_0 - \\epsilon, \\theta_0 + \\epsilon)$:
   $$\\left| \\frac{\\partial^3 \\ln f(x; \\theta)}{\\partial \\theta^3} \\right| \\le M(x) \\quad \\text{with} \\quad \\mathbb{E}_{\\theta_0}[M(X)] = K < \\infty$$

#### Theorem: Existence of a Consistent Root
Under regularity conditions (1)-(4), with probability approaching $1$ as $n \\to \\infty$, the likelihood equation $\\frac{\\partial \\ell_n(\\theta)}{\\partial \\theta} = 0$ has a root $\\hat{\\theta}_n$ such that:

$$\\hat{\\theta}_n \\xrightarrow{P} \\theta_0$$

#### Proof:
Let $\\epsilon > 0$ be chosen sufficiently small such that $(\\theta_0 - \\epsilon, \\theta_0 + \\epsilon) \\subset \\Theta$.
Consider the normalized log-likelihood difference:

$$D_n(\\theta) = \\frac{1}{n} \\left[ \\ell_n(\\theta) - \\ell_n(\\theta_0) \\right] = \\frac{1}{n} \\sum_{i=1}^n \\ln\\left( \\frac{f(X_i; \\theta)}{f(X_i; \\theta_0)} \\right)$$

By the Strong Law of Large Numbers, as $n \\to \\infty$:

$$D_n(\\theta) \\xrightarrow{\\text{a.s.}} \\mathbb{E}_{\\theta_0}\\left[ \\ln\\left( \\frac{f(X; \\theta)}{f(X; \\theta_0)} \\right) \\right] = -\\text{KL}(f(\\cdot; \\theta_0) \\| f(\\cdot; \\theta))$$

where $\\text{KL}(f_0 \\| f)$ is the Kullback–Leibler divergence.
By Gibbs' Inequality (information inequality), the Kullback–Leibler divergence is strictly positive whenever the measures are distinct:

$$\\mathbb{E}_{\\theta_0}\\left[ \\ln\\left( \\frac{f(X; \\theta)}{f(X; \\theta_0)} \\right) \\right] < \\ln \\mathbb{E}_{\\theta_0}\\left[ \\frac{f(X; \\theta)}{f(X; \\theta_0)} \\right] = \\ln(1) = 0$$

Thus, for any fixed $\\theta \\ne \\theta_0$, the expectation is strictly negative!
In particular, evaluate this at the two boundary points $\\theta_1 = \\theta_0 - \\epsilon$ and $\\theta_2 = \\theta_0 + \\epsilon$:

$$\\lim_{n \\to \\infty} \\mathbb{P}\\left( \\frac{1}{n} \\ell_n(\\theta_0 - \\epsilon) < \\frac{1}{n} \\ell_n(\\theta_0) \\right) = 1$$

$$\\lim_{n \\to \\infty} \\mathbb{P}\\left( \\frac{1}{n} \\ell_n(\\theta_0 + \\epsilon) < \\frac{1}{n} \\ell_n(\\theta_0) \\right) = 1$$

Because $\\ell_n(\\theta)$ is continuous, whenever $\\ell_n(\\theta_0 - \\epsilon) < \\ell_n(\\theta_0)$ and $\\ell_n(\\theta_0 + \\epsilon) < \\ell_n(\\theta_0)$, the function $\\ell_n(\\theta)$ must achieve a local maximum at some interior point $\\hat{\\theta}_n \\in (\\theta_0 - \\epsilon, \\theta_0 + \\epsilon)$.
At this local maximum, the derivative vanishes: $\\ell_n'(\\hat{\\theta}_n) = 0$.
Since this event occurs with probability approaching $1$ for any arbitrarily small $\\epsilon > 0$, we have proved the existence of a consistent local root: $\\hat{\\theta}_n \\xrightarrow{P} \\theta_0$.

### Wald's Theorem on Global Strong Consistency
Abraham Wald (1949) proved that if the parameter space $\\Theta$ is compact (or compactifiable) and the log-density satisfies a uniform integrability condition $\\mathbb{E}[\\sup_{\\theta \\in U} \\ln f(X; \\theta)] < \\infty$, then the global Maximum Likelihood Estimator is **strongly consistent**:

$$\\hat{\\theta}_n \\xrightarrow{\\text{a.s.}} \\theta_0$$

Wald's proof demonstrates that the empirical log-likelihood function $\\frac{1}{n} \\ell_n(\\theta)$ converges uniformly across $\\Theta$ to the deterministic limit $\\mathbb{E}_{\\theta_0}[\\ln f(X; \\theta)]$, which has a unique global maximum at $\\theta = \\theta_0$ by the strict negativity of the Kullback–Leibler divergence.

## 5.3 Asymptotic Normality of the MLE: Local Score Expansion and Limiting Gaussian Law

We now establish the centerpiece of large-sample likelihood theory: Maximum Likelihood Estimators converge at a $\\sqrt{n}$ rate to a centered Gaussian distribution with variance equal to the inverse of the Fisher Information.

### Theorem: Asymptotic Normality of the MLE
Under Cramér regularity conditions (C1)-(C6), any consistent root $\\hat{\\theta}_n$ of the likelihood equations satisfies:

$$\\sqrt{n}(\\hat{\\theta}_n - \\theta_0) \\xrightarrow{d} \\mathcal{N}\\left( 0, \\frac{1}{I_1(\\theta_0)} \\right) \\quad \\text{as } n \\to \\infty$$

where $I_1(\\theta_0) = \\mathbb{E}_{\\theta_0}\\left[ \\left( \\frac{\\partial \\ln f(X; \\theta_0)}{\\partial \\theta} \\right)^2 \\right]$ is the single-observation Fisher Information.

#### Rigorous Proof:
By definition, $\\hat{\\theta}_n$ satisfies the likelihood equation:

$$\\ell_n'(\\hat{\\theta}_n) = \\sum_{i=1}^n \\frac{\\partial}{\\partial \\theta} \\ln f(X_i; \\hat{\\theta}_n) = 0$$

Perform a first-order Taylor expansion of the score function $\\ell_n'(\\hat{\\theta}_n)$ around the true parameter $\\theta_0$:

$$0 = \\ell_n'(\\hat{\\theta}_n) = \\ell_n'(\\theta_0) + \\ell_n''(\\theta_n^*) (\\hat{\\theta}_n - \\theta_0)$$

where $\\theta_n^*$ is an intermediate point lying on the line segment connecting $\\hat{\\theta}_n$ and $\\theta_0$: $|\\theta_n^* - \\theta_0| \\le |\\hat{\\theta}_n - \\theta_0|$.
Rearranging this linear equation to isolate the estimation error:

$$\\hat{\\theta}_n - \\theta_0 = -\\frac{\\ell_n'(\\theta_0)}{\\ell_n''(\\theta_n^*)} = \\frac{\\frac{1}{n} \\ell_n'(\\theta_0)}{-\\frac{1}{n} \\ell_n''(\\theta_n^*)}$$

Multiplying both sides by $\\sqrt{n}$:

$$\\sqrt{n}(\\hat{\\theta}_n - \\theta_0) = \\frac{\\frac{1}{\\sqrt{n}} \\ell_n'(\\theta_0)}{-\\frac{1}{n} \\ell_n''(\\theta_n^*)}$$

Now analyze the asymptotic behavior of the numerator and denominator separately:

**1. Analysis of the Numerator (Central Limit Theorem)**:
The numerator is:

$$\\frac{1}{\\sqrt{n}} \\ell_n'(\\theta_0) = \\frac{1}{\\sqrt{n}} \\sum_{i=1}^n \\frac{\\partial}{\\partial \\theta} \\ln f(X_i; \\theta_0) = \\frac{1}{\\sqrt{n}} \\sum_{i=1}^n S_1(\\theta_0; X_i)$$

Each term $S_1(\\theta_0; X_i)$ is an independent, identically distributed random variable.
By Bartlett's First Identity:

$$\\mathbb{E}_{\\theta_0}[S_1(\\theta_0; X_i)] = 0$$

The variance of each score term is the Fisher Information:

$$\\text{Var}_{\\theta_0}(S_1(\\theta_0; X_i)) = \\mathbb{E}_{\\theta_0}[S_1^2] = I_1(\\theta_0)$$

Because $0 < I_1(\\theta_0) < \\infty$, the classical Lindeberg–Lévy Central Limit Theorem applies directly:

$$\\frac{1}{\\sqrt{n}} \\ell_n'(\\theta_0) \\xrightarrow{d} \\mathcal{N}(0, I_1(\\theta_0))$$

**2. Analysis of the Denominator (Law of Large Numbers and Remainder Domination)**:
The denominator is:

$$-\\frac{1}{n} \\ell_n''(\\theta_n^*) = -\\frac{1}{n} \\sum_{i=1}^n \\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X_i; \\theta_n^*)$$

Expand $\\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X_i; \\theta_n^*)$ around $\\theta_0$:

$$\\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X_i; \\theta_n^*) = \\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X_i; \\theta_0) + (\\theta_n^* - \\theta_0) \\frac{\\partial^3}{\\partial \\theta^3} \\ln f(X_i; \\tilde{\\theta}_n)$$

where $\\tilde{\\theta}_n$ lies between $\\theta_n^*$ and $\\theta_0$.
Taking the average across the sample:

$$-\\frac{1}{n} \\ell_n''(\\theta_n^*) = -\\frac{1}{n} \\sum_{i=1}^n \\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X_i; \\theta_0) - (\\theta_n^* - \\theta_0) \\left( \\frac{1}{n} \\sum_{i=1}^n \\frac{\\partial^3}{\\partial \\theta^3} \\ln f(X_i; \\tilde{\\theta}_n) \\right)$$

For the first term, by the Weak Law of Large Numbers:

$$-\\frac{1}{n} \\sum_{i=1}^n \\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X_i; \\theta_0) \\xrightarrow{P} -\\mathbb{E}_{\\theta_0}\\left[ \\frac{\\partial^2}{\\partial \\theta^2} \\ln f(X; \\theta_0) \\right] = I_1(\\theta_0)$$

by Bartlett's Second Identity.
For the second term:
Since $\\hat{\\theta}_n \\xrightarrow{P} \\theta_0$, we have $\\theta_n^* \\xrightarrow{P} \\theta_0$, so $(\\theta_n^* - \\theta_0) \\xrightarrow{P} 0$.
By regularity condition (C6), $\\left| \\frac{1}{n} \\sum_{i=1}^n \\frac{\\partial^3}{\\partial \\theta^3} \\ln f(X_i; \\tilde{\\theta}_n) \\right| \\le \\frac{1}{n} \\sum_{i=1}^n M(X_i) \\xrightarrow{P} \\mathbb{E}[M(X)] < \\infty$.
The product of a term converging in probability to zero and a bounded term converges in probability to zero:

$$(\\theta_n^* - \\theta_0) \\left( \\frac{1}{n} \\sum_{i=1}^n \\frac{\\partial^3}{\\partial \\theta^3} \\ln f(X_i; \\tilde{\\theta}_n) \\right) \\xrightarrow{P} 0$$

Therefore, by Slutsky's Theorem, the denominator converges in probability to the deterministic constant $I_1(\\theta_0)$:

$$-\\frac{1}{n} \\ell_n''(\\theta_n^*) \\xrightarrow{P} I_1(\\theta_0)$$

**3. Combining via Slutsky's Theorem**:
We now have:
- Numerator $U_n = \\frac{1}{\\sqrt{n}} \\ell_n'(\\theta_0) \\xrightarrow{d} U \\sim \\mathcal{N}(0, I_1(\\theta_0))$
- Denominator $V_n = -\\frac{1}{n} \\ell_n''(\\theta_n^*) \\xrightarrow{P} c = I_1(\\theta_0) > 0$

By Slutsky's Theorem (ratio of a weakly convergent sequence and a probability limit):

$$\\sqrt{n}(\\hat{\\theta}_n - \\theta_0) = \\frac{U_n}{V_n} \\xrightarrow{d} \\frac{U}{c} \\sim \\mathcal{N}\\left( 0, \\frac{I_1(\\theta_0)}{(I_1(\\theta_0))^2} \\right) = \\mathcal{N}\\left( 0, \\frac{1}{I_1(\\theta_0)} \\right)$$

This completes the rigorous proof of asymptotic normality!

### Multiparameter Generalization
For a $k$-dimensional parameter vector $\\boldsymbol{\\theta} \\in \\Theta \\subseteq \\mathbb{R}^k$, Taylor expansion of the score vector $\\mathbf{S}_n(\\hat{\\boldsymbol{\\theta}}) = \\mathbf{0}$ yields:

$$\\sqrt{n}(\\hat{\\boldsymbol{\\theta}}_n - \\boldsymbol{\\theta}_0) \\xrightarrow{d} \\mathcal{N}_k\\left( \\mathbf{0}, \\mathbf{I}_1(\\boldsymbol{\\theta}_0)^{-1} \\right)$$

where $\\mathbf{I}_1(\\boldsymbol{\\theta}_0)$ is the $k \\times k$ expected Fisher Information matrix per observation.

## 5.4 Asymptotic Efficiency, CRLB Attainment, and the Hájek–Le Cam Convolution Theorem

A point estimator $T_n$ is said to be **asymptotically efficient** (or Best Asymptotically Normal / BAN) if:

$$\\sqrt{n}(T_n - \\theta) \\xrightarrow{d} \\mathcal{N}(0, V(\\theta)) \\quad \\text{with} \\quad V(\\theta) = \\frac{1}{I_1(\\theta)}$$

Because the Cramér–Rao Lower Bound states that for any unbiased estimator $\\text{Var}(T_n) \\ge \\frac{1}{n I_1(\\theta)}$, an estimator achieving asymptotic variance $V(\\theta) = \\frac{1}{I_1(\\theta)}$ attains the Cramér–Rao bound in the limit.

### The Hájek–Le Cam Convolution Theorem
In 1970–1972, Jaroslav Hájek and Lucien Le Cam proved that the asymptotic variance $\\frac{1}{I_1(\\theta)}$ is indeed the fundamental lower bound on the asymptotic variance of all **regular estimators**.

#### Theorem (Hájek–Le Cam):
Let $\\mathcal{P} = \\{P_\\theta : \\theta \\in \\Theta\\}$ be a locally asymptotically normal (LAN) family. Let $T_n$ be any regular estimator of $\\theta$ (an estimator whose limiting distribution is locally stable under $\\mathcal{O}(1/\\sqrt{n})$ perturbations of $\\theta$). Then the limiting distribution of $\\sqrt{n}(T_n - \\theta)$ is the **convolution** of a centered Gaussian distribution and an independent noise distribution:

$$\\sqrt{n}(T_n - \\theta) \\xrightarrow{d} Z_0 + W$$

where $Z_0 \\sim \\mathcal{N}\\left(0, I_1(\\theta)^{-1}\\right)$ and $W$ is an independent random variable.
Taking variances:

$$\\text{Var}(Z_0 + W) = \\text{Var}(Z_0) + \\text{Var}(W) = \\frac{1}{I_1(\\theta)} + \\text{Var}(W) \\ge \\frac{1}{I_1(\\theta)}$$

The limiting variance is strictly minimized if and only if $W \\equiv 0$ almost surely, which occurs precisely for the Maximum Likelihood Estimator!
This establishes that no regular estimator can ever beat the asymptotic precision of the MLE.

## 5.5 Observed vs Expected Fisher Information in Variance Estimation: The Efron–Hinkley Theorem

To construct asymptotic confidence intervals for $\\theta$, we must estimate the asymptotic variance $V = \\frac{1}{I_n(\\theta)}$. Statisticians face a fundamental choice between two variance estimators:
1. **Expected Information Estimator**: $\\hat{V}_{\\text{exp}} = [\\mathbf{I}_n(\\hat{\\boldsymbol{\\theta}})]^{-1}$, where $\\mathbf{I}_n(\\boldsymbol{\\theta}) = \\mathbb{E}[-\\nabla^2 \\ell_n(\\boldsymbol{\\theta})]$.
2. **Observed Information Estimator**: $\\hat{V}_{\\text{obs}} = [J_n(\\hat{\\boldsymbol{\\theta}})]^{-1}$, where $J_n(\\hat{\\boldsymbol{\\theta}}) = -\\nabla^2 \\ell_n(\\hat{\\boldsymbol{\\theta}})$.

In large samples, both estimators converge to the same limit: $\\frac{1}{n} J_n(\\hat{\\theta}) \\xrightarrow{P} I_1(\\theta_0)$ and $\\frac{1}{n} \\mathbf{I}_n(\\hat{\\theta}) \\xrightarrow{P} I_1(\\theta_0)$.
However, in finite samples, Bradley Efron and David Hinkley (1978) proved that **observed information is superior to expected information**.

### The Efron–Hinkley Curvature Theorem
In translation and curved exponential models, the observed information $J_n$ can be decomposed as:

$$J_n(\\hat{\\theta}) = I_n(\\hat{\\theta}) + a(\\mathbf{X})$$

where $a(\\mathbf{X})$ is an ancillary statistic measuring the statistical curvature of the realized likelihood function.
Efron and Hinkley proved that the conditional distribution of the estimation error given the ancillary curvature:

$$\\sqrt{J_n(\\hat{\\theta})} (\\hat{\\theta} - \\theta_0) \\mid a(\\mathbf{X})$$

converges to $\\mathcal{N}(0, 1)$ with error rate $\\mathcal{O}(1/n)$, whereas normalizing by expected information:

$$\\sqrt{I_n(\\hat{\\theta})} (\\hat{\\theta} - \\theta_0) \\mid a(\\mathbf{X})$$

has a much coarser error rate of order $\\mathcal{O}(1/\\sqrt{n})$.
Observed information measures the actual precision delivered by the realized data sample, whereas expected information averages over hypothetical samples that were never observed. Consequently, modern computational statistics universally prefers observed information $J_n(\\hat{\\boldsymbol{\\theta}})^{-1}$ for standard error calculations.

## 5.6 Model Misspecification and Kullback-Leibler Projection: White's QMLE

In real-world applications, statistical models are idealizations. What happens to the Maximum Likelihood Estimator when the true data-generating distribution $G$ does not belong to the assumed parametric family $\\mathcal{P} = \\{F_\\theta : \\theta \\in \\Theta\\}$?

Halbert White (1982) established the foundational theory of **Quasi-Maximum Likelihood Estimation (QMLE)**.

### The Pseudo-True Parameter
Let $g(x)$ denote the true, unknown probability density function generating the i.i.d. observations $X_1, \\dots, X_n$.
The Quasi-MLE $\\hat{\\theta}_n$ maximizes the assumed log-likelihood $\\ell_n(\\theta) = \\sum_{i=1}^n \\ln f(X_i; \\theta)$.
By the Strong Law of Large Numbers:

$$\\frac{1}{n} \\ell_n(\\theta) = \\frac{1}{n} \\sum_{i=1}^n \\ln f(X_i; \\theta) \\xrightarrow{\\text{a.s.}} \\mathbb{E}_g[\\ln f(X; \\theta)] = \\int \\ln f(x; \\theta) g(x) \\, dx$$

Notice that maximizing $\\mathbb{E}_g[\\ln f(X; \\theta)]$ is mathematically identical to minimizing the Kullback–Leibler divergence between the true density $g$ and the assumed family $f(\\cdot; \\theta)$:

$$\\text{KL}(g \\| f_\\theta) = \\int g(x) \\ln\\left( \\frac{g(x)}{f(x; \\theta)} \\right) dx = \\int g(x) \\ln g(x) \\, dx - \\int g(x) \\ln f(x; \\theta) \\, dx$$

The **pseudo-true parameter** $\\theta^*$ is defined as the parameter value that minimizes the information divergence:

$$\\theta^* = \\arg\\min_{\\theta \\in \\Theta} \\text{KL}(g \\| f_\\theta) = \\arg\\max_{\\theta \\in \\Theta} \\mathbb{E}_g[\\ln f(X; \\theta)]$$

White proved that under mild regularity conditions, the Quasi-MLE is strongly consistent for the pseudo-true parameter:

$$\\hat{\\theta}_n \\xrightarrow{\\text{a.s.}} \\theta^*$$

The MLE converges to the closest member of the candidate family to the true state of nature in the information-theoretic (Kullback–Leibler) projection sense.

## 5.7 The Huber–White Sandwich Covariance Estimator

Under model misspecification, Bartlett's Second Identity collapses! That is:

$$\\mathbf{A}(\\theta^*) = -\\mathbb{E}_g\\left[ \\nabla^2 \\ln f(X; \\theta^*) \\right] \\ne \\mathbb{E}_g\\left[ \\nabla \\ln f(X; \\theta^*) \\nabla \\ln f(X; \\theta^*)^T \\right] = \\mathbf{B}(\\theta^*)$$

The expected Hessian matrix $\\mathbf{A}(\\theta^*)$ (the "bread") does not equal the outer product of the score vectors $\\mathbf{B}(\\theta^*)$ (the "meat").

### Theorem: Asymptotic Distribution of QMLE
Applying a Taylor expansion to the misspecified score equation $\\nabla \\ell_n(\\hat{\\boldsymbol{\\theta}}_n) = \\mathbf{0}$:

$$\\sqrt{n}(\\hat{\\boldsymbol{\\theta}}_n - \\boldsymbol{\\theta}^*) \\xrightarrow{d} \\mathcal{N}_k\\left( \\mathbf{0}, \\mathbf{V}_{\\text{sandwich}} \\right)$$

where the asymptotic covariance matrix is the celebrated **Huber–White Sandwich Matrix**:

$$\\mathbf{V}_{\\text{sandwich}} = \\mathbf{A}(\\theta^*)^{-1} \\mathbf{B}(\\theta^*) \\mathbf{A}(\\theta^*)^{-1}$$

### Empirical Estimation of the Sandwich Matrix
In practice, the sandwich covariance matrix is estimated directly from the sample without knowing the true density $g$:
1. The Hessian (bread) is estimated by the observed Hessian:
   $$\\hat{\\mathbf{A}} = -\\frac{1}{n} \\sum_{i=1}^n \\nabla^2 \\ln f(X_i; \\hat{\\boldsymbol{\\theta}})$$
2. The score covariance (meat) is estimated by the empirical outer product of gradients:
   $$\\hat{\\mathbf{B}} = \\frac{1}{n} \\sum_{i=1}^n \\left( \\nabla \\ln f(X_i; \\hat{\\boldsymbol{\\theta}}) \\right) \\left( \\nabla \\ln f(X_i; \\hat{\\boldsymbol{\\theta}}) \\right)^T$$
3. The **Heteroskedasticity-Consistent (Robust) Covariance Estimator** is:
   $$\\widehat{\\text{Var}}(\\hat{\\boldsymbol{\\theta}}) = \\frac{1}{n} \\hat{\\mathbf{A}}^{-1} \\hat{\\mathbf{B}} \\hat{\\mathbf{A}}^{-1}$$

If the model is correctly specified, then by Bartlett's identity $\\mathbf{A} = \\mathbf{B}$, and the sandwich formula simplifies to $\\mathbf{A}^{-1} \\mathbf{A} \\mathbf{A}^{-1} = \\mathbf{A}^{-1} = \\mathbf{I}_1(\\theta)^{-1}$.
The sandwich estimator provides valid standard errors and confidence intervals even when variance assumptions (e.g., homoskedasticity or equi-dispersion) are violated.

## 5.8 Asymptotic Equivalence of the Classical Likelihood Trinity

In parametric hypothesis testing and interval estimation for a null hypothesis $H_0: \\boldsymbol{\\theta} = \\boldsymbol{\\theta}_0$ versus $H_1: \\boldsymbol{\\theta} \\ne \\boldsymbol{\\theta}_0$, three classical large-sample test statistics form the celebrated **Likelihood Trinity**:

1. **The Wald Test ($W_n$)**:
   Measures the squared distance between the unconstrained MLE $\\hat{\\boldsymbol{\\theta}}$ and the hypothesized value $\\boldsymbol{\\theta}_0$, weighted by the Fisher Information curvature:
   $$W_n = n (\\hat{\\boldsymbol{\\theta}} - \\boldsymbol{\\theta}_0)^T I_1(\\hat{\\boldsymbol{\\theta}}) (\\hat{\\boldsymbol{\\theta}} - \\boldsymbol{\\theta}_0)$$
   *Computational Requirement*: Requires fitting only the unrestricted model.
2. **The Rao Score / Lagrange Multiplier Test ($R_n$)**:
   Evaluates how close the score vector is to zero when evaluated at the restricted null parameter $\\boldsymbol{\\theta}_0$:
   $$R_n = \\frac{1}{n} \\mathbf{S}_n(\\boldsymbol{\\theta}_0)^T I_1(\\boldsymbol{\\theta}_0)^{-1} \\mathbf{S}_n(\\boldsymbol{\\theta}_0)$$
   *Computational Requirement*: Requires fitting only the restricted model under $H_0$, avoiding unconstrained numerical optimization entirely.
3. **The Likelihood Ratio Test (Wilks' Test, $\\Lambda_n$)**:
   Measures the drop in the maximized log-likelihood between the unrestricted and restricted models:
   $$\\Lambda_n = 2 \\left[ \\ell_n(\\hat{\\boldsymbol{\\theta}}) - \\ell_n(\\boldsymbol{\\theta}_0) \\right]$$
   *Computational Requirement*: Requires fitting both the restricted and unrestricted models.

### Theorem: Asymptotic Equivalence under the Null
Under standard Cramér regularity conditions, under the null hypothesis $H_0$:

$$W_n = \\Lambda_n + o_P(1) = R_n + o_P(1) \\xrightarrow{d} \\chi_k^2 \\quad \\text{as } n \\to \\infty$$

All three test statistics share the identical limiting Chi-square distribution with $k$ degrees of freedom. Under local contiguous alternatives $\\boldsymbol{\\theta}_n = \\boldsymbol{\\theta}_0 + \\mathbf{h} / \\sqrt{n}$, all three tests achieve identical asymptotic power, forming the backbone of modern likelihood inference.

## 5.9 Superefficiency and Hodges' Counterexample

Can an estimator ever achieve an asymptotic variance strictly smaller than the Cramér–Rao bound $\\frac{1}{I_1(\\theta)}$? In 1951, Joseph Hodges constructed a famous counterexample proving that non-regular estimators can exhibit **superefficiency** at isolated parameter points.

### Hodges' Superefficient Estimator
Let $X_1, \\dots, X_n \\stackrel{\\text{i.i.d.}}{\\sim} \\mathcal{N}(\\theta, 1)$. Here $I_1(\\theta) = 1$, so the classical CRLB is $1$. The sample mean $\\bar{X}_n$ satisfies $\\sqrt{n}(\\bar{X}_n - \\theta) \\sim \\mathcal{N}(0, 1)$ for all $\\theta$.
Define Hodges' estimator as:

$$T_n = \\begin{cases} \\bar{X}_n & \\text{if } |\\bar{X}_n| > n^{-1/4} \\\\ 0 & \\text{if } |\\bar{X}_n| \\le n^{-1/4} \\end{cases}$$

Now analyze the limiting distribution of $\\sqrt{n}(T_n - \\theta)$:
1. **Case 1 ($\\theta \\ne 0$)**:
   Since $\\bar{X}_n \\xrightarrow{\\text{a.s.}} \\theta \\ne 0$ and $n^{-1/4} \\to 0$, the probability $\\mathbb{P}(|\\bar{X}_n| \\le n^{-1/4}) \\to 0$ exponentially fast.
   Thus $T_n = \\bar{X}_n$ with probability approaching $1$, so:
   $$\\sqrt{n}(T_n - \\theta) \\xrightarrow{d} \\mathcal{N}(0, 1)$$
   The asymptotic variance is $V(\\theta) = 1$, matching the Cramér–Rao bound.
2. **Case 2 ($\\theta = 0$)**:
   Under $\\theta = 0$, $\\sqrt{n}\\bar{X}_n \\sim \\mathcal{N}(0, 1)$, which means $\\bar{X}_n = \\mathcal{O}_P(n^{-1/2})$.
   Because $n^{-1/2} \\ll n^{-1/4}$, the event $|\\bar{X}_n| \\le n^{-1/4}$ occurs with probability approaching $1$:
   $$\\mathbb{P}(|\\bar{X}_n| \\le n^{-1/4}) = \\mathbb{P}(|\\sqrt{n}\\bar{X}_n| \\le n^{1/4}) \\to 1$$
   Thus $T_n = 0$ with probability approaching $1$!
   Consequently:
   $$\\sqrt{n}(T_n - 0) = 0 \\xrightarrow{P} 0$$
   The limiting variance at $\\theta = 0$ is:
   $$V(0) = 0 < 1 = \\frac{1}{I_1(0)}$$
   At $\\theta = 0$, Hodges' estimator has **zero asymptotic variance**—it is superefficient!

### Le Cam's Resolution: Non-Uniform Convergence and Asymptotic Risk
Lucien Le Cam (1953) resolved this apparent paradox:
1. **Measure Zero of Superefficiency**: Le Cam proved that the set of parameter points where an estimator can be superefficient must have **Lebesgue measure zero**.
2. **Catastrophic Penalty near the Superefficient Point**: If one evaluates the risk not at a fixed point, but along a sequence of local drifting parameters $\\theta_n = c / n^{1/4}$, the normalized mean squared error of Hodges' estimator diverges to infinity:
   $$\\lim_{n \\to \\infty} \\mathbb{E}_{\\theta_n}\\left[ n(T_n - \\theta_n)^2 \\right] = \\infty$$
   Superefficiency at $\\theta = 0$ is purchased at the cost of an infinite risk spike in the immediate local neighborhood!

## 5.10 Resampling Asymptotics: Bootstrap and Jackknife Approximations

When sample sizes are moderate, analytical asymptotic Gaussian approximations $\\mathcal{N}(0, I_n^{-1})$ can suffer from skewness and finite-sample distortions. Computer-intensive resampling methods provide non-parametric and parametric approximations to the sampling distribution of the MLE.

### 1. The Nonparametric Bootstrap (Efron, 1979)
Draw $B$ independent resamples $\\mathbf{X}^{*b} = (X_1^{*b}, \\dots, X_n^{*b})$ by sampling $n$ observations uniformly at random **with replacement** from the empirical dataset $\\mathbf{x}$.
For each bootstrap replicate, compute the MLE $\\hat{\\theta}^{*b}$.
The bootstrap standard error is the empirical standard deviation of the bootstrap replicates:

$$\\widehat{\\text{SE}}_{\\text{boot}}(\\hat{\\theta}) = \\sqrt{ \\frac{1}{B - 1} \\sum_{b=1}^B (\\hat{\\theta}^{*b} - \\bar{\\theta}^*)^2 }$$

### 2. The Jackknife (Quenouille–Tukey)
The delete-1 jackknife computes the parameter estimate $\\hat{\\theta}_{(-i)}$ on the subsample of size $n - 1$ obtained by omitting observation $X_i$.
The jackknife bias estimate is:

$$\\widehat{\\text{Bias}}_{\\text{jack}} = (n - 1)(\\bar{\\theta}_{(\\cdot)} - \\hat{\\theta})$$

and the jackknife variance estimator is:

$$\\widehat{\\text{Var}}_{\\text{jack}} = \\frac{n - 1}{n} \\sum_{i=1}^n (\\hat{\\theta}_{(-i)} - \\bar{\\theta}_{(\\cdot)})^2$$

where $\\bar{\\theta}_{(\\cdot)} = \\frac{1}{n} \\sum_{i=1}^n \\hat{\\theta}_{(-i)}$.
Jackknife and bootstrap estimators provide robust, second-order accurate variance estimates that do not require evaluating analytical score derivatives or Hessian matrices.

---

## Fully worked question 1: Full Analytical Proof of Asymptotic Normality for Gaussian Mixture Location Parameters with Explicit Taylor Bounds

### Question
A quantitative trading desk models high-frequency order flow imbalances $X$ using a symmetric two-component Gaussian mixture distribution with equal mixing weights $\\pi_1 = \\pi_2 = 0.5$ and known unit variances $\\sigma_1^2 = \\sigma_2^2 = 1$, but unknown antipodal location parameter $\\theta > 0$:

$$f(x; \\theta) = \\frac{1}{2} \\phi(x - \\theta) + \\frac{1}{2} \\phi(x + \\theta) = \\frac{1}{2\\sqrt{2\\pi}} \\left[ e^{-(x - \\theta)^2/2} + e^{-(x + \\theta)^2/2} \\right]$$

An i.i.d. sample $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ is recorded.

1. Simplify $f(x; \\theta)$ using hyperbolic functions and derive the single-observation log-likelihood $\\ell_1(\\theta; x)$.
2. Calculate the score function $S_1(\\theta; x) = \\frac{\\partial}{\\partial \\theta} \\ell_1(\\theta; x)$ and express it in terms of $\\tanh(\\theta x)$.
3. Compute the second derivative $\\frac{\\partial^2}{\\partial \\theta^2} \\ell_1(\\theta; x)$ and evaluate the Fisher Information $I_1(\\theta)$ as a function of the expectation $\\mathbb{E}_\\theta[X^2 \\text{sech}^2(\\theta X)]$.
4. Provide a complete, rigorous proof that $\\sqrt{n}(\\hat{\\theta}_n - \\theta) \\xrightarrow{d} \\mathcal{N}\\left(0, \\frac{1}{I_1(\\theta)}\\right)$ by bounding the third derivative $\\frac{\\partial^3 \\ell_1}{\\partial \\theta^3}$ by an integrable function $M(x)$ that satisfies Cramér's condition (C6).

### Solution, step 1: Hyperbolic representation and log-likelihood
Recall the definition of the hyperbolic cosine: $\\cosh(u) = \\frac{e^u + e^{-u}}{2}$.
Expand the exponents in the mixture density:

$$(x - \\theta)^2 = x^2 - 2\\theta x + \\theta^2, \\quad (x + \\theta)^2 = x^2 + 2\\theta x + \\theta^2$$

Factor out common terms:

$$f(x; \\theta) = \\frac{1}{2\\sqrt{2\\pi}} e^{-(x^2 + \\theta^2)/2} \\left( e^{\\theta x} + e^{-\\theta x} \\right) = \\frac{1}{\\sqrt{2\\pi}} e^{-(x^2 + \\theta^2)/2} \\cosh(\\theta x)$$

Taking the natural logarithm:

$$\\ell_1(\\theta; x) = -\\frac{1}{2} \\ln(2\\pi) - \\frac{x^2}{2} - \\frac{\\theta^2}{2} + \\ln(\\cosh(\\theta x))$$

### Solution, step 2: Score function derivation
Differentiating $\\ell_1(\\theta; x)$ with respect to $\\theta$:

$$S_1(\\theta; x) = \\frac{\\partial \\ell_1}{\\partial \\theta} = -\\theta + \\frac{1}{\\cosh(\\theta x)} \\frac{\\partial}{\\partial \\theta} \\cosh(\\theta x)$$

Since $\\frac{\\partial}{\\partial \\theta} \\cosh(\\theta x) = x \\sinh(\\theta x)$:

$$S_1(\\theta; x) = -\\theta + x \\frac{\\sinh(\\theta x)}{\\cosh(\\theta x)} = x \\tanh(\\theta x) - \\theta$$

Verify Bartlett's first identity: by symmetry, $f(-x; \\theta) = f(x; \\theta)$, so $X$ is symmetric about zero.
Because $\\tanh(u)$ is an odd function ($\\tanh(-u) = -\\tanh(u)$), the product $x \\tanh(\\theta x)$ is an even function of $x$.
Thus $\\mathbb{E}_\\theta[X \\tanh(\\theta X)] = \\theta$, confirming that $\\mathbb{E}_\\theta[S_1(\\theta; X)] = 0$.

### Solution, step 3: Second derivative and Fisher Information
Differentiate $S_1(\\theta; x)$ once more with respect to $\\theta$:

$$\\frac{\\partial^2 \\ell_1}{\\partial \\theta^2} = \\frac{\\partial}{\\partial \\theta} [x \\tanh(\\theta x) - \\theta] = x \\left( \\text{sech}^2(\\theta x) \\cdot x \\right) - 1 = x^2 \\text{sech}^2(\\theta x) - 1$$

where $\\text{sech}(u) = \\frac{1}{\\cosh(u)}$.
By Bartlett's second identity, the single-observation Fisher Information is:

$$I_1(\\theta) = -\\mathbb{E}_\\theta\\left[ \\frac{\\partial^2 \\ell_1}{\\partial \\theta^2} \\right] = -\\mathbb{E}_\\theta\\left[ X^2 \\text{sech}^2(\\theta X) - 1 \\right] = 1 - \\mathbb{E}_\\theta\\left[ X^2 \\text{sech}^2(\\theta X) \\right]$$

Since $0 < \\text{sech}^2(u) \\le 1$ and $\\text{sech}^2(u) \\to 0$ as $|u| \\to \\infty$, we have $0 < I_1(\\theta) < 1$.
As $\\theta \\to 0^+$, $\\text{sech}^2(0) = 1$ and $\\mathbb{E}_0[X^2] = 1$, giving $I_1(0) = 1 - 1 = 0$ (loss of identifiability at $\\theta = 0$).
For any $\\theta > 0$, $I_1(\\theta) > 0$.

### Solution, step 4: Bounding the third derivative for Cramér regularity
Compute the third derivative of $\\ell_1(\\theta; x)$:

$$\\frac{\\partial^3 \\ell_1}{\\partial \\theta^3} = \\frac{\\partial}{\\partial \\theta} [x^2 \\text{sech}^2(\\theta x) - 1] = x^2 \\left( 2 \\text{sech}(\\theta x) \\cdot [-\\text{sech}(\\theta x) \\tanh(\\theta x)] \\cdot x \\right)$$

$$= -2 x^3 \\text{sech}^2(\\theta x) \\tanh(\\theta x)$$

We seek a dominating function $M(x)$ on a neighborhood $\\mathcal{U} = [\\theta_0 - \\delta, \\theta_0 + \\delta]$ with $\\theta_0 - \\delta > 0$:
Recall that for all real $u$:
$|\\tanh(u)| \\le 1$ and $|\\text{sech}^2(u)| \\le 1$.
Therefore:

$$\\left| \\frac{\\partial^3 \\ell_1(x; \\theta)}{\\partial \\theta^3} \\right| = 2 |x|^3 \\text{sech}^2(\\theta x) |\\tanh(\\theta x)| \\le 2 |x|^3 \\cdot 1 \\cdot 1 = 2 |x|^3$$

Set $M(x) = 2 |x|^3$.
Now compute the expectation of $M(X)$ under the true distribution:

$$\\mathbb{E}_{\\theta_0}[M(X)] = 2 \\mathbb{E}_{\\theta_0}[|X|^3]$$

Since $X$ is a mixture of two normal distributions $\\mathcal{N}(\\theta_0, 1)$ and $\\mathcal{N}(-\\theta_0, 1)$:
If $Z \\sim \\mathcal{N}(\\mu, 1)$, all polynomial moments of $Z$ are finite:

$$\\mathbb{E}[|X|^3] \\le \\mathbb{E}[(|Z| + \\theta_0)^3] < \\infty$$

Because $\\mathbb{E}_{\\theta_0}[M(X)] < \\infty$, Cramér's Condition (C6) holds uniformly!
By Theorem 5.3, the Taylor expansion:

$$\\sqrt{n}(\\hat{\\theta}_n - \\theta_0) = \\frac{\\frac{1}{\\sqrt{n}} \\sum_{i=1}^n S_1(\\theta_0; X_i)}{-\\frac{1}{n} \\sum_{i=1}^n \\ell_1''(\\theta_n^*; X_i)}$$

satisfies:
- Numerator $\\xrightarrow{d} \\mathcal{N}(0, I_1(\\theta_0))$ by the Lindeberg–Lévy Central Limit Theorem.
- Denominator $\\xrightarrow{P} I_1(\\theta_0)$ by the Weak Law of Large Numbers and remainder domination by $M(x)$.
- By Slutsky's Theorem:
  $$\\sqrt{n}(\\hat{\\theta}_n - \\theta_0) \\xrightarrow{d} \\mathcal{N}\\left(0, \\frac{1}{I_1(\\theta_0)}\\right)$$
This completes the rigorous proof.

---

## Fully worked question 2: Sandwich Covariance Derivation for Poisson Regression under Overdispersion (Quasi-Poisson Modeling)

### Question
An environmental health agency investigates daily emergency hospital admissions for acute respiratory distress across $n$ urban metropolitan districts. The number of admissions $Y_i$ in district $i$ is modeled via Poisson regression with log link and a single covariate $x_i$ (daily particulate matter concentration $\\text{PM}_{2.5}$):

$$\\mathbb{P}(Y_i = y_i \\mid x_i; \\beta) = \\frac{e^{-\\mu_i} \\mu_i^{y_i}}{y_i!}, \\quad \\text{where } \\mu_i = e^{\\beta x_i}$$

The true data-generating mechanism, however, exhibits severe **overdispersion** (variance exceeding the mean) due to unobserved neighborhood susceptibility, with true moments:

$$\\mathbb{E}[Y_i \\mid x_i] = \\mu_i = e^{\\beta_0 x_i}, \\quad \\text{Var}(Y_i \\mid x_i) = \\phi \\mu_i = \\phi e^{\\beta_0 x_i}$$

where $\\phi > 1$ is the overdispersion parameter (dispersion index).

1. Write down the quasi-log-likelihood $\\ell_n(\\beta)$ and derive the score equation $\\frac{d\\ell_n}{d\\beta} = 0$.
2. Prove that the Quasi-Maximum Likelihood Estimator $\\hat{\\beta}$ remains **consistent** for the true regression parameter $\\beta_0$ despite overdispersion.
3. Compute the theoretical Hessian matrix $\\mathbf{A}(\\beta_0) = -\\mathbb{E}\\left[ \\frac{d^2 \\ell_n}{d\\beta^2} \\right]$ (the "bread") and the variance of the score function $\\mathbf{B}(\\beta_0) = \\text{Var}\\left( \\frac{d\\ell_n}{d\\beta} \\right)$ (the "meat").
4. Evaluate the **Huber–White sandwich covariance estimator** $V_{\\text{sandwich}} = \\mathbf{A}^{-1} \\mathbf{B} \\mathbf{A}^{-1}$ and determine the exact variance inflation factor resulting from overdispersion compared to the naive model-based variance.

### Solution, step 1: Quasi-log-likelihood and score equation
The Poisson log-likelihood contribution for observation $(x_i, y_i)$ is:

$$\\ell_i(\\beta) = y_i \\ln(\\mu_i) - \\mu_i - \\ln(y_i!) = y_i (\\beta x_i) - e^{\\beta x_i} - \\ln(y_i!)$$

Summing across all $n$ independent observations:

$$\\ell_n(\\beta) = \\sum_{i=1}^n \\left[ y_i \\beta x_i - e^{\\beta x_i} - \\ln(y_i!) \\right]$$

Differentiating with respect to $\\beta$ gives the Score equation:

$$S_n(\\beta) = \\frac{d\\ell_n}{d\\beta} = \\sum_{i=1}^n x_i (y_i - e^{\\beta x_i}) = \\sum_{i=1}^n x_i (y_i - \\mu_i) = 0$$

### Solution, step 2: Consistency under overdispersion
To verify consistency, evaluate the expected value of the score function under the true data-generating distribution where $\\mathbb{E}[Y_i \\mid x_i] = e^{\\beta_0 x_i}$:

$$\\mathbb{E}[S_n(\\beta_0)] = \\sum_{i=1}^n x_i \\mathbb{E}[Y_i - e^{\\beta_0 x_i} \\mid x_i] = \\sum_{i=1}^n x_i (e^{\\beta_0 x_i} - e^{\\beta_0 x_i}) = 0$$

Because the conditional mean function $\\mu_i(\\beta) = e^{\\beta x_i}$ is correctly specified, the score function has zero expectation at the true parameter $\\beta_0$.
Furthermore, the second derivative is:

$$\\frac{d^2 \\ell_n}{d\\beta^2} = -\\sum_{i=1}^n x_i^2 e^{\\beta x_i} < 0$$

Because $\\frac{d^2 \\ell_n}{d\\beta^2}$ is strictly negative everywhere, the log-likelihood is strictly concave.
By the Uniform Law of Large Numbers, $\\hat{\\beta}_n \\xrightarrow{P} \\beta_0$.
**Conclusion**: The Quasi-MLE $\\hat{\\beta}$ is strictly consistent for $\\beta_0$, even though the Poisson variance assumption fails completely!

### Solution, step 3: Evaluation of the Hessian $\\mathbf{A}$ and Score Variance $\\mathbf{B}$
**1. The Hessian Matrix (Bread)**:

$$\\mathbf{A}(\\beta_0) = -\\mathbb{E}\\left[ \\frac{d^2 \\ell_n}{d\\beta^2} \\right] = -\\mathbb{E}\\left[ -\\sum_{i=1}^n x_i^2 e^{\\beta_0 x_i} \\right] = \\sum_{i=1}^n x_i^2 e^{\\beta_0 x_i} = \\sum_{i=1}^n x_i^2 \\mu_i$$

Notice that $\\mathbf{A}(\\beta_0)$ depends only on the mean function $\\mu_i$, which is correctly specified.

**2. The Score Variance (Meat)**:
The score is $S_n(\\beta_0) = \\sum_{i=1}^n x_i (Y_i - \\mu_i)$.
Because observations are independent, the variance of the sum is the sum of variances:

$$\\mathbf{B}(\\beta_0) = \\text{Var}\\left( S_n(\\beta_0) \\right) = \\sum_{i=1}^n x_i^2 \\text{Var}(Y_i \\mid x_i)$$

Now substitute the true overdispersed variance $\\text{Var}(Y_i \\mid x_i) = \\phi \\mu_i$:

$$\\mathbf{B}(\\beta_0) = \\sum_{i=1}^n x_i^2 (\\phi \\mu_i) = \\phi \\sum_{i=1}^n x_i^2 \\mu_i = \\phi \\mathbf{A}(\\beta_0)$$

Notice the remarkable relationship: the score variance $\\mathbf{B}$ is exactly $\\phi$ times the Hessian $\\mathbf{A}$!

### Solution, step 4: Sandwich Covariance Matrix and Inflation Factor
Now evaluate the Huber–White sandwich covariance formula:

$$V_{\\text{sandwich}} = \\mathbf{A}^{-1} \\mathbf{B} \\mathbf{A}^{-1} = \\mathbf{A}^{-1} (\\phi \\mathbf{A}) \\mathbf{A}^{-1} = \\phi \\mathbf{A}^{-1} \\mathbf{A} \\mathbf{A}^{-1} = \\phi \\mathbf{A}^{-1}$$

In contrast, if an analyst naively assumed the Poisson model was correct ($\\phi = 1$), they would report the model-based variance:

$$V_{\\text{naive}} = \\mathbf{A}^{-1} = \\frac{1}{\\sum_{i=1}^n x_i^2 \\mu_i}$$

Comparing the two:

$$\\frac{V_{\\text{sandwich}}}{V_{\\text{naive}}} = \\frac{\\phi \\mathbf{A}^{-1}}{\\mathbf{A}^{-1}} = \\phi$$

The actual estimation variance is **exactly $\\phi$ times larger** than the naive model-based variance!
If overdispersion is $\\phi = 4$, the naive standard error is $\\sqrt{V_{\\text{naive}}} = \\frac{1}{2} \\sqrt{V_{\\text{sandwich}}}$. An analyst reporting naive confidence intervals would produce intervals that are $50\\%$ too narrow, leading to severe Type I error inflation (spurious statistical significance). The Huber–White sandwich estimator automatically multiplies the variance by $\\hat{\\phi} = \\frac{1}{n-1} \\sum \\frac{(y_i - \\hat{\\mu}_i)^2}{\\hat{\\mu}_i}$, restoring exact nominal coverage.

---

## Fully worked question 3: Asymptotic Relative Efficiency (ARE) Comparison of MLE, MOM, and Sample Median in Double Exponential (Laplace) Distributions

### Question
In structural vibration monitoring of railway bridges, heavy mechanical impacts generate acoustic emissions with heavy-tailed, sharp-peaked noise modeled by a Laplace (Double Exponential) distribution with unknown location parameter $\\theta \\in \\mathbb{R}$ and known scale parameter $\\beta = 1$:

$$f(x; \\theta) = \\frac{1}{2} e^{-|x - \\theta|}, \\quad -\\infty < x < \\infty$$

An independent sample of vibration readings $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ is observed ($n$ odd).
Three candidate point estimators for $\\theta$ are considered:
- **Estimator 1 (Method of Moments / Sample Mean)**: $T_1 = \\bar{X}_n = \\frac{1}{n} \\sum_{i=1}^n X_i$.
- **Estimator 2 (Sample Median)**: $T_2 = \\tilde{X}_n = X_{((n+1)/2)}$.
- **Estimator 3 (Maximum Likelihood Estimator)**: $T_3 = \\hat{\\theta}_{\\text{MLE}}$.

1. Derive the Maximum Likelihood Estimator $\\hat{\\theta}_{\\text{MLE}}$ and show that it coincides with the sample median $\\tilde{X}_n$.
2. Calculate the theoretical Fisher Information $I_1(\\theta)$ for the Laplace distribution.
3. Determine the asymptotic distributions of $\\sqrt{n}(T_1 - \\theta)$ and $\\sqrt{n}(T_2 - \\theta)$ as $n \\to \\infty$.
4. Calculate the **Asymptotic Relative Efficiency (ARE)** of the sample mean relative to the sample median:
   $$\\text{ARE}(T_1, T_2) = \\frac{\\text{Asymptotic Variance of } T_2}{\\text{Asymptotic Variance of } T_1}$$
   Interpret the efficiency loss of the sample mean in this heavy-tailed setting.

### Solution, step 1: MLE derivation
The joint likelihood of the sample is:

$$L(\\theta; \\mathbf{X}) = \\prod_{i=1}^n \\left( \\frac{1}{2} e^{-|X_i - \\theta|} \\right) = \\frac{1}{2^n} \\exp\\left( -\\sum_{i=1}^n |X_i - \\theta| \\right)$$

Maximizing $L(\\theta)$ is equivalent to minimizing the sum of absolute deviations:

$$\\hat{\\theta}_{\\text{MLE}} = \\arg\\min_\\theta D(\\theta) = \\arg\\min_\\theta \\sum_{i=1}^n |X_i - \\theta|$$

To find the minimum of $D(\\theta)$, analyze its subgradient with respect to $\\theta$:

$$D'(\\theta) = \\sum_{i=1}^n \\text{sgn}(\\theta - X_i) = \\sum_{i=1}^n \\mathbf{1}_{\\{X_i < \\theta\\}} - \\sum_{i=1}^n \\mathbf{1}_{\\{X_i > \\theta\\}}$$

- When $\\theta < X_{(1)}$, $D'(\\theta) = -n < 0$, so $D$ is decreasing.
- As $\\theta$ crosses each order statistic $X_{(k)}$, $D'(\\theta)$ increases by $2$.
- For $n$ odd, setting $D'(\\theta) = 0$ requires the number of observations below $\\theta$ to equal the number of observations above $\\theta$.
The unique minimizer is the middle order statistic:

$$\\hat{\\theta}_{\\text{MLE}} = X_{((n+1)/2)} = \\tilde{X}_n$$

The Maximum Likelihood Estimator of the location parameter of a Laplace distribution is **identically the sample median**!

### Solution, step 2: Fisher Information calculation
The log-density for a single observation is:

$$\\ln f(x; \\theta) = -\\ln(2) - |x - \\theta|$$

For $x \\ne \\theta$, the score is:

$$S_1(\\theta; x) = \\frac{\\partial}{\\partial \\theta} \\ln f(x; \\theta) = \\text{sgn}(x - \\theta) = \\begin{cases} +1 & \\text{if } x > \\theta \\\\ -1 & \\text{if } x < \\theta \\end{cases}$$

Notice that for almost all $x$, $[S_1(\\theta; x)]^2 = (\\pm 1)^2 = 1$.
Therefore:

$$I_1(\\theta) = \\mathbb{E}_\\theta\\left[ (S_1(\\theta; X))^2 \\right] = \\mathbb{E}_\\theta[1] = 1$$

The single-observation Fisher Information is identically $1$.
The Cramér–Rao Lower Bound for any regular estimator is:

$$\\text{CRLB} = \\frac{1}{n I_1(\\theta)} = \\frac{1}{n}$$

### Solution, step 3: Asymptotic distributions of $T_1$ and $T_2$
**1. Estimator 1 (Sample Mean $T_1 = \\bar{X}_n$)**:
The population variance of $X \\sim \\text{Laplace}(\\theta, 1)$ is:

$$\\text{Var}(X) = \\int_{-\\infty}^\\infty (x - \\theta)^2 \\frac{1}{2} e^{-|x - \\theta|} \\, dx = \\int_0^\\infty u^2 e^{-u} \\, du = \\Gamma(3) = 2$$

By the classical Central Limit Theorem:

$$\\sqrt{n}(\\bar{X}_n - \\theta) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2) = \\mathcal{N}(0, 2)$$

The asymptotic variance of the sample mean is $V(\\bar{X}) = 2$.

**2. Estimator 2 (Sample Median $T_2 = \\tilde{X}_n = \\hat{\\theta}_{\\text{MLE}}$)**:
By the asymptotic distribution theorem for sample quantiles, the sample median $\\tilde{X}_n$ from a continuous population with density $f(x)$ and median $\\theta$ is asymptotically normal:

$$\\sqrt{n}(\\tilde{X}_n - \\theta) \\xrightarrow{d} \\mathcal{N}\\left(0, \\frac{1}{4 [f(\\theta)]^2}\\right)$$

Evaluate the Laplace density at the median $x = \\theta$:

$$f(\\theta) = \\frac{1}{2} e^{-|\\theta - \\theta|} = \\frac{1}{2} e^0 = \\frac{1}{2}$$

Substituting $f(\\theta) = \\frac{1}{2}$:

$$\\text{Asymptotic Variance of } \\tilde{X}_n = \\frac{1}{4 (1/2)^2} = \\frac{1}{4 \\times (1/4)} = 1$$

Therefore:

$$\\sqrt{n}(\\tilde{X}_n - \\theta) \\xrightarrow{d} \\mathcal{N}(0, 1)$$

Notice that the asymptotic variance of the sample median is $1 = \\frac{1}{I_1(\\theta)}$! The sample median attains the Cramér–Rao bound in the limit, confirming that it is the asymptotically efficient MLE.

### Solution, step 4: Asymptotic Relative Efficiency (ARE)
The Asymptotic Relative Efficiency of the sample mean relative to the sample median is:

$$\\text{ARE}(\\bar{X}, \\tilde{X}) = \\frac{V(\\tilde{X})}{V(\\bar{X})} = \\frac{1}{2} = 0.50$$

**Interpretation:**
The sample mean has an ARE of only $50\\%$!
This means that to achieve the same estimation precision as a sample median based on $n = 500$ observations, the sample mean requires:

$$n_{\\text{mean}} = \\frac{500}{0.50} = 1,000 \\text{ observations!}$$

Using the sample mean in Laplace or sharp-peaked, heavy-tailed data effectively discards half of the experimental data. The sample median, by ignoring the magnitude of extreme outliers and focusing exclusively on ordering signs, achieves full asymptotic efficiency.
"""

(OUT_DIR / "unit-5.md").write_text(u5_text, encoding="utf-8")
print(f"Unit 5 prose count: {prose_count(u5_text)} words")
