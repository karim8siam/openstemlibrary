# tooling/add-depth-final-push.py

# 1. Expand Unit 8
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "r", encoding="utf-8") as f:
    u8 = f.read()

u8_addition = r"""

---

## 8.12 Cloud-Native Multidimensional Array Storage: HDF5, Zarr, and Object Stores

In contemporary data-intensive science—including satellite remote sensing grids, climate simulation reanalyses (ERA5), and single-cell spatial transcriptomics—data arrives as multi-terabyte $N$-dimensional numerical arrays. Managing these colossal arrays exceeds the architectural capabilities of tabular formats like CSV or Parquet, requiring specialized **hierarchical multidimensional array stores**.

### Hierarchical Data Format (HDF5)

Created by the National Center for Supercomputing Applications (NCSA), **HDF5 (Hierarchical Data Format 5)** is an on-disk filesystem-within-a-file designed to store petabyte-scale array datasets.
- **Hierarchical POSIX Group Structure**: Datasets are organized into nested directory paths (`/experiments/subject_01/fMRI_raw`) with attached metadata attributes.
- **Chunked Storage and Filters**: Datasets are partitioned into regular multidimensional chunk blocks (e.g. $128 \times 128 \times 64$). Chunks are transparently passed through dynamic compression pipelines (gzip, lzf, blosc) before being written to disk.
- **B-Tree Chunk Indexing**: Slicing an arbitrary multidimensional sub-volume (e.g. extracting a time series across a single voxel: `data[:, 42, 108]`) uses internal B-trees to seek directly to the relevant chunk byte offsets on disk without loading unrequested data.
- **Concurrency Limitation**: Standard HDF5 relies on a single monolithic binary file with mandatory global file-locking, preventing concurrent multi-process writes across distributed cloud clusters.

### Zarr and Cloud-Native Object Stores (S3 / GCS)

To overcome the file-locking limitations of HDF5 in distributed cloud environments, Alistair Miles and the scientific Python community created **Zarr**.

Instead of storing all chunks in a single locked file:
1. **Key-Value Chunk Partitioning**: Zarr stores each compressed array chunk as a **separate, distinct file or cloud object key**:
   ```text
   gs://bucket/climate.zarr/temperature/c/0/14/2
   s3://bucket/genomics.zarr/expression/c/105/4
   ```
2. **Metadata in Pure JSON**: Group hierarchy, data types, chunk shapes, and compressor codecs are stored in human-readable `.zmetadata` and `.zarray` JSON files.
3. **Lockless Asynchronous Cloud Concurrency**: Because each chunk is an independent HTTP REST object, thousands of parallel cloud worker nodes (in AWS Lambda, Google Cloud Run, or Apache Spark) can write to disjoint chunks simultaneously without encountering any file-locking contention.
4. **Blosc Ultra-Fast Compression**: Zarr utilizes the Blosc meta-compressor, which uses CPU SIMD instruction vectorization to accelerate in-memory compression to memory-bus speeds (over $3 \text{ GB/sec}$).

In both Python (`zarr`, `xarray`) and R (`pizzarr`), Zarr represents the state-of-the-art storage standard for petabyte-scale statistical array computation in the cloud.
"""

marker = "## Fully worked question 1:"
idx = u8.find(marker)
u8_new = u8[:idx] + u8_addition.strip() + "\n\n" + u8[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "w", encoding="utf-8") as f:
    f.write(u8_new)
print("Expanded Unit 8 final push!")

# 2. Expand Unit 7
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "r", encoding="utf-8") as f:
    u7 = f.read()

u7_addition = r"""

---

## 7.12 Automatic Differentiation (AutoDiff): Forward Mode, Reverse Mode, and Modern Computational Graphs

In modern statistical computing—such as fitting non-linear mixed models, deep neural networks, Hamiltonian Monte Carlo (HMC/NUTS), and variational inference—optimization algorithms require exact gradients $\nabla f(\boldsymbol{\theta})$ and Hessians $\nabla^2 f(\boldsymbol{\theta})$.

Historically, statisticians relied on two flawed approaches:
- **Numerical Differentiation (Finite Differences)**:
  $$\frac{\partial f}{\partial \theta_j} \approx \frac{f(\boldsymbol{\theta} + h \mathbf{e}_j) - f(\boldsymbol{\theta})}{h}$$
  Suffers from truncation error when $h$ is large, and catastrophic floating-point cancellation when $h$ is small. Furthermore, computing a gradient for $p$ parameters requires $p + 1$ function evaluations, making it hopelessly slow for high-dimensional models.
- **Symbolic Differentiation**: Computes exact algebraic formulas via computer algebra systems (Mathematica, SymPy), but suffers from **expression swell**, producing exponentially complex equations that choke compilers.

The modern solution that powers PyTorch, JAX, Stan, and TensorFlow is **Automatic Differentiation (AutoDiff)**. AutoDiff evaluates exact mathematical derivatives to machine precision by decomposing computer programs into elementary arithmetic operations and applying the chain rule algorithmically.

### Forward-Mode AutoDiff and Dual Numbers

Forward-mode AutoDiff evaluates derivatives simultaneously alongside the primal function evaluation using the algebra of **Dual Numbers**:

$$x = a + b \epsilon, \quad \text{where } \epsilon^2 = 0 \text{ with } \epsilon \ne 0$$

Let $f(x)$ be a function. Evaluating $f$ on a dual number expands via Taylor series:
$$f(a + b \epsilon) = f(a) + f'(a) b \epsilon + \frac{f''(a)}{2!} (b \epsilon)^2 + \dots = f(a) + f'(a) b \epsilon$$
The real component yields the function value $f(a)$, and the dual component yields the exact derivative $f'(a) b$!

- **Multi-Variable Scaling**: For a function $f: \mathbb{R}^p \to \mathbb{R}^m$, evaluating the Jacobian requires $p$ forward passes (one per input coordinate).
- Forward-mode is optimal when $p \ll m$ (few inputs, many outputs).

### Reverse-Mode AutoDiff (Backpropagation)

When a statistical objective function maps a massive parameter vector $\boldsymbol{\theta} \in \mathbb{R}^p$ to a single scalar loss or log-likelihood value $\ell: \mathbb{R}^p \to \mathbb{R}$ (so $m = 1$ and $p \gg 1$, typical in regression, neural nets, and Bayesian posteriors), **Reverse-Mode AutoDiff** is vastly superior.

#### The Two-Pass Execution Mechanics:
1. **The Forward Pass (Tape Recording)**:
   The computer evaluates the objective function from input parameters to the terminal scalar output. Every elementary operation ($+, -, \times, \div, \exp, \sin$) is recorded on an internal directed acyclic execution graph (the **Wengert List** or **Tape**), caching intermediate values.
2. **The Reverse Pass (Adjoint Propagation)**:
   The algorithm initializes the adjoint of the terminal scalar output:
   $$\bar{\ell} = \frac{\partial \ell}{\partial \ell} = 1.0$$
   It then sweeps backward through the recorded tape in reverse topological order, applying the chain rule locally:
   $$\bar{v}_i = \sum_{j \in \text{Children}(i)} \bar{v}_j \frac{\partial v_j}{\partial v_i}$$

#### The Fundamental Complexity Theorem:
The total computational cost of computing the **entire $p$-dimensional gradient vector $\nabla \ell(\boldsymbol{\theta})$ via Reverse-Mode AutoDiff is at most 3 to 4 times the cost of evaluating the scalar function $\ell(\boldsymbol{\theta})$ once**, completely independent of parameter dimension $p$!

$$\text{Cost}(\nabla \ell(\boldsymbol{\theta})) = \mathcal{O}(1) \times \text{Cost}(\ell(\boldsymbol{\theta}))$$

This extraordinary algorithmic efficiency explains why modern probabilistic systems (Stan, PyMC, Pyro) can execute Hamiltonian Monte Carlo trajectories and variational optimizations across models with millions of parameters in seconds.
"""

marker = "## Fully worked question 1:"
idx = u7.find(marker)
u7_new = u7[:idx] + u7_addition.strip() + "\n\n" + u7[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "w", encoding="utf-8") as f:
    f.write(u7_new)
print("Expanded Unit 7 final push!")

# 3. Expand Unit 6
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "r", encoding="utf-8") as f:
    u6 = f.read()

u6_addition = r"""

---

## 6.11 Extreme Value Resampling: GEV Distributions, Peaks-Over-Threshold, and Hill's Index

In risk management, climate extremes (100-year flood levels), and catastrophe insurance, the primary analytical interest lies not in central tendencies (means, medians), but in the extreme tails of the distribution.

### The Fisher–Tippett–Gnedenko Extreme Value Theorem

Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with CDF $F(x)$, and let $M_n = \max(X_1, \dots, X_n)$ denote the sample maximum.
The **Fisher–Tippett–Gnedenko Theorem** (1928, 1943) establishes that if normalizing sequences $a_n > 0$ and $b_n \in \mathbb{R}$ exist such that:

$$\mathbb{P}\left( \frac{M_n - b_n}{a_n} \le z \right) \xrightarrow{d} G(z)$$

then the limiting distribution $G(z)$ must belong to the **Generalized Extreme Value (GEV)** family:

$$G(z) = \exp\left( -\left[ 1 + \xi \left( \frac{z - \mu}{\sigma} \right) \right]_+^{-1/\xi} \right)$$

where $\xi \in \mathbb{R}$ is the **extreme value index (shape parameter)**:
- $\xi = 0$: **Gumbel (Light Tails)**: Exponential, Gaussian, Gamma distributions.
- $\xi > 0$: **Fréchet (Heavy / Power-Law Tails)**: Pareto, Cauchy, Student's $t$ distributions.
- $\xi < 0$: **Weibull (Bounded Support)**: Uniform, Beta distributions with upper finite limits.

### Why Standard Bootstrap Fails on Extreme Values
Suppose we apply Efron's standard non-parametric bootstrap to estimate the sampling distribution of the maximum $M_n$.
In any bootstrap resample of size $n$, the probability that the resample maximum $M_n^*$ equals the observed sample maximum $X_{(n)}$ is:
$$\mathbb{P}(M_n^* = X_{(n)}) = 1 - \left( 1 - \frac{1}{n} \right)^n \to 1 - e^{-1} \approx 63.2\%$$
The bootstrap distribution of the maximum places a discrete point mass of $63.2\%$ on the single point $X_{(n)}$!
In reality, the true maximum $M_n$ has a continuous density with zero point masses. The standard bootstrap is **catastrophically inconsistent for extreme order statistics**.

### Peaks-Over-Threshold (POT) and the Generalized Pareto Distribution (GPD)

To perform valid extreme-tail inference, modern statistics deploys the **Peaks-Over-Threshold (POT)** methodology (Pickands, 1975; Balkema and de Haan, 1974).

Instead of analyzing block maxima $M_n$, the analyst selects a high threshold $u$. For all observations exceeding the threshold ($Y = X - u \mid X > u$), the conditional excess distribution converges asymptotically to the **Generalized Pareto Distribution (GPD)**:

$$H(y) = 1 - \left( 1 + \frac{\xi y}{\tilde{\sigma}} \right)^{-1/\xi}$$

#### Tail Index Estimation via Hill's Estimator:
For heavy-tailed distributions ($\xi > 0$), Bruce Hill (1975) formulated the celebrated **Hill Estimator** based on the $k$ upper order statistics:

$$\hat{\xi}_{Hill}(k) = \frac{1}{k} \sum_{i=1}^k \ln\left( \frac{X_{(n - i + 1)}}{X_{(n - k)}} \right)$$

By fitting the GPD parameters $(\xi, \tilde{\sigma})$ to threshold exceedances and generating parametric bootstrap resamples from the fitted GPD tail, statisticians construct accurate, mathematically consistent confidence intervals for extreme 100-year and 1000-year return levels.
"""

marker = "## Fully worked question 1:"
idx = u6.find(marker)
u6_new = u6[:idx] + u6_addition.strip() + "\n\n" + u6[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "w", encoding="utf-8") as f:
    f.write(u6_new)
print("Expanded Unit 6 final push!")
