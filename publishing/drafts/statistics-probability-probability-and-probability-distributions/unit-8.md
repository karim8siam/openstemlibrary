# Unit 8: Uniform, Exponential and Gamma Distributions

## Learning aims and the meaning of a continuous model

Continuous probability begins with an observation mechanism and a support, not with a curve selected because it looks smooth. This unit develops three families with different mechanisms: the uniform distribution allocates equal probability to equal-length subintervals of a bounded range; the exponential distribution describes a nonnegative wait with constant instantaneous hazard; and the gamma distribution includes sums of independent exponential waits with a common rate. These statements concern stipulated mathematical models. They are hypotheses to assess when a real dataset is involved.

The reader should be able to normalize each density, derive its moments, calculate interval and survival probabilities, distinguish rate from scale, and interpret conditioning on an unfinished wait. The reader should also recognize that a density height is not an event probability. A value of a density can exceed one because it carries inverse measurement units. Its integral over an interval, rather than its height at a point, gives probability. A continuous variable assigns probability zero to each particular value while retaining positive probability over intervals.

There are several ways to connect these families. A uniform input can be transformed into an exponential wait through an inverse distribution function. A sum of exponential stages produces a gamma law when the stages are independent and have a common rate. Equal means do not make these mechanisms interchangeable: their supports, variances and conditional remaining times can differ. Following those differences is more useful than memorizing a table of distribution names.

## Uniform probability as a constant density

Let $a<b$ be finite bounds. A continuous uniform variable on that interval has density $f(x)=1/(b-a)$ between the bounds and zero elsewhere. Integrating the constant height over the support gives one, so the density is normalized. For an interval entirely inside the support, probability is its length divided by the support length. For an interval extending beyond the support, only the overlapping length contributes. Negative overlap must be replaced by zero rather than interpreted as a negative probability.

The uniform assumption is stronger than knowing only minimum and maximum possible values. Knowing that a reading lies between two bounds does not establish that its probability is proportional to interval length. Concentration near the center, near a boundary, or near preferred settings would contradict a constant density. A uniform law is appropriate when the mechanism or an explicitly chosen modeling assumption gives equal-length regions equal probability. It is not the default meaning of uncertainty.

Endpoints can be included or excluded without changing this continuous law because they have probability zero. This convention does not allow an impossible value outside the bounds, and it does not turn a discrete random choice among integers into a continuous uniform experiment. Selecting one of six integers gives six positive point masses. Selecting a real position uniformly along a segment gives a density. Their means might coincide while their event probabilities differ.

$$
P(c<X<d)=\frac{\max\{0,\min(d,b)-\max(c,a)\}}{b-a},\qquad c<d.
$$

## The uniform CDF and its quantiles

The CDF is zero below the lower bound, increases linearly from zero to one across the support, and is one at and above the upper bound. Writing the whole piecewise function matters: the expression $(x-a)/(b-a)$ is valid only within the support. Applying that expression to a point below the lower bound gives a negative number, which cannot be a CDF. Applying it above the upper bound gives a number exceeding one. Boundary logic is part of the calculation.

For a probability level strictly between zero and one, the quantile is $a+p(b-a)$. This follows by solving the linear CDF equation, not by guessing a percentile from the density height. The median is the midpoint. The lower and upper quartiles divide the support into four equal lengths, which also have equal probabilities under this particular law. In another distribution, equal probability intervals can have very different lengths.

Quantiles preserve measurement units. If the variable is measured in seconds, its quantile is a duration in seconds. The probability level is dimensionless. A useful check is to substitute the calculated quantile into the CDF and recover the specified probability. Another is monotonicity: larger probability levels should produce no smaller quantiles. These checks catch reversed bounds or sign errors before an answer reaches a report.

## Deriving the uniform mean and variance

Integration gives the uniform mean $(a+b)/2$. One route is to integrate $x/(b-a)$ from the lower to the upper bound and factor the difference of squares. A more revealing route writes $X=a+(b-a)U$ with $U$ uniform on zero to one. Then the mean follows from $E[U]=1/2$ and linearity. Both routes state the mechanism that makes the midpoint the mean; a bounded but asymmetric variable need not have that midpoint as its mean.

The second raw moment on zero to one is one third, so the variance of the standard uniform variable is $1/3-1/4=1/12$. Scaling gives variance $(b-a)^2/12$ and standard deviation $(b-a)/\sqrt{12}$. Translating the interval changes the mean but leaves its length and variance unchanged. Doubling every length multiplies variance by four. These relationships are useful dimensional checks when units change.

Uniform symmetry gives a zero third central moment. It does not imply that a uniform distribution has the same fourth standardized moment as a normal distribution. In fact its raw kurtosis is $9/5$, reflecting the bounded shape. Symmetry controls odd centered moments when they exist, while tail weight affects even moments. The distinctions introduced in the previous unit remain relevant within this named family.

## Affine transformations and changes of units

An increasing affine transformation $Y=c+dX$ with positive $d$ maps a uniform law to a uniform law on the transformed bounds. Its density must be divided by $d$ because the same probability is spread over an interval that is $d$ times as long. A negative multiplier reverses endpoint order, so the smaller transformed bound must be identified before writing the new support. The density scaling uses the absolute multiplier.

Suppose a uniform position is measured first in meters and then in centimeters. The numerical support length increases by a factor of one hundred, while the density height decreases by that factor. Interval probability remains unchanged. This is why treating a density height as probability creates a unit-dependent answer: the density changes numerically under a unit conversion, whereas the probability of the corresponding physical event does not.

Nonlinear transformations generally destroy uniformity. Squaring a positive uniform variable concentrates transformed density near the lower end because equal transformed intervals correspond to unequal original lengths. A probability calculation can proceed in original space by solving the event inequality, or in transformed space by using a Jacobian. Agreement between those routes is an excellent check. Uniform input does not mean every derived quantity is uniform.

## Conditioning a uniform observation on an interval

If a uniform variable is known to lie in a positive-length subinterval of its support, its conditional distribution is uniform on that subinterval. The original constant density is divided by the probability of the conditioning interval. Since that probability is subinterval length divided by full-support length, the conditional density becomes the reciprocal of the subinterval length. The full-support length cancels because the conditioning has changed the eligible set.

For an interval with zero length, ordinary positive-probability conditioning is unavailable. A statement about a regular conditional law given an exact continuous value belongs to a more careful framework; it cannot be justified by dividing by a zero event probability. In this unit, conditioning statements involving a uniform variable use intervals of positive probability. This keeps the denominator explicit and avoids confusing a measured exact value with a probability-positive event.

Uniform conditioning on a union of separated intervals gives constant density across the eligible pieces, not automatically uniform probability across the pieces as categories. Pieces with different lengths receive different masses. The distinction echoes finite sampling: equal density per unit of length is not equal probability per arbitrarily named region. The observation mechanism determines what is equally weighted.

## Exponential survival from a constant hazard

An exponential waiting variable $T$ with rate $\lambda>0$ has density $\lambda e^{-\lambda t}$ for nonnegative time. Its survival function is $S(t)=P(T>t)=e^{-\lambda t}$ for $t\geq0$. The rate has inverse-time units so that the exponent is dimensionless. Integrating the density from zero to infinity gives one. Integrating from zero to a specified duration gives the CDF $1-e^{-\lambda t}$.

The hazard at a time with positive survival is the density divided by survival. It represents a limiting conditional event rate among paths that have survived to that time, not the unconditional probability of an event at that exact instant. For an exponential law the ratio is the constant rate. Over a short additional duration, the conditional completion probability is approximately rate times duration, with approximation error tending to zero relative to duration as the duration shrinks.

A constant hazard means elapsed time does not change the remaining waiting law under the model. It does not mean the cumulative chance of completion remains constant: the CDF increases with elapsed time. Nor does it mean an event happens every reciprocal-rate units exactly. The mean is reciprocal rate, but a realized wait varies. These are separate interpretations of rate, cumulative probability and expected duration.

## Memorylessness and what it does not imply

For nonnegative durations $s$ and $t$, exponential survival satisfies $S(s+t)=S(s)S(t)$. Dividing by $S(s)>0$ gives $P(T>s+t\mid T>s)=P(T>t)$. Thus a path that has lasted beyond duration $s$ has the same model distribution of additional wait as a fresh path. The property concerns conditional distributions, not a claim that a physical process forgets every aspect of its history.

One must condition on an unfinished wait rather than on its completed value. If a completion has already occurred, there is no remaining first-event wait. If additional state such as workload, temperature or stage progress is observed, conditioning on that state may change predictions even if an exponential approximation was used before observing it. A simple exponential model usually omits such state; its memorylessness should not be exported beyond the information structure it actually specifies.

The multiplication identity also characterizes the ordinary continuous memoryless waiting law under appropriate regularity and properness conditions. A decreasing, continuous survival function with value one at zero and the multiplicative identity must be exponential with positive rate. Taking negative logarithms converts multiplication to addition. A continuous additive function on nonnegative durations is linear, producing the exponential survival. The zero-rate constant-survival case is not a proper finite exponential wait.

## Exponential moments by integration and survival

The mean of an exponential variable is $1/\lambda$, its second raw moment is $2/\lambda^2$, and its variance is $1/\lambda^2$. Substitution $u=\lambda t$ reduces each integral to a standard gamma integral. Alternatively, the mean of any nonnegative variable equals the integral of its survival function, with an extended infinite value allowed. For the exponential law this integral is the reciprocal rate.

The survival-integral identity follows from writing a nonnegative realized duration as the area of the indicator that it exceeds each possible threshold. Taking expectation swaps nonnegative integrations and averages. This reasoning makes the identity useful beyond exponential waiting: a variable can be finite almost surely while its survival area is infinite. An observed completion does not establish the existence of a finite population mean.

The exponential standard deviation equals its mean, and its coefficient of variation is one. A data mechanism with much smaller relative variability or a changing hazard needs another model or a clear approximation argument. The exponential law is right-skewed, with skewness two and excess kurtosis six. These shape features follow from its moments and are consequences of the model, not additional adjustable parameters.

## Rate, scale and parameter conversions

Some references use an exponential scale $\theta=1/\lambda$ and write density $e^{-t/\theta}/\theta$. The rate and scale versions describe the same distribution. Their numerical values are reciprocals and their units differ. A rate of two completions per hour corresponds to scale one half hour, while a scale of two hours corresponds to rate one half per hour. Treating the same number as both parameters silently changes the model.

When converting time units, rates transform inversely to time values. A rate of two per hour is one thirtieth per minute, not one hundred and twenty per minute. A mean of one half hour is thirty minutes. Checking the product of rate and mean gives one in either unit system. A survival exponent such as rate times duration should have the same numerical value after consistent conversion.

Every reported parameter should include its convention and units. An unlabeled phrase such as gamma parameter two is inadequate because it could identify shape, rate or scale. Software often accepts one convention while textbooks display another. Before comparing outputs, inspect the formula used, the support, and the argument order. Matching names alone is insufficient.

## Quantiles, interval events and numerically stable tails

The exponential quantile at a probability level between zero and one is $-\log(1-p)/\lambda$. For the median, this becomes $\log(2)/\lambda$, which is smaller than the mean. A right-skewed law need not have half its probability below its mean. The percentile formula has a simple interpretation through survival: the remaining mass above the quantile is $1-p$.

An interval probability from $c$ to $d$, with nonnegative ordered bounds, is $e^{-\lambda c}-e^{-\lambda d}$. If the lower bound is negative, it should first be clipped to zero; time below zero is outside the support. For a very small duration, calculating the CDF as one minus an exponential can lose relative numerical accuracy through subtraction of nearly equal floating-point values. A specialized negative exponential-minus-one calculation can preserve those small probabilities.

For extreme right tails, using survival directly avoids subtracting a CDF rounded to one. A rounded display of one does not mean the mathematical tail is zero. Similarly, a quantile at probability one is infinite, whereas probabilities strictly below one have finite quantiles. A calculator should reject inappropriate endpoints or label their extended values rather than accidentally produce a plausible finite duration.

## The gamma integral and its recurrence

The gamma function is defined for positive real shape $\alpha$ by $\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du$. Near zero, integrability requires positive shape. At infinity, the exponential factor dominates polynomial growth. Integration by parts gives $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$, and $\Gamma(1)=1$. For positive integer shape, the recurrence gives factorial values: $\Gamma(k)=(k-1)!$.

The gamma function extends a factorial-related normalization beyond integers. This does not mean a noninteger number of actual waiting stages exists. Integer-shape waiting constructions have a direct stage-count interpretation. Noninteger gamma laws are valid continuous distributions whose parameters control shape and scale, but a stage-count story should not be stated literally without a separate mechanism.

Normalization constants are essential. The expression $x^{\alpha-1}e^{-\lambda x}$ has the right broad shape for a gamma curve, but its area is not generally one. Substitution identifies its integral as $\Gamma(\alpha)/\lambda^\alpha$. Multiplying by the reciprocal gives a valid density. A plot that looks like a familiar curve cannot substitute for this calculation.

## Gamma density with shape and rate

This book uses gamma shape $\alpha>0$ and rate $\lambda>0$, with density $\lambda^\alpha x^{\alpha-1}e^{-\lambda x}/\Gamma(\alpha)$ for positive $x$. The density is zero for negative values. The value assigned at zero can be handled as a boundary convention without changing any probability. For shape below one, the density becomes unbounded as the boundary is approached, but the area remains finite because the singularity is integrable.

For shape equal one, the gamma density reduces to the exponential density. For shape greater than one, the interior mode is $(\alpha-1)/\lambda$. For shape at or below one there is no positive interior maximizing point; density is nonincreasing away from the boundary, with divergence at zero for shape below one. A graph should distinguish boundary behavior from an interior mode and should not claim that an unbounded density is an infinite probability.

Holding shape fixed and increasing rate compresses the time axis and lowers the mean. Holding rate fixed and increasing shape adds relative concentration around a later mean. The two parameters play different roles. A parameter slider is educational only if its labels make that difference clear; otherwise a moving curve can reinforce an ambiguous interpretation.

## Gamma moments and transforms

Integrating a raw power against the gamma density gives $E[X^r]=\Gamma(\alpha+r)/(\Gamma(\alpha)\lambda^r)$ when $\alpha+r>0$. The condition matters especially for negative powers, which can fail to be integrable near zero. Positive integer moments always exist. Applying the recurrence gives mean $\alpha/\lambda$ and variance $\alpha/\lambda^2$. Standard deviation is $\sqrt{\alpha}/\lambda$.

The MGF is $(\lambda/(\lambda-t))^\alpha$ for $t<\lambda$, derived by replacing the exponential rate in the normalization integral with $\lambda-t$. Outside that domain the integral diverges. The cumulant generator is $-\alpha\log(1-t/\lambda)$ near zero. Its derivatives give cumulants $\alpha(r-1)!/\lambda^r$. In particular, skewness is $2/\sqrt{\alpha}$ and excess kurtosis is $6/\alpha$.

These formulas explain concentration as shape increases. Relative standard deviation is $1/\sqrt{\alpha}$ even when absolute standard deviation increases at fixed rate. Relative and absolute spread answer different questions. When comparing models with equal means, rate must change with shape, and then absolute variance decreases as shape increases. State what is being held fixed before interpreting a plotted comparison.

## Sums of independent exponential stages

If $X_1,\ldots,X_k$ are independent exponential variables with a common rate, their sum has gamma shape $k$ and that rate. Multiplying MGFs produces the gamma MGF, with the same finite neighborhood of zero establishing the law. An alternative proof uses convolution. For two stages, integrating the product of exponential densities over all allocations of a fixed total produces a factor equal to the total duration.

The common-rate and independence conditions are essential. Unequal exponential stage rates give a different sum law, though the mean is still the sum of reciprocal rates. Dependent stages do not inherit the product-transform calculation. A modeler should not replace every sum of positive waits by gamma merely because gamma contains one useful waiting construction. The density follows from the specified joint stage mechanism.

For positive integer shape, the gamma distribution is also called an Erlang distribution. Its total wait does not have the exponential memoryless property when more than one stage is required. Knowing that the total completion time exceeds an elapsed duration changes what remains. Observing the exact stage currently active gives more information than observing elapsed time alone. The conditional prediction depends on which information was recorded.

## Integer-shape survival and the Poisson connection

For integer shape $k$, gamma survival can be written $e^{-\lambda t}\sum_{j=0}^{k-1}(\lambda t)^j/j!$. Repeated integration by parts derives the finite sum. A second route starts with a homogeneous Poisson event process: the time of the $k$th event exceeds $t$ exactly when fewer than $k$ events have occurred by $t$. Summing the corresponding Poisson masses gives the same expression.

The connection concerns a particular process with independent exponential gaps and a constant common rate. A count distribution at one duration alone does not prove all those process properties. The complete temporal construction supplies the waiting law. In the calculation, the dimensionless quantity rate times duration must be used consistently in both the exponential factor and every power.

Integer-shape survival is convenient for elementary computations because it avoids a general incomplete gamma routine. For noninteger shape, numerical integration or a reliable special-function implementation is needed. Approximating a noninteger shape by a nearby integer simply to use the finite sum changes the distribution. It can be a deliberate approximation, but the change and its effect should be assessed rather than hidden.

## Remaining lifetime under a gamma law

For any nonnegative waiting variable with positive survival at $s$, the probability of lasting at least an additional duration $t$ given survival to $s$ is $S(s+t)/S(s)$. The exponential law cancels the dependence on $s$. For gamma shape two, survival is $e^{-\lambda s}(1+\lambda s)$, so the conditional additional survival is $e^{-\lambda t}(1+\lambda(s+t))/(1+\lambda s)$. The ratio depends on elapsed duration.

This gives a direct way to demonstrate nonmemorylessness without vague statements about aging. At rate one, survival another unit from the start is $2/e$. After already lasting one unit, survival another unit is $3/(2e)$. The conditional probabilities differ. Both are probabilities of an additional wait exceeding one, but they use different eligible populations. Their difference is a consequence of the two-stage construction.

Mean remaining lifetime can also be calculated by integrating conditional survival. For shape two it is $(s+2/\lambda)/(1+\lambda s)$. At the start this is the total mean $2/\lambda$, while at large elapsed time it approaches $1/\lambda$. The model's long-surviving paths increasingly resemble those whose final stage remains. This explanation is tied to the mathematical stage model and does not establish the behavior of any particular physical device.

## Right censoring, truncation and rounded observations

A record saying that a wait exceeded five hours contributes survival probability at five hours to a model for that observation. It is not a completed wait of exactly five hours. A completed continuous wait is represented through a density, or through interval probability when recorded with finite resolution. Confusing these observation types changes the calculation before any inference begins.

If the dataset includes only waits that finish before a cutoff, it is a truncated sample rather than a complete sample with censored records. The conditional density of the included waits must be divided by their probability of inclusion. This generally shifts the observed mean downward relative to the untruncated waiting law. A display of completed waits alone can therefore look less variable and shorter even when the underlying mechanism has not changed.

Rounding a wait to the nearest minute produces a discrete recorded variable derived from an underlying continuous time. The chance of a displayed minute value is the continuous probability over its rounding interval, adjusted at the nonnegative boundary. Exact-time probability zero does not mean every recorded rounded value has zero probability. The observation rule connects continuous theory to the actual data format.

## Mixtures of rates and apparent aging

Suppose an unobserved group chooses an exponential rate before a wait starts. The overall survival is a weighted average of exponential survivals. Unless all positive-weight rates are equal, the mixture is generally not exponential. Among paths that have survived a long duration, slower groups receive larger posterior weight. The mixture hazard can therefore change with duration although each group separately has a constant hazard.

This is a useful explanation of why marginal and conditional models differ. Observing the group produces a simple exponential law. Omitting the group creates a mixture whose remaining-time prediction updates after survival. Averaging the original rates and using a single exponential does not preserve the mixture survival or its mean. The mixture mean is the weighted average of reciprocal rates, not the reciprocal of the weighted rate.

The same reasoning warns against using a fitted marginal hazard as a literal mechanism for every individual. Heterogeneity can produce duration patterns without a within-group change. A probability model can describe such patterns and demonstrate a possibility, but identifying the real source of heterogeneity requires data and an appropriate investigation. Mathematics distinguishes explanations; it does not select a causal explanation by itself.

## Fully worked question 1: A uniform transformation and selected interval

**Question.** A stipulated position $X$ is uniform from two to eight. Define $Y=X^2$. Find $P(9<Y<36)$, the mean of $Y$, its CDF on its support, and its density there. Given that $X>5$, find $P(X<7\mid X>5)$. Explain why $Y$ is not uniform.

**Solution, step 1: Translate the event and integrate the original variable.** Since the original position is positive, $9<X^2<36$ is equivalent to $3<X<6$. The eligible length is three out of six, giving probability one half. The second raw moment of the original uniform variable is $(2^2+2\cdot8+8^2)/3=28$, which is the mean of $Y$. Squaring the mean of $X$, which is five, would give twenty-five and would omit the original variance of three.

**Solution, step 2: Transform the distribution with its support.** The transformed support is four to sixty-four. Within it, $F_Y(y)=P(X\leq\sqrt y)=(\sqrt y-2)/6$, with CDF zero below four and one at and above sixty-four. Differentiation gives $f_Y(y)=1/(12\sqrt y)$ in the support interior. This density decreases rather than remaining constant. Equal-length intervals on the squared scale correspond to unequal-length intervals on the original scale.

**Solution, step 3: Change the denominator when conditioning.** The event $X>5$ restricts the eligible interval to length three, from five to eight. The part also satisfying $X<7$ has length two. The conditional probability is therefore two thirds. This is a conditional calculation in original position space. It does not require treating the transformed variable as uniform, and it does not assign positive mass to any endpoint.

## Fully worked question 2: An unfinished exponential wait

**Question.** A stipulated completion time is exponential with rate two per hour. Calculate its mean and median in minutes, the probability of completion within fifteen minutes, and the probability that a wait already exceeding one hour lasts more than another half hour. Determine the ninetieth percentile in minutes and distinguish it from the mean.

**Solution, step 1: Convert time consistently.** The mean is one half hour, or thirty minutes. The median is $\log(2)/2$ hours, approximately $20.7944$ minutes. Fifteen minutes is one quarter hour, so the completion probability is $1-e^{-2(1/4)}=1-e^{-1/2}$, approximately $0.393469$. Using fifteen directly with a per-hour rate would create a different and invalid unit interpretation.

**Solution, step 2: Condition on surviving the first hour.** The required survival is $S(1.5)/S(1)=e^{-3}/e^{-2}=e^{-1}$, approximately $0.367879$. Memorylessness makes it the same as the survival probability beyond one half hour from a fresh start. It is not the unconditional probability of exceeding one and a half hours, which is $e^{-3}$. Conditioning changes the denominator.

**Solution, step 3: Solve a percentile equation.** Setting survival to one tenth gives duration $\log(10)/2$ hours. Multiplication by sixty gives $30\log(10)$ minutes, approximately $69.0776$. This percentile marks a duration by which ninety percent of modeled waits finish. The thirty-minute mean is an average over all waits and need not have ninety percent, or even fifty percent, below it. Neither quantity promises the completion time of one realized path.

## Fully worked question 3: Three independent exponential stages

**Question.** A procedure has three independent stages, each exponential with rate two per hour. Let $T$ be its total duration. State its law, mean and variance. Calculate $P(T>2)$ and $P(T>3\mid T>1)$. Compare the latter with $P(T>2)$ and explain why the total wait is not memoryless.

**Solution, step 1: Use the common-rate independent-stage construction.** The total is gamma with shape three and rate two per hour. Its mean is three halves hours and variance three quarters square hours. Its MGF is $(2/(2-t))^3$ for transform argument below two per hour in a consistent unit convention. The variance follows by adding the three independent stage variances, each one quarter square hours.

**Solution, step 2: Calculate finite-sum survival.** At two hours the dimensionless rate-duration product is four, giving survival $e^{-4}(1+4+4^2/2)=13e^{-4}$, approximately $0.238103$. The one-hour survival is $5e^{-2}$ and the three-hour survival is $25e^{-6}$. These calculations count zero, one or two process events by each duration under the equivalent Poisson-stage construction.

**Solution, step 3: Condition on the unfinished total.** The requested conditional probability is $25e^{-6}/(5e^{-2})=5e^{-4}$, approximately $0.0915782$. It differs from the fresh two-hour survival $13e^{-4}$. Knowing that the total already exceeded one hour changes the distribution of its additional duration. The total of three exponential stages is gamma, not exponential; memorylessness of each independent stage does not make their summed completion time memoryless.

## Simulating waits without changing the mathematical law

An inverse-CDF simulation uses a uniform input strictly between zero and one. For an exponential wait, transforming that input by $-\log(1-U)/\lambda$ generates the desired CDF. A program must handle its pseudo-random generator's endpoint convention: feeding an exact one creates an infinite logarithm, while an exact zero produces a boundary value with a representation issue in a supposedly continuous sample. A documented open-interval transformation avoids ambiguous endpoints.

Integer-shape gamma simulation can add independent exponential draws. The word independent describes the intended random-input construction; a deterministic pseudo-random stream is an approximation designed to mimic that construction. A fixed seed makes the result reproducible, not more theoretically accurate. Repeating the same seeded experiment yields the same paths and is not a collection of fresh independent replications.

A histogram of simulated waits should be compared with interval probabilities or density-scaled bars. Count heights cannot be compared directly with a probability density curve without matching the vertical scale. A survival explorer can be even clearer: it displays exact survival and the empirical proportion of draws above each threshold, showing both model consequences and sampling variation. A single simulated picture cannot prove a distributional identity.

## Numerical and interpretive audit of a waiting calculation

Before evaluating a continuous waiting probability, identify whether the question is a fresh-start event, an unfinished conditional event, a completed duration, or a rounded observation. Then state support, parameter convention, units and assumptions. A result can be numerically accurate for the wrong event. Writing the probability expression first exposes that problem before arithmetic conceals it.

Check limiting behavior. Uniform CDFs reach zero and one at their bounds. Exponential survival starts at one and decreases toward zero. Gamma survival does the same even when its density vanishes or diverges at the boundary. A survival value increasing with the duration indicates a sign, parameter or implementation error. For conditional survival, setting additional duration to zero should give one whenever the denominator is positive.

Check moments against units and construction. A three-stage common-rate total has three times a stage mean, not the same mean; its variance is three times a stage variance under independence. A square transformation produces square units. A conditional interval calculation uses the eligible interval in its denominator. These simple checks complement numerical integration and simulation because they test meaning as well as arithmetic.

## Beyond the elementary families

A gamma law with an added fixed delay has a shifted support and a survival function that stays one before the delay. It is not the unshifted gamma law with a larger shape merely because its mean is later. A sum of unequal exponential stages can have the same mean as an integer-shape gamma but a different variance and survival. A mixture of stages can have a different mechanism again. Similar summary numbers do not identify a distribution.

The continuous uniform law can model a randomized offset in a specified interval. The exponential law can describe one event gap in a homogeneous process. The integer-shape gamma can describe the time until several such events. These are mechanisms that make the formulas intelligible. When a real process includes scheduled events, changing rates, minimum delays or dependence, start from those features instead of forcing the process into a convenient named family.

Later courses will develop estimation, goodness-of-fit assessment and more general event-time models. The task here is narrower: reason correctly from an explicitly given probability law and recognize the assumptions under which that law arises. Keeping that boundary visible prepares the reader to test models with data rather than treating textbook family names as conclusions about the world.
