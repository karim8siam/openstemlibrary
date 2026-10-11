"""Assemble original saved unit drafts and explicit worked solutions into COURSE_DATA."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / 'publishing/drafts/statistics-probability-introduction-to-statistics'
problems = [[] for _ in range(9)]

def problem(unit, title, question, steps, expected, difficulty='intermediate'):
    number = len(problems[unit-1])+1
    problems[unit-1].append(dict(id=f'stat-{unit}-{number}', title=title, question=question,
        difficulty=difficulty, steps=[dict(stepName=name, explanation=explanation, **({'math':math} if math else {}))
        for name, explanation, math in steps], expected_values=expected))

problem(1,'A complete finite population and all samples',
    'A finite population consists of the four values 1, 2, 3, and 4. Calculate its mean. List every unordered sample of two distinct units, calculate each sample mean, and average those six means. Explain what this exact enumeration shows and what it does not establish for an arbitrary sampling process.',[
    ('Define the target','The population contains four equally weighted units. Its total is ten, so its mean is 2.5. An unordered sample without replacement cannot repeat a unit and treats the pair in either order as the same sample.',r'\mu=(1+2+3+4)/4=2.5'),
    ('Enumerate rather than simulate','The six pairs are (1,2), (1,3), (1,4), (2,3), (2,4), and (3,4). Their means are 1.5, 2, 2.5, 2.5, 3, and 3.5. Their sum is fifteen and their equally weighted average is 2.5.',r'\overline{\bar x}=15/6=2.5'),
    ('Interpret the design','If each of those six samples is equally likely, the sampling average of the sample mean equals the finite-population mean. One realised sample can still differ from 2.5. Unequal selection probabilities or volunteer selection do not inherit this conclusion without examining their actual design. Enumeration verifies a property of this specific equal-probability mechanism.',None)],{'population_mean':2.5,'sample_count':6,'average_sample_mean':2.5})

problem(1,'A volunteer response is not a census',
    'A university has 1,000 eligible students. One hundred voluntarily answer a satisfaction form, and ninety report satisfaction. Calculate the observed proportion and response rate. Evaluate the claim that 90 percent of all eligible students are satisfied. Give a defensible description of the result.',[
    ('Calculate the recorded proportion','Among the one hundred respondents, ninety have the attribute. The observed respondent proportion is 0.90. The response rate is one hundred divided by one thousand, or 0.10. These denominators refer to different questions.',r'\hat p_{\rm respondents}=90/100=0.90;\quad r=100/1000=0.10'),
    ('Identify the missing evidence','Nine hundred eligible students did not respond. Voluntary participation may be related to satisfaction, so the recorded subset is not automatically representative. The counts alone do not tell us how many nonrespondents are satisfied.',None),
    ('Report the scope','A defensible statement is that ninety percent of the one hundred voluntary respondents reported satisfaction, with a ten-percent response rate among eligible students. A statement about all students requires additional evidence or justified assumptions. More precise arithmetic cannot remove the selection limitation.',None)],{'observed_proportion':.9,'response_rate':.1})

problem(1,'Checking a centred calculation',
    'For the waiting times 2, 4, 4, 7, and 13 minutes, calculate the total, mean, and signed deviations from the mean. Verify their sum and explain why their average is unsuitable as a measure of variation.',[
    ('Find the centre','The five observations total thirty minutes, so their equally weighted arithmetic mean is six minutes. This is the recorded-data mean; it does not require any inference about a broader population.',r'\bar x=30/5=6'),
    ('Check cancellation','Subtracting six gives deviations -4, -2, -2, 1, and 7. Their sum is zero, as required by the arithmetic-mean identity. The deviations retain minutes as their unit.',r'\sum_i(x_i-\bar x)=-4-2-2+1+7=0'),
    ('Interpret the failed spread measure','The signed average is zero despite the eleven-minute observed range. Positive and negative distances cancel. Absolute or squared deviations avoid that cancellation and are developed in the variation unit. Zero signed average is an algebraic check, not evidence of zero spread.',None)],{'total':30,'mean':6,'sum_deviations':0,'range':11})

problem(2,'Binary coding versus arbitrary labels',
    'Five observed responses are yes, no, yes, yes, and no. Code yes as one and no as zero and calculate the mean. Then consider coding yes as seven and no as two. Calculate that code mean and explain which quantity directly reports the yes proportion.',[
    ('Use an indicator','The zero-one entries are 1, 0, 1, 1, and 0. Their sum counts yes responses exactly, so the mean is three fifths. A binary indicator is a deliberate coding with a useful proportional interpretation.',r'\bar I=3/5=0.6'),
    ('Calculate the alternate coding','The alternate numbers are 7, 2, 7, 7, and 2, totaling twenty-five. Their code mean is five. The transformation is two plus five times the indicator, which explains the relationship between the two averages.',r'\bar c=2+5\bar I=5'),
    ('Preserve meaning','The proportion yes is sixty percent. The number five is an average of chosen labels, not a sixty-percent proportion or a new response category. If the coding rule is known, the indicator proportion can be recovered, but arbitrary nominal codes should not be interpreted as measured magnitudes.',None)],{'indicator_mean':.6,'alternate_code_mean':5})

problem(2,'Bounds with missing binary responses',
    'There are 100 eligible records, of which 80 have an observed binary response. Twenty-four of the observed responses are positive. Calculate the observed-only positive proportion and the lowest and highest possible complete-data proportions without assumptions about the twenty missing responses.',[
    ('Use the observed denominator','Among observed responses, the positive proportion is twenty-four divided by eighty, or thirty percent. This is not automatically the proportion among all one hundred eligible records.',r'p_{\rm observed}=24/80=0.30'),
    ('Construct worst-case completions','If all twenty missing responses are negative, there are twenty-four positives among one hundred. If all are positive, there are forty-four. No narrower complete-data interval follows from these counts alone.',r'24/100\le p_{\rm complete}\le44/100'),
    ('Explain the distinction','The complete-data proportion is bounded from twenty-four to forty-four percent, while the observed subset gives thirty percent. Additional assumptions about missingness could justify a narrower estimate, but they must be named and supported. Treating missing as negative without justification chooses the lower endpoint rather than discovering the answer.',None)],{'observed_proportion':.3,'lower_bound':.24,'upper_bound':.44})

problem(2,'A sentinel and a genuine zero',
    'A waiting-time export contains 0, 15, 20, 25, and 999. The dictionary states that 999 denotes missing and zero is a genuine immediate-service wait. Find the raw code mean and the correct observed-data mean. Explain the effect of also discarding the genuine zero.',[
    ('Expose the invalid raw calculation','Adding all five exported numbers gives 1,059 and a code mean of 211.8. This averages a sentinel with measured minutes and has no valid waiting-time interpretation.',r'1059/5=211.8'),
    ('Apply the dictionary','Exclude the single missing sentinel, retain the genuine zero, and average the four observed waits. Their total is sixty, giving fifteen minutes. Report four observed and one missing record.',r'\bar x_{\rm observed}=(0+15+20+25)/4=15'),
    ('Audit the extra exclusion','Removing zero as well leaves three positive waits with mean twenty. That describes a selected positive-wait subset and incorrectly changes the intended observed-data target if zero is eligible. The dictionary and eligibility rule determine treatment, not a preference for a more ordinary-looking number.',None)],{'raw_code_mean':211.8,'observed_mean':15,'positive_only_mean':20})

problem(3,'Unequal-width histogram bins',
    'Eight observations occupy a bin of width ten and twelve occupy a bin of width twenty. Determine count-density heights and relative-frequency-density heights. Verify the areas and explain why using raw counts as heights misrepresents the data.',[
    ('Calculate density heights','Count density is count divided by width. Heights are 0.8 and 0.6 observations per unit. The narrower class is taller although its count is smaller, because its observations are concentrated in less horizontal width.',r'h_1=8/10=0.8;\quad h_2=12/20=0.6'),
    ('Verify area and relative scale','The areas are height times width, eight and twelve, recovering counts. Dividing heights by the total twenty gives 0.04 and 0.03 per unit; their areas are 0.4 and 0.6 and sum to one.',r'0.04(10)+0.03(20)=1'),
    ('Reject the misleading encoding','Raw heights eight and twelve would produce areas eighty and two hundred and forty, a one-to-three ratio instead of the observed two-to-three ratio. For unequal widths, histogram area must encode frequency, so a density vertical scale is necessary.',None)],{'count_density_1':.8,'count_density_2':.6,'relative_density_1':.04,'relative_density_2':.03})

problem(3,'Three denominators in one table',
    'Of 40 bus users, 10 arrive late. Of 60 walkers, 6 arrive late. Calculate the proportion late among bus users, the proportion both bus and late among all 100 people, and the proportion bus among the 16 late arrivals. Explain why the answers differ.',[
    ('Condition on bus use','The relevant eligible subset has forty people, ten late. Thus lateness among bus users is one quarter. This is a within-row conditional proportion.',r'P_{\rm recorded}(L\mid B)=10/40=0.25'),
    ('Use the full-table denominator','The joint cell bus and late contains ten of the one hundred recorded people, so its full-table proportion is one tenth. A joint proportion is not the same as a within-bus rate.',r'P_{\rm recorded}(L\cap B)=10/100=0.10'),
    ('Reverse the condition','Sixteen people are late and ten of them are bus users, giving 0.625. This describes travel mode among late people, not lateness among bus users. The three questions share a numerator but have denominators forty, one hundred, and sixteen.',r'P_{\rm recorded}(B\mid L)=10/16=0.625')],{'late_given_bus':.25,'joint_bus_late':.1,'bus_given_late':.625})

problem(3,'A composition reversal',
    'In an easy stratum, option A succeeds in 90 of 100 cases and B in 19 of 20. In a hard stratum, A succeeds in 1 of 10 and B in 20 of 100. Compare each stratum, the aggregate rates, and rates standardized to equal stratum weights. Interpret the reversal descriptively.',[
    ('Compare like strata','In the easy stratum the rates are 0.90 for A and 0.95 for B; in the hard stratum they are 0.10 and 0.20. B has the larger recorded success rate in both strata.',None),
    ('Aggregate with actual counts','A has ninety-one successes in one hundred and ten cases, approximately 0.827273. B has thirty-nine in one hundred and twenty, or 0.325. A appears better overall because its cases are heavily concentrated in the easy stratum while B has many hard cases.',r'p_A=91/110;\quad p_B=39/120'),
    ('Use a common composition','Equal easy and hard weights give A a standardized rate 0.50 and B 0.575. This removes the particular composition difference from that descriptive comparison. It does not establish causal superiority, because case allocation and other factors still require a justified design.',r'p_{A,*}=0.5(0.90)+0.5(0.10)=0.50;\quad p_{B,*}=0.575')],{'aggregate_A':91/110,'aggregate_B':.325,'standardized_A':.5,'standardized_B':.575})

problem(4,'Quartiles that declare their rule',
    'Calculate the median and quartiles for sorted values 1 through 8 using type-seven interpolation. Compare the first and third quartiles with the median-of-halves convention and explain the difference.',[
    ('Find interpolation positions','With n equal eight, type-seven positions are one plus seven p. At p equal 0.25, 0.5, and 0.75, these are 2.75, 4.5, and 6.25. Positions are one-based in the sorted list.',r'h=1+(8-1)p'),
    ('Interpolate between neighbours','The values happen to equal their integer positions, so the interpolated quartiles are 2.75, 4.5, and 6.25. The IQR is 3.5. For a general list, use actual neighbouring values rather than assuming the position is itself the quantile.',r'Q_1=2.75;\quad Q_2=4.5;\quad Q_3=6.25'),
    ('Compare conventions','The lower half 1,2,3,4 has median 2.5 and the upper half 5,6,7,8 has median 6.5. Those are valid under that different convention. Reproducibility requires stating the method, not declaring one answer a rounding mistake.',None)],{'q1':2.75,'median':4.5,'q3':6.25,'iqr':3.5,'halves_q1':2.5,'halves_q3':6.5})

problem(4,'Fences are not deletion orders',
    'For 1, 2, 3, 4, 5, 6, 7, and 30, use type-seven quartiles to find the IQR, 1.5-IQR fences, and whisker endpoints. Identify flagged values and explain what the flag means.',[
    ('Calculate the central span','The quartiles remain 2.75 and 6.25 because the changed final value does not affect those interpolation positions. The IQR is 3.5.',r'\operatorname{IQR}=6.25-2.75=3.5'),
    ('Distinguish fences from observations','The lower fence is minus 2.5 and upper fence 11.5. The smallest and largest actual values within the fences are one and seven, which are the whisker endpoints. Thirty lies beyond the upper fence.',r'F_L=2.75-1.5(3.5)=-2.5;\quad F_U=6.25+1.5(3.5)=11.5'),
    ('Interpret the flag','The flag identifies an observation unusual under this box-plot convention. It does not prove a measurement error or authorize removal. Inspect its source and scientific context, and retain it unless a documented eligibility or correction rule justifies a change.',None)],{'q1':2.75,'q3':6.25,'iqr':3.5,'lower_fence':-2.5,'upper_fence':11.5,'lower_whisker':1,'upper_whisker':7,'flagged_value':30})

problem(4,'A scatter plot preserves a curved pattern',
    'Five paired observations have x values -2, -1, 0, 1, and 2, with y values 4, 1, 0, 1, and 4. Choose a display, describe the relation, and calculate the centred product sum to show why a linear summary can miss it.',[
    ('Keep the pairs','Use a scatter plot with x on the horizontal axis and y on the vertical. Each point retains its observed pairing. A bar chart of independently sorted columns would destroy the relation.',None),
    ('Check the cancellation','The x mean is zero and y mean is two. Centred products are -4, 1, 0, -1, and 4, whose sum is zero. Both variables vary, so Pearson correlation is zero.',r'S_{xy}=-4+1+0-1+4=0'),
    ('Interpret the graph','Every response equals the square of its predictor. The exact U-shaped relationship is not linear or globally monotonic. Zero centred linear association is therefore compatible with a deterministic relation. The scatter plot reveals information a single linear coefficient loses.',None)],{'x_mean':0,'y_mean':2,'sxy':0,'pearson_r':0})

problem(5,'Combining people rather than groups',
    'Ten students have mean score 70 and thirty students have mean score 80. Calculate the mean across all forty students and the equally weighted mean of the two group means. State the target of each result.',[
    ('Recover totals','The implied group score totals are seven hundred and two thousand four hundred. The groups are disjoint and measured on the same score scale, so their totals and counts can be added.',r'T=10(70)+30(80)=3100'),
    ('Use the person denominator','Dividing by forty gives 77.5. Group sizes are the weights because the target treats each student equally.',r'\bar x=3100/40=77.5'),
    ('Name the other target','The equal-group average is seventy-five. It describes an average of two group means with each group given equal importance. It does not describe the equally weighted forty-person mean. Whether it is useful depends on the stated institutional question.',r'(70+80)/2=75')],{'combined_mean':77.5,'equal_group_mean':75,'combined_total':3100})

problem(5,'Equal distance versus equal time',
    'A traveller covers 60 kilometres at 30 kilometres per hour and another 60 kilometres at 60 kilometres per hour. Find the overall speed. Compare it with one hour at each speed and explain the two averaging rules.',[
    ('Add distance and time','The two equal-distance legs take two hours and one hour. Total distance is one hundred and twenty kilometres and total time three hours. Overall speed is forty kilometres per hour.',r'v=120/(60/30+60/60)=40'),
    ('Recognize the harmonic mean','Because distances are equal, this equals the harmonic mean of thirty and sixty. The arithmetic mean forty-five would not preserve total travel time for these legs.',r'H=2/(1/30+1/60)=40'),
    ('Change the exposures explicitly','One hour at each speed covers thirty plus sixty kilometres in two hours, giving forty-five. Equal time produces an arithmetic mean. The correct rule follows from accumulated distance divided by accumulated time, not from the word speed alone.',r'v_{\rm equal\ time}=(30+60)/2=45')],{'equal_distance_speed':40,'equal_time_speed':45,'equal_distance_hours':3})

problem(5,'Sensitivity of mean and median',
    'The values 2, 4, 4, 7, and 13 have mean six and median four. Replace only thirteen with one hundred and thirteen. Recalculate both summaries and explain their different sensitivity without assuming the new value is an error.',[
    ('Track the total change','The total rises by one hundred while count remains five. Therefore the mean rises by twenty, from six to twenty-six.',r'\bar x_{\rm new}=(2+4+4+7+113)/5=26'),
    ('Track the ranks','The sorted middle observation remains four, so the median remains four. Increasing a value already above the middle does not change that middle rank in this example.',r'\operatorname{median}=4'),
    ('Connect to the question','The mean accurately reflects the changed total and the median accurately reflects the unchanged middle position. Resistance to one extreme magnitude is useful for some questions, while total preservation matters for others. Check provenance separately before treating an unusual value as an error.',None)],{'new_mean':26,'new_median':4,'mean_change':20})

problem(6,'Two variance denominators',
    'Calculate the descriptive variance, sample variance, and their standard deviations for 2, 4, 4, 7, and 13. State units and explain why the sample-variance correction does not imply that one realised estimate equals a population variance.',[
    ('Centre and square','The mean is six. Squared deviations are sixteen, four, four, one, and forty-nine, totaling seventy-four. All use the same eligible five observations.',r'S_{xx}=74'),
    ('Apply the two definitions','Dividing by five gives descriptive variance 14.8; dividing by four gives sample variance 18.5. Their square roots are approximately 3.847077 and 4.301163 minutes. Variances are in squared minutes.',r'm_2=74/5=14.8;\quad s^2=74/4=18.5'),
    ('State the statistical scope','The n-minus-one estimator is unbiased for population variance under independent common-distribution sampling with finite variance. That is a repeated-sampling property. It does not guarantee that this particular estimate equals the unknown variance or that its square root is also unbiased.',None)],{'sxx':74,'descriptive_variance':14.8,'sample_variance':18.5,'descriptive_sd':14.8**.5,'sample_sd':18.5**.5})

problem(6,'Within and between variation',
    'Two groups contain values (1,3) and (7,9). Calculate the overall mean, within-group and between-group sums of squares, and both overall variance conventions. Explain why averaging the group descriptive variances is insufficient.',[
    ('Find the centres','Group means are two and eight; the overall mean is five. Each group has two values and internal squared-deviation sum two. The combined within sum is four.',r'\bar x=5;\quad SS_W=2+2=4'),
    ('Add the mean separation','Between sum of squares is two times three squared plus two times three squared, or thirty-six. Total sum of squares is forty, giving descriptive variance ten and sample variance forty thirds.',r'SS_B=2(2-5)^2+2(8-5)^2=36;\quad SS_T=40'),
    ('Interpret the missing component','Each group descriptive variance is one. Their average misses the thirty-six units of squared variation associated with separated group means. Total spread combines within-group variation and group-location differences, without itself providing a causal explanation.',None)],{'overall_mean':5,'within_ss':4,'between_ss':36,'total_ss':40,'descriptive_variance':10,'sample_variance':40/3})

problem(6,'Relative spread and an arbitrary origin',
    'Use the five waiting times with mean six and sample variance 18.5. Calculate the sample coefficient of variation. Convert minutes to seconds and show it stays the same. Then add four to every original value and explain why CV changes although spread does not.',[
    ('Calculate relative spread','Sample standard deviation is the square root of 18.5. Dividing by the positive mean six gives approximately 0.716860, or 71.6860 percent. The measurement has a meaningful zero for this relative comparison.',r'CV=\sqrt{18.5}/6'),
    ('Change units multiplicatively','Seconds multiply mean and standard deviation by sixty, so their ratio is unchanged. Variance instead multiplies by thirty-six hundred. Keep these different transformation rules distinct.',r'CV_{\rm seconds}=60s/(60\bar x)=CV'),
    ('Shift the origin','Adding four gives mean ten but leaves standard deviation unchanged, producing CV approximately 0.430116. This sensitivity to addition explains why a conventional ratio-based CV is unsuitable for scales with an arbitrary zero point, such as Celsius temperatures.',r'CV_{\rm shifted}=\sqrt{18.5}/10')],{'cv':18.5**.5/6,'cv_seconds':18.5**.5/6,'cv_shifted':18.5**.5/10})

problem(7,'Moments for a small asymmetric sample',
    'For 0, 0, and 3, calculate the mean, descriptive central moments m2, m3, and m4, moment skewness, raw kurtosis, and excess kurtosis. Verify the skewness-kurtosis inequality using these descriptive definitions.',[
    ('Centre at the current mean','The mean is one and deviations are -1, -1, and 2. Averaging their squared, cubed, and fourth powers gives m2 two, m3 two, and m4 six. The denominator is three for every central moment.',r'm_2=6/3=2;\quad m_3=6/3=2;\quad m_4=18/3=6'),
    ('Standardize shape','Skewness is one divided by the square root of two, about 0.707107. Raw kurtosis is 1.5 and excess kurtosis minus 1.5. Positive asymmetry and negative normal-reference excess can coexist.',r'g_1=2/2^{3/2};\quad b_2=6/2^2=1.5;\quad g_2=-1.5'),
    ('Check the constraint','Skewness squared plus one is 1.5, exactly equal to raw kurtosis here. This meets the descriptive inequality. The adjusted Fisher-Pearson skewness would be a different coefficient and is not substituted into this check.',r'b_2=g_1^2+1')],{'mean':1,'m2':2,'m3':2,'m4':6,'skewness':2/2**1.5,'raw_kurtosis':1.5,'excess_kurtosis':-1.5})

problem(7,'Translation, scaling and reflection',
    'Starting with 0, 0, and 3, define y equal to ten plus twice x and z equal to ten minus twice x. Find their means and second through fourth central moments. Describe changes to standardized skewness and kurtosis.',[
    ('Transform centres','The original mean is one, so the y mean is twelve and z mean eight. Adding ten shifts the centre; it does not add ten to centred deviations.',r'\bar y=10+2(1)=12;\quad\bar z=10-2(1)=8'),
    ('Transform powers','For y, central moments are four times two, eight times two, and sixteen times six: eight, sixteen, and ninety-six. For z the even moments match and the third is minus sixteen, because reflection reverses odd powers.',r'm_{2,y}=8;\quad m_{3,y}=16;\quad m_{4,y}=96;\quad m_{3,z}=-16'),
    ('Cancel units in shape','Positive scaling preserves original skewness and raw kurtosis. Reflection reverses skewness while raw kurtosis stays 1.5. This validates both centring and standardized-power calculations. A nonlinear transformation would not have these simple rules.',None)],{'mean_y':12,'mean_z':8,'m2_y':8,'m3_y':16,'m4_y':96,'m2_z':8,'m3_z':-16,'m4_z':96,'raw_kurtosis_y':1.5,'raw_kurtosis_z':1.5})

problem(7,'Central quantiles and an influential tail',
    'For 1, 2, 3, 4, 5, 6, 7, and 30, calculate type-seven Bowley skewness and descriptive moment skewness. Explain why the two summaries describe different aspects rather than requiring identical values.',[
    ('Inspect the quartile geometry','The quartiles are 2.75, 4.5, and 6.25. The numerator Q3 plus Q1 minus twice the median is zero and IQR is 3.5. Bowley skewness is therefore zero.',r'B=(6.25+2.75-2(4.5))/3.5=0'),
    ('Calculate tail-weighted moments','The mean is 7.25. Direct centred arithmetic gives m2 77.4375 and m3 1407.65625. Dividing the third moment by the second to power three halves gives moment skewness approximately 2.065711. Cubes give the high observation a strong contribution.',r'g_1=1407.65625/(77.4375)^{3/2}'),
    ('State both scopes','The central quartile distances are balanced, while the third-moment summary has positive upper-tail influence. A plot and the actual tail record clarify the distinction. Neither coefficient alone proves a population shape or establishes that thirty is erroneous.',None)],{'bowley':0,'mean':7.25,'m2':77.4375,'m3':1407.65625,'skewness':1407.65625/77.4375**1.5})

problem(8,'Pearson correlation from centred sums',
    'For paired x values 1,2,3,4 and y values 2,3,5,4, compute Pearson correlation. State its scope and explain why a different dataset could have correlation zero yet a structured relationship.',[
    ('Calculate centred sums','The means are 2.5 and 3.5. Centred arithmetic gives Sxx five, Syy five, and Sxy four. Preserve the pairing while calculating the products.',r'S_{xx}=5;\quad S_{yy}=5;\quad S_{xy}=4'),
    ('Normalize','The denominator is the square root of twenty-five, or five. Pearson correlation is 0.8. A common covariance denominator cancels only when numerator and standard deviations use compatible conventions.',r'r=4/\sqrt{5\cdot5}=0.8'),
    ('Interpret linear association','These recorded pairs have positive linear association. The coefficient is not a causal effect or an agreement measure. A symmetric quadratic relation can have cancelling centred products and correlation zero, so a scatter plot remains necessary.',None)],{'sxx':5,'syy':5,'sxy':4,'pearson_r':.8})

problem(8,'Ranks and pairs when one variable has ties',
    'Paired x values are 10,20,20,40 and y values 1,3,2,4. Assign midranks and calculate Spearman correlation. Enumerate Kendall pair counts and calculate tau-b, showing how the x tie enters the denominator.',[
    ('Use actual midranks','The x ranks are 1,2.5,2.5,4 and y ranks 1,3,2,4. Both mean ranks are 2.5. Rank Sxx is 4.5, Syy five, and Sxy 4.5. Spearman correlation is approximately 0.948683 using Pearson correlation of these ranks.',r'r_S=4.5/\sqrt{4.5(5)}'),
    ('Classify six pairs','Five pairs are concordant and none discordant. The pair between the two x twenties is tied only in x, so Tx is one and Ty zero. There are no double ties. Do not use the no-tie rank-difference shortcut.',None),
    ('Normalize with ties','Tau-b is five divided by the square root of six times five, approximately 0.912871. It differs from Spearman because it uses pair comparisons and tie normalization rather than rank covariance.',r'\tau_b=5/\sqrt{(5+1)(5+0)}')],{'spearman':4.5/(4.5*5)**.5,'concordant':5,'discordant':0,'ties_x_only':1,'ties_y_only':0,'kendall_tau_b':5/30**.5})

problem(8,'Observed binary association',
    'A two-by-two table has a=30 for x=1,y=1; b=10 for x=1,y=0; c=20 for x=0,y=1; and d=40 for x=0,y=0. Calculate phi. Explain why this is not automatically a tetrachoric correlation.',[
    ('Preserve layout and margins','Row margins are forty and sixty; column margins fifty and fifty. The determinant is thirty times forty minus ten times twenty, or one thousand. All margins are positive, so observed phi is defined.',r'ad-bc=1000'),
    ('Calculate observed correlation','The denominator is the square root of six million. Phi is approximately 0.408248 and equals Pearson correlation of the zero-one columns represented by these counts.',r'\phi=1000/\sqrt{40(60)(50)(50)}'),
    ('Separate the latent model','Tetrachoric correlation assumes thresholded jointly normal latent variables and generally requires model-based numerical fitting with the margins. The observed coefficient alone does not justify that assumption or determine a universal conversion. Report phi as observed binary association unless the latent model is explicitly supported.',None)],{'determinant':1000,'phi':1000/(40*60*50*50)**.5})

problem(9,'Fit and verify a simple line',
    'Fit y on x for x=1,2,3,4 and y=2,3,5,4 using an intercept. Calculate fitted values, residuals, SSE, SSR, and R-squared. Verify the residual zero-sum identity and the total-sum decomposition.',[
    ('Find coefficients','Means are 2.5 and 3.5, with Sxx five and Sxy four. Slope is 0.8 and intercept 1.5. The line passes through the sample mean point.',r'\hat y=1.5+0.8x'),
    ('Inspect residuals','Fitted values are 2.3,3.1,3.9,4.7; residuals are -0.3,-0.1,1.1,-0.7. Their sum is zero and their squared sum is 1.8. Centred-x-weighted residuals also sum to zero.',r'SSE=0.09+0.01+1.21+0.49=1.8'),
    ('Partition recorded variation','SST is five and SSR is slope squared times Sxx, giving 3.2. Thus five equals 3.2 plus 1.8, and R-squared is 0.64. This is a descriptive linear-fit proportion, not a causal percentage or a promise about future accuracy.',r'R^2=3.2/5=0.64')],{'slope':.8,'intercept':1.5,'residual_sum':0,'sse':1.8,'ssr':3.2,'sst':5,'r_squared':.64})

problem(9,'Reverse regression is a different fit',
    'Using the same four pairs, fit x on y. Compare its slope with the reciprocal of the y-on-x slope and verify the product of the two fitted slopes equals Pearson correlation squared.',[
    ('Fit the reverse direction','Sxy is four and Syy five, so the x-on-y slope is 0.8. Its intercept is x-bar minus 0.8 times y-bar, giving minus 0.3.',r'\hat x=-0.3+0.8y'),
    ('Compare with inversion','The reciprocal of the forward slope is 1.25, which differs from 0.8. Solving the forward fitted equation for x does not minimize squared x residuals and is not the reverse least-squares fit.',r'1/0.8=1.25\ne0.8'),
    ('Verify the relationship','The product of directional slopes is 0.64, equal to Pearson r squared. It equals one only for a perfect nonconstant linear relation. Directional regression and symmetric correlation therefore convey related but distinct information.',r'b_{yx}b_{xy}=0.8(0.8)=0.64=r^2')],{'reverse_slope':.8,'reverse_intercept':-.3,'reciprocal_forward_slope':1.25,'slope_product':.64})

problem(9,'Audit a synthetic period-level investigation',
    'Four synthetic service periods have arrival counts 1,2,3,4 and period mean waits 2,3,5,4 minutes. Summarize the period responses, predict the fitted mean at x=2.5, and evaluate the statement: each additional arrival causes every customer to wait 0.8 minutes longer. Identify a better conclusion and a needed next step.',[
    ('Keep the observational level','The four response values are period means, not four individual customer waits. Their mean and median are both 3.5 minutes, descriptive variance 1.25, and range three. Equal period weighting does not give the customer-weighted average without customer counts.',r'\bar y=3.5;\quad m_{2,y}=1.25'),
    ('Calculate the descriptive fit','The fitted line is 1.5 plus 0.8 times x, so at 2.5 arrivals it gives 3.5 minutes. The noninteger predictor is a mathematical interpolation of the fitted relation, not an assertion that a real period contains half a person.',r'\hat y(2.5)=1.5+0.8(2.5)=3.5'),
    ('Correct the conclusion','The proposed causal statement is unsupported by these observational synthetic summaries. A defensible description is that higher-arrival periods have a positive fitted linear association with mean wait in this illustration. A real investigation should record staffing, case mix, individual waits, and a suitable design before making causal or individual prediction claims.',None)],{'response_mean':3.5,'response_median':3.5,'response_descriptive_variance':1.25,'response_range':3,'fitted_at_2_5':3.5})

summaries = [
 'Statistical questions, populations and samples, descriptive reasoning, random selection, causality, summation and reproducible evidence.',
 'Measurement scales, operational definitions, questionnaires, data dictionaries, missing-value bounds and defensible cleaning.',
 'Frequency and cumulative tables, class boundaries, histogram density, conditional proportions, grouped approximations and Simpson’s paradox.',
 'Bar charts, histograms, scatter plots, time plots, empirical distribution functions, type-seven quartiles, box plots and graphical audits.',
 'Arithmetic mean, median, quantiles, mode, weighted means, geometric growth factors, harmonic rate averages and robust location.',
 'Range, interquartile range, absolute deviations, descriptive and sample variance, group decomposition, standard scores and coefficients of variation.',
 'Raw and central moments, descriptive and adjusted skewness, quartile asymmetry, raw and excess kurtosis, transformations and shape constraints.',
 'Pearson and rank correlation, ties, Kendall concordance, point-biserial, biserial, phi, tetrachoric models, correlation ratio and intraclass correlation.',
 'Least-squares regression, residuals, sums of squares, R-squared, reverse fits, leverage, extrapolation and a reproducible integrated investigation.'
]
simulations={1:'stat-sampling',3:'stat-histogram',4:'stat-boxplot',5:'stat-location',6:'stat-variation',7:'stat-shape',8:'stat-association',9:'stat-regression'}
units=[]
for i in range(1,10):
    text=(DRAFT/f'unit-{i}.md').read_text()
    title=([
        'Statistical Reasoning, Populations and Evidence',
        'Measurement, Data Collection and Data Quality',
        'Classification, Frequency Tables and Cross-Tabulation',
        'Statistical Graphics and Exploratory Data Analysis'
    ][i-1] if i<=4 else text.splitlines()[0].split(': ',1)[1])
    chunks=re.split(r'^## ([^\n]+)\n',text,flags=re.M)
    sections=[]
    for j in range(1,len(chunks),2):
        number,heading=chunks[j].split(' ',1)
        sections.append(dict(secNumber=number,heading=heading,content=chunks[j+1].strip()))
    sim=simulations.get(i)
    if sim:
        sections[0]['simulations']=[]
        sections[-1]['simulation']=sim
    units.append(dict(id=f'stat-unit-{i}',number=i,title=title,leadSummary=summaries[i-1],
        simulations=[sim] if sim else [],sections=sections,problems=problems[i-1]))
data=dict(title='Introduction to Statistics',language='en',curriculum='University of Dhaka Statistics B.S. Honours, 2023–24: Stat H-101 and H-109',units=units)
(ROOT/'introduction-to-statistics-data.js').write_text('// Original OpenSTEM teaching text. Generated from saved editorial drafts.\nwindow.COURSE_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
(DRAFT/'worked-solutions.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'units':len(units),'sections':sum(len(u['sections']) for u in units),'worked_questions':sum(len(u['problems']) for u in units)}))
