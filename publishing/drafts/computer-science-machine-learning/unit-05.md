# Unit 5: Neural models

*Editorial draft; not approved for live publication.*

## Backpropagation
### Backpropagation

### Backpropagation is efficient application of the chain rule
A feedforward neural network composes functions. For two layers, h=phi(W1 x+b1) and yhat=W2 h+b2. Given a scalar loss L(yhat,y), the chain rule propagates gradients backward through the computational graph. Reverse-mode automatic differentiation computes derivatives of a scalar output with respect to many parameters more efficiently than separately perturbing each parameter. The gradients remain mathematical derivatives of the implemented operations; they do not guarantee the intended learning objective is well chosen.

For a scalar example h=ReLU(wx), prediction yhat=vh and loss (yhat-y)²/2, the derivative with respect to w is (yhat-y)v x when wx>0, and zero when wx<0. At wx=0 the ReLU derivative is not unique and software chooses a subgradient convention. Dead ReLU units occur when preactivations remain negative for many examples, preventing gradients from changing the upstream weights through those examples. Alternative activations have different saturation and computational characteristics.

Gradient checking uses central differences [L(theta+epsilon)-L(theta-epsilon)]/(2epsilon) on small deterministic problems. Very small epsilon causes floating-point cancellation; very large epsilon makes truncation error noticeable. Disable stochastic dropout and fix seeds during the check. Compare relative error with an appropriate scale and inspect individual parameters. A passing check establishes agreement between two implementations of the specified finite computation, not that the model generalizes.

### Chain-rule trace
Let x=2,w=1,v=3,y=4. Then h=ReLU(2)=2, yhat=6, residual 2 and L=2. Derivative dL/dv=(6-4)×2=4; derivative dL/dw=(6-4)×3×2=12. With eta=.01, simultaneous updates are v=2.96 and w=.88. Recompute prediction 2.96×ReLU(1.76)=5.2096 and loss approximately .73157. A step can decrease this example's loss, but no single demonstration guarantees convergence elsewhere.

### Automatic differentiation versus finite-difference checking
Automatic differentiation propagates derivatives of program operations, whereas finite differences estimate sensitivity by repeated evaluations. Agreement is a powerful implementation test when the function is smooth in the neighborhood, but a central finite-difference approximation can disagree near ReLU kinks or numerical discontinuities without proving either implementation wrong. Select parameter values away from known nondifferentiable points and choose step epsilon relative to parameter scale. Validate loss reduction for a small gradient step as a second, weaker sanity check; a finite-difference gradient can be correct while loss still increases under an overly large learning rate. Trace gradient shapes as carefully as numeric values: broadcasting a scalar across a matrix can silently produce an output with the wrong reduction semantics. Check whether gradients are summed or averaged across minibatches so that learning-rate settings have interpretable meaning.

## Network Architectures
### Network Architectures

### Architecture is a statement about useful inductive structure
A dense network connects every input coordinate to many hidden units. A convolutional network shares filters across spatial positions and assumes local patterns can recur, a useful bias for images or structured signals. Recurrent models share an update across time and can retain state, but long-range dependencies may strain gradient propagation. Transformer attention allows direct interactions among positions, while full attention often requires quadratic pairwise score storage in sequence length. Architectural choices affect expressivity, data efficiency, memory and deployment constraints.

A convolution with input width W, kernel K, padding P and stride S has output width floor((W+2P-K)/S)+1 under the conventional discrete formula when dimensions are valid. For W=7,K=3,P=0,S=2, output width is 3. The number of output channels is set by filter count, not implied by that spatial formula. Shared weights reduce parameters compared with unstructured dense connections, but spatial invariance is not perfect: pooling, padding and borders can produce position sensitivity.

Attention weights arise by softmax-normalizing query-key scores, often scaled by inverse square root of key dimension. These weights indicate one layer's information mixing and should not automatically be interpreted as faithful causal explanations of model predictions. A network can use attention patterns that change with equivalent internal parameterization. When privacy, memory or real-time latency matters, compare smaller architectures and compression techniques with full models rather than assuming the largest network is the only serious baseline.

### Architecture lab
For sequence length n=100, a dense attention score matrix has 10,000 entries per head before batching; doubling n to 200 produces 40,000. Calculate actual memory only after specifying numeric precision, batch size, head count and whether activations are saved for backward propagation. Benchmark wall-clock latency and peak memory on the target device; an O(n²) formula is not a complete hardware performance model.

### Parameter sharing and boundary effects
Convolutional filters reuse coefficients at many spatial positions, creating a translation-related inductive bias. Yet padding changes what a filter sees at image borders; zero padding introduces a special artificial boundary that may influence predictions. Compare an object centered in an image with the same object shifted close to the edge. A convolutional model may respond differently, particularly after pooling, striding or cropping. In sequence attention, position encodings likewise supply order information that pure content-based similarity lacks. Ablate positional information in a synthetic sequence task that distinguishes AB from BA; without a representation of order, a permutation-invariant system cannot separate those examples. An architecture should be assessed by the invariances it encodes and the distinctions it can represent. Model capacity alone does not establish suitability for data whose structure is spatial, temporal or relational.

## Optimization
### Optimization

### Optimizing networks requires separating training dynamics from results
Minibatch training estimates a gradient from a subset of observations. Choosing the minibatch size affects noise, device utilization and the number of updates per epoch. Momentum carries a running direction across updates; adaptive methods rescale individual parameter steps using historical gradient statistics. Their exact behavior depends on epsilon constants, decay conventions, bias correction and weight decay implementation. Reproducing a paper requires recording these settings rather than just writing the optimizer name.

A learning-rate schedule may warm up, remain constant, decay at milestones or respond to validation plateaus. Warmup can reduce unstable early updates in some large models, but unnecessary scheduling can complicate a simple task. Gradient accumulation simulates a larger effective batch for some computations while potentially changing behavior of batch-dependent operations. Mixed-precision arithmetic saves memory or increases throughput on suitable hardware but introduces rounding and overflow considerations. Dynamic loss scaling is one technique for handling small gradients with limited numeric range.

Training loss, validation loss and calibration can evolve differently. A network may keep lowering training cross-entropy after its validation cross-entropy has stopped improving. Choose a stopping rule using a validation subset and preserve an untouched test set. Compare seeds where training is stochastic; variance across seeds can exceed the advertised performance improvement of a tuning trick. Runtime cost and energy usage are legitimate evaluation dimensions in a deployable product.

### Gradient noise demonstration
For two single-example gradients g1=2 and g2=6, the full mean gradient is 4. A batch containing only one randomly chosen example has gradient 2 or 6 with equal probability, so its expectation is 4 and its variance about the mean is 4. Averaging both examples removes that sampling variance for this fixed dataset. This does not mean stochastic optimization is always slower; cheaper and more frequent updates can make a small batch effective in wall-clock time. Separate gradient variance from optimizer progress.

### Learning-rate schedules and stateful optimizers
Momentum updates depend on historical gradients, so two training runs with identical current parameters but different optimizer states can move differently on the next batch. To resume training accurately, store and restore optimizer momentum, step count and scheduler position as well as weights. Adam's bias correction uses the step counter; resetting it changes effective update magnitudes. Compare two checkpoint resumes: one complete, one weights-only. If their future loss trajectories differ, the difference is expected and should be explained rather than attributed to random noise without investigation. For controlled optimization comparisons, hold data order, initialization and total update budget fixed. An optimizer that completes fewer updates but uses fewer seconds may still be preferable in production; report both update efficiency and elapsed computation. Early stopping must monitor a metric from a held-out set not simultaneously used to compute parameter gradients.

## Regularization
### Regularization

### Neural regularization can help or hide a representation defect
Weight decay penalizes parameter magnitude under a specified update rule. Dropout randomly masks activations during training and applies an expectation-preserving scaling convention; evaluation uses deterministic activations in standard implementations. Early stopping limits training time based on validation outcomes. Data augmentation expands observed transformations to which the learner is encouraged to become insensitive. None is a substitute for properly labeled data or an evaluation split that reflects the deployment task.

Suppose a medical image classifier uses random horizontal flips. For one anatomical finding, a flip may preserve disease identity; for a laterality-specific label, it may reverse clinical meaning. The augmentation must respect label invariance. Similarly, mixup interpolates inputs and labels and assumes the resulting synthetic examples provide useful smoothness; this can fail when the data manifold has strict physical boundaries or discrete symbolic constraints. An augmentation should be defended by domain knowledge or controlled evidence rather than by a leaderboard convention.

Regularization strength and model capacity interact. Strong weight decay may underfit; too little can allow unstable high-magnitude parameters. Dropout near an output layer can change calibration and convergence behavior. Batch normalization computes statistics from training minibatches and maintains evaluation estimates; a distribution shift can make those estimates stale. In small or non-i.i.d. batches, other normalization approaches may be more appropriate. Report the exact train and inference modes of every layer.

### Controlled ablation
Train four otherwise identical small networks: baseline, with mild weight decay, with dropout, and with augmentation. Hold dataset split, parameter budget and seed list fixed. Evaluate each across several seeds rather than cherry-picking the best run. Record both loss and an error analysis by subgroup. If augmentation improves average accuracy but damages a clinically critical minority case, the evaluation should show that failure explicitly instead of promoting the method as universally beneficial.

### Data augmentation as an invariance claim
Every augmentation says that two modified inputs should share a label or a representation relationship. Random crop for a street-scene classifier can remove the very object that determines a positive label; horizontal flip can change traffic-sign meaning in some settings; aggressive frequency filtering may erase a fault signature in vibration data. Build a transformation audit by sampling original and augmented pairs for each class. Record which labels survive, which become ambiguous and which should be excluded. In supervised learning, measure class-specific changes in error and calibration after augmentation. A higher average validation accuracy can hide deterioration of rare high-cost cases. Augmentation should be applied only within the training pipeline; leaking augmented versions of a single original across train and test invalidates independence. Match the augmentation distribution to plausible deployment changes rather than to arbitrary visual variety.

## Integrated technical investigations and review
# Integrated investigation for Neural models

### Numerical stability across a deep computational graph
Backpropagation is exact differentiation of the implemented graph to floating-point precision, but composing many operations can amplify or attenuate gradients. A deep chain of derivatives with magnitudes below one tends to shrink the gradient; a chain of magnitudes above one can grow dramatically. Residual connections create additional gradient paths, normalization changes activation distributions and initialization controls early signal scale. These techniques address concrete numerical behavior; they are not substitutes for a sensible dataset or objective.

A gradient norm can be monitored across network layers during training. If every early-layer norm is nearly zero while late-layer norms are substantial, investigate saturation, initialization or architectural bottlenecks. Clipping can limit very large updates, but it does not restore information lost by a saturating activation. Adjustments must be evaluated with fixed controls because simultaneous changes to learning rate, activation, depth and data augmentation prevent causal interpretation of the improvement.

### Calibration and selective prediction
Deep classifiers often output scores converted by softmax into normalized probabilities. Softmax normalization ensures nonnegative values summing to one, but does not guarantee calibrated frequencies. Temperature scaling divides logits by positive temperature T before softmax; T>1 generally softens probabilities while preserving class ordering for fixed logits, whereas T<1 sharpens them. Fit T on independent calibration data and evaluate on another holdout. If class distributions change later, the original temperature can become inappropriate.

Selective prediction introduces an abstention region. For example, an image review service may automatically accept cases only when the calibrated top-class probability exceeds a high threshold, routing the rest to experts. Evaluate error rate among accepted cases together with coverage (the fraction accepted), workload, and group-specific abstention. A trivial system abstaining on every case has low accepted-case error but no utility. Both axes are required for a fair comparison.

### Computational costs and deployment footprint
Parameter count is not the same as memory consumed during training. Optimizers can store momentum and second-moment arrays in addition to parameters, and reverse-mode differentiation retains or recomputes intermediate activations. A nominal 100-million-parameter model at four bytes per parameter occupies about 400 MB for weights alone, but the training footprint can be multiple times larger depending on precision, optimizer and batch activations. A report should measure actual peak memory rather than infer all resource costs from weight count.

Full attention's n² score-matrix count similarly does not specify total wall-clock time. Fused kernels, sparsity, memory-efficient attention and hardware-specific implementation change the effective cost. Compare latency at the expected sequence lengths and batch sizes, including long-tail inputs. A network trained efficiently on a desktop GPU may be infeasible for low-power edge hardware even when its averaged validation accuracy is excellent.

### Generalization under limited labels
Deep networks can memorize random labels on finite datasets, so training accuracy alone is weak evidence of learned structure. Evaluate held-out entities and conditions; augmentations should model physically meaningful invariances. Learning curves show how performance changes with data volume but do not automatically reveal a true irreducible limit. Domain shift can dominate architecture choice: changing camera exposure or sensor firmware may degrade a large model as much as a small one. When labels are scarce, transfer learning can be effective, but pretrained data sources and licenses must be considered.

A useful test freezes a pretrained encoder and trains a simple linear head, then compares with partial fine-tuning and full fine-tuning. Report all three under the same split and computational budget. If full fine-tuning wins only on the training fold, the simpler approach may generalize better. Inspect rare-class errors and calibrated uncertainty rather than declaring the largest network best by default.

### Fault-tolerant training and artifacts
Long experiments require reproducibility beyond saving weights at the end. A checkpoint may need model parameters, optimizer statistics, learning-rate scheduler state, random number generator states and preprocessing versions. Resuming with a new optimizer state can change the trajectory even when the model weights match. If exact reproducibility is impossible across hardware kernels, document tolerances and expected nondeterminism rather than promising bitwise identity.

Before publishing a checkpoint, run input-schema tests, deterministic reference predictions, numeric-output finiteness checks, adverse-input tests and license review. A gradient check in a tiny deterministic network validates implementation algebra; an independently labeled test evaluates predictive performance; operational monitoring evaluates service behavior. These are complementary evidence layers and should never be substituted for one another.

### Training correctness and safety correctness are different
A neural network can satisfy every gradient check and still be unfit for deployment. Gradient checks show that implemented derivatives match a local finite-difference oracle; held-out metrics estimate prediction performance on sampled data; robustness tests study defined perturbations; and safety reviews assess decisions and failure consequences. None substitutes for the others. An image model with perfect numerical gradients can learn a watermark shortcut if labels correlate with camera source. A model with high average recall can still miss every observation from a rare hazardous condition. Build separate acceptance gates: deterministic computational correctness, statistical generalization, input contract validity, latency under expected load, and domain-specific action constraints. Treat a failure at any critical gate as a reason to revise the model or its intended scope. Clear separation of claims prevents a visually impressive training curve from being marketed as a complete safety argument.

### Worked question: Two-layer backpropagation
Let h=ReLU(wx), yhat=v h, L=(yhat-y)^2/2 for x=2,w=1,v=3,y=4. Find dL/dw and dL/dv.

**Model the question**
The hidden preactivation wx equals two, so ReLU is active with derivative one. Hidden activation is two, prediction is six, and residual is two.

**Calculate or derive**
dL/dv=(yhat-y)h=2×2=4. For w, apply chain rule through v and ReLU: dL/dw=(yhat-y)v×1×x=2×3×2=12. The objective value is 2.

**Check assumptions and boundaries**
At a negative preactivation, ReLU derivative is zero for ordinary implementations; at exactly zero a subgradient convention is needed. A central finite-difference check with small epsilon can confirm these derivatives away from the kink.

**Answer:** dL/dw=12 and dL/dv=4.

### Worked question: Convolution output dimensions
An image has spatial width and height 7. A convolutional kernel has side length 3, padding 0 and stride 2. Calculate the output spatial dimensions.

**Model the question**
For each spatial axis use floor((W+2P-K)/S)+1, assuming the kernel fits at least once and no dilation is used.

**Calculate or derive**
Substitute W=7,P=0,K=3,S=2 to obtain floor((7-3)/2)+1=floor(2)+1=3. The output therefore contains a 3×3 grid of spatial positions.

**Check assumptions and boundaries**
This does not determine the number of output channels: that depends on the number of filters. Changing padding to one yields floor((7+2-3)/2)+1=4 positions per axis, or 4×4 spatial output.

**Answer:** The output spatial dimensions are 3×3, excluding channel count.

### Worked question: Minibatch gradient variability
A tiny dataset produces scalar example gradients 2 and 6. If one example is sampled uniformly at random for a batch of size one, compute expected gradient and variance; compare with the two-example full batch.

**Model the question**
The random minibatch gradient G is two with probability .5 and six with probability .5. Its expectation is .5×2+.5×6=4.

**Calculate or derive**
Variance is .5(2-4)^2+.5(6-4)^2=.5×4+.5×4=4. The full-batch gradient is the deterministic average (2+6)/2=4 on this fixed two-example dataset, with no sampling variance under this comparison.

**Check assumptions and boundaries**
The full batch may be more expensive to compute per update. Less stochastic noise does not necessarily imply faster progress per second; optimizer stability and device performance also matter. Sampling without replacement requires care in a larger derivation.

**Answer:** Single-example estimator has mean 4 and variance 4; full two-example gradient equals 4 deterministically.
