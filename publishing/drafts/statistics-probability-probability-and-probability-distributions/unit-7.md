# Unit 7: Waiting Counts, Negative Binomial and Poisson Laws

## Learning aims and different meanings of a count

An integer-valued variable does not identify its own probability law. A fixed number of independent opportunities produces a binomial success count. A sequence continued until its first success produces a waiting count. A sequence continued until several successes produces another waiting law. Counts over a modeled interval can follow a Poisson law under an appropriate event mechanism. These descriptions require different supports and parameters even when their numerical means happen to agree.

The aims of this unit are to derive geometric and negative binomial waiting distributions from independent binary trials, distinguish failures from total trials, explain memorylessness in discrete time, derive the Poisson PMF and its moments, and use independent aggregation and thinning correctly. The reader should be able to translate a stopping rule into a count variable and identify the event behind an inequality before calculating a tail.

All event rates and trial probabilities in the examples are fixed teaching assumptions. A fitted rate for a real process would require data, an observation window and model assessment. Calling a process a Poisson process or a trial sequence independent does not make those assumptions true. The models here describe their stated mechanisms and offer tools for checking the consequences.

## Geometric waiting until the first success

Consider mutually independent binary trials with a common success probability $p$, where $0<p\leq1$. Let $T$ be the number of trials up to and including the first success. Its support is the positive integers. For the event $T=t$, the first $t-1$ trials must fail and the next must succeed, so

$$
P(T=t)=(1-p)^{t-1}p,\qquad t=1,2,\ldots.
$$

There is no combination coefficient because the stopping event specifies the final success and every preceding trial is a failure. Permuting the position of that success would change the stopping time. The PMF sums to one by the geometric series when the success probability is positive. At probability one, the first trial succeeds with certainty and the distribution is a point mass at one.

If the success probability is zero, the first success never occurs under the model. No proper finite positive-integer waiting-time PMF results. One can extend the variable to take infinity with probability one, but that is a different specification from the proper geometric law used here. Applying the usual mean formula and presenting an ordinary finite count would be incorrect.

The probability that the wait exceeds an integer $m\geq0$ is the probability that all first $m$ trials fail, namely $(1-p)^m$. The probability that the wait is at least an integer $k\geq1$ is $(1-p)^{k-1}$. The difference between exceeds and at least is one trial. A continuous-time intuition that endpoints have zero probability cannot be transferred to this discrete distribution.

The CDF at an integer $t\geq1$ is $1-(1-p)^t$. Between integers it remains constant according to the general CDF convention. Its jumps are the PMF values. A quantile can be found by identifying the smallest integer where this accumulated probability reaches the requested level. Rounding a real logarithmic solution in the wrong direction can put the threshold below the required cumulative probability.

## Counting failures instead of trials

Another common geometric convention uses $F=T-1$, the number of failures before the first success. Its support begins at zero and its PMF is $P(F=f)=(1-p)^fp$. The two definitions describe the same underlying sequence but different numerical variables. Their variances agree because subtracting one is a location shift, while their means differ by one.

Every formula should identify its convention. A reported mean of five for total trials corresponds to a mean of four for failures in that same model. A software function can use either convention without being wrong, but using its output with a formula from the other convention produces an off-by-one error. The support statement is often the quickest way to detect the mismatch.

The failures PGF is $p/(1-(1-p)z)$ on its convergent domain. Multiplying by $z$ gives the total-trials PGF. Differentiation gives $E[F]=(1-p)/p$ and $E[T]=1/p$. Both have variance $(1-p)/p^2$. For an interior success probability, the MGF is finite when $(1-p)e^t<1$, so its domain includes a neighborhood of zero but is not the entire real line.

The expected total wait can also be derived from a recursion. One trial is always used. With probability $1-p$, that trial fails and the remaining wait has the same distribution as the original because future trials are independent with unchanged probability. If the mean is finite, it satisfies $E[T]=1+(1-p)E[T]$, giving $1/p$. The recursion reflects a renewal of the experiment after failure, not a general property of every waiting process.

## Discrete memorylessness and a constant hazard

For nonnegative integers $m,n$, geometric total waiting satisfies

$$
P(T>m+n\mid T>m)=\frac{(1-p)^{m+n}}{(1-p)^m}=(1-p)^n
$$

when the condition has positive probability. After observing only failures for the first $m$ trials, the probability of waiting more than another $n$ trials is unchanged. This is memorylessness. It follows from the independent common-probability trial mechanism. It does not mean that the elapsed trials are forgotten in the numerical total; it means the remaining distribution is unchanged under the stated information.

The discrete hazard at a positive trial index is the probability of success at that trial given survival to it. For the geometric law it is $P(T=k\mid T\geq k)=p$. The denominator uses at least because the trial has not yet been observed at that information point. Substituting a strictly-greater condition would change the event and can make the expression nonsensical.

Memorylessness does not imply that a long realized run makes success due. Under the model, the next trial still has probability $p$ after any finite failure history with positive probability. A changing success probability, fatigue effect or hidden shared condition would invalidate that conclusion. The appropriate response to such a mechanism is to change the model, not to impose the geometric property regardless of the experiment.

At probability one, conditions describing a positive number of preceding failures have zero probability, so their elementary conditional ratios are undefined. The limiting model is deterministic but remains valid. Boundary checks should distinguish a probability identity on positive-probability conditions from a formal expression containing a zero denominator.

## Negative binomial waiting for several successes

Now continue the independent common-probability sequence until the $r$th success, where $r$ is a positive integer. Let $T_r$ count total trials including that final success. Its support is the integers from $r$ upward. For $T_r=t$, the first $t-1$ trials contain exactly $r-1$ successes and the final trial is a success. Therefore

$$
P(T_r=t)=\binom{t-1}{r-1}p^r(1-p)^{t-r},\qquad t\geq r.
$$

The position coefficient concerns only the trials before the last one. Using $\binom tr$ would allow the stopping success to appear elsewhere and would overcount paths that already reached the required total earlier. The stopping rule is part of the event, not a detail to be added after applying a fixed-length binomial formula.

The failures convention uses $F_r=T_r-r$, with support starting at zero and PMF $\binom{f+r-1}{r-1}p^r(1-p)^f$. Both conventions are often called negative binomial. The parameter $r$ here is a fixed required number of successes, and the variable counts failures or total trials as stated. Other parameterizations in statistical software can use noninteger shape values, but their extended mathematical family should not be confused with this literal integer-success stopping experiment.

When the required success count is one, the law reduces to the geometric distribution under the corresponding convention. At success probability one, the total trial count is exactly $r$ and the failure count is zero. At success probability zero, the stopping event never occurs and no proper finite waiting-count law results. The same parameter existence distinction therefore applies as in the first-success case.

## Negative binomial moments and tail events

The waiting times between successive successes are independent geometric total waits under the independent common-probability trial mechanism. The total wait for $r$ successes is their sum. PGF multiplication gives $(pz/(1-(1-p)z))^r$ for total trials and $(p/(1-(1-p)z))^r$ for failures. This sum representation establishes normalization and moments without separately summing a complicated infinite PMF.

The mean total wait is $r/p$, and its variance is $r(1-p)/p^2$. Mean failures are $r(1-p)/p$, with the same variance. These formulas are not the moments of a fixed-length binomial count because the trial length is random. Increasing the success target changes the expected number of opportunities needed, while changing the probability affects both location and spread.

A waiting-time tail can be related to a fixed-length success count. The event $T_r\leq m$ means that at least $r$ successes have occurred by trial $m$. Under the underlying mechanism, the count in those first $m$ trials is binomial. Thus a cumulative negative binomial question can be calculated through a binomial upper tail. If $m<r$, the event is impossible, consistent with the waiting support.

Waiting for several successes is generally not memoryless in the total elapsed count alone. The information needed to predict remaining trials includes how many successes have already occurred. Two histories of the same length with different progress toward the target can have different remaining waits. The geometric special case avoids that additional progress state because survival means no success has yet occurred.

A failure count can have variance larger than its mean. For the negative binomial failures convention, their ratio is $1/p$ for an interior parameter. This is a property of the stopping mechanism, not proof that every overdispersed dataset came from such a process. Other mixtures and dependence mechanisms can produce similar mean–variance relationships. Distribution selection requires the experiment and more than a single summary ratio.

## The Poisson distribution as an event-count law

A Poisson variable $N$ has parameter $\lambda\geq0$ and PMF

$$
P(N=k)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k=0,1,2,\ldots.
$$

The parameter is the expected count over the specified opportunity or interval, not necessarily a rate per unit time. In a homogeneous time model with rate $\rho$ and duration $h$, the count parameter is $\lambda=\rho h$. Rate has reciprocal-time units while the expected count is dimensionless. Mixing duration units can therefore change the parameter by an unintended factor.

The masses sum to one because the exponential power series sums to $e^\lambda$. At zero parameter, the law is a point mass at zero, interpreted directly without relying on ambiguous powers. For positive parameter, the support is every nonnegative integer. A finite collection of objects with a hard maximum count cannot have this exact unbounded law unless the counted quantity is defined differently or the law is explicitly an approximation.

One derivation takes a binomial limit with increasing trial count, decreasing success probability and fixed product approaching $\lambda$. For fixed count $k$, the combination term and success powers tend to $\lambda^k/k!$, while the failure factor tends to $e^{-\lambda}$. This yields the Poisson PMF. The derivation identifies a rare independent-opportunity mechanism, rather than stating that rarity alone is sufficient.

A homogeneous Poisson process supplies another event mechanism: counts over intervals have parameters proportional to duration, disjoint interval counts are independent, and the process has the appropriate small-interval behavior. A full process theory is developed in the later Stochastic Processes book. Here those conditions are stated when used. Bursty arrivals, a changing rate or dependence between intervals can invalidate the simple homogeneous model.

## Poisson moments and transforms

The PGF is $G_N(z)=\exp(\lambda(z-1))$. It follows by substituting the PMF into the exponential series. Its first derivative at one is $\lambda$, and its second derivative gives factorial second moment $\lambda^2$. Converting to the second raw moment gives $\lambda^2+\lambda$, hence variance $\lambda$. Equal mean and variance are therefore a model consequence, not a universal property of event counts.

The MGF is $\exp(\lambda(e^t-1))$, finite for every real argument. The cumulant generator is $\lambda(e^t-1)$, so every positive-order cumulant equals $\lambda$. For positive parameter, skewness is $1/\sqrt\lambda$ and excess kurtosis is $1/\lambda$. The law becomes less skewed in standardized terms as the expected count increases, but small tail probabilities still require an appropriate exact or checked approximate calculation.

Successive masses satisfy $P(N=k+1)/P(N=k)=\lambda/(k+1)$ for positive parameter. This recurrence shows where the PMF rises and falls and permits stable computations around a suitable central mass. The mode is the integer part of the parameter when the parameter is noninteger; a positive integer parameter gives two adjacent modes. A zero parameter has only count zero. The parameter can be noninteger even though the variable's realized values are integers.

## Aggregation, thinning and conditional allocation

The sum of independent Poisson variables is Poisson with parameter equal to the sum of their parameters. Multiply their PGFs and combine the exponents to prove the result. The independence assumption is essential. Counts sharing an uncertain rate or an outcome constraint do not automatically satisfy this aggregation law simply because each marginal is described as Poisson.

Independent thinning retains each counted event with probability $q$, independently of the count and of other event marks under the stated construction. Conditional on the original count, the retained count is binomial. Substituting into the Poisson PGF gives $\exp(\lambda q(z-1))$, so the marginal retained count is Poisson with parameter $\lambda q$. The discarded count has parameter $\lambda(1-q)$.

The retained and discarded counts are also independent marginally under this independent-marking construction. Their joint PGF is $\exp(\lambda(qz+(1-q)w-1))$, which factorizes into their two PGFs. Conditional on a fixed total, however, one count determines the other and they are dependent. There is no contradiction: conditioning on the shared total changes the information set and the joint law.

For two independent Poisson counts with positive total parameter, conditioning on their sum gives a binomial allocation with probability equal to the first parameter divided by the total parameter. Dividing the joint masses by the total Poisson mass yields the binomial coefficient and allocation powers. This result is useful when the total count is known and the question concerns its composition. If the total parameter is zero, only total zero is possible and a separate degenerate interpretation is needed.

## Approximation and uncertain rates

A binomial count with many independent opportunities and a small common success probability can sometimes be approximated by a Poisson law with matching mean. The approximation should be evaluated for the event being reported. A match of means alone is insufficient: binomial variance is the mean multiplied by one minus the success probability, whereas Poisson variance equals the mean. The support is also finite in one case and infinite in the other.

When exact binomial computation is available, it provides a reference for checking the approximation. A numerical difference in a central probability can differ from the difference in a far tail. One should report the exact model value or an explicit approximation scope rather than applying a universal rare-event slogan. The synthesis unit will compare selected exact and approximate probabilities with measured errors.

A random shared Poisson parameter creates a mixture with extra variation. If the conditional count is Poisson given a parameter variable $\Lambda$ with finite mean and variance, iterated expectation gives overall mean $E[\Lambda]$. Total variance gives $E[\Lambda]+\operatorname{Var}(\Lambda)$. Therefore uncertainty or heterogeneity in a shared rate can produce variance greater than the mean. Treating the mean rate as fixed drops the second component.

The mixture mechanism should not be confused with merely estimating a fixed unknown parameter from data. A random-rate model says how rate variability enters the predictive experiment. An estimate's uncertainty belongs to a statistical analysis and may be represented in several ways depending on the chosen framework. A clear report identifies whether the rate varies across intervals, is a fixed unknown quantity, or is stipulated as known for a teaching example.

## Fully worked question 1: First-success waiting and memorylessness

**Question.** Independent trials succeed with probability one fifth. Let $T$ count trials through the first success and $F=T-1$ count preceding failures. Find $P(T=4)$, $P(T>5)$, and $P(T>8\mid T>3)$. Find both means and the common variance. Explain the meaning of the conditional result and the difference between $T>5$ and $T\geq5$.

**Solution, step 1: Calculate the exact and tail events.** Exactly four trials requires three failures followed by a success, giving $(4/5)^3(1/5)=64/625=0.1024$. More than five trials requires five initial failures, giving $(4/5)^5=1024/3125=0.32768$. At least five trials instead requires only four initial failures and has probability $(4/5)^4=256/625$. The endpoint difference matters because the variable is discrete.

**Solution, step 2: Condition on the observed failure history.** More than eight trials is a subset of more than three. Dividing their probabilities gives $(4/5)^8/(4/5)^3=(4/5)^5=0.32768$. After the three observed failures, waiting more than five additional trials has the same probability as waiting more than five trials initially. This is the memoryless remaining-wait property; it does not claim that total elapsed time is unchanged.

**Solution, step 3: Use the stated count conventions.** Mean total trials is five. Mean failures is four. Their variance is $(4/5)/(1/5)^2=20$. The one-unit shift changes the mean and support while preserving variance. The next trial after any finite failure history still has success probability one fifth under the independent fixed-probability model. A changing-probability process would require a different analysis.

## Fully worked question 2: Waiting until the third success

**Question.** Independent trials succeed with probability two fifths. Let $T_3$ be total trials through the third success and $F_3=T_3-3$ be preceding failures. Find the probability that the third success occurs on trial five, the probability that it occurs by trial five, and the mean and variance of each count convention. Explain why the two requested probabilities use different events.

**Solution, step 1: Place the stopping success correctly.** For the third success on trial five, the first four trials contain exactly two successes and the fifth succeeds. There are $\binom42=6$ possible initial patterns, each with the same probability. The result is $6(2/5)^3(3/5)^2=432/3125=0.13824$. Using a coefficient choosing three success positions among all five would include paths that reached the target earlier.

**Solution, step 2: Convert a cumulative wait to a fixed-length count.** A third success by trial five means at least three successes among the first five trials. Summing the binomial probabilities at three, four and five gives $720/3125+240/3125+32/3125=992/3125=0.31744$. This includes stopping at trials three, four or five, so it is larger than the exact trial-five probability.

**Solution, step 3: Calculate the two means and common variance.** Mean total trials is $3/(2/5)=15/2$. Mean failures is $3(3/5)/(2/5)=9/2$. Variance is $3(3/5)/(2/5)^2=45/4$. Subtracting three changes location but not variance. Predicting a remaining wait after partial history would require the number of successes already observed, since total waiting for several successes is not memoryless in elapsed trial count alone.

## Fully worked question 3: A Poisson interval count and independent marking

**Question.** A stipulated homogeneous event model has rate $1.8$ events per hour. Find the count parameter over two hours and the probability of no event in that interval. Independently mark each event with probability one third. Find the marked-count law, its mean and variance, and the probability of exactly two marked events. Given that five events occurred in total, find the probability that exactly two were marked. Distinguish the unconditional and conditional marked-count questions.

**Solution, step 1: Match the parameter to duration.** The two-hour parameter is $1.8\cdot2=3.6$. The total count is Poisson with that parameter under the stipulated homogeneous model. No events has probability $e^{-3.6}$, approximately $0.027324$. The mean and variance of the total count are both $3.6$, although its realized count must be an integer.

**Solution, step 2: Thin independently.** The marked count is Poisson with parameter $3.6/3=1.2$. Its mean and variance are both $1.2$. Exactly two marked events has probability $e^{-1.2}(1.2)^2/2$, approximately $0.216860$. This marginal question averages over all possible total counts and uses the independent-marking construction.

**Solution, step 3: Condition on a fixed total.** Given five total events, the marked count is binomial with five trials and probability one third. Its exactly-two probability is $\binom52(1/3)^2(2/3)^3=80/243$, approximately $0.329218$. Fixing the total changes the reference experiment from an unbounded Poisson count to marking five known opportunities. The two results answer different questions and need not agree.

## Tail-sum moments and the characterization of memorylessness

A nonnegative integer variable can be represented as a sum of indicators that its value exceeds successive thresholds. For a positive integer wait, each realized value contributes one to the indicator sum at every threshold from zero up to one below that value. Taking expectation gives $E[T]=\sum_{m=0}^{\infty}P(T>m)$, with an extended infinite value permitted. Nonnegative terms justify the interchange through monotone accumulation.

For the geometric law, substituting its survival probabilities turns this into a geometric series and gives mean $1/p$. The corresponding squared-value identity uses increments of successive squares: $t^2=\sum_{m=0}^{t-1}(2m+1)$. Therefore the second moment is the sum of $(2m+1)P(T>m)$ over nonnegative thresholds. Geometric-series differentiation evaluates that sum, and subtracting the squared mean reproduces the variance $(1-p)/p^2$.

The tail-sum route is useful beyond this family. It calculates a waiting mean from survival probabilities without first reconstructing the full PMF. It also reveals why a long tail can give an infinite mean even when a proper stopping time is finite almost surely. Probability one of eventual completion is not the same as a finite expected duration. The tail probabilities must decay rapidly enough for the relevant sum to converge.

Memorylessness characterizes the proper positive-integer geometric law under its usual nondegenerate conditions. Let a survival function satisfy $S(m+n)=S(m)S(n)$ for nonnegative integers, with $S(0)=1$ and $S(1)=q$ in the interval from zero up to but not including one. Repeated application gives $S(m)=q^m$. Differences of consecutive survival values give the geometric PMF with success probability $1-q$. If $q=1$, survival never decreases and no proper finite wait results.

This derivation shows why a constant hazard and an exponential-in-trial-index survival curve are linked. It also offers a structural check on a proposed waiting model. A survival law that is not a geometric power cannot have the stated discrete memoryless property. Similar-looking declining tails are insufficient; the multiplicative identity concerns every allowed pair of integer durations.

For a contrasting multiple-success example, wait for two successes with success probability one half. At trial index $t\geq2$, the PMF is $(t-1)/2^t$, while survival to that trial has probability $t/2^{t-1}$. The hazard is therefore $(t-1)/(2t)$, which changes with the trial index. It starts at one quarter and approaches one half. The total wait is not geometric even though it is a sum of two geometric waits and comes from the same independent trial sequence.

## Administrative cutoffs and observed waiting records

A practical procedure can stop observation after a fixed maximum number of trials even when the underlying model permits a longer wait. If no success is seen by that cutoff, the recorded information is that the first-success time exceeds the cutoff. It is not an observed success at the cutoff. Replacing such records by completed waiting times changes the event and can distort summaries or a subsequent statistical analysis.

Under a geometric model, the probability of no success by a cutoff $c$ is $(1-p)^c$. Among sequences that do finish by the cutoff, the conditional PMF of the completed wait is $p(1-p)^{t-1}/(1-(1-p)^c)$ for trials one through $c$. This is a truncated conditional distribution. Its mean need not equal the unconditional mean $1/p$, because the conditioning deliberately excludes longer waits.

The observation rule also determines how a simulation should report an unfinished path. A label such as more than one hundred trials preserves the censoring information. Reporting one hundred as though a success occurred there does not. A simulation that imposes a computational safety limit should disclose that limit and distinguish unfinished paths from genuine completed counts. It must not silently renormalize the completed paths while still claiming an unconditioned geometric distribution.

For waiting until several successes, a cutoff record can include the number of successes seen so far as well as the fact that the target has not been reached. Those pieces of information affect prediction of the remaining wait. A model that stores only elapsed trial count may discard useful state. The correct level of state depends on the experiment and question, not on the convenience of a display field.

## Controlled numerical tails for an infinite PMF

An infinite-support PMF needs a strategy for numerical tail accumulation. Summing only the displayed counts can leave unaccounted probability, even when the graph looks complete. For the Poisson law, the successive-mass ratio supplies an explicit bound on the remainder. Beyond a count where the ratio is strictly less than one, later ratios are no larger, so later masses are bounded by a geometric sequence.

Suppose the first omitted count is $m$ and $m+1>\lambda$. The probability from that count onward is at most $P(N=m)/(1-\lambda/(m+1))$. This follows by comparing every subsequent mass to the first omitted mass multiplied by successive powers of the largest relevant ratio. It is a rigorous upper bound on omitted probability, not an exact tail expression. A program can use it to choose a display truncation meeting a stated error tolerance.

The bound must be applied in its valid decreasing-tail region. If the ratio is one or larger, the geometric upper series does not provide a finite bound in that form. Starting the bound near the mode without checking the inequality can yield a meaningless denominator. The zero-rate case is handled directly by its point mass rather than by a recurrence dividing by a rate or a vanished mass.

For large parameters, computing the zero-count mass first may underflow and cause a recurrence to return zeros everywhere. Starting from a central log-mass and accumulating outward can avoid that failure. The mathematical PMF remains valid; the numerical representation has lost scale. Exact rational path checks for finite trial models and independent high-precision or analytic checks for selected Poisson values help distinguish model errors from numerical underflow.

## Auditing stopping rules and event-count models

For a waiting law, write whether the variable counts failures or total trials and identify the required success number. Check whether the success probability stays constant after every allowed history and whether the relevant trials are mutually independent. Distinguish an exact stopping trial from reaching the target by a trial. Check that a reported threshold lies within the support before using a PMF or tail formula.

For a Poisson count, state the interval or opportunity and whether the parameter is a mean count or a rate. Verify any assumptions about independent increments, constant rate, event marking and aggregation. A simulation should not label a clustered or variable-rate process homogeneous merely because it has the same average count. Shared randomness can change joint laws and variances even when every displayed mean is preserved.

The planned waiting-count explorer should explicitly display both failures and trials, with their one-success or multiple-success offsets. Invalid zero success probabilities should be explained as no finite stopping time, rather than producing an unexplained infinite output. The event-count explorer should label exact PMFs and simulated frequencies separately and include the zero-rate case. Finite simulation cannot prove normalization of an infinite law or establish a limiting approximation.

Independent checks should enumerate short stopped paths, compare cumulative waits with fixed-length binomial tails, and verify Poisson probabilities against direct exponential expressions. Testing tails should include strict versus nonstrict inequalities. The next unit moves to continuous waiting and duration models, where exponential memorylessness resembles the geometric property but uses continuous intervals and different endpoint behavior.
