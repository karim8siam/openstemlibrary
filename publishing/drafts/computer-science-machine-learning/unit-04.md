# Unit 4: Unsupervised methods

*Editorial draft; not approved for live publication.*

## Clustering
### Clustering

### Clustering organizes data according to a chosen geometry
Clustering attempts to discover groups without observed class labels, but there is no universally correct partition. K-means minimizes the sum of squared distances from observations to their assigned centroids. Given Euclidean distance, the centroid of a fixed cluster is its arithmetic mean; the assignment step chooses the closest centroid. Alternating assignment and centroid update does not increase the objective when implemented exactly, yet it can converge to different local optima from different initializations. A low inertia value does not demonstrate that clusters correspond to real social or biological categories.

K-means tends to favor roughly spherical clusters under its Euclidean loss. Elongated curved patterns, density variation and outliers challenge this geometry. Standardization matters because squaring distances magnifies large-scale coordinates. Alternative methods include hierarchical agglomeration, density-based clustering and Gaussian mixture models. Each brings its own definitions of neighborhood and cluster membership. A Gaussian mixture yields soft posterior assignments under model assumptions; k-means does not become probabilistic simply because its centroids are displayed as colored points.

Select the number of groups using task value, stability, internal criteria and independent context. Silhouette scores compare within-group distance with nearest alternative groups, but can favor geometric separation unrelated to the intended application. Cluster IDs have no inherent ordering and may switch when a model is refit. Operational systems require a versioned mapping from discovered clusters to downstream actions.

### Two-step example
Four one-dimensional observations are 0,2,8,10. For K=2, initialize centroids at 0 and 10. Assignment gives clusters {0,2} and {8,10}, whose updated centroids are 1 and 9. The within-cluster sum of squares is (0-1)²+(2-1)²+(8-9)²+(10-9)²=4. With K=1, centroid 5 gives squared total 25+9+9+25=68. The lower objective for K=2 partly reflects added capacity; it is not a reason to increase K without penalty forever.

### K-means initialization and empty-cluster handling
A k-means implementation must define what happens if a cluster receives no assigned observations. Leaving the centroid as NaN can corrupt all later distances; silently dropping the cluster changes K; reinitializing it to a well-chosen observation is a common fallback, but the resulting algorithm is not exactly the same as the basic theoretical alternating scheme. Multiple initializations reduce sensitivity to one poor starting configuration. K-means++ samples new centers with probability proportional to squared distance from existing centers, providing a structured initialization rather than purely uniform random seeds. Test on a dataset containing duplicated points and K larger than the number of distinct coordinates: some requested partitions may be degenerate. Record the resulting effective clusters. A software implementation that always returns K nonempty clusters cannot satisfy that claim on data with too few distinct points without additional conventions.

## Dimension Reduction
### Dimension Reduction

### Dimension reduction separates compression from explanation
Principal component analysis identifies orthogonal directions of maximum sample variance after centering. If X is centered, eigenvectors of X^T X or right singular vectors from SVD define principal directions. The first component maximizes projected variance subject to unit length; subsequent components are orthogonal to earlier ones. Explained variance is a fraction of measured sample variation, not a percentage of meaningful scientific information preserved. A low-variance direction can still carry a rare class boundary or safety-critical anomaly.

Feature scaling changes PCA when variables have different physical units. An unscaled sensor in thousands of units may dominate a biological marker measured near one. Standardizing columns corresponds to an analysis of correlations rather than raw covariance. The choice should follow the scientific question. PCA is linear: two points close in a curved latent manifold may not remain close under an extreme linear projection, and clusters in a two-dimensional plot can be projection artifacts.

Nonlinear embeddings such as t-SNE and UMAP can support exploratory visualization but do not automatically preserve global distances or cluster sizes. Hyperparameters and random seeds matter. It is particularly dangerous to fit an unsupervised reduction on all data before cross-validation if the method is used inside a predictive pipeline: test distribution information enters feature construction. Fit the transform within each training fold and report component retention honestly.

### Covariance example
Consider centered points (-1,-1), (0,0), (1,1). Sample covariance is [[1,1],[1,1]], with eigenvalues 2 and 0. Principal direction (1,1)/sqrt(2) captures all observed variance, while the orthogonal direction has none. Adding a tiny second-coordinate measurement error makes the second eigenvalue positive, and the proportion changes. This exact toy example is not evidence that a high-dimensional observational dataset truly lies on one noise-free line.

### PCA sign ambiguity and nearly tied directions
An eigenvector is not unique in sign: v and -v represent the same principal axis. If a plotting tool flips the sign of a component between fitting runs, the geometry and explained variance remain identical. A sign flip must not be interpreted as a substantive change in the underlying physical factor. When two eigenvalues are nearly equal, even the direction within their two-dimensional subspace can rotate strongly after small data perturbations. Compare reconstruction error or subspace angles rather than each coefficient individually in such cases. For a downstream classifier, fit PCA inside training folds and apply the learned rotation and centering to held-out data. Fitting the rotation on all observations, even without labels, can bias the evaluation of future distribution generalization. The diagnostic question is whether the reduction preserves information needed by the downstream task, not whether the first two axes look aesthetically separated.

## Density Estimation
### Density Estimation

### Density estimation assigns likelihood under a model
A density describes relative probability per unit volume for continuous observations. The probability of an exact real-valued measurement is zero in standard continuous models, while probability over an interval is an integral of density. Histograms approximate local mass with bins, kernel density estimators smooth observations, and parametric families impose shapes with a small number of parameters. Choosing bandwidth is critical: a tiny kernel width makes a spiky estimate, while a large bandwidth blurs important modes.

For a Gaussian kernel in one dimension, fhat_h(x)=1/(nh) sum_i phi((x-x_i)/h), where phi is the standard normal density. The 1/h normalization ensures each kernel integrates to one. Density values can exceed one when the distribution is concentrated in a narrow interval; this is not a violation because a density is not itself a probability. In multiple dimensions, the bandwidth volume factor becomes h^d, and the number of observations needed for reliable local estimation can grow rapidly with dimension.

A fitted likelihood is not automatically a calibrated anomaly score for business decisions. Complex generative models can assign high density to unimportant easy-to-model patterns and low density to legitimate but rare cases. An anomaly policy should be evaluated against operational harm, not just negative log likelihood. Heavy-tailed data and irregular support make Gaussian approximations fragile. Check boundary bias when measurements are nonnegative or constrained to a simplex.

### Histogram versus kernel lab
Sample values 0,0,1,1,2,8 include one distant measurement. A histogram using bins of width one highlights concentrated mass near zero; a Gaussian KDE spreads some density into negative values even though the measured quantity might be intrinsically nonnegative. Compare bandwidth 0.2,1 and 3. Normalize each estimated curve numerically on a sufficiently wide grid and discuss truncated integration error. If density is used for anomaly alerts, explicitly test the false-alert rate on independent data from a known normal operating regime.

### Density bandwidth as a bias-variance control
For a kernel density estimator, bandwidth changes the effective number of observations influencing each query. Too little bandwidth yields many narrow peaks centered near training points; too much bandwidth washes out distinct modes. Cross-validated likelihood can guide bandwidth, but its target is predictive density under an assumed sampling distribution, not necessarily downstream anomaly alert utility. In a boundary-constrained domain, an unconstrained Gaussian kernel assigns density outside physical support. Test whether reflection or log transformation changes false-alarm behavior near zero. A practical experiment synthesizes a mixture of two normal components, fits KDEs over a grid of bandwidths, and reports integrated squared error against the known generating density. Only synthetic examples have a known ground-truth density; for field measurements, evaluation requires careful held-out likelihood or task-specific labels. Do not infer a density curve's scientific validity from visual smoothness.

## Representation Learning
### Representation Learning

### Representation learning seeks reusable transformations
A learned representation maps an observation to an embedding that makes relevant structure easier to use. An autoencoder trains an encoder z=g(x) and decoder xhat=h(z), often minimizing reconstruction loss. Without a bottleneck, regularization or other constraint, a sufficiently flexible autoencoder can learn an identity map that offers little useful abstraction. Low reconstruction error therefore does not prove the embedding captures semantic or causal factors. The reconstruction objective determines what the model treats as important.

Contrastive learning trains embeddings so that specified positive pairs are closer than selected negatives under a similarity rule. Defining positive pairs is an assumption about invariance: two augmented photographs of the same object may share identity but differ in lighting, while two medical scans of the same patient at different times may differ in clinically meaningful ways. An augmentation safe for retail product photos can be harmful for tumor-detection images. The representation inherits those choices and the composition of available negative examples.

Embeddings can enable search, retrieval and transfer to data-scarce tasks. Evaluate them using independent downstream tasks, robustness to expected transformations, coverage across populations and computational cost. Cosine similarity removes vector magnitude, so it may be appropriate when orientation matters but magnitude does not. Nearest-neighbor retrieval of an embedding must still respect permissions and data privacy; similarity is not an access-control mechanism.

### Applied test
Encode short sensor windows and test whether nearest neighbors share machine type or fault category. Build positive pairs from nonoverlapping augmentations of the same stable operating interval; do not accidentally pair a pre-fault and post-fault window as equivalent. Probe whether embeddings predict device identity more accurately than fault state. Such a result may indicate a shortcut. An ablation removing device-specific metadata can reveal whether the objective learned transferable dynamics or simply memorized hardware signatures.

### Embedding collapse and contrastive shortcuts
Contrastive objectives can fail when every example maps to nearly the same embedding, although many loss constructions include negatives or other constraints to discourage trivial collapse. Some systems avoid collapse without explicit negative pairs through architectural asymmetry, stop-gradient operations or variance regularization; these details change the actual objective. Embedding collapse can be diagnosed by inspecting variance across dimensions and pairwise distances on held-out examples. Even a noncollapsed embedding may capture shortcuts, such as camera identity or watermark appearance. Test retrieval under interventions that remove irrelevant background details while preserving the target object. For a device-failure task, compare same-device different-state pairs with different-device same-state pairs. If model similarity follows device identity instead of fault state, the learned representation may not transfer to new machines. A retrieval demonstration should state what labels or judgments validate relevance rather than presenting neighbors as self-evidently correct.

## Integrated technical investigations and review
# Integrated investigation for Unsupervised methods

### What a cluster assignment means, and what it cannot mean
Unsupervised clusters are defined by a selected objective and measurement geometry. Consider a customer dataset with purchase amount, purchase frequency and region. K-means on raw features may mostly separate spending magnitude; on z-scored features it may divide frequency and region more strongly. Neither partition is an objective discovery of immutable customer types. A downstream marketing claim that one cluster contains 'loyal' customers requires independent evidence about behavior, not merely a low within-cluster squared distance.

A useful stability audit repeats clustering across resampled customers, alternative scales and plausible hyperparameters. Because cluster labels can permute between runs, match groups by overlap or a suitable assignment algorithm before measuring agreement. Report instability particularly for observations near cluster boundaries. A cluster whose membership changes drastically under tiny measurement noise should not control irreversible individual decisions without safeguards.

### Covariance, whitening, and component selection
PCA can be computed from a centered data matrix using its singular-value decomposition, which is numerically preferable to explicitly constructing a covariance matrix in many settings. If singular values are s_j for n observations, corresponding sample covariance eigenvalues are s_j²/(n-1). Retaining the first k directions captures the sum of their eigenvalues divided by total observed variance. This is an exact sample geometry fact; interpreting components as scientific latent causes requires a separate argument.

Whitening scales projected coordinates by inverse component standard deviations, giving approximately unit variance in retained components. It can help distance-based methods when correlations dominate, but it may amplify small noisy directions if tiny eigenvalues are inverted. Add a regularizing floor in practical whitening and state it. A PCA representation may also be unstable under near-equal eigenvalues: small perturbations can rotate the corresponding eigenvectors substantially without changing the useful subspace much.

### Estimating density near a physical boundary
Kernel density estimation over nonnegative variables illustrates how mathematical convenience creates model mismatch. A Gaussian kernel centered near zero puts positive mass at negative x values. If measurements represent rainfall, negative rainfall is impossible. Reflection methods or boundary-aware kernels can reduce this bias, but the best choice depends on the scientific measurement and evaluation purpose. Another response is modeling a transformed variable such as log(x) where x>0, adjusting for the Jacobian when translating densities back to the original units.

In anomaly screening, define the false-alarm burden on known normal cases and evaluate separately on true faults where reliable labels exist. Fitting a flexible density to training data and ranking by low density does not establish causal defect detection. Rare but valid operation regimes can be systematically penalized. Build an explicit benchmark with separate rare-valid and faulty groups, and report their alert rates rather than just global likelihood.

### Latent variable identifiability
Representation learning often infers features that are predictive without being uniquely interpretable. Rotating the coordinates of a latent embedding can preserve pairwise relationships or reconstruction quality while changing the apparent meaning of individual axes. Two equally useful autoencoders can assign different latent directions to physical factors. A chart labeling 'latent dimension 1' as 'maintenance need' may therefore be unjustified unless independent tests establish the correspondence. Similarly, a latent code that predicts device ID can look compact and structured without capturing the intended failure mechanism.

Contrastive positive-pair selection is another scientific hypothesis. Two consecutive image frames may share scene content but not a transient fault. If augmentation erases a hairline crack, the model is explicitly trained to be invariant to a safety-critical signal. Audit augmentations by examining affected labels and have domain specialists verify representative transformed examples. A plausible self-supervised task is not automatically a valid objective for a particular downstream use.

### Generative versus discriminative evaluation
A density estimator can sample plausible observations or estimate relative likelihoods; a classifier predicts a target conditional on observations. Good generative likelihood does not guarantee good discrimination, and strong discrimination does not guarantee a faithful joint model. Evaluate the properties directly relevant to deployment. If the purpose is synthetic data, assess privacy leakage, coverage of rare modes, and whether synthetic samples introduce misleading correlations. A model that produces attractive typical examples can omit critical rare failures while still receiving favorable visual reviews.

For an integrated project, split data by independent collection batches, fit unsupervised transformations on training batches, and freeze the transformations before test scoring. Provide original and projected representations, cluster stability measurements and explicit cases where visualization creates false impressions. The conclusions should refer to descriptive organization, not objective discovery of categories or causes.

### Interpretability must match the causal question
A low-dimensional projection, density curve or cluster assignment summarizes measured associations. It does not identify the effect of intervening on a source variable. If users interpret clusters as stable personal types, misclassification can have durable consequences. When a representation is used for a decision, define how errors affect people and how decisions can be appealed or reviewed. Assess stability under benign measurement variation; if a tiny perturbation changes an expensive intervention, the downstream policy may require smoothing or abstention. Visualization axes may rotate or flip without changing the underlying model, so narrative labels require external verification. A rigorous report includes counterexamples in which geometry and domain meaning disagree. These counterexamples often teach more than a perfectly separated colored scatterplot. The value of unsupervised learning comes from a well-defined downstream use, a reproducible representation and an honest account of the assumptions connecting the two.

### Worked question: K-means objective
Four scalar observations are 0,2,8,10. For K=2 and clusters {0,2},{8,10}, compute centroids and total within-cluster squared error.

**Model the question**
The centroid minimizing squared error within each fixed cluster is its arithmetic mean. Therefore first centroid is one and second centroid is nine.

**Calculate or derive**
Squared distances to centroid 1 are 1 and 1; squared distances to centroid 9 are also 1 and 1. Total within-cluster sum of squares is 4. With K=1, centroid is 5 and total squared error is 25+9+9+25=68.

**Check assumptions and boundaries**
A smaller K-means objective is partly achieved by increasing K; K=4 would fit every data point exactly. Choosing K requires a separate criterion such as stability or domain usefulness. K-means also does not directly validate whether these are naturally occurring categories.

**Answer:** Centroids are 1 and 9, with within-cluster sum of squares 4.

### Worked question: PCA covariance eigenvalues
Centered two-dimensional observations lie at (-1,-1),(0,0),(1,1). Use sample covariance with denominator n-1 and find eigenvalues and the leading unit principal direction.

**Model the question**
The matrix X has columns with identical centered values. The sum of squares in either coordinate is 1+0+1=2; dividing by 2 gives variance one. Cross-product sum is also two, giving covariance one.

**Calculate or derive**
The covariance matrix is [[1,1],[1,1]]. Its eigenvalues are 2 and 0 because rows are identical and trace is two. The leading unit eigenvector is (1,1)/sqrt(2); the orthogonal direction is (1,-1)/sqrt(2).

**Check assumptions and boundaries**
All sample variance lies along one line in this constructed example. For noisy real measurements, the second eigenvalue will often be nonzero. PCA maximizes sample variance, not necessarily supervised signal or causal importance.

**Answer:** Eigenvalues 2 and 0; first principal direction (1,1)/sqrt(2).

### Worked question: Gaussian density mass
Let X have density f(x)=1/sqrt(2pi) exp(-x^2/2). Is f(0) the probability that X exactly equals zero? Estimate the probability of falling in a very narrow interval [-0.01,0.01].

**Model the question**
For a continuous variable, the probability of any exact point is zero. Density at zero is 1/sqrt(2pi)≈0.398942 per unit of x, not a point probability.

**Calculate or derive**
For a sufficiently narrow interval, approximate probability by width times near-constant density: .02×.398942≈.00797884. A more accurate value integrates the density or uses normal CDF values; the rectangle approximation has a small error because the curve is smooth near zero.

**Check assumptions and boundaries**
Changing x units changes numerical density by a Jacobian factor without changing probability mass. This illustrates why comparing likelihood magnitudes across different data representations requires care.

**Answer:** P(X=0)=0; P(-.01≤X≤.01)≈0.007979 by local-density approximation.
