# Unit 1: Experiments, Events, Counting and Probability Models

## Learning aims and the role of a probability model

Probability begins before a number is calculated. A useful analysis identifies an experiment, specifies which outcomes are distinguished, describes the events of interest, and states how probability is assigned. These decisions determine what any later arithmetic means. A correct calculation in the wrong sample space can be more misleading than an obvious arithmetic error because the result may look precise and plausible. This unit develops the language and laws needed to prevent that mistake.

By the end of the unit, the reader should be able to translate an experiment into a finite or continuous sample space, express events with set operations, distinguish an event from its probability, and use counting only when the sampling mechanism justifies equal weighting. The reader should also be able to derive basic probability rules from the axioms, reconstruct overlapping events, and explain why independence requires evidence from a model rather than a visual impression of unrelated events. These skills will support conditional probability and random variables in the following units.

A probability model is a mathematical description of uncertainty. It is not a complete description of the physical world. When a model treats a coin as fair, it assigns equal probability to two recorded outcomes under a stated procedure. The assignment does not assert that every imaginable toss procedure has that property. When a model treats a waiting time as continuous, it idealizes the measurement even though a recorder may display only whole seconds. Good modeling makes these simplifications visible and checks whether they serve the question being asked.

Consider an inspection in which a technician records whether a device passes a specified test. The recorded outcome can be pass or fail. The physical process contains many more details, including temperature, calibration, device history, and the technician's actions. A binary sample space deliberately omits those details. It can answer questions about the pass probability under the modeled conditions, but it cannot by itself answer questions about how temperature changes that probability. Enlarging the model is sometimes necessary; unnecessary detail can also obscure a simple question.

Three objects must stay distinct throughout the book. An outcome is one possible result in the chosen description. An event is a collection of outcomes. A probability is the numerical weight assigned to that collection. Writing that an event equals one half confuses a set with a number. A statement such as the probability of obtaining an even die face equals one half refers to a numerical assignment, while the event itself consists of three faces. This distinction becomes especially valuable when one event can be represented in several ways.

Probability theory studies the consequences of assumptions. Statistical work uses data and design information to assess those assumptions and learn about quantities within them. The two activities interact, but their logical directions differ. Knowing how often a machine failed last month does not automatically specify the probability law for next month. A stability assumption connects past records to future uncertainty. Conversely, a probability model can predict a distribution of failure counts without promising the exact count that will occur. Probability is a disciplined treatment of uncertain outcomes, not a device for turning uncertainty into certainty.

## Experiments, recorded outcomes and sample spaces

An experiment is a procedure whose result is to be recorded. The word does not require a laboratory intervention: drawing a sample, observing a day's rainfall, and following a sequence of software requests can all be modeled as experiments. A random experiment has an outcome that is not fixed in advance within the information and model being used. The term does not imply that the underlying world lacks causes. It identifies the uncertainty relevant to the analysis.

The sample space, denoted by $\Omega$, contains every outcome admitted by the model. A finite sample space contains finitely many outcomes. A countably infinite sample space can be listed in a sequence, as with the number of trials until a first success. An uncountable sample space occurs when a continuous measurement is modeled as a real number in an interval. The choice affects how probabilities are represented. Finite counting arguments are inappropriate for a continuous interval merely because both are called sample spaces.

For two recorded binary trials, a natural ordered sample space is $\{00,01,10,11\}$. Order matters because the first and second trials are distinguished. If only the total number of successes is recorded, the possible records are zero, one, and two. That smaller description merges two ordered outcomes into the record one. Even if the four ordered outcomes are equally likely, the three totals are not: their probabilities are one quarter, one half, and one quarter. Equal probability does not survive an arbitrary change of outcome representation.

This example reveals a general principle. Coarse records receive the combined probability of the detailed outcomes that produce them. The correct procedure is to assign probability at a level supported by the mechanism and then combine weights when records are merged. Counting the number of distinct displayed labels and giving each the same probability skips that step. A screen showing three labels does not imply a one-third probability for each label.

Sampling with and without replacement requires different sample spaces. If one labeled object is drawn from a collection and replaced before a second draw, repeated labels are possible. If it is not replaced, those outcomes disappear. Ordered drawing distinguishes first and second positions. An unordered sample identifies sequences that differ only by order. All three choices change what is being counted. A phrase such as choose two objects is incomplete until the procedure or a defensible mathematical convention makes these choices explicit.

A complete sample space should include outcomes that are inconvenient to the desired conclusion. If a sensor sometimes fails to produce a reading, omitting failure and renormalizing the successful readings changes the experiment to one conditional on a successful reading. That may be useful, but it is a different question. Similarly, an analysis of survey responses that excludes nonresponse cannot describe the full invitation process without an additional model for that excluded result.

The empty set is an event containing no outcomes. The full sample space is an event containing every allowed outcome. A singleton event contains a single outcome. In a finite model with strictly positive weight on every outcome, a singleton has positive probability. In a continuous uniform model, a singleton can have probability zero while still being a member of the sample space. Thus possible and positive-probability are not synonyms across all probability models. The distinction will be developed carefully when distribution functions and densities are introduced.

Sample spaces are descriptions, not uniquely determined truths. One model for selecting a student might use the student's identity as the outcome; another might use the student's department. Both can be appropriate. What matters is whether the probabilities on the department outcomes are obtained by combining the identity probabilities correctly. If departments have unequal sizes and individual students are equally likely, departments are not equally likely. If a department is selected uniformly first and a student is then selected within it, the individual students are generally not equally likely. The recorded labels alone cannot decide between these mechanisms.

Before calculating, write a short model statement. Identify the procedure, the recorded result, the allowed outcomes, and the assumptions about weighting. State whether repeated selection is allowed and whether order is recorded. If the event concerns a sequence, specify when the sequence stops. These statements are part of the mathematical solution. They provide a basis for checking a denominator and make it possible for another person to reproduce the reasoning without guessing what the writer intended.

## Events, set operations and logical translation

An event $A$ is a subset of the sample space. The notation $\omega\in A$ says that outcome $\omega$ satisfies the event's condition. A subset relation $A\subseteq B$ says that every outcome satisfying $A$ also satisfies $B$. Equality of events requires the same outcomes, not merely the same probability. Two different events can receive identical probability while describing different records.

The complement $A^c$ contains outcomes in the sample space that are not in $A$. A complement always depends on the chosen universe. The complement of selecting a physics student may include chemistry and mathematics students in one model, but many additional departments in another. A complement taken against the wrong population is a modeling error. Writing the sample space explicitly avoids silently moving between universes.

The intersection $A\cap B$ contains outcomes satisfying both conditions. The union $A\cup B$ contains outcomes satisfying at least one of them. In probability, the word or normally denotes this inclusive union: an outcome satisfying both conditions remains in the union. If exactly one condition is intended, use a separate event. The symmetric difference $A\triangle B$ is the union of $A\cap B^c$ and $A^c\cap B$, so it excludes the overlap.

The difference $A\setminus B$ means that $A$ occurs while $B$ does not. It can be rewritten as $A\cap B^c$. This form often makes a probability calculation easier because the event is one disjoint part of $A$. If a statement says at least one alarm activates but the temperature alarm does not, translate the words into the appropriate union and complement before using a formula. A brief translation can prevent an entire page of calculations from addressing the wrong event.

Events are disjoint, or mutually exclusive, when their intersection is empty. Disjointness says they cannot occur together under the chosen description. It does not say they are independent. If two disjoint events both have positive probability, the occurrence of one rules out the other, which is strong dependence. Independence is a numerical factorization property introduced below. Treating mutually exclusive as a synonym for independent reverses the intended logic.

Set operations obey familiar laws. Union and intersection are commutative: swapping the order of two events leaves the result unchanged. They are associative: grouping three unions or three intersections differently does not change the result. They are distributive: intersecting an event with a union can be performed by taking the two intersections and then their union. These statements can be checked by asking whether an arbitrary outcome belongs to either side.

For example, an outcome belongs to $A\cap(B\cup C)$ precisely when it is in $A$ and in at least one of $B$ and $C$. That happens precisely when it belongs to $A\cap B$ or to $A\cap C$. This proves the distributive identity without requiring a diagram. A diagram can suggest the result, but an outcome-membership argument establishes it even when a diagram is difficult to draw or has an atypical arrangement.

De Morgan's laws convert complements of compound events:

$$
(A\cup B)^c=A^c\cap B^c,\qquad (A\cap B)^c=A^c\cup B^c.
$$

The first says that neither event occurs exactly when the union fails to occur. The second says that both events fail to occur together if at least one of their conditions fails. The English phrase not both is therefore different from neither. In a two-component system, not both working permits one component to work; neither working permits none. This linguistic difference changes the probability.

For multiple events, exactly one, at least one, at least two, and all are different combinations of intersections and complements. An efficient representation divides the sample space into atoms, meaning disjoint regions defined by the occurrence or nonoccurrence of every event. With three events there are eight possible regions. Every compound event is a union of some of these regions. Assigning weights to the regions makes overlap accounting explicit and provides a useful way to check whether supplied probabilities are mutually consistent.

An atom in this event-based description need not be a singleton outcome. It can contain many detailed outcomes that have the same pattern of event membership. The distinction matters when a region has probability zero or when additional events are later introduced. The atom terminology describes the resolution of the present partition, not necessarily the finest possible description of the experiment.

## Event collections and the probability axioms

In a finite sample space, it is convenient to allow every subset as an event. For a general sample space, probability is defined on an event collection $\mathcal F$ with appropriate closure properties. The collection contains the whole space, contains the complement of each event, and contains a countable union of its events. Such a collection is called a sigma-algebra. This book uses ordinary finite events and measurable sets arising from real-valued measurements; constructing unusual nonmeasurable sets is outside its scope.

The closure conditions serve a practical purpose. If a model assigns a probability to a recorded condition, it should also permit the opposite condition. If it permits a sequence of conditions, it should permit the event that at least one of them occurs. These requirements make the event language compatible with probability laws. They also clarify that the phrase any subset has a probability is an additional convenience of finite models, not a universal definition for every possible sample space.

A probability measure $P$ assigns a number to every event in $\mathcal F$. The axioms are nonnegativity, normalization, and countable additivity. Nonnegativity states that $P(A)\geq0$. Normalization states that $P(\Omega)=1$. Countable additivity states that the probability of a union of pairwise disjoint events equals the sum of their probabilities. Finite additivity follows by making the remaining events in the sequence empty.

The disjointness condition is essential. If two events overlap, adding their probabilities counts the overlap twice. The correction is not a special trick but a consequence of dividing the union into disjoint pieces. The countable condition is also important. A model for a countably infinite waiting time must allow probability to be accumulated over all possible finite stopping times. Finite additivity alone does not supply every limiting identity used in probability theory.

The empty event has probability zero. To see this, write the full space as a disjoint union of itself and the empty event, apply additivity, and subtract the normalized probability of the full space. The complement rule follows by writing the full space as the disjoint union of an event and its complement:

$$
P(A^c)=1-P(A).
$$

This also proves the upper bound $P(A)\leq1$, because the complement has nonnegative probability. Bounds are useful error checks. A numerical answer larger than one cannot be rescued by a persuasive interpretation. It indicates an arithmetic, counting, or modeling failure.

Monotonicity states that if $A\subseteq B$, then $P(A)\leq P(B)$. The proof decomposes $B$ into the disjoint union of $A$ and $B\setminus A$. The second part has nonnegative probability, so the larger set cannot receive less probability. This statement concerns inclusion, not the number of labels used to describe an event. In a nonuniform model, an event with many outcomes can have less probability than a singleton event with a large assigned weight.

The difference rule follows from the same reasoning:

$$
P(A\setminus B)=P(A)-P(A\cap B).
$$

The two-event addition rule is obtained by splitting the union into $A$ and the portion of $B$ outside $A$:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

The correction subtracts one copy of an overlap counted twice in the first two terms. If the events are disjoint, the overlap is empty and the correction vanishes. If one event is contained in the other, the formula reduces to the probability of the larger event. These limiting configurations are quick checks of the identity.

For three events, inclusion–exclusion adds single-event probabilities, subtracts pairwise intersections, and adds the triple intersection. An outcome in all three events was initially counted three times, then subtracted three times, and finally added once. An outcome in exactly two events was counted twice and subtracted once. An outcome in exactly one event was counted once. This outcome-by-outcome reasoning explains the alternating correction pattern rather than asking the reader to memorize signs.

$$
P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C).
$$

The union bound discards overlap corrections and gives an upper bound: the probability of a union is at most the sum of the individual probabilities. The bound may exceed one, in which case normalization supplies the stronger upper bound one. The union bound is useful when intersections are unknown, but it should not be presented as an equality without a disjointness argument.

Two-event overlap probabilities must satisfy

$$
\max\{0,P(A)+P(B)-1\}\leq P(A\cap B)\leq\min\{P(A),P(B)\}.
$$

The upper bound follows from inclusion of the intersection in each event. The lower bound follows from the addition rule and the fact that the union cannot have probability greater than one. These are feasibility bounds, not an estimate of the intersection. Independence, disjointness, or another mechanism would be needed to specify a particular value within them.

Countable additivity also yields continuity for nested events. If events increase by inclusion, the probability of their union is the limit of their probabilities. One proof writes successive newly added portions as disjoint events and applies countable additivity to their union. For decreasing events, take complements and use the increasing result. Because total probability is finite, no extra finite-measure restriction is needed here. These identities help connect finite approximations to infinite sample spaces and later distribution functions.

## Interpretations of probability and their assumptions

The classical approach assigns equal probability to outcomes justified as symmetric or uniformly selected. In a finite sample space with $N$ equally likely outcomes, an event containing $m$ outcomes has probability $m/N$. The familiar favorable-over-total calculation therefore requires two things: correct counting and justified equal weighting. Correct counting alone is insufficient. A biased die has six possible face labels but does not generally give every face probability one sixth.

Symmetry is an argument about the procedure, not merely about the names of outcomes. A random-number program that chooses uniformly from a fixed list supports equal weighting if the algorithm and its implementation do so. A human asked to choose a random digit may prefer certain digits. Renaming the digits does not remove that behavioral mechanism. Whenever a solution invokes equally likely outcomes, it should state the reason or explicitly identify the assumption.

The empirical approach relates probability to frequencies in repeated trials under stable conditions. A recorded relative frequency is the number of occurrences divided by the number of observed trials. It is a property of that dataset. A probability is a property of a model. Connecting them requires assumptions about how trials are generated and whether the relevant mechanism remains stable. Long-run convergence results will be discussed later; they do not make every finite frequency equal to its model probability.

If a modeled fair coin produces twelve heads in twenty trials, the observed head frequency is three fifths while the model probability remains one half. The discrepancy alone does not logically disprove fairness, since such outcomes are allowed by the model. Assessing evidence requires the probability of relevant deviations and a clear inferential question. Replacing the model probability by the observed fraction can be a reasonable estimation step, but it is not a definitional identity.

The subjective approach describes coherent degrees of belief given information. Different analysts can assign different probabilities when they have different information or assumptions. Coherence requires numerical assignments to respect probability laws; the label subjective is not permission to use inconsistent values. A stated probability should identify what information was used, what event it concerns, and how the assignment could be revised when new evidence arrives.

The axiomatic approach abstracts from these interpretations. It specifies mathematical rules for probability assignments and derives their consequences. Classical counts, frequency-based models, and informed beliefs can all be represented within the same axiomatic framework when their assignments satisfy the rules. The framework therefore supplies a common language without claiming that every practical assignment has the same origin or evidential strength.

It is helpful to distinguish model uncertainty from randomness within a model. Suppose an analyst is unsure whether a batch has one of two defect rates. Within either candidate model, individual inspections have modeled random outcomes. Uncertainty about which rate applies is another layer. A mixture model can represent both layers, but only if its weights and conditional mechanisms are stated. Treating one uncertain parameter value as a known constant can understate uncertainty; averaging candidate rates does not always preserve the entire predictive distribution.

Probability values also require a clear reference event. The probability that at least one failure occurs during a week is different from the probability that a randomly selected inspection fails. The first refers to a compound event involving multiple opportunities; the second refers to one opportunity under a selection rule. Both can be meaningful, but their denominators and mechanisms differ. A percentage quoted without its event and reference population is incomplete information.

## Counting finite sample spaces responsibly

The addition principle counts alternatives that are disjoint. If a selection must come from one of two nonoverlapping categories, add the numbers of available choices. If the categories overlap, subtract the overlap. This is the counting counterpart of the probability addition rule. Counting with duplicated labels is particularly dangerous when one physical object is listed in more than one category. The objects, not the category names, determine the actual outcomes.

The multiplication principle counts a sequence of choices when the number of options at each stage is known for every allowed earlier choice. For selecting an ordered pair of distinct objects from $N$ labels, there are $N$ first choices and $N-1$ second choices. With replacement, there are $N$ options at both stages. If the number of second-stage options depends on the first-stage category, split the first-stage cases and sum their separate products. Applying a single product without checking that dependence can overcount or undercount.

The factorial $N!$ counts permutations of $N$ distinct labels. It arises from successively choosing from $N$, then $N-1$, and eventually one option. The number of ordered selections of $r$ distinct labels is $N!/(N-r)!$. An unordered sample of $r$ labels can be placed in $r!$ orders, so dividing by this common multiplicity gives the combination count:

$$
\binom Nr=\frac{N!}{r!(N-r)!},\qquad 0\leq r\leq N.
$$

The division is justified because every unordered sample has exactly the same number of distinct orderings. If labels may repeat or a restriction treats positions differently, that common multiplicity must be reconsidered. A useful derivation always identifies what is being counted before and after the division. Merely seeing an unordered word in a problem is not sufficient reason to divide an arbitrary ordered count by a factorial.

A uniform ordered sample without replacement induces a uniform unordered sample because each subset corresponds to the same number of equally weighted sequences. This gives a mechanism-based justification for combination denominators. It also identifies the limitation: if successive draw probabilities are unequal, the resulting subsets need not be equally likely. Counting subsets still describes possibilities, but their weights must come from the unequal mechanism.

For selections from several groups, products of combination counts specify group compositions. Choosing two labels from one group and one from another creates a product because the selections concern disjoint groups and combine uniquely into a sample. Summing over mutually exclusive compositions then yields an event count. The compositions must exhaust the desired event and must not describe the same sample twice. Recording the number selected from each group is often an efficient way to enforce those requirements.

Complement counting can simplify an at-least-one event. Instead of adding many favorable compositions, subtract the count with none of the desired type from the total count. If a second requirement excludes samples containing only the desired type, subtract those as well when the excluded classes are disjoint. Every subtraction should correspond to a named excluded event. Unexplained arithmetic is difficult to audit and often hides an overlap error.

The pigeonhole principle is a feasibility tool: if more objects are distributed among fewer categories, at least one category contains multiple objects. It does not assign probabilities to the categories. Likewise, a combination count cannot prove independence between group counts. In a fixed-size sample, selecting more members from one group leaves fewer positions for the others. The sample-space restriction itself can create dependence even when individual labels were selected uniformly.

Counting is most reliable when tested on a smaller case that can be enumerated. If a formula for selecting pairs claims ten outcomes from four distinct labels without replacement, writing the six actual unordered pairs exposes the error immediately. Such checks do not replace a general proof, but they help reveal a mistaken interpretation of order or replacement. For the worked questions below, executable enumeration supplies an additional arithmetic check while the written solution explains why the count applies.

## Independence as a property of a probability assignment

Two events are independent when

$$
P(A\cap B)=P(A)P(B).
$$

The definition refers to both the event pair and the probability assignment. The same two subsets of the same finite space can be independent under one weighting and dependent under another. Independence is therefore not visible from a set diagram alone. It also does not mean that the events have no common cause in every causal interpretation. The mathematical definition is a factorization of their joint probability.

If two disjoint events have positive probabilities, their intersection probability is zero while the product is positive. They cannot be independent. If one event has probability zero, the product and intersection probabilities are both zero, so it is independent of every event in this formal sense. These cases reinforce the need to use the equation rather than a vague phrase such as unrelated. Degenerate probabilities deserve explicit handling rather than being discarded as exceptions.

For three events, pairwise independence requires the equation for each pair. Mutual independence additionally requires the triple intersection probability to equal the product of all three probabilities. For a larger collection, mutual independence requires the corresponding factorization for every finite subcollection. A single pairwise check, or even all pairwise checks, cannot establish the full property. The third worked question supplies a finite counterexample that can be audited completely.

Independence of complements follows from the same two-event definition and the difference rule. If $A$ and $B$ are independent, then $P(A\cap B^c)=P(A)-P(A\cap B)=P(A)(1-P(B))$. Thus $A$ and $B^c$ are independent. Applying the argument again gives independence of the two complements. These deductions are valid for the fixed event pair and model; they do not extend to an unstated collection merely because one pair passed a check.

Operational assumptions should precede an independence-based multiplication. Independent draws with replacement can be justified by a modeled procedure that resets the collection and randomizes each new draw independently. Drawing without replacement generally changes later probabilities. Separate physical devices may still share environmental conditions and produce dependent outcomes. The following unit will show how common conditions can create dependence even when outcomes are independent after those conditions are specified.

## Fully worked question 1: A committee and two selection mechanisms

**Question.** A collection contains five distinct physics students, four distinct chemistry students, and three distinct mathematics students. A committee of three distinct students is selected uniformly from all unordered committees. Find the probability that it includes at least one physics student and represents at least two departments. Find the probability that it represents all three departments. Then compare this procedure with selecting one student uniformly within each department. Explain whether the second procedure can be analyzed using the first denominator.

**Solution, step 1: Identify the uniformly weighted outcomes.** There are twelve distinct students. The outcomes are unordered three-student subsets, not department labels and not ordered role assignments. Uniform selection of these subsets gives a denominator of $\binom{12}{3}=220$. The equality of the subset probabilities is an assumption supplied by the question. It could also arise from three sequential uniform draws without replacement followed by discarding the order, because each subset would have six equally weighted orderings.

**Solution, step 2: Count the excluded committees.** A committee with no physics student is drawn entirely from the seven other students, producing $\binom73=35$ outcomes. A committee with at least one physics student but only one represented department must consist entirely of physics students, producing $\binom53=10$ outcomes. The two excluded classes are disjoint. All remaining committees satisfy both requested conditions, so the favorable count is $220-35-10=175$. The required probability is therefore $175/220=35/44$, approximately $0.795455$.

**Solution, step 3: Count the all-department committees directly.** Representation of all three departments in a committee of three requires exactly one student from each. There are five choices for the physics member, four for the chemistry member, and three for the mathematics member. Each choice triple identifies one unique unordered committee. The favorable count is sixty, yielding probability $60/220=3/11$, approximately $0.272727$. This event is a subset of the previous event, and its smaller probability is consistent with monotonicity.

**Solution, step 4: Change the procedure explicitly.** Selecting one student uniformly within each department produces only the sixty all-department committees. Under independent within-department selections, each has probability $1/(5\cdot4\cdot3)=1/60$. Both requested events now have probability one. The procedure is not uniform across all two hundred twenty possible three-student subsets: one hundred sixty of those subsets are impossible under it. Dividing sixty by two hundred twenty would answer the first experiment, not this new one.

**Solution, step 5: Check individual inclusion probabilities.** Under uniform three-student subset selection, a fixed student belongs to $\binom{11}{2}=55$ committees, so the inclusion probability is $55/220=1/4$. Under the one-per-department procedure, a fixed physics student has inclusion probability one fifth, a fixed chemistry student one quarter, and a fixed mathematics student one third. Thus superficially similar descriptions of a random committee can produce different individual weights. The answer is determined by the mechanism, not by the word random alone.

## Fully worked question 2: Reconstructing overlapping events

**Question.** Three recorded events have probabilities $P(A)=0.45$, $P(B)=0.35$, and $P(C)=0.25$. The pairwise intersection probabilities are $P(A\cap B)=0.15$, $P(A\cap C)=0.10$, and $P(B\cap C)=0.08$, while the triple intersection has probability $0.04$. Construct the eight disjoint event regions. Find the probabilities of at least one event, exactly one, exactly two, and none. Determine whether $A$ and $B$ are independent, and explain what the reconstructed regions establish about consistency.

**Solution, step 1: Start with the deepest overlap.** The region in all three events has probability $0.04$. The region in $A$ and $B$ but not $C$ has probability $0.15-0.04=0.11$. Similarly the $A,C$-only region has probability $0.10-0.04=0.06$, and the $B,C$-only region has probability $0.08-0.04=0.04$. Subtracting the triple overlap is necessary because each supplied pair intersection includes it. Treating the pair intersections as pair-only regions would overcount.

**Solution, step 2: Recover the single-event regions.** The $A$-only probability is $0.45-0.11-0.06-0.04=0.24$. The $B$-only probability is $0.35-0.11-0.04-0.04=0.16$. The $C$-only probability is $0.25-0.06-0.04-0.04=0.11$. These three subtractions remove the disjoint portions of each event that also satisfy another event. Every reconstructed value is nonnegative.

**Solution, step 3: Calculate compound events.** Exactly one event has probability $0.24+0.16+0.11=0.51$. Exactly two has probability $0.11+0.06+0.04=0.21$. All three has probability $0.04$. At least one therefore has probability $0.51+0.21+0.04=0.76$. Its complement, none, has probability $0.24$. At least two would have probability $0.21+0.04=0.25$. The disjoint-region method makes clear why the triple region belongs in at least two but not exactly two.

**Solution, step 4: Verify inclusion–exclusion and independence.** Inclusion–exclusion gives $0.45+0.35+0.25-0.15-0.10-0.08+0.04=0.76$, agreeing with the disjoint sum. Independence of $A$ and $B$ would require $0.45\cdot0.35=0.1575$ as their intersection probability. The supplied value is $0.15$, so the pair is dependent in this model. A small numerical difference is still a difference in the stipulated exact values. If the inputs were estimates with uncertainty, a separate statistical question would be needed.

**Solution, step 5: State the consistency result carefully.** The seven nonempty membership regions plus the none region have nonnegative probabilities summing to one. They therefore define a valid finite probability model on eight membership-pattern outcomes that reproduces every supplied probability. This establishes existence of a compatible event model. It does not prove that a particular physical data-generating process has these probabilities, nor does it determine how probability is distributed among finer outcomes within each region. Mathematical feasibility and empirical adequacy are separate claims.

## Fully worked question 3: Pairwise independence does not suffice

**Question.** A model assigns equal probability to the four binary triples $000$, $011$, $101$, and $110$. Let $A$ mean that the first coordinate is one, $B$ that the second coordinate is one, and $C$ that the third coordinate is one. Calculate the single, pair and triple intersection probabilities. Decide whether the events are pairwise independent and mutually independent. Calculate the probability of their union and explain the structural source of the discrepancy.

**Solution, step 1: Identify the event memberships.** Each event contains two of the four equally weighted outcomes. Event $A$ contains $101$ and $110$, event $B$ contains $011$ and $110$, and event $C$ contains $011$ and $101$. Each single-event probability is one half. These are probabilities of sets of triples, not probabilities assigned to a coordinate independently in advance.

**Solution, step 2: Check each pair.** The intersection of $A$ and $B$ contains only $110$, the intersection of $A$ and $C$ only $101$, and the intersection of $B$ and $C$ only $011$. Each has probability one quarter. For each pair, this equals the product of the two single-event probabilities. All three pairs therefore satisfy the definition of independence. This verifies pairwise independence completely, rather than checking just one representative pair.

**Solution, step 3: Check the triple separately.** No allowed triple has all three coordinates equal to one. The triple intersection is empty and has probability zero. Mutual independence would require $P(A\cap B\cap C)=(1/2)^3=1/8$. Because zero differs from one eighth, mutual independence fails. The failure is not an exception to the definition; it demonstrates why the definition includes intersections beyond pairs.

**Solution, step 4: Calculate and interpret the union.** The union contains the three nonzero triples and has probability three quarters. Inclusion–exclusion gives $3(1/2)-3(1/4)+0=3/4$, agreeing with direct counting. The allowed triples always contain an even number of ones. Once two coordinates are known, the third is fixed by this parity constraint. Any pair viewed alone appears independent, but the full triple carries a joint restriction. Pairwise summaries cannot reveal every higher-order relationship.

## Model audit and preparation for the next unit

A probability solution should finish by reconnecting its numerical result to its event and assumptions. Check that the result lies between zero and one, that subset relationships imply correctly ordered probabilities, and that disjoint parts sum to the appropriate total. Verify that every count uses the same distinction between order and replacement. If several event probabilities are supplied, examine whether their overlaps admit nonnegative disjoint-region weights. These checks often detect a problem before any advanced technique is needed.

Numerical enumeration is particularly helpful for finite models, but its interpretation must be limited. An enumeration program checks all outcomes of the encoded sample space. It does not prove that the encoded procedure is the actual selection mechanism. If the code treats every subset uniformly while the real process selects departments first, perfect agreement between code and a combination formula verifies the wrong model. Written assumptions and independent calculations should therefore be reviewed together.

Several misconceptions recur. Equal labels do not imply equal weights. Possibility does not always imply positive probability. Disjointness does not imply independence. Equal event probabilities do not imply equal events. Observed frequency does not equal a stipulated probability by definition. Each misconception replaces a specific mathematical statement with an appealing but incomplete verbal shortcut. The remedy is to return to the experiment, event sets, and probability assignment.

The next unit introduces probabilities after information is given. Conditioning changes the reference collection and renormalizes its probability weights. The set operations and disjoint partitions developed here will make that operation precise. Independence will then receive an information-based interpretation, and Bayes' theorem will organize updates when evidence points back toward possible causes or sources. Those results rest on the same axioms; they do not require a new kind of arithmetic or a departure from coherent probability models.
