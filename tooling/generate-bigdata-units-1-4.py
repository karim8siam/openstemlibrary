#!/usr/bin/env python3
"""
Generate Units 1 to 4 for Big Data Methods for Statistics (Stat H-308).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1 = r"""# Unit 1: The Statistical Geometry of High Dimensions

In classical mathematical statistics, asymptotic theory historically operated in the large-$n$, fixed-$p$ regime: the number of observed experimental units $n$ grows toward infinity while the number of measured covariates or variables $p$ remains small and static ($n \to \infty, p = O(1)$). Under these classical conditions, empirical sample covariance matrices converge almost surely to their population counterparts, ordinary least squares estimators are uniformly minimum variance unbiased (UMVU), and non-parametric estimators converge reliably at polynomial rates.

In modern big data analytics—such as whole-genome sequencing, neuroimaging, digital advertising auctions, and high-frequency sensor arrays—statisticians operate in the high-dimensional regime where $p \gg n$ or $p/n \to \gamma \in (0, \infty)$. In high-dimensional Euclidean space $\mathbb{R}^p$, human geometric intuition fails completely. Space is predominantly empty, pairwise distances between data points concentrate tightly around a single universal value, and independently drawn vectors are almost exactly orthogonal. Understanding this "counter-intuitive geometry" is the prerequisite for designing sound high-dimensional statistical algorithms.

## 1.1 The Curse of Dimensionality and Exponential Volume Collapse

The term **curse of dimensionality** was coined by Richard Bellman in 1957 in the context of dynamic programming and functional approximation. In multivariate statistics, it refers to the exponential volume explosion of Euclidean coordinate spaces as dimension $p$ increases.

### 1. Volume of the Unit Hypercube vs. Hypersphere
Consider a $p$-dimensional hypercube of side length $2R$, centered at the origin:
$$C_p(R) = [-R, R]^p = \{ \mathbf{x} \in \mathbb{R}^p : |x_j| \le R \quad \forall j = 1, \dots, p \}$$
The Lebesgue volume of the hypercube scales exponentially with dimension:
$$\mathrm{Vol}(C_p(R)) = (2R)^p$$

Now consider the inscribed $p$-dimensional hypersphere of radius $R$:
$$S_p(R) = \{ \mathbf{x} \in \mathbb{R}^p : \|\mathbf{x}\|_2 \le R \}$$

*Theorem (Volume of a $p$-Dimensional Hypersphere)*: The volume of a Euclidean ball of radius $R$ in $\mathbb{R}^p$ is:
$$\mathrm{Vol}(S_p(R)) = \frac{\pi^{p/2}}{\Gamma\left(\frac{p}{2} + 1\right)} R^p$$
where $\Gamma(z) = \int_0^\infty t^{z-1} e^{-t}\,dt$ is the Euler Gamma function.

*Proof*: Evaluate the Gaussian integral $\int_{\mathbb{R}^p} e^{-\|\mathbf{x}\|_2^2}\,d\mathbf{x}$ in two distinct coordinate representations.
First, by independence of Cartesian coordinates:
$$\int_{\mathbb{R}^p} e^{-\|\mathbf{x}\|_2^2}\,d\mathbf{x} = \prod_{j=1}^p \int_{-\infty}^\infty e^{-x_j^2}\,dx_j = (\sqrt{\pi})^p = \pi^{p/2}$$
Second, using spherical polar coordinates where $d\mathbf{x} = r^{p-1} dr \, d\Omega_{p-1}$:
$$\int_{\mathbb{R}^p} e^{-\|\mathbf{x}\|_2^2}\,d\mathbf{x} = \int_0^\infty r^{p-1} e^{-r^2} \left[ \int_{\mathbb{S}^{p-1}} d\Omega_{p-1} \right] dr = A_{p-1} \int_0^\infty r^{p-1} e^{-r^2}\,dr$$
where $A_{p-1}$ is the surface area of the unit hypersphere $\mathbb{S}^{p-1}$.
Perform substitution $u = r^2$, so $du = 2r\,dr$:
$$\int_0^\infty r^{p-1} e^{-r^2}\,dr = \frac{1}{2} \int_0^\infty u^{\frac{p}{2} - 1} e^{-u}\,du = \frac{1}{2} \Gamma\left(\frac{p}{2}\right)$$
Equating both expressions:
$$\pi^{p/2} = A_{p-1} \cdot \frac{1}{2} \Gamma\left(\frac{p}{2}\right) \implies A_{p-1} = \frac{2 \pi^{p/2}}{\Gamma(p/2)}$$
Integrating surface area over radius from $0$ to $R$:
$$\mathrm{Vol}(S_p(R)) = \int_0^R A_{p-1} r^{p-1}\,dr = \frac{A_{p-1}}{p} R^p = \frac{2 \pi^{p/2}}{p \, \Gamma(p/2)} R^p = \frac{\pi^{p/2}}{\Gamma(p/2 + 1)} R^p$$
which completes the derivation.

### 2. The Ratio of Hypersphere to Hypercube Volume
Comparing the inscribed ball $S_p(R)$ to its circumscribed hypercube $C_p(R) = [-R, R]^p$:
$$\rho_p = \frac{\mathrm{Vol}(S_p(R))}{\mathrm{Vol}(C_p(R))} = \frac{\pi^{p/2} R^p}{\Gamma(p/2 + 1) (2R)^p} = \frac{(\sqrt{\pi}/2)^p}{\Gamma(p/2 + 1)}$$
By Stirling's approximation $\Gamma(z + 1) \approx \sqrt{2\pi z} (z/e)^z$:
$$\lim_{p \to \infty} \rho_p = \lim_{p \to \infty} \frac{(\sqrt{\pi}/2)^p}{\sqrt{\pi p} \left( \frac{p}{2e} \right)^{p/2}} = 0$$

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Dimension ($p$)</th>
<th>Volume of Unit Ball ($R=1$)</th>
<th>Volume of Bounding Cube ($[-1, 1]^p$)</th>
<th>Volume Ratio ($\rho_p$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>2.0000</td>
<td>2.0000</td>
<td>1.0000 (100.0%)</td>
</tr>
<tr>
<td>2</td>
<td>3.1416 ($\pi$)</td>
<td>4.0000</td>
<td>0.7854 (78.54%)</td>
</tr>
<tr>
<td>3</td>
<td>4.1888 ($\frac{4}{3}\pi$)</td>
<td>8.0000</td>
<td>0.5236 (52.36%)</td>
</tr>
<tr>
<td>5</td>
<td>5.2638</td>
<td>32.0000</td>
<td>0.1645 (16.45%)</td>
</tr>
<tr>
<td>10</td>
<td>2.5502</td>
<td>1024.0000</td>
<td>0.00249 (0.25%)</td>
</tr>
<tr>
<td>20</td>
<td>0.0258</td>
<td>1,048,576.0000</td>
<td>$2.46 \times 10^{-8}$</td>
</tr>
<tr>
<td>50</td>
<td>$1.73 \times 10^{-13}$</td>
<td>$1.13 \times 10^{15}$</td>
<td>$1.53 \times 10^{-28}$</td>
</tr>
</tbody>
</table>
</div>

*Geometric Implication*: In 50 dimensions, the volume of the inscribed ball is essentially zero compared to the hypercube. Almost all the volume of a high-dimensional hypercube is concentrated in its "corners".

## 1.2 Concentration of Measure: The Thin Spherical Shell Phenomenon

Consider a uniform probability distribution over a $p$-dimensional ball of radius $R$: $\mathbf{X} \sim \mathcal{U}(S_p(R))$. 
What fraction of the total probability volume resides within an infinitesimal outer crust of thickness $\epsilon R$, where $\epsilon \in (0, 1)$?

The inner core of radius $(1 - \epsilon) R$ contains volume:
$$\mathrm{Vol}(S_p((1 - \epsilon)R)) = \frac{\pi^{p/2}}{\Gamma(p/2 + 1)} [(1 - \epsilon)R]^p$$
The probability that a uniformly distributed random vector falls inside the thin outer shell of thickness $\epsilon R$ is:

$$P(\|\mathbf{X}\|_2 > (1 - \epsilon)R) = 1 - \frac{\mathrm{Vol}(S_p((1 - \epsilon)R))}{\mathrm{Vol}(S_p(R))} = 1 - (1 - \epsilon)^p$$

Using the inequality $1 - \epsilon \le e^{-\epsilon}$:
$$P(\|\mathbf{X}\|_2 > (1 - \epsilon)R) \ge 1 - e^{-\epsilon p}$$
For any fixed thickness $\epsilon > 0$, as $p \to \infty$:
$$\lim_{p \to \infty} P(\|\mathbf{X}\|_2 > (1 - \epsilon)R) = 1.0$$

*The Spherical Shell Theorem*: In high dimensions, virtually all the volume of a solid Euclidean ball resides in an infinitely thin shell directly adjacent to its surface. A solid ball is geometrically indistinguishable from a hollow soap bubble.

## 1.3 Distance Concentration in High Dimensions

In low dimensions ($p = 2$ or $3$), clustering algorithms (such as $k$-means and hierarchical clustering) and nearest-neighbor search rely on Euclidean distance $\|\mathbf{x}_i - \mathbf{x}_j\|_2$ to distinguish proximate neighbors from distant background points.

In high dimensions, Euclidean distances undergo catastrophic **Distance Concentration**, proved formally by Alexander Hinneburg, Charu Aggarwal, and Daniel Keim (2000).

### Mathematical Derivation of Distance Concentration
Let $\mathbf{X}_1, \dots, \mathbf{X}_n$ be independent and identically distributed random vectors in $\mathbb{R}^p$, where the coordinate components $X_{i, j}$ are independent across $j = 1, \dots, p$ with mean $\mu$, variance $\sigma^2$, and finite fourth moment $\mathbb{E}[X^4] < \infty$.

Consider the squared Euclidean distance between two independent observations $\mathbf{X}_i$ and $\mathbf{X}_k$:
$$D_{ik}^2 = \|\mathbf{X}_i - \mathbf{X}_k\|_2^2 = \sum_{j=1}^p (X_{i, j} - X_{k, j})^2$$
Let $W_j = (X_{i, j} - X_{k, j})^2$. Because coordinates are i.i.d., $W_1, \dots, W_p$ are independent and identically distributed:
$$\mathbb{E}[W_j] = \mathbb{E}[(X_{i, j} - X_{k, j})^2] = \mathrm{Var}(X_{i, j}) + \mathrm{Var}(X_{k, j}) = 2\sigma^2$$
Let $\mathrm{Var}(W_j) = \sigma_W^2 < \infty$.

By the classical Central Limit Theorem, as $p \to \infty$:
$$\frac{D_{ik}^2 - 2 p \sigma^2}{\sqrt{p} \sigma_W} \xrightarrow{d} \mathcal{N}(0, 1)$$
Dividing by $2 p \sigma^2$:
$$\frac{D_{ik}^2}{2 p \sigma^2} = 1 + O_p\left( \frac{1}{\sqrt{p}} \right)$$
Taking the square root via Taylor expansion $\sqrt{1 + z} = 1 + \frac{1}{2}z + O(z^2)$:
$$\frac{D_{ik}}{\sqrt{2 p} \sigma} = 1 + O_p\left( \frac{1}{\sqrt{p}} \right)$$

Let $D_{\min} = \min_{k \ne i} \|\mathbf{X}_i - \mathbf{X}_k\|_2$ be the distance to the nearest neighbor, and let $D_{\max} = \max_{k \ne i} \|\mathbf{X}_i - \mathbf{X}_k\|_2$ be the distance to the furthest neighbor.

*Theorem (Beyer et al. 1999)*: If $\lim_{p \to \infty} \frac{\mathrm{Var}(\|\mathbf{X}\|_2)}{\mathbb{E}[\|\mathbf{X}\|_2]^2} = 0$, then for any fixed sample size $n$:
$$\lim_{p \to \infty} \frac{D_{\max} - D_{\min}}{D_{\min}} = 0 \quad \text{in probability}$$

*Diagnostic Consequence*: In 1,000-dimensional space, the nearest neighbor is essentially at the exact same distance as the furthest neighbor! Any classification or clustering metric based on raw Euclidean distances becomes numerically meaningless without prior dimension reduction.

## 1.4 Near-Orthogonality of Random High-Dimensional Vectors

Consider two independent standard Gaussian vectors $\mathbf{X}, \mathbf{Y} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_p)$ in $\mathbb{R}^p$.
The cosine of the angle $\theta$ between them is defined by their inner product:
$$\cos \theta = \frac{\langle \mathbf{X}, \mathbf{Y} \rangle}{\|\mathbf{X}\|_2 \|\mathbf{Y}\|_2} = \frac{\sum_{j=1}^p X_j Y_j}{\sqrt{\sum_{j=1}^p X_j^2} \sqrt{\sum_{j=1}^p Y_j^2}}$$

### 1. Expectation and Variance of the Inner Product
Each product $Z_j = X_j Y_j$ is the product of two independent standard normals:
$$\mathbb{E}[Z_j] = \mathbb{E}[X_j] \mathbb{E}[Y_j] = 0$$
$$\mathrm{Var}(Z_j) = \mathbb{E}[X_j^2 Y_j^2] - 0 = \mathbb{E}[X_j^2] \mathbb{E}[Y_j^2] = 1 \times 1 = 1$$
Therefore, by the Central Limit Theorem:
$$\sum_{j=1}^p X_j Y_j = \sqrt{p} \, W, \quad W \sim \mathcal{N}(0, 1) + o_p(1)$$
Meanwhile, by the Law of Large Numbers:
$$\frac{1}{p} \|\mathbf{X}\|_2^2 = \frac{1}{p} \sum_{j=1}^p X_j^2 \xrightarrow{p} 1 \implies \|\mathbf{X}\|_2 = \sqrt{p} (1 + o_p(1))$$
$$\|\mathbf{Y}\|_2 = \sqrt{p} (1 + o_p(1))$$

Substituting these asymptotic expansions into the cosine formula:
$$\cos \theta = \frac{\sqrt{p} \, W}{\sqrt{p} \sqrt{p}} = \frac{W}{\sqrt{p}} \sim \mathcal{N}\left( 0, \frac{1}{p} \right)$$
As $p \to \infty$, $\mathrm{Var}(\cos \theta) = 1/p \to 0$. Consequently:
$$\cos \theta \xrightarrow{p} 0 \implies \theta \xrightarrow{p} \frac{\pi}{2} = 90^\circ$$

*The Orthogonality Theorem*: Any two randomly selected vectors in high-dimensional space are almost surely mutually orthogonal. In $p = 10,000$ dimensions, the angle between any pair of independently sampled vectors falls within $[89.5^\circ, 90.5^\circ]$ with probability exceeding $0.9999$.

## 1.5 Breakdown of Non-Parametric Density Estimation

In classical non-parametric statistics, the Rosenblatt-Parzen kernel density estimator evaluates the probability density $f(\mathbf{x})$ by averaging localized kernel weights:
$$\hat{f}_h(\mathbf{x}) = \frac{1}{n h^p} \sum_{i=1}^n K\left( \frac{\mathbf{x} - \mathbf{X}_i}{h} \right)$$
The optimal bandwidth balancing squared bias $O(h^4)$ and estimation variance $O(1 / (n h^p))$ is:
$$h_{\text{opt}} \propto n^{-\frac{1}{p + 4}}$$
The resulting minimal Mean Integrated Squared Error (MISE) scales as:
$$\mathrm{MISE}(\hat{f}) = O\left( n^{-\frac{4}{p + 4}} \right)$$

When $p = 1$, the convergence rate is $O(n^{-4/5}) = O(n^{-0.80})$. 
When $p = 10$, the convergence rate slows to $O(n^{-4/14}) \approx O(n^{-0.286})$.
When $p = 100$, the convergence rate drops to $O(n^{-4/104}) \approx O(n^{-0.0385})$.

To achieve the estimation accuracy that $n = 100$ samples achieve in $1$ dimension, a $10$-dimensional kernel density estimator requires:
$$n_{10} \approx 100^{(10 + 4) / (1 + 4)} = 100^{14/5} = 100^{2.8} \approx 398,000 \text{ observations}$$
In 20 dimensions, it requires over $10^{11}$ observations. In the high-dimensional big data regime, completely unconstrained non-parametric estimation is mathematically impossible. Practitioners must impose structural constraints: sparsity, low-rank manifolds, or additive factorizations.

## 1.6 Worked Problem Examples

### Fully worked question 1: Hypersphere Volume Decay Ratio
A researcher analyzes high-dimensional genomic features in $p = 12$ dimensions, bounded in the unit hypercube $[-1, 1]^{12}$. Compute the exact volume of the inscribed 12-dimensional hypersphere of radius $R = 1$, and determine the exact percentage of the hypercube's volume that lies outside the hypersphere.

### Solution, step 1: State the Volume Formulas
The volume of a $p$-dimensional hypersphere of radius $R$ is:
$$\mathrm{Vol}(S_p(R)) = \frac{\pi^{p/2}}{\Gamma(p/2 + 1)} R^p$$
For $p = 12$ and $R = 1$:
$$\mathrm{Vol}(S_{12}(1)) = \frac{\pi^6}{\Gamma(6 + 1)} = \frac{\pi^6}{\Gamma(7)}$$

### Solution, step 2: Evaluate the Factorial and Numerator
Since $7$ is an integer, $\Gamma(7) = 6! = 720$.
Compute $\pi^6$:
$$\pi \approx 3.14159265 \implies \pi^2 \approx 9.8696044 \implies \pi^6 \approx 961.38919$$
Divide by $720$:
$$\mathrm{Vol}(S_{12}(1)) = \frac{961.38919}{720} \approx 1.33526$$

### Solution, step 3: Compute the Bounding Hypercube Volume and the Outside Fraction
The bounding hypercube is $[-1, 1]^{12}$, with side length $s = 2$.
$$\mathrm{Vol}(C_{12}(1)) = 2^{12} = 4096$$
The volume ratio inside the hypersphere is:
$$\rho_{12} = \frac{\mathrm{Vol}(S_{12}(1))}{\mathrm{Vol}(C_{12}(1))} = \frac{1.33526}{4096} \approx 0.0003260 \quad (0.0326\%)$$
The percentage of volume lying in the outer corners of the hypercube is:
$$1 - \rho_{12} = 1 - 0.0003260 = 0.999674 = \mathbf{99.9674\%}$$
Over $99.96\%$ of the volume resides entirely outside the inscribed sphere in 12 dimensions.

---

### Fully worked question 2: Gaussian Annulus and Empirical Radius
Let $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_p)$ be a standard multivariate normal vector in $p = 100$ dimensions. Derive the expected squared distance $\mathbb{E}[\|\mathbf{X}\|_2^2]$, its standard deviation, and determine the narrow interval $[r_{\text{low}}, r_{\text{high}}]$ containing approximately $95\%$ of all probability mass.

### Solution, step 1: Characterize the Squared Norm Distribution
The squared Euclidean norm is the sum of $p$ squared independent standard normal variates:
$$R^2 = \|\mathbf{X}\|_2^2 = \sum_{j=1}^p X_j^2 \sim \chi_p^2$$
For a chi-square distribution with $p = 100$ degrees of freedom:
$$\mathbb{E}[R^2] = p = 100$$
$$\mathrm{Var}(R^2) = 2p = 200 \implies \mathrm{SD}(R^2) = \sqrt{200} = 10 \sqrt{2} \approx 14.142$$

### Solution, step 2: Apply the Delta Method for the Euclidean Radius $R$
Let $g(y) = \sqrt{y}$. The first derivative evaluated at $\mu = 100$ is:
$$g'(\mu) = \frac{1}{2\sqrt{\mu}} = \frac{1}{2 \times 10} = 0.05$$
By the Delta Method:
$$\mathbb{E}[R] \approx \sqrt{\mathbb{E}[R^2]} = \sqrt{100} = 10.0$$
$$\mathrm{Var}(R) \approx [g'(\mu)]^2 \mathrm{Var}(R^2) = (0.05)^2 \times 200 = 0.0025 \times 200 = 0.50$$
$$\mathrm{SD}(R) \approx \sqrt{0.50} \approx 0.7071$$

### Solution, step 3: Compute the 95% Probability Annulus Interval
By the Central Limit Theorem, $R \approx \mathcal{N}(10.0, 0.7071^2)$.
The $95\%$ confidence bounds are:
$$r_{\text{low}} = 10.0 - 1.96 \times 0.7071 = 10.0 - 1.3859 = \mathbf{8.614}$$
$$r_{\text{high}} = 10.0 + 1.96 \times 0.7071 = 10.0 + 1.3859 = \mathbf{11.386}$$
Although the Gaussian density achieves its maximum at the origin $\mathbf{0}$, the probability of drawing a point near the origin ($\|\mathbf{X}\|_2 \le 5$) is virtually zero ($P < 10^{-12}$). All probability mass is concentrated in a razor-thin spherical shell of radius $10.0 \pm 1.39$.

---

### Fully worked question 3: Angular Spread of Independent Vectors
Two independent feature vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^p$ are sampled from a standard normal distribution in $p = 400$ dimensions. Compute the probability that the angle $\theta$ between them deviates from exact perpendicularity ($90^\circ$) by more than $5^\circ$.

### Solution, step 1: Formulate the Angle Distribution
The cosine of the angle $\theta$ is:
$$\cos \theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$
As established in Section 1.4, for independent Gaussian vectors in dimension $p$:
$$\cos \theta \sim \mathcal{N}\left( 0, \frac{1}{p} \right)$$
For $p = 400$:
$$\sigma_{\cos} = \frac{1}{\sqrt{400}} = \frac{1}{20} = 0.05$$

### Solution, step 2: Convert Angular Deviation to Cosine Threshold
A deviation of more than $5^\circ$ from $90^\circ$ means:
$$|\theta - 90^\circ| > 5^\circ \iff \theta \in [0^\circ, 85^\circ) \cup (95^\circ, 180^\circ]$$
Since $\cos(85^\circ) = \sin(5^\circ)$:
$$\sin(5^\circ) = \sin\left( \frac{5 \pi}{180} \text{ rad} \right) = \sin(0.087266 \text{ rad}) \approx 0.087156$$
Therefore, the condition $|\theta - 90^\circ| > 5^\circ$ is equivalent to:
$$|\cos \theta| > 0.087156$$

### Solution, step 3: Compute the Normal Tail Probability
Standardize the threshold using $\sigma_{\cos} = 0.05$:
$$Z = \frac{|\cos \theta|}{\sigma_{\cos}} = \frac{0.087156}{0.05} = 1.7431$$
The two-tailed standard normal probability is:
$$P(|Z| > 1.7431) = 2 [1 - \Phi(1.7431)]$$
Using standard normal tables: $\Phi(1.7431) \approx 0.95934$.
$$P(|Z| > 1.7431) = 2 \times (1 - 0.95934) = 2 \times 0.04066 = \mathbf{0.0813} \quad (8.13\%)$$
There is only an $8.13\%$ probability that two randomly generated vectors in 400 dimensions will deviate by more than $5^\circ$ from perpendicularity.
"""

(DRAFT_DIR / "unit-1.md").write_text(u1.strip() + "\n", encoding="utf-8")
print("Unit 1 generated.")

# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2 = r"""# Unit 2: Large-Scale Dimension Reduction: Spectral & Manifold Learning

When dealing with massive high-dimensional datasets where $p > 10^4$, fitting models directly on the raw coordinate space is computationally prohibitive and statistically disastrous due to distance concentration and collinearity. Dimension reduction transforms high-dimensional vectors $\mathbf{x} \in \mathbb{R}^p$ into low-dimensional latent representations $\mathbf{z} \in \mathbb{R}^d$ ($d \ll p$) while preserving maximal statistical variance, geometric pairwise distances, or local manifold topology.

## 2.1 High-Dimensional PCA and Breakdown of Classical Consistency

Classical **Principal Component Analysis (PCA)**, formulated by Karl Pearson (1901) and Harold Hotelling (1933), identifies orthogonal projection directions $\mathbf{v}_1, \dots, \mathbf{v}_d \in \mathbb{R}^p$ that maximize sample variance:
$$\mathbf{v}_1 = \arg\max_{\|\mathbf{v}\|_2 = 1} \mathbf{v}^T \mathbf{S} \mathbf{v}$$
where $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$ is the sample covariance matrix (assuming centered data $\sum_{i=1}^n \mathbf{x}_i = \mathbf{0}$). The optimal projection vectors are the eigenvectors of $\mathbf{S}$ corresponding to the largest eigenvalues:
$$\mathbf{S} \mathbf{v}_j = \lambda_j \mathbf{v}_j, \quad \lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p \ge 0$$

### The Inconsistency Breakdown when $p/n \to \gamma > 0$
In the classical regime ($p$ fixed, $n \to \infty$), the Law of Large Numbers guarantees that $\mathbf{S} \xrightarrow{p} \mathbf{\Sigma}$ elementwise. Consequently, the sample eigenvectors $\mathbf{v}_j$ converge almost surely to the true population eigenvectors $\mathbf{u}_j$.

However, in the high-dimensional big data regime where $p$ and $n$ grow simultaneously such that $p/n \to \gamma \in (0, \infty)$, **sample covariance matrices are violently inconsistent**.
Iain Johnstone and Arthur Lu (2009) proved that if the true population covariance is the identity $\mathbf{\Sigma} = \mathbf{I}_p$ (pure isotropic noise), the sample eigenvalues do not concentrate at $1.0$. Instead, they disperse across a broad deterministic spectral distribution.

## 2.2 Random Matrix Theory: The Marchenko-Pastur Distribution

Vladimir Marchenko and Leonid Pastur (1967) established the foundational limit law of high-dimensional random matrix theory.

*Theorem (The Marchenko-Pastur Law)*: Let $\mathbf{X}$ be an $n \times p$ matrix whose entries $X_{ij}$ are independent and identically distributed with mean $0$, variance $\sigma^2$, and finite fourth moment. Let $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$ be the $p \times p$ sample covariance matrix.
As $n, p \to \infty$ with $p/n \to \gamma \in (0, 1]$, the empirical spectral distribution of eigenvalues $F_p(\lambda) = \frac{1}{p} \sum_{j=1}^p \mathbb{I}(\lambda_j(\mathbf{S}) \le \lambda)$ converges weakly almost surely to a continuous probability density $f_{\text{MP}}(\lambda)$:

$$f_{\text{MP}}(\lambda) = \frac{1}{2\pi \sigma^2 \gamma \lambda} \sqrt{(\lambda_+ - \lambda)(\lambda - \lambda_-)} \, \mathbb{I}(\lambda_- \le \lambda \le \lambda_+)$$
where the support boundaries (edges of the Marchenko-Pastur bulk) are:
$$\lambda_- = \sigma^2 (1 - \sqrt{\gamma})^2$$
$$\lambda_+ = \sigma^2 (1 + \sqrt{\gamma})^2$$

When $\gamma > 1$ ($p > n$), the matrix $\mathbf{S}$ has rank at most $n$, meaning $p - n$ eigenvalues are identically zero, producing a point mass of weight $1 - 1/\gamma$ at $\lambda = 0$, while the remaining non-zero eigenvalues follow $f_{\text{MP}}(\lambda)$.

### The BBP Phase Transition in Spiked Covariance Models
Jinho Baik, Gérard Ben Arous, and Sandrine Péché (2005) analyzed the **Spiked Covariance Model**, where the population covariance contains a true signal eigenvalue $\ell_1 > 1$:
$$\mathbf{\Sigma} = \mathrm{diag}(\ell_1, 1, 1, \dots, 1)$$

*Theorem (BBP Phase Transition)*: 
1. **Below Threshold ($\ell_1 \le 1 + \sqrt{\gamma}$)**: The sample principal component eigenvalue $\hat{\lambda}_1$ remains trapped inside the Marchenko-Pastur noise bulk ($\hat{\lambda}_1 \to \lambda_+$), and the sample eigenvector $\hat{\mathbf{v}}_1$ is asymptotically orthogonal to the true signal direction:
$$\lim_{n, p \to \infty} |\langle \hat{\mathbf{v}}_1, \mathbf{u}_1 \rangle|^2 = 0$$
The true signal is completely undetectable!
2. **Above Threshold ($\ell_1 > 1 + \sqrt{\gamma}$)**: The leading sample eigenvalue emerges as an isolated outlier outside the bulk:
$$\hat{\lambda}_1 \xrightarrow{a.s.} \ell_1 \left( 1 + \frac{\gamma}{\ell_1 - 1} \right) > \lambda_+$$
and the sample eigenvector retains non-trivial alignment with the true signal:
$$|\langle \hat{\mathbf{v}}_1, \mathbf{u}_1 \rangle|^2 \xrightarrow{a.s.} \frac{1 - \frac{\gamma}{(\ell_1 - 1)^2}}{1 + \frac{\gamma}{\ell_1 - 1}} > 0$$

## 2.3 Randomized Singular Value Decomposition (Randomized SVD)

When data matrices $\mathbf{X} \in \mathbb{R}^{n \times p}$ are massive ($n, p \ge 10^5$), classical deterministic SVD algorithms (such as Golub-Reinsch bidiagonalization) require $O(n p \min(n, p))$ floating-point operations and random disk I/O, rendering exact SVD computationally impossible.

Nathan Halko, Per-Gunnar Martinsson, and Joel A. Tropp (2011) formulated **Randomized SVD (rSVD)**, which computes a near-optimal rank-$k$ truncated SVD in $O(n p \log k)$ operations using random projections.

### The Two-Stage Halko-Martinsson-Tropp Algorithm
Given matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$, target rank $k$, and oversampling parameter $s$ (typically $s = 5$ or $10$), let $\ell = k + s$:

#### Stage 1: Randomized Subspace Extraction
1. Generate an $n \times \ell$ random Gaussian test matrix $\mathbf{\Omega} \sim \mathcal{N}(0, 1)$.
2. Compute the sample matrix sketch $\mathbf{Y} = \mathbf{A} \mathbf{\Omega} \in \mathbb{R}^{m \times \ell}$.
3. (Optional Power Iteration for Fast Spectral Decay): Set $\mathbf{Y} = (\mathbf{A} \mathbf{A}^T)^q \mathbf{A} \mathbf{\Omega}$ (typically $q = 1$ or $2$) to amplify dominant singular values.
4. Construct an orthonormal basis $\mathbf{Q} \in \mathbb{R}^{m \times \ell}$ for the range of $\mathbf{Y}$ via QR factorization:
$$\mathbf{Y} = \mathbf{Q} \mathbf{R}$$

#### Stage 2: Low-Dimensional Deterministic SVD
5. Project the large matrix $\mathbf{A}$ onto the low-dimensional subspace spanned by $\mathbf{Q}$:
$$\mathbf{B} = \mathbf{Q}^T \mathbf{A} \in \mathbb{R}^{\ell \times n}$$
6. Compute the standard SVD of the small $\ell \times n$ matrix $\mathbf{B}$:
$$\mathbf{B} = \tilde{\mathbf{U}} \mathbf{\Sigma} \mathbf{V}^T$$
7. Reconstruct the left singular vectors of $\mathbf{A}$:
$$\mathbf{U} = \mathbf{Q} \tilde{\mathbf{U}}$$
8. Truncate $\mathbf{U}, \mathbf{\Sigma}, \mathbf{V}$ to the top $k$ components.

*Error Bound*: The expected approximation error satisfies:
$$\mathbb{E}\left[ \|\mathbf{A} - \mathbf{Q} \mathbf{Q}^T \mathbf{A}\|_F \right] \le \left( 1 + \frac{k}{s - 1} \right)^{1/2} \sigma_{k+1}(\mathbf{A})$$
The randomized algorithm matches the theoretical Eckart-Young optimal low-rank error to within a tiny constant factor, while executing in minutes instead of days.

## 2.4 Non-Linear Manifold Learning: t-SNE and UMAP

When high-dimensional data reside on complex, non-linear geometric submanifolds (such as the Swiss roll or single-cell RNA transcriptomic manifolds), linear PCA projections project distant folds of the manifold on top of each other, obscuring cluster structures.

### 1. t-Distributed Stochastic Neighbor Embedding (t-SNE)
Laurens van der Maaten and Geoffrey Hinton (2008) invented **t-SNE** to preserve local neighborhood affinities.

1. **High-Dimensional Gaussian Similarities**: The conditional probability that point $\mathbf{x}_i$ picks $\mathbf{x}_j$ as its neighbor is modeled as Gaussian:
$$p_{j|i} = \frac{\exp(-\|\mathbf{x}_i - \mathbf{x}_j\|_2^2 / 2\sigma_i^2)}{\sum_{k \ne i} \exp(-\|\mathbf{x}_i - \mathbf{x}_k\|_2^2 / 2\sigma_i^2)}, \quad p_{ii} = 0$$
The symmetric joint probability is $p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$.
The local scale $\sigma_i$ is tuned via binary search to match a user-specified **perplexity**:
$$\mathrm{Perp}(P_i) = 2^{H(P_i)} = 2^{-\sum_j p_{j|i} \log_2 p_{j|i}}$$
2. **Low-Dimensional Student-$t$ Similarities**: To overcome the "crowding problem" (moderate distances in high dimensions collapsing onto identical radii in low dimensions), the low-dimensional coordinates $\mathbf{y}_i \in \mathbb{R}^2$ use a heavy-tailed Cauchy / Student-$t$ distribution with 1 degree of freedom:
$$q_{ij} = \frac{(1 + \|\mathbf{y}_i - \mathbf{y}_j\|_2^2)^{-1}}{\sum_{k} \sum_{l \ne k} (1 + \|\mathbf{y}_k - \mathbf{y}_l\|_2^2)^{-1}}, \quad q_{ii} = 0$$
3. **Kullback-Leibler Minimization**: The low-dimensional coordinates are optimized by minimizing:
$$\mathrm{KL}(P \parallel Q) = \sum_{i \ne j} p_{ij} \log\left( \frac{p_{ij}}{q_{ij}} \right)$$
via gradient descent.

## 2.5 Worked Problem Examples

### Fully worked question 1: Marchenko-Pastur Spectral Boundary Calculation
A financial econometrician analyzes daily returns for $p = 500$ stocks over $n = 1000$ trading days ($p/n = 0.5$). Assuming stock returns are standardized independent white noise with variance $\sigma^2 = 1.0$:
1. Calculate the theoretical lower and upper spectral boundaries ($\lambda_-$ and $\lambda_+$) of the sample covariance matrix eigenvalues.
2. Determine whether an observed sample eigenvalue $\hat{\lambda}_1 = 3.20$ represents genuine economic co-movement or random noise.

### Solution, step 1: Identify Parameters and Spectral Formulas
The aspect ratio is:
$$\gamma = \frac{p}{n} = \frac{500}{1000} = 0.5$$
The noise variance is $\sigma^2 = 1.0$.
The Marchenko-Pastur spectral boundaries are:
$$\lambda_- = \sigma^2 (1 - \sqrt{\gamma})^2$$
$$\lambda_+ = \sigma^2 (1 + \sqrt{\gamma})^2$$

### Solution, step 2: Compute Boundary Values
Compute $\sqrt{\gamma} = \sqrt{0.5} \approx 0.707107$.
$$\lambda_- = 1.0 \times (1 - 0.707107)^2 = (0.292893)^2 \approx \mathbf{0.08579}$$
$$\lambda_+ = 1.0 \times (1 + 0.707107)^2 = (1.707107)^2 \approx \mathbf{2.91421}$$
Under the null hypothesis of pure noise, $100\%$ of the 500 sample eigenvalues are asymptotically confined to the interval $[0.0858, 2.9142]$.

### Solution, step 3: Evaluate the Observed Eigenvalue
The observed leading eigenvalue is $\hat{\lambda}_1 = 3.20$.
Since $\hat{\lambda}_1 = 3.20 > \lambda_+ = 2.9142$, the eigenvalue falls strictly outside the Marchenko-Pastur noise bulk.
By the BBP phase transition theorem, this indicates a statistically significant market-wide signal factor (a true non-zero population eigenvalue). The hypothesis of pure uncorrelated noise is rejected at asymptotic significance.

---

### Fully worked question 2: Minimum Signal Threshold for BBP Detection
In a biomedical biomarker study with $p = 2000$ gene transcripts and $n = 500$ patients ($\gamma = 4.0$), what is the minimum population signal eigenvalue $\ell_1$ required for the sample PCA to detect the signal outside the noise bulk?

### Solution, step 1: Formulate the BBP Threshold Criterion
In a spiked covariance model $\mathbf{\Sigma} = \mathrm{diag}(\ell_1, 1, \dots, 1)$ with noise variance $\sigma^2 = 1$, the Baik-Ben Arous-Péché (BBP) phase transition states that the sample eigenvector $\hat{\mathbf{v}}_1$ has non-zero asymptotic alignment with the true signal if and only if:
$$\ell_1 > \ell_{\text{crit}} = 1 + \sqrt{\gamma}$$

### Solution, step 2: Compute the Critical Eigenvalue
Here, $p = 2000$ and $n = 500$:
$$\gamma = \frac{p}{n} = \frac{2000}{500} = 4.0$$
$$\sqrt{\gamma} = \sqrt{4.0} = 2.0$$
The critical threshold is:
$$\ell_{\text{crit}} = 1 + 2.0 = \mathbf{3.0}$$

### Solution, step 3: Interpret the Result
If the true underlying biological signal explains less than 3 times the variance of the background noise ($\ell_1 \le 3.0$), the leading sample eigenvector $\hat{\mathbf{v}}_1$ will be completely orthogonal to the true biological axis ($|\langle \hat{\mathbf{v}}_1, \mathbf{u}_1 \rangle| \to 0$). The signal must exceed $\ell_1 = 3.0$ to overcome high-dimensional noise contamination.

---

### Fully worked question 3: Computational Speedup of Randomized SVD
A genomic data matrix has dimension $m = 100,000$ cells by $n = 20,000$ genes. A bioinformatician requires the top $k = 50$ principal components.
Compare the theoretical arithmetic operation counts of standard full Golub-Reinsch SVD versus Randomized SVD with oversampling $s = 10$ and $q = 1$ power iteration.

### Solution, step 1: Compute Full SVD Operation Count
For an $m \times n$ matrix with $m \ge n$, computing a full truncated SVD using classical bidiagonalization requires:
$$\mathrm{FLOPs}_{\text{full}} \approx 2 m n^2$$
For $m = 100,000$ and $n = 20,000$:
$$\mathrm{FLOPs}_{\text{full}} \approx 2 \times 10^5 \times (2 \times 10^4)^2 = 2 \times 10^5 \times 4 \times 10^8 = \mathbf{8 \times 10^{13} \text{ FLOPs}} \quad (80 \text{ TeraFLOPs})$$

### Solution, step 2: Compute Randomized SVD Operation Count
With target rank $k = 50$ and oversampling $s = 10$, the sketch rank is $\ell = k + s = 60$.
1. Generating $\mathbf{\Omega} \in \mathbb{R}^{n \times \ell}$ and computing $\mathbf{Y} = \mathbf{A} \mathbf{\Omega}$: requires $2 m n \ell$ operations.
$$2 \times 10^5 \times 2 \times 10^4 \times 60 = 2.4 \times 10^{11} \text{ FLOPs}$$
2. Power iteration ($q = 1$): computes $\mathbf{A}^T \mathbf{Y}$ then $\mathbf{A} (\mathbf{A}^T \mathbf{Y})$, requiring $4 m n \ell$ operations:
$$4 \times 10^5 \times 2 \times 10^4 \times 60 = 4.8 \times 10^{11} \text{ FLOPs}$$
3. QR factorization of $\mathbf{Y} \in \mathbb{R}^{m \times \ell}$: requires $2 m \ell^2 = 2 \times 10^5 \times 3600 \approx 7.2 \times 10^8$ operations.
4. Projection $\mathbf{B} = \mathbf{Q}^T \mathbf{A}$: requires $2 m n \ell = 2.4 \times 10^{11}$ operations.
5. SVD of small matrix $\mathbf{B} \in \mathbb{R}^{\ell \times n}$: requires $O(n \ell^2) = 20000 \times 3600 \approx 7.2 \times 10^7$ operations.

Total rSVD operations:
$$\mathrm{FLOPs}_{\text{rSVD}} \approx 2.4 \times 10^{11} + 4.8 \times 10^{11} + 2.4 \times 10^{11} \approx \mathbf{9.6 \times 10^{11} \text{ FLOPs}} \quad (0.96 \text{ TeraFLOPs})$$

### Solution, step 3: Calculate the Speedup Factor
$$\text{Speedup} = \frac{\mathrm{FLOPs}_{\text{full}}}{\mathrm{FLOPs}_{\text{rSVD}}} = \frac{8 \times 10^{13}}{9.6 \times 10^{11}} \approx \mathbf{83.33\times}$$
Randomized SVD reduces computational requirements by more than $83$-fold while capturing $99.9\%$ of the variance of the top 50 components.
"""

(DRAFT_DIR / "unit-2.md").write_text(u2.strip() + "\n", encoding="utf-8")
print("Unit 2 generated.")

# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3 = r"""# Unit 3: Sparse Statistical Learning & Regularization (Lasso, Ridge, Elastic Net)

In linear regression models $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$, where $\mathbf{y} \in \mathbb{R}^n$ is the response vector and $\mathbf{X} \in \mathbb{R}^{n \times p}$ is the design matrix of predictor variables, Ordinary Least Squares (OLS) minimizes the residual sum of squares:
$$\hat{\boldsymbol{\beta}}_{\text{OLS}} = \arg\min_{\boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

When $p > n$ (the high-dimensional regime), the $p \times p$ Gram matrix $\mathbf{X}^T \mathbf{X}$ has rank at most $n < p$. It is strictly singular and non-invertible. There exist infinitely many parameter vectors $\boldsymbol{\beta}$ that interpolate the training data perfectly ($\|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 = 0$), yielding catastrophic overfitting and infinite prediction variance. Regularization introduces mathematical constraints on the parameter vector $\boldsymbol{\beta}$ to guarantee unique, stable, and interpretable solutions.

## 3.1 Ridge Regression ($L_2$ Regularization)

Arthur Hoerl and Robert Kennard (1970) introduced **Ridge Regression**, augmenting the least squares criterion with an $L_2$ penalty on the Euclidean norm of the coefficients:

$$\hat{\boldsymbol{\beta}}_{\text{ridge}} = \arg\min_{\boldsymbol{\beta}} \left\{ \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_2^2 \right\} = \arg\min_{\boldsymbol{\beta}} \left\{ \sum_{i=1}^n \left( y_i - \sum_{j=1}^p X_{ij} \beta_j \right)^2 + \lambda \sum_{j=1}^p \beta_j^2 \right\}$$
where $\lambda \ge 0$ is the regularization tuning parameter.

### 1. Analytical Solution and Singular Value Shrinkage
Differentiating the convex penalized objective with respect to $\boldsymbol{\beta}$ and setting the gradient to zero:
$$-2 \mathbf{X}^T (\mathbf{y} - \mathbf{X} \boldsymbol{\beta}) + 2 \lambda \boldsymbol{\beta} = \mathbf{0} \implies (\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}_p) \boldsymbol{\beta} = \mathbf{X}^T \mathbf{y}$$
Because $\mathbf{X}^T \mathbf{X}$ is positive semi-definite, for any $\lambda > 0$, the matrix $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}_p)$ is strictly positive definite and invertible:
$$\hat{\boldsymbol{\beta}}_{\text{ridge}} = (\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}_p)^{-1} \mathbf{X}^T \mathbf{y}$$

To inspect how Ridge shrinks coefficients, substitute the SVD $\mathbf{X} = \mathbf{U} \mathbf{D} \mathbf{V}^T$ (where $\mathbf{D} = \mathrm{diag}(d_1, \dots, d_p)$):
$$\hat{\boldsymbol{\beta}}_{\text{ridge}} = (\mathbf{V} \mathbf{D}^2 \mathbf{V}^T + \lambda \mathbf{V} \mathbf{I} \mathbf{V}^T)^{-1} \mathbf{V} \mathbf{D} \mathbf{U}^T \mathbf{y} = \mathbf{V} (\mathbf{D}^2 + \lambda \mathbf{I})^{-1} \mathbf{D} \mathbf{U}^T \mathbf{y}$$
The $j$-th component projected onto the right singular vector $\mathbf{v}_j$ is shrunk by factor:
$$\frac{d_j^2}{d_j^2 + \lambda} < 1$$
Directions with large singular values ($d_j^2 \gg \lambda$) are barely shrunk, whereas directions with small singular values ($d_j^2 \ll \lambda$, corresponding to high-variance noise) are shrunk aggressively toward zero.

*Limitation of Ridge*: While Ridge stabilizes inversion, the shrinkage factor $\frac{d_j^2}{d_j^2 + \lambda}$ is strictly non-zero for any finite $\lambda$. All $p$ predictors remain in the model ($\hat{\beta}_j \ne 0$). Ridge regression cannot perform variable selection.

## 3.2 The Lasso ($L_1$ Regularization) and Exact Sparsity

Robert Tibshirani (1996) formulated the **Lasso** (Least Absolute Shrinkage and Selection Operator), replacing the $L_2$ squared penalty with an $L_1$ norm penalty:

$$\hat{\boldsymbol{\beta}}_{\text{lasso}} = \arg\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2n} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_1 \right\} = \arg\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2n} \sum_{i=1}^n (y_i - \mathbf{x}_i^T \boldsymbol{\beta})^2 + \lambda \sum_{j=1}^p |\beta_j| \right\}$$

### 1. Geometric Intuition of Sparsity: Corners of the $L_1$ Ball
The Lagrangian formulation is equivalent to the constrained optimization problem:
$$\min_{\boldsymbol{\beta}} \frac{1}{2n} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 \quad \text{subject to} \quad \sum_{j=1}^p |\beta_j| \le t$$

- The OLS loss contours are elliptical paraboloids centered at the unconstrained OLS estimate $\hat{\boldsymbol{\beta}}_{\text{OLS}}$.
- The Ridge constraint region $\{\boldsymbol{\beta} : \sum \beta_j^2 \le t^2\}$ is a smooth Euclidean hypersphere. The expanding elliptical contour touches the smooth sphere at generic points where all coordinates are non-zero.
- The Lasso constraint region $\{\boldsymbol{\beta} : \sum |\beta_j| \le t\}$ is a cross-polytope (a diamond in 2D, an octahedron in 3D) with sharp corners located precisely on the coordinate axes.
Because the corners stick out, the expanding elliptical loss contours hit a sharp corner with high probability. At a corner on the axis $\beta_1$, all other coordinates $\beta_2 = \dots = \beta_p = 0$ are **identically set to zero**. The Lasso performs simultaneous shrinkage and exact variable selection.

### 2. The Soft-Thresholding Operator in Orthogonal Designs
When the design matrix is orthonormal ($\frac{1}{n} \mathbf{X}^T \mathbf{X} = \mathbf{I}_p$), the Lasso objective decouples into $p$ independent univariate optimization problems.
Let $\hat{\beta}_j^{\text{OLS}} = \frac{1}{n} \mathbf{x}_j^T \mathbf{y}$. The Lasso solution admits a closed-form analytical expression:

$$\hat{\beta}_j^{\text{lasso}} = \mathcal{S}(\hat{\beta}_j^{\text{OLS}}, \lambda) = \mathrm{sign}(\hat{\beta}_j^{\text{OLS}}) \max\left( 0, |\hat{\beta}_j^{\text{OLS}}| - \lambda \right)$$
where $\mathcal{S}(z, \lambda)$ is the **Soft-Thresholding Operator**:
- If $|\hat{\beta}_j^{\text{OLS}}| \le \lambda$, the coefficient is set exactly to $0$.
- If $\hat{\beta}_j^{\text{OLS}} > \lambda$, the coefficient is shrunk by exactly $\lambda$: $\hat{\beta}_j^{\text{OLS}} - \lambda$.
- If $\hat{\beta}_j^{\text{OLS}} < -\lambda$, the coefficient is increased by exactly $\lambda$: $\hat{\beta}_j^{\text{OLS}} + \lambda$.

## 3.3 The Coordinate Descent Algorithm for Lasso

Because the $L_1$ norm $|\beta_j|$ is non-differentiable at $\beta_j = 0$, the Lasso objective cannot be solved via standard gradient descent. Jerome Friedman, Trevor Hastie, and Robert Tibshirani (2007) popularized **Cyclical Coordinate Descent**, which solves large-scale Lasso problems in milliseconds.

Let the objective function be:
$$f(\boldsymbol{\beta}) = \frac{1}{2n} \sum_{i=1}^n \left( y_i - \sum_{k \ne j} X_{ik} \beta_k - X_{ij} \beta_j \right)^2 + \lambda \sum_{k \ne j} |\beta_k| + \lambda |\beta_j|$$
Let $r_i^{(j)} = y_i - \sum_{k \ne j} X_{ik} \beta_k$ be the partial residual for the $j$-th predictor.
Minimizing $f(\boldsymbol{\beta})$ with respect to the single scalar coordinate $\beta_j$ while fixing all other coefficients $\beta_k$ ($k \ne j$):

$$\beta_j \leftarrow \frac{\mathcal{S}\left( \frac{1}{n} \sum_{i=1}^n X_{ij} r_i^{(j)}, \lambda \right)}{\frac{1}{n} \sum_{i=1}^n X_{ij}^2}$$
Assuming standardized features ($\frac{1}{n} \sum_{i=1}^n X_{ij}^2 = 1$):
$$\beta_j \leftarrow \mathcal{S}\left( \frac{1}{n} \mathbf{x}_j^T \mathbf{r}^{(j)}, \lambda \right)$$

The algorithm cycles sequentially through $j = 1, 2, \dots, p$, updating each coordinate until convergence. Because coordinate descent requires only simple vector inner products, it scales efficiently to $p = 100,000$ variables.

## 3.4 The Elastic Net

Hui Zou and Trevor Hastie (2005) identified two critical limitations of the Lasso:
1. When $p > n$, the Lasso selects at most $n$ variables before saturating.
2. If there exists a group of highly correlated variables (such as co-regulated genes), Lasso arbitrarily selects one variable from the group and ignores the rest.

The **Elastic Net** combines $L_1$ and $L_2$ penalties:
$$\hat{\boldsymbol{\beta}}_{\text{enet}} = \arg\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2n} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda \left( \alpha \|\boldsymbol{\beta}\|_1 + \frac{1 - \alpha}{2} \|\boldsymbol{\beta}\|_2^2 \right) \right\}$$
where $\alpha \in [0, 1]$ balances the mixing ratio:
- $\alpha = 1$: pure Lasso.
- $\alpha = 0$: pure Ridge.
- $\alpha \in (0, 1)$: the strictly convex $L_2$ penalty induces the **grouping effect** (correlated variables enter the model together with similar coefficients), while the $L_1$ penalty enforces exact sparsity.

## 3.5 Worked Problem Examples

### Fully worked question 1: Closed-Form Soft-Thresholding
Under an orthonormal design matrix ($\frac{1}{n} \mathbf{X}^T \mathbf{X} = \mathbf{I}_4$), four unconstrained OLS estimates are:
$$\hat{\boldsymbol{\beta}}^{\text{OLS}} = (2.40, -1.80, 0.45, -0.20)^T$$
Determine the exact Lasso estimates $\hat{\boldsymbol{\beta}}^{\text{lasso}}$ for penalty parameter $\lambda = 0.50$ and $\lambda = 1.00$.

### Solution, step 1: State the Soft-Thresholding Formula
For an orthonormal design, the Lasso solution for each coordinate is:
$$\hat{\beta}_j^{\text{lasso}} = \mathrm{sign}(\hat{\beta}_j^{\text{OLS}}) \max(0, |\hat{\beta}_j^{\text{OLS}}| - \lambda)$$

### Solution, step 2: Compute Estimates for $\lambda = 0.50$
Evaluate each coordinate:
1. $j = 1$: $\hat{\beta}_1^{\text{OLS}} = 2.40 > 0.50 \implies \hat{\beta}_1^{\text{lasso}} = 2.40 - 0.50 = \mathbf{1.90}$.
2. $j = 2$: $\hat{\beta}_2^{\text{OLS}} = -1.80$, $|-1.80| = 1.80 > 0.50 \implies \hat{\beta}_2^{\text{lasso}} = -(1.80 - 0.50) = \mathbf{-1.30}$.
3. $j = 3$: $\hat{\beta}_3^{\text{OLS}} = 0.45$, $|0.45| = 0.45 \le 0.50 \implies \hat{\beta}_3^{\text{lasso}} = \mathbf{0.0}$.
4. $j = 4$: $\hat{\beta}_4^{\text{OLS}} = -0.20$, $|-0.20| = 0.20 \le 0.50 \implies \hat{\beta}_4^{\text{lasso}} = \mathbf{0.0}$.
For $\lambda = 0.50$:
$$\hat{\boldsymbol{\beta}}^{\text{lasso}} = (1.90, -1.30, 0, 0)^T$$

### Solution, step 3: Compute Estimates for $\lambda = 1.00$
Evaluate each coordinate:
1. $j = 1$: $2.40 - 1.00 = \mathbf{1.40}$.
2. $j = 2$: $-(1.80 - 1.00) = \mathbf{-0.80}$.
3. $j = 3$: $|0.45| \le 1.00 \implies \mathbf{0.0}$.
4. $j = 4$: $|-0.20| \le 1.00 \implies \mathbf{0.0}$.
For $\lambda = 1.00$:
$$\hat{\boldsymbol{\beta}}^{\text{lasso}} = (1.40, -0.80, 0, 0)^T$$

---

### Fully worked question 2: Ridge Regression Singular Value Shrinkage
A bivariate linear regression model with $n = 100$ observations has design matrix $\mathbf{X}$ whose Gram matrix has singular values $d_1 = 20.0$ and $d_2 = 2.0$.
1. Compute the condition number of $\mathbf{X}^T \mathbf{X}$.
2. Compute the shrinkage factors $\frac{d_j^2}{d_j^2 + \lambda}$ applied to both principal directions under Ridge regularization with $\lambda = 16.0$.
3. Compute the improved condition number of the regularized matrix $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})$.

### Solution, step 1: Compute Original Condition Number
The eigenvalues of $\mathbf{X}^T \mathbf{X}$ are the squared singular values:
$$\lambda_1 = d_1^2 = 20^2 = 400.0$$
$$\lambda_2 = d_2^2 = 2^2 = 4.0$$
The condition number $\kappa$ is:
$$\kappa(\mathbf{X}^T \mathbf{X}) = \frac{\lambda_1}{\lambda_2} = \frac{400.0}{4.0} = \mathbf{100.0}$$

### Solution, step 2: Calculate Ridge Shrinkage Factors
For $\lambda = 16.0$:
- First principal direction ($j = 1$):
$$\text{Shrinkage}_1 = \frac{d_1^2}{d_1^2 + \lambda} = \frac{400}{400 + 16} = \frac{400}{416} \approx \mathbf{0.9615} \quad (3.85\% \text{ shrinkage})$$
- Second principal direction ($j = 2$):
$$\text{Shrinkage}_2 = \frac{d_2^2}{d_2^2 + \lambda} = \frac{4}{4 + 16} = \frac{4}{20} = \mathbf{0.2000} \quad (80.0\% \text{ shrinkage})$$
Ridge shrinks the unstable, noisy second direction by $80\%$, while leaving the dominant signal direction largely unperturbed ($3.85\%$ shrinkage).

### Solution, step 3: Compute Regularized Condition Number
The eigenvalues of $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})$ are:
$$\tilde{\lambda}_1 = 400 + 16 = 416.0$$
$$\tilde{\lambda}_2 = 4 + 16 = 20.0$$
The regularized condition number is:
$$\tilde{\kappa} = \frac{416.0}{20.0} = \mathbf{20.8}$$
Ridge regularization improves matrix conditioning by nearly a factor of 5 (reducing condition number from 100 to 20.8).

---

### Fully worked question 3: Coordinate Descent Step Calculation
In a linear regression model with $n = 5$ observations, feature vector $\mathbf{x}_1 = (1, 1, 1, 1, 1)^T / \sqrt{5}$ (standardized so $\frac{1}{n} \|\mathbf{x}_1\|_2^2 = 1$). The current partial residual vector is $\mathbf{r}^{(1)} = (2.0, -1.0, 3.0, 0.5, 1.5)^T$.
Compute the updated coefficient $\beta_1$ for regularization parameter $\lambda = 0.40$.

### Solution, step 1: Formulate the Coordinate Descent Update
The coordinate update rule is:
$$\beta_1 \leftarrow \mathcal{S}\left( \frac{1}{n} \mathbf{x}_1^T \mathbf{r}^{(1)}, \lambda \right)$$
where $n = 5$ and $\mathbf{x}_1 = \frac{1}{\sqrt{5}} (1, 1, 1, 1, 1)^T$.

### Solution, step 2: Calculate the Inner Product
Compute the sum of partial residuals:
$$\sum_{i=1}^5 r_i^{(1)} = 2.0 - 1.0 + 3.0 + 0.5 + 1.5 = 6.0$$
Compute $\mathbf{x}_1^T \mathbf{r}^{(1)}$:
$$\mathbf{x}_1^T \mathbf{r}^{(1)} = \frac{1}{\sqrt{5}} \sum_{i=1}^5 r_i^{(1)} = \frac{6.0}{\sqrt{5}} \approx \frac{6.0}{2.236068} \approx 2.68328$$
Compute the normalized correlation:
$$\rho_1 = \frac{1}{n} \mathbf{x}_1^T \mathbf{r}^{(1)} = \frac{2.68328}{5} \approx 0.536656$$

### Solution, step 3: Apply the Soft-Thresholding Operator
With $\lambda = 0.40$:
Since $\rho_1 = 0.536656 > 0.40$:
$$\beta_1 \leftarrow \rho_1 - \lambda = 0.536656 - 0.40 = \mathbf{0.1367}$$
The updated coordinate value is $\beta_1 = 0.1367$.
"""

(DRAFT_DIR / "unit-3.md").write_text(u3.strip() + "\n", encoding="utf-8")
print("Unit 3 generated.")

# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4 = r"""# Unit 4: Distributed Computing Foundations: MapReduce, Hadoop & Spark for Statisticians

When datasets expand into the terabyte ($10^{12}$ bytes) and petabyte ($10^{15}$ bytes) scale, they exceed the physical RAM and storage capacity of any single computer workstation. In this regime, statistical data cannot be analyzed using standard single-threaded libraries. Computation must be distributed across clusters of commodity hardware running in parallel.

For statisticians, distributed computing introduces a profound architectural shift: **communication complexity** (the volume of data transferred across the cluster network) often dominates algorithmic running time, rendering classical iterative statistical algorithms hopelessly inefficient unless redesigned to accumulate sufficient statistics in parallel.

## 4.1 Distributed Memory Architectures and the Shared-Nothing Paradigm

High-performance computing historically relied on Symmetric Multiprocessing (SMP) and Non-Uniform Memory Access (NUMA) systems, where multiple CPUs share a common physical address space. However, shared-memory systems are physically limited in scalability (rarely exceeding 128 cores) and are vulnerable to bus lock contention.

Modern big data frameworks operate on the **Shared-Nothing Architecture**:
- The computing cluster consists of $M$ independent compute nodes connected via standard Ethernet switches.
- Each node possesses its own private CPU, private memory (RAM), and local disk storage.
- Nodes share zero physical memory. All coordination occurs via message passing and network data transfer.

## 4.2 The MapReduce Framework for Sufficient Statistics

Jeffrey Dean and Sanjay Ghemawat (2004) at Google formulated the **MapReduce** programming model to abstract distributed data processing, implemented in open-source by Apache Hadoop.

### 1. The Map and Reduce Primitives
MapReduce partitions computation into three strictly choreographed phases:
1. **Map Phase**: Operates on input key-value pairs $(k_1, v_1)$ independently and in parallel across cluster nodes, emitting intermediate key-value pairs:
$$\mathrm{Map}(k_1, v_1) \to \text{list}(k_2, v_2)$$
2. **Shuffle and Sort Phase**: The distributed runtime automatically collects all intermediate values sharing the identical key $k_2$ across all nodes, grouping them into a single list $(k_2, \text{list}(v_2))$ and routing them to the designated reducer node.
3. **Reduce Phase**: Aggregates the values associated with key $k_2$:
$$\mathrm{Reduce}(k_2, \text{list}(v_2)) \to \text{list}(k_3, v_3)$$

### 2. Parallel Evaluation of Sufficient Statistics
Let $\mathbf{x}_1, \dots, \mathbf{x}_N$ be $N$ independent observations distributed across $M$ worker nodes, where $N \gg 10^9$.
A statistic $T(\mathbf{X})$ is defined as **associative and commutative** if it can be decomposed into localized partition evaluations:
$$T(\mathbf{X}) = \bigoplus_{m=1}^M T(\mathbf{X}^{(m)})$$

Examples of MapReduce decompositions in statistics:
1. **Sample Mean**:
   - Mapper: on node $m$, compute local count $n_m = |S_m|$ and local sum $s_m = \sum_{i \in S_m} x_i$. Emit key-value pair `("mean", (n_m, s_m))`.
   - Reducer: sum local counts $N = \sum n_m$ and local sums $S = \sum s_m$. Emit $\bar{x} = S / N$.
   Network transfer is $O(M)$ floating-point numbers instead of $O(N)$ data records.
2. **Gram Matrix $\mathbf{X}^T \mathbf{X}$**:
   - Mapper: on node $m$, compute the local $p \times p$ matrix $\mathbf{G}_m = \mathbf{X}^{(m)T} \mathbf{X}^{(m)}$. Emit `("gram", G_m)`.
   - Reducer: sum $\mathbf{X}^T \mathbf{X} = \sum_{m=1}^M \mathbf{G}_m$.
   Once the $p \times p$ Gram matrix and $p \times 1$ vector $\mathbf{X}^T \mathbf{y}$ are aggregated, the master node solves the normal equations $(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ in $O(p^3)$ time without ever storing the full dataset in memory.

## 4.3 Apache Spark: Resilient Distributed Datasets (RDDs) and MLlib

While Hadoop MapReduce revolutionized batch data processing, it suffered from a fatal performance flaw in statistical applications: MapReduce writes all intermediate outputs to physical disks at the end of every Map and Reduce cycle. Iterative algorithms—such as Gradient Descent, Expectation-Maximization (EM), and MCMC—require dozens of sequential iterations, incurring catastrophic disk I/O bottlenecks.

Matei Zaharia et al. (2010) created **Apache Spark** to enable high-speed in-memory distributed data analysis.

### 1. Resilient Distributed Datasets (RDDs)
An RDD is an immutable, lazily evaluated, fault-tolerant distributed collection of data records partitioned across cluster worker nodes.
RDDs are governed by two distinct operations:
- **Transformations** (Lazy): Construct a new RDD from an existing RDD (e.g., `map`, `filter`, `flatMap`, `groupByKey`). Transformations do not execute immediately; Spark constructs a Directed Acyclic Graph (DAG) representing the **Lineage Graph**.
- **Actions** (Eager): Trigger cluster execution and return a result to the driver program or write to storage (e.g., `count`, `collect`, `reduce`, `take`).
- **Fault Tolerance via Lineage**: If a cluster worker node crashes mid-computation, Spark does not restore from periodic disk checkpoints. Instead, it recomputes only the lost partition by replaying the mathematical transformations along the RDD lineage graph.

### 2. In-Memory Caching for Iterative Machine Learning
By invoking `rdd.cache()` or `rdd.persist(StorageLevel.MEMORY_ONLY)`, the dataset partitions are pinned directly inside worker node RAM.
In subsequent iterations of an optimization algorithm:
$$\boldsymbol{\beta}_{t+1} = \boldsymbol{\beta}_t - \alpha_t \sum_{m=1}^M \nabla f_m(\boldsymbol{\beta}_t)$$
the gradient evaluation streams through cached RAM at memory-bus speeds (tens of gigabytes per second), executing machine learning loops **100 times faster** than disk-backed Hadoop.

## 4.4 Communication Complexity vs. Computational Complexity

In distributed statistical learning, computational complexity $T_{\text{comp}}$ measures the total floating-point operations executed across all processors, while **communication complexity** $T_{\text{comm}}$ measures the total volume of network bits transmitted and the latency of network synchronization barriers.

Let $P$ be the number of worker nodes, $N$ the total sample size, and $p$ the parameter dimension:
- **Local Gradient Evaluation**: $O(N p / P)$ computational operations per node.
- **AllReduce Parameter Broadcast**: Transmitting a $p$-dimensional parameter vector to all $P$ workers requires $O(p \log P)$ communication volume.
- If $p$ is massive ($p = 10^7$) or network bandwidth is congested, worker nodes spend $90\%$ of their time waiting for network packet synchronization (**communication-bound execution**).

To minimize communication overhead, statisticians deploy:
1. **Local SGD / Federated Averaging**: Workers execute $K$ local gradient steps independently before synchronizing parameter averages across the network.
2. **Gradient Compression and Quantization**: Transmitting 1-bit or 8-bit quantized gradients (e.g., SignSGD) instead of 64-bit double-precision floats.

## 4.5 Worked Problem Examples

### Fully worked question 1: MapReduce Decomposition of Sample Variance
Show how sample variance $S^2 = \frac{1}{N - 1} \sum_{i=1}^N (x_i - \bar{x})^2$ can be computed across $M$ distributed worker nodes in a single MapReduce pass, avoiding two-pass mean-centering.

### Solution, step 1: Decompose the Variance Formula into Additive Sufficient Statistics
Expand the numerator of the sample variance:
$$\sum_{i=1}^N (x_i - \bar{x})^2 = \sum_{i=1}^N \left( x_i^2 - 2 x_i \bar{x} + \bar{x}^2 \right) = \sum_{i=1}^N x_i^2 - 2 \bar{x} \sum_{i=1}^N x_i + N \bar{x}^2$$
Since $\sum_{i=1}^N x_i = N \bar{x}$:
$$\sum_{i=1}^N (x_i - \bar{x})^2 = \sum_{i=1}^N x_i^2 - N \bar{x}^2 = \sum_{i=1}^N x_i^2 - \frac{1}{N} \left( \sum_{i=1}^N x_i \right)^2$$
The entire sample variance is completely determined by three additive scalar sufficient statistics:
1. $N = \sum_{i=1}^N 1$ (sample count).
2. $S_1 = \sum_{i=1}^N x_i$ (first raw sum).
3. $S_2 = \sum_{i=1}^N x_i^2$ (sum of squares).

### Solution, step 2: Define the Mapper and Reducer Functions
- **Mapper Execution on Node $m$**:
Partition $m$ contains local data subset $D_m$. The mapper iterates over $D_m$ locally and computes:
$$n_m = |D_m|, \quad s_{1, m} = \sum_{x \in D_m} x, \quad s_{2, m} = \sum_{x \in D_m} x^2$$
Emit intermediate key-value pair:
$$\mathrm{Emit}(\text{"stats"}, (n_m, s_{1, m}, s_{2, m}))$$

- **Reducer Execution on Aggregator Node**:
The reducer receives list of triples from all $M$ worker nodes. It accumulates:
$$N = \sum_{m=1}^M n_m, \quad S_1 = \sum_{m=1}^M s_{1, m}, \quad S_2 = \sum_{m=1}^M s_{2, m}$$

### Solution, step 3: Evaluate Final Estimators
The reducer computes the sample mean and unbiased sample variance:
$$\bar{x} = \frac{S_1}{N}$$
$$S^2 = \frac{1}{N - 1} \left( S_2 - \frac{S_1^2}{N} \right)$$
This executes in a single pass over the dataset with exact $O(M)$ communication complexity.

---

### Fully worked question 2: Communication Volume in Distributed OLS
A dataset containing $N = 10^9$ observations and $p = 500$ covariates is distributed across $P = 100$ cluster worker nodes.
1. Compute the network communication volume required if worker nodes transmit raw data to the master node.
2. Compute the network communication volume required using MapReduce parallel Gram matrix aggregation. Assume 8 bytes per double-precision floating-point number.

### Solution, step 1: Compute Raw Data Transfer Volume
Each observation consists of $p$ features plus 1 response variable ($501$ doubles):
$$\text{Bytes per observation} = 501 \times 8 = 4008 \text{ bytes}$$
Total data volume across $10^9$ rows:
$$\text{Volume}_{\text{raw}} = 10^9 \times 4008 \text{ bytes} \approx 4.008 \times 10^{12} \text{ bytes} \approx \mathbf{4.008 \text{ Terabytes}}$$
Transmitting 4 Terabytes over standard gigabit network interfaces would saturate the network for hours.

### Solution, step 2: Compute Gram Matrix Aggregation Volume
Under the MapReduce approach, each worker node $m$ computes its local $p \times p$ Gram matrix $\mathbf{G}_m = \mathbf{X}_m^T \mathbf{X}_m$ and local vector $\mathbf{h}_m = \mathbf{X}_m^T \mathbf{y}_m$.
Due to symmetry, the upper triangle of $\mathbf{G}_m$ contains $\frac{p(p+1)}{2}$ values, plus $p$ values for $\mathbf{h}_m$:
$$\text{Values per node} = \frac{500 \times 501}{2} + 500 = 125,250 + 500 = 125,750 \text{ floats}$$
$$\text{Bytes per node} = 125,750 \times 8 = 1,006,000 \text{ bytes} \approx 1.006 \text{ MB}$$
For $P = 100$ worker nodes, the total communication volume is:
$$\text{Volume}_{\text{MapReduce}} = 100 \times 1.006 \text{ MB} = \mathbf{100.6 \text{ Megabytes}}$$

### Solution, step 3: Calculate the Communication Reduction Ratio
$$\text{Reduction Factor} = \frac{4.008 \times 10^{12} \text{ bytes}}{1.006 \times 10^8 \text{ bytes}} \approx \mathbf{39,840\times}$$
MapReduce reduces network communication traffic by nearly a factor of $40,000$, enabling distributed regression in seconds.

---

### Fully worked question 3: In-Memory Spark Speedup vs. Disk-Backed Hadoop
A distributed logistic regression model requires $T = 30$ gradient descent iterations on a 500 GB dataset across a 10-node cluster.
- In Hadoop MapReduce, reading/writing intermediate state to distributed disk storage takes 140 seconds per iteration.
- In Apache Spark with RDD memory caching, reading from RAM takes 2.2 seconds per iteration. Computing gradients takes 5.0 seconds per iteration in both engines.
Calculate the total execution time for both systems and determine the Spark speedup factor.

### Solution, step 1: Compute Hadoop Execution Time
In Hadoop MapReduce, each iteration requires disk I/O plus gradient computation:
$$\text{Time per iteration}_{\text{Hadoop}} = 140 + 5.0 = 145.0 \text{ seconds}$$
Total execution time for $T = 30$ iterations:
$$\text{Total Time}_{\text{Hadoop}} = 30 \times 145.0 = \mathbf{4350 \text{ seconds}} \quad (72.5 \text{ minutes})$$

### Solution, step 2: Compute Spark In-Memory Execution Time
The initial iteration loads the dataset into memory (taking 140 s disk load + 5 s computation = 145 s).
The remaining 29 iterations read directly from RAM:
$$\text{Time per subsequent iteration}_{\text{Spark}} = 2.2 + 5.0 = 7.2 \text{ seconds}$$
Total execution time:
$$\text{Total Time}_{\text{Spark}} = 145.0 + 29 \times 7.2 = 145.0 + 208.8 = \mathbf{353.8 \text{ seconds}} \quad (5.897 \text{ minutes})$$

### Solution, step 3: Determine the Speedup Factor
$$\text{Speedup} = \frac{4350 \text{ s}}{353.8 \text{ s}} \approx \mathbf{12.3\times}$$
Spark completes the distributed model fitting $12.3$ times faster by eliminating disk serialization bottlenecks.
"""

(DRAFT_DIR / "unit-4.md").write_text(u4.strip() + "\n", encoding="utf-8")
print("Unit 4 generated.")
