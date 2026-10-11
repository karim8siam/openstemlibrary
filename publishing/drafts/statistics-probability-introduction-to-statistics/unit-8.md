# Unit 8: Correlation and Measures of Association

## 8.1 Paired observations and the question of association

Association concerns how the values of variables vary together across comparable observational units. A paired dataset requires that each x value and its y value belong to the same relevant unit or event. For a study of hours spent revising and examination marks, pairing connects a student's hours to that student's mark. Sorting the two columns separately destroys those connections. A resulting coefficient can look impressive while describing invented pairs rather than the observed relationship.

Start with the measurement scales and the target question. Two numerical variables can support a scatter plot and Pearson correlation when linear association is the intended summary. Ordered variables can support rank-based measures. Two binary variables can be represented in a two-by-two table. Agreement between repeated measurements raises different questions from association alone. A coefficient should be selected because its definition matches the variables and question, not because it is available in a software menu.

A scatter plot is a first diagnostic for numerical pairs. Inspect direction, curvature, clusters, extreme points, and differences in spread. A single coefficient compresses this structure. A near-zero Pearson correlation can coexist with a strong curved relationship, and a large value can be driven by one high-leverage observation. The plot is part of the analysis rather than an optional decoration after the coefficient is computed.

Association does not by itself establish causation. A positive relation between study hours and marks may reflect preparation, motivation, prior knowledge, course difficulty, or selective reporting as well as an effect of additional study. A statistical calculation cannot decide between these explanations without an appropriate design and substantive assumptions. Random assignment, when relevant and properly implemented, addresses different questions from random sampling. Keep the distinction developed in unit one.

Repeated observations from the same person or institution require special attention. Treating every row as an independent unit can overstate the apparent amount of information in later inference. A descriptive correlation can still be calculated for recorded pairs, but its target may mix within-person and between-person relationships. A structured analysis should identify repeated units and consider the level at which the question is posed.

Missing values must be handled as pairs. A Pearson coefficient computed after excluding any row with a missing x or y describes the complete-pair subset. Independently filtering each column can break pairing. Pairwise deletion across many variables can also produce a correlation matrix that lacks properties expected of a single coherent complete-data matrix. This unit uses explicit complete pairs and reports their count; later multivariate courses discuss more complex missing-data procedures.

Range restriction can change correlation. A sample containing only students with very similar entrance scores may show a different relationship from a broader sample spanning the full score range. Correlation is a property of the distribution of paired values, not a universal constant of two variable names. A result should identify population, eligibility criteria, period, and measurement definitions before being generalized.

The coefficients in this unit have different assumptions and interpretations. We will derive descriptive Pearson correlation, compare rank measures with explicit tie handling, and introduce syllabus-listed special cases such as point-biserial, biserial, tetrachoric, correlation ratio, and intraclass correlation. Some specialized measures rely on latent-variable models. Their formulas should not be presented as assumption-free corrections to ordinary observed association.

## 8.2 Covariance and Pearson correlation

For n paired numerical observations, calculate each variable's mean and centred deviations. Define Sxx as the sum of squared x deviations, Syy similarly, and Sxy as the sum of products of paired x and y deviations. Descriptive covariance is Sxy divided by n. Conventional sample covariance divides by n minus one when n is at least two. The covariance has the product of the two variables' units and can be positive, negative, or zero.

Positive products occur when both deviations have the same sign; negative products occur when their signs differ. A positive Sxy therefore indicates that same-side deviations outweigh opposite-side deviations in magnitude. The magnitude depends on measurement units. Converting hours to minutes multiplies the covariance by sixty, so covariance alone is awkward for comparisons across scales. Standardization removes this unit dependence.

Pearson correlation r is Sxy divided by the square root of Sxx times Syy, provided both squared-deviation sums are positive. Using descriptive covariance with descriptive standard deviations gives the same ratio as using sample covariance with sample standard deviations, because the common denominator cancels. Mixing conventions between numerator and denominator would not cancel correctly. A constant x or y makes correlation undefined.

The coefficient lies between minus one and one. The sum of products of two centred vectors cannot exceed the product of their lengths in absolute value, by the Cauchy-Schwarz inequality. This gives the bound. Equality occurs when one centred vector is an exact positive or negative multiple of the other, corresponding to a perfect nonconstant straight-line relationship. A software result outside the interval beyond tiny rounding error indicates a problem.

For x values 1, 2, 3 and y values 2, 4, 6, r is one because y equals twice x. Replacing y by 6, 4, 2 gives r minus one. Adding a constant to a column does not change correlation, and multiplying by a positive constant leaves it unchanged. Multiplying exactly one column by a negative constant reverses the sign. These identities provide simple tests for a correlation implementation.

Zero Pearson correlation does not mean no relationship. For x values minus two, minus one, zero, one, and two, and y equal to x squared, centred-product contributions cancel, yielding r zero. The relationship is exact and curved. A scatter plot makes this obvious. Pearson correlation summarizes linear association; a failure to capture curvature is a limitation of the chosen summary, not evidence that the paired variables are unrelated.

Magnitude labels such as weak, moderate, or strong depend on context, measurement reliability, range, and purpose. A coefficient useful for one physical process may be inadequate for an individual clinical decision. Avoid universal thresholds presented as scientific laws. Report the actual coefficient, count, plot, and context, then explain the practical relevance. Statistical significance, introduced later, is separate from strength and does not establish causality.

Correlation is symmetric: exchanging x and y leaves r unchanged. Regression slopes are not generally symmetric, because predicting y from x and predicting x from y solve different minimization problems. This distinction prepares for unit nine. A correlation coefficient does not itself specify a prediction equation, a direction of causation, or agreement with an identity line.

## 8.3 Spearman rank correlation and ties

Spearman correlation applies Pearson correlation to the ranks of the paired observations. Ranking replaces magnitudes by order positions, making the coefficient sensitive to monotonic rather than strictly linear patterns. A perfectly increasing relationship with distinct values has rank correlation one even when the original scatter plot is curved. A perfectly decreasing ordering has rank correlation minus one. Nonmonotonic patterns can still produce a small coefficient despite strong structured dependence.

Assign ranks independently within each variable while preserving row pairing. The smallest value receives rank one. Tied values receive the average of the positions they occupy, called midranks. For x values 10, 20, 20, and 40, the ranks are 1, 2.5, 2.5, and 4. The two tied twenties occupy positions two and three. Their shared midrank preserves the total rank sum and avoids imposing an artificial order among equal values.

After ranking, calculate Pearson correlation of the rank columns using their actual centred sums. This definition handles ties directly. The familiar shortcut one minus six times the sum of squared rank differences divided by n times n squared minus one is exact when both rankings contain no ties. Applying it unmodified to tied midranks can give a different, incorrect value. Do not treat a convenient no-tie formula as the general definition.

For x ranks 1, 2, 3, 4 and y ranks 1, 3, 2, 4, squared differences total two. The no-tie formula gives one minus twelve divided by sixty, or 0.8. Calculating Pearson correlation of the rank vectors gives the same result. A tie example should instead use the rank covariance formula, so the distinction is visible in a worked calculation rather than relegated to a warning.

Spearman correlation is invariant under strictly increasing transformations applied to either variable because those transformations preserve ranks. A strictly decreasing transformation reverses that variable's ranks and changes the sign. Transformations that create ties, such as heavy rounding or categorization, can change the coefficient. Measurement resolution therefore still matters even though the original numerical gaps are not used.

Ranking reduces the influence of an observation's extreme magnitude but does not remove all sensitivity or bias. A value moved far upward retains its top rank once it passes all others, but changes in ordering can alter the coefficient. Selection, confounding, and missingness remain relevant. Rank correlation is not automatically a causal or robust answer to every problem involving unusual values.

An ordinal variable can support ranks if its category order is meaningful, but many ties reduce the number of distinct order comparisons. A constant rank column makes the coefficient undefined just as a constant numerical column does for Pearson correlation. Report ties and complete-pair count. Inference with ties and small samples requires methods appropriate to that structure, addressed in later nonparametric courses.

Interpret Spearman correlation as a summary of concordant ordering under its Pearson-of-ranks definition. It is not the proportion of correctly ordered pairs; Kendall measures relate more directly to pair comparisons. Different rank coefficients can have different numerical values for the same dataset, so compare their meanings rather than expecting them to coincide.

## 8.4 Kendall pair association and explicit tie handling

Kendall association compares pairs of observational units. For two units i and j, inspect the sign of their x difference and their y difference. If both differences have the same nonzero sign, the pair is concordant. If they have opposite nonzero signs, it is discordant. A tie in either variable prevents classification as an ordinary concordant or discordant pair. There are n times n minus one divided by two unordered pairs in total.

With no ties, Kendall tau-a is the number of concordant pairs minus discordant pairs divided by the total pair count. It ranges from minus one to one. For n equal to four with one discordant pair and five concordant pairs, tau-a is four divided by six, or two thirds. The coefficient describes a normalized balance of pair ordering, so it differs numerically from Spearman's Pearson-of-ranks summary.

Kendall tau-b adjusts for ties in either variable. Let C and D be the concordant and discordant counts, Tx the count tied only in x, and Ty the count tied only in y. Tau-b is (C minus D) divided by the square root of (C plus D plus Tx) times (C plus D plus Ty). Pairs tied in both variables contribute to neither factor. This notation avoids confusing single-variable tie counts with counts that include double ties.

An equivalent formula uses the total pair count n0 and the numbers n1 and n2 tied in x and y respectively, including double ties in those separate totals. The denominator is the square root of (n0 minus n1)(n0 minus n2). Both forms agree when counts are defined consistently. Mixing Tx defined one way with a denominator intended for another definition is a common source of errors. Always state what the tie counters include.

If every x value is tied or every y value is tied, the corresponding denominator factor is zero and tau-b is undefined. A displayed result should explain the lack of order variation. With ties, a pattern can be perfectly consistent in the comparisons that remain but not produce a value one unless the tie structure supports that normalization. The definition should govern interpretation rather than an expectation based only on visual direction.

For a small dataset, list all unordered pairs and classify them. This is slower than a library routine but excellent for verifying a tie-aware implementation. For larger datasets, efficient algorithms avoid explicit enumeration of every pair. The book's illustrative explorer and independent tests use small synthetic data, so transparent pair counts are feasible. Later computing courses develop faster methods and numerical performance concerns.

Kendall tau-c uses a different normalization intended for some rectangular ordinal tables. It is not interchangeable with tau-b, and a report should name the version. The core assessed calculation here is tau-b because the course emphasizes paired observations and ties. An introductory reader should know that the word Kendall alone can conceal several conventions.

Like other observed association measures, Kendall coefficients do not establish causation or agreement of measurement scales. Two raters can rank objects identically while one consistently assigns much higher numerical scores. Their pair ordering agrees, but their absolute ratings do not. That distinction leads to concordance and intraclass correlation, where the intended agreement target must be stated more precisely.

## 8.5 Kendall concordance for several rankings

Kendall's coefficient of concordance W summarizes agreement among m rankings of the same n objects. Organize a table with objects as rows and raters as columns, and rank within each rater's column using midranks for ties. Each rater must rank the same eligible objects under a compatible interpretation. If objects are missing for some raters, the ordinary complete-table formula cannot be used without an appropriate missing-data method.

For each object i, add its ranks across raters to obtain Ri. The mean rank sum is m times n plus one divided by two. Let S be the sum across objects of the squared differences between Ri and that mean. With no ties, W is twelve S divided by m squared times n cubed minus n. Parentheses should make clear that the denominator is m squared multiplied by the entire expression n cubed minus n.

For each rater j, compute a tie term Tj by adding t cubed minus t over that rater's tie groups of size t. With ties, the denominator becomes m squared times (n cubed minus n) minus m times the sum of Tj. This correction must correspond to the actual midranks used. A zero denominator occurs when the rankings contain no usable discrimination under the formula and should produce an unavailable result rather than a numerical claim of agreement.

If two raters rank three objects identically as 1, 2, 3, the rank sums are 2, 4, 6, centred at four. S is eight, so W is ninety-six divided by ninety-six, or one. If one gives ranks 1, 2, 3 and the other 3, 2, 1, every rank sum is four, S is zero, and W is zero. The reversal is strong disagreement, but W is nonnegative; it is not a signed two-variable correlation.

W concerns similarity of rank ordering across raters, not absolute equality of numerical scores. A rater who doubles every score can retain the same ranking and contribute perfect rank concordance. If actual score interchangeability matters, use an agreement method suited to the measurement model. A high W also does not prove the ranking criterion is valid for the intended construct; raters can consistently share a systematic misconception.

The number of raters and objects affects what patterns are possible and how inference is conducted. Descriptive W should be reported with those counts and the tie policy. Tests of concordance require additional assumptions and small-sample considerations not developed in this introductory book. Avoid attaching a significance statement solely because a software routine displays one without understanding its reference distribution.

Several rankings can also have subgroups of raters who agree within groups but disagree between groups. One coefficient compresses that structure. Inspect the rank table and pairwise summaries if the application suggests different perspectives or expertise. A consensus coefficient can be useful, but it should not conceal systematic differences that matter to the decision.

## 8.6 Binary-numerical association: point-biserial and biserial

When one observed variable is binary, coded zero and one, and the other is numerical, point-biserial correlation is simply Pearson correlation of those columns. The coding declares which group is positive, so reversing zero and one reverses the sign. No latent-variable assumption is needed for this observed descriptive definition. At least one observation in each group and positive numerical variation are required for a nondegenerate coefficient.

Let p be the proportion in group one, q equal one minus p, and y-bar-1 and y-bar-0 the group means. Using the descriptive standard deviation sN of all y values, point-biserial r equals (y-bar-1 minus y-bar-0) divided by sN, multiplied by the square root of p q. This formula matches Pearson's centred-sum definition. If using the sample standard deviation instead, an additional denominator-convention factor is required; do not mix the formulas.

For binary values 0, 0, 1, 1 and numerical values 1, 3, 5, 7, the group means are two and six. The overall numerical mean is four and descriptive variance five, so sN is the square root of five. Both group proportions are one half. Point-biserial correlation is two divided by the square root of five, approximately 0.894427. Direct Pearson correlation of the paired columns gives the same answer.

Biserial correlation addresses a different model: the observed binary indicator is assumed to arise by thresholding an underlying continuous normally distributed variable. Under that latent normal model, a conventional biserial coefficient is the point-biserial coefficient multiplied by the square root of p q divided by the standard normal density at the corresponding threshold. The threshold has lower-tail probability q when group one denotes the upper region. The density is positive for finite thresholds.

This adjustment is not a universal improvement to an observed coefficient. It relies on a substantive latent-continuous interpretation and distributional assumptions. A genuinely binary attribute may not represent a thresholded normal trait. In finite data a plug-in biserial estimate can even fall outside the correlation interval, indicating that it should not be treated as an unrestricted observed Pearson coefficient. Model fitting and diagnostics require further care.

The difference between natural and artificial dichotomization matters. A recorded pass/fail status might result from thresholding an examination score, but using the original numerical score, if available and appropriate, retains more information. A medical category may be defined by a policy threshold rather than a simple latent normal mechanism. State the reason for using the binary representation and avoid claiming that an adjustment recovers information without assumptions.

Group labels also affect interpretation. A positive point-biserial coefficient means the group coded one has a higher numerical mean under the displayed formula. It does not say that the label itself causes the difference. Report the means, counts, and measurement context alongside the coefficient. These quantities often explain the practical association more clearly than a standardized number alone.

## 8.7 Two binary variables, phi and the fourfold table

Two binary variables form a two-by-two or fourfold table. Define a as the count with x equal one and y equal one, b as x one and y zero, c as x zero and y one, and d as both zero. State this layout explicitly because different textbooks place the letters differently. The total count is a plus b plus c plus d. Every eligible paired observation contributes to exactly one cell.

The phi coefficient is Pearson correlation of the zero-one columns. In the stated layout, phi equals (a d minus b c) divided by the square root of (a plus b)(c plus d)(a plus c)(b plus d). Each factor is a row or column total. If a variable has only one observed category, a margin is zero and the coefficient is undefined. A zero cell alone need not make it undefined when every margin is positive.

For a equal thirty, b ten, c twenty, and d forty, the determinant a d minus b c is one thousand. The row margins are forty and sixty, and the column margins fifty and fifty. The denominator is the square root of six million, giving phi approximately 0.408248. Direct correlation of the replicated binary pairs gives the same result. This agreement verifies both the table layout and the denominator.

Reversing the coding of either variable changes phi's sign; reversing both preserves it. Its magnitude can be constrained by the marginal proportions, so a value below one may coexist with very strong available association under uneven margins. Interpret the cell proportions and margins alongside the coefficient. Standardization does not erase the mathematical consequences of the binary distributions.

Odds ratios and differences in proportions provide other descriptions of a binary table. They answer different questions and use different scales. A positive phi in the stated coding corresponds to the positive determinant direction, but phi is not numerically equal to an odds ratio. Later epidemiology and categorical-data courses develop those measures, uncertainty, and model-based interpretations. This unit focuses on the syllabus-listed observed correlation and its assumptions.

A binary association can be induced by common causes, selection, or measurement procedures. A table of disease status and exposure status is not automatically an experiment, and a coefficient does not establish exposure effects. Preserve the observational design and timing information. The arithmetic describes the recorded table; causal conclusions require an additional justified argument.

## 8.8 Tetrachoric correlation and latent-normal assumptions

Tetrachoric correlation concerns two observed binary variables assumed to arise by thresholding two underlying continuous variables with a joint bivariate normal distribution. It estimates the latent normal correlation, not the ordinary Pearson correlation of the observed binary columns. The assumptions include a defensible latent-continuous interpretation and a specified threshold model. They cannot be verified solely by noticing that the observed table has four cells.

Marginal binary proportions determine threshold estimates in the standard-normal latent representation. If x equal one represents the upper region, the lower threshold probability is the proportion with x zero; similarly for y. Given those thresholds and a trial latent correlation, the bivariate normal distribution predicts the four cell probabilities. Estimation seeks a correlation whose predicted table agrees with the observed counts under an appropriate fitting criterion.

For ordinary interior tables, fitting generally requires numerical evaluation of bivariate normal probabilities and numerical optimization or root finding. There is no general exact shortcut that converts every phi coefficient to a tetrachoric correlation independently of the margins. A teaching formula that ignores the threshold proportions should therefore be treated cautiously. Specialized software should document its likelihood method, zero-cell handling, convergence, and uncertainty procedures.

One special balanced case is instructive. If both latent thresholds are at their medians, so both observed marginal probabilities are one half, the population binary phi under the bivariate-normal model equals two divided by pi times the arcsine of the latent correlation. Inverting gives latent correlation equal to the sine of pi times phi divided by two. This relationship is exact under those population assumptions, but it is not a universal fourfold-table identity.

For an illustrative balanced model with observed population phi one half, the corresponding latent correlation is the sine of pi divided by four, approximately 0.707107. The observed binary coefficient remains one half. The difference reflects the latent model and dichotomization, not evidence that the observed calculation was inaccurate. An empirical finite table adds estimation uncertainty and possible model mismatch.

Sparse cells, extreme margins, and empty cells can make estimation unstable or push fitted correlations toward boundaries. Some procedures apply continuity corrections or restrictions, which change the fitting convention. Report those choices. A numerical estimate returned without convergence diagnostics is not automatically trustworthy. This introduction explains the model and special case; it does not present a homemade unrestricted estimator as a substitute for specialist software.

When the original continuous variables are available, an appropriate analysis of them often retains more information than a dichotomized table. Thresholding may be necessary for a practical decision, but its information loss and policy dependence should be explicit. A tetrachoric estimate attempts model-based reconstruction under assumptions; it cannot restore all details of the original measurements from four counts.

## 8.9 Correlation ratio and nonlinear group structure

The correlation ratio eta describes how much numerical variation is associated with categories or distinct groups of a predictor. Let y-bar be the overall mean, and let each group j have size nj and mean y-bar-j. The between-group sum of squares is the sum of nj times the squared difference between each group mean and the overall mean. Total sum of squares is the sum of squared individual y deviations from y-bar.

Define eta squared as between-group sum of squares divided by total sum of squares when the latter is positive. Eta is the nonnegative square root. Because total sum of squares equals within plus between components, eta squared lies between zero and one. A value zero means the group means coincide, not that every aspect of the group distributions is identical. A value one means no within-group variation remains under the chosen grouping.

For groups 1, 3 and 7, 9, the overall mean is five, within sum of squares four, and between sum of squares thirty-six. Total sum of squares forty gives eta squared 0.9 and eta approximately 0.948683. This reuses the exact decomposition from unit six and connects it to association. The grouping explains ninety percent of the recorded squared-deviation total in this descriptive sense.

The phrase explains variation is algebraic here and must not be interpreted automatically as causal explanation. Group membership may reflect confounding, selection, or another descriptive partition. The proportion also depends on the chosen grouping. Creating a separate group for each distinct observation can force zero within-group variation and eta one, even when such grouping has no useful predictive or scientific interpretation. Complexity and replication matter.

Eta is generally directional because the roles of categorical grouping and numerical response differ. It is not interchangeable with symmetric Pearson correlation. Group means can follow a curved pattern across numerical x categories even when Pearson r is near zero. Eta captures differences in conditional means under the grouping, but can miss dependence expressed only through different within-group spreads when means coincide.

For a binary grouping variable, eta squared equals the squared point-biserial correlation computed on the same eligible observations. Both use the between-group mean separation relative to total numerical variation. This identity is a useful cross-check. For more than two groups, assigning arbitrary numerical category codes and calculating Pearson correlation can depend on those codes, while eta based on group membership does not depend on their arbitrary order labels.

Later regression and analysis-of-variance courses develop conditional mean functions and inferential uses of this decomposition. Here, preserve the grouping rule and counts, report eta squared as a descriptive proportion, and avoid claims of out-of-sample prediction or causality. A high fitted proportion in the observed data may reflect detailed grouping rather than a stable relationship that generalizes.

## 8.10 Intraclass correlation and a specified measurement model

Intraclass correlation, ICC, is used for related measurements grouped by subject or another unit. Unlike ordinary Pearson correlation between two named columns, ICC compares components of variation under a specified measurement model. Several ICC forms exist because study designs and targets differ: one-way versus two-way models, random versus fixed raters, single versus averaged measurements, and consistency versus absolute agreement. The label ICC without its form is incomplete.

Consider a balanced one-way random-effects model with n subjects and k repeated measurements per subject. Write a measurement as an overall mean plus a subject-specific random effect plus residual measurement variation. Assume independent subject effects with variance sigma-a squared and independent residuals with variance sigma-e squared, under the stated model. The population single-measure ICC is sigma-a squared divided by their sum when total variance is positive.

The population ratio is nonnegative and at most one because its components are nonnegative. It describes the fraction of model variance associated with subject differences and the correlation of two measurements on the same subject under these assumptions. A large value can occur when subjects differ widely even if measurement error is practically substantial. Therefore ICC should be interpreted with the actual error scale and target population spread.

For the balanced one-way sample, calculate a between-subject mean square MSB and a within-subject mean square MSW. The conventional ICC(1,1) estimate is (MSB minus MSW) divided by (MSB plus (k minus one)MSW). Between sum of squares uses k times the squared distances of subject means from the grand mean and divides by n minus one. Within sum of squares uses each measurement's deviation from its subject mean and divides by n times k minus one, meaning n multiplied by (k minus one).

For two subjects measured as 1, 3 and 7, 9, k is two and the grand mean five. Between sum of squares is thirty-six and MSB thirty-six. Within sum of squares is four and MSW two. ICC(1,1) is thirty-four divided by thirty-eight, or seventeen nineteenth, approximately 0.894737. This is a model-based variance-component estimate, distinct from eta squared 0.9 even though both use related sums of squares.

A sample estimate can be negative when MSB is smaller than MSW. This does not mean the population variance component is literally negative under the stated model; it indicates that the unconstrained method-of-moments estimate fell below zero. Some analyses constrain estimates to a boundary. State the procedure and avoid silently truncating a negative number while claiming to report the unmodified formula.

The ICC for an average of k measurements is different from the single-measure ICC because averaging reduces residual variance under the model. The balanced one-way average-measure estimate is (MSB minus MSW) divided by MSB when the denominator is valid. It should be labelled ICC(1,k) and interpreted as reliability of that average, not of one reading. Designs with systematic rater effects require other forms and cannot use the one-way formula without justification.

## 8.11 Association, agreement and responsible interpretation

High correlation can coexist with poor agreement. If one instrument always reports twice another's value plus ten, Pearson correlation can be one while measurements differ substantially. Agreement asks whether values are sufficiently close under the intended unit and tolerance. A paired-difference plot and a specified agreement model address questions that ordinary correlation does not. Do not describe a high r alone as proof that instruments can be substituted.

Observed association also depends on measurement reliability. Random error can weaken some correlations under particular models, while shared systematic errors can strengthen apparent relations. Correcting for attenuation requires assumptions and reliable information about measurement error; it is not a routine step that every coefficient needs. The introductory analysis should describe instruments, coding, timing, and known limitations before interpreting numerical strength.

Subgroups can reveal relationships hidden or reversed in the aggregate. Simpson's paradox in unit three concerned rates, but correlations and regression can also reflect mixtures of groups. Inspect relevant strata and distinguish within-group from between-group patterns. Adding a group variable to a model may clarify a descriptive comparison, but causal adjustment requires a justified understanding of the variable's role.

An association report should specify the coefficient and version, eligible pair count, variable definitions, coding direction, missingness rule, and an appropriate plot or table. For latent coefficients, add the threshold and distributional assumptions. For ICC, name model and single or average measurement target. These details make it possible to reproduce and evaluate the result without guessing at a software default.

Inference is deliberately limited in this first descriptive book. A confidence interval or test for a coefficient relies on additional sampling and modelling assumptions, and repeated or clustered data require suitable methods. The probability, inference, sampling, and regression books in the Statistics department develop those tools. Here, we calculate and interpret observed association accurately rather than attaching unsupported certainty.

The three worked questions for this unit cover Pearson correlation with a curved counterexample, tie-aware rank association, and a binary table with phi. The explanatory sections provide additional hand-checkable examples for W, point-biserial, eta, and ICC. This structure gives the reader three focused solution cards while still covering the full range of major syllabus topics.

## 8.12 The association explorer and an audit plan

The association explorer displays a small paired dataset, a scatter plot, Pearson r, and the fitted simple-regression slope when defined. A control changes one y value while preserving its x pairing. This demonstrates that a coefficient depends on the full paired configuration and can be influenced by an observation with an extreme x position. The same updated data must feed both the graph and the numerical calculation.

At a perfectly increasing straight-line setting, verify r equal to one and the expected slope. At a reversed straight-line setting, verify r minus one. Use the symmetric quadratic example separately to verify zero Pearson correlation despite a deterministic curved relationship. These are complementary checks: a bound test alone could miss an implementation that always returns zero or always returns a positive coefficient.

The simulator should guard against constant columns and explain why correlation or slope is unavailable. Reset must restore every paired value and summary. A numerical table should accompany the graphic for accessibility and for direct calculation. The plot should scale with the data without clipping labels or hiding the changed observation beyond its drawing area.

For rank and binary coefficients, independently calculate small examples rather than trusting the Pearson simulation to validate every method. Enumerate Kendall pairs including ties, reconstruct phi from table margins, and compare point-biserial with direct zero-one Pearson correlation. Those separate checks correspond to separate definitions and catch errors that a generic correlation test cannot detect.

Before proceeding, distinguish linear from monotonic association, state the general Spearman definition with ties, classify a Kendall pair, and explain the difference between observed phi and latent tetrachoric correlation. Then name an ICC form rather than saying ICC alone. These tasks establish the assumptions and computational discipline needed for the regression and integrated investigation in the final unit.
