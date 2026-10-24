# Algorithms — Unit 8: Randomized algorithms


## Probabilistic Analysis

**Core model — Probabilistic Analysis**

Randomized analysis treats a sample of the algorithm's random choices as part of the model. State what is random and whether guarantees are in expectation, with high probability, or absolute.

**Original worked illustration**

For a uniform pivot in quicksort on n distinct values, the worst-case quadratic split is possible, but the expected number of comparisons is Theta(n log n).

**Boundary conditions and checks**

Do not equate 'randomized' with secure randomness; pseudorandom generators are reproducible and may be predictable to adversaries.

**Connections in this unit**

The adjacent subjects are Hashing, Sampling, Randomized Optimization. They are studied alongside Probabilistic Analysis because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Randomized algorithm analysis treats internal random choices as part of the computational model, but the probability space must be explicit. In a Las Vegas algorithm the returned answer is always correct while running time is random. In a Monte Carlo algorithm running time may be controlled while a small error probability remains. Expected runtime does not guarantee every individual execution finishes near the expectation. Concentration inequalities can bound deviations under stated assumptions, and independent random trials may reduce failure probability when independence actually holds. A deterministic pseudorandom generator with a fixed seed provides reproducibility for testing, not true physical randomness.

### Derivation and worked trace

Randomized quicksort chooses a pivot uniformly among the current subarray's elements. For any pair of keys in their sorted rank order, they are compared only if one of the pair is chosen as pivot before a key between them; this event has probability 2/(j-i+1) for ranks i<j. Summing these probabilities across pairs gives an expected comparison count O(n log n). That proof does not say a randomly chosen pivot always splits in half. On a particular unlucky sequence, every pivot could be extreme, producing quadratic comparisons. Repeated randomized trials should report distribution and percentile counts, not just one attractive run.

### Counterexample and failure diagnosis

Probability calculations require attention to conditioning. If an experiment stops at the first success, sample length is a random variable correlated with the observed outcomes. Multiplying marginal probabilities without independence is invalid. When experiments reuse correlated pseudorandom values or share a mutable random generator across threads, the independence model may not match the implementation. For deterministic tests, compare a seeded implementation against an independent mathematical oracle rather than asserting that the same seed produced the same number twice.

### Applications, engineering constraints and validation

Randomized algorithms are valuable in huge datasets, numerical integration, load balancing and optimization, but they can be vulnerable to adversarial input or manipulated hash collisions. Engineering choices include seeding policy, entropy quality, reproducibility, error tolerance and worst-case fallback. Record failure probabilities in clear units; for a Monte Carlo estimator, statistical uncertainty decreases with sample size rather than disappearing at a fixed threshold. The simulation should explain which random generator it uses and which model assumptions cannot be tested by the displayed plot.

## Hashing

**Core model — Hashing**

Hash functions distribute keys into a finite table. For uniform hashing the expected chain length is related to load factor alpha=n/m; collisions cannot be ruled out for a larger key universe.

**Original worked illustration**

Placing n=12 keys into m=6 buckets gives load factor 2. Under a simple uniform-hashing model a successful operation sees a small average chain even though particular collisions are possible.

**Boundary conditions and checks**

A fixed modulo hash against adversarial keys like multiples of m can produce chains of length n. Open addressing degrades sharply at high occupancy.

**Connections in this unit**

The adjacent subjects are Probabilistic Analysis, Sampling, Randomized Optimization. They are studied alongside Hashing because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Hash tables map keys to buckets and use a collision strategy to store distinct keys mapping to the same bucket. Expected constant-time lookup under suitable assumptions is not an unconditional worst-case guarantee. Open addressing probes alternative slots within the table; separate chaining stores multiple records in a bucket. Load factor, hash-family properties, deletion markers, key equality and resize policy all affect behavior. A robust implementation must preserve the invariant that every inserted key is discoverable by the same probe sequence used during lookup.

### Derivation and worked trace

Use table size seven and hash h(k)=k mod 7. The keys 10,17,24 all begin at bucket three. Under linear probing, they occupy slots three, four and five if the table is initially empty. Searching for 24 must inspect slots three, four and five before success, even though its nominal hash bucket is three. Deleting 17 by turning slot four into an empty-never-used marker would make a naïve search for 24 stop early. A tombstone or suitable reinsertion strategy is required to preserve probe continuity. This demonstrates why deletion is harder than insertion in many open-addressed tables.

### Counterexample and failure diagnosis

Uniform-hashing assumptions provide expected-case bounds but may be violated by adversarial keys or predictable hash functions. Cryptographic hash functions, keyed hash functions and randomized seeds serve different purposes; a cryptographic hash does not automatically solve table resizing or memory exhaustion. Collision chains can be long even when average load is modest if hash outputs cluster. Measure the actual distribution of probe lengths, including the tail, and test all-equal hashes as an adversarial case. Equality and hash consistency require that equal keys always produce the same hash under the same table settings.

### Applications, engineering constraints and validation

Hashing appears in caches, database indexes and compilers. A hash table is not naturally sorted, so ordered range queries usually need another structure. Rehashing all keys on capacity growth is an amortized operation and can cause latency spikes. In concurrent tables, resize and iterator safety introduce further complexity beyond the single-threaded expected-count analysis. Document object lifetime, memory overhead, lock strategy and the promised iteration semantics before relying on an asymptotic O(1) label.

## Sampling

**Core model — Sampling**

Random sampling aims to infer a property without examining the complete population. Reservoir sampling maintains an exactly uniform sample from an unknown-length stream using a decreasing replacement probability.

**Original worked illustration**

For a reservoir of size one, after observing item i replace the retained item with probability 1/i. By induction any prior item survives with probability (i-1)/i, yielding a final probability 1/i for each.

**Boundary conditions and checks**

Convenience samples and correlated observations invalidate simple independent-sampling concentration bounds; document replacement and sampling-frame assumptions.

**Connections in this unit**

The adjacent subjects are Probabilistic Analysis, Hashing, Randomized Optimization. They are studied alongside Sampling because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Sampling algorithms select representatives of a dataset, often under memory, time or streaming constraints. Uniform sampling without replacement differs from independent sampling with replacement. Reservoir sampling provides an exact uniform sample from a stream of unknown length using bounded memory. For a reservoir of size one, store the first item; on observing the ith item for i≥2, replace the stored item with probability 1/i. The resulting invariant is that after i observations each of the i items is held with probability exactly 1/i.

### Derivation and worked trace

Verify the reservoir invariant for three arrivals A,B,C. After A, A is stored with probability one. At B, replace with probability one-half, so each of A and B is stored with probability one-half. At C, replace with probability one-third: C is stored with probability one-third, while A and B each survive with probability (1/2)(2/3)=1/3. This reasoning extends inductively. A simulation may approximate those probabilities with repeated trials, but the exact proof does not rely on random experimental frequency.

### Counterexample and failure diagnosis

Sampling bias can arise before the algorithm receives any data. If a stream overrepresents one group because of collection design, perfectly uniform reservoir sampling over that stream preserves the bias relative to the intended population. Likewise choosing every tenth item is not a random sample if the source is periodic with period ten. Sampling without replacement also creates dependence among inclusion events; standard uncertainty formulas need an appropriate finite-population correction in some designs. Never infer representativeness solely from a uniformity guarantee internal to a sampler.

### Applications, engineering constraints and validation

For a larger reservoir of k items, conventional reservoir algorithms include the first k then replace randomly with suitable probabilities. A production implementation must specify behavior when fewer than k items arrive, ensure integer random sampling is unbiased enough for the application and handle backpressure. Use deterministic seeded runs for repeatability and independent chi-squared or other distribution tests over many seeds for broad statistical behavior. A single run can only establish one output, not uniformity. Distinguish data-quality validation from correctness of the selection procedure.

## Randomized Optimization

**Core model — Randomized Optimization**

Randomness may help escape local minima, estimate gradients or explore large spaces. A randomized optimization method needs a clear objective, feasible-state definition and stopping rule.

**Original worked illustration**

For a hill-climbing search over bit strings, flipping one randomly chosen bit changes at most one coordinate; accepting only improvements eventually reaches a local optimum but not necessarily a global one.

**Boundary conditions and checks**

Repeated random restarts increase the chance of exploring new basins without proving global optimality in finite time.

**Connections in this unit**

The adjacent subjects are Probabilistic Analysis, Hashing, Sampling. They are studied alongside Randomized Optimization because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Randomized optimization uses stochastic moves, samples or perturbations to navigate large search spaces where exhaustive exact search is expensive. Simulated annealing sometimes accepts a worse move with probability exp(-Delta/T) when Delta is the increase in objective and T>0 is a temperature. At high temperatures, uphill moves are more likely; as T decreases, the search increasingly favors improvement. This is a heuristic whose empirical usefulness depends on neighbor generation, temperature schedule, objective scaling and stopping criteria. The physical analogy is explanatory, not a guarantee of global optimality for arbitrary finite schedules.

### Derivation and worked trace

Suppose a solution has cost 12 and a proposed neighbor has cost 15. The uphill difference is three. At temperature T=3, the Metropolis acceptance probability is exp(-1), about 0.3679. At temperature T=1, it falls to exp(-3), about 0.0498. A proposal reducing cost from 12 to 10 is accepted with probability one under the standard minimization rule. These calculations can be independently checked in a browser slider. A fixed random seed allows two developers to reproduce the same accept/reject trace; comparing acceptance frequencies over many seeds tests the probabilistic mechanism more meaningfully.

### Counterexample and failure diagnosis

If the objective has hard feasibility constraints, randomly accepting an invalid neighbor is not necessarily allowed. A solver may reject invalid states, repair them, or attach carefully designed penalties. An incorrectly scaled penalty can make infeasible states attractive. For gradient-free local search, poor neighborhood connectivity can trap the search regardless of annealing schedule. Do not call an algorithm globally optimal because it finds the best result among its own sampled attempts. Compare to exhaustive optimum on small instances and describe the gap honestly.

### Applications, engineering constraints and validation

Optimization software should report its objective function, initialization, seed, move counts, termination rule, best-found value and reproducible configuration. For performance-sensitive settings, repeated runs provide estimates of variability and failure risk. Changing the random-number generator, data representation or floating-point platform may change trajectories, so identical seeds are not automatically a universal reproducibility guarantee. Teach students to distinguish an observed improvement from a theorem and to use exact solvers for small cases whenever possible.

## Unit 8 integrated computational laboratory

## Integrated laboratory: reliable probability and randomized computation

Randomized algorithms can be correct through a probabilistic invariant even when every run takes a different path. Consider reservoir sampling of one element from a stream. After processing i elements, the reservoir must contain each of those elements with probability 1/i. At the next item, the newcomer replaces the current sample with probability 1/(i+1). Every older item survives with probability (1/i)(i/(i+1))=1/(i+1), and the new item is selected with the same probability. This inductive proof yields exact fairness under ideal uniform random choices. Repeated experiments estimate whether an implementation behaves consistently with the theory, but cannot replace the proof.

For a stream of five items A,B,C,D,E, the first item has probability one of being stored initially, one-half of surviving the second arrival, two-thirds of surviving the third, three-fourths of surviving the fourth and four-fifths of surviving the fifth. The product is (1)(1/2)(2/3)(3/4)(4/5)=1/5. The same final inclusion probability holds for the last item E, which enters with probability 1/5. The process does not need to know the final stream length. A faulty implementation that replaces the reservoir with constant probability one-half at every arrival strongly favors recent items, violating uniformity while still producing apparently random outputs.

Now estimate the area of a quarter unit disk by generating points uniformly in the unit square. The indicator I of lying inside the disk has expectation pi/4. For N independent points, the estimator pi_hat=4(mean I) has expectation pi and variance 16p(1-p)/N where p=pi/4. The expected estimator is unbiased; its realized error does not decline monotonically with every additional sample. A single seeded run that happens to produce a poor estimate is not necessarily a broken algorithm. Test the exact code path for deterministic replay and evaluate approximate uncertainty over many independent seeds. If points are correlated, the simple independent-sample variance formula can be inappropriate.

Quicksort provides another angle. Picking pivots uniformly at random makes the expected comparison count O(n log n), but the algorithm still admits rare unbalanced partitions. If a user interface shows the average of ten trials, present it as a sample average and not as the theorem itself. Include worst observed count and a rough empirical distribution. Randomization also changes reproducibility: logging the input, algorithm version and pseudorandom seed is often necessary to explain a reported performance anomaly. Random seeds do not fix conceptual bugs in pivot partitioning or comparator transitivity.

Hash tables commonly use randomized hashing assumptions to justify expected lookup time. Insert the keys 10,17,24 into a table of size seven using h(k)=k mod 7 and linear probing. They occupy positions three, four and five. Removing 17 by marking slot four as completely empty breaks a lookup for 24 if search stops at the first empty slot. A tombstone preserves the probe chain, though too many tombstones can degrade performance and motivate rebuilding. This is a deterministic correctness failure, not a low-probability bad luck event. Distinguish hash-table invariants from the statistical analysis of collision patterns.

For randomized optimization, suppose the current cost is 20 and a proposed neighbor has cost 23. At temperature T=2, the standard annealing probability for accepting this worse move is exp(-3/2), approximately 0.2231. At T=6 it rises to exp(-1/2), about 0.6065. A better move of cost nineteen is accepted with probability one under the basic minimization rule. The rule permits escape from local minima, but a finite sequence of moves and a cooling schedule do not prove a global optimum. The acceptance formula assumes a positive temperature and a meaningful objective difference; a zero temperature must be handled by a limiting policy.

Reliability testing should combine exact and statistical checks. For reservoir sampling, verify exact inclusion probabilities mathematically and compare observed frequencies over many seeds against confidence intervals, understanding the chance of false alarms. For hashing, check invariants using adversarial collision sequences. For quicksort, compare output to a trusted sort oracle and test the expected comparison trend only over aggregated trials. For simulated annealing, verify computed acceptance probabilities and legal state transitions without claiming that a near-optimal outcome must always occur.

A publishing-quality simulation should expose initial conditions, seed control, reset semantics, the represented physical or mathematical quantity, and limits of the model. Numerical displays should not imply precise real-world timing when showing abstract operation counts. Explain how an invalid input is rejected; avoid silently clamping illegal values without telling the learner. These details turn an interactive widget from decoration into a reproducible experiment whose outcomes can be questioned, checked and improved.

### Independent audit exercise: reproducible stochastic claims

A browser simulator displaying one Monte Carlo estimate of pi should not convey false precision. Suppose it uses N=400 independent idealized samples and finds 311 quarter-disk hits. The displayed estimate is 4(311/400)=3.11. This is an observed sample statistic, not a claim that pi equals 3.11. The indicator's theoretical success probability is pi/4, and repeated estimates vary. Increasing N often reduces dispersion, but one larger-sample estimate can be farther from pi than a smaller-sample estimate by chance.

For reservoir sampling, compare exact and empirical claims. The exact probability that the final stored element is a particular stream item among ten is one-tenth under ideal uniform decisions. In 1,000 independent runs, seeing that item 95 or 108 times may be entirely consistent with the model. Demanding exactly 100 appearances would make a statistically wrong test. Instead specify an uncertainty threshold and accept that a correctly implemented random algorithm can occasionally fail a probabilistic distribution test. Reproducible seeds make the failed run debuggable, but they do not remove random variation.

A seeded generator is deterministic conditional on its seed and algorithm. For technical validation, report generator type, seed conversion, integer overflow semantics and test sequence. Two languages can disagree if one uses signed 32-bit multiplication and the other arbitrary-precision integers. A unit test that only repeats the same seed checks reproducibility; an independent reference calculation checks the specified generator state transitions. Keep those tests separate.

Randomized optimization adds another layer of uncertainty. At positive temperature T, a worse move with cost increase Delta is accepted with probability exp(-Delta/T) in the standard Metropolis rule. A test can verify the exact probability curve without expecting every individual accept/reject trial to match its probability numerically. Test Delta=0, negative Delta, large positive Delta, very small temperature, invalid temperature and a fixed seed. State when the implementation switches to a zero-temperature greedy limit to avoid division by zero.

## Worked questions and solutions

### Question 1: Probabilistic Analysis: worked application 1

Compute the expected comparison count for randomized quicksort with two distinct keys.

1. **Set up the model and conditions:** Both pivot choices lead to exactly one comparison between the keys.

2. **Carry out the calculation or proof:** Taking expectation over two equally likely pivots gives 1.

3. **State the result and its scope:** Expected comparison count is 1, not 2.

**Answer:** Expected comparison count is 1, not 2.


### Question 2: Hashing: worked application 2

With 12 keys in a hash table of 6 buckets, calculate load factor and state the uniform-hashing assumption.

1. **Set up the model and conditions:** Load factor α is n/m=12/6=2.

2. **Carry out the calculation or proof:** Expected chain behavior requires the hash outcomes to be well spread for the input distribution.

3. **State the result and its scope:** α=2; adversarial collisions can still create a chain of length 12.

**Answer:** α=2; adversarial collisions can still create a chain of length 12.


### Question 3: Sampling: worked application 3

Show reservoir sampling of one item has uniform retention after three observations.

1. **Set up the model and conditions:** At observation 1 retain item 1; after observation 2 retain each of 1 and 2 with probability 1/2.

2. **Carry out the calculation or proof:** At observation 3 the old item survives with probability 2/3 and item 3 replaces it with probability 1/3.

3. **State the result and its scope:** Each of items 1,2,3 has retention probability 1/3.

**Answer:** Each of items 1,2,3 has retention probability 1/3.

