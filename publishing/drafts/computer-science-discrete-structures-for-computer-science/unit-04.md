# Unit 4: Discrete probability


## Finite Experiments

**Core model — Finite Experiments**

A finite probability experiment consists of outcomes and an assigned probability measure; equal likelihood must be justified by the sampling mechanism.

**Original worked illustration**

Two fair coins give four equally probable ordered outcomes, making exactly one head occur in two of four cases for probability 1/2.

**Boundary conditions and checks**

If coins have unequal bias or physical dependence, counting outcomes as equally likely is incorrect.

### A probability model begins with the experiment
A finite probability space lists elementary outcomes and assigns nonnegative weights summing to one. The sample space is not automatically uniform. Rolling a fair six-sided die has six equiprobable outcomes, but selecting a random student from a database where some students appear in multiple rows does not necessarily sample students uniformly. A simulation must say whether it samples rows, students, or unique identifiers; these procedures produce different distributions.

Events are subsets of the sample space, and probabilities add across disjoint events. In an experiment tossing two fair distinguishable coins, the four equally likely strings HH, HT, TH, TT each have probability 1/4. The event 'exactly one head' contains HT and TH, so its probability is 1/2. If the outcomes were instead recorded only as unordered numbers of heads, the three values 0,1,2 would not be equally likely. This is a central distinction between data representation and probability measure.

### Counting as a probability technique
Under a justified uniform model, P(A)=|A|/|Ω|. For n independent fair tosses there are 2^n bitstrings. The probability of exactly k heads is C(n,k)/2^n because the event contains C(n,k) strings. For n=5, exactly two heads occur with probability 10/32. The total over k=0..5 equals 32/32 by the binomial theorem. That total-probability check catches missing or double-counted categories.

### Sampling and simulation
To estimate a probability computationally, generate N independent trials using the specified distribution and calculate the fraction of successes. The law of large numbers explains convergence of the empirical fraction to the true probability as N grows. It does not guarantee that every finite run is accurate. For a Bernoulli indicator with success probability p, the estimator's standard deviation is sqrt(p(1−p)/N), at most 1/(2sqrt(N)). A plot of simulated frequency should be compared against an analytical benchmark where one exists. A pseudorandom number generator is deterministic given its seed and unsuitable as a source of security-grade randomness merely because its output looks irregular.

### Faults in modeling
When testing a rare-event simulator, use the correct denominator: selecting one event per complete experiment is not equivalent to counting successful sub-events within each experiment. Record whether trials are independent, whether probabilities are constant, and whether the output is theoretical or empirical. For example, dealing cards without replacement changes later probabilities. A program that regenerates the deck between draws silently changes the physical model, even if its code is otherwise correct.



## Conditional Probability

**Core model — Conditional Probability**

Conditional probability rescales the probability within the event conditioned upon: P(A given B)=P(A intersection B)/P(B) for P(B)>0.

**Original worked illustration**

From a standard deck, given a card is a face card (12 possibilities), the chance it is a king is 4/12=1/3.

**Boundary conditions and checks**

Conditional probabilities reverse asymmetrically: P(A given B) generally differs from P(B given A). Independence is a separate property.

### Conditional probability restricts the reference population
For events A and B with P(B)>0, P(A|B)=P(A∩B)/P(B). Conditioning changes the universe under discussion to cases where B occurred. It is not generally true that P(A|B)=P(B|A). Suppose 2% of devices are defective, a test detects 95% of defects, and falsely alarms on 4% of good devices. The probability of a true alarm with a defect is 0.02×0.95=0.019; the false-alarm probability is 0.98×0.04=0.0392. Among alarms, the defective share is 0.019/(0.019+0.0392)≈0.3265, not 0.95.

### Bayes' rule follows from two factorizations
The joint probability is both P(A∩B)=P(A|B)P(B) and P(A∩B)=P(B|A)P(A). Equating them and dividing by P(B) yields Bayes' rule. This simple algebra prevents a common interpretive mistake: the test's sensitivity P(positive|defective) is not the posterior probability P(defective|positive). The base rate affects the posterior through P(defective). A classifier's precision can change when deployed to a population with a different prevalence, even if its sensitivity and false-positive rate remain the same.

### Independence and conditional independence
Events A and B are independent when P(A∩B)=P(A)P(B). If P(B)>0, this is equivalent to P(A|B)=P(A). Independence does not mean events cannot occur together; disjoint nonempty events are actually dependent. Conditional independence is different. Two alarm sensors may become independent once the presence or absence of a fire is fixed, but be strongly associated overall because a fire influences both. A Bayesian network expresses these conditional relationships through its graph structure, while numerical parameter assumptions are still necessary for calculations.

### Sequential updates
Suppose three independent components work with probabilities 0.9,0.8,0.95. The probability that all work is their product 0.684. If failures are correlated due to a shared power source, multiplying marginals may be wrong. To model system reliability faithfully, introduce shared causes or conditional probabilities. For any proposed independence assumption, ask what mechanism justifies it. Testing observed association can challenge the assumption, but failing to reject dependence does not establish perfect independence, especially with small samples.



## Expectation

**Core model — Expectation**

Expectation is a probability-weighted average of outcomes and obeys linearity without requiring independent random variables.

**Original worked illustration**

For a fair six-sided die, E[X]=(1+2+3+4+5+6)/6=3.5. For two such dice, E[X+Y]=7 even if their rolls are dependent with the same marginals.

**Boundary conditions and checks**

Expectation does not describe the most likely outcome and does not imply small variance.

### Expected value is a weighted average, not the most likely outcome
For a discrete random variable X taking values xi with probabilities pi, E[X]=Σ xi pi. It can be a number X never takes. A fair die has expected result 3.5, but rolling 3.5 is impossible. This distinction matters when interpreting an algorithm's expected running time: it describes an average under a probability model for input instances or algorithmic choices, not a guarantee for any particular execution.

### Linearity is unusually powerful
For any integrable random variables X and Y, E[X+Y]=E[X]+E[Y], even when they are dependent. Suppose Xi indicates whether the ith of n users clicks a link; then the expected total click count is Σ P(Xi=1). No independence assumption is needed for this expectation. Independence becomes important for calculating many variance or concentration expressions, not for linearity itself. This lets analysts derive expected work counts using indicator variables instead of enumerating all joint outcomes.

### Variance and risk
Variance is E[(X−E[X])²]=E[X²]−E[X]². For a Bernoulli random variable with success probability p, E[X]=p and Var(X)=p(1−p). If n independent Bernoulli trials have the same p, the total S has expectation np and variance np(1−p). The standard deviation scales like sqrt(n) while the mean scales like n, helping explain concentration of normalized averages. Without independence, covariance terms enter the variance and may substantially change the spread.

### An expected-work calculation
An unsorted array of n unique keys is searched sequentially for a key known to be present, with each position equally likely. If the key is at position i, the algorithm performs i comparisons. Expected comparisons equal (1+2+...+n)/n=(n+1)/2. For n=9 that is 5 comparisons. If unsuccessful searches are possible, introduce a probability q of an unsuccessful query and specify the conditional position model; one then obtains E[C]=q n+(1−q)(n+1)/2. A different distribution of popular keys changes the average, so the uniform-position assumption must be visible.

### Interpreting the mean carefully
A low expectation can hide large tail outcomes. A service with response time one millisecond 99% of the time and 1001 milliseconds 1% of the time has average 11 milliseconds; the single average conceals a significant tail. Expected-value analysis should be combined with quantiles, worst-case bounds, or variance when high-cost outcomes matter. Never infer a hard upper bound from an average.



## Randomized Computation

**Core model — Randomized Computation**

Randomized programs generate distributions of outcomes. Analyze both their computational cost and probability of error, distinguishing Las Vegas and Monte Carlo styles.

**Original worked illustration**

A randomized membership test with one-sided error may return a false positive but never a false negative; repeated independent runs can reduce the positive-error probability multiplicatively.

**Boundary conditions and checks**

Repetition only amplifies reliability as calculated when trials are suitably independent; correlated seeds can defeat naïve claims.

### A randomized algorithm has two sources of variation
A randomized program deliberately samples random choices during execution. Its output or runtime may vary even when the input stays fixed. Analyses distinguish randomness in the input from randomness generated by the algorithm itself. For example, randomized quicksort chooses pivots randomly so that its expected comparison count is O(n log n) for every fixed set of distinct keys under the chosen pivot model, even though some pivot sequences still cause quadratic work. The guarantee concerns an expectation over the algorithm's choices, not a guarantee that every run is fast.

### Las Vegas and Monte Carlo behavior
A Las Vegas algorithm always returns a correct answer if it returns, while its runtime is random. A Monte Carlo algorithm has a bounded running time but may produce an incorrect answer with a bounded probability. These definitions are styles of guarantees, not labels for specific programming languages. A randomized primality test that sometimes declares a composite number 'probably prime' is Monte Carlo; repeating independent rounds can reduce the probability of that kind of error when the mathematical test supports such a bound. Reusing correlated random states can invalidate the claimed exponential reduction.

### Uniform sampling through reservoir selection
To choose one element uniformly from a stream of unknown length, store the first element and, on seeing the ith item, replace the stored item with probability 1/i. For the newest item, its final probability is 1/n directly upon arrival at n. For an earlier item j, the probability it is selected when it arrives is 1/j, and the probability it survives each subsequent step i is 1−1/i. The product (1/j)×∏_{i=j+1}^n (i−1)/i telescopes to 1/n. This proof makes no assumption about the content of stream elements; it assumes independent, correctly distributed random selections.

### Error estimates and seeded tests
A simulation with n random trials should report its seed, estimated quantity, uncertainty, and analytical comparison where available. For an event of probability p, the sample proportion from independent trials has standard error sqrt(p(1−p)/n). A test failing because one seeded sample estimate differs from its expectation is not automatically a bug. Conversely, a seeded result that matches expectation once is not a proof of correct sampling. Unit tests should inspect deterministic invariants (output belongs to the input set), boundary cases (one-element stream), and statistical properties across many reproducible seeds.

### Engineering threat model
A general-purpose PRNG may be entirely appropriate for randomized algorithms or classroom Monte Carlo demonstrations but inappropriate for generating login tokens, cryptographic nonces, or secret keys. Security requires unpredictability against an adversary, which differs from statistical uniformity in a non-adversarial experiment. The mathematical random model and the implementation source of randomness must therefore be documented separately.

### Extended laboratory: reliability of a replicated service
A small online library stores an object on two independent servers. Each server is available during a random observation with probability 0.9. The service can read the object if at least one server is up. Enumerate outcomes UU,UD,DU,DD with probabilities 0.81,0.09,0.09,0.01. Read availability is 0.99. This comes from the complement: service unavailable means both servers down, with probability (0.1)²=0.01 under the independence assumption. It is wrong to obtain 0.99 merely by adding availability probabilities, because the result would exceed one and double-count the UU state.

Suppose the two servers share a power supply. Then their failures may be strongly correlated, and P(both down) can be much larger than 0.01 even if each marginal downtime remains 0.1. To express the general case, use P(A∪B)=P(A)+P(B)−P(A∩B) where A and B mean availability. Without a dependence model, the marginals alone do not fix the intersection. The classroom independence calculation is a baseline, not an operational guarantee for deployed machines.

A monitor raises an alarm if at least one server responds slowly. Assume a single server is slow with probability 0.05 and different servers' slowness is independent for this toy model. The probability of any slow server is 1−0.95²=0.0975. But this is not automatically the probability of a slow user response. If requests use the fastest healthy replica, a single slow replica may not delay a request at all. Modeling user experience requires a policy for replica selection and potentially queueing delays, not just component events.

Consider a backup check that correctly alerts on a missing backup with sensitivity 0.95 but falsely alerts 0.03 of the time when a backup exists. If only 1% of the observed days actually lack backups, the fraction of alerts that signal a real problem is 0.01×0.95/[0.01×0.95+0.99×0.03]≈0.2423. The computation makes operational sense only if the base rate and error characteristics refer to the same monitored environment. The alert can still be useful even with a low positive predictive value, because missing backups may be costly, but escalation policies should account for false positives.

Expected cost helps compare responses. Suppose checking an alarm takes 10 minutes, and failing to act on a truly missing backup incurs 1000 minutes of recovery work on average under a simplified scenario. A policy might justify checking alarms promptly even when many are false. However, expectations do not describe tail risks: an actual outage can have much larger effects than the average. A responsible analysis presents the probability model, its uncertainty, and consequences separately.

A Monte Carlo exercise can simulate 10,000 independent server-pair states and record the fraction with at least one live replica. The fraction should fluctuate around 0.99. The standard deviation of the sampled fraction under the Bernoulli model is sqrt(0.99×0.01/10000)≈0.000995. A single run returning 0.988 is plausible; rejecting the simulator merely because the result is not exactly 0.99 would be a statistical mistake. To test implementation logic, also enumerate all four pair states deterministically and verify the outcome rule for each.

When a student changes the server availability slider, the theoretical prediction becomes 1−(1−p)² only if both replicas keep the same independent availability p. If the interface adjusts only one replica, the correct formula is 1−(1−p1)(1−p2). Extreme cases should make sense: with p1=p2=0 the service is unavailable, and with either probability equal to one the service is always available. A teaching simulation should explain these assumptions beside its output rather than hiding them in the code.

### Experiment card: analytical probability versus simulation
The primary probability model returns the chance of exactly one head in n independent fair coin tosses: n/2^n. With n=1 the answer is one-half, with n=2 it is two-fourths, and with n=3 it is three-eighths. The model's curve is not monotone from the first point: the first two values are equal before the probability decreases. This matters for plotting and for tests that wrongly assume every additional toss always changes the likelihood in the same direction.

The independent birthday model uses a simplified year of 365 equally likely days. Its no-collision probability among n independent people is ∏_{i=0}^{n−1}(365−i)/365, so collision probability is one minus that product. For n=1 the collision probability is zero. For n=2 it is 1/365. For n=3 the formula is 1−(364/365)(363/365). At small n, duplicate birthdays are rare, and the model is useful for checking multiplication of sequential conditional probabilities. It does not represent real birth-season variation or correlated birthdays among relatives.

To verify the coin model numerically, independently enumerate bitstrings for n up to twelve and count those with Hamming weight one. To verify the birthday model, recompute the product with a separate high-precision implementation and compare to the displayed six-decimal result within an appropriate rounding tolerance. These are stronger tests than checking that the displayed number lies between zero and one. Also test invalid inputs: a string such as '2.5', a negative count, or a value greater than the supported maximum should not silently be treated as a valid experiment.

A plot intended for learning should label whether it shows a *theoretical probability* or an *empirical frequency*. The present formulas are theoretical results, so the computed outputs should not be called Monte Carlo observations. A future Monte Carlo extension would need an explicit trial count, a seed for reproducibility, and sampling uncertainty. For this revision, the narrower formula-driven simulation is a defensible teaching tool because its assumptions and independent checks are transparent.



## Fully worked questions

### Question 1: Finite Experiments: worked application 1

For two independent fair coin tosses, compute the probability of exactly one head.


**Set up the model and conditions:** Enumerate equally likely ordered outcomes HH,HT,TH,TT.


**Carry out the calculation or proof:** HT and TH satisfy exactly one head.


**State the result and its scope:** Probability is 2/4=1/2.


**Independent reasoning check and edge conditions:** The sample space consists of the four equally likely sequences HH, HT, TH and TT, because each of the two independent fair tosses contributes a factor one-half. Exactly one head occurs in HT and TH. Summing their probabilities gives 1/4+1/4=1/2. Counting the favorable cases gives the same answer C(2,1)/2²=2/4. Do not reduce the sample space to just the counts 0,1,2 heads and assign equal probability to those three values; their multiplicities differ.


**Answer:** Probability is 2/4=1/2.


### Question 2: Conditional Probability: worked application 2

Given a face card from a standard 52-card deck, compute probability it is a king.


**Set up the model and conditions:** Condition on the 12 face cards J,Q,K across four suits.


**Carry out the calculation or proof:** Exactly four of these face cards are kings.


**State the result and its scope:** Conditional probability is 4/12=1/3.


**Independent reasoning check and edge conditions:** A standard 52-card deck contains three face-card ranks J,Q,K in each of four suits, for twelve face cards total. Four of these are kings. Once the condition 'the selected card is a face card' is given, the appropriate uniform reference set has twelve cards rather than all fifty-two. Consequently P(king | face)=4/12=1/3. The unconditional P(king)=4/52=1/13 answers a different question. This demonstration assumes one uniformly selected physical card from an ordinary complete deck.


**Answer:** Conditional probability is 4/12=1/3.


### Question 3: Expectation: worked application 3

Compute E[X] for a fair six-sided die.


**Set up the model and conditions:** Each outcome 1 through 6 occurs with probability 1/6.


**Carry out the calculation or proof:** Sum the weighted values: (1+2+3+4+5+6)/6.


**State the result and its scope:** The expectation is 3.5.


**Independent reasoning check and edge conditions:** Because the six faces are equally likely, E[X]=(1+2+3+4+5+6)/6=21/6=3.5. Pairing symmetrical faces also checks the result: (1+6),(2+5),(3+4) are each seven, so the arithmetic mean of every pair is 3.5. The die never displays a fractional face; the expectation is the long-run average of numerical results under the specified distribution. If the die is biased, use weighted probabilities instead of dividing the unweighted sum by six.


**Answer:** The expectation is 3.5.

