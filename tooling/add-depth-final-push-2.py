#!/usr/bin/env python3
"""
Adds depth to Units 5, 6, and 8 to comfortably exceed 50,500 substantive prose words.
Uses raw strings and clean LaTeX math to ensure zero KaTeX errors.
"""
import sys

def expand_unit_8():
    path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = r"""

## 8.13 Reproducible Computational Workflow Orchestration: Directed Acyclic Graphs, Snakemake, and the R targets Framework

Modern empirical statistical investigations rarely consist of a single self-contained script. A realistic workflow encompasses ingestion of multi-gigabyte raw files, messy data wrangling, categorical factor coding, complex model estimation, cross-validation tuning loops, diagnostic sensitivity analyses, and publication table compilation. In unstructured research environments, analysts execute numbered scripts sequentially (for example, `01_clean.R`, `02_impute.py`, `03_fit.R`, `04_plots.py`). This ad-hoc convention is notoriously fragile. If an analyst modifies an imputation hyperparameter in script 2, they must manually remember which downstream scripts require re-execution. If they accidentally skip script 3 and run script 4, reported tables and visualization figures become mathematically desynchronized, leading to silent, irreproducible reporting errors.

### The Directed Acyclic Graph (DAG) Execution Model

Formal computational workflow managers eliminate this vulnerability by abstracting the research pipeline as a **Directed Acyclic Graph (DAG)** $\mathcal{G} = (\mathcal{V}, \mathcal{E})$.
1. **Vertices (Nodes) $\mathcal{V}$**: Represent discrete pipeline targets—such as raw datasets, transformed feature matrices, fitted model objects, diagnostic summary tables, or rendered markdown chapters.
2. **Directed Edges $\mathcal{E}$**: Represent strict data flow dependencies ($u \to v$ signifies that target $v$ requires target $u$ as an input argument).
3. **Acyclicity**: The graph contains no directed loops ($\nexists v_1 \to v_2 \to \dots \to v_1$), ensuring that execution order can be determined unambiguously via **topological sorting**.

Workflow engines calculate cryptographic hashes (such as SHA-256) of three critical components for every node in the graph:
- The byte content of upstream input data artifacts.
- The abstract syntax tree (AST) or byte code of the user-defined transformation function.
- Declared environment dependencies and execution arguments.

When the workflow is triggered, the engine evaluates the hash of each node against its stored cache. If neither the input data nor the governing function has changed, the engine **skips computation entirely**, retrieving the cached result from disk in microseconds. If an upstream node is modified, the engine invalidates only that node and its downstream topological descendants, executing the minimum necessary set of computations.

### The R `targets` Architecture

In the R ecosystem, the `targets` package (the modern successor to `drake`) implements purely functional, declarative pipeline orchestration. Unlike Makefiles that track filesystem file modification timestamps, `targets` inspects R functions directly:

```r
# _targets.R
library(targets)
library(tarchetypes)

# Source bespoke statistical modeling functions
source("R/functions.R")

# Define declarative workflow pipeline
list(
  tar_target(
    raw_file,
    "data/clinical_trials_raw.parquet",
    format = "file"
  ),
  tar_target(
    cleaned_data,
    wrangle_and_contrast_encode(raw_file)
  ),
  tar_target(
    model_fits,
    fit_mixed_effects_reml(cleaned_data)
  ),
  tar_target(
    diagnostic_report,
    render_quarto_diagnostics(cleaned_data, model_fits),
    format = "file"
  )
)
```

The `targets` architecture offers distinct mathematical guarantees for statistical computing:
- **Dynamic Branching**: If a simulation study tests $1,000$ parameter combinations, `tar_map()` or `pattern = map(...)` splits the computation into $1,000$ independent branches, automatically distributing them across available multi-core worker threads or high-performance computing (HPC) Slurm clusters via `clustermq` or `future`.
- **Target Invariance**: If the analyst alters the Quarto reporting layout without altering `wrangle_and_contrast_encode()` or `fit_mixed_effects_reml()`, running `tar_make()` executes only the rendering step, saving hours of model re-estimation time.
- **Visual Graph Auditing**: The function `tar_visnetwork()` generates an interactive HTML graph displaying nodes as colored circles: green for up-to-date targets, blue for outdated targets requiring rebuild, and red for errored nodes.

### Python Workflow Orchestration: `Snakemake` and `Prefect`

In the Python data science and bioinformatics communities, `Snakemake` provides a domain-specific workflow language built directly on Python grammar. Snakemake rules define expected input files, generated output files, container specifications, and execution scripts:

```python
# Snakefile
rule clean_data:
    input:
        raw="data/measurements_{sample}.csv"
    output:
        processed="data/clean_{sample}.parquet"
    threads: 4
    shell:
        "python scripts/preprocess.py --input {input.raw} --output {output.processed} --threads {threads}"

rule fit_models:
    input:
        processed=expand("data/clean_{sample}.parquet", sample=["A", "B", "C"])
    output:
        summary="reports/model_summary.json"
    script:
        "scripts/fit_statistical_models.py"
```

Snakemake integrates natively with container technologies (Docker, Singularity, Apptainer) and package managers (Conda), allowing each rule in the DAG to execute inside a completely isolated container image. This guarantees that software version differences between local development laptops and remote compute clusters never jeopardize numerical reproducibility.


## 8.14 Statistical Model Serialization, Graph Representation, and Cross-Platform Production Serving with ONNX

Once a complex statistical model is estimated, it must be persisted for subsequent inference, distributed scoring, or long-term archival. In computational statistics, serialization is the process of translating in-memory object graphs (parameters, covariance matrices, decision trees, design matrix column metadata) into contiguous byte streams that can be stored on disk or transmitted over networks.

### Security Vulnerabilities and Brittleness of Python `pickle` and R `saveRDS`

Historically, Python practitioners relied on `pickle` (or its multi-core compression wrapper `joblib`), while R users relied on `save()` and `saveRDS()`. Both formats exhibit critical architectural limitations that render them unsuitable for secure, production-grade statistical software:

1. **Arbitrary Code Execution Vulnerabilities**: Python's `pickle` format is not a passive data structure; it is an interpreted stack language. The pickle byte stream can invoke arbitrary Python callables during unpickling via the `__reduce__` method. Loading a serialized model file from an untrusted third party allows malicious actors to execute arbitrary operating system commands, opening severe security backdoors.
2. **Version Fragility and Bit-Rot**: Serialized `pickle` and `.rds` files store pointers to internal module namespaces, class definitions, and compiled C extensions. If the scikit-learn or statsmodels package is upgraded by even a minor patch version, unpickling old files frequently fails with `ModuleNotFoundError`, `AttributeError`, or altered parameter mappings.
3. **Language Silos**: An object saved via R's `saveRDS()` cannot be natively deserialized inside Python without spinning up an embedded R interpreter process via `rpy2`. Conversely, a Python `joblib` model cannot be natively evaluated within an R process or embedded C++ microservice.

### The Open Neural Network Exchange (ONNX) Architecture

To resolve cross-language incompatibilities and security vulnerabilities, the scientific computing ecosystem developed **ONNX (Open Neural Network Exchange)**. ONNX defines a standardized, language-agnostic computational graph representation serialized via Google Protocol Buffers (`.proto`).

In the ONNX framework:
- Models are represented as a strictly defined Directed Acyclic Graph where nodes are standardized mathematical operators (such as `Gemm` for matrix multiplication, `Relu`, `Conv`, `Softmax`, or `TreeEnsembleRegressor`).
- All tensors possess explicit, static or symbolic data types and dimension shapes (such as `[batch_size, num_features]`).
- The serialization format is strictly passive data: no executable bytecode or arbitrary language functions are permitted, eliminating deserialization attack vectors completely.

Statistical models trained in scikit-learn, LightGBM, or statsmodels can be exported directly into ONNX computational graphs using converter libraries such as `skl2onnx`:

```python
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnxruntime as rt
import numpy as np

# Define input feature schema: batch size variable, 10 continuous predictors
initial_type = [("float_input", FloatTensorType([None, 10]))]

# Convert fitted scikit-learn pipeline into an ONNX graph representation
onnx_model = convert_sklearn(fitted_pipeline, initial_types=initial_type)

# Save passive protocol buffer bytes to disk
with open("statistical_pipeline.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

# High-performance, cross-language inference engine
session = rt.InferenceSession("statistical_pipeline.onnx")
input_name = session.get_inputs()[0].name
label_name = session.get_outputs()[0].name

# Score new test data in microseconds using compiled C++ SIMD kernels
predictions = session.run([label_name], {input_name: X_test.astype(np.float32)})[0]
```

### Advantages for Cross-Platform Deployment

The deployment advantages of the ONNX standard for computational statistics include:
- **Zero Language Runtime Dependency**: The resulting `.onnx` file can be loaded directly inside embedded C++, Rust, Go, or Java microservices using `onnxruntime` libraries. There is no requirement to install Python, R, numpy, or scikit-learn on production edge devices or low-latency prediction servers.
- **Hardware Acceleration**: `onnxruntime` dynamically targets hardware execution providers (CUDA, TensorRT, Intel OpenVINO, Apple CoreML, ARM DirectML), transparently dispatching statistical vector operations to GPUs or neural processing units without altering model definitions.
- **Strict Backward Compatibility**: An ONNX model serialized today retains guaranteed forward compatibility across future operating system and engine upgrades.
"""

    split_target = "## Fully worked question 1:"
    if split_target not in content:
        print("Error: split target not found in Unit 8")
        sys.exit(1)

    parts = content.split(split_target)
    new_content = parts[0] + addition + "\n" + split_target + parts[1]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Unit 8 expanded successfully!")

def expand_unit_6():
    path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = r"""

## 6.13 Nonlinear Least Squares and Bound-Constrained Optimization: The Levenberg–Marquardt and Trust-Region Reflective Algorithms

While linear regression admits a closed-form analytical estimator $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$, many physical, pharmacokinetic, and biochemical systems are governed by inherently nonlinear mathematical models. In nonlinear regression, the relationship between response $y_i$ and predictor vector $\mathbf{x}_i$ is parameterized by a smooth nonlinear function $f(\mathbf{x}_i, \boldsymbol{\beta})$:

$$y_i = f(\mathbf{x}_i, \boldsymbol{\beta}) + \varepsilon_i, \quad \varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$$

The nonlinear least squares objective seeks the parameter vector $\hat{\boldsymbol{\beta}}$ that minimizes the residual sum of squares:

$$S(\boldsymbol{\beta}) = \frac{1}{2} \sum_{i=1}^n [y_i - f(\mathbf{x}_i, \boldsymbol{\beta})]^2 = \frac{1}{2} \|\mathbf{r}(\boldsymbol{\beta})\|_2^2$$

where $\mathbf{r}(\boldsymbol{\beta}) \in \mathbb{R}^n$ is the residual vector with elements $r_i(\boldsymbol{\beta}) = y_i - f(\mathbf{x}_i, \boldsymbol{\beta})$.

### The Jacobian Matrix and the Gauss–Newton Approximation

Let $\mathbf{J}(\boldsymbol{\beta}) \in \mathbb{R}^{n \times p}$ denote the **Jacobian matrix** of the residual vector with respect to $\boldsymbol{\beta}$:

$$J_{ij}(\boldsymbol{\beta}) = \frac{\partial r_i(\boldsymbol{\beta})}{\partial \beta_j} = -\frac{\partial f(\mathbf{x}_i, \boldsymbol{\beta})}{\partial \beta_j}$$

The gradient of the objective $S(\boldsymbol{\beta})$ is expressed neatly in terms of the Jacobian:

$$\nabla S(\boldsymbol{\beta}) = \mathbf{J}(\boldsymbol{\beta})^T \mathbf{r}(\boldsymbol{\beta})$$

The exact Hessian matrix $\nabla^2 S(\boldsymbol{\beta})$ decomposes into two distinct terms:

$$\nabla^2 S(\boldsymbol{\beta}) = \mathbf{J}(\boldsymbol{\beta})^T \mathbf{J}(\boldsymbol{\beta}) + \sum_{i=1}^n r_i(\boldsymbol{\beta}) \nabla^2 r_i(\boldsymbol{\beta})$$

In the vicinity of the optimal parameter solution, the individual residuals $r_i(\boldsymbol{\beta})$ are typically small, zero-mean stochastic errors. Under the **Gauss–Newton approximation**, the second-order second-derivative summation term is neglected entirely, yielding the celebrated approximation:

$$\nabla^2 S(\boldsymbol{\beta}) \approx \mathbf{J}(\boldsymbol{\beta})^T \mathbf{J}(\boldsymbol{\beta})$$

This approximation eliminates the burdensome necessity of computing $n$ separate $p \times p$ second-derivative Hessian matrices, requiring only first-order Jacobian evaluations.

### The Levenberg–Marquardt Damped Regularization

When the matrix $\mathbf{J}^T \mathbf{J}$ is rank-deficient or ill-conditioned, standard Gauss–Newton updates $\Delta \boldsymbol{\beta} = -(\mathbf{J}^T \mathbf{J})^{-1} \mathbf{J}^T \mathbf{r}$ can produce wild, divergent steps. The **Levenberg–Marquardt (LM)** algorithm introduces an adaptive damping parameter $\lambda \ge 0$ into the normal equations:

$$[\mathbf{J}(\boldsymbol{\beta}_k)^T \mathbf{J}(\boldsymbol{\beta}_k) + \lambda_k \mathbf{D}_k] \Delta \boldsymbol{\beta}_k = -\mathbf{J}(\boldsymbol{\beta}_k)^T \mathbf{r}(\boldsymbol{\beta}_k)$$

where $\mathbf{D}_k$ is commonly chosen as the identity matrix $\mathbf{I}_p$ (Levenberg) or the diagonal scaling matrix $\text{diag}(\mathbf{J}^T \mathbf{J})$ (Marquardt), which provides scale invariance across parameters measured in disparate physical units.

The damping parameter $\lambda_k$ dynamically interpolates between two classical optimization regimes:
- **Small $\lambda_k \to 0$**: The update approaches the pure Gauss–Newton step, achieving quadratic convergence near the local optimum.
- **Large $\lambda_k \to \infty$**: The update approaches an infinitesimal gradient descent step $\Delta \boldsymbol{\beta}_k \approx -\frac{1}{\lambda_k} \mathbf{D}_k^{-1} \nabla S(\boldsymbol{\beta}_k)$, guaranteeing monotonic descent when far from the solution.

At each iteration, the algorithm evaluates the **gain ratio** $\rho_k$:

$$\rho_k = \frac{S(\boldsymbol{\beta}_k) - S(\boldsymbol{\beta}_k + \Delta \boldsymbol{\beta}_k)}{L(0) - L(\Delta \boldsymbol{\beta}_k)}$$

where $L(\Delta \boldsymbol{\beta}) = \frac{1}{2} \|\mathbf{r}(\boldsymbol{\beta}_k) + \mathbf{J}(\boldsymbol{\beta}_k) \Delta \boldsymbol{\beta}\|_2^2$ is the predicted reduction from the linearized model. If $\rho_k > 0$, the proposed step reduces the actual residual sum of squares: the step is accepted ($\boldsymbol{\beta}_{k+1} = \boldsymbol{\beta}_k + \Delta \boldsymbol{\beta}_k$) and $\lambda_{k+1}$ is decreased. Conversely, if $\rho_k \le 0$, the step is rejected, $\lambda_k$ is multiplied by an expansion factor (e.g., $10$), and the linear system is solved anew.

### Trust-Region Reflective (TRF) Algorithm for Bound Constraints

In statistical applications, parameters often possess strict physical or biological bounds—such as positive reaction rates ($k > 0$), probabilities bounded in $[0, 1]$, or variances ($\sigma^2 \ge 0$). Standard Levenberg–Marquardt optimization cannot enforce parameter box constraints $\mathbf{l} \le \boldsymbol{\beta} \le \mathbf{u}$.

The **Trust-Region Reflective (TRF)** algorithm (implemented in `scipy.optimize.least_squares` and R's `minpack.lm`) resolves bound constraints through a geometric reflection mechanism:
1. At each step, a quadratic model of the objective is minimized within an ellipsoidal trust region scaled by the distances to active parameter boundaries.
2. If the unconstrained minimizer of the trust region violates a parameter boundary $\beta_j < l_j$ or $\beta_j > u_j$, the optimization search path is mathematically **reflected** off the constraint boundary wall back into the strictly feasible interior parameter space.
3. This reflective trajectory mapping ensures that boundary conditions are strictly respected while maintaining fast superlinear convergence rates without requiring external barrier or penalty hyperparameter tuning.
"""

    split_target = "## Fully worked question 1:"
    if split_target not in content:
        print("Error: split target not found in Unit 6")
        sys.exit(1)

    parts = content.split(split_target)
    new_content = parts[0] + addition + "\n" + split_target + parts[1]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Unit 6 expanded successfully!")

def expand_unit_5():
    path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = r"""

## 5.13 Asymptotic Trio Invariance and Finite-Sample Performance: Likelihood Ratio, Wald, and Rao Score Tests

Statistical hypothesis testing in parametric models relies heavily on the "Holy Trinity" of classical maximum likelihood inference: the **Likelihood Ratio (LR)** test, the **Wald** test, and the **Rao Score (Lagrange Multiplier)** test. Under the null hypothesis $H_0: \boldsymbol{\theta} = \boldsymbol{\theta}_0$ against $H_1: \boldsymbol{\theta} \ne \boldsymbol{\theta}_0$, where $\boldsymbol{\theta} \in \mathbb{R}^p$, all three test statistics converge asymptotically to the same central chi-square distribution with $p$ degrees of freedom:

$$\Lambda_{LR}, \, W, \, S \xrightarrow{d} \chi_p^2 \quad \text{as } n \to \infty$$

However, in finite computational samples, their numerical behaviors, geometric interpretations, computational complexities, and parameter transformation invariance properties diverge dramatically.

### Mathematical Formulations and Geometric Mechanics

Let $\ell(\boldsymbol{\theta})$ denote the sample log-likelihood function, $\hat{\boldsymbol{\theta}}$ denote the unrestricted maximum likelihood estimator, $U(\boldsymbol{\theta}) = \nabla \ell(\boldsymbol{\theta})$ denote the score vector, and $\mathcal{I}(\boldsymbol{\theta}) = -\mathbb{E}[\nabla^2 \ell(\boldsymbol{\theta})]$ denote the Fisher Information matrix (with $\mathcal{J}(\boldsymbol{\theta}) = -\nabla^2 \ell(\boldsymbol{\theta})$ representing the observed information matrix).

1. **The Likelihood Ratio Test**: Evaluates the vertical drop in the log-likelihood curve between the peak $\hat{\boldsymbol{\theta}}$ and the null parameter point $\boldsymbol{\theta}_0$:
   $$\Lambda_{LR} = 2 \left[ \ell(\hat{\boldsymbol{\theta}}) - \ell(\boldsymbol{\theta}_0) \right]$$
2. **The Wald Test**: Evaluates the horizontal distance between $\hat{\boldsymbol{\theta}}$ and $\boldsymbol{\theta}_0$, weighted by the local curvature at the unrestricted maximum:
   $$W = (\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0)^T \mathcal{I}(\hat{\boldsymbol{\theta}}) (\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0)$$
3. **The Rao Score (Lagrange Multiplier) Test**: Evaluates the gradient (slope) of the log-likelihood function at the restricted null parameter $\boldsymbol{\theta}_0$, normalized by information at $\boldsymbol{\theta}_0$:
   $$S = U(\boldsymbol{\theta}_0)^T \mathcal{I}(\boldsymbol{\theta}_0)^{-1} U(\boldsymbol{\theta}_0)$$

### Parameter Transformation Invariance

A profound mathematical distinction between these three estimators lies in their behavior under smooth parameter transformations. Suppose we reparameterize the statistical model via an invertible, differentiable bijection $\boldsymbol{\psi} = g(\boldsymbol{\theta})$.

- **Likelihood Ratio Invariance**: Because the likelihood is a scalar function representing the probability density of observed data, the maximum log-likelihood value is invariant under reparameterization: $\max_{\boldsymbol{\psi}} \ell^*(\boldsymbol{\psi}) = \max_{\boldsymbol{\theta}} \ell(\boldsymbol{\theta})$. Consequently:
  $$\Lambda_{LR}^* = 2 [\ell^*(\hat{\boldsymbol{\psi}}) - \ell^*(\boldsymbol{\psi}_0)] = 2 [\ell(\hat{\boldsymbol{\theta}}) - \ell(\boldsymbol{\theta}_0)] = \Lambda_{LR}$$
  The Likelihood Ratio statistic is **strictly invariant** to any nonlinear reparameterization.
- **Rao Score Invariance**: By the chain rule of multivariable calculus, the gradient transforms via the Jacobian matrix: $U_\psi(\boldsymbol{\psi}) = (\mathbf{J}^{-1})^T U_\theta(\boldsymbol{\theta})$, while the information matrix transforms via $\mathcal{I}_\psi(\boldsymbol{\psi}) = (\mathbf{J}^{-1})^T \mathcal{I}_\theta(\boldsymbol{\theta}) \mathbf{J}^{-1}$. When computing the quadratic form $S = U^T \mathcal{I}^{-1} U$, the Jacobian transformations cancel algebraically:
  $$S^* = U_\psi^T \mathcal{I}_\psi^{-1} U_\psi = U_\theta^T \mathbf{J}^{-1} (\mathbf{J} \mathcal{I}_\theta^{-1} \mathbf{J}^T) (\mathbf{J}^{-1})^T U_\theta = U_\theta^T \mathcal{I}_\theta^{-1} U_\theta = S$$
  The Rao Score test is likewise **strictly invariant** under smooth parameter transformations.
- **Wald Test Non-Invariance**: The Wald statistic measures Euclidean distances in the parameter space. Because nonlinear mappings distort Euclidean distances, the Wald statistic is **not invariant**:
  $$W^* \ne W$$
  In logistic regression, this creates the well-known **Hauck–Donner effect**: when an explanatory variable is an extremely strong predictor (so that true effect $|\beta| \to \infty$), the estimated standard error $\text{SE}(\hat{\beta}) = \mathcal{I}(\hat{\beta})^{-1/2}$ diverges faster than the point estimate $\hat{\beta}$ grows, causing the Wald statistic $W = (\hat{\beta}/\text{SE}(\hat{\beta}))^2$ to paradoxically plunge toward zero. An analyst relying naively on Wald p-values would conclude that an overwhelmingly significant predictor has zero statistical significance, whereas the Likelihood Ratio test remains monotonic and correctly detects extreme significance.

### Computational Efficiency Profiles

The computational trade-offs among the three tests govern their application across large-scale data science pipelines:

| Test | Model Estimations Required | Curvature Evaluation | Primary Computational Use Case |
| :--- | :--- | :--- | :--- |
| **Likelihood Ratio** | Both Null ($H_0$) and Unrestricted ($H_1$) | Not required directly (only scalar $\ell$) | Definitive model selection, nested hypothesis testing |
| **Wald** | Unrestricted ($H_1$) only | Required at $\hat{\boldsymbol{\theta}}$ | Standard regression summary tables (`summary(lm)`, `summary(glm)`) |
| **Rao Score** | Null ($H_0$) only | Required at $\boldsymbol{\theta}_0$ | Genome-wide association scans (GWAS), high-throughput feature screening |

In modern computational genetics, researchers test millions of single nucleotide polymorphisms (SNPs) against a disease phenotype. Fitting an unrestricted generalized linear model with iterative Fisher scoring for each of $10,000,000$ genetic variants requires hours or days of compute time. Because the **Rao Score test requires fitting the model only once under the null hypothesis** (adjusting for baseline covariates like age, sex, and ancestry principal components), all $10,000,000$ candidate SNPs can be scored in seconds via vector-matrix dot products against the precomputed null residual vector:

$$S_k = \frac{(\mathbf{x}_k^T \mathbf{r}_0)^2}{\mathbf{x}_k^T \mathbf{W}_0 \mathbf{x}_k}$$

This makes the Rao Score test the premier computational workhorse of high-throughput statistical scanning.
"""

    split_target = "## Fully worked question 1:"
    if split_target not in content:
        print("Error: split target not found in Unit 5")
        sys.exit(1)

    parts = content.split(split_target)
    new_content = parts[0] + addition + "\n" + split_target + parts[1]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Unit 5 expanded successfully!")

if __name__ == "__main__":
    expand_unit_8()
    expand_unit_6()
    expand_unit_5()
