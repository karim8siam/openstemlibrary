# Unit 7: Moments, Skewness, Kurtosis and Distribution Shape

## 7.1 Shape is more than a single coefficient

A distribution's shape describes how its values are arranged across their range. Features include symmetry or asymmetry, concentration, gaps, multiple peaks, and the relative prominence of tails. A mean and standard deviation cannot distinguish all these features. Numerical coefficients add useful descriptions, but a graph and the context of measurement remain necessary. This unit extends the centred-deviation calculations from variance to third and fourth powers while keeping their limitations visible.

Symmetry means that the distribution is balanced under reflection around a specified centre. An exactly symmetric finite dataset can be paired so that corresponding deviations have equal magnitude and opposite signs, with possible observations at the centre. Values 1, 2, 3, 4, and 5 are symmetric around three. A random sample from a symmetric population need not be exactly symmetric, so distinguish a property of the recorded sample from a model for the broader population.

Right asymmetry is often associated with a longer or more influential upper tail, and left asymmetry with a lower tail. The wording should be supported by the data display and the chosen coefficient. A few high observations can create a large positive third-moment coefficient, while a quantile-based coefficient may still describe a nearly symmetric central portion. These measures examine different aspects of the data rather than necessarily contradicting one another.

Multimodality is separate from skewness. A dataset can have two symmetric peaks and zero third central moment. Conversely, a distribution can have one peak and substantial asymmetry. A kurtosis coefficient also does not count modes. Treating these numbers as a complete classification system can lead to false descriptions. Inspect a histogram with suitable binning, a dot plot for small datasets, and subgroup information when available.

The sample size and measurement resolution matter. Rounded values create ties and can make peaks appear sharper. A small sample's third and fourth moments can be dominated by one observation. A large dataset assembled from heterogeneous groups can have a shape unlike any individual subgroup. Numerical shape summaries should therefore be reported with count, units, eligible population, and relevant grouping information, not as isolated labels.

Shape coefficients usually remove units by standardizing powers of deviations. This permits comparisons across positive linear unit conversions but does not make different constructs substantively equivalent. A skewness coefficient for income and the same coefficient for a chemical concentration describe a common mathematical feature, not the same social or scientific process. Measurement validity remains relevant after units cancel.

We will define moments explicitly, state the finite-sample denominator conventions, and separate descriptive coefficients from adjusted estimators. The probability book later develops population expectations and theoretical distributions. Here, every basic calculation concerns a finite recorded dataset with finite values. The mathematical language provides a bridge to later theory without pretending that a calculated sample coefficient reveals a population shape with certainty.

## 7.2 Raw moments and central moments

The raw moment of order r for a finite dataset is the average of the observations raised to the rth power. We write it as a-r, using denominator n. The first raw moment is the mean. The second raw moment is the mean of squares, not the variance. A raw moment depends on the origin of the measurement scale, because adding a constant changes the powers of the observations. Its units are the original unit raised to power r.

The central moment of order r is the average of the rth powers of deviations from the mean, again with denominator n. We write it as m-r. The first central moment is zero because signed deviations from the mean sum to zero. The second is the descriptive variance m2. The third records signed cubed deviations, and the fourth averages nonnegative fourth powers. These definitions use the same eligible dataset and mean throughout.

The zeroth raw and central moments equal one under the conventional power-zero definition, because the average of n ones is one. This is an algebraic convention useful in expansions. It does not mean that a missing or empty dataset has a defined moment. We still require n greater than zero and valid numerical observations. A zero-valued observation contributes zero to positive-order raw powers and its appropriate centred power to central moments.

For values 1, 2, and 3, the mean is two. The first three raw moments are two, fourteen divided by three, and twelve. Centred deviations are minus one, zero, and one. Therefore m2 is two thirds, m3 is zero, and m4 is two thirds. Notice that m4 is not m2 squared: two thirds differs from four ninths. Averaging powers and taking powers of an average are different operations.

For exact frequency values, multiply each power by its frequency and divide by total frequency. Frequencies preserve replicated observations. For grouped intervals, midpoint powers give approximations, and nonlinear powers can magnify the error due to grouping. A grouped fourth moment should not be presented as exact merely because all calculations were carried out to many decimal places. The original within-class values remain unknown.

Odd central moments can be positive, negative, or zero because odd powers retain sign. Even central moments are nonnegative because even powers do not. For an exactly symmetric finite collection around its mean, paired odd powers cancel. The converse is not generally true: a zero third moment alone does not force every part of the distribution to be symmetric. Several unequal contributions can cancel without producing mirror-image data.

Central moments are unaffected by adding a constant because the mean shifts by the same amount as every observation. Under multiplication by b, the rth central moment multiplies by b to the rth power. A negative b therefore reverses odd central-moment signs and leaves even-order signs nonnegative. Raw moments do not have this simple shift invariance, which is why centring is important for describing shape independently of an arbitrary origin.

Higher-order moments are increasingly sensitive to large deviations. A deviation twice as large contributes four times as much to the second power, eight times as much in magnitude to the third, and sixteen times as much to the fourth. This mathematical sensitivity can highlight tails but also magnify a transcription error. Validate unusually large observations before interpreting a high-order coefficient as a scientific feature.

## 7.3 Converting between raw and central moments

Central moments can be expressed through raw moments by expanding powers of x minus the mean. The second central moment is a2 minus a1 squared. The third is a3 minus three a1 a2 plus two a1 cubed. The fourth is a4 minus four a1 a3 plus six a1 squared a2 minus three a1 to the fourth power. These formulas follow from the binomial expansion and averaging term by term.

For the values 1, 2, and 3, a1 is two, a2 is fourteen thirds, a3 is twelve, and a4 is ninety-eight thirds. Substitution gives m2 equal to two thirds, m3 equal to zero, and m4 equal to two thirds. Calculating the centred powers directly gives the same answers. Using two algebraically independent representations on a small dataset is a useful verification method, especially for detecting a missing coefficient or sign in an expansion.

For a reference c that is not necessarily the mean, define coded deviations u equal to x minus c. Calculate the raw moments of u, and let their first moment be d. The central moments of x equal the central moments of u, so the same expansion with d as the coded mean recovers m2, m3, and m4. Choosing c near the observations keeps the powers smaller and can simplify hand arithmetic.

This coding is computational convenience, not a change in the scientific reference for central moments. The central moments remain centred at the actual mean. If we average powers around a fixed target c without applying the correction, we obtain moments about that target, which combine location departure and spread. Both can be useful, but they should be named differently. A quality-control question about deviation from specification is not identical to a shape question centred at the observed mean.

Raw-to-central formulas can suffer numerical cancellation for large-offset data. Several large terms may nearly cancel to produce a small central moment. Floating-point arithmetic retains finite precision, so subtracting these terms can lose accuracy even when the symbolic formula is correct. Direct centred powers, a stable online method, or higher-precision arithmetic is preferable when the scale demands it. The simulation uses direct centred deviations for transparent verification.

Rounding intermediate means can also distort higher moments. If the true mean is one third but it is replaced by 0.3 before cubing deviations, the signed cancellation and resulting coefficient may shift noticeably in a tiny dataset. Retain full available precision internally and round only the displayed final quantities. A worked solution can show a fraction or several digits to make clear that the calculation did not reuse a coarsely rounded display.

The expansion identities hold for any finite dataset with appropriate numerical values, without an assumption of normality. They are descriptive algebra. In a population setting, corresponding expectation identities require the relevant moments to exist. The probability course makes that distinction precise. Avoid carrying an empirical calculation over to a theoretical heavy-tailed model without checking whether its moments are finite.

These relationships also provide audit checks. m2 should agree with the descriptive variance from unit six. The first central moment should be approximately zero. The fourth moment should be nonnegative. Agreement with these necessary properties does not alone prove correctness, but disagreement exposes a problem that must be resolved before publication or interpretation.

## 7.4 Moment skewness and adjusted conventions

For a dataset with positive m2, the descriptive moment skewness g1 is m3 divided by m2 raised to the power three halves. It is dimensionless because both numerator and denominator have cubic original units. Positive g1 means positive cubed deviations outweigh negative cubed deviations under this definition, and negative g1 means the reverse. If m2 is zero, every observation is equal and the ratio is undefined; report that condition rather than assigning a numerical shape coefficient.

The sign is often consistent with an influential upper or lower tail, but interpret it through the plot. Cubing strongly emphasizes large deviations. A central cluster with one high observation can yield positive g1 even if much of the middle is balanced. A zero value is compatible with exact symmetry, but cancellation can also occur in asymmetric datasets. Skewness is one summary of signed tail-weighted behaviour, not a proof of an entire distributional shape.

For values 0, 0, and 3, the mean is one. The centred deviations are minus one, minus one, and two. m2 is two and m3 is two, so g1 is one divided by the square root of two, approximately 0.707107. The high observation contributes eight to the cubed-deviation sum, while the two low observations contribute minus one each. This small example makes the weighting mechanism visible.

A commonly used adjusted Fisher-Pearson sample skewness is G1 equal to the square root of n times n minus one divided by n minus two, multiplied by g1. It requires n greater than two and positive variance. Parentheses matter: the square root applies to n times n minus one, while n minus two is outside the root in the denominator. For the three-value example the factor is the square root of six, producing adjusted skewness approximately 1.73205.

The adjusted coefficient and the descriptive coefficient are different quantities. Software may label either one skewness. State the definition, sample size, and adjustment when reproducing a result. The adjustment is motivated by sampling considerations, but it should not be advertised as a universal unbiased estimator of population skewness under every distribution. Ratios involving estimated moments have subtle finite-sample behaviour.

Multiplying all observations by a positive constant leaves g1 unchanged because m3 and m2 to the three-halves power scale equally. Adding a constant also leaves it unchanged. Multiplication by a negative constant reverses its sign. Thus a reflected dataset has opposite moment skewness. These transformation properties are useful for tests: a simulation should give the same positive-scale result and the opposite reflected result within numerical tolerance.

Data exclusions and transformations can change skewness substantially. A log transformation of positive right-skewed measurements may reduce asymmetry on the transformed scale, but the log-scale coefficient describes log measurements, not the original units. Excluding an extreme value merely because it raises skewness changes the dataset and requires justification. The coefficient should support transparent description rather than serve as a target manipulated until an analysis looks conventional.

For a small sample, report a coefficient with appropriate modest precision and a graph. An exact-looking decimal with many digits can conceal severe sampling instability. This book's example values are synthetic and allow precise arithmetic checks. A real application should distinguish computational precision from confidence about a population parameter. Later inference courses address uncertainty in skewness estimates.

## 7.5 Quantile and location-based asymmetry measures

Bowley's quartile skewness uses Q1, the median Q2, and Q3. Its numerator is Q3 plus Q1 minus twice Q2, and its denominator is Q3 minus Q1. When the IQR is positive, the coefficient compares the upper and lower distances within the central quantile span. It lies between minus one and one because Q2 lies between Q1 and Q3. Use a declared quantile convention, since different quartiles can change the result in a small sample.

For sorted values 1, 2, 3, 4, 5, 6, 7, and 30, type-seven quartiles are 2.75, 4.5, and 6.25. Their upper and lower central distances are equal, so Bowley skewness is zero despite the high observation thirty. The moment coefficient is positive. This is an instructive difference: one measure describes the central quartile geometry, while the other gives large tail deviations strong influence. Neither should be substituted for the other without explanation.

If Q1 and Q3 coincide, Bowley skewness is undefined because the IQR is zero. The dataset may still contain values away from that repeated central level. A display should show the zero denominator and describe the concentration rather than force a ratio. Similar precautions apply to decile- or percentile-based asymmetry measures. Their robustness and sensitivity depend on which parts of the distribution they use.

Pearson's second skewness coefficient is three times the mean minus the median divided by a declared standard deviation. It is a location-based summary and differs from the third-moment coefficient. The factor three is part of the conventional definition, not an identity linking the median to a theoretical moment. State whether the denominator uses descriptive or sample standard deviation. Changing that convention changes the numerical value.

Pearson's first coefficient uses mean minus mode divided by standard deviation. It requires a defensible mode, which can be difficult for continuous data and depends on grouping or smoothing when exact repeats are absent. A multimodal dataset cannot be reduced to a unique modal value without a rule. For that reason, we emphasize the second coefficient and the directly defined moment and quantile coefficients rather than claiming that a mode is always easy to recover.

The often quoted ordering mean greater than median greater than mode for right-skewed data is a useful pattern in some smooth unimodal distributions, not a universal finite-data theorem. There are asymmetric and multimodal examples that violate it. Use actual calculations and plots. A positive mean-minus-median does not establish every claim about tail shape, and a small difference does not prove symmetry.

Comparing several coefficients can identify where asymmetry appears. A large positive moment coefficient with a near-zero Bowley coefficient suggests that upper-tail deviations have more influence than central-quartile imbalance. That interpretation should be checked against the actual observations. It may reflect one genuine rare event, a mixture, or an error. The numerical contrast directs attention but does not decide the substantive explanation.

Do not average skewness coefficients across groups to recover an overall coefficient. The combined distribution's centre and spread differ from the group centres and spreads, and central moments combine through additional between-group terms. An overall asymmetry can arise from mixing symmetric groups with different means and sizes. Preserve the original data or sufficient moment information if a combined calculation is needed.

## 7.6 Kurtosis, excess kurtosis and tails

The descriptive raw kurtosis coefficient b2 is m4 divided by m2 squared when m2 is positive. It is dimensionless because numerator and denominator both have fourth-power units. Excess kurtosis g2 is b2 minus three. The subtraction uses the normal distribution's population raw kurtosis of three as a reference. A raw value three and an excess value zero therefore express the same normal-reference comparison, but they are different numerical conventions.

Kurtosis is often described loosely as peakedness. That description is incomplete and can be misleading. Fourth powers strongly weight large standardized deviations, so tail contributions are central to the coefficient. Distributions with similar central peaks can have different kurtosis, and distributions with different peaks can have similar kurtosis. Inspect the tails and the full display rather than interpreting a high value as proof of one sharp central spike.

For 0, 0, and 3, m2 is two and m4 is six. Raw kurtosis is six divided by four, or 1.5, and excess kurtosis is minus 1.5. The dataset is right-asymmetric while its excess kurtosis is negative. This demonstrates that skewness and kurtosis describe different aspects and that a small sample with an influential extreme need not have positive excess kurtosis. Relative distances, sample size, and the whole configuration matter.

Positive excess relative to a normal reference is conventionally called leptokurtic, zero excess mesokurtic, and negative excess platykurtic. These labels refer to the stated coefficient, not a complete guarantee about every tail or visual feature. A finite sample's excess of zero does not prove it was sampled from a normal population. Numerous nonnormal distributions can share selected moments, and an empirical estimate fluctuates with sample selection.

A common adjusted excess-kurtosis estimator, for n greater than three, is (n minus one) divided by ((n minus two)(n minus three)), multiplied by ((n plus one)g2 plus six). State the entire formula if used. It differs from descriptive excess and has a particular sampling motivation. The explorer in this book reports descriptive raw and excess kurtosis, making the simpler finite-data definition visible. Adjusted values are explained in the text rather than silently replacing that display.

Kurtosis is undefined for a constant dataset because m2 is zero. The fourth moment itself is zero, but the standardized ratio is zero divided by zero. A numerical routine should not label this as excess minus three or raw zero. The appropriate output states that there is no positive variation with which to standardize shape. This is a general denominator rule shared by skewness and several association measures.

High-order moment calculations require finite inputs. A sentinel such as 999 used for missing data can dominate m4 before anyone notices that it was not a measurement. Clean and validate the data under documented rules first. Do not infer a heavy-tailed scientific phenomenon from a column that still contains encoded missing values or mixed units. A correct formula applied to the wrong variable is not a correct statistical analysis.

## 7.7 A relationship between skewness and kurtosis

Moment coefficients obey useful mathematical constraints. For the descriptive definitions in this unit, raw kurtosis b2 is at least g1 squared plus one when m2 is positive. This is sometimes called the skewness-kurtosis inequality. It gives a check on numerical calculations and shows that large moment asymmetry imposes a minimum fourth-moment contribution. It does not identify the entire distribution or replace plotting.

To understand the inequality, standardize the observations using the descriptive mean and standard deviation. Their average is zero and their average squared value is one. Their average cube is g1 and average fourth power is b2. Consider the average square of the expression z squared minus g1 times z minus one. A square cannot be negative. Expanding and using these moment identities gives b2 minus g1 squared minus one, which must therefore be nonnegative.

This proof is finite-data algebra and requires no normality assumption. For the values 0, 0, and 3, g1 squared is one half and b2 is 1.5, so equality holds. Two distinct standardized values can make the squared expression zero at every observation. Equality is a special configuration, not a general expectation for real datasets. The inequality applies to the descriptive coefficients, so adjusted sample estimators should not be substituted without reconsidering the formula.

The bound implies raw kurtosis is at least one and excess kurtosis at least minus two under these descriptive definitions. A calculated raw kurtosis below one exposes a problem in the data, denominator, or implementation. A value above one does not prove the routine is correct; it passes only a necessary constraint. Combine the inequality with translation and scaling checks and independently calculated examples.

For empirical finite collections, sample-size restrictions can place additional bounds on possible standardized moments, but they are beyond the core introductory syllabus here. The important lesson is that shape coefficients are related through their shared deviations. They are not arbitrary independent labels. A report that quotes impossible combinations may have mixed software conventions or used different eligible subsets for the calculations.

Use the same observations for m2, m3, and m4. If missing-value filtering differs between powers, the inequality and intended coefficient definitions no longer apply to one coherent dataset. This can happen in poorly assembled spreadsheets or when separate calculations exclude different records. Validate eligible counts and row identifiers before interpreting a numerical constraint failure as a mathematical mystery.

## 7.8 Shape under transformation and mixture

Adding a constant does not change descriptive skewness or kurtosis. Positive multiplication does not change either standardized coefficient, while negative multiplication reverses skewness and preserves kurtosis. These results follow from the moment scaling rules and offer direct simulation tests. A conversion from metres to centimetres must not change dimensionless shape. If it does, inspect the implementation or whether a nonlinear conversion was actually applied.

Nonlinear transformations can alter shape. Taking logarithms of positive values compresses large ratios and changes the distances used in moment calculations. A distribution may look more symmetric on the log scale, but the resulting coefficients describe that transformed variable. Back-transforming a mean of logs gives a geometric mean, not the original arithmetic mean. Transformation affects both the descriptive quantity and the interpretation of an eventual model.

Monotonic transformations preserve order but not equal spacing. A quantile's underlying rank relation can remain meaningful while moment coefficients change. Even interpolated sample quantiles can fail to commute exactly with nonlinear transformation because linear interpolation is performed on different scales. State the order of operations when reproducing transformed summaries: transform individual values and then calculate, or transform a previously calculated summary. Those procedures need not agree.

Mixtures of groups can generate asymmetry or multiple peaks even if each group is symmetric. Two narrow groups with different means and unequal sizes can produce an overall distribution pulled toward one side. Changes in group composition can therefore change overall skewness without a change in any group's internal shape. A useful analysis examines subgroup counts and summaries before attributing the overall pattern to one common mechanism.

Measurement limits can also alter shape. Values below a detection threshold may be censored, values above an instrument maximum may be capped, and rounding can create artificial piles. A histogram and moment coefficients then describe the recorded measurement process as well as the underlying phenomenon. Specialized methods are needed to infer an uncensored distribution. This introduction records the limitation rather than pretending that ordinary coefficients solve it.

Changing the eligibility definition changes the distribution. Including zero expenditure for nonbuyers versus analysing buyers only can produce different means, spread, and skewness. Neither distribution is intrinsically the true one for every question. Define the target population and event before calculation. A shape comparison across time must use compatible definitions or explain the change.

## 7.9 Building a reproducible shape summary

Begin with a validated numerical column, a count of eligible and missing observations, and a measurement unit. Inspect a suitable plot and identify obvious rounding or grouping. Calculate the mean and descriptive variance, then use the same centred deviations for third and fourth moments. Keep the calculation convention consistent. If the variance is zero, stop the standardized-shape calculations and report the constant value.

Record both the formula and software convention. A table headed skewness and kurtosis is ambiguous unless it identifies descriptive versus adjusted skewness and raw versus excess kurtosis. A concise footnote can remove that ambiguity. If a reference tool gives different numbers, first compare eligible rows, denominator definitions, adjustments, and quantile methods before assuming one tool contains a bug.

Compare moment and quantile-based descriptions when the scientific question warrants it. A median and IQR describe central rank locations, while g1 and b2 give large deviations more weight. Their disagreement can be informative. Report the observed contrast in plain language and inspect which observations produce it. Do not conceal a coefficient because it does not support a preferred visual story.

Use sensible precision. A coefficient reported to ten decimal places is not a population fact with ten-decimal certainty. Keep sufficient internal precision for checking, but display a modest number of digits appropriate to the sample and purpose. If the dataset is small, emphasize the actual values and graph. If it is large, preserve reproducible code and eligibility rules so that a reviewer can inspect the tail records.

Distinguish an audit from a substantive explanation. Confirming that m4 and the standardized coefficient are calculated correctly does not establish why the tail is long. Source records, design, and domain knowledge are required. A responsible report can state that several high measurements strongly influence fourth-moment shape while leaving their cause open pending investigation.

Three worked questions in this unit calculate moments and shape for a small asymmetric dataset, verify translation and scaling properties, and compare quartile asymmetry with moment asymmetry in a dataset containing an upper extreme. The solutions explicitly retain the descriptive denominator n. Adjusted formulas are available in the explanatory text so that the assessed calculations remain focused and reproducible.

## 7.10 The shape explorer and its educational limits

The shape explorer keeps several low and central values fixed and allows a high value to change. It displays m2, m3, m4, g1, raw kurtosis, and excess kurtosis. Before changing the control, calculate a small reference case by hand. Predict that adding a constant to all values would leave standardized shape unchanged, whereas moving only the final observation can change every central moment because the mean itself also moves.

The simulator should centre at the current mean on every update. It should display an unavailable result if variance is zero and avoid NaN or infinite text leaking into the reader. Direct centred arithmetic is used for clarity, and numerical tests compare selected settings with an independent calculation. The skewness-kurtosis inequality provides an additional check, but does not replace the independent examples.

Watch the graph and the coefficients together. A changing fourth-moment coefficient illustrates sensitivity to large standardized distances. It does not diagnose a named population distribution. The displayed values are synthetic and fixed except for the control; there is no random sampling uncertainty in this particular demonstration. The lesson is about descriptive behaviour, not a fitted probability model.

Reset should restore the original data and every summary. A small-screen reader should receive the same numerical information as a wide-screen reader, and a textual table should make the result understandable without colour. The display should state raw versus excess kurtosis next to the numbers rather than relying on a distant explanation. Accuracy includes making the correct convention easy to see at the point of use.

Before moving to association, explain why a zero third moment does not prove symmetry, why kurtosis is not simply a measure of peak height, and why adding a constant leaves central shape unchanged. Calculate raw and excess kurtosis from m2 and m4, and identify when the ratio is undefined. These skills complete the main single-variable descriptive toolkit and prepare for paired-variable summaries.
