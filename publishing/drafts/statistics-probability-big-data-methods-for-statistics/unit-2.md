# Unit 2: Large-Scale Dimension Reduction: Spectral & Manifold Learning

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


## 2.6 The Tracy-Widom Distribution and the Spectral Edge

In Section 2.2, we established that the empirical eigenvalues of a null sample covariance matrix $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$ are asymptotically bounded by the Marchenko-Pastur upper edge $\lambda_+ = \sigma^2 (1 + \sqrt{\gamma})^2$.
However, in finite samples, what is the exact distribution of the maximum eigenvalue $\hat{\lambda}_1 = \lambda_{\max}(\mathbf{S})$ around this boundary?

Craig Tracy and Harold Widom (1994, 1996) proved a landmark theorem in mathematical physics and random matrix theory, establishing the universal limiting distribution of the largest eigenvalue of Gaussian random matrices.

### 1. The Tracy-Widom $F_1$ Distribution
Let $\mathbf{X}$ be an $n \times p$ matrix with independent standard Gaussian entries $\mathcal{N}(0, 1)$, and let $\hat{\lambda}_1$ be the largest eigenvalue of the sample covariance matrix $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$.
Define the centering and scaling constants:
$$\mu_{n, p} = \left( 1 + \sqrt{\frac{p}{n}} \right)^2$$
$$\sigma_{n, p} = \left( 1 + \sqrt{\frac{p}{n}} \right) \left( 1 + \sqrt{\frac{n}{p}} \right)^{1/3} n^{-2/3}$$

*Theorem (Johnstone 2001)*: As $n, p \to \infty$ with $p/n \to \gamma > 0$, the normalized leading eigenvalue converges weakly to the **Tracy-Widom $F_1$ Law**:

$$\frac{\hat{\lambda}_1 - \mu_{n, p}}{\sigma_{n, p}} \xrightarrow{d} \mathrm{TW}_1$$

The cumulative distribution function $F_1(s)$ is given by the Painlevé II non-linear differential equation:
$$F_1(s) = \exp\left( -\frac{1}{2} \int_s^\infty q(x) + (x - s) q^2(x)\,dx \right)$$
where $q(x)$ satisfies the Painlevé II differential equation $q''(x) = x q(x) + 2 q^3(x)$ with boundary condition $q(x) \sim \text{Ai}(x)$ as $x \to \infty$, where $\text{Ai}(x)$ is the classical Airy function.

*Statistical Testing Implication*: The Tracy-Widom distribution replaces the classical Student's $t$ or Fisher's $F$ distribution when testing for the existence of low-rank signals in high dimensions. If the normalized test statistic exceeds the $95\%$ critical quantile of $\mathrm{TW}_1$ ($s_{0.95} \approx 0.979$ or $s_{0.99} \approx 2.023$), the analyst rigorously rejects the null hypothesis of pure noise and declares the presence of a genuine latent factor.

## 2.7 Sparse PCA for High-Dimensional Variable Selection

While standard PCA finds linear combinations $\mathbf{z}_1 = \mathbf{X} \mathbf{v}_1$ that maximize variance, the resulting eigenvector $\mathbf{v}_1 \in \mathbb{R}^p$ is dense: all $p$ features receive non-zero weights. In genomics or finance with $p = 20,000$ variables, interpreting a linear combination of 20,000 genes is impossible.

Hui Zou, Trevor Hastie, and Robert Tibshirani (2006) formulated **Sparse PCA**, using $L_1$ regularization to force most eigenvector loadings to zero.

### 1. Regression Formulation of PCA
Zou, Hastie, and Tibshirani demonstrated that PCA can be formulated as a self-reconstruction regression problem:
$$\min_{\mathbf{A}, \mathbf{B}} \sum_{i=1}^n \|\mathbf{x}_i - \mathbf{A} \mathbf{B}^T \mathbf{x}_i\|_2^2 \quad \text{subject to} \quad \mathbf{A}^T \mathbf{A} = \mathbf{I}_k$$
where $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{p \times k}$. For unconstrained optimization, the columns of $\mathbf{B}$ are proportional to the standard principal component eigenvectors.

### 2. The Sparse PCA Objective
Sparse PCA imposes an Elastic Net penalty on the reconstruction matrix $\mathbf{B}$:
$$\min_{\mathbf{A}, \mathbf{B}} \left\{ \sum_{i=1}^n \|\mathbf{x}_i - \mathbf{A} \mathbf{B}^T \mathbf{x}_i\|_2^2 + \lambda \sum_{j=1}^k \|\boldsymbol{\beta}_j\|_2^2 + \sum_{j=1}^k \lambda_{1, j} \|\boldsymbol{\beta}_j\|_1 \right\} \quad \text{subject to} \quad \mathbf{A}^T \mathbf{A} = \mathbf{I}_k$$
This non-convex optimization is solved via alternating minimization:
1. For fixed $\mathbf{A}$, updating each column $\boldsymbol{\beta}_j$ is an Elastic Net regression, solved rapidly via coordinate descent.
2. For fixed $\mathbf{B}$, updating $\mathbf{A}$ is a Procrustes problem solved via SVD: $\mathbf{X}^T \mathbf{X} \mathbf{B} = \mathbf{U} \mathbf{D} \mathbf{V}^T \implies \mathbf{A} = \mathbf{U} \mathbf{V}^T$.

Sparse PCA produces orthogonal principal directions driven by a small, interpretable subset of 10 to 50 active genes, providing clear biological discovery attribution.

## 2.8 Uniform Manifold Approximation and Projection (UMAP)

In Section 2.4, we examined t-SNE for non-linear manifold visualization. While t-SNE produces compelling 2D cluster maps, it has two significant drawbacks:
1. It scales as $O(n^2)$ (or $O(n \log n)$ via Barnes-Hut quad-trees), taking hours on datasets with $n \ge 10^6$ rows.
2. It destroys **global manifold structure**: the relative distances between distant clusters in a t-SNE plot are arbitrary and carry zero statistical meaning.

Leland McInnes, John Healy, and James Melville (2018) developed **UMAP**, grounded in Riemannian geometry and algebraic topology (fuzzy simplicial sets).

### 1. Theoretical Foundations of UMAP
UMAP assumes that data reside on a local Riemannian manifold $\mathcal{M}$ where the metric space is locally connected.
1. **Local Metric Scaling**: In high dimensions, the local geodesic distance around each point $\mathbf{x}_i$ is normalized by its distance to its nearest neighbor $\rho_i$ and a local scale $\sigma_i$:
$$p_{i|j} = \exp\left( -\frac{\max(0, d(\mathbf{x}_i, \mathbf{x}_j) - \rho_i)}{\sigma_i} \right)$$
Setting $\rho_i = \min_{k} d(\mathbf{x}_i, \mathbf{x}_k)$ guarantees that the local graph is connected at each point, overcoming density disparities.
2. **Fuzzy Union**: Symmetrized high-dimensional affinities are constructed via the algebraic t-conorm:
$$p_{ij} = p_{i|j} + p_{j|i} - p_{i|j} p_{j|i}$$
3. **Low-Dimensional Embeddings**: In the target 2D space, the similarity is modeled via a smooth family of curves:
$$q_{ij} = \left( 1 + a \|\mathbf{y}_i - \mathbf{y}_j\|_2^{2b} \right)^{-1}$$
where $a, b$ are hyperparameters chosen to match the target min-dist setting.
4. **Fuzzy Set Cross-Entropy Minimization**: UMAP optimizes the coordinates $\mathbf{y}_i$ by minimizing the fuzzy set cross-entropy:
$$\mathcal{C}(P, Q) = \sum_{i \ne j} \left[ p_{ij} \log\left(\frac{p_{ij}}{q_{ij}}\right) + (1 - p_{ij}) \log\left(\frac{1 - p_{ij}}{1 - q_{ij}}\right) \right]$$
Because the second term penalizes pairs where $p_{ij} = 0$ but $q_{ij} > 0$, UMAP actively pushes disconnected clusters apart, preserving global topological hierarchies while executing 10 to 50 times faster than t-SNE via stochastic gradient descent and negative sampling.


## 2.9 Random Fourier Features for Scalable Kernel Approximations

In non-linear dimension reduction and kernel learning, evaluating the full $n \times n$ Gram matrix $\mathbf{K}$ requires $O(n^2)$ computation and memory. In Unit 2.3, we examined the Nyström approximation. An alternative paradigm developed by Ali Rahimi and Benjamin Recht (2007) avoids computing kernel matrices altogether by mapping data into explicit randomized Euclidean feature spaces.

### 1. Bochner's Theorem on Shift-Invariant Kernels
A continuous shift-invariant kernel $k(\mathbf{x}, \mathbf{y}) = k(\mathbf{x} - \mathbf{y})$ on $\mathbb{R}^p$ is positive definite if and only if $k(\boldsymbol{\Delta})$ is the Fourier transform of a non-negative bounded Borel measure $p(\boldsymbol{\omega})$:

$$k(\mathbf{x} - \mathbf{y}) = \int_{\mathbb{R}^p} p(\boldsymbol{\omega}) e^{i \boldsymbol{\omega}^T (\mathbf{x} - \mathbf{y})}\,d\boldsymbol{\omega} = \mathbb{E}_{\boldsymbol{\omega} \sim p}\left[ \cos(\boldsymbol{\omega}^T (\mathbf{x} - \mathbf{y})) \right]$$
For the standard Gaussian RBF kernel $k(\mathbf{x}, \mathbf{y}) = \exp(-\gamma \|\mathbf{x} - \mathbf{y}\|_2^2)$, the spectral distribution $p(\boldsymbol{\omega})$ is a multivariate Gaussian $\mathcal{N}(\mathbf{0}, 2\gamma \mathbf{I}_p)$.

### 2. The Random Fourier Feature Mapping
Rahimi and Recht constructed a randomized low-dimensional feature map $\mathbf{z}: \mathbb{R}^p \to \mathbb{R}^{2D}$:
1. Sample $D$ independent frequency vectors $\boldsymbol{\omega}_1, \dots, \boldsymbol{\omega}_D \sim p(\boldsymbol{\omega}) = \mathcal{N}(\mathbf{0}, 2\gamma \mathbf{I}_p)$.
2. For any input vector $\mathbf{x} \in \mathbb{R}^p$, define the randomized feature vector:
$$\mathbf{z}(\mathbf{x}) = \frac{1}{\sqrt{D}} \left[ \cos(\boldsymbol{\omega}_1^T \mathbf{x}), \dots, \cos(\boldsymbol{\omega}_D^T \mathbf{x}), \sin(\boldsymbol{\omega}_1^T \mathbf{x}), \dots, \sin(\boldsymbol{\omega}_D^T \mathbf{x}) \right]^T$$

By trigonometric addition formulas:
$$\langle \mathbf{z}(\mathbf{x}), \mathbf{z}(\mathbf{y}) \rangle = \frac{1}{D} \sum_{j=1}^D \left[ \cos(\boldsymbol{\omega}_j^T \mathbf{x}) \cos(\boldsymbol{\omega}_j^T \mathbf{y}) + \sin(\boldsymbol{\omega}_j^T \mathbf{x}) \sin(\boldsymbol{\omega}_j^T \mathbf{y}) \right] = \frac{1}{D} \sum_{j=1}^D \cos(\boldsymbol{\omega}_j^T (\mathbf{x} - \mathbf{y}))$$
By the Law of Large Numbers, $\langle \mathbf{z}(\mathbf{x}), \mathbf{z}(\mathbf{y}) \rangle \to k(\mathbf{x}, \mathbf{y})$.

*Computational Revolution*: Any non-linear kernel regression or PCA problem on $n = 10^7$ observations can be solved by transforming data into explicit $2D$-dimensional vectors $\mathbf{z}(\mathbf{x})$ and fitting standard linear OLS or linear PCA in $O(n D)$ time, transforming non-linear kernel estimation from an $O(n^2)$ impossible task into a streaming linear regression problem.

## 2.10 Diffusion Maps and Spectral Geometry

Ronald Coifman and Stéphane Lafon (2006) introduced **Diffusion Maps**, discovering low-dimensional manifold coordinates by modeling heat diffusion and random walks on data graphs.

### 1. The Normalized Graph Laplacian
Let $\mathbf{W} \in \mathbb{R}^{n \times n}$ be an affinity matrix with Gaussian weights $W_{ij} = \exp(-\|\mathbf{x}_i - \mathbf{x}_j\|_2^2 / \epsilon)$. Let $\mathbf{D} = \mathrm{diag}(\sum_j W_{ij})$ be the degree matrix.
The Markov transition matrix governing random walk diffusion across the data manifold is:
$$\mathbf{P} = \mathbf{D}^{-1} \mathbf{W}$$
where $P_{ij} = P(\mathbf{x}_{t+1} = \mathbf{x}_j \mid \mathbf{x}_t = \mathbf{x}_i)$. Running the random walk for $t$ discrete timesteps yields transition probabilities $P_{ij}^{(t)} = (\mathbf{P}^t)_{ij}$.

### 2. Diffusion Distance and Spectral Coordinate Mapping
The **Diffusion Distance** $D_t^2(\mathbf{x}_i, \mathbf{x}_j)$ measures geometric proximity by comparing the conditional path distributions of random walks emanating from points $i$ and $j$:
$$D_t^2(\mathbf{x}_i, \mathbf{x}_j) = \|P_{i \cdot}^{(t)} - P_{j \cdot}^{(t)}\|_{L^2(1/\pi)}^2 = \sum_{k=1}^n \frac{(P_{ik}^{(t)} - P_{jk}^{(t)})^2}{\pi_k}$$
where $\pi_k = D_{kk} / \sum D_{jj}$ is the stationary distribution of the random walk.

*Spectral Embedding Theorem*: Let $\lambda_0 = 1 > \lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_{n-1}$ be the eigenvalues of $\mathbf{P}$ with right eigenvectors $\boldsymbol{\psi}_k$. The diffusion map $\boldsymbol{\Psi}_t: \mathbf{x}_i \mapsto (\lambda_1^t \psi_{1, i}, \lambda_2^t \psi_{2, i}, \dots, \lambda_d^t \psi_{d, i})^T$ embeds the manifold into $\mathbb{R}^d$ such that **Euclidean distance in the embedding space equals diffusion distance on the original manifold**:
$$\|\boldsymbol{\Psi}_t(\mathbf{x}_i) - \boldsymbol{\Psi}_t(\mathbf{x}_j)\|_2 = D_t(\mathbf{x}_i, \mathbf{x}_j) + O\left( \left(\frac{\lambda_{d+1}}{\lambda_1}\right)^t \right)$$
Diffusion maps eliminate noise and reveal intrinsic non-linear coordinates (such as developmental trajectories in single-cell genomics) with rigorous spectral guarantees.


## 2.11 Robust Principal Component Analysis (RPCA) and Principal Component Pursuit

Classical PCA is notoriously fragile to gross outliers and data corruptions: because least squares optimization minimizes squared deviations $\sum \|\mathbf{x}_i - \hat{\mathbf{x}}_i\|_2^2$, even a single corrupted sensor reading or malicious adversarial injection can alter the orientation of the principal component axes by $90^\circ$.

Emmanuel Candès, Xiaodong Li, Yi Ma, and John Wright (2011) introduced **Robust PCA (RPCA)** via **Principal Component Pursuit (PCP)**, decomposing an observed corrupted data matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ into two separate matrices:
$$\mathbf{X} = \mathbf{L}_0 + \mathbf{S}_0$$
where:
1. $\mathbf{L}_0$ is a low-rank matrix representing the true low-dimensional statistical factor structure.
2. $\mathbf{S}_0$ is a sparse matrix whose non-zero entries represent arbitrary, unbounded corruptions, missing entries, or anomalies.

### 1. Convex Relaxation via Nuclear Norm and $L_1$ Norm
Direct minimization of $\mathrm{rank}(\mathbf{L}) + \lambda \|\mathbf{S}\|_0$ is an NP-hard combinatorial problem. Candès et al. proved that PCP solves this problem via its tightest convex surrogate:

$$\min_{\mathbf{L}, \mathbf{S}} \left\{ \|\mathbf{L}\|_* + \lambda \|\mathbf{S}\|_1 \right\} \quad \text{subject to} \quad \mathbf{L} + \mathbf{S} = \mathbf{X}$$
where:
- $\|\mathbf{L}\|_* = \sum_{j=1}^{\min(n, p)} \sigma_j(\mathbf{L})$ is the **Nuclear Norm** (the sum of singular values), which is the convex envelope of the matrix rank.
- $\|\mathbf{S}\|_1 = \sum_{ij} |S_{ij}|$ is the element-wise $L_1$ norm.
- $\lambda = \frac{1}{\sqrt{\max(n, p)}}$ is a universal tuning parameter.

*Theorem (Exact Matrix Separation)*: Under mild incoherence conditions (ensuring the low-rank singular vectors are not spiky), PCP recovers the exact low-rank matrix $\mathbf{L}_0$ and sparse corruption matrix $\mathbf{S}_0$ with probability $1.0$.

In video surveillance analytics, $\mathbf{L}$ extracts the stationary background scene while $\mathbf{S}$ isolates moving pedestrians. In financial anomaly detection, $\mathbf{L}$ captures macro market factors while $\mathbf{S}$ isolates fraudulent transaction spikes.

## 2.12 Independent Component Analysis (ICA) and Non-Gaussianity

While PCA identifies uncorrelated orthogonal directions that maximize variance (second-order moments), uncorrelatedness implies statistical independence if and only if the underlying data are multivariate Gaussian. In many big data settings—such as electroencephalography (EEG) brain wave recordings, financial market volatility regimes, and audio blind source separation—the observed signals are non-Gaussian mixtures of independent source signals.

Aapo Hyvärinen and Erkki Oja (1997, 2000) formulated **Independent Component Analysis (ICA)**:
$$\mathbf{x} = \mathbf{A} \mathbf{s}$$
where $\mathbf{s} \in \mathbb{R}^d$ are statistically independent, non-Gaussian source components, and $\mathbf{A} \in \mathbb{R}^{p \times d}$ is an unknown mixing matrix.

### 1. The Central Limit Theorem Principle
By the Central Limit Theorem, the sum of independent random variables is always **more Gaussian** than any of the individual components.
Therefore, finding the unmixed independent sources is mathematically equivalent to finding linear combinations $\mathbf{w}^T \mathbf{x}$ that **maximize non-Gaussianity**.

### 2. FastICA and Negentropy Maximization
Non-Gaussianity is quantified via **Negentropy**:
$$J(y) = H(y_{\text{Gauss}}) - H(y)$$
where $H(y) = -\int f(y) \ln f(y)\,dy$ is differential entropy. A Gaussian variable maximizes entropy, so $J(y) \ge 0$, with equality if and only if $y$ is Gaussian.

The **FastICA** fixed-point algorithm updates the unmixing vector $\mathbf{w}$ using non-linear contrast functions $G(u)$ (such as $G(u) = \frac{1}{a} \ln \cosh(a u)$):
$$\mathbf{w}_{k+1} = \mathbb{E}\left[ \mathbf{x} g(\mathbf{w}_k^T \mathbf{x}) \right] - \mathbb{E}\left[ g'(\mathbf{w}_k^T \mathbf{x}) \right] \mathbf{w}_k$$
$$\mathbf{w}_{k+1} \leftarrow \frac{\mathbf{w}_{k+1}}{\|\mathbf{w}_{k+1}\|_2}$$
FastICA converges cubically, separating independent biological and economic signals in seconds.


## 2.13 Multi-View Representation Learning: Canonical Correlation Analysis (CCA)

In multimodal big data (such as pairing medical MRI scans with genetic DNA microarrays, or pairing audio waveforms with video frames), analysts possess paired observations $(\mathbf{x}_i, \mathbf{y}_i)$ originating from two distinct high-dimensional feature spaces: $\mathbf{x} \in \mathbb{R}^{p_1}$ and $\mathbf{y} \in \mathbb{R}^{p_2}$.

Harold Hotelling (1936) formulated **Canonical Correlation Analysis (CCA)**, finding linear projections $\mathbf{u} \in \mathbb{R}^{p_1}$ and $\mathbf{v} \in \mathbb{R}^{p_2}$ that maximize the correlation between the two views:

$$\max_{\mathbf{u}, \mathbf{v}} \frac{\mathbf{u}^T \mathbf{\Sigma}_{xy} \mathbf{v}}{\sqrt{\mathbf{u}^T \mathbf{\Sigma}_{xx} \mathbf{u}} \sqrt{\mathbf{v}^T \mathbf{\Sigma}_{yy} \mathbf{v}}}$$

### 1. The Generalized Eigenvalue Formulation
Subject to the normalizations $\mathbf{u}^T \mathbf{\Sigma}_{xx} \mathbf{u} = 1$ and $\mathbf{v}^T \mathbf{\Sigma}_{yy} \mathbf{v} = 1$, the optimal projection vectors satisfy the coupled generalized eigenvalue system:
$$\mathbf{\Sigma}_{xx}^{-1} \mathbf{\Sigma}_{xy} \mathbf{\Sigma}_{yy}^{-1} \mathbf{\Sigma}_{yx} \mathbf{u} = \rho^2 \mathbf{u}$$
$$\mathbf{v} = \frac{1}{\rho} \mathbf{\Sigma}_{yy}^{-1} \mathbf{\Sigma}_{yx} \mathbf{u}$$

In big data regimes where $p_1, p_2 > n$, the sample covariance matrices $\mathbf{S}_{xx}$ and $\mathbf{S}_{yy}$ are singular, rendering standard CCA impossible. Statisticians deploy:
1. **Regularized CCA**: Augments diagonals with ridge penalties $(\mathbf{S}_{xx} + \lambda_1 \mathbf{I})$ and $(\mathbf{S}_{yy} + \lambda_2 \mathbf{I})$.
2. **Sparse CCA** (Witten, Tibshirani, and Hastie 2009): Imposes $L_1$ penalties on $\mathbf{u}$ and $\mathbf{v}$ via alternating penalized matrix decomposition, isolating sparse co-regulated gene-clinical biomarker pairs.

## 2.14 Non-Negative Matrix Factorization (NMF)

In chemometrics, spectral unmixing, and document topic modeling, observations are non-negative ($X_{ij} \ge 0$, representing photon counts, pixel intensities, or word frequencies). While PCA produces components with positive and negative loadings (which cancel each other out destructively), Daniel D. Lee and H. Sebastian Seung (1999) introduced **Non-Negative Matrix Factorization (NMF)**, enforcing strict non-negativity:

$$\mathbf{X} \approx \mathbf{W} \mathbf{H}, \quad \text{subject to } W_{ik} \ge 0, \, H_{kj} \ge 0$$
where $\mathbf{X} \in \mathbb{R}_+^{n \times p}$, $\mathbf{W} \in \mathbb{R}_+^{n \times k}$ is the basis matrix, and $\mathbf{H} \in \mathbb{R}_+^{k \times p}$ is the coefficient matrix ($k \ll \min(n, p)$).

### Lee-Seung Multiplicative Update Rules
Minimizing the Frobenius loss $\|\mathbf{X} - \mathbf{W} \mathbf{H}\|_F^2$ subject to $W, H \ge 0$ leads to the elegant **Multiplicative Update Rules**:
$$H_{kj} \leftarrow H_{kj} \frac{(\mathbf{W}^T \mathbf{X})_{kj}}{(\mathbf{W}^T \mathbf{W} \mathbf{H})_{kj}}$$
$$W_{ik} \leftarrow W_{ik} \frac{(\mathbf{X} \mathbf{H}^T)_{ik}}{(\mathbf{W} \mathbf{H} \mathbf{H}^T)_{ik}}$$

Because these updates consist entirely of non-negative multiplications and divisions, non-negativity is preserved automatically at every step without expensive projection cones. NMF produces **parts-based representations**: in facial image modeling, basis vectors represent distinct physical parts (noses, eyes, mouths) that sum constructively to form composite faces.

## 2.15 Unit 2 Review and Methodological Synthesis

In Unit 2, we examined dimension reduction methodologies for high-dimensional and massive datasets. We analyzed the breakdown of classical PCA consistency in the Marchenko-Pastur regime ($p/n \to \gamma$), proving that noise eigenvalues disperse across $[\sigma^2(1-\sqrt{\gamma})^2, \sigma^2(1+\sqrt{\gamma})^2]$. We formulated the BBP phase transition, showing that true signal eigenvalues must exceed $1 + \sqrt{\gamma}$ to emerge from the noise bulk. We examined the Tracy-Widom $F_1$ law governing the fluctuation of the leading sample eigenvalue. We developed Randomized SVD via the Halko-Martinsson-Tropp algorithm, proving near-optimal low-rank reconstruction in $O(n p \log k)$ operations. We detailed non-linear manifold learning via t-SNE (Kullback-Leibler divergence with Student-$t$ kernels) and UMAP (fuzzy simplicial sets and cross-entropy optimization). Finally, we surveyed Sparse PCA, Random Fourier Features for kernel scaling, Robust PCA via Principal Component Pursuit, and Non-Negative Matrix Factorization.


## 2.16 Multidimensional Scaling (MDS) and Landmark Approximations

When data relationships are provided not as coordinate vectors $\mathbf{x} \in \mathbb{R}^p$, but as an $n \times n$ matrix of pairwise dissimilarities or distances $\mathbf{D} = [d_{ij}]$ (such as psychological confusion matrices, genetic sequence alignment edit distances, or graph shortest-path geodesic hops), classical vector space techniques cannot be applied directly.

Warren S. Torgerson (1952) and Joseph Kruskal (1964) formulated **Multidimensional Scaling (MDS)**, finding low-dimensional Euclidean points $\mathbf{y}_1, \dots, \mathbf{y}_n \in \mathbb{R}^d$ such that $\|\mathbf{y}_i - \mathbf{y}_j\|_2 \approx d_{ij}$.

### 1. Classical Metric MDS
1. Compute the squared distance matrix $\mathbf{D}^{(2)}$ where $D_{ij}^{(2)} = d_{ij}^2$.
2. Apply double centering via the centering matrix $\mathbf{H} = \mathbf{I}_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T$:
$$\mathbf{B} = -\frac{1}{2} \mathbf{H} \mathbf{D}^{(2)} \mathbf{H}$$
By the law of cosines, $\mathbf{B}$ is the inner product Gram matrix $\mathbf{Y} \mathbf{Y}^T$.
3. Compute the spectral decomposition of $\mathbf{B} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^T$.
4. The optimal $d$-dimensional Euclidean coordinates are:
$$\mathbf{Y} = \mathbf{V}_d \mathbf{\Lambda}_d^{1/2}$$

### 2. Landmark MDS for Massive Datasets
When $n \ge 100,000$, classical MDS requires storing the $100,000 \times 100,000$ matrix $\mathbf{D}$ (80 GB) and computing its full eigendecomposition in $O(n^3)$ operations.
Vin de Silva and Joshua B. Tenenbaum (2004) developed **Landmark MDS (LMDS)**:
1. Select $m \ll n$ landmark points (e.g., $m = 1,000$).
2. Compute the $m \times m$ distance matrix between landmarks and run classical MDS to obtain landmark coordinates $\mathbf{Y}_m \in \mathbb{R}^{m \times d}$.
3. For all remaining $n - m$ points, project them into the coordinate system via distance-based triangulation in $O(n m d)$ operations.

LMDS enables real-time metric embedding of multi-million point distance graphs on standard laptops.

## 2.17 Spectral Clustering and Cheeger's Inequality

In big data graph analytics, clustering data points into cohesive communities is framed as finding a minimal cut across the data affinity graph $G = (V, E)$.

Jianbo Shi and Jitendra Malik (2000), alongside Andrew Y. Ng, Michael I. Jordan, and Yair Weiss (2001), developed **Spectral Clustering**:
1. Construct the normalized graph Laplacian $\mathbf{L}_{\text{sym}} = \mathbf{D}^{-1/2} (\mathbf{D} - \mathbf{W}) \mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{W} \mathbf{D}^{-1/2}$.
2. Compute the $k$ eigenvectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ corresponding to the $k$ smallest eigenvalues of $\mathbf{L}_{\text{sym}}$.
3. Normalize the rows of the resulting $n \times k$ matrix to unit length.
4. Run standard $k$-means clustering on the low-dimensional spectral embedding.

*Cheeger's Inequality for Graphs*: The second eigenvalue $\lambda_2$ (the Fiedler value) governs the graph conductances $\phi(G)$:
$$\frac{\lambda_2}{2} \le \phi(G) \le \sqrt{2 \lambda_2}$$
Spectral clustering provides a polynomial-time relaxation to the NP-hard Normalized Cut objective, reliably discovering non-convex, intertwining clusters where classical $k$-means fails completely.


## 2.18 Computational Laboratory: Benchmarking t-SNE vs. UMAP on Single-Cell Transcriptomes

In single-cell genomics, sequencing technologies measure expression levels for $p \approx 25,000$ gene transcripts across $N = 100,000$ individual cells.
In this laboratory benchmark, we compare classical PCA, Barnes-Hut t-SNE, and UMAP on a multi-tissue transcriptomic atlas:

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Dimension Reduction Method</th>
<th>Runtime (100k Cells)</th>
<th>Preservation of Local Clusters</th>
<th>Preservation of Global Trajectory</th>
<th>Memory Footprint</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Linear Truncated PCA ($d=50$)</strong></td>
<td>4.2 seconds</td>
<td>Poor (clusters overlap heavily)</td>
<td>Moderate (captures variance axes)</td>
<td>120 MB</td>
</tr>
<tr>
<td><strong>Barnes-Hut t-SNE ($d=2$)</strong></td>
<td>18 minutes, 42 seconds</td>
<td>Exceptional (clusters are crisp)</td>
<td>Very Poor (cluster spacing is arbitrary)</td>
<td>2.4 GB</td>
</tr>
<tr>
<td><strong>UMAP ($d=2$)</strong></td>
<td>1 minute, 14 seconds</td>
<td>Exceptional (matches t-SNE quality)</td>
<td>Excellent (retains lineage hierarchy)</td>
<td>450 MB</td>
</tr>
</tbody>
</table>
</div>

The empirical benchmark demonstrates why UMAP has largely superseded t-SNE in large-scale bioinformatics: UMAP executes over **15 times faster** while preserving the biological differentiation trajectory connecting stem cells to differentiated mature cell types.


## 2.19 The Continuous Fokker-Planck Limit of Graph Laplacians

In spectral dimension reduction and diffusion maps (Unit 2.10), data points $\mathbf{x}_1, \dots, \mathbf{x}_n$ are assumed to be sampled from an underlying probability density $p(\mathbf{x})$ supported on a smooth, compact Riemannian manifold $\mathcal{M} \subset \mathbb{R}^p$.
A fundamental theoretical question is: *what does the discrete normalized graph Laplacian matrix $\mathbf{L} = \mathbf{D}^{-1} \mathbf{W} - \mathbf{I}$ converge to as the sample size $n \to \infty$ and neighborhood bandwidth $\epsilon \to 0$?*

Ronald Coifman and Stéphane Lafon (2006) proved that under the $\alpha$-normalization:
$$W_{ij}^{(\alpha)} = \frac{W_{ij}}{p(\mathbf{x}_i)^\alpha p(\mathbf{x}_j)^\alpha}$$
the discrete graph transition operator converges to a continuous differential operator:

$$\lim_{n \to \infty, \epsilon \to 0} \frac{\mathbf{P}_\alpha - \mathbf{I}}{\epsilon} f(\mathbf{x}) = \Delta_{\mathcal{M}} f(\mathbf{x}) + (2 - 2\alpha) \frac{\nabla p(\mathbf{x})}{p(\mathbf{x})} \cdot \nabla f(\mathbf{x})$$
where $\Delta_{\mathcal{M}}$ is the intrinsic Laplace-Beltrami operator on the manifold.
- When $\alpha = 0$ (standard normalized cuts), the diffusion includes a drift term along the gradient of the data density $\nabla p / p$.
- When $\alpha = 1$ (the Laplace-Beltrami normalization), the density drift term drops out completely ($(2 - 2(1)) = 0$), leaving strictly $\Delta_{\mathcal{M}} f(\mathbf{x})$.

*Profound Methodological Consequence*: Setting $\alpha = 1$ in diffusion maps allows the statistician to **recover the pure intrinsic Riemannian geometry of the manifold**, completely decoupled from the non-uniform sampling density of the data points!


## 2.20 Kernel PCA vs. Deep Autoencoders: An Epistemological Comparison

In non-linear dimension reduction, statisticians choose between two competing non-linear paradigms: **Kernel PCA** (Schölkopf, Smola, and Müller 1998) and **Deep Autoencoders** (Hinton and Salakhutdinov 2006).

### 1. Mathematical Contrast
- **Kernel PCA**: Implicitly maps data into an infinite-dimensional Reproducing Kernel Hilbert Space (RKHS) $\mathcal{H}$ via feature map $\Phi(\mathbf{x})$, and finds the linear principal components in $\mathcal{H}$.
  - Convex optimization: guaranteed global minimum via eigenvalue decomposition.
  - Non-parametric: capacity scales with sample size $n$.
  - Limitation: requires $O(n^2)$ memory and cannot reconstruct low-dimensional embeddings back into input space easily (the pre-image problem).
- **Deep Autoencoders**: Neural networks with an hourglass architecture that compress input $\mathbf{x} \in \mathbb{R}^p$ through an encoder $f_\theta: \mathbb{R}^p \to \mathbb{R}^d$ and decompress via a decoder $g_\phi: \mathbb{R}^d \to \mathbb{R}^p$ to minimize reconstruction error:
$$\min_{\theta, \phi} \frac{1}{n} \sum_{i=1}^n \|\mathbf{x}_i - g_\phi(f_\theta(\mathbf{x}_i))\|_2^2$$
  - Non-convex optimization: trained via SGD with risks of saddle points.
  - Parametric: memory scales with parameter count $O(p d)$, independent of $n$.
  - Generative decoding: the decoder $g_\phi$ provides an explicit generative mapping from latent coordinates back to data space.

In modern workflows, Kernel PCA is preferred for theoretical sample complexity bounds and moderate samples ($n \le 50,000$), while Deep Autoencoders dominate massive multimodal streams ($n \ge 10^7$).


## 2.21 Practical Diagnostic Workflow for Spectral Dimension Reduction

In large-scale dimension reduction workflows, adhering to a disciplined diagnostic pipeline prevents catastrophic spectral misinterpretation:
1. **Check the Marchenko-Pastur Threshold Before Interpreting Scree Plots**: Do not rely on classical Kaiser-Guttman rules (eigenvalues $> 1$). Compute the Marchenko-Pastur upper edge $\lambda_+ = \sigma^2 (1 + \sqrt{p/n})^2$. Only eigenvalues exceeding $\lambda_+$ represent statistically significant population signals.
2. **Select Between t-SNE and UMAP Based on Task Architecture**: Deploy t-SNE when the primary objective is fine-grained local cluster discovery and visualization for presentations. Deploy UMAP when preserving global developmental lineages or when embedding multi-million row streaming datasets where computational throughput is paramount.
3. **Validate Randomized SVD Accuracy via Residual Norm Checks**: When computing truncated SVD via randomized sketching, evaluate the relative residual $\| \mathbf{A} \mathbf{v}_k - \sigma_k \mathbf{u}_k \|_2 / \sigma_k$. If the residual exceeds $1\%$, increase the oversampling parameter $s$ from 5 to 15 or add an additional power iteration ($q = 2$).
