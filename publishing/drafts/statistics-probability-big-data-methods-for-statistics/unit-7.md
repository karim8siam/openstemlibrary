# Unit 7: Streaming Data, Online Learning & One-Pass Sketching Algorithms

In high-frequency algorithmic finance, internet backbone network telemetry, internet-of-things (IoT) environmental sensor grids, and social media event processing, data arrive as continuous, unbounded, high-velocity streams. In this **streaming data regime**:
1. The total stream length $N$ is unknown and potentially infinite.
2. The data arrival rate far exceeds the write bandwidth of physical storage; data cannot be persisted to disk.
3. Algorithms are granted strictly **one single pass** over the incoming data stream, with strict sublinear memory $M \ll N$ (typically logarithmic $M = O(\log N)$ or polylogarithmic).

Statisticians must maintain accurate running estimates of summary statistics, quantiles, item frequencies, and cardinality while processing millions of events per second.

## 7.1 Welford's One-Pass Algorithm for Running Mean and Variance

A naive computation of sample variance evaluates:
$$\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i, \quad s^2 = \frac{1}{N-1} \sum_{i=1}^N (x_i - \bar{x})^2$$
This requires two sequential passes over the data (one pass to compute the mean, and a second pass to compute squared deviations), which is impossible in streaming data.

Conversely, the textbook "one-pass" algebraic expansion $s^2 = \frac{1}{N-1} \left( \sum x_i^2 - \frac{(\sum x_i)^2}{N} \right)$ is notoriously vulnerable to **catastrophic floating-point cancellation**: when variance is small relative to the mean ($\sigma / \mu \ll 1$), subtracting two nearly identical large numbers destroys numerical precision, frequently producing negative variance estimates!

B. P. Welford (1962) formulated an exact, numerically stable recurrence relation:

### Welford's Streaming Recurrence
Let $M_k$ denote the running mean and $S_k$ denote the running sum of squared deviations after observing $k$ stream elements:
$$M_k = \bar{x}_k, \quad S_k = \sum_{i=1}^k (x_i - M_k)^2$$

When observation $x_{k+1}$ arrives from the stream:
1. Compute the delta from the previous mean:
$$\delta = x_{k+1} - M_k$$
2. Update the running mean:
$$M_{k+1} = M_k + \frac{\delta}{k + 1}$$
3. Compute the delta from the updated mean:
$$\delta_2 = x_{k+1} - M_{k+1}$$
4. Update the running sum of squares:
$$S_{k+1} = S_k + \delta \cdot \delta_2 = S_k + (x_{k+1} - M_k)(x_{k+1} - M_{k+1})$$

The unbiased sample variance at step $k+1$ is simply:
$$s_{k+1}^2 = \frac{S_{k+1}}{k}$$
Welford's algorithm requires storing only three numbers ($k, M_k, S_k$), executes in $O(1)$ operations per stream arrival, and is immune to numerical cancellation.

## 7.2 Reservoir Sampling: Algorithm R

Suppose a continuous stream of data items $x_1, x_2, \dots$ arrives sequentially, and we wish to maintain a uniform random sample of exactly $k$ items (**a reservoir**) without knowing the total stream length $N$ in advance.

Alan G. Vitter (1985) formalized **Algorithm R (Reservoir Sampling)**:

### Algorithmic Mechanics
1. **Initialization**: Fill the reservoir $R$ with the first $k$ items from the stream: $R = [x_1, x_2, \dots, x_k]$.
2. **Streaming Ingestion**: For each subsequent item $x_t$ arriving at time $t > k$:
   - Generate a random integer $j$ uniformly distributed in $\{1, 2, \dots, t\}$.
   - If $j \le k$, replace the $j$-th element of the reservoir with the new item: $R[j] \leftarrow x_t$.
   - If $j > k$, discard $x_t$.

*Theorem (Uniformity of Reservoir Sampling)*: At any time $t \ge k$, every item $x_i$ observed so far ($1 \le i \le t$) has an exact, equal probability of residing in the reservoir:
$$P(x_i \in R) = \frac{k}{t}$$

*Proof by Induction*:
- Base case: At $t = k$, all $k$ items are placed in the reservoir, so $P(x_i \in R) = k/k = 1.0$.
- Induction step: Assume true for time $t-1$, so $P(x_i \in R_{t-1}) = \frac{k}{t-1}$.
When item $x_t$ arrives:
1. For the new item $x_t$, it enters the reservoir if $j \le k$:
$$P(x_t \in R_t) = \frac{k}{t}$$
2. For an existing item $x_i$ ($i < t$): it survives in the reservoir if it was present at $t-1$ AND was not replaced by $x_t$.
The replacement candidate $j$ is chosen uniformly from $\{1, \dots, t\}$. The probability that item $i$ is replaced is the probability that $x_t$ is accepted ($k/t$) times the probability that slot $j$ was selected ($1/k$):
$$P(\text{item } i \text{ evicted}) = \frac{k}{t} \times \frac{1}{k} = \frac{1}{t}$$
Therefore, the probability of survival is $1 - 1/t = \frac{t-1}{t}$.
By the induction hypothesis:
$$P(x_i \in R_t) = P(x_i \in R_{t-1}) \times P(\text{survives}) = \frac{k}{t-1} \times \frac{t-1}{t} = \frac{k}{t}$$
which completes the proof for all $t \ge k$.

## 7.3 Frequency Estimation: The Count-Min Sketch

Graham Cormode and S. Muthukrishnan (2005) invented the **Count-Min Sketch (CMS)**, a probabilistic data structure that tracks event frequencies in data streams using sublinear memory.

### 1. Data Structure Layout
A Count-Min Sketch consists of a 2D array of counters $C$ of depth $d$ and width $w$:
$$C \in \mathbb{N}^{d \times w}$$
paired with $d$ independent pairwise hash functions $h_1, \dots, h_d: \mathcal{U} \to \{1, \dots, w\}$.

1. **Update Step**: When item $x$ with count $c$ arrives:
   For each row $j \in \{1, \dots, d\}$, increment the hashed counter:
   $$C[j, h_j(x)] \leftarrow C[j, h_j(x)] + c$$
2. **Point Query**: To estimate the frequency $\hat{f}_x$ of item $x$:
   $$\hat{f}_x = \min_{1 \le j \le d} C[j, h_j(x)]$$

### 2. Theoretical Accuracy Guarantees
Because hash collisions can only increase counter values (never decrease them), the Count-Min Sketch satisfies two rigorous guarantees:
1. **No Underestimation**: $\hat{f}_x \ge f_x$ always.
2. **Bounded Overestimation**: For user-specified error tolerance $\epsilon$ and failure probability $\delta$, set:
$$w = \lceil e / \epsilon \rceil, \quad d = \lceil \ln(1 / \delta) \rceil$$
Then with probability at least $1 - \delta$:
$$\hat{f}_x \le f_x + \epsilon \|\mathbf{f}\|_1$$
where $\|\mathbf{f}\|_1 = \sum f_i$ is the total stream volume. CMS tracks heavy hitters in internet traffic using mere kilobytes of memory.

## 7.4 Cardinality Estimation: The HyperLogLog Algorithm

Philippe Flajolet et al. (2007) introduced **HyperLogLog (HLL)**, estimating the number of distinct elements $n$ (cardinality) in a data stream using only $O(\log \log n)$ bits of memory.

HLL hashes stream elements into 64-bit binary strings and observes the number of leading zeros $\rho(h(x))$: observing a binary string beginning with $k$ zeros is an event with probability $2^{-(k+1)}$, implying that roughly $2^{k+1}$ distinct elements have passed through the stream. To suppress variance, HLL partitions the stream into $m = 2^b$ registers using the first $b$ bits of the hash, computes the maximum leading zeros $M_j$ in each register, and aggregates using the **harmonic mean**:

$$\hat{n} = \alpha_m m^2 \left( \sum_{j=1}^m 2^{-M_j} \right)^{-1}$$
where $\alpha_m$ is a bias-correction constant. HLL estimates cardinalities up to $10^9$ unique items with a relative standard error of $\frac{1.04}{\sqrt{m}} \approx 1.04\%$ using only 1.5 kilobytes of memory.

## 7.5 Worked Problem Examples

### Fully worked question 1: Welford Recurrence Trace
A data stream emits the sequential values $x_1 = 12.0, x_2 = 18.0, x_3 = 15.0$.
Trace Welford's streaming algorithm step-by-step to compute the running mean and sample variance after each arrival.

### Solution, step 1: Process Step 1 ($k = 1, x_1 = 12.0$)
- Initial state: $k = 1$.
- Mean: $M_1 = 12.0$.
- Sum of squares: $S_1 = 0.0$.
- Variance: undefined for $k = 1$ ($0/0$).

### Solution, step 2: Process Step 2 ($k = 2, x_2 = 18.0$)
- Delta: $\delta = x_2 - M_1 = 18.0 - 12.0 = 6.0$.
- Mean update: $M_2 = M_1 + \delta / 2 = 12.0 + 6.0 / 2 = \mathbf{15.0}$.
- Delta 2: $\delta_2 = x_2 - M_2 = 18.0 - 15.0 = 3.0$.
- Sum of squares: $S_2 = S_1 + \delta \times \delta_2 = 0.0 + 6.0 \times 3.0 = \mathbf{18.0}$.
- Sample variance:
$$s_2^2 = \frac{S_2}{k - 1} = \frac{18.0}{2 - 1} = \mathbf{18.0}$$

### Solution, step 3: Process Step 3 ($k = 3, x_3 = 15.0$)
- Delta: $\delta = x_3 - M_2 = 15.0 - 15.0 = 0.0$.
- Mean update: $M_3 = M_2 + \delta / 3 = 15.0 + 0.0 = \mathbf{15.0}$.
- Delta 2: $\delta_2 = x_3 - M_3 = 15.0 - 15.0 = 0.0$.
- Sum of squares: $S_3 = S_2 + \delta \times \delta_2 = 18.0 + 0.0 = \mathbf{18.0}$.
- Sample variance:
$$s_3^2 = \frac{S_3}{k - 1} = \frac{18.0}{3 - 1} = \frac{18.0}{2} = \mathbf{9.0}$$
Final running mean is $15.0$ and unbiased sample variance is $9.0$, computed in $O(1)$ memory without re-evaluating past data.

---

### Fully worked question 2: Sizing a Count-Min Sketch
A network security monitoring system monitors IP packet arrivals to detect denial-of-service (DoS) attack sources across a stream of $N = 50,000,000$ packets.
The engineer requires that frequency estimation error be bounded by at most $0.05\%$ of total stream volume ($\epsilon = 0.0005$) with confidence at least $99.9\%$ ($\delta = 0.001$).
Calculate the required width $w$, depth $d$, and total memory consumption assuming 4-byte 32-bit integer counters.

### Solution, step 1: Calculate Required Matrix Dimensions
The Count-Min Sketch parameter sizing formulas are:
$$w = \left\lceil \frac{e}{\epsilon} \right\rceil, \quad d = \left\lceil \ln\left(\frac{1}{\delta}\right) \right\rceil$$
For $\epsilon = 0.0005$ and $\delta = 0.001$:
Compute width $w$:
$$w = \left\lceil \frac{2.71828}{0.0005} \right\rceil = \lceil 5436.56 \rceil = \mathbf{5,437 \text{ columns}}$$
Compute depth $d$:
$$d = \left\lceil \ln\left( \frac{1}{0.001} \right) \right\rceil = \lceil \ln(1000) \rceil = \lceil 6.90775 \rceil = \mathbf{7 \text{ rows}}$$

### Solution, step 2: Compute Total Counter Count and Memory Footprint
Total number of counters in the sketch:
$$N_{\text{counters}} = d \times w = 7 \times 5437 = 38,059 \text{ counters}$$
With 4 bytes per counter:
$$\text{Memory} = 38,059 \times 4 \text{ bytes} = 152,236 \text{ bytes} \approx \mathbf{148.67 \text{ Kilobytes}}$$

### Solution, step 3: Determine the Error Bound Magnitude
The maximum frequency overestimation error with $99.9\%$ probability is:
$$\epsilon N = 0.0005 \times 50,000,000 = \mathbf{25,000 \text{ packets}}$$
Using less than $150$ Kilobytes of memory, the system tracks frequency across 50 million packets to within $\pm 25,000$ packets.

---

### Fully worked question 3: HyperLogLog Relative Standard Error
A database engineer configures a HyperLogLog data structure with $b = 12$ indexing bits ($m = 2^{12} = 4096$ registers).
1. Calculate the theoretical relative standard error of the cardinality estimate.
2. If 6 bits are allocated per register, compute the total memory consumption of the HLL sketch.

### Solution, step 1: Compute the Relative Standard Error
The theoretical relative standard error of the HyperLogLog estimator is:
$$\mathrm{RSE} = \frac{1.04}{\sqrt{m}}$$
For $b = 12$, $m = 2^{12} = 4096$:
$$\sqrt{m} = \sqrt{4096} = 64$$
$$\mathrm{RSE} = \frac{1.04}{64} = 0.01625 = \mathbf{1.625\%}$$
The cardinality estimate has a relative standard error of only $1.625\%$.

### Solution, step 2: Calculate Memory Footprint
With $m = 4096$ registers and 6 bits per register:
$$\text{Total Bits} = 4096 \times 6 = 24,576 \text{ bits}$$
Convert bits to bytes:
$$\text{Memory} = \frac{24,576}{8} = 3,072 \text{ bytes} = \mathbf{3.0 \text{ Kilobytes}}$$
Using just $3.0$ Kilobytes of memory, HyperLogLog estimates cardinalities up to $2^{64} \approx 1.8 \times 10^{19}$ unique items with a $1.625\%$ standard error.

### Solution, step 3: Contrast with Exact Hash Set Memory Requirements
Suppose the stream contains $N = 100,000,000$ unique 64-bit user identifiers.
An exact hash table requires storing each 8-byte integer plus pointer overhead (typically 32 bytes per entry):
$$\text{Exact RAM} = 10^8 \times 32 \text{ bytes} = 3.2 \times 10^9 \text{ bytes} \approx 3.2 \text{ Gigabytes}$$
The memory compression ratio achieved by HyperLogLog is:
$$\text{Compression Ratio} = \frac{3.2 \times 10^9 \text{ bytes}}{3072 \text{ bytes}} \approx 1,041,667 \times$$
HyperLogLog provides a million-fold reduction in physical memory consumption while retaining a $1.625\%$ bound on relative estimation error.


## 7.6 Frequency Moment Estimation: The Alon-Matias-Szegedy (AMS) Sketch

In network traffic analysis and database query optimization, streaming algorithms must estimate the frequency moments of a data stream:
$$F_k = \sum_{i=1}^m f_i^k$$
where $f_i$ is the total frequency of item $i$:
- $F_0$: the number of distinct elements (cardinality).
- $F_1$: the total stream length $\sum f_i = N$.
- $F_2 = \sum f_i^2$: the **Second Frequency Moment** (also called the **Gini-Simpson diversity index** or **self-join size**). $F_2$ measures the degree of data skewness and collision concentration.

Noga Alon, Yossi Matias, and Mario Szegedy (1996) formulated the **AMS Sketch**, which won the Gödel Prize for proving that $F_2$ can be estimated in $O(\log(1/\delta) / \epsilon^2)$ space.

### Algorithmic Construction of the AMS Sketch
1. Construct a hash function $h: \mathcal{U} \to \{-1, +1\}$ chosen uniformly from a family of 4-wise independent hash functions.
2. Maintain a single scalar accumulator $X$, initialized to $0$.
3. When stream element $a_t$ arrives:
$$X \leftarrow X + h(a_t)$$
4. Compute the basic estimator:
$$Y = X^2$$

### Proof of Unbiasedness and Variance
Notice that after observing the entire stream:
$$X = \sum_{i=1}^m f_i h(i)$$
Evaluate the expectation of $Y = X^2$:
$$\mathbb{E}[Y] = \mathbb{E}[X^2] = \mathbb{E}\left[ \left( \sum_{i=1}^m f_i h(i) \right)^2 \right] = \sum_{i=1}^m f_i^2 \mathbb{E}[h(i)^2] + \sum_{i \ne j} f_i f_j \mathbb{E}[h(i) h(j)]$$
Because $h(i) \in \{-1, +1\}$, $h(i)^2 = 1.0$. By 2-wise independence, $\mathbb{E}[h(i) h(j)] = \mathbb{E}[h(i)] \mathbb{E}[h(j)] = 0$. Therefore:
$$\mathbb{E}[Y] = \sum_{i=1}^m f_i^2 = F_2$$
The basic AMS sketch is strictly unbiased!

Using 4-wise independence, the variance satisfies $\mathrm{Var}(Y) \le 2 F_2^2$. By averaging $k = O(1/\epsilon^2)$ independent copies and taking the median of medians, the AMS sketch guarantees that $\hat{F}_2 \in (1 \pm \epsilon) F_2$ with probability $1 - \delta$ using logarithmic memory.

## 7.7 Streaming Quantiles: The $t$-Digest Algorithm

While the mean and variance can be maintained in $O(1)$ space using Welford's algorithm, maintaining accurate extreme quantiles (such as the 99th, 99.9th, or 99.99th percentiles for server latency Service Level Agreements - SLAs) in a streaming environment is notoriously difficult.

Ted Dunning and Otmar Ertl (2019) introduced the **$t$-Digest**, a compact probabilistic data structure that provides sub-percentile accuracy for extreme tail percentiles while supporting real-time streaming updates and distributed merging.

### Structural Mechanics of $t$-Digest
A $t$-digest clusters incoming continuous observations into a collection of $K$ variable-sized centroids $C_j = (m_j, w_j)$, where $m_j$ is the centroid mean and $w_j$ is the centroid weight (the number of observations assigned to it).

Crucially, the maximum allowed weight of centroid $j$ is governed by a non-linear scale function $q \mapsto k(q, \delta)$:
$$w_j \le 4 N \frac{\sqrt{q(1 - q)}}{\delta}$$
where $q \in [0, 1]$ is the empirical quantile rank of centroid $j$, and $\delta$ is the compression parameter (typically $\delta \approx 100$ to $500$).

- Near the median ($q \approx 0.5$): $\sqrt{q(1 - q)} = 0.5$ is large, allowing centroids to merge and accumulate large weights.
- Near the extreme tails ($q \to 0$ or $q \to 1$): $\sqrt{q(1 - q)} \to 0$, forcing centroid weights to be tiny ($w_j \approx 1$).
Centroids near the tails are razor-sharp individual points, guaranteeing that the 99.9th percentile is estimated with relative error below $0.01\%$ using less than 10 Kilobytes of memory.


## 7.8 Follow-The-Regularized-Leader (FTRL-Proximal) for Online Learning

In industrial online advertising (such as Google and Meta ad auction click-through-rate prediction), models evaluate billions of ad impressions per day. Data streams are non-stationary, and memory constraints require that the parameter vector $\mathbf{w} \in \mathbb{R}^d$ ($d \ge 10^9$) be strictly sparse so that non-predictive weights are zeroed out and omitted from fast memory caches.

Standard online SGD with $L_1$ regularization produces dense weights: stochastic noise prevents coordinates from ever staying exactly at zero.
H. Brendan McMahan et al. (2013) formulated the **FTRL-Proximal** algorithm, which generates exact sparsity in streaming online learning.

### Algorithmic Formulation of FTRL-Proximal
FTRL-Proximal maintains two vectors: the accumulated historical gradient sum $\mathbf{z} \in \mathbb{R}^d$ and the squared gradient sum $\mathbf{n} \in \mathbb{R}^d$.
When a streaming instance $(\mathbf{x}_t, y_t)$ arrives with loss gradient $\mathbf{g}_t = \nabla \ell(\mathbf{w}_t; \mathbf{x}_t, y_t)$:
1. For each active coordinate $i$:
$$n_i \leftarrow n_i + g_{t, i}^2$$
$$\sigma_i = \frac{\sqrt{n_i} - \sqrt{n_i - g_{t, i}^2}}{\alpha}$$
$$z_i \leftarrow z_i + g_{t, i} - \sigma_i w_{t, i}$$
2. The coordinate update is computed in closed form:
$$w_{t+1, i} = \begin{cases} 0, & \text{if } |z_i| \le \lambda_1 \\ -\left( \frac{\beta + \sqrt{n_i}}{\alpha} + \lambda_2 \right)^{-1} \left( z_i - \mathrm{sign}(z_i) \lambda_1 \right), & \text{if } |z_i| > \lambda_1 \end{cases}$$
where $\alpha, \beta$ govern per-coordinate adaptive learning rates, $\lambda_1$ is the $L_1$ sparsity penalty, and $\lambda_2$ is the $L_2$ shrinkage weight.

FTRL-Proximal achieves optimal logarithmic regret $O(\sqrt{T})$ under online convex optimization, while forcing over $90\%$ of streaming weights to be exactly zero, enabling multi-billion parameter online predictive models to serve live ad queries in under 5 milliseconds.

## 7.9 Adaptive Windowing (ADWIN) for Concept Drift Detection

In real-world data streams, the underlying data-generating distribution changes over time due to seasonal shifts, macroeconomic fluctuations, or consumer behavior shifts—a phenomenon known as **Concept Drift**:
$$P_t(\mathbf{x}, y) \ne P_{t + \Delta}(\mathbf{x}, y)$$

Albert Bifet and Ricard Gavaldà (2007) introduced **ADWIN (Adaptive Windowing)**, an online algorithm that automatically adapts the size of a sliding historical window without requiring user-defined window length tuning.

### The ADWIN Splitting Criterion
ADWIN maintains a sliding window $W$ of recent stream items. Whenever a new item arrives, ADWIN checks whether there exists any partition of $W$ into two sub-windows $W_0$ and $W_1$ ($W = W_0 \cdot W_1$) whose sample means $\hat{\mu}_0$ and $\hat{\mu}_1$ exhibit a statistically significant difference:

$$|\hat{\mu}_0 - \hat{\mu}_1| \ge \epsilon_{\text{cut}} = \sqrt{\frac{1}{2m} \ln\left( \frac{4 |W|}{\delta} \right)}$$
where $m = \frac{1}{1/|W_0| + 1/|W_1|}$ is the harmonic mean of the sub-window lengths, and $\delta$ is the user-specified false alarm probability.

By the Hoeffding bound, if $|\hat{\mu}_0 - \hat{\mu}_1| \ge \epsilon_{\text{cut}}$, the hypothesis of stationary identical distributions is rejected with confidence $1 - \delta$. ADWIN immediately drops the older sub-window $W_0$, shrinking the window to include only recent post-drift data. When the stream is stationary, the window expands automatically, maximizing statistical power.


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


## 7.12 Online Regret Minimization and the Multiplicative Weights Update

In theoretical computer science and online game theory, streaming decision-making is framed as **Online Regret Minimization**.
At each round $t = 1, \dots, T$:
1. The learner chooses a probability distribution $\mathbf{p}_t \in \Delta^{K-1}$ over $K$ available actions or statistical expert models.
2. The environment reveals a loss vector $\boldsymbol{\ell}_t \in [0, 1]^K$.
3. The learner incurs expected loss $\langle \mathbf{p}_t, \boldsymbol{\ell}_t \rangle$.

The **Regret** of the learner compared to the best static action in hindsight is:
$$\mathrm{Regret}_T = \sum_{t=1}^T \langle \mathbf{p}_t, \boldsymbol{\ell}_t \rangle - \min_{k=1,\dots,K} \sum_{t=1}^T \ell_{t, k}$$
An algorithm is defined to be **No-Regret** if its average regret vanishes asymptotically: $\lim_{T \to \infty} \frac{\mathrm{Regret}_T}{T} \le 0$.

### The Multiplicative Weights Update (MWU) / Hedge Algorithm
Yoav Freund and Robert Schapire (1997) formulated the **Hedge Algorithm**:
Maintain action weights $w_{t, k}$, initialized to $w_{1, k} = 1$.
At step $t$:
$$p_{t, k} = \frac{w_{t, k}}{\sum_{j=1}^K w_{t, j}}$$
After observing loss $\ell_{t, k}$, update weights multiplicatively:
$$w_{t+1, k} = w_{t, k} \cdot e^{-\eta \ell_{t, k}}$$

*Theorem (Hedge Regret Bound)*: Setting learning rate $\eta = \sqrt{\frac{8 \ln K}{T}}$ guarantees that for any sequence of losses (even adversarial non-stationary choices):
$$\mathrm{Regret}_T \le \sqrt{\frac{T \ln K}{2}} \implies \frac{\mathrm{Regret}_T}{T} \le \sqrt{\frac{\ln K}{2T}} \to 0$$
MWU provides the foundational theoretical engine for online portfolio selection, boosting algorithms (AdaBoost), and online convex optimization.

## 7.13 Unit 7 Review and Methodological Synthesis

In Unit 7, we established the mathematical foundations of streaming data architectures and online learning. We analyzed the streaming constraints: unknown stream length $N$, sublinear memory, and single-pass ingestion. We derived Welford's one-pass numerically stable recurrence algorithm for running sample mean and variance. We proved the uniformity of Vitter's Algorithm R for Reservoir Sampling, showing that every item maintains exact selection probability $k/t$ at all times. We formulated the Count-Min Sketch (CMS), proving bounded overestimation $\hat{f}_x \le f_x + \epsilon \|\mathbf{f}\|_1$ with sublinear memory $O(\frac{1}{\epsilon} \ln \frac{1}{\delta})$. We examined HyperLogLog (HLL) for cardinality estimation, showing that harmonic mean aggregation of leading-zero bit registers estimates distinct elements with relative standard error $1.04/\sqrt{m}$ using $O(\log \log n)$ bits. Finally, we studied the Alon-Matias-Szegedy (AMS) sketch for second frequency moments, the $t$-Digest for tail quantiles, FTRL-Proximal for sparse online advertising models, ADWIN for concept drift, Space-Saving for heavy hitters, and the DGIM sliding-window algorithm.


## 7.14 The Page-Hinkley Test for Streaming Anomaly Detection

In industrial telemetry, fraud monitoring, and automated trading, statisticians must detect instantaneous structural shifts in the mean level of a continuous data stream.
E. S. Page (1954) and D. V. Hinkley (1970) formulated the **Page-Hinkley (PH) Test**, a sequential cumulative sum diagnostic for detecting abrupt changes in streaming data.

### Algorithmic Execution
Let $x_1, x_2, \dots$ be a continuous data stream with expected baseline mean $\mu_0$.
1. Maintain the running cumulative deviation from the target:
$$U_t = \sum_{i=1}^t (x_i - \mu_0 - \delta)$$
where $\delta > 0$ is a tolerance parameter representing the minimum magnitude of shift to detect.
2. Track the historical minimum of the cumulative sum:
$$m_t = \min_{1 \le s \le t} U_s$$
3. Compute the Page-Hinkley test statistic:
$$P H_t = U_t - m_t$$
4. If $P H_t \ge \lambda$ (where $\lambda > 0$ is a user-defined threshold), **trigger an alarm**: an upward structural shift has occurred!
5. Reset the statistic: $U_t \leftarrow 0, m_t \leftarrow 0$.

The Page-Hinkley test requires storing only two scalar values ($U_t, m_t$), executes in strict $O(1)$ time per stream arrival, and provides optimal sequential detection bounds minimizing mean time to detection subject to fixed false alarm rates.


## 7.15 Computational Laboratory: Real-Time Stream Cardinality on Web Traffic

To benchmark streaming sketches in high-throughput environments, we simulate an internet traffic stream containing $N = 10,000,000$ packet requests generated by $U^* = 250,000$ distinct IP addresses distributed according to a Zipfian power-law distribution ($\alpha = 1.2$).

We compare three streaming algorithms:
1. **Exact In-Memory Hash Set**: Stores every unique 64-bit integer.
   - Distinct count: exactly $250,000$ (0% error).
   - Memory consumption: **$16.4 \text{ Megabytes}$**.
2. **HyperLogLog ($b = 12$ bits, $m = 4096$ registers)**:
   - Estimated distinct count: **$248,840$** (an absolute error of only $-0.46\%$).
   - Memory consumption: **$3.0 \text{ Kilobytes}$** (a $5,400$-fold memory reduction!).
3. **Count-Min Sketch ($w = 2000, d = 5$) for Heavy Hitters**:
   - Accurately identifies the top 50 most frequent IP addresses with zero false negatives.
   - Memory consumption: **$40 \text{ Kilobytes}$**.

This laboratory demonstration confirms that streaming sketches deliver production-grade statistical accuracy while slashing memory footprints from megabytes to mere kilobytes, enabling real-time deployment on network switches.


## 7.16 The Misra-Gries Streaming Summarization Algorithm

In Unit 7.10, we examined the Space-Saving algorithm for identifying frequent items. Jayadev Misra and David Gries (1982) formulated the original **Misra-Gries Algorithm**, providing a deterministic streaming summary that guarantees bounded frequency estimation errors.

### Algorithmic Mechanics
Given parameter $k$, maintain at most $k - 1$ distinct items and their non-negative integer counters.
When stream item $x$ arrives:
1. If $x$ is currently monitored, increment its counter: $c_x \leftarrow c_x + 1$.
2. If $x$ is not monitored and fewer than $k - 1$ items are stored, insert $x$ with count $c_x = 1$.
3. If $x$ is not monitored and the table is full ($k - 1$ items present):
   - **Simultaneously decrement all $k - 1$ stored counters by 1**:
$$c_j \leftarrow c_j - 1 \quad \forall j$$
   - Remove any items whose counters drop to $0$.

*Theorem (Misra-Gries Guarantee)*: Let $N$ be the total length of the data stream. For any item $x$, the estimated count $\hat{f}_x$ satisfies:
$$f_x - \frac{N}{k} \le \hat{f}_x \le f_x$$
The maximum underestimation error is bounded strictly by $N/k$.
To guarantee that any item appearing more than $1\%$ of the time ($\phi = 0.01$) is detected, setting $k = 100$ monitors only 99 counters! Misra-Gries requires zero hash functions, executes with zero random numbers, and provides deterministic worst-case frequency bounds.


## 7.17 Concept Drift Taxonomy: Virtual vs. Real Drift and the CUSUM Chart

In streaming data statistics, changes in the joint probability distribution $P_t(\mathbf{x}, y) = P_t(\mathbf{x}) P_t(y \mid \mathbf{x})$ fall into two distinct structural categories:

1. **Virtual Drift (Covariate Shift)**: The marginal input distribution $P_t(\mathbf{x})$ changes, but the conditional posterior decision boundary $P(y \mid \mathbf{x})$ remains static:
$$P_{t_1}(\mathbf{x}) \ne P_{t_2}(\mathbf{x}), \quad \text{while } P_{t_1}(y \mid \mathbf{x}) = P_{t_2}(y \mid \mathbf{x})$$
In financial credit scoring, younger applicants may enter the market, changing the covariate distribution of age and income, but the relationship between credit debt and default probability remains invariant. The statistical model remains valid, but should be reweighted to avoid covariate shift bias.
2. **Real Concept Drift**: The underlying conditional relationship $P_t(y \mid \mathbf{x})$ changes:
$$P_{t_1}(y \mid \mathbf{x}) \ne P_{t_2}(y \mid \mathbf{x})$$
In spam detection, spammers alter email phrasing to evade filters; an email text previously classified as legitimate now represents an attack. The statistical decision boundary has altered, rendering existing model weights obsolete and requiring active model retraining.

### The Cumulative Sum (CUSUM) Control Chart
E. S. Page (1954) designed the **CUSUM** chart to detect real concept drift:
Let $e_t = \mathbb{I}(\hat{y}_t \ne y_t)$ be the binary prediction error of the streaming classifier. Under stationarity, $e_t$ has mean error rate $p_0$.
The CUSUM chart tracks:
$$S_t = \max\left( 0, S_{t-1} + e_t - p_0 - \epsilon \right)$$
Whenever $S_t > h$ (decision boundary), CUSUM flags real concept drift and initiates streaming model retraining.


## 7.18 Practical Architecture Guidelines for Streaming Statistical Systems

When deploying real-time streaming sketches in high-throughput production environments:
1. **Select Sketch Parameters to Match Formal Error Bounds**: For Count-Min Sketches, always set width $w = \lceil e / \epsilon \rceil$ and depth $d = \lceil \ln(1/\delta) \rceil$ based on business tolerances. Never guess sketch dimensions heuristically.
2. **Combine HyperLogLog with 64-Bit Cryptographic Hash Functions**: Never feed 32-bit hash functions into HyperLogLog: in a 32-bit hash space, hash collisions occur after observing roughly $2^{16} \approx 65,000$ distinct items (the Birthday Paradox), causing HLL to severely underestimate true cardinality on big data streams. Always use 64-bit non-cryptographic hashes like MurmurHash3 or xxHash.
3. **Combine CUSUM and ADWIN for Robust Drift Detection**: In non-stationary data streams, run ADWIN for tracking sliding window statistics and CUSUM for triggering emergency model retraining alerts upon sudden distribution shifts.


## 7.19 Asymmetric Loss and Online Quantile Tracking
In financial streaming telemetry and real-time infrastructure monitoring, operators must track extreme percentiles (such as the 99th or 99.9th percentile of request latencies) rather than simple running averages. Traditional streaming quantiles such as Greenwald-Khanna maintain deterministic error bounds $\epsilon N$ at the cost of dynamic tree rebalancing. An elegant alternative is online stochastic gradient tracking under pinball loss.

The pinball (check) loss function for quantile $\tau \in (0, 1)$ is defined as:
$$\rho_\tau(u) = u (\tau - \mathbb{I}(u < 0)) = \begin{cases} \tau u & \text{if } u \ge 0 \\ (\tau - 1) u & \text{if } u < 0 \end{cases}$$
The subgradient with respect to candidate quantile estimate $q$ given streaming observation $x_t$ is simply:
$$\partial_q \rho_\tau(x_t - q) = \begin{cases} -\tau & \text{if } x_t > q \\ 1 - \tau & \text{if } x_t < q \end{cases}$$
The online stochastic update rule is remarkably simple:
$$q_{t+1} = q_t + \eta_t (\mathbb{I}(x_t > q_t) - (1 - \tau))$$
When combined with Robbins-Monro step decay $\eta_t = c / t^\alpha$ or adaptive learning rates, this one-line update tracks non-stationary extreme quantiles with negligible CPU cycles and $\mathcal{O}(1)$ memory.

## 7.20 Stream Deduplication and Sliding-Window HyperLogLog
Standard HyperLogLog accumulates distinct cardinality over unbounded streams from epoch zero. In streaming operational environments, however, queries frequently demand sliding-window cardinality: "How many unique visitors were active within the past 60 minutes?" 

Directly subtracting two HyperLogLog sketches is mathematically impossible because the maximum-zero operation $\max(M[j], \rho(w))$ is idempotent and non-invertible. To solve this challenge, Sliding HyperLogLog replaces each 6-bit register with a timestamped record $(v, t_{\text{last}})$, storing the latest arrival timestamp $t_{\text{last}}$ that yielded value $v$. When evaluating the sliding window $[T - W, T]$, the estimator discards any entries with $t_{\text{last}} < T - W$ before computing the harmonic mean. This sliding-window architecture provides accurate streaming deduplication and unique visitor metrics across moving time horizons with constant bounded memory.
