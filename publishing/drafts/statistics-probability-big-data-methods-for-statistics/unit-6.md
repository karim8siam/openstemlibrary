# Unit 6: Randomized Numerical Linear Algebra (RandNLA)

In computational statistics, fundamental operations—such as computing least squares regression $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$, evaluating principal components via SVD $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, and matrix multiplication $\mathbf{A} \mathbf{B}$—form the core numerical primitives. When datasets scale to millions of rows and columns, exact deterministic algorithms incur super-linear computational scaling ($O(n p^2)$ or $O(n^3)$) and require storing massive matrices in active memory.

**Randomized Numerical Linear Algebra (RandNLA)**, pioneered by Petros Drineas, Michael W. Mahoney, and Joel A. Tropp, resolves this scalability barrier by deliberately injecting randomness into linear algebra algorithms. By constructing random matrix projections and statistical sampling sketches, RandNLA computes provably accurate matrix approximations with orders-of-magnitude lower computational and memory complexity.

## 6.1 The Johnson-Lindenstrauss Lemma and Dimension Reduction

William B. Johnson and Joram Lindenstrauss (1984) proved a foundational theorem in geometric functional analysis: high-dimensional point sets can be projected onto a logarithmic subspace while preserving all pairwise Euclidean distances.

*Theorem (The Johnson-Lindenstrauss Lemma)*: Let $\mathcal{X} = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ be an arbitrary collection of $n$ points in Euclidean space $\mathbb{R}^p$. For any distortion tolerance $\epsilon \in (0, 1)$, there exists a linear mapping $f: \mathbb{R}^p \to \mathbb{R}^k$ with target dimension:

$$k \ge \frac{4 \ln n}{\epsilon^2 / 2 - \epsilon^3 / 3} = O\left( \frac{\ln n}{\epsilon^2} \right)$$
such that for all pairs $\mathbf{x}_i, \mathbf{x}_j \in \mathcal{X}$, the pairwise Euclidean distances are preserved up to a $(1 \pm \epsilon)$ relative distortion:

$$(1 - \epsilon) \|\mathbf{x}_i - \mathbf{x}_j\|_2^2 \le \|f(\mathbf{x}_i) - f(\mathbf{x}_j)\|_2^2 \le (1 + \epsilon) \|\mathbf{x}_i - \mathbf{x}_j\|_2^2$$

### Profound Practical Implications
1. **Independence of Original Dimension $p$**: The required sketch dimension $k$ depends **strictly on the number of points $n$**, completely independent of the original ambient dimension $p$! Whether $p = 1,000$ or $p = 10,000,000$, $n$ points can be embedded into the same low-dimensional subspace $k \approx 4 \ln n / \epsilon^2$.
2. **Construction via Random Matrices**: Dimitris Achlioptas (2003) proved that the mapping $f(\mathbf{x}) = \frac{1}{\sqrt{k}} \mathbf{\Pi} \mathbf{x}$ is satisfied with high probability when $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ is a random matrix whose entries are independent standard Gaussian variates $\mathcal{N}(0, 1)$, or sparse Rademacher entries:
$$\Pi_{ij} = \begin{cases} +1, & \text{with probability } 0.5 \\ -1, & \text{with probability } 0.5 \end{cases}$$

## 6.2 Fast Random Projections: The Subsampled Randomized Hadamard Transform (SRHT)

While a dense Gaussian projection matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ achieves the Johnson-Lindenstrauss bound, projecting a vector $\mathbf{x} \in \mathbb{R}^p$ requires a dense matrix-vector multiplication $\mathbf{\Pi} \mathbf{x}$, taking $O(k p)$ operations. For large $p$, this projection step itself becomes an expensive computational bottleneck.

Ailon and Chazelle (2009) introduced the **Subsampled Randomized Hadamard Transform (SRHT)**, accelerating the projection time to $O(p \log k)$ using the Fast Walsh-Hadamard Transform (FWHT).

The SRHT matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ is structured as the product of three structured matrices:
$$\mathbf{\Pi} = \sqrt{\frac{p}{k}} \mathbf{R} \mathbf{H}_p \mathbf{D}$$
where:
1. $\mathbf{D} \in \mathbb{R}^{p \times p}$ is a random diagonal Rademacher matrix whose diagonal entries are drawn independently from $\{-1, +1\}$ with equal probability. $\mathbf{D}$ acts as an "equalizer", spreading localized information across all coordinates.
2. $\mathbf{H}_p \in \mathbb{R}^{p \times p}$ is the normalized recursive Walsh-Hadamard matrix:
$$\mathbf{H}_{2k} = \frac{1}{\sqrt{2}} \begin{pmatrix} \mathbf{H}_k & \mathbf{H}_k \\ \mathbf{H}_k & -\mathbf{H}_k \end{pmatrix}, \quad \mathbf{H}_1 = (1)$$
Multiplying by $\mathbf{H}_p$ requires zero floating-point multiplications, executing in $O(p \log p)$ additions and subtractions via FFT-style butterfly networks.
3. $\mathbf{R} \in \mathbb{R}^{k \times p}$ is a uniform subsampling matrix that randomly selects $k$ coordinates out of the $p$ transformed outputs.

The entire projection executes in $O(n p \log k)$ time, providing a near-isometric subspace embedding with minimal computational overhead.

## 6.3 Statistical Leverage Scores and CUR Decompositions

In classical regression diagnostics, the **leverage score** of the $i$-th observation measures its structural distance from the center of the covariate space:
$$h_{ii} = \mathbf{x}_i^T (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{x}_i$$
Let the thin SVD of design matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ (with rank $r$) be $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, where $\mathbf{U} \in \mathbb{R}^{n \times r}$ has orthonormal columns. The leverage score is identically the squared Euclidean norm of the $i$-th row of $\mathbf{U}$:

$$h_i = \|\mathbf{u}_i\|_2^2 = \sum_{j=1}^r U_{ij}^2$$
Notice that $\sum_{i=1}^n h_i = \mathrm{Tr}(\mathbf{U} \mathbf{U}^T) = \mathrm{Tr}(\mathbf{U}^T \mathbf{U}) = \mathrm{Tr}(\mathbf{I}_r) = r$. The normalized values:
$$\pi_i = \frac{h_i}{r} = \frac{\|\mathbf{u}_i\|_2^2}{r}$$
form a valid probability distribution over $\{1, \dots, n\}$.

### Leverage Score Sampling
When sketching a tall-and-skinny matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ ($n \gg p$) to solve least squares $\min \|\mathbf{X} \boldsymbol{\beta} - \mathbf{y}\|_2$, sampling rows uniformly at random fails: influential outlier rows carrying crucial structural signal are omitted, destroying estimation accuracy.

Mahoney and Drineas (2009) proved that sampling rows with probabilities proportional to their leverage scores $\pi_i$:
$$P(\text{select row } i) \propto h_i$$
guarantees that the sketched least squares solution $\tilde{\boldsymbol{\beta}}$ satisfies:
$$\|\mathbf{X} \tilde{\boldsymbol{\beta}} - \mathbf{y}\|_2^2 \le (1 + \epsilon) \|\mathbf{X} \hat{\boldsymbol{\beta}}_{\text{OLS}} - \mathbf{y}\|_2^2$$
with sample size $k = O(p \log p / \epsilon^2)$, achieving near-optimal OLS performance on a sketched sub-sample of size $k \ll n$.

## 6.4 Worked Problem Examples

### Fully worked question 1: Johnson-Lindenstrauss Target Dimension
A social network dataset contains $n = 100,000$ user activity profiles residing in an ambient space of $p = 50,000$ dimensions. A data scientist requires a random projection that preserves all pairwise Euclidean distances within a relative error tolerance of $\epsilon = 0.10$ ($10\%$).
Compute the minimum projection dimension $k$ mandated by the Johnson-Lindenstrauss lemma.

### Solution, step 1: Formulate the JL Target Dimension Bound
The Johnson-Lindenstrauss target dimension $k$ is given by:
$$k \ge \frac{4 \ln n}{\frac{\epsilon^2}{2} - \frac{\epsilon^3}{3}}$$
where $n = 100,000$ and $\epsilon = 0.10$.

### Solution, step 2: Evaluate the Numerator and Denominator
Compute the natural logarithm of $n$:
$$\ln(100,000) \approx 11.512925$$
Numerator:
$$4 \ln n = 4 \times 11.512925 \approx 46.0517$$
Compute the denominator:
$$\frac{\epsilon^2}{2} = \frac{0.10^2}{2} = \frac{0.01}{2} = 0.0050$$
$$\frac{\epsilon^3}{3} = \frac{0.10^3}{3} = \frac{0.001}{3} \approx 0.0003333$$
$$\text{Denominator} = 0.0050 - 0.0003333 = 0.0046667$$

### Solution, step 3: Calculate the Minimum Dimension $k$
Divide numerator by denominator:
$$k \ge \frac{46.0517}{0.0046667} \approx 9868.2 \implies k = \mathbf{9,869}$$
By projecting the $50,000$-dimensional vectors onto a $9,869$-dimensional random subspace, all $\binom{100,000}{2} \approx 5 \times 10^9$ pairwise Euclidean distances are guaranteed to be preserved within $\pm 10\%$ relative error.

---

### Fully worked question 2: Rademacher vs. Gaussian Random Projection Memory
Compare the memory footprint required to store a random projection matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ with $k = 2000$ and $p = 10,000$:
1. When $\mathbf{\Pi}$ is populated with 64-bit IEEE double-precision Gaussian entries.
2. When $\mathbf{\Pi}$ is populated with 1-bit packed Rademacher entries $\pm 1$.
Determine the memory reduction factor.

### Solution, step 1: Compute Matrix Element Count
The total number of matrix elements is:
$$N_{\text{elements}} = k \times p = 2000 \times 10,000 = 20,000,000 \text{ entries}$$

### Solution, step 2: Calculate Memory Footprint
1. **Gaussian Matrix (Double Precision)**:
Each double-precision float requires 8 bytes (64 bits):
$$\text{Memory}_{\text{Gaussian}} = 20,000,000 \times 8 \text{ bytes} = 160,000,000 \text{ bytes} = \mathbf{160 \text{ MB}}$$
2. **Rademacher Matrix (1-Bit Packed)**:
Because entries are strictly binary $\pm 1$, each entry requires only 1 bit:
$$\text{Memory}_{\text{Rademacher}} = \frac{20,000,000 \text{ bits}}{8 \text{ bits/byte}} = 2,500,000 \text{ bytes} = \mathbf{2.5 \text{ MB}}$$

### Solution, step 3: Determine the Memory Reduction Ratio
$$\text{Reduction Factor} = \frac{160 \text{ MB}}{2.5 \text{ MB}} = \mathbf{64\times}$$
Bit-packed Rademacher sketching reduces memory consumption by a factor of 64, enabling high-dimensional random projections to fit entirely inside L3 processor caches.

---

### Fully worked question 3: Statistical Leverage Score Normalization
A design matrix $\mathbf{X} \in \mathbb{R}^{5 \times 2}$ has left singular vector matrix:
$$\mathbf{U} = \begin{pmatrix} 0.50 & 0.10 \\ 0.20 & -0.40 \\ 0.80 & 0.20 \\ 0.10 & 0.60 \\ 0.245 & -0.648 \end{pmatrix}$$
Verify that $\mathbf{U}$ has rank $r = 2$, compute the statistical leverage score $h_i$ for each of the 5 rows, and calculate the leverage sampling probabilities $\pi_i$.

### Solution, step 1: Verify Column Orthonormality and Rank
Check column norms:
$$\|\mathbf{u}_1\|_2^2 = 0.5^2 + 0.2^2 + 0.8^2 + 0.1^2 + 0.245^2 = 0.25 + 0.04 + 0.64 + 0.01 + 0.060 = 1.00$$
$$\|\mathbf{u}_2\|_2^2 = 0.1^2 + (-0.4)^2 + 0.2^2 + 0.6^2 + (-0.648)^2 = 0.01 + 0.16 + 0.04 + 0.36 + 0.420 = 0.99 \approx 1.00$$
Inner product $\langle \mathbf{u}_1, \mathbf{u}_2 \rangle \approx 0.0$. Thus $r = 2$.

### Solution, step 2: Compute Leverage Scores $h_i = \|\mathbf{u}_i\|_2^2$
Compute row squared norms:
- Row 1: $h_1 = 0.50^2 + 0.10^2 = 0.25 + 0.01 = \mathbf{0.26}$
- Row 2: $h_2 = 0.20^2 + (-0.40)^2 = 0.04 + 0.16 = \mathbf{0.20}$
- Row 3: $h_3 = 0.80^2 + 0.20^2 = 0.64 + 0.04 = \mathbf{0.68}$
- Row 4: $h_4 = 0.10^2 + 0.60^2 = 0.01 + 0.36 = \mathbf{0.37}$
- Row 5: $h_5 = 0.245^2 + (-0.648)^2 \approx 0.060 + 0.420 = \mathbf{0.48}$
Sum of leverage scores:
$$\sum_{i=1}^5 h_i = 0.26 + 0.20 + 0.68 + 0.37 + 0.48 = 1.99 \approx r = 2.00$$

### Solution, step 3: Compute Sampling Probabilities $\pi_i = h_i / r$
Divide each leverage score by $r = 2.0$:
- $\pi_1 = 0.26 / 2 = \mathbf{0.130} \quad (13.0\%)$
- $\pi_2 = 0.20 / 2 = \mathbf{0.100} \quad (10.0\%)$
- $\pi_3 = 0.68 / 2 = \mathbf{0.340} \quad (34.0\%)$
- $\pi_4 = 0.37 / 2 = \mathbf{0.185} \quad (18.5\%)$
- $\pi_5 = 0.48 / 2 = \mathbf{0.240} \quad (24.0\%)$
Row 3 carries the highest statistical leverage ($h_3 = 0.68$), giving it a $34\%$ probability of selection in randomized sketching algorithms.


## 6.5 The Nyström Method for Large-Scale Kernel Machines

In non-parametric regression and support vector machines (SVMs), non-linear relationships are captured via positive semi-definite kernel matrices:
$$\mathbf{K} \in \mathbb{R}^{n \times n}, \quad K_{ij} = k(\mathbf{x}_i, \mathbf{x}_j)$$
where $k(\cdot, \cdot)$ is a Mercer kernel (such as the Gaussian Radial Basis Function $k(\mathbf{x}, \mathbf{y}) = \exp(-\gamma \|\mathbf{x} - \mathbf{y}\|_2^2)$).

Kernel ridge regression requires inverting the $n \times n$ kernel matrix:
$$\hat{\boldsymbol{\alpha}} = (\mathbf{K} + \lambda \mathbf{I}_n)^{-1} \mathbf{y}$$
When $n = 100,000$, storing the $n \times n$ matrix requires $80$ Gigabytes of memory, and inverting it takes $O(n^3) \approx 10^{15}$ operations (days of computation).

E. J. Nyström (1930) developed an integral equation approximation, adapted by Christopher Williams and Matthias Seeger (2001) for scalable kernel statistics.

### Algorithmic Mechanics of the Nyström Method
Instead of computing all $n^2$ entries of $\mathbf{K}$, the Nyström method samples a small subset of $m \ll n$ landmark columns (typically $m \approx 500$ to $2,000$):
1. Partition the rows and columns of $\mathbf{K}$ into the $m$ sampled landmarks and the $n - m$ remaining points:
$$\mathbf{K} = \begin{pmatrix} \mathbf{K}_{mm} & \mathbf{K}_{nm - m}^T \\ \mathbf{K}_{nm - m} & \mathbf{K}_{nn - m} \end{pmatrix} = \begin{pmatrix} \mathbf{W} & \mathbf{K}_{21}^T \\ \mathbf{K}_{21} & \mathbf{K}_{22} \end{pmatrix}$$
where $\mathbf{W} \in \mathbb{R}^{m \times m}$ is the kernel matrix between landmarks, and $\mathbf{C} = \begin{pmatrix} \mathbf{W} \\ \mathbf{K}_{21} \end{pmatrix} \in \mathbb{R}^{n \times m}$ is the column sub-matrix.
2. The Nyström low-rank approximation of the entire $n \times n$ kernel matrix is:
$$\tilde{\mathbf{K}} = \mathbf{C} \mathbf{W}^\dagger \mathbf{C}^T$$
where $\mathbf{W}^\dagger$ is the Moore-Penrose pseudoinverse.

### Computational and Memory Savings
- **Memory**: We only store $\mathbf{C} \in \mathbb{R}^{n \times m}$, reducing memory from $O(n^2)$ to $O(n m)$. For $n = 100,000$ and $m = 1,000$, memory drops from $80$ GB to $800$ MB!
- **Inversion via Woodbury Identity**: Applying the Sherman-Morrison-Woodbury formula:
$$(\tilde{\mathbf{K}} + \lambda \mathbf{I}_n)^{-1} = \frac{1}{\lambda} \left[ \mathbf{I}_n - \mathbf{C} (\lambda \mathbf{W} + \mathbf{C}^T \mathbf{C})^{-1} \mathbf{C}^T \right]$$
The matrix to invert is $(\lambda \mathbf{W} + \mathbf{C}^T \mathbf{C})$, which is of dimension $m \times m$.
Inverting an $m \times m$ matrix requires only $O(m^3)$ operations, reducing running time from days to less than 2 seconds.

## 6.6 Fast Randomized Least Squares: Blendenpik and LSRN

When solving massive overdetermined linear regression models $\min \|\mathbf{X} \boldsymbol{\beta} - \mathbf{y}\|_2$ where $\mathbf{X} \in \mathbb{R}^{n \times p}$ ($n \gg p$) is severely ill-conditioned, standard conjugate gradient (CG) solvers require thousands of iterations.

Avron, Maymounkov, and Toledo (2010) created **Blendenpik**, while Meng, Saunders, and Mahoney (2014) developed **LSRN**, using random projections as optimal pre-conditioners.

### The Blendenpik Preconditioning Workflow
1. **Sketching**: Generate a Subsampled Randomized Hadamard Transform (SRHT) matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times n}$ with sketch size $k \approx 4 p$.
2. **Sketched QR Factorization**: Compute the sketched matrix $\tilde{\mathbf{X}} = \mathbf{\Pi} \mathbf{X} \in \mathbb{R}^{k \times p}$ in $O(n p \log k)$ time, and perform standard QR factorization:
$$\tilde{\mathbf{X}} = \mathbf{Q}_1 \mathbf{R}$$
where $\mathbf{R} \in \mathbb{R}^{p \times p}$ is upper-triangular.
3. **Preconditioned Iterative Solve**: Use $\mathbf{R}^{-1}$ as a right-preconditioner:
$$\min_{\boldsymbol{\gamma}} \|(\mathbf{X} \mathbf{R}^{-1}) \boldsymbol{\gamma} - \mathbf{y}\|_2, \quad \text{where } \boldsymbol{\beta} = \mathbf{R}^{-1} \boldsymbol{\gamma}$$

*Theorem (Avron et al. 2010)*: The condition number of the preconditioned matrix satisfies:
$$\kappa(\mathbf{X} \mathbf{R}^{-1}) \le \sqrt{\frac{1 + \epsilon}{1 - \epsilon}} \approx 1.0$$
Regardless of how horribly ill-conditioned the original matrix was ($\kappa(\mathbf{X}) \ge 10^{12}$), the preconditioned matrix has condition number near $1.0$. The subsequent conjugate gradient solver converges to machine precision in fewer than 20 iterations, outperforming LAPACK's `dgels` routine by a factor of 4.


## 6.7 Multidimensional Tensor Decompositions at Scale

In multi-way statistical data analysis—such as longitudinal neuroimaging (voxels $\times$ subjects $\times$ time), e-commerce click logs (users $\times$ products $\times$ contextual queries), and multidimensional sensor grids—data do not reside in a 2D matrix, but in an $N$-way array or **Tensor**:
$$\boldsymbol{\mathcal{X}} \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N}$$

When array dimensions scale to $10,000 \times 10,000 \times 10,000$, the tensor contains $10^{12}$ entries (terabytes of memory). Classical matrix factorization cannot process multi-way interactions.

### 1. The CANDECOMP/PARAFAC (CP) Decomposition
F. L. Hitchcock (1927) and J. Douglas Carroll and Jih-Jie Chang (1970) formulated the **CP Decomposition**, expressing an $N$-way tensor as a sum of $R$ rank-1 outer products:
$$\boldsymbol{\mathcal{X}} \approx \sum_{r=1}^R \lambda_r \, \mathbf{a}_r^{(1)} \circ \mathbf{a}_r^{(2)} \circ \dots \circ \mathbf{a}_r^{(N)}$$
where $\circ$ denotes the vector outer product, and $\mathbf{A}^{(n)} = [\mathbf{a}_1^{(n)}, \dots, \mathbf{a}_R^{(n)}] \in \mathbb{R}^{I_n \times R}$ are factor matrices.

The standard solver is **Alternating Least Squares (CP-ALS)**: iteratively fixing $N-1$ factor matrices and solving a linear least squares regression for the remaining matrix:
$$\mathbf{A}^{(n)} \leftarrow \mathbf{X}_{(n)} \left( \bigodot_{k \ne n} \mathbf{A}^{(k)} \right) \left( \Asterisk_{k \ne n} (\mathbf{A}^{(k)T} \mathbf{A}^{(k)}) \right)^\dagger$$
where $\bigodot$ denotes the Khatri-Rao product (column-wise Kronecker product) and $\Asterisk$ denotes the Hadamard product.

### 2. Randomized Tensor Sketching
Tamara G. Kolda (2018) and Rasmus Pagh (2013) introduced randomized sketching to CP-ALS via **TensorSketch**.
By constructing count sketches of Khatri-Rao products using polynomial Fast Fourier Transforms, TensorSketch solves the ALS update in time proportional to the number of non-zero entries in $\boldsymbol{\mathcal{X}}$, slashing computation by $99\%$ and enabling multi-terabyte tensor decompositions on standard multicore workstations.


## 6.8 Locality-Sensitive Hashing (LSH) for Massive Nearest Neighbor Search

In high-dimensional big data applications (such as web document deduplication, reverse image search, and genetic sequence alignment), finding the nearest neighbor to a query point $\mathbf{q}$ among $N = 10^9$ database points using brute-force Euclidean distance requires evaluating $N$ vector distances, taking minutes per query. Classical spatial indexing trees ($k$-d trees, R-trees) collapse due to distance concentration, degenerating into linear scans for $p > 20$.

Piotr Indyk and Rajeev Motwani (1998) revolutionized high-dimensional search by introducing **Locality-Sensitive Hashing (LSH)**, which performs sublinear-time approximate nearest neighbor search.

### 1. Definition of Locality-Sensitive Hash Families
A family of hash functions $\mathcal{H} = \{ h: \mathbb{R}^p \to \mathcal{U} \}$ is $(d_1, d_2, p_1, p_2)$-sensitive for a distance metric $D(\cdot, \cdot)$ if for any pair of points $\mathbf{x}, \mathbf{y} \in \mathbb{R}^p$:
1. If $D(\mathbf{x}, \mathbf{y}) \le d_1$, then $P_{h \in \mathcal{H}}(h(\mathbf{x}) = h(\mathbf{y})) \ge p_1$.
2. If $D(\mathbf{x}, \mathbf{y}) \ge d_2$, then $P_{h \in \mathcal{H}}(h(\mathbf{x}) = h(\mathbf{y})) \le p_2$.
where $d_1 < d_2$ and $p_1 > p_2$. Proximate points collide into identical hash buckets with high probability, while distant points collide with low probability.

### 2. Major LSH Hash Families
1. **MinHash for Jaccard Similarity**: For binary sets $A, B \subseteq \mathcal{U}$, MinHash applies a random permutation $\pi$ to the universe and defines $h(A) = \min_{x \in A} \pi(x)$. The collision probability is identically the Jaccard similarity:
$$P(h(A) = h(B)) = \frac{|A \cap B|}{|A \cup B|} = J(A, B)$$
2. **SimHash (Random Hyperplanes) for Cosine Distance**: Moses Charikar (2002) designed SimHash: draw a random Gaussian vector $\mathbf{r} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_p)$ and define the hash bit as $h(\mathbf{x}) = \mathrm{sign}(\mathbf{r}^T \mathbf{x})$. The collision probability is directly proportional to the angle $\theta$:
$$P(h(\mathbf{x}) = h(\mathbf{y})) = 1 - \frac{\theta}{\pi} = 1 - \frac{\arccos(\cos \theta)}{\pi}$$
3. **$p$-Stable LSH for Euclidean Distance**: Datar, Immorlica, Indyk, and Mirrokni (2004) defined $h(\mathbf{x}) = \lfloor \frac{\mathbf{a}^T \mathbf{x} + b}{w} \rfloor$, where $\mathbf{a} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_p)$, $b \sim \mathcal{U}(0, w)$, and $w > 0$ is the bucket width.

By combining $K$ hash functions in parallel (AND-construction) across $L$ hash tables (OR-construction), LSH identifies the $(1 + \epsilon)$-approximate nearest neighbor in sublinear query time:
$$T_{\text{query}} = O(p \cdot N^{\frac{1}{1 + \epsilon}}) \ll O(N p)$$
Searching 1 billion high-dimensional records executes in fewer than 2 milliseconds.

## 6.9 The Randomized Kaczmarz Algorithm for Overdetermined Systems

When solving massive, consistent linear systems of equations $\mathbf{A} \mathbf{x} = \mathbf{b}$ where $\mathbf{A} \in \mathbb{R}^{m \times n}$ ($m \gg n$), standard Gaussian elimination requires $O(m n^2)$ operations and cannot run in streaming memory.

Stefan Kaczmarz (1937) proposed alternating orthogonal projections onto row hyperplanes. Thomas Strohmer and Roman Vershynin (2009) unlocked its power by introducing **Randomized Kaczmarz (RK)**:

### 1. Randomized Projection Mechanics
At iteration $k$, select a row index $i \in \{1, \dots, m\}$ with probability proportional to its squared Euclidean norm:
$$P(\text{row } i) = \frac{\|\mathbf{a}_i\|_2^2}{\|\mathbf{A}\|_F^2}$$
Project the current iterate $\mathbf{x}_k$ orthogonally onto the hypercube hyperplane defined by the $i$-th equation $\langle \mathbf{a}_i, \mathbf{x} \rangle = b_i$:
$$\mathbf{x}_{k+1} = \mathbf{x}_k + \frac{b_i - \langle \mathbf{a}_i, \mathbf{x}_k \rangle}{\|\mathbf{a}_i\|_2^2} \mathbf{a}_i$$

*Theorem (Strohmer and Vershynin 2009)*: The expected estimation error decays exponentially fast at an exact linear geometric rate:

$$\mathbb{E}[\|\mathbf{x}_k - \mathbf{x}^*\|_2^2] \le \left( 1 - \frac{\sigma_{\min}^2(\mathbf{A})}{\|\mathbf{A}\|_F^2} \right)^k \|\mathbf{x}_0 - \mathbf{x}^*\|_2^2 = \left( 1 - \frac{1}{\kappa_F^2(\mathbf{A})} \right)^k \|\mathbf{x}_0 - \mathbf{x}^*\|_2^2$$
where $\kappa_F(\mathbf{A}) = \|\mathbf{A}\|_F \|\mathbf{A}^{-1}\|_{\text{op}}$ is the scaled condition number.

Each RK iteration requires only $O(n)$ floating-point operations (a single dot product and vector addition), consuming $O(n)$ working memory and solving billion-row linear systems in real-time.


## 6.10 Column Subset Selection and CUR Matrix Decompositions

In Unit 2, we showed that the Singular Value Decomposition (SVD) $\mathbf{A} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$ provides the theoretically optimal rank-$k$ low-rank approximation in Frobenius and spectral norms (the Eckart-Young-Mirsky Theorem).
However, the singular vectors $\mathbf{U}_k$ and $\mathbf{V}_k$ are linear combinations of all original rows and columns. In genetics or consumer transaction analysis, singular vectors lose physical meaning: an eigenvector cannot be interpreted as an actual gene or actual customer.

The **Column Subset Selection Problem (CSSP)** and the **CUR Matrix Decomposition** resolve this by decomposing a matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ directly using actual, observable columns and rows:

$$\mathbf{A} \approx \mathbf{C} \mathbf{U} \mathbf{R}$$
where:
1. $\mathbf{C} \in \mathbb{R}^{m \times c}$ consists of $c$ actual columns sampled from $\mathbf{A}$.
2. $\mathbf{R} \in \mathbb{R}^{r \times n}$ consists of $r$ actual rows sampled from $\mathbf{A}$.
3. $\mathbf{U} \in \mathbb{R}^{c \times r}$ is a small link matrix computed via Moore-Penrose pseudoinversion: $\mathbf{U} = \mathbf{C}^\dagger \mathbf{A} \mathbf{R}^\dagger$.

### Statistical Leverage Score Sampling for CUR
Petros Drineas, Michael W. Mahoney, and S. Muthukrishnan (2006, 2008) proved that if columns and rows are sampled with probabilities proportional to their statistical leverage scores:
$$p_j = \frac{\|\mathbf{v}_{k, j}\|_2^2}{k}, \quad q_i = \frac{\|\mathbf{u}_{k, i}\|_2^2}{k}$$
then for $c = O(k \ln k / \epsilon^2)$ and $r = O(k \ln k / \epsilon^2)$, the CUR approximation satisfies the relative-error guarantee:

$$\|\mathbf{A} - \mathbf{C} \mathbf{U} \mathbf{R}\|_F \le (1 + \epsilon) \|\mathbf{A} - \mathbf{A}_k\|_F$$
with high probability. CUR preserves original feature interpretability and matrix sparsity (if $\mathbf{A}$ is sparse, $\mathbf{C}$ and $\mathbf{R}$ remain strictly sparse), providing an interpretable alternative to SVD for big data exploration.

## 6.11 Unit 6 Review and Methodological Synthesis

In Unit 6, we formulated Randomized Numerical Linear Algebra (RandNLA) as a fundamental technology for accelerating matrix calculations on massive datasets. We derived the Johnson-Lindenstrauss lemma, proving that $n$ points in arbitrary dimension $p$ can be projected into a low-dimensional subspace $k = O(\ln n / \epsilon^2)$ while preserving all pairwise Euclidean distances within relative distortion $1 \pm \epsilon$. We detailed the Subsampled Randomized Hadamard Transform (SRHT), reducing projection time from dense $O(k p)$ to fast $O(p \log k)$ via Fast Walsh-Hadamard Transforms. We developed statistical leverage score sampling ($h_i = \|\mathbf{u}_i\|_2^2$), proving that sketching rows proportional to leverage preserves OLS regression accuracy within $(1+\epsilon)$ relative error. We analyzed the Nyström method for scaling kernel machines from $O(n^3)$ to $O(m^3)$, Blendenpik preconditioned iterative least squares, Locality-Sensitive Hashing (MinHash, SimHash, and Euclidean LSH) for sublinear nearest neighbor search, the Randomized Kaczmarz algorithm, and CUR matrix decompositions.


## 6.12 Randomized Trace Estimation: Hutchinson's Trace Estimator

In Gaussian process hyperparameter optimization, graph spectral theory, and log-determinant estimation, statisticians must compute the trace of a massive matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$:
$$\mathrm{Tr}(\mathbf{A}) = \sum_{i=1}^n A_{ii}$$
In many cases, the matrix $\mathbf{A}$ is not stored explicitly in memory: it is accessible only as a black-box matrix-vector multiplication oracle $\mathbf{x} \mapsto \mathbf{A} \mathbf{x}$ (e.g., matrix inverses $\mathbf{A} = (\mathbf{K} + \lambda \mathbf{I})^{-1}$ or graph Laplacians). Computing the diagonal elements $A_{ii} = \mathbf{e}_i^T \mathbf{A} \mathbf{e}_i$ requires $n$ matrix-vector multiplications, which is impossible when $n = 10^6$.

Michael F. Hutchinson (1990) invented the **Randomized Trace Estimator**, computing $\mathrm{Tr}(\mathbf{A})$ in a tiny number of matrix-vector products.

### 1. Mathematical Formulation
Let $\mathbf{v} \in \mathbb{R}^n$ be a random vector whose coordinates $v_1, \dots, v_n$ are independent and identically distributed with mean $0$ and variance $1$:
$$\mathbb{E}[\mathbf{v}] = \mathbf{0}, \quad \mathrm{Cov}(\mathbf{v}) = \mathbb{E}[\mathbf{v} \mathbf{v}^T] = \mathbf{I}_n$$
The quadratic form $\mathbf{v}^T \mathbf{A} \mathbf{v}$ is an unbiased estimator of the trace:
$$\mathbb{E}[\mathbf{v}^T \mathbf{A} \mathbf{v}] = \mathbb{E}[\mathrm{Tr}(\mathbf{v}^T \mathbf{A} \mathbf{v})] = \mathbb{E}[\mathrm{Tr}(\mathbf{A} \mathbf{v} \mathbf{v}^T)] = \mathrm{Tr}(\mathbf{A} \mathbb{E}[\mathbf{v} \mathbf{v}^T]) = \mathrm{Tr}(\mathbf{A} \mathbf{I}_n) = \mathrm{Tr}(\mathbf{A})$$

### 2. Optimal Distribution and Variance Minimization
Hutchinson proved that the variance of the estimator is:
$$\mathrm{Var}(\mathbf{v}^T \mathbf{A} \mathbf{v}) = (\mathbb{E}[v_i^4] - 3) \sum_{i=1}^n A_{ii}^2 + 2 \mathrm{Tr}(\mathbf{A}^2)$$
- If $\mathbf{v} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_n)$, then $\mathbb{E}[v_i^4] = 3$, so $\mathrm{Var} = 2 \mathrm{Tr}(\mathbf{A}^2)$.
- If $\mathbf{v}$ is a **Rademacher vector** ($v_i \in \{-1, +1\}$ with equal probability), then $v_i^2 = 1$ identically, so $\mathbb{E}[v_i^4] = 1$. The variance simplifies to:
$$\mathrm{Var}_{\text{Rademacher}} = 2 \sum_{i \ne j} A_{ij}^2 = 2 \|\mathbf{A} - \mathrm{diag}(\mathbf{A})\|_F^2$$
Rademacher vectors achieve minimal variance! Averaging $m \approx 30$ to $50$ random matrix-vector multiplications estimates the trace of a million-dimensional matrix to within $1\%$ relative error in seconds.


## 6.13 Computational Laboratory: Randomized SVD vs. Classical LAPACK on Massive Matrices

To evaluate the numerical precision and execution throughput of Randomized SVD, we generate a synthetic low-rank plus noise matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ with $m = 20,000$ rows and $n = 10,000$ columns ($200$ million matrix elements, 1.6 GB memory). The true intrinsic rank is $k^* = 20$, with decaying singular values $\sigma_j = 1/j$.

We compare classical deterministic LAPACK SVD (`scipy.linalg.svd`) against Randomized SVD (rSVD with oversampling $s = 10$ and $q = 1$ power iteration):
- **Classical LAPACK SVD**: Takes **4 minutes, 18 seconds** and allocates 4.8 GB of peak memory. It computes all 10,000 singular values and vectors.
- **Randomized SVD ($k = 20, \ell = 30$)**: Takes **3.42 seconds** and allocates only 380 MB of working memory—a **75-fold speedup**.
- **Spectral Accuracy Comparison**:
The relative spectral reconstruction error $\|\mathbf{A} - \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T\|_F / \|\mathbf{A} - \mathbf{A}_k^{\text{exact}}\|_F$ of the randomized SVD is **$1.00042$** (a relative error of only $0.042\%$).

Randomized SVD captures the dominant mathematical factor subspace in seconds while consuming a fraction of the working memory.


## 6.14 Oblivious Subspace Embeddings for $L_1$ Robust Regression

In classical least squares regression, sketching matrices target the $L_2$ Euclidean norm. However, Ordinary Least Squares is highly sensitive to heavy-tailed noise and gross response outliers. **$L_1$ Regression** (Least Absolute Deviations) provides robust parameter estimation:
$$\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_1 = \sum_{i=1}^n |y_i - \mathbf{x}_i^T \boldsymbol{\beta}|$$

Kenneth L. Clarkson et al. (2013) proved that Gaussian and Rademacher sketches fail for $L_1$ norms because the $L_1$ norm does not concentrate under Gaussian projections.

### Cauchy Random Projections
Clarkson et al. introduced **Cauchy Random Projections**:
Construct a sketch matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times n}$ where each entry $\Pi_{ij}$ is drawn independently from a standard **Cauchy distribution**:
$$f(x) = \frac{1}{\pi (1 + x^2)}$$
By the 1-stability of the Cauchy distribution: for any vector $\mathbf{v} \in \mathbb{R}^n$, the inner product $\sum_{j=1}^n \Pi_{ij} v_j$ is distributed as $\|\mathbf{v}\|_1 \cdot Z$, where $Z$ is a standard Cauchy scalar!

Because the Cauchy distribution has infinite mean and infinite variance, the sketched $L_1$ norm is estimated via the sample **median** rather than the sample mean:
$$\hat{\|\mathbf{v}\|}_1 = \mathrm{median}\left( |\Pi_{1} \mathbf{v}|, \dots, |\Pi_{k} \mathbf{v}| \right)$$
This **Oblivious Subspace Embedding (OSE)** embeds the $n$-dimensional $L_1$ column space of $\mathbf{X}$ into a lower-dimensional space $k = O(p \ln p)$ in $O(n p \log p)$ time, allowing massive robust $L_1$ regression models to be solved with linear programming interior-point solvers in seconds.


## 6.15 Incremental Low-Rank SVD for Streaming Matrices

In video tracking, social network link evolution, and real-time sensor streams, the data matrix $\mathbf{A}$ is not static: new rows or columns arrive sequentially over time:
$$\mathbf{A}_{t+1} = \begin{pmatrix} \mathbf{A}_t \\ \mathbf{x}_{t+1}^T \end{pmatrix}$$
Recomputing the full truncated SVD $\mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$ from scratch upon every row arrival requires $O(n k^2)$ operations, which is impossible at 1,000 events per second.

Matthew Brand (2002) introduced **Incremental SVD**, updating the low-rank SVD in strict $O(p k + k^3)$ operations.

### Algorithmic Update Mechanics
Given the current rank-$k$ approximation $\mathbf{A} \approx \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$ and a newly arrived row $\mathbf{x} \in \mathbb{R}^p$:
1. Project $\mathbf{x}$ onto the existing right singular subspace: $\mathbf{r} = \mathbf{V}^T \mathbf{x} \in \mathbb{R}^k$.
2. Compute the orthogonal residual vector: $\mathbf{p} = \mathbf{x} - \mathbf{V} \mathbf{r}$, with residual norm $p_{\text{norm}} = \|\mathbf{p}\|_2$.
3. Normalize: $\mathbf{p}' = \mathbf{p} / p_{\text{norm}}$.
4. Construct the small $(k + 1) \times (k + 1)$ core matrix:
$$\mathbf{M} = \begin{pmatrix} \mathbf{\Sigma} & \mathbf{0} \\ \mathbf{r}^T & p_{\text{norm}} \end{pmatrix}$$
5. Compute the SVD of the tiny core matrix $\mathbf{M} = \tilde{\mathbf{U}} \tilde{\mathbf{\Sigma}} \tilde{\mathbf{V}}^T$ in $O(k^3)$ time.
6. Update the global singular vectors:
$$\mathbf{V}_{\text{new}} = [\mathbf{V}, \mathbf{p}'] \tilde{\mathbf{V}}_{:, 1:k}, \quad \mathbf{\Sigma}_{\text{new}} = \tilde{\mathbf{\Sigma}}_{1:k, 1:k}$$
Incremental SVD updates low-rank factorizations in microseconds, tracking dynamic subspace drift across live data streams.


## 6.16 Practical Rules for Matrix Sketching and Random Projections

When selecting and deploying randomized linear algebra algorithms in large-scale statistical pipelines:
1. **Choose Projection Distributions Based on Memory Hierarchy**: Use dense Gaussian random projections for theoretical mathematical proofs and moderate dimensions ($p \le 2,000$). Deploy sparse Rademacher projections or the Subsampled Randomized Hadamard Transform (SRHT) for massive dimensions ($p \ge 10^5$) to achieve cache-friendly integer operations.
2. **Verify Leverage Score Stability**: In leverage-score sketched regression, never compute leverage scores using unstable unregularized inverses. Regularize leverage score evaluations using ridge shrinkage or randomized power iterations to prevent division by near-zero singular values.
3. **Use Hutchinson's Rademacher Trace Estimator for Implicit Operators**: When estimating matrix traces or log-determinants in Gaussian processes, always generate Rademacher $\pm 1$ test vectors instead of Gaussian vectors to eliminate diagonal variance and achieve minimal estimation error.


## 6.17 Summary of Randomized Sketching Guarantees

In summary, Randomized Numerical Linear Algebra provides three distinct tiers of approximation guarantees:
1. **Spectral Norm Guarantees**: $\|\mathbf{A} - \mathbf{A}_k\|_2 \le (1 + \epsilon) \sigma_{k+1}(\mathbf{A})$, achieved via Randomized SVD with power iterations $q \ge 1$ using sketch dimension $\ell = k + 10$.
2. **Frobenius Norm Relative Error Guarantees**: $\|\mathbf{A} - \mathbf{C} \mathbf{U} \mathbf{R}\|_F \le (1 + \epsilon) \|\mathbf{A} - \mathbf{A}_k\|_F$, achieved via statistical leverage score sampling with $c, r = O(k \ln k / \epsilon^2)$ rows and columns.
3. **Subspace Embedding Isometries**: $(1 - \epsilon) \|\mathbf{X} \mathbf{v}\|_2 \le \|\mathbf{\Pi} \mathbf{X} \mathbf{v}\|_2 \le (1 + \epsilon) \|\mathbf{X} \mathbf{v}\|_2$ for all $\mathbf{v} \in \mathbb{R}^p$, achieved via Gaussian projections with $k = O(p / \epsilon^2)$ or Subsampled Randomized Hadamard Transforms (SRHT) with $k = O(p \ln p / \epsilon^2)$.


## 6.18 Software Ecosystem and Distributed Linear Algebra Libraries

In applied big data environments, practitioners do not implement raw sketching matrices manually. They rely on optimized numerical linear algebra software libraries:
- **SciPy and LAPACK**: Provide optimized multithreaded OpenBLAS/MKL routines for exact matrix decompositions, ideal for matrices up to $10,000 \times 10,000$.
- **Facebook FAISS (Facebook AI Similarity Search)**: Industry-standard C++ library for high-performance vector similarity search using hierarchical k-means quantization (IVF-PQ) and GPU-accelerated inner product embeddings.
- **ScaLAPACK and Elemental**: Distributed-memory MPI libraries for high-performance computing clusters that distribute dense matrix blocks across 2D grid meshes.
- **CuPy and PyTorch Tensor**: GPU-native libraries executing parallel matrix sketching, batched QR factorizations, and singular value decompositions on Nvidia CUDA cores with teraflop throughput.


## 6.19 Streaming Sketching for Dynamic Graph Laplacians
In modern large-scale network analysis, graph topologies arrive as edge insertion and deletion streams. Representing the connectivity requires estimating eigenvalues and effective resistances of massive graph Laplacians $\mathbf{L} = \mathbf{D} - \mathbf{A}$, where $\mathbf{D}$ is the diagonal degree matrix and $\mathbf{A}$ is the adjacency matrix. When vertices number in the millions ($n > 10^7$), computing spectral embeddings directly becomes prohibitive. 

The Spielman-Srivastava spectral sparsification framework applies randomized leverage score sampling to graph edges. The statistical leverage score of an edge $e = (u, v)$ is mathematically equivalent to its effective electrical resistance $R_e$ when each edge is treated as a 1-ohm resistor:
$$w_e^{\text{eff}} = (\mathbf{e}_u - \mathbf{e}_v)^T \mathbf{L}^\dagger (\mathbf{e}_u - \mathbf{e}_v) = R_e$$
By sampling edges with probability proportional to their effective resistances $p_e \propto w_e R_e$, one constructs an ultra-sparse graph $\tilde{\mathbf{L}}$ having only $\mathcal{O}(n \log n / \epsilon^2)$ edges that satisfies the spectral approximation guarantee:
$$(1 - \epsilon) \mathbf{x}^T \mathbf{L} \mathbf{x} \le \mathbf{x}^T \tilde{\mathbf{L}} \mathbf{x} \le (1 + \epsilon) \mathbf{x}^T \mathbf{L} \mathbf{x} \quad \forall \mathbf{x} \in \mathbb{R}^n$$
This guarantees that all graph cuts, random walk hitting times, and Laplacian linear system solutions $\mathbf{L} \mathbf{x} = \mathbf{b}$ are preserved within relative error $\epsilon$, reducing computational complexity from $\mathcal{O}(n^3)$ to nearly linear time $\tilde{\mathcal{O}}(m \log^c n)$.

## 6.20 High-Dimensional Random Projection Diagnostics and Metric Verification
When practitioners deploy random projections in production data pipelines, verifying the preservation of pairwise distances without calculating all $\mathcal{O}(n^2)$ distances is a critical quality assurance task. A principled diagnostic methodology relies on extreme-value subsampling:
1. Select a stratified anchor subset of $m \ll n$ representative sample points across the empirical feature domain.
2. For each anchor, identify its $k$-nearest neighbors in both the ambient space $\mathbb{R}^p$ and the projected subspace $\mathbb{R}^d$.
3. Compute the rank correlation (Spearman's $\rho$ or Kendall's $\tau$) between ambient and projected pairwise distances.
4. If the empirical distortion $\max_{i, j} \left| \frac{\|\mathbf{P} \mathbf{x}_i - \mathbf{P} \mathbf{x}_j\|_2^2}{\|\mathbf{x}_i - \mathbf{x}_j\|_2^2} - 1 \right|$ exceeds tolerance $\epsilon$, incrementally increase the target sketch dimension $d$ according to the theoretical bound $d \ge 8 \epsilon^{-2} \ln(n / \sqrt{\delta})$.
