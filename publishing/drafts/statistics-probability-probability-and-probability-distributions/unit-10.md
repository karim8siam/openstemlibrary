# Unit 10: Model Synthesis, Approximation and Reproducible Probability

## Learning aims and the order of a probability investigation

A probability investigation begins with the experiment, the information available and the event to be evaluated. A family name comes later. This unit combines the preceding material into a workflow for choosing a coherent model, calculating exact probabilities when practical, assessing approximations, using simulation with measurable uncertainty and reporting the result honestly. The goal is not to make every real process fit a named distribution. It is to understand what each proposed model assumes and what its conclusions actually describe.

The reader should be able to distinguish fixed-trial counts from waiting counts, replacement from finite-population sampling, one-stage waits from summed stages, and marginal from conditional predictions. The reader should also be able to compare exact and approximate event probabilities, derive a Monte Carlo standard error for independent indicator trials, explain a carefully stated law of large numbers and central limit theorem, and identify which uncertainty a numerical calculation does not address.

The chapter is an editorial supplement to the selected introductory probability course. It brings the named laws together and introduces computation and convergence without claiming to cover advanced asymptotic theory. Later mathematical statistics and simulation courses will develop those subjects more deeply. Here, the emphasis is a reproducible chain from stated assumptions to a defined event and a checked answer.

## Specify the experiment before choosing a law

Write down what is repeated, what is random, when the procedure stops and which outcomes are possible. A count of successes in a fixed number of independent equal-probability trials has a binomial mechanism. A count of failures before a first success has a geometric mechanism. A total number of trials until several successes has a negative binomial mechanism with a different support. The same word count does not identify which of those experiments occurred.

The observation unit matters. A trial might be one independent attempt, one selected object or one time interval. Two attempts from the same underlying batch can be dependent even when they are recorded on different rows. A time-window count can vary because exposure duration varies. A procedure can have changing success probabilities. These features should be stated before choosing a convenient formula, since the formula's assumptions concern the actual random mechanism.

In a mathematical exercise, the mechanism can be stipulated and the task is to derive its consequences. In an empirical investigation, the mechanism is a model supported or challenged by data and domain knowledge. A correct calculation under a model does not prove that the model describes the process. Keep those two levels separate when explaining an answer.

## Support provides an early elimination rule

The possible values of the variable quickly eliminate incompatible exact laws. A count cannot have a continuous density as its exact recorded law. A duration cannot be negative under a physical waiting interpretation. A finite-population count cannot exceed the sample size or the number of marked objects available. A bounded fractional variable cannot have an exact nondegenerate normal law unless its boundedness is itself an approximation rather than a strict condition.

Support also controls event simplification. For an integer count, an event above two means at least three. For a continuous wait, strict and non-strict thresholds have equal probability under an atom-free law. A mixed law needs both its atoms and its density handled. Applying a continuous approximation to a count requires an explicit translation, often including a continuity correction, rather than pretending that the original support changed.

A support audit can catch an impossible model before numerical work. If a simulator produces values outside the stipulated support, either the model, transformation or implementation is wrong for that task. Clipping the values silently creates another law. A repair must identify the new mechanism or correct the original code; it should not merely hide the discrepant observations.

## A mechanism map for the named discrete laws

A Bernoulli variable represents one binary indicator. A binomial variable counts successes across a fixed number of independent trials with a common probability. A hypergeometric variable counts marked items in a uniformly selected fixed-size subset from a finite population. A geometric variable waits for a first success, and a negative binomial variable waits for several successes. A Poisson variable can represent counts in a stipulated homogeneous event process over a fixed exposure or serve as a controlled approximation to certain rare-event counts.

Each mechanism suggests its own checks. For binomial sampling, inspect fixed trial count, independence and common probability. For hypergeometric sampling, inspect uniform subset selection and the finite marked inventory. For waiting laws, inspect the stopping rule and whether failures or total trials are recorded. For a Poisson process interpretation, inspect the rate, duration and independent increment assumptions rather than inferring the full process from one marginal count fit.

These checks are not interchangeable. A finite population with a very small sampling fraction can make a binomial approximation useful, but the exact hypergeometric law remains different. A variable with mean equal to variance need not be Poisson. Summary identities are model consequences and useful diagnostics, not complete characterizations of every distribution sharing those summaries.

## A mechanism map for the named continuous laws

A uniform law describes equal probability per unit of length over a fixed bounded interval. An exponential law describes a proper nonnegative wait with constant hazard. A gamma law includes independent common-rate exponential stage sums and more general positive shapes. A normal law is an exact stipulated symmetric location-scale model on the real line, and it often appears as an approximation for appropriately standardized sums. A beta law describes a bounded continuous variable or a particular representation of uncertainty about a probability.

The distinctions are visible in conditional predictions. An exponential wait has the same additional-wait law after survival. A multi-stage gamma wait generally does not. A beta uncertainty model shared by several observations can induce their marginal dependence. A normal law for individual data and a normal approximation for an average concern different random objects. One family can serve different roles, but its role must be specified.

Model choice is therefore not a vocabulary quiz. A defensible explanation says which features of the experiment justify the law and which remain assumptions. If the actual mechanism is outside these families, a direct finite table, a mixture, an empirical approximation or a more advanced model may be better. Named laws are tools, not an exhaustive list of uncertainty.

## Parameterize with units and conventions

After selecting a family, state every parameter's meaning, allowed range and units. A binomial trial count is a nonnegative integer and its success probability lies from zero to one. A Poisson parameter is the expected count over a specified exposure, whereas a process rate is expected events per unit exposure. A gamma shape is dimensionless and its rate has inverse-time units for a duration model. Normal notation here uses variance as its second parameter.

Rate-duration products should be dimensionless. Variances have squared units, covariance has the product of its variables' units, and a probability is dimensionless. A mistaken conversion can leave an apparently plausible decimal while changing the underlying event by orders of magnitude. Record the numerical values together with their units instead of placing units only in a distant caption.

Parameter conventions must remain consistent across prose, formulas, software and graphs. A negative binomial failure count starts at zero; a total-trial count starts at the target number of successes. Gamma rate and scale are reciprocal. Comparing results before translating conventions creates false disagreements. A reproducible report includes the formula or convention, so another reader can reconstruct the calculation even with different software.

## Define the event and information set explicitly

Translate the question into event notation before calculating. A joint event, a conditional event and a reverse conditional event may share the same words while having different denominators. The probability that an item is flagged within a source is not the source probability among flagged items. A remaining wait after survival is a ratio of survivals, not the original survival at the final time alone.

If some information is unavailable, average over it using the model's weights. If it becomes observed, update the relevant weights or condition on the known value. The law of total probability and conditional expectation provide this bookkeeping. Omitting a group and conditioning on it are different operations. They can alter dependence, shape and prediction even when each group has a simple named law.

State the information set in ordinary language as well as notation. A phrase such as given an unfinished wait at one hour makes the denominator visible to readers who are still learning conditional probability. It also prevents a correct formula from being reused for a completed wait or a different observation history. Clear event definitions are part of accuracy, not a cosmetic addition.

## Exact calculation, numerical evaluation and approximation

An exact expression can still require numerical evaluation. A normal CDF difference is exact under a normal model, while its decimal evaluation has numerical error. A finite binomial sum is exact under its mechanism, while a Poisson replacement is a distributional approximation. A Monte Carlo estimate is a random numerical approximation to a model probability. These three layers should not be described with one undifferentiated word exact.

Separate model assumptions, analytic approximations, floating-point error and simulation sampling error. Using a high-precision numerical library can reduce floating-point error without fixing a wrong model. Increasing simulation trials can reduce Monte Carlo variability without changing an approximation's bias. Evaluating an approximate family perfectly can still produce a poor answer for the original event.

Choose the simplest method that meets the actual accuracy need. A finite enumeration can be preferable to simulation for a small sample space. A direct survival calculation can be preferable to subtracting a near-one CDF. Simulation is particularly useful when the event involves a complicated mechanism and exact calculation is impractical, but it should not replace an available exact benchmark merely to produce an animated result.

## Rare-event Poisson approximation to a binomial law

For a binomial variable with many trials and small success probability, a Poisson law with parameter equal to the binomial mean can approximate its count distribution. The limit arises when trial count increases, success probability decreases and their product approaches a finite positive value. Fixing the product alone does not make the approximation exact at a finite trial count. The discrepancy depends on the probability and the event being evaluated.

The means match, but variances differ: binomial variance is the mean times one minus the success probability, whereas Poisson variance equals its mean. The discrepancy vanishes relatively as success probability tends to zero. The Poisson law also has unbounded support, so it assigns some mass above a finite binomial maximum. That mass may be negligible in a rare-event regime, but it is another reminder that the replacement is approximate.

Assess the actual event instead of citing a vague rule about large samples. A moderate-count central event may be accurate while an extreme tail has a large relative error. If the exact finite sum is computationally easy, calculate both and report the discrepancy. A approximation label without an error assessment gives the reader too little information to judge usefulness.

## Coupling explains an approximation bound

One conservative binomial-to-Poisson error argument compares each Bernoulli indicator with an independent Poisson count having the same small mean. The total variation distance between one Bernoulli law and that Poisson law is $p(1-e^{-p})$, which is no larger than $p^2$. A coupling can make the two draws disagree with probability equal to that distance. Coupling independent pairs and using a union bound gives an event-probability error no larger than the sum of squared probabilities.

For equal probabilities this upper bound is $np^2$. It is a conservative bound, not the actual error for every event, and it should be clipped at one if the displayed bound exceeds the maximum possible probability difference. The argument also applies to a sum of independent unequal-probability Bernoulli variables, whose Poisson comparison has parameter equal to their summed probabilities. Independence is still required for the described coupling construction.

A bound can justify tolerance without calculating every event. It can also be too loose to be useful even when an approximation is good. Failure of a conservative bound to certify accuracy does not prove inaccuracy. Conversely, a small bound supports the stated maximum error but does not turn the approximation into an exact model or establish independence empirically.

## Normal approximation to discrete sums

A binomial count can be standardized using its mean and standard deviation, then approximated by a standard normal law in suitable regimes. The underlying count is discrete, so an event such as at most $k$ is commonly translated to a continuous threshold at $k+1/2$. This continuity correction aligns a unit-width cell around the last included integer with the cumulative event. It is an approximation device, not a change to the true support.

The approximation can be poor when success probability is near a boundary, the variance is small or the event is far into a tail. A large trial count by itself does not guarantee good behavior. Rules involving expected successes and failures are heuristics for central probabilities, not universal error guarantees. Exact binomial or Poisson calculations may be preferable for sparse counts.

When the mean and variance are known, approximate normality of a sum does not imply normality of its individual terms. Binary observations remain binary regardless of how bell-shaped their sum becomes. Similarly, a sampling average can be approximately normal while the population is strongly skewed. State which random variable receives the approximation.

## Law of large numbers under explicit assumptions

For independent identically distributed variables with finite variance, the sample average has the same mean as each variable and variance equal to the individual variance divided by sample size. Chebyshev's inequality therefore bounds the probability that the average differs from the mean by at least a positive tolerance by variance divided by sample size and tolerance squared. As sample size grows, this bound tends to zero, proving convergence in probability in this setting.

This is a weak law of large numbers with sufficient assumptions, not the most general available theorem. It does not say that every successive sample average gets closer to the target, nor that one finite sample must be accurate. The average can move away temporarily. It does not say that a biased sampling mechanism converges to the desired population mean; it can converge to a different mean associated with that mechanism.

For Bernoulli indicators, variance is $p(1-p)$, bounded by one quarter. This gives a distribution-free-in-$p$ variance bound within the independent Bernoulli model. It makes simulated event frequencies a natural setting for convergence demonstrations. The model probability is the target, and repeated random fluctuations around it remain possible at every finite trial count.

## A carefully scoped central limit theorem

For independent identically distributed variables with finite, positive variance, the centered sample sum divided by its standard deviation converges in distribution to the standard normal law. Equivalently, the standardized sample mean approaches that law. The theorem concerns distributional convergence as sample size grows, not a declaration that every dataset of thirty observations is normal. Finite-sample accuracy depends on the underlying distribution and the event.

Heavy tails can make convergence slow, and an infinite variance falls outside this stated theorem. Dependence requires different results and additional conditions. A zero-variance variable is degenerate and cannot be standardized by a positive standard deviation. These limitations are part of the statement, not inconvenient exceptions to hide after using the formula.

The central limit theorem supplies a rationale for some normal approximations and approximate Monte Carlo intervals. It does not prove the assumptions of the simulated or observed mechanism. Nor does it give an exact finite-sample tail probability without more information. For the simple events in this book, exact calculations provide benchmarks against which the approximation can be assessed.

## Monte Carlo estimation with indicator variables

To estimate a model event probability, independently repeat the stipulated experiment and record one when the event occurs and zero otherwise. The average indicator is the Monte Carlo estimate. Under the independent identical model, its expectation is the target probability and its variance is $p(1-p)/N$. Its standard error is the square root of that quantity. This uncertainty concerns numerical sampling from the assumed model.

When the target is unknown, substituting the observed frequency gives an estimated standard error. At a simulated frequency of zero or one, that plug-in estimate vanishes, but the true probability need not be exactly zero or one. Zero observed rare events does not establish impossibility. More appropriate interval methods or an exact binomial calculation may be needed near a boundary.

Simulated observations should preserve the mechanism. Without-replacement sampling must actually avoid repeated selected objects. A shared latent group must be drawn once per experiment if the modeled dependence is shared. Redrawing it for every component changes the law. Correct random-number calls do not compensate for a wrong experiment structure.

## Precision planning and the square-root cost

Because Monte Carlo standard error scales as one over the square root of trial count, halving it requires four times as many independent trials. Increasing trial count tenfold reduces standard error by only the square root of ten. This slow improvement motivates exact calculations, variance-reduction methods and better experiment coding when available. More trials are useful, but they are not a universal substitute for reasoning.

If a target probability is known or approximately anticipated, a desired standard error $s$ suggests trial count at least $p(1-p)/s^2$. Without a reliable anticipated probability, the bound one quarter gives a conservative count. A standard-error target is different from a guaranteed absolute-error tolerance. Turning it into a coverage claim requires an interval method or a probability bound with its own assumptions.

Rare events can have small absolute standard error while large relative error. An estimate near one in a million with only a few observed events is numerically fragile even if its decimal absolute variability looks tiny. Expected event count, relative precision and the purpose of the calculation should guide the trial budget. Reporting many decimal places after only a few events is misleading.

## Probability bounds for a Monte Carlo frequency

Chebyshev's inequality gives a finite-sample bound using the indicator variance: the chance of absolute error at least $\varepsilon$ is no larger than $p(1-p)/(N\varepsilon^2)$. It is conservative but transparent. Using one quarter removes dependence on the unknown probability within the independent Bernoulli setting. A bound exceeding one is uninformative and should not be treated as a meaningful probability estimate.

Hoeffding's inequality gives the sharper independent bounded-variable bound $P(|\hat p-p|\geq\varepsilon)\leq2e^{-2N\varepsilon^2}$. Solving it for a selected error probability gives a conservative trial-count requirement. This guarantee is about the mathematical sampling model and does not cover wrong simulation logic, floating-point bugs or mismatch between the model and reality. Those errors require separate checks.

The purpose of a bound is to make uncertainty accountable. It does not eliminate random error in every particular run. A ninety-five-percent guarantee permits failures within the stated probability model, and a fixed seed selects one deterministic pseudo-random realization rather than making a new guarantee. Display the estimate, target or benchmark, trial count and interpretation together.

## Seeds, reproducibility and independent replications

A pseudo-random generator produces a deterministic sequence from a seed. Recording the generator and seed lets another reader reproduce the same simulation. It does not prove the sequence is suitable for every numerical problem, and it does not make repeated execution with that seed independent. Reproducibility and stochastic independence are separate properties.

For classroom comparisons, common random inputs can make parameter changes easier to interpret because some numerical variation is shared. For assessing run-to-run variability, distinct streams or seeds are needed, with attention to the generator's properties. A report should say whether it used common inputs for comparison or independent replications for variability estimation. The experimental design of the simulation matters just as the experimental design of data collection does.

Store a sufficient record: model parameters, event definition, trial count, generator convention, seed, software version where relevant and the computed outputs. A screenshot alone cannot establish that a later code version reproduces the result. A hash of the source and an executable check can connect saved evidence to the code actually reviewed.

## Independent validation of a simulation

Validate a simulator against exact small cases before trusting it on large ones. A finite committee sampler can be compared with complete enumeration. A binomial sampler can be checked at probability zero, one and one half, as well as a moderate general case. A waiting sampler can be checked against exact survival probabilities. Degenerate parameters expose boundary errors that a typical interior example can miss.

Use more than one kind of check. Exact numeric fixtures test formulas. Property checks test normalization, monotonicity and support. Interaction checks test that controls update the intended model and reset restores defaults. Rendered checks test that the graph, labels and accessible text display the same result. A simulator can pass its internal formula test while its interface still labels a parameter incorrectly.

A statistical comparison should allow expected variation. Requiring every simulated frequency to equal its target is invalid for a finite sample. Conversely, allowing an extremely broad tolerance can let a biased simulator pass. A fixed-seed test can check reproducible outputs, while multiple-seed statistical checks can assess broad behavior. Record which kind of evidence supports each claim.

## Sensitivity analysis distinguishes parameter uncertainty

If a rate or probability is uncertain, calculate the event across a plausible parameter range rather than treating one guess as certain. Sensitivity analysis reveals how conclusions change with assumptions. It does not assign probabilities to the parameter values unless a separate probability model does so. A slider showing alternatives is not a posterior distribution or a confidence interval by itself.

Distinguish parameter sensitivity from Monte Carlo variation. Holding parameters fixed and increasing trials reduces simulation variability. Changing parameters changes the target probability. A broad range caused by uncertain assumptions will not disappear merely because the calculation becomes numerically more precise. A report should identify which uncertainty is dominant rather than presenting a narrow simulation interval as total uncertainty.

The same distinction applies to model families. An exponential and a gamma law with equal mean can yield different survival probabilities. Comparing them is a model-sensitivity exercise, not a sampling-error calculation. It can motivate collecting information about stages or hazard behavior, which helps decide which assumptions are defensible.

## Mixtures require updating after evidence

For a mixture, choose the latent group according to its prior weight, then generate from that group's conditional law. Marginal event probability is the weighted sum of group event probabilities. After observing an event, group weights update through Bayes' theorem. A conditional prediction must use the updated weights, not the original weights, unless the evidence is equally likely in every group.

Survival evidence is especially informative in a mixture of waiting rates. Slow groups become more likely among unfinished paths because their survival probabilities are larger. Each group may have a memoryless exponential wait while the marginal mixture does not. The additional wait depends on elapsed survival through changing group composition. This is an example of dependence and apparent duration effects produced by an unobserved variable.

For moments, use total expectation and total variance. The overall variance includes both average within-group variance and variance of group means. Averaging group variances alone misses heterogeneity. Averaging rates and then inverting likewise misses the mixture's mean duration. The arithmetic must follow the modeled variable and conditioning structure.

## Fully worked question 1: A rare-event approximation audit

**Question.** A stipulated process has two hundred independent opportunities, each succeeding with probability one hundredth. Let $X$ count successes. Calculate the exact probability of at least three successes and the Poisson approximation with matching mean. Compare absolute and relative error, state a conservative event-error bound, and explain why matching the means does not make the approximation exact.

**Solution, step 1: Calculate the exact complement.** The exact law is binomial with two hundred trials and probability $0.01$. The probability of at least three is one minus the sum of the zero, one and two masses: $1-[0.99^{200}+200(0.01)0.99^{199}+\binom{200}{2}(0.01)^2 0.99^{198}]$. This expression refers to a fixed number of trials and should be evaluated without rounding its component masses prematurely.

**Solution, step 2: Replace the count law and compare the same event.** The Poisson mean is two. Its probability of at least three is $1-e^{-2}(1+2+2)=1-5e^{-2}$, approximately $0.323324$. The exact tail is approximately $0.3233213055$. The approximation exceeds it by approximately $0.00000227835$, which is also the absolute error. Dividing by the exact probability gives relative error approximately $0.00000704671$, or $0.000704671$ percent. The agreement is excellent for this particular event; the saved numerical checker reproduces both calculations independently.

**Solution, step 3: State what the bound and moments establish.** The conservative coupling bound is $200(0.01)^2=0.02$ for any event-probability difference under this independent-trial mechanism. It is an upper bound, not the actual discrepancy for this tail. Binomial mean is two and variance is $1.98$, whereas the Poisson mean and variance are both two. Matching the means and being in a rare-event regime support an approximation; they do not make the support, variance or all event probabilities identical.

## Fully worked question 2: Monte Carlo precision and interpretation

**Question.** Independent simulations estimate an event whose exact model probability is one fifth. Ten thousand trials produce one thousand nine hundred and forty events. Calculate the estimate, its actual error against the benchmark, the theoretical standard error and a plug-in estimated standard error. Plan a trial count for standard error at most $0.002$ using the known benchmark, then using a worst-case Bernoulli variance. Explain which uncertainties these calculations cover.

**Solution, step 1: Distinguish the result from its target.** The Monte Carlo estimate is $1940/10000=0.194$. Its signed error is minus $0.006$ against the model benchmark $0.2$, and absolute error is $0.006$. The benchmark is known here because this is a verification exercise. In a general simulation problem it may be unavailable, so the actual realized error cannot be calculated merely from the observed count.

**Solution, step 2: Calculate numerical sampling uncertainty.** The theoretical standard error is $\sqrt{0.2(0.8)/10000}=0.004$. The plug-in value is $\sqrt{0.194(0.806)/10000}$, approximately $0.00395429$. A rough two-standard-error range around the estimate describes an approximate numerical uncertainty calculation, not a guaranteed finite-sample enclosure and not a statement about errors in the model or code. Here the realized error is one and a half theoretical standard errors.

**Solution, step 3: Plan with a stated variance.** Using the known probability, trial count must be at least $0.16/(0.002)^2=40000$ for the target standard error. Using the worst-case variance one quarter gives $62500$. Those counts concern independent indicator trials and a standard-error target. They do not guarantee a specified absolute error in every run, do not validate the simulation mechanism and do not establish that the model probability describes a real process.

## Fully worked question 3: A complete mixture waiting model

**Question.** Before a wait starts, group A is selected with probability one quarter and group B with probability three quarters. Conditional waiting times are exponential with rates one and three per hour respectively. Find the marginal mean and variance, the probability that the wait exceeds one hour, the probability of group A given that evidence, and the conditional mean additional wait. Explain why the mixture is not exponential with the average rate.

**Solution, step 1: Average moments rather than rates.** The mean wait is $(1/4)(1)+(3/4)(1/3)=1/2$ hour. The second raw moment is $(1/4)(2)+(3/4)(2/9)=2/3$ square hours. Therefore variance is $2/3-(1/2)^2=5/12$ square hours. The average rate is two and a half per hour; its reciprocal two fifths hour differs from the correct mixture mean one half hour.

**Solution, step 2: Calculate survival and update group weights.** One-hour survival is $(1/4)e^{-1}+(3/4)e^{-3}$, approximately $0.129310$. The posterior probability of A among surviving paths is $e^{-1}/(e^{-1}+3e^{-3})=1/(1+3e^{-2})$. This posterior is approximately $0.711235$. Slow group A receives more weight after survival than its original one-quarter weight. The update is determined by group survival likelihoods, not by a subjective preference for one group.

**Solution, step 3: Predict within groups and average with the new weights.** Each conditional exponential wait remains memoryless, so its mean additional wait is one hour in A and one third hour in B. If the posterior A probability is $w$, the conditional mean additional wait is $w+(1-w)/3$, approximately $0.807490$ hours. It differs from the original half-hour mean because the group composition has changed. The mixture survival is a sum of exponentials, not the exponential of the average rate; a common-rate simplification would change both the law and its predictions.

## Rounding, significant figures and honest reports

Keep sufficient intermediate precision and round at the end. Rounding component probabilities before subtracting can noticeably distort a small tail. A displayed zero can mean a rounded positive value, a numerical underflow or a genuinely impossible event. Label the situation rather than treating all three as equivalent. Scientific notation is often clearer for very small probabilities.

The number of reported digits should reflect the calculation and purpose. Exact rational probabilities can be retained alongside a readable decimal. Approximation results should be accompanied by an assessed discrepancy or stated bound. Monte Carlo estimates should include trial count and uncertainty, so a long decimal does not suggest precision unsupported by the experiment. More digits cannot repair a poorly specified model.

Words also require precision. Under the model signals a conditional mathematical conclusion. Estimated distinguishes a computed quantity from a known parameter. Approximately separates a numerical or distributional approximation from an exact identity. Independent should identify the relevant trials or variables rather than appear as a vague general property. Clear language is part of reproducibility.

## A compact record another reader can reproduce

A useful probability record contains the experiment, variable, support, assumptions, parameters and units, conditioning information, event, calculation method and result. For a simulation it also includes seed, trial count and numerical uncertainty. For an approximation it includes the original and replacement laws and an error assessment. These items can fit in a short report while still allowing a reader to reconstruct the answer.

The record should distinguish invented teaching data from observed evidence. An example of a batch mechanism with stipulated rates demonstrates Bayes' theorem; it does not establish actual batch quality. A simulated survival curve demonstrates a model consequence; it does not measure a real waiting process. Keeping labels explicit prevents educational examples from being mistaken for empirical claims.

Save executable calculations when the result supports publication. A review log should identify what was checked, which source version was checked and what limitations remain. A passing count of assertions is evidence of those assertions, not proof that every sentence in a textbook is correct. Human academic review and feedback can add a different kind of validation.

## A convergence explorer with accountable randomness

The convergence explorer generates independent-model Bernoulli indicators from a documented seeded stream and shows the running average together with its target probability. The horizontal coordinate is trial count, not elapsed real-world time. The displayed estimate can move away from its target temporarily, making the law of large numbers' probabilistic meaning visible. Increasing trials narrows typical fluctuations without making a monotonic path.

Its text output includes final count, estimate, target, signed error and theoretical standard error. Changing the probability changes the target law; changing trial count changes numerical sampling variability. A reset restores defaults and the same seed, reproducing the initial path. Repeatedly pressing the same fixed-seed run is intentionally reproducible and is not presented as independent replication.

At probabilities zero and one, the indicator law is degenerate and every sample equals the target. The standard error is truly zero there because the model itself is deterministic. This differs from observing zero events at an interior probability, where the plug-in error estimate can vanish despite uncertainty. The explorer's labels and tests keep those two boundary situations distinct.

## Common failures and a correction strategy

When an answer seems implausible, inspect the event and mechanism before repeating arithmetic. A conditional source probability greater than one often indicates a denominator error. A negative variance can indicate inconsistent moments or loss of floating-point precision. A probability outside zero to one indicates a formula, support or numerical failure. A count above a finite inventory indicates a sampling implementation mismatch.

Correct the earliest broken link in the reasoning chain. If the model is wrong, replace or qualify it before recomputing. If the event is wrong, rewrite the probability expression. If units are inconsistent, convert all related quantities. If numerical cancellation is the issue, use a stable formulation. If the simulator changes the mechanism, repair its random procedure rather than widening a tolerance until it passes.

After a correction, rerun the checks affected by it and inspect the explanation. Changing a formula can alter graph labels, expected values, worked answers and interpretation. A coherent educational resource needs agreement across those representations. The final report should describe the corrected result and retained assumptions, not merely state that an error disappeared.

## What this book establishes and what comes next

This book develops probability models from events and axioms through conditional updating, random variables, moments, dependence and named distribution families. It gives original worked questions and interactive demonstrations whose model outputs can be checked. It does not establish the truth of those models for every real dataset, replace sampling design, or provide advanced inference procedures without their assumptions.

The next major courses will use these foundations to develop estimators, sampling distributions, tests, intervals, regression and more sophisticated computational methods. Those topics rely on careful distinctions already introduced: parameter versus observation, conditional versus marginal law, model versus evidence, and numerical precision versus total uncertainty. Carry those distinctions forward rather than treating probability as a collection of isolated formulas.

A strong final habit is to ask four connected questions of every result: what experiment was modeled, what event was calculated, what assumptions made the calculation valid, and what evidence supports applying it? The mathematics provides disciplined answers inside a model. Responsible statistical work connects those answers to the actual question and retains the limits that the evidence cannot remove.
