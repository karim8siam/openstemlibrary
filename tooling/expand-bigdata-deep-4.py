#!/usr/bin/env python3
"""
Deep Expansion Pass 4 for Big Data Methods for Statistics (Book 16) - Units 5 to 8.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 4 applied.")

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5_deep4 = r"""
## 5.9 Accelerated First-Order Methods: Nesterov Momentum and Continuous ODE Dynamics

In Section 5.3, we examined Polyak momentum. Yurii Nesterov (1983) revolutionized convex optimization by introducing **Nesterov Accelerated Gradient (NAG)**, which achieves the theoretical lower bound on first-order convergence rates.

### 1. Nesterov's Accelerated Algorithm
While Polyak momentum computes the gradient at the current position $\mathbf{w}_t$ and then adds momentum, Nesterov computes the gradient **at the projected future position** $\mathbf{w}_t + \beta_t (\mathbf{w}_t - \mathbf{w}_{t-1})$:

$$\mathbf{y}_t = \mathbf{w}_t + \frac{t - 1}{t + 2} (\mathbf{w}_t - \mathbf{w}_{t-1})$$
$$\mathbf{w}_{t+1} = \mathbf{y}_t - \eta \nabla F(\mathbf{y}_t)$$

*Theorem (Nesterov's Optimal Complexity Bound)*: For any $L$-smooth convex objective function, Nesterov acceleration achieves an objective error decay of:
$$F(\mathbf{w}_t) - F(\mathbf{w}^*) \le \frac{2 L \|\mathbf{w}_0 - \mathbf{w}^*\|_2^2}{(t + 1)^2} = O\left( \frac{1}{t^2} \right)$$
Whereas standard gradient descent requires $t = O(1/\epsilon)$ iterations to reach precision $\epsilon$, Nesterov acceleration reaches the exact same precision in $t = O(1/\sqrt{\epsilon})$ iterations. Arkadi Nemirovski proved that $O(1/t^2)$ is the absolute theoretical physical limit for any first-order black-box optimization algorithm.

### 2. The Continuous-Time ODE Limit
Weijie Su, Stephen Boyd, and Emmanuel Candès (2016) unlocked the geometric intuition behind Nesterov acceleration by taking the continuous-time limit as step size $\eta \to 0$.

*Theorem (Su, Boyd, Candès 2016)*: As $\eta \to 0$, the discrete Nesterov sequence converges weakly to the second-order ordinary differential equation (ODE):

$$\ddot{\mathbf{X}}(t) + \frac{3}{t} \dot{\mathbf{X}}(t) + \nabla F(\mathbf{X}(t)) = \mathbf{0}$$

This ODE represents the physical mechanics of a particle sliding over a potential energy surface $F(\mathbf{x})$ subject to an **asymptotically vanishing viscous friction coefficient** $\gamma(t) = 3/t$. In the early iterations when $t$ is small, the high damping coefficient $\gamma(t) = 3/t$ rapidly absorbs kinetic energy, preventing violent oscillations. As $t \to \infty$, friction drops to zero, allowing the particle to accelerate into the minimum at the optimal $O(1/t^2)$ rate.

## 5.10 Second-Order Stochastic Optimization: Sub-Sampled Newton and Newton-Sketch

While first-order SGD scales to massive data, its convergence rate degrades when the objective is ill-conditioned (large condition number $\kappa = \lambda_{\max}(\nabla^2 F) / \lambda_{\min}(\nabla^2 F) \gg 10^6$). Classical Newton-Raphson optimization is affine-invariant and converges quadratically ($O(\epsilon^{2^k})$):
$$\mathbf{w}_{t+1} = \mathbf{w}_t - [\nabla^2 F(\mathbf{w}_t)]^{-1} \nabla F(\mathbf{w}_t)$$
However, computing the full Hessian matrix requires evaluating $n$ individual Hessians.

Mert Pilanci and Martin J. Wainwright (2017) formulated the **Newton-Sketch**, using randomized matrix sketching to approximate the Hessian:
$$\mathbf{H}_t = \frac{1}{m} \sum_{i \in \mathcal{S}_t} \nabla^2 f_i(\mathbf{w}_t) \quad \text{or} \quad \mathbf{H}_t = \mathbf{X}^T \mathbf{\Pi}^T \mathbf{\Pi} \mathbf{X}$$
where $\mathbf{\Pi} \in \mathbb{R}^{m \times n}$ is a random Gaussian or Rademacher sketch matrix with sketch size $m \approx 4 d \ll n$.
Newton-Sketch solves the sketched quadratic sub-problem in $O(m d^2)$ operations instead of $O(n d^2)$, retaining the super-linear convergence of Newton's method while scaling to billion-row datasets.
"""

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6_deep4 = r"""
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
"""

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7_deep4 = r"""
## 7.10 Heavy Hitters: The Space-Saving Algorithm vs. Misra-Gries

In internet router traffic analysis, identifying the "heavy hitters" (the top $k$ destination IP addresses generating more than a fraction $\phi$ of total traffic) is essential for detecting Distributed Denial of Service (DDoS) attacks.

While the Count-Min Sketch provides frequency estimates for all items, Ahmed Metwally, Divyakant Agrawal, and Amr El Abbadi (2005) introduced the **Space-Saving Algorithm**, which tracks the top $k$ items with provable deterministic accuracy guarantees.

### The Space-Saving Algorithm
Maintain a pool of $m = \lceil 1 / \phi \rceil$ stream counters: each entry stores an item key $e_i$, an estimated count $c_i$, and an error bound $\epsilon_i$.
When item $x$ arrives:
1. **Cache Hit**: If $x$ is already in the pool ($x = e_j$), increment its counter: $c_j \leftarrow c_j + 1$.
2. **Cache Miss**: If $x$ is not present:
   - If the pool has free space, insert $x$ with $c = 1, \epsilon = 0$.
   - If the pool is full, find the item $e_{\min}$ with the minimal counter value $c_{\min} = \min_j c_j$.
   - Evict $e_{\min}$ and assign the slot to the new item $x$:
$$e_{\min} \leftarrow x, \quad c_{\min} \leftarrow c_{\min} + 1, \quad \epsilon_{\min} \leftarrow c_{\min} - 1$$

*Theoretical Guarantee*: The true frequency $f_x$ of any item satisfies:
$$c_x - \epsilon_x \le f_x \le c_x$$
Furthermore, $\epsilon_x \le N / m = \phi N$.
Any item whose true frequency exceeds $\phi N$ is **guaranteed to be present in the pool**, with maximum estimation error bounded strictly by $\phi N$. The algorithm uses strict $O(1/\phi)$ memory and executes in $O(1)$ amortized time per arrival using doubly linked bucket lists (Stream-Summary).

## 7.11 The DGIM Algorithm for Sliding-Window Bit Counts

Mayur Datar, Aristides Gionis, Piotr Indyk, and Rajeev Motwani (2002) introduced the **DGIM Algorithm**, solving the fundamental bit-counting problem over sliding windows:
*In a continuous binary stream of 0s and 1s, count how many 1-bits arrived in the most recent $N$ timesteps.*

Storing the entire $N$-bit window requires $N$ bits of physical memory. If $N = 10^{12}$ (the past trillion transactions), storage is impossible.
DGIM approximates the count to within a relative error $\epsilon$ using only:
$$O\left( \frac{1}{\epsilon} \ln^2 N \right) \text{ bits of memory!}$$

### DGIM Bucket Structure
DGIM compresses the sliding window into a collection of variable-sized **Buckets**:
- A bucket is defined by its timestamp (arrival time of its latest bit) and its size (the number of 1-bits it represents).
- Bucket sizes are constrained to powers of 2: $1, 2, 4, 8, 16, \dots$
- For any size $2^j$, there are either 1 or 2 buckets of that size (no more than 2).
- When a new 1 arrives, create a bucket of size 1. If this creates three buckets of size 1, merge the oldest two into a single bucket of size 2, propagating merges up the ladder.
- Buckets whose timestamps fall outside the sliding window $t - t_b > N$ are dropped.

To estimate the count of 1s in the past $k \le N$ steps, sum the sizes of all completely contained buckets, plus **half the size of the oldest overlapping bucket**. The relative estimation error is mathematically bounded by:
$$\text{Relative Error} \le \frac{2^{j-1}}{1 + \sum_{l=0}^{j-1} 2^l} = \frac{2^{j-1}}{2^j} = \mathbf{50\%}$$
By maintaining $k$ buckets per size level, the error drops to $\epsilon$ with $O(\frac{1}{\epsilon} \log^2 N)$ memory, compressing a trillion-bit stream into less than 2 kilobytes.
"""

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8_deep4 = r"""
## 8.9 Weighted False Discovery Rate and Functional Annotations

In high-dimensional genomics and proteomics, hypotheses $H_{0, 1}, \dots, H_{0, m}$ are not exchangeable: extensive prior biological metadata exists. For instance, in a GWAS studying coronary artery disease, single nucleotide polymorphisms (SNPs) located in known cardiac lipid metabolic pathways or protein-coding exons are biologically far more likely to be true non-null signals than intergenic non-coding variants.

Standard Benjamini-Hochberg treats all $m$ hypotheses with equal egalitarian weight, sacrificing statistical power on high-prior variants.
Christopher Genovese, Kathryn Roeder, and Larry Wasserman (2006) introduced the **Weighted False Discovery Rate (wFDR)**.

### Mathematical Formulation of Weighted FDR
Assign each hypothesis $i \in \{1, \dots, m\}$ a non-negative prior weight $w_i \ge 0$, normalized such that:
$$\frac{1}{m} \sum_{i=1}^m w_i = 1$$
Features with strong biological prior evidence receive weights $w_i > 1$, while low-prior background features receive weights $w_i < 1$.

Define the **weighted $p$-value** as:
$$p_i^w = \frac{p_i}{w_i}$$
Apply the standard Benjamini-Hochberg procedure to the weighted $p$-values:
1. Sort weighted $p$-values: $p_{(1)}^w \le p_{(2)}^w \le \dots \le p_{(m)}^w$.
2. Find the largest index $k$ such that:
$$p_{(k)}^w \le \frac{k}{m} q^*$$
3. Reject all corresponding hypotheses $H_{(1)}, \dots, H_{(k)}$.

*Theorem (Genovese, Roeder, Wasserman 2006)*: If the weights $w_i$ are determined independently of the current test statistics (e.g., from prior historical literature, external databases, or sample splitting), the weighted BH procedure **strictly controls the False Discovery Rate at level $q^*$**:
$$\mathrm{FDR} \le q^*$$
Weighting boosts discovery power by $40\%$ to $200\%$ on biologically informative candidates without introducing false positive bias.

## 8.10 Conformal Prediction in High-Dimensional Machine Learning

In modern big data analytics, black-box machine learning algorithms (such as deep neural networks, Random Forests, and XGBoost) generate point predictions $\hat{y} = f(\mathbf{x})$. However, point predictions convey zero statistical confidence: in medical diagnostics or autonomous vehicle steering, knowing whether a prediction has $\pm 2\%$ or $\pm 80\%$ uncertainty is a matter of life and death.

Vladimir Vovk, Alexander Gammerman, and Glenn Shafer (2005), followed by Emmanuel Candès, Yaniv Romano, and Rina Foygel Barber (2019), developed **Conformal Prediction**, generating **exact, distribution-free prediction intervals** for any arbitrary black-box predictive model.

### 1. Split Conformal Prediction
Let $(X_1, Y_1), \dots, (X_n, Y_n)$ be training data, and $(X_{n+1}, Y_{n+1})$ be a new unseen test observation. The only assumption required is **Exchangeability** (satisfied by i.i.d. sampling).

1. **Data Splitting**: Split the historical data into a training set $\mathcal{D}_{\text{train}}$ of size $n_1$ and a calibration set $\mathcal{D}_{\text{cal}}$ of size $n_2$.
2. **Model Training**: Fit an arbitrary model $\hat{\mu}(\mathbf{x})$ on $\mathcal{D}_{\text{train}}$.
3. **Non-Conformity Scoring**: For each observation $i \in \mathcal{D}_{\text{cal}}$, evaluate the prediction residual:
$$E_i = |Y_i - \hat{\mu}(X_i)|$$
4. **Quantile Selection**: Let $q_{\alpha}$ be the $\lceil (n_2 + 1)(1 - \alpha) \rceil / n_2$ empirical quantile of the calibration scores $\{E_1, \dots, E_{n_2}\}$.
5. **Prediction Band Construction**: For a new query point $X_{n+1}$, the conformal prediction interval is:
$$\mathcal{C}(X_{n+1}) = \left[ \hat{\mu}(X_{n+1}) - q_\alpha, \, \hat{\mu}(X_{n+1}) + q_\alpha \right]$$

*Theorem (Exact Finite-Sample Conformal Coverage)*: For any black-box predictive algorithm, any feature dimension $p$, and any underlying probability distribution:

$$1 - \alpha \le P\left( Y_{n+1} \in \mathcal{C}(X_{n+1}) \right) \le 1 - \alpha + \frac{1}{n_2 + 1}$$

The validity of the confidence band is **mathematically exact in finite samples**. It requires zero Gaussian assumptions, zero asymptotic expansions, and zero regularity conditions, establishing conformal prediction as the premier uncertainty quantification engine for modern big data.
"""

def main():
    append_to_unit(5, u5_deep4)
    append_to_unit(6, u6_deep4)
    append_to_unit(7, u7_deep4)
    append_to_unit(8, u8_deep4)
    print("Units 5-8 deep pass 4 applied.")

if __name__ == "__main__":
    main()
