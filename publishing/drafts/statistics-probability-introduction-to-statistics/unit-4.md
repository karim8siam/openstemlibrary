## 4.1 Graphics are arguments built from observations

A statistical graphic translates observations into spatial or visual features. Position, length, area, color, and ordering become a language for comparison. A good graphic makes a relevant structure easier to see while preserving the meaning of the underlying measurements. A poor graphic can exaggerate a small difference, conceal a large one, or imply a relationship that the data do not support. Graphical design is therefore part of statistical reasoning.

Begin by identifying the question the graphic should answer. A bar chart can compare category frequencies, a histogram can display a quantitative distribution, and a scatterplot can display paired quantitative measurements. A line connecting successive observations can communicate a sequence, but the line implies an order that should have a substantive basis. Connecting nominal categories by a line may suggest continuity where there is none.

Choose the visual encoding according to the information. Position along a common numerical axis supports precise comparisons of magnitude. Area and color intensity are harder to compare accurately and need careful legends. A decorative three-dimensional bar can distort the visible length or area depending on perspective. The analyst should not make readers mentally correct for graphical effects before they can interpret the data.

Every graphic should identify the variable, units, population or sample, period, and denominator where appropriate. A percentage axis without a denominator can conceal whether values describe respondents, eligible units, or events. A title should summarize the subject without overstating the conclusion. “Reported waiting times in the pilot sessions” is a description; “New system eliminates waiting” is a claim requiring evidence beyond a single plot.

The graphical scale is part of the argument. A truncated axis can make a small numerical difference look large. A very wide axis can make a substantial difference look small. Neither a zero origin nor a truncated origin is universally correct for every display. The choice should preserve the intended comparison and be made visible. Bars encode magnitude through length, so their baseline is particularly important; a line plot often focuses on change and can use a narrower range with clear labeling.

Distinguish the observed data from model output. Points can show measurements, while a line shows a fitted relationship or an interpolation. The caption should identify which is which. A smooth curve drawn through a few points may be an illustrative interpolation rather than a scientifically validated law. Readers should not infer that unobserved intermediate values were measured simply because the display is continuous.

Graphics can reveal mistakes before they support scientific conclusions. A scatterplot may expose a column entered in different units for one group. A time plot may reveal that a sensor stopped recording. A histogram may show a suspicious concentration at a missing-value code. These patterns should trigger investigation of the records and collection process, not immediate substantive explanations. Exploratory graphics are tools for asking better questions.

The amount of data shown should fit the purpose. With a small dataset, displaying individual points often reveals more than a summary alone. With a very large dataset, overlapping points can hide density, making transparency, aggregation, or density displays useful. Each solution introduces choices that should remain understandable. A plot should simplify the visual task without concealing how observations were combined.

Finally, a graphic should be readable without relying solely on color. Labels, shapes, line styles, and annotations can distinguish groups for readers with different visual abilities and for printed copies. Provide a textual explanation of the principal pattern and, when practical, the numerical data behind the graphic. Accessibility improves statistical interpretation because it forces the display's meaning to be stated clearly.

## 4.2 Bar charts, proportions, and compositional displays

A bar chart represents category values using rectangles whose lengths correspond to numerical quantities. The category positions are separate, and the spaces between bars signal that the horizontal axis is not a continuous measurement scale. Bars can show counts, percentages, or other category summaries, but the axis label must identify which. A bar chart of mean waiting time by laboratory is different from a bar chart of the number of visits to each laboratory.

For count or percentage bars, a zero baseline makes length proportional to magnitude. If bars begin at eighty percent, a comparison of 82 and 84 percent can appear much larger than a two-percentage-point difference. A broken axis may be necessary in an unusual setting, but it should be conspicuous and should not invite a misleading length comparison. The numerical values should be available to confirm the scale.

Category order influences interpretation. Sorting nominal categories by frequency highlights the most common categories. Alphabetical ordering can make lookup easier. Ordinal categories should generally retain their natural order. A horizontal bar chart can accommodate long category labels without rotating text into an awkward angle. Choose the order and orientation for the reader's task rather than for a decorative effect.

Grouped bars compare several groups within each category. They work best when the number of groups is modest and the grouping is visually clear. Stacked bars emphasize composition within a total, but segments that do not share a common baseline are harder to compare precisely. A 100-percent stacked bar removes total-size differences and compares composition. That can be useful, but the sample sizes should still be shown elsewhere.

Pie charts encode parts of a whole through angles and areas. They require categories that form a meaningful partition of a common total. A multiple-response question whose percentages sum above 100 does not fit that structure. Pie charts are often less suitable when categories have similar proportions or when many small categories need comparison. A bar chart can make such differences clearer without changing the data.

If a pie chart is used, avoid three-dimensional perspective, exploded slices that alter the apparent geometry, and ambiguous legends. Label the categories and percentages directly when possible. A small slice should not be omitted merely because it is difficult to label. Combining minor categories into “other” should be disclosed, especially if that combination conceals substantively different groups.

Compositional comparisons should retain their denominator. A rise in the share of one category can occur because its count increased or because another category's count decreased. Percentages alone do not distinguish those mechanisms. For example, the proportion of digital loans can rise even if digital loans remain constant while print loans decline. Showing both counts and shares can clarify whether the comparison concerns volume or composition.

An apparently empty bar may represent zero observations, missing data, or a suppressed value. These should have distinct labels or symbols. A graph showing a zero-height bar for an unmeasured category falsely implies a measured absence. The same caution applies to percentages based on no observations. Undefined quantities should be marked as unavailable rather than visually converted to zero.

Before interpreting a bar display, check that the categories are comparable, the denominator is stable, the baseline is appropriate, and the totals reconcile with the table. A visually polished chart can still be based on a wrong denominator or an inconsistent classification. Graphical accuracy begins with tabular accuracy and then adds careful encoding.

## 4.3 Histograms, density, and the visual structure of a distribution

A histogram displays the distribution of a quantitative variable across numerical intervals. Adjacent rectangles correspond to adjacent intervals, and their areas represent counts or proportions under the stated normalization. Unlike a bar chart of nominal categories, the horizontal positions have numerical meaning. A gap indicates an interval with no observations, not simply spacing inserted for readability.

The distribution's shape can include concentration, asymmetry, multiple clusters, gaps, and a long tail. These features should be described cautiously, especially with small samples. A histogram's appearance depends on bin width and origin. A narrow width can make random fluctuations look like many peaks, while a broad width can conceal distinct groups. Inspect several reasonable choices before claiming that the population has a particular number of modes.

Frequency-density scaling is required for unequal widths if area is to remain proportional to frequency. The previous unit derived the rule. Here the graphical interpretation is the focus: a wide bin can contain many observations while showing a lower density height than a narrow bin. Saying that “the tallest bar contains the most observations” is therefore incorrect for a density histogram with unequal widths. Read the area or the accompanying count labels.

A density histogram approximates a distribution through piecewise-constant heights. It should not be interpreted as an exact population probability density. Its construction summarizes the sample and depends on arbitrary intervals. With more observations and suitable bin choices, it can provide a useful visual estimate, but finite-sample noise remains. A smooth density estimate introduces further choices about smoothing that should be documented.

Symmetry means that the distribution's structure is approximately balanced around a center under a reflected comparison. A symmetric histogram can arise from an asymmetric population by chance, and an asymmetric histogram can arise from a symmetric population in a small sample. Shape descriptions should therefore refer first to the observed data. If a model is proposed, its adequacy should be assessed with additional reasoning and diagnostics.

Skewness in ordinary graphical language describes an extended tail in one direction. A right-skewed distribution has a comparatively long right tail. This does not mean that most observations are on the right side; often most values lie at the lower end with a few large values extending the tail. Later units distinguish this visual description from numerical skewness coefficients, which need not agree perfectly with every intuitive shape judgment.

Multiple clusters can suggest mixed groups, measurement conventions, or genuine structure within one population. A histogram of study duration might show one cluster for weekdays and another for weekends. The pooled display alone cannot identify the mechanism. If a relevant group label is available, compare distributions by that label. The aim is to explain the observed structure through the data-generating process rather than merely name its appearance.

Histograms also reveal digit preference and rounding. A concentration at multiples of five in recalled durations may reflect the reporting process rather than actual behavior. A narrow-bin display can expose this pattern, while a broad-bin display can hide it. Recording precision and recall rules should be consulted before interpreting the clusters as distinct biological or social processes.

The caption should specify the bin convention, normalization, variable units, usable sample size, and important exclusions. When a particular bin choice is central to a conclusion, show that reasonable alternatives produce a similar interpretation. This practice makes a graphical claim less dependent on an invisible formatting decision.

## 4.4 Dot plots and stem-and-leaf displays preserve individual values

A dot plot places an individual mark for each observation along a quantitative axis. Repeated values can be stacked so that their multiplicity remains visible. It is particularly useful for small and medium datasets where each observation can be inspected. Unlike a histogram, it need not group values into broad intervals. The reader can see clusters, gaps, and unusual values while retaining much of the original numerical information.

For a small sample of waiting times, a dot plot can show whether a reported mean is influenced by one long delay or represents the general pattern. It can also show ties caused by rounding. A jittered plot spreads overlapping points slightly for visibility, but the jitter should not be mistaken for measured variation. The axis or caption should make clear that the horizontal or vertical displacement is a display device.

A stem-and-leaf display separates each value into a stem and a leaf. For integer values such as 12, 14, 17, and 23, one convention uses tens as stems and units as leaves: the stem one has leaves two, four, and seven, while stem two has leaf three. A key such as “1 | 2 means 12 minutes” is essential. Without it, the same display can be interpreted at several different scales.

Stems should appear in numerical order, including empty stems when their absence would conceal a gap. Leaves should usually be sorted within each stem. Repeated leaves should be retained because they represent repeated observations. A stem-and-leaf display is not a list of distinct values; removing duplicates would erase frequency information. Negative values and decimal precision require a clearly stated convention.

Splitting stems can increase detail. One split can use leaves zero through four and another five through nine for each stem. This reduces crowding when many values share a tens digit. The split should be consistent across stems. Irregular splitting can make comparisons misleading by assigning different numerical ranges to visually similar rows. If the display becomes too complicated, a dot plot or histogram may be clearer.

Back-to-back stem-and-leaf displays can compare two groups using shared stems and leaves extending in opposite directions. They retain individual values while making differences in concentration visible. The groups should use the same numerical units and precision. If group sizes differ greatly, the longer side may mainly reflect more observations rather than a different distribution, so sample sizes and normalized summaries should accompany the display.

Stem-and-leaf displays have limits. They can be cumbersome for very large datasets or measurements with many relevant decimal places. They can also reveal individual values in privacy-sensitive data. In such settings, grouped graphics may be more suitable. The choice should balance numerical detail, readability, and the conditions under which data may be disclosed.

The important principle is to avoid unnecessary data reduction. If twelve observations can be displayed individually, replacing them by a smooth curve may imply more information than is available. If ten thousand observations overlap beyond readability, some aggregation is sensible. The visual representation should match the resolution and size of the evidence.

An analyst should be able to move between a raw list, a sorted list, a dot plot, a stem-and-leaf display, and a frequency table, explaining what each retains or discards. This skill makes it easier to diagnose discrepancies. If a graphic shows eleven points while the usable data contain twelve records, the mismatch should be resolved before any interpretation is written.

## 4.5 Quartiles and the five-number summary require a convention

The five-number summary consists of a minimum, a lower quartile, a median, an upper quartile, and a maximum. It provides a compact description of location and range. The median is a central ordered value, while quartiles mark positions around the lower and upper quarters. For finite samples, different legitimate interpolation and splitting conventions can give different quartiles. A report should specify its convention when numerical reproducibility matters.

Throughout this book's interactive calculations, the default numerical quantile convention is linear interpolation with index $h=1+(n-1)p$ for sorted data and probability $p$. If $h$ is an integer, use that ordered observation. Otherwise, interpolate between the observations at the integer positions surrounding $h$. This is often called the type-seven convention. It is a chosen finite-sample rule, not the only mathematical definition of a sample percentile.

For sorted values one through eight, the lower quartile has index $1+7(0.25)=2.75$, giving 2.75 by interpolation between two and three. The median has index 4.5, giving 4.5. The upper quartile has index 6.25, giving 6.25. A median-of-halves convention instead gives lower and upper quartiles of 2.5 and 6.5. Neither discrepancy is an arithmetic error if each convention is correctly implemented and clearly identified.

For an odd sample size, median-of-halves methods also differ in whether the overall median is included in each half. With values one through nine, an excluding-median split uses the lower four and upper four values, yielding quartiles 2.5 and 7.5. Including the median in both halves yields three and seven. The type-seven interpolation convention also yields three and seven for this particular sample. Agreement in one sample does not make the conventions identical in general.

The empirical distribution function supplies another quantile definition: choose the smallest observed value whose cumulative proportion reaches the desired probability. This inverse-step-function definition returns observed values rather than interpolated intermediate values. It is particularly natural when the variable is categorical or discrete. It should not be confused with the continuous interpolation rule used for some numerical displays in this book.

Quantiles for ordinal categories should respect category meaning. If the median lies between “fair” and “good,” an interpolated numerical code may not correspond to any interpretable category. Report the middle category or category interval under a stated rule. For quantitative measurements, interpolation can be a useful convention, but it still does not mean that an unobserved value was measured.

Missing values must be handled before ordering. If they are excluded, state the resulting sample size. Sorting a missing-value code such as 999 as though it were a real measurement can change the maximum and upper quantiles dramatically. Ties should remain in the ordered list because they affect positions and cumulative proportions. Quantile calculations operate on observations, not only distinct values.

Small samples have coarse information about tail positions. An interpolated 95th percentile from ten values can be numerically precise while being highly dependent on the two largest observations. That number should not be presented as a stable population threshold without inferential support. The distinction between a sample quantile and a population quantile parallels the distinction between a sample mean and a population mean.

The five-number summary is valuable because it combines central and extreme information, but it does not reconstruct the full distribution. Different datasets can share all five values while differing substantially within the quartile intervals. Use it together with a graph or raw-value display when those differences matter. Numerical compactness should not be mistaken for complete description.

## 4.6 Box plots, fences, whiskers, and unusual observations

A box plot uses a box from the lower to the upper quartile, with a line marking the median. Its basic interpretation depends on the quartile convention already discussed. A common modified box plot adds fences at $Q_1-1.5\operatorname{IQR}$ and $Q_3+1.5\operatorname{IQR}$, where the interquartile range is $Q_3-Q_1$. Observations beyond the fences are displayed individually. Whiskers extend to the most extreme observed values inside the fences, not necessarily to the fence locations themselves.

This distinction between fences and whiskers is essential. A fence is a calculated threshold. A whisker endpoint is an observed value selected by that threshold rule. If the upper fence is 11.5 but the largest observation inside it is seven, the upper whisker ends at seven. Drawing the whisker to 11.5 would imply a convention different from the usual modified box plot. Some software uses other rules, so the plotting definition should be documented.

For the values 1, 2, 3, 4, 5, 6, 7, and 30 under the type-seven convention, the quartiles are 2.75 and 6.25, with median 4.5. The interquartile range is 3.5. The fences are minus 2.5 and 11.5. The whiskers end at one and seven, while thirty is plotted separately. The minimum and maximum of the dataset remain one and thirty even though the whisker endpoints are different.

A flagged observation is unusual under the plotting rule. It is not automatically an error or an observation that should be removed. Waiting thirty minutes may be a genuine equipment failure or a legitimate rare delay. Removing it could make the display smoother while concealing the experience the study intends to describe. The box plot is a diagnostic invitation to investigate, not a deletion command.

The 1.5 multiplier is a convention that balances sensitivity and readability in many exploratory settings. It is not a universal scientific boundary between valid and invalid data. A naturally skewed distribution can produce many flagged values on one side. A small sample can make quartiles unstable. If a threshold is used for a consequential decision, its relevance should be justified independently of the graphical convention.

Box plots make group comparisons compact. Placing several boxes on a common scale can reveal differences in median, central spread, and flagged observations. However, equal box widths can conceal different sample sizes, and the plot can conceal multimodality within groups. Add sample sizes and consider overlaying individual points or a distribution display when the amount of data permits. A box plot alone is not a complete account of shape.

Notched box plots use an additional convention intended to communicate uncertainty about a median under particular approximations. They should not be interpreted as exact confidence statements without understanding the implementation and assumptions. This introductory book uses ordinary boxes without inferential notches so that the distinction between descriptive shape and inferential uncertainty remains clear. More elaborate graphics require more explicit explanation, not less.

When all values are identical, the interquartile range is zero and the box collapses. This is not necessarily a plotting error. In some datasets, a zero interquartile range can coexist with distinct extreme values because most observations are tied. The fence rule can then flag every value outside the common central value. Explain that behavior rather than treating the output as a universal classification of errors.

The box-plot explorer displays the sorted data, interpolation positions, quartiles, fences, whiskers, and flagged values together. Changing one observation shows which summaries move and which remain unchanged. The learner should predict the effect before moving the control. This makes the rank-based nature of quartiles visible and demonstrates why a central summary can remain stable while a tail observation changes dramatically.

## 4.7 Scatterplots and the visual language of association

A scatterplot represents paired measurements as points $(x_i,y_i)$. The pairing is part of the data: both coordinates must belong to the same unit or occasion under the intended design. A list of heights and a separately sorted list of weights cannot be paired after sorting to create a meaningful relationship. Sorting one variable independently destroys the original joint information even though each marginal distribution remains unchanged.

The horizontal and vertical roles should follow the question. A predictor or explanatory measurement is often placed horizontally, while a response is placed vertically. For a purely descriptive comparison, the choice can be conventional. Either way, labels and units are necessary. A slope depends on which variable is vertical and on the measurement units, whereas a standardized correlation has different transformation properties discussed later.

Read several features: direction, form, strength, unusual points, and group structure. Direction describes whether larger horizontal values tend to accompany larger or smaller vertical values. Form describes whether the pattern is approximately linear, curved, segmented, or otherwise structured. Strength concerns how concentrated points are around the relevant form, not merely whether a numerical correlation is large. A strong curved relationship can have a small Pearson correlation.

A symmetric U-shaped pattern illustrates this limitation. If negative and positive horizontal values have similarly large vertical values and values near zero have small vertical values, the linear tendency can cancel. A scatterplot reveals the pattern directly. Reporting only a correlation near zero would conceal it. “No linear association detected in this summary” is therefore different from “no relationship.”

Unusual points can have different roles. A point far from the center of the horizontal values can strongly influence a fitted line. A point with an unusual vertical value relative to nearby horizontal values can have a large residual. These are not identical properties. An observation can have an ordinary residual while exerting considerable leverage on the slope. The regression unit examines these distinctions mathematically.

Group labels can reveal pooled patterns that differ from within-group patterns. Two groups can each have a negative relationship while their combined centers produce a positive overall trend. This resembles the aggregation mechanisms discussed in the previous unit. Color or shape can help show groups, but the legend should remain readable and categories should not be invented solely to make a preferred pattern appear.

Overplotting occurs when multiple observations occupy the same or nearby coordinates. A dense region can appear to contain only a few points because marks overlap. Transparency, small markers, jitter for discrete variables, or count-based displays can help. Jitter should be documented because it changes displayed coordinates slightly. A count annotation can preserve exact repeated positions without suggesting unobserved numerical differences.

Axis choices affect the apparent angle of a line and the visual impression of variation. Rescaling an axis changes the shape of the plotted cloud on the screen even though the numerical correlation is unchanged under a positive linear unit conversion. Readers should use labels and numerical summaries rather than infer a physical relationship from a line's visual angle alone. An aspect ratio is a display choice, not a scientific parameter.

A scatterplot supports exploration, but causal interpretation still requires design and subject knowledge. Time ordering, confounders, selection, measurement error, and feedback can all influence the pattern. The graph's value is that it shows the joint observations transparently and helps identify which explanations deserve investigation. It should not be used as a shortcut around those explanations.

## 4.8 Time plots, ordered data, and changing conditions

A time plot places observations in temporal order and can reveal trends, cycles, abrupt changes, and persistent fluctuations. The order contains information that a histogram discards. Two datasets can have identical values and therefore identical histograms while having very different time sequences. One may alternate between high and low values, while another rises steadily. The appropriate display depends on whether sequence is relevant to the question.

Use a numerical time axis with spacing that reflects actual elapsed time. If measurements occurred on days one, two, and twenty, equally spaced category positions can hide the long gap between the second and third observation. A line connecting the points can suggest continuity during the unobserved period. Mark gaps or show points without connecting them when interpolation would imply unsupported observations.

Changes in collection can mimic changes in the phenomenon. A sensor replacement, a revised questionnaire, or a shift from morning to evening observations can create a sudden level change. Annotate known measurement changes and inspect comparability before explaining the jump as a real trend. A well-labelled time plot can serve as a timeline of both observations and collection conditions.

Counts over unequal observation periods require exposure information. Ten failures over ten operating hours and ten failures over one hundred operating hours represent different rates. A time plot of counts can increase when operating time increases even if reliability per hour remains unchanged. Plotting rates may answer the intended question, but the underlying counts and exposures should be available because a rate based on little exposure can be unstable.

Smoothing can make a trend easier to inspect but can also conceal short-lived events or shift apparent timing. A moving average combines neighboring observations according to a chosen window. The window length and whether it is centered or trailing affect interpretation. A trailing average uses earlier values and can lag a changing process. A centered average uses later observations and is unsuitable for pretending to predict events in real time.

Seasonal patterns involve recurring changes associated with a cycle, such as day of week or semester stage. An overall trend should not be inferred by comparing a busy period with a quiet period without considering the cycle. Plotting comparable periods or adding relevant groupings can clarify the pattern. This book introduces the descriptive issue; a later Time Series Modeling book develops formal methods for dependence and forecasting.

Consecutive observations can share influences, so visual persistence does not provide the same evidence as many independent replications. A run of high sensor readings can reflect one prolonged environmental event. The plot should help identify that dependence rather than encourage treating every second as a separate independent experiment. Sampling frequency and process timescale should both be considered.

Dual-axis time plots can make unrelated series appear to track one another by choosing convenient scales. If two vertical axes are necessary, label both clearly and avoid treating visual overlap as evidence of a quantitative association. A standardized display or separate aligned panels can be easier to interpret. The relevant numerical relationship should be analyzed directly rather than inferred from adjustable graphical scales.

The main questions for a time plot are what changed, when it changed, whether the observation process also changed, and whether the pattern repeats under comparable conditions. These questions keep descriptive exploration connected to the data-generating process. A dramatic line is a starting point for investigation, not a complete explanation of the event it appears to describe.

## 4.9 Cumulative plots, quantile comparisons, and distributional evidence

A cumulative plot shows the fraction of observations at or below a sequence of thresholds. For exact data, the empirical distribution function is a step function. It starts at zero below the minimum and reaches one at or above the maximum. Its jumps reflect observed frequencies. Unlike a histogram, it does not require a bin-width choice, though its appearance still depends on axis scale and how ties are displayed.

A steep portion indicates that many observations lie in a narrow numerical interval. A flat portion indicates a gap without observations. This interpretation follows directly from cumulative counting. If the curve reaches 0.8 at ten minutes, eighty percent of usable observed durations are at most ten minutes under the stated definition. The plot should not convert that sample statement into a population guarantee without additional inference.

Comparing two cumulative curves can reveal differences across the distribution. If one curve is consistently higher at every threshold, it indicates that its observations are concentrated at lower values in a descriptive ordering sense. If the curves cross, one group may have lower values in one region and higher values in another. A single mean or median can miss that crossing pattern. The relevant decision may concern a particular threshold rather than the entire distribution.

A quantile-quantile plot compares ordered positions from two distributions or compares observed quantiles with a specified reference model. Points near a straight line suggest that the distributions are related approximately by a location and scale transformation over the displayed range. Departures can indicate different tail behavior, skewness, or other structure. The reference and plotting positions should be identified so the reader knows what is being compared.

For a theoretical reference, the model introduces assumptions beyond the empirical data. A roughly straight normal-reference plot is evidence of approximate compatibility, not proof that the population is exactly normal. Small samples may not reveal tail differences, while large samples can make minor deviations visually apparent. The purpose of the model and sensitivity of the intended analysis should guide how important those deviations are.

When comparing two empirical samples of different sizes, quantile interpolation is needed to match common probability positions. The chosen convention should be stated. An apparent tail difference based on one extreme point in a small sample should be described cautiously. Displaying the sample sizes and original ranges helps the reader assess how much evidence supports the tail comparison.

Distribution comparisons should retain units and group definitions. If one sample measures duration in seconds and another in minutes, a straight comparison line with a slope of sixty can reflect unit conversion rather than a scientific difference. If groups were selected by different rules, distributional differences may reflect coverage or composition. A graphical match cannot establish equivalent sampling processes, and a graphical mismatch cannot identify its cause by itself.

Cumulative and quantile displays complement histograms and box plots. Histograms emphasize local concentration, box plots emphasize quartile structure and flagged observations, and cumulative plots emphasize threshold proportions. Quantile comparisons emphasize differences in location, scale, and shape relative to another distribution. Choosing several complementary displays can reveal a structure that no single summary captures, provided the report remains focused on its question.

The practical rule is to explain what each visual feature encodes and which assumptions create it. A curve, box, or diagonal line should not be treated as a familiar symbol with a universal interpretation. The reader should be able to connect the display back to counts, ordered values, and a specified comparison. That connection is what makes graphical evidence reproducible.

## 4.10 An exploratory workflow and a transparent box-plot simulation

Exploratory data analysis is a systematic search for structure, errors, and plausible questions. It starts with the data dictionary and collection log, then uses summaries and graphics to understand the observed records. It should not be confused with searching for whichever display supports a predetermined story. The analyst's job is to explain surprising patterns as well as expected ones and to preserve the distinction between exploration and confirmation.

Begin with record counts and missingness. Check the number of usable observations for each plot. Examine a sorted list or a raw-value display when feasible. Look for impossible values, suspicious codes, duplicated records, and evidence of mixed units. Correct verified errors through an audit trail. Retain unexplained unusual values with appropriate flags rather than removing them because they complicate a graphic.

Next inspect distribution, group structure, and sequence. A histogram or dot plot reveals marginal shape. A box plot compares central structure across groups. A scatterplot reveals paired relationships. A time plot reveals order. The choice should be driven by the variables and question. A collection of every available chart can overwhelm readers while failing to identify the relevant evidence.

Write an observation before an explanation. “The afternoon observations have a wider spread” describes a pattern. “The afternoon operator is less careful” is a possible explanation that needs supporting evidence. Other explanations include different instruments, different tasks, greater workload, or a changed measurement rule. Listing plausible alternatives can guide further data collection and prevent a descriptive plot from becoming an unsupported accusation.

The box-plot simulation uses eight artificial values and the displayed type-seven quantile rule. One control changes a high observation while the remaining values stay fixed. The display recalculates the median, quartiles, interquartile range, fences, whiskers, and any flagged point. It also shows the mean so that the reader can compare a rank-based central summary with an arithmetic one under the same change.

At the initial setting, calculate the summaries directly from the sorted list. Check that the displayed box endpoints agree with the stated interpolation positions. Check that whiskers end at actual observations inside the fences. Then move the high-value control and predict which quantities will change. The median can remain unchanged while the mean and range increase, illustrating different sensitivity rather than superiority of one summary for all questions.

The simulator does not decide whether a flagged value is an error. Its flag follows a mathematical convention. A real outlier investigation would require the source record, eligibility rules, instrument information, and scientific context. The display is intentionally limited to descriptive behavior so that learners do not mistake an automated label for a completed investigation.

Audit reset, small-screen layout, and invalid inputs as well as numerical results. The sorted-data table should remain readable, the chart should scale without hiding labels, and the textual summary should carry the same information as the drawing. An accessible numeric summary is especially important because a learner may read the book without perceiving every graphical feature. The simulation's educational content should not depend solely on color or motion.

This unit's worked questions focus on quartile conventions, box-plot fences and whiskers, and selecting an appropriate display for a paired dataset. They connect graphical choices to actual arithmetic and variable definitions. A correct graph is one whose visual encoding and verbal interpretation agree with the data. That standard will also guide the numerical summaries and association measures developed in the following units.
