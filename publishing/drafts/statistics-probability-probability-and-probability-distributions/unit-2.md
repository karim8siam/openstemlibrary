# Unit 2: Conditional Probability, Independence and Bayesian Updating

## Learning aims: probabilities in a stated information set

A probability statement is incomplete if the available information is unclear. The chance that a randomly selected item comes from a particular production batch can differ from the chance that an item with an observed inspection flag comes from that batch. Both probabilities can be correct. They refer to different information sets and therefore different reference collections. Conditioning supplies a precise way to express this difference without changing the underlying rules of probability.

This unit develops conditional probability from intersections and renormalization, derives multiplication and total-probability rules, and uses those rules to establish Bayes' theorem. It also distinguishes ordinary independence from conditional independence and explains how selecting records can create relationships absent in the original model. The three worked questions apply these ideas to batch classification, sequential sampling and a shared-condition experiment. All numerical probabilities in the examples are stipulated educational assumptions, not estimates for an actual industry or institution.

The central discipline is to name what is known before calculating. The statement given a flag is not interchangeable with given a particular source, and neither is interchangeable with given a sequence of earlier outcomes. A conditional probability has a target event and a conditioning event. Reversing them changes the question. A calculation should retain that order in its notation, its denominator and its verbal interpretation.

Conditioning need not describe information acquired later in time. An analyst can ask about a past source given a current record, about one simultaneous measurement given another, or about a future event given a completed history. The word given identifies a reference condition within the model, not a causal direction or a chronological law. Bayesian updating often reverses the direction of a forward probability specification, but that reversal is an application of the same joint probability rather than a reversal of physical causation.

## Conditional probability as restriction and renormalization

For events $A$ and $B$ with $P(B)>0$, the conditional probability of $A$ given $B$ is

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

The numerator retains outcomes satisfying both the information and the target. The denominator is the total weight of outcomes satisfying the information. The ratio makes the conditioning collection have total probability one. Outcomes outside that collection receive no weight in the conditional model. This restriction is not an arbitrary adjustment: it directly answers what fraction of the original probability weight inside the stated condition also satisfies the target.

In a finite equally weighted model, conditioning on an event preserves equal weighting among its constituent outcomes. If a uniform sample space contains one hundred equally weighted records, forty satisfy $B$, and ten satisfy both $A$ and $B$, then the conditional probability is one quarter. The denominator is forty rather than one hundred. In a nonuniform model, counting records alone is insufficient: each record contributes its assigned weight. Conditional probability is a ratio of probabilities, with a ratio of counts as a special case.

The event $B$ may describe an observation, a design restriction or a logical condition. Conditioning on a device passing a test is an information restriction. Conditioning on a sample including a member of a named group is a selection restriction. Conditioning on a mathematical inequality is an event restriction. The same formula applies when the events have positive probability. Whether the restriction is appropriate for the practical question is a separate modeling issue.

For a fixed positive-probability $B$, the function $A\mapsto P(A\mid B)$ obeys the probability axioms. It is nonnegative. It gives the full sample space probability one because the intersection of the full space with $B$ is $B$. For disjoint target events, intersecting each with $B$ keeps them disjoint, so original additivity passes through the common denominator. Consequently complement rules, union rules and bounds remain valid within the conditional model.

For example, the conditional complement rule is $P(A^c\mid B)=1-P(A\mid B)$. The complement here refers to failure of the target under the fixed information, not failure of the information. Confusing $P(A^c\mid B)$ with $P(A\mid B^c)$ changes both sides of the question. One asks about the opposite target in the same reference collection; the other asks about the original target in the opposite reference collection.

Conditioning on the target itself gives $P(A\mid A)=1$ when $P(A)>0$. Conditioning on a condition that implies the target also gives one. If $B\subseteq A$, every retained outcome satisfies $A$. If the target and the condition are disjoint, the conditional probability is zero. These simple cases provide useful checks of more complicated event translations.

The definition requires positive probability for the condition. If $P(B)=0$, both numerator and denominator are zero, and the elementary ratio does not define a conditional probability. It is incorrect to replace the undefined ratio by zero or one according to intuition. Continuous conditional densities and regular conditional distributions provide appropriate extensions in later units, but they require an additional framework. Their formulas cannot be justified by directly dividing two zero probabilities.

This limitation matters when a continuous observation is reported as an exact value. A continuously distributed measurement can assign zero probability to every singleton. Conditioning on a small interval around a value is a positive-probability operation; defining a conditional density at a value is another operation justified through joint densities or a suitable conditional distribution. Treating the two as literally identical conceals a mathematical step. This unit stays with positive-probability events and finite models so that every denominator is explicit.

## Multiplication rules and sequential histories

Rearranging the conditional definition yields the multiplication rule:

$$
P(A\cap B)=P(B)P(A\mid B)=P(A)P(B\mid A),
$$

with each displayed conditional defined when its conditioning event has positive probability. The two products represent the same joint event from different directions. A forward mechanism may make one product easy to specify, while an observed condition makes the reverse conditional the quantity of interest. Bayes' theorem will organize that conversion.

For a sequence of events, repeated multiplication produces a chain rule. A three-event intersection can be written as

$$
P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B).
$$

The last factor is conditioned on the full previous intersection, not merely on the most recent event, unless a model assumption permits that simplification. Ignoring part of the history is equivalent to imposing an additional conditional-independence or memory assumption. A process described informally as sequential does not automatically have such a property.

Suppose labeled objects are drawn without replacement. After each draw, the composition of the collection changes. The probability of the next category depends on earlier categories through the remaining composition. Multiplication of the successive conditional probabilities is valid, while multiplication of the same initial fraction repeatedly is generally not. With replacement and independent randomization, the initial composition can be restored at each stage, justifying a constant probability. These mechanisms produce different joint distributions even when their first-draw probabilities agree.

A probability tree is a visual representation of the chain rule. Its branches at each node correspond to disjoint alternatives under that node's history. Their probabilities must sum to one. The probability of a path is the product of its branch probabilities, and the probability of an event comprising several disjoint paths is the sum of their path probabilities. A correct tree therefore combines multiplication along paths with addition across compatible paths.

The same event can have several paths. At least one success in three trials contains multiple outcome sequences. Adding three probabilities of success on a particular trial overcounts sequences containing multiple successes. A tree avoids that error when its terminal paths distinguish the complete histories. Complementing the all-failure path may be more efficient if the model gives its probability directly. Efficiency should follow correct event construction, not replace it.

Every conditional branch should be labeled with the history that determines it. A diagram containing the number one half at each branch may look convincing, but it is only justified when the mechanism supports those probabilities after every earlier result. A branch whose probability is zero creates an impossible path, and any later conditional attached to that path needs careful interpretation. It is simpler to omit unreachable nodes from an elementary tree than to assign arbitrary probabilities to undefined conditions.

The multiplication rule also applies when events are not stages in time. A joint table of department and equipment choice can be factored as a department probability times an equipment probability within that department. Reversing the factorization uses equipment first and department within the equipment category. The table remains the same. Factoring a joint distribution in a convenient order is a mathematical strategy, not a statement that the first written event caused the second.

## Independence and its information interpretation

When $P(B)>0$, independence of $A$ and $B$ is equivalent to $P(A\mid B)=P(A)$. This follows by dividing the defining equation $P(A\cap B)=P(A)P(B)$ by $P(B)$. The information that $B$ occurs then leaves the modeled probability of $A$ unchanged. If both event probabilities are positive, the reverse conditional is unchanged as well. This symmetry is a consequence of the joint-probability factorization.

The factorization definition remains preferable as the general definition because it handles zero-probability events without undefined conditionals. An event of probability zero is independent of every event in the formal two-event sense. This does not justify conditioning on it by the elementary ratio. Two correct statements can coexist: the factorization property holds, and the event-conditioned ratio is undefined. Keeping the definitions separate prevents a false contradiction.

Independent repeated trials require more than equal marginal probabilities. A process can give every trial the same success probability while making all results strongly dependent. For example, drawing one random binary value and recording it repeatedly gives the same marginal probability at each position, but a first observed value determines all later ones. A binomial model will require independent trials with a common success probability, not merely a common percentage in each position.

Mutual independence supplies every needed factorization for a collection of events. Pairwise independence alone may not permit products for a multi-event path, as shown by the parity example in Unit 1. If three events are only known to be pairwise independent, multiplying their three marginal probabilities to calculate the all-three event is an unjustified additional assumption. It can be tempting because every pairwise check looks reassuring, but the triple condition still requires verification.

Independence is relative to the model's information and population. Two device outcomes may be independent in a model with a fixed operating temperature yet dependent in a model that mixes several temperatures. Conversely, conditioning on an outcome-based selection criterion can introduce dependence among initially independent events. Independence claims should therefore state the relevant conditions and should not be transferred automatically between a full population and a selected subset.

Conditional independence given an event $C$ with positive probability means

$$
P(A\cap B\mid C)=P(A\mid C)P(B\mid C).
$$

This is ordinary independence within the conditional probability model. Conditional independence given a categorical variable requires the corresponding statement within each relevant category with positive probability. Independence in only one category is not enough to justify the claim for the full variable. When some category has zero probability, the elementary conditional statement for that category is not defined and should not be presented as an observed branch.

An assumption of conditional independence can make a model tractable. If a specified batch condition determines a common pass probability and devices are generated independently within the condition, the probability of two passes within that condition is the square of that pass probability. Averaging those squared probabilities across conditions is generally different from squaring the averaged pass probability. This distinction is the source of the shared-condition dependence examined in the third worked question.

## Partitions and the law of total probability

A partition of the sample space is a collection of disjoint events whose union is the whole space. Each outcome belongs to exactly one member. A partition by source category, group membership or modeled operating condition allows a complex event to be decomposed into nonoverlapping pieces. If the members are $H_1,\ldots,H_k$, then $B$ is the disjoint union of the intersections $B\cap H_i$.

Additivity and the multiplication rule therefore give the law of total probability:

$$
P(B)=\sum_{i=1}^{k}P(H_i)P(B\mid H_i).
$$

The formula assumes the displayed conditional probabilities are defined for the partition members used. A zero-probability member contributes zero through its joint event and can be omitted. A countable partition can be handled by countable additivity under the same reasoning. For a continuous grouping variable, sums will become integrals in a later unit.

The partition probabilities act as weights. They sum to one, and the conditional event probabilities lie between zero and one. The resulting overall probability is a weighted average of the conditional probabilities and must lie between their minimum and maximum. This range check is useful. If an overall pass probability exceeds every subgroup pass probability, the weights, denominators or arithmetic are inconsistent.

Equal weighting of categories is valid only when the categories are equally probable under the relevant experiment. A collection containing twenty items from one source and eighty from another does not justify averaging their defect rates with equal weights when an item is drawn uniformly. The source weights are one fifth and four fifths. If the experiment instead selects one of the sources uniformly and then an item within it, equal source weights may be appropriate. The selection mechanism again determines the averaging rule.

The partition must cover the entire reference population. A formula that includes two sources while quietly omitting a third describes a conditional subpopulation, not the full collection. If source information is missing for some records, treating missing source as a separate category can make the completeness problem visible. Assigning the omitted records to known categories without evidence adds a modeling assumption and may change the total probability.

The law of total probability is also a prediction rule. If a future item has an uncertain source, its event probability is obtained by averaging conditional predictions over the source distribution. After evidence changes the source probabilities, the predictive average uses the updated weights. It is not enough to update a source classification and then keep the original predictive weights. The model must carry the information change through all relevant calculations.

## Bayes' theorem from a single joint probability

Bayes' theorem connects the reverse conditional probabilities for two events with positive conditioning probabilities. Starting from the two factorizations of the intersection gives

$$
P(H\mid B)=\frac{P(H)P(B\mid H)}{P(B)}.
$$

For a partition of possible sources, substitute the total-probability expression for the denominator:

$$
P(H_j\mid B)=\frac{P(H_j)P(B\mid H_j)}{\sum_i P(H_i)P(B\mid H_i)}.
$$

The numerator is the joint probability of the selected source and evidence. The denominator is the evidence probability across every allowed source. The resulting probabilities across sources sum to one. This normalization is what makes the result a distribution of sources after the evidence, rather than a list of unnormalized scores.

The probability $P(H_j)$ is called the prior probability relative to the evidence under discussion. The conditional evidence probability $P(B\mid H_j)$ is the likelihood of that evidence under source $H_j$. The updated source probability $P(H_j\mid B)$ is the posterior probability. These names describe roles within one calculation. A posterior after one observation can become the prior before a later observation, provided the later likelihood is correctly conditioned on the information already used.

A likelihood is not automatically a probability distribution over sources. As a function of the source index, its values need not sum to one. It describes how probable the observed evidence is within each source model. Multiplying by source weights and normalizing converts those values into posterior source probabilities. Choosing the source with the largest likelihood while ignoring prior weights answers a different decision question from choosing the source with the largest posterior probability.

The denominator is sometimes called the evidence probability or marginal likelihood. In a finite source model it is a direct weighted sum. Dropping it can be acceptable when writing proportionality for comparing posterior scores, but the final probabilities must be normalized. An unnormalized score of one tenth does not mean a ten-percent posterior probability. The total of all scores determines the scale.

Reversing a conditional without adjustment is a common error. A source may generate a flag frequently, yet flagged items may mostly come from another source because that other source supplies far more items. The prior source weights account for this population composition. The likelihood accounts for the flag mechanism within each source. Both are required to interpret the flag. Neither alone answers the posterior-source question.

Bayes' theorem is not a claim that a prior is unquestionably correct. It states what follows within a specified joint model. A prior derived from an uncertain production mixture can be varied in a sensitivity analysis. A likelihood derived from an uncertain calibration can also be varied. Reporting only one posterior number without its assumptions can conceal substantial model uncertainty. Coherent updating improves the reasoning but cannot repair incorrect inputs by itself.

## Odds, likelihood ratios and sequential updates

For an event $H$ with probability strictly between zero and one, its odds are $P(H)/(1-P(H))$. Odds compare the probability of the event with the probability of its complement. They are not the same as probability: odds one mean probability one half, while odds three mean probability three quarters. Conversion back to probability divides the odds by one plus the odds.

For evidence $B$ with positive relevant probabilities, Bayes' theorem yields

$$
\frac{P(H\mid B)}{P(H^c\mid B)}=\frac{P(H)}{P(H^c)}\frac{P(B\mid H)}{P(B\mid H^c)}.
$$

Posterior odds equal prior odds multiplied by a likelihood ratio. A ratio above one shifts odds toward the target hypothesis. A ratio below one shifts them toward its complement. A ratio equal to one leaves them unchanged. The magnitude of the change depends on the ratio, while the final probability also depends on the starting odds.

If the complement contains several sources, its likelihood must be averaged using the source distribution conditional on belonging to that complement. Using an unweighted average of the source likelihoods is generally wrong. The complement is a composite hypothesis whose internal mixture matters. The first worked question demonstrates this calculation explicitly rather than treating all non-target sources as though they had the same flag rate.

Sequential evidence can be incorporated by the chain rule. For observations $B_1$ and $B_2$, the likelihood under $H$ is $P(B_1\mid H)P(B_2\mid H\cap B_1)$ in event notation. If the observations are conditionally independent given the source, the second factor can be replaced by $P(B_2\mid H)$. Without that assumption, multiplying the two single-observation likelihoods double-counts or misrepresents the dependence structure.

Repeated descriptions of the same evidence are not new independent observations. If a flag is copied into two database columns, observing both columns supplies the same information as observing the original flag. Squaring its likelihood would falsely amplify the evidence. Similarly, two instruments may share a calibration error. Their likelihoods cannot be multiplied as conditionally independent merely because their outputs appear in separate fields.

Log odds can simplify long sequences because multiplication of likelihood ratios becomes addition of their logarithms. This is a computational representation, not a new updating rule. A zero likelihood can exclude a hypothesis under the exact model, while a nearly zero likelihood can lead to numerical underflow if products are calculated directly. Appropriate implementations retain enough numerical precision and keep impossible model outcomes distinct from merely unlikely ones.

When evidence is more likely under a source, the posterior probability of that source often increases, but the amount must be computed. A source with a low prior weight may remain unlikely even after favorable evidence. Conversely, a very common source can dominate a posterior despite a lower evidence likelihood. These observations are consequences of prior-weighted normalization, not exceptions to Bayes' theorem.

## Selection, information loss and induced relationships

Conditioning changes a reference population. It can create dependence between events that were independent before selection. Consider two independent binary events each having probability one half, and retain only records where at least one occurs. Before selection, their joint occurrence has probability one quarter. The retention event has probability three quarters. Among retained records, each event has conditional probability two thirds, while their joint conditional probability is one third.

The product of the two conditional marginal probabilities is four ninths, which differs from one third. The selected events are therefore dependent. Once one event is known to be absent in a retained record, the other must be present. The dependence was created by the retention rule, even though the original events were independent. This example illustrates why relationships in a selected dataset cannot automatically be interpreted as relationships in the full population.

Selection can also change apparent source proportions. If flagged devices are deliberately oversampled, the fraction of flagged devices in the dataset is a property of the sampling design. It is not automatically the flag probability in production. Correct analysis requires the selection mechanism or an appropriate weighting scheme. Conditioning on being included in the dataset is part of the model when inclusion depends on outcomes or sources.

Information can be lost through coarsening. Knowing that at least one of two trials succeeded is less detailed than knowing the full pair of outcomes. An update based on the coarse event averages over compatible detailed outcomes. If one later obtains the full pair, the new calculation must incorporate the additional information without counting the coarse statement as an independent observation. Both statements refer to the same underlying experiment.

The sampling protocol can make a verbal statement ambiguous. Suppose someone reports a selected member of a pair has a property. The event depends on whether the reporter selected uniformly, searched for a member with the property, or followed a deterministic priority rule. These procedures can produce different probabilities for the unreported member. The correct denominator is determined by the reporting process, not by the sentence stripped of its protocol.

A causal interpretation requires more than conditional probability. Observing that one event changes the conditional probability of another does not establish that intervening on the first would change the second. Shared conditions, reverse temporal order and selection can all create such changes. This book uses probability calculations to describe the stipulated joint models. It does not label a conditional association as a causal effect without a separate causal design and assumptions.

## Fully worked question 1: Updating a source after an inspection flag

**Question.** A randomly selected device comes from source $H$, $M$, or $L$ with probabilities $0.20$, $0.50$, and $0.30$. An inspection flag occurs with conditional probabilities $0.08$, $0.03$, and $0.01$ in those sources. Find the overall flag probability, the posterior source probabilities after a flag, and the probability of source $H$ after no flag. Express the flag update for $H$ as an odds calculation. All rates are fixed assumptions of this teaching model; a flag is an instrument output, not a medical diagnosis.

**Solution, step 1: Construct joint weights.** The three sources partition the device population. The joint weights for a flag are $0.20\cdot0.08=0.016$, $0.50\cdot0.03=0.015$, and $0.30\cdot0.01=0.003$. Their sum is $0.034$, so the overall flag probability is $3.4$ percent. It lies between the smallest and largest source flag rates, as any correctly weighted average must.

**Solution, step 2: Normalize within flagged devices.** Dividing each joint weight by $0.034$ gives $P(H\mid F)=8/17$, $P(M\mid F)=15/34$, and $P(L\mid F)=3/34$. The approximate values are $0.470588$, $0.441176$, and $0.088235$. They sum to one. Source $H$ supplies only one fifth of the original population but contributes almost half of the flagged population because its conditional flag rate is higher. This does not mean that a flag proves source $H$.

**Solution, step 3: Update after the opposite evidence.** The no-flag probability is $1-0.034=0.966$. The joint probability of source $H$ and no flag is $0.20(1-0.08)=0.184$. Thus $P(H\mid F^c)=0.184/0.966=4/21$, approximately $0.190476$. This is slightly below the prior one fifth. The no-flag condition is common in every source, so it shifts source probabilities less dramatically than the relatively rare flag in this model.

**Solution, step 4: Calculate the composite-complement likelihood.** The non-$H$ group has prior probability $0.80$. Its joint flag probability is $0.015+0.003=0.018$. The flag probability within this group is therefore $0.018/0.80=0.0225$. This is a weighted average of the $M$ and $L$ flag rates within the non-$H$ population. It is not their simple average, since their source probabilities are unequal.

**Solution, step 5: Verify the odds update.** The prior odds for $H$ are $0.20/0.80=1/4$. The likelihood ratio is $0.08/0.0225=32/9$. Their product is $8/9$, the posterior odds. Converting these odds to probability gives $(8/9)/(1+8/9)=8/17$, agreeing with direct normalization. The flag likelihood $0.08$ itself is not the posterior probability. It refers to flagged outcomes within source $H$, while the posterior refers to source $H$ within flagged outcomes.

## Fully worked question 2: A sequence without replacement

**Question.** An urn contains five labeled marked objects and seven labeled unmarked objects. Three objects are drawn sequentially, uniformly without replacement. Let $E$ be the event that exactly two of the three are marked. Find the probability of the ordered pattern marked, unmarked, marked; find $P(E)$; and calculate the probability of that pattern given $E$. Also find the probability that the first draw is marked given $E$, and the probability that the third draw is marked given the observed first-two pattern marked, unmarked.

**Solution, step 1: Use the evolving composition.** The first marked draw has probability $5/12$. After it, seven of the eleven remaining objects are unmarked, so the second desired draw has probability $7/11$. After those two draws, four of the ten remaining objects are marked. The path probability is $(5/12)(7/11)(4/10)=7/66$, approximately $0.106061$. Multiplying the original fractions unchanged would ignore the removal of objects and describe a different mechanism.

**Solution, step 2: Count the exactly-two event.** Discarding order gives a uniform three-object subset. Exactly two marked objects can be selected in $\binom52\binom71=70$ ways out of $\binom{12}{3}=220$. Hence $P(E)=7/22$, approximately $0.318182$. An ordered calculation gives the same result by adding the three possible category patterns, each of which has probability $7/66$. Their equality follows from exchanging the three positions under this uniform draw mechanism, not from an assumption that all category patterns are equally likely in general.

**Solution, step 3: Condition on the exactly-two event.** The specified marked, unmarked, marked pattern is a subset of $E$, so its conditional probability is $(7/66)/(7/22)=1/3$. Under $E$, the unique unmarked position is equally likely to be first, second or third. Two of those three possibilities have a marked first draw, giving $P(\text{first marked}\mid E)=2/3$. This differs from the unconditional first-draw probability $5/12$ because the condition supplies information about the complete three-draw composition.

**Solution, step 4: Condition on an actual partial history.** Given that the first draw was marked and the second unmarked, ten objects remain, four marked. The third-marked probability is $4/10=2/5$. This is a different condition from $E$. The complete-composition condition guarantees two marked outcomes among all three, while the partial-history condition still permits either category on the third draw. Their denominators and probabilities must not be interchanged.

**Solution, step 5: Distinguish symmetry from independence.** Each position has the same unconditional probability of a marked result under the uniform without-replacement mechanism. Nevertheless the draws are dependent: observing a marked result removes one marked object and changes the chance at later positions. Equal marginal probabilities, exchangeability of positions and independence are distinct properties. Exact ordered enumeration of all $12\cdot11\cdot10$ labeled paths can verify every probability in this solution without changing that interpretation.

## Fully worked question 3: A shared condition creates marginal dependence

**Question.** A trial pair shares one unobserved operating condition. With probability $0.40$ the condition is high, and with probability $0.60$ it is low. Given high, the two binary pass outcomes are independent with pass probability $0.80$ each. Given low, they are independent with pass probability $0.30$ each. Find the marginal pass probability of each trial, the joint probability of two passes, and the probability that the second passes given that the first passes. Determine independence before and after the operating condition is specified. Find the posterior high-condition probability after one pass.

**Solution, step 1: Average the single-trial probabilities.** The marginal probability of a pass at either position is $0.40(0.80)+0.60(0.30)=0.50$. Both positions share this marginal distribution. The equal values reflect the symmetric conditional specification, but they do not establish independence. Independence requires a joint calculation.

**Solution, step 2: Average conditional joint probabilities.** Conditional independence gives two-pass probabilities $0.80^2=0.64$ under high and $0.30^2=0.09$ under low. Averaging with the condition weights yields $P(\text{two passes})=0.40(0.64)+0.60(0.09)=0.31$. If the marginal pass events were independent, their joint probability would be $0.50^2=0.25$. Because the actual model value is $0.31$, they are dependent before the shared condition is specified.

**Solution, step 3: Form the predictive conditional probability.** The probability that the second trial passes given a first pass is $0.31/0.50=0.62$. A first pass increases the posterior plausibility of the high condition, which also raises the predictive pass probability for the second trial. This is information about a shared condition, not evidence that the first outcome physically causes the second.

**Solution, step 4: Verify the explanation by Bayesian updating.** The joint probability of high and a first pass is $0.40\cdot0.80=0.32$. Dividing by the first-pass probability $0.50$ gives posterior high probability $0.64$ and posterior low probability $0.36$. The updated prediction is $0.64(0.80)+0.36(0.30)=0.62$, agreeing with the joint-ratio calculation. The two computations provide different routes to the same result.

**Solution, step 5: State the two independence conclusions.** Within high, the two outcomes are independent by the given model; within low, they are also independent. Thus they are conditionally independent given the categorical operating condition. They are not marginally independent after that condition is averaged out. The complete marginal table has probabilities $0.31$ for two passes, $0.19$ for pass then fail, $0.19$ for fail then pass, and $0.31$ for two failures. These values sum to one and produce the required one-half marginal probabilities. The table displays clustering of matching outcomes due to the shared condition.

## Sensitivity, checking and responsible probability reports

Conditional and posterior probabilities inherit uncertainty from their inputs. When source weights are estimated, a posterior based on them is not known exactly merely because the division is exact. When likelihoods are uncertain, changing them can materially change an update. A sensitivity analysis varies defensible inputs while keeping the probability model coherent, then shows how the target conditional probability responds. It should not vary unrelated pieces in ways that destroy normalization or imply negative region weights.

For a two-source model with prior target probability $p$ and fixed positive likelihood ratio $r$, the posterior probability is $rp/(1-p+rp)$. This expression reveals the interaction between prior and evidence. For fixed $r$, increasing the prior increases the posterior. For fixed prior strictly between zero and one, increasing the likelihood ratio increases the posterior. When the prior approaches zero while the ratio remains finite, the posterior approaches zero; when the prior approaches one, it approaches one. Evidence strength and starting plausibility both matter.

The model may also be structurally uncertain. A conditional-independence assumption used to multiply likelihoods is not just another numeric parameter. If observations share unmodeled information, the joint likelihood requires another form. A sensitivity analysis over numerical rates cannot by itself validate that structure. One should distinguish uncertain values within a chosen model from uncertainty about whether the chosen model represents the experiment adequately.

Useful computational checks begin with a joint table. Construct joint weights from the forward specification, verify nonnegativity and a total of one, sum marginals, and obtain conditional probabilities by normalizing appropriate rows or columns. This route can independently check a symbolic Bayes calculation. For finite sequential draws, enumeration of labeled paths supplies a different check from a hand-written tree. For a shared-condition model, averaging complete conditional tables checks every marginal and intersection at once.

A simulation should display the exact model target alongside random frequencies. In a Bayes frequency explorer, expected counts can illustrate why the denominator contains flagged records from all sources. Random trial counts can then show sampling variation around those expectations. The interface must distinguish stipulated rates, expected counts and realized counts. A rounded expected count is not an actual observed device, and one simulated frequency is not an exact posterior probability.

Boundary inputs deserve explicit behavior. A prior of zero or one can make odds formulas infinite or degenerate, even though direct joint normalization remains interpretable when the evidence has positive probability. Evidence that has zero probability under every source has an undefined posterior in the elementary model. An implementation should explain that the assumed model makes the observation impossible rather than returning a made-up uniform posterior. These cases are part of numerical correctness, not merely interface polish.

A clear probability report names the target, the information, the selection mechanism and the assumptions supporting the numbers. It distinguishes forward likelihoods from reverse source probabilities, conditional independence from marginal independence, and prediction from causation. It avoids converting an uncertain model output into a claim of certainty. The goal is to communicate what the calculation establishes and the conditions under which it establishes it.

The next unit assigns numerical values to outcomes through random variables and develops probability mass functions, densities and cumulative distribution functions. Conditional thinking will continue to matter: a marginal distribution can mix several conditional laws, a transformation can merge outcomes, and a density at a point is not a point probability. The event-based derivations here provide the foundation for those more compact representations.
