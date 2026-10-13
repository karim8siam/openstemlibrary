# Unit 9: Normal and Beta Distributions

## Learning aims and two contrasting supports

The normal and beta families describe fundamentally different supports. A nondegenerate normal variable can take any real value and has a symmetric bell-shaped density. A beta variable lies within a bounded interval, conventionally zero to one, and can be symmetric, skewed, concentrated in the interior or concentrated near the boundaries. Choosing between these families requires understanding the variable and its mechanism, not simply deciding which curve looks familiar.

This unit develops normalization, parameter meaning, moments, interval probabilities and transformations for both laws. It also explains when linear combinations of normal variables remain normal, how beta moments arise from normalization ratios, and why a density that diverges near a boundary can still define a proper probability distribution. The reader should be able to distinguish a random proportion from an estimated fixed probability and a normal model for measurements from a normal approximation for an estimator.

Both families offer useful mathematical structure, but neither validates its own application. A normal law cannot assign exactly zero probability to physically impossible negative values unless it is degenerate or modified. A beta law does not describe a count merely because the count divided by its sample size lies between zero and one. Keeping the support and observation mechanism explicit prevents an attractive formula from answering the wrong question.

## The standard normal density and its normalization

The standard normal density is $\phi(z)=e^{-z^2/2}/\sqrt{2\pi}$ on the whole real line. The normalization factor comes from the Gaussian integral. Squaring the integral of $e^{-z^2/2}$ creates a two-dimensional integral; polar coordinates turn the exponent into minus half the squared radius and contribute a radial Jacobian. The angular integral is $2\pi$ and the radial integral is one, so the original positive integral is $\sqrt{2\pi}$.

This proof illustrates a general principle: a change of variables must transform both the integrand and the element of area. Forgetting the polar radius factor gives an incorrect normalizing constant. It also explains why a simple-looking density can have a normalizing constant involving pi even though the original probability problem concerns one numerical variable. The calculation uses geometry to evaluate an integral, not a physical claim that the variable is an angle.

The density is symmetric because its exponent depends on the square of the argument. Its maximum is at zero. Equal-density points on opposite sides of zero have equal heights, and corresponding reflected intervals have equal probabilities. Symmetry does not make equal-length intervals at different distances from zero equally probable: intervals near the center have more probability than equally wide intervals in the tails.

## Location and scale of a general normal law

Writing $X=\mu+\sigma Z$ with standard normal $Z$ and $\sigma>0$ defines a normal law with mean $\mu$ and standard deviation $\sigma$. Its density is the standard density at $(x-\mu)/\sigma$, divided by $\sigma$. The division accounts for horizontal scaling and preserves total area. This book writes the law as $N(\mu,\sigma^2)$, so the second parameter in that notation is variance rather than standard deviation.

Software conventions differ, and parameter labels must be inspected. A command taking a standard deviation of four does not implement a distribution with variance four; it implements variance sixteen. A stated $N(10,4)$ in this book has standard deviation two. Checking the density denominator and exponent can resolve notation ambiguity when a bare family label cannot.

The mean controls horizontal location while standard deviation controls spread. A larger standard deviation lowers the peak and spreads probability over a broader range. The total area remains one. Density heights measured in inverse units change with scale, but the probability inside a fixed number of standard deviations does not. A normal curve is therefore a location-scale family rather than a collection of unrelated shapes.

## Standardization changes the event as well as the variable

For a nondegenerate normal variable, $Z=(X-\mu)/\sigma$ is standard normal. An interval event must be standardized at both endpoints: $a<X<b$ becomes $(a-\mu)/\sigma<Z<(b-\mu)/\sigma$. The denominator is positive, so inequality order is preserved. If a transformation uses a negative coefficient, the order must instead reverse before the event is evaluated.

Standardization measures signed distance from the mean in standard-deviation units. A score of minus two is below the mean, not a negative probability. The score can be any real number. The CDF converts that score into a probability. A common error is to report the standardized endpoint itself as the desired probability or to use its absolute value before deciding whether the question concerns a left or right tail.

Units disappear from the standardized value because numerator and denominator have matching measurement units. If an original quantity is converted from meters to centimeters, its mean and standard deviation must be converted too. A standardized score should remain unchanged. This provides a practical audit of data exported by different measurement systems.

## The normal CDF, symmetry and interval arithmetic

Define $\Phi(z)=\int_{-\infty}^z\phi(u)\,du$. The CDF does not have an elementary antiderivative, but reliable numerical routines and tables evaluate it. Symmetry gives $\Phi(-z)=1-\Phi(z)$. An interval probability is the upper-end CDF minus the lower-end CDF. A right tail is $1-\Phi(z)$ in exact mathematics, although a dedicated survival routine is preferable numerically in an extreme tail.

A probability table must be read according to its convention. Some tables give the full lower-tail CDF; others give area between zero and a positive score; still others give upper tails. The same listed decimal has different meaning under those headings. Before using a value, check the table's diagram and test its zero-score entry: a lower-tail table gives one half, whereas a center-to-score area gives zero.

Continuity means strict and non-strict inequalities have the same probability for this nondegenerate law. It does not make different thresholds equivalent. Rounding a score before using a table introduces an approximation; rounding the final probability introduces another. State the precision used, especially when a tail decision is sensitive to the threshold.

## Normal quantiles and central intervals

A standard normal quantile $z_p$ solves $\Phi(z_p)=p$ for a level strictly between zero and one. A quantile of a general normal variable is $\mu+\sigma z_p$. The median is the mean because the standard median is zero. A central interval with probability $1-\alpha$ uses lower and upper quantiles at $\alpha/2$ and $1-\alpha/2$, producing symmetric distances around the mean.

The familiar central ninety-five-percent interval is approximately mean plus or minus $1.96$ standard deviations. This describes the modeled distribution of an individual observation. It is not automatically a confidence interval for an unknown mean. A confidence interval requires a sampling model and an estimator's uncertainty. Substituting the observation standard deviation for an estimator standard error changes the question.

A one-sided ninety-five-percent threshold uses a different quantile, approximately $1.64485$ above the standard mean. Confusing central and one-sided coverage is a frequent error because both statements contain the number ninety-five. Write the actual event and the tail mass first. The wording of the coverage question determines which quantile is relevant.

## Deriving normal moments through the MGF

Completing the square in $tz-z^2/2$ gives $-(z-t)^2/2+t^2/2$. The shifted normal density integrates to one, so the standard normal MGF is $e^{t^2/2}$ for every real transform argument. The general normal MGF becomes $e^{\mu t+\sigma^2t^2/2}$. Differentiation at zero gives the mean and second raw moment, and their difference gives variance $\sigma^2$.

The cumulant generator is a quadratic polynomial. Thus the first two cumulants are mean and variance, and all higher cumulants vanish. This is a property of the normal law, not a statement that all its higher moments vanish. Its fourth central moment is $3\sigma^4$, and its sixth central moment is $15\sigma^6$. Higher raw and central moments can be nonzero even when the corresponding cumulants are zero.

Symmetry gives zero odd central moments. The raw third moment can still be nonzero when the mean is nonzero. Keeping raw and centered quantities distinct avoids a misleading claim that a shifted normal variable has zero third moment. Standardized skewness is zero, raw kurtosis is three, and excess kurtosis is zero when variance is positive.

## Affine transformations of one normal variable

For real constants $a$ and $b$, $a+bX$ is normal when $X$ is nondegenerate normal and $b\ne0$. Its mean is $a+b\mu$ and variance $b^2\sigma^2$. A negative multiplier reflects the distribution while retaining a positive standard deviation $|b|\sigma$. A zero multiplier yields a constant variable, which is a point mass rather than a continuous normal density with a valid positive scale.

This closure is useful in calibrated measurements and unit conversions. A correction that subtracts a constant shifts the mean but does not reduce random variation. A multiplication changes both signal scale and standard deviation. Saying that a calibration removes uncertainty merely because it centers readings near a target confuses systematic location correction with dispersion.

Nonlinear transformations need a separate calculation. Squaring a standard normal variable produces a nonnegative law, and exponentiating a normal variable produces a positive right-skewed law. Neither transformation remains normal. A smooth transformation can be approximately linear over a small range, but its approximate normality requires a stated range and an error assessment. The exact affine result should not be extended to every transformation.

## Linear combinations of independent normal variables

Independent normal variables have a normal linear combination. Multiplying their MGFs after scaling yields a new exponential quadratic, with mean equal to the linear combination of means and variance equal to the sum of coefficient-squared variances. Independence justifies the product. For a difference, the negative coefficient reduces the mean appropriately but its squared contribution still adds variance.

Subtracting noisy independent measurements does not subtract their uncertainties. If two independent readings both have variance four, their difference has variance eight, not zero. If they share a common error component, covariance changes the answer. The general variance identity includes pairwise covariance terms, so a difference can have less variance when shared errors cancel. That is a feature of the joint model, not of subtraction alone.

For jointly normal variables, a linear combination is normal even when the variables are dependent, with variance obtained from the full covariance structure. Merely having normal marginal distributions does not establish joint normality. Dependence can create a joint distribution whose marginals are normal but whose linear combinations are not. The joint assumption must be stated if the calculation relies on that stronger closure.

## Zero correlation and normal independence

For a jointly normal pair, zero covariance implies independence. This special implication does not hold for arbitrary random variables, and it does not hold simply because each marginal is normal. The jointly normal density or characteristic function factors when covariance is zero, establishing independence in that particular family. Outside it, covariance summarizes only one aspect of dependence.

One construction shows the missing condition. Let $Z$ be standard normal and let an independent random sign take plus or minus one with equal probability. Set $X=Z$ and $Y$ equal to the sign times $Z$. Both marginals are standard normal and their covariance is zero, but their absolute values are identical. They are dependent. The pair is concentrated on two lines rather than having the usual nonsingular bivariate normal density.

This distinction affects practice because a scatter plot and a correlation coefficient cannot fully establish a joint model. Zero sample correlation is also different from zero population covariance. A theoretical implication inside a model should not be treated as an automatic empirical conclusion from one dataset. The model statement and the evidence for it play different roles.

## The normal approximation and impossible tails

A normal model can assign some probability to negative values even when a measured quantity is physically nonnegative. If that probability is negligible for a stated purpose, the model may be a useful approximation. If it is substantial, the support mismatch becomes material. For a duration with mean two and standard deviation three, a normal law would put a large probability below zero, suggesting that another model or a transformed scale deserves consideration.

Truncating a normal variable to a permitted interval creates a different normalized distribution. Clipping every negative simulated value to zero instead creates a point mass at zero plus a continuous part above zero. Those two operations are not interchangeable. A program should identify whether it rejects, truncates, clips or leaves impossible draws, because each choice changes the probability law.

The same issue arises when approximating bounded proportions. A normal approximation centered well inside zero to one with small standard deviation may have negligible outside mass. Near a boundary or with high variability it can become misleading. A beta model has bounded support by construction, but that does not automatically make it appropriate for every proportion. Mechanism and observational discreteness still matter.

## The beta integral and normalization

For positive shapes $\alpha$ and $\beta$, define $B(\alpha,\beta)=\int_0^1x^{\alpha-1}(1-x)^{\beta-1}\,dx$. The integral is finite because each boundary power is integrable when its corresponding shape is positive. Dividing the integrand by this integral gives the beta density. Negative or zero shapes do not define an ordinary proper beta density under this formulation.

The identity $B(\alpha,\beta)=\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$ connects beta normalization with the gamma function. It can be derived by expressing a product of two gamma integrals in terms of their total and fractional allocation. The change of variables has a Jacobian equal to the total. One integral becomes a gamma normalization and the other becomes the beta integral.

For positive integer shapes the gamma recurrence reduces the normalizing constant to factorials. This often makes exact polynomial calculations possible. Integer shapes are a convenient computational case, not a restriction of the family. A valid beta law can have noninteger positive shapes and an unbounded density near one or both endpoints.

## Beta shape and boundary behavior

The beta density on the open unit interval is proportional to $x^{\alpha-1}(1-x)^{\beta-1}$. When both shapes exceed one, density goes to zero at both boundaries and has an interior mode $(\alpha-1)/(\alpha+\beta-2)$. When both shapes equal one, the density is constant and the law is the standard continuous uniform distribution.

When one shape is below one, the density diverges near the corresponding boundary. When both shapes are below one, density is large near both ends and smallest somewhere in the interior. These boundary divergences remain integrable. They do not create positive point masses at exactly zero or exactly one. An observed dataset with genuine mass at a boundary may require a mixture with boundary atoms rather than an ordinary beta density.

For equal shapes the law is symmetric around one half. Shape equality alone does not imply a central peak: equal shapes below one give two boundary concentrations. Equal shapes above one give an interior peak. The distinction is important when interpreting a slider labeled concentration, since decreasing equal shapes can change the qualitative shape rather than merely widen a bell.

## Beta moments from ratios of integrals

For nonnegative integer $r$, integrating $x^r$ against the beta density gives $E[X^r]=B(\alpha+r,\beta)/B(\alpha,\beta)$. Applying the gamma recurrence produces a product of rising factors. The mean is $\alpha/(\alpha+\beta)$ and the second raw moment is $\alpha(\alpha+1)/((\alpha+\beta)(\alpha+\beta+1))$. Subtracting the squared mean gives variance $\alpha\beta/((\alpha+\beta)^2(\alpha+\beta+1))$.

The moment formula exposes the roles of total shape and relative shape. If both shapes are multiplied by a common positive factor, the mean stays fixed while the total shape changes. Larger total shape reduces variance around the fixed mean. This is a concentration parameterization, and it is often more interpretable than changing two unlabeled shapes independently.

Negative moments require extra conditions. For example, $E[1/X]$ exists only when the first shape exceeds one, because the additional inverse power alters the behavior near zero. A bounded variable has all nonnegative moments, but it need not have finite inverse moments. Bounded support controls large values; it does not remove singular behavior near zero for reciprocal transformations.

## Mean and concentration parameterization

Set a desired mean $m$ strictly between zero and one and a positive concentration $\kappa$. Choosing $\alpha=m\kappa$ and $\beta=(1-m)\kappa$ gives that mean and variance $m(1-m)/(\kappa+1)$. The concentration controls how tightly the density gathers around its mean, though low concentration can place substantial density near boundaries. Increasing concentration at a fixed mean reduces variance monotonically.

A proposed mean and variance cannot always be represented by an ordinary beta law. The required variance must be positive and smaller than $m(1-m)$. Solving for concentration gives $\kappa=m(1-m)/v-1$, which must be positive. The upper bound is also a general variance bound for a variable on zero to one with that mean; ordinary positive beta shapes cannot attain the boundary two-point case exactly.

These formulas help audit parameter choices without fitting data. They do not say that matching two moments proves a beta distribution. Many different bounded laws share the same mean and variance. Moment matching specifies one member of a selected family, while family selection remains a separate modeling choice. A simulation should label that distinction clearly.

## Beta CDFs and exact polynomial cases

The beta CDF is the normalized integral from zero to the threshold and generally requires numerical evaluation. For small positive integer shapes, expansion of the polynomial density gives an elementary CDF. With shapes two and three, the density is $12x(1-x)^2$ and the CDF is $6x^2-8x^3+3x^4$ within the support. It is zero below zero and one above one.

Differentiating the CDF should recover the density, and evaluating it at the support bounds should give zero and one. Both checks are easy in a polynomial case and are useful for validating software fixtures. An interval probability is the difference of CDF values. A beta quantile generally still requires solving an equation, even when the CDF itself is polynomial.

The identity that reflecting a beta variable swaps its two shapes provides another check. If $X$ has shapes $\alpha$ and $\beta$, then $1-X$ has shapes $\beta$ and $\alpha$. Consequently, a lower-tail probability for one shape order corresponds to a reflected upper tail for the other. A discrepancy often indicates reversed shape arguments or an incorrect endpoint convention.

## Rescaling a beta variable to another bounded interval

For finite bounds $a<b$, define $Y=a+(b-a)X$ from a standard beta variable. The transformed density is the standard beta density at $(y-a)/(b-a)$ divided by the interval length. Its mean is $a+(b-a)\alpha/(\alpha+\beta)$, and its variance is $(b-a)^2$ times the standard beta variance. Shape controls fractional position, while the bounds control location and scale.

This construction can describe a modeled quantity with fixed lower and upper limits. The limits must be actual assumptions about the variable, not just the smallest and largest observed sample values presented as certain population bounds. Estimating bounds from data introduces uncertainty that the fixed-bound formula does not address. A fitted density on the sample range can otherwise assign zero probability to future observations merely because they were not previously seen.

If a bounded variable is rounded or censored, the recorded-data law again differs from the underlying continuous density. A displayed maximum can include all values rounding to the upper display limit. Positive mass at the displayed endpoint may be generated by recording, while true endpoint mass in the underlying variable requires a different model. State which level the beta law describes.

## Beta laws from order statistics

Take independent continuous uniform draws on zero to one and sort them. The $k$th smallest of $n$ draws has a beta law with shapes $k$ and $n+1-k$. One derivation considers a small interval around a threshold: choose which draw falls there, require exactly $k-1$ others below it, and the rest above it. Dividing the resulting small-interval probability by interval width gives the beta density with its combinatorial constant.

The construction gives an intuitive meaning to the mean $k/(n+1)$. The smallest draw has a distribution concentrated near zero, the largest near one, and middle order statistics concentrate near central ranks. They are not themselves uniform except in the single-draw case. Sorting changes the marginal law of a selected rank even though every unsorted observation is uniform.

Different order statistics from the same sample are dependent. Their marginal beta laws do not justify independent draws from those marginals when reconstructing a sorted sample. A simulation of the joint order statistics should sort one common independent uniform sample, preserving their dependence and ordering. Modeling each rank separately can produce an impossible sequence with crossed ranks.

## Beta uncertainty about a fixed probability

A beta law can represent uncertainty about an unknown Bernoulli success probability in a Bayesian model. The probability parameter is treated as a random quantity within that uncertainty representation, while observations are conditionally Bernoulli or binomial given it. A prior beta density multiplied by the likelihood for successes and failures yields a posterior beta density with corresponding counts added to its shapes.

For $s$ successes and $f$ failures, the posterior shapes become $\alpha+s$ and $\beta+f$. This algebra follows from adding exponents of the parameter and its complement. It depends on the stipulated conditional sampling model. Dependent observations, changing probabilities or selection effects can invalidate the simple binomial likelihood. Conjugate formulas do not remove the need to assess how the observations were collected.

The posterior mean is a weighted average of the prior mean and observed proportion when at least one observation is present. The prior total shape controls its weight. A posterior interval is a statement about parameter uncertainty under the chosen model; it is not a guaranteed interval containing each future observation. Future observations are binary, while the probability parameter lies on a continuum. The two distributions describe different objects.

## Random probabilities induce dependence in observations

If a common latent probability is beta distributed and several Bernoulli observations are conditionally independent given it, their unconditional outcomes are generally dependent. The joint law averages over a shared uncertain parameter. Seeing one success makes a larger probability more plausible, which changes prediction of another observation. This is the same conditional-versus-marginal distinction encountered with shared sources earlier in the book.

The marginal mean of each Bernoulli observation is the beta mean. The covariance of two distinct observations is the variance of the shared probability, provided the conditional independence assumption holds. A count of several such observations has a beta-binomial mixture law, with more variation than a binomial law having only the same marginal success probability. The extra variation follows from common heterogeneity.

If a new independent probability is drawn separately for every observation, that shared dependence disappears. The two experiments may have identical one-observation success rates while different multi-observation count laws. A beta parameter must therefore be tied to an information and repetition structure, not merely inserted as a decorative distribution for an uncertain number.

## Comparing equal-mean normal and beta models

A beta law and a normal law can have the same mean and variance while retaining different supports and shapes. A normal approximation to a concentrated beta law can work for central probabilities when the mean is away from boundaries, but it is not an exact identity. Tail probabilities near zero or one can differ substantially even when the two first moments agree.

The approximation should be assessed at the events that matter. A visually similar central density does not establish a good extreme quantile. Comparing CDF values at relevant thresholds is more informative than comparing peak heights. When the beta density diverges near a boundary, a normal approximation is especially poorly suited to describing that local behavior. When the modeled quantity has real endpoint masses, neither ordinary continuous law accounts for those masses.

Moment matching is useful because it isolates one reason for differences: with location and variance aligned, discrepancies show shape and support effects. It is not evidence that either family is true. A classroom explorer should let a reader compare probabilities and outside-support normal mass, while labeling both curves as assumed models rather than empirical discoveries.

## Fully worked question 1: A normal measurement interval

**Question.** A stipulated measurement $X$ has law $N(100,100)$ in arbitrary measurement units. Find $P(90<X<115)$, $P(X>120)$, and the ninetieth percentile. Find the central ninety-five-percent interval for individual measurements. Explain why that interval is not automatically a confidence interval for an unknown mean.

**Solution, step 1: Identify the variance convention and standardize.** The variance is one hundred and the standard deviation is ten. The interval endpoints become minus one and one and a half. Its probability is $\Phi(1.5)-\Phi(-1)$, approximately $0.774538$. The upper threshold one hundred and twenty becomes two, giving right-tail probability approximately $0.0227501$. These probabilities concern modeled individual observations.

**Solution, step 2: Transform the requested quantile.** The standard ninetieth percentile is approximately $1.2815516$. The original-scale percentile is $100+10(1.2815516)$, approximately $112.8155$. The probability at or below that threshold is ninety percent under the given continuous model. It is not an average or a prediction guaranteed for one future reading.

**Solution, step 3: State the interval's actual target.** The central ninety-five-percent individual interval is approximately $[80.4004,119.5996]$, using standard quantiles plus and minus $1.959964$. A confidence interval for an unknown mean would instead depend on an estimator, a sample size, an uncertainty calculation and assumptions about sampling. The given distributional interval covers individual values under known model parameters; its interpretation must not be relabeled as inferential certainty about an unknown parameter.

## Fully worked question 2: A polynomial beta density

**Question.** Let $X$ have a beta law with shapes two and three. Derive its density and CDF, calculate its mean and variance, and find $P(X>1/2)$ and $P(1/4<X<3/4)$. State the interior mode and explain why the density value at the mode is not a point probability.

**Solution, step 1: Normalize and integrate.** The beta constant is $\Gamma(2)\Gamma(3)/\Gamma(5)=1/12$, so the density is $12x(1-x)^2$ between zero and one. Expanding and integrating gives $F(x)=6x^2-8x^3+3x^4$ within that interval, with the usual zero and one values outside it. The endpoints and derivative verify normalization and recover the density.

**Solution, step 2: Calculate moments and interval masses.** The mean is two fifths and variance is $6/(25\cdot6)=1/25$. At one half, the CDF is eleven sixteenths, so the upper probability is five sixteenths. At one quarter and three quarters, CDF values are sixty-seven over two hundred and fifty-six and two hundred and forty-three over two hundred and fifty-six. Their difference is eleven sixteenths, or $0.6875$.

**Solution, step 3: Interpret the peak.** The mode is $(2-1)/(2+3-2)=1/3$. Its density is sixteen ninths, larger than one but valid because density is per unit of the variable. The probability of exactly one third is zero under this continuous law. A small interval around that value has probability approximated by density times width, and an exact interval probability comes from the CDF. Peak height and point probability are different quantities.

## Fully worked question 3: An independent normal linear combination

**Question.** Independent variables have laws $X\sim N(10,4)$ and $Y\sim N(3,1)$. Define $Z=2X-3Y+5$. Find its distribution and $P(Z>21)$. Then suppose the pair is jointly normal with covariance one instead of independent. Recalculate the variance and state which earlier result changes.

**Solution, step 1: Combine means and independent variances.** The mean is $2(10)-3(3)+5=16$. Independence gives variance $2^2(4)+(-3)^2(1)=25$. The linear combination is therefore $N(16,25)$, with standard deviation five. The constant changes location but contributes no variance, and the negative coefficient still contributes a positive squared variance term.

**Solution, step 2: Evaluate the upper event.** The threshold twenty-one is one standard deviation above the mean. Its upper-tail probability is $1-\Phi(1)$, approximately $0.158655$. This uses both the independent-normal closure and the correct variance. Subtracting the two variance contributions would not represent the given experiment.

**Solution, step 3: Include the covariance under the new joint model.** The covariance term is $2(2)(-3)(1)=-12$, so the new variance is thirteen and the mean remains sixteen. Joint normality keeps the linear combination normal, now $N(16,13)$. The standardized threshold is $5/\sqrt{13}$, giving upper probability approximately $0.0827589$, so the earlier upper probability changes. A positive covariance reduces variation in this difference-like combination, even though it would increase variation in a same-sign combination.

## Numerical evaluation and boundary safeguards

Numerical probability routines should handle parameter constraints before evaluating densities. A normal scale must be positive for a continuous density. Beta shapes must both be positive. A beta threshold outside zero to one has a CDF determined by support, not by blindly raising a negative quantity to a noninteger power. NaN output is not a meaningful probability result and should not appear silently in a teaching interface.

Normal CDF evaluation often uses the error function, while beta CDF evaluation often uses incomplete beta algorithms. In extreme tails, log probabilities or survival routines can prevent a meaningful small probability from vanishing through rounding. For moderate classroom examples, direct polynomial beta CDFs and tested normal approximations can be adequate if their error is stated and checked against reliable independent fixtures.

A beta density at an endpoint is not needed to compute interval probability. When a shape is below one, attempting to plot the endpoint can create an infinite value and break the vertical scale. A graph can omit exact endpoint heights while explaining the limiting behavior, or restrict an interactive demonstration to shapes with finite boundary values. Either choice must be disclosed so the visible curve does not suggest a false finite endpoint value.

## An explorer that teaches probability rather than appearance

The normal explorer in this book displays the mean, standard deviation and probability between two original-scale bounds, together with the standardized endpoints. Its shaded density area represents the calculated interval probability. Changing the mean translates the curve; changing standard deviation changes both peak and spread. A text result remains available so the lesson does not depend on seeing color or reading a graph.

The beta explorer uses small positive integer shape options for which a polynomial CDF can be checked exactly. It displays mean, variance and an interval probability on zero to one. It does not pretend to implement all possible positive real shapes. Restricting the numerical scope makes the computation transparent, while the text covers the larger mathematical family and its boundary behavior.

The reader should try holding a mean fixed while increasing concentration, then compare an interval around the mean with one near a boundary. The direction of probability change depends on the interval. More concentration does not make every probability larger. A graph and the exact interval result together expose that distinction more clearly than a moving curve alone.

## Model checks from supports, moments and transformations

A proposed normal calculation should be checked against symmetry, scale and limiting behavior. A symmetric interval around the mean has equal lower and upper excluded masses. Increasing an upper threshold cannot increase its right-tail probability. A standardization should be dimensionless. A negative affine transformation reverses the direction of a one-sided event before its probability is computed.

A proposed beta calculation should be checked against positive shapes, bounded support and normalization. Swapping shapes should reflect the law. Mean should lie strictly between zero and one. Variance should be positive and below the fixed-mean bound. When both shapes equal one, calculations should reduce to standard uniform interval lengths. These structural checks can reveal an error even when one decimal output looks plausible.

For both families, a numerical check and a model check answer different questions. A library routine can verify a formula evaluation while leaving an inappropriate model unchallenged. A support audit can identify a modeling mismatch without calculating any integral. A complete answer states the assumed law, the event, the evaluated probability and the limits of that interpretation.

## Preparation for sampling and inference

The normal family will reappear in sampling distributions, large-sample approximations, measurement models and regression. The beta family will reappear in bounded-variable models, order statistics and Bayesian parameter uncertainty. These later uses require additional assumptions beyond the probability calculations developed here. Knowing a family's moments is a foundation for inference, not a substitute for sampling design or model assessment.

For example, normality of a population can give an exact normal sample mean under independent sampling, whereas a central limit theorem can give an approximate normal sample mean from a nonnormal population under stated conditions. Those are different arguments with different precision and finite-sample behavior. Similarly, a beta posterior follows from a chosen prior and likelihood rather than from the fact that the unknown quantity is merely bounded.

The next unit combines the families in a decision process. Its aim is to move from a verbal experiment to a coherent model, assess approximations at the relevant events, and report numerical uncertainty honestly. The normal and beta calculations become tools in that process, with their support and parameter conventions kept visible throughout.
