# tooling/add-depth-pass-3.py

# 1. Expand Unit 3
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md", "r", encoding="utf-8") as f:
    u3 = f.read()

u3_addition = r"""

---

## 3.8 Interactive Visualization Architectures: SVG, HTML5 Canvas, WebGL, and Reactive Dataflow

In modern statistical communication, web-based dashboards and interactive exploratory interfaces (such as R Shiny, Dash, Streamlit, and Observable notebooks) replace static paper figures. Interactive exploration allows users to pan, zoom, dynamically filter cohorts, adjust smoothing bandwidths in real time, and inspect localized residuals.

### The Rendering Pipeline: SVG vs Canvas vs WebGL

When rendering statistical graphics in the web browser, computational engineers must choose between three fundamental graphics rendering technologies based on dataset scale and interactive frame rates:

#### 1. Scalable Vector Graphics (SVG)
SVG represents graphics as an XML-based tree of Document Object Model (DOM) elements: `<circle>`, `<rect>`, `<path>`.
- **Strengths**: Resolution-independent vector graphics (crisp at any zoom level or Retina display resolution). Every individual graphical mark is a distinct DOM node capable of attaching CSS styling, hover events (`mouseover`), and accessible screen-reader tags.
- **Performance Wall**: The web browser's DOM layout and style-recalculation engine is designed for hundreds of elements, not hundreds of thousands. Rendering a scatterplot with $N = 10,000$ points creates 10,000 DOM nodes, causing memory consumption to surge and dragging rendering frame rates below 10 frames per second (fps). SVG is unsuitable for big-data scatterplots.

#### 2. HTML5 Canvas (2D Context)
HTML5 Canvas provides an immediate-mode bitmap surface. The browser exposes a single DOM element (`<canvas>`) and an imperative JavaScript drawing context (`CanvasRenderingContext2D`):
```javascript
const ctx = canvas.getContext('2d');
ctx.beginPath();
ctx.arc(x, y, radius, 0, 2 * Math.PI);
ctx.fillStyle = '#440154';
ctx.fill();
```
- **Strengths**: Because marks are painted directly into a flat pixel raster buffer without creating DOM nodes, memory usage is completely constant $\mathcal{O}(1)$ regardless of how many points are drawn.
- **Capacity**: Easily handles $N = 50,000$ to $100,000$ points with smooth 60 fps rendering.
- **Limitation**: Immediate-mode rendering discards element identity after painting. Implementing tooltips or selection brushes requires maintaining an auxiliary spatial indexing tree (such as a $k$-d tree or R-tree) in JavaScript memory to map cursor coordinates back to data points.

#### 3. WebGL and GPU Shader Acceleration
WebGL maps rendering directly to the machine's Graphics Processing Unit (GPU) hardware via OpenGL ES shader pipelines.
- **Architecture**: Data points are packed into contiguous GPU ArrayBuffers. A **Vertex Shader** executes coordinate transformations in parallel across thousands of GPU cores in a single clock cycle, while a **Fragment Shader** executes anti-aliased point rendering and color mapping.
- **Capacity**: Renders over **$1,000,000$ interactive data points at a solid 60 fps**, facilitating real-time zooming, continuous 3D rotation, and animated dynamic transitions across multi-million-row bioinformatic single-cell RNA datasets.

### Reactive Dataflow and Coordinated Brushing

In multi-view statistical exploratory systems, multiple plots (e.g. a geographic map, a demographic histogram, and an outcome scatterplot) are rendered on the same screen.

The central paradigm for multi-view interaction is **Coordinated Brushing and Linking**:
1. An analyst selects (brushes) a rectangular sub-region on the scatterplot.
2. A reactive event triggers a filtering operation.
3. The geographic map and histogram instantly highlight the selected subset of records in real time.

To maintain sub-16ms latency across millions of records during active mouse drags, modern systems deploy **Bitmask Indexing (Crossfilter)**:
- Pre-calculates sorted column index arrays.
- Maintains a 32-bit integer bitmask for each row, where bit $k$ records whether the observation satisfies filter $k$.
- Updating a brush requires only bitwise binary operations (`AND`, `OR`) over contiguous integer buffers, delivering instant 60 fps interactivity across massive observational cohorts.
"""

marker = "## Fully worked question 1:"
idx = u3.find(marker)
u3_new = u3[:idx] + u3_addition.strip() + "\n\n" + u3[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md", "w", encoding="utf-8") as f:
    f.write(u3_new)
print("Expanded Unit 3 pass 3!")

# 2. Expand Unit 4
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "r", encoding="utf-8") as f:
    u4 = f.read()

u4_addition = r"""

---

## 4.11 Multiway Data Analysis: Tensor Decompositions (CP and Tucker)

In contemporary statistical applications—including neuroimaging (electroencephalogram and fMRI arrays: subjects $\times$ time points $\times$ electrode channels), multi-omic single-cell genomics, and chemometric multi-way fluorescence spectroscopy—observations are naturally structured as higher-order multidimensional arrays: **Tensors**.

A tensor $\boldsymbol{\mathcal{X}} \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N}$ is an $N$-way array, where $N$ denotes the order (number of modes). Classical 2D matrix factorizations (SVD, PCA) flatten higher-order structures into 2D matrices, destroying multidimensional spatio-temporal correlations. Multiway data analysis generalizes matrix decompositions to tensors via two canonical frameworks: **CANDECOMP/PARAFAC (CP)** and the **Tucker Decomposition**.

### The CANDECOMP/PARAFAC (CP) Decomposition

Introduced by J. Douglas Carroll and Jih-Jie Chang (1970) as CANDECOMP, and independently by Richard Harshman (1970) as PARAFAC (Parallel Factor Analysis), the **CP Decomposition** factorizes an $N$-way tensor into a sum of $R$ rank-one component tensors.

For a 3rd-order tensor $\boldsymbol{\mathcal{X}} \in \mathbb{R}^{I \times J \times K}$:

$$\boldsymbol{\mathcal{X}} \approx \sum_{r=1}^R \lambda_r (\mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r)$$

where:
- $\circ$ denotes the vector outer product: $(\mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r)_{ijk} = a_{ir} b_{jr} c_{kr}$.
- $\mathbf{A} = [\mathbf{a}_1, \dots, \mathbf{a}_R] \in \mathbb{R}^{I \times R}$, $\mathbf{B} = [\mathbf{b}_1, \dots, \mathbf{b}_R] \in \mathbb{R}^{J \times R}$, and $\mathbf{C} = [\mathbf{c}_1, \dots, \mathbf{c}_R] \in \mathbb{R}^{K \times R}$ are the **factor loading matrices** for modes 1, 2, and 3.
- $R$ is the **tensor rank**.

#### The Uniqueness Theorem (Kruskal, 1977):
A foundational mathematical virtue of the CP decomposition is its **essential uniqueness**. In standard 2D matrix SVD, factor matrices can be arbitrarily rotated ($\mathbf{X} = (\mathbf{U} \mathbf{Q}) (\mathbf{Q}^\top \mathbf{V}^\top)$). 
In stark contrast, Joseph Kruskal proved that if the sum of the $k$-ranks (Kruskal ranks) of the factor matrices satisfies:
$$k_{\mathbf{A}} + k_{\mathbf{B}} + k_{\mathbf{C}} \ge 2 R + 2$$
then the CP decomposition is **strictly unique up to trivial permutation and scaling of components**! Zero rotational ambiguity. Components extracted from a CP decomposition represent genuine, unmixed physical signals.

#### Optimization via Alternating Least Squares (ALS):
The CP model is fitted by minimizing the squared Frobenius norm error $\|\boldsymbol{\mathcal{X}} - \sum \lambda_r \mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r\|_F^2$. The algorithm alternates between updating $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{C}$ via regularized least squares using the Khatri–Rao column-wise Kronecker product:
$$\mathbf{A} \leftarrow \mathbf{X}_{(1)} (\mathbf{C} \odot \mathbf{B}) [(\mathbf{C}^\top \mathbf{C}) * (\mathbf{B}^\top \mathbf{B})]^{-1}$$
where $\odot$ denotes the Khatri–Rao product and $*$ denotes the Hadamard element-wise product.

### The Tucker Decomposition (Higher-Order SVD)

Formulated by Ledyard Tucker (1966), the **Tucker Decomposition** is a higher-order form of Principal Component Analysis. It decomposes a tensor into a small **core tensor** multiplied by orthogonal factor matrices along each mode:

$$\boldsymbol{\mathcal{X}} \approx \boldsymbol{\mathcal{G}} \times_1 \mathbf{A} \times_2 \mathbf{B} \times_3 \mathbf{C}$$

where:
- $\boldsymbol{\mathcal{G}} \in \mathbb{R}^{P \times Q \times R}$ is the **core tensor**, capturing interactions between latent factors across the modes.
- $\mathbf{A} \in \mathbb{R}^{I \times P}$, $\mathbf{B} \in \mathbb{R}^{J \times Q}$, and $\mathbf{C} \in \mathbb{R}^{K \times R}$ are orthogonal factor matrices ($\mathbf{A}^\top \mathbf{A} = \mathbf{I}_P$).
- $\times_n$ denotes the mode-$n$ tensor-matrix multiplication.

The **Higher-Order SVD (HOSVD)**, formalized by Lieven De Lathauwer and colleagues (2000), computes factor matrices $\mathbf{A}, \mathbf{B}, \mathbf{C}$ directly as the leading left singular vectors of the mode-$n$ unfolded matrices $\mathbf{X}_{(1)}, \mathbf{X}_{(2)}, \mathbf{X}_{(3)}$, providing optimal multilinear dimensionality reduction for massive scientific datasets.
"""

marker = "## Fully worked question 1:"
idx = u4.find(marker)
u4_new = u4[:idx] + u4_addition.strip() + "\n\n" + u4[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "w", encoding="utf-8") as f:
    f.write(u4_new)
print("Expanded Unit 4 pass 3!")

# 3. Expand Unit 6
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "r", encoding="utf-8") as f:
    u6 = f.read()

u6_addition = r"""

---

## 6.10 Resampling Under Complex Survey Designs: BRR, Fay's Perturbation, and Survey Jackknife

In national probability surveys (such as the Demographic and Health Surveys (DHS) or National Health and Nutrition Examination Survey (NHANES)), sampling is not independent and identically distributed (i.i.d.). Modern survey infrastructure deploys complex multistage designs involving:
- Stratification (dividing the population into homogeneous geographic/demographic strata).
- Clustering (sampling Primary Sampling Units (PSUs), such as enumeration blocks or villages).
- Unequal selection probabilities and non-response calibration weights $w_i$.

Applying standard i.i.d. bootstrap or jackknife routines to complex survey data yields **catastrophically underestimated standard errors**, frequently understating true sampling variability by $50\%$ to $80\%$ due to intra-cluster correlation. To produce design-consistent inferences, survey statisticians deploy specialized survey resampling algorithms.

### Balanced Repeated Replication (BRR) and Hadamard Matrices

For stratified two-PSU-per-stratum designs ($n_h = 2$ PSUs sampled from each stratum $h = 1, \dots, H$), Margaret Gurney and Joseph Daly (1965) at the U.S. Census Bureau developed **Balanced Repeated Replication (BRR)**.

In each stratum, an unbiased estimate of the stratum total is formed by selecting one of the two PSUs and doubling its sampling weight, while assigning zero weight to the other PSU.
- Across $H$ strata, there are $2^H$ possible half-sample combinations. For $H = 50$, $2^{50} \approx 1.1 \times 10^{15}$ combinations, which is computationally intractable.
- Plackett and Burman (1946) and Keith McCarthy (1966) discovered that full enumeration is unnecessary: an orthogonal subset of only $K$ balanced half-samples (where $K$ is the smallest multiple of 4 such that $K \ge H$) achieves the **exact same variance estimate as all $2^H$ combinations**!

#### Orthogonal Balance via Hadamard Matrices:
A **Hadamard Matrix** $\mathbf{H}_K \in \{-1, +1\}^{K \times K}$ satisfies:
$$\mathbf{H}_K^\top \mathbf{H}_K = K \mathbf{I}_K$$
Every pair of distinct columns is strictly orthogonal.

For replication $k \in \{1, \dots, K\}$:
The replicate weights for observation $i$ in PSU $j \in \{1, 2\}$ of stratum $h$ are defined by:
$$w_i^{(k)} = \begin{cases} 2 w_i & \text{if } H_{k, h} = +1 \text{ and } j = 1, \text{ or } H_{k, h} = -1 \text{ and } j = 2 \\ 0 & \text{otherwise} \end{cases}$$
The BRR variance estimator across the $K$ balanced replicates is:

$$v_{BRR}(\hat{\theta}) = \frac{1}{K} \sum_{k=1}^K (\hat{\theta}^{(k)} - \hat{\theta})^2$$

Because the Hadamard columns are orthogonal, all cross-stratum covariance terms cancel out identically, matching the theoretical design variance.

### Fay's Modified BRR Method

A practical limitation of standard BRR is that assigning weight zero ($w_i^{(k)} = 0$) to half the sample can cause model estimation algorithms to crash (e.g. if an entire subgroup or rare categorical factor level is omitted in a half-sample).

Robert Fay (1989) formulated **Fay's Generalized BRR**, which perturbs weights by a factor $f \in (0, 1)$ (typically $f = 0.5$ or $f = 0.7$) rather than zeroing them out entirely:

$$w_i^{(k)} = \begin{cases} (1 + f) w_i & \text{for the selected half-sample} \\ (1 - f) w_i & \text{for the unselected half-sample} \end{cases}$$

The variance estimator is scaled by $1 / f^2$:

$$v_{Fay}(\hat{\theta}) = \frac{1}{K f^2} \sum_{k=1}^K (\hat{\theta}^{(k)} - \hat{\theta})^2$$

Fay's method preserves all observations in every replicate sample, guaranteeing numerical stability for complex non-linear models while retaining exact design consistency.
"""

marker = "## Fully worked question 1:"
idx = u6.find(marker)
u6_new = u6[:idx] + u6_addition.strip() + "\n\n" + u6[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "w", encoding="utf-8") as f:
    f.write(u6_new)
print("Expanded Unit 6 pass 3!")

# 4. Expand Unit 7
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "r", encoding="utf-8") as f:
    u7 = f.read()

u7_addition = r"""

---

## 7.10 Global Optimization: Simulated Annealing and Trust-Region Methods in Statistics

In statistical estimation landscapes with complex multimodality, rugged surfaces, and non-differentiable thresholds—such as mixture models with unknown component counts, phylogenetics, changepoint detection, and non-linear pharmacokinetic models—local gradient-based methods (Newton–Raphson, BFGS) inevitably terminate in poor local optima.

To locate the true global extremum, computational statisticians deploy **Global Optimization Heuristics** and **Trust-Region Methods**.

### Simulated Annealing (Kirkpatrick, Gelatt, and Vecchi, 1983)

**Simulated Annealing** adapts the physical thermodynamics of metal metallurgy to numerical optimization. In physical metallurgy, slow controlled cooling (annealing) allows atoms to escape high-energy crystalline defects and settle into the global minimum energy state.

Let $E(\boldsymbol{\theta}) = f(\boldsymbol{\theta})$ denote the objective function (energy).
At iteration $t$ with current state $\boldsymbol{\theta}_t$ and temperature parameter $T_t > 0$:
1. Generate a candidate proposal $\boldsymbol{\theta}^* = \boldsymbol{\theta}_t + \boldsymbol{\Delta}$ from a proposal distribution.
2. Compute the energy difference: $\Delta E = f(\boldsymbol{\theta}^*) - f(\boldsymbol{\theta}_t)$.
3. Evaluate the **Metropolis Acceptance Criterion**:
   - If $\Delta E < 0$ (the proposed state improves the objective), **ACCEPT unconditionally**: $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}^*$.
   - If $\Delta E \ge 0$ (the proposed state worsens the objective), **ACCEPT probabilistically** with acceptance probability:
     $$\mathbb{P}(\text{Accept uphill step}) = \exp\left( -\frac{\Delta E}{T_t} \right)$$
   Draw $U \sim \text{Uniform}(0, 1)$. If $U \le \exp(-\Delta E / T_t)$, accept; otherwise reject.

#### The Crucial Role of Temperature and Cooling Schedules:
- **At High Temperatures ($T \gg 1$)**: $\exp(-\Delta E / T) \approx 1$. The algorithm accepts virtually all uphill steps, exploring the global space freely and escaping local traps.
- **At Low Temperatures ($T \to 0$)**: $\exp(-\Delta E / T) \to 0$. The algorithm accepts only downhill steps, converging greedily to the nearest local minimum.

#### The Hajek Convergence Theorem:
Bruce Hajek (1988) proved that Simulated Annealing is guaranteed to converge to the **global minimum with probability 1** if the cooling schedule satisfies the logarithmic decay condition:

$$T_t = \frac{c}{\ln(1 + t)}$$

where $c$ is a constant greater than the maximum depth of any local energy barrier. While logarithmic cooling is slow, modern practical schedules deploy geometric cooling ($T_{t+1} = \alpha T_t$ with $\alpha \in [0.85, 0.98]$) to find near-optimal parameters across rugged likelihood landscapes.

### Trust-Region Methods and the Powell Dogleg Step

In unconstrained optimization, line-search methods first choose a direction $\mathbf{p}_k$ and then search for an appropriate step size $\alpha_k$.
In contrast, **Trust-Region Methods** first determine a maximum step radius $\Delta_k > 0$, construct a local quadratic model:

$$m_k(\mathbf{p}) = f(\boldsymbol{\theta}_k) + \nabla f(\boldsymbol{\theta}_k)^\top \mathbf{p} + \frac{1}{2} \mathbf{p}^\top \mathbf{B}_k \mathbf{p}$$

and solve the constrained sub-problem strictly inside the "trust region":

$$\min_{\mathbf{p}} m_k(\mathbf{p}) \quad \text{subject to } \|\mathbf{p}\|_2 \le \Delta_k$$

#### The Powell Dogleg Step:
To solve the trust-region sub-problem efficiently without computing exact constrained quadratics, M. J. D. Powell formulated the **Dogleg Step**.
The dogleg trajectory connects three points:
1. The origin $\mathbf{p} = \mathbf{0}$.
2. The **Cauchy Point** $\mathbf{p}_C$: The unconstrained minimum of the quadratic model along the steepest descent direction:
   $$\mathbf{p}_C = -\frac{\|\mathbf{g}_k\|_2^2}{\mathbf{g}_k^\top \mathbf{B}_k \mathbf{g}_k} \mathbf{g}_k$$
3. The **Newton Point** $\mathbf{p}_N = -\mathbf{B}_k^{-1} \mathbf{g}_k$.

The dogleg algorithm moves along the piecewise linear path from $\mathbf{0} \to \mathbf{p}_C \to \mathbf{p}_N$, intersecting the spherical trust-region boundary $\|\mathbf{p}\|_2 = \Delta_k$.
- If the quadratic model accurately predicts the true function decrease ($\rho_k = \frac{f(\boldsymbol{\theta}_k) - f(\boldsymbol{\theta}_k + \mathbf{p}_k)}{m_k(\mathbf{0}) - m_k(\mathbf{p}_k)} \approx 1$), the trust region is expanded: $\Delta_{k+1} = 2 \Delta_k$.
- If the model is inaccurate ($\rho_k < 0.25$), the step is rejected and the trust region is shrunk: $\Delta_{k+1} = 0.5 \Delta_k$.

Trust-region methods provide unconditional global convergence guarantees even for highly non-convex, ill-conditioned statistical likelihood surfaces.
"""

marker = "## Fully worked question 1:"
idx = u7.find(marker)
u7_new = u7[:idx] + u7_addition.strip() + "\n\n" + u7[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "w", encoding="utf-8") as f:
    f.write(u7_new)
print("Expanded Unit 7 pass 3!")

# 5. Expand Unit 8
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "r", encoding="utf-8") as f:
    u8 = f.read()

u8_addition = r"""

---

## 8.10 Automated Testing, Continuous Integration, and Invariance Assertions in Statistical Software

A critical requirement of scientific software engineering is ensuring that computational estimators produce mathematically correct, numerically stable outputs across software updates and operating system platforms. General-purpose software engineering emphasizes unit tests checking trivial string outputs or return codes; statistical software engineering requires **Invariance Assertions and Property-Based Testing**.

### Property-Based Testing and Mathematical Invariance Assertions

In statistical computing, individual point assertions (e.g. `assert mean([1, 2, 3]) == 2.0`) test only trivial edge cases. To rigorously verify statistical estimation routines, developers deploy **Property-Based Testing** (`Hypothesis` in Python, `hedgehog` in R), generating hundreds of randomized input vectors and asserting invariant mathematical properties:

#### Canonical Statistical Invariant Properties:
1. **Idempotence of Projection Matrices**:
   For any linear regression projection matrix $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top$:
   $$\mathbf{H}^2 = \mathbf{H} \quad \text{and} \quad (\mathbf{I} - \mathbf{H})^2 = \mathbf{I} - \mathbf{H}$$
2. **Orthogonality of Residuals**:
   The residual vector $\mathbf{e} = \mathbf{y} - \mathbf{X} \hat{\boldsymbol{\beta}}$ must be strictly orthogonal to the column space of $\mathbf{X}$:
   $$\|\mathbf{X}^\top \mathbf{e}\|_\infty < \epsilon \quad (\text{e.g. } \epsilon = 10^{-12})$$
3. **Translation Equivariance of Sample Variance**:
   For any constant scalar $c \in \mathbb{R}$:
   $$\text{Var}(\mathbf{x} + c \mathbf{1}) \equiv \text{Var}(\mathbf{x})$$
4. **Positive Semi-Definiteness of Covariance Matrices**:
   Every estimated covariance matrix $\hat{\boldsymbol{\Sigma}}$ must have all non-negative eigenvalues:
   $$\min(\text{eig}(\hat{\boldsymbol{\Sigma}})) \ge -\epsilon_{mach}$$

### Continuous Integration (CI) and Multi-Platform Matrix Testing

Statistical algorithms rely heavily on compiled low-level BLAS and LAPACK libraries (e.g. OpenBLAS, Intel MKL, Apple Accelerate). Minor differences in processor instruction sets (x86-64 AVX-512 vs ARM64 NEON) and compiler optimization flags (`-O3`, `-ffast-math`) can cause non-associative floating-point operations to round differently:
$$(a + b) + c \ne a + (b + c)$$

#### Robust Continuous Integration Practices:
- **Fuzzy Tolerance Equality**: In unit tests, never assert exact bitwise equality `assert a == b`. Always assert absolute and relative tolerances:
  ```python
  import numpy.testing as npt
  npt.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)
  ```
- **Matrix Build Workflows**: In GitHub Actions CI pipelines, statistical libraries must run test matrices spanning:
  - OS: Ubuntu Linux, macOS (Apple Silicon ARM64), Windows.
  - Python / R Versions: Current stable release and two preceding minor releases.
  - Linear Algebra Backends: Testing under OpenBLAS and reference LAPACK to catch architecture-dependent sign-flip variations in SVD singular vectors.

By embedding mathematical invariance assertions into automated continuous integration pipelines, statistical software developers ensure that empirical research built atop their libraries remains rigorous, trustworthy, and permanently reproducible.
"""

marker = "## Fully worked question 1:"
idx = u8.find(marker)
u8_new = u8[:idx] + u8_addition.strip() + "\n\n" + u8[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "w", encoding="utf-8") as f:
    f.write(u8_new)
print("Expanded Unit 8 pass 3!")
