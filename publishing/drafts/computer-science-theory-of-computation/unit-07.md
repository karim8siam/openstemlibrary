# Unit 7: Advanced complexity

*Editorial draft; not approved for live publication.*

## Randomized Computation
**Randomized Computation: conceptual explanation**

### Randomized algorithms and error models
A randomized decision algorithm has both an input and internal random bits. Error probability is calculated over the algorithm's random choices for a fixed input, not over an assumed distribution of 'typical' user inputs unless average-case analysis is explicitly chosen. A Monte Carlo algorithm may run within a fixed bound and sometimes give an incorrect answer; a Las Vegas algorithm always gives a correct answer but may have random runtime. Some procedures have one-sided errors, while others can err in either direction.

The complexity class BPP contains languages decidable in polynomial time by randomized algorithms with error probability bounded away from one half, conventionally at most 1/3 for every input. Repetition with independent fresh random bits and majority voting reduces error probability exponentially. If a randomized algorithm has one-sided error p≤1/3 and accepts only on an erroneous positive event, repeating independently and requiring all repeated positives gives an upper bound p^r. For a two-sided-error algorithm, naïvely requiring all accepts does not preserve both yes and no behavior; majority analysis is needed.

A simulator should make its probability assumptions explicit. Drawing an exponentially decaying error-bound curve is useful, but it does not prove independent trials or that a particular deployed algorithm has a 1/3 error bound. Use a deterministic pseudo-random seed for reproducible tests and multiple seeds for empirical exploration. Separate the analytical upper bound, observed error rate, and confidence interval computed from experiments.

### Amplification is not merely repeating an experiment
Suppose a randomized algorithm has two-sided error probability at most 1/3 on every input. Execute it independently r times and take the majority answer. If the input's correct answer is yes, each run answers yes with probability at least 2/3; if the correct answer is no, each run answers no with probability at least 2/3. A concentration bound such as Hoeffding's inequality shows that the probability of the majority being incorrect decreases exponentially with r. The requirement for fresh independent random bits is part of the theorem. Calling one seeded pseudorandom generator repeatedly is an implementation technique whose statistical quality still requires scrutiny.

Do not use the one-sided formula (1/3)^r blindly for two-sided majority voting. That formula applies to an event requiring all r independent failures or to specific one-sided acceptance rules. In the majority setting, multiple combinations of incorrect trial outcomes can produce an erroneous majority. For odd r and independent Bernoulli errors with probability p, the exact majority-error probability is Σ_{j=(r+1)/2}^r choose(r,j)p^j(1−p)^(r−j). At r=3 and p=1/3, the expression is 3(1/9)(2/3)+(1/27)=7/27, which is less than one-third but not 1/27.

To demonstrate empirically, write a small simulator that samples independent Boolean errors at a chosen p and estimates majority error across many repeated experiments. Compare the measured proportion with the exact binomial expression, recording a confidence interval. A Monte Carlo estimate fluctuates; it is neither an exact proof nor a universal error guarantee for an unrelated real-world algorithm.

When explaining BPP, state that the time bound and error guarantee apply uniformly across inputs of each length under the defined random-bit model. Average-case success on a particular benchmark distribution does not establish class membership.

## Hierarchies
**Hierarchies: conceptual explanation**

### Hierarchies and relativization cautions
The deterministic time hierarchy theorem formalizes the intuition that, given suitable constructible time bounds with adequate separation, additional time can decide strictly more languages. Proofs use diagonalization and simulation overhead, not an arbitrary assertion that faster machines are less powerful. A related space hierarchy shows genuine increases in computational power with larger space bounds under corresponding constructibility conditions. Such hierarchy results establish distinctions between some classes, but do not automatically settle nearby open problems such as P versus NP.

An important methodological lesson is that proof techniques can have structural limitations. Relativization asks what happens when all machines in an argument receive access to an external oracle. There exist oracles relative to which P and NP agree and others relative to which they differ. Therefore a proof method that would work unchanged in every oracle world cannot settle P versus NP. This does not prove the conjecture false or true; it rules out an overly broad form of argument.

To teach a hierarchy statement, begin with the exact function assumptions, the type of machine, and the conclusion about language classes. Then explain the diagonal machine's time budgeting and where universal simulation overhead enters. Avoid informal phrases like 'n^2 is faster than n' without quantifying the resource and the asymptotic direction. State what is established and what remains open.

### Hierarchies do not answer unrelated open questions
The deterministic time hierarchy theorem, under suitable time-constructibility and separation assumptions, provides languages solvable with more time that cannot be solved within a smaller bound. The diagonal machine simulates machines that claim to run within the smaller time limit, then changes the selected output on a chosen encoded input while staying within a larger time budget. The construction proves a strict containment for appropriately separated bounds. It does not automatically identify a familiar natural problem in the larger class.

The space hierarchy theorem has a parallel structure involving bounded memory and configuration simulation. Such results show that resource constraints can produce genuine differences in computational ability, but translating them into a proof that P≠NP or that a concrete cryptographic primitive is secure would require additional arguments. P and NP are defined using deterministic and nondeterministic time, not simply two different exponents in deterministic runtime.

Explain relativization carefully: imagine machines that can query an oracle for some set A in one abstract step. Relativized classes P^A and NP^A depend on the oracle. Certain oracles yield equality while others yield inequality, so any proof method that must relativize cannot settle P versus NP in the ordinary world. The result is a limitation of a broad proof technique, not a statement that oracle machines exist as actual physical devices or that one oracle captures the correct answer.

A good student exercise classifies statements as theorems, open problems, or unsupported extrapolations. 'There exists a strict deterministic time hierarchy under appropriate assumptions' is a theorem; 'P≠NP' remains an open problem; 'quantum computers solve all NP-complete problems efficiently' is not a consequence of either theorem.

## Approximation Limits
**Approximation Limits: conceptual explanation**

### Approximation algorithms and hard optimization
Optimization versions of NP-hard problems motivate algorithms that trade exact optimality for provable approximation bounds. For a minimization problem with nonnegative objective, an α-approximation algorithm returns a feasible solution of cost at most α times optimum, with α≥1. For maximization, ratios are conventionally expressed differently; a solution might be guaranteed at least a fraction ρ of optimum with 0<ρ≤1. These inequalities depend on feasible solutions and nonnegative or otherwise appropriately normalized objectives.

In vertex cover, the simple algorithm that repeatedly selects an uncovered edge and includes both endpoints returns at most twice the size of an optimal vertex cover. The selected edges are disjoint as a matching because their endpoints are removed from consideration. Any valid vertex cover must select at least one endpoint from every selected edge, so OPT≥|M|. The algorithm chooses 2|M| vertices, hence cost≤2OPT. This is a concrete proof of an approximation guarantee, not just an empirical observation that it 'seems near optimal'.

A heuristic without a bound can still be useful, but it should not be called an approximation scheme. A PTAS provides a family of polynomial-time algorithms for each fixed accuracy parameter ε, with running time potentially growing sharply as ε shrinks. An FPTAS additionally requires polynomial dependence on 1/ε. When evaluating engineering tools, compare exact solvers, bounded approximations and heuristics on the same instances and report which guarantee each method actually has.

### Approximation ratios with a complete proof
For unweighted vertex cover, repeatedly select any uncovered edge and include both its endpoints. Once selected, remove or mark every edge incident to either endpoint as covered. The selected edges are pairwise disjoint: no later selected edge can share an endpoint with an earlier one because all incident edges have already been covered. These selected edges form a matching M. Any vertex cover, including the optimum, must choose at least one endpoint from each matching edge, so |OPT|≥|M|. The constructed cover contains exactly 2|M| vertices; hence |ALG|≤2|OPT|.

This proof is insensitive to which uncovered edge is chosen. It provides a global worst-case approximation bound, not a guarantee of exact optimality. On a star graph, choosing one leaf-center edge adds both endpoints, while choosing the center alone is optimal; the method attains ratio two when there are many leaves. On a graph consisting of disjoint edges, the algorithm selects both endpoints of every edge, yielding twice the optimum as well. These examples show the guarantee can be tight for the algorithm even though many inputs produce better results.

The corresponding weighted vertex-cover problem requires a different approximation method because counting vertices does not represent total cost. Applying the unweighted proof after assigning large weight to one chosen endpoint can produce an arbitrarily poor weighted ratio. This illustrates how a missing assumption can invalidate a previously correct algorithmic guarantee.

An experiment should compare greedy outputs with exhaustive optimal covers on graphs of very small size. For each graph check feasibility, compute the ratio where OPT>0, and verify no ratio exceeds two. The finite experiment tests implementation; the matching proof establishes the bound for every valid undirected unweighted graph.

## Parameterized Complexity
**Parameterized Complexity: conceptual explanation**

### Parameterized complexity and fixed-parameter tractability
Parameterized complexity studies running time as a function of both overall input size n and a chosen parameter k. A problem is fixed-parameter tractable when it can be solved in f(k)n^c time for computable f and constant c independent of k. This permits an exponential dependence on k while keeping polynomial dependence on n. A runtime such as 2^k n^2 is FPT; n^k is not an FPT bound because the exponent on n depends on k. The distinction matters when k is truly small and n is large.

For vertex cover parameterized by solution size k, pick any uncovered edge (u,v). Every valid vertex cover must contain u or v; branch into two recursive cases, decrementing k. The search tree has at most 2^k leaves, with additional polynomial work at each node. This yields an FPT algorithm. Kernelization can reduce an instance to an equivalent size bounded only by k using safe preprocessing rules. A reduction rule requires an equivalence proof; removing a high-degree vertex merely because it looks influential is not generally a valid argument.

Choose a parameter that matches actual application structure, not simply whatever makes a complexity formula attractive. For instance, treewidth can make some graph problems efficient on tree-like networks, but computing or approximating a useful decomposition has its own cost. Always report parameter values in experiments and test a range of n at fixed k to see whether the predicted separation appears.

### Branching search and the meaning of parameter k
The elementary vertex-cover branching algorithm chooses any remaining edge (u,v), then recursively tries including u or including v while decreasing remaining budget k. The reason this exhausts all feasible covers is that every vertex cover must contain at least one endpoint of every edge. A path in the recursion tree corresponds to a set of selected vertices. If k becomes negative while uncovered edges remain, reject that branch. If no edges remain, accept because all conflict constraints have been covered.

The recurrence T(k)≤2T(k−1)+poly(n) yields O(2^k poly(n)) time for a straightforward implementation. Parameter k is the allowed cover size, not the total number of graph vertices. If k is small, exhaustive branching may be practical even for a large graph; if k grows with n, the exponential factor can dominate. Compare with an O(n^k) brute-force enumeration of all k-subsets, which has an exponent depending on k and therefore is not itself an FPT runtime bound.

Preprocessing can improve the search. If a vertex has degree greater than k, any cover of size at most k must include that vertex: otherwise all its more-than-k neighbors would have to be included. This safe rule decreases k and removes incident edges. The proof depends on simple undirected vertex-cover semantics; do not export it unchanged to arbitrary weighted or directed variants.

For a lab, generate graphs up to twelve vertices, compute the exact answer with full subset enumeration, then compare it against the parameterized branching solver for each k. Invalid-input checks should reject negative k, malformed edges and duplicate vertex identities. Report both node count and recursion-tree size, not just one wall-clock measurement.

## Integrated Case Study and Model Limitations
**Unit synthesis: Advanced complexity.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### Decision-making under explicit guarantees
Imagine a network-monitoring optimizer with a deadline of 100 milliseconds, a requirement to handle large sparse graphs, and tolerance for a solution within a proven factor of two of optimum. A correct design begins with problem formalization: feasible solution, objective, input size, and whether the workload has a useful small parameter. A fast heuristic is not automatically appropriate if the user needs a proof of the approximation ratio. Conversely, a theoretically exact algorithm may miss the deadline on realistic instances even though the inputs are moderate.

Compare three candidate approaches on the same benchmark: a polynomial-time approximation with certified bound, an FPT exact solver for parameter k, and a stochastic heuristic with empirical quality only. Record cost, runtime, memory use, timeout rate and known optimum where available. A benchmark with small inputs can provide useful correctness oracles by exhaustive search. For large inputs where exact optimum is unknown, report upper and lower bounds rather than describing a candidate as optimal.

Include deliberately adversarial instances, not only randomly generated easy inputs. Mathematical worst-case guarantees apply to every valid instance under the model; empirical mean performance applies only to a sampled workload. This final distinction connects randomized algorithms, approximation, parameterization and hierarchy results to honest software evaluation.

### A transparent algorithm-choice report
Imagine solving emergency maintenance routing with constraints on technician availability and travel times. The first step is to formalize the task. A route optimization problem may differ from vertex cover or scheduling even if all involve graphs. If the system must provide a legally or operationally defensible guarantee, a heuristic's plausible route is insufficient evidence for a stated approximation ratio. Select an objective with clear units, define feasibility explicitly, and identify which required constraints are hard and which are optional penalties.

On toy instances, an exact solver can establish optimum values that serve as reference points. On larger instances, compute a feasible solution cost U and a proved lower bound L. For a minimization problem with L>0, the ratio U/L bounds how far the feasible cost might be above optimum, because OPT lies between L and U. If L is loose, the ratio may be pessimistic. Report it as a bound rather than as actual suboptimality. If the objective can be zero or negative, choose an appropriate additive gap or normalized analysis instead.

Randomized search requires careful replication across seeds. Use the same instance set and hardware limits for alternatives. Recording only the best of many stochastic runs while ignoring their total computation budget biases comparisons. Also distinguish approximation guarantee from an observed 95th-percentile quality ratio over a sample distribution.

The final report should recommend a method conditionally: exact FPT search when k is small and the deadline allows; a proved approximation when a guaranteed bound matters; a heuristic when empirical performance and responsive operation take priority, with clear caveats. The formal complexity classes shape expectations but do not substitute for modeling the real task.

### Approximation and randomization notebook
For a randomized Boolean procedure with independent one-sided error probability p≤1/3, calculate (1/3)^r for several r and describe exactly which combined decision rule leads to that product. For two-sided error and majority voting, use the binomial tail rather than reusing the one-sided formula. Design a simulation that shows both the analytical bound and a noisy empirical estimate, with a seeded generator and visible number of trials. A deterministic plotted curve is a prediction under assumptions, not a substitute for sampled randomness.

Prove the factor-two guarantee for unweighted vertex cover using the selected matching. Test it on a star and disjoint edges. Next analyze a parameter-k branching solver: every uncovered edge forces at least one endpoint into a cover, yielding a branching recurrence in k. Compare its exponential dependence on k with a search of all n choose k subsets. Explain the difference between a worst-case approximation guarantee, an exact FPT bound, and observed runtime. These are three distinct kinds of evidence.

### Independent self-check: empirical versus theorem-based evidence
For a randomized trial, state whether error is one-sided or two-sided and whether trial randomness is independent. Choose the correct error-combination formula accordingly. For an approximation algorithm, write the inequality comparing algorithm output to optimum before making any numerical claim. For a parameterized solver, identify parameter k and verify the exponent on overall input size is independent of k. A simulation result may help visualize all three ideas, but only a rigorous condition-by-condition argument can establish the corresponding universal property.

### Worked question: Amplification with independent one-sided error
A one-sided randomized test has false-positive probability at most one-third on each independent trial. If it reports positive only when five trials all report positive, bound its false-positive probability.

**State the formal contract**
On a false instance each trial emits a false positive with probability at most 1/3. With independent fresh random bits, the probability all five do so is at most (1/3)^5.

**Derive the result**
Compute the fraction 1/243, approximately 0.0041152, or 0.4115 percent. The combined rule is appropriate only under the stated one-sided guarantee and acceptance semantics.

**Check the scope and a counterexample**
Without independence or a suitable conditional-error assumption, repeated trials can be perfectly correlated and the joint probability can remain 1/3. The bound is not an empirical error-rate measurement.

**Answer:** At most 1/243 ≈ 0.4115% under the independence assumption.

### Worked question: Prove a vertex-cover approximation bound
A greedy procedure repeatedly chooses any uncovered edge and adds both endpoints to the cover. Prove a factor-two upper bound.

**State the formal contract**
The edges selected by this procedure form a matching, because selecting both endpoints removes all incident uncovered edges before the next edge is chosen.

**Derive the result**
Every vertex cover must include at least one endpoint from every edge in the selected matching. Therefore OPT≥|M|. The algorithm includes exactly two endpoints per selected edge, producing cover size 2|M|≤2OPT.

**Check the scope and a counterexample**
The proof assumes an undirected graph and an unweighted vertex-cover objective. It does not automatically establish the same factor for weighted cover.

**Answer:** The method constructs a valid cover of size at most twice optimum.

### Worked question: Distinguish FPT from XP
Consider two bounds for graph problems parameterized by k: T1(n,k)=2^k n^2 and T2(n,k)=n^k. Which explicitly meets the FPT form?

**State the formal contract**
FPT requires a bound f(k)n^c for computable f and constant c independent of k. The first bound has f(k)=2^k and c=2.

**Derive the result**
The second bound places k in the exponent of n; no constant c independent of k is shown by that formula. It is an example of an XP-style bound, not evidence of fixed-parameter tractability.

**Check the scope and a counterexample**
The claim concerns the displayed algorithms and their bounds, not whether the underlying problem might admit a different FPT algorithm. A slow algorithm does not prove a problem inherently non-FPT.

**Answer:** T1 is explicitly FPT; T2 is only an XP-type bound as given.
