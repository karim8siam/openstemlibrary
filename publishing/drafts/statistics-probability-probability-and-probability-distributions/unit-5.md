# Unit 5: Moments, Generating Functions and Cumulants

## Learning aims and the purpose of distribution summaries

Moments summarize a distribution through averages of powers. Generating functions package probabilities or moments into a function, and cumulants reorganize moment information so that independent sums have especially simple relationships. These tools do not replace a probability model. They are derived from it and have existence conditions that determine when their formulas are meaningful.

This unit develops raw and central moments, probability generating functions for nonnegative integer variables, moment generating functions and their domains, characteristic functions, and the first four cumulants. The reader should be able to recover moments from a valid transform, combine independent variables through transform products, translate between moments and cumulants, and explain why a variable can have finite moments without a moment generating function on an interval around zero.

The emphasis is on reasoning rather than memorizing a transform table. A table can suggest a candidate law, but the variable's support, parameter conventions and transform domain still need to be checked. Differentiating a formula outside its domain does not create a moment, and multiplying transforms without independence does not create the correct law of a sum. The same model discipline used for event probabilities remains necessary in this more compact language.

## Raw moments and their existence

The raw moment of order $r$ is $m_r=E[X^r]$ when the expectation is defined; $m_0=1$. The first raw moment is the mean, and the second raw moment contributes to variance. For a finite discrete distribution every integer-order moment is finite because only finitely many finite values are averaged. For an unbounded distribution, moment existence depends on the tail behavior and must be checked through a sum or integral.

Absolute moments are useful for stating existence unambiguously. If $E[|X|^r]$ is finite, the raw moment of order $r$ is finite. A symmetric distribution with heavy tails may suggest cancellation of odd powers, but symmetry does not make an otherwise undefined signed expectation legitimate. If positive and negative contributions are both infinite, declaring their difference zero is not a valid moment calculation. A symmetric principal-value integral is a different mathematical operation.

A finite higher absolute moment implies finite lower absolute moments. One way to see this is to split the range into values with absolute magnitude at most one and values above one. On the first part, any nonnegative power is bounded by one. On the second part, a smaller power is bounded by a larger power. Thus finiteness of the larger-power integral controls the smaller one. This hierarchy helps justify the lower moments used in a higher-order calculation.

The converse is false. A distribution can have a finite mean but infinite second moment, or finite variance but infinite fourth moment. Reporting skewness and kurtosis requires the corresponding moments and a positive finite variance. The existence of a mean and standard deviation alone does not guarantee that those higher summaries are defined. A probability model should not be assigned every familiar summary merely because a software interface displays fields for them.

Raw moments depend on the origin of the measurement. Adding a constant changes them through binomial expansion. Central moments remove that origin dependence by centering around the mean. Scaling still changes their magnitudes. The difference is useful when interpreting location shifts versus shape changes, but neither set of moments uniquely answers every distributional question from a finite number of summaries.

## Central moments and relations to raw moments

Assuming the required moments exist, the central moment of order $r$ is $\mu_r=E[(X-m_1)^r]$. The first central moment is zero, and the second is variance. Expanding the centered power gives a systematic relationship with raw moments:

$$
\mu_r=\sum_{j=0}^{r}\binom rj(-m_1)^{r-j}m_j.
$$

This formula is a direct application of the binomial theorem followed by linearity of expectation. Its terms are not independent contributions of different events; they are algebraic parts of one centered power. The alternating signs can lead to cancellation in numerical calculations, which is one reason to compute centered moments directly when the distribution is available in a stable form.

The first relevant identities are

$$
\mu_2=m_2-m_1^2,
$$
$$
\mu_3=m_3-3m_1m_2+2m_1^3,
$$
$$
\mu_4=m_4-4m_1m_3+6m_1^2m_2-3m_1^4.
$$

A centered third moment weights the signed cube of deviation. Positive and negative deviations contribute with opposite signs, with larger magnitudes receiving stronger weights. A centered fourth moment weights both signs positively and gives substantial influence to large deviations. Its interpretation concerns the full distribution of those deviations, not just the appearance of one part of a density curve.

For positive finite variance $\sigma^2$, moment skewness is $\mu_3/\sigma^3$. Moment kurtosis is $\mu_4/\sigma^4$, and excess kurtosis subtracts three from that value. These are population-law definitions. Sample estimators and bias corrections may use different formulas and will be considered in statistical-method books. A reported number should identify whether it is a distribution property or a particular sample estimator.

Zero third central moment does not prove symmetry. Oppositely signed cubic contributions can cancel in an asymmetric distribution. Symmetry about the mean, when the relevant odd moments exist, implies their vanishing, but the implication cannot generally be reversed from one moment alone. Similarly, kurtosis does not uniquely characterize tail shape or outlier probability. Several distributions can share the first four moments and differ in events important to an application.

The scaling rules are straightforward. For $Y=a+bX$, its mean is $a+bE[X]$, and a central moment of order $r$ is multiplied by $b^r$. Thus positive rescaling leaves standardized skewness and kurtosis unchanged, while negative rescaling reverses the sign of skewness and leaves kurtosis unchanged. If the variance is zero, the usual standardized ratios are undefined. A degenerate variable has no spread to use as a normalization scale.

## Probability generating functions for count variables

For a nonnegative integer-valued variable $N$, the probability generating function is

$$
G_N(z)=E[z^N]=\sum_{n=0}^{\infty}P(N=n)z^n.
$$

The powers record the count values, and the coefficients are their probability masses. At zero, the usual convention $0^0=1$ in this generating-function expression gives the probability of count zero. At one, the function is one. For real $z$ between zero and one, the nonnegative terms are bounded in total by one, so the PGF is finite without a moment-existence assumption.

A PGF is not defined in this conventional form for an arbitrary real-valued variable. Negative integer values lead to negative powers and require a different representation; fractional values change the power-series interpretation. One can sometimes shift a variable to obtain a nonnegative integer count, but the transformation must be stated. Treating any expression $E[z^X]$ as a standard count PGF hides its support and coefficient meaning.

For a finite-support count, the PGF is a polynomial, and its coefficients can be recovered by differentiation at zero. The same coefficient rule applies to a convergent infinite power series in its interior. The probability of count $n$ is the derivative of order $n$ at zero divided by $n!$. This is a useful way to extract selected probabilities, though direct coefficient expansion can be simpler for small polynomials.

Differentiating at one generates factorial moments rather than raw powers. The first derivative gives the mean when it is finite. The second derivative gives $E[N(N-1)]$, not $E[N^2]$. Therefore variance can be calculated as $G_N''(1)+G_N'(1)-(G_N'(1))^2$ when the second moment is finite. Confusing the second factorial moment with the second raw moment omits the mean term and produces an incorrect variance.

For infinite-support laws, derivatives at one are understood with the appropriate limiting and existence conditions. Nonnegative series terms provide a direct route to factorial moments through limits from below. An infinite derivative can correspond to an infinite moment. A polynomial formula copied from a bounded count cannot justify a finite derivative for an unbounded count with a heavy tail.

## Products of PGFs and independent count sums

If nonnegative integer variables are independent, the PGF of their sum is the product of their PGFs. The reason is $z^{N+M}=z^Nz^M$, followed by factorization of the expectation. Coefficients of the product reproduce the convolution of the two PMFs. This connects the transform method to the event-based sum distribution derived in Unit 4.

The product identity depends on independence. For dependent variables, the expected product of their powers is not generally the product of their expected powers. A joint generating function can represent their joint law, and substituting the same argument for both coordinates gives the generating function of their sum. The extra joint information cannot be manufactured by multiplying marginal functions.

A binary count with success probability $p$ has PGF $(1-p)+pz$. For independent binary counts sharing that same probability, the sum PGF is a power of this linear expression. Expanding the power produces combination coefficients counting which positions contribute successes. Later distribution units will develop the resulting binomial law in detail. Here the derivation shows how generating-function multiplication packages the same counting mechanism.

If the independent binary counts have different success probabilities, their PGF is a product of different linear factors. It is generally not a power of one common factor, and the sum is not the common-probability binomial law. Equal or similar means do not repair that difference. A model can share a summary with a familiar distribution while retaining a different probability pattern.

PGFs also describe independent thinning of counts. Suppose each of a random number of items is retained independently with probability $q$, independently of the original count once that count is specified. Conditional on the original count, the retained-count PGF is $(1-q+qz)^N$. Averaging gives $G_N(1-q+qz)$. This substitution represents a stated retention mechanism; it is not valid for arbitrary outcome-dependent selection.

The count's PGF is a compact representation of a whole distribution, not merely of its moments. Values inside its convergent power-series domain determine its coefficients. Numerical evaluation at only a few arguments gives less information than the entire function. Recovering probabilities from noisy evaluations is a separate computational problem and can be unstable, so a formal coefficient identity should not be confused with a universally reliable numerical inversion routine.

## Moment generating functions and their domains

The moment generating function is $M_X(t)=E[e^{tX}]$ at real arguments where that expectation is finite. At zero it equals one for every random variable. The usual useful MGF condition is finiteness on an open interval containing zero. This condition supplies exponential tail control sufficient for moments of every order and permits differentiation around zero with appropriate justification.

The domain matters. A transform finite only at zero does not serve as a local moment generator. A transform finite on one side of zero may be useful as a one-sided Laplace transform for a nonnegative variable, but it does not satisfy the two-sided neighborhood condition used in standard MGF uniqueness and analytic-expansion arguments. When presenting a formula, state the range of arguments on which it is finite.

For a finite-support law, the MGF is a finite weighted sum of exponentials and is finite for every real argument. For an unbounded law, positive and negative arguments weight different tails. A positive argument magnifies large positive values exponentially, while a negative argument magnifies large negative values. Integrability can therefore differ between the two sides. A variable with moderate polynomial moments can still fail an exponential-moment condition.

Under the neighborhood condition, differentiating the MGF produces $M_X^{(r)}(0)=E[X^r]$. The derivative of the exponential integrand contains the power of the variable, and exponential integrability in a slightly larger interval controls the interchange of differentiation and expectation. This justification is invisible in a purely formal manipulation, but it is what makes the resulting derivative a genuine moment rather than a symbol with an unsupported interpretation.

The MGF has a power-series expansion around zero with moment coefficients when the needed neighborhood exists. The coefficient of $t^r$ is the raw moment divided by $r!$. Having finite moments alone is not enough to guarantee that this series converges to a finite MGF near zero. The third worked question demonstrates a law with finite moments of every positive integer order but no positive-argument MGF.

An MGF finite on a neighborhood of zero determines the distribution uniquely. This is a transform uniqueness theorem, not a claim that a finite list of moments determines every law. Matching two MGFs over the required neighborhood can identify a distribution, while matching only a few derivatives usually cannot. Even matching all moments needs additional conditions before a general uniqueness conclusion is justified.

## MGF operations and independent sums

For a linear transformation $Y=a+bX$, the MGF is $e^{at}M_X(bt)$ wherever the latter expression is finite. This follows by separating the deterministic exponential factor. The transformation also changes the domain: an argument for $Y$ is allowed only when the scaled argument is allowed for $X$. Negative scaling exchanges which tail is amplified by positive and negative arguments.

For independent variables, the MGF of a sum is the product of their MGFs on a common domain of finiteness. The exponential of a sum is a product, and independence factorizes its expectation. The same argument works for characteristic functions without exponential-moment restrictions, as developed below. For dependent variables, one needs a joint transform or a direct calculation from the joint law.

The product method can establish closure properties of distribution families. Derive the individual transform, multiply the transforms for independent components, and identify the resulting expression under a valid uniqueness condition. The independence and domain statements are part of the proof. A familiar-looking product formula with no common neighborhood of finiteness cannot automatically support an MGF uniqueness argument.

An MGF can also bound a tail through Markov's inequality. For a positive argument $t$ in its domain, the event $X\geq a$ implies $e^{tX}\geq e^{ta}$, giving $P(X\geq a)\leq e^{-ta}M_X(t)$. Choosing an argument to minimize this bound is a useful application, but the result remains a bound, not an exact tail probability. If the MGF is infinite for every positive argument, this particular bound supplies no finite improvement.

## Cumulant generating functions

When an MGF is finite on a neighborhood of zero, its cumulant generating function is $K_X(t)=\log M_X(t)$. The MGF is positive for real arguments in its finite domain, so the logarithm is well defined. At zero the cumulant generator is zero. The cumulant of order $r$ is the derivative of order $r$ of this function at zero.

The logarithm changes the independent-sum rule from multiplication to addition. If independent variables have valid MGFs on a common neighborhood, then $K_{X+Y}(t)=K_X(t)+K_Y(t)$. Their cumulants therefore add order by order. This is the principal practical advantage over raw moments, whose expressions for sums contain many cross terms.

For a constant shift and rescaling, $K_{a+bX}(t)=at+K_X(bt)$. The first cumulant becomes $a+b\kappa_1(X)$. Every higher cumulant is multiplied by $b^r$. Thus adding a constant affects only the first cumulant. This mirrors the location invariance of central moments while preserving the especially simple addition law for independent sums.

The first cumulant is the mean and the second is variance. Differentiating the logarithm once gives $K'=M'/M$. Differentiating again gives $K''=M''/M-(M'/M)^2$. At zero the MGF equals one, so these derivatives reproduce the familiar mean and variance formulas. Higher differentiation yields cumulants that are combinations of raw moments rather than the raw moments themselves.

The third cumulant equals the third central moment. The fourth cumulant equals the fourth central moment minus three times the squared variance. Consequently standardized fourth cumulant is excess kurtosis rather than ordinary kurtosis. Confusing these quantities can shift a reported value by three and change the interpretation of a transform comparison.

## Moment–cumulant relations and a recurrence

Write the first four raw moments as $m_1,m_2,m_3,m_4$. The corresponding cumulants are

$$
\kappa_1=m_1,\qquad \kappa_2=m_2-m_1^2,
$$
$$
\kappa_3=m_3-3m_1m_2+2m_1^3,
$$
$$
\kappa_4=m_4-4m_1m_3-3m_2^2+12m_1^2m_2-6m_1^4.
$$

Subtracting three times the squared second central moment from the fourth central-moment expansion verifies the final formula. This supplies a second route to the same expression and helps prevent coefficient errors. The first four cumulants can be defined through these algebraic relations whenever the needed moments are finite, even when a real MGF neighborhood is unavailable. In that case one should not claim that an analytic real cumulant generator exists.

A general recurrence follows from $M'=K'M$. Comparing coefficients of the power series yields

$$
m_n=\sum_{j=1}^{n}\binom{n-1}{j-1}\kappa_j m_{n-j},\qquad m_0=1.
$$

Solving for the last term expresses the next cumulant in terms of lower cumulants and moments. The recurrence is a systematic alternative to repeated differentiation of a logarithm. For finite moment sequences, it can also be used as a formal algebraic coefficient relation without asserting convergence of an infinite series. The distinction between a formal polynomial computation and an analytic transform identity should remain explicit.

For an independent sum, cumulant addition can simplify comparisons of shape as the number of terms grows. If identically distributed independent terms have finite relevant cumulants, the cumulant of their sum is the number of terms times the individual cumulant. Rescaling to an average then introduces the appropriate power of that number. Later convergence material will use these relationships cautiously; vanishing standardized higher cumulants alone is not a complete proof of a general limit theorem.

## Characteristic functions and existence without exponential moments

The characteristic function is $\phi_X(t)=E[e^{itX}]$ for real $t$, where $i$ is the imaginary unit. Euler's identity expresses the integrand as a cosine plus an imaginary sine. Its absolute magnitude is one, so the expectation exists for every real argument and every real-valued random variable. This is the key existence advantage over the MGF.

At zero the characteristic function equals one, and its magnitude is at most one. Its value at a negative argument is the complex conjugate of its value at the positive argument. It is continuous, in fact uniformly continuous, on the real line. These properties follow from the bounded exponential integrand and the expectation operation. A candidate complex function that violates them cannot be the characteristic function of a probability law.

The characteristic function of a linear transformation is $e^{iat}\phi_X(bt)$. For independent variables, the characteristic function of their sum is the product of the individual characteristic functions. No common MGF domain is needed, because the complex integrands remain bounded. This makes characteristic functions useful for heavy-tailed laws and general distributional convergence arguments.

If the absolute moment of order $r$ is finite, differentiation at zero gives $\phi_X^{(r)}(0)=i^rE[X^r]$. The moment condition supports differentiation of the bounded oscillatory integrand through its power-weighted derivative. The existence of the characteristic function itself does not imply the existence of every derivative or every moment. A transform may be defined everywhere yet have limited smoothness at zero.

Characteristic functions determine probability distributions uniquely. This general uniqueness statement does not require a real exponential-moment neighborhood. Its full inversion proof belongs to a more advanced probability course; here it is used as a stated theorem. The transform provides a distributional representation even when moments are missing, while its derivatives provide moment information only when the relevant existence conditions hold.

For an integer-valued law, the characteristic function is periodic with period two pi because each integer value leaves the complex exponential unchanged after that argument shift. For a general real-valued law, such periodicity need not hold. A symmetric law about zero has a real-valued characteristic function because the sine contributions cancel under symmetry. Again, these are implications from distribution structure, not permissions to infer every structural property from a few evaluated transform values.

Near zero, continuity ensures the characteristic function stays nonzero in a sufficiently small neighborhood. A locally consistent logarithm can then connect its derivatives to cumulant relations with powers of the imaginary unit. Care is needed with complex logarithm branches and with differentiability. The algebraic first-four-moment relations above avoid introducing unnecessary complex-analysis machinery for the introductory applications in this book.

## Fully worked question 1: Moments and cumulants of a two-point law

**Question.** A variable takes minus one with probability one quarter and three with probability three quarters. Find its first four raw moments, mean, variance, third and fourth central moments, and first four cumulants. Give its MGF and characterize its domain. Calculate moment skewness, kurtosis and excess kurtosis, assuming the population-law conventions developed in this unit.

**Solution, step 1: Average the powers.** Direct weighted sums give $m_1=2$, $m_2=7$, $m_3=20$, and $m_4=61$. The mean is two. The deviations from this mean are minus three and one, so centered sums can be computed independently of the raw-moment expansions. Their squared average is $(1/4)9+(3/4)1=3$, establishing variance three.

**Solution, step 2: Compute central moments directly.** The third central moment is $(1/4)(-27)+(3/4)(1)=-6$. The fourth central moment is $(1/4)(81)+(3/4)(1)=21$. Substituting the raw moments into the central-moment identities gives the same values. The negative third moment reflects the longer negative deviation combined with its probability weight, even though the higher numerical value is more probable.

**Solution, step 3: Obtain cumulants and the transform.** The first three cumulants are two, three and minus six. The fourth is $21-3(3^2)=-6$. The MGF is $(1/4)e^{-t}+(3/4)e^{3t}$, finite for every real argument because the support is finite. Differentiating its logarithm at zero gives the same cumulants. The fourth cumulant is not the fourth raw moment and is not the fourth central moment.

**Solution, step 4: Standardize the shape summaries.** Skewness is $-6/(3^{3/2})=-2/\sqrt3$. Kurtosis is $21/9=7/3$, and excess kurtosis is $7/3-3=-2/3$. These quantities are dimensionless. The excess value also equals the fourth cumulant divided by squared variance, $-6/9$. All summaries are defined because the variance is positive and every required moment is finite.

## Fully worked question 2: An independent count sum through its PGF

**Question.** Three independent binary trials each succeed with probability two fifths. Their success count is $A$. A fourth binary trial $B$, independent of all three, has the same success probability. Find the PGF of $T=A+B$, its complete PMF, the probability $T=2$, its mean, variance and third cumulant. Explain which part of the calculation would fail if the fourth trial had the same marginal probability but was dependent on the first three.

**Solution, step 1: Build and multiply the generating functions.** One binary trial has PGF $(3/5)+(2/5)z$. Independence of the first three gives $G_A(z)=((3/5)+(2/5)z)^3$. The independent fourth trial contributes another identical factor, so $G_T(z)=((3/5)+(2/5)z)^4$. This product represents the full independent four-trial mechanism, not merely agreement of four marginal success rates.

**Solution, step 2: Extract the masses.** Polynomial expansion gives masses $81/625$, $216/625$, $216/625$, $96/625$, and $16/625$ at counts zero through four. They sum to one. The mass at two is $216/625=0.3456$. The coefficients count the possible positions of successes, while each product weight accounts for their two-fifths success and three-fifths failure probabilities.

**Solution, step 3: Derive mean and variance.** The sum mean is four times two fifths, or $8/5$. Each independent indicator has variance $(2/5)(3/5)=6/25$, so the sum variance is $24/25$. Differentiating the PGF at one gives the same mean, and combining its first and second derivatives gives the same variance. The second PGF derivative alone is a factorial moment, not the variance.

**Solution, step 4: Calculate the third cumulant and state the dependence limitation.** A binary variable with success probability $p$ has third central moment, and hence third cumulant, $p(1-p)(1-2p)$. Substituting two fifths gives $6/125$ per trial; adding four independent cumulants gives $24/125$. If the fourth trial were dependent, its identical marginal PGF would remain valid, but multiplying it by the first count's PGF would not generally give the sum law. Covariance and higher joint relationships could change the distribution and its cumulants.

## Fully worked question 3: Finite moments without a local MGF

**Question.** Let $Z$ have density $(2\pi)^{-1/2}e^{-z^2/2}$ over the real line, and let $W=e^Z$. Show that every positive integer raw moment of $W$ is finite and equals $e^{r^2/2}$. Show that $E[e^{tW}]$ is infinite for every positive $t$, while it is finite for nonpositive $t$. Explain why a characteristic function nevertheless exists and why the formal moment power series cannot supply a positive-argument MGF. The normal density is supplied here as a mathematical input; its family is studied in Unit 9.

**Solution, step 1: Complete the square for a raw moment.** The required expectation is the integral of $e^{rz}$ against the stated normal density. The exponent satisfies $rz-z^2/2=-(z-r)^2/2+r^2/2$. Factoring out $e^{r^2/2}$ leaves a shifted normal density integrating to one. Therefore $E[W^r]=e^{r^2/2}$, finite for every positive integer $r$. In particular the mean and every higher polynomial moment exist.

**Solution, step 2: Inspect the positive-argument exponential integral.** For positive $t$, the MGF integral contains the factor $\exp(te^z-z^2/2)$. As $z$ increases, $te^z$ eventually dominates the quadratic term, so the exponent tends to positive infinity. The integrand does not decay and its integral over a sufficiently large positive tail is infinite. Thus no positive argument belongs to the finite MGF domain. This is stronger than saying that a convenient closed formula is unavailable.

**Solution, step 3: Check the other side and characteristic existence.** For nonpositive $t$, $W$ is positive and $0<e^{tW}\leq1$, so its expectation is finite; at zero it equals one. The domain therefore includes the nonpositive half-line but no open interval around zero. The characteristic integrand $e^{itW}$ has magnitude one for every real argument, so its expectation exists. Existence of this complex transform does not require the absent positive exponential moment.

**Solution, step 4: Test the formal series.** The formal MGF terms would be $e^{r^2/2}t^r/r!$. For any fixed positive $t$, the ratio of consecutive terms is $te^{r+1/2}/(r+1)$, which grows without bound. The terms fail to tend to zero, so the series diverges. Finite moments of every order therefore do not justify substituting them into a convergent positive-argument MGF expansion. The neighborhood condition used earlier is substantive, not a technical ornament.

## Factorial moments and ordinary moments

PGF derivatives naturally produce descending products of a count. The product of order two is the count times one less than the count; the product of order three continues with two less than the count. These are factorial powers, not powers in the ordinary sense. Their expectations often match a counting interpretation: the second factorial moment counts ordered distinct pairs of successes, while the third counts ordered distinct triples.

For a count formed from binary indicators, the product of the total count with one less than itself can be expanded as a sum over distinct ordered indicator pairs. Each pair product equals one when both corresponding events occur. Therefore its expectation is the sum of the pair intersection probabilities. This is valid without independence. Independence simplifies those intersections into probability products, but the factorial-moment identity itself comes from counting and linearity.

Ordinary powers can be expressed through factorial powers. The square of a count equals its second factorial power plus the count. The cube equals its third factorial power plus three times its second factorial power plus the count. The fourth power equals its fourth factorial power plus six times its third, plus seven times its second, plus the count. These identities can be checked by expanding the products as polynomials in the count.

Consequently a PGF supplies raw moments as combinations of its derivatives at one, when they are finite. The coefficients reflect ways to group repeated indices when an ordinary power of a sum of indicators is expanded. A term with all distinct indices corresponds to the highest factorial power; terms with repeated indices correspond to lower ones. This interpretation explains why extra terms appear rather than treating them as arbitrary correction coefficients.

The conversion is particularly useful for sparse-count models, where factorial moments can be easier to derive than raw moments. It is also a source of errors if derivative order is labeled simply moment without specifying the factorial convention. A calculation of variance must combine the second factorial moment with the first raw moment before subtracting the squared mean. The required correction follows from the polynomial identity and is not a statistical bias adjustment.

## Joint transforms and mixed moments

For two variables with an appropriate joint exponential-moment domain, define a joint MGF by averaging $e^{sX+tY}$. Differentiating in one argument produces moments of that coordinate; differentiating in both produces mixed moments such as $E[XY]$. Setting one argument to zero gives the other variable's marginal MGF. A joint transform therefore preserves dependence information that two separate marginal transforms omit.

If the variables are independent, the joint MGF factorizes into the product of their marginal MGFs. The joint characteristic function has the corresponding factorization without real exponential-moment requirements. This is a transform version of independence across the full law, not a conclusion from matching a single derivative. A mixed second derivative equal to the product of first derivatives establishes only a zero-covariance relationship under the relevant moments.

Taking the logarithm of a valid joint MGF produces mixed cumulants. Its mixed second derivative at the origin is covariance. To see this, differentiate the logarithm first in one argument and then in the other; at the origin the joint transform is one, the two first derivatives are the marginal means, and the mixed derivative is the product expectation. The resulting subtraction is exactly the covariance definition from Unit 4.

Under independence, the joint logarithm separates into a function of one argument plus a function of the other. Mixed derivatives involving both arguments then vanish. This is stronger than the vanishing of one covariance. Higher mixed derivatives can represent relationships not visible at second order, much as pairwise independence can miss higher-order event restrictions. Using a joint representation makes the information requirement explicit.

The transform of a linear combination can be obtained by substituting scaled arguments into a joint transform. For example, the MGF of a sum uses the same argument for both coordinates. If the variables are dependent, that substitution is still valid in the joint transform, while replacing the joint transform by a product of margins is not. This distinction offers a compact way to compute a sum law without silently imposing independence.

## Feasibility of moment summaries

Not every proposed collection of moments can belong to a probability law. Variance must be nonnegative, so a proposed second raw moment cannot be smaller than the square of the proposed mean. More generally, the expectation of the square of any polynomial in the variable must be nonnegative whenever its terms are integrable. Expanding that square yields inequalities among moments. These conditions are useful consistency checks before using a moment list in a model.

For a centered variable with finite fourth moment, the squared second moment is at most the fourth moment. This follows by applying nonnegativity of variance to the squared centered variable, or by Cauchy–Schwarz. Thus population kurtosis is at least one when variance is positive. The two-point law in the first worked question satisfies this bound. A reported population kurtosis below one would indicate an incompatible definition, an arithmetic error or a quantity that is not the population-law ratio used here.

A related inequality connects skewness and kurtosis. Standardize a nondegenerate variable to have mean zero and second moment one. The covariance of that standardized variable with its square equals its third moment. Cauchy–Schwarz bounds the squared covariance by the product of the variable's variance and the variance of its square. The result is that squared skewness is at most kurtosis minus one. This constraint does not identify a distribution, but it rules out some inconsistent pairs of shape summaries.

For the first worked law, squared skewness is four thirds and kurtosis minus one is also four thirds, so the inequality is attained. The equality reflects a special relationship available in a two-point distribution. Attainment of a bound deserves a structural explanation rather than being dismissed as numerical coincidence. Conversely, a near equality in estimated sample summaries may be affected by estimation and should not automatically be interpreted as exact distribution structure.

Finite-order feasibility checks do not prove that an arbitrary infinite moment sequence determines a unique law. Moment problems can require additional conditions and are outside the depth of this course. The practical lesson is narrower: use basic nonnegativity and support constraints to audit proposed summaries, and do not infer a full distribution from a small moment list unless a stated family assumption supplies the missing structure.

## Transform interpretation and numerical checks

Transform calculations should begin with a support and domain statement. A PGF concerns nonnegative integer counts and carries masses in its coefficients. An MGF uses real exponentials and may have a limited finite domain. A characteristic function uses bounded complex exponentials and always exists, though its derivatives may not. A cumulant generator is the logarithm of a valid local MGF, while algebraic cumulant relations can still be discussed for finite moments without claiming that local generator exists.

For a finite law, independently compute weighted raw and centered moments and compare them with transform derivatives or power-series coefficients. For an independent count sum, enumerate binary outcomes or convolve the masses, then compare the resulting coefficients with the product PGF. For an unbounded law, check analytic existence rather than relying on a truncated numerical integral. A finite numerical output from a truncated tail cannot prove a divergent integral is finite.

Numerical differentiation of high-order derivatives can be unstable. Small step sizes amplify rounding errors, while large step sizes introduce approximation error. Exact polynomial coefficient calculations or symbolic formulas are preferable when available. For finite rational examples, rational arithmetic can preserve all coefficients exactly and provide a strong check independent of rounded displays. A correct plot of a transform does not by itself verify its derivatives at zero.

No separate interactive simulation is required for this unit's planned treatment. Its principal learning tasks concern exact coefficient algebra, existence and transform domains, which a random animation would not establish. Executable coefficient and moment checks are more useful here. Distribution explorers in later units will use these derived summaries where they clarify model behavior, while clearly distinguishing theoretical values from simulated frequencies.

The next units develop specific discrete and continuous laws. Generating functions will help derive their moments and independent-sum properties, but each law will first be connected to its experiment and support. The most useful transform is the one that preserves those connections and answers the target question under valid assumptions, rather than the one that merely produces the shortest formula.
