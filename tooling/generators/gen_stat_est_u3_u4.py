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
# UNIT 3: Sufficiency, Completeness & the Rao-Blackwell and Lehmann-Scheffé Theorems
# ==============================================================================
u3_text = """# Unit 3: Sufficiency, Completeness & the Rao–Blackwell and Lehmann–Scheffé Theorems

In statistical inference, an observed sample $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ often resides in a high-dimensional space $\\mathbb{R}^n$. Retaining the complete sequence of raw observations is cumbersome and mathematically redundant when only a low-dimensional summary contains all the empirical evidence relevant to the underlying state of nature. The foundational doctrine of data reduction, pioneered by R. A. Fisher, seeks to compress the high-dimensional data vector $\\mathbf{X}$ into a low-dimensional statistic $T(\\mathbf{X})$ without discarding any information regarding the unknown parameter $\\theta$. In this unit, we rigorously formulate the concept of sufficient statistics, prove the Neyman–Fisher Factorization Theorem, characterize minimal sufficiency and ancillarity, establish Basu's Theorem on stochastic independence, formulate the condition of completeness, and prove the two pillars of optimal point estimation: the Rao–Blackwell Theorem and the Lehmann–Scheffé Theorem.

## 3.1 Data Reduction, Statistics, and Conditional Distributions

Let $(\\mathcal{X}, \\mathcal{A}, \\mathcal{P})$ be a statistical experiment where $\\mathcal{P} = \\{P_\\theta : \\theta \\in \\Theta\\}$ is a dominated family of probability measures. A **statistic** $T: \\mathcal{X} \\to \\mathcal{T}$ is any Borel-measurable mapping from the sample space $\\mathcal{X}$ into a metric space $\\mathcal{T}$ (typically $\\mathbb{R}^k$ with $k < n$). A statistic partitions the sample space $\\mathcal{X}$ into level sets or equivalence classes:

$$A_t = \\{ \\mathbf{x} \\in \\mathcal{X} : T(\\mathbf{x}) = t \\}$$

Observing $T(\\mathbf{X}) = t$ informs the investigator that the realization $\\mathbf{X}$ lies somewhere within the sub-manifold $A_t$, while the specific location within $A_t$ is discarded. 

### Formal Definition of Sufficiency
A statistic $T(\\mathbf{X})$ is said to be **sufficient** for the parameter $\\theta$ (or for the family $\\mathcal{P}$) if the conditional distribution of the sample $\\mathbf{X}$ given $T(\\mathbf{X}) = t$ is completely independent of the parameter $\\theta$ for all $t \\in \\mathcal{T}$.

Formally, for every observable event $A \\in \\mathcal{A}$ and for all $\\theta \\in \\Theta$:

$$\\mathbb{P}_\\theta(\\mathbf{X} \\in A \\mid T(\\mathbf{X}) = t) = P(A \\mid t)$$

where $P(A \\mid t)$ does not depend on $\\theta$.

The operational interpretation of sufficiency is profound: once the numerical value of $T(\\mathbf{X})$ is calculated and made known, the original raw data $\\mathbf{X}$ contain zero additional information regarding $\\theta$. An independent researcher armed only with $T(\\mathbf{x})$ could perform a computer simulation from the conditional distribution $P(\\cdot \\mid t)$ to generate synthetic data $\\mathbf{X}^*$ whose joint distribution under $P_\\theta$ is mathematically indistinguishable from the original experimental data $\\mathbf{X}$. Thus, no inferential precision is sacrificed by discarding the raw data and retaining only $T(\\mathbf{X})$.

## 3.2 The Neyman–Fisher Factorization Theorem

Verifying sufficiency directly from the definition requires calculating the conditional distribution of $\\mathbf{X}$ given $T$, which is often technically demanding. The **Neyman–Fisher Factorization Theorem** provides an elegant, necessary, and sufficient algebraic criterion based directly on the structure of the joint density function.

### Theorem: Neyman-Fisher Factorization Criterion
Let $\\mathcal{P} = \\{f(\\mathbf{x}; \\theta) : \\theta \\in \\Theta\\}$ be a family of probability densities dominated by a $\\sigma$-finite measure $\\mu$ on $\\mathcal{X}$. A statistic $T(\\mathbf{X})$ is sufficient for $\\theta$ if and only if there exist non-negative, measurable functions $g(t; \\theta)$ and $h(\\mathbf{x})$ such that for all $\\mathbf{x} \\in \\mathcal{X}$ and all $\\theta \\in \\Theta$:

$$f(\\mathbf{x}; \\theta) = g(T(\\mathbf{x}); \\theta) \\cdot h(\\mathbf{x})$$

where:
1. $g(T(\\mathbf{x}); \\theta)$ depends on the data $\\mathbf{x}$ exclusively through the summary statistic $T(\\mathbf{x})$, and depends on the unknown parameter $\\theta$.
2. $h(\\mathbf{x})$ is a non-negative function of the data that is strictly independent of the parameter $\\theta$.

#### Proof for the Discrete Case:
Suppose $X$ takes values in a countable sample space $\\mathcal{X}$.
**Necessity ($\implies$)**: Assume $T(\\mathbf{X})$ is sufficient. Then the conditional probability $\\mathbb{P}(\\mathbf{X} = \\mathbf{x} \\mid T(\\mathbf{X}) = T(\\mathbf{x}))$ is independent of $\\theta$. Denote this conditional probability by $h_0(\\mathbf{x})$. By the definition of conditional probability:

$$f(\\mathbf{x}; \\theta) = \\mathbb{P}_\\theta(\\mathbf{X} = \\mathbf{x}) = \\mathbb{P}_\\theta(\\mathbf{X} = \\mathbf{x}, T(\\mathbf{X}) = T(\\mathbf{x})) = \\mathbb{P}_\\theta(T(\\mathbf{X}) = T(\\mathbf{x})) \\cdot \\mathbb{P}(\\mathbf{X} = \\mathbf{x} \\mid T(\\mathbf{X}) = T(\\mathbf{x}))$$

Define $g(t; \\theta) = \\mathbb{P}_\\theta(T(\\mathbf{X}) = t)$ and $h(\\mathbf{x}) = h_0(\\mathbf{x})$. Then:

$$f(\\mathbf{x}; \\theta) = g(T(\\mathbf{x}); \\theta) h(\\mathbf{x})$$

which matches the factorization form exactly.

**Sufficiency ($\\impliedby$)**: Assume $f(\\mathbf{x}; \\theta) = g(T(\\mathbf{x}); \\theta) h(\\mathbf{x})$.
Compute the marginal probability mass function of $T(\\mathbf{X})$:

$$q(t; \\theta) = \\mathbb{P}_\\theta(T(\\mathbf{X}) = t) = \\sum_{\\mathbf{y}: T(\\mathbf{y}) = t} f(\\mathbf{y}; \\theta) = \\sum_{\\mathbf{y}: T(\\mathbf{y}) = t} g(t; \\theta) h(\\mathbf{y}) = g(t; \\theta) \\sum_{\\mathbf{y}: T(\\mathbf{y}) = t} h(\\mathbf{y})$$

Now evaluate the conditional probability for any point $\\mathbf{x}$ such that $T(\\mathbf{x}) = t$:

$$\\mathbb{P}_\\theta(\\mathbf{X} = \\mathbf{x} \\mid T(\\mathbf{X}) = t) = \\frac{\\mathbb{P}_\\theta(\\mathbf{X} = \\mathbf{x})}{\\mathbb{P}_\\theta(T(\\mathbf{X}) = t)} = \\frac{g(t; \\theta) h(\\mathbf{x})}{g(t; \\theta) \\sum_{\\mathbf{y}: T(\\mathbf{y}) = t} h(\\mathbf{y})} = \\frac{h(\\mathbf{x})}{\\sum_{\\mathbf{y}: T(\\mathbf{y}) = t} h(\\mathbf{y})}$$

The term $g(t; \\theta)$ cancels out completely! The resulting conditional probability depends solely on the known function $h(\\cdot)$ and is completely free of $\\theta$. Thus $T(\\mathbf{X})$ is sufficient.

In the general measure-theoretic setting (Halmos and Savage, 1949), the proof utilizes the Radon–Nikodym derivative with respect to a dominating finite mixture measure $\\lambda = \\sum c_i P_{\\theta_i}$, verifying that the conditional expectation operator $\\mathbb{E}_\\theta[\\cdot \\mid T]$ is $\\theta$-invariant.

## 3.3 Minimal Sufficiency, Partition Geometry, and the Lehmann–Scheffé Ratio Criterion

Sufficiency alone does not guarantee maximal data compression. The raw data vector itself, $T_{\\text{raw}}(\\mathbf{X}) = (X_1, \\dots, X_n)$, is trivially sufficient because $h(\\mathbf{x}) = 1$ and $g(\\mathbf{x}; \\theta) = f(\\mathbf{x}; \\theta)$. Similarly, any one-to-one transformation or augmented vector $(T(\\mathbf{X}), X_1)$ is sufficient if $T(\\mathbf{X})$ is sufficient. To achieve the greatest possible simplification, we must identify the statistic that achieves the coarsest sufficient partition of the sample space.

### Definition of Minimal Sufficiency
A sufficient statistic $T(\\mathbf{X})$ is said to be **minimal sufficient** if it is a function of any other sufficient statistic. That is, if $S(\\mathbf{X})$ is any arbitrary sufficient statistic for $\\theta$, then there exists a measurable function $\\psi$ such that:

$$T(\\mathbf{X}) = \\psi(S(\\mathbf{X})) \\quad \\text{almost everywhere}$$

Geometrically, if $\\mathcal{A}_T$ and $\\mathcal{A}_S$ represent the partitions generated by $T$ and $S$, then every level set of $S$ is contained within a level set of $T$. Minimal sufficiency means that $T$ provides the maximum possible data reduction without sacrificing sufficiency.

### The Lehmann–Scheffé Theorem for Minimal Sufficiency
E. L. Lehmann and H. Scheffé (1950) formulated a direct and universal criterion for identifying minimal sufficient statistics through likelihood ratios.

#### Theorem: Likelihood Ratio Criterion
Let $f(\\mathbf{x}; \\theta)$ be the density function of the sample. Suppose there exists a statistic $T(\\mathbf{X})$ such that for any two sample realizations $\\mathbf{x}, \\mathbf{y} \\in \\mathcal{X}$, the likelihood ratio:

$$\\frac{f(\\mathbf{x}; \\theta)}{f(\\mathbf{y}; \\theta)}$$

is completely independent of $\\theta$ if and only if $T(\\mathbf{x}) = T(\\mathbf{y})$.
Then $T(\\mathbf{X})$ is a **minimal sufficient statistic** for $\\theta$.

#### Proof:
1. **Sufficiency of $T$**: Select a fixed representative point $\\mathbf{x}_t$ from each level set $A_t = \\{ \\mathbf{x} : T(\\mathbf{x}) = t \\}$. For any $\\mathbf{x} \\in A_t$, by assumption the ratio $\\frac{f(\\mathbf{x}; \\theta)}{f(\\mathbf{x}_t; \\theta)}$ is independent of $\\theta$. Define:
   $$h(\\mathbf{x}) = \\frac{f(\\mathbf{x}; \\theta)}{f(\\mathbf{x}_{T(\\mathbf{x})}; \\theta)}$$
   and define $g(t; \\theta) = f(\\mathbf{x}_t; \\theta)$. Then:
   $$f(\\mathbf{x}; \\theta) = g(T(\\mathbf{x}); \\theta) \\cdot h(\\mathbf{x})$$
   By the Neyman–Fisher Factorization Theorem, $T(\\mathbf{X})$ is sufficient.
2. **Minimality of $T$**: Let $S(\\mathbf{X})$ be any other sufficient statistic. By factorization, $f(\\mathbf{x}; \\theta) = g_S(S(\\mathbf{x}); \\theta) h_S(\\mathbf{x})$. If $S(\\mathbf{x}) = S(\\mathbf{y})$, then:
   $$\\frac{f(\\mathbf{x}; \\theta)}{f(\\mathbf{y}; \\theta)} = \\frac{g_S(S(\\mathbf{x}); \\theta) h_S(\\mathbf{x})}{g_S(S(\\mathbf{y}); \\theta) h_S(\\mathbf{y})} = \\frac{h_S(\\mathbf{x})}{h_S(\\mathbf{y})}$$
   which is independent of $\\theta$. But by the hypothesis of the theorem, the likelihood ratio is independent of $\\theta$ only if $T(\\mathbf{x}) = T(\\mathbf{y})$. Thus, $S(\\mathbf{x}) = S(\\mathbf{y}) \\implies T(\\mathbf{x}) = T(\\mathbf{y})$, which guarantees that $T$ is a functional mapping of $S$. Hence $T(\\mathbf{X})$ is minimal sufficient.

## 3.4 Ancillary Statistics and Basu's Theorem on Independence

In contrast to sufficient statistics, which concentrate all information regarding $\\theta$, some statistics contain absolutely zero information about $\\theta$.

### Definition of an Ancillary Statistic
A statistic $V(\\mathbf{X})$ is called an **ancillary statistic** (or ancillary) if its marginal probability distribution is completely independent of the unknown parameter $\\theta$.

For example, in a location family $f(x; \\mu) = f_0(x - \\mu)$, the sample range $R = X_{(n)} - X_{(1)}$ or any sample spacing $X_i - X_j$ is ancillary because shifting the data by a constant $\\mu$ leaves all differences unchanged. Similarly, in a scale family $f(x; \\sigma) = \\frac{1}{\\sigma} f_0(x/\\sigma)$, scale-free ratios $X_i / X_j$ or Studentized residuals are ancillary.

While ancillary statistics contain zero direct information about $\\theta$, they frequently serve as conditioning variables that indicate the precision or reliability of an experiment.

### Basu's Theorem
In 1955, Debabrata Basu discovered a remarkable theorem connecting sufficiency, completeness, and ancillarity that allows statisticians to establish the statistical independence of two random variables without ever evaluating a joint integral or convolution.

#### Theorem: Basu's Theorem
If $T(\\mathbf{X})$ is a **complete sufficient statistic** for a parameter $\\theta$, and $V(\\mathbf{X})$ is any **ancillary statistic**, then $T(\\mathbf{X})$ and $V(\\mathbf{X})$ are **statistically independent** under every $P_\\theta \\in \\mathcal{P}$.

#### Proof:
Let $B$ be any Borel set in the range of $V$. Because $V$ is ancillary, the marginal probability $\\mathbb{P}(V(\\mathbf{X}) \\in B) = p_B$ is a constant independent of $\\theta$.
Now, consider the conditional probability of the event $\\{V \\in B\\}$ given $T$:

$$\\eta(T) = \\mathbb{P}(V(\\mathbf{X}) \\in B \\mid T(\\mathbf{X}))$$

Because $T$ is a sufficient statistic, this conditional probability is independent of $\\theta$, making $\\eta(T)$ a legitimate statistic.
By the law of total expectation:

$$\\mathbb{E}_\\theta[\\eta(T)] = \\mathbb{E}_\\theta[\\mathbb{P}(V \\in B \\mid T)] = \\mathbb{P}_\\theta(V \\in B) = p_B \\quad \\forall \\theta \\in \\Theta$$

Rearranging this expectation:

$$\\mathbb{E}_\\theta[\\eta(T) - p_B] = 0 \\quad \\forall \\theta \\in \\Theta$$

Now, consider the function $g(T) = \\eta(T) - p_B$. Since $T$ is a **complete** statistic, the only function whose expectation is identically zero across the entire parameter space is the zero function almost everywhere:

$$\\eta(T) - p_B = 0 \\quad \\text{a.e. } P_\\theta \\implies \\mathbb{P}(V \\in B \\mid T) = p_B = \\mathbb{P}(V \\in B) \\quad \\text{a.e.}$$

Because the conditional distribution of $V$ given $T$ equals the marginal distribution of $V$ for all measurable sets $B$, $T(\\mathbf{X})$ and $V(\\mathbf{X})$ are strictly statistically independent.

#### Applications of Basu's Theorem:
Basu's Theorem provides an instant proof that for an i.i.d. Gaussian sample $X_1, \\dots, X_n \\sim \\mathcal{N}(\\mu, \\sigma^2)$:
- The sample mean $\\bar{X}$ is complete sufficient for $\\mu$ when $\\sigma^2$ is fixed.
- The sample variance $S^2 = \\frac{1}{n-1} \\sum (X_i - \\bar{X})^2$ is translation-invariant, hence ancillary for $\\mu$.
- By Basu's Theorem, **$\\bar{X}$ and $S^2$ are strictly independent**, without any tedious orthogonal rotations or Cochran's theorem proofs!

## 3.5 Completeness and Bounded Completeness of Statistical Families

Completeness is a strong uniqueness property of a family of distributions that prevents distinct functions of a sufficient statistic from having identical expectations.

### Formal Definition of Completeness
Let $\\mathcal{P} = \\{P_\\theta : \\theta \\in \\Theta\\}$ be a family of probability measures on $(\\mathcal{X}, \\mathcal{A})$, and let $T(\\mathbf{X})$ be a statistic with induced family of distributions $\\mathcal{P}_T = \\{P_{\\theta}^T : \\theta \\in \\Theta\\}$.
The statistic $T$ (or the family $\\mathcal{P}_T$) is said to be **complete** if for any measurable real-valued function $g$:

$$\\mathbb{E}_\\theta[g(T)] = 0 \\quad \\forall \\theta \\in \\Theta \\implies \\mathbb{P}_\\theta(g(T) = 0) = 1 \\quad \\forall \\theta \\in \\Theta$$

If this condition holds only for all bounded measurable functions $g$ (i.e., $\\sup_t |g(t)| < \\infty$), the statistic $T$ is said to be **boundedly complete**. Completeness implies bounded completeness, but the converse is not true.

### Operational Meaning: Uniqueness of Estimators
Suppose $T$ is complete, and suppose we have two estimators $g_1(T)$ and $g_2(T)$ that are both unbiased estimators of the same parametric function $\\tau(\\theta)$:

$$\\mathbb{E}_\\theta[g_1(T)] = \\tau(\\theta) \\quad \\text{and} \\quad \\mathbb{E}_\\theta[g_2(T)] = \\tau(\\theta) \\quad \\forall \\theta \\in \\Theta$$

Subtracting the two equations:

$$\\mathbb{E}_\\theta[g_1(T) - g_2(T)] = 0 \\quad \\forall \\theta \\in \\Theta$$

By completeness, $g_1(T) - g_2(T) = 0$ almost everywhere. Therefore:

$$g_1(T) = g_2(T) \\quad \\text{a.e.}$$

**Completeness guarantees that there can exist at most one function of $T$ that is unbiased for any given parametric function $\\tau(\\theta)$!**

## 3.6 Completeness in Exponential Families and Laplace Transform Uniqueness

In parametric modeling, proving completeness directly from integrals can be formidable. Fortunately, for exponential families, completeness is guaranteed by the deep analytic properties of the Laplace transform.

### Theorem: Completeness of Exponential Families
Consider a $k$-parameter exponential family with probability density function:

$$f(\\mathbf{x}; \\boldsymbol{\\theta}) = h(\\mathbf{x}) \\exp\\left( \\sum_{j=1}^k \\eta_j(\\boldsymbol{\\theta}) T_j(\\mathbf{x}) - A(\\boldsymbol{\\theta}) \\right)$$

Let $\\mathbf{T}(\\mathbf{X}) = (T_1(\\mathbf{X}), \\dots, T_k(\\mathbf{X}))^T$.
If the natural parameter space:

$$\\mathcal{H} = \\{ \\boldsymbol{\\eta} = (\\eta_1(\\boldsymbol{\\theta}), \\dots, \\eta_k(\\boldsymbol{\\theta}))^T : \\boldsymbol{\\theta} \\in \\Theta \\}$$

contains a $k$-dimensional open rectangle or open ball in $\\mathbb{R}^k$, then the vector statistic $\\mathbf{T}(\\mathbf{X})$ is a **complete minimal sufficient statistic** for $\\boldsymbol{\\theta}$.

#### Proof Sketch (Laplace Transform Uniqueness):
The condition $\\mathbb{E}_{\\boldsymbol{\\eta}}[g(\\mathbf{T})] = 0$ translates into the integral equation:

$$\\int_{\\mathbb{R}^k} g(\\mathbf{t}) e^{\\boldsymbol{\\eta}^T \\mathbf{t}} \\, d\\nu(\\mathbf{t}) = 0 \\quad \\forall \\boldsymbol{\\eta} \\in \\mathcal{H}$$

where $\\nu$ is the base measure induced by $h(\\mathbf{x})$. Decompose $g(\\mathbf{t})$ into its positive and negative parts, $g(\\mathbf{t}) = g^+(\\mathbf{t}) - g^-(\\mathbf{t})$:

$$\\int_{\\mathbb{R}^k} e^{\\boldsymbol{\\eta}^T \\mathbf{t}} g^+(\\mathbf{t}) \\, d\\nu(\\mathbf{t}) = \\int_{\\mathbb{R}^k} e^{\\boldsymbol{\\eta}^T \\mathbf{t}} g^-(\\mathbf{t}) \\, d\\nu(\\mathbf{t})$$

The left and right sides are the bilateral Laplace transforms of the non-negative measures $d\\mu_1(\\mathbf{t}) = g^+(\\mathbf{t}) d\\nu(\\mathbf{t})$ and $d\\mu_2(\\mathbf{t}) = g^-(\\mathbf{t}) d\\nu(\\mathbf{t})$.
By the Lerch–Laplace Inversion Theorem, if two Laplace transforms of Radon measures coincide on an open set in $\\mathbb{R}^k$, their underlying measures must be identical: $\\mu_1 \\equiv \\mu_2$. Thus $g^+(\\mathbf{t}) = g^-(\\mathbf{t})$ almost everywhere, implying $g(\\mathbf{t}) = 0$ almost everywhere.

If the natural parameter space $\\mathcal{H}$ is curved or restricted to a lower-dimensional manifold (such as $\\mathcal{N}(\\theta, \\theta^2)$ where $\\eta_1 = 1/\\theta$ and $\\eta_2 = -1/(2\\theta^2)$), $\\mathcal{H}$ contains no open ball in $\\mathbb{R}^2$, and completeness fails! In curved exponential families, the minimal sufficient statistic is typically not complete.

## 3.7 The Rao–Blackwell Theorem: Variance Reduction via Conditional Expectation

We now turn to the constructive methods of finding optimal estimators. In 1945, C. R. Rao, and independently David Blackwell in 1947, discovered that conditioning any preliminary unbiased estimator on a sufficient statistic strictly improves—or at least never degrades—its performance under any convex loss function.

### Theorem: The Rao–Blackwell Theorem
Let $\\mathbf{X} \\sim P_\\theta$, and let $T(\\mathbf{X})$ be a sufficient statistic for $\\theta$. Let $W(\\mathbf{X})$ be an unbiased estimator of $\\tau(\\theta)$ with $\\text{Var}_\\theta(W) < \\infty$. Define the conditioned statistic:

$$\\phi(T) = \\mathbb{E}[W(\\mathbf{X}) \\mid T(\\mathbf{X})]$$

Then:
1. $\\phi(T)$ is a legitimate estimator that does not depend on $\\theta$.
2. $\\phi(T)$ is an unbiased estimator of $\\tau(\\theta)$:
   $$\\mathbb{E}_\\theta[\\phi(T)] = \\tau(\\theta) \\quad \\forall \\theta \\in \\Theta$$
3. The variance of $\\phi(T)$ is strictly bounded above by the variance of $W$:
   $$\\text{Var}_\\theta(\\phi(T)) \\le \\text{Var}_\\theta(W)$$
   Equality holds if and only if $W$ is already a deterministic function of $T$ almost everywhere ($W = \\phi(T)$ a.e.).

#### Proof:
1. **Observable Statistic**: Because $T$ is sufficient for $\\theta$, the conditional distribution of $\\mathbf{X}$ given $T = t$ is independent of $\\theta$. Therefore, the conditional expectation $\\phi(t) = \\mathbb{E}[W(\\mathbf{X}) \\mid T(\\mathbf{X}) = t]$ does not involve $\\theta$, making $\\phi(T)$ an observable estimator.
2. **Unbiasedness**: By the Law of Total Expectation (tower property):
   $$\\mathbb{E}_\\theta[\\phi(T)] = \\mathbb{E}_\\theta\\left[ \\mathbb{E}[W \\mid T] \\right] = \\mathbb{E}_\\theta[W] = \\tau(\\theta)$$
3. **Variance Reduction**: By the Law of Total Variance (variance decomposition formula):
   $$\\text{Var}_\\theta(W) = \\text{Var}_\\theta\\left( \\mathbb{E}[W \\mid T] \\right) + \\mathbb{E}_\\theta\\left[ \\text{Var}(W \\mid T) \\right] = \\text{Var}_\\theta(\\phi(T)) + \\mathbb{E}_\\theta\\left[ \\text{Var}(W \\mid T) \\right]$$
   Because variance is non-negative, $\\text{Var}(W \\mid T) \\ge 0$, and thus $\\mathbb{E}_\\theta[\\text{Var}(W \\mid T)] \\ge 0$.
   Therefore:
   $$\\text{Var}_\\theta(\\phi(T)) = \\text{Var}_\\theta(W) - \\mathbb{E}_\\theta[\\text{Var}(W \\mid T)] \\le \\text{Var}_\\theta(W)$$
   Equality holds if and only if $\\mathbb{E}_\\theta[\\text{Var}(W \\mid T)] = 0$, which implies $\\text{Var}(W \\mid T) = 0$ almost everywhere, meaning $W$ is a deterministic function of $T$.

### Extension to Convex Loss (Blackwell's Formulation)
If estimation error is evaluated by any strictly convex loss function $L(\\theta, d)$ (such as absolute error $|d - \\theta|$ or asymmetric loss), Jensen's Inequality for conditional expectations yields:

$$\\mathbb{E}_\\theta[L(\\theta, \\phi(T))] = \\mathbb{E}_\\theta[L(\\theta, \\mathbb{E}[W \\mid T])] \\le \\mathbb{E}_\\theta[\\mathbb{E}[L(\\theta, W) \\mid T]] = \\mathbb{E}_\\theta[L(\\theta, W)]$$

Conditioning on a sufficient statistic reduces risk under **every convex loss function**.

## 3.8 The Lehmann–Scheffé Theorem: Constructive Uniqueness of UMVUEs

While the Rao–Blackwell theorem proves that conditioning on a sufficient statistic reduces variance, it does not guarantee that the resulting estimator $\\phi(T)$ has the *absolute minimum* variance among all possible unbiased estimators. What if we had started with a different crude estimator $W^*$? Would conditioning $W^*$ on $T$ produce a different improved estimator $\\phi^*(T)$?

The celebrated **Lehmann–Scheffé Theorem** (1950) provides the definitive answer: if the sufficient statistic is also **complete**, then the Rao–Blackwell estimator is unique and is guaranteed to be the Uniformly Minimum Variance Unbiased Estimator (UMVUE).

### Theorem: The Lehmann–Scheffé Theorem
Let $T(\\mathbf{X})$ be a **complete sufficient statistic** for $\\theta$.
1. If $g(T)$ is any unbiased estimator of $\\tau(\\theta)$ with finite variance, then $g(T)$ is the **unique Uniformly Minimum Variance Unbiased Estimator (UMVUE)** of $\\tau(\\theta)$.
2. If $W(\\mathbf{X})$ is any unbiased estimator of $\\tau(\\theta)$, then the conditioned estimator:
   $$\\phi(T) = \\mathbb{E}[W(\\mathbf{X}) \\mid T(\\mathbf{X})]$$
   is the unique UMVUE of $\\tau(\\theta)$.

#### Proof:
Let $U(\\mathbf{X})$ be any arbitrary unbiased estimator of $\\tau(\\theta)$ with $\\text{Var}_\\theta(U) < \\infty$.
Define $g^*(T) = \\mathbb{E}[U \\mid T]$. By the Rao–Blackwell theorem:
1. $\\mathbb{E}_\\theta[g^*(T)] = \\tau(\\theta)$.
2. $\\text{Var}_\\theta(g^*(T)) \\le \\text{Var}_\\theta(U)$.

Now, suppose $g(T)$ is any function of $T$ that is unbiased for $\\tau(\\theta)$. Then:

$$\\mathbb{E}_\\theta[g(T) - g^*(T)] = \\tau(\\theta) - \\tau(\\theta) = 0 \\quad \\forall \\theta \\in \\Theta$$

Because $T$ is complete, this implies that:

$$g(T) = g^*(T) \\quad \\text{almost everywhere } P_\\theta$$

Therefore, $g(T)$ is identical to $g^*(T)$ almost everywhere!
Consequently:

$$\\text{Var}_\\theta(g(T)) = \\text{Var}_\\theta(g^*(T)) \\le \\text{Var}_\\theta(U)$$

Because $U$ was completely arbitrary, $g(T)$ has a variance less than or equal to that of **every** competing unbiased estimator across the entire parameter space $\\Theta$. Furthermore, if another estimator $U^*$ had equal variance, equality in Cauchy–Schwarz would force $U^* = g(T)$ a.e. Thus $g(T)$ is the unique UMVUE.

### Two Universal Recipes for Constructing UMVUEs
The Lehmann–Scheffé Theorem provides two distinct operational recipes for finding UMVUEs:
1. **Method 1 (Direct Unbiasing of the Complete Sufficient Statistic)**: Find a complete sufficient statistic $T$. Propose a candidate function $g(T)$. Compute its expectation $\\mathbb{E}_\\theta[g(T)]$. If $\\mathbb{E}_\\theta[g(T)] = \\tau(\\theta)$, then $g(T)$ is immediately the UMVUE.
2. **Method 2 (Rao-Blackwell Conditioning)**: Construct a trivial, naive unbiased estimator $W(\\mathbf{X})$ (even one depending only on the single first observation $X_1$). Then evaluate the conditional expectation $\\phi(T) = \\mathbb{E}[W \\mid T]$. By Lehmann–Scheffé, $\\phi(T)$ is automatically the UMVUE.

## 3.9 Rao-Blackwellization in Practice: Conditioning on Sufficient Statistics

To appreciate the practical power of Method 2, consider estimating the probability of zero occurrences in a Poisson process: $\\tau(\\lambda) = \\mathbb{P}(X = 0) = e^{-\\lambda}$, based on an i.i.d. sample $X_1, \\dots, X_n \\sim \\text{Poisson}(\\lambda)$.
The sum $T = \\sum_{i=1}^n X_i \\sim \\text{Poisson}(n\\lambda)$ is a complete sufficient statistic.
Propose the simplest conceivable unbiased estimator of $\\tau(\\lambda)$ using only the first observation:

$$W = \\mathbf{1}_{\\{X_1 = 0\\}}$$

Notice that $\\mathbb{E}[W] = \\mathbb{P}(X_1 = 0) = e^{-\\lambda}$, so $W$ is unbiased, but terribly crude: its variance is $e^{-\\lambda}(1 - e^{-\\lambda})$.
Now, condition $W$ on the complete sufficient statistic $T = t$:

$$\\phi(t) = \\mathbb{E}[W \\mid T = t] = \\mathbb{P}(X_1 = 0 \\mid \\sum_{i=1}^n X_i = t) = \\frac{\\mathbb{P}(X_1 = 0, \\sum_{i=2}^n X_i = t)}{\\mathbb{P}(\\sum_{i=1}^n X_i = t)}$$

Using the fact that $\\sum_{i=2}^n X_i \\sim \\text{Poisson}((n-1)\\lambda)$:

$$\\phi(t) = \\frac{e^{-\\lambda} \\cdot \\frac{((n-1)\\lambda)^t e^{-(n-1)\\lambda}}{t!}}{\\frac{(n\\lambda)^t e^{-n\\lambda}}{t!}} = \\frac{(n-1)^t \\lambda^t}{n^t \\lambda^t} = \\left( \\frac{n-1}{n} \\right)^t = \\left( 1 - \\frac{1}{n} \\right)^t$$

By the Lehmann–Scheffé Theorem, the estimator:

$$\\phi(T) = \\left( 1 - \\frac{1}{n} \\right)^{\\sum_{i=1}^n X_i}$$

is the **unique UMVUE** of $e^{-\\lambda}$! Notice how conditioning effortlessly transformed a binary indicator $W \\in \\{0, 1\\}$ into a smooth, highly efficient exponential estimator.

## 3.10 Inadmissibility of Raw Estimators and Boundary Sufficiency

A fundamental consequence of the Rao–Blackwell Theorem is that any estimator $W(\\mathbf{X})$ that is not almost surely a function of a sufficient statistic is **strictly inadmissible** under squared error loss, provided that $\\mathbb{E}[\\text{Var}(W \\mid T)] > 0$. Conditioning on $T$ eliminates unnecessary Monte Carlo noise without changing the mean.

Furthermore, in distributions with parameter-dependent boundaries (such as $\\text{Uniform}(\\theta_1, \\theta_2)$ or Pareto families), the complete sufficient statistic is composed of extreme order statistics $(X_{(1)}, X_{(n)})$. Rao-Blackwell conditioning on order statistics concentrates probability mass on the boundary simplex, providing optimal non-parametric and parametric estimators that achieve $\\mathcal{O}(1/n^2)$ convergence rates.

---

## Fully worked question 1: Minimal Sufficiency and Completeness in Two-Parameter Uniform and Shifted Exponential Models

### Question
A precision machining facility manufactures ceramic micro-cylinders whose diameters $X$ follow a two-parameter Uniform distribution on an unknown interval $[\\theta_1, \\theta_2]$ with $-\\infty < \\theta_1 < \\theta_2 < \\infty$:

$$f(x; \\theta_1, \\theta_2) = \\frac{1}{\\theta_2 - \\theta_1} \\mathbf{1}_{[\\theta_1, \\theta_2]}(x)$$

An independent sample of cylinder diameters $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ of size $n \\ge 2$ is measured.

1. Write down the joint density function $f_n(\\mathbf{x}; \\theta_1, \\theta_2)$ using indicator functions of the order statistics $X_{(1)} = \\min(X_1, \\dots, X_n)$ and $X_{(n)} = \\max(X_1, \\dots, X_n)$.
2. Using the Lehmann–Scheffé likelihood ratio criterion, prove rigorously that the two-dimensional vector of extreme order statistics $\\mathbf{T}(\\mathbf{X}) = (X_{(1)}, X_{(n)})^T$ is a **minimal sufficient statistic** for $\\boldsymbol{\\theta} = (\\theta_1, \\theta_2)^T$.
3. Derive the joint probability density function of $(X_{(1)}, X_{(n)})$ and prove that $\\mathbf{T}(\\mathbf{X})$ is a **complete statistic** for $\\boldsymbol{\\theta}$.
4. Construct the unique UMVUE for the interval length (spread) $\\tau(\\boldsymbol{\\theta}) = \\theta_2 - \\theta_1$ and calculate its exact variance.

### Solution, step 1: Joint density using order statistics
The joint density of the independent sample is:

$$f_n(\\mathbf{x}; \\theta_1, \\theta_2) = \\prod_{i=1}^n \\left( \\frac{1}{\\theta_2 - \\theta_1} \\mathbf{1}_{[\\theta_1, \\theta_2]}(x_i) \\right) = \\frac{1}{(\\theta_2 - \\theta_1)^n} \\prod_{i=1}^n \\mathbf{1}_{\\{x_i \\ge \\theta_1\\}} \\mathbf{1}_{\\{x_i \\le \\theta_2\\}}$$

The product of indicator functions is non-zero if and only if every single observation satisfies $\\theta_1 \\le x_i \\le \\theta_2$. This condition is satisfied if and only if the minimum observation is at least $\\theta_1$ and the maximum observation is at most $\\theta_2$:

$$f_n(\\mathbf{x}; \\theta_1, \\theta_2) = \\frac{1}{(\\theta_2 - \\theta_1)^n} \\mathbf{1}_{\\{x_{(1)} \\ge \\theta_1\\}} \\mathbf{1}_{\\{x_{(n)} \\le \\theta_2\\}}$$

where $x_{(1)} = \\min_{1 \\le i \\le n} x_i$ and $x_{(n)} = \\max_{1 \\le i \\le n} x_i$.

### Solution, step 2: Proof of minimal sufficiency via likelihood ratio criterion
Consider two sample realizations $\\mathbf{x} = (x_1, \\dots, x_n)$ and $\\mathbf{y} = (y_1, \\dots, y_n)$.
The likelihood ratio is:

$$\\frac{f_n(\\mathbf{x}; \\theta_1, \\theta_2)}{f_n(\\mathbf{y}; \\theta_1, \\theta_2)} = \\frac{\\mathbf{1}_{\\{x_{(1)} \\ge \\theta_1\\}} \\mathbf{1}_{\\{x_{(n)} \\le \\theta_2\\}}}{\\mathbf{1}_{\\{y_{(1)} \\ge \\theta_1\\}} \\mathbf{1}_{\\{y_{(n)} \\le \\theta_2\\}}}$$

We investigate under what conditions this ratio is constant and independent of $(\\theta_1, \\theta_2)$ across the entire domain $\\{(\\theta_1, \\theta_2) : \\theta_1 < \\theta_2\\}$.
Suppose $(x_{(1)}, x_{(n)}) = (y_{(1)}, y_{(n)})$. Then:
$x_{(1)} = y_{(1)}$ and $x_{(n)} = y_{(n)}$. The indicator functions in the numerator and denominator are identical for every parameter pair, so the ratio equals $1$, which is independent of $\\boldsymbol{\\theta}$.

Conversely, suppose $(x_{(1)}, x_{(n)}) \\ne (y_{(1)}, y_{(n)})$. Then either $x_{(1)} \\ne y_{(1)}$ or $x_{(n)} \\ne y_{(n)}$ (or both).
Without loss of generality, suppose $x_{(1)} < y_{(1)}$. Then we can choose a parameter $\\theta_1$ such that:

$$x_{(1)} < \\theta_1 < y_{(1)}$$

For this choice of $\\theta_1$, $\\mathbf{1}_{\\{x_{(1)} \\ge \\theta_1\\}} = 0$, while $\\mathbf{1}_{\\{y_{(1)} \\ge \\theta_1\\}} = 1$. The likelihood ratio evaluates to $0$.
However, if we choose $\\theta_1 < x_{(1)}$, then both indicators are $1$, and the ratio is $1$.
Thus, the likelihood ratio depends explicitly on $\\theta_1$.
By the Lehmann–Scheffé theorem, the likelihood ratio is independent of $(\\theta_1, \\theta_2)$ if and only if:

$$(x_{(1)}, x_{(n)}) = (y_{(1)}, y_{(n)})$$

This rigorously proves that $\\mathbf{T}(\\mathbf{X}) = (X_{(1)}, X_{(n)})^T$ is a **minimal sufficient statistic**.

### Solution, step 3: Joint density and proof of completeness
Let $U = X_{(1)}$ and $V = X_{(n)}$. The joint density of the minimum and maximum order statistics from a sample of size $n$ from a continuous distribution with CDF $F(x)$ and PDF $f(x)$ is:

$$g(u, v) = n(n - 1) [F(v) - F(u)]^{n - 2} f(u) f(v), \\quad u < v$$

For $\\text{Uniform}(\\theta_1, \\theta_2)$, $f(x) = \\frac{1}{\\theta_2 - \\theta_1}$ and $F(x) = \\frac{x - \\theta_1}{\\theta_2 - \\theta_1}$. Thus $F(v) - F(u) = \\frac{v - u}{\\theta_2 - \\theta_1}$.
Substituting these:

$$g(u, v; \\theta_1, \\theta_2) = \\frac{n(n - 1)}{(\\theta_2 - \\theta_1)^n} (v - u)^{n - 2}, \\quad \\theta_1 \\le u < v \\le \\theta_2$$

Now test for completeness. Let $h(u, v)$ be any measurable function such that $\\mathbb{E}_{\\theta_1, \\theta_2}[h(U, V)] = 0$ for all $\\theta_1 < \\theta_2$:

$$\\int_{\\theta_1}^{\\theta_2} \\left( \\int_u^{\\theta_2} h(u, v) (v - u)^{n - 2} \\, dv \\right) du = 0 \\quad \\forall \\theta_1 < \\theta_2$$

Differentiating this integral equation with respect to $\\theta_1$ using Leibniz's rule:

$$-\\int_{\\theta_1}^{\\theta_2} h(\\theta_1, v) (v - \\theta_1)^{n - 2} \\, dv = 0 \\quad \\forall \\theta_2 > \\theta_1$$

Now differentiate this resulting equation with respect to $\\theta_2$:

$$-h(\\theta_1, \\theta_2) (\\theta_2 - \\theta_1)^{n - 2} = 0$$

Since $\\theta_2 > \\theta_1$, the term $(\\theta_2 - \\theta_1)^{n - 2} > 0$. Therefore:

$$h(\\theta_1, \\theta_2) = 0 \\quad \\text{almost everywhere}$$

Since $(\\theta_1, \\theta_2)$ was arbitrary, $h(u, v) = 0$ almost everywhere.
This proves that $(X_{(1)}, X_{(n)})^T$ is a **complete statistic**.

### Solution, step 4: UMVUE of interval length $\\theta_2 - \\theta_1$
The sample range is $R = X_{(n)} - X_{(1)} = V - U$.
Compute its expectation:

$$\\mathbb{E}[V - U] = \\int_{\\theta_1}^{\\theta_2} \\int_u^{\\theta_2} (v - u) \\frac{n(n - 1)}{(\\theta_2 - \\theta_1)^n} (v - u)^{n - 2} \\, dv \\, du = \\frac{n(n - 1)}{(\\theta_2 - \\theta_1)^n} \\int_{\\theta_1}^{\\theta_2} \\int_u^{\\theta_2} (v - u)^{n - 1} \\, dv \\, du$$

Integrate with respect to $v$:

$$\\int_u^{\\theta_2} (v - u)^{n - 1} \\, dv = \\left[ \\frac{(v - u)^n}{n} \\right]_u^{\\theta_2} = \\frac{(\\theta_2 - u)^n}{n}$$

Now integrate with respect to $u$:

$$\\int_{\\theta_1}^{\\theta_2} \\frac{(\\theta_2 - u)^n}{n} \\, du = \\left[ -\\frac{(\\theta_2 - u)^{n+1}}{n(n + 1)} \\right]_{\\theta_1}^{\\theta_2} = \\frac{(\\theta_2 - \\theta_1)^{n+1}}{n(n + 1)}$$

Multiplying by the leading constant:

$$\\mathbb{E}[X_{(n)} - X_{(1)}] = \\frac{n(n - 1)}{(\\theta_2 - \\theta_1)^n} \\frac{(\\theta_2 - \\theta_1)^{n+1}}{n(n + 1)} = \\frac{n - 1}{n + 1} (\\theta_2 - \\theta_1)$$

Therefore, an unbiased estimator of $\\tau(\\boldsymbol{\\theta}) = \\theta_2 - \\theta_1$ is:

$$T^*(\mathbf{X}) = \\frac{n + 1}{n - 1} (X_{(n)} - X_{(1)})$$

Because $T^*$ is a function of the complete sufficient statistic $(X_{(1)}, X_{(n)})$, by the Lehmann–Scheffé Theorem, $T^*$ is the **unique Uniformly Minimum Variance Unbiased Estimator (UMVUE)** of $\\theta_2 - \\theta_1$.

To compute its variance, evaluate the second moment $\\mathbb{E}[(V - U)^2]$:

$$\\mathbb{E}[(V - U)^2] = \\frac{n(n - 1)}{(\\theta_2 - \\theta_1)^n} \\int_{\\theta_1}^{\\theta_2} \\left[ \\frac{(\\theta_2 - u)^{n+1}}{n+1} \\right] du = \\frac{n(n - 1)}{(\\theta_2 - \\theta_1)^n} \\frac{(\\theta_2 - \\theta_1)^{n+2}}{(n+1)(n+2)} = \\frac{n(n - 1)}{(n + 1)(n + 2)} (\\theta_2 - \\theta_1)^2$$

Compute $\\text{Var}(V - U)$:

$$\\text{Var}(V - U) = (\\theta_2 - \\theta_1)^2 \\left[ \\frac{n(n - 1)}{(n + 1)(n + 2)} - \\left( \\frac{n - 1}{n + 1} \\right)^2 \\right] = (\\theta_2 - \\theta_1)^2 \\frac{n - 1}{n + 1} \\left[ \\frac{n}{n + 2} - \\frac{n - 1}{n + 1} \\right]$$

$$= (\\theta_2 - \\theta_1)^2 \\frac{n - 1}{n + 1} \\left[ \\frac{n(n + 1) - (n - 1)(n + 2)}{(n + 1)(n + 2)} \\right] = (\\theta_2 - \\theta_1)^2 \\frac{n - 1}{n + 1} \\frac{2}{(n + 1)(n + 2)} = \\frac{2(n - 1)}{(n + 1)^2 (n + 2)} (\\theta_2 - \\theta_1)^2$$

Thus, the exact variance of the UMVUE $T^*$ is:

$$\\text{Var}(T^*) = \\left( \\frac{n + 1}{n - 1} \\right)^2 \\text{Var}(V - U) = \\frac{(n + 1)^2}{(n - 1)^2} \\frac{2(n - 1)}{(n + 1)^2 (n + 2)} (\\theta_2 - \\theta_1)^2 = \\frac{2}{(n - 1)(n + 2)} (\\theta_2 - \\theta_1)^2$$

The variance scales as $\\mathcal{O}(1/n^2)$, demonstrating the super-efficient precision characteristic of boundary order statistics.

---

## Fully worked question 2: Rao-Blackwellization and UMVUE Derivation for Zero-Truncated Poisson Distributions

### Question
In an epidemiological study of rare disease clusters, public health officials examine hospitals that report at least one admitted case during an outbreak. The number of patients $X$ admitted to an affected hospital follows a Zero-Truncated Poisson (ZTP) distribution with parameter $\\lambda > 0$. The probability mass function is given by:

$$f(x; \\lambda) = \\mathbb{P}(X = x) = \\frac{e^{-\\lambda} \\lambda^x}{x! (1 - e^{-\\lambda})}, \\quad x = 1, 2, 3, \\dots$$

An independent random sample $\\mathbf{X} = (X_1, X_2, \\dots, X_n)$ is obtained from $n$ affected hospitals.

1. Prove that the distribution belongs to an exponential family, and identify a complete sufficient statistic $T(\\mathbf{X})$.
2. The investigators wish to estimate the probability that an affected hospital treats exactly one patient:
   $$\\tau(\\lambda) = \\mathbb{P}(X = 1) = \\frac{\\lambda e^{-\\lambda}}{1 - e^{-\\lambda}}$$
   Propose a naive unbiased estimator $W(\\mathbf{X})$ based solely on the first observation $X_1$.
3. Use the Rao–Blackwell conditioning technique to construct the estimator $\\phi(T) = \\mathbb{E}[W \\mid T = t]$. Express $\\phi(T)$ in terms of Stirling numbers of the second kind or explicit combinatorial sums.
4. Verify by the Lehmann–Scheffé Theorem that $\\phi(T)$ is the unique UMVUE of $\\tau(\\lambda)$.

### Solution, step 1: Exponential family and complete sufficient statistic
Express the PMF in exponential family canonical form:

$$f(x; \\lambda) = \\exp\\left( x \\ln(\\lambda) - \\ln(x!) - \\lambda - \\ln(1 - e^{-\\lambda}) \\right) = \\frac{1}{x!} \\exp\\left( x \\ln(\\lambda) - [\\lambda + \\ln(1 - e^{-\\lambda})] \\right)$$

For an i.i.d. sample of size $n$, the joint probability mass function is:

$$f_n(\\mathbf{x}; \\lambda) = \\left( \\prod_{i=1}^n \\frac{1}{x_i!} \\right) \\exp\\left( \\ln(\\lambda) \\sum_{i=1}^n x_i - n [\\lambda + \\ln(1 - e^{-\\lambda})] \\right)$$

By the Neyman–Fisher Factorization Theorem, with:
- $T(\\mathbf{X}) = \\sum_{i=1}^n X_i$
- $g(t; \\lambda) = \\exp(t \\ln(\\lambda) - n[\\lambda + \\ln(1 - e^{-\\lambda})])$
- $h(\\mathbf{x}) = \\prod_{i=1}^n \\frac{1}{x_i!}$

the statistic $T(\\mathbf{X}) = \\sum_{i=1}^n X_i$ is sufficient for $\\lambda$.
Furthermore, the natural parameter is $\\eta = \\ln(\\lambda)$, whose parameter space $\\mathcal{H} = (-\\infty, \\infty)$ is an open interval in $\\mathbb{R}$. By Theorem 3.6, $T(\\mathbf{X}) = \\sum_{i=1}^n X_i$ is a **complete minimal sufficient statistic**.

### Solution, step 2: Naive unbiased estimator
Define the indicator:

$$W(\\mathbf{X}) = \\mathbf{1}_{\\{X_1 = 1\\}} = \\begin{cases} 1 & \\text{if } X_1 = 1 \\\\ 0 & \\text{if } X_1 > 1 \\end{cases}$$

Taking its mathematical expectation:

$$\\mathbb{E}[W] = 1 \\cdot \\mathbb{P}(X_1 = 1) + 0 \\cdot \\mathbb{P}(X_1 > 1) = \\mathbb{P}(X_1 = 1) = \\tau(\\lambda)$$

Thus $W$ is strictly an unbiased estimator of $\\tau(\\lambda)$.

### Solution, step 3: Rao-Blackwell conditioning
By the Rao–Blackwell Theorem, we compute the conditional expectation:

$$\\phi(t) = \\mathbb{E}[W \\mid T = t] = \\mathbb{P}(X_1 = 1 \\mid \\sum_{i=1}^n X_i = t)$$

Using Bayes' formula for discrete distributions:

$$\\phi(t) = \\frac{\\mathbb{P}(X_1 = 1, \\sum_{i=2}^n X_i = t - 1)}{\\mathbb{P}(\\sum_{i=1}^n X_i = t)} = \\frac{\\mathbb{P}(X_1 = 1) \\cdot \\mathbb{P}(\\sum_{i=2}^n X_i = t - 1)}{\\mathbb{P}(\\sum_{i=1}^n X_i = t)}$$

To evaluate the probability mass function of the sum of independent zero-truncated Poisson random variables, recall the combinatorial expansion using **Stirling numbers of the second kind** $\\left\\{ \\begin{matrix} t \\\\ n \\end{matrix} \\right\\}$.
The probability generating function of $X$ is:

$$G_X(s) = \\frac{e^{\\lambda s} - 1}{e^\\lambda - 1}$$

The PGF of the sum $T = \\sum_{i=1}^n X_i$ of $n$ i.i.d. ZTP variables is:

$$G_T(s) = [G_X(s)]^n = \\frac{(e^{\\lambda s} - 1)^n}{(e^\\lambda - 1)^n} = \\frac{n!}{(e^\\lambda - 1)^n} \\sum_{t=n}^\\infty \\left\\{ \\begin{matrix} t \\\\ n \\end{matrix} \\right\\} \\frac{(\\lambda s)^t}{t!}$$

Extracting the coefficient of $s^t$, the exact PMF of $T = \\sum_{i=1}^n X_i$ is:

$$\\mathbb{P}\\left( \\sum_{i=1}^n X_i = t \\right) = \\frac{n! \\lambda^t}{t! (e^\\lambda - 1)^n} \\left\\{ \\begin{matrix} t \\\\ n \\end{matrix} \\right\\}, \\quad t \\ge n$$

Similarly, the sum of the remaining $n - 1$ variables $\\sum_{i=2}^n X_i$ has PMF:

$$\\mathbb{P}\\left( \\sum_{i=2}^n X_i = t - 1 \\right) = \\frac{(n - 1)! \\lambda^{t - 1}}{(t - 1)! (e^\\lambda - 1)^{n - 1}} \\left\\{ \\begin{matrix} t - 1 \\\\ n - 1 \\end{matrix} \\right\\}, \\quad t - 1 \\ge n - 1$$

Now substitute both distributions and $\\mathbb{P}(X_1 = 1) = \\frac{\\lambda e^{-\\lambda}}{1 - e^{-\\lambda}} = \\frac{\\lambda}{e^\\lambda - 1}$ into the ratio:

$$\\phi(t) = \\frac{ \\left( \\frac{\\lambda}{e^\\lambda - 1} \\right) \\left( \\frac{(n - 1)! \\lambda^{t - 1}}{(t - 1)! (e^\\lambda - 1)^{n - 1}} \\left\\{ \\begin{matrix} t - 1 \\\\ n - 1 \\end{matrix} \\right\\} \\right) }{ \\frac{n! \\lambda^t}{t! (e^\\lambda - 1)^n} \\left\\{ \\begin{matrix} t \\\\ n \\end{matrix} \\right\\} }$$

Simplify the parameters $\\lambda$ and $(e^\\lambda - 1)$:
- In the numerator: $\\lambda \\cdot \\lambda^{t-1} = \\lambda^t$. In the denominator: $\\lambda^t$. These cancel completely!
- In the numerator: $(e^\\lambda - 1) \\cdot (e^\\lambda - 1)^{n-1} = (e^\\lambda - 1)^n$. In the denominator: $(e^\\lambda - 1)^n$. These cancel completely!
Simplify the factorials:

$$\\frac{(n - 1)! / (t - 1)!}{n! / t!} = \\frac{(n - 1)!}{n!} \\cdot \\frac{t!}{(t - 1)!} = \\frac{1}{n} \\cdot t = \\frac{t}{n}$$

Therefore, the conditioned estimator evaluates to the clean combinatorial ratio:

$$\\phi(t) = \\frac{t}{n} \\frac{\\left\\{ \\begin{matrix} t - 1 \\\\ n - 1 \\end{matrix} \\right\\}}{\\left\\{ \\begin{matrix} t \\\\ n \\end{matrix} \\right\\}}$$

### Solution, step 4: UMVUE assertion via Lehmann-Scheffé
Because $\\phi(T)$ is a function of the complete sufficient statistic $T = \\sum_{i=1}^n X_i$, by the Lehmann–Scheffé Theorem, the estimator:

$$T^*(\mathbf{X}) = \\frac{\\sum_{i=1}^n X_i}{n} \\frac{\\left\\{ \\begin{matrix} \\sum X_i - 1 \\\\ n - 1 \\end{matrix} \\right\\}}{\\left\\{ \\begin{matrix} \\sum X_i \\\\ n \\end{matrix} \\right\\}}$$

is the **unique Uniformly Minimum Variance Unbiased Estimator (UMVUE)** of $\\mathbb{P}(X = 1)$. Rao-Blackwell conditioning transformed an unstable single-case indicator into an exact, optimal combinatorial statistic that uses all $n$ data points.

---

## Fully worked question 3: Basu's Theorem Applications: Independence of Sample Mean and Sample Variance, and Ratio Statistics

### Question
Let $X_1, X_2, \\dots, X_n$ be an independent and identically distributed random sample of size $n \\ge 3$ from a normal distribution $\\mathcal{N}(\\mu, \\sigma^2)$ where both the mean $\\mu \\in \\mathbb{R}$ and variance $\\sigma^2 > 0$ are unknown.

1. Identify the minimal sufficient statistic $\\mathbf{T}(\\mathbf{X}) = (\\bar{X}, S^2)^T$ and prove that it is complete for $(\\mu, \\sigma^2)$.
2. Prove using Basu's Theorem that the sample mean $\\bar{X} = \\frac{1}{n} \\sum_{i=1}^n X_i$ is statistically independent of the sample variance $S^2 = \\frac{1}{n-1} \\sum_{i=1}^n (X_i - \\bar{X})^2$.
3. Define the sample coefficient of variation:
   $$V = \\frac{S}{\\bar{X}}$$
   Assuming $\\mu > 0$, determine whether $V$ is independent of $\\bar{X}$ or $S^2$, or both.
4. Define the studentized normalized residuals:
   $$Z_i = \\frac{X_i - \\bar{X}}{S}, \\quad i = 1, 2, \\dots, n$$
   Prove rigorously using Basu's Theorem that the residual vector $\\mathbf{Z} = (Z_1, Z_2, \\dots, Z_n)^T$ is statistically independent of the pair $(\\bar{X}, S^2)$. Compute $\\mathbb{E}[Z_i]$ and $\\text{Var}(Z_i)$ directly from this independence property.

### Solution, step 1: Minimal sufficiency and completeness of $(\\bar{X}, S^2)$
The joint likelihood of the sample is:

$$f_n(\\mathbf{x}; \\mu, \\sigma^2) = (2\\pi\\sigma^2)^{-n/2} \\exp\\left( -\\frac{1}{2\\sigma^2} \\sum_{i=1}^n (x_i - \\mu)^2 \\right)$$

Expanding the sum of squares: $\\sum (x_i - \\mu)^2 = \\sum (x_i - \\bar{x})^2 + n(\\bar{x} - \\mu)^2 = (n - 1)s^2 + n(\\bar{x} - \\mu)^2$.
Thus:

$$f_n(\\mathbf{x}; \\mu, \\sigma^2) = (2\\pi\\sigma^2)^{-n/2} \\exp\\left( -\\frac{n\\mu^2}{2\\sigma^2} \\right) \\exp\\left( \\frac{n\\mu}{\\sigma^2} \\bar{x} - \\frac{1}{2\\sigma^2} \\left[ (n-1)s^2 + n\\bar{x}^2 \\right] \\right)$$

This is a two-parameter exponential family with natural parameters:

$$\\eta_1 = \\frac{n\\mu}{\\sigma^2}, \\quad \\eta_2 = -\\frac{1}{2\\sigma^2}$$

and natural sufficient statistics $T_1 = \\bar{X}$, $T_2 = \\sum X_i^2 = (n - 1)S^2 + n\\bar{X}^2$.
The natural parameter space is $\\mathcal{H} = \\mathbb{R} \\times (-\\infty, 0)$, which is an open, non-empty set in $\\mathbb{R}^2$.
By Theorem 3.6, the vector $(T_1, T_2)^T$, or equivalently the one-to-one transformation $(\\bar{X}, S^2)^T$, is a **complete minimal sufficient statistic** for $(\\mu, \\sigma^2)$.

### Solution, step 2: Independence of $\\bar{X}$ and $S^2$ via Basu's Theorem
To apply Basu's Theorem directly, we hold $\\sigma^2 = \\sigma_0^2$ fixed and view the model as a one-parameter family indexed by $\\mu \\in \\mathbb{R}$.
1. For fixed $\\sigma_0^2$, the normal distribution is a one-parameter exponential family with natural parameter $\\eta = \\frac{n\\mu}{\\sigma_0^2} \\in \\mathbb{R}$. The sample mean $\\bar{X}$ is a **complete sufficient statistic** for $\\mu$.
2. Now consider the sample variance:
   $$S^2 = \\frac{1}{n-1} \\sum_{i=1}^n (X_i - \\bar{X})^2$$
   Let $Y_i = X_i - \\mu \\sim \\mathcal{N}(0, \\sigma_0^2)$.
   Notice that $X_i - \\bar{X} = (Y_i + \\mu) - (\\bar{Y} + \\mu) = Y_i - \\bar{Y}$.
   Therefore, $S^2 = \\frac{1}{n-1} \\sum_{i=1}^n (Y_i - \\bar{Y})^2$.
   The distribution of $Y_i$ is $\\mathcal{N}(0, \\sigma_0^2)$, which does not depend on $\\mu$ at all!
   Consequently, the distribution of $S^2$ is completely independent of $\\mu$. Thus, $S^2$ is an **ancillary statistic** for $\\mu$.
3. By **Basu's Theorem**, since $\\bar{X}$ is complete sufficient for $\\mu$ and $S^2$ is ancillary for $\\mu$:
   $$\\bar{X} \\text{ and } S^2 \\text{ are statistically independent!}$$
Because this independence holds for every fixed $\\sigma_0^2 > 0$, $\\bar{X}$ and $S^2$ are independent under every parameter pair $(\\mu, \\sigma^2) \\in \\mathbb{R} \\times (0, \\infty)$.

### Solution, step 3: Sample coefficient of variation
The sample coefficient of variation is $V = S / \\bar{X}$.
Does the distribution of $V$ depend on $\\mu$?
Yes: $\\mathbb{E}[V] \\approx \\frac{\\sigma}{\\mu}$.
Does it depend on $\\sigma$?
Yes: scaling the data $X_i \\to c X_i$ scales both $S \\to c S$ and $\\bar{X} \\to c \\bar{X}$, so $V \\to V$. Thus $V$ is scale-invariant and ancillary for $\\sigma^2$ when $\\mu = 0$, but when $\\mu > 0$, its distribution depends on the population signal-to-noise ratio $\\mu / \\sigma$.
Because $V$ involves both $\\bar{X}$ and $S$, and is not ancillary for either parameter individually when the other is unknown, $V$ is **not** independent of $\\bar{X}$ or $S^2$.

### Solution, step 4: Independence of studentized residuals
Consider the studentized residual vector:

$$\\mathbf{Z} = \\left( \\frac{X_1 - \\bar{X}}{S}, \\frac{X_2 - \\bar{X}}{S}, \\dots, \\frac{X_n - \\bar{X}}{S} \\right)^T$$

Let $Y_i = \\frac{X_i - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)$ be the standard normal variables.
Then:
- $\\bar{X} = \\mu + \\sigma \\bar{Y}$
- $X_i - \\bar{X} = \\sigma (Y_i - \\bar{Y})$
- $S = \\sigma S_Y$, where $S_Y = \\sqrt{\\frac{1}{n-1} \\sum (Y_i - \\bar{Y})^2}$

Substituting these into the formula for $Z_i$:

$$Z_i = \\frac{\\sigma (Y_i - \\bar{Y})}{\\sigma S_Y} = \\frac{Y_i - \\bar{Y}}{S_Y}$$

The parameters $\\mu$ and $\\sigma$ cancel out completely! The distribution of $\\mathbf{Z}$ depends solely on standard normal variables $Y_1, \\dots, Y_n \\sim \\mathcal{N}(0, 1)$, and is completely free of both $\\mu$ and $\\sigma^2$.
Therefore, $\\mathbf{Z}$ is an **ancillary statistic** for the full parameter vector $\\boldsymbol{\\theta} = (\\mu, \\sigma^2)^T$!

Since $\\mathbf{T} = (\\bar{X}, S^2)^T$ is a complete sufficient statistic for $(\\mu, \\sigma^2)$, by **Basu's Theorem**:
$$\\mathbf{Z} \\text{ is statistically independent of } (\\bar{X}, S^2)^T!$$

Now compute $\\mathbb{E}[Z_i]$ and $\\text{Var}(Z_i)$ using this independence:
By symmetry, $\\sum_{i=1}^n Z_i = \\frac{\\sum (X_i - \\bar{X})}{S} = 0$.
Taking expectation:

$$\\sum_{i=1}^n \\mathbb{E}[Z_i] = 0 \\implies n \\mathbb{E}[Z_i] = 0 \\implies \\mathbb{E}[Z_i] = 0$$

For the variance:

$$\\sum_{i=1}^n Z_i^2 = \\sum_{i=1}^n \\frac{(X_i - \\bar{X})^2}{S^2} = \\frac{(n - 1)S^2}{S^2} = n - 1$$

Notice that $\\sum_{i=1}^n Z_i^2 = n - 1$ is a deterministic constant!
Taking expectation:

$$\\sum_{i=1}^n \\mathbb{E}[Z_i^2] = n - 1 \\implies n \\mathbb{E}[Z_i^2] = n - 1 \\implies \\mathbb{E}[Z_i^2] = \\frac{n - 1}{n}$$

Since $\\mathbb{E}[Z_i] = 0$:

$$\\text{Var}(Z_i) = \\mathbb{E}[Z_i^2] - (\\mathbb{E}[Z_i])^2 = \\frac{n - 1}{n}$$

This elegant proof required zero multivariate integration: Basu's Theorem and algebraic symmetry established both the exact independence and the exact finite-sample moments.
"""

(OUT_DIR / "unit-3.md").write_text(u3_text, encoding="utf-8")
print(f"Unit 3 prose count: {prose_count(u3_text)} words")
